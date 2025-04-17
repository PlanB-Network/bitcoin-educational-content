---
name: Envoy
description: Nastavení a používání pasu s aplikací Envoy
---
![cover](assets/cover.webp)

Envoy je aplikace pro správu peněženky Bitcoin vyvinutá společností Foundation. Je speciálně navržena pro použití s hardwarovou peněženkou Passport.

Passport "*Batch 2*", který představujeme v tomto tutoriálu spolu s aplikací Envoy, je nástupcem edice "*Founder's Edition*". Vyniká prémiovým designem, vysoce kvalitním barevným displejem a ergonomickou fyzickou klávesnicí. Funguje v režimu "*Air-Gap*", což zajišťuje, že soukromé klíče vaší peněženky zůstanou zcela izolované, přičemž komunikace probíhá prostřednictvím karty MicroSD nebo QR kódů. Zařízení je vybaveno vyměnitelnou dobíjecí baterií Nokia BL-5C s kapacitou 1200 mAh. Tato běžně dostupná baterie může být snadno nahrazena, protože model BL-5C lze snadno najít v obchodech.

Co se týče konektivity, je Passport vybaven portem MicroSD, portem USB-C pro nabíjení a zadní kamerou pro snímání QR kódů.

Pokud jde o zabezpečení, Passport obsahuje zabezpečený prvek a zdrojový kód zařízení je zcela otevřený. Nabízí všechny funkce, které se od dobré hardwarové peněženky na bitcoiny očekávají. Všimněte si, že Passport zatím nepodporuje miniskript, ale tato funkce je plánována na druhé čtvrtletí roku 2025.

Za cenu 199 dolarů je Passport považován za špičkovou hardwarovou peněženku, která konkuruje modelům Coldcard Q, Jade Plus, Tezor Safe 5 a špičkovým modelům Ledger.

![Image](assets/fr/01.webp)

Chcete-li spravovat zabezpečenou peněženku v zařízení Passport, máte několik možností. Tato hardwarová peněženka je kompatibilní s většinou softwaru pro správu peněženek na trhu, včetně Sparrow Wallet, Specter Desktop, Nunchuk, Keeper a dalších.

V tomto návodu, který je určen pro začátečníky a středně pokročilé uživatele, se dozvíte, jak používat aplikaci Envoy s aplikací Passport. Je to nejjednodušší způsob, jak využít hardwarovou peněženku na maximum.

Pokud jste pokročilý uživatel a chcete prozkoumat složitější funkce, doporučuji vám podívat se na tento další návod, kde konfigurujeme Passport s peněženkou Sparrow :

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

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

## Stáhnout aplikaci Envoy

Přejděte do obchodu s aplikacemi a stáhněte si aplikaci Envoy :


- V [Obchodě Google Play](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- V [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- Na [F-Cold](https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

Soubor APK si můžete stáhnout také přímo [z repozitáře GitHub nadace](https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Po otevření aplikace vyberte možnost "*Správa pasu*".

![Image](assets/fr/52.webp)

Zvolte, zda chcete aktivovat připojení Tor pro posílení důvěrnosti, a stiskněte tlačítko "*Pokračovat*".

![Image](assets/fr/53.webp)

Pokud je váš Passport již nakonfigurován, vyberte možnost "*Připojit existující Passport*", nebo "*Nastavit nový Passport*", pokud inicializujete hardwarovou peněženku poprvé.

![Image](assets/fr/54.webp)

Přijměte podmínky používání.

![Image](assets/fr/55.webp)

Poté budete vyzváni k ověření pravosti pasu. Klikněte na "*Další*".

![Image](assets/fr/56.webp)

## Startovací pas

Stisknutím tlačítka zapnutí/vypnutí na boku přístroje jej spusťte.

![Image](assets/fr/04.webp)

Stisknutím potvrzovacího tlačítka přejdete do další nabídky.

![Image](assets/fr/05.webp)

V tomto návodu budeme ke správě peněženky zabezpečené pomocí pasu používat službu Envoy. Vyberte možnost "*Envoy App*".

![Image](assets/fr/57.webp)

Klikněte na možnost "*Pokračovat v programu Envoy*".

![Image](assets/fr/58.webp)

Dalším krokem je kontrola zařízení. Tím se potvrdí pravost vašeho pasu a zajistí se, že s ním nebylo při přepravě manipulováno. Budete požádáni o naskenování QR kódu.

![Image](assets/fr/08.webp)

Naskenujte dynamické kódy QR zobrazené v aplikaci pomocí svého pasu. Po dokončení skenování klikněte na "*Další*".

![Image](assets/fr/59.webp)

Poté telefonem naskenujte kód QR zobrazený na pasu.

![Image](assets/fr/60.webp)

Pokud se zobrazí zpráva "*Your Passport is secure*", potvrzuje to, že je vaše hardwarová peněženka pravá. Nyní ji můžete použít k zabezpečení peněženky Bitcoin.

![Image](assets/fr/61.webp)

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

### Bez aplikace Envoy

K tomu použijte kartu MicroSD, která je součástí balení Passportu (nebo jinou kartu), a vložte ji do počítače. Stáhněte si nejnovější verzi firmwaru ze stránek [dokumentace nadace](https://docs.foundation.xyz/firmware-updates/passport/) nebo [jejich úložiště GitHub](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Před instalací do zařízení důrazně doporučujeme zkontrolovat pravost a neporušenost staženého firmwaru. Pokud s tím potřebujete pomoci, podívejte se do tohoto návodu :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### S aplikací Envoy

Druhou, jednodušší možností je použít přímo aplikaci Envoy. Klikněte na "*Stáhnout firmware*".

![Image](assets/fr/62.webp)

K připojení karty MicroSD k telefonu použijte adaptér dodaný s přístrojem Passport.

![Image](assets/fr/63.webp)

V průzkumníku souborů vyberte kartu MicroSD, na kterou chcete uložit firmware.

![Image](assets/fr/64.webp)

Firmware je nyní uložen. Vyjměte kartu MicroSD ze smartphonu a vložte ji do zařízení Passport.

![Image](assets/fr/65.webp)

Otevře se průzkumník souborů Passport. Vyberte soubor `vN.N.N-passport.bin`.

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

Váš Passport byl úspěšně nakonfigurován. Klikněte na potvrzovací tlačítko a pokračujte.

![Image](assets/fr/36.webp)

## Nastavení portfolia v systému Envoy

V tomto návodu vám ukážu, jak používat aplikaci Passport s aplikací Envoy. Tato hardwarová peněženka je však kompatibilní také s aplikacemi Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter a mnoha dalšími...

![Image](assets/fr/66.webp)

Pomocí aplikace Envoy naskenujte QR kód zobrazený na vašem pasu.

![Image](assets/fr/67.webp)

Vaše veřejné klíče jsou nyní importovány do aplikace. Klikněte na "*Ověřit adresu pro příjem*".

![Image](assets/fr/68.webp)

Pomocí pasu naskenujte adresu zobrazenou v systému Envoy.

![Image](assets/fr/69.webp)

Váš cestovní pas potvrdí, zda je peněženka importovaná do systému Envoy platná. Potvrďte to v aplikaci.

![Image](assets/fr/70.webp)

Nyní máte přístup k veřejným informacím o své peněžence na serveru Envoy, ale k utrácení bitcoinů musíte použít svůj pas.

![Image](assets/fr/71.webp)

## Objevte menu Passport

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

Můžete také zadat přístupovou frázi BIP39 nebo použít dočasný seed.

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

## Přijímání bitcoinů

Nyní, když je váš pas nastaven, jste připraveni přijmout první saty na vaší nové peněžence Bitcoin. Chcete-li tak učinit, klikněte v aplikaci Envoy na svůj účet "*Primary 0*".

![Image](assets/fr/72.webp)

Klikněte na tlačítko "*Přijmout*".

![Image](assets/fr/73.webp)

Aplikace Envoy zobrazí první volnou adresu v peněžence. Než ji použijeme, zkontrolujme adresu na obrazovce Passport, abychom se ujistili, že skutečně patří do naší peněženky Bitcoin. V nabídce "*Účet*" ve vašem Passportu vyberte možnost "*Nástroje účtu*".

![Image](assets/fr/74.webp)

Klikněte na "*Ověřit adresu*" a poté naskenujte QR kód zobrazený na zařízení Envoy.

![Image](assets/fr/75.webp)

Ujistěte se, že adresa zobrazená v pase přesně odpovídá adrese zobrazené v aplikaci Sparrow a že se zobrazuje nápis "*Ověřeno*".

![Image](assets/fr/76.webp)

Nyní ji můžete používat k přijímání bitcoinů. Jakmile je transakce odvysílána v síti, objeví se na Envoy. Počkejte, až obdržíte dostatečný počet potvrzení, abyste mohli transakci považovat za definitivní.

![Image](assets/fr/77.webp)

## Odeslat bitcoiny

Teď, když máte v peněžence pár sátů, můžete také nějaké poslat. To provedete kliknutím na tlačítko "*Odeslat*".

![Image](assets/fr/78.webp)

Zadejte adresu příjemce buď přímo vložením, nebo naskenováním QR kódu pomocí fotoaparátu chytrého telefonu.

![Image](assets/fr/79.webp)

Určete částku, kterou chcete odeslat, a klikněte na "*Potvrdit*".

![Image](assets/fr/80.webp)

Vyberte poplatek za transakci podle aktuální situace na trhu a poté zkontrolujte informace o transakci. Pokud je vše v pořádku, klikněte na "*Podepsat pasem*".

![Image](assets/fr/81.webp)

Přidejte k transakci štítek, abyste měli jasný záznam o jejím účelu.

![Image](assets/fr/82.webp)

Envoy poté zobrazí PSBT (*Částečně podepsaná transakce Bitcoin*). Aplikace transakci vytvořila, ale stále jí chybí podpis(y) k odemčení bitcoinů použitých na vstupu. Tyto podpisy může provést pouze Passport, který hostí váš seed poskytující přístup k soukromým klíčům potřebným k podpisu transakce.

![Image](assets/fr/83.webp)

V aplikaci Passport přejděte do nabídky "*Účet*" a klikněte na "*Podepsat pomocí QR kódu*".

![Image](assets/fr/84.webp)

Naskenujte PSBT (*Partially Signed Bitcoin Transaction*) zobrazenou na Envoy.

![Image](assets/fr/85.webp)

Zkontrolujte, zda jsou adresa příjemce a odeslaná částka správné, a poté stiskněte potvrzovací tlačítko.

![Image](assets/fr/86.webp)

Zkontrolujte adresu výměny. V mém příkladu žádná není, protože transakce obsahuje jediný výstup.

![Image](assets/fr/87.webp)

Ujistěte se, že poplatek je ten, který jste si vybrali.

![Image](assets/fr/88.webp)

Pokud jsou všechny údaje správné, klikněte na potvrzovací tlačítko a podepište transakci.

![Image](assets/fr/89.webp)

Váš pas zobrazuje podepsanou transakci ve formě kódu QR.

![Image](assets/fr/90.webp)

V aplikaci Envoy klikněte na ikonu QR kódu a poté naskenujte PSBT zobrazený na obrazovce pasu.

![Image](assets/fr/91.webp)

Naposledy zkontrolujte údaje o transakci. Pokud je vše v pořádku, stiskněte tlačítko "*Odeslat transakci*", čímž ji odešlete do sítě Bitcoin.

![Image](assets/fr/92.webp)

Vaše transakce nyní čeká na potvrzení. Její stav můžete sledovat přímo ze svého účtu.

![Image](assets/fr/93.webp)

Gratulujeme, nyní víte, jak nastavit a používat aplikaci Passport s aplikací Envoy. Pokud pro vás byl tento návod užitečný, budu vám vděčný, když mi níže zanecháte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji za sdílení!

Další informace naleznete v našem návodu k softwaru Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
