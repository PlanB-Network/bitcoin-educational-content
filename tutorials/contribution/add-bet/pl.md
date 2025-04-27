---
name: Dodawanie narzędzi edukacyjnych
description: Jak dodawać nowe materiały edukacyjne w PlanB Network?
---
![event](assets/cover.webp)


Misją PlanB jest dostarczanie wiodących zasobów edukacyjnych na temat Bitcoin, w jak największej liczbie języków. Wszystkie treści publikowane na stronie są open-source i hostowane na GitHub, co pozwala każdemu uczestniczyć we wzbogacaniu platformy.


Oprócz samouczków i szkoleń, PlanB Network oferuje również obszerną bibliotekę różnorodnych treści edukacyjnych na Bitcoin, dostępną dla każdego [w sekcji "BET" (_Bitcoin Educational Toolkit_)](https://planb.network/resources/bet). Baza ta obejmuje plakaty edukacyjne, memy, humorystyczne plakaty propagandowe, schematy techniczne, logo i inne narzędzia dla użytkowników. Celem tej inicjatywy jest wspieranie osób i społeczności nauczających Bitcoin na całym świecie poprzez dostarczanie im niezbędnych zasobów wizualnych.


Chcesz wziąć udział we wzbogacaniu tej bazy danych, ale nie wiesz jak? Ten poradnik jest dla ciebie!


*Konieczne jest, aby wszystkie treści zintegrowane z witryną były wolne od praw lub respektowały licencję pliku źródłowego. Ponadto wszystkie materiały wizualne publikowane w PlanB Network są udostępniane na licencji [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)

![event](assets/01.webp)


- Po pierwsze, musisz mieć konto na GitHub. Jeśli nie wiesz, jak utworzyć konto, przygotowaliśmy szczegółowy samouczek, który Cię poprowadzi.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Przejdź do [repozytorium GitHub PlanB poświęconego danym](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) w sekcji `resources/bet/`:

![event](assets/02.webp)


- Kliknij w prawym górnym rogu przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![event](assets/03.webp)


- Jeśli nigdy wcześniej nie współtworzyłeś zawartości PlanB Network, będziesz musiał utworzyć Fork oryginalnego repozytorium. Rozwidlenie repozytorium oznacza utworzenie kopii tego repozytorium na własnym koncie GitHub, co pozwala na pracę nad projektem bez wpływu na oryginalne repozytorium. Kliknij przycisk `Fork tego repozytorium`:

![event](assets/04.webp)


- Następnie przejdziesz do strony edycji GitHub:

![event](assets/05.webp)


- Utwórz folder dla swojej zawartości. Aby to zrobić, w polu `Nazwij plik...` wpisz nazwę swojej zawartości małymi literami z myślnikami zamiast spacji. W moim przykładzie powiedzmy, że chcę dodać wizualizację PDF listy BIP39 zawierającej 2048 słów. Nazwę więc mój folder `bip39-wordlist`: ![event](assets/06.webp)
- Aby potwierdzić utworzenie folderu, wystarczy dodać ukośnik po nazwie w tym samym polu, na przykład: `bip39-wordlist/`. Dodanie ukośnika automatycznie tworzy folder, a nie plik:

![event](assets/07.webp)


- W tym folderze zostanie utworzony pierwszy plik YAML o nazwie `bet.yml`:

![event](assets/08.webp)


- Wypełnij ten plik informacjami związanymi z treścią przy użyciu tego szablonu:


```yaml
builder:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


Poniżej znajdują się szczegóły do wypełnienia dla każdego pola:



- `builder`**: Wskaż identyfikator swojej organizacji w PlanB Network. Jeśli nie masz jeszcze identyfikatora "builder" dla swojej firmy, możesz go utworzyć, postępując zgodnie z tym samouczkiem.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Jeśli go nie posiadasz, możesz po prostu użyć swojego imienia i nazwiska, pseudonimu lub nazwy firmy bez konieczności tworzenia profilu budowniczego.



- `type`**: Wybierz charakter swojej zawartości spośród następujących dwóch opcji:
 - `Educational Content` dla treści edukacyjnych.
 - `Visual Content` dla innych rodzajów różnorodnej zawartości.



- `links`**: Podaj linki do swojej zawartości. Dostępne są dwie opcje:
 - Jeśli zdecydujesz się hostować swoją zawartość bezpośrednio na GitHub PlanB, będziesz musiał dodać linki do tego pliku w kolejnych krokach.
 - Jeśli Twoje treści są hostowane gdzie indziej, na przykład na Twojej osobistej stronie internetowej, wskaż tutaj odpowiednie linki:
     - `download`: Link do pobrania zawartości.
     - `view`: Link do wyświetlenia treści (może być taki sam jak link do pobrania). Jeśli zawartość jest dostępna w wielu językach, dodaj link dla każdego języka.



- `tags`**: Dodaj dwa tagi powiązane z treścią. Przykłady:
 - Bitcoin
 - technologia
 - ekonomia
 - edukacja
 - meme...



- `contributors`**: Podaj swój identyfikator współtwórcy, jeśli go posiadasz.


Przykładowo, plik YAML może wyglądać następująco:


```yaml
builder: PlanB-Network
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
Kompletna i ponumerowana lista 2048 angielskich słów ze słownika BIP39 używanych do kodowania fraz Mnemonic. Dokument można wydrukować na jednej stronie.

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```