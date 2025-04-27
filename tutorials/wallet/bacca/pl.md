---
name: Bacca
description: Konfigurowanie Ledger bez oprogramowania Ledger Live
---
![cover](assets/cover.webp)


Jeśli korzystasz z Ledger, prawdopodobnie zauważyłeś, że musisz przejść przez oprogramowanie Ledger Live, przynajmniej do początkowej konfiguracji urządzenia, aby sprawdzić jego autentyczność i zainstalować na nim aplikację Bitcoin. Jednak po tej konfiguracji wielu bitcoinerów woli używać specjalistycznego oprogramowania do zarządzania Bitcoin Wallet, takiego jak Sparrow lub Liana, zamiast Ledger Live. Chociaż Ledger produkuje doskonałe portfele sprzętowe, które szybko zawierają najnowsze funkcje Bitcoin, ich oprogramowanie niekoniecznie jest dostosowane do konkretnych potrzeb bitcoinerów. Rzeczywiście, Ledger Live zawiera wiele funkcji zaprojektowanych dla altcoinów, podczas gdy opcje dedykowane zarządzaniu Bitcoin Wallet są ograniczone. Problem ze Sparrow i Liana (na chwilę obecną) polega jednak na tym, że nie pozwalają one na zainstalowanie aplikacji Bitcoin na Ledger.


Aby ominąć konieczność korzystania z Ledger Live podczas początkowej konfiguracji Ledger, można użyć narzędzia Bacca (lub "Ledger Installer"). Oprogramowanie to umożliwia instalację i aktualizację aplikacji Bitcoin, weryfikację autentyczności Ledger, a nawet późniejszą aktualizację oprogramowania sprzętowego urządzenia. Bacca została stworzona przez Antoine Poinsot (Darosior), programistę Bitcoin Core w Chaincode Labs, współzałożyciela [Revault i Liana](https://wizardsardine.com/) oraz Pythcoinera.


W tym samouczku pokażę ci, jak korzystać z tego narzędzia, abyś mógł na dobre obejść się bez oprogramowania Ledger Live i nadal cieszyć się urządzeniami Ledger. Działa na wszystkich urządzeniach: Nano S Classic, Nano S Plus, Nano X, Flex i Stax.


---
*Należy pamiętać, że to narzędzie jest dość nowe, a jego twórcy zaznaczają, że wciąż jest **w fazie testów**. Zalecają używanie go wyłącznie do celów testowych, a nie do urządzenia przeznaczonego do hostowania prawdziwego Bitcoin Wallet, chociaż jest to możliwe. W związku z tym zalecam przestrzeganie zaleceń twórców tego narzędzia, które są określone [w README ich repozytorium GitHub](https://github.com/darosior/ledger_installer).*


---
## Wymagania wstępne


Do korzystania z aplikacji Bacca na komputerze potrzebne są dwa narzędzia:




- Git ;
- Rust.


Jeśli już je zainstalowałeś, możesz pominąć ten krok.


**Linux:**


W dystrybucji Linuksa, Git jest zazwyczaj preinstalowany. Aby sprawdzić, czy Git jest zainstalowany w systemie, można wpisać następujące polecenie w terminalu :


```bash
git --version
```


Jeśli nie masz zainstalowanego Gita w swoim systemie, oto polecenie, aby zainstalować go na Debianie:


```bash
sudo apt install git
```


Wreszcie, aby zainstalować środowisko programistyczne Rust, użyj polecenia :


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Windows:**


Aby zainstalować Git, przejdź do [oficjalnej strony projektu](https://git-scm.com/). Pobierz oprogramowanie i postępuj zgodnie z instrukcjami instalacji.


![BACCA](assets/fr/01.webp)


Postępuj w ten sam sposób, aby zainstalować Rust z [oficjalnej strony internetowej] (https://www.Rust-lang.org/tools/install).


![BACCA](assets/fr/02.webp)


**MacOS:**


Jeśli Git nie jest jeszcze zainstalowany w systemie, otwórz terminal i uruchom następujące polecenie, aby go zainstalować:


```bash
git --version
```


Jeśli Git nie jest zainstalowany w systemie, otworzy się okno z propozycją zainstalowania Xcode, który zawiera Git. Wystarczy postępować zgodnie z instrukcjami wyświetlanymi na ekranie, aby kontynuować instalację.


Aby zainstalować Rust, uruchom następujące polecenie:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## Instalacja Bacca


Otwórz terminal i przejdź do folderu, w którym chcesz zapisać oprogramowanie, a następnie uruchom następujące polecenie:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


Przejdź do katalogu oprogramowania:


```bash
cd ledger_installer
```


Następnie użyj Cargo, aby skompilować projekt i uruchomić GUI Bacca:


```bash
cargo run -p ledger_manager_gui
```


Masz teraz dostęp do oprogramowania Interface.


![BACCA](assets/fr/03.webp)


## Konfiguracja Ledger


Przed rozpoczęciem, jeśli Ledger jest nowy, upewnij się, że skonfigurowałeś kod PIN i zapisałeś frazę odzyskiwania. Nie potrzebujesz Ledger Live do wykonania tych początkowych kroków. Wystarczy podłączyć Ledger za pomocą kabla USB, aby go zasilić. Jeśli nie masz pewności, jak wykonać te dwa kroki, możesz zapoznać się z początkiem samouczka dotyczącego Twojego modelu:


https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Korzystanie z Bacca


Podłącz Ledger do komputera i odblokuj go za pomocą ustawionego kodu PIN. Aplikacja Bacca powinna automatycznie wykryć urządzenie Ledger.


![BACCA](assets/fr/04.webp)


Aby potwierdzić autentyczność urządzenia Ledger, kliknij przycisk "*Check*". Aby kontynuować, należy autoryzować połączenie na urządzeniu Ledger.


![BACCA](assets/fr/05.webp)


Następnie Bacca poinformuje Cię, czy Twój Ledger jest oryginalny. Jeśli tak nie jest, oznacza to, że urządzenie zostało naruszone lub jest podrobione. W takim przypadku należy natychmiast przestać go używać.


![BACCA](assets/fr/06.webp)


W menu "*Apps*" można sprawdzić listę aplikacji już zainstalowanych na urządzeniu Ledger.


![BACCA](assets/fr/07.webp)


Aby zainstalować aplikację Bitcoin, kliknij "*Install*", a następnie autoryzuj instalację na Ledger.


![BACCA](assets/fr/08.webp)


Aplikacja jest dobrze zainstalowana.


![BACCA](assets/fr/09.webp)


Jeśli nie masz zainstalowanej najnowszej wersji aplikacji Bitcoin, Bacca wyświetli przycisk "*Update*" zamiast wskazania "*Latest*". Wystarczy kliknąć ten przycisk, aby zaktualizować aplikację.


![BACCA](assets/fr/10.webp)


Teraz, gdy twój Ledger jest poprawnie skonfigurowany z najnowszą wersją aplikacji Bitcoin, jesteś gotowy do importowania i używania Wallet w oprogramowaniu zarządzającym, takim jak Sparrow lub Liana, bez konieczności przechodzenia przez Ledger Live!


Jeśli uznałeś ten poradnik za przydatny, będę wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również zapoznanie się z tym samouczkiem na temat GnuPG, który wyjaśnia, jak sprawdzić integralność i autentyczność oprogramowania przed jego zainstalowaniem. Jest to ważna praktyka, szczególnie podczas instalowania oprogramowania do zarządzania Wallet, takiego jak Liana lub Sparrow:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc