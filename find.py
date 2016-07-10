#!/usr/bin/python
import os, subprocess
import glob2
import glob


curr_dir = os.getcwd()
def initialize():
    print("current directory: {0}".format(curr_dir))
    init_cmd = "cd {0} && rm -rf testing && mkdir -p testing && touch testing/coverage.xml && echo 'coveragedata' >> testing/coverage.xml".format(curr_dir)
    print("executing: {0}".format(init_cmd))
    exec_cmd = subprocess.Popen(init_cmd, shell=True, stdout=subprocess.PIPE)
    exec_cmd.communicate()

def find_files_with_glob2():
    print "============= USING GLOB2 ==========="
    coverage_results_glob_pattern = os.path.join(curr_dir,'**/testing/*.xml')
    print(coverage_results_glob_pattern)
    coverage_report_filenames = glob2.glob(coverage_results_glob_pattern)
    if len(coverage_report_filenames) > 0:
        print(coverage_report_filenames)
    else:
        print('not found')

def find_files_with_glob():
    print "============= USING GLOB ==========="
    coverage_results_glob_pattern = os.path.join(curr_dir,'*/*/testing/*.xml')
    #coverage_results_glob_pattern = os.path.join('curr_dir','**/testing/*.xml')
    print(coverage_results_glob_pattern)
    coverage_report_filenames = glob.glob(coverage_results_glob_pattern)
    if len(coverage_report_filenames) > 0:
        print(coverage_report_filenames)
    else:
        print '-----'
        print('not found')

if __name__ == '__main__':
    initialize()
    find_files_with_glob()
    find_files_with_glob2()

"""
OUTPUT

current directory: /home/devashish/workspace/shippable/v2/experiments
executing: cd /home/devashish/workspace/shippable/v2/experiments && rm -rf testing && mkdir -p testing && touch testing/coverage.xml && echo 'coveragedata' >> testing/coverage.xml
============= USING GLOB ===========
/home/devashish/workspace/shippable/v2/experiments/*/*/testing/*.xml
-----
not found
============= USING GLOB2 ===========
/home/devashish/workspace/shippable/v2/experiments/**/testing/*.xml
['/home/devashish/workspace/shippable/v2/experiments/testing/coverage.xml']
"""