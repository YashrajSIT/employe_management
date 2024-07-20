from marshmallow import Schema,fields,validate #importing schema,fields,validate from marshmallow
class EmployeeSchema(Schema): # Define a schema for Employee
    id=fields.Int(dump_only=True) # Integer  for employee ID
    name=fields.Str(required=True,validate=validate.Length(min=1)) #String  for employee name, required and minimum length is =1
    department=fields.Str(requires=True,validate=validate.Length(min=1)) #String for department, required and minimum length will be =1
    age=fields.Int(required=True,validate=validate.Range(min=1)) #String for position, required and minimum length is = 1