import os

def dir_path_print(root_dir):
    for path in os.listdir(root_dir):
        full_path = os.path.join(root_dir,path)
        # if path == "dir1":
        if os.path.isdir(full_path):
            print(full_path)
            dir_path_print(full_path)

def file_list(root_dir):
    for path in os.listdir(root_dir):
        full_path = os.path.join(root_dir,path)
        if os.path.isfile(full_path):
            print(full_path)
        elif os.path.isdir(full_path):
            file_list(full_path)


if __name__ == '__main__':
    dir_path_print('../../')
    file_list('../..')