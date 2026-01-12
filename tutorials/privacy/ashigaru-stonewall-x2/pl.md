---
name: Ashigaru - Stonewall x2
description: Zrozumienie i używanie transakcji Stonewall x2 na Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Niech każdy wydatek będzie połączeniem monet

## Co to jest transakcja Stonewall x2?



Stonewall x2 to specyficzna forma transakcji Bitcoin zaprojektowana w celu zwiększenia poufności użytkownika podczas dokonywania wydatków poprzez współpracę z osobą trzecią niezaangażowaną w wydatki. Metoda ta symuluje mini-coinjoin między dwoma uczestnikami, podczas dokonywania płatności na rzecz strony trzeciej. Transakcje Stonewall x2 są dostępne w aplikacji Ashigaru, fork od Samourai Wallet (zespołu stojącego za stworzeniem tego typu transakcji).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Sposób działania jest stosunkowo prosty: użytkownik korzysta z posiadanego UTXO w celu dokonania płatności i korzysta z pomocy osoby trzeciej, która również korzysta z własnego UTXO. Transakcja kończy się czterema wyjściami: dwa z nich w równych kwotach, jeden przeznaczony na adres odbiorcy, drugi na adres należący do współpracownika. Trzeci UTXO jest zwracany na inny adres należący do współpracownika, umożliwiając mu odzyskanie początkowej kwoty (działanie neutralne dla niego, pomijając koszty mining), a ostatni UTXO wraca na adres należący do nas, co stanowi wymianę płatności.



W ten sposób w transakcjach Stonewall x2 zdefiniowano trzy różne role:




- Emitent, który dokonuje faktycznej płatności;
- Współpracownik, który udostępnia bitcoiny w celu zwiększenia anonimowości transakcji, jednocześnie odzyskując swoje środki w całości na koniec (działanie neutralne dla niego, modulując koszty mining);
- Odbiorca, który może być nieświadomy szczególnego charakteru transakcji i po prostu oczekuje płatności od nadawcy.



Weźmy przykład. Alice jest u piekarza, aby kupić bagietkę, która kosztuje `4,000 sats`. Chce zapłacić bitcoinami, zachowując przy tym pewną poufność co do swojej płatności. Wzywa więc swojego przyjaciela Bob, który jej w tym pomoże.



![image](assets/fr/01.webp)



Analizując tę transakcję widzimy, że piekarz faktycznie otrzymał `4,000 sats` jako zapłatę za bagietkę. Alice wykorzystał `10 000 sats` na wejściu i odzyskał `6 000 sats` na wyjściu, co daje saldo netto w wysokości `4 000 sats`, co odpowiada cenie bagietki. Jeśli chodzi o Bob, dostarczył on `15.000 sats` na wejściu i otrzymał dwa wyjścia: jedno o wartości `4.000 sats` i drugie o wartości `11.000 sats`, co daje saldo `0`.



W tym przykładzie celowo pominąłem opłaty mining, aby ułatwić jego zrozumienie. W rzeczywistości opłaty transakcyjne są dzielone równo między wydawcę płatności i współpracownika.



## Jaka jest różnica między Stonewall a Stonewall x2?



Transakcja StonewallX2 działa dokładnie w taki sam sposób jak transakcja Stonewall, z tym wyjątkiem, że ta pierwsza jest oparta na współpracy, podczas gdy druga nie. Jak widzieliśmy, transakcja Stonewall x2 obejmuje udział strony trzeciej, która jest zewnętrzna w stosunku do płatności i która udostępni swoje bitcoiny w celu zwiększenia poufności transakcji. W klasycznej transakcji Stonewall rolę współpracownika przejmuje nadawca.



Wróćmy do naszego przykładu Alice w piekarni. Gdyby nie była w stanie znaleźć kogoś takiego jak Bob, aby towarzyszył jej w szaleństwie wydatków, mogłaby sama wykonać Stonewall. W ten sposób dwa UTXO przy wejściu byłyby jej, a przy wyjściu zgarnęłaby 3.



![image](assets/fr/02.webp)




Z punktu widzenia osoby postronnej transakcja pozostałaby bez zmian.



![image](assets/fr/05.webp)



Logika powinna być zatem następująca, gdy chcesz użyć narzędzia do wydawania Ashigaru:




- Jeśli sprzedawca nie obsługuje Payjoin Stowaway, możesz dokonać wspólnej transakcji z inną osobą poza płatnością dzięki Stonewall x2 ;
- Jeśli nie możesz znaleźć nikogo, kto dokonałby transakcji Stonewall x2, możesz dokonać transakcji Stonewall only, która będzie naśladować zachowanie transakcji Stonewall x2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Jaki jest sens transakcji Stonewall x2?



Struktura Stonewall x2 dodaje ogromną ilość entropii do transakcji, myląc analizę łańcucha. Patrząc z zewnątrz, taka transakcja może być interpretowana jako mały Coinjoin między dwiema osobami. Ale w rzeczywistości jest to płatność. Metoda ta powoduje zatem niepewność w analizie łańcucha, a nawet prowadzi do fałszywych tropów.



Weźmy przykład Alice, Bob i Boulanger. Transakcja na blockchainie wyglądałaby następująco:



![image](assets/fr/03.webp)



Zewnętrzny obserwator polegający na heurystyce analizy łańcucha może błędnie dojść do wniosku, że "*Alice i Bob wykonały mały coinjoin, z jednym UTXO na wejściu i dwoma UTXO na wyjściu*".



![image](assets/fr/04.webp)



Ta interpretacja jest błędna, ponieważ, jak wiadomo, UTXO został wysłany do Boulanger, Alice ma tylko jedno wyjście wymiany, a Bob ma dwa.



![image](assets/fr/01.webp)



Nawet jeśli zewnętrzny obserwator zdoła zidentyfikować stronę transakcji Stonewall x2, nie będzie miał wszystkich informacji. Nie będzie w stanie określić, który z dwóch UTXO o tych samych kwotach odpowiada płatności. Nie będzie też w stanie określić, czy płatności dokonał Alice czy Bob. Wreszcie, nie będzie w stanie ustalić, czy dwa wprowadzone UTXO pochodzą od dwóch różnych osób, czy też należą do jednej osoby, która je połączyła. Ten ostatni punkt wynika z faktu, że klasyczne transakcje Stonewall, omówione powyżej, przebiegają dokładnie według tego samego schematu, co transakcje Stonewall x2. Patrząc z zewnątrz i bez dodatkowych informacji kontekstowych, niemożliwe jest odróżnienie transakcji Stonewall od transakcji Stonewall x2. Te pierwsze nie są transakcjami opartymi na współpracy, podczas gdy te drugie są. Dodaje to jeszcze więcej wątpliwości do wydatków.



![image](assets/fr/05.webp)




## Jak ustanowić połączenie między Paynyms?



Podobnie jak w przypadku innych transakcji opartych na współpracy na Ashigaru (*Cahoots*), Stonewall x2 obejmuje wymianę częściowo podpisanych transakcji między nadawcą a współpracownikiem. Wymiana ta może być przeprowadzona ręcznie, jeśli jesteś fizycznie obecny ze swoim współpracownikiem, lub automatycznie przy użyciu protokołu komunikacyjnego Soroban.



Jeśli wybierzesz drugą opcję, będziesz musiał ustanowić połączenie między Paynymami, zanim będziesz mógł wykonać Stonewall x2. Aby to zrobić, twój Paynym musi "*podążać*" za Paynym twojego współpracownika i vice versa. Aby dowiedzieć się, jak to zrobić, postępuj zgodnie z początkiem tego samouczka:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Jak mogę dokonać transakcji Stonewall x2 na Ashigaru?



Aby przeprowadzić transakcję Stonewall x2, kliknij obraz swojego Paynym w lewym górnym rogu ekranu, a następnie otwórz menu `Współpracuj`. Osoba biorąca udział w transakcji musi zrobić to samo, chyba że wymieniacie się kodami QR osobiście.



![Image](assets/fr/06.webp)



Masz dwie opcje: wybierz `Initiate`, jeśli jesteś nadawcą płatności, lub `Participate`, jeśli jesteś osobą współpracującą przy transakcji, ale nie jesteś ani płatnikiem, ani faktycznym odbiorcą.



![Image](assets/fr/07.webp)



Jeśli masz rolę współpracownika, procedura jest bardzo prosta. W przypadku zdalnej współpracy za pośrednictwem sieci Soroban, kliknij `Uczestnicz`, wybierz konto, którego chcesz użyć, a następnie naciśnij `OCZEKIWAJ NA ŻĄDANIA POBRANIA`, aby poczekać na żądanie wysłane przez płatnika.



![Image](assets/fr/08.webp)



Z drugiej strony, w przypadku współpracy osobistej poprzez skanowanie kodu QR, przejdź do strony głównej wallet, naciśnij ikonę kodu QR u góry ekranu, a następnie zeskanuj kod QR dostarczony przez płatnika inicjującego transakcję.



![Image](assets/fr/09.webp)



Jeśli jesteś w roli płatnika, tj. osoby inicjującej transakcję, przejdź do menu `Współpracuj`, a następnie wybierz `Inicjuj`.



![Image](assets/fr/10.webp)



Dla typu transakcji, ponieważ chcemy wykonać Stonewall x2, wybierz tę opcję.



![Image](assets/fr/11.webp)



Następnie można wybrać między współpracą online (*Cahoots* za pośrednictwem *Soroban*) lub współpracą twarzą w twarz, z wymianą kodów QR.



![Image](assets/fr/12.webp)



### Cahoots online



Jeśli wybrałeś opcję `Online`, wybierz swojego współpracownika z Paynyms, których obserwujesz.



![Image](assets/fr/13.webp)



Kliknij `Set up transaction`, a następnie wybierz konto, z którego chcesz dokonać wydatku.



![Image](assets/fr/14.webp)



Na następnej stronie wprowadź szczegóły transakcji: adres rzeczywistego odbiorcy płatności, kwotę do wysłania i stawkę opłaty. Następnie kliknij `Przejrzyj konfigurację transakcji`.



![Image](assets/fr/15.webp)



Sprawdź dokładnie informacje, upewnij się, że twój współpracownik słucha żądań *Cahoots*, a następnie kliknij zielony przycisk `BEGIN TRANSACTION`, aby zainicjować wymianę PSBT przez Soroban.



![Image](assets/fr/16.webp)



Poczekaj, aż obaj uczestnicy podpiszą transakcję, a następnie wyemituj ją w sieci Bitcoin.



![Image](assets/fr/17.webp)



### Rozmowy twarzą w twarz



Jeśli chcesz przeprowadzić wymianę osobiście, wybierz typ transakcji `STONEWALL X2`, a następnie wybierz opcję `In Person / Manual`.



![Image](assets/fr/18.webp)



Kliknij `Set up transaction`, a następnie wybierz konto, z którego chcesz dokonać wydatku.



![Image](assets/fr/19.webp)



Na następnej stronie wprowadź szczegóły transakcji: adres rzeczywistego odbiorcy płatności, kwotę do wysłania i stawkę opłaty. Następnie kliknij `Przejrzyj konfigurację transakcji`.



![Image](assets/fr/20.webp)



Sprawdź szczegóły, a następnie naciśnij zielony przycisk "ROZPOCZNIJ TRANSAKCJĘ", aby rozpocząć wymianę PSBT za pomocą skanowania kodu QR.



![Image](assets/fr/21.webp)



Wymiana odbywa się poprzez naprzemienne skanowanie ze współpracownikiem: kliknij `SHOW QR CODE`, aby wyświetlić swój kod QR współpracownikowi, który go zeskanuje. On następnie kliknie `SHOW QR CODE`, aby wyświetlić swój kod, a ty zeskanujesz go za pomocą `LAUNCH QR Scanner`. Powtarzaj ten proces, aż wszystkie pięć kroków wymiany zostanie ukończonych.



![Image](assets/fr/22.webp)



Po zakończeniu wszystkich wymian sprawdź szczegóły transakcji, a następnie zwolnij ją, przeciągając zieloną strzałkę u dołu ekranu.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Jego struktura jest następująca:



![Image](assets/fr/24.webp)



*Kredyt: [mempool.space](https://mempool.space/)*



Możemy zaobserwować dwa wejścia z mojego portfela, odpowiednio `91,869 sats` i `64,823 sats`, podczas gdy pozostałe dwa wejścia pochodzą z wallet mojego współpracownika. Po stronie wyjściowej jeden UTXO o wartości `100 000 sats` jest wysyłany do rzeczywistego odbiorcy, a dwa UTXO o wartości `100 000 sats` i `159 578 sats` wracają do portfela mojego współpracownika. Dla niego operacja jest neutralna, ponieważ odzyskuje pełną kwotę środków, które zainwestował we wkład (z wyłączeniem kosztów mining, do których się przyczynił). Ostatecznie otrzymuję UTXO w wysokości 56 270 sats`, odpowiadający różnicy między moim całkowitym wkładem a płatnością w wysokości 100 000 sats` wysłaną do odbiorcy.



Oczywiście mogę opisać tę strukturę, ponieważ sam zbudowałem transakcję. Ale dla obserwatora z zewnątrz, generalnie niemożliwe jest określenie, które UTXO należą do którego uczestnika, zarówno w wejściach, jak i wyjściach.



Aby pogłębić swoją wiedzę na temat zarządzania prywatnością onchain na Bitcoin, polecam wziąć udział w moim szkoleniu BTC 204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c