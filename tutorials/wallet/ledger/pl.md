---
name: Ledger Nano S

description: Jak skonfigurować urządzenie Ledger Nano S
---

![image](assets/cover.webp)


Cold fizyczne Wallet - €60 - Początkujący - Aby zabezpieczyć €2,000 do €50,000


Ledger to francuskie rozwiązanie do zabezpieczania bitcoinów w prosty sposób.


W tym samouczku omówimy również sekcję haseł, zaawansowane rozwiązanie bezpieczeństwa do przechowywania dużych kwot: 20,000€ - 100,000€.


https://www.youtube.com/watch?v=_vsHNTLi8MQ


# Podłącz Ledger do Sparrow Bitcoin Wallet (przewodnik pisania)


Upewnij się, że najpierw zapoznałeś się z innym artykułem "Korzystanie z portfeli sprzętowych Bitcoin". Przejdę przez kilka kroków i skupię się głównie na tym, co jest specyficzne dla Ledger.


## Konfiguracja urządzenia


Ledger jest dostarczany z własnym kablem USB. Upewnij się, że używasz tego kabla, a nie jakiegokolwiek innego. Niektóre kable USB służą wyłącznie do zasilania. Ten kabel przesyła dane ORAZ zasilanie. Kiedy używałem urządzenia z leżącym w pobliżu kablem USB do ładowania telefonu, urządzenie nie łączyło się.


Po podłączeniu do komputera urządzenie włączy się.


![image](assets/1.webp)


Przełączaj się między opcjami. Zobaczysz


1. Skonfiguruj jako nowe urządzenie

2. Przywracanie z frazy odzyskiwania


Zasadniczo pyta, czy chcesz, aby urządzenie utworzyło dla ciebie seed, czy też masz już jeden, którego chcesz użyć. Najlepszą praktyką jest stworzenie własnego seed, ale zrobienie tego bezpiecznie jest bardzo zaawansowane i wykracza poza zakres tego artykułu. Wybierz "Skonfiguruj jako nowe urządzenie"


Następnie zostaniesz poproszony o wybranie kodu PIN. Nie jest on częścią Bitcoin seed i jest specyficzny tylko dla tego urządzenia. Blokuje on urządzenie.


Następnie wyświetli 24 słowa, które należy przejrzeć i zapisać.


Co dziwne, gdy dojdziesz do końca, jest napisane "naciśnij w lewo, aby zweryfikować słowa". To nie opisuje, jak potwierdzić, aby kontynuować, oznacza to tylko, że możesz wrócić i ponownie spojrzeć na słowa. Zamiast tego naciśnij prawo i potwierdź, naciskając jednocześnie lewo i prawo.


Następny fragment jest bardzo irytujący. Miesza 24 słowa i musisz potwierdzić każde z nich, od 1 do 24, przechodząc przez wszystkie słowa dla każdego wyboru. Gdy skończysz, możesz potwierdzić za pomocą dwóch przycisków i kontynuować.


![image](assets/2.webp)


Na pulpicie nawigacyjnym znajduje się przycisk ustawień i przycisk ze znakiem plus, który umożliwia instalowanie aplikacji. Ale najpierw musisz połączyć się z Ledger Live. Zrobimy to w następnej kolejności..


## Pobierz Ledger Live


Możesz pobrać Ledger Live z ich strony internetowej, ale lepiej jest pobrać go z GitHub, gdzie przechowywany jest kod źródłowy.


Google "Ledger live GitHub" lub kliknij ![this](link https://github.com/LedgerHQ/Ledger-live-desktop)


![image](assets/3.webp)


Przewiń w dół, aż zobaczysz nagłówek "Pobrane"..


![image](assets/4.webp)


Na dole znajduje się link: Instrukcje dotyczące weryfikacji Hash i podpisów pakietów instalacyjnych są dostępne na tej stronie. Kliknij to łącze.(https://live.Ledger.tools/lld-signatures)


![image](assets/5.webp)


U góry znajdują się łącza do wyboru pakietu oprogramowania, którego potrzebujesz, w zależności od systemu operacyjnego. Kliknij odpowiedni, aby pobrać.


Następnie chcemy zweryfikować Hash pobieranego pliku, dla dodatkowego bezpieczeństwa. Ledger publikuje Hash każdego z dostępnych plików. Teraz sprawdzimy Hash pobranego pliku i porównamy wyniki. Musi być identyczny, aby upewnić się, że plik nie został zmodyfikowany.


Otwórz terminal na komputerze Mac lub CMD w systemie Windows; wpisz w nim następujące polecenia i naciśnij klawisz Enter:


```bash
cd Downloads
```


```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- For Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- For Windows
```


Mam nadzieję, że to oczywiste, że polecenia zaczynają się po strzałkach. Jeśli ten artykuł jest nieaktualny, należy zmienić nazwę pliku w poleceniach na dokładnie taką samą, jak pobrany plik. Po każdym poleceniu należy nacisnąć klawisz <Enter>. Polecenia widoczne tutaj mogą nie zmieścić się w jednej linii w przeglądarce internetowej. Uwaga, wszystko jest wpisane w jednym wierszu.


Spójrz na wynik Hash i upewnij się, że jest identyczny z tym opublikowanym na GitHub.


Idealnie byłoby, gdybyś chciał uzyskać dodatkową fantazję i upewnić się, że publikowane skróty nie są fałszywe. Robimy to za pomocą podpisów gpg, ale jest to poza zakresem tego artykułu. Jeśli chcesz się o tym dowiedzieć (i sugeruję, że w końcu to zrobisz), przejrzyj ten artykuł.


## Połączenie z Ledger Live


Przed uruchomieniem Ledger Live, włączenie VPN trochę pomaga prywatności. Ledger nadal będzie miał wszystkie adresy, ale nie będzie znał twojego IP Address, co zdradza twój domowy Address. Mullvad VPN to doskonała usługa VPN i nie jest bardzo droga (nie reklamuję, po prostu z niej korzystam).


Zainstaluj oprogramowanie na komputerze i uruchom je.


![image](assets/6.webp)


Wybierz swoje urządzenie i wybierz opcję "Pierwsze użycie..."


![image](assets/7.webp)


Następnie zostaniesz przeniesiony przez kreatora, ale wykonaliśmy wszystkie te kroki, abyś mógł przejść przez kolejne etapy.


![image](assets/8.webp)


Po wielu krokach i quizie sprawdzi, czy urządzenie jest prawdziwe. Musisz upewnić się, że jesteś połączony i wprowadziłeś pin, a następnie zapyta na urządzeniu, czy zezwalasz na połączenie Ledger Live. Trzeba to oczywiście potwierdzić.


![image](assets/9.webp)


W następnym wyskakującym okienku pojawiła się reklama shitcoinów przebrana za "informacje o wydaniu". Odrzuć ją, a następnie powinieneś przejść do tego ekranu.


![image](assets/10.webp)


Musisz kliknąć "Dodaj konto", aby uzyskać Bitcoin Wallet.


![image](assets/11.webp)


Upewnij się, że wybrałeś Bitcoin, a nie Bitcoin Cash lub inny shitcoin. Sprawdzi urządzenie i musisz potwierdzić, aby kontynuować NA URZĄDZENIU. Będzie obliczać adresy przez kilka minut. Następnie kliknij DONE.


![image](assets/12.webp)

![image](assets/13.webp)


Świetnie. Teraz masz menedżera shitcoin Wallet zawierającego Bitcoin Wallet na swoim komputerze. Właściwie już go nie potrzebujesz i możesz się go pozbyć. Prawdziwym celem było uzyskanie aplikacji Bitcoin na samym urządzeniu i był to jedyny sposób, bez wykonywania ekstremalnych technik inżynierii oprogramowania.


Pamiętaj, że wcześniej na urządzeniu mieliśmy przycisk ustawień i przycisk ze znakiem plus. Teraz mamy dodatkowy przycisk - przycisk aplikacji Bitcoin.


Możesz teraz wyłączyć Ledger Live.


## Dodaj passphrase


Teraz, gdy mamy aplikację Bitcoin, możemy dodać passphrase do naszej frazy seed. Nie mogliśmy tego zrobić wcześniej, gdy seed został utworzony po raz pierwszy, ponieważ na początku nie mieliśmy aplikacji Bitcoin i musieliśmy połączyć się z Ledger Live, aby ją uzyskać.


Przejdź do menu "ustawienia" w urządzeniu, a następnie do podmenu "zabezpieczenia". Następnie wybierz passphrase. Zobaczysz "Zaawansowane funkcje". Kliknij prawym przyciskiem myszy, zobaczysz "read manuel...", a następnie po kliknięciu prawym przyciskiem myszy zobaczysz "back". Ale to nie koniec. Intuicyjnie można by tak pomyśleć, ale kliknij ponownie prawy przycisk. Zobaczysz "skonfiguruj passphrase".


Możesz wybrać opcję "Dołącz do PIN" lub "Ustaw tymczasowo". Zalecam "dołącz do kodu PIN". W ten sposób można uzyskać dostęp do różnych portfeli w zależności od kodu PIN wprowadzonego po pierwszym włączeniu urządzenia. Jeśli "ustawisz tymczasowo", będziesz musiał wprowadzić passphrase za każdym razem, gdy chcesz uzyskać dostęp do Wallet, ale zawsze z domyślnego kodu PIN.


Wprowadź numer passphrase i potwierdź go.


Zostanie wyświetlony monit o podanie "Bieżącego kodu PIN". Nie jest to kod PIN powiązany z nowym passphrase. Jest to kod PIN wprowadzony podczas włączania urządzenia na potrzeby tej sesji.


Możesz teraz wyjść do menu głównego, wybierając kilka razy opcję powrotu.


## Oglądanie Wallet


W poprzednich artykułach wyjaśniłem, jak pobrać i zweryfikować Sparrow Wallet oraz jak podłączyć go do własnego węzła lub węzła publicznego. Powinieneś postępować zgodnie z tymi instrukcjami:



- Zainstaluj rdzeń Bitcoin ( https://armantheparman.com/bitcoincore/)



- Instalacja Sparrow Bitcoin Wallet (https://armantheparman.com/download-sparrow/)



- Podłącz Sparrow Bitcoin Wallet do Bitcoin Core (https://armantheparman.com/sparrowcore/)


Alternatywą dla Sparrow Bitcoin Wallet jest Electrum Desktop Wallet, ale przejdę do wyjaśnienia Sparrow Bitcoin Wallet, ponieważ uważam go za najlepszy dla większości ludzi. Zaawansowani użytkownicy mogą skorzystać z Electrum jako alternatywy.


Teraz załadujemy go i podłączymy Ledger, z Wallet zawierającym passphrase. Ten Wallet nigdy nie został ujawniony Ledger Live, ponieważ został utworzony PO podłączeniu urządzenia do Ledger Live. Upewnij się, że nigdy więcej nie podłączysz go do Ledger Live, aby nie ujawniać nowego prywatnego Wallet.


Utwórz nowy Wallet:


![image](assets/14.webp)


Nazwij to czymś ładnym


![image](assets/15.webp)


Zwróć uwagę na pole wyboru "Ma istniejącą transakcję". Jeśli jest to Wallet, którego używałeś wcześniej, zaznacz to pole, w przeciwnym razie saldo będzie nieprawidłowo wyświetlane jako zero. Zaznaczenie tego pola powoduje, że Sparrow sprawdza bazę danych Bitcoin Core (Blockchain) pod kątem poprzednich transakcji. W tym przewodniku używamy zupełnie nowego Wallet, więc możesz pozostawić to pole niezaznaczone.


![image](assets/16.webp)


Kliknij "Connected Hardware Wallet" i upewnij się, że urządzenie jest rzeczywiście podłączone, włączone, wprowadzono kod PIN i wprowadzono aplikację Bitcoin.


![image](assets/17.webp)


Kliknij "Skanuj", a następnie "Importuj magazyn kluczy" na następnym ekranie.


![image](assets/18.webp)


Na następnym ekranie nie ma nic do edycji, Ledger wypełnił go za Ciebie. Kliknij "Zastosuj"


![image](assets/19.webp)


Następny ekran umożliwia dodanie hasła. Nie pomyl tego z "passphrase"; wiele osób to zrobi. Nazewnictwo jest niefortunne. Hasło umożliwia zablokowanie Wallet na komputerze. Jest ono specyficzne dla tego oprogramowania na tym komputerze. Nie jest ono częścią klucza prywatnego Bitcoin.


![image](assets/20.webp)


Po chwili przerwy, gdy komputer będzie się zastanawiał, przyciski po lewej stronie zmienią kolor z szarego na niebieski. Gratulacje, Twój Wallet jest teraz gotowy do użycia. Wykonuj i wysyłaj transakcje do woli.


![image](assets/21.webp)


## Odbiór


Aby otrzymać Bitcoin, przejdź do zakładki Adresy po lewej stronie i wybierz jeden z adresów do odebrania. Kliknij prawym przyciskiem myszy żądany Address i wybierz opcję "Kopiuj Address". Następnie przejdź do Exchange, z którego wysyłane są pieniądze i wklej go tam. Możesz też przekazać Address klientowi, który użyje go do dokonania płatności.


Przy pierwszym użyciu Wallet, powinieneś otrzymać bardzo małą ilość, przećwicz wydawanie jej do innego Address, albo wewnątrz Wallet, albo z powrotem do Exchange, aby udowodnić, że Wallet działa zgodnie z oczekiwaniami.


Gdy to zrobisz, musisz wykonać kopię zapasową zapisanych słów. Pojedyncza kopia nie wystarczy. Należy mieć co najmniej dwie kopie papierowe (metalowa jest lepsza) i przechowywać je w dwóch różnych, dobrze zabezpieczonych lokalizacjach. Zmniejsza to ryzyko, że klęska żywiołowa zniszczy kopię HWW i kopię papierową w jednym incydencie. Więcej informacji na ten temat można znaleźć w sekcji "Korzystanie z portfeli sprzętowych Bitcoin".


## Wysyłanie


![image](assets/22.webp)


Dokonując płatności, musisz wkleić Address, do którego płacisz, w polu "Zapłać do". W rzeczywistości nie możesz pozostawić etykiety pustej, to tylko dla zapisów własnych portfeli, ale Sparrow na to nie pozwala - po prostu wpisz coś (tylko ty to zobaczysz). Wprowadź kwotę i możesz również ręcznie dostosować żądaną opłatę.


Wallet nie może podpisać transakcji, jeśli HWW nie jest podłączony. To jest zadanie HWW - odebrać transakcję, podpisać ją i odesłać z powrotem, podpisaną. Upewnij się, że podczas podpisywania na urządzeniu, wizualnie sprawdzasz, czy Address, którym płacisz, jest taki sam na urządzeniu i na ekranie komputera oraz Invoice, który otrzymujesz (np. mogłeś otrzymać wiadomość e-mail, aby zapłacić określonym Address).


Zwróć również uwagę, że jeśli zdecydujesz się użyć monety, która jest większa niż kwota płatności, pozostała część zostanie odesłana z powrotem na jeden z adresów zmiany portfela. Niektórzy ludzie nie wiedzieli o tym i sprawdzili swoją transakcję na publicznym Blockchain i myśleli, że część Bitcoin została wysłana do atakującego Address, ale w rzeczywistości była to ich własna zmiana Address.


## Oprogramowanie układowe


Aby zaktualizować oprogramowanie sprzętowe, należy połączyć się z Ledger Live. Jeśli chcesz to zrobić, powinieneś najpierw wyczyścić urządzenie i upewnić się, że masz dostępne słowa kopii zapasowej i passphrase, aby przywrócić urządzenie. Powodem, dla którego wolę najpierw wyczyścić urządzenie, jest to, że musisz podłączyć urządzenie do Ledger Live, aby zaktualizować oprogramowanie układowe, a ja wolę nigdy nie wystawiać nowego Wallet (tego z passphrase) na Ledger Live. Po prostu nie ufam, że Ledger nie pobiera informacji o moim kluczu publicznym z urządzenia, gdy łączę się z Ledger Live. Twierdzą, że tego nie robią, ale nie mogę tego zweryfikować, dopóki nie przeczytam kodu i nie zrozumiem również wewnętrznego sprzętu.


## Wnioski


Ten artykuł pokazał, jak korzystać z Ledger HWW w bezpieczniejszy i bardziej prywatny sposób niż reklamowany - ale sam ten artykuł nie wystarczy. Jak wspomniałem na początku, powinieneś połączyć go z informacjami zawartymi w "Korzystanie z portfeli sprzętowych Bitcoin".

Wskazówki:


Statyczny piorun Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/ledgersparrow/


Aby zgłębić ten temat i zwiększyć bezpieczeństwo Wallet na Ledger Nano z BIP39 passphrase, zapraszam do zapoznania się z tym obszernym samouczkiem:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49