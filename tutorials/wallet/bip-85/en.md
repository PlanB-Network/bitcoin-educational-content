---
name: BIP-85
description: How can I use the BIP-85 to generate multiple seedphrases from a main seed?
---
![cover](assets/cover.webp)


## 1. Understanding the BIP-85


### 1.1 What is BIP-85?


BIP-85 is an advanced function that lets you create several **seed secondary phrases** from one **seed main phrase**.


Each seed secondary sentence can be used to create a completely independent Bitcoin portfolio. These portfolios can be used for a variety of purposes: a Hot Wallet on mobile, a portfolio for a relative, a separate savings portfolio, etc.


All seed sub-phrases are **mathematically derived**, but it is **impossible to trace back to the seed main phrase** from a sub-phrase. This ensures complete separation between each portfolio.


As long as you have access to your seed main phrase (and the associated passphrase if you're using one), you can regenerate any seed secondary phrase **identically**, without having to save it separately.


### 1.2 Why use BIP-85?


BIP-85 is useful if you want to :



- Create several independent Bitcoin portfolios without multiple backups
- Manage your funds according to different uses (savings, expenses, family, projects)
- Guaranteeing safeguards for relatives ("Uncle Jim" function)
- Delete a portfolio without losing access to your funds
- Simplify your security: just one seed key phrase to protect


### 1.3 Advantages over BIP-32


With BIP-32, a single seed sentence can be used to generate a complete hierarchy of Bitcoin accounts and addresses, using derivation paths (for example: `m/44'/0'/0'/0/0`). Each path can represent a separate account, but **all remain linked to the same seed sentence**. So, if this seed phrase is compromised, **all derived accounts become accessible**.


With BIP-85, a seed main sentence can be used to generate several totally independent seed secondary sentences: **if one of these secondary seeds is compromised, the attacker will never be able to go back to the main seed or access the other portfolios**.

This makes it possible to compartmentalize risks:



- You can use a secondary seed for Hot Wallet or temporary use, accepting a higher exposure.
- Even if this Hot Wallet is compromised, your other funds, protected by other secondary seeds or kept offline, **remain safe**.


On the other hand, for both BIP-32 and BIP-85, if the main seed is compromised, **all funds are vulnerable**. It is therefore crucial to protect it with the highest level of security.


![image](assets/fr/02.webp)

## 2. Practical use cases for BIP-85


BIP-85 allows you to create multiple Bitcoin portfolios from a single seed core phrase, each with its own seed secondary phrase. Here are five practical use cases for organizing and securing your Bitcoin funds. Each case explains why using BIP-85 is more practical than managing multiple accounts with a single seed phrase via BIP-32.


### 2.1 Limiting the risk of a less-secure portfolio



- Scenario**: You use a "Hot Wallet" wallet (installed on an Internet-connected device), for daily transactions.
- Solution BIP-85**: You create a seed secondary phrase dedicated to this portfolio.
- Advantage over BIP-32**: You don't need to import the seed primary phrase onto your phone, reducing the risk of hacking. Only the seed secondary phrase is compromised, protecting your other wallets. With BIP-32, you need to use the seed main phrase and a bypass path, exposing all your funds.


### 2.2 Create a portfolio for a family member



- Scenario**: You set up a Bitcoin wallet for someone close to you (e.g. your mother), while being able to recover it if they lose it.
- Solution BIP-85**: You create a dedicated seed secondary sentence and share only this one.
- Advantage over BIP-32**: With BIP-32, creating an account for a loved one requires either sharing your main seed phrase, risking all your funds and complicating management for your loved one (managing branching paths), or creating a new seed phrase to save in addition to your main seed phrase.


### 2.3 Facilitating the management of separate portfolios



- Scenario**: You separate your bitcoins for different purposes (e.g. long-term savings, non-KYC funds).
- Solution BIP-85**: You create seed secondary phrases dedicated to each objective.
- Advantage over BIP-32**: With BIP-32, all accounts share the same seed phrase, which complicates management in third-party portfolios by requiring derivation paths such as `m/44'/0'/0'` to be managed. In addition, it is not possible to assign a separate account per device (e.g. "savings on Coldcard", "daily on mobile", "vacations on Trezor"). BIP-85 assigns a unique seed secondary phrase per objective, which is easy to identify and import separately on each device.


### 2.4 Using a temporary wallet for transactions



- Scenario**: You need a temporary portfolio for a one-off transaction or to preserve confidentiality (e.g.: mixing of funds, interaction with a Exchange KYC, etc.).
- Solution BIP-85**: You create a seed secondary sentence, use it for the transaction, then destroy it if necessary, knowing that it can be regenerated.
- Advantage over BIP-32**: With BIP-32, a temporary account depends on the seed main sentence, exposing all your funds if compromised.




## 3. Before you start



- Hardware** (optional)
 - Coldcard Mk4 or Q1
 - MicroSD card



- Basic knowledge
 - Understanding mnemonic phrases (BIP-39): a list of 12 to 24 words to save a portfolio.
 - Know what a Bitcoin wallet is: software or device to manage your bitcoins, and how to restore it with a mnemonic phrase.
 - More resources in Annexes.



- Compatible** software
 - Sparrow wallet (computer, for watch-only or advanced management)
 - Nunchuck (mobile, for multi-signatures)
 - BlueWallet (mobile)
 - ...



- 3.4 Coldcard** configuration
 - Initialize a seed sentence of 24 words on the Coldcard.
 - Optional: Add a passphrase to secure access to BIP-85 branches.
 - Activate useful options: NFC (for export), disable USB on battery (security).



## 4. Step-by-step tutorial


Follow these steps to create, use and retrieve a secondary mnemonic with BIP-85 on your Coldcard.


### 4.1 Generate a seed secondary sentence


You will create a seed secondary phrase from your seed main phrase.

Switch on your Coldcard, enter your PIN code.



- 1. If you have applied a passphrase to your main seed:**
 - From the Home screen, go to `passphrase`.
    - Choose `Add Word` and enter your password.
    - Press `Apply`.
    - Check the wallet's identity: Go to `Advanced > View Identity` to note the wallet's fingerprint.



- 2. Go to BIP-85** menu
 - From the Home screen, go to `Advanced > Derive seed B85`
 - Read the warning and confirm.


The ColdCard informs you that the seeds generated are mathematically derived from your main seed, but cryptographically totally independent.

![image](assets/fr/03.webp)



- 3. Choose a format

Select the seed phrase format: 12, 18 or 24 words. Check the number of words accepted by the Wallet into which you want to import your seed phrase.

![image](assets/fr/04.webp)



- 4. Select index
 - Enter an index between 0 and 9999.
 - This index is crucial for regenerating the secondary seed at a later date. Keep it carefully with a label such as: "Index 1 = Wallet mobile", "Index 2 = family project", "Index 4 = test mix", ...
 - If you lose it, you won't lose access to your funds, but you'll have to test combinations from 0 to 9999 to find them.

![image](assets/fr/05.webp)



- 5. Note or export seed secondary sentence**

ColdCard now displays a new seed secondary sentence. You can :


 - The **note manually**.
 - Press :
     - 1` to save it on the SD card
     - `2` to **enter "use this seed"** mode on the ColdCard (useful for exporting or signing a transaction)
     - 3` to display a **QR code** (to be scanned with a mobile application such as BlueWallet or Nunchuck)
     - 4` to send it by **NFC**


💡 At this point, you have an independent seed phrase, usable in any Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).

![image](assets/fr/06.webp)

![image](assets/fr/07.webp)

### 4.2 Using the secondary seed


You can now use this derived seed to create a new portfolio in :


- a mobile app
- another Hardware Wallet
- a Multisig portfolio


### 4.3 Recovering a lost seed secondary phrase


To retrieve a secondary seed at any time, repeat the process:

1. Restart your ColdCard

2. Enter your PIN

3. Enter your passphrase, if defined

4. Go to `Advanced > Derive seed B85`

5. Choose format (12/18/24 words)

6. Enter the same index (e.g. `1`)

7. You'll get exactly the same secondary seed



## 5. Limits, risks and best practices


### 5.1 Dependence on seed main sentence + passphrase


The use of BIP85 relies entirely on the 24-word seed main sentence, as well as on passphrase if you've applied one.


- From these two elements, all seed secondary phrases can be regenerated.
- Without one of these 2 elements, you lose access to all derivative portfolios.


### 5.2 Risks in multi-signature configuration


We strongly advise against using secondary seed phrases generated from the same primary seed phrase in a multi-sig configuration: if the device or the primary seed phrase is compromised, all the multi-sig keys could be regenerated by an attacker.


### 5.3 Software compatibility


Not all applications directly support BIP85 derivation. However, seeds generated via BIP85 are standard BIP39 seeds (12, 18 or 24 words), and can therefore be used in any BIP39-compatible portfolio.


### 5.4 BIP85 account register


It is recommended to keep an up-to-date personal register of seed secondary phrases.


- It allows you to find out quickly which BIP85 index corresponds to which portfolio, without having to keep seed secondary phrases.
- This register should remain minimalist, with no explicit mention of Bitcoin, and should be stored separately from the main seed. Remember to mention it in your inheritance plan.


The register can contain :


- bIP85 index used (number from 0 to 9999)
- a usage or reference name (e.g. Hot Wallet, personal savings, Wallet from Mom)
- if necessary, the wallet fingerprint for verification in ColdCard


### 5.5 Backup


Backups must include :


- the main seed
- gW-76 (if used)


Never store together:


- the main seed and passphrase
- the main seed and the BIP85 account register


More resources in Annexes.



## APPENDICES


## A.1 Glossary



- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed phrase](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)



### A.2 Save your recovery phrase


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Understanding the passphrase BIP39


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 How Bitcoin portfolios work


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f