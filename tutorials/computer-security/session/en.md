---
name: Session
description: Send encrypted messages, not metadata
---
![cover](assets/cover.webp)


Session is an encrypted messaging application created in 2020, designed to offer a higher level of confidentiality than traditional messaging. It was first developed by the *Oxen Privacy Tech Foundation*, then by the *Session Technology Foundation*.


Session boasts some interesting technical features: end-to-end encryption of messages, a decentralized network organized to guarantee availability and redundancy, and Tor-inspired onion routing. Also, unlike WathsApp or Signal, which require a telephone number for registration, Session asks for no personal information (no number, no email, just a pair of cryptographic keys).


Session lets you send messages, files, voice messages, audio calls, as well as groups of up to 100 members (and communities beyond that), while minimizing metadata leaks.


![Image](assets/fr/01.webp)


Session is aimed above all at users who place confidentiality at the heart of their priorities. This messaging service represents a serious alternative to WhatsApp, with an architecture designed to withstand modern surveillance models.


| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end encryption*


## Install the Session application


Session is available on all platforms. You can download the application directly from your phone's application store:


- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).


On Android, it is also possible to [install via APK](https://github.com/session-foundation/session-android/releases).


In this tutorial, we'll concentrate on the mobile version, but please note that [computer versions are also available](https://getsession.org/download) (MacOS, Linux and Windows). Later on, we'll look at how to synchronize an account across multiple devices.


## Create an account on Session


On first launch, click on "*Create account*".


![Image](assets/fr/02.webp)


Choose a display name for your profile. This can be a pseudonym or your real name.


![Image](assets/fr/03.webp)


You will then have to choose between two notification management modes:



- Fast mode ("*Firebase Cloud Messaging/Apple Push Notification Service*"): enables you to receive message notifications in near real time, thanks to the notification services provided by Google or Apple (depending on your system). For this to work, your IP address and a unique notification ID are transmitted to Google or Apple, and the Session account ID is also registered with an STF server (via Tor). This mode involves (admittedly minimal) exposure of metadata, but does not compromise message content or contacts, and does not allow your actual activity to be traced. This mode is therefore more efficient in terms of responsiveness, but relies on a centralized infrastructure and is slightly less effective in terms of confidentiality.



- Slow mode (*background polling*): the Session application remains active in the background, periodically polling the network for new messages. This approach guarantees greater confidentiality than the first, as no data is transmitted to third-party servers; neither Google, Apple nor STF servers receive any information. On the other hand, this mode has two drawbacks: notifications can be delayed (up to several minutes), and energy consumption is generally higher due to application activity in the background.


![Image](assets/fr/04.webp)


You are now connected to the Session application and can start exchanging messages.


![Image](assets/fr/05.webp)


## Save your Session account


The first thing to do before you start using Session is to save your account so that you can restore it if you lose your device. To do this, click on the "*Continue*" button next to "*Save your recovery password*".


![Image](assets/fr/06.webp)


Session will then display a mnemonic phrase. Copy it carefully and keep it in a secure place. This phrase provides full access to your Session account, so it's important not to divulge it. You'll need it to access your account on another device, especially if your current phone is lost or replaced.


![Image](assets/fr/07.webp)


This phrase works in a similar way to the mnemonic phrases used in Bitcoin wallets. I therefore recommend that you consult this other tutorial, in which I explain the best practices for saving a mnemonic phrase:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Please note**: Unlike the mnemonic phrases used on Bitcoin wallets, on Session, **you absolutely must save each word in its entirety**. The first 4 letters are not enough!


## Setting up the Session application


To access the application settings, click on your profile photo at the top left of Interface. This is where you can add a profile photo.


![Image](assets/fr/08.webp)


In the "*Privacy*" menu, you can enable or disable various features (beware, some may expose your IP address). I also recommend activating the "*Lock App*" option, which requires authentication to access the application.


![Image](assets/fr/09.webp)


In the "*Notification*" menu, you'll find a choice between "*Fast Mode*" and "*Slow Mode*" (see previous parts of the tutorial). You can also customize notifications to suit your preferences.


![Image](assets/fr/10.webp)


Finally, go to the "*Appearance*" menu to adapt Interface to your taste. The "*Recovery Password*" menu allows you to retrieve your mnemonic phrase if you wish to make a new backup.


![Image](assets/fr/11.webp)


## Sending messages with Session


To contact other people, click on the "*+*" button on the home page.


![Image](assets/fr/12.webp)


Several options are available. If you wish to create or join a group, select "*Create Group*" or "*Join Community*".


![Image](assets/fr/13.webp)


If you want someone to add you as a contact, you can have them scan your Session ID as a QR code.


![Image](assets/fr/14.webp)


To send your login remotely, click on "*Invite a Friend*". You can then copy your Session ID and send it via another communication channel. You can also retrieve this information by clicking on your profile photo from the home page.


![Image](assets/fr/15.webp)


If you have another person's Session ID and wish to add it, click on "*New Message*".


![Image](assets/fr/16.webp)


You can then paste its identifier in text, or scan it directly if you have it as a QR code.


![Image](assets/fr/17.webp)


Then send an initial message to this person.


![Image](assets/fr/18.webp)


As soon as the person accepts your request, you'll see their username appear, and you'll be able to chat freely with them.


![Image](assets/fr/19.webp)


## Synchronize Desktop software


To synchronize your account on your computer, you need to install the software. [Download it from the official website](https://getsession.org/download). I advise you to check its authenticity and integrity before installing it.


![Image](assets/fr/20.webp)


On first launch, click on "*I have an account*".


![Image](assets/fr/21.webp)


Enter your mnemonic phrase, making sure to leave a space between each word.


![Image](assets/fr/22.webp)


You can now access your conversations from your computer.


![Image](assets/fr/23.webp)


Congratulations, you've now got the hang of using Session messaging, an excellent alternative to WathsApp!


I also recommend this other tutorial, in which I present Threema, another interesting alternative for your messaging application:


https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74