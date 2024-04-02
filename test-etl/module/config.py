import configparser
import os


class Config:
    def __init__(self, filename='dev_config.ini'):
        self.config_file_path = os.path.join(os.path.dirname(__file__), '', filename)

    def get_config(self, section):
        config = configparser.ConfigParser()
        filepath = self.config_file_path
        config.read(filepath)
        return config[section]
