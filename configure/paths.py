from constant.names import dn_setting, fn_config_paths
from os import getcwd
from os.path import exists
from pathlib import Path
import yaml

# read the configuration
path_run = Path(getcwd())
path_setting = Path(path_run.parent, 'setting')
yaml_config = Path(path_setting, fn_config_paths)
if not exists(yaml_config):
    print(f'{yaml_config} not found')
    exit()
with open(yaml_config, 'r') as yc:
    paths_configuration = yaml.safe_load(yc)
del yc, yaml_config
pass
