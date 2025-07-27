# ConsciousDay – AI-Powered Daily Reflection App

ConsciousDay is a journaling web application that combines mindful self-reflection with intelligent insights. Built using Streamlit, LangChain, and Together AI, it allows users to write daily journal entries and receive AI-generated feedback, strategies, and personalized guidance.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Key Setup](#api-key-setup)
- [Running the App](#running-the-app)
- [Sample Input](#sample-input)
- [Deployment Guide](#deployment-guide)
- [Acceptance Criteria](#acceptance-criteria)
- [Credits](#credits)

---

## Features

- Structured journaling with intention, priorities, thoughts, and dream input
- AI-generated reflection summary and suggested daily strategy
- View history using a calendar date picker
- Simple login system with Streamlit session state
- Stores data in SQLite database
- Clean and minimal user interface using Streamlit

---

## Installation

### Prerequisites

- Python 3.10 or higher
- Together AI API key

### Clone the Repository

```bash
git clone https://github.com/yourusername/consciousday.git
cd consciousday

--create venv

python -m venv venv
venv\Scripts\activate        # For Windows
# OR
source venv/bin/activate     # For macOS/Linux

--install dependencies

pip install -r requirements.txt

--run

streamlit run app.py

