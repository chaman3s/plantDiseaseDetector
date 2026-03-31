import sys
import subprocess
import os

VENV_PYTHON = r"venv\Scripts\python.exe"

def groupCmd(a,cmd):
    print(len(a))
    if len(a) >= 3:
        for i in range(2, len(a)):
            cmd[4] = a[i]
            subprocess.run(cmd)

        with open("requirements.txt", "w") as f:
            subprocess.run(
                [VENV_PYTHON, "-m", "pip", "freeze"],
                stdout=f
            )

a = sys.argv

if len(a) > 1 and a[1] == 'i':
    groupCmd(a=a,cmd=[VENV_PYTHON, "-m", "pip", "install",a[2] ])

elif len(a) > 1 and a[1] == 'a':
    os.system("cmd /k venv\\Scripts\\activate")
elif len(a) > 1 and a[1] == 'r':
    subprocess.run([VENV_PYTHON,a[2]])
elif len(a) > 1 and a[1] == 'u':
    groupCmd(a=a,cmd=[VENV_PYTHON, "-m", "pip", "uninstall", a[2],"-y"])
elif len(a) > 1 and a[1] == 'd':
    os.system("uvicorn api.app:app --reload")
    
else : 
    print ("not valid command")
