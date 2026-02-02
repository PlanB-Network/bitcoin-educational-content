---
name: Zeus Swap
description: Usługa Exchange bez zatrzymania między bitcoinami On-Chain i Lightning Network
---

![cover](assets/cover.webp)



Ekosystem Bitcoin prezentuje dwoistość: główna sieć (On-Chain) oferuje maksymalne bezpieczeństwo, podczas gdy Lightning Network umożliwia natychmiastowe transakcje. Ta architektura dwóch Layer stwarza praktyczne wyzwanie: w jaki sposób można skutecznie przesyłać środki między tymi dwiema warstwami bez scentralizowanych pośredników?



Problem jest konkretny: otrzymujesz płatność Lightning, ale chcesz ją przechowywać w Cold, lub odwrotnie, masz bitcoiny On-Chain, ale potrzebujesz płynności Lightning. Tradycyjne rozwiązania obejmują ręczne otwieranie/zamykanie kanałów Lightning (kosztowne i techniczne) lub scentralizowane platformy wymagające KYC.



Zeus Swap rozwiązuje ten problem dzięki zautomatyzowanej usłudze Exchange bez powierzania środków. Opracowana przez Zeus LSP, pozwala na dwukierunkową konwersję bitcoinów On-Chain na satoshis Lightning, bez powierzania swoich środków pośrednikowi. Proces wykorzystuje kontrakty atomowe (HTLC) gwarantujące, że Exchange zostanie zakończony lub anulowany.



Innowacyjność polega na prostocie: wystarczy kilka kliknięć, aby uzyskać Exchange, który zachowuje suwerenność finansową, bez konieczności rejestracji lub KYC.



## Czym jest Zeus Swap?



Zeus Swap to usługa płynności Exchange opracowana przez Zeus LSP, która umożliwia atomowe swapy między główną siecią Bitcoin a Lightning Network. Jest to infrastruktura techniczna, która wykorzystuje swapy podmorskie i swapy odwrotne w celu ułatwienia dwukierunkowej konwersji między On-Chain BTC i Lightning satoshis, przy jednoczesnym zachowaniu niepowierniczego charakteru operacji.



### Architektura techniczna



Zeus Swap wykorzystuje technologię open-source Bitcoin/Lightning atomic swap firmy Boltz. Protokół wykorzystuje Hash Time Locked Contracts (HTLC): kontrakty blokujące środki z dwoma warunkami zwolnienia (ujawnienie tajemnicy kryptograficznej lub upływ czasu).



W przypadku wymiany podwodnej (On-Chain → Lightning) użytkownik wysyła bitcoiny do Address zawierającego Hash z Lightning Invoice. Zeus LSP odblokowuje te środki tylko poprzez opłacenie odpowiedniego Invoice, ujawniając obraz wstępny, który automatycznie odblokowuje bitcoiny. Mechanizm ten gwarantuje atomowość.



W przypadku zamiany odwrotnej (Lightning → On-Chain) użytkownik płaci Lightning Invoice z Zeus LSP, ujawniając obraz wstępny umożliwiający zwolnienie przygotowanej transakcji Bitcoin do docelowego Address.



Aby uzyskać więcej informacji na temat działania Lightning Network, zapoznaj się z naszym dedykowanym kursem:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Model biznesowy



Zeus LSP działa jako animator rynku, utrzymując płynność On-Chain i Lightning w celu honorowania swapów. W przypadku swapów Zeus stosuje zmienną opłatę (zazwyczaj od 0,1% do 0,5% w zależności od kierunku i warunków) plus opłatę Bitcoin Mining, wyświetlaną w przejrzysty sposób przed zatwierdzeniem.



Jako Lightning Service Provider, Zeus optymalizuje koszty dzięki swojej specjalistycznej wiedzy w zakresie otwierania kanałów na żądanie, wydajnego routingu i niestandardowych rozwiązań płynnościowych.



### Integracja



Zeus Wallet natywnie integruje usługę, umożliwiając wymianę bez opuszczania Interface Bitcoin/Lightning. Eliminuje to konieczność kopiowania i wklejania pomiędzy aplikacjami.



Niezależna sieć Interface pozostaje dostępna dla wszystkich portfeli, gwarantując maksymalną elastyczność użytkowania.



## Główne cechy



### Swapy dwukierunkowe



Zeus Swap oferuje dwa rodzaje Exchange:



**Zamiana okrętów podwodnych (On-Chain → Błyskawica)**: wstrzykuj płynność Błyskawicy z rezerw Bitcoin, przydatne do zasilania mobilnego Wallet lub węzła Błyskawicy bez ręcznego otwierania kanałów.



**Zamiana odwrotna (Lightning → On-Chain)**: zamiana satoshi Lightning na bitcoiny On-Chain w celu długoterminowego przechowywania, unikając kosztownego zamknięcia kanału.



### Interfejsy użytkownika



**Interface web** (swaps.zeuslsp.com): uproszczone doświadczenie bez rejestracji, proces z przewodnikiem z wyświetlaniem opłat i statusu w czasie rzeczywistym.



*integracja *Zeus Wallet**: bezpośrednia zamiana z poziomu aplikacji, automatyczne zarządzanie fakturami i adresami, eliminacja błędów obsługi.



### Bezpieczeństwo i odzyskiwanie



Każdy swap generuje unikalny Contract z niezmiennymi parametrami: Hash Lightning, timeout, zwrot Address. W przypadku awarii, automatyczne odzyskiwanie za pośrednictwem Address, niezależnie od Zeus LSP.



**Zeus Swaps Rescue Key**: podczas wymiany On-Chain → Lightning, Zeus automatycznie generuje uniwersalny klucz odzyskiwania zastępujący stare indywidualne pliki zwrotu. Ten unikalny klucz działa na każdym urządzeniu i dla wszystkich swapów utworzonych za jego pomocą. Ważne jest, aby pobrać i zapisać ten klucz w bezpiecznym miejscu, aby móc odzyskać środki w przypadku niepowodzenia wymiany.



### Optymalizacja sieci



Zeus Swap automatycznie dostosowuje czasy wygaśnięcia i opłaty Mining w zależności od warunków sieciowych. Użytkownicy Zeus korzystają z zaawansowanych opcji: wybór LSP, niestandardowe opóźnienia, kompatybilność z innymi usługami (Boltz).



## Instalacja i użytkowanie



### Metody dostępu



**Interface web** (swaps.zeuslsp.com): uniwersalne rozwiązanie kompatybilne ze wszystkimi portfelami, nie wymaga instalacji, idealne do okazjonalnego użytku.



**Aplikacja Zeus** (iOS/Android): zintegrowane doświadczenie łączące Wallet i swapy, odpowiednie dla zwykłych użytkowników.



Zobacz nasz samouczek Zeus, aby dowiedzieć się więcej o tym kompletnym Wallet :



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Konfiguracja sieciowa



**On-Chain → Lightning**: Proces rozpoczyna się od skonfigurowania zamiany w Interface web Zeus Swap. Użytkownik może użyć strzałki między polami On-Chain i Lightning, aby odwrócić kierunek zamiany.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: wybór kwoty (Sats 50,000 → Sats 49,648 po opłatach) z przejrzystym wyświetlaniem opłat sieciowych (Sats 302) i usługi Zeus (Sats 50).*



Podczas tego procesu Zeus oferuje pobranie uniwersalnego klucza odzyskiwania:



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Okno dialogowe pobierania klucza ratunkowego Zeus Swaps - uniwersalnego klucza, który zastępuje stare indywidualne pliki zwrotu kosztów*



Jeśli użytkownik posiada już klucz, Zeus umożliwia jego sprawdzenie:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface, aby sprawdzić ważność istniejącego klucza ratunkowego Zeus Swaps*



Po skonfigurowaniu Zeus generuje skład Bitcoin Address i wyświetla instrukcje :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Strona zakończenia wymiany: Kod QR i Bitcoin Address za wysłanie 50 000 Satss, z przypomnieniem o 24-godzinnej dacie wygaśnięcia*



Następnie swap czeka na potwierdzenie Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Status "Transakcja w Mempool" - oczekiwanie na potwierdzenie Bitcoin w celu sfinalizowania wymiany*



Po potwierdzeniu zamiana zostanie zakończona automatycznie:



![Swap réussi](assets/fr/06.webp)



*Potwierdzenie sukcesu: 49 648 Sats otrzymanych na Lightning po odliczeniu opłat sieciowych i serwisowych*



### Korzystanie z aplikacji Zeus



**Lightning → On-Chain**: Aplikacja Zeus oferuje zintegrowane doświadczenie dla swapów zwrotnych (Lightning do Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Ekran główny Zeusa pokazujący salda Lightning (69 851 Sats) i On-Chain (38 018 Sats), dostęp do swapów przez menu boczne*



![Configuration du swap reverse](assets/fr/08.webp)



*Utworzenie odwrotnej zamiany Interface: 50,000 Sats Lightning → 49,220 Sats On-Chain, z wyraźnie wyświetlanymi opłatami sieciowymi (530 Sats) i usługowymi (250 Sats). Użytkownicy mogą ręcznie wprowadzić Bitcoin odbierający Address lub generate automatycznie z Wallet Zeus za pomocą przycisku "generate On-Chain Address"



![Finalisation du swap mobile](assets/fr/09.webp)



*Ekrany finalizacji: Ekran płatności Lightning Invoice z komunikatem "ZAPŁAĆ TEN Invoice", potwierdzenie pomyślnej płatności Lightning w 9,96 sekundy oraz zestawienie salda z 49 162 Sats oczekującymi na potwierdzenie*



### Nadzór i bezpieczeństwo



Każdy swap posiada unikalny identyfikator z możliwością śledzenia w czasie rzeczywistym. Wyświetlanie pełnego postępu, automatyczne powiadomienia o datach wygaśnięcia. Automatyczne zalecenia dotyczące ładowania w zależności od warunków sieciowych.



## Zalety i ograniczenia



### Korzyści





- Prostota**: Zamiana za pomocą kilku kliknięć w porównaniu z ręczną manipulacją kanałami
- Non-custodial**: brak KYC, brak konta, środki nigdy nie powierzone stronie trzeciej
- Przejrzystość**: opłaty wyraźnie wyświetlane przed walidacją (od 0,1% do 0,5% + min. w zależności od testów użytkowników - sprawdź aktualne opłaty przy każdym swapie)
- Integracja mobilna**: natywne doświadczenie w Zeus Wallet



### Ograniczenia





- Czas ważności**: maksymalnie 24-48 godzin, awaria, jeśli Bitcoin nie zostanie potwierdzony na czas
- Limity kwotowe**: minimum 25 000 Sats, płynność Zeus LSP zmienna w zależności od warunków
- Ślady On-Chain**: Skrypty HTLC potencjalnie identyfikowalne przez analizę Blockchain
- Wymagane potwierdzenie**: minimum 10 minut na zatwierdzenie Bitcoin



## Najlepsze praktyki



### Harmonogram i koszty





- Obserwuj Mempool.space w okresach niskiego natężenia ruchu
- Preferowane weekendy i godziny poza szczytem, aby obniżyć koszty Mining
- Oblicz rentowność: małe kwoty vs. bezpośrednie otwarcie kanału



### Bezpieczeństwo





- Sprawdź dokładnie adresy Bitcoin (zalecane kopiuj-wklej)
- Utwórz kopię zapasową klucza ratunkowego Zeus Swaps**: pobierz i przechowuj klucz ratunkowy w bezpiecznym miejscu
- Dokument: Contract ID, zwrot Address, data ważności
- Użyj odpowiednich opłat Mining w celu terminowego potwierdzenia



### Strategia użytkowania





- Zrównoważona płynność On-Chain/Lightning dostosowana do Twoich potrzeb
- Zeus Swap dla jednorazowych dostosowań, bezpośrednie kanały dla stałych potrzeb



## Porównanie z innymi usługami swapowymi



### Zeus Swap vs Boltz Exchange



Zeus Swap wykorzystuje technologię backendową Boltz, ale wprowadza kilka kluczowych ulepszeń:



**Korzyści płynące ze swapu Zeus** :




- Interface unified**: natywna integracja w Zeus Wallet vs Interface web technique Boltz
- WebSocket API**: aktualizacje w czasie rzeczywistym vs. ręczne odpytywanie
- Zautomatyzowane zarządzanie**: automatyczne rozliczanie i zarządzanie Address
- Wsparcie mobilne**: tylko optymalizacja pod kątem smartfonów i komputerów stacjonarnych
- Dokumentacja Swagger**: kompletny interfejs API REST dla deweloperów



**Boltz pozostaje korzystny** dla całkowitej niezależności i użytkowania z dowolną konfiguracją Bitcoin/Lightning.



Zeus Swap przekształca sprawdzoną technologię Boltz w główne doświadczenie użytkownika, porównywalne do różnicy między surowym protokołem a przyjazną dla użytkownika aplikacją.



### Zeus Swap vs Phoenix/Breez (zintegrowane swapy)



Phoenix i Breez integrują przezroczyste funkcje wymiany, które ukrywają złożoność techniczną przed użytkownikiem końcowym. Phoenix wykorzystuje automatyczny system swap-in/swap-out, w którym użytkownik nie rozróżnia wyraźnie warstw Bitcoin: "wysyła do Bitcoin Address", a aplikacja obsługuje zamianę w tle.



To bardzo uproszczone podejście doskonale nadaje się dla początkujących, ale ogranicza zrozumienie i kontrolę operacji. Zeus Swap przyjmuje bardziej edukacyjną filozofię: użytkownicy rozumieją, że zamieniają się między dwiema odrębnymi warstwami, stopniowo rozwijając swoje zrozumienie ekosystemu dwóch Layer Bitcoin.



## Szczegółowe porównanie opłat i limitów (2024)



⚠️ **Ostrzeżenie**: Opłaty mogą zmieniać się w czasie w zależności od warunków rynkowych i aktualizacji usług. Przed zatwierdzeniem wymiany należy zawsze sprawdzić opłaty wyświetlane w Interface.




| Usługa | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Kwota minimalna |
| ------------- | ----------------------- | --------------------- | --------------- |
| **Zeus Swap** | ~0.1% + opłaty za mining | 0.5% + opłaty za mining | 25 000 sats |
| **Boltz** | 0.2% + opłaty za mining | 0.5% + opłaty za mining | 50 000 sats |
| **Phoenix** | Tylko opłaty za mining | 0.4% stałe | 10 000 sats |
| **Breez** | 0.25% + opłaty sieciowe | 0.5% + opłaty za mining | 50 000 sats |

Zeus Swap oferuje równowagę między łatwością użytkowania a kontrolą techniczną: bardziej przystępny niż Boltz, bardziej elastyczny niż Phoenix/Breez, z rygorystycznym podejściem bez nadzoru.



## Wnioski



Zeus Swap stanowi znaczącą innowację w ekosystemie Bitcoin, elegancko rozwiązując wyzwanie interoperacyjności między siecią główną a Lightning Network. Łącząc kryptograficzną solidność atomowych swapów z dostępnym doświadczeniem użytkownika, usługa ta demokratyzuje zarządzanie Bitcoin dual-Layer bez naruszania zasad suwerenności finansowej.



Architektura Zeus Swap, odziedziczona po sprawdzonej technologii Boltz, zapewnia, że środki użytkownika pozostają pod jego wyłączną kontrolą przez cały proces wymiany. Podejście to respektuje ducha Bitcoin, oferując jednocześnie wygodę użytkownika wymaganą do przyjęcia do głównego nurtu. Przejrzystość cen i brak procesów KYC wzmacniają tę wyjątkową propozycję wartości.



Dla nowoczesnego użytkownika Bitcoin, Zeus Swap jest strategicznym narzędziem do optymalizacji dystrybucji płynności zgodnie z potrzebami: On-Chain bezpieczne przechowywanie dla długoterminowych oszczędności, Błyskawiczna dostępność dla codziennych wydatków i mikrotransakcji. Ta elastyczność przekształca zarządzanie Bitcoin z ograniczenia technicznego w przewagę konkurencyjną.



Przyszła ewolucja Zeus Swap, wspierana przez doświadczony zespół Zeus LSP i społeczność open-source Boltz, obiecuje dalsze ulepszenia w zakresie kosztów, czasu przetwarzania i doświadczenia użytkownika. Usługa ta jest częścią szerszego trendu w kierunku dojrzewania infrastruktury Bitcoin, gdzie zaawansowanie techniczne staje się przejrzyste dla użytkownika końcowego.



## Zasoby



### Oficjalna dokumentacja




- [Zeus Swap - portal internetowy](https://swaps.zeuslsp.com)
- [Zeus Wallet - Aplikacja mobilna](https://zeusln.app)
- [Blog Zeus - Ogłoszenia i poradniki](https://blog.zeusln.com)
- [Dokumentacja techniczna Zeus](https://docs.zeusln.app)



### Społeczność i wsparcie




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)