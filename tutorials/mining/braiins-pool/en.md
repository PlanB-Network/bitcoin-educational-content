---
name: Braiins Pool

description: Introduction to Braiins Pool
---

![signup](assets/cover.webp)

Braiins Pool, formerly known as Slush Pool, is the very first Bitcoin mining pool. Established in November 2010, it mined its first block on December 16, 2010, block 97834.

As of May 2024, Braiins Pool has a computing power of 13 EH/s, representing about 1.8% of the total Bitcoin hashrate. It has mined a total of 1,307,188 bitcoins, which is approximately 6% of the maximum 21 million bitcoins that will ever exist.

### Compensation System

Since the end of 2023, Braiins Pool has changed its compensation system to adopt the FPPS (Full Pay Per Share) system. This means that miners receive rewards every day for all their work from the previous day, even if the pool did not find a block. This differs from the old system where miners only received a reward when the pool found a block.

**It is worth noting, [according to a tweet by Mononaut](https://x.com/mononautical/status/1777686545715089605) who analyzes the Bitcoin TimeChain, that many mining pools using the FPPS system would send the mined bitcoins to an address of AntPool, which would mean that AntPool controls the hashrate of all these pools, about 47% of the global Bitcoin hashrate. This is very bad news for the decentralization of the network.**

### Pool Fees

The fees for Braiins Pool are 2.5%, however, if you use BraiinsOS on your machines the fees will be 0%

### Withdrawals

**Lightning Withdrawals**
Lightning withdrawals allow you to withdraw your rewards with no minimum amount once a day via a Lightning address. 
To use this method, you must have a wallet compatible with Lightning addresses.

**On-Chain Withdrawals**
On-Chain withdrawals are limited to a minimum amount and may be subject to fees. 
Minimum amount: 20,000 sats
Fees: 10,000 sats for amounts less than 500,000 sats
Free for amounts over 500,000 sats
Withdrawals can be triggered by time interval or by amount.

## Account Creation

To start using Braiins Pool [go to their website](https://braiins.com/pool) and click on "SIGN UP" at the top right


![signup](assets/3.webp)

Enter your information and validate, you will then receive an email requesting confirmation of your address. Confirm with the link in the email you received and then log in to the platform

![signup](assets/4.webp)


## Adding a "worker"
A worker is the miner that you will connect to the pool. To add a new miner, click on "Workers" in the left sidebar menu.
![signup](assets/7.webp)

Then click on the purple "Connect Workers +" button.

In this window, select your geographical area.

If the miner you want to connect uses BraiinsOS, select the "Stratum V2" protocol. Otherwise, choose "Stratum V1".

![signup](assets/8.webp)

You will have the information to enter on your miner's web page (refer to your miner's documentation to know where to enter this information).

Here, **"stratum+tcp://eu.stratum.braiins.com:3333"** is the pool URL.

**JimZap.workerName** is your identifier and the name of your miner, where JimZap is the identifier and .workerName is the name of the miner. If you have multiple miners, you can either give them the same name, in which case their computing power will be added together on the dashboard, or give them different names to monitor them individually.

And the password is always the same **"anything123"**

Once you have entered this information on your miner's web page and it has started mining, you will see it appear after a few minutes on the Braiins Pool Dashboard.

## Dashboard Overview

![signup](assets/9.webp)

In the top banner, you can see the average total hashrate of all your miners over 5 minutes, 1 hour, and 24 hours. And a summary of the number of miners online or offline.
Below, a chart allows you to follow the evolution of your computing power.

![signup](assets/10.webp)

Below this chart, you have several pieces of information about your rewards in sats.

**"Today's Mining Rewards"** Indicates the number of sats you have mined today. At the end of the day, this value will be reset to 0 and the sats will be sent to your account.

**"Yesterday's Total Reward"** The number of sats you mined the day before

**"Est. Profitability (1 TH/s)"** Is an estimate of the number of sats you earn in one day for a computing power of 1 TH/s. For example, if the value is 77 sats, and you have a computing power of 10 TH/s continuously throughout the day, then you would theoretically earn 77 x 10 = 770 sats per day.

**"All Time Reward"** The total sats you have mined with Braiins Pool

**"Reward Scheme"** The fee rate applied by the pool

**"Next Payout ETA"** Estimate of the time it will take before you can withdraw the sats from the platform. Here, the estimate shows nothing because mining has only been underway for a few minutes.

**"Account Balance"** The number of sats available in your account, which you can then withdraw.
## Setting Up Withdrawals
You can withdraw your rewards either on-chain or via lightning with an address.

At the top, click on "Funds". By default, you have a "Bitcoin Account". You can create others to share the rewards. We will return to this in the next section.

For now, click on "Set up".

![signup](assets/17.webp)

In this new window, you can choose "Onchain payout".

Name this wallet, provide a BTC address, and select the type of trigger you want. "Threshold" means that the payment will be triggered when you have accumulated a defined amount of BTC, and with "Time interval", the payment will be triggered at regular intervals (day/weeks/months).

Note that the minimum amount is 0.0002 BTC and that below 0.005 BTC, a fee of 0.0001 BTC will be applied.

![signup](assets/18.webp)

If you want to use Lightning withdrawals, you will need a wallet that provides a Lightning address. For example, you can use getAlby.

Click at the top of the window on "Lightning payout".

Enter your Lightning address and check the box "I understand..." then validate.

With this withdrawal method, your rewards will be sent to your wallet every day.

![signup](assets/14.webp)

Once you have validated your payout settings, you will receive a confirmation email.

![signup](assets/15.webp)

## Sharing Rewards

Braiins Pool also allows you to share your rewards across multiple wallets.

To do this, click at the top on "Mining" then on the left on "Settings".

![signup](assets/19.webp)

On this page, you will be able to add other "Financial Account" by clicking on "Add Another Financial Account" and distribute your rewards in % across these different accounts to which you must associate a wallet. To associate a new wallet with a Financial Account, refer to the previous section.