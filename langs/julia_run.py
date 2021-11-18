import subprocess
import display

def julia_run(file_name):
    cmd = f"julia {file_name}"
    cmd = "".join(cmd).split()
    display.print_run()
    subprocess.run(cmd)

