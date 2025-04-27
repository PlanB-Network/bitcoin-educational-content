---
name: Dodawanie książki do sieci PlanB
description: Jak dodać nową książkę do PlanB Network?
---
![book](assets/cover.webp)


Misją PlanB jest dostarczanie najwyższej jakości zasobów edukacyjnych na temat Bitcoin w jak największej liczbie języków. Wszystkie treści publikowane na stronie są open-source i hostowane na GitHub, dzięki czemu każdy może przyczynić się do wzbogacenia platformy.


**Czy chcesz dodać książkę związaną z Bitcoin na stronie PlanB Network i zwiększyć widoczność swojej pracy, ale nie wiesz jak? Ten poradnik jest dla Ciebie!**

![book](assets/01.webp)


- Po pierwsze, musisz mieć konto GitHub. Jeśli nie wiesz, jak utworzyć konto, przygotowaliśmy szczegółowy samouczek, który Cię poprowadzi.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Przejdź do [repozytorium GitHub PlanB poświęconego danym](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books) w sekcji `resources/books/`:

![book](assets/02.webp)


- Kliknij w prawym górnym rogu przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![book](assets/03.webp)


- Jeśli nigdy wcześniej nie współtworzyłeś zawartości PlanB Network, będziesz musiał utworzyć Fork oryginalnego repozytorium. Rozwidlenie repozytorium oznacza utworzenie kopii tego repozytorium na własnym koncie GitHub, umożliwiając pracę nad projektem bez wpływu na oryginalne repozytorium. Kliknij przycisk `Fork tego repozytorium`:

![book](assets/04.webp)


- Następnie przejdziesz do strony edycji GitHub:

![book](assets/05.webp)


- Utwórz folder dla swojej książki. Aby to zrobić, w polu `Nazwij plik...` wpisz nazwę swojej książki małymi literami z myślnikami zamiast spacji. Na przykład, jeśli książka nazywa się "*My Bitcoin Book*", należy wpisać `my-Bitcoin-book`:

![book](assets/06.webp)


- Aby zatwierdzić utworzenie folderu, wystarczy dodać ukośnik po nazwie książki w tym samym polu, na przykład: `my-Bitcoin-book/`. Dodanie ukośnika automatycznie tworzy folder, a nie plik:

![book](assets/07.webp)


- W tym folderze utworzony zostanie pierwszy plik YAML o nazwie `book.yml`:

![book](assets/08.webp)


- Wypełnij ten plik informacjami o swojej książce, korzystając z tego szablonu:


```yaml
author:
level:
tags:
-
-
```


Poniżej znajdują się szczegóły do wypełnienia dla każdego pola:


- `author`**: Wskazuje nazwisko autora książki.
- `level`**: Wskaż wymagany poziom, aby móc dobrze przeczytać i zrozumieć książkę. Wybierz poziom spośród następujących:
 - początkujący
 - `średniozaawansowany`
- `zaawansowany` - `ekspert`
- `tags`**: Dodaj dwa lub trzy tagi związane z Twoją książką. Na przykład:
    - `Bitcoin`
    - `historia`
    - `technologia`
    - `gospodarka`
    - `edukacja`...


Przykładowo, plik YAML może wyglądać następująco:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- Po zakończeniu wprowadzania zmian w tym pliku, zapisz je, klikając przycisk `Commit changes...`:

![book](assets/10.webp)


- Dodaj tytuł zmian oraz krótki opis:

![book](assets/11.webp)


- Kliknij przycisk Green `Zaproponuj zmiany`:

![book](assets/12.webp)


- Zostanie wyświetlona strona podsumowująca wszystkie wprowadzone zmiany:

![book](assets/13.webp)


- Kliknij na swoje zdjęcie profilowe GitHub w prawym górnym rogu, a następnie na `Twoje repozytoria`:

![book](assets/14.webp)


- Wybierz Fork z repozytorium PlanB Network:

![book](assets/15.webp)


- W górnej części okna powinno pojawić się powiadomienie z nową gałęzią. Prawdopodobnie nazywa się `patch-1`. Kliknij na nią:

![book](assets/16.webp)


- Jesteś teraz w swojej gałęzi roboczej:

![book](assets/17.webp)


- Wróć do folderu `resources/books/` i wybierz folder książki, który właśnie utworzyłeś w poprzednim zatwierdzeniu:

![book](assets/18.webp)


- W folderze książki kliknij przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![book](assets/19.webp)


- Nazwij ten nowy folder `assets` i potwierdź jego utworzenie, umieszczając na końcu ukośnik `/`:

![book](assets/20.webp)


- W folderze `assets` utwórz plik o nazwie `.gitkeep`:

![book](assets/21.webp)


- Kliknij przycisk `Commit changes...`:

![book](assets/22.webp)


- Pozostaw tytuł zatwierdzenia jako domyślny i upewnij się, że pole `Commit directly to the patch-1 branch` jest zaznaczone, a następnie kliknij `Commit changes`:

![book](assets/23.webp)


- Powrót do folderu `assets`:

![book](assets/24.webp)


- Kliknij przycisk "Dodaj plik", a następnie "Prześlij pliki":

![book](assets/25.webp)


- Otworzy się nowa strona. Przeciągnij i upuść obraz okładki swojej książki w tym obszarze. Obraz ten zostanie wyświetlony na stronie PlanB Network:

![book](assets/26.webp)


- Uważaj, obraz musi być w formacie książki, aby jak najlepiej dostosować się do naszej strony internetowej, na przykład:

![book](assets/27.webp)


- Po przesłaniu obrazu upewnij się, że pole `Commit directly to the patch-1 branch` jest zaznaczone, a następnie kliknij `Commit changes`:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- Wróć do folderu `assets` i kliknij na plik pośredni `.gitkeep`:

![book](assets/30.webp)


- Po znalezieniu pliku kliknij 3 małe kropki w prawym górnym rogu, a następnie `Usuń plik`:

![book](assets/31.webp)


- Upewnij się, że nadal jesteś w tej samej gałęzi roboczej, a następnie kliknij przycisk `Commit changes...`:

![book](assets/32.webp)


- Dodaj tytuł i opis do zatwierdzenia, a następnie kliknij `Commit changes`:

![book](assets/33.webp)


- Wróć do folderu książki:

![book](assets/34.webp)


- Kliknij przycisk `Dodaj plik`, a następnie `Utwórz nowy plik`:

![book](assets/35.webp)


- Utwórz nowy plik YAML, nadając mu nazwę ze wskaźnikiem języka książki. Plik ten będzie używany do opisu książki. Na przykład, jeśli chcę napisać opis w języku angielskim, nazwę ten plik `en.yml`:

![book](assets/36.webp)


- Wypełnij ten plik YAML przy użyciu tego szablonu:

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


Poniżej znajdują się szczegóły do wypełnienia dla każdego pola:


- `title`**: Wskaż nazwę książki w cudzysłowie.
- `publication_year`**: Wskazuje rok publikacji książki.
- `cover`**: Wskaż nazwę pliku odpowiadającego obrazowi okładki, zgodnie z językiem aktualnie edytowanego pliku YAML. Na przykład, jeśli edytujesz plik `en.yml` i wcześniej dodałeś angielski obraz okładki zatytułowany `cover_en.webp`, po prostu wskaż `cover_en.webp` w tym polu.
- `description`**: Dodaj krótki akapit opisujący książkę. Opis musi być w tym samym języku, co wskazany w tytule pliku YAML.
- `contributors`**: Dodaj swój identyfikator współtwórcy, jeśli go posiadasz.


Przykładowo, plik YAML może wyglądać następująco:


```yaml