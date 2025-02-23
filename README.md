# bad-2025-puzzle-solution

## Description
This repository contains a solution to the problem of finding the longest sequence of numbers where each 2 starting digits of the next number are equal to the ending 2 digits of the previous number. 

**For example:**
- 1100**22**, **22**0033
- 9889**76**, **76**8989

The following pairs cannot be connected:
- **44**0909, **44**0909
- 1122**33**, 4422**33**
  
The task is to find the longest sequence of such numbers from all the numbers in the ```file.txt``` file (you can rename this file as you like by setting ```input_file``` variable in the main.py file).

**Example:**

We have the following list of numbers: 608017, 248460, 962282, 994725, 177092

The resulting sequence will be: 2484**60** -> **60**80**17** -> **17**7092

After omitting connected digits:
2484**60**80**17**7092

## Installation
Clone the repository:
```bash
git clone https://github.com/Nikitossik/bad-2025-puzzle-solution
```
Go to the root directory:
```bash
cd bad-2025-puzzle-solution
```
## Usage
Add your numbers to ```file.txt```, each number must be on the new line:
```bash
608017
248460
962282
994725
177092
```
Run the script:
```bash
python main.py

Highlighted string sequence: 24846080177092

Full sequence elements: 248460 -> 608017 -> 177092
```
