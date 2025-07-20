---
term: BLK*.DAT
---

Bitcoin Core 中儲存 Blockchain 原始區塊資料的檔案名稱。每個檔案都以其名稱中的唯一號碼來識別。因此，區塊會以時間順序記錄，從檔案 blk00000.dat 開始。當這個檔案達到最大容量時，接下來的區塊會記錄在 blk00001.dat，然後是 blk00002.dat，依此類推。每個 blk 檔案的最大容量為 128 mebibytes (MiB)，相當於 134 MB 多一點。自 0.8.0 版起，這些檔案已移至 `/blocks` 資料夾。