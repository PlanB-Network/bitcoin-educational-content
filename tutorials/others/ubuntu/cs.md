---
name: Ubuntu
description: Kompletní průvodce instalací a používáním Ubuntu jako alternativy k systému Windows
---
![cover](assets/cover.webp)

## Úvod

Operační systém (OS) je hlavní software, který spravuje všechny prostředky počítače. Výběr alternativního operačního systému, jako je Ubuntu, může nabídnout mnoho výhod z hlediska bezpečnosti, nákladů a soukromí.

### Proč Ubuntu?


- Zvýšené zabezpečení** : Distribuce Linuxu jsou známé svým zabezpečením a odolností
- Nulové náklady**: Ubuntu a většina linuxových distribucí jsou zdarma
- Velká komunita**: Komunita uživatelů připravená pomoci prostřednictvím fór a výukových programů
- Respektování soukromí**: Otevřený systém pro větší transparentnost
- Jednoduchost**: Uživatelsky přívětivé rozhraní a snadné použití
- Bohatý ekosystém** : Rozsáhlý katalog softwaru s otevřeným zdrojovým kódem
- Pravidelná podpora**: Zabezpečené aktualizace od společnosti Canonical

## Instalace a konfigurace

### 1. Předpoklady

**Potřebné vybavení:**


- Klíč USB o velikosti nejméně 12 GB
- Počítač s kapacitou alespoň 25 GB

### 2. Stáhnout


- Přejděte na [ubuntu.com/download](https://ubuntu.com/download)
- Vyberte stabilní verzi (doporučuje se LTS)
- Stažení obrazu ISO

![Page de téléchargement Ubuntu](assets/fr/01.webp)

![Sélection de la version Ubuntu](assets/fr/02.webp)

### 3. Vytvoření spouštěcího klíče USB

Můžete použít několik nástrojů, například Balena Etcher :


- Stáhněte si a nainstalujte [Balena Etcher](https://etcher.balena.io/)

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)


- Otevřete Balena Etcher a vyberte obraz ISO Ubuntu
- Výběr klíče USB jako cílového média
- Klikněte na Flash a počkejte na dokončení procesu

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4. Instalace a zabezpečení Ubuntu

**4.1 Zavedení systému z paměťové karty USB** (ve francouzštině)


- Vypnutí počítače
- Připojení klíče USB (obsahujícího Ubuntu)
- Zapněte počítač. Na nejnovějších počítačích by měl systém automaticky rozpoznat spouštěcí klíč USB. Pokud tomu tak není, restartujte počítač podržením přístupové klávesy systému BIOS/UEFI (obvykle F2, F12 nebo Delete, v závislosti na značce)
 - V nabídce BIOS/UEFI vyberte jako spouštěcí zařízení klíč USB
 - Uložit a restartovat

**4.2 Spuštění instalace** (ve francouzštině)

**Startovací obrazovka**

Při zavádění z klíče USB se zobrazí tato obrazovka, která vám umožní spustit Ubuntu.

![Écran de démarrage Ubuntu](assets/fr/06.webp)

**Volba jazyka

Zvolte preferovaný jazyk instalace a systému.

![Sélection de la langue](assets/fr/07.webp)

**Možnosti přístupu

V případě potřeby nakonfigurujte možnosti přístupnosti (čtečka obrazovky, vysoký kontrast atd.).

![Options d'accessibilité](assets/fr/08.webp)

**Konfigurace klávesnice

Vyberte rozložení klávesnice. Pro kontrolu, zda klávesy odpovídají vaší konfiguraci, je k dispozici testovací pole.

![Configuration du clavier](assets/fr/09.webp)

**Síťové připojení**

Během instalace se připojte k síti Wi-Fi nebo kabelové síti, abyste mohli stahovat aktualizace.

![Configuration réseau](assets/fr/10.webp)

**Typ instalace

Vyberte si mezi možnostmi "Vyzkoušet Ubuntu" (testování bez instalace) nebo "Nainstalovat Ubuntu".

![Choix du type d'installation](assets/fr/11.webp)

**Způsob instalace

Vyberte interaktivní instalaci.

![Mode d'installation](assets/fr/12.webp)

**Výběr aplikace

Můžete si vybrat mezi výchozí instalací nebo rozšířeným výběrem aplikací.

![Sélection des applications](assets/fr/13.webp)

**Aplikace třetích stran

Rozhodněte se, zda nainstalovat další ovladače a proprietární software.

![Installation applications tierces](assets/fr/14.webp)

**Typ rozdělení

Máte dvě hlavní možnosti:


- "Vymazat disk a nainstalovat Ubuntu": použije celý disk pro Ubuntu
- "Ruční instalace: vytvoření duálního systému se systémem Windows nebo přizpůsobení oddílů

![Choix du partitionnement](assets/fr/15.webp)

**Vytvoření uživatelského účtu

Nastavte uživatelské jméno a heslo pro účet Ubuntu.

![Création du compte](assets/fr/16.webp)

**Časové pásmo

Pro nastavení systémového času vyberte zeměpisnou oblast.

![Sélection du fuseau horaire](assets/fr/17.webp)

**Shrnutí instalace**

Před zahájením konečné instalace zkontrolujte všechny možnosti. Jakmile kliknete na tlačítko "Instalovat", proces začne.

![Résumé de l'installation](assets/fr/18.webp)

**4.3 Aktualizace Ubuntu po instalaci** (ve francouzštině)

Důležitým krokem po nové instalaci je aktualizace systému. Máte dvě možnosti:

**Možnost 1: Prostřednictvím grafického uživatelského rozhraní**


- V nabídce aplikací vyhledejte položku "Software a aktualizace"
- Aplikace automaticky zkontroluje dostupné aktualizace
- Při instalaci aktualizací postupujte podle pokynů na obrazovce

**Možnost 2: Přes terminál


- Otevření terminálu (Ctrl + Alt + T)
- Zadáním následujícího příkazu zkontrolujte, zda jsou k dispozici aktualizace:

```bash
sudo apt update
```


- Po výzvě zadejte heslo
- Chcete-li nainstalovat aktualizace, zadejte příkaz :

```bash
sudo apt upgrade
```


- Instalaci potvrďte zadáním "Y" a pak zadejte Enter

### 5. Zjištění základních úkolů

**5.1 Procházení internetu

Ve výchozím nastavení najdete Firefox často na panelu spouštění.

Spusťte Firefox a začněte procházet.

Ostatní prohlížeče (Chrome, Brave atd.) lze nainstalovat prostřednictvím Správce softwaru nebo balíčků .deb.

**5.2 Zpracování textu

Ubuntu je dodáváno se sadou LibreOffice (Writer pro zpracování textu).

Jeho otevření : Aktivity > Hledat "LibreOffice Writer" nebo klikněte na ikonu, pokud se objeví na liště.

Můžete vytvářet, upravovat a ukládat dokumenty v různých formátech (včetně formátu .docx).

**5.3 Instalace aplikací

Správce softwaru (nazvaný "Ubuntu Software"): grafické rozhraní pro vyhledávání a instalaci aplikací.

V Terminálu použijte příkaz :

```bash
sudo apt install nom-du-paquet
```

Příklad:

```bash
sudo apt install vlc
```

### 6. Závěr a další zdroje

Nyní jste připraveni používat Ubuntu každý den: zabezpečit svůj systém, procházet stránky, pracovat v kanceláři, instalovat software a udržovat svůj operační systém aktuální!

Chcete-li posunout zabezpečení svého digitálního života o krok dál, doporučujeme vám podívat se na naši službu šifrovaných zpráv, která se dokonale hodí k ochraně vašeho soukromí a doplňuje vaši instalaci Ubuntu:

https://planb.network/tutorials/others/proton-mail