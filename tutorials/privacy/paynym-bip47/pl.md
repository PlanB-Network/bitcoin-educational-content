---
name: BIP47 - PayNym

description: Jak działa PayNyms
---
***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, aplikacja nie może być już używana przez użytkowników, którzy nie mają własnego Dojo. BIP47 pozostaje użyteczny na Sparrow Wallet dla wszystkich użytkowników i **na Samourai Wallet tylko dla użytkowników posiadających Dojo**


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> "Jest za duży", powiedziały wszystkie, a kogut indyk, który urodził się z ostrogami i myślał, że jest cesarzem, spuchł jak statek z postawionymi żaglami i pomaszerował prosto na niego z wielką wściekłością, a jego oczy były czerwone jak ogień. Biedne małe kaczątko nie wiedziało, czy się bronić, czy uciekać, i było bardzo nieszczęśliwe, ponieważ było pogardzane przez wszystkie kaczki na podwórku.

![BIP47, the ugly duckling illustration](assets/1.webp)


Jednym z najważniejszych problemów protokołu Bitcoin jest ponowne wykorzystanie Address. Przejrzystość i dystrybucja sieci sprawiają, że praktyka ta jest niebezpieczna dla prywatności użytkowników. Aby uniknąć problemów z tym związanych, zaleca się użycie nowego pustego odbiorczego Address dla każdej nowej płatności przychodzącej do Wallet, co może być skomplikowane do osiągnięcia w niektórych przypadkach.


Ten kompromis jest tak stary jak Biała Księga. Satoshi już ostrzegał nas przed tym ryzykiem w swojej pracy opublikowanej pod koniec 2008 roku:


> Jako dodatkowy firewall, dla każdej transakcji powinna być używana nowa para kluczy, aby zapobiec powiązaniu ich ze wspólnym właścicielem.

Istnieje wiele rozwiązań umożliwiających otrzymywanie wielu płatności bez ponownego użycia Address. Każde z nich ma swoje kompromisy i wady. Wśród tych wszystkich rozwiązań znajduje się [BIP47](https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki), propozycja opracowana przez Justusa Ranviera i opublikowana w 2015 r., która pozwala na generowanie kodów płatności wielokrotnego użytku. Jego celem jest umożliwienie dokonywania wielu transakcji na rzecz tej samej osoby bez ponownego wykorzystywania Address.


Początkowo propozycja ta spotkała się z pogardą części społeczności i nigdy nie została dodana do Bitcoin Core. Jednak niektóre programy nadal zdecydowały się zaimplementować ją na własną rękę. Na przykład, Samourai Wallet opracował własną implementację BIP47: PayNym. Obecnie ta implementacja jest dostępna w Samourai Wallet dla smartfonów, a także w [Sparrow Wallet](https://sparrowwallet.com/) dla komputerów PC.


Z biegiem czasu Samourai zaprogramował nowe funkcje bezpośrednio związane z PayNym. Obecnie dostępny jest cały ekosystem narzędzi do optymalizacji prywatności użytkowników w oparciu o PayNym i BIP47.

W tym artykule poznasz zasadę działania BIP47 i PayNym, mechanizmy tych protokołów oraz praktyczne zastosowania, które z nich wynikają. W Address przedstawię tylko pierwszą wersję BIP47, która jest obecnie używana w PayNym, ale wersje 2, 3 i 4 działają praktycznie w ten sam sposób.


**Uwaga**, że jedyną istotną różnicą jest transakcja powiadomienia:


- Wersja 1 wykorzystuje prosty Address z OP_RETURN do powiadamiania,
- Wersja 2 wykorzystuje skrypt Multisig (bloom-Multisig) z OP_RETURN,
- Wersje 3 i 4 używają po prostu skryptu Multisig (cfilter-Multisig).


Mechanizmy omówione w tym artykule, w tym badane metody kryptograficzne, mają zatem zastosowanie do wszystkich czterech wersji. Do tej pory implementacja PayNym na Samourai Wallet i Sparrow wykorzystuje pierwszą wersję BIP47.


## Podsumowanie:


1- Problem ponownego użycia Address.


2- Zasady BIP47 i PayNym.


3- Samouczki: Korzystanie z PayNym.



- Budowanie transakcji BIP47 z Samourai Wallet.
- Budowanie transakcji BIP47 za pomocą Sparrow Wallet.


4- Działanie BIP47.



- Kod płatności wielokrotnego użytku.
- Metoda kryptograficzna: Klucz Diffie-Hellmana Exchange ustanowiony na krzywych eliptycznych (ECDH).
- Transakcja powiadomienia.
- Konstruowanie transakcji powiadomienia.
- Odbieranie transakcji powiadomienia.
- Transakcja płatnicza BIP47.
- Otrzymanie płatności BIP47 i uzyskanie klucza prywatnego.
- Zwrot płatności za BIP47.


5- Pochodne zastosowania PayNym.


6- Moja osobista opinia na temat BIP47.


## Problem ponownego użycia Address.


Odbierający Address służy do odbierania bitcoinów. Jest on generowany z klucza publicznego poprzez haszowanie i zastosowanie określonego formatu. Pozwala to na utworzenie nowego warunku wydania monety w celu zmiany jej właściciela.


Aby dowiedzieć się więcej o generowaniu Address, polecam przeczytać ostatnią część tego artykułu: **Bitcoin Wallet - fragment** [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).


Co więcej, prawdopodobnie słyszałeś już od doświadczonego bitcoinera, że adresy odbiorcze są przeznaczone do jednorazowego użytku i że powinieneś generate nowy dla każdej nowej płatności przychodzącej do twojego Wallet. No dobrze, ale dlaczego?


Zasadniczo, ponowne użycie Address nie zagraża bezpośrednio funduszom użytkownika. Zastosowanie kryptografii na krzywych eliptycznych pozwala udowodnić sieci, że jesteś w posiadaniu klucza prywatnego bez ujawniania tego klucza. W związku z tym można zablokować wiele różnych UTXO (Unspent Transaction Outputs) na tym samym Address i wydać je w różnym czasie. Jeśli nie ujawnisz klucza prywatnego powiązanego z tym Address, nikt nie będzie mógł uzyskać dostępu do Twoich środków. Kwestia ponownego użycia Address jest bardziej związana z prywatnością.


Jak wspomniano we wstępie, przejrzystość i dystrybucja sieci Bitcoin oznacza, że każdy użytkownik z dostępem do węzła może obserwować transakcje systemu płatności. W rezultacie mogą zobaczyć różne salda adresów. Następnie Satoshi Nakamoto wspomniał o możliwości generowania nowych par kluczy, a tym samym nowych adresów, dla każdej nowej płatności przychodzącej do Wallet. Celem byłoby posiadanie dodatkowej zapory ogniowej w przypadku powiązania tożsamości użytkownika z jedną z jego par kluczy.


Dziś, wraz z obecnością firm zajmujących się analizą sieci i rozwojem KYC (Know Your Customer), korzystanie z pustych adresów nie jest już dodatkowym firewallem, ale obowiązkiem dla każdego, kto choć trochę dba o swoją prywatność.


Dążenie do prywatności nie jest wygodą ani fantazją Maximalist Bitcoiners. Jest to konkretny parametr, który bezpośrednio wpływa na bezpieczeństwo osobiste i bezpieczeństwo środków. Aby pomóc ci to zrozumieć, oto bardzo konkretny przykład:



- Bob kupuje Bitcoin poprzez Dollar Cost Averaging (DCA), co oznacza, że nabywa niewielką ilość Bitcoin w regularnych odstępach czasu, aby uśrednić swoją cenę wejścia. Bob systematycznie wysyła zakupione środki do tego samego odbierającego Address. Co tydzień kupuje 0,01 Bitcoin i wysyła je do tego samego Address. Po dwóch latach Bob zgromadził cały Bitcoin na tym Address.
- Piekarz na rogu akceptuje płatności Bitcoin. Podekscytowany możliwością wydania Bitcoin, Bob idzie kupić bagietkę w satoshis. Aby zapłacić, używa środków zablokowanych w Address. Jego piekarz wie teraz, że posiada Bitcoin. Tak znaczna kwota może wzbudzić zazdrość, a Bob może być narażony na fizyczny atak w przyszłości.


Ponowne użycie Address pozwala obserwatorowi na niezaprzeczalne powiązanie między różnymi UTXO, a czasami między tożsamością a całym Wallet.

Dlatego większość oprogramowania Bitcoin Wallet automatycznie generuje nowy adres odbiorczy Address po kliknięciu przycisku "Odbierz". Dla zwykłych użytkowników przyzwyczajenie się do korzystania z nowych adresów nie jest dużą niedogodnością. Jednak w przypadku biznesu online, Exchange lub kampanii darowizn, to ograniczenie może szybko stać się nie do opanowania.

Istnieje wiele rozwiązań dla tych organizacji. Każde z nich ma swoje zalety i wady, ale do tej pory, i jak zobaczymy później, BIP47 naprawdę wyróżnia się na tle innych.


Kwestia ponownego wykorzystania Address jest daleka od nieistotnej w Bitcoin. Jak widać na poniższym wykresie zaczerpniętym ze strony internetowej oxt.me, ogólny wskaźnik ponownego wykorzystania Address przez użytkowników Bitcoin wynosi obecnie 52%:

Wykres z OXT.me pokazujący ewolucję ogólnego wskaźnika ponownego wykorzystania Address w sieci Bitcoin.


![image](assets/2.webp)

kredyt: OXT_


Większość tych ponownych użyć pochodzi z giełd, które ze względu na wydajność i wygodę wielokrotnie używają tego samego Address. Do tej pory BIP47 byłby najlepszym rozwiązaniem, aby powstrzymać to zjawisko wśród giełd. Pomogłoby to zmniejszyć ogólny wskaźnik ponownego wykorzystania Address bez powodowania zbyt dużych tarć dla tych podmiotów.


Ten globalny środek w całej sieci jest szczególnie istotny w tym przypadku. Rzeczywiście, ponowne wykorzystanie Address stanowi problem nie tylko dla osoby, która angażuje się w tę praktykę, ale także dla każdego, kto dokonuje z nią transakcji. Utrata prywatności na Bitcoin działa jak wirus, rozprzestrzeniając się od użytkownika do użytkownika. Badanie globalnej miary wszystkich transakcji sieciowych pozwala nam zrozumieć zakres tego zjawiska.


## Zasady BIP47 i PayNym.


BIP47 ma na celu zapewnienie prostego sposobu otrzymywania wielu płatności bez ponownego użycia Address. Jego działanie opiera się na wykorzystaniu kodu płatności wielokrotnego użytku.


W ten sposób wielu nadawców może wysyłać wiele płatności do jednego kodu płatności wielokrotnego użytku innego użytkownika, bez konieczności dostarczania przez odbiorcę nowego pustego Address dla każdej nowej transakcji.


Użytkownik może swobodnie udostępniać swój kod płatności (w sieciach społecznościowych, na swojej stronie internetowej...) bez ryzyka utraty prywatności, w przeciwieństwie do zwykłego otrzymania Address lub klucza publicznego.

Aby przeprowadzić Exchange, obaj użytkownicy muszą posiadać Bitcoin Wallet z implementacją BIP47, taką jak PayNym na Samourai Wallet lub Sparrow Wallet. Powiązanie kodów płatności dwóch użytkowników ustanowi między nimi tajny kanał. Aby prawidłowo ustanowić ten kanał, nadawca musi wykonać transakcję na Bitcoin Blockchain: transakcję powiadomienia (wyjaśnię więcej na ten temat później).


Powiązanie kodów płatności dwóch użytkowników generuje wspólne sekrety, które same generate dużą liczbę unikalnych adresów odbiorczych Bitcoin (dokładnie 2^32). Tak więc w rzeczywistości płatność za pomocą BIP47 nie jest wysyłana na kod płatności, ale na zupełnie normalne adresy, pochodzące z kodów płatności zaangażowanych stron.


Kod płatności działa jako wirtualny identyfikator, wywodzący się z Wallet seed. W strukturze pochodnej HD Wallet kod płatności znajduje się na głębokości 3, na poziomie rachunku Wallet.


![image](assets/3.webp)


Jego cel wyprowadzenia jest oznaczony jako 47" (0x8000002F) w odniesieniu do BIP47. Na przykład, ścieżka derywacji dla kodu płatności wielokrotnego użytku byłaby następująca: ** m/47'/0'/0'/**


Aby dać ci wyobrażenie o tym, jak wygląda kod płatności, oto mój: **PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5**


Można go również zakodować jako kod QR, aby ułatwić komunikację:


![image](assets/4.webp)


Jeśli chodzi o PayNym Bots, te roboty, które widzisz na Twitterze, są po prostu wizualnymi reprezentacjami twojego kodu płatności, stworzonymi przez Samourai Wallet. Są one generowane przy użyciu funkcji Hash, co czyni je niemal unikalnymi. Oto mój z jego identyfikatorem: **+throbbingpond8B1**


![image](assets/5.webp)


Boty te nie mają żadnej rzeczywistej użyteczności technicznej. Zamiast tego ułatwiają interakcje między użytkownikami, tworząc wirtualną tożsamość wizualną.


Dla użytkownika proces dokonywania płatności BIP47 za pomocą implementacji PayNym jest niezwykle prosty. Wyobraźmy sobie, że Alice chce wysyłać płatności do Boba:


1. Bob udostępnia swój kod QR lub bezpośrednio kod płatności wielokrotnego użytku. Może umieścić go na swojej stronie internetowej, w różnych publicznych sieciach społecznościowych lub wysłać go do Alice za pośrednictwem innego środka komunikacji.

2. Alice otwiera oprogramowanie Samourai lub Sparrow i skanuje lub wkleja kod płatności Boba.

3. Alice łączy swój PayNym z PayNym Boba ("Follow" w języku angielskim). Ta operacja jest wykonywana off-chain i pozostaje całkowicie darmowa.

4. Alice łączy swój PayNym z PayNym Boba ("Connect" w języku angielskim). Ta operacja jest wykonywana "On-Chain". Alicja musi uiścić opłaty Mining za transakcję, a także stałą opłatę w wysokości 15 000 Sats za usługę na Samourai. Opłaty za usługę są zniesione w Sparrow. Ten krok nazywamy transakcją powiadomienia.

5. Po potwierdzeniu transakcji powiadomienia Alicja może utworzyć transakcję płatności BIP47 do Boba. Jej Wallet automatycznie utworzy generate nowy pusty Address odbiorczy, dla którego tylko Bob ma klucz prywatny.


Wykonanie transakcji notyfikacji, tj. podłączenie PayNym, jest obowiązkowym warunkiem wstępnym do dokonywania płatności BIP47. Jednak po wykonaniu tej czynności nadawca może dokonać wielu płatności na rzecz odbiorcy (dokładnie 2^32) bez konieczności wykonywania nowej transakcji powiadomienia.


Być może zauważyłeś, że istnieją dwie różne operacje łączenia PayNyms: "follow" i "connect". Operacja połączenia ("connecter") odpowiada transakcji powiadomienia BIP47, która jest po prostu transakcją Bitcoin z pewnymi informacjami przesyłanymi przez wyjście OP_RETURN. W ten sposób pomaga ustanowić zaszyfrowaną komunikację między dwoma użytkownikami w celu wytworzenia wspólnych tajemnic niezbędnych do generowania nowych pustych adresów odbiorczych.


Z drugiej strony, operacja łączenia ("follow" lub "relier") pozwala na połączenie z Soroban, szyfrowanym protokołem komunikacyjnym opartym na Tor, specjalnie opracowanym przez zespoły Samourai.


Podsumowując:



- Łączenie dwóch PayNyms ("follow") jest całkowicie bezpłatne. Pomaga ustanowić szyfrowaną komunikację off-chain, szczególnie w przypadku korzystania z narzędzi Samourai do transakcji kolaboracyjnych (Stowaway lub StonewallX2). Ta operacja jest specyficzna dla PayNym i nie jest opisana w BIP47.
- Połączenie dwóch PayNyms wiąże się z kosztami. Obejmuje to wykonanie transakcji powiadomienia w celu zainicjowania połączenia. Koszt składa się z wszelkich opłat za usługę, opłat za transakcję Mining i 546 Sats wysłanych do Address powiadomienia odbiorcy, aby powiadomić go o otwarciu tunelu. Ta operacja jest powiązana z BIP47. Po jej zakończeniu nadawca może dokonać wielu płatności BIP47 na rzecz odbiorcy.


Aby połączyć dwa PayNyms, muszą one być już połączone.


## Samouczki: Korzystanie z PayNym.


Teraz, gdy zapoznaliśmy się z teorią, przeanalizujmy razem praktykę. Ideą poniższych samouczków jest połączenie mojego PayNym na moim Sparrow Wallet z moim PayNym na moim Samourai Wallet. Pierwszy samouczek pokazuje, jak dokonać transakcji przy użyciu kodu płatności wielokrotnego użytku z Samourai do Sparrow, a drugi samouczek opisuje ten sam mechanizm ze Sparrow do Samourai.


**Uwaga:** Wykonałem te samouczki na Testnet. To nie są prawdziwe bitcoiny.


### Budowanie transakcji BIP47 z Samourai Wallet.


Aby rozpocząć, potrzebujesz oczywiście aplikacji Samourai Wallet. Można ją pobrać bezpośrednio ze sklepu Google Play lub za pomocą pliku APK dostępnego na oficjalnej stronie Samourai.


Po zainicjowaniu Wallet, jeśli jeszcze tego nie zrobiłeś, poproś o swój PayNym, klikając plus (+) w prawym dolnym rogu, a następnie "PayNym".


Pierwszym krokiem do dokonania płatności BIP47 jest pobranie kodu płatności wielokrotnego użytku od naszego odbiorcy. Następnie będziemy mogli się z nim połączyć, a następnie utworzyć link:


![video](assets/6.mp4)


Po potwierdzeniu transakcji powiadomienia mogę wysłać wiele płatności do mojego odbiorcy. Każda transakcja zostanie automatycznie wykonana przy użyciu nowego pustego Address, do którego odbiorca ma klucze. Odbiorca nie musi podejmować żadnych działań, wszystko jest obliczane po mojej stronie.


Oto jak dokonać transakcji BIP47 na Samourai Wallet:


![video](assets/7.mp4)


### Budowanie transakcji BIP47 za pomocą Sparrow Wallet.


Podobnie jak w przypadku Samourai, wymagane jest oczywiście oprogramowanie Sparrow. Jest ono dostępne na komputerze. Można je pobrać z ich [oficjalnej strony internetowej] (https://sparrowwallet.com/).


Upewnij się, że zweryfikowałeś podpis dewelopera i integralność pobranego oprogramowania przed zainstalowaniem go na swoim komputerze.


Utwórz Wallet i poproś o PayNym, klikając "Pokaż PayNym" w menu "Narzędzie" na górnym pasku:


![image](assets/8.webp)


Następnie należy połączyć swój PayNym z kontem odbiorcy. Aby to zrobić, wprowadź kod płatności wielokrotnego użytku w oknie "Znajdź kontakt", śledź go, a następnie wykonaj transakcję powiadomienia, klikając "Połącz kontakt":


![image](assets/9.webp)


Po potwierdzeniu transakcji powiadomienia można wysyłać płatności do kodu płatności wielokrotnego użytku. Oto jak to zrobić:


![video](assets/10.mp4)


Teraz, gdy udało nam się zbadać praktyczny aspekt implementacji BIP47 przez PayNym, zobaczmy, jak działają wszystkie te mechanizmy i jakie metody kryptograficzne są używane.


## Wewnętrzne działanie BIP47.


Aby zbadać mechanizmy BIP47, konieczne jest zrozumienie struktury hierarchicznego deterministycznego (HD) Wallet, mechanizmów uzyskiwania par kluczy potomnych, a także zasad kryptografii krzywych eliptycznych. Na szczęście wszystkie informacje niezbędne do zrozumienia tej części można znaleźć na moim blogu:



- [Zrozumienie ścieżek wyprowadzania Bitcoin Wallet](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-Bitcoin)



- [Bitcoin Wallet - fragment ebooka Bitcoin Zdemokratyzowany 2](https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2)


### Kod płatności wielokrotnego użytku.


Jak wyjaśniono w drugiej części tego artykułu, kod płatności wielokrotnego użytku znajduje się na trzeciej głębokości HD Wallet. Jest on nieco porównywalny do xpub, zarówno pod względem umiejscowienia i struktury, jak i roli.


Oto różne części składające się na 80-bajtowy kod płatności:



- _Bajt 0_: Wersja. Jeśli używana jest pierwsza wersja BIP47, bajt ten będzie równy 0x01.
- _Bajt 1_: Pole bitów. Ta przestrzeń jest zarezerwowana dla zapewnienia dodatkowych wskazówek w przypadku konkretnego użycia. Jeśli po prostu używasz PayNym, ten bajt będzie równy 0x00.
- _Bajt 2_: Parzystość y. Ten bajt wskazuje 0x02 lub 0x03 w zależności od parzystości (liczba parzysta lub nieparzysta) wartości współrzędnej y naszego klucza publicznego. Aby uzyskać więcej informacji na temat tej praktyki, przeczytaj krok 1 sekcji "Wyprowadzanie Address" w tym artykule.
- _Od bajtu 3 do bajtu 34_: Wartość x. Te bajty wskazują współrzędną x naszego klucza publicznego. Konkatenacja x i parzystości y daje nam nasz skompresowany klucz publiczny.
- _Od bajtu 35 do bajtu 66_: Kod łańcucha. To miejsce jest zarezerwowane dla kodu łańcucha powiązanego z wyżej wymienionym kluczem publicznym.
- _Od bajtu 67 do bajtu 79_: Padding. To miejsce jest zarezerwowane na ewentualne przyszłe zmiany. W wersji 1 po prostu wypełniamy ją zerami, aby osiągnąć 80 bajtów, co jest rozmiarem danych dla wyjścia OP_RETURN.


Oto szesnastkowa reprezentacja mojego kodu płatności wielokrotnego użytku, przedstawionego w poprzedniej sekcji, z kolorami odpowiadającymi bajtom przedstawionym powyżej:

Następnie należy również dodać bajt prefiksu "P", aby szybko zidentyfikować, że mamy do czynienia z kodem płatności. Ten bajt to 0x47.


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000**


Na koniec obliczamy sumę kontrolną tego kodu płatności za pomocą HASH256, co oznacza podwójne haszowanie za pomocą funkcji SHA256. Pobieramy pierwsze cztery bajty tego skrótu i łączymy je na końcu (na różowo).


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000567080c4**


Kod płatności jest gotowy, teraz musimy tylko przekonwertować go na Base 58:


**PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5**


Jak widać, konstrukcja ta bardzo przypomina strukturę rozszerzonego klucza publicznego typu "xpub".


Podczas tego procesu, aby uzyskać nasz kod płatności, użyliśmy skompresowanego klucza publicznego i kodu łańcuchowego. Te dwa Elements są wynikiem deterministycznej i hierarchicznej derywacji z Wallet seed, zgodnie z następującą ścieżką derywacji: m/47'/0'/0'/


Mówiąc konkretnie, aby uzyskać klucz publiczny i kod łańcucha kodu płatności wielokrotnego użytku, obliczymy główny klucz prywatny z seed, a następnie wyprowadzimy parę potomną z indeksem 47 + 2^31 (utwardzona derywacja). Następnie wyprowadzimy dwie kolejne pary potomne z indeksem 2^31 (utwardzona derywacja).


**Uwaga:** Jeśli chcesz dowiedzieć się więcej o wyprowadzaniu par kluczy potomnych w hierarchicznym deterministycznym Bitcoin Wallet, polecam wzięcie udziału w CRYPTO301.


### Metoda kryptograficzna: Elliptic Curve Diffie-Hellman key Exchange (ECDH).


Metodą kryptograficzną wykorzystywaną w BIP47 jest ECDH (Elliptic-Curve Diffie-Hellman). Protokół ten jest wariantem klasycznego klucza Diffiego-Hellmana Exchange.


Diffie-Hellman, w swojej pierwszej wersji, to protokół uzgadniania kluczy przedstawiony w 1976 roku, który pozwala dwóm stronom, z których każda posiada parę kluczy publicznych i prywatnych, określić wspólny sekret poprzez wymianę informacji za pośrednictwem niezabezpieczonego kanału komunikacyjnego.


![image](assets/11.webp)


Ten wspólny sekret (czerwony klucz) może być następnie wykorzystywany do innych zadań. Zazwyczaj ten wspólny klucz tajny może być używany do szyfrowania i odszyfrowywania komunikacji w niezabezpieczonej sieci:


![image](assets/12.webp)


Aby osiągnąć ten Exchange, Diffie-Hellman wykorzystuje arytmetykę modularną do obliczania współdzielonego sekretu. Oto uproszczone wyjaśnienie, jak to działa:



- Alicja i Bob uzgadniają wspólny kolor, w tym przypadku żółty. Ten kolor jest znany wszystkim. Jest to informacja publiczna.
- Alicja wybiera sekretny kolor, w tym przypadku czerwony. Miesza oba kolory, uzyskując pomarańczowy.
- Bob wybiera tajny kolor, w tym przypadku turkusowy. Miesza oba kolory, uzyskując błękit nieba.
- Alice i Bob mogą Exchange uzyskane kolory: pomarańczowy i błękitny. To Exchange może się zdarzyć w niezabezpieczonej sieci i może być obserwowane przez atakujących.
- Alicja miesza błękitny kolor otrzymany od Boba ze swoim tajnym kolorem (czerwonym). Otrzymuje kolor brązowy.
- Bob miesza pomarańczowy kolor otrzymany od Alicji ze swoim tajnym kolorem (turkusowym). Otrzymuje również kolor brązowy.


![image](assets/13.webp)


**Kredyt:** Oryginalny pomysł: A.J. Han VinckWersja wektorowa: FlugaalTłumaczenie: Dereckson, domena publiczna, za pośrednictwem Wikimedia Commons. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg


W tym uproszczeniu brązowy kolor reprezentuje sekret współdzielony przez Alicję i Boba. Należy sobie wyobrazić, że w rzeczywistości atakujący nie jest w stanie oddzielić kolorów pomarańczowego i błękitnego w celu odzyskania tajnych kolorów Alicji lub Boba.


Przeanalizujmy teraz jego rzeczywiste działanie. Na pierwszy rzut oka Diffie-Hellman może wydawać się skomplikowany do zrozumienia. W rzeczywistości zasada działania jest niemal dziecinnie prosta. Przed szczegółowym omówieniem jego mechanizmów, szybko przypomnę dwie koncepcje matematyczne, których będziemy potrzebować (i nawiasem mówiąc, są one również używane w wielu innych metodach kryptograficznych).


1. Liczba pierwsza to liczba naturalna, która ma tylko dwa dzielniki: 1 i samą siebie. Na przykład, liczba 7 jest liczbą pierwszą, ponieważ może być podzielna tylko przez 1 i 7 (samą siebie). Z drugiej strony, liczba 8 nie jest liczbą pierwszą, ponieważ może być podzielna przez 1, 2, 4 i 8. Ma ona zatem nie tylko dwa dzielniki, ale cztery dzielniki całkowite i dodatnie.

2. "Modulo" (oznaczane jako "mod" lub "%") to operacja matematyczna, która pozwala dwóm liczbom całkowitym zwrócić resztę z euklidesowego dzielenia pierwszej liczby przez drugą. Na przykład, 16 mod 5 jest równe 1.


Klucz Diffiego-Hellmana Exchange między Alice i Bobem działa w następujący sposób:



- Alicja i Bob określają dwie wspólne liczby: p i g. p jest liczbą pierwszą. Im większa jest ta liczba p, tym bezpieczniejsza będzie metoda Diffiego-Hellmana. g jest pierwiastkiem pierwotnym z p. Te dwie liczby mogą być przekazywane zwykłym tekstem przez niezabezpieczoną sieć, są one odpowiednikami żółtego koloru w powyższym uproszczeniu. Alicja i Bob muszą mieć dokładnie takie same wartości p i g.
- Po wybraniu parametrów Alice i Bob samodzielnie określają tajną liczbę losową. Liczba losowa uzyskana przez Alicję nosi nazwę a (odpowiednik koloru czerwonego), a liczba losowa uzyskana przez Boba nosi nazwę b (odpowiednik koloru turkusowego). Te dwie liczby muszą pozostać tajne.
- Zamiast wymieniać się tymi liczbami a i b, każda ze stron obliczy A (wielkimi literami) i B (wielkimi literami) w taki sposób:


A jest równe g podniesionemu do potęgi a modulo p:

**A = g^a % p**


B jest równe g podniesionemu do potęgi b modulo p:

**B = g^b % p**



- Numery A (odpowiednik koloru pomarańczowego) i B (odpowiednik koloru błękitnego) będą wymieniane między dwiema stronami. Exchange można wykonać zwykłym tekstem za pośrednictwem niezabezpieczonej sieci.
- Alicja, która teraz zna B, obliczy wartość z w taki sposób, że:


z jest równe B podniesionemu do potęgi a modulo p:

**z = B^a % p**



- Dla przypomnienia, B = g^b % p. Zatem:

**z = B^a % p**

**z = (g^b)^a % p**


Zgodnie z zasadami potęgowania:

**(x^n)^m = x^nm**


Dlatego:

**z = g^ba % p**



- Bob, który zna teraz A, również obliczy wartość z w następujący sposób:


z jest równe A podniesionemu do potęgi b modulo p:

**z = A^b % p**


Dlatego:

**z = (g^a)^b % p**

**z = g^ab % p**

**z = g^ba % p**


Dzięki rozdzielności operatora modulo, Alicja i Bob znajdują dokładnie taką samą wartość dla z. Liczba ta reprezentuje ich wspólny sekret, który jest odpowiednikiem koloru brązowego w poprzednim wyjaśnieniu. Mogą używać tego wspólnego sekretu do szyfrowania komunikacji między sobą w niezabezpieczonej sieci.


![Diffie-Hellman Technical Operation Diagram](assets/14.webp)


Atakujący posiadający p, g, A i B nie będzie w stanie obliczyć a, b lub z. Wykonanie tej operacji wymagałoby odwrócenia potęgowania, co jest niemożliwe do wykonania inaczej niż poprzez wypróbowanie wszystkich możliwości jedna po drugiej, ponieważ pracujemy ze skończonym polem. Byłoby to równoważne obliczeniu dyskretnego logarytmu, który jest odwrotnością potęgowania w cyklicznej grupie skończonej.


Dlatego tak długo, jak wybieramy wystarczająco duże wartości dla a, b i p, Diffie-Hellman jest bezpieczny. Zazwyczaj przy parametrach wynoszących 2048 bitów (liczba składająca się z 600 cyfr dziesiętnych) testowanie wszystkich możliwości dla a i b byłoby niepraktyczne. Do tej pory, przy liczbach tego rozmiaru, algorytm jest uważany za bezpieczny.


W tym właśnie tkwi główna wada protokołu Diffiego-Hellmana. Aby być bezpiecznym, algorytm musi wykorzystywać duże liczby. W rezultacie preferowany jest obecnie algorytm ECDH, który jest wariantem Diffiego-Hellmana wykorzystującym krzywą algebraiczną, a konkretnie krzywą eliptyczną. Pozwala to na pracę ze znacznie mniejszymi liczbami przy zachowaniu równoważnego bezpieczeństwa, zmniejszając w ten sposób wymagane zasoby obliczeniowe i pamięciowe.


Ogólna zasada działania algorytmu pozostaje taka sama. Jednak zamiast używać losowej liczby a i liczby A obliczonej z a przy użyciu wykładnictwa modularnego, użyjemy pary kluczy ustalonych na krzywej eliptycznej. Zamiast polegać na rozdzielności operatora modulo, wykorzystamy prawo grup na krzywych eliptycznych, a konkretnie asocjatywność tego prawa.

Jeśli nie wiesz, jak działają klucze prywatne i publiczne na krzywej eliptycznej, wyjaśnię podstawy tej metody w pierwszych sześciu częściach tego artykułu.


Podsumowując, klucz prywatny to liczba losowa z przedziału od 1 do n-1 (gdzie n to rząd krzywej), a klucz publiczny to unikalny punkt na krzywej określony przez klucz prywatny poprzez dodawanie punktów i podwajanie od punktu generatora, jak poniżej:


**K = k-G**


Gdzie K to klucz publiczny, k to klucz prywatny, a G to punkt generatora.


Jedną z właściwości tej pary kluczy jest to, że bardzo łatwo jest określić K, jeśli znasz k i G, ale obecnie niemożliwe jest określenie k, jeśli znasz K i G. Jest to funkcja jednokierunkowa.


Innymi słowy, możesz łatwo obliczyć klucz publiczny, jeśli znasz klucz prywatny, ale niemożliwe jest obliczenie klucza prywatnego, jeśli znasz klucz publiczny. Bezpieczeństwo to ponownie opiera się na niemożności obliczenia logarytmu dyskretnego.


Wykorzystamy tę właściwość do dostosowania naszego algorytmu Diffiego-Hellmana. Tak więc zasada działania ECDH jest następująca:



- Alice i Bob uzgadniają kryptograficznie bezpieczną krzywą eliptyczną i jej parametry. Informacje te są jawne.
- Alicja generuje losową liczbę ka, która będzie jej kluczem prywatnym. Ten klucz prywatny musi pozostać tajny. Określa swój klucz publiczny Ka, dodając i podwajając punkty na wybranej krzywej eliptycznej.


**Ka = ka-G**



- Bob generuje również losową liczbę kb, która będzie jego kluczem prywatnym. Oblicza powiązany klucz publiczny Kb.


**Kb = kb-G**



- Alice i Bob Exchange swoje klucze publiczne Ka i Kb przez niezabezpieczoną sieć publiczną.
- Alicja oblicza punkt (x, y) na krzywej, stosując swój klucz prywatny ka do klucza publicznego Kb Boba.


**(x, y) = ka-Kb**



- Bob oblicza punkt (x, y) na krzywej, stosując swój klucz prywatny kb do klucza publicznego Ka Alicji.


**(x, y) = kb-Ka**



- Alicja i Bob uzyskują ten sam punkt na krzywej eliptycznej. Współdzielonym sekretem będzie współrzędna x tego punktu.


Uzyskują one ten sam wspólny klucz tajny, ponieważ:


**(x, y) = ka-Kb = ka-kb-G = kb-ka-G = kb-Ka**


Potencjalny atakujący obserwujący niezabezpieczoną sieć publiczną może uzyskać jedynie klucze publiczne każdej ze stron i wybrane parametry krzywej. Jak wyjaśniono wcześniej, te dwie informacje same w sobie nie pozwalają na określenie kluczy prywatnych, więc atakujący nie może uzyskać dostępu do sekretu.

ECDH to algorytm, który pozwala na klucz Exchange. Jest on często używany wraz z innymi metodami kryptograficznymi w celu zdefiniowania protokołu. Na przykład ECDH jest używany w rdzeniu TLS (Transport Layer Security), protokołu szyfrowania i uwierzytelniania używanego do transportu internetowego Layer. TLS wykorzystuje ECDHE dla klucza Exchange, wariant ECDH, w którym klucze są efemeryczne, aby zapewnić trwałą poufność. Oprócz ECDHE, TLS wykorzystuje również algorytm uwierzytelniania, taki jak ECDSA, algorytm szyfrowania, taki jak AES, oraz funkcję Hash, taką jak SHA256.


TLS definiuje "s" w "https" i małą ikonę kłódki, którą widzisz w przeglądarce internetowej w lewym górnym rogu, co gwarantuje szyfrowaną komunikację. Tak więc, czytając ten artykuł, korzystasz obecnie z ECDH i prawdopodobnie używasz go codziennie, nie zdając sobie z tego sprawy.


### Transakcja powiadomienia


Jak dowiedzieliśmy się w poprzedniej sekcji, ECDH to wariant Exchange Diffiego-Hellmana obejmujący pary kluczy utworzone na krzywej eliptycznej. Na szczęście mamy mnóstwo par kluczy, które spełniają ten standard w naszych portfelach Bitcoin!


Pomysł polega na wykorzystaniu par kluczy z hierarchicznych deterministycznych portfeli Bitcoin obu stron w celu ustanowienia wspólnych i efemerycznych tajemnic między nimi. W BIP47 zamiast tego używany jest ECDHE (Elliptic Curve Diffie-Hellman Ephemeral).


ECDHE jest początkowo używane w BIP47 do przesyłania kodu płatności nadawcy do odbiorcy. Jest to słynna transakcja powiadomienia. Aby BIP47 mógł być używany, obie strony (nadawca, który wysyła płatności i odbiorca, który otrzymuje płatności) muszą być świadome swojego kodu płatności. Jest to konieczne do uzyskania efemerycznych kluczy publicznych, a tym samym dedykowanych adresów odbiorczych.


Przed tym Exchange nadawca logicznie zna już kod płatności odbiorcy, ponieważ mógł go uzyskać off-chain, na przykład ze swojej strony internetowej lub mediów społecznościowych. Jednak odbiorca niekoniecznie musi znać kod płatności nadawcy. Musi on zostać im przekazany, w przeciwnym razie nie będą w stanie uzyskać swoich kluczy efemerycznych, a tym samym nie będą w stanie dowiedzieć się, gdzie znajdują się ich bitcoiny i odblokować swoich środków. Można by przesłać im off-chain, używając innego systemu komunikacji, ale stanowiłoby to problem, gdyby Wallet został odzyskany z seed.

Rzeczywiście, jak już wspomniałem, adresy BIP47 nie pochodzą z seed odbiorcy (w przeciwnym razie lepiej byłoby użyć bezpośrednio jednego z ich xpubów), ale są wynikiem obliczeń obejmujących zarówno kod płatności odbiorcy, jak i kod płatności nadawcy. Dlatego też, jeśli odbiorca utraci swój Wallet i spróbuje odzyskać go ze swojego seed, będzie musiał mieć wszystkie kody płatności osób, które wysłały mu bitcoiny za pośrednictwem BIP47.


Możliwe byłoby korzystanie z BIP47 bez tej transakcji powiadamiania, ale każdy użytkownik musiałby wykonać kopię zapasową kodów płatności swoich rówieśników. Sytuacja ta pozostanie nie do opanowania, dopóki nie zostanie znaleziony prosty i odporny sposób tworzenia, przechowywania i aktualizowania tych kopii zapasowych. Transakcja powiadamiania jest zatem niemal obowiązkowa w obecnym stanie rzeczy.


Oprócz roli tworzenia kopii zapasowych kodów płatności, jak sama nazwa wskazuje, transakcja ta służy również jako powiadomienie dla odbiorcy. Informuje ona klienta, że tunel został właśnie otwarty.


Zanim wyjaśnię bardziej szczegółowo techniczne funkcjonowanie transakcji powiadomień, chciałbym powiedzieć trochę o modelu prywatności. Rzeczywiście, model prywatności BIP47 uzasadnia pewne środki ostrożności podjęte przy konstruowaniu tej początkowej transakcji.


Sam kod płatności nie stanowi bezpośredniego zagrożenia dla prywatności. W przeciwieństwie do klasycznego modelu Bitcoin, który pozwala na przerwanie przepływu informacji między tożsamością użytkownika a transakcjami, w szczególności poprzez zachowanie anonimowości kluczy publicznych, kod płatności może być bezpośrednio powiązany z tożsamością. Nie jest to obowiązkowe, ale powiązanie to nie jest niebezpieczne.


W rzeczywistości kod płatności nie jest bezpośrednim źródłem adresów używanych do otrzymywania płatności BIP47. Zamiast tego adresy są uzyskiwane poprzez zastosowanie ECDHE między kluczami podrzędnymi kodów płatności obu stron.


W związku z tym sam kod płatności nie stanowi bezpośredniego zagrożenia dla prywatności, ponieważ wynika z niego jedynie powiadomienie Address. Można z niego wywnioskować pewne informacje, ale zwykle nie można wiedzieć, z kim dokonuje się transakcji.


Niezbędne jest zatem zachowanie ścisłej separacji między kodami płatności użytkowników. Pod tym względem początkowy etap komunikacji kodu jest krytycznym momentem dla prywatności płatności, a jednocześnie jest obowiązkowy dla prawidłowego funkcjonowania protokołu. Jeśli jeden z kodów płatności może być publicznie pobrany (na przykład ze strony internetowej), drugi kod, tj. kod nadawcy, nie powinien być powiązany z pierwszym.


Wyobraźmy sobie na przykład, że chcę przekazać darowiznę za pomocą BIP47 na rzecz pokojowego ruchu protestacyjnego w Kanadzie:



- Organizacja ta opublikowała swój kod płatności bezpośrednio na swojej stronie internetowej lub platformach mediów społecznościowych.
- Kod ten jest zatem powiązany z ruchem.
- Pobieram ten kod płatności.
- Zanim będę mógł wysłać im transakcję, muszę upewnić się, że znają mój osobisty kod płatności, który jest również powiązany z moją tożsamością, ponieważ używam go do otrzymywania transakcji z moich sieci społecznościowych.


Jak mogę im to przekazać? Jeśli wyślę je do nich za pomocą konwencjonalnych środków komunikacji, informacje mogą wyciec, a ja mogę zostać zidentyfikowany jako osoba wspierająca pokojowe ruchy.


Transakcja z powiadomieniem z pewnością nie jest jedynym rozwiązaniem do potajemnego przesyłania kodu płatności nadawcy, ale obecnie doskonale spełnia tę rolę, stosując wiele warstw zabezpieczeń.


Na poniższym diagramie czerwone linie reprezentują moment, w którym przepływ informacji musi zostać przerwany, a czarne strzałki reprezentują niezaprzeczalne powiązania, które może wykonać zewnętrzny obserwator:


![Privacy model diagram for reusable payment code](assets/15.webp)


W rzeczywistości, w przypadku klasycznego modelu prywatności Bitcoin, często trudno jest całkowicie przerwać przepływ informacji między parą kluczy a użytkownikiem, zwłaszcza podczas przeprowadzania transakcji zdalnych. Przykładowo, w przypadku kampanii darowizn, odbiorca będzie zobowiązany do ujawnienia Address lub klucza publicznego na swojej stronie internetowej lub platformach mediów społecznościowych. Właściwe użycie BIP47, tj. z transakcją powiadomienia, rozwiązuje ten problem poprzez ECDHE i szyfrowanie Layer, które będziemy badać.


Oczywiście klasyczny model prywatności Bitcoin jest nadal obserwowany na poziomie efemerycznych kluczy publicznych pochodzących z powiązania dwóch kodów płatności. Te dwa modele są od siebie zależne. Chciałbym tylko podkreślić, że w przeciwieństwie do klasycznego użycia klucza publicznego do otrzymywania bitcoinów, kod płatności może być powiązany z tożsamością, ponieważ informacja "Bob dokonuje transakcji z Alicją" zostaje przerwana w innym momencie. Kod płatności jest używany do adresów płatności generate, ale obserwując tylko Blockchain, niemożliwe jest powiązanie transakcji płatniczej BIP47 z kodami płatności użytymi do jej wykonania.


### Konstrukcja transakcji powiadomienia


Zobaczmy teraz, jak działa ta transakcja powiadomienia. Wyobraźmy sobie, że Alice chce wysłać środki do Boba za pomocą BIP47. W moim przykładzie Alice działa jako nadawca, a Bob jako odbiorca. Bob opublikował już swój kod płatności na swojej stronie internetowej, więc Alicja jest już świadoma kodu płatności Boba.


1- Alicja oblicza wspólny sekret za pomocą ECDH:



- Wybiera parę kluczy ze swojego HD Wallet znajdującego się w innej gałęzi niż jej kod płatności. Należy pamiętać, że ta para nie powinna być łatwo powiązana z powiadomieniem Address lub tożsamością Alicji (patrz poprzednia sekcja).
- Alice wybiera klucz prywatny z tej pary. Nazwiemy go **a** (małymi literami).



- Alicja pobiera klucz publiczny powiązany z powiadomieniem Address Boba. Klucz ten jest pierwszym dzieckiem pochodzącym z kodu płatności Boba (indeks 0). Będziemy nazywać ten klucz publiczny "B" (wielkimi literami). Klucz prywatny powiązany z tym kluczem publicznym nazywamy "b" (małymi literami). "B" jest określany przez dodawanie i podwajanie punktów na krzywej eliptycznej od "G" (punkt generatora) z "b" (klucz prywatny).

**B = b-G**



- Alicja oblicza tajny punkt "S" (wielkimi literami) na krzywej eliptycznej poprzez dodawanie i podwajanie punktów, stosując swój klucz prywatny "a" do klucza publicznego "B" Boba.

**S = a-B**



- Alice oblicza współczynnik zaślepienia "f", który zostanie użyty do zaszyfrowania jej kodu płatności. Aby to zrobić, użyje generate liczby pseudolosowej przy użyciu funkcji HMAC-SHA512. Jako drugie dane wejściowe do tej funkcji używa wartości, którą tylko Bob będzie w stanie odzyskać: (x), która jest współrzędną x wcześniej obliczonego tajnego punktu. Pierwszym wejściem jest (o), które jest UTXO zużytym jako wejście do tej transakcji (punkt wyjścia).

**f = HMAC-SHA512(o, x)**


2- Alice konwertuje swój osobisty kod płatności na kod o podstawie 2 (binarny).


3- Używa tego czynnika oślepiającego jako klucza do symetrycznego szyfrowania ładunku swojego kodu płatności. Zastosowany algorytm szyfrowania to po prostu XOR. Wykonywana operacja jest podobna do szyfru Vernama, znanego również jako "jednorazowy pad":



- Alice najpierw dzieli swój czynnik oślepiający na dwie części: pierwsze 32 bajty nazywane są "f1", a ostatnie 32 bajty nazywane są "f2". Mamy więc:

**f = f1 || f2**



- Alicja oblicza szyfrogram (x') współrzędnej x klucza publicznego (x) swojego kodu płatności, a osobno oblicza szyfrogram (c') swojego kodu łańcucha (c). "f1" i "f2" działają jako klucze szyfrujące i używana jest operacja XOR.

**x' = x XOR f1**

**c' = c XOR f2**



- Alice zastępuje rzeczywiste wartości odciętej klucza publicznego (x) i kodu łańcucha (c) w swoim kodzie płatności zaszyfrowanymi wartościami (x') i (c').


Zanim przejdziemy do technicznego opisu tej transakcji powiadamiania, poświęćmy chwilę na omówienie operacji XOR. XOR jest bitowym operatorem logicznym opartym na algebrze boolowskiej. Biorąc pod uwagę dwa operandy bitowe, zwraca 1, jeśli odpowiednie bity są różne, i zwraca 0, jeśli odpowiednie bity są równe. Oto tabela prawdy dla XOR oparta na wartościach operandów D i E:


| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Na przykład:


**0110 XOR 1110 = 1000**


Lub:


**010011 XOR 110110 = 100101**


W przypadku ECDH użycie XOR jako szyfrowania Layer jest szczególnie spójne. Po pierwsze, dzięki temu operatorowi szyfrowanie jest symetryczne. Umożliwia to odbiorcy odszyfrowanie kodu płatności za pomocą tego samego klucza, który został użyty do szyfrowania. Klucz szyfrowania i deszyfrowania jest obliczany na podstawie współdzielonego sekretu przy użyciu ECDH.


Symetria ta jest możliwa dzięki właściwościom komutatywności i asocjatywności operatora XOR:



- Inne właściwości:

-> D ⊕ D = 0

-> D ⊕ 0 = D



- Przemienność:

D ⊕ E = E ⊕ D



- Asocjatywność:

D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z



- Symetria:

Jeśli: D ⊕ E = L

Wtedy: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E

-> D ⊕ L = E

Następnie, ta metoda szyfrowania jest bardzo podobna do szyfru Vernama (One-Time Pad), jedynego znanego do tej pory algorytmu szyfrowania, który ma bezwarunkowe (lub absolutne) bezpieczeństwo. Aby szyfr Vernama miał taką charakterystykę, klucz szyfrujący musi być idealnie losowy, mieć taki sam rozmiar jak wiadomość i być użyty tylko raz. W metodzie szyfrowania zastosowanej tutaj dla BIP47, klucz ma rzeczywiście taki sam rozmiar jak wiadomość, a czynnik oślepiający ma dokładnie taki sam rozmiar jak konkatenacja współrzędnej x klucza publicznego z kodem łańcucha kodu płatności. Ten klucz szyfrowania jest rzeczywiście używany tylko raz. Jednak klucz ten nie pochodzi z idealnego losowego źródła, ponieważ jest to HMAC. Jest raczej pseudolosowy. Dlatego nie jest to szyfr Vernama, ale metoda jest podobna.


Wróćmy do konstrukcji naszej transakcji powiadomienia:


4- Alicja ma obecnie swój kod płatności z zaszyfrowanym ładunkiem. Skonstruuje i wyemituje transakcję obejmującą jej klucz publiczny "A" jako dane wejściowe, dane wyjściowe do powiadomienia Address Boba oraz dane wyjściowe OP_RETURN składające się z jej kodu płatności z zaszyfrowanym ładunkiem. Transakcja ta jest transakcją powiadomienia.


OP_RETURN to kod operacyjny, który jest skryptem oznaczającym wyjście transakcji Bitcoin jako nieprawidłowe. Obecnie jest on używany do nadawania lub Anchor informacji na Bitcoin Blockchain. Może przechowywać do 80 bajtów danych, które są rejestrowane w łańcuchu i dlatego są widoczne dla wszystkich innych użytkowników.


Jak widzieliśmy w poprzedniej sekcji, Diffie-Hellman jest używany do generate współdzielonego sekretu między dwoma użytkownikami komunikującymi się przez niezabezpieczoną sieć, potencjalnie obserwowaną przez atakujących. W BIP47, ECDH jest używany do komunikacji w sieci Bitcoin, która z natury jest przezroczystą siecią komunikacyjną obserwowaną przez wielu atakujących. Współdzielony sekret obliczony za pomocą klucza Diffiego-Hellmana Exchange na krzywej eliptycznej jest następnie wykorzystywany do szyfrowania tajnych informacji, które mają zostać przesłane: kodu płatności nadawcy (Alicji).


Oto schemat zaczerpnięty z BIP47, który ilustruje to, co właśnie opisaliśmy:


![Diagram Alice sends her masked payment code to Bob's notification address](assets/16.webp)


Kredyt: Kody płatności wielokrotnego użytku dla hierarchicznych portfeli deterministycznych, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Jeśli dopasujemy ten schemat do tego, co opisałem wcześniej:



- "Wallet Priv-Key" po stronie Alice odpowiada: a.
- "Child Pub-Key 0" po stronie Boba odpowiada: B.
- "Notification Shared Secret" odpowiada: f.
- "Masked Payment Code" odpowiada zaszyfrowanemu kodowi płatności, tj. zaszyfrowanemu ładunkowi: x' i c'.
- "Transakcja powiadomienia" to transakcja zawierająca OP_RETURN.


Podsumujmy kroki, które właśnie wykonaliśmy, aby wykonać transakcję powiadomienia:



- Alice pobiera kod płatności Boba i powiadomienie Address.
- Alice wybiera UTXO, który należy do niej w jej HD Wallet z odpowiednią parą kluczy.
- Oblicza tajny punkt na krzywej eliptycznej za pomocą ECDH.
- Używa tego tajnego punktu do obliczenia HMAC, który jest czynnikiem zaślepiającym.
- Używa tego czynnika oślepiającego do szyfrowania ładunku swojego osobistego kodu płatności.
- Używa danych wyjściowych transakcji OP_RETURN do przesłania zamaskowanego kodu płatności do Boba.


Aby lepiej zrozumieć jego działanie, a zwłaszcza wykorzystanie OP_RETURN, przeanalizujmy razem prawdziwą transakcję powiadomienia. Transakcję tego typu przeprowadziłem na Testnet, który można znaleźć klikając tutaj:


https://Mempool.space/fr/Testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e


txid: **0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e**


![BIP47 Notification Transaction](assets/17.webp)


Kredyt: https://blockstream.info/


Obserwując tę transakcję, możemy już zobaczyć, że ma ona jedno wejście i 4 wyjścia:



- Pierwszy wynik to OP_RETURN, który zawiera mój zamaskowany kod płatności.
- Drugie wyjście 546 Sats wskazuje na powiadomienie odbiorcy Address.
- Trzeci wynik w wysokości 15 000 Sats reprezentuje opłatę za usługę, ponieważ użyłem Samourai Wallet do skonstruowania tej transakcji.
- Czwarte wyjście dwóch milionów Sats reprezentuje zmianę, tj. pozostałą różnicę z mojego wejścia, która wraca do innego Address należącego do mnie.


Najbardziej interesujące do zbadania jest oczywiście wyjście 0 przy użyciu OP_RETURN. Przyjrzyjmy się bliżej jego zawartości:


![OP_RETURN Output of Notification Transaction BIP47](assets/18.webp)


Kredyt: https://blockstream.info/


Odkrywamy szesnastkowy skrypt danych wyjściowych: **6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000**


W tym skrypcie możemy podzielić kilka części:

Wśród kodów operacyjnych możemy rozpoznać 0x6a, który odnosi się do OP_RETURN i 0x4c, który odnosi się do OP_PUSHDATA1. Bajt następujący po tym kodzie operacyjnym wskazuje rozmiar następującego po nim ładunku. Wskazuje on 0x50, czyli 80 bajtów.


Następnie przychodzi kod płatności z zaszyfrowanym ładunkiem.


Oto mój kod płatności użyty w tej transakcji:


W bazie 58: **PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU**


W bazie 16 (HEX): **4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db**


Jeśli porównamy mój kod płatności z OP_RETURN, zobaczymy, że HRP (w kolorze brązowym) i suma kontrolna (w kolorze różowym) nie są przesyłane. Jest to normalne, ponieważ informacje te są przeznaczone dla ludzi.

Następnie możemy rozpoznać (w Green) wersję (0x01), pole bitowe (0x00) i parzystość klucza publicznego (0x02). Na końcu kodu płatności znajdują się puste bajty w kolorze czarnym (0x00), które umożliwiają wypełnienie do 80 bajtów. Wszystkie te metadane są przesyłane w postaci zwykłego tekstu (niezaszyfrowanego).

Na koniec możemy zauważyć, że współrzędna x klucza publicznego (na niebiesko) i kod łańcucha (na czerwono) zostały zaszyfrowane. Stanowi to ładunek kodu płatności.


### Odbieranie transakcji powiadomienia.


Teraz, gdy Alice wysłała transakcję powiadomienia do Boba, zobaczmy, jak on ją zinterpretuje.


Przypominamy, że Bob musi mieć dostęp do kodu płatności Alicji. Bez tej informacji, jak zobaczymy w następnej sekcji, nie będzie on w stanie wyprowadzić par kluczy utworzonych przez Alicję, a zatem nie będzie w stanie uzyskać dostępu do swoich bitcoinów otrzymanych za pomocą BIP47. Na razie ładunek kodu płatniczego Alicji jest zaszyfrowany. Zobaczmy razem, jak Bob go odszyfruje.


1- Bob monitoruje transakcje, które tworzą wyjścia z jego powiadomieniem Address.

2- Gdy transakcja ma wyjście do jego powiadomienia Address, Bob analizuje je, aby sprawdzić, czy zawiera wyjście OP_RETURN, które jest zgodne ze standardem BIP47.

3- Jeśli pierwszy bajt ładunku OP_RETURN to 0x01, Bob rozpoczyna wyszukiwanie możliwego sekretu współdzielonego z ECDH:



- Bob wybiera klucz publiczny w danych wejściowych transakcji. Oznacza to, że klucz publiczny Alicji o nazwie "A" z: **A = a-G**
- Bob wybiera klucz prywatny "b" powiązany z jego osobistym powiadomieniem Address: **b**
- Bob oblicza tajny punkt "S" (wspólny sekret ECDH) na krzywej eliptycznej, dodając i podwajając punkty, stosując swój klucz prywatny "b" do klucza publicznego "A" Alicji: **S = b-A**
- Bob określa współczynnik zaślepienia "f", który pozwoli mu odszyfrować ładunek kodu płatności Alicji. W ten sam sposób, w jaki Alicja obliczyła go wcześniej, Bob znajdzie "f", stosując HMAC-SHA512 do (x) wartości współrzędnej x tajnego punktu "S" i do (o) UTXO zużytego jako dane wejściowe w tej transakcji powiadomienia: **f = HMAC-SHA512(o, x)**


4- Bob interpretuje dane w OP_RETURN transakcji powiadomienia jako kod płatności. Po prostu odszyfrowuje ładunek tego potencjalnego kodu płatności przy użyciu czynnika oślepiającego "f".



- Bob dzieli współczynnik oślepiania "f" na dwie części: pierwsze 32 bajty "f" to "f1", a ostatnie 32 bajty to "f2".
- Bob odszyfrowuje zaszyfrowaną wartość współrzędnej x (x') klucza publicznego kodu płatności Alice:


**x = x' XOR f1**



- Bob odszyfrowuje zaszyfrowaną wartość kodu łańcucha (c') kodu płatności Alice:


**c = c' XOR f2**


5- Bob sprawdza, czy wartość klucza publicznego kodu płatności Alice jest częścią grupy secp256k1. Jeśli tak, interpretuje ją jako prawidłowy kod płatności. W przeciwnym razie ignoruje transakcję.


Teraz, gdy Bob zna kod płatności Alice, może ona wysłać mu do 2^32 płatności bez konieczności ponownego wykonywania takiej transakcji.


Dlaczego to działa? W jaki sposób Bob może określić ten sam współczynnik zaślepienia co Alice i odszyfrować jej kod płatności? Przeanalizujmy proces ECDH bardziej szczegółowo w oparciu o to, co właśnie opisaliśmy.


Po pierwsze, mamy do czynienia z szyfrowaniem symetrycznym. Oznacza to, że klucz szyfrowania i klucz deszyfrowania mają tę samą wartość. W tym przypadku kluczem w transakcji powiadamiania jest współczynnik zaślepienia (f = f1 || f2). Alicja i Bob muszą uzyskać tę samą wartość dla f bez przekazywania jej bezpośrednio, ponieważ atakujący mógłby ją przechwycić i odszyfrować tajne informacje.


Ten współczynnik zaślepienia uzyskuje się poprzez zastosowanie HMAC-SHA512 do dwóch wartości: współrzędnej x tajnego punktu i zużytego UTXO w danych wejściowych transakcji. Dlatego Bob musi mieć te dwie informacje, aby odszyfrować ładunek kodu płatności Alice.


Jeśli chodzi o wejściowy UTXO, Bob może go po prostu pobrać, obserwując transakcję powiadomienia. W przypadku tajnego punktu Bob będzie musiał użyć ECDH.


Jak pokazano w sekcji dotyczącej Diffiego-Hellmana, wymieniając swoje klucze publiczne i potajemnie stosując swoje klucze prywatne do klucza publicznego drugiej osoby, Alice i Bob mogą znaleźć określony i tajny punkt na krzywej eliptycznej. Transakcja powiadomienia opiera się na tym mechanizmie:


Para kluczy Boba: **B = b-G**


Para kluczy Alice: **A = a-G**


Dla tajnego punktu S (x,y): **S = a-B = a-b-G = b-a-G = b-A**


![Diagram of generating a shared secret with ECDHE](assets/19.webp)

Teraz, gdy Bob zna kod płatności Alice, będzie w stanie wykryć jej płatności BIP47 i uzyskać klucze prywatne blokujące otrzymane bitcoiny.

![Bob interprets Alice's notification transaction](assets/20.webp)


Kredyt: Kody płatności wielokrotnego użytku dla hierarchicznych portfeli deterministycznych, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Jeśli dopasujemy ten schemat do tego, co opisałem wcześniej:



- "Wallet Pub-Key" po stronie Alice odpowiada: A.
- "Child Priv-Key 0" po stronie Boba odpowiada: b.
- "Notification Shared Secret" odpowiada: f.
- "Zamaskowany kod płatności" odpowiada zamaskowanemu kodowi płatności Alicji, tj. z zaszyfrowanym ładunkiem: x' i c'.
- "Transakcja powiadomienia" to transakcja zawierająca OP_RETURN.


Pozwolę sobie podsumować kroki, które właśnie wykonaliśmy, aby otrzymać i zinterpretować transakcję powiadomienia:



- Bob monitoruje wyjścia transakcji do swojego powiadomienia Address.
- Kiedy go wykryje, pobiera informacje zawarte w OP_RETURN.
- Bob wybiera wejściowy klucz publiczny i oblicza tajny punkt przy użyciu ECDH.
- Używa tego tajnego punktu do obliczenia HMAC, który jest czynnikiem zaślepiającym.
- Wykorzystuje ten czynnik oślepiający do odszyfrowania ładunku kodu płatności Alice zawartego w OP_RETURN.


### Transakcja płatnicza BIP47.


Przeanalizujmy teraz proces płatności za pomocą BIP47. Dla przypomnienia aktualna sytuacja:



- Alice zna kod płatności Boba, który po prostu pobrała z jego strony internetowej.



- Bob zna kod płatności Alice dzięki transakcji powiadomienia.



- Alice dokona początkowej płatności na rzecz Boba. W ten sam sposób może dokonać wielu innych płatności.


Zanim wyjaśnię ten proces, myślę, że ważne jest, aby przypomnieć, nad którymi indeksami obecnie pracujemy:


Opisujemy ścieżkę wyprowadzania kodu płatności w następujący sposób: m/47'/0'/0'/.


Następna głębokość rozdziela indeksy w następujący sposób:



- Pierwsza normalna (nieutwardzona) para dzieci jest używana do generate powiadomienia Address, które omówiliśmy w poprzedniej sekcji: m/47'/0'/0'/0/.



- Normalne pary kluczy podrzędnych są używane w ECDH do odbierania adresów płatności generate BIP47, jak zobaczymy w tej sekcji: m/47'/0'/0'/ od 0 do 2 147 483 647/.



- Wzmocnione pary kluczy podrzędnych to efemeryczne kody płatności: m/47'/0'/0'/ od 0' do 2 147 483 647'/.

Za każdym razem, gdy Alice chce wysłać płatność do Boba, uzyskuje nowy unikalny blank Address, ponownie dzięki protokołowi ECDH:


- Alice wybiera pierwszy klucz prywatny pochodzący z jej osobistego kodu płatności wielokrotnego użytku: **a**



- Alicja wybiera pierwszy nieużywany klucz publiczny pochodzący z kodu płatności Boba. Ten klucz publiczny nazwiemy "B". Jest on powiązany z kluczem prywatnym "b", który zna tylko Bob.

**B = b-G**



- Alicja oblicza tajny punkt "S" na krzywej eliptycznej, dodając i podwajając punkty, stosując swój klucz prywatny "a" do klucza publicznego "B" Boba:

**S = a-B**



- Na podstawie tego tajnego punktu Alicja obliczy wspólny tajny kod "s" (małymi literami). W tym celu wybiera współrzędną x tajnego punktu "S" o nazwie "Sx" i przekazuje tę wartość do funkcji SHA256 Hash.

**s = SHA256(Sx)**


Nie ufaj. Weryfikuj! Jeśli chcesz zrozumieć podstawowe zasady funkcji Hash, znajdziesz to, czego potrzebujesz w tym artykule. A jeśli nie ufasz NIST (masz rację) i chcesz być w stanie szczegółowo zrozumieć, jak działa SHA256, wyjaśniam wszystko w tym artykule w języku francuskim.



- Alicja używa współdzielonego sekretu "s" do obliczenia płatności Bitcoin otrzymując Address. Najpierw sprawdza, czy "s" mieści się w rzędzie krzywej secp256k1. Jeśli nie, zwiększa indeks klucza publicznego Boba, aby uzyskać kolejny wspólny klucz tajny.



- Po drugie, oblicza klucz publiczny "K0", dodając punkty "B" i "s-G" na krzywej eliptycznej. Innymi słowy, Alicja dodaje klucz publiczny uzyskany z kodu płatności Boba "B" do innego punktu obliczonego na krzywej eliptycznej poprzez dodanie i podwojenie punktów ze wspólnym sekretem "s" z punktu generatora krzywej secp256k1 "G". Ten nowy punkt reprezentuje klucz publiczny i nazywamy go "K0":

**K0 = B + s-G**



- Za pomocą tego klucza publicznego "K0" Alicja może wyprowadzić pusty klucz odbiorczy Address w standardowy sposób (na przykład SegWit V0 w Bech32).


Gdy Alicja otrzyma Address "K0" należący do Boba, może skonstruować standardową transakcję Bitcoin, wybierając UTXO należący do niej na innej gałęzi jej HD Wallet i wydając go na Address "K0" Boba.


![Alice sends bitcoins with BIP47 to Bob](assets/21.webp)


Kredyt: Kody płatności wielokrotnego użytku dla hierarchicznych portfeli deterministycznych, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki

Jeśli dopasujemy ten schemat do tego, co opisałem wcześniej:



- "Child Priv-Key" po stronie Alice odpowiada: a.
- "Child Pub-Key 0" po stronie Boba odpowiada: B.
- "Payment Secret 0" odpowiada: s.
- "Payment Pub-Key 0" odpowiada: K0.


Pozwolę sobie podsumować kroki, przez które właśnie przeszliśmy, aby wysłać płatność BIP47:



- Alice wybiera pierwszy pochodny klucz prywatny dziecka ze swojego osobistego kodu płatności.
- Oblicza tajny punkt na krzywej eliptycznej przy użyciu ECDH z pierwszego nieużywanego pochodnego klucza publicznego dziecka z kodu płatności Boba.
- Używa tego tajnego punktu do obliczenia współdzielonego klucza tajnego za pomocą SHA256.
- Używa tego wspólnego sekretu do obliczenia nowego tajnego punktu na krzywej eliptycznej.
- Dodaje ten nowy tajny punkt do klucza publicznego Boba.
- Uzyskuje nowy efemeryczny klucz publiczny, dla którego tylko Bob ma powiązany klucz prywatny.
- Alicja może wysłać zwykłą transakcję do Boba z pochodnym efemerycznym odbiorem Address.


Jeśli chce dokonać drugiej płatności, powtórzy powyższe kroki, z tym wyjątkiem, że wybierze drugi wyprowadzony klucz publiczny z kodu płatności Boba. Jest to następny nieużywany klucz. Otrzyma wtedy drugi otrzymany Address należący do Boba, "K1".


![Alice derives three BIP47 receiving addresses for Bob](assets/22.webp)


Kredyt: Kody płatności wielokrotnego użytku dla hierarchicznych portfeli deterministycznych, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Może kontynuować w ten sposób i uzyskać do 2^32 pustych adresów należących do Boba.


Z perspektywy zewnętrznej, obserwując Bitcoin Blockchain, teoretycznie niemożliwe jest odróżnienie płatności BIP47 od zwykłej płatności. Oto przykład transakcji płatności BIP47 na Testnet:


https://blockstream.info/Testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254


txid: **94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254**


Wygląda to jak zwykła transakcja z wydaną kwotą wejściową, płatnością wyjściową w wysokości 210 000 Sats i resztą.


![Bitcoin payment transaction with BIP47](assets/23.webp)


Kredyt: https://blockstream.info/


### Otrzymanie płatności BIP47 i uzyskanie klucza prywatnego.


Alice właśnie dokonała pierwszej płatności na rzecz pustego BIP47 Address należącego do Boba. Zobaczmy teraz, jak Bob otrzymuje tę płatność. Zobaczymy również, dlaczego Alicja nie ma dostępu do klucza prywatnego Address, który właśnie wygenerowała, i jak Bob odzyskuje ten klucz, aby wydać bitcoiny, które właśnie otrzymał.


Gdy tylko Bob otrzyma powiadomienie o transakcji od Alicji, uzyskuje klucz publiczny BIP47 "K0", jeszcze zanim wyśle ona do niego jakąkolwiek płatność. Obserwuje zatem każdą płatność na rzecz powiązanego Address. W rzeczywistości natychmiast uzyskuje kilka adresów, które będzie obserwował (K0, K1, K2, K3...). Oto jak uzyskuje klucz publiczny "K0":



- Bob wybiera pierwszy podrzędny klucz prywatny pochodzący z jego kodu płatności. Ten klucz prywatny nosi nazwę "b". Jest on powiązany z kluczem publicznym "B", którego Alice użyła w poprzednim kroku: **b**



- Bob wybiera pierwszy wyprowadzony klucz publiczny Alicji z jej kodu płatności. Klucz ten nosi nazwę "A". Jest on powiązany z kluczem prywatnym "a", którego Alicja użyła w swoich obliczeniach i o którym wie tylko ona. Bob może wykonać ten proces, ponieważ zna kod płatności Alicji, który został mu przesłany wraz z transakcją powiadomienia.

**A = a-G**



- Bob oblicza tajny punkt "S", dodając i podwajając punkty na krzywej eliptycznej, stosując swój klucz prywatny "b" do klucza publicznego "A" Alicji. Używamy tutaj ECDH, który gwarantuje, że punkt "S" będzie taki sam dla Boba i Alicji.

**S = b-A**



- Podobnie jak Alicja, Bob wyodrębnia współrzędną x tego punktu "S". Nazwaliśmy tę wartość "Sx". Przekazuje tę wartość przez funkcję SHA256, aby znaleźć wspólny sekret "s" (małymi literami).

**s = SHA256(Sx)**



- W taki sam sposób jak Alicja, Bob oblicza punkt "s-G" na krzywej eliptycznej. Następnie dodaje ten tajny punkt do swojego klucza publicznego "B". Następnie otrzymuje nowy punkt na krzywej eliptycznej, który interpretuje jako klucz publiczny "K0":

**K0 = B + s-G**


Gdy Bob posiada klucz publiczny "K0", może uzyskać powiązany z nim klucz prywatny w celu wydania swoich bitcoinów. Jest on jedyną osobą, która może generate tę liczbę.



- Bob dodaje swój pochodny klucz prywatny "b" ze swojego osobistego kodu płatności. Jest on jedyną osobą, która może uzyskać wartość "b". Następnie dodaje "b" do współdzielonego sekretu "s", aby uzyskać k0, klucz prywatny K0: **k0 = b + s**



- Dzięki prawu grupowemu krzywej eliptycznej Bob uzyskuje dokładnie taki klucz prywatny, jaki odpowiada kluczowi publicznemu użytemu przez Alicję. Mamy więc: **K0 = k0-G**


![Bob generates his BIP47 receiving addresses](assets/24.webp)


Kredyt: Kody płatności wielokrotnego użytku dla hierarchicznych portfeli deterministycznych, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Jeśli dopasujemy ten schemat do tego, co opisałem wcześniej:



- "Child Priv-Key 0" po stronie Boba odpowiada: b.



- "Child Pub-Key 0" po stronie Alice odpowiada: A.



- "Payment Secret 0" odpowiada: s.



- "Payment Pub-Key 0" odpowiada: K0.



- "Payment Priv-Key 0" odpowiada: k0.


Pozwolę sobie podsumować kroki, które właśnie wykonaliśmy, aby otrzymać płatność BIP47 i obliczyć odpowiadający jej klucz prywatny:



- Bob wybiera pierwszy pochodny klucz prywatny dziecka ze swojego osobistego kodu płatności.



- Oblicza tajny punkt na krzywej eliptycznej za pomocą ECDH z pierwszego wyprowadzonego klucza publicznego dziecka z kodu łańcucha Alicji.



- Używa tego tajnego punktu do obliczenia współdzielonego klucza tajnego za pomocą SHA256.



- Wykorzystuje ten wspólny sekret do obliczenia nowego tajnego punktu na krzywej eliptycznej.



- Dodaje ten nowy tajny punkt do swojego osobistego klucza publicznego.



- Uzyskuje on nowy efemeryczny klucz publiczny, do którego Alice wyśle swoją pierwszą płatność.



- Bob oblicza klucz prywatny powiązany z tym efemerycznym kluczem publicznym, dodając swój pochodny klucz prywatny z kodu płatności i współdzielonego sekretu.


Ponieważ Alicja nie może uzyskać "b", klucza prywatnego Boba, nie jest w stanie określić k0, klucza prywatnego powiązanego z BIP47 Boba odbierającego Address.


Schematycznie możemy przedstawić obliczenie współdzielonego sekretu "S" w następujący sposób:


![Calculation of the shared secret with ECDHE](assets/25.webp)


Po znalezieniu sekretu współdzielonego za pomocą ECDH, Alicja i Bob obliczają klucz publiczny płatności BIP47 "K0", a Bob również oblicza powiązany klucz prywatny "k0":


![Derivation of the BIP47 receiving address from the shared secret](assets/26.webp)


### Zwrot płatności za BIP47.


Ponieważ Bob zna kod płatności wielokrotnego użytku Alice, ma już wszystkie niezbędne informacje, aby wysłać jej zwrot pieniędzy. Nie będzie musiał kontaktować się z Alice, aby poprosić o jakiekolwiek informacje. Po prostu powiadomi ją za pomocą transakcji powiadamiającej, zwłaszcza aby mogła odzyskać swoje adresy BIP47 za pomocą seed, a następnie może wysłać jej do 2^32 płatności.

Bob może następnie zwrócić Alice pieniądze w ten sam sposób, w jaki ona wysłała mu płatności. Role są odwrócone:


![Bob sends a refund to Alice with BIP47](assets/27.webp)


Kredyt: Kody płatności wielokrotnego użytku dla hierarchicznych portfeli deterministycznych, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Teraz znasz już wszystkie tajniki tego wspaniałego rozwiązania, które reprezentuje BIP47.


## Pochodne zastosowania PayNym.


Wdrożenie tego BIP47 na Samourai Wallet zaowocowało PayNyms, identyfikatorami obliczanymi na podstawie kodów płatności użytkowników. Obecnie ich użyteczność wykracza daleko poza wykorzystanie BIP47.


Zespół Samourai stopniowo rozwija cały ekosystem narzędzi i usług opartych na PayNym użytkownika. Wśród nich są oczywiście wszystkie narzędzia do wydawania pieniędzy, które pozwalają zoptymalizować prywatność użytkownika poprzez dodanie entropii do transakcji, a tym samym dodanie wiarygodnego zaprzeczenia.


Połączone wykorzystanie Soroban, szyfrowanej sieci komunikacyjnej opartej na sieci Tor, i PayNyms znacznie zoptymalizowało doświadczenie użytkownika podczas tworzenia wspólnych transakcji, przy jednoczesnym zachowaniu dobrego poziomu bezpieczeństwa. W ten sposób łatwo jest wykonywać transakcje Stowaway (PayJoin) i StonewallX2 bez ręcznego wykonywania licznych wymian niepodpisanych transakcji wymaganych do skonfigurowania takiej wspólnej transakcji.


W przeciwieństwie do korzystania z BIP47, ponieważ te wspólne transakcje nie wymagają transakcji powiadomienia, wystarczy połączyć PayNyms, aby korzystać z tych narzędzi. Nie ma potrzeby ich łączenia.


Jeśli chcesz dowiedzieć się więcej o transakcjach opartych na współpracy, a szerzej o wszystkich narzędziach do wydawania pieniędzy w Samourai Wallet, możesz przeczytać sekcję "Narzędzia do wydawania pieniędzy" w tym artykule. Znajdziesz tam wyjaśnienie techniczne i szczegółowy samouczek dla każdego narzędzia.


Oprócz tych wspólnych transakcji, niedawno zaobserwowano, że zespół Samourai pracuje nad protokołem uwierzytelniania powiązanym z PayNym: Auth47. Narzędzie to jest już zaimplementowane i umożliwia na przykład uwierzytelnianie za pomocą PayNym na stronie internetowej, która akceptuje tę metodę. Myślę, że w przyszłości, poza możliwością uwierzytelniania w sieci, Auth47 będzie częścią większego projektu wokół ekosystemu BIP47/PayNym/Samourai. Być może protokół ten zostanie wykorzystany do dalszej optymalizacji doświadczenia użytkownika Samourai Wallet, zwłaszcza w zakresie korzystania z narzędzi do wydawania pieniędzy. To się jeszcze okaże...


## Moja osobista opinia na temat BIP47.


Oczywiście główną wadą BIP47 jest transakcja powiadomienia. Powoduje to, że użytkownik musi wydawać opłaty za Mining, co dla niektórych może być irytujące. Jednak argument "spamu" na Bitcoin Blockchain jest absolutnie nie do przyjęcia. Każdy, kto uiszcza opłaty za swoją transakcję, musi mieć możliwość zarejestrowania jej na Ledger, niezależnie od jej celu. Twierdzenie, że jest inaczej, to opowiadanie się za cenzurą.


Możliwe, że w przyszłości zostaną znalezione inne, tańsze rozwiązania umożliwiające przekazywanie kodu płatności nadawcy do odbiorcy i bezpieczne przechowywanie go przez odbiorcę. Ale na razie transakcja z powiadomieniem pozostaje rozwiązaniem o najmniejszej liczbie kompromisów.


Ta wada pozostaje nieistotna, biorąc pod uwagę wszystkie zalety BIP47. Spośród wszystkich istniejących propozycji rozwiązania problemu ponownego wykorzystania Address, wydaje mi się, że jest to najlepsze rozwiązanie.


Jak wyjaśniono wcześniej, większość ponownego wykorzystania Address pochodzi z giełd. BIP47 jest jedynym rozsądnym rozwiązaniem, które faktycznie rozwiązuje ten problem u jego źródła. Każda propozycja mająca na celu zmniejszenie liczby ponownych użyć Address powinna koncentrować się na tym aspekcie i dostosowywać rozwiązanie do głównego źródła problemu.


Pod względem użyteczności, mimo że jego wewnętrzne działanie jest dość złożone, procedura płatności BIP47 jest prosta. Kody płatnicze wielokrotnego użytku mogą być zatem łatwo przyjęte nawet przez początkujących użytkowników.


Pod względem prywatności BIP47 jest bardzo interesujący. Jak wyjaśniłem w sekcji dotyczącej transakcji powiadamiania, kod płatności nie ujawnia żadnych informacji o pochodnych adresach efemerycznych. W związku z tym przerywa przepływ informacji między transakcją Bitcoin a identyfikatorem odbiorcy, w przeciwieństwie do tradycyjnego użycia otrzymującego Address.


A przede wszystkim, implementacja BIP47 przez PayNym działa! Jest dostępna na Samourai Wallet od 2016 roku i na Sparrow Wallet od początku tego roku. Nie jest to projekt naukowy, ale rozwiązanie, które zostało przetestowane wczoraj i jest w pełni funkcjonalne dzisiaj.


Miejmy nadzieję, że w przyszłości te kody płatności wielokrotnego użytku zostaną przyjęte przez podmioty ekosystemu, zaimplementowane w oprogramowaniu Wallet i będą używane przez Bitcoinerów.


Każde prawdziwie pozytywne rozwiązanie dla prywatności użytkowników musi być dyskutowane, forsowane i bronione, aby Bitcoin nie stał się placem zabaw dla CA i narzędziem nadzoru rządów.

Myślał o tym, jak wszędzie był prześladowany i obrażany, a teraz słyszał, jak wszyscy mówią, że jest najpiękniejszym z tych wszystkich pięknych ptaków! I nawet czarny bez pochylił ku niemu swoje gałęzie, a słońce roztaczało takie ciepłe i dobroczynne światło! Wtedy jego pióra nabrzmiały, jego smukła szyja wyprostowała się, a on wykrzyknął z całego serca: "Jak mogłem marzyć o takim szczęściu, kiedy byłem tylko brzydkim małym kaczątkiem"


## Aby pójść dalej:



- Zrozumienie i korzystanie z CoinJoin na Bitcoin.



- Zrozumienie ścieżek wyprowadzania Bitcoin Wallet.



- Instalacja i korzystanie z węzła RoninDojo Bitcoin.


### Zasoby zewnętrzne i podziękowania:


Podziękowania dla LaurentMT i Théo Pantamis za liczne koncepcje, które mi wyjaśnili, a które wykorzystałem w tym artykule. Mam nadzieję, że przekazałem je dokładnie.


Podziękowania dla Fanisa Michalakisa za korektę tekstu i fachowe porady.



- https://bitcoiner.guide/paynym/
- https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols