from Main import *

#test all classes and methods from Main.py
def main():
    Employee1 = Employee(1, "John Smith", 1, 1)
    Employee1.getEmployeeDetails()
    Employee2 = Employee(2, "Jane Doe", 2, 2)
    Employee2.getEmployeeDetails()
  
    #test Department class
    Department1 = Department(1, "IT")
    Department1.getDepartmentDetails()
    Department2 = Department(2, "HR")
    Department2.getDepartmentDetails()
    Department3 = Department(3, "Finance")
    Department3.getDepartmentDetails()
    
    #test Role class
    Role1 = Role(1, "Manager")
    Role1.getRoleDetails()
    Role2 = Role(2, "Employee")
    Role2.getRoleDetails()
    
    #test LeaveType class
    leaveType1 = LeaveType(1, "Sick Leave")
    leaveType1.getLeaveTypeDetails()
    leaveType2 = LeaveType(2, "Vacation Leave")
    leaveType2.getLeaveTypeDetails()
    
    #test Leave class
    leave1 = Leave(1, 1, 1, 5, 10, "01/01/2019", "01/05/2019", "Approved")
    leave1.setLeaveDetails(1, 1, 1, 5, 10, "01/01/2019", "01/05/2019", "Approved")
    leave1.getLeaveDetails()
   
    #test manage account class
    account1 = ManageAccount(1, "John", 1, 1, "1234567890", "123 Main St", "john@email.com")
    account1.setManageAccountDetails(1, "John", 1, 1, "1234567890", "123 Main St", "john@email.com")
    account1.getManageAccountDetails()
    print("Account will be updated")
    account1.updateManageAccountDetails("0987654321", "456 Main St", "john@newemail.com")
    account1.updatedManageAccountDetails()
    print("The account below has been updated")
    account1.getManageAccountDetails()
    
if __name__ == "__main__":
    main()