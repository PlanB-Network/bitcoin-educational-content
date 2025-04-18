---
name: LNbits
description: Účetní platforma pro obchodníky
---
![presentation](assets/lnbits-intro.webp)

# Účetní systém

LNbits obsahuje spoustu nástrojů pro ovládání a směrování příchozích a odchozích peněz, připojení webového obchodu nebo dokonce zařízení, jako je hardwarová peněženka nebo bankomat, které jste si sami vytvořili. Mezi typy uživatelů patří např:


- Majitelé peněženek, kteří chtějí používat LNbits jako rozhraní pro správu svých prostředků i jejich dalších funkcí.
- Online i offline obchodníci nebo poskytovatelé služeb, kteří chtějí přijímat platby v Bitcoin onchainu a Lightning Network.
- Vývojáři, kteří chtějí vytvářet aplikace Lightning Network.
- Provozovatelé uzlů, kteří chtějí integrovat svůj uzel se systémem LNbits pro účely účetnictví.
- Všichni mají různé potřeby. LNbits vytváříme modulárně, aby každý uživatel mohl využívat naše funkce způsobem, který mu nejlépe vyhovuje.

# Správce peněženky

LNbits je svobodný účetní systém s otevřeným zdrojovým kódem - ne správce uzlů. Správa kanálů je doménou uzlu Lightning, který je připojen k LNbits jako zdroj financování, stejně jako LND nebo c-lightning. Za správu celkové přístupnosti a konfiguraci účetních funkcí a interních rozšíření jsou v systému LNbits odpovědní uživatelé Superuser nebo Admin.

LNbits funguje jako rozhraní mezi uživatelem a uzlem Lightning a poskytuje jednoduchý a uživatelsky přívětivý způsob správy a interakce s platební sítí.

Představte si LNbits jako "modulární framework Wordpress" pro váš uzel. Snadno spravovatelná platforma založená na rozšířeních, která můžete kombinovat pro mnoho případů použití.

Představte si LNbits jako svůj vlastní software pro správu bankovních financí. Váš uzel nabízí kanály pro placení a LNbits rozšiřuje váš uzel tak, abyste mohli provozovat více než jednu bleskovou peněženku, kterou váš uzel obsahuje. Tyto peněženky nemusí nutně patřit vám. Řekněme, že jako provozovatel uzlu LN již máte dostatek likvidity kanálů a finančních prostředků a nyní chcete nabídnout některé bankovní služby v bitcoinech svým přátelům, rodině, vlastnímu obchodu nebo jiným běžným obchodníkům.

Nabídnete jim jednoduchý způsob, jak si otevřít "bankovní účet" na vašem uzlu, aniž by měli přístup k ostatním peněženkám na vašem uzlu a k veškeré likviditě vašeho uzlu, ale pouze ke své části. Váš uzel (banka) funguje pouze jako poskytovatel dopravy pro jejich platby (do/z).

POZNÁMKA: všechny prostředky, které vaši "zákazníci" vloží na své bankovní účty LNbits ve vašem uzlu, půjdou přímo do kanálů LN ve vašem uzlu. To znamená, že skutečným vlastníkem těchto prostředků jste VY. Za jejich prostředky budete mít velkou zodpovědnost. Nebuďte zlí a neutíkejte s prostředky, nebuďte zlí a neúčtujte vysoké poplatky. Chceme vyjebat s fiat bankstery, ne vyjebat mezi sebou (s uživateli bitcoinu).

# Demonstrační platforma

Demo najdete na adrese [https://legend.lnbits.com](https://legend.lnbits.com). Je plně funkční a lze ji použít k seznámení se s Lightning Network a funkcemi LNbits a LNURL obecně. Přestože vám v tom nemůžeme zabránit, rádi bychom vás požádali, abyste ji nepoužívali pro produkční nastavení. Nejenže na serverech často pracujeme, abychom otestovali nové funkce, ale také bychom vás rádi povzbudili k suverénnímu provozování vlastního uzlu a LNbits. Pokud si myslíte, že provozování vlastního uzlu je pro vás v tuto chvíli příliš náročné, můžete LNbits připojit ke službě custodian funding sservice v cloudu, jako je Opennode, Luna nebo Votage, nebo k Lightning Tipbot na Telegramu, abychom jmenovali alespoň některé.

# Leták LNbits

Chcete předat základní informace obchodníkovi nebo svému známému ze stavebnictví ? S velkou radostí vám oznamujeme náš první leták, který může každý využít. Jedná se o celosvětově typický formát letáku o 6 stranách (2 sklady) a šířce 3508 a výšce 2480px.

LNbits pro obchodníky: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits pro stavitele: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Některé základy

LNbits funguje na základě protokolu LNURL, což znamená, že požadavky jsou platné ve dvou formách: buď jako https:// clearnet link (nejsou povoleny žádné samopodepsané certifikáty), nebo jako http:// v2/v3 onion link. Chcete-li nabízet služby LNbits, jako jsou kódy LNURLp/w QR nebo karty NFC, které lze používat ve volné přírodě, musíte LNbits otevřít do sítě clearnet (https).

Před instalací LNbits se ujistěte, že jste si přečetli a pochopili následující obecné pokyny o tom, co je LNbits a jaké možnosti vám nabízí.


- [Průvodce LND](https://docs.lightning.engineering/) | Instalace LND
- [Příklad konfigurace LND](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | Nastavení LND
- [CLN Guide](https://docs.corelightning.org/docs/installation) | Instalace CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Spustit strážní věž](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Velmi důležité!

Podrobnější návody na použití LNbitů v konkrétních scénářích použití naleznete zde:


- [Začínáme s LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack guide
- [ToDos pro vaši bezpečnost s LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Soukromé banky v síti Lightning](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Průvodce podsložkou
- [Spusťte peněženky správce pro své přátele a rodinu](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack guide
- [LNbits pro malou restauraci / hotel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack guide
- [Používání kopilota LNbits Streamer](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack guide
- [Spusťte svůj trh NOSTR s LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Průvodce podsložkou
- [Použití LNbits pro školní projekty nebo festivalové akce](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Průvodce pro náhradníky

# Instalace LNbits

## Základní průvodce instalací

LNbits lze nainstalovat na libovolný počítač s operačním systémem Linux. Nevyžaduje výkonný stroj nebo server, stačí dostatečná paměť RAM a určitý prostor na disku pro databázi. Může být spuštěn odděleně od uzlu BTC/LN (místní PC nebo vzdálený VPS) nebo společně na stejném stroji s uzlem nebo již nainstalovaný v softwarovém stroji s uzlem bundle.

Můžete si vybrat mezi nejběžnějšími správci balíčků, jako jsou poetry a nix. LNbits ve výchozím nastavení používá jako databázi SQLite. Můžete také použít PostgreSQL, což se doporučuje pro aplikace s vysokou zátěží. [Zde je návod pro základní instalaci pomocí poetry nebo nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Všichni, kteří se s tímto tématem teprve seznamují, zde najdou podrobnější návody krok za krokem, jak zprovoznit LNbits v konkrétních prostředích:


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) od Axel
- [LNbits na VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes
- [LNbits na cloudflare](https://www.nodeacademy.org/lnbits) od Leo

Video najdete také na stránce [dockerised Setup on a VPS with PostgreSQ, LightningTipBot as a funding source using nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Další scénáře instalace zde](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Pokud jde o softwarové uzly svazků, podívejte se do jejich specifické dokumentace o LNbits: [Citadela](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

Pokud se nezabýváte technickými záležitostmi a nechcete sami hostovat zdroj financování ani lnbits, můžete použít verzi [LNbits SaaS](https://saas.lnbits.com) (Software jako služba). Je to v podstatě jako LNbits v cloudu, ale můžete si sami definovat zdroj financování (např. svůj uzel, peněženku LNbits, LNtipbot, fakewallet atd.) a proměnné prostředí - což u jiných cloudových řešení většinou není.

[Zde je podrobný návod, jak používat LNbits SaaS pro konkrétní případy použití](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Zdroje financování

LNbits není software pro správu uzlů, ale účetní systém zaměřený na LN nad zdrojem financování LND nebo CLN. Po první instalaci můžete LNbits navštívit na adrese http://localhost:5000/.

Chcete-li změnit zdroj financování, přejděte na svůj superuživatelský server a vyberte zdroj financování v části "Správa serveru" nebo upravte soubor .env změnou `LNBITS_BACKEND_WALLET_CLASS` na požadovaný zdroj, pokud jste v souboru `.env` nastavili `adminUI=TRUE`.

Soubor .env najdete ve složce lnbits/ nebo lnbits/apps/data tak, že příkaz rozšíříte o výpis souborů v adresáři pomocí `ls -a`.

Může být také nutné nainstalovat další balíčky nebo provést další kroky nastavení a vybrat požadovaný zdroj financování. Po restartu bude vaše nové nastavení aktivní.

Jaké zdroje financování mohu pro LNbits použít?

LNbits může běžet nad mnoha zdroji financování bleskové sítě. V současné době jsou podporovány služby CoreLightning, LND, LNbits, LNPay, OpenNode a pravidelně přibývají další.

Je důležité vybrat si zdroj, který má dobrou likviditu a dobré partnery. Pokud používáte LNbits pro veřejné služby, mohou platby vašich uživatelů jen tehdy spokojeně proudit oběma směry.

Backendovou peněženku (zdroj financování) lze nakonfigurovat pomocí následujících proměnných prostředí LNbits v souboru `.env` nebo v rámci vašeho superuživatelského účtu v sekci Manage-Server.

Pokud chcete použít verzi .env, parametry najdete zde:

### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-rpc
- Jiskra (c-blesk)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TOKEN`: secret_access_key

### Démon sítě Lightning


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon nebo Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: port
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: macaroon: /file/path/admin.macaroon nebo Bech64/Hex

Místo toho můžete také použít makronku šifrovanou pomocí AES (více informací) pomocí příkazu


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Chcete-li zašifrovat svůj macaroon, spusťte `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.

### LNbits (další instance LNbits)


- Instance LNbits hostovaná na cloudovém serveru nebo na vašem domácím serveru
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! NEPOUŽÍVEJTE jej pro produkční / komerční účely, pouze pro testování !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Lightning TipBot

Chcete-li připojit svůj [Lightning Tipbot](https://t.me/LightningTipBot) z Telegramu, musíte nastavit následující parametr:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: Pro získání klíče musíte jednou spustit /api v soukromém chatu s LightningTipbotem na Telegramu.

Podívejte se také na tento návod, jak nainstalovat [LNbits s LightningTipBot přes vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### IBEX HUB

Zaregistrujte se [zde](https://ibexpay.ibexmercado.com/onboard) a získejte klíče/tokeny odtud, koncový bod je https://ibexpay-api.ibexmercado.com.

Více informací naleznete v [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

Aby poslouchání faktur fungovalo, musíte mít v LNbits veřejně přístupnou adresu URL a nastavit [LNPay webhook](https://dashboard.lnpay.co/webhook/) ukazující na `<Váš hostitel LNbits>/wallet/webhook` s událostí "Příjem peněženky" a bez zadání tajemství. Nastavení `https://mylnbits/wallet/webhook` bude url koncového bodu, který bude informován o každé platbě.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

### OpenNode

Aby faktura fungovala, musíte mít v LNbits veřejně přístupnou adresu URL. Nastavení webhooku je volitelné.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

### Alby

Alby je rozšíření prohlížeče s funkcemi peněženky LN a účtu LNDHUB, které lze použít jako zdroj financování LNbits. [Více informací zde](https://getalby.com/).

Aby faktura fungovala, musíte mít v LNbits veřejně přístupnou adresu URL. Žádné ruční nastavení webhooku není nutné. Přístupový token Alby si můžete vygenerovat zde: https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

## Další / Průvodci řešením problémů

Zde jsou další pokyny pro případ, že byste je potřebovali. Kliknutím na šipku rozbalíte popis.

### The Killswitch 🚨

V poslední době se objevilo tolik nebezpečných chyb nejen v celém prostoru, ale i v LNbits, že jsme se rozhodli s tím něco udělat. Nyní se můžete přihlásit k odběru varování a/nebo k přímé akci, pokud se opět objeví zranitelnost nebo chyba, která by mohla vést ke ztrátě finančních prostředků.

![killswitchn](assets/lnbits-killswitch.webp)

Pokud se přepne na void-wallet, všechny typy uživatelů na instanci uvidí žlutý banner, kde byste normálně našli oznámení "LNbits is in Beta" vedle tématu/jazyka vpravo nahoře - a je to nejzřetelnější náznak, že se něco stalo. Podívejte se na svůj nový server-záložku zvýrazněnou zeleně v levé části okna.

Jak to funguje? Když je killswitch povolen, tajný repozitář na githubu, který je dostupný pouze hlavnímu týmu LNbits, bude kontrolován v intervalu X minut (který lze zadat). Pokud je v tomto repozitáři zveřejněna zranitelná chyba, slouží to jako signál, který spustí killswitch na všech instalacích, které se přihlásily k odběru, a přejde vaše instance lnbits na používání peněženky void. Pokud se mraky vyčistily a vy jste nainstalovali bezpečnostní aktualizaci, můžete zdroj financování nastavit na svůj uzel, peněženku nebo cokoli jiného, co používáte, znovu také prostřednictvím sekce Správa serveru. Na této wiki je sekce o přepínání zdrojů financování, pokud nevíte, co nastavit.

### Rozdíl mezi správcem a superuživatelem

Uživatelské rozhraní správce systému LNbits umožňuje měnit nastavení systému LNbits prostřednictvím rozhraní LNbits. Ve výchozím nastavení je vypnuto a při prvním nastavení proměnné prostředí `LNBITS_ADMIN_UI=true` v souboru `.env` se nastavení inicializuje a bude použito. Od této chvíle se místo nastavení ze souboru .env použijí nastavení z databáze.

### Super uživatel

S uživatelským rozhraním správce jsme zavedli superuživatele, který má přístup k serveru, takže může měnit nastavení, která mohou způsobit pád serveru nebo jeho nereagování prostřednictvím frontendu a rozhraní API, jako je např. změna zdroje financování. Superuživatel je uložen pouze uvnitř tabulky nastavení v databázi. Po "obnovení výchozího nastavení" a restartu se vytvoří nový superuživatel. Přidali jsme také dekorátor pro trasy API, který kontroluje existenci superuživatele. Jeho ID se nikdy neposílá přes api a frontend a pouze dostává bool (ano/ne), zda jste superuživatel, nebo ne.

Pouze superuživatel může přes sekci "Top Up" převádět satoshis do různých peněženek.

Stejně tak můžete superuživatele po jeho vytvoření odeslat prostřednictvím webhooku do jiné služby. Více informací zde https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `třída SaaSSettings`

Ve frontendu najdete také možnost změnit obrázek obchodu, který se zobrazuje na stránce "vytvořit peněženku", a to tak, že otevřete sekci Správa serveru a vyberete možnost Motiv -> Vlastní logo.

### Uživatelé správce

Proměnná prostředí: `LNBITS_ADMIN_USERS`, seznam ID uživatelů oddělený čárkou. Uživatelé administrátora mohou měnit nastavení v uživatelském rozhraní administrátora - s výjimkou nastavení zdroje financování, protože to by vyžadovalo restart serveru a mohlo by potenciálně způsobit jeho nedostupnost. Také mají přístup ke všem rozšířením, která jsou jim vyhrazena v `LNBITS_ADMIN_EXTENSIONS`.

### Povolení uživatelé

Proměnná prostředí: `LNBITS_ALLOWED_USERS`, seznam ID uživatelů oddělený čárkou. Definováním těchto uživatelů již nebude možné LNbits používat veřejně. Přístup k frontendu LNbits pak budou mít pouze definovaní uživatelé a administrátoři.

#### Aktualizace LNbits

Běžná aktualizace místní instance LNbits se provádí jednoduše zkopírováním a vložením následujících příkazů CLI:

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

Pokud používáte Raspiblitz nebo MyNode, můžete navíc potřebovat

```
sudo systemctl restart lnbits
```

na konci, protože spouští LNbits jako službu.

V systému Umbrel/Citadel by příkazy byly následující

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### Přechod z SQLite na PostgreSQL

Pokud již máte LNbits nainstalovaný a spuštěný na databázi SQLite, doporučujeme přejít na postgres, pokud plánujete provozovat LNbits ve velkém měřítku.

Součástí je skript, který migraci snadno provede. Musíte mít již nainstalovaný Postgres a mělo by být zadáno heslo pro uživatele (viz výše uvedený návod k instalaci Postgresu). Kromě toho musí vaše instance LNbits jednou běžet na Postgresu, aby se implementovalo schéma databáze, a teprve poté může migrace fungovat:

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Doufejme, že nyní vše funguje a bude migrovat... Spusťte LNbits znovu a zkontrolujte, zda vše funguje správně.

#### Zálohování a obnovení databáze

Viz [tento velmi podrobný průvodce procesem zálohování a obnovy](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### Financování peněženky LNbits z mého uzlu nefunguje

Pokud chcete odesílat satelity ze stejného uzlu, který je zdrojem financování LNbitů, musíte upravit soubor lnd.conf.

Je třeba zahrnout tyto parametry: `allow-circular-route=1`

Učiňte tak v části Application options v souboru lnd.conf. Na některých uzlech svazků by jinak mohlo dojít k selhání spuštění LND.

POZNÁMKA: Pro přidání prostředků na účet LNbits doporučujeme použít nové rozšíření adminUI s možností "TopUp".

#### Chyba 426

Zobrazí se mi chyba: "lnurl musí být doručen přes veřejně přístupnou doménu https nebo tor. 426 upgrade required"</summary>

Tato chyba je obvykle způsobena tím, že LNbits za tunelem ngnix nepředává adresu LNURL správně. Zastavte LNbits a upravte soubor .env přidáním tohoto řádku:

`FORWARDED_ALLOW_IPS=*`

Pokud používáte konfiguraci ngnix, ujistěte se, že máte tyto hlavičky v konfiguraci ngnix:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Chyba sítě

Při skenování QR se mi zobrazí "https error", "network error" nebo jiné</summary>

Špatná zpráva, jedná se o chybu směrování, která může mít mnoho příčin. Nejprve zkontrolujte QR's LNURL pomocí [Lightning Decoder](https://lightningdecoder.com/), zda v něm nenajdete něco divného. Vyzkoušíme si několik nejpravděpodobnějších problémů a jejich řešení.

LNbits běží pouze přes Tor, nemůžete jej otevřít na veřejné doméně, jako je lnbits.yourdomain.com


- Vzhledem k tomu, že chcete, aby vaše nastavení zůstalo takové, otevřete peněženku LNbits pomocí URI .onion a vytvořte ji znovu. Tímto způsobem se vygeneruje QR, které bude přístupné přes toto .onion URI, takže pouze přes tor. Nevytvářejte tento QR z .local URI, protože nebude dosažitelný přes internet - pouze z vaší domácí sítě LAN.
- Otevřete aplikaci peněženky LN, kterou jste použili ke skenování QR, a tentokrát pomocí tor (viz nastavení aplikace peněženky). Pokud aplikace tor nenabízí, můžete místo toho použít Orbot (Android). Podrobný návod, jak otevřít LNbity pro clearnet/https, najdete v části instalace.

#### Zabránit ostatním v generování peněženek na mých LNbitech

Když spustíte LNbits v clearnetu, v podstatě každý si na něm může vygenerovat peněženku. Vzhledem k tomu, že prostředky vašeho uzlu jsou vázány na tyto peněženky, možná tomu budete chtít zabránit. Existují dva způsoby, jak toho dosáhnout:

Nastavte povolené uživatele a přípony v souboru `.env` ([viz příklad env zde](https://github.com/lnbits/lnbits/blob/main/.env.example)). To funguje pouze v případě, že v souboru .env použijete nastavení `adminUI=FALSE`, v opačném případě to musíte provést v sekci Správa serveru -> Uživatelé -> Povolení uživatelé. Všichni ostatní poté nebudou mít povolení.

#### Přizpůsobení doby platnosti faktury

Nyní můžete generovat faktury s vlastní expirací. Kompatibilní s backendy: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet!

Můžete nastavit `LIGHTNING_INVOICE_EXPIRY` ve svém souboru .env nebo pomocí AdminUI změnit výchozí hodnotu pro všechny faktury. V koncovém bodě /api/v1/payments je také nové pole, kde můžete nastavit expiraci v datech JSON.

## Peněženka-URL odstraněna

### Peněženka na demo serveru legend.lnbits

Vždy si na bezpečném místě uložte kopii své peněženky-URL, Export2phone-QR nebo LNDhub pro své vlastní peněženky. LNbits vám je při ztrátě NEMŮŽE pomoci obnovit.

### Peněženka na vlastním zdroji financování/uzlu

Vždy si na bezpečném místě uložte kopii své peněženky-URL, Export2phone-QR nebo LNDhub pro své vlastní peněženky. Všechny uživatele LNbits a identifikační čísla peněženek najdete v rozšíření správce uživatelů LNbits nebo v databázi sqlite. Chcete-li upravit nebo přečíst databázi LNbits, přejděte do složky LNbits /data a vyhledejte soubor s názvem sqlite.db. Můžete jej otevřít a upravovat pomocí programu Excel nebo pomocí specializovaného editoru SQL, jako je [SQLite browser](https://sqlitebrowser.org/).

Také můžete vypisovat peněženky přes cli a zobrazit každou peněženku v databázi.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

Výstup bude vypadat takto

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

a tyto hodnoty chcete vložit do url takto

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Přičemž f8a43fc363ea428db5c53b3559935f1f nahradíte hodnotou, která je před jménem (v našem příkladu f8a43fc363ea428db5c53b3559935f1f), a 1280ff5910a9c485a782a2376f338b6c je váš uživatel a měla by se stát hodnotou uvedenou za jménem. Pro ukončení sqlite3 zadejte

```
.quit
```

#### LNURL pro bleskovou adresu a naopak

Zkuste tento [kodér](https://lnurl-codec.netlify.app/) od fiatjaf nebo [tento](https://lightningdecoder.com/). Pro platbu nebo kontrolu LNURLp můžete také použít [LNurlpay](https://wwww.lnurlpay.com/). Mělo by na něm být uvedeno HTTPS, NE HTTP.

#### Konfigurace komentáře, který lidé vidí při placení na můj LNURLp QR

Při vytváření LNURL-p se pole pro komentář ve výchozím nastavení nevyplňuje. To znamená, že k platbám není povoleno připojovat komentáře.

Chcete-li povolit komentáře, přidejte délku znaků pole, od 1 do 250. Jakmile tam vložíte číslo, pole pro komentář se zobrazí v procesu platby. Můžete také upravit již vytvořený LNURL-p a přidat toto číslo.

![lnbits comments](assets/lnbits-comments.webp)

#### Vklad onchain BTC na LNbits

Existují dva způsoby, jak vyměnit saty z onchainu BTC na LN BTC (resp. na LNbits).

##### Prostřednictvím externí výměnné služby.

Ostatní uživatelé, kteří nemají přístup k vašemu LNb, mohou použít výměnnou službu, například [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) nebo [ZigZag](https://zigzag.io/). To je užitečné, pokud ze své instance LNbits poskytujete pouze faktury LNURL/LN, ale plátce má pouze onchain saty, takže bude muset na své straně nejprve vyměnit tyto saty. Postup je jednoduchý: uživatel pošle onchain btc do swapové služby a jako cíl swapu poskytne LNURL/LN fakturu z LNbits.

##### Použití rozšíření Onchain a Boltz LNbits.

Mějte na paměti, že se jedná o samostatnou peněženku, nikoliv o peněženku LN btc, kterou LNbits reprezentuje jako "vaši peněženku" při vašem zdroji financování LN. Tuto onchain peněženku lze také použít k výměně LN btc do (např. vaší hardwarové peněženky) pomocí rozšíření LNbits Boltz nebo Deezy. Pokud provozujete webový obchod, který je propojen s vaším LNbits pro platby LN, je velmi praktické pravidelně vypouštět všechny saty z LN do onchainu. To vede k tomu, že ve vašich LN kanálech je více místa, abyste mohli přijímat nové čerstvé saty.

Postup pro ty, kteří nemají hardwarovou peněženku Bitcoin:


- Pomocí peněženky Electrum nebo Sparrow vytvořte novou onchain peněženku a záložní seed uložte na bezpečné místo.
- Přejděte na informace o peněžence a zkopírujte xpub.
- Přejděte na LNbits - rozšíření Onchain a vytvořte novou peněženku pouze pro hodinky s tímto xpubem.
- Přejděte na LNbits - Rozšíření Tipjar a vytvořte nový Tipjar. Kromě peněženky LN vyberte také možnost onchain.
- Volitelně - Přejděte na LNbits - rozšíření SatsPay a vytvořte nový poplatek za onchain btc. Můžete si vybrat mezi onchain a LN nebo oběma. Poté se vytvoří faktura, kterou lze sdílet.
- Nepovinné - Pokud používáte LNbits propojené se stránkou Wordpress + Woocommerce, jakmile vytvoříte/spojíte peněženku pouze pro hodinky s peněženkou LN btc shopu, zákazník bude mít obě možnosti platby na stejné obrazovce.

Při přijetí platby v LNbits se v protokolu transakcí zobrazí pouze obnovený typ transakce.

![lnbits payment details](assets/lnbits-payment-details.webp)

V přehledu transakcí najdete malou zelenou šipku pro přijaté a červenou šipku pro odeslané prostředky.

Pokud na tyto šipky kliknete, zobrazí se vyskakovací okno s podrobnostmi o připojených zprávách a jméno odesílatele, pokud je uvedeno.

Konfigurace jména, které se má zobrazovat v rámci plateb, v LNbits to v současné době není možné - ale přijímat. To je možné pouze v případě, že peněženka LN odesílatele podporuje [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) jako [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

V části s podrobnostmi o transakcích LNbits se pak zobrazí alias/pseudonym (klikněte na šipky). Všimněte si, že tam můžete uvést libovolné jméno, které nemusí souviset se skutečným jménem odesílatele, pokud takové jméno obdržíte.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Chcete-li importovat svůj účet LNbits do aplikace peněženky, otevřete LNbits s účtem / peněženkou, kterou chcete používat, přejděte na "spravovat rozšíření" a aktivujte rozšíření LNDHUB. Otevřete rozšíření LNDHUB, vyberte peněženku, kterou chcete používat, a naskenujte buď "admin", nebo "invoice only" QR v závislosti na úrovni zabezpečení, kterou pro danou peněženku chcete.

Jako peněženkové aplikace pro účet lndhub můžete použít [Zeus](https://zeusln.app/) nebo [Bluewallet](https://bluewallet.io/), přičemž BW podporuje více než jednu takovou peněženku.

Přitom doporučujeme nastavit síťový URI LN na URI vlastního uzlu. Pokud je vaše instance LNbits pouze Tor, musíte tyto aplikace používat také s aktivovaným Tor. Také v tomto případě musíte stránku LNbits otevřít prostřednictvím své adresy Tor .onion.

Pokud se vám při použití ypub v rozšíření On-chain objeví chyba "unsupported hash type", zkontrolujte, zda vaše instance LNbits používá python 3.10, může být ovlivněna [tímto problémem](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Upravte soubor openssl.cnf podle popisu v odpovědi na stackoverflow a restartujte LNbits.

## Tvorba nástrojů a konstrukce pomocí LNbits

LNbits má nejrůznější [otevřené API](https://legend.lnbits.com/docs) a nástroje pro programování a připojení k mnoha různým zařízením pro miliardu případů použití.

Pokud se stavěním začínáte, začněte s tímto [MakerBits prezentace](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) od Bena Arca o stavbě gadgetů založených na LNbits.

### DŮLEŽITÉ:


- LNbits funguje na základě protokolu LNURL, jehož požadavky jsou platné ve dvou formách: buď jako https:// clearnet link (nejsou povoleny žádné certifikáty podepsané vlastním jménem), nebo jako http:// v2/v3 onion link. Chcete-li nabízet služby LNbits, jako jsou kódy LNURLp/w QR nebo karty NFC, které lze používat ve volné přírodě, je třeba otevřít LNbits do sítě clearnet (https).
- K napájení zařízení esp32 používejte pouze kabely DATA. Ne všechny kabely podporují kromě napájení esp také data. Nebyli byste první, kdyby kabel dodaný s esp byl pouze napájecí
- Dbejte na to, abyste nepoužívali USB-Hub s připojenými dalšími zařízeními. To může vést k podivným efektům, které se obtížně ladí (např. nespuštění nebo zastavení).
- Pro realizaci projektů esp s operačním systémem MacOS budete potřebovat ovladač UART Bridge Driver. Pokud máte problémy s ovladačem v systémech Mac nebo Linux, můžete je najít zde, nebo pokud se jedná o TTGO Display, zde. Pokud jste na Windows a máte problémy s připojením, ujistěte se, že jste si stáhli STAROU verzi 11.1.0, protože novější nefunguje! Sériový terminál pro kontrolu připojení najdete také zde - nastavte přenosovou rychlost 115200.
- Přestože je mnohem pohodlnější používat Platform.io (např. závislosti se instalují automaticky), doporučujeme všem, kteří se s tvorbou počítačů teprve seznamují, používat Arduino.
- Displej TT-Go S3: Barva záložky ochranné fólie displeje vám napoví, který přesně ovladač (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) byl použit k její výrobě. Ponechte si ji, abyste mohli ladit, pokud se naprogramujete a obrazovka nezobrazí správně grafiku, např. špatné barvy, zrcadlení obrazu nebo rozhozené pixely na okrajích. Pokud byste to někdy potřebovali udělat, existuje epický návod na přizpůsobení pro různé displeje
- Vždy používejte malá písmena lnurl239xx místo LNURLl239xx
- Přidáním lightning:lnurl1234xyz se vytvoří QR, který při skenování požádá o otevření peněženky uživatele pro tuto fakturu (poslední nainstalovaná aplikace lightning v systému iOS, nastavení v systému Android)
- Pokud flashujete esp32 přes web, bude fungovat pouze s těmito prohlížeči (TL:DR Chrome, Edge a Opera).
- Vezměte prosím na vědomí tento odkaz PIN-OUT pro esp
- Pokud používáte FOSSoftware nebo FOSGuides, vždy uveďte odkaz na autora. Každý rád sleduje, jak jeho dítě roste, a také to iniciuje řetězec budování, který je docela úžasné sledovat :)

Pokud potřebujete pomoc s projektem, přijďte do skupiny [Makerbits Telegram Group](https://t.me/makerbits) - máme pro vás pomoc!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Zde je několik kategorií projektů, které můžete vytvořit pomocí LNbits:


- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardwarová peněženka](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Prodejní automat](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora a Mesh Networking](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [POMOCNÍCI A ZDROJE](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Další příklady projektů "Powered by LNbits" zde](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Případy použití pro LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)