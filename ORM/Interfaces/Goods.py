PROPERTIES = {
    "EanCode": "",
    "Name": "",
    "Weight": 0,
    "Storage_ID": 0,
    "Amount": 0
}

DEFINITIONS = {
    "PK_Goods": {
        "primary_key": True,
        "required": True
    },
    "EanCode": {
        "type": "string",
        "required": True,
        "limit": 13
    },
    "Name": {
        "type": "string",
        "required": True,
        "limit": 50
    },
    "Weight": {
        "type": "int",
        "required": True,
        "limit": -1
    },
    "Storage_ID": {
        "type": "int",
        "required": True
    },
    "Amount": {
        "type": "int",
        "required": True
    }
}