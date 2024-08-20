---
term: COOKIE (.COOKIE)
---

用于比特币核心中RPC（*远程过程调用*）认证的文件。当bitcoind启动时，它会生成一个唯一的认证cookie并将其存储在此文件中。希望通过RPC接口与bitcoind进行交互的客户端或脚本可以使用这个cookie来安全认证。这种机制允许bitcoind与外部应用程序（例如，钱包软件）之间安全通信，无需手动管理用户名和密码。`.cookie`文件在每次重启bitcoind时重新生成，并在关闭时删除。