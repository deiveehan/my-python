import requests
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError
from datetime import date

API_URL = "http://localhost:3000/employees"

class Employee(BaseModel):
    id: Optional[int] = Field(None, alias='id')
    name: str
    dob: date
    age: int
    sex: bool

    class Config:
        from_attributes = True

    def to_serializable_dict(self):
        data = self.dict(by_alias=True)
        if isinstance(data['dob'], date):
            data['dob'] = data['dob'].isoformat()
        return data

# CRUD Operations

def create_employee(employee: Employee) -> Employee:
    response = requests.post(API_URL, json=employee.to_serializable_dict())
    response.raise_for_status()
    return Employee(**response.json())

def get_employee(employee_id: int) -> Employee:
    response = requests.get(f"{API_URL}/{employee_id}")
    response.raise_for_status()
    return Employee(**response.json())

def update_employee(employee_id: int, employee: Employee) -> Employee:
    response = requests.put(f"{API_URL}/{employee_id}", json=employee.to_serializable_dict())
    response.raise_for_status()
    return Employee(**response.json())

def delete_employee(employee_id: int) -> None:
    response = requests.delete(f"{API_URL}/{employee_id}")
    response.raise_for_status()

def get_all_employees() -> List[Employee]:
    response = requests.get(API_URL)
    response.raise_for_status()
    return [Employee(**emp) for emp in response.json()]

# Main Function

def main():
    try:
        # Create an Employee
        new_employee = Employee(name="John Doe", dob="1990-01-01", age=32, sex=True)
        created_employee = create_employee(new_employee)
        print(f"Created Employee: {created_employee}")

        # Get an Employee by ID
        employee = get_employee(created_employee.id)
        print(f"Retrieved Employee: {employee}")

        # Update an Employee
        updated_employee_data = Employee(id=employee.id, name="John Doe Updated", dob="1990-01-01", age=33, sex=True)
        updated_employee = update_employee(employee.id, updated_employee_data)
        print(f"Updated Employee: {updated_employee}")

        # Get All Employees
        all_employees = get_all_employees()
        print(f"All Employees: {all_employees}")

        # Delete an Employee
        delete_employee(employee.id)
        print(f"Deleted Employee with ID: {employee.id}")

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except ValidationError as val_err:
        print(f"Validation error occurred: {val_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    main()
