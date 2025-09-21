---
name: COLDCARD Mk

description: Tworzenie, tworzenie kopii zapasowych i używanie klucza prywatnego Bitcoin z urządzeniem Coldcard i Bitcoin Core
---

![cover](assets/cover.webp)


_Tworzenie, tworzenie kopii zapasowych i używanie klucza prywatnego Bitcoin z urządzeniem Coldcard i Bitcoin Core_


## Kompletny przewodnik po generowaniu klucza prywatnego za pomocą karty Coldcard i używaniu go przez Interface węzła Bitcoin Core!


U podstaw korzystania z sieci Bitcoin leży koncepcja kryptografii asymetrycznej: para kluczy - jeden prywatny i jeden publiczny - które szyfrują i odszyfrowują dane, koncepcja zapewniająca poufność komunikacji.


W przypadku Bitcoin, generując taką parę kluczy prywatnych i publicznych, jesteśmy w stanie przechowywać bitcoiny (UTXO lub niewydane transakcje) i podpisywać transakcje w celu ich wydania.


Obecnie dostępnych jest wiele narzędzi ułatwiających losowe generowanie klucza prywatnego i jego kopii zapasowej w formie tekstowej przy użyciu BIP 39 - standardu określającego sposób, w jaki portfele kojarzą frazę Mnemonic (frazę seed) z kluczami szyfrującymi. Najczęściej fraza Mnemonic składa się z 12 lub 24 słów, które należy bezpiecznie zarchiwizować, aby móc odzyskać Wallet i jego bitcoiny.


W tym artykule dowiemy się, jak utworzyć klucz prywatny generate za pomocą Coldcard Mk4, jednego z najczęściej używanych i najbezpieczniejszych urządzeń w świecie Bitcoin, przy użyciu metody rzutu kostką w celu zapewnienia maksymalnej entropii oraz jak używać go z Bitcoin Core w sposób hermetyzowany!


**Uwaga: 🧰** Aby korzystać z przewodnika, należy pobrać następujące narzędzia:



- Urządzenie Coldcard (Mk3 lub Mk4)
- Karta microSD (4 GB w zupełności wystarczy)
- Magnetyczny kabel USB z funkcją zasilania (mini-usb dla Mk3, usb-c dla Mk4)
- Jedna lub więcej kości jakości


## Generowanie nowej frazy Mnemonic za pomocą karty Coldcard


Rozpoczniemy proces tworzenia klucza prywatnego od zera, zakładając świeżo rozpakowaną kartę Coldcard, na której został już skonfigurowany kod PIN (postępuj zgodnie z instrukcjami na karcie Coldcard podczas inicjalizacji urządzenia).


**Uwaga🚨:** Aby zresetować klucz prywatny już skonfigurowanej karty Coldcard, wykonaj następujące kroki:

_Zaawansowane/Narzędzia > Strefa zagrożenia > Funkcje seed > Zniszcz seed > ✓_


**Uwaga:** Po wykonaniu tych kroków karta Coldcard zapomni klucz prywatny. Upewnij się, że prawidłowo utworzyłeś kopię zapasową frazy Mnemonic, jeśli chcesz móc ją później odzyskać.


## Kroki do wykonania:


Połączenie z kartą Coldcard za pomocą kodu PIN > Nowe słowa seed > Rzut kostką z 24 słowami


Wykonaj 100 rzutów kostką, zapisując uzyskany wynik od 1 do 6 na karcie Coldcard po każdym rzucie. Praktykując tę metodę, tworzysz 256 bajtów entropii, sprzyjając w ten sposób tworzeniu całkowicie losowego klucza prywatnego. Coinkite dostarcza również niezbędną dokumentację do niezależnej weryfikacji swojego systemu generowania entropii.


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


Po wykonaniu 100 rzutów kośćmi naciśnij ✓, a następnie zapisz 24 uzyskane słowa w kolejności. Sprawdź dwukrotnie i naciśnij ✓. Na koniec pozostaje tylko ukończyć test weryfikacyjny 24 słów na karcie Coldcard i voila, twój nowy klucz prywatny został utworzony!


Następnie wybierz, czy chcesz aktywować funkcje NFC (Mk4) i USB, postępując zgodnie z wyświetlanymi krokami. Po przejściu do menu głównego nadszedł czas na aktualizację oprogramowania sprzętowego urządzenia. Przejdź do Advanced/Tools > Upgrade Firmware > Show Version i sprawdź oficjalną stronę internetową, aby zweryfikować i pobrać najnowszą dostępną wersję. Zaleca się aktualizację karty Coldcard w celu zapewnienia maksymalnego bezpieczeństwa.


Przed kontynuowaniem zaleca się zanotowanie odcisku palca klucza głównego (XFP) powiązanego z kluczem prywatnym. Dane te pozwalają na szybką weryfikację, czy jesteś w prawidłowym Wallet, na przykład w przypadku odzyskiwania. Przejdź do Advanced/Tools > View Identity > Master Key Fingerprint (XFP) i zapisz serię ośmiu uzyskanych znaków alfanumerycznych. XFP można zanotować w tym samym miejscu co frazę Mnemonic, nie są to dane wrażliwe.


**Uwaga: 💡** zaleca się przetestowanie kopii zapasowej frazy Mnemonic w innym oprogramowaniu. Aby zrobić to bezpiecznie, zapoznaj się z naszym artykułem Weryfikacja kopii zapasowej Bitcoin Wallet z Tails w mniej niż 5 minut.


## Bonus bezpieczeństwa: "Tajna fraza" (opcjonalnie)


passphrase (tajna fraza) to świetny element, który można dodać do konfiguracji Wallet, aby dodać Layer zabezpieczeń w celu ochrony bitcoinów. passphrase działa jako rodzaj 25. słowa do frazy Mnemonic. Po dodaniu, tworzony jest zupełnie nowy Wallet wraz z kluczem prywatnym i powiązaną z nim frazą Mnemonic. Nie jest konieczne zapisywanie nowej frazy Mnemonic, ponieważ dostęp do Wallet można uzyskać poprzez połączenie początkowej frazy Mnemonic z wybraną frazą passphrase.


Celem jest odnotowanie passphrase oddzielnie od frazy Mnemonic, ponieważ atakujący, który ma dostęp do obu elementów, będzie miał dostęp do funduszy. Z drugiej strony atakujący, który ma dostęp tylko do jednego z tych elementów, nie będzie miał dostępu do funduszy i to właśnie ta konkretna zaleta optymalizuje poziom bezpieczeństwa konfiguracji Wallet.


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## Kroki dodawania passphrase za pomocą Coldcard:


passphrase > Dodaj słowa (zalecane) > Zastosuj. Urządzenie wyświetli XFP nowo wygenerowanego Wallet wraz z passphrase, które należy zanotować wraz z passphrase z tych samych powodów, o których wspomniano wcześniej.


**Wskazówka💡** Tutaj znajdują się dodatkowe zasoby związane z passphrase:



- [Tutaj](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) znajduje się pierwszy z nich autorstwa _Trezor_;
- [Tutaj](https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/) można znaleźć drugi z nich autorstwa_Coinkite_;
- A [tutaj](https://armantheparman.com/passphrase/) znajdziesz ostatni autorstwa _armantheparman_.


## Eksportowanie Wallet do Bitcoin Core


Wallet jest teraz gotowy do wyeksportowania do oprogramowania w celu interakcji z siecią Bitcoin. W tym przewodniku będziemy używać Bitcoin Core (v24.1).


Zapoznaj się z naszymi przewodnikami instalacji i konfiguracji dla Bitcoin Core:



- **Uruchamianie własnego węzła z Bitcoin Core:** https://agora256.com/faire-tourner-son-propre-noeud-avec-Bitcoin-core/
- **Konfiguracja Tora dla węzła Bitcoin Core:** https://agora256.com/configuration-tor-Bitcoin-core/


Najpierw włóż kartę micro SD do Coldcard, a następnie wyeksportuj Wallet do Bitcoin Core, wykonując następujące czynności: Advanced/Tools > Export Wallet > Bitcoin Core. Na karcie micro SD zostaną zapisane dwa pliki: Bitcoin-core.sig i Bitcoin-core.txt. Włóż kartę micro SD do komputera, na którym zainstalowany jest Bitcoin Core i otwórz plik .txt. Zobaczysz wiersz "Dla Wallet z odciskiem palca klucza głównego" Sprawdź, czy ośmioznakowy XFP pasuje do tego, który zanotowałeś podczas tworzenia klucza prywatnego"

Przed wykonaniem instrukcji zawartych w pliku, zacznijmy od przygotowania Wallet w Bitcoin Core Interface, wykonując następujące kroki: przejdź do zakładki Plik > Utwórz Wallet. Wybierz nazwę dla swojego Wallet (termin wymienny z "porte-monnaie" w Core) i zaznacz opcje Wyłącz klucze prywatne, Utwórz pusty Wallet i Deskryptory Wallet, jak pokazano na poniższym obrazku. Następnie naciśnij przycisk Utwórz.


![create a wallet](assets/guide-agora/3.webp)


Po utworzeniu Wallet w Bitcoin Core, przejdź do zakładki Window > Console i upewnij się, że wybrany Wallet na górze strony wyświetla nazwę tego, który utworzyłeś.


Teraz, w pliku .txt wygenerowanym wcześniej przez Coldcard, skopiuj linię zaczynającą się od importdescriptors, a następnie wklej ją do konsoli Bitcoin Core. Powinna zostać zwrócona odpowiedź zawierająca wiersz "success": true.


![nodes window](assets/guide-agora/4.webp)


Jeśli odpowiedź zawiera "message": "Ranged descriptors should not have a label", usuń wpis "label": "Coldcard xxxx0000" w skopiowanym wierszu z pliku .txt, a następnie wklej cały wiersz z powrotem do konsoli Bitcoin Core.


W razie potrzeby można znaleźć pomoc [tutaj](https://github.com/Coldcard/firmware/blob/master/docs/Bitcoin-core-usage.md) na Coldcard Github.


## Walidacja importu Wallet do rdzenia Bitcoin


Aby upewnić się, że operacja zakończyła się powodzeniem, konieczne jest sprawdzenie, czy żądany Wallet został zaimportowany do Bitcoin Core. Prostą metodą potwierdzenia tego jest sprawdzenie, czy adresy wygenerowane w Coldcard odpowiadają adresom wygenerowanym w Bitcoin Core.


Bitcoin Core: Odbiór > Utwórz nowy odbierający Address

Coldcard: Address Explorer > Wybierz Address zaczynający się od bc1q. Coldcard Address "bc1q" powinien pasować do Address wyświetlanego w Bitcoin Core.

Odbieranie i wysyłanie transakcji w trybie "air-gapped


Odbieranie transakcji jest niezwykle proste; wystarczy nacisnąć przycisk Odbierz, oznaczyć transakcję etykietą (opcjonalne, ale zalecane) i utworzyć nowy odbierający Address. Następnie wystarczy udostępnić Address nadawcy.


Teraz kluczowym elementem tej konfiguracji Coldcard + Bitcoin Core jest wysyłanie transakcji bez połączenia Coldcard i jej klucza prywatnego z Internetem, metoda zwana air-gapped, która wykorzystuje funkcję TBSP (PSBT - częściowo podpisane transakcje Bitcoin) Bitcoin.

Zasadniczo używamy Bitcoin Core Interface do skonstruowania transakcji, którą następnie eksportujemy za pośrednictwem karty micro SD do Coldcard w celu podpisania, a następnie zwracamy podpisany plik transakcji do Bitcoin Core i transmitujemy transakcję do sieci. Musimy to zrobić w ten sposób, ponieważ Wallet zaimportowany do Bitcoin Core nie ma klucza prywatnego, a jedynie klucz publiczny (który pozwala nam na generate naszych adresów odbiorczych), więc niemożliwe jest podpisanie transakcji bezpośrednio w oprogramowaniu, aby wydać nasze bitcoiny.


Przed kontynuowaniem upewnij się, że następujące opcje są włączone w Ustawienia > Wallet:



- Włącz funkcje kontroli monet
- Wydawanie niepotwierdzonych monet (opcjonalnie)
- Włączanie kontroli TBPS


![option ](assets/guide-agora/5.webp)


### Kroki wysyłania w trybie air-gapped:


Wyślij > Wejścia > wybierz żądany UTXO, a następnie wprowadź Address odbiorcy w Zapłać do. Opłata za transakcję: Wybierz ... > Niestandardowe > Wprowadź opłatę transakcyjną (Bitcoin Core oblicza Sats/kilobajt zamiast sat/bajt jak większość alternatywnych rozwiązań Wallet. Tak więc 4000 Sats/kilobajt = 4 Sats/bajt). Utwórz niepodpisaną transakcję > zapisz plik na karcie micro SD i włóż ją do Coldcard.


W aplikacji Coldcard naciśnij przycisk Ready to sign, zweryfikuj szczegóły transakcji, a następnie naciśnij przycisk ✓ i włóż kartę micro SD z powrotem do komputera po wygenerowaniu podpisanych plików.


Wróć do Bitcoin Core, przejdź do zakładki Plik > Załaduj TBSP z pliku i wprowadź podpisany plik transakcji .PSBT. Na ekranie pojawi się okno PSBT Operations, potwierdzające, że transakcja jest w pełni podpisana i gotowa do transmisji. Pozostaje tylko nacisnąć przycisk Transmisja transakcji.


![PSBT operations](assets/guide-agora/6.webp)


### Wnioski


Połączenie urządzenia Coldcard z Bitcoin Core, na którym uruchamiasz własny węzeł, jest potężne. Dodajmy do tego klucz prywatny wygenerowany za pomocą 100 rzutów kostką i tajną frazę, a konfiguracja Wallet stanie się wyrafinowaną i solidną fortecą.


Zachęcamy do kontaktu z nami w celu podzielenia się swoimi uwagami i pytaniami! Naszym celem jest dzielenie się wiedzą i zwiększanie naszego zrozumienia z dnia na dzień.