from constant.keys import *
from constant.names import *
from os import getcwd
from os.path import exists
from pathlib import Path
# global paths
path_to_running_script = Path(getcwd())
path_to_project = path_to_running_script.parent
path_to_projects = path_to_project.parent
path_to_home = path_to_projects.parent
# project paths
path_to_project_configure_dir = Path(path_to_project, dir_configure)
path_to_project_constant_dir = Path(path_to_project, dir_constant)
path_to_project_data_dir = Path(path_to_project, dir_data)
path_to_project_logs_dir = Path(path_to_project, dir_logs)
path_to_project_script_dir = Path(path_to_project, dir_script)
path_to_project_setting_dir = Path(path_to_project, dir_setting)
del dir_configure, dir_constant, dir_script, dir_setting
# file paths
path_to_file_json_cache = Path(path_to_project_data_dir, fn_json)
path_to_file_logger_config = Path(path_to_project_setting_dir, fn_logger_config)
path_to_file_logger_output = Path(path_to_project_logs_dir, fn_logger_output)
# save paths to dict and append files at paths
paths = dict()
paths.update(
    {
        global_: {
            run:            path_to_running_script,
            project:        path_to_project,
            projects:       path_to_projects,
            home:           path_to_home},
        project: {
            configure:      path_to_project_configure_dir,
            constant:       path_to_project_constant_dir,
            data:           path_to_project_data_dir,
            logs:           path_to_project_logs_dir,
            script:         path_to_project_script_dir,
            setting:        path_to_project_setting_dir},
        file: {
            json_file:      path_to_file_json_cache,
            yaml_logger_config:  path_to_file_logger_config,
            logger_output:  path_to_file_logger_output
        }
    }
)
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
del path_to_project_configure_dir, path_to_project_constant_dir, path_to_project_script_dir, path_to_project_setting_dir
pass
