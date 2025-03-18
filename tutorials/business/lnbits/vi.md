---
name: LNbits
description: Merchant Accounting Platform
---
![presentation](assets/lnbits-intro.webp)

# Accounting system

LNbits is packed with lots of tools to control and channel your incoming and outgoing funds, connect your webstore or even devices like a hardware wallet or an ATM that you have built yourself. User types include:


- Wallet owners who want to use LNbits as an interface for their funds management as well as its extra-features.
- Online and offline merchants or service providers who want to accept Bitcoin onchain and Lightning Network payments.
- Developers who want to build Lightning Network applications.
- Node operators who want to integrate their node with the LNbits system for accounting purposes.
- All of those have different needs. We build LNbits in a modular way so that every user can use our features in a way that suits you best.

# Wallet manager

LNbits is a free and open-source accounting system - not a node manager. Channel management is the domain of the Lightning node that is connected to LNbits as a funding source like LND or c-lightning. The Superuser or Admin Users in the LNbits system are responsible for managing the overall accessability and configuration of the accounting features and internal extensions.

LNbits acts as an interface between the user and the Lightning node, providing a simple, user-friendly way to manage and interact with the payment network.

Think of LNbits like a “wordpress modular framework” for your node. An easy to manage platform, based on extensions that you can combine for numerous use cases.

Think of LNbits as your own bank financial management software. Your node offers channels to pay through and LNbits extends you node to be able to run more than one lightning wallet your node comes with. These wallets to not necessarily need to belong to yourself. Let’s say you, as the LN node runner, already have enough channel liquidity and funds and now you want to offer some bitcoin banking services to your friends, family, own shop or other regular merchants.

You will offer a simple way to them to open a “banking account” on your node without having access to other wallets on your node and to all your node liquidity, but only their part. Your node (the bank) only acts as a transport provider for their payments (in/out).

NOTE: all funds that your “customers” deposit into their LNbits bank accounts on your node, will go straight into your node LN channels. That means YOU are actually the real owner of those funds. You will have a big responsibility for their funds. Don’t be evil and run away with the funds, don’t be evil and charge high fees. We want to fuck the fiat banksters, not to fuck each others (bitcoin users).

# Demo platform

The demo can be found at [https://legend.lnbits.com](https://legend.lnbits.com). Its fully functional and can be used to learn about the Lightning Network and features of LNbits and LNURL in general. Though we cannot prevent you from it we would like to ask you to not use it for your production setup. Not only are we working on the servers often to test new features but also we would like to encourage you to run your own node and LNbits in a sovereign way. If you think running a node is too much asked for the moment you can connect LNbits to a custodian funding sservice in the cloud like Opennode, Luna or Votage or to the Lightning Tipbot on Telegram just to name some.

# LNbits flyer

Want to hand over some basic info to a merchant or a building friend of yours ? We are very happy to announce our first flyer for everyone to use. The size is a globally typical flyerformat with 6 pages (2 folds) and a width of 3508 and a height of 2480px.

LNbits for merchants: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits for builders: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Some Basics

LNbits works based on the LNURL protocol which means that requests are valid in two forms: either as https:// clearnet link (no self-signed certificates allowed) or as http:// v2/v3 onion link. To offer LNbits services like LNURLp/w QR codes or NFC Cards, that can be used in the wild, you will need to open LNbits up to clearnet (https).

Before you install LNbits make sure to have read and understood the following general guides about what LNbits is and which possibilities it unleashes for you.


- [LND Guide](https://docs.lightning.engineering/) | Installing LND
- [LND Config Example](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | LND Settings
- [CLN Guide](https://docs.corelightning.org/docs/installation) | Installing CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips)  Nostr Spec
- [Run a watchtower](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Very important!

More detailed guides using LNbits in specific use case scenarios here:


- [Getting Started with LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack guide
- [ToDos for your safety with LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Private Banks on Lightning Network](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Substack guide
- [Run custodian wallets for your friends & family](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack guide
- [LNbits for a small restaurant / hotel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack guide
- [Using LNbits Streamer copilot](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack guide
- [Start your NOSTR Market with LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack guide
- [Using LNbits for schools projects or festival events](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools)  Substack guide

# Install LNbits

## Basic installation guide

LNbits can be installed on any Linux OS machine. It does not require a powerful machine or server, just enough RAM memory and some disk space for the database. It can be run separately from a BTC/LN node (local PC or remote VPS) or together on the same machine with the node or already installed in a bundle node software machine.

You can choose between the most common package managers like poetry and nix. By default, LNbits will use SQLite as its database. You can also use PostgreSQL which is recommended for applications with a high load. [Here is a guide for basic installation using poetry or nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

For everyone new to this, you will find more detailed step-by-step guides for getting your LNbits running in specific enviornments:


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [LNbits on a VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) by Leo

You can also find a video on the [dockerised Setup on a VPS with PostgreSQ, LightningTipBot as a funding source using nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[More installation scenarios here](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

For bundle software nodes, please refer to their specific documentation about LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

When you´re not into the technical stuff and neither want to host your funding source nor your lnbits yourself there is a [LNbits SaaS version](https://saas.lnbits.com) (Software-as-a-service) you can use. It is basically like LNbits in a cloud but you can define the funding source (e.g. your Node, a LNbits wallet, the LNtipbot, fakewallet etc) and environmnent variables yourself - which mostly is not the case on other cloud-solutions.

[Here is a detailed guide how to use LNbits SaaS for specific use cases](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Funding sources

LNbits is not a node management software but a LN focused accounting system on top of a LND or CLN funding source. After the first installation you can visit your LNbits at http://localhost:5000/.

To modify the funding source go to your super-user-URL and select a funding source within "Manage Server" or edit the .env file by modifying `LNBITS_BACKEND_WALLET_CLASS` to your needed source if you set `adminUI=TRUE` in the `.env`.

You will find the .env file within your lnbits/ or lnbits/apps/data folder by extending the command to list files in your directory by `ls -a`.

You might also need to install additional packages or perform additional setup steps, selecting the desired funding source. After a restart your new setup will be active.

Which funding sources can I use for LNbits?

LNbits can run on top of many lightning-network funding sources. Currently there is support for CoreLightning, LND, LNbits, LNPay, OpenNode, with more being added regularly.

It is important to choose a source that has a good liquidity and good peers connected. If you use LNbits for public services your users payments can only then flow happily in both directions.

A backend wallet (funding source) can be configured using the following LNbits environment variables in the `.env` file or within your superuser account under Manage-Server section.

If you would like to use the .env version you can find the parameters here:

### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-rpc
- Spark (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon or Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: port
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon or Bech64/Hex

You can also use an AES-encrypted macaroon (more info) instead by using


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

To encrypt your macaroon, run `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.

### LNbits (another LNbits instance)


- LNbits instance hosted on a cloud server or your own home server
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! Do NOT use this one for production / commercial purposes, only for testing !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Lightning TipBot

To connect your [Lightning Tipbot](https://t.me/LightningTipBot) from Telegram you will need to set the following parameter:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: To get the Key you will need to run /api in a private chat with the LightningTipbot on Telegram once.

Also see this tutorial how to install [LNbits with LightningTipBot via vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### IBEX HUB

Register [here](https://ibexpay.ibexmercado.com/onboard) then get your keys/tokens from there, endpoint is https://ibexpay-api.ibexmercado.com.

More info see [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

For the invoice listener to work you have a publicly accessible URL in your LNbits and have to set up a [LNPay webhook](https://dashboard.lnpay.co/webhook/) pointing to `<your LNbits host>/wallet/webhook` with the "Wallet Receive" event and no secret given. The setting  `https://mylnbits/wallet/webhook` will be the endpoint url that gets notified about any payment.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

### OpenNode

For the invoice to work, you need to have a publicly accessible URL in your LNbits. The webhook setting is optional.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

### Alby

Alby is a browser extension with LN wallet functionalities and LNDHUB account that can be used as funding source for LNbits. [More details here](https://getalby.com/).

For the invoice to work you must have a publicly accessible URL in your LNbits. No manual webhook setting is necessary. You can generate an Alby access token here: https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

## Additional / Troubleshooting Guides

Here are some additional instructions in case your would need them. Click on the arrow to expand the description.

### The Killswitch 🚨

There have been so many dangerous bugs lately not only in the whole space but also in LNbits that we decided to do something about it. You can now opt-in for warnings and/or to take direct action, when a vulnerability or a bug that could lead to the loss of funds occurs again.

![killswitchn](assets/lnbits-killswitch.webp)

If switched to void-wallet all usertypes on the instance will see a yellow banner where you would normally find the "LNbits is in Beta" notice next to the theme/language area up to the right - and is the most obvious hint, that something happend. Have a look at your new server-tab highlighted in green in the left part of the window.

How does it work ? When the killswitch is enabled, a secret github repository only available to the LNbits core team will be checked at an interval of X minutes (which can be specified). If a vulnerable bug is published in this repository, it serves as a signal that triggers the killswitch on all installations that subscribed and transitions your lnbits instance to use the void wallet. If the clouds have cleared and you have installed the security update you can set your funding source to your node, wallet or whatever you are using again also via the Manage Server section. This wiki has a section about switching funding sources if you do not know what to configure.

### Difference between admin and superuser

The LNbits Admin UI lets you change LNbits settings via the LNbits frontend. It is disabled by default and the first time you set the enviroment variable `LNBITS_ADMIN_UI=true` in the `.env` file, the settings are initialized and will be used. From there on the according settings from the database instead those of the .env file are used.

### Super User

With the Admin UI we introduced the super user which has access to the server so can change settings that may crash the server or make it unresponsive via frontend and api, like e.g changing the funding source. The super user is only stored inside the settings table of the database. After the settings are "reset to defaults" and restarted a new super user is created. We also added a decorator for the API routes to check for the existance of a super user. Its ID is never sent over the api and the frontend and only receives a bool (yes/no) if you are super user or not.

Only the super user is allowed to brrrr satoshis to different wallets via the "Top Up" section.

You can as well post the super user via webhook to another service when it is created. More info here https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

In the frontend you will also find the possibility to change the shop-image that is shown on the "create wallet" page by opening the Manage Server section and choosing Theme -> Custom Logo.

### Admin Users

Enviroment variable: `LNBITS_ADMIN_USERS`, comma-seperated list of user IDs. Admin Users can change settings in the admin ui - with the exception of funding source settings, because this would require a server restart and could potentially make the server inaccessable. Also they have access to all the extensions dedicaated to them in `LNBITS_ADMIN_EXTENSIONS`.

### Allowed Users

Enviroment variable: `LNBITS_ALLOWED_USERS`, comma-seperated list of user IDs. By defining these users LNbits will no longer be useable by the public. Only defined users and admins can then access the LNbits frontend.

#### Update LNbits

A normal updating of your LNbits local instance is simply by copy paste the following CLI commands:

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

If you run Raspiblitz or MyNode you might additionally need a

```
sudo systemctl restart lnbits
```

at the end, because it runs LNbits as a service.

On Umbrel/Citadel the commands would be

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### SQLite to PostgreSQL migration

If you already have LNbits installed and running on an SQLite database we highly recommend to migrate to postgres if you are planning to run LNbits on scale.

There's a script included that can do the migration easyly. You need to have Postgres already installed and there should be a password for the user (see Postgres install guide above). Additionally, your LNbits instance needs to run once on postgres to implement the database schema before the migration can work:

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Hopefully now everything works and gets migrated... Launch LNbits again and check if everything is working properly.

#### Backup and restore of the database

Please refer to [this very detailed guide about the backup & restore process](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### Funding my LNbits wallet from my node doesn't work

If you want to send sats from the same node that is the funding source of your LNbits, you will need to edit the lnd.conf file.

The parameters to be included are: `allow-circular-route=1`

Please do so in the section Application options of your lnd.conf. On some bundle node the start of LND could fail otherwise.

NOTE: It is recommended to instead use the new adminUI extension with the "TopUp" option to add funds to a LNbits account.

#### Error 426

I got the error: "lnurl needs to be delivered over publically accessible https domain or tor. 426 upgrade required"</summary>

This error usually is because your LNbits behind a ngnix tunnel is not forwarding the LNURL address correct. Stop your LNbits and edit the .env file adding this line:

`FORWARDED_ALLOW_IPS=*`

Also if you use a ngnix setup, be sure you have these headers in the ngnix config:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Network Error

I got "https error", network error" or others when scanning a QR</summary>

Bad news, this is a routing error that might have quite a lot of reasons. First check the QR´s LNURL with the [Lightning Decoder](https://lightningdecoder.com/) if you can find something weird in there. Let´s try a few of the most possible problems and their solutions.

LNbits is running via Tor only, you can't open it on a public domain like lnbits.yourdomain.com


- Given that you want your setup to stay like this open your LNbits wallet using the .onion URI and create it again. In this way the QR is generated to be accessible via this .onion URI so via tor only. Do not generate that QR from a .local URI, because it will not be reachable via internet - only from within your home-LAN.
- Open your LN wallet app that you used to scan that QR and this time by using tor (see wallet app settings). If the app doesn't offer tor, you can use Orbot (Android) instead. See installation section for detailed instructions on how to open your LNbits for clearnet/https.

#### Prevent others from generating wallets on my LNbits

When you run your LNbits in clearnet basically everyone can generate a wallet on it. Since the funds of your node are bound to these wallets you might want to prevent that. There are two ways to do so:

Configure allowed users and extensions in the `.env` file ([see the env example here](https://github.com/lnbits/lnbits/blob/main/.env.example)). This only works if you use the setting `adminUI=FALSE` in the .env, otherwise you need to do that in the Manage Server section -> Users -> Allowed Users. Everyone else will not be allowed afterwards.

#### Customize the invoice expiry timeframe

Now you can generate invoices with a custom expiry. Compatible with backends: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet so far!

You can set `LIGHTNING_INVOICE_EXPIRY` in your .env file or use the AdminUI to change the default value for all invoices. There is also a new field in the /api/v1/payments endpoint where you can set expiry in the JSON data.

## Wallet-URL deleted

### Wallet on demo server legend.lnbits

Always save a copy of your wallet-URL, Export2phone-QR or LNDhub for your own wallets in a safe place. LNbits CANNOT help you to recover them when lost.

### Wallet on your own funding source/node

Always save a copy of your wallet-URL, Export2phone-QR or LNDhub for your own wallets in a safe place. You can find all LNbits users and wallet-IDs in your LNbits user manager extension or in your sqlite database. To edit or read the LNbits database, go to the LNbits /data folder and look for the file called sqlite.db. You can open and edit it with excel or with a dedicated SQL-Editor like [SQLite browser](https://sqlitebrowser.org/).

Also you can dump the wallets via cli and view every wallet within your database.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

The output will look something like this

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

and you want to put these values into a url like this

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Whereby you replace f8a43fc363ea428db5c53b3559935f1f with the value that comes before the name (in our example f8a43fc363ea428db5c53b3559935f1f) and 1280ff5910a9c485a782a2376f338b6c is your user and should become the value shown after the name. To quit sqlite3 put in

```
.quit
```

#### LNURL for a lightning-address vice versa

Try this [encoder](https://lnurl-codec.netlify.app/) from fiatjaf or [this one](https://lightningdecoder.com/). For to pay or check an LNURLp you can as well use [LNurlpay](https://wwww.lnurlpay.com/). It should state HTTPS NOT HTTP.

#### Configure a comment that people see when paying to my LNURLp QR

When you create a LNURL-p, by default the comment box is not filled. That means comments are not allowed to be attached to payments.

In order to allow comments, add the characters lenght of the box, from 1 to 250. Once you put a number there, the comment box will be displayed in the payment process. You can also edit a LNURL-p already created and add that number.

![lnbits comments](assets/lnbits-comments.webp)

#### Deposit onchain BTC to LNbits

There are two ways to exchange sats from onchain BTC to LN BTC (resp. to LNbits).

##### Via an external swap service.

Other users that dont have access to your LNb its can use a swap service like [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) or [ZigZag](https://zigzag.io/). This is useful if you provide only LNURL/LN invoices from your LNbits instance, but a payer only has onchain sats so they will have to swap those sats first on their side. The procedure is simple: user sends onchain btc to the swap service and provides the LNURL / LN invoice from LNbits as destination of the swap.

##### Using the Onchain and Boltz LNbits extension.

Keep in mind that this is a separate wallet, not the LN btc one that is represented by LNbits as "your wallet" upon your LN funding source. This onchain wallet can be used also to swap LN btc to (e.g. your hardwarewallet) by using the LNbits Boltz or Deezy extension. If you run a webshop that is linked to your LNbits for LN payments, it is very handy to regularily drain all the sats from LN into onchain. This leads to more space in your LN channels to be able to receive new fresh sats.

Procedure for those without a bitcoin hardware wallet:


- Use Electrum or Sparrow wallet to create a new onchain wallet and save the backup seed in a safe place.
- Go to wallet information and copy the xpub.
- Go to LNbits - Onchain extension and create a new watch-only wallet with that xpub.
- Go to LNbits - Tipjar extension and create a new Tipjar. Select also the onchain option besides the LN wallet.
- Optional - Go to LNbits - SatsPay extension and create a new charge for onchain btc. You can choose between onchain and LN or both. It will then create an invoice that can be shared.
- Optional - If you use your LNbits linked to a Wordpress + Woocommerce page, once you create/link a watch-only wallet to your LN btc shop wallet, the customer will have both options to pay on the same screen.

When you receive a payment in LNbits, the transaction log will display only a resumed type of the transaction.

![lnbits payment details](assets/lnbits-payment-details.webp)

In your transaction overview you will find a little green arrow for received and a red arrow for the funds that are sent.

If you click on those arrows, a details popup shows attached messages as well as the sender´s name if given.

To Configure a name to appear within payments, in LNbits this is currently not possible to do - but to receive. This is only possible if the sender's LN wallet supports [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) like [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

You will then see an alias/pseudonym in the details section of your LNbits transactions (click the arrows). Note that you can give any name there and it might not be related to the real sender´s name if your receive such.

![lnbits namedesc](assets/lnbits-namedesc.webp)

To import your LNbits account in a wallet app, open your LNbits with the account / wallet you want to use, go to "manage extensions" and activate the LNDHUB extension. Open the LNDHUB extension, choose the wallet you want to use and scan either the "admin" or "invoice only" QR, depending on the security level you want for that wallet.

You can use [Zeus](https://zeusln.app/) or [Bluewallet](https://bluewallet.io/) as wallet apps for a lndhub account whereby BW supports more than one such wallet.

When doing this we recommend to as well set the LN network URI to the one of your own node. If your LNbits instance is Tor only, you also have to use theose apps with Tor activated. Also in this case you need to open the LNbits page through your Tor .onion address.

If you have an Error "unsupported hash type" when using a ypub in On-chain extension, check if your LNbits instance is using python 3.10 it could be affected by [this issue](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Edit the openssl.cnf like described in the stackoverflow answer and restart your LNbits.

## Tooling & Building with LNbits

LNbits has all sorts of [open APIs](https://legend.lnbits.com/docs) and tools to program and connect to a lot of different devices for a gazillion of use-cases.

When you are new to building start with this [MakerBits presentations](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) from Ben Arc about building gadgets based on LNbits.

### IMPORTANT:


- LNbits works based on the LNURL protocol which requests are valid in two forms: either as https:// clearnet link (no self-signed certificates allowed) or as http:// v2/v3 onion link. To offer LNbits services like LNURLp/w QR codes or NFC Cards, that can be used in the wild, you will need to open LNbits to clearnet (https).
- Only use DATA-Cables to power your esp32. Not all cables support data in addition to powering the esp. You wouldnt be the first if the cable that came with the esp is a power-only one
- Make sure to not use a USB-Hub with other devices attached. This can lead to weird effects that are hard to debug (e.g. not starting or stopping).
- To realize esp projects with a MacOS you will need an UART Bridge Driver. If you have problems with the driver on Mac or Linux systems, you can find those here or, if a TTGO Display is involved this one. If you are on windows and have problems connecting make sure to download the OLD version 11.1.0 because the newer one is not working! You can also find a serial terminal here to check your connection - set to baudrate 115200.
- Though it is way more comfortable to use Platform.io (e.g. dependencies are installed automatically) we recommend using Arduino for everyone new to building.
- TT-Go Display S3: The colour of the tab of the screen protector film tells you which controller exactly (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) has been used to build it. Keep it to be able to debug if you programm yourself and the screen does not display graphics correctly, e.g. colours wrong, mirrored images, or stray pixels at the edges. If you ever need to do this, there is an epic guide on adjusting for different displays
- Always use lowercase lnurl239xx instead of LNURLl239xx
- Adding lightning:lnurl1234xyz will create a QR that requests to open the users wallet for this invoice on scan (last installed lightning app on iOS, setting in Android)
- If you are flashing an esp32 via web will only work with these browsers (TL:DR Chrome, Edge & Opera).
- Please note this PIN-OUT reference for the esp
- When you use FOSSoftware or FOSGuides pls always link the author. Everyone loves to watch their baby grow and it also initiates a building chain that is quite awesome to watch :)

Come to the [Makerbits Telegram Group](https://t.me/makerbits) if you need help with a project - we got you!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Here are some projects categories you can build with LNbits:


- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Vending machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora and Mesh Networking](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [HELPERS & RESOURCES](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [More examples of projects "Powered by LNbits" here](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Use cases for LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)