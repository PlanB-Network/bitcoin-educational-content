---
name: BTCPay Server - Umbrel
description: Installing and using BTCPay Server on Umbrel to accept Bitcoin and Lightning
---

![cover](assets/cover.webp)


In the Bitcoin ecosystem, accepting payments represents a major challenge for merchants and businesses alike. Traditional solutions, whether banking (credit cards, Stripe, PayPal) or even Bitcoin (BitPay, Coinbase Commerce), impose intermediaries who levy substantial fees, collect your sensitive business data, and can block or censor your transactions at their whim. This dependence runs counter to Bitcoin's fundamental principles of decentralization, confidentiality and financial sovereignty.


BTCPay Server is emerging as the open-source answer to this problem. This self-hosted payment processor turns your own Bitcoin node into a professional infrastructure, with no middleman, no additional processing fees and no compromise on privacy. Developed by a global community of contributors since 2017, BTCPay Server allows you to receive Bitcoin and Lightning payments directly into your wallets, retaining full control of your funds at all times.


Traditionally, installing BTCPay Server requires advanced technical skills: Linux server configuration, mastery of Docker, SSL certificate management and network security. Umbrel revolutionizes this approach with a one-click installation directly integrated with your Bitcoin and Lightning node. This simplification makes what was previously reserved for experienced technicians accessible to everyone.


**Important to understand**: BTCPay Server on Umbrel works by default on your local network only. You can create invoices, accept Lightning and Bitcoin payments, and manage your accounting from any device connected to your home network (computer, smartphone, tablet). This configuration is ideal for billing in-person services, managing face-to-face payments, or using BTCPay Server from your local network. On the other hand, to integrate BTCPay Server into an online store that is publicly accessible on the Internet, an additional configuration with public exposure will be required (we'll cover this issue at the end of the tutorial).


This tutorial takes you through the complete installation of BTCPay Server on Umbrel, configuring your Bitcoin wallet and Lightning node, creating and paying invoices, and managing accounting reporting. You'll discover how to use BTCPay Server efficiently on your local network, and then we'll look at solutions for public display if you want to integrate it with an e-commerce site.


## Prerequisites


To follow this tutorial, you need to have Umbrel correctly installed and configured. If you haven't already done so, please see our tutorial on Umbrel installation.


https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Your Bitcoin Core node must be fully synchronized with the blockchain (100% in Umbrel's Bitcoin application). This initial synchronization usually takes between 3 days and 2 weeks, depending on your hardware and Internet connection.


To accept instant Lightning payments, you'll also need to install LND (Lightning Network Daemon) on Umbrel. See our tutorial on installing and configuring LND on Umbrel if you'd like to enable this feature.


https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Allow at least 50 GB of free disk space for BTCPay Server, its databases and Lightning data. A stable Internet connection via Ethernet cable is strongly recommended to avoid disconnections.


## Installing BTCPay Server on Umbrel


From the Umbrel interface (`umbrel.local`), access the App Store and search for "BTCPay Server" in the Bitcoin category.


![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)


Click Install. Umbrel automatically checks that Bitcoin Core and LND are installed, then starts deployment (2-5 minutes).


![Dépendances requises pour BTCPay Server](assets/fr/02.webp)


Once installed, open the application. You'll need to create an administrator account with strong credentials.


![Création du compte administrateur BTCPay Server](assets/fr/03.webp)


Once your account has been created, BTCPay Server will immediately prompt you to set up your first store. Choose a business name and select a reference currency (EUR, USD or BTC).


![Création du premier magasin BTCPay Server](assets/fr/04.webp)


## Access BTCPay Server on your local network


BTCPay Server is accessible from any device on your local network (WiFi or Ethernet). Access from your browser to :


```url
http://umbrel.local
```


Or direct to :


```url
http://umbrel.local:3003
```


**Remote access with Tailscale**: To access BTCPay Server from anywhere in the world, use Tailscale. This secure VPN lets you connect to your Umbrel as if you were on your local network. See our tutorial dedicated to Tailscale on Umbrel.


https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Configuring your Bitcoin wallet


To accept payments, you need to configure a Bitcoin wallet. BTCPay Server displays configuration options in the dashboard.


![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)


To configure wallet Bitcoin, go to "Wallets" > "Bitcoin".


You have two options: create a new wallet directly in BTCPay, or import an existing wallet. For importing, several methods are available:


- Connect hardware wallet** (recommended): Import your public keys via the Vault application
- Import wallet file** (recommended): Upload an exported file from your wallet
- Enter extended public key**: Enter your XPub/YPub/ZPub manually
- Scan wallet QR code** : Scan a QR code from BlueWallet, Cobo Vault, Passport or Specter DIY
- Enter wallet seed** (not recommended) : Enter your 12- or 24-word recovery phrase


![Options de création de portefeuille](assets/fr/06.webp)


For this tutorial, we're going to create a new Hot wallet: the private key will therefore be stored on our Umbrel server. In this case, we strongly advise you to move the funds regularly to a cold wallet to avoid storing large amounts on the server.


![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)


Once configured, BTCPay Server confirms that your wallet is ready to accept on-chain payments.


![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)


## Activate Lightning Network


To accept instant Lightning payments, go to Wallets > Lightning. Then, as your LND node is already in place on Umbrel, simply click on the "Save" button to validate the connection between your BTCPay Server and your Lightning node.


![Configuration du nœud Lightning](assets/fr/09.webp)


## Create and pay invoices


In the BTCPay Server interface, navigate to Invoices > Create Invoice. Enter the amount, add an optional description, and click Create.


![Création d'une nouvelle facture](assets/fr/10.webp)


You can then click on the "Checkout" button to display the invoice. BTCPay then generates an invoice with a unified QR code (BIP21) containing the Bitcoin address and the Lightning invoice.


![Détails de la facture générée](assets/fr/11.webp)


Your customer can scan the QR code with any compatible wallet.


![Page de paiement avec QR code](assets/fr/12.webp)


Once paid, the invoice becomes "Settled" in a matter of seconds for Lightning.


![Confirmation de paiement réussi](assets/fr/13.webp)


## Payment management and tracking


In the "Reporting" section, "Invoices" tab, you'll find a complete history of your invoices with date, amount, status and payment method. You can export it if required.


![Section reporting avec l'historique des factures](assets/fr/14.webp)


## Store configuration


BTCPay Server allows you to manage multiple stores with distinct parameters. Each store represents a separate business entity: e-commerce store, physical point of sale, or service billing.


In the store settings, you will find several important sections:


![Paramètres du magasin](assets/fr/15.webp)



- General Settings**: Shop name, reference currency (BTC, EUR, USD), invoice expiry time (default 15 minutes), number of blockchain confirmations required
- Rates**: Configuration of exchange rate sources and fiat/Bitcoin conversions
- Checkout Appearance**: Customize the appearance of your checkout pages (logo, colors, personalized messages)
- Email Settings**: Configuration of e-mail notifications for payments received
- Access Tokens**: Management of API tokens for e-commerce integrations (WooCommerce, Shopify, etc.)
- Users**: Manage user access to the store with different levels of permissions (Owner, Guest)
- Webhooks**: Webhook configuration for real-time synchronization with your accounting or ERP system


BTCPay Server also offers a Plugins section to extend functionality with e-commerce integrations, point-of-sale systems and additional tools.


![Gestion des plugins](assets/fr/16.webp)


## Advantages and limitations of local use


**Advantages of BTCPay Server over Umbrel** :


- Total sovereignty: exclusive control of private keys and funds, no third party can freeze or censor your payments
- Substantial savings: only Bitcoin network costs (a few cents on Lightning) vs. 2-3% on traditional processors
- Maximum confidentiality: no registration, identity verification or data sharing with third-party companies
- Open-source architecture guarantees transparency, auditability and sustainability via a large community of developers
- Easy installation via Umbrel, with no need for advanced technical skills


**Important limitations** :


- Local network only**: BTCPay Server on Umbrel is only accessible from your home network. Perfect for face-to-face billing, freelance services or small physical businesses, but unsuitable for publicly accessible online stores.
- Full technical responsibility: node maintenance, regular backups, connectivity monitoring
- Lightning liquidity management: opening and managing channels with sufficient inbound capacity
- Support limited to community documentation and forums, requiring more autonomy than a commercial customer service department


This local network limitation is the main obstacle to integrating BTCPay Server into an e-commerce store, where customers need to be able to access payment pages from anywhere on the Internet.


## Best practices and safety


Activate automatic Umbrel backups and store a copy on external media (USB stick, hard disk, encrypted cloud). Keep your Bitcoin seeds (recovery phrases) in a safe, physically separate place. Back up LND's channel.backup file for Lightning recovery.


Regularly monitor Bitcoin Core synchronization, Lightning channels and BTCPay Server response. A simple weekly test: generate and pay a bill for a few satoshis. Keep Umbrel up to date (security patches, enhancements). Make a backup before major updates. For professional use, consider external monitoring (UptimeRobot) with e-mail/SMS alerts.


## Exposing BTCPay Server publicly for an online store


To integrate BTCPay Server into a web-based e-commerce store (WooCommerce, Shopify, etc.), your customers need to be able to access payment pages from anywhere, not just your local network.


**Solution: Nginx Proxy Manager**


You can expose BTCPay Server publicly using Nginx Proxy Manager (available in the Umbrel App Store). This solution requires :


- A domain name (classic or free via DuckDNS, No-IP, Afraid.org)
- Configuring port forwarding (ports 80 and 443) on your router
- Installation of Nginx Proxy Manager, which automatically manages SSL certificates


This configuration exposes your server to the Internet and requires extra vigilance (strong passwords, 2FA, regular updates). We'll be preparing a dedicated tutorial detailing this complete procedure.


## Conclusion


BTCPay Server on Umbrel combines the power of the Bitcoin node with the simplicity of Umbrel to create a self-hosted professional payment infrastructure accessible to all. This financial sovereignty comes with a maintenance responsibility, but Umbrel greatly simplifies the operational burden compared to the benefits: elimination of processing fees, protection of your privacy, resistance to censorship and total control of your funds.


Local network use already covers a wide range of applications: billing for freelance services, in-person payments, small physical shops, or simply learning and experimenting with Bitcoin and Lightning in a controlled environment. For e-commerce needs requiring public exposure, the Nginx Proxy Manager solution exists, but requires additional technical configuration, which we'll detail in a dedicated tutorial.


Whether you're running a business, a fledgling project or simply experimenting, BTCPay Server on Umbrel offers complete financial autonomy. The path begins with your first store, your first invoice, your first payment received directly into your sovereign infrastructure.


## Resources


### Official documentation


- [Official BTCPay Server website](https://btcpayserver.org)
- [Complete BTCPay Server documentation](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Tailscale documentation](https://tailscale.com/kb)

### Community and support


- [Forum BTCPay Server](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)