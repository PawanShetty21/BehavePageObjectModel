from configparser import ConfigParser

'''
config = ConfigParser()
config.read("Config.ini")

print(config.get("basic info", "testURL")) # ("Secition", "key")
print(config.get("locator-loginpage", "username")) # ("Secition", "key")

'''

def readConfig(section, key):
    config = ConfigParser()
    config.read("/Users/admin/PycharmProjects/nopCommerceApp/Configurations/Config.ini")
    return config.get(section, key) # This is like value = config.get(section, key) then return value




