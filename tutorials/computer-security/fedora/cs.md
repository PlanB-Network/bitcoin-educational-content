---
name: Fedora
description: Distribuce Linuxu, která vám poskytne bezplatný, kompletní a bezpečný pracovní prostor.
---


![cover](assets/cover.webp)





Fedora je svobodný operační systém s otevřeným zdrojovým kódem založený na Linuxu, který byl uveden na trh v roce 2003, vyvinutý komunitou **Fedora Project** a podporovaný společností **Red Hat Linux**. Je známý svou stabilitou, dobrým výkonem a snadným používáním, takže je vynikající volbou pro začátečníky i pokročilé uživatele. Systém běží na většině moderních procesorových architektur, takže jej lze snadno nainstalovat prakticky na jakýkoli počítač. Fedora je k dispozici také v několika předkonfigurovaných edicích, nazývaných "Fedora Spins" nebo "Fedora Editions", určených pro specifické potřeby (videohry, astronomie, vývoj...).



## Architektura systému Fedora Linux



Jak jste se dočetli dříve, Fedora je svobodný operační systém založený na jádře Linux. Jádro Linuxu je část operačního systému, která komunikuje s hardwarem počítače a spravuje systémové prostředky, jako je paměť a výpočetní výkon.



Fedora Linux obsahuje celou řadu softwarových nástrojů a aplikací, které jsou nutné k provozu operačního systému nad jádrem Linux. Modulární architektura systému Fedora znamená, že se skládá především ze souboru jednotlivých komponent, které lze podle potřeby snadno přidávat, odebírat nebo nahrazovat. To umožňuje utvářet operační systém pouze s využitím potřebných prostředků.



Součástí systému Fedora je také desktopové prostředí, což je prostředí Interface, prostřednictvím kterého uživatelé provádějí úlohy a přistupují k aplikacím. Výchozím pracovním prostředím systému Fedora je prostředí GNOME, které je uživatelsky přívětivé, snadno použitelné a vysoce přizpůsobitelné.



## Proč si vybrat Fedoru?



Mezi množstvím dostupných linuxových distribucí vyniká Fedora zejména díky:





- Modularita**: Díky kompatibilitě s různými procesorovými architekturami lze Fedoru nainstalovat na většinu počítačů, dokonce i na ty s nízkým výkonem, a dokonale se tak přizpůsobit vašim potřebám.





- Jednoduchý a intuitivní nástroj Interface**: Fedora kombinuje moderní grafické rozhraní Interface s výkonným rozhraním příkazového řádku Interface, takže je snadno použitelná pro všechny profily.





- Stabilita jádra**: Fedora, založená na platformě Red Hat, je známá spolehlivostí svých aktualizací, zejména aktualizací jádra, které jsou prováděny bez větších chyb díky bezplatným příspěvkům velké komunity.





- Rychlá a snadná instalace**: díky velikosti bitové kopie pouhé 3 GB je instalace rychlá a snadná, a to i na počítačích s omezenými zdroji.



## Edice Fedora



V závislosti na vašem profilu a způsobu použití nabízí Fedora edice, které vyhovují vašim potřebám. Najdete zde především:





- Fedora Workstation**: Tato edice je ideální pro osobní a/nebo profesionální použití na vašich počítačích a obsahuje obecné nástroje, jako jsou prohlížeče, kancelářský balík (textové editory) a software pro přehrávání médií.





- Fedora Server**: Tato edice je určena pro správu serverů. Fedora Server obsahuje řadu nástrojů, které vám pomohou nasadit a spravovat servery ve vlastním měřítku.





- Fedora CoreOS**: Chcete snadno spouštět a nasazovat cloudové aplikace? Fedora CoreOS je edice, která vám poskytne nástroje pro vytváření a správu obrazů například pomocí Dockeru a Kubernetu.



V tomto tutoriálu se budeme věnovat edici Fedora Workstation. Níže uvedené postupy jsou však podobné i pro ostatní edice.



## Instalace a konfigurace Fedora Workstation



Instalace Fedory Workstation vyžaduje následující hardwarovou konfiguraci:




- Klíč USB o velikosti alespoň **8 GB** pro spuštění operačního systému.
- Na disku Hard v počítači je nejméně **40 GB volného místa**.
- 4 GB RAM** pro plynulý provoz.



### Stáhnout Fedora Workstation



Edici [Fedora Workstation] (https://fedoraproject.org/fr/workstation/download) si můžete stáhnout z oficiálních stránek projektu Fedora. Poté vyberte verzi odpovídající architektuře vašeho procesoru (32bitová - 64bitová) a klikněte na ikonu **Stáhnout**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Vytvoření spouštěcího klíče USB



Chcete-li nainstalovat Fedoru, musíte vytvořit bootovací USB klíč pomocí softwaru, jako je [Balena Etcher](https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Po dokončení instalace programu Balena Etcher otevřete aplikaci a vyberte stažený obraz ISO Fedora Workspace. Jako cílové médium vyberte klíč USB a kliknutím na tlačítko **Flash** spusťte vytváření bootovacího klíče.



![boot](assets/fr/05.webp)


### Instalace systému Fedora



Po dokončení zavádění klíče USB vypněte počítač.


Zapněte počítač a během spouštění přejděte do systému BIOS stisknutím klávesy `F2`, `F12` nebo `ESC`, v závislosti na typu počítače.



V možnostech spouštění vyberte jako primární spouštěcí zařízení klíč USB. Potvrzením této volby se počítač restartuje a automaticky spustí instalační program Fedora** nacházející se na klíči USB.



Po spuštění počítače z paměti USB se zobrazí obrazovka **GRUB**.



V této fázi máte následující možnosti:




- Testovací média**: Tato možnost umožňuje zkontrolovat integritu USB klíče a zajistit, aby byly přítomny všechny závislosti potřebné pro správnou instalaci. Jedná se o nepovinný krok, ale doporučuje se, pokud máte o USB flash disku pochybnosti.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Spusťte Fedoru**: Spustí Fedoru v "živém" režimu bez instalace.



Na pracovní ploše Fedory (v režimu živé instalace) klikněte na **Install Fedora** (nebo Install on Hard disk) a spusťte instalační proces. Můžete zvolit pozdější instalaci a otestovat Fedoru bez nutnosti instalace.



![install-live](assets/fr/08.webp)



Prvním krokem je výběr **instalačního jazyka** a **rozložení klávesnice** systému Fedora



![language](assets/fr/10.webp)





- Výběr instalačního disku:



Vyberte disk Hard, na který chcete nainstalovat Fedoru.



Pokud je disk prázdný, Fedora automaticky využije veškeré dostupné místo. V opačném případě můžete rozdělení disku přizpůsobit (ručně nebo automaticky).



![disk](assets/fr/11.webp)





- Šifrování:



V této fázi Fedora doporučuje disk zašifrovat, abyste získali další stupeň zabezpečení Layer. Tím zajistíte, že vaše data bude moci číst pouze systém Fedora.



![chiffrement](assets/fr/12.webp)



Před spuštěním instalace zobrazí Fedora souhrn vašich voleb. Potvrďte je a kliknutím na tlačítko instalovat spusťte instalaci Fedory.



![resume](assets/fr/13.webp)



Během instalace Fedora zkopíruje soubory a nakonfiguruje systém. Po dokončení se počítač automaticky restartuje.



![installation](assets/fr/14.webp)



### Základní konfigurace


Při prvním použití je třeba dokončit několik nastavení:




- V případě potřeby změňte jazyk systému.



![language](assets/fr/15.webp)





- Vyberte si rozložení klávesnice podle svých preferencí.



![keyboard](assets/fr/16.webp)





- Zvolte časové pásmo zadáním názvu města do vyhledávacího řádku a klikněte na příslušnou nabídku.



![timezone](assets/fr/17.webp)





 - Povolte nebo zakažte přístup k poloze aplikacím, které to potřebují, a také automatické odesílání hlášení o chybách.



![location](assets/fr/18.webp)





- Rozhodněte se, zda chcete povolit úložiště softwaru třetích stran.



![logs](assets/fr/19.webp)





- Zadejte své celé jméno a definujte uživatelské jméno svého účtu.



![name](assets/fr/20.webp)





- Vytvořte si bezpečné heslo pro relaci: co nejdelší (minimálně 20 znaků), co nejnáhodnější a s různými znaky (malá a velká písmena, čísla a symboly). Nezapomeňte si heslo uložit.



![mdp](assets/fr/21.webp)



Po dokončení všech těchto kroků spusťte Fedoru a začněte ji okamžitě používat bez dalšího restartu.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Po dokončení instalace můžete konzultovat svůj domov Interface s několika předinstalovanými nástroji.



![install-now](assets/fr/09.webp)



## Objevte základní úkoly



### Procházení internetu


Výchozím prohlížečem systému Fedora je **Firefox**. Je snadno použitelný a vhodný pro většinu potřeb.


Pokud dáváte přednost jinému prohlížeči, můžete jej nainstalovat ze **správce softwaru** nebo prostřednictvím **terminálu**.


### Zpracování textu


Fedora standardně obsahuje kancelářský balík **LibreOffice**, který nabízí několik užitečných nástrojů:




- Writer** pro zpracování textu.
- Calc** pro tabulkové procesory.
- Impress** k vytváření prezentací.


## Instalace aplikací


K instalaci nových aplikací můžete použít **správce softwaru** systému Fedora (nazvaný _Software_), který instalaci usnadňuje a vizualizuje.  Použití **terminálu** je však často rychlejší a přesnější.



Před instalací jakéhokoli softwaru vždy nezapomeňte aktualizovat **úložiště** a ujistěte se, že máte přístup k nejnovějším dostupným verzím.



Následujícím příkazem pak spustíte instalaci požadované aplikace:


sudo dnf install software_name`


## Aktualizace operačního systému


Po instalaci je důležité Fedoru aktualizovat, abyste mohli využívat nejnovější bezpečnostní záplaty a aktualizace softwaru.


### Možnost 1: prostřednictvím grafiky Interface




- Otevřete **Nastavení** systému Fedora a přejděte do části **Systém**.
- Klikněte na **Aktualizace softwaru**.
- Spusťte stahování aktualizací a počkejte na dokončení procesu.



Po instalaci aktualizací může být vyžadován **restart**.


### Možnost 2: Přes terminál




- Otevřete terminál a začněte aktualizací **repozitářů**, abyste se ujistili, že máte nejnovější verze:



```shell
sudo dnf check-update
```





- Poté aktualizujte veškerý nainstalovaný software pomocí následujícího příkazu:



```shell
sudo dnf upgrade
```



Nyní je váš systém Fedora aktualizován a připraven k používání pro všechny každodenní úkoly. Objevte náš návod na Linux Mint, další distribuci Linuxu, a zjistěte, jak nastavit zdravé a bezpečné prostředí pro vaše transakce Bitcoin.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5