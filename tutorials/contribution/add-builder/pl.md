---
name: Dodawanie konstruktora
description: Jak zaproponować dodanie nowego konstruktora do PlanB Network?
---
![builder](assets/cover.webp)


Misją PlanB jest dostarczanie najwyższej jakości zasobów edukacyjnych na Bitcoin, w jak największej liczbie języków. Wszystkie treści publikowane na stronie są open-source i hostowane na GitHub, co pozwala każdemu uczestniczyć we wzbogacaniu platformy.


Czy chcesz dodać nowego "budowniczego" Bitcoin do witryny PlanB Network i zapewnić widoczność swojej firmie lub oprogramowaniu, ale nie wiesz jak? Ten poradnik jest dla Ciebie!

![builder](assets/01.webp)


- Po pierwsze, musisz mieć konto GitHub. Jeśli nie wiesz, jak utworzyć konto, przygotowaliśmy szczegółowy samouczek, który Cię poprowadzi.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Przejdź do [repozytorium GitHub PlanB poświęconego danym](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/builders) w sekcji `resources/builder/`:

![builder](assets/02.webp)


- Kliknij w prawym górnym rogu przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![builder](assets/03.webp)


- Jeśli nigdy wcześniej nie współtworzyłeś zawartości PlanB Network, będziesz musiał utworzyć Fork oryginalnego repozytorium. Rozwidlenie repozytorium oznacza utworzenie kopii tego repozytorium na własnym koncie GitHub, co pozwala na pracę nad projektem bez wpływu na oryginalne repozytorium. Kliknij przycisk `Fork tego repozytorium`:

![builder](assets/04.webp)


- Następnie przejdziesz do strony edycji GitHub:

![builder](assets/05.webp)


- Utwórz folder dla swojej firmy. Aby to zrobić, w polu `Nazwij plik...` wpisz nazwę swojej firmy małymi literami z myślnikami zamiast spacji. Na przykład, jeśli firma nazywa się "Bitcoin Baguette", należy wpisać `Bitcoin-baguette`:

![builder](assets/06.webp)


- Aby zatwierdzić utworzenie folderu, wystarczy dodać ukośnik po nazwie w tym samym polu, na przykład: `Bitcoin-baguette/`. Dodanie ukośnika automatycznie tworzy folder, a nie plik:

![builder](assets/07.webp)


- W tym folderze zostanie utworzony pierwszy plik YAML o nazwie `builder.yml`:

![builder](assets/08.webp)


- Wypełnij ten plik informacjami o swojej firmie, korzystając z tego szablonu:


```yaml
name:

address_line_1:
address_line_2:
address_line_3:

language:
-

links:
website:
twitter:
Github:
youtube:
nostr:

tags:
-
-

category:
```


Oto, co należy wypełnić dla każdego klucza:


- `name`: Nazwa firmy (obowiązkowa);
- `Address`: Lokalizacja firmy (opcjonalnie);
- `language`: Kraje, w których działa Twoja firma lub obsługiwane języki (opcjonalnie);
- `links` : Różne oficjalne linki Twojej firmy (opcjonalnie);
- `tags`: 2 terminy, które kwalifikują Twoją firmę (obowiązkowe);
- `category` : Kategoria, która najlepiej opisuje dziedzinę, w której działa Twoja firma spośród następujących opcji:
 - `Wallet`,
 - `infrastruktura`,
 - `Exchange`,
 - `edukacja`,
 - `service`,
 - `communities`,
 - `konferencja`,
 - `privacy`,
 - `inwestycja`,
 - `node`,
 - `Mining`,
 - `news`,
 - `producent`.


Przykładowo, plik YAML może wyglądać następująco:


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![builder](assets/09.webp)


- Po zakończeniu wprowadzania zmian w tym pliku, zapisz je, klikając przycisk `Commit changes...`:

![builder](assets/10.webp)


- Dodaj tytuł zmian wraz z krótkim opisem:

![builder](assets/11.webp)


- Kliknij przycisk Green `Zaproponuj zmiany`:

![builder](assets/12.webp)


- Zostanie wyświetlona strona podsumowująca wszystkie wprowadzone zmiany:

![builder](assets/13.webp)


- Kliknij na swoje zdjęcie profilowe GitHub w prawym górnym rogu, a następnie na `Twoje repozytoria`:

![builder](assets/14.webp)


- Wybierz Fork z repozytorium PlanB Network:

![builder](assets/15.webp)


- W górnej części okna powinno pojawić się powiadomienie z nową gałęzią. Prawdopodobnie nazywa się `patch-1`. Kliknij na nią:

![builder](assets/16.webp)


- Jesteś teraz w gałęzi roboczej (**upewnij się, że jesteś w tej samej gałęzi, co poprzednie modyfikacje, to ważne!**):

![builder](assets/17.webp)


- Wróć do folderu `resources/builders/` i wybierz folder swojej firmy, który właśnie utworzyłeś w poprzednim zatwierdzeniu:

![builder](assets/18.webp)


- W folderze swojej firmy kliknij przycisk "Dodaj plik", a następnie "Utwórz nowy plik":

![builder](assets/19.webp)


- Nazwij ten nowy folder `assets` i potwierdź jego utworzenie, umieszczając na końcu ukośnik `/`:

![builder](assets/20.webp)


- W folderze `assets` utwórz plik o nazwie `.gitkeep`:

![builder](assets/21.webp)


- Kliknij przycisk `Commit changes...`:

![builder](assets/22.webp)


- Pozostaw tytuł zatwierdzenia jako domyślny i upewnij się, że pole `Commit directly to the patch-1 branch` jest zaznaczone, a następnie kliknij `Commit changes`: ![builder](assets/23.webp)
- Wróć do folderu `assets`:

![builder](assets/24.webp)


- Kliknij przycisk "Dodaj plik", a następnie "Prześlij pliki":

![builder](assets/25.webp)


- Otworzy się nowa strona. Przeciągnij i upuść obraz swojej firmy lub oprogramowania w tym obszarze. Obraz ten będzie wyświetlany na stronie PlanB Network:

![builder](assets/26.webp)


- Może to być logo lub ikona:

![builder](assets/27.webp)


- Po przesłaniu obrazu sprawdź, czy zaznaczone jest pole `Commit directly to the patch-1 branch`, a następnie kliknij `Commit changes`:

![builder](assets/28.webp)


- Uważaj, twój obraz musi być kwadratowy, musi mieć nazwę `logo` i musi być w formacie `.webp`. Pełna nazwa pliku powinna zatem brzmieć: `logo.webp`:

![builder](assets/29.webp)


- Wróć do folderu `assets` i kliknij na plik pośredni `.gitkeep`:

![builder](assets/30.webp)


- Gdy znajdziesz się na pliku, kliknij trzy małe kropki w prawym górnym rogu, a następnie `Usuń plik`:

![builder](assets/31.webp)


- Sprawdź, czy nadal jesteś w tej samej gałęzi roboczej, a następnie kliknij przycisk `Commit changes`:

![builder](assets/32.webp)


- Dodaj tytuł i opis do zatwierdzenia, a następnie kliknij `Commit changes`:

![builder](assets/33.webp)


- Wróć do folderu swojej firmy:

![builder](assets/34.webp)


- Kliknij przycisk `Dodaj plik`, a następnie `Utwórz nowy plik`:

![builder](assets/35.webp)


- Utwórz nowy plik YAML, nadając mu nazwę ze wskaźnikiem języka ojczystego. Plik ten będzie używany do opisu konstruktora. Na przykład, jeśli chcę napisać opis w języku angielskim, nazwę ten plik `en.yml`:

![builder](assets/36.webp)


- Wypełnij ten plik YAML przy użyciu tego szablonu:

```yaml
description: |

contributors:
-
```



- Dla klucza `contributors` możesz dodać swój identyfikator kontrybutora do PlanB Network, jeśli go posiadasz. Jeśli nie, pozostaw to pole puste.
- W przypadku klucza `description` wystarczy dodać krótki akapit opisujący firmę lub oprogramowanie. Opis musi być w tym samym języku, co nazwa pliku. Nie musisz tłumaczyć tego opisu na wszystkie języki obsługiwane na stronie, ponieważ zespoły PlanB zrobią to za pomocą swojego modelu. Na przykład, oto jak może wyglądać plik:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![builder](assets/37.webp)


- Kliknij przycisk "Zatwierdź zmiany":

![builder](assets/38.webp)


- Upewnij się, że pole `Commit directly to the patch-1 branch` jest zaznaczone, dodaj tytuł, a następnie kliknij `Commit changes`:

![builder](assets/39.webp)


- Folder firmowy powinien teraz wyglądać następująco:

![builder](assets/40.webp)


- Jeśli wszystko jest w porządku, wróć do źródła Fork:

![builder](assets/41.webp)


- Powinieneś zobaczyć komunikat informujący, że w Twojej gałęzi wprowadzono zmiany. Kliknij przycisk `Porównaj i pobierz żądanie`:

![builder](assets/42.webp)


- Dodaj jasny tytuł i opis do swojego PR:

![builder](assets/43.webp)


- Kliknij przycisk `Utwórz żądanie ściągnięcia`:

![builder](assets/44.webp)

Gratulacje! Twój PR został pomyślnie utworzony. Administrator sprawdzi go teraz i, jeśli wszystko jest w porządku, zintegruje go z głównym repozytorium PlanB Network. Twój profil powinien pojawić się na stronie kilka dni później.


Pamiętaj, aby śledzić postępy swojego PR. Administrator może zostawić komentarz z prośbą o dodatkowe informacje. Dopóki twój PR nie zostanie zatwierdzony, możesz zapoznać się z nim w zakładce `Pull requests` w repozytorium PlanB Network GitHub:

![builder](assets/45.webp)

Dziękuję bardzo za cenny wkład! :)