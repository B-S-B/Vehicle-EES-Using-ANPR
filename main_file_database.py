import sys
from my_db_other import dbhelper

class vehicle_check:
    def __init__(self):
        #connect to the database
        self.db = dbhelper()
        self.menu()
        
    def menu(self):
        user_input=input("""
                   1.Add the vehical in data base:
                   2.Check if vehicle is already in our database:
                   """)
        if user_input=="1":
            self.register()
                
        elif user_input =="2":
            self.numberplate()
        
        else:
            sys.exit(1000)
            
                       
    def register(self):
        EMP_ID = int(input("Enter the employ id"))
        NAME = input("Enter the owner name")
        PHONE_NO= int(input("Enter the mobile number"))
        VECHICLE_NO = str(input("Enter the vehicle number"))
        
        response = self.db.register(EMP_ID,NAME,PHONE_NO,VECHICLE_NO)
        
        if response:
            print("Registration successful")
        
        else:
            print("Registration faild")
        
        self.menu()
            
  
    def numberplate(self):
        reg_plate=input("Enter the vehicale number plate")
        
        self.db.search(reg_plate)
        



if __name__ =="__main__":
    obj = vehicle_check()
