---
name: Green Wallet

description: Průvodce nastavením a používáním (CC Bistack)
---

![obálka](assets/cover.webp)

Hot Mobile Wallet - Začátečník - Zdarma - Zabezpečení od 0 do 1 000 €

Pro zabezpečení částek nižších než 1 000 € je zdarma hot wallet (připojený k internetu) ideální pro začátečníky. Jeho nastavení je snadné a jeho rozhraní je navrženo pro začátečníky.

Pokud chcete navštívit jejich webovou stránku, klikněte zde (https://blockstream.com/green/)!

## Video Návod

![video návod na green wallet](https://www.youtube.com/watch?v=lONbCS31am4)

## Písemný Návod

> Tento průvodce byl vyroben a patří Bitstacku. Bitstack je bitcoinová neo banka se sídlem v Paříži, která umožňuje DCA na bitcoinu. Průvodce napsal Loic Morel dne 15. 02. 2023. Patří jim. https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet

![obrázek](assets/0.webp)

Jak nainstalovat vaši první Bitcoin peněženku? Návod na Green Wallet

Pokud chcete využít mnoha výhod systému Bitcoin, včetně necenzurovatelnosti a nezabavitelnosti vašich prostředků, musíte osobně uchovávat klíče, které vám dávají přístup k vašim bitcoinům.

V tomto návodu vám vysvětlím, jak nastavit vaši první peněženku s Green Wallet. Tento software je zvláště vhodný pro začátečnické uživatele. Je velmi snadno použitelný, i když nemáte pokročilé znalosti o Bitcoinu.

Green Wallet je dostupný na všech typech zařízení. V tomto návodu uvidíme, jak jej používat na mobilu, ale můžete si jej také stáhnout na počítač.

Prvním krokem je samozřejmě stáhnout software nebo aplikaci Green Wallet. Pokud jste na mobilu, můžete si ji jednoduše stáhnout z vašeho obchodu. Ujistěte se, že jste na oficiální stránce pro stahování aplikace. Zde jsou stránky v závislosti na vašem systému:

> - Google Play Store
>
> - Apple App Store

Pokud si stahujete software na počítač, důrazně doporučuji ověřit pravost a integritu binárního souboru před jeho instalací na vašem stroji. Jak provést tuto operaci, vám vysvětlím v budoucím návodu.

## Výběr Nastavení Aplikace

Při spuštění aplikace se dostanete na úvodní obrazovku. V tuto chvíli nemáte žádné peněženky. Později, pokud jste vytvořili více peněženek, je zde najdete.

První akcí před vytvořením vaší peněženky je otevřít nastavení aplikace a vybrat ty, které vám nejlépe vyhovují.

![obrázek](assets/1.webp)

- "Enhanced Privacy" umožňuje zakázat možnost pořizování snímků obrazovky v aplikaci. Tato možnost také skryje náhledy a automaticky zabezpečí aplikaci, když zamknete telefon. Je dostupná pouze na Androidu;
- Poté si můžete vybrat směrování vašeho provozu přes Tor, takže všechna vaše připojení jsou šifrována. To mírně zpomalí provoz vaší aplikace, ale doporučuji ji aktivovat pro zachování vašeho soukromí;

- Možnost "Testnet" umožňuje vytvářet peněženky na Testnetu. Jedná se o síť, která funguje přesně jako systém Bitcoin, s výjimkou toho, že bitcoiny vyměňované na ní nemají absolutně žádnou hodnotu. Tato oddělená síť Testnet je oblíbená uživateli nebo vývojáři, kteří chtějí testovat aplikace bez jakéhokoli finančního rizika. Pokud chcete používat Green Wallet na skutečném systému Bitcoin, můžete tuto možnost nechat nezaškrtnutou;

- Možnost "Help Green" umožňuje předávat důvěrné informace Blockstreamu, aby mohli vylepšit svou aplikaci;

- Možnost "Personal Electrum Server" umožňuje připojit váš vlastní vzdálený Bitcoin uzel pro přístup k informacím o síti a vysílání vašich transakcí;
- Možnost "SPV ověření" vám umožňuje stáhnout a ověřit určité informace z Blockchainu sami. To snižuje potřebu důvěřovat uzlu Blockstream. Vezměte prosím na vědomí, že tato možnost neposkytuje všechny záruky skutečného Bitcoinového uzlu, ale pokud žádný nemáte, může být dobré ji aktivovat.
Jakmile si vyberete svá nastavení, můžete kliknout na tlačítko "Uložit" a poté restartovat svou aplikaci.

## Vytvoření Bitcoinové peněženky

Dalším krokem je vytvoření vaší Bitcoinové peněženky. K tomu klikněte na:

> - Přidat peněženku;
> - Nová peněženka;
> - Bitcoin.

![image](assets/3.webp)

Možnost "Obnovit peněženku" vám umožňuje znovu získat přístup k existující peněžence pomocí její mnemonické fráze. Možnost "Peněženka pouze pro sledování" vám umožňuje importovat rozšířený veřejný klíč (xpub) pro zobrazení pohybů peněženky bez možnosti utrácet její prostředky.

> "Peněženka pouze pro sledování je obzvláště užitečná, pokud máte hardwarovou peněženku. Můžete importovat xpub do svého telefonu pro vytváření přijímacích adres a sledování zůstatku peněženky hostované na hardwarové peněžence."
> Možnosti sítě vám umožňují připojit vaši peněženku k různým systémům. Síť "Liquid" je Bitcoinová sidechain. Síť "Testnet" je kopie Bitcoinové sítě, ale s bitcoiny, které nemají žádnou hodnotu. Nakonec, síť "Testnet Liquid" je ekvivalentem Testnetu pro sidechain Liquid. V tomto návodu jednoduše chceme vytvořit Bitcoinovou peněženku, takže vybereme síť "Bitcoin".

Poté budete dotázáni, jaký typ peněženky chcete vytvořit. Nejjednodušší možností je vytvořit peněženku "Single Sig". V tomto případě bude každý UTXO (kus bitcoinu), který nám patří, zamčen pouze jedním párem klíčů.

Vyberte "Single Signature".

Poté si můžete vybrat, zda chcete mít mnemonickou frázi o 12 slovech nebo o 24 slovech. Tato fráze vám umožní obnovit přístup k vaší peněžence z jakéhokoli kompatibilního softwaru v případě ztráty, krádeže nebo poškození vašeho telefonu.

Fráze o 24 slovech je bezpečnější proti útokům hrubou silou než fráze o 12 slovech. V současné době je však fráze o 12 slovech stále dostatečně bezpečná. V praktickém smyslu, pokud si vyberete frázi o 12 slovech, budete se nacházet těsně nad minimálním doporučeným limitem NIST. To znamená, že vaše fráze je dnes bezpečná, ale v budoucnu nemusí být kvůli pokrokům v počítačové technice (pokud také nepoužíváte BIP39 heslo). Ve výchozím nastavení doporučuji vybrat frázi o 24 slovech, ale je na vás, abyste si učinili vlastní volbu.

![image](assets/6.webp)

Software vám poté poskytne vaši obnovovací frázi. Musíte ji řádně uložit tím, že ji zapíšete na vhodné fyzické médium. Důrazně se nedoporučuje uchovávat tuto frázi na jakémkoli digitálním médiu, i když je šifrována. Měla by být napsána na papír nebo kov v závislosti na uložené hodnotě.

Tato fráze je nesmírně důležitá, protože umožňuje přístup ke klíčům vaší peněženky bez jakýchkoli omezení. Pokud ji ztratíte, již nebudete moci přistupovat k vašim bitcoinům, pokud váš telefon přestane fungovat. Pokud je tato mnemonická fráze ukradena, útočník může vaše prostředky nevratně ukrást.

Slova v této frázi musí být napsána dohromady. Nerozdělujte svou frázi! Kromě toho je také nezbytné zapsat každé slovo ve stanoveném pořadí spolu s jeho číslem. Fráze v nesprávném pořadí je k ničemu.

Pokud se chcete dozvědět více o zabezpečení obnovovací fráze, vřele doporučuji přečíst si můj věnovaný článek na toto téma.

![image](assets/7.webp)
Green Wallet vás poté požádá, abyste potvrdili určitá slova z vaší fráze, aby se zajistilo, že jste si je správně zapsali.
![image](assets/10.webp)

Poté si můžete vybrat název pro svou peněženku, abyste ji odlišili od ostatních, pokud později vytvoříte více peněženek. V této fázi název není důležitý, protože tuto peněženku smažeme, abychom ověřili platnost mnemonické fráze v dalším kroku.

Je také požadováno, abyste nastavili PIN. Používá se k uzamčení přístupu k vaší peněžence. Je doporučeno nastavit složité a náhodné heslo, zejména pro ochranu vaší peněženky v případě, že by vám byl telefon ukraden.

Tento PIN nemá nic společného samotnou Bitcoin peněženkou. Ve skutečnosti, pouze s obnovovací frází budete schopni znovu získat přístup ke všem vašim bitcoinům. PIN pouze blokuje přístup k vaší peněžence ve vašem telefonu. Proto je zálohování fráze mnohem důležitější než zálohování tohoto PINu.

Později můžete přidat možnost biometrického zámku, abyste nemuseli pokaždé zadávat PIN při používání. Obecně platí, že biometrie je mnohem méně bezpečná než samotný PIN. Proto bych ve výchozím nastavení nedoporučoval implementaci této možnosti odemykání.

Zadaný PIN musíte na aplikaci Green zadat podruhé pro jeho potvrzení.

![image](assets/12.webp)

Gratulujeme! Dokončili jste vytvoření vaší Bitcoin peněženky.

![image](assets/14.webp)

Pokud chcete do této Bitcoin peněženky přidat BIP39 heslovou frázi, musíte kliknout na tři tečky v pravém horním rohu obrazovky při zadávání PINu pro odemčení peněženky. Buďte opatrní, důrazně nedoporučuji používat heslovou frázi, pokud nerozumíte mechanismům derivace, které jsou v hře. Mohli byste přijít o přístup k vašim bitcoinům.

## Simulace obnovy vaší Bitcoin peněženky

Před odesláním bitcoinů do vaší nové peněženky je nezbytné provést test obnovy, abyste zajistili, že vaše záloha mnemonické fráze je funkční. V praxi peněženku smažeme, zatímco je ještě prázdná, a pokusíme se ji obnovit pouze pomocí obnovovací fráze, jako bychom přišli o přístup k našemu telefonu.

Kromě ověření platnosti fráze vám tato praxe také umožní procvičit obnovu Bitcoin peněženky. Takže pokud se někdy ocitnete v nouzové situaci, budete přesně vědět, jaké kroky podniknout, abyste znovu získali přístup k vašim prostředkům.

K tomu, než peněženku smažete, musíte získat referenční informaci, která vám umožní ji později rozpoznat. Proto si zkopírujete posledních 8 znaků první adresy, která vám bude nabídnuta.
Pro přístup k této informaci klikněte na tlačítko "Přijmout". Peněženka zobrazí adresu. Zapište si posledních 8 znaků adresy na samostatný kus papíru. To odpovídá kontrolnímu součtu adresy.

Například na mé peněžence by 8 znaků k zapsání bylo: JTbP4482.

![image](assets/16.webp)

Jakmile máte tyto informace zapsané, můžete svou peněženku smazat. Z domovské obrazovky peněženky klikněte na ikonu nastavení, poté klikněte na "Odpojit".

> "Chci znovu zdůraznit, že tato operace musí být provedena s prázdnou peněženkou, před odesláním jakýchkoli bitcoinů do ní. V opačném případě riskujete jejich ztrátu."

![image](assets/19.webp)

Poté budete přesměrováni na obrazovku pro odemčení peněženky. Klikněte na tři tečky v pravém horním rohu obrazovky, poté klikněte na "Smazat peněženku" a potvrďte.

![image](assets/21.webp)
Nyní se nacházíte na domovské obrazovce aplikace Green Wallet a nejsou zde dostupné žádné peněženky. Nacházíte se v situaci, jako kdybyste ztratili nebo rozbili svůj telefon a pokoušeli se obnovit svou peněženku pouze pomocí mnemonické fráze.

Nyní klikněte na "Přidat peněženku", poté na "Obnovit peněženku" a nakonec na "Bitcoin".

![image](assets/23.webp)

Software nás poté zeptá, zda chceme obnovit z QR kódu nebo z mnemonické fráze. V našem případě jde o frázi.

Dále nás požádají, abychom zadali obnovovací frázi. To je fráze, kterou jsme si zapsali při vytváření peněženky. Pokud používáte 24slovní frázi, nezapomeňte kliknout na malé políčko "24".

Jakmile jsou všechna slova zadána, pokud vám software řekne, že je zde chyba, znamená to, že kontrolní součet vaší fráze je nesprávný. V tomto případě to znamená, že papírová záloha vaší mnemonické fráze je neplatná. Musíte začít tento návod znovu od začátku a ujistit se, že jste frázi správně zapsali, když vám byla dána.

Jinak můžete kliknout na "Pokračovat".

![image](assets/26.webp)

Software uvede "Peněženka nenalezena". To je zcela normální, protože v tuto chvíli jsme do ní ještě neposlali žádné bitcoiny. Proto nemůže detekovat žádné transakce na blockchainu spojené s touto peněženkou.

Klikněte na "Ruční obnova" na spodní části obrazovky, poté klikněte na "Jednoduchý podpis".

![image](assets/28.webp)

Nakonec budete požádáni, abyste této peněžence dali název a přiřadili jí PIN. Můžete jí dát stejný název a PIN jako počáteční peněžence.
Pro připomenutí, tento PIN slouží pouze k odemčení peněženky v této aplikaci a na tomto konkrétním telefonu. Na rozdíl od obnovovací fráze neumožňuje regenerovat vaši peněženku na jiném softwaru nebo hardwaru.
![image](assets/30.webp)

Jakmile je PIN ověřen, budete přesměrováni zpět na domovskou stránku vaší peněženky. Je čas zkontrolovat, zda je vaše obnovovací fráze funkční tím, že pozorujete první odvozenou adresu. K tomu opět klikněte na "Přijmout" a přistupte k první adrese.

Pokud posledních 8 znaků přesně odpovídá těm, které jste si jako svědky zapsali na papír před smazáním peněženky, pak je vaše fráze platná. V mém případě můžeme vidět, že kontrolní součet mé první adresy skutečně odpovídá dříve zaznamenané hodnotě: JTbP4482.

![image](assets/32.webp)

Vím, že tato ověřovací praxe je zdlouhavá, ale je naprosto nezbytná pro zajištění správné bezpečnosti vaší Bitcoin peněženky. Důrazně doporučuji vyvinout tento zvyk při vytváření peněženky, ať už je to na softwaru nebo hardwaru.

S Green Wallet jsem použil první adresu k provedení tohoto procesu. Můžete však také vzít rozšířený veřejný klíč (xpub/zpub) nebo hlavní otisk soukromého klíče jako informaci pro svědectví.

## Používání Bitcoin peněženky Green Wallet

Jakmile je vaše peněženka nastavena a ověřena, můžete ji začít používat.

Pro začátek doporučuji přizpůsobit nastavení vaší peněženky. K tomu klikněte na ikonu nastavení v pravém horním rohu obrazovky.

- Možnost "Displayed Unit" umožňuje přizpůsobit jednotku používanou ve vaší peněžence. Pokud máte malé množství prostředků, může být relevantní zobrazit vaši peněženku v sats místo v bitcoinech. Satoshi (sat) odpovídá jedné sté miliontině bitcoinu: 1 BTC = 100,000,000 sats.
- Možnost "Default Fee Amount" vám umožňuje přizpůsobit poplatky přiřazené k vašim transakcím jako výchozí. Čím vyšší jsou poplatky za vbyte (virtuální bajt), tím rychleji budou vaše transakce potvrzeny. Tuto sazbu poplatku můžete později upravit pro každou transakci v závislosti na zatížení sítě Bitcoin.
- Možnost "Biometric Connection" vám umožňuje odemknout vaši peněženku pomocí otisku prstu místo PINu. Obecně doporučuji tuto možnost neaktivovat. Biometrické údaje jsou mnohem méně bezpečné než PIN kód.

![obrázek](assets/34.webp)
Ve výchozím nastavení vám Green Wallet přiřadí účet BIP49 "Nested SegWit" s adresami P2SH (Pay to Script Hash). Před několika lety bylo používání tohoto typu účtu relevantní, protože ještě ne všichni podporovali nativní adresy SegWit. Dnes většina služeb souvisejících s Bitcoinem podporuje SegWit, takže již není důvod používat účet "Nested SegWit".

Nyní vytvoříme nový účet BIP84 "Native SegWit", abychom využili všech jeho výhod a získali také adresy P2WPKH (Pay to Witness Public Key Hash). K tomu klikněte na váš "Legacy SegWit Account" a poté na "Add a new account" a nakonec na "SegWit Account". Poté můžete tomuto účtu dát název, pokud chcete.

![obrázek](assets/36.webp)

V budoucnu, pokud budete potřebovat na této peněžence vytvořit nové účty, doporučuji výchozí volbu účtů SegWit V0 BIP84 nebo SegWit V1 BIP86 (pokud jsou k dispozici).

Na domovské stránce vaší peněženky můžete vidět vaše různé účty, včetně vašeho nového účtu SegWit.

Dále je ovládání aplikace Green Wallet velmi jednoduché. Chcete-li do své peněženky přijímat bitcoiny, klikněte na tlačítko "Receive". Peněženka zobrazí přijímací adresu. Adresa vám umožňuje přijímat bitcoiny do vaší peněženky. Můžete ji buď zkopírovat ve formátu textu, abyste ji poslali svému plátci, nebo naskenovat QR kód jinou Bitcoin peněženkou, aby byla adresa zaplacena.

![obrázek](assets/38.webp)

Tento typ adresy plátci neudává, kolik by vám měl poslat. Můžete také vytvořit adresu, která automaticky požádá plátce o zvolenou částku. K tomu klikněte na "More options" a zadejte požadovanou částku.

Protože používáte účet SegWit V0 BIP84, vaše adresa by měla začínat předponou "bc1q". V mém příkladu používám peněženku Testnet, takže předpona se mírně liší od vaší.

Přijímací adresu byste neměli používat vícekrát. Jedná se o špatnou praxi, která ohrožuje vaše soukromí. Ve výchozím nastavení vám Green wallet vygeneruje novou adresu, když kliknete na "Receive" a předchozí adresa již byla použita. Můžete také kliknout na ikonu rotující šipky, abyste požádali o novou prázdnou adresu spojenou s vaší peněženkou.

> "Tip: Při kopírování a vkládání přijímací adresy nemusíte ověřovat, že každý znak adresy je správný. Adresy totiž obsahují kontrolní součet pro detekci malé chyby při psaní. Je nutné pouze zkontrolovat první a poslední znaky adresy, aby se zajistila její platnost."
> Na níže uvedených snímcích obrazovky můžete vidět, že jsem poslal 0,02 btc na mou adresu. Transakce se na Green zobrazuje jako "nepotvrzená", dokud nebude zařazena do blockchainu těžařem. Jakmile transakce obdrží několik potvrzení, úspěšně jste přijali své bitcoiny do vlastní peněženky.

![obrázek](assets/40.webp)
Pokud chcete poslat bitcoiny, musíte získat přijímací adresu, na kterou chcete prostředky poslat, a kliknout na tlačítko "Odeslat". Na další stránce musíte zadat cílovou adresu. Můžete ji zadat ručně nebo naskenovat QR kód kliknutím na příslušnou ikonu. Poté vyberte částku transakce. Můžete zadat částku v bitcoinech nebo částku v amerických dolarech kliknutím na bílou dvojitou šipku.
![obrázek](assets/43.webp)

Uprostřed obrazovky můžete vybrat sazbu poplatku přiřazenou k této transakci. Můžete buď následovat doporučení aplikace, nebo si poplatky přizpůsobit. Čím vyšší poplatky nastavíte ve srovnání s ostatními transakcemi čekajícími na potvrzení, tím rychleji bude vaše transakce zahrnuta, a naopak.

Klikněte na "Další". Poté se dostanete na obrazovku, která vám poskytne podrobnosti o vaší transakci. Můžete ověřit, že zadaná adresa je správná, že částka odpovídá tomu, co chcete poslat, a že poplatky jsou správné.

Pro podepsání transakce a její vysílání do sítě Bitcoin posuňte zelené tlačítko na spodku obrazovky doprava.

![obrázek](assets/46.webp)

Vaše transakce se nyní zobrazuje na palubní desce vaší Bitcoin peněženky.

## Závěr

Gratulujeme! Nyní máte vlastní Bitcoin peněženku s vlastní správou. Vaše bitcoiny opravdu patří vám.

Tato Green Wallet od Blockstream je vynikající řešení pro začátečníky s malým množstvím bitcoinů. Jak jste viděli, je velmi snadné ji používat. Přesto se jedná o hot wallet. Pokud máte významné množství bitcoinů, doporučuji použít hardware peněženku.

Jakmile se naučíte ovládat Green Wallet a pochopíte mechanismy, které jsou v hře, můžete prozkoumat komplexnější řešení jako Samourai Wallet nebo Sparrow Wallet.
Na závěr vás znovu připomínám, že musíte absolutně dbát na zálohu vaší obnovovací fráze. Poskytuje přímý a neomezený přístup k vašim bitcoinům. Pokud ji ztratíte, nebudete již moci získat zpět své bitcoiny, pokud váš telefon bude ztracen, rozbitý nebo ukraden. Každý, kdo má přístup k této frázi, může vaše bitcoiny ukrást a nebude možné je získat zpět.

> Tento průvodce byl vyroben a patří Bitstack. Bitstack je bitcoinová neo banka se sídlem v Paříži, která umožňuje DCA na bitcoin. Průvodce napsal Loic Morel dne 15. 02. 2023. Patří jim. [Odkaz na původní článek](https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet)