---
name: Blixt Wallet
description: How to start using a powerful LN node on your mobile?
---
![cover](cover.webp)

This guide is dedicated to all those new users that want to start using Bitcoin Lightning Network (LN) in a FREE OPEN SOURCE, FULL NON-CUSTODIAL way.

Using [Blixt Wallet](https://blixtwallet.com/), a full LN node on your mobile, wherever you are.

If you never used Bitcoin Lightning Network, before you begin, [please read this simple explanation analogy about Lightning Network (LN)](https://darth-coin.github.io/beginner/ln-airport-analogy-en.html).

## IMPORTANT ASPECTS:

- Blixt is a private node, NOT a routing node! Keep that in mind : That means, all the LN channels in Blixt will be unannounced to the LN graph (so called private channels). That means, THIS NODE WILL NOT DO ROUTING of others payments through Blixt node. This Blixt node is NOT for routing, I repeat. Is mainly to be able to manage your own LN channels and do your LN payments privately, whenever you need. This Blixt node, is necessary to be online and synced ONLY BEFORE you are going to do your transactions. That’s why you will see an icon on top that indicate the sync status. It takes only few moments, depending how much time you kept it offline.

- Blixt is using LND (aezeed) as wallet backend, so don’t try to import other types of bitcoin wallets into it. [Here you have explained the types of wallet mnemonic seeds](https://coldbit.com/what-types-of-mnemonic-seeds-are-used-in-bitcoin/). And here is [a more extensive list of all types of wallets](https://walletsrecovery.org/). So if you had previously a LND node, you can import the seed and the backup.channels into Blixt, [as it is explained in this guide](https://darth-coin.github.io/nodes/shtf-restore-lnd-node-en.html).

- At the end of this guide you will find a special section with ["tips and tricks"](https://darth-coin.github.io/wallets/getting-started-blixt-wallet-en.html#tips)

- Blixt important links - see them at the end of this guide, please bookmark them.

---

## Blixt - First Contact

So… Darth’s Mom decided to start using LN with Blixt. Hard decision, but wise. Blixt is only for smart people and those who really want to learn more, deep use of LN.

![blixt](assets/en/01.webp)

Darth warn his mom:

"*Mom, if you start using Blixt LN Node, you will need first to know what is Lightning Network and how it works, at least at basic level. [Here I put together a simple list of resources about Lightning Network](https://blixtwallet.github.io/faq#what-is-ln). Please read them first.*"

Darth’s Mom read the resources and did her first step: install Blixt on her brand new Android device. Blixt is also available for iOS and macOS (desktop). But those are not for Darth’s Mom… Nevertheless it is recommended to use a newer version of Android, at least 9 or 10 for better compatibility and experience. Running a full LN node on a mobile device is not an easy task and could take some space (min 600MB) and memory.

Once you open Blixt, the “Welcome” screen will give you some options:

![blixt](assets/en/02.webp)

On top right corner, you will see 3 dots that activate a menu with:

- “enable Tor” - user can start with Tor network, in special if wanted to restore an old LND node that was running with Tor only peers.
- “Set Bitcoin node” - if user want to connect to its own node directly, to sync the blocks through Neutrino, can do it straight away from welcome screen. This option is also good in case that your internet connection or Tor, is not so stable to connect to default bitcoin node (node.blixtwallet.com).
- Soon it will be added the language there, so user can start straight with a language that is comfortable. If you want to contribute to this open source project with translations in other languages, [please join here](https://explore.transifex.com/blixt-wallet/blixt-wallet/).

### OPTION A - Create new wallet

If you choose to “create a new wallet”, you will be redirected straight to the main screen of Blixt Wallet.

This is your “cockpit” and also is the “Main LN Wallet”, so be aware, it will show you only the balance of your LN wallet. The onchain wallet is separately displayed (see C).

![blixt](assets/en/03.webp)

A - Blixt blocks sync indicator icon. This is the most important thing for a LN node: to be synchronized with the network. If that icon is still there working, means your node IS NOT READY! So have patience, in special for the first initial sync. It could take up to 6-8 min, depending on your device and internet connection.

You could click it and see the status of the sync:

![blixt](assets/en/04.webp)

Also you could click on the “Show LND Log” (A) button if you want to see and read more technical details of the LND log, in real time. Is very useful for debug and learning more how LN works.

B - Here you can access all the Blixt Settings, and are a lot! Blixt is offering many rich features and options to manage your LN node like a pro. All those options are explained in details in the “[Blixt Features Page](https://blixtwallet.github.io/features#blixt-options) - Options Menu”.

C - Here you have the “Magic Drawer” menu, [also explained in details here](https://blixtwallet.github.io/features#blixt-drawer). Here is the “Onchain Wallet” (B), Lightning Channels (C), Contacts, Channels status icon (A), Keysend (D).

![blixt](assets/en/05.webp)

D - Is the help menu, with links to FAQ / Guides page, contact developer, Github page and Telegram support group.

E - Indicate your first BTC address, where you can deposit your first testing sats. THIS IS OPTIONAL! If you deposit straight into that address, is opening a LN channel towards Blixt Node. That means you will see your deposited sats, going into another onchain transaction (tx), for opening that LN channel. You can check that into Blixt onchain wallet (see point C), clicking on the top right TX menu.

![blixt](assets/en/06.webp)

As you can see in the Onchain Transaction Log, the steps are very detailed indicating where the sats are going (deposit, open, close channel).

RECOMMENDATION:

After testing several situations, we came to the conclusion that is much better efficient to open channels between 1 and 5 M sats. Smaller channels tend to be depleted quickly and paying a higher % of fees comparative with bigger channels.

F - Indicate your main Lightning wallet balance. This is NOT your total Blixt wallet balance, it represent only the sats you have in Lightning Channels, available to send. As was indicated before, the Onchain wallet is separate. Keep in mind this aspect. The onchain wallet is separate for an important reason: it is used mainly for opening/closing LN channels.

Ok so now Darth’s Mom deposited some sats into that onchain address displayed on the main screen. It is recommended that when you do that, to keep your Blixt app online and active for a while, until the BTC tx is taken by the miners into the first block.

After that could take up to 20-30 min until is fully confirmed and the channel is open and you will see it in the Magic Drawer - Lightning Channels as active. Also the small colored dot on top of the drawer, if is green will indicate that your LN channel is online and ready to be used to send sats over LN.

The address and the welcome message displayed will disappear. There’s no more necessary to open a automatic channel now. You can also deactivate the option in Settings menu.

Is time to move on, testing other features and options to open LN channels.

Now, let’s open another channel with another node peer. Blixt community put togheter [a list of good nodes to start using with Blixt](https://github.com/hsjoberg/blixt-wallet/issues/1033).

**Procedure to open a LN channel in Blixt**

This is very simple, only take some few steps and a bit of patience:

- Got to the [Blixt Community](https://github.com/hsjoberg/blixt-wallet/issues/1033) list of peers
- Select a node and click on its name title link, it will open its Amboss page
- Click to display the QR code for the node URI address

![blixt](assets/en/07.webp)

Open Blixt and go to top drawer - Lightning Channels and click on the “+” button

![blixt](assets/en/08.webp)

Now, click on (A) camera to scan the QR code from Amboss page and the node details will be filled out. Add the amount of the sats for the channel you want and then select the fee rate for the tx. You can leave it auto (B) for a faster confirmation or adjust it manually sliding the button. You can also long press the number and edit it as you like.

Do not put less than 1 sat/vbyte ! Usually is better to consult the [mempool fees](https://mempool.space/) before opening a channel and select a convenient fee.

Done, now just click on the button “open channel” and wait for 3 confirmations, that usually takes 30 min (1 block aprox each 10min).

Once is confirmed, you will see the channel active in your section “Lightning Channels”.

---

## Blixt - Second Contact

Ok so now we have a LN channel with only OUTBOUND liquidity. That means we can only SEND, we still can’t RECEIVE sats over LN.

![blixt](assets/en/09.webp)

Why? Did you read the guides indicated in the beginning? No? Go back and read them. It is very important to understand how LN channels works.

![blixt](assets/en/10.webp)

As you can see in this example, the channel open with the first deposit, do not have too much INBOUND liquidity (“Can receive”) but have a lot of OUTBOUND liquidity (“Can send”).

So what options you have, if you want to receive more sats over LN?

- Spend some sats from existing channel. Yes, LN is a payment network of Bitcoin, used mainly to spend your sats faster, cheaper, private and easy. LN is NOT a hodling way, for that you have the onchain wallet.

- Swap some sats, back into your onchain wallet, using a submarine swap service. In this way you are not spending your sats, but giving it back to your own onchain wallet. Here you can see in details some methods, in the [Blixt Guides Page](https://blixtwallet.github.io/guides).

- Open an INBOUND channel from any LSP provider. Here is a video demo about how to use LNBig LSP for opening an inbound channel. That means, you will pay a small fee for an EMPTY channel (on your side) and you will be able to receive more sats into that channel. If you are a merchant that receive more than spend, that is a good option. Also if you are buying sats over LN, using Robosats or any other LN exchange.

- Open a Dunder channel, with Blixt node or any other Dunder LSP provider. A Dunder channel is a simple way to get some INBOUND liquidity, but in the same time you deposit some sats into that channel. Is also good because it will open the channel with an [UTXO](https://en.bitcoin.it/wiki/UTXO) that is not from your Blixt wallet. That add some privacy. Is also good because, if you do not have sats into an onchain wallet, to open a normal LN channel, but you have them into another LN wallet, you can just pay from that another wallet through LN the opening and the deposit (on your side) of that Dunder channel. [More details how Dunder works and how to run your own server here](https://github.com/hsjoberg/dunder-lsp).

![blixt](assets/en/11.webp)

Here are the steps to activate opening a Dunder channel:

- Go to Settings, in “Experiments” section activate the box for “Enable Dunder LSP”.
- Once you did that, go back up to “Lightning Network” section and you will see that appeared the option “Set Dunder LSP Server”. There, by default is set “https://dunder.blixtwallet.com” but you can change it with any other Dunder LSP provider address. [Here is a Blixt community list](https://github.com/hsjoberg/blixt-wallet/issues/1033) with nodes that can provide Dudner LSP channels for your Blixt.
- Now you can go to main screen and click on “Receive” button. Then follow this procedure [explained in this guide](https://blixtwallet.github.io/guides#guide-lsp).

OK, so after the Dunder channel is confirmed (will take few minutes) you will end up with having 2 LN channels: one opened initially with autopilot (channel A) and one with more inbound liquidity, opened with Dunder (channel B).

![blixt](assets/en/12.webp)

Good, now you are good to go, to send and receive enough sats over LN !

HAPPY BITCOIN LIGHTNING!

---

## Blixt - Third Contact

Remember, in the chapter one “First Contact” were 2 options in the Welcome screen:
- [Option A](https://darth-coin.github.io/wallets/getting-started-blixt-wallet-en.html#option-a) - Create new wallet
- Option B - Restore wallet

So now let’s discuss about how to restore a Blixt wallet or any other LND crashed node. This is a bit more technical, but please pay attention. Is not that hard.

### OPTION B - Restore wallet

In the past I wrote a dedicated guide about [how to restore a crashed Umbrel node](https://darth-coin.github.io/nodes/shtf-restore-lnd-node-en.html), where I mentioned also the method of using Blixt as quick restore process, using the seed + channel.backup file from Umbrel.

I also wrote a guide how to restore your Blixt node or migrate your Blixt to another device, [here](https://blixtwallet.github.io/faq#blixt-restore).

![blixt](assets/en/13.webp)

But let’s explain in simple steps this process. As you can see in the image above, there are 2 things you should do to restore your previous Blixt/LND node:

- top box is where you have to fill with all 24 words from your seed (old / dead node)
- bottom are two button options to insert / upload the channel.backup file, previously saved from your old Blixt/LND node. It can be from a local file (you upload it into your device previously) or can be from a Google drive / iCloud remote location. Blixt have this option to save your channels backup directly into a Google / iCloud drive. See more details in [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).

Nevertheless to mention, if you previously didn’t have any open LN channels, there’s no need to upload any channels.backup file. Simply insert the 24 words seed and hit restore button.

Don’t forget to activate Tor, from the top 3 dots menu, as we explained in the Option A section. That is the case when you ONLY had Tor peers and could not be contacted over clearnet (domain/IP). Otherwise is not necessary.

Another useful feature is to set a specific Bitcoin node from that top menu. By default it sync blocks from node.blixtwallet.com (neutrino mode) but you can set any other Bitcoin node that provide neutrino sync.

So once you fill those options, and hit the restore button, Blixt will start first to sync the blocks through Neutrino as we explained in the First Contact chapter. So be patient and watch the restore process in the main screen, by clicking on the sync icon.

![blixt](assets/en/14.webp)

As you can see in this example, it shows that the bitcoin blocks are 100% synced (A) and the recovering process is in course (B). That means the LN channels you had previously, it will be closed and the funds restored into your Blixt onchain wallet.

This process takes time! So please, be patient and try to keep your Blixt active and online. The initial sync could take up to 6-8 min and the closing channels could take up to 10-15 min. So you better have the device charged well.

Once this process it started, you could check in the Magic Drawer - Lightning Channels, the status of each of your previous channels,showing that are in “pending to close” status. Once each channel is closed, you could see the closing tx in the onchain wallet (see Magic Drawer - Onchain), and open up the tx menu log.

![blixt](assets/en/15.webp)

Also will be good to check and add if are not there, your previously peers you had in your old LN node. So go to Settings menu, down to “Lightning Network” and enter into option “Show Lightning Peers”.

![blixt](assets/en/16.webp)

Inside the section you will see the peers you are connected in that moment and you could add more, better to add those you had channels before. Just go to [Amboss page](https://amboss.space/), search for your peer nodes aliases or nodeID and scan their node URI.

![blixt](assets/en/17.webp)

As you can in the image above, are 3 aspects:

A - represents the clearnet node address URI (domain/IP)

B - represents the Tor onion node address URI (.onion)

C - is the QR code to scan with your Blixt camera or the copy button.

This node address URI you have to add it into your peers list. So be aware is not enough just the node alias name or nodeID.

Now you can go to Magic Drawer (top left menu) - Lightning Channels, and you can see at which maturity block height the funds will be returned into your onchain address.

![blixt](assets/en/18.webp)

That block number 764272 is when the funds will be usable in your bitcoin onchain address. And it could take up to 144 blocks from the 1st confirmation block until are released. [So check that in the mempool](https://mempool.space/).

And that’s it. Just wait patiently until all channels are closed and funds back into your onchain wallet.

👉 **Secret restore method :**

There's another method to restore your Blixt LND node without even closing the channels. But is hidden from usual noob users, because this method is ONLY for those who knows what they are doing.

In case you need to migrate your existing (working) Blixt node to another new device, without closing the existing LN channels, you will have to do these steps:

- We suppose that you already saved the Blixt Wallet seed (24 words aezeed)
- On the old device, go to "Settings" - debug section - "Compact LND database". This step is optional but recommended if you want a smaller size of the channel.db file. Usually is quite big, depending of your node activity. This will restart Blixt and compact the db file size.
- Once restarted, go to "Settings" and change your regular alias name to "Hampus". This will activate the hidden options, only for advanced users.
- Go way down to "Debug" section and you will see a new option "Export channel.db file". WARNING! Once you do this export, the existing Blixt LN node will be disabled on this old device and will export the entire node database (channel.db) ready to be imported into a new device.
- This db file will be saved into a designated folder on your old device (Documents or Downloads) and from there you will have to move it as it is to your new device. You can use for example [LocalSend FOSS app](https://github.com/localsend/localsend) to transfer the file directly between devices.
- In this moment your old Blixt MUST stay shut down. DO NOT OPEN IT AGAIN!
- Once you transfer the channel.db file to the new device, start the new installation of Blixt and choose "Restore wallet" in the first screen.
- On the button where it says "Select SCB file" long press (NOT simple click!) and then you will see the option to select a channel.db file where you save it locally in the new device. If you just simple press that button it will use by default a SCB file (with closing channels), it doesn't work for full backup live channels.
- Put the 24 words seed and then click "Restore"
- You will see that Blixt will start syncing with Neutrino. You can watch the sync logs too.
- KEEP IN MIND! Try to keep Blixt open all the time on this phase! Do not let it go on sleep or close the app screen. That could intrerrupte the initial sync and you have to do it again. Wait patiently, is not taking more then few minutes.
- Once the initial blocks sync is finished it will quickly scan your previous wallet addresses and then your channels will be back online, alive and well.
- Unfortunately the previous payments history and contacts is not possible (yet) to be restored. But that is not so important anyways.

And DONE! Now you have a fully restored Blixt LN node. It could work also with other LND backups (Umbrel, Raspiblitz etc) if you saved correctly previously the channel.db file. So Blixt can literally save any LND dead node.

---

## Blixt - Fourth Contact

This chapter is about customization and know better you Blixt Node. I will not describe all the features available, are too many and were already explained in the [Blixt Features Page](https://blixtwallet.github.io/features).

But I will point out some of those necessary to go forward using your Blixt and have a great experience.

### A - Name (NameDesc)

![blixt](assets/en/19.webp)

[The NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) is a standard for conveying "receiver name" in BOLT11 invoices.

This could be any name and can be changed anytime.

This option is really useful in various cases, when you want to send a name together with the invoice description, so the receiver could have a hint from who received those sats. This is fully optional and also in the payment screen, user have to tick the box indicating to send the alias name.

Here is an example of how would appear when you use [chat.blixtwallet.com](https://chat.blixtwallet.com/)

![blixt](assets/en/20.webp)

This is another example sending to another wallet app that support NameDesc:

![blixt](assets/en/21.webp)

### B - Lightning Box

Starting with the new v0.6.9-420 [recently announced](https://github.com/hsjoberg/blixt-wallet/releases/tag/v0.6.9-420), Blixt introduced a new powerful feature for Lightning Address in Blixt.

This new feature is optional opt-in, is not ON by default!

For the moment the default LN Box is run by Blixt server and offer a @blixtwallet.com LN Address. But ANYBODY with a LND public node can run the Lightning Box server and offer LN Address for its own domain, self-custody.

Right now, the Blixt server is only forwarding the payments sent to LN addresses @blixtwallet.com to the Blixt users that set their LN address. Users must put their Blixt node wallet in "persistent mode" in order to receive these payments to their @blixtwallet.com LN addresses.

See in the release notes the video demo about how to setup your LN Address in Blixt.

This LN address implemented into Blixt wallet app, is like a chat over LN, instant and fun, also supporting [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (adding an alias name to a payment). You can add in contact list all your regular LN addresses you are using frecquently and have it at hand for chatting. Now Blixt can be considered a full LN chat app 😂😂.

Another useful feature is the full support fro LUD-18 (that also [Stacker.News](https://stacker.news/r/DarthCoin) and others is supporting it).

![blixt](assets/en/22.webp)

As you can see in the screenshot above, sending from a Stacker News account, it displayed nicely the logo + LN address + message. Same way works for sending from Blixt, you can attach your Blixt LN Address or simply add the alias name (previously set in Blixt settings) or even both.

This option from LUD-18 could be useful also for subscription services, where user can send a specific alias (is NOT your node alias or your real name!) and based on that you could be registered or receive back a specific message or whatever else. Attaching an alias name ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ comment ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) to a LN payment can have multiple use cases!

Here is the code for [Lightning Box](https://github.com/hsjoberg/lightning-box) if you run it for yourself, for your family and friends, on your own node.

Here also you can run the [LSP Dunder server](https://github.com/hsjoberg/dunder-lsp) for Blixt mobile nodes and offer liquidity for Blixt users if you have a good public LN node (works only with LND).

### C - Backup LN Channels and seed words

This is a very important feature !

After opening or closing a LN channel you should do a backup. It can be done manually saving a small file on local device (download folder usually) or using a Google Drive or iCloud account.

![blixt](assets/en/23.webp)

Go to Blixt Settings - Wallet section. There you have the options to save all important data for your Blixt wallet:

- “Show mnemonic” - will display the 24 words seed to write them down
- “Remove mnemonic from device” - this is optional and use it only if you really want to remove the seed words from your device. This will NOT wipe your wallet, only the seed. But be aware ! There is not way to recover them if you did not write them down first.
- “Export channel backup” - this option will save a small file on your local device, usually into “downloads” folder, from where you can take it and move it outside your device, for safe keeping.
- “Verify channel backup” - this is good option if you use Google drive or iCloud to check the integrity of the backup done remotely.
- “ Google drive channel backup” - will save the backup file into your personal Google drive. The file is encrypted and is stored in a separate repository than your usual google files. So there are no concerns that can be read by anybody. Anyways that file is totally useless without the seed words, so nobody can take your funds from that file only.

I would recommend for this section the following:

- use a password manager to store safely your seed and backup file. KeePass or Bitwarden are very good for that and can be used on multiplatform and self hosted or offline.
- DO THE BACKUP EVERY TIME you open or close a channel. That file is updated with the channels info. There’s no need to do it after each transaction you’ve done on LN. The channel backup is not storing that info, is storing only the status of the channel.

![blixt](assets/en/24.webp)

---

## Blixt - Tips and Tricks

### CASE 1 - SYNCING PROBLEMS

"_My Blixt is not syncing... My Blixt do not show the balance... My Blixt cannot open channels... I tried to restore it in another device... etc_"

All these issues start because YOUR DEVICE IS NOT SYNCING PROPERLY. Please understand this important aspect: Blixt is a mobile LND node, that uses Neutrino for syncing / reading the blocks.

- Here's a less technical explanation from [Bitcoin Magazine](https://bitcoinmagazine.com/technical/why-bitcoin-wallets-need-block-filters)
- Here are more technical resources from [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Here is how you can activate Neutrino on your own home node and serve blocks filters for your mobile node, from [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core)

REMINDER: Using Neutrino over clearnet is totally safe, your IP or xpub are not leaked. You are just reading blocks from a remote node with neutrino. That's all. All the rest is done on your local device.

So there's NO NEED to use it with Tor. Tor will add a huge latency on your syncing process and will make your Blixt very unstable. If you really want to use over Tor, be sure what are you doing and have a good connection and patience. Same case for using a VPN. Be careful what latency is given to you from that VPN.

You can test the latency of a neutrino server by simply ping it, from a PC or from your mobile.

![blixt](assets/en/25.webp)

This is an usual ping to the neutrino server europe.blixtwallet.com, this shows that the connection is very good with a response time of avg 50ms and a TTL of 51. The response time can vary but not too much. TTL must be stable.

If these values are higher than 100-150ms then your syncing process will stale or even worse, it could cause closed channels by peers ! Do not ignore this aspect.

Without a proper sync, you also cannot see the correct balance or your LN channels will not get online and operational. No matter how many giga ultra terra mbps you have the download speed IT DOESN'T MATTER. It matter the time response and TTL (time to live).

This is like a general case for LATAM users. I don't know what happen down there but you guys have a terrible connection with pings of over 200ms that can disrupt any sync.

So what is the solution for these desperate users?

- stop using Blixt with Tor. Is totally useless
- you can use a VPN but choose it wisely and monitor all the time the ping. Use one that is closer to your geographical location. Distance means more ms response time, remember.
- select wisely your neutrino peers, here is a list of well known public neutrino servers:

```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```

Another way is to select one from this list of nodes announcing the "compact filters" (BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Choose one that is closer to your geographical location.

Another way (the best way) is to connect to a local community node, run by a friend or group that you know them, and is offering neutrino connection. [Here are the instructions how to do it.](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) Their node will not be affected in any way, they just need a stable and public connection.

There is a need for more neutrino servers in the LATAM region, for a better and fast sync. So please organize yourself, with your local Bitcoin community and decide who and where is running a Bitcoin Core + Neutrino for your own use. With just a public IP is enough. If you do not have access to a public IP, you can use a VPS IP and make wireguard tunnel to your home node. That way you redirect all the traffic to your local VPS IP, without revealing any private information about your home node.

### CASE 2 - NEVER FINISH SYNCING

"_My Blixt have good connection with neutrino server but is stuck syncing._"

#### Time Server

Sometimes people use various old devices or are not properly connected to a time server. Neutrino is syncing ok until reached the actual blocks that do not correspond to real local time. You will see in Blixt lnd logs an error saying that "block time stamp is far from future" or something related with "header don't pass sanity check".

Quick fix: set the correct time and date for your device and restart Blixt.

#### Low space on device

Sometimes using an old device, with low space, it can reach a threshold limit and stuck. Indeed for more you are using this mobile LND node, the neutrino files get bigger and also the channel.db file.

Quick fix: Go to Blixt Options - Debug section - Select "stop LND and delete neutrino files". It will restart the app and start a new fresh sync. Sometimes this quick fix can repair also corrupted data. Keep in mind that will take some time, between 1 and 3 min to fully resync. It is NOT deleting existing funds or channels, but yes, after resync it could trigger a re-scan of your bitcoin addresses and that could take more time.

Next step is to check how much data is still occupied. You can see this in Android App info - data. If is still bigger than 400-500MB, you can compact the lnd files. So go to Blixt Options - Debug section - Select "Compact DB LND". Restart Blixt app if is not doing automatically. The compaction is taking place at startup and is only once. Now you will see that Blixt data is more less occupied.

#### Persistent mode

Sometimes people do not open Blixt for long time, so is way too old the sync. But they expect to be synced instantly when they open it.

Please have patience, and look at the top spinning wheel. Optional you can go to Options - See Node Info and see if is synced to chain and synced to graph marked as "true". Without that "true" mention you cannot use properly Blixt, you cannot see correctly the balance, you cannot see the LN channels online, you cannot do payments.

Quick fix: There's a powerful option to "keep alive" your Blixt node. Go to Options - Experiments - Select "Activate Persistent Mode". That will restart your Blixt and will put the lnd service in persistent mode, aka will always be active and keep online your sync, even if you switch to another app or simply close Blixt (not force close or kill the task). You can keep it like that all day if you are in a stable connection and you need to use Blixt several times. It will not consume too much the battery.

### CASE 3 - I WANT TO MIGRATE TO ANOTHER DEVICE

OK about this scenario I wrote extensive guide on the [FAQ page](https://blixtwallet.github.io/faq#blixt-restore): with 2 options, fast (cooperative close of channels before migration) and slow (force close channels because old device is dead).

But I want to reiterate here some important aspects and add a new "secret" procedure.

REMINDER:

- Always do a backup of your channels status (SCB) AFTER each time you open or close a channel. It takes just few seconds to do it.
- Do not keep the old SCB files, to not get confused and restore them. Are totally useless and could trigger a penalty procedure if you se them. Always use the last version of the SCB file if you proceed to restore.
- Save the SCB file (is an encrypted text with the extension .bin) out of your device, in a safe place. You can use [LocalSend](https://github.com/localsend/localsend) for moving this file onto a PC or other device.
- Save also the seed of your Blixt wallet in a safe place, for example an offline password manager / encrypted USB.

Secret method: How to migrate Blixt node without closing the existing channels. For this you will need to read carefully the previous section "Third Contact" in this guide about "Restore wallet".

This procedure IT IS NOT FOR NOOBS, it is only for advanced users! That's why is not widely open and I recommend to do it only with assistance from Blixt devs or my support. Please do not ignore this advice.

### CASE 4 - WHAT PEERS TO USE TO OPEN CHANNELS?

As I wrote in [Blixt guides page](https://blixtwallet.github.io/guides) there are many ways to open channels with this mobile LND node. But some important aspects I would like to remind you here:

- open with well known LSP nodes and with community vouched peers. [See here a list](https://github.com/hsjoberg/blixt-wallet/issues/1033)
- do not open with random Tor only nodes. Those are worthless and you will get only issues of not being able to do payments. No matter how good is your friend "the node runner" with a shity Tor node in a jungle, it will never give you the best routes for a mobile private node. You do not open channels with somebody because is your friend. This is not Facebook! You open a channel for: good routes, small fees, availability.
- there's no need to open a shit ton of small channels, 2-3 or max 4, but with a good amount of sats. Do not open small channels, are totally useless. Smaller than 200k for a mobile have not much use.
- keep in mind the LSPs that offer inbound channels and JIT (just in time) channels. Those are very useful because you do not need to use any of your UTXOs, you can pay the opening channel with funds you already have in other LN wallets, stacking and preparing them for a bigger channel to open. You should use these JIT channels in your favor. [I've explained in this guide](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) more options for peers for private nodes like Blixt. Also [here in this guide posted on SN](https://stacker.news/items/679242/r/DarthCoin) I explained how to manage the private mobile nodes liquidity.

---

## Conclusion

OK, there are many other amazing features that Blixt offers, I will let you discover them one by one and have fun.

This app is really underestimated, mainly because is not backed by any VCs funding, is community driven, build with love and passion for Bitcoin and Lightning Network.

This mobile LN node, Blixt is a very powerful tool in hands of many users, if they know how to use it well. Just imagine, you are walking around the world with a LN node in your own pocket and nobody will know it.

And not talking about all other rich features that come with, that very few or none other wallet apps could offer.

Meanwhile here are all the links about this amazing Bitcoin Lightning Node:

- [Blixt Official Webpage](https://blixtwallet.com/)
- [Blixt Github page](https://github.com/hsjoberg/blixt-wallet/)
- [Blixt Features page](https://blixtwallet.github.io/features) - explaining one by one each feature and functionality.
- [Blixt FAQ page](https://blixtwallet.github.io/faq) - List of Q&A and troubleshooting of Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demos, video tutorials, extra guides and use cases for Blixt
- Download: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK direct download](https://github.com/hsjoberg/blixt-wallet/releases)
- [Telegram group for direct support](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Geyser crowdfunding page](https://geyser.fund/project/blixt) - donate sats as you like to support the project
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonymous LN chat
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - promo video (you can test your 1st use of LN)
- [Printable A4 flyer with first steps using Blixt, in various languages](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt also offers a full functional demo](https://blixt-wallet-git-master-hsjoberg.vercel.app/) right on its website or on a dedicated version web, to have a full experience testing, before start using in real world.

---
**DISCLAIMER:**

*I am not paid or supported in any way by the developers of this app. I wrote this guide because I saw that the interest in this wallet app is increasing and new users still don’t understand how to start with it. Also to help Hampus (the main dev) with documentation about using this node wallet.*

*I do not have any other interest in promoting this LN app, other than pushing forward the Bitcoin and LN adoption. This is the only way!*

---
