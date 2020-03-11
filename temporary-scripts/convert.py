#
# Perform XSLT transformations on a directory tree
#
import check
import lxml.etree
import os


n = 0


def convert(root1, root2):

    global n
    if not os.path.isdir(root2):
        os.makedirs(root2)
    for fname in os.listdir(root1):
        path1 = os.path.join(root1, fname)
        path2 = os.path.join(root2, fname)
        if os.path.isdir(path1):
            convert(path1, path2)
        elif os.path.isfile(path1) and os.path.splitext(path1)[1] == '.cellml':
            try:
                print('.', end='')
                if False:
                    check.xslt_1_0_to_1_1(path1, path2)

                    # Fix comments issue
                    with open(path2, 'r') as f:
                        text = f.read()
                    text = text.replace('-->', '-->\n')
                    with open(path2, 'w') as f:
                        f.write(text)

                    # Still changes namespaces and model header
                else:
                    with open(path1, 'r') as f:
                        text = f.read()
                    text = text.replace(
                        'http://www.cellml.org/cellml/1.0#',
                        'http://www.cellml.org/cellml/1.1#')
                    text = text.replace(
                        'CellML 1.0',
                        'CellML 1.1')
                    text = text.replace(
                        '5.4.2',
                        '5.4.3')
                    with open(path2, 'w') as f:
                        f.write(text)

                n += 1

            except lxml.etree.XMLSyntaxError:
                print(f'Unable to convert {path1}: XML error in input file.')


if __name__ == '__main__':
    print('Converting', end='')
    convert('models_1_0', os.path.join('models_1_1', 'converted'))
    print()
    print(f'Converted {n} files.')
