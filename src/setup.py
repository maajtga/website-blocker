import sys
from cx_Freeze import setup, Executable

includefiles = ['icon.png']
includes = []

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}
# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Weblock",
        version = "0.1",
        description = "A Website Blocker",
        options = {"build_exe": {'includes':includes,'include_files':includefiles}},
        executables = [Executable("app.py", base=base)])