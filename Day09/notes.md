# Day 09 - Dictionaries and Nesting

## Topics Covered

- **Dictionaries**: Key-value pairs data structure
- **Dictionary Operations**: Adding, updating, and accessing values
- **Iterating through dictionaries**
- **Nesting**: Lists in dictionaries, dictionaries in dictionaries

## Key Concepts

### Dictionary Basics

```python
# Creating a dictionary
my_dict = {
    "key1": "value1",
    "key2": "value2"
}

# Accessing values
print(my_dict["key1"])

# Adding new key-value pairs
my_dict["key3"] = "value3"

# Updating existing values
my_dict["key1"] = "new_value"

# Looping through a dictionary
for key in my_dict:
    print(key)  # Prints the key
    print(my_dict[key])  # Prints the value
```

### Nesting

```python
# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

# Nesting dictionaries in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]
```

## Project: Secret Auction Program

### Description

Created a blind auction program where multiple bidders can place bids secretly. The program:

1. Takes bidder names and bid amounts
2. Clears the screen between bidders for privacy
3. Stores all bids in a dictionary
4. Determines the highest bidder
5. Announces the winner

### Features

- Dictionary to store bidder names as keys and bid amounts as values
- Function to find the highest bidder
- Loop to handle multiple bidders
- Screen clearing for bid privacy
- ASCII art logo for visual appeal

### Implementation Highlights

```python
# Dictionary to store bids
bids = {}

# Function to find winner
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            winner = bidder
            highest_bid = bid_amount
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Main program logic
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    # ... continues
```

## Learning Outcomes

- Understanding dictionaries as a key-value data structure
- Iterating through dictionaries to find specific values
- Using dictionaries to store and manage related data
- Applying dictionary operations to solve real-world problems
- Working with nested data structures
- Building an interactive program with user input and data processing

## Notes

- Dictionaries are mutable (can be changed after creation)
- Keys must be immutable (strings, numbers, tuples)
- Values can be of any data type
- Use dictionaries when you need to associate values with keys
- Nesting allows for complex data structures to represent hierarchical data
