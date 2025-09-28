---
name: Braiins Mini Miner
description: Łatwe tworzenie Mining z domu.
---
![cover](assets/cover.webp)



### Wprowadzenie



Mini Miner Braiins BMM 100 to produkt stworzony przez Mining pool Braiins. Urządzenie to ma atrakcyjny wygląd i jest niezwykle ciche. Wytwarza 1,1 Th/s mocy obliczeniowej i zużywa około 40 watów. W przeciwieństwie do innych urządzeń, nie jest to produkt open source, ale jego instalacja jest naprawdę łatwa i zajmuje tylko kilka kliknięć! Mini Miner BMM 100 jest pierwszą wydaną wersją. Obecnie w produkcji jest wersja 2, zwana BMM 101, która różni się od pierwszej większym wyświetlaczem i obecnością Wi-Fi, ale procedury instalacji są takie same.



Znacznie więcej ważnych informacji można również znaleźć w kompletnym przewodniku bezpośrednio na stronie [strona producenta] (https://braiins.com/hardware/mini-Miner-bmm-100).



### Przegląd BMM 100



urządzenie wygląda jak równoległościan z wyświetlaczem z przodu



![image](assets/en/01.webp)



wentylator w górnej części



![image](assets/en/02.webp)



natomiast z tyłu mamy: otwór na zasilanie, miejsce na kartę SD (która może być potrzebna do aktualizacji), mały przycisk z napisem `IP REPORT`, który pozwala poznać IP Address mini Miner, który Address jest potrzebny, aby uzyskać dostęp do pulpitu nawigacyjnego urządzenia. Po naciśnięciu przycisku adres IP Address jest wyświetlany przez około 5 sekund, a następnie znika i ponownie pojawia się ekran ustawień. Jeśli jednak zajdzie potrzeba zmiany niektórych ustawień, wystarczy ponownie nacisnąć dany przycisk, a IP Address pojawi się ponownie na ekranie. Kontynuując listę, znajdujemy port Ethernet i dostęp do resetowania urządzenia, w którym należy chwycić pin i przytrzymać przez 10 sekund, aby zresetować wszystkie ustawienia mini Miner. Wreszcie znajdujemy dwa wskaźniki świetlne, jeden Green i jeden czerwony, które wskazują nam status Miner.



![image](assets/en/03.webp)



### Podłączanie Mini Miner



Konieczne będzie podłączenie urządzenia do Internetu przez Ethernet, należy pamiętać, że w nowej wersji (BMM 101) nie jest to już konieczne. Wracając do tego mini Miner, po zlokalizowaniu lokalizacji będziemy musieli podłączyć go najpierw do linii internetowej, a następnie do zasilania: urządzenie włączy się automatycznie i wyświetli swój adres IP Address na ekranie.



### Konfiguracja



Musimy otworzyć przeglądarkę i wpisać IP Address, który pokazuje nam mini Miner w pasku wyszukiwania. Przypominam, że aby znaleźć urządzenie w sieci, musisz być lokalny, więc musisz mieć komputer, którego używasz, podłączony do tej samej sieci co mini Miner. Po wprowadzeniu adresu IP Address wciskamy enter, a na ekranie pojawi się strona logowania do systemu operacyjnego mini Miner, którym jest Braiins OS.



![image](assets/en/06.webp)



Aby się zalogować, należy wpisać `root` jako nazwę użytkownika, natomiast hasło można pozostawić puste. Po kliknięciu zaloguj pojawi się mini panel Miner.



![image](assets/en/07.webp)



### Ustawienia ogólne



Przejdźmy do Systemu



![image](assets/en/24.webp)



w ustawieniach znajdziemy kilka ogólnych ustawień, takich jak motyw (jasny lub ciemny), język, strefa czasowa i zmiana hasła.



![image](assets/en/25.webp)



Jeśli przejdziemy do "Mini Miner Screen" zamiast tego mamy ustawienia naszego mini Miner, takie jak wyświetlanie ekranu. Możemy wybrać, czy ma być wyświetlana godzina, cena Bitcoin, czy też ekran z informacjami o stanie urządzenia, takimi jak produkt Hash, temperatura, zużyte waty itp. Tutaj to użytkownik wybiera, co chce widzieć na ekranie; możemy również zmienić jasność ekranu, ustawić tryb nocny i wyświetlać czas w formacie 12-godzinnym lub 24-godzinnym.



![image](assets/en/26.webp)



Po wprowadzeniu zmian kliknij przycisk `Zapisz zmiany`, a zmiany zostaną wyświetlone na ekranie urządzenia



![image](assets/en/27.webp)



### Połączenie z Mining pool



Teraz jeszcze nie działamy, ponieważ musimy połączyć się z pulą, aby uruchomić Mining, więc musimy przejść do "Konfiguracji"



![image](assets/en/08.webp)



a pierwszy wpis to po prostu `Pools`.



![image](assets/en/09.webp)



Tutaj będziemy musieli zdecydować, której puli użyć. W tym poradniku pokażę dwie opcje. Pierwszą z nich jest podłączenie nas do Mining pool Braiins, który jest również używany przez profesjonalnych górników, jak widać z tego samouczka:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Drugą opcją jest podłączenie nas do Mining pool, który mina w solo, jak Public Pool, postępuj zgodnie z tym przewodnikiem, aby to zrobić:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

#### Basen Braiins



Aby połączyć się z tą pulą, musimy utworzyć konto. Pula ta dokonuje również płatności za pomocą Lightning Network, więc będziemy mogli otrzymać kilka Sats dziennie. Aby to zrobić, musimy skonfigurować błyskawicę Address, na której będziemy otrzymywać nagrody. Jeśli nie wiesz, jak utworzyć konto w puli braiins lub jak skonfigurować piorun Address, możesz postępować zgodnie z tym przewodnikiem:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Gdy to zrobimy, jesteśmy w pulpicie nawigacyjnym puli Braiins. To, co musimy zrobić, to powiedzieć puli, że chcemy połączyć się z jednym z naszych górników, więc po lewej stronie ekranu znajdziesz kilka wpisów. Musimy przejść do "pracowników"



![image](assets/en/04.webp)



i musimy kliknąć fioletowy przycisk po prawej stronie z napisem "Połącz pracowników"



![image](assets/en/05.webp)



Tutaj pojawia się okno z informacjami potrzebnymi do podłączenia naszego mini Miner do puli. Tutaj jedyną zmianą, jaką możemy wprowadzić, jest wybranie Stratum V2. Aby dowiedzieć się, czym jest Stratum v2, zobacz ten wpis w [glosariuszu] (https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Teraz musimy skopiować ten ciąg, który zaczyna się od stratumv2. Klikamy więc mały symbol "kopiuj", a następnie przechodzimy do pulpitu nawigacyjnego naszego mini Miner, który pozostawiliśmy w konfiguracji i pulach. Klikamy na dodaj nową pulę



![image](assets/en/11.webp)



i wklej skopiowany ciąg znaków w miejscu poniżej adresu Pool URL.



![image](assets/en/12.webp)



Teraz musimy dodać nazwę użytkownika i hasło. Wróćmy do puli dashboad. Pod spodem mamy również identyfikator użytkownika i hasło. UserID i nasza nazwa użytkownika, ta, którą podaliśmy podczas tworzenia konta, plus nazwa Miner, którą chcemy umieścić. możesz zdecydować, czy chcesz nadać nazwę urządzeniu, które podłączasz do puli, jest to opcjonalne, ale zaleca się umieszczenie go, więc jeśli podłączysz wiele urządzeń, łatwiej będzie je od razu zidentyfikować. Jeśli nie chcesz nic wpisywać, możesz pozostawić `workerName`.



![image](assets/en/13.webp)



Następnie przechodzimy do naszego mini Miner i wpisujemy nazwę użytkownika. Tutaj wpiszemy w moim przypadku "finalstepbitcoin", który jest moim identyfikatorem użytkownika, miniminer dot. Jest to nazwa, którą zdecydowałem się nadać urządzeniu. Jeśli nie chcesz nadawać mu nazwy, po prostu wpisz userid kropka nazwa robocza. W moim przypadku będzie to finalstepbitcoin.workername. Po wprowadzeniu nazwy użytkownika możesz wybrać hasło i wpisać je w puste pole. Możesz również wpisać anithing123, który jest również wyświetlany na ekranie puli, ale po prostu chce wskazać, że możesz wpisać dowolne hasło.



Po wprowadzeniu wszystkich danych należy nacisnąć przycisk zapisu po prawej stronie (ten w kształcie dyskietki) i w ten sposób skonfigurować dane puli w mini Miner.



![image](assets/en/14.webp)



Teraz musisz wrócić do pulpitu puli i kliknąć "Połączono! Wróć."



![image](assets/en/15.webp)



Podłączyliśmy nasz mini Miner do puli Braiins! Możesz go teraz zobaczyć na liście pracowników. Jeśli się nie pojawi, odśwież ją i poczekaj kilka chwil. Gdy się pojawi, sprawdź, czy ma status "OK" ze znacznikiem wyboru Green.



![image](assets/en/17.webp)



jeśli wrócisz do pulpitu nawigacyjnego, powinieneś zacząć widzieć ruch na wykresie i zobaczyć Hashrate naszego urządzenia. Oznacza to, że pula odbiera naszą pracę, a zatem podważamy wszystkie intencje i cele.



![image](assets/en/16.webp)



#### Basen publiczny



Dzięki tej puli można spróbować szczęścia i wydobywać solo, opierając się na puli. W tym przypadku nie otrzymamy nagrody, ale otrzymamy pełną nagrodę, jeśli kiedykolwiek uda nam się wydobyć blok. Następnie łączymy się z pulą publiczną, pulą tylko Mining, która jest całkowicie otwarta. Otwieramy nowe okno w przeglądarce i przechodzimy do [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



pojawi się strona ze wszystkimi potrzebnymi informacjami. Następnie kopiujemy tam warstwę Address



![image](assets/en/19.webp)



następnie wracamy do pulpitu nawigacyjnego naszego mini Miner, przechodzimy do konfiguracji i do pul, klikamy na dodaj nową pulę (ten sam proces, co powyżej) i wklejamy 'stratum Address pod adresem url puli.



![image](assets/en/20.webp)



Teraz wróćmy do strony puli i zobaczmy, że jako nazwę użytkownika musimy wpisać Bitcoin Address, który będzie tym, na którym otrzymamy nagrodę w przypadku podważenia bloku, następnie kropkę, a następnie nazwę naszego urządzenia, tak jak to zrobiliśmy wcześniej z Braiins Pool, podczas gdy hasło możemy wybrać sami.



![image](assets/en/21.webp)



Wracamy do mini Miner i pod nazwą użytkownika wklejamy Address Bitcoin, po którym następuje kropka i nazwa, ja wpiszę `miniminer`. W haśle zamiast tego wpiszę test, możesz wpisać cokolwiek chcesz.



![image](assets/en/22.webp)



Teraz zapisujemy ustawienia i wyłączamy pulę Braiins.



![image](assets/en/23.webp)



Dobrze! Jesteśmy teraz Mining na basenie publicznym!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)