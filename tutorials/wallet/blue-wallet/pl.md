---
name: Blue Wallet

description: Bitcoin Radykalnie prosty i potężny portfel
---
![cover](assets/cover.webp)



Rozpoczęcie korzystania z Bitcoin wydaje się być dużym wyzwaniem dla osób, które sceptycznie podchodzą do prostoty jego użytkowania. Znalezienie odpowiednich narzędzi, które zapewnią tę prostotę, staje się zatem niezwykle ważne dla lepszego przyjęcia Bitcoin jako medium Exchange, a nie tylko jako magazynu wartości.



W tym samouczku przyjrzymy się Blue Wallet, prostemu, ale bardzo skutecznemu Bitcoin Wallet, który pozwala zarządzać bitcoinami osobiście, a także tworzyć spółdzielnie zarządzające oparte na [Multisig](https://planb.network/resources/glossary/multisig) (nie martw się, wrócimy do tego).



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## Rozpoczęcie pracy z Blue Wallet



Blue Wallet to open source'owy, samoobsługowy Bitcoin Wallet, który pozwala przejąć kontrolę nad bitcoinami. Jest on dostępny jako aplikacja mobilna na platformy Android i iOS. W tym samouczku będziemy opierać się na wersji na Androida, jednak wszystkie procesy, które zostaną opracowane, są równie ważne na iOS.



![download](assets/fr/01.webp)



⚠️ Pamiętaj, aby pobrać aplikację Blue Wallet Bitcoin Wallet na oficjalnej platformie, aby zagwarantować jej autentyczność i chronić swoje bitcoiny przed możliwymi wyciekami i włamaniami.



Po zainstalowaniu można utworzyć nowy Wallet i zapisać 12 słów odzyskiwania lub zaimportować istniejący Bitcoin Wallet. Dowiedz się, jak wykonać skuteczną kopię zapasową słów kluczowych, aby nie stracić dostępu do swoich bitcoinów.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Dzięki Blue Wallet możesz tworzyć oddzielne, dedykowane portfele Bitcoin. Na przykład, możesz mieć jeden Wallet dla swoich oszczędności, a drugi dla codziennych wydatków, wszystko w tej samej aplikacji.



![home](assets/fr/02.webp)



## Rodzaje portfeli



W Blue Wallet znajdziesz dwa natywne typy portfeli Bitcoin.



### Portfel Bitcoin



Jeśli jesteś przyzwyczajony do innych portfeli Bitcoin, takich jak Phoenix lub Aqua, nie będziesz wcale odstawał od Interface z portfelem Bitcoin Blue Wallet.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Niebieski Wallet reprezentuje standardowy Wallet w ekosystemie Bitcoin. Możesz wydawać bitcoiny, o ile jesteś w posiadaniu słów odzyskiwania, które zapewnią ważny podpis w sieci w celu uwierzytelnienia, że jesteś właścicielem bitcoinów.



Aby utworzyć portfel Bitcoin, kliknij przycisk **Dodaj teraz**, wprowadź nazwę portfela i wybierz typ Bitcoin.



![bitcoin-wallet](assets/fr/03.webp)



Po kliknięciu podglądu Bitcoin Wallet będziesz mógł przeglądać historię transakcji oraz wysyłać i odbierać bitcoiny.



⚠️ Wszystkie transakcje w Bitcoin Wallet znajdują się w głównym łańcuchu protokołu Bitcoin (Mainnet).





- Odbieranie bitcoinów za pomocą Bitcoin Blue Wallet jest intuicyjne. W dolnej części ekranu kliknij przycisk **Odbierz**. Udostępnij kod QR lub swój Bitcoin Address nadawcy, aby mógł wysłać Ci bitcoiny.



Możesz także skonfigurować predefiniowaną kwotę, aby określić kwotę Bitcoin, którą chcesz otrzymywać.



![receive-bitcoin](assets/fr/04.webp)





- Za pomocą przycisku **Wyślij** wyślij bitcoiny do Bitcoin Address, ustawiając żądaną kwotę i zatwierdzając transakcję.



![send-bitcoin](assets/fr/05.webp)



Blue Wallet umożliwia skonfigurowanie parametrów przesyłki Bitcoin według własnego uznania.



Możesz zatem wybrać współczynnik opłaty transakcyjnej, który Ci odpowiada, jeśli chcesz, aby Twoja transakcja została szybko zweryfikowana w Mempool i włączona do bloku przez górników. W zależności od wybranego współczynnika, górnicy będą traktować transakcję priorytetowo w mniejszym lub większym stopniu. Więcej informacji można znaleźć w naszym samouczku dotyczącym przestrzeni Mempool.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- Dzięki Blue Wallet możesz dodać wielu odbiorców do jednej przesyłki.



Po dodaniu Bitcoin Address pierwszego odbiorcy, w opcjach kliknij na **Dodaj odbiorcę**, dodaj Bitcoin Address, a następnie ustaw kwotę do wysłania do tego odbiorcy i tak dalej. Blue Wallet wyśle bitcoiny dla wielu przesyłek w oparciu o Twoją pojedynczą akcję.



![add-recipients](assets/fr/07.webp)



Możesz usunąć jednego lub wszystkich odbiorców, klikając odpowiednio **Usuń odbiorcę** i **Usuń wszystkich odbiorców**.



![remove-recipient](assets/fr/08.webp)





- **Zawyżone opłaty**: Dokonałeś transakcji, której potwierdzenie zajmuje dużo czasu? Włączając inflację opłat, możesz dodać dodatkowe opłaty transakcyjne do oczekującej transakcji, aby przyspieszyć jej potwierdzenie.



![bumping](assets/fr/09.webp)



### Portfel Multisig



Multisig (wielopodpisowy) Wallet reprezentuje Wallet utworzony z połączenia określonej liczby (minimum 2) portfeli Bitcoin. W tym typie Wallet, w zależności od wybranej konfiguracji i metody, wydawanie bitcoinów staje się działaniem zbiorowym i opartym na współpracy.



W Blue Wallet możesz tworzyć portfele z wieloma podpisami dla swojego stowarzyszenia, rodziny, firmy. W tej sekcji zbadamy każdy aspekt tego specjalnego rodzaju portfela.



Dodaj nowy portfel i wybierz typ **Multisig Vault**, aby utworzyć portfel z wieloma podpisami.



![multisig-vault](assets/fr/10.webp)



Zdefiniuj konfigurację m-de-n w swojej organizacji z wieloma podpisami, klikając **Ustawienia sejfu**.



⚠️ W konfiguracji m-of-n, **m** reprezentuje minimalną liczbę podpisów wymaganych do zatwierdzenia transakcji, a **n** liczbę portfeli w organizacji.



Pamiętaj, aby zdefiniować minimalną liczbę podpisów (m) dla większości organizacji. Na przykład konfiguracja 2 na 3 z wieloma podpisami wymaga, aby dwa portfele w organizacji podpisały transakcję, zanim będzie można ją przeprowadzić.



zdefiniowanie konfiguracji m-of-n, gdzie n równa się m, jest dużym ryzykiem. Kiedy członek traci dostęp do swojego Wallet, tracisz autoryzację do wydawania bitcoinów w Wallet.



Oto kilka przykładów optymalnych konfiguracji zapewniających bezpieczeństwo i dostępność bitcoinów:





- wielokrotny podpis 2-de-3.





- podpis 5-de-7 multi.



![vault-settings](assets/fr/11.webp)



Zachowaj najlepsze praktyki, wybierając format P2WSH.



❗ **[P2WSH](https://planb.network/resources/glossary/p2wsh) lub Pay to Witness Script Hash** to metoda blokowania, która blokuje wychodzące bitcoiny transakcji (Outputs) do Hash niestandardowego skryptu, który konfiguruje Blue Wallet. Główną zaletą tego typu blokady jest to, że zmniejsza ona rozmiar danych transakcji i pośrednio pozwala płacić niższe opłaty transakcyjne.



Utwórz lub zaimportuj każdy z **n** portfeli w swojej konfiguracji. W naszym samouczku będziemy używać konfiguracji 2 z 3 z wieloma podpisami. Pamiętaj, aby zapisać słowa odzyskiwania dla każdego portfela osobno.



![vault-keys](assets/fr/12.webp)





- Odbieranie bitcoinów



Na stronie Multisig Wallet znajduje się historia transakcji oraz przyciski Odbierz i Wyślij.



Odbieranie bitcoinów w Wallet z wieloma podpisami jest takim samym procesem, jak w przypadku standardowego Bitcoin Wallet.





- **Wysyłanie bitcoinów**:



Zarządzając Wallet z wieloma podpisami, wydawanie bitcoinów staje się czynnością złożoną, czy to z innymi osobami, czy z drugim własnym Wallet. Pojedynczy podpis Wallet nie jest już wystarczający. Dodaje to Layer bezpieczeństwa do twoich bitcoinów, ponieważ złośliwa osoba nie będzie w stanie wydać tych bitcoinów, gdy wejdzie w posiadanie tylko jednego z twoich kluczy prywatnych.



Podobnie jak w przypadku standardowego portfela Bitcoin Blue Wallet, można zdefiniować wielu odbiorców w opcji **Dodaj odbiorców**.



Podczas zatwierdzania transakcji potrzebny będzie drugi podpis, aby zatwierdzić wydanie bitcoinów. Pamiętaj, że jesteśmy w konfiguracji 2 na 3 z wieloma podpisami.



Drugi sygnatariusz Wallet, jeśli jest również użytkownikiem, może podpisać transakcję, nawet jeśli jest poza Internetem (bez Wi-Fi, bez danych mobilnych), skanując kod QR [częściowo podpisanej transakcji](https://planb.network/resources/glossary/psbt), którą właśnie utworzyłeś.



![mutisig-send](assets/fr/13.webp)





- Idź dalej z portfelem **Multi signature**:



Na Interface wielopodpisowego Wallet kliknij przycisk **Zarządzaj kluczami**.



Zapominając jednego ze słów odzyskiwania jednego z portfeli sygnatariuszy (**Zapomnij o tym seed...**), powiadamiasz Blue Wallet o usunięciu kopii zapasowej tych słów z jego pamięci. Zostanie zatem utworzona zewnętrzna kopia zapasowa.



![revoke-key](assets/fr/14.webp)



Wykonując tę czynność, zachowujesz tylko klucz publiczny powiązany z tymi słowami odzyskiwania.



⚠️ Przechowywanie tylko kluczy publicznych (XPUB) pozwala na dodanie dodatkowego poziomu bezpieczeństwa do konfiguracji 2 na 3 z wieloma podpisami. Rzeczywiście, przechowywanie wszystkich słów odzyskiwania w jednym miejscu może być szkodliwe, gdy telefon jest atakowany. Atakujący mający dostęp tylko do jednego **VAULT** (słowa kluczowego), którego używasz do podpisywania transakcji, nie będą w stanie ukraść twoich bitcoinów (wymagane minimum 02 podpisy), ponieważ klucze publiczne nie mogą być używane do podpisywania transakcji.



## Więcej opcji z Blue Wallet



### Poprawa bezpieczeństwa dostępu do portfela



W Ustawieniach, opcja **Bezpieczeństwo** pozwala zdefiniować użycie odcisku palca do przeprowadzenia transakcji, eksportu lub usunięcia Wallet. Uwierzytelnia to osobę korzystającą ze smartfona.



![biometry](assets/fr/15.webp)



## Aktywuj Lightning Network



Lightning Network nie jest już natywnie obsługiwany w aplikacji Blue Wallet.



W menu Ustawienia > **Ustawienia Lightning** można ręcznie powiązać urządzenie Lightning Wallet podczas korzystania z węzła Lightning Network Daemon (LND). Zainstaluj koncentrator LND, a następnie skojarz Wallet, wprowadzając łącze wygenerowane przez koncentrator.



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Ukończyłeś już niebieską wycieczkę po Wallet i jesteś gotowy do korzystania z Bitcoin w całej jego prostocie i mocy. Zalecamy, abyś zrobił kolejny krok i dowiedział się, jak możesz akceptować płatności Bitcoin w swoich sklepach dzięki mocy Lightning.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06