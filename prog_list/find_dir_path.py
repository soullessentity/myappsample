import os
def print_dir_list(root_dir):
    for path in os.listdir(root_dir):
        full_path = os.path.join(root_dir, path)
        if os.path.isdir(full_path):
            print(full_path)
            print_dir_list(full_path)

def print_file_list(root_dir):
    for file in os.listdir(root_dir):
        full_path = os.path.join(root_dir,file)
        if os.path.isfile(full_path):
            print(full_path)
        elif os.path.isdir(full_path):
            print_file_list(full_path)


if __name__ == '__main__':
    print_dir_list('../../Myapp1/dir1')
    print_file_list('../../Myapp1/prog_list')
