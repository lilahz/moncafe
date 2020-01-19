import sys
from DTO import Employee
from DTO import Supplier
from DTO import Product
from DTO import Coffee_stand

from Repository import repo


def main():
    repo.create_table()

    with open(sys.argv[0], 'r') as config_file:
        for line in config_file:
            line = line.strip('\n')
            line = line.replace(' ','').split(',')
            if line[0] == 'E':
                tmp = Employee(int(line[1]), line[2], float(line[3]), int(line[4]))
                repo.Employees.insert(tmp)
            if line[0] == 'S':
                tmp = Supplier(int(line[1]), line[2], line[3])
                repo.Suppliers.insert(tmp)
            if line[0] == 'P':
                tmp = Product(int(line[1]), line[2], float(line[3]))
                repo.Products.insert(tmp)
            if line[0] == 'C':
                tmp = Coffee_stand(line[1], line[2], line[3])
                repo.Coffee_stands.insert(tmp)


if __name__ == "__main__":
    main()
