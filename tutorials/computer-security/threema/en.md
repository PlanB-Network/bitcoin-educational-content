---
name: Threema
description: Secure, anonymous instant messaging
---
![cover](assets/cover.webp)


Founded in 2012 in Switzerland, Threema is an instant messaging app designed to guarantee privacy and security. Unlike WhatsApp, Telegram or Signal, Threema requires no phone number or e-mail address to create an account. Each user has a unique identifier, enabling completely anonymous registration.


On the technical side, communications over Threema are end-to-end encrypted. The mobile application code has been open source since 2020, but the server infrastructure remains proprietary and centralized. Servers are hosted exclusively in Switzerland (a country renowned for its legal framework for data protection).


![Image](assets/fr/01.webp)


Threema has basic clients for Android and iOS. There is also a web application, as well as software available for Windows, Linux and macOS. However, to use them, you must first register on a mobile device.


The Threema application is not free. It works on a one-off purchase model: €5.99 to use the app for life (or €4.99 if you buy it direct). To really use Threema anonymously, payment needs to be anonymous too. That's why you can buy an activation key in bitcoins or cash on the "*Threema Shop*" to activate the Android version. On iOS, on the other hand, the purchase must go through the App Store, due to Apple's restrictions on app monetization.


There's also a dedicated business version called "*Threema Work*". In this tutorial, we'll concentrate on the home version.


| Application          | E2EE 1:1       | E2EE groups    | Anonymous registration | Open-source client license | Open-source server license | Decentralized server | Year of creation  |
| -------------------- | -------------- | -------------- | ---------------------- | -------------------------- | -------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                      | ❌                          | ❌                          | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optional) | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Telegram             | 🟡 (optional) | ❌              | 🟡                     | ✅                          | ❌                          | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                      | ✅                          | ✅                          | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                      | ✅                          | ❌                          | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                      | ✅                          | ✅                          | 🟡 (federated)      | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                      | ✅                          | N/A                        | 🟡 (via email)      | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                      | ✅                          | ✅                          | 🟡 (federated)      | 2014              |
| Session              | ✅              | ✅              | ✅                      | ✅                          | ✅                          | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                      | ✅                          | ✅                          | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                      | ✅                          | ❌                          | 🟡(no directory)     | 2019              |
| Keet                 | ✅              | ✅              | ✅                      | ❌                          | N/A                        | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2013              |

*E2EE = End-to-end encryption*


## Install the Threema application


Threema is available on all platforms. You can download the application directly from your phone's app store:


- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).


On Android, it is also possible to [install via APK](https://shop.threema.ch/en/download).


There are also [computer versions](https://threema.ch/download) (MacOS, Linux and Windows). This tutorial will show you how to synchronize them.


## Buy Threema license


Once you've installed the application, if you've gone directly through an app store, you've already paid for the license and should have immediate access to it. If you went through F-Droid or the APK, you now need to purchase a license on the official website.


[Go to the "*Threema Shop*"(https://shop.threema.ch/) and click on the "*Buy Threema for Android*" button.


![Image](assets/fr/02.webp)


Select the number of licenses you wish to purchase (just one if it's just for you), choose the currency, and select the license delivery method. You can choose to receive the license by e-mail, or directly on the site if you wish to remain anonymous. Then click on "*Proceed to payment*".


![Image](assets/fr/03.webp)


Choose your payment method. In my case, I'm going to pay in bitcoins, which I also recommend you do, as it allows you to remain anonymous (provided you use Bitcoin appropriately) and is much more convenient than a remote cash payment. Then click on "*Next*".


![Image](assets/fr/04.webp)


If you don't need an invoice, click "*Next*" again without entering any personal information.


Then confirm your purchase by clicking on "*Confirm payment*".


![Image](assets/fr/05.webp)


You'll then need to send the amount indicated to the Bitcoin address provided (unfortunately, Lightning is not yet supported). Once the transaction has been confirmed on the Blockchain, click on "*Close*" next to the invoice.


You will then have access to your license key. Please note: if you haven't entered an e-mail address, this key will only be displayed here. Remember to save the URL of the page so that you can access it later if necessary.


![Image](assets/fr/06.webp)


## Create an account on Threema


Now that you have your license key, you can finally launch the application. On first launch, if you haven't purchased Threema via an application store, you'll be asked to enter your license key, purchased on the site.


![Image](assets/fr/07.webp)


Then click on the "*Set up now*" button.


![Image](assets/fr/08.webp)


Move your finger across the screen to generate a source of entropy, needed to create your "*Threema ID*".


![Image](assets/fr/09.webp)


Your "*Threema ID*" will then be displayed. It will enable you to contact other users. Click on "*Next*".


![Image](assets/fr/10.webp)


Choose a password. It will enable you to restore access to your account should the need arise. Make your password as long and random as possible, and keep a secure copy of it, for example in a password manager.


![Image](assets/fr/11.webp)


Then choose a username, which can be either your real name or a pseudonym.


![Image](assets/fr/12.webp)


You can then link your Threema ID to your telephone number. This makes it easier for you to search through your contacts, but if you use Threema, it's also to preserve your anonymity: so it's best not to link it. Click on "*Next*".


![Image](assets/fr/13.webp)


Once you have completed this step, click on "*Finish*".


![Image](assets/fr/14.webp)


You are now connected to Threema and can start communicating.


![Image](assets/fr/15.webp)


## Set up Threema


First of all, access the settings by clicking on the three small dots in the top right-hand corner, then select "*Settings*".


![Image](assets/fr/16.webp)


In the "*Privacy*" tab, you'll find several options to adjust to your needs:


- Synchronizing the contacts on your phone ;
- Accepting messages from unknown people;
- Writing indicator during data entry ;
- Notice of receipt of messages..


![Image](assets/fr/17.webp)


In the "*Security*" tab, I recommend activating the "*Locking mechanism*" option to protect access to the application. It is also advisable to activate passphrase to secure your local backups.


![Image](assets/fr/18.webp)


Feel free to explore the other sections of the settings to customize the application to your preferences.


![Image](assets/fr/19.webp)


## Backing up your Threema account


Before you start exchanging messages, it's important to plan a way of recovering your account, especially if your phone is changed or lost. To do this, click on the three dots at the top right of the Interface, then access the "*Backups*" menu.


![Image](assets/fr/20.webp)


Here you will find two options for backing up your data:


- "*Threema Safe*";
- "*Data Backup*".


"Threema Safe* saves all your account information, except your conversations, on Threema's servers. This data is encrypted with the password you chose when you created your account, ensuring that Threema has no access to it. Backups are made automatically and regularly.


With "*Threema Safe*", to recover your account on a new device, all you need to do is enter your "*Threema ID*" and your password. If either of these two pieces of information is missing, it will be impossible to restore your account.


This option only allows you to retrieve your ID, profile, contacts, groups and certain settings, but **not your conversation history**.


To activate "*Threema Safe*", simply check the option in the "*Backups*" menu.


![Image](assets/fr/21.webp)


If you also want to back up and restore your conversation history, you'll need to use the "*Data Backup*" option. This generates a full backup of your account, stored locally on your phone. You'll need to transfer this backup to your new device and use your password (and possibly your passphrase) to restore your entire account.


Since this backup is only local, it needs to be regularly copied to external media. Otherwise, if your device is lost, recovery will be impossible. This method is therefore best suited to a planned transfer from one device to another, rather than to emergency situations.


Please note: "*Data Backup*" only works if you're using the same operating system. You won't be able to use it, for example, to migrate from a Samsung to an iPhone.


## Customize your Threema profile


In the top left-hand corner of Interface, click on your profile picture, then select "*My Profile*".


![Image](assets/fr/22.webp)


Here you can customize your profile: add a photo, choose who can see it, or view your Threema login.


![Image](assets/fr/23.webp)


## Synchronize PC software


If you want to access your conversations on your PC, you can synchronize your Threema account with the dedicated software. Download the software for your operating system [from the official website](https://threema.ch/en/download).


![Image](assets/fr/24.webp)


On your phone, click on the three dots at top right, then open the "*Threema 2.0 for Desktop*" menu.


![Image](assets/fr/25.webp)


Click on "*Add device*", then use your phone to scan the QR code displayed by the software on your computer.


![Image](assets/fr/26.webp)


To confirm synchronization, click on the emoji group displayed in the software.


![Image](assets/fr/27.webp)


On your computer, log in using your password.


![Image](assets/fr/28.webp)


In addition to the mobile application, you can now access your Threema account directly from your computer.


![Image](assets/fr/29.webp)


## Sending messages with Threema


Now that everything is set up correctly, you can start communicating. Click on the "*Start chat*" button.


![Image](assets/fr/30.webp)


Select "*New contact*".


![Image](assets/fr/31.webp)


Enter or scan your correspondent's "*Threema ID*".


![Image](assets/fr/32.webp)


Click on the message icon.


![Image](assets/fr/33.webp)


Send a first message to your correspondent.


![Image](assets/fr/34.webp)


When your correspondent answers, the connection will be established, and you'll be able to see his or her name and profile photo. You can then exchange messages, multimedia files and even make calls.


![Image](assets/fr/35.webp)


Congratulations, you're now up to speed on using Threema messaging, a great alternative to WathsApp! If you found this tutorial useful, I'd be very grateful if you'd leave a green thumb below. Feel free to share this tutorial on your social networks. Thank you very much!


I also recommend this other tutorial, in which I introduce you to Proton Mail, a much more privacy-friendly alternative to Gmail :


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2