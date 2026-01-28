---
name: Zeus Embedded
description: Jak korzystać z Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS to początkowo aplikacja mobilna do zdalnego zarządzania węzłami piorunochronów, umożliwiająca sterowanie węzłem zainstalowanym na zdalnym serwerze


Ale aplikacja zawiera również "wbudowany węzeł".



**To właśnie ten aspekt aplikacji będziemy badać w tym samouczku.** Pozwala to każdemu na posiadanie własnego węzła Lightning na urządzeniach mobilnych, bez potrzeby posiadania dedykowanego serwera, w taki sam sposób, w jaki ACINQ oferuje swój niesamowity Wallet Lightning Phoenix.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Dla przypomnienia, Lightning to sieć, która działa równolegle z Bitcoin, umożliwiając wymianę bitcoinów bez konieczności systematycznego przeprowadzania transakcji On-Chain. Rezultatem są niemal natychmiastowe transakcje, bez konieczności czekania 10 minut na zatwierdzenie bloku. Jest to szczególnie przydatne podczas płacenia sprzedawcy w świecie fizycznym. Co więcej, Lightning zapewnia niezwykły poziom **poufności**, którego sieć Bitcoin nie posiada natywnie*.



**Zeus "Integrated "** jest skierowany do użytkowników Bitcoin, którzy chcą zmaksymalizować swoją prywatność i autonomię.


Krótko mówiąc, jest to **potencjalnie** Wallet mobile marzeń cypherpunków. Nawet jeśli jest jeszcze w powijakach (wersja alfa) i ma kilka błędów, jego funkcje są legendarne i nie ma wątpliwości, że zachwyci najbardziej nieustraszonych z nas, którzy chcą maksymalnej kontroli i opcjonalności.



Z drugiej strony, nie sądzę, by był on obecnie odpowiedni dla początkujących, którzy nie są zaznajomieni z Bitcoin i chcą po prostu prostego sposobu wysyłania/odbierania satoshis. Chociaż może się to zmienić w przyszłości, ponieważ funkcja opieki za pośrednictwem protokołu Cashu (chaumian Ecash) jest wdrażana dla początkujących...



## Zainstaluj aplikację



Przejdź do [strony internetowej projektu](https://zeusln.com/), aby pobrać aplikację dla systemu operacyjnego smartfona:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Tworzenie portfolio



Po uruchomieniu aplikacji kliknij przycisk "Szybki start", aby rozpocząć tworzenie Wallet.



![image](assets/fr/03.webp)





Następnie pojawi się seria ekranów inicjalizacyjnych. Poczekaj kilka chwil, a następnie kilka minut, aż węzeł zostanie w 100% zsynchronizowany przez Neutrino.



Może to potrwać kilka minut. Dla informacji, neutrino jest sposobem dla mobilnych portfeli na dostęp do informacji Blockchain Bitcoin, bez konieczności uruchamiania Full node.



![image](assets/fr/04.webp)





Po kilku chwilach jesteś gotowy do pracy.



![image](assets/fr/05.webp)




## Konfiguracja aplikacji



Gotowe, ale nie do końca, ponieważ nie trzeba dodawać, że użytkownik Zeusa zasługujący na to miano porusza się po Wallet z klasą i stylem. Będziemy więc musieli zmienić jego awatar.



Kliknij swój awatar w prawym górnym rogu ekranu:



![image](assets/fr/06.webp)





Kliknij na koło zębate, a następnie na plus "+" :



![image](assets/fr/07.webp)





Wybierz najpiękniejsze zdjęcie Zeusa reprezentujące Wallet i kliknij "WYBIERZ ZDJĘCIE" na dole ekranu, a następnie wróć, klikając strzałkę w prawym górnym rogu.



![image](assets/fr/08.webp)





Na koniec nadaj swojemu Wallet pseudonim i kliknij "ZAPISZ KONFIGURACJĘ Wallet", aby zmiana zaczęła obowiązywać. Na koniec kliknij strzałkę wstecz w lewym górnym rogu, aby powrócić do ekranu głównego.



![image](assets/fr/09.webp)





Tym razem możemy naprawdę zacząć.



![image](assets/fr/10.webp)



### Biometria



Aby zabezpieczyć dostęp do Wallet, można dodać kod PIN/hasło i aktywować dane biometryczne.



Aby to zrobić, przejdź do menu głównego Wallet, klikając poziome kreski w lewym górnym rogu.



![image](assets/fr/11.webp)





Wybierz "Ustawienia", następnie "Zabezpieczenia", a na końcu "Ustaw/Zmień PIN".



![image](assets/fr/12.webp)





Utwórz kod PIN, potwierdź go i aktywuj dane biometryczne, naciskając odpowiedni przycisk "Biometrics".  Wróć do menu głównego, używając strzałki w lewym górnym rogu.



![image](assets/fr/13.webp)




### Zapisz frazę Mnemonic



Po powrocie do menu głównego kliknij "Utwórz kopię zapasową Wallet", a następnie przeczytaj tekst ostrzegawczy, który informuje, że utrata 24 słów, które wkrótce otrzymasz, jest równoznaczna z utratą dostępu do twoich funduszy i że każdy, kto ma te słowa oprócz ciebie, może uzyskać dostęp do twoich funduszy. Nigdy nikomu ich nie dawaj.



Wybierz "ZROZUMIAŁEM" u dołu ekranu. Następnie kliknij każde z 24 słów, aby je wyświetlić, i zanotuj je uważnie.



Można go zapisać na papierze lub, w celu zwiększenia bezpieczeństwa, wygrawerować na stali nierdzewnej, aby zabezpieczyć go przed pożarem, powodzią lub zawaleniem. Wybór nośnika dla Mnemonic będzie zależał od strategii bezpieczeństwa, ale jeśli używasz Zeusa jako portfela wydatków zawierającego umiarkowane kwoty, papier powinien być wystarczający.



Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Po zakończeniu klikamy "I'VE BACKUP MY 24 WORDS" u dołu ekranu i wracamy do ekranu głównego, gotowi do otrzymania naszych pierwszych bitcoinów.




## Opcja 1 - Odbiór bitcoinów On-Chain i otwarcie kanału Lightning



**Zeus Embedded** został zaprojektowany przede wszystkim jako wbudowany węzeł oświetleniowy, ale może być również używany jako Wallet On-Chain.



Aby otrzymać bitcoiny On-Chain, kliknij przycisk "On-Chain", a następnie "Odbierz".


Na koniec zeskanuj kod QR lub skopiuj Bitcoin Address, aby wpłacić środki.



![image](assets/fr/15.webp)





Gdy środki zostaną potwierdzone i zaksięgowane na Wallet, można ich użyć do otwarcia **kanału Lightning**. Kanał Lightning to brama do Lightning Network, umożliwiająca znacznie bardziej poufny i szybszy obrót bitcoinami Exchange.





- Aby to zrobić, kliknij "PRZENIEŚ FUNDUSZE On-Chain DO LIGHTNING"



Na następnym ekranie zostaniesz poproszony o otwarcie kanału we współpracy z **"Olympus by Zeus "**, LSP (Lightning Service Provider) preferowanym przez Wallet.


W tym samouczku wybierzemy tę opcję dla uproszczenia, ale całkowicie możliwe jest otwieranie kanałów z dowolnym węzłem w sieci.


Możliwe jest nawet otwarcie kilku kanałów w jednej transakcji poprzez wybranie opcji "OPEN ADDITIONAL CHANNEL". *Ale zajmiemy się tym w "zaawansowanej" wersji samouczka* **Zeus Embedded**.





- Następnie wybierz kwotę, którą chcesz przeznaczyć na ten kanał. W naszym przypadku wykorzystane zostaną wszystkie środki On-Chain, więc aktywujemy przycisk "Wykorzystaj wszystkie możliwe środki".





- Na koniec wybierz przycisk "OTWÓRZ KANAŁ" w dolnej części ekranu.



![image](assets/fr/16.webp)





W ciągu kilku sekund kanał został ustanowiony i jesteśmy gotowi do wykonania naszych pierwszych transakcji Lightning. Na ekranie głównym widzimy mały zegar obok naszego salda Wallet. Wynika to z faktu, że musimy jeszcze poczekać na 3 potwierdzenia On-Chain, zanim kanał będzie naprawdę funkcjonalny.



![image](assets/fr/17.webp)





Po 3 potwierdzeniach zauważamy, że nasze saldo jest teraz zapisywane we wkładce Lightning.



![image](assets/fr/18.webp)



Mały szczegół: kiedy klikniemy menu na dole ekranu, aby wyświetlić stan naszych kanałów Lightning, zobaczymy, że niewielka część naszego salda nie jest dostępna do wydania: możemy wydać tylko 208253 satoshi zamiast 210370, które faktycznie posiadamy. Jest to normalne, ponieważ jest to specyficzne dla protokołu Lightning.



Na koniec należy zauważyć, że nasz partner Olympus zastrzega sobie prawo do zamknięcia kanału według własnego uznania, jeśli na przykład nie jest on używany. Aby upewnić się, że nasz kanał jest utrzymywany, będziemy musieli zapłacić LSP (Lightning Service Provider), jak zobaczymy w następnym akapicie, poprzez drugi sposób otwarcia kanału.





## Wysyłanie bitcoinów przez Lightning



Teraz, gdy już uruchomiliśmy nasz kanał, zobaczmy, jak możemy go wykorzystać do opłacenia błyskawicy Invoice (Invoice).



Aby to zrobić, kliknij przycisk "Lightning", a następnie "Wyślij".



![image](assets/fr/19.webp)





Na następnym ekranie skopiuj swój Invoice do dedykowanego pola lub zeskanuj go, klikając ikonę w prawym górnym rogu. Na koniec przesuń przycisk "Przesuń, aby zapłacić" w prawo, aby zapłacić.



![image](assets/fr/20.webp)






Poczekaj kilka sekund, a Invoice zostanie spłacony, a twoje satoshis podróżują z prędkością światła.



![image](assets/fr/21.webp)





Zeus umożliwia następnie dodanie notatki w celu denominacji płatności lub wyświetlenie trasy, jaką przebyły satoshi przed dotarciem do miejsca docelowego (oraz opłat pobranych przez wszystkie węzły pośrednie). Jest to rodzaj funkcjonalności, którą uwielbiamy w Wallet.



![image](assets/fr/22.webp)



Należy pamiętać, że w przeciwieństwie do Wallet, takiego jak [Phoenix]([Plan ₿ Academy - Phoenix](https://planb.academy/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), w przypadku Zeusa trasa jest obliczana lokalnie i nie jest delegowana do strony trzeciej (ACINQ w przypadku Phoenix). Jesteś więc jedyną osobą, która zna odbiorcę płatności. Tracimy nieco na wydajności (płatności trwają nieco dłużej, ale zyskujemy wiele pod względem prywatności).





Klikając na małą strzałkę na dole ekranu głównego, można również wyświetlić naszą historię płatności. Tutaj widzimy w Green 212,121 Sats otrzymane za On-Chain, następnie odpowiednio na czerwono 211,756 Sats wykorzystane do otwarcia naszego kanału, a następnie 121,212 satoshis wykorzystane do zapłaty za nasze oświetlenie Invoice.



![image](assets/fr/23.webp)





## Opcja 2 - Odbieranie bitcoinów bezpośrednio przez Lightning



Zamiast otwierać kanał ręcznie, jak właśnie widzieliśmy, możliwe jest otrzymywanie środków bezpośrednio przez Lightning, nawet bez wcześniej istniejącego kanału, za pomocą Olympus, Zeus LSP.




- Aby to zrobić, kliknij przycisk "Lightning" na ekranie głównym, a następnie "Odbierz".
- Następnie wybierz kwotę, którą chcesz otrzymać w polu "Kwota" i wybierz przycisk "UTWÓRZ Invoice" u dołu ekranu.



![image](assets/fr/24.webp)





Następny ekran pokazuje Invoice, które należy zapłacić, aby otrzymać satoshis. Powiedziano nam, że LSP wstrzyma 10 000 Sats, jeśli płatność zostanie dokonana przez Lightning. Zobaczymy później, jak te opłaty za otwarcie kanału są uzasadnione.



Zapłać Invoice lub zleć to komuś innemu, a kanał zostanie otwarty automatycznie, ale z potrąceniem 10 000 Sats zgodnie z umową.



![image](assets/fr/25.webp)





Znajdujemy się teraz na czele 2 kanałów Lightning, których status można sprawdzić, klikając przycisk wskazany białą strzałką u dołu ekranu głównego.



Widzimy, że w przeciwieństwie do kanału otwartego z naszej wagi On-Chain, ten otwarty bezpośrednio przez błyskawicę nie wyświetla żadnego ostrzeżenia.


Ponieważ zapłaciłeś za skonfigurowanie tego kanału, dostawca usług Lightning (LSP) zobowiązuje się do utrzymania kanału przez 3 miesiące i oferuje "płynność przychodzącą". Na dolnym kanale widać, że pojemność odbiorcza wynosi 96383 satoshi. W związku z tym LSP związał kapitał, aby umożliwić otrzymywanie płatności bezpośrednio po otwarciu kanału.



Tak więc 10 000 Satoshi uiszczonych opłat pokrywa: koszt otwarcia kanału (transakcja Bitcoin On-Chain, gwarancja utrzymania kanału przez 3 miesiące i blokada kapitału).



![image](assets/fr/26.webp)





Gratulacje, jesteś teraz gotowy do korzystania z Zeus Embedded, mobilnego systemu oświetleniowego Wallet z najbardziej zaawansowanymi funkcjami na rynku.





Aby dowiedzieć się więcej o technicznym działaniu Lightning Network, można znaleźć doskonałe bezpłatne szkolenie Plan ₿ Academy Fanisa Michalakisa:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb