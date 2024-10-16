import sys
import csv

def main():
    paper_presenters = sys.argv[1]
    cl_f = sys.argv[2]

    presenters = set()
    for l in open(paper_presenters, 'r'):
        l = l.strip()
        presenters.add(l)


    in_class = set()
    with open(cl_f, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            in_class.add(row[-1])

    print(presenters - in_class)
    print()
    print(in_class - presenters)
        

if __name__ == "__main__":
    main()
