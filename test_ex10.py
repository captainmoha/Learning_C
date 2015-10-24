# script to compile and run a c program with a lot of commandline arguments
import os

# create list of commands and commandline arguments
commands = ["make ex10_arraysOfStrings_looping", "valgrind ./ex10_arraysOfStrings_looping " + " ".join([str(x) for x in range(23690)])]

for command in commands:
	os.system(command)

# program breaks at 23690 commandline arguments