---
name: Sats.mobi

description: A Telegram-accessible custodial wallet
---

![cover](assets/cover.webp)

_This tutorial was written by_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

## Sats.Mobi
SatsMobi is a wallet that operates on Telegram, featuring all the functionalities of a Lightning Network (custodial) wallet, plus a series of very entertaining features. It originated from a fork of the now-discontinued LightningTipBot, inheriting all its features, while adding more current ones, thus making it more modern. Like LNTipBot, Sats.Mobi also embraces the open-source philosophy. The wallet can be configured and managed independently by cloning it from this [repository](https://github.com/massmux/SatsMobiBot).

If you prefer to use it in a simple way, you can start a chat session on Telegram. From this chat, you find out, it is actually a bot.

## Settings
From the Telegram search bar, look for "satsmobi" and the link to the [bot](@SatsMobiBot) will appear.

**Attention**: if you're not sure about searching via Telegram, access the bot securely using the following [link](https://t.me/SatsMobiBot)

![image](assets/it/01.webp)

All you need to do to get started is press _START_.

![image](assets/it/02.webp)

To explore the wallet, you can select _Menu_ at the bottom left.

![image](assets/it/03.webp)

Now you can opt for _/help_ among the main commands.

![image](assets/it/04.webp)

Sats.Mobi welcomes us by showing a message, listing all the main functionalities. Upon startup, the bot also created an LN Address, linked to the chosen handle on Telegram (which is unique by default). You can clearly see the commands for sending and receiving sats with this wallet, as well as other functions we will explore later. It's interesting to also take a look at the _/advanced_ menu.

![image](assets/it/05.webp)

It's worth noting that Sats.Mobi also creates an anonymous LN Address, to be used for gaining privacy. The bot works by ginving it some commands: just click on the corresponding word, or type the slash "/" in the message bar, followed by the command you want to execute. Even if the wallet has just been created, for example you can click on _/transactions_.

![image](assets/it/06.webp)

This command shows the list of the latest transactions: in this particular case they are equal to zero.

![image](assets/it/07.webp)

## Receiving sats
The command to create an invoice and receive sats is _/invoice_. Sats.Mobi operates exclusively in satoshi, the smallest unit of Bitcoin; therefore, to create an invoice, it is necessary to write the amount in sats in the message bar and then send it in the chat with the bot.
![image](assets/it/08.webp)

In the following example, we chose to receive an amount of 210 sats.

![cover](assets/it/09.webp)

After a few moments of waiting for the invoice to be prepared, it was available as both text and as a QR code. When paying the invoice, the wallet showed the balance. For some reason, if the total is not updated, you can write _/balance_ and press the `enter` key.

![image](assets/it/10.webp)

## Sending sats

While sats are an extremely valuable asset that one should not part with lightly, Sats.Mobi makes this action appealing. Conducting a few brief tests, such as a couple of trial transactions, should not be a problem.

### Paying an invoice

The simplest way to pay an invoice is to copy the message string `lnbc1xxxxx` and paste it into the message bar after typing the command _/pay_. **The correct syntax** requires leaving a space after the command.

![image](assets/it/11.webp)

The wallet will send a message asking for confirmation. By clicking on _Pay_, the invoice is paid.

![image](assets/it/12.webp)

Sats.Mobi can rely on an efficient and well-connected Lightning node, and payments rarely fail because it always manages to find the correct routing.

### Paying comfortably from mobile

While browsing on Telegram, you'll find that Sats.Mobi is also available on mobile. The most convenient way to make payments on mobile is by scanning a QR code; however, this wallet intentionally lacks that feature since it is not a standalone app, but rather embedded within a social media app. Nevertheless, Sats.Mobi is designed to enhance the mobile experience as much as possible — it can decode images, such as photographs of the QR code for the invoice you wish to pay.

Suppose, for example, you want to pay an invoice of 50 sats.

![image](assets/it/20.webp)

When this is shown to us, we can take a photo of the related QR code.

![image](assets/it/21.webp)

You can then open Telegram on the mobile and, in the chat with Sats.Mobi, attach the photo just taken of the QR code.

![cover](assets/it/22.webp)

Once selected, you can send it to the bot:

![image](assets/it/23.webp)
Sats.Mobi will decode the photo and **immediately present the payment request**, with the correct description. The chat will ask for confirmation: to proceed, you must press _/pay_.
![image](assets/it/24.webp)

Please wait a moment to allow the payment to be processed.

![image](assets/it/25.webp)

The invoice for 50 sats will be paid, a result achieved without the use of a camera and its integrated scanning function.

### Sats.Mobi in Telegram Groups

![image](assets/it/27.webp)

One of the features that made LNTipBot famous, which Sats.Mobi brings to Telegram, is its ability to create a fun and interactive experience for group members.
Owners can invite the bot to join the group chat and then designate Sats.Mobi as an admin. From that moment on, the fun begins, as members can start rewarding each other for their contributions to the group.
- _/tip_ adds a tip by replying to a message;
- _/send_ sends funds specifying a LN Address or a Telegram handle as the recipient;
- _/faucet_ (in the _/advanced_ menu) allows creating a series of tips that the fastest members of the group can collect by clicking on _/collect_;
- _/tipjar_ (in the _/advanced_ menu) creates another type of distribution that can be sent to users in the group.

Each of these commands has its syntax, which is explained in the main command menu.

And if we are not the owner of a group? No problem: just ask the founder to invite Sats.Mobi, add it as admin of the group, and you're all set!

## Point of Sale (POS)

When Sats.Mobi is launched for the first time, the bot introduces another feature for the user: **the POS**. Users can activate this "device" by entering the command _/pos_ or by clicking the corresponding button in the console at the bottom right. The POS functions as a web app that opens as a pop-up within the Telegram chat.

![image](assets/it/14.webp)

The interface displays the user's personal Telegram handle in the top left corner and operates just like any other POS system: by entering the amount on the keypad. Let's say we want to collect 21 euro cents for a service. Since Sats.Mobi primarily manages sats, converting that amount in your head can be tricky. However, the POS conveniently displays euros as the unit of account while simultaneously showing the equivalent in satoshi.

![image](assets/it/15.webp)
Clicking on _/OK_, it displays the invoice that can be shown to the customer via a QR code, or that can be sent as a string through instant messaging, so it can be paid.
![image](assets/it/16.webp)
![image](assets/it/17.webp)

Naturally, the POS is also available on mobile phones, accessed in the same way as previously shown.

![image](assets/it/18.webp)

It is also well displayed on the mobile phone screen:

![image](assets/it/19.webp)

## Additional Features

There are additional features that enhance the Sats.Mobi wallet, which, as we've seen, expands the concept of a wallet beyond just receiving and sending payments:
- _/nostr_: to connect the wallet to your own Nostr user to receive zaps;
- _/cashback_: shows a code that can be presented to a merchant to obtain cashback on a purchase;
- _/buy_: starts a guided procedure within the bot, which allows buying sats for euros;
- _/activatecard_: to request the activation of an NFC debit card, rechargeable through the Sats.Mobi wallet and for which notifications can be activated;
- _/link_: creates a link for your own Zeus or Blue Wallet, which can be used as remote controls for this wallet.

## Conclusion
Sats.Mobi is a pleasant and fun wallet to use, which brings back the experiences had with LNTipBot using the more advanced functions of LNBits. However, it is important to remember that **it is a custodial service**. Therefore, it should be used to hold very few sats, it is not a main wallet for your Lightning Network funds. There is also an intrinsic capacity limit, equal to 500,000 sats, a limit that is advised not to exceed.

If you are looking for non-custodial Lightning Network wallets, it is definitely advisable to look at other products.

---
### Documentation
- [Github](https://github.com/massmux/SatsMobiBot)
- Playlist of [videos](https://www.youtube.com/results?search_query=sats.mobi) demo