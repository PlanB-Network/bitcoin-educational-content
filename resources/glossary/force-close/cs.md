---
term: NÁSILÍ ZAVŘÍT
---

Nespolupracující mechanismus uzavírání bleskového kanálu. Když dva uživatelé otevřou kanál s Multisig 2/2, každý z nich může jednostranně uzavřít kanál odvysíláním posledního již podepsaného Commitment Transaction, aby získal zpět své bitcoiny v řetězci. Tento postup je znám jako "vynucené uzavření".


Tato metoda se obvykle používá v případě, že jeden z účastníků již neodpovídá nebo pokud není možné kanál uzavřít ve spolupráci. Pokud je možné se násilnému uzavření vyhnout, je to nejlepší, protože vymáhání prostředků v řetězci trvá déle a může být mnohem dražší z hlediska poplatků.


Při silovém uzavření vysílá jeden ze dvou uživatelů signál Commitment Transaction, který odráží poslední známý stav kanálu Lightning. Poté dojde k časovému zámku, než je možné bitcoiny v řetězci získat, což dává druhé straně čas na ověření, že transakce odpovídá poslednímu stavu kanálu. Pokud se uživatel pokusí podvádět tím, že zveřejní neaktuální Commitment Transaction, může druhá strana použít tajemství odvolání, aby podvodníka potrestala a získala zpět všechny prostředky v kanálu.