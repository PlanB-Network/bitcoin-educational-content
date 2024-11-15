---
name: Přidání záznamu konference
description: Jak přidat záznam z konference na síť PlanB Network?
---
![konference](assets/cover.webp)

Mise PlanB je poskytovat špičkové vzdělávací zdroje o Bitcoinu v co nejvíce jazycích. Veškerý obsah publikovaný na webu je open-source a hostovaný na GitHubu, což umožňuje komukoli přispět k obohacení platformy.

Chcete přidat záznam vaší Bitcoinové konference na web síť PlanB Network a zvýšit viditelnost této události, ale nevíte jak? Tento tutoriál je pro vás!

Pokud však chcete přidat konferenci, která se bude konat v budoucnu, doporučuji vám přečíst tento další tutoriál, ve kterém vysvětlujeme, jak přidat novou událost na web.

https://planb.network/tutorials/others/add-event


![konference](assets/01.webp)
- Nejprve potřebujete mít účet na GitHubu. Pokud nevíte, jak vytvořit účet, připravili jsme podrobný tutoriál, který vás provede.

https://planb.network/tutorials/others/create-github-account


- Přejděte na [GitHubový repozitář PlanB věnovaný datům](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) v sekci `resources/conference/`:
![konference](assets/02.webp)
- Klikněte vpravo nahoře na tlačítko `Add file` a poté na `Create new file`:
![konference](assets/03.webp)
- Pokud jste předtím nikdy nepřispívali k obsahu sítě PlanB Network, budete muset vytvořit svůj fork původního repozitáře. Forkování repozitáře znamená vytvoření kopie tohoto repozitáře na vašem vlastním účtu GitHub, což vám umožňuje pracovat na projektu bez ovlivnění původního repozitáře. Klikněte na tlačítko `Fork this repository`:
![konference](assets/04.webp)
- Poté se dostanete na stránku GitHub pro úpravy:
![konference](assets/05.webp)
- Vytvořte složku pro vaši konferenci. K tomu v poli `Name your file...` napište název vaší konference malými písmeny s pomlčkami místo mezer. Například, pokud se vaše konference jmenuje "Paris Bitcoin Conference", měli byste poznamenat `paris-bitcoin-conference`. Přidejte také rok vaší konference, například: `paris-bitcoin-conference-2024`:
![konference](assets/06.webp)
- Pro potvrzení vytvoření složky jednoduše poznamenejte lomítko za názvem ve stejném poli, například: `paris-bitcoin-conference-2024/`. Přidání lomítka automaticky vytvoří složku místo souboru:
![konference](assets/07.webp)
- V této složce vytvoříte první YAML soubor pojmenovaný `conference.yml`:
![konference](assets/08.webp)
Vyplňte tento soubor informacemi týkajícími se vaší konference pomocí této šablony:
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

Například váš YAML soubor by mohl vypadat takto:

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paříž, Francie
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - Mezinárodní
  - Veřejnost
```

![konference](assets/09.webp)
Pokud ještě nemáte pro vaši organizaci identifikátor "*builder*", můžete jej přidat podle tohoto dalšího návodu.
https://planb.network/tutorials/others/add-builder

- Jakmile dokončíte změny v tomto souboru, uložte je kliknutím na tlačítko `Commit changes...`:
![konference](assets/10.webp)
- Přidejte název pro vaše změny, stejně jako krátký popis:
![konference](assets/11.webp)
- Klikněte na zelené tlačítko `Propose changes`:
![konference](assets/12.webp)
- Poté se dostanete na stránku shrnující všechny vaše změny:
![konference](assets/13.webp)
- Klikněte na vaši profilovou fotografii GitHub v pravém horním rohu, poté na `Your Repositories`:
![konference](assets/14.webp)
- Vyberte vaši kopii repozitáře PlanB Network:
![konference](assets/15.webp)
- V horní části okna byste měli vidět oznámení s vaší novou větví. Pravděpodobně se jmenuje `patch-1`. Klikněte na ni:
![konference](assets/16.webp)
- Nyní jste ve vaší pracovní větvi:
![konference](assets/17.webp)
- Vraťte se do složky `resources/conference/` a vyberte složku vaší konference, kterou jste právě vytvořili v předchozím commitu:
![konference](assets/18.webp)
- Ve složce vaší konference klikněte na tlačítko `Add file`, poté na `Create new file`:
![konference](assets/19.webp)
- Pojmenujte tuto novou složku `assets` a potvrďte její vytvoření umístěním lomítka `/` na konci:
![konference](assets/20.webp)
- V této složce `assets` vytvořte soubor s názvem `.gitkeep`:
![konference](assets/21.webp)
- Klikněte na tlačítko `Commit changes...`:
![konference](assets/22.webp)
- Nechte název commitu ve výchozím nastavení a ujistěte se, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`:
![konference](assets/23.webp)
- Vraťte se do složky `assets`:
![konference](assets/24.webp)
- Klikněte na tlačítko `Add file`, poté na `Upload files`:
![konference](assets/25.webp)
- Otevře se nová stránka. Přetáhněte obrázek, který reprezentuje vaši konferenci a bude zobrazen na webu PlanB Network: ![konference](assets/26.webp)
- Může to být logo, miniatura nebo dokonce plakát:
![konference](assets/27.webp)
- Jakmile je obrázek nahrán, zkontrolujte, že je zaškrtnuto políčko `Commit directly to the patch-1 branch`, poté klikněte na `Commit changes`:
![konference](assets/28.webp)
- Buďte opatrní, váš obrázek musí být pojmenován `thumbnail` a musí být ve formátu `.webp`. Celý název souboru by tedy měl být: `thumbnail.webp`:
![konference](assets/29.webp)
- Vraťte se do vaší složky `assets` a klikněte na mezi soubor `.gitkeep`:
![konference](assets/30.webp)
- Jakmile jste na souboru, klikněte na 3 malé tečky v pravém horním rohu a poté na `Delete file`:
![konference](assets/31.webp)
- Ověřte, že jste stále ve stejné pracovní větvi, poté klikněte na tlačítko `Commit changes`:
![konference](assets/32.webp)
- Přidejte název a popis k vašemu commitu, poté klikněte na `Commit changes`:
![konference](assets/33.webp)
- Vraťte se do své složky konference: ![konference](assets/34.webp)
- Klikněte na tlačítko `Přidat soubor`, poté na `Vytvořit nový soubor`:
![konference](assets/35.webp)
- Vytvořte nový soubor markdown (.md) a pojmenujte ho podle indikátoru vašeho mateřského jazyka. Tento soubor bude použit pro záznamy vaší konference. Například, pokud chci psát popisy konferencí v angličtině, pojmenuji tento soubor en.md:
![konference](assets/36.webp)
- Vyplňte tento soubor markdown pomocí této šablony, kterou můžete přizpůsobit konfiguraci vaší konference:

```markdown
---
name: Pařížská Bitcoinová Konference 2024
description: Největší bitcoinová konference ve Francii s více než 8 000 účastníky každý rok!
--- 

# Hlavní scéna

## Pátek dopoledne

![video](https://youtu.be/XXXXXXXXXXXX)

## Pátek odpoledne

![video](https://youtu.be/XXXXXXXXXXXX)

## Sobota dopoledne

![video](https://youtu.be/XXXXXXXXXXXX)

## Sobota odpoledne

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshopová místnost

## Budoucnost těžby Bitcoinu: Výzvy a inovace

![video](https://youtu.be/XXXXXXXXXXXX)

Přednášející: Satoshi Nakamoto, Satoshi Nakamoto

## Je soukromí na Bitcoinu stále možné?

![video](https://youtu.be/XXXXXXXXXXXX)

Přednášející: Satoshi Nakamoto

## Bitcoin Core: Hluboký ponoření do zdrojového kódu

![video](https://youtu.be/XXXXXXXXXXXX)

Přednášející: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Vytváření a zabezpečení Bitcoinových peněženek s Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Přednášející: Satoshi Nakamoto
```

![konference](assets/37.webp)
- Na začátku vašeho dokumentu, v "úvodní části", vyplňte pole `name:` názvem vaší konference a rokem záznamů. Do pole `description:` napište krátký popis vaší akce v jazyce souboru. Například pro soubor pojmenovaný `en.md` by popis měl být v angličtině. Tým PlanB Network se postará o překlad vašeho popisu pomocí jejich modelu.
- Nadpisy první úrovně, označené `#`, se používají k organizaci konference podle scén. Například `# Hlavní scéna` pro hlavní scénu a `# Workshopová místnost` pro scénu věnovanou workshopům.

- Nadpisy druhé úrovně, označené dvojitým `##`, se používají k oddělení různých záznamů videí. Pokud byly konference natáčeny nepřetržitě přes půl dne, uveďte například `## Pátek dopoledne`. Pokud byly konference natáčeny a vysílány jednotlivě, pojmenujte konferenci přímo druhým nadpisem.

- Pod každým nadpisem druhé úrovně vložte odkaz na odpovídající záznam videa. Syntaxe by měla být: `![video](https://youtu.be/XXXXXXXXXXXX)`, kde `XXXXXXXXXXXX` nahradíte skutečným odkazem na video.

- Pokud formát dovoluje (jednotlivé konference), můžete přidat jména přednášejících. K tomu přidejte pole `Přednášející:` následované jménem nebo pseudonymem přednášejícího pod odkazem na video. V případě více přednášejících oddělte každé jméno čárkou, například takto: `Přednášející: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Jakmile dokončíte úpravy tohoto souboru, uložte je kliknutím na tlačítko `Commit changes...`:
![konference](assets/38.webp)
- Přidejte název pro vaše úpravy, stejně jako krátký popis:
![konference](assets/39.webp)
- Klikněte na `Commit changes`: ![konference](assets/40.webp)
- Složka vaší konference by nyní měla vypadat takto:
![konference](assets/41.webp)
- Pokud je vše k vaší spokojenosti, vraťte se do kořenového adresáře vašeho forku:
![konference](assets/42.webp)
- Měli byste vidět zprávu, která indikuje, že vaše větev prošla modifikacemi. Klikněte na tlačítko `Compare & pull request`:
![konference](assets/43.webp)
- Přidejte jasný titulek a popis pro váš PR:
![konference](assets/44.webp)
- Klikněte na tlačítko `Create pull request`:
![konference](assets/45.webp)
Gratulujeme! Váš PR byl úspěšně vytvořen. Administrátor jej nyní zkontroluje a pokud je vše v pořádku, sloučí ho do hlavního repozitáře PlanB Network. Záznamy vaší konference by se na webu měly objevit o několik dní později.

Prosím, sledujte průběh vašeho PR. Je možné, že administrátor zanechá komentář s žádostí o dodatečné informace. Dokud není váš PR validován, můžete si jej prohlížet pod záložkou `Pull requests` na GitHub repozitáři PlanB Network:
![konference](assets/46.webp)

Moc vám děkujeme za váš cenný příspěvek! :)
