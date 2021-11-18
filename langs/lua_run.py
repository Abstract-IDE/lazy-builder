import subprocess
import display


def lua_run(file_name):
    cmd = f"lua {file_name}"
    cmd = "".join(cmd).split()
    display.print_run()
    subprocess.run(cmd)
