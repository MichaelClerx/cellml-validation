#!/usr/bin/env python3
#
# Compares the 1.0 and 1.1 model test sets
#
import os


def compare(path1, path2):
    pass


def diff(root1, root2):

    paths1, paths2 = os.listdir(root1), os.listdir(root2)
    paths1.sort()
    paths2.sort()
    paths1, paths2 = iter(paths1), iter(paths2)

    try:
        p2 = next(paths2)
        q2 = os.path.join(root2, p2)

        for p1 in paths1:
            q1 = os.path.join(root1, p1)

            if p1 == p2:
                if os.path.isdir(q1) and os.path.isdir(q2):
                    print('Recursing into: ' + q1)
                    diff(q1, q2)
                elif os.path.isfile(q1) and os.path.isfile(q2):
                    print('Comparing: ' + p1)
                    #compare(p1, p2)
                else:
                    print('File/directory mismatch: ' + q1)
                    print(p1, os.path.isdir(q1), os.path.isdir(q2))

                p2 = next(paths2)
                q2 = os.path.join(root2, p2)

            elif p1 < p2:
                print('Exists only in 1.0: ' + p1)
            else:
                while p2 < p1:
                    print('Exists only in 1.1: ' + p2)
                    p2 = next(paths2)
                q2 = os.path.join(root2, p2)
    except StopIteration:
        pass

    for p1 in paths1:
        print('Exists only in 1.0: ' + p1)
    for p2 in paths2:
        print('Exists only in 1.1: ' + p2)



if __name__ == '__main__':

    root1 = os.path.abspath('models_1_0')
    root2 = os.path.abspath('models_1_1')

    diff(root1, root2)
