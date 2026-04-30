---
name: Delta Chat
description: Praktyczny przewodnik po zdecentralizowanym narzędziu do przesyłania wiadomości
---

![image](assets/cover.webp)




## Wprowadzenie - kontrola czatu i prywatność



W ostatnich latach coraz więcej mówi się o Chat Control, propozycji regulacyjnej, która ma na celu wprowadzenie automatycznego skanowania prywatnych wiadomości na głównych platformach komunikacyjnych. Deklarowanym celem jest walka z nielegalnymi treściami, problem polega na tym, że mechanizm ten w rzeczywistości wiązałby się z masową inwigilacją, podważając szyfrowanie end-to-end, a tym samym prywatność wszystkich użytkowników, a nie tylko przestępców.



Prawdziwe ryzyko polega na tym, że czaty stają się kontrolowanymi środowiskami, w których każda wiadomość, obraz lub załącznik mogą zostać sprawdzone, zanim jeszcze dotrą do odbiorcy. I tutaj pojawia się jedno z możliwych rozwiązań: odejście od scentralizowanych platform i przejście na zdecentralizowane systemy przesyłania wiadomości, które nie są zależne od jednego dostawcy i nie mogą być łatwo poddane tego rodzaju kontroli.



Jedno z takich rozwiązań zostanie zaprezentowane w tym poradniku: Delta Chat. Dojrzałe i już użyteczne narzędzie.




## Dlaczego Delta Chat i jak to działa



Delta Chat to już bardzo dobre rozwiązanie do przesyłania wiadomości do codziennego użytku: bardzo przydatne do rozmów z przyjaciółmi, rodziną i innymi ludźmi, podobnie jak prawdziwy odpowiednik WhatsApp.



Jest to zdecentralizowany system przesyłania wiadomości oparty w całości na poczcie e-mail. Zasadniczo wykorzystuje on infrastrukturę tradycyjnej poczty e-mail, ale buduje na niej nowoczesny interfejs komunikatora internetowego. Na pierwszy rzut oka może się to wydawać nieco improwizowane, ale w rzeczywistości działa bardzo dobrze i jest zaskakująco solidne. Można korzystać z dedykowanych serwerów pocztowych o nazwie ChatMail, ale może on również płynnie współpracować ze zwykłymi serwerami pocztowymi. Oznacza to, że możesz zalogować się za pomocą istniejącego konta, jeśli chcesz, bez konieczności tworzenia czegokolwiek nowego.



Kolejną atrakcją jest obsługa WebXDC, które są małymi aplikacjami internetowymi, które mogą być używane bezpośrednio w czatach, podobnie jak mini-aplikacje w Telegram. Ważną różnicą jest to, że aplikacje te nie mają dostępu do Internetu, więc nie mogą śledzić użytkownika ani wysyłać danych na zewnątrz.



Z punktu widzenia bezpieczeństwa, Delta Chat wykorzystuje zweryfikowane szyfrowanie end-to-end, oparte na PGP, ale z nowoczesnymi rozszerzeniami, które sprawiają, że poziom ochrony jest porównywalny z Signal. Jedynym obecnym brakiem jest Perfect Forward Secrecy, ale jest to aspekt ewoluujący.



Opierając się wyłącznie na poczcie e-mail, Delta Chat całkowicie tego unika:




- obowiązkowe numery telefonów
- Scentralizowane identyfikatory
- rejestracje powiązane z pojedynczą usługą



To właśnie sprawia, że narzędzie to jest bardzo odporne na inwazyjne regulacje, takie jak Chat Control.




## Instalacja



Z oficjalnej strony [Delta Chat](https://delta.chat/download) można przejść do sekcji pobierania. Na Linuksa jest on wygodnie dostępny przez Flathub, ale są też pakiety dla Arch, NixOS, Snap i wersje samodzielne.



![image](assets/it/01.webp)



Jest on również dostępny dla:




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Sklep Play](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- i innych sklepów (...).



Jeśli szukasz przewodnika po instalacji F-Droid, ten samouczek może ci pomóc:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Jedna bardzo ważna rzecz: wersje desktopowe nie wymagają telefonu. W przeciwieństwie do WhatsApp lub SimpleX Chat, nie musisz najpierw rejestrować się z telefonu komórkowego. Możesz utworzyć swój profil bezpośrednio na komputerze lub przenieść go z innego urządzenia.




## Tworzenie profilu



Po otwarciu aplikacji Delta Chat zapyta, czy utworzyć nowy profil, czy użyć istniejącego.



![image](assets/it/02.webp)



Tworząc nowy profil można wprowadzić:




- nazwa
- obraz (opcjonalnie)



Serwer ChatMail jest proponowany domyślnie, ale jest to możliwe:




- wybrać inny serwer ChatMail
- używać klasycznego konta e-mail
- ręczna konfiguracja IMAP i SMTP
- zarejestrować się przy użyciu kodu zaproszenia innego użytkownika



Po kilku sekundach profil jest gotowy i można rozpocząć korzystanie z aplikacji.



![image](assets/it/03.webp)




## Interface i czat



Interfejs jest bardzo prosty i nieskomplikowany:




- Komunikaty urządzenia, które są komunikacją lokalną
- Zapisane wiadomości, podobne do tych w Telegram i synchronizowane między urządzeniami



![image](assets/it/04.webp)



Aby dodać kontakt, po prostu:




- Wyświetlanie kodu QR
- Skanowanie drugiej osoby
- Zaproś przez link (udostępnij link zaproszenia).



![image](assets/it/05.webp)



Po nawiązaniu połączenia automatycznie konfigurowane jest szyfrowanie end-to-end. Interfejs użytkownika czatu jest bardzo podobny do interfejsu WhatsApp:




- wiadomości tekstowe i głosowe
- zdjęcia, filmy i pliki
- odpowiedzi na wiadomości
- reakcje
- wyskakujące komunikaty
- konfigurowalne powiadomienia.



![image](assets/it/06.webp)



## WebXDC: aplikacje w czatach:



Delta Chat umożliwia korzystanie z WebXDC, czyli małych aplikacji osadzonych w konwersacjach. Oto krótka lista najbardziej przydatnych z nich:




- ankiety
- deski kreślarskie
- tymczasowe czaty prywatne
- gry ze współdzielonymi wynikami na czacie



Można również uruchamiać bardziej złożone gry, co pokazuje elastyczność tego narzędzia.



![image](assets/it/07.webp)



## Grupy, kanały i funkcje zaawansowane



Możesz tworzyć grupy, używać naklejek (zwłaszcza na pulpitach), a po aktywowaniu opcji eksperymentalnych, nawet kanałów, podobnych do tych w Telegram.



W ustawieniach zaawansowanych można włączyć:




- połączenia głosowe (wciąż eksperymentalne)
- zaawansowane zarządzanie profilami e-mail
- pełne kopie zapasowe.



![image](assets/it/08.webp)



## Wiele urządzeń i tworzenie kopii zapasowych



Delta Chat w pełni obsługuje wiele urządzeń:




- można dodać drugie urządzenie za pomocą kodu QR
- można wykonać pełny transfer za pomocą kopii zapasowej.



W ciągu kilku sekund ponownie znajdziesz swoje czaty, grupy i całą historię, bez konieczności korzystania z centralnego serwera.



![image](assets/it/09.webp)




## Wnioski



W czasach, gdy coraz częściej mówi się o kontrolowaniu prywatnej komunikacji, Delta Chat stanowi konkretną odpowiedź: zdecentralizowane, szyfrowane wiadomości, które są naprawdę użyteczne każdego dnia.



Jest to rozwiązanie, które ze wszystkich, które wypróbowałem, najbardziej przekonało mnie prostotą, prywatnością i wolnością. Jeśli chcesz, możesz również skontaktować się ze mną na Delta Chat poprzez następujący [link do zaproszenia](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Jeśli podobał Ci się ten przewodnik, możesz mnie wesprzeć, przekazując darowiznę i zostawiając kciuk w górę. I pamiętaj: tylko używając i eksplorując Delta Chat zarówno z telefonu komórkowego, jak i komputera stacjonarnego, naprawdę odkryjesz jego pełną funkcjonalność.



Do następnego razu.