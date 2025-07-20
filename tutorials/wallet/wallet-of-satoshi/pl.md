---
name: Wallet z Satoshi
description: Najprostszy Wallet do rozpoczęcia działalności
---
![cover](assets/cover.webp)

_Ten poradnik został napisany przez_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Pobieranie, konfigurowanie i używanie Wallet z Satoshi


Wallet z Satoshi to Lightning Network Wallet, opiekuńczy i bardzo prosty w użyciu.

Na potrzeby kursu [BTC105 - Finding Now](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5) jest on używany do kuponów Redeem Lightning Network.


**Zawsze pamiętaj**: _nie klucze, nie monety_


Portfele powiernicze nie pozwalają użytkownikom na pełną kontrolę nad swoimi środkami. Zazwyczaj nie są one zalecane, z wyjątkiem początkujących graczy. WoS powinien być używany jako przejściowy Wallet lub do przechowywania kieszonkowego, a nie do długoterminowego gromadzenia środków.


---

Wallet z Satoshi (WoS) jest produktem powierniczym, ale ma pewną reputację. Możemy rozsądnie zwrócić się do narzędzia takiego jak WoS, na przykład, aby zwiększyć naszą zdolność do otrzymywania płynności. Tymczasowo delegujemy do WoS "brudną robotę" zarządzania płynnością kanałów dla nas. Po osiągnięciu określonej kwoty, opróżnimy WoS On-Chain do naszego Wallet.


**WARNING⚠️: Zaleca się przeczytanie samouczka w całości przed kontynuowaniem**


### Pobieranie Wallet z Satoshi


Przejdź do Sklepu Play i pobierz WoS


![image](assets/it/01.webp)


**Uwaga:** WoS można pobrać tylko z oficjalnych sklepów. Jeśli system operacyjny urządzenia jest zaprogramowany, przed otwarciem WoS nastąpi weryfikacja przez sam system operacyjny. Po zakończeniu weryfikacji wybierz opcję _Open_.


![image](assets/it/02.webp)


Wallet z Satoshi otwiera się z następującym ekranem i konieczne jest kliknięcie na _Start_


![image](assets/it/03.webp)


### Rejestracja konta w WoS


W tym momencie Wallet już działa, ale dla większego bezpieczeństwa przystępujemy do ustawienia loginu: będzie on potrzebny do odzyskania środków w przypadku awarii lub utraty urządzenia. Dlatego wybierz menu w lewym górnym rogu.


![image](assets/it/04.webp)


Otworzy się całe okno menu, w którym należy ustawić wyłącznie walutę (Wallet z Satoshi domyślnie prezentuje dolara amerykańskiego jako walutę referencyjną) i kolor motywu (jasny/ciemny), zgodnie z gustem. Nie należy używać innych poleceń.


Ponieważ WoS jest narzędziem powierniczym, nie możemy wykonać kopii zapasowej Wallet za pomocą frazy Mnemonic, ale możemy umożliwić WoS odzyskanie naszych środków, w przypadku utraty lub nieużywania urządzenia mobilnego, klikając _Login/Register_

Pojawi się okno z prośbą o podanie adresu e-mail Address. Może to być **poczta Proton** (zalecane), ale musi być funkcjonalna, ponieważ pozwoli nam odzyskać środki w Wallet w przypadku utraty/kradzieży lub uszkodzenia telefonu komórkowego.


![image](assets/it/08.webp)


Wallet z Satoshi wysłał wiadomość na wskazaną skrzynkę e-mail.


![image](assets/it/09.webp)


W skrzynce pocztowej znajdziemy dwa słowa, które musimy wpisać, przepisując je, w miejscu udostępnionym przez aplikację.


- nie aktywuj tłumacza: słowa są i muszą pozostać w języku angielskim**
- przepisz dwa słowa zwracając uwagę na wielkie/małe litery**


![image](assets/it/10.webp)


Po przepisaniu dwóch słów kliknij przycisk _OK_.


![image](assets/it/11.webp)


Wynikiem powinien być obraz pojawiający się u góry, z symbolem znacznika wyboru do weryfikacji.


![image](assets/it/12.webp)


podczas gdy w sekcji ustawień czerwony pasek _Login/Register_ wyświetla teraz adres e-mail użytkownika Address.


![image](assets/it/13.webp)


### Otrzymywanie płatności


Aby odbierać w WoS, kliknij _Receive_, a pojawi się seria poleceń.


![image](assets/it/14.webp)


Możesz otrzymać


- przez LN-Address **a**
- poprzez LN, ustawiając Invoice **b**
- on chain (WoS obsługuje sieć Bitcoin, ale z płatnymi podmianami) **c**
- skanując kod QR urządzenia LNurl-p **d**


![image](assets/it/15.webp)


### Tworzenie Invoice


Kliknij na _Receive_ i wybierz polecenie z symbolem Lightning Network.


![image](assets/it/16.webp)


Pojawi się menu tworzenia Invoice, w którym klikamy _Add Amount_, aby wpisać dokładną kwotę i dodać opis, w tym przykładzie "Mój pierwszy Invoice".


![image](assets/it/17.webp)


Za pomocą klawiatury ustawiamy kwotę.


![image](assets/it/18.webp)


aby następnie otrzymać płatność Invoice. Otrzymana płatność wygląda następująco:


![image](assets/it/19.webp)


### Odbiór z punktu sprzedaży


Wallet z Satoshi ma domyślną funkcję, która czyni go szczególnie odpowiednim dla sprzedawców: POS. Zobaczmy, jak ją aktywować.


Na ekranie głównym wybierz menu w prawym górnym rogu.


![image](assets/it/20.webp)


Następnie wybierz opcję _Point of Sale_.


![image](assets/it/21.webp)


W najnowszej wersji WoS należy wybrać opcję _Keypad_.


![image](assets/it/22.webp)

a następnie wpisz kwotę na klawiaturze, w poniższym przykładzie równą 10 centów / 118 Sats. Dodaj opis kolekcji, w tym przypadku "moja druga z POS". Zaświeci się duży przycisk Green, który należy kliknąć

![image](assets/it/23.webp)


do generate Invoice i pokazać go - na przykład - klientowi.


![image](assets/it/24.webp)


Ta płatność jest również pobierana!


![image](assets/it/25.webp)


### Wysyłanie płatności


Prostota jest mocną stroną głównego ekranu WoS. Aby zapłacić Invoice, kliknij _Wyślij_


![image](assets/it/26.webp)


Przy pierwszym użyciu WoS prosi o pozwolenie na dostęp do kamery


![image](assets/it/27.webp)


Od tego momentu kamera aktywuje się


![image](assets/it/28.webp)


Kadrując Invoice, widzimy, że zażądano płatności w wysokości 210 Sats. Odczytywany jest również opis, jeśli żądający go ustawił. Ten ekran jest podsumowaniem, a także prośbą o potwierdzenie: WoS "prosi o autoryzację" wysłania płatności, która jest udzielana poprzez kliknięcie przycisku Green _Wyślij_


![image](assets/it/29.webp)


Gdy płatność dotrze do miejsca docelowego, WoS powiadomi o tym na tym ekranie


![image](assets/it/30.webp)


Na ekranie głównym po kliknięciu na _History_ (tuż pod saldem) pojawi się lista transakcji


![image](assets/it/31.webp)


#### Odzyskiwanie konta WoS


Teraz zobaczymy, jak zainstalować WoS na nowym urządzeniu; będzie to również przydatne w przypadku kradzieży, utraty lub niemożności obsługi telefonu komórkowego, na którym wcześniej zainstalowano Wallet. Po ponownej instalacji należy powtórzyć procedurę rejestracji konta, z jednym wariantem: na końcu prośby o zalogowanie się przy użyciu wcześniej ustawionego adresu e-mail, WoS pojawi się w następujący sposób:


![image](assets/it/33.webp)


Komunikat ostrzega, że wysłano wiadomość e-mail z procedurą reaktywacji konta. Należy otworzyć swoją skrzynkę e-mail.


**WAŻNE: otwórz wiadomość e-mail z komputera lub w każdym razie z urządzenia innego niż to, na którym zamierzasz odzyskać konto WoS. W skrzynce odbiorczej znajdujemy wiadomość, która pokazuje nam kod QR do obramowania


![image](assets/it/34.webp)


Po obramowaniu kodu QR na stronie głównej WoS pojawi się odzyskane konto wraz z saldem i historią.