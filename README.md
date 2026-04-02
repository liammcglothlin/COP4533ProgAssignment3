# COP4533 Programming Assignment 3

## Highest Value Longest Common Subsequence (HVLCS)

**Name:** Liam McGlothlin
**Course:** COP4533 – Algorithms
**Semester:** Spring 2026


# Overview

This project computes the **Highest Value Longest Common Subsequence (HVLCS)** between two strings.

Each character has an associated value, and the goal is to find a common subsequence that **maximizes total value**, not length.

The program outputs:

1. The maximum value
2. One optimal subsequence that achieves this value

---

# How to Run

### Run with input file:

```bash
python src/solve.py < data/example.in
```

### Example Input (`example.in`)

```
3
a 2
b 4
c 5
aacb
caab
```

### Example Output (`example.out`)

```
9
cb
```

---

# Assumptions

* Strings contain only characters listed in the alphabet input
* Character values are non-negative integers
* Input is well-formed
* Any optimal subsequence is acceptable if multiple exist

---

# Question 1: Empirical Comparison

I generated 10 input files with increasing string lengths (from 25 up to 250).

For each input:

* The HVLCS algorithm was executed
* Runtime was measured using Python timing functions

The results were recorded and plotted (see `runtime_graph.png`).

### Observation

The runtime increases as input size increases. The graph shows approximately **quadratic growth**.

### Explanation

The DP algorithm runs in:

[
O(nm)
]

When both strings have similar length (n), this becomes:

[
O(n^2)
]

This matches the observed runtime behavior.

---
# Question 2: Recurrence Equation

Let:

- OPT(i, j) = maximum total value of a common subsequence of A[1..i] and B[1..j]  
- v(x) = value of character x  

### Recurrence:

OPT(i, j) = 0, if i = 0 or j = 0  

If A[i] != B[j]:  
OPT(i, j) = max(OPT(i-1, j), OPT(i, j-1))  

If A[i] == B[j]:  
OPT(i, j) = max(OPT(i-1, j), OPT(i, j-1), v(A[i]) + OPT(i-1, j-1))  

---

### Explanation

At each position (i, j), we consider:

- Skipping a character from string A  
- Skipping a character from string B  
- Taking the character (only if they match)  

Even when characters match, taking them is not always optimal, so we take the maximum of all possibilities.

# Question 3: Algorithm and Complexity

### Pseudocode

```
HVLCS(A, B, val):
    n = length(A)
    m = length(B)

    create DP[0..n][0..m]

    for i = 0 to n:
        DP[i][0] = 0
    for j = 0 to m:
        DP[0][j] = 0

    for i = 1 to n:
        for j = 1 to m:
            if A[i] == B[j]:
                DP[i][j] = max(
                    DP[i-1][j],
                    DP[i][j-1],
                    DP[i-1][j-1] + val[A[i]]
                )
            else:
                DP[i][j] = max(
                    DP[i-1][j],
                    DP[i][j-1]
                )

    return DP[n][m]
```

### Time Complexity

[
O(nm)
]

### Space Complexity

[
O(nm)
]

---

# Project Structure

```
hw3/
│
├── src/
│   ├── solve.py
│   ├── q1_runner.py
│   └── graph_runtime.py
│
├── data/
│   ├── example.in
│   ├── example.out
│   ├── test1.in ... test10.in
│
├── runtime_results.csv
├── runtime_graph.png
└── README.md
```

---

# Reproducibility

To reproduce results:

1. Generate test cases for q1:

```bash
python src/q1_runner.py
```

2. Generate graph:

```bash
python src/graph_runtime.py
```

---

# Summary

This project implements a dynamic programming solution to compute the HVLCS efficiently.

The empirical results confirm the theoretical time complexity of (O(nm)), and the recurrence correctly models all possible optimal choices at each step.

---
