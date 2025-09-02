---
name: Picocrypt
description: Nástroj s otevřeným zdrojovým kódem pro šifrování dat
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Floriana BURNELA zveřejněného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním obsahu byly provedeny změny.*



___



## I. Prezentace



V tomto tutoriálu se podíváme na Picocrypt, jednoduchý, lehký a účinný šifrovací software pro šifrování dat s vysokou úrovní zabezpečení.



Je vhodný pro **šifrování souborů** a můžete jej použít k ochraně **dat v počítači, na USB flash disku**, ale také dat uložených v cloudu. Můžete například šifrovat data a ukládat je na **Microsoft OneDrive, Google Drive, iCloud nebo Dropbox**, i když pro tento účel dávám přednost jinému softwaru, který bude představen v některém z příštích článků.



Můžete jej použít i v případě, že potřebujete **sdílet data s třetí stranou**: díky Picocryptu a dešifrovacímu klíči bude moci dešifrovat data ve svém počítači. Pokud tedy dojde ke kompromitaci vašeho účtu nebo počítače, vaše data jsou chráněna.



Pro sledování projektu Picocrypt existuje pouze jeden Address:





- [Picocrypt na GitHubu](https://github.com/Picocrypt/Picocrypt)



PicoCrypt je zcela **zdarma a s otevřeným zdrojovým kódem** a je k dispozici pro **okna,** **Linux** a **macOS**. V systému Windows si jej můžete nainstalovat na vlastní počítač nebo použít přenosnou verzi.



## II. Picocrypt, šifrovací software s otevřeným zdrojovým kódem



Šifrovací software Picocrypt** se prezentuje jako **alternativa** k jiným známým řešením, jako jsou **VeraCrypt** a **Cryptomator** (*určené k šifrování dat v cloudových prostředích*) nebo **AxCrypt**. Mimochodem, na oficiálním GitHubu Picocryptu najdete srovnání s některými konkurenty:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Zdroj: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt je **velmi lehký**, váží pouhé **3 MB** a nemusí se instalovat: je to **přenosná aplikace**, jejíž výhodou je, že nevyžaduje práva správce! Nezanedbává však bezpečnost, protože se spoléhá na **odolné a spolehlivé algoritmy**:





- Šifrovací algoritmus XChaCha20**
- Funkce obcházení kláves **Argon2**



Kromě právě zmíněných výhod vás zaujme především **jeho snadné používání**!



Potřebuje jen jednu věc: **Jak je vidět z výše uvedené srovnávací tabulky (poslední řádek), je to v plánu. Ale protože se jedná o open source, nic vám nebrání podívat se na jeho zdrojový kód.



Přestože je v tabulce výše srovnáván s nástrojem BitLocker, **podle mého názoru jsou nástroje BitLocker a Picocrypt určeny k odlišnému použití**: BitLocker je určen k šifrování celého svazku (například svazku systému Windows) a Picocrypt k šifrování stromové struktury nebo úložného prostoru typu "Disk".



## III. Používání Picocryptu



Pro tuto ukázku bude použit počítač se systémem Windows 11.



### A. Šifrování dat pomocí Picocryptu



Nejprve je třeba stáhnout soubor Picocrypt.exe z oficiálního serveru GitHub ([viz tato stránka](https://github.com/Picocrypt/Picocrypt/releases)).



Otevřete aplikaci a zobrazte na obrazovce její minimalistickou verzi Interface. Chcete-li zašifrovat data, ať už **soubor, několik souborů nebo složku**, jednoduše je **přetáhněte a pusťte do aplikace Picocrypt Interface**. Tím se vyberou data, která mají být zašifrována.



![Image](assets/fr/020.webp)



V případě šifrování dat pak máte k dispozici několik možností, včetně šifrovacího klíče. Může to být **silné heslo** nebo **šifrovací klíč ve formě souboru s klíčem**, případně **obojí**. Vezmeme-li si příklad hesla, máte na výběr mezi vytvořením vlastního hesla nebo vygenerováním hesla pomocí programu Picocrypt.



Toto heslo musí být silné, protože může být použito k dešifrování dat. Zadejte jej do polí "**Heslo**" a "**Potvrdit heslo**" a poté kliknutím na "**Šifrovat**" data zašifrujte! Ještě předtím můžete kliknutím na tlačítko "**Změnit**" vedle položky "**Uložit výstup jako**" určit výstupní adresář.



**Poznámka**: Chcete-li použít klíč ve formátu souboru, klikněte na tlačítko "**Vytvořit**" napravo od položky "**Keyfiles**" a vytvořte klíč. Poté jej vyberte kliknutím na "**Upravit**" a přetažením souboru klíče na příslušnou oblast.



![Image](assets/fr/019.webp)



Oba vybrané soubory jsou **zašifrovány a seskupeny** do souboru "**Encrypted.zip.pcv**", protože **PCV** je přípona používaná programem Picocrypt. Tento soubor ZIP je díky šifrování nečitelný. Chcete-li zabránit seskupení vybraných souborů do jediného zašifrovaného souboru ZIP, musíte zaškrtnout možnost "**Rekurzivně**", aby bylo zašifrováno tolik souborů, kolik jich má být zašifrováno.



Abychom měli přístup k našim datům, musíme je dešifrovat pomocí Picocryptu.



![Image](assets/fr/023.webp)



Než si povíme něco o dešifrování dat, uvedeme si několik informací o některých dostupných možnostech:





- Paranoidní režim**: použijte nejvyšší úroveň zabezpečení, kterou Picocrypt nabízí. Nástroj použije několik kaskádových šifrovacích algoritmů (XChaCha20 a Serpent) a HMAC-SHA3 místo BLAKE2b pro ověřování dat.
- Reed-Solomon**: implementace *Reed-Solomon* kódů pro opravu chyb, které usnadňují opravu chyb u poškozených dat. To umožňuje podporovat úroveň poškození přibližně 3 % souboru.
- Rozdělit na části** nebo **rozdělit na několik částí**: pokud šifrujete velký soubor, můžete Picocrypt požádat, aby jej rozdělil na několik částí. To může usnadnit přenos souboru.
- Komprimovat soubory** nebo **Komprimovat soubory**: komprese souborů pro snížení velikosti šifrovaných souborů.
- Odstraněné soubory** nebo **Fichiers supprimés**: odstranění zdrojových souborů, aby zůstala pouze zašifrovaná verze



### B. Dešifrování dat pomocí Picocryptu



Pokud potřebujete data dešifrovat, není to o nic složitější než jejich zašifrování. Jednoduše otevřete Picocrypt a **přetáhněte soubor PCV, který chcete dešifrovat**. Poté zadejte heslo a/nebo vyberte soubor s klíčem a teprve poté klikněte na tlačítko "**Decrypt**".



![Image](assets/fr/021.webp)



Nešifrovaná verze archivu ZIP "Encrypted.zip" mi nyní umožňuje obnovit mé dva soubory v čistém textu!



![Image](assets/fr/022.webp)



## IV. Závěr



**Byli jste varováni: Picocrypt se velmi snadno používá a funguje! Přestože je Interface minimalistický, obsahuje několik velmi užitečných možností pro přizpůsobení šifrování! A protože je k dispozici v přenosné verzi, můžete si jej vzít s sebou, ať už jdete kamkoli, abyste mohli svá data bez obav dešifrovat**



Nezapomeňte používat silná hesla k ochraně dat, a pokud používáte soubor s klíčem, nezapomeňte jej zálohovat, jinak již nebudete moci dešifrovat kontejner PCV vygenerovaný programem Picocrypt. Nakonec byste měli vědět, že existuje také verze [CLI](https://github.com/Picocrypt/CLI) (s menším počtem funkcí), která umožňuje spouštět Picocrypt z příkazového řádku: i zde vám Picocrypt otevírá dveře k novým možnostem.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5