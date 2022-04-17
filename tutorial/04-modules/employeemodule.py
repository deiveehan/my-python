employee = {
    "name": "Deivee",
    "location": "Canada",
    "empId": 118384,
    "skills": ["Kubenretes", "Go lang", "Python", "Spring boot"]
}

def displayEmployeeDetails():
    print("Name of employee: " + employee["name"])
    print("Location: " + employee["location"])
    print("EmpId: " + str(employee["empId"]))
    # print("Skills: " + employee["skills"])

def getEmpId():
    return str(employee["empId"])
