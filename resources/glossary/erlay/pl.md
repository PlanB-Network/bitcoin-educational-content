---
term: ERLAY
---

Proponowany protokół sieciowy poprawiający wydajność przekazywania niepotwierdzonych transakcji między węzłami Bitcoin.


Obecnie każda transakcja jest propagowana za pośrednictwem systemu, w którym każdy węzeł rozgłasza transakcję, o której wie, do wszystkich swoich rówieśników. Problem polega na tym, że prowadzi to do dużej nadmiarowości i wykorzystania przepustowości dla duplikatów. Wiele transmisji transakcji jest niepotrzebnych, ponieważ odbiorca już wie o tych transakcjach, a każdy węzeł musi wiedzieć o każdej transakcji tylko raz. Erlay proponuje domyślnie ograniczyć do 8 liczbę węzłów równorzędnych, do których węzeł bezpośrednio wysyła transakcje, o których wie, a następnie wykorzystać proces uzgadniania oparty na bibliotece minisketch, aby efektywniej udostępniać brakujące transakcje.


Erlay zmniejszyłby zużycie przepustowości o około 40%, czyniąc działanie Full node bardziej dostępnym dla użytkowników z ograniczonymi połączeniami internetowymi, a tym samym promując lepszą decentralizację sieci. Protokół ten utrzymywałby również niemal stałe zużycie przepustowości wraz ze wzrostem liczby połączeń. Oznacza to, że operatorom węzłów byłoby znacznie łatwiej zaakceptować bardzo dużą liczbę połączeń od swoich rówieśników, co zwiększyłoby bezpieczeństwo sieci Bitcoin poprzez zmniejszenie ryzyka partycjonowania, celowego lub przypadkowego. Ponadto Erlay utrudniłby określenie węzła źródłowego transakcji, zwiększając w ten sposób poufność dla użytkowników węzłów nie działających w sieci Tor.


Erlay jest proponowany w BIP330.