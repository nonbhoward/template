from constant.keys import *
from constant.names import *
from os import getcwd
from os.path import exists
from pathlib import Path
# global paths
path_to_running_script = Path(getcwd())
path_to_project = path_to_running_script.parent
path_to_projects = path_to_project.parent
# project paths
path_to_project_configure_dir = Path(path_to_project, dir_configure)
path_to_project_constant_dir = Path(path_to_project, dir_constant)
path_to_project_data_dir = Path(path_to_project, dir_data)
path_to_project_logs_dir = Path(path_to_project, dir_logs)
path_to_project_script_dir = Path(path_to_project, dir_script)
path_to_project_setting_dir = Path(path_to_project, dir_setting)
del dir_configure, dir_constant, dir_script, dir_setting
# home paths
path_to_home = path_to_projects.parent
path_to_desktop = Path(path_to_home, dir_desktop)
path_to_documents = Path(path_to_home, dir_documents)
path_to_downloads = Path(path_to_home, dir_downloads)
path_to_music = Path(path_to_home, dir_music)
path_to_pictures = Path(path_to_home, dir_pictures)
path_to_videos = Path(path_to_home, dir_videos)
# root paths
path_to_root = Path(path_to_projects.parts[0])
path_to_dev = Path(path_to_root, dev)
path_to_etc = Path(path_to_root, etc)
path_to_media = Path(path_to_root, media)
path_to_mnt = Path(path_to_root, mnt)
path_to_opt = Path(path_to_root, opt)
path_to_proc = Path(path_to_root, proc)
path_to_snap = Path(path_to_root, snap)
path_to_tmp = Path(path_to_root, tmp)
path_to_usr = Path(path_to_root, usr)
path_to_var = Path(path_to_root, var)
# file paths
path_to_file_json_cache = Path(path_to_project_data_dir, fn_json)
path_to_file_logger_config = Path(path_to_project_setting_dir, fn_logger_config)
path_to_file_logger_output = Path(path_to_project_logs_dir, fn_logger_output)
# save paths to dict and append files at paths
paths = dict()
paths.update(
    {
        global_: {
            run:                    path_to_running_script,
            project:                path_to_project,
            projects:               path_to_projects},
        project: {
            configure:              path_to_project_configure_dir,
            constant:               path_to_project_constant_dir,
            data:                   path_to_project_data_dir,
            logs:                   path_to_project_logs_dir,
            script:                 path_to_project_script_dir,
            setting:                path_to_project_setting_dir},
        home: {
            home:                   path_to_home,
            desktop:                path_to_desktop,
            documents:              path_to_documents,
            downloads:              path_to_downloads,
            music:                  path_to_music,
            pictures:               path_to_pictures,
            videos:                 path_to_videos},
        root: {
            root:                   path_to_root,
            dev:                    path_to_dev,
            etc:                    path_to_etc,
            media:                  path_to_media,
            mnt:                    path_to_mnt,
            opt:                    path_to_opt,
            proc:                   path_to_proc,
            snap:                   path_to_snap,
            tmp:                    path_to_tmp,
            usr:                    path_to_usr,
            var:                    path_to_var},
        file: {
            json_file:              path_to_file_json_cache,
            yaml_logger_config:     path_to_file_logger_config,
            logger_output:          path_to_file_logger_output
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
