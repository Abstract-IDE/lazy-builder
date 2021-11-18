import subprocess
import display


def zsh_run(file_name):
    cmd = f"zsh {file_name}"
    cmd = "".join(cmd).split()
    display.print_run()
    subprocess.run(cmd)
