---
term: BIP
---

Akronym pro "Bitcoin Improvement Proposal" (Návrh na vylepšení Bitcoinu). Bitcoin Improvement Proposal (BIP) je formální proces pro navrhování a dokumentování vylepšení a změn protokolu Bitcoinu a jeho standardů. Jelikož Bitcoin nemá centrální entitu, která by rozhodovala o aktualizacích, BIPy umožňují komunitě navrhovat, diskutovat a implementovat vylepšení strukturovaným a transparentním způsobem. Každý BIP detailně popisuje cíle navrhovaného vylepšení, odůvodnění, potenciální dopady na kompatibilitu, stejně jako výhody a nevýhody. BIPy mohou psát jakýkoliv člen komunity, ale musí být schváleny ostatními vývojáři a editory, kteří udržují databázi Bitcoin Core na GitHubu: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun a Ruben Somsen. Je však důležité pochopit, že role těchto jedinců při editaci BIPů neznamená, že kontrolují Bitcoin. Pokud někdo navrhne vylepšení, které není přijato v rámci formálního rámce BIP, může ho stále představit přímo komunitě Bitcoinu nebo dokonce vytvořit fork obsahující jejich modifikaci. Výhoda procesu BIP spočívá ve formálnosti a centralizaci, které usnadňují debatu a snaží se vyhnout rozdělení mezi uživateli Bitcoinu, s cílem implementovat aktualizace konsenzuálním způsobem. Nakonec je to princip ekonomické většiny, který určuje mocenské dynamiky v rámci protokolu.

BIPy jsou klasifikovány do tří hlavních kategorií:
* *Standards Track BIPs*: Týkají se modifikací, které přímo ovlivňují implementace Bitcoinu, jako jsou pravidla pro validaci transakcí a bloků;
* *Informational BIPs*: Poskytují informace nebo doporučení bez navrhování přímých změn protokolu;
* *Process BIPs*: Popisují změny v procesech okolo Bitcoinu, jako jsou procesy správy.

Standards Track a Informational BIPy jsou také klasifikovány podle "Vrstvy":
* *Consensus Layer*: BIPy v této vrstvě se týkají pravidel konsensu Bitcoinu, jako jsou modifikace pravidel pro validaci bloků nebo transakcí. Tyto návrhy mohou být buď soft forky (zpětně kompatibilní modifikace) nebo hard forky (ne-zpětně kompatibilní modifikace). Například BIPy pro SegWit a Taproot patří do této kategorie;
* *Peer Services*: Tato vrstva se týká provozu sítě uzlů Bitcoinu, tj. jak uzly nalézají a komunikují mezi sebou na internetu.
* *API/RPC*: BIPy této vrstvy se týkají aplikačních programovacích rozhraní (API) a vzdálených procedurálních volání (RPC), které umožňují softwaru Bitcoinu interagovat s uzly;
* *Applications Layer*: Tato vrstva se týká aplikací postavených na Bitcoinu. BIPy v této kategorii se typicky zabývají modifikacemi na úrovni standardů Bitcoinových peněženek.

Proces podávání BIP začíná konceptualizací a diskusí o nápadu na mailing listu *Bitcoin-dev*. Pokud je nápad slibný, autor vytvoří návrh BIPu podle specifického formátu a podá ho prostřednictvím Pull Requestu na Core GitHub repozitáři. Editory tento návrh přezkoumají, aby ověřili, že splňuje všechna kritéria. BIP musí být technicky proveditelný, prospěšný pro protokol, musí dodržovat požadované formátování a být v souladu s filozofií Bitcoinu. Pokud BIP splňuje tyto podmínky, je oficiálně integrován do GitHub repozitáře BIPů. Poté je mu přiděleno číslo. Toto číslo obvykle určuje editor, často Luke Dashjr, a je přiděleno logicky: BIPy, které se zabývají podobnými tématy, často dostávají po sobě jdoucí čísla.

BIPy poté procházejí různými stavy během svého životního cyklu. Aktuální stav je specifikován v hlavičce každého BIPu:
* Draft: Návrh je stále ve fázi konceptualizace a debaty;
* Navrženo: BIP je považován za kompletní a připravený k přezkumu komunitou;
* Odloženo: BIP je odložen na později šampionem nebo editorem;
* Zamítnuto: BIP je klasifikován jako zamítnutý, pokud nevykazoval žádnou aktivitu po dobu 3 let. Jeho autor si může později vybrat jeho obnovení, což by mu umožnilo vrátit se do stavu návrhu;
* Staženo: BIP byl stažen jeho autorem;
* Finální: BIP je přijat a široce implementován v Bitcoinu;
* Aktivní: Pouze pro procesní BIPy, tento status je přiřazen, jakmile je dosaženo určitého konsensu;
* Nahrazeno / Zastaralé: BIP již není aplikovatelný nebo byl nahrazen novějším návrhem, který jej činí zbytečným.

![](../../dictionnaire/assets/25.png)

> ► *BIP je zkratka pro "Bitcoin Improvement Proposal". Ve francouzštině lze přeložit jako "Proposition d'amélioration de Bitcoin". Nicméně, ve většině francouzských textů se přímo používá zkratka "BIP" jako obecné podstatné jméno, někdy ženského, někdy mužského rodu.*