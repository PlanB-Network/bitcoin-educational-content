---
name: Breez bod prodeje

description: Průvodce začátkem přijímání bitcoinů pomocí Breez POS
---

![obálka](assets/cover.webp)

_Tento text pochází z webové dokumentace Breez: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## Co je Breez POS?

**Breez** je kompletní, nezákonná aplikace Lightning. Pojďme to rozložit:

- **Lightning** je platební síť bitcoinu, která snižuje dobu transakcí z minut na milisekundy a poplatky za transakce z několika dolarů na několik centů nebo méně. Lightning proměňuje bitcoin z digitálního zlata na digitální měnu, přičemž zachovává všechny výhody, které dělají bitcoin skvělým.
- **Nezákonný** znamená, že Breez nepřebírá držení peněz uživatelů. Mnoho aplikací Lightning přebírá držení peněz svých uživatelů. Jsou to v podstatě bitcoinové banky. S nezákonnou aplikací jako je Breez jsou všichni uživatelé svými vlastními bankami.
- **Kompletní služba** znamená, že Breez se automaticky a na pozadí stará o téměř veškerou technickou operaci. Věci jako vytváření kanálů, příchozí likvidita a směrování zůstávají skryté. (Ale Breez je také open source, takže ti, kteří mají zájem o audit technologie, jsou vítáni!)

**Breez POS** je zkratka pro náš režim bodu prodeje. Jinými slovy, Breez funguje jako digitální pokladna pro podniky a obchodníky, kteří chtějí přijímat platby Lightning (kromě svého "standardního" režimu, který je jako digitální verze kožené peněženky pro bitcoin, a přehrávač podcastů nové generace). Nyní se podívejme, jak nastavit Breez jako Lightning pokladnu pro váš podnik.

## Jak začít s Breezem?

1. Prvním krokem je stáhnout aplikaci. Je dostupná pro Android a iOS (nainstalujte TestFlight a klikněte na odkaz ze svého zařízení).
2. Breez se může automaticky zálohovat na Google Drive, iCloud nebo na jakýkoliv server WebDav.
   > Všimněte si, že každé zařízení provozuje vlastní Lightning uzl. Režim POS můžete provozovat na libovolném počtu zařízení, ale zůstatky zůstanou oddělené.
3. S otevřenou aplikací klikněte na ikonu v levém horním rohu a najděte režim Bodu prodeje.

## Nastavení POS

1. Klikněte na tuto ikonu v levém horním rohu a klikněte na Bod prodeje > Nastavení POS.

### Heslo manažera

V nastavení POS máte možnost vytvořit heslo manažera. Heslo manažera znemožňuje odesílání odchozích plateb z aplikace Breez bez autorizace. Prodejní personál bude moci přijímat platby pouze z zařízení. Všimněte si, že pokud používáte tuto možnost, můžete také chtít zabránit přístupu k záloze Breez, takže použití externího účtu WebDav (např. Nextcloud) se doporučuje pro tento případ použití.

### Seznam položek

Seznam položek je katalog položek na prodej a jejich cen. Existují dva způsoby, jak přidat položky do seznamu:

- Pro vložení položek jednu po druhé klikněte na Položky v horní části hlavního pohledu POS, poté na znaménko "+" v pravém dolním rohu. Zde můžete zadat název jednoho typu položky, cenu (zobrazenou v ekvivalentu měny dle vašeho výběru) a SKU (unikátní interní identifikátor pro tento typ položky; je volitelný).
- Pro zadání více položek najednou klikněte na ikonu kalkulačky v levém horním rohu, poté na Bod prodeje > Předvolby > Nastavení POS a poté klikněte na tři tečky napravo od Seznamu položek a poté na Importovat z CSV. To vám umožní importovat připravený CSV soubor obsahující názvy, ceny a SKU vašich položek.

### Zobrazení Fiat

Breez posílá a přijímá pouze bitcoin a u většiny transakcí na Lightning, které bývají za menší částky, je suma obvykle zobrazena v Satoshis, známých také jako sats (1 BTC = 100,000,000 sats). Mnoho obchodníků však považuje za praktické vidět (a sdělit zákazníkům) hodnotu nákupu zobrazenou v místní fiat měně.

V hlavním zobrazení POS je měna, která je aktuálně zobrazena, viditelná na pravé straně (výchozí je SAT). K dispozici je také rozbalovací seznam dalších měn, které lze zobrazit. Pro přidání nebo odebrání měn z tohoto rozbalovacího seznamu klikněte na Bod prodeje > Předvolby > Fiat měny. Poté jednoduše zaškrtněte měny, které byste chtěli mít ve svém rozbalovacím menu, a odškrtněte ty, které byste chtěli vynechat.

Zobrazené hodnoty pocházejí z yadio, respektovaného zdroje údajů o směnných kurzech, a jsou aktualizovány téměř v reálném čase. Ale pamatujte: bez ohledu na to, jaká hodnota měny je aktuálně zobrazena, platba sama je v bitcoinech.

### Účtování objednávky

Pro sestavení objednávky buď přidejte položky ze seznamu položek, nebo jednoduše zadejte sumu na klávesnici. Poté klikněte na Účtovat v horní části hlavního zobrazení POS. Uvidíte QR kód, který může zákazník naskenovat svou aplikací Lightning, který můžete přímo sdílet z jiné aplikace na vašem zařízení, nebo který můžete kopírovat a vkládat tam, kde je to potřeba.

Po naskenování tohoto kódu nebo kliknutí na sdílenou/vloženou fakturu uvidí zákazník fakturu ve své aplikaci Lightning a bude mít možnost ji zaplatit a okamžitě uzavřít transakci.

Jakmile uvidíte animaci Platba schválena! v aplikaci Breez na zařízení obchodníka, můžete kliknout na ikonu tiskárny, abyste vygenerovali účtenku pro zákazníka. Pro použití tiskárny účtenek v Androidu zkuste použít tento ovladač. Všimněte si, že můžete také tisknout předchozí transakce prostřednictvím obrazovky Transakce.

### Zpráva o prodeji

Pro zobrazení denního/týdenního/měsíčního reportu vašich prodejů (pro účely účetnictví nebo jiné), klikněte na ikonu v levém horním rohu a poté klikněte na Transakce. Klikněte na ikonu Reportu pro zobrazení reportu a na ikonu Kalendáře pro změnu vybraného časového rozmezí.

### Export transakcí

Pro zobrazení seznamu přijatých plateb v Breez, klikněte na ikonu v levém horním rohu a poté klikněte na Transakce. Klikněte na tři tečky v pravém horním rohu, poté na Export pro export seznamu příchozích plateb ve formátu CSV. Pro omezení seznamu na určité časové období klikněte na ikonu kalendáře a nastavte časový rozsah.

### Tisk účtenek

Pro tisk prodejní účtenky klikněte na ikonu tiskárny v pravém horním rohu dialogu potvrzení platby. Alternativně klikněte na ikonu v levém horním rohu a poté klikněte na Transakce. Najděte prodej, který chcete vytisknout, otevřete ho a klikněte na ikonu tiskárny v pravém horním rohu.

> Poznámka: použijte tento ovladač pro tisk na přenosnou 58mm/80mm Bluetooth/USB termální tiskárnu.

## Chci se dozvědět více

- Pro více informací o Lightning a Breez, navštivte náš [blog](https://breez.technology/blog).
- Pro další technické tipy, jak z aplikace získat maximum a provádět běžné operace, si prohlédněte naši [dokumentaci](https://breez.technology/documentation).
- Pokud narazíte na problém a nenajdete odpověď v žádné z našich pomocných materiálů, můžete nás najít na [Telegramu](https://t.me/breez_labs) nebo nám poslat [email](mailto:support@breez.technology).
- Pokud chcete vidět některá demonstrační videa režimu Breez POS v akci, která vytvořili naši fanoušci a uživatelé, [zde](https://www.youtube.com/watch?v=xxxx) je skvělé krátké video a [zde](https://www.youtube.com/watch?v=xxxx) je delší, podrobnější video.