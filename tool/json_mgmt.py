from constant.paths import paths
from json import dumps, loads
from os import remove
from os import walk
from os.path import exists
from pathlib import Path
import logging
log = logging.getLogger(__name__)


class JsonManager:
    def __init__(self):
        self.data_path = paths['project']['data']
        self.cache = paths['file']['json cache']
        log.info(f'{self.__class__.__name__} initialized with path {self.cache}')

    def erase_data(self):
        # get a list of all files in the data path
        data_files = list()
        for root, _, files in walk(self.data_path):
            for file in files:
                data_files.append(Path(root, file))
        # delete each file in the data path
        for data_file in data_files:
            if exists(data_file):
                remove(data_file)

    def read(self, file='') -> dict:
        file = self.cache if not file else file
        if not exists(file):
            log.error(f'error with path {file}')
            log.error(f'path does not exist, exiting')
            exit()
        with open(file, 'r') as jf:
            log.debug(f'loading json from file {file}')
            contents = loads(jf.read())
        return contents

    def write(self, data: dict):
        file_to_write = self.cache
        if exists(file_to_write):
            log.warning(f'overwriting file at {file_to_write}')
        with open(file_to_write, 'w') as ftw:
            ftw.write(dumps(data))

    @property
    def cache(self):
        return self._path_to_data

    @cache.setter
    def cache(self, value):
        self._path_to_data = value
