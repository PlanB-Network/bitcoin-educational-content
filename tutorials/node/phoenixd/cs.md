---
name: Phoenixd
description: Nasazení vlastního minimalistického uzlu Lightning pomocí Phoenixd
---

![cover](assets/cover.webp)



Finanční autonomie znamená také kontrolu nad infrastrukturou Lightning. Pro vývojáře a společnosti, které chtějí integrovat Bitcoin Lightning do svých aplikací, představuje **Phoenixd** ideální řešení: minimalistický specializovaný uzel Lightning s automatickou správou likvidity.



Phoenixd je server Lightning vyvinutý společností ACINQ a určený speciálně pro odesílání a přijímání plateb Lightning prostřednictvím rozhraní HTTP API. Na rozdíl od plnohodnotných implementací, jako je LND nebo Core Lightning, Phoenixd abstrahuje od veškeré složitosti správy kanálů a zároveň zachovává vlastní ochranu vašich prostředků.



V tomto tutoriálu se podíváme, jak nainstalovat, nakonfigurovat a používat Phoenixd k vývoji aplikací Lightning s vlastní infrastrukturou a snadno použitelným rozhraním API.



## Co je Phoenixd?



Phoenixd je minimální specializovaný uzel Lightning vyvinutý společností ACINQ. Je to řešení určené pro vývojáře a podniky, které chtějí integrovat Lightning do svých aplikací bez složité správy Full node.



### Princip fungování



**Phoenixd je minimální uzel Lightning, který používá ACINQ jako svého poskytovatele služeb Lightning (LSP) pro automatickou likviditu. Při přijímání plateb Lightning automaticky otevírá kanály s uzly ACINQ, aby přidělil potřebnou příchozí kapacitu. Tato likvidita "on-the-fly" je okamžitá, ale zpoplatněná přesně **1 % + poplatky Mining** z přijaté částky.



**Automatická správa:** Systém spravuje tři klíčové položky Elements:




- Kanály Lightning**: Otevírejte, zavírejte a spravujte automaticky podle potřeby
- Příchozí/odchozí likvidita**: Automatické poskytování prostřednictvím spojování a otevírání kanálů
- Poplatek za kredit** : Drobné platby, které nestačí k ospravedlnění kanálu, se ukládají jako rezerva na budoucí poplatky



### Výhody společnosti Phoenixd



**Vy máte pod kontrolou své soukromé klíče (12 slov seed) a finanční prostředky. Phoenixd generuje vaše klíče Wallet lokálně, aniž by je kdy sdílel.



**Osobní infrastruktura:** Phoenixd běží na vašem serveru, což vám umožňuje přístup k podrobným protokolům, konfiguraci a ovládání API. Přístup k vašim prostředkům již není závislý na službě třetí strany.



**Integrované rozhraní API:** Phoenixd nabízí rozhraní API HTTP pro integraci s jinými službami, nativní podporu LNURL a vývoj vlastních aplikací.



**Snadná integrace:** Díky jednoduchému rozhraní REST API lze Phoenixd integrovat do jakékoli aplikace nebo služby vyžadující platby Lightning.



**Důležitá poznámka:** Automatická likvidita stále pochází od ACINQ jako LSP (Lightning Service Provider). Phoenixd používá pro automatickou správu kanálů stejný mechanismus jako Phoenix mobile.



## Instalace aplikace Phoenixd



### Předpoklady



Phoenixd vyžaduje prostředí Linux (doporučujeme Ubuntu/Debian) se základními znalostmi příkazového řádku. Pro optimální výkon budete potřebovat :





- Server Linux**: VPS nebo místní počítač se stabilním připojením
- OpenJDK 21** : Běhové prostředí Javy
- Stabilní připojení k internetu**: Pro synchronizaci s Lightning Network
- Název domény** (nepovinné) : Pro zabezpečený přístup HTTPS k rozhraní API



### Stažení a instalace



**1. Stáhnout Phoenixd**



Přejděte na stránku [GitHub releases] (https://github.com/ACINQ/phoenixd/releases) a stáhněte si nejnovější verzi pro vaši architekturu:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. První spuštění



Spusťte inicializaci systému Phoenixd:



```bash
./phoenixd
```



Při prvním spuštění budete vyzváni k potvrzení dvou důležitých kroků zadáním "Rozumím" :



**Zpráva 1 - Zálohování:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Těchto 12 slov si uložte** - je to jediná záruka vašeho uzdravení.



**Zpráva 2 - Automatická likvidita:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Pro každé potvrzení zadejte `Rozumím`.



![Premier démarrage](assets/fr/01.webp)



*První spuštění aplikace Phoenixd: záložní potvrzení a automatická likvidita*



**3. Konfigurace v provozu** (pouze ve francouzštině)



Pro nepřetržitý provoz vytvořte systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Služba Phoenixd aktivní a funkční prostřednictvím systemd a `auto-liquidity` na 2m sat*



## Konfigurace a zabezpečení



### Konfigurační soubor



Phoenixd automaticky vytvoří soubor `~/.phoenix/phoenix.conf` se základními parametry:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Klíčové parametry:**




- `autoliquidity`: Velikost automaticky otevíraných kanálů (výchozí: 2M Sats)
- http-password`: Heslo administrátora pro API (vytváření Invoice a odesílání plateb)
- http-password-limited-access`: Omezené heslo (pouze při vytváření Invoice)



### Zabezpečený přístup pomocí HTTPS



Ve výchozím nastavení je rozhraní Phoenixd API dostupné pouze prostřednictvím místního protokolu HTTP (`http://127.0.0.1:9740`). Chcete-li uzel používat zvenčí (mobilní aplikace, jiné servery, webové integrace), musíte nakonfigurovat zabezpečený přístup HTTPS.



**Zpětný princip proxy:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** funguje jako **reverzní proxy server**: naslouchá požadavkům HTTPS z Internetu na portu 443, přesměruje je na lokální port Phoenixd (port 9740) a poté odesílá šifrované odpovědi zpět klientovi.



**Certifikát SSL/TLS** je digitální soubor, který :




- Prokázání identity serveru** (zabrání útokům typu man-in-the-middle)
- Povoluje šifrování HTTPS**: všechna data, včetně hesel API, jsou během přenosu šifrována
- Vydává zdarma** společnost Let's Encrypt prostřednictvím nástroje certbot



Tato konfigurace umožňuje :




- Zabezpečený přístup k rozhraní API z internetu**
- Šifrování hesel API** během přenosu (aby se zabránilo jejich přenosu v otevřeném textu)
- Integrace Phoenixd** do externích aplikací vyžadujících HTTPS
- Dodržování bezpečnostních standardů** pro finanční rozhraní API



Konfigurace tohoto reverzního proxy serveru HTTPS pomocí nginx :



**1. Konfigurace Nginx**



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. SSL** certifikát



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Funkční test



Zkontrolujte, zda Phoenixd pracuje správně:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Tyto příkazy by měly vracet informace JSON o stavu a zůstatku uzlu (zpočátku prázdné).



![Commandes CLI](assets/fr/03.webp)



*Příkazy getinfo a getbalance pro kontrolu stavu uzlu*



## Používání rozhraní API



### První test příjmu



**1. Vytvoření blesku** Invoice



Pomocí rozhraní API vytvořte první službu Invoice:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Porozumění mechanismu automatické likvidity



**Základní princip:** Když obdržíte platbu Lightning, Phoenixd musí někdy otevřít nový kanál, aby ji mohl přijmout. Toto otevření kanálu stojí poplatek, který se **automaticky odečítá** od přijaté částky.



**Konkrétní příklad se 100 000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*První přejímací test: Sats 100 tisíc, konečný zůstatek Sats 75 561 po odečtení nákladů na likviditu*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Výpočet poplatku:**




- Poplatek za služby**: 1 % kapacity kanálu (2 115 000 Sats) = 21 150 Sats
- Poplatky Mining**: (pro transakci On-Chain): ~3 289 Sats (pro transakci On-Chain)
- Celkem**: 24 439 Sats automaticky odečteno



**Ověření pomocí příkazů CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Konečný zůstatek po odeslání platby: 257 Sats zbývající po odeslání zásilky Lightning*



**Poplatkový kredit pro malé platby:** Pokud obdržíte platby příliš malé na to, abyste mohli odůvodnit otevření kanálu (< cca 25 tisíc Sats), uloží se do nevratného "poplatkového kreditu". Tento kredit bude použit na úhradu budoucích poplatků za kanál, jakmile obdržíte dostatečnou částku.



**2. Sledujte otevření kanálu**



Sledujte protokoly Phoenixd:



```bash
journalctl -u phoenixd -f
```



Zobrazí se otevření kanálu a automatické odečtení poplatků za likviditu. Poplatky se liší podle podmínek Mempool Bitcoin, ale vždy zahrnují 1% servisní poplatek plus aktuální poplatek Mining.



**3. Zkontrolujte kanál**



```bash
./phoenix-cli listchannels
```



Tento příkaz zobrazí aktivní kanály s jejich stavem a zůstatkem.



### Kompletní operace API



Phoenixd zpřístupňuje rozhraní REST API na portu 9740, které umožňuje :



**Základní operace:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Důležité pro náklady:**




- Příjem**: 1 % + poplatek Mining za automatickou likviditu
- Přeprava**: 0.4% poplatek za směrování u Lightning Network



**Webhooks:** Webhooks umožňují společnosti Phoenixd **automaticky upozorňovat** vaše aplikace, když dojde k nějaké události (přijetí platby, zaplacení Invoice, otevření kanálu atd.). Namísto neustálého žádání společnosti Phoenixd o aktualizace obdrží vaše aplikace okamžité oznámení HTTP.



**Váš internetový obchod automaticky obdrží oznámení, když zákazník zaplatí za objednávku, což umožňuje okamžité ověření transakce.



Konfigurace v souboru `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Pokročilé aplikace



### Integrace LNURL



Phoenixd nativně podporuje protokoly LNURL pro pokročilou integraci:



**LNURL-Pay:** Platba za služby kompatibilní s LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Získání prostředků ze služeb LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Ověřování prostřednictvím Lightning pro přístup ke službám


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integrace s LNbits



LNbits může podle své [oficiální dokumentace](https://docs.lnbits.org/guide/wallets.html) používat jako zdroj financování službu Phoenixd:



*konfigurace *LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Tato integrace umožňuje vytvářet podúčty LNbits napájené vaším uzlem Phoenixd a poskytuje webovou službu Interface pro správu více peněženek Lightning.



### Vlastní aplikace



Díky komplexnímu rozhraní REST API můžete vyvíjet :



**E-commerce:** Přímá integrace plateb Lightning do vašeho obchodu


**Dárcovské služby:** Dárcovské systémy s fakturami a automatickými webhooky


**Boty sociálních sítí:** Boti Telegramu/Discordu s funkcemi tipů


**Paywall Lightning:** Prémiový obsah dostupný za poplatek Lightning



## Bezpečnost a osvědčené postupy



### Ochrana přístupu



**Hesla API:** Automaticky generovaná hesla jsou klíčem k vaší pokladnici Lightning. Nikdy je nesdílejte a v případě pochybností je změňte.



**Firewall:** Nikdy nenechávejte port 9740 otevřený přímo do Internetu. Vždy používejte nginx s protokolem HTTPS.



**Vylepšené ověřování:** Zvažte VPN nebo Tailscale, abyste omezili přístup k serveru pouze na autorizovaná zařízení.



### Základní zálohy



**Obnovení seed:** Uložte svých 12 slov na bezpečné místo mimo server. To je jediná záruka obnovy.



*adresář ~/.phoenix:** Tuto složku pravidelně zálohujte (po vypnutí Phoenixd), abyste zachovali stav kanálu a urychlili obnovu.



**Kódy pro obnovení služeb:** Uschovejte si také záložní kódy pro všechny služby, u kterých jste aktivovali 2FA pomocí aplikace Phoenix.



### Monitorování a údržba



**Záznamy z monitorování:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Aktualizace:** Sledujte [GitHub releases](https://github.com/ACINQ/phoenixd/releases) pro nové verze. Aktualizace je stejně jednoduchá jako výměna binárního souboru a restartování služby.



## Srovnání s alternativami



### Phoenixd vs Phoenix standard



**Fénix standard (mobilní) :**




- ✅ Okamžitá instalace, nulová konfigurace
- ✅ Interface mobile intuitive
- ✅ Stejné automatické ukládání jako Phoenixd
- ❌ Žádné rozhraní API pro vývojáře
- ❌ Žádný přístup k podrobným protokolům



**Phoenixd (server) :**




- ✅ HTTP API pro integrace
- ✅ Plný přístup k protokolům
- ✅ Osobní infrastruktura
- ❌ Vyžaduje technické dovednosti
- ❌ Nutná údržba serveru



**Obě používají jako LSP pro automatickou likviditu ACINQ.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ Úplné ovládání, úplný protokol Lightning
- ✅ Velká komunita, vyspělý ekosystém
- ❌ Komplexní manuální řízení likvidity
- ❌ Velká křivka učení



**Phoenixd :**




- ✅ Automatická správa likvidity (jako Phoenix mobile)
- ✅ API pro vývojáře
- ✅ Zjednodušená konfigurace
- ❌ Používá ACINQ jako LSP (bez nezávislého směrování)
- ❌ Méně flexibilní než úplné uzly



## Řešení běžných problémů



### Problémy s přístupem k API



**Ověření se nezdařilo":**


1. Kontrola hesla v souboru `~/.phoenix/phoenix.conf`


2. Kontrola formátu ověření `-u:password`


3. Ujistěte se, že je spuštěn Phoenixd (`./phoenix-CLI getinfo`)



**Časové limity připojení:**




- Zkontrolujte, zda Phoenixd naslouchá na správném portu (9740)
- Otestování místního přístupu před konfigurací HTTPS
- Zkontrolujte protokoly: `journalctl -u phoenixd -f`



### Problémy s likviditou



**Platby nepřicházejí :**


1. Zkontrolujte, zda částka přesahuje minimální hranici (~30k Sats)


2. Prohlížení protokolů pro identifikaci chyb v kanálech


3. V případě potřeby restartujte Phoenixd



**Zůstatek ve "výdajovém kreditu":**


Drobné platby jsou uloženy jako rezerva. Přijetím vyšší částky se spustí otevření kanálu a tyto prostředky se uvolní.



## Závěr



Phoenixd představuje pro vývojáře vynikající kompromis mezi snadností použití a technickou suverenitou. Nabízí jednoduché, ale výkonné rozhraní Lightning API s automatickou správou likvidity, čímž eliminuje složitost tradičních uzlů Lightning.



Toto řešení je vhodné zejména pro vývojáře a společnosti, které chtějí :




- Integrace Bitcoin Lightning do vašich aplikací
- Vyhněte se složitosti správy kanálů Lightning
- Využijte výhod samostatně hostované infrastruktury
- Jednoduché a spolehlivé rozhraní API



S Phoenixd si můžete vytvořit vlastní soukromou infrastrukturu Lightning s moderním rozhraním REST API a automatickou správou technických aspektů. Je to ideální řešení pro demokratizaci integrace Lightning ve vašich projektech.



## Užitečné zdroje



### Oficiální dokumentace




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Zdrojové kódy a verze
- Stránka serveru Phoenix**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Úplná dokumentace
- Často kladené dotazy Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Často kladené otázky



### Podpora Společenství




- Problémy na GitHubu** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Technická podpora
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Novinky a oznámení