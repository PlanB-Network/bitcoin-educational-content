---
name: Ashigaru - Ricochet
description: Porozumění a používání transakcí Ricochet
---
![cover ricochet](assets/cover.webp)



> *Prémiový nástroj, který přidává k transakci další historické údaje. Překážejte černým listinám a chraňte se před neoprávněným uzavřením účtu třetí stranou.*

## Co je to Ricochet?



Ricochet je technika spočívající v provedení několika fiktivních transakcí vůči sobě samému, která simuluje převod vlastnictví bitcoinů. Tento nástroj se od ostatních transakcí Ashigaru (zděděných po Samurai Wallet) liší tím, že neposkytuje prospektivní anonymitu, ale spíše formu retrospektivní anonymity. Ricochet ve skutečnosti rozmazává specifika, která mohou ohrozit zaměnitelnost části Bitcoin.



Pokud například vytvoříte coinjoin, bude váš díl vystupující z mixu identifikován jako takový. Nástroje pro analýzu řetězců jsou schopny detekovat paterny transakcí coinjoin a přiřadit dílům, které z nich vycházejí, označení. Cílem coinjoinu je v podstatě přerušit historické vazby mince, ale její průchod coinjoiny zůstává zjistitelný. Analogicky lze tento jev přirovnat k šifrování textu: ačkoli k původnímu textu nelze získat přístup v otevřeném textu, je snadné zjistit, že bylo použito šifrování.



Označení "coinjoined" může ovlivnit zaměnitelnost UTXO. Regulované subjekty, například burzovní platformy, mohou odmítnout přijmout coinjoined UTXO, nebo dokonce požadovat vysvětlení od jeho majitele, přičemž hrozí zablokování účtu nebo zmrazení finančních prostředků. V některých případech může platforma dokonce nahlásit vaše chování státním orgánům.



K tomu slouží metoda Ricochet. Aby zmizel otisk zanechaný spojením mincí, provede Ricochet čtyři po sobě jdoucí transakce, při nichž si uživatel převede své prostředky na různé adresy. Po této sekvenci transakcí nástroj Ricochet nakonec nasměruje bitcoiny na jejich konečné místo určení, například na výměnnou platformu. Cílem je vytvořit odstup mezi původní transakcí coinjoin a konečným aktem utrácení. Tímto způsobem budou nástroje pro analýzu blockchainu předpokládat, že po coinjoinu pravděpodobně došlo k převodu vlastnictví, a proto není třeba podnikat kroky proti emitentovi.



![image](assets/fr/01.webp)



V souvislosti s metodou Ricochet si lze představit, že software pro analýzu řetězců bude zkoumat hlouběji než čtyři odrazy. Tyto platformy však čelí dilematu při optimalizaci detekčního prahu. Potřebují stanovit prahový počet přeskoků, po jehož překročení akceptují, že pravděpodobně došlo ke změně vlastníka a že odkaz na předchozí coinjoin by měl být ignorován. Stanovení tohoto prahu je však riskantní: každé rozšíření počtu pozorovaných skoků exponenciálně zvyšuje objem falešně pozitivních případů, tj. osob mylně označených jako účastníci coinjoinu, i když ve skutečnosti operaci provedl někdo jiný. Tento scénář představuje pro tyto společnosti velké riziko, protože falešně pozitivní výsledky vedou k nespokojenosti, která může postižené zákazníky přivést ke konkurenci. Z dlouhodobého hlediska vede příliš ambiciózní práh detekce k tomu, že platforma ztrácí více zákazníků než její konkurenti, což může ohrozit její životaschopnost. Proto je pro tyto platformy komplikované zvyšovat počet zjištěných odchylek, přičemž 4 je často dostatečný počet, aby bylo možné jejich analýzy vyvrátit.



Proto **nejčastější případ použití Ricochetu nastává, když je třeba utajit předchozí účast v coinjoinu na UTXO, který vlastníte.** V ideálním případě je nejlepší vyhnout se převodu bitcoinů, které prošly coinjoinem, na regulované subjekty. Nicméně v případě, že vám nezbývá jiná možnost, zejména při naléhavé potřebě likvidace bitcoinů ve státní měně, nabízí Ricochet účinné řešení.



## Jak funguje Ricochet na Ashigaru?



Ricochet je jednoduše metoda posílání bitcoinů sobě samému, kterou původně vynalezli vývojáři Samurai Wallet. Ricochet je tedy možné dokonale simulovat ručně, aniž by bylo nutné používat specializovaný nástroj. Pro ty, kteří si však chtějí proces zautomatizovat a zároveň se těšit z vybroušenějšího výsledku, představuje dobré řešení nástroj Ricochet dostupný prostřednictvím aplikace Ashigaru (což je Samourai fork).



Protože Ashigaru si za své služby účtuje poplatky, stojí Ricochet 100 000 sats jako poplatek za služby a navíc poplatek mining. Jeho použití se proto doporučuje pro převody významných částek.



Aplikace Ashigaru nabízí dvě varianty hry Ricochet:





- Posílený Ricochet neboli "rozložené doručení", které nabízí výhodu rozložení poplatků za služby Ashigaru na pět po sobě jdoucích transakcí. Tato možnost také zajišťuje, že každá transakce je vysílána v samostatném čase a zaznamenána v jiném bloku, což co nejvěrněji napodobuje chování při změně vlastnictví. Ačkoli je tato metoda pomalejší, je vhodnější pro ty, kteří nespěchají, protože maximalizuje efektivitu Ricochetu tím, že posiluje jeho odolnost vůči řetězové analýze;





- Klasický Ricochet, který je určen k rychlému provádění operací, vysílá všechny transakce ve zkráceném časovém intervalu. Tato metoda tedy nabízí menší důvěrnost a menší odolnost vůči analýze než zesílená metoda. Měla by se používat pouze pro urgentní zásilky.



## Jak vytvořit Ricochet na Ashigaru?



Vytvoření ricochetu na Ashigaru je velmi jednoduché: stačí aktivovat příslušnou možnost při vytváření transakce odeslání. Začněte tím, že kliknete na tlačítko `+`, poté na `Odeslat` a vyberete účet, z něhož chcete peníze odeslat.



![Image](assets/fr/02.webp)



Vyplňte informace o transakci: částku, která má být odeslána, a konečnou adresu příjemce po skocích Ricochet. Poté zaškrtněte možnost `Ricochet`.



![Image](assets/fr/03.webp)



Poté si můžete vybrat mezi dvěma režimy Ricochet popsanými v teoretické části: buď klasický Ricochet, kdy jsou všechny transakce zahrnuty do stejného bloku, nebo rozložené doručení, které zlepšuje kvalitu Ricochetu za cenu delšího zpoždění.



Po výběru potvrďte výběr stisknutím šipky v dolní části obrazovky.



![Image](assets/fr/04.webp)



Na další obrazovce se zobrazí kompletní shrnutí transakce. Zde také můžete upravit sazbu poplatků za transakce Ricochet podle podmínek na trhu. Pokud vám vše vyhovuje, přetáhněte zelenou šipku a podepište a distribuujte transakce Ricochet.



![Image](assets/fr/05.webp)



Počkejte, až se jednotlivé skoky spustí automaticky.



![Image](assets/fr/06.webp)



Vaše transakce byly úspěšně odvysílány.



![Image](assets/fr/07.webp)



Nyní jste již plně obeznámeni s možností Ricochet, která je k dispozici v aplikaci Ashigaru. Chcete-li jít dál, doporučuji vám absolvovat můj vzdělávací kurz BTC 204, který vás podrobně naučí, jak posílit důvěrnost onchainu.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c