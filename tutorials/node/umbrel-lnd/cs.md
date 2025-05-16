---
name: Deštník LND
description: Pokročilý návod na instalaci a konfiguraci Lightning Network Daemon (LND) v systému Umbrel
---
![cover](assets/cover.webp)




## Úvod



Tento pokročilý návod vás krok za krokem provede instalací, konfigurací a používáním aplikace Lightning Node (LND) v uzlu Umbrel. Naučíte se otevírat kanály, spravovat likviditu a synchronizovat uzel s mobilní aplikací.



## 1. Předpoklad: funkční uzel Bitcoin Umbrel



Před nasazením blesku Lightning musíte mít plně funkční uzel Bitcoin v systému Umbrel. To zahrnuje instalaci Umbrel (na Raspberry Pi, NAS nebo jiný počítač) a plnou synchronizaci Blockchain Bitcoin.



Pro instalaci Umbrelu a konfiguraci uzlu Bitcoin doporučujeme postupovat podle našeho specializovaného návodu :



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Ujistěte se, že je váš uzel Bitcoin aktuální a správně funguje, protože Lightning Network na něj spoléhá při všech transakcích off-chain.



## 2. Úvod do Lightning Network



Lightning Network je protokol druhého Layer, který je určen k urychlení a snížení nákladů na transakce Bitcoin tím, že se provádějí mimo hlavní Blockchain.



Konkrétně Lightning využívá síť platebních kanálů mezi uzly: dva uživatelé otevřou kanál zablokováním On-Chain BTC (počáteční transakce) a poté mohou v rámci tohoto kanálu okamžitě provádět platby Exchange. Tyto transakce off-chain se nezaznamenávají na Blockchain, z čehož plyne jejich rychlost a prakticky nulové náklady.



Platby mohou být směrovány více kanály (díky zprostředkujícím uzlům), aby se dostaly ke kterémukoli příjemci v síti, což umožňuje téměř neomezený rozsah okamžitých transakcí. Lightning tak nabízí velmi rychlé a levné transakce, které jsou ideální pro každodenní platby nebo mikrotransakce, a zároveň odlehčuje zátěž Blockchain Bitcoin.



Aby mohl uzel Lightning fungovat, musí být trvale připojen k síti a komunikovat s ostatními uzly Lightning. Existují různé softwarové implementace (LND, Core Lightning, Eclair atd.), které jsou vzájemně kompatibilní. Společnost Umbrel používá LND (Lightning Network Daemon) jako součást své oficiální aplikace Lightning Node. Tento výukový kurz se zaměřuje na LND.



Pro kompletní teoretické seznámení s Lightning Network doporučujeme absolvovat náš specializovaný kurz :



https://planb.network/courses/introduction-theorique-au-lightning-network-34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

V tomto kurzu se důkladně seznámíte se základními koncepty Lightning Network a poté přejdete k praxi s uzlem LND.



## 3. Proč hostovat LND na vlastní pěst?



Provozování vlastního uzlu Lightning (LND) na platformě Umbrel vám dává naprostou suverenitu nad vašimi prostředky a kanály ve srovnání s custodial nebo semi-custodial řešeními.



### Srovnání řešení Lightning :



**Solutions custodiales (např.: Wallet z Satoshi)** :




- Vaše bitcoiny Lightning spravuje důvěryhodná třetí strana
- Snadné použití, žádná technická složitost
- Provozovatel má vaše finanční prostředky a může sledovat vaše transakce
- Obětujete kontrolu a důvěrnost



**Spotřebitelská portfolia bez komodit (např. Phoenix, Breez)** :




- Uživatelé si ponechávají své soukromé klíče, a tím i Ownership svých BTC
- Žádná kompletní správa uzlů - aplikace spravuje kanály na pozadí
- Kompromis mezi jednoduchostí a suverenitou
- Závislost na dodavatelské infrastruktuře z hlediska likvidity
- Technická omezení (jeden smartphone nemůže směrovat platby za jiné)



**Samostatný uzel LND (Umbrel)** :




- Maximální suverenita: vaše BTC On-Chain a off-chain jsou zcela pod vaší kontrolou
- Do otevírání kanálů ani správy vašich plateb nejsou zapojeny žádné třetí strany
- Zvýšená důvěrnost (vaše kanály a transakce jsou známy pouze vám a vašim přímým kolegům)
- Svoboda používání: připojení k vlastním službám a peněženkám
- Možnost směrování transakcí pro ostatní (mikropoplatky)
- Zvýšená technická odpovědnost (údržba, správa likvidity, zálohování)



Stručně řečeno, samoobslužný hosting LND vám poskytuje maximální kontrolu, ale vyžaduje více technických dovedností. Je to kompromis mezi pohodlím a suverenitou.



## 4. Návod krok za krokem



### 4.1 Instalace a konfigurace aplikace Lightning Node v systému Umbrel



Po synchronizaci uzlu Umbrel (Bitcoin) postupujte podle následujících kroků :



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Nainstalujte aplikaci Lightning Node ze sekce "App Store" v Interface Umbrel.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) bude nasazen na váš Umbrel jako aplikace. Při jejím prvním otevření se zobrazí varovná zpráva informující o tom, že Blesk je experimentální technologie.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Můžete si vybrat mezi vytvořením nového uzlu nebo obnovením uzlu ze zálohy/seed. Při první instalaci zvolte vytvoření nového uzlu. Aplikace Lightning Node generate vytvoří 24slovnou frázi Mnemonic (váš seed Lightning): pečlivě si ji zapište (nejlépe offline, na papír), protože bude v případě potřeby použita k obnovení vašich prostředků Lightning.



**Poznámka: V nejnovějších verzích Umbrelu poskytuje instalace aplikace Lightning toto 24slovo seed (samotný uzel Umbrel Bitcoin nikoli).



![Interface principale de Lightning Node](assets/fr/04.webp)



Po inicializaci získáte přístup k hlavnímu uzlu Lightning Node Interface.



![Paramètres de l'application](assets/fr/05.webp)



V nastavení aplikace najdete řadu důležitých možností:




   - Zjistěte si ID uzlu (jedinečný identifikátor uzlu)
   - Připojení externího zařízení Wallet (Připojení Wallet)
   - Zobrazit tajná slova
   - Přístup k pokročilým nastavením
   - Obnovení kanálů
   - Stažení souboru zálohy kanálu
   - Povolení automatického zálohování
   - Konfigurace zálohování přes Tor (Zálohování přes Tor)



Tyto možnosti jsou nezbytné pro zabezpečení a správu uzlu Lightning. Ujistěte se, že jste aktivovali automatické zálohování a že máte v bezpečí svá tajná slova.



**Užitečné zdroje:**




- [Umbrel Community](https://community.umbrel.com) - Diskuzní fórum pro uživatele, kteří sdílejí problémy a řešení týkající se Umbrelu a jeho ekosystému


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Popis funkcí aplikace Lightning Node v aplikaci Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Oficiální dokumentace ke LND

### 4.2 Otevření kanálu Lightning



Po spuštění služby LND můžete otevřít svůj první kanál Lightning. Chcete-li najít kvalitní uzly, ke kterým se můžete připojit:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) je průzkumník pro vyhledávání spolehlivých uzlů pro otevření kanálů.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Například uzel [ACINQ](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) je uznávaným uzlem s vynikajícími statistikami dostupnosti a likvidity.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



V tomto tutoriálu otevřeme kanál s [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Informace potřebné pro připojení (pubkey@ip:port) jsou uvedeny na jejich stránce Amboss.



Otevření kanálu :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Na domovské stránce uzlu Lightning klikněte na tlačítko "+ OPEN CHANNEL"



![Configuration du canal](assets/fr/10.webp)



Na stránce konfigurace kanálu :




   - Vložte ID uzlu zkopírované ze systému Amboss (formát: pubkey@ip:port)
   - Definujte velikost kapacity kanálu (některé uzly jako ACINQ mají minimální hodnoty, např. 400k Sats)
   - V případě potřeby upravte poplatky za zahajovací transakce



![Canal en cours d'ouverture](assets/fr/11.webp)



Po odeslání transakce se kanál na domovské stránce zobrazí jako "otevřený". Vyčkejte na potvrzení transakce On-Chain.



![Détails du canal](assets/fr/12.webp)



Kliknutím na kanál zobrazíte jeho podrobnosti:




   - Aktuální stav
   - Celková kapacita
   - Rozdělení likvidity (příchozí/odchozí)
   - Veřejný klíč vzdáleného uzlu
   - A další technické informace



### Použití Lightning Network+ k získání příchozí likvidity



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



V obchodě s aplikacemi Umbrel je k dispozici aplikace Lightning Network+, která usnadňuje získávání příchozích peněz.



![Interface principale de LN+](assets/fr/14.webp)



Hlavní okno Interface nabízí tři důležité možnosti:




- "Swapy likvidity: prozkoumejte dostupné nabídky swapů
- "Otevřít pro mě": filtrování výměn, pro které máte nárok
- "To Docs": přístup k dokumentaci



![Message d'erreur LN+](assets/fr/15.webp)



Poznámka: Pokud ještě nemáte otevřený kanál, zobrazí se po kliknutí na možnost "Otevřít pro mě" tato chybová zpráva.



![Liste des swaps disponibles](assets/fr/16.webp)



Na stránce "Liquidity Swaps" jsou zobrazeny všechny nabídky swapů dostupné v síti.



![Swaps éligibles](assets/fr/17.webp)



"Otevřít pro mě" filtruje pouze ty výměny, pro které váš uzel splňuje požadované podmínky.



![Détails d'un swap](assets/fr/18.webp)



Příklad údajů o výměně :




- Konfigurace Pentagonu (5 účastníků)
- Kapacita 300k Sats na kanál
- Předpoklad: minimálně 10 otevřených kanálů s celkovou kapacitou 1M Sats
- Volná místa: 4/5



### 4.3 Synchronizace s mobilní aplikací (Zeus)



Pro vzdálené ovládání uzlu Lightning (chytrý telefon) můžete použít aplikaci Zeus (open-source aplikace dostupná pro iOS/Android).



**Konfigurace Zeus s deštníkem :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Ujistěte se, že je váš uzel Umbrel přístupný (ve výchozím nastavení přes Tor).


V deštníku Interface otevřete aplikaci Lightning Node a klikněte na tlačítko "Connect Wallet", jak ukazuje šipka.



![Page de connexion avec QR code](assets/fr/20.webp)



Zobrazí se QR kód obsahující přístupové údaje k LND ve formátu lndconnect. Tento QR kód je obzvláště hustě nabitý informacemi, proto si jej pro snazší čtení neváhejte zvětšit.



![Configuration initiale de Zeus](assets/fr/21.webp)



V telefonu :




   - Otevřít Zeus
   - Na domovské stránce klikněte na možnost "Pokročilé nastavení" a připojte vlastní uzel Lightning
   - V parametrech vyberte možnost "Vytvořit nebo připojit Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



V Diovi:




   - Jako typ připojení vyberte "LND (REST)"
   - Můžete buď naskenovat kód QR (doporučená metoda), nebo zadat informace ručně. (Neváhejte QR kód Umbrel přiblížit, protože je velmi hustý)
   - Důležité: aktivujte možnost "Použít Tor", pokud je váš Umbrel přístupný pouze přes Tor (výchozí nastavení)
   - Uložit konfiguraci



Váš Zeus je nyní připojen k uzlu Umbrel a umožňuje vám provádět bleskové platby, prohlížet si kanály, zůstatky atd., přičemž zůstává zcela samostatně spravován.



**Rozšířené možnosti připojení:**



Ve výchozím nastavení se Zeus ↔ Umbrel připojuje přes Tor. Pro rychlejší připojení existují dvě alternativy:



**Lightning Node Connect (LNC)** :




   - Mechanismus šifrovaného připojení společnosti Lightning Labs
   - Instalace aplikace Lightning Terminal do aplikace Umbrel (zahrnuje přístup k LNC)
   - generate připojovací QR kód v terminálu Lightning (Připojit → Připojit Zeus přes LNC)
   - Naskenujte ji do programu Zeus (jako typ připojení zvolte "LNC")



**VPN Tailscale**:




   - Snadno konfigurovatelná síť VPN
   - Nainstalujte si Tailscale na Umbrel (App Store) a do mobilního telefonu
   - Připojení k Zeus přes soukromou IP adresu Tailscale místo Tor Address



Tyto možnosti nejsou povinné a řešení Tor + Zeus ve většině případů funguje dobře.



> **Užitečné zdroje:**
> - [Zeus Documentation - Umbrel Connection](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Oficiální průvodce připojením Zeus k Umbrelu
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus open-source projekt
> - [Komunita Umbrel - Připojení Zeus přes Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Návod na připojení Zeus k Umbrel pomocí Tailscale

## 5. Bezpečnost a osvědčené postupy



Správa samostatně hostovaného uzlu Lightning vyžaduje zvláštní pozornost věnovanou zabezpečení.



### Zálohování a zabezpečení uzlu



**Zásadní typy záloh**



Uzel Lightning Umbrel vyžaduje dva typy záloh:



**Věta seed (24 slov)**




- Zpětné získání prostředků z On-Chain
- Potřebné k obnovení blesku Wallet
- Pro mimořádně bezpečné ukládání (offline, na papíře)



**Soubor statické zálohy kanálu (SCB)**




- Obsahuje informace o kanálu Lightning
- Umožňuje nucené uzavření kanálu v případě havárie
- Důležité:** Nikdy neukládejte soubor `channel.db` ručně (riziko sankcí)



**Ruční postup zálohování



Ruční uložení kanálů :


1. Vstupte do nabídky uzlu Lightning (tři tečky "⋮" vedle "+ Otevřít kanál")


2. Stáhněte si soubor zálohy kanálu


3. Export nového SCB po každé úpravě kanálu


4. Bezpečné uložení SCB (šifrované médium, kopie mimo pracoviště)



**Umbrel** automatický zálohovací systém



Umbrel je vybaven důmyslným automatickým zálohovacím systémem, který zajišťuje :



*Ochrana údajů:*




- Šifrování na straně klienta před přenosem
- Odesílání přes síť Tor
- Údaje doplněné náhodným vyplněním
- Šifrovací klíč jedinečný pro vaše zařízení



*Zvýšené zabezpečení:*




- Okamžité zálohování při změně stavu
- Zálohování "návnady" v náhodných intervalech
- Skrytí změn velikosti zálohy
- Ochrana proti časové analýze



*Proces obnovy:*




- Identifikátor a klíč odvozený od vašeho deštníku seed
- Kompletní obnova je možná pouze pomocí věty Mnemonic
- Automatické obnovení nejnovějších záloh
- Obnovení nastavení a dat kanálu



### Obnova po havárii



Pokud dojde ke ztrátě uzlu (selhání hardwaru, poškození karty SD) :




- Opětovná instalace deštníku
- Zadejte do aplikace Lightning 24 slov seed
- Import souboru SCB během obnovy



Společnost LND bude kontaktovat všechny partnery vašich starých kanálů, aby je uzavřela a získala zpět váš podíl na finančních prostředcích společnosti On-Chain. Kanály budou trvale uzavřeny (v případě potřeby budou znovu otevřeny).



### Dostupnost a ochrana proti podvodům



V ideálním případě nechávejte uzel online co nejčastěji. V případě delší nepřítomnosti:




- Zlomyslný partner by se mohl pokusit vysílat starý stav kanálu
- Blesk stanoví "lhůtu pro protest" (přibližně 2 týdny u LND)
- Pokud se chystáte na delší dobu odjet, nastavte si službu Watchtower



**Konfigurace Watchtower:**




- V rozšířeném nastavení LND přidejte adresu URL důvěryhodného serveru Watchtower
- Můžete použít veřejnou službu nebo si nainstalovat vlastní Watchtower




Chcete-li se dozvědět více o konfiguraci a používání strážních věží, doporučujeme vám podívat se na náš specializovaný návod :



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Další osvědčené postupy





- Aktualizace softwaru:** Udržujte Umbrel a LND v aktuálním stavu (opravy zabezpečení)
- Hardwarová ochrana:** Použijte stabilní systém (Raspberry Pi s SSD, mini-PC) a UPS
- Zabezpečení sítě:** Ponechte výchozí konfiguraci Toru, změňte heslo správce Umbrel (výchozí: "moneyprintergobrrr")
- Šifrování:** Pokud je to možné, zapněte šifrování disku



## 6. Další nástroje



Aplikace Lightning Node od společnosti Umbrel poskytuje základní funkce pro správu kanálů, ale nástroje třetích stran nabízejí pokročilé funkce.



### ThunderHub



Interface moderní webový systém správy uzlů Lightning, který lze nainstalovat prostřednictvím obchodu s aplikacemi Umbrel.



**Vlastnosti:**




- Vizualizace kanálů v reálném čase (kapacity, zůstatky)
- Integrované nástroje pro vyvažování
- Podpora vícecestného účtování (MPP)
- Generování kódu QR LNURL
- Správa transakcí On-Chain



ThunderHub je ideální pro monitorování aktivního směrovacího uzlu a provádění jednoduchého vyvažování.



### Ride The Lightning (RTL)



Web Interface je kompatibilní s několika implementacemi Lightning (LND, Core Lightning, Eclair).



**Zajímavé informace:**




- Správa více uzlů
- Kontextově citlivé ovládací panely
- Podpora pro výměnu ponorek (Lightning Loop)
- dvoufaktorové ověřování
- Export/import záloh kanálů



RTL je kompletní "švýcarský armádní nůž" pro správu uzlu Lightning s odbornějším přístupem.



### Další užitečné nástroje





- Lightning Shell** : Příkazový řádek (lncli) přes prohlížeč
- BTC RPC Explorer a Mempool** : Monitorování Blockchain
- LNmetrics & Torq**: Analýza výkonu směrování
- Amboss a 1ML**: "Sociální" správa vašeho uzlu (aliasy, kontakty, analýza sítě)



Tyto nástroje lze nainstalovat několika kliknutími prostřednictvím obchodu Umbrel App Store bez složité konfigurace.



**Další zdroje nástrojů:**




- [ThunderHub.io - Funkce](https://thunderhub.io) - Přehled funkcí ThunderHubu
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - Dokumentace RTL
- [David Kaspar - Rebalance přes ThunderHub](https://blog.davidkaspar.com) - Praktický průvodce rebalancováním
- [Průvodce "Správa uzlů Lightning"](https://github.com/openoms/lightning-node-management) - Pokročilá dokumentace pro uživatele napájení



## Závěr



Provozování vlastního uzlu LND na platformě Umbrel je důležitým krokem k finanční suverenitě. Vyžaduje sice větší technické zapojení než depozitní řešení, ale výhody z hlediska kontroly, důvěrnosti a aktivní účasti na Lightning Network jsou značné.



Podle tohoto návodu byste nyní měli být schopni nainstalovat LND, otevřít kanály, spravovat likviditu a vzdáleně přistupovat k uzlu. Neváhejte postupně prozkoumat pokročilé funkce a další nástroje, jak se budete s ekosystémem lépe seznamovat.



Nezapomeňte, že bezpečnost vašich prostředků závisí na vašich bezpečnostních opatřeních a postupech. Než se rozhodnete pro velké částky, věnujte čas porozumění všem aspektům.