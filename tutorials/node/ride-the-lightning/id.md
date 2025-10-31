---
name: Ride The Lightning (RTL)
description: Use Ride The Lightning (RTL) to manage your Lightning node
---
![cover](assets/cover.webp)


## 1. Introduction



**Ride The Lightning (RTL)** is a complete Interface web application for managing a Lightning Network node. This self-hosted web application offers a Lightning **"cockpit"** accessible from your browser. RTL works with all major Lightning implementations (LND, Core Lightning/CLN and Eclair) and gives you total control over your node and channels. Open-source (MIT license) and free of charge, RTL is integrated by default in many turnkey node solutions (RaspiBlitz, MyNode, Umbrel, etc.).



**Without a graphical Interface, Lightning nodes can only be managed via user-friendly CLI commands. RTL simplifies these operations with an ergonomic Interface. Here are the main applications:**





- View your channels and node - The dashboard displays On-Chain balance, Lightning liquidity (local/remote), synchronization status, node alias and more. You can view your channel list, capacity, local/remote distribution and status. RTL offers context-sensitive dashboards to analyze activity from different angles.





- **Lightning channel management** - Open/close channels with a few clicks. RTL lets you connect to a peer and open a channel without a command. You can adjust routing fees, view the balance score, or initiate a circular rebalance to rebalance funds between channels.





- **Track and make payments** - RTL manages Lightning transactions: send payments via invoices, generate invoices to receive, track transactions (payments, routing) with detailed history. Interface also analyzes routing to see which payments are passing through your node.





- **Wallet On-Chain management and backup** - The On-Chain tab lets you generate addresses and send transactions. RTL makes it easy to save channels by exporting the SCB file for LND, with automatic update for each channel modification.



In short, RTL is a **powerful dashboard for the Lightning Network**, offering an educational Interface for piloting your node on a daily basis. This tutorial will guide you through its installation and use to manage your channels and payments.



## 2. Technical operation of RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Before getting down to the nitty-gritty, it's useful to briefly understand **how RTL interacts with your Lightning node** on a technical level.



**General architecture:** RTL is a web application built with Node.js (backend) and Angular (frontend). In concrete terms, RTL runs as a small local web server (on port 3000 by default) that dialogs with your Lightning implementation via its APIs. Depending on the type of :





- With **LND**, RTL uses LND's REST API (port 8080) to execute Lightning commands. The connection is secured by TLS and requires LND's **admin macaroon** file for authentication.





- With **Core Lightning (CLN)**, RTL uses either the REST API provided by *c-lightning-REST*, or an **access rune** via the `commando` plugin. Solutions such as Umbrel automatically configure these Elements.





- With **Eclair**, RTL connects to the Eclair REST API using the configured authentication password.



**Configuration and security:** RTL is configured via a JSON file (`RTL-Config.json`) where you define the web port, access password, and connection information to your node. The Interface web is protected by a login/password (default `password` to be changed) and supports 2FA. By default, RTL runs as local HTTP (`http://localhost:3000`), but for remote access, always use a secure connection (HTTPS via reverse-proxy, Tor, or VPN).



In short, RTL is an additional component that connects to your node via secure APIs, requires appropriate access tokens, and offers its own security Layer. This modular architecture even allows you to manage **several Lightning nodes with a single RTL instance**.



## 3. RTL installation



As RTL is distributed as open-source software, there are several ways to install it on your system. In this section, we'll cover two main approaches: manual installation and installation via Umbrel.



### Manual method



Manual installation is suitable if you like to keep fine-grained control, or if you're integrating RTL into a custom configuration. The steps below are for a LND node running Linux (e.g. Raspberry Pi or VPS running Ubuntu/Debian), but are similar for CLN/Eclair.



**Prerequisite:** make sure you have a **synchronized** Bitcoin node and a working Lightning node (LND, CLN or Eclair) on the machine. RTL does not contain a Lightning node per se, it connects to an existing node. You also need **Node.js** installed (version 14+ recommended). You can check with `node -v` or install Node from the official site (https://nodejs.org/en/download/) or your package manager.



The main installation stages are :



**Download RTL code**: Clone the official RTL GitHub repository in the directory of your choice. For example:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Install dependencies**: RTL is a Node.js application, so you need to install its required modules. In the RTL folder, run :



```bash
npm install --omit=dev --legacy-peer-deps
```



This command installs the necessary NPM packages (ignoring development dependencies). The `--legacy-peer-deps` option is recommended to avoid possible Node dependency conflicts.



**RTL-Config**: Once the dependencies are in place, prepare the configuration file. Copy/rename the `Sample-RTL-Config.json` file in the project root to `RTL-Config.json`. Open it in your :





- **UI password**: choose a secure password and enter it in `multiPass` (instead of the default `"password"`).
- **Port**: default `3000`. You can change it if this port is already taken on your machine.
- **Node**: in the `nodes[0]` section, adjust the parameters for your node:
     - `lnNode`: a descriptive name for your node (e.g. `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (or `"CLN"`/`"ECL"` as appropriate).
     - Under `authentication`:
       - macaroonPath`: specify the full path to the folder containing LND's macaroon admin.
       - `configPath`: path to the node's config file (`LND.conf` for LND).
     - Under `settings`:
       - `fiatConversion`: set to `true` if you want fiat currency conversion.
       - `unannouncedChannels`: set to `true` to see unannounced channels.
       - themeColor` and `themeMode`: Interface customization.
       - channelBackupPath`: path for LND channel backups.
       - `lnServerUrl`: URL of your Lightning node (e.g. `https://127.0.0.1:8080`).



**Start the RTL server**: In the RTL folder, run :



```bash
node rtl
```



The application starts up and can be accessed at `http://localhost:3000`.



**(Optional) Run RTL as a service**: For automatic startup, create a systemd :



To do this:




- Open a terminal on your machine.
- Create a new service file with the following command (replace `nano` with your favorite editor):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Copy and paste the content below into this file:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Replace `/path/to/RTL/rtl` with the actual path to the `rtl` file on your machine, and `<your_user>` with your Linux username.
- Save and close the file.
- Reload the systemd configuration:


```bash
sudo systemctl daemon-reload
```




- Activate and start the RTL service:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL will now start automatically each time the machine is rebooted. You can check its status with :


```bash
sudo systemctl status RTL
```



### Installation via Umbrel



If you use [Umbrel](https://getumbrel.com), RTL installation is much simpler:





- Access Interface Umbrel (usually via `http://umbrel.local`)
- Go to the **App Store**
- Search for "Ride The Lightning"



**Important note: there are two separate RTL applications in the Umbrel App Store:**




- **Ride The Lightning** (for LND): for use with Umbrel's default Lightning node (LND).
- **Ride The Lightning (Core Lightning)**: use only if you have installed the *Core Lightning* application on Umbrel and wish to manage this node with RTL.



*Each RTL version is preconfigured to dialogue with the corresponding implementation (LND or Core Lightning). If you haven't changed your Lightning node, simply choose the classic LND version*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Click on **Install**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Important:** After installation, RTL displays a screen with the default password. **Copy and save this password** - you'll need it to log on to Interface RTL. This password will be displayed each time RTL starts up until you check the "Don't show it again" option.



Umbrel automatically takes care of :




- Download and configure RTL
- Configuring access to the Lightning node
- Manage updates
- Securing access to Interface



Once installed, the application appears in your *Apps* menu on Umbrel. Click on **Ride The Lightning** to launch it.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



On the login screen, enter the password you copied earlier. Once logged in, the Interface web RTL will be accessible directly from the Umbrel dashboard, with no additional configuration required!



## 4. Introduction and use of Interface RTL



Now that RTL is up and running, let's explore its Interface web and its key features. We'll go through the different sections of the application to give you a complete overview.



### The main control panel



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



As soon as you log in, you access the **main dashboard**, which gives you an overview of your Lightning node. This page centralizes essential information:




- Your total Lightning balance
- On-Chain balance available
- The breakdown of your liquidity (incoming/outgoing)
- Quick access to send and receive Satss via your Lightning node



### Fund management On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



The **On-Chain** tab lets you manage your bitcoins directly on the main chain:




- Balance display in different units (Sats, BTC, USD)
- Complete list of transactions
- Address generation Taproot (P2TR), P2SH (NP2WKH) or Bech32 (P2WKH)
- UTXO management, receiving and sending bitcoins



### Lightning: detailed presentation of submenus



Interface RTL features a side menu dedicated to Lightning Network, bringing together all the essential functions for managing your node. Here are the details of each sub-menu, in the order of the screenshot:



#### 1. Peers/Channels



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



This sub-menu allows you to :




- View the list of your connected peers and Lightning channels open or waiting.
- Add a new peer (connect to another Lightning node).
- Open, close or manage existing channels.
- View details of each channel: capacity, local/remote balances, status, trading history, balance score, etc.



#### 2. Transactions



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



In this submenu, you can :




- Send Lightning payments (via Invoice).
- generate and manage invoices to receive payments.
- View the complete history of payments sent and received, with details (amount, date, status, charges, number of skips, etc.).



#### 3. Routing



This submenu displays :




- Payments routed by your node for other Lightning Network users.
- Routing statistics: number of transactions relayed, fees earned, errors encountered.
- Exportable history for advanced analysis.



#### 4. Deferrals



This sub-menu offers :




- Detailed reports on the activity of your Lightning node.
- Charts and tables on channels, payments, fees, capacity, etc.
- Tools to better understand your node's performance.



#### 5. Graph Lookup



This sub-menu allows you to :




- Explore the topology of the Lightning Network.
- Search for specific nodes or channels.
- Obtain information on connectivity and overall network capacity.



#### 6. Sign/Verify



This submenu offers :




- The ability to sign a message with your node's key (proof of Ownership).
- Signature verification to authenticate messages from other nodes.



#### 7. Backup



This sub-menu is dedicated to backup:




- Export channel backup file (SCB for LND).
- Restore configuration or channels if necessary.
- Tips for securing your backups.



#### 8. Node/Network



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



In this submenu you will find :




- A complete summary of your Lightning node's status: alias, version, color, synchronization status.
- Statistics on channels (active, waiting, closed), total capacity, connectivity.
- Information about the global Lightning Network and your node's position in it.



### Services: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz is a privacy-friendly, non-custodial Exchange service that converts bitcoins between the Lightning Network and Blockchain Bitcoin (On-Chain). It offers two types of operation: Reverse Submarine Swap (**Swap Out**) and Submarine Swap (**Swap In**).



#### Swap Out (Reverse Submarine Swap)



Swap Out converts Satss available on the Lightning Network into On-Chain bitcoins. This mechanism is useful when a node runs out of incoming capacity, or when you want to recover funds from a On-Chain Address. The process works as follows:




- The user selects an amount to be exchanged
- The node sends a Lightning payment to Boltz
- In Exchange, Boltz blocks an equivalent amount in On-Chain bitcoins
- Once the transaction has been confirmed, the user can claim the funds by revealing a secret used in the swap



This process is non-custodial, with Boltz never holding the user's funds.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Submarine Swap)



Swap In, on the other hand, allows On-Chain funds to be reinjected into the Lightning Network. This is particularly useful for restoring output capacity on your channels. The procedure is as follows:




- The user sends bitcoins to a specific Address generated by Boltz
- These funds can only be released by Boltz if he pays a Lightning Invoice generated by the user's node
- Once the Invoice has been paid, the funds are available on the Lightning channel, increasing the node's output capacity



![Configuration d'un swap-in](assets/fr/12.webp)



These two mechanisms enable Lightning channel liquidity to be managed efficiently, while maintaining the user's sovereignty over his funds.



### Configuration and customization



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



The **Node Config** tab lets you customize your experience:




- Activation of unannounced channels
- Customize sale display
- Block explorer configuration
- Adjusting the Interface



### Documentation and help



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Finally, the **Help** section offers comprehensive documentation on :




- Initial configuration
- Peer and channel management
- Payments and transactions
- Backups and restores
- Reports and statistics
- Signatures and verifications
- Node and application parameters



This comprehensive Interface lets you manage your Lightning node efficiently, from basic operations to advanced features, all in an intuitive, well-organized Interface.



## 5. Advanced use cases & security



In this section, here's what you need to know to go further with RTL and secure your Lightning node:



### Monitoring and troubleshooting



To monitor your node, you can export RTL data (logs, CSV) and view them in tools such as Grafana. In the event of a problem (blocked payment, inactive channel), consult the LND/CLN logs and use the diagnostic commands (`lncli listchannels`, `lncli pendingchannels`, etc.). RTL also offers Interface logs for monitoring routing events.



### Secure remote access



Never expose RTL directly on the Internet. Give preference to :




- **VPN** (e.g. Tailscale) for private, encrypted access
- **Tor** for secure, anonymous access
- Reverse proxy **HTTPS** (Nginx/Caddy) only if you know how to configure it



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Good safety practices





- **Protect your access**: never share admin.macaroon or your RTL password. Limit permissions on sensitive files.
- **Regular backups**: export the channel backup file (SCB) after each modification and store it outside the node.
- **Updates**: keep RTL, your node and Umbrel up to date with the latest security fixes.
- **Confidentiality**: anonymize logs and screenshots before sharing them. Never share your balances or peer lists publicly.
- **Single access**: RTL is not multi-user. Do not share admin access. For read-only access, use a dedicated macaroon if necessary.



By applying these principles, you greatly limit the risks and retain control over your Lightning node.



## 7. Conclusion



**Ride The Lightning** is an essential tool for effectively managing a Bitcoin/Lightning node, whether you're a beginner or an advanced user. It provides a clear Interface for controlling your channels, payments and node health, while deepening your understanding of Lightning Network.



RTL stands out for its multi-implementation compatibility, its advanced functions (rebalancing, swaps, reports) and its pedagogical approach. For simple needs, the Interface Umbrel or a Wallet mobile will suffice, but RTL makes perfect sense for active, optimized node management.



To find out more :




- Official RTL website: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Technical discussions, project announcements, feedback and educational resources
- **Umbrel Community Forum**: [community.getumbrel.com](https://community.getumbrel.com) - Official forum with dedicated Bitcoin/Lightning section, guides and solutions to common problems
- **Lightning Network Developers**: [github.com/lightning](https://github.com/lightning) - Official GitHub repository for following development and contributing source code
- **Stack Exchange Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Technical Q&A with developers and advanced users



In short, RTL gives you total control over your Lightning node, in a modern, full-featured Interface.



**Sources :** RTL official website; RTL GitHub; Umbrel App Store; Umbrel Community; Plan ₿ Academy resources.



To deepen your understanding of how the Lightning Network works, I also recommend you take this free course:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb