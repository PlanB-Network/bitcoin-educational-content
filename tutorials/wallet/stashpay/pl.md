---
name: StashPay
description: Minimalistyczny Bitcoin Wallet dla każdego
---

![cover](assets/cover.webp)



Doświadczenie użytkownika jest kluczowym czynnikiem w przyjmowaniu rozwiązań Bitcoin na całym świecie. Zapewnienie płynnego, prostego i technicznie nieobciążonego doświadczenia jest priorytetem dla wielu portfeli i platform Exchange. Pod tym względem StashPay wyróżnia się minimalistycznym podejściem, jednocześnie demonstrując moc Lightning Network.



W tym samouczku przyjrzymy się temu portfolio, aby dowiedzieć się, jak to działa i jak jest idealne dla małych firm lub osób prowadzących jednoosobową działalność gospodarczą.



## Rozpoczęcie korzystania ze StashPay



StashPay to samoobsługowy Wallet Lightning, znany przede wszystkim ze swojego minimalistycznego, skoncentrowanego na użytkowniku doświadczenia.  Dzięki temu Wallet nie potrzebujesz żadnej wiedzy technicznej, aby otrzymać i wysłać swoje pierwsze satoshis.



StashPay to projekt open-source opracowany w React Native i ma na celu rozwiązanie problemu wysokich opłat transakcyjnych nawet w przypadku transakcji w głównym łańcuchu protokołu Bitcoin. Jest on dostępny jako aplikacja mobilna na platformy Android i iOS za pośrednictwem linków do pobrania znajdujących się na [stronie internetowej](https://stashpay.me/).



![introduce](assets/fr/01.webp)



Ważne jest, aby pobrać aplikację na Androida ze strony internetowej, ponieważ nie jest ona dostępna w sklepie Google Play.


Po zakończeniu pobierania należy przyznać niezbędne uprawnienia, aby można było zainstalować aplikację na telefonie z systemem Android.



Po zainstalowaniu aplikacji StashPay utworzy dla Ciebie początkowy Bitcoin Wallet przy pierwszym otwarciu. Przed każdą transakcją zalecamy wykonanie kopii zapasowej tego Wallet. Poniżej znajdują się wszystkie nasze wskazówki dotyczące prawidłowego tworzenia kopii zapasowych fraz odzyskiwania.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Uzyskaj dostęp do ustawień StashPay, klikając ikonę "Ustawienia", a następnie kliknij opcję **Utwórz kopię zapasową**. Następnie autoryzuj wyświetlanie fraz odzyskiwania. Nie kopiuj fraz odzyskiwania do schowka telefonu, ponieważ mogą one być dostępne dla innych nieuczciwych aplikacji zainstalowanych na telefonie.



![backup](assets/fr/02.webp)



Możesz także odzyskać Bitcoin Wallet, którego już używasz, klikając opcję **Odzyskaj Wallet** i wprowadzając 12 lub 24 słowa odzyskiwania.



### Odbierz swoje pierwsze satoshi na StashPay



Na ekranie głównym kliknij przycisk **Odbierz** i ustaw kwotę większą niż określona na czerwono. W naszym przypadku nie możemy otrzymać mniej niż 0,11 USD za pomocą StashPay Wallet.



![receive](assets/fr/03.webp)



Po zdefiniowaniu kwoty można kliknąć przycisk **Utwórz Invoice**, a następnie zeskanować lub skopiować Invoice, aby wysłać go do nadawcy satoshis.



![receive_sats](assets/fr/04.webp)



Historię transakcji można wyświetlić, klikając ikonę "zegara" na stronie głównej.



![network_fee](assets/fr/05.webp)



Zauważyłeś, że aby otrzymać satoshis, będziesz musiał uiścić opłatę sieciową. Opłaty te zostaną odjęte od satoshis, które zamierzasz otrzymać. Dzieje się tak, ponieważ StashPay jest Wallet opartym na Breez Development Kit. Aby otrzymać satoshis z wolną od węzłów Lightning implementacją zestawu, Breez obciąży klienta (w naszym przypadku StashPay) `0,25% + 40 satoshis`. Dowiedz się więcej w naszym samouczku Misty Breez.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Wysyłaj bitcoiny za pomocą StashPay



Wysyłanie bitcoinów za pomocą StashPay jest dość intuicyjne dzięki minimalistycznemu Interface. Na ekranie głównym kliknij przycisk **Wyślij**. Zeskanuj kod QR lub wklej Address, do którego chcesz wysłać satoshi. StashPay automatycznie wykryje łańcuch protokołu Bitcoin, do którego chcesz wysłać bitcoiny.



![send](assets/fr/06.webp)



Ponieważ StashPay jest Wallet opartym na Breez Development Kit, korzysta z interesującej zalety: wysyłania bitcoinów w głównym łańcuchu przy niskich kosztach. Breez wykorzystuje usługę Boltz do przeprowadzania transakcji między różnymi łańcuchami protokołu Bitcoin, umożliwiając klientom, którzy wdrażają zestaw deweloperski, korzystanie z tej usługi bezpośrednio w swojej aplikacji.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Breez SDK narzuca jednak minimalną kwotę, przy której można wysyłać bitcoiny do Address w głównym łańcuchu.



![onchain](assets/fr/07.webp)



Możesz również wysłać bitcoiny za pomocą Lightning Address swojego odbiorcy. Sprawdź szczegóły transakcji, a następnie potwierdź, klikając przycisk **Wyślij**.



![confirm](assets/fr/08.webp)



## Więcej konfiguracji



W ustawieniach StashPay można dostosować konfiguracje, aby spersonalizować korzystanie z Wallet.



StashPay pozwala Exchange satoshis w oparciu o lokalną walutę do wyboru. Kliknij opcję **Waluty**, a następnie wyszukaj swoją walutę na liście +113 walut oferowanych przez StashPay.



![currencies](assets/fr/09.webp)



W menu **Opcje odbioru** znajdziesz wszystkie ustawienia dotyczące odbierania bitcoinów za pomocą StashPay. Na przykład, wybierając **Wybierz Lightning lub Onchain**, włącz Wallet, aby otrzymywać bitcoiny z głównego łańcucha.



![receive-onchain](assets/fr/10.webp)



Opcja **Scan OnChain addresses** pozwala odświeżyć saldo Wallet poprzez sprawdzenie wszystkich UTXO (bitcoinów, których jeszcze nie wydałeś) powiązanych z różnymi adresami.



![rescan](assets/fr/11.webp)



Menu **Export log** zawiera listę wszystkich działań infrastruktury Breez i Boltz dotyczących transakcji i wymiany atomowej między różnymi łańcuchami protokołów Bitcoin.



![export](assets/fr/12.webp)



Właśnie zapoznałeś się z minimalistycznym Bitcoin Wallet od StashPay. Jeśli ten poradnik okazał się przydatny, polecamy nasz poradnik, jak zacząć korzystać z Bitcoin i zarobić swoje pierwsze bitcoiny.



https://planb.network/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f