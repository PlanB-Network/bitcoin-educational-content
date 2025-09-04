---
name: Trezor U2F & FIDO2
description: Strengthen your online security with Trezor
---
![cover](assets/cover.webp)


Trezor devices are hardware wallets originally designed to secure a Bitcoin wallet, but they also feature advanced options for strong authentication on the web. Thanks to their compatibility with the **U2F** and **FIDO2** protocols, they enable you to secure access to your online accounts without relying solely on passwords.


The U2F (*Universal 2nd Factor*) protocol was introduced by Google and Yubico in 2014, then standardized by the FIDO Alliance. It enables a second physical authentication factor (2FA) to be added when logging in. Once activated, in addition to the classic password, users must approve each attempt to connect to their account by pressing a button on their Trezor. In this context, the Trezor works in a similar way to a Yubikey.


This method is based on asymmetrical cryptography: no secret data is transmitted, making phishing or interception attacks ineffective. U2F is now supported by many online services.


In addition to U2F, which enables two-factor authentication, Trezors also support FIDO2 (*Fast IDentity Online 2.0*), an evolution of U2F. This is a standardized authentication protocol from 2018, which extends the logic of U2F and aims to completely replace passwords. It is based on two components: *WebAuthn* (browser side) and *CTAP2* (physical key side). FIDO2 enables "passwordless" authentication: users identify themselves solely via their Trezor device, which acts as a unique cryptographic token, with no additional password. This protocol is now compatible with a number of online services, particularly those geared towards the enterprise.


In addition to "passwordless*" functionality, FIDO2 also enables two-factor authentication in a similar way to U2F.


FIDO2 also introduces the notion of resident credentials, i.e. identifiers stored directly in the Trezor, which include both the private key enabling connection and the user's identification information. This mechanism enables truly password-free authentication: simply plug in your Trezor and confirm access, without entering either ID or password. Conversely, non-resident credentials, which are more conventional, store only the private key in the device; the user ID remains stored on the server side, and must therefore be entered at each connection. We'll look at how to save them with your Trezor later on.


In this tutorial we'll discover how to activate U2F or FIDO2 for two-factor authentication, and then how to configure FIDO2 to access your accounts without a password, directly with your Trezor.


**Note:** U2F is compatible with all Trezor models, but FIDO2 is only supported on the Safe 3, Safe 5, and Model T, not the Model One.


## Using U2F/FIDO2 for 2FA on a Trezor


Before you start, make sure you've set up your Bitcoin wallet on your Trezor. It's important to save your mnemonic correctly, as the keys used for U2F and FIDO2 in two-factor authentication are derived from this mnemonic. If your Trezor is lost or damaged, you can recover access to your keys by entering your mnemonic phrase on another Trezor device (note that for FIDO2 credentials in "*passwordless*" mode, seed alone is not enough, as we'll see in the next sections).


Connect your Trezor to your computer and unlock it.


![Image](assets/fr/01.webp)


Access the account you want to secure with two-factor authentication. For example, I'm going to use a Bitwarden account. You'll usually find the 2FA option in the service settings, under the "*authentication*", "*security*", "*login*" or "*password*" tabs.


![Image](assets/fr/02.webp)


In the section dedicated to two-factor authentication, select the "*Passkey*" option (the term may vary depending on the site you're using).


![Image](assets/fr/03.webp)


You will often be asked to confirm your current password.


![Image](assets/fr/04.webp)


Give your security key a name for easy recognition, then click on "*Read Key*".


![Image](assets/fr/05.webp)


Your account details will appear on the Trezor screen. Touch the screen or press the button to confirm. You will also be asked to confirm your PIN code.


![Image](assets/fr/06.webp)


Register this security key.


![Image](assets/fr/07.webp)


From now on, when you want to connect to your account, in addition to your usual password, you'll be asked to connect your Trezor.


![Image](assets/fr/08.webp)


You can then press your Trezor screen to confirm authentication.


![Image](assets/fr/09.webp)


The advantage of using a Hardware Wallet Trezor for two-factor authentication is that you can easily recover your keys thanks to the mnemonic phrase. In addition to this basic backup, you can also use an emergency code provided by each service where you have activated 2FA. This emergency code enables you to connect to your account if you lose your security key. It therefore replaces the 2FA for a connection if necessary.


On Bitwarden, for example, you can access this code by clicking on "*View recovery code*".


![Image](assets/fr/10.webp)


I recommend that you keep this code in a different place from where you store your main password, to prevent them being stolen together. For example, if your password is saved in a password manager, keep your 2FA emergency code on paper, separately.


This approach offers you two levels of backup in the event of loss of your Trezor for 2FA authentication: a first backup using the mnemonic phrase for all your accounts, and a second one specific to each account with the emergency codes. However, it is important **not to confuse the role of the mnemonic with that of the emergency code**:


- The 12- or 24-word mnemonic phrase gives you access not only to the keys used for 2FA on all your accounts, but also to your bitcoins secured with your Trezor ;
- The emergency code allows you to temporarily bypass the 2FA request only on the account concerned (in this example, only on Bitwarden).


## Using FIDO2 on a Trezor


In addition to two-factor authentication, FIDO2 also enables "passwordless" authentication, i.e. without having to enter a password when logging on to a site. Simply connect your Trezor to your computer to access your secure account this way. Here's how to configure this feature.


Before you start, make sure you've set up your Bitcoin wallet on your Trezor. It's important to save the mnemonic, as the FIDO2 "*passwordless*" identifiers are encrypted with your seed (we'll find out how to save these identifiers correctly in the next section).


Connect the Trezor to your computer and unlock it.


![Image](assets/fr/01.webp)


Access the account you wish to secure in "*passwordless*" mode. I'll use a Bitwarden account as an example. This option is usually found in the service settings, often under a "*authentication*", "*security*" or "*password*" tab.


On Bitwarden, for example, the option is found under the "*Master password*" tab. Click on "*Turn on*" to activate authentication via FIDO2.


![Image](assets/fr/11.webp)


You will often be asked to confirm your password.


![Image](assets/fr/12.webp)


Your account details will appear on the Trezor screen. Touch the screen or press the button to confirm. You'll also need to confirm your PIN code.


![Image](assets/fr/13.webp)


On the site, add a name to remember your security key, then click on "*Turn on*".


![Image](assets/fr/14.webp)


You will then be asked to identify yourself to check that the key is working properly.


![Image](assets/fr/15.webp)


From now on, when logging in to your account, it will no longer be necessary to enter your email address or login. Simply click on the button to authenticate yourself with a physical key on the login form.


![Image](assets/fr/16.webp)


Confirm the connection to your Trezor by entering your Hardware Wallet PIN.


![Image](assets/fr/17.webp)


You will be connected to your account without having to enter your password.


![Image](assets/fr/18.webp)


**Please note that even if you activate "*passwordless*" authentication via FIDO2 on your Trezor, the main password for your online account will still be valid for log-in purposes**


## Save your FIDO2 credentials (credentials residents)


If you're using FIDO2 or U2F for two-factor authentication, i.e. to log in to accounts that require a password in addition to 2FA validation via your Trezor, then the mnemonic phrase alone will retrieve access to your keys. However, if you are using FIDO2 in "*passwordless*" mode as described in the previous section, it will be necessary to make a copy of your FIDO credentials in addition to backing up your mnemonic phrase which encrypts these credentials.


To do this, you'll need a computer with Python installed. Open a terminal and run the following command to install the necessary Trezor software:


```shell
pip3 install --upgrade trezor
```


Connect your Trezor to the computer via USB and unlock it using your PIN code.


![Image](assets/fr/01.webp)


To retrieve the list of FIDO2 identifiers stored on the Trezor, run the following command:


```shell
trezorctl fido credentials list
```


Confirm the export on your Trezor.


![Image](assets/fr/19.webp)


Your FIDO2 login information will be displayed on your terminal. For example, for my Bitwarden account, I got this information:


```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```


Copy and save all this information in a text file. There is no significant risk associated with this backup, other than revealing that you are using these services with FIDO2. The "*Credential ID*" is encrypted using your wallet's seed, which means that an attacker obtaining this backup would not be able to connect to your accounts, but only notice that you are using these accounts. To decrypt these IDs, you need the seed in your wallet.


You can therefore create several copies of this text file, and store them in different places, for example locally on your computer, on a file-hosting service and on external media such as a USB stick. However, bear in mind that this backup is not automatically updated, so you'll need to renew it every time you set up a new "*passwordless*" connection with your Trezor.


Now let's imagine you've broken your Trezor. To retrieve your FIDO2 credentials, you'll first need to recover your wallet using your mnemonic phrase on a new FIDO2-compatible Trezor device.


Once the recovery is complete, to import your FIDO2 identifiers on the new device, run the following command in your terminal:


```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```


Simply replace `<CREDENTIAL_ID>` with one of your identifiers. For example, in my case, this would give:


```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```


Your Trezor will prompt you to import your FIDO2 identifier. Confirm by pressing on the screen.


![Image](assets/fr/20.webp)


Your FIDO2 login is now operational on your Trezor. Repeat this procedure for each of your identifiers.


Congratulations, you're now up to speed on using your Trezor with U2F and FIDO2! If you found this tutorial useful, I'd be very grateful if you'd leave a green thumb below. Please feel free to share this tutorial on your social networks. Thank you very much!


I'd also recommend this other tutorial, in which we look at another solution for U2F and FIDO2 authentication:


https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e