---
name: Přidání knihy do sítě PlanB
description: Jak přidat novou knihu do sítě PlanB?
---
![book](assets/cover.webp)

Mise PlanB je poskytovat špičkové vzdělávací zdroje o Bitcoinu v co nejvíce jazycích. Veškerý obsah publikovaný na webu je open-source a hostovaný na GitHubu, což umožňuje komukoli přispět k obohacení platformy.

**Chcete přidat knihu související s Bitcoinem na web síť PlanB a zvýšit viditelnost vaší práce, ale nevíte jak? Tento tutoriál je pro vás!**
![book](assets/01.webp)
- Nejprve potřebujete mít účet na GitHubu. Pokud nevíte, jak vytvořit účet, připravili jsme podrobný tutoriál, který vás provede.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Přejděte na [GitHubový repozitář PlanB věnovaný datům](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) v sekci `resources/books/`:
![book](assets/02.webp)
- Klikněte vpravo nahoře na tlačítko `Add file`, poté na `Create new file`:
![book](assets/03.webp)
- Pokud jste předtím nikdy nepřispívali do obsahu sítě PlanB, budete muset vytvořit svůj fork původního repozitáře. Forknutí repozitáře znamená vytvoření kopie tohoto repozitáře na vašem vlastním účtu na GitHubu, což vám umožní pracovat na projektu bez ovlivnění původního repozitáře. Klikněte na tlačítko `Fork this repository`:
![book](assets/04.webp)
- Poté se dostanete na stránku GitHubu pro úpravy:
![book](assets/05.webp)
- Vytvořte složku pro vaši knihu. Chcete-li to provést, do pole `Name your file...` napište název vaší knihy malými písmeny s pomlčkami místo mezer. Například, pokud se vaše kniha jmenuje "*My Bitcoin Book*", měli byste napsat `my-bitcoin-book`:
![book](assets/06.webp)
- Pro potvrzení vytvoření složky jednoduše přidejte lomítko za název vaší knihy ve stejném poli, například: `my-bitcoin-book/`. Přidání lomítka automaticky vytvoří složku místo souboru:
![book](assets/07.webp)
- V této složce vytvoříte první YAML soubor pojmenovaný `book.yml`:
![book](assets/08.webp)
- Vyplňte tento soubor informacemi o vaší knize pomocí této šablony:

```yaml
author: 
level: 
tags:
  - 
  - 
```

Zde jsou detaily, které je třeba vyplnit pro každé pole:
- **`author`**: Uveďte jméno autora knihy.
- **`level`**: Uveďte požadovanou úroveň pro dobré pochopení knihy. Vyberte úroveň z následujících:
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**: Přidejte dva nebo tři tagy související s vaší knihou. Například:
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...

Například váš YAML soubor by mohl vypadat takto:

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![book](assets/09.webp)
- Jakmile dokončíte úpravy tohoto souboru, uložte je kliknutím na tlačítko `Commit changes...`:
![book](assets/10.webp)
- Přidejte název pro vaše změny, stejně jako krátký popis: ![book](assets/11.webp)
- Klikněte na zelené tlačítko `Propose changes` (Navrhnout změny): ![book](assets/12.webp)
- Poté se dostanete na stránku shrnující všechny vaše změny: ![book](assets/13.webp)
- Klikněte na obrázek vašeho profilu GitHub v pravém horním rohu, poté na `Your Repositories` (Vaše repozitáře): ![book](assets/14.webp)
- Vyberte svůj fork repozitáře PlanB Network: ![book](assets/15.webp)
- Na vrchu okna byste měli vidět oznámení s vaší novou větví. Pravděpodobně se jmenuje `patch-1`. Klikněte na ni: ![book](assets/16.webp)
- Nyní jste ve své pracovní větvi: ![book](assets/17.webp)
- Vraťte se do složky `resources/books/` a vyberte složku vaší knihy, kterou jste právě vytvořili v předchozím commitu: ![book](assets/18.webp)
- Ve složce vaší knihy klikněte na tlačítko `Add file` (Přidat soubor), poté na `Create new file` (Vytvořit nový soubor): ![book](assets/19.webp)
- Pojmenujte tuto novou složku `assets` a potvrďte její vytvoření umístěním lomítka `/` na konci: ![book](assets/20.webp)
- V této složce `assets` vytvořte soubor s názvem `.gitkeep`: ![book](assets/21.webp)
- Klikněte na tlačítko `Commit changes...` (Potvrdit změny...): ![book](assets/22.webp)
- Nechte název commitu ve výchozím nastavení a ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch` (Potvrdit přímo do větve patch-1), poté klikněte na `Commit changes` (Potvrdit změny): ![book](assets/23.webp)
- Vraťte se do složky `assets`: ![book](assets/24.webp)
- Klikněte na tlačítko `Add file` (Přidat soubor), poté na `Upload files` (Nahrát soubory): ![book](assets/25.webp)
- Otevře se nová stránka. Přetáhněte obrázek obálky vaší knihy do oblasti. Tento obrázek bude zobrazen na webu PlanB Network: ![book](assets/26.webp)
- Buďte opatrní, obrázek musí být ve formátu knihy, aby co nejlépe odpovídal našemu webu, například: ![book](assets/27.webp)
- Jakmile je obrázek nahrán, ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch` (Potvrdit přímo do větve patch-1), poté klikněte na `Commit changes` (Potvrdit změny): ![book](assets/28.webp)- Vezměte prosím na vědomí, že váš obrázek musí být pojmenován `cover_en`, pokud je obálka v angličtině a musí být ve formátu `.webp`. Tedy úplný název souboru by měl být `cover_en.webp`, `cover_fr.webp`, `cover_it.webp` atd. Pokud si přejete použít různé obrázky obálek pro každý jazyk, například v případě překladu knihy, můžete je umístit na stejné místo ve složce `assets`: ![book](assets/29.webp)
- Vraťte se do vaší složky `assets` a klikněte na mezi soubor `.gitkeep`: ![book](assets/30.webp)
- Jakmile jste na souboru, klikněte na 3 malé tečky v pravém horním rohu a poté na `Delete file` (Smazat soubor): ![book](assets/31.webp)
- Ujistěte se, že jste stále ve stejné pracovní větvi, poté klikněte na tlačítko `Commit changes...` (Potvrdit změny...): ![book](assets/32.webp)
- Přidejte název a popis k vašemu commitu, poté klikněte na `Commit changes` (Potvrdit změny): ![book](assets/33.webp)
- Vraťte se do složky vaší knihy:![book](assets/34.webp)
- Klikněte na tlačítko `Přidat soubor` a poté na `Vytvořit nový soubor`:
![book](assets/35.webp)
- Vytvořte nový YAML soubor tak, že ho pojmenujete s indikátorem jazyka knihy. Tento soubor bude použit pro popis knihy. Například, pokud chci napsat můj popis v angličtině, pojmenuji tento soubor `en.yml`:
![book](assets/36.webp)
- Vyplňte tento YAML soubor pomocí této šablony:
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

Zde jsou detaily, které je třeba vyplnit pro každé pole:
- **`title`**: Uveďte název knihy v uvozovkách.
- **`publication_year`**: Uveďte rok, kdy byla kniha publikována.
- **`cover`**: Uveďte název souboru odpovídajícího obrázku obálky, v souladu s jazykem YAML souboru, který právě upravujete. Například, pokud upravujete soubor `en.yml` a dříve jste přidali anglický obrázek obálky s názvem `cover_en.webp`, jednoduše uveďte `cover_en.webp` v tomto poli.
- **`description`**: Přidejte krátký odstavec popisující knihu. Popis musí být ve stejném jazyce, jak je uvedeno v názvu YAML souboru.
- **`contributors`**: Přidejte své ID přispěvatele, pokud jej máte.

Například, váš YAML soubor by mohl vypadat takto:

```yaml
title: "Moje Bitcoinová Kniha"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Objevte průkopnický svět Bitcoinu s touto komplexní příručkou určenou pro začátečníky. Moje Bitcoinová Kniha odhaluje složitosti Bitcoinu, poskytuje jasný a stručný úvod do toho, jak protokol funguje. Od jeho revoluční technologie po jeho potenciální dopad na globální ekonomiku, tato kniha nabízí cenné vhledy a praktické znalosti. Ideální pro ty, kteří jsou noví v Bitcoinu, pokrývá základy, tipy pro zabezpečení a budoucnost digitálních financí. Ponořte se do budoucnosti peněz a posilněte se vědomostmi, abyste mohli sebevědomě navigovat digitálním věkem.

contributors:
  - pretty-private

![book](assets/37.webp)
- Klikněte na tlačítko `Potvrdit změny...`:
![book](assets/38.webp)
- Ujistěte se, že je zaškrtnuto políčko `Potvrdit přímo do větve patch-1`, přidejte název, a poté klikněte na `Potvrdit změny`:
![book](assets/39.webp)
- Složka knihy by nyní měla vypadat takto:
![book](assets/40.webp)
- Pokud je pro vás vše v pořádku, vraťte se do kořenové složky vašeho forku:
![book](assets/41.webp)
- Měli byste vidět zprávu, která indikuje, že vaše větev byla upravena. Klikněte na tlačítko `Porovnat & vytvořit pull request`:
![book](assets/42.webp)
- Přidejte jasný název a popis k vašemu PR:
![book](assets/43.webp)
- Klikněte na tlačítko `Vytvořit pull request`:
![book](assets/44.webp)
Gratulujeme! Váš PR byl úspěšně vytvořen. Administrátor jej nyní zkontroluje a pokud je vše v pořádku, sloučí ho do hlavního repozitáře PlanB Network. Vaši knihu byste měli na webu vidět o několik dní později.

Nezapomeňte sledovat průběh vašeho PR. Administrátor může zanechat komentář s žádostí o dodatečné informace. Dokud váš PR není ověřen, můžete jej zobrazit na záložce `Pull requests` na GitHub repozitáři PlanB Network.
Děkujeme vám velice za váš cenný příspěvek! :)
