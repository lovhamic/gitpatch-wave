# Contributing to GitPatch Wave

Thank you for your interest in contributing to GitPatch Wave. This document provides guidelines and instructions for submitting contributions, reporting defects, and participating in project development.

## Code of Conduct

All contributors and maintainers are expected to adhere to the project Code of Conduct detailed in `CODE_OF_CONDUCT.md`. Professional and respectful communication is required across all interactions.

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Git version control
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Local Environment Setup

1. Fork the repository on GitHub.
2. Clone your forked repository locally:

```bash
git clone https://github.com/<your-username>/gitpatch-wave.git
cd gitpatch-wave
```

3. Create and activate an isolated virtual environment:

```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

4. Install runtime and development dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

5. Verify local installation:

```bash
python app.py
```

Navigate to `http://127.0.0.1:8080/` in your browser.

## Development Workflow

1. Create a descriptive feature branch from `main`:

```bash
git checkout -b feature/dynamic-colormap
# or for bug fixes:
git checkout -b fix/equation-parser-space
```

2. Make focused, atomic commits with clear imperative messages:

```bash
git commit -m "Add log2 and sinh to allowed mathematical functions"
```

3. Write or update unit tests in `tests/test_app.py` for any new logic or bug fixes.

4. Run the automated test suite locally:

```bash
python -m unittest discover tests
```

5. Run static linting checks:

```bash
flake8 app.py tests/
```

6. Push your branch to GitHub and open a Pull Request against `main`.

## Coding Standards

- Python code must comply with PEP 8 standards.
- Functions and public routes must include docstrings documenting parameters, return types, and exceptions.
- JavaScript should maintain vanilla DOM practices without adding heavy external frontend dependencies unless approved via an issue discussion.
- All documentation and commits must maintain a professional tone without emojis.

## Reporting Issues

When reporting an issue, use the GitHub Bug Report template and include:
- A clear, descriptive summary of the problem.
- Exact steps to reproduce the issue.
- Expected behavior versus actual behavior.
- Operating system, browser, and Python versions.
- Terminal stack traces or browser console logs if applicable.
