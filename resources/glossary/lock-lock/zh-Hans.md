---
term: LOCK (.LOCK)

---
Bitcoin Core 中用于锁定数据目录的文件。它在 bitcoind 或 Bitcoin-qt 启动时创建，以防止程序被重复启动而同时访问同一个数据目录。目的是防止冲突和数据损坏。如果软件意外停止运行，.lock 文件可能会保留，必须在重启 Bitcoin Core 前手动删除。
