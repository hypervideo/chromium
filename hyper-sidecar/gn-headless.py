import os,pathlib,sys
root=pathlib.Path(__file__).resolve().parents[1]
os.execv(str(root/"buildtools/linux64/gn"),["gn",*sys.argv[1:],"--root-target=//headless","--root-pattern=//headless:headless_shell"])
