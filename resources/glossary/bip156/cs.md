---
term: BIP156

---
Návrh známý jako Dandelion, jehož cílem je zlepšit soukromí při směrování transakcí v síti Bitcoin a čelit tak deanonymizaci. Při standardním fungování Bitcoinu jsou transakce okamžitě vysílány do více uzlů. Pokud je pozorovatel schopen vidět každou transakci přenášenou každým uzlem v síti, může předpokládat, že první uzel, který transakci odeslal, je také uzlem, z něhož transakce pochází, a že tedy pochází od provozovatele tohoto uzlu. Tento jev by potenciálně mohl pozorovatelům umožnit spojit transakce, které jsou obvykle anonymní, s IP adresami.

Cílem BIP156 je tento problém řešit. Za tímto účelem zavádí dodatečnou fázi vysílání, aby byla zachována anonymita před veřejným šířením. Pampeliška tedy nejprve používá fázi "kmene", kdy je transakce odeslána náhodnou cestou uzlů, a teprve poté je vysílána do celé sítě ve fázi "fluff". Stonek a chmýří jsou odkazy na chování transakce při jejím šíření sítí a připomínají tvar pampelišky (anglicky *a dandelion*).

Tato metoda směrování zamlžuje stopu vedoucí zpět ke zdrojovému uzlu, takže je obtížné vysledovat transakci v síti až k jejímu původu. Dandelion tak zlepšuje soukromí tím, že omezuje schopnost protivníků deanonymizovat síť. Tato metoda je ještě účinnější, pokud transakce prochází během fáze "kmene" uzlem, který svou síťovou komunikaci šifruje, jako například Tor nebo *P2P Transport V2*. BIP156 zatím nebyl do jádra Bitcoinu přidán.

![](../../dictionnaire/assets/36.webp)