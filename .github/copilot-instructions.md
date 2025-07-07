# GitHub Copilot Instructions

This repository contains Python solutions and exercises for LeetCode-style algorithm and data structure problems.

## General Guidelines

- Use Python 3.10+ syntax when applicable.
- Focus on clarity, correctness, and readability over performance unless otherwise specified.
- Use **type hints** for all function arguments and return values.
- Include **docstrings** for each function explaining the purpose, inputs, and outputs.
- Avoid using unnecessary libraries — stick to Python’s standard library unless otherwise specified.
- Favor idiomatic Python and list comprehensions where appropriate.
- Use descriptive and consistent naming conventions (e.g., `two_sum`, `max_subarray_sum`).
- Each solution should be written as a function, optionally accompanied by test cases using `assert` statements.

## Examples

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    """
    index_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in index_map:
            return [index_map[diff], i]
        index_map[num] = i
    return []
```