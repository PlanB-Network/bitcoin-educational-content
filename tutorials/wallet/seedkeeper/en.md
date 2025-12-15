---
name: Seedkeeper
description: How do I back up my wallet Bitcoin with the Seedkeeper smart card?
---

![cover](assets/cover.webp)


The Seedkeeper is a smartcard developed by Satochip, a Belgian company specializing in hardware solutions for managing and protecting digital secrets. Renowned for its range of smartcards for the Bitcoin ecosystem, Satochip designed the Seedkeeper as an alternative to traditional methods of storing mnemonic phrases.


In concrete terms, the Seedkeeper takes the form of a multifunctional, EAL6-certified smart card with a secure processor and tamper-proof memory (a so-called "Secure Element"). As its name suggests, its role is to store Bitcoin wallet mnemonics and passwords in an encrypted and protected way. With Seedkeeper, you can generate, import, organize and save your secrets directly in the card's secure component.


In my opinion, Seedkeeper has two main uses, which we will explore in 2 separate tutorials:


- Bitcoin** mnemonic phrase storage: instead of writing down your 12 or 24 words on paper, you can import them into the smartcard and protect them with a PIN code.
- Password management**: you can generate strong passwords via the Seedkeeper application and store them directly in the smartcard, giving you a convenient, easy-to-use offline password manager.


Technically speaking, Seedkeeper has a capacity of 8192 bytes, enabling it to store a minimum of 50 separate secrets (the exact number will depend on their size and the metadata associated with each one). Seedkeeper can be accessed either [via a smart card reader connected](https://satochip.io/accessories/) to a computer, or via the mobile application with NFC connection. The whole system operates in offline mode, without an Internet connection, guaranteeing a limited attack surface.


![Image](assets/fr/001.webp)


A particularly interesting feature is the ability to duplicate the contents of one Seedkeeper to another in order to create a backup. In this tutorial, we'll show you how to do just that.


Seedkeeper is also very interesting when combined with wallet stateless hardware such as SeedSigner or Specter DIY. In this case, there's no need to use Satochip's client on the computer or cell phone. The Seedkeeper keeps the seed in its secure element and can be used directly with the signing device, eliminating the need for a paper QR code. I won't develop this particular use case in this tutorial, as it's the subject of another dedicated tutorial :


https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. What use case for Seedkeeper?


In this tutorial, I'll only deal with use cases related to Bitcoin, since that's what this tutorial is about. We won't go into the password management functionality, which will be the subject of another tutorial.


Compared to a simple paper backup of the mnemonic phrase, using a Seedkeeper has several advantages:



- Theft-resistant:** The seed in your wallet is not accessible in clear text. To extract it, you need to know the Seedkeeper PIN. A thief who gets hold of the device won't be able to do anything with it without this code.



- Spreading the risk over two factors:** you can divide security between a digital and a physical factor. For example, if you store the Seedkeeper PIN in your password manager, you'll need both access to this manager and physical possession of the smartcard to obtain the seed (a significantly reduced probability of attack).



- Centralized management:** Seedkeeper facilitates the management of multiple seeds from different wallets.



- Easy backups:** simply duplicate encrypted backups to other SeedKeepers.


However, there are a number of disadvantages compared with a simple paper backup of your seed:



- The price:** although modest (around €25), is still higher than that of a sheet of paper.



- Dependence on a general-purpose computing device:** entering and managing seed requires a computer or smartphone, which means that your mnemonic passes through a machine with a much wider attack surface than wallet hardware. This can represent a risk if the machine is compromised. This is why I don't recommend using Seedkeeper to store the seed of a wallet hardware (except in stateless use without a computer, as with SeedSigner). The role of wallet hardware is precisely to store the seed in a minimalist, highly secure environment. By manually entering your seed on your usual computer, it is no longer confined to the wallet hardware: it also ends up on a general-purpose machine, exposed to multiple attack vectors. So it's better to use Seedkeeper for a hot wallet rather than a cold one (except SeedSigner / stateless wallet hardware).



- The risk of loss linked to the PIN:** the direct inaccessibility of the seed, unlike a paper backup, does indeed provide protection against physical theft. But as always, security is a balancing act between the risk of theft and the risk of loss. If your backup requires a PIN, the loss of this code will make it impossible to recover your mnemonic phrase, and thus access your bitcoins.


In view of these advantages and disadvantages, I consider that the best uses for Seedkeeper (apart from its password manager function) are, on the one hand, storing seeds from your **software wallets**, since they already reside on your phone or computer, or from your screenless wallet hardware like the Satochip, and on the other hand, using it in combination with stateless wallet hardware like the SeedSigner, where it really comes into its own.


Another particularly interesting use case for Seedkeeper is the possibility of securely and reliably backing up your wallets' *Descriptors*.


## 2. How do I get a Seedkeeper?


There are two main ways to get your Seedkeeper. You can [buy it directly from Satochip's official store](https://satochip.io/product/seedkeeper/) or from an authorized reseller. But since [the Seedkeeper applet is open-source](https://github.com/Toporin/Seedkeeper-Applet), you also have the option of installing it yourself on [a blank smart card](https://satochip.io/product/blank-javacard-for-diy-project/).


If you wish to use Seedkeeper's backup functionality, you will obviously need to purchase two smartcards.


## 3. Installing the Seedkeeper client


In this tutorial, we'll back up our seed wallet on our Seedkeeper. The first step is to install the software on your computer or smartphone. On a PC, you'll need to [download the latest version of Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). On mobile, the Seedkeeper application is available on the [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) as well as on the [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).


![Image](assets/fr/002.webp)


## 4. Seedkeeper initialization


Launch the application and click on the "*Click & Scan*" button.


![Image](assets/fr/003.webp)


You will be asked for a PIN code for your Seedkeeper. As this is a new card, no PIN has yet been defined. Enter any code to skip this step, then click "*Next*".


![Image](assets/fr/004.webp)


Then place the card on the back of your smartphone. The application will detect that Seedkeeper has not yet been initialized, and will prompt you to set your smart card's PIN code, between 4 and 16 characters long. For optimum security, choose a strong password that's as long as possible, random and made up of a wide variety of characters. This PIN code is the only barrier against physical access to your recovery phrase.


**Remember also to save this PIN now**, for example in a password manager, or on a separate physical medium. In the latter case, never keep the medium containing the PIN in the same place as your Seedkeeper, otherwise this security will become useless. It's important to have a reliable backup: without the PIN, you won't be able to recover the secrets stored on your Seedkeeper.


![Image](assets/fr/005.webp)


Confirm your PIN code a second time.


![Image](assets/fr/006.webp)


Your Seedkeeper is now initialized. You can unlock it by entering the PIN code you've just set.


![Image](assets/fr/007.webp)


You will now be taken to your smart card management page.


![Image](assets/fr/008.webp)


## 5. Register a seed on Seedkeeper


Once your Seedkeeper is unlocked, click on the "*+*" button.


![Image](assets/fr/009.webp)


Select "Import secret*". The "*Generate secret*" option lets you create a new mnemonic phrase directly from within the application.


![Image](assets/fr/010.webp)


In our case, we want to save the seed in our wallet. Click on "*Mnemonic*".


![Image](assets/fr/011.webp)


Assign a "*Label*" to this secret so that it can be easily identified if you store several pieces of information in your Seedkeeper.


![Image](assets/fr/012.webp)


Then enter your recovery phrase in the field provided. If you wish, you can also add a passphrase BIP39 or your *Descriptors*. Then click on "Import*".


![Image](assets/fr/013.webp)


*The mnemonic displayed in this image is fictitious and does not belong to anyone. It is only an example. Never reveal your own mnemonic to anyone, or your bitcoins will be stolen


Place your Seedkeeper on the back of your smartphone.


![Image](assets/fr/014.webp)


Your seed has been registered.


![Image](assets/fr/015.webp)


## 6. Access your seed on Seedkeeper


If you'd like to check your mnemonic phrase, pick up your Seedkeeper and click on the "*Click & Scan*" button.


![Image](assets/fr/016.webp)


Enter your PIN code, then press "*Next*".


![Image](assets/fr/017.webp)


Place your Seedkeeper on the back of your smartphone.


![Image](assets/fr/018.webp)


This takes you to a list of all your registered secrets. In this example, I want to display the seed of my "*Blockstream App*" wallet, so I click on it.


![Image](assets/fr/019.webp)


Press the "*Reveal*" button.


![Image](assets/fr/020.webp)


Scan your Seedkeeper again.


![Image](assets/fr/021.webp)


Your previously recorded mnemonic phrase is now displayed on the screen.


![Image](assets/fr/022.webp)


## 7. Backing up Seedkeeper


We're now going to make a backup of my Seedkeeper on a second Seedkeeper so as to have two copies. This redundancy can be part of a strategy to secure your bitcoins: for example, storing your phrase in two separate locations to limit physical risks, or entrusting a copy to a trusted relative as part of an inheritance plan.


To do this, take along your second Seedkeeper (remember to identify one of the two with a mark on it to avoid any confusion). Start by initializing it, as described in step 4 of this tutorial. Choose a strong password once again. Depending on your strategy, you may opt for a different password or keep the same one.


![Image](assets/fr/023.webp)


Open the application, click on "*Click & Scan*", enter the password of your Seedkeeper n°1 (source), then scan it.


![Image](assets/fr/024.webp)


This takes you to the home page, with a list of your secrets. Click on the three small dots at the top right of the interface.


![Image](assets/fr/025.webp)


Select "*Make a backup*", then press "*Start*".


![Image](assets/fr/026.webp)


Enter the PIN code of your backup card (Seedkeeper n°2).


![Image](assets/fr/027.webp)


Then scan the card.


![Image](assets/fr/028.webp)


Do the same with the main card (Seedkeeper n°1), then click on "*Make a backup*".


![Image](assets/fr/029.webp)


Your Seedkeeper n°2 now contains all the secrets stored on Seedkeeper n°1.


![Image](assets/fr/030.webp)


You can scan your Seedkeeper n°2 to check that the secrets have been copied.


![Image](assets/fr/031.webp)


That's all there is to it! Now you know how to use Seedkeeper to save the mnemonic phrase of a Bitcoin wallet. In a future tutorial, we'll look at how to use Seedkeeper to store your passwords. I also invite you to discover its combined use with SeedSigner :


https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

In this tutorial, we've mentioned the ***Descriptors*** in your Bitcoin wallet several times. Don't know what they are? In that case, I recommend that you take our free CYP 201 training course, which goes into in-depth detail on all the mechanisms involved in operating HD wallets!


https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f