# streamlitstandlone
Instruction on how to generate standalone streamlit applications using pyinstaller

Make sure you streamlit application can be installed in a venv so that you concretely know what packages and modules are required

Once you have done this, and whilst in the python venv install pyinstaller:

pip install pyinstaller

You will need to slightlly modify your application to provide a streamlit wrapper file to be able to run the application. See the repo for an example of the streamlit wrapper file.

You will also need to slightly modify your application so that it can be run from streamlit from the standalone application. You can do this by:

This is an example build command for pyinstaller to build a standalone streamlit application for windows. You should modify the sections to add your own dependencies:

pyinstaller --onedir --add-data="_your_script_name:." --add-data="_path_to_streamlit_static_directory_in_the_virtual_env>:streamlit/static" --additional-hooks-dir=hooks --copy-metadata streamlit --copy-metadata pydeck --hidden-import=_any_modules_a_build_fails_to_find> --hidden-import=_add_as_many_as_needed> --hidden-import=streamlit.runtime.scriptrunner.magic_funcs --hidden-import=streamlit-options-menu run_streamlit.py

I use the --onedir as I find it much more reliable than --onefile. Everything does not need to be loaded into memory and its still easy to package the resultant app for windows using something like InnoSetup.

Note where you need to add your own input relevant to your environment and project.

Also note the 'hooks' directory which, if you need to use it, should be in the same directory as the script. Sometimes, pyinstaller might not correctly identify all dependencies, especially for more complex packages. You can create a custom hook to ensure all components are bundled. See the hooks script in the repostory for an example of this.


