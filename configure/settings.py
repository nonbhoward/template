from common.names import dn_setting
from common.names import fn_log
from common.names import fn_settings
from common.paths import path
from pathlib import Path
import os
import yaml

# read the paths configuration
path_run = Path(os.getcwd())
path_setting = Path(path_run.parent, dn_setting)
path_to_paths_setup = Path(path_setting, fn_settings)
if not os.path.exists(path_to_paths_setup):
    print(f'{path_to_paths_setup} not found')
    exit()
with open(path_to_paths_setup, 'r') as p_cfg:
    paths_configuration = yaml.safe_load(p_cfg)

# read the settings configuration
path_to_settings = Path(path.dirs['project']['setting'], fn_settings)
if not os.path.exists(path_to_settings):
    print(f'{path_to_settings} not found')
    exit()
with open(path_to_settings, 'r') as cfg:
    config = yaml.safe_load(cfg)
del cfg, path_to_settings

# update the logger to use the logging path
config['logger']['handlers']['file'].update(
    filename=Path(path.dirs['project']['logs'], fn_log))
