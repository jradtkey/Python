#def print_directory_contents(sPath):

#    for key in variable:
#        pass

'''
This function takes the name of a directory
and prints out the paths files within that
directory as well as any files contained in
contained directories.

This function is similar to os.walk. Please don't
use os.walk in your answer. We are interested in your
ability to work with nested structures.
'''
#    fill_this_in

def print_directory_contents(sPath):
    import os
    dirs = os.listdir( sPath )
    for file in dirs:
        print file
print_directory_contents("/.git/")
