# TrimCalc

This project is designed to help users calculate the trim size and trim weight based on input measurements. It is particularly useful for those working with material rolls in industries such as printing and packaging.

## Features

- Calculate the trim size of the material roll.
- Calculate the trim weight of the material roll.

## How It Works

The script prompts the user to input the following data:
1. MR Size in inches.
2. Slit roll size in millimeters.
3. Number of slits across the roll.
4. Label roll weight.

Based on these inputs, the script performs the following calculations:
1. Converts the slit roll size from millimeters to inches.
2. Calculates the trim size by subtracting the total slit sizes from the MR size.
3. Calculates the trim weight using the roll weight and the trim size.

The results are then displayed to the user.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/takdm/trimcalc.git
   cd trimcalc
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   python3 main.py
   
