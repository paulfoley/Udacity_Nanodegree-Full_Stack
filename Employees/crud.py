from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from employees import Base, Employee, Address

engine = create_engine('sqlite:///employeeData.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

rebeccaEmployee = Employee(name = "Rebecca Allen")
session.add(rebeccaEmployee)
session.commit()

rebeccaAddress = Address(street = "512 Sycamore Road", zip = "02001", employee = rebeccaEmployee)
session.add(rebeccaAddress)
session.commit()

employees = session.query(Employee).all()
for employee in employees:
	print(employee.name)

rebecca = session.query(Employee).filter_by(name = "Rebecca Allen").one()
address = session.query(Address).filter_by(employee_id = rebecca.id).one()
address.street = "281 Summer Circle"
adresss.zip = "00189"
session.add(address)
session.commit()