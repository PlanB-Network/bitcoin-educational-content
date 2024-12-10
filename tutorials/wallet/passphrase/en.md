---
name: BIP39 Passphrase
description: Understanding how a passphrase works
---
![cover](assets/cover.webp)

## What is a BIP39 passphrase?

HD wallets are typically generated from a mnemonic phrase consisting of 12 or 24 words. This phrase is very important because it allows for the restoration of all the keys of a wallet in case its physical medium (like a hardware wallet, for example) is lost. However, it constitutes a single point of failure because if it is compromised, an attacker could steal all the bitcoins.

![PASSPHRASE BIP39](assets/notext/01.webp)

This is where the passphrase comes in. It's an optional password that you can freely choose, which is added to the mnemonic phrase in the key derivation process to enhance the wallet's security.

![PASSPHRASE BIP39](assets/notext/02.webp)

Be careful not to confuse the passphrase with your hardware wallet's PIN code or the password used to unlock access to your wallet on your computer. Unlike all these elements, the passphrase plays a role in the derivation of your wallet's keys. **This means that without it, you will never be able to recover your bitcoins.**

The passphrase works in tandem with the mnemonic phrase, altering the seed from which the keys are generated. Thus, even if someone obtains your 12 or 24-word phrase, without the passphrase, they cannot access your funds. **Using a passphrase essentially creates a new wallet with distinct keys. Modifying (even slightly) the passphrase will generate a different wallet.**

## Why should you use a passphrase?

The passphrase is arbitrary and can be any combination of characters chosen by the user. Using a passphrase thus offers several advantages. First, it reduces all risks associated with the compromise of the mnemonic phrase by requiring a second factor to access the funds (burglary, access to your home, etc.).

Next, it can be used strategically to create a decoy wallet, to deal with physical constraints to steal your funds like the infamous "*$5 wrench attack*". In this scenario, the idea is to have a wallet without a passphrase containing only a small amount of bitcoins, enough to satisfy a potential aggressor, while having a hidden wallet. This latter uses the same mnemonic phrase but is secured with an additional passphrase.

Finally, using a passphrase is interesting when one wishes to control the randomness of the HD wallet's seed generation.

## How to choose a good passphrase?
For the passphrase to be effective, it must be sufficiently long and random. Just like with a strong password, I recommend choosing a passphrase that is as long and random as possible, with a variety of letters, numbers, and symbols to make any brute force attack impossible.

It is also important to properly save this passphrase, in the same way as the mnemonic phrase. **Losing it means losing access to your bitcoins**. I strongly advise against memorizing it solely in your head, as this unreasonably increases the risk of loss. The ideal is to write it down on a physical medium (paper or metal) separate from the mnemonic phrase. This backup must obviously be stored in a different location from where your mnemonic phrase is kept to prevent both from being compromised simultaneously.

## Tutorials

To set up a passphrase on a Ledger device (Stax, Flex, or Nano), you can consult this tutorial:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49