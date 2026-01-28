---
term: Gossip
definition: P2P-protokoll för att sprida information mellan noder på ett epidemiskt sätt.
---

Gossip är en distribuerad algoritm för peer-to-peer (P2P) som sprider information epidemiskt till alla nätverksagenter. För Bitcoin, Lightning och andra distribuerade system gör det här protokollet att nodernas Global State kan utbytas och synkroniseras på bara några få cykler. Varje nod sprider information till en eller flera slumpmässiga eller icke-slumpmässiga grannar, som i sin tur sprider informationen till andra grannar, och så vidare, tills ett globalt synkroniserat tillstånd har uppnåtts.


Inom Lightning är gossip ett kommunikationsprotokoll mellan noder för att dela information om nätverkets aktuella tillstånd och topologi. Skvallerprotokollet gör det möjligt för noder att känna till det dynamiska tillståndet för betalningskanaler och andra noder, för att underlätta routningen av transaktioner över nätverket utan att kräva direkta anslutningar mellan alla noder.


