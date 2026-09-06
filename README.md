# ⚽ Smart Football Scout

Smart Football Scout is a full-stack mobile application built to digitize and manage football talent evaluation. The system is designed with a decoupled architecture, separating a secure, cloud-hosted backend API from a cross-platform mobile client. 

### 🏗️ Architecture & Tech Stack
* **Backend:** Python, Django, Django REST Framework (DRF)
* **Frontend:** Flutter, Dart
* **Security:** JWT (JSON Web Tokens), Role-Based Access Control (RBAC)
* **Deployment & DevOps:** Docker, Git, Back4App (Containers as a Service)
* **Database:** SQLite / PostgreSQL 

### ✨ Key Features
* **Secure API Communication:** Fully protected endpoints requiring JWT authentication for data access and manipulation.
* **Comprehensive Data Models:** Systematized tracking of `Players`, `Matches`, and detailed `ScoutReports`.
* **Cloud-Hosted Infrastructure:** Containerized Django backend deployed seamlessly via Back4App with configured CORS and CSRF protections.
* **Cross-Platform Mobile UI:** A responsive Flutter client featuring persistent local storage for session management and real-time API consumption.
