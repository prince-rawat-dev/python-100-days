# Day 43 - Virtual Environment

## Lecture

Lecture 43

## Topic

Virtual Environment in Python

## Concepts Covered

* What is a Virtual Environment
* Why Virtual Environment is used
* Creating a Virtual Environment
* `python -m venv`
* Creating `venv1`
* Activating Virtual Environment in Windows PowerShell
* `.\venv1\Scripts\Activate.ps1`
* Checking the active Virtual Environment
* Installing packages inside Virtual Environment
* Installing `requests` using `pip`
* Testing the `requests` package
* Understanding package isolation
* `python -m pip install requests`
* Checking installed packages
* `pip freeze`
* Creating `requirements.txt`
* `python -m pip freeze > requirements.txt`
* Purpose of `requirements.txt`
* Using `.gitignore` with Virtual Environment
* Ignoring `venv1/`
* Ignoring `__pycache__/`
* Ignoring `*.pyc`
* Ignoring `.env`
* Understanding the difference between project files and Virtual Environment files
* Understanding the role of `.vscode`
* Keeping project/program files outside `venv1`
* Testing package installation with a real Python program
* Verifying `requests` using `https://example.com`
* Successful response with Status Code: 200

## Practice Programs

1. Create and Activate a Virtual Environment
2. Install and Test the `requests` Package
3. Generate `requirements.txt`
4. Configure `.gitignore` for the Virtual Environment

## Practical Work Completed

* Created `venv1` inside the Day 43 folder
* Activated `venv1` using PowerShell
* Installed `requests`
* Tested `requests` successfully
* Received `Status Code: 200`
* Generated `requirements.txt`
* Created `.gitignore`
* Added `venv1/` to `.gitignore`
* Added `__pycache__/` to `.gitignore`
* Added `*.pyc` to `.gitignore`
* Added `.env` to `.gitignore`
* Understood that Python programs should remain outside `venv1`
* Understood that `venv1` contains the isolated Python environment
* Kept `.vscode` configuration because it can contain project-specific VS Code settings

## Previous Concepts Reinforced

* Python packages
* pip
* import
* modules
* Python project structure
* VS Code
* Git
* GitHub
* `.gitignore`
* Command Line / PowerShell

## Important Commands Learned

```bash
python -m venv venv1
```

```powershell
.\venv1\Scripts\Activate.ps1
```

```bash
python -m pip install requests
```

```bash
python -m pip freeze > requirements.txt
```

## Status

Completed ✅
