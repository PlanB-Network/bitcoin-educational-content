---
name: Divly
description: Łatwo obliczaj i deklaruj podatki od kryptowalut za pomocą Divly, w pełnej zgodności z przepisami podatkowymi.
---

![cover](assets/cover.webp)



## Wprowadzenie


Ten samouczek wyjaśnia, jak używać [Divly](https://divly.com/) do przygotowania raportu podatkowego Bitcoin (BTC). Przygotowanie raportu podatkowego obejmuje zebranie wszystkich istotnych transakcji BTC w roku obrotowym, obliczenie podlegających opodatkowaniu zysków lub dochodów oraz wyeksportowanie raportu, który można przesłać do lokalnego organu podatkowego.


W jurysdykcjach, w których Bitcoin podlega przepisom podatkowym, należy zgłaszać zyski lub straty ze zbycia BTC oraz dochód uzyskany w BTC. Korzystanie z oprogramowania do raportowania podatkowego pomaga uporządkować te informacje i skutecznie wygenerować raport podatkowy.


## Pierwsze kroki


Na początek:



- Utwórz konto Divly.
- Ustaw **kraj rezydencji podatkowej** i **walutę lokalną**.
- Upewnij się, że ustawienia te odzwierciedlają jurysdykcję, w której raportowane są podatki.


Divly wykorzystuje tę konfigurację do zastosowania odpowiednich reguł podatkowych i konwersji walut podczas generowania raportu.


![img](assets/en/01.webp)


## Krok 1 - Zaimportuj wszystkie transakcje Bitcoin z wallet i wymiany


Wszystkie transakcje Bitcoin za dany rok podatkowy muszą zostać zaimportowane przed dokonaniem jakichkolwiek obliczeń podatkowych.


Divly obsługuje wiele metod importu:



- Połączenia API lub OAuth** dla giełd lub usług, które je obsługują
- Przesyłanie plików CSV** z wallet lub giełd
- Ręczne wprowadzanie** dla wszelkich transakcji nieobjętych metodami automatycznymi


Upewnij się, że zaimportowałeś **każdy wpływ i wypływ BTC** odpowiedni dla raportowanego okresu podatkowego.


![img](assets/en/02.webp)


## Krok 2 - Przegląd zaimportowanych transakcji


**Potwierdź saldo kryptowalut:**


Najlepiej zacząć od sprawdzenia, czy całkowita liczba posiadanych kryptowalut zgadza się z liczbą wyświetlaną w Divly. Divly oblicza stan posiadania, sumując wszystkie zaimportowane transakcje.


Aby to zrobić, zacznij od przejścia do strony Przegląd. Sprawdź, czy każda wymieniona kryptowaluta jest rzeczywiście liczbą, którą posiadasz. Divly nie wyświetla walut fiducjarnych w przeglądzie, więc zignoruj je w tym ćwiczeniu.


Możesz filtrować według wallet, jeśli znajdziesz jakieś problemy. Pomaga to zrozumieć, które wallet mogą być niezsynchronizowane.


![img](assets/en/03.webp)


Po zaimportowaniu:



- Przejdź do sekcji **Transakcje**.
- Sprawdź, czy każda transakcja zawiera prawidłowe daty i kwoty.
- W razie potrzeby usuwanie ostrzeżeń o brakującej cenie lub podstawie kosztowej.


**Ważne: ** Upewnij się, że zaimportowałeś **WSZYSTKIE** swoje transakcje kryptowalutowe do Divly przed przejściem do następnego kroku. W tym zimne wallet! W przeciwnym razie istnieje ryzyko, że podatki nie będą prawidłowe.


![img](assets/en/04.webp)


## Krok 3 - Kategoryzacja odpowiednich wpłat i wypłat


Różne rodzaje transakcji kryptowalutowych mogą mieć różne konsekwencje podatkowe. Obejmują one takie działania, jak podarowanie kryptowaluty, utracone aktywa, nagrody mining, fork, zrzuty i podobne zdarzenia. Ważne jest, aby wszystkie transakcje były dokładnie skategoryzowane.


W większości przypadków Divly automatycznie przypisuje prawidłowe etykiety. Jeśli jednak dostępne dane transakcji są niewystarczające, automatyczna klasyfikacja może nie być możliwa. W takich sytuacjach użytkownik jest odpowiedzialny za ręczne przypisanie odpowiedniej etykiety. Aby zrozumieć znaczenie i traktowanie podatkowe każdej etykiety, należy zapoznać się z powiązanym artykułem pomocy.


Aby oznaczyć transakcje, przejdź do strony Transakcje. Wybierz jedną lub więcej transakcji i wybierz odpowiednią etykietę z menu rozwijanego w górnej części strony.


![img](assets/en/05.webp)


## Krok 4 - Generowanie raportu podatkowego


Po zaimportowaniu i sklasyfikowaniu transakcji:



- Przejdź do sekcji **Raport podatkowy**.
- Wybierz odpowiedni **rok podatkowy**.
- Przejrzyj podsumowanie obliczonych zysków, strat i kategorii dochodów.


Podsumowanie agreguje zdarzenia podlegające opodatkowaniu na podstawie zaimportowanych danych i klasyfikacji.


Interfejs raportu podatkowego Divly pozwala potwierdzić, że wszystkie transakcje zostały zarejestrowane przed eksportem.


![img](assets/en/06.webp)


## Krok 5 - Eksport raportu


Po przeglądzie:



- Wyeksportuj sfinalizowany raport podatkowy BTC w formacie dostępnym dla danego kraju.
- Zapisz wyeksportowany plik lub wydrukuj go w celu przesłania do organu podatkowego.


![img](assets/en/07.webp)


W zależności od jurysdykcji może być konieczne przestrzeganie określonych instrukcji przesyłania lub korzystanie z formularzy specyficznych dla danego kraju z wyeksportowanymi danymi. [Przewodniki Divly dla poszczególnych krajów](https://divly.com/en/guides) mogą w razie potrzeby pomóc w krokach związanych z przesyłaniem danych.