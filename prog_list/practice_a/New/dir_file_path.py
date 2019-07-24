import os

def find_dir_list(root_dir):
    print(os.path.abspath(root_dir))
    for path in os.listdir(root_dir):
        full_path = os.path.join(root_dir, path)
        if os.path.isdir(full_path):
            print(full_path)
            find_dir_list(full_path)

def find_file_list(root_dir):
    for path in os.listdir(root_dir):
        full_path = os.path.join(root_dir, path)
        if os.path.isfile(full_path):
            print(full_path)
        elif os.path.isdir(full_path):
            find_file_list(full_path)


if __name__ == '__main__':
    find_dir_list('../..')
    find_file_list('../')
