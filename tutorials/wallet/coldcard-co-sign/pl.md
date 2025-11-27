---
name: COLDCARD - Co-Sign
description: Odkryj funkcję Co-Sign i korzystaj z niej na swojej karcie COLDCARD
---

![cover](assets/cover.webp)


*Uwaga: Ten samouczek jest przeznaczony dla osób, które mają już pewne doświadczenie z portfelami wielopodpisowymi, urządzeniami Coinkite i oprogramowaniem takim jak Sparrow wallet lub Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Dlaczego ColdCard Co-Sign?



Ta funkcja umożliwia dodanie **warunków wydatków** do urządzenia ColdCard (Q lub Mk4) w sposób podobny do sprzętowego modułu bezpieczeństwa (HSM), aby chronić środki, zachowując jednocześnie znaczną elastyczność i kontrolę nad nimi.



Warunkami wydatkowania mogą być na przykład





- Limity wielkości**: ograniczają ilość bitcoinów, które można wydać w pojedynczej transakcji.
- Limity prędkości:** decydują o tym, ile transakcji można przeprowadzić w jednostce czasu (na godzinę, dzień, tydzień itp.), wymagając minimalnej liczby bloków między nimi.
- Wstępnie zatwierdzone adresy:** Zezwalaj na wysyłanie bitcoinów tylko na wstępnie zatwierdzone adresy.
- Uwierzytelnianie dwuskładnikowe:** Wymaga potwierdzenia z aplikacji mobilnej 2FA innej firmy (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) na smartfonie/tablecie z obsługą NFC i dostępem do Internetu.



**Jak to działa



Poprzez dodanie drugiego seed do urządzenia ColdCard Mk4 lub Q, zwanego "kluczem polityki wydatków", który będziemy nazywać w tym samouczku "kluczem C".


Oprócz tego dodatkowego seed, zostaniesz poproszony o Supply co najmniej jeden dodatkowy klucz (XPUB), który nazwiemy "kluczem zapasowym", aby utworzyć Wallet Multisig 2-on-N.



Podsumowując, zamierzamy utworzyć Wallet Multisig, a urządzenie ColdCard będzie zawierać 2 klucze prywatne potrzebne do wydawania środków, klucz główny seed urządzenia i "klucz zasad wydawania".



Za każdym razem, gdy "klucz C" zostanie poproszony o podpisanie, zastosowanie będą miały określone warunki wydatków, a karta ColdCard podpisze się tylko wtedy, gdy transakcja jest z nimi zgodna.



Jeśli chcesz zrezygnować z tych warunków wydatków, możesz to zrobić:




- podpisując jednym z kluczy zapasowych i ręką seed lub 2 kluczami zapasowymi w zależności od rozmiaru Multisig.
- wprowadzając "Spending Policy Key" lub "C Key" w menu "Co-Sign". **Ten ostatni nie może być konsultowany bezpośrednio na urządzeniu, w przeciwnym razie każdy mógłby anulować skonfigurowane warunki wydatków **




## Konfigurowanie podpisu współbieżnego ColdCard



![video](https://youtu.be/MjMPDUWWegw)



### 1- Aktywacja funkcji



Przede wszystkim upewnij się, że Twoje urządzenie ma co najmniej najnowszą wersję oprogramowania układowego:




- Mk4: v5.4.2
- Q: v1.3.2Q




W Mk4 lub ColdCardQ przejdź do *Advanced Tools > ColdCard Co-Signing*.



![Co-Sign](assets/fr/01.webp)



*W poniższym samouczku zrzuty ekranu zostaną wykonane na ColdCardQ dla wygody, ale kroki i menu są identyczne między Mk4 i Q.*



Wyświetlane jest podsumowanie funkcji.


Terminologia używana do oznaczania kluczy, której użyjemy ponownie w Wallet z wieloma podpisami 2 na 3, który zamierzamy utworzyć, to:



Klucz A = karta główna Coldcard seed


Klucz B = klucz zapasowy


Klucz C = Klucz polityki wydatków



Kliknij **"ENTER "**.



![Co-Sign](assets/fr/02.webp)



Następnym krokiem jest podjęcie decyzji, który klucz prywatny będzie działał jako "Spending Policy Key" lub "Key C".



Widzimy, że mamy do wyboru kilka opcji:





- Lub naciśnij **"ENTER "**, aby generate utworzył nowe zdanie seed składające się z 12 słów.





- Kliknij **"(1) "**, aby zaimportować istniejący 12-słowny seed, lub wybierz **"(2) "**, aby zaimportować istniejący 24-słowny seed.





- Lub naciśnij **"(6) "**, aby zaimportować seed ze skarbca urządzenia.



Na potrzeby tego samouczka zdecydowaliśmy się zaimportować istniejący 12-słowny seed, naciskając **"(1) "**. Może to być dowolny seed BIP39, który już posiadasz i dla którego oczywiście masz kopię zapasową.



Za pomocą klawiatury wprowadź 12 słów seed. W tym przykładzie wybierzemy ważną frazę seed wołowina x 12. Następnie naciśnij **"ENTER "**.


*Uwaga: jeśli nie masz kopii zapasowej tego seed, nie będziesz już mógł modyfikować ustawień "Co-Sign" na swoim urządzeniu, aby zmienić warunki wydatków*



Funkcja "Co-Sign" jest teraz aktywna na urządzeniu. Następnie musimy wybrać nasze warunki wydatków, a następnie dokończyć tworzenie wielopodpisowego Wallet.



![Co-Sign](assets/fr/03.webp)



### 2- Wybierz warunki wydatków lub "*politykę wydatków*"



Tutaj określamy warunki wydatków, które muszą być spełnione, gdy **"Klucz C "** lub **"Klucz polityki wydatków**" podpisuje transakcję.



W menu **"Co-Signing "** kliknij **"Spending Policy**".



Następnie można wybrać maksymalną wielkość, tj. maksymalną liczbę satoshi, które można wydać w pojedynczej transakcji.



W tym przykładzie wybierzemy maksymalną wielkość **21212** satoshi. Kliknij **"ENTER "**, aby potwierdzić.




![Co-Sign](assets/fr/04.webp)



Następnie wybieramy maksymalną prędkość, tj. liczbę transakcji, które urządzenie będzie w stanie podpisać w jednostce czasu. W tym samouczku wybierzemy nieograniczoną prędkość, tj. bez limitu liczby transakcji.




![Co-Sign](assets/fr/05.webp)



### 3- Utwórz Wallet Multisig 2-on-N



Nadal musimy wybrać trzeci klucz dla naszego Wallet Multisig, tj. **"Backup Key "** (Klucz B), oprócz **głównego seed** urządzenia (Klucz A) i **"Spending Policy Key "** (Klucz C).



Nasz "klucz B" będzie musiał zostać zaimportowany za pomocą karty SD lub kodu QR w przypadku ColdCardQ.


Aby to zrobić, będziemy potrzebować drugiego urządzenia ColdCard Mk4 lub Q, na którym używany jest nasz "Klucz B".



Na drugim urządzeniu zawierającym **"Klucz zapasowy "**, powiedzmy ColdCard Mk4 w tym przykładzie, przejdź z menu głównego do **"Ustawienia "**, następnie **"Multisig Wallet"**, a na końcu **"Eksportuj Xpub "**.


(Jeśli Twoim drugim urządzeniem jest ColdCardQ, będziesz mieć oczywiście możliwość wyeksportowania Xpub za pomocą kodu QR).





![Co-Sign](assets/fr/06.webp)





Na następnym ekranie włóż kartę SD i kliknij przycisk **"Zatwierdź "** w prawym dolnym rogu. Następnie kliknij **"(1) "**, aby zapisać plik na karcie SD.



Plik będzie zawierał odcisk palca klucza publicznego (*fingerprint*) w swojej nazwie i będzie miał postać `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Następnie włóż kartę SD do "początkowego" ColdCardQ, aby zaimportować nasz "klucz zapasowy" (klucz B).


W menu "ColdCard Co-Signing" wybierz "Build 2-of-N", a następnie na następnym ekranie kliknij **"ENTER "**, a następnie ponownie **"ENTER "**, aby zaimportować "Backup Key" z karty SD.



![Co-Sign](assets/fr/08.webp)



Na następnym ekranie pozostaw "Numer konta" pusty (chyba że wiesz dokładnie, co robisz) i ponownie kliknij **"ENTER "**.



![Co-Sign](assets/fr/09.webp)



Wreszcie jesteśmy gotowi do użycia naszego nowego Wallet Multisig 2-sur-3, złożonego w następujący sposób:



Klucz A= Coldcard Q master seed


Klucz B= Klucz zapasowy (właśnie zaimportowany z drugiego urządzenia Coldcard)


Klucz C= Klucz polityki wydatków (jeśli jest używany do podpisywania, nakłada predefiniowane warunki wydatków)



## Podpisz z Sparrow wallet



W razie potrzeby zapoznaj się z poniższymi samouczkami, aby zapoznać się z oprogramowaniem Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Eksport Wallet Multisig 2-sur-3 do Sparrow wallet



Teraz musimy wyeksportować nasze Wallet Multisig do Sparrow, abyśmy mogli umieścić tam nasze pierwsze satoshi.



W menu głównym aplikacji ColdCardQ wybierz **"Ustawienia "**, a następnie **"Portfele Multisig"**.


Zostanie wyświetlony zestaw portfeli Multisig znanych z karty ColdCard, z liczbą kluczy "2/3" (2-sur3). Wybierz Multisig **"ColdCard Co-Sign "**, który właśnie utworzyliśmy, a następnie kliknij **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Na koniec wybierz metodę, która pozwoli Ci wyeksportować Wallet do Sparrow. W naszym przypadku wybierzemy kartę SD i klikniemy **"(1) "** po włożeniu karty SD do gniazda A urządzenia.



![Co-Sign](assets/fr/11.webp)



Następnie w Sparrow wallet wybierz "Importuj Wallet".



![Co-Sign](assets/fr/12.webp)



Następnie kliknij **"Importuj plik "**. Następnie wybierz plik **"export-Coldcard_Co-sign.txt "** na karcie SD.



![Co-Sign](assets/fr/13.webp)



Nadaj swojemu Wallet nazwę, która będzie wyświetlana w Sparrow, i wybierz hasło do szyfrowania Wallet (lub nie).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Jesteśmy teraz gotowi, aby otrzymać nasze pierwsze satoshi i przetestować warunki wydatków, które zastosowaliśmy do naszego Wallet.



![Co-Sign](assets/fr/16.webp)



### 2- Testowanie predefiniowanych polityk wydatków



Dla przypomnienia, zdecydowaliśmy się na maksymalną wielkość 21212 satoshi dla naszego Wallet Multisig. Oznaczało to, że za każdym razem, gdy klucz polityki wydatków (klucz C) podpisywał transakcję, ta ostatnia byłaby ważna tylko wtedy, gdy wydana kwota była mniejsza lub równa 21212 satoshi.



Przetestujmy to.


Najpierw kliknijmy zakładkę "Receive" w Sparrow i upuśćmy kilka Satss na Wallet, którego będziemy używać w całym tym samouczku.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Następnie spróbujmy wydać więcej niż 21212 dozwolonych satoshi, symulując transakcję o wartości 50 000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Po zeskanowaniu kodu QR reprezentującego *niepodpisaną* transakcję za pomocą naszego ColdCardQ w celu zaimportowania transakcji, na ekranie pojawia się następujący komunikat. Komunikat ostrzegawczy mówi nam, że warunki wydatków nie zostały spełnione. Jeśli mimo to podpiszemy transakcję, to tylko jeden z 2 kluczy (główny seed na urządzeniu, ale nie "Klucz C") zostanie podpisany.




![Co-Sign](assets/fr/23.webp)



Tutaj, po zaimportowaniu naszej transakcji do Sparrow, widzimy, że tylko jeden z podpisów został zastosowany do transakcji.



![Co-Sign](assets/fr/24.webp)




Teraz powtórzmy eksperyment, ale dla transakcji o wartości 21 000 satoshi, tj. mniejszej niż maksymalna wielkość (21212 Sats), którą ustawiliśmy dla tego Wallet.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Spróbujmy podpisać tę transakcję za pomocą naszego ColdCardQ.



Tym razem nie ma problemu, nie pojawia się żaden komunikat ostrzegawczy, a kiedy importujemy podpisaną transakcję do Sparrow wallet, tym razem zastosowano dwa podpisy, dzięki czemu transakcja jest ważna i gotowa do dystrybucji.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Co-Sign z Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA i adresy na białej liście



W tym akapicie użyjemy naszego Wallet Multisig Co-Sign z Nunchuk i skorzystamy z okazji, aby zastosować nowe warunki wydatków, aby zobaczyć, jak to działa.



Przejdź do *Avanced Tools > ColdCard Co-Signing*.


Zostaniemy poproszeni o wprowadzenie naszego "klucza polityki wydatków", aby uzyskać dostęp do menu umożliwiającego zmianę warunków wydatków. W naszym przypadku wpisujemy 12 x "wołowina".



Zdecydowaliśmy się utrzymać wielkość 21212 Sats i maksymalną "Limit Velocity" ze względów praktycznych związanych z tym samouczkiem. Z drugiej strony użyjemy menu **"Whitelist Addresses "**, aby narzucić adresy, na które można wydać nasze fundusze.




![Co-Sign](assets/fr/31.webp)




Zeskanuj kody QR powiązane z adresami (wybierzemy 2), które chcesz dodać do białej listy, a następnie kliknij **"ENTER "**. Po sprawdzeniu poprawności adresów poprzez kolejne naciśnięcie **"ENTER "**, widzimy, że zastosowano ograniczenia dotyczące adresów Magnitude i beneficjentów.



![Co-Sign](assets/fr/32.webp)



Na koniec, aby uzyskać pełny obraz możliwości oferowanych przez "Co-Sign", aktywujmy opcję "Web 2FA".


Ta funkcja umożliwia korzystanie z aplikacji zgodnej z TOTP RFC-6238, takiej jak Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / lub Aegis Authenticator, w celu dodania dodatkowego zabezpieczenia Layer.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Mówiąc konkretnie, przed podpisaniem transakcji należy zbliżyć urządzenie z obsługą NFC i dostępem do Internetu do karty Coldcard. Spowoduje to automatyczne przejście do strony internetowej coldcard.com, na której zostaniesz poproszony o wprowadzenie 6-cyfrowego kodu aplikacji. Jeśli wprowadzisz prawidłowy kod, strona internetowa wyświetli kod QR do zeskanowania dla ColdCardQ lub 8-cyfrowy kod do wprowadzenia na Mk4, aby autoryzować urządzenie do podpisania.





![Co-Sign](assets/fr/33.webp)



Po zeskanowaniu kodu QR wyświetlanego w aplikacji do podwójnego uwierzytelniania i dodaniu konta ColdCard Co-Sign (CCC) zostaniesz poproszony o zweryfikowanie, czy wszystko jest w porządku, wprowadzając kod 2FA.



Wpisz swoją kartę ColdCard z tyłu urządzenia NFC.



![Co-Sign](assets/fr/34.webp)



Na otwartej stronie internetowej wprowadź kod 2FA swojej ulubionej aplikacji. Następnie zeskanuj kod QR wyświetlony na karcie ColdCardQ (lub wprowadź 8-cyfrowy kod wyświetlony na karcie Mk4).



![Co-Sign](assets/fr/35.webp)




Nałożyliśmy teraz limit wielkości (21212 Sats), adresów docelowych i podwójnego uwierzytelniania.



![Co-Sign](assets/fr/36.webp)



### 2- Eksport Wallet Multisig 2-on-3 do Nunchuk



Tym razem wyeksportujmy Wallet Multisig 2-na-3 do Nunchuka, tak jak zrobiliśmy to wcześniej z Sparrow.


Przejdź do *Settings > Multisig Wallets > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Tym razem wybierz opcję eksportu NFC, klikając przycisk ColdcardQ o tej samej nazwie **"NFC "**.



![Co-Sign](assets/fr/37.webp)



W Nunchuk, jeśli otwierasz aplikację po raz pierwszy, kliknij na **"Odzyskaj istniejący Wallet"**.



![Co-Sign](assets/fr/38.webp)



Jeśli masz już Wallet w aplikacji, kliknij **"+"** w prawym górnym rogu, a następnie **"Odzyskaj istniejący Wallet"**.



![Co-Sign](assets/fr/39.webp)




Następnie wybierz **"Odzyskaj Wallet z COLDCARD "**, a następnie **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Na koniec dotknij tylnej części smartfona do ekranu ColdCardQ, aby zaimportować Wallet przez NFC.



![Co-Sign](assets/fr/41.webp)



Nasze konto i satoshis zdeponowane wcześniej za pośrednictwem Sparrow wallet wróciły.



![Co-Sign](assets/fr/42.webp)



### 3- Testowanie predefiniowanych polityk wydatków



Spróbujmy teraz wykonać transakcję, która narusza 2 warunki wydatków, które ustawiliśmy. **Spróbujemy wydać więcej niż 21212 Sats na Address, który nie został zatwierdzony.** Spróbujmy wysłać 22 222 Sats na losowy Address.



![Co-Sign](assets/fr/43.webp)



Po utworzeniu transakcji kliknij 3 małe kropki w prawym górnym rogu, aby wyeksportować ją do karty ColdCard.



![Co-Sign](assets/fr/44.webp)



Następnie wybierz **"Eksportuj przez BBQR "** i zeskanuj kod QR wyświetlony za pomocą ColdCardQ.



![Co-Sign](assets/fr/45.webp)



Następnie ColdcardQ wyświetla ostrzeżenie, które po przewinięciu do dołu ekranu wyjaśnia, że transakcja narusza warunki wydatków, zgodnie z oczekiwaniami.



**Należy zauważyć, że urządzenie nie informuje nas o warunkach wydatków, aby uniemożliwić potencjalnemu atakującemu próbę obejścia ograniczeń




![Co-Sign](assets/fr/46.webp)



Jeśli nadal zatwierdzasz, naciskając **"ENTER "**, pojawi się kod QR reprezentujący podpisaną transakcję. Jeśli zaimportujesz go na Nunchuka, zobaczysz, że zastosowano tylko jeden podpis.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Wykonajmy dokładnie tę samą operację, ale tym razem z transakcją, która przestrzega limitu wielkości (21212 Sats) i wydaje satoshis na jeden z 2 adresów, które wstępnie skonfigurowaliśmy.



Wysyłamy Nunchuk 12121 Sats na jeden z naszych 2 adresów. Następnie eksportujemy transakcję do ColdCard, tak jak zrobiliśmy to wcześniej.



![Co-Sign](assets/fr/49.webp)




Po zaimportowaniu niepodpisanej transakcji do naszego ColdCardQ, zobaczmy, co tym razem zobaczymy.



Ostrzeżenie jest zawsze obecne, ale tym razem, przewijając do dołu ekranu, widzimy, że chodzi o zatwierdzenie transakcji za pomocą 2FA. Urządzenie prosi nas o zbliżenie naszej karty ColdcardQ do terminala NFC podłączonego do Internetu (smartfona lub tabletu), co czynimy.



![Co-Sign](assets/fr/50.webp)



Na naszym smartfonie otwiera się strona internetowa z prośbą o wprowadzenie kodu 2FA, co robimy dzięki Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





Następnie zeskanuj kod QR, który pojawi się na stronie internetowej, aby autoryzować kartę ColdCard do podpisania transakcji.


Transakcja jest teraz podpisana przez 2 klucze i dlatego jest ważna.



Jeśli funkcja "Push Tx" jest włączona na karcie ColdCardQ, transakcję można przesłać bezpośrednio do sieci za pomocą prostego dotknięcia tylnej części smartfona.



![Co-Sign](assets/fr/52.webp)




Jeśli nie masz włączonej funkcji "Push tx", naciśnij przycisk "QR" na ColdCardQ, aby wyświetlić podpisaną transakcję jako kod QR i zaimportować ją do Nunchuka w taki sam sposób, jak w poprzednim przykładzie.



![Co-Sign](assets/fr/53.webp)



Tym razem zauważamy, że zastosowano 2 podpisy, więc transakcja jest gotowa do transmisji w sieci Bitcoin.



![Co-Sign](assets/fr/54.webp)




Zbliżamy się do końca tego samouczka, który zawiera przegląd możliwości oferowanych przez funkcję Co-Sign zintegrowaną z urządzeniami ColdCardQ i Mk4 firmy Coinkite, a także jej wykorzystanie za pośrednictwem portfeli takich jak Sparrow i Nunchuk.