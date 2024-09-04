import streamlit.web.cli as stcli
import sys
import os

if __name__ == '__main__':
    script_path = os.path.join(os.path.dirname(__file__), "insert_main_script_name")
    sys.argv = ["streamlit", "run", script_path, "--global.developmentMode=false"]
    sys.exit(stcli.main())

