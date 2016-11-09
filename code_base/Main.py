#!/usr/bin/python

import os
import time
import subprocess
import sys
import getopt


#---------Set sys.path for pcat execution---------------------------------------
# Absolute path to pcat
full_path = os.path.abspath(os.path.dirname(sys.argv[0])).split('code_base')[0]
sys.path.append(full_path)
# Walk path and append to sys.path
for root, dirs, files in os.walk(full_path):
    for dir in dirs:
        sys.path.append(os.path.join(root, dir))

from Constants import Constants

def usage():
    print "Usage: %s   <one or more parameters>"  % os.path.basename(__file__)
    print "  Used to initiate test cases."
    print "  Parameters:"
    print "     -F | --function        function_name "
    print "    All tests require a valid function name"



def main(argv):

    if len(sys.argv) == 1:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(
            argv, "hF:C", [
                "help", "function="])

    except getopt.GetoptError:
        usage()
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-F", "--function"):
            l_Test_Function = arg

    ## All different test cases should be mentioned here
    if l_Test_Function == "ytube":
        from ytubeMain import ytubeMain
        l_ytube = ytubeMain()
        l_result = l_ytube.runTest()

    # Print out the result and exit
    if l_result == Constants.SUCCESS:
        print "Test Passed\n"
        sys.exit(Constants.SUCCESS)
    else:
        print "Test Failed\n"
        sys.exit(Constants.FAILED)



if __name__ == "__main__":
    main(sys.argv[1:])


