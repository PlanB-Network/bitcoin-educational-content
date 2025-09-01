---
name: Jami
description: Share freely and confidentially.
---

![cover](assets/cover.webp)


Jami is a free, open-source peer-to-peer messaging program with a long history and a wide range of features. Its history goes back to December 2004, when Montreal-based *Savoir-faire Linux* launched SFLPhone, a digital telephony project for businesses based entirely on open-source technologies. The software, which complied with telecommunications standards (SIP and IAX), stood out for its ability to handle large numbers of lines and calls.


In 2015, SFLPhone was renamed Ring, and integrated a distributed architecture no longer requiring a central server. The following year, Ring officially joined the GNU project, strengthening its foothold in the free software ecosystem. Finally, in December 2018, to avoid confusion with commercial products using the English term "*Ring*", the software adopted its current name: Jami. Since then, it has continued to evolve as a free, decentralized and privacy-friendly communication platform.


Today, Jami is available on many systems. It's renowned for its performance, fluidity and ease of use. It lets you communicate via instant messaging, audio calls or video calls, while ensuring the confidentiality of your conversations through end-to-end encryption. Simple installation and a host of features make it a complete communications application that's easy and convenient to use on a daily basis.


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
| **Jami**                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end encryption*



## Why use Jami?



- It's open-source and totally free**, so you can use it at no cost.
- Complete with useful features**: this software lets you take advantage of numerous options, thanks to the ability to add plugins easily from the store. It's even possible to create your own extensions for features more suited to your needs.
- Easy to use and Interface intuitive**: despite the many features Jami has to offer, it's still very easy to get to grips with.
- Strong security**: Jami incorporates an advanced encryption algorithm that guarantees the security of your communications while respecting your privacy.
- Highly accessible and fast**: it offers easy communication even when bandwidth is limited, for enhanced user-friendliness.


## How do I install Jami?


Before moving on to installing Jami, it's important to note that the application is available on different operating systems. Its installation will therefore depend on the system you're using.


![0_01](assets/fr/01.webp)


### For Android or iOS users


The application is available directly from the App Store or Play Store. Simply search for it in the search bar, then launch the installation.


### For Windows or macOS users


To install Jami on your device, you first need to visit the official Jami website. By default, the site displays the software corresponding to your device's operating system, and you can click directly on the download button to launch it. However, you can also download the Windows executable directly from the [download page](https://jami.net/download-jami-windows/).


![0_02](assets/fr/02.webp)


For macOS users, the file is also available from [macOS download page](https://jami.net/download-jami-macos/).


![0_03](assets/fr/03.webp)


Once you've downloaded the executable, start the installation process by double-clicking on it. Accept the terms of use, then start the installation and wait for it to finish.


![0_04](assets/fr/04.webp)


![0_05](assets/fr/05.webp)


### For linux users


To install Jami on Linux, it's best to use the command line. It's important to note that Jami is available for different Linux distributions. Before you start installing Jami, make sure you choose the right distribution for your system.


Once you've selected your distribution, you can install the system. You'll need to install the dependencies required to run Jami on your Linux OS. The commands are directly available on [this page](https://jami.net/download-jami-linux/).


![0_06](assets/fr/06.webp)


To install Jami on **Ubuntu**, you can do it as follows:


```shell
sudo apt install gnupg dirmngr ca-certificates curl --no-install-recommends
```


This command installs the tools needed to manage GPG keys (gnupg and dirmngr), SSL certificates (ca-certificates) and the curl download tool.


https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

```shell
curl -s https://dl.jami.net/public-key.gpg | sudo tee /usr/share/keyrings/jami-archive-keyring.gpg > /dev/null
```


Here, curl is used to download Jami's GPG public key. The redirection to /dev/null avoids displaying the raw key on the screen.


```shell
sudo sh -c "echo 'deb [signed-by=/usr/share/keyrings/jami-archive-keyring.gpg] https://dl.jami.net/stable/ubuntu_25.04/ jami main' > /etc/apt/sources.list.d/jami.list"
```


This command adds the official Jami repository to the list of APT sources.


```shell
sudo apt-get update && sudo apt-get install jami
```


Finally, update the list of available packages with `apt-get update`, then install Jami directly from the official repository with `apt-get install jami`.


## Jami basic configuration


Once Jami has been installed on your system, you can launch it directly from the system menu.


Once you've started the application, you'll have the option of creating an account or continuing with one you've already created.


![0_07](assets/fr/07.webp)


### Create an account


Creating a Jami account is relatively simple. You don't need an e-mail address or telephone number: Jami collects only the minimum of information. If you wish, you can register a username (alias) that points to your *Jami ID* (cryptographic fingerprint). The *alias ↔ Jami ID* association is published on a default name server (replaceable / self-hosting), so the alias is not necessarily mandatory.


![0_08](assets/fr/08.webp)


To protect your data locally, you can set a password to encrypt your profile and backups on the device. This password is optional and has no effect on end-to-end encryption of communications, which is active by default. If you activate this local protection, choose a long, random and unique password, then validate.


![0_09](assets/fr/09.webp)


After encrypting your account, set your full name.


![0_10](assets/fr/10.webp)


![0_11](assets/fr/11.webp)


## Login to an existing account


Jami does not use **identifiers** and has no database to connect to your account. All your data is stored directly on your device. In order to connect to your old account, you need to perform a **backup** of your old account.


Go to **Settings**, then **Account**, then **Account Management**. Scroll to the bottom and perform a **backup of your account**. Choose the location where the backup file will be saved, enter the **password** defined when your account was created, then validate.


![0_12](assets/fr/12.webp)


This backup file will enable you to reconnect to your account.


![0_13](assets/fr/13.webp)


### Connection via archive


To do this, click on the **Import from a backup archive** button, and select the backup file for your Jami account.


![0_14](assets/fr/14.webp)


If you set a password when you created your account, enter it and confirm. Your data and messages will appear automatically.


![0_15](assets/fr/15.webp)


It's important to make regular back-ups of your account to keep your data up to date and ensure you don't lose your latest messages.


### Connection via a device


If you're already logged in on another device with your Jami account, go to **Account** then to the **Connected device** section and click on **Connect a new device**. The QR code reader will appear, along with a field for entering a connection code.


![0_16](assets/fr/16.webp)


Launch Jami on the new device and select **I already have an account** then **Import from another device**. You'll then get a **QR code** and a login code. To connect, you can use the QR code scanner to scan the code displayed on the other device. However, it's often simpler to copy the connection code and paste it directly into the field provided.


![0_17](assets/fr/17.webp)


If you set a password when you created your account, you'll need to enter it on the new device to continue.


![417](assets/fr/18.webp)


Confirm the connection on the device already connected to continue.


![0_19](assets/fr/19.webp)


Once the password has been entered, the device will automatically connect to the account and synchronize. You can then send and receive messages from any of your devices.


## Add an extension to Jami


One of Jami's interesting features is its ability to integrate new options via extensions (plugins). Plugins are native modules (C/C++); the SDK provides tools and scripts (notably in Python) to help create them. Some plugins are available directly [here](https://jami.net/extensions/).


To install an extension, on Desktop open the integrated extension store, download the appropriate plugin, then go to **Settings → Extensions → Install** and activate it. On Android, the store is not integrated: download the `.jpl` file, then import it manually from **Settings → Extensions → Install**; the import is automatic and you can then activate it and adjust its settings if necessary.


![0_20](assets/fr/20.webp)


To develop your own plugins, check out the blog post **[Discover the Jami Plugin SDK and create your own plugins](https://jami.net/plugins-sdk/)**.


## Advanced features


Jami also offers **advanced features** for users wishing to go further in configuring and using the application. These options include:



- Create a rendezvous point**: This feature lets you create a **rendezvous point** for your communications, useful for organizing secure sessions or exchanges between several users.
- Connect to a Jami server**: You can connect Jami to a **Jami server**, which can improve the performance or availability of communications, especially in professional environments.
- Set up a SIP account**: You can set up a **SIP account** (Session Initiation Protocol), enabling you to integrate Jami with existing telephone systems or make telephone calls.


![0_21](assets/fr/21.webp)


These options are designed for more advanced users who wish to customize their Jami experience and take advantage of additional features for specific needs.


In short, Jami is a complete, secure and flexible communications solution, suitable for both personal use and more specific needs thanks to its **extensions**. Its simple installation, intuitive handling and advanced features such as **encryption**, **multi-device synchronization** and the ability to **create your own plugins** make it a powerful tool for managing your communications while preserving your **privacy**.


Discover Tox, a decentralized protocol that combines end-to-end encryption (E2E), public keys and many other algorithms to offer you optimal communication that protects your confidentiality through its various clients.


https://planb.network/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3