# -*- coding: utf-8 -*-

import os
import tempfile
import json

# build filename in OS TEMP dir
filename = os.sep.join([tempfile.gettempdir(), "myjson.json"])

# The data (dict)
person = {
  "name": "Helga",
  "age": 42,
  "city": "Berlin"
}

# write json file
f = open(filename, "w")      # open for write
f.write(json.dumps(person))  # convert dict to json string and write
f.close()                    # close filehandle

# open and read the json file
f = open(filename, "r")      # open for read
content = f.read()           # read file content
f.close()                    # close filehandle

print(content, type(content))

person_from_file = json.loads(content)  # convert json string to dict
print(person_from_file, type(person_from_file))

os.remove(filename)          # remove file
