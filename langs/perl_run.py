import subprocess

def perl_run(file_name):
    subprocess.run(["clear"])
    print("__________________________________________")
    cmd = f"perl {file_name}"
    cmd = "".join(cmd).split()
    subprocess.run(cmd)

