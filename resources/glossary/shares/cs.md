---
term: AKCIE

---
V kontextu těžebních poolů je podíl ukazatel, který se používá ke kvantifikaci příspěvku jednotlivého těžaře v rámci poolu. Tento ukazatel slouží jako základ pro výpočet odměny, kterou pool přerozděluje jednotlivým těžařům. Každý podíl odpovídá hashi, který splňuje cíl obtížnosti nižší, než je obtížnost sítě Bitcoin.

Pro vysvětlení použijte analogii: vezměte si dvacetistěnnou kostku. Předpokládejme, že v případě Bitcoinu vyžaduje důkaz práce k potvrzení bloku hod číslem nižším než 3 (tj. dosažení výsledku 1 nebo 2). Nyní si představte, že v rámci těžebního poolu je cílová obtížnost pro podíl nastavena na 10. Pro jednotlivého těžaře v poolu se tedy každý hod kostkou, jehož výsledkem je číslo nižší než 10, počítá jako platný podíl. Tyto podíly pak těžař předá poolu, aby si mohl nárokovat odměnu, i když neodpovídají platnému výsledku pro blok Bitcoinu.

Pro každý vypočtený hash se jednotlivý těžař v poolu může setkat se třemi různými scénáři:


- Pokud je hodnota hash větší nebo rovna cílové hodnotě obtížnosti nastavené fondem pro sdílenou složku, pak je tato hodnota hash nepoužitelná. Těžař pak změní svou nonce a pokusí se o nový hash: `hash > share > block`.
- Pokud je hash nižší než cílová hodnota obtížnosti podílu, ale vyšší nebo roven cílové hodnotě obtížnosti Bitcoinu, pak tento hash představuje platný podíl, který však nestačí k ověření bloku. Těžař může tento hash odeslat do svého poolu a nárokovat si odměnu spojenou s podílem: `share > hash > block`.
- Pokud je hash nižší než cílová obtížnost sítě Bitcoin, je považován za platný podíl i platný blok. Těžař předá tento hash svému poolu, který jej spěchá odvysílat do sítě Bitcoin. Tento hash je pro těžaře rovněž považován za platný podíl: `podíl > blok > hash`.

![](../../dictionnaire/assets/32.webp)

Tento systém podílů se používá k odhadu práce, kterou odvedl každý jednotlivý těžař v rámci poolu, aniž by bylo nutné jednotlivě přepočítávat všechny hashe vygenerované těžařem, což by bylo pro pool zcela neefektivní.

Těžební pooly upravují obtížnost akcií, aby vyrovnaly ověřovací zátěž a zajistily, že každý těžař, ať už malý nebo velký, odevzdá akcie přibližně každých několik sekund. To umožňuje přesný výpočet hashrate každého těžaře a rozdělení odměn podle zvolené metody výpočtu odměn (PPS, PPLNS, TIDES...).

> ► *Ve francouzštině lze slovo "shares" přeložit jako "podíl".*