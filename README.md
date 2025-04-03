# -AI-Assessment-Solution4

📌 Overview
This project is my solution for the AI Internship Assessment at PearlThoughts. It involves solving a given problem using Python, implementing best practices, and ensuring security measures.

📁 Project Structure
bash
Copy
Edit
📂 AI-Assessment-Solution4
│── 📜 main.py                # Main script to run the project
│── 📜 requirements.txt       # Required dependencies
│── 📜 config.py (REMOVED)    # Previously contained sensitive info, now using .env
│── 📜 .gitignore             # Ensures unnecessary files are not pushed
│── 📜 README.md              # Documentation for the project
⚙️ Setup & Installation
Follow these steps to set up and run the project on your local machine:

1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/shashankshri2/-AI-Assessment-Solution4.git
cd -AI-Assessment-Solution4
2️⃣ Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Since sensitive credentials were removed from config.py, create a .env file and add your environment variables:

bash
Copy
Edit
TWILIO_ACCOUNT_SID="your_account_sid"
TWILIO_AUTH_TOKEN="your_auth_token"
5️⃣ Run the Project
bash
Copy
Edit
python main.py
🛠️ Approach & Features
Problem Breakdown: Step-by-step analysis of the given task

Python Implementation: Used efficient libraries and techniques

Security Measures: Removed sensitive data and implemented .env files

Optimized Code: Ensured best practices for maintainability
