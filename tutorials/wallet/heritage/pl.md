---
name: Heritage
description: Portfel Bitcoin ze zintegrowanym mechanizmem dziedziczenia poprzez skrypty Taproot
---

![cover](assets/cover.webp)



Przekazanie bitcoinów w przypadku śmierci lub niezdolności do pracy stanowi poważne wyzwanie dla każdego posiadacza aktywów kryptowalutowych. Bez odpowiedniego planu dziedziczenia, aktywa te stają się nie do odzyskania dla bliskich.



Heritage zapewnia elegancką odpowiedź poprzez wdrożenie mechanizmu dead-man switch bezpośrednio na blockchainie Bitcoin. Ten wallet o otwartym kodzie źródłowym umożliwia skonfigurowanie warunków sukcesji on-chain: jeśli właściciel nie dokona dalszych transakcji przez określony czas, wcześniej wyznaczone klucze alternatywne mogą zwolnić środki.



## Czym jest dziedzictwo?



Heritage to portfolio Bitcoin natywnie integrujące mechanizm dziedziczenia poprzez skrypty Taproot. Opracowane na licencji MIT przez Jérémie Rodon, to oprogramowanie open-source gwarantuje przejrzystość i trwałość.



Heritage używa skryptów Taproot zakodowanych w adresach Bitcoin. Każdy UTXO integruje dwa rodzaje warunków wydatków:





- Ścieżka podstawowa** : Właściciel może wydać swoje bitcoiny w dowolnym momencie za pomocą swojego klucza głównego
- Alternatywne ścieżki**: Dla każdego wyznaczonego spadkobiercy skrypt łączy jego klucz publiczny z blokadą czasową



Każda transakcja właściciela automatycznie odracza datę aktywacji klauzul spadkowych. W przypadku przedłużającej się nieaktywności (śmierć, niezdolność do pracy) warunki są automatycznie uruchamiane.



## Usługa dziedzictwa (opcjonalnie)



Heritage oferuje dwie opcje użytkowania:



** Zrób to sam (za darmo)**: Sama aplikacja open-source. Zarządzasz wszystkim autonomicznie za pomocą własnego węzła. Ta opcja oferuje wbudowany dostęp do kopii zapasowych, wbudowane dziedziczenie i wyłączną kontrolę nad bitcoinami. Musisz jednak utworzyć własne alerty (kalendarz, przypomnienia), aby nie zapomnieć o odnowieniu timelocków, i nie ma automatycznych powiadomień dla spadkobierców.



**Korzystaj z usługi (0,05% rocznie)** : Usługa btc-heritage.com dodaje funkcje upraszczające zarządzanie:




- Automatyczne przypomnienia przed upływem terminów
- Automatyczne powiadomienia dla spadkobierców, aby przeprowadzić ich przez proces odzyskiwania danych
- Priorytetowe wsparcie
- Uproszczone zarządzanie deskryptorami



Opłata: 0,05% zarządzanej kwoty rocznie, minimum 0,5 mBTC/rok. Pierwszy rok bezpłatny.



Usługa pozostaje bezobsługowa: klucze prywatne nigdy nie opuszczają urządzenia użytkownika. Heritage nie ma dostępu do Twoich środków.



## Heritage CLI



Dla zaawansowanych użytkowników preferujących terminal, Heritage oferuje narzędzie wiersza poleceń (CLI) do kontroli granularnej i obsługi maszyny z ogranicznikiem przepływu powietrza.



![Page Heritage CLI](assets/fr/03.webp)



Pełna dokumentacja CLI jest dostępna na stronie [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Znajdziesz tam instrukcje dotyczące pobierania, łączenia się z usługą, tworzenia portfeli (za pomocą Ledger lub kluczy lokalnych), zarządzania spadkobiercami i transakcjami.



Ten samouczek koncentruje się na aplikacji Desktop, która jest bardziej dostępna dla większości użytkowników.



## Pulpit Heritage



Heritage Desktop to aplikacja graficzna z intuicyjnym interfejsem, który prowadzi użytkownika przez każdy etap procesu konfiguracji.



### Pobierz



Wejdź na stronę [btc-heritage.com](https://btc-heritage.com) i kliknij "Pobierz aplikację".



![Page d'accueil Heritage](assets/fr/01.webp)



Wybierz wersję odpowiadającą Twojemu systemowi operacyjnemu (Linux 64bity lub Windows 64bity). Pliki binarne nie są podpisane cyfrowo, co może powodować ostrzeżenia dotyczące bezpieczeństwa.



![Page de téléchargement](assets/fr/02.webp)



### Instalacja w systemie Linux



W systemie Linux aplikacja jest dystrybuowana w formacie AppImage. Przed jej uruchomieniem należy zainstalować zależność `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Następnie utwórz plik wykonywalny i uruchom go:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Pierwsze uruchomienie



Przy pierwszym uruchomieniu kreator onboardingu oferuje trzy opcje:



![Onboarding initial](assets/fr/05.webp)





- Skonfiguruj Wallet z planem dziedzictwa**: Utwórz nowy wallet z planem dziedzictwa
- Odziedzicz bitcoiny**: Odzyskaj bitcoiny jako spadkobierca
- Eksploruj samodzielnie**: Eksploruj funkcje bez pomocy



Wybierz "Setup an Heritage Wallet", aby utworzyć swój pierwszy wallet.



### Połączenie sieciowe Bitcoin



Wybierz sposób połączenia z siecią Bitcoin:



![Choix connexion](assets/fr/06.webp)





- Korzystanie z usługi Heritage**: Zarządzana infrastruktura, prostsza dla spadkobierców
- Korzystanie z własnego węzła**: Połączenie z własnym węzłem Bitcoin Core lub Electrum



W tym samouczku użyjemy naszego własnego węzła.



### Zarządzanie kluczami prywatnymi



Wybierz sposób zarządzania kluczami prywatnymi:



![Gestion des clés](assets/fr/07.webp)





- Z urządzeniem sprzętowym Ledger** : Maksymalne bezpieczeństwo ze sprzętem wallet (zalecane)
- Lokalne przechowywanie z hasłem**: Klucze przechowywane lokalnie z ochroną hasłem
- Przywracanie istniejącego wallet** : Przywracanie z istniejącego seed



### Konfiguracja węzła



Jeśli używasz własnego węzła, aplikacja poprowadzi Cię przez jego konfigurację. Upewnij się, że węzeł Bitcoin lub Electrum jest :




- Zainstalowany i uruchomiony
- Zsynchronizowany z siecią Bitcoin
- Skonfigurowany do przyjmowania połączeń RPC (dla Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Kliknij "My Bitcoin node is up and running", gdy węzeł będzie gotowy.



### Panel stanu



Kliknij "Status" w prawym górnym rogu, a następnie "Open Configuration", aby uzyskać dostęp do parametrów połączenia.



![Panneau Status](assets/fr/09.webp)



Ustaw adres URL serwera Electrum (np. `umbrel.local:50001`, jeśli używasz Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Utworzenie wallet



Po nawiązaniu połączenia kliknij "Utwórz Wallet" w zakładce WALLETS.



![Créer wallet](assets/fr/11.webp)



Wyskakujące okienko wyjaśnia podzieloną architekturę Heritage :



![Architecture split](assets/fr/12.webp)



1. **Dostawca kluczy (offline)**: Zarządza kluczami prywatnymi i podpisuje transakcje. Może to być oprogramowanie Ledger lub wallet.


2. **Online Wallet**: Obsługuje synchronizację z siecią Bitcoin, tworzenie adresów i rozgłaszanie transakcji.



Wypełnij formularz tworzenia:



![Formulaire création wallet](assets/fr/13.webp)





- Nazwa Wallet**: Unikalna nazwa do identyfikacji wallet
- Dostawca kluczy**: Wybierz Local Key Storage dla tego samouczka
- Nowy/Przywróć**: Wybierz "New" (Nowy), aby utworzyć nowy generate
- Liczba słów**: 24 słowa zalecane dla maksymalnego bezpieczeństwa



Wprowadź silne hasło i wybierz opcje dla Wallet online:



![Options Online Wallet](assets/fr/14.webp)





- Węzeł lokalny**: Wykorzystuje własny węzeł Electrum lub Bitcoin Core
- Usługa Heritage**: Korzysta z usługi Heritage (zalecane dla funkcji powiadomień)



Kliknij "Utwórz Wallet", aby sfinalizować tworzenie.



### Interface z wallet



Urządzenie wallet zostało utworzone. Interfejs wyświetla :



![Interface wallet](assets/fr/15.webp)





- Równowaga
- Przyciski WYŚLIJ i ODBIERZ
- Historia transakcji
- Historia konfiguracji dziedzictwa
- Adresy wallet



### Tworzenie spadkobierców



Przejdź do zakładki "SPADKOBIERCY", aby utworzyć spadkobierców.



![Page Heirs](assets/fr/16.webp)



Wyskakujące okienko informacyjne wyjaśnia:




- Spadkobiercy to klucze publiczne Bitcoin powiązane z osobami fizycznymi
- Każdy spadkobierca ma swoją własną mnemotechnikę
- Pierwszy spadkobierca powinien być "kopią zapasową" dla ciebie (na wypadek utraty głównego wallet)



#### Tworzenie kopii zapasowej spadkobiercy



Kliknij "Utwórz spadkobiercę" i nadaj mu nazwę "Kopia zapasowa".



![Création héritier Backup](assets/fr/17.webp)



Wyskakujące okienko wyjaśnia, dlaczego 12-wyrazowe zdanie bez passphrase jest bezpieczne dla spadkobierców:


1. **Brak natychmiastowego dostępu**: Klucze spadkobiercy nie mają dostępu do środków do momentu wygaśnięcia blokady czasowej


2. **Wykrywanie kompromisów**: Jeśli ktoś uzyska dostęp do frazy, można zaktualizować konfigurację Heritage


3. **Długotrwała dostępność**: passphrase może zostać zapomniany po wielu latach



Konfiguracja spadkobiercy :



![Configuration héritier](assets/fr/18.webp)





- Dostawca kluczy** : Lokalny magazyn kluczy
- Nowość**: Wygeneruj nowy seed
- Liczba słów**: 12 słów



Zakończ tworzenie :



![Finalisation héritier](assets/fr/19.webp)





- Typ spadkobiercy**: Rozszerzony klucz publiczny
- Eksport do usługi**: Opcjonalnie, umożliwia automatyczne powiadamianie spadkobierców



Dziedzic kopii zapasowej został utworzony:



![Héritier créé](assets/fr/20.webp)



#### Zapisywanie frazy mnemonicznej spadkobiercy



Kliknij na spadkobiercę kopii zapasowej, a następnie na "Pokaż Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**WAŻNE: Zanotuj te 12 słów i przechowuj je w bezpiecznym miejscu. Jest to klucz do odzyskania środków.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Usuwanie seed z aplikacji



Po zapisaniu frazy, przejdź do parametrów spadkobiercy (ikona koła zębatego):



![Paramètres héritier](assets/fr/23.webp)



Użyj opcji "Strip Heir Seed", aby usunąć klucz prywatny z aplikacji. Potwierdź, że zapisałeś frazę.



![Strip Heir Seed](assets/fr/24.webp)



Jest to środek bezpieczeństwa: tylko klucz publiczny pozostaje w aplikacji, wystarczający do skonfigurowania dziedziczenia.



#### Utworzenie drugiego spadkobiercy



Powtórz ten proces, aby utworzyć drugiego spadkobiercę (np. "Satoshi"). Będziesz mieć teraz dwóch spadkobierców:



![Deux héritiers](assets/fr/25.webp)





- Kopia zapasowa**: Osobisty klucz awaryjny
- Satoshi**: Wyznaczony spadkobierca



### Konfiguracja dziedzictwa



Wróć do urządzenia wallet i kliknij ikonę Ustawienia:



![Paramètres wallet](assets/fr/26.webp)



W sekcji "Konfiguracja dziedzictwa" kliknij przycisk "Utwórz":



![Heritage Configuration](assets/fr/27.webp)



Ustal limity czasowe dla każdego spadkobiercy:



![Configuration délais](assets/fr/28.webp)





- Backup**: 180 dni (6 miesięcy) - Data zapadalności: 2026-06-18
- Satoshi**: 455 dni (15 miesięcy) - Data zapadalności: 2027-03-20



**Ważne**: Każdy spadkobierca musi mieć większe opóźnienie niż poprzedni. Pierwszy spadkobierca (Backup) będzie miał dostęp do środków jako pierwszy.



Skonfiguruj również :



![Configuration finale](assets/fr/29.webp)





- Data referencyjna**: Data rozpoczęcia obliczania czasu realizacji
- Minimalny termin zapadalności**: Minimalne opóźnienie po transakcji (zalecane 10 dni)



Kliknij "Utwórz", aby zatwierdzić konfigurację.



Konfiguracja Heritage jest teraz aktywna:



![Configuration active](assets/fr/30.webp)



Wyświetla obu spadkobierców wraz z ich terminami i datami wygaśnięcia.



### Zapisywanie deskryptorów



**Ważne**: Zachowaj deskryptory wallet. Bez nich, nawet przy użyciu frazy mnemonicznej, odzyskanie środków jest niemożliwe.



Kliknij "Deskryptory kopii zapasowej" :



![Bouton Backup](assets/fr/31.webp)



Zapisz plik JSON zawierający deskryptory Bitcoin:



![Backup descripteurs](assets/fr/32.webp)



Plik ten powinien zostać przekazany spadkobiercom wraz z odpowiednimi frazami mnemonicznymi.



### Odbieranie bitcoinów



Kliknij "RECEIVE", aby wybrać adres odbioru generate:



![Recevoir bitcoins](assets/fr/33.webp)



Gratulacje! Twój Heritage Wallet jest gotowy do otrzymywania bitcoinów. Każdy wygenerowany adres automatycznie uwzględnia warunki Heritage.



Po otrzymaniu transakcji saldo zostanie zaktualizowane:



![Solde mis à jour](assets/fr/34.webp)



Historia wyświetla transakcję i powiązaną konfigurację Heritage.



---

## Odzyskanie przez spadkobiercę



Po upływie ustalonego czasu spadkobierca może odzyskać środki.



### Wymagania wstępne



Spadkobierca potrzebuje :


1. Jego 12-wyrazowa fraza mnemotechniczna


2. Oryginalny plik kopii zapasowej deskryptora wallet (JSON)



### Tworzenie spadkobiercy Wallet



W zakładce "INHERITANCES" wyskakujące okienko przypomina o tych warunkach wstępnych:



![Page Heir Wallets](assets/fr/35.webp)



**Uwaga**: Bez pliku kopii zapasowej deskryptora dostęp do środków jest NIEMOŻLIWY, nawet przy użyciu poprawnej frazy mnemonicznej.



Kliknij "Utwórz spadkobiercę Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Prosimy o wypełnienie formularza:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Nazwa spadkobiercy Wallet**: Nazwa identyfikująca spadkobiercę wallet
- Dostawca kluczy** : Lokalny magazyn kluczy
- Przywróć**: Wybierz tę opcję, aby wprowadzić istniejącą frazę



Wprowadź 12 słów frazy mnemonicznej spadkobiercy i skonfiguruj Heritage Provider:



![Entrée mnemonic](assets/fr/38.webp)





- Dostawca dziedzictwa**: "Lokalny", aby użyć własnego węzła z plikiem kopii zapasowej



Załaduj plik kopii zapasowej JSON i kliknij "Create Heir Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Spadkobierca Wallet



Zostanie utworzony spadkobierca Wallet. Początkowo, jeśli blokada czasowa jeszcze nie wygasła, dziedziczenie nie jest dostępne:



![Pas d'héritage disponible](assets/fr/40.webp)



Po upływie opóźnienia i zsynchronizowaniu środków z siecią Bitcoin pojawią się one na liście spadków:



![Héritage disponible](assets/fr/41.webp)



Interfejs wyświetla :




- Typ klucza i odcisk palca
- Fundusze podlegające dziedziczeniu ogółem
- Aktualna kwota do wydania (0 sat, jeśli blokada czasowa jeszcze nie wygasła)
- Terminy zapadalności i wygaśnięcia



Po osiągnięciu daty zapadalności przycisk "Wydaj" przenosi bitcoiny do osobistego wallet.



---

## Najlepsze praktyki



### Zapisywanie deskryptorów



Deskryptory wallet są niezbędne do odtworzenia adresów Heritage. **Bez deskryptorów, nawet przy użyciu frazy mnemonicznej, nie będziesz w stanie znaleźć swoich funduszy.



### Bezpieczeństwo kluczy





- Jeśli to możliwe, użyj Ledger jako klucza głównego
- Nigdy nie przechowuj zdań spadkobierców w tym samym miejscu, co własnych
- Rozpowszechnianie informacji w wielu mediach i lokalizacjach



### Dokumentacja dla Twoich bliskich



Napisz jasne instrukcje wyjaśniające każdy krok procesu odzyskiwania. Spadkobiercy mogą nie być zaznajomieni z Bitcoin w krytycznym momencie.



## Alternatywy



Istnieją inne rozwiązania do zarządzania transmisją bitcoinów, w tym Liana i Bitcoin Keeper. Nasze samouczki znajdziesz poniżej:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Wnioski



Heritage pozwala zaplanować sukcesję Bitcoin w suwerenny sposób za pośrednictwem aplikacji Desktop. Wdrożenie wymaga przemyślanego rozważenia odpowiednich ram czasowych i zabezpieczenia tajemnic. Nie zapomnij przekazać ich swoim spadkobiercom:




- Ich 12-wyrazowa fraza mnemotechniczna
- Plik kopii zapasowej deskryptora
- Instrukcje odzyskiwania



## Zasoby





- [Oficjalna strona Heritage](https://btc-heritage.com)
- [Dokumentacja CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)