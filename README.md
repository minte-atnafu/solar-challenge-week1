# Solar Challenge Week 1

## How to Reproduce the Environment

### 1. Clone the repository
```powershell
git clone https://github.com/minte-atnafu/solar-challenge-week1.git
cd solar-challenge-week1


# Create virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


#  Verify Python installation
python --version

#Continuous Integration
GitHub Actions workflow (.github/workflows/ci.yml) automatically installs dependencies and verifies the Python environment by running:


# implemnt the follwing folder structure

├── .vscode/

│   └── settings.json

├── .github/

│   └── workflows

│       ├── unittests.yml

├── .gitignore

├── requirements.txt

├── README.md

 |------ src/

├── notebooks/

│   ├── __init__.py

│   └── README.md

├── tests/

│   ├── __init__.py

└── scripts/

    ├── __init__.py

    └── README.md

![Git Network Graph](docs/git-network-graph.png)
