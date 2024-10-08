import sys
import random

def main():
    cl_list = sys.argv[1]
    classlist = []
    for l in open(cl_list, 'r'):
        l = l.strip()
        classlist.append(l)

    random.shuffle(classlist)
    print(classlist[0])

if __name__ == "__main__":
    main()
