# Day 13 - Debugging Techniques and Best Practices

## Topics Covered

- **Debugging Fundamentals**: Understanding what debugging is and why it matters
- **Common Error Types**: Syntax errors, runtime errors, and logical errors
- **Debugging Techniques**: Systematic approaches to finding and fixing bugs
- **Error Messages**: Reading and understanding Python error messages
- **Print Debugging**: Using print statements to trace code execution
- **VSCode Debugger**: Using breakpoints and step-through debugging
- **Best Practices**: Writing code that's easier to debug

## What is Debugging?

Debugging is the process of finding and fixing errors (bugs) in your code. It's a critical skill for every programmer.

### Why Bugs Happen

- Syntax errors (typos, missing colons, etc.)
- Logic errors (wrong algorithm or conditions)
- Runtime errors (invalid operations during execution)
- Off-by-one errors (incorrect loop ranges or indices)
- Type errors (wrong data types)
- Scope issues (variable not accessible)

## 10 Debugging Techniques

### 1. Describe the Problem

**Technique**: Clearly articulate what the code is supposed to do vs. what it's actually doing.

**Example Bug**:

```python
# Bug: Loop doesn't reach 20
for i in range(1, 20):
    if i == 20:
        print("You got it")
```

**Fix**:

```python
# Fixed: range(1, 21) includes numbers 1-20
for i in range(1, 21):  # range is exclusive of end
    if i == 20:
        print("You got it")
```

**Key Lesson**: `range(start, stop)` is exclusive of the stop value.

---

### 2. Reproduce the Bug

**Technique**: Find the exact conditions that cause the error.

**Example Bug**:

```python
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])  # IndexError when randint returns 6
```

**Fix**:

```python
# Lists are 0-indexed, so valid indices are 0-5
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
```

**Key Lesson**: Python lists are 0-indexed. A list with 6 items has indices 0-5.

---

### 3. Play Computer

**Technique**: Manually step through your code like a computer, tracking variable values.

**Example Bug**:

```python
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:  # Bug: People born in 1994 are skipped!
    print("You are a Gen Z.")
```

**Fix**:

```python
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:  # Include 1994
    print("You are a Gen Z.")
```

**Key Lesson**: Watch out for boundary conditions. Test edge cases!

---

### 4. Fix the Errors

**Technique**: Read error messages carefully - they tell you exactly what's wrong!

**Example Bug**:

```python
age = input("How old are you?")
if age > 18:  # TypeError: '>' not supported between 'str' and 'int'
    print("You can drive at age {age}.")  # Missing f before string
```

**Fix**:

```python
age = int(input("How old are you? "))  # Convert to int
if age >= 18:
    print(f"You can drive at age {age}.")  # Use f-string
```

**Key Lesson**:

- `input()` returns a string - convert it if you need a number
- Use `f""` for f-strings, not just `""`

---

### 5. Print is Your Friend

**Technique**: Use `print()` statements to see what's happening at each step.

**Example**:

```python
def calculate_total():
    pages = int(input("Number of pages: "))
    word_per_page = int(input("Words per page: "))

    # Add print statements to debug
    print(f"Debug: pages = {pages}")
    print(f"Debug: word_per_page = {word_per_page}")

    total_words = pages * word_per_page
    print(f"Debug: total_words = {total_words}")

    return total_words
```

**Key Lesson**: Print variables at each step to see where values go wrong.

---

### 6. Use a Debugger

**Technique**: Use VSCode's built-in debugger with breakpoints.

**How to Use VSCode Debugger**:

1. **Set a Breakpoint**: Click left of line number (red dot appears)
2. **Start Debugging**: Press F5 or click "Run and Debug"
3. **Step Through Code**:
   - F10: Step over (execute current line)
   - F11: Step into (enter function)
   - Shift+F11: Step out (exit function)
4. **Inspect Variables**: Hover over variables to see their values
5. **Watch Expressions**: Add variables to watch panel

**Example Bug**:

```python
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # Set breakpoint here
    print(b_list)
```

**Key Lesson**: Debuggers let you pause execution and inspect everything!

---

### 7. Take a Break

**Technique**: Step away when stuck - come back with fresh eyes.

**Why It Works**:

- Your brain continues working on the problem unconsciously
- Fresh perspective helps you see obvious mistakes
- Reduces frustration and mental fatigue

**When to Take a Break**:

- Stuck on the same bug for > 30 minutes
- Getting frustrated or tired
- Can't think of new approaches

**What to Do**:

- ☕ Get a coffee/tea
- 🚶 Go for a walk
- 🧘 Stretch or meditate
- 💬 Chat with a colleague about something else

---

### 8. Ask a Friend (or Rubber Duck)

**Technique**: Explain your code line-by-line to someone else.

**Rubber Duck Debugging**:

1. Get a rubber duck (or any object)
2. Explain your code to it, line by line
3. Often you'll find the bug while explaining!

**Why It Works**:

- Forces you to think about what the code actually does
- Verbalizing assumptions reveals flaws
- Slows you down to notice details

**What to Explain**:

- What you're trying to do
- What the code currently does
- What each line is supposed to accomplish
- What values variables should have

---

### 9. Run Code Often

**Technique**: Run and test your code frequently as you write it.

**Good Practice** ✅:

```
Write 5-10 lines → Run → Test → Write more
```

**Bad Practice** ❌:

```
Write 100 lines → Run → Find 50 bugs
```

**Benefits**:

- Catch bugs immediately while context is fresh
- Know exactly which recent change caused the bug
- Build confidence that working code stays working
- Faster development overall

---

### 10. Search for Help

**Technique**: Use Google, StackOverflow, and documentation.

**How to Search Effectively**:

1. **Copy the Error Message**:

   ```
   "IndexError: list index out of range" python
   ```

2. **Search for Concepts**:

   ```
   "python list indexing start at 0 or 1"
   ```

3. **Check Official Documentation**:

   - [Python Docs](https://docs.python.org/)
   - Library documentation

4. **Use StackOverflow**:
   - Search before asking
   - Look for accepted answers
   - Check answer dates (newer Python versions may differ)

**Resources**:

- 🔍 Google: Quick searches
- 📚 StackOverflow: Specific problems
- 📖 Python Docs: Official reference
- 💬 Reddit r/learnpython: Community help
- 🐙 GitHub Issues: Library-specific problems

---

## Common Error Types in Python

### Syntax Errors

Code violates Python's grammar rules - won't run at all.

```python
# SyntaxError: invalid syntax
if x > 5
    print("Greater")  # Missing colon

# SyntaxError: EOL while scanning string literal
message = "Hello  # Missing closing quote

# SyntaxError: unmatched ')'
result = (5 + 3))  # Extra closing parenthesis
```

**How to Fix**: Read the error message, check the line indicated and the line before it.

---

### IndentationError

Python requires consistent indentation.

```python
# IndentationError: expected an indented block
def my_function():
print("Hello")  # Must be indented

# IndentationError: unexpected indent
x = 5
    y = 10  # Unexpected indent
```

**How to Fix**: Use consistent indentation (4 spaces is standard).

---

### NameError

Variable or function name not defined.

```python
# NameError: name 'age' is not defined
print(age)  # age was never defined

# NameError: name 'Print' is not defined
Print("Hello")  # Python is case-sensitive, should be print()
```

**How to Fix**: Check spelling, capitalization, and that variable was defined before use.

---

### TypeError

Wrong type of data for an operation.

```python
# TypeError: can only concatenate str (not "int") to str
result = "Age: " + 25  # Can't add string and int

# TypeError: '>' not supported between 'str' and 'int'
age = "25"
if age > 18:  # Comparing string to int
    pass
```

**How to Fix**: Convert types appropriately (`int()`, `str()`, `float()`).

---

### IndexError

Trying to access an index that doesn't exist.

```python
# IndexError: list index out of range
fruits = ["apple", "banana"]
print(fruits[2])  # Only indices 0 and 1 exist
```

**How to Fix**: Check list length, remember 0-indexing.

---

### KeyError

Trying to access a dictionary key that doesn't exist.

```python
# KeyError: 'age'
person = {"name": "John"}
print(person["age"])  # Key 'age' doesn't exist
```

**How to Fix**: Check if key exists or use `.get()` method.

---

### ValueError

Correct type but inappropriate value.

```python
# ValueError: invalid literal for int() with base 10: 'abc'
num = int("abc")  # Can't convert 'abc' to integer
```

**How to Fix**: Validate input before conversion.

---

### Logic Errors

Code runs without errors but produces wrong results.

```python
# Bug: Calculating area incorrectly
def circle_area(radius):
    return 3.14 * radius  # Should be radius ** 2

# Bug: Off-by-one error
for i in range(1, 10):  # Meant to include 10
    print(i)
```

**How to Fix**: Use print debugging, test with known inputs, step through logic.

---

## Debugging Best Practices

### Write Debuggable Code

1. **Use Descriptive Names**:

   ```python
   # Bad
   x = 5

   # Good
   user_age = 5
   ```

2. **Keep Functions Small**:

   - One function = one responsibility
   - Easier to test and debug

3. **Add Comments for Complex Logic**:

   ```python
   # Calculate compound interest: A = P(1 + r/n)^(nt)
   final_amount = principal * (1 + rate/compounding_frequency) ** (compounding_frequency * years)
   ```

4. **Use Meaningful Error Messages**:
   ```python
   if age < 0:
       raise ValueError(f"Age cannot be negative: {age}")
   ```

### Test as You Go

- ✅ Write a function → Test it → Move on
- ✅ Use simple test cases first
- ✅ Test edge cases (0, negative, empty, very large)

### Use Version Control

- Commit working code frequently
- Can revert to last working version
- See what changed when bug appeared

### Read Documentation

- Understand what functions/methods actually do
- Check return types
- Look for examples

---

## Debugging Mindset

### Remember:

1. **Bugs are Normal** 🐛

   - Every programmer deals with bugs
   - Even experts write buggy code

2. **Debugging is a Skill** 📈

   - Gets easier with practice
   - Learn patterns of common mistakes

3. **Be Systematic** 🔍

   - Don't randomly change things
   - Form hypothesis → Test → Evaluate

4. **Stay Calm** 😌

   - Frustration makes debugging harder
   - Take breaks when needed

5. **Learn from Bugs** 📚
   - Each bug teaches you something
   - Keep notes of tricky bugs you solved

---

## Quick Debugging Checklist

When you encounter a bug:

- [ ] Read the error message carefully
- [ ] Check the line number mentioned
- [ ] Verify variable types (use `type()`)
- [ ] Add print statements to trace execution
- [ ] Check for typos in variable/function names
- [ ] Verify indentation is correct
- [ ] Test with simple input first
- [ ] Check boundary conditions
- [ ] Use the debugger to step through code
- [ ] Search error message online
- [ ] Take a break if stuck > 30 minutes
- [ ] Explain code to someone (or something)

---

## Summary

Debugging is about being methodical and persistent. Use a combination of techniques:

1. **Understand** the problem clearly
2. **Reproduce** the bug consistently
3. **Isolate** where the bug occurs
4. **Fix** the bug
5. **Test** that the fix works
6. **Learn** from the experience

Practice these techniques, and debugging will become second nature! 🚀
