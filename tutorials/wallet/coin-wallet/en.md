---
name: Coin Wallet
description: Tutorial about Coin Wallet and ways to enhance privacy and security
---

![cover](assets/cover.webp)

This tutorial covers [Coin Wallet](https://coin.space/) - a self-custodial crypto wallet for mobile devices, and how to increase security and privacy when using mobile wallet apps.


## About Coin Wallet

**Coin Wallet** is a self-custodial / non-custodial, open-source wallet created by a team of Bitcoin enthusiasts in 2015. It started as a web application, followed by the iOS app in 2017, and the Android app in 2020 - available on Google Play, Samsung Galaxy Store, and Huawei AppGallery.

Key advantages:
- Non-custodial architecture  
- Fully [open-source code](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)  
- Simple and clean design  
- Focused on the core purpose - securely storing cryptocurrency, without unnecessary features  
- Cross-platform support: mobile (iOS & Android), desktop, web
- RBF (Replace-By-Fee) support - speed up stuck transactions anytime
- Hardware 2FA with [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2 key
- Built-in Tor support – route all traffic through the Tor network for maximum privacy


## 1️⃣ Installing Coin Wallet
Coin Wallet is available on all major platforms.

- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)

- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)

- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)

- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)

- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)

- [Android APK](https://coin.space/api/v3/download/android-apk/any)

- [All release links](https://github.com/CoinSpace/CoinSpace/releases)

Also available for desktop (Windows, Linux, macOS), as a web app and via Tor.

![image](assets/en/01.webp)

## 2️⃣ Creating a Wallet and Setting the PIN

A wallet is created using a passphrase – a random sequence of 12 words separated by spaces, generated from a [list of 2048 words](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).  
Coin Wallet supports 12, 15, 18, 21, or 24-word passphrases imported from other wallets.

The passphrase is the human-readable form of the master private key. It must be saved securely. The passphrase is all that is needed to access or restore the wallet. If the passphrase is lost, the wallet and all funds are permanently lost. The passphrase must never be shared. Coin Wallet does not store keys on any server or database.

**Is a 12-word passphrase secure?**  
With 2048 possible words per position, there are 2048¹² ≈ 10³⁹ combinations — providing ~128 bits of security, comparable to Bitcoin private keys. This level is widely considered sufficient.

![image](assets/en/02.webp)

After the passphrase is written down and confirmed, the app asks to set a **4-digit PIN** for everyday access. For added convenience, you can enable biometric authentication (fingerprint or face recognition) instead of using a PIN.

![image](assets/en/03.webp)


There is no account, no key recovery, no passphrase reset, and no transaction reversal. Security is the user’s full responsibility.

For detailed best practices on saving the mnemonic phrase:  

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Passphrase + PIN. When and How They Are Used

**When is the passphrase required?**  
Only in these rare cases:
- Setting up the wallet on a new device  
- Reinstalling the Coin Wallet app  
- Clearing the app/browser data (Local Storage)  
- Removing a hardware key from the account  
- Entering the wrong PIN three times (the app locks for security)

In everyday use, the 4-digit PIN is sufficient to unlock the wallet.

**Passphrase + PIN: How It Works**  
The passphrase is the true master private key and works on any device.  
Since typing 12–24 words every time would be inconvenient, Coin Wallet uses a 4-digit PIN for fast, everyday access on the current device.  
A simple PIN alone is not secure enough to protect the master key directly, so it is never used for encryption. Instead:

- The PIN is sent to the server and exchanged for a long cryptographic token.  
- This token decrypts the encrypted master key stored only on the device.

If the PIN is entered incorrectly three times, the server permanently deletes the token. The locally stored key becomes unusable, and the only way to recover the wallet is by entering the original passphrase.  
This design gives both convenience and strong fallback protection.


## 4️⃣ Receiving ₿itcoin - Address Types and Privacy

Coin Wallet supports all three Bitcoin address formats:

- **Native SegWit (Bech32)** – starts with **bc1q** – lowest fees, recommended
- **Nested SegWit (P2SH)** – starts with **3**  
- **Legacy (P2PKH)** – starts with **1**  

![image](assets/en/04.webp)

**Why does the address change after each deposit?**  
This is intentional and protects privacy. Every time coins are received, Coin Wallet automatically generates a new unused address. If the same address were reused (for example, for monthly salary), anyone could easily sum up all incoming transactions on a blockchain explorer and know the total income.

Old addresses remain valid forever – you can still receive to them – but using a fresh address each time is the recommended privacy best practice.

**How to receive Bitcoin:**
1. Open the coin  
2. Tap **Receive**  
3. Choose the desired address type (preferably **bc1q** – `Native SegWit`)  
4. Show the QR code or copy the address and send it to the payer

**Optional - Mecto (for in-person payments):**  
On the same Receive screen there is a `Mecto` button.  
When you turn it on:
- You will be asked to enter a **nickname** (gravatar)
- Your current location + receive address are temporarily shared with other Coin Wallet users who also have Mecto enabled  
- They can discover you on a small map and send coins without typing or scanning

Data is visible only to other Mecto users and is automatically deleted after 1 hour (or immediately when you turn it off).  
Mecto is completely optional – leave it off if you prefer maximum privacy.

![image](assets/en/05.webp)

## 5️⃣ Sending ₿itcoin

To send Bitcoin:

1. Open the coin → tap **Send**  
2. Paste the address or scan QR code  
3. Enter amount (or tap **Max**)  
4. Choose transaction speed:  

   | Speed   | Approx. confirmation time | Fee level     |
   |---------|---------------------------|---------------|
   | **Slow**    | ~120 minutes              | Lowest       
   | **Default** | ~60 minutes               | Medium       
   | **Fast**    | ~20 minutes               | Higher        

5. Confirm with your 4-digit PIN → transaction is broadcast

### How to speed up a pending ₿itcoin transaction (RBF)

If you chose a slow fee and the transaction is stuck:

1. Go to **History** tab  
2. Tap the pending transaction  
3. Tap **Accelerate** (Replace-By-Fee)  
4. Confirm → the transaction will be re-broadcast with a higher fee

RBF acceleration is currently supported for:  
Bitcoin • Avalanche • Binance Smart Chain • Ethereum • Ethereum Classic • Polygon

More about Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/

## 6️⃣ Exporting Private Keys

**When do you actually need a private key?**  
(99 % of users never do — the 12-word passphrase is enough)

| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### How to export private keys in Coin Wallet

1. Open **Bitcoin (BTC)**  
2. Scroll to the bottom of the page - tap **Export private keys**  
3. The app shows every address with balance + its private key in **WIF** format (starts with 5, K, or L) and a QR code.

Only non-empty addresses appear.

**Example WIF key**  
`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`

**What to do next (recommended)**  
- Open Electrum, Sparrow, BlueWallet or any hardware wallet
- Import/Sweep private key
- All funds instantly move to a new secure address under your current seed

Never store the private key digitally in plain text. After sweeping, it can be safely deleted.

For a complete guide on private keys and derivation paths: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)


## 7️⃣ Technical Details – BIP39, BIP32 and Derivation Paths

Coin Wallet strictly follows the official Bitcoin standards that are used by almost all serious wallets.

`BIP39` - how the passphrase becomes the master private key  
- Default number of words: 12  
- Optional passphrase/password: none ("")  
- Initial entropy: 128 bits (12 words) → 256 bits (24 words)  
- Open-source implementation: https://github.com/paulmillr/scure-bip39  
- Word list: standard English list of 2048 words  
- Supports import of 12, 15, 18, 21 and 24-word phrases from any other BIP39 wallet

`BIP32 + BIP44/BIP49/BIP84` - deterministic generation of all addresses  
From one master key the wallet can generate billions of addresses in a strictly defined order. This is why the same 12 words entered into Electrum, Sparrow, Trezor, Ledger, BlueWallet, etc. will show exactly the same addresses and balances.

**Derivation paths used in Coin Wallet for Bitcoin**

| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Inside each path:
- `/0` — external chain (addresses you show to receive payments)  
- `/1` — internal chain (change addresses that the wallet uses itself)

Because Coin Wallet follows these public standards without any changes, your funds will remain recoverable in any other compatible wallet even in 10–20–30 years.

## 8️⃣ Enhancing Anonymity with Tor

**Why use Tor in Coin Wallet**  
Tor hides your real IP address from Bitcoin nodes, exchanges, and observers.  
All traffic (balances, transactions, swaps) goes through the Tor network - no direct connections, no IP leaks.
This is implemented directly in the app’s source code (see [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).

Coin Wallet has a hidden .onion address and, since v6.6.3 (December 2024), **built-in Tor support directly in the mobile app**.

### How to enable Tor on Android & iOS

1. **Install Orbot** - official Tor Project app (free)  
   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)  
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)  

2. **Open Orbot → tap Start**  
   Select **Coin Wallet** from the list so only the wallet uses Tor (optional but recommended)  
   Wait until it says **"Connected"** (10–30 seconds)

3. **Open Coin Wallet → Settings → Network**  
   Turn on **Use Tor**

4. **Check status**  
   A **purple Tor onion icon** appears in the top bar → all traffic is now routed through Tor

![image](assets/en/06.webp)

That’s it - your mobile Coin Wallet is fully anonymous.

Enjoy private crypto management!

## 📝 Conclusion

[Coin Wallet](https://coin.space/) - one of the true Bitcoin wallet pioneers with a 10-year development history. 
It is deliberately simple and stays laser-focused on its core mission: securely storing your cryptocurrency.
There is no advertising, no news feed, no subscriptions, no social features, no distractions - just a clean, fast, self-custodial wallet that does exactly what it’s supposed to do.
Coin Wallet puts simplicity and security first - always has, always will.

## 📖 Resources

https://coin.space/

https://support.coin.space/hc/en-us

https://en.bitcoin.it/wiki/Wallet

https://bitcoinops.org/

https://github.com/CoinSpace/CoinSpace/

https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/

https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts

https://github.com/paulmillr/scure-bip39
