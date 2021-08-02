from configure.settings import config
from common.paths import path
from pathlib import Path
import os
import shutil


source_project_name = config['deployment']['source']
target_project_name = config['deployment']['target']
if not target_project_name:
    print(f'error, no target name provided')
    exit()


# construct paths
source_project = Path(path.paths['projects'], source_project_name)
target_project = Path(path.paths['projects'], target_project_name)


# inventory of links to be created
links_to_create = dict(config['deployment']['link at target'])
files_to_copy = dict(config['deployment']['copy to target'])


# build the links
for link_label, link_parts in links_to_create.items():
    # make the parent directory if needed
    target_dir = Path(target_project, link_parts[0])
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    source_file = Path(source_project, * link_parts)
    target_file = Path(target_project, * link_parts)
    if not os.path.exists(target_file):
        # execute the creation
        os.symlink(src=source_file, dst=target_file)


# copy unlinked files
for copy_label, copy_parts in files_to_copy.items():
    # make the parent directory if needed
    target_dir = Path(target_project, copy_parts[0])
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    source_file = Path(source_project, * copy_parts)
    target_file = Path(target_project, * copy_parts)
    if not os.path.exists(target_file):
        # execute the creation
        shutil.copy(src=source_file, dst=target_file)

print(f'link deployment complete')
