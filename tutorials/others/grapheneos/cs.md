---
name: GrapheneOS

description: Tutoriál k Graphene OS
---

> "[GrapheneOS](https://grapheneos.org/) je mobilní operační systém zaměřený na soukromí a bezpečnost s kompatibilitou s aplikacemi pro Android, vyvíjený jako neziskový open source projekt."

GrapheneOS, původně založený v roce 2014 jako 'CopperheadOS', je založen na tradičním kódu Androidu (AOSP), ale s mnoha změnami a vylepšeními zaměřenými na zlepšení soukromí a bezpečnosti uživatelů. GrapheneOS dává uživateli kontrolu nad jejich telefonem, nikoli velkým technologickým společnostem.

### Obsah:

- Úvod
- Příprava
- Instalace
- Alternativní aplikace
- Nevýhody
- Užitečné informace

Průvodce od https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md

## Proč používat GrapheneOS?

Moderní telefony jsou zařízení za 500-1000 dolarů určená pro sledování a sběr dat. Každý aspekt našeho života jimi prochází a bohužel mnoho těchto dat je ve formě nebo jiné sdíleno s třetími stranami.
GrapheneOS je speciálně vyvinutý k omezení tohoto sdílení dat a zlepšení bezpečnosti vašeho zařízení před potenciálními vektory útoků. Něco jako účet GrapheneOS neexistuje. K stahování aplikací nebo interakci s OS nepotřebujete žádný účet. Jednoduše řečeno, nejste produkt.

GrapheneOS poskytuje dodatečnou bezpečnost vašemu Android zážitku prostřednictvím několika jednoduchých základních principů.

1. **Redukce útočné plochy** - Odstranění zbytečného kódu (nebo bloatware).
2. **Prevence vystavení zranitelnostem** - Umožnění uživateli dostatečnou granularitu pro výběr kompromisů, se kterými jsou pohodlní.
3. **Omezení sandboxu** - GrapheneOS posiluje stávající sandboxy Androidu, dále omezujíc přístup každé aplikace ke komunikaci se zbytkem vašeho telefonu.

Dozvědět se více o technických detailech sady funkcí GrapheneOS [zde](https://grapheneos.org/features).

### Ulehčení přechodu

Pokud jste byli léta zakořeněni v ekosystému Google nebo Apple, myšlenka ztráty veškerého toho pohodlí přes noc může být děsivá. Ale s pečlivě zváženými rozhodnutími ohledně instalace aplikací (o kterých se později zmíníme), lze mnoho očekávaných obtíží snížit nebo odstranit.

Ačkoliv se alternativy stávají čím dál tím lepšími, myšlenka takové změny může být stále odrazující. Pokud se ocitnete v této situaci, moje nejlepší rada je používat vaše nové zařízení s GrapheneOS vedle vašeho stávajícího telefonu po určitou dobu. Odtud můžete pomalu přestat používat 2-3 aplikace týdně, dokud nezjistíte, že sáhnete pouze po vašem zařízení s GrapheneOS.

Pokud se rozhodnete pro tento přístup, buďte k sobě striktní a co nejrychleji ukončete svou závislost na sledovaných alternativách. My lidé jsme líní a často si vybereme cestu nejmenšího odporu. Pamatujte, proč jste se rozhodli pro změnu.

**Místo placení vašimi osobními daty jste se rozhodli platit svým časem a někdy i tvrdě vydělanými penězi (v závislosti na alternativních aplikacích, které instalujete).**

## Začínáme

GrapheneOS je v současné době ve výrobě pouze pro _(poněkud ironicky)_ řadu telefonů [Google Pixel](https://grapheneos.org/faq#supported-devices). To má ovšem svůj dobrý důvod. Telefony Pixel nabízejí nejlepší hardwarovou bezpečnost, která doplňuje práci vykonanou na zpevnění OS. To zahrnuje věci jako izolace konkrétních komponent a ověřený start.

### Výběr zařízení

Při výběru Pixelu, na který chcete nainstalovat GrapheneOS, se ujistěte, že zkontrolujete, jak dlouho zařízení bude nadále dostávat výchozí [aktualizace zabezpečení](https://support.google.com/pixelphone/answer/4457705?hl=cs#zippy=%2Cpixel-xl-a-a-g-a-g).
V době psaní je Pixel 6a nejlevnějším modelem dostupným s dobrým dlouhodobým supportem, zaručeným do července 2027. Pokud si vyberete tento model, OEM odemčení nebude fungovat s verzí továrního OS. Budete ho muset aktualizovat na vydání z června 2022 nebo pozdější prostřednictvím aktualizace přes síť. Po aktualizaci budete také muset zařízení obnovit do továrního nastavení, aby bylo možné opravit OEM odemčení. Všechny ostatní modely, které nejsou uzamčeny operátorem, budou připraveny na GrapheneOS hned po vybalení.

Při výběru zařízení se také budete chtít ujistit, že kupujete odemčenou verzi. Někteří operátoři, jako je Verizon, dodávají své jednotky s uzamčeným bootloaderem, což úplně brání následujícímu procesu.

### Instalace GrapheneOS

Web installer GrapheneOS celý proces značně usnadňuje a umožňuje ho dokončit komukoli za méně než 10 minut.
Následující pokyny jsou zjednodušenou verzí převzatou z výše uvedeného odkazu.

Vše, co potřebujete:

- Pixel
- USB kabel pro propojení telefonu s počítačem
- Počítač pro spuštění webového prohlížeče (jakýkoli prohlížeč založený na Chromium: Chrome, Edge, Brave atd.)

1. Prvním krokem je jít do **Nastavení** > **O telefonu** a opakovaně klepat na číslo sestavení, dokud neuvidíte, že je aktivován **'Vývojářský režim'**.
2. Dále přejděte do **Nastavení** > **Systém** > **Možnosti pro vývojáře** a povolte **'OEM odemčení'**.
3. Nyní restartujte zařízení a při zapínání telefonu držte stisknuté tlačítko snížení hlasitosti.
4. Připojte telefon k notebooku a pokud bude vyžádáno autorizace, povolte spojení.
5. Na stránce web installeru klikněte na 'Odemknout bootloader'.
6. Poté uvidíte změnu možností telefonu. Použijte tlačítko hlasitosti pro změnu výběru na `odemknout` a tlačítko napájení pro potvrzení.
7. Dále na stránce web installeru klikněte na stáhnout vydání.
8. Po úplném stažení přejděte k dalšímu kroku a klikněte na 'Flash vydání'. To zabere minutu nebo dvě a telefon nemusíte vůbec dotýkat.
9. Nakonec přejděte k dalšímu kroku web installeru a klikněte na **Zamknout Bootloader**. Budete potřebovat změnit výběr a potvrdit tlačítkem napájení stejným způsobem jako dříve v procesu.
10. Když uvidíte slovo `Start`, potvrďte to tlačítkem napájení a zařízení se spustí do vašeho nového operačního systému bez Google.

![obrázek](assets/2.webp)

Úvodní obrazovka GrapheneOS

_Po počátečním spuštění a nastavení je dobré praxí zakázat OEM odemčení v Nastavení > Systém > Možnosti pro vývojáře._

_Můžete také zvážit další, nepovinný, ale doporučený krok ověření instalace prostřednictvím aplikace Auditor. K dokončení tohoto kroku budete potřebovat další Android telefon s nainstalovanou aplikací. Pokyny k tomu najdete [zde](https://attestation.app/tutorial)._

![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Video detailně popisující výše uvedené jednoduché kroky

Pokud se vám tyto jednoduché kroky zdají příliš složité, můžete zvážit koupi Pixelu s předinstalovaným softwarem GrapheneOS [zde](https://ronindojo.io/en/roninmobile). Mějte na paměti, že tímto poskytovateli dáváte malou míru důvěry.

### Předinstalované aplikace

Nyní, když jste nastaveni, můžete si všimnout, jak málo aplikací GrapheneOS obsahuje po první instalaci. Ve výchozím nastavení budete mít tyto aplikace nainstalované:

![obrázek](assets/3.webp)

Předinstalované aplikace
Jediné dva pojmy, se kterými nemusíte být obeznámeni, jsou 'Auditor' a 'Vanadium'.
- '[Auditor app](https://play.google.com/store/apps/details?id=app.attestation.auditor) využívá zabezpečení založené na hardwaru k ověření identity zařízení spolu s autentičností a integritou operačního systému. Aplikace ověří, že zařízení běží na původním operačním systému s uzamčeným bootloaderem a že nedošlo k žádné manipulaci s operačním systémem.'
- [Vanadium](https://github.com/GrapheneOS/Vanadium) je varianta webového prohlížeče Chromium zpevněná z hlediska soukromí a bezpečnosti.

## Přizpůsobení

Nastavení telefonu je osobní věc, ale zde jsou některé z prvních položek, které měním při instalaci GrapheneOS, abych se cítil více jako doma.

### Nastavení tapety a aktualizace tématu

Přejděte do Nastavení > Tapeta a styl. Odtud:

- Aktualizuji pozadí domovské obrazovky a uzamčené obrazovky obrázky staženými z webu.
- Vyberu akcentové barvy používané v celém uživatelském rozhraní.
- Zapnu tmavý režim.

### Zobrazení procenta baterie

Přejděte do **Nastavení** > **Baterie**, poté zapněte **Zobrazit procento baterie** na stavovém řádku.

### Import kontaktů

**Z jiného telefonu s Androidem** - Přejděte do aplikace Kontakty a hledejte možnost Exportovat do VCF.

**Z iOS** - Použijte aplikaci jako Export Contact a použijte možnost exportu 'vCard' pro export souboru VCF.
Jakmile máte soubor VCF, můžete jej přenést do vašeho zařízení GrapheneOS pomocí možnosti externího úložiště, jako je microSD karta nebo USB disk. Pokud žádný z těchto nemáte po ruce, můžete zvolit sdílení prostřednictvím jedné z mnoha aplikací uvedených níže.

![obrázek](assets/4.webp)

Personalizovaná domovská obrazovka

## Alternativní aplikace

Aby byl váš telefon užitečný, budete chtít nainstalovat nějaké aplikace! Následující možnosti jsou zahrnuty, protože jsem je všechny osobně používal nebo protože dostávají silná doporučení od širší komunity zaměřené na soukromí. Existuje mnoho dalších skvělých alternativ, které nejsou zmíněny, a [Awesome Privacy](https://awesome-privacy.xyz) nabízí neuvěřitelně rozsáhlý seznam aplikací zachovávajících soukromí pro všechny typy zařízení.

Jen proto, že aplikace je Free and Open Source Software (FOSS), neznamená, že je bez potenciálních úniků soukromí. Použijte [Exodus](https://reports.exodus-privacy.eu.org/en/) k zjištění, jak vaše preferované aplikace obstojí v jejich auditech soukromí.

### F-Droid

[F-Droid](https://f-droid.org/) je instalovatelný katalog FOSS aplikací pro Android. Klient usnadňuje procházení, instalaci a aktualizaci aplikací na vašem zařízení. Stojí za zmínku, že aktualizace přes F-Droid mohou být někdy pomalejší než u jiných obchodů s aplikacemi. To je hlavně závislé na tom, zda je aplikace nalezena prostřednictvím hlavního repozitáře F-Droid nebo vlastního.

Pro instalaci F-Droid jednoduše přejděte na jejich webové stránky prostřednictvím prohlížeče na vašem telefonu GrapheneOS a klepněte na stáhnout. Tím se stáhne soubor `.apk`. Poté vás bude dotázáno, zda si přejete aplikaci nainstalovat.

Kromě aplikací nalezených ve výchozím repozitáři ve F-Droid, mnoho projektů Open Source také hostuje vlastní repozitář, který lze přidat v nastavení aplikace F-Droid. Pokud tomu tak je, dotčený projekt vás provede velmi jednoduchými kroky potřebnými k dosažení toho na jejich webových stránkách.

![obrázek](assets/5.webp)

Domovská obrazovka F-Droid

### Aurora Store
[Aurora Store](https://auroraoss.com/) je FOSS verze obchodu Google Play. Aurora vypadá a funguje velmi podobně jako tradiční Play Store a umožňuje vám stahovat a aktualizovat jakoukoli aplikaci, kterou byste normálně našli přes možnost Google.

Klíčovou funkcí Aurory je anonymní přihlášení. To znamená, že si můžete stáhnout jakékoli vaše oblíbené aplikace, které nejsou dostupné přes F-Droid nebo přímé APK, aniž byste museli být přihlášeni k vašemu účtu Google.

Než se rozhodnete udělat z toho vaši výchozí možnost instalace, pamatujte, že mnoho aplikací, od kterých se snažíme odejít, bylo nainstalováno z obchodu Play. Jen proto, že jsou přístupné z Aurory, to nemění fakt, že některé mohou obsahovat vestavěné sledovací funkce. Nebude to vždy možné, ale kdykoli to jde, hledejte alternativu F-Droid před stahováním přes Auroru.

Pro instalaci Aurory jednoduše vyhledejte 'Aurora Store' v F-Droid.

Aurora také má některé potenciální vektory útoku, jelikož "anonymní účty" jsou ve skutečnosti vytvořeny a kontrolovány Aurorou. Mohli by, teoreticky, poskytovat škodlivé aktualizace nebo posílat aplikace na váš telefon, i když byste stále museli na zařízení přijmout výzvu k instalaci. Aurora také občas má problémy s aplikacemi, které se nezobrazují kvůli špatnému určení regionu a zařízení. To se obvykle dá obejít následujícími kroky.

**Top tip** - Někdy může Aurora Store zažívat omezení rychlosti, které omezuje vaši schopnost vyhledávat a instalovat aplikace. Aby jste toto obešli, jděte do **Nastavení** > **Aplikace** > **Aurora** > **Otevřít jako výchozí**, poté přidejte doménu `play.google.com`. Nyní, kdykoli přejdete na webovou stránku produktu nebo služby, která má odkaz 'Stáhnout přes Play Store', klepnutím na něj otevřete danou aplikaci v Aurorě, abyste ji mohli stáhnout.

![image](assets/6.webp)

Domovská obrazovka Aurora Store

### APK Stahování

Aplikace na Androidu lze také stahovat a instalovat prostřednictvím souboru `.apk`. To je skvělá alternativa, která nevyžaduje žádné třetí strany obchody s aplikacemi, stačí stáhnout soubor přímo z webové stránky projektu nebo služby nebo z GitHub repozitáře.

Nevýhodou tohoto přístupu je, že nedostanete automatické aktualizace, takže budete muset sledovat komunikační kanály této služby, abyste se dozvěděli o nových verzích. Existuje však skvělý projekt nazvaný Obtanium, který má za cíl toto řešit. [Obtainium](https://github.com/ImranR98/Obtainium) vám umožňuje instalovat a aktualizovat Open-Source aplikace přímo ze stránek s vydáními a dostávat oznámení, když jsou k dispozici nové verze.

![image](assets/7.webp)

Náhled Obtanium

### Webové Aplikace

V případech, kdy byste mohli chtít službu používat jen zřídka a nechcete stahovat nativní aplikaci, můžete jednoduše přistupovat k webové verzi. Mnoho webových stránek dnes také nabízí podporu Progressive Web App (PWA). To znamená, že si můžete přidat konkrétní webovou stránku (např. Twitter.com) na domovskou obrazovku vašeho telefonu. Pak když na ikonu klepnete, otevře se jako aplikace na celou obrazovku bez obvyklých rozptýlení, které přicházejí s typickým prohlížečem. Níže můžete vidět příklad, jak to vypadá.

Pro dosažení tohoto ve Vanadiu, nativním prohlížeči GrapheneOS, jednoduše přejděte na webovou stránku dle výběru, klepněte na tři svislé tečky v pravém horním rohu obrazovky a poté klepněte na **'Přidat na domovskou obrazovku'**.

Jedinou nevýhodou tohoto přístupu je, že protože je to jen záložka webové stránky, nedostanete žádnou formu oznámení. I když někteří by to mohli vidět jako pozitivum!

![image](assets/8.webp)

Twitter PWA

### Webové Prohlížeče
S předbalenou možností, Vanadium, opravdu nemůžete šlápnout vedle. Aplikace se chová identicky jako jakýkoliv jiný mobilní prohlížeč, který jsem zkoušel, a nikdy jsem neměl žádné problémy s kompatibilitou.
Pro případy, kdy potřebujete přistupovat k nativním `.onion` stránkám Tor, můžete si přímo z jejich [webové stránky](https://www.torproject.org/download/#android) nebo přes F-Droid stáhnout APK prohlížeče Tor.

### VPN

Pro ochranu vaší online aktivity před zvědavým poskytovatelem internetových služeb (ISP) je dobrá volba aplikace Virtual Private Network (VPN). VPN posílá váš internetový provoz šifrovaným tunelem na sdílenou IP adresu kontrolovanou poskytovatelem VPN služby, aby zajistila, že vaše aktivita zařízení nemůže být spojena s vámi.

Následují 3 dobře respektované možnosti, které vám umožní platit za službu v Bitcoinu a bez poskytnutí jakýchkoli osobních informací. Všechny 3 možnosti jsou dostupné přes F-Droid.

- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)

### Zasílání zpráv

V posledních letech se objevilo mnoho řešení pro šifrované zasílání zpráv. Problém ale zůstává, pokud máte nainstalovanou nejlepší a nejprivátnější možnost na svém telefonu, ale nemáte žádné kontakty, které by ji používaly, jaký to má smysl?

Většina lidí, které nezajímá prostor soukromí, pravděpodobně používá WhatsApp nebo iMessage. První jmenovaný lze stáhnout přes Aurora Store, ale ten druhý na GrapheneOS (samozřejmě!) fungovat nebude.

- [Signal](https://signal.org/) je jedním z populárnějších poslů s šifrováním end-to-end (E2EE), který má silnou historii a bohatou sadu funkcí. Signal vyžaduje pro registraci telefonní číslo, takže pokud plánujete chatovat s lidmi, kterým byste raději nezveřejnili své telefonní číslo, možná byste měli zvážit některé alternativy. Signal musí být stažen přes Aurora Store.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) je poměrně nový E2EE posel. Nevyžaduje uživatelské ID, telefonní číslo ani osobní informace. Lidé vás najdou skenováním vašeho osobního QR kódu nebo návštěvou vašeho jedinečného odkazu. Simplex také umožňuje pokročilým uživatelům provozovat vlastní server, čímž dále snižuje závislost na jakékoli centralizované entitě. Simplex nemá desktopového klienta, takže nemusí být vhodný, pokud je pro vás prioritou více zařízení. Simplex pro Android je dostupný přes F-Droid.
- [Threema](https://threema.ch/en/faq/libre_installation) nabízí podobný zážitek jako Simplex, ale existuje již déle a v důsledku toho působí trochu více vypolírovaně. Threema není zdarma, doživotní licence stojí 4,99 USD a lze ji koupit za Bitcoin. Threema nabízí webového klienta a nativní desktopové aplikace. Aplikace pro Android je dostupná přes F-Droid.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) je neoficiální FOSS fork oficiální aplikace Telegram pro Android. Telegram má šifrované 'tajné chaty' E2EE, ale výchozí možnost není soukromá. Telegram FOSS lze stáhnout z F-Droid.

![obrázek](assets/9.webp)
Vlevo: Threema
Vpravo: Simplex

### Média
- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) je multiplatformní klient Spotify, který nevyžaduje prémiový účet. Spotube je dostupný přes F-Droid.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) je fantastická aplikace pro streamování jakékoli hudby z YouTube Music zdarma. ViMusic je dostupný z F-Droid.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) nabízí zážitek z YouTube bez otravných reklam a pochybných oprávnění. S NewPipe můžete odebírat kanály, poslouchat na pozadí a dokonce stahovat pro offline zhlédnutí. NewPipe je přístupný přes F-Droid.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) je přehrávač podcastů, který vám umožní odebírat a spravovat všechny vaše oblíbené pořady. AntennaPod je dostupný přes F-Droid.

![obrázek](assets/11.webp)

Vlevo: Spotube
Vpravo: ViMusic

### Mapy

Pokud chcete mít hlasovou asistenci při řízení a používání mapové aplikace v GrapheneOS, budete muset nainstalovat [RHVoice](https://rhvoice.org/installation/) a [nakonfigurovat](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available) jej.

- [Magic Earth](https://www.magicearth.com/) je alternativa map, která podporuje navigaci zatáčka po zatáčce, 3D a offline mapy. Magic Earth lze stáhnout z Aurora Store.
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) je alternativa map pro cestovatele, turisty, turisty pěší a cyklisty založená na datech OpenStreetMap získaných od uživatelů. Jedná se o soukromí zaměřený, open-source fork aplikace Maps.me (dříve známé jako MapsWithMe). Podporuje 100% funkcí bez aktivního internetového připojení a lze jej stáhnout z F-Droid.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) je další skvělá alternativa map, která podporuje všechny výše uvedené funkce.

![obrázek](assets/13.webp)

Vlevo: Magic Earth
Vpravo: Organic Maps

### Email

- [Proton Mail](https://proton.me/mail) nabízí bezplatnou soukromou e-mailovou službu, která podporuje auditované E2EE. Proton také nabízí placenou verzi, která podporuje vlastní domény a [aliasy](https://proton.me/support/creating-aliases). Proton Mail lze stáhnout jako přímý APK soubor nebo přes Aurora.
- [Tutanota](https://tutanota.com/) nabízí stejné funkce jako Proton Mail, včetně volitelných placených služeb a lze ji stáhnout jako přímý APK soubor nebo přes F-Droid.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) je open source e-mailový klient, který funguje s prakticky každým poskytovatelem e-mailu. Podporuje více účtů, sjednocenou doručenou poštu a standard šifrování OpenPGP.

![obrázek](assets/15.webp)

Vlevo: Proton Mail
Vpravo: Tutanota

### Produktivita

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) je program pro synchronizaci souborů. Synchronizuje soubory mezi dvěma nebo více zařízeními v reálném čase, bezpečně chráněné před zvědavými očima. Vaše data jsou pouze vaše a vy si zasloužíte rozhodnout, kde budou uložena, zda budou sdílena s nějakou třetí stranou a jak budou přenášena přes internet. Syncthing je dostupný přes F-Droid.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) propojí všechna vaše zařízení, aby mezi sebou snadno komunikovala, když jsou připojena k vaší domácí síti. Snadno posílejte soubory, fotografie, data schránky mezi všemi vašimi zařízeními (i na iOS!). KDE Connect lze stáhnout z F-Droid.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) je aplikace pro šifrované poznámky E2EE pro synchronizaci vašich myšlenek a seznamů úkolů napříč všemi vašimi zařízeními. Jejich bezplatný plán by měl pokrýt většinu osobních případů použití. Notesnook je dostupný na F-Droid.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) je velmi podobný Notesnook, ale vyžaduje placený plán pro srovnatelnou sadu funkcí. Standard Notes je dostupný prostřednictvím F-Droid.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) je klávesnicová aplikace, která vám umožní přizpůsobit si prakticky cokoli, co si dokážete představit, pokud jde o vaše psaní na telefonu. Lze ji stáhnout přes F-Droid.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) je výchozí aplikace klávesnice od Google. Podle mé zkušenosti nabízí zdaleka nejlepší zážitek z psaní a swipování. Pokud si tuto aplikaci stáhnete, ujistěte se, že úplně zakážete všechna oprávnění související se sítí. Lze ji stáhnout přes Aurora.

![obrázek](assets/17.webp)

Vlevo: Notesnook
Vpravo: KDE Connect

### Životní styl

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) je krásně navržená Open Source aplikace pro počasí dostupná přes F-Droid. Podporuje také mnoho různých velikostí widgetů, takže můžete vidět počasí ve vaší vybrané lokalitě přímo z vaší domovské obrazovky.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) je Open Source a soukromí chránící překladová aplikace, která podporuje více než 200 jazyků. Translate You je dostupný přes F-Droid.
- [Proton Calendar](https://proton.me/calendar/download) je jednoduchý kalendář s E2EE, který bezproblémově spolupracuje s vašimi účty Proton email. Proton Calendar lze stáhnout jako APK nebo přes obchod Aurora.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) je aplikace pro zobrazování a ukládání palubních lístků, kupónů, vstupenek do kina a členských karet atd. Stačí stáhnout příslušný soubor `pkpass` nebo `espass` a otevřít aplikací. PassAndroid je dostupný přes F-Droid.

![obrázek](assets/19.webp)
Vlevo: Geometric Weather
Vpravo: Proton Calendar

### Bezpečnost/Soukromí

- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) nabízí bezplatné řešení správce hesel s E2EE pro všechna vaše zařízení napříč platformami. Jejich placená služba umožňuje integraci kódů 2FA do aplikace. Serverová část Bitwarden může být hostována samostatně a aplikace pro Android je dostupná přes F-Droid.
- [Proton Pass](https://proton.me/pass/download) nabízí podobnou bezplatnou službu jako Bitwarden, ale zákazníci [Proton Unlimited](https://proton.me/pricing) mají přístup k dalším pokročilým funkcím. Proton Pass je dostupný přes APK nebo Aurora.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) je aplikace pro dvoufaktorovou autentizaci pro systémy využívající protokoly jednorázových hesel. Tokeny lze snadno přidat skenováním QR kódu. FreeOTP je dostupný přes F-Droid.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) je bezplatná, bezpečná a open source aplikace pro Android pro správu vašich tokenů pro dvoufázové ověření pro vaše online služby. Aegis je dostupný přes F-Droid.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) je placená, multiplatformní služba, která šifruje vaše data lokálně, takže je můžete bezpečně nahrávat na váš oblíbený cloudový servis. Cryptomator lze stáhnout přes F-Droid.

![obrázek](assets/21.webp)
Vlevo: Proton Pass
Vpravo: Bitwarden

### Cloudová řešení

- [Proton Drive](https://proton.me/drive/download) je placené E2EE cloudové řešení pro zálohování a ukládání všech vašich souborů. V době psaní právě oznámili desktopového klienta pro Windows, ale uživatelé Mac a Linux musí nadále používat webovou verzi pro synchronizaci ze svých počítačů (zatím). Android klient je dostupný jako APK nebo přes Aurora.
- [Skiff](https://skiff.com/download) také nabízí placené E2EE cloudové úložiště a nástroje pro spolupráci na souborech. Nabízejí desktopového klienta pro Mac a Windows (stejně jako webovou aplikaci) a jejich Android klienty musí být staženy z Aurora.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) nabízí plně vybavené cloudové řešení pro spolupráci, synchronizaci mezi zařízeními a ukládání souborů. Pokročilejší uživatelé si mohou vybrat samostatné hostování jejich Free and Open Source softwaru na libovolném hardwaru, který si zvolí. Android klienti mohou být staženi přes F-Droid.
- [Cryptpad](https://cryptpad.fr/) nabízí bezplatnou, webovou, E2EE alternativu k Google Docs.

![obrázek](assets/23.webp)

Proton Drive

## Nevýhody

Open Source a alternativy chránící soukromí k aplikacím technologických konglomerátů, na které jste si zvykli používat, jsou hojné a některé z nich jsou často lepší než uzavřené zdroje plné špehovacího softwaru.

Nicméně při přechodu na GrapheneOS jsou některá pohodlí, která musíte obětovat, protože neexistují žádné alternativy. Patří mezi ně:

- **Apple CarPlay/Android Auto** - Budete muset zůstat u dobrého starého Bluetooth, USB nebo Aux.
- **Apple/Google Pay** - Většina lidí stejně nosí svou peněženku s sebou!
- **Bankovní aplikace** - Ne že by tyto vůbec nefungovaly. Některé fungují dokonale. Jiné fungují pouze s povolenými Google Play Services (více o tom níže) a další vůbec nefungují. Přečtěte si zprávu o vaší bance [zde](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) a zjistěte aktuální stav. Nebojte se, pokud je vaše banka na seznamu těch, které nefungují, pamatujte, že můžete jednoduše uložit URL jako webovou aplikaci na vaší domovskou obrazovku.
- **Push notifikace** - Většina aplikací, které vám posílají aktualizace, když nepoužíváte konkrétní aplikaci, to dělá prostřednictvím Google Play Services. Ty nejsou ve výchozím nastavení nainstalovány s GrapheneOS, takže pokud zjistíte, že nejste okamžitě informováni, když vám váš přítel pošle e-mail, pravděpodobně to je důvod. Dobrou zprávou je, že některé z výše uvedených aplikací implementovaly vlastní pozadové spojení pro pravidelnou kontrolu aktualizací a poté vám poskytnou notifikaci, pokud je to potřeba.

### Sandboxed Google Play
GrapheneOS má kompatibilní vrstvu, která nabízí možnost instalovat a používat oficiální vydání Google Play ve standardním sandboxu aplikací. Google Play na GrapheneOS nezískává žádná speciální přístupová práva nebo privilegia oproti obejití sandboxu aplikací a získání obrovského množství vysoce privilegovaného přístupu.

Pokud si bez těch push notifikací pro vaši oblíbenou aplikaci nebo určité "nezbytné" aplikace bez Play Services nedokážete představit život, GrapheneOS vám umožňuje tyto služby nainstalovat v úplně izolovaném prostředí. Po instalaci tyto služby nepotřebují k fungování žádný účet Google a jejich oprávnění lze pečlivě kontrolovat.

Než se rozhodnete tyto nainstalovat hned první den, vyzývám vás, abyste zjistili, jak daleko se dostanete bez nich. Pravděpodobně budete překvapeni, kolik aplikací funguje naprosto normálně i bez nich.

Pokud je chcete nainstalovat, jednoduše klepněte na předinstalovanou aplikaci 'Aplikace' a poté na 'Služby Google Play'. Zvažte jejich instalaci společně s těmi méně soukromými aplikacemi, bez kterých se neobejdete, v úplně odděleném uživatelském profilu, aby byla zajištěna další úroveň oddělení od zbytku vašeho telefonu.

![obrázek](assets/24.webp)

Instalační obrazovka Služeb Google Play

### Profily

GrapheneOS vám umožňuje mít oddělený telefonní zážitek uvnitř vašeho telefonu. Další profily mohou instalovat vlastní aplikace a služby a nemohou přistupovat k žádným souborům nebo datům z účtu vlastníka.
Pokud máte jen jednu nebo dvě z těch nezbytných aplikací, které vyžadují Služby Google Play, ale používáte je jen velmi zřídka, instalace těchto aplikací společně se Službami Google Play v odděleném profilu může být skvělý nápad, jak dále posílit jakékoli malé soukromí, které zůstává tím, že je necháte běžet v profilu vlastníka.

Více o tomto případu použití si můžete přečíst [zde](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).

Pokud se rozhodnete přidat oddělený profil, aby vyhovoval vašemu případu použití, aplikace [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) by vám mohla být užitečná. Insular vám umožňuje snadno klonovat kteroukoli z vašich stávajících aplikací do nového profilu bez nutnosti použít jakoukoli z tradičních cest instalace zmíněných dříve v tomto průvodci. Insular také umožňuje rychle "zmrazit" kteroukoli z těchto aplikací, aby úplně zakázal veškeré jejich pozadí služby.

![obrázek](assets/24.webp)

Obrazovka správy uživatelských profilů

### e-SIM

Pokud chcete posunout soukromí vašeho telefonu na další úroveň a mít mobilní službu, která není spojena s vaší skutečnou identitou, eSIM by pro vás mohl být řešením. eSIM je virtuální SIM, kterou si můžete zakoupit online a přidat do svého telefonu prostřednictvím QR kódu. Společnosti, které nabízejí takové služby a lze za ně platit anonymně Bitcoinem, zahrnují [Silent.Link](https://silent.link/) a [Bitrefill](https://www.bitrefill.com/gb/en/esims/).

eSIM by neměly být považovány za kompletní řešení pro soukromí telefonu. Mohou být užitečným nástrojem, pokud jsou ve správných rukou, ale prosím, prověřte [kompromisy](https://grapheneos.org/faq#cellular-tracking) používání jakéhokoli typu mobilní služby, pokud je vaším záměrem úplně se "odpojit".

Pro provozování eSIM v GrapheneOS musí být nainstalovány izolované Služby Google Play.

## Zálohy
Po nastavení vašeho nového Pixel telefonu bez Google je dobré si vytvořit zálohu. Tato záloha vám umožní obnovit telefon do stejného stavu v případě, že telefon ztratíte nebo bude ukraden.
Můžete se rozhodnout uložit záložní soubor na jakékoli externí úložiště nebo na vlastní cloudové řešení jako je Nextcloud, ačkoliv někteří uživatelé hlásí různé úrovně úspěchu s posledně jmenovanou možností.

Jak vytvořit vaši první zálohu:

1. Přejděte do **Nastavení** > **Systém** > **Zálohování**, poté si poznamenejte váš 12-slovný obnovovací kód. Tento kód je potřebný k dešifrování záložního souboru v pozdějším termínu. Ztratíte-li kód, ztratíte přístup k záloze telefonu.
2. Poté si vyberte místo uložení. Doporučil bych externí USB disk nebo průmyslovou microSD kartu.
3. Vyberte data k zálohování. Pokud máte na určeném úložišti dostatek místa, doporučuji vybrat vše.
4. Klepněte na tři tečky v pravém horním rohu a vyberte **Zálohovat nyní**.

![obrázek](assets/26.webp)

Obrazovka zálohování

Pamatujte, že pokud děláte offline zálohy na externí úložiště, je rozumné tento krok pravidelně opakovat, aby žádné nedávné důležité aktualizace vašeho telefonu nebyly ztraceny v případě nejhoršího scénáře.

![video](https://www.youtube.com/embed/eyWmcItzisk)

Video popisující proces zálohování

## Závěr

V posledních letech software GrapheneOS výrazně dozrál. Je stabilnější a kompatibilnější než kdykoli předtím. Spolu s rozkvětem ekosystému aplikací Open Source a ochrany soukromí, činí GrapheneOS skutečně životaschopnou alternativou k stock Androidu nebo iOS, i pro 'normální' lidi jako jste vy!

Porušování dat a masové sledování jsou v dnešním světě tak běžné, že už ani nejsou na titulních stránkách. Je na vás, abyste se chránili. Cestou budou nutné úpravy a oběti, ale snížení vaší expozice těmto porušením není tak těžké, jak si myslíte.

Doufám, že tento průvodce vám alespoň trochu pomůže na vaší cestě. Pokud jste našli tento průvodce užitečným a chtěli byste podpořit mou práci, zvažte prosím poslání [darování](/tips).

Pokud jste stávajícím uživatelem GrapheneOS, nebo se jím stanete díky tomuto průvodci, zvažte [darování](https://grapheneos.org/donate) na podporu jejich důležité práce.

### Další informace

GrapheneOS je zajímavá oblast, do které by se člověk mohl snadno ponořit na týdny. Je toho tolik, co se dá naučit a upravit, aby zážitek odpovídal vašim požadavkům a modelům ohrožení. Níže jsou odkazy, kde můžete pokračovat ve vaší cestě:

- [Oficiální uživatelská příručka GrapheneOS](https://grapheneos.org/usage) - Oficiální web
- [Fórum GrapheneOS](https://discuss.grapheneos.org/) - Oficiální web
- [Masterclass nastavení GrapheneOS](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video od 'The Privacy Wayfinder'
- [Všeobecný podcast GrapheneOS](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast od 'Watchman Privacy'

plné uznání: https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md