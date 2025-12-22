# Day 01: Band Name Generator

## Project Overview

A simple interactive program that generates a creative band name by combining a city name with a pet's name.

## Objective

Learn the fundamentals of Python including:

- `print()` function for output
- `input()` function for user interaction
- String concatenation
- Variables and data types

## How It Works

### Flow

1. Welcome message is displayed to the user
2. User is prompted to enter their hometown city
3. User is prompted to enter their pet's name
4. The program combines both inputs to generate a creative band name
5. Result is displayed to the user

### Code Breakdown

```python
print("Welcome to the Band Name Generator.")
```

- Displays welcome message to introduce the program

```python
city = input("What's the name of the city you grew up in?\n")
```

- Prompts user for a city name
- Stores the input in the `city` variable
- `\n` creates a newline before input is taken

```python
pet = input("What's your pet's name?\n")
```

- Prompts user for their pet's name
- Stores the input in the `pet` variable

```python
print("Your band name could be " + city + " " + pet)
```

- Concatenates three strings: the message + city + space + pet
- Displays the generated band name

## Key Concepts Learned

| Concept              | Example             | Purpose                  |
| -------------------- | ------------------- | ------------------------ |
| Variables            | `city = input(...)` | Store user input         |
| Input Function       | `input("prompt")`   | Get user input as string |
| Print Function       | `print(...)`        | Display output           |
| String Concatenation | `"text" + variable` | Combine strings          |
| Newline Character    | `\n`                | Add line breaks          |

## Example Output

```
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
New York
What's your pet's name?
Fluffy
Your band name could be New York Fluffy
```

## Potential Enhancements

1. **Better formatting**: Use f-strings instead of concatenation

   ```python
   print(f"Your band name could be {city} {pet}")
   ```

2. **Multiple suggestions**: Generate several band name combinations

3. **Input validation**: Ensure user doesn't enter empty strings

4. **Case handling**: Capitalize the output for better presentation

5. **Save results**: Write generated band names to a file

## Skills Applied

- ✅ Variable assignment
- ✅ User input handling
- ✅ String operations
- ✅ Basic output formatting
