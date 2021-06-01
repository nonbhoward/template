from constant.keys import *
from constant.names import *
from os import getcwd, walk
from os.path import exists
from pathlib import Path
paths = dict()
# global paths
path_to_running_script = Path(getcwd())
path_to_project = path_to_running_script.parent
path_to_projects = path_to_project.parent
path_to_home = path_to_projects.parent
path_to_root = Path(path_to_home.parts[0])
# save paths to dict and append files at paths
paths.update({
        global_: {
            run:                    path_to_running_script,
            project:                path_to_project,
            projects:               path_to_projects}})
# project paths
paths[project] = dict()
for root_, dirs_, _ in walk(path_to_project):
    for dir_ in dirs_:
        paths[project].update({dir_: Path(root_, dir_)})
    break
# home paths
paths[home] = dict()
for root_, dirs_, _ in walk(path_to_home):
    for dir_ in dirs_:
        paths[home].update({dir_: Path(root_, dir_)})
    break
# root paths
paths[root] = dict()
for root_, dirs_, _ in walk(path_to_root):
    for dir_ in dirs_:
        paths[root].update({dir_: Path(root_, dir_)})
    break
# file paths
path_to_file_json_cache = Path(paths['project']['data'], fn_json)
path_to_file_logger_config = Path(paths['project']['setting'], fn_logger_config)
path_to_file_logger_output = Path(paths['project']['logs'], fn_logger_output)
paths.update({
    file: {
        json_file: path_to_file_json_cache,
        yaml_logger_config: path_to_file_logger_config,
        logger_output: path_to_file_logger_output}})
del path_to_running_script, path_to_project, path_to_projects, path_to_home
# verify paths
for meta, meta_details in paths.items():
    for path_name, path in meta_details.items():
        print(f'checking if {meta} path name {path_name} exists at {path}')
        if not exists(path):
            print(f'expected path does not exist at {path}')
            if meta == file:
                continue
            print(f'exiting program')
            exit()
del meta, meta_details, path_name, path
pass
