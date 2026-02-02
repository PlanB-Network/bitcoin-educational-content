---
name: Zeus Swap
description: Non-custodial exchange service between On-Chain and Lightning Network bitcoins
---

![cover](assets/cover.webp)


The Bitcoin ecosystem presents a duality: the main network (On-Chain) offers maximum security, while Lightning Network enables instant transactions. This two-layer architecture creates a practical challenge: how can funds be transferred efficiently between these two layers without centralized intermediaries?


The problem is concrete: you receive a Lightning payment but want to keep it in Cold storage, or conversely, you have On-Chain bitcoins but need Lightning liquidity. Traditional solutions involve the manual opening/closing of Lightning channels (costly and technical) or centralized platforms requiring KYC.


Zeus Swap solves this problem with an automated, non-custodial exchange service. Developed by Zeus LSP, it allows you to convert On-Chain bitcoins into Lightning satoshis bidirectionally, without entrusting your funds to an intermediary. The process uses atomic contracts (HTLC) guaranteeing that the exchange will either complete or cancel.


The innovation lies in its simplicity: just a few clicks for an exchange that preserves your financial sovereignty, with no registration or KYC required.


## What is Zeus Swap?


Zeus Swap is a liquidity exchange service developed by Zeus LSP that enables atomic swaps between the main Bitcoin network and Lightning Network. It is a technical infrastructure that uses submarine swaps and reverse swaps to facilitate two-way conversion between On-Chain BTC and Lightning satoshis, while preserving the non-custodial nature of the operation.


### Technical architecture


Zeus Swap uses Boltz's open-source Bitcoin/Lightning atomic swap technology. The protocol uses Hash Time Locked Contracts (HTLC): contracts locking funds with two release conditions (revelation of a cryptographic secret or time expiration).


For a submarine swap (On-Chain → Lightning), the user sends bitcoins to an address incorporating the Hash of a Lightning invoice. Zeus LSP unlocks these funds only by paying the corresponding invoice, revealing the pre-image which automatically unlocks the bitcoins. This mechanism guarantees atomicity.


For a reverse swap (Lightning → On-Chain), the user pays a Lightning invoice from Zeus LSP, revealing a pre-image enabling the release of a prepared Bitcoin transaction to the destination address.


For more details on how the Lightning Network works, take a look at our dedicated course :


https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Business model


Zeus LSP acts as market maker, maintaining On-Chain and Lightning liquidity to honor swaps. For swaps, Zeus applies a variable fee (typically 0.1% to 0.5% depending on direction and conditions) plus Bitcoin's mining fee, transparently displayed prior to validation.


As a Lightning Service Provider, Zeus optimizes costs thanks to its expertise in on-demand channel opening, efficient routing and customized liquidity solutions.


### Integration


Zeus Wallet natively integrates the service, enabling swaps without leaving Interface Bitcoin/Lightning. This eliminates the friction of copying and pasting between applications.


The independent Interface web remains accessible to all wallets, guaranteeing maximum flexibility of use.


## Main features


### Bidirectional swaps


Zeus Swap offers two types of exchange:


**Submarine swaps (On-Chain → Lightning)**: inject Lightning liquidity from your Bitcoin reserves, useful for feeding a mobile Wallet or Lightning node without manually opening channels.


**Reverse swaps (Lightning → On-Chain)**: convert Lightning satoshis into On-Chain bitcoins for long-term storage, avoiding costly channel closures.


### User interfaces


**Interface web** (swaps.zeuslsp.com): simplified experience without registration, guided process with real-time display of fees and status.


**Zeus Wallet integration**: direct swaps from the application, automatic management of invoices and addresses, eliminating handling errors.


### Safety and recovery


Each swap generates a unique contract with immutable parameters: Hash Lightning, timeout, refund address. In the event of failure, automatic recovery via the address provided, independently of Zeus LSP.


**Zeus Swaps Rescue Key**: during a On-Chain → Lightning swap, Zeus automatically generates a universal recovery key replacing the old individual refund files. This unique key works on any device and for all swaps created with it. It is crucial to download and save this key in a secure location to be able to recover your funds in the event of a swap failure.


### Network optimization


Zeus Swap automatically adjusts expiry times and mining fees according to network conditions. Zeus users benefit from advanced options: choice of LSP, customized delays, compatibility with other services (Boltz).


## Installation and use


### Access methods


**Interface web** (swaps.zeuslsp.com): universal solution compatible with all wallets, no installation required, ideal for occasional use.


**Zeus app** (iOS/Android): integrated experience combining Wallet and swaps, suitable for regular users.


See our Zeus tutorial to learn more about this complete Wallet :


https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Web configuration


**On-Chain → Lightning**: The process begins by configuring the swap on the Interface web Zeus Swap. The user can use the arrow between the On-Chain and Lightning fields to reverse the direction of the swap.


![Interface de création de swap](assets/fr/01.webp)


*Interface Zeus Swap: amount selection (Sats 50,000 → Sats 49,648 after fees) with transparent display of network fees (Sats 302) and Zeus service (Sats 50).*


During the process, Zeus offers you to download the universal recovery key :


![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)


*Download dialog for the Zeus Swaps Rescue Key - a universal key that replaces the old individual reimbursement files*


If you already have a key, Zeus allows you to check it:


![Vérification de la clé existante](assets/fr/03.webp)


*Interface to check the validity of an existing Zeus Swaps Rescue Key*


Once configured, Zeus generates the Bitcoin depot address and displays the instructions :


![Adresse de dépôt et instructions](assets/fr/04.webp)


*Swap completion page: QR code and Bitcoin address for sending 50,000 Satss, with reminder of 24-hour expiry date*


The swap then waits for Bitcoin confirmation:


![Attente de confirmation](assets/fr/05.webp)


*Status "Transaction in Mempool" - waiting for Bitcoin confirmation to finalize the swap*


Once confirmed, the swap is completed automatically:


![Swap réussi](assets/fr/06.webp)


*Confirmation of success: 49,648 Sats received on Lightning after deduction of network and service charges*


### Using the Zeus App


**Lightning → On-Chain**: The Zeus application offers an integrated experience for reverse swaps (Lightning to Bitcoin).


![Navigation vers les swaps dans Zeus](assets/fr/07.webp)


*Zeus main screen showing Lightning (69,851 Sats) and On-Chain (38,018 Sats) balances, access to swaps via the side menu*


![Configuration du swap reverse](assets/fr/08.webp)


*Interface reverse swap creation: 50,000 Sats Lightning → 49,220 Sats On-Chain, with network charges (530 Sats) and service (250 Sats) clearly displayed. Users can either manually enter a Bitcoin receiving address, or generate one automatically from the Wallet Zeus via the "generate On-Chain Address" button.*


![Finalisation du swap mobile](assets/fr/09.webp)


*Finalization screens: Lightning invoice payment screen with "PAY THIS Invoice", confirmation of successful Lightning payment in 9.96 seconds, and balance statement with the 49,162 Sats awaiting confirmation*


### Surveillance and security


Each swap has a unique identifier with real-time tracking. Full progress display, automatic alerts for expiry dates. Automatic charge recommendations according to network conditions.


## Advantages and limitations


### Benefits



- Simplicity**: Swap in a few clicks vs. manual channel manipulation
- Non-custodial**: no KYC, no account, funds never entrusted to a third party
- Transparency**: fees explicitly displayed before validation (0.1% to 0.5% + minage depending on user tests - check current fees at each swap)
- Mobile integration**: native experience in Zeus Wallet


### Limitations



- Expiry times**: 24-48h maximum, failure if Bitcoin not confirmed in time
- Amount limits**: minimum 25,000 Sats, Zeus LSP liquidity variable according to conditions
- Traces On-Chain**: HTLC scripts potentially identifiable by Blockchain analysis
- Confirmation required**: minimum 10 minutes for Bitcoin validation


## Best practices


### Timing and costs



- Watch Mempool.space for times of low congestion
- Prefer weekends and off-peak hours to reduce mining costs
- Calculate profitability: small amounts vs. direct channel opening


### Security



- Check Bitcoin addresses carefully (copy-paste recommended)
- Back up the Zeus Swaps Rescue Key**: download and store the recovery key in a safe place
- Document: contract ID, refund address, expiry date
- Use appropriate mining fees for timely confirmation


### Usage strategy



- Balance On-Chain/Lightning liquidity to suit your needs
- Zeus Swap for one-off adjustments, direct channels for permanent needs


## Comparison with other swap services


### Zeus Swap vs Boltz Exchange


Zeus Swap uses Boltz's backend technology, but makes some crucial improvements:


**Zeus Swap benefits** :


- Interface unified**: native integration in Zeus Wallet vs Interface web technique Boltz
- WebSocket API**: real-time updates vs. manual polling
- Automated management**: automatic billing and address management
- Mobile support**: smartphone vs. desktop optimization only
- Swagger documentation**: complete REST API for developers


**Boltz remains advantageous** for total independence and use with any Bitcoin/Lightning setup.


Zeus Swap transforms proven Boltz technology into a mainstream user experience, comparable to the difference between a raw protocol and a user-friendly application.


### Zeus Swap vs Phoenix/Breez (integrated swaps)


Phoenix and Breez integrate transparent swap functionalities that hide the technical complexity from the end user. Phoenix uses an automatic swap-in/swap-out system where the user does not explicitly distinguish between Bitcoin layers: he "sends to a Bitcoin address" and the application handles the swap in the background.


This ultra-simplified approach is perfectly suited to beginners, but limits understanding and control of operations. Zeus Swap adopts a more educational philosophy: users understand that they are swapping between two distinct layers, gradually developing their understanding of the two-layer Bitcoin ecosystem.


## Detailed comparison of fees and limits (2024)


⚠️ **Warning**: Fees may vary over time depending on market conditions and service updates. Always check the fees displayed in the Interface before validating a swap.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Minimum amount |
| ------------- | ----------------------- | --------------------- | --------------- |
| **Zeus Swap** | ~0.1% + mining fees | 0.5% + mining fees | 25,000 sats |
| **Boltz** | 0.2% + mining fees | 0.5% + mining fees | 50,000 sats |
| **Phoenix** | Mining fees only | 0.4% fixed | 10,000 sats |
| **Breez** | 0.25% + network fees | 0.5% + mining fees | 50,000 sats |

Zeus Swap offers a balance between ease of use and technical control: more accessible than Boltz, more flexible than Phoenix/Breez, with a strict non-custodial approach.


## Conclusion


Zeus Swap represents a significant innovation in the Bitcoin ecosystem, elegantly resolving the challenge of interoperability between the main network and Lightning Network. By combining the cryptographic robustness of atomic swaps with an accessible user experience, this service democratizes Bitcoin dual-layer management without compromising the principles of financial sovereignty.


Zeus Swap's non-custodial architecture, inherited from proven Boltz technology, ensures that your funds remain under your exclusive control throughout the swap process. This approach respects the spirit of Bitcoin while offering the user convenience required for mainstream adoption. Pricing transparency and the absence of KYC processes reinforce this unique value proposition.


For the modern Bitcoin user, Zeus Swap is a strategic tool for optimizing the distribution of liquidity according to needs: On-Chain secure storage for long-term savings, Lightning availability for daily spending and microtransactions. This flexibility transforms Bitcoin management from a technical constraint into a competitive advantage.


The future evolution of Zeus Swap, supported by the experienced Zeus LSP team and the Boltz open-source community, promises continued improvements in terms of costs, processing times and user experience. This service is part of the wider trend towards maturation of the Bitcoin infrastructure, where technical sophistication becomes transparent to the end-user.


## Resources


### Official documentation


- [Zeus Swap - Web portal](https://swaps.zeuslsp.com)
- [Zeus Wallet - Mobile application](https://zeusln.app)
- [Blog Zeus - Announcements and tutorials](https://blog.zeusln.com)
- [Zeus technical documentation](https://docs.zeusln.app)


### Community and support


- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)