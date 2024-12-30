---
name: Remix - Whirlpool
description: How many remixes should be done on Whirlpool?
---
![cover remix- wp](assets/cover.webp)

***WARNING:** Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24th, the Whirlpool Stats Tool is no longer available for download, as it was hosted on Samourai's Gitlab. Even if you had previously downloaded this tool locally to your machine, or it was installed on your RoninDojo node, WST will not function at this time. It relied on data provided by OXT.me for its operation, and this site is no longer accessible. Currently, WST is not particularly useful since the Whirlpool protocol is inactive. However, it remains possible that these softwares might be reinstated in the coming weeks. Moreover, the theoretical part of this article remains relevant for understanding the principles and goals of coinjoins in general (not just Whirlpool), as well as understanding the effectiveness of the Whirlpool model. You can also learn how to quantify the privacy provided by coinjoin cycles.*

_We are closely following the developments of this case as well as developments concerning the associated tools. Rest assured that we will update this tutorial as new information becomes available._

_This tutorial is provided for educational and informational purposes only. We do not endorse or encourage the use of these tools for criminal purposes. It is the responsibility of each user to comply with the laws in their jurisdiction._

---

> *"Break the link your coins leave behind"*

This is a question I am often asked. **When doing coinjoins with Whirlpool, how many remixes should be done to achieve satisfactory results?**

The purpose of coinjoin is to offer plausible deniability by mixing your coin with a group of indistinguishable coins. The goal of this action is to break the traceability links, both from the past to the present and from the present to the past. In other words, an analyst who knows your initial transaction at the entry of the coinjoin cycles should not be able to definitively identify your UTXO at the exit of the remix cycles (analysis from entry cycles to exit cycles).
![past-present links diagram](assets/en/1.webp)

Conversely, an analyst who knows your UTXO at the exit of the coinjoin cycles should be unable to determine the original transaction at the entry of the cycles (analysis from exit cycles to entry cycles).
![present-past links diagram](assets/en/2.webp)
However, the number of remixes is not a reliable criterion for evaluating the difficulty an analyst would encounter in establishing links between the past and the present, or vice versa. A more relevant indicator would be the size of the groups in which your coin is hiding. These indicators are referred to as "anonsets". In the case of Whirlpool, there are two types of anonsets.

Firstly, we can determine the size of the group where your UTXO is hidden at the exit of the coinjoin cycles, i.e., the number of indistinguishable coins present within this group.
![probable UTXOs at exit](assets/en/3.webp)
This indicator, called "prospective anonset" in French, "forward anonset" in English, or "forward-looking metrics", allows us to assess the resistance of your coin to analyses tracing its path from the entry to the exit of the coinjoin cycles. This metric estimates the extent to which your UTXO is protected against attempts to reconstruct its history from its entry point to its exit point in the coinjoin process. For example, if your transaction participated in its first coinjoin cycle and two additional downstream cycles were performed, the prospective anonset of your coin would be `13`:
![forward anonset](assets/en/4.webp)
Secondly, another indicator can be calculated to evaluate the resistance of your piece to an analysis from the present to the past. By knowing your UTXO at the end of cycles, this indicator determines the number of potential Tx0 transactions that could have constituted your input in the coinjoin cycles (analysis from the end to the beginning of the cycles). This indicator measures how difficult it is for an analyst to trace the origin of your piece after it has gone through coinjoins.![Probable sources at input](assets/en/5.webp)
The name of this indicator is "backward anonset" or "backward-looking metrics". In French, I like to call it "anonset rétrospectif". In the diagram below, this corresponds to all the orange Tx0 bubbles:
![backward anonset](assets/en/6.webp)
To learn more about the calculation method for these indicators, I recommend reading [my Twitter thread](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) on this topic. We are also preparing a more comprehensive article on the PlanB Network.

I am aware that the provided answer may seem unsatisfactory as you were hoping for a specific number of remixes, and I am directing you to documentation. The reason for this is that the number of remixes is an unreliable indicator for evaluating the anonymity gained in coinjoin cycles. Therefore, it is not possible to define a fixed number of remixes as an absolute and universal security threshold.

It is true that each additional remix of your piece increases its anonymity sets. However, it is important to understand that it is primarily the remixes performed by your peers that contribute to the growth of your prospective anonset. With the Whirlpool model, your transaction can achieve considerable levels of prospective anonset with just two or three coinjoin cycles, solely through the activity of peers involved in previous coinjoins.

The retrospective anonset, on the other hand, is not a concern in our case. In fact, from your initial coinjoin, you benefit from an inheritance of previous pool transactions, immediately giving your piece a high backward anonset, with a marginal increase in each subsequent cycle.
It is also important to understand that the creation of plausible deniability is never complete. It relies on the probability of tracing your coin. This probability decreases as the size of the groups concealing it increases. Therefore, you should adjust your objectives in terms of anonsets according to your personal expectations. Ask yourself about the reasons that lead you to use coinjoins and the levels of anonymity necessary to achieve these objectives. For example, if the use of coinjoins is simply aimed at preserving the privacy of your wallet when sending a few sats to your godchild for their birthday, very high levels of anonymity are not necessary. Your godchild is probably unable to perform in-depth chain analysis, and even if they were, the repercussions on your life would not be catastrophic. However, if you are the target of an authoritarian regime where the slightest piece of information can result in imprisonment, your actions will need to be guided by much stricter criteria.

To determine these famous anonset indicators, you can use a Python tool called **WST** (Whirlpool Stats Tool).

However, it is not always necessary to calculate the anonsets of each of your coinjoined coins. The design of Whirlpool itself already provides you with guarantees. As mentioned earlier, retrospective anonset is rarely a concern. From your initial mix, you already obtain a particularly high retrospective score. As for prospective anonset, you just need to keep your coin in the post-mix account for a sufficiently long period of time. For example, here are the anonset scores of one of my `100,000 sats` coins after spending two months in the coinjoin pool:
![WST anonsets](assets/en/7.webp)
It displays a retrospective score of `34,593` and a prospective score of `45,202`. In concrete terms, this means two things:
- If an analyst knows my coin at the end of the cycles and tries to trace its origin, they will encounter `34,593` potential sources, each with an equal probability of being mine.
- If an analyst knows my coin at the beginning of the cycles and tries to determine its correspondence at the end, they will be faced with `45,202` possible UTXOs, each with the same probability of being mine.
That is why I consider the use of Whirlpool to be particularly relevant in a `Hodl -> Mix -> Spend -> Replace` strategy. In my opinion, the most logical approach is to keep the majority of one's savings in bitcoins in a cold wallet, while constantly maintaining a certain number of coins in coinjoin on Samourai to cover daily expenses. Once the bitcoins from the coinjoins are spent, they are replaced with new ones to return to the defined threshold of mixed coins. This method allows us to free ourselves from the concern of the anonsets of our UTXOs, while making the time required for coinjoins to be effective much less restrictive.

I hope this answer has shed some light on the Whirlpool model. If you want to learn more about how coinjoins work on Bitcoin, I recommend reading my comprehensive article on this topic:

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**External resources:**
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://estudiobitcoin.com/como-instalar-y-utilizar-whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/
- https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7.
