import os
from flask.json import jsonify


def list_files(startpath):
    pathStruct = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        pathStruct.append({'level': level, 'name': os.path.basename(root)})
        # print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            pathStruct.append({'level': level+1, 'name': f})
            # print('{}{}'.format(subindent, f))
        return jsonify({'data': pathStruct})


def autoversion_filter(filename):
    fullpath = os.path.join(os.getcwd(), filename[1:])
    try:
        timestamp = str(os.path.getmtime(fullpath))
    except OSError:
        return filename
    newfilename = "{0}?v={1}".format(filename, timestamp)
    return newfilename