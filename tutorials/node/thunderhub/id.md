---
name: ThunderHub
description: Interface Lightning node management web LND
---
![cover](assets/cover.webp)



## Introduction



ThunderHub is an **open-source manager for Lightning nodes (LND)**, offering an intuitive Interface accessible from any device or browser.



**Main features:**




- **Monitoring**: Global view of balances, channels, transactions, routing statistics
- **Management**: Open/close channels, incoming/outgoing payments, channel balancing
- **Integrations**: LNURL support, swaps via Boltz, Amboss backup
- **Interface responsive**: Compatible with mobile, tablet and desktop devices with dark/light themes



ThunderHub integrates easily with **Umbrel**, **Voltage**, **RaspiBlitz** and **MyNode**, simplifying the day-to-day management of your node.



**ThunderHub is particularly suited to operators looking for an ergonomic Interface to manage their channels, control liquidity (rebalancing), monitor transactions and integrate third-party services such as Amboss. Security is assured via a local or Tor connection.**



If you don't yet have a Lightning node, we recommend you follow our LND Umbrel tutorial:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installation



ThunderHub can be installed in a number of different ways, depending on your Lightning node hosting environment. Whether you use a turnkey solution (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, etc.) or a manual installation, ThunderHub is often available without major effort. Below, we describe two common approaches: via the Umbrel App Store, and via manual installation (applicable to a server or self-hosted distribution).



### Installation via Umbrel



Umbrel integrates ThunderHub into its **App Store**, making installation extremely simple. No need for a command line or manual configuration: everything is done via Interface Umbrel. Just follow these steps:





- **Open the Umbrel dashboard**: Connect to the Interface web of your Umbrel node (e.g. `http://umbrel.local` on your local network, or via its `.onion` Address if you're using Tor).
- **Access the App Store**: In Umbrel's main menu, click on "App Store" (or "App"). Search for **ThunderHub** in the list of available applications.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Install ThunderHub**: Click on the ThunderHub application, then on the install button. Confirm if necessary. Umbrel will automatically download and deploy ThunderHub on your node.





- **Launch the application**: Once installation is complete (a few tens of seconds), ThunderHub appears on your home page. Click on the icon to open it. ThunderHub launches in your browser.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Important:** When ThunderHub is first opened, it automatically displays the **default password** required to log in. A "Don't show this again" option lets you hide this display for future connections. **We strongly advise you to:**




- **Save this password immediately** in your password manager
- Copy it **for use in the next step**
- Check "Don't show this again" once the password has been saved



![Page de connexion de ThunderHub](assets/fr/03.webp)



You will then be taken to the login page, where you must enter the password you copied in the previous step to unlock the Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel takes care of providing ThunderHub with LND connection information (TLS certificate, administration macaroon, etc.) in the background, so you don't need to do any additional configuration. In just a few clicks, you'll have ThunderHub up and running on your Umbrel node.



### Manual installation (self-hosted, excluding Umbrel)



For users outside Umbrel (e.g. on a personal server, a Raspberry Pi with RaspiBlitz or a *stand-alone* installation), ThunderHub installation requires a few extra steps. Below we describe the installation from source and the configuration, according to the [official ThunderHub documentation](https://docs.thunderhub.io).



#### Installation



**Prerequisites:** Make sure that your system meets the minimum requirements according to [documentation setup](https://docs.thunderhub.io/setup):




- **Node.js** version 18 or higher
- **npm** installed
- Access to LND authentication files :
  - LND TLS certificate (`tls.cert`)
  - LND administration macaroon (`admin.macaroon`)
  - LND gRPC service Address (hostname:port) (default `127.0.0.1:10009` locally)



**1. Retrieve ThunderHub code:** Clone the project's GitHub repository as described in the [installation documentation](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. install dependencies and build the application:**



```bash
npm install
npm run build
```



These commands install all the required modules and then compile the application (ThunderHub is written in TypeScript/React).



**3. Update later:** ThunderHub offers several methods for future updates:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Configuration (Setup)



**1. Main configuration file:** Create a `.env.local` file at the root of the ThunderHub folder to customize the configuration (this will prevent your settings from being overwritten during updates). Main variables as per [setup documentation](https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Server Accounts configuration:** Create the YAML file specified in `ACCOUNT_CONFIG_PATH` :



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Remote Access:** To connect to a remote LND node, add to `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Security:** On first startup, ThunderHub **automatically** hides the `masterPassword` and all account passwords in the YAML file, to avoid having passwords in clear text on the server.



**5. Start ThunderHub:**



```bash
npm start
```



By default, the server listens on port 3000. Access `http://localhost:3000` (or `http://ip-serveur:3000` from the local network).



**6. Docker alternative:** ThunderHub provides official Docker images:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



The ThunderHub login page appears. Select the configured account and enter the password to access the dashboard.



**Installation on other distributions:** Pre-packaged node distributions (RaspiBlitz, MyNode, Start9, etc.) generally offer native ThunderHub support via their respective administration interfaces.



**For more information:** Consult the complete official documentation :




- **Installation:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Configuration:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



These resources detail advanced options such as SSO accounts, encrypted macaroons, TOR configuration and much more.



Once ThunderHub is installed and accessible, you're ready to exploit all its features. In the following section, we'll take a look at the Interface ThunderHub and its various tabs, to guide you through its use.



## Interface presentation



Interface ThunderHub is structured around a main menu (usually displayed in the left-hand side column) comprising several key sections. Each corresponds to an aspect of managing your Lightning node. Let's go through them one by one:





- **Home** - Home tab with general dashboard (overview of your node and quick actions).
- **Dashboard** - Customizable dashboard with widgets and advanced metrics.
- **Peers** - Lightning peer management (connections to other nodes).
- **Channels** - Detailed management of Lightning channels.
- **Rebalance** - Channel balancing tool (circular payments).
- **Transactions** - Lightning payment history (LN transactions).
- **Forwards** - Routing statistics (payments relayed by your node).
- **Chain** - Node's On-Chain portfolio (On-Chain BTC: UTXOs, transactions).
- **Amboss** - Integration with Amboss (node monitoring, backups, etc.).
- **Tools** - Miscellaneous tools (backups, signed messages, macaroons, reports, etc.).
- **Swap** - On-Chain/Lightning swap functions via Boltz.
- **Stats** - Advanced statistics and node performance metrics.



*(Note: Depending on the ThunderHub version, some sections may have slightly different headings or additional features, but the general principles remain the same)*



### Home (General control panel)



ThunderHub's **Home** tab is the home page that appears after you log in. It contains the **General Dashboard**, which offers a **global overview** of the status of your Lightning node and suggests **quick actions** for routine operations. Here's what you'll typically find:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Balances and capacities:** At the top of the page, ThunderHub displays your available balances. Here you'll typically see the On-Chain balance (Bitcoin On-Chain in the node's Wallet, symbolized by an Anchor ⚓) and the Lightning balance (your channels' capacities, symbolized by a lightning Bolt ⚡). This gives you an immediate idea of the funds you have in On-Chain and Lightning. If you have several accounts or channels, make sure you're on the right one (e.g. Mainnet vs Testnet).





- **Key statistics:** The dashboard can show some global metrics for your node - for example, number of open channels, number of connected peers, routing fees earned (if applicable), etc. It's a summary of the node's recent activity and health.





- **Quick Actions:** The dashboard features buttons for quickly executing the most common tasks, without having to navigate through menus. These quick actions include:





- **Ghost**: Set up a custom Lightning Address via Amboss.
- **Donate**: Make a donation via Lightning.
- **Login/Go To**: Connect to your Amboss account (Quick Connect) and go directly to Amboss.space to view your node's information.
- **Address**: Enter a Lightning Address to make a payment.
- **Open**: Open a new Lightning channel. Clicking opens a form for entering the URI of the remote node to which to open the channel, the amount and, if applicable, the maximum On-Chain fee to be used.
- **Decode**: Decode a Lightning Invoice or LNURL to view details before payment.
- **LNURL**: Process LNURLs for Lightning payments or withdrawals.
- **LnMarkets Login**: Login to LnMarkets for trading.



These quick actions allow you to perform the most frequent operations directly from the home page, without having to navigate through the Interface's various tabs.



In short, the ThunderHub dashboard gives you a **quick look** at your node and lets you perform the most frequent operations (send/receive, open a channel) with a single click. It's the ideal starting point for day-to-day administration.



### Dashboard



The **Dashboard** section is separate from the Home tab and offers a more advanced, customizable dashboard. This section allows you to create a customized view with specific widgets according to your needs as a node operator.





- **Customizable widgets:** Unlike the Home page, which has a fixed layout, the Dashboard lets you choose exactly which Elements to display and how to organize them.



![Dashboard sans widgets activés](assets/fr/06.webp)



If no widgets are enabled, you'll see a "No Widgets Enabled!" message with a "Settings" button to access the customization parameters.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



In the settings, you can choose from a wide range of widgets organized into categories: "Lightning - Info", "Lightning - Table", "Lightning - Graph", and so on. Each widget can be individually activated or deactivated with the "Show/Hide" buttons.



![Bas de la page des paramètres](assets/fr/08.webp)



At the bottom of the settings, you'll find the "To Dashboard" button to return to the dashboard and the "Reset Widgets" button to reset the default display.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Once configured, your dashboard can display various graphs and metrics: Lightning payment graphs, number of invoices issued, forwards statistics, detailed balances, etc.





- **Advanced metrics:** Access more detailed statistics on your node's performance, with graphs and real-time data.





- **Configurable overview:** Tailor the display to suit whether you're a casual user or a professional operator managing multiple routing channels.





- **Modular Interface:** Add or remove widgets as required: forwards charts, liquidity metrics, node health alerts, etc.



This section is particularly useful for advanced users who wish to monitor specific metrics or get a more technical overview of their Lightning node. It complements the Home section by offering greater flexibility and control over how information is displayed.



### Peers



The **Peers** section lists all Lightning nodes currently connected to yours as peers. A **peer** is a direct node-to-node connection on the Lightning Network. Your node can be connected to peers even without an open channel (e.g., just to Exchange gossip information on the network), or of course every open channel automatically implies a connected peer.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



In the Peers tab, you'll see :





- **Information columns:** The Interface displays useful details such as synchronization status, connection type (clearnet or Tor), ping, satoshis received/sent and volume of data exchanged.
- Add a peer: ThunderHub lets you manually connect to a new peer via the **"Add"** button in the top right-hand corner. You'll need to enter the node's URI (format `<public_key>@<socket>`). Once validated, ThunderHub sends the corresponding `lncli connect` command. If the node is online and accessible, it will be added to your list of peers.



### Channels



The **Channels** tab is the heart of Lightning channel management. It's probably the section you'll consult most frequently. It presents **all your Lightning channels** with their details, and allows you to perform management actions on these channels.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Here's what you'll find on the Channels page:





- **Channel list view:** Each open (or opening/closing) channel is listed, usually with the alias of the remote node, the total channel capacity, and a colored bar illustrating the distribution of local vs. remote liquidity. ThunderHub uses a color code (often blue/Green) or percentage to indicate channel balance: for example, blue for your local share, Green for the remote share. If a channel is perfectly balanced (50/50), the bar will be half of each color. This allows you to identify at a glance which channels are unbalanced (all blue = almost all local, all Green = almost all remote).





- **Information columns:** The Interface displays detailed columns including Status, Available Actions, Peer Info, Channel ID, Capacity, Activity, Fees and Balance with graphical liquidity display.





- **Display configuration:** A cogwheel in the top right-hand corner lets you customize the channel display to suit your preferences.





- **Status:** You'll also see status indicators - e.g. `Active` (the channel is open and operational), `Offline` (the peer is disconnected, so the channel is momentarily unusable), `Pending` (for openings or closings awaiting On-Chain confirmation).





- **Actions on a channel:** For each channel, ThunderHub provides action buttons (often in the form of icons):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- **Edit fees:** The Interface "Update Channel Policy" lets you adjust all channel parameters: Base Fee, Fee Rate (in ppm), CLTV Delta, Max HTLC and Min HTLC. This allows you to adjust your fee policies individually per channel, with the aim of attracting (or discouraging) routing traffic. *(Note: ThunderHub is not a substitute for an automatic fee management tool, but for manual adjustment it's very effective)*
- Close Channel (**Close**): The Interface "Close Channel" gives you the choice between a **cooperative close** (default) or a **forced close** (**Force Close**) by defining the charges (in Sats/vByte). **Important:** always prefer cooperative close when possible, to avoid On-Chain settlement delays and higher fees. ThunderHub will tell you whether the peer is online (cooperative possible) or not. In the event of force close, be sure to confirm as this is irreversible and will trigger a sweeping transaction with a timelock (generally 144 blocks or ~1 day on Bitcoin Mainnet).
- **Open a new channel:** To open a new channel, click on the cogwheel at the top right of the Channels page, then select "Open". You can then initiate a channel to a new or existing peer. The advantage of using this page is that you have a list of your existing channels in front of you, which can help you decide where to open a new channel.



In short, the Channels section gives you **fine control over each channel**. This is where you drive liquidity allocation, decide which channels to keep or close, and set your per-channel routing parameters. ThunderHub offers a clear Interface for these crucial node management operations.



### Rebalance



The **Rebalance** tab is dedicated to **channel balancing**. Balancing (or *rebalancing*) involves readjusting the distribution of funds between your outgoing and incoming channels, by making a **circular payment** from one of your channels to another of your channels, via the Lightning Network. This allows you, without bringing in new funds, to shift liquidity from a channel that's too full to one that's too empty, making your channels more useful (a balanced channel can both send and receive payments).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub greatly facilitates this operation, which would otherwise be tedious on the command line. Here's how to use the Rebalance section:





- **Initial channel view:** On entering Rebalance, ThunderHub displays a list of your channels, with a balance indicator for each (similar to the one on the Channels page). You can see right away which channels are out of balance. ThunderHub can sort channels in order of increasing balance, so that the most unbalanced channels stand out at the top of the list (0.0 meaning entirely local or remote).





- **Peer selection:** The Interface makes it easy to select outgoing and incoming peers for rebalancing.





- **Parameter settings:** You can set :
  - The **maximum fee** (in Sats and ppm) you're willing to pay
  - The **amount to rebalance** with "Fixed" or "Target" option
- **Nodes to avoid** when routing
- **Maximum trial time** for route finding





- Select **source** channel: First select the **outgoing (source)** channel, i.e. the channel from which you have too much local liquidity to move. In practice, this is a channel where your local share is high (> 50%). Let's imagine an A channel with 1,000,000 Satss, 900,000 of which are local - a good candidate for sending Satss elsewhere. By clicking on this A channel as "outgoing", ThunderHub marks it as a source.





- Choose **target channel**: Next, choose the **incoming (target)** channel that needs to receive liquidity. Typically, this will be a channel where it's the other way around - most funds are on the far side (e.g. only 100,000 local Satss out of 1,000,000). ThunderHub, once the source channel has been selected, will sort the other channels in reverse order (decreasing balance) to help identify the most complementary channels. Select a B channel that has room on the local side. ThunderHub will then clearly display which two channels have been selected (source A and target B).





- **Set fee amount and tolerance:** A form allows you to enter :





  - The **amount** to be rebalanced (in Sats). Often, we choose an amount equal to what would balance both channels at \~50/50. ThunderHub can pre-fill half the excess capacity of the source channel, for example.
  - The **maximum fee** you are willing to pay for this operation (optional). This fee is expressed in Sats (total cost of circular routing). If you leave it blank, ThunderHub will search for a path regardless of cost, which is generally not advisable (it's better to set a limit, e.g. 10 Sats for a small rebalance, or a maximum ppm).





- **Find Route:** Click on the button to find a route. ThunderHub queries LND to calculate a route from your source channel through the network to your own target channel. If it finds a possible route that meets your fee criteria, it displays it with details of the hops and the fee cost. For example, it might indicate that it has found a 3-hop path with a total of 2 Sats in charges.





- **Start rebalance:** If you are happy with the proposed route, click on **Balance Channel**. ThunderHub will then initiate circular payment via LND. If the payment is successful, you'll see a notification of success, and channels A and B will have their balances modified in real time. ThunderHub will update the balance indicator for these channels (ideally they will be greener than before, indicating better balance).





- **Adjustments and iterations:** If no route is found on the first try (or if it's too expensive), you can adjust the parameters:





  - Try a smaller amount (sometimes a partial rebalance goes through while a large amount fails).
  - Increase the maximum fee gradually, but be careful not to pay more in fees than it's worth.
  - Use the **Get Another Route** button, if available, to try an alternative.
  - Try another pair of channels if things really get sticky.



ThunderHub makes the process very **intuitive and visual**. In just 4 steps (select outgoing channel, select incoming channel, amount, validate), you can do what used to require complex manual commands. The tool is invaluable for maintaining a well-balanced node, improving your routing performance and experience (easier to send and receive payments across all your channels).



Finally, note that a rebalance consumes routing costs (paid to intermediate nodes), so it's an **investment** to make your node more fluid. Use it wisely, for example to support a channel to a service you use often (inbound liquidity) or to balance a large routing channel. ThunderHub lets you do this **simply and efficiently**.



### Transactions



The **Transactions** section in ThunderHub corresponds to your node's **Lightning** transaction history, i.e. payments and invoices paid or received via the channels. It's a kind of statement of account for your LN operations.



![Historique des transactions Lightning](assets/fr/14.webp)



In this tab you will find :





- **Invoice graph:** In the top right-hand corner, a graph shows the evolution of invoices received over time, allowing you to visualize your node's activity.





- A chronological list of all Lightning transactions made *from* or *to* your node. Each entry can show :





  - Type of operation: **sent payment** (outgoing payment) or **received payment** (inbound, via a paid Invoice).
  - The amount in Sats.
  - Date/time.
  - Payment ID (Hash or RHash pre-image) or comment (if you added a memo to Invoice).
  - Status: **completed**, or possibly **in progress**/*failed* (e.g. a payment awaiting resolution, but generally LND processes this quickly, so there's little "pending" here compared to On-Chain transactions).



In short, the Transactions section serves as your **LN activity log**. It's very useful for checking that a payment has gone through, how many fees it cost, or tracing the history of your Lightning exchanges. In conjunction with the Forwards section (described next), you'll have a complete view of the money that has passed through your node.



### Forwards



The **Forwards** tab is dedicated to your node's **routing** activity, i.e. payments that **transit** through your channels (when you act as an intermediary node on the Lightning Network). If you operate your node as a routing node, this is an important section for tracking your performance.



![Statistiques de routage Lightning](assets/fr/15.webp)



In Forwards, ThunderHub presents :





- **Filters and display options:** At top right, filters let you sort data by day/week/month/year, and choose between graphical or tabular display.





- **Activity message:** If no routing has been performed during the selected period, the Interface displays "No forwards for this period", as shown in this example.





- A **table of recent forwards**: each entry corresponds to a payment that has been **forwarded** through your node. For each forward, we generally see :





  - Timestamp,
  - the amount routed (in Sats),
  - the **fee earned** on this forward (in Sats, this is the difference between what you received on the incoming channel and sent on the outgoing one),
  - the incoming and outgoing channels used (often identified by the peer alias or channel ID).
  - status (normally *completed*, or failure if a forward failed en route).





- **Aggregated statistics**: ThunderHub calculates and displays at the top of the page totals and statistics over a given period (e.g. last 24 hours, or 7 days, etc., sometimes configurable).



In short, the Forwards section offers a **real-time overview of your Lightning node's routing activity**. Coupled with the Channels and Rebalance sections, this forms a complete package for optimizing your node: Channels/Rebalance for liquidity, Forwards for observing results (flows and profits).



### Chain



The **Chain** section corresponds to the Bitcoin On-Chain portfolio management of your LND node. This Interface allows you to view and manage Bitcoin funds, which are used to open channels or receive funds from closed channels.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



In Chain, you will find :





- **Balance On-Chain:** Displays the total BTC balance available in Wallet LND.





- **List of UTXOs:** View all unspent outputs (UTXO) with amount, confirmations, Address and format for each output.





- **Transaction history:** Detailed table of all Bitcoin transactions with type (in/out), date, amount, charges, confirmations, inclusion block, addresses and txid.



### Amboss



ThunderHub integrates with the **Amboss** platform (amboss.space), which offers detailed information on Lightning nodes, a liquidity marketplace, and useful features such as encrypted channel backup and availability monitoring.



![Intégration Amboss avec ses options](assets/fr/17.webp)



In ThunderHub, the Amboss section allows you to **link** your node to your Amboss account:





- **Ghost Address:** Set up a **personalized Lightning Address** for your node, facilitating incoming payments.





- Automatic channel backups:** Flagship feature for encrypted channel backups** (SCB files) on Amboss. Activate **Amboss Auto Backup = Yes** in the settings to automatically send encrypted backup updates each time you change channels. In the event of a failure, you'll be able to recover your funds thanks to this external backup.





- **Health Checks:** Activate **Amboss Healthcheck = Yes** to have your node send regular pings to Amboss. You'll receive alerts if your node appears to be offline.





- **Other features:** Automatic balance push, **Magma/Hydro** integration (liquidity marketplace), and access to detailed performance statistics.



Amboss integration adds an essential **security Layer** with automatic external backup and availability monitoring, accessible directly from ThunderHub.



### Tools



The **Tools** section groups together various advanced tools for managing your node. Here are the main Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Backups:** Manually manage your channel backups (SCB). ThunderHub lets you **download the complete backup file** of your channels (option "Backup all channels -> Download"). Keep this `channel-all.bak` file in a safe place - it's essential for recovering your funds in the event of a crash. You can also **import** a backup file when redeploying a node.





- **Accounting:** Export tool for financial reports including fees earned/paid and volumes routed over a given period.
- **Signed messages:** Sign or verify messages with your node to prove ownership of your Lightning node via cryptographic signature.
- Macaroons (Bakery section):** Manage LND** macaroons to create customized access. The Interface "Bakery" allows you to precisely select each permission: "Add or remove Peers", "Create Chain Addresses", "Create Invoices", "Create Macaroons", "Derive Keys", "Get Access Keys", "Get Chain Transactions", "Get Invoices", "Get Wallet Info", "Get Payments", "Get Peers", "Pay Invoices", "Revoke Access Ids", "Send to Chain Addresses", "Sign bytes", "Sign Messages", "Stop daemon", "Verify bytes signature", "Verify messages", and so on. Each permission can be activated individually with the "Yes/No" buttons to create a tailor-made macaroon.
- **System information:** Display of Wallet version and activated RPCs.



In short, the Tools section brings together advanced administration functions - backups, accounting, security and access management - in a unified Interface.



### Swap



ThunderHub's **Swap** tab lets you swap Lightning satoshis to Bitcoin On-Chain via the Boltz service. This feature is useful for "dumping" excess Lightning liquidity to the channel without closing a channel.



![Interface de swap via Boltz](assets/fr/19.webp)



The process is simple:





- **Amount**: Define the amount to be exchanged
- **Address**: Enter Bitcoin reception Address
- **Execution**: ThunderHub communicates with Boltz to automatically process the Exchange



**Benefits:**




- Non-custodial service (no cash custody)
- Preserve your existing channels
- Easy-to-use integrated Interface



Boltz charges a small commission and you pay the standard Bitcoin transaction fee. ThunderHub displays all costs before confirmation.



### Stats



ThunderHub's **Stats** section offers **advanced statistics** on your Lightning node to analyze performance and optimize routing.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



This section is essential for optimizing your costs, identifying successful channels and planning the expansion of your node.



## Conclusion



**ThunderHub** has established itself as the essential tool for easy administration of a Lightning **LND** node. This modern Interface offers all the essential functions: channel management, payments, monitoring, with advanced features such as automated rebalancing and Amboss integration.



**Key benefits:**




- Interface sleek and intuitive
- Powerful tools (rebalance, Boltz swaps, automatic backups)
- Compatible with Umbrel, Voltage, RaspiBlitz and other distributions



ThunderHub democratizes advanced Lightning node management, making accessible what previously required complex technical commands. Whether you're a beginner or an experienced operator, ThunderHub lets you efficiently manage your Lightning node via a modern, comprehensive Interface.



## Resources



**Official links:**




- **Official website:** [thunderhub.io](https://thunderhub.io)
- **Documentation:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **GitHub source code:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)