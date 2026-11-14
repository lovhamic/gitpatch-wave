# Security Policy

## Supported Versions

The table below indicates current security support status for GitPatch Wave releases.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | Yes                |
| < 1.0   | No                 |

## Reporting a Vulnerability

If you discover a security vulnerability within GitPatch Wave, please do not report it through public GitHub issues. Instead, report it privately through one of the following channels:

- Use GitHub Private Vulnerability Reporting on the repository.
- Email the project maintainer directly with details.

Please include:
- A description of the vulnerability and its potential impact.
- Step-by-step instructions or proof-of-concept demonstrating the issue.
- Proposed mitigations or patches if available.

You will receive an acknowledgment within 48 hours, followed by updates on investigation and remediation timelines.

## Threat Model and Expression Evaluation

### Evaluation Mechanism

GitPatch Wave evaluates user-defined mathematical expressions on the server via Python. The current evaluation context restricts built-in functions:

```python
eval(clean_eq, {"__builtins__": None}, safe_dict)
```

Where `safe_dict` exposes only authorized mathematical operations (`sin`, `cos`, `tan`, `exp`, `sqrt`, `pi`, `abs`, `log`, `log10`, `e`) and numerical variables.

### Operational Scope and Recommendations

1. **Intended Environment**: GitPatch Wave is designed as a local single-user mathematical exploration utility.
2. **Untrusted Networks**: Do not expose the development server (`app.py`) to untrusted public networks or the open internet without additional protection.
3. **Production Hardening**: For multi-tenant or public cloud deployments, replace the dynamic evaluator with an Abstract Syntax Tree (AST) validation parser or a sandboxed math expression library (such as `simpleeval` or `SymPy`) to strictly forbid arbitrary attribute access and object introspection.
