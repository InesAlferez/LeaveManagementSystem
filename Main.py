# Create a leave management system for a company
        
class Employee:
    #initialize Employee class
    def __init__(self, employeeID, name, departmentID, roleID):
        self.employeeID = employeeID
        self.name = name
        self.departmentID = departmentID
        self.roleID = roleID
    
    def setEmployeeDetails(self, employeeID, name, departmentID, roleID):
        #set employee details
        self.employeeID = employeeID
        self.name = name
        self.departmentID = departmentID
        self.roleID = roleID
        
    def getEmployeeDetails(self):
        #get employee details
        print("Employee ID: ", self.employeeID)
        print("Employee Name: ", self.name)
        print("Department ID: ", self.departmentID)
        print("Role ID: ", self.roleID)
    
class Department:
    #initialize Department class
    def __init__(self, departmentID, departmentName):
        self.departmentID = departmentID
        self.departmentName = departmentName
        
    def setDepartmentDetails(self, departmentID, departmentName):
        #set department details
        self.departmentID = departmentID
        self.departmentName = departmentName
    
    def getDepartmentDetails(self):
        #get department details
        print("Department ID: ", self.departmentID)
        print("Department Name: ", self.departmentName)
    
class Role:
    def __init__(self, roleID, roleName):
        #initialize Role class
        self.roleID = roleID
        self.roleName = roleName
    
    def setRoleDetails(self, roleID, roleName):
        #set role details
        self.roleID = roleID
        self.roleName = roleName  
        
    def getRoleDetails(self):
        #get role details
        print("Role ID: ", self.roleID)
        print("Role Name: ", self.roleName)
    
class LeaveType:
    def __init__(self, leaveTypeID, leaveTypeName):
        #initialize LeaveType class
        self.leaveTypeID = leaveTypeID
        self.leaveTypeName = leaveTypeName
        
    def setLeaveTypeDetails(self, leaveTypeID, leaveTypeName):
        #set leave type details
        self.leaveTypeID = leaveTypeID
        self.leaveTypeName = leaveTypeName
        
    def getLeaveTypeDetails(self):
        #get leave type details
        print("Leave Type ID: ", self.leaveTypeID)
        print("Leave Type Name: ", self.leaveTypeName)
    
class Leave:
    def __init__(self, leaveID, employeeID, leaveTypeID, numDays, leaveBalance, startDate, endDate, status):
        #initialize Leave class
        self.leaveID = leaveID
        self.employeeID = employeeID
        self.leaveTypeID = leaveTypeID
        self.numDays = numDays
        self.leaveBalance = leaveBalance
        self.startDate = startDate
        self.endDate = endDate
        self.status = status
        
    def setLeaveDetails(self, leaveID, employeeID, leaveTypeID, numDays, leaveBalance, startDate, endDate, status):
        #set leave details
        self.leaveID = leaveID
        self.employeeID = employeeID
        self.leaveTypeID = leaveTypeID
        self.numDays = numDays
        self.leaveBalance = leaveBalance
        self.startDate = startDate
        self.endDate = endDate
        self.status = status
        
    def getLeaveDetails(self):
        #get leave details
        print("Leave ID: ", self.leaveID)
        print("Employee ID: ", self.employeeID)
        print("Leave Type ID: ", self.leaveTypeID)
        print("Number of Days: ", self.numDays)
        print("Leave Balance: ", self.leaveBalance)
        print("Start Date: ", self.startDate)
        print("End Date: ", self.endDate)
        print("Status: ", self.status)
    

class ManageAccount:
    def __init__(self, employeeID, name, departmentID, roleID, phoneNumber, address, email):
        #initialize ManageAccount class
        self.employeeID = employeeID
        self.name = name
        self.departmentID = departmentID
        self.roleID = roleID
        self.phoneNumber = phoneNumber
        self.address = address
        self.email = email
        
    def setManageAccountDetails(self, employeeID, name, departmentID, roleID, phoneNumber, address, email):
        #set manage account details
        self.employeeID = employeeID
        self.name = name
        self.departmentID = departmentID
        self.roleID = roleID
        self.phoneNumber = phoneNumber
        self.address = address
        self.email = email
        
    def getManageAccountDetails(self):
        #get manage account details
        print("Employee ID: ", self.employeeID)
        print("Employee Name: ", self.name)
        print("Department ID: ", self.departmentID)
        print("Role ID: ", self.roleID)
        print("Phone Number: ", self.phoneNumber)
        print("Address: ", self.address)
        print("Email: ", self.email)
        
    def updateManageAccountDetails(self, phoneNumber, address, email):
        #update manage account details
        self.phoneNumber = phoneNumber
        self.address = address
        self.email = email
        
    def updatedManageAccountDetails(self):
        #updated manage account details
        print("Updated Phone Number: ", self.phoneNumber)
        print("Updated Address: ", self.address)
        print("Updated Email: ", self.email)