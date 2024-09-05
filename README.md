# streamlitstandlone
Instruction on how to generate standalone streamlit applications using pyinstaller

- Make sure you streamlit application can be installed in a venv so that you concretely know what packages and modules are required

- Once you have done this, and whilst in the python venv install pyinstaller:

<code>pip install pyinstaller</code>

- You will need to slightlly modify your application to provide a streamlit wrapper file to be able to run the application. See the repo for an example of the streamlit wrapper file.

- You will also need to slightly modify your application so that it can be run from streamlit from the standalone application. You can do this by:

- This is an example build command for pyinstaller to build a standalone streamlit application for windows. You should modify the sections to add your own dependencies:

<code>pyinstaller --onedir --add-data="_your_script_name:." --add-data="_path_to_streamlit_static_directory_in_the_virtual_env>:streamlit/static" --additional-hooks-dir=hooks --copy-metadata streamlit --copy-metadata pydeck --hidden-import=_any_modules_a_build_fails_to_find --hidden-import=_add_as_many_as_needed --hidden-import=streamlit.runtime.scriptrunner.magic_funcs --hidden-import=streamlit-options-menu run_streamlit.py</code>

- I use the --onedir as I find it much more reliable than --onefile. Everything does not need to be loaded into memory and its still easy to package the resultant app for windows using something like InnoSetup. Also note where you need to add your own input relevant to your environment and project.

- Also note the 'hooks' directory which, if you need to use it, should be in the same directory as the script. Sometimes, pyinstaller might not correctly identify all dependencies, especially for more complex packages. You can create a custom hook to ensure all components are bundled. See the hooks script in the repostory for an example of this (note that the streamlit file is one I did really have to add to ensure all streamlit components and modules were packaged by pyinstaller).

To bundle an app for Mac there are a few things to note:

- The pyinstaller command stays pretty much the same. I again use --onedir as I just find it works compared to the --onefile which seems to have different types of issues each time.

<code>pyinstaller --onedir --add-data="_your_script_name:." --add-data="path_to_streamlit_static_directory_in_the_virtual_env" --additional-hooks-dir=hooks --copy-metadata streamlit --copy-metadata pydeck --hidden-import=_any_modules_a_build_fails_to_find --hidden-import=_add_as_many_as_needed --hidden-import=streamlit.runtime.scriptrunner.magic_funcs --hidden-import=streamlit-options-menu run_streamlit.py</code>
  
- To be able to distribute the App I used pkgbuild. This does not ship by default with Mac OS and you will need to install the command line version of Xcode to be able to leverage it. To install the tools:

<code>xcode-select --install</code>

- Once installed you can run a command like this to create a Mac package:
  
<code>pkgbuild --root _path_to_streamlit_app_dir --identifier com.AppName.myapp --version 0.1 --install-location /Applications AppName.pkg</code>

- However note that if you intend to distribute the package across the internet ie. it will be downloaded you are going to need to ensure that after the package install, as part of its post install behavour it removes the quarantine flags that are added by MacOS to a file when it is downloaded from the internet. These prevent the app from running. To do this create a directory called 'scripts' in the root of your streamlit app directory (alongside the script) and create a shell script called postinstall in there as such:

<code>#!/bin/bash
# Remove quarantine flag from the installed app
xattr -dr com.apple.quarantine /Applications/myapp
exit 0</code>

- End users who download the App will still need to cntrl-open the App to install it, as its not signed, and you need to temporarily pass Gatekeeper security for the App install, but once installed the App just needs to be double clicked from the App directory and it will launch a terminal window that launches the web server and the streamlist web app will fire up.



