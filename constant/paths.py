from configure.paths import paths_configuration
from constant.keys import files
from constant.keys import home
from constant.keys import project
from constant.keys import projects
from constant.keys import root
from constant.keys import script
from getpass import getuser
from os import getcwd, walk
from os.path import exists
from pathlib import Path
from sys import platform


class Paths:
    def __init__(self, config):
        self.config = config
        # dicts
        self._config = dict()
        self._files = dict()
        self._paths = dict()

    @property
    def config(self) -> dict:
        return self._config

    @config.setter
    def config(self, value):
        self._config = value

    @property
    def files(self) -> dict:
        return self._files

    @files.setter
    def files(self, value):
        self._files = value

    @property
    def _home(self) -> Path:
        return self.paths[home]

    @_home.setter
    def _home(self, value):
        self.paths[home] = value

    @property
    def paths(self):
        return self._paths

    @paths.setter
    def paths(self, value):
        if not isinstance(value, Path):
            coerce_path_(value)
        self._paths = value

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
    print(f'warning, {value} not of type Path')
    try:
        value = Path(value)
    except TypeError as err:
        print(f'unable to construct Path from {value}')
        for err in err.args:
            print(err)
        exit()


# global paths
paths = Paths(paths_configuration)
paths.paths[script] = Path(getcwd())
paths.paths[project] = paths.paths[script].parent
paths.paths[projects] = paths.paths[project].parent
paths.paths[home] = paths.paths[projects].parent
paths.paths[root] = paths.paths[home].parts[0]


# verify home path integrity before continuing
# TODO REDO

# populate files with enabled roots
for path_key, path_root in paths.paths.items():
    if not isinstance(path_root, Path):
        print(f'warning, {path_root} not of type Path')
        continue
    for root_, dirs_, _ in walk(path_root):
        for dir_ in dirs_:
            paths.files.update({dir_: Path(root_, dir_)})
            # paths[path_key].update({dir_: Path(root_, dir_)})
        break

# verify paths
for meta, meta_details in paths.items():
    if meta is setting:
        continue
    for path_key, path_root in meta_details.items():
        print(f'checking if {meta} path name {path_key} exists at {path_root}')
        if not exists(path_root):
            print(f'expected path does not exist at {path_root}')
            if meta == file:
                continue
            print(f'exiting program')
            exit()
pass
