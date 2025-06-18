# TrimCalc

TrimCalc helps you calculate the trim size and trim weight for material rolls—ideal for printing and packaging professionals.

## Features

- **Trim Size Calculation:** Find the leftover width after slitting.
- **Trim Weight Calculation:** Estimate the weight of the trimmed portion.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/takdm/trimcalc.git
   cd trimcalc
   ```

2. **(Optional) Create a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Run the calculator:**
   ```bash
   python3 main.py
   ```

4. **Follow the prompts:**
   - Enter MR Size (inches)
   - Enter Slit Roll Size (mm)
   - Enter Number of Slits
   - Enter Label Roll Weight

## How It Works

- **Input:** MR size (inches), slit roll size (mm), number of slits, and roll weight.
- **Process:** Converts slit size to inches, calculates total slit width, computes trim size and weight.
- **Output:** Displays the trim size (inches) and trim weight.

---

**Example:**
```
Enter MR Size (inches): 40
Enter Slit Roll Size (mm): 100
Enter Number of Slits: 8
Enter Label Roll Weight: 50

Trim Size: 8.50 inches
Trim Weight: 10.63
```

---

## License

MIT License

