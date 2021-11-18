import subprocess
import display

def R_run(file_name):
    cmd = f"Rscript {file_name}"
    cmd = "".join(cmd).split()
    display.print_run()
    subprocess.run(cmd)

