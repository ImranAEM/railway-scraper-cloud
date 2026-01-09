# 🚆 Azure Train Data Project with iRail API
----------------------------------------------------------------------------------------------------------
### 📌 Project Description
----------------------------------------------------------------------------------------------------------
This project is part of the BeCode BootCamp and focuses on building a cloud-based data pipeline using Microsoft Azure and the iRail API.

The goal of the project is to fetch real-time train data from Belgium, process it with Python, and prepare it for storage in an Azure SQL Database, using an Azure Function App as the core ingestion layer.

The project emphasizes understanding how a real-world, serverless data pipeline works, from consuming a public API to structuring data for cloud storage.

### 🗂️ Folder Structure
----------------------------------------------------------------------------------------------------------


    iRail_cloud_project/
    │
    ├─ function_app.py        # Azure Function App (HTTP Trigger)
    ├─ requirements.txt       # Project dependencies
    ├─ local.settings.json    # Local Azure Functions configuration
    ├─ .venv310/              # Python 3.10 virtual environment
    └─ README.md


### 🧠 Learning Objectives
----------------------------------------------------------------------------------------------------------
* Understand how Azure Functions (Python) work.

* Consume data from a public API (iRail).

* Work with real-world JSON data.

* Prepare structured data for insertion into an Azure SQL Database.

* Understand the fundamentals of a cloud-based data pipeline.

* Gain hands-on experience with Azure resources via the Azure Portal.

### 🎯 Mission Objectives
----------------------------------------------------------------------------------------------------------

* Create an Azure Function with an HTTP trigger.

* Connect to the iRail API to fetch train-related data.

* Process and structure the retrieved data.

* Prepare the data for insertion into an Azure SQL database.

* Document the entire process clearly and transparently.

### 🔍 Methodology
----------------------------------------------------------------------------------------------------------

1️⃣ Azure Function App

* Creation of an Azure Function App using the Azure Portal.

* Configuration of the Python 3.10 runtime.

* Implementation of an HTTP-triggered function.

* Use of environment variables for configuration and credentials.

2️⃣ iRail API Integration

* Consumption of iRail API endpoints.

* Retrieval of train data in JSON format.

* Selection of relevant fields such as stations, departures, schedules, and status.

3️⃣ Data Processing

* Conversion of JSON responses into Python data structures.

* Cleaning and selecting only the necessary fields.

* Preparing the dataset for SQL insertion.

4️⃣ SQL Preparation

* Design of the data insertion flow toward Azure SQL Database.

* Development of the SQL connection logic.

* Preparation for execution once the Function App runs correctly.

### 📈 Current Project Status
----------------------------------------------------------------------------------------------------------
* Azure Function App successfully created.

* HTTP trigger implemented.

* Connection to the iRail API working as expected.

* Data processing logic implemented in Python.

* SQL insertion logic prepared.

* Local execution currently blocked due to an issue with func start, pending resolution.

🧪 Learning Outcomes
----------------------------------------------------------------------------------------------------------

* Practical understanding of serverless architectures.

* Experience working with real-time public APIs.

* First hands-on cloud data pipeline implementation.

* Preparing structured data for relational databases.

* Improved technical documentation skills for cloud projects.

### ⏱️ Timeline
----------------------------------------------------------------------------------------------------------

Project completed over 5 days:

* Azure setup and resource creation.

* Azure Function development.

* iRail API integration.

* Data processing implementation.

* Documentation and project review.

### ✅ Conclusion
----------------------------------------------------------------------------------------------------------

This project represents a first complete cloud-based data pipeline, focused on understanding the full flow from an external API to a serverless Azure environment.

Rather than focusing on advanced features, the project prioritizes clarity, structure, and real-world understanding, laying a solid foundation for future improvements such as automation, dashboards, or advanced deployment strategies.