# Day 32 — Exercise 4: Secret Code Language

## Lecture
Lecture 40

## Topic
Exercise 4 — Secret Code Language

## Overview

Built an interactive Python program that can encode and decode
messages using the rules given in Exercise 4.

The project processes messages word-by-word and applies different
rules depending on the length of each word.

## Coding Rules

### Word length >= 3
- Remove the first character
- Append it at the end
- Add three random characters at the beginning and end

### Word length < 3
- Reverse the word

## Decoding Rules

### Word length < 3
- Reverse the word

### Word length >= 3
- Remove three characters from the beginning and end
- Move the last remaining character to the beginning

## CONCEPT OF "key":
- The "key" is NOT an encryption/password key.
It represents the NUMBER OF RANDOM CHARACTERS added to BOTH the beginning and end of every word containing at least 3 characters.

- Example with key = 3:

prince
  ↓
rincep
  ↓
abc + rincep + xyz
  ↓
abcrincepxyz

## Concepts Covered

- Strings
- Lists
- `split()`
- `join()`
- String slicing
- `len()`
- `for` loop
- `while` loop
- `if-elif-else`
- `match-case`
- `break`
- `continue`
- Functions
- User input
- Exception handling
- Random character generation

## Practice Programs

1. Basic Secret Code
2. Secret Code Using Functions
3. Secret Code Menu
4. Final Secret Code Project

## Mini Project

Final version added to:

`Mini_Projects/03_Secret_Code_Language.py`

## Status

Completed ✅