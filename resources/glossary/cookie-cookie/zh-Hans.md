---
term: cookie (.cookie)

---
Bitcoin Core 中用于 RPC（*远程过程调用*）身份验证的文件。当 bitcoind 启动时，它会生成一个唯一的身份验证 cookie 并存储在这个文件中。希望通过 RPC 接口与 bitcoind 进行交互的客户端或脚本可以使用这个 cookie 进行安全认证。这种机制允许 bitcoind 与外部应用程序（例如钱包软件）进行安全通信，而无需手动管理用户名和密码。每次重启 bitcoind 时，".cookie "文件都会重新生成，并在关闭时删除。