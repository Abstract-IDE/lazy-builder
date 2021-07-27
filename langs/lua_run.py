import subprocess

def lua_run(file_name):
    cmd = f"lua {file_name}"
    cmd = "".join(cmd).split()
    subprocess.run(cmd)
