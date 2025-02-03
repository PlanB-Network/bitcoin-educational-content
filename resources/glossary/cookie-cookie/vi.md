---
term: COOKIE (.COOKIE)

---
File used for RPC (*Remote Procedure Call*) authentication in Bitcoin Core. When bitcoind starts, it generates a unique authentication cookie and stores it in this file. Clients or scripts wishing to interact with bitcoind via the RPC interface can use this cookie to authenticate securely. This mechanism allows for safe communication between bitcoind and external applications (such as wallet software, for example), without requiring manual management of usernames and passwords. The `.cookie` file is regenerated at each restart of bitcoind and deleted upon shutdown.