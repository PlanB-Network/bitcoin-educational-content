---
name: Ride The Lightning (RTL)
description: Ke správě uzlu Lightning použijte aplikaci Ride The Lightning (RTL)
---
![cover](assets/cover.webp)


## 1. Úvod



**Ride The Lightning (RTL)** je kompletní webová aplikace Interface pro správu uzlu Lightning Network. Tato samostatně hostovaná webová aplikace nabízí **kokpit Lightning** přístupný z prohlížeče. RTL pracuje se všemi hlavními implementacemi Lightning (LND, Core Lightning/CLN a Eclair) a poskytuje vám úplnou kontrolu nad vaším uzlem a kanály. RTL je zdarma a s otevřeným zdrojovým kódem (licence MIT) a je standardně integrován do mnoha hotových řešení uzlů (RaspiBlitz, MyNode, Umbrel atd.).



**Bez grafického rozhraní Interface lze uzly Lightning spravovat pouze pomocí uživatelsky přívětivých příkazů CLI. RTL tyto operace zjednodušuje pomocí ergonomického Interface. Zde jsou hlavní aplikace:**





- **Zobrazení kanálů a uzlů** - Na ovládacím panelu se zobrazuje zůstatek On-Chain, likvidita Lightning (místní/vzdálená), stav synchronizace, alias uzlu a další údaje. Můžete si zobrazit seznam kanálů, kapacitu, místní/vzdálenou distribuci a stav. RTL nabízí kontextové ovládací panely pro analýzu činnosti z různých úhlů pohledu.





- **Blesková správa kanálů** - Otevřete/zavřete kanály několika kliknutími. RTL umožňuje připojit se k partnerovi a otevřít kanál bez příkazu. Můžete upravit poplatky za směrování, zobrazit skóre zůstatku nebo iniciovat kruhové vyvážení pro změnu rovnováhy prostředků mezi kanály.





- **Sledování a provádění plateb** - RTL spravuje transakce Lightning: odesílání plateb prostřednictvím faktur, příjem faktur generate, sledování transakcí (platby, směrování) s podrobnou historií. Interface také analyzuje směrování a zjišťuje, které platby procházejí vaším uzlem.





- **Wallet Správa a zálohování On-Chain** - Karta On-Chain umožňuje zadávat adresy generate a odesílat transakce. RTL usnadňuje ukládání kanálů exportem souboru SCB pro LND s automatickou aktualizací při každé změně kanálu.



Stručně řečeno, RTL je **výkonný přístrojový panel pro Lightning Network**, který nabízí vzdělávací Interface pro každodenní pilotování vašeho uzlu. Tento návod vás provede jeho instalací a používáním pro správu kanálů a plateb.



## 2. Technický provoz RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Než se pustíme do podrobností, je užitečné stručně pochopit **jak RTL spolupracuje s uzlem Lightning** na technické úrovni.



**Obecná architektura:** RTL je webová aplikace vytvořená pomocí Node.js (backend) a Angular (frontend). Konkrétně RTL běží jako malý místní webový server (ve výchozím nastavení na portu 3000), který vede dialog s vaší implementací Lightning prostřednictvím svých rozhraní API. V závislosti na typu :





- S modulem **LND** používá RTL k provádění příkazů Lightning rozhraní REST API modulu LND (port 8080). Připojení je zabezpečeno protokolem TLS a pro ověření vyžaduje soubor **admin macaroon** systému LND.





- S **Core Lightning (CLN)** používá RTL buď rozhraní REST API poskytované modulem *c-lightning-REST*, nebo **přístupovou runu** prostřednictvím zásuvného modulu `commando`. Řešení jako Umbrel automaticky konfigurují tyto Elements.





- S rozhraním **Eclair** se RTL připojí k rozhraní Eclair REST API pomocí nakonfigurovaného ověřovacího hesla.



**Konfigurace a zabezpečení:** RTL se konfiguruje pomocí souboru JSON (`RTL-Config.json`), kde definujete webový port, přístupové heslo a informace o připojení k uzlu. Web Interface je chráněn přihlašovacím jménem/heslem (výchozí `heslo` lze změnit) a podporuje 2FA. Ve výchozím nastavení běží RTL jako lokální HTTP (`http://localhost:3000`), ale pro vzdálený přístup vždy používejte zabezpečené připojení (HTTPS přes reverzní proxy, Tor nebo VPN).



Stručně řečeno, RTL je další komponenta, která se připojuje k uzlu prostřednictvím zabezpečených rozhraní API, vyžaduje příslušné přístupové tokeny a nabízí vlastní zabezpečení Layer. Tato modulární architektura dokonce umožňuje spravovat **několik uzlů Lightning pomocí jediné instance RTL**.



## 3. Instalace RTL



Protože je RTL šířen jako software s otevřeným zdrojovým kódem, existuje několik způsobů, jak jej do systému nainstalovat. V této části se budeme zabývat dvěma hlavními přístupy: ruční instalací a instalací pomocí nástroje Umbrel.



### Manuální metoda



Ruční instalace je vhodná, pokud si chcete zachovat jemnou kontrolu nebo pokud integrujete jazyk RTL do vlastní konfigurace. Níže uvedené kroky se týkají uzlu LND se systémem Linux (např. Raspberry Pi nebo VPS s Ubuntu/Debian), ale jsou podobné i pro CLN/Eclair.



**Předpoklad:** ujistěte se, že máte v počítači **synchronizovaný** uzel Bitcoin a funkční uzel Lightning (LND, CLN nebo Eclair). RTL neobsahuje uzel Lightning jako takový, připojuje se k existujícímu uzlu. Potřebujete také nainstalovaný **Node.js** (doporučená verze 14+). Můžete to zkontrolovat pomocí `node -v` nebo nainstalovat Node z oficiálních stránek (https://nodejs.org/en/download/) nebo ze svého správce balíčků.



Hlavní fáze instalace jsou :



**Stáhněte si kód RTL**: Klonujte oficiální repozitář RTL na GitHubu do adresáře, který si vyberete. Například:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Instalace závislostí**: RTL je aplikace Node.js, takže je třeba nainstalovat její potřebné moduly. Ve složce RTL spusťte příkaz :



```bash
npm install --omit=dev --legacy-peer-deps
```



Tento příkaz nainstaluje potřebné balíčky NPM (ignoruje vývojové závislosti). Doporučuje se použít volbu `--legacy-peer-deps`, aby se předešlo možným konfliktům závislostí na Node.



**RTL-Config**: Po vytvoření závislostí připravte konfigurační soubor. Zkopírujte/přejmenujte soubor `Sample-RTL-Config.json` v kořenovém adresáři projektu na `RTL-Config.json`. Otevřete jej ve svém :





- **Heslo uživatelského rozhraní**: zvolte bezpečné heslo a zadejte ho do `multiPass` (místo výchozího `"heslo"`).
- **Port**: výchozí `3000`. Pokud je tento port na vašem počítači již obsazen, můžete jej změnit.
- **Uzel**: v sekci `uzly[0]` nastavte parametry pro svůj uzel:
     - `lnNode`: popisný název uzlu (např. `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (případně `"CLN"`/`"ECL"`).
     - V části `autentizace`:
       - macaroonPath`: zadejte úplnou cestu ke složce obsahující správce macaroon LND.
       - `configPath`: cesta ke konfiguračnímu souboru uzlu (`LND.conf` pro LND).
     - V části `Nastavení`:
       - `fiatConversion`: nastavte na `true`, pokud chcete provést konverzi fiat měny.
       - `unannouncedChannels`: nastavte na `true` pro zobrazení neohlášených kanálů.
       - themeColor` a `themeMode`: Interface přizpůsobení.
       - channelBackupPath`: cesta pro zálohy kanálů LND.
       - `lnServerUrl`: URL vašeho uzlu Lightning (např. `https://127.0.0.1:8080`).



**Spustit server RTL**: V adresáři RTL spusťte příkaz :



```bash
node rtl
```



Aplikace se spustí a je přístupná na adrese `http://localhost:3000`.



**(Volitelné) Spusťte RTL jako službu**: Pro automatické spuštění vytvořte systemd :



Za tímto účelem:




- Otevřete terminál v počítači.
- Vytvořte nový soubor služby pomocí následujícího příkazu (`nano` nahraďte svým oblíbeným editorem):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Zkopírujte a vložte níže uvedený obsah do tohoto souboru:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Nahraďte `/path/to/RTL/rtl` skutečnou cestou k souboru `rtl` na vašem počítači a `<your_user>` svým uživatelským jménem v Linuxu.
- Uložte a zavřete soubor.
- Znovu načtěte konfiguraci systemd:


```bash
sudo systemctl daemon-reload
```




- Aktivujte a spusťte službu RTL:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL se nyní automaticky spustí při každém restartu počítače. Jeho stav můžete zkontrolovat pomocí :


```bash
sudo systemctl status RTL
```



### Instalace přes Umbrel



Pokud používáte [Umbrel](https://getumbrel.com), je instalace RTL mnohem jednodušší:





- Přístup ke službě Interface Umbrel (obvykle prostřednictvím `http://umbrel.local`)
- Přejděte do **App Store**
- Hledat "Ride The Lightning"



**Důležitá poznámka: v obchodě Umbrel App Store jsou dvě samostatné aplikace RTL:**




- **Ride The Lightning** (pro LND): pro použití s výchozím bleskovým uzlem Umbrel (LND).
- **Ride The Lightning (Core Lightning)**: použijte pouze v případě, že máte nainstalovanou aplikaci *Core Lightning* na Umbrel a chcete tento uzel spravovat pomocí RTL.



*Každá verze RTL je předkonfigurována pro dialog s odpovídající implementací (LND nebo Core Lightning). Pokud jste svůj uzel Lightning nezměnili, jednoduše zvolte klasickou verzi LND*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Klikněte na **Instalace**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Důležité:** Po instalaci se na obrazovce RTL zobrazí výchozí heslo. **Toto heslo si zkopírujte a uložte** - budete ho potřebovat k přihlášení do programu Interface RTL. Toto heslo se zobrazí při každém spuštění RTL, dokud nezaškrtnete možnost "Nezobrazovat znovu".



Umbrel se automaticky postará o :




- Stažení a konfigurace jazyka RTL
- Konfigurace přístupu k uzlu Lightning
- Správa aktualizací
- Zajištění přístupu ke Interface



Po instalaci se aplikace objeví v nabídce *Apps* v aplikaci Umbrel. Kliknutím na **Ride The Lightning** ji spustíte.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Na přihlašovací obrazovce zadejte heslo, které jste si dříve zkopírovali. Po přihlášení bude webový RTL Interface přístupný přímo z ovládacího panelu Umbrel bez nutnosti další konfigurace!



## 4. Zavedení a použití Interface RTL



Nyní, když je RTL spuštěn, prozkoumejme jeho web Interface a jeho klíčové funkce. Projdeme si jednotlivé části aplikace, abychom vám poskytli kompletní přehled.



### Hlavní ovládací panel



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Jakmile se přihlásíte, získáte přístup k **hlavnímu panelu**, který vám poskytne přehled o vašem uzlu Lightning. Na této stránce jsou soustředěny základní informace:




- Váš celkový zůstatek na účtu Lightning
- Dostupný zůstatek On-Chain
- Rozdělení vaší likvidity (příchozí/odchozí)
- Rychlý přístup k odesílání a přijímání Satss prostřednictvím uzlu Lightning



### Správa fondů On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Na kartě **On-Chain** můžete spravovat své bitcoiny přímo v hlavním řetězci:




- Zobrazení zůstatku v různých jednotkách (Sats, BTC, USD)
- Úplný seznam transakcí
- Address generace Taproot (P2TR), P2SH (NP2WKH) nebo Bech32 (P2WKH)
- Správa UTXO, příjem a odesílání bitcoinů



### Lightning: podrobná prezentace podnabídek



Interface RTL obsahuje postranní nabídku věnovanou Lightning Network, která sdružuje všechny základní funkce pro správu uzlu. Zde jsou uvedeny podrobnosti o jednotlivých dílčích nabídkách v pořadí podle obrázku obrazovky:



#### 1. Kolegové/kanály



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Tato podnabídka umožňuje :




- Zobrazení seznamu připojených kolegů a otevřených nebo čekajících kanálů Lightning.
- Přidání nového partnera (připojení k jinému uzlu Lightning).
- Otevření, uzavření nebo správa stávajících kanálů.
- Zobrazení podrobností o každém kanálu: kapacita, místní/vzdálené zůstatky, stav, historie obchodování, bilanční skóre atd.



#### 2. Transakce



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



V této podnabídce můžete :




- Odesílání plateb Lightning (prostřednictvím Invoice).
- generate a spravovat faktury pro příjem plateb.
- Zobrazit kompletní historii odeslaných a přijatých plateb s podrobnostmi (částka, datum, stav, poplatky, počet vynechaných plateb atd.).



#### 3. Směrování



V této dílčí nabídce se zobrazí :




- Platby směrované vaším uzlem pro ostatní uživatele Lightning Network.
- Statistiky směrování: počet předaných transakcí, získané poplatky, zjištěné chyby.
- Exportovatelná historie pro pokročilou analýzu.



#### 4. Odklady



Tato podnabídka nabízí :




- Podrobné zprávy o činnosti uzlu Lightning.
- Grafy a tabulky kanálů, plateb, poplatků, kapacity atd.
- Nástroje pro lepší pochopení výkonu uzlu.



#### 5. Vyhledávání grafů



Tato podnabídka umožňuje :




- Prozkoumejte topologii systému Lightning Network.
- Vyhledávání konkrétních uzlů nebo kanálů.
- Získejte informace o konektivitě a celkové kapacitě sítě.



#### 6. Podepsat/ověřit



Tato podnabídka nabízí :




- Možnost podepsat zprávu klíčem svého uzlu (důkaz Ownership).
- Ověřování podpisu pro ověřování zpráv z jiných uzlů.



#### 7. Záloha



Tato podnabídka je určena pro zálohování:




- Export souboru zálohy kanálu (SCB pro LND).
- V případě potřeby obnovte konfiguraci nebo kanály.
- Tipy pro zabezpečení záloh.



#### 8. Uzel/síť



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



V této podnabídce najdete :




- Kompletní shrnutí stavu uzlu Lightning: alias, verze, barva, stav synchronizace.
- Statistiky kanálů (aktivní, čekající, uzavřené), celková kapacita, konektivita.
- Informace o globální síti Lightning Network a pozici vašeho uzlu v ní.



### Služby: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz je služba Exchange, která neomezuje soukromí a převádí bitcoiny mezi Lightning Network a Blockchain Bitcoin (On-Chain). Nabízí dva typy operací: Reverzní podmořský swap (**Swap Out**) a podmořský swap (**Swap In**).



#### Swap Out (Reverzní výměna ponorek)



Funkce Swap Out převádí saty dostupné na Lightning Network na bitcoiny On-Chain. Tento mechanismus je užitečný, když uzlu dojde příchozí kapacita nebo když chcete získat zpět prostředky z On-Chain Address. Proces funguje následovně:




- Uživatel vybere částku, která má být vyměněna
- Uzel odešle Boltzovi platbu Lightning
- V Exchange blokuje Boltz ekvivalentní částku v bitcoinech On-Chain
- Jakmile je transakce potvrzena, může si uživatel vyžádat finanční prostředky odhalením tajemství použitého při výměně



Tento proces není vázán na majetek uživatele a společnost Boltz nikdy nedrží jeho finanční prostředky.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Výměna (Submarine Swap)



Swap In naproti tomu umožňuje, aby prostředky z On-Chain byly znovu vloženy do Lightning Network. To je užitečné zejména pro obnovení výstupní kapacity kanálů. Postup je následující:




- Uživatel posílá bitcoiny na konkrétní číslo Address vygenerované společností Boltz
- Tyto prostředky může Boltz uvolnit pouze v případě, že zaplatí poplatek Lightning Invoice generovaný uzlem uživatele
- Po zaplacení částky Invoice jsou prostředky k dispozici v kanálu Lightning, čímž se zvýší výstupní kapacita uzlu



![Configuration d'un swap-in](assets/fr/12.webp)



Tyto dva mechanismy umožňují efektivně řídit likviditu bleskového kanálu při zachování suverenity uživatele nad jeho prostředky.



### Konfigurace a přizpůsobení



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



Na kartě **Konfigurace uzlu** si můžete přizpůsobit prostředí:




- Aktivace neohlášených kanálů
- Přizpůsobení prodejního displeje
- Konfigurace Block explorer
- Nastavení Interface



### Dokumentace a nápověda



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



A konečně, sekce **Nápověda** nabízí komplexní dokumentaci k :




- Počáteční konfigurace
- Řízení partnerů a kanálů
- Platby a transakce
- Zálohování a obnovení
- Zprávy a statistiky
- Podpisy a ověření
- Parametry uzlu a aplikace



Tento komplexní model Interface vám umožní efektivně spravovat uzel Lightning, od základních operací až po pokročilé funkce, a to vše v intuitivním a přehledném modelu Interface.



## 5. Pokročilé případy použití a zabezpečení



V této části se dozvíte, co potřebujete vědět, abyste se s RTL dostali dál a zabezpečili svůj uzel Lightning:



### Monitorování a řešení problémů



Chcete-li sledovat svůj uzel, můžete exportovat data RTL (protokoly, CSV) a zobrazit je v nástrojích, jako je Grafana. V případě problému (zablokovaná platba, neaktivní kanál) nahlédněte do protokolů LND/CLN a použijte diagnostické příkazy (`lncli listchannels`, `lncli pendingchannels` atd.). RTL nabízí také protokoly Interface pro sledování událostí směrování.



### Zabezpečený vzdálený přístup



Nikdy nevystavujte RTL přímo na internetu. Dávejte přednost :




- **VPN** (např. Tailscale) pro soukromý, šifrovaný přístup
- **Tor** pro bezpečný a anonymní přístup
- Reverzní proxy server **HTTPS** (Nginx/Caddy) pouze pokud víte, jak jej nakonfigurovat



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Správné bezpečnostní postupy





- **Chraňte svůj přístup**: nikdy nesdílejte heslo admin.macaroon nebo RTL. Omezte oprávnění k citlivým souborům.
- **Pravidelné zálohování**: po každé změně exportujte soubor zálohy kanálu (SCB) a uložte jej mimo uzel.
- **Aktualizace**: udržujte RTL, svůj uzel a Umbrel v aktuálním stavu s nejnovějšími bezpečnostními opravami.
- **Důvěrnost**: před sdílením anonymizujte protokoly a snímky obrazovky. Nikdy nesdílejte své zůstatky nebo seznamy kolegů veřejně.
- **Jediný přístup**: RTL není víceuživatelský. Nesdílejte přístup správce. Pro přístup pouze pro čtení použijte v případě potřeby vyhrazený makropřístup.



Uplatněním těchto zásad výrazně omezíte rizika a zachováte si kontrolu nad uzlem Lightning.



## 7. Závěr



**Ride The Lightning** je základním nástrojem pro efektivní správu uzlu Bitcoin/Lightning, ať už jste začátečník nebo pokročilý uživatel. Poskytuje přehledné Interface pro ovládání kanálů, plateb a stavu uzlu a zároveň prohlubuje vaše znalosti Lightning Network.



RTL vyniká kompatibilitou s mnoha implementacemi, pokročilými funkcemi (rebalancování, swapy, reporty) a pedagogickým přístupem. Pro jednoduché potřeby postačí Interface Umbrel nebo Wallet mobile, ale RTL dává dokonalý smysl pro aktivní, optimalizovanou správu uzlů.



Chcete-li se dozvědět více :




- Oficiální webové stránky RTL: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Technické diskuse, oznámení projektů, zpětná vazba a vzdělávací zdroje
- **Fórum komunity Umbrel**: [community.getumbrel.com](https://community.getumbrel.com) - Oficiální fórum se sekcí věnovanou Bitcoin/Lightning, návody a řešením běžných problémů
- **Lightning Network Vývojáři**: [github.com/lightning](https://github.com/lightning) - Oficiální úložiště GitHub pro sledování vývoje a přispívání zdrojovým kódem
- Zásobník Exchange **Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Technické otázky a odpovědi pro vývojáře a pokročilé uživatele



Stručně řečeno, RTL vám poskytuje úplnou kontrolu nad vaším uzlem Lightning v moderním, plně vybaveném modelu Interface.



**Zdroje :** Oficiální webové stránky RTL; RTL GitHub; Umbrel App Store; Umbrel Community; zdroje sítě Plan B.



Chcete-li si prohloubit své znalosti o tom, jak Lightning Network funguje, doporučuji vám také absolvovat tento bezplatný kurz:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb