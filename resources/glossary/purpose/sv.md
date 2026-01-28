---
term: Syfte
definition: Härledningsnivå i HD-plånböcker som identifierar den adressstandard som används.
---

I deterministiska och hierarkiska (HD) portföljer representerar syftet, som definieras av BIP43, en specifik härledningsnivå. Detta index, som finns på första djupet i härledningsträdet (`m / purpose' /`), identifierar den härledningsstandard som antagits av portföljen, för att underlätta kompatibilitet mellan olika programvaror för portföljhantering. I fallet med SegWit-adresser (BIP84) anges t.ex. syftet som `/84'/`. Denna metod gör det möjligt att effektivt organisera nycklar mellan olika Address-typer inom en och samma HD-portfölj. De standardindex som används är :




- För P2PKH: `44'` ;
- För P2WPKH inbäddad i P2SH: `49'` ;
- För P2WPKH: `84'` ;
- För P2TR: `86'`.