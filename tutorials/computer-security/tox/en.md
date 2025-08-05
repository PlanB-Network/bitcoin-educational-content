---
name: Tox
description: Open up conversations without intermediaries on the decentralized Tox protocol
---
![cover](assets/cover.webp)


End-to-end encryption is a service offered by many messaging apps such as WhatsApp and Telegram. Encryption here means that before the message is sent by the sender, it is secured by a cryptographic lock to which only the recipient has the key. Today we're off to discover a totally decentralized, end-to-end encrypted messaging application, based on principles similar to Blockchain, to offer secure, end-to-end encrypted communication without intermediaries: Tox Chat.


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
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end encryption*


## What is Tox?


Tox is a free (open source), decentralized communications protocol that uses *Networking and Cryptography Library* (NaCl) technology plus combinations of encryption algorithms to ensure the security and confidentiality of its users. Tox lets you exchange text messages, make audio and video calls, share files and share your screen with friends securely, decentralized and without intermediaries.


The technology that the Tox protocol uses is similar to peer-to-peer networks such as blockchains, which favors the decentralization of the protocol's infrastructure. Unlike social networks and end-to-end encrypted messaging applications, the Tox Chat application is built on a decentralized protocol that has no central server. All users communicate in an intermediary-free, censorship-resistant peer-to-peer network. To communicate, each user is identified by a unique ID (ToxID) derived from his or her public key, which is stored in a distributed Hash table.


## Join Tox


You can use the Tox protocol through an instant messaging client that you can download from the [Tox Chat site](https://tox.chat).


![download](assets/fr/01.webp)


Depending on your operating system, you can download and install a Tox client that matches :



- aTox: [aTox](https://github.com/evilcorpltd/aTox), a Tox client written in Kotlin available only on Android


![aTox](assets/fr/02.webp)



- qTox: A Tox client from [open source](https://github.com/TokTok/qTox) based on the Qt Framework (C++) available on Windows, Linux, MacOs.


![qTox](assets/fr/03.webp)



- Toxic: [Toxic](https://github.com/JFreegman/toxic) is a Tox client written in C and running on systems with command-line interfaces.


![Toxic](assets/fr/04.webp)


In this tutorial, we'll use qTox clients on Windows and aTox to communicate.


## Getting started with qTox


Once downloaded, install your Tox client and create your profile.


![qTox-acount](assets/fr/05.webp)


Congratulations, you've just joined the Tox protocol. On the qTox software, you can find your profile information by clicking on your user name.


![profil](assets/fr/06.webp)


In particular, you'll find your Tox ID, which you can save as a QR code and share with people who want to get in touch with you.


Export your Tox profile file so that you have a backup of your profile and contact information that you can use to restore. Click on the **Export** button, then choose the path to your backup file.


![export](assets/fr/07.webp)


From the **More** menu, add friends, import contacts and manage the friend requests you receive.


![friends](assets/fr/08.webp)


You can reach me via this Tox ID for example: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F


Once the friend request has been sent, the recipient will have to accept or reject your request before you can contact them.


![request](assets/fr/09.webp)


Your Tox client includes all the options offered by instant messaging applications:



- Video calls



- Voice calls



- File sharing



- emojis


![chat](assets/fr/10.webp)


### Peer-to-peer groups


Your Tox clients also enable you to communicate with a group of people in a completely decentralized way: these are called conferences. In the **Groups** menu, create a new conference or consult the list of invitations to join conferences you've received.


![conferences](assets/fr/11.webp)


Once the conference has been created, you can invite your friends to join the conference on your Tox client. In your list of friends, right-click on the username of the friend you wish to invite. Click on the **Invite to conference** option, then select the conference name you've created. You can also invite a friend by implicitly creating a conference with the **Create a new conference** option.


⚠️ Tox clients are still under development, so you may encounter errors when interacting with the software. Conferencing and video calling functionalities are not yet available on the Tox Android client (aTox).


![invite](assets/fr/12.webp)


### File transfers


In the **File transfers** menu, you'll find a history of the files you've sent and those you've received from your contacts.


![files](assets/fr/13.webp)


You can also customize your file-sharing configurations for each discussion you have. Right-click on your recipient's username and select "Show more details".


![details](assets/fr/14.webp)


From the Interface details, you can manage the authorizations you grant to your recipient for :



- Automatic acceptance of conference invitations.



- Automatic file acceptance.



- Backup paths for your discussion files.


![permissions](assets/fr/15.webp)


### More parameters


In the **Settings** menu, you can customize your Tox client's settings.



- In the **General** section, change the basic language of your Tox client, define the file backup paths and the maximum file size to be accepted automatically.


![general](assets/fr/16.webp)



- In the **Interface user** section, modify the fonts and sizes of your messages. You can also change the theme of your Tox client.


![ui](assets/fr/17.webp)



- The **Privacy** tab lets you define ephemeral messages by unchecking the "Keep chat history" box. You can also change your Nospam code when you notice you're being spammed by friend requests by clicking on the "Generate random NoSpam code" button.


![privacy](assets/fr/18.webp)


### What guarantees confidentiality on Tox?


The Tox protocol uses the Distributed Hash Table to create a network of decentralized nodes. Each Tox client is part of the DHT network and stores information about other nodes. In the case of Tox, the DHT stores IP addresses as values associated with Tox public keys (Tox ID). This makes it easy to search for a Tox Client device without having to query a central server.


Imagine writing to our user `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` whom we'll name **user B**. Your Tox client will locate this identifier in the Hash Distributed table and retrieve the associated IP address. Once the IP address has been found, your Tox client will create a direct, encrypted communication channel with our **user B**'s machine, or use other nodes as relays to reach **User B**. Encryption algorithms ensure that, regardless of the communication channel, only **User B** will be able to read the contents of your message.


If you've enjoyed discovering Tox and have been able to understand how it's useful for strengthening your privacy, please feel free to give this tutorial a thumbs-up. We also recommend our tutorial on Simple Login, a tool that lets you receive and send e-mails anonymously.


https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41