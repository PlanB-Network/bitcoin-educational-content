---
name: COLDCARD Mk4
description: Przewodnik konfiguracji i użytkowania COLDCARD Mk4 z Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Hardware wallets** to fizyczne urządzenia stworzone wyłącznie do bezpiecznego przechowywania klucza prywatnego Bitcoin. Przechowują one klucze prywatne w trybie offline, co oznacza, że hakerzy nie mogą uzyskać do nich dostępu przez Internet. Podczas gdy **software wallet** są używane głównie do codziennych transakcji, **hardware wallet** są często używane do bezpiecznego przechowywania większych ilości bitcoinów przez długi czas. Podczas dokonywania transakcji Bitcoin przy użyciu **hardware wallets**, wallet może podpisywać transakcje wewnątrz urządzenia, więc klucz prywatny nigdy nie jest narażony na działanie środowisk połączonych z Internetem.


W tym samouczku zbadamy jeden z najpopularniejszych sprzętowych wallet produkowanych przez Coinkite, Coldcard Mk4. Przyjrzymy się, jak skonfigurować i używać tego sprzętowego wallet do wykonywania transakcji Bitcoin.


## Przegląd Coldcard Mk4


Coldcard Mk4 jest sprzętem Bitcoin-only wallet wyprodukowanym przez Coinkite. Urządzenie to jest wyposażone w ekran, klawiaturę numeryczną i przesuwaną pokrywę ochronną. Ponadto urządzenie oferuje kilka sposobów łączenia się i interakcji, w tym USB-C, pracę w trybie air-gapped przy użyciu karty MicroSD, NFC i tryb wirtualnego dysku. Mk4 zawiera również zaawansowane funkcje bezpieczeństwa, takie jak BIP39 passphrase i trick PIN, dając użytkownikom większą kontrolę i ochronę nad Bitcoin.


## Konfiguracja początkowa: PIN i słowa antyphishingowe


Aby rozpocząć, Coldcard Mk4 można kupić bezpośrednio na stronie [Coinkite's website] (https://store.coinkite.com/store). Kupujący mogą również wybrać płatność za pomocą waluty fiducjarnej lub Bitcoin. Ponadto potrzebna będzie również karta MicroSD (wystarczy 4 GB) i źródło zasilania, które można podłączyć za pomocą kabla USB-C (Coldcard Mk4 ma tylko port wejściowy zasilania USB-C). Należy pamiętać, że ponieważ Mk4 nie ma wbudowanej baterii, musi być podłączony do źródła zasilania przez cały czas użytkowania.


Urządzenie Mk4 zostanie dostarczone w torbie zabezpieczonej przed manipulacją. Upewnij się, że torba nie została naruszona. Jeśli zauważysz coś, co może stanowić problem, np. uszkodzenie lub rozdarcie torby, możesz poinformować Coinkite, wysyłając wiadomość e-mail na adres support@coinkite.com. Ponadto na torbie z zabezpieczeniem przed manipulacją można znaleźć 12-cyfrowy numer, który będziemy nazywać numerem torby Mk4. Numer ten zostanie później wykorzystany do sprawdzenia, czy urządzenie nie zostało naruszone podczas wysyłki i czy pochodzi bezpośrednio od Coinkite. Numer torby jest bezpiecznie przechowywany w Coldcard secure element przy użyciu pamięci flash OTP (One-Time-Programmable), co oznacza, że nie można go zmienić po zaprogramowaniu. Po włączeniu urządzenia po raz pierwszy numer wyświetlany na ekranie musi być zgodny z numerem na torbie. Gwarantuje to, że otrzymany Mk4 jest oryginalnym urządzeniem z fabryki i nie został wymieniony ani zmodyfikowany. Chociaż ta weryfikacja potwierdza integralność urządzenia tylko w momencie pierwszego włączenia, secure element nadal chroni klucze prywatne, kod PIN i passphrase, dzięki czemu niezwykle trudno jest naruszyć Bitcoin w przypadku jakiejkolwiek manipulacji. Ponadto dobre praktyki, takie jak prawidłowe zabezpieczenie danych związanych z wallet, będą korzystne dla ogólnego bezpieczeństwa samej karty Cold. Więcej informacji można znaleźć w tym [artykule] (https://blog.coinkite.com/understanding-mk4-security-model/), który omawia model bezpieczeństwa karty Coldcard.


Klawiatura składa się z 10 przycisków numerycznych, przycisku OK (`✓`) i przycisku anulowania (`✕`). Niektóre przyciski numeryczne mogą być również używane do nawigacji: `5` do nawigacji w górę (`^`), `7` do nawigacji w lewo (`<`), `8` do nawigacji w dół (`˅`) i `9` do nawigacji w prawo (`>`).


![01](assets/en/01.webp)


Jeśli nie ma żadnych problemów z opakowaniem, można je otworzyć. Mk4 będzie dostarczany z kartą zapasową wallet, która może być używana do przechowywania informacji dotyczących kodu PIN urządzenia, słów antyphishingowych i seedphrase. Wykonaj następujące kroki, aby zainicjować urządzenie:


1. Przygotuj kartkę papieru i długopis.

2. Podłącz Mk4 do źródła zasilania (kabel USB-C) i włóż kartę MicroSD.

3. Po pierwszym włączeniu urządzenia na ekranie zostanie wyświetlony komunikat dotyczący Warunków sprzedaży i użytkowania Coldcard. Przejdź w dół, a następnie naciśnij `✓`, aby kontynuować.

4. Następnie na ekranie zostanie wyświetlony 12-cyfrowy numer. Sprawdź ten numer z numerem na torbie zabezpieczonej przed manipulacją i dodatkową kopią numeru torby, która została dołączona do torby zabezpieczonej przed manipulacją, aby upewnić się, że urządzenie nie zostało naruszone. Jeśli numery się nie zgadzają, należy natychmiast skontaktować się z pomocą techniczną Coinkite. W przeciwnym razie naciśnij `✓`, aby kontynuować.


![02](assets/en/02.webp)


5. Wybierz `Wybierz kod PIN`.

6. Przejdź w dół podczas czytania instrukcji, aby przejść do następnego kroku.


![03](assets/en/03.webp)


7. Na Mk4 utwórz i wprowadź prefiks PIN (musi mieć od 2 do 6 znaków) i zapisz go, a następnie naciśnij `✓`, aby kontynuować.

8. Zapisz dwa słowa wyświetlane na ekranie. Są to słowa antyphishingowe. Naciśnij `✓`, aby kontynuować.


![04](assets/en/04.webp)


9. Utwórz i wprowadź sufiks kodu PIN (lub pozostałą część kodu PIN, musi mieć długość od 2 do 6 znaków) i zapisz go. Naciśnij `✓`, aby kontynuować.

10. Wprowadź ponownie prefiks PIN. Naciśnij `✓`, aby kontynuować.


![05](assets/en/05.webp)


11. Sprawdź, czy słowa antyphishingowe są takie same jak te wpisane w kroku 8. Naciśnij `✓`, aby kontynuować.

12. Wprowadź ponownie sufiks kodu PIN (lub pozostałą część kodu PIN). Naciśnij `✓`, aby kontynuować.


![06](assets/en/06.webp)


13. Kod PIN Mk4 i słowa antyphishingowe zostały pomyślnie utworzone i zapisane przez urządzenie.


![07](assets/en/07.webp)


Należy pamiętać, że Mk4 zawsze poprosi o wprowadzenie kodu PIN przy każdym włączeniu urządzenia. Bez tego kodu PIN nie można uzyskać dostępu do Coldcard Mk4. Upewnij się więc, że utworzyłeś wystarczającą kopię zapasową kodu PIN i słów antyphishingowych.


## Konfiguracja Wallet


Następnym krokiem jest skonfigurowanie wallet. Można to zrobić na trzy sposoby:


- Tworzenie nowego wallet (standard)
- Tworzenie nowego wallet za pomocą rzutów kośćmi
- Importowanie wallet


### Tworzenie nowego wallet (standard)


Aby utworzyć nowy wallet, wystarczy wykonać następujące czynności.


1. Wybierz `New Wallet` (lub `New Seed Words`) > Wybierz `12 Word` lub `24 Word (domyślnie)` w zależności od preferencji.


![08](assets/en/08.webp)


2. Urządzenie wygeneruje 12 lub 24 słowa jako seedphrase w zależności od wyboru. Nawiguj w dół, starannie zapisując każde słowo we właściwej kolejności. Następnie naciśnij przycisk `✓`, aby kontynuować.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Urządzenie poprosi o zweryfikowanie seedphrase, zadając pytania w losowej kolejności (na przykład `Słowo 1 to?`, następnie `Słowo 5 to?`, następnie `Słowo 12 to?` itd. Odnieś się do notatki z kroku 2 i wybierz słowa poprawnie (naciskając `1`, `2` lub `3`, w zależności od tego, co odpowiada poprawnemu słowu), aby ukończyć tworzenie wallet.


![09](assets/en/09.webp)


4. Mk4 zapyta, czy chcesz włączyć NFC/Tap, czy nie. Na razie wybierz `✕` dla tej opcji. Można to zmienić w ustawieniach w przyszłości.

5. Wreszcie, Mk4 pozwoli również wyłączyć port USB (który może być używany do przesyłania danych bez ochrony przed dostępem powietrza). Na razie wybierz `✓` dla tej opcji. Można to zmienić w ustawieniach w przyszłości.

6. Na ekranie zostanie wyświetlone menu główne z napisem "Gotowy do podpisania" u góry. Oznacza to zakończenie procesu tworzenia wallet.


![10](assets/en/10.webp)


### Tworzenie nowego wallet z rzutem kostką


Alternatywnie, możesz także wygenerować nowy seedphrase za pomocą entropii. Zrób to, jeśli nie ufasz świeżo wygenerowanemu seedphrase z Mk4.


Procedura dla Coldcard Mk4 jest następująca:


1. Wybierz `New Wallet` (lub `New Seed Words`) > Wybierz `12 Word Dice Roll` lub `24 Word Dice Roll` w zależności od preferencji.

2. Zostaniesz poproszony o wprowadzenie wyników rzutów kośćmi. Każdy rzut kostką dodaje losowości do procesu tworzenia wallet, zapewniając, że twój seedphrase jest generowany w całkowicie bezpieczny i nieprzewidywalny sposób. Minimalna liczba rzutów to 50 dla 12-wyrazowego seedphrase i 99 dla 24-wyrazowego seedphrase. Naciśnij `✓` po wprowadzeniu co najmniej 99 wartości rzutów kośćmi.


![11](assets/en/11.webp)


3. Urządzenie wygeneruje 12 lub 24 słowa jako seedphrase w zależności od dokonanego wyboru. Nawiguj w dół, starannie zapisując każde słowo we właściwej kolejności. Następnie naciśnij przycisk `✓`, aby kontynuować.

4. Urządzenie poprosi o zweryfikowanie seedphrase, zadając pytania w losowej kolejności (na przykład `Słowo 1 to?`, następnie `Słowo 5 to?`, następnie `Słowo 12 to?` itd. Odnieś się do notatki z kroku 3 i wybierz słowa poprawnie (naciskając `1`, `2` lub `3`, w zależności od tego, które odpowiada poprawnemu słowu), aby ukończyć tworzenie wallet.


![12](assets/en/12.webp)


5. Mk4 zapyta, czy chcesz włączyć NFC/Tap, czy nie. Na razie wybierz `✕` dla tej opcji. Można to zmienić w ustawieniach w przyszłości.

6. Wreszcie, Mk4 pozwoli również wyłączyć port USB (który może być używany do przesyłania danych bez ochrony przed dostępem powietrza). Na razie wybierz `✓` dla tej opcji. Można to zmienić w ustawieniach w przyszłości.

7. Na ekranie zostanie wyświetlone menu główne z napisem "Gotowy do podpisania" u góry. Oznacza to zakończenie procesu tworzenia wallet.


![13](assets/en/13.webp)


### Importowanie wallet


Ostatnią opcją jest zaimportowanie wallet. Możesz to zrobić, jeśli chcesz odzyskać wallet z seedphrase, który już posiadasz. Możesz wykonać następujące kroki:


1. Wybierz `Importuj istniejące`.

2. Wybierz `24 słowa`, `18 słów` lub `12 słów`, w zależności od liczby słów seedphrase.


![14](assets/en/14.webp)


3. Coldcard Mk4 zapyta, jakie jest każde słowo w kolejności. Dla każdego słowa nawiguj w dół lub w górę, aż znajdziesz prefiks zapisu dla każdego słowa. Urządzenie będzie zawężać możliwości do momentu znalezienia prawidłowego słowa. W ten sam sposób postępuj z pozostałymi słowami.

4. W przypadku ostatniego słowa Coldcard Mk4 wyświetli tylko ograniczoną liczbę możliwych słów. Brak pasujących słów może oznaczać, że zostały one wprowadzone nieprawidłowo. W przeciwnym razie wybierz słowo pasujące do słowa na karcie seedphrase.


![15](assets/en/15.webp)


5. Mk4 zapyta, czy chcesz włączyć NFC/Tap, czy nie. Na razie wybierz `✕` dla tej opcji. Można to zmienić w ustawieniach w przyszłości.

6. Wreszcie, Mk4 pozwoli również wyłączyć port USB (który może być używany do przesyłania danych bez ochrony przed dostępem powietrza). Na razie wybierz `✓` dla tej opcji. Można to zmienić w ustawieniach w przyszłości.

7. Na ekranie zostanie wyświetlone menu główne z napisem "Gotowy do podpisania" u góry. Oznacza to zakończenie procesu tworzenia wallet.


![16](assets/en/16.webp)


Należy pamiętać, że seedphrase to jedyny dostęp do odzyskania wallet. Utwórz kopię zapasową seedphrase i przechowuj ją w bezpiecznym miejscu. **Nie twoje klucze, nie twoje monety**, ktokolwiek ma twój seedphrase ma dostęp do twoich bitcoinów!


## Konfiguracja passphrase


Jedną z najlepszych praktyk w Bitcoin jest użycie passphrase. passphrase działa jako 13. lub 25. słowo oprócz seedphrase. Różnica polega na tym, że możesz wybrać dowolną frazę, podczas gdy seedphrase jest wybierany z wcześniej określonej listy 2048 słów. Domyślnie, po skonfigurowaniu wallet, zaczniesz od wallet z pustym passphrase. Aby skonfigurować niepusty passphrase, wystarczy wykonać następujące czynności:


1. Przejdź do `Passphrase`.

2. Przejdź w dół, aby przeczytać opis passphrase, a następnie naciśnij `✓`, aby kontynuować.

3. Wybierz `Edit Phrase`.


![17](assets/en/17.webp)


4. Wprowadź swój passphrase:


   - Naciśnij `1` (litery), `2` (cyfry) lub `3` (symbole), aby wybrać typ znaku.
   - Naciśnij `4`, aby przełączać między małymi i wielkimi literami (można używać tylko podczas wprowadzania liter).
   - Nawiguj za pomocą `^` lub `˅`, aby wybrać znak dla passphrase.
   - Nawiguj za pomocą `<` lub `>`, aby przechodzić między znakami. Możesz także użyć `>`, aby dodać spacje.
   - Naciśnij `✕`, aby usunąć znaki.
   - Naciśnij `✓` po zakończeniu edycji passphrase.

5. Dodatkowo, pozostałe opcje posiadają następujące funkcje:


   - Opcje `Add Word` lub `Add Numbers` mogą być używane do dodawania liter/liczb do aktualnie edytowanego passphrase.
   - Naciśnij `Clear ALL`, aby zresetować aktualnie edytowany passphrase.
   - Naciśnij `CANCEL`, aby powrócić do menu głównego.

6. Zapisz swój passphrase jako kopię zapasową.

7. Naciśnij `APPLY`, aby uzyskać dostęp do wallet za pomocą właśnie ustawionego passphrase.

8. Mk4 wyświetli wtedy 8-znakowy odcisk palca klucza głównego. Można go traktować jako "identyfikator" wallet. Zapisz ten odcisk palca i naciśnij `✓`, aby kontynuować.


![18](assets/en/18.webp)


9. Teraz wallet wyświetli menu główne wallet z wprowadzonym passphrase.

10. Ważne jest, aby pamiętać, że wallet nie powie ci, że wprowadziłeś nieprawidłowy passphrase, ponieważ każdy passphrase odpowiada każdemu własnemu wallet z unikalną tożsamością (odcisk palca klucza głównego). Dlatego dobrą praktyką jest ponowne wprowadzenie tego samego passphrase i sprawdzenie, czy generuje on ten sam odcisk palca wallet, upewniając się, że został wprowadzony poprawnie. W tym celu należy wykonać kroki od 11 do 14.

11. W menu głównym wybierz `Restore Master`, a następnie naciśnij `✓`. Jesteś teraz z powrotem w menu głównym wallet z pustym passphrase.


![19](assets/en/19.webp)


12. Przejdź ponownie do `Passphrase`, a następnie naciśnij `✓`, aby kontynuować.

13. Wprowadź ponownie numer passphrase, który zapisałeś w kroku 6, a następnie naciśnij przycisk `APPLY`.

14. Sprawdź 8-znakowy odcisk palca klucza głównego pod kątem zgodności z odciskiem zapisanym w kroku 8. Jeśli oba odciski palców nie pasują do siebie, mogło dojść do wpisania błędnych znaków. Zamiast tego możesz wybrać nowy passphrase i powtórzyć proces od kroku 1. Jeśli jednak oba odciski palców są zgodne, oznacza to, że urządzenie passphrase zostało wprowadzone prawidłowo.

15. wallet z wybranym passphrase jest gotowy do użycia.


## Eksportowanie Wallet do Sparrow


Podobnie jak inne sprzętowe wallet, Coldcard Mk4 nie może być używany samodzielnie. Musi być połączona z oprogramowaniem wallet, które działa jako interfejs. Oprogramowanie wallet umożliwia przeglądanie salda, tworzenie transakcji i zarządzanie adresami, podczas gdy Coldcard bezpiecznie podpisuje te transakcje bez ujawniania kluczy prywatnych.


W tym samouczku użyjemy Sparrow Wallet jako interfejsu. Procedura eksportu wallet jest następująca:


1. Upewnij się, że do Mk4 włożona jest karta MicroSD.

2. Wykonaj czynności opisane w sekcji "Konfigurowanie passphrase" na wallet z passphrase, który chcesz wyeksportować. Jeśli chcesz wyeksportować wallet z pustym passphrase, możesz pominąć ten krok.

3. Przejdź do `Advanced/Tools` > Wybierz `Export Wallet` > Wybierz `Generic JSON` > Przewiń w dół, czytając instrukcje, a następnie naciśnij `✓`.


![20](assets/en/20.webp)


4. Mk4 utworzył teraz plik w formacie `.json` na karcie MicroSD.


![21](assets/en/21.webp)


5. Wyjmij kartę MicroSD z karty Cold i włóż ją do urządzenia, w którym zainstalowany jest Sparrow Wallet.

6. Otwórz Sparrow Wallet.

7. Kliknij na `File`


![22](assets/en/22.webp)


Następnie kliknij `Nowy Wallet`


![23](assets/en/23.webp)


Następnie wprowadź nazwę dla wallet


![24](assets/en/24.webp)


Następnie kliknij przycisk "Utwórz Wallet"


![25](assets/en/25.webp)


8. Wybierz `Typ skryptu`.


![26](assets/en/26.webp)


9. W sekcji Magazyn kluczy wybierz `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Poszukaj Coldcard i kliknij `Import File...`.


![28](assets/en/28.webp)


11. Wybierz plik utworzony w kroku 4 (ten w formacie `.json`).


![29](assets/en/29.webp)


12. Na Mk4 wróć do menu głównego i przejdź do `Advanced/Tools` > `View Identity`. Upewnij się, że odcisk palca wyświetlany na ekranie Mk4 jest zgodny z tym na Sparrow Wallet (główny odcisk palca w sekcji Keystore)

13. Kliknij przycisk "Zastosuj" w prawym dolnym rogu.


![30](assets/en/30.webp)


14. Opcjonalnie można również dodać hasło dla wyeksportowanego wallet. Hasło to jest wymagane przy każdym otwarciu aplikacji Sparrow Wallet w celu uzyskania dostępu do wallet. Jeśli w przyszłości zapomnisz hasła, możesz po prostu powtórzyć kroki 1-13 i wybrać nowe hasło.


![31](assets/en/31.webp)


15. wallet został pomyślnie wyeksportowany i jest gotowy do użycia.


![32](assets/en/32.webp)


## Otrzymywanie bitcoinów


Następnie dowiemy się, jak odbierać Bitcoin za pomocą Mk4. Proces ten jest dość prosty, ponieważ nie trzeba używać samego urządzenia Mk4. Jeśli już wyeksportowałeś wallet do Sparrow, możesz odbierać Bitcoin bezpośrednio przez Sparrow Wallet. Wykonaj poniższe kroki, aby otrzymywać bitcoiny za pomocą Mk4:


1. Otwórz Sparrow Wallet.

2. Wybierz `Open Wallet` > Wybierz plik wallet, do którego chcesz otrzymywać bitcoiny > Wprowadź hasło powiązane z tym wallet.


![33](assets/en/33.webp)


3. W interfejsie Sparrow kliknij zakładkę `Receive` po lewej stronie interfejsu.


![34](assets/en/34.webp)


4. Na górze pojawi się adres wraz z kodem QR. Możesz skopiować i wkleić adres lub zeskanować kod QR za pomocą wallet, którego będziesz używać do wysyłania bitcoinów do Sparrow Wallet. Opcjonalnie możesz wpisać etykietę dla otrzymanych bitcoinów.


![35](assets/en/35.webp)


5. Po wysłaniu bitcoinów, w interfejsie Sparrow kliknij zakładkę "Transakcje" po lewej stronie interfejsu. W górnej części historii transakcji pojawi się nowy wpis, który odpowiada właśnie dokonanej transakcji.


![36](assets/en/36.webp)


6. Możesz także przejść do zakładki `UTXOs` po lewej stronie interfejsu, aby zobaczyć bitcoiny, które właśnie otrzymałeś.


![37](assets/en/37.webp)


## Wysyłanie bitcoinów


W przeciwieństwie do otrzymywania bitcoinów, wydawanie bitcoinów powiązanych z kartą Cold wymaga użycia karty Cold do podpisywania transakcji. Procedura wysyłania bitcoinów za pomocą Mk4 jest następująca:


1. Włóż kartę MicroSD do urządzenia, w którym zainstalowany jest Sparrow Wallet.

2. Otwórz Sparrow Wallet.

3. Wybierz `Open Wallet` > Wybierz plik wallet, którego chcesz użyć do wysyłania bitcoinów > Wprowadź hasło powiązane z tym wallet.


![38](assets/en/38.webp)


4. W interfejsie Sparrow kliknij zakładkę `Send` po lewej stronie interfejsu.


![39](assets/en/39.webp)


5. W zakładce `Pay to` wprowadź adres, na który chcesz wysłać bitcoiny.

6. Dodaj etykietę dla transakcji.

7. Wprowadź kwotę bitcoinów, którą chcesz wysłać.

8. Wprowadź opłatę, przełączając `Zakres` lub bezpośrednio wprowadź liczbę w części `Opłata`.


![40](assets/en/40.webp)


9. W prawym dolnym rogu kliknij "Utwórz transakcję".


![41](assets/en/41.webp)


10. Zostaniesz przeniesiony do nowej karty transakcji, której nazwa jest etykietą wprowadzoną w kroku 6. Kliknij `Finalizuj transakcję do podpisania`.


![42](assets/en/42.webp)


11. Kliknij `Zapisz transakcję` i zapisz transakcję na karcie MicroSD. W razie potrzeby zmień nazwę pliku. Ten krok spowoduje zapisanie transakcji jako pliku PSBT.


![43](assets/en/43.webp)


12. Wyjmij kartę MicroSD i włóż ją do Coldcard Mk4.

13. Włącz Mk4, podłączając go do źródła zasilania.

14. Wprowadź kod PIN.

15. Przejdź do `Passphrase` i wprowadź passphrase z wallet, którego chcesz użyć do wysłania bitcoinów. Jeśli chcesz użyć wallet z pustym passphrase, pomiń ten krok.

16. Upewnij się, że odcisk palca klucza głównego jest taki sam jak odcisk palca na Sparrow Wallet. Można to sprawdzić w zakładce "Ustawienia" Sparrow Wallet po lewej stronie interfejsu. Następnie naciśnij `✓` na Mk4, aby kontynuować. Spowoduje to przejście do menu głównego.

17. W menu głównym Mk4 wybierz `Gotowy do podpisania`. Na ekranie pojawi się komunikat `OKAY TO SEND?`. Upewnij się, że ilość bitcoinów, które chcesz wysłać i adres odbiorczy są prawidłowe. Naciśnij `✓`, aby potwierdzić lub `✕`, aby anulować.

18. Jeśli do wyboru jest wiele plików PSBT, Mk4 wyświetli komunikat "Wybierz plik PSBT do podpisania". Naciśnij `✓`, aby kontynuować. Następnie wybierz plik PSBT, który chcesz podpisać, nawigując w dół lub w górę. Wykonaj krok 17 dla tej transakcji.


![44](assets/en/44.webp)


19. Mk4 wyświetli teraz komunikat `PSBT Signed` wraz z nazwą pliku podpisanego PSBT. Naciśnij `✓`, aby kontynuować.

20. Wyjmij kartę MicroSD z karty Cold i włóż ją do urządzenia, w którym zainstalowano kartę Sparrow Wallet.

21. W Sparrow Wallet kliknij `Load Transaction` (Załaduj transakcję).


![45](assets/en/45.webp)


22. Wybierz plik o tej samej nazwie, co plik utworzony w kroku 19.


![46](assets/en/46.webp)


23. Kliknij `Broadcast Transaction`.


![47](assets/en/47.webp)


24. Twoja transakcja została nadana i jest obecnie przetwarzana. Możesz przejść do zakładki `Transakcje`, aby zobaczyć status potwierdzenia transakcji.


![48](assets/en/48.webp)


## Aktualizacja oprogramowania sprzętowego


### Sprawdzanie wersji oprogramowania sprzętowego


Oprogramowanie sprzętowe Coldcard Mk4 można zawsze zaktualizować do nowszej wersji. Aby sprawdzić, czy karta Mk4 została zaktualizowana do najnowszej wersji, należy wykonać następujące czynności:

1. Włącz Mk4, podłączając go do źródła zasilania.

2. Wprowadź kod PIN.

3. Przejdź do `Zaawansowane/Narzędzia` > Wybierz `Upgrade Firmware` > Wybierz `Pokaż wersję`.


![49](assets/en/49.webp)


Sprawdź wersję wyświetlaną na ekranie Mk4 z wersją na stronie [Coinkite's website](https://coldcard.com/downloads). Jeśli wersja jest inna, możesz zaktualizować oprogramowanie układowe do nowszej wersji.


![50](assets/en/50.webp)


### Aktualizacja oprogramowania sprzętowego


Jeśli chcesz zaktualizować oprogramowanie sprzętowe do najnowszej wersji, wykonaj następujące czynności:


1. Włóż kartę MicroSD do laptopa/komputera PC.

2. Wejdź na stronę [Coinkite's website] (https://coldcard.com/downloads) i pobierz najnowsze oprogramowanie na kartę MicroSD (czerwony przycisk po prawej stronie obrazu Mk4 z numerem wersji).


![51](assets/en/51.webp)


Możesz również pobrać inne wersje, klikając `All Files on Mk4` i wybierając wersję, którą chcesz pobrać. Pobrany plik będzie w formacie `.dfu`.


![52](assets/en/52.webp)


3. Wyjmij kartę MicroSD i włóż ją do Mk4.

4. Włącz Mk4, podłączając go do źródła zasilania.

5. Wprowadź kod PIN.

6. Przejdź do `Advanced/Tools` > Wybierz `Upgrade Firmware` > Wybierz `From MicroSD` > Przewiń w dół, czytając instrukcje, a następnie naciśnij `✓`.


![53](assets/en/53.webp)


7. Wybierz plik `.dfu` pobrany w kroku 2.

8. Coldcard Mk4 wyświetli komunikat `Install this new firmware? Przewiń w dół, czytając instrukcje, a następnie naciśnij `✓`.


![54](assets/en/54.webp)


9. Poczekaj, aż Mk4 zakończy instalację nowego oprogramowania sprzętowego. Nie odłączaj źródła zasilania podczas instalacji.

10. Po zakończeniu Mk4 uruchomi się ponownie. Możesz wprowadzić kod PIN i wykonać kroki "Sprawdzanie wersji oprogramowania sprzętowego", aby sprawdzić, czy oprogramowanie sprzętowe zostało zaktualizowane, czy nie.


## Funkcje zaawansowane


### Zmiana kodu PIN


Jeśli chcesz zmienić kod PIN logowania, wykonaj następujące czynności:


1. Przygotuj długopis i kartkę papieru.

2. Włącz Mk4, podłączając go do źródła zasilania.

3. Wprowadź kod PIN.

4. Przejdź do `Ustawienia` > wybierz `Ustawienia logowania` > wybierz `Zmień główny PIN`

5. Przejdź w dół podczas czytania wiadomości, a następnie naciśnij `✓`, aby kontynuować.


![55](assets/en/55.webp)


6. Wprowadź stary kod PIN.

7. Wprowadź nowy prefiks PIN (musi mieć od 2 do 6 znaków) i zapisz go.

8. Mk4 wyświetli teraz dwa nowe słowa antyphishingowe, zapisz je, a następnie naciśnij `✓`, aby kontynuować.

9. Wprowadź nowy sufiks kodu PIN (lub pozostałą część kodu PIN, o długości od 2 do 6 znaków) i zapisz go.


![56](assets/en/56.webp)


10. Wprowadź ponownie nowy prefiks PIN.

11. Sprawdź, czy słowa antyphishingowe pasują do tych, które napisałeś w kroku 8.

12. Wprowadź ponownie nowy sufiks kodu PIN (lub pozostałą część kodu PIN).


![57](assets/en/57.webp)


13. Kod PIN został pomyślnie zmieniony.


### PINy do sztuczek - Dodaj nową sztuczkę


Trick PIN to alternatywny kod PIN, różniący się od kodu użytego do skonfigurowania karty Coldcard Mk4 po raz pierwszy. Po włączeniu urządzenia Mk4 można wprowadzić sztuczny kod PIN zamiast głównego kodu PIN, aby uruchomić określone działania. Aby skonfigurować sztuczny kod PIN w Mk4, można wykonać następujące czynności:


1. Przygotuj długopis i kartkę papieru.

2. Włącz Mk4, podłączając go do źródła zasilania.

3. Wprowadź kod PIN.

4. Przejdź do `Ustawienia` > wybierz `Ustawienia logowania` > wybierz `Piny sztuczek` > wybierz `Dodaj nową sztuczkę`.


![58](assets/en/58.webp)


5. Wprowadź prefiks kodu PIN (musi mieć od 2 do 6 znaków) i zapisz go.

6. Mk4 wyświetli teraz dwa nowe słowa antyphishingowe, zapisz je, a następnie naciśnij `✓`, aby kontynuować.

7. Wprowadź sufiks kodu PIN (lub resztę kodu PIN, musi mieć od 2 do 6 znaków) i zapisz go.


![59](assets/en/59.webp)


8. Przejdź w dół lub w górę, aby wybrać akcję, którą chcesz sparować z utworzonym właśnie kodem PIN. Lista działań obejmuje:


    - po wybraniu opcji `Brick Self` chipy Mk4 zostaną zniszczone po wprowadzeniu kodu PIN, dzięki czemu Mk4 będzie trwale bezużyteczny.
    - `Wipe Seed`, możesz wybrać pomiędzy następującymi działaniami:
      - `Wipe & Reboot`: seed zostanie wyczyszczony, a karta Cold uruchomi się ponownie po wprowadzeniu kodu PIN.
      - `Silent Wipe`: seed jest wymazywany po cichu, jednak karta Cold będzie działać tak, jakby PIN został wprowadzony nieprawidłowo.
      - `Wipe -> Wallet`: seed jest wymazywany po cichu, a karta Cold przeniesie cię do wallet pod przymusem.
    - "Przymus Wallet", po wybraniu, Mk4 doprowadzi do przymusu wallet po wprowadzeniu kodu PIN.
    - `Login Countdown`, możesz wybrać pomiędzy następującymi działaniami:
      - `Wipe & Countdown`: seed zostanie natychmiast wyczyszczony, a następnie Mk4 zacznie wyświetlać odliczanie.
      - `Odliczanie i cegła`: Rozpoczyna się odliczanie, a Mk4 zamuruje się po upływie czasu.
      - `Just Countdown`: Mk4 rozpocznie odliczanie i zrestartuje się po upływie czasu.
    - po wybraniu opcji `Look Blank`, po wprowadzeniu kodu PIN, karta Cold zachowuje się tak, jakby seedphrase została wyczyszczona, ale w rzeczywistości nadal znajduje się w pamięci.
    - po wybraniu tej opcji Coldcard uruchomi się ponownie po wprowadzeniu kodu PIN.
    - "Tryb Delta", ta zaawansowana funkcja jest przeznaczona dla doświadczonych użytkowników i ma na celu ochronę przed poważnymi zagrożeniami, takimi jak wymuszenie przez kogoś z wiedzą wewnętrzną. Gdy tryb Delta jest aktywowany, COLDCARD wydaje się otwierać prawdziwą wallet, umożliwiając atakującemu przeglądanie i potwierdzenie, że wygląda autentycznie. Jednak potajemnie blokuje wszystkie podpisywanie transakcji, więc nie można wysyłać bitcoinów. Wyłącza również dostęp do frazy seed, a każda próba jej wyświetlenia spowoduje jej całkowite usunięcie. Aby fałszywy wallet wyglądał bardziej przekonująco, Trick PIN używany w trybie Delta musi zaczynać się od tych samych cyfr, co prawdziwy PIN (więc pokazuje te same słowa antyphishingowe), ale kończy się inaczej.
    - `Policy Unlock`, po wybraniu, Single Signer Spending Policy (SSSP) zostanie wyłączony po wprowadzeniu kodu PIN.
    - `Policy Unlock & Wipe`, po wybraniu udaje, że wyłącza SSSP, ale przy okazji wymazuje seedphrase.

9. Po wybraniu czynności, którą chcesz sparować z kodem PIN triku, potwierdź wybór, naciskając przycisk `✓`. Podstępny kod PIN został pomyślnie skonfigurowany.

10. W zakładce `Ustawienia` > `Ustawienia logowania` > `Trick PINs` możesz zobaczyć listę utworzonych przez siebie kodów PIN i powiązanych z nimi akcji. Możesz zmienić konfigurację kodów PIN sztuczek i powiązanych z nimi akcji. Można je również ukryć lub usunąć, wybierając kod PIN, a następnie opcję `Ukryj sztuczkę` lub `Usuń sztuczkę`.


![60](assets/en/60.webp)


### Podstępne kody PIN - Dodaj, jeśli błędne


Alternatywnie można dodać akcję `Add If Wrong`, która zostanie uruchomiona po wprowadzeniu nieprawidłowego kodu PIN określoną liczbę razy. Można to skonfigurować, wykonując następujące kroki:


1. Włącz Mk4, podłączając go do źródła zasilania.

2. Wprowadź kod PIN.

3. Przejdź do `Ustawienia` > wybierz `Ustawienia logowania` > wybierz `Trick PINs` > wybierz `Add If Wrong`.


![61](assets/en/61.webp)


4. Mk4 wyświetli komunikat dotyczący tego ustawienia. Przejdź w dół, czytając wyjaśnienie, a następnie naciśnij `✓`, aby kontynuować.

5. Wprowadź liczbę błędnych prób wymaganych do uruchomienia akcji. Uwaga: Maksymalna liczba prób wynosi `12`. Wynika to z faktu, że Mk4 został zaprojektowany w taki sposób, że gdy nieprawidłowy PIN zostanie wprowadzony `13` razy, urządzenie zablokuje się, czyniąc go bezużytecznym na stałe. Po wprowadzeniu numeru naciśnij `✓`, aby kontynuować.

6. Przejdź w górę lub w dół, aby wybrać akcję. Dostępne są następujące akcje:


   - `Wipe, Stop`: seedphrase zostanie skasowany, a urządzenie wyświetli komunikat "Seed is wipeed, Stop"
   - `Wipe & Reboot`: seedphrase zostanie skasowany, a urządzenie uruchomi się ponownie bez żadnego komunikatu.
   - `Silent Wipe`: seedphrase jest wymazywany po cichu, a urządzenie zachowuje się jak przy próbie podania błędnego PIN-u (brak oczywistego komunikatu o wymazaniu).
   - `Brick Self`: Urządzenie jest trwale wyłączone i wyświetla tylko komunikat "Bricked"
   - `Ostatnia szansa`: Urządzenie seedphrase zostanie skasowane, ale dostępna będzie ostatnia próba wprowadzenia kodu PIN; ponowne wprowadzenie błędnego kodu PIN spowoduje zamurowanie urządzenia.
   - `Just Reboot`: Urządzenie po prostu uruchamia się ponownie i nic więcej się nie zmienia.

Wybierz działanie, które chcesz zastosować i naciśnij `✓`, aby kontynuować


![62](assets/en/62.webp)


7. Zostaniesz przeniesiony do katalogu `Ustawienia > Ustawienia logowania > Trick PINs`. Pod `Trick PINs:`, znajdziesz listę kodów PIN wraz z akcją `WRONG PIN`. Możesz także ukryć lub usunąć go, wybierając PIN, a następnie wybierając `Ukryj sztuczkę` lub `Usuń sztuczkę`.


![63](assets/en/63.webp)



## Wnioski


Ten samouczek zawiera przewodnik dotyczący konfiguracji Mk4, przeprowadzania transakcji Bitcoin za pomocą Mk4 oraz korzystania z niektórych zaawansowanych funkcji Mk4. Mk4 oferuje bezpieczne i elastyczne sposoby przechowywania bitcoinów i zarządzania nimi. Jego konstrukcja zapewnia, że klucze prywatne nigdy nie opuszczają urządzenia, a funkcje takie jak passphrase, oszukańcze kody PIN i transakcje air-gapped dają użytkownikom pełną kontrolę nad konfiguracją zabezpieczeń. Można go sparować z Sparrow Wallet, aby zapewnić przyjazne dla użytkownika doświadczenie w tworzeniu, podpisywaniu i zarządzaniu transakcjami Bitcoin bez uszczerbku dla prywatności i bezpieczeństwa.


Jeśli chcesz poznać inne funkcje, możesz sprawdzić dokumentację na stronie Coinkite [tutaj](https://coldcard.com/docs/). Mam nadzieję, że ten poradnik okaże się przydatny podczas korzystania z karty Cold Mk4. Dziękuję i do zobaczenia następnym razem!