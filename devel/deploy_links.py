from constant.paths import path
from os import mkdir, symlink
from os.path import exists
from pathlib import Path

# developer provides a target project name
target_project_name = 'flightcoordinator'  # FIXME, provide a target
source_project_name = 'template'

# construct paths
target_project = Path(path.paths['projects'], target_project_name)
source_project = Path(path.paths['projects'], source_project_name)

# inventory of links to be created
sym_links = dict()
sym_links['relative parts'] = dict()
sym_links['relative parts'].update({
    'configure logger':     ['configure', 'logger.py'],
    'configure paths':      ['configure', 'paths.py'],
    'constant keys':        ['constant', 'keys.py'],
    'constant names':       ['constant', 'names.py'],
    'constant paths':       ['constant', 'paths.py'],
    'data path':            ['data'],
    'devel clean up':       ['devel', 'clean_up.sh'],
    'devel flags':          ['devel', 'flags.py'],
    'log path':             ['logs'],
    'script initialize':    ['script', 'initialize.py'],
    'setting logger':       ['setting', 'logger.yaml'],
    'setting paths':        ['setting', 'paths.yaml'],
    'tool json':            ['tool', 'json_mgmt.py']
})

# build the links
sym_links['links'] = dict()
for link_label, link_parts in sym_links['relative parts'].items():
    # make the parent directory if needed
    target_dir = Path(target_project, link_parts[0])
    if not exists(target_dir):
        mkdir(target_dir)
    source_file = Path(source_project, * link_parts)
    target_file = Path(target_project, * link_parts)
    if not exists(target_file):
        # execute the creation
        symlink(src=source_file, dst=target_file)
