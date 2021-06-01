from constant.keys import *
from os import getcwd, walk
from os.path import exists
from pathlib import Path

# global paths
paths = dict()
path_to_running_script = Path(getcwd())
path_to_project = path_to_running_script.parent
path_to_projects = path_to_project.parent
path_to_home = path_to_projects.parent
path_to_root = Path(path_to_home.parts[0])

# define and save the global path root
paths.update({
    global_: {
        run:        path_to_running_script,
        project:    path_to_project,
        projects:   path_to_projects}})

# define other path roots
path_roots = {
    home:       path_to_home,
    project:    path_to_project,
    root:       path_to_root}

# path roots : project, home, and root
for path_name, path_root in path_roots.items():
    paths[path_name] = dict()
    for root_, dirs_, _ in walk(path_root):
        for dir_ in dirs_:
            paths[path_name].update({dir_: Path(root_, dir_)})
        break

# verify paths
for meta, meta_details in paths.items():
    for path_name, path_root in meta_details.items():
        print(f'checking if {meta} path name {path_name} exists at {path_root}')
        if not exists(path_root):
            print(f'expected path does not exist at {path_root}')
            if meta == file:
                continue
            print(f'exiting program')
            exit()
pass
