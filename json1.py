import json

data = '''
{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 333 334 3234"
        },
    "email": {
        "hide": "yes"
        }
}
'''
data_json = json.loads(data)
print("Name:",data_json["name"])
print("Attribute:",data_json["email"]["hide"])