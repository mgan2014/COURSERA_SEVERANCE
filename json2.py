import json

data = '''
[
{
    "name": "Mason",
    "phone": {
        "type": "local",
        "number": "356 343 7989"
        },
    "email": {
        "hide": "no"
        }
},
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
]
'''
data_json = json.loads(data)
print("count:", len(data_json))
for each_name in data_json:
    print("Name:",each_name["name"])
    print("Attribute:",each_name["email"]["hide"])