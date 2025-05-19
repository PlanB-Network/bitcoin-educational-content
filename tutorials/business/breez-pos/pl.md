---
name: Punkt sprzedaży Breez

description: Przewodnik po rozpoczęciu akceptacji Bitcoin przy użyciu Breez POS
---

![cover](assets/cover.webp)

ten tekst pochodzi ze strony internetowej z dokumentacją Breez: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_


## Czym jest Breez POS?


**Breez** to w pełni funkcjonalna aplikacja Lightning. Rozłóżmy to na czynniki pierwsze:



- Lightning** to sieć płatności Bitcoin, która skraca czas transakcji z minut do milisekund, a opłaty transakcyjne z kilku dolarów do kilku centów lub mniej. Lightning zmienia Bitcoin z cyfrowego złota w cyfrową walutę, zachowując przy tym wszystkie korzyści, które sprawiają, że Bitcoin jest świetny.
- Non-custodial** oznacza, że Breez nie przejmuje pieniędzy użytkowników. Wiele aplikacji Lightning przejmuje pieniądze swoich użytkowników. Są to w zasadzie banki Bitcoin. W przypadku aplikacji non-custodial, takiej jak Breez, wszyscy użytkownicy są swoimi własnymi bankami.
- Pełna obsługa** oznacza, że Breez zajmuje się prawie wszystkimi operacjami technicznymi automatycznie i w tle. Rzeczy takie jak tworzenie kanałów, płynność przychodząca i routing pozostają pod maską. (Ale Breez jest również open source, więc osoby zainteresowane audytem technologii są mile widziane)


**Breez POS** to skrót od naszego trybu punktu sprzedaży. Innymi słowy, Breez działa jak cyfrowa kasa fiskalna dla firm i sprzedawców, którzy chcą akceptować płatności Lightning (oprócz trybu "standardowego", który jest jak cyfrowa wersja skórzanego Wallet dla Bitcoin i odtwarzacza podcastów nowej generacji). Przyjrzyjmy się teraz, jak skonfigurować Breez jako kasę Lightning dla swojej firmy.


## Jak rozpocząć korzystanie z Breez?


1. Pierwszym krokiem jest pobranie aplikacji. Jest ona dostępna na Androida i iOS (zainstaluj TestFlight i kliknij link na swoim urządzeniu).

2. Breez może automatycznie tworzyć kopie zapasowe na Dysku Google, iCloud lub dowolnym serwerze WebDav.

**Uwaga:** Każde urządzenie obsługuje własny węzeł Lightning. Możesz uruchomić tryb POS na dowolnej liczbie urządzeń, ale salda pozostaną oddzielne.

3. Po otwarciu aplikacji kliknij ikonę w lewym górnym rogu, aby znaleźć tryb punktu sprzedaży.


## Konfiguracja POS


Aby skonfigurować POS, kliknij ikonę w lewym górnym rogu, a następnie kliknij Punkt sprzedaży > Ustawienia POS.


### Hasło menedżera


W ustawieniach POS można utworzyć hasło menedżera. Hasło menedżera uniemożliwia wysyłanie płatności wychodzących z aplikacji Breez bez autoryzacji. Personel sprzedaży będzie mógł otrzymywać płatności tylko z urządzenia. Pamiętaj, że jeśli korzystasz z tej opcji, możesz również chcieć uniemożliwić dostęp do kopii zapasowej Breez, więc w tym przypadku zaleca się korzystanie z zewnętrznego konta WebDav (np. Nextcloud).


### Lista przedmiotów


Lista przedmiotów to katalog przedmiotów na sprzedaż wraz z ich cenami. Istnieją dwa sposoby dodawania przedmiotów do listy:



- Aby wprowadzać pozycje pojedynczo, kliknij pozycję Pozycje w górnej części głównego widoku POS, a następnie znak "+" w prawym dolnym rogu. W tym miejscu można wprowadzić nazwę pojedynczego typu pozycji, cenę (wyświetlaną w wybranej walucie) i SKU (unikalny wewnętrzny identyfikator dla tego typu pozycji; jest on opcjonalny).
- Aby wprowadzić wiele pozycji jednocześnie, kliknij ikonę kalkulatora w lewym górnym rogu, a następnie Punkt sprzedaży > Preferencje > Ustawienia POS, a następnie kliknij trzy kropki po prawej stronie Listy pozycji, a następnie Importuj z CSV. Umożliwi to zaimportowanie przygotowanego wcześniej pliku CSV zawierającego nazwy, ceny i jednostki SKU produktów.


### Fiat Display


Breez wysyła i odbiera tylko Bitcoin, a w przypadku większości transakcji na Lightning, które zwykle dotyczą mniejszych kwot, suma jest zwykle wyświetlana w Satoshis, czyli Sats (1 BTC = 100 000 000 Sats). Jednak wielu sprzedawców uważa za praktyczne, aby móc zobaczyć (i poinformować klientów) wartość zakupu wyświetlaną w lokalnej walucie fiducjarnej.


W głównym widoku POS aktualnie wyświetlana waluta jest widoczna po prawej stronie (domyślnie SAT). Dostępna jest również rozwijana lista innych walut dostępnych do wyświetlenia. Aby dodać lub usunąć waluty z tej rozwijanej listy, kliknij na Point of Sale > Preferences > Fiat Currencies. Następnie po prostu zaznacz waluty, które chcesz mieć w rozwijanym menu i odznacz te, które chcesz pominąć.


Wyświetlane wartości pochodzą z yadio, szanowanego źródła danych o stawkach Exchange i są aktualizowane niemal w czasie rzeczywistym. Ale pamiętaj: niezależnie od tego, jaka wartość waluty jest aktualnie wyświetlana, sama płatność jest w Bitcoin.


### Opłata za zamówienie


Aby utworzyć zamówienie, dodaj pozycje z listy pozycji lub po prostu wprowadź sumę na klawiaturze. Następnie kliknij Charge w górnej części głównego widoku POS. Zobaczysz wtedy kod QR, który klient może zeskanować za pomocą aplikacji Lightning, który możesz udostępnić bezpośrednio z innej aplikacji na swoim urządzeniu lub który możesz skopiować i wkleić w razie potrzeby.


Po zeskanowaniu tego kodu lub kliknięciu udostępnionego/wklejonego Invoice, klient zobaczy Invoice w swojej aplikacji Lightning i będzie miał możliwość natychmiastowego opłacenia i rozliczenia transakcji.


Po wyświetleniu animacji "Płatność zatwierdzona!" w aplikacji Breez na urządzeniu sprzedawcy można kliknąć ikonę drukarki, aby wydrukować paragon generate dla klienta. Aby użyć drukarki paragonów w systemie Android, spróbuj użyć tego sterownika. Pamiętaj, że możesz również wydrukować poprzednie transakcje na ekranie Transakcje.


### Raport sprzedaży


Aby wyświetlić dzienny, tygodniowy i/lub miesięczny raport sprzedaży (do celów księgowych lub innych), kliknij ikonę w lewym górnym rogu, a następnie kliknij Transakcje. Kliknij ikonę raportu, aby wyświetlić raport i ikonę kalendarza, aby zmienić wybrany zakres dat.


### Eksportowanie transakcji


Aby wyświetlić listę płatności otrzymanych w Breez, kliknij ikonę w lewym górnym rogu, a następnie kliknij Transakcje. Kliknij trzy kropki w prawym górnym rogu, a następnie Eksportuj, aby wyeksportować listę płatności przychodzących w formacie CSV. Aby ograniczyć listę do określonego okresu czasu, kliknij ikonę kalendarza, aby ustawić zakres dat.


### Drukowanie paragonów


Aby wydrukować potwierdzenie sprzedaży, kliknij ikonę drukowania w prawym górnym rogu okna dialogowego potwierdzenia płatności. Alternatywnie, kliknij ikonę w lewym górnym rogu, a następnie kliknij Transakcje. Znajdź sprzedaż do wydrukowania, otwórz ją i kliknij prawą górną ikonę drukowania.


**Uwaga:** używaj tego sterownika do drukowania na przenośnej drukarce termicznej Bluetooth/USB 58 mm/80 mm.


## Chcę dowiedzieć się więcej



- Więcej informacji na temat Lightning and Breez można znaleźć na naszym [blogu](https://breez.technology/blog).
- Aby uzyskać więcej wskazówek technicznych dotyczących maksymalnego wykorzystania aplikacji i wykonywania typowych operacji, zapoznaj się z naszą [dokumentacją] (https://breez.technology/documentation).
- Jeśli utkniesz w martwym punkcie i nie możesz znaleźć odpowiedzi w naszej literaturze pomocy, możesz znaleźć nas na [Telegramie](https://t.me/breez_labs) lub wysłać nam [e-mail](mailto:support@breez.technology).
- Jeśli chcesz zobaczyć kilka filmów demonstracyjnych trybu Breez POS w akcji wykonanych przez naszych fanów i użytkowników, [tutaj](https://www.youtube.com/watch?v=xxxx) jest świetny krótki, a [tutaj](https://www.youtube.com/watch?v=xxxx) jest dłuższy, bardziej szczegółowy.