import shutil,os

# open("templateFolder/entry.js", "wb").write(open("dict/js/entry.js", "rb")

# shutil.copy("templateFolder/entry.js", "dict/entry.js") 

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v")
parser.add_argument("-b")
parser.add_argument("-tableName")
args = parser.parse_args(["-v", "12", "-b", "aaaaa", "-tableName", "BBBBB"])
print(args.v)
print(args.b)
print(args.tableName)