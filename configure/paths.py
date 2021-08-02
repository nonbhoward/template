from common.names import dn_setting
from common.names import fn_paths_config
from os import getcwd
from os.path import exists
from pathlib import Path
import yaml

# read the configuration
path_run = Path(getcwd())
path_setting = Path(path_run.parent, dn_setting)
path_to_paths_config = Path(path_setting, fn_paths_config)
if not exists(path_to_paths_config):
    print(f'{path_to_paths_config} not found')
    exit()
with open(path_to_paths_config, 'r') as p_cfg:
    paths_config = yaml.safe_load(p_cfg)
del p_cfg, path_to_paths_config
