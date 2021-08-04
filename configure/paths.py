from common.names import fn_paths_config
from pathlib import Path
import os
import yaml

# read the configuration
path_run = Path(os.getcwd())
path_setting = Path(path_run.parent, 'setting')
path_to_paths_config = Path(path_setting, fn_paths_config)
if not os.path.exists(path_to_paths_config):
    print(f'{path_to_paths_config} not found')
    exit()
with open(path_to_paths_config, 'r') as p_cfg:
    paths_configuration = yaml.safe_load(p_cfg)
