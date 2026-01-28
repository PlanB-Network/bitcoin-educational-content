---
name: Seedkeeper - Password Manager
description: How to save your passwords with the Seedkeeper smart card?
---

![cover](assets/cover.webp)


The Seedkeeper is a smartcard developed by Satochip, a Belgian company specializing in hardware solutions for managing and protecting digital secrets. Renowned for its range of smartcards for the Bitcoin ecosystem, Satochip conceived the Seedkeeper as an alternative to traditional methods of storing mnemonic phrases and other digital secrets.


In concrete terms, the Seedkeeper takes the form of a multifunctional, EAL6-certified smart card with a secure processor and tamper-proof memory (a so-called "Secure Element"). As its name suggests, its role is to store Bitcoin wallet mnemonics and passwords in an encrypted and protected way. With Seedkeeper, you can generate, import, organize and save your secrets directly in the card's secure component.


In my opinion, Seedkeeper has two main uses, which we will explore in 2 separate tutorials:


- Bitcoin** mnemonic phrase storage: instead of writing down your 12 or 24 words on paper, you can import them into the smartcard and protect them with a PIN code.
- Password management**: you can generate strong passwords via the Seedkeeper application and store them directly in the smartcard, giving you a convenient, easy-to-use offline password manager.


Technically speaking, Seedkeeper has a capacity of 8192 bytes, enabling it to store a minimum of 50 separate secrets (the exact number will depend on their size and the metadata associated with each one). Seedkeeper can be accessed either [via a smart card reader connected](https://satochip.io/accessories/) to a computer, or via the mobile application with NFC connection. The whole system operates in offline mode, without an Internet connection, guaranteeing a limited attack surface.


![Image](assets/fr/001.webp)


A particularly interesting feature is the ability to duplicate the contents of one Seedkeeper to another in order to create a backup. In this tutorial, we'll show you how to do just that.


In this tutorial, we'll only cover the use of SeedKeeper for traditional passwords, in the manner of a password manager. If you'd like to use SeedKeeper to save Bitcoin wallet mnemonic phrases, please see this other tutorial:


https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. How do I get a Seedkeeper?


There are two main ways to get your Seedkeeper. You can [buy it directly from Satochip's official store](https://satochip.io/product/seedkeeper/) or from an authorized reseller. But since [the Seedkeeper applet is open-source](https://github.com/Toporin/Seedkeeper-Applet), you also have the option of installing it yourself on [a blank smart card](https://satochip.io/product/blank-javacard-for-diy-project/).


If you wish to use Seedkeeper's backup functionality, you will obviously need to purchase two smartcards.


## 2. Installing the Seedkeeper client


The first step is to install the software on your computer or smartphone. On a PC, you'll need to [download the latest version of Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). On mobiles, the Seedkeeper application is available on the [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) and on the [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).


![Image](assets/fr/002.webp)


## 3. Seedkeeper initialization


Launch the application and click on the "*Click & Scan*" button.


![Image](assets/fr/003.webp)


You will be asked for a PIN code for your Seedkeeper. As this is a new card, no PIN has yet been defined. Enter any code to skip this step, then click "*Next*".


![Image](assets/fr/004.webp)


Then place the card on the back of your smartphone. The application will detect that Seedkeeper has not yet been initialized, and will prompt you to set your smart card's PIN code, between 4 and 16 characters long. For optimum security, choose a robust PIN code that is as long as possible, random and made up of a wide variety of characters. This PIN is the only barrier against physical access to your passwords.


**Remember also to save this PIN now**, for example in a password manager, or on a separate physical medium. In the latter case, never keep the medium containing the PIN in the same place as your Seedkeeper, otherwise this security will become useless. It's important to have a reliable backup: without the PIN, you won't be able to recover the secrets stored on your Seedkeeper.


![Image](assets/fr/005.webp)


Confirm your PIN code a second time.


![Image](assets/fr/006.webp)


Your Seedkeeper is now initialized. You can unlock it by entering the PIN code you've just set.


![Image](assets/fr/007.webp)


You will now be taken to your smart card management page.


![Image](assets/fr/008.webp)


## 4. Save passwords on Seedkeeper


Once your Seedkeeper is unlocked, click on the "*+*" button.


![Image](assets/fr/009.webp)


Select "Generate secret*". The "*Import a secret*" option allows you to save an existing secret (for example, a password you've created in the past).


![Image](assets/fr/010.webp)


In our case, we want to save a password. Click on "*Password*".


![Image](assets/fr/011.webp)


Assign a "*Label*" to this secret so that it can be easily identified if you store several pieces of information in your Seedkeeper. You can also add an identifier associated with the password and the URL of the site.


![Image](assets/fr/012.webp)


Choose the length and parameters of your password, then click on "*Generate*", then "*Import*".


![Image](assets/fr/013.webp)


Place your Seedkeeper on the back of your smartphone.


![Image](assets/fr/014.webp)


Your password has been registered.


![Image](assets/fr/015.webp)


## 5. Access your Seedkeeper password


If you want to check your password, take your Seedkeeper and click on the "*Click & Scan*" button.


![Image](assets/fr/016.webp)


Enter your PIN code, then press "*Next*".


![Image](assets/fr/017.webp)


Place your Seedkeeper on the back of your smartphone.


![Image](assets/fr/018.webp)


This takes you to a list of all your registered secrets. In this example, I want to display the password for my Plan ₿ Academy account, so I click on it.


![Image](assets/fr/019.webp)


Press the "*Reveal*" button.


![Image](assets/fr/020.webp)


Scan your Seedkeeper again.


![Image](assets/fr/021.webp)


Your previously saved password now appears on the screen. You can copy it and use it on the relevant website.


![Image](assets/fr/022.webp)


## 6. Backing up Seedkeeper


We're now going to make a backup of my Seedkeeper on a second Seedkeeper so that we have two copies. This redundancy can be part of a strategy to secure your most important passwords: for example, storing your Seedkeepers in 2 separate locations to limit physical risks, or entrusting a copy to a trusted relative.


To do this, take along your second Seedkeeper (remember to identify one of the two with a mark on it to avoid any confusion). Start by initializing it, as described in step 3 of this tutorial. Once again, choose a strong PIN code. Depending on your strategy, you may opt for a different PIN or keep the same one.


![Image](assets/fr/023.webp)


Open the application, click on "*Click & Scan*", enter the PIN of your Seedkeeper n°1 (source), then scan it.


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


That's all there is to it! Now you know how to use Seedkeeper to store your passwords. In a future tutorial, we'll look at how to use Seedkeeper to back up a Bitcoin wallet. I also invite you to discover its combined use with SeedSigner :


https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356