---
name: Sentinel Watch-Only
description: Co je to peněženka pouze pro sledování a jak ji používat?
---
![cover](assets/cover.webp)

---

***VAROVÁNÍ:** Po zatčení zakladatelů peněženky Samourai a zabavení jejich serverů 24. dubna aplikace Sentinel nadále funguje, ale **je nutné používat vlastní Dojo** pro přístup k informacím o blockchainu a odesílání transakcí.*

_Sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento návod aktualizujeme, jakmile budou k dispozici nové informace._

_Tento návod je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

*"Uchovávejte své soukromé klíče v soukromí."*

V tomto článku prozkoumáme vše, co potřebujete vědět o peněženkách pouze pro sledování. Probereme, jak fungují, a prozkoumáme různé dostupné aplikace na trhu. Nakonec nabídneme podrobný návod na jednu z nejpopulárnějších aplikací pro peněženky pouze pro sledování: Sentinel.

## Co je to peněženka pouze pro sledování?
Peněženka pouze pro sledování, nebo peněženka pouze pro čtení, je typ softwaru navržený tak, aby uživateli umožnil sledovat transakce spojené s jedním nebo více konkrétními veřejnými klíči Bitcoinu, aniž by měl přístup k odpovídajícím soukromým klíčům.

Tento typ aplikace uchovává pouze data potřebná pro sledování Bitcoinové peněženky, včetně zobrazení jejího zůstatku a historie transakcí, ale nemá přístup k soukromým klíčům. Proto je nemožné utratit bitcoiny držené v peněžence na aplikaci pouze pro sledování.
![watch-only](assets/en/1.webp)
Peněženka pouze pro sledování se obvykle používá ve spojení s hardwarovou peněženkou. To umožňuje uchovávat soukromé klíče peněženky "v chladu", na zařízení nepřipojeném k internetu, které má minimální útočnou plochu, izoluje soukromé klíče od potenciálně zranitelných prostředí. Aplikace pouze pro sledování na druhé straně výhradně uchovává rozšířený veřejný klíč (`xpub`, `zpub` atd.) Bitcoinové peněženky. Tento rodičovský klíč neumožňuje odhalení přidružených soukromých klíčů a tedy neumožňuje utrácení bitcoinů. Nicméně umožňuje odvození dětských veřejných klíčů a přijímacích adres. S vědomím adres peněženky zabezpečené hardwarovou peněženkou může aplikace pouze pro sledování sledovat tyto transakce na Bitcoinové síti, nabízí uživateli možnost sledovat jejich zůstatek a generovat nové přijímací adresy, aniž by musel každé připojit svou hardwarovou peněženku.

## Kterou peněženku pouze pro sledování použít?
V současnosti je nejkomplexnější aplikací pouze pro sledování [Sentinel](https://sentinel.watch/), vyvinutý týmy Samourai Wallet. Zahrnuje všechny základní funkce pro dobrou peněženku pouze pro sledování:
- Podpora pro rozšířené klíče, veřejné klíče a adresy;
- Možnost organizovat více účtů nebo peněženek do kolekcí;
- Generování adres pro přijímání bitcoinů na hardwarové peněžence bez nutnosti jejího přímého použití;
- Možnost sestavit a odeslat transakce offline;
- Možnost připojení k vlastnímu Bitcoinovému uzlu;
- Integrace Toru pro zvýšené soukromí.
Jediné nevýhody Sentinelu spočívají v tom, že aplikace je k dispozici výhradně pro Android a nepodporuje peněženky s více podpisy. Proto, pokud vlastníte zařízení s Androidem a vaše peněženka je klasická s jedním podpisem, doporučuji Sentinel.
Pro ty, kteří chtějí sledovat peněženku s více podpisy, je jedinou aplikací, kterou znám a která nabízí režim pouze pro sledování pro tyto typy peněženek, Blue Wallet, a je dostupná jak pro Android, tak pro iOS.
Pro uživatele iOS, kteří hledají alternativu k Sentinel, mohou být možnostmi [Green Wallet](https://blockstream.com/green/) nebo [Blue Wallet](https://bluewallet.io/watch-only/), ačkoliv jejich funkce pouze pro sledování není tak komplexní jako u Sentinelu. ![watch-only](assets/notext/2.webp)
## Jak používat Sentinel Watch-Only peněženku?
### Instalace a nastavení
Začněte instalací aplikace Sentinel. Můžete tak učinit buď z Google Play Store nebo pomocí [APK dostupného ke stažení na oficiálních stránkách](https://sentinel.watch/download/).

![watch-only](assets/notext/3.webp)

Při prvním otevření aplikace máte na výběr mezi:
- `Připojit k Dojo`;
- `Připojit k serveru Samourai`.

Dojo, vyvinutý týmem Samourai, je plná verze Bitcoinového uzlu, kterou lze nainstalovat samostatně nebo přidat jedním kliknutím do řešení uzlu v boxu, jako jsou [Umbrel](https://umbrel.com/) a [RoninDojo](https://ronindojo.io/).

[**-> Zjistěte, jak nainstalovat RoninDojo v2 na Raspberry Pi.**](https://planb.network/fr/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)

Pokud máte vlastní Dojo, můžete se na této fázi připojit. Tím získáte nejvyšší úroveň soukromí při kontrole informací o transakcích v Bitcoinové síti.

![watch-only](assets/notext/4.webp)

Jinak je možné zvolit výchozí server Samourai. Můžete také vybrat, zda se připojit přes Tor nebo ne.

![watch-only](assets/notext/5.webp)

Poté se dostanete na hlavní stránku Sentinelu.

![watch-only](assets/notext/6.webp)

Pro začátek můžete aplikaci nastavit. Klikněte na tři malé tečky v pravém horním rohu, poté na `Nastavení`.

![watch-only](assets/notext/7.webp)
Výběrem `Uživatelský PIN kód` máte možnost nastavit heslo pro zabezpečení přístupu k vaší peněžence pouze pro sledování. Máte také možnost změnit referenční měnu pro převod vašich zůstatků na fiat měnu, nebo dokonce skrýt hodnoty ve fiat měně aktivací možnosti `Skrýt hodnoty ve fiat měně`. Pro zvýšení bezpečnosti můžete aktivovat `Zakázat snímky obrazovky`, což brání jakýmkoli snímkům obrazovky vaší aplikace Sentinel a tím zabraňuje jakémukoli odhalení informací na externím displeji.
![watch-only](assets/notext/8.webp)

V tomto menu nastavení máte také možnost zálohovat svůj Sentinel.

### Používání peněženky pouze pro sledování
Na domovské stránce stiskněte modré tlačítko `NOVÝ`, abyste přidali nový rozšířený veřejný klíč pro sledování. Poté máte možnost naskenovat QR kód vašeho klíče nebo přímo vložit klíč (`xpub`, `zpub`...) výběrem `Vložit veřejný klíč`.

![watch-only](assets/notext/9.webp)

Obecně je `xpub` vaší peněženky přímo přístupný prostřednictvím softwaru pro správu vaší peněženky, který používáte. Například, pokud spravujete svou hardware peněženku pomocí Sparrow, tato informace se nachází v záložce `Nastavení`, v sekci `Keystore`.

![watch-only](assets/notext/10.webp)
Po zadání rozšířeného veřejného klíče do aplikace Sentinel vám aplikace nabídne možnost vytvořit novou kolekci. Kolekce představuje soubor rozšířených veřejných klíčů organizovaných dohromady. Tato možnost vám dává možnost nejen vypsat všechny vaše `xpubs`, ale také je klasifikovat uspořádaným způsobem. Například, pokud máte peněženku Samourai s více účty (vklad, premix, postmix...), můžete všechny tyto účty shromáždit pod kolekcí `Samourai`. Pro peněženky spravované pro vaši rodinu byste mohli vytvořit kolekci pojmenovanou `Rodina`.
Vyberte `Vytvořit novou kolekci`. Poté zadejte název pro rozšířený klíč, který jste právě integrovali. Například, pokud naskenuji účet pro vklady mé peněženky Samourai, pojmenuji tento klíč `Vklad`. Klikněte na `ULOŽIT` pro dokončení.

![watch-only](assets/notext/11.webp)

Dále přiřaďte název této kolekci a stiskněte ikonu ověření umístěnou v pravém horním rohu obrazovky pro uložení kolekce. Vaše kolekce je nyní viditelná na domovské obrazovce Sentinel.

![watch-only](assets/notext/12.webp)

Pokud si přejete přidat další rozšířený veřejný klíč, klikněte znovu na `NOVÝ` a zadejte svůj klíč.

![watch-only](assets/notext/13.webp)
Poté budete vyzváni k výběru kolekce, do které chcete tento klíč začlenit, nebo k vytvoření nové. Například, v mém případě jsem nastavil kolekci speciálně pro mou peněženku Ledger.
![watch-only](assets/notext/14.webp)

Pro detailní zobrazení rozšířených klíčů kolekce jednoduše na ni klikněte. Poté můžete procházet různé záložky a zobrazit historii transakcí.

![watch-only](assets/notext/15.webp)

Z kolekce můžete klepnutím na tři malé tečky v pravém horním rohu a poté na `Zobrazit nespotřebované výstupy` získat přístup k seznamu UTXO držených sledovanou peněženkou.

![watch-only](assets/notext/16.webp)

### Odesílání a přijímání bitcoinů pomocí Sentinel
Stejně jako u každé dobré peněženky pouze pro sledování, Sentinel vám umožňuje generovat přijímací adresy pro přijímání bitcoinů na sledované peněžence. Ale Sentinel nabízí také další pokročilou funkci: vytvoření a vysílání částečně podepsané bitcoinové transakce (PSBT). Peněženka držící soukromé klíče tak může tuto transakci podepsat, která, jakmile je podepsána, může být vysílána na bitcoinovou síť pomocí Sentinel. Podívejme se, jak to všechno udělat.

**Pozor, není doporučeno přijímat bitcoiny na přijímací adresu, kterou peněženka sama neověřila.** Pokud peněženka držící soukromé klíče, například hardwarová peněženka, explicitně nepotvrdila, že určitá adresa je s ní spojena, odesílání bitcoinů na tuto adresu je riskantní praxe. Skutečně, bez tohoto potvrzení, není žádná záruka, že adresa skutečně patří vaší peněžence. Proto by měla být přijímací funkce peněženky pouze pro sledování používána s opatrností, s vědomím, že odeslané prostředky by mohly být potenciálně ztraceny.

Pro přijetí bitcoinů přes Sentinel vyberte kolekci, která vás zajímá, poté klikněte na záložku odpovídající rozšířenému veřejnému klíči, na který chcete převést prostředky.

![watch-only](assets/notext/17.webp)

Nakonec klikněte na ikonu šipky v dolní levé části obrazovky. Sentinel poté pro vás vygeneruje prázdnou přijímací adresu. Můžete ji zkopírovat nebo naskenovat pomocí QR kódu.

![watch-only](assets/notext/18.webp)
Pro vygenerování PSBT z Sentinelu a tím zahájení transakce, přejděte na rozšířený klíč peněženky, ze které chcete platbu provést. Vezměme si například můj vkladový účet na mé peněžence Samourai. Poté klikněte na ikonu šipky v pravém dolním rohu obrazovky.
![watch-only](assets/notext/19.webp)

Zadejte všechny parametry související s vaší transakcí:
- Zadejte adresu příjemce (kliknutím na ikonu QR kódu máte možnost tuto adresu naskenovat);
- Uveďte částku, kterou chcete na tuto adresu poslat;
- Určete poplatky za transakci.

Jakmile vyplníte všechna potřebná pole pro vaši transakci, stiskněte tlačítko `COMPOSE UNSIGNED TRANSACTION`.

![watch-only](assets/notext/20.webp)

Poté získáte přístup k PSBT, což představuje sestavenou, ale nepodepsanou Bitcoinovou transakci, jelikož Sentinel nemá přístup k vašim soukromým klíčům. Máte možnost tuto transakci zkopírovat, exportovat jako soubor `.psbt`, nebo ji naskenovat pomocí animovaného QR kódu.

![watch-only](assets/notext/21.webp)

Poté přejděte do peněženky, která má soukromé klíče pro podepsání transakce (Samourai, hardware peněženka...).

![watch-only](assets/notext/22.webp)

Jakmile je transakce podepsána, můžete se vrátit do Sentinelu, abyste ji odeslali. K tomu z hlavního menu klikněte na tři malé tečky v pravém horním rohu a poté na `Broadcast transaction`.

![watch-only](assets/notext/23.webp)

Máte možnost zadat váš podepsaný PSBT třemi různými způsoby:
- Vložením přímo ze schránky;
- Importem z `.psbt` souboru;
- Naskenováním pomocí QR kódu.

![watch-only](assets/notext/24.webp)

Jakmile je podepsaná transakce zadána do šedého rámečku, můžete kliknout na zelené tlačítko `BROADCAST TRANSACTION` a odeslat ji do Bitcoinové sítě. Sentinel vám poskytne jeho TXID.

![watch-only](assets/notext/25.webp)

