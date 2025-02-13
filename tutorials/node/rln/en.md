---
name: RGB Lightning Node
description: How do I launch an RGB-compatible Lightning node with RLN?
---
![cover](assets/cover.webp)

In this step-by-step tutorial, you'll learn how to set up a Lightning RGB node on a Regtest environment. We'll see how to create RGB tokens and circulate them in channels.

## The RLN project

Bitfinex's RGB team has been working since 2022 to enrich the RGB ecosystem by developing a complete technology stack. Rather than aiming for a single commercial product, its efforts are focused on making open-source software bricks available, contributing to RGB protocol specifications and creating implementation references.

Among Bitfinex's notable contributions to the RGB ecosystem is [the *RGBlib* library](https://github.com/RGB-Tools/rgb-lib), written in Rust and accessible via bindings in Kotlin and Python, which greatly simplifies the development of RGB applications by encapsulating complex validation and engagement mechanisms.

The Bitfinex team has also designed an RGB mobile wallet, called "[*Iris Wallet*](https://iriswallet.com/)", available on Android. This wallet integrates the use of an RGB proxy server to easily manage off-chain data exchanges (*consignments*) for *Client-side Validation* on RGB.

Bitfinex has also developed the `rgb-lightning-node` (RLN) project. This is a Rust daemon based on a fork of `rust-lightning` (LDK), modified to take into account the existence of RGB assets in a channel. When a channel is opened, the presence of RGB tokens can be specified, and each time the channel state is updated, a state transition is created that reflects the distribution of tokens in Lightning outputs. This enables :


- Open Lightning channels in USDT, for example;
- Route these tokens through the network, provided the routing paths have sufficient liquidity;
- Exploit Lightning's punishment and timelock logic without modification: simply anchor the RGB transition in an additional output of the commitment transaction.

The RLN code is still in its alpha stage: we recommend using it in **regtest** or on the **testnet** only.

## RGB protocol reminder

RGB is a protocol that runs on top of Bitcoin and emulates smart contract functionality and digital asset management, without overloading the blockchain on which it is based. Unlike conventional on-chain smart contracts (as on Ethereum, for example), RGB relies on a "*Client-side validation*" system: the majority of data and status histories are exchanged and stored exclusively by the participants involved, whereas the Bitcoin blockchain only hosts small cryptographic commitments (via mechanisms such as *Tapret* or *Opret*). In the RGB protocol, the Bitcoin blockchain therefore only serves as a time-stamping server and double-spending protection system.

An RGB contract is structured like an evolutionary state machine. It starts with a Genesis that defines the initial state (describing, for example, the supply, ticker or other metadata) according to a strictly typed and compiled Schema. State Transitions and, if necessary, State Extensions are then applied to modify or extend this state. Each operation, whether transferring fungible assets (RGB20) or creating unique assets (RGB21), involves *Single-use Seals*. These link Bitcoin UTXOs to off-chain states and prevent double spending, while ensuring confidentiality and scalability.

To learn more about how the RGB protocol works, I recommend you take this comprehensive training course:

https://planb.network/courses/csv402
## RGB-compatible Lightning node installation

To compile and install the `rgb-lightning-node` binary, we start by cloning the repository and its sub-modules, then we run the :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- The `--recurse-submodules` option also clones the necessary sub-devices (including the modified version of `rust-lightning`);
- The `--shallow-submodules` option restricts the depth of the clone to speed up downloading, while still providing access to essential commits.

From the project root, run the following command to compile and install the binary :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` ensures that the version of dependencies is respected;
- `--debug` is not compulsory, but can help you focus (you can use `--release` if you prefer) ;
- `--path .` tells `cargo install` to install from the current directory.

At the end of this command, an `rgb-lightning-node` executable will be available in your `$CARGO_HOME/bin/`. Make sure this path is in your `$PATH` so you can invoke the command from any directory.

## Prerequisites

To function, the `rgb-lightning-node` daemon needs the presence and configuration of :


- A `bitcoind`** node

Each RLN instance will need to communicate with `bitcoind` to broadcast and monitor its on-chain transactions. Authentication (login/password) and URL (host/port) will need to be provided to the daemon.


- An indexer** (Electrum or Esplora)

The daemon must be able to list and explore on-chain transactions, in particular to find the UTXO on which an asset has been anchored. You'll need to specify the URL of your Electrum server or Esplora.


- An RGB** proxy

The proxy server is a component (optional, but highly recommended) to simplify the exchange of RGB *consignments* between Lightning peers. Once again, a URL must be specified.

IDs and URLs are entered when the daemon is *unlocked* via the API.

## Regtest launch

For simple use, there's a `regtest.sh` script that automatically starts, via Docker, a set of services: `bitcoind`, `electrs` (indexer), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

This allows you to launch a local, isolated, pre-configured environment. It creates and destroys containers and data directories on each reboot. We'll begin by starting the :

```bash
./regtest.sh start
```

This script will :


- Create a `docker/` directory to store ;
- Run `bitcoind` in regtest, as well as the indexer `electrs` and the `rgb-proxy-server` ;
- Wait until everything is ready to use.

![RLN](assets/fr/04.webp)

Next, we'll launch several RLN nodes. In separate shells, run, for example (to launch 3 RLN nodes) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RLN](assets/fr/05.webp)


- The `--network regtest` parameter indicates the use of the regtest configuration;
- `--daemon-listening-port` indicates on which REST port the Lightning node will listen for API calls (JSON);
- `--ldk-peer-listening-port` specifies which Lightning p2p port to listen on;
- `dataldk0/`, `dataldk1/` are the paths to the storage directories (each node stores its info separately).

You can now execute commands on your RLN nodes from your browser, thanks to the API. In particular, this is where you can *unlock* daemons. Simply open a browser on the same computer as your nodes, and enter the URL :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

For a node to open a channel, it must first have bitcoins on an address generated with the following command (for node n°1, for example):

```bash
curl -X POST http://localhost:3001/address
```

The answer will provide you with an address.

![RLN](assets/fr/06.webp)

On the `bitcoind` Regtest, we're going to mine a few bitcoins. Run :

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Send funds to the node address generated above:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Then mine a block to confirm the transaction:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Testnet launch (without Docker)

If you want to test a more realistic scenario, you can launch RLN nodes on the Testnet rather than in Regtest, pointing to public services, or services you control:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

By default, if no configuration is found, the daemon will try to use the :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

With login :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

You can also customize these elements via the `init`/`unlock` API.

## Issuing an RGB token

To issue a token, we'll start by creating "colorable" UTXOs:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RLN](assets/fr/10.webp)

You can, of course, adapt the order. To confirm the transaction, we mine a :

```bash
./regtest.sh mine 1
```

We can now create an RGB asset. The command will depend on the type of asset you wish to create and its parameters. Here I'm creating a NIA (*Non Inflatable Asset*) token named "PBN" with a supply of 1000 units. The `precision` allows you to define the divisibility of the units.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

The response includes the ID of the newly created asset. Remember to note this identifier. In my case, it's :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

You can then transfer it on-chain, or allocate it in a Lightning channel. That's exactly what we're going to do in the next section.

## Opening a channel and transferring an RGB asset

You must first connect your node to a peer on the Lightning network using the `/connectpeer` command. In my example, I control both nodes. So I'll retrieve the public key of my second Lightning node with this command:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

The command returns the public key of my node n°2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Next, we'll open the channel by specifying the relevant asset (`PBN`). The `/openchannel` command lets you define the size of the channel in satoshis and opt to include the RGB asset. It depends on what you want to create, but in my case, the command is :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Find out more here:


- `peer_pubkey_and_opt_addr`: Identifier of the peer we wish to connect to (the public key we found earlier);
- `capacity_sat`: Total channel capacity in satoshis ;
- `push_msat`: Amount in millisatoshis initially transferred to the peer when the channel is opened (here I immediately transfer 10,000 sats so that he can make an RGB transfer later) ;
- `asset_amount`: Amount of RGB assets to be committed to the channel ;
- `asset_id` : Unique identifier of the RGB asset engaged in the channel;
- `public`: Indicates whether the channel should be made public for routing on the network.

![RLN](assets/fr/14.webp)

To confirm the transaction, 6 blocks are mined:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

The Lightning channel is now open and also contains 500 `PBN` tokens on node n°1's side. If node n°2 wishes to receive `PBN` tokens, it must generate an invoice. Here's how to do it:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

With :


- `amt_msat`: Invoice amount in millisatoshis (minimum 3000 sats) ;
- `expiry_sec` : Invoice expiry time in seconds ;
- `asset_id` : Identifier of the RGB asset associated with the invoice ;
- `asset_amount`: Amount of RGB asset to be transferred with this invoice.

In response, you will get an RGB invoice:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

We will now pay this invoice from the first node, which holds the necessary cash with the `PBN` token:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

Payment has been made. This can be verified by executing the command :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

Here's how to deploy a Lightning node modified to carry RGB assets. This demonstration is based on :


- A regtest environment (via `./regtest.sh`) or testnet ;
- A Lightning node (`rgb-lightning-node`) based on a `bitcoind`, an indexer and an `rgb-proxy-server` ;
- A series of JSON REST APIs for opening/closing channels, issuing tokens, transferring assets via Lightning, etc.

Thanks to this process :


- Lightning engagement transactions include an additional output (OP_RETURN or Taproot) with the anchoring of an RGB transition;
- Transfers are made in exactly the same way as traditional Lightning payments, but with the addition of an RGB token;
- Multiple RLN nodes can be linked to route and experiment with payments across multiple nodes, provided there is sufficient liquidity in both bitcoins and asset RGB on the path.

If you found this tutorial useful, I'd be very grateful if you put a green thumb below. Please feel free to share this article on your social networks. Thank you very much!

I also recommend this other tutorial in which I explain how to use the RGB CLI tool developed by the LNP/BP association to create an RGB contract:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4