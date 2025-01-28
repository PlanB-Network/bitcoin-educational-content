---
term: ATOMIC SWAP

---
Technology allowing the direct exchange of cryptocurrencies between two parties, without the need for trust and without requiring an intermediary. These exchanges are called "atomic" because they can only result in two outcomes:


- Either the exchange is successful, and both participants have effectively exchanged their cryptocurrencies;
- Or the exchange fails, and both participants leave with their original cryptocurrencies.

Atomic Swaps can be performed either with the same cryptocurrency, in which case it is also referred to as a "*coinswap*," or between different cryptocurrencies. Historically, they relied on "Hash Time-Locked Contracts" (HTLC), a time-locking system that guarantees the completion or total cancellation of the exchange, thus preserving the integrity of the funds of the parties involved. This method required protocols capable of handling both scripts and timelocks. However, in recent years, the trend has shifted towards the use of *Adaptor Signatures*. This second approach has the advantage of eliminating the need for scripts, thereby reducing operational costs. Its other major benefit is that it does not require the use of identical hashing for both parts of the transaction, which helps to avoid revealing a link between them.