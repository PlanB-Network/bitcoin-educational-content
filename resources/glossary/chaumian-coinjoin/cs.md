---
term: CHAUMIAN COINJOIN
---

Protokol coinjoin, který využívá Davidovy Chaumovy slepé podpisy a Tor pro komunikaci mezi účastníky a serverem koordinátora. Cílem Chaumian coinjoin je zajistit účastníkům, že koordinátor nemůže ukrást bitcoiny, ani propojit vstupy a výstupy.

K dosažení tohoto cíle uživatelé odesílají svůj vstup a kryptograficky zaslepenou adresu pro příjem koordinátorovi. Tato adresa, jakmile je odhalena, je určena k přijetí bitcoinů jako výstup z coinjoin. Koordinátor tyto tokeny podepíše a vrátí je uživatelům. Uživatelé se pak anonymně znovu připojí k serveru koordinátora s novou identitou Tor a odhalí své výstupní adresy v prostém textu pro konstrukci transakce. Koordinátor může ověřit, že všechny tyto přijímací adresy pocházejí od legitimních uživatelů, protože již dříve podepsal jejich zaslepenou verzi svým soukromým klíčem. Nicméně nemůže spojit konkrétní výstupní adresu s daným vstupním uživatelem. Proto neexistuje žádné propojení mezi vstupy a výstupy, ani z pohledu koordinátora. Jakmile koordinátor sestaví transakci, pošle ji zpět účastníkům, kteří ji podepíší, aby odemkli svůj vstup, po ověření, že jejich výstup je skutečně v této transakci. Účastníci pošlou podpis koordinátorovi. Jakmile jsou všechny podpisy shromážděny, může koordinátor vysílat transakci coinjoin na síť Bitcoin.

![](../../dictionnaire/assets/38.png)

Tato metoda zajišťuje, že koordinátor nemůže během celého procesu coinjoin ohrozit anonymitu účastníků ani ukrást bitcoiny.

Je obtížné určit s jistotou, kdo jako první představil myšlenku coinjoin na Bitcoinu a kdo měl nápad použít Davidovy Chaumovy slepé podpisy v tomto kontextu. Často se má za to, že o tom jako první diskutoval Gregory Maxwell v [zprávě na BitcoinTalk v roce 2013](https://bitcointalk.org/index.php?topic=279249.0):

> *"Použitím Chaumových slepých podpisů: Uživatelé se připojí a poskytnou vstupy (a adresy pro změnu) stejně jako kryptograficky zaslepenou verzi adresy, na kterou chtějí poslat své soukromé coiny; server podepíše tokeny a vrátí je. Uživatelé se anonymně znovu připojí, odhalí své výstupní adresy a vrátí je serveru. Server může vidět, že všechny výstupy byly jím podepsány a že tedy všechny výstupy pocházejí od platných účastníků. Později se lidé znovu připojí a podepíší."*

Maxwell, G. (2013, srpen 22). *CoinJoin: Soukromí Bitcoinu pro skutečný svět*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0
Nicméně existují i jiné, dřívější zmínky, jak o Chaumových podpisech v kontextu míchání, tak i o coinjoinech. [V červnu 2011 Duncan Townsend představil na BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) mixer, který využívá Chaumovy podpisy způsobem velmi podobným moderním Chaumian coinjoinům. Ve stejném vlákně je [zpráva od uživatele hashcoin jako reakce na Duncana Townsenda](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) s návrhem na vylepšení jeho mixéru. Tato zpráva přesně prezentuje to, co se nejvíce podobá coinjoinům. Zmínka o podobném systému je také v [zprávě od Alexe Mizrahiho z roku 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), kdy radil tvůrcům Tenebrixu. Termín "coinjoin" sám by nebyl vynalezen Gregem Maxwellem, ale pocházel by z nápadu Petera Todda.