'''Creates an Employee with an Address'''

# Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Employee, Address

engine = create_engine('sqlite:///employees.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create Employee
rebeccaEmployee = Employee(name = "Rebecca Allen")
session.add(rebeccaEmployee)
session.commit()

# Create Employee
rebeccaAddress = Address(street = "512 Sycamore Road", zip = "02001", employee = rebeccaEmployee)
session.add(rebeccaAddress)
session.commit()

# Read
employees = session.query(Employee).all()
for employee in employees:
	print(employee.name)

# Update
rebecca = session.query(Employee).filter_by(name = "Rebecca Allen").one()
address = session.query(Address).filter_by(employee_id = rebecca.id).one()
address.street = "281 Summer Circle"
address.zip = "00189"
session.add(address)
session.commit()

# Read
addresses = session.query(Address).all()
for address in addresses:
	print(address.street)
	print(address.zip)