class emp:

    def __init__(self, name, age, salary): 
        self.name=name
        self.age=age
        self.salary=salary
        return None

    def display_details(self): 
        print(f"name is :  {self.name} \n age: {self.age} \n Sal: {self.salary}")
        return None
    
    def __del__(self): 
        print("Inside a drestructor, object has been deleted")
        return None

emp1=emp("Deivee", 25, 9999)
emp1.display_details()
