---
term: Shards (lightning)
definition: Del av en betalning som skickas separat via olika Lightning-rutter (MPP/AMP).
---

I samband med *Multi-Path Payments (MPP)* eller *Atomic Multi-Path Payments (AMP)* är en Shard en bråkdel av en global betalning. Varje Shard representerar en del av den totala betalningen, som dirigeras separat via en annan rutt på Lightning.


I MPP delar alla shards samma hemlighet, medan i AMP har varje Shard en unik partiell hemlighet. Mottagaren grupperar skärvorna tillsammans för att återskapa och slutföra hela betalningen. Denna mekanism kringgår likviditetsbegränsningar på en enda kanal.