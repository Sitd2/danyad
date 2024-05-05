import copy
import logging
import numpy as np
import pandas as pd
from pathlib import Path

LOGGER = logging.getLogger()


class DataHandlerABS:
    def __init__(self, config_data: dict[str]):
        self.config = copy.deepcopy(config_data)
        self.random_state = self.config.get('random_state')
        self.label_names = self.config.get('label_names')
        self.feature_num = self.config.get('feature_num')
        self.feature_num = self.config.get('feature_cat')

        self._src_path = None
        self._data_folder = None
        self._data_path = None
        self._raw_data = None

    @property
    def src_path(self):
        if self._src_path is None:
            self._src_path = Path('.').absolute().parents[0]
        return self._src_path

    @property
    def data_folder(self):
        if self._data_folder is None:
            data_folder_conf = self.config.get('data_folder')
            data_folder_is_relative = data_folder_conf.get('is_relative')
            data_folder_path = data_folder_conf['path']
            if data_folder_is_relative:
                self._data_folder = self.src_path / data_folder_path
            else:
                self._data_folder = Path(data_folder_path)
        return self._data_folder

    @property
    def data_path(self):
        if self._data_path is None:
            self._data_path = self.data_folder / self.config['data_file_name']
        return self._data_path

    @staticmethod
    def read_data(data_path, sep=';'):
        suffix = data_path
        if suffix == '.csv':
            data = pd.read_csv(data_path, sep=sep)
        elif suffix == '.pickle':
            data = pd.read_pickle(data_path)
        elif suffix == '.xlsx':
            data = pd.read_excel(data_path)
        else:
            data = None
            text = f'Could not read this file with suffix "{suffix}" choose from [".csv", ".pickle", ".xlsx"]'
            LOGGER.exception(f'File suffix error {suffix}')
            raise ValueError(text)
        return data

    @property
    def raw_data(self):
        if self._raw_data is None:
            LOGGER.info(f'Start load data from {self.data_path}')
            self._raw_data = self.read_data(self.data_path)
            LOGGER.info(f'Finished loading data')
        return self._raw_data


class DataHandler(DataHandlerABS):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = None

    @property
    def data(self):
        if self._data is None:
            # ToDo
            self._data = copy.deepcopy(self.raw_data)
        return self._data
