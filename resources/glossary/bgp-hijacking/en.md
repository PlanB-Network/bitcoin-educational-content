---
term: BGP hijacking
definition: Attack manipulating Internet routing to redirect traffic to a malicious network, which can be used to isolate Bitcoin nodes.
---

Attack in which a malicious actor manipulates BGP advertisements to redirect Internet traffic to their own network. By pretending to be the legitimate origin of certain IP address ranges, the attacker can intercept, monitor or block traffic destined for these addresses.

BGP (*Border Gateway Protocol*) is the protocol that determines how traffic is routed between the various autonomous networks (AS) that make up the global Internet. It decides which paths data takes to get from one point to another.

In the context of Bitcoin, BGP Hijacking can be used to divert traffic between nodes on the Bitcoin network in order to isolate some of them. This attack can also target Stratum servers used by mining pools, redirecting miners' computing power to the attacker's own pool. Since miners rarely restart their machines, this redirection can persist for a long time. Such an attack may aim not only at direct financial gain by stealing block rewards but also at temporarily gaining more influence over the network.