---
name: JoinMarket

description: Przewodnik i samouczek dotyczący korzystania z JoinMarket do wykonywania CoinJoin przez Bitcoin za pomocą wiersza poleceń
---

![cover](assets/cover.webp)



---

Jeśli znalazłeś tę stronę, wyszukując w Internecie hasło "JoinTmarket", to masz moje szczere uznanie. Natknąłeś się jednak na przewodnik, który dotyczy zupełnie innego, ale niezwykle interesującego tematu! 🚬🍁



Celem tego samouczka jest zilustrowanie teoretycznego i praktycznego działania JoinMarket za pomocą wiersza poleceń. 🐢 💚



## JoinMarket Definicja teoretyczna



Możemy zdefiniować JoinMarket jako narzędzie lub Wallet, które umożliwia CoinJoin z innymi użytkownikami w sposób całkowicie Trustless i bez żadnego centralnego koordynatora.



Ponieważ cała część teoretyczna tego narzędzia jest niezwykle obszerna, zdecydowałem się na Address w konkretnym odcinku mojego podcastu. Dla tych, którzy rozumieją język włoski, gorąco polecam kontynuowanie czytania po wysłuchaniu odcinka, aby lepiej przyswoić podstawowe pojęcia dotyczące prawidłowego korzystania z tego programu.



Odcinek można obejrzeć pod poniższymi linkami:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [podcast Google](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (tutaj można odsłuchać bezpośrednio z przeglądarki).
- [Antenna pod](https://antennapod.org/) to darmowy i opensource'owy menedżer podcastów, który nie wymaga rejestracji. Aby znaleźć odcinek, pobierz aplikację, ręcznie dodaj mój podcast, wklejając [ten link](https://Anchor.fm/s/bd5d5b20/podcast/rss) w sekcji _feed rss_, a następnie wyszukaj odcinek poświęcony JoinMarket.



## Instalacja



Systemy operacyjne:





- Raspiblitz
- Parasol
- MyNode
- Raspibolt



## Pliki konfiguracyjne



JoinMarket jest konfigurowalnym oprogramowaniem z nieskończoną liczbą ustawień; ustawienia te są określone w pliku konfiguracyjnym znajdującym się w głównym katalogu programu o nazwie `Joinmarket.cfg`.



W tej sekcji omówimy niektóre pola, które mogą okazać się interesujące do zbadania i / lub modyfikacji, w zależności od potrzeb. Chciałbym podkreślić, że wszystkie wymienione poniżej zmiany są przydatne, aby dostosować działanie oprogramowania do własnych potrzeb, ale nie są obowiązkowe.



Najpierw przejdźmy do folderu `joinmarket/scripts` i uruchommy polecenie:



```bash
python wallet-tool.py generate
```


W tym momencie powinien pojawić się błąd, ale spowoduje to, że oprogramowanie utworzy dla nas wstępnie ustawiony plik ustawień generate. Możemy przejść i edytować plik ustawień z terminala za pomocą:



```bash
nano joinmarket.cfg
```



lub:



```bash
vim joinmarket.cfg
```



po otwarciu zauważymy wiele wierszy z różnymi ustawieniami i ich wyjaśnieniem w języku angielskim. Poniżej przeanalizujemy najbardziej interesujące zmienne:





- `merge_algorithm` w przypadku, gdy robimy to jako twórca, to pole dostosowuje, jak agresywnie oprogramowanie będzie konsolidować niewydane wyjścia. Jeśli mamy wiele UTXO do skonsolidowania, sensowne może być przełączenie z _gradual_ na _greedy_
- `tx_fees` dostosowuje jako taker opłaty, którymi należy opłacić transakcję, bardzo przydatna jest zmiana tego ustawienia w przypadku częstego korzystania z tumblra (porozmawiamy o tym później), ponieważ jeśli wystąpi skok opłat podczas wykonywania tego ostatniego, jeśli nie ustawimy tego pola poprawnie, ryzykujemy, że wydamy dużo Sats na CoinJoin. Ustawiając wartości w tysiącach (np. 2000), będzie to oznaczać 2 Sats/vBytes, 3500 - 3,5 Sats/vBytes itd. Zalecałbym liczbę od 1500 do 6000 w zależności od potrzeb.
- `max_cj_fee_abs` służy do określenia, ile jesteśmy skłonni zapłacić w wartościach bezwzględnych za twórców, których wybierzemy podczas CoinJoin. Domyślnie to pole dla twórców wynosi 200 Sats, dobrą opcją może być liczba od 200 do 1000 Sats za odpowiednika (zależy to od tego, ile chcesz wydać i ile anon-set szukasz dla swoich CoinJoins)
- `max_cj_fee_rel` ma taką samą funkcję jak pole powyżej, ale określa względne opłaty (procentowe), które jesteśmy skłonni zapłacić każdemu kontrahentowi. Ponieważ jest to wartość "procentowa", należy uważać, aby nie ustawić wysokich wartości, aby uniknąć wysokich kosztów w CoinJoins z dużymi kwotami. Domyślną wartością dla makerów jest _0.00002_, zalecam podobną lub nieco wyższą wartość.
- `minimum_makers` to pole, które określa, z iloma innymi kontrahentami wykonujemy CoinJoin, domyślnie joinMarket zawsze wybiera od 4 do 9 kontrahentów, jeśli chcemy, dla większej prywatności, możemy zwiększyć tę wartość do 5 lub 6 (spowoduje to jednak, że transakcje będą droższe).
- `cjfee_a` określa, w przypadku gdy działamy jako twórca, ile Sats w wartościach bezwzględnych chcemy pobrać za wynajem naszej płynności. To pole jest całkowicie subiektywne, domyślna wartość jest już bardzo dobra (dzięki temu będziemy mieć lepszą prywatność jako twórca), możemy rozważyć ustawienie jej na 0, jeśli chcemy zarobić więcej CoinJoin w krótszym czasie.
- `cjfee_r` to samo pole co powyżej, ale w ujęciu procentowym, a nie bezwzględnym. Ponownie zalecam pozostawienie wartości domyślnej lub obniżenie jej, aby przyciągnąć więcej chętnych.
- `ordertype` za pomocą tego pola wybieramy od producenta, czy pobierać opłatę bezwzględną (absoffer) czy procentową (reloffer). Zazwyczaj biorcy preferują oferty bezwzględne w kwestiach ekonomicznych.
- `minsize` jeśli jako twórca nie chcemy, aby UTXO był zbyt mały, możemy określić minimalny CoinJoin, aby wziąć udział. To pole jest wyrażone w Satoshi i jest całkowicie subiektywne. Możemy pozostawić to pole na 0 lub zwiększyć do 500000 (Sats), 1000000 (Sats) i tak dalej.



Należy bardzo uważać, aby nie edytować niewłaściwych pól, niektóre zmienne w pliku joinmarket.cfg, jeśli są ustawione nieprawidłowo, mogą zagrozić funkcjonalności oprogramowania lub całkowicie unicestwić prywatność, oczy otwarte i ostrożność na maksa!



## Konfiguracja środowiska pracy



Niektóre węzły automatycznie ustawiają prawidłowe wartości dla tych pól w pliku joinmarket.cfg, ale zalecamy ponowne sprawdzenie ich ręcznie:





- `rpc_user = yourusername-as-in-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #domyślnie zwykle poprawne`
- `rpc_port = 8332 # domyślnie dla Mainnet`



W tym momencie możemy przystąpić do tworzenia naszego Wallet w JoinMarket:



```bash
python wallet-tool.py generate
```



To polecenie poprosi nas o wprowadzenie hasła, za pomocą którego zaszyfrujemy Wallet i nazwę, którą chcemy mu nadać, gdy zapyta, czy chcesz obsługiwać obligacje wierności, zalecam użycie opcji _yes_, zwrócone dane wyjściowe będą wyglądać następująco:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


w przypadku pojawienia się błędu najprawdopodobniej nieprawidłowo ustawiliśmy 4 pola RPC określone powyżej. W takim przypadku pomocne może być skorzystanie z [tego przewodnika] (https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) znajdującego się w oryginalnej dokumentacji JoinMarket.



Ukończyliśmy konfigurację naszego środowiska pracy i możemy rozpocząć eksplorację poleceń, które będą dla nas najbardziej przydatne. Wszystkie skrypty, które omówimy, można uruchomić w konsoli, a następnie `--help`, aby uzyskać szczegółowe wyjaśnienie.



Możemy teraz spróbować uruchomić:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



to polecenie wyświetli wszystkie różne głębokości mieszania Wallet z różnymi adresami sklasyfikowanymi jako:




- Nowy (Address nigdy nie używany)
- Change-out (pozostała część poprzedniej transakcji)
- Cj-out (wyjście CoinJoin)



oto praktyczny przykład rezultatu:



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


Teraz możemy przystąpić do zdeponowania naszych pierwszych Satoshis pod jednym lub kilkoma adresami, pamiętając, że niezależnie od twórcy lub biorcy, oprogramowanie nigdy nie przejdzie i nie skonsoliduje UTXO bezpośrednio na różne głębokości mieszania, w ten sposób możemy zachować Satoshis o różnych poziomach prywatności oddzielnie w Wallet.



## Wysyłanie Bitcoin z CoinJoin Single



Możemy teraz przenieść nasze Satoshis. Jednym z głównych poleceń w tym oprogramowaniu jest skrypt:



```bash
pyhton sendpayment.py
```


która pozwoli nam wysyłać transakcje na inne adresy z lub bez CoinJoin. Prześledźmy jak to działa i kilka praktycznych przykładów. Domyślne formatowanie komendy jest następujące (należy pamiętać o zamianie tekstu otoczonego symbolami < i >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



podstawowym przykładem użycia może być:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


w tym przypadku wyślemy do Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc tj. 5000000 Satoshi z naszej mixdepth 0 (domyślnej) wybierając od 4 do 9 odpowiedników dla CoinJoin (opcja domyślna).



Aby mieć większą kontrolę nad tym, jak i które UTXO wydać, możemy przejść do dodatkowych opcji tego polecenia:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


w tym przykładzie dodaliśmy dwie specyfikacje: -N wskazuje, z iloma kontrahentami będziemy miksować, -m głębokość miksu, z którego będziemy wypłacać środki. W rzeczywistości wysłaliśmy 100 000 000 Sats (1 btc) do Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c ze środkami w mixdepth 1 i mieszając z 5 kontrahentami.



Jeśli ustawimy 0 jako wartość wysyłania, określając mixdepth, joinMarket wykona tak zwany `sweep`, czyli wyśle wszystkie fundusze w tej mixdepth, konsolidując je ze sobą:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



tutaj wysłaliśmy wszystkie środki z mixdepth 0 (mogliśmy tego nie określać, ponieważ jest to ustawienie domyślne) mieszając z 7 odpowiednikami.



Polecenie sendpayment służy do przenoszenia środków z joinMarket do zewnętrznego Wallet lub do wysyłania Satoshi do osoby, dodając Layer prywatności między nami a nią. Aby uzyskać wystarczający poziom prywatności na naszych UTXO, bardziej odpowiednie jest użycie polecenia tumbler.py, które wyjaśnimy w dalszej części tego przewodnika.



## Bycie twórcą



Skrypt, który omówimy w tej sekcji to:



```bash
yg-privacyenhanced.py
```



Program ten służy do działania jako maker na rynku joinMarket. Oprogramowanie połączy się z naszym węzłem Bitcoin i z wewnętrznym rynkiem platformy, na którym makerzy prezentują się jako oferenci płynności, a takerzy szukają kontrahentów. Jeśli chcesz użyć obligacji fidelity bond, możesz ją utworzyć za pomocą tego formatowania:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



na przykład:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



wyjściem, które zostanie nam zwrócone, będzie Bitcoin Address (tj. ten, na którym będziesz musiał zdeponować środki, które chcesz przydzielić do fidelity).



**Uwaga**: Istnieją dwie rzeczy, na które należy zwrócić szczególną uwagę, jeśli zamierzasz utworzyć Fidelity Bond (znany również jako FB);





- po zdeponowaniu środków nie można ich ponownie przenieść do momentu wygaśnięcia. Zwróć uwagę na to, ile sat wysyłasz do Address i jak formatujesz datę. Błędy są niedozwolone!
- Fidelity bond jest łatwo rozpoznawalny w łańcuchu, dlatego zaleca się zdeponowanie środków za pośrednictwem CoinJoin i przy użyciu źródła niezwiązanego z tożsamością użytkownika. To samo zaleca się zrobić, gdy chcesz przenieść wygasłą obligację lojalnościową z JoinMarket.



Ważne jest, aby pamiętać, że możliwe jest doładowanie obligacji lojalnościowej tylko jedną transakcją, w przypadku wielokrotności UTXO tylko największa z nich zostanie uznana za ważną dla FB.



Zajmijmy się teraz skryptem wspomnianym na początku tego akapitu, po utworzeniu fidelity bond (który, jak pamiętamy, jest opcjonalny) jesteśmy gotowi do uruchomienia pliku wykonywalnego, aby działać jako twórca na joinMarket. Po zdeponowaniu Satss na różnych adresach i mixdepth możemy uruchomić polecenie:



```bash
python yg-privacyenhanced.py <wallet name>
```



Od tego momentu (po kilku minutach łączenia się z siecią) i do momentu zatrzymania skryptu, nasz klient JoinMarket pojawi się na liście aktywnych makerów w protokole i zaoferuje naszą płynność różnym kontrahentom w celu wykonania CoinJoin. Nie spodziewaj się dziesiątek CoinJoins dziennie (chyba że masz ogromną fidlity i dużą płynność zdeponowaną na Wallet), pamiętaj również, że czynniki takie jak wymagane opłaty i zdeponowane Satoshis wpływają na to, jak często będziesz makerem.



Uruchamiając poniższe polecenie, będziesz mógł zobaczyć historię wszystkich transakcji dokonanych na Wallet oraz wszelkie zyski (jeśli jesteś makerem) lub koszty opłat (jeśli jesteś biorcą), które miałeś przez cały okres użytkowania Wallet.



```bash
python wallet-tool.py <wallet name> history
```



Gdy Satoshis wykonają CoinJoins, będą przenosić się z mixdepth do mixdepth, aż dotrą do ostatniego. Po przekroczeniu czwartej głębokości powrócą do głębokości mieszania 0, od ciebie zależy, ile prywatności zdobędziesz przed przeniesieniem ich do Cold Wallet, zaleca się ukończenie pełnego cyklu Wallet.



## Tumbler



Oto w końcu jesteśmy w najbardziej soczystej części JoinMarket, tumblrze! Jeśli słuchałeś podcastu, wiesz już, o co w tym wszystkim chodzi. Jedno zalecenie, zanim zaczniemy: **Uważaj na opłaty! Pamiętaj, aby ustawić limity w pliku joinmarket.cfg (jak wyjaśniono na początku) i rozważ uruchomienie programu tylko wtedy, gdy opłaty onchain są stosunkowo niskie (poniżej 10 Sats/vB).



Aby uruchomić tumbler, konieczne jest zatrzymanie skryptu od makera (jeśli był aktywny), po czym możemy uruchomić polecenie:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Konieczne jest wprowadzenie **co najmniej** 3 adresów wyjściowych dla tumblera: ma to zapewnić dobrą prywatność i nie tworzyć oczywistych powiązań między UTXO w całym procesie. Jak zwykle, dodając `--help` do polecenia można przejść i zobaczyć wszystkie dodatkowe szczegóły. Przejdźmy do bardziej złożonego przykładu z zaawansowanymi regułami:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



W tym przypadku uruchomiliśmy skrypt tumblingu, który nie będzie używał domyślnej liczby odpowiedników (parametr -N wskazuje, że wymagamy 7 odpowiedników z maksymalną wariancją 2, więc losowa liczba twórców od 5 do 9) i z większą liczbą CoinJoin na mixdepth (domyślnie ten skrypt tworzy losową liczbę CoinJoin na sekcję Wallet w zakresie od 1 do 3, używając polecenia -c 3 1 zamiast tego będzie od 2 do 4). W ten sposób wydamy więcej Sats na opłaty, ale będziemy mieć większy zestaw anonimowości.



Można również dodać dowolną liczbę adresów wyjściowych (minimum 3, nie ma maksimum poza zdrowym rozsądkiem). Jednak ze względu na kwestie prywatności nie można zdecydować, w jaki sposób Satoshi zostanie rozdzielony między adresy określone jako wyjściowe.



Tumbler jest celowo długim procesem, czasami może się zdarzyć, że coś przestanie działać, w większości przypadków rozwiąże się to w ciągu kilku godzin. W przypadku całkowitej awarii możemy spróbować uruchomić go ponownie za pomocą polecenia:



```bash
python tumbler.py --restart
```



Można też po prostu ponownie uruchomić nowe polecenie mieszania. Nie uruchomi to harmonogramu poprzedniego tumblera, ale rozpocznie nowy cykl mieszania. W przypadku, gdy zamknięcie terminala SSH do węzła również zatrzymuje skrypt, można skorzystać z programu `TMUX`, który można zainstalować za pomocą polecenia:



```bash
sudo apt install tmux
```



Uruchomienie go z powłoki poprzez wpisanie `tmux` otworzy terminal, który pozostanie aktywny w tle nawet po zamknięciu zdalnego połączenia. Po ponownym połączeniu się z węzłem za pomocą polecenia: `tmux attach` ponownie otworzysz powłokę, która pozostała aktywna w tle.



## Wnioski



JoinMarket to nieograniczone i konfigurowalne oprogramowanie. W tym przewodniku odkryliśmy główne funkcje, dzięki czemu każdy (a przynajmniej ja próbowałem, zdaję sobie sprawę, że korzystanie z tego oprogramowania nie jest spacerkiem po parku) może z niego korzystać. Jednym z największych problemów z JoinMarket jest właśnie to: liczba osób korzystających z niego i bycie twórcą. Jeśli niewielu użytkowników korzysta z tego oprogramowania, ogólna prywatność (anon-set) jest obniżona. Dlatego mam nadzieję, że ten przewodnik zachęci do korzystania i przekona cię do pobrania i zainstalowania mojego ulubionego oprogramowania do tworzenia CoinJoin. Jeśli chcesz jeszcze bardziej zagłębić się w niektóre aspekty, polecam przeczytać różne szczegółowe dokumenty na githubie, są one bardzo dobrze zrobione i można je znaleźć tutaj.



Szczęśliwe mieszanie żółwi! 🐢 💚



[Tutaj](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) możesz wesprzeć Turtlecute