import subprocess

def zsh_run(file_name):
    cmd = f"python {file_name}"
    cmd = "".join(cmd).split()
    subprocess.run(cmd)
