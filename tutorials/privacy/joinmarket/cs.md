---
name: JoinMarket

description: Průvodce a návod, jak používat JoinMarket k provádění CoinJoin přes Bitcoin prostřednictvím příkazového řádku
---

![cover](assets/cover.webp)



---

Pokud jste tuto stránku našli při vyhledávání "JoinTmarket" na internetu, upřímně vám děkuji. Narazili jste však na průvodce, který se zabývá zcela jiným, ale nesmírně zajímavým tématem! 🚬🍁



Cílem tohoto výukového kurzu je ukázat teoretické a praktické ovládání programu JoinMarket prostřednictvím příkazového řádku. 🐢 💚



## Teoretická definice JoinMarket



JoinMarket můžeme definovat jako nástroj, neboli Wallet, který umožňuje CoinJoin s ostatními uživateli zcela v režimu Trustless a bez centrálního koordinátora.



Vzhledem k tomu, že celá teoretická část tohoto nástroje je nesmírně rozsáhlá, rozhodl jsem se, že ji v konkrétním díle svého podcastu Address. Těm, kteří rozumí italsky, vřele doporučuji po poslechu epizody pokračovat ve čtení, aby si lépe osvojili základní pojmy pro správné používání tohoto programu.



Na těchto přímých odkazech si můžete epizodu prohlédnout:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (zde si ji můžete poslechnout přímo z prohlížeče).
- [Antenna pod](https://antennapod.org/) je bezplatný správce podcastů s otevřeným zdrojovým kódem, který nevyžaduje registraci. Chcete-li najít epizodu, stáhněte si aplikaci, ručně přidejte můj podcast vložením [tento odkaz](https://Anchor.fm/s/bd5d5b20/podcast/rss) do sekce _feed rss_ a poté vyhledejte epizodu věnovanou JoinMarket.



## Instalace



Operační systémy:





- Raspiblitz
- Deštník
- MyNode
- Raspibolt



## Konfigurační soubory



JoinMarket je přizpůsobitelný software s nekonečným počtem nastavení; tato nastavení jsou uvedena v konfiguračním souboru umístěném v hlavním adresáři programu s názvem `Joinmarket.cfg`.



V této části se budeme zabývat některými poli, která můžete podle svých potřeb prozkoumat a/nebo upravit. Rád bych zdůraznil, že všechny níže uvedené změny je užitečné znát, abyste mohli přizpůsobit fungování softwaru osobním potřebám, a zároveň nejsou povinné.



Nejprve se přesuňme do složky `joinmarket/scripts` a spusťme příkaz:



```bash
python wallet-tool.py generate
```


V tuto chvíli by se měla zobrazit chyba, ale software generate pro nás vytvoří soubor s přednastavenými nastaveními. Soubor s nastavením můžeme z terminálu upravit pomocí:



```bash
nano joinmarket.cfg
```



nebo:



```bash
vim joinmarket.cfg
```



po otevření si všimneme mnoha řádků s různými nastaveními a jejich vysvětlením v angličtině. Konkrétně si níže rozebereme nejzajímavější proměnné:





- `merge_algorithm` v případě, že to děláme jako výrobce, toto pole nastavuje, jak agresivně bude software konsolidovat nevyužité výstupy. V případě, že máme mnoho UTXO ke konsolidaci, může mít smysl přepnout z _gradual_ na _greedy_
- `tx_fees` nastavuje jako taker poplatky, kterými se transakce platí, je velmi užitečné změnit toto nastavení v případě, že používáte tumbler často (o tom budeme mluvit později), protože pokud dojde ke skokovému zvýšení poplatků během provádění posledního, pokud toto pole nenastavíme správně, riskujeme, že utratíme hodně Sats za CoinJoin. Nastavením hodnot v tisících (například 2000) to bude odpovídat 2 Sats/vBajtech, 3500 3,5 Sats/vBajtech atd. V závislosti na vašich potřebách bych doporučil číslo v rozmezí 1500 až 6000.
- `max_cj_fee_abs` slouží k určení toho, kolik jsme ochotni zaplatit v absolutních hodnotách za výrobce, které jsme si vybrali během CoinJoin. Ve výchozím nastavení je toto pole pro tvůrce 200 Sats, dobrou volbou by mohlo být číslo v rozmezí 200 až 1000 Sats za protistranu (záleží na tom, kolik chcete utratit a kolik anoncí hledáte pro své CoinJoiny)
- `max_cj_fee_rel` má stejnou funkci jako pole výše, ale určuje relativní poplatky (v procentech), které jsme ochotni zaplatit každé protistraně. Protože se jedná o `procentní` hodnotu, dávejte pozor, abyste nenastavovali vysoké hodnoty, abyste se vyhnuli vysokým nákladům v CoinJoinech s velkými částkami. Výchozí hodnota pro tvůrce je _0,00002_, doporučuji podobnou nebo mírně vyšší hodnotu.
- `minimum_makers` je pole, které určuje, s kolika dalšími protistranami provádíme CoinJoin, ve výchozím nastavení joinMarket vždy vybírá 4 až 9 protistran, pokud chceme pro větší soukromí, můžeme tuto hodnotu zvýšit na 5 nebo 6 (transakce se tím však prodraží).
- `cjfee_a` určuje, kolik Sats v absolutním vyjádření chceme inkasovat za pronájem naší likvidity v případě, že vystupujeme jako maker. Toto pole je zcela subjektivní, výchozí hodnota je již velmi dobrá (budeme mít tedy lepší soukromí jako tvůrce), můžeme zvážit její snížení na 0, pokud chceme vydělat více CoinJoin za kratší dobu.
- `cjfee_r` stejné jako výše uvedené pole, ale v procentech, nikoli absolutně. Opět doporučuji ponechat výchozí hodnotu nebo ji snížit, abyste přilákali více zájemců.
- `ordertype` pomocí tohoto pole vybíráme od výrobce, zda chceme účtovat absolutně (absoffer) nebo procentuálně (reloffer). U ekonomických otázek dávají přijímající obvykle přednost absolutním nabídkám.
- `minsize` pokud jako tvůrce nechceme mít UTXO příliš malý, můžeme zadat minimální hodnotu CoinJoin pro účast. Toto pole je vyjádřeno v Satoshi a je zcela subjektivní. Můžeme toto pole ponechat na hodnotě 0 nebo zvýšit na 500000 (Sats), 1000000 (Sats) atd.



Buďte velmi opatrní a neupravujte nesprávná pole, některé z proměnných v souboru joinmarket.cfg by při nesprávném nastavení mohly ohrozit funkčnost softwaru nebo zcela zničit vaše soukromí, mějte oči otevřené a buďte maximálně opatrní!



## Nastavení pracovního prostředí



Některé uzly automaticky nastavují správné hodnoty těchto polí v souboru joinmarket.cfg, doporučuji je překontrolovat ručně:





- `rpc_user = yourusername-as-in-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #default obvykle správně`
- `rpc_port = 8332 # výchozí pro Mainnet`



V tuto chvíli můžeme pokračovat ve vytváření našeho Wallet v rámci JoinMarket:



```bash
python wallet-tool.py generate
```



Tento příkaz nás nechá zadat heslo, kterým chceme zašifrovat Wallet, a jméno, které mu chceme dát.Když se vás zeptá, zda chcete podporovat věrnostní vazby, doporučuji použít možnost _yes_, vrácený výstup bude vypadat takto:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


v případě, že se objeví chyba, je pravděpodobné, že jsme nesprávně nastavili výše uvedená 4 pole RPC. V případě, že by mohlo pomoci postupovat podle [tohoto návodu](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure), který se nachází v originální dokumentaci JoinMarket.



Dokončili jsme nastavení našeho pracovního prostředí a můžeme začít zkoumat příkazy, které pro nás budou nejužitečnější. Všechny skripty, o kterých budeme hovořit, lze spustit v konzoli a po zadání `--help` získat podrobný výklad.



Nyní se můžeme pokusit o spuštění:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



tento příkaz vám zobrazí všechny různé hloubky portfolia s různými adresami kategorizovanými jako:




- Nové (Address nikdy nepoužité)
- Změna (zbytek předchozí transakce)
- Cj-out (výstup CoinJoin)



zde je praktický příklad výsledku:



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


Nyní můžeme přistoupit k uložení našich prvních Satoshů v rámci jedné nebo více adres, přičemž nezapomeňte, že bez ohledu na tvůrce nebo příjemce software nikdy nepůjde a nebude přímo konsolidovat UTXO do různých hloubek mixu, tímto způsobem můžeme udržovat Satoshy s různými úrovněmi soukromí odděleně v rámci Wallet.



## Odesílání Bitcoin s CoinJoin Single



Nyní můžeme přesunout naše Satoshi. Jedním z hlavních příkazů tohoto programu je skript:



```bash
pyhton sendpayment.py
```


což nám umožní zasílat transakce na jiné adresy s CoinJoin nebo bez ní. Projdeme si, jak to funguje, a několik praktických příkladů. Ve výchozím nastavení je formátování příkazu následující (nezapomeňte nahradit text uzavřený symboly < a >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



základním příkladem použití může být:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


v tomto případě budeme posílat do Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0,05 Btc, tj. 5000000 Satoshi z naší mixdepth 0 (výchozí) tím, že si vybereme 4 až 9 protějšků pro CoinJoin (výchozí možnost).



Chcete-li mít větší kontrolu nad tím, jak a které UTXO utratit, můžeme si projít další možnosti tohoto příkazu:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


v tomto příkladu jsme přidali dvě specifikace: -N udává, s kolika protistranami budeme mixovat, -m hloubku mixu, ze kterého budeme vybírat prostředky. Ve skutečnosti jsme poslali 100 000 000 Sats (1 btc) na Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c s prostředky v mixdepth 1 a mixováním s 5 protistranami.



Pokud jako hodnotu odeslání zadáme 0 a uvedeme mixdepth, joinMarket provede tzv. `sweep`, tj. odešle všechny prostředky v této mixdepth tak, že je vzájemně zkonsoliduje:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



zde jsme poslali všechny prostředky z hloubky mixu 0 (nemohli jsme ji zadat, protože je výchozí), které se mísí se 7 protějšky.



Příkaz sendpayment slouží k přesunu prostředků z joinMarket na externí Wallet nebo k odeslání Satoshi osobě přidáním Layer soukromí mezi námi a ní. Pro získání dostatečné úrovně soukromí na našich UTXO je vhodnější použít příkaz tumbler.py, který si vysvětlíme později v této příručce.



## Být tvůrcem



Skript, kterým se budeme zabývat v této části, je:



```bash
yg-privacyenhanced.py
```



Tento program slouží jako tvůrce v joinMarketu. Program se připojí k našemu uzlu Bitcoin a k internímu trhu platformy, na kterém se tvůrci prezentují jako nabízející likviditu a nabízející hledají protistrany. V případě, že chcete použít věrnostní dluhopis, můžete jej vytvořit pomocí tohoto formátování:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



například:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



výstup, který nám bude vrácen, bude Bitcoin Address (tj. ten, na který budete muset vložit prostředky, které chcete přidělit věrnostnímu programu).



**Upozornění**: Pokud se chystáte vytvořit dluhopis věrnosti (tzv. FB), je třeba věnovat pozornost dvěma věcem;





- jakmile jsou prostředky jednou uloženy, nelze je znovu přesunout, dokud nevyprší jejich platnost. Dávejte pozor na to, kolik sats posíláte na Address a jak formátovat datum. Chyby nejsou přípustné!
- Věrnostní dluhopis je v řetězci snadno rozpoznatelný, proto je vhodné vkládat prostředky prostřednictvím CoinJoin a s původem nesouvisejícím s vaší identitou. Totéž je vhodné udělat, jakmile budete chtít prošlý fidelity bond přesunout mimo JoinMarket.



Je důležité si uvědomit, že věrnostní dluhopis je možné dobít pouze jednou transakcí, v případě násobků UTXO bude za platnou pro FB považována pouze ta největší.



Zabývejme se nyní skriptem uvedeným na začátku tohoto odstavce, jakmile jsme vytvořili věrnostní dluhopis (který, jak si pamatujeme, je nepovinný), jsme připraveni spustit spustitelný soubor, který bude fungovat jako tvůrce na joinMarket. Jakmile jsou saty uloženy na různých adresách a mixdepth, můžeme spustit příkaz:



```bash
python yg-privacyenhanced.py <wallet name>
```



Od této chvíle (po několika minutách připojení k síti) až do zastavení skriptu se náš klient JoinMarket objeví na seznamu aktivních tvůrců v protokolu a nabídne naši likviditu různým protistranám k provedení CoinJoin. Neočekávejte desítky CoinJoinů denně (pokud nemáte obrovskou fidlitu a velkou likviditu uloženou na Wallet), nezapomeňte také, že faktory jako požadované poplatky a uložené Satoshi ovlivňují, jak často budete makerem.



Spuštěním níže uvedeného příkazu si budete moci prohlédnout historii všech transakcí provedených na Wallet a případné zisky (pokud jste tvůrce) nebo výdaje na poplatky (pokud jste příjemce), které jste za dobu trvání portfolia měli.



```bash
python wallet-tool.py <wallet name> history
```



Jakmile vaši Satoshové vytvoří CoinJoiny, budou se pohybovat z jedné hloubky mixu do druhé, dokud nedosáhnou poslední hloubky mixu. Jakmile překročí čtvrtou, vrátí se do mixhloubky 0, je na vás, kolik soukromí získají, než je přesunete do Cold. Wallet, doporučuje se dokončit celý cyklus Wallet.



## Tumbler



A jsme konečně u nejšťavnatější části JoinMarketu, u tumbleru! Pokud jste poslouchali podcast, už víte, o co jde. Než začneme, jedno doporučení: **Nezapomeňte nastavit limity v souboru joinmarket.cfg (jak bylo vysvětleno na začátku) a zvažte spuštění programu pouze tehdy, když jsou onchain poplatky relativně nízké (pod 10 Sats/vB).**



Pro spuštění bubnu je nutné zastavit skript od výrobce (pokud byl aktivní), poté můžeme spustit příkaz:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Je nezbytné zadat **nejméně** 3 výstupní adresy pro tumbler: to proto, aby byla zajištěna dobrá ochrana osobních údajů a aby v průběhu procesu nevznikaly zjevné vazby mezi UTXO. Jako obvykle přidáním `--help` k příkazu můžete přejít a zobrazit všechny další podrobnosti. Přejděme` k zobrazení složitějšího příkladu s pokročilými pravidly:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



V tomto případě jsme spustili tumbling skript, který nepoužije výchozí počet protějšků (parametr -N udává, že požadujeme 7 protějšků s maximální odchylkou 2, tedy náhodný počet tvůrců od 5 do 9) a s větším počtem CoinJoin na hloubku mixu (ve výchozím nastavení tento skript vytváří náhodný počet CoinJoin na sekci Wallet v rozmezí od 1 do 3, při použití příkazu -c 3 1 bude místo toho od 2 DO 4). Tímto způsobem utratíme více Sats v poplatcích, ale budeme mít větší sadu anonymity.



Můžete také přidat libovolný počet výstupních adres (minimálně 3, maximální počet není stanoven jinak než zdravým rozumem). Z důvodu ochrany osobních údajů však není možné rozhodnout, jak bude Satoshi rozdělen mezi adresy zadané jako výstupní.



Tumbler je záměrně dlouhý proces, občas se může stát, že něco přestane fungovat, ve většině případů se to vyřeší během několika hodin. V případě úplného pádu se jej můžeme pokusit restartovat příkazem:



```bash
python tumbler.py --restart
```



Nebo jednoduše znovu spusťte nový příkaz pro převracení. Tím se nespustí plánování předchozího převalování, ale zahájí se nový cyklus míchání. V případě, že zavření terminálu SSH k uzlu zastaví i skript, můžete využít program `TMUX`, který lze nainstalovat pomocí příkazu:



```bash
sudo apt install tmux
```



Spuštění z shellu zadáním `tmux` otevře terminál, který zůstane aktivní na pozadí, i když vzdálené připojení ukončíte. Když se znovu připojíte k uzlu příkazem: `tmux attach` znovu otevřete shell, který zůstal aktivní na pozadí.



## Závěr



JoinMarket je bezbřehý a přizpůsobitelný software. V této příručce jsme objevili hlavní funkce tak, aby jej mohl používat každý (nebo jsem se o to alespoň pokusil, uvědomuji si, že používání tohoto softwaru není procházka růžovým sadem). Jedním z největších problémů JoinMarketu je právě to, že jej používá mnoho lidí a že je tvůrcem. Pokud tento software využívá málo uživatelů, snižuje se celková míra soukromí (anon-set). Proto doufám, že tento návod bude motivovat k používání a přesvědčí vás, abyste si stáhli a nainstalovali můj oblíbený software pro tvorbu CoinJoin. V případě, že chcete jít ještě hlouběji do některých aspektů, doporučuji vám dát přečíst různé podrobné dokumenty na githubu, jsou vermanete dobře zpracované a najdete je zde.



Veselé míchání želv!🐢 💚



[Zde](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) můžete podpořit Turtlecute