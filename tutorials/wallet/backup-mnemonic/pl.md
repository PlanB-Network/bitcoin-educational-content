---
name: Zapisz swoją frazę Mnemonic
description: Poznaj najlepsze praktyki w zakresie ochrony Bitcoin Wallet
---
![cover](assets/cover.webp)


Kiedy tworzysz nowy Bitcoin Wallet, czy to za pomocą oprogramowania, czy Hardware Wallet, otrzymujesz frazę Mnemonic składającą się z 12 lub 24 słów. Ta fraza jest bardzo ważna, ponieważ jest źródłem wszystkich kluczy prywatnych, które zabezpieczają twoje Bitcoiny. Dlatego musi być starannie chroniona, aby zagwarantować odzyskanie środków w przypadku uszkodzenia, kradzieży lub utraty nośnika Wallet.


W tym samouczku omówimy najlepsze praktyki bezpiecznego zapisywania frazy Mnemonic, aby nie stracić dostępu do swoich bitcoinów.


## Świadomość ryzyka


Mnemonic daje ci pełny, nieograniczony dostęp do wszystkich twoich bitcoinów. Każdy, kto jest w posiadaniu tej frazy, może ukraść twoje fundusze, nawet bez fizycznego dostępu do nośnika, na którym znajduje się Wallet.


Oznacza to na przykład, że jeśli używasz Bitcoin Wallet na Ledger, każdy, kto ma dostęp do twojej frazy Mnemonic, może ukraść wszystkie twoje bitcoiny, nawet bez dostępu do samego Ledger. Dlatego **nigdy nie powinieneś udostępniać swojej frazy Mnemonic**, niezależnie od sytuacji.


Fraza ta jest zatem unikalną informacją, która umożliwia przywrócenie dostępu do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia nośnika Wallet. Weźmy ponownie przykład Ledger: w przypadku utraty urządzenia można odzyskać środki, wprowadzając frazę Mnemonic na nowym Ledger lub dowolnym innym kompatybilnym Wallet, zarówno programowym, jak i sprzętowym.


Dlatego ważne jest, aby zapisać tę frazę z najwyższą starannością i przechowywać ją w bezpiecznym miejscu, co szczegółowo omówimy w kolejnych sekcjach.


**Twoja fraza Mnemonic jest zatem narażona na dwa główne ryzyka: kradzieży i utraty**


Do kradzieży może dojść na dwa główne sposoby:




- Ktoś uzyskał fizyczny dostęp do kopii zapasowej, na przykład podczas włamania lub za pośrednictwem znajomego;
- Dobrowolnie lub mimowolnie podzieliłeś się swoim wyrokiem z inną osobą.


Aby uniknąć fizycznej kradzieży kopii zapasowej frazy Mnemonic, ważne jest, aby przechowywać ją w bezpiecznym miejscu. Przyjrzymy się temu punktowi szczegółowo w kolejnych sekcjach.


Jeśli chodzi o zdalne próby kradzieży, zawsze pamiętaj, aby nigdy nie udostępniać swojej frazy Mnemonic, niezależnie od sytuacji. Próby phishingu są powszechne: fałszywe wiadomości e-mail, strony internetowe imitujące oficjalne portfele lub bezpośrednie prośby za pośrednictwem różnych kanałów komunikacji. Jeśli ktoś prosi o podanie passphrase, jest to oszustwo, nawet w nagłych przypadkach! Złodzieje często podają się za pracowników producenta Hardware Wallet, ale należy pamiętać, że firmy te nigdy nie poproszą o passphrase, niezależnie od sytuacji. Zachowaj więc szczególną czujność wobec wszelkich otrzymywanych wiadomości, czy to za pośrednictwem poczty elektronicznej, telefonu, poczty, sieci społecznościowych, czy nawet osobiście.


W przypadku konieczności wprowadzenia frazy do Hardware Wallet lub oprogramowania w celu przywrócenia dostępu do Wallet po wystąpieniu problemu z początkową obsługą, należy poświęcić czas na sprawdzenie autentyczności i integralności używanego sprzętu lub oprogramowania. Nie panikuj i postępuj metodycznie.


Zachowaj również ostrożność podczas obsługi frazy Mnemonic. Upewnij się, że nie jesteś obserwowany przez inne osoby lub kamerę.


Jeśli chodzi o ryzyko utraty, może ono wynikać z trzech głównych powodów: utraty nośnika kopii zapasowej, jego degradacji lub błędu w jego ocenie. Przyjrzymy się bliżej, jak uniknąć lub zminimalizować te trzy ryzyka w kolejnych sekcjach.


## Wsparcie


Aby zapisać frazę odzyskiwania, należy zapisać ją na nośniku fizycznym, takim jak papier lub metal. Nigdy nie używaj nośnika cyfrowego: nie zapisuj go w pliku tekstowym, nie rób zdjęcia ani nie przechowuj w menedżerze haseł. Metody te znacznie zwiększają powierzchnię ataku w porównaniu z nośnikami fizycznymi. Zasada jest zatem jasna: używaj papieru, kartonu lub metalu do zapisywania swojego hasła.


Podczas gdy zapisywanie frazy na zwykłej kartce papieru jest już dobrą praktyką, wybór metalowego uchwytu, takiego jak stal nierdzewna, zapewnia dodatkowe bezpieczeństwo. Ten rodzaj uchwytu chroni frazę Mnemonic przed ryzykiem pożaru, powodzi lub zawalenia, które mogą mieć wpływ na miejsce przechowywania.


Dla tych, którzy szukają ekonomicznej opcji tworzenia kopii zapasowych swoich fraz na metalu, [metoda DIY "*SAFU Ninja*"](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/) jest doskonałym rozwiązaniem. Wystarczy kupić w sklepie metalowe podkładki, śrubę i nakrętkę. Następnie należy wygrawerować słowa sentencji na każdej podkładce, numerując je i montując na śrubie z nakrętką. Ta niedroga metoda już zapewnia dobrą odporność.


![SEED](assets/fr/01.webp)


Źródło zdjęcia: [*SAFU Ninja Review*, Jameson Lopp](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/).


Jeśli wolisz zainwestować w kompletne metalowe urządzenie do tworzenia kopii zapasowych, polecam zapoznać się z [testami odporności Jamesona Loppa](https://jlopp.github.io/metal-Bitcoin-storage-reviews/), które oceniają większość rozwiązań dostępnych na rynku. Radziłbym zdecydować się na jednoczęściowe wsporniki, takie jak metalowa płytka do grawerowania, tłoczenia lub wykrawania. Takie urządzenia oferują zazwyczaj znacznie większą odporność niż systemy wykorzystujące niezależne litery do montażu.


Jeśli zdecydujesz się na papierowy Wallet, masz kilka opcji: zwykły czysty arkusz papieru, kartonowy Wallet często dostarczany z Hardware Wallet lub nasz szablon do pobrania, który możesz wydrukować [klikając tutaj] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/Wallet-backup-sheet/assets/Mnemonic-sheet.pdf).


![SEED](assets/fr/02.webp)


## Kopia zapasowa


Teraz, gdy wybrałeś już swój fizyczny nośnik, nadszedł czas, aby zapisać swoją frazę odzyskiwania! Aby uniknąć utraty bitcoinów, postępuj zgodnie z poniższymi najlepszymi praktykami.


Po pierwsze, upewnij się, że nie jesteś obserwowany, ani przez inne osoby, ani przez kamery, gdy piszesz swoje zdanie.


Następnie poświęć czas na jasne i czytelne napisanie każdego słowa. Być może będziesz musiał ponownie przeczytać swoje zdanie za wiele lat lub ktoś inny będzie musiał to zrobić w ramach spadku. Staranne pismo odręczne jest zatem niezbędne.


Teoretycznie możliwe jest zapisanie tylko pierwszych 4 liter każdego słowa, ponieważ na liście 2048 słów w BIP39 żadne dwa słowa nie mają tych samych pierwszych 4 liter w tej samej kolejności. Jeśli jednak na nośniku jest wystarczająco dużo miejsca, zalecam zapisywanie każdego słowa w całości. Może to być przydatne w przypadku częściowej degradacji nośnika. Na przykład, jeśli zanotujesz tylko `accu` dla słowa `accuse`, a litera `u` zniknie, możesz być zmuszony do wyboru między `accuse`, `access`, `accident` lub `account`. Z drugiej strony, w przypadku całego słowa, nawet jeśli brakuje jednej litery, nadal łatwo jest rozpoznać prawidłowe słowo.


Ważne jest również, aby pisać słowa we właściwej kolejności. Jeśli masz swoje 24 słowa, ale nie znasz ich dokładnej kolejności, odzyskanie Wallet będzie niemożliwe. Numerowanie słów jest równie ważne: jeśli nośnik zostanie uszkodzony lub słowa zostaną zdezorganizowane, ponumerowanie ich pozwoli ci łatwo umieścić je z powrotem we właściwej kolejności.


![SEED](assets/fr/03.webp)


Ponadto ważne jest, aby zrozumieć, że teoretycznie sama fraza Mnemonic nie zawsze wystarcza do odzyskania dostępu do bitcoinów. Musisz również znać ścieżki derywacji użyte do generate kluczy. Jeśli używasz SingleSig Wallet ze standardową ścieżką, odzyskanie kluczy będzie stosunkowo proste. Jednak w przypadku niestandardowej ścieżki może to stać się niemożliwe, nawet przy posiadaniu frazy Mnemonic. Aby uniknąć tego problemu, zdecydowanie zalecam zanotowanie na nośniku ścieżki derywacji używanego konta. Informacje te można znaleźć w ustawieniach oprogramowania Wallet. Na przykład dla standardowego Taproot Wallet domyślną ścieżką derywacji będzie :


```txt
m / 86' / 0' / 0' /
```


![SEED](assets/fr/04.webp)


W przypadku korzystania z Multisig Wallet lub Wallet ze złożonymi skryptami zawierającymi klucze odzyskiwania, takimi jak te oferowane przez oprogramowanie Liana, konieczne jest zapisanie **Deskryptorów skryptu wyjściowego**. Deskryptory te zawierają wszystkie informacje potrzebne, oprócz fraz odzyskiwania, do odzyskania dostępu do bitcoinów.


Kopię zapasową można również wzbogacić o dodatkowe informacje związane z obsługą Wallet. Na przykład zanotuj kod PIN użyty do odblokowania Hardware Wallet lub słowa antyphishingowe, jeśli używasz karty COLDCARD.


![SEED](assets/fr/05.webp)


Z drugiej strony, jeśli używasz passphrase, upewnij się, że nie zapisujesz go na tym samym nośniku, co frazę Mnemonic. Celem passphrase jest ochrona Wallet w przypadku kradzieży. Aby dowiedzieć się więcej na temat korzystania z passphrase, zapoznaj się z tym uzupełniającym samouczkiem:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Po zapisaniu frazy Mnemonic na nośniku fizycznym zdecydowanie zaleca się wykonanie testu odzyskiwania, gdy nowo utworzony Wallet jest nadal pusty. Test ten polega na zapisaniu przykładowej informacji, celowym usunięciu pustego Wallet, a następnie próbie przywrócenia go przy użyciu tylko fizycznej kopii zapasowej frazy Mnemonic. Umożliwi to sprawdzenie, czy kopia zapasowa jest kompletna i wolna od błędów wejściowych. Pozwoli to również na zapoznanie się z procesem odzyskiwania. W ten sposób, jeśli będziesz musiał odzyskać dane w przyszłości, będziesz lepiej przygotowany i unikniesz stresu związanego z pierwszą próbą w rzeczywistej sytuacji. Aby dowiedzieć się więcej o tym, jak przeprowadzić ten test, zobacz ten poradnik :


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Na koniec pozostaje kwestia liczby kopii zapasowych. Wybór ten zależy wyłącznie od osobistej sytuacji użytkownika. Ograniczenie liczby kopii, na przykład poprzez zapisanie frazy Mnemonic tylko raz na nośniku, zmniejsza ryzyko kradzieży, ale zwiększa ryzyko utraty. I odwrotnie, wykonanie kilku kopii zmniejsza ryzyko utraty, ale zwiększa ryzyko kradzieży. Do użytkownika należy więc znalezienie odpowiedniej równowagi dla swoich potrzeb i określenie liczby kopii, która jest najbardziej odpowiednia.


## Przechowywanie


Po starannym utworzeniu kopii zapasowej frazy Mnemonic nadszedł czas, aby wybrać odpowiednią lokalizację przechowywania. Będzie to zależeć od strategii bezpieczeństwa. W każdym razie wybierz miejsce, które jest poza zasięgiem wzroku, gdzie jest mało prawdopodobne, że ktoś się na nie natknie, ale dostępne do okresowych kontroli. Upewnij się również, że jest chroniony przed Elements, aby zapobiec uszkodzeniu podłoża.


Odradzam również przechowywanie Mnemonic w miejscach, w których nie jesteś suwerenny, takich jak sejf w kancelarii notarialnej lub banku. Opcje te mogą wydawać się bezpieczne, ale oznaczają, że dostęp do kopii zapasowej zależy od strony trzeciej, co jest sprzeczne z podstawowymi zasadami Bitcoin.


W celu zwiększenia bezpieczeństwa zalecam użycie plastikowej torebki zabezpieczonej przed manipulacją lub podobnego systemu zamykania. Umożliwi to sprawdzenie, czy nikt nie uzyskał dostępu do frazy. Na przykład, jeśli przechowujesz swoją frazę w domu i przyjmujesz gości, może być niemożliwe sprawdzenie, czy ktoś ją widział, zapamiętał lub sfotografował. Etui zabezpieczające przed manipulacją ułatwia tego rodzaju weryfikację: jeśli jest nienaruszone, możesz mieć pewność, że Twoja fraza pozostała tajna. Te w pełni nieprzezroczyste etui są dostępne online lub w wyspecjalizowanych sklepach Bitcoin.


![SEED](assets/fr/06.webp)


Wreszcie, gdy zwrot jest przechowywany w kopercie zabezpieczonej przed manipulacją, nie zapomnij zanotować unikalnego identyfikatora koperty. Pozwoli to zweryfikować jej autentyczność podczas kontroli.


## Zarządzanie czasem


Teraz, gdy fraza jest starannie przechowywana, ważne jest, aby regularnie ją monitorować. Okresowo sprawdzaj, czy Twoja fraza jest nadal obecna w miejscu przechowywania i czy jej nieprzezroczysta koperta nie została otwarta.


Podczas tych kontroli można również otworzyć kopertę, aby sprawdzić stan podłoża. Upewnij się, że jest ono nieuszkodzone, a zdanie jest nadal doskonale czytelne. Jeśli zauważysz jakiekolwiek oznaki uszkodzenia, najlepiej utworzyć nową kopię z Hardware Wallet. Sprawdź, czy ta nowa kopia działa, a następnie zniszcz uszkodzoną kopię zapasową, aby uniknąć ryzyka wycieku.


Wreszcie, zarządzanie frazami Mnemonic wiąże się również z kwestią dziedziczenia. Temat ten zostanie szczegółowo omówiony w przyszłym samouczku.


## Idąc dalej


Aby pójść o krok dalej i jeszcze bardziej wzmocnić swoją strategię bezpieczeństwa, zalecam zapoznanie się z technicznym działaniem Bitcoin Wallet. Rozumiejąc, w jaki sposób różne Elements współdziałają ze sobą, a także ich znaczenie i implikacje, będziesz w stanie dostosować swoją strategię bezpieczeństwa z pełną świadomością związanego z tym ryzyka. W szczególności, jeśli zrozumiesz na poziomie technicznym, co umożliwia fraza Mnemonic, będziesz w stanie dostosować sposób rejestrowania, przechowywania i zarządzania nią w czasie.


Dlatego zapraszam do wzięcia udziału w bezpłatnym szkoleniu CYP201 oferowanym przez Plan ₿ Network. Szkolenie to szczegółowo wyjaśnia działanie portfeli Bitcoin, umożliwiając opanowanie aspektów technicznych niezbędnych do skutecznego zabezpieczenia środków:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Jeśli ten poradnik okazał się przydatny, będę wdzięczny za pozostawienie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!