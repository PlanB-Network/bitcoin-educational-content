---
name: SwapMarket
description: Bitcoin and Lightning swap services aggregator
---

![cover](assets/cover.webp)


Transferring funds between Bitcoin on-chain and Lightning Network generally requires either the manual opening of Lightning channels (technical and costly), or the use of centralized swap platforms with KYC. SwapMarket offers an alternative: trustless atomic swaps via competitive providers, without KYC.


Innovation: although providers are intermediaries, HTLC (*Hash Time Locked Contracts*) mathematically guarantee that your funds remain under your control. The aggregation of several providers (Boltz, ZEUS Swaps, Eldamar, Middle Way) creates price competition. Interface web open-source self-hostable.


## What is SwapMarket?


An open-source aggregator launched in 2024, SwapMarket functions as a comparator of Bitcoin/Lightning swap providers. The user instantly compares conditions (fees, liquidity, limits) and selects the optimal provider.


### Technical architecture


**Frontend client-side**: 100% client-side application (fork Boltz Web App) hosted on GitHub Pages. Code runs in browser without backend server. History stored locally (cookies/cache). Public and auditable source code.


**Provider discovery** : Hardcoded list in `src/configs/mainnet.ts`. New providers added via Pull Request or email.


**Independent backends**: Each provider operates its own Boltz backend. The interface queries the APIs in real time to compare quotes instantly.


**HTLC Atomic Swaps**: Hash Time Locked Contracts guarantee atomicity: either the swap executes, or each party recovers its funds. Counterparty risk mathematically eliminated.


### Philosophy


SwapMarket reduces centralization by creating competition between providers for fees and liquidity. No KYC, open-source self-hostable code, multiplication of independent operators to avoid single points of failure.


## Main features


### Provider Marketplace


The interface displays all active providers: name of provider, fees applied (percentage and/or fixed), minimum/maximum amounts available, and swap types supported. The application directly queries the APIs of each provider referenced in the configuration file to retrieve quotes in real time. Competition between providers guarantees optimal rates, generally around 0.5% for standard swaps.


### Bidirectional swaps


**Swap-in (on-chain → Lightning)**: Convert on-chain BTCs into Lightning satoshis. Use case: power a mobile wallet Lightning, obtain incoming capacity on a node, or have instant liquidity.


**Swap-out (Lightning → on-chain)**: Convert Lightning satoshis to on-chain BTC. Use case: empty a wallet Lightning to cold storage or rebalance liquidity between layers.


### Safety and recovery


**Trustless atomic swaps**: HTLCs guarantee that either the exchange is completed in full, or each party recovers its stake. Counterparty risk is mathematically eliminated.


**Repayment mechanism**: Each swap has a timelock. If the swap fails, the funds are automatically refundable after expiration. The user always retains the option of reclaiming his bitcoins.


**Recovery keys**: SwapMarket lets you export recovery keys for swaps in progress. In the event of a problem, these keys can be used to finalize or cancel a swap from any device.


## Installation and access


### Interface web


SwapMarket requires no installation. Access is via browser by visiting https://swapmarket.github.io. For maximum confidentiality, use Brave, Firefox with anti-tracking extensions, or LibreWolf. Tor Browser is recommended for network anonymity.


No registration, email or identity verification required.


### Self-hosting (optional)


For technical users wishing to eliminate any dependency on the official GitHub Pages domain, SwapMarket can be run locally :


**Via npm** :

```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```


**Via Docker** :

```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```


The application will be accessible at `http://localhost:3000`. Self-hosting guarantees total control over the interface, eliminates the risk of censorship of the official domain, and allows source code to be audited before execution.


### Initial configuration


**Wallet Lightning**: Make sure you have an operational wallet Lightning (Phoenix, Zeus, BlueWallet, etc.). For swap-ins, you will generate a Lightning invoice. For swap-outs, you will pay a Lightning invoice.


**Wallet on-chain**: For swap-ins, you'll need a wallet Bitcoin on-chain to send funds. For swap-outs, prepare a Bitcoin receiving address.


**Optional configuration**: SwapMarket stores swap history and preferences in browser cookies. No account creation required.


## Access to settings and Rescue Key


Before making your first swaps, we strongly recommend that you download your **Rescue Key**. This emergency key enables you to recover your funds in the event of a technical problem or loss of access to your device.


### Access parameters


From the SwapMarket main page, click on the gear icon (⚙️) at the top right of the interface, next to the swap form.


![Accès aux paramètres](assets/fr/01.webp)


### Page Settings


The Settings page opens, displaying several configuration options:



- Denomination**: Choice of BTC or sats
- Decimal Separator**: Decimal separator (, or .)
- Audio/Browser Notifications**: Audio and browser notifications
- Rescue Key** : Download the recovery key
- Logs**: View, download or delete logs


![Page Settings](assets/fr/02.webp)


### Download Rescue Key


Click on the **Download** button next to "Rescue Key".


**Important points** :


- The Rescue Key is a **one-stop emergency key** that works for all your future swaps
- Keep this key in a **secure and permanent** place (password manager, digital safe)
- In the event of a swap problem (timeout, technical failure), this key allows you to recover your funds


## Creating a swap step by step


### Swap-out: Lightning → Bitcoin


This first example shows how to convert Lightning satoshis into on-chain bitcoins.


**Step 1: Swap configuration


From the main page, select the swap form :


- LIGHTNING** (upper field): Enter the amount you wish to send in sats Lightning (example: 30,000 sats)
- BITCOIN** (lower field): The amount you will receive is automatically displayed after fees have been deducted (example: 29,320 sats)


In the bottom field, paste your **receiving Bitcoin address** where you wish to receive the funds. Check this address carefully.


The default provider is usually Boltz Exchange. Network fees and provider fees are clearly displayed.


![Configuration swap-out](assets/fr/03.webp)


**Step 2: Provider selection**


Click on the provider drop-down menu (default: "Boltz Exchange") to display all available liquidity providers.


A modal window opens, displaying a comparison table:


- Status**: Green indicator if the provider is active
- Alias**: Provider name (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Fee**: Charges applied by the provider (generally between 0.49% and 0.5%)
- Max Swap**: Maximum amount accepted for a swap


Compare fees and maximum amounts, then select the provider of your choice.


**Please note**: The provider selection interface does not display the **minimum amounts** for each provider. This information only appears in the swap creation interface, after a provider has been selected. Minimum and maximum amounts may vary from provider to provider, and may change over time. **Always check these limits at the time of your swap**: if the amount you wish to swap is outside the limits of a provider, you can select another more suitable for your transaction.


![Sélection du provider](assets/fr/04.webp)


**Step 3: Swap creation and Lightning** payment


Click on the yellow **"CREATE ATOMIC SWAP "** button. SwapMarket will generate a **Lightning invoice** (BOLT11) for you to pay from your wallet Lightning.


The page displays :


- Swap ID**: Unique swap identifier (example: J4ymFIMVR6Hm)
- Status**: "swap.created" (swap created, awaiting payment)
- QR code**: Scan it with your wallet Lightning
- Invoice Lightning**: Character string starting with "lnbc" (example: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)


Pay this invoice from your wallet Lightning (Phoenix, Zeus, BlueWallet, etc.). The exact amount to be paid is displayed (example: 30,000 sats).


![Paiement Lightning](assets/fr/05.webp)


**Step 4: Confirmation and acceptance**


Once the Lightning payment has been confirmed, SwapMarket instantly receives your payment and the provider broadcasts the Bitcoin transaction to your address.


The status changes to **"invoice.settled "** (invoice paid), and a confirmation message is displayed.


Your on-chain bitcoins will be available as soon as the transaction has been confirmed (usually a few minutes to a few hours, depending on the mining fees chosen by the provider).


![Confirmation swap-out](assets/fr/06.webp)


You can click on **"OPEN CLAIM TRANSACTION "** to view the Bitcoin transaction on a blockchain browser.


### Swap-in: Bitcoin → Lightning


This second example shows how to convert on-chain bitcoins into Lightning satoshis.


**Step 1: Swap configuration


From the main page, select the swap form :


- BITCOIN** (upper field): Enter the amount you wish to send in sats Bitcoin (example: 63,400 sats)
- LIGHTNING** (bottom field): The amount you will receive is automatically displayed after deduction of fees (example: 62 884 sats)


In the bottom field, paste a Lightning** invoice (BOLT11) generated from your wallet Lightning, or use your LNURL address if your wallet supports it.


![Configuration swap-in](assets/fr/07.webp)


**Step 2: Rescue Key check**


After clicking on **"CREATE ATOMIC SWAP "**, a modal window appears, asking you to verify your Rescue Key.


![Modal Rescue Key](assets/fr/08.webp)


**Boltz Rescue Key**: As you have already uploaded your recovery key during initial configuration (see previous section), click on the **"VERIFY EXISTING KEY "** button to import the key you have saved.


Select the previously downloaded Rescue Key file. After successful verification, the interface automatically switches to the next step.


**Step 3: Bitcoin** deposit address


SwapMarket now generates a **unique Bitcoin address** containing the HTLC contract linked to your Lightning invoice.


The page displays :


- Swap ID**: Unique identifier (example: 1kGmB6JyGqU4)
- Status**: "invoice.set" (invoice set, awaiting payment Bitcoin)
- QR code**: Bitcoin depot address
- Bitcoin** address: Usually begins with "bc1p..." (example: bc1p5mvtwxapjkds...9d4n9f)
- Warning in yellow** : "Make sure your transaction confirms within ~24 hours after creation of this swap!"


This period of ~24 hours is the **timeout** of the HTLC contract. If your Bitcoin transaction is not confirmed within this timeframe, the swap will fail and you will need to use your Rescue Key to recover your funds.


![Adresse de dépôt Bitcoin](assets/fr/09.webp)


You can copy the address by clicking on the **"ADDRESS "** button, or scan the QR code directly from your wallet on-chain.


**Step 4: Sending bitcoins**


From your wallet Bitcoin on-chain, send **exactly** the amount indicated (e.g. 63,400 sats) to the address generated.


**Important**: Use appropriate mining fees to guarantee fast confirmation. If the fee is too low and the transaction remains in mempool beyond the timeout (~24h), the swap will fail.


Once the transaction has been sent, SwapMarket detects that it is in the mempool and displays :


- Status** : "transaction.mempool
- Message**: "Transaction is in mempool - Waiting for confirmation to complete the swap"


![Transaction en mempool](assets/fr/10.webp)


**Step 5: Confirmation and Lightning** reception


As soon as the Bitcoin transaction receives its first confirmation, the provider automatically pays your Lightning invoice. You instantly receive the satoshis on your wallet Lightning.


The status changes to **"transaction.claim.pending "**, then a confirmation message is displayed:


![Confirmation swap-in](assets/fr/11.webp)


Your Lightning satoshis are immediately available in your wallet.


## Advantages and limitations


### Benefits


**Rate competition**: The aggregation of providers creates a natural competition pulling fees down (0.49% to 0.5%).


**Confidentiality**: No KYC, 100% client-side interface (no transmission of personal data), Tor Browser compatible.


**Non-custodial**: HTLC mathematically guarantee exclusive control of your funds. Either the swap succeeds, or you get your bitcoins back.


**Open-source self-hostable**: auditable public code, deployable locally for maximum resistance to censorship.


### Limitations


**Limited liquidity**: Limited number of active providers (Boltz, Eldamar, MiddleWay depending on period). Maximum amounts may be limited.


**Expiration time**: Timeout from 24h to 48h. If on-chain transaction is not confirmed before expiration, manual recovery required.


**Interface centralization**: Although self-hostable, the official interface is hosted on GitHub Pages. If GitHub censors the repo, access via swapmarket.github.io will be blocked (solution: self-hosting).


**on-chain Traces**: HTLC scripts are potentially identifiable by advanced blockchain analysis.


## Best practices


### Secure configuration


**Download your Rescue Key**: Before your first swaps, download your Rescue Key from Settings (see dedicated section above). This unique key will work for all your future swaps, enabling you to recover your funds in the event of a problem.


**Use Tor Browser**: For maximum confidentiality, access SwapMarket via Tor Browser to hide your IP address.


**Consider self-hosting**: For technical users, running your own SwapMarket instance eliminates dependency on the official GitHub Pages domain.


### Swap optimization


**Keep an eye on the mempool**: Check mempool.space before a swap-in. Choose times of low activity to minimize mining costs.


**Check addresses**: For swap-outs, meticulously check your receiving address. Use copy and paste and check the first 5 and last 5 characters.


**Test with small amounts**: Start with the minimum allowed (25,000 to 50,000 sats). Increase gradually once you've mastered the process.


**Document your swaps**: Make a note of each swap's ID, redemption address and expiry date. This information facilitates tracking and recovery in the event of a technical problem.


### Usage strategy


**Balance your cash flow**: Use SwapMarket to adjust your allocation between on-chain (savings, long-term security) and Lightning (daily expenses, instant payments) according to your real needs.


**Calculate profitability**: For permanent Lightning liquidity needs, compare the cumulative cost of repeated swaps versus opening a Lightning channel directly. SwapMarket excels for one-off adjustments, not necessarily for large regular flows.


## SwapMarket vs Boltz: What's the difference?


### Boltz: Technology vs. Service


**Boltz is the open-source technology** (`boltz-backend` on GitHub) that implements atomic swaps via HTLC between Bitcoin, Lightning and Liquid.


**Critical point**: All SwapMarket providers (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) deploy their own instance of the Boltz backend. The underlying technology is therefore identical. A vulnerability in the Boltz backend would potentially affect all providers, but the open-source nature of the system allows community auditing.


**Boltz Exchange** is a single service operated by the Boltz team, while **SwapMarket** brings together several providers all using Boltz technology, creating a competitive pricing environment.


See our Boltz and Zeus Swap tutorials for more details:


https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Key differences


| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarket benefits**: Price competition, diversification of backend instances, real-time comparison.


**Technological alternatives** (not SwapMarket compatible): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. These solutions use their own implementations of submarine swaps.


**Recommendation**: Use Boltz Exchange for simplicity or SwapMarket to optimize costs through competition. Both are equivalent in safety (HTLC non-custodial).


## Conclusion


SwapMarket facilitates Bitcoin/Lightning exchanges by aggregating multiple providers into a single interface. The HTLC architecture guarantees the non-custodial nature of swaps, the absence of KYC preserves confidentiality, and the self-hostable open-source code reinforces resistance to censorship.


Competition between providers improves rates and multiplies sources of liquidity. To optimize two-layer management (on-chain savings, Lightning expenses), SwapMarket is a practical tool that preserves financial sovereignty and confidentiality.


## Resources


### Official documentation


- [SwapMarket - Web application](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Technical documentation](https://docs.boltz.exchange/)
- [Guide self-hosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)


### Related projects


- [Boltz Exchange](https://boltz.exchange) - Original atomic swap service
- [ZEUS Swaps](https://zeusln.com) - Lightning swaps provider