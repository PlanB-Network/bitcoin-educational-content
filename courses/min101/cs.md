---
name: Úvod do Bitcoin mining
goal: Porozumění Bitcoin mining a proof-of-work od začátku
objectives: 


  - Porozumět proof-of-work a jeho úloze v Bitcoin.
  - Analyzujte mechanismus nastavení obtížnosti.
  - Zjistěte, co vlastně znamenají technické termíny spojené s mining.
  - Popište kroky při sestavování bloku Bitcoin a jeho součástí.
  - Identifikovat hlavní vývoj v odvětví mining.


---

# Objevte základy Bitcoin mining



Porozumět proof of work znamená pochopit, jak funguje Bitcoin. Bez tohoto vynálezu a jeho důmyslného využití by Bitcoin jednoduše nemohl existovat. Tento kurz vám poskytne veškerou teorii mining, kterou potřebujete pro svou bitcoinovou cestu.



MIN 101 je určen především začátečníkům, protože vysvětluje všechny pojmy přesně od začátku. Pokud však již máte středně pokročilé znalosti, umožní vám tento kurz upevnit si své znalosti, opravit některé přibližné intuice a prozkoumat detaily, které v běžných výkladech často chybí.



Na konci tohoto kurzu budete schopni jednoduše a důsledně vysvětlit, jak funguje systém proof-of-work. MIN 101 je také ideálním úvodem do všech dalších pokročilejších kurzů věnovaných Bitcoin mining na Plan ₿ Academy, ať už teoretických, nebo praktických.



+++


# Úvod


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Přehled kurzů


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Vítejte v kurzu MIN 101, ve kterém se seznámíte se základními teoretickými koncepty mining a Proof-of-Work v rámci systému Bitcoin. Tento kurz je prvním krokem na vaší cestě bitcoinera za pochopením fungování mining. Po jeho absolvování budete moci přejít k pokročilejším teoretickým kurzům nebo se pustit do praktického těžení a sami se stát těžařem bitcoinů!



V tomto kurzu MIN 101 se nebudeme vracet k základním pojmům Bitcoin, protože půjdeme přímo k jádru věci: mining. Pokud jste o Bitcoin nikdy neslyšeli nebo pokud jsou vám jeho základy stále trochu nejasné, důrazně vám doporučuji začít naším úvodním kurzem BTC 101. Jakmile si tyto základy osvojíte, budete se moci s jistotou pustit do kurzu MIN 101:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Část 1 - Úvod



Tento kurz začneme nepovinnou první kapitolou, ve které vám nabídnu velmi zjednodušené vysvětlení mining, abyste si udělali jasnou představu, než se pustíte do technických mechanismů.



Cílem této kapitoly není poskytnout vám všechny technické podrobnosti (ty přijdou na řadu později v průběhu kurzu), ale poskytnout vám vodítko. Jakmile si tento rámec vytvoříte, každý pokročilejší koncept, který bude představen později, do této struktury přirozeně zapadne.



### Část 2 - Jak funguje proof of work



Po úvodu je 2. část technickým základem vzdělávacího programu. Jejím cílem je krok za krokem vysvětlit, jak Bitcoin vytváří platné bloky. Začneme objevováním struktury bloku a poté přejdeme k mechanismu proof-of-work: úloze cíle, nonce a hašovací funkce. Nakonec se podíváme, jak se Bitcoin daří udržovat stabilní míru produkce bloků navzdory výkyvům v hashovací síle, a to díky mechanismu nastavení obtížnosti. Na konci této části budete mít úplnou představu o základních principech Bitcoin proof-of-work.



### Část 3 - Motivační systém Bitcoin mining



Ve třetí části se podíváme na to, proč jsou horníci vybízeni k poctivé účasti na mining. Podrobně popíšeme princip blokové odměny, její složení a způsob výpočtu, její vývoj v čase prostřednictvím halvování a specifickou roli transakce na coinbase.



### Část 4 - Průmysl Bitcoin mining



Čtvrtá část vrací mining do provozní reality. Sleduje vývoj strojů mining od počátku Bitcoin až po moderní ASIC, aby bylo možné pochopit současná hardwarová omezení. Podíváme se také na základy poolů mining, abychom pochopili, jak se těžařům daří snižovat rozptyl jejich příjmů.



### Část 5 - Závěrečná část



V závěrečné části kurzu si můžete vyzkoušet své znalosti o mining při předávání diplomu.



Cílem tohoto kurzu MIN 101 je proto umožnit vám odejít s jasnými, strukturovanými a trvalými znalostmi o Bitcoin mining, a to jak z technického, tak z ekonomického hlediska.



Jste připraveni objevit Bitcoin mining? Začněme!




## Bitcoin mining snadno


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Než přejdu k podrobnějšímu a techničtějšímu vysvětlení Bitcoin [mining](https://planb.academy/resources/glossary/mining), rád bych vás seznámil s principem, který je záměrně jednoduchý a schematický. Pokud již máte základní znalosti, můžete v další kapitole, po zodpovězení kvízových otázek, přejít přímo k jádru věci. Tato kapitola je určena především začátečníkům, abyste mohli začít nenásilně.



Představte si Bitcoin jako velký veřejný zápisník sdílený všemi, kam si zapisujeme, kdo komu poslal bitcoiny. Tomuto zápisníku se říká [blockchain](https://planb.academy/resources/glossary/blockchain). Nemůže ho mít v držení jen jeden člověk, jinak by musel být důvěryhodný. Místo toho Bitcoin funguje kolektivně: tisíce počítačů ověřují a udržují stejnou verzi tohoto zápisníku.



![Image](assets/fr/049.webp)



Když v systému Bitcoin provedete platbu, vytvoříte [transakci](https://planb.academy/resources/glossary/transaction-tx). Tato transakce není okamžitě přidána do zápisníku. Nejprve je odeslána do sítě a poté čeká na začlenění do dalšího transakčního paketu. Tento paket se nazývá [blok](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



Blok je jednoduše sada transakcí seskupených dohromady. Když je blok připraven, nestačí ho jen zveřejnit. Musíte síti dokázat, že si blok zaslouží být přidán do fondu. Zde přichází na řadu mining.



Mining je práce při ověřování bloku spotřebou energie. Aktéři zvaní [těžaři](https://planb.academy/resources/glossary/miner) používají specializované počítače. Tyto stroje spotřebovávají elektrickou energii na provádění velmi velkého počtu testů ve smyčce, dokud nenajdou důkaz, který síť akceptuje. Když těžař tento důkaz najde, je jeho blok považován za platný.



Jakmile je blok ověřen, je vysílán do sítě. Ostatní [uzly](https://planb.academy/resources/glossary/node) rychle zkontrolují, zda je v souladu s pravidly, a pak jej přidají do posloupnosti předchozích bloků. Proto se tomuto řetězci říká "blockchain": každý nový blok přichází za ostatními, v postupném pořadí, a tento řetězec postupně roste.



![Image](assets/fr/051.webp)



Shrneme-li to, transakce se nejprve vytvoří. Poté se seskupí do bloku. Poté těžař tento blok ověří spotřebou elektřiny. Nakonec je tento blok přidán do blockchainu a transakce v něm obsažené se stanou [potvrzenými](https://planb.academy/resources/glossary/confirmation).



Pokud horníci spotřebovávají elektřinu, není to proto, že jsou dobrovolníci. Dělají to proto, že za to dostanou odměnu. Když těžař validuje blok, získává dva druhy příjmů. Na jedné straně dostává nově vytvořené bitcoiny. Na druhé straně inkasuje [poplatky](https://planb.academy/resources/glossary/transaction-fees), které platí uživatelé za transakce zahrnuté v bloku. Jinými slovy, těžař je odměňován jednak prostřednictvím naprogramované emise peněz, jednak prostřednictvím transakčních poplatků stanovených trhem.



V této fázi máte záměrně k dispozici velmi jednoduchý pohled na mining. Zatím není podrobně vysvětleno, jak je blok konstruován, ani jak přesně funguje důkaz, který těžaři hledají, ani jak si Bitcoin udržuje stabilní tempo, ani jak se přesně vypočítává odměna, ani jak se o ni žádá. To nevadí, to všechno uvidíme ve zbytku tohoto kurzu MIN 101!



Cílem této kapitoly bylo jednoduše vám dát jasnou mentální strukturu: transakce → bloky → mining → blockchain → odměna. Tento řetězec myšlenek si zapamatujte. Ve zbytku kurzu bude každá kapitola přidávat vrstvu technických detailů k jednomu z těchto prvků, dokud nepochopíte nejen to, o co jde, ale také jak a proč to funguje spolehlivě, ve velkém měřítku, bez šéfa a bez potřeby důvěry.



# Jak proof of work funguje


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Cesta transakce Bitcoin


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Abychom pochopili, o čem je Bitcoin mining, musíme nejprve sledovat průběh typické transakce Bitcoin. To vám přesně ukáže, kde se blok dostává do hry a proč je jádrem systému. To bych chtěl, abyste v této první kapitole objevili.



V systému Bitcoin je transakce datová struktura, která převádí vlastnictví bitcoinů z jednoho uživatele na druhého. Konkrétně spotřebovává `výstupy` z minulých transakcí (tzv. [UTXO](https://planb.academy/resources/glossary/utxo)) a označuje je jako `vstupy` a poté vytváří nové `výstupy`, které určují, komu tyto bitcoiny nyní patří a za jakých podmínek je lze později utratit.



![Image](assets/fr/001.webp)



Důležitým bodem Bitcoin je oprávnění utrácet. Bitcoin nejsou na účtu, jako mohou být vaše peníze v bance, ale jsou uzamčeny podmínkami pro utrácení. Když chce [wallet](https://planb.academy/resources/glossary/wallet) použít UTXO jako [vstup](https://planb.academy/resources/glossary/input), musí poskytnout kryptografický důkaz, že má právo jej odemknout. Tento důkaz má často podobu [digitálního podpisu](https://planb.academy/resources/glossary/digital-signature) generated ze [soukromého klíče](https://planb.academy/resources/glossary/private-key). Proto bitcoináři trvají na zabezpečení svých soukromých klíčů: právě ty odemykají přístup k bitcoinům a následně umožňují jejich utrácení.



![Image](assets/fr/002.webp)



Digitální podpis v systému Bitcoin hraje dvě důležité role:




- Autorizace výdajů: prokazuje, že uživatel vlastní soukromý klíč, který se očekává podle podmínky UTXO;
- Ochrana integrity: spojuje autorizaci s přesnými údaji o transakci (příjemci, částky, poplatky atd.). Pokud někdo transakci dodatečně změní, podpis již nebude platný.



Jakmile je transakce správně sestavena a podepsána uživatelským zařízením Bitcoin wallet, musí být vysílána v síti Bitcoin.



### Úloha uzlu Bitcoin v distribuci



Bitcoin je síť typu [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p): neexistuje žádný centrální server, který by přijímal a zpracovával všechny transakce. Tuto úlohu plní uzly společně. Uzel Bitcoin je část softwaru (např. [jádro Bitcoin](https://planb.academy/resources/glossary/bitcoin-core)) připojená k ostatním uzlům v síti Bitcoin, jejímž hlavním úkolem je ověřovat, ukládat a předávat transakce a bloky.



Když odešlete transakci ze zařízení wallet, předá ji zařízení wallet uzlu (vašemu vlastnímu nebo uzlu služby). Tento uzel nejprve zkontroluje, zda transakce splňuje různá pravidla, jako např:




- podpisy jsou platné;
- vstupy odkazují na existující mince UTXO (tj. existující bitcoiny);
- tyto prostředky UTXO ještě nebyly vynaloženy jinde;
- množství [výstupů](https://planb.academy/resources/glossary/output) je menší nebo rovno množství vstupů (bitcoiny nevznikají z ničeho);
- atd.



Pokud transakce projde všemi těmito kontrolami, uzel ji rozšíří do ostatních uzlů v síti, se kterými je propojen. Ty ji zase zkontrolují a předají dál, a tak dále. Během několika sekund je transakce rozšířena a stává se známou celé síti Bitcoin nebo alespoň její velké části.



![Image](assets/fr/003.webp)



### Mempool: čekárna na transakce



Mezi okamžikem, kdy je transakce vysílána, a okamžikem, kdy je potvrzena v bloku, musí čekat. Tento čekací prostor se nazývá **paměťový fond** (zkratka slov `paměť` a `paměťový fond`). [Mempool](https://planb.academy/resources/glossary/mempool) je tedy dočasný úložný prostor pro platné, ale dosud nepotvrzené transakce.



Důležitá poznámka: neexistuje jediný mempool, pouze mempooly. Každý uzel si udržuje svůj vlastní mempool s vlastními lokálními omezeními. To znamená, že v každém okamžiku mohou mít dva uzly mírně odlišný obsah mempoolu (v závislosti na tom, co přijaly, co odmítly nebo co vyčistily).



![Image](assets/fr/004.webp)



V této fázi síť o transakci ví, ověřila ji a drží ji v paměti, dokud nebude potvrzena. K potvrzení této transakce však dojde až tehdy, když ji těžař vloží do bloku a tento blok je sítí přijat.



### Blockchain: veřejný registr časových razítek



Protože bitcoin je nehmotná měna, musí řešit jeden problém: zabránit [dvojímu utrácení](https://planb.academy/resources/glossary/double-spending-attack) bez centrální autority. Pokud se dvě transakce pokoušejí utratit stejnou částku UTXO, musí být všichni schopni konvergovat k jednomu ucelenému stavu. Satoshi Nakamoto tento problém shrnuje touto slavnou větou:



> Jediný způsob, jak potvrdit neexistenci transakce, je mít povědomí o všech transakcích.

Jinými slovy, abyste věděli, že bitcoin ještě nebyl utracen, potřebujete společný záznam o minulých výdajích.



To je úloha blockchainu: veřejného registru obsahujícího historii transakcí. Bitcoin však nezapisuje každou transakci, jakmile se uskuteční, ale seskupuje je do bloků. Každý blok funguje jako stránka historie, a systém tak funguje jako server s časovými razítky: ověřitelným způsobem řadí transakce v čase.



Tento registr nelze přepsat díky jednoduchému principu: každý blok obsahuje kryptografický otisk ([hash](https://planb.academy/resources/glossary/hash-function)) předchozího bloku. Bloky jsou tedy propojeny: pokud změníte blok z minulosti, změní se jeho hash, čímž se přeruší vazba s dalším blokem, čímž se přeruší vazba s blokem následujícím atd. Právě tento řetězec závislostí je příčinou názvu "*blockchain*".



![Image](assets/fr/005.webp)



Jakmile jsme pochopili tyto základní principy Bitcoin, můžeme popsat cíl těžaře konkrétněji: vytvořit nový blok, který rozšíří stávající řetězec tím, že zapíše čekající transakce, a pak se pokusí o jeho platnost (to je slavný "[proof of work](https://planb.academy/resources/glossary/proof-of-work)", který budeme studovat v jedné z dalších kapitol). Nejprve však v následující kapitole společně zjistíme, jak se kandidátský blok konstruuje.



## Stavba bloku Bitcoin


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Nyní jste pochopili, jak transakce Bitcoin funguje a jakou roli hraje blockchain. Než se však podrobněji podíváme na to, jak proof-of-work funguje, je tu ještě jeden zásadní krok, který musí těžař provést: konstrukce [kandidátského bloku](https://planb.academy/resources/glossary/candidate-block). Než se pustíme do hledání platného důkazu, zjistíme společně, co je to kandidátský blok a jak jej těžař konstruuje.



### Kandidátský blok



Miner si musí své bloky postavit sami, než se je pokusí vytěžit. Každý těžař si z transakcí čekajících v jeho mempoolu sestaví tzv. kandidátský blok. Sestavení kandidátského bloku se tedy skládá z:




- vybrat, které transakce se mají zahrnout;
- uspořádat tyto transakce způsobem, který je v souladu s pravidly Bitcoin;
- vytvořit metadata bloku uložená v jeho [záhlaví](https://planb.academy/resources/glossary/block-header).



Výběr transakcí se řídí jednoduchou ekonomickou logikou: blok má kapacitu omezenou protokolem Bitcoin, takže těžař se snaží maximalizovat to, co za tento prostor získá. Vybírá si přednostně transakce, které nabízejí nejvyšší poplatky v poměru k prostoru, který v bloku zabírají (to je známé jako "sazba poplatků", vyjádřená v sats/vB). Podrobnostmi o poplatcích se budeme zabývat později; stačí si zapamatovat myšlenku třídění podle efektivity prostoru.



Blok Bitcoin se proto skládá ze dvou hlavních částí:




- seznam transakcí;
- záhlaví bloku, které slouží svým způsobem jako identifikační karta bloku.



![Image](assets/fr/006.webp)



Záhlaví je zásadní, protože se používá jako základ pro proof-of-work: v Bitcoin netěžíte přímo celý blok; těžíte pouze záhlaví bloku, které shrnuje informace potřebné k propojení bloku s řetězcem a k odevzdání jeho obsahu. Aby záhlaví mohlo reprezentovat všechny transakce, používá Bitcoin kryptografický nástroj: [Merkleho strom](https://planb.academy/resources/glossary/merkle-tree).



### Merklův strom: shrnutí velkého souboru transakcí



Výpis všech transakcí v záhlaví by byl nemožný: blok může obsahovat tisíce transakcí, zatímco záhlaví má pevnou velikost (80 bajtů). Řešením je proto výpočet jedinečného hashe, který závisí na všech transakcích v bloku: jedná se o [Merkleho kořen](https://planb.academy/resources/glossary/merkle-root).



Princip je následující:




- se vypočítá kryptografický otisk (hash) každé transakce;
- tyto hashe se spárují, spojí a poté se opět hashují, aby se vytvořila nová vrstva hashů;
- tento proces se opakuje, dokud se nezíská jediný konečný hash: Merkleho kořen.



![Image](assets/fr/007.webp)



Pokud tedy dojde ke změně jedné transakce, byť jen o jediný bit, výsledkem je změna jejího otisku, která se rozšíří do kořene Merkle. Tento kořen je obsažen v záhlaví bloku. Změna minulé transakce tedy znamená změnu záhlaví bloku, v němž je zahrnuta, a tedy i otisku bloku a následně i propojení s následujícími bloky.



Od [SegWit](https://planb.academy/resources/glossary/segwit) jsme oddělili podpisy od zbytku. Ve skutečnosti jsou tedy v každém bloku vnořeny 2 Merklovy stromy. Toto oddělení má důsledky pro způsob, jakým počítáme velikost bloku, a pro některé kryptografické závazky, ale základní myšlenka zůstává stejná: hlavička musí kompaktním způsobem odevzdat celý obsah bloku.



### Záhlaví bloku



Záhlaví bloku je dlouhé 80 bajtů a obsahuje přesně 6 polí. Právě těchto šest prvků se bude hashovat při vyhledávání proof of work (viz další kapitola):





- Verze (`version`): Tento údaj udává, jaká pravidla nebo signály aktualizace blok dodržuje. Slouží jako mechanismus pro zachování kompatibility a vývoje protokolu.




- Hash předchozího bloku (`previousblockhash`): Toto je hash hlavičky předchozího bloku. To je to, co spojuje bloky dohromady. Bez tohoto pole bychom měli nezávislé bloky. Zahrnutím hashe hlavičky předchozího bloku získáme řetězec, kde každý nový blok navazuje na předchozí.





- Merklův kořen (`merkleroot`): Jedná se o otisk všech transakcí v bloku (prostřednictvím Merklova stromu). Spojuje záhlaví s obsahem: pokud těžař změní výběr nebo pořadí transakcí, změní se i kořen.





- [Časové razítko](https://planb.academy/resources/glossary/timestamp): Jedná se o časové razítko (unixový čas) zvolené těžařem (s omezením platnosti), které musí udávat, kdy byl blok vytěžen. Nemusí být dokonale přesné na sekundu, ale musí splňovat určité podmínky, aby zůstalo pro síť přijatelné.





- Kódovaný [cíl obtížnosti](https://planb.academy/resources/glossary/difficulty-target) (`nbits`): Toto pole kóduje aktuální cíl obtížnosti. Podrobněji se mu budeme věnovat v kapitole o obtížnosti, ale nezapomeňte, že tento parametr je součástí hlavičky.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): Jedná se o hodnotu, kterou může těžař libovolně upravovat. Slouží jako nastavitelná proměnná v průběhu proof-of-work. Její úlohu podrobněji vysvětlím v další kapitole, ale je důležité pochopit, že nonce je součástí hlavičky bloku a je určena k tomu, aby umožnila postupné pokusy.



Pro snazší představu uvádíme příklad záhlaví bloku v hexadecimálním formátu (80 bajtů):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Zde je rozpis podle jednotlivých polí:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Tato hlavička kandidáta na blok sestavená těžařem tvoří základ jeho práce. Při hledání platného bloku proof-of-work se ve smyčce nehešuje přímo celý seznam transakcí, ale spíše tento 80bajtový blok, který obsahuje vše potřebné k propojení bloku s minulostí a k odevzdání jeho obsahu a zároveň obsahuje parametry potřebné pro mechanismus mining, který prozkoumáme v další kapitole.



## Hash, cíl a nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



V předchozích kapitolách jste sledovali cestu transakce Bitcoin: vytvořena a podepsána wallet, předána uzly, uložena v mempoolech a poté potvrzena, když ji těžař zahrne do bloku přijatého sítí. Zatím jsme však neviděli, jak může těžař přidat svůj blok do blockchainu. Jaký proces se skrývá za mining?



Pochopení procesu mining je poměrně jednoduché. Jde o tři pojmy, které jdou ruku v ruce: hashovací funkce, cílová hodnota a proměnná, kterou může těžař upravovat. Podívejme se, jak to všechno funguje.



### Hašovací funkce



Hašovací funkce je nástroj, který přijímá zprávu jako vstup a vytváří výstup pevné velikosti, nazývaný "*fingerprint*" nebo "*hash*".



![Image](assets/fr/010.webp)



Hašovací funkce je v počítačových systémech zajímavá, protože má určité vlastnosti:





- Pokud změníte jediný bit na vstupu, výsledný výstupní hash se zcela nepředvídatelně změní;



![Image](assets/fr/011.webp)





- Není možné přejít z výstupu na vstup: funkce je nevratná;



![Image](assets/fr/012.webp)





- Je nemožné najít dvě různé zprávy, které by poskytovaly přesně stejný hash.



![Image](assets/fr/013.webp)



Hashovací funkce použitá v Bitcoin pro mining je `SHA256`, která se použije dvakrát po sobě. Tato funkce je známá jako dvojitý [SHA256](https://planb.academy/resources/glossary/sha256) nebo `SHA256d`. Právě toto dvojité hašování vytváří otisk bloku.



```text
hash = SHA256(SHA256(message))
```



V našem případě `zpráva` odpovídá záhlaví bloku, které jste viděli v předchozí kapitole. Připomínáme, že záhlaví je malá struktura, která shrnuje vše, co se v bloku nachází.



![Image](assets/fr/014.webp)



### Důkaz práce: nalezení hashe menšího než cílová hodnota



Proof-of-Work je často popisován jako řešení složitého problému. Ve skutečnosti nejde ani tak o problém, jako o hledání metodou pokus-omyl: těžař musí najít takovou verzi hlavičky, jejíž hash (po průchodu hashovací funkcí `SHA256d`) splňuje jednoduchou podmínku: musí být menší než určitý cíl.



Tato podmínka je formulována takto:




- hash záhlaví bloku se vypočítá pomocí hashovací funkce;
- interpretujeme tento hash jako číslo;
- aby byl blok platný, musí být toto číslo menší nebo rovno hodnotě nazvané "*obtížnostní cíl*".



Jinými slovy, blok je platný, pokud:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Cílem je 256bitové číslo. Protože hash vytvořený pomocí `SHA256d` je také 256bitový, lze je porovnat jako dvě čísla. Čím nižší je cíl, tím obtížnější je podmínka, protože pod touto hranicí je méně možných výsledků. Naopak čím vyšší je cílová hodnota, tím snadnější je podmínku splnit a tím snazší je blok vydolovat. Na to, jak se tato cílová hodnota určuje, se blíže podíváme v dalších kapitolách.



V tomto systému je zajímavá hashovací funkce. Uvědomte si, že je snadné vypočítat výstup ze vstupu, ale je nemožné najít vstup, pokud známe pouze výstup funkce. V systému mining nemají těžaři za úkol najít přesný hash, ale spíše najít hash pod cílovou hodnotou. Jediný způsob, jak toho dosáhnout, je provést velmi velký počet pokusů, dokud konkrétní hlavička jejich kandidátského bloku po zaheslování nevytvoří hash menší než tato cílová hodnota.



Jakmile je cílová hodnota dostatečně nízká, stává se tento proces nákladným. Těžař vypočítá hash záhlaví svého kandidátského bloku, zkontroluje výsledek, a pokud podmínka není splněna, upraví záhlaví a výpočet zopakuje. Tato smyčka se opakuje, dokud není nalezena platná hlavička. Když hash záhlaví nakonec splní podmínku, je vytvořen proof of work, blok je považován za platný a může být vysílán v síti Bitcoin, aby jej uzly přidaly do svého blockchainu. Vítězný těžař pak obdrží příslušnou odměnu (její složení si podrobně popíšeme později), zatímco všichni těžaři se okamžitě pustí do hledání nové platné hlavičky pro další blok.



Základní výhoda tohoto mechanismu spočívá v jeho asymetrii. Vytvoření proof of work je pro těžaře nákladné, protože vyžaduje velký počet hashovacích výpočtů. Na druhou stranu pro ověřovatele, tj. síťové uzly, je ověřování velmi jednoduché: stačí, když hashují hlavičku bloku dodanou těžařem, a zkontrolují, zda je výsledný hash skutečně nižší než cílový. Nalezení důkazu tedy vyžaduje mnoho práce a prostředků, zatímco ověření jeho platnosti je rychlé a levné. Právě tato vlastnost definuje efektivní systém proof-of-work.



### Nonce



Zůstává praktická otázka: pokud hlavička kandidáta na blok zkonstruovaná těžařem neposkytuje platný hash, jak to může těžař zkusit znovu? Musí něco v hlavičce upravit, aby získal jiný hash. To je právě úloha nonce.



Pamatujte na první vlastnost hashovací funkce: stačí změnit jediný bit na vstupu, aby vznikl zcela jiný a nepředvídatelný výstupní hash. Každý výpočet hashe se tedy podobá náhodnému losování.



![Image](assets/fr/016.webp)



Aby mohl těžař zkusit své štěstí znovu, nemusí měnit celou hlavičku svého kandidátského bloku: stačí změnit jen její malou část, protože i jediný odlišný bit povede ke zcela novému hashi, který je potenciálně platný, pokud je menší než cílový.



Právě proto hlavička bloku obsahuje nonce. Nonce je 32bitová hodnota, která se použije jednou a poté se nahradí. V praxi může těžař pro stejný kandidátský blok otestovat přibližně 4,29 miliardy možných hodnot (od `0` do `2^32 - 1`). Každá varianta nonce mění záhlaví bloku a v důsledku toho zcela mění hash vytvořený po použití hashovací funkce `SHA256d`.



Proces mining je velmi jednoduchý:




- těžař sestaví kandidátský blok (transakce + hlavička);
- pak vypočítá hash `SHA256d(header)`;
- pokud je výsledek větší než cíl, změní se nonce;
- začíná znovu;
- atd.



![Image](assets/fr/017.webp)



Nonce totiž není jediné pole, které lze upravit. Jakákoli změna v rámci transakcí bloku vede ke změně kořene Merkleho stromu, a tedy ke změně záhlaví tohoto bloku. S moderním výpočetním výkonem lze projít 4,29 miliardy možných hodnot nonce relativně rychle. Proto existuje další pole, obecně označované jako "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", které dále násobí možnosti změny záhlaví. K tomuto mechanismu se podrobněji vrátíme v některé z dalších kapitol.



### K čemu je proof of work?



Nazýváme to "důkaz", protože výsledek je okamžitě ověřitelný: jakmile je blok vytvořen, může kterýkoli uzel během zlomku sekundy zkontrolovat, zda je kryptografický hash jeho hlavičky skutečně nižší než požadovaný cíl. Říkáme tomu "práce", protože dosažení tohoto hashe vyžaduje množství pokusů, a tedy skutečné náklady na výpočet a energii.



V [bílé knize](https://planb.academy/resources/glossary/white-paper) Bitcoin uvádí Satoshi Nakamoto dvě výhody použití systému proof-of-work v Bitcoin:





- Seal o hospodářských dějinách:**



Jakmile je výpočetní zátěž vyčerpána, blok je uzamčen: jeho změna by vyžadovala opětovné provedení proof of work tohoto bloku. A protože jsou bloky zřetězené, změna starého bloku by znamenala také přepočítání všech následujících bloků a následné dohnání a překonání probíhající práce poctivého řetězce.



Jinými slovy, proof-of-work slouží jako páteř systému časových razítek, takže s přibývajícími bloky je falšování minulosti stále nákladnější. Když je vytěžen nový blok, je zabezpečení poskytované proof of work aplikováno současně a rovnoměrně na všechny existující bloky UTXO. S každým přidaným blokem tak každý blok UTXO akumuluje dodatečné množství zabezpečení od Proof-of-Work.





- Definujte pravidlo většiny ([konsenzus](https://planb.academy/resources/glossary/consensus)) a neutralizujte Sybila:**



Proof-of-Work také umožňuje Bitcoin dosáhnout konsensu, aniž by se spoléhal na pravidlo hlasování "jedno ID = jeden hlas", které by mohlo být snadno zfalšováno masivním vytvářením identit (IP, uzlů, klíčů...).



V Bitcoin není "*většina*" největší počet účastníků, ale **řetězec, který nashromáždí nejvíce práce**. Jak uvádí Satoshi, jedná se o princip "jeden procesor = jeden hlas", tj. hlasování vážené skutečným výpočetním výkonem vynaloženým na vytvoření platných bloků. Nasazení tisíců uzlů tedy samo o sobě nepřináší žádnou výhodu oproti Bitcoin. Bez dalšího výpočetního výkonu se již nehromadí žádné důkazy práce a [útok Sybil](https://planb.academy/resources/glossary/sybil-attack) se stává zbytečným, zatímco rozhodovací pravidlo zůstává objektivní a nevyžaduje žádnou identifikaci účastníků.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: Peer-to-Peer Electronic Cash System.*](https://bitcoin.org/bitcoin.pdf)



Zásady týkající se užitečnosti a pravomocí nezletilých jsou velmi složitým tématem, kterému se v tomto kurzu nebudu podrobněji věnovat. K tomuto tématu se však podrobněji vrátíme v budoucích vzdělávacích kurzech MIN 201.



V tuto chvíli lze fungování mining shrnout takto: těžaři vytvoří kandidátský blok s transakcemi čekajícími v mempoolech a poté hledají hash jeho hlavičky (prostřednictvím `SHA256d`), který je menší nebo roven cílové hodnotě. Toho dosáhnou testováním nonces metodou pokus-omyl.



V příští kapitole si uděláme krátkou historickou odbočku k principu proof-of-work, abychom pochopili jeho pozadí, a poté se podíváme na to, jak je systémem určován cíl obtížnosti.



## Historie proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work nebyl vynalezen pro Bitcoin. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) převzal a shromáždil několik starších myšlenek, které již byly zkoumány v různých kontextech.



### Hashcash



Koncem 90. let 20. století se problém nevyžádané elektronické pošty stal významným. Pokud totiž odeslání e-mailu nestojí téměř nic, může spammer odeslat miliony. Pokud však každá zpráva vyžaduje malé výpočetní úsilí, zůstává odeslání jedné legitimní zprávy pro běžného uživatele snadné, zatímco odeslání milionů zpráv se stává velmi nákladným.



To je cílem [Hashcash](https://planb.academy/resources/glossary/hashcash), navrženého Adam Back v roce 1997, který je považován za vynález principu proof-of-work. Princip Hashcash je velmi podobný principu mining: vytvořit hash, který respektuje podmínku (mít na začátku hashe určitý počet nul). Tento důkaz pak doprovází zprávu a příjemce jej může velmi rychle ověřit. Pokud je přijat e-mail, který tento důkaz neobsahuje, může být okamžitě považován za spam, a tedy filtrován. Spammeři jsou pak nuceni vynaložit značné množství energie na rozeslání milionů zpráv, což drasticky snižuje (nebo dokonce zcela likviduje) ziskovost tohoto typu operací, ať už marketingových, nebo podvodných.



V současné době se Hashcash nepoužívá pro e-mail. Filtrování nevyžádané pošty je nyní z velké části založeno na centralizovaných systémech. Výhoda Hashcash oproti současným řešením spočívá v tom, že nevyžaduje centralizované filtrování: každý si může nastavit parametry podle vlastních kritérií. Nevyžaduje ani identifikaci, protože vyhledávání pomocí hashe lze provádět anonymně. Především se nespoléhá na reputační systém, který má tendenci zavádět subjektivní formy filtrování.



Hashcash nebyl o vytváření peněz. Jeho cílem bylo uvalit mezní náklady na snadno automatizovatelnou digitální akci.



![Image](assets/fr/008.webp)



### Bit Gold



Na přelomu 90. let a roku 2000 se Nick Szabo zabýval myšlenkou digitálního nedostatku na základě proof of work. Jeho koncepční projekt nazvaný Bitové zlato předpokládá vytváření hodnotových jednotek řešením nákladné úlohy proof of work a následným zaznamenáváním těchto důkazů do rejstříku za účelem vytvoření určité formy vlastnictví.



Bit Gold nevedl k nasazení systému jako Bitcoin, ale obsahuje několik důležitých poznatků: myšlenku, že výpočet může způsobit nedostatek, a myšlenku časového označování prvků v čase, aby se vytvořila historie, kterou je obtížné přepsat.



### RPOW



V roce 2004 navrhl Hal Finney RPOW (*Reusable Proofs of Work*). Myšlenka spočívala ve vytváření důkazů práce, které by se pak mohly vyměňovat, a nikoli pouze spotřebovávat. Cílem RPOW bylo vytvořit digitální token založené na proof of work se systémem pro ověřování a přenos těchto token bez jejich duplikace. RPOW opět uspokojivě nevyřešil problém zcela decentralizovaného registru, jak to později učinil Bitcoin, ale zůstává jedním z velkých předchůdců Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold a RPOW používají proof-of-work k zavedení nákladů a vytvoření formy nedostatku. Bitcoin tento mechanismus přebírá, ale dává mu ústřední a kolektivní roli: proof-of-work se nepoužívá pouze k vytvoření něčeho, ale také k rozhodnutí, kdo má právo zapsat další stránku registru (další blok), a k tomu, aby bylo nákladné tento registr zfalšovat.



## Úprava cílové hodnoty obtížnosti


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



V předchozích kapitolách jste se seznámili s podstatou proof-of-work: těžaři hashují hlavičku svého kandidátského bloku pomocí `SHA256d` a blok je považován za platný pouze tehdy, pokud je výsledný hash číselně menší nebo roven referenční hodnotě zvané cíl. Otázkou pak zůstává: odkud se tato cílová hodnota bere a jak systém zajišťuje, aby zůstala v čase konzistentní?



Cílem společnosti Bitcoin je dosáhnout průměrné rychlosti nalezení jednoho bloku každých 10 minut. Toto tempo samozřejmě není zaručeno na vteřinu. V praxi se stává, že některé bloky jsou nalezeny několik sekund po nalezení předchozího, zatímco jiné jsou nalezeny až po více než hodině. Důležitý je zde průměr za dostatečně dlouhé období.



![Image](assets/fr/019.webp)



Tato variabilita vyplývá z pravděpodobnostní povahy testu mining: každý pokus je nezávislým pokusem s konstantní pravděpodobností (za předpokladu, že se cílová hodnota nezmění), že výsledek bude nižší než cílová hodnota. Lze ji proto přirovnat k loterii s průběžným losováním: čím více hašů těžaři za sekundu provedou, tím kratší je očekávaná prodleva před vznikem platného bloku, aniž by se však kdykoli odstranila náhodnost od jednoho losování k druhému.



### Proč se snažit o 10 minut mezi bloky?



Ačkoli pro to neexistují žádné důkazy, Satoshi Nakamoto jistě zvolil 10 minut jako praktický kompromis mezi účinností a bezpečností. Kratší interval by zajistil častější potvrzování, ale způsobil by více dočasných rozdělení sítě. Abychom tento bod pochopili, musíme se vrátit ke způsobu šíření bloku.



Když těžař najde platný blok, okamžitě ho rozešle svým kolegům. Uzly, které jej obdrží, zkontrolují jeho platnost (transakce, proof of work, pravidla konsensu atd.) a pak jej postupně předají dál. Toto šíření trvá určitou dobu, která je omezena latencí internetu, šířkou pásma a schopností jednotlivých uzlů blok ověřit.



![Image](assets/fr/020.webp)



Pokud během této difuzní prodlevy objeví platný blok ve stejné výšce i jiný těžař, může dojít k dočasnému rozdělení sítě: jedna část uzlů a těžařů se spoléhá na blok A, zatímco druhá na blok B. Jedná se o dočasné rozdělení sítě.



![Image](assets/fr/021.webp)



Tato rozdělení nejsou katastrofální. Nakamotův konsenzus předpovídá, že v dlouhodobém horizontu převládne pouze jedna větev: ta, která nashromáždí nejvíce práce. Jakmile je totiž například na bloku A vytěžen nový blok, celá síť se resynchronizuje na tuto větev a opustí blok B, který se pak stane "*[stale blokem](https://planb.academy/resources/glossary/stale-block)*", v běžném jazyce někdy chybně nazývaným "*orphan blok*".



![Image](assets/fr/022.webp)



Na druhou stranu mají svou cenu: po několik minut pracuje část horníků na větvi, která bude opuštěna. Tato práce je pak z hlediska celkové bezpečnosti zbytečná, protože nepřispěla k vytvoření konečného řetězce. Čím kratší je interval mezi jednotlivými bloky, tím větší je pravděpodobnost takových rozdělení, protože doba šíření představuje větší část času mezi jednotlivými bloky.



Desetiminutový interval obvykle poskytuje dostatek času na to, aby se vítězný blok rozšířil do širokého okolí, než se najde konkurenční blok ve stejné výšce. Je to kompromis, který omezuje rozdělení, snižuje plýtvání výpočetním výkonem a pomáhá síti zůstat synchronizovaná v globálním měřítku.



### Porozumění hashrate



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" označuje množství výpočtů hash za sekundu, ať už je provede jeden těžař, skupina těžařů nebo všichni těžaři v Bitcoin. Vyjadřuje se v `H/s` (hashe za sekundu) s násobky jako `TH/s` (terahashe za sekundu) nebo `EH/s` (exahashe za sekundu). Představuje počet pokusů, které mohou těžaři každou sekundu provést, aby se pokusili získat hash nižší než cílový.



Pokud cíl zůstane pevný, pak:




- každý pokus má pevně stanovenou pravděpodobnost úspěchu;
- více pokusů za sekundu zvyšuje pravděpodobnost, že se vítězný pokus objeví rychle


Jinými slovy, pokud by zítřejší síť Bitcoin zdvojnásobila svůj výpočetní výkon připojením dvojnásobného počtu strojů mining, bez korekčního mechanismu by byly bloky nalezeny v průměru dvakrát rychleji. Cílová hodnota proto musí být upravena tak, aby kompenzovala odchylky hashrate.



### Úprava cílové hodnoty obtížnosti



Bitcoin řeší tento problém pomocí mechanismu pravidelného přizpůsobování cílů, který upravuje obtížnost mining. Princip je následující: každý uzel přepočítá každých 2016 bloků (přibližně každé 2 týdny) cíl obtížnosti na základě pozorování, kolik času bylo skutečně potřeba k výrobě těchto bloků 2016.



Cílem tohoto mechanismu je zkrátit průměrnou dobu výroby bloku na přibližně 10 minut, přičemž celkový počet hashrate sítě se neustále mění v důsledku odpojování strojů nebo naopak přidávání nových strojů.



![Image](assets/fr/023.webp)



Výpočet vychází z pozorovaného času za uplynulé období:




- pokud byly poslední bloky roku 2016 nalezeny příliš rychle, znamená to, že v tomto období došlo ke zvýšení hashrate; Bitcoin pak ztěžuje podmínku snížením cíle pro další období;
- pokud byly bloky z roku 2016 nalezeny příliš pomalu, znamená to, že se snížila hodnota hashrate; Bitcoin tento stav zmírňuje zvýšením cíle.



Vzorec je následující:



```txt
Tn = To * (Ta / Tt)
```



S:




- `tn`: nový cíl
- `to`: starý cíl
- `Ta`: uplynulý reálný čas za posledních 2016 bloků
- `Tt`: cílový čas (v sekundách)



S cílovou dobou dvou týdnů, tj. `Tt = 1 209 600` sekund:



```txt
Tn = To * (Ta / 1 209 600)
```



Abychom pochopili, jak [upravit obtížnost](https://planb.academy/resources/glossary/difficulty-adjustment) Bitcoin mining, uvádíme příklad s fiktivními hodnotami:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


S:



- `**To = 18,045,755,102**`: Stará cílová hodnota, tj. referenční hodnota před úpravou.
- `**ta = 1 000 000 sekund**`: Čas skutečně strávený výrobou posledních 2016 bloků. Protože je tento čas kratší než cílový čas, síť těžila příliš rychle.
- `**1 209 600 sekund**`: Cílový čas odpovídající 10 minutám na blok pro bloky 2016, který se používá jako referenční hodnota pro úpravu.
- `**tn = 14 918 779 020**`: Nový cíl vypočítaný po úpravě obtížnosti.



Zde je nový cíl nižší než starý, což znamená, že mining se stává těžším, aby se v příštím období zpomalila bloková výroba.


*Cílové hodnoty v tomto příkladu jsou zjednodušené a zmenšené pro účely výuky; skutečný cíl použitý v Bitcoin je 256bitové celé číslo zcela jiného řádu.*



Tento výpočet provádí každý uzel lokálně na základě časových značek zadaných v blocích. Protože všechny uzly použijí stejná pravidla, dojdou ke stejnému výsledku a nový cíl se stane společnou referencí pro další bloky 2016.



U této úpravy je třeba upozornit na jeden důležitý detail: **je omezena**. Bitcoin omezuje změny obtížnosti za období, aby se zabránilo příliš prudkým změnám, které by ji mohly zablokovat. Ve skutečnosti je skutečná doba, která se bere v úvahu, omezena tak, aby zůstala v rozmezí odpovídajícím čtyřnásobku (minimálně jedna čtvrtina starého cíle, maximálně čtyřnásobek starého cíle). Tím se zabrání extrémnímu přehodnocování, pokud jsou časové značky velmi atypické nebo se s nimi manipuluje.



### Cílové zastoupení



V záhlaví bloku se cíl nezobrazuje v plné 256bitové podobě, protože by zabíral příliš mnoho místa. Místo toho 32bitové pole `nBits` kóduje cíl v kompaktním formátu, srovnatelném s vědeckým zápisem o základu 256: exponent (1 bajt) a koeficient (3 bajty). Z těchto dvou hodnot se pak rekonstruuje celý cíl. Nebudeme zde zacházet do podrobností, protože se jedná o poměrně složitou problematiku, která nijak nepřispívá k pochopení mining. Jen si pamatujte, že cíl není v hlavičce bloku uložen v surové podobě, ale v kompaktní podobě.



V této závěrečné kapitole I. části jsme se seznámili s tím, jak funguje proof-of-work v Bitcoin: těžař sestaví kandidátský blok výběrem transakcí ze svého mempoolu, vypočítá hlavičku kandidátského bloku, provede hashování, porovná výsledný hash s cílovou hodnotou periody a pak začne znovu úpravou nonce, dokud nezíská platný hash. Nakonec každých 2016 bloků síť přepočítá nový cíl, aby se udržel průměrný čas kolem 10 minut na blok, a to i přes neustálé změny v hashrate.




# Motivační systém Bitcoin mining


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Jak si dokážete představit, Bitcoin mining není altruistická činnost. Miner mají skutečné náklady: elektřinu na provoz svých mining počítačů, nákup specializovaného vybavení, mzdy na údržbu, někdy i prostory a chladicí systémy. Aby systém Bitcoin fungoval, musí být soukromé zájmy těžařů v souladu s kolektivními zájmy sítě. Přesně takovou úlohu plní odměna mining. Podporuje těžaře, aby investovali do proof of work, zahrnovali platné transakce a respektovali pravidla protokolu, místo aby se jej snažili zkorumpovat.



Tato logika vychází z teorie her: protokol činí poctivost racionální. Těžař vydělává peníze, když vytvoří platný blok, který uzly přijmou. Naopak, pokud se pokusí podvádět, jeho blok bude uzly odmítnut a on nedostane nic. Protože výroba bloku něco stojí, představuje odmítnutý blok přímou ztrátu. V konkurenčním prostředí, kde tisíce hráčů současně hledají platný blok, je proto po většinu času nejvýhodnější strategií striktní dodržování pravidel a poctivé maximalizování příjmů.



Za tímto účelem protokol Bitcoin stanoví, že těžař, který najde platný blok, získává právo na zařazení určité transakce do něj, za což těžař obdrží určitou částku BTC. Tato odměna se nazývá **[odměna za blok](https://planb.academy/resources/glossary/block-reward)**. V této první kapitole této části je cílem pochopit, z čeho se skládá a jak se určuje. Později se podíváme, jak se část tvorby peněz vyvíjí v čase (pomocí haléřů) a jak se vlastně technicky inkasuje (prostřednictvím transakce na coinbase).



### Z čeho se skládá bloková odměna?



V předchozích kapitolách jsme viděli, jak se těžařům daří najít platný blok. Jakmile těžař najde hlavičku, jejíž hash je menší než cílový, je jeho kandidátský blok považován za platný. Může jej pak distribuovat do celé sítě Bitcoin. Blok se přidá ke zbytku blockchainu a potvrdí transakce, které obsahuje.



Právě tato událost (skutečné přidání bloku do blockchainu) je spouštěcím mechanismem pro vyplacení odměny vítěznému těžaři. Tato odměna se skládá ze dvou různých prvků, které se sčítají:




- [bloková dotace](https://planb.academy/resources/glossary/block-subsidy)**;
- transakční poplatky**.



![Image](assets/fr/024.webp)



Podívejme se, čemu tyto dvě části odměny odpovídají.



### Bloková dotace



Bloková dotace odpovídá peněžní části odměny. Když těžař vytvoří platný blok, protokol mu povolí vytvořit určitý počet nových bitcoinů a přidělit si je jako odměnu. Tyto bitcoiny jsou vytvořeny ex nihilo. Předtím neexistovaly.



Množství nově vytvořených bitcoinů však v žádném případě není libovolné. Je striktně definováno pravidly protokolu Bitcoin a je stejné pro všechny těžaře. Na tento mechanismus se blíže podíváme v následující kapitole, protože dotace nemá neomezeně pevnou hodnotu: je pravidelně rozdělována podle přesného harmonogramu. Prozatím si to jen zapamatujte:




- bloková dotace je jednou ze dvou složek blokové odměny;
- je omezena a určena protokolem, nikoli těžařem (i když těžař může technicky požadovat méně než maximální částku);
- vytváří bitcoiny ze vzduchu.



Tato dotace hraje v rámci protokolu Bitcoin dvě hlavní role. První je povzbudit hráče k účasti na mining. V prvních letech Bitcoin (a někdy i dnes) byly transakční poplatky velmi nízké. Dotace proto zaručila dostatečnou kompenzaci, která přilákala těžaře a zachovala určitou úroveň bezpečnosti systému.



Druhá role se týká distribuce měny. Každá nová měna stojí před otázkou, jak spravedlivě rozdělit peněžní jednotky mezi obyvatelstvo. Bloková dotace poskytuje odpověď na tento problém. Vytvořením bitcoinů prostřednictvím mining umožňuje jejich počáteční distribuci otevřeným a neutrálním způsobem: kdokoli je může získat, pokud se účastní mining, bez nutnosti předchozí autorizace nebo identifikace.



Na druhou stranu, protože tyto bitcoiny vznikají z ničeho, jejich hodnota není bez základu. Tím, že dotace zvyšuje množství peněz v oběhu, mechanicky rozmělňuje hodnotu stávajících bitcoinů. Zavádí tedy určitou formu měnové inflace. V následující kapitole však uvidíme, že tato dotace je předurčena k postupnému zániku a že inflace nakonec ustane.



![Image](assets/fr/025.webp)



### Transakční poplatky



Druhá složka blokové odměny je spojena s používáním systému: když uživatel zveřejní transakci, chce, aby byla potvrzena. Prostor pro bloky je však omezený a bloky se objevují v průměru jen přibližně každých 10 minut. Blokový prostor je tedy vzácný zdroj. Když poptávka převyšuje nabídku, cena roste: to je trh s transakčními poplatky. Každý těžař, kterému se podaří vytvořit platný blok, získává právo inkasovat na svůj účet plnou výši transakčních poplatků spojených se všemi transakcemi, které do svého bloku zahrnul.



Můžete si to představit jako aukční systém: každá transakce navrhuje výši poplatku a těžaři upřednostňují ty, které maximalizují jejich příjem, a to při omezeném prostoru. Tento mechanismus přirozeně vyrovnává zájmy:




- spěchající uživatelé zaplatí více, aby byli rychle zařazeni;
- těžaři jsou vyzýváni, aby zahrnuli transakce, které platí nejvyšší poplatky za blokový prostor.
- síť se vyhýbá spamu, protože zveřejnění transakce něco stojí.



#### Jak se vypočítávají transakční poplatky?



Navzdory všeobecnému přesvědčení nejsou poplatky výstupem transakce Bitcoin. Ve skutečnosti transakce vynakládá vstupy a vytváří výstupy. Vstupy představují zdroj použitých bitcoinů, zatímco výstupy představují cíl plateb. Transakční poplatky jsou jednoduše **rozdíl mezi celkovými vstupy a celkovými výstupy**.



Jinými slovy, vstupy bitcoinů, které patří uživateli, vytvářejí výstupy pro příjemce, ale nereprodukují celou částku spotřebovanou vstupy. Rozdíl mezi nimi představuje transakční poplatky, které může těžař inkasovat.



Uveďme si příklad. Transakce spotřebuje dva vstupy, jeden ve výši `100 000 sats` a druhý ve výši `150 000 sats`, a vytvoří tři výstupy ve výši `35 000 sats`, `42 000 sats` a `170 000 sats`.



![Image](assets/fr/027.webp)



Součet vstupů je tedy `250 000 sats`, zatímco součet výstupů je `247 000 sats`. To znamená, že na vstupech bylo spotřebováno 3 000 sats`, aniž by byly znovu vytvořeny na výstupech: tato částka odpovídá poplatkům navrhovaným touto transakcí.



![Image](assets/fr/028.webp)



Pokud těžař zahrne tuto transakci do platného bloku, bude mít nárok na vrácení těchto 3 000 sats`, navíc k poplatkům za všechny ostatní transakce zahrnuté do bloku. Neexistuje však žádná přímá vazba mezi transakcí, která platí poplatek on-chain, a částkou sats, kterou těžař skutečně inkasuje. Technicky vzato jsou poplatky ve výši `3 000 sats` zničeny a těžař na oplátku získává právo znovu získat stejnou částku pro sebe.



#### Poměr poplatků



Blok není omezen počtem transakcí, ale svou celkovou kapacitou (dnes v praxi váhou bloku). Některé transakce zabírají více místa než jiné: transakce s mnoha vstupy a výstupy bude větší než jednoduchá transakce s jedním vstupem a dvěma výstupy. Velikost ovlivní také použité skripty.



![Image](assets/fr/026.webp)



Dvě transakce tedy mohou platit stejnou výši poplatků v absolutním vyjádření, ale z pohledu těžaře nejsou ekonomicky rovnocenné. Pokud je jedna z nich dvakrát větší, stojí dvakrát více místa v bloku. Místa je málo, takže těžař se snaží maximalizovat svůj příjem na jednotku místa.



Proto v praxi vyjadřujeme konkurenceschopnost transakce pomocí poměru poplatků, obvykle v `sats/vB` ([satoshi](https://planb.academy/resources/glossary/satoshi-sat) za virtuální bajt). Výpočet tohoto poměru je jednoduchý:



```text
fee rate = fee / weight (in vB)
```



Například pokud máme transakci, která váží `141 vB` a na poplatcích je alokováno `1 974 sats`, bude sazba poplatků `14 sats/vB`.



```text
1 974 / 141 ≈ 14 sats/vB
```



Tento poměr vysvětluje ekonomická rozhodnutí těžařů: při pevné kapacitě maximalizuje zařazení transakcí s vysokou sazbou celkové poplatky za blok, a tedy i odměnu těžaře. Vysvětluje také, proč nízkonákladové transakce zůstávají dlouho ve frontě v mempoolech: konkurují ostatním transakcím, které za jednotku prostoru platí více.



### Ochrana sítě proti spamu



Poplatky slouží také k provozně bezpečnostním účelům: zavádějí náklady na multiplikaci transakcí. Pokud by zveřejnění transakce bylo zdarma, bylo by snadné zaplavit síť zbytečnými transakcemi a nasytit mempooly, což by zvýšilo zatížení uzlů.



V praxi uzly používají místní zásady předávání (pravidla mempoolu) a často nastavují minimální prahovou hodnotu poplatku, pod kterou transakci nepředají (ve výchozím nastavení `0,1 sat/vB` v jádře Bitcoin prostřednictvím `minRelayTxFee`). Transakce může být platná v přísném smyslu pravidel konsensu, ale většina uzlů ji nepředá, pokud jsou její poplatky příliš nízké. V důsledku toho neobíhá, nedostane se k těžařům a má jen malou šanci na potvrzení.



V tuto chvíli jste pochopili podstatu blokové odměny: odpovídá kompenzaci pro vítězného těžaře a skládá se ze dvou různých prvků. Na jedné straně je to bloková dotace definovaná pravidly protokolu, která vytváří nové bitcoiny ex nihilo. A na druhé straně poplatky za transakce zahrnuté do vytěženého bloku.



V příští kapitole se podrobněji zaměříme na blokovou dotaci, abychom přesně pochopili, jak se vypočítává a jak se vyvíjí v čase podle pravidel protokolu Bitcoin.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



V předchozí kapitole jsme viděli, že těžaři, kteří vytvoří platný blok, obdrží odměnu, která se skládá z poplatků za transakce zahrnuté v bloku a z blokové dotace. Zatím jsme však nevysvětlili, jak se výše této dotace určuje. Mechanismus, který tuto hodnotu stanovuje a vyvíjí, je známý jako ***[halving](https://planb.academy/resources/glossary/halving)***.



### Co je to půlení?



Halving je událost naprogramovaná v protokolu Bitcoin, která snižuje dotaci bloku na polovinu, tj. maximální množství nových bitcoinů, které může vítězný těžař vytvořit v každém bloku. Nemá vliv na transakční poplatky: poplatky existují nezávisle a zůstávají určeny aktivitou uživatelů a soutěží o místo v bloku.



Když byla v roce 2009 zahájena těžba bloku Bitcoin, byla stanovena dotace na 50 BTC za každý vytěžený blok. Od té doby byla tato dotace při každém půlení několikrát snížena na polovinu.



![Image](assets/fr/029.webp)



Halving se nespustí podle data, ale podle výšky bloku. Provádí se **každých 210 000 bloků**. Vzhledem k tomu, že Bitcoin se zaměřuje na průměrný interval přibližně 10 minut na blok, odpovídá 210 000 bloků zhruba čtyřem letům.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Pokud si tedy uvědomíme, že `n` je počet již proběhlých půlení, lze blokovou dotaci v BTC vypočítat následovně:



```text
subsidy(n) = 50 / 2^n
```



### Minulé půlení



Zde je souhrnná tabulka již proběhlých půlení s výškou bloku, datem a novou blokovou dotací platnou po události:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Kdy a jak dotace skončí?



Halving se opakuje, pokud lze dotaci vyjádřit v minimální jednotce systému: satoshi.



```text
1 BTC = 100 000 000 sats
```



Se snižováním dotace na polovinu se nakonec dostaneme na tak malé zlomky bitcoinu, že budou menší než 1 satoshi. V tomto okamžiku již není možné vytvořit polovinu jednotky satoshi. Tvorba peněz prostřednictvím blokové dotace se zastaví a těžaři jsou odměňováni pouze na základě transakčních poplatků. Od tohoto okamžiku budou všechny bitcoiny v oběhu a nebude již možné vyrábět nové jednotky.



Definitivní konec blokových dotací nastane na úrovni bloku 6 930 000, tj. při 33. a posledním půlení. Očekává se, že k této události dojde kolem roku 2140, i když přesné datum nelze určit, protože bude záviset na skutečné rychlosti, jakou budou bloky do té doby nalezeny.



Protože bloková dotace se řídí geometrickou posloupností s poměrem 1/2 při každém půlení, byla tvorba peněz v počátcích Bitcoin extrémně vysoká a poté velmi rychle klesala. Při sedmém půlení již bude do oběhu uvedeno více než 99 % bitcoinů. Očekává se, že hranice 99 % bude překročena mezi lety 2032 a 2036. To znamená, že pak bude trvat více než 100 let, než se vytěží poslední zbývající 1 % bitcoinů. Zatímco v době spuštění Bitcoin byla měnová inflace velmi vysoká, aby umožnila širokou distribuci měny, nyní je velmi nízká a bude dále klesat, dokud nedosáhne úrovně skutečné tvrdé měny, jejíž nabídka v oběhu se již nemůže zvyšovat.



![Image](assets/fr/030.webp)



### Proč nikdy nebude 21 milionů BTC?



Maximální peněžní zásoba Bitcoin je často uváděna jako 21 milionů BTC. To je dobrá aproximace pro pochopení jeho měnové politiky, ale z čistě technického hlediska celková nabídka nikdy ve skutečnosti nedosáhne přesně 21 000 000 bitcoinů.



Hlavní důvod je mechanický. Postupnými půleními bloková dotace nakonec klesne pod minimální hodnotu 1 sat, čímž se ukončí vydávání před dosažením přesné teoretické celkové hodnoty. V důsledku této minimální granularity a pravidel zaokrouhlování je celkový počet bitcoinů vytvořených dotací o něco nižší než 21 milionů.



Kromě toho se k tomu mohou přidat i okrajové odchylky související s protokolem. Ve vzácných případech se například může stát, že někteří těžaři nepožádají o plnou dotaci, což definitivně sníží množství skutečně vydaných bitcoinů. Můžeme také zmínit [blok genesis](https://planb.academy/resources/glossary/genesis-block), vytvořený 3. ledna 2009 Satoshi, jehož vytvořené bitcoiny nejsou součástí [UTXO set](https://planb.academy/resources/glossary/utxo-set), a také některé historické události spojené s chybami, jako jsou duplicitní identifikátory transakcí coinbase.



Nakonec musíme vzít v úvahu také všechny bitcoiny, které byly zničeny nebo zablokovány:




- bitcoiny uzamčené v neřešitelných skriptech;
- ty, které byly záměrně zničeny skripty `OP_RETURN`;
- nebo ztrátě soukromých klíčů na úrovni aplikace.



Teoreticky je tedy zásoba Bitcoin omezena na 21 milionů. V praxi však nikdy nebude v oběhu 21 milionů bitcoinů.



## Transakce na platformě coinbase


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



V předchozích kapitolách jsme uvedli dva důležité body. Za prvé, těžař, kterému se podaří vytvořit a distribuovat platný blok, obdrží odměnu. Na druhé straně jsme viděli, že tato odměna se skládá ze dvou různých prvků:




- bloková dotace (bitcoiny vytvořené ex nihilo, jejichž maximální výše je stanovena protokolem a postupně se snižuje prostřednictvím halvings);
- všechny transakční poplatky zaplacené uživateli, jejichž transakce byly do bloku zahrnuty.



Zůstává však jedna otázka: jakým mechanismem těžař tuto odměnu v Bitcoin získává? Právě to je úlohou konkrétní transakce zvané "coinbase".



### Jak funguje transakce na platformě coinbase



Jak jsme viděli v první části kurzu, každý blok Bitcoin obsahuje seznam čekajících transakcí, které bude potvrzovat. Úplně první z nich je vždy [transakce na coinbase](https://planb.academy/resources/glossary/coinbase-transaction). Díky ní může vítězný těžař obdržet svou odměnu.



![Image](assets/fr/031.webp)



Na první pohled vypadá jako klasická transakce Bitcoin: má [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), výstupy a je zahrnuta do Merkleova stromu bloku. Liší se však v jednom důležitém ohledu: nevynakládá žádné existující prostředky UTXO.



V klasické transakci Bitcoin odkazují `vstupy` na předchozí nevyužité výstupy (UTXO), které poskytují vstupní hodnotu. Výstupy pak tuto hodnotu přerozdělují novým UTXO s novými podmínkami čerpání. Jinými slovy, abyste mohli bitcoiny odeslat, musíte je již vlastnit. Naproti tomu transakce na coinbase nespotřebovává žádné bitcoiny na vstupu: vytváří bitcoiny na výstupu přímo z nuly.



Právě tento mechanismus umožňuje, aby se prostřednictvím blokové dotace dostávaly do oběhu nové bitcoiny, a těžařům připisuje poplatky spojené s transakcemi zahrnutými do bloku. Transakce na coinbase nemůže odkazovat na skutečně existující UTXO (ve skutečnosti odkazuje na fiktivní UTXO), protože její úlohou je právě vytvořit část hodnoty (dotaci) a získat zpět druhou část (poplatky), aniž by je obdržela z předchozí transakce. Aby celý systém zůstal konzistentní, musí se část odpovídající poplatkům přesně rovnat součtu bitcoinů spotřebovaných na vstupu, ale nevytvořených znovu na výstupu v ostatních transakcích bloku.



![Image](assets/fr/032.webp)



Tato transakce není volitelná. Blok, který neobsahuje transakci coinbase, je neplatný a síťové uzly jej systematicky odmítají.



⚠️ Upozornění: termín "*coinbase*" nemá žádnou souvislost se stejnojmennou směnárenskou platformou. V Bitcoin se výraz "*coinbase*" historicky vztahuje k transakci, která vytváří blokovou odměnu. Společnost tento termín jednoduše převzala do svého názvu.



Transakce coinbase ve skutečnosti plní několik rolí současně:




- První z nich je ten, který jsme si právě podrobně popsali: těžaři se přiřadí odměna, na kterou má nárok za vytvoření platného bloku.
- Jeho druhou, spíše technickou úlohou je ukotvení kryptografického závazku ke svědkům (podpisům) transakcí SegWit zahrnutých do bloku.
- Třetí úloha, tentokrát nesouvisející přímo s protokolem, ale související s moderní industrializací mining, spočívá v tom, že coinbase se nyní často používá k ukotvení libovolných technických údajů. Tato data jsou zpravidla spojena s provozem poolů mining a jejich vnitřní organizací.



Abychom vám pomohli pochopit tato různá použití, podíváme se nyní blíže na strukturu transakce na coinbase.



### Základní struktura transakce coinbase



Transakce coinbase musí obsahovat přesně jeden vstup. Pro zjednodušení někdy říkáme, že nemá žádný vstup, protože tento vstup nevydává žádné skutečné UTXO. Ve skutečnosti existuje vstup s odkazovaným zdrojem, ale ten záměrně ukazuje na neexistující UTXO.



Jak jsme již viděli, každá transakce Bitcoin musí jako vstup spotřebovat UTXO, aby mohla vytvořit platné výstupy. V transakci Bitcoin má tato spotřeba podobu odkazu na existující UTXO jako vstup. Toto odkazování se provádí jednoduše uvedením identifikátoru předchozí transakce (té, v níž byl UTXO vytvořen), jakož i jeho indexu mezi výstupy této transakce. Konkrétně je UTXO definován pomocí hashe (předchozí TXID) a indexu.



Ale v případě transakce na coinbase musí vstup místo odkazu na skutečný existující UTXO nutně ukazovat na tento konkrétní falešný UTXO s TXID plným nul, který neodpovídá žádnému skutečnému TXID:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Přímo následuje falešný index:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



V základním protokolu Bitcoin, jak je popsán v Satoshi Nakamoto, je tento falešný vstup jediným omezením uloženým transakci s coinbase.



Stejně jako jakýkoli jiný kód UTXO, na který se odkazuje na vstupu transakce, je spojen s polem `scriptSig`. V běžné transakci obsahuje toto pole `scriptSig` prvky potřebné ke splnění `scriptPubKey`, a tím k odemčení použitého UTXO. Ale v konkrétním případě coinbase, protože odkazovaný UTXO je záměrně fiktivní, je pole `scriptSig` zcela volné. Uživatelé Miner tedy mohou zadat libovolné údaje. Později se podíváme na to, jak je tato volnost využívána.


Kromě tohoto falešného vstupu existuje jeden nebo více naprosto standardních výstupů, které těžaři umožňují získat bitcoiny z odměny na jedné z jeho adres Bitcoin. Tyto výstupy jsou UTXO uzamčené pomocí `scriptPubKey` (např. skript ukazující na adresu ovládanou těžařem nebo poolem). Jediná zvláštnost zde spočívá v pravidle pro výpočet jejich hodnoty: celkový součet výstupů coinbase nesmí nikdy překročit maximální povolenou dotaci, ke které se přičítají poplatky za bloky.



Historicky se tedy transakce na coinbase omezuje na toto jednoduché schéma: falešný vstup odkazující na neexistující UTXO a jeden nebo více výstupů určených k rozdělení blokové odměny vítěznému těžaři. Dnes se však coinbase na tuto distribuční roli již neomezuje. Její zvláštní postavení v bloku a velká flexibilita její struktury vedly k novým způsobům využití, a to jak v samotném protokolu, tak v mechanismech správy poolu mining.



### Další použití coinbase



Postupem času se transakce na coinbase stala obzvláště vhodným místem pro integraci různých informací užitečných pro mining a pro samotnou strukturu bloku. Podívejme se na ně, abychom lépe pochopili celkovou organizaci coinbase.



#### BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) je [soft fork](https://planb.academy/resources/glossary/soft-fork) nasazený v březnu 2013, počínaje blokem 227 930, který představil druhou verzi bloků Bitcoin. Tato nová verze vyžaduje, aby každý blok obsahoval v `scriptSig` transakce coinbase výšku vytvářeného bloku.



Na jedné straně tento vývoj objasňuje způsob, jakým se síť dohodne na vývoji struktury bloků a pravidel konsensu. Na druhé straně zajišťuje jedinečnost každého bloku a transakce v coinbase.



Proto není `scriptSig` od coinbase zcela zdarma. Od aktivace BIP-34 je jednoduše omezena na začátek výšky bloku, ve kterém je tato transakce coinbase zahrnuta.



![Image](assets/fr/035.webp)



#### Extra-nonce



Jak jsme viděli v prvních kapitolách tohoto kurzu, těžař má v záhlaví bloku 32bitové pole nonce, které upravuje metodou pokus-omyl tak, aby našel hash menší nebo roven cílové hodnotě. Tento 32bitový prostor již umožňuje prozkoumat velmi velké množství kombinací, ale při vysoké obtížnosti mining může být tento rozsah zcela vyčerpán v relativně krátkém čase, a proto nemusí přinést žádnou kombinaci, která by vytvořila platný hash. Pokud byly bez úspěchu vyzkoušeny všechny možné hodnoty `nonce`, musí těžař upravit další prvek, aby změnil hlavičku bloku, a zahájit novou sérii pokusů.



Protože transakce coinbase nabízí volné pole prostřednictvím `scriptSig` svého vstupu, řešením pro rozšíření prostoru nonce je využití části tohoto `scriptSig`. To se obecně označuje jako extra-nonce. Modifikací extra-nonce těžař modifikuje `scriptSig` coinbase, tj. identifikátor transakce, dále Merkleho kořen bloku a nakonec samotnou hlavičku bloku. Tímto způsobem získá nový prohledávaný prostor hashů, který může prozkoumat, aniž by musel upravovat ostatní součásti svého kandidátského bloku.



![Image](assets/fr/036.webp)



#### Identifikace poolů a těžařů



V současné době je velmi velká část světových zásob hashrate organizována v bazénech mining. Tyto struktury sdružují jednotlivé těžaře, aby spojili svou práci a snížili rozptyl svých příjmů.



Z provozních důvodů využívají pooly mining také volné pole `scriptSig` vstupu coinbase k vkládání různých informací. Ty se liší pool od poolu a síťový protokol od síťového protokolu, ale obecně zahrnují jedinečný identifikátor (často dodatečnou nonce strukturovanou do několika dílčích částí) přidělený každému těžaři, aby se zabránilo duplicitě práce v rámci poolu. Obvykle se přidává identifikační značka poolu, která se používá pro veřejné přiřazení nalezených bloků, statistiky mining a další účely sledování.



![Image](assets/fr/037.webp)



#### Závazek společnosti SegWit



Od roku 2017, kdy byl povolen soft SegWit, byly údaje o svědcích (tj. obecně podpisy) odděleny od kmenových údajů transakcí, a to zejména z důvodu odstranění problému s [chybovostí transakcí Bitcoin](https://planb.academy/resources/glossary/malleability-transaction). Toto oddělení tedy zavádí nový prvek, který má být v bloku odevzdán.



Za tímto účelem jsou svědci seskupeni do dalšího vyhrazeného Merkleho stromu, jehož kořen je poté odevzdán do transakce coinbase prostřednictvím výstupu `OP_RETURN`.



![Image](assets/fr/038.webp)



V tomto kurzu se nebudu tomuto mechanismu věnovat podrobněji, protože to přesahuje rámec tohoto článku, ale stačí si uvědomit, že od zavedení SegWit slouží transakce coinbase jako prostředek, který v bloku ukotvuje otisk shrnující všechny svědky SegWit. Svědci jsou umístěni do nezávislého Merkleho stromu, kořen tohoto stromu je zapsán do výstupu transakce coinbase a tato transakce coinbase je sama zahrnuta do hlavního Merkleho stromu spolu se všemi ostatními transakcemi, jejichž kořen se objevuje v záhlaví bloku. Takto jsou svědci, uložení odděleně od hlavních dat transakce, stále odevzdáváni do záhlaví bloku.



![Image](assets/fr/039.webp)



#### Libovolné zprávy



Protože `scriptSig` umožňuje volné vložení libovolných informací, které si těžař zvolí, někteří využili příležitosti a přidali do něj spíše zprávy osobního než technického charakteru. Nejznámějším případem je samozřejmě Satoshi Nakamoto s jeho dnes již kultovním vzkazem:



> The Times 03/leden/2009 Kancléřka na pokraji druhé finanční pomoci bankám

Tato zpráva, která se nachází v bloku Genesis (úplně první blok bloku Bitcoin), je ve skutečnosti zakódována v hexadecimálním tvaru v `scriptSig` transakce coinbase:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Doba splatnosti


Jakmile je blok vytěžen a distribuován, objeví se transakce coinbase v blockchainu jako jakákoli jiná transakce. Pro vítězného těžaře vytvoří UTXO, což mu umožní vyzvednout si odměnu. Tyto UTXO však není možné okamžitě utratit: podléhají [době splatnosti](https://planb.academy/resources/glossary/maturity-period). Tato splatnost je stanovena na 100 bloků po bloku obsahujícím coinbase. Konkrétně tedy transakce coinbase musí mít celkem 101 potvrzení, aby se její výstupy staly pro vítězného těžaře utratitelnými.


![Image](assets/fr/040.webp)


Cílem tohoto pravidla je omezit dopad reorganizací řetězců na ekonomiku. Jak jsme viděli v předchozích kapitolách, může se stát, že ve stejné výšce jsou téměř současně nalezeny dva různé platné bloky různými těžaři. Na krátký okamžik může dojít k rozdělení sítě: některé uzly obdrží nejdříve blok A, zatímco jiné uvidí nejdříve blok B. Pak v průběhu dalších bloků jedna z těchto dvou větví nahromadí více práce a stane se referenční větví. Druhá větev je opuštěna a její bloky se stanou zastaralými. Transakce, které obsahovala, se pak teoreticky mohou vrátit do mempoolů a čekat na potvrzení.



V praxi k tomu dochází jen zřídka, protože trh s poplatky často vede k tomu, že se téměř stejné transakce objevují ve dvou konkurenčních blocích ve stejné výšce. To je jeden z důvodů, proč se transakce Bitcoin běžně považuje za neměnnou po šesti potvrzeních: reorganizace více než šesti bloků je tak nepravděpodobná, že ji lze rozumně považovat za nemožnou.



![Image](assets/fr/041.webp)



Problémem těchto reorganizací v případě transakce s coinbase je, že se nejedná o běžnou transakci. Uvádí do oběhu zcela nové bitcoiny. Pokud by bylo možné odměnu za blok okamžitě utratit, mohla by vzniknout problematická kaskádová situace:




- těžař utrácí bitcoiny z coinbase,
- tyto bitcoiny obíhají v ekonomice,
- pak byl původní blok při reorganizaci definitivně opuštěn.



Bitcoiny v oběhu by pak v konečném řetězci nikdy neexistovaly a řada transakcí, které byly platné v době emise, by se stala neplatnou a posteriori.



Doba splatnosti ukládá dostatečně dlouhý časový rámec, aby tento scénář nebyl reálný. Reorganizace 101 bloků se v praxi považuje za nemožnou (i když zůstává nekonečně malá pravděpodobnost). Nevíme přesně, proč Satoshi zvolil tak vysokou hodnotu doby splatnosti, ale je pravděpodobné, že byla zvolena tak, aby mechanismus zůstal funkční i v případě velkých poruch sítě.



Toto pravidlo zabraňuje tomu, aby nově vytvořené peníze s blokovou odměnou začaly obíhat dříve, než bude blok, který je generated, bezpečně pohřben pod velkým množstvím nahromaděné práce.



---

Nyní jsme se dostali na konec našeho vysvětlení, jak funguje Bitcoin mining. Nyní byste měli mít jasnou představu o základních mechanismech.



V poslední části kurzu se vrátíme ke konkrétnějším aspektům, abychom vám ukázali, jak se Bitcoin mining zhmotňuje v reálném světě: jeho industrializace, používané stroje, seskupení hráčů atd. Cílem bude poskytnout vám celkový pohled na Bitcoin mining, a to jak z teoretického a protokolárního hlediska, které jsme právě viděli, tak i z jeho praktické a provozní stránky.



# Průmysl Bitcoin mining


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## Vývoj strojů mining


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



V počátcích Bitcoin nebyla mining průmyslovou činností. Byla součástí softwaru Bitcoin, spuštěna na osobním počítači, často ze zvědavosti, někdy za účelem podpory sítě a druhotně za účelem získání bitcoinů, které tehdy neměly prakticky žádnou tržní hodnotu.



V průběhu let prošla tato činnost proměnou: stroje se změnily, obtížnost vzrostla a z mining se stalo samostatné odvětví. Podívejme se na provozní aspekty hry Bitcoin mining.



### Začínáme: mining s procesorem



V roce 2009 a v prvních letech byl mining prováděn převážně pomocí procesoru běžného počítače. Bitcoin byl tehdy jen jednoduchý software, který sloužil jako wallet, uzel a těžař. K účasti na procesu mining a v mnoha případech i k nalezení bloků stačilo pouhé spuštění softwaru Satoshi Nakamoto na osobním počítači.



Procesor umí všechno, ale není na nic optimalizovaný. Provádí velmi obecné instrukce se složitou logikou. Pro úlohy, jako je opakované hashování hlaviček bloků, není ideálním nástrojem, ale při spuštění sítě je náročnost tak nízká, že k nalezení bloků bohatě stačí.



Toto období je důležité, protože nám připomíná důležitou věc: proof of work nezávisí na konkrétní kategorii zařízení. Důležitá je schopnost počítat hashe rychleji než ostatní, a to při daných nákladech. Jakmile se objeví technická výhoda, automaticky se promění v ekonomickou výhodu. V absolutních číslech je však i dnes možné pokusit se najít bloky Bitcoin pomocí běžného procesoru. Takový přístup zvolil například projekt NerdMiner. Šance na nalezení bloku je prakticky nulová, ale stále existuje nekonečně malá pravděpodobnost.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Přechod na GPU



Brzy si těžaři uvědomili, že úzkým hrdlem není výkon, ale schopnost provádět paralelně obrovské množství podobných operací. Právě to dokázaly grafické procesory (GPU). Původně byly GPU navrženy tak, aby prováděly stejné operace s velkým množstvím dat. Tato architektura se dokonale hodila pro úlohy, jako je opakované hashování: místo několika vysoce univerzálních jader máte stovky, později tisíce jednotek schopných provádět stejné instrukce současně.



Při srovnatelné spotřebě energie dokáže GPU vytvořit mnohem více hashů za sekundu než CPU. Ve stejné době měl bitcoin směnný kurz vůči dolaru, jeho hodnota rostla a objevovaly se směnné platformy. Od té doby se začal měnit charakter mining. Už nešlo jen o účast, ale o vydělávání peněz. Objevily se specializované konfigurace: stroje postavené kolem několika grafických karet, někdy bez obrazovek, s minimálním systémem a specializovaným softwarem, jejichž jediným účelem bylo těžit.



Právě v tomto okamžiku začaly obtíže s mining explodovat. Od poloviny roku 2010 do poloviny roku 2011 se dokonce zvýšila tisícinásobně. Mechanicky začíná specializace, stejně jako u raných forem industrializace, a běžní uživatelé - kteří se spokojí se spuštěním softwaru Bitcoin na svých osobních počítačích - mají nyní jen velmi malou šanci najít platný blok.



![Image](assets/fr/044.webp)



*Zdroj: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Mezi érou GPU a moderní érou [ASIC](https://planb.academy/resources/glossary/asic) nastala přechodná fáze: používání FPGA. FPGA je přeprogramovatelná součástka: lze ji nakonfigurovat tak, aby přímo implementovala logický obvod určený pro konkrétní výpočet, v tomto případě `SHA256d`. Záměrem bylo ještě více se vzdálit od hardwaru pro všeobecné použití (CPU/GPU) a získat tak větší energetickou účinnost. Brzy by se však vylepšení provedená virtuálně na FPGA uplatnila i fyzicky na samotných čipech: to je příchod ASIC.



### Příchod ASIC



Závěrečnou etapou specializace hardwaru mining byl vznik ASIC (*Aplication-Specific Integrated Circuits*). ASIC je čip určený pro jednu úlohu. V případě Bitcoin mining je tímto úkolem právě provádění `SHA256d` maximální rychlostí a s optimální energetickou účinností. Na rozdíl od GPU se ASIC nepoužívá k provozování her, 3D vykreslování nebo umělé inteligence. Slouží k hašování, a to je vše.



![Image](assets/fr/045.webp)



*ASIC S21 XP vyrobený společností Bitmain*



Tato specializace má dva hlavní důsledky:




- Prvním z nich je skok ve výkonu a efektivitě. U zařízení srovnatelné generace produkuje ASIC mnohem více hashů za sekundu než GPU, přičemž spotřebovává méně energie. Mining s GPU se rychle stal nekonkurenceschopným: i když technicky fungoval, náklady na elektrickou energii ve většině souvislostí daleko převyšovaly očekávaný výnos;
- Druhým důvodem je změna modelu: investice se přesunuly především do hardwaru průmyslové třídy. Mining nyní zahrnuje nákup strojů určených k tomuto účelu, jejich nepřetržité napájení, chlazení, údržbu a absorbování jejich zastarávání. Protože ASIC není ekonomicky věčný: když na trh přijde nová, účinnější generace, staré stroje se postupně stávají méně rentabilními, i když zůstávají funkční.



Od tohoto okamžiku už nemluvíme jen o koníčku. Mluvíme o odvětví, kde konkurenceschopnost závisí na rovnici:




- náklady na elektřinu;
- náklady na vybavení a odpisy;
- schopnost chlazení a provozu ve velkém měřítku;
- dostupnost a spolehlivost stroje;
- rychlost komunikace;
- atd.



### Zemědělské podniky Mining



Izolovaný stroj může těžit, ale seskupením stovek, později tisíců strojů ASIC na jednom místě sdílíme fixní náklady, optimalizujeme logistiku a přibližujeme se modelu specializovaného datového centra.



[Farma mining](https://planb.academy/resources/glossary/mining-farm) je ve své nejjednodušší podobě budova (nebo sada kontejnerů) naplněná jednotkami ASIC, které jsou v provozu 24 hodin denně, 7 dní v týdnu. Nyní je úkolem udržet stabilní provozní podmínky:




- dodávat velké množství levné a stabilní elektrické energie;
- řídit teplo, aby se zabránilo škrcení, protože hustota energie je značná;
- filtrovat prach, kontrolovat vlhkost, čistit;
- sledování výkonu stroje v reálném čase (teploty, chyby hardwaru, poklesy hashrate atd.).



![Image](assets/fr/043.webp)



*Jedna ze sedmi budov určených pro Bitcoin mining v areálu Rockdale společnosti Riot Platforms nedaleko Austinu v Texasu. Tato je speciálně věnována imerzi mining*



Mining je nyní poháněn průmyslovými subjekty, z nichž některé jsou kótovány na burze, které budují a provozují velmi rozsáhlé farmy. Patří mezi ně společnosti MARA Holdings (Nasdaq: `MARA`) a Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



I když se nebudeme zabývat podrobnostmi modelů ziskovosti, je důležité pochopit, proč mining nabyl právě této podoby. Proof-of-work je konkurenční mechanismus: pravděpodobnost nalezení bloku, a tedy vydělání peněz, je úměrná podílu hashrate, který nasadíte. V důsledku toho existuje neustálý tlak na zvyšování výpočetního výkonu, snižování nákladů na jednotku výpočtu a omezování ztrát. V důsledku toho se prostředí, která nabízejí levnější elektřinu, klima příznivé pro chlazení nebo bohatou energetickou infrastrukturu, přirozeně stávají atraktivnějšími.



Mining Bitcoin se tak z činnosti, která byla v počátcích přístupná každému, stala činnost, které dominuje specializované vybavení a profesionální operace. To však nemění pravidla protokolu. Teoreticky může těžit kdokoli s jakýmkoli strojem. V praxi však úroveň obtížnosti a účinnosti ASIC způsobila, že domácí mining je ve většině případů značně nekonkurenceschopný.



Samozřejmě stále existují situace, ve kterých může být domácí mining zajímavý, například pokud využíváte velmi levnou elektřinu nebo pokud využíváte teplo generated z horníka k vytápění domu v zimě. V každém případě si však budete muset pořídit stroj vybavený čipem ASIC. A co víc, protože váš výkon mining zůstane v porovnání se sítí Bitcoin extrémně malý, budete muset najít způsob, jak snížit rozptyl svých příjmů: to je právě úloha poolů mining, o kterých budeme hovořit v další kapitole.



Pokud byste chtěli prozkoumat domácí řešení mining s rekuperací tepla, máme pro vás návody na různé nástroje, a to jak hotové, tak i pro kutily:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Seskupení do skupin mining


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin zahrnuje průběžné a nevyhnutelné náklady, mezi nimiž je na prvním místě spotřeba energie stroje. Tyto náklady vznikají nezávisle na jakýchkoli výsledcích, přestože příjmy z mining jsou ze své podstaty vzácné a náhodné. Objevení bloku závisí výhradně na podílu těžaře na hashrate, což činí příjmy tím nepředvídatelnějšími, čím menší je tento podíl. Právě tento praktický problém rychle vedl k rozsáhlému využívání [poolů mining](https://planb.academy/resources/glossary/pool-mining). V této závěrečné kapitole kurzu MIN 101 nabízím úvod do principů a fungování poolů mining v Bitcoin.



### Co je to bazén mining?



Pool mining je organizace (často online služba), která sdružuje výpočetní výkon mnoha nezávislých těžařů s cílem zvýšit frekvenci, s jakou jejich skupina nachází bloky. Když pool najde blok, odměna za blok je pak přerozdělena mezi účastníky podle interních pravidel poolu (která budou probírána v kurzu MIN 201, protože jsou pro MIN 101 příliš složitá).



Účastníci poolu mining jsou pak často označováni jako "[hashers](https://planb.academy/resources/glossary/hasher)", nikoli jako "miners", protože již neprovádějí veškerou práci s mining, ale pouze hashují data, která jim pool předává.



Dávejte pozor, abyste nezaměnili fond mining s farmou mining. Jedná se o dva odlišné koncepty. Jak jsme viděli v předchozí kapitole, farma je fyzická lokalita, kde jeden subjekt provozuje mnoho strojů mining. Naproti tomu pool je především virtuální seskupení: tisíce strojů, často geograficky rozptýlených, pracují pod společnou koordinací. Farma se však může účastnit a často se také účastní poolu.



![Image](assets/fr/048.webp)



### Snížení rozdílu v příjmech



Proč se tedy připojit k bazénu? Jednoduše proto, že výsledek činnosti mining je pravděpodobnostní: při každém pokusu o hašování existuje velmi malá šance, že splní cíl obtížnosti, a tedy vytvoří platný blok.



Ve velmi dlouhém období by váš průměrný výdělek měl být úměrný vašemu podílu na celkovém fondu hashrate. Tento princip vyplývá přímo ze zákonů pravděpodobnosti: každý výpočet hashe představuje nezávislé náhodné losování a podle zákona velkých čísel frekvence, s jakou objevujete bloky, matematicky konverguje k vašemu podílu na celkovém počtu hashrate v síti. V krátkodobém až střednědobém horizontu však mohou být vaše skutečné výdělky velmi nepravidelné. Právě tomuto rozporu mezi teoretickým průměrem a náhodnou skutečností říkáme v matematice **variance**.



Zde je jednoduchý příklad, který ilustruje tento princip:




- Síť Bitcoin produkuje v průměru 144 bloků denně (přibližně jeden blok každých 10 minut);
- Pokud máte `0,0001 %` z celkového počtu hashrate, vaše očekávání je `144 × 0,000001`, tedy `0,000144` bloku/den;
- Jinými slovy byste měli najít blok v průměru každých `1 / 0,000144` dní, tj. každých 6 944 dní, tedy přibližně 19 let.



Tato hodnota však odpovídá pouze matematickému očekávání: rozdělení časů objevení se řídí náhodným zákonem, takže v praxi je zcela možné, že se nikdy neobjeví jediný blok, a to ani za velmi dlouhé období. Můžete mít smůlu a velmi dlouhou dobu nic nenajít, přičemž budete platit opakující se náklady (elektřina, údržba, odpisy zařízení...).



Bazén mining mění povahu tohoto problému: kombinací jednotek hashrate nachází bazén bloky častěji. Každý účastník pak souhlasí s tím, že obdrží pouze část každého nalezeného bloku, ale mnohem častěji. Jde o transformaci z vysoce volatilního, široce rozprostřeného příjmu na pravidelnější příjem, a to za cenu sdílení odměn a placení servisních poplatků.



### Proč se při seskupení snižuje rozptyl?



Čím vyšší je váš výpočetní výkon, tím vyšší je očekávaná četnost nalezených bloků. Ještě důležitější je, že čím častější jsou události, tím blíže jsou pozorované výsledky statistickému průměru za dané období.



Drobný těžař může samostatně těžit celé roky bez jediného bloku, pak jednoho dne dostane velkou výplatu a pak už nic. V poolu stále platí stejná pravděpodobnostní realita, ale v kolektivním měřítku je vyhlazena: pool nachází bloky častěji a přerozdělování tyto události mění na pravidelnější výplaty pro každého účastníka. **Pool mining tedy prodává předvídatelnost aktivity mining**.



### Historické památky



Jak jsme viděli v předchozí kapitole, na samém začátku bylo možné mining řešit samostatně s běžným počítačem, protože obtížnost byla velmi nízká. Jakmile však globální hashrate explodoval (GPU, poté ASIC), stal se sólový mining pro většinu účastníků velmi časově náročným hazardem.



První bazény vznikly právě jako reakce na tuto novou skutečnost. Braiins Pool (dříve Slush Pool / Bitcoin.cz) je první pool Bitcoin mining: svůj první blok vytěžil 16. prosince 2010. Úspěch tohoto prvního poolu mining byl rychlý, neboť během několika dní získal téměř 3,5 % celosvětového podílu hashrate.



![Image](assets/fr/047.webp)



Po technické stránce pak byly pooly strukturovány na základě specializovaných komunikačních protokolů mezi poolem a těžaři (např. [Stratum](https://planb.academy/resources/glossary/stratum), pak Stratum V2), aby bylo možné efektivně organizovat distribuovanou práci. Na tyto koncepty se blíže podíváme v našem školení MIN 201.



### Moderní situace



V době psaní tohoto článku (začátek roku 2026) je globální Bitcoin hashrate řádově zetta-hash za sekundu (= 1 000 EH/s = 1 000 000 000 000 000 000 000 000 hashů za sekundu) a téměř všechny nalezené bloky pocházejí z poolů mining.



Zde je dosavadní pořadí hlavních skupin mining a jejich podíl na hashrate. Toto pořadí se pravděpodobně do doby, než budete číst tento kurz, změní. Aktuální údaje naleznete na adrese [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Zdroj [mempool.space](https://mempool.space/graphs/mining/pools), údaje za jeden měsíc, 16. prosince 2025 až 16. ledna 2025.*



V pokročilejším kurzu se budeme hlouběji zabývat vnitřním fungováním poolů (podíly, síťové protokoly, platební metody...), protože právě zde se dostávají do hry detaily, které určují ziskovost těžaře i potenciální důsledky pro Bitcoin.



---

Dostali jsme se na konec kapitoly MIN 101. Děkujeme vám, že jste ji sledovali až do konce. Pokud si chcete zhodnotit dovednosti, které jste v průběhu kurzu získali, čeká vás v následující části závěrečná zkouška.



Se základními znalostmi, které jste právě získali, můžete nyní absolvovat pokročilejší kurzy mining na Plan ₿ Academy, ať už teoretické, jako je tento, nebo praktičtější, abyste se i vy mohli začít účastnit Bitcoin mining!



# Závěrečná část


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Recenze a hodnocení


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Závěrečná zkouška


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Závěr


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>