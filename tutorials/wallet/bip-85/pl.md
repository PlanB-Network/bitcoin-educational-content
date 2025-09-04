---
name: BIP-85
description: Jak mogę użyć BIP-85 do generate wielu fraz źródłowych z głównego seed?
---
![cover](assets/cover.webp)



## 1. Zrozumienie BIP-85



### 1.1 Czym jest BIP-85?



BIP-85 to zaawansowana funkcja, która pozwala utworzyć kilka **fraz drugorzędnych seed** z jednej **frazy głównej seed**.



Każde zdanie dodatkowe seed można wykorzystać do utworzenia całkowicie niezależnego portfela Bitcoin. Portfele te mogą być wykorzystywane do różnych celów: Hot Wallet na telefonie komórkowym, portfel dla krewnego, oddzielny portfel oszczędnościowy itp.



Wszystkie podfrazy seed są **matematycznie pochodne**, ale **niemożliwe jest prześledzenie wstecz do głównej frazy seed** z podfrazy. Zapewnia to całkowite oddzielenie każdego portfela.



Tak długo, jak masz dostęp do głównej frazy seed (i powiązanej passphrase, jeśli jej używasz), możesz zregenerować dowolną drugorzędną frazę seed **identycznie**, bez konieczności zapisywania jej osobno.



### 1.2 Dlaczego warto korzystać z BIP-85?



BIP-85 jest przydatny, jeśli chcesz :





- Tworzenie kilku niezależnych portfeli Bitcoin bez wielu kopii zapasowych
- Zarządzaj swoimi środkami według różnych zastosowań (oszczędności, wydatki, rodzina, projekty)
- Gwarantowanie zabezpieczeń dla krewnych (funkcja "wujka Jima")
- Usunięcie portfela bez utraty dostępu do środków
- Uprość swoje zabezpieczenia: tylko jedna fraza kluczowa seed do ochrony



### 1.3 Zalety w porównaniu z BIP-32



Z BIP-32, pojedyncze zdanie seed może być użyte do generate pełnej hierarchii kont i adresów Bitcoin, używając ścieżek pochodnych (na przykład: `m/44'/0'/0'/0/0`). Każda ścieżka może reprezentować oddzielne konto, ale **wszystkie pozostają powiązane z tym samym zdaniem seed**. Tak więc, jeśli ta fraza seed zostanie naruszona, **wszystkie konta pochodne staną się dostępne**.



Dzięki BIP-85, główne zdanie seed może być użyte do generate kilku całkowicie niezależnych zdań seed: **jeśli jedno z tych drugorzędnych nasion zostanie naruszone, atakujący nigdy nie będzie w stanie wrócić do głównego seed ani uzyskać dostępu do innych portfeli**.


Umożliwia to rozdzielenie ryzyka:





- Możesz użyć dodatkowego seed do Hot Wallet lub tymczasowego użytku, akceptując wyższą ekspozycję.
- Nawet jeśli ten Hot Wallet zostanie naruszony, pozostałe środki, chronione przez inne nasiona wtórne lub przechowywane offline, **pozostają bezpieczne**.



Z drugiej strony, zarówno w przypadku BIP-32, jak i BIP-85, jeśli główny seed zostanie naruszony, **wszystkie fundusze są narażone**. Dlatego kluczowe jest, aby chronić go na najwyższym poziomie bezpieczeństwa.



![image](assets/fr/02.webp)


## 2. Praktyczne przypadki użycia BIP-85



BIP-85 umożliwia tworzenie wielu portfeli Bitcoin z pojedynczej frazy głównej seed, każdy z własną frazą dodatkową seed. Oto pięć praktycznych przypadków użycia do organizowania i zabezpieczania funduszy Bitcoin. Każdy przypadek wyjaśnia, dlaczego korzystanie z BIP-85 jest bardziej praktyczne niż zarządzanie wieloma kontami za pomocą pojedynczej frazy seed za pośrednictwem BIP-32.



### 2.1 Ograniczenie ryzyka mniej bezpiecznego portfela





- Scenariusz**: Używasz "Hot Wallet" Wallet (zainstalowanego na urządzeniu podłączonym do Internetu), do codziennych transakcji.
- Rozwiązanie BIP-85**: Tworzysz drugorzędną frazę seed dedykowaną dla tego portfela.
- Przewaga nad BIP-32**: Nie trzeba importować głównej frazy seed do telefonu, co zmniejsza ryzyko włamania. Narażona jest tylko fraza dodatkowa seed, co chroni inne portfele. W przypadku BIP-32 musisz użyć głównej frazy seed i ścieżki obejścia, ujawniając wszystkie swoje środki.



### 2.2 Tworzenie portfolio dla członka rodziny





- Scenariusz**: Ustawiasz Bitcoin Wallet dla kogoś bliskiego (np. swojej matki), jednocześnie mogąc go odzyskać, jeśli go zgubi.
- Rozwiązanie BIP-85**: Tworzysz dedykowane zdanie pomocnicze seed i udostępniasz tylko to zdanie.
- Przewaga nad BIP-32**: W przypadku BIP-32 utworzenie konta dla bliskiej osoby wymaga albo udostępnienia głównej frazy seed, ryzykując wszystkie środki i komplikując zarządzanie dla bliskiej osoby (zarządzanie ścieżkami rozgałęzień), albo utworzenia nowej frazy seed do zapisania oprócz głównej frazy seed.



### 2.3 Ułatwienie zarządzania oddzielnymi portfelami





- Scenariusz**: Oddzielasz swoje bitcoiny do różnych celów (np. długoterminowe oszczędności, fundusze inne niż KYC).
- Rozwiązanie BIP-85**: Tworzysz drugorzędne frazy seed dedykowane dla każdego celu.
- Przewaga nad BIP-32**: W przypadku BIP-32 wszystkie konta mają tę samą frazę seed, co komplikuje zarządzanie w portfelach stron trzecich, wymagając zarządzania ścieżkami pochodnymi, takimi jak `m/44'/0'/0'`. Ponadto nie jest możliwe przypisanie oddzielnego konta dla każdego urządzenia (np. "oszczędności na karcie Coldcard", "codziennie na telefonie komórkowym", "wakacje na Trezorze"). BIP-85 przypisuje unikalną frazę drugorzędną seed dla każdego celu, która jest łatwa do zidentyfikowania i zaimportowania oddzielnie na każdym urządzeniu.



### 2.4 Korzystanie z tymczasowego Wallet dla transakcji





- Scenariusz**: Potrzebujesz tymczasowego portfela do jednorazowej transakcji lub w celu zachowania poufności (np.: mieszanie funduszy, interakcja z Exchange KYC itp.).
- Rozwiązanie BIP-85**: Tworzysz zdanie podrzędne seed, używasz go do transakcji, a następnie niszczysz w razie potrzeby, wiedząc, że można je zregenerować.
- Przewaga nad BIP-32**: W przypadku BIP-32 konto tymczasowe jest zależne od głównego zdania seed, narażając wszystkie środki w przypadku naruszenia bezpieczeństwa.





## 3. Przed rozpoczęciem





- Sprzęt** (opcjonalnie)
 - Coldcard Mk4 lub Q1
 - Karta MicroSD





- Podstawowa wiedza
 - Zrozumienie zwrotów Mnemonic (BIP-39): lista od 12 do 24 słów do zapisania w portfolio.
 - Dowiedz się, czym jest Bitcoin Wallet: oprogramowanie lub urządzenie do zarządzania bitcoinami i jak je przywrócić za pomocą frazy Mnemonic.
 - Więcej zasobów w załącznikach.





- Kompatybilne** oprogramowanie
 - Sparrow wallet (komputer, tylko do oglądania lub zaawansowanego zarządzania)
 - Nunchuck (mobilny, do wielu podpisów)
 - BlueWallet (mobilny)
 - ...





- 3.4 Konfiguracja karty Coldcard**
 - Zainicjuj zdanie seed składające się z 24 słów na karcie Coldcard.
 - Opcjonalnie: Dodaj passphrase, aby zabezpieczyć dostęp do oddziałów BIP-85.
 - Aktywuj przydatne opcje: NFC (dla eksportu), wyłączenie USB na baterii (bezpieczeństwo).




## 4. Samouczek krok po kroku



Wykonaj poniższe kroki, aby utworzyć, używać i pobierać dodatkowy Mnemonic z BIP-85 na karcie Coldcard.



### 4.1 generate a seed zdanie odrębne



Frazę drugorzędną seed utworzysz na podstawie frazy głównej seed.


Włącz kartę Coldcard i wprowadź kod PIN.





- 1. Jeśli zastosowałeś passphrase do swojego głównego seed:**
 - Na ekranie głównym przejdź do `passphrase`.
    - Wybierz `Add Word` i wprowadź swoje hasło.
    - Naciśnij przycisk "Zastosuj".
    - Sprawdź tożsamość Wallet: Przejdź do `Advanced > View Identity`, aby zanotować odcisk palca Wallet.





- 2. Przejdź do menu BIP-85**
 - Na ekranie głównym przejdź do `Zaawansowane > Pochodna seed B85`
 - Przeczytaj ostrzeżenie i potwierdź.



ColdCard informuje, że wygenerowane nasiona pochodzą matematycznie z głównego seed, ale są całkowicie niezależne kryptograficznie.


![image](assets/fr/03.webp)





- 3. Wybierz format


Wybierz format frazy seed: 12, 18 lub 24 słowa. Sprawdź liczbę słów akceptowanych przez Wallet, do którego chcesz zaimportować frazę seed.


![image](assets/fr/04.webp)





- 4. Wybierz indeks
 - Wprowadź indeks z zakresu od 0 do 9999.
 - Indeks ten ma kluczowe znaczenie dla regeneracji wtórnego seed w późniejszym terminie. Należy go starannie przechowywać z etykietą taką jak: "Indeks 1 = Wallet mobilny", "Indeks 2 = projekt rodzinny", "Indeks 4 = mieszanka testowa", ....
 - Jeśli go zgubisz, nie stracisz dostępu do swoich środków, ale będziesz musiał przetestować kombinacje od 0 do 9999, aby je znaleźć.


![image](assets/fr/05.webp)





- 5. Uwaga lub eksport zdania dodatkowego seed**


ColdCard wyświetla teraz nowe zdanie pomocnicze seed. Można :




 - Notatka ręcznie**.
 - Prasa :
     - 1`, aby zapisać go na karcie SD
     - `2`, aby **wprowadzić tryb "użyj tego seed"** na karcie ColdCard (przydatne do eksportowania lub podpisywania transakcji)
     - 3`, aby wyświetlić **kod QR** (do zeskanowania za pomocą aplikacji mobilnej, takiej jak BlueWallet lub Nunchuck)
     - 4`, aby wysłać przez **NFC**



💡 W tym momencie masz niezależną frazę seed, możliwą do użycia w dowolnym Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Korzystanie z dodatkowego seed



Możesz teraz użyć tego pochodnego seed do utworzenia nowego portfela w :




- aplikacja mobilna
- kolejny Hardware Wallet
- portfel Multisig



### 4.3 Odzyskiwanie utraconej frazy drugorzędnej seed



Aby odzyskać dodatkowy seed w dowolnym momencie, należy powtórzyć ten proces:


1. Uruchom ponownie kartę ColdCard


2. Wprowadź kod PIN


3. Wprowadź swój passphrase, jeśli jest zdefiniowany


4. Przejdź do `Zaawansowane > Wyprowadź seed B85`


5. Wybierz format (12/18/24 słów)


6. Wprowadź ten sam indeks (np. `1`)


7. Otrzymasz dokładnie taki sam wtórny seed




## 5. Ograniczenia, ryzyko i najlepsze praktyki



### 5.1 Zależność od zdania głównego seed + passphrase



Użycie BIP85 opiera się całkowicie na 24-wyrazowym zdaniu głównym seed, a także na passphrase, jeśli je zastosowałeś.




- Z tych dwóch Elements można zregenerować wszystkie wtórne frazy seed.
- Bez jednego z tych 2 Elements tracisz dostęp do wszystkich portfeli instrumentów pochodnych.



### 5.2 Ryzyko związane z konfiguracją z wieloma podpisami



Zdecydowanie odradzamy używanie drugorzędnych fraz seed generowanych z tej samej podstawowej frazy seed w konfiguracji multi-sig: jeśli urządzenie lub podstawowa fraza seed zostanie naruszona, wszystkie klucze multi-sig mogą zostać ponownie wygenerowane przez atakującego.



### 5.3 Kompatybilność oprogramowania



Nie wszystkie aplikacje bezpośrednio obsługują derywację BIP85. Jednak nasiona generowane przez BIP85 są standardowymi nasionami BIP39 (12, 18 lub 24 słowa), a zatem mogą być używane w dowolnym portfolio kompatybilnym z BIP39.



### 5.4 Rejestr kont BIP85



Zaleca się prowadzenie aktualnego osobistego rejestru fraz drugorzędnych seed.




- Pozwala to szybko sprawdzić, który indeks BIP85 odpowiada danemu portfelowi, bez konieczności utrzymywania drugorzędnych fraz seed.
- Rejestr ten powinien pozostać minimalistyczny, bez wyraźnej wzmianki o Bitcoin i powinien być przechowywany oddzielnie od głównego seed. Pamiętaj, aby wspomnieć o nim w swoim planie spadkowym.



Rejestr może zawierać :




- używany indeks bIP85 (liczba od 0 do 9999)
- nazwa użytkowa lub referencyjna (np. Hot Wallet, oszczędności osobiste, Wallet od mamy)
- w razie potrzeby odcisk palca Wallet do weryfikacji w ColdCard



### 5.5 Kopia zapasowa



Kopie zapasowe muszą zawierać :




- główny seed
- gW-76 (jeśli jest używany)



Nigdy nie przechowywać razem:




- główne seed i passphrase
- główny seed i rejestr rachunków BIP85



Więcej zasobów w załącznikach.




## DODATKI



## A.1 Słowniczek





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [fraza seed](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Zapisz frazę odzyskiwania



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Zrozumienie passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Jak działają portfele Bitcoin



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f