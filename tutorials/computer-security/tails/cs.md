---
name: Tails

description: Instalace Tails na USB klíč
---

![image](assets/cover.webp)

Přenosný a amnestický operační systém, který vás chrání před sledováním a cenzurou.

## Proč mít USB klíč s nainstalovaným Tails?

Tails (https://tails.net/) je nejjednodušší způsob, jak mít kdykoliv k dispozici bezpečný počítač, který po použití na jakémkoliv počítači nezanechá žádné stopy.

Chcete-li používat Tails, vypněte počítač, ke kterému máte přístup (u rodičů, u přátel, v internetové kavárně...) a spusťte ho s vaším USB klíčem Tails místo Windows, macOS nebo Linuxu.

Poté budete mít pracovní prostředí a komunikační prostředí nezávislé na obvyklém operačním systému, které nikdy nepoužívá pevný disk.

Tails nikdy nepíše na pevný disk a k fungování používá pouze RAM počítače. Tato paměť je při vypnutí Tails úplně smazána, čímž se odstraní všechny možné stopy.

## Několik konkrétních případů použití

Abychom vám dali konkrétní představy o výhodách mít vždy u sebe USB klíč s Tails, zde je malý neúplný seznam sestavený týmem Agora256:

- Připojení k internetu a Toru necenzurovaným a anonymním způsobem pro prohlížení webových stránek bez zanechání stop;
- Otevření PDF ze podezřelého webu;
- Test vaší zálohy soukromého klíče Bitcoin s peněženkou Electrum;
- Použití kancelářského balíku (LibreOffice) a práce na počítači, který vám nepatří;
- První kroky v prostředí Linuxu, abyste se naučili opustit svět Microsoftu a Apple.

## Jak důvěřovat Tails?

Při používání softwaru je vždy prvek důvěry, ale nemusí být slepá. Nástroj jako Tails musí usilovat o poskytnutí prostředků svým uživatelům, aby byl důvěryhodný. Pro Tails to znamená:

- Veřejný zdrojový kód: https://gitlab.tails.boum.org/;
- Projekt založený na renomovaných projektech: Tor a Debian;
- Ověřitelné a reprodukovatelné stažení;
- Doporučení různých jednotlivců a organizací.

## Instalační a uživatelská příručka

Účelem této instalační příručky je provést vás každým krokem instalace. Nebudeme popisovat akce, které mají být provedeny více než oficiální příručka, ale ukážeme vám správný směr, přičemž vám poskytneme tipy a triky.

Z důvodu praktických zkušeností budou tyto tipy zaměřeny na platformy macOS a Linux.
🛠️
Před zahájením tohoto postupu se prosím ujistěte, že máte USB klíč s minimální rychlostí čtení 150 MB/s a kapacitou alespoň 8 GB, ideálně USB 3.0.

Předpoklady:

- 1 USB klíč, pouze pro Tails, s kapacitou alespoň 8 GB
- Počítač připojený k internetu s Linuxem, macOS (nebo Windows)
- Přibližně jedna hodina volného času, v závislosti na rychlosti vašeho internetového připojení, včetně ½ hodiny na instalaci (soubor ke stažení o velikosti 1,3 GB)

## Krok 1: Stáhněte Tails do svého počítače

![image](assets/1.webp)

> 🔗 Oficiální sekce Tails: https://tails.net/install/linux/index.fr.html#download

Stažení instalačního souboru s příponou .img může trvat nějaký čas v závislosti na rychlosti vašeho internetového stahování, takže plánujte dopředu. S moderním a efektivním připojením to zabere méně než 5 minut.

Uložte soubor do známé složky, například Stahování, protože to bude nutné pro další krok.

## Krok 2: Ověřte své stažení

![image](assets/2.webp)
🔗 Oficiální sekce Tails: https://tails.net/install/linux/index.fr.html#verify
Ověření staženého souboru zajišťuje, že pochází od vývojářů Tails a nebyl poškozen nebo zachycen během stahování.

Je možné ručně ověřit, že soubor, který jste právě stáhli, je očekávaný pomocí PGP, ale bez pokročilých znalostí nabízí toto ověření stejnou úroveň bezpečnosti jako ověření pomocí JavaScriptu na stránce ke stažení, přičemž je mnohem složitější a náchylnější k chybám.

Pro ověření souboru použijte tlačítko "Select your download..." poskytnuté v oficiální sekci!

## Krok 3: Instalace Tails na váš USB klíč

![obrázek](assets/3.webp)

> 🔗 Oficiální sekce Tails:
>
> - Linux: https://tails.net/install/linux/index.fr.html#install
> - macOS: https://tails.net/install/mac/index.fr.html#etcher a https://tails.net/install/mac/index.fr.html#install

Tento krok instalace Tails na váš USB klíč je nejtěžší v celém průvodci, zejména pokud jste to nikdy předtím nedělali. Nejdůležitější je vybrat správný postup v oficiální sekci pro váš operační systém: Linux nebo macOS.

Jakmile jsou nástroje nainstalovány a připraveny podle doporučení, soubor s příponou .img lze zkopírovat na váš klíč (smazat všechna existující data), aby byl "bootovatelný" samostatně.

Hodně štěstí! a uvidíme se u kroku 4.

## Krok 4: Restart na vašem USB klíči Tails

![obrázek](assets/4.webp)

> 🔗 Oficiální sekce Tails: https://tails.net/install/linux/index.en.html#restart
> Je čas spustit jeden z vašich počítačů pomocí vašeho nového USB klíčku. Vložte jej do jednoho z jeho USB portů a restartujte!

> 💡 Většina počítačů automaticky nebootuje z USB klíčku Tails, ale můžete stisknout klávesu bootovacího menu, aby se zobrazil seznam možných zařízení, ze kterých lze bootovat.

Pro určení, kterou klávesu byste měli stisknout, abyste měli bootovací menu, které vám umožní vybrat USB klíč místo vašeho obvyklého pevného disku, zde je neúplný seznam podle výrobce:

| Výrobce | Klávesa          |
| ------- | ---------------- |
| Acer    | F12, F9, F2, Esc |
| Apple   | Option           |
| Asus    | Esc              |
| Clevo   | F7               |
| Dell    | F12              |
| Fujitsu | F12, Esc         |
| HP      | F9               |
| Huawei  | F12              |
| Intel   | F10              |
| Lenovo  | F12              |
| MSI     | F11              |
| Samsung | Esc, F12, F2     |
| Sony    | F11, Esc, F10    |
| Toshiba | F12              |
| ostatní... | F12, Esc         |

Jakmile je USB klíč vybrán, měli byste vidět tento nový bootovací obrazovku, což je velmi dobré znamení, takže nechte počítač pokračovat v bootování...

![obrázek](assets/5.webp)

## Krok 5: Vítejte v Tails!

![obrázek](assets/6.webp)

> 🔗 Oficiální sekce Tails: https://tails.net/install/linux/index.en.html#tails

Jednu nebo dvě minuty po bootovacím načítači a načítací obrazovce se objeví uvítací obrazovka.

![obrázek](assets/7.webp)

Na uvítací obrazovce vyberte svůj jazyk a rozložení klávesnice v sekci Jazyk & Region. Klikněte na Start Tails.

![obrázek](assets/8.webp)
Pokud váš počítač není připojen k vaší síti kabelem, prosím, odkážete se na oficiální instrukce Tails, které vám pomohou se připojit k vaší síti bez Wi-Fi (sekce "Test your Wi-Fi").
Jakmile budete připojeni k lokální síti, objeví se průvodce Tor Connection, který vám pomůže se připojit k síti Tor.

![obrázek](assets/9.webp)

Můžete začít anonymně prohlížet, prozkoumávat možnosti a software zahrnutý v Tails. Užijte si to, máte spoustu prostoru pro chyby, protože na USB klíči se nic nemodifikuje... Váš další restart zapomene na všechny vaše zkušenosti!

## V budoucím průvodci...

Jakmile si trochu více pohrajete se svým vlastním USB klíčem Tails, prozkoumáme další pokročilá témata v dalším článku, jako jsou:

> Aktualizace klíče s nejnovější verzí Tails; Konfigurace a používání trvalého úložiště; Instalace dalšího softwaru.
> Do té doby, jako vždy, pokud máte jakékoli otázky, neváhejte je sdílet s komunitou Agora256. Učíme se společně, abychom byli zítra lepší než dnes!