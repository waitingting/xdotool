import os
import shutil
from pkgutil import get_data

root_path = "/usr/share/icons/bloom/apps"
root_path = "/usr/share/icons/bloom-classic/apps"
root_path = "/usr/share/icons/Vintage/apps"

def get_list(base_dir):
    files=os.listdir(base_dir)
    us = []
    for file in files:
        if file.endswith(".c"):
            print(file)
        us.append(os.path.join(base_dir, file))
    return us

def copy_icon(source, target):
    icon_sizes = get_list(root_path)
    for icon_size in icon_sizes:
        icon_files = get_list(icon_size)
        source_file = os.path.join(icon_size, source)
        target_file = os.path.join(icon_size, target)
        if source_file in icon_files:
            print(source_file)
            shutil.copyfile(source_file,target_file)

def rm_icon(target):
    icon_sizes = get_list(root_path)
    for icon_size in icon_sizes:
        icon_files = get_list(icon_size)
        target_file = os.path.join(icon_size, target)
        if target_file in icon_files:
            print(target_file)
            os.remove(target_file)


def get_filelist(dir):
    filelist=[]
    for home,dirs,files in os.walk(dir):
        for filename in files:
            if filename.endswith(".c"):
                print(os.path.join(home,filename))
                filelist.append(os.path.join(home,filename))
    return filelist

get_list("/home/uos/workspace/xdotool")
# copy_icon("google-chrome.svg","rpa-robot.svg")
# rm_icon("rpa-robot.svg")
    
    