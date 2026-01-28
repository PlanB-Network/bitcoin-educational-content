---
name: JoinMarket

description: 如何使用 JoinMarket 透過指令行做 CoinJoin over Bitcoin 的指南與教學
---

![cover](assets/cover.webp)



---

如果您在網路上搜尋「JoinTmarket」而找到這個頁面，我衷心感謝您。不過，您偶然發現的這份指南，是關於一個完全不同，但卻非常有趣的主題！🚬🍁



本教學的目的是透過命令列說明 JoinMarket 的理論與實際操作。🐢 💚



## JoinMarket 理論定義



我們可以將 JoinMarket 定義為一個工具，或是一個 Wallet，它能以完全 Trustless 的方式與其他使用者進行 CoinJoin，而且不需要任何中央協調者。



由於這個工具的整個理論部分非常廣泛，因此我決定在我的播客中以特定的一集來介紹 Address。對於能聽懂義大利語的人，我強烈建議您在聽完這一集後繼續閱讀，以便更好地吸收正確使用此程式的基本概念。



您可以透過這些直接連結追看本集：




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (在此您可直接從瀏覽器收聽)。
- [Antenna pod](https://antennapod.org/) 是免費且開放原始碼的 Podcast 管理程式，不需要註冊。若要尋找這一集，請下載應用程式，在 _feed rss_ 部分貼上 [this link](https://Anchor.fm/s/bd5d5b20/podcast/rss) 來手動加入我的 Podcast，然後搜尋 JoinMarket 專屬的一集。



## 安裝



作業系統：





- Raspiblitz
- 傘
- 我的節點
- Raspibolt



## 組態檔案



JoinMarket 是個可自訂的軟體，擁有無限的設定；這些設定都指定在主程式目錄中名為 `Joinmarket.cfg` 的設定檔中。



在本節中，我們將介紹一些您可能會感興趣的領域，您可以根據自己的需求進行探索和/或修改。我想強調的是，以下列出的所有變更都是有用的資訊，可以讓軟體的操作符合個人需求，但並非強制執行。



首先讓我們移到 `joinmarket/scripts` 資料夾，然後執行指令：



```bash
python wallet-tool.py generate
```


此時我們應該會收到一個錯誤，但這樣做會使軟體為我們 generate 一個預先設定的設定檔。我們可以從終端機編輯設定檔，方法如下



```bash
nano joinmarket.cfg
```



或



```bash
vim joinmarket.cfg
```



一旦打開，我們會發現許多行有各種設定及其英文說明。具體來說，我們將在下面分析最有趣的變數：





- `merge_algorithm` 如果我們做為一個製造商，這個欄位會調整軟體整合未使用的 Output 的積極程度。如果我們有許多 UTXOs 要合併，從 _gradual_ 切換到 _greedy_ 可能會比較合理。
- `tx_fees` 用來調整支付交易的費用，如果您經常使用不倒翁 (我們稍後會談到) 的話，變更這個設定是非常有用的，因為如果在執行後者的過程中費用激增，如果我們沒有正確設定這個欄位，就有可能為了 CoinJoin 而花費大量的 Sats。以千為單位設定值 (例如 2000)，這將等於 2 Sats/vBytes，3500 等於 3.5 Sats/vBytes，以此類推。我建議根據您的需求，設定 1500 到 6000 之間的數值。
- `max_cj_fee_abs` 用來指定在 CoinJoin 期間，我們願意為所選擇的製造商支付的絕對金額。製造商的預設值是 200 Sats，一個好的選擇可能是每個對手從 200 到 1000 Sats 不等（這是基於您想要花多少錢，以及您為您的 CoinJoins 尋求多少anon-set）。
- `max_cj_fee_rel` 的功能與上述欄位相同，但指定了我們願意支付給每個交易對手的相對費用（百分比）。由於這是一個 ` 百分比 ` 值，請注意不要設定高值，以免在 CoinJoins 的大額交易中產生高昂的費用。製造商的預設值是 _0.00002_，我建議使用類似的或略高的值。
- `minimum_makers` 是指定我們與多少個其他交易對手做 CoinJoin 的欄位，預設 joinMarket 總是選擇 4 到 9 個交易對手，如果我們想要更隱私，我們可以將這個值提高到 5 或 6 (不過這會讓交易更昂貴)。
- `cjfee_a` 指定，在我們作為製造商的情況下，我們想要收取多少 Sats 的絕對值來出租我們的流動性。這個欄位是完全主觀的，預設值已經很好（我們作為莊家會有更好的隱私），如果我們想在更短的時間內賺更多的 CoinJoin，可以考慮將其設為 0。
- `cjfee_r` 與上述欄位相同，但以百分比表示，而非絕對值。我再次建議您保留預設值或降低預設值，以吸引更多人購買。
- `ordertype` 利用這個欄位，我們可以從製造商處選擇是絕對出價 (absoffer) 還是百分比出價 (reloffer)。通常在經濟問題上，出價者偏好絕對出價。
- `minsize` 如果作為製造者，我們不希望 UTXO 太小，我們可以指定最低 CoinJoin 參與。這個欄位以 Satoshi 表示，完全是主觀的。我們可以將此欄位保留為 0 或增加為 500000 (Sats)、1000000 (Sats)，如此類推。



請小心不要編輯錯誤的欄位，joinmarket.cfg 檔案中的某些變數如果設定錯誤，可能會損害軟體的功能或完全毀壞您的隱私！



## 工作環境設定



有些節點會自動在 joinmarket.cfg 檔案中為這些欄位設定正確的值，我建議您重新手動檢查：





- `rpc_user = yourusername-as-in-Bitcoin.conf`。
- `rpc_password=yourpassword-as-in-Bitcoin.conf`。
- `rpc_host = localhost #預設值通常正確``。
- `rpc_port = 8332 # Mainnet` 的預設值



此時我們可以在 JoinMarket 內建立我們的 Wallet：



```bash
python wallet-tool.py generate
```



這個指令會讓我們輸入一個密碼來加密 Wallet，以及我們想要給它的名稱，當它詢問您是否要支援保真度綁定時，我建議您使用 _yes_ 選項，傳回的輸出結果會是這樣：



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


如果出現錯誤，很可能是我們錯誤設定上面指定的 4 個 RPC 欄位。如果您有任何疑問，請參考 JoinMarket 原始文件中的 [this guide](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure)。



我們已經完成工作環境的設定，可以開始探索對我們最有用的指令。我們將討論的所有指令碼都可以在控制台中啟動，接著是 `--help`，可以得到深入的解釋。



現在我們可以嘗試啟動：



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



此指令將顯示所有不同的 Wallet mixdepths 與不同的位址分類：




- 全新 (Address 從未使用)
- 變更（先前交易的剩餘部分）
- Cj-out (CoinJoin 的輸出)



這裡有一個實用的結果範例：



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


現在我們可以將第一個 Satoshis 存放在一個或多個地址中，請記住，無論製造者或接受者是誰，軟體都不會直接將 UTXO 合併到不同的 mixdepths 中，這樣我們就可以在 Wallet 中分開不同隱私等級的 Satoshs。



## 傳送 Bitcoin 與 CoinJoin 單一



現在我們可以移動我們的 Satoshis。本軟體的主要指令之一是指令碼：



```bash
pyhton sendpayment.py
```


可讓我們在有 CoinJoin 或沒有 CoinJoin 的情況下，將交易傳送到其他地址。讓我們來看看它的運作方式和一些實例。默認情況下，命令的格式為（記得取代由符號 < 和 > 圍繞的文字）：



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



一個基本的使用範例可能是：



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


在這種情況下，我們將從我們的 mixdepth 0（預設值）向 Address 傳送 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc，即 5000000 Satoshi，方法是為 CoinJoin 選擇 4 到 9 個對應項目（預設選項）。



若要更多地控制如何以及花費哪些 UTXO，我們可以查看此指令的附加選項：



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


在這個範例中，我們加入了兩個規格： -N 表示我們要與多少個交易對手混合，-m 表示我們要從中提取資金的混合深度。事實上，我們已將 100,000,000 Sats (1 btc) 傳送至 Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c，資金在 mixdepth 1 中，並與 5 個交易對手混合。



如果我們指定一個 mixdepth，以 0 作為傳送值，joinMarket 就會執行所謂的「掃蕩」，也就是說，它會將該 mixdepth 中的所有基金互相整合，然後傳送出去：



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



在這裡，我們將來自 mixdepth 0 的所有資金 (我們可以不指定，因為這是預設值) 與 7 個對應項目混合。



sendpayment 指令用來從 joinMarket 移動資金到外部 Wallet 或透過在我們和某人之間加入 Layer 的隱私來傳送 Satoshi 給他。若要在我們的 UTXOs 上獲得足夠的隱私等級，使用 tumbler.py 指令會比較適合，我們會在本指南稍後解釋。



## 成為製造者



本節要介紹的腳本是：



```bash
yg-privacyenhanced.py
```



該程式用於在 joinMarket 中充當莊家。該軟件將連接到我們的 Bitcoin 節點和平台的內部市場，在該市場中，莊家作為流動性出價者展示自己，而莊家則尋找交易對手。如果您想使用保真債券，您可以使用此格式創建一個：



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



例如：



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



將返回給我們的輸出將是 Bitcoin Address（即您需要在上面存入您要分配給保真的資金）。



**注意**：如果您要建立 Fidelity Bond（又稱 FB），有兩件事必須密切注意；





- 一旦存入資金後，在到期前無法再次移動。請注意您傳送至 Address 的 Satss 數量以及日期的格式。不允許出錯！
- 保真保證金很容易被識別，所以建議您透過 CoinJoin 存入資金，並使用與您身份無關的來源。一旦您想要將已過期的保真債券移出 JoinMarket，同樣的事情也是可取的。



請務必記住，只需一次交易即可重新載入保真債券，如果是 UTXO 多次交易，則只有最大的一次交易才會被視為 FB 有效。



現在讓我們處理本段開頭提到的腳本，一旦我們建立了保真債券（我們記得這是選擇性的），我們就可以運行可執行檔在 joinMarket 上作為莊家了。一旦 Satss 存入不同的地址和 mixdepth，我們就可以執行指令：



```bash
python yg-privacyenhanced.py <wallet name>
```



從這一點開始（連線到網路幾分鐘之後），直到我們停止腳本，我們的JoinMarket客戶端會出現在協定上活躍的莊家列表上，並提供我們的流動資金給不同的交易對手做CoinJoin。不要期望每天有幾十個 CoinJoins（除非您有巨大的信心和大量的流動資金存放在 Wallet），也請記住，所需的費用和 Satoshis 存款等因素會影響您成為莊家的頻率。



執行下面的指令，您就可以看到 Wallet 上所有交易的歷史記錄，以及您在 Wallet 使用期間的任何收益（如果您是莊家）或費用支出（如果您是閒家）。



```bash
python wallet-tool.py <wallet name> history
```



一旦您的 Satoshis 進行 CoinJoins，它們會從一個混合深度移動到另一個混合深度，直到它們到達最後一個混合深度。一旦過了第四個，它們就會回到混合深度 0，這取決於在將它們移到 Cold Wallet 之前要獲得多少隱私，建議完成一個完整的 Wallet 循環。



## 不倒翁



我們終於來到 JoinMarket 最多汁的部分，不倒翁！如果您聽過播客，您已經知道這是怎麼一回事了。在我們開始之前，有一個建議： **小心費用！** 記得在 joinmarket.cfg 檔案中設定限制（如開頭所說明的），並考慮只在 onchain 費用相對較低時（低於 10 Sats/vB）才執行程式。



要啟動不倒翁，必須先停止製作程式腳本 (如果它已啟動)，之後才能執行指令：



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



必須輸入 ** 至少 ** 3 個輸出位址給滾揉器：這是為了確保良好的隱私性，並且在整個過程中不會在 UTXOs 之間產生明顯的連結。如同往常一樣，只要在指令中加入`--help`，您就可以看到所有額外的細節。讓我們去看一個有進階規則的更複雜範例：



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



在這種情況下，我們啟動了一個翻滾腳本，它不會使用預設的對應數量（-N 參數表示我們需要 7 個對應數量，最大方差為 2，因此製造商的隨機數量從 5 到 9），而且每個 mixdepth 的 CoinJoin 數量較多（預設情況下，此腳本製造每段 Wallet 的 CoinJoin 的隨機數量從 1 到 3 不等，使用 -c 3 1 指令反而會從 2 到 4 不等）。如此一來，我們將花費更多的 Sats 費用，但卻有更大的匿名集。



您也可以加入任意數量的輸出位址 (最少 3 個，除了常識之外沒有最大值)。但是，基於隱私權問題，無法決定 Satoshi 如何在指定為輸出的位址間分配。



Tumbler 是一個特意設計的長時間程序，偶爾可能會發生某些事情停止運作，在大多數情況下，這會在幾小時內自行解決。在完全當機的情況下，我們可以嘗試用命令重新啟動它：



```bash
python tumbler.py --restart
```



或者只需重新啟動新的翻滾指令。這不會啟動前一個翻滾器的排程，但會開始一個新的混合循環。萬一關閉節點的 SSH 終端也會停止腳本，您可以利用可安裝指令的 `TMUX` 程式：



```bash
sudo apt install tmux
```



從 shell 鍵入 `tmux` 來啟動它，會為您開啟一個終端機，即使您關閉遠端連線，該終端機仍會在背景中保持活動。當您使用 `tmux attach` 指令重新連線到您的節點時，您會重新開啟終端機：`tmux attach` 重新連線到您的節點時，您會重新開啟在背景中保持活躍的 shell。



## 總結



JoinMarket 是一個無限且可自訂的軟體。在這份指南中，我們發現了它的主要功能，因此任何人都有可能使用它 (或至少我已經嘗試，我知道使用這個軟體並不是在公園裡散步)。JoinMarket 最大的問題之一就是：使用它的人數和成為製造者。如果很少使用者利用這個軟體，整體的隱私（anon-set）就會降低。這就是為什麼我希望這份指南可以激勵使用，並說服您下載並安裝我最喜歡的軟體來做 CoinJoin。如果您想要更深入地瞭解某些方面，我建議您閱讀 github 上的各種深入說明文件，它們做得非常好，您可以在這裡找到。



快樂的混合龜！🐢 💚



[Here](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) 您可以支援 Turtlecute