from flask_restful import Resource, reqparse, request
from flask import jsonify
from app.models import Departments, Employees, Organizations, Contracts, ProjectWorks
from app import db


def getUpdate(model_class, *names):
    data_query = model_class.query.all()
    data = []
    if data_query:
        for i in data_query:
            data_item = {}
            for name in names:
                data_item[name] = getattr(i, name)
            data.append(data_item)
        return jsonify(data)
    
def postUpdate(model_class, *names):
    parser = reqparse.RequestParser()
    for name in names:
        parser.add_argument(name)
    args = parser.parse_args()
    if args: 
        item_data = {}
        for name in names:
            item_data[name] = args[name]

        item = model_class(**item_data)
        db.session.add(item)
        db.session.commit()
        return True
    return False

# def deleteUpdate(model_class, name):
#     # parser = reqparse.RequestParser()
#     # parser.add_argument(name)
#     # args = parser.parse_args()
#     # print(args)
#     id = request.args.get('id')
#     item_data={}
#     item_data[name] = id
#     item = model_class.query.filter_by(**item_data).first()
#     db.session.delete(item)
#     db.session.commit()

# def deleteUpdate(model_class, name):
#     id = request.args.get('id')
#     item_data = {name: id}
#     item = model_class.query.filter_by(**item_data).first()

#     if model_class == Departments:
#         Employees.query.filter_by(Kod_department=id).delete()
#         ProjectWorks.query.filter_by(Kod_department=id).delete()

#     elif model_class == Employees:
#         ProjectWorks.query.filter_by(Kod_employee=id).delete()

#     elif model_class == Organizations:
#         Contracts.query.filter_by(Kod_organization=id).delete()

#     elif model_class == Contracts:
#         ProjectWorks.query.filter_by(Kod_contract=id).delete()


#     db.session.delete(item)
#     db.session.commit()

def deleteUpdate(model_class, name):
    id = request.args.get('id')
    item_data = {name: id}
    item = model_class.query.filter_by(**item_data).first()

    if model_class == Departments:
        Employees.query.filter_by(Kod_department=id).delete()
        ProjectWorks.query.filter_by(Kod_department=id).delete()

    # elif model_class == Employees:
    #     # ProjectWorks.query.filter_by(Kod_employee=id).delete()

    elif model_class == Organizations:
        Contracts.query.filter_by(Kod_organization=id).delete()

    elif model_class == Contracts:
        ProjectWorks.query.filter_by(Kod_contract=id).delete()

    elif model_class == ProjectWorks:
        pass

    db.session.delete(item)
    db.session.commit()


def putUpdate(model_class, data, nameIdent):
    kod_department = data.get(nameIdent)
    item = model_class.query.get(kod_department)
    if item and data:
        data.pop(nameIdent, None)
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return True
    return False


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'Hello'}
    
class DepartmentsRespoce(Resource):
    def post(self):
        return postUpdate(Departments,"Department_name", "Department_floor", "Department_phone", "Department_fio")
    def get(self):
        return getUpdate(Departments,"Kod_department", "Department_name", "Department_floor", "Department_phone", "Department_fio")
    def delete(self):
        deleteUpdate(Departments, "Kod_department")
    def put(self):
        data = request.json
        putUpdate(Departments, data, "Kod_department")

class EmployeesResponce(Resource):
    def post(self):
        return postUpdate(Employees,"Kod_department", "Employee_fio", "Employee_post", "Employee_number", "Employee_gender", "Employee_address", "Employee_date")
    def get(self):
        return getUpdate(Employees, "Kod_employee" , "Kod_department", "Employee_fio", "Employee_post", "Employee_number", "Employee_gender", "Employee_address", "Employee_date")
    def delete(self):
        deleteUpdate(Employees, "Kod_employee")
    def put(self):
        data = request.json
        putUpdate(Employees, data, "Kod_employee")

class OrganizationResponce(Resource):
    def post(self):
        return postUpdate(Organizations, "Organization_type", "Organization_name", "Organization_country", "Organization_city", "Organization_adress", "Organization_fio")
    def get(self):
        return getUpdate(Organizations,"Kod_organization","Organization_name", "Organization_type", "Organization_country", "Organization_city", "Organization_adress", "Organization_fio")
    def delete(self):
        deleteUpdate(Organizations, "Kod_organization")
    def put(self):
        data = request.json
        putUpdate(Organizations, data, "Kod_organization")

class ContractResponce(Resource):
    def post(self):
        return postUpdate(Contracts, "Kod_organization", "Contract_number", "Contract_date", "Contract_amount")
    def get(self):
        return getUpdate(Contracts, "Kod_contract", "Kod_organization", "Contract_number", "Contract_date", "Contract_amount")
    def delete(self):
        deleteUpdate(Contracts, "Kod_contract")
    def put(self):
        data = request.json
        putUpdate(Contracts, data, "Kod_contract")

class ProjectWorksResponce(Resource):
    def post(self):
        return postUpdate(ProjectWorks, "Kod_contract", "Kod_department", "Work_start_date", "Work_end_date")
    def get(self):
        return getUpdate(ProjectWorks, "Kod_work", "Kod_contract", "Kod_department", "Work_start_date", "Work_end_date")
    def delete(self):
        deleteUpdate(ProjectWorks, "Kod_work")
    def put(self):
        data = request.json
        putUpdate(ProjectWorks, data, "Kod_work")
    