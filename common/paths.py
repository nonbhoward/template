from configure.paths import paths_configuration
from pathlib import Path
import os


class Paths:
    def __init__(self, paths_configuration_):
        self._configuration = paths_configuration_
        # dicts
        self._children = dict()
        self._paths = dict()

    # aggregate attributes
    @property
    def configuration(self):
        return self._configuration

    @property
    def to(self) -> dict:
        return self._children

    # discrete attributes
    @property
    def home(self) -> Path:
        return self._paths['home']

    @property
    def project(self) -> Path:
        return self._paths['project']

    @property
    def projects(self) -> Path:
        return self._paths['projects']

    @property
    def root(self) -> Path:
        return self._paths['root']

    @property
    def script(self) -> Path:
        return self._paths['script']


# global paths
path = Paths(paths_configuration)
setattr(Paths, 'script', Path(os.getcwd()))
setattr(Paths, 'project', path.script.parent)
setattr(Paths, 'projects', path.project.parent)
setattr(Paths, 'home', path.projects.parent)
setattr(Paths, 'root', Path(path.home.parts[0]))


# populate files with enabled roots
path_check = {
    'script':   path.script,
    'project':  path.project,
    'projects': path.projects,
    'home':     path.home,
    'root':     path.root
}

for path_name, path_path in path_check.items():
    # exclude non paths, exclude non-enabled (toggle via yaml)
    if not isinstance(path_path, Path):
        print(f'warning, {path_path} not of type Path')
        continue
    if path_name not in path.configuration['roots']['enabled']:
        print(f'warning, {path_name} is not enabled')
        continue
    # init a new files parent container
    path.to[path_name] = dict()
    for root, directories, _ in os.walk(path_path):
        for directory in directories:
            path.to[path_name].update({directory: Path(root, directory)})
        break  # no recursion


# verify paths, end program on failure
for path_name, path_path in path_check.items():
    print(f'checking if {path_name} exists at {path_path}')
    if not os.path.exists(path_path):
        print(f'expected path does not exist at {path_path}')
        print(f'exiting program')
        exit()
