---
name: BTCPay Server
description: Akceptowanie płatności BTC bez pośredników
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server to darmowy pakiet oprogramowania o otwartym kodzie źródłowym stworzony przez Nicolasa Doriera, który umożliwia akceptowanie płatności bitcoinami bez pośredników. Zaprojektowany z myślą o autonomii i suwerenności finansowej, instaluje się na własnym serwerze i zapewnia pełne zarządzanie transakcjami, od fakturowania po walidację płatności on-chain lub Lightning Network i księgowość. Łatwo integruje się z witrynami e-commerce (WooComerce, Shopify itp.) lub może być używany jako terminal płatniczy w sklepach fizycznych (*POS*).



BTCPay Server to bez wątpienia najbardziej zaawansowane rozwiązanie dla sprzedawców chcących akceptować bitcoiny. Jest to najbardziej wszechstronne i solidne oprogramowanie pod względem bezpieczeństwa, suwerenności i poufności. Z drugiej strony, jest ono również najbardziej skomplikowane w instalacji i utrzymaniu. Istnieją również prostsze alternatywy: niektóre są całkowicie powiernicze, jak OpenNode, podczas gdy inne oferują interesujący kompromis między łatwością użytkowania a suwerennością, jak Swiss Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Celem tego samouczka jest poprowadzenie użytkownika krok po kroku przez instalację, konfigurację i korzystanie z serwera BTCPay, tak aby można było wdrożyć bezpieczną, niezależną infrastrukturę płatniczą zgodnie z etosem Bitcoin.



## Funkcje serwera BTCPay



Scentralizowane rozwiązania Bitcoin w punktach sprzedaży, takie jak na przykład *OpenNode*, oferują łatwość użytkowania, ale polegają na firmie zewnętrznej, ponieważ nie mogą być hostowane samodzielnie i w większości przypadków są zastrzeżone. Chociaż ułatwiają konfigurację płatności, wiążą się z opłatami prowizyjnymi i narażają użytkowników na większe ryzyko niż rozwiązanie takie jak BTCPay Server, zarówno pod względem przechowywania środków, jak i poufności.



Serwer BTCPay jest przeznaczony dla sprzedawców internetowych lub fizycznych, stowarzyszeń i organizacji non-profit, które chcą otrzymywać darowizny w bitcoinach. Jest to również idealne rozwiązanie dla właścicieli projektów i deweloperów poszukujących bezpośredniego wsparcia od swojej społeczności.



Specjalne funkcje BTCPay Server obejmują :




- jego **pełną autonomię**,
- brak procedury **KYC**,
- pełna kontrola nad środkami**,
- **eliminacja opłat platformowych**.



Stając się własnym procesorem płatności, eliminujesz wszelką zależność od scentralizowanej strony trzeciej między Tobą a Twoimi klientami. Możesz akceptować płatności bezpośrednio w bitcoinach i fakturach płatniczych generate. Gwarantuje to, że ani Ty, ani Twoja firma nie możecie zostać zbanowani przez nikogo innego. Odgrywasz rolę zarówno banku, jak i procesora płatności, bez konieczności płacenia prowizji pośrednikowi za każdą transakcję.



Opłaty transakcyjne dla **on-chain** pozostają niezmienione, ale można je obniżyć, korzystając z sieci **Liquid** lub **Lightning**.



Ponadto :




- W pełni konfigurowalny interfejs i faktury;
- Natywne wsparcie **Tor** dla zwiększonej poufności;
- Wsparcie dla **crowdfundingu**, **POS** i **przycisków płatności**;
- Kompatybilny z wieloma walutami;
- Bitcoin płatności bezpośrednie i peer-to-peer ;
- Pełna kontrola nad kluczami prywatnymi;
- Zwiększona prywatność ;
- Zwiększone bezpieczeństwo;
- Oprogramowanie hostowane samodzielnie;
- Wsparcie dla **SegWit** i **Sieci Lightning**;
- Wewnętrzny portfel oparty na węzłach, z integracją portfeli sprzętowych.



## Instalacja i konfiguracja serwera BTCPay



### Wybór trybu hostingu



Serwer BTCPay można zainstalować na wiele różnych sposobów. W zależności od potrzeb i zasobów istnieją trzy główne opcje:




- Serwer BTCPay hostowany przez stronę trzecią**: korzystasz z platformy, która hostuje usługę dla Ciebie. Jest to proste, ale zazwyczaj nie jest darmowe.
- Serwer BTCPay hostowany samodzielnie na serwerze w chmurze** (np. za pośrednictwem [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) lub innego dostawcy). Jest to zalecane rozwiązanie dla większości początkujących sprzedawców.
- Serwer BTCPay zainstalowany na własnym sprzęcie (lokalnie)** : na komputerze, mini-PC lub Umbrel. Ta metoda jest bardziej techniczna, ale oferuje całkowitą niezależność.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Dla początkującego sprzedawcy **wdrożenie na serwerze w chmurze** jest najlepszym kompromisem między autonomią, prostotą i bezpieczeństwem, bez konieczności zarządzania całą infrastrukturą techniczną.



Serwer BTCPay można szybko wdrożyć u wielu dostawców usług hostingowych. Wśród nich **Voltage** wyróżnia się jako wzorcowe rozwiązanie dla użytkowników wymagających **niezawodnej**, **profesjonalnej** i **zagranicznej** infrastruktury.



### Utwórz instancję serwera BTCPay na serwerze Voltage



**Voltage** to gotowa platforma hostingowa Bitcoin i Lightning, która umożliwia natychmiastowe wdrożenie własnego serwera BTCPay, bez skomplikowanej konfiguracji lub konserwacji serwera.



Odwiedź [oficjalną stronę Voltage](https://voltage.cloud).



![capture](assets/fr/03.webp)



Utwórz **konto użytkownika** z prawidłowym adresem e-mail i silnym hasłem.



![capture](assets/fr/04.webp)



Voltage oferuje **bezpłatny 7-dniowy okres próbny**. Należy pamiętać, że po 7-dniowym bezpłatnym okresie próbnym zostaniesz poproszony o zarejestrowanie się w stałej subskrypcji w wysokości **25 USD miesięcznie**, aby kontynuować **utrzymywanie aktywnych węzłów**.



Po utworzeniu konta Voltage i zalogowaniu się po raz pierwszy, zostaniesz przekierowany na stronę główną, która ma dwie główne sekcje:




- Sekcja **Infrastruktury** do zarządzania węzłami Lightning, Bitcoin Core, serwerem BTCPay i innymi usługami Bitcoin w chmurze;
- oraz sekcję **Płatności**, która umożliwia dostęp do API Lightning firmy Voltage w celu zintegrowania płatności Bitcoin z niestandardowymi aplikacjami.



Aby wdrożyć instancję **BTCPay Server**, kliknij **Infrastruktura dostępu**. W tym miejscu można tworzyć, zarządzać i monitorować wszystkie usługi, w tym węzeł Bitcoin i serwer BTCPay.



#### Utwórz grupę



Przed wdrożeniem usługi platforma wyświetli monit o **utworzenie grupy**. Grupa** (obszar roboczy) to obszar roboczy, który grupuje wszystkie usługi Bitcoin i Lightning (np. węzeł, serwer BTCPay, eksplorator itp.). To trochę jak folder zawierający różne projekty.



![capture](assets/fr/05.webp)



Na potrzeby tego samouczka utworzona przez nas grupa będzie nosiła nazwę **Genesis**. Jeśli chcesz, możesz dodać zdjęcie profilowe. Gdy to zrobisz, kliknij przycisk **Twórz**. Możesz zaprosić innych użytkowników do dołączenia do grupy, a nawet zmienić nazwę grupy, jeśli chcesz.



Na stronie głównej grupy dostępnych jest kilka opcji:




- Węzły Lightning**: aby wdrożyć kompletny węzeł Lightning (LND);
- Węzły rdzenia Bitcoin**: aby uruchomić kompletny węzeł Bitcoin;
- Serwer BTCPay** : do hostowania gotowej do użycia instancji BTCPay;
- Konta Nostr**: do zarządzania tożsamościami Nostr.



Aktywuj **podwójne uwierzytelnianie (2FA)**, aby zabezpieczyć swoje konto i usługi (przycisk jest widoczny na czerwono, jeśli jest nieaktywny).



![capture](assets/fr/06.webp)



Kliknij **BTCPay Server** wśród opcji, a następnie **Launch a BTCPay Store**.



![capture](assets/fr/07.webp)



Voltage poprosi następnie o **utworzenie i skonfigurowanie instancji serwera BTCPay** poprzez wybranie **nazwy usługi** (1) i włączenie płatności Lightning (2).



Jeśli zdecydujesz się akceptować płatności Lightning, będziesz potrzebować węzła Lightning.



Jeśli nie masz jeszcze węzła Bitcoin lub Lightning, Voltage automatycznie zasugeruje jego utworzenie.



Kliknij na **Utwórz węzeł Lightning** (3) .



![capture](assets/fr/08.webp)



Po przejściu do interfejsu tworzenia węzła zostaniesz poproszony o wybranie między **standardowym** i **profesjonalnym** układem.



Możesz utworzyć prawdziwy węzeł (**Mainnet**) lub węzeł testowy (**Testnet**). Następnie kliknij przycisk **Kontynuuj**.



![capture](assets/fr/09.webp)



W tym poradniku użyjemy planu standardowego. Wprowadź **nazwę węzła**, **hasło** i naciśnij przycisk **Utwórz**.



![capture](assets/fr/10.webp)



Po kilku chwilach węzeł zacznie działać i będzie można otworzyć darmowy kanał o przepustowości 500 000 sats.



![capture](assets/fr/11.webp)



Nieco dalej po prawej stronie znajdziesz wszystkie potrzebne informacje na temat węzła!



![capture](assets/fr/12.webp)



Teraz, gdy mamy już uruchomiony nasz węzeł Lightning, wróćmy do instalacji naszego serwera BTCPay. Możesz teraz kliknąć przycisk **Utwórz BTCPay**.



![capture](assets/fr/13.webp)



Otworzy się strona z domyślnymi danymi logowania oraz komunikatem z prośbą o zmianę początkowego hasła. Gdy to zrobisz, kliknij przycisk **Zaloguj się teraz**, aby uzyskać dostęp do interfejsu.



![capture](assets/fr/14.webp)



To wszystko! Twój serwer BTCPay jest gotowy do użycia. Zostaniesz przekierowany bezpośrednio na stronę logowania do serwera BTCPay.



![capture](assets/fr/15.webp)



Po zalogowaniu skonfiguruj swój pierwszy **sklep**:





- Nadaj mu **nazwę**.





- Wybierz **domyślną walutę** (EUR, USD, CFA itp.).





- Wybierz **dostawcę kursów wymiany** (np. CoinGecko).



![capture](assets/fr/16.webp)



Nastąpi przekierowanie do pulpitu nawigacyjnego sklepu. W interfejsie pulpitu nawigacyjnego zauważysz, że przycisk **Utwórz swój sklep** jest zaznaczony na zielono, ponieważ ten krok został już zakończony.



![capture](assets/fr/17.webp)



Nieco dalej mamy przyciski **Konfiguruj wallet** i **Konfiguruj węzeł Lightning**. W naszym przypadku połączyliśmy się już z węzłem Lightning działającym na napięciu. Więc nie będziemy musieli tego robić tutaj.



Przejdźmy teraz do konfiguracji portfolio. Kliknij przycisk **Konfiguruj portfolio**.



Ponieważ dopiero zaczynamy pracę z serwerem BTCPay, podłączmy istniejący wallet. Naciśnij więc **Podłącz istniejący portfel**.



![capture](assets/fr/18.webp)



Następnie należy wybrać **metodę importu**. Wśród dostępnych opcji wybierz **Wprowadź rozszerzony klucz publiczny**.



![capture](assets/fr/19.webp)



Łącząc istniejący wallet, możesz otrzymywać płatności **bezpośrednio na tym zewnętrznym wallet**, bez dostępu serwera BTCPay do twojego klucza prywatnego. Tak więc, nawet jeśli serwer zostałby zhakowany lub klucz publiczny (`xpub`) naruszony, atakujący mógłby wyświetlić historię transakcji, ale **nie byłby w stanie uzyskać dostępu do twoich środków**.



Po kliknięciu przycisku **Wprowadź rozszerzony klucz publiczny** zostaniesz **przekierowany** na stronę, na której musisz podać ten klucz.



Teraz pobierzmy **rozszerzony klucz publiczny**.



### Podłączanie Bitcoin wallet



Aby otrzymywać płatności, musisz podłączyć Bitcoin wallet do swojego sklepu. W tym celu dostępnych jest kilka opcji:





- Portfolio sprzętu** (Ledger, Trezor, Coldcard...) ;





- Portfolio oprogramowania** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- Serwer BTCPay** wewnętrzny wallet (niezalecany, ponieważ jest mniej bezpieczny i bardziej naraża środki w przypadku włamania na serwer).



W tym samouczku będziemy używać **portfolio oprogramowania**, które jest bardziej dostępne do początkowej konfiguracji. Możesz wybierać spośród wielu kompatybilnych aplikacji: **Electrum**, **Phoenix**, **Zeus**, **Muun** itd.



Do demonstracji użyjemy **Electrum**. Otwórz **Electrum**, kliknij na **Portfolio**, a następnie na **Informacje**:



![capture](assets/fr/20.webp)



Następnie skopiuj **główny klucz publiczny (xpub)**.



![capture](assets/fr/21.webp)



Po skopiowaniu głównego klucza publicznego wklej go w polu dostępnym na stronie serwera BTCPay.



![capture](assets/fr/22.webp)



Po weryfikacji nastąpi przekierowanie do pulpitu nawigacyjnego sklepu.



![capture](assets/fr/23.webp)



### Generowanie punktu sprzedaży (PoS)



Po skonfigurowaniu sklepu i portfolio możesz teraz skonfigurować **punkt sprzedaży (PoS)**, aby zacząć otrzymywać płatności Bitcoin bezpośrednio od klientów.



Ta zintegrowana funkcja **BTCPay Server** jest idealna dla **handlowców, rzemieślników, restauratorów lub usługodawców**, którzy chcą akceptować Bitcoin **bez strony internetowej** lub specjalnych umiejętności technicznych.



### Jaki jest punkt sprzedaży?



**PoS** to **uproszczony interfejs POS**, który działa jak **terminal płatniczy Bitcoin**.


Pozwala na :




- Utwórz **menu produktów lub usług** ze stałymi cenami.
- Wygeneruj **natychmiastową fakturę z kodem QR** do zeskanowania.
- Udostępnij **adres URL płatności** dostępny za pośrednictwem smartfona, tabletu lub komputera.



Innymi słowy, PoS zamienia twój serwer BTCPay w **bezpośredni interfejs sprzedaży**, gdzie każda płatność jest odbierana **w twoim własnym Bitcoin wallet**, bez pośredników.



### Konfiguracja PoS



W panelu BTCPay kliknij na **PLUGINS**, a następnie na **Point of sale**.



Następnie kliknij **Utwórz nową aplikację PoS**. Ta czynność dodaje **nową aplikację** do sklepu BTCPay, tak jakbyś instalował mini wewnętrzną witrynę sprzedaży.



Zostanie otwarta strona umożliwiająca utworzenie aplikacji. Zdefiniuj **nazwę aplikacji**: jest to nazwa wewnętrzna, widoczna tylko z pulpitu nawigacyjnego (np. _Shoe Shop_).



Kliknij przycisk **Utwórz**, aby zatwierdzić.



![capture](assets/fr/24.webp)



Po utworzeniu zostaniesz przekierowany na **stronę szczegółowej konfiguracji** punktu sprzedaży.



### Dostosuj swój interfejs sprzedaży



Na tej stronie można zdefiniować podstawowe elementy systemu PoS:





- Nazwa aplikacji** (wewnętrzna nazwa zarządzania, może zostać zmieniona w dowolnym momencie).





- Wyświetlany tytuł** (to, co klienci zobaczą u góry strony).





- Styl punktu sprzedaży** (tryb **Opis** jest odpowiedni dla usług takich jak strzyżenie lub posiłki, podczas gdy tryb **Katalog produktów** jest idealny dla sklepów oferujących kilka produktów).





- Wyświetlana waluta** (wybierz **XOF**, **EUR** lub **USD** zgodnie ze swoimi zwykłymi cenami).





- Lista produktów** (dodaj tutaj swoje produkty, opisy i ceny).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Zapisz i przetestuj swój PoS



Po zakończeniu konfiguracji kliknij **Zapisz**, aby zapisać ustawienia, a następnie **Widok**, aby wyświetlić podgląd PoS.



Zobaczysz stronę prezentującą Twoje produkty, z każdym przyciskiem odpowiadającym produktowi lub usłudze.



Gdy tylko klient wybierze produkt:



1. BTCPay automatycznie generuje fakturę Bitcoin lub Lightning**.



2. Na ekranie pojawi się **kod QR**.



3. Klienci mogą **skanować i płacić bezpośrednio** za pomocą Bitcoin wallet.




![capture](assets/fr/27.webp)



### Wynik końcowy



Masz teraz kompletny **Bitcoin Point of Sale**, który możesz :





- Otwieranie ze smartfona lub tabletu w sklepie;





- Wyświetlanie na ekranie w celu zeskanowania przez klienta;





- Lub udostępnić za pośrednictwem publicznego adresu URL, takiego jak uproszczona strona zamówienia.



Przy każdej płatności kwota jest automatycznie zapisywana na **własnym koncie BTCPay wallet**, bez pośredników lub opłat stron trzecich.


Dzięki temu PoS staje się **samodzielnym terminalem płatniczym Bitcoin**.




## Codzienne użytkowanie



Przed wypłatą jakichkolwiek rzeczywistych płatności zalecamy przeprowadzenie **testu**, aby sprawdzić, czy wszystko działa prawidłowo.



### Testowanie płatności





- Utwórz fakturę** z poziomu interfejsu PoS (na przykład za produkt o wartości 1 satoshi lub niewielką kwotę).





- Zeskanuj wyświetlony na ekranie kod QR** za pomocą Bitcoin lub Lightning wallet (takich jak **Phoenix**, **Muun** lub **Wallet lub Satoshi**).




![capture](assets/fr/28.webp)





- Zatwierdź płatność** w wallet: transakcja zostanie wysłana natychmiast.





- Powrót do serwera BTCPay**: faktura pojawi się jako **Zapłacona** na liście.



![capture](assets/fr/29.webp)



Gratulacje! Twój punkt sprzedaży jest teraz **funkcjonalny**. Możesz zacząć otrzymywać płatności Bitcoin od swoich klientów, prosto, szybko i bez pośredników.



### Tworzenie faktury dla klienta



W menu **Faktury** kliknij **Nowa faktura**.



![capture](assets/fr/30.webp)



Wprowadź **kwotę** i **walutę lokalną** (BTCPay automatycznie oblicza równowartość w BTC), a także inne informacje o produkcie.



![capture](assets/fr/31.webp)



Udostępnij klientowi **kod QR** lub **URL**.



![capture](assets/fr/32.webp)



### Śledzenie otrzymanych płatności



W menu **Faktury** zobaczysz listę wszystkich swoich transakcji.


Możliwe statusy to :





- Oczekuje**: płatność nie została jeszcze potwierdzona.





- Zapłacono**: płatność potwierdzona.





- Wygasła**: faktura nieopłacona w terminie.



### Zwrot pieniędzy klientowi



W menu **Faktury** wybierz fakturę do zwrotu.



![capture](assets/fr/33.webp)



Kliknij **Refund** i wprowadź adres Bitcoin podany przez klienta.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Raporty i eksport danych



BTCPay Server umożliwia **eksportowanie transakcji** (w formacie CSV lub Excel). Jest to bardzo praktyczne dla księgowości i kasy.



![capture](assets/fr/36.webp)



W menu **Report** kliknij na **Export**: wszystkie transakcje zostaną zapisane w pliku CSV, z którym można następnie zapoznać się lokalnie.



## Bezpieczeństwo i najlepsze praktyki



Autonomia przyznana przez serwer BTCPay (pełna suwerenność nad środkami) jest prawdziwą siłą. Z tą wolnością wiąże się jednak większa odpowiedzialność w zakresie bezpieczeństwa. Zarządzając własnymi płatnościami, przyjmujesz rolę własnego banku. Dlatego konieczne jest przyjęcie najlepszych praktyk w celu ochrony środków, danych i infrastruktury. Oto główne punkty, które należy wziąć pod uwagę.



### Bezpieczny dostęp do serwera





- Używaj silnego hasła: łącz duże i małe litery, cyfry i znaki specjalne. Unikaj ponownego używania istniejącego hasła.
- Aktywuj uwierzytelnianie dwuskładnikowe (2FA), aby uzyskać dostęp do interfejsu BTCPay.
- Regularnie aktualizuj system operacyjny, instancję serwera BTCPay i zależności (Docker, węzeł Bitcoin, węzeł Lightning...). Aktualizacje często usuwają luki w zabezpieczeniach.



### Zarządzanie kluczami prywatnymi i tworzenie ich kopii zapasowych





- Zapisuj klucze prywatne i frazy seed offline na nośnikach fizycznych (papierowych lub metalowych).
- Najlepiej użyć sprzętowego wallet.
- Przechowuj kilka kopii zapasowych w oddzielnych, chronionych lokalizacjach fizycznych.



### Bezpieczne płatności i poufność





- Skorzystaj z sieci Tor lub VPN, aby ukryć adres IP swojego serwera i chronić swoją prywatność.
- Wyłącz niepotrzebne porty na serwerze i ogranicz połączenia SSH tylko do zaufanych adresów.
- Aktywuj HTTPS (certyfikat SSL) dla wszystkich połączeń z interfejsem internetowym BTCPay.
- Nigdy nie udostępniaj interfejsu administracyjnego personelowi, który nie został przeszkolony w zakresie zarządzania portfelem Bitcoin.



### Wdrażanie najlepszych praktyk dla sieci Lightning



Twój sklep jest podłączony do **węzła Lightning hostowanego na Voltage**, co znacznie upraszcza techniczne zarządzanie siecią. Niemniej jednak nadal ważne jest przyjęcie **dobrych praktyk monitorowania i bezpieczeństwa**:





- Zapisz login węzła Voltage API** i klucze dostępu (które umożliwiają połączenie BTCPay).
- Chroń swoje konto Voltage** za pomocą uwierzytelniania dwuskładnikowego i silnego hasła.
- Monitoruj status węzła i kanału** z pulpitu nawigacyjnego Voltage: pomaga to wykryć wszelkie anomalie lub desynchronizację.
- Unikaj udostępniania swoich danych uwierzytelniających API** lub ujawniania ich publicznie (np. w kodzie witryny).
- W przypadku migracji wystarczy **rekonfigurować połączenie między BTCPay i Voltage**: nie trzeba ręcznie zamykać kanału.



Dzięki Voltage korzystasz z **bezpiecznej, wysoce dostępnej** i **automatycznie tworzonej kopii zapasowej** infrastruktury, zachowując **pełną suwerenność nad płatnościami Lightning**.



### Organizacja i struktura procedur wewnętrznych





- Zdefiniuj jasne zasady zarządzania dostępem: kto może tworzyć faktury, przeglądać płatności, uzyskiwać dostęp do węzła itp.
- Udokumentuj swoje procedury tworzenia kopii zapasowych i przywracania danych, aby móc szybko zareagować w razie incydentu.
- Regularnie testuj przywracanie kopii zapasowych, aby upewnić się, że działają one prawidłowo.
- Przeszkol swój personel lub współpracowników w zakresie podstawowych zasad bezpieczeństwa operacyjnego: czujność na phishing, korzystanie z bezpiecznych haseł, poszanowanie poufności.



### Nadzór i ustanowienie bieżącej konserwacji





- Ciągłe monitorowanie aktywności serwera za pomocą narzędzi do rejestrowania lub monitorowania.
- Zaplanuj okresowy przegląd bezpieczeństwa: sprawdź aktualizacje, dostęp, kopie zapasowe i spójność transakcji.



Gratulacje! Dotarłeś do końca tego samouczka. Możesz teraz samodzielnie zapoznać się z serwerem BTCPay, co ułatwi Ci zarządzanie sklepem.



Aby dowiedzieć się więcej, polecam udział w naszym kompletnym szkoleniu na temat integracji Bitcoin w firmie:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a