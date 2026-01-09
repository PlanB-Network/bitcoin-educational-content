---
name: Ashigaru - Whirlpool Coinjoin
description: Jak tworzyć coinjoiny w aplikacji Ashigaru?
---

![cover](assets/cover.webp)



"*a bitcoin wallet for the streets*"



W tym samouczku dowiesz się, czym jest coinjoin i jak go wykonać za pomocą aplikacji Ashigaru Terminal i implementacji Whirlpool, protokołu coinjoin odziedziczonego po Samourai Wallet.



## Jak działają przeguby Whirlpool



W tym samouczku nie będę wracał do pojęcia coinjoina, jego użyteczności ani teoretycznego działania Whirlpool, ponieważ tematy te zostały już szczegółowo wyjaśnione w części 5 szkolenia BTC 204 w Akademii Planu ₿. Jeśli jeszcze nie opanowałeś działania Whirlpool lub zasady coinjoin, zdecydowanie zalecam zapoznanie się z tą częścią 5 przed kontynuowaniem:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Oto jednak kilka krótkich faktów i liczb, które mogą się przydać.



Portfele kompatybilne z Whirlpool wykorzystują 4 oddzielne konta, aby spełnić potrzeby procesu coinjoin:




- Konto **Deposit**, identyfikowane przez indeks `0`;
- Konto **Bad Bank** (lub *doxxic exchange*), oznaczone indeksem `2,147,483,644'`;
- Konto **Premix**, identyfikowane przez indeks `2 147 483 645'`;
- Konto **Postmix**, identyfikowane przez indeks `2 147 483 646'`.



Na Ashigaru w listopadzie 2025 r. dostępne są dwa nominały puli (lista ta prawdopodobnie będzie ewoluować w nadchodzących miesiącach: pamiętaj więc, aby sprawdzać wartości podczas czytania):




- 0.25 BTC`, z opłatą wpisową w wysokości 0,0125 BTC`;
- 0.025 BTC, z opłatą wpisową w wysokości 0,00125 BTC.



Każdy cykl mieszania może obejmować od 5 do 10 UTXO na wejściu i wyjściu.



![Image](assets/fr/01.webp)



## Wymagania dotyczące oprogramowania



Do tworzenia coinjoinów za pomocą Whirlpool potrzebne będą trzy oddzielne programy:





- Ashigaru Terminal**, który pozwala zarządzać coinjoinami bezpośrednio z komputera;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, aplikacja na smartfona, dzięki której możesz wydawać swoje bitcoiny w *postmix* z dowolnego miejsca;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, implementacja węzła Bitcoin gwarantująca suwerenne połączenie z siecią, bez zależności od serwera innej firmy.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Zainstaluj każde z tych narzędzi, postępując zgodnie z odpowiednimi samouczkami, a następnie możesz rozpocząć tworzenie pierwszych coinjoinów.



## Odbieranie bitcoinów



Po utworzeniu portfela zaczniesz od pojedynczego konta, oznaczonego indeksem `0`. Jest to konto `Deposit`. To właśnie na to konto będziesz wysyłać bitcoiny przeznaczone do coinjoinów. Możesz je otrzymać za pośrednictwem aplikacji Ashigaru (patrz część 5 dedykowanego samouczka) lub za pośrednictwem Ashigaru Terminal (również szczegółowo opisanego w części 5 dedykowanego samouczka).



Gdy twoje konto depozytowe będzie zawierało co najmniej kwotę potrzebną do uczestnictwa w najmniejszej puli (plus opłaty za usługi i minimum wymagane do pokrycia kosztów mining), będziesz gotowy do zainicjowania pierwszych coinjoinów.



![Image](assets/fr/02.webp)



## Tx0



Gdy środki dotrą na konto depozytowe, a transakcja zostanie potwierdzona, możesz rozpocząć proces łączenia monet. Aby to zrobić, w terminalu Ashigaru otwórz menu `Wallets`, a następnie wybierz swój wallet. Jeśli wallet jest zablokowany, oprogramowanie poprosi o podanie hasła i passphrase.



![Image](assets/fr/03.webp)



Następnie wybierz konto `Deposit`.



![Image](assets/fr/04.webp)



Przejdź do menu `UTXOs`.



![Image](assets/fr/05.webp)



Tutaj zobaczysz listę wszystkich UTXO na swoim koncie depozytowym. Wybierz te, które chcesz wysłać w cyklach coinjoin.



Dla większej poufności i uniknięcia *Common Input Ownership Heuristic (CIOH)*, zaleca się użycie tylko jednego UTXO na wejście w Whirlpool (szczegółowe wyjaśnienie tej zasady można znaleźć w BTC 204).



Naciśnij klawisz `ENTER` na klawiaturze, aby wybrać UTXO: gwiazdka `(*)` pojawi się obok niego, aby wskazać, że został wybrany.



![Image](assets/fr/06.webp)



Następnie kliknij przycisk `Mix Selected`.



![Image](assets/fr/07.webp)



Jeśli masz UTXO wystarczająco duży, aby uczestniczyć w jednej z dwóch dostępnych pul, możesz wybrać pulę docelową za pomocą strzałek. Na tej stronie zostaną wyświetlone szczegóły dotyczące Tx0 :




- liczba UTXO, które wejdą do puli;
- różne stosowane opłaty (opłaty za usługi i opłaty mining) ;
- wielkość *doksycznej zmiany*.



Sprawdź dokładnie informacje, a następnie kliknij `Broadcast`, aby nadać Tx0.



![Image](assets/fr/08.webp)



Ashigaru wyświetli wtedy TXID twojego Tx0, potwierdzając, że transakcja została rozesłana w sieci.



![Image](assets/fr/09.webp)



## Tworzenie coinjoinów



Gdy Tx0 zostanie nadany, wróć do strony głównej konta depozytowego, a następnie kliknij `Konta` i wybierz konto `Premix`.



![Image](assets/fr/10.webp)



W menu `UTXOs` zobaczysz różne wyrównane części, gotowe do wejścia w cykle coinjoin. Gdy tylko Tx0 zostanie potwierdzone, Ashigaru Terminal automatycznie rozpocznie pierwszy cykl mieszania.



![Image](assets/fr/11.webp)



Po potwierdzeniu Tx0, pierwsza transakcja coinjoin zostanie utworzona i wysłana automatycznie przez Ashigaru Terminal. Przechodząc do `Konta > Postmix > UTXOs`, możesz zobaczyć swoje wyrównane UTXO, oczekujące na potwierdzenie ich pierwszego cyklu.



![Image](assets/fr/12.webp)



Możesz teraz pozostawić Ashigaru Terminal uruchomiony w tle: będzie on kontynuował automatyczne miksowanie i remiksowanie twoich utworów.



## Wykończenie połączeń coinjoin



Teraz możesz pozwolić swoim monetom remiksować się automatycznie. Model Whirlpool oznacza, że nie ma żadnych dodatkowych opłat za remiksowanie: żadnych opłat za usługę, żadnych opłat mining. Umożliwienie monetom udziału w większej liczbie cykli mieszania może więc przynieść tylko korzyści dla poufności.



Aby lepiej zrozumieć ten mechanizm i ile cykli warto na niego czekać, polecam przeczytać ten artykuł:



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Aby wyświetlić liczbę remiksów wykonanych przez każdy z twoich utworów, otwórz menu `UTXOs` na koncie `Postmix`.



![Image](assets/fr/13.webp)



Aby wydać mieszane monety, przejdź do aplikacji Ashigaru, która używa tego samego wallet, co oprogramowanie Ashigaru Terminal. wallet wyświetlany przy otwarciu odpowiada kontu `Deposit`. Aby uzyskać dostęp do konta `Postmix`, które zawiera mieszane UTXO, kliknij symbol Whirlpool w prawym górnym rogu.



![Image](assets/fr/14.webp)



Na tym koncie zobaczysz wszystkie swoje monety, które są obecnie mieszane. Aby je wydać, naciśnij symbol `+` w prawym dolnym rogu ekranu, a następnie wybierz `Wyślij`.



![Image](assets/fr/15.webp)



Podaj szczegóły transakcji: adres odbiorcy, kwotę do wysłania i, jeśli chcesz, wybierz konkretną strukturę transakcji, aby jeszcze bardziej zwiększyć poufność (zobacz odpowiednie samouczki).



![Image](assets/fr/16.webp)



Dokładnie sprawdź szczegóły transakcji, a następnie przeciągnij strzałkę u dołu ekranu, aby potwierdzić wysyłkę.



![Image](assets/fr/17.webp)



Twoja transakcja została podpisana i wyemitowana w sieci Bitcoin.



![Image](assets/fr/18.webp)



## Wydać Doxxic Change



Pamiętaj: Model Whirlpool opiera się na wyrównywaniu twoich elementów w Tx0, zanim wejdą do pul. To właśnie ten mechanizm przerywa śledzenie UTXO. Moim zdaniem jest to najbardziej wydajny model coinjoin, ale ma jedną wadę: generuje *zmianę*, która nie przechodzi przez proces coinjoin.



Ta zmiana odpowiada UTXO utworzonemu dla każdego Tx0. Jest ona izolowana na specjalnym koncie o nazwie `Doxxic Change` lub `Bad Bank`, w zależności od oprogramowania, aby uniknąć używania jej z innymi UTXO. Jest to bardzo ważne, ponieważ te UTXO nie zostały zmieszane: ich linki identyfikowalności pozostają nienaruszone i mogą zagrozić poufności, ustanawiając połączenie między tobą a twoją aktywnością coinjoin. Dlatego należy obchodzić się z nimi ostrożnie i **nigdy nie używać ich z innymi UTXO**, niezależnie od tego, czy są mieszane, czy nie. Połączenie toksycznego UTXO z mieszanym UTXO zniweczy wszystkie korzyści w zakresie prywatności uzyskane dzięki coinjoinowi.



Na chwilę obecną Ashigaru nie oferuje bezpośredniego dostępu do tego konta `Doxxic Change` (przynajmniej ja go nie znalazłem). Funkcja ta zostanie prawdopodobnie dodana w przyszłej aktualizacji. W międzyczasie jedynym sposobem na odzyskanie tych środków jest zaimportowanie seed do Sparrow Wallet. Ten ostatni zazwyczaj automatycznie wykryje, że jest to wallet używany z Whirlpool i da ci dostęp do wszystkich czterech kont, w tym konta `Doxxic Change`. Następnie możesz wydać te UTXO jak zwykłe bitcoiny z Sparrow.



Oto kilka możliwych strategii zarządzania swoimi walutowymi UTXO z coinjoins bez narażania swojej prywatności:





- Łączenie ich w mniejsze pule:** Jeśli twój toksyczny UTXO jest wystarczająco duży, aby dołączyć do mniejszej puli, jest to ogólnie najlepsza opcja. Uważaj jednak, aby nigdy nie łączyć kilku toksycznych UTXO, ponieważ spowoduje to utworzenie połączenia między różnymi wpisami w Whirlpool.





- Oznacz je jako niewydawalne:** Innym rozważnym podejściem jest po prostu pozostawienie ich na osobnym koncie i pozostawienie ich nietkniętych. Zapobiegnie to przypadkowemu ich wydaniu. Jeśli wartość bitcoina wzrośnie, mogą zostać otwarte nowe pule dostosowane do ich wielkości.





- Przekazywanie darowizn:** Możesz zamienić toksyczne UTXO na darowizny dla deweloperów Bitcoin, projektów open-source lub stowarzyszeń, które akceptują BTC. Pozwala to na użyteczne pozbycie się ich przy jednoczesnym wspieraniu ekosystemu.





- Kup przedpłacone karty podarunkowe lub karty Visa:** Platformy takie jak [Bitrefill](https://www.bitrefill.com/) umożliwiają wymianę bitcoinów na karty podarunkowe lub doładowywane karty Visa, które można wykorzystać w sklepach. Może to być prosty i dyskretny sposób na wydawanie toksycznych UTXO.





- Zamień je na Monero:** Samourai Wallet oferował nieistniejącą już usługę atomowego swapu BTC/XMR. Jeśli podobna usługa istnieje (osobiście o żadnej nie wiem), jest to doskonałe rozwiązanie do izolowania tych UTXO, konwertowania ich na Monero, a następnie wysyłania ich z powrotem do Bitcoin. Metoda ta była jednak kosztowna i zależna od dostępnej płynności.





- Przeniesienie ich do Lightning Network:** Przeniesienie tych UTXO do Lightning Network w celu skorzystania z obniżonych opłat transakcyjnych jest potencjalnie interesującą opcją. Metoda ta może jednak ujawnić pewne informacje w zależności od sposobu korzystania z Lightning i dlatego należy jej używać ostrożnie.



## Jak mogę sprawdzić jakość naszych cykli coinjoin?



Aby coinjoin był naprawdę skuteczny, musi charakteryzować się wysokim stopniem jednorodności między kwotami wejściowymi i wyjściowymi. Ta jednorodność zwiększa liczbę możliwych interpretacji dla zewnętrznego obserwatora, co z kolei zwiększa niepewność co do transakcji. Aby zmierzyć tę niepewność, używamy koncepcji entropii zastosowanej do transakcji. Model Whirlpool jest uznawany za jeden z najskuteczniejszych pod tym względem, ponieważ gwarantuje doskonałą jednorodność między uczestnikami. Aby uzyskać bardziej dogłębne spojrzenie na tę zasadę, zalecam zapoznanie się z ostatnim rozdziałem części 5 szkolenia BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Wydajność kilku cykli coinjoin jest mierzona wielkością zbiorów, w których moneta jest ukryta. Zbiory te definiują tak zwane *anonsets*. Istnieją dwa rodzaje: pierwszy mierzy poufność w obliczu analizy retrospektywnej (od teraźniejszości do przeszłości), a drugi mierzy odporność na analizę prospektywną (od przeszłości do teraźniejszości). Aby uzyskać pełne wyjaśnienie tych dwóch wskaźników, przeczytaj poniższy samouczek (lub, ponownie, szkolenie BTC 204):



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Jak zarządzać postmixem?



Po uruchomieniu kilku cykli coinjoin, najlepszą strategią jest trzymanie UTXO na koncie `Postmix`, pozwalając im mieszać się w nieskończoność, dopóki nie będzie trzeba ich wydać.



Niektórzy użytkownicy wolą przenieść swoje mieszane bitcoiny do zabezpieczonego sprzętowo wallet. Ta opcja jest możliwa, ale wymaga pewnego rygoru, aby zapewnić, że poufność uzyskana dzięki coinjoins nie zostanie naruszona.



Najczęstszym błędem jest łączenie UTXO. Ważne jest, aby nigdy nie łączyć mieszanych UTXO z niemieszanymi UTXO w tej samej transakcji, w przeciwnym razie istnieje ryzyko uruchomienia *Common Input Ownership Heuristic (CIOH)*. Oznacza to rygorystyczne zarządzanie UTXO, w szczególności poprzez jasne i precyzyjne etykietowanie. Ogólnie rzecz biorąc, łączenie UTXO jest złą praktyką, która często prowadzi do utraty poufności, jeśli jest źle zarządzana.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Należy również zachować ostrożność przy konsolidacji mieszanych UTXO. Ograniczone konsolidacje można rozważyć, jeśli UTXO mają znaczące anonsety, ale nieuchronnie zmniejszają one poziom poufności. Unikaj masowych lub pospiesznych konsolidacji, przeprowadzanych przed wystarczającą liczbą remiksów, ponieważ mogą one ustanowić powiązania wnioskowania między elementami przed i po remiksie. W razie wątpliwości najlepiej nie konsolidować UTXO postmix i przesyłać je pojedynczo do sprzętu wallet, generując za każdym razem nowy pusty adres odbioru. Nie zapomnij oznaczyć każdego przeniesionego UTXO.



Zdecydowanie odradzamy przenoszenie postmix UTXO do portfeli przy użyciu skryptów mniejszościowych. Na przykład, jeśli uczestniczyłeś w Whirlpool z portfela multi-sig w `P2WSH`, będzie niewielu z was dzielących ten typ skryptu. Wysyłając swoje UTXO postmix do tego samego typu skryptu, znacznie zmniejszasz swoją anonimowość. Poza typem skryptu, inne specyficzne odciski palców wallet mogą zagrozić twojej poufności, więc najlepiej jest wydać je z aplikacji Ashigaru.



Wreszcie, podobnie jak w przypadku wszystkich transakcji Bitcoin, nigdy nie używaj ponownie adresu odbiorczego. Każda płatność musi zostać wysłana na nowy, unikalny, pusty adres.



Najprostszą i najbezpieczniejszą metodą jest pozostawienie zmieszanych UTXO na koncie `Postmix`, pozwolenie im na naturalne remiksowanie i wydawanie ich tylko wtedy, gdy są potrzebne z Ashigaru.



Portfele Ashigaru i Sparrow zawierają dodatkowe zabezpieczenia przed najczęstszymi błędami związanymi z analizą blockchain, pomagając zachować poufność transakcji.