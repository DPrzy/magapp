import os
import Rules

db_config = {
    #server address
    "server_name": "",

    #database
    "database_name": "Warehouse",

    #sql login
    "login": "",
    "password": ""
}

CACHE = {
    "OBJECTS": []
}

INTERFACES: {}

for file in os.listdir("./Interfaces"):
    if (file.endswith(".py")):
        fname = file[:-3]
        interfaces[fname] = __import__(fname)

def checkDefinitions(object):
    if object.interface in INTERFACES:
        defs = INTERFACES[object["interface"]].DEFINITIONS
        
        # check if all required fiels are set
        required = {x for x in defs if "required" in x}
        print("Required items:", required)
        if (len(object.properties) < len(required)):
            return False
        for k, v in object.properties.items():
            if k in defs:
                specifics = defs[k]

def create(classname, properties = None):
    if classname in INTERFACES:
        object = {
            "interface": classname
        }
        if properties != None:

