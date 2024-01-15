from app import app, db, api
from app.responces import HelloWorld, DepartmentsRespoce, EmployeesResponce, OrganizationResponce, ContractResponce, ProjectWorksResponce


api.add_resource(HelloWorld, '/hello')
api.add_resource(DepartmentsRespoce, '/departments')
api.add_resource(EmployeesResponce, '/employees')
api.add_resource(OrganizationResponce, '/organizations')
api.add_resource(ContractResponce, '/contracts')
api.add_resource(ProjectWorksResponce, '/works')