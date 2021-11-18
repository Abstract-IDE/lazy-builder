import subprocess
import display


def ruby_run(file_name):
    cmd = f"ruby {file_name}"
    cmd = "".join(cmd).split()
    display.print_run()
    subprocess.run(cmd)
