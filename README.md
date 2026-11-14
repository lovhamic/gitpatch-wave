# GitPatch Wave

GitPatch Wave is an interactive wave mechanics and mathematics visualization application featuring a Git-inspired dark user interface. It provides real-time numerical plotting of arbitrary mathematical wave functions, custom parameter manipulation via sliders, time-dependent wave propagation, and composite wave superposition analysis.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Mathematical Principles](#mathematical-principles)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Quick Start](#quick-start)
- [User Interface and Controls](#user-interface-and-controls)
- [Mathematical Function Reference](#mathematical-function-reference)
- [Production Deployment](#production-deployment)
- [Docker Containerization](#docker-containerization)
- [Standalone Desktop Executable](#standalone-desktop-executable)
- [Running Automated Tests](#running-automated-tests)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

In physics and mathematics, wave superposition governs phenomena ranging from acoustic interference and electromagnetic radiation to quantum wave packet behavior. GitPatch Wave translates these concepts into an exploratory computational canvas.

Users can define multiple independent wave equations, declare arbitrary custom variables (e.g., amplitude, wave number, angular frequency), dynamically modify values using sliders or precision numeric inputs, and observe both individual wave modes and their resultant interference pattern rendered at up to 60 frames per second.

---

## Key Features

- **Multi-Wave Plotting**: Define and render multiple mathematical equations concurrently with color-coded path visualization.
- **Dynamic Parameter Binding**: Create custom variables (e.g., `A`, `k`, `w`, `phi`) with customizable slider bounds and instantaneous updates.
- **Wave Superposition Engine**: Real-time point-by-point summation of active wave components rendered with high-contrast glow illumination.
- **Live Time Evolution**: Continuous animation mode (`Live Exec`) advancing the time parameter `t` using `requestAnimationFrame`.
- **Interactive Canvas Navigation**: Click-and-drag panning, scroll-wheel zooming, and real-time world-coordinate tracking under the cursor.
- **Dual Display Modes**: Toggleable Cartesian grid mesh with adaptive numerical axis labeling.
- **Zero-Dependency Frontend**: Pure HTML5 Canvas 2D and vanilla JavaScript without external UI framework bloat.
- **Vectorized Evaluation Engine**: Server-side NumPy computation sampling 1,000 points across the active viewport per calculation.
- **Packaging and Distribution**: Built-in support for standalone desktop compilation via PyInstaller and containerization via Docker.

---

## Mathematical Principles

### Wave Function Formulation

GitPatch Wave evaluates one-dimensional spatial wave equations propagating through time:

$$y(x, t) = f(x, t)$$

Standard harmonic wave equations frequently modeled in the tool take the form:

$$y_i(x, t) = A_i \sin(k_i x - \omega_i t + \phi_i)$$

Where:
- $A$: Amplitude (peak deviation from equilibrium)
- $k$: Wave number ($k = \frac{2\pi}{\lambda}$, where $\lambda$ is wavelength)
- $\omega$: Angular frequency ($\omega = 2\pi f$, where $f$ is frequency)
- $t$: Time parameter (driven incrementally during Live Exec mode)
- $\phi$: Phase shift

### The Principle of Superposition

When two or more waves traverse the same medium simultaneously, the net displacement at any point is the algebraic sum of the displacements of the individual waves:

$$y_{\text{total}}(x, t) = \sum_{i=0}^{n-1} y_i(x, t)$$

GitPatch Wave computes this summation vectorially across 1,000 points sampled along the visible horizontal domain $[x_{\min}, x_{\max}]$.

---

## Technology Stack

### Backend
- **Python 3.9+**: Core application runtime.
- **Flask**: Microframework for routing, asset delivery, and calculation endpoints.
- **NumPy**: Vectorized array operations and mathematical primitives.
- **Gunicorn**: Production WSGI HTTP server.

### Frontend
- **HTML5 Canvas**: Hardware-accelerated 2D raster plotting.
- **Vanilla JavaScript (ES6+)**: Event handling, state management, and render loops.
- **Modern CSS3**: Dark mode UI styling with custom typography (Rajdhani and JetBrains Mono).

### Packaging and Testing
- **PyInstaller**: Standalone cross-platform desktop binary compilation.
- **Docker**: Containerized deployment.
- **Python unittest / pytest**: Comprehensive automated unit test coverage.

---

## Repository Structure

```
gitpatch-wave/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml          # GitHub Issue form for defects
│   │   ├── feature_request.yml     # GitHub Issue form for enhancements
│   │   └── config.yml              # Issue template configuration
│   ├── workflows/
│   │   └── ci.yml                  # GitHub Actions CI workflow (multi-OS/Python)
│   └── PULL_REQUEST_TEMPLATE.md    # Pull Request submission checklist
├── docs/
│   ├── API_REFERENCE.md            # HTTP API endpoint specifications
│   └── ARCHITECTURE.md             # Architecture, data flow, and coordinate math
├── scripts/
│   └── build_exe.py                # PyInstaller build automation script
├── static/
│   └── script.js                   # Canvas rendering engine and UI controller
├── templates/
│   ├── index.html                  # Main plotter interface
│   └── intro.html                  # Procedural splash screen
├── tests/
│   ├── __init__.py                 # Test package marker
│   └── test_app.py                 # Automated unit tests for endpoints and math
├── .dockerignore                   # Docker build exclusion rules
├── .editorconfig                   # Cross-editor formatting specifications
├── .gitattributes                  # Line ending and binary handling rules
├── .gitignore                      # Git repository exclusion rules
├── app.py                          # Flask application server and calculation logic
├── CODE_OF_CONDUCT.md              # Contributor Covenant Code of Conduct
├── CONTRIBUTING.md                 # Contribution and development guidelines
├── Dockerfile                      # Production container image definition
├── GitPatchWave.spec               # PyInstaller specification file
├── LICENSE                         # MIT License
├── Procfile                        # Platform process definition (Gunicorn)
├── pyproject.toml                  # PEP 517/621 project configuration
├── README.md                       # Main project documentation
├── requirements.txt                # Production Python dependencies
└── requirements-dev.txt            # Development and testing dependencies
```

---

## Prerequisites

Before running the project, ensure your environment meets the following requirements:

- **Python**: Version 3.9, 3.10, 3.11, 3.12, 3.13, or 3.14.
- **pip**: Python package manager (version 21.0 or higher recommended).
- **Web Browser**: Modern browser with HTML5 Canvas and ES6 support (Chrome, Firefox, Safari, Edge).

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/lovhamic/gitpatch-wave.git
cd gitpatch-wave
```

### 2. Create and Activate a Virtual Environment

It is recommended to run the project within an isolated virtual environment:

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the core dependencies:

```bash
pip install -r requirements.txt
```

To install development, testing, and build dependencies:

```bash
pip install -r requirements-dev.txt
```

---

## Quick Start

Start the local development server:

```bash
python app.py
```

The application initiates the Flask development server on `http://127.0.0.1:8080/` and automatically launches your default web browser after approximately 1.5 seconds.

### Environment Variable Overrides

You can customize runtime behavior using environment variables:

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `HOST` | `127.0.0.1` | Network interface to bind the server to. |
| `PORT` | `8080` | Port number to listen on. |
| `NO_BROWSER` | `0` | Set to `1` or `true` to suppress automatic browser launch. |

Example running on custom port without browser launch:

```bash
PORT=5000 NO_BROWSER=1 python app.py
```

---

## User Interface and Controls

### Interface Components

1. **Functions Panel**:
   - Displays active mathematical wave functions.
   - Click **`+ New Branch (Eq)`** to add an equation.
   - Click the red **`x`** button next to any equation to remove it.
   - Equations update the canvas automatically upon typing.

2. **Parameters Panel**:
   - Displays dynamic scalar variables available for use in equations.
   - Click **`+ New Commit (Var)`** to introduce a variable.
   - Edit the variable name directly in the blue label field.
   - Adjust values using either the slider or the precision numeric box.
   - Default variable ranges: `min=0`, `max=10`, `step=0.1`.

3. **Superposition Toggle (`MERGE WAVES (SUM)`)**:
   - When checked, dims individual wave lines and overlays the calculated algebraic sum as a bright, glowing white curve.

4. **Live Execution (`Live Exec`)**:
   - Enables continuous animation by advancing the time parameter `t` by `0.1` units per animation frame.

5. **Grid Mesh (`Grid Mesh`)**:
   - Toggles Cartesian coordinate axes and grid lines with live axis markers.

6. **Coordinate Readout**:
   - Displays real-time Cartesian coordinates $(x, y)$ corresponding to the exact cursor position on the canvas.

### Canvas Interactions

- **Pan (Translate)**: Click and drag anywhere on the canvas to pan across the horizontal and vertical domains.
- **Zoom (Scale)**: Rotate the mouse scroll wheel forward to zoom in, or backward to zoom out.
- **Resize**: Canvas dimensions dynamically adapt to browser window resizing events.

---

## Mathematical Function Reference

The backend evaluation engine provides access to the following functions and constants:

| Function / Constant | Mathematical Representation | Example Usage |
| ------------------- | --------------------------- | ------------- |
| `sin(u)` | $\sin(u)$ | `sin(x - t)` |
| `cos(u)` | $\cos(u)$ | `cos(2*x + t)` |
| `tan(u)` | $\tan(u)$ | `tan(0.1*x)` |
| `exp(u)` | $e^u$ | `exp(-x^2)` |
| `sqrt(u)` | $\sqrt{u}$ | `sqrt(abs(x))` |
| `abs(u)` | $\|u\|$ | `abs(sin(x))` |
| `log(u)` | $\ln(u)$ | `log(abs(x) + 1)` |
| `log10(u)` | $\log_{10}(u)$ | `log10(abs(x) + 1)` |
| `pi` | $\pi \approx 3.14159265$ | `sin(2*pi*x)` |
| `e` | $e \approx 2.71828182$ | `e^(-x^2)` |
| `x` | Domain coordinate vector | `-` |
| `t` | Elapsed time parameter | `-` |
| `^` or `**` | Exponentiation ($u^v$) | `x^2` or `x**2` |

### Equation Examples

- **Traveling Wave**:
  ```
  A * sin(k*x - w*t)
  ```
  *(Requires variables `A`, `k`, and `w`)*

- **Standing Wave**:
  ```
  2 * A * sin(k*x) * cos(w*t)
  ```

- **Gaussian Wave Packet**:
  ```
  exp(-0.2 * (x - t)^2) * cos(3 * (x - t))
  ```

- **Beat Frequency Interference**:
  Equation 0:
  ```
  sin(5.0 * x - 2.0 * t)
  ```
  Equation 1:
  ```
  sin(5.5 * x - 2.2 * t)
  ```
  *(Enable `MERGE WAVES (SUM)` to view the resulting envelope)*

---

## Production Deployment

For production deployments, execute the application using Gunicorn (included in `requirements.txt`):

```bash
gunicorn --bind 0.0.0.0:8080 --workers 4 --threads 2 app:app
```

### Deploying to Platform-as-a-Service (PaaS)

A `Procfile` is provided in the repository root for compatibility with deployment platforms such as Heroku, Render, and Railway:

```procfile
web: gunicorn app:app
```

Ensure the platform's `PORT` environment variable is exposed, which `gunicorn` reads automatically.

---

## Docker Containerization

A lightweight Docker configuration is included for running the application in isolated container environments.

### 1. Build the Docker Image

```bash
docker build -t gitpatch-wave:latest .
```

### 2. Run the Container

```bash
docker run -d -p 8080:8080 --name gitpatch-wave gitpatch-wave:latest
```

Navigate to `http://localhost:8080` in your web browser.

---

## Standalone Desktop Executable

GitPatch Wave can be compiled into a single self-contained executable file that requires no external Python installation on client machines.

### Building with the Automated Script

Ensure development dependencies are installed:

```bash
pip install -r requirements-dev.txt
```

Run the build automation script:

```bash
python scripts/build_exe.py
```

### Building with the PyInstaller Specification File

Alternatively, invoke PyInstaller directly using the provided `.spec` configuration:

```bash
pyinstaller GitPatchWave.spec
```

The resulting standalone executable will be generated inside the `dist/` directory:
- **Windows**: `dist/GitPatchWave.exe`
- **Linux / macOS**: `dist/GitPatchWave`

When launched, the executable automatically initializes the embedded web server and opens the UI in the default system browser.

---

## Running Automated Tests

The repository includes a comprehensive unit test suite covering routing, numerical calculation accuracy, superposition correctness, variable parsing, and error handling.

### Run with Python unittest (Built-in)

```bash
python -m unittest discover tests
```

### Run with pytest

```bash
pytest
```

### Code Style and Quality Checks

To verify code quality and style conformity:

```bash
flake8 app.py tests/
```

---

## Security Considerations

### Expression Evaluation Model

GitPatch Wave evaluates user-defined mathematical equations on the server using Python. The execution environment restricts available built-in functions:

```python
eval(clean_eq, {"__builtins__": None}, safe_dict)
```

Where `safe_dict` permits only verified mathematical functions and user-defined numeric constants.

### Operational Guidelines

- **Local Use**: GitPatch Wave is designed and intended for local, single-user computational exploration and classroom demonstrations.
- **Public Hosting**: If deploying this service to public or untrusted networks, replace the dynamic evaluator with an Abstract Syntax Tree (AST) validation parser or a grammar-restricted math parser (such as `simpleeval` or `SymPy`) to eliminate any potential object introspection vectors.

For complete vulnerability reporting instructions, refer to `SECURITY.md`.

---

## Contributing

Contributions are welcome. Please read `CONTRIBUTING.md` for guidelines on setting up a development environment, submitting issues, following coding standards, and opening pull requests.

All participants must abide by the `CODE_OF_CONDUCT.md`.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.

```
Copyright (c) 2026 lovhamic
```
