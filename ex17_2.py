from sys import argv

script, from_file, to_file = argv

with open(from_file) as f: indata = f.read(); with open(to_file, 'w') as f: f.write(indata)
