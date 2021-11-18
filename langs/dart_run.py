import subprocess
import display


def dart_run(file_name):
    cmd = f"dart {file_name}"
    cmd = "".join(cmd).split()
    display.print_run()
    subprocess.run(cmd)
