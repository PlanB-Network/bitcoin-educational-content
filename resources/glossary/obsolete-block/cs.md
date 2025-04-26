---
term: ZASTARALÝ (BLOK)

---
Označuje blok bez potomků: platný blok, který je však vyloučen z hlavního řetězce Bitcoinu. Vzniká, když dva těžaři v krátkém časovém úseku najdou platný blok ve stejné výšce řetězce a odvysílají jej po síti. Uzly nakonec vyberou pouze jeden blok, který zařadí do řetězce podle principu řetězce s největším množstvím nashromážděné práce, čímž ostatní bloky "zastarají". Proces vedoucí k vytvoření zastaralého bloku je následující:


- Dva těžaři najdou platný blok ve stejné výšce řetězce v krátkém časovém intervalu. Nazvěme je `Blok A` a `Blok B`;
- Každý z nich vysílá svůj blok do sítě uzlů Bitcoinu. Každý uzel má nyní 2 bloky ve stejné výšce. Existují tedy dva platné řetězce;
- Těžaři pokračují v hledání důkazů práce pro následující bloky, ale musí si nutně vybrat pouze jeden blok mezi `Blokem A` a `Blokem B`, na kterém budou těžit;
- Těžař nakonec najde platný blok nad blokem B. Nazvěme jej `Blok B+1`;
- Vysílají `Blok B+1` do uzlů sítě;
- Protože uzly sledují nejdelší řetězec (s největším množstvím nahromaděné práce), odhadnou, že je třeba sledovat řetězec B;
- Opustí `blok A`, který již není součástí hlavního řetězce. Stal se tak zastaralým blokem.

![](../../dictionnaire/assets/9.webp)

> ► V angličtině se označuje jako "Stale Block". Ve francouzštině se může také nazývat "bloc périmé" nebo "bloc abandonné". Ačkoli s tímto použitím nesouhlasím, někteří bitcoináři používají termín "bloc orphelin" pro označení toho, co je ve skutečnosti zastaralý blok.*