---
term: ROUND PAYMENT
---

Interní heuristika pro analýzu řetězce u Bitcoinu, která umožňuje formulovat hypotézu o povaze výstupů transakce na základě kulatých částek. Obecně, když se setkáme s jednoduchým vzorem platby (1 vstup a 2 výstupy), pokud jeden z výstupů používá kulatou částku, pak tento reprezentuje platbu. Eliminací, pokud jeden výstup reprezentuje platbu, druhý reprezentuje vrácení peněz. Lze tedy interpretovat, že je pravděpodobné, že uživatel provádějící transakci stále vlastní výstup identifikovaný jako vrácení peněz.

Je třeba poznamenat, že tato heuristika není vždy použitelná, protože většina plateb je stále prováděna v jednotkách fiat měn. Skutečně, když obchodník ve Francii přijímá bitcoiny, obvykle neuvádějí stabilní ceny v sats. Raději by volili konverzi mezi cenou v eurech a množstvím bitcoinů k zaplacení prostřednictvím jejich POS (jako například BTCPay Server). Proto by výstup transakce neměl obsahovat kulaté číslo. Nicméně, analytik by se mohl pokusit tuto konverzi provést s přihlédnutím k směnnému kurzu platnému v době vysílání transakce v síti. Pokud by se jednoho dne bitcoin stal preferovanou jednotkou účtu v našich výměnách, tato heuristika by mohla být ještě užitečnější pro analýzy.

![](../../dictionnaire/assets/11.png)