import configparser
from jproperties import Properties

# config = configparser.RawConfigParser()
# config.read("Configuration/config.properties")


# class Readconfig:
#     @staticmethod
#     def get_url():
#         url = config.get("common info", "baseurl")
#         return url
#
#     @staticmethod
#     def get_username():
#         username = config.get("common info", "username")
#         return username
#
#     @staticmethod
#     def get_password():
#         password = config.get("common info", "password")
#         return password

config = Properties()
with open("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work\\nop_commerce_Admin\\Configuration"
          "\\config.properties", "rb")as configfile:
    config.load(configfile)

class Readconfig:

    @staticmethod
    def get_url():
        url = config.get("baseurl").data
        return url

    @staticmethod
    def get_username():
        username = config.get("username").data
        return username

    @staticmethod
    def get_password():
        password = config.get("password").data
        return password

