---
term: ATOMIC SWAP
---

Technology allowing the direct exchange of cryptocurrencies between two parties, without requiring trust or intermediaries.  These exchanges are called "atomic" because they can only result in two outcomes:
* Either the swap is successful, and both participants have effectively exchanged their cryptocurrencies;
*Or the exchange fails, and both parties retain their original funds.*

Atomic Swaps can occur either within the same cryptocurrency (referred to as a *coinswap*) or between different cryptocurrencies. Historically, they relied on "Hash Time-Locked Contracts" (HTLC), a time-locking system that ensure that either both parts of the trade are completed or neither is, thereby preserving the integrity of the participant's funds. This method required protocols capable of handling both scripts and timelocks. 

In recent years, however, there has been a shift toward using *Adaptor Signatures*, which offer several advantages:

- They eliminate the need for scripts, reducing operational costs;
- They do not need the use of identical hashes on both sides of the swap, improving privacy by breaking any visible link between the two transactions.