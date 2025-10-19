---
name: Ginger Wallet
description: Oprogramowanie Bitcoin Wallet o otwartym kodzie źródłowym, Fork z Wasabi Wallet, integrujące Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet jest otwartoźródłowym, nieobciążającym portfelem Bitcoin skoncentrowanym na poufności i prywatności. Rozpoczął życie jako Fork od Wasabi Wallet (po wersji 2.0.7.2 - licencja MIT).



Ginger Wallet zachowuje architekturę techniczną Wasabi, dodając jednocześnie kilka specyficznych funkcji. Zgodnie z dokumentacją [Ginger Wallet](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), Wasabi kładzie nacisk na **autonomię i kontrolę**, podczas gdy Ginger skupia się na **łatwości użytkowania, bezpieczeństwie i uproszczonym doświadczeniu**, dzięki czemu jest dostępny dla osób mniej zaznajomionych z aspektami technicznymi.



Ginger Wallet to oprogramowanie Wallet tylko dla komputerów (bez aplikacji mobilnej).



## Czym jest CoinJoin?



CoinJoin** to szczególny rodzaj struktury transakcji Bitcoin, która łączy kilku uczestników w jednej wspólnej transakcji. Mechanizm ten łączy wpisy różnych użytkowników we wspólną transakcję, co sprawia, że śledzenie środków jest niezwykle trudne - jeśli nie często niemożliwe, jeśli jest wykonane prawidłowo. W rezultacie dla zewnętrznego obserwatora staje się prawie niemożliwe zidentyfikowanie z całą pewnością pochodzenia i przeznaczenia zaangażowanych bitcoinów, w przeciwieństwie do konwencjonalnych transakcji Bitcoin.



Dla użytkownika CoinJoin pomaga zachować poufność. Na przykład, jeśli otrzymasz darowiznę w wysokości 10 000 Sats na Bitcoin Address, nadawca może śledzić te środki i, w niektórych przypadkach, wywnioskować, że posiadasz większą ilość bitcoinów lub obserwować twoje działania. Dokonując CoinJoin po tej darowiźnie w wysokości 10 000 Sats, przerywasz możliwość śledzenia: nadawca nie będzie już w stanie uzyskać żadnych informacji o tobie z tej płatności.



Chaumian CoinJoin oferuje wysoki poziom bezpieczeństwa, ponieważ środki pozostają pod wyłączną kontrolą użytkownika przez cały czas. Nawet operatorzy serwerów koordynujących nie mogą w żadnym wypadku przekierować bitcoinów uczestników. Ani użytkownicy, ani koordynatorzy nie muszą ufać sobie nawzajem: każdy zachowuje kontrolę nad swoimi kluczami prywatnymi i pozostaje wyłącznie upoważniony do zatwierdzania transakcji. Żadna strona trzecia nie może zatem przywłaszczyć sobie bitcoinów użytkownika podczas CoinJoin, ani ustanowić bezpośredniego połączenia między jego danymi wejściowymi i wyjściowymi.



Aby dowiedzieć się więcej o CoinJoin, sprawdź kurs BTC 204 Akademii Plan ₿:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Zainstaluj Ginger Wallet



Aby zainstalować Ginger Wallet, odwiedź stronę internetową [Ginger Wallet](https://gingerwallet.io).



Naciśnij **Download**, aby pobrać odpowiednią wersję dla swojego komputera (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Inną opcją jest przejście do witryny [GitHub] projektu (https://github.com/GingerPrivacy/GingerWallet/releases), aby go pobrać.



![screen](assets/fr/04.webp)



Następnie uruchom program instalacyjny.



![screen](assets/fr/05.webp)




## Ustawienia parametrów



### Wstępne konfiguracje



Otwórz Ginger Wallet, wybierz preferowany język.



![screen](assets/fr/06.webp)



Od samego początku Ginger przypomina o kosztach związanych z procesem CoinJoin.



![screen](assets/fr/07.webp)



Następnie naciśnij **Start**, a następnie **New**, aby utworzyć nowe portfolio.



![screen](assets/fr/08.webp)



Następnie zapisz i potwierdź seedphrase.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Aby zwiększyć bezpieczeństwo, Ginger Wallet umożliwia dodanie passphrase.



![screen](assets/fr/11.webp)



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Ten passphrase, po dodaniu, będzie wymagany przy każdej próbie uzyskania dostępu do portfolio.



![screen](assets/fr/12.webp)



Ginger automatycznie aktywuje domyślny **CoinJoin** podczas tworzenia portfolio. Użytkownik jest o tym informowany i może dostosować ustawienia do swoich potrzeb.



![screen](assets/fr/13.webp)




### Ustawienia ogólne



Po utworzeniu pierwszego portfolio zostaniesz przeniesiony do Interface Wallet Ginger.



![screen](assets/fr/14.webp)



Aktywuj **Tryb dyskretny**, jeśli chcesz ukryć salda w swoich portfelach.



![screen](assets/fr/15.webp)



Możesz utworzyć wiele portfolio na Ginger Wallet. Wystarczy kliknąć na **Dodaj portfolio**.



![screen](assets/fr/16.webp)



Ginger obsługuje korzystanie z portfeli sprzętowych za pośrednictwem Bitcoin core standard Interface, chociaż bezpośrednia integracja z lub do portfela sprzętowego nie jest jeszcze dostępna.



Kompatybilne portfele sprzętowe obejmują (ale nie ograniczają się do) :




- BLOCKSTREAM Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- itp.



Teraz kliknij **Ustawienia**.



![screen](assets/fr/17.webp)



Te ustawienia są ustawieniami aplikacji w ogóle, a konfiguracje, które tam wprowadzisz, będą miały zastosowanie do wszystkich portfeli.



W **Ustawieniach** dostępne są zakładki :





- Ogólne**



![screen](assets/fr/18.webp)





- Wygląd



W tej zakładce można między innymi zmienić język, walutę i jednostkę wyświetlania opłat (BTC/Satoshi).



![screen](assets/fr/19.webp)





- Bitcoin**



Na tej karcie można włączyć Bitcoin Knots, aby działał po uruchomieniu aplikacji, wybrać sieć (Main/RegTest) i dostawcę opłat (Mempool Space/BLOCKSTREAM info/Full node) itp.



![screen](assets/fr/20.webp)





- Funkcje bezpieczeństwa**



W zakładce Bezpieczeństwo można włączyć uwierzytelnianie dwuskładnikowe, aktywować lub dezaktywować Tor, a nawet wyłączyć go po zamknięciu aplikacji Ginger.



![screen](assets/fr/21.webp)



**NB** :




- W przypadku uwierzytelniania dwuskładnikowego należy upewnić się, że aplikacja uwierzytelniająca obsługuje protokół SHA256 i 8-cyfrowe kody. Ginger Wallet wymaga 8-cyfrowego kodu 2FA w celu zwiększenia bezpieczeństwa. Ten dłuższy format sprawia, że kod jest znacznie trudniejszy do odgadnięcia lub złamania, oferując lepszą ochronę przed nieautoryzowanym dostępem.
- Domyślnie cały ruch sieciowy Ginger przechodzi przez Tor, eliminując potrzebę ręcznej konfiguracji. Jeśli Tor jest już aktywny w systemie, Ginger automatycznie nada mu priorytet.



Jednak po dezaktywacji Tora w ustawieniach prywatność pozostaje ogólnie zachowana, z wyjątkiem dwóch sytuacji:




- podczas CoinJoin, koordynator może połączyć wejścia i wyjścia z IP Address;
- podczas transmisji transakcji złośliwy węzeł, z którym się łączysz, może powiązać Twoją transakcję z Twoim adresem IP.



Nie zapomnij nacisnąć **Done** (w prawym dolnym rogu Coin) za każdym razem, aby zapisać ustawienia. Niektóre ustawienia wymagają ponownego uruchomienia Ginger Wallet.



Ponadto pasek wyszukiwania w górnej części portfela umożliwia wyszukiwanie i dostęp do dowolnego parametru itp.



![screen](assets/fr/22.webp)




### Konfiguracja portfela



W aplikacji można utworzyć kilka portfolio, dzięki czemu każde z nich można skonfigurować zgodnie z własnymi potrzebami. W tym celu należy kliknąć na **trzy kropki** przed nazwą portfela, a następnie na **Ustawienia portfela**.



![screen](assets/fr/23.webp)



Jak widać, oprócz parametru Wallet, będziesz mógł zobaczyć swoje UTXO (listę posiadanych tokenów), statystyki i informacje Wallet (na przykład rozszerzony klucz publiczny).



Aby powrócić do konfiguracji naszego portfolio, po kliknięciu parametrów portfolio zostaniesz przeniesiony do następujących zakładek:




- Ogólne** (gdzie można zmienić nazwę portfela) ;



![screen](assets/fr/24.webp)





- CoinJoin** (gdzie można dostosować ustawienia CoinJoin tego portfela) ;



![screen](assets/fr/25.webp)





- Narzędzia** (gdzie można sprawdzić seedphrase, ponownie zsynchronizować portfolio lub je usunąć).



![screen](assets/fr/26.webp)




## Odbieranie bitcoinów



Aby otrzymywać bitcoiny w Wallet na Ginger Wallet :




- naciśnij **Odbierz** ;



![screen](assets/fr/27.webp)





- Wprowadź nazwę źródła, z którym chcesz powiązać Address. Jest to etykieta umożliwiająca śledzenie płatności. Nie ma to żadnego wpływu na On-Chain; są to po prostu informacje o identyfikowalności przechowywane lokalnie w aplikacji;



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- kliknij małą strzałkę po lewej stronie **generate**, aby wybrać format Address (**SegWit** /**Taproot**), a następnie kliknij **generate**, aby wybrać generate i Address oraz kod QR.



![screen](assets/fr/29.webp)



Ten kod Address lub QR zostanie wykorzystany przez nadawcę do wysłania bitcoinów.



![screen](assets/fr/30.webp)




## Wysyłanie bitcoinów



Samouczek wideo dotyczący wysyłania za pośrednictwem Ginger Wallet.



![Vidéo](https://youtu.be/2nf5aAimfhg)



Aby to zrobić :




- Naciśnij przycisk **Wyślij**;
- wprowadź numer Address odbiorcy, kwotę do wysłania i etykietę;
- sprawdzić przegląd transakcji i potwierdzić wysłanie.



![screen](assets/fr/31.webp)




## Wydawanie bitcoinów



Łatwo jest kupować i sprzedawać Bitcoin z Ginger Wallet. W zaledwie kilku krokach możesz wydać swoje bitcoiny.



### Kup bitcoiny



Użytkownicy Ginger Wallet mogą kupować bitcoiny.





- Naciśnij przycisk **Kup**. Przycisk ten pozostaje widoczny nawet wtedy, gdy Wallet jest pusty.



![screen](assets/fr/32.webp)





- Wybierz swój kraj, a nawet stan (w niektórych regionach, takich jak Kanada), przed przystąpieniem do zakupu Bitcoin. W rzeczywistości, po kliknięciu funkcji **Kup** po raz pierwszy, będziesz musiał również określić swój region.



![screen](assets/fr/33.webp)



Naciśnij **Kontynuuj**, aby przejść przez proces zakupu.





- Następnie wprowadź kwotę bitcoinów, które chcesz kupić w dedykowanym polu. Możesz również wybrać walutę transakcji.



![screen](assets/fr/34.webp)



Każda waluta ma minimalny i maksymalny limit zakupu. Na przykład w USD maksymalny limit wynosi 30 000 USD.



Jeśli dokonałeś już zakupu, możesz wyświetlić historię transakcji, klikając przycisk **Poprzednie zamówienia**. Wyświetlona zostanie lista wcześniejszych transakcji i ich status.





- Wybierz ofertę odpowiednią dla siebie.



W tym momencie zobaczysz listę wszystkich dostępnych ofert. Dla każdej oferty dostępne są :




 - nazwa dostawcy (1) ;
 - liczba bitcoinów odpowiadająca wcześniej wprowadzonej kwocie, metoda płatności i opłata za zakup (2) ;
 - przycisk **Accept** (3).



![screen](assets/fr/35.webp)



Opłaty wskazane w ofercie nie stanowią dodatkowego kosztu. Są one już wliczone w całkowitą kwotę oferty.



W prawym górnym rogu Coin ekranu z etykietą **All** można filtrować oferty według metody płatności. Wybrana metoda płatności zostanie ustawiona domyślnie, ale można ją zmienić w dowolnym momencie.



![screen](assets/fr/36.webp)



Jeśli znajdziesz odpowiednią ofertę, kliknij przycisk **Accept**, aby kontynuować zakup. Zostaniesz przekierowany na stronę sprzedawcy, gdzie będziesz mógł sfinalizować transakcję.



### Sprzedaż bitcoinów



Użytkownicy Ginger Wallet mogą sprzedawać Bitcoin. Przycisk **Sprzedaj** jest widoczny tylko wtedy, gdy w portfelu dostępne są środki.





- Kliknij przycisk **Sprzedaj**.



![screen](assets/fr/37.webp)





- Podobnie jak w przypadku opcji **Kup**, podczas korzystania z funkcji Sprzedaj po raz pierwszy, należy wybrać kraj przed przystąpieniem do sprzedaży Bitcoin.





- Następnie musisz wprowadzić ilość Bitcoinów, które chcesz sprzedać. Możesz wprowadzić tę kwotę w BTC lub w walucie fiducjarnej, takiej jak dolar amerykański (USD).





- Gdy to zrobisz, zobaczysz listę dostępnych ofert. Wybierz ofertę sprzedaży, która Ci odpowiada, a następnie kliknij **Accept**, aby kontynuować.





- Teraz należy sfinalizować transakcję:
 - Po zaakceptowaniu oferty zostaniesz przekierowany na stronę dostawcy;
 - Postępuj zgodnie z instrukcjami na stronie dostawcy;
 - W pewnym momencie otrzymasz od odbiorcy Address i dokładną kwotę do wysłania;
 - Następnie wróć do Ginger Wallet, aby kontynuować proces;
 - Po powrocie do Ginger Wallet pojawi się okno dialogowe umożliwiające kontynuowanie poprzez kliknięcie **Wyślij**.



Spowoduje to otwarcie ekranu **Wyślij** ze wstępnie wypełnionym Address odbiorcy i kwotą. Można również użyć przycisku **Wyślij** na ekranie głównym. Chociaż transakcję można wysłać ręcznie, zalecamy wykonanie jej za pomocą okna dialogowego w celu zoptymalizowania procesu.



## Wykonaj CoinJoin na Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Chroń poufność swoich bitcoinów dzięki **CoinJoin**, zintegrowanemu bezpośrednio z Ginger Wallet. Wallet wykorzystuje **WABISABI**, protokół Chaumian CoinJoin zaprojektowany w celu ułatwienia bardziej dostępnych i wydajnych coinjoinów.



Do ciebie należy wybór strategii CoinJoin (automatycznej lub ręcznej), która najbardziej ci odpowiada.



Ginger CoinJoin jest gotowy do użycia natychmiast po pobraniu (nie są wymagane żadne dodatkowe kroki). Ginger CoinJoin działa automatycznie w tle, aby chronić prywatność użytkownika przy każdej transakcji. W praktyce czytnik CoinJoin pojawi się za każdym razem, gdy masz saldo, które można zanonimizować.



Jeśli chodzi o ręczne uruchamianie CoinJoin, jest to operacja jednym kliknięciem. Uruchom rundę i poczekaj, aż transakcja CoinJoin zostanie utworzona i potwierdzona. Wynik anonimizacji zostanie wyświetlony w Interface.



Można wykonać kilka miksów, aż do osiągnięcia pożądanego poziomu anonimowości. Można również wykluczyć określone części z miksowania.



Domyślnie Ginger korzysta z własnego koordynatora ze wszystkimi wstępnie skonfigurowanymi parametrami i gwarantowanymi opłatami. Coinjoiny tokenów o wartości powyżej 0,03 BTC wiążą się z opłatą koordynatora w wysokości 0,3% oprócz opłaty Mining. Wpisy o wartości 0,03 BTC lub mniejszej, a także remiksy, są zwolnione z opłat koordynatora, nawet po pojedynczej transakcji. Dlatego płatność dokonana za pomocą środków CoinJoin pozwala zarówno nadawcy, jak i odbiorcy na remiksowanie swoich monet bez ponoszenia opłat koordynatora.



Ginger preferuje coinjoiny z większą liczbą uczestników niż mniejsze, szybsze rundy. Większe coinjoiny oferują większą anonimowość, niższe koszty i większą wydajność przestrzeni BLOCK.




## Bezpieczeństwo i najlepsze praktyki



Dążenie do decentralizacji i zachowania prywatności wymaga przyjęcia kilku najlepszych praktyk:




- Zawsze przechowuj seedphrase w bezpiecznym miejscu poza siecią;
- W przypadku utraty komputera lub podejrzenia nieautoryzowanego dostępu należy natychmiast utworzyć nowy Wallet. Przenieś swoje środki do nowego portfela i usuń stary;
- Użyj innego Address dla każdego odbioru, aby uniknąć ponownego użycia adresów;
- Aplikacje portfolio należy zawsze pobierać wyłącznie z oficjalnego konta GitHub lub oficjalnej strony internetowej.



Teraz wiesz już, jak korzystać z aplikacji Ginger Wallet do wysyłania, odbierania i wydawania bitcoinów.



Jeśli uważasz ten poradnik za przydatny, zostaw mi kciuk Green poniżej. Zachęcamy do udostępnienia tego artykułu za pośrednictwem mediów społecznościowych. Dziękuję bardzo!



Sugeruję również zapoznanie się z tym samouczkiem na temat korzystania z aplikacji komputerowej Liana do wysyłania i odbierania bitcoinów, a także wdrażania zautomatyzowanego planu spadkowego.



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04