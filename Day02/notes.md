# Day 02: Tip Calculator

## Project Overview

A simple tip calculator that asks for the bill total, desired tip percentage, and number of people, then outputs what each person should pay.

## Objectives

- Practice numeric input handling with `int` and `float`
- Perform percentage calculations
- Use rounding for currency-friendly values
- Format output with f-strings

## How It Works

1. Greet the user.
2. Ask for the bill amount and convert to `float`.
3. Ask for a tip percentage (e.g., 10, 12, 15) and convert to `int`.
4. Ask how many people will split the bill and convert to `int`.
5. Compute tip, total bill, and per-person share.
6. Round to two decimals and display using an f-string.

## Code Walkthrough

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $") )
tip_percentage = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
```

- Gather inputs and convert to numeric types for math operations.

```python
tip_amount = (tip_percentage / 100) * bill
total_bill = bill + tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
```

- Calculate tip, total, and split the bill evenly; round to cents.

```python
print(f"Each person should pay ${final_amount:.2f}")
```

- Format output to always show two decimal places.

## Key Concepts

| Concept         | Example                         | Purpose                         |
| --------------- | ------------------------------- | ------------------------------- |
| Type conversion | `float(input(...))`             | Enable arithmetic on user input |
| Percentage math | `(tip_percentage / 100) * bill` | Derive tip value                |
| Division        | `total_bill / people`           | Split cost equally              |
| Rounding        | `round(value, 2)`               | Keep currency to two decimals   |
| f-strings       | `f"${value:.2f}"`               | Cleanly format monetary output  |

## Example Run

```
Welcome to the tip calculator!
What was the total bill? $150
What percentage tip would you like to give? 10 12 15 12
How many people to split the bill? 5
Each person should pay $33.60
```

## Potential Enhancements

- Validate inputs (non-empty, numeric, positive values)
- Allow custom tip percentages beyond preset suggestions
- Handle edge cases (e.g., zero people, zero/negative numbers)
- Support currency symbols/locale-aware formatting
- Provide a breakdown summary (bill, tip, total, per-person)
