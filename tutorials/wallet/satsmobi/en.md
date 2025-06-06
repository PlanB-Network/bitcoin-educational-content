---
name: Sats.mobi
description: A Wallet (custodial) within Telegram's reach
---
![cover](assets/cover.webp)

_This tutorial was written by_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

# Sats.Mobi

SatsMobi is a Wallet running on Telegram, which has all the functions of a Wallet Lightning Network (custodial) and offers, in addition, a number of very fun features. It stems from a Fork from LightningTipBot, now discontinued, inherits all its features while adding more current ones, making it more modern. Of LNTipBot, Sats.Mobi also traces the open source philosophy. Wallet can, in fact, be configured and managed on its own by cloning it from this [repository](https://github.com/massmux/SatsMobiBot).

If, on the other hand, you prefer to use it in a simple way, simply start a chat on Telegram and you will find that it is a bot.

# Settings

From the Telegram search bar, search for "satsmobi" and the link to the [bot](@SatsMobiBot) will appear.

**Caution**: If you are not sure about the search via Telegram, access the bot securely using the following [link](https://t.me/SatsMobiBot)

![image](assets/it/01.webp)

All you need to start it, is to press _START_

![image](assets/it/02.webp)

To explore Wallet you can select _Menu_ in the lower left corner.

![image](assets/it/03.webp)

Opt now for _/help_ among the main commands.

![image](assets/it/04.webp)

Sats.Mobi welcomes us by showing a message, listing all the main features. At startup, the bot has also created a LN Address, linked to the handle chosen on Telegram (which is unique by default). Commands to send and receive Sats with this Wallet are visible, as well as other functions that we will see later. It is also interesting to take a look at the _/advanced_ menu right away

![image](assets/it/05.webp)

It jumps out that Sats.Mobi has also created an anonymous LN Address, which can be used to gain privacy. The bot works with commands: just click on the corresponding word, or type the slash "/" in the message bar, followed by the command you want to have executed. Even if Wallet has just been created, choose, for example, _/transactions_

![cimageover](assets/it/06.webp)

This command shows the list of last transactions, in this particular case zero.

![image](assets/it/07.webp)

# Receiving Sats

The command for creating a Invoice and receiving Sats is _/invoice_. Sats.Mobi reasons exclusively in Satoshi, the smallest unit in Bitcon; therefore, in order to create the Invoice, it is necessary to write the amount in Sats in the message bar and later send it in the chat with the bot.

![image](assets/it/08.webp)

In the following example, an amount of 210 Sats was chosen to be received.

![cover](assets/it/09.webp)

After a few moments of waiting for Invoice to be prepared, the latter is available as text and as a QR code. By paying Invoice, Wallet shows the balance. If for some reason the total is out of date, write _/balance_ and press the `send` key.

![image](assets/it/10.webp)

# Send Sats

Although Satss are an invaluable asset from which one should not part superficially, Sats.Mobi makes this part appealing, performing some short tests (i.e., a couple of test transactions) will not be a problem.

## Paying a Invoice

The easiest way to pay a Invoice is to copy the message string `lnbc1xxxxx` and paste it into the message bar after typing the _/pay_ command. **Correct syntax** involves leaving a space after the command.

![image](assets/it/11.webp)

Wallet sends a message asking for confirmation. By clicking on _Pay_ the Invoice is paid.

![image](assets/it/12.webp)

Sats.Mobi can rely on an efficient and well-connected Lightning node, rarely payments fail because it can always find the correct routing.

## Pay conveniently from mobile

Turning to Telegram, Sats.Mobi is also available on mobile. The most convenient function for mobile payment is to frame a QR code, but this Wallet lacks this by design, since it is not a stand-alone app but is contained in a social. Sats.Mobi is therefore programmed to make the mobile experience as easy as possible: it can in fact decode an image, such as a photograph taken of the QR code of the Invoice you want to pay for.

Suppose, for example, we want to pay a Invoice of 50 Sats.

![image](assets/it/20.webp)

When this is shown to us, we can take a picture of the relevant QR code.

![image](assets/it/21.webp)

We then open Telegram on the cell phone and, in the chat with Sats.Mobi, attach the photo we just took to the QR code

![cover](assets/it/22.webp)

Once selected, we send it to the bot:

![image](assets/it/23.webp)

Sats.Mobi decodes the photo and **presents the payment request** immediately, with the correct description. The chat asks for a confirmation, to proceed you must press _/pay_

![image](assets/it/24.webp)

We wait a few moments to allow the payment to be processed.

![image](assets/it/25.webp)

Invoice by 50 Sats was paid, a result achieved without the use of a camera and its built-in scan function.

## Sats.Mobi in Telegram Groups

![image](assets/it/27.webp)

Of the features that made LNTipBot famous and that Sats.Mobi brings back to Telegram, there is the one that makes the experience of members in a group fun and interactive.

Owners can invite the bot to join in the group chat and then appoint Sats.Mobi as admin. From then on, the fun begins, because members can start rewarding other users for their contributions in the group.


- _/tip_ adds a tip by responding to a message;
- _/send_ sends funds by specifying a LN Address or Telegram handle as the recipient;
- _/faucet_ (in the _/advanced_ menu) allows you to create a set of tips that the fastest group members can collect by clicking _/collect_;
- _/tipjar_ (in the _/advanced_ menu) creates another type of distribution that can be sent to users in the group.

Each of these commands has its own syntax, which is explained in the main command menu.

What if we are not an owner of a group? No problem: just ask the founder to invite Sats.Mobi, add him/her as admin of the same, and you're done!

# Point of Sale (POS)

When starting Sats.Mobi for the first time, the bot also creates another feature for the user: **the POS**. The "device" is activated by the user with the _/pos_ command or by clicking on the relevant button from the console in the lower right corner. In fact, the POS is a web app, which opens as a pop-up on the Telegram chat

![image](assets/it/14.webp)

The interface carries Telegram's personal handle in the upper left corner and is used simply as one uses all POS: by typing the amount on the keypad. Now suppose we want to collect 21 cents for a service. Knowing that Sats.Mobi natively handles only Satss, it is not easy to do the conversion in your head. Instead, the POS displays the euro as the unit of account while showing the equivalent in Satoshi.

![image](assets/it/15.webp)

Clicking on _/OK_ brings up the Invoice that can be shown to the customer via a QR code, or that can be sent as a string via instant messaging, so that it can be paid for

![image](assets/it/16.webp)

![image](assets/it/17.webp)

Of course, the POS is also available on a cell phone by calling it up in the same way as shown above.

![image](assets/it/18.webp)

It also presents itself well viewable from the cell phone display:

![image](assets/it/19.webp)

# Additional features

There are other features that complement the Wallet Sats.Mobi offering, which, as we have seen, expands the Wallet concept beyond the operations of receiving and sending payments:


- _/nostr_: to connect Wallet to its user Nostr to receive zaps;
- _/cashback_: shows a code that you can show to a merchant to get cashback on an expense;
- _/buy_: starts a wizard within the bot, which allows you to purchase Sats for euros:
- _/activatecard_: to request activation of an NFC debit card, which can be reloaded through the Wallet Sats.Mobi and for which notifications can be activated;
- _/link_: creates a link for your own Wallet Zeus or Blue Wallet, which you can use as remote controls of this Wallet.

# Conclusion

Sats.Mobi is a Wallet that is pleasant and fun to use, bringing back into use the experiences made with LNTipBot using the more advanced features of LNBits. However, it is important to remember that **it is a custodial service**. It is therefore to be used to custodial very few Satss; it is not a Wallet principal for its own Lightning Network funds. There is also an inherent capacity limit of 500,000 Satss, a limit that is not recommended to be exceeded.

If you are looking for Wallet Lightning Network non-custodial, you should definitely look to other products.

---
### Documentation


- [Github](https://github.com/massmux/SatsMobiBot)
- Playlist of [video](https://www.youtube.com/results?search_query=Sats.mobi) demos