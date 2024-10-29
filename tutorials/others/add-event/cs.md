---
name: Přidání události na síť PlanB
description: Jak mohu navrhnout přidání nové události na síť PlanB?
---
![event](assets/cover.webp)

Mise PlanB je poskytovat špičkové vzdělávací zdroje o Bitcoinu v co nejvíce jazycích. Veškerý obsah publikovaný na webu je open-source a hostován na GitHubu, což nabízí každému možnost přispět k obohacení platformy.

Pokud chcete přidat konferenci o Bitcoinu na web síť PlanB a zvýšit viditelnost vaší události, ale nevíte jak? Tento tutoriál je pro vás!
![event](assets/01.webp)
- Nejprve potřebujete mít účet na GitHubu. Pokud nevíte, jak vytvořit účet, připravili jsme podrobný tutoriál, který vás provede.

https://planb.network/tutorials/others/create-github-account


- Přejděte na [GitHubový repozitář PlanB věnovaný datům](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) v sekci `resources/conference/`:
![event](assets/02.webp)
- Klikněte vpravo nahoře na tlačítko `Add file`, poté na `Create new file`:
![event](assets/03.webp)
- Pokud jste nikdy předtím nepřispívali k obsahu sítě PlanB, budete muset vytvořit svůj fork původního repozitáře. Forknutí repozitáře znamená vytvoření kopie tohoto repozitáře na vašem vlastním účtu GitHub, což vám umožní pracovat na projektu bez ovlivnění původního repozitáře. Klikněte na tlačítko `Fork this repository`:
![event](assets/04.webp)
- Poté se dostanete na stránku GitHubu pro úpravy:
![event](assets/05.webp)
- Vytvořte složku pro vaši konferenci. Chcete-li to provést, do pole `Name your file...` napište název vaší konference malými písmeny s pomlčkami místo mezer. Například, pokud se vaše konference jmenuje "Paris Bitcoin Conference", měli byste poznamenat `paris-bitcoin-conference`. Také přidejte rok vaší konference, například: `paris-bitcoin-conference-2024`:
![event](assets/06.webp)
- Pro potvrzení vytvoření složky jednoduše poznamenejte lomítko za názvem ve stejném poli, například: `paris-bitcoin-conference-2024/`. Přidání lomítka automaticky vytvoří složku místo souboru:
![event](assets/07.webp)
- V této složce vytvoříte první YAML soubor pojmenovaný `events.yml`:
![event](assets/08.webp)
- Vyplňte tento soubor informacemi o vaší konferenci pomocí této šablony:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

Například váš YAML soubor by mohl vypadat takto:

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Paříž, Francie
  address_line_2: 
  address_line_3: 
  name: Pařížská Bitcoinová Konference 2024
  builder: Pařížská Bitcoinová Konference
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
```yaml
description: Největší konference o Bitcoinu ve Francii s více než 8 000 účastníky každý rok!
language:
    - fr
    - en
    - es
    - it
links:
    website: https://paris.bitcoin.fr/conference
    replay_url:
    live_url:
tags:
    - Bitcoiner
    - General
    - International
```
![událost](assets/09.webp)
Pokud ještě nemáte pro vaši organizaci identifikátor "*builder*", můžete jej přidat podle tohoto dalšího návodu.

https://planb.network/tutorials/others/add-builder



- Jakmile dokončíte úpravy tohoto souboru, uložte je kliknutím na tlačítko `Commit changes...`:
![událost](assets/10.webp)
- Přidejte název pro vaše změny, stejně jako krátký popis:
![událost](assets/11.webp)
- Klikněte na zelené tlačítko `Propose changes`:
![událost](assets/12.webp)
- Poté se dostanete na stránku shrnující všechny vaše změny:
![událost](assets/13.webp)
- Klikněte na vaši profilovou fotografii v pravém horním rohu, poté na `Your Repositories`:
![událost](assets/14.webp)
- Vyberte váš fork repozitáře PlanB Network:
![událost](assets/15.webp)
- Na vrchu okna byste měli vidět oznámení s vaší novou větví. Pravděpodobně se jmenuje `patch-1`. Klikněte na ni:
![událost](assets/16.webp)
- Nyní jste ve vaší pracovní větvi:
![událost](assets/17.webp)
- Vraťte se do složky `resources/conference/` a vyberte složku vaší konference, kterou jste právě vytvořili v předchozím commitu:
![událost](assets/18.webp)
- Ve složce vaší konference klikněte na tlačítko `Add file`, poté na `Create new file`:
![událost](assets/19.webp)
- Pojmenujte tuto novou složku `assets` a potvrďte její vytvoření pomocí lomítka `/` na konci:
![událost](assets/20.webp)
- V této složce `assets` vytvořte soubor s názvem `.gitkeep`:
![událost](assets/21.webp)
- Klikněte na tlačítko `Commit changes...`:
![událost](assets/22.webp)
- Nechte název commitu ve výchozím nastavení a ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`:
![událost](assets/23.webp)
- Vraťte se do složky `assets`:
![událost](assets/24.webp)
- Klikněte na tlačítko `Add file`, poté na `Upload files`: ![událost](assets/25.webp)
- Otevře se nová stránka. Přetáhněte obrázek, který reprezentuje vaši konferenci a bude zobrazen na webu PlanB Network:
![událost](assets/26.webp)
- Může to být logo, miniatura nebo dokonce plakát:
![událost](assets/27.webp)
- Jakmile je obrázek nahrán, ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`:
![událost](assets/28.webp)
- Pozor, váš obrázek musí být pojmenován `thumbnail` a musí být ve formátu `.webp`. Celý název souboru by tedy měl být: `thumbnail.webp`:
![událost](assets/29.webp)
- Vraťte se do vaší složky `assets` a klikněte na mezi soubor `.gitkeep`:
![událost](assets/30.webp)
- Jakmile budete na souboru, klikněte na 3 malé tečky v pravém horním rohu a poté na `Smazat soubor`: ![událost](assets/31.webp)
- Ověřte, že jste stále na stejné pracovní větvi, poté klikněte na tlačítko `Commit changes` (Potvrdit změny):
![událost](assets/32.webp)
- Přidejte název a popis k vašemu commitu, poté klikněte na `Commit changes` (Potvrdit změny):
![událost](assets/33.webp)
- Vraťte se do kořenového adresáře vašeho repozitáře:
![událost](assets/34.webp)
- Měli byste vidět zprávu, která indikuje, že vaše větev prošla změnami. Klikněte na tlačítko `Compare & pull request` (Porovnat a vytvořit pull request):
![událost](assets/35.webp)
- Přidejte jasný název a popis k vašemu PR (pull requestu):
![událost](assets/36.webp)
- Klikněte na tlačítko `Create pull request` (Vytvořit pull request):
![událost](assets/37.webp)
Gratulujeme! Váš PR byl úspěšně vytvořen. Administrátor jej nyní zkontroluje a pokud bude vše v pořádku, začlení jej do hlavního repozitáře sítě PlanB. Vaši událost byste měli na webu vidět několik dní poté.

Nezapomeňte sledovat průběh vašeho PR. Administrátor vám může zanechat komentář s žádostí o dodatečné informace. Dokud váš PR není schválen, můžete jej konzultovat na záložce `Pull requests` (Pull requesty) na GitHub repozitáři sítě PlanB:
![událost](assets/38.webp)
Moc vám děkujeme za vaši cennou příspěvek! :)
