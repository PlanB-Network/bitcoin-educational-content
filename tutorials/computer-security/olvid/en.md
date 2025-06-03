---
name: Olvid
description: Private messaging for everyone
---
![cover](assets/cover.webp)


Olvid is a French instant messaging application launched in 2019, designed to offer a high level of security, without compromising on privacy. Unlike WhatsApp or Signal, Olvid asks for no personal data on registration: no phone number, no email, nothing. Identification between users is based on an exchange of keys, with no directory server or shared address book.


All messages are encrypted end-to-end using an original cryptographic protocol, designed to protect metadata too: nobody knows who you're talking to, or when. Client code is open source, but the central server used to route encrypted messages remains proprietary and hosted on AWS.


Olvid offers a free version and a subscription version at €4.99 per month. The free version offers full functionality, with the exception of making audio and video calls (although it is possible to receive them), and does not allow account synchronization across multiple devices. So if you're planning to use your smartphone exclusively, and don't need to make calls, Olvid is an excellent solution.


Olvid is certified by ANSSI (the French cybersecurity authority). This application is an excellent alternative to traditional messaging services (WhatsApp, Facebook Messenger, WeChat...) for those seeking privacy while retaining simplicity of use.


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
| **Olvid**                | **✅**              | **✅**              | **✅**                   | **✅**                          | **❌**                           | **❌**                    | **2019**              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end encryption*


## Install the Olvid application


Olvid is available on all platforms. You can download the application directly from your phone's app store:


- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);


On Android, it is also possible to [install via APK](https://www.olvid.io/download/).


In this tutorial, we'll be concentrating on the mobile version, but please note that [computer versions are also available](https://www.olvid.io/download/) (MacOS, Linux and Windows). If you choose the paid version, you'll be able to synchronize your account on multiple devices.


![Image](assets/fr/01.webp)


## Create an account on Olvid


When you launch the application for the first time, click on the "*I am a new user*" button.


![Image](assets/fr/02.webp)


Choose a nickname or enter your first and last name.


![Image](assets/fr/03.webp)


Add a profile photo.


![Image](assets/fr/04.webp)


Your account is now created.


![Image](assets/fr/05.webp)


To prevent any loss of access to your Olvid account, we recommend setting up automatic backups. To do this, open the settings by clicking on the three dots at the top right of Interface, then select "*Settings*".


![Image](assets/fr/06.webp)


Go to the "*Save keys and contacts*" menu.


![Image](assets/fr/07.webp)


Then click on "*Generate a backup key*". This key will encrypt your backups. If you need to recover your account on another device and no longer have access to it, you'll need both a backup and this key to decrypt it.


![Image](assets/fr/08.webp)


Keep this key in a secure place. You can also make a paper copy.


![Image](assets/fr/09.webp)


You can then choose to create a local backup or an automatic backup on a cloud service. This second option is highly recommended to guarantee access to your Olvid account in all circumstances, even if you lose your phone.


![Image](assets/fr/10.webp)


Make sure the "*Enable automatic backup*" option is checked.


![Image](assets/fr/11.webp)


You can also explore the other settings available to customize the application to your needs.


![Image](assets/fr/12.webp)


## Sending messages with Olvid


To be able to send messages, you must first add contacts. From the home page, click on the blue "*+*" button.


![Image](assets/fr/13.webp)


Olvid then displays your user ID. You can then pass it on to the people you wish to communicate with, so that they can add you as a contact.


To add a person, scan their ID with your camera, or paste it in manually by clicking on the three small dots in the top right-hand corner.


![Image](assets/fr/14.webp)


Once the ID has been scanned, you can either have your contact scan the QR code displayed, or send them a remote connection request by clicking on "*Remote contact*".


![Image](assets/fr/15.webp)


The connection is now established.


![Image](assets/fr/16.webp)


You can now start exchanging messages and other content with your correspondent!


![Image](assets/fr/17.webp)


From the home page, you'll find all your conversations.


![Image](assets/fr/18.webp)


The second tab contains all your contacts.


![Image](assets/fr/19.webp)


You can also create group discussions.


![Image](assets/fr/20.webp)


Congratulations, you're now up to speed on using Olvid messaging, a great alternative to WathsApp! If you found this tutorial useful, I'd be very grateful if you'd leave a green thumb below. Please feel free to share this tutorial on your social networks. Thank you very much!


I also recommend this other tutorial, in which I introduce you to Proton Mail, a much more privacy-friendly alternative to Gmail :


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2