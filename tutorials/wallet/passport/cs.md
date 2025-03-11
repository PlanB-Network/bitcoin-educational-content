---
name: Passport - Nadace
description: Konfigurace a používání hardwarové peněženky Passport v ručním režimu
---
![cover](assets/cover.webp)

Passport je hardwarová peněženka pouze pro bitcoiny, kterou navrhla americká společnost Foundation Devices založená v dubnu 2020 v Bostonu.

Passport "*Batch 2*", který představujeme v tomto tutoriálu, je nástupcem edice "*Founder's Edition*". Vyniká prémiovým designem, vysoce kvalitním barevným displejem a ergonomickou fyzickou klávesnicí. Funguje v režimu "*Air-Gap*", což zajišťuje, že soukromé klíče vaší peněženky zůstanou zcela izolované, přičemž komunikace probíhá prostřednictvím karty MicroSD nebo QR kódů. Zařízení je vybaveno vyměnitelnou dobíjecí baterií Nokia BL-5C s kapacitou 1200 mAh. Tato běžně dostupná baterie může být snadno nahrazena, protože model BL-5C lze snadno najít v obchodech.

Co se týče konektivity, je Passport vybaven portem MicroSD, portem USB-C pro nabíjení a zadní kamerou pro snímání QR kódů.

Pokud jde o zabezpečení, Passport obsahuje zabezpečený prvek a zdrojový kód zařízení je zcela otevřený. Nabízí všechny funkce, které se od dobré hardwarové peněženky na bitcoiny očekávají. Všimněte si, že Passport zatím nepodporuje miniskript, ale tato funkce je plánována na druhé čtvrtletí roku 2025.

Za cenu 199 dolarů je Passport považován za špičkovou hardwarovou peněženku, která konkuruje modelům Coldcard Q, Jade Plus, Tezor Safe 5 a špičkovým modelům Ledger.

![Image](assets/fr/01.webp)

Chcete-li spravovat zabezpečenou peněženku v zařízení Passport, máte několik možností. Tato hardwarová peněženka je kompatibilní s většinou softwaru pro správu peněženek na trhu, včetně Sparrow Wallet, Specter Desktop, Nunchuk, Keeper a dalších. V tomto návodu se naučíme, jak ji používat s peněženkou Sparrow Wallet.

Pokud jste začátečník, je nejjednodušší používat Passport s nativní aplikací Envoy, kterou vyvinula společnost Foundation. Chcete-li zjistit, jak používat aplikaci Envoy s aplikací Passport, přečtěte si tento další návod :

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## Vybalení pasu

Po obdržení pasu se ujistěte, že krabice a pečeť na kartonu jsou neporušené, abyste potvrdili, že balíček nebyl otevřen. Při nastavení zařízení bude rovněž provedeno softwarové ověření jeho pravosti a neporušenosti.

![Image](assets/fr/02.webp)

Obsah krabice zahrnuje :


- Cestovní pas;
- Kousek kartonu na zapsání mnemotechnické fráze;
- Kabel USB-C pro nabíjení ;
- Karta MicroSD ;
- Dva adaptéry MicroSD na Lightning nebo USB-C ;
- Nálepky.

V zařízení najdete :


- Klávesnice (1) ;
- Port USB-C (2);
- Tlačítko pro mazání (3);
- Tlačítko pro návrat (4) ;
- Potvrzovací tlačítko (5);
- Směrová podložka (6);
- Tlačítko zapnutí/vypnutí (7);
- Indikátor stavu (8);
- Port MicroSD (9) ;
- Tlačítko pro změnu režimu aA1 (10) ;
- Zadní fotoaparát.

![Image](assets/fr/03.webp)

## Startovací pas

Stisknutím tlačítka zapnutí/vypnutí na boku přístroje jej spusťte.

![Image](assets/fr/04.webp)

Stisknutím potvrzovacího tlačítka přejdete do další nabídky.

![Image](assets/fr/05.webp)

V tomto návodu budeme ke správě peněženky zabezpečené pomocí pasu používat peněženku Sparrow Wallet. Vyberte možnost "*Ruční nastavení*".

![Image](assets/fr/06.webp)

Poté přijměte podmínky používání.

![Image](assets/fr/07.webp)

Dalším krokem je kontrola zařízení. Tím se potvrdí pravost vašeho pasu a zajistí se, že s ním nebylo při přepravě manipulováno. Budete požádáni o naskenování QR kódu.

![Image](assets/fr/08.webp)

Přejděte na [oficiální ověřovací stránku](https://validate.foundationdevices.com/) a vyberte "*Pas*".

![Image](assets/fr/09.webp)

Pomocí fotoaparátu pasu naskenujte kód QR zobrazený na webu.

![Image](assets/fr/10.webp)

Zařízení poté zobrazí 4 slova.

![Image](assets/fr/11.webp)

Zadejte tato slova na webové stránce, abyste potvrdili pravost svého pasu, a klikněte na "*Validate*".

![Image](assets/fr/12.webp)

Pokud se zobrazí zpráva "*Passed*", je vaše hardwarová peněženka pravá. Nyní ji můžete použít k zabezpečení peněženky Bitcoin.

![Image](assets/fr/13.webp)

Potvrďte výsledek testu v pasu.

![Image](assets/fr/14.webp)

## Nastavení kódu PIN

Poté následuje krok zadání kódu PIN. Kód PIN odemkne váš pas. Poskytuje tedy ochranu před neoprávněným fyzickým přístupem. Kód PIN se nepodílí na odvození kryptografických klíčů vaší peněženky. Takže i bez přístupu ke kódu PIN vám vlastnictví vaší 12- nebo 24slovné mnemotechnické fráze umožní znovu získat přístup k vašim bitcoinům.

![Image](assets/fr/15.webp)

Doporučujeme zvolit co nejnáhodnější kód PIN. Nezapomeňte tento kód uložit na jiné místo, než kde je uložen váš pas (např. do správce hesel).

Můžete si zvolit 6 až 12místný kód PIN. Doporučuji, aby byl co nejdelší.

Pomocí klávesnice zadejte čísla PIN. Po dokončení klikněte na potvrzovací tlačítko.

![Image](assets/fr/16.webp)

Potvrďte PIN podruhé.

![Image](assets/fr/17.webp)

Váš kód PIN byl zaregistrován.

![Image](assets/fr/18.webp)

## Aktualizace firmwaru Passportu

Vaše hardwarová peněženka doporučuje aktualizovat její firmware. Doporučuji provést aktualizaci okamžitě, abyste mohli využít vylepšení a oprav, které přinášejí nejnovější verze. Chcete-li pokračovat, klikněte na potvrzovací tlačítko vpravo.

![Image](assets/fr/19.webp)

Váš Passport je připraven přijmout nový firmware prostřednictvím karty MicroSD.

![Image](assets/fr/20.webp)

K tomu použijte kartu MicroSD, která je součástí balení Passportu (nebo jinou kartu), a vložte ji do počítače. Stáhněte si nejnovější verzi firmwaru ze stránek [dokumentace nadace](https://docs.foundation.xyz/firmware-updates/passport/) nebo [jejich úložiště GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Před instalací do zařízení důrazně doporučujeme zkontrolovat pravost a neporušenost staženého firmwaru. Pokud s tím potřebujete pomoci, podívejte se do tohoto návodu :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Po kontrole souboru `.bin` jej umístěte na kartu MicroSD a poté ji vložte do zařízení Passport. Otevře se průzkumník souborů Passport. Vyberte soubor `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Klikněte na "*Vybrat*".

![Image](assets/fr/23.webp)

Poté potvrďte instalaci firmwaru.

![Image](assets/fr/24.webp)

Vyčkejte na dokončení aktualizace.

![Image](assets/fr/25.webp)

Po dokončení aktualizace zadejte kód PIN, abyste odemkli zařízení a pokračovali v konfiguraci.

![Image](assets/fr/26.webp)

## Vytvoření nové peněženky Bitcoin

Nyní je čas vytvořit novou peněženku Bitcoin. Klikněte na potvrzovací tlačítko.

![Image](assets/fr/27.webp)

Chcete-li vytvořit nové portfolio, klikněte na "*Vytvořit nové semeno*".

![Image](assets/fr/28.webp)

Můžete si vybrat mezi mnemotechnickou frází o 12 nebo 24 slovech. Bezpečnost, kterou obě možnosti nabízejí, je podobná, takže se můžete rozhodnout pro tu, která se nejsnáze ukládá, tj. 12 slov.

![Image](assets/fr/29.webp)

Klikněte na "*Pokračovat*".

![Image](assets/fr/30.webp)

Váš Passport nyní vygeneruje váš "*záložní kód*". Jedná se o sérii čísel, která lze použít k dešifrování zálohy vaší peněženky uložené na MicroSD. Tento zálohovací systém, specifický pro zařízení Foundation, představuje další zálohu vaší mnemotechnické fráze, ale není kompatibilní s jiným softwarem pro Bitcoin.

Pokud se rozhodnete tento "*záložní kód*" použít, nezapomeňte jej uložit na jiné místo než kartu MicroSD se zašifrovanou zálohou peněženky. Můžete se však rozhodnout tento systém nepoužívat, pokud máte pocit, že vám postačí dobrá záloha vaší mnemotechnické fráze.

![Image](assets/fr/31.webp)

Zadejte svůj "*Kód zálohy*" a potvrďte, že jste jej uložili správně.

![Image](assets/fr/32.webp)

Pokud byla vložena karta MicroSD, byla na ni uložena zašifrovaná záloha vašeho portfolia.

![Image](assets/fr/33.webp)

V pasu se zobrazí vaše 12slovná mnemotechnická fráze. Tato mnemotechnická fráze vám umožní plný a neomezený přístup ke všem vašim bitcoinům. Kdokoli, kdo tuto frázi zná, může vaše prostředky ukrást, a to i bez fyzického přístupu k vašemu pasu.

Fráze o 12 slovech obnoví přístup k bitcoinům v případě ztráty, krádeže nebo poškození pasu. Je proto velmi důležité jej pečlivě uložit a uchovávat na bezpečném místě.

Můžete jej napsat na karton dodávaný v krabici, nebo pro větší bezpečnost doporučuji vyrýt jej na podstavec z nerezové oceli, který jej ochrání před požárem, povodní nebo zřícením.

Kliknutím na potvrzovací tlačítko zobrazíte svou mnemotechnickou frázi.

![Image](assets/fr/34.webp)

Pro více informací o správném způsobu ukládání a správy mnemotechnických frází vřele doporučuji sledovat tento další návod, zejména pokud jste začátečníci:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

samozřejmě nesmíte tato slova nikdy sdílet na internetu, jako to dělám já v tomto návodu. Toto ukázkové portfolio bude použito pouze na Testnetu a na konci tutoriálu bude smazáno.**_

Vytvořte si fyzickou zálohu této věty.

![Image](assets/fr/35.webp)

Váš Passport byl úspěšně nakonfigurován. Kliknutím na potvrzovací tlačítko pokračujte.

![Image](assets/fr/36.webp)

## Objevení nabídky

Rozhraní Passport má tři hlavní nabídky:


- "*Účet*";
- "*Více*";
- "*Nastavení*".

Mezi těmito nabídkami se pohybujete pomocí šipek doleva a doprava na směrovém panelu.

### *Nabídka "Účet*

V nabídce "*Účet*" najdete hlavní funkce své peněženky Bitcoin. Transakci můžete podepsat buď prostřednictvím fotoaparátu, nebo portu MicroSD.

![Image](assets/fr/37.webp)

Podnabídka "*Nástroje účtu*" nabízí možnosti, jako je ověření adresy, podepsání zprávy nebo nahlédnutí do adres ve vašem portfoliu.

![Image](assets/fr/38.webp)

V podnabídce "*Správa účtu*" můžete svou peněženku Bitcoin připojit k softwaru pro správu peněženky (kterému se budeme věnovat v dalších krocích tohoto návodu) nebo si svůj účet zobrazit a přejmenovat.

![Image](assets/fr/39.webp)

### Více" menu

V nabídce "*Další*" můžete vytvořit nový účet ve svém portfoliu, spojený se stejnou mnemotechnickou frází.

![Image](assets/fr/40.webp)

Můžete také zadat přístupovou frázi BIP39 (viz další část) nebo použít dočasný seed.

![Image](assets/fr/41.webp)

### Nabídka "Nastavení

V nabídce "*Nastavení*" najdete všechna nastavení peněženky a zařízení.

![Image](assets/fr/42.webp)

Podnabídka "*Zařízení*" nabízí možnosti přizpůsobení jasu obrazovky, nastavení prodlevy před automatickým uzamčením, změnu kódu PIN nebo přejmenování zařízení.

![Image](assets/fr/43.webp)

Podnabídka "*Zálohování*" umožňuje exportovat zálohu šifrovaného portfolia, zkontrolovat platnost existující zálohy nebo znovu vyhledat "*Kód zálohy*".

![Image](assets/fr/44.webp)

Podnabídka "*Firmware*" slouží k aktualizaci firmwaru zařízení Passport. Doporučujeme provádět tyto aktualizace pravidelně, abyste mohli využívat nejnovější opravy a funkce.

![Image](assets/fr/45.webp)

Podnabídka "*Bitcoin*" umožňuje změnit zobrazenou jednotku (BTC nebo satoshis), spravovat případnou peněženku Multisig nebo přepnout do režimu "*Testnet*".

![Image](assets/fr/46.webp)

V části "*Pokročilé*" můžete zobrazit slova své mnemotechnické fráze, provádět akce na vložené kartě MicroSD, obnovit tovární nastavení zařízení Passport nebo provést kontrolu pravosti, jak bylo provedeno dříve.

![Image](assets/fr/47.webp)

Můžete aktivovat funkci "*Bezpečnostní slova*", která zvyšuje úroveň zabezpečení tím, že při odemykání zařízení po zadání prvních čtyř číslic kódu PIN zobrazí dvě konkrétní slova. Tato slova, která se uloží během konfigurace, zajistí, že zařízení Passport nebylo vyměněno nebo s ním nebylo manipulováno. V případě pozdějšího zjištění jakýchkoli nesrovnalostí doporučujeme zařízení nepoužívat. Doporučuji vám tuto možnost aktivovat, abyste předešli většině rizik fyzického ohrožení zařízení.

![Image](assets/fr/48.webp)

A konečně podnabídka "*Rozšíření*" umožňuje aktivovat funkce specifické pro určité použití spotřebiče, například protokol Whirlpool coinjoin.

![Image](assets/fr/49.webp)

## Přidání přístupové fráze BIP39

Pokud chcete, můžete před pokračováním přidat přístupovou frázi BIP39. Přístupová fráze BIP39 je volitelné heslo, které si můžete libovolně zvolit a které se přidává k vaší mnemotechnické frázi pro posílení zabezpečení peněženky. Pokud je tato funkce povolena, přístup k vaší peněžence Bitcoin bude vyžadovat jak mnemotechnickou, tak heslovou frázi. Bez obou by bylo nemožné peněženku obnovit.

Před konfigurací této možnosti na vašem Passportu důrazně doporučujeme přečíst si tento článek, abyste plně porozuměli teoretickému fungování přístupové fráze a vyhnuli se chybám, které by mohly vést ke ztrátě vašich bitcoinů:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Chcete-li ji aktivovat, přejděte do nabídky "*Další*" a klikněte na "*Zadat přístupovou frázi*".

![Image](assets/fr/50.webp)

Zadejte svou přístupovou frázi pomocí klávesnice aA1 a nezapomeňte ji jednou nebo vícekrát uložit na fyzické médium (papír nebo kov). Pro tento příklad používám velmi slabou přístupovou frázi, ale vy byste měli zvolit silnou, náhodnou přístupovou frázi, zahrnující všechny typy znaků a dostatečně dlouhou (jako silné heslo).

![Image](assets/fr/51.webp)

Upozorňujeme, že u přístupových hesel BIP39 záleží na velikosti písmen a překlepů. Pokud zadáte přístupovou frázi mírně odlišnou od původně nakonfigurované, Passport neohlásí chybu, ale odvodí jinou sadu kryptografických klíčů, které nebudou těmi, které byly ve vaší původní peněžence.

Proto je důležité si při konfiguraci někde poznamenat otisk hlavního klíče, který vám bude přidělen v dalším kroku. Například s mou přístupovou frází `Plan B Network` je otisk hlavního klíče `745D526B`.

![Image](assets/fr/52.webp)

Při každém odemknutí pasu se musíte vrátit do této nabídky, abyste zadali přístupovou frázi a použili ji v peněžence. Passport neukládá přístupovou frázi.

Při každém odemknutí po zapsání přístupové fráze zkontrolujte na této potvrzovací obrazovce, zda je zadaný otisk prstu stejný jako ten, který jste zapsali při konfiguraci. Pokud ano, je vaše přístupová fráze správná a přistupujete ke správné peněžence Bitcoin. Pokud tomu tak není, jste na špatné peněžence a musíte to zkusit znovu a dávat pozor, abyste neudělali žádnou chybu při zadávání.

Než obdržíte své první bitcoiny do peněženky, **důrazně vám doporučuji provést test obnovy prázdných peněz**. Zaznamenejte si některé referenční informace, jako je vaše xpub nebo první přijímací adresa, a poté vymažte svou peněženku na Passportu, dokud je ještě prázdná (`Nastavení -> Pokročilé -> Vymazat Passport`). Poté se pokuste peněženku obnovit pomocí papírových záloh mnemotechnické fráze a případné přístupové fráze. Zkontrolujte, zda se informace o souboru cookie vygenerované po obnovení shodují s těmi, které jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé. Další informace o tom, jak provést zkušební obnovu, naleznete v tomto dalším návodu :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)

## Konfigurace peněženky v aplikaci Sparrow Wallet

V tomto tutoriálu vám ukážu pokročilé použití aplikace Passport s aplikací Sparrow Wallet. Tato hardwarová peněženka je však kompatibilní také s aplikacemi Envoy (aplikace Foundation), Keeper, BlueWallet, Nunchuk, Specter a mnoha dalšími...

Začněte stažením a instalací aplikace Sparrow Wallet [z oficiálních stránek](https://sparrowwallet.com/) do počítače, pokud jste tak ještě neučinili.

![Image](assets/fr/54.webp)

Před instalací nezapomeňte zkontrolovat pravost a neporušenost softwaru. Pokud nevíte, jak to udělat, přečtěte si tento návod:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Po otevření aplikace Sparrow Wallet klikněte na kartu "*File*" a poté na "*New Wallet*".

![Image](assets/fr/55.webp)

Pojmenujte svou peněženku a klikněte na "*Vytvořit peněženku*".

![Image](assets/fr/56.webp)

Vyberte možnost "*Airgapped Hardware Wallet*".

![Image](assets/fr/57.webp)

Klikněte na "*Scan...*" vedle možnosti "*Passport*". Tím se otevře vaše webová kamera.

![Image](assets/fr/58.webp)

V hardwarové peněžence přejděte do nabídky "*Účet*", vyberte podnabídku "*Správa účtu*" a klikněte na "*Připojit peněženku*".

![Image](assets/fr/59.webp)

V zobrazeném rozevíracím seznamu vyberte možnost "*Sparrow*".

![Image](assets/fr/60.webp)

Pak vyberte možnost "*Single-sig*" pro normální konfiguraci bez multisig.

![Image](assets/fr/61.webp)

Vyberte možnost "*QR kód*".

![Image](assets/fr/62.webp)

Váš pas pak vygeneruje dynamické kódy QR. Pomocí webové kamery počítače je můžete naskenovat do softwaru Sparrow.

![Image](assets/fr/63.webp)

Nyní byste měli vidět svůj xpub a otisk hlavního klíče, který by se měl shodovat s otiskem zobrazeným v pasu při zadávání přístupové fráze. Klikněte na tlačítko "*Použít*".

![Image](assets/fr/64.webp)

Nastavte si silné heslo pro zabezpečení přístupu do peněženky Sparrow. Toto heslo ochrání vaše veřejné klíče, adresy, štítky a historii transakcí před neoprávněným přístupem. Toto heslo je dobré uložit do správce hesel, abyste ho nezapomněli.

![Image](assets/fr/65.webp)

Passport vás poté vyzve k naskenování první adresy příjmu, abyste potvrdili, že import proběhl úspěšně.

![Image](assets/fr/66.webp)

V aplikaci Sparrow přejděte na kartu "*Příjem*" a naskenujte QR kód první adresy.

![Image](assets/fr/67.webp)

Pokud je operace úspěšná, zobrazí se na vašem pasu nápis "*Ověřeno*".

![Image](assets/fr/68.webp)

Tím se potvrdí, že import proběhl úspěšně.

![Image](assets/fr/69.webp)

## Přijímání bitcoinů

Nyní, když je váš pas nastaven, jste připraveni přijmout první saty na vaší nové peněžence Bitcoin. Chcete-li tak učinit, klikněte na Sparrow na nabídku "*Přijmout*".

![Image](assets/fr/70.webp)

Sparrow zobrazí první prázdnou adresu účtenky ve vašem portfoliu. Můžete přidat štítek.

![Image](assets/fr/71.webp)

Před použitím zkontrolujeme adresu na obrazovce Passport, abychom se ujistili, že patří do naší peněženky Bitcoin. V aplikaci Sparrow si můžete QR kód adresy v případě potřeby zvětšit kliknutím na něj. V nabídce "*Účet*" ve službě Passport vyberte možnost "*Nástroje účtu*".

![Image](assets/fr/72.webp)

Klikněte na "*Ověřit adresu*" a naskenujte QR kód zobrazený na Sparrow Wallet.

![Image](assets/fr/73.webp)

Ujistěte se, že adresa zobrazená v pase přesně odpovídá adrese zobrazené v aplikaci Sparrow a že se zobrazuje nápis "*Ověřeno*".

![Image](assets/fr/74.webp)

Nyní ji můžete používat k přijímání bitcoinů. Jakmile je transakce odvysílána v síti, objeví se na Sparrow. Počkejte, až obdržíte dostatek potvrzení, abyste mohli transakci považovat za definitivní.

![Image](assets/fr/75.webp)

## Odeslat bitcoiny

Teď, když máte v peněžence několik sátů, můžete také nějaké poslat. Chcete-li tak učinit, klikněte na nabídku "*UTXOs*".

![Image](assets/fr/76.webp)

Vyberte UTXO, které chcete použít jako vstupy pro tuto transakci, a klikněte na "*Odeslat vybrané*".

![Image](assets/fr/77.webp)

Zadejte adresu příjemce, štítek, který vám připomene účel transakce, a částku, kterou chcete na tuto adresu poslat.

![Image](assets/fr/78.webp)

Upravte sazbu poplatku podle aktuálních podmínek na trhu a klikněte na "*Vytvořit transakci*".

![Image](assets/fr/79.webp)

Zkontrolujte, zda jsou všechny parametry transakce správné, a poté klikněte na tlačítko "*Finalizovat transakci k podpisu*".

![Image](assets/fr/80.webp)

Kliknutím na "*Show QR*" zobrazíte PSBT (*Partially Signed Bitcoin Transaction*). Sparrow transakci sestavil, ale stále mu chybí podpisy k odemčení bitcoinů použitých na vstupu. Tyto podpisy může provést pouze Passport, který hostí váš seed poskytující přístup k soukromým klíčům potřebným k podpisu transakce.

![Image](assets/fr/81.webp)

V aplikaci Passport přejděte do nabídky "*Účet*" a klikněte na "*Podepsat pomocí QR kódu*".

![Image](assets/fr/82.webp)

Naskenujte PSBT (*Partially Signed Bitcoin Transaction*) zobrazený na Sparrow Wallet.

![Image](assets/fr/83.webp)

Zkontrolujte, zda jsou adresa příjemce a odeslaná částka správné, a poté stiskněte potvrzovací tlačítko.

![Image](assets/fr/84.webp)

Zkontrolujte adresu výměny. V mém příkladu žádná není, protože transakce obsahuje jediný výstup.

![Image](assets/fr/85.webp)

Ujistěte se, že poplatek je ten, který jste si vybrali.

![Image](assets/fr/86.webp)

Pokud jsou všechny údaje správné, klikněte na potvrzovací tlačítko a podepište transakci.

![Image](assets/fr/87.webp)

V aplikaci Sparrow Wallet klikněte na "*Scan QR*" a naskenujte QR kód zobrazený na vašem pasu.

![Image](assets/fr/88.webp)

Vaše podepsaná transakce je nyní připravena k odvysílání v síti Bitcoin a zařazení do bloku těžařem. Pokud je vše v pořádku, klikněte na "*Broadcast Transaction*".

![Image](assets/fr/89.webp)

Vaše transakce byla odeslána a čeká na potvrzení.

![Image](assets/fr/90.webp)

Gratulujeme, nyní víte, jak nakonfigurovat a používat aplikaci Passport. Pokud pro vás byl tento návod užitečný, budu vám vděčný, když mi níže zanecháte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji za sdílení!

Další informace naleznete v našem návodu k softwaru Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
