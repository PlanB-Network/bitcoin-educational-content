---
name: Peach
description: Kompletny przewodnik po korzystaniu z Peach i wymianie bitcoinów P2P
---
![cover](assets/cover.webp)


![peach](https://youtu.be/ziwhv9KqVkM)


## Wprowadzenie


Pozbawione KYC giełdy peer-to-peer (P2P) mają zasadnicze znaczenie dla zachowania poufności i autonomii finansowej użytkowników. Umożliwiają one bezpośrednie transakcje między osobami fizycznymi bez konieczności weryfikacji tożsamości, co ma kluczowe znaczenie dla tych, którzy cenią sobie prywatność. Aby uzyskać bardziej dogłębne zrozumienie koncepcji teoretycznych, zapoznaj się z kursem BTC204:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Co to jest Peach?


Peach to platforma P2P Exchange, która pozwala użytkownikom kupować i sprzedawać bitcoiny bez KYC. Oferuje intuicyjny Interface i zaawansowane funkcje bezpieczeństwa. W porównaniu z innymi rozwiązaniami, takimi jak Bisq, HodlHodl i Robosat, Peach wyróżnia się łatwością obsługi i niskimi opłatami.


### 2. Prywatność i gromadzenie danych


**Jakie informacje gromadzi Peach?**


Peach stara się przechowywać absolutne minimum danych o swoich użytkownikach. Oto przegląd danych przechowywanych na serwerach firmy:




- Hash unikalnego identyfikatora aplikacji (AdID)
- Hash danych dotyczących płatności
- Twoje zaszyfrowane rozmowy
- Dane transakcji w celu zapewnienia, że anonimowi użytkownicy nie przekraczają limitu handlowego (rodzaje używanych metod płatności, kwoty zakupu i sprzedaży)
- Adresy używane do wysyłania i odbierania z rachunku powierniczego
- Dane dotyczące użytkowania (Firebase i Google Analytics), wyłącznie za zgodą użytkownika


Dla przypomnienia, Hash to dane, które stają się nierozpoznawalne, podobnie jak w przypadku szyfrowania. Te same dane zawsze będą generować ten sam Hash, umożliwiając wykrycie duplikatów bez znajomości oryginalnych danych.


*Więcej informacji na temat hashowania można znaleźć w tym kursie:*


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Kto może zobaczyć moje dane dotyczące płatności?**




- Tylko kontrahent może zobaczyć szczegóły płatności
- Dane są przesyłane za pośrednictwem serwerów Peach, ale są w pełni szyfrowane od końca do końca
- W przypadku sporu szczegóły płatności i historia konwersacji będą widoczne dla wyznaczonego mediatora Peach


## Instalacja i konfiguracja


### 1. Zainstaluj aplikację Peach


![Installation de Peach](assets/fr/01.webp)




- Pobierz aplikację ze strony [Peach Bitcoin] (https://peachbitcoin.com/fr/quick-start/).
- Postępuj zgodnie z instrukcjami instalacji na urządzeniu.
- Podczas instalacji zostaniesz poproszony o wybranie, czy chcesz udostępnić określone dane w celu ulepszenia aplikacji Peach (obrazek 1)
- Na następnym ekranie (obrazek 2) dostępne są dwie opcje:
 - Jeśli jesteś nowym użytkownikiem, kliknij "Nowy użytkownik", aby utworzyć nowy profil
 - Jeśli masz już konto, użyj opcji "Przywróć", aby przywrócić istniejący profil
- Jeśli posiadasz kod polecający, możesz wprowadzić go tutaj.
- Aby przywrócić istniejące konto (obrazek 3), należy :
 - Plik kopii zapasowej
 - Hasło do odszyfrowania tego pliku


### 2. Przegląd ekranów głównych


Aplikacja Peach jest zorganizowana wokół czterech głównych ekranów dostępnych z dolnego paska nawigacyjnego:


![Navigation dans l'application](assets/fr/02.webp)




- **Strona główna**: Główny ekran do kupowania i sprzedawania bitcoinów. W tym miejscu można tworzyć nowe transakcje i uzyskiwać dostęp do dostępnych ofert.
- **Wallet**: Zintegrowany Bitcoin Wallet, który umożliwia :
 - Sprawdź saldo
 - Odbieranie bitcoinów
 - Wysyłanie bitcoinów
 - Wyświetlanie historii transakcji
- **Transakcje**: Twoje centrum zarządzania handlem, w którym znajdziesz :
 - Bieżące transakcje
 - Pełna historia wymian
 - Status każdej transakcji
- **Ustawienia**: Centrum konfiguracji konta dla :
 - Zarządzanie metodami płatności
 - Konfiguracja kopii zapasowych
 - Dostosuj swoje preferencje
 - Dostęp do pomocy i wsparcia


### 3. Konfiguracja metod płatności


![Accès aux paramètres de paiement](assets/fr/03.webp)


Dostęp do metod płatności można uzyskać w zakładce Ustawienia (obrazek 8)


**Płatności online**


![Configuration des paiements en ligne](assets/fr/04.webp)




- Kliknij przycisk, aby dodać nową metodę płatności
- Wybierz walutę
- Wybierz preferowaną metodę płatności


*Rodzaje dostępnych metod płatności:*


***Dostępne przelewy bankowe: ***




- SEPA (standardowa lub natychmiastowa)
- Podaj swoje dane bankowe SEPA


***Portfele online akceptowane :***




- Dostępnych jest kilka opcji w zależności od kraju (Revolut, Paypal, Wise, Strike itp.)
- Postępuj zgodnie z instrukcjami, aby dodać dane logowania


***Karta podarunkowa, którą można wykorzystać :***




- Amazon
- Wprowadź kraj wydania karty i inne niezbędne informacje


***Krajowe opcje płatności:***


Krajowe systemy płatności :




- Satispay (Włochy)
- MB Way (Portugalia)
- Bizum (Hiszpania)
- Szybsze płatności (Wielka Brytania)


***Płatności osobiste:***


![Configuration des paiements en personne](assets/fr/05.webp)




- Wybierz "Meetup
- Następnie wybierz spotkanie z listy


### Sposób użycia




- Możesz skonfigurować kilka metod płatności jednocześnie
- Im więcej metod dodasz, tym szerszy zakres ofert będziesz mieć do dyspozycji
- Przed rejestracją sprawdź poprawność swoich danych
- Metody płatności można zmienić lub usunąć w dowolnym momencie


**Uwaga dotycząca bezpieczeństwa**: Informacje dotyczące płatności są szyfrowane i udostępniane tylko partnerowi Exchange podczas transakcji.


### 4. Jak zabezpieczyć Wallet


**Zrozumienie konta Peach**


Konto Peach nie jest tradycyjnym kontem z loginem i hasłem. Jest to plik przechowywany lokalnie w telefonie, co oznacza, że Peach nie musi przechowywać twoich danych ani znać twojej tożsamości: masz kontrolę. Plik ten zawiera wszystkie dane użytkownika, od kluczy Bitcoin Wallet po szczegóły płatności.


Takie podejście gwarantuje większą poufność, ale oznacza również większą odpowiedzialność. Utrata telefonu bez kopii zapasowej oznacza utratę dostępu do konta Peach i środków. Dlatego ważne jest, aby wykonać kopię zapasową tego pliku i zabezpieczyć go silnym hasłem.


**Utwórz kopie zapasowe**


![Accéder aux sauvegardes](assets/fr/13.webp)




- Dostęp do ustawień można uzyskać z zakładki w prawym dolnym rogu ekranu głównego
- Wybierz opcję "Kopie zapasowe" w menu ustawień


![Processus de sauvegarde](assets/fr/06.webp)


Dostępne są dwa rodzaje kopii zapasowych:


**Zapisz plik konta (obrazek 14)**




- Kliknij "Utwórz nową kopię zapasową"
- Utwórz silne hasło do szyfrowania pliku kopii zapasowej
- Przechowuj ten plik w bezpiecznym miejscu


Kopia zapasowa pliku przywraca całe konto Peach, w tym :




- Twój Wallet
- Metody płatności
- Historia konwersacji
- Dane dotyczące płatności
- Historia transakcji z danymi kontrahenta


**Zapisywanie frazy odzyskiwania (obrazek 15)**




- Postępuj zgodnie z instrukcjami, aby wyświetlić frazę odzyskiwania
- Ostrożnie zapisz słowa we właściwej kolejności
- Przechowuj tę kopię zapasową w bezpiecznej lokalizacji, najlepiej innej niż plik konta


Fraza odzyskiwania odzyskuje tylko :




- Dostęp do konta
- Twoje fundusze Bitcoin


Przegrasz:




- Historia konwersacji
- Dane dotyczące płatności
- Informacje o kontrahencie w historii transakcji


W celu zapewnienia optymalnego bezpieczeństwa zalecamy wykonywanie obu typów kopii zapasowych.


## Kupowanie i sprzedawanie bitcoinów


### 1. Jak kupić Bitcoiny


![Création et vue des offres](assets/fr/07.webp)




- Na ekranie głównym kliknij przycisk "Kup" (zdjęcie 16)
- Skonfiguruj zakup zgodnie ze swoimi preferencjami (zdjęcie 17)
- Przeglądanie listy dostępnych ofert (zdjęcie 18)


![Sélection et confirmation d'achat](assets/fr/08.webp)




- Wybierz ofertę odpowiednią dla siebie (zdjęcie 19)
- Dokonać płatności w uzgodniony sposób
- Potwierdź płatność w aplikacji i oceń transakcję (zdjęcie 20)


![Réception des bitcoins](assets/fr/09.webp)




- Śledzenie statusu transakcji
- Sprawdź potwierdzenie otrzymania bitcoinów
- Środki będą dostępne w Wallet Peach


### 2. Jak sprzedawać Bitcoiny


![Création d'un ordre de vente](assets/fr/10.webp)




- Skonfiguruj ofertę sprzedaży (zdjęcie 24)
- Sfinansuj transakcję, wysyłając bitcoiny na podany adres Address (zdjęcie 25)
- Poczekaj na potwierdzenie transakcji (zdjęcie 26)
- Twoja oferta jest teraz widoczna dla kupujących (zdjęcie 27)


![Attente du paiement](assets/fr/11.webp)




- Monitoruj status swojej oferty
- Oczekiwanie na potwierdzenie płatności od kupującego
- Sprawdź szczegóły transakcji


![Finalisation de la vente](assets/fr/12.webp)




- Sprawdź status płatności
- Potwierdzenie otrzymania płatności
- Ocena transakcji
- Bitcoiny są automatycznie wydawane kupującemu


**Wskazówki dotyczące udanej transakcji**




- Szybkie reagowanie na wiadomości od kontrahenta
- Dokładnie sprawdź szczegóły płatności
- Nie wahaj się skorzystać z usługi mediacji, jeśli masz problem


**Uwaga dotycząca bezpieczeństwa**: Nigdy nie potwierdzaj otrzymania płatności, dopóki nie zweryfikujesz, że wpłynęła ona na Twoje konto.


## Zalety i wady


### Korzyści z brzoskwini




- **Nie jest wymagany KYC**: Zachowuje poufność użytkownika.
- **Brak dostępu do danych bankowych**: Peach nie ma dostępu do danych bankowych ani tożsamości użytkownika.
- **Intuicyjny Interface**: Łatwy w użyciu dla średnio zaawansowanych użytkowników.
- **Open Source**: Kod źródłowy jest publiczny i weryfikowalny przez społeczność.


### Wady brzoskwini




- **Ograniczona płynność**: Mniejszy wolumen obrotu niż w przypadku bardziej ugruntowanych platform.
- **Ryzyko regulacyjne**: Aplikacja jest zarządzana przez szwajcarską firmę. Podlega zatem szwajcarskim przepisom, które mogą ewoluować i potencjalnie cenzurować aplikację.


## Przydatne zasoby




- Francuskie wideo objaśniające: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Skrócona instrukcja obsługi: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)