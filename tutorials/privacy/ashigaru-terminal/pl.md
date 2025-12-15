---
name: Ashigaru Terminal
description: Użyj Ashigaru na pulpicie do tworzenia coinjoinów
---

![cover](assets/cover.webp)



Ashigaru Terminal to opracowana przez zespół Ashigaru adaptacja Sparrow Server, która implementuje protokół Whirlpool coinjoin. Oprogramowanie to jest kontynuacją prac rozpoczętych przez Samourai Wallet, w szczególności nad Whirlpool GUI, którego podstawowe zasady przyjmuje: samokontrola i zachowanie poufności.



Oprogramowanie to jest fork serwera Sparrow, zmodyfikowanym i zoptymalizowanym pod kątem pełnej integracji z ekosystemem Whirlpool, protokołem ZeroLink coinjoin pierwotnie opracowanym przez zespoły Samourai.



Ashigaru Terminal działa w oparciu o minimalistyczny interfejs TUI i może być wdrożony na komputerze osobistym lub na dedykowanym serwerze. Umożliwia bezpośrednią interakcję z Whirlpool w celu inicjowania "*Tx0*", zarządzania kontami "*Deposit*", "*Premix*", "*Postmix*" i "*Badbank*" oraz wykonywania automatycznych remiksów w celu wzmocnienia poufności części.



Krótko mówiąc, Ashigaru Terminal będzie szczególnie przydatny, jeśli chcesz tworzyć coinjoiny za pomocą Whirlpool.



W tym pierwszym poradniku przeprowadzę cię przez instalację i obsługę Ashigaru Terminal. Drugi, bardziej zaawansowany poradnik poświęcony będzie faktycznemu tworzeniu coinjoinów.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Zainstaluj terminal Ashigaru



Aby zainstalować Ashigaru Terminal, będziesz potrzebował przeglądarki Tor Browser, ponieważ pliki binarne są dystrybuowane tylko przez sieć Tor. Jeśli jeszcze tego nie zrobiłeś, [zainstaluj ją na swoim komputerze](https://www.torproject.org/download/).



### 1.1. pobierz Ashigaru Terminal



Z przeglądarki Tor Browser przejdź do [strony wydań ich repozytorium Git] (http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/), aby pobrać najnowszą wersję Ashigaru Terminal dla swojego systemu operacyjnego.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Pobierz następujące 2 pliki dla swojego systemu operacyjnego:




- Plik binarny (`ashigaru_terminal_v1.0.0_amd64.deb` dla Debiana/Ubuntu, `.dmg` dla macOS lub `.zip` dla Windows) ;
- Podpisany plik haseł: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Sprawdź terminal Ashigaru



Przed uruchomieniem oprogramowania na urządzeniu należy sprawdzić jego autentyczność i integralność. Jest to ważny krok, ponieważ zapobiega zainstalowaniu fałszywej wersji, która może zagrozić bitcoinom lub zainfekować komputer.



Otwórz nową kartę przeglądarki i przejdź do [Keybase verification tool](https://keybase.io/verify). Wklej zawartość właśnie pobranego pliku `.txt` w odpowiednie pole, a następnie kliknij przycisk `Verify`.



![Image](assets/fr/02.webp)



Aby urozmaicić źródła weryfikacji, możesz również porównać wiadomość z tą dostępną na stronie clearnet [ashigaru.rs](https://ashigaru.rs/download/), w sekcji `/download`.



![Image](assets/fr/03.webp)



Jeśli podpis jest prawidłowy, Keybase wyświetli komunikat potwierdzający, że plik został podpisany przez programistów Ashigaru.



![Image](assets/fr/04.webp)



Możesz również kliknąć profil `ashigarudev` wyświetlany przez Keybase i sprawdzić, czy jego kluczowy odcisk palca pasuje dokładnie do: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Jeśli na tym etapie pojawi się błąd, podpis jest nieprawidłowy. W takim przypadku **nie instaluj pobranego oprogramowania**. Rozpocznij ponownie od początku lub poproś społeczność o pomoc przed kontynuowaniem.



Keybase dostarczyła uwierzytelniony hash aplikacji. Teraz sprawdzimy, czy hash pobranego pliku `.deb`, `.zip` lub `.dmg` jest zgodny z tym zweryfikowanym w Keybase. Aby to zrobić, przejdź do [HASH FILE ONLINE](https://hash-file.online/).



Kliknij przycisk `BROWSE...` i wybierz plik `.deb`, `.zip` lub `.dmg` pobrany w kroku 1.1. Następnie wybierz funkcję skrótu `SHA-256` i kliknij `CALCULATE HASH`, aby generate hash dla twojego pliku.



![Image](assets/fr/06.webp)



Witryna wyświetli następnie skrót oprogramowania. Porównaj go z hashem zweryfikowanym na Keybase.io. Jeśli oba są idealnie zgodne, weryfikacja autentyczności i integralności przebiegła pomyślnie. Można wtedy korzystać z oprogramowania.



![Image](assets/fr/07.webp)



### 1.3 Uruchomienie terminalu Ashigaru





- Debian / Ubuntu



Aby zainstalować oprogramowanie, uruchom polecenie :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Zmodyfikuj kolejność zgodnie z pobraną wersją.



Następnie sprawdź instalację:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Następnie uruchom oprogramowanie:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Windows**



Kliknij prawym przyciskiem myszy pobrany i sprawdzony plik `.zip`, a następnie wybierz `Extract All...`, aby wyodrębnić jego zawartość.



Po zakończeniu rozpakowywania kliknij dwukrotnie plik `Ashigaru-terminal.exe`, aby uruchomić oprogramowanie.



![Image](assets/fr/08.webp)



## 2. Rozpoczęcie pracy z terminalem Ashigaru



Ashigaru Terminal to program typu TUI (*Text-based User Interface*), czyli minimalistyczny interfejs działający bezpośrednio w terminalu. Interakcja z nim odbywa się za pomocą menu i skrótów klawiaturowych, ale bez klasycznego środowiska graficznego.



![Image](assets/fr/09.webp)



Jest łatwy w użyciu: użyj klawiszy strzałek na klawiaturze, aby poruszać się po menu i naciśnij klawisz `Enter`, aby zatwierdzić akcję lub potwierdzić wybór.



## 3. Podłączanie węzła do terminala Ashigaru



Domyślnie Ashigaru Terminal łączy się z publicznym serwerem Electrum. To oczywiście stwarza ryzyko w zakresie poufności i suwerenności. Dlatego skonfigurujemy go tak, aby łączył się bezpośrednio z własnym Electrum Server.



Aby to zrobić, otwórz menu `Preferences > Server`.



![Image](assets/fr/10.webp)



Kliknij przycisk `< Edytuj >`.



![Image](assets/fr/11.webp)



Wybierz `Private Electrum Server`, a następnie kliknij `<Kontynuuj>`.



![Image](assets/fr/12.webp)



Wprowadź adres URL i port swojego serwera. Możesz określić adres Tor w `.onion`. Następnie kliknij `< Test >`, aby zweryfikować połączenie.



![Image](assets/fr/13.webp)



Jeśli połączenie się powiedzie, pojawi się komunikat `Success` wraz ze szczegółowymi informacjami o serwerze.



![Image](assets/fr/14.webp)



Jeśli nie masz jeszcze węzła Bitcoin, polecam ci udział w tym kursie:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*W moim przypadku, na potrzeby tego samouczka, zamierzam odłączyć się od mojego serwera Electrs, ponieważ pracuję w sieci testowej. Jednak działanie pozostaje identyczne na mainnet.*



## 4. Utwórz portfolio na Ashigaru Terminal



Teraz, gdy oprogramowanie jest poprawnie skonfigurowane, możemy dodać portfel Bitcoin.



Masz dwie możliwości:




- Możesz stworzyć nowy wallet od podstaw i używać go wyłącznie w Ashigaru Terminal. W takim przypadku będziesz musiał otwierać to oprogramowanie za każdym razem, gdy będziesz chciał wejść w interakcję z wallet;
- Alternatywnie, można zaimportować istniejący Ashigaru wallet bezpośrednio z telefonu do Ashigaru Terminal. Wadą tej metody jest to, że nieznacznie zmniejsza bezpieczeństwo konfiguracji, ponieważ wallet jest wtedy narażony na dwa ryzykowne środowiska zamiast jednego. Z drugiej strony, zaletą jest możliwość pozostawienia Ashigaru Terminal uruchomionego w sposób ciągły, aby mieszać monety, jednocześnie umożliwiając ich zdalne wydawanie za pośrednictwem aplikacji mobilnej Ashigaru.



W tym samouczku wybierzemy drugą metodę. Jeśli jednak wolisz utworzyć zupełnie nowe portfolio, procedura pozostaje taka sama: jedyną różnicą będzie podczas tworzenia, kiedy będziesz musiał zapisać nową frazę mnemoniczną i nowy passphrase.



Zauważ również, że Ashigaru Terminal nie pozwala na bezpośrednie wydawanie bitcoinów. Możesz zsynchronizować ten sam portfel na Ashigaru Terminal i w aplikacji Ashigaru (co zrobię w tym samouczku) lub w Sparrow Wallet.



Jeśli nie masz jeszcze wallet w aplikacji Ashigaru, możesz skorzystać z dedykowanego samouczka :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Przejdź do menu `Wallets`.



![Image](assets/fr/15.webp)



Następnie wybierz `Utwórz / przywróć wallet...`. Opcja `Otwórz Wallet...` umożliwia dostęp do portfolio już zapisanego w Ashigaru Terminal w późniejszym terminie.



![Image](assets/fr/16.webp)



Nadaj swojemu portfolio nazwę.



![Image](assets/fr/17.webp)



Następnie wybierz typ portfela `Hot Wallet`.






![Image](assets/fr/18.webp)



Na tym etapie procedura różni się w zależności od początkowego wyboru:




- Jeśli chcesz utworzyć nowy portfel od podstaw, kliknij `<Generuj nowy Wallet>`, zdefiniuj passphrase BIP39, a następnie ostrożnie zapisz frazę mnemoniczną i passphrase na nośniku fizycznym;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Jeśli chcesz używać tego samego wallet co aplikacja Ashigaru, wprowadź 12 słów frazy mnemonicznej i passphrase BIP39 bezpośrednio do odpowiednich pól. Wpisz słowa małymi literami, w całości, w kolejności, oddzielone spacją, bez cyfr i dodatkowych znaków.



Po zakończeniu tego kroku kliknij przycisk `< Next >`.



*Uwaga*: Jeśli nie możesz kliknąć tego przycisku, fraza mnemoniczna jest nieprawidłowa. Sprawdź dokładnie, czy żadne ze słów nie jest niepoprawne lub błędnie napisane.



![Image](assets/fr/19.webp)



Następnie należy ustawić hasło. Zostanie ono użyte do odblokowania terminala Ashigaru wallet i zabezpieczenia go przed nieautoryzowanym dostępem fizycznym. Nie jest ono zaangażowane w kryptograficzne wyprowadzanie kluczy: innymi słowy, nawet bez tego hasła każdy, kto posiada frazę mnemoniczną i passphrase, będzie w stanie przywrócić wallet i uzyskać dostęp do bitcoinów.



Wybierz długie, złożone, losowe hasło. Przechowuj jego kopię w bezpiecznym miejscu: najlepiej na nośniku fizycznym lub w bezpiecznym menedżerze haseł.



Po zakończeniu kliknij przycisk `< OK >`.



![Image](assets/fr/20.webp)



## 5. Korzystanie z portfolio



Następnie możesz wybrać konto, do którego chcesz uzyskać dostęp. Na razie nie zainicjowaliśmy żadnych miksów, więc uzyskamy dostęp do konta `Deposit`.



![Image](assets/fr/21.webp)



Obsługa jest identyczna jak w Sparrow, ponieważ Ashigaru Terminal jest fork serwera Sparrow. Znajdziesz te same menu:



![Image](assets/fr/22.webp)





- transakcje": pozwala sprawdzić historię transakcji powiązanych z tym kontem. W moim przypadku niektóre z nich już się pojawiły, ponieważ dokonałem ich za pomocą aplikacji Ashigaru na tym samym wallet.



![Image](assets/fr/23.webp)





- receive`: generuje nowy, pusty adres odbioru w celu umieszczenia środków na koncie depozytowym.



![Image](assets/fr/24.webp)





- addresses`: wyświetla listę wszystkich adresów, niezależnie od tego, czy należą do wewnętrznego czy zewnętrznego łańcucha konta.



![Image](assets/fr/25.webp)





- `UTXOs`: wyświetla listę wszystkich dostępnych UTXO.



![Image](assets/fr/26.webp)





- `Settings`: daje dostęp do *deskryptora* portfela. Możesz również sprawdzić seed, dostosować *Gap Limit* lub zmienić datę utworzenia portfela.



![Image](assets/fr/27.webp)



Wiesz już, jak zainstalować i obsługiwać Ashigaru Terminal. W następnym samouczku zobaczymy, jak wykonywać coinjoiny za pomocą tego oprogramowania i jak zarządzać środkami w "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
