---
name: Server LNbits
description: Instalace a konfigurace samostatně hostovaného serveru LNbits na Ubuntu VPS s PHOENIXD nebo na Umbrel
---

![cover](assets/cover.webp)



LNbits je open source webová aplikace Interface, která přemění jakýkoli backend Lightningu (LND, Core Lightning, PHOENIXD) na kompletní platformu služeb. Toto samostatně hostované řešení umožňuje izolovaně spravovat více portfolií Lightning, nasazovat prodejní místa, vytvářet dárcovské systémy nebo fakturační služby a přitom si zachovat plnou kontrolu nad svými prostředky.



Tento výukový program se zabývá dvěma způsoby instalace: **VPS Ubuntu s PHOENIXD** (lehké řešení bez plného uzlu Bitcoin) a **Umbrel** (integrace se stávajícím uzlem LND). Na rozdíl od obecného návodu LNbits od Plan B Network, který se zabývá koncepty a rozšířeními, se tento návod zaměřuje na technické postupy instalace krok za krokem.



## Co je LNbits?



LNbits je účetní systém Lightning vyvinutý v jazyce Python (FastAPI), který se připojuje ke stávajícímu backendu (LND, Core Lightning, PHOENIXD). Na rozdíl od tradičních uzlů Lightning nabízí LNbits přístupný Interface, který umožňuje spravovat několik izolovaných portfolií s vlastními klíči API. Můžete vytvořit podúčty pro svou rodinu, zaměstnance nebo projekty, aniž byste jim poskytli přístup ke všem svým prostředkům.



Oddělená architektura ukládá informace do SQLite (výchozí) nebo PostgreSQL (produkční), zatímco finanční prostředky zůstávají spravovány backendem Lightning. Toto oddělení zaručuje přenositelnost: můžete přejít z PHOENIXD na LND, aniž byste přišli o uživatelská data.



## Klíčové vlastnosti



LNbits nabízí univerzální **rozšiřující systém**: (prodejní místo), Paywall (monetizace obsahu), Events (prodej vstupenek), LndHub (server pro BlueWallet), Bolt Cards (NFC platby), Split Payments (automatická distribuce) a User Manager (správa uživatelů s autentizací).



Na **dashboardu** se zobrazují zůstatky v reálném čase, historie transakcí a nástroje pro vyúčtování. Každý Wallet má jedinečnou adresu URL obsahující jeho klíče API, což umožňuje přístup bez tradičního přihlášení. Tříúrovňový systém klíčů API** (admin, Invoice, pouze pro čtení) nabízí granulární kontrolu oprávnění pro bezpečné integrace.



LNbits nativně implementuje **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) a podporuje **Lightning Address**, což zaručuje kompatibilitu s moderními peněženkami Lightning a usnadňuje nasazení profesionálních služeb.



## Podporované platformy



**Ubuntu VPS**: Lehké řešení bez plného uzlu Bitcoin. Předpoklady: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + doménové jméno vyžadováno pro veřejné vystavení (služby LNURL).



**Umbrel**: Snadná instalace z App Store. Předpoklad: funkční uzel Umbrel se synchronizovaným LND a otevřenými kanály. Automatická konfigurace.



Níže jsou uvedeny odkazy na naše výukové programy Umbrel a Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalace na Ubuntu VPS s PHOENIXD



### Krok 1: Zabezpečení serveru VPS



**Před jakoukoli instalací** je třeba zabezpečit server VPS Ubuntu podle pravidel techniky. Tento krok je **kriticky důležitý** pro ochranu vaší infrastruktury a vašich prostředků Lightning.



Zde je podrobný průvodce, který vám pomůže začít: *costas: *[Počáteční konfigurace serveru Ubuntu - průvodce krok za krokem](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** Autor: Daniel P. Costas.



Tato příručka se zabývá konfigurací uživatelů, zabezpečeným SSH, bránou firewall (UFW), fail2ban, automatickými aktualizacemi a správnými postupy zabezpečení systému.



### Krok 2: Instalace PHOENIXD



Jakmile je server zabezpečen, je třeba nainstalovat a nakonfigurovat PHOENIXD. Společnost Plan B Network nabízí kompletní specializovaný výukový program zahrnující instalaci, generování seed a konfiguraci služby systemd:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Jakmile je PHOENIXD spuštěn (zkontrolujte to pomocí `./Phoenix-CLI getinfo`), všimněte si **HTTP hesla** v `~/.Phoenix/Phoenix.conf` - budete ho potřebovat pro připojení LNbits ke PHOENIXD.



### Nasazení LNbitů



Nainstalujte UV a klonujte LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfigurace backendu PHOENIXD:


```bash
cp .env.example .env && nano .env
```



Přidat do souboru `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Otestujte pomocí `uv run lnbits --host 0.0.0.0 --port 5000` a poté vytvořte službu systemd s `Wants=PHOENIXD.service`.



## Počáteční nastavení a první použití



### Aktivace SuperUživatele



Aktivujte správce Interface v souboru `.env` :


```
LNBITS_ADMIN_UI=true
```



Restartujte LNbits (`sudo systemctl restart lnbits`) a načtěte ID SuperUser:


```bash
cat ~/lnbits/data/.super_user
```



Přejděte na `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` pro panel správy. V nabídce "Server" můžete konfigurovat zdroje financování, rozšíření a uživatelské účty.



### Bezpečné vytvoření účtu



**Důležité pro veřejné vystavení**: Pokud vystavujete instanci LNbits na veřejném doménovém jméně přístupném z internetu, je **kriticky důležité** zakázat volné vytváření uživatelských účtů.



Ve správě SuperUser Interface přejděte do části "Nastavení" a poté do části "Správa uživatelů". Najdete zde možnost "Povolit vytváření nových uživatelů".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Pro veřejnou výstavu s názvem domény** :




- Je třeba zakázat** možnost "Povolit vytváření nových uživatelů"
- Bez této ochrany si může kdokoli na internetu vytvořit účet ve vaší instanci
- Útočník může bez vašeho vědomí vytvořit účty a používat likviditu vašeho LIGHTNING NODE
- Uživatelské účty je třeba vytvořit ručně v nástroji Interface SuperUser



**Pouze pro místní použití** :




- Tato možnost není tak důležitá, pokud je instance přístupná pouze lokálně (http://localhost:5000)
- Vypnutí této možnosti je však dobrým bezpečnostním postupem



Po konfiguraci může nové uživatelské účty vytvářet pouze správce SuperUser prostřednictvím Interface "Users". Tento přístup zaručuje úplnou kontrolu nad tím, kdo může přistupovat k infrastruktuře Lightning a používat vaše prostředky.



### Otevření prvního kanálu



PHOENIXD automaticky spravuje kanály prostřednictvím automatické likvidity. generate bleskový Invoice ve výši ~30 000 Sats z LNbits a zaplatit jej z jiného Wallet. PHOENIXD automaticky otevře kanál ACINQ. Odečte se poplatek za otevření (~20-23 tisíc Sats), zbývající částka (~7-10 tisíc Sats) se objeví po potvrzení On-Chain.



Zkontrolujte stav pomocí `./Phoenix-CLI getinfo`. Pak zvažte vypnutí automatické likvidity (`auto-liquidity=off` v `Phoenix.conf`), abyste mohli kontrolovat otevírání kanálů.



### Veřejné zobrazení a HTTPS



**Důležité**: (zabezpečení klíčem API + kompatibilita s LNURL). Tento krok přeskočte pouze pro místní použití.



**Caddy (doporučeno)**: automatické SSL. `sudo apt install -y caddy`, upravte `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Restartování: `sudo systemctl restart caddy`.



**Nginx** : Více kontroly. Nainstalujte `nginx certbot python3-certbot-nginx`, vytvořte `/etc/nginx/sites-available/lnbits` :


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Aktivace: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Přidat do souboru `.env`: `FORWARDED_ALLOW_IPS=*``



## Instalace deštníku



### Nasazení z obchodu App Store



Přejděte do obchodu s aplikacemi Umbrel, vyhledejte položku "LNbits" a klikněte na tlačítko "Instalovat".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel automaticky kontroluje požadované závislosti. LNbits vyžaduje ke svému běhu LIGHTNING NODE (LND). Pokud je váš LIGHTNING NODE již v provozu, potvrďte kliknutím na "Instalovat LNbits".



![Dépendances LNbits](assets/fr/02.webp)



Umbrel stáhne obraz Dockeru, automaticky nakonfiguruje připojení s LND a spustí kontejner (2-5 minut). Instalace probíhá zcela na pozadí.



### Počáteční konfigurace Superuživatele



Při prvním spuštění vás LNbits vyzve k vytvoření účtu správce SuperUser. Zadejte uživatelské jméno a nastavte bezpečné heslo pro ochranu přístupu do systému správy Interface.



![Configuration SuperUser](assets/fr/03.webp)



**Důležité**: Tento účet SuperUser má ve vaší instanci LNbits plná práva. Zvolte si silné heslo a udržujte ho v bezpečí.



Po vytvoření účtu budete automaticky přesměrováni do hlavní oblasti správy Interface. Společnost Umbrel již nastavila LND jako váš zdroj financování - všechny bleskové platby budou probíhat přes vaše stávající kanály.



### Přístup ke správci Interface



V levém bočním menu klikněte na položku "Settings" (Nastavení), čímž získáte přístup k celému panelu správy.



![Interface Settings](assets/fr/04.webp)



V části "Správa peněženek" se zobrazují klíčové informace o konfiguraci:




- Zdroj financování** : LndBtcRestWallet (přímé připojení k uzlu LND Umbrel)
- Bilance uzlů** : Celková likvidita dostupná ve vašich kanálech Lightning
- LNbits Balance**: Finanční prostředky přidělené systému LNbits (původně 0 Sats)



Nyní můžete přímo využívat likviditu svého uzlu Umbrel pro všechny peněženky LNbits, které vytvoříte. Není potřeba žádná další konfigurace - LNbits je spuštěn a funguje.



### Správa uživatelů



Jednou z nejvýkonnějších funkcí LNbits je možnost vytvořit více nezávislých uživatelů, z nichž každý má své heslo a izolovanou peněženku. Tato architektura umožňuje využívat likviditu uzlu Umbrel a zároveň nabízí zcela izolované podúčty pro různé účely: podnikání, rodinu, zaměstnance, projekty atd.



V postranní nabídce klikněte na položku "Uživatelé" a získáte přístup ke správě uživatelů. Kliknutím na "CREATE ACCOUNT" (Vytvořit účet) přidáte nového uživatele.



![Gestion des utilisateurs](assets/fr/05.webp)



Vyplňte formulář pro vytvoření uživatele:




- Uživatelské jméno**: Přihlašovací jméno (příklad: "Satoshi")
- Nastavení hesla**: Aktivací této možnosti nastavíte ověřovací heslo
- Heslo** a **Heslo opakovat**: Nastavte heslo pro tohoto uživatele



![Création utilisateur satoshi](assets/fr/06.webp)



Nepovinná pole (veřejný klíč Nostr, e-mail, jméno, příjmení) lze pro minimální konfiguraci ponechat prázdná. Kliknutím na tlačítko "CREATE ACCOUNT" (Vytvořit účet) potvrďte zadání.



![Confirmation utilisateur créé](assets/fr/07.webp)



Váš nový uživatel se nyní zobrazí v seznamu uživatelů se svým jedinečným identifikátorem a uživatelským jménem.



![Liste des utilisateurs](assets/fr/08.webp)



**Důležitý bod**: Každý uživatel se může přihlásit zcela samostatně pomocí vlastního hesla. Správce SuperUser si zachovává plnou kontrolu prostřednictvím nástroje pro správu Interface.



### Správa uživatelů Wallet



Po vytvoření uživatele "Satoshi" je třeba mu přiřadit blesk Wallet. Klikněte na ikonu Wallet (druhá ikona) příslušného uživatele a poté na "CREATE NEW Wallet".



![Gestion des wallets](assets/fr/09.webp)



V dialogovém okně se zobrazí výzva k pojmenování zařízení Wallet. Zadejte popisný název (např. "Wallet Of Satoshi") a vyberte měnu zobrazení (CUC, USD, EUR atd.).



![Création wallet](assets/fr/10.webp)



Klikněte na "CREATE". LNbits pro tohoto uživatele okamžitě vygeneruje funkční Wallet Lightning.



![Confirmation wallet créé](assets/fr/11.webp)



Nyní vidíte dvě existující peněženky: výchozí Wallet "LNbits Wallet" vytvořenou automaticky a novou "Wallet Of Satoshi". Pro zjednodušení uživatelského prostředí můžete výchozí peněženku Wallet odstranit kliknutím na ikonu odstranění (červený koš).



![Wallet final unique](assets/fr/12.webp)



Uživatel "Satoshi" má nyní k dispozici jediný, jasně identifikovaný Wallet. Každý uživatel Wallet pracuje zcela autonomně, přičemž využívá likviditu vašeho základního uzlu LND.



**Klíčový koncept**: Všechny tyto peněženky sdílejí globální likviditu vašeho uzlu Umbrel. Nevytváříte nové kanály Lightning pro každý Wallet - LNbits funguje jako inteligentní účetní Layer, který řídí přidělování prostředků v rámci vaší stávající infrastruktury Lightning. V tom spočívá síla systému LNbits s více Wallet.



### Přihlášení uživatele



Odhlaste se z účtu SuperUser (ikona vpravo nahoře) a vraťte se na přihlašovací stránku LNbits. Nyní se můžete přihlásit pomocí přihlašovacích údajů nového uživatele.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Zadejte dříve definované uživatelské jméno ("Satoshi") a heslo a klikněte na tlačítko "PŘIHLÁSIT SE". Uživatel získá přímý přístup ke svému osobnímu Wallet, zcela izolovanému od administračního Interface.



### Interface od uživatele Wallet



Po připojení uživatel přistupuje ke svému zařízení Interface ze zařízení Wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Model Interface je vybaven :




- Aktuální zůstatek**: Zobrazuje se v Sats a ve zvolené měně (v tomto příkladu CUC)
- Hlavní činnosti**: "PASTE REQUEST" (vložit účet k zaplacení), "CREATE Invoice" (generate účtenka), ikona QR (rychlé skenování)
- Historie transakcí** : Kompletní seznam všech plateb a příjmů
- Pravý boční panel**: Možnosti konfigurace a přístupu



### Mobilní přístup Wallet



Pravý boční panel nabízí mimořádně praktickou funkci: mobilní přístup k Wallet. Rozbalte část "Mobilní přístup" a zjistěte, jaké možnosti jsou k dispozici.



![Mobile Access](assets/fr/15.webp)



LNbits nabízí několik způsobů, jak tento Wallet používat v chytrém telefonu:



**Možnost 1: Kompatibilní mobilní aplikace




- Stáhněte si **Zeus** nebo **BlueWallet** z App Store nebo Google Play
- Aktivace rozšíření **LndHub** v systému LNbits pro tento modul Wallet
- Naskenujte QR kód LndHub pomocí mobilní aplikace a připojte Wallet



**Možnost 2: Přímý přístup přes mobilní prohlížeč**




- Kód QR zobrazený v části "Export do telefonu pomocí kódu QR" obsahuje úplnou adresu URL zařízení Wallet s integrovaným ověřováním
- Naskenováním tohoto QR kódu z chytrého telefonu otevřete Wallet přímo v mobilním prohlížeči
- Přidání stránky na domovskou obrazovku pro rychlý přístup



**Důležité zabezpečení**: Tato adresa URL obsahuje klíče API pro plný přístup ke Wallet. Nikdy jej nesdílejte veřejně. S tímto QR kódem zacházejte stejně jako s privátními klíči Bitcoin - kdokoli naskenuje tento QR kód, získá plný přístup ke Wallet.



Tato mobilní funkce promění vaši instanci LNbits Umbrel ve skutečný server Lightning Wallet pro vás a vaše přátele, přičemž si díky vlastnímu uzlu zachováte naprostou suverenitu nad svými prostředky.



### Sdílení přístupu uživatelů



Hlavním případem použití této konfigurace pro více uživatelů je **společné sdílení peněženek s rodinou nebo blízkými osobami**. Jakmile vytvoříte uživatele s vyhrazeným jménem Wallet (například "Satoshi" v našem příkladu), můžete tyto přihlašovací údaje sdílet s důvěryhodnými členy své domácnosti.



**Zabezpečení přístupu do služby Umbrel**: Přístup k vaší instanci LNbits na Umbrelu je přirozeně chráněn, protože k ní lze přistupovat pouze :




- V místní síti** : Členové vaší domácnosti připojeni ke stejné síti WiFi/Ethernet mohou přistupovat k instanci
- Přes VPN**: Pokud na serveru Umbrel používáte nakonfigurovanou síť VPN, jako je Tailscale, mohou oprávnění uživatelé získat bezpečný vzdálený přístup



Díky této dvojí ochraně (přístup k síti + ověřování uživatelů) je možnost "Povolit vytváření nových uživatelů" v systému Umbrel méně kritická. K přihlášení Interface se dostanou pouze osoby, které již mají přístup k vaší síti nebo VPN.



**Typický scénář**: Vytvoříte účet "otec", účet "matka", účet "firma" atd. Každý člen rodiny má svůj vlastní izolovaný Wallet Lightning, přičemž využívá sdílené likvidity vašeho uzlu Umbrel. Stačí sdílet uživatelské jméno a heslo - uživatel se pak může připojit z libovolného zařízení ve vaší místní síti nebo prostřednictvím sítě VPN Tailscale. Další informace naleznete v našem specializovaném výukovém programu Tailscale:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Prozkoumejte dostupná rozšíření



Vraťte se do Superuživatele Interface a přejděte do nabídky "Rozšíření" v levém bočním panelu, kde najdete kompletní ekosystém rozšíření LNbits.



![Extensions disponibles](assets/fr/16.webp)



LNbits nabízí bohatý katalog rozšíření, která promění vaši instanci ve skutečnou platformu služeb Lightning:





- Jukebox**: Systém jukeboxu s napájením Sats (platby Spotify)
- Lístky podpory**: Placený systém podpory (přijímání odpovědí na dotazy)
- TPoS**: Bezpečný mobilní terminál pro prodejce
- Správce uživatelů**: pokročilá správa uživatelů a Wallet (kterou jsme právě použili)
- Události**: Prodej a ověřování platnosti vstupenek na akce
- LNURLZařízení**: Správa prodejních míst, bankomaty, připojené přepínače
- SMTP**: Umožněte uživatelům odesílat e-maily a získávat Satss
- Boltcards**: Programování NFC karet pro platby Lightning tap-to-pay
- NostrNip5**: Vytvářejte adresy NIP5 pro své domény
- Rozdělené platby**: Automatické rozdělení plateb mezi více peněženek



Každé rozšíření se aktivuje jediným kliknutím z tohoto přístroje Interface. Rozšíření označená "FREE" jsou zdarma, zatímco některá jsou k dispozici jako "PAID" verze. Prozkoumejte katalog a najděte ta, která odpovídají vašim potřebám - ať už jde o podnikání, správu rodiny nebo experimentování s možnostmi Lightning Network.



## Výhody a omezení



**Výhody**: (plná kontrola nad prostředky/klíči/daty), flexibilita architektury (bezztrátová migrace VPS→Full node), profesionální systém rozšíření, intuitivní Interface.



**Omezení** : Software v beta verzi (opatrně s ohledem na množství), zabezpečení v odpovědnosti správce, URL obsahující citlivé klíče API (povinné HTTPS), správa více uživatelů znamená odpovědnost správce.



## Osvědčené postupy



**Zálohy**: seed PHOENIXD/přístupové údaje LND, databáze LNbits, soubory `.env`. Automatizovat denně, uchovávat mimo produkční server, šifrované. Pravidelně testujte obnovení.



**Údržba**: Pravidelně kontrolujte aktualizace (LNbits, Lightning backend, operační systém). Před významnými aktualizacemi vždy zkontrolujte poznámky k vydání.





- Na deštníku**: App Store vás automaticky upozorní na nové verze. Synchronizujte rozšíření prostřednictvím "Správa rozšíření" > "Aktualizovat vše". Zkontrolujte zahrnutí databáze SQLite do automatických záloh Umbrel.
- Na VPS**: Lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Sledujte systémové protokoly: `sudo journalctl -u lnbits -f`.



## Závěr



Samostatné hostování LNbits nabízí konkrétní cestu k finanční suverenitě Blesku. VPS+PHOENIXD nabízí odlehčené řešení pro rychlé služby, Umbrel plnou integraci se stávajícím uzlem Bitcoin. Škálovatelná architektura umožňuje vývoj od jednoduchého Wallet pro více uživatelů až po sofistikované obchodní případy použití.



Samostatné hostování znamená odpovědnost: zálohujte semena, chraňte přístup, začněte se skromnými částkami. Díky těmto opatřením se LNbits stává robustním řešením pro bleskovou ekonomiku a zároveň zachovává decentralizaci a autonomii.



## Zdroje



### Oficiální dokumentace




- [Dokumentace LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Oficiální průvodce instalací](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Průvodci Společenství




- [Počáteční konfigurace serveru Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) by Daniel P. Costas (zabezpečení VPS krok za krokem)
- [LNbits + PHOENIXD instalace na Ubuntu VPS](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) Daniel P. Costas (kompletní průvodce)
- [LNbits Server na Clearnetu](https://ereignishorizont.xyz/lnbits-server/en/) od Axel
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes