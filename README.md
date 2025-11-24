# Cybercafe Management System

## Project Overview
This project implements a simple command-line interface (CLI) based Cybercafe Management System. It allows for the management of customer and computer details within a cybercafe environment, including basic operations like adding, displaying, updating, and deleting records, as well as calculating billing based on usage time.

## Features
The system provides the following functionalities:
*   **Display Records:** View all entries in the `customer_details` or `computer_details` tables.
*   **Display Single Record:** Retrieve and display details for a specific customer by username or a specific computer by ID.
*   **Add Customer Details:** Register new customer information, including username, computer ID, ID proof, ID number, mobile number, and email ID.
*   **Add Computer Details:** Add new computer entries, including computer ID, name, and IP address.
*   **Update Customer Details:** Modify existing customer information such as username, computer ID, ID proof, ID number, mobile number, or email ID.
*   **Update Computer Details:** Change details for existing computers, including computer name or IP address.
*   **Delete Records:** Remove customer records by username or computer records by computer ID.
*   **Billing:** Calculate the cost of computer usage based on start and end times.

## Technologies Used
*   **Python:** The primary programming language for the application logic.
*   **mysql.connector:** Python library for connecting to and interacting with MySQL databases.
*   **MySQL Database:** Used as the backend to store customer and computer data.

## Setup and Installation

### Prerequisites
Before running the application, ensure you have the following installed:
*   **Python 3.x**
*   **MySQL Server**

### Installation

```bash
git clone <url>
cd <folders>
```

### Database Setup
1.  **Create the Database:**
    ```sql
    CREATE DATABASE cybercafe;
    USE cybercafe;
    ```
2.  **Create `customer_details` Table:**
    ```sql
    CREATE TABLE customer_details (
        username VARCHAR(255) PRIMARY KEY,
        computer_id INT,
        id_proof VARCHAR(255),
        id_number INT,
        mobile_number INT,
        email_id VARCHAR(255)
    );
    ```
3.  **Create `computer_details` Table:**
    ```sql
    CREATE TABLE computer_details (
        computer_id INT PRIMARY KEY,
        computer_name VARCHAR(255),
        IP_address VARCHAR(255)
    );
    ```
4.  **Update Database Credentials:**
    The application connects to MySQL using `host='localhost', user='root', passwd='', database='cybercafe'`. If your MySQL setup uses different credentials, you will need to manually update these in the `main.py` file.

### Python Dependencies
Install the required Python library:
```bash
pip install mysql-connector-python
```

### Running the Application
Navigate to the project directory in your terminal and run:
```bash
python main.py
```

## Instructions for Testing
Once the application is running, you can test its functionalities by interacting with the menu options presented in the console. Follow the prompts to:
*   Add new customers and computers.
*   Display various records.
*   Update existing details.
*   Delete records.
*   Test the billing calculation.

Ensure that each operation performs as expected and that data is correctly stored and retrieved from the MySQL database.

