---
name: Byk Bitcoin Wallet
description: Dowiedz się, jak korzystać z Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Ten przewodnik przeprowadzi Cię przez instalację, konfigurację i użytkowanie Bull Bitcoin Mobile. Dowiesz się, jak odbierać i wysyłać środki w trzech sieciach: onchain, Liquid i Lightning, a także jak przenieść Bitcoin z jednej sieci do drugiej. Dodatki zawierają zasoby i kontakty, informacje ogólne i krótkie wyjaśnienia pojęć technicznych.



## Wprowadzenie



**Bull Bitcoin Mobile**, opracowany przez **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([utwórz konto](https://app.bullbitcoin.com/registration/orangepeel)), jest **samodzielnym** Bitcoin Wallet, co oznacza, że masz pełną kontrolę nad swoimi kluczami prywatnymi, a tym samym swoimi środkami, bez zależności od strony trzeciej. Ten Wallet o otwartym kodzie źródłowym i zakorzeniony w filozofii Cypherpunk łączy w sobie prostotę, poufność i zaawansowane funkcje, takie jak swapy międzysieciowe i obsługa PayJoin. Pozwala zarządzać bitcoinami w trzech sieciach: **Bitcoin onchain**, **Liquid** i **Lightning**, z których każda jest dostosowana do konkretnych zastosowań.



### Kontekst rozwoju



Wallet stanowi odpowiedź na poważne wyzwanie: Opłaty sieciowe Bitcoin są nieodpowiednie dla małych płatności lub do otwierania małych, samodzielnie hostowanych kanałów Lightning. Wallet Bull Bitcoin Mobile oferuje rozwiązanie samoobsługowe, opierając się na 3 głównych sieciach Bitcoin:





- Sieć Bitcoin (onchain)**: Idealna do średnio- i długoterminowego przechowywania UTXO i transakcji o dużej wartości, gdzie opłaty są proporcjonalnie nieistotne.
- Liquid Network**: Zaprojektowany do szybkich (~2 minuty), bardziej poufnych (ukryte kwoty), tanich transakcji, idealny do gromadzenia małych kwot lub ochrony prywatności.
- Sieć Lightning**: Zoptymalizowana pod kątem natychmiastowych, tanich płatności, odpowiednia do codziennych transakcji o małej i średniej wartości.



Na przykład w przypadku Bull Bitcoin Mobile można gromadzić niewielkie kwoty w portfelach **Liquid** lub **Lightning**, a następnie, po osiągnięciu znacznej kwoty, można :





- Transfer do sieci onchain w celu bezpiecznego średnio- lub długoterminowego przechowywania, o zwiększonej poufności dzięki Liquid i/lub Lightning upstream oraz z opłatami onchain za pojedynczą transakcję



### Ciągła ewolucja



Wallet stale się rozwija, więc nie zdziw się, jeśli znajdziesz rozbieżności między tym samouczkiem a aktualną aplikacją.




- Na przykład od 19.07.2025 r. przyciski **"Kup / Sprzedaj / Zapłać "** są widoczne, ale wyszarzone w aplikacji, ponieważ opcje te, dostępne na Exchange [bullbitcoin.com] (https://app.bullbitcoin.com/registration/orangepeel), zostaną wkrótce zintegrowane w celu ujednolicenia doświadczenia. Ich użycie pozostanie całkowicie opcjonalne. Wiele innych zmian jest w toku lub jest planowanych: zarządzanie wieloma Wallet, passphrase, kompatybilność z portfelami sprzętowymi...
- Na [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) możesz sprawdzić aktualne tematy i nadchodzące zmiany. Ponieważ projekt jest w 100% open-source i "zbudowany publicznie", możesz również przesłać nam swoje sugestie i wszelkie napotkane błędy.




## 1. Wymagania wstępne



Przed rozpoczęciem korzystania z **Bull Bitcoin Mobile** upewnij się, że posiadasz następujące elementy:





- Kompatybilny smartfon**: Urządzenie z systemem **iOS** (iPhone lub iPad) lub **Android**
- Połączenie z Internetem
- Zabezpiecz nośnik kopii zapasowej**: Zapisz swoją **frazę odzyskiwania** (12 słów) na papierze lub metalu i przechowuj ją w bezpiecznym miejscu.
- Podstawowa wiedza**: Przydatne jest minimalne zrozumienie koncepcji Bitcoin (adresy, transakcje, opłaty), chociaż ten samouczek wyjaśnia każdy krok dla początkujących.



## 2. Instalacja





- Pobierz aplikację** :
 - [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Pobierz ze sklepu z aplikacjami na urządzenia z systemem Android
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Pobierz bezpośrednio APK na urządzenia z systemem Android**
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** Pobierz przez TestFlight dla urządzeń Apple
 - Sprawdź nazwę dewelopera (Bull Bitcoin), aby uniknąć fałszywych aplikacji.
 - Upewnij się, że pobrana wersja odpowiada najnowszej stabilnej wersji wskazanej na GitHub.
 - Bull Bitcoin Mobile jest aplikacją **open-source**. Aby zobaczyć kod: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Zainstaluj aplikację




## 3. Konfiguracja początkowa



### 3.1 Uruchom aplikację :



Aplikacja wykorzystuje unikalną 12-wyrazową frazę odzyskiwania dla obu portfeli:




 - bezpieczne Bitcoin' Wallet**: Dla transakcji w sieci Bitcoin (onchain)
 - gW-29**: Do natychmiastowych transakcji w sieciach Liquid i Lightning



Po otwarciu zostanie wyświetlony monit o zaimportowanie istniejącej frazy odzyskiwania lub utworzenie nowej Wallet :



![image](assets/fr/02.webp)



### 3.2 Fraza odzyskiwania :



Jeśli chcesz ponownie użyć istniejącego Wallet, kliknij "**Odzyskaj Wallet**" i wpisz 12 słów frazy odzyskiwania.



W przeciwnym razie kliknij "**Utwórz nowy Wallet**" :




- Zapisz swoją frazę odzyskiwania z najwyższą starannością. Zapisz ją na papierze lub metalu i przechowuj w bezpiecznym miejscu (skrytka depozytowa, lokalizacja offline). Ta fraza jest jedynym sposobem na uzyskanie dostępu do bitcoinów w przypadku utraty urządzenia lub usunięcia aplikacji.
- Ważne jest również, aby pamiętać, że każdy, kto ma tę frazę, może ukraść wszystkie twoje bitcoiny. Nigdy nie przechowuj ich cyfrowo:
 - Brak zrzutu ekranu
 - Brak kopii zapasowych w chmurze, poczcie e-mail lub wiadomościach
 - Brak funkcji kopiuj/wklej (ryzyko zapisania w schowku)



**! Ten punkt jest krytyczny**. W celu uzyskania dalszej pomocy :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Zabezpieczanie dostępu :





- Przejdź do ustawień, a następnie kliknij **Kod PIN**.
- Skonfiguruj solidny **kod PIN**, aby chronić dostęp do aplikacji.
- Ten krok jest opcjonalny, ale zdecydowanie zalecany, aby uniemożliwić osobom mającym dostęp do telefonu uzyskanie dostępu do Wallet.



![image](assets/fr/03.webp)



### 3.4 Połączenie z węzłem osobistym (opcjonalnie):



Wallet BullBitcoin domyślnie łączy się z serwerami Electrum: pierwszym zarządzanym przez Bull Bitcoin i dodatkowym serwerem od Blockstream, z których oba są uważane za nieprowadzące dzienników, co zmniejsza ryzyko śledzenia.



Dla większej poufności można podłączyć aplikację do własnego węzła Bitcoin za pośrednictwem serwera Electrum (instrukcje dostępne na [BullBitcoin's GitHub](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Otrzymywanie środków



Odbieranie środków za pomocą **Bull Bitcoin Mobile** jest proste i dostosowane do Twoich potrzeb, niezależnie od tego, czy korzystasz z :




  - sieć **Bitcoin (onchain)** dla długoterminowej ochrony,
  - sieć **Liquid** dla szybkiej, większej liczby Confidential Transactions,
  - sieć **Lightning** do natychmiastowych płatności o niskiej wartości.



Aplikacja automatycznie generuje adresy Lightning reception lub Invoice, w zależności od wybranej sieci. Oto jak postępować dla każdej sieci.



### 4.1. onchain (sieć Bitcoin)



Na ekranie głównym można :




- lub wybierz **Secure Bitcoin Wallet**, a następnie kliknij "**Odbierz "**:



![image](assets/fr/04.webp)





- lub kliknij "**Odbierz "**, a następnie wybierz sieć **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Opcja "Tylko kopiowanie lub skanowanie Address" wyłączona (domyślnie)



![image](assets/fr/06.webp)





- Daje to dostęp do opcjonalnych parametrów zaawansowanych. Można określić :
 - Kwota** w BTC, Sats lub fiat.
 - **osobista notatka**, która zostanie dołączona do kopii URI/kodu QR.
 - Aktywacja **PayJoin** (szczegóły w Załączniku 3), która poprawia poufność poprzez połączenie wpisów nadawcy i odbiorcy.





- Przykład automatycznie wygenerowanego identyfikatora URI** :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- Zastosowanie**: Skopiuj URI, aby udostępnić go nadawcy, lub pozwól mu zeskanować kod QR.



#### 4.1.2. Opcja "Tylko kopiowanie lub skanowanie Address" włączona



![image](assets/fr/07.webp)





- Po włączeniu opcji **"Kopiuj lub skanuj tylko Address"** aplikacja generuje prosty Bitcoin Address w formacie SegWit (bech32).





- Przykład:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Nawet jeśli wprowadzisz kwotę lub notatkę, nie zostaną one uwzględnione w kodzie QR ani w kopii Address





- Zastosowanie**: Skopiuj Address, aby udostępnić go nadawcy, lub pozwól mu zeskanować kod QR.



#### 4.1.3. Generowanie nowego Address





- Po co używać nowego Address dla każdej transakcji? To **chroni Twoją prywatność**, uniemożliwiając powiązanie wielu płatności z tym samym Address i ogranicza możliwości śledzenia na Blockchain.
 - Domyślnie Bull Bitcoin automatycznie generuje nieużywany Address.**
 - Możesz wymusić utworzenie nowego Address, klikając **"New Address"** w dolnej części ekranu.
 - Wszystkie adresy są powiązane z frazą seed: bez względu na to, z ilu adresów korzystasz, Twój portfel będzie wyświetlał jedno saldo i może automatycznie konsolidować środki po dokonaniu wysyłki.





- Wskazówka: Zawsze używaj nowego Address** dostarczonego przez Bull Bitcoin, chyba że masz konkretną potrzebę (np. publiczny Address do przyjmowania darowizn).



### 4.2. Liquid



Na ekranie głównym można :




- lub wybierz **Płatności natychmiastowe Wallet**, a następnie kliknij **"Odbierz "**, a następnie **"Liquid"**:



![image](assets/fr/08.webp)





- lub kliknij "**Odbierz "**, a następnie wybierz sieć **Liquid**:



![image](assets/fr/09.webp)



Po przejściu do ekranu **"Odbierz "** skopiuj Liquid Address:





- Brak kwoty lub uwagi. Przykład:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Lub określając **kwotę** (w BTC, Sats lub fiat) i/lub **osobistą notatkę**, która ma zostać dołączona do kopii URI / kodu QR. Przykład:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Użyj**: Skopiuj Address/URI, aby udostępnić go nadawcy, lub pozwól mu zeskanować kod QR.



### 4.3. Błyskawica



Na ekranie głównym można :




- lub wybrać **Płatności natychmiastowe Wallet**, a następnie kliknąć "**Odbierz "**:



![image](assets/fr/10.webp)





- lub kliknij "**Odbierz "**, a następnie wybierz sieć **Lightning**:



![image](assets/fr/11.webp)



#### 4.3.1. Działanie, ograniczenia i korzyści





- Mechanizm**: Bull Bitcoin Wallet to Wallet, który umożliwia dokonywanie i otrzymywanie płatności za pośrednictwem Lightning. Środki otrzymane za pośrednictwem Lightning są przechowywane w sieci **Liquid** (w Wallet Instant Payments) dzięki automatycznej wymianie za pośrednictwem **Boltz**. Daje to możliwość interakcji z Lightning bez konieczności zarządzania kanałami płynności, przy jednoczesnym zachowaniu własnego depozytu.





- Limity:**
 - Minimalna kwota** 100 satoshis (od 19.07.2025) przy generate Invoice.
 - Użytkownik ponosi koszty**, które zostaną odliczone od kwoty wysłanej przez nadawcę, w przeciwieństwie do odbioru za pomocą Wallet Lightning native, gdzie tylko nadawca płaci koszty przelewu oprócz wysłanej kwoty. Na dzień 19/07/2025, 47 Sats jest odliczanych od wysłanej kwoty.





- Korzyści** :
 - Samodzielne zarządzanie**: Twoje środki pozostają pod Twoją kontrolą, przechowywane na Liquid Network.
 - Brak wysokich opłat onchain**: Przechowywanie na Liquid pozwala uniknąć kosztownych depozytów onchain w celu otwarcia kanału Lightning lub dodania płynności. Operacje te można przeprowadzić później, gdy kwota zgromadzona na Liquid uzasadnia opłaty.





- Wskazówka:** Jeśli nadawca ma Wallet Bull Bitcoin, użyj Liquid Network bezpośrednio, aby uniknąć opłat za wymianę



#### 4.3.2. generate Invoice





- Wprowadź **kwotę** (w BTC, Sats lub fiat)





- Dodaj **osobistą notatkę**, która zostanie zintegrowana z Invoice. Jeśli nadawca zapłaci Invoice, Wallet będzie również zawierał to w szczegółach transakcji.





- Ważność Invoice:** Błyskawica Invoice jest ważna przez **12 godzin**. Po tym czasie wygasa i nie może być opłacony. Należy wygenerować nowy Invoice.





- Zastosowanie**: Skopiuj Invoice, aby udostępnić go nadawcy, lub pozwól mu zeskanować kod QR.




## 5. Wysyłanie funduszy



### 5.1. Podstawowa zasada



Albo ze strony głównej, albo z portfeli:



![image](assets/fr/12.webp)



aby przejść do ekranu wysyłania:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** ułatwia wysyłanie pieniędzy, automatycznie wykrywając sieć (Bitcoin, Liquid lub Lightning) na podstawie wprowadzonego Address lub Invoice (skopiowanego lub zeskanowanego za pomocą kodu QR).



### 5.2. transmisja łańcuchowa (sieć Bitcoin)



#### 5.2.1. Ekran wysyłania



**Akcja**: Wprowadź lub zeskanuj Bitcoin onchain Address





- Jeśli kwota nie została zdefiniowana, na przykład :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Następnie możesz wybrać na ekranie wysyłania :
 - Kwota w BTC, sat lub fiat. Minimalna kwota: 546 satoshis w dniu 22/07/2025.
 - Opcjonalna notatka identyfikująca transakcję. Widoczna tylko dla użytkownika w szczegółach transakcji.



![image](assets/fr/14.webp)





- Jeśli kwota została już zdefiniowana, na przykład :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Następnie zostaniesz przeniesiony bezpośrednio do poniższego ekranu potwierdzenia.



#### 5.2.2 Ekran potwierdzenia



Poświęć trochę czasu na sprawdzenie wszystkich parametrów, zwłaszcza kwoty, docelowego Address i opłat.


Następnie można dostosować parametry:



![image](assets/fr/15.webp)




- Opłaty**: Można wybrać :
  - Oszacowana zostanie szybkość realizacji** transakcji i związane z nią opłaty
  - Oszacowane zostaną opłaty** w trybie bezwzględnym (całkowite opłaty w satoshis) lub względnym (opłaty za bajt) oraz szybkość transakcji





- Ustawienia zaawansowane** :





 - Replace-by-fee (RBF)** : Aktywowana domyślnie, funkcja ta przyspiesza transakcję poprzez uiszczenie wyższej opłaty (szczegóły w Załączniku 4).





 - Ręczny wybór UTXO**: Jeśli środki są przechowywane pod kilkoma różnymi adresami Wallet, można wybrać adresy, z których mają zostać wysłane środki. Dlaczego warto to zrobić? Wraz ze wzrostem popularności Bitcoin rosną opłaty za przelewy. Wysyłanie z kilku adresów z małymi kwotami jest droższe niż wysyłanie z jednego Address, ale zrobienie tego teraz pozwala uniknąć konieczności robienia tego później, kiedy opłaty będą jeszcze wyższe. Nazywa się to **konsolidacją UTXO**



![image](assets/fr/16.webp)





- Wysyłanie za pomocą PayJoin**: Jeśli funkcja została aktywowana przez odbiorcę, który dostarczył URI, np :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Następnie Bull Bitcoin Mobile skonfiguruje wysyłanie, łącząc twoje UTXO z UTXO odbiorcy jako danymi wejściowymi, poprawiając poufność (szczegóły w Załączniku 3).



### 5.3. Wyślij do Liquid



#### 5.3.1 Ekran wysyłania



Sieć **Liquid** umożliwia szybkie transakcje (~2 minuty dzięki jednemu blokowi na minutę), bardziej poufne (zamaskowane kwoty) niż w sieci onchain i przy bardzo niskich opłatach. Środki są wypłacane z **Instant Payments Wallet**.



**Akcja**: Wprowadź lub zeskanuj Liquid Address





- Jeśli kwota nie została zdefiniowana, na przykład :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Następnie możesz wybrać na ekranie wysyłania :




- Kwota w BTC, sat lub fiat. Brak minimum, możliwy 1 Satoshi;
- Opcjonalna notatka identyfikująca transakcję. Widoczna tylko dla użytkownika w szczegółach transakcji.



![image](assets/fr/17.webp)





- Jeśli kwota została już zdefiniowana, na przykład :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Następnie zostaniesz przeniesiony bezpośrednio do poniższego ekranu potwierdzenia.



#### 5.3.2 Ekran potwierdzenia



Poświęć trochę czasu na sprawdzenie wszystkich parametrów, zwłaszcza ilości i miejsca docelowego Address.



![image](assets/fr/18.webp)





- Opłaty**: Proporcjonalnie do złożoności transakcji, zazwyczaj na podstawie 0,1 sat/vB, tj. 20-40 sat za prostą transakcję (33 Sats na dzień 22.07.2025).



### 5.4. Wyślij do Lightning



#### 5.4.1 Ekran wysyłania



Sieć **Lightning** umożliwia natychmiastowe, tanie płatności na niewielkie kwoty, idealne do małych codziennych transakcji.



**Akcja**: Wprowadź lub zeskanuj Lightning Invoice





- W przypadku zeskanowania LN-URL Address, który umożliwia ustawienie ilości


Przykład: `orangepeel@walletofsatoshi.com`.


następnie można wybrać na ekranie wysyłania :




 - Kwota w BTC, sat lub fiat. Minimalna kwota 1000 satoshis w dniu 23/07/2025 r
 - Opcjonalna notatka identyfikująca transakcję. Zostanie ona wysłana do odbiorcy.



![image](assets/fr/19.webp)





- W przypadku zeskanowania urządzenia Lightning Invoice zawierającego określoną ilość


Przykład:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Następnie zostaniesz przeniesiony bezpośrednio do poniższego ekranu potwierdzenia.



Uwaga: kwota musi być większa niż 21 Sats w dniu 23.07.2025 r



#### 5.4.2 Działanie, ograniczenia i korzyści





- Mechanizm**: Środki są pobierane z **Instant Payments Wallet** (Liquid) i konwertowane poprzez **Liquid → Lightning** swap z **Boltz**.





- Limity:**
 - Minimalna kwota** wyższa niż Wallet Lightning native (patrz wyżej)
 - Wydatki** plus Liquid → Błyskawiczna wymiana przez Boltza





- Korzyści** :
 - Samodzielne zarządzanie**: Środki pozostają pod kontrolą użytkownika, są przechowywane na Liquid Network i w razie potrzeby można je przesyłać za pośrednictwem usługi Lightning
 - Brak wysokich opłat onchain**: Przechowywanie na Liquid pozwala zaoszczędzić na kosztownych depozytach onchain w celu otwarcia kanału Lightning lub dodania płynności. Operacje te można przeprowadzić później, gdy kwota zgromadzona na Liquid uzasadnia opłaty.





- Wskazówka:** Jeśli odbiorca posiada Wallet Bull Bitcoin, użyj Liquid Network bezpośrednio, aby uniknąć kosztów wymiany



#### 5.3.3 Ekran potwierdzenia



Poświęć trochę czasu na sprawdzenie wszystkich parametrów, zwłaszcza ilości i miejsca docelowego Address.



![image](assets/fr/20.webp)




## 6. Wyświetl historię



**Bull Bitcoin Mobile** ułatwia śledzenie transakcji w sieciach **Bitcoin (onchain)**, **Liquid** i **Lightning**. Dostęp do historii można uzyskać na dwa sposoby i wyświetla ona szczegółowe informacje dla każdego rodzaju transakcji. Możesz również sprawdzić swoje transakcje za pomocą zewnętrznych przeglądarek bloków.



### 6.1. Historia dostępu





- Za pośrednictwem ekranu głównego** :
 - Kliknij na **Secure Bitcoin Wallet**, aby wyświetlić transakcje **onchain**, lub na **Instant Payments Wallet** dla **Liquid** i **Lightning**.
 - Historia jest wyświetlana bezpośrednio pod sumą portfela, filtrowana zgodnie z wybranym typem Wallet.



![image](assets/fr/21.webp)





- Za pośrednictwem dedykowanej strony** :
 - Na ekranie głównym kliknij symbol **historii** (ikona zegara lub podobna).
 - Dostęp do strony z listą wszystkich transakcji, z filtrami według typu akcji: **Wyślij**, **Odbierz**, **Zamień**, **PayJoin**, **Sprzedaj**, **Kup** (uwaga: opcje Sprzedaj i Kup są w trakcie opracowywania i nie są obecnie dostępne, 20 lipca 2025 r.).



![image](assets/fr/22.webp)



### 6.2. Szczegóły transakcji



Każda transakcja wyświetla określone informacje w zależności od sieci i rodzaju działania (wysyłanie lub odbieranie). Oto szczegóły dostępne dla **transakcji onchain**:



![image](assets/fr/23.webp)



### 6.3. Sprawdzanie przez Block explorer



Lista eksploratorów dla sieci **Bitcoin onchain**, **Liquid** i **Lightning** znajduje się w Załączniku 4.



W przypadku **Lightning** transakcje nie są widoczne w publicznych przeglądarkach. Sprawdź szczegóły (w tym Swap ID dla Boltz) w aplikacji.




## 7. Ustawienia



Strona "Ustawienia" jest dostępna bezpośrednio ze strony głównej aplikacji Bull Bitcoin i służy do konfigurowania i zarządzania różnymi aspektami portfolio i doświadczenia użytkownika.



![image](assets/fr/24.webp)





- Wallet Kopia zapasowa**: Wyświetla frazę odzyskiwania portfela dla bezpiecznej kopii zapasowej. Najlepsze praktyki w zakresie zarządzania i przechowywania frazy odzyskiwania znajdują się w sekcji 3. dotyczącej tworzenia portfela.





- Szczegóły Wallet** :
 - Pubkey**: Klucz publiczny powiązany z Wallet, używany do adresów odbioru generate Bitcoin.
 - Ścieżka pochodna**: Ścieżka pochodna używana do adresów generate Wallet z klucza prywatnego.





- Serwer Electrum (węzeł Bitcoin)**: Skonfiguruj połączenie z niestandardowym węzłem Bitcoin dla transakcji onchain.





- Kod PIN**: Aktywacja i/lub modyfikacja kodu zabezpieczającego w celu ochrony dostępu do aplikacji i funkcji Wallet.





- Waluta**: Wybierz, czy kwoty mają być wyświetlane w BTC czy Sats, oraz domyślną walutę fiducjarną (dolar, euro itp.).





- Ustawienia automatycznej wymiany**: Funkcja _Auto Swap_ pozwala zautomatyzować transfer BTC z **Instant Payments Wallet (Liquid)** do **Bitcoin On-Chain** Wallet, gdy tylko kwota osiągnie próg, który uznasz za wystarczająco wysoki, aby uzasadnić opłatę transakcyjną.





- Dzienniki**: Wyświetlane dzienniki aktywności, które mogą być udostępniane działowi pomocy technicznej w celu ułatwienia rozwiązywania problemów.





- Dostęp do pomocy technicznej przez Telegram** : Bezpośredni link do oficjalnego kanału Telegram w celu uzyskania pomocy.





- Dostęp do Github** : Link do repozytorium [Bull Bitcoin Github](https://github.com/SatoshiPortal) w celu przeglądania kodu open-source lub zgłaszania problemów.




## DODATKI



### A1. Wyjaśnienie PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definicja** :




- PayJoin lub **Pay-to-EndPoint (P2EP)** to technika transakcji Bitcoin, która zwiększa poufność w sieci **onchain**. Łączy ona wpisy nadawcy i odbiorcy w jednej transakcji, dzięki czemu kwoty i adresy są trudniejsze do wyśledzenia.



**Operacja:**




- W transakcji PayJoin nadawca i odbiorca współpracują ze sobą za pośrednictwem kompatybilnego serwera PayJoin w celu generate wspólnej transakcji.
- Zamiast tylko nadawcy dostarczającego wpisy (UTXO), odbiorca również wnosi swój wkład w postaci jednego z własnych UTXO. Powoduje to rozmycie informacji widocznych na Blockchain: zamiast jednego wpisu odpowiadającego rzeczywistej kwocie, są teraz dwa wpisy, a dane wyjściowe nie odzwierciedlają bezpośrednio wymienionej kwoty.
- Ostateczna transakcja przypomina standardową transakcję Bitcoin (wiele wejść / wiele wyjść), ale ukrywa rzeczywistą wysłaną kwotę i powiązania między adresami dzięki strukturze steganograficznej.



**Do użytku w Bull Bitcoin Mobile**




- Odbiór** (Address Supply): PayJoin jest domyślnie włączony.
- Wyślij** : Wallet automatycznie wykrywa URI PayJoin i odpowiednio konfiguruje transakcję, na przykład:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Korzyści**




- Zwiększona poufność**: PayJoin unieważnia założenie, że wszystkie wpisy w transakcji należą do jednego podmiotu. Dzięki PayJoin dane wejściowe pochodzą zarówno od nadawcy, jak i odbiorcy, łamiąc to założenie.
- Maskowanie kwoty** : Rzeczywista kwota wymiany nie pojawia się bezpośrednio w wynikach. Jest ona obliczana jako różnica między przychodzącym i wychodzącym UTXO odbiorcy, co sprawia, że analiza jest myląca.



**Limity**




- PayJoin wymaga, aby nadawca i odbiorca korzystali z kompatybilnych portfeli, w przeciwnym razie używana jest standardowa transakcja onchain.
- Transakcja jest nieco bardziej złożona (więcej wejść i wyjść), co skutkuje nieco wyższymi kosztami.
- Chociaż zaprojektowano go tak, aby przypominał standardową transakcję, zaawansowana heurystyka (np. niejednoznaczne dane wyjściowe, znane serwery PayJoin) może prowadzić do podejrzeń o jego użycie, choć bez absolutnej pewności.



**Więcej informacji:**




- [Glosariusz](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Wyjaśnienie Replace-by-fee (RBF)



**Definicja**: Replace-by-fee (RBF) to funkcja sieci Bitcoin, która umożliwia nadawcy przyspieszenie potwierdzenia transakcji **onchain** poprzez wyrażenie zgody na uiszczenie wyższej opłaty.



**Limity** :




- RBF nie jest dostępny dla transakcji Liquid lub Lightning.
- Początkowa transakcja musi być oznaczona jako zgodna z RBF podczas jej tworzenia, co Bull Bitcoin Mobile robi automatycznie, chyba że jest wyłączona.



**Więcej informacji:**




- [Glosariusz](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Najlepsze praktyki



Aby bezpiecznie i wydajnie korzystać z **Bull Bitcoin Mobile**, należy przestrzegać poniższych zaleceń. Pomogą one chronić środki, zoptymalizować transakcje i zachować poufność w sieciach **Bitcoin (onchain)**, **Liquid** i **Lightning**.





- Zabezpiecz swoją frazę odzyskiwania** :
 - Samouczek: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Użyj bezpiecznego uwierzytelniania** :
 - Aktywuj **silny kod PIN** lub **uwierzytelnianie biometryczne** (odcisk palca lub rozpoznawanie twarzy), aby chronić dostęp do aplikacji.
 - Nigdy nie udostępniaj swojego kodu PIN ani danych biometrycznych.





- Chroń swoją prywatność** :
 - generate nowy Address dla każdego odbioru onchain lub Liquid w celu ograniczenia śledzenia na Blockchain.
 - Użyj PayJoin, jeśli jest dostępny, aby zwiększyć poufność w odniesieniu do kwoty wysyłanej w łańcuchu
 - Aby zapewnić maksymalną poufność, połącz swój Wallet z własnym węzłem Bitcoin za pośrednictwem serwera Electrum zamiast korzystać z węzła publicznego





- Wybierz sieć najlepiej dopasowaną do Twoich potrzeb** :
 - Onchain**: Preferowany w przypadku długoterminowego przechowywania lub transakcji o dużej wartości (opłaty nieistotne w stosunku do kwoty).
 - Liquid**: Służy do szybkich, tanich transferów o zwiększonej poufności.
 - Błyskawica**: Wybierz natychmiastowe, tanie przelewy dla małych kwot. Jeśli masz dwóch użytkowników Wallet Bull Bitcoin, wybierz Liquid, aby uniknąć opłat za wymianę Lightning <> Liquid przez Boltz.





- Zawsze sprawdzaj adresy wysyłki**:
 - Przed wysłaniem środków należy dokładnie sprawdzić Address. Środki wysłane na niewłaściwy Address zostaną bezpowrotnie utracone. Używaj funkcji kopiuj/wklej lub skanowania kodów QR, nigdy nie kopiuj/modyfikuj Address ręcznie.





- Optymalizacja kosztów** :
 - W przypadku transakcji onchain należy wybrać odpowiednie opłaty (wolne, średnie, szybkie) w zależności od pilności i przeciążenia sieci.
 - Użyj Liquid lub Lightning dla małych ilości.
 - Aktywuj Replace-by-fee (RBF) (patrz Załącznik 4) dla przesyłek łańcuchowych, jeśli przewidujesz potrzebę przyspieszenia potwierdzenia.





- Aktualizuj aplikację na bieżąco




### A4. Dodatkowe zasoby





- Oficjalne linki i wsparcie:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : e-mail wsparcia
 - [Oficjalna strona Bull Bitcoin](https://bullbitcoin.com/) :** Informacje o usługach Bull Bitcoin, tworzenie konta, dostęp do aplikacji
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Przeglądaj kod, ewolucję i mapę drogową, przyczyniaj się do rozwoju...
 - [Konto X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
 - Grupa Telegram** dla Wallet mobile: czat grupowy z pomocą techniczną, patrz strona "Ustawienia".





- Block Explorers :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Błyskawica: **[1ML (Lightning Network)](https://1ml.com/)**





- Nauka i samouczki:** **[Plan ₿ Network](https://planb.network/)** :
 - Zabezpieczanie frazy odzyskiwania



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Glosariusz](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** :
 - [Glosariusz](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin



#### Przegląd firmy



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, to najstarsza nie-depozytowa platforma Exchange poświęcona wyłącznie Bitcoin, założona w 2013 roku w Ambasadzie Bitcoin w Montrealu w Kanadzie. Kierowana przez Francisa Pouliota, uznanego pioniera w ekosystemie Bitcoin, firma pozycjonuje się jako kluczowy gracz w promowaniu suwerenności finansowej i autonomii użytkowników. Jej misją jest umożliwienie jednostkom odzyskania kontroli nad swoimi pieniędzmi poprzez wykorzystanie Bitcoin jako narzędzia wolności i płatności, przy jednoczesnym odrzuceniu walut fiducjarnych i kryptowalut innych niż Bitcoin.



![image](assets/fr/26.webp)



[Utwórz konto](https://app.bullbitcoin.com/registration/orangepeel) z 0,25% rabatem na zakupy i sprzedaż Bitcoin.



#### Wartości i filozofia



Bull Bitcoin wyróżnia się zasadami Commitment do Cypherpunk i etyką Bitcoin:





- Skupiamy się wyłącznie na Bitcoin** : Platforma jest wierna wizji zdecentralizowanej, odpornej na cenzurę waluty.





- Non-custodian** : Użytkownicy zachowują pełną kontrolę nad swoimi Bitcoinami, wysyłając środki do własnych portfeli.





- Poufność**: Zminimalizowane gromadzenie danych osobowych, z opcjami zakupu bez KYC dla transakcji poniżej 999 USD. Dane są chronione zgodnie z przepisami (FINTRAC w Kanadzie, AMF we Francji).





- Przejrzystość**: Brak ukrytych opłat, koszty są wliczone w spread (różnicę między ceną kupna i sprzedaży).





- Suwerenność finansowa**: Bull Bitcoin promuje niezależność od tradycyjnych systemów bankowych i scentralizowanych instytucji.



#### Główne usługi





- Depozyt fiat** : Użytkownicy mogą zasilić swoje konto Bull Bitcoin walutą fiducjarną (CAD, EUR itp.) za pomocą przelewu bankowego lub gotówki/karty debetowej w wybranych kanadyjskich urzędach pocztowych.





- Zakup Bitcoin** : Użytkownicy mogą zakupić Bitcoin, który jest wysyłany bezpośrednio do ich portfela niedepozytowego, gwarantując całkowitą kontrolę nad ich funduszami.





- Zaplanowany zakup Bitcoin**: Bull Bitcoin oferuje zautomatyzowaną usługę cyklicznego zakupu (DCA - Dollar Cost Averaging) w regularnych odstępach czasu, czerpiąc z dostępnego salda, z bezpośrednim transferem Bitcoinów do kontrolowanego przez użytkownika Wallet, zmniejszając wpływ zmienności cen.



Należy pamiętać, że opcja o nazwie "AutoBuy" umożliwia konwersję fiatów, gdy tylko dotkną one salda Bull Bitcoin, i wysyłanie Bitcoinów do własnego Wallet. Opcja ta może być również połączona z cyklicznym przelewem bankowym zaplanowanym w banku w celu wykonania DCA. Ta opcja automatyzuje akumulację Bitcoin bez konieczności otwierania aplikacji.






- Kupno Bitcoin po ustalonej cenie "Limit Order "**: Umożliwia kupno Bitcoin po cenie określonej z góry przez użytkownika, która jest automatycznie realizowana, gdy cena indeksu Bull Bitcoin osiągnie lub spadnie poniżej ustalonego limitu.





- Sprzedaż Bitcoin**: Użytkownicy mogą sprzedawać swoje Bitcoiny i otrzymywać środki w walucie fiat bezpośrednio na swoje konto bankowe za pośrednictwem przelewu bankowego lub przelewu SEPA.





- Płatności zewnętrzne**: Bull Bitcoin umożliwia użytkownikom wysyłanie pieniędzy fiducjarnych na konta bankowe z ich Bitcoinów, całkowicie transparentnie dla odbiorcy.





- Bull Bitcoin Prime**: Bull Bitcoin Prime to usługa premium dla klientów zamożnych i korporacyjnych, oferująca spersonalizowane rozwiązania i wsparcie premium. Obejmuje to dostęp do obniżonych opłat, dedykowanego menedżera konta i dostosowanych usług korporacyjnych. Usługa ta skierowana jest do instytucji, profesjonalnych traderów i klientów korporacyjnych poszukujących dogłębnej wiedzy specjalistycznej i priorytetowego traktowania.





- Mobilny Wallet**: Bull Bitcoin oferuje open-source'ową, samowystarczalną mobilną Wallet, dostępną na Androida i iOS, która obsługuje transakcje onchain, Liquid i Lightning Network.





- Wsparcie edukacyjne**: Bezpłatne przewodniki i spersonalizowany coaching, aby pomóc użytkownikom w tworzeniu, zabezpieczaniu i zarządzaniu portfelami Bitcoin, wzmacniając autonomię finansową.



#### Zgodność i bezpieczeństwo





- Regulacje**: Zarejestrowany w FINTRAC (Kanada) i AMF (Francja), Bull Bitcoin spełnia wymogi KYC/AML.





- Bezpieczeństwo**: Korzystanie z bezpiecznych portfeli i zaleceń dotyczących przechowywania offline. Dane osobowe są przechowywane w infrastrukturze Bitcoin firmy Bull, która jest w 100% hostowana samodzielnie i nie zależy od żadnej strony trzeciej.