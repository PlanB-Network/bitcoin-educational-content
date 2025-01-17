---
name: Watch Tower
description: Understanding and using a watch tower
---

## How do watchtowers work?

An essential part of the Lightning Network ecosystem, watchtowers give an extra degree of protection to users' lightning channels. Its main responsibility is to keep an eye on the channels' health and intervene if one channel party tries to defraud the other.

So how can a watchtower determine if a channel has been compromised? The watchtower receives the information it needs from the client, one of the channel parties, in order to properly identify and respond to any breaches. The most recent transaction details, the current channel condition, and the information required to create penalty transactions are frequently included in this information. Before transmitting the data to the watchtower, the client might encrypt it to protect privacy and secrecy. This prevents the watchtower from decrypting the encrypted data unless a breach has really taken place, even if it gets the data. The client's privacy is protected by this encryption system, which also stops the watchtower from accessing private data without authorization.

## How to set up your own Eye of Satoshi and start contributing

The Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) is a non-custodial Lightning watchtower compliant with [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). It has two main components:

1. teos: including a CLI and the server-side core functionality of the tower. Two binaries—teosd and teos-cli—will be produced when this crate is built.
2. teos-common: Including shared server-side and client-side functionality (helpful for creating a client).

To run the tower successfully, you will need bitcoind running before running the tower with the teosd command. Before running both of these commands you need to set up your bitcoin.conf file. Here are the steps on how to do this:-

1. Install bitcoin core from the source or download it. After downloading, place bitcoin.conf file in the Bitcoin core user directory. Check this link for more information regarding where to place the file as it depends on the operating system you are using.
2. After Identifying the place where the file needs to be created, add these options:-

```
#RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

#chain
regtest=1```

- server: For RPC requests
- rpcuser and rpcpassword: RPC clients can authenticate with the server
- regtest: Not required but useful if you're planning for development.

rpcuser and rpcpassword need to be picked by you. They must be written without quotes. Eg:-

```
rpcuser=aniketh
rpcpassword=strongpassword```

Now, if you run bitcoind it should start running the node.

1. For the tower part, first, you have to install teos from source. Follow the instructions given in this link.
2. After successfully installing teos in your system and running the tests, you can proceed with the last step which is to set up the teos.toml file in the teos user directory. The file needs to be placed in a folder called .teos (mind the dot) under your home folder. That is, for instance, /home/<your-username>/.teos for Linux. Once you've find the place, create a teos.toml file and set these options corresponding to the things we've changed on bitcoind.

```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>```

Notice that here the username and password need to be written quoted, that is, for the same example as before:

```
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"```

Once you've done that, you should be good to go to run the tower. Given we are running on regtest, chances are there won't be any blocks mined in out bitcoin test network the first time the tower connects to it (it there are, something is certainly off). The tower builds an internal cache of the latest 100 blocks from bitcoind, so on running for the first time we may get the following error:

_ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more_

Given we are running on regtest we can mine block by issuing an RPC command, without the need of waiting for the 10-minute median time that we usually see in other networks (like mainnet or testnet). Check bitcoin-cli help and look for how to mine blocks. If you need some help, you can go through this article.

![image](assets/2.webp)

That's it, you've successfully run the tower. Congratulations. 🎉
