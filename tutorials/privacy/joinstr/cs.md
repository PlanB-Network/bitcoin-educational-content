---
name: Joinstr
description: Decentralizované CoinJoins prostřednictvím sítě Nostr pro suverénní důvěrnost Bitcoin
---

![cover](assets/cover.webp)



Transparentnost blockchainu Bitcoin umožňuje sledovat historii transakcí. CoinJoins tyto vazby přerušují smícháním více souběžných transakcí, čímž obnovují úroveň důvěrnosti srovnatelnou s hotovostí.



Tradiční řešení se však spoléhají na centrálního koordinátora jako na jediný bod selhání. Společnosti Wasabi a Samourai ukončily svou činnost v roce 2024 pod tlakem regulačních orgánů.



**Joinstr** tuto slabinu odstraňuje tím, že ke koordinaci využívá decentralizovanou síť Nostr. Tato open source aplikace umožňuje skutečně suverénní CoinJoiny, kde žádná centrální autorita nemůže službu cenzurovat, monitorovat nebo přerušit.



## Co je Joinstr?



Joinstr je open source nástroj, který revolučním způsobem mění přístup CoinJoins tím, že využívá protokol Nostr jako koordinační infrastrukturu. Na rozdíl od centralizovaných řešení vyžadujících vyhrazený server se Joinstr spoléhá na distribuovanou síť relé Nostr, která účastníkům umožňuje koordinovat přímo mezi vrstevníky.



**Decentralizovaná architektura** : Síť Nostr nahrazuje centrálního koordinátora. Účastníci vytvářejí "pooly" nebo se k nim připojují zasíláním zašifrovaných oznámení prostřednictvím relé Nostr. Tyto informace (částky, účastníci, adresy) zůstávají pro relé nesrozumitelné, což zajišťuje, že žádný centrální subjekt nemůže monitorovat, cenzurovat nebo filtrovat připojení mincí.



**Mezinformační mechanismus SIGHASH_ALL|ANYONECANPAY**: Joinstr využívá tento podpisový příznak Bitcoin a umožňuje každému účastníkovi podepsat pouze svůj vstup, zatímco ověřuje všechny výstupy. Každý uživatel generuje svůj PSBT lokálně a poté jej distribuuje prostřednictvím Nostr. Každý uživatel vygeneruje svůj PSBT lokálně, podepíše jej a poté jej distribuuje prostřednictvím Nostr. Vaše bitcoiny zůstávají pod vaší výhradní kontrolou až do konečného podpisu.



**Filozofie**: Joinstr se řídí cypherpunkovým étosem Bitcoin a usiluje o tři cíle: **odolnost vůči cenzuře** (žádný úřad nemůže službu zastavit), **úplná neomezenost** (své soukromé klíče si ponecháte) a **rovné zacházení** (žádný UTXO nesmí být diskriminován).



### Hlavní funkce



**Flexibilní bazény**: Na rozdíl od pevných nominálních hodnot může každý uživatel vytvořit pool s přesně požadovanou částkou a cílovým počtem účastníků, čímž se optimalizuje využití UTXO bez umělého dělení.



**Transparentní poplatky**: Žádné koordinační poplatky. Pouze transakční poplatky Bitcoin jsou rovnoměrně rozděleny mezi účastníky (několik tisíc satoši na osobu).



**Efemérnost**: Žádná uživatelská data se neuchovávají. Informace se přenášejí prostřednictvím šifrovaných efemérních zpráv Nostr, které se po transakci okamžitě zapomenou.



### Dostupné platformy



Tento návod se zaměřuje na **Android aplikaci**, která je v současné době jediným stabilním a doporučeným řešením. Zásuvný modul Electrum existuje, ale má problémy s kompatibilitou, které jej činí nestabilním. Webové rozhraní je ve vývoji.



## Konfigurace jádra Bitcoin



Joinstr Android vyžaduje připojení k uzlu Bitcoin prostřednictvím RPC. Nejprve je nutné nakonfigurovat jádro Bitcoin v počítači tak, aby přijímalo připojení z telefonu.



**Poznámka**: Podrobnější informace o kompletní konfiguraci jádra Bitcoin naleznete v našich specializovaných tutoriálech:



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Požadavky na síť



#### Vyhledejte svou místní IP adresu



Telefon se systémem Android musí být schopen dosáhnout uzlu Bitcoin v místní síti. Zjistěte IP adresu počítače:



**V systému macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Jednoduchá alternativa:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**V systému Linux** :



```bash
hostname -I | awk '{print $1}'
```



**V systému Windows** :



```cmd
ipconfig
```



Zjistěte adresu IPv4 (formát `192.168.x.x` nebo `10.0.x.x`)



### Konfigurace RPC



#### Upravit bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Najděte svůj soubor `bitcoin.conf`:




- Linux**: bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Otevřete soubor v oblíbeném textovém editoru a přidejte tuto konfiguraci pro aktivaci serveru RPC.



**Doporučená konfigurace pro začátek (záložka)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



*konfigurace *mainnet** (pro produkční použití) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Důležité** :




- Pro první testy se doporučuje použít Signet**: aplikace je stále ve vývoji (beta verze) a mohou se v ní vyskytovat chyby. Signet vám umožňuje testovat zdarma, aniž byste riskovali skutečné finanční prostředky
- Nahraďte `192.168.1.0/24` podsítí vaší sítě (např. pokud je vaše IP `192.168.68.57`, použijte `192.168.68.0/24`)



**Zabezpečení**: Generování silného hesla :



```bash
openssl rand -base64 32
```



### Inicializace



#### Restartujte a zkontrolujte



1. Úplné vypnutí jádra Bitcoin


2. Restartujte jej, abyste použili konfiguraci




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Při prvním spuštění jádra Bitcoin se stáhne a synchronizuje blockchain záložek. Tato operace je mnohem rychlejší než u mainnet (trvá jen několik minut). Než budete pokračovat, počkejte, dokud nebude synchronizace dokončena.



![CRÉATION DE WALLET](assets/fr/04.webp)



Po synchronizaci vytvořte nové portfolio kliknutím na "Create a new wallet". Dejte mu explicitní název, například `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



Váš wallet je nyní vytvořen a připraven přijímat záložky bitcoinů k testování.



#### Získat záložky bitcoins (test)



Chcete-li otestovat Joinstr na záložce, potřebujete zdarma testovací bitcoins :



![SIGNET FAUCET](assets/fr/06.webp)



Použijte veřejnou záložku, například :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



V okně Bitcoin Core vytvořte novou adresu příjmu (karta "Příjem"), zkopírujte ji a vložte do formuláře kohoutku. V případě potřeby vyřešte captcha. Během několika sekund obdržíte zdarma zaknihované bitcoiny.



## Aplikace pro Android



### Instalace



![APPLICATION ANDROID](assets/fr/07.webp)



Nejnovější verzi APK stáhnete na adrese [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases). V prohlížeči systému Android stáhněte soubor a poté jej otevřete a spusťte instalaci. V případě potřeby je třeba v nastavení zabezpečení telefonu povolit instalaci z neznámých zdrojů.



### Konfigurace aplikace



![PERMISSIONS VPN](assets/fr/08.webp)



Při prvním spuštění si aplikace Joinstr vyžádá oprávnění k ovládání integrované sítě VPN. Oba požadavky na oprávnění přijměte: Přijměte souhlas s ovládáním OpenVPN i s připojením k VPN. Tato oprávnění jsou nutná pro integraci VPN, která chrání soukromí vaší sítě.



![INTERFACE APPLICATION](assets/fr/09.webp)



Aplikace Joinstr je rozdělena do tří hlavních karet:




- Domov**: Úvodní obrazovka
- Bazény**: Vytváření a správa bazénů CoinJoin
- Nastavení**: Konfigurace aplikace



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Konfigurace nastavení na kartě "Nastavení":



**1. Nostr relé**: Nostr relay adresa pro koordinaci fondu




- Příklad: `wss://relay.damus.io`
- Další doporučené relaye: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Důležité**: Všichni účastníci musí použít **stejný Nostr relay**, aby viděli a připojili se ke stejným bazénům. Pokud používáte jiné relé, neuvidíte bazény vytvořené na jiných relé



**2. Adresa URL uzlu**: IP adresa uzlu Bitcoin (bez portu)




- Formát: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. Uživatelské jméno RPC** : Uživatelské jméno nakonfigurované v poli `rpcuser=` na vašem bitcoin.conf




- Příklad: `satoshi



**4. RPC Heslo** : Heslo nastavené v poli `rpcpassword=` na vašem bitcoin.conf



**5. Port RPC** : Port RPC v závislosti na síti




- Mainnet** : `8332`
- Záložka**: `38332`



**6. Wallet**: Vyberte základní portfolio Bitcoin obsahující UTXO, které mají být smíchány




- Příklad: `tuto_joinstr_signet`



**7. Brána VPN**: Vyberte server Riseup VPN




- Příklad: `(Paris) vpn07-par.riseup.net`
- Ostatní jsou k dispozici: Další: Amsterdam, Seattle atd.
- ⚠️ **Důležité**: Všichni účastníci ve stejném fondu musí pro účast v CoinJoin používat **stejnou bránu VPN**. Během směšovacího kola se všichni účastníci musí objevit se stejnou výstupní IP adresou, aby síťová analýza nemohla účastníky vzájemně porovnávat



Aplikace Joinstr** nativně integruje** síť Riseup VPN, což zjednodušuje koordinaci mezi účastníky.



**Důležité** :




- Zkontrolujte, zda jsou telefon a počítač ve stejné místní síti Wi-Fi
- Připojení VPN se aktivuje automaticky při účasti ve fondu
- Po nastavení všech parametrů klikněte na **"Uložit "**



## Praktické využití



### Vytvoření fondu nebo připojení k němu



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Máte dvě možnosti, jak se zúčastnit akce CoinJoin:



**Možnost 1: Vytvoření nového fondu**



Na kartě "Pools" klikněte na možnost "Create New Pool". Zadejte nominální hodnotu v BTC (např. 0,002 BTC) a požadovaný počet účastníků (minimálně 2, doporučeno 3-5 pro větší anonymitu). Aplikace poté čeká na další uživatele, kteří se k vašemu poolu připojí. Po dosažení požadovaného počtu se automaticky spustí proces výstupní registrace a vy budete muset vybrat svůj UTXO do mixu a kliknout na "Registrovat".



**⏱️ Důležité**: Pooly vyprší po **10 minutách** nečinnosti. Pokud není dosaženo požadovaného počtu účastníků, bazén se automaticky uzavře.



**Možnost 2: Připojení k existujícímu fondu**



Na kartě "Zobrazit další pooly" můžete procházet dostupné pooly vytvořené jinými uživateli. Vyberte fond odpovídající vaší částce a připojte se k němu. Ujistěte se, že jste nakonfigurovali stejný Nostr relay a VPN Gateway jako ostatní účastníci (viz část Konfigurace).



**Pravidlo výběru UTXO**: Vaše hodnota UTXO musí být o něco vyšší než nominální hodnota fondu (mezi +500 a +5000 sats).



**Příklad**: Pro pool 0,002 BTC (200 000 sats) použijte UTXO mezi 200 500 a 205 000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Proces je pak **zcela automatický**: jakmile je váš vstup zaregistrován, aplikace čeká, až všichni účastníci zaregistrují své vstupy. Jakmile jsou všechny vstupy zaregistrovány, vytvoří se PSBT, automaticky se podepíše vašimi klíči a poté se spojí s podpisy ostatních účastníků. Nakonec je celá transakce odvysílána v síti Bitcoin. Po dokončení vysílání obdržíte TXID (identifikátor transakce). V systému Android není nutná žádná ruční manipulace s PSBT.



### Ověření on-chain



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Po odvysílání transakce obdržíte TXID (identifikátor transakce). Prohlédněte si jej na [mempool.space](https://mempool.space) nebo ve svém oblíbeném prohlížeči. Chcete-li testovat na záložce, použijte [mempool.space/signet](https://mempool.space/signet).



Můžete pozorovat :





- N položek**: Na každého účastníka připadá jeden záznam (v našem případě 2 záznamy)
- N stejných výstupů**: přesná částka nominální hodnoty (zde 2 výstupy po 0,00199800 BTC)
- Vývojový diagram**: mempool.space vizuálně zobrazuje kombinaci vstupů a výstupů
- Vlastnosti** : Transakci lze identifikovat jako SegWit, Taproot, RBF atd.



Protože všechny hlavní výstupy mají stejnou částku, je **nemožné určit, který patří komu**. To je základní princip CoinJoin: nerozlišitelnost výstupů.



**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Upozornění**: Pokud byly vaše UTXO větší než nominální hodnota fondu, budete mít devizové výstupy (přebytky). Tyto devizové UTXO zůstávají dohledatelné a musí být spravovány odděleně od vašich anonymizovaných výstupů. Nikdy je nekombinujte se svými smíšenými výstupy.



## Balíčky kvality a anonymity CoinJoin



Efektivita transakce CoinJoin se měří podle jejího **anonsetu**: počtu výstupů stejné hodnoty, které transakce vyprodukuje. Čím vyšší je toto číslo, tím obtížnější je určit, který vstup odpovídá kterému výstupu.



Společnost Joinstr v současné době vytváří v průměru skupiny **2 až 5 účastníků**. Tato čísla jsou nižší než u tradičních centralizovaných koordinátorů, jako je Wasabi (50-100 účastníků) nebo Whirlpool (5-10 účastníků), ale to je cena za decentralizaci.



💡 **Chcete-li podrobně porozumět množinám anonymity a jejich výpočtu**, podívejte se na náš kompletní kurz: [Anonymity sets](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. ostatní CoinJoins




| Aspekt | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Účastníci na fond** | 50-100 | 5-10 | Variabilní (P2P) | **2-5** |
| **Koordinátor** | Centralizovaný (uzavřen 2024) | Centralizovaný (aktivní) | P2P maker/taker | **Žádný (Nostr)** |
| **Odolnost vůči cenzuře** | Nízká | Střední | Velmi vysoká | **Velmi vysoká** |
| **Poplatky za koordinaci** | Procento | Vstupní poplatek | Placeno výrobcům | **Žádný** |
| **Diskriminace UTXO** | Ano (černé listiny) | Ne | Ne | **Ne** |

💡 **Další aktivní roztoky CoinJoin** :




- Ashigaru**: V tomto případě se jedná o open-source implementaci protokolu Whirlpool s centralizovaným koordinátorem, ale s možností decentralizovaného nasazení. Pokračuje v provozu po převzetí Samourai Wallet v roce 2024.
- JoinMarket**: Na základě obchodního modelu "maker/taker", kdy "maker" poskytuje likviditu a je odměňován "takerem", je založeno decentralizované řešení P2P bez centrálního koordinátora.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Základní kompromis**: Joinstr a JoinMarket jsou jediná dvě řešení bez centrálního koordinátora. JoinMarket používá obchodní model P2P s finančními pobídkami, zatímco Joinstr využívá Nostr pro koordinaci bez nákladů. Joinstr obětuje okamžitou anonymitu ve velkém měřítku ve prospěch jednoduchosti (žádné řízení tvůrců/odběratelů) a úplné absence koordinačních poplatků.



**Praktické doporučení**: Pro kompenzaci menších skupin proveďte několik po sobě jdoucích kol CoinJoin s různými účastníky. Rozdělte si kola a mezi jednotlivými koly vyměňte štafety Nostr, abyste maximalizovali důvěrnost.



Více informací o tomto tématu najdete v našem kompletním kurzu o soukromí bitcoinů:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Výhody a omezení



### Nejdůležitější informace



**Zvýšené soukromí**: Kombinace šifrování komunikace Nostr, sdílené VPN mezi účastníky a doporučeného používání sítě Tor vytváří vícevrstvou ochranu, kterou je těžké obejít.



**Transparentní, minimální náklady**: Žádné náklady na koordinaci, pouze náklady na mining jsou spravedlivě rozděleny mezi účastníky. Žádné procento nevybírá žádný provozovatel.



### Omezení, která je třeba zvážit





- Proměnlivá likvidita**: Menší skupiny, mohou čekat, až se účastníci sejdou
- Probíhající projekt**: Aplikace v beta verzi, možné chyby. Nejprve testujte s malým množstvím na záložce
- Sybil útočí**: Možnost, že jeden soupeř ovládá několik účastníků bazénu



## Osvědčené postupy



**Izolace UTXO**: Nikdy nekombinujte smíšený UTXO s nesmíšeným. Pro anonymizované výstupy používejte samostatné portfolio.



**Nejdůležitější je více kol**: Proveďte minimálně 3 po sobě jdoucí kola s různými účastníky. Měňte množství a časování, abyste se vyhnuli šablonám. Jednotlivá kola provádějte s odstupem několika hodin.



**Ochrana sítě**: Kromě vestavěné sítě VPN systematicky používejte Tor. Generujte efemérní klíče Nostr pro každou důležitou relaci.



**Obezřetný postup**: Začněte se záložkami po malých částkách.



## Závěr



Joinstr představuje skutečně decentralizované řešení ochrany soukromí Bitcoin. Tím, že ke koordinaci využívá Nostr, eliminuje závislost na centrálních koordinátorech a zároveň zachovává suverenitu uživatelů.



**Pro uživatele, kteří si cení odolnosti vůči cenzuře a jsou připraveni provést několik kol CoinJoin, aby kompenzovali menší fondy.



Na pozadí rostoucí finanční kontroly se decentralizované nástroje na ochranu soukromí stávají nezbytnými.



## Zdroje



### Oficiální dokumentace




- [oficiální webové stránky Joinstr](https://joinstr.xyz)
- [Uživatelská dokumentace](https://docs.joinstr.xyz/users/using-joinstr)
- [Technická dokumentace](https://docs.joinstr.xyz/overview/how-does-it-work)
- [zdrojový kód GitLab](https://gitlab.com/invincible-privacy/joinstr)
- [aplikace pro Android](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Výukové programy




- [Electrum plugin tutorial](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Kompletní průvodce od Uncensored Tech



### Společenství a podpora




- [Telegram Joinstr Group](https://t.me/joinstr) - Komunitní podpora a záložkové koutky
- [Technická diskuse na DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Další nástroje




- [Záložka Faucet](https://signetfaucet.com) - Bezplatný test Bitcoins
- [Alt Signet Faucet](https://alt.signetfaucet.com) - alternativa Faucet
- [Mempool.space](https://mempool.space) - Block explorer s analýzou soukromí