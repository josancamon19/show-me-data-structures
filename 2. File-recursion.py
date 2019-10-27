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
    files_found = []
    for f in os.listdir(path):
        if os.path.isfile(path + f) and f.endswith(suffix):
            files_found.append(path + f)
        else:
            files_found += find_files(suffix, path + f + '/')
    return files_found


if __name__ == '__main__':
    print(find_files('.c', 'testdir/'))
