#! /usr/bin/python3

# ----------------------------------------------------------------------------
# import important module
import argparse
import re                   # regular expression for recognizing file
from pathlib import Path    # required for path
# ----------------------------------------------------------------------------



# ----------------------------------------------------------------------------
parser = argparse.ArgumentParser()
# for Run the program
parser.add_argument("-r", type=int, default=0,
        help="0 or 1, 1 means RUN and 0(default) means don't RUN the program")
# for Build the program
parser.add_argument("-b", type=int, default=0,
        help="0 or 1, 1 means BUILD and 0(default) means don't BUILD the program")
# for Build and Run the program
parser.add_argument("-br", type=int, default=0,
        help="0 or 1, 1 means BUILD and RUN and 0 means don't BUILD and RUN the program")
# for Output/compiled file to specific location we want
parser.add_argument("-o", type=str,
        help='location for output of compiled language (eg. /home/user/folder1/)')
# Program/file Name(which we want to build/run)
parser.add_argument("program_name", metavar='program_name',
        help='File/Program that you want to RUN/BUILD (eg. hello.c, calculate.py, auto.sh)')
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
args = parser.parse_args()
program_name = args.program_name
run = args.r
build = args.b
build_run = args.br
parent_dir = Path(__file__).parent.absolute()
program_dir = Path.cwd()
output_location = args.o
program_name_no_loc = program_name.split("/")[-1]
program_name_safe = f"{program_dir}/{program_name_no_loc}"
# ----------------------------------------------------------------------------



# ----------------------------------------------------------------------------
def analyse_program_extension(file_name):
    """ Analyse Program Name """
    file_extension = re.split('\.', file_name)

    if len(file_extension) == 1 or file_extension[-1] == '':
        return 0
    # returning extension name (eg. from file hello.py, py will be returned )
    return file_extension[-1]
program_extension = analyse_program_extension(program_name)
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
interpreted_language = 0
compiled_language = 0
with open(f"{parent_dir}/lists/compiled_language") as File:
    if str(program_extension) in File.read().split():
        compiled_language = 1
with open(f"{parent_dir}/lists/interpreted_language") as File:
    if str(program_extension) in File.read().split():
        interpreted_language = 1
# ----------------------------------------------------------------------------



# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
#for interpreted language
if interpreted_language and build == 1 or interpreted_language and build_run == 1:
    print("Interpreted Language can't compiled")
if interpreted_language and run == 1:
    if program_extension == "py":
        from langs.python_run import python_run
        python_run(program_name)

    if program_extension == "bash":
        from langs.bash_run import bash_run
        bash_run(program_name)

    if program_extension == "zsh":
        from langs.zsh_run import zsh_run
        zsh_run(program_name)


#for compiled_language language
# build compiled language
if compiled_language:
    if program_extension in ["c", "c++", "cpp", "C", "cxx"]:
        from langs.c_family_run import c_family_run
        c_family_run(program_name_safe, [build, run, build_run], output_location)


    if program_extension == "v":
        from langs.v_run import v_run
        v_run(program_name_safe, [build, run, build_run], output_location)
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
