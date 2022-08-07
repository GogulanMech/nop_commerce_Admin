import configparser

config = configparser.RawConfigParser()
config.read("Configuration/config.properties")


class Readconfig:
    @staticmethod
    def get_url():
        url = config.get("common info", "baseurl")
        return url

    @staticmethod
    def get_username():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password
