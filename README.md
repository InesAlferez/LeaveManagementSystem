<h1 align="center">Welcome to LeaveManagementSystem 👋</h1>
<p>
</p>

> The Employee Management System is a Python-based application designed to manage employee-related data within an organization. This system includes several classes that handle employee details, departments, roles, leaves, and account information. 

## Usage


<h1>Features</h1>
<h2>1. Classes:</h2>
<h3>The system comprises the following classes with specific functionalities:</h3>

Employee: Manages employee details such as ID, name, department, and role.
Department: Handles department-related details including Department ID and name.
Role: Manages roles within the organization.
LeaveType: Manages various leave types such as sick leave and vacation leave.
Leave: Handles employee leave-related data.
ManageAccount: Manages employee account information like contact details and address.

<h2>2. Functionalities:</h2>

Each class offers methods to set, retrieve, and update specific details related to employees, departments, roles, leaves, and accounts. These functionalities can be utilized to create, modify, and retrieve relevant information within an organizational structure.

<h2>Classes</h2>

<h3>Class Details:</h3>
Each class is designed with an initialization method (__init__) to create instances with specific attributes.
Setter methods (set*Details) are provided to update or set class attributes.
Getter methods (get*Details) retrieve and display information stored within the classes.

Specific methods within each class offer functionalities tailored to their respective purposes.
<h2>Usage</h2>

The system is structured to be integrated into larger applications or utilized individually to manage employee-related data efficiently. Users can import these classes into their projects and utilize their methods to handle employee management operations.

<h2>Integration:</h2>

## Importing:
```sh
from main import Employee, Department, Role, LeaveType, Leave, ManageAccount
```

<h3>2. Creating Instances:</h3> 

## Example Usage
```sh
employee = Employee(1, "John Doe", 1, 1)
employee.getEmployeeDetails()
```

<h3>3. Using Methods:</h3>
Use setter methods to update details.
Employ getter methods to retrieve and display information.

## Author

👤 **Ines Alferez**

* Github: [@InesAlferez](https://github.com/InesAlferez)
* LinkedIn: [@ines-alferez-0a0881234](https://linkedin.com/in/ines-alferez-0a0881234)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_