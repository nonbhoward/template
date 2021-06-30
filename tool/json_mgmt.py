from constant.names import fn_json
from constant.paths import path
from json import dumps, loads
from os import remove, walk
from os.path import exists
from pathlib import Path
import logging
log = logging.getLogger(__name__)
data_path = path.dirs['project']['data']
default_cache = Path(path.dirs['project']['data'], fn_json)


class JsonManager:
    def __init__(self, item='', filepath=''):
        """
        :param item: path or data
        :param filepath: optional filepath, use to manage multiple cache in parallel
        """
        jsm = self.__class__.__name__
        # init
        self.cache = filepath if filepath else default_cache
        # startup
        self.data = item if item else None
        try:
            self.data = self.read(item) if is_path_(item) else self.read()
        except Exception as exc:
            for xarg in exc.args:
                log.error(f'{xarg}')
            print(f'error instantiating {jsm}')
        log.info(f'{jsm} initialized with path {self.cache}')

    def clear_cache(self):
        remove(self.cache)
        self._data = ''

    def read(self, file='') -> dict:
        file = self.cache if not file else file
        if not exists(file):
            log.warning(f'required path does not exist at {file}')
            return {}
        with open(file, 'r') as jf:
            log.info(f'loading json from file {file}')
            contents = loads(jf.read())
        return contents

    def write(self, data=''):
        data = data if data else self._data
        file_to_write = self.cache
        if exists(file_to_write):
            log.warning(f'overwriting file at {file_to_write}')
        with open(file_to_write, 'w') as ftw:
            log.info(f'writing to disk from {ftw}')
            ftw.write(dumps(data))

    @property
    def cache(self):
        return self._path_to_data

    @cache.setter
    def cache(self, value):
        self._path_to_data = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        # FIXME can cause excessive writes, re-work (resolved)
        if value is not None:
            self.write(value)
        self._data = value


def is_dict_(item) -> bool:
    return True if isinstance(item, dict) else False


def is_path_(item) -> bool:
    return True if isinstance(item, Path) else False
