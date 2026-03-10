---
name: Lightning Network+
description: Get free incoming liquidity with cooperative openings on your Lightning node
---

![cover](assets/cover.webp)


## Introduction


[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) is a community platform designed to facilitate cooperation between Lightning Network node operators. Its main objective is to improve the connectivity, liquidity and decentralization of the Lightning network, without the need for centralized intermediaries.


This tutorial will focus on the **"Swaps "** service, which is the most widely used and structuring feature of LN+ today. The other services offered by the platform will also be presented.


## LN+ overview


### What is Lightning Network Plus?


Lightning Network Plus (LN+) is a community platform for Lightning node operators wishing to cooperate directly and voluntarily. It aims to facilitate the creation of useful, balanced and sustainable Lightning channels, while avoiding the need for centralized solutions or imposed hubs.


LN+ is based on a fundamental principle: peer-to-peer cooperation, founded on transparency, reciprocity and reputation.


### LN+ services at a glance


LN+ offers several services designed to improve the topology and liquidity of the Lightning network, including :



- Swaps**: reciprocal opening of channels between operators (main service).
- Rings**: circular channel openings between several participants.
- Trust-based swaps**: variants that rely more on the trust and history of participants.
- Social features**: profiles, comments and reputation system.


In the remainder of this tutorial, we'll concentrate exclusively on the **Swaps** service, which is at the heart of current LN+ usage.


## LN+ "Swaps" service


### Definition of a LN+ swap


A LN+ **swap** is a voluntary agreement between two Lightning node operators to mutually open Lightning channels of equivalent (or pre-agreed) capacity. Unlike a conventional unilateral channel opening, the swap is based on **explicit reciprocity**.


In practice :



- You open a channel to your partner's node.
- Your partner opens a channel to your node.
- Both parties are tying up a similar quantity of on-chain bitcoins.


### What is the purpose of swaps for node operators?


The Swaps service addresses several key issues encountered by Lightning operators:



- Improved connectivity**: creation of useful bidirectional channels as soon as they are opened.
- Better liquidity management**: each party has both incoming and outgoing capacity.
- Reduced risk of unnecessary channels**: the partner is encouraged to keep the channel open.
- Greater decentralization**: direct connections between operators, without imposed hubs.


### For which node profiles are swaps useful?


Swaps are particularly useful for :



- New nodes wishing to rapidly improve their routability.
- Intermediary operators looking to increase the density of their channel graph.
- Routing-oriented nodes that want to optimize their topology.


## Connect your Lightning node to LN+


### Technical requirements


Before you begin, you will need :



- A working Lightning node (LND, Core Lightning or Eclair).
- Access to your node's management interface.
- Sufficient on-chain capacity to open channels.


Go to the [Lightning Network](https://lightningnetwork.plus/) Plus website and click on the `Login` button at the top right of the interface.


![capture](assets/fr/03.webp)


### Authentication by message signature


To authenticate yourself, you need to sign the message provided using your Lightning node's private key. With ThunderHub, this operation is very simple.


Start by copying the message displayed by LN+.


![capture](assets/fr/04.webp)


In ThunderHub, go to the `Tools` tab, then click on the `Sign` button in the `Messages` section.


![capture](assets/fr/05.webp)


Paste the authentication message provided by LN+, then click `Sign`.


![capture](assets/fr/06.webp)


ThunderHub then signs this message using your node's private key. Copy the generated signature.


![capture](assets/fr/07.webp)


Paste this signature into the corresponding field on the LN+ site, then click `Sign in`.


![capture](assets/fr/08.webp)


You are now connected to LN+ with your Lightning node. This process allows LN+ to verify that you are the rightful owner of the node you claim on their platform.


![capture](assets/fr/09.webp)


If you wish, you can personalize your LN+ profile, for example by adding a short biography.


## Participate in an existing swap


### Access to swap offers


To participate in your first channel opening, go to the `Swaps` menu at the top of the interface. Here you'll find all the swaps currently available, depending on your node's characteristics.


![capture](assets/fr/10.webp)


### Conditions of eligibility


To join an existing swap offer, simply select the corresponding ad and register. However, LN+ allows the swap creator to define certain **eligibility conditions**, such as :



- a minimum number of channels already open ;
- minimum total node capacity ;
- certain types of connection accepted.


### Recent nodes


As a result, especially in the early stages of use, it's possible that **few or no offers are available** to your node. This is a common situation for new nodes or those not yet connected.


In my case, despite the existence of a few open channels, none of the offers met the required criteria.


## Create your own swap offer


### When should you create your own swap?


When no existing offer is available, creating your own swap is often the best solution. It also allows you to retain control over the swap's parameters.


### Swap configuration


Click on **Start Liquidity Swap**, then configure your offer parameters:



- select the total number of participants (3, 4 or 5);
- indicate the capacity of the channels to be opened;
- define the commitment period during which participants agree not to close their channels;
- specify any restrictions applicable to participants (minimum number of channels, minimum total capacity, type of connection accepted).


![capture](assets/fr/11.webp)


### Publication and participants' expectations


Once all the parameters have been entered, click on **Start Liquidity Swap** to publish your offer. Now all you have to do is wait for other operators to sign up.


![capture](assets/fr/12.webp)


## Finalizing a swap


### Effective channel opening


Now that all the swap positions have been taken, each participant can see, from his LN+ interface, which node he needs to open a Lightning channel to.


![capture](assets/fr/13.webp)


On your side, open the channel using the Node ID provided by LN+ and respecting the amount indicated. This operation can be carried out via ThunderHub, another Lightning node manager or directly via your node's basic interface.


![capture](assets/fr/14.webp)


Once opened, the channel appears in the waiting channels section.


![capture](assets/fr/15.webp)


### Confirmation in LN+


Then return to LN+ to confirm that you have initiated channel opening, by clicking on the `Channel Opening Started` button.


![capture](assets/fr/16.webp)


### End of swap


When all participants have opened the channels to which they have committed, the swap is considered complete.


## Reputation and good communication practices


### The LN+ reputation system


LN+ incorporates a reputation system based on the opinions left by participants at the end of swaps. These opinions are public and directly influence an operator's ability to join or create future swaps.


![capture](assets/fr/17.webp)


### Recommended best practices


In order to preserve a good reputation and ensure the smooth running of swaps, it is recommended to :



- respect channel opening deadlines ;
- communicate quickly in the event of a problem or delay;
- use the comments section to exchange views with other participants;
- not to close a channel before the end of the commitment period.



![capture](assets/fr/18.webp)


### Why reputation is central to LN+


LN+ is based on a model of voluntary cooperation, with no strong technical constraints. Reputation is therefore the main incentive for ensuring the reliability and trustworthiness of participants.


## Other LN+ services


In addition to Swaps, LN+ offers other services designed to improve connectivity and coordination between Lightning node operators. Rings** enable several participants to create a loop of channel openings, thus reinforcing the redundancy of routing paths and the density of the Lightning graph. Trust-based swaps** are based on similar principles to classic swaps, but offer greater flexibility to participants who already have an established reputation on the platform.


LN+ also integrates social features such as public node profiles, swap comments and a reputation system. These tools are not technical services per se, but play a central role in the smooth running of the platform, facilitating communication, coordination and trust between operators.


## Conclusion


LN+'s Swaps service is an effective tool for improving connectivity, liquidity and decentralization in the Lightning network. By promoting reciprocal, coordinated channel openings, LN+ enables node operators to strengthen their topology, while at the same time promoting responsible, decentralized cooperation.