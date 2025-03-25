---
name: Wallet of Satoshi (WoS)
description: The simplest Wallet (custodial) to start with
---
![cover](assets/cover.webp)

_This tutorial was written by_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

# Download, configure and use Wallet of Satoshi

Wallet of Satoshi is a Wallet Lightning Network, custodial, very simple to use.

For the purposes of the course [BTC105 - Finding Yourself Now](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5), it is used to redeem Lightning Network vouchers.

**always remember**: _not your keys, not your coins_

Wallet custodial, do not allow users to fully dispose of their funds. They are normally not recommended, except for those starting from scratch. WoS should be used as a gateway Wallet or to store pocket money, not to accumulate funds for the long term.

---
Wallet of Satoshi (WoS) is a custodial product, but it has a certain reputation. We can reasonably turn to a tool like WoS, for example, to increase our ability to receive liquidity. We temporarily delegate to WoS "the dirty work" of managing channel liquidity for us. Once we reach a certain amount, we will empty WoS On-Chain on our Wallet non-custodial.

**ATTENZIONE⚠️: It is recommended that you read the tutorial in its entirety before proceeding**

## Downloading Wallet of Satoshi

Let's go to the playstore and download WoS

![image](assets/it/01.webp)

**Note:** WoS is downloaded only from the official stores. If the device operating system is programmed, a verification part by the OS itself takes place before opening WoS. Once the verification phase has passed, choose _Open_.

![image](assets/it/02.webp)

Wallet of Satoshi opens with the following screen and you need to click on _Start_

![image](assets/it/03.webp)

## Registering an account for WoS

At this point Wallet is up and running, but for added security let's set up a login: this will be used to recover funds in case of device failure or loss. Then select the menu at the top left.

![image](assets/it/04.webp)

The whole menu window opens, in which you only need to set the currency (Wallet of Satoshi by default presents the U.S. dollar as the reference currency) and the theme color (light/dark), depending on your taste. Do not use the other controls.

Since WoS is a custodial tool, we cannot back up Wallet with Mnemonic phrase, however, we can enable WoS to retrieve our funds, in case of lost or unused mobile device, by clicking on _Login/Register_

![image](assets/it/07.webp)

A window appears in which we are asked to enter an email address. It can be **a Proton email** (recommended), however it works, because it is the one that will allow us to recover Wallet funds, in case of lost/stolen or broken cell phone

![image](assets/it/08.webp)

Wallet of Satoshi sent a message to the reported email box

![image](assets/it/09.webp)

In the inbox we will find two words, we have to enter them, rewriting them, in the space that the app presents to us


- do not activate the translator: the words are and should remain in English**
- rewrite the two words paying attention to upper/lower case**

![image](assets/it/10.webp)

After transcribing the two words, click _OK_

![image](assets/it/11.webp)

The result is that a figure should appear at the top, with a check mark symbol for verification

![image](assets/it/12.webp)

while in the settings section, the red band of _Login/Register_ now displays the user's email address.

![image](assets/it/13.webp)

## Receiving payments

To receive on WoS click _Receive_ and a series of commands appear.

![image](assets/it/14.webp)

You can receive


- via LN-Address **a**
- via LN, setting Invoice **b**
- on chain (WoS supports the Bitcoin network but with submarine swaps for a fee) **c**
- framing the QR code of an LNurl-p **d**

![image](assets/it/15.webp)

## Invoice Creation

Click on _Receive_ and choose the command with the symbol of Lightning Network

![image](assets/it/16.webp)

Just the Invoice creation menu appears, where we click _Add Amount_ to write the exact amount and add a description, in this example "My first Invoice."

![image](assets/it/17.webp)

Using the keyboard we set the amount

![image](assets/it/18.webp)

and then get Invoice paid. The payment received appears like this:

![image](assets/it/19.webp)

## Collection from POS

Wallet of Satoshi has an interesting feature by default, making it especially suitable for merchants: POS. Let's see how to activate it.

From the main screen, select the menu in the upper right corner

![image](assets/it/20.webp)

After that, select _Point of Sale_

![image](assets/it/21.webp)

With the latest release of WoS, pay attention to select the _Keypad_

![image](assets/it/22.webp)

and then type the amount on the keypad, in the following example equal to 18 cents / 118 Sats. Add a description for the collection, in this case "my second with POS." A large green button lights up, and it is to click

![image](assets/it/23.webp)

in order to generate the Invoice and show it-for example-to a client.

![image](assets/it/24.webp)

This payment is also collected!

![image](assets/it/25.webp)

## Sending payments

Simplicity is a strength of the WoS main screen. To pay for a Invoice, click on _Send_

![image](assets/it/26.webp)

On first use, WoS asks for permissions to access the camera

![image](assets/it/27.webp)

From this moment, the camera is activated

![image](assets/it/28.webp)

Framing Invoice, we see that a payment of 210 Sats has been requested. It also reads a description, if the requester has set one. This screen is the summary and also a request for confirmation: WoS "asks for permission" to send the payment, which is granted by clicking the green _Send_ button

![image](assets/it/29.webp)

When the payment arrives at its destination, WoS alerts with this screen

![image](assets/it/30.webp)

From the princicpal screen, clicking on _History_ (just below the balance) brings up the list of transactions

![image](assets/it/31.webp)

### WoS account recovery

Now, we will see how to install WoS on a new device; this will also be useful in cases of theft, loss, or inability to operate the cell phone on which Wallet was previously installed. Once re-installed, you have to redo the account registration procedure just explained, with one variation: at the end of the login request with the previously set email, WoS will appear like this:

![image](assets/it/33.webp)

A message alerts us that the procedure to reactivate the account has been emailed. One has to open one's mailbox.

**IMPORTANT**: open the email from a PC or, at any rate, from a device other than those on which you are going to retrieve the WoS account. In the inbox we find a message that shows us a QR code to frame

![image](assets/it/34.webp)

Once the QR code is framed, the retrieved account will appear on the WoS main page, with the balance and history.