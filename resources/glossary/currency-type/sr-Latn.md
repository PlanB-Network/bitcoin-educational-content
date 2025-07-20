---
term: TIP VALUTE
---

U kontekstu determinističkih i hijerarhijskih (HD) novčanika, tip valute (*coin type* na engleskom) je nivo derivacije koji omogućava razlikovanje grana Wallet na osnovu različitih korišćenih kriptovaluta. Ovaj Layer derivacije, definisan BIP 44, nalazi se na dubini 2 strukture derivacije, nakon master ključa i svrhe. Na primer, za Bitcoin, dodeljeni indeks je `0x80000000`, zabeležen kao `/0'/` u putanji derivacije. To znači da su sve adrese i nalozi izvedeni iz ove putanje povezani sa Bitcoin. Ovaj Layer derivacije omogućava jasno razdvajanje različitih sredstava u multi-valutnom Wallet. Evo indeksa korišćenih za razne kriptovalute:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...


![](../../dictionnaire/assets/21.webp)