---
name: JoinMarket

description: 명령줄을 통해 JoinMarket을 사용하여 Bitcoin을 통해 CoinJoin을 수행하는 방법에 대한 가이드 및 튜토리얼
---

![cover](assets/cover.webp)



---

온라인에서 "JoinTmarket"을 검색하여 이 페이지를 찾으셨다면 진심으로 감사드립니다. 하지만 완전히 다르지만 매우 흥미로운 주제를 다루는 가이드를 우연히 발견하셨습니다! 🚬🍁



이 튜토리얼의 목적은 명령줄을 통해 JoinMarket의 이론적 및 실제 작동을 설명하는 것입니다. 🐢 💚



## JoinMarket 이론적 정의



JoinMarket은 중앙 코디네이터 없이 다른 사용자와 완전히 Trustless 방식으로 CoinJoin을 가능하게 하는 도구, 즉 Wallet로 정의할 수 있습니다.



이 도구의 전체 이론적 부분이 매우 광범위하기 때문에 팟캐스트의 특정 에피소드에서 Address를 다루기로 결정했습니다. 이탈리아어를 이해할 수 있는 분이라면 이 프로그램을 올바르게 사용하기 위한 기본 개념을 더 잘 이해할 수 있도록 에피소드를 들은 후에도 계속 읽어보시기를 적극 권장합니다.



이 직접 링크에서 에피소드를 확인할 수 있습니다:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [구글 팟캐스트](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep)(여기에서 브라우저에서 바로 들을 수 있습니다).
- [안테나 팟](https://antennapod.org/)은 등록이 필요 없는 무료 오픈소스 팟캐스트 매니저입니다. 앱을 다운로드하고 [이 링크](https://Anchor.fm/s/bd5d5b20/podcast/rss)를 _피드 RSS_ 섹션에 붙여넣어 내 팟캐스트를 수동으로 추가한 다음 JoinMarket 전용 에피소드를 검색합니다.



## 설치



운영 체제:





- 라스피블리츠
- Umbrel
- MyNode
- 라스피볼트



## 구성 파일



JoinMarket은 무한한 설정이 가능한 사용자 정의 소프트웨어로, 이러한 설정은 기본 프로그램 디렉토리에 있는 'Joinmarket.cfg'라는 구성 파일에 지정되어 있습니다.



이 섹션에서는 필요에 따라 살펴보고 수정할 수 있는 몇 가지 필드를 살펴보고자 합니다. 아래에 나열된 모든 변경 사항은 필수 사항은 아니지만 개인의 필요에 따라 소프트웨어 작동을 조정하기 위해 알아두면 유용하다는 점을 강조하고 싶습니다.



먼저 `joinmarket/scripts` 폴더로 이동하여 명령을 실행해 보겠습니다:



```bash
python wallet-tool.py generate
```


이 시점에서 오류가 발생해야 하지만 이렇게 하면 소프트웨어가 미리 설정된 설정 파일을 generate로 생성합니다. 터미널에서 설정 파일을 편집할 수 있습니다:



```bash
nano joinmarket.cfg
```



또는:



```bash
vim joinmarket.cfg
```



를 열면 다양한 설정과 그에 대한 설명이 영어로 된 수많은 줄을 볼 수 있습니다. 특히 가장 흥미로운 변수를 아래에서 분석해 보겠습니다:





- merge_algorithm`은 메이커의 경우 이 필드에서 소프트웨어가 사용하지 않은 출력을 얼마나 적극적으로 통합할지 조정합니다. 통합할 UTXO가 많은 경우 _gradual_에서 _greedy_로 전환하는 것이 좋을 수 있습니다
- tx_fees`는 테이커가 트랜잭션을 지불할 수수료를 조정하며, 텀블러를 자주 사용하는 경우 이 설정을 변경하는 것이 매우 유용합니다(나중에 설명하겠습니다). 후자를 실행하는 동안 수수료가 급증하는 경우 이 필드를 올바르게 설정하지 않으면 CoinJoin에 많은 Sats을 소비할 위험이 있기 때문입니다. 2000과 같이 수천 단위로 값을 설정하면 2 Sats/vBytes, 3500 ~ 3.5 Sats/vBytes 등이 됩니다. 필요에 따라 1500에서 6000 사이의 숫자를 권장합니다.
- 'max_cj_fee_abs'는 CoinJoin 기간 동안 선택한 메이커에게 절대적인 금액으로 지불할 의향이 있는 금액을 지정하는 데 사용됩니다. 기본적으로 메이커에 대한 이 필드는 200 Sats이며, 좋은 옵션은 상대방당 200~1000 Sats 사이의 숫자일 수 있습니다(이는 지출하고자 하는 금액과 코인조인에 대해 얼마나 많은 익명 세트를 원하는지에 따라 결정됩니다)
- max_cj_fee_rel`은 위의 필드와 동일한 기능을 하지만 각 거래 상대방에게 지불하고자 하는 상대 수수료(백분율)를 지정합니다. 이 값은 '백분율' 값이므로 금액이 많은 코인코인에서는 높은 비용을 피하기 위해 높은 값을 설정하지 않도록 주의하시기 바랍니다. 메이커의 기본값은 _0.00002_이며, 이와 비슷하거나 약간 높은 값을 권장합니다.
- '최소_메이커'는 CoinJoin를 수행하는 다른 거래 상대방 수를 지정하는 필드로, 기본적으로 joinMarket은 항상 4~9개의 거래 상대방을 선택하며, 개인정보 보호를 강화하려면 이 값을 5 또는 6으로 높일 수 있습니다(단, 거래 비용이 더 비싸지게 됩니다).
- 'cjfee_a'는 메이커로 활동하는 경우 유동성 대여를 위해 절대적으로 얼마나 많은 Sats을 받고자 하는지를 지정합니다. 이 필드는 전적으로 주관적이며, 기본값은 이미 매우 좋으며(따라서 메이커로서 더 나은 프라이버시를 확보할 수 있습니다) 더 짧은 시간에 더 많은 CoinJoin를 만들고 싶다면 0으로 설정하는 것을 고려할 수 있습니다.
- cjfee_r` 위 필드와 동일하지만 절대값이 아닌 백분율로 표시됩니다. 다시 말하지만 더 많은 응시자를 유치하려면 기본값을 그대로 두거나 낮추는 것이 좋습니다.
- 주문 유형` 이 필드를 사용하면 메이커에서 절대가(앱소퍼) 또는 퍼센트(리로퍼)로 청구할지 여부를 선택합니다. 일반적으로 테이커는 경제적인 문제 때문에 절대 입찰을 선호합니다.
- '최소 크기'는 메이커로서 UTXO이 너무 작고 싶지 않은 경우 참여할 수 있는 최소 CoinJoin을 지정할 수 있습니다. 이 필드는 Satoshi로 표현되며 전적으로 주관적입니다. 이 필드를 0으로 두거나 500000(Sats), 1000000(Sats) 등으로 늘릴 수 있습니다.



잘못된 필드를 편집하지 않도록 각별히 주의하세요. joinmarket.cfg 파일의 일부 변수는 잘못 설정하면 소프트웨어의 기능을 손상시키거나 개인정보가 완전히 소멸될 수 있으므로 눈을 크게 뜨고 최대한 주의하세요!



## 작업 환경 설정



일부 노드는 joinmarket.cfg 파일 내에서 이러한 필드에 대한 올바른 값을 자동으로 설정하므로 수동으로 다시 확인하는 것이 좋습니다:





- `rpc_user = yourusername-as-in-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = 로컬 호스트 #기본값은 일반적으로 올바름`
- `rpc_port = 8332 # Mainnet의 기본값`



이 시점에서 JoinMarket 내에서 Wallet 생성을 진행할 수 있습니다:



```bash
python wallet-tool.py generate
```



이 명령은 Wallet를 암호화할 비밀번호와 이름을 입력하게 하고, 충실도 채권을 지원할지 여부를 묻는 메시지가 표시되면 _yes_ 옵션을 사용하는 것이 좋으며, 반환되는 출력은 다음과 같이 표시됩니다:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


오류가 발생하는 경우 위에 명시된 4개의 RPC 필드를 잘못 설정했을 가능성이 높습니다. 이 경우 JoinMarket 문서 원본에 있는 [이 가이드](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure)를 따르는 것이 도움이 될 수 있습니다.



작업 환경 설정을 완료했으며 가장 유용한 명령어를 살펴볼 수 있습니다. 앞으로 설명할 모든 스크립트는 콘솔에서 실행한 다음 `--도움말`을 입력하면 자세한 설명을 확인할 수 있습니다.



이제 실행을 시도해 볼 수 있습니다:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



이 명령은 다양한 주소로 분류된 다양한 Wallet 믹스뎁스를 모두 표시합니다:




- 신규(Address 미사용)
- 변경 아웃(이전 거래의 나머지 부분)
- Cj-out(CoinJoin의 출력)



다음은 실제 결과의 예입니다:



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


이제 첫 번째 사토시를 하나 이상의 주소에 입금할 때 메이커나 테이커에 관계없이 소프트웨어가 UTXO을 다른 믹스뎁스로 직접 통합하지 않는다는 점을 기억하면, 프라이버시 수준이 다른 사토시를 Wallet 내에서 분리하여 보관할 수 있습니다.



## CoinJoin 싱글로 Bitcoin 보내기



이제 사토시를 움직일 수 있습니다. 이 소프트웨어의 주요 명령 중 하나는 스크립트입니다:



```bash
pyhton sendpayment.py
```


를 사용하면 CoinJoin를 사용하거나 사용하지 않고 다른 주소로 트랜잭션을 보낼 수 있습니다. 작동 방식과 몇 가지 실제 예시를 살펴보겠습니다. 기본적으로 명령의 서식은 (< 및 > 기호로 둘러싸인 텍스트를 대체하는 것을 잊지 마세요) 다음과 같습니다:



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



를 사용하는 것이 기본적인 예가 될 수 있습니다:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


이 경우 믹스뎁스 0(기본값)에서 CoinJoin(기본 옵션)에 대해 4~9개 중 하나를 선택해 Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05Btc, 즉 5000000 Satoshi로 전송합니다.



이 명령에 대한 추가 옵션을 살펴보고 어떤 UTXO를 어떻게 사용할지 더 자세히 제어할 수 있습니다:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


이 예에서는 두 가지 사양을 추가했습니다: -N은 얼마나 많은 거래 상대방과 믹싱할 것인지, -m은 자금을 인출할 믹스 깊이를 나타냅니다. 실제로 믹스뎁스 1의 자금으로 5개의 거래 상대방과 믹스하여 100,000,000 Sats(1비트코인)를 Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c로 보냈습니다.



믹스뎁스를 지정하여 전송 값으로 0을 입력하면 joinMarket은 소위 '스윕'을 수행하여 해당 믹스뎁스에 있는 모든 자금을 서로 통합하여 전송합니다:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



여기서는 믹스뎁스 0(기본값이므로 지정하지 않았을 수 있음)의 모든 자금을 7개의 대응 자산과 혼합하여 보냈습니다.



Sendpayment 명령은 joinMarket에서 외부 Wallet로 자금을 이동하거나 우리와 그 사이에 개인정보 보호 Layer를 추가하여 개인에게 Satoshi을 보내는 데 사용됩니다. UTXO에서 충분한 수준의 개인정보 보호를 확보하려면 이 가이드의 뒷부분에서 설명하는 tumbler.py 명령을 사용하는 것이 더 적절합니다.



## 메이커 되기



이 섹션에서 다룰 스크립트는 다음과 같습니다:



```bash
yg-privacyenhanced.py
```



이 프로그램은 조인마켓에서 메이커 역할을 하는 데 사용됩니다. 이 소프트웨어는 Bitcoin 노드와 플랫폼의 내부 마켓플레이스에 연결하여 메이커가 유동성 입찰자로 나서고 테이커가 거래상대방을 찾습니다. 충실도 채권을 사용하려는 경우 이 포맷으로 채권을 생성할 수 있습니다:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



예를 들어



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



당사에 반환되는 출력물은 Bitcoin Address(즉, 충실도에 할당하려는 자금을 입금해야 하는 출력물)가 될 것입니다.



**주의**: 피델리티 채권(일명 FB)을 만들려는 경우 주의해야 할 두 가지 사항이 있습니다;





- 자금이 입금되면 만료될 때까지 다시 이동할 수 없습니다. Address에 전송하는 Sats의 수와 날짜 형식에 주의하세요. 오류는 허용되지 않습니다!
- 충실도 채권은 체인에서 쉽게 알아볼 수 있으므로 신원과 무관한 출처로 CoinJoin을 통해 자금을 입금하는 것이 좋습니다. 만료된 충실도 채권을 JoinMarket 밖으로 옮기고자 할 때도 동일한 방법을 사용하는 것이 좋습니다.



단 한 번의 거래로 충실도 채권을 재충전할 수 있으며, UTXO 배수의 경우 가장 큰 배수만 FB에 유효한 것으로 간주된다는 점을 기억하는 것이 중요합니다.



이제 이 단락의 시작 부분에서 언급한 스크립트를 다루겠습니다. 충실도 본드(선택 사항임을 기억하세요)를 생성한 후에는 실행 파일을 실행하여 joinMarket에서 메이커 역할을 할 준비가 된 것입니다. 다양한 주소와 믹스뎁스에 사츠가 입금되면 명령을 실행할 수 있습니다:



```bash
python yg-privacyenhanced.py <wallet name>
```



이 시점부터 (네트워크에 몇 분간 연결한 후) 스크립트를 중지할 때까지 JoinMarket 클라이언트는 프로토콜의 활성 메이커 목록에 나타나고 다양한 거래 상대방에게 유동성을 제공하여 CoinJoin를 만들게 됩니다. 하루에 수십 개의 코인조인을 기대하지 마시고(Wallet에 엄청난 유동성을 예치하지 않는 한), 필요한 수수료와 예치된 사토시와 같은 요소가 메이커가 되는 빈도에 영향을 미친다는 점을 기억하시기 바랍니다.



아래 명령을 실행하면 Wallet에서 이루어진 모든 거래 내역과 Wallet의 수명 기간 동안 발생한 이익(메이커인 경우) 또는 수수료 비용(테이커인 경우)을 확인할 수 있습니다.



```bash
python wallet-tool.py <wallet name> history
```



사토시가 코인조인을 만들면 마지막 믹스뎁스에 도달할 때까지 믹스뎁스에서 믹스뎁스로 이동합니다. 네 번째를 지나면 믹스뎁스 0으로 돌아가는데, 얼마나 많은 프라이버시를 확보한 후 Cold Wallet로 이동하는지는 여러분의 선택에 달려 있으며, 전체 Wallet 사이클을 완료하는 것이 좋습니다.



## 텀블러



드디어 조인마켓의 가장 핵심적인 부분인 텀블러를 소개합니다! 팟캐스트를 들어보셨다면 어떤 내용인지 이미 알고 계실 것입니다. 시작하기 전에 한 가지 권장 사항을 알려드리겠습니다: **수수료에 주의하세요!** 처음에 설명한 대로 joinmarket.cfg 파일에서 한도를 설정하고 온체인 수수료가 상대적으로 낮을 때만(10Sats/vB 미만) 프로그램을 실행하는 것을 고려하세요.



텀블러를 실행하려면 메이커에서 스크립트를 중지해야 하며(활성화된 경우), 그 후에 명령을 실행할 수 있습니다:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



텀블러의 출력 주소를 **최소** 3개 이상 입력해야 합니다. 이는 개인정보 보호를 보장하고 프로세스 전반에 걸쳐 UTXO 간에 명백한 링크를 만들지 않기 위한 것입니다. 평소와 같이 명령에 `--help`를 추가하면 모든 추가 세부 정보를 볼 수 있습니다. 고급 규칙이 있는 좀 더 복잡한 예제를 살펴보겠습니다:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



이 경우 기본 카운터 수를 사용하지 않고(-N 매개변수는 최대 분산이 2인 7개의 카운터 수가 필요하므로 5에서 9까지 무작위 수의 메이커가 필요함) 믹스뎁스당 더 많은 수의 CoinJoin를 사용하는 텀블링 스크립트를 시작했습니다(기본적으로 이 스크립트는 1~3 범위의 Wallet 섹션당 무작위 수의 CoinJoin를 만들지만 -c 3 1 명령을 사용하면 2~4까지가 됩니다). 이렇게 하면 더 많은 Sats을 수수료로 사용하지만 익명성이 더 많이 설정됩니다.



출력 주소를 원하는 만큼 추가할 수도 있습니다(최소 3개, 상식적인 수준 외에는 최대값이 없음). 그러나 개인정보 보호 문제로 인해 출력으로 지정된 주소에 Satoshi을 어떻게 분배할지는 결정할 수 없습니다.



텀블러는 의도적으로 긴 프로세스로, 가끔 작동이 멈추는 경우가 있지만 대부분의 경우 몇 시간 내에 저절로 해결됩니다. 완전히 중단된 경우 다음 명령을 사용하여 재시작을 시도해 볼 수 있습니다:



```bash
python tumbler.py --restart
```



또는 새 텀블링 명령을 다시 시작합니다. 이렇게 하면 이전 텀블러의 스케줄링이 시작되지는 않지만 새로운 믹싱 주기가 시작됩니다. 노드에 대한 SSH 터미널을 닫아도 스크립트가 중지되는 경우 이 명령으로 설치할 수 있는 `TMUX` 프로그램을 활용할 수 있습니다:



```bash
sudo apt install tmux
```



셸에서 `tmux`를 입력하여 실행하면 원격 연결을 닫아도 백그라운드에서 활성 상태로 유지되는 터미널이 열립니다. 명령으로 노드에 다시 연결하면 터미널이 다시 열립니다: tmux attach` 명령으로 노드에 다시 연결하면 백그라운드에서 활성 상태로 유지되던 셸이 다시 열립니다.



## 결론



JoinMarket은 무한한 사용자 정의가 가능한 소프트웨어입니다. 이 가이드에서는 누구나(또는 적어도 제가 사용해 본 결과 이 소프트웨어를 사용하는 것이 공원에서 산책하는 것이 아니라는 것을 깨달았습니다) 사용할 수 있도록 주요 기능을 발견했습니다. JoinMarket의 가장 큰 문제 중 하나는 바로 이 소프트웨어를 사용하고 메이커가 되는 사람의 수입니다. 이 소프트웨어를 사용하는 사용자가 적으면 전반적인 프라이버시(익명 설정)가 낮아집니다. 그렇기 때문에 이 가이드가 사용을 장려하고 제가 가장 좋아하는 소프트웨어를 다운로드하여 설치하여 CoinJoin를 만들도록 설득하는 데 도움이 되기를 바랍니다. 몇 가지 측면에 대해 더 자세히 알아보고 싶다면 깃허브에 있는 다양한 심층 문서를 읽어보시길 권해드립니다.



행복한 믹싱 거북이!🐢 💚



[여기](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR)에서 터틀큐트를 지원할 수 있습니다