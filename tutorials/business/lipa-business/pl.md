---
name: Lipa for Business
description: Rozwiązania płatnicze Bitcoin i Lightning dla sprzedawców
---

![cover](assets/cover.webp)



Sprzedawcy są obecnie coraz bardziej zainteresowani akceptowaniem płatności Bitcoin za pośrednictwem Lightning Network. W przeciwieństwie do tradycyjnych płatności kartą kredytową, które wiążą się z wysokimi opłatami i długim czasem rozliczenia, transakcje Lightning są praktycznie natychmiastowe, nie podlegają obciążeniom zwrotnym i zachowują poufność klienta.



Aby firma mogła łatwo wdrożyć Bitcoin, rozwiązanie płatnicze musi pozostać proste dzięki intuicyjnej kasie Interface, oferować funkcje dla wielu użytkowników i najlepiej oferować automatyczne przeliczanie na lokalną walutę w celu złagodzenia zmienności.



**Lipa for Business** jest idealną odpowiedzią na te potrzeby. Jest to szwajcarskie rozwiązanie opracowane przez Lightning Payment Services AG, zaprojektowane w celu umożliwienia sprzedawcom akceptowania płatności Bitcoin Lightning w prosty i wydajny sposób, przy jednoczesnym zachowaniu braku ograniczeń.



*Uwaga: Zrzuty ekranu użyte w tym samouczku pochodzą z oficjalnej strony Lipa for Business (lipa.swiss/en/for-business) i zostały użyte w celach edukacyjnych*



## Przedstawiamy Lipa dla biznesu



Lipa for Business to aplikacja mobilna, która działa jak kasa Bitcoin i Lightning. Oferuje usprawniony Interface do zbierania płatności w Sats i integruje profesjonalne funkcje: dostęp pracowników, eksport księgowości, pulpit nawigacyjny, a wszystko to bez konieczności posiadania środków.



### Najważniejsze cechy



**Natychmiastowe płatności Lightning**: Faktury Bitcoin Lightning są generowane w ciągu kilku sekund, zapewniając praktycznie natychmiastowe transakcje bez pośredników bankowych. Opłaty są niskie i przejrzyste w porównaniu do tradycyjnych rozwiązań.



**Interface POS intuicyjny**: Aplikacja zapewnia przejrzysty Interface POS, zaprojektowany do łatwego użytkowania w sklepie. Wprowadź kwotę w lokalnej walucie, a aplikacja natychmiast wyświetli kwotę w BTC i kod QR płatności. Kompatybilny ze wszystkimi portfelami Lightning na rynku.



**Zarządzanie wieloma pracownikami**: Wszyscy pracownicy mogą korzystać z aplikacji w celu wypłaty środków, bez konieczności posiadania do nich dostępu. Właściciel zachowuje pełną kontrolę, a synchronizacja w chmurze zapewnia, że żadna transakcja nie zostanie utracona. Każdy pracownik otrzymuje osobny dostęp za pośrednictwem zaproszenia z kodem QR.



**Automatyczna konwersja na CHF**: Dla szwajcarskich sprzedawców Lipa oferuje natychmiastową konwersję sprzedaży na franki szwajcarskie na koncie bankowym. Ta opcja jest opcjonalna: możesz zachować płatności w Bitcoin (bezpłatnie) lub przeliczyć je na CHF/EUR za 0,98% prowizji.



**Web dashboard**: Panel administracyjny Interface dostępny za pośrednictwem dashboard.lipa.swiss, umożliwiający przeglądanie wszystkich transakcji, filtrowanie według okresu lub pracownika oraz eksportowanie danych księgowych w formacie CSV. Pulpit nawigacyjny może być również używany do faktur internetowych generate z kodami QR bezpośrednio z Interface.



## Utwórz konto



⚠️ **Important** : Instalacja aplikacji wymaga szwajcarskiego miejsca zamieszkania. To ograniczenie geograficzne ma zastosowanie ze względu na zgodność z przepisami.



Aby korzystać z Lipa for Business, należy najpierw utworzyć dedykowane konto sprzedawcy:





- Wejdź na stronę lipa.swiss/for-business i pobierz aplikację na swoją platformę (Android lub iOS)
- Zainstaluj "lipa Wallet for business" z Google Play lub App Store
- Przy pierwszym uruchomieniu wprowadź dane swojej firmy: nazwę firmy, kontaktowy adres e-mail, telefon i Address
- Adres e-mail jest głównym identyfikatorem dostępu do pulpitu nawigacyjnego



Po przesłaniu formularza Lipa utworzy Twoją przestrzeń handlową. Przed ostateczną aktywacją może zostać przeprowadzona krótka ręczna kontrola (uproszczony proces KYC). Aktywacja następuje zwykle w ciągu 24 godzin, ale czas ten może się różnić.



**Ważne**: Do rozpoczęcia wypłaty środków w Bitcoin nie jest wymagane połączenie z kontem bankowym. Dane bankowe są wymagane tylko w przypadku wybrania automatycznej konwersji na CHF.



## Instalacja i Interface



**Aplikacja mobilna**: Dostępna na smartfony i tablety z systemem Android/iOS. Interface został zaprojektowany do użytku w punkcie sprzedaży, z czytelnym Elements i interakcjami ograniczonymi do tego, co niezbędne. Przycisk "Zrealizuj płatność" zapewnia dostęp do ekranu wprowadzania kwoty.



**Wymagania techniczne**: Wymagane stabilne połączenie internetowe (minimum 3G) do przetwarzania płatności Lightning w czasie rzeczywistym.



**Web dashboard**: Bezpłatny pulpit dostępny pod adresem dashboard.lipa.swiss. Bezpieczne połączenie e-mail (magiczny link bez hasła). Interface pokazuje wszystkie transakcje z pełnymi szczegółami: data, kwota BTC/fiat, kurs Exchange, pracownik itp. Eksport CSV do integracji z księgowością.



![Dashboard Lipa Business](assets/fr/02.webp)



Pulpit nawigacyjny może być również używany do faktur internetowych generate z kodami QR bezpośrednio z Interface:



![Génération factures web](assets/fr/03.webp)



**Multi-terminal**: Natywne wsparcie dla wielu terminali w firmie. Dodaj nowe urządzenia, tworząc pracowników za pomocą zaproszenia z kodem QR. Każdy terminal jest powiązany z tym samym sprzedawcą Wallet, zachowując identyfikowalność według kasjera.



## Akceptowanie płatności



Proces windykacji jest podobny do konwencjonalnej transakcji:



![Processus de paiement Lipa](assets/fr/01.webp)





- Wprowadź kwotę**: Na ekranie płatności wprowadź kwotę w lokalnej walucie (CHF lub EUR). Przykład: za kawę w cenie 4,50 CHF, wprowadź 4,50
- Generowanie Invoice** : Aplikacja natychmiast przelicza kwotę na satoshi po aktualnym kursie i generuje błyskawiczny Invoice w formie kodu QR
- Płatność klienta** : Klient skanuje kod QR za pomocą Wallet Lightning i zatwierdza płatność
- Potwierdzenie** : Płatność jest potwierdzana w ciągu kilku sekund, z wizualnym wyświetleniem sukcesu



## Profesjonalne narzędzia



**Historia i statystyki**: Każda płatność jest rejestrowana z pełnymi szczegółami. Pulpit nawigacyjny oferuje przegląd z filtrami według okresu lub pracownika, porównywalny z klasycznym systemem kasowym.



**Eksport danych księgowych**: Eksport danych w formacie CSV/Excel ze wszystkimi niezbędnymi informacjami (stawka Exchange, transaction ID) w celu integracji z oprogramowaniem księgowym.



**Zarządzanie pracownikami**: Dodawanie/usuwanie autoryzowanych użytkowników za pośrednictwem pulpitu nawigacyjnego. Każdy pracownik otrzymuje oddzielny dostęp z możliwością śledzenia transakcji. Cofnięcie dostępu możliwe w dowolnym momencie.



**Kopia zapasowa**: Niepowiernicze konto sprzedawcy z 24-słowną frazą odzyskiwania do przechowywania. Tylko właściciel głównego Wallet powinien zarządzać tą kopią zapasową - pracownicy nie mają do niej dostępu.



## Automatyczne przeliczanie CHF



**Dostępność**: Usługa dostępna dla szwajcarskich sprzedawców z płatnością w CHF (EUR w zależności od dostępności).



**Konfiguracja**: Wybór między odbiorem w Bitcoin (bezpłatnie) lub konwersją fiat za pośrednictwem partnera finansowego. W przypadku konwersji na CHF, wprowadź IBAN dla przelewów.



**Opłaty**: 0.98% prowizji od przeliczonych kwot (w porównaniu do 0% w przypadku płatności w BTC). Brak innych ukrytych opłat lub subskrypcji.



**Jak to działa? Otrzymana kwota jest natychmiast sprzedawana po kursie rynkowym i przelewana na konto bankowe. Przelew następuje zgodnie ze standardowymi terminami banku.



**Elastyczność**: Opcja odwracalna w dowolnym momencie w parametrach. Umożliwia testowanie w trybie "konwersji fiat", a następnie przełączenie na 100% BTC, gdy poczujesz się komfortowo.



## Bezpieczeństwo i poufność



** Bez opieki**: Użytkownik zachowuje stałą kontrolę nad otrzymanymi środkami. Para kluczy prywatny/publiczny jest generowana podczas konfiguracji (stąd 24-wyrazowa fraza). Lipa nie przechowuje kluczy prywatnych użytkownika.



**Bezpieczeństwo pracowników**: Pracownicy mogą jedynie tworzyć faktury, a nie wydawać środki. W przypadku problemów z terminalem środki pozostają bezpieczne, a dostęp można cofnąć.



**Poufność klienta**: pseudonimowe płatności Lightning bez dołączonych danych osobowych. W przeciwieństwie do płatności kartą, które przechodzą przez scentralizowane sieci.



**Uwierzytelnianie**: Pulpit nawigacyjny dostępny za pośrednictwem wiadomości e-mail z magicznym łączem. Aplikacja mobilna chroniona kodem PIN lub danymi biometrycznymi.



## Zalecane przypadki użycia





- Gastronomia**: Bary, restauracje, kawiarnie do przyjmowania dodatków w Bitcoin z zarządzaniem napiwkami
- Handel detaliczny**: Sklepy spożywcze, piekarnie w celu rozszerzenia metod płatności bez stałych opłat
- Nomadyczni sprzedawcy**: food trucki, targi, festiwale za pomocą smartfona
- Wydarzenia** : Tymczasowe stoiska z gotowymi do użycia rozwiązaniami
- Usługi**: Konsultanci, rzemieślnicy do jednorazowego rozliczenia w Bitcoin



## Zalety i ograniczenia



### Korzyści




- Prosty Interface bez konieczności posiadania umiejętności technicznych
- Rozwiązanie bez opieki z całkowitą kontrolą środków
- Zarządzanie wieloma pracownikami z możliwością śledzenia
- W zestawie eksport księgowości i pulpit nawigacyjny
- Opcja automatycznej konwersji CHF dla szwajcarskich sprzedawców detalicznych
- Przejrzyste opłaty: 0% Bitcoin, 0,98% konwersji fiat
- Pozycjonowanie jako innowacyjna firma w ekosystemie Bitcoin
- Ochrona przed inflacją i dewaluacją waluty
- Odporny na cenzurę, zdecentralizowany system płatności



### Ograniczenia




- Tylko obsługa błyskawic (bez Bitcoin On-Chain)
- Konwersja Fiata jest obecnie ograniczona do Szwajcarii
- Wymaga od klientów posiadania kompatybilnego Wallet Lightning
- Statyczne kody QR nie są obecnie dostępne
- Połączenie internetowe wymagane dla wszystkich transakcji



## Wnioski



Lipa for Business jest pozycjonowana jako kompletne rozwiązanie do akceptacji Bitcoin w sklepie. Nie wymaga kosztownej infrastruktury (wystarczy zwykły smartfon), koszty są niskie i stałe, a integracja z istniejącymi procesami jest łatwa.



Jego przyjazny dla prywatności charakter, w połączeniu z profesjonalnymi narzędziami do zarządzania, czyni go atrakcyjnym wyborem dla sprzedawców, którzy chcą wdrożyć Bitcoin przy jednoczesnym zachowaniu prostoty i bezpieczeństwa.



## Zasoby





- [Oficjalna strona Lipa for Business](https://lipa.swiss/en/for-business)
- [Dashboard web](https://dashboard.lipa.swiss)
- [Lipa Support for Business](https://help.lipa.swiss/business)
- [Lipa General Support](https://help.lipa.swiss/Wallet)
- [LinkedIn Lipa](https://www.linkedin.com/company/getlipa)
- [Twitter @lipa_btc](https://twitter.com/lipa_btc)