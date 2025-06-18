---
name: Robosats

description: Jak korzystać z Robosatów
---

![cover](assets/cover.webp)


RoboSats (https://learn.robosats.com/) to łatwy sposób na prywatne Exchange Bitcoin dla walut krajowych. Upraszcza on obsługę peer-to-peer i wykorzystuje błyskawiczne przechowywanie faktur, aby zminimalizować wymagania dotyczące przechowywania i zaufania.


![video](https://youtu.be/XW_wzRz_BDI)


## Przewodnik


**Uwaga:** Ten przewodnik pochodzi od Bitocin Q&A (https://bitcoiner.guide/robosats/). Cała zasługa dla niego, możesz go wesprzeć [tutaj](https://bitcoiner.guide/contribute); BitcoinQ&A jest również mentorem Bitcoin. Skontaktuj się z nim w sprawie mentoringu!


![image](assets/0.webp)


RoboSats - Prosty i prywatny P2P Exchange oparty na technologii Lightning


## Przed rozpoczęciem


### Rzeczy, które musisz wiedzieć


| Jargon       | Definition                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Your automatically generated private trade identity. Do not re-use the same robot more than once as this can degrade your privacy.                                                             |
| Token        | A string of random characters used to generate your unique robot.                                                                                                                              |
| Maker        | A user who creates an offer to buy or sell Bitcoin.                                                                                                                                            |
| Taker        | A user who takes another user up on their offer to buy or sell Bitcoin.                                                                                                                        |
| Bond         | An amount of Bitcoin locked up by both peers as a pledge to play fair and complete their part of the trade. Bonds are typically 3% of the total trade amount and are powered by Hodl Invoices. |
| Trade Escrow | Used by the seller as a method of holding the trade amount of Bitcoin, again using Hodl Invoices.                                                                                              |
| Fees         | RoboSats charges 0.2% of the trade amount, which is split between both maker and taker. The taker pays 0.175% and the maker pays 0.025%.                                                       |

## Rzeczy, które musisz mieć


### A Lightning Wallet


RoboSats jest natywny dla Lightning, więc będziesz potrzebować Wallet Lightning, aby sfinansować obligację i otrzymać zakupiony Sats jako kupujący. Należy zachować ostrożność przy wyborze Wallet, ponieważ ze względu na technologię używaną do działania RoboSats, nie wszystkie są kompatybilne.


Jeśli jesteś node runnerem, Zeus jest zdecydowanie najlepszą opcją. Jeśli nie masz własnego węzła, gorąco polecam Phoenix, wieloplatformowy mobilny Wallet z prostą konfiguracją i dostępem do Lightning. Phoenix został wykorzystany w produkcji tego przewodnika.


### Niektóre Bitcoin


Kupujący i sprzedający muszą sfinansować obligację, zanim jakakolwiek transakcja będzie mogła mieć miejsce. Zwykle jest to bardzo niewielka kwota (~3% kwoty transakcji), ale mimo to jest to warunek wstępny.


Korzystasz z RoboSats, aby kupić swój pierwszy Sats? Dlaczego nie poprosić znajomego o pożyczenie niewielkiej kwoty wymaganej do rozpoczęcia gry? Jeśli lecisz sam, oto kilka innych świetnych opcji, aby uzyskać Sats noKYC na dobry początek.


### Dostęp do RoboSatów


Oczywiście będziesz musiał uzyskać dostęp do RoboSats! Można to zrobić na cztery główne sposoby:


1. Przez przeglądarkę Tor (zalecane!)

2. Przez zwykłą przeglądarkę internetową (niezalecane!)

3. Poprzez Android APK

4. Twój własny klient


Jeśli dopiero zaczynasz korzystać z przeglądarki Tor, dowiedz się więcej i pobierz ją [tutaj] (https://www.torproject.org/download/).


Krótka uwaga dla użytkowników iOS, którzy chcą uzyskać dostęp do RoboSats przez Tor ze swoich telefonów. "Onion Browser" nie jest przeglądarką Tor. Zamiast tego użyj Orbot + Safari i Orbot + DuckDuckGo.


## Zakup Bitcoin


Poniższe kroki zostały przeprowadzone w maju 2023 r. przy użyciu wersji 0.5.0, dostępnej za pośrednictwem przeglądarki Tor. Kroki powinny być identyczne dla użytkowników uzyskujących dostęp do RoboSats za pośrednictwem Android APK.


W chwili pisania tego tekstu RoboSats jest nadal w fazie aktywnego rozwoju, więc Interface może się nieco zmienić w przyszłości, ale podstawowe kroki wymagane do ukończenia transakcji powinny pozostać w dużej mierze niezmienione.


**Uwaga:** po pierwszym załadowaniu RoboSats pojawi się ta strona docelowa. Kliknij Start.


![image](assets/2.webp)


generate token i przechowuj go w bezpiecznym miejscu, takim jak zaszyfrowana aplikacja do notatek lub menedżer haseł. Token ten może zostać wykorzystany do odzyskania tymczasowego identyfikatora robota w przypadku zamknięcia przeglądarki lub aplikacji w połowie transakcji.


![image](assets/3.webp)


Poznaj swoją nową tożsamość robota, a następnie kliknij Kontynuuj.


![image](assets/4.webp)


Kliknij Oferty, aby przeglądać książkę zamówień. W górnej części strony możesz filtrować według własnych preferencji. Pamiętaj, aby zwrócić uwagę na procent obligacji i premię w stosunku do średniej stawki Exchange.



- Wybierz tag "Kup
- Wybierz walutę
- Wybierz metody płatności


![image](assets/5.webp)


**Uwaga:** kliknij ofertę, z której chcesz skorzystać. Wprowadź kwotę (w wybranej walucie fiducjarnej), którą chcesz kupić od sprzedawcy, a następnie sprawdź szczegóły i kliknij "Przyjmij zamówienie".


Jeśli sprzedawca nie jest online (oznaczony czerwoną kropką na zdjęciu profilowym), zobaczysz ostrzeżenie, że transakcja może potrwać dłużej niż zwykle. Jeśli będziesz kontynuować transakcję, a sprzedawca nie przystąpi do niej na czas, otrzymasz rekompensatę w wysokości 50% kwoty kaucji za zmarnowany czas.


![image](assets/6.webp)


Następnie musisz zablokować obligację handlową, płacąc Invoice na ekranie. Jest to Invoice, który zostaje zamrożony w Wallet. Zostanie on naliczony tylko wtedy, gdy nie uda ci się sfinalizować transakcji.


![image](assets/7.webp)


W swoim Lightning Wallet zeskanuj kod QR i zapłać Invoice.


![image](assets/8.webp)


Następnie wpisz w swoim Lightning Wallet generate i Invoice pokazaną kwotę i wklej w odpowiednie miejsce.


![image](assets/9.webp)


Poczekaj, aż sprzedawca zablokuje kwotę transakcji. Gdy to nastąpi, RoboSats automatycznie przejdzie do następnego kroku, w którym otworzy się okno czatu. Przywitaj się i poproś sprzedawcę o informacje dotyczące płatności fiat. Po ich podaniu wyślij płatność wybraną metodą, a następnie potwierdź ją w RoboSats. Cały czat w RoboSats jest szyfrowany PGP, co oznacza, że tylko Ty i Twój partner handlowy możecie czytać wiadomości.


![image](assets/10.webp)


Gdy sprzedawca potwierdzi otrzymanie płatności, RoboSats automatycznie zwolni płatność za pomocą podanego wcześniej Invoice.


![image](assets/11.webp)


Po opłaceniu Invoice transakcja zostaje zakończona, a obligacja odblokowana. Następnie zobaczysz podsumowanie transakcji.


![image](assets/12.webp)


Sprawdź urządzenie Lightning Wallet, aby uzyskać potwierdzenie, że urządzenie Sats zostało dostarczone.


![image](assets/13.webp)


## Dodatkowe funkcje


Oprócz oczywistego kupowania i sprzedawania Bitcoin, RoboSats ma kilka innych funkcji, o których powinieneś wiedzieć.

Robot Garage


Chcesz mieć wiele transakcji w tym samym czasie, ale nie chcesz udostępniać im tej samej tożsamości? Nie ma problemu! Kliknij zakładkę Robot, generate dodatkowego Robota i utwórz lub przyjmij kolejne zlecenie.


![image](assets/14.webp)


### Tworzenie zamówień


Oprócz skorzystania z czyjejś oferty, możesz stworzyć własną i poczekać, aż inny Robot sam się do Ciebie zgłosi.



- Otwórz stronę Utwórz.
- Określ, czy Twoje zlecenie ma na celu kupno czy sprzedaż Bitcoin.
- Wprowadź kwotę i walutę, za pomocą której chcesz kupować/sprzedawać.
- Wprowadź metody płatności, których chcesz użyć.
- Wprowadź wartość procentową "Premii ponad rynek", którą jesteś skłonny zaakceptować. Należy pamiętać, że może to być wartość ujemna, aby złożyć ofertę ze zniżką w stosunku do bieżącej ceny rynkowej.
- Kliknij przycisk Utwórz zamówienie.
- Zapłać Piorunowi Invoice, aby zablokować Obligację Twórcy.
- Twoje zamówienie jest teraz aktywne. Usiądź wygodnie i poczekaj, aż ktoś je zaakceptuje.


![image](assets/15.webp)


### Wypłaty On-Chain


RoboSats koncentruje się na Lightning, ale kupujący mają możliwość otrzymania Sats do On-Chain Bitcoin Address. Kupujący mogą wybrać tę opcję po zablokowaniu obligacji. Po wybraniu On-Chain kupujący zobaczy przegląd opłat. Dodatkowe opłaty za tę usługę obejmują:



- Opłata za wymianę pobierana przez RoboSats - ta opłata jest dynamiczna i zmienia się w zależności od obciążenia sieci Bitcoin.
- Opłata Mining za transakcję wypłaty - jest konfigurowana przez kupującego.


![image](assets/16.webp)


### P2P Swapy


RoboSats umożliwia użytkownikom wymianę Sats na lub z ich Lightning Wallet. Wystarczy kliknąć przycisk wymiany u góry strony z ofertami, aby wyświetlić aktualne oferty wymiany.


Jako nabywca oferty "Swap In" wysyłasz On-Chain Bitcoin do partnera i otrzymujesz Sats z powrotem, pomniejszony o reklamowane opłaty i/lub premie, do swojego Wallet Lightning. Jako nabywca oferty "Swap Out" wysyłasz Sats za pośrednictwem Lightning i otrzymujesz Bitcoin, pomniejszony o wszelkie opłaty i/lub premie, do swojego On-Chain Address. Użytkownicy Samourai lub Sparrow Wallet mogą również skorzystać z funkcji Stowaway, aby dokończyć wymianę.


Oferty swapowe RoboSats mogą również obejmować powiązane alternatywy dla Bitcoin, które obejmują RBTC, LBTC i WBTC. Należy zachować szczególną ostrożność podczas interakcji z tymi tokenami, ponieważ wszystkie one wiążą się z różnymi kompromisami. Pegged Bitcoin to nie Bitcoin!


![image](assets/17.webp)


### Uruchom własnego klienta RoboSats


Operatorzy węzłów Umbrel, Citadel i Start9 mogą zainstalować własnego klienta RoboSats bezpośrednio na swoim węźle. Korzyści z tego są następujące:



- Znacznie krótsze czasy ładowania.
- Bezpieczniej: kontrolujesz, jaką aplikację kliencką RoboSats uruchamiasz.
- Uzyskaj bezpieczny dostęp do RoboSats z dowolnej przeglądarki / urządzenia. Nie ma potrzeby korzystania z TOR, jeśli jesteś w sieci lokalnej lub korzystasz z VPN: backend węzła obsługuje toryfikację potrzebną do anonimizacji.
- Umożliwia kontrolowanie koordynatora rynku P2P, z którym się łączysz (domyślnie robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)


![image](assets/18.webp)


## FAQ


### Czy mogę zostać oszukany?


Jako kupujący, jeśli wysłałeś fiat wymagany dla Twojej strony transakcji, ale sprzedawca nie zwolnił Sats, możesz otworzyć spór. Jeśli w trakcie procesu sporu udowodnisz arbitrom RoboSats, że wysłałeś fiat, środki escrowed sprzedawcy i jego zabezpieczenie handlowe zostaną ci zwrócone.

Jak anulować transakcję?


Możesz anulować transakcję po zaksięgowaniu obligacji, klikając przycisk Collaborative Cancel w menu transakcji. Jeśli Twój partner handlowy wyrazi zgodę na anulowanie, nie poniesiesz żadnych opłat. Jeśli jednak Twój partner handlowy chce sfinalizować transakcję, a Ty i tak ją anulujesz, stracisz swoje zabezpieczenie handlowe.


### Czy RoboSats współpracuje z metodą płatności "X"?


W RoboSats nie ma ograniczeń co do metod płatności. Jeśli nie widzisz żadnych ofert w wybranej przez siebie metodzie, stwórz własną ofertę przy jej użyciu!


![image](assets/19.webp)


### Czego RoboSats dowiaduje się o mnie, gdy z niego korzystam?


Jeśli korzystasz z RoboSats przez Tor lub aplikację na Androida, to nic! Więcej informacji tutaj.



- Tor chroni prywatność w sieci.
- Szyfrowanie PGP zapewnia prywatność czatu handlowego.
- Brak kont oznacza jednego robota na transakcję. Oznacza to, że RoboSats nie może skorelować wielu transakcji z jednym podmiotem.


Istnieją jednak pewne zastrzeżenia! Lightning jest dość prywatny jako nadawca, ale nie jako odbiorca. Jeśli odbierasz do własnego węzła Lightning, identyfikator węzła jest udostępniany na fakturach. Ten identyfikator węzła daje każdemu, kto go zna, punkt wyjścia do próby powiązania aktywności On-Chain. Dotyczy to również sytuacji, gdy użytkownik zdecyduje się na otrzymywanie transakcji za pośrednictwem wypłaty On-Chain.


Aby złagodzić ten problem, użytkownicy mogą zdecydować się na użycie rozwiązania takiego jak Proxy Wallet dla Lightning lub CoinJoin dla On-Chain.


### Federacja


Obecnie istnieje jeden koordynator RoboSats obsługiwany przez zespół programistów RoboSats. W Bitcoin każda forma centralizacji stanowi łatwiejszy cel dla rządów lub organów regulacyjnych, które mogą nie patrzeć przychylnie na konkretną usługę.


Ponieważ RoboSats jest projektem Open Source, każdy może pobrać kod i uruchomić własnego koordynatora. Chociaż w pewnym stopniu decentralizuje to ryzyko z dala od pojedynczego celu, to również osłabia i tak już cienki rynek płynności.


Zespół RoboSats zdaje sobie z tego sprawę i rozpoczął prace nad modelem federacyjnym. Jako użytkownik końcowy nie powinno to znacząco zmienić przedstawionego powyżej przepływu handlu, ale pojawią się dodatkowe widoki lub ekrany umożliwiające dodawanie lub usuwanie różnych koordynatorów.


KONIEC przewodnika

https://bitcoiner.guide/robosats/