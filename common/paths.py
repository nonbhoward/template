from configure.paths import paths_configuration
from pathlib import Path
import os


class Paths:
    def __init__(self, paths_configuration_):
        self._configuration = paths_configuration_
        # dicts
        self._dirs = dict()
        self._paths = dict()

    # aggregate attributes
    @property
    def children(self) -> dict:
        return self._dirs

    @children.setter
    def children(self, value):
        self._dirs = value

    @property
    def configuration(self):
        return self._configuration

    # discrete attributes
    @property
    def home(self) -> Path:
        return self._paths['home']

    @home.setter
    def home(self, value):
        self._paths['home'] = value

    @property
    def project(self) -> Path:
        return self._paths['project']

    @project.setter
    def project(self, value):
        self._paths['project'] = value

    @property
    def projects(self) -> Path:
        return self._paths['projects']

    @projects.setter
    def projects(self, value):
        self._paths['projects'] = value

    @property
    def root(self) -> Path:
        return self._paths['root']

    @root.setter
    def root(self, value):
        self._paths['root'] = value

    @property
    def script(self) -> Path:
        return self._paths['script']

    @script.setter
    def script(self, value):
        self._paths['script'] = value


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
    path.children[path_name] = dict()
    for root_, dirs_, _ in os.walk(path_path):
        for dir_ in dirs_:
            path.children[path_name].update({dir_: Path(root_, dir_)})
        break


# verify paths
for path_name, path_path in path_check.items():
    print(f'checking if {path_name} exists at {path_path}')
    if not os.path.exists(path_path):
        print(f'expected path does not exist at {path_path}')
        print(f'exiting program')
        exit()
