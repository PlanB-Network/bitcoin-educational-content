---
name: Cryptomator
description: Šifrování souborů v cloudu
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Floriana BURNELA zveřejněného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___



## I. Prezentace



V tomto návodu použijeme aplikaci Cryptomator k šifrování dat uložených v cloudu, ať už na Microsoft OneDrive, Google Drive, Dropboxu, Boxu nebo dokonce iCloudu.



Šifrování dat uložených v online úložištích, jako je Disk, je nejlepším způsobem, jak chránit své soubory a své soukromí. Díky šifrování jste jediným, kdo může vaše data dešifrovat a přečíst, i když jsou uložena na serveru v USA nebo v jiné zemi na světě.



V této ukázce bude použit počítač se systémem Windows 11 22H2 a službou OneDrive, ale postup je stejný i v jiných verzích systému Windows a jiných úložných službách. Stačí nainstalovat synchronizačního klienta a přidat účet. Tím umožníte aplikaci Cryptomator ukládat svá data do trezoru.



![Image](assets/fr/020.webp)



Cryptomator je alternativou k jiným aplikacím, zejména k Picocryptu, který byl představen v jiném článku a který vypadá jinak, ale jeho použití je stejně jednoduché. Cryptomator je také **otevřený zdrojový kód**, je kompatibilní s RGPD a **šifruje data pomocí šifrovacího algoritmu AES-256 bitů**. Naproti tomu Picocrypt spoléhá na rychlejší algoritmus XChaCha20 (rovněž 256bitový).



https://planb.academy/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Aplikace Cryptomator je k dispozici pro systémy **Windows** (exe / msi), **Linux**, **macOS,** ale také **Android** a **iOS**. Mimochodem, všechny aplikace jsou zdarma, s výjimkou aplikace pro Android, za kterou je třeba zaplatit (14,99 eur).



Ve vašem počítači **Cryptomator vytvoří složku, ve které vytvoří trezor**. V rámci trezoru, který může být uložen na vašem OneDrive, Disku Google nebo podobně, budou vaše data zašifrována. Pokud tedy uložíte všechna svá data do trezoru umístěného v úložišti na Disku, budou chráněna (protože jsou zašifrována).



**Poznámka**: v tomto článku jsou jako příklad použity služby online úložišť, ale Cryptomator lze použít k šifrování dat na místním disku, externím disku nebo dokonce na NAS. Ve skutečnosti neexistují žádná omezení.



## II. Instalace programu Cryptomator



Chcete-li začít, musíte si **stáhnout** a **nainstalovat** **Cryptomator**. Po dokončení stahování stačí k dokončení instalace několik kliknutí. Stejně jako [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/) se Cryptomator spoléhá na WinFsp, který **připojí virtuální jednotku na váš počítač se systémem Windows**.





- [Stáhnout Cryptomator z oficiálních stránek](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Používání programu Cryptomator v systému Windows



### A. Vytvoření nového trezoru



Chcete-li vytvořit nový trezor, klikněte na tlačítko "**Přidat**" a vyberte možnost "**Nový trezor...**". Vaše stávající a známé trezory v tomto počítači se poté zobrazí v levém okně Interface. **Trezor vytvořený na počítači A lze otevřít a upravit na počítači B**, pokud je vybaven programem Cryptomator (a je znám šifrovací klíč).



![Image](assets/fr/015.webp)



Začněte tím, že trezoru dáte název, například "**IT-Connect**". Tím vytvořím ve službě OneDrive adresář s názvem "**IT-Connect**".



![Image](assets/fr/011.webp)



V dalším kroku Cryptomator pravděpodobně **detekuje "jednotku "** přítomnou ve vašem počítači: Disk Google, OneDrive, Dropbox atd..... Abyste si mohli vybrat poskytovatele přímo. Zkoušel jsem to na dvou různých počítačích se systémem Windows 11 a několika jednotkami a nebyly detekovány. Není to problém, stačí definovat "**Vlastní umístění**" a vybrat kořenový prostor úložiště. Např: **C:\Users\<Username>\OneDrive**.



![Image](assets/fr/018.webp)



Dále můžete upravit možnost v části expertní nastavení.



![Image](assets/fr/021.webp)



Dále je třeba definovat **heslo odpovídající šifrovacímu klíči**. Toto heslo vám umožní **odemknout trezor Cryptomator** a získat přístup k jeho datům. **Pokud ho ztratíte, ztratíte přístup k datům**. Nakonec máte ještě možnost **vytvořit záložní klíč** zaškrtnutím možnosti "**Ano, raději bezpečně, než litovat**", podobně jako u klíče pro obnovení [BitLocker] (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). To se doporučuje, ale neukládejte tento záložní klíč v kořenovém adresáři služby OneDrive!



Klikněte na "**Vytvořit trezor**".



![Image](assets/fr/019.webp)



Zkopírujte klíč pro obnovení a uložte jej do svého oblíbeného správce hesel. Klikněte na "**Další**".



![Image](assets/fr/013.webp)



To je vše, váš nový kmen je vytvořen a připraven k použití!



![Image](assets/fr/014.webp)



### B. Přístupové údaje



Chcete-li získat přístup k trezoru a jeho datům, ať už **čtením stávajících dat nebo přidáním nových dat**, musíte jej **odemknout**. Aplikace Cryptomator zobrazuje seznam známých trezorů: zobrazí se trezor IT-Connect, takže jej jednoduše vyberte a klikněte na "**Odemknout**".



![Image](assets/fr/016.webp)



Pro odemknutí trezoru je nutné zadat heslo. Poté klikněte na "**Uvolnit jednotku**".



![Image](assets/fr/022.webp)



**Váš trezor je připojen k počítači se systémem Windows jako virtuální jednotka.** Tato jednotka, která zde zdědí písmeno E, vám umožní přístup k vašim datům (v prostém textu, protože trezor je odemčený).



![Image](assets/fr/017.webp)



Na straně OneDrive nemůžeme procházet přímo trezor Cryptomatoru. Nemůžeme vidět data (ani názvy souborů, ani jejich obsah). To znamená, že nemusíte přidávat data do trezoru Cryptomator prostřednictvím obvyklého zástupce OneDrive. **Data musíte přidat pomocí virtuální jednotky aplikace Cryptomator.**



![Image](assets/fr/012.webp)



### C. Kmenové možnosti



Nastavení trezoru je přístupné přes tlačítko "**Volby šifrovaného svazku**" (když je uzamčen) a umožňuje automatické uzamčení v případě nečinnosti, stejně jako u trezoru s heslem. Možnost "**Odemknout šifrovaný svazek při spuštění**", jak napovídá její název, odemkne jednotku bez jakéhokoli vašeho zásahu a připojí virtuální jednotku. Z bezpečnostních důvodů je lepší se aktivaci této možnosti vyhnout.



Na kartě "**Mounting**" můžete také rozhodnout o připojení pouze pro čtení nebo o přiřazení konkrétního písmene.



![Image](assets/fr/024.webp)



Kromě toho můžete v nastavení aplikace Cryptomator **povolit automatické spouštění aplikace**.



## IV. Závěr



S nástrojem **Cryptomator** můžete během několika minut **vytvořit šifrovaný trezor** a chránit tak data, která chcete ukládat do služby OneDrive a dalších. Jeho použití je velmi snadné, pokud jde o "spárování" s jednotkou: pro tento účel má mou přednost před Picocryptem.