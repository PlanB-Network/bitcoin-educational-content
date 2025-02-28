---
name: RGB
description: Giới thiệu và tạo tài sản trên RGB
---

![RGB vs Ethereum](assets/0.webp)

## Giới thiệu

Vào ngày 3 tháng 1 năm 2009, Satoshi Nakamoto đã khởi động nút Bitcoin đầu tiên, từ thời điểm đó các nút mới đã tham gia và Bitcoin bắt đầu hoạt động như thể nó là một hình thức sống mới, một hình thức sống không ngừng phát triển, từng bước trở thành mạng lưới an toàn nhất thế giới nhờ vào thiết kế độc đáo, được Satoshi suy nghĩ kỹ lưỡng, thông qua các động cơ kinh tế, nó thu hút người dùng thường được gọi là các thợ mỏ để đầu tư vào năng lượng và sức mạnh tính toán góp phần vào an ninh mạng.

Khi Bitcoin tiếp tục tăng trưởng và được áp dụng rộng rãi, nó đối mặt với vấn đề mở rộng quy mô, mạng lưới Bitcoin cho phép một khối mới với các giao dịch được khai thác trong khoảng thời gian xấp xỉ 10 phút, giả sử chúng ta có 144 khối trong một ngày với giá trị tối đa là 2700 giao dịch mỗi khối, Bitcoin chỉ cho phép khoảng 4.5 giao dịch mỗi giây, Satoshi đã nhận thức được hạn chế này, chúng ta có thể thấy trong một email1 gửi cho Mike Hearn vào tháng 3 năm 2011 nơi ông giải thích cách thức hoạt động của những gì chúng ta ngày nay biết đến là kênh thanh toán. micropayments nhanh chóng và an toàn mà không cần chờ xác nhận. Đây là nơi các giao thức ngoại tuyến xuất hiện.

Theo Christian Decker2, các giao thức ngoại tuyến thường là các hệ thống mà người dùng sử dụng dữ liệu từ một blockchain và quản lý nó mà không chạm vào chính blockchain cho đến phút cuối cùng. Dựa trên khái niệm này, Lightning Network ra đời, một mạng lưới sử dụng các giao thức ngoại tuyến để cho phép thực hiện các thanh toán Bitcoin gần như tức thì và vì không phải tất cả các hoạt động này được ghi lại trên chuỗi khối, nó cho phép hàng nghìn giao dịch mỗi giây và mở rộng quy mô Bitcoin.

Nghiên cứu và phát triển trong lĩnh vực giao thức ngoại tuyến trên Bitcoin đã mở ra một hộp Pandora, ngày nay chúng ta biết rằng chúng ta có thể đạt được nhiều hơn là chuyển giá trị một cách phi tập trung, tổ chức phi lợi nhuận LNP/BP Standards Association tập trung vào phát triển các giao thức tầng 2 và 3 trên Bitcoin và Lightning Network, trong số các dự án này RGB nổi bật.

## RGB là gì?

RGB xuất phát từ nghiên cứu của Peter Todd3 về single-use-seals và client-side-validation, được Giacomo Zucco và cộng đồng đúc kết từ năm 2016-2019 thành một giao thức tài sản tốt hơn cho Bitcoin và mạng Lightning. Sự phát triển tiếp theo của những ý tưởng này đã dẫn đến việc phát triển RGB thành một hệ thống hợp đồng thông minh đầy đủ tính năng do Maxim Orlovsky dẫn dắt việc triển khai kể từ năm 2019 với sự tham gia của cộng đồng.

Chúng ta có thể định nghĩa RGB là một tập hợp các giao thức mã nguồn mở cho phép chúng ta thực hiện các hợp đồng thông minh phức tạp một cách có thể mở rộng và bảo mật. Đó không phải là một mạng lưới cụ thể (như Bitcoin hay Lightning); mỗi hợp đồng thông minh chỉ là một tập hợp các bên tham gia hợp đồng có thể tương tác sử dụng các kênh giao tiếp khác nhau (mặc định là mạng Lightning). RGB sử dụng blockchain Bitcoin như một lớp cam kết trạng thái và duy trì mã của hợp đồng thông minh và dữ liệu ngoại tuyến, điều này làm cho nó có khả năng mở rộng, tận dụng giao dịch Bitcoin (và Script) như một hệ thống kiểm soát quyền sở hữu cho hợp đồng thông minh; trong khi sự phát triển của hợp đồng thông minh được xác định bởi một kế hoạch ngoại tuyến, cuối cùng quan trọng là mọi thứ được xác thực ở phía client.

Nói một cách đơn giản, RGB là một hệ thống cho phép người dùng kiểm tra, thực thi và xác minh một hợp đồng thông minh một cách độc lập bất kỳ lúc nào mà không phát sinh thêm chi phí vì nó không sử dụng blockchain như các hệ thống "truyền thống", hệ thống hợp đồng thông minh phức tạp được Ethereum tiên phong nhưng do yêu cầu người dùng chi trả một lượng lớn gas cho mỗi hoạt động, chúng không bao giờ đạt được khả năng mở rộng mà họ hứa hẹn và do đó không bao giờ là một lựa chọn để ngân hàng cho người dùng bị loại trừ khỏi hệ thống tài chính hiện tại.
Hiện nay, ngành công nghiệp blockchain khuyến khích cả mã của hợp đồng thông minh và dữ liệu phải được lưu trữ trong blockchain và thực thi bởi mỗi nút của mạng, bất kể sự tăng kích thước quá mức hoặc việc sử dụng sai mục đích nguồn lực tính toán. Sơ đồ được đề xuất bởi RGB thông minh và hiệu quả hơn nhiều, vì nó cắt đứt với lý thuyết blockchain bằng cách có hợp đồng thông minh và dữ liệu được tách rời khỏi blockchain và do đó tránh được tình trạng bão hòa của mạng mà các nền tảng khác gặp phải, đồng thời nó không buộc mỗi nút phải thực thi mỗi hợp đồng mà chỉ là các bên liên quan, điều này thêm vào tính bảo mật ở mức độ chưa từng thấy trước đây.
![RGB so với Ethereum](assets/1.webp)

## Hợp đồng thông minh trong RGB

Trong hợp đồng thông minh RGB, nhà phát triển định nghĩa một sơ đồ chỉ ra các quy tắc về cách hợp đồng phát triển theo thời gian. Sơ đồ là tiêu chuẩn cho việc xây dựng hợp đồng thông minh trong RGB, và cả người phát hành khi định nghĩa hợp đồng cho việc phát hành và một ví hoặc sàn giao dịch đều phải tuân thủ một sơ đồ cụ thể mà họ phải xác nhận hợp đồng. Chỉ khi việc xác nhận là chính xác thì mỗi bên có thể chấp nhận yêu cầu và làm việc với tài sản.

Một hợp đồng thông minh trong RGB là một đồ thị hướng không chu trình (DAG) của các thay đổi trạng thái, nơi chỉ một phần của đồ thị luôn được biết đến và không có quyền truy cập vào phần còn lại. Sơ đồ RGB là một bộ quy tắc cốt lõi cho sự phát triển của đồ thị này mà hợp đồng thông minh bắt đầu với. Mỗi bên tham gia hợp đồng có thể thêm vào những quy tắc đó (nếu điều này được cho phép bởi sơ đồ) và đồ thị kết quả được xây dựng từ việc áp dụng lặp đi lặp lại những quy tắc đó.

## Tài sản có thể thay thế

Các tài sản có thể thay thế trong RGB tuân theo quy định LNPBP RGB-20, khi một RGB-20 được định nghĩa, dữ liệu tài sản được biết đến như "dữ liệu genesis" được phân phối qua mạng Lightning, chứa những gì cần thiết để sử dụng tài sản. Hình thức tài sản cơ bản nhất không cho phép phát hành thứ cấp, đốt token, đổi tên hoặc thay thế.

Đôi khi, người phát hành sẽ cần phát hành thêm token trong tương lai, ví dụ như stablecoins như USDT, giữ giá trị của mỗi token liên kết với giá trị của một đồng tiền lạm phát như USD. Để đạt được điều này, các sơ đồ RGB-20 phức tạp hơn tồn tại, và ngoài dữ liệu genesis họ yêu cầu người phát hành sản xuất các lô hàng, sẽ cũng lưu thông trong mạng Lightning; với thông tin này chúng ta có thể biết tổng nguồn cung lưu hành của tài sản. Điều tương tự áp dụng cho việc đốt tài sản, hoặc thay đổi tên của nó.

Thông tin liên quan đến tài sản có thể công khai hoặc riêng tư: nếu người phát hành yêu cầu bảo mật, anh/cô ấy có thể chọn không chia sẻ thông tin về token và thực hiện các hoạt động trong sự riêng tư tuyệt đối, nhưng chúng ta cũng có trường hợp ngược lại trong đó người phát hành và các chủ sở hữu cần quy trình toàn bộ được minh bạch. Điều này được thực hiện bằng cách chia sẻ dữ liệu token.

## Quy trình RGB-20

Quy trình đốt token làm cho token bị vô hiệu, token đã đốt không thể sử dụng nữa.

Quy trình thay thế xảy ra khi token được đốt và một lượng mới của cùng token được tạo ra. Điều này giúp giảm kích thước của dữ liệu lịch sử của tài sản, điều quan trọng để duy trì tốc độ tài sản.

Để hỗ trợ trường hợp sử dụng nơi có thể đốt tài sản mà không cần phải thay thế chúng, một sơ đồ phụ của RGB-20 được sử dụng chỉ cho phép đốt tài sản.

## Tài sản không thể thay thế
Các tài sản không thể thay thế trong RGB tuân theo quy định LNPBP RGB-21, khi chúng ta làm việc với NFTs, chúng ta cũng có một kế hoạch chính và một kế hoạch phụ. Những kế hoạch này có một quy trình khắc, cho phép chúng ta gắn dữ liệu tùy chỉnh bởi phần của chủ sở hữu token, ví dụ phổ biến nhất chúng ta thấy trong NFTs ngày nay là nghệ thuật số liên kết với token. Người phát hành token có thể cấm việc khắc dữ liệu này bằng cách sử dụng kế hoạch phụ RGB-21. Không giống như các hệ thống blockchain NFT khác, RGB cho phép phân phối dữ liệu token phương tiện truyền thông kích thước lớn một cách hoàn toàn phi tập trung và chống kiểm duyệt, sử dụng một phần mở rộng của mạng Lightning P2P gọi là Bifrost, cũng được sử dụng để xây dựng nhiều hình thức khác của chức năng hợp đồng thông minh đặc biệt cho RGB.
Ngoài tài sản có thể thay thế và NFTs, RGB và Bifrost có thể được sử dụng để sản xuất các hình thức hợp đồng thông minh khác, bao gồm DEXes, bể thanh khoản, đồng tiền ổn định thuật toán, v.v., mà chúng tôi sẽ đề cập trong các bài viết tương lai.

## NFT từ RGB so với NFT từ các nền tảng khác

- Không cần lưu trữ blockchain đắt đỏ
- Không cần IPFS, thay vào đó sử dụng một phần mở rộng của mạng Lightning (gọi là Bifrost) (và hoàn toàn mã hóa end-to-end)
- Không cần giải pháp quản lý dữ liệu đặc biệt - một lần nữa, Bifrost đảm nhận vai trò đó
- Không cần phải tin tưởng các trang web để duy trì dữ liệu cho token NFT hoặc về các vấn đề tài sản / hợp đồng ABIs
- Mã hóa DRM tích hợp và quản lý sở hữu
- Cơ sở hạ tầng cho việc sao lưu sử dụng mạng Lightning (Bifrost)
- Các cách để kiếm tiền từ nội dung (không chỉ bán chính NFT, mà còn truy cập vào nội dung, nhiều lần)

## Kết luận

Kể từ khi Bitcoin ra đời, gần 13 năm trước đã có rất nhiều nghiên cứu và thử nghiệm trong lĩnh vực này, cả những thành công và sai lầm đã cho phép chúng ta hiểu thêm một chút về cách thức hệ thống phi tập trung hoạt động trong thực tế, điều gì làm cho chúng thực sự phi tập trung và những hành động nào có xu hướng dẫn chúng đến sự tập trung, tất cả điều này đã dẫn chúng tôi đến kết luận rằng sự phi tập trung thực sự là một hiện tượng hiếm và khó đạt được, sự phi tập trung thực sự chỉ được Bitcoin đạt được và chính vì lý do này mà chúng tôi tập trung nỗ lực xây dựng dựa trên nó.

RGB có hố thỏ riêng của mình trong hố thỏ Bitcoin, trong khi tôi đang rơi xuống qua chúng, tôi sẽ đăng những gì tôi đã học, trong bài viết tiếp theo chúng ta sẽ có một giới thiệu về các nút LNP và RGB và cách sử dụng chúng.

# Hướng dẫn RGB-node

## Giới thiệu

Trong hướng dẫn này, chúng tôi giải thích cách sử dụng RGB-node để tạo một token có thể thay thế và cách chuyển giao nó, tài liệu này dựa trên demo RGB-node và khác biệt ở chỗ hướng dẫn này sử dụng dữ liệu thử nghiệm thực tế và vì thế, chúng ta phải xây dựng Partially Signed Bitcoin Transaction của riêng mình, psbt từ bây giờ.

## Yêu cầu

Khuyến nghị sử dụng một bản phân phối Linux, hướng dẫn này được viết sử dụng Pop!OS, dựa trên Ubuntu và bạn sẽ cần:

- cargo
- Bitcoin core
- git
Lưu ý: Hướng dẫn này chỉ ra việc thực thi các lệnh trong terminal Linux, để phân biệt những gì người dùng nhập và phản hồi mà họ nhận được trong terminal, chúng tôi bao gồm ký hiệu $ tượng trưng cho dấu nhắc bash.
Bạn sẽ cần cài đặt một số phụ thuộc:

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

Xây dựng & Chạy

RGB-node đang trong quá trình phát triển (WIP), đó là lý do tại sao chúng ta phải định vị chính mình tại một commit cụ thể (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) để có thể biên dịch và sử dụng nó một cách chính xác, cho việc này chúng ta thực hiện các lệnh sau.

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

Bây giờ chúng ta biên dịch nó, đừng quên sử dụng cờ --locked vì có một thay đổi lớn được giới thiệu trên một phiên bản của clap.

```
$ cargo install --path . --all-features --locked

....
....
    Finished release [optimized] target(s) in 2m 14s
  Installing /home/user/.cargo/bin/fungibled
  Installing /home/user/.cargo/bin/rgb-cli
  Installing /home/user/.cargo/bin/rgbd
  Installing /home/user/.cargo/bin/stashd
   Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```

Như trình biên dịch rust thông báo cho chúng ta, các tệp nhị phân đã được sao chép vào thư mục $HOME/.cargo/bin, nếu trình biên dịch của bạn sao chép chúng vào một nơi khác bạn phải đảm bảo rằng thư mục đó phải được bao gồm trong $PATH.

Trong số các tệp nhị phân đã cài đặt, chúng ta có thể thấy ba daemons hoặc dịch vụ (các tệp kết thúc bằng d) và một cli (giao diện dòng lệnh), cli cho phép chúng ta tương tác với daemon rgbd chính. Như trong hướng dẫn này chúng ta sẽ chạy hai nút, chúng ta cũng sẽ cần hai khách hàng, mỗi người phải kết nối với nút của riêng mình, cho việc đó chúng ta tạo hai bí danh.

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

Chúng ta có thể chỉ chạy các bí danh hoặc thêm chúng vào cuối tệp $HOME/.bashrc và chạy source $HOME/.bashrc.
Giả định

RGB-node không xử lý bất kỳ chức năng liên quan đến ví tiền nào, nó chỉ thực hiện các nhiệm vụ cụ thể của RGB trên dữ liệu sẽ được cung cấp bởi một ví bên ngoài như bitcoin core. Cụ thể, để minh họa một quy trình làm việc cơ bản với việc phát hành và chuyển giao, chúng ta sẽ cần:

- Một issuance_utxo mà rgb-node-0 sẽ gắn tài sản mới phát hành
- Một receive_utxo nơi rgb-node-1 nhận tài sản
- Một change_utxo nơi rgb-node-0 nhận tài sản thay đổi
- Một giao dịch bitcoin đã ký một phần (tx.psbt), mà khóa công khai đầu ra sẽ được điều chỉnh để bao gồm một cam kết về việc chuyển giao.

Chúng ta sẽ sử dụng bitcoin core cli, chúng ta cần phải có daemon bitcoind đang chạy trên testnet, điều này sẽ mang lại cho chúng ta khả năng tương tác và cuối cùng chúng ta sẽ có thể gửi tài sản của mình cho người dùng RGB khác đã theo dõi hướng dẫn này.
Vì lý do đơn giản, chúng ta sẽ thêm bí danh này vào cuối tệp ~/.bashrc của mình.
```
alias bcli="bitcoin-cli -testnet"
```

Hãy liệt kê các giao dịch đầu ra chưa tiêu của chúng ta và chọn hai cái, một sẽ là issuance_utxo và cái kia là change_utxo, không quan trọng cái nào là cái nào, điều quan trọng là người phát hành có quyền kiểm soát hai UTXO này.

```
$ bcli listunspent
[
  {
    "txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
    "vout": 1,
    "address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
    "label": "",
    "scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
    "amount": 0.01703963,
    "confirmations": 62432,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
    "safe": true
  },
  {
    "txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
    "vout": 1,
    "address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
    "scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
    "amount": 0.02877504,
    "confirmations": 189184,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
    "safe": true
  }
]
```

Trước khi tiếp tục, chúng ta cần phải nói về outpoints, một giao dịch đơn lẻ có thể bao gồm nhiều đầu ra, outpoint bao gồm cả một TXID 32 byte và một số chỉ mục đầu ra 4 byte (vout) để tham chiếu đến đầu ra cụ thể được phân tách bằng dấu hai chấm :. Trong danh sách listunspent của chúng ta, chúng ta có thể tìm thấy hai UTXO, trên mỗi cái chúng ta có thể thấy txid và vout, đó là các outpoint của issuance_utxo và change_utxo của chúng ta.

receive_utxo là một UTXO được kiểm soát bởi người nhận, trong trường hợp này chúng ta sẽ sử dụng e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 là một outpoint từ ví khác.
- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Chúng ta sẽ tạo một giao dịch đã ký một phần (tx.psbt) mà đầu ra sẽ được chỉnh sửa để bao gồm một cam kết chuyển giao, nhớ thay thế txid và vout bằng của bạn, địa chỉ đích không quan trọng, nó có thể là của bạn hoặc của người khác, không quan trọng sats đi đâu, điều quan trọng là chúng ta sử dụng issuance_utxo.

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0
}
```

Đầu ra cho chúng ta một psbt ở dạng mã hóa base64 mà chúng ta sẽ sử dụng để tạo tx.psbt.
```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```

Hãy tạo một thư mục mới có tên là rgbdata trong đó lưu trữ thư mục dữ liệu của từng nút.

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

Sau khi đã ở trong $HOME/rgbdata, chúng ta khởi động mỗi nút trong các terminal khác nhau, nơi ~/.cargo/bin là thư mục mà cargo đã sao chép tất cả các tệp nhị phân sau khi cài đặt rgb-node.

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## Phát Hành

Để phát hành một tài sản, chúng ta chạy rgb0-cli với các subcommands fungible issue, sau đó là các đối số, mã ticker USDT, tên "USD Tether" và trong phần phân bổ, chúng ta sẽ sử dụng số lượng phát hành và issuance_utxo như chúng ta thấy dưới đây:

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

Tài sản đã được phát hành thành công. Sử dụng thông tin này để chia sẻ:
Thông tin tài sản:

```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    amount: 1000
    origin: ~
knownInflation: {}
knownAllocations:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    revealedAmount:
      value: 1000
      blinding: "0000000000000000000000000000000000000000000000000000000000000001"
Chúng tôi nhận được assetId, chúng tôi cần nó để chuyển tài sản.

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

## Tạo UTXO bị che mờ

Để nhận USDT mới, rgb-node-1 cần tạo một UTXO bị che mờ tương ứng với receive_utxo để giữ tài sản.

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```

Để có thể chấp nhận các giao dịch liên quan đến UTXO này, chúng tôi sẽ cần receive_utxo gốc và blinding_factor.

## Chuyển

Để chuyển một số lượng tài sản nào đó cho rgb-node-1, chúng tôi cần gửi nó đến UTXO bị che mờ, rgb-node-0 cần tạo một consignment và một disclosure, và cam kết nó vào một giao dịch bitcoin. Sau đó, chúng tôi sẽ cần một psbt mà chúng tôi sẽ chỉnh sửa để bao gồm cam kết. Ngoài ra, các tùy chọn -i và -a cho phép chúng tôi cung cấp một outpoint đầu vào sẽ là nguồn gốc của tài sản và một phân bổ nơi chúng tôi sẽ nhận thay đổi, chúng tôi phải chỉ định nó theo cách sau @<change_utxo>.
$ rgb0-cli chuyển giao có thể thay thế utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt lô hàng.rgb tiết lộ.rgb chứng từ.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
Chuyển giao thành công, lô hàng và tiết lộ được ghi vào "consignment.rgb" và "disclosure.rgb", giao dịch chứng từ được ký một phần vào "witness.psbt"
Dữ liệu lô hàng để chia sẻ: consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
Điều này sẽ tạo ra ba tệp mới, consignment, disclosure và psbt bao gồm tweak, psbt này được gọi là giao dịch chứng nhận (witness transaction), consignment được gửi đến rgb-node-1.

## Chứng Nhận

Giao dịch chứng nhận cần được ký và phát sóng, để làm điều này, chúng ta cần mã hóa nó trở lại dưới dạng base64.

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

Ký nó với subcommand walletprocesspsbt.
```yaml
bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
```
Dưới đây là bản dịch của đoạn văn bản kỹ thuật bạn yêu cầu:

```json
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",  "complete": true
}
```

Bây giờ, hãy hoàn thiện nó và lấy mã hex.

Lưu ý: Đoạn văn bản bạn cung cấp là một chuỗi mã hóa của một Partially Signed Bitcoin Transaction (PSBT) và không thể "dịch" theo nghĩa truyền thống. Mã hex được yêu cầu ở cuối là một định dạng biểu diễn dữ liệu nhị phân của PSBT, và không liên quan đến quá trình dịch ngôn ngữ. Để "hoàn thiện" và lấy mã hex, bạn cần sử dụng một công cụ hoặc phần mềm hỗ trợ xử lý PSBT, chẳng hạn như Bitcoin Core, Electrum, hoặc các thư viện lập trình như libwally hoặc bitcoinjs-lib.
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}

## Phát sóng

Phát sóng nó bằng cách sử dụng lệnh phụ sendrawtransaction để nó được xác nhận vào blockchain.
## Chấp Nhận

Để chấp nhận việc chuyển giao tài sản, rgb-node-1 cần phải nhận được tệp consignment từ rgb-node-0, có receive_utxo và blinding_factor tương ứng được tạo ra trong quá trình tạo UTXO mù.

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Chuyển giao tài sản đã được chấp nhận thành công.
```

Bây giờ, chúng ta có thể thấy (trong trường knownAllocations) sự phân bổ mới của 100 đơn vị tài sản trong <receive_utxo> bằng cách chạy:

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```yaml
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    amount: 1000
    origin: ~
knownInflation: {}
knownAllocations:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    revealedAmount:
      value: 1000
      blinding: "0000000000000000000000000000000000000000000000000000000000000001"
  - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
    index: 1
    outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
    revealedAmount:
      value: 100
      blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```

Vì receive_utxo đã được làm mờ khi thực hiện chuyển giao, nên người thanh toán rgb-node-0 không có thông tin về nơi 100 USDT đã được gửi, do đó vị trí không được hiển thị trong knownAllocations.

```bash
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  ticker: USDT
  name: USD Tether
  description: ~
  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"

Nhưng như bạn có thể thấy, rgb-node-0 không thể thấy sự thay đổi 900 tài sản mà chúng tôi đã cung cấp cho lệnh chuyển với đối số -a. Để đăng ký sự thay đổi, rgb-node-0 cần chấp nhận việc tiết lộ.

```
$ rgb0-cli fungible enclose disclosure.rgb

Dữ liệu tiết lộ đã được bao đóng thành công.
```

Nếu rgb-node-0 thành công, bạn có thể thấy sự thay đổi bằng cách liệt kê tài sản.

```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
  name: USD Tether
## Mô tả
description: ~  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 0
      outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
      revealedAmount:
        value: 900
        blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2

## Kết luận

Chúng tôi đã có thể tạo ra một tài sản có thể thay thế và chuyển nó từ giao dịch này sang giao dịch khác một cách riêng tư, nếu chúng ta kiểm tra giao dịch đã xác nhận trong một trình duyệt khối, chúng ta sẽ không tìm thấy bất kỳ điều gì khác biệt so với giao dịch thông thường, điều này là nhờ vào việc RGB sử dụng các con dấu sử dụng một lần để điều chỉnh các giao dịch. Trong bài viết này, tôi giới thiệu cách thức hoạt động của RGB.

Bài viết này có thể có lỗi, nếu bạn tìm thấy điều gì đó, vui lòng cho tôi biết để cải thiện hướng dẫn này, các gợi ý và phê bình cũng được chào đón, chúc bạn hack vui vẻ! 🖖