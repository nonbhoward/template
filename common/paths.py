from configure.paths import paths_config
from common.keys import home
from common.keys import project
from common.keys import projects
from common.keys import root
from common.keys import script
from pathlib import Path
import os


class Paths:
    def __init__(self, configuration):
        self.configuration = configuration
        # dicts
        self._dirs = dict()
        self._paths = dict()

    # interface
    @property
    def configuration(self) -> dict:
        return self._configuration

    @configuration.setter
    def configuration(self, value):
        self._configuration = value

    @property
    def dirs(self) -> dict:
        return self._dirs

    @dirs.setter
    def dirs(self, value):
        self._dirs = value

    @property
    def paths(self):
        return self._paths

    @paths.setter
    def paths(self, value):
        self._paths = coerce_path_(value) if not isinstance(value, Path) else value

    # protected
    @property
    def _home(self) -> Path:
        return self.paths[home]

    @_home.setter
    def _home(self, value):
        self.paths[home] = value

    @property
    def _project(self) -> Path:
        return self.paths[project]

    @_project.setter
    def _project(self, value):
        self.paths[project] = value

    @property
    def _projects(self) -> Path:
        return self.paths[projects]

    @_projects.setter
    def _projects(self, value):
        self.paths[projects] = value

    @property
    def _root(self) -> Path:
        return self.paths[root]

    @_root.setter
    def _root(self, value):
        self.paths[root] = value

    @property
    def _script(self) -> Path:
        return self.paths[script]

    @_script.setter
    def _script(self, value):
        self.paths[script] = value


def coerce_path_(value):
    print(f'warning, value \'{value}\' not of type Path')
    try:
        value = Path(value)
    except Exception as exc:
        print(f'unable to construct Path from {value}')
        for arg in exc.args[0]:
            print(arg)
        exit()
    return value


# global paths
path = Paths(paths_config)
path.paths[script] = Path(os.getcwd())
path.paths[project] = path.paths[script].parent
path.paths[projects] = path.paths[project].parent
path.paths[home] = path.paths[projects].parent
path.paths[root] = Path(path.paths[home].parts[0])


# populate files with enabled roots
for path_key, path_root in path.paths.items():
    # exclude non paths, exclude non-enabled (toggle via yaml)
    if not isinstance(path_root, Path):
        print(f'warning, {path_root} not of type Path')
        continue
    if path_key not in path.configuration['enabled roots']:
        print(f'warning, {path_key} is not enabled')
        continue
    # init a new files parent container
    path.dirs[path_key] = dict()
    for root_, dirs_, _ in os.walk(path_root):
        for dir_ in dirs_:
            path.dirs[path_key].update({dir_: Path(root_, dir_)})
        break


# verify paths
for path_key, path_root in path.paths.items():
    print(f'checking if {path_key} exists at {path_root}')
    if not os.path.exists(path_root):
        print(f'expected path does not exist at {path_root}')
        print(f'exiting program')
        exit()
