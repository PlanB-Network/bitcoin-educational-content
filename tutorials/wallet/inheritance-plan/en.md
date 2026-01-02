---
name: Inheritance plan Bitcoin
description: How to transfer bitcoins to your loved ones
---

![cover](assets/cover.webp)


The transmission of bitcoins represents a major technical challenge that many holders overlook. Unlike traditional banking assets, where a financial institution can remit the funds to the rightful owners, Bitcoin works without intermediaries. Your loved ones will never be able to access your funds without the necessary technical information, regardless of their legal legitimacy.


This tutorial guides you through the creation of a technical inheritance plan. You'll learn how the on-chain mechanisms for automated transmission work, how to document your configurations, and how to choose the right solutions to ensure that your Bitcoin legacy remains accessible to your loved ones.


## Why a technical heritage plan is essential


Bitcoin is based on a fundamental cryptographic principle: whoever holds the private keys controls the funds. This sovereignty becomes a major vulnerability when the holder disappears without having transmitted the necessary information.


A Bitcoin inheritance plan must meet two seemingly contradictory objectives: allowing your loved ones to access your funds when the time comes, while preventing anyone else from accessing them prematurely. This delicate balance relies on Bitcoin's native programming capabilities.


Technical complexity adds an extra layer of difficulty. Your heirs will have to manipulate concepts such as recovery phrases, portfolio descriptors, or derivation paths. Without adequate preparation, even a well-intentioned heir risks making irreversible mistakes.


## How on-chain inheritance works


Bitcoin uses its scripting language to encode spending conditions directly in transactions. on-chain inheritance exploits this programmability to create alternative recovery paths that activate automatically.


### Timelocks


Timelocks are the fundamental mechanism of Bitcoin inheritance. They enable funds to be locked until a time condition is met.


**CLTV (CheckLockTimeVerify)**: This absolute timelock checks that a specific time (date or block height) has been reached before authorizing the expenditure. For example, "these funds can only be spent after block 900000" or "after January 1, 2026". The advantage of CLTV is that it allows long delays (several years), but the date is fixed and applies identically to all UTXOs in the portfolio. To maintain control of your funds, you must periodically create a new portfolio with an extended expiry date and transfer your funds to it.


**CSV (CheckSequenceVerify)**: This relative timelock verifies that a certain number of blocks have elapsed since the UTXO was created. For example, "these funds can only be spent 52560 blocks (~1 year) after receipt". The advantage of CSV is that each UTXO has its own independent counter. Every time you perform a transaction, the newly created UTXOs reset their own time limit. However, the technical limit of 65535 blocks (~15 months maximum) restricts the possible timeframes. This approach is more natural for everyday use, since your normal activity automatically pushes back the deadlines.


### Multiple spending paths


An inheritance portfolio combines several spending paths in each address:



- Main path** : The owner can spend his funds at any time with his main key, with no time restrictions.
- Recovery path(s)**: One or more alternative keys can spend funds only after a set time has elapsed.


Each transaction performed by the owner "refreshes" the UTXO, creating new outputs with reset timelocks. This mechanism ensures that as long as the owner remains active, the recovery paths never activate.


### Miniscript and Taproot


**Miniscript** is a structured language developed by Andrew Poelstra, Pieter Wuille and Sanket Kanjalkar that makes it easy to write and analyze complex Bitcoin scripts. It allows you to compose readable and verifiable spending conditions, essential for inheritance configurations involving multiple keys and timelocks.


**Taproot** (activated in November 2021) significantly improves on-chain inheritance. Thanks to its tree structure (MAST), only the spending condition used is revealed on the blockchain. If the owner spends his funds normally, the inheritance conditions remain invisible. This confidentiality also reduces transaction costs for complex paths.


## The critical importance of descriptors


For legacy portfolios, the recovery phrase (seed) is not enough to restore access to funds. The **descriptor** becomes the critical element.


A descriptor is a string that exhaustively describes the structure of a portfolio: the public keys involved, spending conditions, derivation paths, and configured timelocks. Here's a simplified example:


```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```


This descriptor says: "either the master key can spend immediately, or the recovery key can spend after 52560 blocks".


Let's unpack this example:


- `wsh()` : Witness Script Hash, indicates address type (P2WSH)
- or_d()`: "or" condition with a default branch
- pk([fingerprint/path]xpub...)`: The master public key with its fingerprint and derivation path
- and_v()`: "and" condition combining recovery key with timelock
- `older(52560)`: The relative time lock of 52560 blocks


**Without the descriptor, even with all the recovery phrases, your heirs won't be able to rebuild the portfolio.** A standard portfolio can only be restored from seed because it follows standardized derivation paths (BIP44, BIP84). A legacy portfolio, on the other hand, uses customized scripts that cannot be guessed. The descriptor backup (or the configuration file exported by your software) must accompany the recovery phrases in your inheritance plan.


## Documentary components of an inheritance plan


Beyond the technical mechanisms, an effective legacy plan rests on three pillars of documentation.


### The letter of inheritance


This personal letter is the entry point to your plan. Written for your heirs, it explains the context and the precautions to be taken.


Your letter must include explicit safety rules:


- Don't rush, take time to learn before moving funds
- Never communicate a complete recovery phrase to a single person
- Never enter a recovery phrase into an unverified software program or computer
- Beware of scams and people offering unsolicited help
- Seek the advice of at least two people you trust before making any decision


This letter also contains your notary's contact details and the location of your will. It should never contain recovery phrases or passwords.


### The directory of trusted contacts


No heir should face bitcoin recovery alone. This directory lists people who can provide technical or legal assistance.


For each contact, document: full name, relationship to you, role in the plan, level of trust, Bitcoin skills, and full contact details. The basic rule: your heirs should always consult at least two different people before making any important decision.


### Bitcoin asset inventory


This section maps all your bitcoins with the technical information needed to recover them.


For each portfolio, document :


- Portfolio type**: hardware, software, configuration (single-sig, multisig, legacy)
- Device location**: physical location of wallet hardware
- Descriptor/configuration file location**: critical for advanced portfolios
- Location of recovery phrase**: separate from descriptor
- Access codes**: where PINs and passphrases are stored
- Configured delays**: when recovery paths activate


## Technical solutions available


Several software packages implement on-chain inheritance mechanisms. Each has its own technical characteristics.


### Liana


Liana is desktop software (Linux, macOS, Windows) using Miniscript to create portfolios with timed recovery paths. The project is developed by Wizardsardine, co-founded by Antoine Poinsot (Bitcoin Core contributor).


**Technical architecture**: Liana creates P2WSH portfolios (SegWit native) by default, with Taproot support available depending on the compatibility of your wallet hardware. The architecture is based on a main path and one or more recovery paths. The generated descriptor encodes all conditions and must be saved.


**Timelocks used**: Liana uses relative timelocks (CSV), limited to 65535 blocks (~15 months). To maintain control, you must perform a refresh transaction before the timelock expires.


**Hardware wallet integration**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY, and other devices are compatible for signing transactions.


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper


Bitcoin Keeper is a mobile application (iOS, Android) combining multisig and timelocks via its "Enhanced Vaults". The mobile approach with integrated guidance makes it accessible to less technical users.


**Technical architecture**: Enhanced Vaults use Miniscript to create multisig configurations where additional keys activate after defined delays. The Inheritance Key adds to the existing quorum, while the Emergency Key can bypass the multisig completely.


**Timelocks used**: Bitcoin Keeper uses absolute timelocks (CLTV), allowing lead times in excess of 15 months. The activation date is set at wallet creation and applies to all UTXOs. The application incorporates a "revaulting" function which automatically manages the refresh: the user simply follows the guided steps, without having to manually create a new wallet.


**Additional features**: Integrated inheritance documents, Canary Wallets to detect key compromise, and refresh reminders.


https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Heritage


Heritage is a desktop application that uses Taproot scripts to encode inheritance conditions. The use of Taproot offers enhanced confidentiality, since unused paths remain invisible on the blockchain.


**Technical architecture**: Each Heritage address integrates a main path and alternative paths for each heir, with progressive timeframes. The hierarchical structure makes it possible to define a personal backup at 6 months and family heirs at 12-15 months.


**Modes of use**: Stand-alone version with your own node (free) or managed service adding reminders and notifications to heirs (0.05%/year).


https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## The heir's recovery process


Understanding the recovery process helps prepare an effective plan. Here are the technical steps an heir will need to follow.


### Recovery requirements


The heir needs :

1. **The descriptor or configuration file** of the original portfolio (JSON or text format, depending on the software)

2. **Its recovery phrase** (the one associated with its inheritance key, usually 12 or 24 words)

3. **Compatible software** (Liana, Bitcoin Keeper, Heritage, or Sparrow/Specter for standard descriptors)

4. **A connection to a Bitcoin** node to check timelock status and broadcast the transaction


### Recovery steps


1. **Install the software** on a secure device and configure the connection to the Bitcoin network (personal node or Electrum server)

2. **Import the descriptor** to reconstruct the portfolio structure. The software will automatically generate all addresses used

3. **Restore inheritance key** from recovery phrase. The software will check that this key corresponds to one of the keys authorized in the descriptor

4. **Synchronize portfolio** to discover all UTXOs and their spending conditions

5. **Check timelock expiration**: the software will indicate for each UTXO whether the recovery path is active

6. **Create the recovery transaction** to an address controlled solely by the heir (ideally a new single wallet)

7. **Sign and broadcast** the transaction on the Bitcoin network


If the timelock has not yet expired, the heir will have to wait. The software will display the date or block from which recovery becomes possible. During this waiting period, the funds remain secure on the blockchain.


### Points to watch for the heir


The heir must pay particular attention to :


- Check the authenticity of downloaded software** (checksums, signatures)
- Never share your recovery phrase** with anyone offering help
- Consult at least two people you trust** before carrying out recovery
- Transfer the funds to a simple portfolio** that he controls completely after recovery


## Best practices


### Separation of information


Never store all information in one place. The descriptor must be separated from the recovery phrases, which in turn are separated from the PIN codes. This distribution complicates access for an attacker while remaining reconstitutable by your legitimate heirs.


### Recovery tests


Before depositing significant funds, test the entire recovery process with a small amount. Verify that you can restore the portfolio from the descriptor and recovery phrases on a blank device. Document the steps for your heirs.


### Timelock maintenance


Plan to refresh your timelocks well before they expire. For a 12-month timelock, perform a transaction every 9-10 months. Software usually offers reminders or automated refresh functions.


### Plan update


Your Bitcoin configuration evolves. Each significant change (new portfolio, modification of deadlines, addition of heir) must be reflected in your documentation. Establish an annual review routine.


## Choosing your approach


The choice between the different solutions depends on your technical profile and your specific needs.


**Liana** is suitable for desktop users who prefer open source software with full control via their own node. Configuration remains accessible thanks to the guided interface. Relative timelocks (CSV) simplify maintenance, as your normal activity automatically pushes back deadlines. Limitation: maximum delay of approx. 15 months (65535 blocks).


**Bitcoin Keeper** targets mobile users looking for an intuitive interface with integrated accompanying documents. The application offers two types of special key: the Inheritance Key (which adds to the quorum) and the Emergency Key (which bypasses it completely). Absolute timelocks (CLTV) allow lead times in excess of 15 months, with an integrated revaulting function simplifying refreshment. The Diamond Hands plan unlocks advanced legacy features.


**Inheritance** is aimed at technical users who appreciate Taproot confidentiality and hierarchical inheritance with progressive delays. The Taproot tree structure hides inheritance conditions during normal transactions, revealing only the condition used during recovery.


All three solutions have one thing in common: they require periodic refreshing to prevent premature activation of recovery paths. This constraint is both the price and the guarantee of on-chain's untrusted legacy. Schedule regular reminders and make this maintenance part of your Bitcoin management routine.


## Conclusion


A technical Bitcoin legacy plan combines cryptographic mechanisms (timelocks, Miniscript, Taproot) with rigorous documentation. Advanced wallets allow you to transmit your bitcoins automatically after a period of inactivity, without third-party intervention.


The critical elements to pass on to your heirs are: the descriptor or configuration file, their recovery phrase, detailed recovery instructions, and contact details of competent people who can assist them.


Start by choosing a technical solution suited to your profile, test it with a small amount, then document the whole in a structured plan. The initial complexity guarantees that your Bitcoin assets will be passed on in full confidence.


## Resources


### Inheritance plan template



- [Bitcoin Inheritance Plan Template (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plan ₿ Network Documentation Template


### Technical references



- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Specification of absolute timelocks (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Specification of relative timelocks (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Official Miniscript documentation by Pieter Wuille


### Official solution websites



- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7