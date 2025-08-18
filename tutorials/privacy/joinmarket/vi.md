---
name: Tham gia thị trường

description: Hướng dẫn và hướng dẫn cách sử dụng JoinMarket để thực hiện CoinJoin trên Bitcoin thông qua dòng lệnh
---

![cover](assets/cover.webp)



---

Nếu bạn tìm thấy trang này bằng cách tìm kiếm trực tuyến "JoinTmarket", tôi xin chân thành cảm ơn. Tuy nhiên, bạn đã tình cờ tìm thấy một hướng dẫn đề cập đến một chủ đề hoàn toàn khác nhưng cực kỳ thú vị! 🚬🍁



Mục tiêu của hướng dẫn này là minh họa hoạt động lý thuyết và thực hành của JoinMarket thông qua dòng lệnh. 🐢 💚



## Định nghĩa lý thuyết của JoinMarket



Chúng ta có thể định nghĩa JoinMarket là một công cụ hoặc Wallet cho phép CoinJoin kết nối với những người dùng khác theo cách hoàn toàn giống Trustless và không cần bất kỳ điều phối viên trung tâm nào.



Vì toàn bộ phần lý thuyết của công cụ này cực kỳ rộng, tôi quyết định sẽ giới thiệu nó trong một tập podcast cụ thể. Với những ai hiểu tiếng Ý, tôi thực sự khuyên bạn nên tiếp tục đọc sau khi nghe tập podcast, để nắm vững hơn các khái niệm cơ bản và sử dụng chương trình này một cách hiệu quả.



Bạn có thể theo dõi tập phim tại các liên kết trực tiếp sau:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Podcast của Google](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon âm nhạc](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b 03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---rùa dễ thương)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (bạn có thể nghe trực tiếp từ trình duyệt tại đây).
- [Antenna pod](https://antennapod.org/) là một trình quản lý podcast miễn phí và mã nguồn mở, không yêu cầu đăng ký. Để tìm tập, hãy tải xuống ứng dụng, thêm podcast của tôi theo cách thủ công bằng cách dán [liên kết này](https://Anchor.fm/s/bd5d5b20/podcast/rss) vào phần _feed rss_, sau đó tìm tập dành riêng cho JoinMarket.



## Cài đặt



Hệ điều hành:





- Raspiblitz
- Ô
- Nút của tôi
- Raspibolt



## Tệp cấu hình



JoinMarket là phần mềm có thể tùy chỉnh với vô số cài đặt; các cài đặt này được chỉ định trong tệp cấu hình nằm trong thư mục chương trình chính có tên là `Joinmarket.cfg`.



Trong phần này, chúng ta sẽ xem xét một số lĩnh vực mà bạn có thể thấy thú vị để khám phá và/hoặc điều chỉnh, tùy thuộc vào nhu cầu của bạn. Tôi muốn nhấn mạnh rằng tất cả những thay đổi được liệt kê dưới đây đều hữu ích để bạn có thể điều chỉnh hoạt động của phần mềm cho phù hợp với nhu cầu cá nhân mà không bắt buộc.



Đầu tiên, hãy chuyển đến thư mục `joinmarket/scripts` và chạy lệnh:



```bash
python wallet-tool.py generate
```


Lúc này, chúng ta sẽ gặp lỗi, nhưng làm như vậy sẽ khiến phần mềm tự động tạo một tệp cài đặt mặc định cho chúng ta. Chúng ta có thể chỉnh sửa tệp cài đặt từ terminal bằng cách:



```bash
nano joinmarket.cfg
```



hoặc:



```bash
vim joinmarket.cfg
```



Sau khi mở, chúng ta sẽ thấy nhiều dòng với các thiết lập khác nhau và giải thích bằng tiếng Anh. Cụ thể, chúng ta sẽ phân tích các biến số thú vị nhất dưới đây:





- `merge_algorithm` trong trường hợp chúng ta là người tạo, trường này sẽ điều chỉnh mức độ tích cực mà phần mềm sẽ hợp nhất các Đầu ra chưa sử dụng. Trong trường hợp chúng ta có nhiều UTXO cần hợp nhất, việc chuyển từ _gradual_ sang _greedy_ có thể là hợp lý.
- `tx_fees` điều chỉnh phí giao dịch với tư cách là người nhận. Việc thay đổi cài đặt này rất hữu ích trong trường hợp bạn thường xuyên sử dụng tumbler (chúng ta sẽ nói về điều này sau), bởi vì nếu phí tăng đột biến trong quá trình thực hiện tumbler, nếu chúng ta không thiết lập đúng trường này, chúng ta có nguy cơ phải chi rất nhiều Sats cho CoinJoin. Bằng cách đặt giá trị theo đơn vị nghìn (chẳng hạn như 2000), con số này sẽ tương đương với 2 Sats/vByte, 3500 đến 3,5 Sats/vByte, v.v. Tôi khuyên bạn nên chọn một con số từ 1500 đến 6000 tùy theo nhu cầu của bạn.
- `max_cj_fee_abs` được sử dụng để chỉ định số tiền chúng ta sẵn sàng trả theo giá trị tuyệt đối cho các maker mà chúng ta chọn trong CoinJoin. Theo mặc định, trường này dành cho maker là 200 Sats, một lựa chọn tốt có thể là một con số từ 200 đến 1000 Sats cho mỗi đối tác (điều này dựa trên số tiền bạn muốn chi tiêu và số lượng anon-set bạn tìm kiếm cho CoinJoin của mình).
- `max_cj_fee_rel` có cùng chức năng với trường trên nhưng chỉ định mức phí tương đối (phần trăm) mà chúng ta sẵn sàng trả cho mỗi bên đối tác. Vì đây là giá trị `phần trăm`, hãy cẩn thận không đặt giá trị cao để tránh chi phí cao trong CoinJoins với số lượng lớn. Giá trị mặc định cho người tạo là _0,00002_, tôi khuyên bạn nên đặt giá trị tương tự hoặc cao hơn một chút.
- `minimum_makers` là trường chỉ định số lượng đối tác khác mà chúng ta thực hiện CoinJoin, theo mặc định joinMarket luôn chọn từ 4 đến 9 đối tác, nếu muốn bảo mật hơn, chúng ta có thể tăng giá trị này lên 5 hoặc 6 (tuy nhiên điều này sẽ làm cho các giao dịch tốn kém hơn).
- `cjfee_a` chỉ định, trong trường hợp chúng ta là người tạo ra, số lượng Sats theo giá trị tuyệt đối mà chúng ta muốn thu thập để cho thuê thanh khoản. Trường này hoàn toàn mang tính chủ quan, giá trị mặc định đã rất tốt (do đó, chúng ta sẽ có quyền riêng tư tốt hơn với tư cách là người tạo ra). Chúng ta có thể cân nhắc giảm giá trị này xuống 0 nếu muốn tạo ra nhiều CoinJoin hơn trong thời gian ngắn hơn.
- `cjfee_r` giống như trường trên nhưng tính theo phần trăm chứ không phải giá trị tuyệt đối. Một lần nữa, tôi khuyên bạn nên giữ nguyên giá trị mặc định hoặc giảm giá trị xuống để thu hút nhiều người tham gia hơn.
- `ordertype` với trường này, chúng tôi chọn từ người tạo giá là tính giá tuyệt đối (absoffer) hay tính giá phần trăm (reoffer). Thông thường, người mua thích giá tuyệt đối cho các vấn đề kinh tế.
- `minsize`: Nếu với tư cách là nhà sản xuất, chúng ta không muốn UTXO quá nhỏ, chúng ta có thể chỉ định CoinJoin tối thiểu để tham gia. Trường này được biểu thị bằng Satoshi và hoàn toàn mang tính chủ quan. Chúng ta có thể giữ nguyên trường này ở mức 0 hoặc tăng lên 500000 (Sats), 1000000 (Sats), v.v.



Hãy hết sức cẩn thận để không chỉnh sửa các trường sai, một số biến trong tệp joinmarket.cfg nếu thiết lập không đúng có thể làm ảnh hưởng đến chức năng của phần mềm hoặc phá hủy hoàn toàn quyền riêng tư của bạn, hãy cảnh giác và hết sức thận trọng!



## Thiết lập môi trường làm việc



Một số nút tự động đặt giá trị chính xác cho các trường này trong tệp joinmarket.cfg. Tôi khuyên bạn nên kiểm tra lại theo cách thủ công:





- `rpc_user = yourusername-as-in-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #mặc định thường đúng`
- `rpc_port = 8332 # mặc định cho Mainnet`



Tại thời điểm này, chúng ta có thể tiến hành tạo Wallet trong JoinMarket:



```bash
python wallet-tool.py generate
```



Lệnh này sẽ yêu cầu chúng ta nhập mật khẩu để mã hóa Wallet và tên mà chúng ta muốn đặt cho nó, khi lệnh hỏi bạn có muốn hỗ trợ trái phiếu trung thực hay không, tôi khuyên bạn nên sử dụng tùy chọn _yes_, đầu ra trả về sẽ như thế này:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


Trong trường hợp lỗi xuất hiện, rất có thể chúng tôi đã thiết lập sai 4 trường RPC được chỉ định ở trên. Trong trường hợp đó, việc làm theo [hướng dẫn này](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) có trong tài liệu gốc của JoinMarket có thể hữu ích.



Chúng ta đã hoàn tất việc thiết lập môi trường làm việc và có thể bắt đầu khám phá các lệnh hữu ích nhất. Tất cả các tập lệnh chúng ta sẽ thảo luận có thể được khởi chạy trong bảng điều khiển, sau đó dùng lệnh `--help` để được giải thích chi tiết.



Bây giờ chúng ta có thể thử khởi chạy:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



lệnh này sẽ hiển thị cho bạn tất cả các độ sâu trộn Wallet khác nhau với các địa chỉ khác nhau được phân loại như sau:




- Mới (Address chưa bao giờ được sử dụng)
- Thay đổi (phần còn lại của giao dịch trước đó)
- Cj-out (đầu ra của CoinJoin)



Sau đây là một ví dụ thực tế về kết quả:



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


Bây giờ chúng ta có thể tiến hành gửi những Satoshi đầu tiên của mình vào một hoặc nhiều địa chỉ, lưu ý rằng bất kể là người tạo hay người nhận, phần mềm sẽ không bao giờ hợp nhất UTXO trực tiếp vào các độ sâu trộn khác nhau, theo cách này chúng ta có thể giữ những Satoshi có mức độ riêng tư khác nhau riêng biệt trong Wallet.



## Gửi Bitcoin với CoinJoin Đơn



Bây giờ chúng ta có thể di chuyển Satoshi. Một trong những lệnh chính trong phần mềm này là tập lệnh:



```bash
pyhton sendpayment.py
```


cho phép chúng ta gửi giao dịch đến các địa chỉ khác có hoặc không có CoinJoin. Hãy cùng tìm hiểu cách thức hoạt động và một số ví dụ thực tế. Theo mặc định, định dạng của lệnh là (nhớ thay thế văn bản được bao quanh bởi các ký hiệu < và >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



một ví dụ cơ bản về cách sử dụng có thể là:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


trong trường hợp này, chúng ta sẽ gửi đến Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0,05 Btc tức là 5000000 Satoshi từ mixdepth 0 (mặc định) bằng cách chọn từ 4 đến 9 đối tác cho CoinJoin (tùy chọn mặc định).



Để kiểm soát tốt hơn cách thức và loại UTXO nào sẽ được sử dụng, chúng ta có thể xem xét các tùy chọn bổ sung cho lệnh này:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


Trong ví dụ này, chúng tôi đã thêm hai thông số kỹ thuật: -N cho biết số lượng đối tác chúng tôi sẽ giao dịch, -m cho biết độ sâu giao dịch mà chúng tôi sẽ rút tiền. Trên thực tế, chúng tôi đã gửi 100.000.000 Sats (1 BTC) đến Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c với số tiền ở độ sâu giao dịch 1 và giao dịch với 5 đối tác.



Nếu chúng ta đặt 0 làm giá trị gửi bằng cách chỉ định mixdepth, joinMarket sẽ thực hiện cái gọi là `quét`, nghĩa là nó sẽ gửi tất cả các khoản tiền trong mixdepth đó bằng cách hợp nhất chúng với nhau:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



ở đây chúng tôi đã gửi toàn bộ số tiền từ mixdepth 0 (chúng tôi không thể chỉ định vì đó là mặc định) trộn với 7 khoản tương ứng.



Lệnh sendpayment được sử dụng để chuyển tiền từ joinMarket đến Wallet bên ngoài hoặc gửi Satoshi cho một người bằng cách thêm Layer bảo mật giữa chúng tôi và người đó. Để đạt được mức độ riêng tư cần thiết trên UTXO, tốt hơn nên sử dụng lệnh tumbler.py mà chúng tôi sẽ giải thích sau trong hướng dẫn này.



## Trở thành một nhà sáng tạo



Kịch bản chúng ta sẽ đề cập trong phần này là:



```bash
yg-privacyenhanced.py
```



Chương trình này được sử dụng để hoạt động như một nhà tạo lập (maker) trên joinMarket. Phần mềm sẽ kết nối với nút Bitcoin của chúng tôi và với thị trường nội bộ của nền tảng, nơi các nhà tạo lập tự giới thiệu mình là người đấu giá thanh khoản và người mua tìm kiếm đối tác. Trong trường hợp bạn muốn sử dụng trái phiếu trung thực, bạn có thể tạo một trái phiếu với định dạng sau:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



Ví dụ:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



đầu ra trả về cho chúng tôi sẽ là Bitcoin Address (tức là đầu ra mà bạn sẽ cần gửi số tiền bạn muốn phân bổ cho Fidelity).



**Thận trọng**: Có hai điều bạn cần đặc biệt chú ý nếu muốn tạo Trái phiếu trung thực (hay còn gọi là FB);





- Một khi tiền đã được gửi, chúng sẽ không thể được chuyển đi cho đến khi hết hạn. Hãy chú ý đến số lượng Satss bạn gửi đến Address và cách bạn định dạng ngày tháng. Không được phép có bất kỳ sai sót nào!
- Trái phiếu trung thực có thể dễ dàng nhận dạng trên chuỗi, vì vậy bạn nên gửi tiền thông qua CoinJoin và với nguồn gốc không liên quan đến danh tính của bạn. Bạn cũng nên làm điều tương tự khi muốn chuyển trái phiếu trung thực đã hết hạn ra khỏi JoinMarket.



Điều quan trọng cần nhớ là có thể nạp lại trái phiếu trung thực chỉ bằng một giao dịch, trong trường hợp bội số UTXO thì chỉ giao dịch lớn nhất mới được coi là hợp lệ đối với FB.



Bây giờ chúng ta hãy xử lý tập lệnh được đề cập ở đầu đoạn này, sau khi tạo xong liên kết bảo mật (mà chúng ta nhớ là tùy chọn), chúng ta đã sẵn sàng chạy tệp thực thi để hoạt động như một trình tạo trên joinMarket. Sau khi Satss đã được gửi đến các địa chỉ khác nhau và mixdepth, chúng ta có thể chạy lệnh:



```bash
python yg-privacyenhanced.py <wallet name>
```



Từ thời điểm này trở đi (sau vài phút kết nối mạng) và cho đến khi chúng tôi dừng tập lệnh, ứng dụng JoinMarket của chúng tôi sẽ xuất hiện trong danh sách các maker đang hoạt động trên giao thức và cung cấp thanh khoản cho các đối tác khác nhau để tạo ra CoinJoin. Đừng mong đợi hàng chục CoinJoin mỗi ngày (trừ khi bạn có độ tin cậy cao và thanh khoản lớn được gửi vào Wallet), cũng nên nhớ rằng các yếu tố như phí yêu cầu và số Satoshi được gửi sẽ ảnh hưởng đến tần suất bạn trở thành maker.



Bằng cách chạy lệnh bên dưới, bạn sẽ có thể xem lịch sử của tất cả các giao dịch được thực hiện trên Wallet và bất kỳ khoản lãi (nếu bạn là người tạo) hoặc chi phí phí (nếu bạn là người nhận) mà bạn đã có trong suốt thời gian hoạt động của Wallet.



```bash
python wallet-tool.py <wallet name> history
```



Sau khi Satoshi của bạn tạo CoinJoin, chúng sẽ di chuyển từ mixdepth này sang mixdepth khác cho đến khi đến mixdepth cuối cùng. Sau khi qua mixdepth thứ tư, chúng sẽ trở về mixdepth 0. Bạn có thể tùy ý chọn mức độ riêng tư trước khi di chuyển chúng đến Cold Wallet. Tốt nhất là nên hoàn thành một chu kỳ Wallet đầy đủ.



## Người lật người



Cuối cùng thì chúng ta cũng đến phần hấp dẫn nhất của JoinMarket, chiếc cốc thủy tinh! Nếu bạn đã nghe podcast, chắc hẳn bạn đã biết nội dung chính của nó. Một lời khuyên trước khi bắt đầu: **Hãy cẩn thận với phí!** Hãy nhớ đặt giới hạn trong tệp joinmarket.cfg (như đã giải thích ở phần đầu) và chỉ nên chạy chương trình khi phí onchain tương đối thấp (dưới 10 Sats/vB).



Để khởi chạy tumbler, cần phải dừng tập lệnh từ maker (nếu nó đang hoạt động), sau đó chúng ta có thể chạy lệnh:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Điều cần thiết là phải nhập **ít nhất** 3 địa chỉ đầu ra cho tumbler: điều này nhằm đảm bảo tính riêng tư và không tạo ra các liên kết rõ ràng giữa các UTXO trong suốt quá trình. Như thường lệ, bằng cách thêm `--help` vào lệnh, bạn có thể xem tất cả các chi tiết bổ sung. Hãy cùng xem một ví dụ phức tạp hơn với các quy tắc nâng cao:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



Trong trường hợp này, chúng tôi đã khởi chạy một tập lệnh tumbling không sử dụng số lượng bản sao mặc định (tham số -N cho biết chúng tôi cần 7 bản sao với độ biến thiên tối đa là 2, do đó số lượng nhà sản xuất ngẫu nhiên từ 5 đến 9) và với số lượng CoinJoin lớn hơn trên mỗi mixdepth (theo mặc định, tập lệnh này tạo ra số lượng CoinJoin ngẫu nhiên trên mỗi phần của Wallet trong khoảng từ 1 đến 3, thay vào đó, sử dụng lệnh -c 3 1 sẽ là từ 2 ĐẾN 4). Theo cách này, chúng tôi sẽ tốn nhiều phí Sats hơn nhưng có bộ ẩn danh tốt hơn.



Bạn cũng có thể thêm bao nhiêu địa chỉ đầu ra tùy thích (tối thiểu là 3, không có giới hạn tối đa nào khác ngoài mức độ thông thường). Tuy nhiên, vì lý do riêng tư, không thể quyết định cách phân phối Satoshi giữa các địa chỉ được chỉ định làm đầu ra.



Tumbler là một quá trình dài, đôi khi có thể xảy ra tình trạng ngừng hoạt động, nhưng trong hầu hết các trường hợp, điều này sẽ tự khắc phục trong vòng vài giờ. Trong trường hợp bị sập hoàn toàn, chúng ta có thể thử khởi động lại bằng lệnh:



```bash
python tumbler.py --restart
```



Hoặc chỉ cần khởi động lại một lệnh trộn mới. Thao tác này sẽ không bắt đầu quá trình lên lịch cho lệnh trộn trước đó mà sẽ bắt đầu một chu kỳ trộn mới. Trong trường hợp việc đóng terminal SSH trên node của bạn cũng dừng tập lệnh, bạn có thể sử dụng chương trình `TMUX` có thể được cài đặt bằng lệnh:



```bash
sudo apt install tmux
```



Khởi chạy nó từ shell bằng cách gõ `tmux` sẽ mở một terminal cho bạn, terminal này sẽ vẫn hoạt động ở chế độ nền ngay cả khi bạn đóng kết nối từ xa. Khi bạn kết nối lại với node bằng lệnh: `tmux attach`, shell vẫn đang hoạt động ở chế độ nền sẽ được mở lại.



## Phần kết luận



JoinMarket là một phần mềm vô hạn và có thể tùy chỉnh. Trong hướng dẫn này, chúng tôi đã khám phá các chức năng chính để bất kỳ ai (hoặc ít nhất là tôi đã thử, tôi nhận ra rằng việc sử dụng phần mềm này không hề dễ dàng) đều có thể sử dụng. Một trong những vấn đề lớn nhất của JoinMarket chính là: số lượng người dùng và việc là một nhà sáng tạo. Nếu ít người dùng tận dụng phần mềm này, quyền riêng tư tổng thể (anon-set) sẽ bị giảm sút. Đó là lý do tại sao tôi hy vọng hướng dẫn này sẽ khuyến khích việc sử dụng và thuyết phục bạn tải xuống và cài đặt phần mềm yêu thích của tôi để tạo CoinJoin. Trong trường hợp bạn muốn tìm hiểu sâu hơn về một số khía cạnh, tôi khuyên bạn nên đọc các tài liệu chuyên sâu khác nhau trên GitHub, chúng được viết rất tốt và bạn có thể tìm thấy chúng tại đây.



Chúc các bạn nuôi rùa vui vẻ!🐢 💚



[Tại đây](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) bạn có thể ủng hộ Turtlecute