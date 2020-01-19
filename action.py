import sys
from DAO import Activity
from Repository import repo


def main():
    with open(sys.args(0), 'r') as action_file:
        for line in action_file:
            line = line.strip('\n')
            line = line.replace(' ', '').split(',')
            tmp = Activity(line[0], line[1], line[2], line[3])
            repo.Activities.insert(tmp)
            if line[1] > 0:
                tmp = repo.Products.find(line[0])
                repo.Products.update(line[0], line[1] + tmp.quantity)
            elif line[1] < 0:
                tmp = repo.Products.find(line[0])
                repo.Products.update(line[0], tmp.quantity - line[1])
