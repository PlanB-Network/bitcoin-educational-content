---
term: SHARES
---

V kontextu těžebních poolů je share ukazatelem používaným k kvantifikaci příspěvku jednotlivého těžaře v rámci poolu. Toto měření slouží jako základ pro výpočet odměny, kterou pool redistribuuje každému těžaři. Každý share odpovídá hashi, který splňuje cílovou obtížnost nižší než je obtížnost sítě Bitcoin.

Pro vysvětlení pomocí analogie si představte dvacetistrannou kostku. Na Bitcoinu předpokládejme, že důkaz práce vyžaduje hodit číslo menší než 3 pro validaci bloku (to znamená dosáhnout výsledku 1 nebo 2). Nyní si představte, že v rámci těžebního poolu je cílová obtížnost pro share nastavena na 10. Tedy pro jednotlivého těžaře v poolu, každý hod kostkou, který vede k číslu menšímu než 10, se počítá jako platný share. Tyto shares jsou pak těžařem přenášeny do poolu, aby si nárokoval svou odměnu, i když neodpovídají platnému výsledku pro blok na Bitcoinu.

Pro každý vypočítaný hash se jednotlivý těžař v poolu může setkat se třemi různými scénáři:
* Pokud je hodnota hash větší nebo rovna nastavené cílové obtížnosti poolu pro share, pak tento hash není k ničemu užitečný. Těžař pak změní svůj nonce, aby se pokusil o nový hash: `hash > share > block`.
* Pokud je hash nižší než cílová obtížnost share, ale větší nebo rovna cílové obtížnosti Bitcoinu, pak tento hash představuje platný share, který však není dostatečný pro validaci bloku. Těžař může tento hash poslat svému poolu, aby si nárokoval odměnu spojenou se sharem: `share > hash > block`.
* Pokud je hash nižší než cílová obtížnost sítě Bitcoin, je považován jak za platný share, tak za platný blok. Těžař přenáší tento hash do svého poolu, který se snaží jej rychle vysílat do sítě Bitcoin. Tento hash je také počítán jako platný share pro těžaře: `share > block > hash`.

![](../../dictionnaire/assets/32.png)

Tento systém share je používán k odhadu práce vykonané každým jednotlivým těžařem v rámci poolu, aniž by bylo nutné jednotlivě přepočítávat všechny hashi generované těžařem, což by pro pool bylo zcela neefektivní.

Těžební pooly upravují obtížnost shares, aby vyvážily zátěž ověřování a zajistily, že každý těžař, ať už malý nebo velký, odesílá shares přibližně každých několik sekund. To umožňuje přesný výpočet hashrate každého těžaře a distribuci odměn podle zvolené metody výpočtu kompenzace (PPS, PPLNS, TIDES...).

> ► *Ve francouzštině lze "shares" přeložit jako "part".*