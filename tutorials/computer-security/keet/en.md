---
name: Keet
description: Peer-to-peer chat
---
![cover](assets/cover.webp)


Keet is an instant messaging application designed to work without any servers. Launched in 2022 by Holepunch (a company financed by Tether and Bitfinex), the application is based entirely on a peer-to-peer network and features a radically decentralized approach: messages, calls and files are exchanged directly between users, with no intermediaries.


Keet encrypts all communications end-to-end and asks for no personal data. Registration is anonymous, with no phone number or email required. In addition to exchanging text messages, Keet offers very high quality video calls, as well as unlimited file sharing. The application can therefore be used in a hybrid way, for both personal and professional use.


![Image](assets/fr/01.webp)


At the moment (April 2025), Keet is not entirely open-source. Some of the source code is available on [Holepunch's GitHub repository](https://github.com/holepunchto), notably the cryptographic and network components, but the client Interface is not yet. Holepunch has, however, announced its intention to make the entire application open-source eventually. Depending on when you discover this tutorial, this may already have been done.



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


## Install Keet


Keet is available on all platforms. You can download the application directly from your phone's app store:


- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);


On Android, it is also possible to [install via APK](https://github.com/holepunchto/keet-mobile-releases/releases).


In this tutorial, we'll be concentrating on the mobile version, but please note that [computer versions are also available](https://keet.io/) (MacOS, Linux and Windows). It's also possible to synchronize your account on multiple devices.


## Create an account on Keet


On first launch, you can ignore the presentation screens.


![Image](assets/fr/02.webp)


Click on the "*I'm a new user*" button.


![Image](assets/fr/03.webp)


Accept the terms of use, then click on "*Quick setup*".


![Image](assets/fr/04.webp)


Choose a name or nickname, then click on "*Finish setup*".


![Image](assets/fr/05.webp)


Your profile is now created. Click "*Finish setup*" again to finalize.


![Image](assets/fr/06.webp)


You can customize your profile at any time from the "*Profile*" tab.


## Save your Keet account


The first thing to do with your new Keet account is to save your recovery phrase. This is a sequence of 24 words that will enable you to restore access to your account in the event of loss or change of device. This phrase gives full access to your account to anyone who knows it, so it's important to make a reliable backup and never divulge it.


To do this, click on the "*Profile*" tab at the bottom right of the Interface.


![Image](assets/fr/07.webp)


Then access the "*Settings*" menu.


![Image](assets/fr/08.webp)


Select "*Privacy and Security*".


![Image](assets/fr/09.webp)


Then click on "*Recovery phrase*".


![Image](assets/fr/10.webp)


Press the "*View phrase*" button to display your recovery phrase. Copy it carefully and keep it in a safe place.


![Image](assets/fr/11.webp)


## Sending messages with Keet


To communicate on Keet, you need to create "*Rooms*". To do this, click on the pencil icon at the top right of the Interface.


![Image](assets/fr/12.webp)


Select "*New group chat*".


![Image](assets/fr/13.webp)


Choose a name and description for your "*Room*", then click on "*Create group chat*".


![Image](assets/fr/14.webp)


Your "*Room*" is now created. Click on the "*+*" icon at top right to invite participants.


![Image](assets/fr/15.webp)


Define the rights you grant to new members via the invitation link, as well as the duration of the link's validity. Then click on "*generate invite*".


![Image](assets/fr/16.webp)


Keet will generate a link to join your "*Room*". You can either copy it and share it, or have its QR code scanned by the people you wish to invite.


![Image](assets/fr/17.webp)


You can now start exchanging messages and multimedia files. To launch a call, click on the phone icon in the top right-hand corner.


![Image](assets/fr/18.webp)


From this group, you can also send private messages to a specific member. Click on the group's profile picture, then select the desired member in the "*Members*" section.


![Image](assets/fr/19.webp)


Click on the "*Send DM request*" button and enter your message.


![Image](assets/fr/20.webp)


Once the DM request has been accepted, you'll find this contact on the home page, where you can talk to him privately.


![Image](assets/fr/21.webp)


## Synchronize your account on multiple devices


Now that you know how to use Keet and have an account, you can also synchronize it on another device, such as a computer. To do this, open the application on your mobile, then click on "*Profile*" and access "*Settings*".


![Image](assets/fr/22.webp)


Then go to the "*My devices*" menu.


![Image](assets/fr/23.webp)


Click on "*Add device*". Keet will generate a link to synchronize a new device. Copy this link.


![Image](assets/fr/24.webp)


On your second device, install Keet. On the home screen, select the "*I'm a current user*" option.


![Image](assets/fr/25.webp)


Then click on "*Link device*".


![Image](assets/fr/26.webp)


Paste the link provided by your first device, then click on "*Start syncing*".


![Image](assets/fr/27.webp)


On your first device, click on "*Confirm link devices*" to authorize the connection.


![Image](assets/fr/28.webp)


On the second device, complete the process by clicking on "*Link devices*".


![Image](assets/fr/29.webp)


You can now access all your "*Room*" and conversations from this new device.


![Image](assets/fr/30.webp)


Congratulations, you're now up to speed on using Keet messaging, a great alternative to WathsApp! If you found this tutorial useful, I'd be very grateful if you'd leave a green thumb below. Feel free to share this tutorial on your social networks. Thank you very much!


I also recommend this other tutorial, in which I introduce you to Proton Mail, a much more privacy-friendly alternative to Gmail :


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2