# Calculator (PyQt5)

<p align="center">
  <img src="https://github.com/user-attachments/assets/86c9341c-3293-4d56-ab40-16da6c7970b9" width="45%" />
  <img src="https://github.com/user-attachments/assets/ed3503af-bf8d-4a9d-b737-cb153cfdd8db" width="45%" />
</p>




A simple desktop calculator application built with Python and PyQt5. This project demonstrates a small GUI calculator with basic numeric input, arithmetic, and a styled interface.

## Features
- Graphical calculator UI using PyQt5
- Numeric buttons (0–9) and decimal point
- Basic arithmetic operations (+, -, ×, ÷)
- Clear and backspace controls
- Result rounding to 2 decimal places in the current implementation
- Simple CSS-like styling via Qt setStyleSheet

## Requirements
- Python 3.8+ (should work on 3.8 — 3.11)
- PyQt5

## Quick start — run locally
1. Clone the repo:
   ```bash
   git clone https://github.com/shabeeh-ahmed/calculator.git
   cd calculator
   ```

2. Create and activate a virtual environment (recommended):
   - macOS / Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

3. Install PyQt5:
   ```bash
   pip install PyQt5
   ```

4. Run the app:
   ```bash
   python calculator.py
   ```

The calculator window should open. Enter numbers and operations using the on-screen buttons.

## Project structure
- `calculator.py` — Main application source (GUI and logic)
- `.gitignore` — ignores __pycache__ and .venv

## Notes & Known issues
I inspected the code while preparing this README; a few behaviors and bugs are worth noting:
- The `nine()` function currently appends `'8'` instead of `'9'`, so the 9 button does not work correctly.
- The minus (`-`), multiply (`x`), divide (`÷`), and percent (`%`) buttons are created but not all have click handlers wired in the same way as others (only some buttons connect to methods). You may want to add/confirm `.clicked.connect(...)` handlers for them.
- Percent functionality is present as a button but lacks implementation in the code.
- The app uses Python's `eval()` to evaluate expressions. Be careful: `eval()` can be dangerous with untrusted input. For a local desktop calculator this is acceptable, but consider parsing or a safe evaluator for production or when executing arbitrary input.
- The decimal handling uses `allow_dot` to prevent multiple dots, but dot handling around operators could be tightened (e.g., entering `1.+.2` should be prevented).
- Results are rounded to 2 decimal places (via `round(result, 2)`). You can adjust precision as needed.

## How to contribute
- Fix bugs (for example: correct `nine()` to append `'9'`; add missing click handlers; implement percent).
- Add keyboard input support (so users can type numbers and operators).
- Replace `eval()` with a safer expression parser.
- Add unit tests / UI tests if desired.

Steps to contribute:
1. Fork the repo.
2. Create a feature branch: `git checkout -b fix/nine-button`.
3. Make your changes and commit them.
4. Push and open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
Repository owner: @shabeeh-ahmed
