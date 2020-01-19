import os
import sqlite3
from DAO import Employees
from DAO import Suppliers
from DAO import Products
from DAO import Coffee_stands
from DAO import Activities
import atexit


class Repository:
    def __init__(self):
        self._conn = sqlite3.connect('./moncafe.db')
        self.Employees = Employees(self._conn)
        self.Suppliers = Suppliers(self._conn)
        self.Products = Products(self._conn)
        self.Coffee_stands = Coffee_stands(self._conn)
        self.Activities = Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_table(self):
        c = self._conn.cursor()
        c.execute("DROP TABLE IF EXISTS Employees")
        c.execute("DROP TABLE IF EXISTS Suppliers")
        c.execute("DROP TABLE IF EXISTS Products")
        c.execute("DROP TABLE IF EXISTS Coffee_stands")
        c.execute("DROP TABLE IF EXISTS Activities")

        self._conn.executescript("""
        CREATE TABLE Employees (
            id              integer    PRIMARY KEY,
            name            text        NOT NULL,
            salary          text        NOT NULL,
            coffee_stand    integer     REFERENCES Coffee_stands(id)
        );

        CREATE TABLE Suppliers (
            id                  integer     PRIMARY KEY,
            name                text        NOT NULL,
            contact_information text
        );

        CREATE TABLE Products (
            id          integer        PRIMARY KEY,
            description text           NOT NULL, 
            price       real           NOT NULL,
            quantity    integer        NOT NULL
        );

        CREATE TABLE Coffee_stands (
            id                      integer    PRIMARY KEY,
            location                text       NOT NULL,
            number_of_employees     integer 
        );

        CREATE TABLE Activities (
            product_id      integer     REFERENCES Products(id),
            quantity        integer     NOT NULL,
            activator_id    integer     NOT NULL,
            date            date        NOT NULL
        );
    """)


# the repository singleton
repo = Repository()
# atexit.register(repo._close)
