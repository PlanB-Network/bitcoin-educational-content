---
name: LN Markets
description: Bitcoin trading platform on Lightning Network
---

![cover](assets/cover.webp)


LN Markets is the first truly Lightning-native Bitcoin trading platform, allowing you to trade leveraged Bitcoin derivatives directly from your wallet Lightning, with no KYC, instant settlements and minimal custody. Launched in 2020, it eliminates the frictions of traditional exchanges: no identity verification, no blocked deposits, no waiting for blockchain confirmations. Your wallet Lightning becomes your trading account.


## What is LN Markets?


LN Markets offers **Futures** (perpetual contracts with leverage up to 100×) and **Options** (Call/Put with risk limited to the premium paid). The platform functions as a liquidity aggregation layer consolidating multiple trading venues for optimal zero-slippage execution. Your funds are only locked in for the exact duration of your active positions, not days or weeks as with a traditional custodial account.


### Trading products available


**Futures (Perpetual Contracts)**


Perpetual contracts are futures with no expiry date, enabling you to speculate on the Bitcoin price trend with leverage. LN Markets offers two margin management modes:


**Isolated mode**: Each position has its own dedicated margin. Only the funds allocated to this specific position are at risk. If the position reaches the liquidation price, **only this position is liquidated**, your other positions and remaining balance are not affected. Ideal for strictly limiting risk per trade.


**Cross Mode (Cross Margin)** : Margin is shared between all your open positions. Your total account balance serves as collateral for all your positions. If a position goes bad, the system draws on your entire available balance to avoid liquidation. **Risk**: if your total balance runs out, all your positions may be liquidated simultaneously. Recommended only for experienced traders seeking to maximize capital efficiency.


**Position management** :



- Long position**: you bet on the rise of BTC/USD. If the price rises, you win; if it falls, you lose. **Example**: Bitcoin at $100,000, you open a Long with 10,000 sats and 10× leverage. If Bitcoin rises to $105,000 (+5%), your position gains 50% (5% × 10), i.e. ~5,000 sats profit. If Bitcoin falls to $95,000 (-5%), you lose 50%, i.e. a loss of ~5,000 sats.



- Short position**: you bet on BTC/USD falling. If the price goes down, you win; if it goes up, you lose. **Example**: Bitcoin at $100,000, you open a short with 10,000 sats and 10× leverage. If Bitcoin falls to $95,000 (-5%), you win 50%, i.e. ~5,000 sats. If Bitcoin rises to $105,000 (+5%), you lose 50%.


Leverage (up to 100×) amplifies gains and losses proportionally. A **funding rate** mechanism (periodic charges every 8 hours) balances long and short positions. You can manage up to 100 futures positions simultaneously.


**Options**


An option is like a **lottery ticket with expiry date**. You pay a premium to bet on the direction of the Bitcoin price. **Major advantage**: you can never lose more than the premium paid, no liquidation possible.



- Call Option (bullish bet)**: You bet that Bitcoin will rise above the strike before expiration. You win if the price rises, loss limited to the premium if the price falls.



- Put Option (bearish bet)**: You bet that Bitcoin will fall below the strike. You win if the price falls, loss limited to the premium if the price rises.



- Straddle (volatility bet)**: You buy a Call AND a Put simultaneously. You win if Bitcoin makes a big move in any direction, you lose both premiums if the price remains stable.


Limit: 50 simultaneous positions. Ideal for beginning leveraged trading without fear of liquidation.


**sats ↔ sUSD**: Instantly convert your satoshis into synthetic dollars (sUSD) to protect yourself from volatility, or vice versa to regain Bitcoin exposure.


## Platform access and account creation


### Go to LN Markets


Go to [lnmarkets.com](https://lnmarkets.com) and click on "Open App".


![Page d'accueil LN Markets](assets/fr/01.webp)


### Create your account


The welcome screen offers several connection methods:


![Méthodes de connexion](assets/fr/02.webp)


**Options available** :

1. **Register with a Lightning wallet** (recommended) : LNURL-auth with Phoenix, Breez, Zeus or BlueWallet

2. **Register with email**: classic account (limits Lightning experience)

3. **Alby** or **Ledger**: browser extensions


### Connection via Lightning (LNURL-auth)


Click on "Register with a Lightning wallet". Scan the QR code with your wallet Lightning :


![QR code LNURL-auth](assets/fr/03.webp)


Your wallet automatically signs a cryptographic request and your account is created instantly, without email or password. Strong security and total anonymity.


### Initial configuration


![Configuration post-connexion](assets/fr/04.webp)


**Available parameters** :


- Username**: personalize your username
- Automatic withdrawals**: activate automatic withdrawals to your wallet after trade closure
- Two-Factor Authentication**: enhanced security with 2FA
- Documentation**: access official resources


## Interface tour


The LN Markets interface is organized into several sections accessible from the side menu:


### Dashboard


![Dashboard](assets/fr/06.webp)


Displays your performance by product type (Futures Cross, Futures Isolated, Options) with P&L, traded volumes and your personal Address Lightning (e.g. `pivi@lnmarkets.com`).


### Profile


![Profil trader](assets/fr/07.webp)


Detailed statistics: number of trades, trader type (SCALPER, etc.), median position duration, Long/Short breakdown, win rate, averages (quantity, margin, leverage), and progressive fee structure according to volume.


### Trades


![Historique des trades](assets/fr/08.webp)


The Trades tab displays a complete history of your positions, with all important metrics: creation date, direction (Long/Short), position size (quantity), committed margin, entry and exit price, realized profit/loss (P&L) and trading fees. You can filter by product type (futures/options) and export your data for external analysis or accounting.


### Settings


![Paramètres de la plateforme](assets/fr/05.webp)


The Settings tab offers two tabs: **Account** and **Interface**.


**Account** tab:


Account management with editable fields :


- Username**: change your username (e.g. "pivi") with the "Update" button
- Email**: add/edit your email address
- Deposit bitcoin address**: the bitcoin address you can use to deposit on-chain funds.


**Three configuration toggles** :


- Appear in leaderboards**: choose whether or not to appear in public leaderboards
- Use Taproot addresses**: use Bitcoin addresses Taproot for on-chain deposits/withdrawals
- Enable automatic withdrawals**: activate automatic withdrawals to your wallet Lightning after trade closure


**Account migration**: Section allowing you to migrate your Lightning account to classic email/password authentication.


**Session management**: "Clear session and local data" button to disconnect and clean local browser data.


**Interface** tab:


Customize the user experience with seven toggles:


- Skip order confirmation**: deactivate confirmation modal before trade execution (fast trading)
- Show tooltips**: display tooltips when hovering over elements
- Private Mode (masks sensitive data)**: masks amounts and sensitive data in the interface (privacy mode)
- Show net PL in profile**: show net profit/loss in your public profile
- Use unit icons**: display icons for currency units (sats, $)
- Enable sound notifications**: activate sound notifications for trading events
- Enable desktop notifications**: activate operating system desktop notifications


### Wallet


![Wallet](assets/fr/09.webp)


Bitcoin and Synthetic USD balances with history of deposits, withdrawals, cross transfers, swaps, funding and on chain address management.


### API


![API V3](assets/fr/10.webp)


LN Markets offers a complete API REST (V2 and V3) to fully automate your trading via scripts or bots. You can create API keys with customizable permissions (read-only, trading, withdrawals) directly from the interface. Official TypeScript and Python SDKs are available for easy integration. Full API V3 documentation is available at [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).


## First deposit of funds


Click on "Deposit". Three methods are available:


![Modal de dépôt](assets/fr/11.webp)


1. **LNURL**: scan the QR code with your wallet Lightning

2. **Invoice**: enter an amount then scan the Lightning invoice

3. **On-Chain**: depot Bitcoin on chain


## Trading in practice


### Trade Futures Long: betting on the upside


From the Dashboard, click on "Futures" then "Isolated". Click on **"Buy "** to open a Long position.


![Interface Futures Long](assets/fr/12.webp)


Click on the **calculator** icon next to the "Buy" button to display the position calculator:


![Calculateur de position Long](assets/fr/13.webp)


**Concrete example** :


- Quantity**: $100 (position size)
- Trade Margin**: 12.336 sats (committed margin)
- Leverage**: 7.73× (each 1% BTC variation = 7.73% on your capital)
- Entry price** : $104,863.5
- Liquidation**: $92,852 (critical automatic liquidation price)
- Exit price**: $110,000 (for profit calculation)
- PL** : 4,492 sats (profit if exit at $110,000)


**Scenarios** :


- Increase +4.9%** ($110,000) : +4,492 sats profit (+36.4%)
- Neutral** ($104,863) : -185 sats (fees only)
- Down -11.5%** ($92,852): total liquidation (-100%)


Click on the "Buy" button to confirm the trade. **Two possible cases** :



- If you have enough liquidity** in your account: a confirmation modal is displayed directly (image below). Click on "Yes" to execute the trade instantly.


![Confirmation trade Long](assets/fr/14.webp)



- If you don't have enough cash**: a Lightning QR code is displayed instead. Scan it with your wallet Lightning to pay the required margin. The trade opens automatically on receipt of payment


### Trade Futures Short: betting on the downside


Click on **"Sell "** to open a Short position (you win if the price falls). Open the calculator with the calculator icon to set up your position:


![Calculateur de position Short](assets/fr/15.webp)


Click on "Sell" to confirm. As for the Long, **two possible cases**:



- If you have enough cash**: direct confirmation mode, click on "Yes"
- If you don't have enough cash**: a Lightning QR code is displayed (image below). Scan it with your wallet Lightning to pay the required margin:


![Paiement Lightning pour Short](assets/fr/16.webp)


Once the Lightning payment has been received, your Short position opens automatically. You can then manage it from the trading interface.


#### Closing a position


To close your position (Long or Short), click on the **small cross in the bottom right-hand corner** of the management interface:


![Interface de clôture](assets/fr/17.webp)


A confirmation dialog is displayed to confirm the trade closure:


![Confirmation clôture](assets/fr/18.webp)


The modal displays your current P&L (profit or loss). Click "Yes" to close. The balance is instantly added (profit) or deducted (loss) from your Wallet via Lightning.


### Trade Options Call: conditional right to buy


Options offer **risk limited** to the premium paid, with no liquidation possible. A Call gives you the right (not the obligation) to buy Bitcoin at the strike price before expiration. Unlike futures, you can never lose more than the premium invested.


From the Dashboard, click on "Options", then select the "Call" tab.


![Interface Options Call](assets/fr/19.webp)


Configure your trade with the following parameters:


- Quantity**: $100 (size of your contract)
- Expiry** : 2025-11-15 (expiration date)
- Strike**: $96,000 (target price)


The other fields are calculated automatically:


- Margin**: 1.045 sats (premium payable, your investment)
- Breakeven**: $96,923 (price to recover your stake)
- Delta**: 40 (Bitcoin price sensitivity)


**How to calculate your win?**


Your profit depends on the Bitcoin price at expiry. Formula: **(BTC price - Strike) × Contract size - Premium paid**.


**Concrete examples** :



- Bitcoin at $96,000** (current price) : Intrinsic value = $0. **Loss: -1.045 sats** (you lose the premium)



- Bitcoin at $97,000**: Intrinsic value = (97,000 - 96,000) × 0.00105 BTC = $1.05. Converted to sats ≈ 2,175 sats. **Profit: 2.175 - 1.045 = +1.130 sats** (+108% gain)



- Bitcoin at $98,000**: intrinsic value = $2,000 ≈ 3,224 sats. **Profit: +2,179 sats** (+208% gain)



- Bitcoin at $100,000**: intrinsic value = $4,000 ≈ 5,263 sats. **Profit: +4,218 sats** (+403% gain)



- Bitcoin under $96,000**: Option expires worthless. **Limited loss: -1,045 sats**, no liquidation possible


Click on "Buy Call". A confirmation dialog box appears:


![Confirmation Call option](assets/fr/20.webp)


Click "Buy Call" again to confirm. The option appears in "Running Options". On expiry, LN Markets automatically calculates the intrinsic value and adjusts your profit/loss.


**Note on Put Options** : The operation is identical to that of a call, but in reverse. With a Put, you bet on the Bitcoin price going **down**. If Bitcoin falls below your strike, you win; if it stays above, you lose only the premium paid. The calculation of gains follows the same logic: **(Strike - BTC price) × Contract size - Premium paid**.


### Lightning fund withdrawal


Click on "Withdraw":


![Modal de retrait](assets/fr/21.webp)


**Methods** : LNURL, Invoice, Lightning Address, On-Chain.


**Invoice procedure** :

1. Generate a Lightning invoice from your wallet

2. Copy the invoice (begins with `lnbc...`)

3. Paste it into the LN Markets field

4. Confirm withdrawal

5. Your wallet is credited in 1-3 seconds


No Lightning withdrawal fees, only minimal routing costs (<0.1% in practice).


## Risks and best practices


**Main risks** :


- Total liquidation**: high leverage can wipe out 100% of margin in minutes
- Experimental service**: alpha phase, technological uncertainties
- Counterparty risk**: platform remains single counterparty


**Best practices** :


1. **Capital management**: adopt a risk management strategy tailored to your profile. For example: allocate 5% of your total assets to leveraged trading, then risk a maximum of 1% of this capital per trade (e.g.: 1 BTC asset → 5M sats to trade → 50k sats max risk per position)


2. **Systematic stop-loss**: configure stop-losses to limit your losses per trade. With a 1% risk rule, for example, even 10 consecutive losing trades represent only 10% of your trading capital


3. **Start small**: test first with a few thousand satss to understand the mechanisms before applying your capital management strategy


4. **Regularly withdraw your profits**: secure your profits on your main wallet, leaving only active trading capital on the platform


5. **Watch out for leverage**: avoid leverage >20× unless you are fully aware of liquidation risks


**Costs**: no Lightning deposit/withdrawal fees, spread ~0.1% per trade (falling to 0.06% depending on volume).


## Advantages and limitations


**Advantages** :


- Non-custodial (total control excluding trading periods)
- KYC-free (anonymity via Lightning/Nostr)
- Instant settlements (deposits/withdrawals in seconds)
- Zero-slippage execution with liquidity aggregation
- API public and Nostr support


**Limitations** :


- Service alpha (possible evolutions)
- Lower liquidity than Binance/Deribit
- Forbidden to US residents


## Conclusion


LN Markets embodies a major evolution of Bitcoin trading by natively integrating Lightning Network to give control back to users. For savvy bitcoiners looking to speculate without compromising their sovereignty, it's a unique alternative to traditional centralized exchanges.


The platform continues to evolve with USDT linear futures and non-custodial trading via Discreet Log Contracts (DLC) under development. By applying good risk management practices (small amounts, stop-loss, regular withdrawals), LN Markets becomes a powerful tool for exploring Bitcoin leverage responsibly.


Start small, test with a few thousand satss, and gradually explore this new Lightning Network frontier. Happy sovereign trading ⚡️!


## Resources



- [LN Markets official website](https://lnmarkets.com)
- [Documentation](https://docs.lnmarkets.com)