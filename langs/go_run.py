import subprocess
import display


def go_exec():
    cmd = f"{file_name_no_extc_with_loc}"
    if output_location != "None":
        cmd = f"{output_location}{file_name_no_extc}"
    cmd = "".join(cmd).split()

    try:
        display.print_run()
        subprocess.run(cmd)
        print("\n\n")
    except FileNotFoundError:
        print(f"compiled file, {file_name_no_extc_with_loc}, \033[91mnot found")

def go_build():
    cmd = f"go build -o {file_name_no_extc} {file_name_with_location}"
    if output_location != "None":
        cmd = f"go build -o {output_location}{file_name_no_extc} {file_name_with_location}"
    cmd = "".join(cmd).split()

    status = subprocess.run(cmd)

    if  status.returncode == 0:
        display.sucess_msg()
    if status.returncode != 0:
        display.failed_msg()
        exit(1)


def go_buildexec():
    go_build()
    go_exec()


def go_run(program_name, conditions, output_loc="None"):
    build, run, build_run = conditions
    global file_name, file_name_no_extc, output_location, file_name_with_location, file_name_no_extc_with_loc
    file_name = program_name.split("/")[-1]
    file_name_no_extc = file_name.split(".")[0]     # getting rid of extension
    file_name_no_extc_with_loc = program_name.split(".")[0]
    file_name_with_location = program_name
    output_location = str(output_loc)

    if run == 1 and build == 0:
        go_exec()
    if run == 1 and build == 1:
        go_buildexec()
    if build == 1 and run == 0:
        go_build()
    if build_run == 1:
        go_buildexec()

