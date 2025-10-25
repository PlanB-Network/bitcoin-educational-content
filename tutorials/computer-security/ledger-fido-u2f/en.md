---
name: "Ledger U2F & FIDO2"
description: Enhance your online security with Ledger
---
![cover](assets/cover.webp)


Ledger devices are hardware wallets originally designed to secure a Bitcoin wallet, but they also feature advanced options for strong authentication on the web. Thanks to their compatibility with the **U2F** and **FIDO2** protocols, they enable you to secure access to your online accounts by setting up a second authentication factor.


The U2F (Universal 2nd Factor) protocol was introduced by Google and Yubico in 2014, then standardized by the FIDO Alliance. It enables a second physical authentication factor (2FA) to be added when logging in. Once activated, in addition to the classic password, users must approve each attempt to connect to their account by pressing a button on their Ledger. In this context, the Ledger works in a similar way to a Yubikey. U2F is in fact a sub-component of the FIDO2 standard, encompassing it while bringing significant improvements, including native support for modern browsers and greater flexibility in authentication key management.


These methods are based on asymmetrical cryptography: no secret data is transmitted, making phishing or interception attacks ineffective. U2F and FIDO2 are now supported by many online services.


In this tutorial, we'll show you how to activate U2F and FIDO2 for two-factor authentication with your Ledger.


**Note:** U2F and FIDO2 are supported on all Ledger devices equipped with recent firmware: from version 2.1.0 for the Nano X and Nano S classic, and from version 1.1.0 for the Nano S Plus. Stax and Flex models are natively compatible.


## Install the Ledger Security Key application


If you're using a Ledger device, you probably know that the firmware alone doesn't contain all the features needed to manage crypto wallets. For example, to use a Bitcoin wallet, you need to install the "*Bitcoin*" application. Similarly, to manage MFA keys, you'll need to install the "*Security Key*" application.


Before you start, make sure you've set up your Bitcoin wallet on your Ledger. It's important to save your mnemonic correctly, as the keys used for 2FA are derived from this mnemonic. If your Ledger is lost or damaged, you can recover access to your keys by entering your mnemonic phrase on another Ledger device (for the moment, FIDO2 identifiers in "*passwordless*" mode are not yet supported on Ledgers, so there are no resident identifiers).


Connect your Ledger to your computer and unlock it.


![Image](assets/fr/01.webp)


To install the application, open the [Ledger Live] software (https://www.Ledger.com/Ledger-live), then go to the "*My Ledger*" tab. Find the "*Security Key*" application and install it on your device.


![Image](assets/fr/02.webp)


The "*Security Key*" application should now appear alongside the other applications installed on your Ledger.


![Image](assets/fr/03.webp)


Click on the application to leave it open for the next steps in the tutorial.


![Image](assets/fr/04.webp)


## Use U2F/FIDO2 for 2FA with a Ledger


Access the account you want to secure with two-factor authentication. For example, I'm going to use a Bitwarden account. You'll usually find the 2FA option in the service settings, under the "*authentication*", "*security*", "*login*" or "*password*" tabs.


![Image](assets/fr/05.webp)


In the section dedicated to two-factor authentication, select the "*Passkey*" option (the term may vary depending on the site you're using).


![Image](assets/fr/06.webp)


You will often be asked to confirm your current password.


![Image](assets/fr/07.webp)


Give your security key a name for easy recognition, then click on "*Read Key*".


![Image](assets/fr/08.webp)


Your account details will appear on the Ledger display. Press the "*Register*" button to confirm (or both buttons simultaneously, depending on the model you're using).


![Image](assets/fr/09.webp)


The access key has been successfully registered.


![Image](assets/fr/10.webp)


Register this security key.


![Image](assets/fr/11.webp)


From now on, when you log in to your account, in addition to your usual password, you'll be asked to connect your Ledger.


![Image](assets/fr/12.webp)


You can then press the "*Log in*" button on your Ledger display to confirm authentication (or both buttons simultaneously, depending on the model you're using).


![Image](assets/fr/13.webp)


The advantage of using a Hardware Wallet Ledger for two-factor authentication is that you can easily recover your keys thanks to the mnemonic phrase. In addition to this basic backup, you can also use an emergency code supplied by each service where you have activated 2FA. This emergency code enables you to connect to your account if you lose your security key. It therefore replaces the 2FA for a connection if necessary.


On Bitwarden, for example, you can access this code by clicking on "*View recovery code*".


![Image](assets/fr/14.webp)


I recommend that you keep this code in a different place from where you store your main password, to prevent them being stolen together. For example, if your password is saved in a password manager, keep your 2FA emergency code on paper, separately.


This approach offers you two levels of backup in the event of loss of your Ledger for 2FA authentication: a first backup using the mnemonic phrase for all your accounts, and a second account-specific backup using the emergency codes. However, it is important **not to confuse the role of the mnemonic with that of the emergency code**:


- The 12- or 24-word mnemonic phrase gives you access not only to the keys used for 2FA on all your accounts, but also to your bitcoins secured with your Ledger ;
- The emergency code allows you to temporarily bypass the 2FA request only on the account concerned (in this example, only on Bitwarden).


Congratulations, you're now up to speed on using your Ledger for MFA! If you found this tutorial useful, I'd be very grateful if you'd leave a green thumb below. Please feel free to share this tutorial on your social networks. Thank you very much!


I'd also recommend this other tutorial, in which we look at another solution for U2F and FIDO2 authentication:


https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e