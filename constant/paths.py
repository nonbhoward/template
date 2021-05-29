from constant.keys import *
from constant.names import *
from os import getcwd
from os.path import exists
from pathlib import Path
# global paths
path_run = Path(getcwd())
path_project = path_run.parent
path_projects = path_project.parent
path_home = path_projects.parent
# project paths
path_project_configure = Path(path_project, dir_configure)
path_project_constant = Path(path_project, dir_constant)
path_project_script = Path(path_project, dir_script)
path_project_setting = Path(path_project, dir_setting)
del dir_configure, dir_constant, dir_script, dir_setting
# save paths to dict
paths = dict()
paths.update(
    {
        global_: {
            run:          path_run,
            project:      path_project,
            projects:     path_projects,
            home:         path_home},
        project: {
            configure:    path_project_configure,
            constant:     path_project_constant,
            script:       path_project_script,
            setting:      path_project_setting}
    }
)
del path_run, path_project, path_projects, path_home
# verify paths
for meta, meta_details in paths.items():
    for path_name, path in meta_details.items():
        print(f'checking if {meta} path name {path_name} exists')
        if not exists(path):
            print(f'error, path does not exist at {path}')
            exit()
del meta, meta_details, path_name, path
# append files at paths
paths.update(
    {
        file: {
            logger_config: Path(path_project_setting, file_logger_config)
        }
    }
)
del path_project_configure, path_project_constant, path_project_script, path_project_setting
pass
