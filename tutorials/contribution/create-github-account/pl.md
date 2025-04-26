---
name: Konto GitHub
description: Jak utworzyć własne konto na GitHub?
---

![cover](assets/cover.webp)


Misją Plan ₿ jest dostarczanie najwyższej jakości zasobów edukacyjnych na temat Bitcoin, dostępnych w jak największej liczbie języków. Wszystkie treści publikowane na stronie są open-source i hostowane na GitHub, oferując każdemu możliwość przyczynienia się do wzbogacenia platformy. Wkład może przybierać różne formy: poprawianie i korekta istniejących tekstów, tłumaczenia na inne języki, aktualizowanie informacji lub tworzenie nowych samouczków, które nie są jeszcze dostępne na naszej stronie.


Jeśli chcesz współtworzyć Plan ₿ Network, będziesz musiał korzystać z Git i GitHub, więc jeśli te narzędzia są ci nieznane lub ich działanie wydaje się niejasne, nie panikuj, ten artykuł jest dla ciebie! Dokonamy wspólnie przeglądu podstaw Git i GitHub, a także związanego z nimi żargonu technicznego, aby umożliwić ci efektywne korzystanie z nich później.


## Czym jest Git?


Git to system kontroli wersji, zaprojektowany specjalnie do zarządzania projektami oprogramowania. Stworzony w 2005 roku przez Linusa Torvaldsa, Git szybko stał się standardem w branży tworzenia oprogramowania do kontroli wersji. Ale co to dokładnie oznacza?

![git](assets/11.webp)

W swojej istocie Git umożliwia programistom śledzenie zmian wprowadzanych w kodzie źródłowym projektu w czasie. Oznacza to, że przy każdej zmianie w kodzie, Git zapisuje nową wersję projektu. W przypadku wystąpienia błędu lub gdy eksperymentalna funkcja nie działa zgodnie z oczekiwaniami, możliwe jest przywrócenie poprzedniego stanu kodu, jak wehikuł czasu, ale dla plików.


Jedną z kluczowych funkcji Git jest zarządzanie gałęziami. Gałąź to rodzaj równoległej linii, na której deweloperzy mogą pracować niezależnie od reszty projektu. Znacznie ułatwia to dodawanie nowych funkcji lub poprawianie błędów bez naruszania głównego kodu. Gdy modyfikacje zostaną przetestowane i zatwierdzone, można je scalić z główną gałęzią.


Jedną z osobliwości Git jest jego zdolność do działania w sposób rozproszony. Każdy deweloper ma pełną kopię projektu na dysku Hard swojego komputera, co pozwala mu pracować w trybie offline i scalać zmiany później, gdy dostępne jest połączenie internetowe. Zmniejsza to ryzyko konfliktów i pozwala wielu deweloperom pracować jednocześnie nad tym samym projektem bez wchodzenia sobie w drogę.

Początkowo Git był przeznaczony głównie do projektów związanych z tworzeniem oprogramowania. Jednak może być również używany do zarządzania projektami pisania treści. Zamiast współpracować nad kodem, współpracujemy nad tekstem. I właśnie tę metodę Plan ₿ Network przyjęło do zarządzania swoimi treściami! Git ułatwia współpracę przy pisaniu kursów i samouczków, ponieważ pozwala na precyzyjne śledzenie zmian, wydajne zarządzanie wersjami, a także umożliwia przeglądanie i ulepszanie treści przez innych współtwórców.


## Czym jest GitHub?


GitHub to platforma do zarządzania kodem źródłowym i hostingu oparta na systemie kontroli wersji Git, który właśnie omówiliśmy. Uruchomiony w 2008 roku, GitHub szybko zyskał popularność i stał się niezbędnym punktem odniesienia dla programistów na całym świecie. Ale czym różni się GitHub od Git i dlaczego jest tak ważny w naszej metodzie tworzenia treści?

![github](assets/12.webp)

Po pierwsze, ważne jest, aby zrozumieć, że GitHub opiera się na Git (który omówiliśmy w poprzedniej sekcji). Podczas gdy Git jest narzędziem, które śledzi zmiany w kodzie, GitHub jest usługą online, która hostuje, udostępnia i zarządza tym kodem.


Wyobraź sobie Git jako rodzaj dziennika, którego każdy programista używa na własnym komputerze do rejestrowania wszystkich zmian w swoim projekcie. Z drugiej strony, GitHub jest jak publiczna biblioteka, w której wszystkie te dzienniki mogą być udostępniane, porównywane i łączone.


Podstawowa różnica między Git i GitHub polega na ich funkcji: Git jest narzędziem używanym lokalnie przez każdego dewelopera do zarządzania swoimi wersjami kodu, podczas gdy GitHub jest platformą internetową, która hostuje te wersje i ułatwia współpracę.


GitHub to znacznie więcej niż tylko usługa hostingu kodu. To platforma współpracy, która umożliwia programistom efektywną współpracę. I rzeczywiście, Plan ₿ Network wykorzystuje tę platformę do hostowania nie tylko całego kodu, który zasila witrynę, ale także, i to nas interesuje, całej zawartości (samouczki, szkolenia, zasoby...).


## Niektóre terminy techniczne


W Git i GitHub napotkasz polecenia i funkcje, których nazwy mogą wydawać się skomplikowane. W tej ostatniej części przedstawię kilka prostych definicji, aby zrozumieć terminy techniczne, które można napotkać podczas korzystania z Git i GitHub:



- Fetch origin:** Polecenie, które pobiera najnowsze informacje i zmiany ze zdalnego repozytorium bez scalania ich z lokalną pracą. Aktualizuje lokalne repozytorium o nowe gałęzie i zatwierdzenia obecne w zdalnym repozytorium.



- Pull origin:** Polecenie, które pobiera aktualizacje ze zdalnego repozytorium i natychmiast integruje je z lokalną gałęzią, aby ją zsynchronizować. Łączy to kroki pobierania i scalania w jednym poleceniu.
- Synchronizuj Fork:** Funkcja na GitHub, która umożliwia aktualizację Fork projektu o najnowsze zmiany z repozytorium źródłowego. Gwarantuje to, że kopia projektu jest na bieżąco z głównym rozwojem.
- Push origin:** Polecenie używane do wysyłania lokalnych zmian do zdalnego repozytorium.



- Pull Request:** Żądanie wysłane przez współautora w celu wskazania, że wprowadził zmiany do gałęzi w zdalnym repozytorium i chce, aby te zmiany zostały sprawdzone i potencjalnie scalone z główną gałęzią repozytorium.



- Zatwierdź:** Zapisywanie zmian. Zatwierdzenie jest jak natychmiastowa migawka pracy w danym momencie, co pozwala na zachowanie historii zmian. Każde zatwierdzenie zawiera opisową wiadomość wyjaśniającą, co zostało zmodyfikowane.



- Gałąź:** Równoległa wersja repozytorium, umożliwiająca pracę nad zmianami bez wpływu na główną gałąź (często nazywaną "główną" lub "master"). Gałęzie ułatwiają rozwój nowych funkcji i poprawianie błędów bez ryzyka zakłócenia stabilnego kodu.



- Scalanie:** Scalanie polega na integracji zmian z jednej gałęzi do drugiej. Służy na przykład do dodawania zmian z gałęzi roboczej do gałęzi głównej, co pozwala na dodawanie różnych wkładów.



- Fork:** Rozwidlenie repozytorium oznacza utworzenie kopii tego repozytorium na własnym koncie GitHub, co pozwala na pracę nad projektem bez wpływu na oryginalne repozytorium. Fork może albo pójść własną drogą i stać się innym projektem niż oryginalny, albo może regularnie synchronizować się z oryginalnym projektem, aby wnieść do niego swój wkład.



- Klonowanie:** Klonowanie repozytorium oznacza utworzenie lokalnej kopii na komputerze, co daje dostęp do wszystkich plików i historii. Pozwala to na pracę nad projektem bezpośrednio lokalnie.



- Repozytorium:** Miejsce przechowywania projektu na GitHub. Repozytorium zawiera wszystkie pliki projektu, a także historię wszystkich zmian, które zostały w nim wprowadzone. Jest to podstawa przechowywania i współpracy na GitHub.



- Issue:** Narzędzie do śledzenia zadań i błędów na GitHubie. Zagadnienia umożliwiają zgłaszanie problemów, proponowanie ulepszeń lub omawianie nowych funkcji. Każde zgłoszenie można przypisać, oznaczyć i skomentować.


Lista ta nie jest oczywiście wyczerpująca. Istnieje wiele innych terminów technicznych specyficznych dla Git i GitHub. Jednak te wymienione tutaj są głównymi, z którymi często będziesz się spotykać.


Po przeczytaniu tego artykułu możliwe jest, że niektóre aspekty Git i GitHub są nadal niejasne, dlatego zachęcam do samodzielnego rozpoczęcia korzystania z tych narzędzi. Praktyka jest często najlepszym sposobem na zrozumienie, jak działa maszyna! Aby rozpocząć, możesz odkryć te 2 inne samouczki:


## Jak utworzyć konto GitHub


Jeśli chcesz współtworzyć PlanB Network, będziesz potrzebować konta GitHub. W tym samouczku poprowadzimy Cię krok po kroku, jak utworzyć własne konto, skonfigurować je i odpowiednio zabezpieczyć.



- Przejdź do [https://github.com/signup](https://github.com/signup).
- Wprowadź swój adres e-mail Address, a następnie kliknij przycisk Green `Kontynuuj`:

![github](assets/1.webp)


- Wybierz silne hasło, a następnie kliknij przycisk Green "Kontynuuj":

![github](assets/12.webp)


- Następnie wybierz swoją nazwę użytkownika. Możesz ujawnić swoją prawdziwą tożsamość lub użyć pseudonimu. Następnie kliknij przycisk Green "Kontynuuj":

![github](assets/3.webp)


- Ukończ Captcha:

![github](assets/4.webp)


- Otrzymasz wiadomość e-mail zawierającą kod potwierdzający, który należy wprowadzić, aby sfinalizować tworzenie konta:

![github](assets/5.webp)


- Wypełnij pytania, jeśli chcesz, aby GitHub kierował Cię do określonych narzędzi, lub kliknij `pomiń personalizację`, aby ją pominąć:

![github](assets/6.webp)


- Wybierz darmowy plan, klikając przycisk "Kontynuuj za darmo":

![github](assets/7.webp)


- Nastąpi przekierowanie do pulpitu nawigacyjnego.
- Jeśli chcesz, możesz dostosować swoje konto, klikając swoje zdjęcie profilowe znajdujące się w prawym górnym rogu ekranu, a następnie przechodząc do menu `Ustawienia`:

![github](assets/8.webp)


- W tej sekcji możesz dodać nowe zdjęcie profilowe, wybrać nazwę, dostosować biografię lub dodać link do swojej osobistej strony internetowej:

![github](assets/9.webp)


- Zalecam również odwiedzenie menu `Hasło i uwierzytelnianie`, aby skonfigurować co najmniej uwierzytelnianie dwuskładnikowe:

![github](assets/10.webp)