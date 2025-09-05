---
name: VirtualBox
description: Instalace VirtualBoxu ve Windows 11 a vytvoření prvního virtuálního počítače
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Floriana Burnela publikovaného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___




## I. Prezentace



V tomto návodu se dozvíte, jak nainstalovat VirtualBox do systému Windows 11 a vytvořit virtuální počítače, ať už pro provoz systému Windows 10, Windows 11, Windows Server nebo distribuce Linuxu (Debian, Ubuntu, Kali Linux atd.).



Tento úvodní kurz k VirtualBoxu vám pomůže začít pracovat s tímto open source virtualizačním řešením vyvinutým společností Oracle, které je zcela zdarma. Později budou na internetu zveřejněny další výukové materiály, které vás do této problematiky zasvětí hlouběji.



Pokud jde o virtualizaci pracovní stanice, ať už pro účely testování v rámci projektu nebo během studia IT, VirtualBox je jednoznačně dobrým řešením. Je také alternativou k dalším řešením, jako je Hyper-V, které je integrováno do systémů Windows 10 a Windows 11 (a také Windows Server), a VMware Workstation (zpoplatněné) / VMware Workstation Player (zdarma pro osobní použití).



Moje konfigurace: **Pracovní stanice s Windows 11, na kterou nainstaluji VirtualBox**, ale VirtualBox můžete nainstalovat jak na Windows 10 (nebo starší verzi), tak i na Linux. Co se týče virtuálních počítačů, VirtualBox podporuje širokou škálu systémů, včetně Windows (např. Windows 10, Windows 11, Windows Server 2022 atd.), Linux (Debian, Rocky Linux, Ubuntu, Fedora atd.), BSD (PfSense) a MacOS.



## II. Stáhnout VirtualBox pro Windows 11



Pro stažení VirtualBoxu pro instalaci do počítače se systémem Windows existuje pouze jedna dobrá stránka Address: [oficiální web VirtualBoxu](https://www.virtualbox.org/wiki/Downloads) v sekci "**Downloads**". Stačí kliknout na "Windows hosts" a začít stahovat tento spustitelný soubor, který má velikost něco málo přes 100 MB.



![Image](assets/fr/025.webp)



## III. Instalace VirtualBoxu ve Windows 11



### A. Instalace VirtualBoxu



Instalace VirtualBoxu** je jednoduchá a postup je stejný pro všechny verze systému Windows. Začněte spuštěním spustitelného souboru VirtualBoxu, který jste právě stáhli, a poté klikněte na "**Další**".



![Image](assets/fr/026.webp)



Tuto instalaci lze přizpůsobit, ale doporučuji nainstalovat všechny funkce: což je případ výchozího výběru. Na obrázku níže můžete vidět různé Elements, včetně:





- Podpora USB ve VirtualBoxu**, která umožní VirtualBoxu podporovat zařízení USB
- VirtualBox Bridged Network** pro integraci podpory sítě v režimu "Bridge" (virtuální počítač se může připojit přímo k místní síti)
- VirtualBox Host-Only Network** pro integraci podpory sítě v režimu "Host-Only" (virtuální počítač může v tomto režimu komunikovat pouze s fyzickým hostitelem Windows 11 a ostatními virtuálními počítači)



Pro pokračování klikněte na tlačítko "**Další**".



![Image](assets/fr/001.webp)



Klikněte na "**Ano**" a mějte na paměti, že **síť bude v počítači s Windows 11 na chvíli přerušena**, zatímco VirtualBox provede úpravy sítě pro podporu různých typů sítí, včetně režimu Bridge.



![Image](assets/fr/002.webp)



Po potvrzení se spustí instalace... Zobrazí se oznámení "**Chcete nainstalovat tento software zařízení?**". Zaškrtněte možnost "**Vždy důvěřovat softwaru od společnosti Oracle Corporation**" a klepněte na tlačítko "**Install**". VirtualBox skutečně potřebuje do počítače nainstalovat několik ovladačů.



![Image](assets/fr/003.webp)



Instalace je nyní dokončena! Zaškrtněte možnost "**Po instalaci spustit Oracle VM VirtualBox 6.1.34**" a kliknutím na "**Kliknout**" software spusťte.



![Image](assets/fr/004.webp)



### B. Přidání rozšiřujícího balíčku



Na oficiálních stránkách VirtualBoxu (viz předchozí odkaz) si můžete stáhnout oficiální balíček rozšíření, který je dostupný v sekci "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" po kliknutí na odkaz "**Všechny podporované platformy**". Tento balíček vám umožní přidat do VirtualBoxu další funkce: jeho přidání není povinné, ale může být užitečné! Obsahuje například podporu USB 3.0 ve virtuálních počítačích, podporu webové kamery a šifrování disku.



Otevřete VirtualBox, klikněte na "**Soubor**" a poté na "**Nastavení**" v nabídce.



![Image](assets/fr/005.webp)



Klikněte na "**Rozšíření**" vlevo (1) a poté na tlačítko "**+**" vpravo (2), abyste **nahráli balíček rozšíření VirtualBox**, který jste právě stáhli (3).



![Image](assets/fr/006.webp)



Potvrďte kliknutím na tlačítko "**Instalace**".



![Image](assets/fr/007.webp)



Klikněte na "**OK**": oficiální balíček rozšíření je nyní nainstalován ve vaší instanci VirtualBoxu!



![Image](assets/fr/008.webp)



Přejděme k vytvoření našeho prvního virtuálního počítače.



## IV. Vytvoření prvního virtuálního počítače VirtualBox



Chcete-li ve VirtualBoxu vytvořit nový virtuální počítač, jednoduše klikněte na tlačítko "**Nový**" a spusťte průvodce vytvořením virtuálního počítače. Protože jste VirtualBox spustili poprvé, rád bych vám poskytl několik dalších informací o Interface a dalších tlačítkách.





- Nastavení**: obecná konfigurace VirtualBoxu (výchozí složka virtuálního počítače, správa aktualizací, jazyk, sítě NAT, rozšíření atd.)
- Import**: import virtuálního zařízení ve formátu OVF
- Export**: export stávajícího virtuálního počítače ve formátu OVF pro vytvoření virtuálního zařízení
- Přidat**: přidání existujícího virtuálního počítače do inventáře VirtualBoxu ve standardním formátu VirtualBoxu (.vbox) nebo ve formátu XML



Vlevo v části "**Nástroje**" získáte přístup k **pokročilým funkcím, zejména pro správu virtuální sítě, ale také pro správu úložiště virtuálního počítače**. Pod položkou "**Tools**" budou později přidány vaše virtuální počítače.



![Image](assets/fr/009.webp)



### A. Proces vytváření virtuálního počítače



**Připomínáme, že VirtualBox podporuje řadu operačních systémů, včetně Windows, Linuxu a BSD. V tomto příkladu vytvořím virtuální počítač pro systém Windows 11. Je třeba vyplnit několik polí:





- Název**: název virtuálního počítače (tento název se zobrazí ve VirtualBoxu)
- Složka stroje**: místo pro uložení virtuálního počítače s vědomím, že v tomto umístění bude vytvořena podsložka s názvem virtuálního počítače
- Typ**: typ operačního systému v závislosti na tom, jaký OS chcete nainstalovat
- Verze**: verze systému, který chcete nainstalovat, v tomto případě Windows 11, tedy "**Windows11_64**"



Pro pokračování klikněte na tlačítko "**Další**".



![Image](assets/fr/010.webp)



V závislosti na operačním systému, který jste vybrali v předchozím kroku, **VirtualBox doporučí prostředky, které mají být virtuálnímu počítači přiděleny**. Zde hovoříme o paměti RAM, kterou chcete virtuálnímu počítači přidělit. Předpokládejme 4 GB, protože to je skutečně doporučeno pro systém Windows 11, ale pokud máte nedostatek prostředků, zadejte místo toho 2 GB. **Pokračování



**Poznámka**: prostředky přidělené virtuálnímu počítači lze později změnit.



![Image](assets/fr/011.webp)



Pokud jde o virtuální disk Hard, začínáme od nuly, takže musíme zvolit možnost "**Vytvořit virtuální disk Hard nyní**", aby virtuální počítač měl úložný prostor pro instalaci operačního systému a ukládání dat. Klepněte na tlačítko "**Vytvořit**".



![Image](assets/fr/012.webp)



VirtualBox podporuje tři různé formáty virtuálních disků Hard, což je zásadní rozdíl oproti jiným řešením, jako jsou VMware a Hyper-V. Na výběr jsou tři formáty:





- VDI**, oficiální formát VirtualBoxu
- VHD**, což je oficiální formát Hyper-V, ačkoli v současnosti se častěji používá nový formát VHDX
- VMDX** je oficiální formát VMware pro VMware Workstation i VMware ESXi



Chcete-li vytvořit virtuální počítač, který bude používán pouze v této instanci VirtualBoxu, vyberte možnost "**VDI**". Na druhou stranu, pokud má být virtuální disk Hard později připojen k hostiteli Hyper-V, může být vhodné začít s formátem VHD, abyste se vyhnuli nutnosti konverze. Klikněte na tlačítko "**Další**".



![Image](assets/fr/013.webp)



**Virtuální disk může mít dynamickou nebo pevnou velikost**. Pokud je dynamický, soubor, který představuje **virtuální disk (zde soubor .vdi), se bude zvětšovat podle toho, jak se na disk zapisují data**, dokud nedosáhne své maximální velikosti, ale nebude se zmenšovat, pokud budou data odstraněna. Naopak, pokud má pevnou velikost, **celý úložný prostor je alokován okamžitě (a tedy rezervován)**, což umožňuje o něco vyšší výkon, ale při prvním vytvoření virtuálního disku to trvá déle.



Osobně považuji pro testovací virtuální počítače s VirtualBoxem režim "**Dynamicky přidělené**" za dostatečný.



![Image](assets/fr/014.webp)



**Dalším krokem je zadání velikosti virtuálního disku**, přičemž je třeba mít na paměti, že ve výchozím nastavení bude disk uložen v adresáři virtuálního počítače (to lze v této fázi změnit). Uvedl jsem velikost 64 GB, abych vyhověl požadavkům systému Windows 11, ale i zde lze přiřadit menší velikost. Kliknutím na tlačítko "**Vytvořit**" vytvořte virtuální počítač!



![Image](assets/fr/015.webp)



V tuto chvíli je virtuální počítač v našem inventáři, je nakonfigurován, ale operační systém není nainstalován. Před spuštěním virtuálního počítače musíme dokončit jeho konfiguraci.



### B. Přiřazení obrazu ISO virtuálnímu počítači VirtualBoxu



K instalaci systému Windows 11 nebo jakéhokoli jiného systému potřebujeme instalační zdroje. Ve většině případů používáme k instalaci operačního systému obraz disku ve formátu ISO. **Obraz ISO systému Windows 11 je nutné nahrát do virtuální jednotky DVD našeho virtuálního počítače



Klikněte na virtuální počítač v inventáři VirtualBoxu (1) a poté na tlačítko "**Konfigurace**" (2), které zpřístupní obecnou konfiguraci tohoto virtuálního počítače. Tato nabídka slouží ke správě zdrojů (např. zvýšení paměti RAM, konfigurace procesoru atd.). Klikněte vlevo na položku "**Storage**" (3), na jednotku DVD, kde je prozatím napsáno "**Empty**" (4), poté klikněte na ikonu ve tvaru DVD (5) a "**Choose a disk file**" (**Vyberte soubor disku**).



![Image](assets/fr/016.webp)



Vyberte obraz ISO operačního systému, který chcete nainstalovat, a klikněte na tlačítko OK. Tohle se mi zobrazí:



![Image](assets/fr/017.webp)



Zůstaňte v části "**Konfigurace**" virtuálního počítače, musím ještě vysvětlit několik věcí.



### C. Síťové připojení virtuálního počítače



Přejděte do části "**Síť**" vlevo. Tato část umožňuje spravovat síť virtuálního počítače: počet virtuálních síťových rozhraní (až 4 na virtuální počítač), MAC Address a režim přístupu k síti (NAT, přístupový most, vnitřní síť atd.). **Pokud chcete, aby měl virtuální počítač přístup k internetu, vyberte možnost "NAT" nebo "Bridge Access "**, ale tento druhý režim vyžaduje, aby byl v síti aktivní server DHCP, nebo abyste museli konfigurovat IP Address ručně.



Poznámka: K síťové části se podrobněji vrátím ve zvláštním článku.



![Image](assets/fr/018.webp)



### D. Počet virtuálních procesorů



Stejně jako fyzický počítač potřebuje virtuální počítač ke svému fungování paměť RAM, disk Hard a procesor. Při vytváření virtuálního počítače jste si možná všimli, že průvodce nezahrnoval konfiguraci procesoru. Tu však můžete kdykoli nakonfigurovat prostřednictvím karty "**Systém**" a poté "**Procesor**", kde můžete zvolit počet virtuálních procesorů.



Poznámka: pro vnořenou virtualizaci je vyžadována volba "**Povolit vnořenou VT-x/AMD-v**".



V mém případě má virtuální počítač 2 virtuální procesory:



![Image](assets/fr/019.webp)



**Neváhejte se podívat do dalších částí konfigurační nabídky.



### E. První spuštění a instalace operačního systému



Chcete-li spustit virtuální počítač, jednoduše jej vyberte v inventáři a klikněte na tlačítko "**Spustit**". Otevře se druhé okno s vizuálním přehledem virtuálního počítače.



![Image](assets/fr/020.webp)



Au, objeví se mi ošklivá chyba a můj virtuální počítač se nespustí! Chyba je "Login failed for virtual machine..." s následujícími údaji:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Ve skutečnosti je to normální, protože **v mém počítači není povolena funkce virtualizace**! Chcete-li tento problém odstranit, musíte restartovat počítač, abyste získali přístup do systému BIOS a virtualizaci povolili.



![Image](assets/fr/021.webp)



Bez čekání restartuji počítač a **stisknu klávesu "SUPPR" pro přístup do systému BIOS** (klávesa se může lišit v závislosti na počítači a může to být například F2) mé základní desky ASUS. Pro aktivaci virtualizace musí být v mém případě povolen režim "SVM Mode". I zde platí, že u jednotlivých základních desek a výrobců se může název měnit. Hledejte funkci odkazující na **AMD-V** (pro procesor AMD) nebo **Intel VT-x** (pro procesor Intel).



![Image](assets/fr/022.webp)



Po provedení této úpravy ji uložte a restartujte fyzický počítač... Tentokrát může **VirtualBox spustit virtuální počítač** a načíst obraz ISO systému Windows pro instalaci operačního systému! 🙂



![Image](assets/fr/023.webp)



Na našem fyzickém hostiteli se systémem Windows 11, kde je nainstalován VirtualBox, vidíme, že složka virtuálního počítače se systémem Windows 11 obsahuje různé soubory.





- Soubor VBOX** (ve formátu XML) odpovídající konfiguraci virtuálního počítače (RAM, CPU atd.)
- Soubor VBOX-PREV** je záloha předchozí konfigurace
- Soubor VDI** odpovídá virtuálnímu disku Hard v dynamickém režimu, takže má v současné době pouze 13 GB, zatímco jeho maximální velikost je 64 GB
- Soubor NVRAM** obsahuje stav systému BIOS virtuálního počítače, který je ekvivalentem nevolatilní paměti fyzického počítače



![Image](assets/fr/024.webp)



## V. Závěr



**VirtualBox je nyní spuštěn na našem fyzickém počítači se systémem Windows 11! Zbývá jen využít jeho výhod a vytvořit virtuální počítače!** K instalaci systému Windows 11 do virtuálního počítače VirtualBox se vrátím v jiném článku. V případě Windows 10, Windows Serveru nebo linuxové distribuce (Ubuntu, Debian atd.) se nechte vést!