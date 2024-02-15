# imports: std
import os
import sys
from typing import Iterator

# imports: non-std

# imports: local

# const
HEADING2 = b"## Generated Todo's"
HRULE = b"---\r\n---"
MD_PATH = "./README.md"
SRC_DIR = "./Src"
ENCODING = sys.getfilesystemencoding()

# global

# main
def main():
    ind_start,ind_end = find_readme_header()
    todo_dict = create_dict()
    with open(MD_PATH,"rb+") as file_obj:
        file_obj.seek(ind_end)
        preserve_content = file_obj.read()
        file_obj.seek(ind_start)
        for key in todo_dict:
            file_obj.write(bytes("### "+key,ENCODING)+b"\r\n")
            for info in todo_dict[key]:
                if info[1].find("# TODO:") != -1:
                    content = info[1].strip().replace("# TODO:",f"- [ ] line #{info[0]}:")
                elif info[1].find("# TODONE:") != -1:
                    content = info[1].strip().replace("# TODONE:",f"- [x] line #{info[0]}:")
                file_obj.write(bytes(content,ENCODING)+b"\r\n")
        file_obj.write(preserve_content)
        file_obj.truncate()


    pass

# code blocks
def find_readme_header() -> tuple[int,int]:
        with open(MD_PATH,"rb+") as file_obj:
            content = file_obj.read()
            if content.find(HEADING2) == -1:
                file_obj.seek(0,2)
                file_obj.write(b"\r\n"+HEADING2+b"\r\n"*4+HRULE)
                file_obj.seek(0)
                content = file_obj.read()
                start_point = content.find(HEADING2) + len(HEADING2) + 4 
            else:
                start_point = content.find(HEADING2) + len(HEADING2) + 2 
            end_point =content.find(HRULE,start_point)
        return (start_point,end_point)

def get_paths() -> list:
    target_pys = []
    for dir_path, _, file_names in os.walk(SRC_DIR):
        for file in file_names:
            if os.path.splitext(file)[1] == ".py":
                path = os.path.normpath(os.path.join(dir_path,file))
                target_pys.append(path)
    return target_pys

def filter_paths(path_list: list) -> Iterator[tuple[str,int,str]]:
    for path in path_list:
        with open(path,'r') as file_obj:
            content_lines = file_obj.readlines()
        for index,line in enumerate(content_lines):
            if line.find("# TODO") != -1:
                yield (path, index, line)
            else:
                yield ("", 0, "")

def create_dict() -> dict:
    todo_dict = {}
    for path, indent, line in filter_paths(get_paths()):
        if path == "":
            continue
        elif not todo_dict.get(path):
            todo_dict[path] = [(indent, line)]
        else:
            todo_dict[path].append((indent,line))
    return todo_dict

if __name__ == '__main__':
    main()

