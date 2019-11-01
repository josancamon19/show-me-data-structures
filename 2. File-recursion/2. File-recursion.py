import os


def find_files(suffix, path):
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

    if not os.path.isdir(path):
        print("Add a valid directory path")
        return []

    if not suffix or len(suffix) == 0 or suffix.isnumeric():
        print("This is not a valid suffix", str(suffix))
        return []

    files_found = []
    for f in os.listdir(path):
        if os.path.isfile(path + f):
            if f.endswith(suffix):
                files_found.append(path + f)
        else:
            files_found += find_files(suffix, path + f + '/')
    return files_found


if __name__ == '__main__':
    print(find_files('.c', 'testdir/'))  # return all files with .c extension in testdir/
    print(find_files('.h', 'testdir/'))  # return all files with .h extension in testdir/
    print(find_files('.h', 'te'))  # te is not a valid dir
    print(find_files('', 'testdir/'))  # '' suffix is not valid
