---
name: BitBanana
description: Mobile manager for your Lightning node
---

![cover](assets/cover.webp)


In this tutorial, you'll learn how to install and configure BitBanana on Android to control your Lightning node from your smartphone. We'll see how to connect the app to your existing infrastructure (Umbrel, RaspiBlitz, myNode, or any LND/Core Lightning node), make Lightning payments, manage your channels remotely, view your routing revenue, and back up your configurations. You'll also learn about the best security practices for protecting access to your node, and how it compares with Zeus, a popular alternative.


## Introducing BitBanana


BitBanana is an open source Android mobile application that turns your smartphone into a complete dashboard for remote control of your Lightning node. Unlike Lightning wallets, which embed a local node on the phone, BitBanana adopts a 100% remote control philosophy: the app holds no satoshi and connects only to your existing infrastructure.


Developed by Michael Wünsch under MIT license, the application guarantees total transparency with zero collection of personal data and verified reproducible builds. BitBanana natively supports LND and Core Lightning via standard URIs (`lndconnect://` and `clngrpc://`), drastically simplifying initial configuration. The application also recognizes LndHub and Nostr Wallet Connect for users without a personal node, although these modes operate custodially with limited functionality.


The interface offers full access to all your node's critical functions: sending and receiving payments (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), Lightning channel management (opening, closing, fee adjustment, rebalancing), advanced coin control, and watchtower management. BitBanana also implements several robust security layers: biometric locking, stealth mode, Emergency PIN, and native Tor support to anonymize connections.


## Supported platforms and installation


### Installation


BitBanana is exclusively available for Android 8.0 or higher. The application does not exist on iOS, and no version is planned. This limitation is explained by the project's history: BitBanana is the direct successor to Zap Android, originally developed by Michael Wünsch, who decided to continue his work under his own brand. Zap was a family of separate applications (Zap Android, Zap iOS, Zap Desktop) developed by different contributors with separate code bases. BitBanana is pursuing only the Android branch.


In addition, the iOS ecosystem presents significant regulatory and technical constraints for non-custodial Lightning applications. In 2023, Apple rejected a Zeus update for "license violations", and in 2024, Phoenix Wallet left the US App Store in the face of regulatory uncertainties regarding Lightning service providers. These obstacles explain why many Lightning developers prefer Android, which offers a more open policy for non-custodial applications.


Three installation methods are available for Android: Google Play Store (5000+ installations, automatic updates), F-Droid (reproducible builds, source code verification), or manual APK from GitHub.


![BitBanana](assets/fr/01.webp)


The official bitbanana.app website (left) boasts "100% Self-Custodial with ZERO data collection". The central screen shows the three download options: F-Droid (recommended), Google Play, and APK. The screen on the right shows the notifications permission for payment alerts.


The application requests permissions: network (node connection), camera (QR codes), NFC (LNURL), background services (notifications), biometrics (security), and WireGuard VPN. No trackers, zero data collection. Enable password or biometric locking to secure access.


## Initial configuration


### Connecting to a LND node


To connect BitBanana to your LND node (Umbrel, RaspiBlitz, myNode), obtain a `lndconnect` URI or QR code containing the address, TLS certificate and authentication macaroon.


For this tutorial, we're using a LND node via umbrel. For more details, please see our dedicated tutorial :


https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)


On the Lightning Node application, access the menu on the top right and select "Connect wallet".


![BitBanana](assets/fr/04.webp)


Select **gRPC (Tor)** to connect via Tor (recommended). The QR code and details (Host .onion, Port 10009, Macaroon) are displayed.


![BitBanana](assets/fr/02.webp)


In BitBanana, press "CONNECT NODE", scan the QR code or paste the URI. Authorize camera access, then check the .onion address displayed before confirming.


**Core Lightning** connection


If you use Core Lightning (CLN) instead of LND, the process remains identical, with the URI `clngrpc://` containing the mutual TLS certificates. Core Lightning natively supports BOLT12 (offers), enabling reusable invoices and recurring payments not available on LND.


**Connection without personal node (LNbits/hosted)**


If you don't have a Lightning node, BitBanana can connect to hosted services via LndHub (the protocol used by BlueWallet and LNbits) or Nostr Wallet Connect (NWC). Please note: these modes operate in custodial mode (the service hosts your funds) with limited functionality. You won't be able to manage channels or configure routing fees, and will only be able to send and receive Lightning payments.


For more details on LNbits or Nostr Wallet Connect, please consult our various tutorials:


https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Daily use


### Interface main


The home screen displays your Lightning balance, with the menu at top left giving access to the following sections: Channels, Routing, Sign/Verify, Nodes, Contacts, Settings, Backup. The clock icon (top right) opens the transaction history. The "Send" and "Receive" buttons at the bottom allow you to send and receive your satoshis.


![BitBanana](assets/fr/05.webp)


### Lightning and on-chain payments


![BitBanana](assets/fr/10.webp)


**Send a payment:** Press the "Send" button from the home screen. The payment screen (left) offers you to paste an address or payment data into the "Address or payment data" field, with a QR scanner at top right for scanning codes. You can also select a contact saved in the Contacts section to avoid having to scan each time.


BitBanana intelligently recognizes all payment formats: classic Lightning invoices (character strings starting with `lnbc`), Lightning Address (email format such as `utilisateur@domaine.com`), LNURL-pay codes for dynamic payments, LNURL-withdraw for withdrawing funds, and even Keysend payments directly to a Lightning public key without a prior invoice. The application automatically performs the necessary LNURL resolutions in the background.


Once the invoice has been loaded, BitBanana displays full details: exact amount, estimated routing fees, payment description (if provided by the recipient), and invoice expiry date. After confirmation, the payment is routed via your Lightning channels. You can then view the route taken hop by hop and the charges actually paid in the transaction details.


**Receive payment:** Press the "Receive" button. A selector (right screen) lets you choose between Lightning (instant payment via your channels) and On-Chain. For a Lightning receipt, enter the desired amount in satoshis (or leave at 0 to create an invoice with no fixed amount for the payer to complete), and add an optional description to appear on the invoice. BitBanana instantly generates a Lightning invoice with QR code for scanning. You can also copy the invoice as text and send it by e-mail. As soon as payment is received, a push notification alerts you and the transaction appears immediately in the history with all its details.


### Channels and routing


![BitBanana](assets/fr/06.webp)


The "Channels" section displays your send/receive capabilities and lists your channels with unique avatars. Each channel shows its liquidity split between local and remote balance. Touch a channel for full details and actions (closing, changing routing fees). The three dots at top right give access to the "Rebalance" option to rebalance your channels' liquidity. The "+" button opens a new channel.


The Routing section (central screen) displays forwarding revenues by period (1D, 1W, 1M, 3M, 6M, 1Y) with detailed forwards history to optimize your strategy.


Sign/Verify (right screen) allows you to cryptographically sign/verify messages to prove node control.


### Multi-nodes and parameters


![BitBanana](assets/fr/07.webp)


**Manage Nodes**: lists your nodes, with buttons to add manually, scan QR, or toggle between nodes. In particular, you can set up different types of connection to the same node: LAN, VPN or Tor.


**Manage Contacts**: stores your Lightning contacts for quick payments.


**Settings**: customize currency, language, avatars. Security & Privacy section: App Lock (PIN/biometrics), Hide balance (stealth mode), Tor (IP anonymization). Configuration of price oracles, block explorers, custom fee estimators.


## Advantages and limitations


**Highlights:**


- Total mobility: control your Lightning node from anywhere
- Full functionality: payments (LNURL, Lightning Address, BOLT 12), channel management, coin control, watchtowers, multi-nodes
- Security: PIN/biometrics, stealth mode, Emergency PIN, native Tor, screenshot blocking
- Free, open source (MIT), zero commissions, zero data collection


**Limitations:**


- Requires an active Lightning node (or LNbits in custodial mode)
- No iOS version planned
- Securing access to the phone is critical (macaroon admin = total access to the node)


## Best practices


**Safety:**


- Activate PIN/biometrics lock (prevents unauthorized access to node)
- Set up an Emergency PIN (deletes sensitive data in the event of duress)
- Never share your login URI or macaroon
- Stealth mode in hostile environments


**Login:**


- VPN mesh (Tailscale, ZeroTier): best compromise between speed and security
- Tor: maximum confidentiality, higher latency
- Clearnet: avoid unless necessary (IP exposure, open ports)


### Backup and restoration


Finally, there's the "Backup" menu, which lets you save your configurations for telephone migration or reinstallation.


![BitBanana](assets/fr/08.webp)


**Important:** The backup does NOT contain seed or channel backups (to be done on the node). It contains: node configurations (addresses, certificates, macaroons), labels, contacts, parameters. Restore button allows you to import an existing backup. Confirmation required before saving.


![BitBanana](assets/fr/09.webp)


Enter an encryption password (right screen). The system opens the file selector (left screen) to save `BitBananaBackup_2025-XX-XX.dat`. Confirmation "Backup created".


**Security:** Store the backup encrypted (personal cloud, USB, NAS). Never share files or passwords. Test restoration regularly. The backup recovers connections, not funds.


## BitBanana vs Zeus: What's the difference?


If you're exploring mobile apps for managing a Lightning node, you're likely to come across Zeus, a popular alternative to BitBanana. Unlike BitBanana, which focuses exclusively on remote control of an existing node, Zeus takes a more comprehensive approach, offering two modes of operation: a Lightning node embedded directly in the application (embedded mode with integrated LND) and remote connection to an external node, just like BitBanana.


This dual functionality makes Zeus particularly attractive for beginners wishing to experiment with Lightning without any prior infrastructure. Embedded mode enables immediate start-up with a complete mobile node, while advanced users can switch to remote connection once their personal node has been configured. Zeus also supports LND and Core Lightning for remote connection, such as BitBanana.


Another major advantage of Zeus is its cross-platform availability (iOS and Android), whereas BitBanana remains exclusively Android-based. Zeus also incorporates Olympus LSP infrastructure to facilitate the receipt of Lightning payments via just-in-time channels, a Point of Sale system for merchants, and integrated swap functionality to manage liquidity.


However, BitBanana retains its specific strengths: a simpler, more streamlined interface, a better user experience (UX) thanks to its exclusive focus on remote control, and an educational approach with contextual explanations. Zeus offers more functionality, but at the cost of a more complex interface. The application remains particularly suited to users wishing to control a node exclusively from a distance, without custodial functions.


To find out more about Zeus, take a look at the following tutorials:


https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Conclusion


BitBanana turns your Android smartphone into a complete Lightning dashboard, offering unprecedented mobility for node operators. The application covers all functionalities: payments (all formats), channel management, coin control, watchtowers, multi-node, with enhanced security (PIN/biometrics, Tor, Emergency PIN).


Entirely sovereign, BitBanana collects no data and compromises neither the confidentiality nor the control of your funds. Open source code (MIT) guarantees transparency.


## Resources


### Official documentation


- [BitBanana website](https://bitbanana.app)
- [Complete documentation](https://docs.bitbanana.app)
- [GitHub source code](https://github.com/michaelWuensch/BitBanana)


### Installation


- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)