---
term: CoinJoin
---

CoinJoin to technika wykorzystywana do łamania identyfikowalności bitcoinów. Opiera się ona na wspólnej transakcji o określonej strukturze o tej samej nazwie: transakcji CoinJoin. Transakcje CoinJoin pomagają poprawić ochronę prywatności użytkowników Bitcoin, utrudniając zewnętrznym obserwatorom analizę transakcji. Struktura ta pozwala na mieszanie wielu monet w jednej transakcji, co utrudnia określenie powiązań między adresami wejściowymi i wyjściowymi.


Ogólne działanie CoinJoin jest następujące: różni użytkownicy, którzy chcą mieszać, wpłacają kwotę jako dane wejściowe transakcji. Te dane wejściowe pojawią się jako różne dane wyjściowe tej samej kwoty. Pod koniec transakcji niemożliwe jest określenie, które dane wyjściowe należą do którego użytkownika. Z technicznego punktu widzenia nie ma powiązania między danymi wejściowymi i wyjściowymi transakcji CoinJoin. Powiązanie między każdym użytkownikiem a każdym UTXO jest zerwane w taki sam sposób, jak historia każdej monety.


![](../../dictionnaire/assets/4.webp)


Aby umożliwić CoinJoin bez utraty przez użytkownika kontroli nad swoimi środkami w dowolnym momencie, transakcja jest najpierw konstruowana przez koordynatora, a następnie przesyłana do każdego użytkownika. Następnie każdy z nich podpisuje transakcję po swojej stronie po sprawdzeniu, czy mu odpowiada, a następnie wszystkie podpisy są dodawane do transakcji. Jeśli użytkownik lub koordynator spróbuje ukraść środki innych, modyfikując dane wyjściowe transakcji CoinJoin, podpisy będą nieważne, a transakcja zostanie odrzucona przez węzły. Gdy rejestrowanie danych wyjściowych uczestników odbywa się przy użyciu ślepych podpisów Chauma, aby uniknąć powiązania z danymi wejściowymi, jest to określane jako "Chaumian CoinJoin".


Mechanizm ten zwiększa poufność transakcji bez konieczności modyfikacji protokołu Bitcoin. Konkretne implementacje CoinJoin, takie jak Whirlpool, JoinMarket czy Wabisabi, oferują rozwiązania ułatwiające proces koordynacji między uczestnikami i zwiększające efektywność transakcji CoinJoin. Oto przykład transakcji CoinJoin:


```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```


Trudno jest ustalić z całą pewnością, kto pierwszy wprowadził ideę CoinJoin na Bitcoin i kto wpadł na pomysł wykorzystania ślepych podpisów Davida Chauma w tym kontekście. Często uważa się, że Gregory Maxwell jako pierwszy omówił tę kwestię w [wiadomości na BitcoinTalk w 2013 r.] (https://bitcointalk.org/index.php?topic=279249.0):

Korzystanie ze ślepych podpisów Chauma: Użytkownicy łączą się i dostarczają dane wejściowe (i zmieniają adresy), a także kryptograficznie blinded wersję Address, do której chcą wysłać swoje prywatne monety; serwer podpisuje tokeny i zwraca je. Użytkownicy ponownie łączą się anonimowo, demaskują swoje adresy wyjściowe i wysyłają je z powrotem do serwera. Serwer widzi, że wszystkie dane wyjściowe zostały przez niego podpisane, a zatem wszystkie dane wyjściowe pochodzą od prawidłowych uczestników. Później ludzie łączą się ponownie i podpisują.

Maxwell, G. (2013, 22 sierpnia). *CoinJoin: Bitcoin prywatność dla prawdziwego świata*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0


Istnieją jednak wcześniejsze wzmianki, zarówno o sygnaturach Chaum w kontekście mieszania, jak i coinjoinów. [W czerwcu 2011 r. Duncan Townsend zaprezentował na BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) mikser, który wykorzystuje podpisy Chaum w sposób dość podobny do współczesnych coinjoinów Chaumian. W tym samym wątku znajduje się [wiadomość od hashcoin w odpowiedzi na Duncana Townsenda](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) w celu ulepszenia jego miksera. Wiadomość ta przedstawia to, co najbardziej przypomina coinjoiny. Wzmianka o podobnym systemie znajduje się również w [wiadomości od Alexa Mizrahi z 2012 r.](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), gdy doradzał on twórcom Tenebrix. Sam termin "CoinJoin" nie został wymyślony przez Grega Maxwella, ale pochodzi od pomysłu Petera Todda.


> termin "CoinJoin" nie ma francuskiego tłumaczenia. Niektórzy użytkownicy bitcoinów używają również terminów "mix", "mixing" lub "mixage" w odniesieniu do transakcji CoinJoin. Mieszanie jest raczej procesem stosowanym w sercu CoinJoin. Ważne jest również, aby nie mylić mieszania poprzez coinjoiny z mieszaniem za pośrednictwem centralnego aktora, który przejmuje bitcoiny w trakcie procesu. Nie ma to nic wspólnego z CoinJoin, w którym użytkownik nie traci kontroli nad swoimi bitcoinami podczas tego procesu*