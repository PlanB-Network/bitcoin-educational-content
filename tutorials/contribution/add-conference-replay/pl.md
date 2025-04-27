---
name: Dodawanie powtórki konferencji
description: Jak dodać powtórkę konferencji w PlanB Network?
---
![conference](assets/cover.webp)


Misją PlanB jest dostarczanie najwyższej jakości zasobów edukacyjnych na temat Bitcoin w jak największej liczbie języków. Wszystkie treści publikowane na stronie są open-source i hostowane na GitHub, dzięki czemu każdy może przyczynić się do wzbogacenia platformy.


Czy chcesz dodać powtórkę swojej konferencji Bitcoin na stronie PlanB Network i zapewnić widoczność tego wydarzenia, ale nie wiesz jak? Ten poradnik jest dla Ciebie!


Jeśli jednak chcesz dodać konferencję, która odbędzie się w przyszłości, radzę przeczytać ten samouczek, w którym wyjaśniamy, jak dodać nowe wydarzenie do witryny.


https://planb.network/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- Po pierwsze, musisz mieć konto na GitHub. Jeśli nie wiesz, jak utworzyć konto, przygotowaliśmy szczegółowy samouczek, który Cię poprowadzi.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Przejdź do [repozytorium GitHub PlanB poświęconego danym](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) w sekcji `resources/conference/`:

![conference](assets/02.webp)


- Kliknij w prawym górnym rogu przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![conference](assets/03.webp)


- Jeśli nigdy wcześniej nie współtworzyłeś zawartości PlanB Network, będziesz musiał utworzyć Fork oryginalnego repozytorium. Rozwidlenie repozytorium oznacza utworzenie kopii tego repozytorium na własnym koncie GitHub, co pozwala na pracę nad projektem bez wpływu na oryginalne repozytorium. Kliknij przycisk `Fork tego repozytorium`:

![conference](assets/04.webp)


- Następnie przejdziesz do strony edycji GitHub:

![conference](assets/05.webp)


- Utwórz folder dla swojej konferencji. Aby to zrobić, w polu `Nazwij plik...` wpisz nazwę konferencji małymi literami z myślnikami zamiast spacji. Na przykład, jeśli konferencja nazywa się "Paris Bitcoin Conference", należy wpisać `paris-Bitcoin-conference`. Dodaj również rok konferencji, na przykład: `paris-Bitcoin-conference-2024`:

![conference](assets/06.webp)


- Aby potwierdzić utworzenie folderu, wystarczy dodać ukośnik po swojej nazwie w tym samym polu, na przykład: `paris-Bitcoin-conference-2024/`. Dodanie ukośnika automatycznie tworzy folder, a nie plik:

![conference](assets/07.webp)


- W tym folderze utworzony zostanie pierwszy plik YAML o nazwie `conference.yml`:

![conference](assets/08.webp)

Wypełnij ten plik informacjami związanymi z konferencją, korzystając z tego szablonu:

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


Przykładowo, plik YAML może wyglądać następująco:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


Jeśli nie masz jeszcze identyfikatora "*builder*" dla swojej organizacji, możesz go dodać, postępując zgodnie z tym samouczkiem.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Po zakończeniu wprowadzania zmian w tym pliku, zapisz je, klikając przycisk `Commit changes...`:

![conference](assets/10.webp)


- Dodaj tytuł zmian oraz krótki opis:

![conference](assets/11.webp)


- Kliknij przycisk Green `Zaproponuj zmiany`:

![conference](assets/12.webp)


- Zostanie wyświetlona strona podsumowująca wszystkie wprowadzone zmiany:

![conference](assets/13.webp)


- Kliknij na swoje zdjęcie profilowe GitHub w prawym górnym rogu, a następnie na `Twoje repozytoria`:

![conference](assets/14.webp)


- Wybierz Fork z repozytorium PlanB Network:

![conference](assets/15.webp)


- Powinieneś zobaczyć powiadomienie w górnej części okna z nową gałęzią. Prawdopodobnie nazywa się ona `patch-1`. Kliknij na nią:

![conference](assets/16.webp)


- Jesteś teraz w swojej gałęzi roboczej:

![conference](assets/17.webp)


- Wróć do folderu `resources/conference/` i wybierz folder konferencji, który właśnie utworzyłeś w poprzednim zatwierdzeniu:

![conference](assets/18.webp)


- W folderze konferencji kliknij przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![conference](assets/19.webp)


- Nazwij ten nowy folder `assets` i potwierdź jego utworzenie, umieszczając na końcu ukośnik `/`:

![conference](assets/20.webp)


- W folderze `assets` utwórz plik o nazwie `.gitkeep`:

![conference](assets/21.webp)


- Kliknij przycisk `Commit changes...`:

![conference](assets/22.webp)


- Pozostaw tytuł zatwierdzenia jako domyślny i upewnij się, że pole `Commit directly to the patch-1 branch` jest zaznaczone, a następnie kliknij `Commit changes`:

![conference](assets/23.webp)


- Powrót do folderu `assets`:

![conference](assets/24.webp)


- Kliknij przycisk "Dodaj plik", a następnie "Prześlij pliki":

![conference](assets/25.webp)


- Otworzy się nowa strona. Przeciągnij i upuść obraz, który reprezentuje Twoją konferencję i będzie wyświetlany na stronie PlanB Network: ![conference](assets/26.webp)
- Może to być logo, miniatura, a nawet plakat:

![conference](assets/27.webp)


- Po przesłaniu obrazu sprawdź, czy zaznaczone jest pole `Commit directly to the patch-1 branch`, a następnie kliknij `Commit changes`:

![conference](assets/28.webp)


- Uważaj, twój obraz musi mieć nazwę `thumbnail` i musi być w formacie `.webp`. Pełna nazwa pliku powinna zatem brzmieć: `thumbnail.webp`:

![conference](assets/29.webp)


- Wróć do folderu `assets` i kliknij na plik pośredni `.gitkeep`:

![conference](assets/30.webp)


- Gdy znajdziesz się na pliku, kliknij na 3 małe kropki w prawym górnym rogu, a następnie na `Usuń plik`:

![conference](assets/31.webp)


- Sprawdź, czy nadal jesteś w tej samej gałęzi roboczej, a następnie kliknij przycisk `Commit changes`:

![conference](assets/32.webp)


- Dodaj tytuł i opis do zatwierdzenia, a następnie kliknij `Commit changes`:

![conference](assets/33.webp)


- Wróć do folderu konferencji:

![conference](assets/34.webp)


- Kliknij przycisk `Dodaj plik`, a następnie `Utwórz nowy plik`:

![conference](assets/35.webp)


- Utwórz nowy plik markdown (.md), nadając mu nazwę ze wskaźnikiem języka ojczystego. Plik ten będzie używany do powtórek konferencji. Na przykład, jeśli chcę napisać opisy konferencji w języku angielskim, nazwę ten plik en.md:

![conference](assets/36.webp)


- Wypełnij ten plik markdown przy użyciu tego szablonu, który możesz dostosować do konfiguracji swojej konferencji:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- Na początku dokumentu, we "front matter", wypełnij pole `name:` z nazwą konferencji i rokiem powtórek. W polu `description:` wpisz krótki opis wydarzenia w języku pliku. Na przykład, dla pliku o nazwie `en.md`, opis powinien być w języku angielskim. Zespół PlanB Network zajmie się tłumaczeniem opisu przy użyciu swojego modelu.
- Tytuły pierwszego poziomu, oznaczone `#`, są używane do organizowania konferencji według scen. Na przykład `# Main Stage` dla sceny głównej i `# Workshop Room` dla sceny poświęconej warsztatom.



- Tytuły drugiego poziomu, oznaczone podwójnym `##`, są używane do oddzielania różnych powtórek wideo. Jeśli konferencje były filmowane nieprzerwanie przez pół dnia, należy wskazać na przykład `## piątek rano`. Jeśli konferencje były filmowane i transmitowane indywidualnie, należy nazwać konferencję bezpośrednio tytułem drugiego poziomu.



- Pod każdym tytułem drugiego poziomu wstaw link do odpowiedniej powtórki wideo. Składnia powinna być następująca: `![wideo](https://youtu.be/XXXXXXXXXXXX)`, zastępując `XXXXXXXXXXXX` rzeczywistym linkiem wideo.



- Jeśli pozwala na to format (indywidualne konferencje), można dodać nazwiska prelegentów. Aby to zrobić, dodaj pole `Speaker:`, a następnie imię i nazwisko lub pseudonim prelegenta pod linkiem wideo. W przypadku wielu prelegentów, oddziel każde nazwisko przecinkiem, na przykład: `Prelegent: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- Po zakończeniu modyfikacji tego pliku zapisz je, klikając przycisk `Commit changes...`:

![conference](assets/38.webp)


- Dodaj tytuł modyfikacji oraz krótki opis:

![conference](assets/39.webp)


- Kliknij `Commit changes` (Zatwierdź zmiany):

![conference](assets/40.webp)


- Folder konferencji powinien teraz wyglądać następująco:

![conference](assets/41.webp)


- Jeśli wszystko jest w porządku, wróć do źródła Fork:

![conference](assets/42.webp)


- Powinieneś zobaczyć komunikat wskazujący, że twoja gałąź została poddana modyfikacjom. Kliknij przycisk `Porównaj i pobierz żądanie`:

![conference](assets/43.webp)


- Dodaj jasny tytuł i opis dla swojego PR:

![conference](assets/44.webp)


- Kliknij przycisk `Utwórz żądanie ściągnięcia`:

![conference](assets/45.webp)

Gratulacje! Twój PR został pomyślnie utworzony. Administrator przejrzy go teraz i, jeśli wszystko jest w porządku, połączy go z głównym repozytorium PlanB Network. Powtórki Twojej konferencji powinny pojawić się na stronie kilka dni później.


Pamiętaj, aby śledzić postępy swojego PR. Możliwe, że administrator pozostawi komentarz z prośbą o dodatkowe informacje. Dopóki twój PR nie zostanie zatwierdzony, możesz go wyświetlić w zakładce `Pull requests` w repozytorium PlanB Network na GitHubie:

![conference](assets/46.webp)


Dziękuję bardzo za cenny wkład! :)