from constant.paths import path
from json import dumps
from json import loads
from pathlib import Path
import logging
import os
import time
log = logging.getLogger(__name__)


class JsonDataManager:
    def __init__(self, cache_filepath, data_is_json=True):
        """
        a class handling common json file interactions
        :param cache_filepath: the address of the cache file on disk"""
        # init
        project_data_path = path.dirs['project']['data']
        self._filepath = cache_filepath \
            if isinstance(cache_filepath, Path) else Path(project_data_path, cache_filepath)
        self._data = None
        self._data_is_json = data_is_json
        self._cache_able_to_be_read = False
        self._refresh_age_threshold = 600
        # check if cache is readable
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as cache:
                cache_contents = loads(cache.read()) if self.data_is_json else cache.read()
                data_unserialized = cache_contents if cache_contents else None
                self.data = data_unserialized
                self.readable = True if self.data else False
        log.info(f'{self.__class__.__name__} initialized with path {self.filepath}')

    def erase(self):
        """
        delete cache file from system, set class cache data to None
        :return: None
        """
        os.remove(self.filepath)
        self.data = None
        self.readable = False

    def read(self):
        """
        conditions for reading json cache data
        1. cache data not readable, log warning, return None
        2. cache data readable, return ??
        :return: None
        """
        cache_file = self.filepath
        if not self.readable:
            print_and_log(f'cache data is not readable at {cache_file}', level=logging.WARNING)
            return None
        with open(cache_file, 'r') as json_file:
            log.info(f'loading json from file {cache_file}')
            # data_unserialized = loads(json_file.read())
            data_unserialized = json_file.read()
        self.data = data_unserialized

    def write(self, serializable_data):
        """
        :param serializable_data: serializable data to dump to json and write to disk
        :return: None
        """
        data_to_write = dumps(serializable_data) if self.data_is_json else serializable_data
        write_location = self.filepath
        if os.path.exists(write_location):
            log.warning(f'overwriting file at {write_location}')
        with open(write_location, 'w') as file_to_write:
            log.info(f'writing to disk from {file_to_write}')
            file_to_write.write(data_to_write)
            self.data = loads(data_to_write) if self.data_is_json else data_to_write
            self.readable = True

    @property
    def age(self):
        time_create = os.path.getmtime(self.filepath) \
            if os.path.exists(self.filepath) else 0
        time_now = time.time()
        return time_now - time_create

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def data_is_json(self):
        return self._data_is_json

    @property
    def filepath(self):
        return self._filepath

    @property
    def readable(self):
        return self._cache_able_to_be_read

    @readable.setter
    def readable(self, value):
        default_value = False
        value_is_boolean = True if isinstance(value, bool) else False
        if not value_is_boolean:
            log.warning(f'property must be set to type boolean, defaulting to {default_value}')
        self._cache_able_to_be_read = value if value_is_boolean else default_value

    @property
    def refresh_age_threshold(self):
        return self._refresh_age_threshold

    @refresh_age_threshold.setter
    def refresh_age_threshold(self, value):
        default_value = 600  # seconds
        value_is_int = True if isinstance(value, int) else False
        if not value_is_int:
            log.warning(f'property must be set to type int, defaulting to {default_value} minutes')
        self._refresh_age_threshold = value if value_is_int else default_value

    @property
    def stale(self):
        return True if self.age > self.refresh_age_threshold else False


def print_and_log(message, level=logging.INFO):
    print(f'{logging.getLevelName(level)} {message}')
    log.log(level=level, msg=message)
