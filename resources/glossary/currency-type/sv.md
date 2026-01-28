---
term: Valutatyp
definition: Härledningsnivå för HD-plånböcker som gör det möjligt att separera grenar efter de kryptovalutor som används.
---

I samband med deterministiska och hierarkiska (HD) plånböcker är valutatypen (*coin type* på engelska) en härledningsnivå som gör det möjligt att differentiera grenarna i Wallet baserat på de olika kryptovalutor som används. Denna Layer av härledning, definierad av BIP 44, ligger på djup 2 i härledningsstrukturen, efter huvudnyckeln och syftet. Till exempel, för Bitcoin är det tilldelade indexet `0x80000000`, noterat som `/0'/` i härledningsvägen. Detta innebär att alla adresser och konton som härleds från denna sökväg är associerade med Bitcoin. Denna Layer-avledning möjliggör en tydlig separation av olika tillgångar i en Wallet med flera valutor. Här är de index som används för olika kryptovalutor:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...


