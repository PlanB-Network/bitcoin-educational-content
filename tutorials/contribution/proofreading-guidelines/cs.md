---
name: Pokyny pro korektury
description: Jaké důležité faktory je třeba mít na paměti při korektuře na Akademii Plan ₿?
---

![github](assets/cover.webp)


Vítejte v tomto návodu o **pokynech, kterými je třeba se řídit při korekturách obsahu v Akademii Plan ₿**. Jsme rádi, že sdílíte naše poslání překládat materiály Bitcoin do co největšího počtu jazyků, abychom lidem pomohli získat povědomí o tom, jak funguje a jak ji lze využít v každodenním životě.


Přispívání do Plan ₿ Academy [veřejné úložiště](https://github.com/PlanB-Network/bitcoin-educational-content) vám především dává možnost psát výukové programy, opravovat stávající obsah nebo dokonce navrhnout přidání nového jazyka do platformy. Chcete-li se dozvědět více, připojte se nejprve k naší [Telegramové skupině](https://t.me/PlanBNetwork_ContentBuilder) a napište krátkou prezentaci o sobě a jazycích, které ovládáte.


Tento návod je určen přispěvatelům, kteří chtějí provádět korektury obsahu. Většina z nich toho o [Githubu](https://planb.academy/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ani o [jazyku Markdown](https://www.markdownguide.org/basic-syntax/), který v úložišti používáme, moc neví, a proto je důležité podělit se s nimi o několik informací o klíčových faktorech, které jsou s tímto úkolem spojeny.


Níže jsem shromáždil nejčastější problémy, se kterými se korektoři setkávají. Neváhejte navrhnout další, protože to může pomoci ostatním zlepšit se.


Než se ponoříte do podrobností, přečtěte si nejprve tento návod o praktických postupech na Githubu: forkování repozitáře Plan ₿ Academy, odevzdávání změn a odesílání PR:


https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017


## Co je to korektura?


Korektura je závěrečný proces kontroly psaného textu, jehož cílem je odhalit a opravit gramatické, pravopisné, interpunkční a formátovací chyby. Zajišťuje, aby byl text před zveřejněním nebo odevzdáním jasný, souvislý a bez chyb.


Při řešení tohoto typu úkolu je důležité dodržet význam původního jazyka (EN nebo FR), ale dbát na to, aby byl text ve finálním jazyce co nejplynulejší pro rodilého mluvčího.


Vždy mějte na paměti, že překlad/korektura je VZDĚLÁVÁNÍ!


Naším společným cílem je totiž vzdělávat co nejvíce lidí v oblasti Bitcoin, a proto je zásadní, aby materiály, které čtou, byly plynulé a srozumitelné.

V tomto smyslu jsou všichni přispěvatelé na Akademii Plan ₿ pedagogové!


## První kroky před korekturou na Akademii Plan ₿


Před zahájením nového korektorského úkolu jej oznamte ve skupině [Telegram](https://t.me/PlanBNetwork_ContentBuilder) nebo informujte svého koordinátora Akademie Plán ₿, který otevře speciální [issue](https://github.com/orgs/PlanB-Network/projects/3). Jakmile obdržíte odkaz na vydání, jednoduše **komentujte, že začínáte** s úkolem korektury daného obsahu.


Tento systém pomáhá koordinátorovi sledovat průběh práce v repozitáři a umožňuje korektorovi "nárokovat" obsah, čímž se zabrání duplicitnímu úsilí někoho jiného.

V samotném vydání najdete odkazy, které vás přesměrují na obsah ke kontrole. Můžete na ně jednoduše kliknout, nebo ještě lépe, můžete se vrátit do vlastního forknutého repozitáře a pracovat přímo odtud. Pojďme se podívat, jak to můžete udělat!


Především **VŽDY nezapomeňte na SYNCHRONIZACI repozitáře ve větvi "dev "**. Tímto způsobem bude obsah vždy aktualizován před zahájením jakéhokoli typu úlohy a nebudete vytvářet konflikty mezi starým a novým materiálem. Nezapomeňte kliknout na "Synchronizovat fork" a "Aktualizovat větev".



![REVIEW](assets/en/1.webp)



Po úspěšné synchronizaci můžete přímo přistupovat k obsahu, který vás zajímá, a odevzdat jej v nové větvi, jak ukazuje tento [tutoriál](https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017). V opačném případě si můžete otevřít novou větev, ve které budete pracovat, kliknutím na "Branches" (Větve), jak je uvedeno níže.



![REVIEW](assets/en/2.webp)



Na této nové stránce najdete všechny pobočky, které jste již otevřeli, pod názvem "Vaše pobočky". Tato část je velmi užitečná, protože umožňuje snadno najít, kde jste upravili nějaký obsah. Pokud chcete otevřít novou pobočku, můžete kliknout na "Nová pobočka" v pravém horním rohu stránky.



![REVIEW](assets/en/3.webp)



Poté se zobrazí vyskakovací okno, do kterého je třeba vložit název nové větve. V níže uvedeném případě jsem zvolil název "BTC101-FR". Tímto způsobem si budu vždy pamatovat, že tuto konkrétní větev je třeba použít pro korekturu kurzu BTC101 ve francouzštině a **nebudu ji používat pro žádný jiný úkol**.


Doporučuji vám, abyste postupovali stejně: nezapomeňte otevřít novou větev, kdykoli budete chtít začít nový úkol.



![REVIEW](assets/en/4.webp)



Po vytvoření této nové větve na ni klikněte v části "Vaše větve" na předchozí stránce a začněte pracovat na souboru *.md*, který se týká konkrétního obsahu (v mém případě kliknu na "kurzy" -> "BTC101" -> "fr.md"). Všechny revize související s konkrétním souborem budou muset být odevzdány (uloženy) uvnitř stejné větve.



## Původní jazyk nebo překlad?


Při korekturách obsahu je důležité **vždy zkontrolovat původní anglickou (nebo francouzskou)** verzi. Uvědomte si, že překládáme pomocí nástrojů umělé inteligence, takže vykreslení v cílovém jazyce nemusí být plynulé nebo dobře srozumitelné pro konečného čtenáře.


V případě potřeby můžete text upravit a změnit věty. Naším cílem je zvýšit plynulost, ale vždy se držet původního významu. V případě pochybností, jak zacházet s konkrétním slovem, se určitě zeptejte koordinátora překladu.


Nástroje LLM mohou některá slova související s Bitcoin překládat doslovně, stejně jako Lightning Network. Je to zejména v případě, kdy se jedná o velmi odborná slova. V takových případech je vhodné pro lepší srozumitelnost zachovat původní anglické slovo v cílovém jazyce, pokud vám vaše jazyková pravidla neukládají překládat každé slovo.


V tomto druhém případě si **vždy vyhledejte, zda dané slovo** již nepřeložil někdo jiný z vaší komunity Bitcoin a zda se nyní široce používá.



- Jedním z řešení by mohlo být **zkontrolovat na [BitcoinWiki](https://en.bitcoin.it/wiki/Main_Page)** v cílovém jazyce, zda bylo slovo přeloženo, nebo ne. Pokud není, ponecháte slovo v angličtině.



- V každém případě bych doporučoval **vložit EN slovo nicméně** a přidat odpovídající význam v cílovém jazyce do kulaté závorky podle schématu EN (LANG) nebo naopak. Např. Address (indirizzo) nebo indirizzo (adresa).



- Dalším dobrým řešením je zachovat původní slovo/výraz a pak **vytvořit hypertextový odkaz**, který přesměruje na [glosář](https://planb.academy/en/resources/glossary) na webu planb.network. K tomu je třeba vložit slovo/frázi do hranatých závorek a odkaz do kulatých závorek, jak vidíte v příkladu níže:


```
[UTXO](https://planb.academy/resources/glossary/utxo)
```


V konečném výsledku (obrázek níže) se nezobrazí celý odkaz a slovo se stane klikacím.



![REVIEW](assets/en/5.webp)



Vezměte prosím na vědomí, že odkaz na glosář, který získáte z webové stránky, obsahuje za slovem "síť" kód jazyka (příklad: ``https://planb.academy/en/resources/glossary/utxo``-> zde si můžete přečíst kód jazyka "cs"). V takovém případě **odstraňte jazykový kód z odkazu**, jak jste viděli v rámečku výše. Tímto způsobem systém čtenáře automaticky přenese do jím určeného jazyka.


Obsah úložiště je plný hypertextových odkazů, jako jsou tyto výše uvedené. Nyní, když víte, co znamenají, **zajistěte, abyste neodstranili žádný odkaz** vložený původním autorem.



- S vykreslováním slov souvisí také následující. Pokud v textu najdete "Plan ₿ Academy", **ponechte jej v tomto původním tvaru**. Nepřekládejte slovo "plan" ani slovo "network". Kromě toho při uvádění názvu Plan ₿ Academy NEPOUŽÍVEJTE člen "The": **považujte ji za značku**.



- Totéž platí pro "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", které by měly být rovněž zachovány v původní podobě.


Poslední poznámka k tomuto odstavci: jak jsme uvedli výše, k překladu obsahu používáme nástroje umělé inteligence a poté žádáme přispěvatele o zásah, abychom se ujistili, že je vše plynulé a dobře zkontrolované.


Pokud ke korektuře většiny textu použijete umělou inteligenci, určitě si toho všimneme, protože známe typické struktury vět, které umělá inteligence generuje. Pokud zjistíme, že jste se při korekturách spoléhali pouze na UI, aniž byste použili výrazné změny, může být výsledná odměna v sats snížena na polovinu!



## Struktura záhlaví


V jazyce markdown začínají všechny nadpisy (a názvy odstavců) znakem hash ``#``. Počet znaků hash odpovídá úrovni nadpisu. Například nadpis třetí úrovně má před textem tři číselné znaky (např. `#### Můj nadpis`).


V kurzech jsou nejdůležitější části představeny jedním hash znakem, zatímco dílčí části mohou mít dva až čtyři hash znaky. Ve výukových kurzech obvykle používáme pouze záhlaví se dvěma hash znaky.



![REVIEW](assets/en/6.webp)



Dbejte na to, abyste před nadpisem NIKDY neodstraňovali znaky hash**, jinak způsobíte problémy se strukturou textu.


Zároveň **nezměňte** část chapterID, kterou vidíte na obrázku výše, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` nebo odkazy na video, jako ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


Když před název vložíme ``#``, v náhledu kurzu se automaticky zvýrazní tučným písmem, takže **se vyhněte tomu, aby byly názvy při opravách tučné**.


Poznámka na okraj: v EN verzi kurzů mají **názvy uvozené jedním nebo dvěma ``#`` všechna slova začínající velkými písmeny**, zatímco názvy začínající třemi nebo čtyřmi ``#`` toto pravidlo obvykle nedodržují. Pokud je to možné, ujistěte se, že názvy v cílovém jazyce dodržují tuto strukturu.



## Úvodní část kurzů


Na začátku jakéhokoli obsahu najdete následující statická slova psaná malými písmeny: "název", "popis", "cíle". Jsou používána webovými stránkami k dekódování samotného obsahu a jsou **vždy ponechána v EN**. V důsledku toho je NEPŘEKLÁDEJTE, jinak obsah způsobí problémy se synchronizací. Ujistěte se, že jste zkontrolovali pouze část za dvojtečkou, která je automaticky přeložena umělou inteligencí.



![REVIEW](assets/en/7.webp)



V téže úvodní části zachovejte stávající formát. Na začátek textu nic nepřidávejte. Např. se vyhněte přidávání "tt" před pomlčky, jako na obrázku níže!



![REVIEW](assets/en/8.webp)


## Jak se vypořádat s obrázky z kurzů


Na našich webových stránkách jsou nyní k dispozici přeložené obrázky pro téměř každý kurz!


Při korektuře vždy zkontrolujte, zda jsou všechny obrázky přítomny a správně zobrazeny. Pokud v `zobrazení kódu` najdete takovýto řádek `![IMAGE](assets/en/001.webp)`, znamená to, že se zde zobrazí obrázek.


Mezi kód obrázku a text vždy přidejte nový řádek. Příklad níže:


```
WRONG CONFIGURATION:
- to start translating, click on the button `Translate`: ![language](assets/08.webp)
To save, click on `save`!


RIGHT CONFIGURATION:

- to start translating, click on the button `Translate`:

![language](assets/08.webp)

To save, click on `save`!
```



Kromě toho si nezapomeňte přečíst obsah každého obrázku. Pokud si všimnete jakýchkoli problémů s překladem textu uvnitř obrázků, informujte o tom koordinátora a dostanete možnost provést korekturu i vy!


Obrázek si můžete prohlédnout v sekci `Preview` na Githubu (nebo na našich webových stránkách, otevřete v jiné záložce). Poté se vraťte do vedlejší sekce `kód` a proveďte korekturu.


![REVIEW](assets/en/9.webp)


## Doporučení pro formát


Níže najdete několik příkladů formátových problémů, na které je třeba dávat pozor při korektuře obsahu v cílovém jazyce.



- Věnujte pozornost podivným interpunkčním znaménkům, jako je `\*\*`` nebo ``**``, která mohou představovat špatné vykreslení tučného symbolu. Na obrázku níže vidíte, že hvězdičky jsou pouze v pravé části slova, což vypadá divně.



![REVIEW](assets/en/10.webp)



Proto vždy zkontrolujte originální anglický text, abyste zjistili, zda tam má být tučný text. V takovém případě stačí přidat na začátek slova dvě hvězdičky, aby se na webu zobrazilo správně. Ve skutečnosti je v jazyce markdown **pro zobrazení tučného písma nutné vložit dvě hvězdičky ``**`` před i za slovo/větu** (viz příklad níže).



![REVIEW](assets/en/11.webp)




- Stejné problémy mohou nastat u symbolů jako $ a `` `` ``.

Ujistěte se, že jste zkontrolovali původní jazykový soubor (často EN nebo FR), abyste zjistili, kde mají tyto symboly být. Vždy můžete v této věci požádat o pomoc koordinátora.



- Pokud najdete citáty, nezapomeňte si na internetu vyhledat správný překlad ve vašem jazyce. Uvozovky se obvykle vkládají za symbol ``>``.



![REVIEW](assets/en/12.webp)




## Korektury výukových programů


Pokud se rozhodnete provést korekturu výukových materiálů, koordinátor otevře zvláštní otázku pro **celou sekci výukových materiálů**. Po dokončení úkolu můžete svůj postup zdokumentovat komentářem v čísle se seznamem zkontrolovaných tutoriálů: vytvoříte si tak přehledný systém sledování pro budoucí použití, což je důležité, protože každý měsíc přibývá nový obsah. Příklad tohoto přístupu si můžete prohlédnout [zde](https://github.com/PlanB-Network/bitcoin-educational-content/issues/3023#issuecomment-3364923190).


![REVIEW](assets/en/13.webp)


Vzhledem k tomu, že nové výukové programy jsou přidávány každý měsíc, může se stát, že vaše pobočka bude během korektur zastaralá. Někteří korektoři k tomuto problému přistupují tak, že synchronizují přesně tu větev, ve které pracují: **Nikdy to prosím nedělejte! Pokud to uděláte, riskujete, že ztratíte veškerý pokrok, kterého jste do té doby dosáhli!**


Místo toho byste měli nejprve dokončit korektury výukových programů v aktuálním fork. Poté **synchronizujte `dev`** a vytvořte novou větev, ve které se zaměříte na korektury nově přidaných výukových materiálů (pouze těch, které v předchozí větvi chybí).


V tutoriálech je možné, že **obrázky nebudou přeloženy**. Vzhledem k tomu, že většina výukových programů je **původně napsána ve francouzštině nebo angličtině**, pravděpodobně najdete obrázky, které obsahují příkazy nebo pokyny v původním jazyce. Uveďme si příklad z výukového programu Sparrow v nizozemštině, a to tak, že uvedeme text i související obrázek.


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Publieke server_".
```


![REVIEW](assets/en/14.webp)


Jak vidíte, obrázek jasně ukazuje na `Veřejný server`, v angličtině, zatímco v textu je uveden výraz `_Publieke server_`. V tomto případě je problém s koherencí, protože čtenář při konfrontaci obrázku s textem nachází protichůdné informace.


Tuto záležitost vyřešíte tak, že vložíte příkaz tak, jak je zobrazen na obrázku (anglicky nebo francouzsky), a do závorek vložíte překlad do vašeho jazyka , jak je uvedeno níže:


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Public Server_" (Publieke server).
```



## Korektury kvízů


Věděli jste, že můžete také opravovat kvízové otázky v každém kurzu? Chcete-li například opravit kvízy pro kurz BTC101 v oblasti IT, můžete si otevřít zvláštní větev a postupovat touto cestou: "kurzy" -> "BTC101" -> "kvíz". Tam najdete všechny složky věnované jednotlivým otázkám spolu s příslušným jazykovým souborem ve formátu _yml_.


Opět se ujistěte, že se nacházíte ve vyhrazené pobočce, kterou jste otevřeli speciálně pro tento účel, a vždy informujte koordinátora.


Při korektuře tohoto typu souboru _yml_ je důležité mít na paměti, abyste se vyhnuli přidávání dvojteček ``:`` nebo uvozovek uvnitř textu. Dvojtečka se ve skutečnosti **používá** pouze k oddělení dvojic klíč-hodnota, jako je "wrong_answers", od ostatních. Příklad můžete vidět na obrázku níže:


![REVIEW](assets/en/15.webp)


Po přezkoumání otázky se ujistěte, že jste změnili stav "přezkoumáno" z "false" na "true", jak je znázorněno na obrázku níže. Ujistěte se, že **zachováváte tyto stavy v angličtině**, bez ohledu na to, v jakém jazyce pracujete!



![REVIEW](assets/en/16.webp)


Pokud chybí stavový řádek "reviewed:true", nezapomeňte jej **přidat na konec kvízu**.


## Korektury glosáře


Stejně jako u kvízů můžete provést korekturu slovníčku. Původní slovníček byl napsán ve francouzštině, takže v něm najdete věty jako např: "Ve francouzštině lze tento výraz přeložit jako..."


V takových případech větu přizpůsobte cílovému jazyku nebo angličtině. Například můžete napsat "V angličtině je tento výraz...".

Pokud je název ponechán v angličtině, můžete větu přizpůsobit svému jazyku: "Ve svahilštině je tento výraz..."


Kromě toho dbejte na to, abyste názvy psali VELKÝMI PÍSMENY.


![REVIEW](assets/en/17.webp)



## Název a popis vašeho PR


Při odesílání PR by bylo úžasné, kdybyste ji pojmenovali v tomto formátu: [KOREKTURA] NÁZEV OBSAHU - JAZYK:


```
[PROOFREADING] BTC101 - ENGLISH
```


Kromě toho můžete do části **komentáře k PR** napsat "uzavírá" + číslo problému, které vám koordinátor poslal při zahájení korektury, před které napíšete ``#``.

Pokud jste například právě odeslali PR s korekturou cyp201 + kvízy, můžete napsat "uzavírá [#2934](https://github.com/PlanB-Network/bitcoin-educational-content/issues/2934)".


Tímto způsobem budou PR a problém propojeny a kdokoli bude číst veřejný repozitář Github, může snadno najít informace.



## Další osvědčené postupy



- Pokud potřebujete v textu vyhledat konkrétní slova, můžete kliknout na ``CTRL+F`` a zobrazí se část pro vyhledávání a nahrazování. Tato část je velmi užitečná, pokud potřebujete přejít na určitou část textu nebo potřebujete hromadně nahradit konkrétní slova/věty, aniž byste museli procházet celý obsah.



![REVIEW](assets/en/18.webp)



Při použití funkce "nahradit vše" je důležité překontrolovat výsledky, abyste se ujistili, že odkazy nebyly také změněny. Chcete-li například změnit slovo "Bitcoin" na "Bitkoin" (což může být v některých jazycích nezbytné), můžete pomocí funkce "nahradit vše" efektivně aktualizovat všechny výskyty v textu. Mějte však na paměti, že tento nástroj změní také všechny odkazy obsahující toto slovo, což může vést k problémům s přesměrováním.


V níže uvedeném příkladu korektor použil výše uvedenou funkci k nahrazení slova "satoshi" slovem "satoshi(sats)" a také změnil odkaz na výukový program obsahující samotné slovo. V důsledku toho se odkaz stal neplatným.


Vždy překontrolujte všechny hypertextové odkazy v textu a ujistěte se, že jsou správné.



![REVIEW](assets/en/19.webp)




- V návaznosti na téma, pokud autor vloží odkaz odkazující na kurz nebo výukový kurz Plan ₿ Academy (**ne** v závorce), webová stránka automaticky vytvoří "kartu" zobrazující související miniaturu. V důsledku toho vždy dbejte na to, abyste mezi text a samotný odkaz **vložili nový řádek**, jinak se může na webu zobrazit následující chyba.



![REVIEW](assets/en/20.webp)



## Závěr


Pokud to shrneme, znalost běžných chyb korektorů vám může pomoci zlepšit vaše dovednosti při kontrole obsahu. Je snadné přehlédnout takové věci, jako je kontext nebo konzistence, a zachycení těchto chyb může mít velký význam.


Vždy mějte na paměti, že tyto kurzy a výukové programy může číst i začátečník, takže je naší povinností zajistit, aby jim plně porozuměl. **Jako korektor jste pedagogem!**


Nyní jste připraveni začít s korekturami kurzů, výukových programů, kvízů a slovníčků. Zůstaňte naladěni, abyste mohli začít kontrolovat také přepisy videí!


Děkujeme, že jste si přečetli tento návod, a přejeme vám příjemnou cestu za korekturami!