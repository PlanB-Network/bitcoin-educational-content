---
name: Ricochet
description: Porozumění a používání transakcí Ricochet
---
![cover ricochet](assets/cover.webp)

***VAROVÁNÍ:** Po zatčení zakladatelů peněženky Samourai a zabavení jejich serverů 24. dubna již nástroj Ricochet není dostupný. Je však možné, že tento nástroj bude v nadcházejících týdnech znovu zaveden. Mezitím můžete Ricochet provést pouze ručně. Teoretická část tohoto článku zůstává relevantní pro pochopení jeho fungování a naučení se, jak to udělat ručně.*

_Sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento návod aktualizujeme, jakmile budou k dispozici nové informace._

_Tento návod je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je odpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

> *"Prémiový nástroj, který přidává k vaší transakci extra skoky historie. Zmate blacklisty a pomozte chránit proti nespravedlivým uzavřením účtů třetími stranami."*

## Co je Ricochet?
Ricochet je technika, která zahrnuje provádění několika fiktivních transakcí na sebe samého za účelem simulace převodu vlastnictví bitcoinů. Tento nástroj se liší od ostatních transakcí Samourai, protože neposkytuje potenciální anonymitu, ale spíše formu retrospektivní anonymity. Ricochet pomáhá rozmazat specifika, která by mohla ohrozit zaměnitelnost bitcoinové mince.

Například, pokud provedete coinjoin, výstup vaší mince z mixu bude takto identifikován. Nástroje pro analýzu řetězce jsou schopny detekovat vzory transakcí coinjoin a označit mince, které z nich vycházejí. Skutečně, coinjoin má za cíl přerušit historické vazby mince, ale její průchod coinjoiny zůstává detekovatelný. Abychom učinili analogii, tento jev je podobný šifrování textu: i když nemůžeme přistupovat k původnímu prostému textu, je snadno identifikovatelné, že bylo použito šifrování.

Přesněji, toto označení "mince výstupu coinjoin" může ovlivnit zaměnitelnost UTXO. Regulované subjekty, jako jsou platformy pro výměnu, mohou odmítnout přijmout UTXO, které prošlo coinjoinem, nebo dokonce vyžadovat vysvětlení od jeho majitele, s rizikem, že jejich účet bude zablokován nebo prostředky zmrazeny. V některých případech může platforma dokonce nahlásit vaše chování státním orgánům.

Zde vstupuje do hry metoda Ricochet. Aby se rozmazal otisk zanechaný coinjoinem, Ricochet provede čtyři po sobě jdoucí transakce, kde uživatel převádí své prostředky na sebe na různé adresy. Po této sérii transakcí nástroj Ricochet nakonec směruje bitcoiny na jejich konečné místo určení, jako je například platforma pro výměnu. Cílem je vytvořit vzdálenost mezi původní transakcí coinjoin a konečným aktem výdaje. Tímto způsobem budou nástroje pro analýzu řetězce myslet, že pravděpodobně došlo k převodu vlastnictví po coinjoinu, a proto není nutné proti odesílateli podnikat žádné kroky.
![ricochet diagram](assets/en/1.webp)
V kontextu metody Ricochet by si člověk mohl představit, že software pro analýzu řetězců by prohloubil své zkoumání za hranici čtyř odrazů. Tyto platformy se nicméně potýkají s dilematem optimalizace prahu detekce. Musí stanovit limit počtu skoků, po kterých přiznají, že pravděpodobně došlo ke změně vlastnictví a že spojení s předchozím coinjoinem by mělo být ignorováno. Určení tohoto prahu je však riskantní: každé rozšíření pozorovaného počtu skoků exponenciálně zvyšuje objem falešných pozitivů, tj. jedinců chybně označených za účastníky coinjoinu, když operaci ve skutečnosti provedl někdo jiný. Tento scénář představuje pro tyto společnosti velké riziko, protože falešná pozitiva vedou k nespokojenosti, která může dotčené zákazníky přivést k konkurenci. V dlouhodobém horizontu příliš ambiciózní práh vede k tomu, že platforma ztrácí více zákazníků než její konkurenti, což by mohlo ohrozit její životaschopnost. Pro tyto platformy je tedy komplikované zvyšovat počet pozorovaných odrazů, a 4 je často dostatečný počet k odražení jejich analýz.
Takže **nejčastější případ použití pro Ricochet nastává, když je nutné skrýt předchozí účast na coinjoinu na UTXO, které vám patří**. Ideálně je nejlepší se vyhnout převodu bitcoinů, které prošly coinjoinem, na regulované subjekty. Pokud však není jiná možnost, zejména v naléhavosti přeměnit bitcoiny na fiat měnu, nabízí Ricochet účinné řešení.

## Jak funguje Ricochet na Samourai Wallet?
Ricochet je jednoduše metoda, při které si člověk pošle bitcoiny sám sobě. Je tedy zcela možné manuálně simulovat Ricochet bez použití specializovaného nástroje. Pro ty, kteří si přejí automatizovat proces a zároveň těžit z dokonalejšího výsledku, je nástroj Ricochet dostupný prostřednictvím aplikace Samourai Wallet dobrým řešením.

Jelikož je služba na Samourai placená, Ricochet vyžaduje poplatek ve výši `100,000 sats` jako poplatek za službu, kromě poplatků za těžbu. Jeho použití je tedy doporučeno spíše pro převody významných částek.

Aplikace Samourai nabízí dvě varianty Ricochetu:
- Posílený Ricochet, neboli "stupňovité doručení", nabízí výhodu rozložení poplatků za službu Samourai do pěti po sobě jdoucích transakcí. Tato možnost také zajišťuje, že každá transakce je vysílána v odlišném čase a zaznamenána v jiném bloku, což úzce napodobuje chování změny vlastnictví. Ačkoli pomalejší, tato metoda je preferována pro ty, kteří se nechtějí nikam hnát, protože maximalizuje efektivitu Ricochetu zvýšením jeho odolnosti proti analýze řetězců.
- Klasický Ricochet, který je navržen k rychlému provedení operace vysíláním všech transakcí v redukovaném časovém intervalu. Tato metoda tedy nabízí menší soukromí a nižší odolnost vůči analýze ve srovnání s posílenou metodou. Měla by být upřednostněna pouze pro naléhavé převody.

## Jak provést Ricochet na Samourai Wallet?
Pro provedení transakce Ricochet z aplikace Samourai Wallet postupujte podle našeho video návodu:
![Ricochet YouTube video návod](https://youtu.be/Gsz0zuVo3N4)

Pokud si přejete prozkoumat transakce Ricochet provedené v tomto návodu, zde jsou:
- První transakce Ricochet: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://mempool.space/fr/testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Poslední transakce Ricochet: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://mempool.space/fr/testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)
**Externí zdroje:**
- https://docs.samourai.io/en/wallet/features/ricochet