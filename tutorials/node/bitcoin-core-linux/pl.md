---
name: Bitcoin Core (Linux)
description: Uruchamianie własnego węzła z Bitcoin Core
---

![cover](assets/cover.webp)


# Uruchamianie własnego węzła z Bitcoin Core


Wprowadzenie do Bitcoin i koncepcji węzła, uzupełnione kompleksowym przewodnikiem instalacji w systemie Linux.


Jedną z najbardziej ekscytujących propozycji Bitcoin jest możliwość samodzielnego uruchomienia programu, a tym samym uczestniczenia na poziomie granularnym w sieci i weryfikacji transakcji publicznej Ledger.


Bitcoin, projekt typu open-source, jest publicznie rozpowszechniany i dostępny za darmo od 2009 roku. Prawie 15 lat po swoim powstaniu, Bitcoin jest obecnie solidną i niepowstrzymaną cyfrową siecią monetarną, korzystającą z potężnego organicznego efektu sieciowego. Za ich wysiłki i wizję, Satoshi Nakamoto zasługuje na naszą wdzięczność. Nawiasem mówiąc, udostępniamy białą księgę Bitcoin tutaj na Agora 256 (uwaga: również na uniwersytecie).


## Stawanie się własnym bankiem


Uruchomienie własnego węzła stało się niezbędne dla zwolenników aksjomatu Bitcoin. Nie pytając nikogo o zgodę, można pobrać Blockchain od początku i w ten sposób zweryfikować wszystkie transakcje od A do Z zgodnie z protokołem Bitcoin.


Program zawiera również własny Wallet. W ten sposób mamy kontrolę nad transakcjami, które wysyłamy do reszty sieci, bez żadnego pośrednika lub strony trzeciej. Jesteś swoim własnym bankiem.


Pozostała część tego artykułu jest zatem przewodnikiem po instalacji Bitcoin Core - najczęściej używanej wersji oprogramowania Bitcoin - w szczególności na dystrybucjach Linuksa kompatybilnych z Debianem, takich jak Ubuntu i Pop!/\_OS. Postępuj zgodnie z tym przewodnikiem, aby zbliżyć się o krok do swojej indywidualnej suwerenności.


## Podręcznik instalacji Bitcoin Core dla Debian/Ubuntu


**Wymagania wstępne**


- Co najmniej 6 GB pamięci masowej na dane (przycięty węzeł) - 1 TB pamięci masowej na dane (Full node)
- Odczekaj co najmniej 24 godziny na zakończenie pobierania początkowego bloku (IBD). Operacja ta jest obowiązkowa nawet w przypadku przyciętego węzła.
- Należy zapewnić ~600 GB przepustowości dla IBD, nawet w przypadku przyciętego węzła.


**Uwaga: 💡** poniższe polecenia są predefiniowane dla Bitcoin Core w wersji 24.1.


## Pobieranie i weryfikacja plików


1. Pobierz Bitcoin-24.1-x86_64-linux-gnu.tar.gz, a także pliki SHA256SUMS i SHA256SUMS.asc. (https://bitcoincore.org/bin/Bitcoin-core-24.1/Bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Otwórz terminal w katalogu, w którym znajdują się pobrane pliki. Np. cd ~/Downloads/.

3. Sprawdź, czy suma kontrolna pliku wersji jest wymieniona w pliku sumy kontrolnej za pomocą polecenia sha256sum --ignore-missing --check SHA256SUMS.

4. Wyjście tego polecenia powinno zawierać nazwę pobranego pliku wersji, po którym następuje "OK". Przykład: Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Zainstaluj git za pomocą polecenia sudo install git. Następnie sklonuj repozytorium zawierające klucze PGP sygnatariuszy Bitcoin Core za pomocą polecenia git clone https://github.com/Bitcoin-core/guix.sigs.

6. Zaimportuj klucze PGP wszystkich sygnatariuszy za pomocą polecenia gpg --import guix.sigs/builder-keys//\*

7. Sprawdź, czy plik sumy kontrolnej jest podpisany kluczami PGP sygnatariuszy, używając polecenia gpg --verify SHA256SUMS.asc.


Każdy podpis zwróci wiersz zaczynający się od: gpg: Good signature i inny wiersz kończący się odciskiem palca klucza głównego: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (przykład odcisku klucza PGP Pietera Wuille'a).


**Uwaga💡:** nie jest konieczne, aby wszystkie klucze sygnatariuszy zwracały "OK". W rzeczywistości może być potrzebny tylko jeden. Do użytkownika należy określenie własnego progu walidacji dla weryfikacji PGP.


Komunikaty OSTRZEŻENIE można ignorować:


- `Ten klucz nie jest certyfikowany zaufanym podpisem!`
- "Nic nie wskazuje na to, że podpis należy do właściciela"


## Instalacja Bitcoin Core graficznego Interface


1. W terminalu, nadal w katalogu, w którym znajduje się plik wersji Bitcoin Core, użyj polecenia tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz, aby rozpakować pliki zawarte w archiwum.


2. Zainstaluj wcześniej wyodrębnione pliki za pomocą polecenia sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/\*


3. Zainstaluj niezbędne zależności za pomocą polecenia sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev


4. Uruchom Bitcoin-qt (Bitcoin Core graficzny Interface) za pomocą polecenia Bitcoin-qt.


5. Aby wybrać przycięty węzeł, zaznacz opcję Limit Blockchain storage i skonfiguruj limit przechowywanych danych:


![welcome](assets/1.webp)


## Zakończenie części 1: Przewodnik instalacji


Po zainstalowaniu Bitcoin Core zaleca się, aby działał on tak często, jak to możliwe, aby przyczyniać się do rozwoju sieci Bitcoin poprzez weryfikację transakcji i przesyłanie nowych bloków do innych komputerów równorzędnych.


Dobrą praktyką pozostaje jednak okresowe uruchamianie i synchronizowanie węzła, nawet tylko w celu sprawdzenia poprawności odebranych i wysłanych transakcji.


![Creation wallet](assets/2.webp)


# Konfiguracja Tora dla głównego węzła Bitcoin


**Uwaga💡:** ten przewodnik jest przeznaczony dla Bitcoin Core 24.0.1 na dystrybucjach Linuksa kompatybilnych z Ubuntu/Debian.


## Instalowanie i konfigurowanie Tora dla Bitcoin Core


Po pierwsze, musimy zainstalować usługę Tor (The Onion Router), sieć używaną do anonimowej komunikacji, która pozwoli nam anonimizować nasze interakcje z siecią Bitcoin. Wprowadzenie do narzędzi ochrony prywatności online, w tym Tor, można znaleźć w naszym artykule na ten temat.


Aby zainstalować Tor, otwórz terminal i wpisz sudo apt -y install tor. Po zakończeniu instalacji usługa zostanie automatycznie uruchomiona w tle. Sprawdź, czy działa poprawnie za pomocą polecenia sudo systemctl status tor. W odpowiedzi powinien pojawić się komunikat Active: active (exited). Naciśnij Ctrl+C, aby wyjść z tej funkcji.


**Wskazówka:** w każdym przypadku możesz użyć następujących poleceń w terminalu, aby uruchomić, zatrzymać lub ponownie uruchomić Tora:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Następnie uruchommy graficzny Bitcoin Core Interface za pomocą polecenia Bitcoin-qt. Następnie włączmy automatyczną funkcję oprogramowania, aby kierować nasze połączenia przez proxy Tor: Ustawienia > Sieć, a stamtąd możemy zaznaczyć Połącz przez proxy SOCKS5 (domyślne proxy), a także Użyj oddzielnego proxy SOCKS5, aby dotrzeć do peerów za pośrednictwem usług cebulowych Tor.


![option](assets/3.webp)


Bitcoin Core automatycznie wykrywa, czy Tor jest zainstalowany, a jeśli tak, domyślnie tworzy połączenia wychodzące do innych węzłów również korzystających z Tora, oprócz połączeń z węzłami korzystającymi z sieci IPv4/IPv6 (clearnet).


**Uwaga💡:** aby zmienić język wyświetlacza na francuski, przejdź do zakładki Wyświetlacz w Ustawieniach.


## Zaawansowana konfiguracja Tora (opcjonalnie)


Możliwe jest skonfigurowanie Bitcoin Core tak, aby używał tylko sieci Tor do łączenia się z peerami, optymalizując w ten sposób naszą anonimowość za pośrednictwem naszego węzła. Ponieważ nie ma wbudowanej funkcji do tego celu w graficznym Interface, będziemy musieli ręcznie utworzyć plik konfiguracyjny. Przejdź do Ustawienia, a następnie Opcje.


![option 2](assets/4.webp)


Tutaj kliknij na Otwórz plik konfiguracyjny. W pliku tekstowym Bitcoin.conf wystarczy dodać linię onlynet=onion i zapisać plik. Aby to polecenie odniosło skutek, należy ponownie uruchomić Bitcoin Core.

Następnie skonfigurujemy usługę Tor tak, aby Bitcoin Core mógł odbierać połączenia przychodzące za pośrednictwem proxy, umożliwiając innym węzłom w sieci korzystanie z naszego węzła do pobierania danych Blockchain bez narażania bezpieczeństwa naszej maszyny.


W terminalu wpisz sudo nano /etc/tor/torrc, aby uzyskać dostęp do pliku konfiguracyjnego usługi Tor. W tym pliku poszukaj linii #ControlPort 9051 i usuń #, aby ją włączyć. Teraz dodaj dwie nowe linie do pliku: HiddenServiceDir /var/lib/tor/Bitcoin-service/ i HiddenServicePort 8333 127.0.0.1:8334. Aby wyjść z pliku podczas jego zapisywania, naciśnij Ctrl+X > Y > Enter. Wróć do terminala, uruchom ponownie Tor, wpisując polecenie sudo systemctl restart tor.


Dzięki tej konfiguracji Bitcoin Core będzie mógł nawiązywać połączenia przychodzące i wychodzące z innymi węzłami w sieci tylko za pośrednictwem sieci Tor (Onion). Aby to potwierdzić, kliknij zakładkę Window, a następnie Peers.


![Nodes Window](assets/5.webp)


## Dodatkowe zasoby


Ostatecznie korzystanie tylko z sieci Tor (onlynet=onion) może narazić cię na atak Sybil. Dlatego też niektórzy zalecają utrzymywanie konfiguracji wielosieciowej w celu ograniczenia tego rodzaju ryzyka. Ponadto wszystkie połączenia IPv4/IPv6 będą kierowane przez serwer proxy Tor po jego skonfigurowaniu, jak wskazano wcześniej.


Alternatywnie, aby pozostać wyłącznie w sieci Tor i zmniejszyć ryzyko ataku Sybil, możesz dodać Address innego zaufanego węzła do pliku Bitcoin.conf, dodając linię addnode=trusted_address.onion. Możesz dodać tę linię wiele razy, jeśli chcesz połączyć się z wieloma zaufanymi węzłami.


Aby wyświetlić dzienniki węzła Bitcoin związane konkretnie z jego interakcją z Torem, dodaj debug=tor do pliku Bitcoin.conf. Będziesz miał teraz odpowiednie informacje o Torze w dzienniku debugowania, który możesz wyświetlić w oknie Informacje za pomocą przycisku Plik debugowania. Możliwe jest również przeglądanie tych dzienników bezpośrednio w terminalu za pomocą polecenia bitcoind -debug=tor.


**Tip💡:** oto kilka interesujących linków:


- Strona Wiki wyjaśniająca Tor i jego związek z Bitcoin
- Generator plików konfiguracyjnych Bitcoin Core autorstwa Jamesona Loppa
- Przewodnik konfiguracji Tora autorstwa Jona Atacka


Jak zawsze, jeśli masz jakieś pytania, podziel się nimi ze społecznością Agora256. Uczymy się razem, aby jutro być lepszymi niż dziś!