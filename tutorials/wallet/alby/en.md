---
name: Alby

description: Browser extension for Bitcoin and Lightning Network
---

![cover](assets/cover.webp)



Making payments increasingly easy with bitcoin is the challenge facing many companies in the sector. Alby stands out from the crowd with its Alby wallet extension for browsers. This extension aims to set up a fluid framework that automatically detects addresses and allows you to make frictionless bitcoin payments. In this tutorial, we discover the Alby extension and test how it facilitates payments from the browser.



![video](https://youtu.be/nd5fX2vHuDw)



## Alby extension


The Alby extension is a tool that enables your web browser to interact easily and securely with the Bitcoin network and its Lightning Network layer. It is characterized by three aspects:


- Lightning Network wallet: Link your Alby node or account to send and receive bitcoin quickly and cheaply via the Lightning Network layer.
- Fluid payments via the Web: It eliminates the need to scan QR codes or switch between applications for bitcoin payments on websites that support Lightning. It enables smooth transactions with a single click, or without confirmation if you've set a budget.
- A Nostr manager: The extension manages your Nostr keys, making it easy to connect and interact with Nostr applications acting as a secure signatory without exposing your private key to every platform.


https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Connect to the extension


In this tutorial, we'll be using the Alby extension in the Firefox browser under a Ubuntu operating system. However, it is also available on Windows and with browsers such as Chrome.


You can add the Alby extension to your browser by visiting the [Firefox] extension store (https://addons.mozilla.org/fr/firefox/addon/alby/) or the [Chrome] extension store (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).


![firefox](assets/fr/01.webp)


![chrome](assets/fr/02.webp)


ℹ️ It's important to check that the author of the extension is indeed the official Alby account, to avoid any form of piracy or theft of your bitcoins.


Add the extension to your browser by clicking on the button on the right.

Grant the necessary permissions to install and use the extension, then pin the extension to the toolbar for easy retrieval.


![pin](assets/fr/03.webp)


You should also define an unlock code (very important), which will guarantee secure access to your Lightning wallet from your browser. We suggest you set a strong alphanumeric password.


ℹ️ Save this password in a safe place so that you can access it if you forget, as it can be changed but not retrieved.


https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)


Alby demonstrates its adaptability by offering you two choices:


- Continue with a Alby account if you want to enjoy the applications while keeping control of your bitcoins.
- Connect your own wallet or Lightning node if you already have one supported by the extension.


https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


In this tutorial, we choose to continue with the Alby account to take advantage of the features of the Alby ecosystem.


https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Login to your Alby account, or create one if you don't have one yet.


![signup](assets/fr/05.webp)


## Making your first payments


Once logged in, you can click on the Alby extension in the toolbar to access your portfolio.


![buzzin](assets/fr/06.webp)


Once you've created your Alby account, you'll need to connect it to a wallet in order to spend satoshis. To link the bitcoin wallet to your Alby account, we suggest you use a Alby Hub node, which you can either set up on your computer or subscribe to a plan offered by Alby.


![hubplan](assets/fr/13.webp)



In this tutorial, our Alby account is supported by a local installation on our machine.

To build your own Alby node, we recommend our Alby Hub tutorial.


https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

This node lets you create self-custodial Lightning portfolios and efficiently manage your Lightning channels to send and receive satoshis.


![channels](assets/fr/14.webp)


Open reception channels that define the total number of satoshis you can receive.


![receivechanal](assets/fr/15.webp)


Open sending channels by blocking satoshis on a bitcoin onchain address. The satoshis you've blocked define the total satoshis you're able to spend.


![spend](assets/fr/16.webp)


You can now send and receive satoshis via the Alby extension.


![exchange](assets/fr/08.webp)


From this point onwards, the Alby extension is able to detect Lightning addresses and invoices available on the web pages you visit, and will suggest that you pay them in bitcoin or Lightning directly from your extension.


![suggest](assets/fr/09.webp)


![pay](assets/fr/10.webp)



## Securing recovery keys with the master key


The master key offered by the Alby extension acts as a protective overlay that enables you to communicate securely with the main Bitcoin network layer (Onchain), the Nostr system and enables you to activate the Lightning connection with Nostr applications.


![masterKey](assets/fr/11.webp)


This master key takes the form of 12 words similar to your recovery phrase. We therefore recommend that you store it using secure methods to ensure that it can be accessed at any time.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)


You can now experience frictionless bitcoin and Lightning payments with the Alby extension. If you enjoyed this tutorial, we recommend our Alby Hub tutorial to set up your own Alby node and control all aspects of your Alby wallets from a smooth and powerful interface.


https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a