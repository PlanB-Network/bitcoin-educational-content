---
name: Umbrel Nostr
description: Konfigurace a používání aplikací Nostr v systému Umbrel
---

![cover](assets/cover.webp)



## Předpoklady: Instalace deštníku



Umbrel je platforma s otevřeným zdrojovým kódem, která umožňuje snadno hostovat aplikace Bitcoin a další služby na vlastním serveru. Jedná se o řešení typu "vše v jednom", které výrazně zjednodušuje vlastní hostování uzlů Bitcoin a decentralizovaných aplikací.



Ujistěte se, že jste nainstalovali Umbrel podle našeho průvodce instalací:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Úvod do Nostr



**Nostr** je otevřený decentralizovaný síťový protokol určený pro sociální sítě. Jeho název je zkratkou _"Notes and Other Stuff Transmitted by Relays"_. Umožňuje komukoli publikovat zprávy (poznámky), spravované jako události JSON, a šířit je prostřednictvím relay serverů namísto centralizované platformy. Každý uživatel vlastní dvojici kryptografických klíčů (soukromý/veřejný), které slouží jako identifikátor: veřejný klíč (npub) identifikuje uživatele a soukromý klíč (nsec) umožňuje podepisování zpráv. Díky této distribuované architektuře nabízí **Nostr odolnost vůči cenzuře** a velkou flexibilitu: můžete používat několik klientů a připojit se k libovolnému počtu relayů, aniž byste byli závislí na jediném serveru.



Stručně řečeno, Nostr je decentralizovaný komunikační protokol, ve kterém **klienti** (uživatelské aplikace) odesílají a přijímají události prostřednictvím **relayerů** (serverů). Tento protokol je od roku 2023 oblíbený zejména u komunity Bitcoin, a to díky hodnotám decentralizace a suverenity dat.



**Poznámka:** Chcete-li používat službu Nostr, potřebujete svůj soukromý klíč (vygenerovaný klientem Nostr nebo pomocí specializovaného rozšíření). **Nikdy nesdílejte svůj soukromý klíč**, protože by to komukoli umožnilo vydávat se za vás. Uchovávejte jej na bezpečném místě a používejte nástroje pro bezpečnou správu klíčů (viz Tip níže).



## Aplikace deštníku pro Nostr



Společnost Umbrel nabízí ekosystém integrovaných aplikací, které umožňují plně využívat výhody Nostr na vašem osobním uzlu. Podrobně si popíšeme používání hlavních aplikací souvisejících s Nostrem: **Nostr Relay**, **noStrudel**, **Snort** a **Nostr Wallet Connect**. Každá z nich splňuje specifickou potřebu: _Nostr Relay_ je **soukromý relay server**, _noStrudel_ a _Snort_ jsou **klienti Nostr** (rozhraní pro čtení/publikování poznámek), zatímco _Nostr Wallet Connect_ je nástroj pro propojení vašeho **Lightning portfolia** s Nostr.



### Nostr Relay - Vaše soukromé relé na Umbrelu



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** je oficiální aplikace společnosti Umbrel pro provozování **vlastního relé Nostr** na vašem uzlu. Hlavním cílem je mít **soukromé** a spolehlivé relé, které **zálohuje veškerou vaši aktivitu Nostr** v reálném čase. Jinými slovy, používáním tohoto osobního relé vedle veřejných relé si zajistíte, že všechny vaše poznámky, zprávy a reakce budou zkopírovány domů, v bezpečí před cenzurou nebo ztrátou dat.



**Instalace:** Z obchodu s aplikacemi Umbrel (kategorie _Social_) nainstalujte _Nostr Relay_. Po spuštění aplikace poběží na pozadí (služba docker).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Prostřednictvím aplikace Umbrel se zobrazí její web Interface: obsahuje základní informace a především adresu URL vašeho relé (vpravo nahoře), kterou je třeba zkopírovat pro další použití. K dispozici je také synchronizační tlačítko (ikona zeměkoule).



**Chcete-li využít výhod relé Umbrel:**



**Přidejte relé do klienta Nostr:** Do své klientské aplikace (např. Damus v iOS, Amethyst v Androidu, Snort nebo noStrudel v Umbrelu atd.) přidejte adresu URL svého soukromého relé, kterou jste zkopírovali dříve. Ve výchozím nastavení naslouchá relé Umbrel na portu **4848**. Pokud k němu přistupujete v místní síti, získáte adresu URL, jako např: `ws://umbrel.local:4848` (nebo použijte místní IP adresu serveru Umbrel).



Pokud používáte Tailscale (viz níže), můžete dokonce použít alias MagicDNS DNS (obvykle `umbrel` nebo automaticky generovaný název) a přistupovat k němu odkudkoli, vždy na portu 4848.



Pokud dáváte přednost Toru, získejte .onion Address od Umbrelu a používejte jej s portem 4848 prostřednictvím prohlížeče nebo klienta kompatibilního s Tor (viz část Tor)



Po přidání adresy URL do konfigurace relé klienta Nostr se k tomuto relé připojte. V klientovi byste měli vidět, že je relé Umbrel připojeno (obvykle je označeno tečkou Green nebo podobně).



**Synchronizace historie (volitelné)**: V Interface na webu _Nostr Relay_ na Umbrel klikněte na ikonu **globe** 🌐 (v horní části stránky). Tato akce donutí relé Umbrel připojit se k ostatním relé (nakonfigurovaným v klientovi) a **importovat staré veřejné** aktivity. To znamená, že minulé poznámky, které jste publikovali nebo četli prostřednictvím veřejných relay, budou staženy a uloženy také na vašem soukromém relay. Vyčkejte prosím, než dojde k synchronizaci.



**Používejte Nostr jako obvykle:** Od nynějška budou všechny nové aktivity (zveřejněné poznámky, reakce, zašifrované soukromé zprávy atd.), které provedete na Nostru, přeposílány jako obvykle na veřejná relé **a paralelně na vaše relé Umbrel**. Pokud je váš klient Nostr správně nakonfigurován, bude každou událost odesílat na všechna relé (včetně vašeho). Vaše soukromé relé bude fungovat jako záloha v reálném čase. I v případě dočasného odpojení budou vaši zákazníci moci díky tomuto relé později znovu synchronizovat chybějící data. to vám dává úplnou kontrolu nad vašimi daty Nostr



V pozadí je _Nostr Relay_ společnosti Umbrel založen na open-source projektu **nostr-rs-relay** (implementace protokolu Rust). Podporuje celý protokol Nostr a řadu standardních NIP (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33 atd.), což zaručuje maximální kompatibilitu se zákazníky.



### noStrudel - Klient Nostr pro průzkumníky



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** je webový klient Nostr orientovaný na výkonné uživatele, který je ideální pro podrobné pochopení a prozkoumání sítě Nostr. Je to jakési pískoviště pro kontrolu událostí a relayů a pro experimentování s pokročilými funkcemi protokolu. Interface je v angličtině a je poměrně technický, takže je ideální pro zkušené uživatele, které zajímá vnitřní fungování systému Nostr.



**Instalace:** Nainstalujte _noStrudel_ z obchodu s aplikacemi Umbrel (kategorie _Social_). Po spuštění k němu můžete přistupovat prostřednictvím prohlížeče na adrese Address vašeho Umbrelu (např. `http://umbrel.local` nebo prostřednictvím jeho .onion/Tailscale, viz část Externí přístup).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Konfigurace relé:** Po otevření aplikace noStrudel se v pravém horním rohu zobrazí tlačítko "Nastavení relé". Kliknutím na něj nakonfigurujete relé.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Na tuto stránku vložte adresu URL svého relé Umbrel, kterou jste zkopírovali dříve. Můžete také přidat další relé, která aplikace ve výchozím nastavení navrhuje. Jakmile nakonfigurujete relé, klikněte vlevo dole na "Přihlásit se" a pokračujte.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Připojení:** noStrudel nabízí několik možností připojení. V našem případě zvolíme "Private Key" a vložíme dříve vygenerovaný soukromý klíč Nostr. Pokud klíč ještě nemáte, můžete si nainstalovat rozšíření [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj), které vám umožní vytvořit a/nebo uložit klíče Nostr a tím bezpečněji komunikovat s různými aplikacemi Nostr.



![Interface principale de noStrudel](assets/fr/07.webp)



Po připojení můžete pomocí aplikace noStrudel sdílet své poznámky prostřednictvím služby Nostr. Interface vám umožní přístup k :





- Kompletní ovládací panel Nostr s časovou osou poznámek, oznámeními, zprávami a vyhledáváním v profilu
- Správa relé a stav připojení
- Pokročilé nástroje pro zkoumání událostí a jejich obsahu JSON
- Možnosti konfigurace filtrů časové osy a kódů PIN



**Tip:** Na _noStrudel_ můžete nastavit _časové filtry_ nebo testovat různé _NIP (Nostr Implementation Possibilities)_. Zkontrolujte například podporu NIP-05 (decentralizované identifikátory) nebo novějších funkcí. Díky tomu je _noStrudel_ vynikajícím nástrojem pro experimentování v kontrolovaném prostředí.



### Snort - Moderní zákazník Nostr na Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** je další webový klient Nostr dostupný na platformě Umbrel, který nabízí moderní, rychlý a přehledný **Interface** pro interakci s decentralizovanou sociální sítí. Na rozdíl od noStrudel, který se zaměřuje na zkušené uživatele, se _Snort_ snaží o jednoduché používání bez obětování funkčnosti. Je vytvořen v Reactu a nabízí přehledné UX připomínající klasické sociální sítě, takže je vhodný pro každodenní používání.



**Instalace:** Nainstalujte si aplikaci _Snort_ z obchodu Umbrel App Store (kategorie _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Po otevření aplikace Snort se v levém dolním rohu zobrazí tlačítko "Zaregistrovat".



![Options de connexion dans Snort](assets/fr/10.webp)



Můžete se zaregistrovat nebo se připojit k existujícímu účtu (což v tomto tutoriálu uděláme).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort nabízí několik metod připojení. Můžete použít dříve nainstalované rozšíření Nostr Connect nebo jiné dostupné metody. Po připojení budete moci aplikaci plně využívat.



Model Interface od společnosti _Snort_ nabízí :





- Zobrazení **Příspěvky/Konverzace/Globální** pro navigaci mezi poznámkami, vlákny diskuzí nebo globálním kanálem
- Karty pro **oznámení**, **zprávy** (DM), **vyhledávání**, **profil** atd.
- Tlačítko **+** nebo _Write_ pro publikování nové poznámky
- Správa **odběrů (následujících)** a **seznamů**
- Nabídka správy relé pro přidávání/odebírání relé a sledování jejich dostupnosti



**Doporučená konfigurace relé:** Chcete-li přidat relé Umbrel, přejděte do Nastavení - Relé. Zadejte adresu URL svého relé (`ws://umbrel:4848` nebo jinou adresu URL v závislosti na konfiguraci) do seznamu relé Snortu. Tímto způsobem bude Snort kromě veřejných relay zveřejňovat vaše poznámky i na vašem soukromém relay.



### Nostr Wallet Connect - Propojte svůj blesk Wallet s Nostrem



**Nostr Wallet Connect (NWC)** je aplikace, která **připojuje váš uzel Umbrel (Lightning)** ke kompatibilním aplikacím Nostr a umožňuje provádět platby Lightning (například posílání _zaps_, mikroplateb za "lajkování" obsahu). V tomto návodu se podíváme na to, jak připojit noStrudel k uzlu Lightning a provádět platby přímo z Interface.



**Instalace a konfigurace:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Nainstalujte si _Nostr Wallet Connect_ z obchodu Alby na Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



V aplikaci noStrudel klikněte na svůj profil v pravém horním rohu a poté na tlačítko "spravovat".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Klikněte na "Lightning" a poté na "connect Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Z dostupných možností připojení vyberte možnost "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Kliknutím na "Připojit" budete automaticky přesměrováni do relace Umbrel Nostr Wallet Connect.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Na stránce Nostr Wallet Connect můžete :




   - Definujte svůj maximální rozpočet
   - Ověřování oprávnění
   - Nastavení doby vypršení platnosti připojení


Kliknutím na tlačítko "připojit" dokončete.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Jste přesměrováni na noStrudel s potvrzující zprávou: nyní můžete z uzlu Wallet/LND zapnout celý svět!



Díky NWC začínají vaše **placení blesků přes Nostr** (zapsy na odměňování příspěvků, platby _Value for Value_ atd.) ve **vašem vlastním uzlu**. Už nemusíte své transakce směrovat přes externí služby nebo pokaždé skenovat QR z telefonu. Uživatelský zážitek se výrazně zlepší, přičemž zůstává _nezávazkový_ a šetrný k soukromí.



Pokud chcete vědět, jak nastavit vlastní uzel Lightning v Umbrelu, doporučuji vám podívat se na tento další komplexní návod:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Pokročilá konfigurace a zabezpečení



Společné používání aplikací Umbrel a Nostr na pokročilé úrovni vyžaduje zvláštní pozornost věnovanou **bezpečnosti** a **konektivitě**. Zde je několik tipů, jak chránit konfiguraci a optimálně k ní přistupovat, ať jste kdekoli.



### Zabezpečený přístup zvenčí: Tor a Tailscale



Z bezpečnostních důvodů je Umbrel ve výchozím nastavení přístupný pouze v místní síti (a přes Tor). Chcete-li s Nostrem komunikovat mimo domov, máte dvě preferovaná řešení: **Tor** (anonymní přístup přes síť onion) a **Tailscale** (privátní síť VPN).





- **Přístup přes Tor:** Umbrel automaticky konfiguruje **službu Tor (.onion)** pro svůj web a aplikace Interface. To znamená, že můžete přistupovat ke Interface Umbrel (včetně *noStrudel* nebo *Snort*) odkudkoli pomocí prohlížeče Tor, aniž byste odhalili svou veřejnou IP adresu. *Tor slouží k přístupu ke službám Umbrel mimo vaši místní síť, aniž by vaše zařízení bylo vystaveno internetu ([Nastavení Toru v systému - Návody - Komunita Umbrel](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww)).* Chcete-li tuto možnost použít, přejděte do nastavení Umbrel a načtěte adresu URL .onion vašeho Umbrelu (nebo naskenujte uvedený QR kód). V prohlížeči Tor přistupte k této .onion adrese Address


**Nostr relay přes Tor:** Pokud chcete, aby váš Nostr relay byl pro vaše zákazníky (nebo autorizované přátele) dostupný přes Tor, je to možné. Společnost Umbrel neposkytuje relay .onion Address přímo, ale protože běží na portu 4848, můžete buď :





    - Použijte .onion Address UI Umbrel a nakonfigurujte klienta tak, aby se připojoval prostřednictvím tohoto Interface (nepraktické pro WebSocket),





- Nebo vystavte port 4848 jako samostatnou službu cibule. To vyžaduje hrátky s konfigurací Toru v Umbrelu (vyhrazeno pro pokročilé uživatele, kteří umí pracovat s SSH). Případně zvažte **Tor tunel** na jiném serveru, který přesměruje na Umbrel: pro osobní použití je však nejjednodušší použít Tailscale.





- **Přístup přes Tailscale:** [Tailscale](https://tailscale.com/) je síťové řešení VPN, které vytváří virtuální privátní síť mezi vašimi zařízeními a společností Umbrel. Výhoda: funguje to, jako byste byli v síti LAN, ale přes internet, šifrovaně a bez složité konfigurace. **Tailscale přiřadí vašemu zařízení Umbrel pevnou IP adresu a název soukromé domény bez ohledu na jeho umístění v síti** ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard)). V praxi to znamená, že jakmile si nainstalujete Tailscale na Umbrel (z obchodu Umbrel App Store, kategorie *Networking*) **a** na svá zařízení (mobilní telefon, počítač...), budete se moci na Umbrel připojit prostřednictvím Address jako `100.x.y.z


pro Nostr_ je Tailscale velmi užitečný: váš mobilní telefon, pokud má Tailscale aktivní, se bude moci připojit k `ws://umbrel:4848` (díky MagicDNS) nebo přímo k IP adrese Tailscale a portu 4848 a používat relay. Klienti jako Damus nebo Amethyst uvidí váš Umbrel, jako by byl ve stejné místní síti. **Tip:** Povolte v Tailscale volbu **MagicDNS**, abyste místo zapamatování IP používali hostitelské jméno `umbrel`. Tím zajistíte bezproblémové připojení k relé, i když jste na cestách ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Tailscale navíc umožňuje přistupovat k Interface Umbrel (a tedy i k webovým klientům _noStrudel/Snort_) prostřednictvím jednoduchého prohlížeče, a to pomocí privátní IP adresy nebo přiděleného názvu domény. Prohlížeč Tor není potřeba a rychlost přenosu dat je obecně vyšší než přes síť Tor.




**Poznámka: Tor a Tailscale se vzájemně nevylučují. Tor můžete mít aktivní pro anonymní přístup nebo specifické služby a Tailscale můžete používat každý den kvůli jeho jednoduchosti. V obou případech nemusíte otevírat port na směrovači, což posiluje bezpečnost.**



### Zabezpečení relé Nostr (doporučené postupy)



Pokud na serveru Umbrel hostujete relay Nostr, zejména v pokročilém kontextu, nezapomeňte použít několik osvědčených postupů:





- Soukromý nebo omezený relay: Ve výchozím nastavení je váš relay Umbrel soukromý (není veřejně oznámený), a pokud k němu přistupujete pouze přes Tailscale nebo vaši síť LAN, zůstane pro cizí osoby nedostupný. **Zachovejte důvěrnost odkazu** Nevysílejte jej ve veřejných sítích Nostr, pokud nechcete dobrovolně hostovat další uživatele, což je úplně jiná otázka (moderování, šířka pásma atd.). Pro osobní použití doporučujeme omezit přístup na sebe a případně na několik důvěryhodných přátel a rodinných příslušníků.





- **Whitelist / Auth**: Implementace nostr-rs-relay podporuje mechanismus ověřování **NIP-42** a také *whitelisty* veřejných klíčů. Povolením těchto voleb můžete omezit relay tak, aby **přijímal pouze události podepsané určitými klíči (vašimi)** nebo aby se klienti museli pro publikování autentizovat. *Nastavení vyžaduje úpravu konfiguračního souboru `config.toml` relay v Umbrelu (přes SSH v kontejneru Docker).* Je to pokročilá manipulace, ale můžete například vypsat seznam povolených reklam (`pubkey_whitelist`). Tímto způsobem, i když někdo objeví váš relay, nebude tam moci nic publikovat, pokud nebude na seznamu.





- **Aktualizace a údržba:** Udržujte svůj Umbrel a aplikaci *Nostr Relay* aktuální. Aktualizace mohou zahrnovat vylepšení výkonu (např. lepší zpracování spamu) a opravy zabezpečení. V aplikaci Umbrel pravidelně kontrolujte, zda v App Store nejsou k dispozici aktualizace aplikace *Nostr Relay*, a v případě potřeby je použijte.





- **Sledování a omezení:** Sledujte, jak je relé používáno. Pokud jej otevřete ostatním, sledujte zatížení (CPU/RAM úložiště) vašeho Umbrelu, protože relé může rychle nahromadit velké množství dat. nostr-rs-relay nabízí konfigurovatelné **limitní hodnoty rychlosti a úložiště** (`limitní hodnoty` v konfiguraci, např. počet událostí za sekundu, maximální velikost události, čištění starých událostí...). Pro soukromé použití na ně pravděpodobně nebudete muset sahat, ale vězte, že tyto parametry existují, pokud je budete potřebovat ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- **Zabezpečení klíčů Nostr:** Tento bod již byl zmíněn, ale je velmi důležitý: nikdy nezadávejte své soukromé klíče Nostr do služby Interface, které plně nedůvěřujete. Místo toho používejte k podepisování citlivých akcí rozšíření prohlížeče nebo externí zařízení (například *podpisovače* Nostr na samostatných telefonech). V systému Umbrel mohou vaši weboví klienti jako *Snort* a *noStrudel* pracovat bez znalosti vašeho tajného klíče prostřednictvím NIP-07. Využijte této příležitosti a spojte pohodlí a bezpečnost.




Pokud budete postupovat podle těchto tipů, bude vaše integrace uzlu Umbrel s Nostrem výkonná **a** bezpečná. Budete mít kompletní prostředí: uzel Bitcoin pro platby Lightning, soukromé relé Nostr pro suverenitu dat a vysoce výkonné webové klienty Nostr pro navigaci v této nové decentralizované sociální síti. Užijte si objevování Nostr s Umbrelem!