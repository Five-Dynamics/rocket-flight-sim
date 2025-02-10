# 🚀 Python Simulation: Rocket Py

![Black Style Check](https://github.com/Five-Dynamics/rocket-flight-sim/actions/workflows/python-black-style-enforce.yaml/badge.svg) ![EditorConfig Check](https://github.com/Five-Dynamics/rocket-flight-sim/actions/workflows/python-editor-config.yaml/badge.svg) ![Run Simulation](https://github.com/Five-Dynamics/rocket-flight-sim/actions/workflows/python-test_build.yaml/badge.svg)

## 📌 Overview
This repository contains a **rocket simulation project** written in Python. It includes structured modules, configuration files, and GitHub Actions workflows to ensure proper coding style and successful code execution.

---

## 📂 **Repository Structure**
rocket_py/ # Main Python simulation code (where you are right now)
 ├── polaris1/ # Polaris 1 rocket simulation module │ ├── data/ # Data files for the simulation │
 ├── testrocket.py # Test script for rocket simulation (HAS TO PASS BUILD FOR PR)
 ├── requirements.txt # Python dependencies

.editorconfig # Enforces consistent code style across editors (download in recommended extensions)


## 🤝 Contributing Guidelines

We welcome contributions to improve this project! To ensure consistency and maintain code quality, please follow these steps before submitting a Pull Request (PR).

## ⚙️ **Setting Up the Environment**
### 🏗️ **Create a Virtual Environment (One Level Down from Root)**
To maintain dependencies separately, **create a virtual environment (`venv`) inside `rocket_py`** :
```sh
cd rocket_py
python -m venv venv
```
Then to activate:
Windows:
`venv\Scripts\activate`

Mac/Linux
`source venv/bin/activate`

📦 Install Required Packages
Once the virtual environment is activated, install the dependencies:
`pip install -r requirements.txt`

🎨 Checking Code Formatting
This project uses Black to enforce code formatting. YOUR PR WILL FAIL IF THIS DOESN'T PASS
`black --check .`

Can autoformat to pass (Make sure to check the changes)
`black .`

🔍 3. Lint Code with Pylint
Run Pylint to check for errors and ensure the code meets quality standards.

Run Pylint and Enforce a Minimum Score (I suggest trying to get a 10.00):
`pylint --fail-under=7.0 $(git ls-files '*.py')`

🔤 4. Ensure Consistency with EditorConfig
Make sure your files follow .editorconfig rules (UTF-8 encoding, indentation, and line endings)
This should be automated as long as you have .editorconfig extension
