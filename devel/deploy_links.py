from configure.settings import config
from constant.paths import path
from pathlib import Path
import os

source_project_name = config['link deployment']['source']
target_project_name = config['link deployment']['target']
if not target_project_name:
    print(f'no target name provided')
    exit()

# construct paths
source_project = Path(path.paths['projects'], source_project_name)
target_project = Path(path.paths['projects'], target_project_name)

# inventory of links to be created
relative_symbolic_links = dict(config['link deployment']['relative symbolic links'])

# build the links
for link_label, link_parts in relative_symbolic_links.items():
    # make the parent directory if needed
    target_dir = Path(target_project, link_parts[0])
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    source_file = Path(source_project, * link_parts)
    target_file = Path(target_project, * link_parts)
    if not os.path.exists(target_file):
        # execute the creation
        os.symlink(src=source_file, dst=target_file)
