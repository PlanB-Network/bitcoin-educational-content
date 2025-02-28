---
name: Ocean Mining

description: Introduction to Ocean Mining
---

![signup](assets/cover.webp)

**May 2024**

Ocean Mining is a somewhat unique mining pool. Here, no accounts, no email addresses, no passwords are required. Just like Bitcoin, everything is transparent, pseudonymous, and contributors can choose from four different block templates.

### Compensation System

The compensation system of Ocean is called TIDES, "Transparent Index of Distinct Extended Shares". This system records the work provided by the miners, known as "shares". The pool calculates the percentage of "shares" for each contributor, then adds their Bitcoin address into the pool's block template as the beneficiary of this percentage of the block reward.

The block template is updated approximately every 10 seconds to account for the most lucrative new transactions and to change the distribution of the block reward if necessary.

![signup](assets/rem.webp)

Whether your machines are connected or not at the time the pool mines a new block does not matter. The work already submitted is kept for the next eight blocks found by the pool.

Keeping the work for eight blocks instead of resetting the counters to zero with each new block mined means that your compensation will only be 100% once the pool has found eight blocks after you started contributing. This also means that you will continue to be compensated for eight blocks if you stop contributing to the pool.

This mechanism smooths out the compensation and discourages "pool hopping", which involves switching pools regularly depending on which one is most likely to find the next block.

### Withdrawals

The operation of Ocean Mining allows its contributors to recover "clean" bitcoins, meaning bitcoins that are directly issued by the block reward.

Unlike the majority of other pools, Ocean does not receive the newly mined bitcoins; the contributors' addresses are directly integrated into the block template.

For now, the minimum amount to truly benefit from the clean bitcoins is 1,048,576 sats. With each block mined by the pool, your share of "shares" must entitle you to more than 1,048,576 sats for them to be directly paid to you by the block reward.
Otherwise, your sats will be kept by Ocean until your total rewards exceed this amount.

All bitcoins temporarily kept by Ocean are on this address: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, everything is verifiable on the TimeChain.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
It is also possible to withdraw your sats via Lightning using BOLT12. We will see how to set this up.

### Pool Fees

The fees range from 0% to 2% depending on the chosen block template.

## The Transparency of Ocean

### Contributor Data

![signup](assets/1.webp)

All the information about the pool is transparent, including all user data. To understand this point, let's take an example:

[On the Ocean dashboard](https://ocean.xyz/dashboard), you have numerous pieces of information like the hashrate over the last six months, the number of participants in the pool, the total number of bitcoins mined, etc.

We will focus on the "Contributors" section. You can see the list of all contributors with their average hashrate over the last three hours as well as the percentage of **"shares"** and **"hash"** relative to the rest of the pool.

**"Shares %"** is the percentage of work provided by the contributor in the window of the last eight blocks compared to the rest of the pool.

**"Hash %"** is the percentage of the average hashrate provided by the contributor over the last three hours compared to the rest of the pool.

![signup](assets/2.webp)

You will notice that the "Contributors" are identified by a Bitcoin address. You can click on any of these addresses for more details.

If we take the first one, the one with the highest hashrate [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), you can see all the details about this user: hashrate, number of bitcoins mined, with which block, and even the details of each of their machines (ASICs). However, they remain anonymous, as on Bitcoin.

### Block Template

At the top left on the dashboard, you have "Next block". On this page, there are four different block templates. Ocean allows each contributor to choose the block template they wish to support. This does not have a direct impact on your compensation. When the pool mines a block, all contributors are compensated regardless of the template they have chosen. This simply allows everyone to "vote" for the block template that suits them.

![signup](assets/3.webp)

**CORE:** Fee 2%, this is the classic Bitcoin Core template without filter, as written on their page "Includes transactions and the majority of spam"

**CORE+ANTISPAM:** Fee 0%, Bitcoin Core with a filter against certain transactions like Ordinals "Includes transactions and limits spam"

**OCEAN:** Fee 0%, Bitcoin Knot "Includes only transactions and reasonably small data"

**DATA-FREE:** Fee 0%, Bitcoin Knot "Includes only transactions without any arbitrary data"

### Distinction between Bitcoin Core and Bitcoin Knot
Bitcoin Core is the software that enables about 99% of Bitcoin nodes around the world to operate. Bitcoin is a protocol, which means that, just like the Internet, where there are multiple browsers, there can be several different software programs coexisting on the same TimeChain. However, out of concern for compatibility and to limit the risk of bugs that would leave indelible traces on the TimeChain, almost all Bitcoin developers work on Bitcoin Core. Bitcoin Knots is a fork of Bitcoin Core, meaning it shares the majority of their code, greatly limiting the risk of bugs. This fork was created by Luke Dashjr, who wanted to apply more restrictive rules than Bitcoin Core without creating a hard fork. Now, Bitcoin Core and Bitcoin Knots coexist thanks to Nakamoto consensus.

## Adding a Worker

To add a worker, start by choosing your block template. This choice will determine the pool URL to enter on your miner (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

Next, for the user field, enter a Bitcoin address you own. Here is the list of compatible address types:
- **P2PKH** (Original address type. Begins with “1”)
- **P2SH** (Multisignature or P2SH-Segwit. Begins with “3”)
- **Bech32** (Segwit. Begins with “bc”.)
- **Bech32m** (Taproot. Begins with “bc”. Longer than Bech32.)

If you have multiple miners, you can enter the same address for all of them so their hash rates are combined and appear as a single miner. You can also distinguish them by adding a distinct name to each. To do this, simply add “.workername” after the Bitcoin address.

Finally, for the password field, use `x`.

**Example:**
If you choose the **OCEAN** template, your Bitcoin address is `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` and you wish to name your miner “Brrrr”, then you will need to enter the following information in your miner's interface:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **USER**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **PASSWORD**: `x`

A few minutes after starting mining, you will be able to see your data on the Ocean site by searching for your address.

### Dashboard Overview
- **Shares in Reward Window**: This data indicates the number of shares, the work you have sent to the pool in the window of the last 8 blocks mined by the pool.
- **Estimated Rewards in Windows**: Estimate of the number of sats you will earn with the work already done. This does not take into account transaction fees, but only the coinbase, the new bitcoins issued by the network.
- **Estimated Earnings Next Block**: Estimate of the number of sats earned if a block is mined now. Remember, if this value is less than 1,048,576 sats, you will not directly receive the sats to your address. They will be sent to Ocean's address until your earnings exceed this threshold.

Below, you have a graph displaying your hashrate history up to 6 months.

![signup](assets/4.webp)

Here, you have your average hashrate over different time scales, from 60s to 24h, as well as the history of blocks mined by the pool for which you have contributed and been rewarded.

![signup](assets/5.webp)

You have the option to export a CSV file of this history with the **Download CSV** button.

![signup](assets/6.webp)

In the following section, you have a list of all the miners you have connected to the pool with this address. You have, of course, their individual hashrate, but also the number of sats they have individually received for their work.

![signup](assets/7.webp)

You can click on the **Nickname** of any miner. You will then have all the information we just saw, but specifically for that miner.

And at the bottom of the page, some additional information where you can see the history of payments on your address, the sats you have mined but have not yet been paid, and the total sats you have mined.

![signup](assets/8.webp)

Here, you can see that in the **Estimated Time Until Minimum Payout** box, it is written Lightning because we have set up a BOLT12 offer.

### Setting up Lightning Withdrawals

As you have understood, Ocean aims to maximize transparency and minimize custody (holding your sats on your behalf).

That's why, for Lightning withdrawals, it is necessary to use **BOLT12 offers**. This is a new way of making a payment on the Lightning network that is starting to emerge in 2024 and allows for several things:
- It's a reusable payment link, allowing for automatic payments and, unlike a Lightning address, the BOLT12 is non-custodial.
- It is also a payment method that provides proof that the payment was made, which is not the case with LNURLs.
- Very important, it can be used in conjunction with a Bitcoin signature to prove that you are both the holder of the BTC address and the BOLT12 offer.
As of today (May 2024), few solutions exist to use this method. In this example, we will use a Start9 server with Core Lightning. When other tools, such as Phoenix Wallet for example, have integrated BOLT12 offers, this tutorial will remain applicable. Make sure you have open channels with incoming liquidity, otherwise payments will not work.

Start by going to your dashboard on the Ocean site by entering your BTC address, then click on the **Configuration** tab.

![signup](assets/9.webp)

We will copy the **Description** text, here:
`OCEAN Payouts for bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Now go to your Core Lightning interface on your Start9 server (or any wallet capable of providing a BOLT12 offer).

![signup](assets/10.webp)

Click on **Receive**.

Check **Offer**, then paste the previously copied text into the **Description** field and leave the **Amount** field empty.

![signup](assets/11.webp)

Click on **Generate Offer**.

![signup](assets/12.webp)

You have generated a reusable and permanent payment link that does not require a central server as is the case with Lightning addresses. Copy the link and then return to the Ocean page.

In the **Lightning BOLT12 Offer** field, paste the payment link and leave the **Block Height** field at its default value. Click on **GENERATE**.

![signup](assets/13.webp)

For Ocean to ensure that this payment link is indeed yours without using an account system, you will need to sign the message that has just been generated with your private key corresponding to the Bitcoin address you are using. Many solutions exist to sign a message with your private key. In this tutorial, we will take the example of BlueWallet, but the method is the same for all wallets.

![signup](assets/14.webp)

Assuming your private key is in BlueWallet (you can do the same with a hardware wallet), click on the concerned wallet.

![signup](assets/15.webp)

Then on the **…** at the top right.

![signup](assets/15bis.webp)

And **Sign/Verify Message**.

![signup](assets/16.webp)

In this window, you have three fields: **Address**, **Signature**, and **Message**.

In the **Address** field, enter your Bitcoin address. If we go back to our example, it is the address: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

Leave the **Signature** field empty.
And paste the generated message into the **Message** field on Ocean's page: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`
Click on **Sign**.

This will generate a cryptographic signature that proves you are the owner of the address `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, and this signature is unique thanks to the message provided by Ocean, generated from the BOLT12 payment link.

![signup](assets/17.webp)

Copy the signature and paste it on Ocean's page, then click on **CONFIRM**.

![signup](assets/18.webp)

You should see a confirmation message.

![signup](assets/19.webp)

Now go to the **My Stats** tab. Additional information is displayed at the top with the BOLT12 payment link you previously generated with Core Lightning on Start9.

![signup](assets/20.webp)