---
name: Peach
description: Kompletny przewodnik po korzystaniu z Peach i handlu bitcoinami w P2P
---

![cover](assets/cover.webp)





## Wprowadzenie



Pozbawione KYC giełdy peer-to-peer (P2P) mają zasadnicze znaczenie dla zachowania poufności i autonomii finansowej użytkowników. Umożliwiają one bezpośrednie transakcje między osobami fizycznymi bez konieczności weryfikacji tożsamości, co ma kluczowe znaczenie dla tych, którzy cenią sobie prywatność. Aby lepiej zrozumieć koncepcje teoretyczne, zapoznaj się z kursem BTC204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Co to jest Peach?



Peach to platforma wymiany P2P, która pozwala użytkownikom kupować i sprzedawać bitcoiny bez KYC. Oferuje intuicyjny interfejs i zaawansowane funkcje bezpieczeństwa. W porównaniu z innymi rozwiązaniami, takimi jak Bisq, HodlHodl i Robosat, Peach wyróżnia się łatwością użytkowania.


System multisignature escrow (2-2) gwarantuje bezpieczeństwo środków podczas transakcji. Peach obsługuje różne metody płatności i posiada system reputacji, który kieruje działaniami traderów. Jak zwykle w przypadku platform P2P, ważne jest zatem utrzymanie dobrej reputacji w celu utrzymania wiarygodności wśród innych traderów.



### 2. Prywatność i gromadzone dane



**Jakie informacje gromadzi Peach?



Peach stara się przechowywać absolutne minimum danych o swoich użytkownikach. Oto przegląd danych przechowywanych na naszych serwerach:





- hash unikalnego identyfikatora aplikacji (AdID)
- hash danych dotyczących płatności
- Twoje zaszyfrowane rozmowy
- Dane transakcji w celu zapewnienia, że anonimowi użytkownicy nie przekraczają limitu handlowego (rodzaje używanych metod płatności, kwoty zakupu i sprzedaży)
- Addresses używane do wysyłania i odbierania z rachunku powierniczego
- Dane dotyczące użytkowania (Firebase i Google Analytics), wyłącznie za zgodą użytkownika



Dla przypomnienia, hash to dane, które stają się nierozpoznawalne, podobnie jak w przypadku szyfrowania. Te same dane zawsze będą generować ten sam hash, umożliwiając wykrycie duplikatów bez znajomości oryginalnych danych.



*Aby uzyskać bardziej szczegółowe wyjaśnienie hashing, weź udział w tym kursie:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Kto może zobaczyć moje dane dotyczące płatności?





- Tylko kontrahent może zobaczyć szczegóły płatności
- Dane są przesyłane za pośrednictwem serwerów Peach, ale są w pełni szyfrowane od końca do końca
- W przypadku sporu szczegóły płatności i historia konwersacji będą widoczne dla wyznaczonego mediatora Peach



## Instalacja i konfiguracja



### 1. Zainstaluj aplikację Peach



![Installation de Peach](assets/fr/01.webp)





- Pobierz aplikację z [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). W systemie iOS należy najpierw zainstalować aplikację [testflight](https://apps.apple.com/us/app/testflight/id899247664).
- Postępuj zgodnie z instrukcjami instalacji na urządzeniu.
- Podczas instalacji zostaniesz poproszony o wybranie, czy chcesz udostępnić określone dane w celu ulepszenia aplikacji Peach. (obraz 1)
- Na następnym ekranie (obrazek 2) dostępne są dwie opcje:
 - Jeśli jesteś nowym użytkownikiem, kliknij "Nowy użytkownik", aby utworzyć nowy profil
 - Jeśli masz już konto, użyj opcji "Przywróć", aby przywrócić istniejący profil
- Jeśli posiadasz kod polecający, możesz wpisać go tutaj.
- Aby przywrócić istniejące konto (obrazek 3), należy :
 - Plik kopii zapasowej
 - Hasło do odszyfrowania tego pliku



### 2. Przegląd ekranów głównych



Aplikacja Peach jest zorganizowana wokół czterech głównych ekranów dostępnych z dolnego paska nawigacyjnego:



![Navigation dans l'application](assets/fr/02.webp)





- Strona główna (4)** : Główny ekran, z którego można wybrać kupno lub sprzedaż, utworzyć nowe transakcje i uzyskać dostęp do dostępnych ofert:
 - tworzyć oferty za pomocą dwóch przycisków poniżej (utwórz kupno / utwórz sprzedaż)
 - skorzystać z istniejących ofert stworzonych przez innych użytkowników, korzystając z dwóch przycisków poniżej ("Kup"/"Sprzedaj").





- Wallet (5)** : Zintegrowany bitcoin wallet, który pozwala na :
 - Sprawdź saldo
 - Odbieranie bitcoinów
 - Bitcoiny Envoyer (z kontrolą monet)
 - Wyświetlanie historii transakcji
 - Finansowanie sprzedaży





- Transakcje (6)**: bieżące i przeszłe kontrakty w trzech zakładkach:
 - Zakupy w toku
 - Sprzedaż w toku
 - Historia twoich giełd





- Ustawienia (7)** : Koncentrator konfiguracji dla
 - Wyświetl swój profil (reputacja, odznaki, limity itp.)
 - Zarządzanie bezpieczeństwem (kopie zapasowe, pin)
 - Zarządzanie metodami płatności
 - Kontakt z pomocą techniczną
 - Zmień język
 - itp.



### 3. Konfiguracja metod płatności



![Accès aux paramètres de paiement](assets/fr/03.webp)



Metodami płatności można zarządzać w ustawieniach (obrazek 8)



Peach oferuje płatności online i płatności bezpośrednie (tylko na zarejestrowanych meetupach).



**Płatności online



**Ważne:**


aby chronić użytkowników, Peach wymaga, aby źródło środków było zgodne z reklamowanym. Do handlowców należy upewnienie się, że tak jest, dla ich własnej ochrony.



![Configuration des paiements en ligne](assets/fr/04.webp)



Aby dodać metodę :




- W zakładce "online" kliknij "dodaj walutę/metodę"
- Wybierz walutę
- Wybierz preferowaną metodę płatności



*Rodzaje dostępnych metod płatności:*



***W przypadku przelewów bankowych: ***




- SEPA (standardowa lub natychmiastowa)
- Wprowadź dane bankowe SEPA.



***Zaakceptowano wallet online :***




- Dostępnych jest kilka opcji w zależności od kraju (Revolut, Paypal, Wise, Strike itp.)
- Postępuj zgodnie z instrukcjami, aby dodać dane logowania



*karta podarunkowa do wykorzystania:*** Karta podarunkowa do wykorzystania:*** Karta podarunkowa do wykorzystania:*** Karta podarunkowa do wykorzystania:*** Karta podarunkowa do wykorzystania:*** Karta podarunkowa do wykorzystania:***




- Amazon, Steam itp.
- Wprowadź kraj wydania karty i inne niezbędne informacje



***Krajowe opcje płatności:***


Krajowe systemy płatności :




- Satispay (Włochy)
- MB Way (Portugalia)
- Bizum (Hiszpania)
- Szybsze płatności (Wielka Brytania)
- itp.



***W przypadku płatności bezpośrednich: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Wybierz "Meetup" (obrazek 12)
- Następnie wybierz spotkanie z listy (obrazek 13)



### Sposób użycia





- Możesz dodać kilka metod płatności
- Im więcej metod dodasz, tym szerszy zakres ofert będziesz mieć do dyspozycji
- Sprawdź poprawność swoich danych przed rejestracją
- Metody płatności można zmienić lub usunąć w dowolnym momencie



**Uwaga dotycząca bezpieczeństwa**: Informacje o płatności są szyfrowane i udostępniane tylko partnerowi wymiany podczas transakcji, z wyjątkiem sporów, do których dostęp będzie miał również mediator Peach.



### 4. Jak zabezpieczyć swoje portfolio



**Zrozumienie konta Peach



Konto Peach nie ma nazwy użytkownika ani hasła. Jest to plik przechowywany lokalnie w telefonie, co oznacza, że Peach nie musi przechowywać Twoich danych ani znać Twojej tożsamości: masz kontrolę. Plik ten zawiera wszystkie dane: w tym 12 słów do odzyskiwania bitcoinów, klucze PGP, szczegóły płatności itp. Dlatego ważne jest, aby zapisać ten plik i zabezpieczyć go hasłem __robust__.



Takie podejście gwarantuje pewien stopień poufności i pozostawia odpowiedzialność za zarządzanie danymi i kopiami zapasowymi w rękach użytkownika. Utrata telefonu bez kopii zapasowej oznacza utratę dostępu do konta Peach i środków.



**Utwórz kopie zapasowe**






- Dostęp do ustawień można uzyskać z zakładki w prawym dolnym rogu ekranu głównego
- Wybierz opcję "Kopie zapasowe" w menu ustawień



![Processus de sauvegarde](assets/fr/06.webp)



Dostępne są dwa rodzaje kopii zapasowych:



**Zapisz plik konta (obrazek 14)**




- Kliknij "Utwórz nową kopię zapasową"
- Utwórz **silne** hasło do szyfrowania pliku kopii zapasowej
- Wyślij ten plik do lokalizacji, która zapewni jego nadmiarowość w przypadku utraty telefonu.



Kopia zapasowa pliku przywraca całe konto Peach, w tym :




- Twoje portfolio
- Metody płatności
- Dane dotyczące płatności
- Historia transakcji ze szczegółowymi informacjami o kontrahentach i rozmowach z nimi



**Zapisywanie frazy odzyskiwania (obrazek 15)**




- Postępuj zgodnie z instrukcjami, aby wyświetlić frazę odzyskiwania
- Ostrożnie zapisz słowa we właściwej kolejności
- Przechowuj tę kopię zapasową w bezpiecznej lokalizacji, najlepiej innej niż plik konta



Fraza odzyskiwania umożliwia odzyskanie :




- Twoja reputacja, twoje transakcje
- Twoje fundusze bitcoin



Ale **NIE** następujące:




- Bieżące i przeszłe rozmowy
- Dane dotyczące płatności
- Informacje o kontrahencie w historii transakcji




## Kupowanie i sprzedawanie bitcoinów



### 1.a Jak kupić bitcoiny: Przyjmij ofertę sprzedaży



Pierwszym odruchem kupującego powinno być sprawdzenie ofert sprzedaży, które są już finansowane za pomocą bitcoinów.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Na ekranie głównym kliknij przycisk "Kup" (zdjęcie 16)
- Następnie można przejrzeć listę bitcoinów, które zostały umieszczone w systemie escrow i są gotowe do sprzedaży (obrazek 17). Możesz zobaczyć kwotę, cenę (w % w stosunku do rynku KYC), metody płatności i akceptowane waluty.
- Użyj filtrów do sortowania i porządkowania ofert (ilustracja 18).
- Uwaga: przycisk na dole strony filtrów umożliwia otrzymywanie powiadomień o opublikowaniu oferty pasującej do filtrów; oraz przycisk "reset", który po prostu czyści wszystkie filtry (zdjęcie 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Wyświetl odpowiadającą Ci ofertę i wyślij żądanie wymiany (zdjęcie 19)
- Możesz złożyć kilka wniosków o wymianę, a pierwsza pozytywna oferta anuluje pozostałe wnioski.
- Dokonać płatności w uzgodniony sposób.


**Przypomnienie:** Źródło środków musi być zgodne ze źródłem określonym podczas dodawania metody płatności.




- Potwierdź płatność w aplikacji natychmiast po jej dokonaniu**.
- Poczekaj, aż sprzedawca otrzyma płatność i zadeklaruj ją jako taką (zdjęcie 20)
- I wreszcie, oceń swoje doświadczenia ze sprzedawcą (zdjęcie 21)



![Réception des bitcoins](assets/fr/09.webp)





- Śledzenie statusu transakcji
- Sprawdź potwierdzenie otrzymania bitcoinów
- Środki będą dostępne w portfelu Peach (zdjęcie 22 i 23)



### 1.b Jak kupić bitcoiny: Utwórz ofertę



Jeśli nie możesz znaleźć odpowiedniej oferty sprzedaży, możesz utworzyć ofertę kupna. Ponieważ na tym etapie nie angażujesz żadnych bitcoinów, będziesz miał mniejsze szanse na znalezienie partnera do wymiany, zwłaszcza jeśli twoje osiągnięcia i reputacja są słabe lub nie istnieją. Aby temu zaradzić, ważne jest, aby podczas tworzenia oferty *złożyć ofertę o wysokiej cenie*, aby zmotywować sprzedawców do wybrania Twojej oferty. Kontynuujmy:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Na ekranie głównym kliknij przycisk "Utwórz ofertę zakupu" (zdjęcie 24)
- Dodaj metodę płatności, jeśli jeszcze tego nie zrobiłeś, i wprowadź swoje preferencje (ilość, premia itp.) (zdjęcie 25).


Opcja "natychmiastowa" umożliwia automatyczne zaakceptowanie żądania transakcji.




 - Kliknij ponownie "Utwórz ofertę", aby kontynuować
- Po utworzeniu, to sprzedający przychodzą do Ciebie z prośbą o wymianę. Możesz zamknąć i wyjść z aplikacji bez obaw.
- Możesz zmienić premię, jeśli nie otrzymasz żadnych zapytań. Pamiętaj: wyższa premia zmotywuje sprzedawców do skorzystania z Twojej oferty (zdjęcie 26).
- Swoją ofertę znajdziesz w zakładce "Kup", która znajduje się w oknie "Exchange" (rys. 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Po otrzymaniu prośby o zakup (rys. 28) (i jeśli nie dezaktywowałeś natychmiastowego handlu na rys. 25), zaakceptuj transakcję po sprawdzeniu reputacji sprzedawcy. Jeśli funkcja natychmiastowego handlu jest włączona, przejdź bezpośrednio do obrazka 29.
- Sprzedawca musi następnie umieścić bitcoiny w systemie escrow ("zasilić sejf"). (zdjęcie 29)
- Następnie zapłać sprzedawcy w miejscu docelowym pokazanym na Rys. 30 za pośrednictwem osobistego systemu bankowego. Nie przeciągaj kursora "Dokonałem płatności", dopóki tego nie zrobisz!
- Użytkownik może komunikować się ze sprzedawcą za pośrednictwem systemu wiadomości (szyfrowanego P2P). W przypadku problemu można otworzyć spór, klikając ikonę w prawym górnym rogu (zdjęcie 31). Wówczas do dyskusji włączy się mediator Peach.



![Offre de vente completée](assets/fr/12.webp)





- Gdy sprzedawca otrzyma pieniądze, zgłosi to, a system escrow zwolni bitcoiny, które będą w drodze do twojego wallet (domyślnie za pośrednictwem GroupHug, systemu grupowania transakcji Peach, który działa raz dziennie),
- Oceń swoje doświadczenia ze sprzedawcą



To wszystko!



**Uwaga dla nowych kupujących:** sprzedawcy opierają swoje transakcje na reputacji kupujących i zwykle unikają ofert od kupujących bez zakończonych transakcji. W pierwszej kolejności łatwiej jest zbudować reputację, przyjmując istniejące oferty sprzedaży.




### 2.a Jak sprzedawać bitcoiny: Utwórz sprzedaż



Najszybszym i najłatwiejszym sposobem sprzedaży na Peach jest **stworzenie oferty sprzedaży**.



![Création d'un ordre de vente](assets/fr/13.webp)





- Na stronie głównej kliknij opcję "Utwórz ofertę sprzedaży" (zdjęcie 32)
- Skonfiguruj swoją ofertę, upewnij się, że wprowadziłeś metodę płatności i odpowiednie parametry


można również :




  - stworzyć kilka identycznych ofert
  - aktywuj "natychmiastową wymianę", aby pierwszy kupujący, który się pojawi, mógł przyjąć umowę (bez Twojego potwierdzenia) i przystąpić do płatności.
  - wybierz adres zwrotu pieniędzy
  - finansowanie bagażnika z wallet Peach
- Sfinansuj transakcję, wysyłając bitcoiny na podany adres (obrazek 34)
- Poczekaj na potwierdzenie transakcji. Po zakończeniu Twoja oferta będzie widoczna na rynku.



![Attente du paiement](assets/fr/14.webp)





- Poczekaj, aż kupujący przyjmie Twoją ofertę. Rozważ zwiększenie premii (%), jeśli chcesz przyspieszyć bieg wydarzeń (zdjęcie 36)
- Po otrzymaniu prośby o wymianę sprawdź reputację kupującego. Sam oceń, czy profil jest dla Ciebie odpowiedni i kliknij "Akceptuj", jeśli tak. (37)
- Teraz kolej kupującego na dokonanie płatności ze swojego banku do Twojego. Następnie prześle on płatność do Ciebie. Nie wahaj się skontaktować z kupującym na czacie.
- po sprawdzeniu, że środki zostały otrzymane przez bank*, zwolnij środki, klikając przycisk "otrzymałem płatność" (obrazek 38). Nigdy nie potwierdzaj otrzymania płatności przed sprawdzeniem, czy wpłynęła ona na Twoje konto.
- Ocena transakcji
- Bitcoin są automatycznie wydawane kupującemu,



Proszę bardzo!



**Uwagi dotyczące bezpieczeństwa i wskazówki dotyczące udanej transakcji:**




 - Zwróć uwagę na dane kupującego i sprawdź, czy pochodzenie środków zgadza się z tym opisanym w Peach. Jeśli pochodzenie środków nie zgadza się z tym ogłoszonym, przejdź do czatu i otwórz spór (obrazek 39), a następnie odeślij środki z powrotem do miejsca ich pochodzenia.
 - Postępuj zgodnie z instrukcjami podanymi w żółtym kodzie.
 - Szybkie reagowanie na wiadomości od kontrahenta
 - zwracaj uwagę na postawę kupującego, zwłaszcza gdy masz do czynienia z profilem o niewielkim doświadczeniu
 - Nie wahaj się skorzystać z usługi mediacji, jeśli masz problem



### 2.b Jak sprzedawać bitcoiny: przyjmowanie ofert



Możliwe jest również przeglądanie i wybieranie ofert zakupu. Należy zachować szczególną ostrożność, ponieważ to właśnie tutaj można znaleźć najwięcej oszustów.



![Prendre une offre d'achat](assets/fr/15.webp)





- Na stronie głównej kliknij "Sprzedaż" (zdjęcie 40)
- Użyj filtrów, aby wyświetlić i wybrać najbardziej atrakcyjne oferty (zdjęcie 41)



![vérification de la réputation](assets/fr/16.webp)





- przed złożeniem wniosku o transakcję zalecamy ocenę przydatności profilu kupującego. Możesz kliknąć ofertę, a następnie identyfikator użytkownika, aby zobaczyć jego profil. Na przykład oferta na obrazku 42 może zostać uznana za "ryzykowną" (nowy użytkownik, stosunkowo wysoka kwota). "Ryzyko", jakie ponosisz, korzystając z tej oferty, to po prostu strata czasu, o ile nie popełnisz błędu polegającego na uwolnieniu bitcoinów bez otrzymania pieniędzy. Nadal możesz zdeponować bitcoiny w sejfie.


Z drugiej strony, ta na obrazku 43 pochodzi od doświadczonego tradera (obrazek 44), bez sporów w swojej historii. Jest to zatem mniej ryzykowna oferta.



![Match avec vendeur](assets/fr/17.webp)





- Po złożeniu oferty, jeśli kupujący zaakceptuje Twoją prośbę, aplikacja przeniesie Cię do obrazu 34, gdzie możesz kontynuować transakcję w sposób opisany poniżej.




## Zalety i wady



### Korzyści Peach





- Nie jest wymagany KYC**: Zachowuje poufność użytkownika.
- Brak dostępu do danych bankowych**: Peach nie ma dostępu do danych bankowych ani tożsamości użytkownika.
- Interface intuicyjny**: Łatwy w użyciu dla średnio zaawansowanych użytkowników.
- Open Source** : Kod źródłowy jest publiczny i weryfikowalny przez społeczność.



### Wady Peach





- Ograniczona Liquid**: Mniejszy wolumen obrotu niż w przypadku bardziej ugruntowanych platform.
- Ryzyko regulacyjne** : Aplikacja jest zarządzana przez szwajcarską firmę. Podlega zatem szwajcarskim przepisom, które mogą ewoluować i potencjalnie cenzurować aplikację.



## Przydatne zasoby





- Francuskie wideo objaśniające: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Skrócona instrukcja obsługi: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (uważaj na oszustów, administratorzy nigdy nie napiszą do ciebie najpierw przez prywatną wiadomość)