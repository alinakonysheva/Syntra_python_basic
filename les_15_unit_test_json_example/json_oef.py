import json

# Opening JSON file
f = open('test_ex.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for k, v in data.items():
    print(k, v)

# Closing file
f.close()