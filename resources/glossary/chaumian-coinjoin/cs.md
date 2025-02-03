---
term: CHAUMIAN COINJOIN

---
Protokol coinjoin, který využívá slepé podpisy Davida Chauma a Tor pro komunikaci mezi účastníky a serverem koordinátora. Cílem Chaumova coinjoinu je zajistit účastníkům, že koordinátor nemůže ukrást bitcoiny, ani propojit vstupy a výstupy.

Za tímto účelem uživatelé předávají koordinátorovi své vstupní údaje a kryptograficky zaslepenou adresu příjmu. Tato adresa je po odblokování určena k příjmu bitcoinů jako výstupu z coinjoinu. Koordinátor tyto tokeny podepíše a vrátí je uživatelům. Uživatelé se pak znovu anonymně připojí k serveru koordinátora s novou identitou Tor a odhalí své výstupní adresy v otevřeném textu pro konstrukci transakce. Koordinátor může ověřit, že všechny tyto přijímací adresy pocházejí od legitimních uživatelů, protože jejich zaslepenou verzi předtím podepsal svým soukromým klíčem. Nemůže však přiřadit konkrétní výstupní adresu k danému vstupnímu uživateli. Mezi vstupy a výstupy tedy neexistuje žádná vazba, a to ani z pohledu koordinátora. Jakmile koordinátor transakci zkonstruuje, pošle ji zpět účastníkům, kteří ji podepíší, aby odemkli své vstupy, poté co ověří, že jejich výstup je skutečně v této transakci. Účastníci pošlou podpis koordinátorovi. Jakmile jsou shromážděny všechny podpisy, koordinátor může transakci coinjoin vysílat v síti Bitcoin.

![](../../dictionnaire/assets/38.webp)

Tato metoda zajišťuje, že koordinátor nemůže ohrozit anonymitu účastníků ani ukrást bitcoiny během celého procesu spojování mincí.

Je obtížné s jistotou určit, kdo jako první představil myšlenku coinjoin u Bitcoinu a kdo měl nápad použít v této souvislosti slepé podpisy Davida Chauma. Často se má za to, že jako první o ní hovořil Gregory Maxwell v [zprávě na BitcoinTalku v roce 2013](https://bitcointalk.org/index.php?topic=279249.0):

> *"Pomocí Chaumových slepých podpisů: Uživatelé se připojují a poskytují vstupy (a mění adresy), jakož i kryptograficky zaslepenou verzi adresy, na kterou chtějí poslat své soukromé mince; server tokeny podepíše a vrátí je. Uživatelé se znovu anonymně připojí, odmaskují své výstupní adresy a vrátí je serveru. Server vidí, že všechny výstupy byly jím podepsány, a že tedy všechny výstupy pocházejí od platných účastníků. Později se lidé znovu připojí a podepíší. "*
Maxwell, G. (2013, 22. srpna). *CoinJoin: Bitcoin privacy for the real world* (Soukromí bitcoinů pro reálný svět). Fórum BitcoinTalk. https://bitcointalk.org/index.php?topic=279249.0

Existují však i další dřívější zmínky, a to jak o Chaumových signaturách v kontextu míchání, tak o koincidencích. [V červnu 2011 představil Duncan Townsend na BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) mixér, který používá Chaumovy signatury způsobem dosti podobným moderním Chaumovým coinjoinům. Ve stejném vlákně je [zpráva od hashcoinu v reakci na Duncana Townsenda](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) k vylepšení jeho mixéru. Tato zpráva přesně představuje to, co se nejvíce podobá coinjoins. Zmínka o podobném systému je také ve [zprávě od Alexe Mizrahiho z roku 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), když radil tvůrcům Tenebrixu. Samotný termín "coinjoin" by nevymyslel Greg Maxwell, ale pocházel by z nápadu Petera Todda.