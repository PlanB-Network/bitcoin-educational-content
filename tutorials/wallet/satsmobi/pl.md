---
name: Sats.mobi

description: Dostępna przez Telegram usługa Wallet
---

![cover](assets/cover.webp)


_Ten poradnik został napisany przez_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi to Wallet działający na Telegramie, posiadający wszystkie funkcje Lightning Network (opiekuńczego) Wallet oraz szereg bardzo zabawnych funkcji. Wywodzi się z Fork nieistniejącego już LightningTipBota, dziedzicząc wszystkie jego funkcje i dodając bardziej aktualne, dzięki czemu jest bardziej nowoczesny. Podobnie jak LNTipBot, Sats.Mobi również przyjmuje filozofię open-source. Wallet można skonfigurować i zarządzać nim niezależnie, klonując go z tego [repozytorium](https://github.com/massmux/SatsMobiBot).


Jeśli wolisz używać go po prostu, rozpoczęcie czatu na Telegramie ujawni, że jest to bot.


## Ustawienia

Na pasku wyszukiwania Telegram wyszukaj "satsmobi", a pojawi się link do [bota](@SatsMobiBot).


**Uwaga**: Jeśli nie masz pewności co do wyszukiwania przez Telegram, uzyskaj bezpieczny dostęp do bota za pomocą następującego [linku](https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Aby rozpocząć, wystarczy nacisnąć przycisk _START_


![image](assets/it/02.webp)


Aby przeglądać Wallet, można wybrać _Menu_ w lewym dolnym rogu.


![image](assets/it/03.webp)


Teraz wybierz _/help_ wśród głównych poleceń.


![image](assets/it/04.webp)


Sats.Mobi wita nas wyświetlając wiadomość, w której wymienione są wszystkie główne funkcje. Po uruchomieniu bot utworzył również LN Address, powiązany z wybranym uchwytem na Telegramie (który jest domyślnie unikalny). Widoczne są polecenia wysyłania i odbierania Sats za pomocą tego Wallet, a także inne funkcje, które zobaczymy później. Warto również spojrzeć na menu _/advanced_


![image](assets/it/05.webp)


Warto zauważyć, że Sats.Mobi stworzył również anonimowego LN Address, który ma być używany do uzyskania prywatności. Bot działa z poleceniami: wystarczy kliknąć odpowiednie słowo lub wpisać ukośnik "/" na pasku wiadomości, a następnie polecenie, które chcesz wykonać. Nawet jeśli Wallet został właśnie utworzony, wybierz na przykład _/transakcje_


![image](assets/it/06.webp)


Polecenie to wyświetla listę ostatnich transakcji, w tym konkretnym przypadku równą zero.


![image](assets/it/07.webp)


## Odbiór Sats

Polecenie utworzenia Invoice i otrzymania Sats to _/invoice_. Sats.Mobi działa wyłącznie w Satoshi, najmniejszej jednostce Bitcoin; dlatego, aby utworzyć Invoice, konieczne jest wpisanie kwoty w Sats na pasku wiadomości, a następnie wysłanie jej na czacie z botem.

![image](assets/it/08.webp)


W poniższym przykładzie dokonano wyboru, aby otrzymać kwotę 210 Sats.


![cover](assets/it/09.webp)


Po kilku chwilach oczekiwania na przygotowanie Invoice, jest on dostępny jako tekst i jako kod QR. Po opłaceniu Invoice, Wallet pokaże saldo. Jeśli z jakiegoś powodu suma nie jest aktualizowana, należy wpisać _/balance_ i nacisnąć klawisz `enter`.


![image](assets/it/10.webp)


## Wysyłanie Sats


Choć Sats są niezwykle cennym nabytkiem, z którym nie należy rozstawać się lekką ręką, Sats.Mobi czyni tę część atrakcyjną, przeprowadzenie krótkich testów (tj. kilku próbnych transakcji) nie będzie problemem.


### Płacenie Invoice


Najprostszym sposobem na opłacenie Invoice jest skopiowanie ciągu wiadomości `lnbc1xxxxx` i wklejenie go do paska wiadomości po wpisaniu komendy _/pay_. **Prawidłowa składnia** wymaga pozostawienia spacji po komendzie.


![image](assets/it/11.webp)


Wallet wysyła wiadomość z prośbą o potwierdzenie. Po kliknięciu na _Pay_, Invoice zostanie opłacony.


![image](assets/it/12.webp)


Sats.Mobi może polegać na wydajnym i dobrze połączonym węźle Lightning, rzadko kiedy płatności zawodzą, ponieważ zawsze udaje mu się znaleźć prawidłowy routing.


### Wygodne płacenie z telefonu komórkowego


Przeglądając Telegram, Sats.Mobi jest również dostępny na urządzeniach mobilnych. Najwygodniejszą funkcją do płacenia za pomocą telefonu komórkowego jest skanowanie kodu QR, ale Wallet nie ma go z założenia, ponieważ nie jest samodzielną aplikacją, ale znajduje się w sieci społecznościowej. Sats.Mobi jest zatem zaprogramowany tak, aby w jak największym stopniu ułatwić korzystanie z urządzeń mobilnych: może dekodować obraz, taki jak zdjęcie zrobione z kodu QR Invoice, którym chcesz zapłacić.


Załóżmy na przykład, że chcesz zapłacić Invoice w wysokości 50 Sats.


![image](assets/it/20.webp)


Gdy zostanie nam to pokazane, możemy zrobić zdjęcie powiązanego kodu QR.


![image](assets/it/21.webp)


Następnie otwieramy Telegram na telefonie komórkowym i na czacie z Sats.Mobi załączamy właśnie zrobione zdjęcie kodu QR


![cover](assets/it/22.webp)


Po wybraniu wysyłamy go do bota:


![image](assets/it/23.webp)

Sats.Mobi dekoduje zdjęcie i **natychmiast przedstawia żądanie płatności** z prawidłowym opisem. Czat prosi o potwierdzenie, aby kontynuować należy nacisnąć _/pay_

![image](assets/it/24.webp)


Poczekaj chwilę, aby umożliwić przetworzenie płatności.


![image](assets/it/25.webp)


Invoice za 50 Sats został opłacony, wynik osiągnięty bez użycia kamery i jej zintegrowanej funkcji skanowania.


### Sats.Mobi w grupie Telegram


![image](assets/it/27.webp)


Wśród funkcji, które rozsławiły LNTipBot i które Sats.Mobi wprowadza do Telegrama, jest ta, która sprawia, że doświadczenie jest zabawne i interaktywne dla członków grupy.

Właściciele mogą zaprosić bota do dołączenia do czatu grupowego, a następnie nominować Sats.Mobi jako administratora. Od tego momentu zaczyna się zabawa, ponieważ członkowie mogą zacząć nagradzać innych użytkowników za ich wkład w grupę.


- _/tip_ dodaje napiwek odpowiadając na wiadomość;
- _/send_ wysyła środki określając LN Address lub uchwyt Telegram jako odbiorcę;
- _/faucet_ (w menu _/advanced_) umożliwia tworzenie serii wskazówek, które najszybsi członkowie grupy mogą zbierać, klikając na _/collect_;
- _/tipjar_ (w menu _/advanced_) tworzy inny typ dystrybucji, który może być wysyłany do użytkowników w grupie.


Każde z tych poleceń ma swoją składnię, która jest wyjaśniona w głównym menu poleceń.


A jeśli nie jesteśmy właścicielem grupy? Nie ma problemu: wystarczy poprosić założyciela o zaproszenie Sats.Mobi, dodać go jako administratora grupy i gotowe!


## Punkt sprzedaży (POS)


Kiedy Sats.Mobi jest uruchamiany po raz pierwszy, bot tworzy również kolejną funkcję dla użytkownika: ** POS**. "Urządzenie" jest aktywowane przez użytkownika za pomocą polecenia _/pos_ lub poprzez kliknięcie odpowiedniego przycisku w konsoli w prawym dolnym rogu. W rzeczywistości POS jest aplikacją internetową, która otwiera się jako wyskakujące okienko na czacie Telegrama


![image](assets/it/14.webp)


Interface wyświetla osobisty uchwyt Telegram użytkownika w lewym górnym rogu i jest używany tak, jak wszystkie POS: wpisując kwotę na klawiaturze. Załóżmy teraz, że chcemy pobrać 21 eurocentów za usługę. Wiedząc, że Sats.Mobi natywnie zarządza tylko Sats, nie jest łatwo dokonać konwersji w głowie. Wręcz przeciwnie, POS wyświetla euro jako jednostkę rozliczeniową, pokazując jednocześnie równowartość w Satoshi.


![image](assets/it/15.webp)

Kliknięcie przycisku _/OK_ powoduje wyświetlenie Invoice, który można pokazać klientowi za pomocą kodu QR lub wysłać jako ciąg znaków za pośrednictwem komunikatora internetowego, aby można było zapłacić.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Oczywiście POS jest również dostępny na telefonach komórkowych, z dostępem w taki sam sposób, jak pokazano wcześniej.


![image](assets/it/18.webp)


Jest również dobrze wyświetlany na ekranie telefonu komórkowego:


![image](assets/it/19.webp)


## Dodatkowe funkcje


Istnieją inne funkcje, które uzupełniają ofertę Sats.Mobi Wallet, który, jak widzieliśmy, rozszerza koncepcję Wallet poza operacje odbierania i wysyłania płatności:


- _/nostr_: aby połączyć Wallet z własnym użytkownikiem Nostr w celu odbierania zapów;
- _/cashback_: pokazuje kod, który można przedstawić sprzedawcy w celu uzyskania zwrotu gotówki za zakup;
- _/buy_: uruchamia procedurę prowadzoną przez bota, która umożliwia zakup Sats za euro;
- _/activatecard_: żądanie aktywacji karty debetowej NFC, którą można doładować za pomocą Sats.Mobi Wallet i dla której można aktywować powiadomienia;
- _/link_: tworzy link do własnego Zeusa lub Blue Wallet, które mogą być używane jako piloty do tego Wallet.


## Wnioski

Sats.Mobi to przyjemny i zabawny Wallet, który przywołuje doświadczenia z LNTipBot przy użyciu bardziej zaawansowanych funkcji LNBits. Należy jednak pamiętać, że **jest to usługa powiernicza**. Dlatego powinien być używany do przechowywania bardzo niewielu Sats, nie jest to główny Wallet dla funduszy Lightning Network. Istnieje również wewnętrzny limit pojemności, równy 500 000 Sats, którego zaleca się nie przekraczać.


Jeśli szukasz portfeli Lightning Network, które nie podlegają ograniczeniom, zdecydowanie warto przyjrzeć się innym produktom.


---
### Dokumentacja


- [Github](https://github.com/massmux/SatsMobiBot)
- Lista odtwarzania [wideo](https://www.youtube.com/results?search_query=Sats.mobi) demo