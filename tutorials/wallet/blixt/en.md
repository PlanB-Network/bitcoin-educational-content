---
name: Blixt

description: Mobile LN Node Wallet
---

![presentation](assets/blixt_intro_en.webp)

## A powerful BTC/Lightning node in your pocket, wherever you are

I would like to introduce you to an interesting and powerful new BTC/LN mobile node and wallet – Blixt. The name comes from Swedish and means "lightning".
If you never used Bitcoin Lightning Network, before you begin, please read [this simple explanation analogy about Lightning Network (LN)](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport).

## IMPORTANT ASPECTS:

### 1. Blixt is a private node, NOT a routing node! Keep that in mind.

That means, all the LN channels in Blixt will be unannounced to the LN graph (so called private channels). That means, THIS NODE WILL NOT DO ROUTING of others payments through Blixt node. [Read more about private and public channels here](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).

The Blixt mobile node is NOT for routing, I repeat. Is mainly to be able to manage your own LN channels and do your LN payments privately, whenever you need.

The Blixt mobile node, is necessary to be online and synced ONLY BEFORE you are going to do your transactions. That’s why you will see an icon on top that indicate the sync status. It takes only few moments, depending how much time you kept it offline and re-sync the LN graph.

### 2. Blixt is using LND (aezeed) as wallet backend, so don’t try to import other types of bitcoin wallets into it.

[Here you have explained the types of wallets](https://coldbit.com/what-types-of-mnemonic-seeds-are-used-in-bitcoin/). So if you had previously a LND node, you can import the seed and the backup.channels into Blixt, [as it is explained in this guide](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).

### 3. Blixt important links (please bookmark them):

- [Blixt Github repository](https://github.com/hsjoberg/blixt-wallet) | [Github Releases](https://github.com/hsjoberg/blixt-wallet/releases) (download the apk file directly)
- [Blixt Features page](https://blixtwallet.github.io/features) - explaining one by one each feature and functionality.
- [Blixt FAQ page](https://blixtwallet.github.io/faq) - List of Q&A and troubleshooting of Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demos, video tutorials, extra guides and use cases for Blixt
- [Printable A4 flyer](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) with first steps using Blixt, in various languages.
- Blixt also offers a full functional demo right on [its website](https://blixtwallet.com) or on a dedicated [web version](https://blixt-wallet-git-master-hsjoberg.vercel.app/), to have a full experience testing, before start using Blixt in real world.
- [Geyser crowdfunding page](https://geyser.fund/project/blixt) - donate sats as you like to support the project
- [Telegram support group](https://t.me/blixtwallet)

# Key features available

## Neutrino Node

Blixt connects by default to Blixt's server to synchronize blocks and index with Neutrino (SPV mode for Simplified Payment Verification), but the user can also connect to their own node. It is surprising to see that synchronizing an SPV node takes less than 5 minutes, in my case on Android 11, to be ready to use the full node wallet (on-chain and LN).

## Complete Non-Custodial Node

The user can manage their own channels with an easy-to-use interface and with enough displayed information to have a good experience. In the top left drawer menu, you can go to the Lightning channels to start opening with other nodes, as you wish. Don't forget to enable Tor in the settings. It's much better for privacy and also because as a mobile node, if you change your internet connection / clearnet IP frequently, your peers may be disrupted. With the Tor node URI, you will always have the same private identifier regardless of your location / IP.

## Backup/Restore an LND Node

A powerful, easy-to-manage, and useful feature is restoring other dead LND nodes, with just the 24-word seed list and the channels.backup file. [Here is a guide on how to restore dead Umbrel nodes in Blixt in case of SHTF.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)

The user also has the option to save the Blixt channel backup to Google Drive and/or local storage on their own mobile device (to later move it to a safe place, away from your phone).

The restoration process is quite simple: insert the 24-word seed, add the backup file (previously copied to the mobile memory), and click restore. It will take some time to synchronize and scan all the blocks for your past transactions. The channels will be automatically closed and the funds returned to your on-chain wallet (see the top left drawer menu - on-chain).

**Note** If you previously had open channels with your old node behind Tor, you must first enable the Tor option (and restart the application) from the menu settings. This way, the closing procedure will not fail and/or the forced closing option will not be used.

Remember to backup your LN channels after opening and/or closing channels. It only takes a few seconds to be safe. Later, you can move the backup file to a safe place away from your mobile device.
To test your seed in a restoration scenario, before adding funds, simply use the same 24-word seed (aezeed) in BlueWallet. If the generated BTC address is the same in Blixt, you are good to go. No need to use BlueWallet after that, you can simply delete the tested wallet for restoration.

## Built-in Tor

Once you have activated it, the application will restart behind the Tor network. From this point on, you can see in the menu settings your node ID with an onion address, so that other nodes can open channels to your small Blixt mobile node. Or let's say you have your own node at home and you want to have small channels with your Blixt mobile node. A perfect combination.

## Dunder LSP - Liquidity Service Provider

A simple and fantastic feature that offers new users the ability to start accepting BTC on the Lightning Network immediately, without the need to deposit funds on-chain and then open LN channels.

For new users, this is great news because they are supposed to be able to start from scratch, directly on LN. To do this, simply create an LN invoice from the main screen on the "receive" button, enter the amount, description, etc., and pay from another wallet. Blixt will open a channel of up to 400k sats per transaction received. You can open multiple channels if necessary.

An interesting and useful case is as follows: let's say your first received amount is 200k. Blixt will open a 400k sats channel with already 200k (minus opening fees) on your side, but since you still have 200k "space" available, you can receive more. So the next payment, let's say 100k, will arrive directly through this channel, without additional fees, and you still have 100k space to receive more.

But if you choose to receive, let's say, 300k for the third payment, it will create another new 400k channel and push these 300k to your side.

If there are too many requests, the Blixt node can adjust the channel capacity during opening.

## Automatic Channel Opening

In the settings, the user can activate this option and have an automated service that opens channels with the best nodes and routes based on the available balance in the on-chain wallet of the Blixt application. This is a beneficial feature for new users who are not sure which node to open a channel with and/or how to open an LN channel. It's like an autopilot for LN.

**Remember:** this option is used only once, when you create your new Blixt wallet, and is enabled by default. So if the new user scans the on-chain QR code on the main screen and deposits their first sats to that address, Blixt will automatically open a channel with those sats, with the Blixt public node.

## Incoming Liquidity Services

Feature dedicated to merchants who need more INCOMING liquidity, easy to use. To do this, simply select one of the liquidity providers from the list, pay the amount you want for the channel, and provide your node ID, and from there, a channel will open to your Blixt node.

## Contact Lists

Useful feature if you want to have a durable list of recipients with whom you trade most of the time. This list can consist of LNURLs, Lightning addresses, or future static payment information/invoices. For now, this list cannot be saved outside the application, but there are plans to have an option to export it.

## LNURL and Lightning Address

Full LNURL support. You can pay to LNURL, LN-auth, LN-chan request with LNURL.
You can send to any LN address and also add it into your contacts list.
Also starting with vers. 0.6.9 is available to receive to your own LN Address _@blixtwallet.com_ type, through [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box) feature.

## Keysend

A very powerful feature that few mobile wallets have. You can send/push funds directly through a channel or pointed to another node, adding a message if necessary. Is like a secret chat over LN. This feature is very useful for displaying messages on the Amboss.space billboard ([here is a guide on this Amboss billboard](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).

## Message signing

Very useful tool for signing messages with your Blixt node's private key, authentication messages, and so on. Very few mobile wallets have this feature, almost none.

## Multi-Channel Payments - Multi-Path Payments (MPP)

Useful feature for LN payments, allowing you to split an LN payment into multiple parts, across multiple channels. It's a good way to balance liquidity on the network and improve privacy.

## Lightning Browser

A series of third-party services with LN, organized within a simple, accessible, and user-friendly browser. It's also a good way to promote businesses that accept BTC on LN. This is a feature that will be further developed in the future. For now, it does not work behind Tor, so browsing these applications will be in clear (clearnet).

## Log Explorers

This is a powerful tool to check LND logs and the status of your node in general. There is an option to save the log file. It is very useful to have these logs at hand in case you need developer assistance in identifying certain issues.

## Security

You can set in the application settings, for greater security of your wallet/node, the possibility to start the application with a PIN code and/or fingerprint.

## On-chain Wallet

This feature is a bit hidden, in the drawer menu in the top left. Since it is not often used by an LN user, it is not visible on the main screen. But that's okay, you can have it on a separate wallet where you can manage addresses and view the transaction log, by importing your seed on Sparrow for example. Maybe in the future, Blixt wallet will also include a feature to manage UTxOs. But for now, ONLY use this on-chain wallet to open or close channels on LN.

## Special features

- With the vers. 0.6.9 was introduced the "persistent mode" that allow user to run Blixt as an always online LN node, keeping the LND services alive and the LN wallet ready to receive/send anytime.
- Simple Taproot Channels - allow opening Taproot channels for more privacy and advanced features
- Zero-confirmation channels with Blixt Dunder LSP
- Speedloader ("LN channel sync") - This means all channels will be synced quickly on startup, for better pathfinding. While it's a bit annoying that you have to see the sync screen in the beginning, it will ensure that the wallet knows about all channels and the payments will be faster and more reliable.
- Translated in 25+ languages!

## "Easter Eggs"

Yes, in the Blixt application, there are some hidden features, little things that make the application charming, activating fun/interesting actions and responses.
Hint: try clicking twice on the Blixt logo in the drawer 🙂 I'll let you discover the rest.

# Blixt Getting Started Step-by-Step Guide

**Tip:** as new LN user, if you start using Blixt LN Node, you will need first to know what is Lightning Network and how it works, at least at basic level. [Here we put together a simple list of resources about Lightning Network](https://blixtwallet.github.io/faq#what-is-ln). Please read them first.

Running a full LN node on a mobile device is not an easy task and could take some space (min 600MB) and memory. We recommend to have a good mobile device, updated and using at least Android 11 as OS.

Once you open Blixt, the “Welcome” screen will give you some options:

![Demo Blixt 01](assets/blixt_t01.webp)

On top right corner, you will see 3 dots that activate a menu with:

- “enable Tor” - user can start with Tor network, in special if wanted to restore an old LND node that was running with Tor only peers.
- “Set Bitcoin node” - if user want to connect to its own node directly, to sync the blocks through Neutrino, can do it straight away from welcome screen. This option is also good in case that your internet connection or Tor, is not so stable to connect to default bitcoin node (node.blixtwallet.com).

## First Step - Create new wallet

If you choose to “create a new wallet”, you will be redirected straight to the main screen of Blixt Wallet.

This is your “cockpit” and also is the “Main LN Wallet”, so be aware, it will show you only the balance of your LN wallet. The onchain wallet is separately displayed (see C).

![Demo Blixt 02](assets/blixt_t02.webp)

A - Blixt blocks sync indicator icon. This is the most important thing for a LN node: to be synchronized with the network. If that icon is still there working, means your node IS NOT READY! So have patience, in special for the first initial sync. It could take up to 6-8 min, depending on your device and internet connection.

You could click it and see the status of the sync:

![Demo Blixt 03](assets/blixt_t03.webp)

Also you could click on the “Show LND Log” (A) button if you want to see and read more technical details of the LND log, in real time. Is very useful for debug and learning more how LN works.

B - Here you can access all the Blixt Settings, and are a lot! Blixt is offering many rich features and options to manage your LN node like a pro. All those options are explained in details in the [“Blixt Features Page - Options Menu”](https://blixtwallet.github.io/features#blixt-options).

C - Here you have the “Magic Drawer” menu, also explained in details here. Here is the “Onchain Wallet” (B), Lightning Channels (C), Contacts, Channels status icon (A), Keysend (D).

![Demo Blixt 04](assets/blixt_t04.webp)

D - Is the help menu, with links to FAQ / Guides page, contact developer, Github page and Telegram support group.

E - Indicate your first BTC address, where you can deposit your first testing sats. THIS IS OPTIONAL! If you deposit straight into that address, is opening a LN channel towards Blixt Node. That means you will see your deposited sats, going into another onchain transaction (tx), for opening that LN channel. You can check that into Blixt onchain wallet (see point C), clicking on the top right TX menu.

![Demo Blixt 05](assets/blixt_t05.webp)

As you can see in the Onchain Transaction Log, the steps are very detailed indicating where the sats are going (deposit, open, close channel)

**Recommendation:** after testing several situations, we came to the conclusion that is much better efficient to open channels between 1 and 5 M sats. Smaller channels tend to be depleted quickly and paying a higher % of fees comparative with bigger channels.

F - Indicate your main Lightning wallet balance. This is NOT your total Blixt wallet balance, it represent only the sats you have in Lightning Channels, available to send. As was indicated before, the Onchain wallet is separate. Keep in mind this aspect. The onchain wallet is separate for an important reason: it is used mainly for opening/closing LN channels.

Ok so now you deposited some sats into that onchain address displayed on the main screen. It is recommended that when you do that, to keep your Blixt app online and active for a while, until the BTC tx is taken by the miners into the first block.

After that could take up to 20-30 min until is fully confirmed and the channel is open and you will see it in the Magic Drawer - Lightning Channels as active. Also the small colored dot on top of the drawer, if is green will indicate that your LN channel is online and ready to be used to send sats over LN.

The address and the welcome message displayed will disappear. There’s no more necessary to open a automatic channel now. You can also deactivate the option in Settings menu.

Is time to move on, testing other features and options to open LN channels.

Now, let’s open another channel with another node peer. Blixt community put together [a list of good nodes to start using with Blixt.](https://github.com/hsjoberg/blixt-wallet/issues/1033)

### Procedure to open a normal unannounced (private) LN channel in your Blixt mobile node

This is very simple, only take some few steps and a bit of patience:

- Go to the [Blixt Community list](https://github.com/hsjoberg/blixt-wallet/issues/1033) of good peers
- Select a node and click on its name title link, it will open its Amboss page
- Click to display the QR code for the node URI address

![Demo Blixt 06](assets/blixt_t06.webp)

Now, open Blixt and go to top drawer - Lightning Channels and click on the “+” button

![Demo Blixt 07](assets/blixt_t07.webp)

Now, click on (A) camera to scan the QR code from Amboss page and the node details will be filled out. Add the amount of the sats for the channel you want and then select the fee rate for the tx. You can leave it auto (B) for a faster confirmation or adjust it manually sliding the button. You can also long press the number and edit it as you like.

Do not put less than 1 sat/vbyte ! Usually is better to [consult the mempool fees](https://mempool.space/) before opening a channel and select a convenient fee.

Done, now just click on the button “open channel” and wait for 3 confirmations, that usually takes 30 min (1 block aprox each 10min).

Once is confirmed, you will see the channel active in your section “Lightning Channels”.

## Second Step - Obtain more Inbound Liquidity

Ok so now we have a LN channel with only OUTBOUND liquidity. That means we can only SEND, we still can’t RECEIVE sats over LN. Why? Did you read the guides indicated in the beginning? No? Go back and read them. It is very important to understand how LN channels works.

![Demo Blixt 08](assets/blixt_t08.webp)

As you can see in this example, the channel open with the first deposit, do not have too much INBOUND liquidity (“Can receive”) but have a lot of OUTBOUND liquidity (“Can send”).

So what options you have, if you want to receive more sats over LN?

- Spend some sats from existing channel. Yes, LN is a payment network of Bitcoin, used mainly to spend your sats faster, cheaper, private and easy. LN is NOT a hodling way, for that you have the onchain wallet.
- Swap some sats, back into your onchain wallet, using a submarine swap service. In this way you are not spending your sats, but giving it back to your own onchain wallet. Here you can see in details some methods, in the [Blixt Guides Page](https://blixtwallet.github.io/guides).
- Open an INBOUND channel from any LSP provider. Here is a video demo about [how to use LNBig LSP for opening an inbound channel](https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). That means, you will pay a small fee for an EMPTY channel (on your side) and you will be able to receive more sats into that channel. If you are a merchant that receive more than spend, that is a good option. Also if you are buying sats over LN, using Robosats or any other LN exchange.
- Open a Dunder channel, with Blixt node or any other Dunder LSP provider. A Dunder channel is a simple way to get some INBOUND liquidity, but in the same time you deposit some sats into that channel. Is also good because it will open the channel with an [UTXO](https://en.bitcoin.it/wiki/UTXO) that is not from your Blixt wallet. That add some privacy.
  Is also good because, if you do not have sats into an onchain wallet, to open a normal LN channel, but you have them into another LN wallet, you can just pay from that another wallet through LN the opening and the deposit (on your side) of that Dunder channel. [More details how Dunder works and how to run your own server here.](https://github.com/hsjoberg/dunder-lsp)

![Demo Blixt 09](assets/blixt_t09.webp)

Here are the steps how to activate opening a Dunder channel:

- Go to Settings, in “Experiments” section activate the box for “Enable Dunder LSP”.
- Once you did that, go back up to “Lightning Network” section and you will see that appeared the option “Set Dunder LSP Server”. There, by default is set “https://dunder.blixtwallet.com” but you can change it with any other Dunder LSP provider address. [Here is a Blixt community list](https://github.com/hsjoberg/blixt-wallet/issues/1033) with nodes that can provide Dudner LSP channels for your Blixt.
- Now you can go to main screen and click on “Receive” button. Then follow this procedure explained [in this guide](https://blixtwallet.github.io/guides#guide-lsp).

Ok, so after the Dunder channel is confirmed (will take few minutes) you will end up with having 2 LN channels: one opened initially with autopilot (channel A) and one with more inbound liquidity, opened with Dunder (channel B).

![Demo Blixt 10](assets/blixt_t10.webp)

Good, now you are good to go, to send and receive enough sats over LN !

## Third Step - Restore Node Procedure

So now let’s discuss about how to restore a Blixt wallet or any other LND crashed node. This is a bit more technical, but please pay attention. Is not that hard.

**Reminder:** in the past I wrote a dedicated guide with multiple options [how to restore a crashed LND node](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), where I mentioned also the method of using Blixt as quick restore process, using the seed + channel.backup file from your dead LND node. I also wrote a guide how to restore your Blixt node or migrate your Blixt to another device, [here](https://blixtwallet.github.io/faq#blixt-restore).

![Demo Blixt 11](assets/blixt_t11.webp)

But let’s explain in simple steps this process. As you can see in the image above, there are 2 things you should do to restore your previous Blixt/LND node:

- top box is where you have to fill with all 24 words from your seed (old / dead node)
- bottom are two button options to insert / upload the channel.backup file, previously saved from your old Blixt/LND node. It can be from a local file (you upload it into your device previously) or can be from a Google drive / iCloud remote location. Blixt have this option to save your channels backup directly into a Google / iCloud drive. See more details in [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).

Nevertheless to mention, if you previously didn’t have any open LN channels, there’s no need to upload any channels.backup file. Simply insert the 24 words seed and hit restore button.

Don’t forget to activate Tor, from the top 3 dots menu, as we explained in the "First Step" chapter of this guide. That is the case when you ONLY had Tor peers and could not be contacted over clearnet (domain/IP). Otherwise is not necessary.

Another useful feature is to set a specific Bitcoin node from that top menu. By default it sync blocks from node.blixtwallet.com (neutrino mode) but you can set any other Bitcoin node that provide neutrino sync.

So once you fill those options, and hit the restore button, Blixt will start first to sync the blocks through Neutrino as we explained in the "First Step" chapter of this guide. So be patient and watch the restore process in the main screen, by clicking on the sync icon.

![Demo Blixt 12](assets/blixt_t12.webp)

As you can see in this example, it shows that the bitcoin blocks are 100% synced (A) and the recovering process is in course (B). That means the LN channels you had previously, it will be closed and the funds restored into your Blixt onchain wallet.

This process takes time! So please, be patient and try to keep your Blixt active and online. The initial sync could take up to 6-8 min and the closing channels could take up to 10-15 min. So you better have the device charged well.

Once this process it started, you could check in the Magic Drawer - Lightning Channels, the status of each of your previous channels,showing that are in “pending to close” status. Once each channel is closed, you could see the closing tx in the onchain wallet (see Magic Drawer - Onchain), and open up the tx menu log.

![Demo Blixt 13](assets/blixt_t13.webp)

Also will be good to check and add if are not there, your previously peers you had in your old LN node. So go to Settings menu, down to “Lightning Network” and enter into option “Show Lightning Peers”.

![Demo Blixt 14](assets/blixt_t14.webp)

Inside the section you will see the peers you are connected in that moment and you could add more, better to add those you had channels before. Just go to Amboss page, search for your peer nodes aliases or nodeID and scan their node URI.

![Demo Blixt 15](assets/blixt_t15.webp)

As you can in the image above, are 3 aspects:

A - represents the clearnet node address URI (domain/IP)

B - represents the Tor onion node address URI (.onion)

C - is the QR code to scan with your Blixt camera or the copy button.

This node address URI you have to add it into your peers list. So be aware is not enough just the node alias name or nodeID.

Now you can go to Magic Drawer (top left menu) - Lightning Channels, and you can see at which maturity block height the funds will be returned into your onchain address.

![Demo Blixt 16](assets/blixt_t16.webp)

That block number 764272 is when the funds will be usable in your bitcoin onchain address. And it could take up to 144 blocks from the 1st confirmation block until are released. So check that in [the mempool](https://mempool.space/).

And that’s it. Just wait patiently until all channels are closed and funds back into your onchain wallet.

## Fourth Step - Customization

This chapter is about customization and know better you Blixt Node. I will not describe all the features available, are too many and were already explained in the [Blixt Features Page](https://blixtwallet.github.io/features).

But I will point out some of those necessary to go forward using your Blixt and have a great experience.

### A - Name (NameDesc)

![Demo Blixt 17](assets/blixt_t17.webp)

[The NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) is a standard for conveying "receiver name" in BOLT11 invoices.

This could be any name and can be changed anytime.

This option is really useful in various cases, when you want to send a name together with the invoice description, so the receiver could have a hint from who received those sats. This is fully optional and also in the payment screen, user have to tick the box indicating to send the alias name.

Here is an example of how would appear when you use [chat.blixtwallet.com](https://chat.blixtwallet.com/)

![Demo Blixt 18](assets/blixt_t18.webp)

This is another example sending to another wallet app that support NameDesc:

![Demo Blixt 19](assets/blixt_t19.webp)

### B - Backup LN Channels and seed words

This is a very important feature!

After opening or closing a LN channel you should do a backup. It can be done manually saving a small file on local device (download folder usually) or using a Google Drive or iCloud account.

![Demo Blixt 20](assets/blixt_t20.webp)

Go to Blixt Settings - Wallet section. There you have the options to save all important data for your Blixt wallet:

- “Show mnemonic” - will display the 24 words seed to write them down
- “Remove mnemonic from device” - this is optional and use it only if you really want to remove the seed words from your device. This will NOT wipe your wallet, only the seed. But be aware ! There is not way to recover them if you did not write them down first.
- “Export channel backup” - this option will save a small file on your local device, usually into “downloads” folder, from where you can take it and move it outside your device, for safe keeping.
- “Verify channel backup” - this is good option if you use Google drive or iCloud to check the integrity of the backup done remotely.
- “Google drive channel backup” - will save the backup file into your personal Google drive. The file is encrypted and is stored in a separate repository than your usual google files. So there are no concerns that can be read by anybody. Anyways that file is totally useless without the seed words, so nobody can take your funds from that file only.

I would recommend for this section the following:

- use a password manager to store safely your seed and backup file. [KeePass](https://keepass.info/) or Bitwarden are very good for that and can be used on multiplatform and self hosted or offline.
- DO THE BACKUP EVERY TIME you open or close a channel. That file is updated with the channels info. There’s no need to do it after each transaction you’ve done on LN. The channel backup is not storing that info, is storing only the status of the channel.

![Demo Blixt 21](assets/blixt_t21.webp)

## Conclusion

Ok, there are many other amazing features that Blixt offers, I will let you discover them one by one and have fun.

This app is really underestimated, mainly because is not backed by any VCs funding, is community driven, build with love and passion for Bitcoin and Lightning Network.

This mobile LN node, Blixt is a very powerful tool in hands of many users, if they know how to use it well. Just imagine, you are walking around the world with a LN node in your own pocket and nobody will know it.

And not talking about all other rich features that come with, that very few or none other wallet apps could offer.

I hope you enjoy using it. Personally, I love it and it's very useful to me (see here a use case where this wallet is a great tool).

HAPPY BITCOIN LIGHTNING!

May The ₿ITCOIN Be With You!

**Disclaimer:** I am not paid or supported in any way by the developers of this app. I wrote this guide because I saw that the interest in this wallet app is increasing and new users still don’t understand how to start with it. Also to help Hampus (the main dev) with documentation about using this node wallet. I do not have any other interest in promoting this LN app, other than pushing forward the Bitcoin and LN adoption. This is the only way!
