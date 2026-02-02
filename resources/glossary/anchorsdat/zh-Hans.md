---
term: Anchors.dat

definition: 一个Bitcoin Core文件，存储客户端在关闭前连接的节点的IP地址，以便在重启时方便重新连接。
---
在 Bitcoin Core 客户端中使用的文件，用于保存客户端关闭前连接的外发节点的 IP 地址。因此，每次节点停止时都会创建 Anchors.dat 文件，并在重启时删除它。该文件中包含 IP 地址的节点，用于帮助节点重启时快速建立连接。
