---
name: Dana Wallet
description: Minimalistyczny portfel dla cichych płatności (BIP-352)
---

![cover](assets/cover.webp)



Ponowne wykorzystanie adresów Bitcoin jest jednym z najbardziej bezpośrednich zagrożeń dla poufności użytkownika. Gdy odbiorca udostępnia jeden adres w celu otrzymania wielu płatności, każdy obserwator może prześledzić wszystkie powiązane transakcje i odtworzyć ich historię finansową. Problem ten dotyczy w szczególności twórców treści, organizacji charytatywnych lub aktywistów, którzy chcą publicznie wyświetlać adres darowizny bez narażania prywatności swojej lub swoich darczyńców.



Dana Wallet odpowiada na ten problem eleganckim rozwiązaniem: Silent Payments. Ten minimalistyczny, open-source'owy wallet, uruchomiony w 2024 roku, generuje statyczny adres wielokrotnego użytku, gwarantując jednocześnie, że każda otrzymana płatność trafia na osobny adres w łańcuchu bloków. Nadawca nie potrzebuje wcześniejszej interakcji z odbiorcą, a żaden zewnętrzny obserwator nie może połączyć ze sobą poszczególnych transakcji. W łańcuchu bloków płatności te wyglądają jak zwykłe transakcje Taproot.



Dana Wallet jest dostępna na Mainnet i Signet, ale deweloperzy nadal uważają ją za eksperymentalną i zalecają, aby nie wpłacać środków, których nie jesteś gotów stracić. W tym samouczku użyjemy wersji Signet, aby odkryć Silent Payments bez ryzykowania prawdziwych środków.



## Co to jest Dana Wallet?



### Filozofia i cele



Dana Wallet przyjmuje podejście "SP-first": wallet generuje wyłącznie adresy Silent Payments i akceptuje tylko ten rodzaj płatności. Za pomocą tej aplikacji nie będzie można utworzyć klasycznego adresu Bitcoin (starszego, SegWit lub Taproot). To celowe ograniczenie pozwala w pełni skoncentrować się na nauce protokołu BIP-352 bez rozpraszania się innymi funkcjami. Przejrzysty interfejs celowo faworyzuje łatwość użytkowania nad mnogością opcji, dzięki czemu narzędzie jest dostępne nawet dla użytkowników nowych w koncepcjach poufności on-chain.



Projekt jest całkowicie open-source, opracowany przy użyciu Flutter dla interfejsu mobilnego i Rust dla wewnętrznej logiki kryptograficznej. Architektura ta łączy w sobie płynne doświadczenie użytkownika z optymalną wydajnością dla intensywnych operacji skanowania.



### Jak działają ciche płatności?



Ciche płatności (BIP-352) opierają się na zaawansowanym mechanizmie kryptograficznym wykorzystującym klucz Elliptic Curve Diffie-Hellman Key Exchange (ECDH). Odbiorca generuje statyczny adres (zaczynający się od `sp1...` na mainnet lub `tsp1...` na Signet) składający się z dwóch różnych kluczy publicznych: klucza skanowania ($B_{scan}$) do wykrywania przychodzących płatności i klucza wydawania ($B_{spend}$) do wydawania otrzymanych środków. To rozdzielenie umożliwia przechowywanie klucza wydawania na sprzęcie wallet podczas korzystania z klucza skanowania na podłączonym urządzeniu.



Gdy nadawca chce dokonać płatności, jego wallet łączy sumę kluczy prywatnych jego wejść z publicznym kluczem skanowania odbiorcy, aby obliczyć wspólny sekret ECDH. Sekret ten generuje kryptograficzną "poprawkę", która dodana do klucza wydatków odbiorcy tworzy unikalny adres Taproot dla tej transakcji.



Odbiorca może odtworzyć te obliczenia przy użyciu swojego prywatnego klucza skanowania i kluczy publicznych widocznych w transakcji (właściwość matematyczna Diffiego-Hellmana). Umożliwia mu to wykrycie i wydanie środków bez wcześniejszej interakcji z nadawcą.



Takie podejście ma kilka zalet:




- Poufność odbiorcy**: każda płatność trafia na inny adres
- Poufność nadawcy**: brak trwałego identyfikatora łączącego płatności
- Brak zewnętrznego serwera**: protokół działa autonomicznie
- Niewyróżniające się transakcje**: Ciche płatności wyglądają jak zwykłe transakcje Taproot



Główną wadą jest koszt skanowania: odbiorca musi przeanalizować każdą nową transakcję Taproot, aby wykryć te przeznaczone dla niego.



Jeśli chcesz dowiedzieć się więcej o technicznym działaniu Silent Payments, polecamy kurs BTC204 dotyczący poufności w Bitcoin, który zawiera rozdział poświęcony Silent Payments:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Obsługiwane platformy



Dana Wallet jest dostępna jako aplikacja na Androida. APK można pobrać za pośrednictwem dedykowanego repozytorium F-Droid dostarczonego przez deweloperów, za pośrednictwem Obtainium lub bezpośrednio z GitHub. Dla użytkowników Linuksa istnieje techniczna możliwość skompilowania aplikacji Flutter na pulpit.



Aplikacja nie jest dostępna na iOS ani w oficjalnych sklepach (Google Play, App Store), co odzwierciedla jej eksperymentalny status i skupienie się na odbiorcach technicznych.



## Instalacja



### Niezbędne warunki wstępne



Aby zainstalować Dana Wallet na Androidzie, potrzebujesz urządzenia z Androidem z włączoną opcją "Nieznane źródła" w ustawieniach bezpieczeństwa. Konto ani rejestracja nie są wymagane.



### Dodaj depozyt F-Cold



Zalecaną metodą jest dodanie dedykowanego repozytorium F-Droid Dana Wallet. Przejdź do `fdroid.silentpayments.dev`, gdzie znajdziesz link do repozytorium i kod QR do zeskanowania. Repozytorium oferuje obecnie 3 aplikacje: wersję Mainnet, Development i Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Instalacja przez F-Droid



Otwórz aplikację F-Droid na urządzeniu z systemem Android, a następnie przejdź do Ustawień za pomocą ikony w prawym dolnym rogu. Wybierz "Repozytoria", aby zarządzać źródłami aplikacji. Naciśnij przycisk "+", aby dodać nowe repozytorium, a następnie zeskanuj kod QR lub wklej link `https://fdroid.silentpayments.dev/fdroid/repo`. Po dodaniu repozytorium zobaczysz trzy dostępne wersje Dana Wallet. Wybierz "Dana Wallet - Zakładka" i naciśnij "Zainstaluj".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Konfiguracja początkowa



### Tworzenie portfolio



Przy pierwszym uruchomieniu Dana Wallet wyświetla ekran powitalny przedstawiający jej misję: "Wysyłaj i odbieraj darowizny bez pośredników". Naciśnij "Rozpocznij", aby kontynuować. Następny ekran przedstawia trzy kluczowe zalety aplikacji:




- Darowizny bez wysiłku**: zacznij otrzymywać darowizny w kilka sekund
- Prywatność domyślnie**: brak konieczności posiadania serwerów lub złożonej infrastruktury
- Doświadczenie podobne do poczty e-mail**: wysyłaj i odbieraj bitcoiny tak prosto, jak e-mail



Możesz wybrać "Przywróć", aby przywrócić istniejący portfel lub "Utwórz nowy wallet", aby utworzyć nowy. Naciśnij "Utwórz nowy wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Następnie aplikacja generuje frazę odzyskiwania, którą należy dokładnie zanotować na nośniku fizycznym. Nawet w przypadku środków testowych, które nie mają rzeczywistej wartości, należy stosować dobre praktyki tworzenia kopii zapasowych.



### Interface i parametry



Po utworzeniu portfela zostaniesz przeniesiony do głównego interfejsu, podzielonego na dwie zakładki: "Transakcje" i "Ustawienia".



Zakładka **Transact** wyświetla saldo bitcoinów (i jego konwersję na dolary), listę ostatnich transakcji oraz dwa przyciski akcji: "Zapłać", aby wysłać środki, oraz przycisk odbioru (ikona pobierania).



Zakładka **Ustawienia** oferuje cztery opcje:




- Pokaż frazę seed**: wyświetla frazę odzyskiwania do przechowywania
- Zmień walutę fiducjarną**: zmiana wyświetlanej waluty (domyślnie USD)
- Set backend url**: konfiguracja adresu URL serwera Blindbit (patrz następna sekcja)
- Wipe wallet**: całkowite wyczyszczenie wallet z urządzenia



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Serwer Blindbit



Dana Wallet używa serwera indeksującego o nazwie **Blindbit** do wykrywania cichych płatności. Zrozumienie, jak to działa, jest ważne dla oceny modelu zaufania aplikacji.



**Po co nam serwer?



Aby wykryć cichą płatność, wallet musi teoretycznie przeskanować wszystkie transakcje Taproot w każdym bloku i wykonać obliczenia kryptograficzne (ECDH) dla każdej z nich. Na telefonie komórkowym operacja ta byłaby zbyt wymagająca obliczeniowo i pod względem przepustowości.



Serwer Blindbit rozwiązuje ten problem poprzez wstępne obliczanie danych pośrednich (zwanych "tweaks") dla wszystkich transakcji Taproot. Następnie wallet pobiera te poprawki (33 bajty na transakcję) i wykonuje ostateczne obliczenia **lokalnie**, aby sprawdzić, czy płatność należy do Ciebie.



**Zachowana poufność**



W przeciwieństwie do konwencjonalnego serwera Electrum, w którym ujawniasz swoje adresy, serwer Blindbit nie wie, które płatności należą do Ciebie. Udostępnia te same dane wszystkim użytkownikom, a ostateczną weryfikację przeprowadza telefon użytkownika. Poufność użytkownika jest zatem zachowana w stosunku do serwera.



**Domyślny serwer



Dana Wallet używa publicznego serwera `silentpayments.dev/blindbit/signet` (dla Signet) lub `silentpayments.dev/blindbit/mainnet` (dla Mainnet). Możesz zmienić ten adres URL w ustawieniach, jeśli hostujesz własny serwer.



**Własny serwer Blindbit**



Dla użytkowników pragnących całkowitej suwerenności, możliwe jest hostowanie własnego serwera Blindbit Oracle. Wymaga to :




- Kompletny węzeł rdzenia Bitcoin **bez orła** (inny niż pruned)
- Instalacja Blindbit Oracle (dostępna na GitHub: `setavenger/blindbit-oracle`)
- Około 10 GB dodatkowej przestrzeni dyskowej
- Umiejętności techniczne (kompilacja Go, konfiguracja serwera)



Żadna spakowana aplikacja nie jest jeszcze dostępna dla Umbrel lub Start9. Instalacja pozostaje na razie ręczna. Jest to dziedzina aktywnie ewoluująca i w przyszłości mogą pojawić się bardziej dostępne rozwiązania.



## Codzienne użytkowanie



### Otrzymywanie środków



Aby otrzymać bitcoiny, naciśnij przycisk odbioru (ikona pobierania) na ekranie głównym. Dana Wallet wyświetli wówczas pełny adres Silent Payment w formacie `tsp1q...` w zakładce Bookmark. Interfejs oferuje kilka opcji:




- Pokaż kod QR**: wyświetla kod QR adresu w celu łatwego skanowania
- Udostępnij**: udostępnianie adresu za pośrednictwem aplikacji telefonu
- Kopiuj**: kopiuje adres do schowka



Jak pokazano na ekranie, możesz udostępnić ten adres publicznie w sieciach społecznościowych bez narażania swojej prywatności.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Aby uzyskać pierwsze środki testowe na Signet, użyj dedykowanego kranu Silent Payments dostępnego pod adresem `silentpayments.dev/faucet/signet`. Skopiuj swój adres `tsp1...`, wklej go w polu dostępnym w kranie, a następnie potwierdź żądanie. Poczekaj na wydobycie bloku (około 10 minut na Signet).



### Wyślij płatność



Aby wysłać środki, naciśnij przycisk "Zapłać" na ekranie głównym. Zostanie wyświetlony ekran "Wybierz odbiorcę(ów)" z trzema opcjami umożliwiającymi określenie odbiorcy:




- Wprowadź informacje o płatności ręcznie
- Wklej ze schowka**: wklejanie adresu ze schowka
- Skanuj kod QR**: skanowanie kodu QR zawierającego adres



Po zatwierdzeniu adresu odbiorcy na ekranie "Wprowadź kwotę" można wprowadzić kwotę do wysłania w satoshis. Dostępne saldo jest wyświetlane w celach informacyjnych. Naciśnij "Przejdź do wyboru opłaty", aby kontynuować.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Następny ekran pokazuje trzy poziomy opłat, w zależności od wymaganej pilności:




- Szybkie** (10-30 minut): wyższe opłaty za szybkie potwierdzenie
- Normalny** (30-60 minut): umiarkowane koszty
- Wolny** (1+ godzina): minimalna opłata za transakcje niepilne



Po wybraniu poziomu opłaty, ekran potwierdzenia "Gotowy do wysłania?" podsumowuje wszystkie szczegóły: adres docelowy, kwotę, szacowany czas i opłatę transakcyjną. Sprawdź dokładnie te informacje, a następnie naciśnij "Wyślij", aby wysłać transakcję.



Po wysłaniu transakcja pojawia się w historii ze statusem "Niepotwierdzona", dopóki nie zostanie uwzględniona w bloku. Saldo zostanie odpowiednio zaktualizowane.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Zalety i ograniczenia



### Najważniejsze wydarzenia





- Pedagogiczny**: uproszczony interfejs skoncentrowany na nauce Silent Payments
- Dwukierunkowy**: obsługuje zarówno wysyłanie, jak i odbieranie, w przeciwieństwie do innych portfeli
- Open-source**: w pełni audytowalny kod w serwisie GitHub
- Dedykowany Faucet**: ułatwia uzyskanie finansowania testów
- Bez konta**: nie wymaga rejestracji ani podawania danych osobowych



### Ograniczenia do rozważenia





- Eksperymentalne**: nieaudytowane oprogramowanie, należy zachować ostrożność w przypadku Mainnet
- Ograniczona platforma**: głównie Android, brak wersji na iOS
- Ograniczona funkcjonalność**: brak kontroli monet, brak subkont, brak Lightning
- Intensywne skanowanie**: wykrywanie płatności pochłania znaczne zasoby



## Najlepsze praktyki



### Bezpieczeństwo seed



Nawet w przypadku testów Signet z bezwartościowym tłem, frazę odzyskiwania należy traktować poważnie. Użyj opcji "Pokaż frazę seed" w ustawieniach, aby dokładnie ją zapisać. Dobrą praktyką jest utrzymywanie całkowicie oddzielnych portfeli dla Signet i Mainnet: nigdy nie używaj seed stworzonego do testów na wallet przeznaczonym do otrzymywania prawdziwych środków.



### Ostrzeżenie o statusie eksperymentalnym



Dana Wallet jest nadal uważana za eksperymentalną przez jej twórców. Jak wyraźnie stwierdzają: "Nie używaj środków, których nie chcesz stracić". Do celów edukacyjnych wybierz wersję Signet. Jeśli korzystasz z wersji Mainnet, ogranicz się do kwot token.



### Kopia zapasowa i przywracanie



Odzyskiwanie funduszy Silent Payments wymaga wallet kompatybilnego z protokołem BIP-352. Standardowy wallet nie może skanować łańcucha bloków w celu odzyskania UTXO Silent Payments. Zachowaj zainstalowany Wallet Dana lub użyj opcji "Przywróć" przy pierwszym uruchomieniu, aby odzyskać istniejący wallet.



## Porównanie z BIP-47 i PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Ciche płatności eliminują transakcję powiadomienia BIP-47 kosztem droższego skanowania. PayJoin rozwiązuje inny problem (korelacja danych wejściowych) i może być połączony z Silent Payments.



## Wnioski



Dana Wallet to cenne narzędzie edukacyjne do nauki o cichych płatnościach w środowisku wolnym od ryzyka. Jego minimalistyczne podejście pozwala zrozumieć podstawowe mechanizmy protokołu BIP-352 bez rozpraszania się drugorzędnymi funkcjami. Eksperymentując z Signet, rozwiniesz praktyczne zrozumienie tej obiecującej technologii zapewniającej poufność transakcji Bitcoin.



Silent Payments stanowi znaczący krok naprzód w pogodzeniu łatwości użytkowania i poszanowania prywatności. Entuzjazm społeczności i pierwsze integracje z różnymi portfelami (Cake Wallet, BitBox02, BlueWallet do wysyłania) wskazują na przyszłość, w której publikowanie adresu darowizny nie będzie już zagrażać prywatności finansowej jego właściciela.



## Zasoby



### Oficjalna dokumentacja




- Repozytorium Dana Wallet GitHub: https://github.com/cygnet3/danawallet
- F-Cold depozyt: https://fdroid.silentpayments.dev
- Strona społeczności Silent Payments: https://silentpayments.xyz
- Specyfikacja BIP-352: https://bips.dev/352



### Narzędzia testowe Signet




- Faucet Ciche płatności: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Serwer Blindbit (hostowany samodzielnie)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle