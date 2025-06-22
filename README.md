# 📚 EduTech (2024) – Educational Web Application

This Project is a responsive educational web application developed during my **6-month industrial training**, using **Django (Python)** for the backend and **HTML, CSS, and Bootstrap** for the frontend.

The platform provides users access to educational data and analytics related to **student dropouts**, **courses**, **colleges**, **universities**, and more. The project also includes modules for managing national education coordinators, laws, and states/UT-wise statistics. Both **user** and **admin panels** offer interactive functionality to manage and explore rich educational datasets, visualized using basic data analysis tools.

---

## 🚀 Features

### 👨‍🎓 User Module:
- 🔐 User Registration/Login
- 📊 View Analytics & Dropout Statistics
- 📚 Browse Courses, Colleges, and Universities
- 🏛 Explore State & UT-wise Education Data
- 📈 Access National Coordinators & Laws
- 📬 Help and Support Section

### 🛠 Admin Module:
- 🔐 Admin Login/Profile Management
- 📝 Manage Blogs and Posts
- 🏫 Add/Edit Universities & Colleges
- 📜 Manage Educational Laws
- 🌐 National Coordinators Panel

---

## 🧰 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Python (Django)  
- **Database:** SQLite  
- **Analysis Tools:** pandas, matplotlib (basic usage)  
- **Architecture:** MVT (Model-View-Template) – Django Framework  
- **Deployment:** PythonAnywhere 
---

## 📁 Project Info

- 🕒 Duration: 6 Months  
- 🏫 Completed as part of Industrial Training  
- 📌 Focused on educational content, statistics, and admin data control  
- 💡 Involved basic data analysis for student dropout insights

---

## ⚙️ Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/edutech-webapp.git
cd edutech-webapp

# Set up virtual environment
python -m venv venv
venv\Scripts\activate     # Windows

# Install required packages
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start the server
python manage.py runserver

