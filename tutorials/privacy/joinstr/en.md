---
name: Joinstr
description: Decentralized CoinJoins via the Nostr network for sovereign Bitcoin confidentiality
---

![cover](assets/cover.webp)


The transparency of the Bitcoin blockchain makes it possible to trace transaction history. CoinJoins break these links by mixing multiple simultaneous transactions, restoring a level of confidentiality comparable to cash.


However, traditional solutions rely on a central coordinator as a single point of failure. Wasabi and Samourai ceased operations in 2024 under regulatory pressure.


**Joinstr** eliminates this weakness by using the decentralized Nostr network for coordination. This open source application enables truly sovereign CoinJoins, where no central authority can censor, monitor or interrupt the service.


## What is Joinstr?


Joinstr is an open source tool that revolutionizes the CoinJoins approach by leveraging the Nostr protocol as a coordination infrastructure. Unlike centralized solutions requiring a dedicated server, Joinstr relies on a distributed network of Nostr relays to enable participants to coordinate directly between peers.


**Decentralized architecture** : The Nostr network replaces the central coordinator. Participants create or join "pools" by posting encrypted announcements via the Nostr relays. This information (amounts, participants, addresses) remains unintelligible to the relays, ensuring that no central entity can monitor, censor or filter CoinJoins.


**SIGHASH_ALL|ANYONECANPAY mechanism**: Joinstr exploits this Bitcoin signature flag, allowing each participant to sign only his or her input while validating all outputs. Each user generates his or her PSBT locally, then distributes it via Nostr. Each user generates his PSBT locally, signs it, then distributes it via Nostr. Your bitcoins remain under your exclusive control until the final signature.


**Philosophy**: Joinstr follows the Bitcoin cypherpunk ethos, aiming for three goals: **resistance to censorship** (no authority can stop the service), **total non-custodiality** (you keep your private keys), and **equal treatment** (no UTXO can be discriminated against).


### Main features


**Flexible pools**: Unlike fixed denominations, any user can create a pool with the exact amount desired and the target number of participants, optimizing the use of UTXO without artificial splitting.


**Transparent fees**: No coordination fees. Only Bitcoin transaction fees are shared equally between participants (a few thousand satoshis per person).


**Ephemerality**: No user data retained. Information transits via encrypted ephemeral Nostr messages, immediately forgotten after the transaction.


### Available platforms


This tutorial focuses on the **Android application**, the only currently stable and recommended solution. A Electrum plugin exists but has compatibility problems that make it unstable. A web interface is under development.


## Bitcoin Core configuration


Joinstr Android requires a connection to a Bitcoin node via RPC. You must first configure Bitcoin Core on your computer to accept connections from your phone.


**Note**: For more details on the complete configuration of Bitcoin Core, see our dedicated tutorials :


https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Network requirements


#### Locate your local IP address


Your Android phone must be able to reach your Bitcoin node on the local network. Find the IP address of your computer:


**On macOS** :


```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```


Simple alternative:


```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```


**On Linux** :


```bash
hostname -I | awk '{print $1}'
```


**On Windows** :


```cmd
ipconfig
```


Find the IPv4 address (format `192.168.x.x` or `10.0.x.x`)


### RPC configuration


#### Edit bitcoin.conf


![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)


Locate your `bitcoin.conf` file:


- **Linux**: ~/.bitcoin/bitcoin.conf
- **macOS**: ~/Library/Application Support/Bitcoin/bitcoin.conf
- **Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`


![CONTENU BITCOIN.CONF](assets/fr/02.webp)


Open the file with your favorite text editor and add this configuration to activate the RPC server.


**Recommended configuration for getting started (bookmark)** :


```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```


**mainnet** configuration (for production use) :


```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```


**Important** :


- Signet is highly recommended for your first tests: the application is still in development (beta), and bugs may still exist. Signet lets you test free of charge, without risking real funds
- Replace `192.168.1.0/24` with your network subnet (e.g. if your IP is `192.168.68.57`, use `192.168.68.0/24`)


**Security**: Generate a strong password :


```bash
openssl rand -base64 32
```


### Initialization


#### Restart and check


1. Shut down Bitcoin Core completely

2. Restart it to apply the configuration



![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)


When Bitcoin Core starts up for the first time, it will download and synchronize the bookmark blockchain. This operation is much faster than on mainnet (only a few minutes). Please wait until synchronization is complete before proceeding.


![CRÉATION DE WALLET](assets/fr/04.webp)


Once synchronized, create a new portfolio by clicking on "Create a new wallet". Give it an explicit name like `tuto_joinstr_signet`.


![WALLET CRÉÉ](assets/fr/05.webp)


Your wallet is now created and ready to receive bookmarked bitcoins for testing.


#### Get bookmarked bitcoins (test)


To test Joinstr on bookmark, you need free test bitcoins :


![SIGNET FAUCET](assets/fr/06.webp)


Use a public bookmark like :


- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)


In Bitcoin Core, generate a new receive address ("Receive" tab), copy it and paste it into the faucet form. Solve the captcha if necessary. You'll receive free bookmarked bitcoins within seconds.


## Android application


### Installation


![APPLICATION ANDROID](assets/fr/07.webp)


Go to [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) to download the latest APK version. On your Android browser, download the file, then open it to launch the installation. You'll need to allow installation from unknown sources in your phone's security settings if necessary.


### Application configuration


![PERMISSIONS VPN](assets/fr/08.webp)


On first launch, the Joinstr application will ask for permissions to control the built-in VPN. Accept both permission requests: OpenVPN control and VPN connection. These permissions are required for VPN integration, which protects your network privacy.


![INTERFACE APPLICATION](assets/fr/09.webp)


The Joinstr application is organized into three main tabs:


- Home: Home screen
- Pools: Creating and managing CoinJoin pools
- Settings: Application configuration


![CONFIGURATION SETTINGS](assets/fr/13.webp)


Configure settings in the "Settings" tab:


**1. Nostr Relay**: Nostr relay address for pool coordination


- Example: `wss://relay.damus.io`
- Other recommended relays: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Important**: All participants must use the **same Nostr relay** to see and join the same pools. If you use a different relay, you will not see pools created on other relays


**2. Node URL**: IP address of your Bitcoin node (without port)


- Format: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`


**3. RPC Username** : The user name configured in `rpcuser=` on your bitcoin.conf


- Example: satoshi


**4. RPC Password** : The password set in `rpcpassword=` on your bitcoin.conf


**5. RPC Port** : RPC port depending on network


- **Mainnet** : `8332`
- **Bookmark**: `38332`


**6. Wallet**: Select the Bitcoin Core portfolio containing the UTXOs to be mixed


- Example: `tuto_joinstr_signet`


**7. VPN Gateway**: Select a Riseup VPN server


- Example: `(Paris) vpn07-par.riseup.net`
- Others available: Amsterdam, Seattle, etc.
- ⚠️ **Important**: All participants in the same pool must use the **same VPN Gateway** to participate in CoinJoin. During the mixing round, all participants must appear with the same exit IP address to prevent network analysis from correlating participants


The Joinstr application **integrates natively** the Riseup VPN, simplifying coordination between participants.


**Important** :


- Make sure your phone and computer are on the same local WiFi network
- The VPN connection will be activated automatically when participating in a pool
- Click on **"Save "** once you have set all the parameters


## Practical use


### Create or join a pool


![CRÉATION POOL ANDROID](assets/fr/10.webp)


You have two options for participating in a CoinJoin:


**Option 1: Create a new pool**


Click on "Create New Pool" in the "Pools" tab. Specify the denomination in BTC (e.g. 0.002 BTC) and the desired number of participants (minimum 2, recommended 3-5 for greater anonymity). The application then waits for other users to join your pool. Once the required number has been reached, the output registration process begins automatically, and you'll need to select your UTXO to mix and click on "Register".


**⏱️ Important**: Pools expire after **10 minutes** of inactivity. If the required number of participants is not reached, the pool will be automatically closed.


**Option 2: Join an existing pool**


In the "View Other Pools" tab, browse the available pools created by other users. Select a pool corresponding to your amount and join it. Make sure you have configured the same Nostr relay and VPN Gateway as the other participants (see Configuration section).


**UTXO selection rule**: Your UTXO must be slightly higher than the pool denomination (between +500 and +5000 sats surplus).


**Example**: For a pool of 0.002 BTC (200,000 sats), use a UTXO between 200,500 and 205,000 sats.


![PROCESSUS COINJOIN](assets/fr/11.webp)


The process is then **fully automatic**: once your input has been registered, the application waits for all participants to register their inputs. Once all inputs have been registered, the PSBT is created, automatically signed with your keys, then combined with the signatures of the other participants. Finally, the complete transaction is broadcast on the Bitcoin network. You receive the TXID (transaction identifier) once the broadcast is complete. No manual manipulation of PSBT is required on Android.


### on-chain verification


![TRANSACTION MEMPOOL](assets/fr/12.webp)


Once the transaction has been broadcast, you will receive the TXID (transaction identifier). View it on [mempool.space](https://mempool.space) or your favorite browser. To test on a bookmark, use [mempool.space/signet](https://mempool.space/signet).


You can observe :



- **N entries**: One per participant (in our example, 2 entries)
- **N identical outputs**: exact amount of the denomination (here, 2 outputs of 0.00199800 BTC each)
- **Flow chart**: mempool.space visually displays the mix of inputs and outputs
- **Features** : The transaction can be identified as SegWit, Taproot, RBF, etc.


As all main outputs have the same amount, it's **impossible to determine which belongs to whom**. This is the fundamental principle of CoinJoin: the indistinguishability of outputs.


**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)


**Please note**: If your UTXOs were larger than the pool denomination, you will have foreign exchange outputs (surpluses). These exchange UTXOs remain traceable and must be managed separately from your anonymized outputs. Never combine them with your mixed outputs.


## CoinJoin quality and anonymity packages


The efficiency of a CoinJoin is measured by its **anonset**: the number of outputs of identical value produced by the transaction. The higher this number, the more difficult it is to determine which input corresponds to which output.


Joinstr currently generates pools of **2 to 5 participants** on average. These figures are lower than traditional centralized coordinators like Wasabi (50-100 participants) or Whirlpool (5-10 participants), but that's the price of decentralization.


💡 **To understand anonymity sets and their calculation in detail**, see our full course: [Anonymity sets](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).


### Joinstr vs. other CoinJoins


| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinator** | Centralized (up to 2024) | Centralized (active) | P2P maker/taker | **None (Nostr)** |
| **Resistance to censorship** | Low | Medium | Very high | **Very high** |
| **Coordination fees** | Percentage | Entrance fee | Paid by makers | **None** |
| **UTXO Discrimination** | Yes (blacklists) | No | No | **No** |

💡 **Other active CoinJoin solutions** :


- **Ashigaru**: Open-source implementation of the Whirlpool protocol with centralized coordinator but deployable in a decentralized way. Continues to operate after the seizure of Samourai Wallet in 2024.
- **JoinMarket**: Decentralized P2P solution with no central coordinator, based on a maker/taker business model where "makers" provide liquidity and are remunerated by "takers".


https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**The fundamental trade-off**: Joinstr and JoinMarket are the only two solutions without a central coordinator. JoinMarket uses a P2P business model with financial incentives, while Joinstr uses Nostr for cost-free coordination. Joinstr sacrifices immediate large-scale anonymity in favor of simplicity (no maker/taker management) and the total absence of coordination fees.


**Practical recommendation**: To compensate for smaller pools, run several successive rounds of CoinJoin with different participants. Space out your rounds and change Nostr relays between each round to maximize your confidentiality.


Feel free to consult our complete course on bitcoin privacy for more information on this topic:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Advantages and limitations


### Highlights


**Enhanced privacy**: The combination of Nostr communications encryption, shared VPN between participants, and the recommended use of Tor creates multi-layered protection that's hard to bypass.


**Transparent, minimal costs**: No coordination costs, only mining costs are shared equitably between participants. No percentage levied by any operator.


### Constraints to consider



- Variable liquidity: Smaller pools, can wait for participants to come together
- Project in progress: Application in beta, bugs possible. Test first with small amounts on bookmark
- Sybil attacks: Possibility of one opponent controlling several pool participants


## Best practices


**UTXO isolation**: Never combine a mixed UTXO with an unmixed one. Use a separate portfolio for your anonymized outputs.


**Multiple rounds essential**: Perform a minimum of 3 successive rounds with different participants. Vary amounts and timings to avoid patterns. Space rounds several hours apart.


**Network protection**: Systematically use Tor in addition to the built-in VPN. Generate ephemeral Nostr keys for each important session.


**Cautious progress**: Start bookmarking with small amounts.


## Conclusion


Joinstr represents a truly decentralized Bitcoin privacy solution. By using Nostr for coordination, it eliminates dependence on central coordinators while preserving user sovereignty.


For users who value resistance to censorship and are prepared to perform several rounds of CoinJoin to compensate for smaller pools.


Against a backdrop of increasing financial scrutiny, decentralized tools to protect privacy are becoming essential.


## Resources


### Official documentation


- [Joinstr official website](https://joinstr.xyz)
- [User documentation](https://docs.joinstr.xyz/users/using-joinstr)
- [Technical documentation](https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLab source code](https://gitlab.com/invincible-privacy/joinstr)
- [Android application](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)


### Tutorials


- [Electrum plugin tutorial](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Complete guide by Uncensored Tech


### Community and support


- [Telegram Joinstr Group](https://t.me/joinstr) - Community support and bookmark corners
- [Technical discussion on DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)


### Additional tools


- [Bookmark Faucet](https://signetfaucet.com) - Free test Bitcoins
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet alternative
- [Mempool.space](https://mempool.space) - Block explorer with privacy analysis
