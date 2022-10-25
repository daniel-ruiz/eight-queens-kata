# Eight Queens Kata

## Description
This repository was created as a way to learn about backtracking algorithms while using TDD.
The goal of this program is to solve the [Eight Queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle), which is a known problem whose solution can be calculated using this technique.

## How to run the project
This project uses some dependencies that are meant to be managed by [pipenv](https://pipenv.pypa.io/en/latest/index.html). 
So first of all, we'll need to install this Python library.

```
pip install pipenv
```

After that, we will install the project dependencies.

```
pipenv install --dev --deploy
```

We can then run the test suite by executing the following command:

```
pytest
```

If we want to print a solution of the problem, we can execute the following script in a Python shell:

```python
from eight_queens_kata.solver import EightQueensSolver

solution = EightQueensSolver().solve()

print(solution)
```

Make sure you are in the `src` folder so that the `eight_queens_kata` package is found.
