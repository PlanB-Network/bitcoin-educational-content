---
term: CHAUMIAN CoinJoin
---

Protokół CoinJoin, który wykorzystuje ślepe podpisy Davida Chauma i Tor do komunikacji między uczestnikami a serwerem koordynatora. Celem Chaumian CoinJoin jest zapewnienie uczestnikom, że koordynator nie może ukraść bitcoinów ani połączyć ze sobą wejść i wyjść.


Aby to osiągnąć, użytkownicy przesyłają swoje dane wejściowe i kryptograficznie blinded odbiór Address do koordynatora. Ten Address, po unblinded, ma na celu otrzymanie bitcoinów jako danych wyjściowych z CoinJoin. Koordynator podpisuje te tokeny i zwraca je użytkownikom. Następnie użytkownicy ponownie łączą się anonimowo z serwerem koordynatora z nową tożsamością Tor i ujawniają swoje adresy wyjściowe w postaci zwykłego tekstu w celu skonstruowania transakcji. Koordynator może zweryfikować, że wszystkie te adresy odbiorcze pochodzą od legalnych użytkowników, ponieważ wcześniej podpisał ich wersję blinded swoim kluczem prywatnym. Nie może on jednak powiązać konkretnego wyjściowego Address z danym użytkownikiem wejściowym. Dlatego też nie ma powiązania między danymi wejściowymi i wyjściowymi, nawet z perspektywy koordynatora. Gdy transakcja zostanie skonstruowana przez koordynatora, wysyła ją z powrotem do uczestników, którzy podpisują ją, aby odblokować swoje dane wejściowe, po sprawdzeniu, czy ich dane wyjściowe rzeczywiście znajdują się w tej transakcji. Uczestnicy wysyłają podpis do koordynatora. Po zebraniu wszystkich podpisów koordynator może rozgłosić transakcję CoinJoin w sieci Bitcoin.


![](../../dictionnaire/assets/38.webp)


Metoda ta zapewnia, że koordynator nie może naruszyć anonimowości uczestników ani ukraść bitcoinów podczas całego procesu CoinJoin.


Trudno jest z całą pewnością określić, kto pierwszy wprowadził ideę CoinJoin na Bitcoin i kto wpadł na pomysł wykorzystania ślepych podpisów Davida Chauma w tym kontekście. Często uważa się, że Gregory Maxwell jako pierwszy omówił tę kwestię w [wiadomości na BitcoinTalk w 2013 r.] (https://bitcointalk.org/index.php?topic=279249.0):


> *"Używając ślepych podpisów Chauma: Użytkownicy łączą się i dostarczają dane wejściowe (i zmieniają adresy), a także kryptograficznie blinded wersję Address, do której chcą wysłać swoje prywatne monety; serwer podpisuje tokeny i zwraca je. Użytkownicy ponownie łączą się anonimowo, demaskują swoje adresy wyjściowe i zwracają je serwerowi. Serwer widzi, że wszystkie dane wyjściowe zostały przez niego podpisane, a zatem wszystkie dane wyjściowe pochodzą od prawidłowych uczestników. Później ludzie łączą się ponownie i podpisują. "*

Maxwell, G. (2013, 22 sierpnia). *CoinJoin: Bitcoin prywatność dla prawdziwego świata*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

Istnieją jednak inne wcześniejsze wzmianki, zarówno o sygnaturach Chauma w kontekście miksowania, jak i coinjoinów. [W czerwcu 2011 r. Duncan Townsend zaprezentował na BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) mikser, który wykorzystuje podpisy Chauma w sposób dość podobny do współczesnych coinjoinów Chauma. W tym samym wątku znajduje się [wiadomość od hashcoin w odpowiedzi na Duncana Townsenda](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) w celu ulepszenia jego miksera. Ta wiadomość dokładnie przedstawia to, co najbardziej przypomina coinjoiny. Wzmianka o podobnym systemie znajduje się również w [wiadomości od Alexa Mizrahi z 2012 r.](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), gdy doradzał on twórcom Tenebrix. Sam termin "CoinJoin" nie został wymyślony przez Grega Maxwella, ale pochodzi od pomysłu Petera Todda.