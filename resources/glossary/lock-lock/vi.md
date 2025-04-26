---
term: LOCK (.LOCK)

---
File used in Bitcoin Core for locking the data directory. It is created when bitcoind or Bitcoin-qt starts to prevent multiple instances of the software from accessing the same data directory simultaneously. The goal is to prevent conflicts and data corruption. If the software stops unexpectedly, the .lock file may remain and must be manually deleted before restarting Bitcoin Core.