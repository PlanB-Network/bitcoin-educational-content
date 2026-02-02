---
term: Knapsack solver

definition: Phương pháp chọn xu cũ trong Bitcoin Core, đã được thay thế bằng Branch-and-Bound.
---
An old method used for selecting coins in the Bitcoin Core wallet before version 0.17. The Knapsack Solver attempts to solve the coin selection problem by iteratively and randomly choosing UTXOs, and adding them up by subsets, with the goal of minimizing fees and the size of the transaction. This method has since been replaced by *Branch-and-Bound*.