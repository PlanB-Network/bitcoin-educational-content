---
name: Dodawanie podcastu do PlanB Network
description: Jak dodać nowy podcast do PlanB Network?
---
![podcast](assets/cover.webp)


Misją PlanB jest dostarczanie najwyższej jakości zasobów edukacyjnych na temat Bitcoin w jak największej liczbie języków. Wszystkie treści publikowane na stronie są open-source i hostowane na GitHub, dzięki czemu każdy może uczestniczyć we wzbogacaniu platformy.


Chcesz dodać podcast Bitcoin do witryny PlanB Network i zwiększyć widoczność swojego programu, ale nie wiesz jak to zrobić? Ten poradnik jest dla Ciebie!

![podcast](assets/01.webp)


- Po pierwsze, musisz mieć konto GitHub. Jeśli nie wiesz, jak je utworzyć, przygotowaliśmy szczegółowy samouczek, który Cię poprowadzi.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Przejdź do [repozytorium GitHub PlanB poświęconego danym](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts) w sekcji `resources/podcasts/`:

![podcast](assets/02.webp)


- Kliknij w prawym górnym rogu przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![podcast](assets/03.webp)


- Jeśli nigdy wcześniej nie współtworzyłeś zawartości PlanB Network, będziesz musiał utworzyć Fork oryginalnego repozytorium. Rozwidlenie repozytorium oznacza utworzenie kopii tego repozytorium na własnym koncie GitHub, umożliwiając pracę nad projektem bez wpływu na oryginalne repozytorium. Kliknij przycisk `Fork tego repozytorium`:

![podcast](assets/04.webp)


- Następnie przejdziesz do strony edycji GitHub:

![podcast](assets/05.webp)


- Utwórz folder dla swojego podcastu. Aby to zrobić, w polu `Nazwij plik...` wpisz nazwę swojego podcastu małymi literami z myślnikami zamiast spacji. Na przykład, jeśli twój program nazywa się "Super Podcast Bitcoin", powinieneś napisać `super-podcast-Bitcoin`:

![podcast](assets/06.webp)


- Aby zatwierdzić utworzenie folderu, wystarczy dodać ukośnik po nazwie podcastu w tym samym polu, na przykład: `super-podcast-Bitcoin/`. Dodanie ukośnika automatycznie tworzy folder, a nie plik:

![podcast](assets/07.webp)


- W tym folderze utworzysz pierwszy plik YAML o nazwie `podcast.yml`:

![podcast](assets/08.webp)


- Wypełnij ten plik informacjami o swoim podcaście, korzystając z tego szablonu:


```yaml
name:
host:
language:
links:
podcast:
twitter:
website:
description: |

tags:
-
-
contributors:
-
```


Poniżej znajdują się szczegóły do wypełnienia dla każdego pola:



- `name`**: Podaj nazwę swojego podcastu.
- `host`**: Lista nazwisk lub pseudonimów prelegentów lub gospodarza podcastu. Każda nazwa powinna być oddzielona przecinkiem.
- `language`**: Wskaż kod języka używanego w podcaście. Na przykład dla języka angielskiego `en`, dla włoskiego `it`...



- `links`**: Podaj linki do swoich treści. Dostępne są dwie opcje:
 - `podcast`: link do podcastu,
 - `twitter`: link do profilu Twitter podcastu lub organizacji go produkującej,
 - `website`: link do strony internetowej podcastu lub organizacji, która go wyprodukowała.



- `description`**: Dodaj krótki akapit opisujący Twój podcast. Opis musi być w tym samym języku, co wskazany w polu `language:`.



- `tags`**: Dodaj dwa tagi powiązane z podcastem. Przykłady:
    - `Bitcoin`
    - `technologia`
    - `gospodarka`
    - `edukacja`...



- `contributors`**: Podaj swój identyfikator współtwórcy, jeśli go posiadasz.


Przykładowo, plik YAML może wyglądać następująco:


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- Po zakończeniu wprowadzania zmian w tym pliku, zapisz je, klikając przycisk `Commit changes...`:

![podcast](assets/10.webp)


- Dodaj tytuł zmian oraz krótki opis:

![podcast](assets/11.webp)


- Kliknij przycisk Green `Zaproponuj zmiany`:

![podcast](assets/12.webp)


- Następnie pojawi się strona podsumowująca wszystkie wprowadzone zmiany:

![podcast](assets/13.webp)


- Kliknij na swoje zdjęcie profilowe GitHub w prawym górnym rogu, a następnie na `Twoje repozytoria`:

![podcast](assets/14.webp)


- Wybierz Fork z repozytorium PlanB Network:

![podcast](assets/15.webp)


- W górnej części okna powinno pojawić się powiadomienie z nową gałęzią. Prawdopodobnie nazywa się `patch-1`. Kliknij na nią:

![podcast](assets/16.webp)


- Jesteś teraz w swojej gałęzi roboczej:

![podcast](assets/17.webp)


- Wróć do folderu `resources/podcast/` i wybierz folder podcast, który właśnie utworzyłeś w poprzednim zatwierdzeniu: ![podcast](assets/18.webp)
- W folderze podcastów kliknij przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![podcast](assets/19.webp)


- Nazwij ten nowy folder `assets` i potwierdź jego utworzenie, dodając ukośnik `/` na końcu:

![podcast](assets/20.webp)


- W folderze `assets` utwórz plik o nazwie `.gitkeep`:

![podcast](assets/21.webp)


- Kliknij przycisk `Commit changes...`:

![podcast](assets/22.webp)


- Pozostaw tytuł zatwierdzenia jako domyślny i upewnij się, że pole `Commit directly to the patch-1 branch` jest zaznaczone, a następnie kliknij `Commit changes`:

![podcast](assets/23.webp)


- Powrót do folderu `assets`:

![podcast](assets/24.webp)


- Kliknij przycisk "Dodaj plik", a następnie "Prześlij pliki":

![podcast](assets/25.webp)


- Otworzy się nowa strona. Przeciągnij i upuść logo podcastu w tym obszarze. Obraz ten będzie wyświetlany na stronie PlanB Network:

![podcast](assets/26.webp)


- Obraz musi być kwadratowy, aby jak najlepiej pasował do naszej strony internetowej:

![podcast](assets/27.webp)


- Po przesłaniu obrazu sprawdź, czy zaznaczone jest pole `Commit directly to the patch-1 branch`, a następnie kliknij `Commit changes`:

![podcast](assets/28.webp)


- Uważaj, twój obraz musi mieć nazwę `logo` i musi być w formacie `.webp`. Pełna nazwa pliku powinna zatem brzmieć: `logo.webp`:

![podcast](assets/29.webp)


- Wróć do folderu `assets` i kliknij na plik pośredni `.gitkeep`:

![podcast](assets/30.webp)


- Gdy znajdziesz się na pliku, kliknij trzy małe kropki w prawym górnym rogu, a następnie `Usuń plik`:

![podcast](assets/31.webp)


- Sprawdź, czy nadal jesteś w tej samej gałęzi roboczej, a następnie kliknij przycisk `Commit changes`:

![podcast](assets/32.webp)


- Dodaj tytuł i opis do zatwierdzenia, a następnie kliknij `Commit changes`:

![podcast](assets/33.webp)


- Wróć do katalogu głównego repozytorium:

![podcast](assets/34.webp)


- Powinieneś zobaczyć komunikat informujący, że w Twojej gałęzi wprowadzono zmiany. Kliknij przycisk `Porównaj i pobierz żądanie`:

![podcast](assets/35.webp)


- Dodaj jasny tytuł i opis do swojego PR:

![podcast](assets/36.webp)


- Kliknij przycisk `Utwórz żądanie ściągnięcia`:

![podcast](assets/37.webp)

Gratulacje! Twój PR został pomyślnie utworzony. Administrator przejrzy go teraz i, jeśli wszystko jest w porządku, połączy go z głównym repozytorium PlanB Network. Podcast powinien pojawić się na stronie kilka dni później.


Prosimy o śledzenie postępów PR. Administrator może zostawić komentarz z prośbą o dodatkowe informacje. Dopóki twój PR nie zostanie zatwierdzony, możesz go wyświetlić w zakładce `Pull requests` w repozytorium PlanB Network GitHub:

![podcast](assets/38.webp)

Dziękuję bardzo za cenny wkład! :)