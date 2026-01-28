---
term: Multi-path payments (MPP)
definition: Lightning-teknik som delar upp en betalning i flera delar som skickas via olika vägar.
---

Ett samlingsbegrepp för alla betalningstekniker på Lightning som gör det möjligt att bryta ner en transaktion i flera mindre delar och skicka dem via olika vägar. Med andra ord tar varje betalningsfraktion en annan nodväg. Detta gör det möjligt att kringgå likviditetsbegränsningar på en enda kanal i rutten.


Betalningar med flera vägar ger också små fördelar när det gäller sekretess, eftersom det blir svårare för en observatör att koppla varje betalningsfragment till hela transaktionen. I grundversionen delar dock alla fragment samma hemlighet för HTLC:er, vilket kan göra transaktionen spårbar om en observatör befinner sig på flera vägar. Eftersom hemligheten är unik för alla delar av betalningen är den dessutom inte atomär. Detta innebär att vissa delar av betalningen kan utföras framgångsrikt, medan andra kan misslyckas. Dessa nackdelar korrigeras med "Atomic Multi-Path Payment".