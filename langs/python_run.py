import subprocess

def python_run(file_name):
    subprocess.run(["clear"])
    print("__________________________________________")
    cmd = f"python {file_name}"
    cmd = "".join(cmd).split()
    subprocess.run(cmd)

