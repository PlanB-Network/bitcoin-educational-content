---
name: Wkład - samouczek Git (zaawansowany)
description: Przewodnik dla zaawansowanych użytkowników oferujący samouczek na temat Plan ₿ Network z Gitem
---
![cover](assets/cover.webp)


Przed przystąpieniem do tego samouczka dotyczącego dodawania nowego samouczka należy wykonać kilka wstępnych kroków. Jeśli jeszcze tego nie zrobiłeś, najpierw zapoznaj się z tym samouczkiem wprowadzającym, a następnie wróć tutaj:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Masz już :



- Wybierz motyw dla swojego samouczka;
- Kontakt z zespołem Plan ₿ Network za pośrednictwem [grupy Telegram](https://t.me/PlanBNetwork_ContentBuilder) lub paolo@planb.network ;
- Wybierz swoje narzędzia.


W tym samouczku dla doświadczonych użytkowników Git, krótko podsumujemy kluczowe kroki i podstawowe wytyczne dotyczące oferowania nowego samouczka Plan ₿ Network. Jeśli nie jesteś zaznajomiony z Git i GitHub, zalecam zamiast tego skorzystanie z jednego z tych 2 bardziej szczegółowych samouczków, które poprowadzą Cię krok po kroku:



- Średniozaawansowany (GitHub Desktop) :


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- Początkujący (web Interface) :


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Sugerowane narzędzia


Do edycji plików Markdown :



- Obsidian (darmowy, nie open-source)
- Mark Text (darmowy, open-source)
- Zettlr (darmowy, open-source)
- Typora (Payware, ~15€, nie open-source)


Dla Git :



- Git (darmowy, open-source)
- GitHub Desktop (bezpłatny, open-source)
- Sourcetree (bezpłatny, nie open-source)


Do edycji plików YAML :



- Visual Studio Code (bezpłatne, open-source)
- Sublime Text (darmowy z ograniczeniami, nie open-source)


Tworzenie diagramów i wizualizacji :



- Canva (darmowa z płatnymi opcjami, nie open-source)
- Inkscape (darmowy, open-source)
- Penpot (darmowy, open-source)


## Przepływy pracy


### 1 - Konfiguracja środowiska lokalnego



- Musisz mieć własny Fork z [repozytorium Plan ₿ Network na GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content).
- Zsynchronizuj główną gałąź (`dev`) Fork z repozytorium źródłowym.
- Zaktualizuj lokalnego klona.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - Utwórz nowy oddział



- Upewnij się, że jesteś w gałęzi `dev`.
- Utwórz nową gałąź z opisową nazwą (np. `tuto-Green-Wallet-loic`).
- Opublikuj tę gałąź w Fork online.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - Dodaj dokumenty samouczka


***Uwaga:*** Kroki 3 i 4 można zautomatyzować za pomocą [mojego skryptu Python GUI](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Uruchom go bezpośrednio z folderu w lokalnym klonie, a następnie wypełnij wymagane pola w GUI. Więcej informacji na temat instalacji i użytkowania można znaleźć w [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).


Jeśli wolisz zrobić to ręcznie, wykonaj następujące kroki :



- Zlokalizuj odpowiedni folder w lokalnym repozytorium (np. `tutorials/Wallet`).
- Utwórz katalog dedykowany samouczkowi z wyraźną nazwą (np. `Green-Wallet`). Ta nazwa folderu określi również ścieżkę URL samouczka. Powinna być pisana małymi literami, bez znaków specjalnych (z wyjątkiem myślników) i bez spacji.
- Dodaj następujące elementy do tego katalogu:
    - Podfolder o nazwie `assets` zawierający :
        - Dwa obrazy `.webp`:
            - `logo.webp`: Logo samouczka (kwadratowy format z tłem). To logo musi reprezentować prezentowane oprogramowanie lub narzędzie. Jeśli samouczek nie jest specyficzny dla narzędzia (np.: ogólny przewodnik po generowaniu frazy Mnemonic), możesz wybrać odpowiednią grafikę (np.: ogólną ikonę).
            - `cover.webp`: Obraz okładki wyświetlany na początku samouczka.
        - Podfolder zawierający kod oryginalnego języka samouczka. Na przykład, jeśli samouczek jest napisany w języku angielskim, ten podfolder powinien mieć nazwę `en'. W tym folderze należy umieścić wszystkie elementy wizualne samouczka (diagramy, obrazy, zrzuty ekranu itp.).
    - Plik `tutorial.yml` zawierający metadane (autor, tagi, kategoria, poziom trudności itp.).
    - Plik Markdown zawierający samouczek, nazwany zgodnie z kodem języka (np. `fr.md`, `en.md` itd.).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - Wypełnienie pliku YAML



- Uzupełnij plik `tutorial.yml` w następujący sposób:


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



- id** : UUID (_Universally Unique Identifier_), który jednoznacznie identyfikuje samouczek. Można go generate za pomocą [narzędzia online](https://www.uuidgenerator.net/version4). Jedynym wymogiem jest to, aby ten identyfikator UUID był losowy, aby uniknąć konfliktów z innym identyfikatorem UUID na platformie;



- project_id** : UUID firmy lub organizacji stojącej za narzędziem prezentowanym w samouczku [z listy projektów](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Na przykład, jeśli tworzysz samouczek dotyczący oprogramowania Green Wallet, możesz znaleźć ten `project_id` w następującym pliku: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Informacje te są dodawane do pliku YAML samouczka, ponieważ Plan ₿ Network utrzymuje bazę danych wszystkich firm i organizacji działających na Bitcoin lub powiązanych projektach. Dodając `project_id` podmiotu powiązanego z twoim tutorialem, tworzysz link między dwoma Elements;



- tagi** : 2 lub 3 odpowiednie słowa kluczowe związane z treścią samouczka, wybrane wyłącznie [z listy tagów Plan ₿ Network] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- category** : Podkategoria odpowiadająca treści poradnika, zgodnie ze strukturą strony Plan ₿ Network (na przykład dla portfeli: `desktop`, `hardware`, `mobile`, `backup`);



- level** : Poziom trudności samouczka, wybierany spośród:
    - początkujący
    - `średniozaawansowany`
    - `zaawansowany`
    - `ekspert`



- professor_id** : Twój `professor_id` (UUID) wyświetlany w [profilu profesora](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors);



- original_language** : Oryginalny język samouczka (np. `fr`, `en` itp.);



- korekta** : Informacje o procesie korekty. Ukończ pierwszą część, ponieważ korekta własnego samouczka liczy się jako pierwsza weryfikacja:
    - language** : Kod języka korekty (np. `fr`, `en` itp.).
    - last_contribution_date** : Data dnia.
    - pilne** : 1
    - contributor_names** : Twój identyfikator GitHub.
    - nagroda** : 0


Aby uzyskać więcej informacji na temat identyfikatora nauczyciela, zapoznaj się z odpowiednim samouczkiem :


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


### 5 - Tworzenie treści



- Uzupełnij właściwości pliku Markdown za pomocą :
    - Tytuł (`name`).
    - Krótki opis (`description`).
- Dodaj obraz okładki na górze samouczka, używając składni Markdown (zastąp "Green" nazwą pokazanego narzędzia):


```
![cover-green](assets/cover.webp)
```



- Napisz treść samouczka w Markdown:
    - Używaj dobrze skonstruowanych nagłówków (`##`), list i akapitów.
    - Wstawianie wizualizacji przy użyciu składni Markdown :


```
![nom-image](assets/en/001.webp)
```




- Umieść diagramy i obrazy w odpowiednim podfolderze językowym w `/assets`.


### 6 - Zapisz i prześlij samouczek



- Zapisz zmiany lokalnie, tworząc zatwierdzenie z opisową wiadomością.
- Prześlij zmiany do GitHub Fork.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- Po zakończeniu utwórz Pull Request (PR) na GitHub, aby zaproponować integrację swoich modyfikacji.
- Dodaj tytuł i krótki opis do PR. W komentarzu należy podać odpowiedni numer wydania.


### 7 - Korekta i scalanie



- Poczekaj na weryfikację lub informację zwrotną od administratora.
- W razie potrzeby wprowadź poprawki i opublikuj nowe zatwierdzenia.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- Po scaleniu PR można usunąć gałąź roboczą.


## Standardy tworzenia treści



- Formatowanie obsługiwane na platformie** :
    - Klasyczny Markdown: listy, linki, obrazy, cytaty, pogrubienie, kursywa itp.
    - LaTeX (tylko blok, nie inline): ograniczone przez `$$`.
    - Kod wbudowany: Składnia z pojedynczym backtickiem.
    - Bloki kodu: Składnia z trzema znakami backticks, na przykład :


```
print("Hello, Bitcoin!")
```



- Ilustracje i wykresy** :
    - Wszystkie obrazy muszą być w formacie WebP. Użyj tego bezpłatnego narzędzia, aby przekonwertować je w razie potrzeby: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Nazwij wizualizacje za pomocą 2 lub 3 cyfr (np. `001.webp`, `002.webp`).
    - W przypadku samouczków mobilnych lub Hardware Wallet użyj makiet.
    - Używaj tylko samodzielnie stworzonych lub bezpłatnych materiałów wizualnych.
    - Upewnij się, że są one istotne i wysokiej jakości.
- Karta graficzna** :
    - Czcionka: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Kolory Plan ₿ Network :
        - Pomarańczowy: `#FF5C00`
        - Czarny: `#000000`
        - Biały: `#FFFFFF`


Jeśli masz trudności techniczne z przesłaniem swojego samouczka, nie wahaj się poprosić o pomoc na [naszej dedykowanej grupie Telegram dla kontrybucji] (https://t.me/PlanBNetwork_ContentBuilder). Dziękujemy bardzo!