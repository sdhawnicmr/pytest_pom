from configparser import ConfigParser

def read_configuration(section, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(section, key)