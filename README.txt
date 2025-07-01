
# Return/Exchange Cycle Detector

## Description
This project detects potential fraud cycles in product return/exchange patterns using graph cycle detection (DFS).

## How to Run
1. Run the Python file: `python main.py`
2. Enter the number of return/exchange transactions.
3. Enter each transaction as "ProductA ProductB" indicating that ProductA was returned for ProductB.

## Example
```
Input:
4
P1 P2
P2 P3
P3 P1
P4 P5

Output:
Cycle detected! Potential fraud in return/exchange patterns.
```

## Data Structures Used
- Graph (Adjacency List)
- DFS for cycle detection
