---
name: LNbits Server
description: Installation and configuration of a self-hosted LNbits server on Ubuntu VPS with PHOENIXD or on Umbrel
---

![cover](assets/cover.webp)


LNbits is an open source Interface web application that transforms any Lightning backend (LND, Core Lightning, PHOENIXD) into a complete service platform. This self-hosted solution enables you to manage multiple Lightning portfolios in isolation, deploy points of sale, create donation systems or billing services, while retaining total control over your funds.


This tutorial covers two installation approaches: **VPS Ubuntu with PHOENIXD** (lightweight solution without a full Bitcoin node) and **Umbrel** (integration with your existing LND node). Unlike Plan B Network's general LNbits tutorial, which covers concepts and extensions, this guide focuses on step-by-step technical installation procedures.


## What is LNbits?


LNbits is a Lightning accounting system developed in Python (FastAPI) that connects to an existing backend (LND, Core Lightning, PHOENIXD). Unlike traditional Lightning nodes, LNbits offers an accessible Interface, enabling you to manage several isolated portfolios with their own API keys. You can create sub-accounts for your family, employees or projects, without giving them access to all your funds.


The decoupled architecture stores information in SQLite (default) or PostgreSQL (production), while funds remain managed by your Lightning backend. This separation guarantees portability: you can migrate from PHOENIXD to LND without losing your user data.


## Key features


LNbits offers a versatile **extension system**: TPoS (point of sale), Paywall (content monetization), Events (ticketing), LndHub (server for BlueWallet), Bolt Cards (NFC payments), Split Payments (automatic distribution), and User Manager (user management with authentication).


The **dashboard** displays real-time balances, transaction history and billing tools. Each Wallet has a unique URL containing its API keys, allowing access without a traditional login. The three-level API key system** (admin, Invoice, read-only) offers granular control of permissions for secure integrations.


LNbits natively implements **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) and supports **Lightning Address**, guaranteeing compatibility with modern Lightning wallets and facilitating the deployment of professional services.


## Supported platforms


**Ubuntu VPS**: Lightweight solution without full Bitcoin node. Prerequisites: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + domain name required for public exposure (LNURL services).


**Umbrel**: Easy installation from the App Store. Prerequisite: functional Umbrel node with synchronized LND and open channels. Automatic configuration.


Below are links to our Umbrel and Umbrel LND tutorials:


https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installing on Ubuntu VPS with PHOENIXD


### Step 1: Securing the VPS server


**Before any installation**, you need to secure your Ubuntu VPS server according to the rules of the art. This step is **critical** to protect your infrastructure and your Lightning funds.


Here's a detailed guide to help you get started: **[Initial Ubuntu server configuration - Step-by-step guide](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** by Daniel P. Costas.


This guide covers user configuration, secure SSH, firewall (UFW), fail2ban, automatic updates, and good system security practices.


### Step 2: Installing PHOENIXD


Once your server is secure, you need to install and configure PHOENIXD. Plan B Network offers a complete dedicated tutorial covering installation, seed generation and systemd service configuration:


https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Once PHOENIXD is up and running (check with `./Phoenix-CLI getinfo`), note the **HTTP password** in `~/.Phoenix/Phoenix.conf` - you'll need it to connect LNbits to PHOENIXD.


### LNbits deployment


Install UV and clone LNbits :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```


Configure the PHOENIXD backend:

```bash
cp .env.example .env && nano .env
```


Add to `.env` :

```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```


Test with `uv run lnbits --host 0.0.0.0 --port 5000` then create a systemd service with `Wants=PHOENIXD.service`.


## Initial setup and first use


### SuperUser activation


Activate the Interface administrator in `.env` :

```
LNBITS_ADMIN_UI=true
```


Restart LNbits (`sudo systemctl restart lnbits`) and retrieve the SuperUser ID:

```bash
cat ~/lnbits/data/.super_user
```


Go to `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` for the administration panel. The "Server" menu lets you configure funding sources, extensions and user accounts.


### Secure account creation


**Important for public exposure**: If you're exposing your LNbits instance on a public domain name accessible from the Internet, it's **critical** to disable the free creation of user accounts.


From the SuperUser administration Interface, go to "Settings" and then to the "User Management" section. You'll find the "Allow creation of new users" option.


![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)


**For a public exhibition with domain name** :


- You must disable** the "Allow creation of new users" option
- Without this protection, anyone on the Internet can create an account on your instance
- An attacker could create accounts and use the liquidity of your Lightning node without your knowledge
- You'll need to create user accounts manually from the Interface SuperUser


**For local use only** :


- This option is less critical if your instance is only accessible locally (http://localhost:5000)
- However, disabling this option is a good general safety practice


Once configured, only the SuperUser administrator can create new user accounts via the Interface "Users". This approach guarantees total control over who can access your Lightning infrastructure and use your funds.


### Opening the first channel


PHOENIXD automatically manages channels via auto-liquidity. Generate a Lightning invoice of ~30,000 Sats from LNbits and pay it from another wallet. PHOENIXD automatically opens a channel to ACINQ. The opening fee (~20-23k Sats) is deducted, the remaining balance (~7-10k Sats) appears after On-Chain confirmation.


Check status with `./Phoenix-CLI getinfo`. Then consider disabling auto-liquidity (`auto-liquidity=off` in `Phoenix.conf`) to control channel openings.


### Public display and HTTPS


**Important**: HTTPS mandatory for public display (API key security + LNURL compatibility). Skip this step for local use only.


**Caddy (recommended)**: automatic SSL. `sudo apt install -y caddy`, edit `/etc/caddy/Caddyfile` :

```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```

Restart: `sudo systemctl restart caddy`.


**Nginx** : More control. Install `nginx certbot python3-certbot-nginx`, create `/etc/nginx/sites-available/lnbits` :

```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```

Activate: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`


Add to `.env`: `FORWARDED_ALLOW_IPS=*`


## Umbrel installation


### Deployment from the App Store


Go to the Umbrel App Store, search for "LNbits", and click on "Install".


![Installation LNbits Umbrel](assets/fr/01.webp)


Umbrel automatically checks for required dependencies. LNbits requires LIGHTNING NODE (LND) to run. If your Lightning node is already operational, click on "Install LNbits" to confirm.


![Dépendances LNbits](assets/fr/02.webp)


Umbrel downloads the Docker image, automatically configures connections with LND, and starts the container (2-5 minutes). Installation takes place entirely in the background.


### Initial SuperUser configuration


On first launch, LNbits prompts you to create the SuperUser administrator account. Enter a user name and set a secure password to protect access to the Interface administration system.


![Configuration SuperUser](assets/fr/03.webp)


**Important**: This SuperUser account has full privileges on your LNbits instance. Choose a strong password and keep it safe.


Once you've created an account, you're automatically taken to the Interface main administration area. Umbrel has already set up LND as your funding source - all Lightning payments will go through your existing channels.


### Access to Interface administrator


In the left-hand side menu, click on "Settings" to access the full administration panel.


![Interface Settings](assets/fr/04.webp)


The "Wallets Management" section displays key information about your configuration:


- Funding Source** : LndBtcRestWallet (direct connection to your LND Umbrel node)
- Node Balance** : Total liquidity available in your Lightning channels
- LNbits Balance**: Funds allocated to the LNbits system (initially 0 Sats)


You can now directly exploit the liquidity of your Umbrel node for all the LNbits wallets you create. No additional configuration is required - LNbits is up and running.


### User management


One of LNbits' most powerful features is its ability to create multiple independent users, each with password authentication and isolated wallets. This architecture makes it possible to take advantage of the liquidity of your Umbrel node while offering totally isolated sub-accounts for different uses: business, family, employees, projects, etc.


In the side menu, click on "Users" to access user management. Click on "CREATE ACCOUNT" to add a new user.


![Gestion des utilisateurs](assets/fr/05.webp)


Fill in the user creation form:


- Username**: Login username (example: "Satoshi")
- Set Password**: Activate this option to set an authentication password
- Password** and **Password repeat**: Set the password for this user


![Création utilisateur satoshi](assets/fr/06.webp)


Optional fields (Nostr Public Key, Email, First Name, Last Name) can be left blank for minimal configuration. Click on "CREATE ACCOUNT" to confirm.


![Confirmation utilisateur créé](assets/fr/07.webp)


Your new user now appears in the list of users with his or her unique identifier and user name.


![Liste des utilisateurs](assets/fr/08.webp)


**Important point**: Each user can log on completely independently with his or her own password. The SuperUser administrator retains full control via the Interface administration tool.


### User wallet management


Now that the "Satoshi" user has been created, you need to assign him a Wallet Lightning. Click on the wallet icon (second icon) for the user concerned, then on "CREATE NEW Wallet".


![Gestion des wallets](assets/fr/09.webp)


A dialog box prompts you to name the Wallet. Enter a descriptive name (e.g. "Wallet Of Satoshi") and select the display currency (CUC, USD, EUR, etc.).


![Création wallet](assets/fr/10.webp)


Click on "CREATE". LNbits instantly generates a working Wallet Lightning for this user.


![Confirmation wallet créé](assets/fr/11.webp)


You now see the two existing wallets: the default Wallet "LNbits Wallet" created automatically, and the new "Wallet Of Satoshi". To simplify the user experience, you can delete the default Wallet by clicking on the delete icon (red trash can).


![Wallet final unique](assets/fr/12.webp)


The "Satoshi" user now has a single, clearly identified Wallet. Each user Wallet operates completely autonomously, while using the liquidity of your underlying LND node.


**Key concept**: All these wallets share the global liquidity of your Umbrel node. You don't create new Lightning channels for each Wallet - LNbits acts as an intelligent accounting layer that manages the allocation of funds within your existing Lightning infrastructure. That's the power of LNbits' multi-Wallet system.


### User login


Log out of the SuperUser account (icon top right) and return to the LNbits login page. You can now log in with the new user's credentials.


![Connexion utilisateur satoshi](assets/fr/13.webp)


Enter the user name ("Satoshi") and password previously defined, then click on "LOGIN". The user gains direct access to his personal Wallet, totally isolated from the administration Interface.


### Interface from Wallet user


Once connected, the user accesses his Interface from Wallet Lightning.


![Interface wallet utilisateur](assets/fr/14.webp)


The Interface features :


- Current balance**: Displayed in Sats and in the chosen currency (CUC in this example)
- Main actions**: "PASTE REQUEST" (paste a bill to pay), "CREATE Invoice" (generate a receipt), QR icon (quick scan)
- Transaction history** : Complete list of all payments and receipts
- Right side panel**: Configuration and access options


### Wallet mobile access


The right-hand side panel offers a particularly practical feature: mobile access to the Wallet. Unfold the "Mobile Access" section to discover the available options.


![Mobile Access](assets/fr/15.webp)


LNbits offers several ways to use this Wallet on a smartphone:


**Option 1: Compatible mobile applications


- Download **Zeus** or **BlueWallet** from App Store or Google Play
- Activate the **LndHub** extension in LNbits for this Wallet
- Scan the LndHub QR code with the mobile app to connect the Wallet


**Option 2: Direct access via mobile browser**


- The QR code displayed in "Export to Phone with QR Code" contains the full URL of the Wallet with integrated authentication
- Scan this QR code from your smartphone to open Wallet directly in your mobile browser
- Add page to home screen for quick access


**Important security**: This URL contains the API keys for full access to Wallet. Never share it publicly. Treat this QR code as you would your Bitcoin private keys - anyone scanning this QR code gets full access to Wallet.


This mobile feature turns your LNbits Umbrel instance into a veritable Lightning wallet server for you and your friends, while retaining complete sovereignty over your funds thanks to your self-hosted node.


### User access sharing


The main use case for this multi-user configuration is **sharing wallets with your family or close circle**. Once you've created a user with a dedicated Wallet (such as "Satoshi" in our example), you can share these login credentials with trusted members of your household.


**Access security on Umbrel**: Access to your LNbits instance on Umbrel is naturally protected, as it can only be accessed :


- On your local network** : Members of your household connected to the same WiFi/Ethernet network can access the instance
- Via VPN**: If you use a VPN such as Tailscale configured on your Umbrel server, authorized users can gain secure remote access


This double layer of protection (network access + user authentication) makes the "Allow creation of new users" option less critical on Umbrel. Only people who already have access to your network or VPN can reach the Interface login.


**Typical scenario**: You create a "dad" account, a "mom" account, a "business" account and so on. Each member of the family has their own isolated Wallet Lightning, while benefiting from the shared liquidity of your Umbrel node. Simply share the username and password - the user can then connect from any device on your local network or via your Tailscale VPN. Please see our dedicated Tailscale tutorial for more information:


https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Explore available extensions


Return to the Interface SuperUser and access the "Extensions" menu in the left side panel to discover the complete LNbits extension ecosystem.


![Extensions disponibles](assets/fr/16.webp)


LNbits offers a rich catalog of extensions that transform your instance into a veritable Lightning services platform:



- Jukebox**: Sats-powered jukebox system (Spotify payments)
- Support Tickets**: Paid support system (receive Satss to answer questions)
- TPoS**: Secure, mobile point-of-sale terminal for retailers
- User Manager**: advanced user and wallet management (which we've just used)
- Events**: Sale and validation of event tickets
- LNURLDevices**: Point-of-sale management, ATMs, connected switches
- SMTP**: Enable users to send emails and earn Satss
- Boltcards**: Programming NFC cards for Lightning tap-to-pay payments
- NostrNip5**: Create NIP5 addresses for your domains
- Splitpayments**: Automatic distribution of payments between multiple wallets


Each extension is activated with a single click from this Interface. Extensions marked "FREE" are free of charge, while some are available as "PAID" versions. Explore the catalog to identify the ones that match your needs - whether for business, family management, or experimenting with Lightning Network's capabilities.


## Advantages and limitations


**Benefits**: Financial sovereignty (full control over funds/keys/data), architectural flexibility (lossless VPS→full node migration), professional extension system, intuitive Interface.


**Limitations** : Software in beta (caution on amounts), security under administrator's responsibility, URLs containing sensitive API keys (HTTPS mandatory), multi-user management implies custodial responsibility.


## Best practices


**Backups**: seed PHOENIXD/credentials LND, LNbits database, `.env` files. Automate daily, keep off production server, encrypted. Test restores regularly.


**Maintenance**: Regularly check for updates (LNbits, Lightning backend, operating system). Always check release notes before major updates.



- On Umbrel**: App Store automatically notifies you of new versions. Synchronize extensions via "Manage Extensions" > "Update All". Check SQLite database inclusion in Umbrel automatic backups.
- On VPS**: Update manually with `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Monitor system logs: `sudo journalctl -u lnbits -f`.


## Conclusion


LNbits self-hosting offers a concrete path to Lightning financial sovereignty. VPS+PHOENIXD offers a lightweight solution for fast services, Umbrel full integration with existing Bitcoin node. The scalable architecture enables evolution from simple multi-user Wallet to sophisticated business use cases.


Self-hosting implies responsibility: back up seeds, protect access, start with modest amounts. With these precautions, LNbits becomes a robust solution for the Lightning economy, while preserving decentralization and autonomy.


## Resources


### Official documentation


- [LNbits Documentation](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Official installation guide](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)


### Community guides


- [Initial Ubuntu server configuration](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) by Daniel P. Costas (step-by-step VPS security)
- [LNbits + PHOENIXD installation on Ubuntu VPS](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) by Daniel P. Costas (complete guide)
- [LNbits Server on Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes