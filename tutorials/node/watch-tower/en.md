---
name: Lightning Watchtower
description: Understanding and using a Watchtower on your Lightning node
---
![cover](assets/cover.webp)


## How do Watchtowers work?


An essential part of the Lightning Network ecosystem, _Watchtowers_ provide an extra level of protection for users' Lightning channels. Their main role is to monitor channel status and intervene if one side of the channel tries to defraud the other.


How can a Watchtower determine whether a channel has been compromised? It receives from the customer (one of the parties to the channel) the information needed to correctly identify and deal with any breach. This information includes details of the most recent transaction, the current status of the channel, and the elements required to create penalty transactions. Before transmitting this data to Watchtower, the customer can encrypt it to preserve confidentiality. So, even if Watchtower receives the data, it will not be able to decrypt it until a breach has actually occurred. This encryption mechanism protects the customer's privacy and prevents Watchtower from gaining unauthorized access to sensitive information.


In this tutorial, we'll look at 3 ways of using a **Watchtower** :


- first, the classic raw method via LND,
- then another approach with Eye of Satoshi,
- and finally, the simplified configuration of a Watchtower on your Lightning node hosted with Umbrel.


## 1 - Configuring a Watchtower or a client via LND


*This tutorial is taken from [the official LND documentation](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Some changes may have been made to the original version


Since v0.7.0, `LND` supports the execution of a private altruistic Watchtower as a fully integrated subsystem of `LND`. Watchtowers provide a second line of defense against malicious or accidental breach scenarios when the customer node is offline or unable to respond at the time of breach, offering an increased degree of security for channel funds.


Unlike a _reward watchtower_, which demands a share of the channel's funds in return for its service, an _altruist watchtower_ returns all the victim's funds (minus On-Chain fees) without charging a commission. Reward watchtowers will be activated in a later version; they are still in the testing and improvement phase.


In addition, `LND` can now be configured to function as a _watchtower client_, saving encrypted breach remediation transactions (so-called "justice transactions") from other altruistic watchtowers. The Watchtower stores encrypted blobs of fixed size and can only decrypt and publish the justice transaction after the offending party has broadcast a revoked Commitment state. Customer ↔ Watchtower communications are encrypted and authenticated using ephemeral key pairs, which limits Watchtower's ability to track its customers via long-term credentials.


Note that we have chosen to deploy in this release a limited set of features already providing significant security for `LND` users. Many other watchtower-related features are either close to completion or well advanced; we will continue to deliver them as we test them, and as soon as they are deemed safe.


note: for the time being, watchtowers only save the `to_local` and `to_remote` output of revoked commitments; saving HTLC output will be deployed in a future version, as the protocol can be extended to include additional signature data in encrypted blobs._


### Configuring a Watchtower


To set up a Watchtower, command-line users need to compile the optional `watchtowerrpc` sub-server, which allows interaction with the Watchtower via gRPC or `lncli`. Published binaries include the `watchtowerrpc` sub-server by default.


The minimum configuration to activate Watchtower is `Watchtower.active=1`.


You can retrieve your Watchtower configuration information with `lncli tower info` :


```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```


The full set of Watchtower configuration options is available via `LND -h` :


```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```


#### Listening interfaces


By default, the Watchtower listens on `:9911`, which corresponds to port `9911` on all available interfaces. Users can define their own listening interfaces via the `--Watchtower.listen=` option. You can check your configuration in the `"listeners"` field of `lncli tower info`. If you have trouble connecting to your Watchtower, make sure that the `<port>` is open or that your proxy is correctly configured to an active Interface.


#### External IP addresses


Users can also specify the Watchtower's external IP address(es) with `Watchtower.externalip=`, which exposes the Watchtower's full URI (pubkey@host:port) via RPC or `lncli tower info` :


```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```


Watchtower URIs can be communicated to customers to connect and use with the following command:


```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```


If Watchtower customers need to access it remotely, make sure to :


- Open port 9911 (or a port defined via `Watchtower.listen`).
- Use a proxy to redirect traffic from an open port to the Watchtower's listening address.


#### Tor hidden services


Watchtowers support Tor hidden services and can automatically generate one at startup with the following options:


```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```


The .onion address then appears in the `"uris"` field during an `lncli tower info` query:


```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```


note: the Watchtower public key is distinct from the public key of the `LND` node. For the time being, it acts as a "soft whitelist", as customers need to know the Watchtower's public key to use it as a backup, pending more advanced whitelisting mechanisms. We recommend NOT disclosing this public key openly, unless you're prepared to expose your Watchtower to the entire Internet._


#### Watchtower database directory


The Watchtower database can be moved using the `Watchtower.towerdir=` option. Note that a `/Bitcoin/Mainnet/Watchtower.db` suffix will be added to the chosen path to isolate databases by string. Thus, setting `Watchtower.towerdir=/path/to/towerdir` will produce a database at `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.


Under Linux, for example, the Watchtower's default database is located at :

`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`


### Configuring a Watchtower client


To configure a Watchtower client, you need two items:



- Activate the Watchtower client with the `--wtclient.active` option.


```shell
$  lnd --wtclient.active
```



- The URI of an active Watchtower.


```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```


You can configure several watchtowers in this way.


#### Fee rates for legal transactions


Users can optionally set the fee rate for justice transactions via the `wtclient.sweep-fee-rate` option, which accepts values in sat/byte. The default value is 10 sat/byte, but it is possible to aim for higher rates to achieve higher priority during peak charges. Changing `sweep-fee-rate` applies to all new updates after daemon restart.


#### Supervision


With the `lncli wtclient` command, users can now interact directly with the Watchtower client to obtain or modify information on all registered watchtowers.


For example, with `lncli wtclient tower`, you can find out the number of sessions currently negotiated with the Watchtower added above and determine whether it is being used for backups thanks to the `active_session_candidate` field.


```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```


To obtain information on Watchtower sessions, use the `--include_sessions` option.


```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```


All Watchtower client configuration options are available via `lncli wtclient -h` :


```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```



## 2 - Installing your own Eye of Satoshi


*This tutorial is partly extracted from an article on the [Summer of Bitcoin Blog](https://blog.summerofbitcoin.org/). Modifications have been made to the original version*


The Eye of Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) is a non-depository Watchtower Lightning, conforming to [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). It consists of two main components:



- teos**: includes a command-line Interface (CLI) and the essential server features of Watchtower. Two binaries - **teosd** and **teos-CLI** - are produced when this _crate_ is compiled.



- teos-common**: includes shared server-side and client-side functionality (useful for creating a client).


To run Watchtower correctly, you need to run **bitcoind** before launching Watchtower with the **teosd** command. Before running these two commands, you need to configure your **Bitcoin.conf** file. Here's how to do it:



- Install Bitcoin core from source or download it. After downloading, place the **Bitcoin.conf** file in the Bitcoin core user directory. See this link for more information on where to place the file, as this depends on the operating system used.



- Once the location has been identified, add the following options:


```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```



- server**: for RPC requests



- rpcuser** and **rpcpassword**: authenticate RPC clients to the server



- regtest**: not required, but useful if you're planning development.


The values for **rpcuser** and **rpcpassword** are to be chosen by you. They must be written without quotation marks. For example:


```shell
rpcuser=aniketh
rpcpassword=strongpassword
```


Now, if you run **bitcoind**, the node should start.



- For the Watchtower part, you must first install **teos** from source. Follow the instructions given in this link.



- Once you've successfully installed **teos** on your system and run the tests, you can move on to the final step: setting up the **teos.toml** file in the teos user directory. The file should be placed in a folder named **.teos** (note the dot) under your home directory. For example, **/home//.teos** under Linux. Once the location has been found, create a **teos.toml** file and set these options in line with the changes made on **bitcoind** :


```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```


Note that here, the username and password must be written **within quotation marks**. Using the previous example :


```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```


Once this has been done, you should be ready to launch the Watchtower. Since we're running on **regtest**, it's likely that no blocks were mined on our Bitcoin test network when the Watchtower first connected (if they were, something's wrong). Watchtower builds an internal cache of the last 100 blocks of **bitcoind**; so, on first launch, you might get the following error:


```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```


Since we're using **regtest**, we can Miner blocks by issuing a RPC command, without having to wait for the median 10-minute delay seen on other networks (such as Mainnet or Testnet). See **bitcoin-cli** help for details of how to Miner blocks.


![Image](assets/fr/01.webp)


That's all: you've successfully run the Watchtower. Congratulations. 🎉



## 3 - Configuring a Watchtower on Umbrel


On Umbrel, connecting to a Watchtower to protect your Lightning node is extremely simple, as everything is done via the graphical Interface. After remotely connecting to your node, open the "**Lightning Node**" application.


![Image](assets/fr/02.webp)


Click on the three small dots at the top right of the Interface, then select "**Advanced Settings**".


![Image](assets/fr/03.webp)


In the "**Watchtower**" menu, two options are available:



- Watchtower Service**: this option lets you operate a Watchtower, i.e. a service that monitors the channels of other nodes to detect any attempted fraud. In the event of a breach, your Watchtower publishes a transaction on the Blockchain, enabling users to recover their locked funds. Once activated, your Watchtower's URI appears and can be communicated to other nodes so that they can add it to their Watchtower client;



- Watchtower Client**: this option lets you connect to external watchtowers to protect your own channels. Once activated, you can add Watchtower services to which your node will transmit the necessary information about its channels. These watchtowers will then monitor their status and intervene in the event of attempted fraud.


The priority for you is of course to activate the *Watchtower Client* to protect your node, but I also recommend that you activate the *Watchtower Service* to contribute to the security of other users in return.


![Image](assets/fr/04.webp)


Then click on the green "**Save and Restart Node**" button. Your LND will restart.


In the same menu, you'll also find the URI of your Watchtower service if you've activated it. You can also add the URI of an external Watchtower to protect your channels. Click on "**ADD**" to confirm.


![Image](assets/fr/05.webp)


There are several Watchtowers available online. For example, [LN+ and Voltage offer an altruistic Watchtower](https://lightningnetwork.plus/Watchtower) to which you can connect:


```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```


![Image](assets/fr/06.webp)


Another option is to exchange your Watchtower URI with your fellow bitcoiners, so that each protects the other's node.


I also recommend that you set up several Watchtowers to reduce the risks in the event of one of them becoming unavailable.


Finally, you can adjust the "**Watchtower Client Sweep Fee Rate**" parameter. This defines the maximum fee rate you are willing to pay for a Watchtower broadcast punishment transaction to be included in a block. Make sure you set a sufficiently high value, adapted to the amounts locked in your channels.