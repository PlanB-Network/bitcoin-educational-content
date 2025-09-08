---
name: Wkład - samouczek sieciowy GitHub (dla początkujących)
description: Kompletny przewodnik po samouczkach Plan ₿ Network z GitHub Web
---
![cover](assets/cover.webp)


Przed przystąpieniem do tego samouczka dotyczącego dodawania nowego samouczka należy wykonać kilka wstępnych kroków. Jeśli jeszcze tego nie zrobiłeś, najpierw zapoznaj się z tym samouczkiem wprowadzającym, a następnie wróć tutaj:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Masz już:




- Wybierz motyw dla swojego samouczka;
- Kontakt z zespołem Plan ₿ Network za pośrednictwem [grupy Telegram](https://t.me/PlanBNetwork_ContentBuilder) lub paolo@planb.network ;
- Wybierz swoje narzędzia.


W tym samouczku przyjrzymy się, jak dodać swój samouczek do Plan ₿ Network za pomocą internetowej wersji GitHub. Jeśli opanowałeś już Git, ten bardzo szczegółowy samouczek może nie być dla ciebie konieczny. Zamiast tego zalecam zapoznanie się z jednym z dwóch pozostałych poradników, w których szczegółowo opisuję wytyczne i kroki wprowadzania zmian z lokalnego pliku:




- Doświadczeni użytkownicy**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410


- Średniozaawansowany (GitHub Desktop)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Wymagania wstępne


Wymagania wstępne przed rozpoczęciem samouczka:




- Posiadać konto [GitHub] (https://github.com/signup);
- Posiadanie Fork z [repozytorium źródłowego Plan ₿ Network](https://github.com/PlanB-Network/Bitcoin-educational-content);
- Posiadać [profil nauczyciela na Plan ₿ Network](https://planb.network/professors) (tylko jeśli oferujesz pełny samouczek).


Jeśli potrzebujesz pomocy w uzyskaniu tych warunków wstępnych, moje inne samouczki będą pomocne:



https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Gdy wszystko jest już gotowe i masz Fork z repozytorium Plan ₿ Network, możesz rozpocząć dodawanie samouczka.


## 1 - Utwórz nowy oddział


Otwórz przeglądarkę i przejdź do strony Fork w repozytorium Plan ₿ Network. Jest to Fork utworzony w serwisie GitHub. Adres URL Fork powinien wyglądać następująco: `https://github.com/[twoja-nazwa-użytkownika]/Bitcoin-educational-content`:


![GITHUB](assets/fr/01.webp)


Upewnij się, że jesteś w głównej gałęzi `dev`, a następnie kliknij przycisk "*Sync Fork*". Jeśli Fork nie jest aktualny, GitHub poprosi o aktualizację gałęzi. Kontynuuj tę aktualizację:


![GITHUB](assets/fr/02.webp)


Kliknij gałąź `dev`, a następnie nazwij swoją gałąź roboczą tak, aby jej tytuł wyraźnie odzwierciedlał jej cel, używając myślników do oddzielenia słów. Na przykład, jeśli naszym celem jest napisanie samouczka na temat korzystania z Green Wallet, gałąź może nazywać się: `tuto-Green-Wallet-loic`. Po wprowadzeniu odpowiedniej nazwy, kliknij "*Twórz gałąź*", aby potwierdzić utworzenie nowej gałęzi opartej na `dev`:


![GITHUB](assets/fr/03.webp)


Powinieneś być teraz w nowej gałęzi pracy:


![GITHUB](assets/fr/04.webp)


Oznacza to, że wszelkie wprowadzone zmiany zostaną zapisane tylko w tej konkretnej gałęzi.


Dla każdego nowego artykułu, który planujesz opublikować, utwórz nową gałąź z `dev`.


Gałąź w Git reprezentuje równoległą wersję projektu, umożliwiając pracę nad modyfikacjami bez wpływu na główną gałąź, dopóki praca nie będzie gotowa do integracji.


## 2 - Dodaj pliki samouczka


Po utworzeniu gałęzi roboczej nadszedł czas na integrację nowego samouczka.


W plikach gałęzi należy znaleźć odpowiedni podfolder do umieszczenia samouczka. Organizacja folderów odzwierciedla różne sekcje witryny Plan ₿ Network. W naszym przykładzie, ponieważ dodajemy samouczek na Green Wallet, przejdź do następującej ścieżki: `Bitcoin-educational-content\tutorials\Wallet`, która odpowiada sekcji `Wallet` na stronie internetowej:


![GITHUB](assets/fr/05.webp)


W folderze `Wallet` utwórz nowy katalog przeznaczony specjalnie dla twojego samouczka. Nazwa tego folderu powinna wyraźnie wskazywać na oprogramowanie objęte samouczkiem, używając myślników do łączenia słów. W moim przykładzie folder będzie nosił nazwę `Green-Wallet`. Kliknij na "*Add File*", a następnie na "*Create new file*":


![GITHUB](assets/fr/06.webp)


Wprowadź nazwę folderu, a następnie ukośnik `/`, aby potwierdzić jego utworzenie jako folderu.


![GITHUB](assets/fr/07.webp)


W tym nowym podfolderze dedykowanym samouczkowi należy dodać kilka elementów:




- Utwórz folder `assets`, aby przechowywać wszystkie ilustracje potrzebne do tutorialu;
- W folderze `assets` utwórz podfolder o nazwie zgodnej z oryginalnym kodem językowym samouczka. Na przykład, jeśli samouczek jest napisany w języku angielskim, ten podfolder powinien mieć nazwę `en`. Umieść w tym folderze wszystkie elementy wizualne samouczka (diagramy, obrazy, zrzuty ekranu itp.).
- Plik `tutorial.yml` musi zostać utworzony w celu zapisania szczegółów samouczka;
- Aby zapisać rzeczywistą treść samouczka, należy utworzyć plik markdown. Plik ten musi być nazwany zgodnie z kodem języka, w którym jest napisany. Na przykład, dla poradnika napisanego w języku francuskim, plik powinien nazywać się `fr.md`.


Podsumowując, oto hierarchia plików (będziemy kontynuować ich tworzenie w następnej sekcji):


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```


## 3 - Wypełnienie pliku YAML


Zacznijmy od pliku YAML. W polu tworzenia nowego pliku wpisujemy `tutorial.yml`:


![GITHUB](assets/fr/08.webp)


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



- project_id**: UUID firmy lub organizacji stojącej za narzędziem prezentowanym w poradniku [z listy projektów](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Na przykład, jeśli tworzysz samouczek dotyczący oprogramowania Green Wallet, możesz znaleźć ten `project_id` w następującym pliku: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Informacje te są dodawane do pliku YAML samouczka, ponieważ Plan ₿ Network utrzymuje bazę danych wszystkich firm i organizacji działających na Bitcoin lub powiązanych projektach. Dodając `project_id` podmiotu powiązanego z twoim tutorialem, tworzysz link między dwoma Elements;



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


Po zakończeniu modyfikacji pliku `tutorial.yml`, zapisz dokument, klikając przycisk "*Commit changes...*":


![GITHUB](assets/fr/09.webp)


Dodaj tytuł i opis oraz upewnij się, że zatwierdzenie dotyczy gałęzi utworzonej na początku tego samouczka. Następnie potwierdź, klikając "*Commit changes*".


![GITHUB](assets/fr/10.webp)


## 4 - Tworzenie podfolderów dla obrazów


Kliknij ponownie na "*Add File*", a następnie na "*Create new file*":


![GITHUB](assets/fr/11.webp)


Wpisz `assets`, a następnie ukośnik `/`, aby utworzyć folder:


![GITHUB](assets/fr/12.webp)


Powtórz ten krok w folderze `/assets`, aby utworzyć podfolder językowy, na przykład `fr`, jeśli samouczek jest w języku francuskim:


![GITHUB](assets/fr/13.webp)


W tym folderze utwórz fikcyjny plik, aby zmusić GitHub do zachowania folderu (który w przeciwnym razie byłby pusty). Nazwij ten plik `.gitkeep`. Następnie kliknij "*Commit changes...*".


![GITHUB](assets/fr/14.webp)


Sprawdź ponownie, czy jesteś na właściwej gałęzi, a następnie kliknij "*Commit changes*".


![GITHUB](assets/fr/15.webp)


## 5 - Tworzenie pliku Markdown


Teraz utworzymy plik, który będzie hostował tutorial, nazwany zgodnie z kodem języka, na przykład `fr.md`, jeśli piszemy po francusku. Przejdź do folderu samouczka:


![GITHUB](assets/fr/16.webp)


Kliknij "Dodaj plik*", a następnie "Utwórz nowy plik*".


![GITHUB](assets/fr/17.webp)


Nazwij plik używając kodu języka. W moim przypadku, ponieważ samouczek jest napisany w języku francuskim, nazwałem swój plik `fr.md`. Rozszerzenie `.md` wskazuje, że plik jest w formacie Markdown.


![GITHUB](assets/fr/18.webp)


Zaczynamy od wypełnienia sekcji `Properties` na górze dokumentu. Ręcznie dodaj i wypełnij następujący blok kodu (klucze `name:` i `description:` muszą być w języku angielskim, ale ich wartości muszą być zapisane w języku używanym w samouczku):


```
---
name: [Titre]
description: [Description]
---
```


![GITHUB](assets/fr/19.webp)


Wpisz nazwę swojego samouczka i krótki opis:


![GITHUB](assets/fr/20.webp)


Następnie dodaj ścieżkę do obrazu okładki na początku samouczka. Aby to zrobić, zanotuj:


```
![cover-green](assets/cover.webp)
```


Ta składnia przyda się zawsze, gdy trzeba będzie dodać obraz do samouczka. Wykrzyknik wskazuje obraz, którego tekst alternatywny (alt) jest określony między nawiasami kwadratowymi. Ścieżka do obrazu jest wskazana między nawiasami:


![GITHUB](assets/fr/21.webp)


Kliknij przycisk "*Commit changes...*", aby zapisać plik.


![GITHUB](assets/fr/22.webp)


Sprawdź, czy jesteś we właściwej gałęzi, a następnie potwierdź zatwierdzenie.


![GITHUB](assets/fr/23.webp)


Folder samouczka powinien teraz wyglądać następująco, zgodnie z kodem języka:


![GITHUB](assets/fr/24.webp)


## 6 - Dodaj logo i okładkę


W folderze `assets` należy dodać plik o nazwie `logo.webp`, który będzie służył jako miniatura artykułu. Ten obraz musi być w formacie `.webp` i musi być kwadratowy, aby pasował do Interface użytkownika.


Możesz wybrać logo oprogramowania użyte w samouczku lub dowolny inny odpowiedni obraz, o ile jest on wolny od tantiem. Dodatkowo, dodaj obraz zatytułowany `cover.webp` w tym samym miejscu. Będzie on wyświetlany w górnej części samouczka. Upewnij się, że ten obraz, podobnie jak logo, respektuje prawa użytkowania i jest odpowiedni do kontekstu samouczka.


Aby dodać obrazy do folderu `/assets`, możesz przeciągnąć i upuścić je z plików lokalnych. Upewnij się, że jesteś w folderze `/assets` i we właściwej gałęzi, a następnie kliknij "*Commit changes*".


![GITHUB](assets/fr/26.webp)


Obrazy powinny pojawić się w folderze.


![GITHUB](assets/fr/27.webp)


## 7 - Pisanie samouczka


Kontynuuj pisanie samouczka, zapisując zawartość w pliku Markdown z kodem języka (w moim przykładzie, w języku francuskim, jest to plik `fr.md`). Przejdź do pliku i kliknij ikonę ołówka:


![GITHUB](assets/fr/28.webp)


Rozpocznij pisanie samouczka. Dodając podtytuł, użyj odpowiedniego formatowania Markdown, poprzedzając tekst `##`:


![GITHUB](assets/fr/29.webp)


Przełączaj się między widokami "*Edit*" i "*Preview*", aby lepiej wizualizować renderowanie.


![GITHUB](assets/fr/30.webp)


Aby zapisać swoją pracę, kliknij "*Commit Changes...*", upewnij się, że jesteś we właściwej gałęzi, a następnie potwierdź, klikając ponownie "*Commit Changes*".


![GITHUB](assets/fr/31.webp)


## 8 - Dodaj wizualizacje


Podfolder językowy w folderze `/assets` (w moim przykładzie: `/assets/en`) służy do przechowywania diagramów i wizualizacji, które będą towarzyszyć samouczkowi. O ile to możliwe, unikaj umieszczania tekstu na obrazach, aby treść była dostępna dla międzynarodowej publiczności. Oczywiście prezentowane oprogramowanie będzie zawierać tekst, ale jeśli dodasz schematy lub dodatkowe wskazówki na zrzutach ekranu oprogramowania, zrób to bez tekstu lub, jeśli to konieczne, użyj języka angielskiego.


Aby nazwać obrazy, po prostu użyj numerów odpowiadających kolejności ich pojawiania się w samouczku, sformatowanych jako dwie cyfry (lub trzy cyfry, jeśli samouczek zawiera więcej niż 99 obrazów). Na przykład, nazwij swój pierwszy obraz `01.webp`, drugi `02.webp` i tak dalej.


Obrazy muszą być wyłącznie w formacie `.webp`. W razie potrzeby możesz użyć [mojego oprogramowania do konwersji obrazów] (https://github.com/LoicPandul/ImagesConverter).


![GITHUB](assets/fr/32.webp)


Po dodaniu obrazów do podfolderu możesz usunąć fikcyjny plik `.gitkeep`. Otwórz ten plik, kliknij na trzy małe kropki w prawym górnym rogu, a następnie na "*Usuń plik*".


![GITHUB](assets/fr/33.webp)


Zapisz zmiany, klikając "*Commit changes...*".


![GITHUB](assets/fr/34.webp)


Aby wstawić diagram z podfolderu do dokumentu redakcyjnego, użyj następującego polecenia Markdown, zwracając uwagę na określenie odpowiedniego tekstu alternatywnego i prawidłowej ścieżki obrazu dla danego języka:


```
![green](assets/fr/01.webp)
```


Wykrzyknik na początku oznacza obraz. Tekst alternatywny, który pomaga w dostępności i odniesieniach, jest umieszczony między nawiasami kwadratowymi. Wreszcie, ścieżka do obrazu jest wskazana między nawiasami.


![GITHUB](assets/fr/35.webp)


Jeśli chcesz tworzyć własne schematy, pamiętaj o przestrzeganiu wytycznych graficznych Plan ₿ Network, aby zapewnić spójność wizualną:




- Czcionka**: Użyj [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- Kolory**:
 - Pomarańczowy: #FF5C00
 - Czarny: #000000
 - Biały: #FFFFFF


**Niezbędne jest, aby wszystkie wizualizacje zintegrowane z samouczkami były wolne od praw autorskich lub respektowały licencję pliku źródłowego**. Dlatego wszystkie diagramy publikowane na Plan ₿ Network są udostępniane na licencji CC-BY-SA, tak samo jak tekst.


**-> Wskazówka:** Podczas publicznego udostępniania plików, takich jak obrazy, ważne jest, aby usunąć zbędne metadane. Mogą one zawierać poufne informacje, takie jak dane o lokalizacji, daty utworzenia i szczegóły dotyczące autora. Aby chronić swoją prywatność, warto usunąć te metadane. Aby uprościć tę operację, można użyć specjalistycznych narzędzi, takich jak [Exif Cleaner](https://exifcleaner.com/), który umożliwia czyszczenie metadanych dokumentu za pomocą prostego przeciągania i upuszczania.


## 9 - Zaproponuj samouczek


Po zakończeniu pisania samouczka w wybranym języku, następnym krokiem jest przesłanie **Pull Request**. Administrator doda brakujące tłumaczenia do twojego poradnika, korzystając z naszej automatycznej metody tłumaczenia z korektą ludzką.


Aby kontynuować tworzenie pull requesta, po zapisaniu wszystkich zmian kliknij przycisk "*Contribute*", a następnie "*Open pull request*":


![GITHUB](assets/fr/36.webp)


Pull Request to prośba o zintegrowanie zmian z gałęzi użytkownika z główną gałęzią repozytorium Plan ₿ Network, co umożliwia przeglądanie i omawianie zmian przed ich scaleniem.


Przed kontynuowaniem sprawdź dokładnie na dole Interface, czy zmiany są zgodne z oczekiwaniami:


![GITHUB](assets/fr/37.webp)


Upewnij się, że gałąź robocza Interface została scalona z gałęzią `dev` repozytorium Plan ₿ Network (która jest gałęzią główną).


Wprowadź tytuł, który krótko podsumowuje zmiany, które chcesz scalić z repozytorium źródłowym. Dodaj krótki komentarz opisujący te zmiany (jeśli masz numer wydania powiązany z tworzeniem samouczka, pamiętaj, aby zanotować `Zamyka #{numer wydania}` jako komentarz), a następnie kliknij przycisk Green "*Utwórz żądanie ściągnięcia*", aby potwierdzić żądanie scalenia:


![GITHUB](assets/fr/38.webp)


Twój PR będzie widoczny w zakładce "*Pull Request*" w głównym repozytorium Plan ₿ Network. Wszystko, co musisz teraz zrobić, to poczekać, aż administrator skontaktuje się z Tobą, aby potwierdzić, że Twój wkład został scalony lub poprosić o dalsze modyfikacje.


![GITHUB](assets/fr/39.webp)


Po scaleniu PR z główną gałęzią, zalecamy usunięcie gałęzi roboczej (w moim przykładzie: `tuto-Green-Wallet`), aby zachować czystą historię Fork. GitHub automatycznie zaoferuje tę opcję na stronie PR:


![GITHUB](assets/fr/40.webp)


Jeśli chcesz wprowadzić zmiany w swoim wkładzie po przesłaniu PR, kroki, które należy wykonać, zależą od aktualnego statusu PR:




- Jeśli twój PR jest nadal otwarty i nie został jeszcze scalony, wprowadź zmiany w tej samej gałęzi roboczej. Zatwierdzone zmiany zostaną dodane do wciąż otwartego PR;
- W przypadku, gdy twój PR został już scalony z główną gałęzią, będziesz musiał powtórzyć proces od początku, tworząc nową gałąź, a następnie przesyłając nowy PR. Przed kontynuowaniem upewnij się, że Fork jest zsynchronizowane z repozytorium źródłowym Plan ₿ Network w gałęzi `dev`.


Jeśli masz trudności techniczne z przesłaniem swojego samouczka, nie wahaj się poprosić o pomoc na [naszej dedykowanej grupie Telegram dla kontrybucji] (https://t.me/PlanBNetwork_ContentBuilder). Dziękujemy bardzo!