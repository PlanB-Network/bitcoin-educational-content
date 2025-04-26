---
name: Oznaczanie czasem certyfikatów i dyplomów Plan ₿ Network
description: Dowiedz się, w jaki sposób Plan ₿ Network wydaje weryfikowalne dowody dla Twoich certyfikatów i dyplomów
---

![cover](assets/cover.webp)


Jeśli to czytasz, istnieje duże prawdopodobieństwo, że otrzymałeś certyfikat testu ₿-CERT lub dyplom ukończenia jednego z kursów, w których uczestniczyłeś na planb.network, więc gratulujemy tego osiągnięcia!


W tym samouczku dowiemy się, w jaki sposób Plan ₿ Network wydaje weryfikowalne dowody dla certyfikatu testu ₿-CERT lub dowolnego dyplomu ukończenia kursu. Następnie w drugiej części opiszemy, jak zweryfikować autentyczność tych dowodów.


# Mechanizm zabezpieczający Plan ₿ Network


W Plan ₿ Network podpisujemy kryptograficznie certyfikaty i dyplomy oraz oznaczamy je czasem za pomocą łańcucha czasu (tj. Bitcoin Blockchain), poprzez mechanizm dowodowy, który opiera się na dwóch operacjach kryptograficznych:


1. Podpis GPG na pliku tekstowym, który syntetyzuje twoje osiągnięcia

2. Znacznik czasu tego samego podpisanego pliku za pośrednictwem [opentimestamps](https://opentimestamps.org/).


Pierwsza operacja umożliwia potwierdzenie wystawcy certyfikatu (lub dyplomu), a druga pozwala zweryfikować datę jego wydania.

Wierzymy, że ten prosty mechanizm dowodowy umożliwia nam wydawanie certyfikatów i dyplomów z niezaprzeczalnymi dowodami, które każdy może niezależnie zweryfikować.


![image](./assets/proof-mechanism.webp)


Dzięki temu mechanizmowi dowodowemu każda próba zmiany nawet najmniejszego szczegółu certyfikatu lub dyplomu spowoduje uzyskanie zupełnie innego SHA-256 Hash podpisanego pliku, natychmiast ujawniając wszelkie manipulacje, ponieważ zarówno podpis, jak i Timestamp nie będą już ważne. Co więcej, jeśli ktokolwiek spróbuje złośliwie podrobić certyfikaty lub dyplomy w imieniu Plan ₿ Network, prosta weryfikacja podpisu ujawni oszustwo.


## Jak działa podpis GPG?


Podpis GPG jest generowany przy użyciu oprogramowania open-source o nazwie GNU Privacy Guard. Oprogramowanie to pozwala użytkownikom łatwo tworzyć klucze prywatne, podpisywać i weryfikować podpisy oraz szyfrować i odszyfrowywać pliki. Dla celów tego samouczka ważne jest, aby pamiętać, że Plan ₿ Network używa GPG do tworzenia kluczy prywatnych / publicznych i podpisywania wszystkich certyfikatów ₿-CERT i dyplomów ukończenia kursu.


Z drugiej strony, jeśli ktoś chce zweryfikować autentyczność podpisanego pliku, może użyć GPG do zaimportowania klucza publicznego wystawcy i zweryfikowania go.


Ci, którzy są ciekawi i chcą dowiedzieć się więcej o tym fantastycznym oprogramowaniu, mogą zapoznać się z ["The GNU Privacy Handbook"] (https://www.gnupg.org/gph/en/manual/x135.html)


## Jak działa znacznik czasu?


Każdy może użyć OpenTimestamps do Timestamp pliku i uzyskać weryfikowalny dowód jego istnienia. Innymi słowy, nie zapewnia on dowodu na to, kiedy plik został utworzony, ale raczej dowód na to, że plik istniał nie później niż w określonym momencie.

OpenTimestamps zapewnia tę usługę za darmo, wykorzystując wysoce wydajną metodę przechowywania dowodu w Bitcoin Blockchain. Wykorzystuje algorytm SHA-256 Hash do utworzenia unikalnego identyfikatora pliku i konstruuje Merkle Tree przy użyciu hashy plików przesłanych przez innych użytkowników. Tylko Hash struktury Merkle Tree jest zakotwiczony w transakcji OP_RETURN, zapewniając bezpieczny i kompaktowy sposób weryfikacji istnienia pliku.

Gdy ta transakcja znajdzie się w bloku, każdy, kto posiada plik początkowy i powiązany z nim plik `.ots`, może zweryfikować autentyczność znacznika czasu. W drugiej części samouczka zobaczymy, jak zweryfikować certyfikat Bitcoin lub dowolny dyplom ukończenia kursu za pomocą szablonu i graficznego Interface na stronie OpenTimestamps.


# Jak zweryfikować certyfikat lub dyplom Plan ₿ Network ₿-CERT?


## Krok 1. Pobierz swój certyfikat lub dyplom


Zaloguj się do panelu osobistego/studenckiego na stronie planb.network.


![image](./assets/login.webp)


Przejdź do "Poświadczeń", klikając menu po lewej stronie i wybierz sesję egzaminacyjną lub dyplom.


![image](./assets/credential.webp)


Pobierz plik zip.


![image](./assets/download.webp)


Wyodrębnij zawartość, klikając prawym przyciskiem myszy plik `.zip` i wybierając opcję "Wyodrębnij". Znajdziesz trzy różne pliki:



- Podpisany plik tekstowy (np. certyfikat.txt)
- Plik Open Timestamp (OTS) (np. certificate.txt.ots)
- Certyfikat w formacie PDF (np. certyfikat.pdf)


## Krok 2: Jak zweryfikować podpis pliku tekstowego?


Najpierw przejdź do folderu, w którym wyodrębniłeś pliki i otwórz terminal (kliknij prawym przyciskiem myszy okno folderu i kliknij "Otwórz w terminalu"). Następnie postępuj zgodnie z poniższymi instrukcjami.


1. Zaimportuj klucz publiczny PGP Plan ₿ Network za pomocą następującego polecenia:


```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```


Po pomyślnym zaimportowaniu klucza PGP powinien zostać wyświetlony następujący komunikat


```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


UWAGA: jeśli widzisz, że 1 klucz został przetworzony, a 0 kluczy zostało zaimportowanych, prawdopodobnie oznacza to, że już wcześniej zaimportowałeś ten sam klucz, co jest całkowicie w porządku.


2. Zweryfikuj podpis certyfikatu lub dyplomu za pomocą następującego polecenia:


```bash
gpg --verify certificate.txt
```


To polecenie powinno wyświetlić szczegółowe informacje o podpisie, w tym:



- Kto podpisał (Plan ₿ Network)
- Kiedy został podpisany
- Czy podpis jest ważny, czy nie


To jest przykład wyniku:


```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```


Jeśli zobaczysz komunikat "BAD signature", oznacza to, że plik został zmodyfikowany.


## Krok 3: Weryfikacja otwartego Timestamp


### Weryfikacja za pomocą graficznego Interface


1. Odwiedź stronę OpenTimestamps: https://opentimestamps.org/

2. Kliknij zakładkę "Stempel i weryfikacja".

3. Przeciągnij i upuść plik OTS (np. `certificate.txt.ots`) do wyznaczonego obszaru.

4. Przeciągnij i upuść plik ze znacznikiem czasu (np. `certificate.txt`) do wyznaczonego obszaru.

5. Witryna automatycznie zweryfikuje otwarty Timestamp i wyświetli wynik.


Jeśli wyświetlony zostanie następujący komunikat, oznacza to, że Timestamp jest ważny:


![cover](assets/opentimestamp_wegui_verified.webp)


### Metoda CLI


UWAGA: ta procedura **będzie wymagać uruchomionego lokalnego węzła Bitcoin**


1. Zainstaluj klienta OpenTimestamps z oficjalnego [repozytorium] (https://github.com/opentimestamps/opentimestamps-client), uruchamiając następujące polecenie:


```
pip install opentimestamps-client
```


2. Przejdź do katalogu zawierającego wyodrębnione pliki certyfikatów.


3. Uruchom następujące polecenie, aby zweryfikować otwarty Timestamp:


```
ots verify certificate.txt.ots
```


To polecenie spowoduje:



- Sprawdź Timestamp w stosunku do Bitcoin Blockchain
- Pokazuje, kiedy dokładnie plik został oznaczony znacznikiem czasu
- Potwierdzenie autentyczności Timestamp


### Wyniki końcowe


Weryfikacja zakończy się pomyślnie, jeśli wyświetlone zostaną **obydwa** poniższe komunikaty:


1. Sygnatura GPG jest zgłaszana jako **"Dobra sygnatura z Plan ₿ Network"**

2. Weryfikacja OpenTimestamps pokazuje określony blok Bitcoin Timestamp i zgłasza **"Sukces! Blok Bitcoin [blockheight] poświadcza, że dane istniały od [Timestamp]"**


Teraz, gdy już wiesz, w jaki sposób Plan ₿ Network wystawia weryfikowalne dowody dla dowolnego certyfikatu i dyplomu ₿-CERT, możesz łatwo zweryfikować ich integralność.