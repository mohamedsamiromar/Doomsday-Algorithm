# Doomsday Algorithm

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A clean, efficient implementation of Conway's Doomsday Algorithm in Python. This algorithm allows you to calculate the day of the week for any given date.

## What is the Doomsday Algorithm?

The Doomsday Algorithm is a method devised by mathematician John Conway to mentally calculate the day of the week for any given date. The algorithm is based on the fact that certain dates in each month (called "doomsdays") always fall on the same day of the week within any given year.

For example, in any year, 4/4, 6/6, 8/8, 10/10, and 12/12 all fall on the same day of the week. Once you know what day of the week the doomsdays fall on in a particular year, you can use that as an anchor to figure out the day of the week for any other date.

## Features

- Calculate the day of the week for any date in the Gregorian calendar
- Support for both interactive and command-line usage
- Proper handling of leap years
- Input validation for dates
- Clean, well-commented code

## Installation

No external dependencies required! Just clone the repository:

```bash
git clone https://github.com/yourusername/doomsday-algorithm.git
cd doomsday-algorithm
```

## Usage

### Interactive Mode

```bash
python doomsday.py
```

Follow the prompts to enter a date in DD/MM/YYYY format.

### Command Line Mode

```bash
python doomsday.py <day> <month> <year>
```

Example:
```bash
python doomsday.py 25 12 2023
```

Output:
```
25/12/2023 was/is/will be a Monday
```

## How it Works

The algorithm follows these steps:

1. **Century Anchor**: Each century has an anchor day (0=Sunday, 1=Monday, etc.)
2. **Year Calculation**: Calculate the contribution of the specific year within the century
3. **Doomsday Calculation**: Combine the century anchor and year calculation
4. **Date Calculation**: Find the closest doomsday to the target date and calculate the offset

The mathematical formula is elegantly implemented in this script with detailed comments to help you understand each step.

## Algorithm Accuracy

The implementation is accurate for dates in the Gregorian calendar (from October 15, 1582 onwards). Note that historical dates might differ based on when different countries adopted the Gregorian calendar.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## Author

[Your Name Here] - [Your GitHub Profile]

---

*"Time is an illusion. Lunchtime doubly so." - Douglas Adams*