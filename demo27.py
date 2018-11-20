
'''

File Handling / JSON file

'''

# Normal File Handling

try:

    f = open("sample.txt", "w")
    f.write("This is a sample Entry to the file")

except Exception as e:
    print(e)

finally:
    f.close()


import json
# JSON file Handling
try:

    f = open("sample_json.json", "r")
    data = f.read()
    json_data = json.loads(data)
    print(json_data["name"])
except Exception as e:
    print(e)
finally:
    f.close()
