import subprocess
import display


def c_family_exec():
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


def c_family_build():
    cmd = f"gcc -Wall -ggdb {file_name_with_location} -o {file_name_no_extc} -lstdc++ -lm -msse3 -fdiagnostics-generate-patch"
    if output_location != "None":
        cmd = f"gcc -Wall -ggdb {file_name_with_location} -o {output_location}{file_name_no_extc} -lstdc++ -lm -msse3 -fdiagnostics-generate-patch"
    cmd = "".join(cmd).split()

    status = subprocess.run(cmd)

    if  status.returncode == 0:
        display.sucess_msg()
    if status.returncode != 0:
        display.failed_msg()
        exit(1)


def c_family_buildexec():
    c_family_build()
    c_family_exec()


def c_family_run(program_name, conditions, output_loc="None"):
    build, run, build_run = conditions
    global file_name, file_name_no_extc, output_location, file_name_with_location, file_name_no_extc_with_loc
    file_name = program_name.split("/")[-1]
    file_name_no_extc = file_name.split(".")[0]     # getting rid of extension
    file_name_no_extc_with_loc = program_name.split(".")[0]
    file_name_with_location = program_name
    output_location = str(output_loc)

    if run == 1 and build == 0:
        c_family_exec()
    if run == 1 and build == 1:
        c_family_buildexec()
    if build == 1 and run == 0:
        c_family_build()
    if build_run == 1:
        c_family_buildexec()

