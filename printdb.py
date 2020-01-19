import sqlite3
from Repository import repo


def main():
    # Print the Activities table
    print("Activities")
    for row in repo.Activities.print():
        print(row)
    # Print the Coffee stands table
    print("Coffee stands")
    for row in repo.Coffee_stands.print():
        print(row)
    # Print the Employees table
    for row in repo.Employees.print():
        print(row)
    # Print the Products table
    for row in repo.Products.print():
        print(row)
    # Print the Suppliers table
    for row in repo.Suppliers.print():
        print(row)

    print()


if __name__ == "__main__":
    main()
