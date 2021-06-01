from constant.names import fn_json
from constant.paths import paths
from json import dumps, loads
from os import remove, walk
from os.path import exists
from pathlib import Path
import logging
log = logging.getLogger(__name__)


class JsonManager:
    def __init__(self):
        self.project_data = paths['project']['data']
        self.cache = Path(self.project_data, fn_json)
        log.info(f'{self.__class__.__name__} initialized with path {self.cache}')

    def erase_data(self):
        # get a list of all files in the data path
        log.info(f'erasing all files in {self.project_data}')
        data_files = list()
        for root, _, files in walk(self.project_data):
            for file in files:
                file_path = Path(root, file)
                log.info(f'file found : {file_path}')
                data_files.append(file_path)
        # delete each file in the data path
        for data_file in data_files:
            if exists(data_file):
                log.info(f'deleting file {data_file}')
                remove(data_file)

    def read(self, file='') -> dict:
        file = self.cache if not file else file
        if not exists(file):
            log.error(f'exiting program, required path does not exist at {file}')
            exit()
        with open(file, 'r') as jf:
            log.info(f'loading json from file {file}')
            contents = loads(jf.read())
        return contents

    def write(self, data: dict):
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
