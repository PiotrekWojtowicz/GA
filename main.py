import sys

from matrix import spliter
from utilities import checkargs, bcolors

if(not checkargs(sys.argv)):
    print(bcolors.FAIL+"Invalid number of arguments {0} expected {1}".format(len(sys.argv)-1, 1))
    exit(1)

print(spliter(sys.argv[1])[0])



