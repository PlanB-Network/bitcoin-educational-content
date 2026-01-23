---
term: Anchors.dat
definition: 一個Bitcoin Core文件，存儲客戶端在關閉前連接的節點的IP地址，以便在重啟時方便重新連接。
---

Bitcoin Core 用戶端中使用的檔案，用來儲存用戶端關閉前所連線的出線節點的 IP 位址。因此，每次停止節點時都會建立 Anchors.dat，並在重新啟動時刪除。此檔案中包含 IP 位址的節點用來在節點重新啟動時幫助快速建立連線。