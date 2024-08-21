---
term: ZASTARALÝ (BLOK)
---

Odkazuje na blok bez potomků: platný blok, ale vyloučený z hlavního řetězce Bitcoinu. K tomu dochází, když dva těžaři najdou platný blok na stejné výšce řetězce během krátkého časového období a šíří jej po síti. Uzly nakonec vyberou pouze jeden blok, který bude začleněn do řetězce, podle principu řetězce s největším nahromaděným pracovním výkonem, čímž se druhý stává "zastaralým". Proces vedoucí k vytvoření zastaralého bloku je následující:
* Dva těžaři najdou platný blok na stejné výšce řetězce během krátkého časového intervalu. Nazvěme je `Blok A` a `Blok B`;
* Každý z nich šíří svůj blok do sítě Bitcoinových uzlů. Každý uzel nyní má 2 bloky na stejné výšce. Existují tedy dvě platné řetězce;
* Těžaři pokračují ve vyhledávání důkazů práce pro následující bloky, ale musí se nutně rozhodnout pouze pro jeden blok mezi `Blokem A` a `Blokem B`, na kterém budou těžit;
* Těžař nakonec najde platný blok nad `Blokem B`. Nazvěme ho `Blok B+1`;
* Šíří `Blok B+1` do uzlů sítě;
* Jelikož uzly následují nejdelší řetězec (s největším nahromaděným pracovním výkonem), odhadnou, že `Řetězec B` je ten, který je třeba následovat;
* Opustí `Blok A`, který již není součástí hlavního řetězce. Stal se tak zastaralým blokem.

![](../../dictionnaire/assets/9.png)

> ► *V angličtině se tomu říká "Stale Block". Ve francouzštině se mu může také říkat "bloc périmé" nebo "bloc abandonné". Ačkoliv s tímto použitím nesouhlasím, někteří bitcoinisté používají termín "bloc orphelin" pro to, co je ve skutečnosti zastaralý blok.*