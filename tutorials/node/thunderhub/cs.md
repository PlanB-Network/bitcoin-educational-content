---
name: ThunderHub
description: Interface Správa bleskového uzlu web LND
---
![cover](assets/cover.webp)



## Úvod



ThunderHub je **open-source správce uzlů Lightning (LND)**, který nabízí intuitivní Interface přístupný z jakéhokoli zařízení nebo prohlížeče.



**Hlavní funkce:**




- **Monitorování**: Globální přehled o zůstatcích, kanálech, transakcích a statistikách směrování
- **Vedení**: Otevírání/zavírání kanálů, příchozí/odchozí platby, vyrovnávání kanálů
- **Integrace**: Podpora LNURL, výměna přes Boltz, zálohování Amboss
- **Interface reaguje**: Kompatibilní s mobilními zařízeními, tablety a stolními počítači s tmavými/světlými motivy



ThunderHub se snadno integruje se službami **Umbrel**, **Voltage**, **RaspiBlitz** a **MyNode**, což zjednodušuje každodenní správu uzlu.



**ThunderHub je vhodný zejména pro provozovatele, kteří hledají ergonomické řešení Interface pro správu svých kanálů, řízení likvidity (rebalancování), monitorování transakcí a integraci služeb třetích stran, jako je například Amboss. Bezpečnost je zajištěna prostřednictvím místního připojení nebo připojení přes Tor.**



Pokud ještě nemáte uzel Lightning, doporučujeme vám postupovat podle našeho návodu LND Umbrel:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalace



ThunderHub lze nainstalovat několika různými způsoby v závislosti na hostitelském prostředí uzlu Lightning. Ať už použijete řešení na klíč (Umbrel, Voltage, RaspiBlitz, MyNode, Start9 atd.), nebo ruční instalaci, ThunderHub je často k dispozici bez většího úsilí. Níže popisujeme dva běžné přístupy: prostřednictvím obchodu s aplikacemi Umbrel a prostřednictvím ruční instalace (použitelné pro server nebo samohostitelskou distribuci).



### Instalace přes Umbrel



Umbrel integruje ThunderHub do svého **App Store**, takže instalace je velmi jednoduchá. Není potřeba příkazový řádek ani ruční konfigurace: vše se provádí prostřednictvím Interface Umbrel. Stačí postupovat podle následujících kroků:





- Otevřete přístrojovou desku Umbrel: Připojte se k webu Interface uzlu Umbrel (např. `http://umbrel.local` v místní síti nebo přes jeho `.onion` Address, pokud používáte Tor).
- **Přístup do App Store**: V hlavní nabídce Umbrel klikněte na "App Store" (nebo "App"). V seznamu dostupných aplikací vyhledejte **ThunderHub**.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Nainstalujte ThunderHub**: Klepněte na aplikaci ThunderHub a poté na tlačítko instalovat. V případě potřeby potvrďte. Umbrel automaticky stáhne a nasadí ThunderHub na váš uzel.





- **Spusťte aplikaci**: Po dokončení instalace (několik desítek sekund) se ThunderHub objeví na domovské stránce. Klepnutím na ikonu ji otevřete. Aplikace ThunderHub se spustí v prohlížeči.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Důležité:** Při prvním otevření služby ThunderHub se automaticky zobrazí **přednastavené heslo** potřebné k přihlášení. Volba "Nezobrazovat znovu" umožňuje toto zobrazení skrýt pro budoucí připojení. **Důrazně vám doporučujeme:**




- Uložte toto heslo okamžitě do správce hesel
- Zkopírujte ji pro použití v dalším kroku
- Po uložení hesla zaškrtněte políčko "Nezobrazovat znovu"



![Page de connexion de ThunderHub](assets/fr/03.webp)



Poté budete přesměrováni na přihlašovací stránku, kde musíte zadat heslo, které jste zkopírovali v předchozím kroku, abyste odemkli zařízení Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel se postará o to, aby ThunderHubu poskytl informace o připojení LND (certifikát TLS, makra pro správu atd.) na pozadí, takže nemusíte provádět žádnou další konfiguraci. Stačí několik kliknutí a na uzlu Umbrel bude ThunderHub spuštěn.



### Ruční instalace (na vlastním hostingu, kromě Umbrelu)



Pro uživatele mimo Umbrel (např. na osobním serveru, Raspberry Pi s RaspiBlitz nebo *samostatné* instalaci) vyžaduje instalace ThunderHubu několik dalších kroků. Níže popisujeme instalaci ze zdrojových kódů a konfiguraci podle [oficiální dokumentace ThunderHub](https://docs.thunderhub.io).



#### Instalace



**Předpoklady:** Ujistěte se, že váš systém splňuje minimální požadavky podle [nastavení dokumentace](https://docs.thunderhub.io/setup):




- **Node.js** verze 18 nebo vyšší
- nainstalováno **npm**
- Přístup k ověřovacím souborům LND :
  - Certifikát TLS LND (`tls.cert`)
  - LND administration macaroon (`admin.macaroon`)
  - LND gRPC služba Address (název hostitele:port) (výchozí `127.0.0.1:10009` lokálně)



**1. Získat kód ThunderHub:** Klonujte úložiště GitHub projektu podle popisu v [instalační dokumentaci](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. nainstalujte závislosti a sestavte aplikaci:**



```bash
npm install
npm run build
```



Tyto příkazy nainstalují všechny potřebné moduly a poté aplikaci zkompilují (ThunderHub je napsán v jazyce TypeScript/React).



**3. Pozdější aktualizace:** ThunderHub nabízí několik způsobů budoucích aktualizací:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Konfigurace (nastavení)



**1. Hlavní konfigurační soubor:** Vytvořte soubor `.env.local` v kořenovém adresáři ThunderHubu a přizpůsobte si konfiguraci (zabráníte tak přepsání nastavení při aktualizacích). Hlavní proměnné podle [dokumentace k nastavení](https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Konfigurace účtů serveru:** Vytvoření souboru YAML uvedeného v poli `ACCOUNT_CONFIG_PATH` :



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Vzdálený přístup:** Chcete-li se připojit ke vzdálenému uzlu LND, přidejte do souboru `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Zabezpečení:** Při prvním spuštění ThunderHub **automaticky** skryje `masterPassword` a všechna hesla účtů v souboru YAML, aby se zabránilo tomu, že budou hesla na serveru v otevřeném textu.



**5. Spuštění ThunderHubu:**



```bash
npm start
```



Ve výchozím nastavení server naslouchá na portu 3000. Přistupte na `http://localhost:3000` (nebo `http://ip-serveur:3000` z místní sítě).



**6. Alternativa Docker:** ThunderHub poskytuje oficiální obrazy Docker:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Zobrazí se přihlašovací stránka služby ThunderHub. Vyberte nakonfigurovaný účet a zadejte heslo pro přístup k ovládacímu panelu.



**Instalace v jiných distribucích:** Předpřipravené distribuce uzlů (RaspiBlitz, MyNode, Start9 atd.) obvykle nabízejí nativní podporu ThunderHubu prostřednictvím příslušných administračních rozhraní.



**Další informace:** Přečtěte si kompletní oficiální dokumentaci :




- **Instalace:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Konfigurace:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Tyto zdroje podrobně popisují pokročilé možnosti, jako jsou účty SSO, šifrované makra, konfigurace TOR a mnoho dalšího.



Po instalaci a zpřístupnění služby ThunderHub můžete využívat všechny její funkce. V následující části se podíváme na ThunderHub Interface a jeho různé karty, abychom vás provedli jeho používáním.



## Prezentace Interface



Aplikace Interface ThunderHub je strukturována kolem hlavní nabídky (obvykle se zobrazuje v levém bočním sloupci), která obsahuje několik klíčových oddílů. Každá z nich odpovídá určitému aspektu správy uzlu Lightning. Projděme si je jednu po druhé:





- **Domů** - karta Domů s obecným řídicím panelem (přehled uzlů a rychlých akcí).
- **Dashboard** - Přizpůsobitelný dashboard s widgety a pokročilými metrikami.
- **Peers** - Správa peerů Lightning (připojení k jiným uzlům).
- **Kanály** - podrobná správa kanálů Lightning.
- **Rebalance** - nástroj pro vyrovnávání kanálů (kruhové platby).
- **Transakce** - Historie plateb Lightning (transakce LN).
- **Forwards** - Statistiky směrování (platby předané vaším uzlem).
- **Řetězec** - Nodeovo portfolio On-Chain (On-Chain BTC: UTXOs, transakce).
- **Amboss** - Integrace se systémem Amboss (monitorování uzlů, zálohování atd.).
- **Nástroje** - Různé nástroje (zálohy, podepsané zprávy, makra, zprávy atd.).
- **Výměna** - funkce výměny On-Chain/Lightning prostřednictvím Boltze.
- **Statistiky** - Pokročilé statistiky a metriky výkonu uzlů.



*(Poznámka: V závislosti na verzi ThunderHubu mohou mít některé části mírně odlišné nadpisy nebo další funkce, ale obecné zásady zůstávají stejné)*



### Domů (Obecný ovládací panel)



Karta **Home** služby ThunderHub je domovská stránka, která se zobrazí po přihlášení. Obsahuje **obecný ovládací panel**, který nabízí **globální přehled** o stavu uzlu Lightning a navrhuje **rychlé akce** pro běžné operace. Zde je uvedeno, co zde obvykle najdete:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Zůstatky a kapacity:** V horní části stránky zobrazuje ThunderHub vaše dostupné zůstatky. Obvykle zde uvidíte zůstatek On-Chain (Bitcoin On-Chain v uzlu Wallet, symbolizovaný symbolem Anchor ⚓) a zůstatek Blesk (kapacity vašich kanálů, symbolizované bleskem Bolt ⚡). Tím získáte okamžitou představu o prostředcích, které máte v On-Chain a Blesku. Pokud máte více účtů nebo kanálů, ujistěte se, že jste na tom správném (např. Mainnet vs. Testnet).





- **Klíčové statistiky:** Na ovládacím panelu lze zobrazit některé globální metriky uzlu - například počet otevřených kanálů, počet připojených partnerů, získané poplatky za směrování (pokud jsou k dispozici) atd. Jedná se o shrnutí nedávné aktivity a stavu uzlu.





- **Rychlé akce:** Přístrojový panel obsahuje tlačítka pro rychlé provádění nejběžnějších úloh bez nutnosti procházet nabídkami. Mezi tyto rychlé akce patří :





- **Duch**: Nastavte si vlastní blesk Address prostřednictvím služby Amboss.
- **Darovat**: Přispějte prostřednictvím aplikace Lightning.
- Přihlášení/přejít na: Připojte se ke svému účtu Amboss (Quick Connect) a přejděte přímo na **Amboss.space**, kde si můžete zobrazit informace o svém uzlu.
- **Address**: Pro provedení platby zadejte Lightning Address.
- **Otevřeno**: Otevřete nový kanál Lightning. Kliknutím se otevře formulář pro zadání URI vzdáleného uzlu, na který se má kanál otevřít, částky a případně maximálního poplatku On-Chain, který se má použít.
- **Dekódování**: Před platbou dekódujte Lightning Invoice nebo LNURL a zobrazte podrobnosti.
- **LNURL**: Zpracovávejte LNURL pro platby nebo výběry Lightning.
- **LnMarkets Přihlášení**: Přihlášení k LnMarkets pro obchodování.



Tyto rychlé akce umožňují provádět nejčastější operace přímo z domovské stránky, aniž byste museli procházet různé karty Interface.



Stručně řečeno, ovládací panel ThunderHubu vám poskytuje **rychlý pohled** na váš uzel a umožňuje provádět nejčastější operace (odesílání/příjem, otevření kanálu) jediným kliknutím. Je to ideální výchozí bod pro každodenní správu.



### Přístrojová deska



Sekce **Dashboard** je oddělena od karty Domů a nabízí pokročilejší, přizpůsobitelný panel. Tato sekce umožňuje vytvořit vlastní zobrazení s konkrétními widgety podle vašich potřeb jako provozovatele uzlu.





- **Přizpůsobitelné widgety:** Na rozdíl od domovské stránky, která má pevné rozvržení, si na hlavním panelu můžete přesně vybrat, které widgety Elements se mají zobrazit a jak je uspořádat.



![Dashboard sans widgets activés](assets/fr/06.webp)



Pokud nejsou povoleny žádné widgety, zobrazí se zpráva "Nejsou povoleny žádné widgety!" s tlačítkem "Nastavení" pro přístup k parametrům přizpůsobení.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



V nastavení si můžete vybrat z široké nabídky widgetů rozdělených do kategorií: "Blesk - informace", "Blesk - tabulka", "Blesk - graf" atd. Každý widget lze jednotlivě aktivovat nebo deaktivovat pomocí tlačítek "Zobrazit/skrýt".



![Bas de la page des paramètres](assets/fr/08.webp)



V dolní části nastavení najdete tlačítko "Na ovládací panel", kterým se vrátíte na ovládací panel, a tlačítko "Obnovit widgety", kterým obnovíte výchozí zobrazení.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Po konfiguraci může panel zobrazovat různé grafy a metriky: Můžete zobrazit grafy bleskových plateb, počet vystavených faktur, statistiky předaných faktur, podrobné zůstatky atd.





- **Pokročilé metriky:** Přístup k podrobnějším statistikám výkonu uzlu s grafy a údaji v reálném čase.





- **Konfigurovatelný přehled:** Přizpůsobte si zobrazení tak, aby vyhovovalo běžnému uživateli nebo profesionálnímu operátorovi, který spravuje více směrovacích kanálů.





- **Modulární Interface:** Podle potřeby přidávejte nebo odebírejte widgety: grafy forwardů, metriky likvidity, upozornění na stav uzlu atd.



Tato část je užitečná zejména pro pokročilé uživatele, kteří chtějí sledovat konkrétní metriky nebo získat podrobnější technický přehled o svém uzlu Lightning. Doplňuje sekci Domů tím, že nabízí větší flexibilitu a kontrolu nad zobrazováním informací.



### Kolegové



V části **Peers** jsou uvedeny všechny uzly Lightning aktuálně připojené k vašemu uzlu jako peers. **Peer** je přímé spojení mezi uzly na Lightning Network. Váš uzel může být připojen k peerům i bez otevřeného kanálu (např. jen k informacím o drbech v síti Exchange), nebo samozřejmě každý otevřený kanál automaticky znamená připojeného peera.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Na kartě Peers uvidíte :





- **Informační sloupce:** V Interface se zobrazují užitečné podrobnosti, jako je stav synchronizace, typ připojení (clearnet nebo Tor), ping, přijaté/odeslané satoshy a objem vyměněných dat.
- **Přidání partnera:** ThunderHub umožňuje ruční připojení k novému partnerovi pomocí tlačítka **"Přidat"** v pravém horním rohu. Musíte zadat URI uzlu (ve formátu `<veřejný_klíč>@<socket>`). Po ověření odešle ThunderHub příslušný příkaz `lncli connect`. Pokud je uzel online a přístupný, bude přidán do seznamu partnerů.



### Kanály



Karta **Kanály** je srdcem správy kanálů aplikace Lightning. Je to pravděpodobně sekce, do které budete nahlížet nejčastěji. Představuje **všechny vaše kanály Lightning** s jejich podrobnostmi a umožňuje provádět akce správy těchto kanálů.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Na stránce Kanály najdete následující informace:





- **Zobrazení seznamu kanálů:** Každý otevřený (nebo otevíraný/zavíraný) kanál je uveden v seznamu, obvykle s aliasem vzdáleného uzlu, celkovou kapacitou kanálu a barevným pruhem znázorňujícím rozložení místní a vzdálené likvidity. ThunderHub používá barevný kód (často modrý/Green) nebo procentní podíl pro označení vyváženosti kanálu: například modrá barva pro místní podíl, Green pro vzdálený podíl. Pokud je kanál dokonale vyvážený (50/50), bude mít sloupec polovinu každé barvy. To umožňuje na první pohled určit, které kanály jsou nevyvážené (všechny modré = téměř všechny místní, všechny Green = téměř všechny vzdálené).





- **Informační sloupce:** V Interface se zobrazují podrobné sloupce včetně stavů, dostupných akcí, informací o partnerovi, ID kanálu, kapacity, aktivity, poplatků a zůstatku s grafickým zobrazením likvidity.





- **Konfigurace zobrazení:** Ozubené kolečko v pravém horním rohu umožňuje přizpůsobit zobrazení kanálu podle vašich preferencí.





- **Stav:** Zobrazí se také indikátory stavu - např. `Aktivní` (kanál je otevřený a funkční), `Offline` (partner je odpojen, takže kanál je momentálně nepoužitelný), `Čeká` (pro otevření nebo uzavření, které čeká na potvrzení On-Chain).





- **Akce na kanálu:** Pro každý kanál poskytuje ThunderHub tlačítka akcí (často ve formě ikon):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- **Úprava poplatků:** Pomocí funkce Interface "Aktualizace zásad kanálu" můžete upravit všechny parametry kanálu: Základní poplatek, sazbu poplatku (v ppm), deltu CLTV, maximální HTLC a minimální HTLC. To vám umožní upravit zásady poplatků individuálně pro každý kanál s cílem přilákat (nebo odradit) směrovaný provoz. *(Poznámka: ThunderHub nenahrazuje automatický nástroj pro správu poplatků, ale pro ruční nastavení je velmi účinný)*
- Zavřít kanál (**Zavřít**): "Zavírací kanál" Interface umožňuje volbu mezi **kooperativním zavíráním** (výchozí) nebo **vynuceným zavíráním** (*Force Close*) definováním poplatků (v Sats/vByte). **Důležité:** pokud je to možné, vždy dávejte přednost kooperativnímu uzavření, abyste se vyhnuli zpoždění vypořádání On-Chain a vyšším poplatkům. ThunderHub vám sdělí, zda je partner online (možnost kooperace), nebo ne. V případě vynuceného uzavření nezapomeňte potvrdit, protože je nevratné a vyvolá zametací transakci s časovým zámkem (obvykle 144 bloků nebo ~1 den na Bitcoin Mainnet).
- **Otevření nového kanálu:** Chcete-li otevřít nový kanál, klikněte na ozubené kolečko v pravém horním rohu stránky Kanály a vyberte možnost "Otevřít". Poté můžete zahájit kanál s novým nebo stávajícím partnerem. Výhodou použití této stránky je, že máte před sebou seznam svých stávajících kanálů, což vám může pomoci při rozhodování, kde nový kanál otevřít.



Sekce Kanály vám zkrátka umožňuje **přesné ovládání jednotlivých kanálů**. Zde řídíte přidělování likvidity, rozhodujete, které kanály ponechat nebo zrušit, a nastavujete parametry směrování pro jednotlivé kanály. ThunderHub nabízí pro tyto klíčové operace správy uzlů přehledný nástroj Interface.



### Vyvážení



Karta **Rebalance** je určena pro **vyvažování kanálů**. Vyrovnávání (nebo *vyrovnávání*) spočívá v úpravě rozdělení finančních prostředků mezi odchozí a příchozí kanály provedením **okružní platby** z jednoho kanálu do jiného kanálu prostřednictvím Lightning Network. To vám umožní, aniž byste museli přinášet nové prostředky, přesunout likviditu z příliš plného kanálu do příliš prázdného, čímž se vaše kanály stanou užitečnějšími (vyvážený kanál může odesílat i přijímat platby).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub tuto operaci, která by jinak byla v příkazovém řádku zdlouhavá, výrazně usnadňuje. Zde se dozvíte, jak sekci Rebalance používat:





- **Úvodní zobrazení kanálů:** Po vstupu do nástroje Rebalance zobrazí ThunderHub seznam vašich kanálů s ukazatelem vyvážení pro každý z nich (podobně jako na stránce Kanály). Ihned vidíte, které kanály jsou nevyvážené. ThunderHub umí seřadit kanály podle rostoucí vyváženosti tak, že nejvíce nevyvážené kanály vystupují na začátku seznamu (0,0 znamená zcela místní nebo vzdálené).





- **Výběr partnerů:** Interface umožňuje snadný výběr odchozích a příchozích partnerů pro rebalancování.





- **Nastavení parametrů:** Můžete nastavit :
  - **maximální poplatek** (v Sats a ppm), který jste ochotni zaplatit
  - **částka k rebalancování** s možností "Fixní" nebo "Cílová"
- Uzly, kterým je třeba se při směrování vyhnout
- **Maximální zkušební doba** pro vyhledání trasy





- Vyberte kanál **zdroje**: Nejprve vyberte **odchozí (zdrojový)** kanál, tj. kanál, z něhož máte příliš mnoho lokální likvidity k přesunu. V praxi se jedná o kanál, kde je váš lokální podíl vysoký (> 50 %). Představme si kanál A s 1 000 000 sáty, z nichž 900 000 je lokálních - dobrý kandidát na odeslání sátů jinam. Kliknutím na tento kanál A jako "odchozí" jej ThunderHub označí jako zdroj.





- Vyberte **cílový kanál**: Dále vyberte **příchozí (cílový)** kanál, který má přijímat likviditu. Obvykle to bude kanál, kde je to naopak - většina prostředků je na vzdálenější straně (např. pouze 100 000 místních Satsů z 1 000 000). ThunderHub po výběru zdrojového kanálu seřadí ostatní kanály v opačném pořadí (klesající zůstatek), aby pomohl identifikovat nejvíce doplňující kanály. Vyberte kanál B, který má místo na místní straně. Poté zařízení ThunderHub jasně zobrazí, které dva kanály byly vybrány (zdrojový A a cílový B).





- **Nastavení výše poplatku a tolerance:** Formulář umožňuje zadat :





- **Částka**, která má být vyrovnána (v Sats). Často volíme částku, která odpovídá vyvážení obou kanálů v poměru \~50/50. ThunderHub může předvyplnit například polovinu přebytečné kapacity zdrojového kanálu.
  - **Maximální poplatek**, který jste ochotni za tuto operaci zaplatit (nepovinné). Tento poplatek je vyjádřen v Sats (celkové náklady na kruhové směrování). Pokud jej necháte prázdný, bude ThunderHub hledat cestu bez ohledu na náklady, což obecně není vhodné (je lepší nastavit limit, např. 10 Sats pro malou rebalanci nebo maximální ppm).





- **Vyhledat trasu:** Kliknutím na tlačítko vyhledáte trasu. ThunderHub se dotáže LND a vypočítá trasu ze zdrojového kanálu přes síť do vlastního cílového kanálu. Pokud najde možnou trasu, která splňuje vaše kritéria poplatků, zobrazí ji s podrobnostmi o skocích a cenou poplatků. Může například uvést, že nalezl cestu o 3 skocích s celkovými poplatky 2 Sats.





- **Zahájení rebalance:** Pokud jste s navrženou trasou spokojeni, klikněte na **Balance Channel**. ThunderHub poté zahájí kruhovou platbu prostřednictvím LND. Pokud bude platba úspěšná, zobrazí se oznámení o úspěchu a u kanálů A a B se v reálném čase změní zůstatky. ThunderHub u těchto kanálů aktualizuje ukazatel zůstatku (v ideálním případě bude zelenější než dříve, což znamená lepší zůstatek).





- **Úpravy a iterace:** Pokud není nalezena žádná trasa na první pokus (nebo je příliš drahá), můžete upravit parametry:





  - Zkuste menší částku (někdy se částečné vyvážení podaří, zatímco velké množství se nepodaří).
  - Maximální výši poplatku zvyšujte postupně, ale dávejte pozor, abyste na poplatcích nezaplatili více, než se vyplatí.
  - Chcete-li vyzkoušet alternativní trasu, použijte tlačítko **Získat jinou trasu**, je-li k dispozici.
  - Pokud se situace opravdu zhorší, zkuste jiný pár kanálů.



ThunderHub umožňuje velmi **intuitivní a vizuální** proces. V pouhých 4 krocích (výběr odchozího kanálu, výběr příchozího kanálu, částka, ověření) můžete provést to, co dříve vyžadovalo složité ruční příkazy. Tento nástroj je neocenitelný pro udržování vyváženého uzlu, zlepšuje výkonnost směrování a uživatelský komfort (snadnější odesílání a přijímání plateb napříč všemi kanály).



Nakonec si uvědomte, že rebalance spotřebovává náklady na směrování (placené zprostředkujícím uzlům), takže se jedná o **investici** do zvýšení plynulosti vašeho uzlu. Používejte ji s rozmyslem, například k podpoře kanálu ke službě, kterou často používáte (příchozí likvidita), nebo k vyvážení velkého směrovacího kanálu. ThunderHub vám to umožní **jednoduše a efektivně**.



### Transakce



Sekce **Transakce** v systému ThunderHub odpovídá historii transakcí vašeho uzlu **Lightning**, tj. platbám a fakturám zaplaceným nebo přijatým prostřednictvím kanálů. Je to jakýsi výpis z účtu pro vaše operace LN.



![Historique des transactions Lightning](assets/fr/14.webp)



Na této kartě najdete :





- **Graf Invoice:** V pravém horním rohu se zobrazuje graf vývoje přijatých faktur v čase, který vám umožní vizualizovat aktivitu vašeho uzlu.





- Chronologický seznam všech transakcí Lightning provedených *z* nebo *do* vašeho uzlu. Každá položka může zobrazovat :





  - Typ operace: **odeslaná platba** (odchozí platba) nebo **přijatá platba** (příchozí, prostřednictvím placeného Invoice).
  - Částka v Sats.
  - Datum/čas.
  - ID platby (předobraz Hash nebo RHash) nebo komentář (pokud jste přidali poznámku do Invoice).
- Stav: **(např. platba čekající na vyřešení, ale LND ji zpravidla zpracovává rychle, takže ve srovnání s transakcemi On-Chain je zde málo "čekajících").**



Sekce Transakce zkrátka slouží jako **deník aktivit LN**. Je velmi užitečná pro kontrolu, zda platba proběhla, kolik poplatků stála, nebo pro sledování historie vašich bleskových výměn. Ve spojení se sekcí Převody (popsanou dále) získáte kompletní přehled o penězích, které prošly vaším uzlem.



### Útočníci



Karta **Předávání** je určena pro **směrování** vašeho uzlu, tj. pro platby, které **přecházejí** přes vaše kanály (když fungujete jako zprostředkující uzel na Lightning Network). Pokud svůj uzel provozujete jako směrovací uzel, je tato část důležitá pro sledování vaší výkonnosti.



![Statistiques de routage Lightning](assets/fr/15.webp)



ThunderHub představuje v sekci Forwards :





- **Filtry a možnosti zobrazení:** Filtry vpravo nahoře umožňují seřadit data podle dne/týdne/měsíce/roku a zvolit grafické nebo tabulkové zobrazení.





- **Zpráva o činnosti:** Pokud během vybraného období nebylo provedeno žádné směrování, zobrazí se na displeji Interface zpráva "No forwards for this period" (Žádné směrování za toto období), jak je znázorněno v tomto příkladu.





- **tabulka posledních přeposlání**: každá položka odpovídá platbě, která byla **přeposlána** prostřednictvím vašeho uzlu. U každého přeposlání zpravidla vidíme :





  - Timestamp,
  - směrované množství (v Sats),
- **poplatek** získaný za toto přeposlání (v systému Sats je to rozdíl mezi částkou, kterou jste obdrželi na příchozím kanálu, a částkou, kterou jste odeslali na odchozím kanálu),
  - použité příchozí a odchozí kanály (často identifikované aliasem partnera nebo ID kanálu).
  - stav (obvykle *dokončeno* nebo selhání, pokud se předání nezdařilo po cestě).





- **Souhrnné statistiky**: ThunderHub vypočítává a zobrazuje v horní části stránky celkové součty a statistiky za dané období (např. za posledních 24 hodin nebo 7 dní atd., někdy lze konfigurovat).



Sekce Forwards zkrátka nabízí **přehled o směrování uzlu Lightning v reálném čase**. Ve spojení s částmi Kanály a Rebalance tvoří kompletní balíček pro optimalizaci uzlu: Kanály/Rebalance pro likviditu, Forwardy pro sledování výsledků (toků a zisků).



### Řetěz



Sekce **Chain** odpovídá správě portfolia Bitcoin On-Chain vašeho uzlu LND. Tato část Interface umožňuje prohlížet a spravovat prostředky Bitcoin, které se používají k otevření kanálů nebo přijímání prostředků z uzavřených kanálů.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



V řetězci najdete :





- Zůstatek On-Chain: **Zobrazuje celkový zůstatek BTC dostupný v Wallet LND.**





- **Seznam UTXO:** Zobrazení všech nevyčerpaných výstupů (UTXO) s částkou, potvrzeními, Address a formátem pro každý výstup.





- **Historie transakcí:** Podrobná tabulka všech transakcí Bitcoin s typem (v/výstup), datem, částkou, poplatky, potvrzeními, blokem zařazení, adresami a txid.



### Amboss



ThunderHub je integrován s platformou **Amboss** (amboss.space), která nabízí podrobné informace o uzlech Lightning, tržiště likvidity a užitečné funkce, jako je šifrované zálohování kanálů a monitorování dostupnosti.



![Intégration Amboss avec ses options](assets/fr/17.webp)



Sekce Amboss v nástroji ThunderHub umožňuje **připojit** váš uzel k účtu Amboss:





- **Ghost Address:** Nastavte si **personalizovaný blesk Address** pro svůj uzel, který usnadňuje příchozí platby.





- Automatické zálohování kanálů:** Stěžejní funkce pro šifrované zálohování kanálů** (soubory SCB) v systému Amboss. Aktivujte v nastavení **Amboss Auto Backup = Yes**, aby se při každé změně kanálu automaticky odesílaly aktualizace šifrovaných záloh. V případě selhání budete moci díky této externí záloze obnovit své prostředky.





- **Kontroly stavu:** Aktivujte **Amboss Healthcheck = Yes**, aby váš uzel pravidelně odesílal pingy do systému Amboss. Pokud se bude zdát, že je váš uzel offline, obdržíte upozornění.





- Další funkce: Automatické odesílání zůstatku, integrace **Magma/Hydro** (tržiště likvidity) a přístup k podrobným statistikám výkonnosti.



Integrace se službou Amboss přidává zásadní **zabezpečení Layer** s automatickým externím zálohováním a monitorováním dostupnosti, které je přístupné přímo z ThunderHubu.



### Nástroje



V části **Nástroje** jsou seskupeny různé pokročilé nástroje pro správu uzlu. Zde jsou hlavní Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Zálohování:** Zálohování kanálu (SCB) můžete spravovat ručně. ThunderHub umožňuje **stahovat kompletní záložní soubor** vašich kanálů (možnost "Zálohovat všechny kanály -> Stáhnout"). Tento soubor `channel-all.bak` si uložte na bezpečné místo - je nezbytný pro obnovu vašich prostředků v případě havárie. Záložní soubor můžete také **importovat** při opětovném nasazení uzlu.





- **Účetnictví:** Exportní nástroj pro finanční výkazy včetně získaných/zaplacených poplatků a objemů směrovaných za dané období.
- **Podepsané zprávy:** **Podepište nebo ověřte zprávy** pomocí svého uzlu, abyste prokázali Ownership svého uzlu Lightning pomocí kryptografického podpisu.
- Makronky (sekce Pekařství):** Spravujte makronky LND** a vytvořte si vlastní přístup. Oddíl Interface "Pekárna" umožňuje přesně vybrat jednotlivá oprávnění: "Přidat nebo odebrat partnery", "Vytvořit řetězové adresy", "Vytvořit faktury", "Vytvořit makaróny", "Odvodit klíče", "Získat přístupové klíče", "Získat řetězové transakce", "Získat faktury", "Získat informace o Wallet", "Získat platby", "Získat partnery", "Zaplatit faktury", "Odvolat přístupové kódy", "Odeslat na řetězové adresy", "Podepsat bajty", "Podepsat zprávy", "Zastavit daemon", "Ověřit podpis bajtů", "Ověřit zprávy" atd. Každé oprávnění lze aktivovat jednotlivě pomocí tlačítek "Ano/Ne" a vytvořit tak makarón na míru.
- **Systémové informace:** Zobrazení verze Wallet a aktivovaných RPC.



Sekce Nástroje zkrátka sdružuje pokročilé funkce správy - zálohování, účetnictví, zabezpečení a správu přístupu - v jednotném nástroji Interface.



### Výměna



Karta **Výměna** na ThunderHubu umožňuje vyměnit satelity Lightning za Bitcoin On-Chain prostřednictvím služby Boltz. Tato funkce je užitečná pro "vyhození" přebytečné likvidity Lightning do kanálu bez nutnosti uzavření kanálu.



![Interface de swap via Boltz](assets/fr/19.webp)



Postup je jednoduchý:





- **Částka**: Definujte částku, která má být vyměněna
- **Address**: Zadejte příjem Bitcoin Address
- **Provedení**: ThunderHub komunikuje s Boltzem a automaticky zpracovává Exchange



**Výhody:**




- Služba bez opatrovnictví (bez úschovy peněz)
- Zachování stávajících kanálů
- Snadno použitelný integrovaný Interface



Společnost Boltz si účtuje malou provizi a vy platíte standardní transakční poplatek Bitcoin. ThunderHub zobrazí všechny náklady před potvrzením.



### Statistiky



Sekce **Stats** služby ThunderHub nabízí **rozšířené statistiky** uzlu Lightning pro analýzu výkonu a optimalizaci směrování.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Tato část je nezbytná pro optimalizaci nákladů, identifikaci úspěšných kanálů a plánování rozšíření vašeho uzlu.



## Závěr



**ThunderHub** se etabloval jako základní nástroj pro snadnou správu uzlu Lightning **LND**. Tento moderní Interface nabízí všechny základní funkce: správu kanálů, platby, monitorování a pokročilé funkce, jako je automatické vyrovnávání a integrace se systémem Amboss.



**Klíčové výhody:**




- Interface elegantní a intuitivní
- Výkonné nástroje (rebalance, Boltzovy výměny, automatické zálohování)
- Kompatibilní s distribucemi Umbrel, Voltage, RaspiBlitz a dalšími



ThunderHub demokratizuje pokročilou správu uzlů Lightning a zpřístupňuje to, co dříve vyžadovalo složité technické příkazy. Ať už jste začátečník, nebo zkušený operátor, ThunderHub vám umožní efektivně spravovat uzel Lightning prostřednictvím moderního, komplexního nástroje Interface.



## Zdroje



**Oficiální odkazy:**




- **Oficiální webové stránky:** [thunderhub.io](https://thunderhub.io)
- **Dokumentace:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **Zdrojový kód GitHub:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)