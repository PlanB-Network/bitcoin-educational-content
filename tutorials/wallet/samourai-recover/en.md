---
name: Samourai Wallet - Recover
description: How to recover bitcoins stuck on Samourai Wallet?
---
![cover](assets/cover.webp)

Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, some functionalities of the application are now inoperative, and users who do not have their own Dojo can no longer broadcast transactions.

After assisting several users in recovering their bitcoins in recent days, I believe I have encountered most of the issues that may arise during the restoration of a Samourai Wallet. Therefore, this tutorial will start with a situation report to identify the functionalities that remain operational and those that are no longer available within the Samourai Wallet ecosystem and the software affected by this incident. Next, we will proceed step by step to recover a Samourai Wallet using the Sparrow Wallet software. We will examine all potential obstacles encountered during this process and see solutions to resolve them. Finally, in the last part, you will discover the potential risks to your privacy following the server seizure.

*A big thank you to [@Louferlou](https://twitter.com/Louferlou), who has assisted several users in their recovery and shared his experiences with me, and who has also contributed to testing to determine what is still functional.*

## Is Samourai Wallet still working?

Yes, **the Samourai Wallet app is still working**, but under certain conditions.

Firstly, it is necessary that the app had been previously installed on your smartphone. The Google Play Store has removed the app, and the APK was hosted on the seized website. Therefore, it is complicated to install Samourai at the moment. You might find APKs online, but I advise against downloading them unless you are sure of the source.

Given that the Samourai Wallet page is no longer available on the Google Play Store, it is not possible to disable automatic updates. If the app returns to the download platforms, it would be wise to **disable automatic updates** until more information is available regarding the development of the case.

If Samourai Wallet is already installed on your smartphone, you should still be able to access the app. To use the wallet functionality of Samourai, it is essential to connect a Dojo. Previously, users without a personal Dojo depended on Samourai's servers to access Bitcoin blockchain information and to broadcast transactions. With the seizure of these servers, the app can no longer access this data.
If you didn't have a connected Dojo before but have one now, you can set it up to use your Samourai app again. This involves checking your backups, deleting the wallet (the wallet, not the application), and recovering the wallet by connecting your Dojo to the application. For more details on these steps, you can consult [this tutorial, in the section "_Preparing your Samourai Wallet_" : COINJOIN - DOJO](https://planb.network/en/tutorials/privacy/coinjoin-dojo).
If your Samourai app was already connected to your own Dojo, then the wallet part works perfectly for you. You can still see your balance and broadcast transactions. Despite everything that's happening, I think Samourai Wallet remains the best mobile wallet software at the moment. Personally, I plan to continue using it.

The main problem you might encounter is the inaccessibility of Whirlpool accounts from the app. Usually, Samourai tries to establish a connection with your Whirlpool CLI and start the coinjoin cycles before giving you access to these accounts. However, since this connection is no longer possible, the app continues to search indefinitely without ever giving you access to the Whirlpool accounts. In this case, you can recover these accounts on another wallet software while only keeping the deposit account on Samourai.

### What tools are still available on Samourai?

On the other hand, some tools are either affected by the server shutdown or completely unavailable.

Regarding individual spending tools, everything works normally provided, of course, that you have your own Dojo. Normal Stonewall transactions (and not Stonewall x2) work without any problem.

Comments on Twitter have highlighted that the privacy offered by a Stonewall transaction might now be reduced. The added value of a Stonewall transaction lies in the fact that it is indistinguishable from a Stonewall x2 transaction in terms of structure. When an analyst encounters this specific pattern, they cannot determine whether it is a standard Stonewall with a single user or a Stonewall x2 involving two users. However, as we will see in the following paragraphs, carrying out Stonewall x2 transactions has become more complex due to the unavailability of Soroban. Some therefore think that an analyst might now assume that any transaction with this structure is a normal Stonewall. Personally, I do not share this assumption. Although Stonewall x2 transactions may be less frequent (and I think they were already before this incident), the fact that they are still possible can invalidate an entire analysis based on the assumption that they are not.
**[-> Learn more about Stonewall transactions.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**
Regarding Ricochet, I have not been able to verify if the service is still operational, due to not owning a Dojo on the Testnet, and I prefer not to risk spending `100 000 sats` towards a wallet that could be controlled by the authorities. If you have had the opportunity to test this tool recently, I invite you to contact me so we can update this article.

If you need to use Ricochet, be aware that you can always perform this operation manually with any wallet software. To learn how to manually perform the various hops properly, I recommend consulting this other article: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

The JoinBot tool is no longer operational, as it was entirely dependent on the participation of a wallet managed by Samourai.

Regarding other types of collaborative transactions, often referred to as "cahoots," they remain possible, but only manually. Before the server shutdown, you had two options for performing Stonewall x2 or Stowaway (PayJoin) transactions:
- Use the Soroban network to automatically and remotely exchange the PSBTs;
- Or perform these exchanges manually by scanning multiple QR codes.

After several tests, it appears that Soroban is no longer functioning. To perform these collaborative transactions, the exchange of data must therefore be done manually. Here are two options for performing this exchange:
- If you are physically close to your collaborator, you can scan the QR codes successively;
- If you are distant from your collaborator, you can exchange the PSBTs via an external communication channel to the application. However, be careful, as the data contained in these PSBTs are sensitive in terms of privacy. I recommend using an encrypted messaging service to ensure the confidentiality of the exchange.

**[-> Learn more about Stonewall x2 transactions.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4-x2)**

**[-> Learn more about Stowaway transactions.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**

As for Whirlpool, the protocol no longer seems to function, even for users who have their own Dojo. I have been monitoring my RoninDojo these past few days and attempted some basic manipulations, but the Whirlpool CLI has not been able to connect since the server shutdown.

However, I remain hopeful that this protocol can be reactivated or perhaps reimagined differently in the coming weeks, depending on how the situation evolves. This pause could be an opportunity to explore new approaches or potential improvements to this system.
### What external tools are still available?
Regarding other tools related to the Samourai environment, some are still available while others are not.

The free chain analysis website OXT.me is unfortunately no longer available for the time being.

The Whirlpool Stats Tool is no longer available for download, as it was hosted on Samourai's GitLab. Even if you had previously downloaded this Python tool locally on your machine, or if it was installed on your RoninDojo node, WST will not work for the time being. Indeed, it depended on data provided by OXT.me for its operation, and this site is no longer accessible. Currently, WST is not particularly useful since the Whirlpool protocol is inactive.

The KYCP.org site is currently no longer accessible.

The GitLab that hosted the code for the Boltzmann Calculator Python tool has also been seized. At this time, it is therefore no longer possible to download this tool. But if you have a RoninDojo, you can continue to use Boltzmann Calculator in the same way as before.

As for RoninDojo, this node-in-box software continues to function correctly despite the unavailability of certain specific tools such as Whirlpool CLI and WST. It can still be used for other wallet software thanks to Fulcrum or Electrs. If you wish to obtain more information about RoninDojo or if you have specific questions, I encourage you to join [their Telegram group](https://t.me/RoninDojoNode).

However, the source code for RoninDojo is currently no longer accessible, as it was hosted on Samourai's GitLab. It is therefore not possible to manually install it on a Raspberry Pi at the moment.

Regarding the watch-only wallet software Sentinel, the situation is similar to that of the Samourai app. If you have your own Dojo, you can continue to use Sentinel without any problem. However, if you do not have a Dojo, you will no longer be able to establish a connection. Unlike Samourai, the Sentinel website is still accessible online. But be cautious with this site and the APK offered there, as it is unclear who currently controls these resources.

### Is Sparrow Wallet affected?

Sparrow Wallet continues to operate normally, with the exception of Samourai tools that are no longer available. Currently, it is no longer possible to perform coinjoins via Sparrow. Similarly, collaborative spending tools are no longer accessible, as Sparrow does not offer the option of manual exchange of PSBTs, unlike Samourai. For all other functionalities, Sparrow operates without issue. You can also use this software to recover a Samourai wallet if necessary.
## How to Recover a Samourai Wallet?
As we have seen in the previous sections, if you own your own Dojo, it's not necessarily required to switch software. **Samourai remains an excellent choice of hot wallet** for your daily spending. However, if you do not have a Dojo or if you prefer to opt for another software, I will explain the complete recovery process, detailing any potential obstacles you might encounter.

In any case, it's important to take your time and ensure not to make any mistakes. Remember, there's no rush, as you hold your private keys, and the seizure of Samourai's servers does not affect this in any way. Whatever happens, they obviously cannot access your private keys.

### Verify the passphrase

To recover your wallet, you must have your passphrase, even if you opt for recovery via the backup file. Start by verifying the validity of this passphrase. Open your Samourai Wallet app, click on your Paynym icon at the top left, then select `Settings`.

![samourai](assets/1.webp)

Next, click on `Troubleshooting` and then on `Passphrase/backup test`.

![samourai](assets/2.webp)

Enter your passphrase and click `Ok`. If it is correct, Samurai will confirm it. You also have the option to verify the backup file if you plan to use it later.

![samourai](assets/3.webp)

This step is optional but recommended. It confirms that the passphrase is correct, eliminating a potential source of problems later on. If Samourai indicates that the passphrase is incorrect at this stage, recovery will not be possible. Make sure you have entered the passphrase correctly and check it again.

### Option 1: Recover the wallet on Sparrow with the backup file

Since version 1.8.6 of Sparrow Wallet, it is possible to directly import your Samourai wallet using the backup text file named `samourai.txt`, which your application automatically generates. This file contains all the necessary information to recover your wallet and is encrypted with your passphrase for security.

If you choose this option, you will need your up-to-date `samourai.txt` file and your passphrase. To generate this file on Samourai Wallet, click on the three small dots at the top right, then select `Export wallet backup`.

![samourai](assets/4.webp)
Next, choose `Export to Clipboard`. After that, you will need to transfer this file to your PC securely. Since the file is encrypted, but the passphrase alone is sufficient to decrypt it, it's important to take precautions during its transmission. If you opt for a direct transfer as plain text, you will need to create a `samourai.txt` file on your PC and paste the contents of the clipboard into it. An alternative would be to directly retrieve the `samourai.txt` file from the files stored on your phone.
Once you have access to the file on your PC, open Sparrow Wallet, click on the `File` tab, and select `Import Wallet` to start importing your wallet.

![samourai](assets/5.webp)

Scroll down to `Samourai Backup`, click on `Import File`, and then select your `samourai.txt` file.

![samourai](assets/6.webp)

Sparrow will then ask you for a password to decrypt the file. This password is actually your passphrase. Enter it in the corresponding field and click on `Import`.

![samourai](assets/7.webp)

If at this stage, your wallet does not appear, it is possible that you made a mistake when copying the `samourai.txt` file or when entering the passphrase. You can consult the troubleshooting section for more help.

![samourai](assets/8.webp)

For the script type, if you haven't configured other scripts in Samourai, you should normally use only SegWit V0 (Native SegWit / P2WPKH). Keep this default script and click on `Import`.

![samourai](assets/9.webp)

Name your wallet, for example, "Samourai Recovery", and then click on `Create Wallet`.

![samourai](assets/10.webp)

Sparrow will then ask you to choose a password. This password only protects access to your wallet on this PC and does not pertain to the derivation of your wallet's keys. Make sure to choose a strong password, note it down to remember it, and click on `Set Password`.

![samourai](assets/11.webp)

Sparrow will then derive the keys of your wallet and search for the corresponding transactions.

![samourai](assets/12.webp)

For now, only your deposit account is accessible. If you were using Samourai for this account only, you should see all your funds. However, if you were also using Whirlpool, you will need to derive the `premix`, `postmix`, and `badbank` accounts. On Sparrow, simply click on the `Settings` tab, then on `Add Accounts...`.

![samourai](assets/13.webp)
In the window that opens, select `Whirlpool Accounts` from the dropdown menu, then click on `OK`.
![samourai](assets/14.webp)

You will then see your various Whirlpool accounts appear, and Sparrow will derive the necessary keys to use the associated bitcoins.

![samourai](assets/15.webp)

If you are using a different software than Sparrow, like Electrum, to recover your Samourai wallet, here are the Whirlpool account indexes for manual recovery:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

You now have access to your bitcoins on Sparrow. If you need help using Sparrow Wallet, you can also check out [our dedicated tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

I also recommend manually importing the labels you had associated with your UTXOs on Samourai. This will allow you to perform effective coin control on Sparrow subsequently.

### Option 2: Recover the wallet on Sparrow with the mnemonic phrase

If you do not wish to perform the recovery with the backup file, you can opt for a more traditional method by simply using your 12-word recovery phrase and your passphrase. This second option is often simpler.

To start, make sure you have your recovery phrase and your passphrase at hand. Then, open the Sparrow Wallet software, click on the `File` tab, and select `Import Wallet` to begin importing your wallet.

![samourai](assets/16.webp)

Choose `Mnemonic Words (BIP39)` and, in the dropdown menu, click on `Use 12 Words`.

![samourai](assets/17.webp)

Enter the 12 words of your recovery phrase in the correct order.

![samourai](assets/18.webp)

If Sparrow displays an `Invalid Checksum` message, this indicates that the checksum of the recovery phrase is not valid, which probably means you made a mistake when entering the words.

![samourai](assets/19.webp)

If your phrase is correct, check the `Use Passphrase?` box and enter your passphrase in the dedicated field. Finally, if everything seems correct, click on the `Discover Wallet` button.

![samourai](assets/20.webp)

Name your wallet, for example, "Samourai Recovery", then click on `Create Wallet`.

![samourai](assets/21.webp)
Sparrow will then ask you to choose a password. This password only protects access to your wallet on this PC and does not relate to the derivation of your wallet's keys. Make sure to choose a strong password, write it down to remember it, and click on `Set Password`.
![samourai](assets/22.webp)

Sparrow will then derive the keys for your wallet and search for corresponding transactions.

![samourai](assets/23.webp)

If at this stage, your wallet does not appear, it is possible that you made a mistake when entering the passphrase or recovery phrase. You can consult the dedicated troubleshooting section for more help.

For now, only your deposit account is accessible. If you were using Samourai for this account only, you should see all your funds. However, if you were also using Whirlpool, you will need to derive the `premix`, `postmix`, and `badbank` accounts. On Sparrow, simply click on the `Settings` tab, then on `Add Accounts...`.

![samourai](assets/24.webp)

In the window that opens, select `Whirlpool Accounts` from the dropdown list, then click on `OK`.

![samourai](assets/25.webp)

You will then see your various Whirlpool accounts appear, and Sparrow will derive the necessary keys to use the associated bitcoins.

![samourai](assets/26.webp)

If you are using another software like Electrum to recover your Samourai wallet, here are the Whirlpool account indexes for manual recovery:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

You now have access to your bitcoins on Sparrow. If you need help using Sparrow Wallet, you can also consult [our dedicated tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

I also recommend manually importing the labels you had associated with your UTXOs on Samourai. This will allow you to perform effective coin control on Sparrow subsequently.

### What are the common problems encountered?

After assisting several people in the past few days, I believe I have encountered most of the problems that can prevent the recovery of your wallet. If you still cannot access your wallet despite the previous tutorials, here are some additional recommendations.
First and foremost, for the recovery to work, it is absolutely essential that the recovery phrase is correct. If you are unable to find your 12-word phrase, you can use *option 1* to recover from Samourai's backup file. You can also access your recovery phrase directly in Samourai Wallet by navigating to `Settings`, then `Wallet`, and finally selecting `Show 12-word recovery phrase`.

Next, a typing error in your passphrase during recovery will result in incorrect derived keys, which will prevent the recovery of your wallet on Sparrow. **The passphrase must be perfectly accurate!**

To resolve this, I first advise you to check the validity of your passphrase in the Samourai application as described in the "_Verify the passphrase_" section of this article:
1. **Validation in Samourai:** If Samourai confirms that the passphrase is correct, try the recovery again from the beginning, making sure to accurately enter the passphrase in Sparrow without error;
2. **Passphrase Error:** If Samourai indicates that the passphrase is incorrect, it is pointless to continue attempts on Sparrow. As long as the correct passphrase is not found, the recovery of your wallet is impossible. If you have permanently lost your passphrase, keep your Samourai application safe. All you can do is hope that the servers are restarted so that you can make expenditures directly from the application without needing recovery. **Do not attempt to connect a Dojo in this case**, as this would imply resetting your wallet on Samourai, which requires access to the passphrase.

Among other encountered errors, many are related to the network configuration on Sparrow.

First, ensure that Sparrow is correctly configured in `mainnet` mode rather than in `testnet` mode. Indeed, if Sparrow searches for your transactions on the Testnet, it will find nothing, because your wallet is on the Mainnet. The Testnet is an alternative version of Bitcoin, used solely for testing and development, and operates on a separate network from the main network (Mainnet), with its own blocks and transactions. To check which network you are on, click on the `Tools` tab, then on `Restart In`. If the `Mainnet` option is displayed, then you are not on the main network. Select it to restart Sparrow on the Mainnet, and then begin your recovery process again.

![samourai](assets/27.webp)
Some have also encountered difficulties connecting Sparrow to their node. At the bottom right of Sparrow, a colored switch indicates whether your software is correctly connected to a Bitcoin node. To retrieve your Samourai transactions, it is essential that the software is well connected. Check that the switch is activated, as in my image below (yellow for a public node, green for Bitcoin Core, and blue for an Electrum server).
![samourai](assets/28.webp)

If the switch is not activated, click on it to reactivate the connection.

![samourai](assets/29.webp)

If the problem persists, here are some possible solutions:
- If you are trying to connect to your own Electrum server (blue) or your Bitcoin Core (green) and Sparrow cannot connect, check the connection information under `File > Preferences... > Server`;

![samourai](assets/30.webp)

- If the connection problem persists, it could be due to an incomplete synchronization of your node. Ensure that your node and your indexer are 100% synchronized. If necessary as a last resort, disconnect your node from Sparrow and connect to a public node;
- If you were already connected to a public node and the connection fails, try changing the node by selecting another one from the dropdown list.

![samourai](assets/31.webp)

If you have successfully recovered your wallet, but it seems incomplete, there might be a problem related to derivation.

A problem could occur if you used your Samourai deposit account with a different script type than `P2WPKH`. By default, Samourai uses this script type, but if you have manually changed it, you must also adjust this when recovering on Sparrow.

To derive branches for other script types, you need to repeat the recovery process for each script type used. For this, go to `File > New Wallet` on Sparrow, select another script type from the dropdown list, click on `New or Imported Software Wallet`, and follow the same steps as in the initial tutorial.

![samourai](assets/32.webp)

Another derivation problem I encountered is related to the Gap Limit value. This value tells Sparrow after how many empty addresses it should stop deriving new addresses. If after recovery, you notice that some transactions are missing, this could be due to a too low Gap Limit. To solve this, go to the account that is causing the problem, for example, the postmix account (if several accounts are concerned, repeat this operation for each).

![samourai](assets/33.webp)

Click on the `Settings` tab and then on the `Advanced...` button.
![samourai](assets/34.webp)
Gradually increase the value of the Gap Limit, for example, I set it to `400` here. Then, click on the `Close` button.

![samourai](assets/35.webp)

Click on `Apply` to finalize. Sparrow will then derive a larger number of addresses and search for funds on them, which should help recover all of your transactions.

![samourai](assets/36.webp)

That covers the various recovery issues I've encountered over the last few days. If, after trying all these solutions, you're still having trouble, I invite you to join [the Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) to ask for help. I regularly visit this Discord and would be delighted to help if I have the solution. Other bitcoiners will also be able to share their experiences and offer their assistance. **In any case, it is essential to keep your recovery phrase, your backup file, and your passphrase confidential**. Do not share them with anyone, as this could allow them to steal your bitcoins.

Once the recovery is complete, you now have access to your bitcoins. That's a good thing, but it might not be enough. Indeed, the seizure of servers raises new potential risks for your privacy. In the following section, we will examine these risks in detail and outline the precautions to take to protect your privacy.

## What are the consequences for the privacy of your transactions?

### As a Samourai user without Dojo

If you were using Samourai Wallet without having connected your own Dojo, your xpubs had to be communicated to Samourai's servers for the app to function. With the seizure of these servers, it's possible that authorities now have access to these xpubs.

This scenario remains hypothetical. We do not know if these xpubs were recorded, if any potential storage was destroyed, if the authorities have recovered them, and if they plan to use them for chain analysis. However, in such a situation, it is prudent to consider the worst-case scenario, where the authorities have the xpubs of users who did not connect their own Dojo.
For reference, an xpub is a string of characters that contains all the necessary elements for generating child public keys (public key + chain code). It is used in hierarchical deterministic wallets to generate receiving addresses and observe transactions of an account without exposing the associated private keys. This allows, for example, the creation of a "watch-only" wallet. However, disclosing xpubs can compromise the user's privacy, as they allow third parties to track transactions and see the balances of associated accounts.
Anyone who knows your xpubs can thus see all the receiving addresses of your wallet, those used in the past, and those that will be generated in the future.

For users without a Dojo, a potential leak of your xpubs has two major consequences:
- The coinjoins you may have performed are rendered ineffective from a privacy standpoint for anyone who knows your xpubs, thus your coins lose all anonset;
- This person can also track all the receiving addresses of your Samourai Wallet.

It is therefore important to consider the worst-case scenario and to part with this wallet, potentially compromised in terms of privacy. To do this, create a new wallet from scratch with another software, like Sparrow Wallet. After verifying the validity of your backups, transfer all your funds by making transactions. Although this operation does not break the traceability link of your coins, it will prevent the authorities from knowing with certainty the addresses of your new wallet.

During this transfer operation, I recommend avoiding the consolidation of your coins. If we assume that your xpubs are compromised, consolidation will have no impact from the viewpoint of the person having access to these xpubs, since your privacy is already compromised with them. However, I advise you not to consolidate your coins too much mainly to protect your privacy from other people. In the worst case, only the authorities might have access to your xpubs, but the rest of the world does not know about them. Thus, from the viewpoint of others, consolidating your coins could significantly harm your privacy because of the Common Input Ownership Heuristic (CIOH).

Finally, to definitively break the tracking, also consider performing coinjoins from this new wallet.
**Warning:** Simply retrieving your Samourai wallet on Sparrow Wallet is not enough. It is necessary to create an entirely new wallet with a new recovery phrase if you want to avoid using xpubs that may have leaked. If you import your existing seed into Sparrow, you are only changing the wallet management software, but the wallet remains the same.

### As a user of Sparrow or Samourai with Dojo

If your wallet is only managed on Sparrow Wallet, your xpubs could not have leaked, whether you are using a public node or your own Bitcoin node. Similarly, if you are using the Samourai app and have always connected this app to your own Dojo since the creation of your wallet, your xpubs are also secure.

However, if you have used the same wallet during a period **without your own Dojo** and then with your own Dojo, it is possible that the Samourai servers might have had access to your xpubs, and therefore the authorities could know them. If you are in this specific situation, I advise you to follow the recommendations of the previous section and consider your xpubs as compromised.

For those who have always used Sparrow or Samourai with their own Dojo, the main risk is that the anonsets of your coins could potentially be reduced. Suppose, in the worst-case scenario, that all users without a Dojo have their xpubs in the hands of the authorities, then the path of their coins through the coinjoin cycles could be traced by these authorities.

To illustrate this, let's take a concrete example. Imagine that you participated in a first cycle of coinjoin, followed by two additional downstream coinjoin cycles. If the xpubs of users without a Dojo have not leaked, then the prospective anonset of your coin would be 13.

![samourai](assets/37.webp)

However, if we consider that the xpubs have leaked and that you encountered a user without a dojo during the initial coinjoin, and then 2 during the first downstream coinjoin, then your prospective anonset would only be 10 instead of 13 from the authority's point of view.

![samourai](assets/38.webp)
This potential decrease in anonset is complex to quantify, as it depends on numerous factors, and each coin is affected differently. For example, a user without Dojo encountered in the early cycles affects the prospective anonset much more than one encountered in the later cycles. To give you an idea of the situation, which remains hypothetical, the latest statistics provided by Samourai indicated that between 85% and 90% of the coins involved in coinjoins came from users with Dojo, Sparrow, or Bitcoin Keeper, that is, users who, even in the worst-case scenario, would not have seen their xpubs leaked.
Although these figures are difficult to verify, they seem consistent to me for two reasons:
- Sparrow Wallet is widely used;
- Most node-in-box software offers Dojo implementations, and these mainstream software like Umbrel are very popular nowadays.

Thus, several aspects need to be considered. If the privacy of your coins vis-à-vis the authorities is extremely important to you, it would be prudent to prepare for the worst scenario, and it is difficult to guarantee 100% that your Whirlpool coinjoin cycles could not be traced due to the potential leak of xpubs from users without Dojo. Although this assumption is highly unlikely, it is not impossible.

On the other hand, if the privacy of your coins vis-à-vis the authority potentially in possession of these xpubs is not crucial for you, then the situation can be considered differently.

I specify "vis-à-vis the authority" because it is important to remember that only the authority that seized the servers is potentially aware of these xpubs. If your goal in using coinjoin was to prevent your baker from being able to follow your funds, then he is no better informed than before the server seizure.

Finally, it is essential to consider the initial anonset of your coin, before the server seizure. Let's take the example of a coin that had reached a prospective anonset of 40,000; the potential decrease in this anonset is probably negligible. Indeed, with an already very high base anonset, it is unlikely that the presence of a few users without Dojo could radically change the situation. However, if your coin had an anonset of 40, then this potential leak could seriously affect your anonsets and potentially allow tracing.
With the WST tool now out of service following the shutdown of OXT.me, you can only estimate these anonsets. For the retrospective anonset, there's not too much to worry about since the Whirlpool model ensures that it is very high from the first coinjoin, thanks to the legacy of your peers. The only case where this could pose a problem is if your coin hasn't been remixed for several years and it was mixed at the beginning of a pool's launch. Regarding the prospective anonset, you can examine the duration your coin has been available for coinjoins. If it has been several months, then it probably has an extremely high prospective anonset. Conversely, if it was added to a pool just a few hours before the servers were seized, then its prospective anonset is probably very low.
[**-> Learn more about anonsets and their calculation method.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

Another aspect to consider is the impact of consolidations on the anonsets of coins that have been mixed. Given that Whirlpool accounts are no longer accessible via the Samourai app, it is likely that many users have transferred their wallet to other software and attempted to withdraw their funds from Whirlpool. In particular, last weekend, when transaction fees on the Bitcoin network were relatively high, there was a strong technical and economic incentive to consolidate post-mix coins. This means that it is likely that many users have made significant consolidations.

The problem with these post-mix consolidations is that they always reduce the anonsets, not only for the user who performs them but also for the users they encountered during their coinjoin cycles. Although I have not been able to verify or quantify this phenomenon precisely, the economic incentives related to transaction fees at that time can lead us to assume that the anonsets are potentially lower.

### As a Sentinel User

The network operation of the watch-only wallet application Sentinel is similar to that of Samourai. To access your wallet information, the application must transmit the xpubs, public keys, and addresses you have provided to a Dojo. If you have always used your own Dojo on Sentinel, there is no problem, and you can continue to use the application without worry. However, if you were dependent on Samourai's servers for your Sentinel, it is possible that your xpubs have been exposed. In this case, it is advisable to follow the same wallet change process recommended for Samourai Wallet when connected to Samourai's servers.

In the unlikely event that you were using your Dojo with Samourai but not with Sentinel, it would be wiser to consider that your xpubs are compromised.

## Conclusion
Thank you for reading this article to the end. If you think information is missing or if you have suggestions, please do not hesitate to contact me to share your thoughts. Additionally, if you need further assistance in recovering your Samourai Wallet despite this tutorial, I invite you to join [the Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) to ask for help. I regularly visit this Discord and would be delighted to assist you if I have the solution. Other bitcoiners will also be able to share their experiences and offer their support. **In any case, it is essential to keep your recovery phrase, your backup file, and your passphrase confidential**. Do not share them with anyone, as this could enable them to steal your bitcoins.