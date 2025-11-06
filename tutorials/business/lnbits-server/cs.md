---
name: Server LNbits
description: Instalace a konfigurace samostatně hostovaného serveru LNbits na Ubuntu VPS s Phoenixd nebo na Umbrel
---

![cover](assets/cover.webp)



LNbits je webové rozhraní s otevřeným zdrojovým kódem, které přemění jakýkoli backend Lightningu (LND, Core Lightning, Phoenixd) na kompletní platformu služeb. Toto samostatně hostované řešení umožňuje izolovaně spravovat více portfolií Lightning, nasazovat prodejní místa, vytvářet dárcovské systémy nebo fakturační služby a přitom si zachovat plnou kontrolu nad svými prostředky.



Tento výukový program se zabývá dvěma způsoby instalace: **VPS Ubuntu s Phoenixd** (lehké řešení bez plného uzlu Bitcoin) a **Umbrel** (integrace se stávajícím uzlem LND). Na rozdíl od obecného návodu Plan ₿ Academy LNbits, který se zabývá koncepty a rozšířeními, se tento návod zaměřuje na technické postupy instalace krok za krokem.



## Co je LNbits?



LNbits je účetní systém Lightning vyvinutý v jazyce Python (FastAPI), který se připojuje ke stávajícímu backendu (LND, Core Lightning, Phoenixd). Na rozdíl od tradičních uzlů Lightning nabízí LNbits přístupné rozhraní pro správu několika izolovaných portfolií s vlastními klíči API. Můžete vytvářet podúčty pro svou rodinu, zaměstnance nebo projekty, aniž byste jim poskytli přístup ke všem svým prostředkům.



Oddělená architektura ukládá informace do SQLite (výchozí) nebo PostgreSQL (produkční), zatímco finanční prostředky zůstávají spravovány backendem Lightning. Toto oddělení zaručuje přenositelnost: můžete přejít z Phoenixd na LND, aniž byste přišli o uživatelská data.



## Klíčové vlastnosti



LNbits nabízí univerzální **rozšiřující systém**: (prodejní místo), Paywall (monetizace obsahu), Events (prodej vstupenek), LndHub (server pro BlueWallet), Bolt Cards (NFC platby), Split Payments (automatická distribuce) a User Manager (správa uživatelů s autentizací).



Na **dashboardu** se zobrazují zůstatky v reálném čase, historie transakcí a nástroje pro vyúčtování. Každý wallet má jedinečnou adresu URL obsahující jeho klíče API, což umožňuje přístup bez tradičního přihlášení. Tříúrovňový systém klíčů API** (administrátor, faktura, pouze pro čtení) nabízí granulární kontrolu oprávnění pro bezpečné integrace.



LNbits nativně implementuje **LNURL** (LNURL-pay, LNURL-withdraw, LNURL-auth) a podporuje **Lightning Address**, což zaručuje kompatibilitu s moderními peněženkami Lightning a usnadňuje nasazení profesionálních služeb.



## Podporované platformy



**Ubuntu VPS**: Lehké řešení bez plného uzlu Bitcoin. Předpoklady: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + doménové jméno vyžadováno pro veřejné vystavení (služby LNURL).



**Umbrel**: Snadná instalace z App Store. Předpoklad: funkční uzel Umbrel se synchronizovaným LND a otevřenými kanály. Automatická konfigurace.



Níže jsou uvedeny odkazy na naše výukové programy Umbrel a Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalace na Ubuntu VPS s Phoenixd



### Krok 1: Zabezpečení serveru VPS



**Před jakoukoli instalací** je třeba zabezpečit server VPS Ubuntu podle pravidel techniky. Tento krok je **kriticky důležitý** pro ochranu vaší infrastruktury a vašich prostředků Lightning.



Zde je podrobný průvodce, který vám pomůže začít: *costas: *[Počáteční konfigurace serveru Ubuntu - průvodce krok za krokem](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** Autor: Daniel P. Costas.



Tato příručka se zabývá konfigurací uživatelů, zabezpečeným SSH, bránou firewall (UFW), fail2ban, automatickými aktualizacemi a správnými postupy zabezpečení systému.



### Krok 2: Instalace aplikace Phoenixd



Jakmile je server zabezpečen, je třeba nainstalovat a nakonfigurovat Phoenixd. Plan ₿ Academy nabízí komplexní specializovaný výukový program, který se zabývá instalací, generováním seed a konfigurací služby systemd :



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Jakmile je Phoenixd spuštěn (zkontrolujte pomocí `./phoenix-cli getinfo`), poznamenejte si **HTTP heslo** v `~/.phoenix/phoenix.conf` - budete ho potřebovat pro připojení LNbits k Phoenixd.



### Nasazení LNbitů



Nainstalujte UV a klonujte LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfigurace backendu Phoenixd:


```bash
cp .env.example .env && nano .env
```



Přidat do souboru `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Otestujte pomocí `uv run lnbits --host 0.0.0.0 --port 5000` a poté vytvořte službu systemd pomocí `Wants=phoenixd.service`.



## Počáteční nastavení a první použití



### Aktivace SuperUživatele



Aktivujte rozhraní správce v souboru `.env` :


```
LNBITS_ADMIN_UI=true
```



Restartujte LNbits (`sudo systemctl restart lnbits`) a načtěte ID SuperUser:


```bash
cat ~/lnbits/data/.super_user
```



Přejděte na `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>` pro panel správy. V nabídce "Server" můžete konfigurovat zdroje financování, rozšíření a uživatelské účty.



### Bezpečné vytvoření účtu



**Důležité pro veřejné vystavení**: Pokud vystavujete instanci LNbits na veřejném doménovém jméně přístupném z internetu, je **kriticky důležité** zakázat volné vytváření uživatelských účtů.



V rozhraní pro správu SuperUseru přejděte do části "Nastavení" a poté do části "Správa uživatelů". Tam najdete možnost "Povolit vytváření nových uživatelů".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Pro veřejnou výstavu s názvem domény** :




- Je třeba zakázat** možnost "Povolit vytváření nových uživatelů"
- Bez této ochrany si může kdokoli na internetu vytvořit účet ve vaší instanci
- Útočník by mohl vytvořit účty a používat likviditu vašeho uzlu Lightning bez vašeho vědomí
- Uživatelské účty je třeba vytvořit ručně v rozhraní SuperUser



**Pouze pro místní použití** :




- Tato možnost není tak důležitá, pokud je instance přístupná pouze lokálně (http://localhost:5000)
- Vypnutí této možnosti je však dobrým bezpečnostním postupem



Po konfiguraci může nové uživatelské účty vytvářet pouze správce SuperUser prostřednictvím rozhraní "Users". Tento přístup zaručuje úplnou kontrolu nad tím, kdo může přistupovat k infrastruktuře Lightning a používat vaše prostředky.



### Otevření prvního kanálu



Phoenixd automaticky spravuje kanály prostřednictvím automatické likvidity. Vygenerujte bleskovou fakturu ve výši ~30 000 sats z LNbits a zaplaťte ji z jiného wallet. Phoenixd automaticky otevře kanál pro ACINQ. Odečte se poplatek za otevření (~20-23 tisíc sats), zbývající částka (~7-10 tisíc sats) se objeví po potvrzení on-chain.



Zkontrolujte stav pomocí `./phoenix-cli getinfo`. Pak zvažte vypnutí automatické likvidity (`auto-liquidity=off` v `phoenix.conf`), abyste mohli kontrolovat otevírání kanálů.



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


Aktivace: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Přidat do souboru `.env`: `FORWARDED_ALLOW_IPS=*``



## Instalace deštníku



### Nasazení z obchodu App Store



Přejděte do obchodu s aplikacemi Umbrel, vyhledejte položku "LNbits" a klikněte na tlačítko "Instalovat".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel automaticky kontroluje požadované závislosti. LNbits vyžaduje ke své činnosti Lightning Node (LND). Pokud je váš uzel Lightning již funkční, klikněte na "Instalovat LNbits" a potvrďte.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel stáhne obraz Dockeru, automaticky nakonfiguruje připojení s LND a spustí kontejner (2-5 minut). Instalace probíhá zcela na pozadí.



### Počáteční konfigurace Superuživatele



Při prvním spuštění vás LNbits vyzve k vytvoření účtu správce SuperUser. Zadejte uživatelské jméno a bezpečné heslo pro ochranu přístupu k administračnímu rozhraní.



![Configuration SuperUser](assets/fr/03.webp)



**Důležité**: Tento účet SuperUser má ve vaší instanci LNbits plná práva. Zvolte si silné heslo a udržujte ho v bezpečí.



Po vytvoření účtu jste automaticky přesměrováni do hlavního administračního rozhraní. Společnost Umbrel již nastavila LND jako váš zdroj financování - všechny platby Blesku budou probíhat přes vaše stávající kanály.



### Přístup k rozhraní správce



V levém bočním menu klikněte na položku "Settings" (Nastavení), čímž získáte přístup k celému panelu správy.



![Interface Settings](assets/fr/04.webp)



V části "Správa peněženek" se zobrazují klíčové informace o konfiguraci:




- Zdroj financování** : LndBtcRestWallet (přímé připojení k uzlu LND Umbrel)
- Bilance uzlů** : Celková likvidita dostupná ve vašich kanálech Lightning
- LNbits Balance**: Prostředky přidělené systému LNbits (původně 0 sats)



Nyní můžete přímo využívat likviditu svého uzlu Umbrel pro všechny peněženky LNbits, které vytvoříte. Není potřeba žádná další konfigurace - LNbits je spuštěn a funguje.



### Správa uživatelů



Jednou z nejvýkonnějších funkcí LNbits je možnost vytvořit více nezávislých uživatelů, z nichž každý má své heslo a izolovanou peněženku. Tato architektura umožňuje využívat likviditu uzlu Umbrel a zároveň nabízí zcela izolované podúčty pro různé účely: podnikání, rodinu, zaměstnance, projekty atd.



V postranní nabídce klikněte na položku "Uživatelé" a získáte přístup ke správě uživatelů. Kliknutím na "CREATE ACCOUNT" (Vytvořit účet) přidáte nového uživatele.



![Gestion des utilisateurs](assets/fr/05.webp)



Vyplňte formulář pro vytvoření uživatele:




- Uživatelské jméno**: Přihlašovací jméno (příklad: "satoshi")
- Nastavení hesla**: Aktivací této možnosti nastavíte ověřovací heslo
- Heslo** a **Heslo opakovat**: Nastavte heslo pro tohoto uživatele



![Création utilisateur satoshi](assets/fr/06.webp)



Nepovinná pole (veřejný klíč Nostr, e-mail, jméno, příjmení) lze pro minimální konfiguraci ponechat prázdná. Kliknutím na tlačítko "CREATE ACCOUNT" (Vytvořit účet) potvrďte zadání.



![Confirmation utilisateur créé](assets/fr/07.webp)



Váš nový uživatel se nyní zobrazí v seznamu uživatelů se svým jedinečným identifikátorem a uživatelským jménem.



![Liste des utilisateurs](assets/fr/08.webp)



**Důležitý bod**: Každý uživatel se může přihlásit zcela samostatně pomocí vlastního hesla. Správce SuperUser si ponechává plnou kontrolu prostřednictvím administračního rozhraní.



### Správa uživatelů wallet



Po vytvoření uživatele "satoshi" je třeba mu přiřadit blesk wallet. Klikněte na ikonu wallet (druhá ikona) příslušného uživatele a poté na "CREATE NEW WALLET" (Vytvořit novou peněženku).



![Gestion des wallets](assets/fr/09.webp)



V dialogovém okně se zobrazí výzva k pojmenování jednotky wallet. Zadejte popisný název (např. "Wallet Of Satoshi") a vyberte měnu zobrazení (CUC, USD, EUR atd.).



![Création wallet](assets/fr/10.webp)



Klikněte na "CREATE". LNbits pro tohoto uživatele okamžitě vygeneruje funkční wallet Lightning.



![Confirmation wallet créé](assets/fr/11.webp)



Nyní vidíte dvě existující peněženky: výchozí wallet "LNbits wallet" vytvořenou automaticky a novou "Wallet Of Satoshi". Pro zjednodušení uživatelského prostředí můžete výchozí peněženku wallet odstranit kliknutím na ikonu odstranění (červený koš).



![Wallet final unique](assets/fr/12.webp)



Uživatel "satoshi" má nyní k dispozici jediný, jasně identifikovaný wallet. Každý uživatel wallet pracuje zcela autonomně a zároveň využívá likviditu vašeho základního uzlu LND.



**Klíčový koncept**: Všechny tyto peněženky sdílejí globální likviditu vašeho uzlu Umbrel. Pro každou wallet nevytváříte nové kanály Lightning - LNbits funguje jako inteligentní účetní vrstva, která řídí přidělování prostředků v rámci vaší stávající infrastruktury Lightning. V tom spočívá síla systému LNbits pro více wallet.



### Přihlášení uživatele



Odhlaste se z účtu SuperUser (ikona vpravo nahoře) a vraťte se na přihlašovací stránku LNbits. Nyní se můžete přihlásit pomocí přihlašovacích údajů nového uživatele.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Zadejte dříve definované uživatelské jméno ("satoshi") a heslo a klikněte na tlačítko "PŘIHLÁSIT SE". Uživatel získá přímý přístup ke svému osobnímu počítači wallet, zcela izolovaný od administračního rozhraní.



### Interface od uživatele wallet



Po přihlášení má uživatel přístup ke kompletnímu rozhraní wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Funkce rozhraní :




- Aktuální zůstatek**: Zobrazuje se v sats a ve zvolené měně (v tomto příkladu CUC)
- Hlavní činnosti**: VLOŽIT POŽADAVEK, VYTVOŘIT FAKTURU, ikona QR (rychlé skenování)
- Historie transakcí** : Kompletní seznam všech plateb a příjmů
- Pravý boční panel**: Možnosti konfigurace a přístupu



### Mobilní přístup ke wallet



Pravý boční panel nabízí mimořádně praktickou funkci: mobilní přístup k wallet. Rozbalte část "Mobilní přístup" a zjistěte, jaké možnosti jsou k dispozici.



![Mobile Access](assets/fr/15.webp)



LNbits nabízí několik způsobů, jak tuto aplikaci wallet ve smartphonu používat:



**Možnost 1: Kompatibilní mobilní aplikace




- Stáhněte si **Zeus** nebo **BlueWallet** z App Store nebo Google Play
- Aktivace rozšíření **LndHub** v LNbits pro tento wallet
- Naskenujte QR kód LndHub pomocí mobilní aplikace a připojte zařízení wallet



**Možnost 2: Přímý přístup přes mobilní prohlížeč**




- Kód QR zobrazený v nabídce "Export do telefonu pomocí kódu QR" obsahuje úplnou adresu URL serveru wallet s integrovaným ověřováním
- Naskenováním tohoto QR kódu z chytrého telefonu otevřete wallet přímo v mobilním prohlížeči
- Přidání stránky na domovskou obrazovku pro rychlý přístup



**Důležité zabezpečení**: Tato adresa URL obsahuje klíče API pro plný přístup do wallet. Nikdy jej nesdílejte veřejně. S tímto QR kódem zacházejte stejně jako s privátními klíči Bitcoin - kdokoli naskenuje tento QR kód, získá plný přístup do wallet.



Tato mobilní funkce promění vaši instanci LNbits Umbrel ve skutečný server Lightning wallet pro vás a vaše přátele, přičemž si díky vlastnímu uzlu zachováte naprostou suverenitu nad svými prostředky.



### Sdílení přístupu uživatelů



Hlavním případem použití této konfigurace pro více uživatelů je **společné sdílení peněženek s rodinou nebo blízkými osobami**. Jakmile vytvoříte uživatele s vyhrazeným jménem wallet (například "satoshi" v našem příkladu), můžete tyto přihlašovací údaje sdílet s důvěryhodnými členy své domácnosti.



**Zabezpečení přístupu do služby Umbrel**: Přístup k vaší instanci LNbits na Umbrelu je přirozeně chráněn, protože k ní lze přistupovat pouze :




- V místní síti** : Členové vaší domácnosti připojeni ke stejné síti WiFi/Ethernet mohou přistupovat k instanci
- Přes VPN**: Pokud na serveru Umbrel používáte nakonfigurovanou síť VPN, jako je Tailscale, mohou oprávnění uživatelé získat bezpečný vzdálený přístup



Díky této dvojité vrstvě ochrany (přístup k síti + ověření uživatele) není možnost "Povolit vytváření nových uživatelů" v systému Umbrel tak kritická. Do přihlašovacího rozhraní se dostanou pouze osoby, které již mají přístup k vaší síti nebo VPN.



**Typický scénář**: Vytvoříte účet "otec", účet "matka", účet "firma" atd. Každý člen rodiny má svůj vlastní izolovaný účet wallet Lightning, přičemž využívá sdílené likvidity vašeho uzlu Umbrel. Stačí sdílet uživatelské jméno a heslo - uživatel se pak může připojit z libovolného zařízení ve vaší místní síti nebo prostřednictvím sítě VPN Tailscale. Další informace naleznete v našem specializovaném výukovém programu Tailscale:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Prozkoumejte dostupná rozšíření



Vraťte se do rozhraní SuperUser a v levém postranním panelu přejděte do nabídky "Extensions", kde najdete kompletní ekosystém rozšíření LNbits.



![Extensions disponibles](assets/fr/16.webp)



LNbits nabízí bohatý katalog rozšíření, která promění vaši instanci ve skutečnou platformu služeb Lightning:





- Jukebox**: Systém jukeboxu s napájením sats (platby Spotify)
- Lístky podpory**: Placený systém podpory (dostáváte satsy na zodpovězení dotazů)
- TPoS**: Bezpečný mobilní terminál pro prodejce
- Správce uživatelů**: pokročilá správa uživatelů a wallet (kterou jsme právě použili)
- Události**: Prodej a ověřování platnosti vstupenek na akce
- LNURLZařízení**: Správa prodejních míst, bankomaty, připojené přepínače
- SMTP**: Umožněte uživatelům odesílat e-maily a získávat satss
- Boltcards**: Programování NFC karet pro platby Lightning tap-to-pay
- NostrNip5**: Vytvářejte adresy NIP5 pro své domény
- Rozdělené platby**: Automatické rozdělení plateb mezi více peněženek



Každé rozšíření se aktivuje jediným kliknutím v tomto rozhraní. Rozšíření označená "FREE" jsou zdarma, některá jsou k dispozici v placené verzi. Prozkoumejte katalog a vyberte ta, která odpovídají vašim potřebám - ať už jde o podnikání, správu rodiny nebo experimentování s možnostmi Lightning Network.



## Výhody a omezení



**Výhody**: (úplná kontrola nad prostředky/klíči/daty), flexibilita architektury (bezztrátová migrace VPS→full node), profesionální systém rozšíření, intuitivní rozhraní.



**Omezení** : Software v beta verzi (opatrně s ohledem na množství), zabezpečení v odpovědnosti správce, URL obsahující citlivé klíče API (povinné HTTPS), správa více uživatelů znamená odpovědnost správce.



## Osvědčené postupy



**Zálohy**: Zálohy: Phoenixd Seed/LND pověření, databáze LNbits, soubory .env. Automatizovat denně, uchovávat mimo produkční server, šifrované. Pravidelně testovat obnovení.



**Údržba**: Pravidelně kontrolujte aktualizace (LNbits, Lightning backend, operační systém). Před významnými aktualizacemi vždy zkontrolujte poznámky k vydání.





- Na deštníku**: App Store vás automaticky upozorní na nové verze. Synchronizujte rozšíření prostřednictvím "Správa rozšíření" > "Aktualizovat vše". Zkontrolujte zařazení databáze SQLite do automatických záloh Umbrel.
- Na VPS**: Lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Sledujte systémové protokoly: `sudo journalctl -u lnbits -f`.



## Závěr



Samostatné hostování LNbits nabízí konkrétní cestu k finanční suverenitě Blesku. VPS+Phoenixd nabízí odlehčené řešení pro rychlé služby, Umbrel plnou integraci se stávajícím uzlem Bitcoin. Škálovatelná architektura umožňuje vývoj od jednoduchého víceuživatelského wallet až po sofistikované obchodní případy použití.



Samostatné hostování znamená odpovědnost: zálohujte semena, chraňte přístup, začněte se skromnými částkami. Díky těmto opatřením se LNbits stává robustním řešením pro bleskovou ekonomiku a zároveň zachovává decentralizaci a autonomii.



## Zdroje



### Oficiální dokumentace




- [Dokumentace LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [Oficiální průvodce instalací](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Průvodci Společenství




- [Počáteční konfigurace serveru Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) by Daniel P. Costas (zabezpečení VPS krok za krokem)
- [LNbits + Phoenixd instalace na Ubuntu VPS](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) Daniel P. Costas (kompletní průvodce)
- [LNbits Server na Clearnetu](https://ereignishorizont.xyz/lnbits-server/en/) od Axel
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes