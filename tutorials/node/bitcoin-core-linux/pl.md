---
name: Bitcoin Core (Linux)
description: Uruchamianie własnego węzła z Bitcoin core w systemie Linux
---

![cover](assets/cover.webp)


## Uruchamianie własnego węzła za pomocą Bitcoin core


Wprowadzenie do Bitcoin i koncepcji węzła, uzupełnione kompleksowym przewodnikiem instalacji w systemie Linux.


Jednym z najbardziej ekscytujących aspektów Bitcoin jest możliwość samodzielnego uruchomienia programu, a tym samym uczestniczenia na poziomie granularnym w sieci i weryfikacji transakcji publicznej Ledger.


Bitcoin, jako projekt open-source, jest swobodnie dostępny i publicznie rozpowszechniany od 2009 roku. Prawie 17 lat po swoim powstaniu, Bitcoin jest obecnie solidną i niepowstrzymaną cyfrową siecią monetarną, korzystającą z potężnego organicznego efektu sieciowego. Za swoje wysiłki i wizję, Satoshi Nakamoto zasługuje na naszą wdzięczność. Nawiasem mówiąc, udostępniamy białą księgę Bitcoin tutaj na Agora 256 (uwaga: również na uniwersytecie).


### Stawanie się własnym bankiem


Uruchomienie własnego węzła stało się niezbędne dla zwolenników etosu Bitcoin. Nie pytając nikogo o zgodę, można pobrać Blockchain od początku i w ten sposób zweryfikować wszystkie transakcje od A do Z zgodnie z protokołem Bitcoin.


Program zawiera również własny Wallet. W ten sposób mamy kontrolę nad transakcjami, które wysyłamy do reszty sieci, bez żadnego pośrednika lub strony trzeciej. Jesteś swoim własnym bankiem.


Pozostała część tego artykułu jest zatem przewodnikiem po instalacji Bitcoin core - najczęściej używanej wersji oprogramowania Bitcoin - w szczególności na dystrybucjach Linuksa kompatybilnych z Debianem, takich jak Ubuntu i Pop!OS. Postępuj zgodnie z tym przewodnikiem, aby zbliżyć się o krok do swojej indywidualnej suwerenności.


## Podręcznik instalacji Bitcoin core dla Debian/Ubuntu


**Wymagania wstępne**


- Minimum 6 GB pamięci masowej na dane (węzeł pruned) - 1 TB pamięci masowej na dane (Full node)
- Spodziewaj się, że *Initial Block Download* (IBD) zajmie co najmniej 24 godziny. Ta operacja jest obowiązkowa nawet dla węzła pruned.
- Należy zapewnić ~600 GB przepustowości dla IBD, nawet dla węzła pruned.


**Uwaga: 💡** poniższe polecenia są predefiniowane dla Bitcoin core w wersji 24.1.


### Pobieranie i weryfikacja plików



- [Pobierz](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, a także pliki `SHA256SUMS` i `SHA256SUMS.asc` (oczywiście należy pobrać najnowszą wersję oprogramowania).



- Otwórz terminal w katalogu, w którym znajdują się pobrane pliki. Przykład: `cd ~/Downloads/`.



- Sprawdź, czy suma kontrolna pliku wersji jest wymieniona w pliku sumy kontrolnej za pomocą polecenia `sha256sum --ignore-missing --check SHA256SUMS`.



- Wynik tego polecenia powinien zawierać nazwę pobranego pliku wersji, po którym następuje `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Zainstaluj git za pomocą polecenia `sudo apt install git`. Następnie sklonuj repozytorium zawierające klucze PGP sygnatariuszy Bitcoin core za pomocą polecenia `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Zaimportuj klucze PGP wszystkich sygnatariuszy za pomocą polecenia `gpg --import guix.sigs/builder-keys/*`



- Sprawdź, czy plik sumy kontrolnej jest podpisany kluczami PGP sygnatariuszy za pomocą polecenia `gpg --verify SHA256SUMS.asc`.



Każdy prawidłowy podpis wyświetli linię zaczynającą się od: `gpg: Good signature` i kolejny wiersz kończący się na: `Odcisk palca klucza głównego: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (przykład odcisku klucza PGP Pietera Wuille'a).


**Uwaga💡:** nie jest konieczne, aby wszystkie klucze sygnatariuszy zwracały "OK". W rzeczywistości może być potrzebny tylko jeden. Do użytkownika należy określenie własnego progu walidacji dla weryfikacji PGP.


Możesz zignorować ostrzeżenia:



- `Ten klucz nie jest certyfikowany zaufanym podpisem!`



- "Nic nie wskazuje na to, że podpis należy do właściciela"


### Instalacja Bitcoin core graficznego Interface



- W terminalu, nadal w katalogu, w którym znajduje się plik wersji Bitcoin core, użyj polecenia `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, aby rozpakować pliki zawarte w archiwum.



- Zainstaluj wcześniej wyodrębnione pliki za pomocą polecenia `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Zainstaluj niezbędne zależności za pomocą polecenia `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Uruchom _bitcoin-qt_ (Bitcoin core graficzny Interface) używając komendy `Bitcoin-qt`.



- Aby wybrać węzeł pruned, zaznacz opcję _Limit Blockchain storage_ i skonfiguruj limit przechowywanych danych:


![welcome](assets/fr/02.webp)


### Zakończenie części 1: Przewodnik instalacji


Po zainstalowaniu Bitcoin core zaleca się, aby działał on tak często, jak to możliwe, aby przyczyniać się do rozwoju sieci Bitcoin poprzez weryfikację transakcji i przesyłanie nowych bloków do innych komputerów równorzędnych.


Dobrą praktyką pozostaje jednak okresowe uruchamianie i synchronizowanie węzła, nawet tylko w celu sprawdzenia poprawności odebranych i wysłanych transakcji.


![Creation wallet](assets/fr/03.webp)


## Konfiguracja Tora dla węzła Bitcoin core


**Uwaga💡:** ten przewodnik jest przeznaczony dla Bitcoin core 24.0.1 na dystrybucjach Linuksa kompatybilnych z Ubuntu/Debian.


### Instalowanie i konfigurowanie Tora dla Bitcoin core


Najpierw musimy zainstalować usługę Tor (The Onion Router), sieć używaną do anonimowej komunikacji, która pozwoli nam anonimizować nasze interakcje z siecią Bitcoin. Wprowadzenie do narzędzi ochrony prywatności online, w tym Tor, można znaleźć w naszym artykule na ten temat.


Aby zainstalować Tor, otwórz terminal i wpisz `sudo apt -y install tor`. Po zakończeniu instalacji usługa zostanie automatycznie uruchomiona w tle. Sprawdź, czy działa poprawnie za pomocą polecenia `sudo systemctl status tor`. Odpowiedź powinna pokazać `Active: active (exited)`. Naciśnij `Ctrl+C`, aby wyjść z tej funkcji.


**Wskazówka:** w każdym przypadku możesz użyć następujących poleceń w terminalu, aby uruchomić, zatrzymać lub ponownie uruchomić Tora:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Następnie uruchommy graficzny Bitcoin core za pomocą polecenia `Bitcoin-qt`. Następnie włącz automatyczną funkcję oprogramowania, aby kierować nasze połączenia przez proxy Tor: _Ustawienia > Sieć_, a następnie zaznaczamy opcję _Połącz przez proxy SOCKS5 (domyślne proxy)_ oraz _Użyj oddzielnego proxy SOCKS5, aby dotrzeć do peerów za pośrednictwem usług cebulowych Tor_.


![option](assets/fr/04.webp)


Bitcoin core automatycznie wykrywa, czy Tor jest zainstalowany, a jeśli tak, domyślnie tworzy połączenia wychodzące do innych węzłów również korzystających z Tora, oprócz połączeń z węzłami korzystającymi z sieci IPv4/IPv6 (clearnet).


**Uwaga💡:** aby zmienić język wyświetlacza na francuski, przejdź do zakładki Wyświetlacz w Ustawieniach.


### Zaawansowana konfiguracja Tora (opcjonalnie)


Możliwe jest skonfigurowanie Bitcoin core tak, aby używał tylko sieci Tor do łączenia się z rówieśnikami, optymalizując w ten sposób naszą anonimowość za pośrednictwem naszego węzła. Ponieważ nie ma wbudowanej funkcji do tego w graficznym Interface, będziemy musieli ręcznie utworzyć plik konfiguracyjny. Przejdź do Ustawienia, a następnie Opcje.


![option 2](assets/fr/05.webp)


Tutaj należy kliknąć na _Open configuration file_. W pliku tekstowym `Bitcoin.conf` wystarczy dodać linię `onlynet=onion` i zapisać plik. Aby to polecenie odniosło skutek, należy ponownie uruchomić Bitcoin core.


Następnie skonfigurujemy usługę Tor tak, aby Bitcoin core mógł odbierać połączenia przychodzące za pośrednictwem proxy, umożliwiając innym węzłom w sieci korzystanie z naszego węzła do pobierania danych Blockchain bez narażania bezpieczeństwa naszej maszyny.


W terminalu wpisz `sudo nano /etc/tor/torrc`, aby uzyskać dostęp do pliku konfiguracyjnego usługi Tor. W tym pliku poszukaj linii `#ControlPort 9051` i usuń `#`, aby ją włączyć. Teraz dodaj dwie nowe linie do pliku:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Aby wyjść z pliku podczas jego zapisywania, naciśnij `Ctrl+X > Y > Enter`. Wróć do terminala, zrestartuj Tora wpisując komendę `sudo systemctl restart tor`.


Dzięki tej konfiguracji Bitcoin core będzie mógł nawiązywać połączenia przychodzące i wychodzące z innymi węzłami w sieci tylko za pośrednictwem sieci Tor (Onion). Aby to potwierdzić, kliknij zakładkę _Window_, a następnie _Peers_.


![Nodes Window](assets/fr/06.webp)


### Dodatkowe zasoby


Ostatecznie korzystanie tylko z sieci Tor (`onlynet=onion`) może sprawić, że będziesz podatny na Sybil Attack. Dlatego niektórzy zalecają utrzymywanie konfiguracji z wieloma sieciami, aby złagodzić tego typu ryzyko. Ponadto wszystkie połączenia IPv4/IPv6 będą kierowane przez serwer proxy Tor po jego skonfigurowaniu, jak wskazano wcześniej.


Alternatywnie, aby pozostać wyłącznie w sieci Tor i zmniejszyć ryzyko Sybil Attack, możesz dodać Address innego zaufanego węzła do pliku `Bitcoin.conf`, dodając linię `addnode=trusted_address.onion`. Możesz dodać tę linię wiele razy, jeśli chcesz połączyć się z wieloma zaufanymi węzłami.


Aby wyświetlić logi węzła Bitcoin związane konkretnie z jego interakcją z Torem, dodaj `debug=tor` do pliku `Bitcoin.conf`. Będziesz miał teraz odpowiednie informacje o Torze w dzienniku debugowania, który możesz wyświetlić w oknie _Information_ za pomocą przycisku _Debug File_. Możliwe jest również przeglądanie tych dzienników bezpośrednio w terminalu za pomocą polecenia `bitcoind -debug=tor`.


**Tip💡:** oto kilka interesujących linków:


- [Strona Wiki wyjaśniająca Tor i jego związek z Bitcoin](https://en.Bitcoin.it/wiki/Tor)
- [Generator plików konfiguracyjnych Bitcoin core autorstwa Jamesona Loppa](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Przewodnik konfiguracji Tora autorstwa Jona Atacka](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Jak zawsze, jeśli masz jakieś pytania, podziel się nimi ze społecznością Agora256. Uczymy się razem, aby jutro być lepszymi niż dziś!