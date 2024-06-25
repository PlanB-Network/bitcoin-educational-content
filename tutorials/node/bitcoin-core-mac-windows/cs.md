---
name: Noeud Bitcoin Core (mac & windows)
description: Instalace Bitcoin Core na Mac nebo Windows
---

Instalace Bitcoin Core na váš běžný počítač je možná, ale není to ideální. Pokud vám nevadí nechat počítač zapnutý 24/7, pak to bude fungovat dobře. Pokud potřebujete počítač vypnout, je otravné čekat, až se software po každém zapnutí znovu synchronizuje.

Tyto pokyny jsou pro uživatele Mac nebo Windows. Uživatelé Linuxu pravděpodobně mou pomoc nepotřebují, ale pokyny pro Linux jsou velmi podobné jako pro Mac.

## Začněte čistě

Ideálně byste měli použít čistý počítač, jeden bez malware. I když používáte hardware peněženku, malware vás může připravit o vaše mince.

Můžete buď kompletně vyčistit starý počítač a použít ho jako věnovaný Bitcoin počítač, nebo koupit věnovaný počítač/laptop.

## Pevný disk

Bitcoin Core zabere na vašem disku asi 400 gigabajtů dat a bude dále růst. Můžete použít interní disk, ale můžete také připojit externí pevný disk. Vysvětlím obě možnosti. Ideálně byste měli použít pevný disk typu SSD. Pokud máte starý počítač, pravděpodobně interně takový nemá. Stačí koupit externí SSD s kapacitou 1 nebo 2 terabajty a použít to. Běžný disk pravděpodobně bude fungovat, ale můžete narazit na problémy a bude to mnohem pomalejší.

![image](assets/1.webp)

## Stáhněte si Bitcoin Core

Přejděte na bitcoin.org (ujistěte se, že nejdete na bitcoin.com, což je shitcoin stránka vlastněná Rogerem Verem, která lidi klame k nákupu Bitcoin Cash místo Bitcoinu)

Až tam budete, není zvláštně zřejmé, kde software získat. Přejděte do menu zdrojů a klikněte na „Bitcoin Core“, jak je ukázáno níže:

![image](assets/2.webp)

To vás přivede na stránku ke stažení:

![image](assets/3.webp)

Klikněte na oranžové tlačítko Stáhnout Bitcoin Core:

![image](assets/4.webp)

Na výběr je několik možností, v závislosti na vašem počítači. První dvě jsou relevantní pro tento průvodce; vyberte Windows nebo Mac na levém panelu. Po kliknutí se začne stahovat, nejpravděpodobněji do vaší složky Stažené soubory.

## Ověřte stažení (část 1)

Potřebujete soubor, který obsahuje hash hodnoty různých verzí. Tento soubor býval na stránce ke stažení na bitcoin.org, ale nyní se přesunul na bitcoincore.org/en/download:

![image](assets/5.webp)

Potřebujete soubor s binárními hash hodnotami SHA256. Tento soubor obsahuje SHA256 hash hodnoty různých stahovacích balíčků Bitcoin Core.

Dále potřebujeme zahashovat stažený Bitcoin Core a porovnat to s tím, co soubor říká, že by hash hodnota měla být. Pak víme, že stažení je identické s tím, co se očekává, podle bitcoincore.org.

Přejděte znovu do složky Stažené soubory a spusťte tento příkaz (nahraďte X plným názvem souboru bitcoin node ke stažení přesně):

```bash
shasum -a 256 XXXXXXXXXXXX # <--- PRO MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- PRO WINDOWS
```

Dostanete výstup hash hodnoty. Poznamenejte si ji a porovnejte ji s hash hodnotou v souboru SHA256SUMS.

Pokud jsou výstupy identické, pak jste ověřili, že žádný bit dat nebyl pozměněn... téměř. Stále musíme být jisti, že soubor SHA256SUMS není škodlivý.

Pro pokračování v dalším kroku musíme mít na našem počítači nainstalovaný gpg.
Abychom toho dosáhli, podívejte se na můj průvodce SHA256/gpg a posuňte se přibližně do poloviny k sekci "Stáhnout gpg" a hledejte podnadpis vašeho operačního systému. Poté se vraťte zpět sem.
## Získání veřejného klíče

Zpět na stránce ke stažení získejte soubor s SHA256 hash podpisy

![obrázek](assets/6.webp)

Klikněte na něj a uložte soubor na disk, ideálně do složky Stažené soubory.

Tento soubor obsahuje podpisy různých lidí souboru SHA256SUMS.

Chceme veřejný klíč hlavního vývojáře, Wladimira J. van der Laana, na našem klíčenku počítače. Jeho ID veřejného klíče je:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Zkopírujte tento text do následujícího příkazu:

```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Pokud vás to zajímá, kdykoliv můžete zjistit, jaké klíče jsou v klíčence počítače s tímto příkazem:

```bash
gpg --list-keys
```

## Ověření stažení (část 2)

Máme veřejný klíč, takže nyní můžeme ověřit soubor SHA256SUMS, který obsahuje hashe stažení Bitcoin Core a podpis pro tyto hashe.

Otevřete znovu Terminál nebo CMD a ujistěte se, že jste ve složce Stažené soubory. Odtud spusťte tento příkaz:

```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```

První uvedený soubor je přesný pravopis souboru s podpisem. Druhý uvedený soubor by měl být přesný pravopis textového souboru obsahujícího hashe. Oba soubory by měly být ve stejné složce a vy musíte být ve složce souborů, jinak musíte zadat úplnou cestu pro každý soubor.

Toto je výstup, který byste měli dostat

![obrázek](assets/7.webp)

Varovnou zprávu je bezpečné ignorovat – to je jen připomínka, že jste se osobně nesetkali s Wladimirem na klíčové akci a nezeptali se ho, jaký je jeho veřejný klíč, a poté svému počítači neřekli, aby tomuto klíči plně důvěřoval.

Pokud jste dostali tuto zprávu, nyní víte, že soubor SHA256SUMS.asc nebyl po podepsání Wladimirem nijak pozměněn.

## Instalace Bitcoin Core

Neměli byste potřebovat podrobné instrukce, jak program nainstalovat.

![obrázek](assets/8.webp)

## Spuštění Bitcoin Core

Na Macu můžete dostat varování (Apple je stále proti Bitcoinu)

![obrázek](assets/9.webp)

Klikněte na OK a poté otevřete vaše Systémové předvolby

![obrázek](assets/10.webp)

Klikněte na ikonu Bezpečnost a soukromí:

![obrázek](assets/11.webp)

Poté klikněte na "otevřít přesto":

![obrázek](assets/12.webp)

Objeví se znovu chyba, ale tentokrát budete mít k dispozici tlačítko OTEVŘÍT. Klikněte na něj.

![obrázek](assets/13.webp)

Bitcoin Core by se měl načíst a budete mít k dispozici několik možností:

![obrázek](assets/14.webp)

Zde si můžete vybrat, zda použijete výchozí cestu, kam bude blockchain stažen, nebo můžete zvolit externí disk. Doporučuji nezměnit výchozí cestu, pokud budete používat interní disk, usnadní to nastavení, když instalujete další software pro komunikaci s Bitcoin Core.
Můžete se rozhodnout provozovat ořezaný uzel, což ušetří místo, ale omezí, co s vaším uzlem můžete dělat. Tak či onak, stejně budete stahovat celý blockchain a ověřovat ho, takže pokud máte dostatek místa, nechte si to, co jste stáhli, a neorezávejte, pokud to není nutné.
Jakmile potvrdíte, začne se blockchain stahovat. Bude to trvat mnoho dní.

![obrázek](assets/15.webp)

Počítač můžete kdykoliv vypnout a vrátit se ke stahování, pokud chcete, nezpůsobí to žádné škody.