---
name: BTCPAY SERVER - Parasol
description: Instalowanie i używanie BTCPAY SERVER na Umbrel do akceptowania Bitcoin i Lightning
---

![cover](assets/cover.webp)



W ekosystemie Bitcoin akceptowanie płatności stanowi poważne wyzwanie zarówno dla sprzedawców, jak i firm. Tradycyjne rozwiązania, czy to bankowe (karty kredytowe, Stripe, PayPal), czy nawet Bitcoin (BitPay, Coinbase Commerce), narzucają pośredników, którzy pobierają znaczne opłaty, gromadzą poufne dane biznesowe i mogą BLOCK lub cenzurować transakcje według własnego uznania. Zależność ta jest sprzeczna z podstawowymi zasadami Bitcoin dotyczącymi decentralizacji, poufności i suwerenności finansowej.



BTCPAY SERVER staje się odpowiedzią open-source na ten problem. Ten samoobsługowy procesor płatności zamienia własny węzeł Bitcoin w profesjonalną infrastrukturę, bez pośredników, bez dodatkowych opłat za przetwarzanie i bez uszczerbku dla prywatności. Opracowany przez globalną społeczność współpracowników od 2017 roku, BTCPAY SERVER umożliwia otrzymywanie płatności Bitcoin i Lightning bezpośrednio do portfeli, zachowując pełną kontrolę nad swoimi środkami przez cały czas.



Tradycyjnie instalacja BTCPAY SERVER wymaga zaawansowanych umiejętności technicznych: Konfiguracji serwera Linux, opanowania Dockera, zarządzania certyfikatami SSL i bezpieczeństwa sieci. Umbrel rewolucjonizuje to podejście dzięki instalacji jednym kliknięciem bezpośrednio zintegrowanej z Bitcoin i LIGHTNING NODE. To uproszczenie sprawia, że to, co wcześniej było zarezerwowane dla doświadczonych techników, jest dostępne dla każdego.



**Ważne do zrozumienia**: BTCPAY SERVER na Umbrel działa domyślnie tylko w sieci lokalnej. Możesz tworzyć faktury, akceptować płatności Lightning i Bitcoin oraz zarządzać swoją księgowością z dowolnego urządzenia podłączonego do sieci domowej (komputer, smartfon, tablet). Ta konfiguracja jest idealna do rozliczania usług osobistych, zarządzania płatnościami twarzą w twarz lub korzystania z BTCPAY SERVER z sieci lokalnej. Z drugiej strony, aby zintegrować BTCPAY SERVER ze sklepem internetowym, który jest publicznie dostępny w Internecie, wymagana będzie dodatkowa konfiguracja z publiczną ekspozycją (omówimy tę kwestię na końcu samouczka).



Ten samouczek przeprowadzi Cię przez pełną instalację BTCPAY SERVER na Umbrel, konfigurację Bitcoin, Wallet i LIGHTNING NODE, tworzenie i opłacanie faktur oraz zarządzanie raportowaniem księgowym. Dowiesz się, jak efektywnie korzystać z BTCPAY SERVER w sieci lokalnej, a następnie omówimy rozwiązania do publicznego wyświetlania, jeśli chcesz zintegrować go z witryną e-commerce.



## Wymagania wstępne



Aby skorzystać z tego samouczka, musisz mieć poprawnie zainstalowany i skonfigurowany Umbrel. Jeśli jeszcze tego nie zrobiłeś, zapoznaj się z naszym samouczkiem dotyczącym instalacji Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Węzeł Bitcoin core musi być w pełni zsynchronizowany z Blockchain (100% w aplikacji Bitcoin firmy Umbrel). Ta początkowa synchronizacja trwa zwykle od 3 dni do 2 tygodni, w zależności od sprzętu i połączenia internetowego.



Aby akceptować natychmiastowe płatności Lightning, musisz również zainstalować LND (Lightning Network Daemon) na Umbrel. Zapoznaj się z naszym samouczkiem dotyczącym instalowania i konfigurowania LND na Umbrel, jeśli chcesz włączyć tę funkcję.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Należy zapewnić co najmniej 50 GB wolnego miejsca na dysku dla BTCPAY SERVER, jego baz danych i danych Lightning. Zdecydowanie zaleca się stabilne połączenie z Internetem za pomocą kabla Ethernet, aby uniknąć rozłączeń.



## Instalacja BTCPAY SERVER na parasolu



Z Umbrel Interface (`umbrel.local`), przejdź do App Store i wyszukaj "BTCPAY SERVER" w kategorii Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Kliknij przycisk Zainstaluj. Umbrel automatycznie sprawdzi, czy Bitcoin core i LND są zainstalowane, a następnie rozpocznie wdrażanie (2-5 minut).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Po zainstalowaniu otwórz aplikację. Konieczne będzie utworzenie konta administratora z silnymi poświadczeniami.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Po utworzeniu konta BTCPAY SERVER natychmiast wyświetli monit o skonfigurowanie pierwszego sklepu. Wybierz profesjonalną nazwę i walutę referencyjną (EUR, USD lub BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Dostęp do BTCPAY SERVER w sieci lokalnej



BTCPAY SERVER jest dostępny z dowolnego urządzenia w sieci lokalnej (WiFi lub Ethernet). Dostęp z przeglądarki do :



```url
http://umbrel.local
```



Lub bezpośrednio do :



```url
http://umbrel.local:3003
```



**Zdalny dostęp za pomocą Tailscale**: Aby uzyskać dostęp do BTCPAY SERVER z dowolnego miejsca na świecie, użyj Tailscale. Ta bezpieczna sieć VPN pozwala łączyć się z Umbrel tak, jakbyś był w sieci lokalnej. Zobacz nasz samouczek poświęcony Tailscale na Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfiguracja portfela Bitcoin



Aby akceptować płatności, należy skonfigurować Bitcoin Wallet. BTCPAY SERVER wyświetla opcje konfiguracji na pulpicie nawigacyjnym.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Aby skonfigurować Wallet Bitcoin, przejdź do "Wallets" > "Bitcoin".



Masz dwie możliwości: utworzyć nowy portfel bezpośrednio w BTCPay lub zaimportować istniejący portfel. W przypadku importu dostępnych jest kilka metod:




- Podłącz Hardware Wallet** (zalecane): Import kluczy publicznych za pośrednictwem aplikacji Vault
- Importuj plik Wallet** (zalecane): Prześlij wyeksportowany plik ze swojego portfolio
- Wprowadź rozszerzony klucz publiczny**: Wprowadź swój XPub/YPub/ZPub ręcznie
- Zeskanuj kod QR Wallet** : Skanowanie kodu QR z BlueWallet, Cobo Vault, Passport lub Specter DIY
- Wprowadź Wallet seed** (niezalecane): Wprowadź 12- lub 24-wyrazową frazę odzyskiwania



![Options de création de portefeuille](assets/fr/06.webp)



Na potrzeby tego samouczka utworzymy nowy Hot Wallet: klucz prywatny będzie zatem przechowywany na naszym serwerze Umbrel. W takim przypadku zdecydowanie zalecamy regularne przenoszenie środków do Cold Wallet, aby uniknąć przechowywania dużych kwot na serwerze.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Po skonfigurowaniu BTCPAY SERVER potwierdza, że Wallet jest gotowy do przyjmowania płatności On-Chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktywuj Lightning Network



Aby zaakceptować natychmiastowe płatności Lightning, przejdź do Wallets > Lightning. Następnie, ponieważ węzeł LND jest już na miejscu w Umbrel, wystarczy kliknąć przycisk "Zapisz", aby zatwierdzić połączenie między BTCPAY SERVER a LIGHTNING NODE.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Tworzenie i opłacanie faktur



W Interface BTCPAY SERVER przejdź do pozycji Faktury > Utwórz Invoice. Wprowadź kwotę, dodaj opcjonalny opis i kliknij przycisk Utwórz.



![Création d'une nouvelle facture](assets/fr/10.webp)



Następnie można kliknąć przycisk "Checkout", aby wyświetlić Invoice. Następnie BTCPay generuje Invoice z ujednoliconym kodem QR (BIP21) zawierającym Bitcoin Address i Lightning Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Klient może zeskanować kod QR za pomocą dowolnego kompatybilnego Wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Po dokonaniu płatności Invoice zostaje "rozliczony" w ciągu kilku sekund dla Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Zarządzanie i śledzenie płatności



W sekcji "Raportowanie", w zakładce "Faktury", znajdziesz pełną historię swoich faktur, z datą, kwotą, statusem i metodą płatności. W razie potrzeby można ją wyeksportować.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfiguracja sklepu



BTCPAY SERVER umożliwia zarządzanie wieloma sklepami o różnych parametrach. Każdy sklep reprezentuje oddzielną jednostkę biznesową: sklep e-commerce, fizyczny punkt sprzedaży lub rozliczanie usług.



W ustawieniach sklepu znajduje się kilka ważnych sekcji:



![Paramètres du magasin](assets/fr/15.webp)





- Ustawienia ogólne**: Nazwa sklepu, waluta referencyjna (BTC, EUR, USD), czas wygaśnięcia Invoice (domyślnie 15 minut), liczba wymaganych potwierdzeń Blockchain
- Stawki**: Konfiguracja źródeł stawek Exchange i konwersji fiat/Bitcoin
- Wygląd kasy**: Dostosuj wygląd stron kasy (logo, kolory, spersonalizowane wiadomości)
- Ustawienia e-mail**: Konfiguracja powiadomień e-mail o otrzymanych płatnościach
- Tokeny dostępu**: API Zarządzanie token dla integracji e-commerce (WooCommerce, Shopify itp.)
- Użytkownicy**: Zarządzanie dostępem użytkowników do sklepu z różnymi poziomami uprawnień (Właściciel, Gość)
- Webhooks**: Konfiguracja Webhook do synchronizacji w czasie rzeczywistym z systemem księgowym lub ERP



BTCPAY SERVER oferuje również sekcję wtyczek, aby rozszerzyć funkcjonalność o integracje e-commerce, systemy punktów sprzedaży i dodatkowe narzędzia.



![Gestion des plugins](assets/fr/16.webp)



## Zalety i ograniczenia lokalnego użytkowania



**Korzyści BTCPAY SERVER na Umbrel** :




- Całkowita suwerenność: wyłączna kontrola nad kluczami prywatnymi i środkami, żadna strona trzecia nie może zamrażać ani cenzurować płatności
- Znaczne oszczędności: tylko koszty sieciowe Bitcoin (kilka centów na Lightning) w porównaniu do 2-3% na tradycyjnych procesorach
- Maksymalna poufność: brak rejestracji, weryfikacji tożsamości lub udostępniania danych firmom zewnętrznym
- Architektura open-source gwarantuje przejrzystość, możliwość kontroli i zrównoważony rozwój dzięki dużej społeczności deweloperów
- Łatwa instalacja za pomocą Umbrel, bez konieczności posiadania zaawansowanych umiejętności technicznych



**Ważne ograniczenia** :




- Tylko sieć lokalna**: BTCPAY SERVER na Umbrel jest dostępny tylko z sieci domowej. Idealny do rozliczeń bezpośrednich, usług freelancerskich lub małych firm fizycznych, ale nieodpowiedni dla sklepów internetowych, które są publicznie dostępne w Internecie.
- Pełna odpowiedzialność techniczna: konserwacja węzłów, regularne tworzenie kopii zapasowych, monitorowanie łączności
- Błyskawiczne zarządzanie płynnością: otwieranie i zarządzanie kanałami o wystarczającej przepustowości
- Wsparcie ograniczone do dokumentacji społeczności i forów, wymagające większej autonomii niż komercyjny dział obsługi klienta



To ograniczenie sieci LAN jest główną przeszkodą w integracji BTCPAY SERVER ze sklepem e-commerce, w którym klienci muszą mieć dostęp do stron płatności z dowolnego miejsca w Internecie.



## Najlepsze praktyki i bezpieczeństwo



Aktywuj automatyczne tworzenie kopii zapasowych Umbrel i przechowuj kopię na nośniku zewnętrznym (pamięć USB, dysk Hard, zaszyfrowana chmura). Przechowuj nasiona Bitcoin (frazy odzyskiwania) w bezpiecznym, fizycznie oddzielnym miejscu. Zapisz plik LND channel.backup do odzyskiwania Lightning.



Regularnie monitoruj synchronizację Bitcoin core, kanały Lightning i odpowiedź BTCPAY SERVER. Prosty cotygodniowy test: generate i zapłacić rachunek za kilka satoshi. Aktualizuj Umbrel (poprawki bezpieczeństwa, ulepszenia). Przed większymi aktualizacjami należy wykonać kopię zapasową. W przypadku zastosowań profesjonalnych warto rozważyć zewnętrzny monitoring (UptimeRobot) z alertami e-mail/SMS.



## Pokaż BTCPAY SERVER publicznie dla sklepu internetowego



Aby zintegrować BTCPAY SERVER z internetowym sklepem e-commerce (WooCommerce, Shopify itp.), klienci muszą mieć dostęp do stron płatności z dowolnego miejsca, a nie tylko z sieci lokalnej.



**Rozwiązanie: Nginx Proxy Manager**



BTCPAY SERVER można udostępnić publicznie za pomocą Nginx Proxy Manager (dostępnego w Umbrel App Store). To rozwiązanie wymaga :




- Nazwa domeny (klasyczna lub bezpłatna za pośrednictwem DuckDNS, No-IP, Afraid.org)
- Konfiguracja przekierowania portów (porty 80 i 443) na routerze
- Instalacja Nginx Proxy Manager, który automatycznie zarządza certyfikatami SSL



Ta konfiguracja wystawia serwer na działanie Internetu i wymaga dodatkowej czujności (silne hasła, 2FA, regularne aktualizacje). Przygotujemy dedykowany samouczek szczegółowo opisujący tę pełną procedurę.



## Wnioski



BTCPAY SERVER na Umbrel łączy w sobie moc węzła Bitcoin z prostotą Umbrel, tworząc samodzielnie hostowaną profesjonalną infrastrukturę płatniczą dostępną dla wszystkich. Ta suwerenność finansowa wiąże się z odpowiedzialnością za utrzymanie, ale Umbrel znacznie upraszcza obciążenie operacyjne w porównaniu z korzyściami: eliminacją opłat za przetwarzanie, ochroną prywatności, odpornością na cenzurę i całkowitą kontrolą środków.



Korzystanie z sieci lokalnej obejmuje już szeroki zakres zastosowań: rozliczanie usług freelancerów, płatności bezpośrednie, małe sklepy fizyczne lub po prostu naukę i eksperymentowanie z Bitcoin i Lightning w kontrolowanym środowisku. Dla potrzeb e-commerce wymagających publicznej ekspozycji istnieje rozwiązanie Nginx Proxy Manager, ale wymaga dodatkowej konfiguracji technicznej, którą szczegółowo omówimy w dedykowanym samouczku.



Niezależnie od tego, czy prowadzisz firmę, raczkujący projekt, czy po prostu eksperymentujesz, BTCPAY SERVER na Umbrel oferuje pełną autonomię finansową. Ścieżka zaczyna się od pierwszego sklepu, pierwszego Invoice, pierwszej płatności otrzymanej bezpośrednio do suwerennej infrastruktury.



## Zasoby



### Oficjalna dokumentacja




- [Oficjalna strona BTCPAY SERVER](https://btcpayserver.org)
- [Pełna dokumentacja BTCPAY SERVER](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Dokumentacja Tailscale](https://tailscale.com/kb)


### Społeczność i wsparcie




- [Forum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)