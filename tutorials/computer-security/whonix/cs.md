---
name: Whonix
description: Zachovejte své soukromí a důvěrnost.
---

![cover](assets/cover.webp)



**Whonix** je linuxová distribuce založená na **Debianu**, navržená tak, aby poskytovala prostředí kombinující **bezpečnost**, **anonymitu** a **soukromí**. Snadno se učí a je kompatibilní s různými rozhraními (virtuální počítače, Qubes OS, Live mode), ve výchozím nastavení obsahuje směrování síťového provozu přes **Tor**, **dvojitý firewall** (jeden firewall na bráně a druhý na pracovní stanici), **plnou ochranu proti úniku IP/DNS** a nástroje pro účinné maskování vaší aktivity před pozorovateli sítě, včetně vašeho poskytovatele internetových služeb. **Whonix** je více než jen anonymní systém, je to kompletní bezpečné vývojové prostředí.



## Proč si vybrat společnost Whonix?





- Zdarma**: Stejně jako většina linuxových distribucí je i Whonix open-source systém licencovaný zcela zdarma. Je vyvíjen jako open source, s aktivní a transparentní komunitou.
- Soukromí, bezpečnost a anonymita**: Hlavním cílem společnosti Whonix je nabídnout mimořádně bezpečné prostředí, ve kterém jsou všechna vaše data chráněna a vaše komunikace šifrována prostřednictvím sítě Tor.
- Snadné použití**: Whonix nabízí intuitivní, předem nakonfigurovanou grafickou aplikaci Interface, vhodnou i pro začínající uživatele. Není třeba být odborníkem, abyste mohli využívat výhod pokročilé ochrany.
- Ideální prostředí pro bezpečný vývoj**: Whonix vám umožní vyvíjet, testovat, kontrolovat nebo spouštět programy, aniž byste odhalili svou skutečnou IP adresu Address nebo prozradili své zvyky při prohlížení webu nebo síťové komunikaci.
- Jednorázové relace a režim Live**: Whonix lze spustit v režimu Live nebo prostřednictvím jednorázových počítačů (např. prostřednictvím **Qubes OS**), což umožňuje provádět kritické úlohy bez zanechání trvalých stop po ukončení relace.
- Relativně jednoduchá instalace**: Pro rychlou instalaci do virtuálních počítačů (VirtualBox, KVM, Qubes) jsou dodávány obrazy připravené k použití. Systém je zdokumentován a pravidelně aktualizován.



## Instalace a konfigurace



Než přejdeme k instalaci Whonixu, je nutné upozornit, že tato distribuce **zatím není oficiálně dostupná** jako hlavní systém, který lze nainstalovat přímo na disk Hard (v režimu holého kovu). Jinými slovy, Whonix zatím **nemůžete nainstalovat jako klasický hlavní operační systém**, jako je Ubuntu nebo standardní Debian.



K dispozici je však několik edic, které umožňují používat Whonix **volatilně** (režim Live, dočasné relace) nebo **trvale** (prostřednictvím virtuálních počítačů nebo integrace do operačního systému Qubes).



Pro dlouhodobé a stabilní používání je v současné době jedinou oficiálně doporučenou metodou **virtualizace**. Systém Whonix můžete provozovat pomocí **VirtualBox** (Whonix-Gateway a Whonix-Workstation) nebo jej integrovat do systému, jako je **Qubes OS**. V tomto návodu se zaměříme na instalaci ve VirtualBoxu.



### Předpoklady



Před instalací systému Whonix ve virtuálním režimu se ujistěte, že váš počítač splňuje minimální technické požadavky. Virtualizace vyžaduje určité prostředky, které ne všechny počítače mohou nabídnout. Proto je nezbytné, aby váš procesor podporoval technologii virtualizace (Intel VT-x nebo AMD-V) a aby tato možnost byla povolena v systému BIOS/UEFI.



Zde jsou doporučené specifikace pro hladký a stabilní provoz zařízení Whonix:





- Paměť RAM (Random Access Memory)**: doporučuje se minimálně **8 GB**. Čím více paměti RAM máte, tím více prostředků můžete přidělit virtuálním počítačům (Gateway a Workstation) a zvýšit tak jejich výkon.
- Dostupné místo na disku**: počítejte s minimálně 30 GB volného místa na disku**. To zahrnuje prostor potřebný pro dva virtuální počítače, systémové soubory a veškerá data nebo snímky.
- Procesor**: doporučuje se procesor s alespoň **4 fyzickými jádry** (8 logických vláken), zejména pokud chcete paralelně spouštět další služby nebo nástroje.



### Stáhnout Whonix



Systém Whonix je k dispozici v několika edicích podle typu prostředí, ve kterém jej chcete používat. Pro většinu uživatelů (Windows, Linux nebo MacOs) je nejjednodušší nastavit edici VirtualBox. Obraz si můžete stáhnout přímo z [oficiálních webových stránek](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **není kompatibilní** s MacBooky s procesory Apple Silicon (architektura ARM).



## Instalace VirtualBoxu



Pro spuštění systému Whonix budete potřebovat **hypervisor**, jako je VirtualBox, Qubes nebo KVM.



Po stažení souboru jej nainstalujte stejně jako jakýkoli jiný software. Přijměte výchozí možnosti, pokud nemáte specifické požadavky. Ztratili jste se? Podívejte se na našeho průvodce používáním VirtualBoxu.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Importování aplikace Whonix



Po instalaci VirtualBoxu můžete importovat dříve stažené soubory `.ova` společnosti Whonix (`Whonix-Gateway-Xfce.ova` a `Whonix-Workstation-Xfce.ova`).



Otevřete VirtualBox a klikněte na **Soubor → Importovat zařízení**.


Vyberte příslušný soubor `.ova` (začněte bránou).



![0_03](assets/fr/03.webp)



Vyberte umístění, kam budou uloženy soubory virtuálního počítače Whonix.



![0_04](assets/fr/04.webp)



Přijměte podmínky použití, spusťte import a počkejte na dokončení procesu.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Konfigurace Whonix



Před spuštěním aplikace Whonix je důležité upravit některá **systémová nastavení**, aby byl zajištěn lepší výkon:



Vyberte virtuální počítač **Whonix-Workstation-Xfce** a klikněte na **Konfigurace**.



![0_06](assets/fr/07.webp)



Přejděte na kartu **Systém**, kde je výchozí přidělení paměti RAM 2048 MB. Doporučujeme ji **zvýšit na 4096 MB (4 GB)** pro větší plynulost, zejména pokud hodláte otevírat více aplikací nebo pracovat v dlouhých relacích. Brána může zůstat na 2048 MB, pokud nepoužíváte mnoho paralelních připojení Tor.



![0_08](assets/fr/08.webp)



### Začínáme se společností Whonix



Aby systém Whonix fungoval správně a bezpečně, **musíte dodržet tuto spouštěcí sekvenci**:



Nejprve spusťte počítač **Whonix-Gateway-Xfce**. Tento stroj je zodpovědný za směrování veškerého provozu přes síť **Tor**. Bez spuštěné brány nebude přes Tor směrován žádný provoz a ztratíte anonymitu.



![0_09](assets/fr/09.webp)



Jakmile je brána plně spuštěna (uvidíte připojený Tor), můžete spustit **Whonix-Workstation-Xfce**, který se automaticky připojí přes bránu.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Aktualizace systému



Vstupte do terminálu a vložte následující příkaz pro aktualizaci seznamu balíčků:



```shell
sudo apt update
```



Poté spusťte následující příkaz a nainstalujte dostupné aktualizace:



```shell
sudo apt full-upgrade
```



## Objevte Whonix



**Whonix** je systém navržený tak, aby poskytoval **bezpečné**, **anonymní** a **důvěrné** počítačové prostředí, ideální pro surfování po internetu bez ohrožení vaší identity nebo vašich dat. K dosažení tohoto cíle je dodáván s řadou užitečných každodenních aplikací, které jsou navrženy tak, aby hned od začátku posílily vaši digitální bezpečnost.


### KeepassXC



**KeePassXC** je integrovaný správce hesel společnosti Whonix. Umožňuje **bezpečně vytvářet, ukládat a spravovat** hesla, aniž byste si je museli všechna pamatovat ručně. Hesla jsou uložena v **šifrované databázi** chráněné hlavním heslem.



### Prohlížeč Tor



**Tor Browser** je výchozím webovým prohlížečem společnosti Whonix. Spoléhá se na síť **Tor**, která přesměrovává váš provoz přes několik relé po celém světě, takže je prakticky nemožné identifikovat vaši skutečnou IP adresu Address.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** je lehký a rychlý Bitcoin Wallet, předinstalovaný na Whonixu, který vám umožní anonymně spravovat **transakce s kryptoměnami**. Nestahuje celý Blockchain, ale k získání potřebných informací využívá vzdálené servery, takže je mnohem lehčí než plnohodnotný Wallet.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix je víc než jen operační systém: je to skutečné **bezpečné prostředí** navržené tak, aby chránilo vaši anonymitu, soukromí a citlivé činnosti. Díky architektuře založené na technologii Tor, inteligentnímu rozdělení mezi bránu a pracovní stanici a předinstalovaným nástrojům, jako jsou Tor Browser, KeePassXC a Electrum, nabízí hotové řešení pro každého, kdo chce **prohlížet anonymně**, **bezpečně pracovat** nebo **pracovat s důvěrnými daty**.



Chcete-li posílit zabezpečení svého systému Unix, podívejte se na náš návod na auditování počítače: zkontrolujte, zda v operačním systému nejsou bezpečnostní díry, a ujistěte se, že vaše data nejsou ohrožena.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af