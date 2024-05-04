import copy
import logging


class DataHandler:
    def __init__(self, config_data: dict[str]):
        self.config = copy.deepcopy(config_data)
