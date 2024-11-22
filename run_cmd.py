import subprocess
import os

def runCommand(cmd: str):
    try:
        result = subprocess.run([cmd], shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print("Error:- ",e)
        return None

if __name__ == "__main__":
    res=runCommand("mkdir test")
    if res:
        print("Command Output:", res)
    else:
        print("No output, but the command may have executed successfully.")
    
    