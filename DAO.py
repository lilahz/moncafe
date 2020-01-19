from DTO import Employee
from DTO import Supplier
from DTO import Product
from DTO import Coffee_stand
from DTO import Activity


class Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)""",
                           [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name, salary, coffee_stand FROM Employees WHERE id = ?
        """, [employee_id])

        return Employee(*c.fetchone())

    def print(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Employees ORDER BY id
        """)
        result = c.fetchall()

        return result


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)""",
                           [supplier.id, supplier.name, supplier.contact_information])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id, name, contact_information FROM Suppliers WHERE id = ?
            """, [supplier_id])

        return Supplier(*c.fetchone())

    def print(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Suppliers ORDER BY id
        """)
        result = c.fetchall()

        return result


class Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)""",
                           [product.id, product.description, product.price, product.quantity])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id, description, price, quantity FROM Products WHERE id = ?
            """, [id])

        return Product(*c.fetchone())

    def update(self, id, quantity):
        self._conn.execute("""
            UPDATE Products SET quantity=(?) WHERE id=(?)
        """, [quantity, id])

    def print(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Products ORDER BY id
        """)
        result = c.fetchall()

        return result


class Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("""INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)""",
                           [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    # self._conn.commit()

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id, location, number_of_employees FROM Coffee_stands WHERE id = ?
            """, [id])

        return Coffee_stand(*c.fetchone())

    def print(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Coffee_stands ORDER BY id
        """)
        result = c.fetchall()

        return result


class Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activity):
        self._conn.execute("""INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)""",
                           [activity.product_id, activity.quantity, activity.activator_id, activity.date])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT product_id, quantity, activator_id, date FROM Activities WHERE product_id = ?
            """, [id])

        return Activity(*c.fetchone())

    def print(self):
        # TODO: maybe do find_all like in https://www.cs.bgu.ac.il/~spl201/index.php?page=PracticalSession13
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Activities ORDER BY product_id
        """)
        result = c.fetchall()

        return result

    def print_report(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT Employees.name, Employees.salary, Coffee_stands.location FROM Employees JOIN Coffee_stands on 
            Employees.coffee_stand = Coffee_stands.id ORDER BY Employees.name
        """)
        result = c.fetchall()

        return result
