# SmartBooks API
SmartBooks API is a backend project designed to manage personal and business finances. It allows users to record income and expenses, generate reports, and export data in CSV or PDF formats. The project uses **Django** and **Django REST Framework (DRF)** and implements token-based authentication and role-based permissions.

# Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Setup Instructions](#setup-instructions)  
- [API Endpoints](#api-endpoints)  
- [Authentication](#authentication)  
- [Reports & Export](#reports--export)  
 


# Features

- User registration and login (token authentication)  
- CRUD operations for Income, Expenses, and Transactions  
- Filtering by date range, source, or category  
- Pagination and search for lists  
- Role-based permissions for secure access  
- Generate reports on financial data  
- Export reports to CSV and PDF  



##  Tech Stack

- Python 3.13  
- Django 5.x  
- Django REST Framework  
- MySQL (or SQLite for testing)  
- DRF token authentication  
- ReportLab (for PDF export)  


1. **Clone the repository**
```bash
git clone https://github.com/your-username/SmartBooks-API.git
cd SmartBooks-API

| Endpoint              | Method           | Description                                   |
| --------------------- | ---------------- | --------------------------------------------- |
| `/api/register/`      | POST             | Register a new user                           |
| `/api/login/`         | POST             | Obtain auth token                             |
| `/api/income/`        | GET, POST        | List or create income records                 |
| `/api/income/{id}/`   | GET, PUT, DELETE | Retrieve, update, or delete an income record  |
| `/api/expenses/`      | GET, POST        | List or create expense records                |
| `/api/expenses/{id}/` | GET, PUT, DELETE | Retrieve, update, or delete an expense record |
| `/api/transactions/`  | GET              | List all transactions (income + expenses)     |
| `/api/reports/`       | GET              | Generate summary reports                      |
| `/api/export/csv/`    | GET              | Export report as CSV                          |
| `/api/export/pdf/`    | GET              | Export report as PDF                          |
Authentication

Obtain token via /api/login/ with username & password

Include token in request headers for protected endpoints: