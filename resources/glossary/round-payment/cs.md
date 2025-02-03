---
term: KRUHOVÁ PLATBA

---
Interní heuristika pro analýzu řetězců v Bitcoinu, která umožňuje na základě zaokrouhlených částek vyslovit hypotézu o povaze výstupů transakce. Obecně platí, že pokud se setkáme s jednoduchým vzorem platby (1 vstup a 2 výstupy), pokud jeden z výstupů utratí kulatou částku, pak představuje platbu. Na základě eliminace platí, že pokud jeden výstup představuje platbu, druhý představuje změnu. Lze tedy interpretovat, že je pravděpodobné, že uživatel zadávající transakci stále disponuje výstupem identifikovaným jako změna.

Je třeba poznamenat, že tato heuristika není vždy použitelná, protože většina plateb se stále provádí v jednotkách fiat měny. Pokud totiž obchodník ve Francii přijímá bitcoiny, zpravidla nezobrazuje stabilní ceny v sats. Raději se rozhodnou pro přepočet mezi cenou v eurech a částkou v bitcoinech, která má být zaplacena prostřednictvím jejich pokladny (jako například server BTCPay). Proto by se ve výstupu transakce nemělo objevit zaokrouhlené číslo. Nicméně analytik by se mohl pokusit tento přepočet provést s přihlédnutím ke směnnému kurzu platnému v okamžiku vysílání transakce do sítě. Pokud se jednoho dne bitcoin stane preferovanou zúčtovací jednotkou na našich burzách, mohla by se tato heuristika stát pro analýzy ještě užitečnější.

![](../../dictionnaire/assets/11.webp)