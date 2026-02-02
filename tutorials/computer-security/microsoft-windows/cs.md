---
name: Windows 11
description: Automatická instalace systému Microsoft Windows 11 pomocí konfiguračního souboru
---
![cover](assets/cover.webp)


V tomto návodu se dozvíte, jak automaticky nainstalovat systém Windows 11 jiným způsobem než standardním postupem instalace systému Windows.


## Stáhnout!


Nejprve budete potřebovat instalační soubor. Nejbezpečnější a nejspolehlivější místo, odkud jej můžete stáhnout, je přímo z oficiálních stránek společnosti Microsoft.


Jednoduše navštivte níže uvedený odkaz a podle pokynů stáhněte [soubor ISO systému Windows 11](https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Jakmile se ocitnete na stránce pro stahování, přejděte dolů k části pro stažení souboru ISO.


![Image](assets/en/01.webp)


َa vyberte správnou verzi.


![Image](assets/en/03.webp)


Po výběru systému Windows 11 klikněte na tlačítko Potvrdit.


V tomto kroku může zpracování žádosti trvat několik sekund a poté se zobrazí následující stránka:


![Image](assets/en/04.webp)


Po potvrzení požadavku je třeba zvolit preferovaný jazyk.


![Image](assets/en/05.webp)


Po výběru jazyka a kliknutí na tlačítko Potvrdit bude požadavek zpracován. Tento krok může trvat několik sekund.


Po úspěšném zpracování požadavku se zobrazí stránka s odkazem na stažení souboru .iso. Kliknutím na tlačítko Stáhnout 64bitový soubor zahájíte stahování.


Velikost souboru je přibližně 5,5 GB a vygenerovaný odkaz bude platný 24 hodin.


## Automatizace!


V této fázi musíme provést změny ve standardní instalaci systému Windows. V této fázi pomocí bezobslužné instalace určíme, které položky budou nainstalovány, aniž by do toho uživatel dodatečně zasahoval. V této metodě se vlastně používá soubor XML pro konfiguraci instalačních kroků a služeb instalovaných v systému Windows. Jinými slovy, použití souboru Unattended.xml vytváří automatizaci procesu během instalace, čímž se zabrání nutnosti výběru více možností a zamezí se zdlouhavým krokům, které jsou obvykle během instalace nutné. Tato metoda je neobvyklá, ale standardní metoda, kterou zavedla společnost Microsoft. Další informace jsou k dispozici na [oficiálních stránkách společnosti Microsoft](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Na internetu jsou k dispozici různé nástroje pro generování bezobslužných souborů. Některé z nich jsou online, jiné offline. Jedním z online nástrojů pro vytvoření tohoto souboru je [tato webová stránka](https://schneegans.de/windows/unattend-generator). Po jeho otevření se nám zobrazí následující stránka:


![Image](assets/en/06.webp)


Jak je uvedeno v horní části stránky, tuto metodu lze použít pro instalaci systémů Windows 10 a 11. V prvním kroku vybereme jazyk systému Windows. Pokud potřebujeme přidat druhý nebo dokonce třetí jazyk do seznamu jazyků zobrazení a klávesnice systému Windows, můžeme použít níže uvedené pole:


![Image](assets/en/07.webp)


V dalším kroku vybereme požadované umístění.


![Image](assets/en/08.webp)


V této fázi můžeme také určit architekturu procesoru počítače. V tomto kroku můžeme:

1. Rozhodněte se, zda budete ignorovat bezpečnostní funkce systému Windows, jako je TPM a Secure Boot. Funkce Secure Boot zajišťuje, že pokud dojde během zavádění systému k manipulaci s některými základními soubory systému Windows, je problém zjištěn a je zabráněno jejich spuštění. Tato funkce také pomáhá chránit systém před instalací škodlivých aktualizací systému Windows. Povolení možnosti obejít tyto funkce je u některých počítačů, zejména starších modelů, někdy nevyhnutelné. Obecně se však doporučuje funkce jako Secure Boot ponechat povolené.

2. Požadavek na připojení k internetu pro dokončení procesu ignorujte. To je užitečné v situacích, kdy není k dispozici kabelové připojení k síti LAN, protože ve většině případů není bezdrátová karta během instalace systému Windows ještě rozpoznána a je vyžadován přístup k internetu prostřednictvím kabelu. Aktivace této možnosti řeší problémy spojené s tímto krokem.


V dalším kroku můžeme zvolit název počítače.


![Image](assets/en/09.webp)


Můžeme také umožnit systému Windows zvolit název systému. V tomto kroku můžeme vybrat typ systému Windows, zda komprimovaný, nebo nekomprimovaný, nebo nechat systém Windows určit vhodnou verzi na základě specifikací počítače. V této fázi lze také nastavit časové pásmo.


Dalším krokem je nastavení oddílu:


![Image](assets/en/10.webp)


V této fázi můžeme zadat typ oddílu pro instalaci systému Windows a požadovaná nastavení pro instalaci prostředí pro obnovení systému Windows. Výběrem první možnosti se výběr oddílu a jeho rozdělení odloží na dobu instalace systému Windows a během instalace budou tyto otázky položeny stejně jako při běžném způsobu instalace.


V tomto kroku vybereme verzi systému Windows, kterou chceme nainstalovat:


![Image](assets/en/11.webp)


Pokud je k dispozici produktový klíč, lze jej v této fázi rovněž zadat.


Dalším krokem je konfigurace přihlašovacího účtu systému Windows:


![Image](assets/en/12.webp)


## Schůzky k účtu


V této fázi:


1. Pro účet správce můžeme definovat jméno a heslo. Je také možné vytvořit více uživatelských účtů nebo účtů správce.

2. Zde určíme, ke kterému účtu se přihlásit poprvé po instalaci systému Windows. Jednotlivé možnosti této sekce jsou zobrazeny na obrázku.

3. Pokud nechcete, aby byly vytvořeny žádné účty, vyčistěte všechny účty a vyberte tuto možnost. V tomto případě budete po instalaci systému Windows automaticky přihlášeni k účtu správce systému Windows.


V dalším kroku je třeba nakonfigurovat nastavení hesla a hostitelského souboru:


![Image](assets/en/13.webp)


V této fázi určíme, zda mají mít hesla dobu platnosti. Kromě toho tato část obsahuje nastavení zabezpečení týkající se neúspěšných pokusů o přihlášení, které lze podle potřeby povolit nebo zakázat.


V dolní části této sekce se nachází nastavení pro zobrazení souborů. Žádná z těchto možností není k dispozici během standardní instalace systému Windows a musí být nakonfigurována po instalaci. Naopak při bezobslužné metodě instalace jsou tato nastavení snadno přístupná.


Dalším krokem je konfigurace nastavení zabezpečení systému Windows:


![Image](assets/en/14.webp)


## Nastavení zabezpečení


V této fázi:


1. Program Windows Defender lze povolit nebo zakázat. Tato funkce funguje jako bezpečnostní software ve Windows a pomáhá zabránit spouštění škodlivých souborů, některým síťovým útokům a dalším.

2. Automatické aktualizace systému Windows lze zakázat. Jedná se o jeden z častých problémů, se kterými se uživatelé systému Windows potýkají!

3. Tato část umožňuje povolit nebo zakázat UAC (Řízení uživatelských účtů). Tato funkce zabraňuje spouštění podezřelých aplikací se zvýšenými oprávněními pro čtení a zápis.

4. Tuto funkci používá systém Windows k detekci potenciálně škodlivého softwaru.

5. Povolení nebo zakázání podpory dlouhých cest v aplikacích systému Windows, například v prostředí PowerShell a dalších.

6. Povolení nebo zakázání vzdálené plochy pro vzdálený přístup k systému.


V závislosti na použité verzi systému Windows mohou, ale nemusí být některé z těchto funkcí podporovány.


Dalším krokem je konfigurace ikon:


![Image](assets/en/15.webp)


V této části:


1. Na ploše jsou uvedeny ikony, které lze podle potřeby přidávat nebo odebírat.

2. V seznamu jsou uvedeny ikony nabídky Start, které lze také přidávat nebo odebírat na základě požadavků.

3. Tato část umožňuje nastavit, zda mají být nainstalovány nástroje související s virtualizací. Tato možnost je specifická pro systém Windows 11 a nevztahuje se na systém Windows 10.


Dalším krokem je konfigurace nastavení Wi-Fi:


![Image](assets/en/16.webp)


V této části lze konfigurovat nastavení sítě Wi-Fi. Jak již bylo zmíněno, ve většině případů není karta Wi-Fi při instalaci systému Windows rozpoznána, takže připojení během instalace obvykle není možné. Pokud je však bezdrátová karta rozpoznána, lze se pomocí konfigurace této části připojit k internetu.


Další krok zahrnuje důležité nastavení:


![Image](assets/en/17.webp)


V této části určíme, zda mají být informace o problémech systému odeslány společnosti Microsoft, nebo ne.


Dalším krokem je konfigurace výchozích aplikací:


![Image](assets/en/18.webp)


## Výchozí povolení/vypnutí softwaru


V této části můžeme vybrat aplikace, které nechceme, aby byly nainstalovány ve výchozím nastavení. Můžeme se například rozhodnout neinstalovat Cortanu nebo Copilota.


Další krok zahrnuje nastavení zabezpečení související se spouštěním aplikací:


![Image](assets/en/19.webp)


Použitím nastavení WDAC lze zabránit spuštění některých aplikací.


Po použití požadovaných nastavení lze nakonec stáhnout vygenerovaný soubor XML:


![Image](assets/en/20.webp)


Kliknutím na Stáhnout soubor XML se stáhne soubor autounattend.xml. Chcete-li tento soubor použít, jednoduše připojte stažený soubor ISO na jednotku USB, umístěte soubor autounattend.xml do kořenového adresáře a poté pokračujte v instalaci systému Windows.


Jedním z dostupných nástrojů pro vytvoření bootovacího disku USB je Rufus. Rufus dokáže vytvořit bootovací instalační flash disk systému Windows s daným instalačním souborem ISO systému Windows. Je rychlý a jednoduchý, můžete si ho stáhnout [zde](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


V tomto softwaru po výběru požadované jednotky USB a příslušného souboru ISO klikneme na tlačítko Start.


![Image](assets/en/22.webp)


V této fázi zakážeme všechny možnosti, protože jejich povolení může způsobit konflikty při použití vygenerovaného souboru Unattend. Po zkopírování souborů na jednotku USB umístíme soubor autounattend.xml do kořenového adresáře:


![Image](assets/en/23.webp)


V tomto okamžiku je jednotka USB připravena k automatické instalaci systému Windows a instalaci lze spustit pomocí této jednotky.


## Úprava ISO


Pokud potřebujete nainstalovat systém Windows do virtuálního počítače, můžete použít software pro vytváření a úpravu souborů ISO. Jedním z takových programů je AnyBurn. Po rozbalení obsahu souboru ISO staženého z webových stránek společnosti Microsoft umístěte soubor autounattend.xml do kořenového adresáře. Poté pomocí programu AnyBurn vytvořte nový soubor ISO s aktualizovaným obsahem.


AnyBurn je multifunkční software pro práci se soubory ISO. Nabízí různé funkce pro práci se soubory ISO, jednou z nich je vytváření bootovacích obrazů ISO; [zde](https://www.anyburn.com/download.php) je originální webová stránka.


Na hlavní stránce softwaru vyberte možnost "Vytvořit obrázek ze souboru/složky":


![Image](assets/en/24.webp)


Na další stránce vyberte všechny soubory extrahované z ISO spolu se souborem autounattend.xml.


![Image](assets/en/25.webp)


V tomto kroku nakonfigurujeme nastavení, aby byl soubor ISO spustitelný:


![Image](assets/en/26.webp)


V této fázi je třeba nastavit cestu k souboru bootfix.bin, aby bylo možné ISO zavést. Tento soubor se nachází v kořenovém adresáři ISO, uvnitř zaváděcí složky. Doporučuje se také v části Vlastnosti povolit možnosti ISO9660 i UDF.


![Image](assets/en/27.webp)


Po tomto kroku se kliknutím na tlačítko Další vytvoří soubor ISO. Tento soubor lze použít ve virtualizačním softwaru, jako je Oracle VirtualBox. Níže naleznete výukový program o VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65