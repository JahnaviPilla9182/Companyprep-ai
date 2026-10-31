# Companyprep-ai
# 🚀 Company Prep AI – AI-Powered Company Interview Preparation Platform

## 📌 Project Overview

**Company Prep AI** is an AI-powered interview preparation platform designed to help students and job seekers prepare for company-specific placement drives and technical interviews.

The platform generates personalized interview preparation roadmaps based on the target company, job role, required skills, current experience level, available study hours, and preparation duration.

It helps candidates follow a structured learning path, practice interview questions, access useful learning resources, and track their preparation progress.

## ✨ Key Features

- **Company-Based Preparation:** Select a target company and job role to receive a customized preparation plan.
- **Personalized AI Roadmaps:** Generate adaptive weekly preparation roadmaps based on individual requirements.
- **Technical Interview Questions:** Get role-specific technical and interview practice questions.
- **Learning Resources:** Access recommended learning materials and preparation resources.
- **Progress Tracking:** Track completed topics and monitor preparation progress.
- **Flexible Preparation Plans:** Customize roadmaps according to available study hours and preparation duration.
- **AI-Powered Assistance:** Use AI to generate relevant preparation recommendations.
- **PDF Export:** Download preparation materials and roadmaps in PDF format.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Frontend and web application |
| Google Gemini API | AI-powered content generation |
| Groq API | AI-powered responses |
| Pandas | Data handling and processing |
| FPDF2 | PDF generation |
| Python-dotenv | Environment variable management |
| Pytest | Testing |

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Company-Prep-AI.git
```

### 2. Navigate to the Project Directory

```bash
cd Company-Prep-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Keys

Create a `.env` file in the project root directory.

Add your API keys:

```env
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder values with your actual API keys.

**Note:** Never upload your `.env` file or expose your API keys on GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 📂 Project Structure

```text
Company-Prep-AI/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── assets/
├── tests/
│
└── ...
```

*Note: Update the folder structure above to match your actual project files.*

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

1. Push the project to a GitHub repository.
2. Visit https://share.streamlit.io/
3. Sign in using your GitHub account.
4. Select your Company Prep AI repository.
5. Choose `app.py` as the main application file.
6. Add your API keys under Streamlit Secrets.
7. Click **Deploy**.

## 🎯 Project Objectives

- Simplify company-specific placement preparation.
- Provide personalized interview preparation strategies.
- Reduce the time required to plan a preparation schedule.
- Help students improve their technical and interview skills.
- Make AI-powered placement preparation accessible and structured.

## 🔮 Future Enhancements

- AI-powered mock interview sessions.
- Resume analysis and improvement suggestions.
- Coding practice with automated evaluation.
- Company-wise aptitude preparation.
- Performance analytics and personalized recommendations.
- User authentication and individual progress history.

## 👩‍💻 Developed By

**Pilla Jahnavi**

Computer Science and Engineering

GMR Institute of Technology

---

⭐ If you find this project useful, consider giving the repository a star!
