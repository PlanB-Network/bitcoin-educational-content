---
name: Wallet of Satoshi
description: The simplest custodial wallet to get started with Bitcoin
---
![cover](assets/cover.webp)
_This tutorial was written by_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

## Downloading, Setting Up, and Using Wallet of Satoshi

Wallet of Satoshi is a Lightning Network custodial wallet, and it is very simple to use.
For the purposes of the Italian course [BTC105 - Trovarsi Ora](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5), it is used to redeem Lightning Network vouchers.

**Always remember**: _not your keys, not your coins_

Custodial wallets do not allow users full control over their funds. They are normally not recommended, except for beginners. Wallet of Satoshi (WoS) should be used as a transitional wallet or for holding pocket money, not for long-term fund accumulation.

---

Wallet of Satoshi is a custodial product, which nonetheless has a good reputation. We can reasonably turn to a tool like WoS, for example, to increase our ability to receive liquidity: we temporarily delegate to WoS the "dirty work" of managing the liquidity of the channels for us. Once a certain amount is reached, we will empty WoS on-chain to our non-custodial wallet.

**WARNING⚠️: It is recommended to read the tutorial in its entirety before proceeding**

### Downloading Wallet of Satoshi

Go to the Play Store and download WoS

![image](assets/it/01.webp)

**Note:** WoS is only downloaded from official stores. If the device operating system is programmed, before opening WoS there is a verification part by the OS itself. After the verification phase, choose _Open_.

![image](assets/it/02.webp)

Wallet of Satoshi opens to the following window, and it is necessary to click on _Start_

![image](assets/it/03.webp)

### Registering an Account on WoS

At this point, the wallet is already operational, but for greater security, we should set up a log-in: it will be needed to recover funds in case of device malfunction or loss. Therefore, select the menu at the top left.

![image](assets/it/04.webp)

When the entire menu window opens, you must exclusively set the currency (Wallet of Satoshi by default presents the US dollar as the reference currency) and the theme color (light/dark), according to your taste. Do not use the other commands.

Being WoS a custodial tool, we cannot back up the wallet with the mnemonic seedphrase, but we can enable WoS to recover our funds, in case of loss or non-use of the mobile device, by clicking on _Login/Register_
A window will appear, asking us to enter an email address. It can be **a Proton mail address** (recommended), but it must be functional, as it will allow us to recover the funds in the wallet in case of loss/theft or damage to the mobile phone.

![image](assets/it/08.webp)

Wallet of Satoshi will then send a message to the indicated email inbox.

![image](assets/it/09.webp)

In the mailbox, we will find two words, which we will need to rewrite in the space provided by the app:
- **do not activate the translator: the words are and must remain in English**
- **rewrite the two words paying attention to uppercase/lowercase**

![image](assets/it/10.webp)

After transcribing the two words, click on _OK_.

![image](assets/it/11.webp)

The result should be an image appearing at the top, with the checkmark symbol for verification.

![image](assets/it/12.webp)

In the settings section, the red _Login/Register_ bar will then display the user's email address.

![image](assets/it/13.webp)

### Receiving Payments

To receive on WoS, click _Receive_ and a series of commands will appear.

![image](assets/it/14.webp)

You can receive:
- via a LN-Address **a**
- via LN, by setting the invoice **b**
- on chain (WoS supports the Bitcoin network but with paid submarine swaps) **c**
- by scanning an LNurl-p QR code **d**

![image](assets/it/15.webp)

### Creating an Invoice

Click on _Receive_ and choose the command with the Lightning Network symbol.

![image](assets/it/16.webp)

The invoice creation menu appears, where you can click on _Add Amount_ to write the exact amount and add a description, in this example, «My first invoice».

![image](assets/it/17.webp)

With the keyboard, you can set the amount.

![image](assets/it/18.webp)

After you have received payment, it appears like this:

![image](assets/it/19.webp)

### Collection from POS

Wallet of Satoshi has a default feature, which makes it particularly suitable for merchants: the POS. Let's see how to activate it.

From the main screen, select the menu at the top right.

![image](assets/it/20.webp)

Then select _Point of Sale_.

![image](assets/it/21.webp)

With the latest release of WoS, make sure to select the _Keypad_.

![image](assets/it/22.webp)
Afterwards, you can type the amount on the keypad: in the following example, it is equal to 10 cents / 118 sats. Add a description to receive the funds, in this case "my second with POS". Please click on the large green button that lit up on the screen.
![image](assets/it/23.webp)

This way, you will generate the invoice to show it - for example - to a customer.

![image](assets/it/24.webp)

The payment will be collected as the image indicates!

![image](assets/it/25.webp)

### Sending payments

Simplicity is a strength of the WoS main screen. To pay an invoice, click on _Send_

![image](assets/it/26.webp)

At a first use, WoS asks for permission to access the camera.

![image](assets/it/27.webp)

From this moment on, the camera is activated.

![image](assets/it/28.webp)

When scanning the invoice, we will see that a payment of 210 sats has been requested. A description is displayed as well if the requester has set one. This screen is the summary and also a request for confirmation: WoS "asks for authorization" to send the payment, which is granted by clicking the green _Send_ button.

![image](assets/it/29.webp)

When the payment reaches its destination, WoS notifies us through this screen.

![image](assets/it/30.webp)

From the main screen, clicking on _History_ (just below the balance) we can always check the list of transactions.

![image](assets/it/31.webp)

#### Recovering the WoS account

Now, we will see how to install WoS on a new device; it will be useful in cases of theft, loss, or inability to use the mobile phone on which the Wallet was previously installed. Once re-installed, you must redo the account registration procedure just explained, with a single variant: at the end of the request to log-in with the previously set email, WoS will show this screen:

![image](assets/it/33.webp)

A message will warn you that an email containing the procedure to reactivate the account has been sent to your address. You must open your email inbox.

**IMPORTANT**: open the email from a PC or, in any case, from a different device from the one on which you are about to recover the WoS account. In the inbox, you will find a message that shows you a QR code to scan.

![image](assets/it/34.webp)

Once the QR code is scanned, the recovered account will appear on the main page of WoS, with the related balance and history.