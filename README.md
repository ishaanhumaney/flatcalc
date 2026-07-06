# FlatCalc

A streamlined, text-based command-line calculator built with Python. It evaluates standard mathematical expressions, exponents, square roots, and custom $n$-th roots directly from your terminal. Instead of blindly passing strings to Python's execution engine, it uses custom token filtering and a restricted execution scope to keep runtime math parsing clean.

## Overview

Most simple Python calculators either rely on massive, over-engineered parsing libraries or take the shortcut of using a raw, insecure `eval()`. FlatCalc bridges that gap. It provides a lightweight interactive loop that processes mathematical inputs securely. By pairing a strict character whitelist with a sandboxed environment that strips away internal Python builtins, it protects the runtime engine while keeping calculation execution instantaneous.

## Key Features

* **Restricted Math Sandbox**: Strips `__builtins__` from the execution context to prevent arbitrary code execution vulnerabilities.
* **Input Validation Layer**: A strict character whitelist rejects malicious inputs or syntax syntax anomalies before they ever hit the engine.
* **Extended Math Notation**: Out-of-the-box support for `^` syntax (translated to `**` natively), `sqrt(x)`, and custom $n$-th roots using `root(x, n)`.
* **Zero Dependencies**: Pure Python standard library implementation. No pip installs or heavy configurations required.

## Tech Stack Breakdown

* **Language**: Python 3.x
* **Core Libraries**: `math` (for optimized floating-point square roots)
* **Execution Architecture**: Scoped `eval` mapping with custom closure injections for root computations.

## Prerequisites & Web-Based Quick Start

### Run Instantly via GitHub Codespaces (No setup required)
1. Click the **Code** button at the top of this repository.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. Once the terminal loads at the bottom, type:
   ```bash
   python main.py

### Local Setup
If you prefer running it locally, ensure you have Python 3 installed.
  1. Download or copy main.py.
  2. Open your terminal in the directory containing the file and execute:
       python main.py

## Project Structure
```bash
flatcalc
│
├── .github/
│      └── workflows/
│          └── ci.yml         # Multi-version automated syntax validation
├── .gitignore                # Standard Python environment exclusions
├── README.md                 # Documentation and architecture guide
└── main.py                   # Main application file containing parser and CLI loop
```
## Usage Examples
Once the interactive prompt calc> is active, you can pass regular calculations or custom functions:

Basic Arithmetic: 10 + 2 * (5 - 3) -> Returns 14

Exponents: 2^3 -> Returns 8

Square Root: sqrt(25) -> Returns 5.0

Cube / Custom Roots: root(8, 3) -> Returns 2.0

To exit the application, simply type quit.

## Roadmap
[ ] Add an implicit multiplication parser (e.g., parsing 2(3+5) to 2*(3+5)).

[ ] Implement history tracking to recall previous outputs via an underscore variables (_).

[ ] Build a lightweight test suite verifying boundary conditions for fraction exponents and zero-division handling.
