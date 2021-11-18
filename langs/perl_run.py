import subprocess
import display


def perl_run(file_name):
    cmd = f"perl {file_name}"
    cmd = "".join(cmd).split()
    display.print_run()
    subprocess.run(cmd)
