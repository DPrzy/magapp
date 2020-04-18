"""
    required
    limit
    type
"""

def checkRule(object, property, rule):
    interface = object["interface"]
    defs = interface.DEFINITIONS[property]
    if rule == "required":
        return property in object.properties and object.properties[property] != None
    elif rule == "limit":
        