import subprocess
import display


def python_run(file_name):
    cmd = f"python {file_name}"
    cmd = "".join(cmd).split()
    display.print_run()
    subprocess.run(cmd)
