
import os
import json
import re
import time as t
from unittest import result
from secret import prefix
def traverse_folder(path, root_path, level=1, parent_path=None):
    result = {
        "Path": prefix +  os.path.relpath(path, root_path),
        "Name": os.path.basename(path),
        "level": level,
        "children": []
    }

    if parent_path:
        result["level"] = level - len(parent_path.split(os.path.sep))

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path): # 如果是文件夹
            result["type"] = "folder"
            result["children"].append(traverse_folder(item_path, parent_path, level + 1))
        else: # 如果是文件
            result["children"].append({
                "Path": prefix +  os.path.relpath(item_path, root_path),
                "Name": item,
                "type": os.path.splitext(item)[1][1:],
                "level": level + 1,
                "children": []
            })

    return result

def get_tree(target_folder):
    result = traverse_folder(target_folder,root_path=target_folder)
    return json.dumps(result, indent=2,ensure_ascii=False)

def get_tree_as_file(target_folder):
    result = traverse_folder(target_folder,root_path=target_folder)
    # file_name = str(t.time()) + ".json"
    file_name = target_folder.split(os.path.sep)[-1] + ".json"
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)  # Get the absolute file path
    with open(file_path,"w",encoding="utf-8") as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
    print("File saved to: ", file_path)
    return file_path


if __name__ == "__main__":
    target_folder = os.path.dirname(os.path.abspath(__file__))
    # res = get_tree(target_folder)
    # print(res)
    get_tree_as_file(target_folder)