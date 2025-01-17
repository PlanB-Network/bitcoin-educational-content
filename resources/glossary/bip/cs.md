---
term: BIP

---
Zkratka pro "Bitcoin Improvement Proposal" Bitcoin Improvement Proposal (BIP) je formální proces navrhování a dokumentování vylepšení a změn protokolu Bitcoin a jeho standardů. Vzhledem k tomu, že Bitcoin nemá centrální subjekt, který by rozhodoval o aktualizacích, umožňují BIP komunitě navrhovat, diskutovat a zavádět vylepšení strukturovaným a transparentním způsobem. Každý BIP podrobně popisuje cíle navrhovaného vylepšení, zdůvodnění, potenciální dopady na kompatibilitu a také výhody a nevýhody. BIP může napsat kterýkoli člen komunity, ale musí být schválen ostatními vývojáři a editory, kteří spravují databázi Bitcoin Core GitHub: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun a Ruben Somsen. Je však důležité si uvědomit, že úloha těchto osob při editaci BIP neznamená, že ovládají Bitcoin. Pokud někdo navrhne vylepšení, které není přijato v rámci formálního rámce BIP, může je stále předložit přímo komunitě Bitcoinu nebo dokonce vytvořit fork zahrnující jeho úpravu. Výhoda procesu BIP spočívá v jeho formálnosti a centralizaci, které usnadňují diskusi, aby se zabránilo rozdělení mezi uživateli Bitcoinu, kteří se snaží implementovat aktualizace konsensuálním způsobem. Nakonec je to princip ekonomické většiny, který určuje dynamiku moci v rámci protokolu.

BIP se dělí do tří hlavních kategorií:


- BIPs pro sledování standardů*: Týkají se úprav, které přímo ovlivňují implementace Bitcoinu, jako jsou pravidla pro ověřování transakcí a bloků;
- Informační BIP*: BIP: poskytují informace nebo doporučení, aniž by navrhovaly přímé změny protokolu;
- Zpracování BIP*: Popište změny v postupech týkajících se bitcoinu, například v procesech řízení.

BIP pro sledování standardů a informační BIP jsou také klasifikovány podle "vrstvy":


- Konsenzuální vrstva*: BIP v této vrstvě se týkají pravidel konsensu Bitcoinu, například úprav pravidel pro ověřování bloků nebo transakcí. Tyto návrhy mohou být buď měkké (zpětně kompatibilní úpravy), nebo tvrdé (zpětně nekompatibilní úpravy). Do této kategorie patří například BIP pro SegWit a Taproot;
- Peer služby*: Tato vrstva se týká fungování sítě uzlů Bitcoinu, tj. způsobu, jakým uzly na internetu vyhledávají a komunikují mezi sebou.
- API/RPC*: BIP této vrstvy se týkají rozhraní pro programování aplikací (API) a volání vzdálených procedur (RPC), které umožňují interakci softwaru Bitcoinu s uzly;
- Vrstva aplikací*: Tato vrstva se týká aplikací postavených nad Bitcoinem. BIP v této kategorii se obvykle zabývají úpravami na úrovni standardů bitcoinových peněženek.

Proces předkládání BIP začíná koncepcí a diskusí o nápadu v e-mailové konferenci *Bitcoin-dev*. Pokud je nápad slibný, autor vypracuje návrh BIP podle určitého formátu a odešle jej prostřednictvím žádosti o vytažení (Pull Request) v úložišti Core GitHub. Redakce tento návrh přezkoumá a ověří, zda splňuje všechna kritéria. BIP musí být technicky proveditelný, přínosný pro protokol, musí splňovat požadované formátování a být v souladu s filozofií Bitcoinu. Pokud BIP tyto podmínky splňuje, je oficiálně začleněn do repozitáře BIP na GitHubu. Poté je mu přiděleno číslo. O tomto čísle zpravidla rozhoduje editor, často Luke Dashjr, a přiděluje se logicky: BIPy, které se zabývají podobnými tématy, často dostávají po sobě jdoucí čísla.

BIP pak v průběhu svého životního cyklu procházejí různými statusy. Aktuální stav je uveden v záhlaví každého BIP:


- Návrh: Návrh je stále ve fázi přípravy a projednávání;
- Navrhované: BIP je považován za dokončený a připravený k přezkoumání komunitou;
- Odloženo: Šampion nebo editor odloží BIP na později;
- Zamítnuto: BIP je klasifikován jako zamítnutý, pokud po dobu tří let nevykazoval žádnou činnost. Jeho autor se může rozhodnout jej později obnovit, což by mu umožnilo vrátit se do stavu návrhu;
- Staženo: BIP byl autorem stažen;
- Finále: BIP je v Bitcoinech akceptován a široce implementován;
- Aktivní: Tento status je přidělen pouze procesním BIP, jakmile je dosaženo určitého konsensu;
- Nahrazeno / zastaralé: BIP již není použitelný nebo byl nahrazen novějším návrhem, který jej činí zbytečným.

![](../../dictionnaire/assets/25.webp)

> ► *BIP je zkratka pro "Bitcoin Improvement Proposal". Do francouzštiny se dá přeložit jako "Proposition d'amélioration de Bitcoin". Ve většině francouzských textů se však zkratka "BIP" používá přímo jako obecné podstatné jméno, někdy v ženském, někdy v mužském rodě.*