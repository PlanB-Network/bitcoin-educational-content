---
name: Satodime
description: Find out how to use the Satodime with the mobile application
---
![cover](assets/cover.webp)


This guide takes you through the installation, configuration and use of the Satodime mobile application. You'll learn how to take possession of your card, create safes, add funds, unseal and recover your private keys. Appendices provide resources, best practices and technical explanations.


## Introduction


**Satodime**, developed by **[Satochip](https://satochip.io/fr/)**, is a secure bearer card for storing Bitcoin in a tangible and simple way. It acts as a self-custodial wallet hardware, where you have full control over your private keys without depending on a third party. Open-source and EAL6+ certified, it supports up to three independent safes.


### Product background


Satodime, a **carte au porteur, belongs to whoever physically possesses it**, with no need for prior registration or identification. It meets the need for secure, portable bitcoin storage, allowing anyone holding the card to use it or transfer bitcoins by scanning it via the mobile app to take possession or unseal safes. Unlike a paper bill, it uses a secure chip to seal the private keys, which are revealed only after unsealing, making the card similar to cash where ownership is determined by physical possession. Ideal for giving bitcoins as gifts, it facilitates the secure transfer of bitcoins from hand to hand, while the mobile application exploits NFC for accessible smartphone interaction.



- Security**: Private keys generated and stored in the tamper-proof chip; visible status (sealed, unsealed, empty).
- Features**: Buy bitcoins directly via the app (Paybis partner); manage Mainnet and Testnet.
- Open-source**: Code under AGPLv3 license, verifiable on GitHub.


### Continuous evolution


The application evolves regularly. Check the Satochip website or stores for updates. For example, new blockchains or purchase functionalities may be added. Check the [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) for ongoing developments.


## 1. Prerequisites


Before getting started with **Satodime**, make sure you have the following items:



- Compatible smartphone**: Android or iOS device with NFC enabled.
- Satodime** card: New or uninitialized.
- Internet connection**: To download the app.
- Basic knowledge**: Understanding private/public keys and the risks of loss (irreversible).
- Secure medium**: A safe place to record private keys once unsealed (paper, metal; never digital).


## 2. Installation



- Download the application** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Check the developer (Satochip) to avoid fraud.
 - Satodime is **open-source**. Source code : [Satochip's GitHub](https://github.com/Toporin/Satodime-Applet).



- Install and launch the application**: Activate NFC on your phone if necessary.


![image](assets/fr/01.webp)


## 3. Initial configuration


### 3.1 Launch application and scan


Open the app and follow the wizard. Place the Satodime card on your phone's NFC reader (usually on the back). Hold it down throughout the operation to ensure a stable connection.



- If NFC doesn't work, check your phone's settings.
- A toast confirms the success: "Successful reading".


![image](assets/fr/02.webp)


As a general rule, **all the following operations will require confirmation by scanning the Satodime card**


### 3.2 Taking possession of the card (*Ownership*)


For the first use, become the owner of the card to secure it:



- Click on "*Take Ownership*" in the app.
- Confirm the operation: this generates a unique owner key.
- Scan the map again to apply the changes.
- Warning**: This step is irreversible. Please refer to [the article on *ownership*](https://satochip.io/satodime-ownership-explained/).


![image](assets/fr/03.webp)



## 4. Create a safe


Satodime supports up to 3 safes. Create one to store bitcoin:



- Select an empty safe (e.g. Safe 01).
- Select blockchain (Bitcoin).
- Click on "*Create & Seal*".
- Scan the card to generate and seal the private key (unknown until unsealed).
- Congratulations**: Your safe is now sealed and ready to receive funds.


![image](assets/fr/04.webp)


![image](assets/fr/05.webp)


## 5. Add funds


Once sealed, load the safe with bitcoins:



- Select the safe.
- Click on "*Add funds*".
- Copy the public address or scan the QR code.
- Send funds from another wallet.
- Check the balance after confirmation on the blockchain.
- Purchase option: Click on "*Purchase*" to purchase directly via Paybis (Visa, Mastercard, etc.). Applicable fees.


![image](assets/fr/06.webp)


## 6. Unseal a safe


To access the private key and transfer the funds elsewhere, unseal the safe:



- Select the sealed safe.
- Click on "Unseal".
- Confirm the warning: this operation is irreversible.
- Scan the card to unseal.
- The safe is set to "*Unsealed*"; the private key can now be viewed/exported.
- Warning**: Once unsealed, the private key is accessible. If someone takes possession of your smartphone, they can access this key, and thus recover the funds in your safe (irreversible).


![image](assets/fr/07.webp)


## 7. Recover private key


After unsealing, export the key for use in another wallet :



- Make sure you're in a safe environment.
- Click on "*Show private key*".
- Choose the format: Legacy, SegWit, WIF, etc.
- Copy the key or scan the QR code.
- Security**: Never share your private key. Store it offline.
- Import it into a wallet software program compatible with fund management (Sparrow Wallet or Electrum, for example).


![image](assets/fr/08.webp)




## 8. Reset trunk


Resetting the safe irreversibly deletes the associated private key. In other words, if you have not secured a copy of your private key, or imported it into another wallet, resetting the safe will cause the irreversible loss of the funds in it.


![image](assets/fr/09.webp)


Resetting the trunk makes the slot empty and ready for a new trunk.


## 9. Transfer ownership


To - for example - offer bitcoins through Satodime, you must :


- Take ownership of the card,
- Create a Bitcoin safe,
- Transfer satss there,
- Transfer card ownership: the next person to scan the card becomes its owner,
- Give the Satodime card to the person of your choice, and invite them to download the application and then scan the card to take ownership of it - and thus access the bitcoins 'stored' on it.


![image](assets/fr/10.webp)



## APPENDICES


### A1. Best practices


To use **Satodime** securely :



- Secure the card**: Treat it like cash; loss = lost funds if not the owner.
- Key backup**: After unsealing, record private keys on a secure physical medium. Never digital.
- Check status**: Always scan to confirm card ownership and sealed/unsealed status of safes.
- Confidentiality**: Use new addresses; avoid centralized exchanges for transfers.
- Updates**: Keep the app up to date via the stores.
- Recovery**: If the card is lost but owned, the funds are on the blockchain; use the private key if unsealed.


### A2. Additional resources


Specific to Satodime :


- [Satodime product](https://satochip.io/fr/product/satodime/)
- [Mobile Guide](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)


[Plan ₿ Academy](https://planb.academy/) for tutorials on self-custody, private keys, etc.


**Save your recovery phrase** :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tutorial on the Satochip (the brand's first product) :**


https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Seedkeeper tutorials:**


https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. About Satochip


**Official links** :


- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Support: info@satochip.io


**Satochip** is a Belgian company that develops hardware and software solutions for managing and storing bitcoins and other cryptocurrencies. Its flagship product, the Satochip hardware wallet, is an NFC card equipped with an EAL6+ certified secure element. Complemented by the Seedkeeper, a mnemonic phrase and secret manager, and the Satodime, a bearer card, Satochip offers a comprehensive range tailored to users' needs. Its devices, powered by open source software, aim to democratize security on Bitcoin.