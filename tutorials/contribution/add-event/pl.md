---
name: Dodaj wydarzenie w PlanB Network
description: Jak mogę zasugerować dodanie nowego wydarzenia w PlanB Network?
---
![event](assets/cover.webp)


Misją PlanB jest dostarczanie najwyższej jakości zasobów edukacyjnych na temat Bitcoin w jak największej liczbie języków. Wszystkie treści publikowane na stronie są open-source i hostowane na GitHub, oferując każdemu możliwość przyczynienia się do wzbogacenia platformy.


Jeśli chcesz dodać konferencję Bitcoin do witryny PlanB Network i zwiększyć widoczność swojego wydarzenia, ale nie wiesz jak? Ten poradnik jest dla Ciebie!

![event](assets/01.webp)


- Po pierwsze, musisz mieć konto na GitHub. Jeśli nie wiesz, jak utworzyć konto, przygotowaliśmy szczegółowy samouczek, który Cię poprowadzi.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Przejdź do [repozytorium GitHub PlanB poświęconego danym](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) w sekcji `resources/conference/`:

![event](assets/02.webp)


- Kliknij w prawym górnym rogu przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![event](assets/03.webp)


- Jeśli nigdy wcześniej nie współtworzyłeś zawartości PlanB Network, będziesz musiał utworzyć Fork oryginalnego repozytorium. Rozwidlenie repozytorium oznacza utworzenie kopii tego repozytorium na własnym koncie GitHub, umożliwiając pracę nad projektem bez wpływu na oryginalne repozytorium. Kliknij przycisk `Fork tego repozytorium`:

![event](assets/04.webp)


- Następnie przejdziesz do strony edycji GitHub:

![event](assets/05.webp)


- Utwórz folder dla swojej konferencji. Aby to zrobić, w polu `Nazwij plik...` wpisz nazwę konferencji małymi literami z myślnikami zamiast spacji. Na przykład, jeśli konferencja nazywa się "Paris Bitcoin Conference", należy wpisać `paris-Bitcoin-conference`. Dodaj również rok konferencji, na przykład: `paris-Bitcoin-conference-2024`:

![event](assets/06.webp)


- Aby potwierdzić utworzenie folderu, wystarczy dodać ukośnik po swojej nazwie w tym samym polu, na przykład: `paris-Bitcoin-conference-2024/`. Dodanie ukośnika automatycznie tworzy folder, a nie plik:

![event](assets/07.webp)


- W tym folderze utworzony zostanie pierwszy plik YAML o nazwie `events.yml`:

![event](assets/08.webp)


- Wypełnij ten plik informacjami o swojej konferencji, korzystając z tego szablonu:


```yaml
start_date:
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


Przykładowo, plik YAML może wyglądać następująco:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

Jeśli nie masz jeszcze identyfikatora "*builder*" dla swojej organizacji, możesz go dodać, postępując zgodnie z tym samouczkiem.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Po zakończeniu wprowadzania zmian w tym pliku, zapisz je, klikając przycisk `Commit changes...`:

![event](assets/10.webp)


- Dodaj tytuł zmian oraz krótki opis:

![event](assets/11.webp)


- Kliknij przycisk Green `Zaproponuj zmiany`:

![event](assets/12.webp)


- Zostanie wyświetlona strona podsumowująca wszystkie wprowadzone zmiany:

![event](assets/13.webp)


- Kliknij na swoje zdjęcie profilowe GitHub w prawym górnym rogu, a następnie na `Twoje repozytoria`:

![event](assets/14.webp)


- Wybierz Fork z repozytorium PlanB Network:

![event](assets/15.webp)


- W górnej części okna powinno pojawić się powiadomienie z nową gałęzią. Prawdopodobnie nazywa się `patch-1`. Kliknij na nią:

![event](assets/16.webp)


- Jesteś teraz w swojej gałęzi roboczej:

![event](assets/17.webp)


- Wróć do folderu `resources/conference/` i wybierz folder konferencji, który właśnie utworzyłeś w poprzednim zatwierdzeniu:

![event](assets/18.webp)


- W folderze konferencji kliknij przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![event](assets/19.webp)


- Nazwij ten nowy folder `assets` i potwierdź jego utworzenie, umieszczając na końcu ukośnik `/`:

![event](assets/20.webp)


- W folderze `assets` utwórz plik o nazwie `.gitkeep`:

![event](assets/21.webp)


- Kliknij przycisk `Commit changes...`:

![event](assets/22.webp)


- Pozostaw tytuł zatwierdzenia jako domyślny i upewnij się, że pole `Commit directly to the patch-1 branch` jest zaznaczone, a następnie kliknij `Commit changes`:

![event](assets/23.webp)


- Powrót do folderu `assets`:

![event](assets/24.webp)


- Kliknij przycisk `Dodaj plik`, a następnie `Prześlij pliki`: ![event](assets/25.webp)
- Otworzy się nowa strona. Przeciągnij i upuść obraz, który reprezentuje Twoją konferencję i będzie wyświetlany na stronie PlanB Network:

![event](assets/26.webp)


- Może to być logo, miniatura, a nawet plakat:

![event](assets/27.webp)


- Po przesłaniu obrazu sprawdź, czy pole `Commit directly to the patch-1 branch` jest zaznaczone, a następnie kliknij `Commit changes`:

![event](assets/28.webp)


- Uważaj, twój obraz musi mieć nazwę `thumbnail` i musi być w formacie `.webp`. Pełna nazwa pliku powinna zatem brzmieć: `thumbnail.webp`:

![event](assets/29.webp)


- Wróć do folderu `assets` i kliknij na plik pośredni `.gitkeep`:

![event](assets/30.webp)


- Po znalezieniu pliku kliknij 3 małe kropki w prawym górnym rogu, a następnie `Usuń plik`:

![event](assets/31.webp)


- Sprawdź, czy nadal jesteś w tej samej gałęzi roboczej, a następnie kliknij przycisk `Commit changes`:

![event](assets/32.webp)


- Dodaj tytuł i opis do zatwierdzenia, a następnie kliknij `Commit changes`:

![event](assets/33.webp)


- Wróć do katalogu głównego repozytorium:

![event](assets/34.webp)


- Powinieneś zobaczyć komunikat informujący, że w Twojej gałęzi wprowadzono zmiany. Kliknij przycisk `Porównaj i pobierz żądanie`:

![event](assets/35.webp)


- Dodaj jasny tytuł i opis do swojego PR:

![event](assets/36.webp)


- Kliknij przycisk `Utwórz żądanie ściągnięcia`:

![event](assets/37.webp)

Gratulacje! Twój PR został pomyślnie utworzony. Administrator sprawdzi go teraz i, jeśli wszystko jest w porządku, połączy go z głównym repozytorium PlanB Network. Wydarzenie powinno pojawić się na stronie kilka dni później.


Pamiętaj, aby śledzić postępy swojego PR. Administrator może zostawić komentarz z prośbą o dodatkowe informacje. Dopóki twój PR nie zostanie zatwierdzony, możesz zapoznać się z nim w zakładce `Pull requests` w repozytorium PlanB Network GitHub:

![event](assets/38.webp)

Dziękuję bardzo za cenny wkład! :)