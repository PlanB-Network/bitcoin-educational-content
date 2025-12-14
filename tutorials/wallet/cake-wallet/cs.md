---
name: Cake Wallet
description: Výukový program o Cake Wallet a tichých platbách
---

![cover](assets/cover.webp)


Tato příručka se zabývá [**Cake Wallet**](https://cakewallet.com/): open-source, necustodialní, na soukromí zaměřený víceměnový wallet dostupný pro Android, iOS, macOS, Linux a Windows. Ponoříme se do jeho funkcí specifických pro ochranu soukromí Bitcoin, projdeme si odesílání/přijímání Bitcoin prostřednictvím **Tichých plateb** (vylepšený protokol pro ochranu soukromí on-chain) a podíváme se na implementaci PayJoin v2 pro asynchronní transakce.


## 🎉 Klíčové funkce



- [**Tiché platby (BIP-352)**](https://bips.dev/352/) vylepšuje předchozí [BIP 47 platebních kódů](https://silentpayments.xyz/docs/comparing-proposals/bip47/) nazývané také "PayNyms" o opakovaně použitelné skryté adresy. Když odesílatel použije vaši adresu Tiché platby, jeho wallet odvodí pomocí různých klíčů jedinečnou jednorázovou adresu, která se spojí do jedinečné jednorázové adresy Taproot. V záznamech blockchainu se zobrazují nesouvisející transakce, což zabraňuje propojení příchozích plateb. Tiché platby nabízejí řadu výhod, mezi něž patří např:
    - Opakovaně použitelné adresy: Pro každou transakci není nutné zadávat novou adresu generate, což přináší lepší uživatelský komfort a větší soukromí
    - Nulové zvýšení nákladů: Tiché platby nezvyšují velikost ani náklady na transakce.
    - Zvýšená anonymita: Vnější pozorovatelé nemohou spojit transakce s adresou tiché platby.
    - Není nutná interakce mezi odesílatelem a příjemcem: Transakce lze provádět bez jakékoliv komunikace mezi stranami.
    - Jedinečné adresy pro každou platbu: Eliminuje riziko náhodného opakovaného použití adresy.
    - Není vyžadován žádný server: Tiché platby lze provádět bez potřeby vyhrazeného serveru.
- PayJoin v2** zmírňuje analýzu transakčního grafu sloučením vstupů odesílatelů a příjemců do jediné transakce. Dort Wallet zavádí dva zásadní pokroky:
    - Asynchronní transakce**: Odesílatel a příjemce již nemusí být současně online, aby mohli dokončit soukromou transakci.
    - Komunikace bez serveru**: Žádná ze stran nemusí provozovat server Payjoin, čímž odpadá hlavní technická překážka.
- Coin Control** umožňuje manuální volbu UTXO během transakcí. Tím se zabrání náhodnému propojení adres při utrácení více UTXO s různým původem.
- Podpora TOR**, která uživatelům umožňuje směrovat síťový provoz přes síť Tor
- RBF** (Replace-By.Fee) umožňuje upravit poplatek po odeslání transakce.


## 1️⃣ Nastavení Wallet


Cake Wallet nabízí širokou škálu podpory platforem. Můžete si vybrat mezi `Android`, `iOS / macOS` , `Linux` a `Windows`.  Chcete-li začít, navštivte stránku https://docs.cakewallet.com/get-started/ a vyberte svůj operační systém.


![image](assets/en/01.webp)


Po instalaci nastavte `PIN` (4 nebo 6 číslic). Poté se zobrazí:


1. `Vytvoření nového účtu Wallet` (pro nové uživatele)

2. `Obnovit Wallet` (pro stávající peněženky)


![image](assets/en/02.webp)


Na další obrazovce si můžete vybrat z široké nabídky kryptoměn. Vyberte `Bitcoin`, klepněte na `Další` a zadejte `Název Wallet` pro identifikaci wallet. Klepnutím na `Rozšířené nastavení` se zobrazí řada `Nastavení ochrany osobních údajů`. Proveďte tyto změny:



- Fiat API:** vyberte `Tor Only` (směruje požadavky na cenu přes Tor)
- Swap:** vyberte `Tor Only` (anonymizuje výměnný provoz)


Ve výchozím nastavení je generován typ BIP-39 seed s možností změny na typ Electrum seed. Odvozovací cesty jsou následující:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Pokud chcete přidat další úroveň zabezpečení, můžete nastavit `passphrase`.  Hlavním účelem passphrase je poskytnout dodatečnou ochranu proti fyzickým útokům. I když útočník najde frázi seed, bez správného passphrase se k vašemu wallet nedostane. Jinými slovy, samotná fráze seed představuje jeden wallet, zatímco fráze seed plus passphrase vytvoří zcela jiný wallet bez spojení s původním. Tato funkce také umožňuje "tajné peněženky" chráněné pomocí passphrase a poskytuje vám věrohodné popření. V případě nátlaku můžete prozradit frázi seed, zatímco větší majetek zůstane v bezpečí v wallet chráněném frází passphrase.


Pokud již provozujete vlastní uzel, přepněte na `Přidat nový vlastní uzel` a zadejte svůj `Uzel Address` pro ověřování transakcí a bloků v rámci vlastní infrastruktury. Po dokončení klepněte na `Pokračovat` a `Další` a vytvořte svůj wallet.


![image](assets/en/03.webp)


Na další obrazovce se zobrazí prohlášení o vyloučení odpovědnosti:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Chcete-li se seznámit s osvědčenými postupy pro ukládání mnemotechnické fráze, přečtěte si tento návod:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ťukněte na položku `Rozumím. Ukažte mi můj seed` a uložte tato slova na bezpečné místo! Poté klepněte na `Ověřit seed` a po ověření `Otevřít Wallet`.


## nastavení 2️⃣


Než se ponoříme hlouběji, podívejme se na `Home Screen` a `Settings`.


Na domovské obrazovce se zobrazují různé položky:



- nabídka `Hamburger` nás přivede do `Nastavení`
- Dostupný zůstatek
- Karta tichých plateb pro zahájení skenování transakcí odeslaných na vaši adresu tichých plateb
- Karta Payjoin pro `Povolení` Payjoin jako funkce pro zachování soukromí a úsporu poplatků
- dole jsou zkratky pro `Přehled Wallet`, `Příjem`, `Výměna` mezi Bitcoin a jinými měnami, `Odeslání` a `Koupě`


![image](assets/en/11.webp)


Klepnutím na ikonu `Hamburger menu` otevřete nabídku nastavení. Projděme si možnosti.


![image](assets/en/05.webp)


### A - Připojení a synchronizace 🔗


Zde můžeme znovu připojit wallet, spravovat uzly a připojit se k vlastnímu uzlu (doporučeno). Funkce `Skenování tichých plateb` nám umožňuje přizpůsobit skenování zadáním buď možnosti `Skenovat podle výšky bloku`, nebo `Skenovat podle data`.


![image](assets/en/06.webp)


Jako `Alpha` funkce je k dispozici také možnost `Povolit integrovaný Tor` pro směrování provozu přes síť Tor.


### B - Nastavení tichých plateb 🔈


Tuto funkci můžeme zobrazit přepnutím karty Tiché platby na domovské obrazovce. Povolení možnosti `Vždy skenovat` umožní aplikaci wallet nepřetržitě sledovat blokový řetězec pro příchozí Tiché platby. Můžeme zadat parametry skenování a přizpůsobit tak proces skenování našim potřebám, jak je popsáno výše.


![image](assets/en/07.webp)


### C - Zabezpečení a zálohování 🗝️


Abychom zabezpečili svou službu wallet, můžeme vytvořit zálohu podle pokynů v aplikaci. Tím zajistíme, že budeme mít bezpečnou kopii našich soukromých klíčů, což nám umožní obnovit náš wallet v případě jeho ztráty nebo odcizení. Kromě toho si můžeme zobrazit naši frázi a soukromé klíče seed, změnit kód PIN, povolit biometrické ověřování, Podepsat/Ověřit a nastavit 2FA pro další úroveň ochrany.


![image](assets/en/08.webp)


**Poznámka**: Od září 2025 musí biometrické ověřování otisků prstů v zařízeních se systémem Android fungovat alespoň s biometrickou implementací třídy 2, více informací naleznete zde [https://source.android.com/docs/security/features/biometric/measure#biometric-classes]. Tento požadavek se však může v budoucnu změnit.


### D - Nastavení soukromí 🔒


Zabezpečení naší služby wallet můžeme zvýšit také použitím sítě Tor, která šifruje naše internetové připojení a chrání naše soukromí při přístupu k externím zdrojům. Kromě toho můžeme zabránit pořizování snímků obrazovky, abychom zachovali důvěrnost informací o našem systému wallet, povolit automaticky generované adresy, aby se pro každou transakci vytvářely nové, a zakázat akce nákup/prodej, abychom zabránili neoprávněným transakcím. Dále můžeme `Zakázat PayJoin`, což je další funkce ochrany soukromí, kterou si projdeme později.


![image](assets/en/09.webp)


### E - Další nastavení 🔧


Další nastavení nám umožňují spravovat prioritu poplatků a nastavit výchozí úroveň poplatků pro naše transakce. To nám umožňuje řídit poplatky za transakce spojené s našimi Tichými platbami s ohledem na aktuální vytížení sítě.


![image](assets/en/10.webp)


## 3️⃣ Přijímání ₿itcoinů pomocí tichých plateb


Pro příjem Bitcoin je k dispozici několik možností a typů adres. `Segwit (P2WPKH)` *(začínající bc1q....)* je výchozí volbou.  V tomto příkladu vybereme `Tiché platby`.


Chcete-li přijmout tichou platbu, nejprve klepněte na ikonu `Přijmout` v aplikaci Cake Wallet. Poté zadejte částku, kterou očekáváte obdržet. Chcete-li zadat typ adresy, znovu klepněte na ikonu `Přijmout` v horní části obrazovky a z možností vyberte možnost `Tiché platby`.


Na hlavní obrazovce se zobrazí váš opakovaně použitelný kód QR pro tichou platbu a adresa. Podle očekávání je adresa poměrně dlouhá:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Nyní pomocí kompatibilního zařízení BIP-352 (například modrého Wallet) naskenujte tento QR kód a odešlete platbu. Uvidíte, že zařízení wallet z vaší tiché adresy odvodí jedinečnou cílovou adresu.


![image](assets/en/13.webp)


## 4️⃣ Odesílání ₿itcoin pomocí tichých plateb


Protože modrý Wallet umí pouze "odesílat" tiché platby, použijeme jako přijímající stranu jiný kompatibilní BIP 352 wallet. Tento proces je totožný s běžnou transakcí Bitcoin.



- Klepněte na možnost `Odeslat` na domovské obrazovce
- buď vložením naší opakovaně použitelné adresy `sp1qq...`, nebo naskenováním QR kódu přímo v aplikaci.
- Zvolte, kolik chcete utratit ze svého dostupného zůstatku
- Klepnutím na `Odeslat` v dolní části obrazovky potvrďte transakci


Jakmile zadáme adresu `sp1qq...`, wallet na pozadí automaticky odvodí odpovídající adresu `bc1p...` Taproot (P2TR), která bude použita pro Tichou platbu.


Volitelně můžeme pro každou transakci zapsat interní poznámku, upravit nastavení poplatků nebo vybrat určité UTXO pro transakci pomocí funkce `Coin Control`.


![image](assets/en/14.webp)


transakci potvrdíte přejetím prstem doprava.


Po odeslání transakce budete dotázáni, zda si přejete přidat tento kontakt do svého adresáře.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Zopakujme si, o čem PayJoin je (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2 je funkce pro zachování soukromí a úsporu poplatků v systému Bitcoin, která umožňuje odesílateli a příjemci transakce spolupracovat na vytvoření jediné transakce. Tato transakce má vstupy od *obou* odesílatele i příjemce, což prolamuje nejběžnější techniky sledování proti Bitcoin a umožňuje lepší škálování a za určitých okolností také úsporu poplatků._


Chcete-li se o PayJoin dozvědět více, můžete také navštívit následující výukový program.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Pro použití PayJoin potřebují obě strany PayJoin kompatibilní wallet a příjemce musí mít ve svém wallet alespoň jednu minci nebo výstup. Chcete-li začít, postupujte podle následujících kroků:


1. Klepněte na tlačítko `Hamburger Menu` a klepněte na tlačítko `Soukromí`

2. Přepnutí možnosti `Použít Payjoin`

3.  Klepněte na `Přijmout` na domovské obrazovce a zobrazí se kód QR PayJoin a tlačítko pro kopírování (pokud je vybrán Segwit)


![image](assets/en/16.webp)


## 6️⃣ Další funkce


K dispozici je několik dalších funkcí, jako jsou `Swapy` ve více měnách, možnosti `Koupit a prodat` s různými propojeními s prodejci a specifické programy pro Cake, jako je `Cake Pay`, který umožňuje nákup předplacených karet nebo dárkových karet.


![image](assets/en/17.webp)


## 🎯 Závěr


Přinášíme recenzi produktu Cake Wallet, který díky funkcím, jako jsou Tiché platby (BIP-352) a Payjoin v2, nabízí praktické soukromí jako Bitcoin.


Tiché platby nahrazují jednorázové adresy opakovaně použitelnými skrytými adresami, aby se zabránilo propojení příchozích transakcí pomocí on-chain. Ačkoli se problémy se synchronizací předchozích verzí znatelně zlepšily, jsou vyžadovány určité zvýšené výpočetní nároky na skenování a detekci Tichých plateb, které vyžadují více zdrojů a šířku pásma.


Payjoin v2 narušuje analýzu řetězců tím, že spojuje vstupy odesílatele a příjemce do jedné transakce bez dalších poplatků nebo centrální koordinace. Tím se ruší běžná heuristika vlastnictví vstupů, což je významná výhoda, protože to znamená, že nelze předpokládat, že všechny vstupy patří odesílateli.


Pro uživatele, kteří upřednostňují finanční anonymitu, je dort Wallet vhodnou volbou. Zahrnuje protokoly o ochraně soukromí přímo do svých základních funkcí, takže jsou přístupné bez jakýchkoli technických složitostí. Vzhledem k tomu, že se zvyšuje dohled nad veřejnými blockchainy, pomáhají nástroje, jako je tento, zachovat soukromí transakcí tam, kde je to nejdůležitější. Širší implementace těchto standardů v rámci prostředí wallet by byla vítaným vývojem.


## 📚 Zdroje


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/