---
name: ArkadeOS
description: Kompletní průvodce portfoliem Arkade a protokolem Ark
---

![cover](assets/cover.webp)



Síť Bitcoin se potýká s velkou výzvou: škálovatelností. Hlavní vrstva (vrstva 1) sice nabízí bezkonkurenční zabezpečení a decentralizaci, ale dokáže zpracovat pouze omezený počet transakcí za sekundu. Jako slibné řešení druhé vrstvy (vrstva 2) se ukázala síť Lightning Network, která umožňuje rychlé a levné platby. Lightning však přináší svá vlastní omezení: správu kanálů, potřebu příchozí likvidity a technickou složitost, která může odradit nové uživatele.



To je pozadí **Ark**, nového protokolu 2. vrstvy, který má nabídnout zjednodušené uživatelské prostředí bez ztráty suverenity. **ArkadeOS** (neboli Arkade) je první významnou implementací tohoto protokolu, která nabízí portfolio Bitcoin nové generace.



Tento návod vás provede světem hry Arkade. Prozkoumáme, jak funguje protokol Arkade, jak nainstalovat a nakonfigurovat Arkade wallet a jak jej používat k okamžitému a důvěrnému odesílání a přijímání bitcoinů bez obvyklých třecích ploch Lightning Network.



## Porozumění protokolu Archa



Než se ponoříte do používání systému Arkade, je nezbytné pochopit klíčové koncepty protokolu Arkade, který jej pohání. Arkade není samostatný blockchain, ale inteligentní koordinační mechanismus nad Bitcoin.



### Koncept VTXO


Srdcem systému Ark je **VTXO** (Virtual UTXO). VTXO je UTXO, který ještě nebyl zveřejněn v blockchainu Bitcoin: existuje mimo hlavní řetězec (off-chain), ale je podpořen transakcemi předem podepsanými v blockchainu.



Na rozdíl od zůstatku na centralizované burze vám VTXO skutečně patří. Jste držitelem kryptografického důkazu, který vám umožňuje kdykoli si nárokovat odpovídající skutečné bitcoiny v blockchainu, a to i v případě, že server Archa zmizí. VTXO umožňují okamžitý převod hodnoty mezi uživateli bez čekání na potvrzení bloku.



### Úloha ASP (Ark Service Provider)


Protokol Ark pracuje na modelu klient-server. Server se nazývá **ASP** (Ark Service Provider). ASP hraje roli průvodce:




- Zajišťuje potřebnou likviditu sítě.
- Koordinuje transakce mezi uživateli.
- Organizuje vypořádací "kola" v blockchainu.



Je důležité si uvědomit, že ASP je **nezávislá**. Nikdy nedrží vaše soukromé klíče ani nemůže ukrást vaše finanční prostředky. Její role je čistě technická a logistická. Pokud ASP cenzuruje vaše transakce nebo dojde k jejímu výpadku, můžete své prostředky vždy získat zpět prostřednictvím jednostranného výstupního postupu.



### Okruhy a soukromí


Transakce na platformě Ark jsou dokončovány v dávkách zvaných **Rounds**. ASP pravidelně (např. každých několik sekund) shromažďuje všechny čekající transakce a ukotvuje je v blockchainu Bitcoin v jedné optimalizované transakci.


Tento mechanismus má dvě hlavní výhody:




- Škálovatelnost**: Jediná transakce on-chain může ověřit tisíce plateb off-chain, což výrazně snižuje náklady uživatelů.
- Důvěrnost**: V každém kole funguje jako **CoinJoin**. Prostředky od všech účastníků se smíchají do společného fondu a poté se přerozdělí ve formě nových VTXO. Tím se přeruší vazba mezi odesílatelem a příjemcem, takže pro vnějšího pozorovatele je velmi obtížné, ne-li nemožné, platby vysledovat.



## Prezentace systému ArkadeOS



ArkadeOS je konkrétní aplikace, která zpřístupňuje protokol Ark široké veřejnosti. Vyvinula ji společnost Ark Labs a jedná se o kompletní ekosystém, který se skládá z portfolia (Wallet), serveru (Operator) a vývojářských nástrojů.



Pro koncového uživatele má Arkade podobu elegantního, intuitivního webu wallet (PWA - Progressive Web App). Za známým rozhraním skrývá kryptografickou složitost VTXO a roundů. S Arkade máte k dispozici adresu pro příjem, tlačítko pro odeslání a historii transakcí, stejně jako u klasického wallet, ale se silou bezprostřednosti a důvěrnosti Arkade.



## Instalace a konfigurace



Vzhledem k tomu, že Arkade je progresivní webová aplikace, je její instalace mimořádně snadná a nemusí nutně zahrnovat tradiční aplikační úložiště.



### Přístup a instalace


K Arkade můžete přistupovat přímo z jakéhokoli moderního webového prohlížeče (Chrome, Safari, Brave) na počítači nebo mobilu.





- Navštivte oficiální webové stránky aplikace: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Uvítá vás řada úvodních obrazovek, které vás seznámí s klíčovými koncepty Arkade: nový ekosystém pro Bitcoin, důležitost self-custody a výhody dávkových transakcí.



![arkade onboarding](assets/fr/02.webp)





- V systému Android (Chrome/Brave)** : Stiskněte nabídku prohlížeče (tři tečky) a vyberte "Instalovat aplikaci" nebo "Přidat na domovskou obrazovku".
- V systému iOS (Safari)**: Stiskněte tlačítko sdílení (čtverec se šipkou nahoru) a vyberte možnost "Na domovské obrazovce".



Po instalaci se aplikace Arkade spouští jako nativní aplikace, přes celou obrazovku a bez adresního řádku.



### Vytvoření portfolia


Při prvním spuštění budete vyzváni ke konfiguraci portfolia.





- Klikněte na **"Vytvořit nový Wallet"**.



![create wallet](assets/fr/03.webp)





- Model wallet je vytvořen okamžitě. Na rozdíl od tradičních peněženek Bitcoin nepoužívá **Arkade frázi pro obnovu o 12 nebo 24 slovech**. Místo toho Arkade automaticky vygeneruje **privátní klíč** ve formátu Nostr (nsec), který bude použit k zálohování a obnově vašeho wallet. Nezapomeňte tento klíč ihned uložit (viz další část).





- Zobrazí se obrazovka "Your new wallet is live!", která potvrzuje, že je váš wallet připraven k použití. Klepnutím na **"GO TO WALLET "** se dostanete do hlavního rozhraní.



Po vstupu do wallet se dostanete do hlavního rozhraní aplikace Arkade. Zde najdete svůj zůstatek, tlačítka pro odesílání a přijímání peněz a záložku "Aplikace", která umožňuje přístup k integrovaným aplikacím, jako jsou Boltz (Lightning exchange), LendaSat a LendaSwap (úvěrové služby) a Fuji Money (syntetická aktiva).



![wallet interface](assets/fr/04.webp)



### Připojení k ASP


Ve výchozím nastavení je portfolio automaticky nakonfigurováno tak, aby se připojilo k oficiálnímu ASP společnosti Arkade Labs. K jakému serveru jste připojeni, můžete zkontrolovat v nabídce **Nastavení** > **O serveru**, kde uvidíte adresu serveru (v současné době `https://arkade.computer`).



V současné verzi Arkade (Beta) není možné ručně upravovat server ASP. Aplikace se automaticky připojuje k oficiálnímu serveru ASP společnosti Arkade Labs. V budoucnu si uživatelé možná budou moci vybrat mezi různými ASP podle svých preferencí, ale tato funkce zatím není k dispozici.



### Zálohování soukromého klíče


**Arkade používá soukromý klíč ve formátu Nostr (nsec) jako metodu zálohování a obnovy. Chcete-li zálohovat svůj soukromý klíč :





- Na hlavní obrazovce přejděte na položku **Nastavení**.
- Vyberte možnost **"Zálohování a soukromí "**.
- Zobrazí se váš **soukromý klíč** ve formátu `nsec...`. Tento dlouhý řetězec znaků je vaším jediným prostředkem k obnovení wallet.
- Stisknutím tlačítka **"KOPÍROVAT NSEC NA KLIPBOARD "** zkopírujete svůj soukromý klíč.
- Tento klíč uchovávejte na bezpečném místě**: napište si ho na papír, uložte do zabezpečeného správce hesel nebo použijte jiný vhodný způsob zálohování.
- Arkade také nabízí možnost **"Povolit zálohování Nostr "**. Tato funkce využívá protokol Nostr (decentralizovaná síť) k automatickému zálohování určitých dat z vašeho wallet v zašifrované podobě na relé Nostr. To usnadňuje synchronizaci mezi více zařízeními a nabízí jednodušší obnovu stavu vašeho zařízení wallet.



**Důležité**: Nostr zálohování je pouze **komfortní** funkce. Nenahrazují zálohu klíče nsec. Zálohy Nostr nezaručují trvalé uložení dat. Váš soukromý klíč nsec zůstává jediným zaručeným prostředkem pro obnovu vašich prostředků.



![backup private key](assets/fr/05.webp)




## Používání aplikace Arkade



Jakmile si nastavíte wallet, můžete se pustit do zkoumání možností aplikace Arkade. Rozhraní je navrženo tak, aby bezproblémově sjednocovalo různé typy plateb Bitcoin (On-chain, Lightning, Ark).



### Přijímání finančních prostředků



Chcete-li financovat své portfolio, stiskněte tlačítko **"Přijmout "**. Arkade nabízí tři způsoby příjmu:





- Platba archy**: Pokud odesílatel také používá Arkade, sdílejte svou adresu Arkade pro okamžitý, důvěrný a prakticky bezplatný převod.
- Kauce v řetězci (stravování)**: Pomocí adresy Bitcoin (`bc1p...`) můžete přijímat z klasického wallet nebo z burzy. Počkejte na potvrzení (~10 min), než se prostředky převedou na VTXO.
- Blesková výměna**: Vygenerujte fakturu Lightning a zaplaťte ji z externího wallet Lightning. Prostředky dorazí okamžitě prostřednictvím automatického swapu.



![receive amount](assets/fr/06.webp)



Na obrazovce účtenky se zobrazí všechny dostupné možnosti: (BIP21) a Blesková faktura. Pro platby Lightning nechte aplikaci během transakce otevřenou.



![receive confirmation](assets/fr/07.webp)



### Zasílání finančních prostředků



Chcete-li odeslat peníze, stiskněte tlačítko **"Odeslat "** a vložte adresu příjemce nebo naskenujte kód QR. Arkade automaticky rozpozná typ požadované platby:





- Platba za arch**: Na adresu Archy je převod okamžitý, soukromý a prakticky zdarma (0 SATS poplatků). Příjemce nemusí být online.
- Blesková** platba: Arkade automaticky provede výměnu.: Naskenujte fakturu Lightning (`lnbc...`) a Arkade automaticky provede výměnu. ASP zaplatí fakturu za vás a odečte z vašeho zůstatku v Arkade.
- Platba v řetězci**: Vůči klasické adrese Bitcoin (`bc1q...` nebo `bc1p...`) iniciuje Arkade "Společný výstup", který bude zařazen do dalšího kola on-chain.



Zkontrolujte údaje na obrazovce "Podepsat transakci" a poté potvrďte tlačítkem **"TAP TO SIGN "**.



![send payment](assets/fr/08.webp)



**Aktuální omezení (Beta)**: VTXO vytvořené před méně než 24 hodinami nelze použít pro výstupy on-chain. Pokud narazíte na chybu, vyčkejte, dokud vaše VTXO nebudou "zralé".



**Důvěrnost výstupu on-chain**: Výstupní transakce [Ark na mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Pozorujeme distribuovaný vstup na 4 různé výstupy, podobně jako u CoinJoin. Pro vnějšího pozorovatele není možné určit, které množství patří kterému uživateli.



![transaction ark mempool](assets/fr/11.webp)



## Pokročilé funkce



### Správa vypršení platnosti VTXO


Technickou vlastností protokolu Ark je, že VTXO mají **omezenou životnost**. Toto časové omezení vyplývá z návrhu protokolu. Doba vypršení platnosti je konfigurovatelná každým serverem ASP; na oficiálním ASP společnosti Arkade Labs je tato doba přibližně **4 týdny (≈30 dní)**.



**Toto omezení umožňuje serveru Ark efektivně spravovat likviditu a čistit VTXO od neaktivních uživatelů. Po vypršení platnosti může server Archa technicky požadovat zbývající prostředky ve stromu VTXO.



** Aby byly jednotky VTXO stále aktivní, je třeba je před vypršením jejich platnosti "obnovit". Obnovení spočívá v účasti v novém "kole", kdy jsou vaše VTXO, jejichž platnost se blíží vypršení, vyměněny za nové VTXO s novou plnou dobou platnosti (≈30 dní u Arkade Labs ASP).



Portfolio Arkade tento proces řídí automaticky: aplikace neustále sleduje stav vašich VTXO a automaticky je obnovuje několik dní před vypršením jejich platnosti. Pokud aplikaci otevíráte pravidelně (alespoň jednou týdně), vaše VTXO budou automaticky udržovány aktivní.



**Pokud své portfolio neotevřete déle než 4 týdny, platnost vašich VTXO vyprší. O své prostředky však nepřijdete: zachováte si možnost získat je zpět prostřednictvím **jednostranného výstupu** (viz další část). Tento postup je sice nákladnější a pomalejší, ale zajišťuje, že vaše prostředky zůstanou obnovitelné.



Nutnost pravidelně otevírat aplikaci činí z Arkade **"Hot Wallet"** určený pro každodenní výdaje, nikoliv jako trezor pro dlouhodobé spoření. Chcete-li bitcoiny uchovávat bez jejich dlouhodobého používání, dejte přednost chladnému hardwaru wallet.



**Zkontrolujte stav VTXO**: Stav VTXO můžete sledovat v nabídce **Nastavení** > **Pokročilé**. V části "Další obnovení" se dozvíte, kdy proběhne další automatické obnovení, a v části "Virtuální mince" si můžete prohlédnout podrobný seznam všech svých VTXO s datem vypršení platnosti.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (Jednostranný odchod)



Jednostranné ukončení je **základní kryptografickou zárukou** protokolu Ark, která vám zaručí, že dostanete své prostředky zpět, i když ASP zmizí, cenzuruje vaše transakce nebo odmítne spolupracovat. Technicky vzato jsou vaše VTXO **předem podepsané transakce Bitcoin**, které vlastníte. V naprosto naléhavém případě můžete tyto transakce vysílat do blockchainu Bitcoin a získat tak své prostředky zpět, aniž by vás kdokoli autorizoval.



**Jak to funguje? Proces probíhá ve dvou fázích. Nejdříve **Unrolling**: postupně vysíláte předem podepsané transakce, které tvoří vaše VTXO ve stromu transakcí. Poté následuje **Finalizace**: po vypršení časových zámků (obvykle 24 hodin) si vyzvednete bitcoiny ze standardní adresy.



**Aktuální stav v Arkade**: V betaverzi zatím není k dispozici tlačítko ani jednoduché uživatelské rozhraní pro jednostranný výstup. Tato funkce v současné době vyžaduje použití Arkade SDK a technické znalosti programování v jazyce TypeScript.



**I když postup není dostupný stisknutím tlačítka, kryptografická záruka existuje. Vaše VTXO obsahují předem podepsané transakce, které vám legitimně patří. Právě tato technická záruka dělá z Archy **nezabavitelný** protokol: i v nejhorším případě zůstávají vaše prostředky technicky obnovitelné. V budoucích verzích Arkade bude pravděpodobně přidáno zjednodušené rozhraní.



## Výhody a omezení



Abychom uvedli Arkade do správného kontextu, shrňme její současné silné a slabé stránky.



### Nejdůležitější informace




- Zkušenosti uživatelů (UX)**: Žádná správa kanálů, příchozí kapacita nebo složité zálohování kanálů jako u Lightning. Stačí nainstalovat a používat.
- Ochrana osobních údajů** : Výchozí architektura CoinJoin nabízí mnohem vyšší úroveň anonymity než standardní transakce on-chain nebo Lightning.
- Interoperabilita**: Zaplaťte jakýkoli QR kód Bitcoin (On-chain nebo Lightning) z jediného rozhraní.



### Omezení




- Mladý protokol**: Archa je velmi nová technologie. Mohou se vyskytovat chyby. Doporučuje se nepoužívat Ark k ukládání částek, jejichž ztráta by byla kritická.
- Závislost na ASP**: Přestože systém není závislý na systému ASP, je jeho plynulost závislá na dostupnosti ASP. Pokud je ASP offline, nemůžete již provádět okamžité transakce (pouze vyvést své prostředky on-chain).
- Hot Pouze Wallet** : Nutnost pravidelného otevírání aplikace pro obnovení VTXO není vhodná pro studené úložiště (úložiště Cold).



## Srovnání: Arkade vs Lightning vs Cashu



Abychom lépe pochopili pozici společnosti Arkade, porovnejme ji s dalšími dvěma hlavními řešeními pro škálování.



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** je ideálním kompromisem: jednoduchost a důvěrnost Cashu, ale suverenita (bez vazby) Blesku.



## Podpora a pomoc



Pokud se při používání aplikace Arkade setkáte s jakýmikoli problémy nebo máte dotazy, nabízí aplikace několik možností podpory:





- Přejděte na **Nastavení** > **Podpora**.
- Najdete zde několik možností:
  - Zákaznická podpora**: Získejte pomoc se svým portfoliem, nahlaste chyby nebo položte dotazy.
  - Zabezpečený chat**: Vaše konverzace jsou zabezpečené a soukromé a mezi jednotlivými relacemi se uchovává jejich historie.
  - Hlášení chyb**: Nahlaste všechny problémy, se kterými se setkáte, včetně kroků k jejich reprodukci.
  - Sledování pokroku**: Sledujte své tikety podpory a konverzace po celou dobu.



![support](assets/fr/10.webp)



Tým Arkade je také aktivní na Telegramu prostřednictvím kanálu @arkade_os, kde poskytuje podporu a možnosti integrace.



## Důležité upozornění: Aplikace v beta verzi



**⚠️ Arkade je v současné době ve veřejné beta verzi na mainnet Bitcoin**. Přestože je aplikace funkční se skutečnými bitcoiny, je důležité přijmout určitá opatření.



### Doporučení pro použití




- Používejte malé množství**: Vyvarujte se ukládání velkých částek na Arkade. Tuto kartu wallet používejte na běžné výdaje a úspory si nechte na chladném hardwaru wallet.
- Možné chyby a omezení**: Jako u každé aplikace, která je v procesu vývoje, se i u Arkade mohou vyskytnout chyby nebo neočekávané chování. Případné problémy nahlaste prostřednictvím integrované podpory.
- Rychlý vývoj** : Aplikace a protokol se neustále zdokonalují. Některé funkce se mohou v budoucích verzích změnit nebo přidat.



### Současná známá omezení




- 24hodinové zpoždění na VTXO** : Nově vytvořené VTXO nelze okamžitě použít pro výstupy on-chain.
- ASP unique**: V aplikaci zatím není možné změnit server ASP.
- Jednostranný technický výstup**: Zjednodušené rozhraní pro jednostranný výstup zatím neexistuje (vyžaduje SDK).



Tým Arkade Labs aktivně pracuje na zmírnění těchto omezení v budoucích verzích.



## Závěr



ArkadeOS představuje zásadní průlom v ekosystému Bitcoin. Implementací protokolu Ark dokazuje, že je možné sladit jednoduchost používání se základními principy Bitcoin: nedůvěřuj, ověřuj.



Ačkoli je Arkade stále v plenkách, nabízí fascinující pohled na to, jak by mohla vypadat budoucnost plateb Bitcoin: okamžité, soukromé a přístupné všem bez technických předpokladů. Je to dokonalý nástroj pro vaše každodenní výdaje, který doplňuje řešení bezpečného spoření (Cold Wallet).



Doporučujeme vám, abyste si Arkade vyzkoušeli v malém množství a objevili tento nový protokol na vlastní kůži. Ekosystém se rychle vyvíjí a Arkade stojí v čele této inovace.



## Zdroje



Další informace najdete v oficiálních zdrojích:





- Webové stránky Arkade**: [arkadeos.com](https://arkadeos.com)
- Dokumentace**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Protokol Ark**: [ark-protocol.org](https://ark-protocol.org)
- Zdrojový kód** : [GitHub Arkade](https://github.com/arkade-os)