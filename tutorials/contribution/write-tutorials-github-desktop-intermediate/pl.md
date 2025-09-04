---
name: Wkład - samouczek z GitHub Desktop (średniozaawansowany)
description: Kompletny przewodnik po proponowaniu samouczka na Plan ₿ Network przy użyciu GitHub Desktop
---
![cover](assets/cover.webp)


Przed przystąpieniem do tego samouczka dotyczącego dodawania nowego samouczka należy wykonać kilka wstępnych kroków. Jeśli jeszcze tego nie zrobiłeś, zapraszam najpierw do zapoznania się z tym samouczkiem wprowadzającym, a następnie do powrotu tutaj:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Już to zrobiłeś:


- Wybierz temat swojego samouczka;
- Kontakt z zespołem Plan ₿ Network za pośrednictwem [grupy Telegram](https://t.me/PlanBNetwork_ContentBuilder) lub paolo@planb.network;
- Wybierz swoje narzędzia.


W tym samouczku zobaczymy, jak dodać swój samouczek na Plan ₿ Network, konfigurując lokalne środowisko za pomocą GitHub Desktop. Jeśli jesteś już biegły w Git, ten bardzo szczegółowy poradnik może nie być dla ciebie konieczny. Zalecałbym raczej zapoznanie się z tym innym poradnikiem, w którym przedstawiam tylko główne wytyczne, bez szczegółowych wskazówek krok po kroku:



- Doświadczeni użytkownicy**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Jeśli wolisz nie konfigurować lokalnego środowiska, postępuj zgodnie z tym innym samouczkiem przeznaczonym dla początkujących, w którym wprowadzamy zmiany bezpośrednio przez Interface w sieci GitHub:



- Początkujący (web Interface)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Wymagania wstępne


Oprogramowanie wymagane do wykonania tego samouczka:



- [GitHub Desktop](https://desktop.github.com/);
- Edytor plików markdown, taki jak [Obsidian](https://obsidian.md/);
- Edytor kodu ([VSC](https://code.visualstudio.com/) lub [Sublime Text](https://www.sublimetext.com/)).


![TUTO](assets/fr/01.webp)


Wymagania wstępne przed rozpoczęciem samouczka:



- Posiadać konto [GitHub] (https://github.com/signup);
- Posiadanie Fork z [repozytorium źródłowego Plan ₿ Network](https://github.com/PlanB-Network/Bitcoin-educational-content);
- Posiadać [profil profesora na Plan ₿ Network](https://planb.network/professors) (tylko jeśli proponujesz kompletny samouczek).


Jeśli potrzebujesz pomocy w uzyskaniu tych warunków wstępnych, moje inne samouczki pomogą ci:



Gdy wszystko jest już na swoim miejscu, a lokalne środowisko jest odpowiednio skonfigurowane z własnym Fork z Plan ₿ Network, możesz rozpocząć dodawanie samouczka.


## 1 - Utwórz nowy oddział


Otwórz przeglądarkę i przejdź do strony Fork repozytorium Plan ₿ Network. Jest to Fork, które utworzyłeś na GitHub. Adres URL Fork powinien wyglądać następująco: `https://github.com/[twoja-nazwa-użytkownika]/Bitcoin-educational-content`:


![TUTO](assets/fr/03.webp)


Upewnij się, że jesteś w głównej gałęzi `dev`, a następnie kliknij przycisk `Sync Fork`. Jeśli Fork nie jest aktualny, GitHub zaproponuje aktualizację gałęzi. Wykonaj tę aktualizację. Jeśli natomiast gałąź jest już aktualna, GitHub poinformuje Cię o tym:


![TUTO](assets/fr/04.webp)


Otwórz oprogramowanie GitHub Desktop i upewnij się, że Fork jest prawidłowo wybrany w lewym górnym rogu okna:


![TUTO](assets/fr/05.webp)


Kliknij przycisk "Pobierz źródło". Jeśli lokalne repozytorium jest już aktualne, GitHub Desktop nie zasugeruje żadnych dodatkowych działań. W przeciwnym razie pojawi się opcja `Pull origin`. Kliknij ten przycisk, aby zaktualizować lokalne repozytorium:


![TUTO](assets/fr/06.webp)


Sprawdź, czy rzeczywiście jesteś w głównej gałęzi `dev`:


![TUTO](assets/fr/07.webp)


Kliknij tę gałąź, a następnie kliknij przycisk "Nowa gałąź":


![TUTO](assets/fr/08.webp)


Upewnij się, że nowa gałąź jest oparta na repozytorium źródłowym, a mianowicie `PlanB-Network/Bitcoin-educational-content`.


Nazwij swoją gałąź w taki sposób, aby tytuł jasno określał jej cel, używając myślników do oddzielenia każdego słowa. Na przykład, powiedzmy, że naszym celem jest napisanie samouczka na temat korzystania z oprogramowania Sparrow Wallet. W takim przypadku gałąź robocza przeznaczona do napisania tego samouczka mogłaby nosić nazwę: `tuto-sparrow-Wallet-loic`. Po wprowadzeniu odpowiedniej nazwy, kliknij `Create branch`, aby potwierdzić utworzenie gałęzi:


![TUTO](assets/fr/09.webp)


Teraz kliknij przycisk "Opublikuj gałąź", aby zapisać nową gałąź roboczą w Fork online na GitHub:

![TUTORIAL](assets/fr/10.webp)

Teraz na pulpicie GitHub powinieneś znaleźć się w nowej gałęzi. Oznacza to, że wszystkie zmiany wprowadzone lokalnie na komputerze zostaną zapisane wyłącznie w tej gałęzi. Ponadto, dopóki ta gałąź pozostaje wybrana na Pulpicie GitHub, pliki widoczne lokalnie na komputerze odpowiadają plikom tej gałęzi (`tuto-sparrow-Wallet-loic`), a nie plikom głównej gałęzi (`dev`).


![TUTORIAL](assets/fr/11.webp)


Dla każdego nowego artykułu, który chcesz opublikować, musisz utworzyć nową gałąź z `dev`. Gałąź w Git jest równoległą wersją projektu, która pozwala na wprowadzanie zmian bez wpływu na główną gałąź, dopóki praca nie będzie gotowa do scalenia.


## 2 - Dodawanie plików samouczka


Po utworzeniu gałęzi roboczej nadszedł czas na integrację nowego samouczka. Masz dwie opcje: użyć mojego skryptu Python, który automatyzuje tworzenie niezbędnych dokumentów, lub ręcznie utworzyć każdy plik. Przyjrzymy się krokom, które należy wykonać dla każdej opcji.


### Z moim skryptem Pythona


Musisz zainstalować na swoim komputerze:


- Python 3.8 lub nowszy.


Aby użyć skryptu, należy przejść do folderu, w którym jest on przechowywany. Skrypt znajduje się w repozytorium danych Plan ₿ Network w ścieżce: `Bitcoin-educational-content/scripts/tutorial-related/data-creator`.


Po znalezieniu się w folderze zainstaluj zależności:


```
pip install -r requirements.txt
```


Następnie uruchom oprogramowanie za pomocą polecenia:


```
python3 main.py
```


Otworzy się graficzny interfejs użytkownika Interface (GUI). Za pierwszym razem konieczne będzie wprowadzenie wszystkich niezbędnych informacji, ale przy kolejnych użyciach skrypt zapamięta dane osobowe, więc nie trzeba będzie wprowadzać ich ponownie.


![DATA-CREATOR-PY](assets/fr/37.webp)


Zacznij od wprowadzenia lokalnej ścieżki do folderu `/tutorials` w sklonowanym repozytorium (`.../Bitcoin-educational-content/tutorials/`). Możesz wprowadzić ją ręcznie lub kliknąć przycisk "Przeglądaj", aby nawigować za pomocą eksploratora plików.


![DATA-CREATOR-PY](assets/fr/38.webp)


Wybierz język, w którym zostanie napisany samouczek.


![DATA-CREATOR-PY](assets/fr/39.webp)


W polu "Contributor's GitHub ID" wprowadź swoją nazwę użytkownika GitHub.


![DATA-CREATOR-PY](assets/fr/40.webp)


Następnie należy wypełnić profil profesora. Dostępnych jest kilka opcji:


- Wprowadź pierwsze litery swojego imienia i nazwiska w polu "Nazwa profesora". Twoje imię i nazwisko pojawi się na liście rozwijanej "Propozycje profesorów" poniżej. Wybierz je, klikając na nie;
- Alternatywnie możesz bezpośrednio kliknąć listę rozwijaną "Propozycje profesorów" i wybrać nazwisko swojego profesora.


Ta czynność spowoduje automatyczne wpisanie identyfikatora UUID profesora w odpowiednim polu.



![DATA-CREATOR-PY](assets/fr/41.webp)


Jeśli nie masz jeszcze profilu profesora, zapoznaj się z tym samouczkiem:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Następnie kliknij przycisk "Nowy samouczek".


![DATA-CREATOR-PY](assets/fr/42.webp)


Wybierz kategorię główną dla swojego samouczka. Następnie wybierz odpowiednią podkategorię w oparciu o wybraną kategorię główną.


![DATA-CREATOR-PY](assets/fr/43.webp)


Określ poziom trudności samouczka.


![DATA-CREATOR-PY](assets/fr/44.webp)


Wybierz nazwę dla katalogu utworzonego specjalnie na potrzeby samouczka. Nazwa tego folderu powinna odzwierciedlać oprogramowanie omówione w samouczku, używając myślników do oddzielenia słów. Na przykład, folder może mieć nazwę `red-Wallet`:


![DATA-CREATOR-PY](assets/fr/45.webp)


Identyfikator `project_id` to identyfikator UUID firmy lub organizacji stojącej za narzędziem opisanym w poradniku, dostępny [na liście projektów] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Na przykład, dla samouczka na temat Sparrow Wallet, można znaleźć jego `project_id` w pliku: `Bitcoin-educational-content/resources/projects/sparrow/project.yml`. Informacje te są dodawane do pliku YAML samouczka, ponieważ Plan ₿ Network utrzymuje bazę danych firm i organizacji aktywnych w Bitcoin lub powiązanych projektach. Dodając powiązany `project_id`, łączysz swoją zawartość z odpowiednim podmiotem.


***Aktualizacja:*** W nowej wersji skryptu nie trzeba już ręcznie wprowadzać `project_id`. Dodano funkcję wyszukiwania, aby znaleźć projekt według nazwy i automatycznie pobrać odpowiedni `project_id`. Wpisz początek nazwy projektu w polu "Project Name", aby go wyszukać, a następnie wybierz żądaną firmę z rozwijanego menu. Identyfikator `project_id` zostanie automatycznie wypełniony w polu poniżej. W razie potrzeby można go również wprowadzić ręcznie.


![DATA-CREATOR-PY](assets/fr/46.webp)


W przypadku tagów wybierz 2 lub 3 odpowiednie słowa kluczowe związane z treścią samouczka, wybierając wyłącznie z [listy tagów Plan ₿ Network] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). Oprogramowanie udostępnia również funkcję wyszukiwania słów kluczowych z rozwijaną listą.


![DATA-CREATOR-PY](assets/fr/47.webp)


Po wprowadzeniu i zweryfikowaniu wszystkich informacji kliknij przycisk "Utwórz samouczek", aby potwierdzić utworzenie plików samouczka. Spowoduje to generate folderu samouczka i wszystkich niezbędnych plików w wybranej kategorii lokalnie.


![DATA-CREATOR-PY](assets/fr/48.webp)


Możesz teraz pominąć podrozdział "Bez mojego skryptu Python", a także krok 3, "Wypełnij plik YAML", ponieważ skrypt już wykonał te czynności za Ciebie. Przejdź bezpośrednio do kroku 4 i zacznij pisać swój samouczek.


Więcej informacji na temat tego skryptu Pythona można znaleźć w pliku [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


### Bez mojego skryptu Pythona


Otwórz menedżera plików i przejdź do folderu `Bitcoin-educational-content`, który reprezentuje lokalny klon repozytorium. Zazwyczaj powinieneś go znaleźć pod `Documents\GitHub\Bitcoin-educational-content`.


W tym katalogu należy zlokalizować odpowiedni podfolder do umieszczenia samouczka. Organizacja folderów odzwierciedla różne sekcje strony Plan ₿ Network. W naszym przykładzie, ponieważ chcemy dodać samouczek na temat Sparrow Wallet, powinniśmy przejść do następującej ścieżki: `Bitcoin-educational-content\tutorials\Wallet`, która odpowiada sekcji `Wallet` na stronie internetowej:


![TUTO](assets/fr/12.webp)


W folderze `Wallet` należy utworzyć nowy katalog specjalnie dedykowany samouczkowi. Nazwa tego folderu powinna nawiązywać do oprogramowania opisanego w tutorialu, pamiętając o łączeniu słów myślnikami. W moim przykładzie folder będzie nosił nazwę `sparrow-Wallet`:


![TUTO](assets/fr/13.webp)


W tym nowym podfolderze poświęconym samouczkowi należy dodać kilka Elements:


- Utwórz folder `assets`, w którym znajdą się wszystkie ilustracje niezbędne do stworzenia samouczka;
- W folderze `assets` należy utworzyć podfolder o nazwie zgodnej z oryginalnym kodem językowym samouczka. Na przykład, jeśli samouczek jest napisany w języku angielskim, ten podfolder musi mieć nazwę `en`. Umieść w nim wszystkie elementy wizualne samouczka (diagramy, obrazy, zrzuty ekranu itp.).
- Plik `tutorial.yml` musi zostać utworzony w celu zapisania szczegółów związanych z samouczkiem;
- Należy utworzyć plik w formacie markdown, aby zapisać rzeczywistą treść samouczka. Plik ten musi być zatytułowany zgodnie z kodem języka, w którym został napisany. Na przykład, dla poradnika napisanego w języku francuskim, plik musi mieć nazwę `fr.md`.


![TUTO](assets/fr/14.webp)


Podsumowując, oto hierarchia plików do utworzenia:


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```


## 3 - Wypełnienie pliku YAML


Wypełnij plik `tutorial.yml` kopiując poniższy szablon:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


Poniżej znajdują się wymagane pola:



- id**: UUID (_Universally Unique Identifier_), który jednoznacznie identyfikuje samouczek. Można go generate za pomocą [narzędzia online](https://www.uuidgenerator.net/version4). Jedynym wymogiem jest to, aby ten identyfikator UUID był losowy, aby uniknąć konfliktów z innym identyfikatorem UUID na platformie;



- project_id**: UUID firmy lub organizacji stojącej za narzędziem prezentowanym w samouczku [z listy projektów](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Na przykład, jeśli tworzysz samouczek dotyczący oprogramowania Green Wallet, możesz znaleźć ten `project_id` w następującym pliku: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Ta informacja jest dodawana do pliku YAML samouczka, ponieważ Plan ₿ Network utrzymuje bazę danych wszystkich firm i organizacji działających na Bitcoin lub powiązanych projektach. Dodając `project_id` podmiotu powiązanego z twoim tutorialem, tworzysz link między dwoma Elements;



- tagi**: 2 lub 3 odpowiednie słowa kluczowe związane z treścią samouczka, wybrane wyłącznie [z listy tagów Plan ₿ Network] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- category**: Podkategoria odpowiadająca treści poradnika, zgodnie ze strukturą strony Plan ₿ Network (na przykład dla portfeli: `desktop`, `hardware`, `mobile`, `backup`);



- level**: Poziom trudności samouczka, wybierany spośród:
    - początkujący
    - `średniozaawansowany`
    - `zaawansowany`
    - `ekspert`



- professor_id**: Twój `professor_id` (UUID) wyświetlany w [profilu profesora](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors);



- original_language**: Oryginalny język samouczka (np. `fr`, `en` itp.);



- korekta**: Informacje o procesie korekty. Ukończ pierwszą część, ponieważ korekta własnego samouczka liczy się jako pierwsza weryfikacja:
    - language**: Kod języka korekty (np. `fr`, `en` itp.).
    - last_contribution_date**: Data dnia.
    - pilne**: 1
    - contributor_names**: Twój identyfikator GitHub.
    - nagroda**: 0


Aby uzyskać więcej informacji na temat identyfikatora nauczyciela, zapoznaj się z odpowiednim samouczkiem:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


Po zakończeniu modyfikacji pliku `tutorial.yml`, zapisz dokument klikając na `File > Save`:


![TUTO](assets/fr/16.webp)


Możesz teraz zamknąć edytor kodu.


## 4 - Wypełnij plik Markdown


Teraz możesz otworzyć plik, który będzie hostował twój samouczek, nazwany kodem twojego języka, na przykład `fr.md`. Przejdź do Obsidian, po lewej stronie okna, przewiń drzewo folderów, aż znajdziesz folder swojego samouczka i plik, którego szukasz:


![TUTO](assets/fr/18.webp)


Kliknij plik, aby go otworzyć:


![TUTO](assets/fr/19.webp)


Zaczniemy od wypełnienia sekcji `Properties` w górnej części dokumentu.


![TUTO](assets/fr/20.webp)


Ręcznie dodaj i wypełnij następujący blok kodu:


```
---
name: [Title]
description: [Description]
---
```


![TUTO](assets/fr/21.webp)


Wpisz nazwę swojego samouczka i jego krótki opis:


![TUTO](assets/fr/22.webp)


Następnie dodaj ścieżkę obrazu okładki na początku samouczka. Aby to zrobić, zanotuj:


```
![cover-sparrow](assets/cover.webp)
```


Ta składnia będzie przydatna, gdy konieczne będzie dodanie obrazu do samouczka. Wykrzyknik wskazuje, że jest to obraz, z tekstem alternatywnym (alt) określonym między nawiasami. Ścieżka do obrazu jest wskazana między nawiasami:


![TUTO](assets/fr/23.webp)


## 5 - Dodaj logo i okładkę


W folderze `assets` należy dodać plik o nazwie `logo.webp`, który będzie służył jako miniatura artykułu. Ten obraz musi być w formacie `.webp` i musi być kwadratowy, aby harmonizował z Interface użytkownika. Możesz wybrać logo oprogramowania opisanego w samouczku lub dowolny inny odpowiedni obraz, pod warunkiem, że jest wolny od praw. Ponadto, w tym samym miejscu należy dodać obraz o nazwie `cover.webp`. Obraz ten będzie wyświetlany w górnej części poradnika. Upewnij się, że ten obraz, podobnie jak logo, przestrzega praw użytkowania i jest odpowiedni dla kontekstu twojego samouczka:

## 6 - Pisanie samouczka i dodawanie wizualizacji


Kontynuuj pisanie samouczka, redagując treść. Jeśli chcesz zintegrować podtytuł, zastosuj odpowiednie formatowanie markdown, poprzedzając tekst `##`:


![TUTO](assets/fr/24.webp)


Podfolder language w folderze `assets` służy do przechowywania diagramów i wizualizacji, które będą towarzyszyć samouczkowi. O ile to możliwe, unikaj umieszczania tekstu na obrazach, aby treść była dostępna dla międzynarodowej publiczności. Oczywiście, prezentowane oprogramowanie będzie zawierać tekst, ale jeśli dodasz diagramy lub dodatkowe wskazówki na zrzutach ekranu oprogramowania, zrób to bez tekstu lub, jeśli okaże się to niezbędne, użyj języka angielskiego.


![TUTO](assets/fr/25.webp)


Aby nazwać obrazy, po prostu użyj numerów odpowiadających kolejności ich pojawiania się w samouczku, sformatowanych za pomocą dwóch cyfr (lub trzech cyfr, jeśli samouczek zawiera więcej niż 99 obrazów). Na przykład, nazwij swój pierwszy obraz `01.webp`, drugi `02.webp` i tak dalej.


Obrazy muszą być wyłącznie w formacie `.webp`. W razie potrzeby możesz użyć [mojego oprogramowania do konwersji obrazów] (https://github.com/LoicPandul/ImagesConverter).


![TUTO](assets/fr/26.webp)


Aby wstawić diagram do dokumentu, użyj następującego polecenia Markdown, upewniając się, że określono odpowiedni tekst alternatywny, a także poprawną ścieżkę obrazu:


```
![sparrow](assets/fr/01.webp)
```


Wykrzyknik na początku wskazuje, że jest to obraz. Tekst alternatywny, który pomaga w dostępności i SEO, jest umieszczony między nawiasami. Wreszcie, ścieżka do obrazu jest wskazana między nawiasami.


Jeśli chcesz tworzyć własne diagramy, pamiętaj o przestrzeganiu karty graficznej Plan ₿ Network, aby zapewnić spójność wizualną:


- Czcionka**: Użyj [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- Kolory**:
 - Pomarańczowy: #FF5C00
 - Czarny: #000000
 - Biały: #FFFFFF


**Niezbędne jest, aby wszystkie wizualizacje zintegrowane z samouczkami były wolne od praw lub respektowały licencję pliku źródłowego**. Ponadto wszystkie diagramy publikowane na Plan ₿ Network są udostępniane na licencji CC-BY-SA, tak samo jak tekst.

**-> Wskazówka:** Podczas publicznego udostępniania plików, takich jak obrazy, ważne jest, aby usunąć wszelkie niepotrzebne metadane. Mogą one zawierać poufne informacje, takie jak dane o lokalizacji, daty utworzenia lub szczegóły dotyczące autora. Aby chronić swoją prywatność, zaleca się usunięcie tych metadanych. Aby uprościć ten proces, można użyć specjalistycznych narzędzi, takich jak [Exif Cleaner](https://exifcleaner.com/), który umożliwia czyszczenie metadanych dokumentu za pomocą prostego przeciągania i upuszczania.

## 7 - Zapisz i prześlij samouczek


Po zakończeniu pisania samouczka w wybranym języku, następnym krokiem jest przesłanie **Pull Request**. Administrator zajmie się dodaniem brakujących tłumaczeń twojego poradnika, dzięki naszej zautomatyzowanej metodzie tłumaczenia z ludzką weryfikacją.


Aby kontynuować składanie Pull Request, otwórz oprogramowanie GitHub Desktop. Oprogramowanie powinno automatycznie wykryć zmiany wprowadzone lokalnie w gałęzi w porównaniu do oryginalnego repozytorium. Przed kontynuowaniem sprawdź dokładnie po lewej stronie Interface, czy zmiany te są zgodne z oczekiwaniami:


![TUTO](assets/fr/28.webp)


Dodaj tytuł swojego zatwierdzenia, a następnie kliknij niebieski przycisk `Commit to [your branch]`, aby zatwierdzić te zmiany:


![TUTO](assets/fr/29.webp)


Zatwierdzenie to zapis zmian wprowadzonych w gałęzi, któremu towarzyszy opisowa wiadomość, pozwalająca śledzić ewolucję projektu w czasie. Jest to rodzaj pośredniego punktu kontrolnego.


Następnie kliknij przycisk `Push origin`. Spowoduje to wysłanie zatwierdzenia do Fork:


![TUTO](assets/fr/30.webp)


Jeśli nie ukończyłeś samouczka, możesz wrócić do niego później i wprowadzić nowe zatwierdzenia. Jeśli ukończyłeś zmiany dla tej gałęzi, kliknij przycisk `Preview Pull Request`:


![TUTO](assets/fr/31.webp)


Możesz sprawdzić ostatni raz, czy wprowadzone modyfikacje są poprawne, a następnie kliknąć przycisk `Utwórz żądanie ściągnięcia`:


![TUTO](assets/fr/32.webp)


Żądanie ściągnięcia to prośba o zintegrowanie zmian z gałęzi użytkownika do głównej gałęzi repozytorium Plan ₿ Network, co pozwala na przejrzenie i omówienie zmian przed ich połączeniem.


Nastąpi automatyczne przekierowanie do przeglądarki w serwisie GitHub na stronę przygotowania wniosku o pociągnięcie:


![TUTO](assets/fr/33.webp)

Wskaż tytuł, który krótko podsumowuje zmiany, które chcesz scalić z repozytorium źródłowym. Dodaj krótki komentarz opisujący te zmiany (jeśli masz numer wydania powiązany z tworzeniem samouczka, pamiętaj, aby odnotować w komentarzu `Zamyka #{numer wydania}`), a następnie kliknij przycisk Green `Utwórz żądanie ściągnięcia`, aby potwierdzić żądanie scalenia:

![TUTO](assets/fr/34.webp)


Twój PR będzie wtedy widoczny w zakładce `Pull Request` głównego repozytorium Plan ₿ Network. Wszystko, co musisz zrobić, to poczekać, aż administrator skontaktuje się z tobą, aby potwierdzić połączenie twojego wkładu lub poprosić o dodatkowe modyfikacje.


![TUTO](assets/fr/35.webp)


Po scaleniu PR z główną gałęzią zaleca się usunięcie gałęzi roboczej (`tuto-sparrow-Wallet`), aby zachować czystą historię Fork. GitHub automatycznie zaoferuje tę opcję na stronie PR:


![TUTO](assets/fr/36.webp)


W oprogramowaniu GitHub Desktop można przełączyć się z powrotem do głównej gałęzi Fork (`dev`).


![TUTO](assets/fr/07.webp)


Jeśli chcesz wprowadzić zmiany w swoim wkładzie po przesłaniu PR, procedura zależy od aktualnego stanu PR:


- Jeśli twój PR jest nadal otwarty i nie został jeszcze scalony, wprowadź zmiany lokalnie, pozostając w tej samej gałęzi. Gdy modyfikacje zostaną sfinalizowane, użyj przycisku `Push origin`, aby dodać nowe zatwierdzenie do wciąż otwartego PR;
- Jeśli twój PR został już scalony z główną gałęzią, będziesz musiał rozpocząć proces od nowa, tworząc nową gałąź, a następnie przesyłając nowy PR. Przed kontynuowaniem upewnij się, że lokalne repozytorium jest zsynchronizowane z repozytorium źródłowym Plan ₿ Network.


Jeśli napotkasz trudności techniczne w przesłaniu swojego samouczka, nie wahaj się poprosić o pomoc na [naszej dedykowanej grupie Telegram dla kontrybucji] (https://t.me/PlanBNetwork_ContentBuilder). Dziękujemy!