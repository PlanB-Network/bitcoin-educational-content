---
name: Konfiguracja pierwszego węzła Lightning
goal: Zrozumienie, instalacja, konfiguracja i korzystanie z węzła Lightning
objectives: 


  - Zrozumienie roli i celu węzła Lightning.
  - Identyfikacja różnych dostępnych rozwiązań programowych.
  - Zainstaluj i skonfiguruj węzeł Lightning (LND).
  - Podłącz konto wydatków.
  - Poznaj ryzyko związane z korzystaniem z węzła Lightning.


---

# Pierwszy krok w kierunku autonomii w Lightning



Zdobyłeś już swój pierwszy sats, zabezpieczyłeś środki na własne utrzymanie i wdrożyłeś węzeł Bitcoin, aby być suwerennym w korzystaniu z on-chain. Następnym krokiem jest uzyskanie takiej samej autonomii na Lightning: to jest właśnie cel tego kursu.



LNP202 jest przeznaczony dla średnio zaawansowanych użytkowników i prowadzi krok po kroku przez wdrożenie pierwszego węzła Lightning, bez zaawansowanych umiejętności technicznych.



Dowiesz się, jak zainstalować LND na Umbrel, otworzyć kanały i zarządzać nimi, nadzorować węzeł i podłączyć mobilny wallet, dzięki czemu będziesz mógł cieszyć się doświadczeniem porównywalnym z wallet, zachowując pełną kontrolę nad swoimi środkami.



+++


# Wprowadzenie


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Przegląd kursu


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 to praktyczny kurs mający na celu uzyskanie autonomii w Lightning poprzez obsługę własnego węzła. Cel jest prosty: zacząć od węzła Bitcoin, wdrożyć LND na Umbrel, odpowiednio go zabezpieczyć, otworzyć i zarządzać pierwszymi kanałami, a następnie korzystać z węzła na co dzień z mobilnego wallet. Ten kurs zakłada, że przeszedłeś już kurs BTC 202, ponieważ zakładam, że twój węzeł Bitcoin na Umbrel jest już na miejscu i zsynchronizowany. Nie będziemy tutaj wracać do tego, jak skonfigurować węzeł Bitcoin.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Aby lepiej zrozumieć wewnętrzną mechanikę Lightning, kurs LNP 201 jest również wysoce zalecany, chociaż nie jest to warunek wstępny dla tego kursu:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

W pierwszej części tego kursu LNP202 przyjrzymy się, czym tak naprawdę jest węzeł Lightning, czym różni się od prostego wallet i dlaczego obsługa węzła osobistego jest jedynym sposobem korzystania z Lightning bez delegowania sats do zaufanej strony trzeciej. Ta sekcja kończy się strategicznym wyborem: które rozwiązanie jest odpowiednie dla Ciebie, od najprostszych podejść do klasycznego węzła Lightning, który będziemy wdrażać w tym kursie.



W części 2 kursu zainstalujesz LND na Umbrel, a następnie wdrożysz elementy, które zapobiegają najbardziej kosztownym błędom: realistyczną strategię tworzenia kopii zapasowych i ochronę przed oszustwami za pomocą wieży strażniczej. Gdy te podstawy zostaną wdrożone, otworzysz swój pierwszy kanał, dzięki czemu będziesz mógł zacząć płacić na Lightning z własną infrastrukturą.



Jak widać, w tym kursie LNP202 będziemy konfigurować węzeł Lightning w trybie plug-and-play za pośrednictwem Umbrel, a nie klasycznego podejścia wiersza poleceń, aby był odpowiedni dla średnio zaawansowanych użytkowników. Jeśli wolisz instalację w wierszu poleceń, zalecamy skorzystanie z poniższego samouczka. W przygotowaniu są również inne, bardziej zaawansowane kursy Lightning zorientowane na wiersz poleceń.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Część 3 przeprowadzi Cię od działającego węzła do takiego, który umiesz kontrolować. Zaczniesz od określenia profilu operatora węzła Lightning (konsument, sprzedawca lub router), a następnie zapoznasz się z kompletnym pakietem oprogramowania do zarządzania, aby śledzić swoje kanały i działać czysto w topologii. Na koniec zajmiemy się bardzo ważną kwestią związaną z Lightning: jak uzyskać płynność przychodzącą, czy to za pośrednictwem rozwiązań płatnych, czy współpracujących.



Część 4 skupi się na codziennym użytkowaniu. Skonfigurujesz połączenie między węzłem a klientem mobilnym, dzięki czemu będziesz mógł płacić i odbierać po prostu ze swojego smartfona, bez rezygnacji z własnej opieki. Przyjrzymy się najpierw podejściu sieciowemu za pośrednictwem *Tailscale*, a następnie podejściu opartemu na protokole za pośrednictwem *Nostr Wallet Connect*, z ich zaletami i kompromisami. Kurs zakończy się ostatnim rozdziałem, który da ci odpowiednie nawyki, aby utrzymać samokontrolę, zarówno pod względem operacyjnym, jak i pedagogicznym.



Jeśli będziesz postępować zgodnie z tym kursem LNP202 we właściwej kolejności, pod koniec będziesz mieć kompletną konfigurację węzła Lightning, funkcjonalną do codziennego użytku, a przede wszystkim pod kontrolą.




## Zrozumienie węzłów Lightning


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Przed uruchomieniem własnego węzła, niniejszy rozdział zawiera krótki przegląd podstawowej teorii stojącej za [Lightning Network](https://planb.academy/resources/glossary/lightning-network). Rzeczywiście ważne jest zrozumienie mechanizmów z tym związanych, ponieważ umożliwi to identyfikację zagrożeń i przyjęcie dobrych praktyk w celu ich ograniczenia. Nie będę jednak wchodził tutaj w szczegóły, ponieważ nie jest to głównym celem tego kursu. Jeśli chcesz zagłębić się w ten temat, gorąco polecam zapoznanie się z kursem LNP 201 Fanisa Michalakisa, który jest punktem odniesienia w tej dziedzinie:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Co to jest węzeł Lightning?



Wróćmy do podstaw: zanim zdefiniujemy, czym jest węzeł, musimy zrozumieć, czym jest Lightning Network. Jest to protokół najwyższej warstwy, zbudowany na Bitcoin, zaprojektowany w celu umożliwienia transakcji [offchain](https://planb.academy/resources/glossary/offchain) BTC, które są szybkie (z niemal natychmiastową finalnością) i ogólnie niedrogie. "Offchain" oznacza, że transakcje przeprowadzane na Lightning nie są przeznaczone do wyświetlania na głównym [blockchainie](https://planb.academy/resources/glossary/blockchain) Bitcoin. Lightning jest również częściową odpowiedzią na rosnące wykorzystanie Bitcoin i przeciążenie [onchain](https://planb.academy/resources/glossary/onchain), które budzi obawy o [skalowalność](https://planb.academy/resources/glossary/scalability) systemu.



Aby działać, Lightning opiera się na otwieraniu [kanałów płatności](https://planb.academy/resources/glossary/payment-channel) między uczestnikami, w ramach których transakcje mogą być przeprowadzane niemal natychmiast, często przy minimalnych opłatach, bez konieczności rejestrowania ich jeden po drugim w łańcuchu bloków Bitcoin. Kanały te mogą pozostawać otwarte przez bardzo długi czas, wymagając transakcji onchain tylko wtedy, gdy są otwierane i zamykane.



[Węzeł Lightning](https://planb.academy/resources/glossary/lightning-node) jest uczestnikiem sieci Lightning, otwierającym kanały i dokonującym płatności z innymi węzłami. Mówiąc konkretnie, węzeł Lightning to oprogramowanie działające na komputerze i implementujące protokół Lightning Network. Przykłady obejmują LND, Core Lightning lub Eclair. Główną rolą tego oprogramowania jest:




- połączyć się z [węzłem Bitcoin](https://planb.academy/resources/glossary/full-node), aby uzyskać informacje z głównego łańcucha bloków;
- tworzyć i zarządzać dwukierunkowymi kanałami płatności z innymi węzłami;
- wymieniać wiadomości z całą siecią Lightning.



![Image](assets/fr/001.webp)



### Node vs. Lightning Wallet: ważne rozróżnienie



Na Bitcoin (onchain), "*[wallet](https://planb.academy/resources/glossary/wallet)*" odnosi się do oprogramowania, które zarządza [kluczami prywatnymi](https://planb.academy/resources/glossary/private-key), oblicza saldo z [UTXO](https://planb.academy/resources/glossary/utxo) i tworzy transakcje. Ten wallet może być oparty na własnym węźle Bitcoin lub na węźle kogoś innego, ale obecnie rola węzła i rola wallet onchain są wyraźnie różne.



Na Lightning trudniej jest ponownie użyć tego rodzaju słownictwa bez wprowadzania zamieszania. Termin "*Lightning wallet*" jest raczej niejasny, ponieważ w rzeczywistości nie ma czegoś takiego jak prawdziwie samowystarczalny Lightning wallet, chyba że jest on oparty na węźle. Możliwe są zatem tylko dwie sytuacje:



- Aby mieć prawdziwy węzeł Lightning (tj. bez nadzoru): oprogramowanie, którego używasz (np. aplikacja mobilna, taka jak Phoenix lub instancja LND na Umbrel) faktycznie uruchamia węzeł, a ty faktycznie posiadasz klucze do pobierania bitcoinów. W tym przypadku "*Lightning wallet*" jest tak naprawdę tylko interfejsem użytkownika na węźle Lightning, wbudowanym lub zdalnym.



- Aby skorzystać z usługi powierniczej: używasz aplikacji, która pokazuje saldo w [sats](https://planb.academy/resources/glossary/satoshi-sat) na Lightning, ale w tle środki znajdują się w węźle dostawcy (np. Wallet of Satoshi). Nie masz ani kluczy, ani kontroli nad kanałami. Twoje saldo jest jedynie wpisem księgowym w bazie danych firmy. Można to porównać do pozostawienia bitcoinów na platformie wymiany, ze wszystkimi związanymi z tym zagrożeniami. W tym przypadku "*Lightning wallet*" jest jedynie dostępem do konta zarządzanego przez operatora, który z kolei obsługuje prawdziwy węzeł Lightning.



Tak więc w Lightning nie ma nic pomiędzy: albo masz węzeł (nawet wbudowany), więc jesteś pod własną opieką, albo nie, więc firma jest właścicielem twojego sats. Ale jak zobaczymy w kolejnych rozdziałach, te dwa zastosowania mogą być czasami trudne do rozróżnienia. Na przykład Phoenix to aplikacja mobilna, która osadza prawdziwy węzeł Lightning, ale użytkownik niekoniecznie jest tego świadomy, ponieważ pełna złożoność jego działania jest prawie całkowicie ukryta.



### Przypomnienie, jak działa Lightning Network



W tej sekcji krótko przypomnę, jak działa Lightning. Ponownie, jeśli chcesz uzyskać bardziej dogłębną prezentację koncepcji teoretycznych, zapraszam do zapoznania się z dedykowanym kursem LNP 201.



#### Kanały płatności: otwieranie, aktualizacja i zamykanie



Sercem sieci Lightning są dwukierunkowe kanały płatności. Kanał można otworzyć (tj. utworzyć), zaktualizować w miarę przeprowadzania transakcji Lightning, a następnie ostatecznie zamknąć. Z punktu widzenia onchain, kanał to nic innego jak [wielopodpisowe](https://planb.academy/resources/glossary/multisig) [wyjście](https://planb.academy/resources/glossary/output) 2/2.



![Image](assets/fr/002.webp)



Z punktu widzenia Lightning jest to kanał płatności z [płynnością](https://planb.academy/resources/glossary/liquidity-lightning) podzieloną między dwóch uczestników.



![Image](assets/fr/003.webp)





- Otwieranie kanału:**



Dwa węzły decydują się otworzyć kanał. Jeden z nich przekazuje bitcoiny w transakcji onchain o nazwie *funding transaction*. Transakcja ta tworzy wyjście oparte na [skrypcie](https://planb.academy/resources/glossary/script) wielopodpisowym 2 na 2, co oznacza, że wydanie tych środków na Bitcoin wymaga [podpisu](https://planb.academy/resources/glossary/digital-signature) obu węzłów w kanale. Przed wydaniem tej transakcji, strona dostarczająca środki prosi drugą o podpisanie *withdrawal transaction*, która nie jest wydawana onchain, ale która umożliwia jej odzyskanie środków w przypadku wystąpienia problemu.



![Image](assets/fr/004.webp)





- Transakcje Commitment:**



Stan kanału (tj. dystrybucja sats między A i B) jest reprezentowany przez *[commitment transaction](https://planb.academy/resources/glossary/commitment-transaction)*, znany obu węzłom, ale nie jest natychmiast transmitowany w łańcuchu bloków. Ta transakcja opisuje sposób redystrybucji funduszy kanału w łańcuchu bloków zgodnie z płatnościami dokonanymi na Lightning.



Przy każdej płatności Lightning dwa węzły podpisują nowy stan, który zastępuje poprzedni. Stary stan jest unieważniany dzięki mechanizmowi klucza unieważniającego: jeśli jeden z uczestników spróbuje rozgłosić stary stan, drugi może odzyskać pełną kwotę środków jako karę.



Ważną ideą jest to, że zawsze istnieje podpisana transakcja Bitcoin, nie transmitowana w łańcuchu, przechowywana przez węzły i umożliwiająca redystrybucję sats zgodnie z płatnościami dokonanymi na Lightning Network.



![Image](assets/fr/005.webp)





- Zamknięcie kanału:**



Kanał można zamknąć w sposób czysty poprzez zamknięcie kooperacyjne, gdy obie strony zgadzają się co do ostatecznego stanu kanału, lub jednostronnie (zamknięcie wymuszone), jeśli jeden z uczestników przestanie współpracować lub stanie się nieosiągalny. We wszystkich przypadkach zamknięcie przybiera formę transakcji onchain, która wydaje wynik 2/2 i rozdziela środki między uczestników zgodnie z ostatnim ważnym stanem kanału.



![Image](assets/fr/006.webp)



Lightning działa zatem jako warstwa drugorzędna zakotwiczona na Bitcoin: tylko niektóre zdarzenia (otwieranie i zamykanie kanałów) pojawiają się w głównym łańcuchu bloków. Płatności pośrednie pozostają poza łańcuchem.



Zanim przejdziemy dalej, oto dwie podstawowe koncepcje pozwalające zrozumieć, jak zarządzać kanałem Lightning:




- Liquidity*: ilość sats dostępna po jednej stronie kanału;
- [Pojemność](https://planb.academy/resources/glossary/lightning-channel-capacity) *: jest to całkowita kwota zablokowana w wyjściu multisig 2/2, tj. suma płynności po obu stronach kanału.



#### Sieć kanałów i płynność



Kanał nie służy tylko do płatności między dwoma węzłami: jest częścią globalnej sieci połączonych kanałów. Twój węzeł może kierować płatności dla innych użytkowników za pośrednictwem własnych kanałów, a Ty możesz wysłać sats do węzła Lightning, z którym nie masz bezpośredniego kanału, o ile można znaleźć prawidłową ścieżkę między dwoma węzłami.



Każdy węzeł zna, za pośrednictwem [protokołu plotek](https://planb.academy/resources/glossary/gossip), mapę tej sieci: które kanały istnieją, które węzły są połączone kanałem dwukierunkowym i które przepustowości są publikowane. Aby wysłać płatność do odbiorcy bez bezpośredniego kanału, węzeł użytkownika oblicza trasę składającą się z kilku przeskoków: węzeł użytkownika → węzeł X → węzeł Y → węzeł odbiorcy. W każdym przeskoku płatność przechodzi przez kanał, który musi mieć wystarczającą płynność w kierunku płatności.



![Image](assets/fr/007.webp)



Płynność kanału nie jest zatem symetryczna: jedna strona może być mocno obciążona, podczas gdy druga jest prawie pusta. Zarządzanie tą płynnością, tj. wiedza o tym, gdzie znajdują się sats i w którym kierunku mogą płynąć, jest jednym z najważniejszych aspektów obsługi węzła Lightning. Przyjrzymy się temu bardziej szczegółowo w kolejnych rozdziałach praktycznych.



#### HTLC: transport płatności bez bycia okradzionym



Aby umożliwić płatnościom przechodzenie przez węzły pośrednie bez potrzeby zaufania, Lightning wykorzystuje [inteligentne kontrakty](https://planb.academy/resources/glossary/smart-contract) o nazwie *[HTLC](https://planb.academy/resources/glossary/htlc)* (*Hashed Time-Locked Contracts*). Mówiąc prościej, HTLC uzależnia transfer środków od ujawnienia sekretu i zawiera ograniczenie czasowe w celu ochrony nadawcy w przypadku niepowodzenia transakcji. Każda płatność jest zatem uzależniona od przedstawienia obrazu wstępnego (sekretu, którego [hash](https://planb.academy/resources/glossary/hash-function) odpowiada uzgodnionej wartości). Jeśli odbiorca końcowy dostarczy ten obraz wstępny, może zażądać środków, co z kolei umożliwia każdemu węzłowi pośredniczącemu odzyskanie własnych środków.



![Image](assets/fr/008.webp)



Oszczędzę ci szczegółów technicznych dotyczących działania HTLC, ponieważ nie są one istotne dla celów tego kursu. Szczegółowe wyjaśnienie znajdziesz w kursie teoretycznym LNP 201. Pamiętaj tylko, że HTLC umożliwiają wymianę atomową: albo transfer jest zakończony i nikt nie jest poszkodowany w routingu, albo kończy się niepowodzeniem i każdy uczestnik odzyskuje swoje początkowe środki. Nie ma nic pomiędzy.



### Główne implementacje węzłów Lightning



Podobnie jak w przypadku Bitcoin, istnieje kilka implementacji protokołu Lightning. Wiele niezależnych zespołów opracowuje własne wersje, z których wszystkie są interoperacyjne, ponieważ są zgodne z tymi samymi specyfikacjami ([BOLT](https://planb.academy/resources/glossary/bolt)). Oto główne implementacje używane obecnie.



#### LND (*Lightning Network Daemon*)



LND to kompletna implementacja protokołu Lightning, napisana w języku Go i opracowana przez Lightning Labs.



![Image](assets/fr/009.webp)



#### Core Lightning (*CLN*)



Core Lightning (wcześniej *C-Lightning*) to implementacja opracowana przez Blockstream. Jest napisana w języku C, z niektórymi komponentami w Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair to implementacja napisana w języku Scala i opracowana przez francuską firmę ACINQ. ACINQ obsługuje jeden z najważniejszych węzłów routingu w sieci Lightning za pomocą Eclair i wykorzystuje tę implementację jako podstawę oprogramowania dla własnych produktów, takich jak aplikacja Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) to zestaw deweloperski Rust, utrzymywany przez Spiral (Block, ex-Square). Nie jest to gotowy do użycia daemon, jak LND lub CLN, ale biblioteka dla programistów chcących zintegrować Lightning bezpośrednio ze swoimi aplikacjami.



![Image](assets/fr/012.webp)



W tym kursie LNP202 skupimy się głównie na LND: implementacji, która jest najczęściej używana w rozwiązaniach "pod klucz" dla klientów prywatnych, takich jak Umbrel.



To tyle, jeśli chodzi o to krótkie przypomnienie, jak działa Lightning. Jeszcze raz powtórzę, że jeśli jakieś koncepcje nie są dla ciebie zrozumiałe lub jeśli chciałbyś zagłębić się w nie przed zastosowaniem ich w praktyce, kurs Fanisa Michalakisa jest niezbędnym źródłem informacji na ten temat:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Dlaczego warto uruchomić własny węzeł Lightning?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Odpowiedź na to pytanie jest dość prosta, ponieważ jest retoryczna: bez własnego węzła nie korzystasz już tak naprawdę z Lightning, a jedynie z iluzji Lightning w infrastrukturze firmy.



Korzystanie z Lightning custodial wallet oznacza, że bitcoiny technicznie należą do firmy obsługującej węzeł. Użytkownik nie posiada kluczy prywatnych i nie kontroluje kanałów. Saldo wallet to tylko wiersz w bazie danych usługodawcy. Sytuacja ta jest z pewnością bardzo wygodna dla początkujących, a doświadczenie użytkownika jest często płynne, ale zasadnicze pytanie brzmi: jaka jest korzyść z używania Bitcoin i Lightning, jeśli ostatecznie rezygnujesz z aspektów, które odróżniają je od tradycyjnych walut i banków?



Dwie główne wartości Bitcoin to suwerenność monetarna (brak zależności od organu centralnego w zakresie emisji i przechowywania) oraz odporność na cenzurę (brak możliwości uniemożliwienia lub filtrowania płatności przez stronę trzecią). System powierniczy na Lightning jest sprzeczny z oboma tymi celami: nie można sprawdzić wewnętrznej podaży pieniądza platformy, a z definicji operator, który posiada wszystkie fundusze i wszystkie kanały, może cenzurować, opóźniać, ustalać priorytety lub blokować płatności. W tych warunkach możemy zasadnie zadać sobie pytanie, **jaki jest sens używania bitcoina za pośrednictwem Lightning, jeśli będzie on odtwarzał te same wzorce zaufania i zależności, co w przypadku tradycyjnych państwowych systemów walutowych**.



> Potrzebny jest elektroniczny system płatności oparty na dowodzie kryptograficznym zamiast na zaufaniu, umożliwiający dwóm chętnym stronom dokonywanie transakcji bezpośrednio ze sobą, bez potrzeby korzystania z zaufanej strony trzeciej.
*Biała księga Satoshi Nakamoto, Bitcoin


Pomijając filozofię, bardziej konkretne wady są następujące. Po pierwsze, nie masz możliwości zweryfikowania, czy firma faktycznie posiada bitcoiny odpowiadające wyświetlanym saldom. Może ona działać w oparciu o rezerwę cząstkową, zostać zhakowana, zbankrutować lub po prostu zniknąć. W takim przypadku jesteś tylko kolejnym wierzycielem, bez prawdziwej gwarancji, że odzyskasz swoje pieniądze.



Po drugie, firma podlega ryzyku regulacyjnemu: nakazom sądowym, zamrożeniu środków, żądaniom zablokowania użytkowników lub transakcji, wzmocnionemu nadzorowi, a nawet całkowitemu zakazowi działalności w niektórych jurysdykcjach. Każde ograniczenie, które ciąży na dostawcy usług, mechanicznie odbija się na użytkowniku.



Pod względem poufności sytuacja nie jest lepsza. Operator powierniczy widzi wszystkie przepływy: kwoty, częstotliwości, odbiorców, salda, zwyczaje związane z wydatkami. W połączeniu z informacjami dostarczanymi przez aplikację i ewentualnie analizą łańcucha Bitcoin, informacje te mogą zapewnić bardzo precyzyjny profil Twojej aktywności finansowej. Po raz kolejny jest to dalekie od celu Bitcoin, jakim jest ograniczenie monitorowania finansów.



Dobrą wiadomością jest to, że dziś obsługa własnego węzła Lightning nie jest już domeną ekspertów technicznych, jak to mogło być pod koniec 2010 roku. Dla użytkowników domowych dostępne są stosunkowo proste rozwiązania, które szczegółowo wyjaśnimy w następnym rozdziale.




## Wybór odpowiedniego rozwiązania dla danego zadania


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



W dzisiejszych czasach możliwe jest uzyskanie doświadczenia użytkownika bardzo zbliżonego do tego z Lightning custodial wallet, pozostając w samoopiece. Celem tego rozdziału jest pomoc w wyborze ścieżki najlepiej dopasowanej do profilu użytkownika.



### Opcja 1: Nie używaj Lightning bezpośrednio



Pierwszym rozwiązaniem jest po prostu nieużywanie Lightning natywnie, ale korzystanie z Bitcoin lub [Liquid](https://planb.academy/resources/glossary/liquid-network) wallet, które zawierają [atomowe swapy](https://planb.academy/resources/glossary/atomic-swap). Na przykład aplikacje Aqua lub Bull Bitcoin Wallet wykorzystują tę metodę, umożliwiając płacenie [faktur Lightning](https://planb.academy/resources/glossary/invoice-lightning) bez samodzielnej obsługi węzła Lightning, pozostając pod własną opieką.



Zasada jest prosta: Twoje środki pozostają w Bitcoin, on-chain lub Liquid, a dostęp do nich uzyskujesz za pośrednictwem wallet, w którym przechowujesz klucze w tradycyjny sposób. Po zeskanowaniu faktury Lightning, wallet inicjuje transakcję (on-chain lub Liquid) do usługi atomic swap. Usługa ta następnie zarządza płatnością Lightning za pośrednictwem własnego węzła, używając bitcoinów dostarczonych przez on-chain lub Liquid. W rezultacie nie musisz samodzielnie obsługiwać żadnych kanałów Lightning, ale nadal możesz płynnie rozliczać faktury Lightning.



![Image](assets/fr/013.webp)



Główną zaletą tego podejścia, w porównaniu z konwencjonalnym wallet Lightning, jest to, że użytkownik pozostaje w 100% w posiadaniu swoich środków przez cały czas. Bitcoiny znajdują się w łańcuchu onchain lub Liquid wallet, z własną [frazą mnemoniczną](https://planb.academy/resources/glossary/seed). Nawet podczas swapu użytkownik pozostaje w posiadaniu swoich środków, ponieważ swap jest atomowy. Opiera się na mechanizmie kryptograficznym, który zapewnia, że istnieją tylko dwa możliwe wyniki: albo swap zakończy się całkowitym sukcesem, albo nie powiedzie się i usługa nie może przywłaszczyć twoich środków.



Większość portfeli oferujących tego typu funkcjonalność opiera się na [Boltz](https://boltz.exchange/) dla technicznej części swapu.



Rozwiązanie to oferuje również interesujące korzyści w zakresie poufności, zwłaszcza w połączeniu z Liquid. Dla początkujących jest to również bardzo łatwe do skonfigurowania i zapisania: klasyczna fraza mnemoniczna, brak kanałów, brak płynności do zrównoważenia...



Z drugiej strony podejście to ma swoje ograniczenia. Po pierwsze, nie jest ono niewymierne: jesteś zależny od dostępności i dobrej woli usługi swap. Jeśli przestanie ona obsługiwać Twoje konto lub przestanie działać, nie będziesz już mógł płacić za jej pośrednictwem faktur Lightning. Do tego dochodzą niemałe opłaty: płacisz zarówno [opłaty transakcyjne](https://planb.academy/resources/glossary/transaction-fees) onchain lub Liquid, jak i prowizję za usługę swap. Ponadto, jeśli opłaty onchain gwałtownie wzrosną, korzystanie z Lightning może stać się bardzo kosztowne.



Tak więc do sporadycznego użytku jest to nadal akceptowalne, ale dla bardzo aktywnego użytkownika Lightning lepiej jest robić rzeczy dobrze z prawdziwym węzłem Lightning.



### Opcja 2: Wbudowane węzły Lightning



Druga kategoria rozwiązań opiera się na węzłach Lightning osadzonych bezpośrednio w aplikacji mobilnej. Phoenix Wallet był pionierem tego modelu i pozostaje punktem odniesienia. Obecnie inne projekty oferują porównywalne podejścia, takie jak Zeus (w trybie wbudowanym) lub BitKit.



Idea jest prosta: aplikacja faktycznie uruchamia węzeł Lightning, ale wszystkie złożone operacje są obsługiwane automatycznie w tle. Masz interfejs "*Lightning wallet*" z frazą mnemoniczną do tworzenia kopii zapasowych, widzisz saldo i płacisz faktury, ale nie zarządzasz kanałami, płynnością ani większością parametrów.



![Image](assets/fr/014.webp)



Rozwiązania te są zawsze samoobsługowe. Klucze kontrolujące środki są generated i przechowywane w telefonie, a kopia zapasowa jest wykonywana za pomocą seed lub równoważnego mechanizmu. Nie jesteś po prostu posiadaczem konta u usługodawcy, ale właścicielem bitcoinów zablokowanych w kanałach, które należą do Ciebie i nie mogą zostać skradzione.



Zalety węzłów pokładowych LN są liczne:




- niezwykle łatwa instalacja i użytkowanie;
- wrażenia użytkownika zbliżone do tych z Lightning wallet, ale z możliwością samodzielnego przechowywania;
- brak ręcznego zarządzania kanałami lub płynnością;
- stosunkowo prosta kopia zapasowa.



Jednak te wbudowane wallet mają również znaczące ograniczenia. Po pierwsze, jeśli chodzi o poufność, operator usługi (np. ACINQ w przypadku Phoenix) ma dość szczegółowy wgląd w przepływy przechodzące przez węzeł: ilości, częstotliwości, odbiorców, nawet jeśli to się poprawi, szczególnie wraz ze stopniowym wdrażaniem *Trampoline Nodes*. Po drugie, jesteś w dużym stopniu zależny od tego operatora jako głównego peera Lightning. Jeśli węzeł ACINQ stanie się niedostępny (w przypadku Phoenix), jeśli firma znajdzie się pod presją regulacyjną lub zmieni swój model biznesowy, doświadczenie użytkownika może zostać poważnie pogorszone, a nawet zagrożone.



Wreszcie, ta prostota ma swoją cenę. Wbudowane usługi węzła LN zazwyczaj pobierają określone opłaty za wpłaty, wypłaty lub niektóre operacje zarządzania kanałami. Moim zdaniem model ten ma sens pod względem oferowanych usług, ale w przypadku intensywnego użytkowania może być znacznie droższy niż dobrze zarządzany konwencjonalny węzeł Lightning.



### Opcja 3: klasyczny węzeł Lightning



Trzecim rozwiązaniem, któremu przyjrzymy się dokładniej w tym kursie LNP202, jest obsługa konwencjonalnego węzła Lightning na dedykowanym serwerze lub urządzeniu.



Przez "klasyczny" rozumiem, że użytkownik samodzielnie instaluje i konfiguruje implementację Lightning (np. LND) na własnym węźle Bitcoin. Wybierasz swoich peerów, otwierasz kanały, zarządzasz [płynnością przychodzącą i wychodzącą](https://planb.academy/resources/glossary/inbound-capacity) oraz ustawiasz zasady opłat za routing.



Pod względem suwerenności jest to najlepsze rozwiązanie. Nie jesteś już zależny od konkretnej firmy w zakresie swoich kanałów lub płatności: jeśli peer cię ocenzuruje lub zamknie kanał, możesz otworzyć inny z innym węzłem. Jeśli usługa zniknie, twoje sats pozostaną w kanałach, które kontrolujesz, i możesz je repatriować w łańcuchu. Możesz także zoptymalizować swoje długoterminowe koszty: gdy twoje kanały są prawidłowo dobrane i zarządzane, ogólny koszt płatności może stać się bardzo niski.



Pod względem poufności podlegasz oczywiście ograniczeniom modelu Lightning, ale nie przekazujesz całej swojej działalności jednemu operatorowi.



W przeciwieństwie do tego, konfiguracja klasycznego węzła Lightning jest oczywiście bardziej złożona: musisz zainstalować, skonfigurować, utrzymywać, monitorować aktualizacje, zrozumieć logikę kanałów i polityk opłat, zarządzać kanałami i przepływem gotówki itd. Błędna konfiguracja, niechlujne tworzenie kopii zapasowych lub nieostrożne zarządzanie mogą łatwiej doprowadzić do utraty sats. Węzeł musi również działać w sposób ciągły.



To jest właśnie ścieżka, którą proponuję podążać w tym kursie, towarzysząc ci na każdym kroku, aby ograniczyć ryzyko i ustrukturyzować swoje podejście.



### Które rozwiązanie dla którego profilu użytkownika?



Aby wybrać odpowiednie rozwiązanie dla profilu użytkownika Lightning, należy wziąć pod uwagę dwa czynniki: częstotliwość korzystania z Lightning i apetyt na zarządzanie techniczne.



Jeśli nie dokonujesz wielu płatności Lightning od czasu do czasu, ale nadal chcesz mieć możliwość rozliczania faktur LN z telefonu od czasu do czasu, bez rezygnacji z samodzielnego przechowywania: Bitcoin lub Liquid wallet z funkcją wymiany jest prawdopodobnie najlepszą opcją. Zachowujesz własność swoich środków, nie zarządzasz węzłami i akceptujesz nieco wyższe opłaty w zamian za prostotę.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Jeśli korzystasz z Lightning dość regularnie i chcesz korzystać z zalet prawdziwego węzła, ale nie chcesz poświęcać czasu na zarządzanie kanałami, opłatami lub infrastrukturą, mobilny wbudowany węzeł Lightning jest dobrym rozwiązaniem. Zachowujesz kontrolę nad swoimi środkami, UX pozostaje bardzo przystępny, a cała złożoność jest ukryta, za cenę wyraźnej zależności od operatora.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Jeśli jesteś średnio zaawansowanym lub zaawansowanym użytkownikiem, chcesz zainwestować czas w zrozumienie i zarządzanie swoją infrastrukturą oraz chcesz mieć maksymalną kontrolę nad swoimi kanałami, płynnością i kosztami: klasyczny węzeł Lightning oparty na serwerze jest najlepszym rozwiązaniem. Jest to najbardziej wymagające rozwiązanie, ale także najbardziej zgodne z ideą suwerenności Bitcoin.




# Tworzenie pierwszego węzła Lightning


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Instalacja LND z Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Teraz, gdy zapoznaliśmy się z podstawami Lightning i dostępnymi rozwiązaniami, nadszedł czas, aby przejść do rzeczy. Aby wziąć udział w tym kursie, potrzebujesz węzła Bitcoin zsynchronizowanego z Umbrel. Ten kurs szkoleniowy LNP202 jest kontynuacją BTC 202; jeśli nie masz jeszcze węzła Bitcoin, zapraszam do wzięcia udziału w tym innym kursie szkoleniowym przed powrotem tutaj, gdy węzeł zostanie zsynchronizowany. Zdecydowanie zalecam zapoznanie się z nim, ponieważ nie będę wchodził w szczegóły dotyczące jego działania, konfiguracji i środków bezpieczeństwa.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

W tym pierwszym rozdziale przyjrzymy się, jak zainstalować LND na Umbrel. Sposób działania Umbrel sprawia, że ten krok jest bardzo prosty, ponieważ wszystko, co musisz zrobić, to zainstalować aplikację.



Ze strony głównej otwórz `App Store` w dolnej części interfejsu.



![Image](assets/fr/015.webp)



W pasku wyszukiwania wpisz `Lightning Node`, a następnie kliknij aplikację.



![Image](assets/fr/016.webp)



Następnie kliknij przycisk `Install`, aby rozpocząć instalację.



![Image](assets/fr/017.webp)



Na stronie głównej kliknij aplikację, aby ją otworzyć, a następnie wybierz `Setup a new node`.



![Image](assets/fr/018.webp)



Otrzymujesz 24-wyrazową frazę mnemotechniczną. Przechowuj ją w bezpiecznym miejscu. W następnym rozdziale przyjrzymy się bardziej szczegółowo, jak odzyskać dostęp do węzła Lightning (jest to znacznie bardziej złożony proces niż w przypadku prostego Bitcoin wallet), ale na razie pamiętaj, że ta fraza odgrywa kluczową rolę i należy ją zachować z najwyższą starannością.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Zapisz tę frazę w taki sam sposób, jak konwencjonalną frazę mnemoniczną: na fizycznym nośniku (papier lub metal) przechowywanym w bezpiecznym miejscu, a następnie kliknij przycisk `NEXT`.



![Image](assets/fr/019.webp)



Następnie wprowadź słowa zdania, aby sprawdzić, czy zapisałeś je poprawnie.



![Image](assets/fr/020.webp)



Komunikat ostrzegawczy przypomni, że aplikacja jest w wersji beta, a Lightning Network pozostaje technologią eksperymentalną. Oczywiście nigdy nie zapisuj w węźle Lightning kwot, których nie jesteś gotów stracić.



Następnie przejdziesz do głównego interfejsu węzła Lightning. Po lewej stronie znajduje się Bitcoin onchain wallet hostowany na węźle. Jest to generated z 24-wyrazowej frazy, którą właśnie zapisałeś.



Pośrodku znajdziesz swój Lightning wallet. W rzeczywistości reprezentuje on [wychodzącą gotówkę](https://planb.academy/resources/glossary/outbound-capacity), tj. bitcoiny, które posiadasz w swoich kanałach Lightning.



Po prawej stronie zobaczysz kilka ważnych informacji o swoim węźle:




- Liczba połączeń i otwartych kanałów;
- Całkowity wychodzący przepływ gotówki, czyli to, co teoretycznie możesz wydać na Lightning;
- Całkowita przychodząca płynność, tj. to, co teoretycznie możesz otrzymać na Lightning.



![Image](assets/fr/021.webp)



Zacznijmy od dostosowania naszego węzła. Kliknij na trzy małe kropki w prawym górnym rogu interfejsu, a następnie na `Ustawienia zaawansowane`. W podmenu `Personalizacja` możesz zdefiniować publiczną nazwę dla swojego węzła (unikaj używania prawdziwego imienia i nazwiska) i wybrać jego kolor.



![Image](assets/fr/046.webp)



Następnie kliknij zielony przycisk `ZAPISZ I URUCHOM PONOWNIE`, aby ponownie uruchomić węzeł i zastosować wprowadzone zmiany.



Węzeł Lightning jest teraz gotowy do otwarcia pierwszych kanałów płatności. Ale najpierw przyjrzyjmy się, jak chronić sats!



## Zapisywanie węzła Lightning


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Przed wysłaniem pierwszego sats do węzła ważne jest, aby zrozumieć, jak działa jego kopia zapasowa i jakie są związane z tym zagrożenia. W przeciwieństwie do prostego portfela Bitcoin onchain, tworzenie kopii zapasowej węzła Lightning jest dość złożone: niewłaściwa strategia może doprowadzić do trwałej utraty środków. W tym rozdziale przyjrzymy się temu, co tak naprawdę należy zarchiwizować i jak Umbrel obsługuje ten proces za pomocą LND.



W tym kursie będziemy używać implementacji LND (*Lightning Network Daemon*). Chociaż zasady są podobne w innych implementacjach, pliki odzyskiwania i procedury, o których będę mówić, są specyficzne dla LND.



### Co powinienem zaoszczędzić na węźle Lightning?



Na węźle Lightning nie wystarczy zapisać seed i mieć nadzieję, że wszystko wróci do normy. Kilka elementów odgrywa różne role, więc ważne jest, aby je rozróżnić.



#### seed (*aezeed*)



Po zainicjowaniu LND otrzymuje się 24-słowny seed. Jest to specyficzny dla LND format o nazwie "*aezeed*". Nie jest to klasyczny seed BIP39, choć bardzo go przypomina. Z tego seed, LND wyprowadza klucze prywatne twojego onchain wallet powiązanego z węzłem Lightning, tj. adresy, na które możesz odbierać lub na które możesz repatriować bitcoiny po zamknięciu kanału.



![Image](assets/fr/019.webp)



Ten seed może być zatem użyty do odtworzenia wallet onchain powiązanego z danym węzłem oraz do odzyskania środków, które zostały już repatriowane onchain (np. po zamknięciu kanału). Z drugiej strony, sam seed nie jest wystarczający do przywrócenia kanałów Lightning, które są nadal otwarte, ponieważ nie zawiera niezbędnych informacji o statusie kanałów.



#### Baza danych kanałów (`channel.db`)



LND przechowuje szczegółowy status kanałów w bazie danych o nazwie `channel.db`. Ta baza danych zawiera:




- lista otwartych kanałów;
- rówieśników i ich identyfikatorów;
- ostatnie commitment transaction dla każdego kanału (kolejne stany, które określają, kto jest właścicielem czego w kanale i umożliwiają odzyskanie środków onchain w przypadku problemu);
- informacje potrzebne do ukarania użytkownika, który próbuje wysłać stary raport.



Problem z tą bazą danych polega na tym, że ciągle się ona zmienia: każda płatność, każdy routing, każde otwarcie lub zamknięcie kanału modyfikuje jej zawartość. Dlatego konwencjonalna kopia zapasowa (np. okresowa kopia pliku `channel.db`) jest niebezpieczna. Jeśli przywrócisz zbyt starą wersję `channel.db` i ponownie złożysz węzeł z tym przestarzałym stanem, twoi rówieśnicy mogą uznać, że nadajesz stary stan kanału. W takim przypadku protokół przewiduje karę: twój peer może odzyskać pełną kwotę funduszy kanału, tak jakbyś próbował oszukiwać.



W praktyce, `channel.db` nie jest nośnikiem kopii zapasowej jako takim. Jest to żywy stan węzła. Jedyną sytuacją, w której sensowne jest użycie go do przywrócenia węzła, jest odzyskanie tej bazy danych bezpośrednio z maszyny, która właśnie uległa awarii (np. dysk, który jest nadal czytelny). W takim przypadku odzyskuje się najnowszy stan i można ponownie uruchomić LND na innej maszynie w oparciu o tę bazę danych, wiedząc, że stan ten jest tak aktualny, jak to tylko możliwe, ponieważ stara maszyna już nie działa. Inną sytuacją, w której ta metoda może służyć jako odpowiednia kopia zapasowa, jest konfiguracja z dwoma dyskami, z dynamiczną, trwałą kopią z jednego na drugi. Ten typ konfiguracji jest jednak bardziej złożony w implementacji.



Jednak wykonywanie okresowych kopii `channel.db` i przechowywanie ich jako kopii zapasowych do późniejszego przywrócenia jest bardzo złym pomysłem: w dniu, w którym ich użyjesz, ryzykujesz ukaranie siebie i utratę całego sats.



#### Statyczna kopia zapasowa kanału (SCB)



Aby umożliwić odzyskiwanie danych po awarii, LND wprowadził mechanizm *Static Channel Backup* (SCB). Jest to specjalny plik, często nazywany `channel.backup`, który zawiera statyczne informacje o twoich kanałach: kim są twoi rówieśnicy, jak się z nimi skontaktować i jakie są twoje kanały.



Plik ten nie zawiera szczegółowego stanu kanału ani historii aktualizacji. Nie pozwala na ponowne otwarcie kanałów w dokładnym stanie, w jakim się znajdowały, ani na kontynuowanie działania tego węzła Lightning. Jego rolą jest raczej działanie jako punkt zaczepienia, aby poprosić rówieśników o pomoc w czystym zamknięciu wszystkich kanałów, a tym samym otrzymaniu sats onchain, na kluczach, które można odzyskać dzięki seed. Tak więc, w przeciwieństwie do pliku `channel.db`, który jest modyfikowany przy każdej płatności lub routingu, plik SCB jest aktualizowany tylko wtedy, gdy kanał jest otwierany lub zamykany.



W przypadku odzyskiwania za pośrednictwem SCB proces wygląda następująco:




- Przywracasz swój seed (*aezeed*), który odtwarza twój onchain wallet powiązany z węzłem Lightning;
- Użytkownik przekazuje LND najnowszy SCB;
- LND używa SCB do znalezienia listy użytkowników i kanałów, które z nimi posiadasz;
- Kontaktuje się z każdym peerem, informuje go o utracie danych i prosi o "wymuszenie zamknięcia" kanału z nim, aby można było odzyskać udział onchain.



Pomysł polega na tym, że twoi rówieśnicy, zauważając, że zgłaszasz utratę danych, wyemitują swój ostatni commitment transaction i zamkną kanał siłowy. Po potwierdzeniu tych transakcji środki ponownie pojawią się w portfelu onchain (powiązanym z seed).



Ten mechanizm odzyskiwania nie jest jednak doskonały. Po pierwsze, w rzeczywistości nie przywraca węzła Lightning, ponieważ wszystkie kanały zostaną zamknięte. Będziesz wtedy musiał zbudować nowy węzeł Lightning od podstaw. Po drugie, nie gwarantuje 100% odzyskania środków, choć znacznie zwiększa szanse na odzyskanie sald onchain w przypadku wystąpienia problemu. Protokół odzyskiwania środków zależy bowiem od współpracy i dostępności węzłów równorzędnych: jeśli jeden z nich jest offline, utracił własne dane lub odmawia współpracy, środki mogą pozostać zablokowane, a nawet zostać trwale utracone. Dlatego ważne jest, aby nie utrzymywać otwartych kanałów na węźle Lightning z nieosiągalnymi peerami przez długi czas. Jeśli w tym momencie dojdzie do utraty danych, a peer pozostanie nieosiągalny, odzyskanie środków za pośrednictwem SCB będzie niemożliwe, a środki pozostaną utracone, dopóki peer nie powróci do trybu online (być może na zawsze).



Podsumowując, dobra strategia tworzenia kopii zapasowych Lightning na LND opiera się na trzech filarach:




- seed (*aezeed*), dla warstwy onchain;
- Niezawodna automatyczna kopia zapasowa SCB;
- Dobre zarządzanie kanałami poprzez wybieranie wiarygodnych partnerów i zapobiegawcze zamykanie tych, którzy często są nieosiągalni.



### W jaki sposób Umbrel zarządza kopią zapasową węzła LND?



Umbrel oferuje uproszczony mechanizm tworzenia kopii zapasowych dla węzła LND, oparty właśnie na SCB. Pomysł polega na tym, aby zaoszczędzić użytkownikowi kłopotów z samodzielnym manipulowaniem tym plikiem, tworząc jego kopię zapasową i automatyzując proces w jak największym stopniu.



Po utworzeniu węzła na Umbrel otrzymasz seed, który pełni podwójną rolę:




- wyprowadza Bitcoin z łańcucha wallet powiązanego z węzłem Lightning;
- służy do uzyskania identyfikatora kopii zapasowej i klucza szyfrowania używanego do zdalnych kopii zapasowych SCB.



Dzięki temu mechanizmowi Umbrel automatycznie tworzy zaszyfrowaną kopię zapasową SCB i przechowuje ją na swoich serwerach za pośrednictwem sieci Tor. SCB jest przechowywany w postaci zaszyfrowanej, dzięki kluczowi pochodzącemu z seed. Tak więc, w przypadku utraty danych, wystarczy odtworzyć węzeł Bitcoin i Lightning na Umbrel, na tej samej lub innej maszynie, a następnie wprowadzić seed. Będziesz wtedy mógł pobrać najnowszy status SCB z serwerów Umbrel, odszyfrować go i rozpocząć proces odzyskiwania środków.



Te kopie zapasowe są lokalnie szyfrowane przez węzeł przed wysłaniem, co gwarantuje poufność danych: Umbrel nie może odczytać zawartości SCB. Transmisja odbywa się za pośrednictwem sieci Tor, co zapobiega wyciekowi adresu IP użytkownika. Co więcej, Umbrel dodaje szum do ruchu (losowe wypełnianie i fałszywe kopie zapasowe wysyłane w nieregularnych odstępach czasu), aby uniemożliwić serwerowi dokładne ustalenie, kiedy otwierasz lub zamykasz kanał.



Główną zaletą tej metody jest to, że znacznie upraszcza tworzenie kopii zapasowej węzła Lightning: wystarczy wykonać kopię zapasową seed tylko raz podczas inicjalizacji węzła. Wiąże się to z pewnym ryzykiem, ponieważ jest to tylko kopia zapasowa SCB, ale dla rozsądnych kwot jest to akceptowalny kompromis.



### Najlepsze praktyki ograniczające ryzyko strat



Nawet z kopią zapasową Umbrel, kilka prostych dobrych praktyk może znacznie zmniejszyć ryzyko utraty sats:





- Monitoruj dostępność swoich rówieśników:



Jeśli ważny kanał jest często powiązany z nieosiągalnym lub niestabilnym peerem, bezpieczniej jest go zamknąć, gdy węzeł nadal działa. Prewencyjna współpraca lub wymuszone zamknięcie eliminuje potencjalne źródło problemów w przypadku odzyskiwania SCB.





- Unikaj koncentrowania zbyt dużej płynności na nieznanych graczach:



Im większy kanał peer ma z tobą, tym ważniejsze jest, aby był niezawodny. Wybierz poważne, dobrze połączone i aktywne węzły, aby przyszłe odzyskiwanie za pośrednictwem SCB mogło przebiegać płynnie.





- Uzupełnienie Umbrel o lokalne kopie zapasowe:



Oprócz automatycznej kopii zapasowej Umbrel, można również przechowywać zaszyfrowaną kopię pliku SCB (`channel.backup`) na nośniku zewnętrznym i okresowo ją aktualizować. Najlepiej byłoby odnawiać go za każdym razem, gdy otwierasz lub zamykasz kanał. Daje to rozwiązanie zapasowe, jeśli z jakiegokolwiek powodu usługa automatycznego tworzenia kopii zapasowych Umbrel stanie się niedostępna.





- Zarządzanie seed we właściwy sposób



Twój seed Umbrel nie tylko przywraca twój onchain wallet, ale także uzyskuje klucz szyfrowania dla kopii zapasowych. Atakujący mający do niego dostęp może zatem uruchomić odzyskiwanie i przenieść środki do własnego wallet, nie mając nawet fizycznego dostępu do węzła.



Tak więc, jeśli musisz przywrócić węzeł, ale nie masz już seed, nie będziesz w stanie niczego odzyskać: wszystkie sats zostaną utracone. Dlatego bardzo ważne jest, aby zachować seed z najwyższą starannością, tylko na nośniku fizycznym (papierowym lub metalowym) i przechowywać go w bezpiecznym miejscu. Więcej informacji na temat zarządzania seed można znaleźć w tym samouczku:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Jak zapisać węzeł Lightning na Umbrel?



Teraz, gdy już zrozumiałeś, jak działa teoria, przejdźmy do szczegółów. W aplikacji Lightning Node (która w rzeczywistości jest LND) kliknij trzy małe kropki w prawym górnym rogu.



![Image](assets/fr/022.webp)



Istnieją trzy elementy interesujące z punktu widzenia kopii zapasowej:




- Sprawdź, czy opcja `Automatyczne kopie zapasowe` jest włączona. Spowoduje to automatyczne wysłanie zaszyfrowanego SCB na serwery Umbrel.
- Następnie możesz wybrać, czy chcesz wysyłać przez Tor, czy przez Clearnet, używając opcji `Backup over Tor`. Jak wyjaśniono w poprzednich sekcjach, zdecydowanie zalecam korzystanie z sieci Tor w celu zachowania poufności.
- Na końcu znajduje się przycisk "Pobierz plik kopii zapasowej kanału", który umożliwia pobranie pliku "channel.backup", tj. zaszyfrowanej migawki SCB, na komputer. Umożliwia to od czasu do czasu tworzenie dodatkowych lokalnych kopii zapasowych, oprócz tych automatycznie wysyłanych na serwery Umbrel.



Teraz wiesz, jak chronić sats węzła Lightning przed utratą danych. W następnym rozdziale przyjrzymy się, jak zabezpieczyć węzeł przed próbami oszustwa.




## Watchtower: rola i konfiguracja


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



W Lightning każdy kanał opiera się na sekwencji kolejnych stanów, reprezentowanych przez niepublikowane commitment transaction. Z każdą płatnością lub routingiem Lightning, 2 uczestników kanału tworzy nową parę commitment transaction, odzwierciedlającą bieżącą dystrybucję środków w kanale. Stare commitment transaction stają się nieaktualne.



Jeśli jedna ze stron opublikuje nieaktualny stan, druga ma prawo ją ukarać i odzyskać pełną kwotę środków kanału. W tym rozdziale przyjrzymy się pokrótce, jak działa ten mechanizm, a następnie wyjaśnimy, jak skonfigurować ***watchtower***: system ochrony węzła Lightning przed możliwymi próbami oszustwa.



### Zrozumienie działania wież strażniczych


W dowolnym momencie każda strona w kanale ma commitment transaction, który, jeśli zostanie opublikowany, umożliwi im zamknięcie kanału i odzyskanie swojej części funduszy. Proces ten znany jest jako *wymuszone zamknięcie*. Ale jeśli spróbują opublikować starszy commitment transaction, odpowiadający poprzedniemu stanowi kanału, w którym posiadał więcej sats, wówczas transakcja ta zostanie uznana za próbę oszustwa. W takim przypadku kontrahent może użyć klucza odwołania powiązanego z tym starszym stanem, aby odzyskać pełną kwotę środków na kanale, podczas gdy oszust jest tymczasowo blokowany przez blokadę czasową.


System ten oznacza, że publikowanie starego stanu, tj. próba oszustwa, jest bardzo ryzykowna: jeśli druga strona zobaczy tę transakcję w mempool lub na blockchainie przed wygaśnięciem blokady czasowej, może użyć klucza unieważnienia i odzyskać wszystkie środki. **Dlatego bezpieczeństwo kanału Lightning zależy od zdolności do wykrycia próby oszustwa w oknie czasowym narzuconym przez blokadę czasową**.



#### Dlaczego wieże strażnicze są potrzebne?



Mechanizm karny działa tylko wtedy, gdy poszkodowany jest w stanie to zrobić:




- monitoruje każdy nowy blok Bitcoin, aby sprawdzić, czy kanał commitment transaction został opublikowany;
- określić, czy ta transakcja odpowiada ostatniemu ważnemu stanowi, czy stanowi odwołanemu;
- w przypadku unieważnienia statusu, aby nadać legalną transakcję na czas, używając klucza unieważnienia w celu odzyskania wszystkich środków przed wygaśnięciem blokady czasowej.



![Image](assets/fr/023.webp)



W idealnym scenariuszu węzeł Lightning jest online 24 godziny na dobę, 7 dni w tygodniu, jest zsynchronizowany i stale monitoruje łańcuch bloków. Z tego powodu może samodzielnie wykryć próbę oszustwa i zareagować. W praktyce jednak osobisty węzeł Lightning może się wyłączyć, szczególnie w przypadku przedłużającej się przerwy w dostawie prądu lub awarii połączenia internetowego.



To właśnie w tych okresach przestoju ryzyko staje się realne: jeśli nieuczciwy peer opublikuje stary status, gdy węzeł jest offline, a blokada czasowa skończy się bez żadnej reakcji z twojej strony, oszustwo staje się skuteczne. Tracisz część lub całość swoich środków w kanale.



Watchtower zostały wprowadzone w celu zmniejszenia tego ryzyka. Watchtower to zewnętrzna usługa, która monitoruje blockchain w imieniu użytkownika, skanując w poszukiwaniu możliwej publikacji starego statusu na jednym z jego kanałów i, jeśli to konieczne, automatycznie transmituje transakcję karną w jego imieniu. Tak więc, nawet jeśli twój węzeł Lightning pozostaje offline przez dłuższy czas, tak długo, jak strażnica, z której korzystasz, będzie w stanie chronić twoje fundusze, monitorując wszelkie próby oszustwa i stosując odpowiednią karę, gdy tylko ją wykryje.



#### Jak działa wieża strażnicza



Wieża strażnicza została zaprojektowana w taki sposób, aby zminimalizować ilość informacji uzyskiwanych o kanałach, zapewniając jednocześnie środki do działania w przypadku wystąpienia problemu:




- Dla każdego nowego stanu kanału z peerem węzeł przygotowuje z wyprzedzeniem potencjalną transakcję karną. W przypadku oszustwa peera, transakcja ta pozwoli odzyskać wszystkie środki na kanale;
- Twój węzeł następnie szyfruje tę transakcję karną przy użyciu TXID odpowiedniego commitment transaction (tego, który zostałby użyty, gdyby oszust próbował dokonać oszustwa). Dopóki nie nastąpi zamknięcie, watchtower nie może odszyfrować tej transakcji, ponieważ nie zna w pełni TXID oszukańczej transakcji;
- Twój węzeł wysyła do watchtower pakiet zawierający zaszyfrowaną transakcję kary i połowę TXID potencjalnej oszukańczej transakcji.



Ponieważ TXID przesłany do wieży strażniczej jest niekompletny, nie może ona odszyfrować transakcji wymiaru sprawiedliwości. Może jednak monitorować blockchain pod kątem TXID, który pasuje do części, której jest właścicielem. Jeśli wykryje taką transakcję, spróbuje użyć pełnego TXID tej transakcji do odszyfrowania transakcji kary. Jeśli odszyfrowanie się powiedzie, wie, że jest to próba oszustwa i natychmiast publikuje transakcję karną dla ciebie.



![Image](assets/fr/024.webp)



Wieża strażnicza nie ma zatem wglądu w szczegóły kanałów użytkownika: ani w tożsamość peerów, ani w salda, ani w strukturę transakcji. Widzi tylko zaszyfrowane pakiety. Jedyną informacją, jaką może wydedukować, jest szybkość aktualizacji kanałów, ponieważ otrzymuje pakiet dla każdego nowego stanu, ale nie jest w stanie poznać jego zawartości. W przypadku oszustwa z pewnością odkryje informacje o kanale, odszyfrowując transakcję kary, ale przynajmniej sats zostanie zapisany.



Mechanizm ten opiera się na kompromisie: delegujesz możliwość opublikowania wstępnie podpisanej transakcji karnej do watchtower, ale ta transakcja pozostaje całkowicie nieprzejrzysta dla watchtower, dopóki nie dojdzie do oszustwa. Strażnica nie może ani modyfikować odbiorców, ani przekierowywać środków, ponieważ ma tylko transakcję, która została już podpisana, z wyjściami zamrożonymi na twoją korzyść. Nie może też poznać szczegółów kanału w legalnym wymuszonym lub kooperacyjnym zamknięciu, ponieważ identyfikatory TXID nie pasują do siebie. Z drugiej strony, watchtower pozostaje minimalną zaufaną stroną trzecią: musisz polegać na tym, że będzie online i prawidłowo rozgłosi twoją transakcję sprawiedliwości, kiedy będziesz tego potrzebować.



#### Stawanie się wieżą strażniczą



Teoretycznie każdy węzeł Lightning może działać jako strażnica dla innych węzłów (jeśli używają tej samej implementacji, np. LND), będąc jednocześnie chronionym przez inne węzły odgrywające dla niego tę rolę. W poniższych sekcjach praktycznych pokażę, jak skonfigurować ten prosty mechanizm na LND pod Umbrel.


W związku z tym interesującą strategią może być uzgodnienie z zaufanymi przyjaciółmi bitcoinerów, aby działali jako strażnicy. Ty monitorujesz ich kanały, a oni monitorują twoje.



### Znajdź altruistyczną strażnicę



Jeśli nie znasz nikogo w swoim otoczeniu, kto mógłby świadczyć usługi wieży strażniczej, istnieje wiele altruistycznych publicznych wież strażniczych, do których możesz się podłączyć. Na przykład w tym kursie LNP202 sugeruję podłączenie się do usługi wieży strażniczej oferowanej wspólnie przez LN+ i Voltage, która jest wieżą strażniczą dla LND.


Tutaj znajdują się dane logowania:



- Przez Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Przez clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Aby podziękować im za dostarczanie tej bezpłatnej usługi strażniczej, [możesz przekazać darowiznę za pośrednictwem Lightning](https://lightningnetwork.plus/donation).


Teraz, gdy używamy altruistycznej usługi strażniczej, zobaczmy, jak skonfigurować ją na naszym węźle LND pod Umbrel.


### Konfigurowanie wieży strażniczej


W aplikacji `Lightning Node` kliknij trzy kropki w prawym górnym rogu interfejsu, a następnie wybierz `Ustawienia zaawansowane`.


![Image](assets/fr/025.webp)


Następnie przejdź do menu `Watchtower`.


![Image](assets/fr/026.webp)



Aktywuj opcję `Watchtower Client`, a następnie kliknij przycisk `SAVE AND RESTART NODE`. Poczekaj na ponowne uruchomienie LND.


![Image](assets/fr/027.webp)


Po zakończeniu restartu wróć do tego samego menu i wprowadź identyfikator wybranej altruistycznej wieży strażniczej w odpowiednim polu. Następnie kliknij przycisk `ADD`, aby potwierdzić. Możesz również dostosować parametr `Watchtower Client Sweep Fee Rate`: jest to stawka opłaty, którą jesteś skłonny zapłacić za ewentualną transakcję sprawiedliwości transmitowaną przez strażnicę. Nie ma potrzeby wybierania zbyt wysokiej stawki, ale należy również unikać zbyt niskiej stawki, w przeciwnym razie transakcja prawna nie zostanie potwierdzona na czas.


Uruchom ponownie węzeł za pomocą przycisku `SAVE AND RESTART NODE`, aby zastosować te zmiany.


![Image](assets/fr/028.webp)



Jeśli wrócisz do tego samego menu, zobaczysz, że węzeł Lightning jest teraz chroniony przez dodaną przed chwilą wieżę strażniczą.



![Image](assets/fr/029.webp)



Altruistyczna wieża strażnicza jest zazwyczaj wystarczająca, zwłaszcza jeśli nie umieszczasz dużych kwot pieniędzy na węźle Lightning i jeśli dobrze zarządzasz węzłem (nie pozostawiaj go wyłączonego zbyt długo). Aby zapewnić jeszcze większe bezpieczeństwo, można również dodać kilka, powtarzając ten sam proces.



## Otwórz swój pierwszy kanał Lightning


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Jeśli dotarłeś tak daleko, wiesz już, że węzeł Lightning bez kanału jest trochę jak pusty wallet: istnieje, ale jest bezużyteczny. Aby móc wysyłać lub odbierać płatności, węzeł musi być połączony z co najmniej jednym innym węzłem w sieci Lightning za pośrednictwem kanału. W przyszłości zdecydowanie zalecamy otwarcie kilku kanałów ze względu na odporność i wydajność routingu. W kolejnych rozdziałach przyjrzymy się również sposobom zarządzania płynnymi aktywami, optymalizacji topologii kanałów i korzystania z bardziej zaawansowanych narzędzi niż podstawowy interfejs LND na Umbrel.



Ale w tym rozdziale wprowadzającym celem jest po prostu zrozumienie, jak wybrać dobrego peera Lightning, gdzie znaleźć informacje potrzebne do wyboru peerów i wreszcie, jak otworzyć swój pierwszy kanał za pośrednictwem podstawowego interfejsu LND.



### Jak wybrać dobrego partnera Lightning?



Po otwarciu kanału należy wybrać węzeł równorzędny: inny węzeł Lightning, z którym węzeł będzie bezpośrednio połączony za pośrednictwem kanału. Wybór węzła równorzędnego jest ważny, ponieważ będzie miał bezpośredni wpływ na:




- łatwość, z jaką płatności trafiają do celu;
- niezawodność kanałów w czasie;
- koszty routingu.



Nie ma czegoś takiego jak idealne dopasowanie dla każdego, ale istnieje szereg wiarygodnych kryteriów identyfikacji dobrych kandydatów.



#### 1. Łączność węzła



Dobry peer to węzeł, który jest dobrze połączony z siecią Lightning. Oznacza to nie tylko posiadanie dużej liczby kanałów (choć może to być wskaźnik), ale przede wszystkim bycie połączonym z innymi niezawodnymi węzłami i zajmowanie wystarczająco centralnej pozycji w grafie sieci.



Dobrze połączony węzeł zwiększa szanse na znalezienie wydajnej trasy do większości miejsc docelowych płatności. Zmniejsza to również liczbę potrzebnych węzłów pośredniczących, co obniża koszty.



I odwrotnie, otwarcie pierwszego kanału do odizolowanego lub słabo połączonego węzła może ograniczyć twoje możliwości: będziesz w stanie zapłacić temu peerowi, ale znacznie trudniej będzie zapłacić reszcie sieci.



#### 2. Kapitalizacja i przepustowość kanału



Dobry peer jest również wystarczająco skapitalizowanym węzłem. Wskazuje na to jego całkowita pojemność kanału (suma sats zaangażowanych we wszystkie jego kanały) i jego średnia pojemność kanału (często lepiej jest mieć tylko kilka dobrze skapitalizowanych kanałów niż wiele małych).



Węzeł o niewielkiej przepustowości lub którego wszystkie kanały są małe, nie będzie w stanie kierować płatności o dużych kwotach, co spowoduje awarie routingu.



#### 3. Zasady dotyczące wydatków



Każdy węzeł ustala własne opłaty za routing (`opłata podstawowa` i `stawka opłaty`). Dobry peer nie będzie pobierał wygórowanych opłat za strategiczne kanały. W przypadku pierwszego kanału najlepiej jest wybrać węzeł z raczej umiarkowanymi opłatami, aby nie utrudniać własnych płatności.



Pamiętaj, że twoje własne opłaty za routing również wpływają na to, jak inni postrzegają cię jako peera: węzeł, który stale zmienia swoje opłaty lub nakłada absurdalne koszty, rzadko jest doceniany.



#### 4. Stabilność i staż pracy



Stabilność peera jest bardzo ważnym kryterium. Dobry węzeł ma wysoki czas działania (bardzo rzadko jest offline), utrzymuje swoje kanały otwarte przez długi czas i nie otwiera/zamyka kanałów bez powodu.



Stare i wciąż aktywne kanały są dobrym sygnałem: sugerują, że relacja jest opłacalna dla peera, że węzeł wie, jak zarządzać swoim kapitałem i że nie zamyka się w dowolnym momencie, więc nie musisz płacić opłat onchain za zamknięcie i ponowne otwarcie.



I odwrotnie, partner, który często jest offline lub szybko zamyka kanały, może być źródłem problemów i dodatkowych kosztów związanych z otwieraniem nowych kanałów.



Nawet stosując te kryteria, nie dokonasz idealnego wyboru za pierwszym razem. To normalne: prawdziwa jakość rówieśnika ujawnia się podczas jego użytkowania. Dlatego ważne jest, aby:




- monitorować aktywność kanału (kierowane wolumeny, dostępność itp.);
- zamknąć kanały, które nie służą żadnemu celowi lub których użytkownicy są zbyt często offline;
- z czasem przenieść swój kapitał do lepszych spółek.



Pomysł nie polega na codziennym otwieraniu i zamykaniu kanałów (co byłoby kosztowne w kosztach onchain), ale na stopniowej ewolucji topologii w celu uzyskania zestawu niezawodnych, dobrze połączonych peerów zgodnych z Twoimi potrzebami.



### Jak znaleźć rówieśnika?



Aby zastosować te kryteria, potrzebne są narzędzia zapewniające widoczność sieci Lightning. W tym celu dostępnych jest kilka eksploratorów i usług. Do najbardziej znanych eksploratorów Lightning należą [1ML](https://1ml.com/) i [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Tutaj jednak sugeruję skorzystanie z [narzędzia Lightning Terminal od Lightning Labs](https://terminal.lightning.engineering/), które zapewnia ranking (co prawda oparty na częściowo subiektywnych kryteriach) węzłów Lightning uznanych za najbardziej istotne dla otwarcia kanału.



![Image](assets/fr/030.webp)



Problem z bardzo dużymi węzłami Lightning na szczycie tego rankingu polega na tym, że większość z nich nie akceptuje otwierania kanałów poniżej bardzo wysokich kwot. Wiele z nich stosuje również surowe zasady zarządzania peerami, co może prowadzić do zamknięcia kanału. Z drugiej strony, węzły te zazwyczaj nie potrzebują przychodzącej płynności, biorąc pod uwagę ich liczbę połączeń.



Dlatego radziłbym zejść w dół rankingu, aby znaleźć węzeł, który jest dobrze połączony, niezawodny i wystarczająco centralny w grafie sieci, ale nie jest zbyt duży. Na przykład tutaj zidentyfikowałem węzeł Lightning na stacker.news, który jest bardzo dobrze połączony, ma wysoką przepustowość i zajmuje centralną pozycję w grafie sieci.



![Image](assets/fr/031.webp)



Innym interesującym podejściem jest otwarcie kanału do węzła potrzebującego przychodzącej płynności, takiego jak znajomy sprzedawca, stowarzyszenie lub społeczność. Strategia ta ma trzy zalety:




- Ponieważ wybrany podmiot potrzebuje przychodzącej płynności, logicznie będzie miał mniejszą motywację do zamknięcia kanału bez powodu;
- Jego działalność gospodarcza zwiększa szanse na routing na tym kanale, a tym samym na pobieranie opłat;
- Wyświadczasz przysługę ekosystemowi i wnosisz cenny wkład w życie innych bitcoinerów.



Po zidentyfikowaniu odpowiedniego węzła można pobrać jego identyfikator Node ID. Jest to po prostu połączenie klucza publicznego węzła, separatora `@`, jego adresu IP lub adresu Tor oraz używanego portu. Ten identyfikator jest łatwo dostępny z profilu węzła w dowolnym eksploratorze Lightning.



### Otwórz swój pierwszy kanał przez LND



Teraz, gdy zidentyfikowaliśmy węzeł, za pomocą którego otworzymy nasz pierwszy kanał, potrzebujemy sats, aby go zablokować. Aby to zrobić, należy podać Bitcoin onchain wallet powiązany z LND.



Z głównego interfejsu LND zlokalizuj swój `Bitcoin Wallet`, a następnie kliknij przycisk `Deposit`. Adres odbiorczy onchain to generated: wyślij na niego sats. Kwota, którą musisz przesłać, zależy od pojemności, którą chcesz przydzielić do swojego pierwszego kanału, ale pamiętaj, że musisz wysłać nieco więcej niż docelowa pojemność. Na przykład, jeśli chcesz otworzyć kanał 500 000 sats, nie wysyłaj dokładnie 500 000 sats, ale wyższą kwotę.



![Image](assets/fr/032.webp)



Gdy transakcja zostanie nadana, pojawi się w interfejsie. Poczekaj na potwierdzenie przed otwarciem kanału. Po potwierdzeniu obok transakcji pojawi się zielona strzałka.



![Image](assets/fr/033.webp)



Przewiń w dół do głównego interfejsu, a następnie kliknij `+ OPEN CHANNEL`.



![Image](assets/fr/034.webp)



Wprowadź `Node ID` węzła, z którym chcesz otworzyć kanał, wskaż kwotę, którą chcesz zablokować, a następnie dostosuj opłatę za transakcję otwarcia zgodnie ze stanem rynku opłat onchain. Oczywiście upewnij się wcześniej, że masz wystarczające środki w swoim portfelu LND onchain.



Po ustawieniu wszystkich parametrów kliknij przycisk `OPEN CHANNEL`.



![Image](assets/fr/035.webp)



Poczekaj, aż transakcja otwierająca zostanie potwierdzona w łańcuchu. Twój pierwszy kanał jest teraz oficjalnie operacyjny: gratulacje!



Widać, że w tej chwili 100% płynności kanału jest po mojej stronie: to normalne, ponieważ to ja otworzyłem kanał. W miarę ewolucji płatności i routingu dystrybucja ta ulegnie zmianie, ale całkowita pojemność kanału zawsze pozostanie taka sama.



![Image](assets/fr/036.webp)



Teraz, gdy masz już kanał, możesz dokonać pierwszych płatności Lightning, pod warunkiem, że wybrany węzeł jest prawidłowo podłączony do sieci. Oczywiście w późniejszych rozdziałach przyjrzymy się, jak skonfigurować wygodniejszą metodę płacenia faktur Lightning z telefonu komórkowego. Na razie jednak spróbujmy dokonać pierwszej płatności bezpośrednio z LND do Umbrel.



Aby to zrobić, w sekcji `Lightning Wallet` kliknij przycisk `WYŚLIJ`, a następnie wklej fakturę do ustawienia.



![Image](assets/fr/037.webp)



Wyświetlona zostanie kwota faktury. Potwierdź płatność, klikając przycisk `WYŚLIJ`.



![Image](assets/fr/038.webp)



Jeśli znaleziona zostanie prawidłowa trasa, pierwsza płatność Lightning powinna zakończyć się powodzeniem.



![Image](assets/fr/039.webp)



Jeśli następnie spojrzymy na rozkład płynności w kanale, zobaczymy, że mój peer ma teraz po swojej stronie 5 002 sats. Odpowiada to 5 000 sats płatności, której właśnie dokonałem, a którą skierowałem do węzła odbiorcy. Dodatkowe 2 sats reprezentują opłaty za routing, które zapłaciłem, ponieważ odbiorca otrzymał dokładnie 5 000 sats.



![Image](assets/fr/040.webp)



Aby poprawić niezawodność naszych płatności, konieczne będzie oczywiście otwarcie innych kanałów. W zależności od naszych celów, będziemy również musieli znaleźć sposób na udostępnienie przychodzącej płynności, abyśmy mogli otrzymywać płatności na Lightning. Będzie to tematem następnej sekcji.



# Zarządzanie węzłem Lightning


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Zdefiniuj profil operatora węzła


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Teraz, gdy węzeł Lightning jest już uruchomiony, następnym krokiem jest zdefiniowanie profilu tradera. Jest to ważny wybór, ponieważ określa strategię otwierania kanałów, preferowany typ partnerów i sposób zarządzania płynnością.



W przypadku Lightning, aby to zadziałało, potrzebna jest płynność we właściwym kierunku. Płynność wychodząca odpowiada twojej zdolności do płacenia (sats dostępny po twojej stronie kanałów). Płynność przychodząca odpowiada twojej zdolności do otrzymywania (sats dostępne po stronie twoich partnerów). Innymi słowy, twój profil sprowadza się do prostego pytania: czy sats przez większość czasu opuszczają twój węzeł, czy do niego wchodzą?



### Konsument



Jest to profil zdecydowanej większości użytkowników. Używasz swojego węzła do dokonywania płatności Lightning: do kupowania towarów i usług, płacenia rachunków, wysyłania napiwków - krótko mówiąc, do korzystania z Lightning jako szybkiego środka płatniczego. Z drugiej strony, otrzymujesz niewiele z Lightning lub tylko marginalnie, na przykład kilka darowizn, zwroty między przyjaciółmi lub kilka mikropłatności.



Ten profil jest najłatwiejszy w zarządzaniu, ponieważ główną potrzebą jest możliwość dokonywania płatności. W praktyce oznacza to, że potrzebujesz płynności wychodzącej. Po otwarciu jednego lub więcej kanałów o odpowiednim rozmiarze do stabilnych, dobrze połączonych węzłów, płatności wychodzące będą mechanicznie przenosić płynność na drugą stronę kanałów. To właśnie ten ruch w naturalny sposób tworzy rozsądną ilość płynności przychodzącej. W rezultacie, nawet jeśli nie chcesz regularnie otrzymywać płatności, nadal będziesz w stanie otrzymywać je od czasu do czasu bez konieczności wdrażania złożonej strategii. Nie musisz więc martwić się o płynność przychodzącą.



W tym kursie LNP202 skupimy się na tym "konsumenckim" profilu operatora węzła, ponieważ odpowiada on prawie wszystkim użytkownikom Bitcoin na Lightning.



### Sprzedawca detaliczny



Sprzedawca jest w pewnym sensie przeciwieństwem konsumenta. Tutaj głównym celem nie jest płacenie, ale zbieranie. Firma, usługodawca, sklep internetowy lub punkt sprzedaży, który akceptuje Lightning, otrzyma wiele płatności przychodzących i dokona stosunkowo niewielu płatności wychodzących z tego węzła.



Ten profil jest bardziej wymagający, ponieważ odmowa płatności na Lightning potencjalnie oznacza utratę sprzedaży. Priorytetem staje się zatem płynność przychodząca. Jeśli węzeł nie ma wystarczającej płynności przychodzącej, klienci zobaczą, że ich płatności nie powiodą się, nawet jeśli mają środki, po prostu dlatego, że nie ma trasy, aby dostarczyć płynność do Ciebie we właściwym kierunku.



Głównym wyzwaniem dla sprzedawcy jest również naturalna ewolucja kanałów. Jeśli wszystko, co robisz, to odbieranie, twoje kanały będą się stopniowo zapełniać. Potrzebne są więc mechanizmy utrzymywania i odnawiania płynności przychodzącej.



Istnieje jednak prostszy przypadek: mieszany profil konsumenta/sprzedawcy. Jeśli zbierasz na Lightning, ale także wydajesz na Lightning (wydatki biznesowe, płatności dla dostawców, a nawet wydatki osobiste), wówczas płatności wychodzące w naturalny sposób odtwarzają przychodzące. Zarządzanie staje się płynniejsze, ponieważ przepływy kompensują się nawzajem i nie ma potrzeby uciekania się do sztucznych mechanizmów zaprojektowanych wyłącznie w celu odzyskania płynności przychodzącej.



### Router



Router jest specyficznym profilem. Nie używa swojego węzła Lightning do płacenia lub pobierania opłat, ale do kierowania płatności innych osób i pobierania opłat. Celem jest bycie użyteczną, niezawodną i ekonomicznie konkurencyjną trasą w ramach wykresu Lightning.



Szczerze mówiąc, bycie routerem na Lightning jest bardziej złożonym biznesem, niż się wydaje, a rentowność jest trudna do osiągnięcia. Po pierwsze, otwieranie i zamykanie kanałów wiąże się z wysokimi kosztami onchain. Aby skutecznie routować, często trzeba dostosowywać topologię, testować, zamykać nieefektywne kanały, otwierać nowe i regularnie przywracać równowagę płynności. Po drugie, konkurencja jest zaciekła: duże węzły o ugruntowanej pozycji w naturalny sposób przechwytują dużą część ruchu i trudno jest zdobyć przyczółek bez wiązania znacznego kapitału w dużych kanałach.



Istnieją również wysokie wymagania operacyjne. Węzeł routingu musi być niezwykle stabilny, monitorowany, odpowiednio zabezpieczony i rygorystycznie zarządzany. Trzeba monitorować wydajność kanału, dostosowywać politykę opłat, utrzymywać zrównoważoną płynność, zarządzać peerami i szybko rozwiązywać problemy techniczne. Ten poziom zaangażowania może być interesujący jako techniczne hobby lub wkład w infrastrukturę, ale jeśli celem jest po prostu korzystanie z Lightning w suwerenny sposób, angażowanie się w routing w celu zarabiania pieniędzy rzadko jest istotne. Dlatego ten kurs LNP202 nie obejmuje dogłębnie tego profilu.



### Jasno określ swoją sytuację, zanim przejdziesz dalej



Jeśli pasujesz do profilu konsumenta, Twoim priorytetem będzie możliwość niezawodnego płacenia przy prostym zarządzaniu. Jeśli jesteś sprzedawcą, Twoim priorytetem będzie bezawaryjne wypłacanie gotówki, co oznacza strategię pozyskiwania płynności przychodzącej. Jeśli rozważasz routing, musisz podejść do niego jako do wymagającego, niepewnego ekonomicznie i czasochłonnego działania.



Zdefiniowanie tego profilu teraz pomoże uniknąć klasycznej pułapki: stosowania strategii kanału zaprojektowanej dla sprzedawcy lub routera, gdy jesteś po prostu użytkownikiem, który chce zapłacić.



## Korzystanie z menedżera węzłów Lightning


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



W poprzedniej części tego szkolenia LNP202 korzystaliśmy z podstawowego interfejsu aplikacji `Lightning Node` na Umbrel. Interfejs ten jest wystarczający do podstawowych operacji (sprawdzanie sald, przeglądanie dystrybucji gotówki, otwieranie i zamykanie kanałów), ale jest celowo bardzo uproszczony. Ta prostota ogranicza dostępne opcje i nie daje dostępu do wielu zaawansowanych funkcji węzła LND. Z tego powodu będziemy teraz używać innego, bardziej wszechstronnego oprogramowania do zarządzania węzłami Lightning.



To dodatkowe oprogramowanie będzie po prostu uzupełniającym interfejsem zarządzania dla węzła. Oznacza to, że możesz nadal używać interfejsu `Lightning Node` równolegle, a nawet używać kilku różnych, jeśli chcesz. Są to po prostu różne sposoby interakcji z tym samym węzłem Lightning.



Do najbardziej znanych programów należą:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Wszystkie trzy rozwiązania są dobre. Jeśli chcesz, możesz przetestować wszystkie trzy z węzłem, zanim wybierzesz ten, który najbardziej Ci odpowiada. Osobiście używam ThunderHub z przyzwyczajenia i dlatego, że wydaje się bardziej kompletny niż inne. Jest to narzędzie, które zaprezentuję w tym szkoleniu, ale możesz również wybrać jedną z dwóch pozostałych alternatyw. Mamy dedykowany samouczek dla każdego z tych programów na Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Instalacja ThunderHub



Wszystkie te programy można bardzo łatwo zainstalować z Umbrel App Store. Jak już wspomniałem, użyjemy tutaj ThunderHub, ale jeśli chcesz przetestować inny później, procedura będzie podobna.



![Image](assets/fr/041.webp)



Umbrel zapewnia domyślne hasło dostępu do ThunderHub. Skopiuj je: będziesz go potrzebować od razu. Pamiętaj również, aby zapisać je w menedżerze haseł, ponieważ będziesz o nie proszony przy każdym otwarciu oprogramowania.



![Image](assets/fr/042.webp)



Kliknij `Login`, a następnie wklej hasło dostarczone przez Umbrel, aby się zalogować.



![Image](assets/fr/043.webp)



Nastąpi przeniesienie do strony głównej ThunderHub, która wyświetla główne informacje o węźle Lightning.



![Image](assets/fr/044.webp)



Na początek zalecam aktywację uwierzytelniania dwuskładnikowego (2FA). W ustawieniach wystarczy kliknąć `Włącz` obok `Włącz 2FA`, a następnie postępować zgodnie ze zwykłym procesem.



![Image](assets/fr/045.webp)



### Użyj ThunderHub



ThunderHub jest stosunkowo łatwy do opanowania. Wszystkie menu są dostępne z lewej kolumny interfejsu. Podsumowując, oto co robi każde z nich:




- home: przegląd węzłów, salda i szybkie działania;
- pulpit nawigacyjny: konfigurowalny pulpit nawigacyjny z widżetami i danymi;
- peers: przeglądanie i zarządzanie połączeniami z innymi węzłami Lightning;
- kanały": pełne zarządzanie kanałami (płynność, opłaty, zamknięcie itp.);
- rebalance": narzędzie do równoważenia kanałów za pomocą płatności cyklicznych;
- transakcje: historia wysłanych i otrzymanych płatności Lightning;
- forwards`: statystyki routingu i koszty generated przez węzeł;
- `Chain`: Portfel Bitcoin onchain (UTXO i transakcje);
- integracja gW-201 do monitorowania i tworzenia kopii zapasowych;
- `Tools`: zaawansowane narzędzia (kopie zapasowe, raporty, makarony, podpisy itp.);
- zamiana: Zamiana lightning/onchain za pośrednictwem Boltz;
- `Stats`: ogólne statystyki i wydajność węzła Lightning.



Dzięki temu zestawowi funkcji masz wszystkie narzędzia potrzebne do wydajnego zarządzania węzłem Lightning. Nie jest konieczne, aby od razu opanować każdą opcję w szczegółach: będziemy je odkrywać stopniowo w trakcie tego kursu. Jeśli jednak chcesz zapoznać się z oprogramowaniem bardziej szczegółowo, zapoznaj się z naszym samouczkiem ThunderHub:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Najbardziej interesującym nas menu jest `Channels`. Oferuje ono szczegółowy widok wszystkich kanałów w węźle, wraz z ich rozkładem płynności. W szczególności możesz zobaczyć, które kanały są otwarte w `Open`, które czekają na otwarcie lub zamknięcie w `Pending`, a które są już zamknięte w `Closed`.



![Image](assets/fr/047.webp)



W przypadku danego kanału można kliknąć nazwę peera lub identyfikator kanału, aby otworzyć jego stronę Amboss i uzyskać więcej informacji. Możesz także kliknąć ikonę ołówka, aby zmodyfikować parametry kanału, w tym zasady opłat stosowane do tego kanału, jeśli Twój węzeł kieruje płatności do węzła Twojego peera.



![Image](assets/fr/048.webp)



Jeśli używasz węzła Lightning głównie jako "konsumenta", nie musisz zmieniać tych opłat: możesz zachować wartości domyślne. Z drugiej strony, jeśli chcesz lepiej zrozumieć, jak działają opłaty za routing w Lightning, polecam szkolenie LNP 201, a w szczególności rozdział 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Klikając mały krzyżyk obok elementu równorzędnego, można zainicjować zamknięcie kanału. Jeśli na przykład zauważysz, że partner jest regularnie nieaktywny, może być wskazane zamknięcie tego kanału w celu przeniesienia kapitału do bardziej niezawodnego partnera.



Masz wtedy dwie możliwości. Pierwszą i zawsze preferowaną jest zamknięcie w trybie współpracy. Potwierdzając tę akcję, węzeł prosi peera o wspólne zamknięcie kanału. Jeśli się zgodzi, możesz nadać transakcję zamknięcia onchain i odzyskać swoją część środków. Zaletą tej metody jest to, że wybierasz opłaty onchain za transakcję, unikając w ten sposób niepotrzebnych kosztów, a środki są odzyskiwane szybciej, bez blokady czasowej.



![Image](assets/fr/049.webp)



Drugą opcją jest wymuszone zamknięcie. W tym przypadku nie pytasz o zgodę peera i bezpośrednio transmitujesz ostatni posiadany commitment transaction. Nie polecam tej metody, chyba że jest to ostateczność, na przykład jeśli peer systematycznie odmawia zamknięcia kooperacyjnego lub przestaje odpowiadać. Wymuszone zamknięcie ma dwie główne wady: opłaty są często bardzo wysokie, ponieważ zostały ustalone z wyprzedzeniem, aby przewidzieć wzrost opłat onchain, a odzyskanie środków jest opóźnione, ponieważ są one blokowane przez blokadę czasową. Ta blokada czasowa daje peerowi czas na reakcję w przypadku próby oszustwa (co oczywiście nie ma miejsca w tym przypadku, ale nadal trzeba czekać).



![Image](assets/fr/050.webp)



Wreszcie, aby otworzyć nowy kanał, przejdź do menu `Home` i kliknij `Open a Channel` w sekcji `Liquidity`. Następnie będziesz mógł wprowadzić identyfikator wybranego węzła, pojemność kanału, żądaną opłatę za routing Lightning i opłatę onchain za transakcję otwierającą.



![Image](assets/fr/051.webp)



Są to główne czynności, które należy wykonać na ThunderHub. W trakcie tego kursu LNP202 odkryjemy inne funkcje.



## Uzyskanie przychodzącej płynności


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Jak widać, posiadanie płynności wychodzącej w celu dokonywania płatności na Lightning nie jest szczególnie skomplikowane. Wystarczy otworzyć kanały z własnej inicjatywy do innych węzłów i rozpocząć wysyłanie sats. Z drugiej strony, posiadanie płynności przychodzącej w celu otrzymywania płatności na Lightning jest bardziej skomplikowane, ponieważ albo potrzebujesz innych węzłów, aby otworzyć kanały do Ciebie, albo musisz samodzielnie przenieść płynność, dokonując płatności.



Jeśli przyjmiesz profil "konsumenta", generalnie nie musisz martwić się o płynność przychodzącą. Korzystanie z węzła Lightning będzie głównie zorientowane na płatności, a nie na wypłatę gotówki. Po prostu dokonując kilku płatności Lightning, z czasem w naturalny sposób stworzysz płynność przychodzącą.



Z drugiej strony, jeśli masz profil "sprzedawcy", sytuacja jest odwrotna: będziesz głównie zbierać płatności i wykonywać ich niewiele. Nie możesz więc polegać wyłącznie na własnych płatnościach w celu uzyskania płynności przychodzącej. Konieczne staje się zatem, aby inne węzły Lightning otworzyły kanały do twojego. Ale jak można to osiągnąć? Jak skłonić innych operatorów do pozyskania dla Ciebie kapitału? Właśnie to zbadamy w tym rozdziale.



### Kupowanie płynności przychodzącej



Jak można się spodziewać, najskuteczniejszym sposobem skłonienia kogoś do działania jest zapłacenie mu. W przypadku płynności przychodzącej do węzła Lightning zasada jest dokładnie taka sama. Najprostszym sposobem na doprowadzenie kanałów do węzła jest zapłacenie za usługę i związane z nią powiązanie kapitałowe.



Jeśli jesteś firmą lub sprzedawcą detalicznym, takie podejście oznacza, że możesz szybko uzyskać niezawodne kanały do zbierania płatności od klientów bez tarć.



Istnieje wiele sposobów na zakup płynności przychodzącej. Osobiście używam i polecam platformę Amboss [Magma](https://magma.amboss.tech/). Jest bardzo łatwa w użyciu, otwarcie kanału jest szybkie, a stawki są ogólnie rozsądne. Magma działa jak rynek z twórcami i biorcami, ale wersja 2 znacznie uprościła doświadczenie: wystarczy utworzyć żądanie, zapłacić cenę za pośrednictwem Lightning, a Magma automatycznie dopasuje ją do najlepszej dostępnej oferty. Po sześciu potwierdzeniach onchain, kanał z przychodzącą płynnością jest gotowy do działania. Oto jak to działa:



Przejdź do [strony internetowej Magma](https://magma.amboss.tech/buy), w sekcji `Kup kanały`.



![Image](assets/fr/052.webp)



Jeśli chcesz, możesz utworzyć konto, aby śledzić swoje zakupy, ale nie jest to obowiązkowe. Jeśli użytkownik nie utworzy konta, Magma po prostu dostarczy mu identyfikator sesji, który umożliwi mu późniejsze odzyskanie zakupów.



Po wejściu na stronę wypełnij informacje wymagane do zakupu płynności. Wybierz opcję "Jednorazowo", aby dokonać jednorazowego zakupu, a następnie wprowadź kwotę, którą chcesz zapłacić za przychodzącą płynność. Im wyższa zapłacona kwota, tym większa przepustowość kanału otwartego dla węzła. Poniżej znajduje się szacunkowa pojemność kanału: jest to przybliżenie, ponieważ ostateczna kwota będzie zależeć od najlepszej oferty znalezionej przez Magma, która czasami jest wyższa, a czasami niższa.



![Image](assets/fr/053.webp)



Następnie wprowadź identyfikator węzła. Można go znaleźć na przykład w menu `Node ID` aplikacji `Lightning Node` na Umbrel.



![Image](assets/fr/054.webp)



Po wypełnieniu wszystkich informacji kliknij przycisk "Przejrzyj i otwórz zamówienie".



![Image](assets/fr/055.webp)



Jeśli nie utworzyłeś konta, Magma dostarczy Ci klucz sesji i plik kopii zapasowej. Przechowuj te dwa elementy w bezpiecznym miejscu, ponieważ pozwolą ci one odzyskać zamówienie w późniejszym terminie lub śledzić jego status w przypadku wystąpienia problemu. Po zapisaniu pliku kliknij przycisk `Pay with Lightning`.



![Image](assets/fr/056.webp)



Następnie Magma generate wystawia fakturę Lightning na wybraną kwotę. Musisz ją zapłacić. Jeśli masz już kanały w swoim węźle Lightning, możesz zapłacić bezpośrednio z niego lub użyć innego zewnętrznego wallet Lightning.



![Image](assets/fr/057.webp)



Po dokonaniu płatności transakcja jest wyświetlana jako przetworzona w interfejsie Magma.



![Image](assets/fr/058.webp)



Po kilku minutach żądanie zostanie przetworzone: kanał z sats zostanie otwarty dla węzła Lightning. Gdy transakcja otwarcia zostanie potwierdzona w łańcuchu, uzyskasz dostęp do odpowiedniej przychodzącej płynności.



![Image](assets/fr/059.webp)



Magma jest również zintegrowana bezpośrednio z ThunderHub. W zakładce `Home` przewiń w dół do sekcji `Liquidity` i kliknij `Buy Inbound Liquidity`. Wszystko, co musisz zrobić, to wprowadzić żądaną kwotę i potwierdzić. Nie musisz ręcznie opłacać żadnych faktur, ponieważ ThunderHub automatycznie zajmie się płatnościami z Twojego węzła.



![Image](assets/fr/060.webp)



Jeśli jesteś sprzedawcą, ten rodzaj usługi jest szczególnie odpowiedni, ponieważ umożliwia szybkie uzyskanie dużej ilości płynności przychodzącej z wiarygodnych węzłów, gwarantując, że Twoi klienci będą mogli zapłacić Ci bez trudności. Z drugiej strony, jeśli jesteś osobą prywatną lub nie chcesz płacić za płynność przychodzącą, istnieją również darmowe rozwiązania. Przyjrzyjmy się im.



### Współpracująca płynność przychodząca



Jeśli nie jesteś traderem, ale nadal potrzebujesz pewnej płynności przychodzącej (na przykład, aby zasilić swój węzeł podczas uruchamiania, czekając na dokonanie niektórych płatności), niekoniecznie musisz za to płacić. Jednym z preferowanych przeze mnie rozwiązań jest współpraca z innymi operatorami węzłów, którzy również potrzebują płynności przychodzącej, aby otworzyć dla siebie kanały Lightning. W ten sposób otwarcie kanału przynosi płynność wychodzącą, jednocześnie zapewniając płynność przychodzącą, bezpłatnie (modulo opłaty onchain za otwarcie).



Można to oczywiście zorganizować bezpośrednio z innymi bitcoinerami. Istnieje jednak platforma dedykowana tego typu okrągłym otwarciom: [Lightning Network +](https://lightningnetwork.plus/). Zasadą nie jest otwieranie dwóch kanałów między tymi samymi osobami, ale tworzenie okrągłych otwarć obejmujących co najmniej trzech uczestników, a nawet więcej.



Weźmy przykład, aby zrozumieć, jak działa Lightning Network +:




- Operator węzła o nazwie `A` publikuje ogłoszenie, w którym informuje, że chce otworzyć kanał o wartości 1 miliona sats z dwiema innymi osobami;
- Ogłoszenie pozostaje aktywne do momentu dodania kolejnych uczestników;
- Później dwaj operatorzy, `B` i `C`, dołączają do ogłoszenia węzła `A`. Trójkąt jest teraz kompletny i można rozpocząć fazę otwarcia.
- Węzeł `A` otwiera kanał do węzła `B`;
- Węzeł `B` otwiera kanał do węzła `C`;
- Węzeł `C` otwiera kanał do węzła `A`.



Pod koniec operacji każdy węzeł ma 1 milion sats płynności wychodzącej i 1 milion sats płynności przychodzącej. Schemat ten można rozszerzyć do czterech lub pięciu uczestników.



Oczywiście nie ma technicznego mechanizmu gwarantującego, że uczestnik faktycznie otworzy kanał, który zobowiązał się utworzyć. Dlatego platforma stworzyła system reputacji, oparty na pozytywnych recenzjach, gdy operatorzy wywiązują się ze swoich zobowiązań. A w najgorszym przypadku, jeśli natkniesz się na kogoś, kto nie będzie współpracował, nie stracisz żadnych pieniędzy: po prostu przegapisz okazję na napływ płynności.



Rozwiązanie to jest szczególnie odpowiednie dla profilu "konsumenckiego", ponieważ pozwala na uzyskanie płynności przychodzącej bezpłatnie, jednocześnie łącząc węzeł z innymi małymi operatorami. Z drugiej strony, jeśli jesteś traderem, takie podejście generalnie nie jest odpowiednie: każdy sat płynności przychodzącej wymaga zablokowania sata płynności wychodzącej, a duże zapotrzebowanie na płynność przychodzącą wiązałoby się z wiązaniem zbyt dużej ilości kapitału.



Aby korzystać z Lightning Network +, masz dwie możliwości: albo użyć aplikacji zintegrowanej z Umbrel, albo użyć klasycznej strony internetowej i utworzyć konto, logując się z węzła. Polecam tę drugą opcję, ponieważ zintegrowana aplikacja nie oferuje pełnego zakresu dostępnych funkcji.



Wejdź na stronę [Lightning Network+](https://lightningnetwork.plus/) i kliknij przycisk `Login` w prawym górnym rogu interfejsu.



![Image](assets/fr/061.webp)



Aby się uwierzytelnić, należy podpisać dostarczoną wiadomość przy użyciu klucza prywatnego węzła Lightning. W przypadku ThunderHub operacja ta jest bardzo prosta. Zacznij od skopiowania wiadomości wyświetlanej przez LN+.



![Image](assets/fr/062.webp)



W ThunderHub przejdź do zakładki `Tools`, a następnie kliknij przycisk `Sign` w sekcji `Messages`.



![Image](assets/fr/063.webp)



Wklej wiadomość uwierzytelniającą dostarczoną przez LN+, a następnie kliknij `Podpisz`.



![Image](assets/fr/064.webp)



Następnie ThunderHub podpisuje tę wiadomość przy użyciu klucza prywatnego węzła. Skopiuj podpis generated.



![Image](assets/fr/065.webp)



Wklej ten podpis do odpowiedniego pola na stronie LN+, a następnie kliknij `Zaloguj`.



![Image](assets/fr/066.webp)



Jesteś teraz połączony z LN+ za pomocą swojego węzła Lightning. Ten proces pozwala LN+ zweryfikować, czy jesteś prawowitym właścicielem węzła, do którego rościsz sobie prawo na ich platformie.



![Image](assets/fr/067.webp)



Jeśli chcesz, możesz spersonalizować swój profil LN+, na przykład dodając krótką biografię.



Aby wziąć udział w pierwszym otwarciu kanału kołowego, przejdź do menu `Swaps` w górnej części interfejsu. Znajdziesz tam wszystkie aktualnie dostępne swapy, w zależności od charakterystyki twojego węzła.



![Image](assets/fr/068.webp)



Aby dołączyć do istniejącej oferty wymiany, wystarczy ją kliknąć i zarejestrować się. Jednak w LN+ twórca swapu może nałożyć na uczestników pewne warunki, takie jak minimalna liczba kanałów lub minimalna całkowita pojemność węzła. Dlatego możliwe jest, zwłaszcza w pierwszych dniach, że niewiele ofert będzie dostępnych dla węzła. W moim przypadku, pomimo kilku już otwartych kanałów, żadne oferty nie były dostępne dla mojego węzła. Stworzyłem więc własny swap i możesz zrobić to samo, jeśli jesteś w takiej samej sytuacji.



Kliknij `Start Liquidity Swap`, a następnie wprowadź parametry oferty:




- Wybierz całkowitą liczbę uczestników (3, 4 lub 5);
- Wskaż liczbę kanałów, które mają zostać otwarte (upewnij się, że masz co najmniej taką liczbę w swoim łańcuchu wallet);
- Zdefiniuj czas otwarcia kanału. Jest to okres, w którym uczestnicy zgadzają się ich nie zamykać;
- Po prawej stronie można ustawić ograniczenia dla uczestników: minimalną liczbę kanałów, minimalną łączną pojemność i typ akceptowanego połączenia.



Po ustawieniu wszystkich parametrów kliknij przycisk `Start Liquidity Swap`.



![Image](assets/fr/069.webp)



Twoja oferta wymiany została utworzona. Teraz wystarczy poczekać na rejestrację innych operatorów węzłów. Jeśli warunki nie są zbyt restrykcyjne, nie powinno to zająć zbyt wiele czasu. Pamiętaj, aby monitorować status wymiany w kolejnych godzinach lub dniach.



![Image](assets/fr/070.webp)



Wszystkie miejsca wymiany zostały zajęte: przechodzimy teraz do fazy otwierania kanału. Każdy uczestnik widzi na swoim interfejsie LN+, do którego węzła musi otworzyć kanał Lightning.



![Image](assets/fr/084.webp)



Po swojej stronie należy otworzyć kanał przy użyciu identyfikatora węzła dostarczonego przez LN+ i przestrzegając wskazanej kwoty. Jak widzieliśmy w poprzednich rozdziałach, można to zrobić za pośrednictwem ThunderHub, innego menedżera węzłów Lightning lub bezpośrednio z podstawowego interfejsu aplikacji Lightning Node.



![Image](assets/fr/085.webp)



Po uruchomieniu otwarcia można je zobaczyć w sekcji kanałów oczekujących. W moim przypadku jest to kanał z węzłem `Plebian_fr`.



![Image](assets/fr/086.webp)



Następnie można powrócić do LN+, aby potwierdzić rozpoczęcie otwierania kanału. Wystarczy kliknąć przycisk `Channel Opening Started`.



![Image](assets/fr/087.webp)



Gdy wszyscy pozostali uczestnicy również otworzą kanał, do którego się zobowiązali, pamiętaj, aby zostawić im pozytywną recenzję.



![Image](assets/fr/088.webp)



W przypadku trudności lub opóźnień możesz skontaktować się bezpośrednio ze swoimi rówieśnikami za pośrednictwem sekcji komentarzy na dole strony.



![Image](assets/fr/089.webp)



Niektórzy uczestnicy mogą chcieć zrównoważyć kanały okrężne od samego początku, dokonując płatności na swoją rzecz. Zapewnia to zrównoważoną dystrybucję gotówki w każdym kanale. Jeśli jesteś w profilu "konsumenta", nie jest to konieczne, ale możesz albo samemu dokonać takiego zrównoważenia, jeśli chcesz, albo tymczasowo ustawić opłaty za kanały na zero, aby ułatwić to rówieśnikowi, który chce to zrobić. Czasami nikt nie chce tego robić.



![Image](assets/fr/090.webp)




# Uwolnienie potencjału węzła Lightning


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Podłącz mobilny wallet przez Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



To wszystko, masz teraz dobrze połączony węzeł Lightning, zarówno z płynnością przychodzącą, jak i wychodzącą. Jesteś więc gotowy do korzystania z węzła Lightning w prawdziwym życiu. Do tej pory zawsze używaliśmy interfejsów bezpośrednio na Umbrel, albo aplikacji `Lightning Node`, albo interfejsu `ThunderHub`. Narzędzia te działają do wysyłania i odbierania płatności, ale wyraźnie nie są zoptymalizowane pod kątem codziennych płatności Lightning. Interfejs jest przeznaczony do użytku na komputerze, niepraktyczny na smartfonie, a także wymaga połączenia z tą samą siecią, aby działał poprawnie (chociaż technicznie możliwe jest zdalne połączenie przez Tor).



W praktyce to, czego szukamy jako bitcoinerzy, to klasyczny interfejs Lightning wallet na smartfonie: możliwość skanowania faktur za pomocą kodu QR oraz prosty interfejs do płacenia i wypłacania gotówki sats. Właśnie to będziemy wdrażać w tym i następnym rozdziale. Ogólną ideą jest posiadanie mobilnej aplikacji Lightning wallet na smartfonie, która może być używana z dowolnego miejsca (nie tylko z sieci lokalnej), ale która w tle opiera się na własnym węźle Lightning do wysyłania i odbierania płatności.



### Jakie są rozwiązania umożliwiające nawiązanie kontaktu z klientem mobilnym?



Obecnie istnieje na to kilka sposobów, zarówno pod względem aplikacji mobilnej, jak i rodzaju połączenia między węzłem a tą aplikacją. Trzy główne tryby połączenia to:




- przez ***Tor***;
- przez VPN ***Tailscale***;
- przez ***Nostr Wallet Connect***.



Kilka lat temu łączyłem się przez ***Tor***, ale szybko przestałem: liczba awarii i opóźnienia w komunikacji były zbyt duże. W teorii to działa, ale w praktyce doświadczenie użytkownika było katastrofalne. Dlatego odradzam to podejście.



Alternatywą, którą następnie zastosowałem, było użycie ***Tailscale*** VPN w celu zapewnienia komunikacji między aplikacją mobilną a węzłem. To rozwiązanie działa bardzo dobrze: nawet w sieciach komórkowych o niskiej przepustowości moje płatności zawsze przechodzą bez trudności. Jest to metoda, którą przedstawię jako pierwszą w tym rozdziale, z aplikacją Zeus.



W następnym rozdziale przyjrzymy się innemu, nowszemu rozwiązaniu, które również działa bardzo dobrze: ***Nostr Wallet Connect***. Tym razem użyjemy aplikacji Alby Go, aby przedstawić alternatywę, chociaż Zeus jest również kompatybilny z NWC, jeśli chcesz.



### Instalacja i konfiguracja Tailscale



Do tej pierwszej metody będziemy potrzebować Tailscale. Jest to rozwiązanie VPN oparte na WireGuard, które pozwala bezpiecznie łączyć urządzenia rozproszone po całym Internecie, jednocześnie automatycznie zarządzając szyfrowaniem, uwierzytelnianiem i przechodzeniem przez NAT. Mówiąc prościej, to tak, jakby wszystkie urządzenia były podłączone do tej samej sieci LAN co router, nawet jeśli mogą znajdować się w dowolnym miejscu w Internecie.



Aby z niego skorzystać, należy najpierw utworzyć konto. Wejdź na stronę Tailscale, a następnie kliknij przycisk `Get Started`.



![Image](assets/fr/071.webp)



Następnie wybierz dostawcę tożsamości dla swojego konta Tailscale. Osobiście użyłem jednego z moich kont GitHub do zalogowania się.



![Image](assets/fr/072.webp)



Po zalogowaniu zostaniesz poproszony o udzielenie odpowiedzi na kilka pytań dotyczących Twojego użytkowania. Odpowiedz na nie krótko, aby kontynuować.



![Image](assets/fr/073.webp)



Następnie Tailscale oferuje zainstalowanie klienta na komputerze. W tej chwili nie jest to przedmiotem naszego zainteresowania: przejdź bezpośrednio do Umbrel i zainstaluj aplikację Tailscale z App Store.



![Image](assets/fr/074.webp)



Po otwarciu aplikacji kliknij `Log In`, a następnie postępuj zgodnie z procesem uwierzytelniania, używając tej samej metody, co podczas tworzenia konta.



![Image](assets/fr/075.webp)



Kliknij `Connect`, aby potwierdzić. Urządzenie Umbrel jest teraz połączone z siecią VPN.



![Image](assets/fr/076.webp)



Następnie pobierz aplikację Tailscale na swój smartfon i zaloguj się przy użyciu tego samego konta. Uwaga: w systemie Android nie jest możliwe jednoczesne korzystanie z dwóch sieci VPN. Aby Tailscale działał, musisz wyłączyć wszystkie inne aktywne sieci VPN. Co więcej, za każdym razem, gdy chcesz użyć węzła Lightning za pośrednictwem Zeus, musisz aktywować Tailscale VPN, w przeciwnym razie połączenie nie zostanie nawiązane.



![Image](assets/fr/077.webp)



W witrynie Tailscale, teraz gdy co najmniej dwóch klientów jest podłączonych, można uzyskać dostęp do konsoli administracyjnej z listą wszystkich urządzeń podłączonych do sieci i ich adresów IP Tailscale.



![Image](assets/fr/078.webp)



### Połącz Zeusa



Zainstaluj aplikację Zeus na swoim telefonie. Po jej otwarciu wybierz `Advanced Setup`, a następnie `Create or connect a wallet`.



![Image](assets/fr/079.webp)



W sekcji `Interfejs Wallet` wybierz `LND (REST)`. Następnie wprowadź adres Tailscale swojego Umbrel, który można znaleźć na pulpicie nawigacyjnym Tailscale lub bezpośrednio w aplikacji Tailscale na Umbrel. Jako port wpisz `8080`.



![Image](assets/fr/080.webp)



Następnie Zeus prosi o podanie `Macaroon`. Jest to autoryzacja token, która pozwala precyzyjnie zdefiniować prawa przyznane aplikacji (w tym przypadku Zeusowi) do interakcji z węzłem Lightning. Możliwe jest generate utworzenie makaronu z ThunderHub, w menu `Tools`, podmenu `Bakery`, ale w tym celu najprostszym sposobem jest pobranie go bezpośrednio z aplikacji `Lightning Node`.



Kliknij na trzy małe kropki w prawym górnym rogu interfejsu, a następnie na `Connect Wallet`. Wybierz `REST (sieć lokalna)`. Będziesz wtedy mógł skopiować makaron z odpowiednimi uprawnieniami.



![Image](assets/fr/081.webp)



Wklej go do odpowiedniego pola w aplikacji Zeus, a następnie kliknij przycisk `SAVE WALLET CONFIG`.



![Image](assets/fr/082.webp)



Dostęp do węzła Lightning można teraz uzyskać z aplikacji Zeus. Oznacza to, że możesz otrzymywać płatności za faktury generate bezpośrednio na swoim węźle Lightning ze smartfona, a także płacić za faktury Lightning, gdziekolwiek jesteś.



![Image](assets/fr/083.webp)



Wskazówka: Tailscale nie ogranicza się do zdalnego korzystania z węzła Lightning. Umożliwia on dostęp do wszystkich narzędzi Umbrel z poziomu innego oprogramowania, nawet zdalnie. Na przykład, możesz użyć adresu IP Tailscale swojego Umbrel do połączenia węzła Bitcoin (przez Electrs lub Fulcrum) z Sparrow Wallet, bez przechodzenia przez Tor. Po raz kolejny pozwala to uniknąć powolności związanej z Torem. Wystarczy zainstalować klienta Tailscale na komputerze i podłączyć go do sieci.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

W następnym rozdziale przyjrzymy się innemu, równie skutecznemu sposobowi połączenia klienta mobilnego z węzłem Lightning: Nostr Wallet Connect. Będziemy używać innej aplikacji niż Zeus (chociaż Zeus jest również kompatybilny z NWC), a mianowicie Alby Go.



## Podłącz mobilny wallet przez NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Jeśli nie jesteś przekonany do połączenia Tailscale lub jeśli zarządzanie podwójną siecią VPN wydaje się zbyt kłopotliwe, ten rozdział sugeruje inny sposób korzystania ze zdalnego klienta mobilnego do płacenia i odbierania sats za pośrednictwem węzła Lightning: ***Nostr Wallet Connect***.



W tym przykładzie wykorzystamy aplikację mobilną Alby Go, która jest bardzo dobrze zaprojektowana i wyjątkowo łatwa do opanowania. Można jednak użyć również Zeusa lub dowolnej innej aplikacji mobilnej kompatybilnej z NWC. Lista kompatybilnych aplikacji znajduje się na [repozytorium `awesome-nwc` GitHub](https://github.com/getAlby/awesome-nwc).



### Jak działa Nostr Wallet Connect?



Nostr Wallet Connect jest ustandaryzowanym protokołem, który pozwala aplikacji lub stronie internetowej wyzwalać akcje na zdalnym węźle Lightning, bez nawiązywania bezpośredniego połączenia sieciowego z tym węzłem (bez API LND odsłoniętego, bez VPN, bez usługi `.onion`...). NWC definiuje sposób, w jaki aplikacja formułuje intencję (np. `pay_intece`) i odbiera wynik.



Działa to całkiem prosto. Sesję inicjuje się poprzez zeskanowanie kodu QR lub poprzez deeplink `nostr+walletconnect:`. Ciąg ten zawiera parametry sesji i sekret autoryzacji. Następnie, gdy aplikacja chce zapłacić, serializuje żądanie, szyfruje je i publikuje jako zdarzenie w przekaźniku Nostr. Węzeł odczytuje zdarzenie w przekaźniku, odszyfrowuje je, sprawdza, czy autor jest autoryzowany dla tej sesji, wykonuje płatność, a następnie zwraca zaszyfrowaną odpowiedź (sukces z obrazem wstępnym lub błąd). Przekaźnik działa jedynie jako pośrednik w transporcie: nie może odczytać treści, ale może obserwować czas i częstotliwość żądań.



W porównaniu z połączeniem przez Tailscale lub Tor, główną zaletą NWC jest to, że węzeł nie jest bezpośrednio osiągalny z zewnątrz. To znacznie upraszcza użytkowanie mobilne: węzeł nie musi akceptować połączeń przychodzących, musi jedynie być w stanie komunikować się z przekaźnikiem. Z drugiej strony, wprowadza to funkcjonalną zależność od przekaźników Nostr: jeśli są one niedostępne, jakość działania ulega pogorszeniu. Ponadto, nawet jeśli wiadomości są szyfrowane, przekaźnik może obserwować pewien poziom metadanych aktywności.



Ważna jest również różnica w modelach bezpieczeństwa. Tailscale lub Tor zapewniają bezpośredni dostęp do węzła (za pośrednictwem API lub LND) chronionego wysoce wrażliwymi sekretami. Jest to potężne, ponieważ możesz zarządzać wszystkim, ale jest to również powierzchnia ataku niższej warstwy. W przypadku NWC dostęp jest bardziej aplikacyjny: delegujesz sesję token, która autoryzuje tylko określone działania.



### Zainstaluj Alby Hub na węźle Lightning



Wcześniej w sklepie Umbrel App Store dostępna była aplikacja przeznaczona specjalnie do połączeń NWC, ale niestety nie jest ona już dostępna. Aby ustanowić tego typu połączenie, należy teraz użyć Alby Hub. Aby to zrobić, zacznij od zainstalowania aplikacji Alby Hub bezpośrednio ze sklepu.



![Image](assets/fr/091.webp)



Po otwarciu pomiń ekrany wprowadzające, a następnie kliknij przycisk `Get Started (LND)`. Ważne jest, aby sprawdzić, czy w nawiasie jest napisane `LND`, a nie `LDK`. Jeśli pojawi się `LND`, oznacza to, że Alby Hub poprawnie wykrył istniejący węzeł Lightning i skonfiguruje się jako interfejs dla niego. Z drugiej strony, jeśli pojawi się `LDK`, oznacza to, że Alby Hub nie wykrył twojego węzła i ma zamiar utworzyć nowy, co nie jest tutaj celem.



![Image](assets/fr/092.webp)



Następnie użytkownik zostanie poproszony o założenie konta Alby. Nie jest to konieczne w przypadku korzystania wyłącznie z NWC, ale możesz chcieć to zrobić, jeśli chcesz skorzystać z określonych usług Alby. Jeśli nie, kliknij `Może później`, aby kontynuować.



![Image](assets/fr/093.webp)



Następnie wybierz silne, unikalne hasło. Będzie ono chronić dostęp do Alby Hub w węźle. Pamiętaj, aby zapisać je w menedżerze haseł.



![Image](assets/fr/094.webp)



Spowoduje to przejście do interfejsu Alby Hub. Nie musisz przechodzić przez cały proces konfiguracji, chyba że chcesz używać go jako głównego menedżera węzła Lightning. Jak widzieliśmy wcześniej, Alby Hub może w rzeczywistości zastąpić użycie ThunderHub do administrowania węzłem. Jeśli chcesz dowiedzieć się więcej o opcjach Alby Hub, zapoznaj się z naszym dedykowanym samouczkiem:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Przejdź do menu `Connections`.



![Image](assets/fr/095.webp)



Tutaj można zobaczyć wszystkie aplikacje, które mogą łączyć się z węzłem Lightning za pośrednictwem NWC. Należą do nich Zeus, wspomniany już w poprzednim rozdziale. Tutaj będziemy używać Alby Go. Kliknij Alby Go, a następnie przycisk `Connect to Alby Go`, aby rozpocząć proces łączenia.



![Image](assets/fr/096.webp)



### Instalowanie i podłączanie Alby Go



Na smartfonie zainstaluj aplikację Alby Go:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



W Alby Hub skonfiguruj prawa, które chcesz przyznać aplikacji Alby Go w węźle Lightning. Możesz na przykład ustawić limity wydatków na okres, datę wygaśnięcia łącza NWC lub pozostawić całkowitą kontrolę. Po ustawieniu parametrów kliknij przycisk `Next`.



![Image](assets/fr/097.webp)



Alby Hub następnie generates kod QR do ustanowienia połączenia NWC między węzłem Lightning i Alby Go.



![Image](assets/fr/098.webp)



W aplikacji Alby Go, po pierwszym otwarciu, kliknij na `Connect Wallet`, a następnie zeskanuj kod QR dostarczony przez Alby Hub.



![Image](assets/fr/099.webp)



Wybierz nazwę, aby zidentyfikować ten wallet. Masz teraz zdalny dostęp do węzła Lightning za pośrednictwem Alby Go. Możesz otrzymywać faktury generate do sats w swoim węźle lub ustawiać faktury Lightning bezpośrednio z nim.



![Image](assets/fr/100.webp)



Na przykład wysłałem 1543 sats z interfejsu Alby Go.



![Image](assets/fr/101.webp)



Jeśli przejdę do podstawowego interfejsu mojego węzła Lightning na Umbrel, zobaczę, że ta płatność rzeczywiście została dokonana przez mój węzeł.



![Image](assets/fr/102.webp)



Teraz wiesz, jak łatwo korzystać z węzła Lightning z dowolnego miejsca.



## Długotrwała autonomia na Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Doszliśmy do końca tego praktycznego kursu LNP202. Masz już podstawy potrzebne do suwerennego korzystania z Lightning Network: rozumiesz prawdziwą rolę węzła, kompromisy między różnymi podejściami i skonfigurowałeś instancję LND na Umbrel ze spójną strategią tworzenia kopii zapasowych i ochrony. Otworzyłeś również swoje pierwsze kanały, nauczyłeś się zarządzać płynnością, aby Twoje płatności były niezawodne każdego dnia.



Z operacyjnego punktu widzenia węzeł powinien teraz wejść w rytm konserwacji. Najważniejsze jest jego monitorowanie (czas pracy, synchronizacja, status kanału, awarie płatności itp.), stosowanie aktualizacji oferowanych przez Umbrel, gdy dostępne są stabilne wersje, oraz okresowe sprawdzanie, czy kopie zapasowe i konfiguracja watchtower są nadal aktywne.



Jeśli chodzi o kanały, przyjmij pragmatyczne podejście: zachowaj te, które są dla Ciebie przydatne, zamknij te, które są trwale nieaktywne lub powiązane z niestabilnymi partnerami i stopniowo realokuj swój kapitał w kierunku bardziej solidnej topologii.



**Jedną z najczęstszych pułapek na tym etapie jest przydzielenie zbyt dużej ilości kapitału do węzła Lightning. Należy pamiętać, że węzeł Lightning jest znacznie mniej bezpieczny niż sprzętowy wallet, a dostępność środków zaangażowanych w kanały zależy od mechanizmów tworzenia kopii zapasowych, które pozostają niedoskonałe. Dlatego bardzo ważne jest, aby trzymać się rozsądnych kwot, na których utratę można sobie pozwolić w przypadku problemu, i zawsze utrzymywać większość swoich sats na sprzętowym wallet onchain.



Jeśli chodzi o narzędzia, polecam pozostać ciekawym i uważnym na nowe rozwiązania. W tej sesji szkoleniowej odkryliśmy kilka z nich, zarówno do zarządzania węzłem, jego łącznością, jak i zdalnym wykorzystaniem do dokonywania płatności. Lightning jest jednak szczególnie dynamiczną dziedziną. Każdego roku pojawiają się nowe i istotne narzędzia, a wiele nowych aplikacji pojawia się również na Umbrel. Bycie na bieżąco z tymi nowościami może pozwolić ci odkryć bardziej wydajne lub bardziej praktyczne rozwiązania niż te przedstawione w tym kursie.



Na froncie edukacyjnym, jeśli jeszcze tego nie zrobiłeś, zdecydowanie radzę ci wziąć udział w kursie teoretycznym LNP 201 Fanisa Michalakisa, poświęconym działaniu Lightning Network. Pomoże ci on lepiej zrozumieć manipulacje wykonywane w tym kursie LNP202 i da ci większą pewność siebie w codziennym zarządzaniu węzłem.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

W innym duchu, ale równie istotnym dla twojej podróży bitcoinowej, polecam również doskonały kurs Ludovica Larsa na temat historii powstania Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Ale zanim przejdziesz dalej, możesz napisać recenzję tego kursu LNP202 i oczywiście uzyskać dyplom, aby potwierdzić, że zrozumiałeś całą jego zawartość.



# Część końcowa


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Recenzje i oceny


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Egzamin końcowy


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Wnioski


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>