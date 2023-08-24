# CompanyAssetTracker
This is a simple application that helps companies track and manage their corporate assets. It uses the **Django Rest Framework** to create a **RESTful API** that makes it easy to interact with the data. This makes it a powerful tool for companies of all sizes to improve their asset management processes.
# Key-Features
- **Multi-Company Support:** The software is designed to cater to multiple companies, offering each company an independent asset management system within the application. Company administrators can utilize the company ID to access information and perform various actions such as updates and deletions. The software fully supports Create, Read, Update, and Delete (CRUD) operations for comprehensive management.

- **Staff Management:** Company administrators can efficiently create and manage staff profiles with ease.

- **Employee Handling:** The application allows for the registration of employees associated with a company. Essential employee details like name, address, email, and phone number can be conveniently recorded. Additionally, updates and deletions for existing employee records are also supported.

- **Device/Asset Creation:** Company administrators have the capability to add new assets/devices to the system, providing essential information such as device name, description, serial number, and condition. The software also allows for updates and deletions of existing device records. For scenarios such as device repairs or removals, updates can be made using the device's unique ID.

- **Device Log Tracking:** The software plays a vital role in asset management by enabling thorough tracking of asset movements within the organization. This functionality encompasses monitoring checkout and return times, asset quantities, conditions, and the staff members involved. This comprehensive approach enhances asset management, accountability, and historical record-keeping, providing a streamlined process for asset utilization and tracking.

# Automated API Documentation 
The Corporate Asset Tracker includes an API that enables programmatic interaction with the application. You can access the API documentation at [[http://localhost:8000/swagger/]([http://127.0.0.1:8000/api/v1/swagger/](http://127.0.0.1:8000/api/v1/swagger/))](http://localhost:8000/swagger/).

# How to Use

Follow these steps to set up and run the project:

1. Clone the project repository from :

2. Create a virtual environment:

3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install project dependencies from `requirements.txt`:

5. Perform database migrations:
   ```
    python manage.py makemigrations
    python manage.py migrate
   ```
6. Run the project:
    ```
    python manage.py runserver
     ```
7. Access the admin page: Open your web browser and navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

8. Create a superuser account:
   ```
     python manage.py createsuperuser
   ```
9. You're all set!

# Some JSON Object Examples for Request/Response:
1. **Creating a new company (POST)**
   ```
     POST http://127.0.0.1:8000/api/v1/companies/
   ```
   Request Body
  ```
     {
      "name": "Optimizely",
      "address": "Gulshan, Dhaka",
      "phone_number": "01671977294",
      "website": "https://www.optimizely.com/",
      }
 ```
   Response:
   
     ```
       {
        "id": 1,
        "name": "Optimizely",
        "address": "Gulshan, Dhaka",
        "phone_number": "01671977294",
        "website": "https://www.optimizely.com/",
        "created_at": "2023-08-24T16:33:39.672340Z",
        "updated_at": "2023-08-24T16:33:39.672340Z"
        }
    ```
2. **List Information for a specific company by Using company_id (Get)**
   ```
     GET http://127.0.0.1:8000/api/v1/companies/1
   ```
      Response:
     
   ```
         {
          "id": 1,
          "name": "Optimizely",
          "address": "Gulshan, Dhaka",
          "phone_number": "01671977294",
          "website": "https://www.optimizely.com/",
          "created_at": "2023-08-24T16:33:39.672340Z",
          "updated_at": "2023-08-24T16:33:39.672340Z"
          }
   ```
3. **Creating a new Employee (POST)**
   ```
     POST http://127.0.0.1:8000/api/v1/employees/
   ```
   Request Body
  ```
     {
        "first_name": "Shakil Mahmud",
        "last_name": "Shuvo",
        "email": "abc@gmail.com",
        "departments": "ML",
        "position": "Junior ML Engineer",
         "company": 1
      }
 ```
   Response:
   
     ```
    {
        "id": 1,
        "first_name": "Shakil Mahmud",
        "last_name": "Shuvo",
        "email": "abc@gmail.com",
        "departments": "ML",
        "position": "Junior ML Engineer",
        "created_at": "2023-08-24T16:35:32.348255Z",
        "updated_at": "2023-08-24T16:35:32.348255Z",
        "company": 1
    }
    ```
4. **List Information for a specific employee by Using employee_id (Get)**
   ```
     GET http://127.0.0.1:8000/api/v1/employees/1
   ```
      Response:
     
   ```
      {
        "id": 1,
        "first_name": "Shakil Mahmud",
        "last_name": "Shuvo",
        "email": "abc@gmail.com",
        "departments": "ML",
        "position": "Junior ML Engineer",
        "created_at": "2023-08-24T16:35:32.348255Z",
        "updated_at": "2023-08-24T16:35:32.348255Z",
        "company": 1
    }
   ```
5. **Creating a new Staff (POST)**
   ```
     POST http://127.0.0.1:8000/api/v1/staff/
   ```
   Request Body
  ```
     {
         "first_name": "Rahim",
        "last_name": "Uddin",
         "company": 1
      }
 ```
   Response:
   
     ```
    {
        "id": 1,
        "first_name": "Rahim",
        "last_name": "Uddin",
        "created_at": "2023-08-24T16:37:05.234174Z",
        "updated_at": "2023-08-24T16:37:05.234174Z",
        "company": 1
    }
    ```
6. **List Information for a specific staff by Using staff_id (Get)**
   ```
     GET http://127.0.0.1:8000/api/v1/staff/1
   ```
      Response:
     
   ```
    {
        "id": 1,
        "first_name": "Rahim",
        "last_name": "Uddin",
        "created_at": "2023-08-24T16:37:05.234174Z",
        "updated_at": "2023-08-24T16:37:05.234174Z",
        "company": 1
    }
   ```
7. **Creating a new Device (POST)**
   ```
     POST http://127.0.0.1:8000/api/v1/devices/
   ```
   Request Body
  ```
     {
         "name": "ASUS VivoBook 15 X515EA",
        "description": "Key Features\r\n\r\n    MPN: BQ2227W-X515EA\r\n    Model: VivoBook 15 X515EA\r\n    Processor: Intel Core i5-1135G7 Processor (8M Cache, 2.40 GHz up to 4.20 GHz)\r\n    RAM: 8GB DDR4 RAM (ON BOARD), Storage: 512GB SSD\r\n    Display: 15.6-inch, FHD (1920 x 1080)\r\n    Features: Illuminated Chiclet Keyboard, Type-C",
        "serial_number": "15151231354",
        "condition": "new",
      }
 ```
   Response:
   
     ```
    {
        "id": 1,
        "name": "ASUS VivoBook 15 X515EA",
        "description": "Key Features\r\n\r\n    MPN: BQ2227W-X515EA\r\n    Model: VivoBook 15 X515EA\r\n    Processor: Intel Core i5-1135G7 Processor (8M Cache, 2.40 GHz up to 4.20 GHz)\r\n    RAM: 8GB DDR4 RAM (ON BOARD), Storage: 512GB SSD\r\n    Display: 15.6-inch, FHD (1920 x 1080)\r\n    Features: Illuminated Chiclet Keyboard, Type-C",
        "serial_number": "15151231354",
        "condition": "new",
        "created_at": "2023-08-24T16:41:37.683481Z",
        "updated_at": "2023-08-24T16:41:37.683481Z",
        "company": 1
    }

    ```
8. **List Information for a specific device by Using device_id (Get)**
   ```
     GET http://127.0.0.1:8000/api/v1/devices/1
   ```
      Response:
     
   ```
    {
        "id": 1,
        "name": "ASUS VivoBook 15 X515EA",
        "description": "Key Features\r\n\r\n    MPN: BQ2227W-X515EA\r\n    Model: VivoBook 15 X515EA\r\n    Processor: Intel Core i5-1135G7 Processor (8M Cache, 2.40 GHz up to 4.20 GHz)\r\n    RAM: 8GB DDR4 RAM (ON BOARD), Storage: 512GB SSD\r\n    Display: 15.6-inch, FHD (1920 x 1080)\r\n    Features: Illuminated Chiclet Keyboard, Type-C",
        "serial_number": "15151231354",
        "condition": "new",
        "created_at": "2023-08-24T16:41:37.683481Z",
        "updated_at": "2023-08-24T16:41:37.683481Z",
        "company": 1
    }

   ```
9. **Creating a new Device-Log/ Assign (POST)**
   ```
     POST http://127.0.0.1:8000/api/v1/device-log/
   ```
   Request Body
  ```
     {
 "checkout_time": "2023-08-10",
      "checkout_quantity": 1,
      "chekout_note": "It was new, unpacked",
      "checkout_condition": "good",
      "return_quantity": 1,
      "returned_note": "Its alright",
      "return_time": null,
      "returned_condition": "good",
      "created_at": "2023-08-24T16:52:32.187892Z",
      "issuing_time": "2023-08-24T16:52:32.187892Z",
      "device": 1,
      "employee": 1,
      "company": 1,
      "checkout_by_staff": 1,
      "returned_by_staff": 1
      }
 ```
   Response:
   
     ```
     {
      "id": 1,
      "checkout_time": "2023-08-10",
      "checkout_quantity": 1,
      "chekout_note": "It was new, unpacked",
      "checkout_condition": "good",
      "return_quantity": 1,
      "returned_note": "Its alright",
      "return_time": null,
      "returned_condition": "good",
      "created_at": "2023-08-24T16:52:32.187892Z",
      "issuing_time": "2023-08-24T16:52:32.187892Z",
      "device": 1,
      "employee": 1,
      "company": 1,
      "checkout_by_staff": 1,
      "returned_by_staff": 1
  }

    ```
10. **List Information for a specific device-log by Using device-log_id (Get)**
   ```
     GET http://127.0.0.1:8000/api/v1/device-log/2
   ```
  Response:
     
   ```
{
    "id": 2,
    "checkout_time": "2023-08-03",
    "checkout_quantity": 1,
    "chekout_note": "The monitor was good and healthy",
    "checkout_condition": "fair",
    "return_quantity": 1,
    "returned_note": "He lost it",
    "return_time": null,
    "returned_condition": "lost",
    "created_at": "2023-08-24T16:53:34.101354Z",
    "issuing_time": "2023-08-24T16:53:34.101354Z",
    "device": 2,
    "employee": 3,
    "company": 2,
    "checkout_by_staff": 2,
    "returned_by_staff": 1
}


   ```
    
  


