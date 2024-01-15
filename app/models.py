from app import db


class Departments(db.Model):
    Kod_department= db.Column(db.Integer, primary_key=True)
    Department_name = db.Column(db.String(100), nullable=False)
    Department_floor = db.Column(db.Integer, nullable=True)
    Department_phone= db.Column(db.String(25), nullable=True)
    Department_fio = db.Column(db.String(100), nullable=False)

class Employees(db.Model):
    Kod_employee = db.Column(db.Integer, primary_key=True)
    Kod_department = db.Column(db.Integer, db.ForeignKey('departments.Kod_department'))
    Employee_fio = db.Column(db.String(150), nullable=False)
    Employee_post = db.Column(db.String(50), nullable=False)
    Employee_number = db.Column(db.Integer, nullable=False)
    Employee_gender = db.Column(db.String(25), nullable=False)
    Employee_address = db.Column(db.String(100), nullable=True)
    Employee_date  = db.Column(db.String(15),nullable=False)

class Organizations(db.Model):
    Kod_organization = db.Column(db.Integer, primary_key=True)
    Organization_name = db.Column(db.String(100), nullable=False)
    Organization_type = db.Column(db.String(100), nullable=False)
    Organization_country = db.Column(db.String(20), nullable = False)
    Organization_city = db.Column(db.String(20), nullable=False)
    Organization_adress= db.Column(db.String(100), nullable=False)
    Organization_fio = db.Column(db.String(100), nullable=False)

class Contracts(db.Model):
    Kod_contract = db.Column(db.Integer, primary_key=True)
    Kod_organization = db.Column(db.Integer, db.ForeignKey('organizations.Kod_organization'))
    Contract_number = db.Column(db.String(50), nullable=False)
    Contract_date = db.Column(db.String(50), nullable=False)
    Contract_amount = db.Column(db.Numeric(precision=10, scale=2))

class ProjectWorks(db.Model):
    Kod_work = db.Column(db.Integer, primary_key=True)
    Kod_contract = db.Column(db.Integer, db.ForeignKey('contracts.Kod_contract'))
    Kod_department = db.Column(db.Integer, db.ForeignKey('departments.Kod_department'))
    Work_start_date = db.Column(db.String(50), nullable=False)
    Work_end_date = db.Column(db.String(50), nullable=False)