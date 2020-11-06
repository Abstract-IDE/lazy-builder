import subprocess

def bash_run(file_name):
    subprocess.run(["clear"])
    print("__________________________________________")
    cmd = f"bash {file_name}"
    cmd = "".join(cmd).split()
    subprocess.run(cmd)

