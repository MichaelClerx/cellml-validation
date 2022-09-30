#!/usr/bin/env python3
#
# Compares the 1.0 and 1.1 model test sets
#
import os


def compare(path1, path2):
    pass


def diff(path1, path2, root):

    paths1, paths2 = os.listdir(path1), os.listdir(path2)
    paths1.sort()
    paths2.sort()
    paths1, paths2 = iter(paths1), iter(paths2)

    def nxt(path, piter):
        p = next(piter)
        while p.endswith('.md') or p.startswith('.'):
            p = next(piter)
        q = os.path.join(path, p)
        r = os.path.relpath(q, root)
        return p, q,r


    try:
        p1, q1, r1 = nxt(path1, paths1)
        p2, q2, r2 = nxt(path2, paths2)

        while True:
            if p1 == p2:
                if os.path.isdir(q1) and os.path.isdir(q2):
                    diff(q1, q2, root)
                elif os.path.isfile(q1) and os.path.isfile(q2):
                    #print('Comparing: ' + p1)
                    compare(p1, p2)
                else:
                    print('File/directory mismatch: ' + r1)
                    print(p1, os.path.isdir(q1), os.path.isdir(q2))

                p1, q1, r1 = nxt(path1, paths1)
                p2, q2, r2 = nxt(path2, paths2)

            elif p1 < p2:
                while p1 < p2:
                    print('Exists only in 1.0: ' + r1)
                    p1, q1, r1 = nxt(path1, paths1)
            else:
                while p2 < p1:
                    print('Exists only in 1.1: ' + r2)
                    p2, q2, r2 = nxt(path2, paths2)

    except StopIteration:
        pass

    for p1 in paths1:
        print('Exists only in 1.0: ' + q1)
    for p2 in paths2:
        print('Exists only in 1.1: ' + q2)



if __name__ == '__main__':

    root1 = os.path.abspath('models_1_0')
    root2 = os.path.abspath('models_1_1')
    rroot = os.path.abspath('')

    diff(root1, root2, rroot)
