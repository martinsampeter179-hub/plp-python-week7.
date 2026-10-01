# PLP Python Week 7 Assignment

## File Descriptions
* `list_warmup.py`: Demonstrates basic Python list operations including index access, appending, removing items, and checking list length.
* `shopping_list.py`: An interactive menu-driven program that manages a shopping list with safe removal and loop controls.
* `list_report.py`: Analyzes a list of grocery items using loops to display numbered items, count items over 4 characters, and find the longest item name.

## Reflection
It is safer to check if an item exists in a list using the `in` operator before calling `.remove()` because calling `.remove()` on an item that is not present raises a `ValueError`. Checking first prevents the program from crashing abruptly and allows you to handle missing items gracefully with a clear message to the user.
