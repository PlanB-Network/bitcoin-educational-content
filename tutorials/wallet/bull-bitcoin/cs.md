---
name: Bull Bitcoin Wallet
description: Zjistěte, jak používat Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Tento videonávod od společnosti BTC Sessions vás provede procesem nastavení a používání Bull Bitcoin Wallet!*


Tato příručka vás seznámí s instalací, konfigurací a používáním systému Bull Bitcoin Wallet. Naučíte se odesílat a přijímat finanční prostředky v sítích Bitcoin On-Chain, Liquid a Lightning a také přesouvat Bitcoin mezi nimi. Rozsáhlé funkce wallet z něj dělají výkonný nástroj "vše v jednom" pro správu Bitcoin. Začněme.


## Úvod


Bull Bitcoin Wallet, vyvinutý [Bull Bitcoin](https://www.bullbitcoin.com/), je **samostatný** Bitcoin wallet, což znamená, že máte plnou kontrolu nad svými soukromými klíči, a tedy i nad svými prostředky, aniž byste byli závislí na třetí straně. Tento Wallet s otevřeným zdrojovým kódem a s kořeny ve filozofii Cypherpunk kombinuje jednoduchost, důvěrnost a pokročilé funkce, jako jsou swapy mezi sítěmi a podpora PayJoin. Umožňuje spravovat vaše bitcoiny ve třech sítích: **Bitcoin onchain**, **Liquid** a **Lightning**, přičemž každá z nich je přizpůsobena specifickému použití. Na [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) se můžete podívat na aktuální témata a nadcházející vývoj. Jelikož je projekt 100% open-source a "postaven veřejně", můžete také posílat své návrhy a případné chyby, na které narazíte. Zatímco některé peněženky nyní podporují více sítí, Bull Bitcoin Wallet vyniká hlubokou integrací funkcí ochrany soukromí ve všech těchto sítích, což z něj dělá výkonný nástroj pro správu vašeho Bitcoin ve všech hlavních sítích


## 1️⃣ Předpoklady


Než začnete **Bull Bitcoin Wallet** používat, ujistěte se, že máte následující položky:



- Kompatibilní smartphone**: Zařízení se systémem **iOS** (iPhone nebo iPad) nebo **Android**
- Připojení k internetu
- Zabezpečená zálohovací média**: Napište si **obnovovací frázi** (12 slov) na papír nebo kov a uložte ji na bezpečném místě.
- Základní znalosti**: V tomto návodu jsou vysvětleny jednotlivé kroky pro začátečníky.


## instalace 2️⃣


Aplikaci můžete nainstalovat prostřednictvím:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(pro zařízení iOS)
- [Obchod Google Play](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (pro zařízení se systémem Android)


Uživatelé systému Android mají také alternativní možnosti:



- Stáhněte si APK přímo ze stránky [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) nebo
- Instalace prostřednictvím kompatibilního obchodu Nostr [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Po instalaci aplikace postupujte podle uvítací obrazovky a nakonfigurujte svůj účet.


## 3️⃣ Počáteční konfigurace


Po otevření se zobrazí následující možnosti:



- `Vytvořit nový Wallet`
- `Recover Wallet` a
- `Rozšířené možnosti`


Začněme klepnutím na možnost `Rozšířené možnosti`.


Zde můžeme před vytvořením nebo obnovením souboru wallet nakonfigurovat pokročilá nastavení:


1. Povolte `Tor proxy` pro směrování provozu přes síť Tor.

1. [Aplikace Orbot](https://orbot.app/en/) musí být nainstalována a spuštěna před povolením

2. Tor Proxy se vztahuje pouze na Bitcoin (nikoli Liquid) a může vést ke zpomalení připojení.

2. Nastavení `Vlastní Electrum Server` nebo

3. Upravte nastavení `Recover Bull`. Více se o [Recover Bull](https://recoverbull.com/) dozvíme později.


Po provedení všech volitelných úprav klepněte na tlačítko `Done`. Chcete-li znovu použít stávající Wallet, klepněte na `Obnovit Wallet` a vyplňte 12 slov své obnovovací fráze.


V opačném případě klikněte na možnost `Vytvořit nový Wallet`.


![image](assets/en/01.webp)


## domovská obrazovka 4️⃣


Než se ponoříme hlouběji, podívejme se na úvodní obrazovku, abychom se zorientovali:



- v horní části se nachází nabídka `přehled transakcí` a `nastavení`.
- Položka `Dostupný zůstatek` má možnost soukromí, kterou lze zapnout nebo vypnout.
- Přístup k `Bitcoin Bull Exchange` pro `Koupit, prodat nebo zaplatit` (závisí na jurisdikci a může vyžadovat KYC).
- `Převod` finančních prostředků mezi peněženkami
- `Secure Bitcoin` se rovná Onchain Bitcoin Wallet
- `Instantní platby` přes Lightning- / Liquid Network *(Poznámka: Bull Bitcoin Wallet umožňuje provádět a přijímat platby přes Lightning. Prostředky přijaté prostřednictvím Lightning jsou uloženy v síti [*Liquid](https://liquid.net/) (v Wallet Okamžité platby) díky automatické výměně prostřednictvím [*Boltz výměna](https://boltz.exchange/). To vám dává možnost komunikovat s Lightningem bez nutnosti spravovat kanály likvidity, přičemž zůstávají ve vlastní úschově)*
- `Odesílání` a `Příjem` finančních prostředků


![image](assets/en/02.webp)


Nejprve provedeme několik důležitých konfigurací a začneme s `Zálohováním`.


## 5️⃣ Zálohování


Chcete-li zahájit proces zálohování, klepněte na ikonu `Wallet Backup` v pravém horním rohu aplikace a vyberte možnost `Wallet Backup`. Zobrazí se vám dvě metody zabezpečení vašeho wallet: `Šifrovaný trezor` a `Fyzická záloha`. Prozkoumejme každou z nich.


![image](assets/en/03.webp)


### Fyzické zálohování


Klepnutím na možnost `Fyzická záloha` zobrazíte seznam 12 slov, která představují vaši frázi pro obnovu nebo frázi seed. Vezměte prosím v úvahu následující:



- Napište si svou "frázi o zotavení" s maximální pečlivostí. Napište si ji na papír nebo na kov a uložte ji na bezpečném místě (bezpečnostní schránka, offline místo). Tato fráze je vaším jediným prostředkem pro přístup k bitcoinům v případě ztráty zařízení nebo vymazání aplikace.
- Je také důležité si uvědomit, že kdokoli s touto frází může ukrást všechny vaše bitcoiny. Nikdy je neukládejte digitálně:
- Žádný snímek obrazovky
- Žádné zálohování do cloudu, e-mailu nebo zpráv
- Žádné kopírování/vkládání (riziko uložení do schránky)


![image](assets/en/25.webp)


Na další obrazovce budete muset slova seřadit ve správném pořadí, abyste se ujistili, že jste větu seed napsali správně. Po dokončení testu se zobrazí potvrzení, že test proběhl úspěšně.


! **Tento bod je rozhodující**. Další pomoc :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Šifrovaný trezor


K dispozici je také možnost šifrovaného anonymního zálohování v cloudu. Ale nezmínili jsme se v minulém odstavci, že zálohování v cloudu je rizikové a měli byste se mu vyhnout? Tým Bull Bitcoin však vyvinul chytrý způsob, jak tento proces zabezpečit. Funguje to následovně:


`Recoverbull` je zálohovací protokol, který zjednodušuje zabezpečení vašeho Bitcoin wallet rozdělením zálohování na dvě části. Nejprve je soubor zálohy vašeho zařízení wallet zašifrován pomocí silného šifrovacího klíče. Tento zašifrovaný soubor můžete uložit kamkoli chcete, například na Disk Google nebo do svého zařízení. Za druhé, šifrovací klíč potřebný k odemčení souboru je uložen na serveru Recoverbull Key Server. Chcete-li obnovit soubor wallet, potřebujete jak zašifrovaný záložní soubor, tak klíč, ke kterému získáte přístup pomocí kódu PIN nebo hesla. Tato konstrukce zajišťuje, že samotná cloudová záloha je k ničemu a že samotný server s klíči je bez vašeho konkrétního záložního souboru k ničemu. Vaše prostředky tak zůstanou v bezpečí i v případě, že dojde ke kompromitaci jedné části.


Představte si ji jako bezpečnostní schránku. Šifrovaný záložní soubor je *schránka*, kterou můžete uložit kamkoli (například na Disk Google). Váš kód PIN pro obnovení je *klíč*, který je uložen samostatně na serveru Recoverbull Key Server. Zloděj by musel získat jak vaši konkrétní schránku, tak váš konkrétní klíč, aby ji mohl otevřít. Tato konstrukce zajišťuje, že i když někdo získá váš záložní soubor, je bez klíče ze serveru nepoužitelný a klíč serveru je bez vašeho jedinečného záložního souboru nepoužitelný.


Další informace o zálohovacím protokolu `Recoverbull` wallet [zde](https://recoverbull.com/).


Klepněte na `Šifrovaný trezor` a poté klepnutím na `Pokračovat` potvrďte použití výchozího serveru. Připojení bude směrováno přes síť `Tor`, aby bylo zajištěno soukromí a anonymita.


**Znalost kódů PIN**



- `Pin odemknutí aplikace`**:** Volitelný PIN nastavený v `Nastavení > Bezpečnostní PIN` pro uzamčení aplikace v telefonu.
- `Pin obnovy`**:** Povinný PIN vytvořený během procesu zálohování `Šifrovaného trezoru`, který se používá k dešifrování záložního souboru během obnovy.


Jedná se o dva samostatné kódy PIN. Nezapomeňte svůj kód PIN pro obnovení, protože je nezbytný pro obnovení vašeho zařízení wallet."


**Nastavení kódu PIN pro obnovení:**



- Pro obnovení přístupu ke službě wallet je nutné vytvořit kód PIN nebo heslo.
- PIN / Heslo musí mít alespoň 6 číslic (např. se vyhněte jednoduchým sekvencím jako 123456, které nejsou akceptovány).
- Bez tohoto kódu PIN není možné obnovení kódu wallet.


Dále vyberte poskytovatele trezoru:



- `Google Drive` nebo
- `vlastní umístění` (např. vaše zařízení)


![image](assets/en/04.webp)


Nyní uložte `záložní soubor`. Poté klepněte na `Test Recovery`, vyberte uložený záložní soubor nebo trezor a klepněte na `Decrypt Vault`. Zadejte své `PIN` nebo `Heslo`. Pokud vše fungovalo, zobrazí se obrazovka `Test byl úspěšně dokončen`.


### Importní / exportní štítky


Nyní, když jsme vytvořili naši zálohu, se podívejme na `Labels`.  Bull Bitcoin wallet zlepšuje soukromí a organizaci tím, že umožňuje uživatelům vytvářet vlastní štítky pro jejich přijímací adresy a transakce. Tyto štítky vám pomohou kategorizovat vaše finanční prostředky, protože transakce odeslané na označenou adresu zdědí tento štítek, a můžete také označit odchozí transakce a sledovat jejich změnu. Zařízení wallet plně podporuje standard [BIP-329](https://bip329.org/), což znamená, že můžete exportovat všechny své štítky do souboru a importovat je do jiného zařízení wallet. Tato funkce zajišťuje bezproblémové zálohování historie transakcí a jejich kategorizace nebo jejich migraci mezi různými instancemi wallet, aniž byste ztratili personalizovanou organizaci.


![image](assets/en/05.webp)


## nastavení 6️⃣


Když máte primární zálohu zabezpečenou, prozkoumejme další funkce dostupné v nastavení.


### A - Zajištění přístupu


Chcete-li aplikaci zabezpečit, přejděte na `Nastavení` a zvolte `Zabezpečení PIN` a vyberte kód PIN. Vytvořte si silný kód PIN, kterým uzamknete přístup ke svému zařízení wallet. Tento krok je sice volitelný, ale důrazně jej doporučujeme, abyste zabránili neoprávněnému přístupu, pokud telefon používá někdo jiný.


![image](assets/en/06.webp)


### B - Připojení k osobnímu uzlu (volitelné)


BullBitcoin Wallet se ve výchozím nastavení připojuje k serverům Electrum: prvnímu, který spravuje Bull Bitcoin, a sekundárnímu serveru od společnosti Blockstream, přičemž se má za to, že oba nevedou žádné protokoly, což snižuje riziko sledování.


Pro větší důvěrnost můžete aplikaci připojit k vlastnímu uzlu Bitcoin prostřednictvím serveru Electrum. Za tímto účelem klepněte na `Nastavení` > `Nastavení Bitcoin` > `Nastavení Electrum Server` a poté klepněte na `+ Přidat vlastní server` a zadejte adresu a pověření serveru.


![image](assets/en/07.webp)


### C - měna


Dostupný zůstatek se na hlavní obrazovce zobrazuje v `sats` a `USD`. Chcete-li tuto hodnotu změnit, přejděte do `Nastavení` > `Měna`. Tam můžete přepínat mezi `sats/BTC` a vybrat svou `výchozí fiat měnu`.


![image](assets/en/08.webp)


### D - Nastavení Bitcoin


Nabídka `Bitcoin Settings` nabízí hluboký přístup k základním konfiguracím a datům vašeho wallet. Zde můžete kontrolovat základní údaje o svých peněženkách `Secure Bitcoin` a `Instant payments` a získat tak plnou transparentnost a kontrolu. Mezi klíčové funkce této nabídky patří:



- Podrobnosti o Wallet:** Chcete-li zobrazit konkrétní informace, přejděte na Zabezpečený Bitcoin nebo Okamžité platby wallet.
- Otisk prstu Wallet:** Jedinečný identifikátor pro váš wallet.
- Veřejný klíč (Pubkey):** Klíč používaný pro příjem adres generate.
- Descriptor:** Technické shrnutí struktury vašeho wallet.
- Cesta odvození:** Konkrétní cesta, která se používá pro generate všech adres z vašeho hlavního soukromého klíče.
- Zobrazení Address:** Přístup k seznamu nepoužívaných přijímacích adres a změna adres (již brzy)


Kromě toho máte možnost:



- nastavením `Aktivovat automatický převod` nastavíte maximální okamžitý zůstatek na účtu wallet, který bude automaticky převeden na zabezpečený bitcoinový účet wallet.
- Import obecných peněženek pomocí fráze `Mnemonic` nebo import `pouze hodinek`
- Připojení `Hardwarových peněženek`: v současné době jsou podporována zařízení ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade a Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Přímo z wallet máte přístup na burzu [Bull Bitcoin](https://www.bullbitcoin.com/), která vám umožňuje nakupovat, prodávat a platit Bitcoin, aniž byste museli opustit aplikaci. Tato integrace poskytuje pohodlné řešení pro správu vašich potřeb Bitcoin. Upozorňujeme, že přístup k burze a jejím službám může být omezen na základě vaší jurisdikce a pro splnění regulačních norem a využívání všech funkcí platformy může být vyžadováno dokončení ověření Know Your Customer (KYC).


Chcete-li začít, klepněte na `Exchange` v pravém dolním rohu a poté na `Přihlásit se` nebo `Přihlásit se` ke svému účtu.


Výměna nabízí následující [funkce](https://www.bullbitcoin.com/):



- Koupit Bitcoin s vlastní úschovou z bankovního účtu
- Bez vazby
- Fyzické nebo právnické osoby
- Okamžitý výběr
- Žádné skryté poplatky
- Lightning Network k dispozici
- Žádné limity transakcí
- Opakované možnosti nákupu


![image](assets/en/09.webp)


Další informace naleznete v tomto návodu:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Přijímání finančních prostředků


Příjem peněz pomocí **Bull Bitcoin Wallet** je jednoduchý a flexibilní, protože podporuje tři různé sítě přizpůsobené pro různé případy použití:



- Síť `Bitcoin (onchain)` pro bezpečné a dlouhodobé ukládání dat.
- Síť `Liquid` pro rychlé a důvěrnější transakce.
- Síť `Lightning` pro okamžité a levné platby.


Aplikace automaticky vygeneruje příslušnou adresu nebo fakturu na základě vybrané sítě. Zde je uveden postup pro jednotlivé sítě.


### Příjem prostřednictvím sítě Onchain (síť Bitcoin)


Chcete-li přijímat prostředky on-chain, můžete buď na domovské obrazovce vybrat `Zabezpečení Bitcoin Wallet` a klepnout na `Příjem`, nebo klepnout na hlavní tlačítko `Příjem` a poté vybrat `Síť Bitcoin`.


Pro generování adresy příjmu máte k dispozici dva základní režimy:


**Výchozí režim (URI s dalšími vstupními parametry)


Ve výchozím nastavení generuje wallet [BIP21 URI](https://bips.dev/21/). Jedná se o standardizovaný formát, který obsahuje více informací než pouhou adresu, včetně částky, osobní poznámky a parametrů PayJoin pro zvýšení soukromí. Tento komplexní URI je zakódován do QR kódu a zpřístupněn ke kopírování. Formát vypadá následovně: `bitcoin:<adresa>?<parametr1>=<hodnota1>&<parametr2>=<hodnota2>`.



- Další vstupní parametry:**
    - Částka:** Zadejte požadovanou částku v BTC, sats nebo ve fiat měně.
    - Zpráva:** Přidejte osobní poznámku, která bude viditelná pro odesílatele.
    - PayJoin:** Tuto možnost povolte, chcete-li zlepšit ochranu osobních údajů tím, že v transakci spojíte vstupy od odesílatele i příjemce.


Příklad URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Důležité upozornění: Na adresy uvedené v tomto návodu neposílejte žádné finanční prostředky, wallet bude smazán.*


![image](assets/en/10.webp)


**Povolena možnost kopírování nebo skenování pouze Address


Pokud je povolena možnost `Kopírovat nebo skenovat pouze Address`, aplikace generuje jednoduchou adresu Bitcoin ve formátu SegWit (bech32).


Příklad:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


I když zadáte částku nebo poznámku, nebudou zahrnuty do kódu QR ani do zkopírované adresy.


![image](assets/en/11.webp)


### Příjem prostřednictvím Liquid Network


Na účet Liquid Network můžete obdržet platbu. Na obrazovce `Přijmout` máte k dispozici dvě stejné možnosti pro vytvoření žádosti o platbu:


**1. Jednoduchý Address:** Zkopírujte standardní adresu `Liquid`. Jedná se o jedinečný identifikátor vašeho wallet v síti Liquid a neobsahuje žádnou konkrétní částku ani zprávu.


Příklad Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Podrobná žádost o platbu (URI):** Pro strukturovanější žádost můžete zadat částku a osobní poznámku. Tyto informace jsou automaticky zakódovány do sdíleného URI a odpovídajícího QR kódu.



- Částka:** Částku můžete nastavit v měně Bitcoin (BTC), Satoshis (Sats) nebo ve fiat měně.
- Poznámka:** Přidejte osobní vzkaz pro identifikaci transakce.


**Příklad URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Chcete-li transakci dokončit, zadejte odesílateli `adresu` nebo `URI`. To můžete provést zkopírováním do schránky nebo naskenováním QR kódu přímo z obrazovky.


![image](assets/en/12.webp)


### Příjem přes Lightning



Zařízení Bull Bitcoin Wallet také umožňuje odesílat a přijímat platby prostřednictvím Lightning Network. Klíčovou funkcí je, že prostředky přijaté prostřednictvím Lightning jsou automaticky převáděny a ukládány na `Liquid Network` v rámci vašeho `Instant Payments Wallet`. Tuto službu zajišťuje `Boltz`. Tato konstrukce vám umožňuje využívat rychlost a nízké náklady Lightning bez složitého řízení kanálů likvidity, a to vše při zachování plné vlastní úschovy vašich prostředků. Tento hybridní přístup je sice self-custodial a vyhýbá se složitosti správy kanálů, ale zavádí službu třetí strany (Boltz), malý swapový poplatek a spoléhání se na federaci funkcionářů Liquid Network jako držitelů klíčů, což je rozdíl oproti tradičnímu, ne-custodial Lightningu wallet, kde spravujete své vlastní kanály. Více informací o Liquid a tamním modelu správy se dozvíte zde:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Limity:**
    - Minimální částka:** Je vyžadována minimální částka faktury. Aktuální limit najdete v aplikaci
    - Poplatky:** Příjemce je povinen zaplatit malý poplatek za výměnu. Tento poplatek se odečítá z částky, kterou odesílatel převede, a může se změnit
- Výhody:**
    - Vlastní úschova:** Své finanční prostředky máte vždy pod kontrolou a jsou zabezpečeny v síti Liquid.
    - Vyhněte se vysokým poplatkům On-Chain:** Použitím služby Lightning a uložením na Liquid obejdete poplatky on-chain spojené s otevřením tradičního kanálu Lightning. Můžete se rozhodnout přesunout prostředky do kanálu on-chain později, až nashromážděná částka ospravedlní tyto výdaje.
    - Tip:** Chcete-li provést cenově nejvýhodnější transakci mezi dvěma uživateli Bull Bitcoin, použijte přímo síť **Liquid**, abyste se zcela vyhnuli poplatkům za výměnu Lightning.


Chcete-li obdržet platbu, musíte vystavit fakturu generate:


1. `Zadejte částku`**:** Zadejte částku, kterou chcete obdržet, a to v měně Bitcoin (BTC), Satoshis (Sats) nebo ve fiat měně.

2. `Přidat poznámku` **(volitelné):** Připojte poznámku nebo poznámku. Ta bude vložena do faktury a zobrazí se v historii transakcí po dokončení platby, což usnadní její identifikaci.

3. `Invoice Platnost`**:** Blesková faktura je časově omezená a její platnost vyprší po **12 hodinách**. Pokud nebude v této lhůtě uhrazena, stane se neplatnou a budete si muset generate vystavit novou.


Fakturu můžete odesílateli poskytnout zkopírováním do schránky nebo naskenováním kódu QR zobrazeného na obrazovce.


![image](assets/en/13.webp)


## 9️⃣ Zasílání finančních prostředků


Na obrazovku odeslání se dostanete přímo z domovské stránky nebo z kterékoli peněženky. Bull Bitcoin Wallet zjednodušuje proces tím, že automaticky detekuje cílovou síť - `Bitcoin`, `Liquid` nebo `Lightning` - na základě zadané adresy nebo faktury, ať už vložené, nebo naskenované pomocí QR kódu.


### Přenos On-Chain prostřednictvím sítě Bitcoin


Odeslání peněz on-chain znamená, že vaše transakce je zaznamenána přímo v blockchainu Bitcoin. Tato metoda je nejlepší pro větší převody nebo převody, které nejsou časově citlivé. Začít můžete klepnutím na `tlačítko odeslání` vpravo dole a naskenováním nebo zadáním `standardní adresy Bitcoin`.


Pokud zadaná adresa neobsahuje konkrétní částku, budete vyzváni k vyplnění údajů na obrazovce odeslání. Částku můžete zadat ve vámi preferované jednotce, například v BTC, satoshi nebo ve fiat ekvivalentu. Máte také možnost přidat osobní poznámku, což je soukromá poznámka pro vlastní potřebu, která vám později pomůže transakci identifikovat. Tato poznámka není sdílena s příjemcem.


Naopak, pokud již naskenovaný nebo vložený požadavek na platbu obsahuje všechny potřebné údaje, jako je URI BIP21 s předem definovanou částkou, obejde wallet obrazovku pro zadávání údajů a přenese vás přímo na obrazovku pro potvrzení autorizace platby.


![image](assets/en/14.webp)


Před odvysíláním transakce se zobrazí potvrzovací obrazovka. Je důležité věnovat chvíli času a pečlivě zkontrolovat každý parametr, věnovat velkou pozornost adrese příjemce, odesílané částce a síťovým poplatkům. Tato obrazovka také poskytuje výkonné nástroje pro přizpůsobení transakce.


Poplatky můžete kontrolovat dvěma základními způsoby. Prvním způsobem je výběr požadované rychlosti transakce, například nízké, střední nebo vysoké, a wallet vám automaticky vypočítá příslušný poplatek. Druhý způsob umožňuje přesnější ovládání tím, že vám umožní nastavit konkrétní poplatek, a to buď jako absolutní celkovou částku v satoshi, nebo jako relativní sazbu za bajt, která pak poskytne odhadovanou dobu potvrzení.


Pokročilým uživatelům nabízí wallet několik nastavení pro jemné doladění transakce. ve výchozím nastavení je zapnuta funkce `Replace-by-Fee` (RBF), což je cenná funkce, která umožňuje urychlit transakci, pokud se zasekne v mempoolu, jejím opětovným vysláním s vyšším poplatkem. Můžete také ručně vybrat, ze kterých `Unspent Transaction Outputs` (UTXOs) se mají utratit. Jedná se o mocný nástroj pro konsolidaci UTXO, strategii, při které spojíte více malých vstupů do jednoho většího. To sice může stát více na poplatcích za aktuální transakci, ale může to výrazně snížit poplatky za budoucí transakce, zejména pokud se očekává nárůst síťových poplatků.


![image](assets/en/15.webp)


Funkce PayJoin se automaticky provede při skenování žádosti příjemce o platbu (URI BIP21), která obsahuje parametr `pj=`. Pokud jednoduše vložíte prostou adresu bez dalších parametrů, tato funkce se neaktivuje. Tato kolaborativní metoda zvyšuje soukromí tím, že kombinuje vstupy od odesílatele i příjemce, čímž prolamuje heuristiku společného vlastnictví vstupů a za určitých okolností umožňuje lepší škálování a také úsporu poplatků.


### Odesílání do Liquid Network


Zařízení `Liquid Network` je navrženo pro rychlé a důvěrné transakce s minimálními poplatky. Při odesílání peněz prostřednictvím Liquid jsou tyto peníze vybírány z vašeho účtu `Instant Payments Wallet`. Proces je jednoduchý: jednoduše zadáte nebo naskenujete adresu příjemce `Liquid`.


Pokud v adrese není uvedena částka, budete o její zadání požádáni na obrazovce odeslání. Částku můžete zadat v BTC, satoších nebo fiat. Klíčovou výhodou Liquid je její nízká minimální hranice. Stejně jako u transakcí on-chain můžete přidat nepovinnou osobní poznámku pro vlastní záznamy. Pokud již žádost o platbu obsahuje částku, přejde wallet přímo na obrazovku potvrzení.


Na obrazovce potvrzení transakce Liquid zkontrolujete podrobnosti. Poplatky jsou pozoruhodně nízké a vypočítávají se na základě složitosti transakce. Obvykle se pohybují kolem 0,1 sat/vB, což u jednoduché transakce činí pouhých 20-40 satoshis (například 26 satoshis k 21. prosinci 2025).


![image](assets/en/16.webp)


### Odesílání do Lightning Network


Můžete buď naskenovat bleskovku Address (např. `runningbitcoin@rizful.com`), která vám umožní nastavit částku a volitelnou poznámku pro příjemce, nebo naskenovat fakturu s předem definovanou částkou, čímž se dostanete přímo na obrazovku potvrzení.


*Vezměte na vědomí, že platí minimální částky a poplatky.*


Bull Bitcoin Wallet odesílá bleskové platby výběrem prostředků z vašeho účtu `Instant Payments Wallet` (na Liquid) a jejich výměnou prostřednictvím `Boltz`. Tento hybridní přístup je plně samospasitelný a vyhýbá se vysokým poplatkům za správu vyhrazeného kanálu Lightning na on-chain, ale vyžaduje zaplacení poplatku za `swap`. Nejnižší náklady získáte, když budete odesílat přímo na adresu Liquid příjemce, pokud používá také Bull Bitcoin wallet.


## 🔟 Převod prostředků mezi peněženkami


Bull Bitcoin umožňuje přesunout váš Bitcoin mezi vaším `Secure Bitcoin` wallet a vaším `Instant Payments Wallet` na Liquid Network nebo na `externí Wallet`. Chcete-li provést převod, jednoduše přejděte do sekce `Převod`, vyberte zdrojovou a cílovou peněženku, zadejte částku, kterou chcete přesunout, a potvrďte transakci.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Obnovení vašeho Bull Bitcoin Wallet


V této části je vysvětleno, jak obnovit přístup k prostředkům Bull Bitcoin Wallet, pokud zařízení ztratíte, odinstalujete aplikaci nebo jednoduše potřebujete přejít na nové zařízení. Jak již bylo vysvětleno, existují dvě základní metody obnovy: pomocí jedinečné metody `Recoverbull` a pomocí standardní `BIP39 seed fráze`.


### Metoda 1: Recoverbull


Rekapitulace: Zálohy Wallet jsou šifrovány lokálně. Zašifrovaný soubor může být uložen v cloudovém úložišti nebo v jiném zařízení. Šifrovací klíč je uložen na serveru Recoverbull Key Server. Obojí je uchováváno odděleně a pro obnovu zařízení wallet je nutné je kombinovat.


Pro začátek odstraním Wallet se všemi prostředky a znovu nainstaluji wallet. Znovu se ocitneme na obrazovce `Vítejte`. Tentokrát vyberte možnost `Obnovit Wallet`. Poté přejděte na metodu `Šifrovaný trezor`, potvrďte použití `Výchozího klíčového serveru` a vyberte umístění nebo `Poskytovatele trezoru`, kam jste uložili záložní soubor.


![image](assets/en/18.webp)


Uvádí, že trezor byl úspěšně importován. Klepněte na tlačítko `Decrypt Vault` a zadejte `PIN`. Na další obrazovce se zobrazí vaše `zůstatky` a `počet transakcí`, které byly obnoveny.


![image](assets/en/19.webp)


### Metoda 2: Výchozí fráze


Tato metoda využívá hlavní frázi pro obnovení účtu wallet, standardní seznam 12 slov, který slouží jako konečná záloha vašich prostředků. Jedná se o nejuniverzálnější způsob obnovy Bitcoin wallet, protože není vázán na žádnou konkrétní službu nebo server. Pokud máte tuto frázi, můžete obnovit svůj klíč wallet na jakémkoli kompatibilním zařízení, a to i bez přístupu ke klíčovému serveru Bull Bitcoin.


Na uvítací obrazovce vyberte možnost `Obnovit Wallet`. Tentokrát vyberte metodu `Fyzické zálohování`. Aplikace zobrazí mřížku se slovy. Pečlivě vyberte jednotlivá slova z 12slovné věty seed ve správném pořadí. Buďte pečliví, protože jediná chyba bude mít za následek nesprávné slovo wallet.


## 1️⃣2️⃣ Připojení zařízení Hardware Wallet


Mnoho uživatelů Bitcoin si pro nejvyšší úroveň zabezpečení vybírá uložení svých prostředků v "chladicím skladu". To znamená, že `privátní klíče`, které ovládají váš Bitcoin, uchovávají na zařízení, které není nikdy připojeno k internetu. Hardwarové zařízení wallet (neboli Signing device) je specializované fyzické zařízení určené právě k tomuto účelu. Funguje jako digitální trezor pro vaše klíče a zajišťuje, že nebudou nikdy vystaveny potenciálním hrozbám online počítače nebo chytrého telefonu.


Připojením hardwarového zařízení wallet k aplikaci Bull Bitcoin získáte to nejlepší z obou světů: nekompromisní zabezpečení chladicího úložiště pro vaše soukromé klíče v kombinaci s výkonnými funkcemi a uživatelsky přívětivým rozhraním Bull Bitcoin wallet pro prohlížení zůstatků a správu transakcí. V této závěrečné kapitole vám ukážeme, jak připojit hardwarovou kartu wallet, například [Coldcard Q](https://coldcard.com/q), k vašemu zařízení Bull Bitcoin wallet. Tento návod se nebude podrobně zabývat nastavením karty Coldcard Q; o tom se můžete dozvědět zde:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importování modelu Wallet


![image](assets/en/26.webp)


Nejprve v hlavní nabídce karty Coldcard Q vyberte možnost `Exportovat Wallet` a poté `Bull Wallet`. Na kartě Coldcard se zobrazí QR kód generate.


![image](assets/en/20.webp)


Otevřete zařízení Bull Bitcoin Wallet a přejděte na `Nastavení` > `Nastavení Bitcoin` > `Importovat wallet` a vyberte `Koldcard Q` na telefonu a klepnutím na `Otevřít fotoaparát` naskenujte tento QR kód pro import veřejných klíčů hardwaru wallet.


![image](assets/en/21.webp)


### Příjem pomocí karty Coldcard Q


Chcete-li přijímat Bitcoin pomocí připojené karty Coldcard Q, nemusíte mít zařízení fyzicky připojené k telefonu. Zařízení Bull Bitcoin Wallet již importovalo potřebné veřejné klíče, což mu umožňuje samostatně přijímat adresy generate.


1. Klepněte na importované podpisové zařízení Coldcard Q a vyberte možnost `Přijmout`.

2. Aplikace automaticky zobrazí čerstvou adresu Bitcoin z karty wallet karty Coldcard.

3. Tuto adresu použijte pro příjem finančních prostředků. Zařízení Bitcoin bude zajištěno přímo klíči hardwarového zařízení wallet, i když bylo během procesu offline.


![image](assets/en/22.webp)


### Odesílání pomocí karty Coldcard Q


Odeslání Bitcoin s kartou Coldcard Q vyžaduje vaše fyzické potvrzení k autorizaci jakékoli transakce. Zatímco aplikace Bull Wallet slouží k sestavení transakce, konečný podpis lze vytvořit pouze na samotném hardwaru wallet.


Začněte tím, že otevřete kartu `Coldcard Q` wallet a klepněte na `Odeslat`. Poté `otevřete fotoaparát` a naskenujte QR kód přijímající adresy. Po naskenování zadejte `částku`, kterou chcete odeslat, a podle potřeby upravte `prioritu poplatku`.


Další možnosti naleznete v části Rozšířená nastavení. Zde naleznete možnost `Nahradit poplatkem` (RBF), která je ve výchozím nastavení aktivována a umožňuje urychlit zaseknutou transakci později. K dispozici máte také možnost `Coin Control`, která vám umožňuje ručně vybrat konkrétní UTXO, které chcete utratit.


Po zkontrolování všech údajů klepněte na možnost `Zobrazit PSBT` a připravte transakci.


![image](assets/en/23.webp)


Klepněte na tlačítko `Scan` na kartě Coldcard Q a pomocí jejího fotoaparátu naskenujte kód QR zobrazený na telefonu. Na obrazovce karty Coldcard se poté zobrazí všechny podrobnosti o transakci. Pečlivě zkontrolujte částku, adresu příjemce a svou adresu pro změnu. Pokud je vše v pořádku, stiskněte tlačítko `Enter` na kartě Coldcard Q a podepište transakci. Poté se na obrazovce zobrazí QR kód podepsané transakce.


![image](assets/en/24.webp)


V zařízení Bull wallet klepněte na tlačítko `Jsem hotov` a poté klepnutím na tlačítko `Kamera` naskenujte QR kód `podepsané transakce` z karty Coldcard Q. V zařízení Bull Wallet se nyní zobrazí obrazovka se souhrnem podepsané transakce. Naposledy si ji prohlédněte a poté klepněte na tlačítko `Vysílat` transakci. Tím se proces dokončí odesláním transakce do sítě Bitcoin a vaše finanční prostředky budou na cestě.


## 🎯 Závěr


Nyní jste dokončili svou cestu po Bull Bitcoin Wallet. Aplikace vám poskytne výkonné nástroje pro ochranu soukromí a zabezpečení přímo na dosah ruky a usnadní vám používání pokročilých funkcí. Pomáhá vám zůstat v soukromí díky funkcím, jako je `PayJoin`, která skrývá vaše transakce v blockchainu, a `Tor integration`, která maskuje vaši síťovou aktivitu před zvědavýma očima. Pro ty, kteří chtějí mít maximální kontrolu, se můžete připojit k `vlastnímu osobnímu uzlu Bitcoin`, abyste se přestali spoléhat na servery třetích stran, a používat `hardwarový wallet`, abyste měli své soukromé klíče zcela offline a v bezpečí. Díky chytrým možnostem zálohování a bezproblémové podpoře pro Bitcoin, Liquid a Lightning je Bull Bitcoin Wallet silnou, univerzální volbou pro každého, kdo to myslí vážně s udržením svých prostředků v soukromí, bezpečí a pod plnou vlastní kontrolou.


## 📚 Zdroje Bull Wallet


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Webové stránky ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)