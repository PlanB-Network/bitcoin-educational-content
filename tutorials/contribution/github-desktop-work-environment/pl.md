---
name: Pulpit GitHub
description: Jak skonfigurować lokalne środowisko pracy?
---
![github](assets/cover.webp)


Misją PlanB jest dostarczanie najwyższej jakości zasobów edukacyjnych na temat Bitcoin w jak największej liczbie języków. Wszystkie treści publikowane na stronie są open-source i hostowane na GitHub, co pozwala każdemu uczestniczyć we wzbogacaniu platformy. Wkład może przybierać różne formy: poprawianie i korekta istniejących tekstów, tłumaczenie na inne języki, aktualizowanie informacji lub tworzenie nowych samouczków, które nie są jeszcze dostępne na naszej stronie.


Jeśli chcesz wnieść swój wkład do PlanB Network, musisz użyć GitHub, aby zaproponować zmiany. W tym celu dostępne są dwie opcje:


- Przyczyń się bezpośrednio przez Interface** na stronie GitHub: Jest to najprostsza metoda. Jeśli jesteś początkującym użytkownikiem lub planujesz wnieść tylko kilka drobnych zmian, ta opcja jest prawdopodobnie najlepsza dla Ciebie;
- Współtwórz lokalnie za pomocą Git**: Ta metoda jest bardziej odpowiednia, jeśli planujesz wnosić regularny lub znaczący wkład w PlanB Network. Chociaż skonfigurowanie lokalnego środowiska Git na komputerze może początkowo wydawać się skomplikowane, podejście to jest bardziej wydajne na dłuższą metę. Pozwala ono na bardziej elastyczne zarządzanie zmianami. Jeśli jesteś w tym nowy, nie martw się, **wyjaśniamy cały proces konfiguracji środowiska w tym samouczku** (obiecujemy, że nie będziesz musiał wpisywać żadnych wierszy poleceń ^^).


Jeśli nie masz pojęcia, czym jest GitHub lub jeśli chcesz dowiedzieć się więcej o technicznych terminach związanych z Gitem i GitHubem, polecam przeczytać nasz artykuł wprowadzający, aby zapoznać się z tymi pojęciami.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c




- Aby rozpocząć, będziesz oczywiście potrzebować konta GitHub. Jeśli już je masz, możesz się zalogować, w przeciwnym razie możesz skorzystać z naszego samouczka, aby utworzyć nowe.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



## Krok 1: Instalacja GitHub Desktop



- Przejdź na stronę https://desktop.github.com/, aby pobrać oprogramowanie GitHub Desktop. Oprogramowanie to umożliwia łatwą interakcję z GitHub bez konieczności korzystania z terminala:

![github-desktop](assets/1.webp)


- Przy pierwszym uruchomieniu oprogramowania zostaniesz poproszony o podłączenie konta GitHub. Aby to zrobić, kliknij `Sign in to GitHub.com`:

![github-desktop](assets/2.webp)


- W przeglądarce otworzy się strona uwierzytelniania. Wprowadź swój adres e-mail Address i hasło wybrane podczas tworzenia konta, a następnie kliknij przycisk `Zaloguj`:

![github-desktop](assets/3.webp)


- Kliknij `Authorize desktop`, aby potwierdzić połączenie między Twoim kontem a oprogramowaniem:

![github-desktop](assets/4.webp)


- Nastąpi automatyczne przekierowanie do oprogramowania GitHub Desktop. Kliknij na `Finish`: ![github-desktop](assets/5.webp)
- Jeśli właśnie utworzyłeś swoje konto GitHub, zostaniesz przekierowany na stronę wskazującą, że nie utworzyłeś jeszcze żadnych repozytoriów. W tym momencie odłóż na bok oprogramowanie GitHub Desktop; wrócimy do niego później: ![github-desktop](assets/6.webp)


## Krok 2: Instalacja Obsidian


Przejdźmy teraz do instalacji oprogramowania do pisania. Tutaj masz kilka opcji. Będziesz potrzebował oprogramowania, które obsługuje edycję plików Markdown, ponieważ PlanB Network używa tego formatu dla plików tekstowych w swoim repozytorium.


Istnieje wiele programów specjalizujących się w edycji plików Markdown, takich jak Typora, zaprojektowanych specjalnie do pisania. Chociaż nie jest to idealne rozwiązanie, można również wybrać edytor kodu, taki jak Visual Studio Code (VSC) lub Sublime Text. Jednak jako pisarz wolę używać oprogramowania Obsidian. Zobaczmy razem, jak go zainstalować i rozpocząć z nim pracę.



- Wejdź na https://obsidian.md/download i pobierz oprogramowanie: ![github-desktop](assets/7.webp)
- Zainstaluj Obsidian, uruchom oprogramowanie, wybierz język, a następnie kliknij `Quick Start`: ![github-desktop](assets/8.webp)
- Dotrzesz do oprogramowania Obsidian. Na razie nie masz otwartych żadnych plików: ![github-desktop](assets/9.webp)


## Krok 3: Fork repozytorium PlanB Network



- Przejdź do repozytorium danych PlanB Network pod następującym adresem Address: [https://github.com/PlanB-Network/Bitcoin-educational-content](https://github.com/PlanB-Network/Bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Na tej stronie kliknij przycisk `Fork` w prawym górnym rogu okna: ![github-desktop](assets/11.webp)
- W menu tworzenia można pozostawić ustawienia domyślne. Upewnij się, że pole `Kopiuj tylko gałąź deweloperską` jest zaznaczone, a następnie kliknij przycisk `Utwórz Fork`: ![github-desktop](assets/12.webp)
- Następnie dotrzesz do własnego Fork repozytorium PlanB Network: ![github-desktop](assets/13.webp)

Ten Fork stanowi oddzielne repozytorium od oryginalnego, chociaż obecnie zawiera te same dane. Będziesz teraz pracować na tym nowym repozytorium.


W pewnym sensie stworzyliśmy kopię repozytorium źródłowego PlanB Network. Fork (kopia) i oryginalne repozytorium będą teraz rozwijać się niezależnie od siebie. W oryginalnym repozytorium inni współtwórcy mogą dodawać nowe dane, podczas gdy ty, na swoim Fork, będziesz kontynuował własne modyfikacje.

Aby zachować spójność między tymi dwoma repozytoriami, konieczna będzie ich okresowa synchronizacja, tak aby pobierały te same informacje. Aby wysłać zmiany do repozytorium źródłowego, należy użyć tak zwanego **Pull Request**. Aby zintegrować zmiany z repozytorium źródłowego do Fork, należy użyć polecenia **Sync Fork** dostępnego na GitHub web Interface.

![github-desktop](assets/14.webp)


## Krok 4: Klonowanie Fork



- Wróć do oprogramowania GitHub Desktop. W tym momencie twój Fork powinien pojawić się w sekcji `Twoje repozytoria`. Jeśli nie zobaczysz go od razu, użyj przycisku podwójnej strzałki, aby odświeżyć listę. Gdy pojawi się Fork, kliknij go, aby go wybrać:

![github-desktop](assets/15.webp)


- Następnie kliknij niebieski przycisk: `Clone [username]/Bitcoin-educational-content`:

![github-desktop](assets/16.webp)


- Zachowaj domyślną ścieżkę. Aby potwierdzić, kliknij niebieski przycisk `Clone`:

![github-desktop](assets/17.webp)


- Poczekaj, aż GitHub Desktop sklonuje lokalnie twój Fork:

![github-desktop](assets/18.webp)


- Po sklonowaniu repozytorium oprogramowanie oferuje dwie opcje. Należy wybrać pierwszą z nich: `To contribute to the parent project`. Ten wybór pozwoli ci zaprezentować swoją przyszłą pracę jako wkład w projekt macierzysty (`PlanB-Network/Bitcoin-educational-content`), a nie wyłącznie jako modyfikację twojego osobistego Fork (`[nazwa użytkownika]/Bitcoin-educational-content`). Po wybraniu opcji kliknij `Kontynuuj`:

![github-desktop](assets/19.webp)


- Pulpit GitHub jest teraz poprawnie skonfigurowany. Teraz możesz pozostawić oprogramowanie otwarte w tle, aby śledzić modyfikacje, które wprowadzimy.

![github-desktop](assets/20.webp)

To, co osiągnęliśmy na tym etapie, to utworzenie lokalnej kopii repozytorium, które jest hostowane na GitHub. Dla przypomnienia, to repozytorium jest Fork repozytorium źródłowego PlanB Network. Będziesz mógł wprowadzać modyfikacje do tej lokalnej kopii, takie jak dodawanie samouczków, tłumaczeń lub poprawek. Po wprowadzeniu tych modyfikacji należy użyć polecenia **Push origin**, aby wysłać lokalne modyfikacje do Fork hostowanego na GitHub.


Można również pobrać modyfikacje z Fork, na przykład podczas synchronizacji z repozytorium PlanB Network. W tym celu należy użyć polecenia **Fetch origin**, aby pobrać modyfikacje do lokalnej kopii (klonu), a następnie polecenia **Pull origin**, aby połączyć je ze swoją pracą. Pozwala to być na bieżąco z najnowszymi osiągnięciami projektu przy jednoczesnym efektywnym wkładzie.


![github-desktop](assets/21.webp)

## Krok 5: Utwórz nowy skarbiec Obsidian



- Otwórz oprogramowanie Obsidian i kliknij małą ikonę skarbca w lewym dolnym rogu okna:

![github-desktop](assets/22.webp)


- Kliknij przycisk `Open`, aby otworzyć istniejący folder jako skarbiec: ![github-desktop](assets/23.webp)
- Otworzy się eksplorator plików. Musisz zlokalizować i wybrać folder zatytułowany `GitHub`, który powinien znajdować się w katalogu `Documents` wśród twoich plików. Ścieżka ta odpowiada ścieżce ustalonej w kroku 4. Po wybraniu folderu potwierdź jego wybór. Tworzenie skarbca w Obsidian rozpocznie się na nowej stronie oprogramowania:


![github-desktop](assets/24.webp)

-> **Uwaga**, ważne jest, aby nie wybierać folderu `Bitcoin-educational-content` podczas tworzenia nowego skarbca w Obsidian. Zamiast tego należy wybrać folder nadrzędny, `GitHub`. Jeśli wybierzesz folder `Bitcoin-educational-content`, folder konfiguracyjny `.obsidian`, zawierający lokalne ustawienia Obsidian, zostanie automatycznie zintegrowany z repozytorium. Chcemy tego uniknąć, ponieważ nie jest konieczne przenoszenie konfiguracji Obsidian do repozytorium PlanB Network. Alternatywą jest dodanie folderu `.obsidian` do pliku `.gitignore`, ale ta metoda zmodyfikowałaby również plik `.gitignore` repozytorium źródłowego, co nie jest pożądane.



- Po lewej stronie okna widoczne jest drzewo plików z różnymi repozytoriami GitHub, które zostały sklonowane lokalnie.
- Klikając strzałki obok nazw folderów, można je rozwinąć, aby uzyskać dostęp do podfolderów repozytoriów i ich dokumentów:

![github-desktop](assets/25.webp)


- Nie zapomnij ustawić Obsidian na tryb ciemny: "Światło przyciąga błędy" ;)


## Krok 6: Zainstalowanie edytora kodu


Większość modyfikacji będzie dotyczyć plików w formacie Markdown (`.md`). Do edycji tych dokumentów można użyć oprogramowania Obsidian, które omówiliśmy wcześniej. Jednak PlanB Network używa innych formatów plików i będziesz musiał zmodyfikować niektóre z nich.


Na przykład podczas tworzenia nowego samouczka należy utworzyć plik YAML (`.yml`), aby wprowadzić tagi samouczka, jego tytuł i identyfikator nauczyciela. Obsidian nie oferuje możliwości modyfikowania tego typu plików, więc potrzebny będzie edytor kodu.


W tym celu dostępnych jest kilka opcji. Chociaż do tych modyfikacji można użyć standardowego notatnika komputera, rozwiązanie to nie jest idealne do schludnej pracy. Zalecam wybór oprogramowania specjalnie zaprojektowanego do tego celu, takiego jak [VS Code](https://code.visualstudio.com/download) lub [Sublime Text](https://www.sublimetext.com/download). Sublime Text, jako szczególnie lekki, będzie więcej niż wystarczający dla naszych potrzeb.


- Zainstaluj jeden z tych programów i zachowaj go do przyszłych modyfikacji. ![github-desktop](assets/26.webp)

Gratulacje! Twoje środowisko pracy jest teraz skonfigurowane do współtworzenia PlanB Network. Możesz teraz zapoznać się z naszymi innymi samouczkami dla każdego rodzaju wkładu (tłumaczenie, korekta, pisanie).


https://planb.network/tutorials/others

..).