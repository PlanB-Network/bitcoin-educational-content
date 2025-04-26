---
name: Whirlpool Stats Tools - Anonsets
description: Understand the concept of anonset and how to calculate it with WST
---
![cover](assets/cover.webp)

***WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, the Whirlpool Stats Tool is no longer available for download, as it was hosted on Samourai's Gitlab. Even if you had previously downloaded this tool locally to your machine, or it was installed on your RoninDojo node, WST will not function at this time. It relied on data provided by OXT.me for its operation, and this site is no longer accessible. Currently, WST is not particularly useful since the Whirlpool protocol is inactive. However, it remains possible that these softwares might be reinstated in the coming weeks. Moreover, the theoretical part of this article remains relevant for understanding the principles and goals of coinjoins in general (not just Whirlpool), as well as understanding the effectiveness of the Whirlpool model. You can also learn how to quantify the privacy provided by coinjoin cycles.*

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

---

> *Break the link your coins leave behind*

In this tutorial, we will study the concept of anonsets, indicators that allow us to estimate the quality of a coinjoin process on Whirlpool. We will cover the method of calculation and interpretation of these indicators. Following the theoretical part, we will move on to practice by learning to calculate the anonsets of a specific transaction using the Python tool *Whirlpool Stats Tools* (WST).

## What is a coinjoin on Bitcoin?
**Coinjoin is a technique that breaks the traceability of bitcoins on the blockchain**. It relies on a collaborative transaction with a specific structure of the same name: the coinjoin transaction.

Coinjoin transactions enhance the privacy of Bitcoin users by complicating chain analysis for external observers. Their structure allows merging multiple coins from different users into a single transaction, thus obscuring the trails and making it difficult to determine the links between input and output addresses.

The principle of coinjoin is based on a collaborative approach: several users who wish to mix their bitcoins deposit identical amounts as inputs of the same transaction. These amounts are then redistributed in outputs of equivalent value. At the end of the transaction, it becomes impossible to associate a specific output with a given user. No direct link exists between the inputs and outputs, thereby breaking the association between the users and their UTXO, as well as the history of each coin.

![coinjoin](assets/notext/1.webp)

Example of a coinjoin transaction:
[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

To carry out a coinjoin while ensuring that each user maintains control over their funds at all times, the process begins with the construction of the transaction by a coordinator, who then transmits it to each participant. Each user then signs the transaction after verifying that it suits them. All collected signatures are finally integrated into the transaction. If an attempt to divert funds is made by a user or the coordinator, by modifying the outputs of the coinjoin transaction, the signatures will prove invalid, leading to the rejection of the transaction by the nodes.

There are several implementations of coinjoin, such as Whirlpool, JoinMarket, or Wabisabi, each aiming to manage the coordination between participants and increase the efficiency of coinjoin transactions.
In this tutorial, we will focus on my favorite implementation: Whirlpool, which is available on Samourai Wallet and Sparrow Wallet. In my opinion, it's the most efficient implementation for coinjoins on Bitcoin.

## What is the utility of coinjoin on Bitcoin?

The utility of coinjoin lies in its ability to produce plausible deniability, by drowning your coin within a group of indistinguishable coins. The goal of this action is to break the traceability links, both from the past to the present and from the present to the past.

In other words, an analyst who knows your initial transaction at the entry of the coinjoin cycles should not be able to identify with certainty your UTXO at the exit of the remix cycles (analysis from cycle entry to cycle exit).

![coinjoin](assets/en/2.webp)

Conversely, an analyst who knows your UTXO at the exit of the coinjoin cycles should be unable to determine the original transaction at the entry of the cycles (analysis from cycle exit to cycle entry).

![coinjoin](assets/en/3.webp)

To assess the difficulty for an analyst to link the past to the present and vice versa, it's necessary to quantify the size of the groups within which your coin is concealed. This measure tells us the number of analyses having an identical probability. Thus, if the correct analysis is drowned among 3 other analyses of equal probability, your level of concealment is very low. On the other hand, if the correct analysis is within a set of 20,000 analyses all equally probable, your coin is very well hidden.

And precisely, the size of these groups represents indicators that are called "anonsets".

## Understanding anonsets
Anonsets serve as indicators to evaluate the degree of privacy of a particular UTXO. More specifically, they measure the number of indistinguishable UTXOs within the set that includes the studied coin. The requirement of a homogeneous UTXO set means that anonsets are usually calculated over coinjoin cycles. The use of these indicators is particularly relevant for Whirlpool coinjoins due to their uniformity.

Anonsets allow, where appropriate, to judge the quality of the coinjoins. A large anonset size means an increased level of anonymity, as it becomes difficult to distinguish a specific UTXO within the set.

There are two types of anonsets:
- **The prospective anonymity set;**
- **The retrospective anonymity set.**
The first indicator shows the size of the group among which the studied UTXO is hidden at the end of the cycle, knowing the UTXO at the entry, that is, the number of indistinguishable coins present within this group. This indicator allows measuring the resistance of the coin's confidentiality against an analysis from past to present (entry to exit). In English, the name of this indicator is "*forward anonset*", or "*forward-looking metrics*". 
![coinjoin](assets/en/4.webp)

This metric estimates the extent to which your UTXO is protected against attempts to reconstruct its history from its entry point to its exit point in the coinjoin process.

For example, if your transaction participated in its first coinjoin cycle and two other descendant cycles were completed, the prospective anonset of your coin would be `13`:

![coinjoin](assets/en/5.webp)

The second indicator shows the number of possible sources for a given coin, knowing the UTXO at the end of the cycle. This indicator measures the resistance of the coin's confidentiality against an analysis from present to past (exit to entry), that is, how difficult it is for an analyst to trace back to the origin of your coin, before the coinjoin cycles. In English, the name of this indicator is "*backward anonset*", or "*backward-looking metrics*".

![coinjoin](assets/en/6.webp)

Knowing your UTXO at the exit of the cycles, the retrospective anonset determines the number of potential Tx0 transactions that could have constituted your entry into the coinjoin cycles. In the diagram below, this corresponds to the sum of all the orange bubbles.

![coinjoin](assets/en/7.webp)

## Calculating anonsets with Whirlpool Stats Tools (WST)
To calculate these indicators on your own coins that have gone through coinjoin cycles, you can use a tool specially developed by Samourai Wallet: *Whirlpool Stats Tools*.

If you have a RoninDojo, WST is preinstalled on your node. You can therefore skip the installation steps and directly follow the usage steps. For those who do not have a RoninDojo node, let's see how to proceed with the installation of this tool on a computer.

You will need: Tor Browser (or Tor), Python 3.4.4 or higher, git, and pip. Open a terminal. To check the presence and version of these software on your system, enter the following commands:
```plaintext
python --version
git --version
pip --version
```

If needed, you can download them from their respective websites:
- https://www.python.org/downloads/ (pip comes directly with Python since version 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.
Once all these software are installed, from a terminal, clone the WST repository:
```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```

![WST](assets/notext/8.webp)

Navigate to the WST directory:
```plaintext
cd whirlpool_stats
```

Install the dependencies:
```plaintext
pip3 install -r ./requirements.txt
```

![WST](assets/notext/9.webp)

You may also install them manually (optional):
```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```

Navigate to the `/whirlpool_stats` subfolder:
```plaintext
cd whirlpool_stats
```

Start WST:
```plaintext
python3 wst.py
```

![WST](assets/notext/10.webp)

Launch Tor or Tor Browser in the background.

**-> For RoninDojo users, you can resume the tutorial directly here.**

Set the proxy to Tor (RoninDojo),
```plaintext
socks5 127.0.0.1:9050
```

or to Tor Browser depending on what you are using:
```plaintext
socks5 127.0.0.1:9150
```

This manipulation will allow you to download data on OXT via Tor, in order to not leak information about your transactions. If you are a novice and this step seems complex, know that it simply involves directing your internet traffic through Tor. The simplest method consists of launching the Tor Browser in the background on your computer, then executing only the second command to connect via this browser (`socks5 127.0.0.1:9150`).

![WST](assets/notext/11.webp)

Next, navigate to the working directory from which you intend to download the WST data using the `workdir` command. This folder will serve to store the transactional data that you will retrieve from OXT in the form of `.csv` files. This information is essential for calculating the indicators you are looking to obtain. You are free to choose the location of this directory. It might be wise to create a folder specifically for WST data. As an example, let's opt for the downloads folder. If you are using RoninDojo, this step is not necessary:
```plaintext
workdir path/to/your/directory
```

The command prompt should then have changed to indicate your working directory.

![WST](assets/notext/12.webp)

Then download the data from the pool containing your transaction. For example, if I am in the `100,000 sats` pool, the command is:
```plaintext
download 0001
```

![WST](assets/notext/13.webp)

The denomination codes on WST are as follows:
- Pool 0.5 bitcoins: `05`
- Pool 0.05 bitcoins: `005`
- Pool 0.01 bitcoins: `001`
- Pool 0.001 bitcoins: `0001`
Once the data is downloaded, load it. For example, if I am in the pool of `100,000 sats`, the command is:
```plaintext
load 0001
```

This step takes a few minutes depending on your computer. Now is a good time to make yourself a coffee! :)

![WST](assets/notext/14.webp)

After loading the data, type the `score` command followed by your TXID (transaction identifier) to get its anonsets:
```plaintext
score TXID
```

**Attention:** the choice of TXID to use varies depending on the anonset you wish to calculate. To assess the prospective anonset of a coin, it is necessary to enter, via the `score` command, the TXID corresponding to its first coinjoin, which is the initial mix performed with this UTXO. On the other hand, to determine the retrospective anonset, you must enter the TXID of the last coinjoin performed. To summarize, the prospective anonset is calculated from the TXID of the first mix, while the retrospective anonset is calculated from the TXID of the last mix.

WST then displays the retrospective score (*Backward-looking metrics*) and the prospective score (*Forward-looking metrics*). For example, I took the TXID of a random coin on Whirlpool that does not belong to me.

![WST](assets/notext/15.webp)

The transaction in question: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)

If we consider this transaction as the first coinjoin performed for the concerned coin, then it benefits from a prospective anonset of `86,871`. This means it is hidden among `86,871` indistinguishable coins. For an external observer who knows this coin at the beginning of the coinjoin cycles and attempts to trace its output, they will be faced with `86,871` possible UTXOs, each with an identical probability of being the sought-after coin.

If we consider this transaction as the last coinjoin of the coin, it then has a retrospective anonset of `42,185`. This means there are `42,185` potential sources for this UTXO. If an external observer identifies this coin at the end of the cycles and seeks to trace its origin, they will be faced with `42,185` possible sources, all with an equal probability of being the origin sought.
In addition to the anonset scores, WST also provides you with the diffusion rate of your output within the pool based on the anonset. This other indicator simply allows you to assess the potential for improvement of your piece. This rate is particularly useful for the prospective anonset. Indeed, if your piece has a diffusion rate of 15%, it means it can be confused with 15% of the pieces in the pool. That's good, but you still have a very large margin for improvement by continuing to remix. On the other hand, if your piece has a diffusion rate of 95%, then you are approaching the limits of the pool. You can continue to remix, but your anonset will not increase much.

It is important to note that the anonsets calculated by WST are not perfectly accurate. Given the huge volume of data to be processed, WST uses the *HyperLogLogPlusPlus* algorithm to significantly reduce the burden associated with local data processing and the necessary memory. This is an algorithm that allows estimating the number of distinct values in very large data sets while maintaining high accuracy in the result. Therefore, the scores provided are good enough to be used in your analyses, as they are very close estimates to reality, but they should not be interpreted as exact values to the unit.

In conclusion, keep in mind that it is not imperative to systematically calculate the anonsets for each of your pieces in coinjoins. The very design of Whirlpool already provides guarantees. Indeed, the retrospective anonset is rarely a concern. From your initial mix, you obtain a particularly high retrospective score thanks to the legacy of previous mixes since the Genesis coinjoin. As for the prospective anonset, it is enough to keep your piece in the post-mix account for a sufficiently long period.

This is why I consider the use of Whirlpool as particularly relevant in a *Hodl -> Mix -> Spend -> Replace* strategy. In my opinion, the most logical approach is to keep the bulk of one's bitcoin savings in a cold wallet, while continuously maintaining a certain number of pieces in coinjoins on Samourai to cover daily expenses. Once the bitcoins from the coinjoins are spent, they are replaced by new ones, in order to return to the defined threshold of mixed pieces. This method allows one to free themselves from the concern of our UTXO anonsets, while making the time necessary for the effectiveness of coinjoins much less constraining.

**External Resources:**

- [Podcast in French on chain analysis](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Wikipedia article on HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourai's repository for Whirlpool Stats
- Whirlpool website by Samourai
- [Medium article in English on privacy and Bitcoin by Samourai](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Medium article in English on the concept of anonymity set by Samourai](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7)
