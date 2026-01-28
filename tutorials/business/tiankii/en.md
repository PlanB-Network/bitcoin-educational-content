---
name: Tiankii
description: Lightning suite of tools for retailers and consumers
---

![cover](assets/cover.webp)


In the Bitcoin ecosystem, accepting payments in real time remains a major challenge for businesses and individuals. Traditional solutions often require advanced technical knowledge, a complex infrastructure to maintain, or require funds to be held by intermediaries. This situation is holding back the mass adoption of Bitcoin as an everyday currency, despite the promise of Lightning Network's technological advances.


Tiankii, a Salvadorian company born in 2021, responds to this problem by offering an accessible, modular Bitcoin infrastructure. Rather than forcing the adoption of a closed ecosystem, Tiankii offers a suite of interconnected tools enabling anyone to integrate Bitcoin Lightning into their business without sacrificing control of their funds.


## What is Tiankii?


### Origin and philosophy


Tiankii - a Nahuatl term meaning "open-air market accessible to all" - is El Salvador's first 100% Bitcoin start-up. Founded by Darvin Otero following the adoption of Bitcoin as the country's legal tender, the company aims to transform Bitcoin from a store of value into a transactable currency for everyday purchases. Unlike custodial platforms, Tiankii adopts a non-custodial approach where users retain control of their funds, with the infrastructure serving only as a technical intermediary.


### Technical architecture


Tiankii is positioned as a provider of Bitcoin-as-a-Service infrastructure based on Lightning Network. This second-layer technology enables near-instantaneous transactions with negligible costs, making micropayments and everyday purchases possible.


The architecture is based on three pillars:


**Lightning-first**: Systematically favor the Lightning network for its speed and lower costs, while retaining on-chain transaction support for large amounts.


**Open standards**: Use of LNURL to automate payment requests, Lightning Address for readable email IDs, and Bolt Card for interoperable NFC payments.


**wallet-agnostic modularity**: Possibility of connecting different Lightning portfolios (LNbits, Blink, BlueWallet) or your own node, offering maximum flexibility depending on the level of expertise and autonomy required.


## Tiankii ecosystem tools


### Bitcoin POS - In-store payment terminal


The application turns smartphone or tablet into a Lightning terminal. The merchant enters the amount in local currency, and the app generates a Lightning QR code or accepts a Bolt Card. Transactions are instantly credited commission-free, with automatic conversions in over 150 currencies, tip management and sales history.


### Merchant Dashboard - Unified sales management


Interface web centralized to connect its wallet Lightning, track transactions in real time, issue invoices and generate accounting reports. The platform aggregates all channels: in-store payments (POS), online sales (e-commerce plug-ins), or API integrations. Payments converge on the chosen wallet.


### Bitcoin Contactless Card (Bolt Card)


The NFC Bolt Card represents Tiankii's major innovation in democratizing Bitcoin for the general public. Functioning like a contactless bank card, it lets you pay for Bitcoin Lightning purchases simply by tapping on a compatible terminal.


Unlike traditional custodial solutions, this card follows an open standard guaranteeing interoperability. Users can link it to their own wallet via the IBI application, thus retaining their private keys and full control over the associated funds. Payment takes just a second, with no need to take out your smartphone or have an active internet connection at the time of payment.


This solution is particularly inclusive for people unfamiliar with smartphones, offering an accessible gateway to the Bitcoin economy.


### IBI App - Interface individual Bitcoin


The IBI application (Individual Bitcoin Interface) is designed for individuals wishing to use Bitcoin Lightning on a daily basis. Its main advantage lies in the generation of a personalized Address Lightning, a payment identifier readable in email format (example: alice@ibi.me).


This identifier drastically simplifies the receipt of payments: no need to generate a new invoice for each transaction, the sender can simply enter the Lightning address. The interface also lets you manage your Bolt Card (activation, deactivation, spending limits), connect various Lightning wallets, and make payments by scanning QR codes.


### E-commerce plugins


Ready-to-use integrations for WooCommerce, Shopify and Cloudbeds. Installs in minutes to add Bitcoin Lightning to checkout. Benefits: zero commission (vs. 2-3% credit cards), instant settlement, worldwide access, elimination of chargebacks. Payments arrive directly on the merchant's connected wallet.


### Bitcoin API and developer tools


The Tiankii SDK makes it possible to integrate Bitcoin Lightning into existing applications without maintaining its own node. API handles invoice creation, payment verification and bulk mailings via a robust infrastructure hosted on Google Cloud. Command Center completes the offering for organizations with Address Lightning on custom domains, bulk payments, and centralized management of NFC terminals and cards.


## Installation and first steps


### Essential prerequisites


Using Tiankii requires no complex technical prerequisites. The applications operate via a web browser on a smartphone, tablet or computer. No native application installation is required: all you need is Internet access and a recent browser to access IBI or the Merchant Dashboard.


**For private users (IBI App)**: No prior wallet Lightning is required. When you create your account, Tiankii automatically configures a working Address Lightning via the [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), a nodeless implementation that uses the Liquid network in the background. You can immediately receive and send payments without any technical configuration. This solution drastically simplifies access for beginners, while remaining self-custodial.


**For merchants (Merchant Dashboard)** : The connection of an existing wallet Lightning is mandatory to use Point of Sale terminals and receive payments. Tiankii supports many solutions: mobile wallets (Blink, Strike), self-hosted solutions (LNbits, LND/CLN node), or web wallets (Alby). Detailed connection guides are available in the Resources section of this tutorial.


### For private customers: IBI App


**Account creation


Go to accounts.ibi.me to create your account. On this page you can choose between two account types: "Personal Use" for individual use, or "Business Use" for commercial use. Select "Personal Use" to access the tools for receiving and sending payments in Bitcoin.


![Choix du type de compte](assets/fr/01.webp)


After selecting "Personal Use", you will be automatically redirected to go.ibi.me to complete your registration. This can be done via email, phone number, or using your Google, Microsoft or Twitter account. Once created, you can immediately access your IBI interface, with your Lightning Address already operational.


![Création du compte](assets/fr/02.webp)


**Interface main**


The IBI interface displays your balance in satoshis and local currency (USD). Three buttons allow you to interact: "Receive" to receive payments, "Scan" to scan a QR code, and "Send" to send satoshis.


![Interface IBI](assets/fr/03.webp)


**Receive payment**


To receive satoshis, press "Receive". The application automatically generates a QR code and displays your personalized Address Lightning (nom@ibi.me format). Share this address or the QR code with the sender: the funds arrive instantly in your IBI account.


![Réception avec Lightning Address](assets/fr/04.webp)


Once your balance has been credited, you can use these satoshis to make payments.


**Send a payment**


To send satoshis, press "Send". You can either scan a Lightning QR code, or directly enter a Lightning Address destination.


![Solde et boutons IBI](assets/fr/05.webp)


![Interface d'envoi](assets/fr/06.webp)


Enter the desired amount in satoshis, check the equivalent amount in local currency, then confirm payment.


![Confirmation du montant](assets/fr/07.webp)


A success notification confirms the shipment with details: amount sent, transaction fee, and recipient.


![Paiement réussi](assets/fr/08.webp)


**Account management


In Settings, you can manage your Bitcoin NFC cards (Bolt Cards). The interface lets you activate, deactivate or set spending limits for your cards.


![Historique des transactions](assets/fr/09.webp)


![Paramètres IBI](assets/fr/10.webp)


### For merchants: Merchant Dashboard and POS


**Business account creation


Go to accounts.ibi.me to create your account. Select "Business Use" to access merchant tools. This type of account unlocks access to the Merchant Dashboard and point-of-sale terminals.


After selecting "Business Use", you will be automatically redirected to the Merchant Dashboard (pay.tiankii.com). This takes you to the business management interface with revenue tracking, transactions and payment tools. To start accepting payments, you must first connect your wallet Lightning by clicking on the link at the top of the page (see arrow on image).


![Dashboard marchand](assets/fr/11.webp)


**wallet Lightning** connection


Crucial step in activating your point of sale: connect your wallet Lightning to receive payments. The interface offers several connection options. Please note that some options (Bitcoin Onchain and Lightning Network) are still under development and appear grayed out on the interface.


![Options de connexion wallet](assets/fr/12.webp)


For this tutorial, we're using the Lightning Address connection, compatible with Chivo, Blink Wallet and Strike. Enter your Lightning Address (nom@domaine.com format), for example from LN Markets, Alby, or any other compatible supplier.


![Saisie de la Lightning Address](assets/fr/13.webp)


Once you've logged in, your account is operational. You can now access the POS or return to the dashboard to configure other settings.


![Connexion réussie](assets/fr/14.webp)


*payment Links** *Payment Links


The "Payment Tools" menu gives access to "Payment Request", which lets you create and manage payment links. This feature is useful for generating personalized payment links to be sent by email or message: donations, single payments, multiple payments, or even paywalls to protect content. You can create different types of links to suit your business needs.


![Liens de paiement](assets/fr/15.webp)


**Sales terminal configuration**


To accept in-store payments, access the "Sales Terminal" menu from "Payment Tools". This section allows you to create and manage your POS terminals (the number of terminals depends on your plan, see Freemium vs. Business plans below). Click on "Open" to open the POS interface in your browser.


![Gestion des terminaux](assets/fr/16.webp)



**Generating a sale**


The POS terminal displays a numeric keypad for entering the sale amount. Enter the amount in your local currency (e.g. 500 sats corresponds to 630.74 ARS), then press "OK" to confirm.


![Saisie du montant](assets/fr/17.webp)


The application instantly generates a Lightning QR code and a Lightning Address for payment. Customers can scan the QR code with their wallet or use their Bolt Card on an NFC terminal.


![QR code de paiement](assets/fr/18.webp)


As soon as payment is received, a confirmation screen appears, showing the amount received in local currency and satoshis. You can send a receipt by email, print the ticket, or start a new sale immediately.


![Paiement encaissé](assets/fr/19.webp)


**Monitoring and management**


All transactions are recorded in your Merchant Dashboard. You have complete tracking of revenues by period, total number of sales, and detailed history for your accounting.


The Settings interface offers several configuration tabs. The "General Settings" tab lets you manage your merchant profile and notifications. The "Users" tab lets you add and manage access to the Merchant Dashboard for your team (multi-user management according to your plan). The "Development Workspace" tab gives access to API keys for advanced integrations, while "Subscription" lets you manage your subscription.


![Paramètres du compte marchand](assets/fr/20.webp)


**Freemium vs Business plans


Tiankii offers two packages for the Merchant Dashboard. The **Freemium** plan (free) is suitable for start-ups with limitations: a single point of sale, a single user, monthly volume limited to 1,000 USD, and no access to e-commerce connectors. The **Business** plan (0.5% fee per transaction) offers unlimited terminals, unlimited users, unlimited volume, access to WooCommerce/Shopify/Cloudbeds plugins, and exclusive WhatsApp notifications.


![Comparaison plans Freemium et Business](assets/fr/21.webp)


## Benefits and constraints


### Highlights


**Self-custodial**: You keep your private keys and full control of your funds. No risk of account freezing or third-party platform bankruptcy.


**Simplicity**: Lightning Address as an email address, NFC payments with a simple tap, intuitive interface with no technical expertise required.


**Complete ecosystem**: Tools for all profiles (individuals, retailers, developers) with modular integrations to suit your needs.


**Professional compliance**: Secure cloud hosting, PCI-DSS compliance, Salvadorian regulatory compliance.


### Limitations


**Lightning constraints**: Requires permanent wallet connection, liquidity management for large volumes, risk of failure if recipient is offline. Tiankii mitigates these aspects with integrated LSPs.


**SaaS dependency**: If Tiankii is unavailable, invoice generation is temporarily impossible (your funds remain secure).


**Privacy**: Tiankii can observe transaction metadata (amounts, dates). Less private than a self-hosted solution such as BTCPay Server.


## Conclusion


Tiankii illustrates how a well-designed infrastructure can remove the technical barriers preventing the mass adoption of Bitcoin as an everyday currency. By combining the power of Lightning Network with a non-custodial approach and accessible tools, the ecosystem offers a balanced path between financial sovereignty and ease of use.


For merchants, Tiankii represents an opportunity to drastically reduce transaction costs while accessing a new customer base. For consumers, Lightning Address and NFC cards transform Bitcoin into a practical currency, without technical complexity.


Although widespread adoption of Bitcoin remains a challenge requiring education and time, infrastructures such as Tiankii demonstrate that the technical tools already exist. The mission of simplifying Bitcoin payments is no longer a distant vision, but a reality accessible to anyone willing to take the plunge.


## Resources


### Official documentation


- [Tiankii official website](https://tiankii.com)
- [Tiankii Help Center](https://help.tiankii.com)
- [IBI application](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Command Center](https://cc.ibi.me)


### Wallet connection guides


- [Connect LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)


### Community


- [Lightning Network Plus](https://lightningnetwork.plus) - Lightning educational resource
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salvadorian circular economy initiative Bitcoin


### Related tools


- [Blink Wallet](https://blink.sv) - Wallet Lightning compatible recommended
- [LNbits](https://lnbits.com) - Self-hosted wallet solution
- [Standard Bolt Card](https://github.com/boltcard) - Technical specifications for NFC cards