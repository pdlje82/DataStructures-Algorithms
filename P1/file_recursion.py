import os
import time


def find_files(suffix, path, dir_list=None):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    print('Starting find_files')
    print('current path: ', path)
    file_list = []
    pop_list = []
    srch_results = []

    if dir_list is None:
        dir_list = [path]
        print('dir_list is None')

    tmp_index = len(dir_list)
    dir_list += os.listdir(path)
    print('dir_list after joining:\n', dir_list)

    # create file list
    for i, e in enumerate(dir_list):
        if i >= tmp_index:
            dir_list[i] = os.path.join(path, dir_list[i])
        if os.path.isfile(os.path.join(path, e)):  # if entry is file
            file_list.append(os.path.join(path, e))  # add entry to file list
            pop_list.insert(0, i)  # create pop_index list in reverse order

    # remove files from directory list
    for pop_index in pop_list:  # remove all file entries from directory list
        dir_list.pop(pop_index)
    dir_list.pop(0)
    print('dir_list after removing files and pop(0):\n ', dir_list)

    # add files with correct suffix to search result list
    for e in file_list:
        if e.endswith(suffix):
            srch_results.append(e)
    print('Search results: ', srch_results)
    time.sleep(0.1)
    if len(dir_list) == 0:
        print('end recursion')
        return srch_results
    print('next recursive call')
    print('____________________________________________________________')
    return srch_results + find_files(suffix, dir_list[0], dir_list)



path = '.\\testdir'
suffix = '.c'
srch_results = find_files(suffix, path)

print(srch_results)





# Let us print the files in the directory in which you are running this script
# print (os.listdir("."))
#
# # Let us check if this file is indeed a file!
# print (os.path.isfile("./ex.py"))
#
# # Does the file end with .py?
# print ("./ex.py".endswith(".py"))

# print(os.path.isdir('.'))
#
# print(os.path.isfile('.\\LRU_Cache.py'))
#
# print(os.listdir('.'))

#os.path.join(...)