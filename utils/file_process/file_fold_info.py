import os

def generate_file_tree(root_path):
    file_tree = {}
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            file_path = os.path.relpath(os.path.join(dirpath, filename), root_path)
            file_name, file_ext = os.path.splitext(filename)
            file_info = {
                "File Name": file_name,
                "Extension": file_ext,
                "Path": file_path
            }
            file_tree[file_path] = file_info
    return file_tree
    
def generate_fold_tree(root_path):
            folder_tree = {}
            for dirpath, dirnames, filenames in os.walk(root_path):
                folder_name = os.path.basename(dirpath)
                folder_path = os.path.relpath(dirpath, root_path)
                files = filenames
                parent_directory = os.path.dirname(dirpath)
                folder_tree[folder_name] = {
                    "Folder Path": folder_path,
                    "Files": files,
                    "Parent Directory": parent_directory
                }
            return folder_tree

# root_path = os.path.dirname(os.path.abspath(__file__))
root_path = r"C:\Users\yangzairun\Desktop\河南桦粮机械设备有限公司基础建站资料包--给设计"
# print(generate_fold_tree(root_path))
print(generate_file_tree(root_path))

