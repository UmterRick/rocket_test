import os
import ntpath, posixpath

#  path = input() # example : r"C:\\catalog1\\catalog2\\catalog3"
#  path = r"C:\\catalog1\\catalog2\\catalog3"
test_path = r"/cat1/cat2/cat3/"


def makepath(path: str):
    try:
        path = os.path.normpath(path)
        path = path.split(os.sep)
        if path[0] == '':
            path.pop(0)
    except TypeError:
        pass
    parent = path.pop(0)
    while len(path) != 0:
        try:
            new_dir = path.pop(0)
            my_path = os.path.join(parent, new_dir)
            parent = my_path
            os.mkdir(my_path)
            print(f'Directory {new_dir} was created in {parent}')
        except os.error as err:
            print(err.errno, err)
            if err.errno == 17:
                continue

exists = '/Users/usermac/PycharmProjects/Rocket_test/cat1/cat2/cat3/'
makepath(exists)