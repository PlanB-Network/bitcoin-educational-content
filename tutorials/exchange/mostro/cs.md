---
name: Mostro
description: Výměnná platforma Bitcoin P2P bez KYC prostřednictvím Lightning a Nostr
---

![cover](assets/cover.webp)



Jak získat nebo prodat bitcoiny, aniž byste ohrozili svou finanční suverenitu? Centralizované platformy zavádějí invazivní postupy KYC, které odhalují vaše osobní údaje, s možností svévolného zmrazení účtu nebo státního dohledu.



**Mostro P2P** nabízí decentralizovanou alternativu kombinující Lightning Network, protokol Nostr a podržené faktury. Její hlavní inovace: automatizovaný systém úschovy, kdy vaše bitcoiny zůstávají pod vaší kontrolou po celou dobu výměny, což eliminuje riziko krádeže, bankrotu burzy nebo svévolné konfiskace.



## Co je Mostro P2P?



Mostro P2P je open source výměnný protokol Bitcoin, který vytvořil **grunch**, vývojář populárního bota Telegram **lnp2pbot** spuštěného v roce 2021. Zatímco lnp2pbot již umožnil výměnu P2P bez KYC prostřednictvím Lightning, představoval velkou zranitelnost: **Telegram představuje centralizovaný bod selhání** náchylný k cenzuře ze strany vlád.



Mostro představuje **decentralizovanou evoluci** tohoto konceptu: nahrazením Telegramu protokolem **Nostr** (nesčítatelná síť distribuovaných relé) Mostro toto systémové riziko eliminuje. Protokol kombinuje Lightning Network pro okamžité transakce, Nostr pro komunikaci odolnou vůči cenzuře a **podržené faktury**, čímž vytváří skutečně nekuriózní automatizovanou úschovu.



### Technická architektura



Mostro funguje prostřednictvím tří složek:




- Démon Mostrod**: koordinuje výměny mezi uživateli a Lightning Network
- Uzel Lightning**: vytváří zadržené faktury (~24hodinová kryptografická úschova)
- Zákazníci Mostro**: uživatelská rozhraní (CLI, mobilní zařízení, web)



Příkazy jsou na Nostr zveřejňovány jako veřejné události (typ 38383), zatímco soukromé obchody jsou přenášeny prostřednictvím end-to-end šifrovaných zpráv (NIP-59, NIP-44). Každá instance Mostru definuje své vlastní poplatky (obvykle mezi 0,3 % a 1 %) a limity transakcí (v závislosti na instanci od několika tisíc do několika set tisíc sats).



### Rozhodující výhody



**Odolný vůči cenzuře**: Žádná vláda nemůže Mostro vypnout, dokud někde na světě existují relé Nostra. Na rozdíl od zranitelného lnp2pbot přes Telegram umožňuje Mostro výměny, které jsou **odolné vůči cenzuře**.



**Escrow non-custodial**: V tomto případě se jedná o bleskové faktury, které uzamknou vaše bitcoiny, aniž by je trvale převedly. Vaše prostředky zůstávají pod vaší kontrolou a v případě problému se vám automaticky vrátí (~24 h).



**Důvěrnost podle návrhu**: K dispozici jsou dva režimy, které vyhovují vašim potřebám. Režim Reputace** propojuje vaši reputaci s klíčem Nostr a buduje trvalou důvěru. Plně soukromý režim** upřednostňuje absolutní anonymitu s jednorázovými efemérními klíči.



## Hlavní funkce



**Decentralizovaná komunikace**: Všechny objednávky jsou zveřejňovány na Nostru prostřednictvím kryptograficky podepsaných událostí. Soukromá jednání jsou přenášena prostřednictvím end-to-end šifrovaných zpráv, což zaručuje absolutní důvěrnost.



**Reputační systém**: 5hvězdičkové hodnocení s iterativním výpočtem trvale uložené v Nostru. Umožňuje postupně budovat pověst spolehlivého obchodníka.



**Decentralizovaná arbitráž**: V případě sporu nestranný rozhodce přezkoumá důkazy a rozhodne na základě transparentních kritérií. Každý spor generuje jedinečný kód token pro dohledatelnost.



**Flexibilita platby**: Podpora mnoha fiat měn prostřednictvím služby směnných kurzů yadio.io. Přijímá převody SEPA, PayPal, Revolut, hotovost a jakýkoli způsob dohodnutý mezi stranami.



## Zákazníci společnosti Mostro mají k dispozici



Společnost Mostro nabízí dva hlavní provozní klienty pro vaše výměny P2P.



### Mostro CLI - Klient příkazového řádku



**Mostro CLI** je nejvyspělejší a nejfunkčnější klient. Je napsán v jazyce Rust a nabízí celou řadu funkcí systému Mostro prostřednictvím rozhraní příkazového řádku. Je kompatibilní se systémy MacOS, Linux a Windows.



**Hlavní ovládací prvky** :




- `listorders`: Zobrazit všechny dostupné objednávky
- `neworder` : Vytvoření nového příkazu k nákupu nebo prodeji
- `takesell` / `takebuy`: Přijmout příkaz k nákupu nebo prodeji
- `fiatsent`: Potvrdit odeslání fiat platby
- `release`: Uvolnit úschovu a dokončit výměnu
- `getdm`: Zobrazit přímé zprávy
- `rate` : Vyhodnocení protistrany po výměně



Ideální pro technické uživatele, automatizaci a prostředí vyžadující maximální bezpečnost.



### Mostro Mobile - aplikace pro chytré telefony



**Mobilní aplikace** v alfa verzi umožňuje obchodování s P2P přímo z vašeho chytrého telefonu. Intuitivní grafická aplikace Interface s navigací v záložkách, zobrazením příkazů, pokročilými filtry a integrovaným chatem pro komunikaci s protistranami.



Je k dispozici pro **Android** (prostřednictvím APK na GitHubu) a představuje optimální volbu pro uživatele, kteří upřednostňují jednoduchost a příležitostné mobilní obchodování.



### Mostro-web - web Interface (ve vývoji)



Interface pokročilá webová aplikace v JavaScriptu, která je ve fázi aktivního vývoje. Je navržena tak, aby nabízela kompletní uživatelské prostředí s rozsáhlými funkcemi pro obchodování a správu portfolia. Přístup přes prohlížeč bez nutnosti instalace.



## Instalace a konfigurace



Tento návod vás provede instalací a používáním dvou hlavních klientů Mostro: CLI a mobilní aplikace.



### Základní předpoklady



Než začnete, budete potřebovat :





- Fungující Lightning Network** wallet s dostatečnou likviditou (nebo kompatibilní s Lightning)
 - Doporučujeme: Phoenix, Breez, Wallet z Satoshi...
 - Minimální likvidita 1000 satoshis pro testování



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Soukromý klíč Nostr** (formát `nsec1...`)
 - Vytvoření speciálního obchodního klíče na [nostrkeygen.com](https://nostrkeygen.com/)
 - Důležité**: Nikdy nepoužívejte svůj hlavní osobní klíč Nostr
 - Uchovávejte svůj soukromý klíč na bezpečném místě (správce hesel)





- Volitelné, ale doporučené**: Připojení VPN nebo Tor pro maskování vaší IP adresy



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Instalace zařízení Mostro CLI



#### V systému macOS



**Krok 1: Kontrola Rust**



Zkontrolujte, zda je nainstalována aplikace Rust (vyžaduje se verze 1.64+):



```bash
rustc --version
```



Pokud není Rust nainstalován :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Krok 2: Klonování úložiště**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Krok 3: Konfigurace**



Zkopírujte a upravte položku :



```bash
cp .env-sample .env
```



Otevřete soubor `.env` a nakonfigurujte nastavení:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Důležité pro synchronizaci CLI/Mobile**: Pro přístup ke stejným příkazům v CLI a mobilní aplikaci je nutné použít **stejný Mostro Pubkey** a **stejné Nostr relé** v obou klientech. Zkontrolujte tato nastavení v Nastavení v mobilní aplikaci.



![Configuration .env](assets/fr/02.webp)



**Krok 4: Instalace**



Zkompilujte a nainstalujte CLI :



```bash
cargo install --path .
```



Kompilace trvá 1-2 minuty. Spustitelný soubor `mostro-cli` se nainstaluje do adresáře `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Krok 5: Kontrola**



Zkontrolujte, zda vše funguje:



```bash
mostro-cli --help
```



Měli byste vidět kompletní seznam objednávek.



![Vérification avec --help](assets/fr/04.webp)



#### V systému Linux (Ubuntu/Debian)



Instalace je stejná jako v systému macOS, navíc je přidán :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Poté postupujte podle kroků 3 a 4 v části macOS.



#### V systému Windows



Nejprve nainstalujte Rust pomocí [rustup.rs](https://rustup.rs/) a poté použijte prostředí PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Identická konfigurace: zkopírujte `.env-sample` do `.env` a vyplňte své parametry.



### Instalace aplikace Mostro Mobile



#### V systému Android



**Krok 1**: Přejděte na stránku [GitHub releases page](https://github.com/MostroP2P/mobile/releases) a stáhněte si soubor **app-release.apk** (cca 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Krok 2: Po stažení otevřete soubor APK ze stažených souborů. Systém Android vás požádá o autorizaci instalace z tohoto zdroje.



![Téléchargement et installation APK](assets/fr/11.webp)



**Krok 3**: Postupujte podle obrazovek pro vstup do systému, které představují funkce:




- Volně obchodujte s Bitcoin - bez KYC** : Obchodujte bez ověřování totožnosti díky Nostr
- Soukromí ve výchozím nastavení**: Vyberte si mezi režimem reputace a režimem úplného soukromí
- Bezpečnost na každém kroku**: Ochrana pomocí zadržených faktur bez zadržení



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Krok 4**: Pokračujte v nástupu a zjistěte :




- Plně šifrovaný chat**: Koncová šifrovaná komunikace
- Přijměte nabídku**: Prohlédněte si knihu objednávek a vyberte si nabídku
- Nemůžete najít, co potřebujete?** : Vytvořte si vlastní objednávku na míru



![Suite onboarding](assets/fr/13.webp)



**Krok 5: Po dokončení přihlašování aplikace automaticky vygeneruje pár klíčů Nostr. Přejděte do nabídky (☰) a poté do **Účtu** a uložte svá **Tajná slova** (fráze pro obnovení). Na této obrazovce máte také možnost změnit dříve zmíněný režim ochrany osobních údajů.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Důležité**: Zapište si obnovovací frázi na bezpečné místo (správce hesel, papírový trezor).



### Počáteční konfigurace zabezpečení



Ať už používáte jakoukoli platformu :





- Vyhrazený klíč**: Pro obchodování používejte samostatnou identitu Nostr
- Malé množství**: Pro začátek začněte s méně než 10 000 sats
- Více relé**: Konfigurace 3-5 geograficky různorodých relé
- Ochrana sítě**: Aktivujte VPN nebo Tor, abyste skryli svou IP adresu
- Wallet secure**: Aktivujte automatické uzamčení svého blesku wallet



## Použití s CLI



Tato část ukazuje nákup bitcoinů prostřednictvím služby Mostro CLI podle skutečného případu použití.



### Krok 1: Seznam dostupných objednávek



Příkaz `listorders` zobrazí všechny aktivní objednávky:



```bash
mostro-cli listorders
```



Zobrazí se tabulka s podrobnostmi o každé objednávce: ID, typ (nákup/prodej), částka, měna, způsob platby.



![Liste des ordres disponibles](assets/fr/05.webp)



V tomto příkladu je viditelný příkaz k prodeji 5 EUR přes Revolut (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Krok 2: Přijetí objednávky



Chcete-li tyto bitcoiny koupit, proveďte objednávku pomocí `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Společnost Mostro vás požádá o předložení **Faktury Lightning**, abyste mohli obdržet BTC. Přesná částka je uvedena v satoších (zde: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Krok 3: Poskytnutí faktury Lightning



Vygenerujte bleskovou fakturu z wallet (Phoenix, Breez atd.) na přesnou částku a odešlete ji :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Systém zásilku potvrdí a sdělí vám, že máte počkat, až prodávající zaplatí zadrženou fakturu, a teprve poté aktivovat úschovu.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Krok 4: Kontaktování prodejce



Po aktivaci úschovy si pomocí `dmtouser` vyžádejte od prodávajícího platební údaje:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Krok 5: Získání odpovědi



Zkontrolujte přímé zprávy a zjistěte, jak prodejce reaguje:



```bash
mostro-cli getdm
```



Prodejce vám sdělí své platební ID (zde jeho Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Krok 6: Provedení fiat platby



Zašlete platbu dohodnutým způsobem (v tomto případě Revolut) na uvedené kontaktní údaje. **Uchovejte si všechny podklady** (snímky obrazovky, odkazy na transakce).



### Krok 7: Potvrzení odeslání platby



Po provedení platby informujte společnost Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Krok 8: Přijetí bitcoinů



Jakmile prodávající potvrdí přijetí fiatů a uvolní escrow příkazem `release`, okamžitě obdržíte své bitcoiny na vámi zadanou fakturu Lightning.



### Krok 9: Hodnocení



Ohodnoťte prodávajícího a přispějte tak k jeho decentralizované reputaci:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Užitečné příkazy



**Zrušení objednávky** (před jejím přijetím) :


```bash
mostro-cli cancel -o <order-id>
```



**Vytvoření nové objednávky prodeje** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Otevřít spor** :


```bash
mostro-cli dispute -o <order-id>
```



## Použití s mobilní aplikací



Tato část ukazuje prodej bitcoinů prostřednictvím aplikace Mostro Mobile na základě skutečného případu použití.



### Interface hlavní



Aplikace má 3 hlavní karty:





- Objednávková kniha**: Procházet dostupné příkazy k nákupu (BUY BTC) a prodeji (SELL BTC)
- Moje obchody**: Zobrazit své aktivní a historické příkazy
- Chat**: Komunikujte se svými protistranami pomocí čísel



![Interface principale](assets/fr/14.webp)



### Doporučená konfigurace



Před obchodováním proveďte několik nastavení v nabídce (☰) > **Nastavení** :





- Blesk Address** (volitelně): Pro přímé přijímání plateb
- Relé**: Přidat několik relé Nostr pro zvýšení odolnosti (např. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Zkontrolujte veřejný klíč instance Mostro, kterou používáte



![Paramètres de l'application](assets/fr/16.webp)



**Důležité pro synchronizaci CLI/Mobile**: Pokud používáte CLI i mobilní aplikaci, nakonfigurujte **přesně stejné relé Nostr a Mostro Pubkey** v obou klientech. Bez této shodné konfigurace nebudou na obou rozhraních k dispozici stejné objednávky. Relé a Mostro Pubkey viditelné v Nastavení (obrázek výše) musí odpovídat těm, které jsou uvedeny v souboru `.env' vašeho CLI.



### Krok 1: Vytvoření příkazu k prodeji



Stiskněte zelené tlačítko **"+"** vpravo dole a poté vyberte možnost **Prodat** (červené tlačítko).



![Boutons de création d'ordre](assets/fr/17.webp)



Vyplňte formulář pro vytvoření :



1. **Měna**: Zvolte měnu, ve které si přejete přijímat (EUR, USD atd.)


2. **Částka** : Zadejte částku ve fiat (např. 1 až 3 EUR)


3. **Způsoby platby** : Zvolte metodu (např. "Revolut")


4. **Typ ceny**: Vyberte "Tržní cena"


5. **Premium**: Doporučuje se: 0% pro rychlý prodej)



Pro zveřejnění objednávky stiskněte tlačítko **Odeslat**.



### Krok 2: Potvrzení zveřejnění



Vaše objednávka je nyní zveřejněna! Bude k dispozici po dobu 24 hodin. Můžete ji zrušit kdykoli předtím, než ji kupující převezme, provedením příkazu `cancel`.



![Ordre publié](assets/fr/18.webp)



Příkaz se zobrazí na kartě **Moje obchody** se stavem "Čeká na vyřízení" a odznakem "Vytvořeno vámi".



### Krok 3: Kupující převezme vaši objednávku



Když kupující přijme vaši objednávku, obdržíte oznámení. Podrobnosti naleznete v části **Moje obchody**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Důležité pokyny**: Nyní musíte **zaplatit zobrazenou fakturu**, abyste uzamkli své bitcoiny (zde 4674 sats za 1-5 EUR) v úschově. Máte na to maximálně **15 minut**, jinak bude výměna zrušena.



Zkopírujte si zadrženou fakturu a zaplaťte ji z blesku wallet (Phoenix, Breez atd.).



### Krok 4: Komunikace s kupujícím



Po aktivaci úschovy stiskněte tlačítko **KONTAKT** a otevřete šifrovaný chat s kupujícím.



Kupující (zde "anonymous-gloriaZhao") vás bude kontaktovat a vyžádá si vaše platební údaje. Odpovězte prosím a uveďte své údaje (Revtag, IBAN atd.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Krok 5: Přijetí platby fiat



Počkejte, až vám na účet Revolut (nebo jinou dohodnutou metodou) přijde platba ve fiat. **Důkladně zkontrolujte**:




- Přesná částka
- Odesílatel
- Odkaz, pokud je požadován



Kupující vás bude informovat prostřednictvím chatu, že platbu odeslal. Mostro také zobrazí zprávu potvrzující, že vám byl fiat odeslán.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Krok 6: Uvolnění úschovy



Po **potvrzení přijetí** platby ve fiat na váš účet stiskněte zelené tlačítko **RELEASE** a potvrďte odeslání satss kupujícímu.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoiny jsou okamžitě převedeny kupujícímu prostřednictvím jeho faktury Lightning.



### Krok 7: Zhodnocení úvahy



Po uvolnění stiskněte tlačítko **RATE** a ohodnoťte kupujícího. Vyberte 1 až 5 hvězdiček (zde 5/5) a stiskněte **Odeslat hodnocení**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Výměna je u konce!



### Nákup bitcoinů pomocí mobilní aplikace



Proces **koupě** bitcoinů je podobný, ale obrácený:



1. Pro zobrazení prodejních příkazů přejděte na kartu **Order Book** > **BUY BTC**


2. Kliknutím na zajímavou objednávku zobrazíte podrobnosti


3. Stiskněte tlačítko **Přijmout objednávku**


4. Poskytněte fakturu Lightning (vygenerovanou z wallet)


5. Počkejte, až prodávající aktivuje úschovu


6. Kontaktujte prodávajícího prostřednictvím **KONTAKT** a získejte informace o platbě


7. Odeslat platbu fiat (uschovejte si doklad)


8. Prodávající po ověření uvolní úschovu


9. Okamžitě přijímejte bitcoiny na své Lightning faktuře


10. Ohodnotit prodejce (1-5 hvězdiček)



### Řízení problémů



**Zrušení objednávky**: V části **Moje obchody** stiskněte příkaz a poté tlačítko **ZRUŠIT** (dostupné pouze před jeho přijetím).



**Otevřít spor**: Pokud dojde k neshodě, stiskněte v podrobnostech objednávky tlačítko **DISPUTE**. Přiložte všechny důkazy (snímky obrazovky chatu, odkazy na bankovní transakce).



## Výhody a omezení



### Výhody



**Finanční suverenita**: Vaše bitcoiny nikdy neopustí vaši přímou kontrolu díky mechanismu zadržování faktur, což eliminuje riziko bankrotu burzy nebo pirátství.



**Odolný vůči cenzuře**: Žádný úřad nemůže síť vypnout ani cenzurovat vaše příkazy. Systém funguje, dokud jsou v provozu relé Nostr.



**Výchozí anonymita**: Pouze pseudonymní klíč Nostr vás identifikuje, bez KYC nebo osobních údajů. Koncová šifrovaná komunikace.



**Flexibilita platby**: (převody, mobilní aplikace, hotovost, barter).



### Omezení



**Raný vývoj**: Je nutné vytvořit základní rozhraní a naučit se něco nového.



**Omezená likvidita**: Omezený počet příkazů, zejména u velkých částek nebo vzácných měn.



**Technické požadavky**: Požadujeme základní znalosti Lightning a Nostr.



**Individuální odpovědnost**: V případě problémů není vyžadována centralizovaná podpora, opatrnost.



## Závěr



Mostro P2P představuje slibnou alternativu k centralizovaným burzám, která kombinuje Lightning Network, Nostr a automatickou úschovu pro skutečně decentralizované obchodování. Navzdory svému ranému vývoji a omezené likviditě platforma již nyní nabízí finanční suverenitu, odolnost vůči cenzuře a výchozí anonymitu.



Pro bitcoinery, kteří dávají přednost autonomii a důvěrnosti, je Mostro životaschopnou možností hodnou postupného zkoumání. Jeho decentralizovaná architektura zaručuje spíše komunitní než komerční vývoj, čímž připravuje půdu pro budoucnost skutečně svobodných burz Bitcoin.



## Zdroje



### Oficiální dokumentace




- [oficiální stránky Mostro](https://mostro.network)
- [Technická dokumentace](https://mostro.network/docs-english/index.html)
- [Nadace Mostro](https://mostro.foundation)



### Zdrojový kód a vývoj




- [Hlavní repozitář GitHub](https://github.com/MostroP2P/mostro)
- [Webový klient](https://github.com/MostroP2P/mostro-web)
- [Zákazník CLI](https://github.com/MostroP2P/mostro-cli)



### Společenství




- [Nostr protokol](https://nostr.com)
- [Lightning Network Guides](https://lightning.network)