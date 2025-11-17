---
name: Serwer BTCPay - Umbrel
description: Instalowanie i używanie serwera BTCPay na Umbrel do akceptowania Bitcoin i Lightning
---

![cover](assets/cover.webp)



W ekosystemie Bitcoin przyjmowanie płatności stanowi poważne wyzwanie zarówno dla sprzedawców, jak i firm. Tradycyjne rozwiązania, czy to bankowe (karty kredytowe, Stripe, PayPal), czy nawet Bitcoin (BitPay, Coinbase Commerce), narzucają pośredników, którzy pobierają znaczne opłaty, gromadzą poufne dane biznesowe i mogą blokować lub cenzurować transakcje według własnego uznania. Ta zależność jest sprzeczna z podstawowymi zasadami Bitcoin dotyczącymi decentralizacji, poufności i suwerenności finansowej.



BTCPay Server staje się odpowiedzią open-source na ten problem. Ten samoobsługowy procesor płatności zamienia własny węzeł Bitcoin w profesjonalną infrastrukturę, bez pośredników, bez dodatkowych opłat za przetwarzanie i bez uszczerbku dla prywatności. Opracowany przez globalną społeczność współpracowników od 2017 roku, BTCPay Server umożliwia otrzymywanie płatności Bitcoin i Lightning bezpośrednio do portfeli, zachowując pełną kontrolę nad swoimi środkami przez cały czas.



Tradycyjnie instalacja BTCPay Server wymaga zaawansowanych umiejętności technicznych: Konfiguracji serwera Linux, opanowania Dockera, zarządzania certyfikatami SSL i bezpieczeństwa sieci. Umbrel rewolucjonizuje to podejście dzięki instalacji jednym kliknięciem bezpośrednio zintegrowanej z węzłem Bitcoin i Lightning. To uproszczenie sprawia, że to, co wcześniej było zarezerwowane dla doświadczonych techników, jest dostępne dla każdego.



**Ważne do zrozumienia**: Serwer BTCPay na Umbrel działa domyślnie tylko w sieci lokalnej. Możesz tworzyć faktury, akceptować płatności Lightning i Bitcoin oraz zarządzać swoją księgowością z dowolnego urządzenia podłączonego do sieci domowej (komputer, smartfon, tablet). Ta konfiguracja jest idealna do rozliczania usług osobistych, zarządzania płatnościami twarzą w twarz lub korzystania z serwera BTCPay z sieci lokalnej. Z drugiej strony, aby zintegrować BTCPay Server ze sklepem internetowym, który jest publicznie dostępny w Internecie, wymagana będzie dodatkowa konfiguracja z publiczną ekspozycją (omówimy tę kwestię na końcu samouczka).



Ten samouczek przeprowadzi Cię przez pełną instalację BTCPay Server na Umbrel, konfigurację węzła Bitcoin wallet i Lightning, tworzenie i opłacanie faktur oraz zarządzanie raportowaniem księgowym. Dowiesz się, jak efektywnie korzystać z BTCPay Server w sieci lokalnej, a następnie przyjrzymy się rozwiązaniom do publicznego wyświetlania, jeśli chcesz zintegrować go z witryną e-commerce.



## Wymagania wstępne



Aby skorzystać z tego samouczka, musisz mieć poprawnie zainstalowany i skonfigurowany Umbrel. Jeśli jeszcze tego nie zrobiłeś, zapoznaj się z naszym samouczkiem dotyczącym instalacji Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Węzeł Bitcoin Core musi być w pełni zsynchronizowany z łańcuchem bloków (100% w aplikacji Bitcoin firmy Umbrel). Ta początkowa synchronizacja trwa zwykle od 3 dni do 2 tygodni, w zależności od posiadanego sprzętu i połączenia internetowego.



Aby akceptować natychmiastowe płatności Lightning, musisz również zainstalować LND (Lightning Network Daemon) na Umbrel. Zapoznaj się z naszym samouczkiem dotyczącym instalowania i konfigurowania LND na Umbrel, jeśli chcesz włączyć tę funkcję.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Należy zapewnić co najmniej 50 GB wolnego miejsca na dysku dla serwera BTCPay, jego baz danych i danych Lightning. Zdecydowanie zaleca się stabilne połączenie internetowe za pomocą kabla Ethernet, aby uniknąć rozłączeń.



## Instalacja serwera BTCPay na platformie Umbrel



Z poziomu interfejsu Umbrel (`umbrel.local`) przejdź do sklepu App Store i wyszukaj "BTCPay Server" w kategorii Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Kliknij Zainstaluj. Umbrel automatycznie sprawdzi, czy Bitcoin Core i LND są zainstalowane, a następnie rozpocznie wdrażanie (2-5 minut).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Po zainstalowaniu otwórz aplikację. Konieczne będzie utworzenie konta administratora z silnymi poświadczeniami.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Po utworzeniu konta serwer BTCPay natychmiast wyświetli monit o skonfigurowanie pierwszego sklepu. Wybierz nazwę firmy i walutę referencyjną (EUR, USD lub BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Dostęp do serwera BTCPay w sieci lokalnej



Serwer BTCPay jest dostępny z dowolnego urządzenia w sieci lokalnej (WiFi lub Ethernet). Dostęp z przeglądarki do :



```url
http://umbrel.local
```



Lub bezpośrednio do :



```url
http://umbrel.local:3003
```



**Zdalny dostęp za pomocą Tailscale**: Aby uzyskać dostęp do serwera BTCPay z dowolnego miejsca na świecie, użyj Tailscale. Ta bezpieczna sieć VPN pozwala łączyć się z Umbrel tak, jakbyś był w sieci lokalnej. Zobacz nasz samouczek poświęcony Tailscale na Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfiguracja portfela Bitcoin



Aby akceptować płatności, należy skonfigurować Bitcoin wallet. BTCPay Server wyświetla opcje konfiguracji na pulpicie nawigacyjnym.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Aby skonfigurować wallet Bitcoin, przejdź do "Portfele" > "Bitcoin".



Masz dwie możliwości: utworzyć nowy portfel bezpośrednio w BTCPay lub zaimportować istniejący portfel. W przypadku importu dostępnych jest kilka metod:




- Podłącz sprzęt wallet** (zalecane): Zaimportuj klucze publiczne za pomocą aplikacji Vault
- Importuj plik wallet** (zalecane): Prześlij wyeksportowany plik ze swojego portfolio
- Wprowadź rozszerzony klucz publiczny**: Wprowadź swój XPub/YPub/ZPub ręcznie
- Zeskanuj kod QR wallet** : Skanowanie kodu QR z BlueWallet, Cobo Vault, Passport lub Specter DIY
- Wprowadź wallet seed** (niezalecane): Wprowadź 12- lub 24-wyrazową frazę odzyskiwania



![Options de création de portefeuille](assets/fr/06.webp)



Na potrzeby tego samouczka utworzymy nowy Hot wallet: klucz prywatny będzie zatem przechowywany na naszym serwerze Umbrel. W takim przypadku zdecydowanie zalecamy regularne przenoszenie środków do zimnego wallet, aby uniknąć przechowywania dużych kwot na serwerze.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Po skonfigurowaniu serwer BTCPay potwierdza, że wallet jest gotowy do przyjmowania płatności on-chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktywuj Lightning Network



Aby akceptować natychmiastowe płatności Lightning, przejdź do Wallets > Lightning. Następnie, ponieważ węzeł LND jest już zainstalowany w Umbrel, wystarczy kliknąć przycisk "Zapisz", aby zweryfikować połączenie między serwerem BTCPay a węzłem Lightning.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Tworzenie i opłacanie faktur



W interfejsie BTCPay Server przejdź do opcji Faktury > Utwórz Invoice. Wprowadź kwotę, dodaj opcjonalny opis i kliknij przycisk Utwórz.



![Création d'une nouvelle facture](assets/fr/10.webp)



Następnie można kliknąć przycisk "Checkout", aby wyświetlić fakturę. Następnie BTCPay generuje fakturę z ujednoliconym kodem QR (BIP21) zawierającym adres Bitcoin i fakturę Lightning.



![Détails de la facture générée](assets/fr/11.webp)



Klient może zeskanować kod QR za pomocą dowolnego kompatybilnego wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Po opłaceniu faktura staje się "rozliczona" w ciągu kilku sekund dla Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Zarządzanie i śledzenie płatności



W sekcji "Raportowanie", w zakładce "Faktury", znajdziesz pełną historię swoich faktur z datą, kwotą, statusem i metodą płatności. W razie potrzeby można ją wyeksportować.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfiguracja sklepu



BTCPay Server umożliwia zarządzanie wieloma sklepami o różnych parametrach. Każdy sklep reprezentuje oddzielny podmiot biznesowy: sklep e-commerce, fizyczny punkt sprzedaży lub rozliczanie usług.



W ustawieniach sklepu znajduje się kilka ważnych sekcji:



![Paramètres du magasin](assets/fr/15.webp)





- Ustawienia ogólne**: Nazwa sklepu, waluta referencyjna (BTC, EUR, USD), czas wygaśnięcia faktury (domyślnie 15 minut), liczba wymaganych potwierdzeń blockchain
- Kursy**: Konfiguracja źródeł kursów wymiany i konwersji fiat/Bitcoin
- Wygląd kasy**: Dostosuj wygląd stron kasy (logo, kolory, spersonalizowane wiadomości)
- Ustawienia e-mail**: Konfiguracja powiadomień e-mail o otrzymanych płatnościach
- Tokeny dostępu**: Zarządzanie tokenami API dla integracji e-commerce (WooCommerce, Shopify itp.)
- Użytkownicy**: Zarządzanie dostępem użytkowników do sklepu z różnymi poziomami uprawnień (Właściciel, Gość)
- Webhooks**: Konfiguracja Webhook do synchronizacji w czasie rzeczywistym z systemem księgowym lub ERP



BTCPay Server oferuje również sekcję Wtyczki, aby rozszerzyć funkcjonalność o integracje e-commerce, systemy punktów sprzedaży i dodatkowe narzędzia.



![Gestion des plugins](assets/fr/16.webp)



## Zalety i ograniczenia lokalnego użytkowania



**Zalety serwera BTCPay w porównaniu z Umbrel**:




- Całkowita suwerenność: wyłączna kontrola nad kluczami prywatnymi i środkami, żadna strona trzecia nie może zamrażać ani cenzurować płatności
- Znaczne oszczędności: tylko koszty sieciowe Bitcoin (kilka centów na Lightning) w porównaniu do 2-3% na tradycyjnych procesorach
- Maksymalna poufność: brak rejestracji, weryfikacji tożsamości lub udostępniania danych firmom zewnętrznym
- Architektura open-source gwarantuje przejrzystość, możliwość audytu i zrównoważony rozwój dzięki dużej społeczności deweloperów
- Łatwa instalacja za pomocą Umbrel, bez konieczności posiadania zaawansowanych umiejętności technicznych



**Ważne ograniczenia** :




- Tylko sieć lokalna**: Serwer BTCPay na Umbrel jest dostępny tylko z sieci domowej. Idealny do rozliczeń bezpośrednich, usług freelancerskich lub małych firm fizycznych, ale nieodpowiedni dla publicznie dostępnych sklepów internetowych.
- Pełna odpowiedzialność techniczna: konserwacja węzłów, regularne tworzenie kopii zapasowych, monitorowanie łączności
- Błyskawiczne zarządzanie płynnością: otwieranie i zarządzanie kanałami o wystarczającej przepustowości
- Wsparcie ograniczone do dokumentacji społeczności i forów, wymagające większej autonomii niż komercyjny dział obsługi klienta



To ograniczenie sieci lokalnej jest główną przeszkodą w integracji serwera BTCPay ze sklepem e-commerce, w którym klienci muszą mieć dostęp do stron płatności z dowolnego miejsca w Internecie.



## Najlepsze praktyki i bezpieczeństwo



Aktywuj automatyczne tworzenie kopii zapasowych Umbrel i przechowuj kopię na nośniku zewnętrznym (pamięć USB, dysk twardy, zaszyfrowana chmura). Przechowuj nasiona Bitcoin (frazy odzyskiwania) w bezpiecznym, fizycznie oddzielnym miejscu. Utwórz kopię zapasową pliku channel.backup LND na potrzeby odzyskiwania Lightning.



Regularnie monitoruj synchronizację Bitcoin Core, kanały Lightning i odpowiedź serwera BTCPay. Prosty cotygodniowy test: generate i zapłacenie rachunku za kilka satoshi. Aktualizuj Umbrel (poprawki bezpieczeństwa, ulepszenia). Przed większymi aktualizacjami należy wykonać kopię zapasową. W przypadku zastosowań profesjonalnych warto rozważyć zewnętrzny monitoring (UptimeRobot) z alertami e-mail/SMS.



## Publiczne udostępnienie serwera BTCPay dla sklepu internetowego



Aby zintegrować serwer BTCPay z internetowym sklepem e-commerce (WooCommerce, Shopify itp.), klienci muszą mieć dostęp do stron płatności z dowolnego miejsca, a nie tylko z sieci lokalnej.



**Rozwiązanie: Nginx Proxy Manager**



Możesz publicznie udostępnić serwer BTCPay za pomocą Nginx Proxy Manager (dostępnego w Umbrel App Store). To rozwiązanie wymaga :




- Nazwa domeny (klasyczna lub bezpłatna za pośrednictwem DuckDNS, No-IP, Afraid.org)
- Konfiguracja przekierowania portów (porty 80 i 443) na routerze
- Instalacja Nginx Proxy Manager, który automatycznie zarządza certyfikatami SSL



Ta konfiguracja wystawia serwer na działanie Internetu i wymaga dodatkowej czujności (silne hasła, 2FA, regularne aktualizacje). Przygotujemy dedykowany samouczek szczegółowo opisujący tę pełną procedurę.



## Wnioski



Serwer BTCPay na Umbrel łączy moc węzła Bitcoin z prostotą Umbrel, aby stworzyć samodzielnie hostowaną profesjonalną infrastrukturę płatniczą dostępną dla wszystkich. Ta suwerenność finansowa wiąże się z odpowiedzialnością za utrzymanie, ale Umbrel znacznie upraszcza obciążenie operacyjne w porównaniu z korzyściami: eliminacją opłat za przetwarzanie, ochroną prywatności, odpornością na cenzurę i całkowitą kontrolą środków.



Korzystanie z sieci lokalnej obejmuje już szeroki zakres zastosowań: rozliczenia za usługi freelancerów, płatności osobiste, małe sklepy fizyczne lub po prostu naukę i eksperymentowanie z Bitcoin i Lightning w kontrolowanym środowisku. Dla potrzeb e-commerce wymagających publicznej ekspozycji istnieje rozwiązanie Nginx Proxy Manager, ale wymaga dodatkowej konfiguracji technicznej, którą szczegółowo omówimy w dedykowanym samouczku.



Niezależnie od tego, czy prowadzisz firmę, raczkujący projekt, czy po prostu eksperymentujesz, serwer BTCPay na Umbrel oferuje pełną autonomię finansową. Ścieżka zaczyna się od pierwszego sklepu, pierwszej faktury, pierwszej płatności otrzymanej bezpośrednio do suwerennej infrastruktury.



## Zasoby



### Oficjalna dokumentacja




- [Oficjalna strona serwera BTCPay](https://btcpayserver.org)
- [Pełna dokumentacja serwera BTCPay](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Dokumentacja Tailscale](https://tailscale.com/kb)


### Społeczność i wsparcie




- [Forum BTCPay Server](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)