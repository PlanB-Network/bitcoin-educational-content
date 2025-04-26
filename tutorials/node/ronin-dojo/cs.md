---
name: RoninDojo

description: Instalace a používání vašeho Bitcoinového uzlu RoninDojo.
---
***VAROVÁNÍ:** Po zatčení zakladatelů peněženky Samourai a zabavení jejich serverů dne 24. dubna jsou některé funkce RoninDojo, jako je Whirlpool, již nefunkční. Je však možné, že tyto nástroje budou v nadcházejících týdnech obnoveny nebo spuštěny jinak. Jelikož byl kód RoninDojo hostován na GitLabu Samourai, který byl také zabaven, v současné době není možné kód stáhnout na dálku. Týmy RoninDojo pravděpodobně pracují na znovuzveřejnění kódu.*

_Sledujeme vývoj této kauzy stejně jako vývoj s ním spojených nástrojů. Ujistěte se, že tento návod aktualizujeme, jakmile budou k dispozici nové informace._

_Tento návod je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je zodpovědností každého uživatele dodržovat zákony ve své jurisdikci._

_Tento návod je věnován instalaci RoninDojo v1. Pro využití nejnovějších vylepšení a funkcí vřele doporučuji konzultovat náš návod věnovaný přímé instalaci RoninDojo v2 na vašem Raspberry Pi:_ https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Provozování a používání vlastního uzlu je zásadní pro skutečnou účast na Bitcoinové síti. Ačkoli provoz Bitcoinového uzlu nepřináší uživateli žádné finanční výhody, umožňuje mu zachovat soukromí, jednat nezávisle a mít kontrolu nad svou důvěrou v síť.

V tomto článku se podrobně podíváme na RoninDojo, skvělé řešení pro provozování vlastního Bitcoinového uzlu.

### Obsah:

- Co je RoninDojo?
- Jaký hardware vybrat?
- Jak nainstalovat RoninDojo?
- Jak používat RoninDojo?
- Závěr

Pokud nejste obeznámeni s tím, jak Bitcoinový uzel funguje a jakou má roli, doporučuji začít čtením tohoto článku: Bitcoinový uzel - Část 1/2: Technické koncepty.

![Samourai](assets/1.webp)

## Co je RoninDojo?

Dojo je plný server Bitcoinového uzlu vyvinutý týmem peněženky Samourai. Můžete jej volně nainstalovat na jakékoli zařízení.

RoninDojo je asistent pro instalaci a nástroj pro správu Dojo a různých dalších nástrojů. RoninDojo přebírá původní implementaci Dojo a přidává k ní mnoho dalších nástrojů, zatímco zároveň usnadňuje instalaci a správu.

Nabízejí také "plug-and-play" hardware, RoninDojo Tanto, s předinstalovaným RoninDojo na stroji sestaveném jejich týmem. Tanto je placené řešení, vhodné pro ty, kteří si nechtějí špinit ruce.

Kód pro RoninDojo je open-source, takže je také možné toto řešení nainstalovat na vlastní hardware. Tato možnost je cenově výhodná, ale vyžaduje trochu více manipulace, což uděláme v tomto článku.

RoninDojo je Dojo, takže umožňuje snadnou integraci Whirlpool CLI do vašeho Bitcoinového uzlu pro co nejlepší zážitek CoinJoin. S Whirlpool CLI nejenže můžete nechat vaše bitcoiny remixovat 24/7 bez nutnosti nechat zapnutý osobní počítač, ale také výrazně zlepšit vaše soukromí.
RoninDojo integruje mnoho dalších nástrojů, které spoléhají na váš Dojo, jako je například kalkulačka Boltzmann, která určuje úroveň soukromí transakce, Electrum server pro připojení vašich různých Bitcoin peněženek k vašemu uzlu, nebo Mempool server pro soukromé sledování vašich transakcí. Ve srovnání s jiným řešením uzlu, jako je Umbrel, který jsem vám představil v tomto článku, je RoninDojo hluboce zaměřen na řešení a nástroje "On Chain", které optimalizují soukromí uživatele. Proto RoninDojo neumožňuje interakci se sítí Lightning Network.
RoninDojo nabízí méně nástrojů ve srovnání s Umbrelem, ale několik zásadních funkcí pro Bitcoinera, které jsou na Roninu přítomny, je neuvěřitelně stabilních.

Pokud tedy nepotřebujete všechny funkce serveru Umbrel a chcete pouze jednoduchý a stabilní uzel s několika zásadními nástroji jako Whirlpool nebo Mempool, pak je RoninDojo pravděpodobně dobrým řešením pro vás.

Podle mého názoru je vývojové zaměření Umbrelu silně orientováno na síť Lightning Network a univerzální nástroje. Stále jde o Bitcoin uzel, ale cílem je udělat z něj multitaskingový mini-server. Naopak, vývojové zaměření RoninDojo je více v souladu s týmy u Samourai Wallet a soustředí se na zásadní nástroje pro Bitcoinera, což umožňuje plnou nezávislost a optimalizované řízení soukromí na Bitcoinu.

Vezměte prosím na vědomí, že nastavení uzlu RoninDojo je o něco složitější než nastavení uzlu Umbrel.

Nyní, když jsme si vytvořili představu o RoninDojo, pojďme se podívat, jak tento uzel společně nastavit.

## Jaký hardware vybrat?

Pro výběr stroje, který bude hostit a provozovat RoninDojo, máte několik možností.

Jak bylo vysvětleno dříve, nejjednodušší volbou je objednat si Tanto, plug-and-play stroj navržený speciálně pro tento účel. Pro objednání vašeho přejděte sem: [odkaz](https://shop.ronindojo.io/product-category/nodes/).

Vzhledem k tomu, že týmy RoninDojo produkují open-source kód, je také možné implementovat RoninDojo na jiných strojích. Nejnovější verze instalačního průvodce najdete na této stránce: [odkaz](https://ronindojo.io/en/downloads.html), a nejnovější verze kódu na této stránce: [odkaz](https://code.samourai.io/ronindojo/RoninDojo).

Osobně jsem ho nainstaloval na Raspberry Pi 4 8GB a vše funguje perfektně.

Nicméně, vezměte prosím na vědomí, že týmy RoninDojo uvádějí, že často dochází k problémům s pouzdrem a adaptérem SSD. Proto se nedoporučuje používat pro SSD vašeho stroje pouzdro s kabelem. Místo toho je preferováno použití karty pro rozšíření úložiště speciálně navržené pro vaši základní desku, jako je tato: Karta pro rozšíření úložiště Raspberry Pi 4.

Zde je příklad, jak nastavit váš vlastní uzel RoninDojo:

- Raspberry Pi 4.
- Pouzdro s ventilátorem.
- Kompatibilní karta pro rozšíření úložiště.
- Napájecí kabel.
- Průmyslová micro SD karta o kapacitě 16GB nebo více.
- SSD o kapacitě 1TB nebo větší.
- Ethernetový kabel RJ45, doporučena kategorie 8.

## Jak nainstalovat RoninDojo?

### Krok 1: Příprava bootovatelné micro SD karty.

Jakmile máte svůj stroj sestavený, můžete začít s instalací RoninDojo. Začněte vytvořením bootovatelné micro SD karty vypálením příslušného diskového obrazu na ni.

Vložte vaši micro SD kartu do vašeho osobního počítače, poté přejděte na oficiální webové stránky RoninDojo a stáhněte si diskový obraz RoninOS: https://ronindojo.io/en/downloads.html.
Stáhněte si obraz disku, který odpovídá vašemu hardware. V mém případě jsem stáhl obraz "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ":
![Stáhnout obraz disku RoninOS](assets/2.webp)

Jakmile je obraz stažen, ověřte jeho integritu pomocí odpovídajícího souboru .SHA256. V tomto článku podrobně popíšu, jak to udělat: Jak ověřit integritu softwaru Bitcoinu na Windows?

Specifické pokyny pro ověření integrity RoninOS jsou také dostupné na této stránce: https://wiki.ronindojo.io/en/extras/verify.

Pro vypálení tohoto obrazu na vaši micro SD kartu můžete použít software jako je Balena Etcher, který si můžete stáhnout zde: https://www.balena.io/etcher/.

Provedete to tak, že v Etcheru vyberete obraz a vypálíte ho na micro SD kartu:

![Vypálit obraz disku s Etcherem](assets/3.webp)

Jakmile je operace dokončena, můžete vložit bootovatelnou micro SD kartu do Raspberry Pi a zapnout stroj.

### Krok 2: Konfigurace RoninOS.

RoninOS je operační systém vašeho uzlu RoninDojo. Jedná se o modifikovanou verzi Manjara, distribuce Linuxu. Po spuštění stroje a několikaminutovém čekání můžete začít s jeho konfigurací.

Pro vzdálené připojení k němu budete potřebovat najít IP adresu vašeho stroje RoninDojo. To můžete udělat například připojením k administračnímu panelu vašeho internetového boxu, nebo také můžete stáhnout software jako https://angryip.org/ pro skenování vaší lokální sítě a nalezení IP stroje.

Jakmile máte IP, můžete převzít kontrolu nad vaším strojem z jiného počítače připojeného k téže lokální síti pomocí SSH.

Z počítače běžícího na macOS nebo Linuxu jednoduše otevřete terminál. Z počítače běžícího na Windows můžete použít specializovaný nástroj jako Putty nebo přímo použít Windows PowerShell.

Jakmile je terminál otevřen, napište následující příkaz:

> ssh root@192.168.?.?

Jednoduše nahraďte dva otazníky IP adresou vašeho dříve nalezeného RoninDojo.
Tip: V Shellu klikněte pravým tlačítkem pro vložení položky.

Dále se dostanete na ovládací panel Manjara. Vyberte správné rozložení klávesnice pomocí šipek pro změnu cíle v rozbalovacím seznamu.

![Konfigurace klávesnice Manjaro](assets/4.webp)

Vyberte uživatelské jméno a heslo pro vaši relaci. Použijte silné heslo a bezpečně si ho zazálohujte. Můžete volitelně použít slabé heslo během instalace a později ho snadno změnit "kopírováním a vkládáním" do RoninUI. To vám umožní použít velmi silné heslo bez nutnosti trávit příliš mnoho času ručním psaním během nastavování Manjara.

![Konfigurace uživatelského jména Manjaro](assets/5.webp)

Dále budete také požádáni o výběr hesla pro root. Pro heslo roota zadejte přímo silné heslo. Nebudete ho moci změnit z RoninUI. Také si bezpečně zazálohujte toto heslo roota.

Poté zadejte svou polohu a časovou zónu.

![Konfigurace časové zóny Manjaro](assets/6.webp)

![Konfigurace polohy Manjaro](assets/7.webp)

Dále vyberte hostname.

![Konfigurace hostname Manjaro](assets/8.webp)

Nakonec ověřte informace o konfiguraci Manjara a potvrďte.

![Ověření informací o konfiguraci ManjaroOS](assets/9.webp)

### Krok 3: Stáhnout RoninDojo.
Počáteční konfigurace RoninOS bude provedena. Jakmile bude dokončena, jak je vidět na screenshotu výše, stroj se restartuje. Počkejte několik okamžiků, poté zadejte následující příkaz, abyste se znovu připojili k vašemu stroji RoninDojo:
> ssh username@192.168.?.?

Jednoduše nahraďte "username" uživatelským jménem, které jste si dříve vybrali, a otazníky nahraďte IP adresou vašeho RoninDojo.

Poté zadejte své uživatelské heslo.

V terminálu to bude vypadat takto:

![SSH Connection to RoninOS](assets/10.webp)

Nyní jste připojeni k vašemu stroji, na kterém je aktuálně pouze RoninOS. Nyní potřebujete na něm nainstalovat RoninDojo.

Stáhněte si nejnovější verzi RoninDojo zadáním následujícího příkazu:

> git clone https://code.samourai.io/ronindojo/RoninDojo

Stahování bude rychlé. V terminálu uvidíte toto:

![Cloning RoninDojo](assets/11.webp)

Počkejte, až stahování skončí, poté nainstalujte a přistupte k uživatelskému rozhraní RoninDojo pomocí následujícího příkazu:

> ~/RoninDojo/ronin

Budete vyzváni k zadání vašeho uživatelského hesla:

![Bitcoin Node Password Verification](assets/12.webp)

Tento příkaz je nutný pouze při prvním přístupu k vašemu RoninDojo. Poté, abyste přistoupili k RoninCLI přes SSH, budete jednoduše potřebovat zadat příkaz [SSH username@192.168.?.?] nahrazením "username" vaším uživatelským jménem a zadáním IP adresy vašeho uzlu. Budete vyzváni k zadání vašeho uživatelského hesla.

Dále uvidíte tuto úžasnou animaci:

![RoninCLI launch animation](assets/13.webp)

Poté konečně dorazíte na uživatelské rozhraní RoninDojo CLI.

### Krok 4: Instalace RoninDojo.

V hlavním menu navigujte pomocí šipek na klávesnici do menu "System". Stiskněte klávesu enter pro potvrzení vašeho výběru.

![RoninCLI navigation menu to System](assets/14.webp)

Poté přejděte do menu "System Setup & Install".

![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)

Nakonec zaškrtněte "System Setup" a "Install RoninDojo" pomocí mezerníku, poté vyberte "Accept" pro zahájení instalace.

![RoninDojo installation confirmation](assets/16.webp)

Nechte instalaci probíhat v klidu. V mém případě to trvalo asi 2 hodiny. Během procesu nechte terminál otevřený.

Občas zkontrolujte svůj terminál, protože budete v určitých fázích instalace vyzváni k stisknutí klávesy, jako zde například:

![RoninDojo installation in progress](assets/17.webp)

Na konci instalace uvidíte start různých kontejnerů:

![Node container startup](assets/18.webp)

Poté se váš uzel restartuje. Připojte se znovu k RoninCLI pro další krok.

![Bitcoin node restart](assets/19.webp)

### Krok 5: Stáhněte řetězec proof-of-work a přistupte k RoninUI.

Po dokončení instalace začne váš uzel stahovat Bitcoinový řetězec proof-of-work. Toto se nazývá Initial Block Download (IBD). Obvykle to trvá mezi 2 a 14 dny v závislosti na vašem internetovém připojení a zařízení.

Pokrok stahování řetězce můžete sledovat přístupem k webovému rozhraní RoninUI.

Pro přístup z lokální sítě zadejte do adresního řádku vašeho prohlížeče:

- Buď přímo zadejte IP adresu vašeho stroje (192.168.?.?)

- Nebo zadejte: ronindojo.local
Nezapomeňte vypnout svůj VPN, pokud jej používáte.
### Možný zvrat

Pokud se nemůžete připojit k RoninUI z vašeho prohlížeče, zkontrolujte správnou funkčnost aplikace z vašeho Terminálu připojeného k vašemu uzlu přes SSH. Připojte se k hlavnímu menu následováním předchozích kroků:

- Napište: SSH username@192.168.?.? a nahraďte svými přihlašovacími údaji.

- Zadejte své uživatelské heslo.

Až se dostanete do hlavního menu, přejděte na:

> RoninUI > Restart

Pokud aplikace restartuje správně, je problém s připojením z vašeho prohlížeče. Zkontrolujte, že nepoužíváte VPN a ujistěte se, že jste připojeni ke stejné síti jako váš uzel.

Pokud restart vyvolá chybu, zkuste aktualizovat operační systém a poté RoninUI znovu nainstalovat. Pro aktualizaci OS:

> System > Software Updates > Update Operating System

Po dokončení aktualizace a restartu se znovu připojte k vašemu uzlu přes SSH a znovu nainstalujte RoninUI:

> RoninUI > Re-install

Po znovu stažení RoninUI zkuste se připojit k RoninUI přes váš prohlížeč.

> Tip: Pokud omylem opustíte RoninCLI a ocitnete se na terminálu Manjaro, jednoduše zadejte příkaz "ronin", abyste se přímo vrátili do hlavního menu RoninCLI.

### Přihlášení na webu

Můžete se také přihlásit k webovému rozhraní RoninUI z jakékoli sítě pomocí Tor. Pro toto získejte Tor adresu vašeho RoninUI z RoninCLI:

> Credentials > Ronin UI

Získejte Tor adresu končící na .onion a poté se přihlaste do Ronin UI zadáním této adresy do vašeho Tor prohlížeče. Buďte opatrní, abyste nevystavili různé přihlašovací údaje, jelikož jde o citlivé informace.

![RoninUI webové přihlašovací rozhraní](assets/20.webp)

Po přihlášení budete vyzváni k zadání vašeho uživatelského hesla. Je to stejné heslo, které používáte pro přihlášení přes SSH.

![RoninUI webové rozhraní správcovského panelu](assets/21.webp)

Zde můžeme sledovat průběh IBD (Initial Block Download). Buďte trpěliví, stahujete všechny transakce provedené na Bitcoinu od 3. ledna 2009.

Po stažení celého blockchainu indexer kompaktuje databázi. Tato operace trvá asi 12 hodin. Můžete také sledovat její průběh pod "Indexer" v RoninUI.

Váš uzel RoninDojo bude po tomto plně funkční:

![Indexer synchronizován na 100% funkční uzel](assets/22.webp)

Pokud chcete změnit uživatelské heslo na silnější, můžete tak učinit nyní z karty "Settings". Na RoninDojo neexistuje žádná další bezpečnostní vrstva, proto doporučuji vybrat si opravdu silné heslo a postarat se o jeho zálohu.

## Jak používat RoninDojo?

Jakmile je řetězec stažen a kompaktován, můžete začít využívat služeb nabízených vaším novým uzlem RoninDojo. Podívejme se, jak je používat.

### Připojení softwaru peněženky k electrs.

První užitečnost vašeho nově nainstalovaného a synchronizovaného uzlu bude vysílání vašich transakcí do Bitcoinové sítě. Pravděpodobně budete chtít připojit různý software pro správu peněženek k němu.

Můžete to udělat pomocí Electrum Rust Server (electrs). Aplikace je obvykle předinstalována na vašem uzlu RoninDojo. Pokud ne, můžete ji ručně nainstalovat z rozhraní RoninCLI.

Jednoduše přejděte na:

> Applications > Manage Applications > Install Electrum Server

Pro získání Tor adresy vašeho Electrum Serveru, z menu RoninCLI, přejděte na:

> Credentials > Electrs
Stačí zadat .onion odkaz do vašeho peněženkového softwaru. Například ve Sparrow Wallet, jděte na záložku:
> Soubor > Předvolby > Server

V typu serveru vyberte "Private Electrum", poté zadejte Tor adresu vašeho Electrum Serveru do příslušného pole. Nakonec klikněte na "Testovat spojení" pro test a uložení vašeho spojení.

![Rozhraní pro připojení Sparrow Wallet k electrs](assets/23.webp)

### Připojení softwaru peněženky k Samourai Dojo.

Místo použití Electrs, můžete také použít Samourai Dojo pro připojení vaší kompatibilní softwarové peněženky k vašemu uzlu RoninDojo. Například Samourai Wallet nabízí tuto možnost.

Pro toto připojení jednoduše naskenujte QR kód spojení vašeho Dojo. Pro přístup k němu z RoninUI, klikněte na záložku "Dashboard" a poté na tlačítko "Spravovat" v okně vašeho Dojo. Poté uvidíte QR kódy pro spojení vašeho Dojo a BTC-RPC Exploreru. Pro jejich zobrazení klikněte na "Zobrazit hodnoty".

![Načítání QR kódu pro spojení s Dojo](assets/24.webp)

Pro připojení vaší Samourai Wallet k vašemu Dojo budete potřebovat naskenovat tento QR kód během instalace aplikace:

![Připojení k Dojo z aplikace Samourai Wallet](assets/25.webp)

### Používání vlastního Mempool Exploreru.

Nepostradatelný nástroj pro Bitcoinery, explorer umožňuje kontrolovat různé informace o Bitcoinovém řetězci. S Mempool, například, můžete v reálném čase kontrolovat poplatky aplikované ostatními uživateli, aby jste mohli případně upravit ty vaše. Také můžete kontrolovat stav potvrzení jedné z vašich transakcí nebo zobrazit zůstatek adresy.

Tyto nástroje exploreru vás mohou vystavit rizikům soukromí a vyžadují, abyste důvěřovali databázi třetí strany. Když používáte tento online nástroj bez procházení vaším vlastním uzlem:

- Riskujete únik informací o vaší peněžence.

- Důvěřujete správci webové stránky pro řetězec proof-of-work, který hostují.

Aby jste se vyhnuli těmto rizikům, můžete použít vlastní instanci Mempool na vašem uzlu prostřednictvím sítě Tor. S tímto řešením nejenže chráníte své soukromí při používání služby, ale také již nemusíte důvěřovat poskytovateli, protože dotazujete vaši vlastní databázi.

Pro toto začněte instalací Mempool Space Visualizer z RoninCLI:

> Aplikace > Spravovat aplikace > Instalovat Mempool Space Visualizer

Po instalaci získejte odkaz na váš Mempool. Tor adresa vám umožní přístup k němu z jakékoli sítě. Podobně, získáme tento odkaz přes RoninCLI:

> Přihlašovací údaje > Mempool

![Načtení Tor adresy Mempool](assets/26.webp)

Stačí zadat vaši Tor adresu Mempool do prohlížeče Tor, abyste si užili vlastní instanci Mempool, založenou na vašich vlastních datech. Doporučuji přidat tuto Tor adresu do oblíbených pro rychlejší přístup. Také můžete vytvořit zástupce na vaší ploše.

![Rozhraní Mempool Space](assets/27.webp)

Pokud ještě nemáte prohlížeč Tor, můžete si ho stáhnout zde: https://www.torproject.org/download/

Také k němu můžete přistupovat z vašeho smartphonu instalací prohlížeče Tor a zadáním stejné adresy. Odkudkoli můžete sledovat stav Bitcoinového řetězce pomocí vašeho vlastního uzlu.

### Používání Whirlpool CLI.

Váš uzel RoninDojo také zahrnuje WhirlpoolCLI, vzdálené rozhraní příkazové řádky pro automatizaci míchání Whirlpool.
Když provádíte CoinJoin s implementací Whirlpool, aplikace, kterou používáte, musí zůstat otevřená, aby mohla provádět míchání a opětovné míchání. Tento proces může být pro uživatele, kteří chtějí dosáhnout vysoké úrovně anonymity, zdlouhavý, protože zařízení, na kterém je aplikace s Whirlpool spuštěná, musí zůstat neustále zapnuté. V praxi to znamená, že pokud chcete zapojit vaše UTXO do nepřetržitých remixů 24/7, budete muset neustále nechat zapnutý váš osobní počítač nebo telefon s otevřenou aplikací.
Jedním řešením tohoto omezení je použití WhirlpoolCLI na stroji, který má být neustále zapnutý, například na Bitcoinovém uzlu. S tím mohou být naše UTXO remixovány 24/7 bez nutnosti nechat běžet jiné zařízení než náš Bitcoinový uzel.
WhirlpoolCLI se používá s WhirlpoolGUI, grafickým rozhraním, které se instaluje na osobní počítač pro snadnou správu Coinjoinů. V tomto článku podrobně vysvětlím, jak nastavit Whirlpool CLI s vaším vlastním dojo: [odkaz](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).

Pokud se chcete dozvědět více o Coinjoin obecně, vše vysvětluji v tomto článku: [odkaz](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).

### Použití nástroje Whirlpool Stat Tool.

Po provedení CoinJoinů s Whirlpool možná budete chtít znát skutečnou úroveň soukromí vašich smíchaných UTXO. Nástroj Whirlpool Stat Tool vám to umožní snadno zjistit. S tímto nástrojem můžete vypočítat perspektivní skóre a retrospektivní skóre vašich smíchaných UTXO. Doporučuji přečíst si tuto sekci, abyste se dozvěděli více o výpočtu těchto Anon Sets a jak fungují: [odkaz](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).

Nástroj je předinstalován na vašem RoninDojo. Zatím je dostupný pouze z RoninCLI. Pro jeho spuštění z hlavního menu přejděte na:

> Samourai Toolkit > Whirlpool Stat Tool

Zobrazí se pokyny k použití. Po dokončení stiskněte libovolnou klávesu pro přístup k příkazovým řádkům:

![Domovská stránka softwaru Whirlpool Stats Tool](assets/28.webp)

Zobrazí se terminál:

> wst#/tmp>

Pro ukončení tohoto rozhraní a návrat do menu RoninCLI jednoduše zadejte příkaz:

> quit

Na začátku nastavíme proxy na Toru, abychom mohli s úplným soukromím extrahovat data OXT. Zadejte příkaz:

> socks5 127.0.0.1:9050

Poté stáhněte data z poolu, který obsahuje vaši transakci:

> download 0001
>
> Nahraďte 0001 kódem denominace poolu, který vás zajímá.

Kódy denominací na WST jsou následující:

- Pool 0.5 bitcoinů: 05

- Pool 0.05 bitcoinů: 005

- Pool 0.01 bitcoinů: 001

- Pool 0.001 bitcoinů: 0001
![Stahování dat z poolu 0001 z OXT](assets/29.webp)
Jakmile jsou data stažena, načtěte je příkazem:

> load 0001
>
> Nahraďte 0001 kódem poolu, který vás zajímá.

![Načítání dat z poolu 0001](assets/30.webp)
Nechte proběhnout proces načítání, může to trvat několik minut. Po načtení dat zadejte příkaz score následovaný vaším TXID (identifikátorem transakce) pro získání Anon Sets:

> score TXID
>
> Nahraďte TXID identifikátorem vaší transakce.

![Tisk předpokládaných a retrospektivních skóre daného TXID](assets/31.webp)

WST poté zobrazí retrospektivní skóre (metriky zpětného pohledu) následované prospektivním skóre (metriky vpřed hledící). Kromě skóre Anon Sets WST také poskytuje míru rozptylu vašeho výstupu v poolu na základě anon setu.

Vezměte prosím na vědomí, že prospektivní skóre vašeho UTXO je vypočítáno na základě TXID vašeho počátečního míchání, nikoli vašeho posledního míchání. Naopak, retrospektivní skóre UTXO je vypočítáno na základě TXID posledního cyklu.

Pokud znovu nerozumíte těmto konceptům Anon Sets, doporučuji přečíst si tuto část mého článku o Coinjoin, kde vše vysvětluji podrobně s diagramy: [https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)

### Použití kalkulačky Boltzmann.

Kalkulačka Boltzmann je nástroj, který vám umožní snadno vypočítat různé pokročilé metriky Bitcoin transakce, včetně její úrovně entropie. Všechna tato data vám umožní kvantifikovat úroveň soukromí transakce a detekovat jakékoli potenciální chyby. Tento nástroj je předinstalován na vašem uzlu RoninDojo.

Pro přístup k němu z RoninCLI se připojte přes SSH, poté přejděte do menu:

> Samourai Toolkit > Boltzmann Calculator

Než vysvětlím, jak jej používat na RoninDojo, vysvětlím, co tyto metriky představují, jak jsou vypočítány a k čemu slouží.

Tyto ukazatele lze použít pro jakoukoli Bitcoin transakci, ale jsou obzvláště zajímavé pro studium kvality transakce Coinjoin.

1. První ukazatel, který tento software vypočítá, je počet možných kombinací. Je označen na kalkulačce jako "nb combinations". Vzhledem k hodnotám UTXO tento ukazatel představuje počet možných mapování vstupů na výstupy.

> Pokud nejste obeznámeni s termínem "UTXO", doporučuji přečíst si tento krátký článek: Mechanismus Bitcoin transakce: UTXO, vstupy a výstupy.

Jinými slovy, tento ukazatel představuje počet možných interpretací dané transakce. Například struktura Coinjoin Whirlpool 5x5 bude mít počet možných kombinací rovný 1496:

![Schéma transakce Coinjoin na kycp.org](assets/32.webp)

Kredit: KYCP
2. Druhým vypočítaným ukazatelem je entropie transakce. Vzhledem k tomu, že počet možných kombinací pro transakci může být velmi vysoký, může být místo toho využita entropie. Entropie představuje binární logaritmus počtu možných kombinací. Její vzorec je následující:
- E: entropie transakce.
- C: počet možných kombinací pro transakci.

> E = log2(C)

V matematice je binární logaritmus (základ 2) inverzní funkcí funkce mocniny 2. Jinými slovy, binární logaritmus x je mocnina, na kterou musí být číslo 2 zvýšeno, aby byla získána hodnota x.

Takže:

> E = log2(C)
> C = 2^E

Tento ukazatel je vyjádřen v bitech. Například zde je výpočet entropie transakce Whirlpool 5x5 Coinjoin, s dříve zmíněným počtem možných kombinací rovným 1496:

> C = 1496
>
> E = log2(1496)
>
> E = 10.5469 bitů

Tato Coinjoin transakce má tedy entropii 10.5469 bitů, což je velmi dobré.

Čím vyšší tento ukazatel je, tím více různých interpretací transakce existuje a tím je transakce důvěrnější.

Pojďme se podívat na další příklad. Zde je "klasická" transakce, která má jeden vstup a dva výstupy:

![Schéma Bitcoin transakce na oxt.me](assets/34.webp)

Kredit: OXT

Tato transakce má pouze jednu možnou interpretaci:

> [(inp 0) > (Outp 0 ; Outp 1)]

Takže její entropie bude rovna 0:

> C = 1
>
> E = log2(C)
>
> E = 0

3. Třetím ukazatelem, který Boltzmannova kalkulačka vrací, je efektivita Tx nazývaná "Efektivita peněženky". Tento ukazatel jednoduše umožňuje porovnat vstupní transakci s nejlepší možnou transakcí ve stejné konfiguraci.

Nyní představíme koncept maximální entropie, který představuje nejvyšší dosažitelnou entropii pro danou strukturu transakce. Například struktura Whirlpool 5x5 Coinjoin bude mít maximální entropii 10.5469. Ukazatel efektivity porovnává tuto maximální entropii s aktuální entropií vstupní transakce. Jeho vzorec je následující:

- ER: Aktuální entropie vyjádřená v bitech.
- EM: Maximální entropie se stejnou strukturou vyjádřená v bitech.
- Ef: Efektivita vyjádřená v bitech.

> Ef = ER - EM
>
> Ef = 10.5469 - 10.5469
>
> Ef = 0 bitů

Tento ukazatel je také vyjádřen jako procento, takže vzorec se stává:

- CR: Aktuální počet možných kombinací.
- CM: Maximální počet možných kombinací se stejnou strukturou.
- Ef: Efektivita vyjádřená jako procento.

> Ef = CR/CM
>
> Ef = 1496/1496
>
> Ef = 100%

Efektivita 100% znamená, že tato transakce má nejvyšší možnou soukromí vzhledem k její struktuře.

4. Čtvrtým vypočítaným ukazatelem je hustota entropie. Umožňuje nám vztáhnout entropii ke každému vstupu nebo výstupu. Tento ukazatel lze použít k porovnání efektivity mezi transakcemi různých velikostí.

Jeho výpočet je velmi jednoduchý: entropii transakce dělíme počtem přítomných vstupů a výstupů. Například pro Whirlpool 5x5 Coinjoin bychom měli:

    ED: Hustota entropie vyjádřená v bitech.
    E: Entropie transakce vyjádřená v bitech.
    T: Celkový počet vstupů a výstupů v transakci.

T = 5 + 5 = 10
ED = E / TED = 10.5469 / 10
ED = 1.054 bitů

Pátým poskytnutým údajem kalkulačky Boltzmann je tabulka pravděpodobností spojení mezi vstupy a výstupy. Tato tabulka jednoduše udává pravděpodobnost (Boltzmannovo skóre), že daný vstup odpovídá danému výstupu.

Pokud vezmeme náš příklad s Whirlpool Coinjoin, tabulka pravděpodobnosti by vypadala takto:

| %       | Výstup 0 | Výstup 1 | Výstup 2 | Výstup 3 | Výstup 4 |
|---------|----------|----------|----------|----------|----------|
| Vstup 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Vstup 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Zde vidíme, že každý vstup má stejnou pravděpodobnost spojení s každým výstupem.

Pokud však vezmeme příklad transakce s jedním vstupem a dvěma výstupy, vypadalo by to takto:

| Vstup | Výstup 0 | Výstup 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

V tomto příkladu vidíme, že pravděpodobnost, že každý výstup pochází z vstupu 0, je 100%.

Čím nižší je tato pravděpodobnost, tím vyšší je úroveň důvěrnosti.

6. Šestým vypočítaným údajem je počet deterministických spojení. Bude také poskytnut poměr deterministických spojení. Tento ukazatel zdůrazňuje počet spojení mezi vstupy a výstupy dané transakce, které mají pravděpodobnost 100%, což znamená, že jsou nezpochybnitelné.

Poměr udává počet deterministických spojení v transakci ve srovnání s celkovým počtem spojení.

Například transakce Coinjoin Whirlpool nemá mezi vstupy a výstupy žádná deterministická spojení. Ukazatel bude nula a poměr také 0%.

Nicméně pro druhou studovanou transakci (1 vstup a 2 výstupy) je ukazatel 2 a poměr je 100%.

Pokud je tento ukazatel nula, znamená to dobrou důvěrnost.

Nyní, když jsme prozkoumali ukazatele, pojďme se podívat, jak je vypočítat pomocí tohoto softwaru. Z RoninCLI přejděte do menu:

> Samourai Toolkit > Boltzmann Calculator

![Domovská stránka softwaru Boltzmann Calculator](assets/35.webp)

Po spuštění softwaru zadejte ID transakce, kterou chcete studovat. Můžete zadat více transakcí najednou oddělením čárkou, poté stiskněte enter:

![Zadejte TXID pro studium na Boltzmann Calculator](assets/36.webp)

Kalkulačka poté vrátí všechny ukazatele, které jsme předtím viděli:

![Tisk údajů Boltzmann Calculator pro tento TXID](assets/37.webp)

Pro ukončení softwaru a návrat do menu RoninCLI napište příkaz "Quit".

Pro více informací o kalkulačce Boltzmann doporučuji číst tyto články:

- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159

- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
### Připojení Bisq.
Bisq je platforma pro peer-to-peer směnu, která vám umožňuje kupovat a prodávat bitcoiny. Používá se s desktopovým softwarem, který běží na Toru a umožňuje vám směňovat bitcoiny bez nutnosti poskytovat vaši identitu.
Bisq zabezpečuje peer-to-peer směny prostřednictvím systému s více podpisy 2/2. Tento software můžete používat se svým vlastním uzlem RoninDojo, abyste optimalizovali soukromí vašich směn a důvěřovali datům z blockchainu vašeho vlastního uzlu.

Pro stažení softwaru Bisq přejděte na jejich oficiální webovou stránku: https://bisq.network/

Pro začátek s softwarem doporučuji přečíst tuto stránku: https://bisq.network/getting-started/

Pro získání připojovacího odkazu od vašeho RoninDojo budete potřebovat se připojit k RoninCLI přes SSH. Poté přejděte do menu:

> Aplikace > Spravovat aplikace

Zadejte své heslo, poté zaškrtněte políčko klávesou mezerníku:

> [ ] Povolit připojení Bisq

Potvrďte svou volbu. Nechte svůj uzel nainstalovat, poté získejte adresu Tor V3 z:

> Přihlašovací údaje > Bitcoind

Zkopírujte adresu pod "Bitcoin Daemon".

Svou adresu Bitcoind Tor V3 můžete také získat z rozhraní RoninUI jednoduše kliknutím na "Spravovat" v boxu "Bitcoin Core" na "Dashboardu":

![Získání adresy TorV3 Bitcoin Daemon na RoninUI](assets/38.webp)

Pro připojení vašeho uzlu k Bisq přejděte do menu:

> Nastavení > Informace o síti

![Přístup k rozhraní pro připojení uzlu z softwaru Bisq](assets/39.webp)

Klikněte na bublinu "Použít vlastní uzly Bitcoin Core". Poté zadejte vaši adresu Bitcoin TorV3 do určeného pole, s ".onion", ale bez "http://".

![Pole pro zadání adresy TorV3 vašeho uzlu v softwaru Bisq](assets/40.webp)

Restartujte software Bisq. Váš uzel je nyní připojen k vašemu Bisq.

### Další funkce.

Váš uzel RoninDojo také zahrnuje další základní funkce. Máte možnost skenovat specifické informace, aby byly vzaty v úvahu.

Například je někdy možné, že vaše peněženka připojená k vašemu RoninDojo nenajde bitcoiny, které vám patří. Zůstatek je 0, i když jste si jisti, že máte v této peněžence bitcoiny. Existuje mnoho možných příčin, včetně chyby v cestách derivace, a mezi nimi je také možné, že váš uzel neobservuje vaše adresy.

Pro opravu tohoto stavu můžete zkontrolovat, zda váš uzel sleduje váš xpub pomocí nástroje "xpub tool". Pro přístup k němu z RoninUI přejděte do menu:

> Údržba > XPUB Tool

Zadejte problematický xpub a klikněte na "Kontrola" pro ověření této informace.

![XPUB Tool z RoninUI](assets/41.webp)

Pokud váš xpub sleduje uzel, uvidíte toto zobrazení:

![Výsledek nástroje XPUB Tool ukazující úspěšnou analýzu](assets/42.webp)

Zkontrolujte, zda se všechny transakce správně zobrazují. Také ověřte, zda typ derivace odpovídá vaší peněžence. Zde vidíme, že uzel interpretuje tento xpub jako derivaci BIP44. Pokud tento typ derivace neodpovídá vaší peněžence, klikněte na tlačítko "Změnit typ", poté vyberte BIP44/BIP49/BIP84 podle vašeho výběru:

![Změna typu derivace studovaného xpub z RoninUI](assets/43.webp)

Pokud váš xpub není sledován vaším uzlem, uvidíte tuto obrazovku, která vás vyzve k jeho importu:
![Importujte xpub pomocí nástroje XPUB na RoninUI](assets/44.webp)
Můžete také použít další údržbové nástroje:

- Nástroj pro transakce: Umožňuje vám sledovat detaily konkrétní transakce.
- Nástroj pro adresy: Umožňuje ověřit, že konkrétní adresa je sledována vaším Dojo.
- Nové prohledání bloků: Nutí váš uzel k novému prohledání vybraného rozsahu bloků.

Na RoninUI také najdete nástroj "Push Tx". Umožňuje vám vysílat podepsanou transakci do Bitcoinové sítě. Musí být zadána v hexadecimálním formátu:

![Nástroj pro vysílání podepsané transakce z RoninUI](assets/45.webp)

## Závěr.

Viděli jsme, jak nainstalovat a začít používat tento úžasný nástroj, kterým je RoninDojo. Je to vynikající volba pro provozování vlastního Bitcoinového uzlu. Je to stabilní řešení, které integruje a udržuje aktuální všechny nezbytné nástroje pro Bitcoinera.

Pokud vás používání terminálu neodrazuje a nepotřebujete nástroje související s Lightning Network, pak by vás RoninDojo mohlo zaujmout.

Pokud můžete, zvažte darování vývojářům, kteří pro vás tyto open-source softwary vytvářejí zdarma: https://donate.ronindojo.io/

Pro další informace o RoninDojo doporučuji prozkoumat odkazy v mých externích zdrojích níže.

### Další čtení:

- Porozumění a používání CoinJoin na Bitcoinu.
- Hašovací funkce - úryvek z e-knihy Bitcoin Démocratisé 1.
- Vše, co potřebujete vědět o Bitcoinové heslové frázi.

### Externí zdroje:

- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/představení-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/
