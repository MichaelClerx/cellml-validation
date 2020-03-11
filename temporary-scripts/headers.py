#
# Add headers to files
#
import os


def scan(root, found=[]):
    for name in os.listdir(root):
        if name in ['.' or '..']:
            continue
        path = os.path.join(root, name)
        if os.path.isdir(path):
            scan(path, found)
        base, ext = os.path.splitext(name)
        if ext == '.cellml':
            found.append(path)
    return found


files = scan('./')

header = (
    '<!-- CellML Test Suite.'
    ' https://github.com/MichaelClerx/cellml-validation -->\n'
)

for path in files:
    with open(path, 'r') as f:
        lines = f.readlines()
    if lines[0].startswith('<?xml'):
        lines = lines[:1] + [header] + lines[1:]
        with open(path, 'w') as f:
            f.writelines(lines)
    else:
        print(path)

