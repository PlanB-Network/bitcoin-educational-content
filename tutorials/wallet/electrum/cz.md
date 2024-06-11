---
name: Electrum

description: Kompletní průvodce Electrum, od začátečníka po experta
---

![obálka](assets/cover.webp)

Popis pro Electrum

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

> "Musím říct, když jsem narazil na tento průvodce, byl jsem šokován. Gratuluji Armanovi the Parmanovi za to. Byla by to škoda, kdybychom to zde nehostili a nepřeložili do co nejvíce jazyků. Upřímně, tomu chlapíku dejte spropitné." Rogzy

Původní příspěvek:

![Electrum Desktop Wallet (Mac / Linux) - stáhnout, ověřit, připojit k vašemu uzlu.](https://youtu.be/wHmQNcRWdHM)

![Provádění Bitcoin transakce s Electrum](https://youtu.be/-d_Zd7VcAfQ)

## Proč Electrum?

Toto je podrobný průvodce, jak používat Bitcoin peněženku Electrum, s řešeními všech jejích pastí a zvláštností - něco, co jsem vyvinul po několika letech používání a výuky studentů o bezpečnosti a soukromí Bitcoinu. Electrum není nejlepší Bitcoin peněženka pro osobu, která chce mít vše co nejjednodušší a zůstat na úrovni začátečníka. Místo toho je určena pro osobu, která je, nebo aspiruje být, "pokročilým" uživatelem.

Pro nového Bitcoinera je vynikající pouze pod dohledem zkušeného uživatele, který mu ukáže cestu. Pokud se učí používat ji sami, bude to bezpečné, pokud si dají čas a použijí ji v testovacím prostředí pouze s malým počtem satoshi na začátku. Tento průvodce podporuje toto úsilí, ale je také dobrým zdrojem pro kohokoli jiného.

> Varování: Tento průvodce je obsáhlý. Nepokoušejte se udělat vše v jeden den. Nejlepší je průvodce uložit a postupně se k němu vracet.

## Stahování Electrum

Ideálně použijte speciální Bitcoin počítač pro vaše Bitcoin transakce (Můj průvodce pro toto https://armantheparman.com/mint/) _(TAKÉ dostupné v sekci o soukromí)_. Je v pořádku cvičit s malými částkami na "špinavém" počítači, když se učíte (kdo ví, kolik skrytého malwaru váš běžný počítač za ta léta nahromadil - nechcete vystavit vaše Bitcoin peněženky jim).

Electrum získáte z https://electrum.org/.

Klikněte na záložku Stáhnout nahoře.

Klikněte na odkaz ke stažení, který odpovídá vašemu počítači. Jakýkoliv Linux nebo Mac počítač může použít odkaz Python (červený kruh). Linuxový počítač s čipem Intel nebo AMD může použít Appimage (zelený kruh; to je jako spustitelný soubor pro Windows). Zařízení Raspberry Pi má mikroprocesor ARM a může použít pouze verzi Python (červený kruh), nikoli Appimage, i když Pi běží na Linuxu. Modrý kruh je pro Windows a černý kruh pro Mac.

![obrázek](assets/1.webp)

## Ověření Electrum

Účelem "ověření" staženého souboru je ujistit se, že s daty nebylo nijak manipulováno. Zabraňuje použití "hacknuté" škodlivé verze softwaru. Je v pořádku toto ověření přeskočit, pokud používáte staženou kopii pouze pro cvičení, tj. nepoužíváte peněženky, které drží vážné peníze. Poté, co budete připraveni používat Electrum pro vaše skutečné fondy, měli byste svou kopii smazat a začít znovu, tentokrát ověřením vašeho stažení.
K tomu používáme nástroje pro kryptografii s veřejným a soukromým klíčem – gpg, o kterém jsme napsali průvodce zde (https://armantheparman.com/gpg/). Nástroj gpg je součástí všech operačních systémů Linux. Pro Mac a Windows si pro instrukce ke stažení prohlédněte odkaz na gpg.

Kromě stažení softwaru Electrum potřebujete pro zabezpečení také digitální PODPIS softwaru. Jedná se o řetězec textu (ve skutečnosti jde o číslo zakódované pomocí textu), který vyprodukoval vývojář svým SOUKROMÝM klíčem gpg. Pomocí programu gpg pak můžeme „otestovat“ PODPIS proti jeho VEŘEJNÉMU klíči (vytvořenému z vývojářova soukromého klíče), ke kterému má každý přístup, oproti staženému SOUBORU.

Jinými slovy, se třemi vstupy (podpis, veřejný klíč a datový soubor) získáme výstup pravda nebo nepravda, který potvrdí, že s souborem nebylo manipulováno.

Pro získání podpisu klikněte na odkaz odpovídající souboru, který jste stáhli (viz barevné šipky):

![image](assets/2.webp)

Kliknutím na odkaz se soubor může automaticky stáhnout do vaší složky Stahování, nebo se může otevřít v prohlížeči. Pokud se otevře v prohlížeči, musíte soubor uložit. Můžete kliknout pravým tlačítkem a vybrat „uložit jako“. V závislosti na operačním systému nebo prohlížeči může být nutné kliknout pravým tlačítkem na prázdné místo, nikoli na text.

Níže je uveden vzhled staženého textu. Můžete vidět, že existuje několik podpisů – jsou to podpisy různých lidí. Můžete ověřit každý z nich nebo libovolný. Ukážu vám, jak ověřit pouze podpis vývojáře.

![image](assets/3.webp)

Dále potřebujete získat veřejný klíč ThomasV – hlavního vývojáře. Můžete ho získat přímo od něj, z jeho účtu na Keybase, Githubu, nebo od někoho jiného, z keyserveru, nebo z webových stránek Electrum.

Získání z webových stránek Electrum je ve skutečnosti nejméně bezpečný způsob, protože pokud je tato webová stránka nebezpečná (právě to ověřujeme), proč bychom z ní získávali veřejný klíč (veřejný klíč by mohl být falešný)?

Prozatím to udržím jednoduché a ukážu vám, jak ho získat z webových stránek, ale mějte to na paměti. Zde je kopie (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc) na GitHubu, kterou můžete porovnat.

Trochu se posuňte dolů na stránce, abyste našli odkaz na veřejný klíč ThomasV (červený kruh níže). Klikněte na něj a stáhněte ho, nebo pokud se v prohlížeči otevře nějaký text, klikněte pravým tlačítkem a uložte.

![image](assets/4.webp)

Nyní máte 3 nové soubory, pravděpodobně všechny ve složce Stahování. Nezáleží na tom, kde jsou, ale proces je jednodušší, pokud je umístíte všechny do stejné složky.

Tři soubory:

1. Stažení Electrum
2. Soubor s podpisem (obvykle má stejný název jako stažení Electrum s příponou „.asc“)
3. Veřejný klíč ThomasV.

Otevřete terminál na Macu nebo Linuxu, nebo příkazový řádek (CMD) ve Windows.

Přejděte do adresáře Stahování (nebo kamkoli jste tyto tři soubory umístili). Pokud nevíte, co to znamená, naučte se z tohoto krátkého videa pro Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) a tohoto pro Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Pamatujte, že na počítačích s Linuxem jsou názvy adresářů citlivé na velká a malá písmena.
V terminálu napište toto, abyste importovali veřejný klíč ThomasV do "klíčenky" vašeho počítače (klíčenka je abstraktní koncept - ve skutečnosti jde jen o soubor ve vašem počítači):
```bash
gpg --import ThomasV.asc
```

Ujistěte se, že název souboru odpovídá tomu, co jste si stáhli. Všimněte si také, že jde o dvojitou pomlčku, ne o jednoduchou. Dále si všimněte, že před a za "--import" je mezera. Poté stiskněte <enter>.

Soubor by se měl importovat. Pokud dostanete chybu, zkontrolujte, zda jste ve složce, kde soubor skutečně existuje. Aby jste zkontrolovali, ve které složce jste (na Macu nebo Linuxu), napište pwd. Aby jste viděli, jaké soubory se nachází ve složce, ve které jste (na Macu nebo Linuxu), napište ls. Měli byste vidět textový soubor "ThomasV.asc", možná mezi dalšími soubory.

Poté spustíme příkaz pro ověření podpisu.

```bash
gpg --verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Všimněte si, že zde jsou 4 "elementy", každý oddělený mezerou. Text jsem střídavě zvýraznil tučně, aby vám to pomohlo vidět. Čtyři elementy jsou:

1. program gpg
2. možnost --verify
3. název souboru s podpisem
4. název souboru programu

Zajímavé je, že někdy můžete vynechat 4. element a počítač uhodne, co máte na mysli. Nejsem si jistý, ale myslím, že to funguje pouze v případě, že se názvy souborů liší pouze příponou "asc" na konci.

Nekopírujte jen názvy souborů, které jsem zde ukázal - ujistěte se, že odpovídají názvu souboru, který máte ve svém systému.

Stiskněte <enter> pro spuštění příkazu. Měli byste vidět "dobrý podpis od ThomasV" jako indikaci úspěchu. Objeví se nějaké chyby, protože nemáme veřejné klíče pro podpisy ostatních lidí, které jsou obsaženy v souboru s podpisem (tento systém kombinování podpisů v jednom souboru se může v pozdějších verzích změnit). Také se na konci objeví varování, které můžeme ignorovat (to nás upozorňuje, že jsme počítači výslovně neřekli, že důvěřujeme veřejnému klíči ThomasV).

Nyní máme ověřenou kopii Electrum, kterou je bezpečné používat.

## Spuštění Electrum

### Spuštění Electrum, pokud používáte Python

Pokud jste si stáhli verzi pro Python, takto to funguje. Na stránce ke stažení uvidíte toto:

![image](assets/5.webp)

Pro Linux je dobré nejprve aktualizovat váš systém:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Zkopírujte zvýrazněný žlutý text, vložte ho do terminálu a stiskněte <enter>. Budete požádáni o heslo, možná o potvrzení pokračování, a poté se nainstalují tyto soubory ("závislosti").

Budete také potřebovat rozbalit zip soubor do složky podle vašeho výběru. To můžete udělat pomocí grafického uživatelského rozhraní, nebo z příkazové řádky (příkaz zvýrazněný růžově) - pamatujte, že názvy vašich souborů se mohou lišit. (Poznamenejme, že když jsme ověřovali stažení v předchozí sekci, ověřovali jsme zip soubor, nikoli rozbalenou složku.)

Existuje možnost "instalace" pomocí programu PIP, ale to není nutné a přidává další kroky a instalaci souborů. Program jednoduše spusťte pomocí terminálu, abyste to všechno obešli.

Kroky (Linux) jsou:

1. navigujte do složky, kde jsou soubory rozbalené
2. napište: ./run_electrum

Na Macu jsou kroky stejné, ale možná budete muset nejprve nainstalovat Python3 a použít tento příkaz pro spuštění:

```bash
```bash
python3 ./run_electrum
```

Jakmile je Electrum spuštěno, terminálové okno zůstane otevřené. Pokud jej zavřete, program Electrum se ukončí. Pouze jej minimalizujte, když používáte Electrum.

### Spuštění Electrum s Appimage

To je trochu jednodušší, ale ne tak snadné jako spustitelný soubor pro Windows. V závislosti na verzi Linuxu, kterou používáte, mohou mít soubory Appimage výchozí atributy nastavené tak, že systém jejich spuštění neumožňuje. Musíme to změnit. Pokud vaše Appimage funguje, tento krok můžete přeskočit. Přejděte v terminálu tam, kde se soubor nachází, a poté spusťte tento příkaz:

```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

„sudo“ uděluje oprávnění superuživatele; „chmod“ je příkaz ke změně módu, který upravuje, kdo může číst, psát nebo spouštět; „ug+x“ znamená, že upravujeme uživatele a skupinu tak, aby bylo umožněno spuštění.

Upravte název souboru tak, aby odpovídal vaší verzi.

Poté Electrum spustíte dvojitým kliknutím na ikonu Appimage.

### Spuštění Electrum na Macu

Stačí dvakrát kliknout na stažený soubor (jedná se o „disk“). Otevře se okno. Přetáhněte ikonu Electrum v okně na plochu nebo kamkoli jinam, kde chcete program uchovávat. Poté můžete „disk“ vysunout a smazat (stažený soubor).

Program spustíte dvojitým kliknutím na něj. Můžete se setkat s některými specifickými chybami pro Mac, které je třeba obejít.

### Spuštění Electrum na Windows

Přestože Windows nemám rád ze všeho nejvíce, je to nejjednodušší metoda. Stačí dvakrát kliknout na spustitelný soubor.

## Začněte s falešnou peněženkou

Když poprvé spustíte Electrum, otevře se okno jako toto:

![obrázek](assets/6.webp)

Později si server vybereme ručně, ale prozatím ponechte výchozí nastavení a auto-připojení.

Dále vytvořte falešnou peněženku – do této peněženky nikdy nevkládejte prostředky. Účelem této falešné peněženky je postupovat softwarem a ujistit se, že vše funguje dobře, než do něj nahrajete vaši skutečnou peněženku. Snažíme se vyhnout náhodnému prozrazení soukromí se skutečnou peněženkou. Pokud jen cvičíte, peněženku, kterou vytvoříte, můžete stejně považovat za falešnou.

Název můžete nechat jako „default_wallet“ nebo jej změnit na cokoli jiného a kliknout na další. Později, pokud budete mít více peněženek, je můžete v této fázi najít a otevřít kliknutím na „Choose…“

![obrázek](assets/7.webp)

Vyberte „Standard wallet“ a <Next>:

![obrázek](assets/8.webp)

Poté vyberte „I already have a seed“. Nechci, abyste si zvykli na vytváření Electrum seedu, protože používá vlastní protokol, který není kompatibilní s ostatními peněženkami – to je důvod, proč neklikáme na „new seed“.

![obrázek](assets/9.webp)

Přejděte na https://iancoleman.io/bip39/ a vytvořte falešný seed. Nejprve změňte počet slov na 12 (což je běžná praxe), poté klikněte na „generate“ a slova v okně zkopírujte do schránky.

![obrázek](assets/10.webp)

Poté slova vložte do Electrum. Zde je příklad:

![obrázek](assets/11.webp)

Electrum bude hledat slova, která odpovídají jeho vlastnímu protokolu. Musíme to obejít. Klikněte na možnosti a vyberte BIP39 Seed:

![obrázek](assets/12.webp)
Semeno poté začne být platné. (Před tímto krokem Electrum očekávalo Electrum semeno, takže toto semeno bylo považováno za neplatné). Než kliknete na další, všimněte si textu, který říká "Checksum OK". Je důležité (pro skutečnou peněženku, kterou později můžete použít), abyste toto viděli před pokračováním, protože to potvrzuje platnost zadaného semena. Varování u spodní části můžete ignorovat, jedná se o stížnost vývojářů Electrum na BIP39 a jejich "FUD'ové" tvrzení, že jejich verze (která není kompatibilní s ostatními peněženkami) je lepší.

> Rychlá odbočka pro důležité varování. Účelem kontrolního součtu je ujistit se, že jste zadali své semeno bez chyb při psaní. Kontrolní součet je poslední část semena (12. slovo je slovo kontrolního součtu), které je matematicky určeno první částí semena (11 slov). Pokud byste na začátku něco špatně napsali, slovo kontrolního součtu se matematicky neshoduje a software peněženky vás upozorní varováním. To neznamená, že semeno nemůže být použito k vytvoření funkční Bitcoin peněženky. Představte si vytvoření peněženky s chybou při psaní, načtení peněženky bitcoinem, a pak jednoho dne budete potřebovat peněženku obnovit, ale když to uděláte, neopakujete chybu při psaní - obnovíte špatnou peněženku! Je poměrně nebezpečné, že vám Electrum umožní pokračovat ve vytváření peněženky, pokud je váš kontrolní součet neplatný, takže buďte varováni, je vaší odpovědností se ujistit. Ostatní peněženky vám nepovolí pokračovat, což je mnohem bezpečnější. To je jedna z věcí, které mám na mysli, když říkám, že používání Electrum je v pořádku, jakmile se naučíte ho správně používat (vývojáři Electrum by to měli opravit).

Všimněte si, že pokud byste chtěli přidat heslovou frázi, možnost to vybrat je v tomto okně možností, hned nahoře.

Po kliknutí na OK se vrátíte tam, kde jste zadali frázi semena. Pokud jste vybrali možnost heslové fráze, NEZADÁVEJTE ji spolu se slovy semena (výzva k tomu přijde dále).

Pokud jste nevyžádali heslovou frázi, uvidíte následující obrazovku – další možnosti pro typ skriptu vaší peněženky a cestu derivace, o kterých se můžete dozvědět zde (https://armantheparman.com/public-and-private-keys/), ale stačí nechat výchozí nastavení a pokračovat.

![obrázek](assets/13.webp)

> Pro další informace: První možnost vám umožňuje vybrat mezi legacy (adresy začínající na „1“), pay-to-script-hash (adresy začínající na „3“) nebo bech32/native segwit (adresy začínající na „bc1q“). V době psaní Electrum ještě nepodporuje taproot (adresy začínající na „bc1p“). Druhá možnost v tomto okně vám umožňuje upravit cestu derivace. Doporučuji toto nikdy neměnit, zejména před pochopením, co to znamená. Lidé budou zdůrazňovat důležitost zapsání cesty derivace, abyste mohli peněženku v případě potřeby obnovit, ale pokud ji necháte jako výchozí, pravděpodobně to bude v pořádku, takže se nebojte – ale stále je dobrým zvykem zapsat si cestu derivace.

Dále vám bude nabídnuta možnost přidat HESLO. To by nemělo být zaměňováno s „HESLOVOU FRÁZÍ“. Heslo zamyká soubor na vašem počítači. Heslová fráze je součástí struktury soukromého klíče. Jelikož se jedná o fiktivní peněženku, můžete heslo nechat prázdné a pokračovat.

![obrázek](assets/14.webp)
Dostanete vyskakovací okno o notifikacích nové verze (doporučuji vybrat ne). Peněženka se poté sama vygeneruje a bude připravena k použití (ale pamatujte, že tato peněženka je určena k smazání, je to jen zkušební peněženka).
![obrázek](assets/15.webp)

Jsou zde některé věci, které doporučuji udělat pro nastavení softwarového prostředí (vyžadováno pouze jednou):

### Změňte jednotky na BTC

Přejděte do horního menu, nástroje –> electrum předvolby, a tam pod záložkou obecné najdete možnost změnit „základní jednotku“ na BTC.
Povolte záložky Adresy a Mince

Přejděte do horního menu, zobrazení, a vyberte „zobrazit adresy“. Poté se vraťte do zobrazení a vyberte „zobrazit mince“.

### Povolte Oneserver

Ve výchozím nastavení se Electrum připojuje k náhodnému uzlu. Také se připojuje k mnoha dalším sekundárním uzlům. Nejsem si jistý, jaká data jsou s těmi sekundárními uzly vyměňována, ale nechceme, aby k tomu docházelo, kvůli soukromí. I když určíte uzel, např. svůj vlastní, k těmto mnoha dalším uzlům bude také dojít k připojení, a nejsem si jistý, jaké informace jsou sdíleny. Bez ohledu na to, je snadné tomu zabránit. Než vám ukážu, jak určit svůj vlastní uzel, donutíme Electrum, aby se připojoval pouze k jednomu serveru najednou.

> Existuje způsob, jak to udělat zadáním „oneserver“ z příkazové řádky, ale tento způsob nedoporučuji. Ukážu alternativu, která se mi zdá být snazší na dlouhou dobu a pravděpodobněji zabrání náhodnému připojení k jiným uzlům.

Důvod, proč používáme zkušební peněženku, je ten, že kdybychom načetli naši skutečnou peněženku, se skutečnými bitcoiny, nechtěně bychom se již připojili k náhodnému uzlu (i když jsme na začátku vybrali „nastavit server ručně“, stále se připojuje k těmto dalším sekundárním uzlům z nějakého důvodu (hej vývojáři Electrum, měli byste to opravit). Pokud by naše peněženka byla soukromá, byla by to katastrofa.

Kroky, které vám níže ukážu, také nemůžeme provést bez nejprve načtení nějakého typu peněženky. (Budeme upravovat konfigurační soubor, který je naplněn a připraven k úpravám pouze po načtení peněženky).

**Ukončete Electrum (DŮLEŽITÉ, pokud to neuděláte, následující změny, které provedete, budou smazány).**

### LINUX/MAC Konfigurační soubor

Otevřete terminál v Linuxu nebo Macu (instrukce pro Windows později):

Automaticky byste měli být ve složce domů. Odtud navigujte do skryté složky nastavení electrum (to je něco jiného než kde je aplikace).

```bash
cd .electrum
```

Všimněte si tečky před „electrum“, která naznačuje, že je to skrytá složka.

Další způsob, jak se tam dostat, je napsat:

```bash
cd ~/.electrum
```

kde „~“ představuje cestu vašeho domovského adresáře. Plnou cestu vašeho aktuálního adresáře můžete vidět s příkazem „pwd“.

Až budete v adresáři „.electrum“, napište „nano config“ a stiskněte <enter>.

Otevře se textový editor (nazývaný nano) s otevřeným konfiguračním souborem. Myš zde moc nefunguje. Použijte šipky k navigaci na řádek, který říká:

```json
"oneserver": false,
```

Změňte „false“ na „true“; a neničte syntaxi (nemažte čárku ani středník).

Stiskněte <ctrl> x, pro ukončení, poté „y“ pro uložení, a poté <enter>, což potvrdí změnu bez úpravy názvu souboru.
Nyní spusťte Electrum znovu. Poté klikněte na kruh v pravém dolním rohu, což otevře nastavení sítě. Pak, blízko vrcholu v záložce přehled, uvidíte "připojeno k 1 uzlu" - to ukazuje na úspěch.
Hned pod tím uvidíte textové pole a v něm je adresa serveru. V současné době jste připojeni k tomuto náhodnému uzlu. Více o připojení k uzlu v další sekci.

### Konfigurační soubor pro Windows

Konfigurační soubor pro Windows je trochu těžší najít. Adresář je: `C:/Users/Parman/AppData/Roaming/Electrum`

Samozřejmě musíte změnit "Parman" na vaše vlastní uživatelské jméno pro počítač.

V této složce najdete konfigurační soubor. Otevřete ho v textovém editoru a upravte řádek:

```json
"oneserver": false,
```

Změňte "false" na "true"; nedotýkejte se syntaxe (nemažte čárku nebo středník).

Poté soubor uložte a zavřete.

## Připojení Electrum k uzlu

Dále chceme připojit naši zkušební peněženku k uzlu našeho výběru. Pokud nejste připraveni spustit vlastní uzel, můžete udělat jedno z následujících:

1. Připojit se k osobnímu uzlu přítele (vyžaduje Tor)
2. Připojit se k uzlu důvěryhodné společnosti
3. Připojit se k náhodnému uzlu (nedoporučuje se).

Mimochodem, zde jsou instrukce, jak spustit vlastní uzel, a to jsou důvody, proč byste to měli udělat. (všechny tutoriály v sekci Node nebo v našich bezplatných kurzech)

### Připojení k uzlu přítele přes Tor (Průvodce brzy přijde.)

### Připojení k uzlu důvěryhodné společnosti

Jediný důvod pro to by byl, pokud musíte přistupovat k blockchainu a nemáte k dispozici vlastní uzel (nebo přítele).

Pojďme se připojit k uzlu Bitaroo – Bylo nám řečeno, že nesbírají data. Jsou to směnárna pouze pro Bitcoin, provozovaná vášnivým Bitcoinistou. Připojení k nim zahrnuje trochu důvěry, ale je to lepší než připojení k náhodnému uzlu, který by mohl být sledovací společností.

Dostanete se do Nastavení sítě kliknutím na kruh v pravém dolním rohu okna Peněženky (červená značí nepřipojeno, zelená značí připojeno a modrá značí připojeno přes Tor).

![image](assets/16.webp)

Jakmile kliknete na ikonu kruhu, objeví se vyskakovací okno: Vaše peněženka ukáže "připojeno k 1 uzlu", protože jsme to dříve vynutili.

Zrušte zaškrtnutí políčka "vybrat server automaticky" a poté do pole Server zadejte údaje Bitaroo, jak je ukázáno:

![image](assets/17.webp)

Zavřete okno a nyní bychom měli být připojeni k uzlu Bitaroo. Pro potvrzení by kruh měl být zelený. Klikněte na něj znovu a zkontrolujte, že se údaje serveru nezměnily zpět na náhodný uzel.

### Připojení k vlastnímu uzlu

Pokud máte vlastní uzel, to je skvělé. Pokud máte pouze Bitcoin Core a ne Electrum SERVER, ještě nebudete moci připojit Electrum WALLET k vašemu uzlu.

> Poznámka: Electrum Server a Electrum Wallet jsou různé věci. Server je software potřebný, aby Electrum Wallet mohl komunikovat s Bitcoin blockchainem - nevím, proč to bylo navrženo tímto způsobem - možná kvůli rychlosti, ale nemusí to být pravda.
Pokud spustíte softwarový balíček pro uzel, jako je MyNode (ten, který lidem doporučuji začít s), Raspiblitz (doporučený, jakmile se stanete pokročilejšími), nebo Umbrel (osobně ho zatím nedoporučuji, protože jsem narazil na příliš mnoho problémů), pak budete moci připojit svou peněženku jednoduše zadáním IP adresy počítače (Raspberry Pi) běžícího uzel, plus dvojtečka, a 50002, jak je ukázáno na obrázku v předchozí sekci. (Dále vám ukážu, jak najít IP adresu vašeho uzlu).
Otevřete nastavení sítě (klikněte na zelený nebo červený kruh v pravém dolním rohu). Odškrtněte políčko "vybrat server automaticky", poté zadejte svou IP adresu, jak jsem to udělal já, vaše bude odlišná, ale dvojtečka a "50002" by měly být stejné.

![obrázek](assets/18.webp)

Zavřete okno, a nyní bychom měli být připojeni k vašemu uzlu. Pro potvrzení klikněte znovu na kruh a zkontrolujte, že se údaje serveru nezměnily zpět na náhodný uzel.

Někdy, i přes správné postupy, se zdá, že se připojení nedaří. Zde jsou věci, které můžete zkusit…

- Aktualizujte na novější verzi Electrum a vašeho softwaru uzlu
- Zkuste smazat složku cache v adresáři ".electrum"
- Zkuste změnit port z 50002 na 50001 v nastavení sítě
- Použijte tento průvodce pro připojení pomocí Tor jako alternativu (https://armantheparman.com/tor/)
- Přeinstalujte Electrum Server na uzlu

## NALEZENÍ IP ADRESY VAŠEHO UZLU

IP adresa není něco, co by běžný uživatel obvykle věděl, jak vyhledat a použít. Pomohl jsem mnoha lidem spustit uzel a poté připojit jejich peněženky k uzlu – častým problémem se zdá být nalezení jeho IP adresy.

Pro MyNode můžete do okna prohlížeče zadat: `mynode.local`

Někdy "mynode.local" nefunguje (ujistěte se, že to nezadáváte do vyhledávacího pole Google. Aby navigační lišta rozpoznala váš text jako adresu a ne jako vyhledávání, předřaďte textu `http://` takto: `http://mynode.local`. Pokud to nefunguje, zkuste to s "s", jako toto: `https://mynode.local`.

To vám umožní přístup k zařízení a můžete kliknout na odkaz nastavení (viz můj modrý "kruh" níže) pro zobrazení této obrazovky, kde se nachází IP adresa:

![obrázek](assets/19.webp)

Tato stránka se načte a uvidíte IP uzlu (modrý "kruh")

![obrázek](assets/20.webp)

Poté, v budoucnu, můžete do svého prohlížeče zadat 192.168.0.150, nebo http://192.168.0.150.

Pro Raspiblitz (když nepřipojujete obrazovku), potřebujete jinou metodu (která funguje i pro MyNode):

Přihlaste se na webovou stránku vašeho routeru – zde najdeme IP adresu všech vašich připojených zařízení. Webová stránka routeru bude IP adresa, kterou zadáte do webového prohlížeče. Moje vypadá takto:

    http://192.168.0.1

Pro získání přihlašovacích údajů k routeru můžete hledat v uživatelské příručce nebo někdy dokonce na samolepce na samotném routeru. Hledejte uživatelské jméno a heslo. Pokud to nenajdete, zkuste Uživatel: "admin" Heslo: "password"

Pokud se vám podaří přihlásit, uvidíte svá připojená zařízení a z jejich názvů by mohlo být jasné, které je vaším uzlem. IP adresa tam bude.
### Pokud první dvě metody selžou, poslední bude fungovat, ale je to zdlouhavé:
Nejprve najděte IP adresu jakéhokoli zařízení ve vaší síti (váš aktuální počítač bude stačit).

Na Macu ji najdete v Nastavení sítě:

![obrázek](assets/21.webp)

Zajímají nás první 4 prvky (192.168.0), ne čtvrtý prvek, "166", který vidíte na obrázku (váš bude jiný).

Pro Linux použijte příkazový řádek:

```bash
ifconfig | grep inet
```

Tato vertikální čára je symbol "pipe" a najdete ji pod klávesou <delete>. Uvidíte nějaký výstup a IP adresu. (Ignorujte 127.0.0.1, to není ono, a ignorujte také netmask)

Pro Windows otevřete příkazový řádek (cmd) a zadejte:

```bash
ipconfig/all
```

a stiskněte Enter. IP adresu najdete ve výstupu.

To byla ta snadná část. Teď přichází na řadu těžká část, najít IP adresu vašeho uzlu – musíme hádat metodou pokus-omyl. Řekněme například, že IP adresa vašeho počítače začíná na 192.168.0.xxx, pak pro váš uzel, v prohlížeči zkuste: `https://192.168.0.2`

Nejmenší možné číslo je 2 (0 znamená jakékoli zařízení a 1 patří routeru) a nejvyšší, myslím, že je 255 (to je náhodou 11111111 v binárním kódu, největší číslo, které může 1 byte obsahovat).

Postupně se propracujte směrem k 255. Nakonec se zastavíte na správném čísle, které načte stránku vašeho MyNode (nebo RaspiBlitz). Pak budete vědět, jaké číslo zadat do nastavení sítě Electrum, abyste se připojili k vašemu uzlu.

Bude to vypadat nějak takto (ujistěte se, že zahrnete dvojtečku a číslo za ní):

![obrázek](assets/22.webp)

> Je dobré vědět, že tyto IP adresy jsou VNITŘNÍ pro vaši domácí síť. Nikdo zvenčí je nemůže vidět a nejsou citlivé. Jsou to jakési telefonní přípojky ve velké organizaci, které vás směrují na různé telefony.

## Smazání falešné peněženky

Nyní jsme úspěšně připojeni k jednomu a jedinému uzlu. Takto bude Electrum odteď výchozí. Nyní byste měli smazat falešnou peněženku (Menu: soubor –> smazat), pro případ, že byste omylem poslali prostředky na tuto nezabezpečenou peněženku (Je nezabezpečená, protože jsme ji nevytvořili bezpečným způsobem).

## Vytvoření cvičné peněženky

Po smazání falešné peněženky začněte znovu a vytvořte novou, stejným způsobem, jen tentokrát si zapište seed slova a uchovávejte je na poměrně bezpečném místě.

Je dobrý nápad naučit se, jak Electrum funguje s touto cvičnou peněženkou, bez obtížného hardware peněženky (potřebné pro vysokou bezpečnost). Vložte do této peněženky jen malou část bitcoinů – Předpokládejte, že tyto peníze ztratíte. Až budete dostatečně zkušení, pak se naučte používat Electrum s hardware peněženkou.

Ve vytvořené nové peněžence uvidíte seznam adres. Zelené se nazývají "přijímací adresy". Jsou produktem 3 věcí:

- Seed fráze
- Heslo
- Derivační cesta

Vaše nová peněženka má sadu přijímacích adres, které mohou být matematicky a reprodukovatelně vytvořeny jakoukoli softwarovou peněženkou, která má seed, heslo a derivační cestu. Je jich 4,3 miliardy! Více, než budete potřebovat. Electrum vám ukáže pouze prvních 20, a pak další, jak budete ty první používat.
Více informací o soukromých klíčích bitcoinu najdete v tomto průvodci.
![obrázek](assets/23.webp)

To se velmi liší od některých dalších peněženek, které zobrazují pouze jednu adresu najednou.

Protože jste při vytváření této peněženky zadali seed frázi, Electrum má soukromý klíč pro každou z adres, a proto je možné z těchto adres utrácet.

Dále si všimněte, že existují žluté adresy nazývané "změnové adresy" – Jedná se o další sadu adres z jiné matematické větve (existuje dalších 4,3 miliardy těchto adres). Peněženka je používá k automatickému odesílání přebytečných prostředků zpět do peněženky jako změnu. Například, pokud vezmete 1,5 bitcoinu a utratíte 0,5 u obchodníka, zbytek 1,0 musí jít někam. Vaše peněženka ho pošle na další prázdnou žlutou změnovou adresu – jinak půjde těžaři! Pro více informací o tomto (UTXOs) viz tento průvodce. (https://armantheparman.com/utxo/)

Poté se vraťte na webovou stránku soukromých klíčů Iana Colmana a zadejte seed (místo generování nového). Uvidíte, že informace o soukromém a veřejném klíči se změní; všechno níže závisí na věcech výše na stránce.

> Pamatujte, že byste "nikdy" neměli zadávat seed na počítači pro vaši skutečnou Bitcoin peněženku – malware ji může ukrást. Nyní používáme pouze cvičnou peněženku, pro účely učení, takže to prozatím není problém.

Rolujte dolů a změňte cestu derivace na BIP84 (segwit) tak, aby odpovídala vaší peněžence Electrum kliknutím na záložku BIP84.

![obrázek](assets/24.webp)

Pod tím uvidíte rozšířený soukromý klíč účtu a rozšířený veřejný klíč účtu:

![obrázek](assets/25.webp)

Přejděte do Electrum a porovnejte, že se shodují. V horním menu je položka peněženka –> informace:

![obrázek](assets/26.webp)

Tohle se objeví:

![obrázek](assets/27.webp)

Všimněte si, že se dva veřejné klíče shodují.

Dále porovnejte adresy. Vraťte se na stránku Iana Colemana a rolujte dolů:

![obrázek](assets/28.webp)

Všimněte si, že se shodují s adresami v Electrum.

Nyní zkontrolujeme změnové adresy. Rolujte trochu nahoru k cestě derivace a změňte poslední 0 na 1:

![obrázek](assets/29.webp)

Nyní rolujte dolů a porovnejte, že se adresy shodují se žlutými adresami v Electrum

Proč jsme to všechno dělali?

Vzali jsme seed slova a prošli je dvěma různými nezávislými softwarovými programy, abychom se ujistili, že nám dávají stejné informace. To výrazně snižuje riziko, že by v nich číhal škodlivý kód, který by nám poskytoval falešné soukromé nebo veřejné klíče, nebo adresy.

Dalším krokem je přijmout malý test a utratit ho v peněžence z jedné adresy na druhou.

## Testování peněženky (Naučte se ji používat)

Zde vám ukážu, jak přijmout UTXO do vaší peněženky a poté ji (utratit) na jinou adresu v peněžence. Jedná se o velmi malou částku, kterou nám nebude vadit ztratit.

To má několik účelů.

- Dokáže, že máte moc utrácet mince v nové peněžence.
- Ukáže, jak používat software Electrum k provedení platby (a některé funkce), než přidáme další složitost pro bezpečnost (použití hardwarové peněženky nebo počítače bez připojení k internetu)
- Posílí myšlenku, že máte na výběr mnoho adres pro příjem a utrácení, v rámci téže peněženky.
Otevřete svou testovací peněženku Electrum a klikněte na záložku Adresy, poté pravým tlačítkem myši klikněte na první adresu a vyberte Kopírovat -> Adresa:
![image](assets/30.webp)

Adresa je nyní v paměti vašeho počítače.

Nyní přejděte na burzu, kde máte nějaké bitcoiny, a vyjměme malé množství na tuto adresu, řekněme 50 000 satoshi. Jako příklad použiji Coinbase, protože je to nejčastěji používaná burza, i když jsou nepřítelem Bitcoinu, a je mi nepříjemné se přihlásit do starého opuštěného účtu za tímto účelem.

Přihlaste se a klikněte na tlačítko Odeslat/Přijmout, které je dnes v pravém horním rohu webové stránky.

![image](assets/31.webp)

Samozřejmě nemám na Coinbase žádné prostředky, ale představte si, že zde jsou prostředky a postupujte podle návodu: Vložte adresu z Electrum do pole "Komu", jak jsem to udělal. Také budete muset vybrat množství (doporučuji asi 50 000 satoshi). Nezadávejte "volitelnou zprávu" - Coinbase už tak sbírá dost vašich dat (a prodává je), není třeba jim pomáhat. Nakonec klikněte na "Pokračovat". Poté nevím, jaké další vyskakovací okna se objeví, jste na to sami, ale metoda je podobná pro všechny burzy.

![image](assets/32.webp)

V závislosti na burze můžete vidět satoshi ve své peněžence okamžitě nebo s několikahodinovým/denním zpožděním.

Všimněte si, že Electrum vám ukáže přijaté mince, i když nebyly potvrzeny na blockchainu. Mince, které máte, jsou čteny ze seznamu čekajících transakcí Bitcoin Node, nebo "mempool". Když se dostanou na blok, uvidíte prostředky jako potvrzené.

Nyní, když máme v naší peněžence UTXO, měli bychom jej označit. Toto označení vidíme pouze my, nesouvisí s veřejným ledgerem. Všechna naše označení v Electrum jsou viditelná pouze na počítači, který používáme. Můžeme dokonce uložit soubor a použít ho k obnovení všech našich označení na jiném počítači se stejnou peněženkou.

### Označte UTXO

Potřeboval jsem dar na tuto testovací peněženku, díky @Sathoarder za poskytnutí živého UTXO (10 000 satoshi) a další osoba (anon) darovala na stejnou adresu (5000 satoshi). Všimněte si, že na první adrese je zůstatek 15 000 satoshi a celkem 2 transakce (pravý sloupec). Dole je zůstatek 10 000 satoshi potvrzených a dalších 5 000 satoshi nepotvrzených (stále v mempoolu).

![image](assets/33.webp)

Nyní, pokud přejdeme na záložku Mince, můžeme vidět dvě "přijaté mince" nebo UTXO. Oba jsou na stejné adrese.

![image](assets/34.webp)

Vrátíme-li se na záložku adres, pokud dvakrát kliknete na oblast "označení" vedle adresy, budete moci zadat nějaký text, poté stiskněte <enter> pro uložení:

![image](assets/35.webp)

Je dobré si vést záznamy o tom, odkud vaše mince pocházejí, zda nejsou spojeny s KYC, a kolik vás každé UTXO stálo (v případě, že budete potřebovat prodat a vypočítat daň, která vám bude vládou ukradena).
Ideálně byste se měli vyhnout hromadění více mincí na téže adrese. Pokud se rozhodnete to udělat (nedělejte to), můžete každou minci označit místo označení všech stejným štítkem pomocí metody adresy. Ve skutečnosti nemůžete jít na záložku "mince" a upravit tam štítky (ne, to by bylo příliš intuitivní!). Musíte jít na záložku Historie, najít transakci, označit ji, a pak uvidíte štítky v sekci mincí. Všechny štítky, které vidíte v sekci mincí, pocházejí z označení adresy NEBO z historických štítků, ale jakýkoliv štítek z historie přepíše štítek adresy. Pro zálohování vašich štítků do souboru je můžete exportovat z menu nahoře, peněženka–>štítky–>export.

Dále, pojďme utratit mince z první adresy na druhou adresu. Klikněte pravým tlačítkem na první adresu a vyberte "utratit z" (To ve skutečnosti není v tomto scénáři nutné, ale představte si, že máme mnoho mincí na mnoha adresách; použitím této funkce můžeme peněžence nařídit, aby utratila pouze mince, které chceme. Pokud chceme vybrat více mincí na více adresách, můžeme adresy vybrat kliknutím levého tlačítka myši při držení klávesy command, poté kliknout pravým tlačítkem a vybrat "utratit z":

![obrázek](assets/36.webp)

Jakmile to uděláte, objeví se na spodní části okna peněženky zelený pruh ukazující počet vybraných mincí a celkovou dostupnou částku k utracení.

Můžete také utratit jednotlivé mince v rámci adresy a vyloučit ostatní na téže adrese, ale to se nedoporučuje, protože necháváte mince na adrese, která byla kryptograficky oslabena v důsledku utracení jedné z mincí (další důvod, proč nedávat více mincí na jednu adresu, kromě důvodů soukromí, je, že pokud utratíte jednu, měli byste je utratit všechny, což se stává zbytečně drahým). Zde je, jak vybrat jedinou minci z sdílené adresy, ale nedělejte to:

![obrázek](assets/37.webp)

Nyní máme vybrány dvě mince k utracení. Dále jsme se rozhodli, kam je utratit. Pošleme je na druhou adresu. Budeme potřebovat takto zkopírovat adresu:

![obrázek](assets/38.webp)

Poté jděte na záložku "Odeslat" a vložte druhou adresu do pole "platba pro". Není třeba přidávat popis; můžete, ale můžete to udělat později úpravou štítků. Pro částku vyberte "Max" pro utracení všech vybraných mincí. Poté klikněte na "Zaplatit" a poté klikněte na tlačítko "pokročilé" v pop-up okně, které se objeví.

![obrázek](assets/39.webp)

Vždy klikněte na "pokročilé" v této fázi, abychom získali jemnou kontrolu a přesně viděli, co je v transakci. Zde je transakce:

![obrázek](assets/40.webp)

Vidíme dvě vnitřní bílé okna/panely. Horní je okno vstupů (které mince jsou utraceny) a dolní je okno výstupů (kam mince jdou).

Poznámka, stav (vlevo nahoře) je zatím "nepodepsaný". "Odeslaná částka" je 0, protože mince jsou převáděny v rámci peněženky. Poplatek je 481 sats. Pozor, pokud by to bylo 480 sats, poslední nula by byla odstraněna, takto 0.0000048 a pro unavené oko to může vypadat jako 48 sats – buďte opatrní (něco, co by vývojáři Electrum měli opravit).
Velikost transakce se vztahuje na velikost dat v bytech, nikoli na množství bitcoinu. Funkce "replace by fee" je ve výchozím nastavení aktivní a umožňuje vám znovu odeslat transakci s vyšším poplatkem, pokud je to potřeba. LockTime vám umožňuje nastavit, kdy je transakce platná – s tím jsem si ještě nehrál, ale doporučuji to nepoužívat, pokud plně nerozumíte, co děláte, a nemáte praxi s malými částkami.

Dole máme nějaké sofistikované nástroje pro úpravu poplatku za těžbu. Pro interní převody stačí nastavit minimální poplatek 1 sat/byte. Stačí ručně zadat číslo do pole Cílový poplatek. Pro kontrolu vhodného poplatku pro externí platbu můžete navštívit https://mempool.space a zjistit, jak je mempool zaneprázdněn, a jsou zde zobrazeny některé doporučené poplatky.

![obrázek](assets/41.webp)

Vybral jsem 1 sat/byte.

V okně pro vstupy vidíme dva záznamy. První je dar 5000 sat. Na levé straně vidíme jeho transakční hash (který můžeme vyhledat na blockchainu). Vedle toho je „21“ – to značí, že je to výstup označený číslem 21 v této transakci (ve skutečnosti je to 22. výstup, protože první je označen nulou).

Je třeba si zde všimnout: UTXO existuje pouze uvnitř transakce. Abychom mohli UTXO utratit, musíme na něj odkázat a tento odkaz vložit do vstupu nové transakce. Výstupy se pak stanou novými UTXO a staré UTXO se stane STXO (Spotřebovaný transakční výstup).

Druhý řádek je dar 10 000 sat. Vedle transakčního hashe, ze kterého pochází, je „0“, protože je to první (a možná jediný) výstup této transakce.

V dolním okně vidíme naši adresu. Všimněte si, že celková částka vstupů se úplně neshoduje s celkovou částkou výstupů. Rozdíl jde těžaři. Těžař se dívá na rozdíl ve všech transakcích v bloku, který se snaží vytěžit, a přičte toto číslo ke své odměně. (Poplatky za těžbu jsou takto zcela odpojeny od řetězce transakcí a začínají nový život).

Pokud upravíme poplatek za těžbu, hodnota výstupu se automaticky změní.

> Je důležité si zde všimnout: Všimněte si barvy adres v okně transakce. Pamatujte, že zelené adresy jsou uvedeny na vaší kartě adres. Pokud je adresa zvýrazněna zeleně (nebo žlutě) v okně transakce, pak Electrum adresu rozpoznal jako jednu ze svých. Pokud adresa není zvýrazněna, jedná se o externí adresu (externí vůči aktuálně otevřené peněžence) a měli byste ji pečlivěji zkontrolovat.

Jakmile zkontrolujete vše v transakci a jste si jisti, že jste spokojeni s tím, které mince utrácíte a kam mince posíláte, můžete kliknout na „finalise“.

![obrázek](assets/42.webp)

Po kliknutí na „finalise“ již nemůžete provádět úpravy – pokud potřebujete, musíte toto zavřít a začít znovu. Všimněte si, že tlačítko „finalise“ se změnilo na „export“, a objevila se nová tlačítka: „save“, „combine“, „sign“ a „broadcast“. Tlačítko „broadcast“ je neaktivní, protože transakce je v této fázi nepodepsaná a tedy neplatná.

Jakmile kliknete na sign, pokud má vaše peněženka heslo, budete vyzváni k jeho zadání, a poté se stav (v pravém horním rohu) změní z „Unsigned“ na „Signed“. Poté bude tlačítko „Broadcast“ dostupné.
Po odeslání transakce můžete zavřít okno transakce. Pokud přejdete na záložku s adresami, uvidíte, že první adresa je prázdná a druhá adresa má 1 UTXO.
Poznámka: Všechny tyto změny uvidíte ještě předtím, než byla transakce zařazena do bloku, neboli "potvrzena". Důvodem je, že Electrum aktualizuje zůstatky/transakce na základě nejen dat blockchainu, ale také dat z mempoolu. Ne všechny peněženky to dělají.

Je třeba zdůraznit, že místo odeslání můžeme transakci uložit na později. Lze ji uložit buď v nepodepsaném nebo podepsaném stavu.

Klikněte na tlačítko "export" (paradoxně, NEklikejte na tlačítko "save"), a uvidíte několik možností. Transakce je zakódována textem, a proto ji lze uložit několika způsoby.

![obrázek](assets/43.webp)

Uložení do QR kódu je velmi zajímavé. Pokud toto zvolíte, objeví se QR kód:

![obrázek](assets/44.webp)

Poté můžete vyfotit QR kód. Existuje několik věcí, které s tím můžete dělat, ale prozatím řekněme, že jej později znovu načítáte do peněženky. Můžete zavřít Electrum, znovu načíst peněženku a přejít do menu Nástroje:

![obrázek](assets/45.webp)

To spustí kameru vašeho počítače. Pak ukážete kameře fotku QR kódu ve vašem telefonu, a toto načte transakci zpět přesně tak, jak jste ji nechali.

Není intuitivní, jak načíst uložené transakce, takže si to dobře zapamatujte. Načtení transakce není "nástroj", ale možnost je skryta v menu nástrojů (další věc, kterou by vývojáři Electra měli opravit).

Podobný proces je možný s transakcí uloženou jako soubor. Zkuste si s oběma metodami procvičit, a to v rámci téže peněženky. Zde to dále neproberu, ale můžete tuto funkci použít k předávání transakce mezi stejnou peněženkou na různých počítačích, mezi multisignaturními peněženkami a mezi hardwarovými peněženkami. Zde jsou nějaké instrukce.

Nyní se vraťme k tlačítku "save" – toto není způsob, jak uložit text transakce. To, co to ve skutečnosti dělá, je říct peněžence Electrum, aby na lokálním počítači rozpoznala tuto transakci jako odeslanou platbu. Pokud to uděláte omylem, uvidíte transakci s malou ikonou počítače. Můžete na transakci kliknout pravým tlačítkem a smazat ji – nebojte se, tímto způsobem nemůžete smazat bitcoiny. Electrum poté zapomene, že tato transakce kdy existovala, a "vrátí" sats zpět a zobrazí sats na správném místě, kde ve skutečnosti existují.

### Adresy pro vrácení peněz

Adresy pro vrácení peněz jsou zajímavé. Musíte rozumět UTXO, abyste pochopili toto vysvětlení. Pokud posíláte na adresu částku menší než UTXO, pak zbylé bitcoiny půjdou těžaři, pokud není určen výstup pro vrácení peněz.

Můžete mít UTXO 6.15 bitcoinu a chtít poslat 0.15 bitcoinu na podporu nějakých protestujících, kteří jsou utlačováni tyranskou "demokratickou" vládou někde ve světě. Potom byste vzali 6.15 bitcoinu (pomocí funkce "spend from" v Electrum) a vložili je do transakce.

Do pole "pay to" vložíte adresu protestujících, možná byste do pole "description" napsali "EndTheFed & WEF", a jako částku zadáte 0.15 bitcoinu a kliknete na "pay", poté "advanced".
Na obrazovce transakce, v okně pro vstup, uvidíte 6.15 bitcoinový UTXO. V okně pro výstup uvidíte adresu bez zvýraznění (to je adresa protestujících) s 0.15 bitcoinu vedle ní. Uvidíte také žlutou adresu s mírně méně než 6.0 bitcoinu. To je změnová adresa automaticky vybraná peněženkou z jedné z jejích vlastních žlutých změnových adres. Účelem změnové adresy je, aby peněženka mohla vkládat změnové mince do nich, aniž by to narušilo dostupnost přijímacích adres, pro které máte možná plány, nebo pro které jste vystavili faktury. Pokud mají být později použity zákazníky, například, nechcete, aby vaše peněženka je automaticky používala a zaplňovala je. Je to nepřehledné a špatné pro soukromí.
Všimněte si, že jak upravujete poplatek za těžbu, množství změny se automaticky upraví, nikoli částka platby.

### Ruční změna nebo platba mnoha

To je opravdu zajímavá funkce Electra. Přistupujete k ní takto.

![obrázek](assets/46.webp)

Poté můžete zadat více cílů pro UTXO zůstatek, který utrácíte, takto:

![obrázek](assets/47.webp)

Vložte adresu, napište čárku, pak mezeru, pak částku, pak <enter>, a opakujte. NEZADÁVEJTE ČÁSTKY DO OKNA “AMOUNT” – Electrum zde bude celkovou částku vyplňovat, jak budete zadávat jednotlivé částky do okna “Pay to”.

To vám umožní ručně určit, kam půjde změna (např. na konkrétní adresu ve vaší peněžence, nebo do jiné peněženky), nebo můžete zaplatit mnoha lidem najednou. Pokud váš celkový součet není dostatečně vysoký, aby odpovídal velikosti UTXO, Electrum pro vás stále vytvoří další výstup pro změnu.

Funkce Pay to Many také umožňuje možnost vytvořit vlastní “PayJoins” nebo “CoinJoins” – mimo rozsah tohoto článku, ale mám zde průvodce. (https://armantheparman.com/cj/)

## Peněženky

Chci demonstrovat Watching Only Wallet pomocí Electra. Abych to mohl udělat, musím nejprve definovat “peněženku”. Existují dva způsoby, jak se slovo “peněženka” používá v Bitcoinu:

- Typ A, “peněženka” – odkazuje na software, který vám ukazuje vaše adresy a zůstatky, např. Electrum, Blue Wallet, Sparrow Wallet atd.

- Typ B, “peněženka” – odkazuje na jedinečnou kolekci adres, které jsou spojeny s kombinací našeho seed_phrase/passphrase/derivation_path. V jakékoli peněžence je 8.6 miliardy adres (4.3 miliardy přijímacích adres a 4.3 miliardy změnových adres). Pokud změníte cokoli v seed phrase, passphrase, nebo derivation path, získáte nepoužitou peněženku s novými a všechny jedinečnými 8.6 miliardami prázdných adres.

Který typ někdo má na mysli, když používá slovo “peněženka”, je zřejmé z kontextu.

## Watching Wallet – cvičení

Není úplně zřejmé, k čemu je watching wallet, ale začnu vysvětlováním, co to je, jak si vytvořit cvičnou, a poté se k jejímu účelu vrátíme později, když budu vysvětlovat více o hardware peněženkách. (Pro podrobný přehled o tom, jak používat hardware peněženku a různé konkrétní značky, viz zde.)
Připravíme si ukázkovou běžnou peněženku (tentokrát přidáme trochu více složitosti s heslovou frází) a poté k ní příslušnou sledovací peněženku. Pokud chcete, můžete zkopírovat přesně tu, kterou jsem vytvořil já, nebo si vytvořit vlastní – tato peněženka má být zahozena; skutečně ji nepoužívejte. Začněte vygenerováním 12-slovného seedu pomocí webové stránky Ian Coleman.
Všimněte si 12 náhodných slov na níže uvedeném snímku obrazovky a toho, že jsem do pole pro heslovou frázi zadal heslovou frázi:

HESLOVÁ FRÁZE: „Craig Wright je lhář a podvodník a patří do vězení. Také Ross Ulbricht by měl být okamžitě propuštěn z vězení.“

Heslová fráze může být dlouhá až 100 znaků a ideálně by měla být jednoznačná a ne příliš krátká – Tato, kterou jsem použil, je jen pro zábavu – obecně doporučuji vyhnout se velkým písmenům a symbolům, aby se snížil váš stres při zkoušení kombinací, pokud byste někdy měli problém si heslovou frázi zapamatovat.

![obrázek](assets/48.webp)

Dále v Electrumu přejděte do menu soubor–>nový/obnovit. Zadejte jedinečný název pro vytvoření nové peněženky a klikněte na „další“.

![obrázek](assets/49.webp)

Další kroky byste už teď měli znát, takže je uvedu bez obrázků:

- Standardní peněženka
- Již mám seed
- Zkopírujte a vložte 12 slov do pole nebo je ručně napište.
- Klikněte na možnosti a vyberte BIP39, a také klikněte na zaškrtávací políčko heslové fráze („rozšířit tento seed vlastními slovy“)
- Zadejte svou heslovou frázi přesně tak, jak jste to udělali na stránce Ian Coleman
- Ponechte výchozí sémantiku skriptů a cestu derivace
- Není třeba přidávat heslo (zamyká peněženku)

Nyní se vraťte na stránku Ian Coleman, dolů do sekce „cesta derivace“ a klikněte na záložku „BIP 84“, abyste vybrali stejnou sémantiku skriptů jako výchozí v Electrumu (Native Segwit).

![obrázek](assets/50.webp)

Rozšířené soukromé a veřejné klíče jsou hned níže a mění se, když uděláte změny v cestě derivace (nebo cokoli jiného výše na stránce).

![obrázek](assets/51.webp)

Uvidíte také „BIP32 rozšířené soukromé/veřejné“ klíče – ty prozatím ignorujeme.

Rozšířený soukromý klíč účtu lze použít k úplné regeneraci vaší peněženky. Rozšířený veřejný klíč účtu však může vyprodukovat pouze omezenou verzi stejné peněženky (sledovací peněženka) – Pokud tento klíč vložíte do Electrumu, stále vyprodukuje všech 8,6 miliardy adres, které by seed nebo rozšířený soukromý klíč měly, ale Electrumu nebudou k dispozici žádné soukromé klíče, takže žádné výdaje nejsou možné. Udělejme to teď, abychom ukázali, o co jde:

Zkopírujte „rozšířený veřejný klíč účtu“ do schránky.

Poté přejděte do Electrumu, nechte otevřenou aktuální peněženku, kterou jsme vytvořili, a přejděte do souboru–>nový/obnovit. Proces vytvoření peněženky je trochu jiný než předtím:

- Standardní peněženka
- Použít hlavní klíč
- Vložte rozšířený veřejný klíč do pole a pokračujte
- Není třeba zadávat heslovou frázi; je již součástí rozšířeného veřejného klíče
- Není třeba zadávat sémantiku skriptů a cestu derivace
- Není třeba přidávat heslo (zamyká peněženku)

Když se peněženka načte, měli byste si všimnout, že jsou načteny přesně stejné adresy jako dříve, když byl zadán seed. Měli byste si také všimnout v horní části na titulní liště, že je napsáno „sledovací peněženka“. Tato peněženka vám může ukázat vaše adresy a zůstatky (kontrolou zůstatků prostřednictvím uzlu), ale nejste schopni podepisovat transakce (protože sledovací peněženka nemá soukromé klíče).
Tak jaký to má smysl?
Jedním z důvodů, a ne hlavním, je, že můžete potenciálně sledovat svou peněženku a její zůstatek na počítači, aniž byste vystavovali své soukromé klíče jakémukoli malwaru na počítači.

Dalším důvodem je, že je to POVINNÉ pro provedení plateb, pokud se rozhodnete uchovávat své soukromé klíče mimo počítač; vysvětlím:

> Hardware peněženky (HWW) byly vytvořeny tak, aby zařízení mohlo bezpečně držet vaše soukromé klíče (zamčené PINem), nikdy nevystavovalo klíče počítači (i když je připojeno k počítači kabelem) a samo o sobě nemohlo připojit se k internetu. Takové zařízení nemůže samo o sobě provádět transakce, protože všechny bitcoinové transakce začínají odkazem na UTXO(s) na blockchainu (který je na uzlu). Peněženka musí specifikovat, ve kterém transakčním ID se UTXO nachází, a který výstup transakce je ten, který má být utracen. Pouze po specifikaci vstupu může být vytvořena nová transakce, natož podepsána. Hardware peněženky nemohou vytvářet transakce, protože nemají přístup k žádným UTXO – nejsou s ničím spojeny! Obvykle je z HWW extrahován rozšířený veřejný klíč a adresy jsou pak zobrazeny na počítači – mnoho lidí bude znát software Ledger nebo Trezor Suite, který na jejich počítači zobrazuje adresy a zůstatky – to je sledovací peněženka. Tyto programy mohou vytvářet transakce, ale nemohou je podepsat. Mohou mít transakce podepsané pouze HWW, které jsou k nim připojeny. HWW převezme nově vytvořenou transakci od sledovací peněženky, podepíše ji a poté ji pošle zpět počítači k vysílání uzlu. HWW nemůže vysílat samostatně, to dělá jeho přidružená sledovací peněženka. Tímto způsobem spolupracují dvě peněženky (peněženka s veřejným klíčem na počítači a peněženka s soukromým klíčem v HWW) na generování, podepisování a vysílání, a to vše při zajištění, že soukromé klíče zůstanou izolované a daleko od zařízení připojeného k internetu.

## Částečně podepsané bitcoinové transakce (PSBTs)

Je možné, aby byla transakce vytvořena a uložena do souboru, později znovu načtena, podepsána, uložena, později znovu načtena a nakonec vysílána – neříkám, že by to někdo potřeboval dělat; je to jen něco, co je možné.

Nyní zvažte multisignature peněženku 3 z 5 – 5 soukromých klíčů vytváří peněženku, a 3 jsou potřebné k úplnému podepsání transakce (Zde se dozvíte více o klíčích multisignature peněženky). Je možné mít 5 různých počítačů, každý s jedním z pěti soukromých klíčů.

Počítač jedna by mohl generovat transakci a podepsat ji. Poté by ji mohl uložit do souboru a poslat e-mailem Počítači 2. Počítač 2 ji může poté podepsat a potenciálně uložit soubor do QR kódu a přenést QR prostřednictvím Zoom hovoru Počítači 3 na druhé straně světa. Počítač 3 může zachytit QR, načíst transakci do electrum a podepsat transakci. Po prvních 2 podpisech byla transakce PSBT (částečně podepsaná bitcoinová transakce). Po 3. podpisu se transakce stala plně podepsanou a platnou, připravenou k vysílání.

Chcete-li se dozvědět více o PSBTs, podívejte se na tento průvodce. (https://armantheparman.com/psbt/)

## Používání hardware peněženek s Electrum

Mám průvodce o používání hardware peněženek obecně, který bych považoval za důležité, aby si lidé, kteří jsou noví v HWWs, přečetli. (https://armantheparman.com/using-hwws/)
Najdete zde také průvodce různými značkami HWW připojenými k Sparrow Bitcoin Wallet. (https://armantheparman.com/hwws/)
Toto bude můj první průvodce, který ukazuje, jak používat hardware peněženku s Electrum – budu používat hardware peněženku ColdCard, abych to demonstroval. Není to myšleno jako podrobný průvodce specificky pro ColdCard, ten průvodce najdete zde. Ukazuji pouze specifika pro Electrum. (https://armantheparman.com/cc/)

### Připojení přes micro SD kartu (air-gapped)

Před připojením vaší skutečné peněženky přes ColdCard doufám, že jste provedli předchozí kroky načtení Electrum dummy peněženky a nastavení síťových parametrů.

Pak na ColdCard vložte SD kartu. Předpokládám, že jste již vytvořili svůj seed. Pokud přistupujete k peněžence s heslovou frází, aplikujte ji nyní. Rolujte dolů a vyberte v menu Pokročilé/Nástroje –> Exportovat peněženku –> Electrum peněženka.

Můžete rolovat dolů a číst zprávu. Vždy vám nabídne vybrat „1“ pro zadání nenulového čísla účtu (něco, co je součástí cesty derivace), ale pokud jste dodrželi mou radu, nezabývali jste se výchozími cestami derivace, takže nebudete chtít nenulové číslo účtu; stačí stisknout fajfku a pokračovat.

Poté vyberte sémantiku skriptu. Většina lidí bude vybírat „Native Segwit“.

Zobrazí se „Soubor peněženky Electrum byl zapsán“, a zobrazí se název souboru. Zapamatujte si ho.

Pak vyjměte micro SD kartu a vložte ji do počítače s Electrum.

Některé operační systémy automaticky otevřou průzkumníka souborů, když vložíte microSD. Mnoho lidí uvidí nový soubor peněženky a dvakrát na něj klikne, a diví se, proč to nefunguje. Není to skvělý design. Ve skutečnosti musíte ignorovat průzkumníka souborů (zavřít ho) a otevřít soubor peněženky pomocí Electrum:

Otevřete Electrum. Pokud je již otevřen s nějakou jinou peněženkou, vyberte soubor –> nový. Hledáme toto okno:

![image](assets/52.webp)

Tady je trik, není to intuitivní. Klikněte na „vybrat“. Pak navigujte v souborovém systému na microSD kartě a najděte soubor peněženky a otevřete ho.

Nyní jste otevřeli odpovídající sledovací peněženku vaší hardware peněženky. Skvělé.

### Připojení přes USB kabel.

Tento způsob by měl být jednodušší, ale pro počítače s Linuxem je to mnohem těžší. Je třeba aktualizovat něco, co se nazývá „Udev pravidla“. Jak na to (podrobný průvodce https://armantheparman.com/gpg-articles/ ), a stručně:

Je dobré se ujistit, že systém je aktualizovaný. Pak:

```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

pak...

```bash
python3 -m pip install ckcc-protocol
```

Pokud dostanete chybu, ujistěte se, že máte nainstalovaný pip. Můžete zkontrolovat s (pip –version), a můžete ho nainstalovat s (sudo apt install python3-pip)

Vytvořte nebo upravte existující soubor, /etc/udev/rules.d/

Takto:

```bash
sudo nano /etc/udev/rules.d
```

Otevře se textový editor. Zkopírujte text odtud a vložte ho do souboru rules.d, uložte a zavřete.

![image](assets/53.webp)

Pak postupně spusťte tyto příkazy:

```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```
Pokud dostanete zprávu "skupina plugdev" již existuje, je to v pořádku, pokračujte. Po druhém příkazu nedostanete žádnou zpětnou vazbu/odpověď, jen pokračujte k třetímu příkazu.
Možná budete muset zařízení ColdCard odpojit a poté znovu připojit k počítači.

Pokud i přes to všechno stále nemůžete zařízení ColdCard připojit, zkuste aktualizovat firmware (návod brzy, ale prozatím návod najdete na webových stránkách výrobce).

Dále vytvořte novou peněženku:

- Standardní peněženka
- Použít hardwarové zařízení
- Bude skenovat a detekovat vaše zařízení ColdCard. Pokračujte.
- Vyberte sémantiku skriptu a cestu derivace
- Rozhodněte, zda by soubor peněženky měl být šifrován (doporučeno)

### Transakce pomocí zařízení ColdCard

S připojeným kabelem jsou transakce snadné. Podpis transakcí bude plynulý.

Pokud používáte zařízení v režimu bez připojení k síti (air-gapped), musíte ručně přenášet uloženou transakci mezi zařízeními pomocí karty microSD. Existují určité triky.

Po vytvoření transakce a jejím finalizování musíte kliknout na tlačítko export v levém dolním rohu. Uvidíte "uložit do souboru", což je protiintuitivně to, co nechceme. Ve skutečnosti musíte nejprve přejít na úplně poslední možnost v menu, která říká "pro hardwarové peněženky", a pak, v rámci této volby, najít další "uložit do souboru" a vybrat to. Poté uložte soubor na kartu microSD, vyjměte kartu a vložte ji do zařízení ColdCard. Nezapomeňte, že možná budete muset použít heslovou frázi k výběru správné peněženky. Na obrazovce se zobrazí připraveno k podpisu. Klikněte na zaškrtávací políčko, prohlédněte si transakci a potvrďte kliknutím na zaškrtávací políčko. Až budete hotovi, vyjměte kartu a vložte ji zpět do počítače.

Poté musíme otevřít transakci pomocí Electrum. Funkce je skryta v menu nástroje -> načíst transakci. Projděte systém souborů a najděte soubor. Při každém podpisu budou vždy tři soubory. Původní uložený soubor, který vytvořila Sledující Peněženka, a dva vytvořené zařízením ColdCard (nevim proč to dělá). Jeden bude říkat "podepsáno" a druhý "konečné". Není to intuitivní, ale "podepsaný" soubor není užitečný, potřebujeme otevřít "konečnou" transakci.

Jakmile to načtete, můžete kliknout na "vysílat" a platba bude provedena.

## Aktualizace Electrum a skrytý adresář ".electrum"

Electrum žije na vašem počítači na dvou místech. Jedná se o samotnou aplikaci a o skrytou konfigurační složku. Tato složka se nachází na různých místech v závislosti na vašem operačním systému:

Windows:

> C:/Users/your_user_name_goes_here/AppData/Roaming/Electrum

Mac:

> /Users/your_user_name_goes_here/.electrum

Linux:

> /home/your_user_name_goes_here/.electrum

Všimněte si, že před "electrum" v Linuxu a Macu je tečka – to značí, že adresář je skrytý. Také si všimněte, že tento adresář je vytvořen (automaticky) až při prvním spuštění Electrum. Adresář obsahuje konfigurační soubor Electrum a také adresář, který obsahuje všechny vaše uložené peněženky.

Pokud odstraníte program Electrum z vašeho počítače, skrytý adresář zůstane, pokud ho aktivně také neodstraníte.
Pro aktualizaci Electra postupujte stejným způsobem, jaký jsem popsal na začátku pro stažení a ověření. Poté budete mít na počítači dvě kopie programu a můžete spustit kteroukoli – každý program bude přistupovat ke stejné skryté složce electrum pro svou konfiguraci a přístup k peněžence. Vše, co jsme uložili, jako je základní jednotka, výchozí uzel pro připojení, další preference a přístup k peněženkám, zůstane, protože vše je uloženo v této složce.
### Přesun vašeho Electra a peněženek na jiný počítač

K tomu můžete zkopírovat soubory programu na USB disk a také zkopírovat adresář .electrum. Poté je zkopírujte nebo přesuňte na nový počítač. Program nemusíte znovu ověřovat. Nezapomeňte zkopírovat adresář .electrum na výchozí místo (pamatujte, že ho musíte zkopírovat PŘED prvním spuštěním Electra na tom počítači, jinak bude vyplněna prázdná výchozí složka .electrum a můžete být zmateni).

## Popisky

Jak jsem vysvětlil dříve, na záložce s adresami je sloupec s popisky. Můžete tam dvakrát kliknout a zadat poznámky pro sebe (jsou pouze na vašem počítači, nejsou veřejné a nejsou na blockchainu).

![obrázek](assets/54.webp)

Při přesunu vaší peněženky Electrum na jiný počítač možná nebudete chtít ztratit všechny tyto poznámky. Můžete je zálohovat do souboru pomocí nabídky, peněženka–> popisky –>export, a poté na novém počítači použít peněženka–>popisky–>import.

## Tip:

Pokud shledáváte tento zdroj užitečným a chtěli byste podpořit to, co dělám pro Bitcoin, můžete zde darovat nějaké satoshi:

Statická Lightning adresa: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/