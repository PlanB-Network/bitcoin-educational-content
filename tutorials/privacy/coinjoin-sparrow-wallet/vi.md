---
name: Coinjoin - Sparrow Wallet
description: Làm thế nào để thực hiện một coinjoin trên Sparrow Wallet?
---
![cover](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, công cụ Whirlpool không còn hoạt động, ngay cả đối với những người có Dojo riêng hoặc đang sử dụng Sparrow Wallet. Tuy nhiên, vẫn có khả năng công cụ này có thể được khôi phục trong những tuần tới hoặc được ra mắt lại theo một cách khác. Hơn nữa, phần lý thuyết của bài viết này vẫn còn liên quan để hiểu về nguyên tắc và mục tiêu của coinjoins nói chung (không chỉ Whirlpool), cũng như hiểu về hiệu quả của mô hình Whirlpool.*

_Chúng tôi đang theo dõi sát sao các diễn biến của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này được cung cấp chỉ cho mục đích giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng các công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ các luật lệ trong phạm vi quyền hạn của họ._

---

Trong hướng dẫn này, bạn sẽ học được coinjoin là gì và làm thế nào để thực hiện một coinjoin sử dụng phần mềm Sparrow Wallet và triển khai Whirlpool.

## Coinjoin trên Bitcoin là gì?
**Coinjoin là một kỹ thuật làm gián đoạn khả năng theo dõi bitcoin trên blockchain**. Nó dựa vào một giao dịch hợp tác với cấu trúc cụ thể mang tên giống như vậy: giao dịch coinjoin.

Coinjoins tăng cường sự riêng tư cho người dùng Bitcoin bằng cách làm phức tạp việc phân tích chuỗi cho các quan sát viên bên ngoài. Cấu trúc của chúng cho phép kết hợp nhiều đồng tiền từ các người dùng khác nhau vào một giao dịch duy nhất, do đó làm mờ các dấu vết và khó xác định được liên kết giữa địa chỉ đầu vào và đầu ra.

Nguyên tắc của coinjoin dựa trên một cách tiếp cận hợp tác: một số người dùng muốn trộn bitcoin của họ đặt cùng một số tiền như là đầu vào của cùng một giao dịch. Các số tiền này sau đó được phân phối lại như là đầu ra với giá trị bằng nhau cho mỗi người dùng. Cuối cùng, việc liên kết một đầu ra cụ thể với một người dùng cụ thể tại đầu vào trở nên không thể. Không có liên kết trực tiếp nào giữa các đầu vào và đầu ra, điều này phá vỡ mối liên hệ giữa người dùng và UTXO của họ, cũng như lịch sử của từng đồng tiền.
![coinjoin](assets/notext/1.webp)

Ví dụ về một giao dịch coinjoin (không phải của tôi): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Để thực hiện một coinjoin trong khi đảm bảo rằng mỗi người dùng luôn kiểm soát quỹ của mình, quá trình bắt đầu với việc xây dựng giao dịch bởi một điều phối viên, người sau đó truyền đạt nó cho mỗi người tham gia. Mỗi người dùng sau đó ký vào giao dịch sau khi xác minh rằng nó phù hợp với họ. Tất cả chữ ký thu thập được cuối cùng được tích hợp vào giao dịch. Nếu có nỗ lực chuyển hướng quỹ bởi một người dùng hoặc điều phối viên, thông qua việc sửa đổi đầu ra của giao dịch coinjoin, các chữ ký sẽ trở nên không hợp lệ, dẫn đến việc giao dịch bị các nút từ chối.

Có một số triển khai của coinjoin, như Whirlpool, JoinMarket, hoặc Wabisabi, mỗi cái nhằm mục đích quản lý sự phối hợp giữa các bên tham gia và tăng hiệu quả của giao dịch coinjoin.
Trong hướng dẫn này, chúng ta tập trung vào việc triển khai **Whirlpool**, mà tôi coi là giải pháp hiệu quả nhất để thực hiện coinjoins trên Bitcoin. Mặc dù có sẵn trên một số ví, hướng dẫn này chỉ khám phá việc sử dụng nó với phần mềm Sparrow Wallet Desktop.

## Tại Sao Lại Thực Hiện CoinJoins Trên Bitcoin?

Một trong những vấn đề ban đầu với bất kỳ hệ thống thanh toán ngang hàng nào là double-spending: làm thế nào để ngăn chặn các cá nhân có ý định xấu sử dụng cùng một đơn vị tiền tệ nhiều lần mà không cần đến một cơ quan trung ương để phân xử?

Satoshi Nakamoto đã cung cấp một giải pháp cho bài toán này thông qua giao thức Bitcoin, một hệ thống thanh toán điện tử ngang hàng hoạt động độc lập với bất kỳ cơ quan trung ương nào. Trong bài viết của mình, ông nhấn mạnh rằng cách duy nhất để chứng minh sự vắng mặt của double-spending là đảm bảo tính hiển thị của tất cả các giao dịch trong hệ thống thanh toán.

Để đảm bảo rằng mỗi người tham gia đều biết về các giao dịch, chúng phải được công bố công khai. Do đó, hoạt động của Bitcoin dựa trên một cơ sở hạ tầng minh bạch và phân tán, cho phép bất kỳ người vận hành nút nào cũng có thể xác minh toàn bộ chuỗi chữ ký điện tử và lịch sử của mỗi đồng tiền, từ khi nó được tạo ra bởi một thợ mỏ.

Bản chất minh bạch và phân tán của blockchain Bitcoin có nghĩa là bất kỳ người dùng mạng nào cũng có thể theo dõi và phân tích các giao dịch của tất cả các bên tham gia khác. Do đó, sự ẩn danh ở cấp độ giao dịch là không thể. Tuy nhiên, sự ẩn danh được bảo tồn ở cấp độ nhận dạng cá nhân. Khác với hệ thống ngân hàng truyền thống, nơi mỗi tài khoản được liên kết với một danh tính cá nhân, trên Bitcoin, quỹ được liên kết với các cặp khóa mật mã, do đó cung cấp cho người dùng một hình thức giả danh sau các định danh mật mã.

Do đó, bảo mật trên Bitcoin bị xâm phạm khi các quan sát viên bên ngoài quản lý để liên kết các UTXO cụ thể với người dùng đã được xác định. Một khi mối liên kết này được thiết lập, việc truy vết các giao dịch của họ và phân tích lịch sử của bitcoin của họ trở nên khả thi. Coinjoin chính xác là một kỹ thuật được phát triển để phá vỡ khả năng truy vết của UTXOs, do đó cung cấp một lớp bảo mật nhất định cho người dùng Bitcoin ở cấp độ giao dịch.

## Whirlpool Hoạt Động Như Thế Nào?

Whirlpool nổi bật so với các phương pháp coinjoin khác bằng cách sử dụng giao dịch "_ZeroLink_", đảm bảo rằng không có liên kết kỹ thuật nào có thể xảy ra giữa tất cả các đầu vào và tất cả các đầu ra. Sự trộn lẫn hoàn hảo này được đạt được thông qua một cấu trúc nơi mỗi người tham gia đóng góp một lượng như nhau vào đầu vào (ngoại trừ phí khai thác), do đó tạo ra các đầu ra với số lượng hoàn toàn bằng nhau.

Cách tiếp cận hạn chế này đối với đầu vào mang lại cho các giao dịch coinjoin Whirlpool một đặc điểm độc đáo: sự vắng mặt hoàn toàn của các liên kết xác định giữa các đầu vào và đầu ra. Nói cách khác, mỗi đầu ra có khả năng bằng nhau được gán cho bất kỳ người tham gia nào, so với tất cả các đầu ra khác của giao dịch.
Ban đầu, số lượng người tham gia trong mỗi Whirlpool coinjoin được giới hạn ở 5, với 2 người mới tham gia và 3 người remix (chúng tôi sẽ giải thích các khái niệm này thêm sau). Tuy nhiên, sự tăng của phí giao dịch trên chuỗi quan sát được vào năm 2023 đã thúc đẩy các đội ngũ Samourai tái cân nhắc mô hình của họ để cải thiện quyền riêng tư trong khi giảm chi phí. Do đó, dựa trên tình hình thị trường của phí và số lượng người tham gia, điều phối viên giờ đây có thể tổ chức coinjoins bao gồm 6, 7, hoặc 8 người tham gia. Những phiên tăng cường này được gọi là "_Surge Cycles_". Quan trọng là phải lưu ý rằng, bất kể cài đặt nào, luôn chỉ có 2 người mới tham gia trong các giao dịch Whirlpool coinjoins.

Do đó, các giao dịch Whirlpool được đặc trưng bởi một số lượng đầu vào và đầu ra giống nhau, có thể là:
- 5 đầu vào và 5 đầu ra;
![coinjoin](assets/notext/2.webp)
- 6 đầu vào và 6 đầu ra;
![coinjoin](assets/notext/3.webp)
- 7 đầu vào và 7 đầu ra;
![coinjoin](assets/notext/4.webp)
- 8 đầu vào và 8 đầu ra. ![coinjoin](assets/notext/5.webp)
Mô hình được đề xuất bởi Whirlpool dựa trên các giao dịch coinjoin nhỏ. Khác với Wasabi và JoinMarket, nơi sự mạnh mẽ của các anonsets dựa vào số lượng người tham gia trong một chu kỳ duy nhất, Whirlpool đặt cược vào việc kết nối nhiều chu kỳ nhỏ.

Trong mô hình này, người dùng chỉ phải chịu phí khi họ lần đầu tiên nhập vào một hồ bơi, cho phép họ tham gia vào nhiều lần remix mà không cần phí bổ sung. Những người mới tham gia sẽ chịu phí khai thác cho những người remix.

Với mỗi coinjoin bổ sung mà một đồng tiền tham gia, cùng với các đối tác đã gặp trước đó, các anonsets sẽ tăng lên theo cấp số nhân. Mục tiêu là tận dụng những lần remix miễn phí này, mỗi lần đều góp phần tăng cường mật độ của các anonsets liên quan đến mỗi đồng tiền được trộn.

Whirlpool được thiết kế dựa trên hai yêu cầu quan trọng:
- Khả năng triển khai trên thiết bị di động, vì Samourai Wallet chủ yếu là một ứng dụng dành cho điện thoại thông minh;
- Tốc độ của các chu kỳ remix để thúc đẩy sự tăng lên đáng kể của anonsets.

Những yêu cầu này đã hướng dẫn sự lựa chọn của các nhà phát triển Samourai Wallet trong việc thiết kế Whirlpool, khiến họ hạn chế số lượng người tham gia mỗi chu kỳ. Quá ít người tham gia sẽ làm giảm hiệu quả của coinjoin, giảm đáng kể anonsets được tạo ra với mỗi chu kỳ, trong khi quá nhiều người tham gia sẽ gây ra vấn đề quản lý trên các ứng dụng di động và cản trở dòng chảy của các chu kỳ.

**Cuối cùng, không cần phải có một số lượng lớn người tham gia mỗi coinjoin trên Whirlpool vì anonsets được tạo ra qua việc tích lũy nhiều chu kỳ coinjoin.**
[-> Tìm hiểu thêm về anonsets của Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)
### Các hồ bơi Coinjoin và phí
Để đảm bảo rằng nhiều chu kỳ tăng hiệu quả anonsets của các đồng tiền được trộn, một khung nhất định phải được thiết lập để hạn chế số lượng UTXOs được sử dụng. Whirlpool xác định các hồ bơi khác nhau cho mục đích này.

Một hồ bơi đại diện cho một nhóm người dùng muốn trộn cùng nhau, họ đồng ý về số lượng UTXOs để sử dụng nhằm tối ưu hóa quá trình coinjoin. Mỗi hồ bơi xác định một số lượng cố định cho UTXO, mà người dùng phải tuân thủ để tham gia. Do đó, để thực hiện coinjoins với Whirlpool, bạn cần chọn một hồ bơi. Các hồ bơi hiện có sẵn như sau:
- 0.5 bitcoin;
- 0.05 bitcoin;
- 0.01 bitcoin;
- 0.001 bitcoin (= 100,000 sats).

Bằng cách tham gia vào một hồ bơi với bitcoins của bạn, chúng sẽ được chia để tạo ra UTXOs hoàn toàn đồng nhất với những người tham gia khác trong hồ bơi. Mỗi hồ bơi có một giới hạn tối đa; do đó, đối với các số lượng vượt quá giới hạn này, bạn sẽ buộc phải thực hiện hai lần nhập riêng biệt trong cùng một hồ bơi hoặc chuyển sang một hồ bơi khác với số lượng lớn hơn:

| Hồ bơi (bitcoin) | Số lượng tối đa mỗi lần nhập (bitcoin) |
|------------------|----------------------------------------|
| 0.5              | 35                                     |
| 0.05             | 3.5                                    |
| 0.01             | 0.7                                    |
| 0.001            | 0.025                                  |
Như đã đề cập trước đây, một UTXO được coi là thuộc về một nhóm khi nó sẵn sàng được tích hợp vào một coinjoin. Tuy nhiên, điều này không có nghĩa là người dùng mất quyền sở hữu của nó. **Qua các chu kỳ trộn lẫn, bạn vẫn giữ toàn quyền kiểm soát chìa khóa của mình và do đó, quyền kiểm soát bitcoins của bạn.** Đây là điều phân biệt kỹ thuật coinjoin với các kỹ thuật trộn lẫn tập trung khác.

Để tham gia vào một nhóm coinjoin, phí dịch vụ cũng như phí khai thác phải được thanh toán. Phí dịch vụ được cố định cho mỗi nhóm và nhằm mục đích bồi thường cho các đội ngũ chịu trách nhiệm phát triển và bảo trì Whirlpool. Đối với người dùng Sparrow Wallet, phí này được đội ngũ Samourai chuyển cho các nhà phát triển của Sparrow.

Phí dịch vụ khi sử dụng Whirlpool phải được thanh toán một lần khi nhập nhóm. Một khi bước này hoàn tất, bạn có cơ hội tham gia vào số lượng không giới hạn các lần remix mà không cần phí bổ sung. Dưới đây là phí cố định hiện tại cho mỗi nhóm:

| Nhóm (bitcoin) | Phí Vào (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Những phí này cơ bản như một vé vào cửa cho nhóm được chọn, bất kể số lượng bạn đưa vào coinjoin. Vì vậy, dù bạn tham gia nhóm 0.01 với chính xác 0.01 BTC hay bạn nhập với 0.5 BTC, phí sẽ giữ nguyên về giá trị tuyệt đối.

Trước khi tiến hành coinjoins, người dùng do đó có sự lựa chọn giữa 2 chiến lược:
- Chọn một nhóm nhỏ hơn để giảm thiểu phí dịch vụ, biết rằng họ sẽ nhận lại nhiều UTXO nhỏ;
- Hoặc ưu tiên một nhóm lớn hơn, đồng ý trả phí cao hơn để kết thúc với số lượng UTXO giá trị lớn hơn ít hơn.

Nói chung, việc gộp nhiều UTXO đã trộn sau các chu kỳ coinjoin không được khuyến khích, vì điều này có thể làm mất đi tính bảo mật đã đạt được, đặc biệt là do Heuristic Sở Hữu Đầu Vào Chung (CIOH). Do đó, có thể sẽ khôn ngoan hơn khi chọn một nhóm lớn hơn, ngay cả khi điều này có nghĩa là phải trả nhiều hơn, để tránh có quá nhiều UTXO giá trị nhỏ ở đầu ra. Người dùng phải cân nhắc những sự đánh đổi này để chọn nhóm họ ưa thích.

Ngoài phí dịch vụ, phí khai thác điển hình cho bất kỳ giao dịch Bitcoin nào cũng cần được xem xét. Là một người dùng Whirlpool, bạn sẽ phải trả phí khai thác cho giao dịch chuẩn bị (`Tx0`) cũng như cho coinjoin đầu tiên. Tất cả các lần remix tiếp theo sẽ miễn phí, nhờ vào mô hình của Whirlpool dựa trên việc thanh toán của người mới tham gia.

Thực tế, trong mỗi coinjoin Whirlpool, hai người dùng trong số các đầu vào là người mới tham gia. Các đầu vào khác đến từ những người remix. Kết quả là, phí khai thác cho tất cả các bên tham gia trong giao dịch được trả bởi hai người tham gia mới này, những người sau đó cũng sẽ được hưởng các lần remix miễn phí:
![coinjoin](assets/en/6.webp)
Nhờ vào hệ thống phí này, Whirlpool thực sự khác biệt so với các dịch vụ coinjoin khác vì anonsets của UTXOs không tỷ lệ với giá trả bởi người dùng. Do đó, có thể đạt được mức độ ẩn danh đáng kể cao chỉ bằng cách trả phí vào cửa của nhóm và phí khai thác cho hai giao dịch (cả `Tx0` và hỗn hợp ban đầu).
Quan trọng cần lưu ý rằng người dùng cũng sẽ phải chịu phí đào để rút UTXOs của họ khỏi hồ sau khi hoàn thành nhiều lần coinjoin, trừ khi họ đã chọn tùy chọn `mix to`, điều này sẽ được thảo luận trong hướng dẫn dưới đây.
### Các tài khoản ví HD được sử dụng bởi Whirlpool
Để thực hiện coinjoin qua Whirlpool, ví cần phải tạo ra nhiều tài khoản riêng biệt. Một tài khoản, trong bối cảnh của một ví HD (Hierarchical Deterministic), tạo thành một phần hoàn toàn tách biệt với các phần khác, sự tách biệt này xảy ra ở mức độ thứ ba của hệ thống phân cấp của ví, tức là, ở mức của `xpub`.
Một ví HD lý thuyết có thể tạo ra đến `2^(32/2)` tài khoản khác nhau. Tài khoản ban đầu, được sử dụng mặc định trên tất cả các ví Bitcoin, tương ứng với chỉ mục `0'`.

Đối với các ví được điều chỉnh cho Whirlpool, như Samourai hoặc Sparrow, 4 tài khoản được sử dụng để đáp ứng nhu cầu của quá trình coinjoin:
- Tài khoản **deposit**, được xác định bởi chỉ mục `0'`;
- Tài khoản **bad bank** (hoặc doxxic change), được xác định bởi chỉ mục `2 147 483 644'`;
- Tài khoản **premix**, được xác định bởi chỉ mục `2 147 483 645'`;
- Tài khoản **postmix**, được xác định bởi chỉ mục `2 147 483 646'`.

Mỗi tài khoản này đều thực hiện một chức năng cụ thể trong coinjoin.

Tất cả các tài khoản này đều được liên kết với một hạt giống duy nhất, cho phép người dùng khôi phục quyền truy cập vào tất cả bitcoin của họ bằng cách sử dụng cụm từ khôi phục và, nếu có, cụm từ mật khẩu của họ. Tuy nhiên, cần phải chỉ định cho phần mềm, trong quá trình khôi phục này, các chỉ mục tài khoản đã được sử dụng.

Bây giờ, hãy xem xét các giai đoạn khác nhau của một Whirlpool coinjoin trong các tài khoản này.

### Các giai đoạn khác nhau của coinjoins trên Whirlpool
**Giai đoạn 1: Tx0**
Điểm khởi đầu của bất kỳ Whirlpool coinjoin nào là tài khoản **deposit**. Đây là tài khoản bạn tự động sử dụng khi bạn tạo một ví Bitcoin mới. Tài khoản này phải được nạp với bitcoin mà bạn muốn trộn.

`Tx0` đại diện cho giai đoạn đầu tiên của quá trình trộn Whirlpool. Mục tiêu là chuẩn bị và cân bằng UTXOs cho coinjoin, bằng cách chia chúng thành các đơn vị tương ứng với số lượng của hồ được chọn, nhằm đảm bảo sự đồng nhất của việc trộn. Các UTXOs được cân bằng sau đó được gửi đến tài khoản **premix**. Còn sự khác biệt không thể nhập vào hồ được tách ra thành một tài khoản cụ thể: **bad bank** (hoặc "doxxic change").

Giao dịch ban đầu `Tx0` cũng phục vụ để thanh toán phí dịch vụ cho người điều phối trộn. Khác với các giai đoạn tiếp theo, giao dịch này không phải là cộng tác; người dùng do đó phải chịu toàn bộ phí đào:
![coinjoin](assets/en/7.webp)
Trong ví dụ này của giao dịch `Tx0`, một đầu vào `372,000 sats` từ tài khoản **deposit** của chúng tôi được chia thành nhiều UTXOs đầu ra, được phân bổ như sau:
- Một lượng `5,000 sats` dành cho người điều phối về phí dịch vụ, tương ứng với việc nhập vào hồ của `100,000 sats`;
- Ba UTXOs được chuẩn bị cho việc trộn, chuyển hướng đến tài khoản **premix** của chúng tôi và đăng ký với người điều phối. Các UTXOs này được cân bằng ở mức `108,000 sats` mỗi cái, nhằm mục đích chi trả phí đào cho lần trộn ban đầu của chúng;
- Số dư thừa, không thể nhập vào hồ bơi vì quá nhỏ, được coi là thay đổi độc hại. Nó được gửi đến tài khoản cụ thể của nó. Tại đây, thay đổi này lên đến `40,000 sats`;
- Cuối cùng, có `3,000 sats` không tạo thành một đầu ra, nhưng là phí khai thác cần thiết để xác nhận `Tx0`.

Ví dụ, đây là một Tx0 Whirlpool thực tế (không phải từ tôi): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Bước 2: Thay Đổi Độc Hại**
Số dư thừa, không thể hòa nhập vào hồ bơi, tương đương với `40,000 sats`, được chuyển hướng đến tài khoản **ngân hàng xấu**, còn được gọi là "thay đổi độc hại", để đảm bảo sự tách biệt nghiêm ngặt từ các UTXO khác trong ví.

UTXO này nguy hiểm cho quyền riêng tư của người dùng vì không chỉ luôn gắn liền với quá khứ của nó, và do đó có thể với danh tính của chủ sở hữu, mà ngoài ra, nó được ghi nhận là thuộc về một người dùng đã thực hiện coinjoin.

Nếu UTXO này được hợp nhất với các đầu ra đã trộn, những đầu ra này sẽ mất tất cả quyền riêng tư đã đạt được trong các chu kỳ coinjoin, đặc biệt là do CIOH (*Common-Input-Ownership-Heuristic*). Nếu nó được hợp nhất với các thay đổi độc hại khác, người dùng có nguy cơ mất quyền riêng tư vì điều này sẽ liên kết các mục nhập khác nhau của các chu kỳ coinjoin. Do đó, nó phải được xử lý một cách cẩn thận. Cách quản lý UTXO độc hại này sẽ được chi tiết trong phần cuối của bài viết này, và các hướng dẫn tương lai sẽ đi sâu hơn vào các phương pháp này trên Mạng PlanB.

**Bước 3: Hỗn Hợp Ban Đầu**
Sau khi hoàn thành `Tx0`, các UTXO đã được cân bằng được gửi đến tài khoản **premix** của ví chúng tôi, sẵn sàng được giới thiệu vào chu kỳ coinjoin đầu tiên của chúng, còn được gọi là "hỗn hợp ban đầu". Nếu, như trong ví dụ của chúng tôi, `Tx0` tạo ra nhiều UTXO dành cho việc trộn, mỗi UTXO sẽ được tích hợp vào một coinjoin ban đầu riêng biệt.
Sau những hỗn hợp ban đầu này, tài khoản **premix** sẽ trống, trong khi tiền xu của chúng tôi, sau khi đã trả phí khai thác cho coinjoin đầu tiên này, sẽ được điều chỉnh chính xác theo số lượng được xác định bởi hồ bơi đã chọn. Trong ví dụ của chúng tôi, UTXO ban đầu của chúng tôi là `108 000 sats` sẽ được giảm xuống chính xác còn `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Bước 4: Các Lần Remix**
Sau hỗn hợp ban đầu, các UTXO được chuyển đến tài khoản **postmix**. Tài khoản này tập hợp các UTXO đã được trộn và những UTXO đang chờ được remix. Khi khách hàng Whirlpool hoạt động, các UTXO nằm trong tài khoản **postmix** sẽ tự động có sẵn cho việc remix và sẽ được chọn ngẫu nhiên để tham gia vào các chu kỳ mới.

Như một lời nhắc nhở, các lần remix sau đó là 100% miễn phí: không yêu cầu thêm phí dịch vụ hoặc phí khai thác. Giữ các UTXO trong tài khoản **postmix** do đó giữ nguyên giá trị của chúng, và đồng thời cải thiện anonsets của chúng. Đó là lý do tại sao việc cho phép những đồng tiền này tham gia vào nhiều chu kỳ coinjoin là quan trọng. Điều này không tốn của bạn bất cứ điều gì, và nó tăng cấp độ ẩn danh của chúng.
Khi bạn quyết định chi tiêu các UTXO đã được trộn lẫn, bạn có thể thực hiện trực tiếp từ tài khoản **postmix** này. Được khuyến nghị giữ các UTXO đã trộn trong tài khoản này để hưởng lợi từ việc remix miễn phí và ngăn chúng rời khỏi chu trình Whirlpool, điều này có thể làm giảm quyền riêng tư của chúng.
Như chúng ta sẽ thấy trong hướng dẫn sau, còn có tùy chọn `mix to` cho phép tự động gửi các đồng tiền đã trộn của bạn đến một ví khác, chẳng hạn như một ví lạnh, sau một số lượng coinjoin đã xác định.

Sau khi thảo luận về lý thuyết, hãy cùng nhau thực hành với hướng dẫn sử dụng Whirlpool qua phần mềm Sparrow Wallet cho máy tính!

## Hướng dẫn: Coinjoin Whirlpool trên Sparrow Wallet
Có nhiều lựa chọn để sử dụng Whirlpool. Lựa chọn đầu tiên tôi muốn giới thiệu cho bạn là tùy chọn Sparrow Wallet, một phần mềm quản lý ví Bitcoin mã nguồn mở cho PC.
Sử dụng Sparrow có ưu điểm là khá dễ bắt đầu, nhanh chóng thiết lập, và không yêu cầu thiết bị nào khác ngoài máy tính và kết nối internet. Tuy nhiên, có một nhược điểm đáng chú ý: coinjoins chỉ xảy ra khi Sparrow được khởi chạy và kết nối. Điều này có nghĩa là nếu bạn muốn trộn và remix bitcoins của mình 24/7, bạn sẽ cần phải liên tục giữ máy tính của mình bật.

### Cài đặt Sparrow Wallet
Để bắt đầu, bạn rõ ràng cần phần mềm Sparrow Wallet. Bạn có thể trực tiếp tải xuống từ [trang web chính thức](https://sparrowwallet.com/download/) hoặc trên [GitHub của họ](https://github.com/sparrowwallet/sparrow/releases).

Trước khi cài đặt phần mềm, việc xác minh chữ ký và tính toàn vẹn của tệp thực thi bạn vừa tải xuống sẽ rất quan trọng. Nếu bạn muốn biết thêm chi tiết về quy trình cài đặt và xác minh phần mềm Sparrow, tôi khuyên bạn nên đọc hướng dẫn khác này: *[Hướng dẫn Sparrow Wallet](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)*

### Tạo một Ví Phần mềm
Sau khi cài đặt phần mềm, bạn sẽ cần tiến hành tạo một ví Bitcoin. Quan trọng cần lưu ý rằng để tham gia vào coinjoins, việc sử dụng một ví phần mềm (còn gọi là "ví nóng") là cần thiết. Do đó, **sẽ không thể thực hiện coinjoins với một ví được bảo mật bởi một ví cứng**.

Mặc dù không bắt buộc, trong trường hợp bạn dự định trộn một lượng lớn, rất được khuyến khích sử dụng một cụm mật khẩu BIP39 mạnh cho ví này.

Để tạo một ví mới, mở Sparrow, sau đó nhấp vào tab `File` và `New Wallet`.

![sparrow](assets/notext/9.webp)

Chọn một tên cho ví này, ví dụ: "Ví Coinjoin". Nhấp vào nút `Create Wallet`.

![sparrow](assets/notext/10.webp)

Giữ nguyên cài đặt mặc định, sau đó nhấp vào nút `New or Imported Software Wallet`.

![sparrow](assets/notext/11.webp)

Khi bạn truy cập vào cửa sổ tạo ví, tôi khuyên bạn nên chọn một chuỗi 12 từ, vì nó là hoàn toàn đủ. Chọn `Generate New` để tạo một cụm từ khôi phục mới, và nhấp vào `Use Passphrase` nếu bạn muốn thêm một cụm mật khẩu BIP39. Rất quan trọng phải sao lưu thông tin khôi phục của bạn bằng vật lý, dù là trên giấy hay trên một hỗ trợ kim loại, để đảm bảo an toàn cho bitcoins của bạn.

![sparrow](assets/notext/12.webp)
Đảm bảo tính hợp lệ của sao lưu cụm từ khôi phục của bạn trước khi nhấp vào `Confirm Backup...`. Sparrow sau đó sẽ yêu cầu bạn nhập lại cụm từ của mình để xác minh rằng bạn đã ghi chú nó. Sau khi hoàn thành bước này, tiếp tục bằng cách nhấp vào `Create Keystore`.
![sparrow](assets/notext/13.webp)
Để đường dẫn phái sinh được đề xuất mặc định và nhấn `Import Keystore`. Trong ví dụ của tôi, đường dẫn phái sinh có sự khác biệt nhỏ vì tôi đang sử dụng Testnet cho hướng dẫn này. Đường dẫn phái sinh xuất hiện cho bạn sẽ như sau:
```plaintext
m/84'/0'/0'
```

![sparrow](assets/notext/14.webp)

Sau đó, Sparrow sẽ hiển thị chi tiết phái sinh của ví mới của bạn. Trong trường hợp bạn đã thiết lập một cụm từ bí mật, bạn nên ghi chú lại `Master fingerprint` của mình. Mặc dù dấu vân tay khóa chính này không phải là dữ liệu nhạy cảm, nó sẽ hữu ích cho bạn để sau này xác minh rằng bạn thực sự đang truy cập vào ví đúng và để xác nhận không có lỗi khi nhập cụm từ bí mật của bạn.

Nhấn vào nút `Apply`.

![sparrow](assets/notext/15.webp)

Sparrow mời bạn tạo một mật khẩu cho ví của mình. Mật khẩu này sẽ được yêu cầu để truy cập vào nó qua phần mềm Sparrow Wallet. Chọn một mật khẩu mạnh, sao lưu nó, và sau đó nhấn vào `Set Password`.

![sparrow](assets/notext/16.webp)

### Nhận bitcoins
Sau khi tạo ví, ban đầu bạn sẽ có một tài khoản duy nhất, với chỉ số `0'`. Đây là tài khoản **gửi tiền** mà chúng tôi đã nói về trong các phần trước. Đây là tài khoản mà bạn sẽ cần gửi bitcoins vào để trộn.

Để làm điều này, chọn tab `Receive` ở phía bên trái của cửa sổ. Sparrow sẽ tự động tạo một địa chỉ mới trống để nhận bitcoins.

![sparrow](assets/notext/17.webp)

Bạn có thể nhập một nhãn cho địa chỉ này, và sau đó gửi bitcoins cần trộn vào đó.

![sparrow](assets/notext/18.webp)

### Thực hiện Tx0
Một khi giao dịch của bạn được xác nhận, bạn có thể chuyển đến tab `UTXOs`.

![sparrow](assets/notext/19.webp)

Tiếp theo, chọn UTXO(s) mà bạn muốn gửi vào chu kỳ coinjoin. Để chọn nhiều UTXO cùng một lúc, giữ phím `Ctrl` trong khi nhấp vào các UTXO bạn chọn.

![sparrow](assets/notext/20.webp)

Sau đó nhấn vào nút `Mix Selected` ở phía dưới cửa sổ. Nếu nút này không xuất hiện trên giao diện của bạn, đó là vì bạn đang sử dụng ví được bảo mật bằng ví cứng. Bạn cần sử dụng ví phần mềm để thực hiện coinjoins với Sparrow.
![sparrow](assets/notext/21.webp)
Một cửa sổ mở ra để giải thích cách Whirlpool hoạt động. Đây là sự đơn giản hóa của những gì tôi đã giải thích trong các phần trước. Nhấn vào `Next` để tiếp tục.

![sparrow](assets/notext/22.webp)

Trên trang tiếp theo, bạn có thể nhập một "SCODE" nếu bạn có. Một SCODE là một mã khuyến mãi cung cấp giảm giá cho phí dịch vụ của hồ bơi. Samourai Wallet thỉnh thoảng cung cấp những mã như vậy cho người dùng của mình trong các sự kiện đặc biệt. Tôi khuyên bạn nên [theo dõi Samourai Wallet](https://twitter.com/SamouraiWallet) trên mạng xã hội để không bỏ lỡ các SCODE trong tương lai.
Trên cùng một trang, bạn cũng cần thiết lập mức phí cho `Tx0` và lần trộn đầu tiên của bạn. Lựa chọn này sẽ ảnh hưởng đến tốc độ xác nhận cho giao dịch chuẩn bị và lần coinjoin đầu tiên của bạn. Hãy nhớ rằng bạn chịu trách nhiệm về phí khai thác cho `Tx0` và lần trộn ban đầu, nhưng bạn sẽ không phải trả phí khai thác cho các lần trộn lại sau đó. Điều chỉnh thanh trượt `Premix Priority` theo sở thích của bạn, sau đó nhấp vào `Next`.
![sparrow](assets/notext/23.webp)

Trong cửa sổ mới này, bạn sẽ có tùy chọn chọn hồ bơi mà bạn muốn tham gia sử dụng danh sách thả xuống. Trong trường hợp của tôi, sau khi ban đầu chọn một UTXO của `456 214 sats`, lựa chọn duy nhất của tôi là hồ bơi `100 000 sats`. Giao diện này cũng thông báo cho bạn về phí dịch vụ cần phải trả cũng như số lượng UTXOs sẽ được tích hợp vào hồ bơi. Nếu điều kiện dường như thỏa đáng với bạn, tiếp tục bằng cách nhấp vào `Preview Premix`.

![sparrow](assets/notext/24.webp)

Sau bước này, Sparrow sẽ yêu cầu bạn nhập mật khẩu cho ví của bạn, cái mà bạn đã thiết lập khi tạo nó trên phần mềm. Một khi mật khẩu được nhập, bạn sẽ truy cập vào bản xem trước của `Tx0` của mình. Ở phía bên trái cửa sổ của bạn, bạn sẽ thấy Sparrow đã tạo ra các tài khoản cần thiết để sử dụng Whirlpool (`Deposit`, `Premix`, `Postmix`, và `Badbank`). Bạn cũng sẽ có cơ hội xem cấu trúc của `Tx0` của mình, với các đầu ra khác nhau:
- Phí dịch vụ;
- Các UTXOs được cân bằng dự định nhập vào hồ bơi;
- Sự thay đổi độc hại (Doxxic Change).

![sparrow](assets/notext/25.webp)

Nếu giao dịch phù hợp với bạn, nhấp vào `Broadcast Transaction` để phát sóng `Tx0` của bạn. Nếu không, bạn có tùy chọn điều chỉnh các tham số của `Tx0` này bằng cách chọn `Clear` để xóa dữ liệu đã nhập và bắt đầu quá trình tạo từ đầu.

### Thực hiện Coinjoins
Một khi Tx0 được phát sóng, bạn sẽ tìm thấy UTXOs của mình sẵn sàng để được trộn trong tài khoản `Premix`.
![sparrow](assets/notext/26.webp)

Một khi `Tx0` được xác nhận, UTXOs của bạn sẽ được đăng ký với điều phối viên, và các lần trộn ban đầu sẽ tự động bắt đầu liên tiếp.

![sparrow](assets/notext/27.webp)

Bằng cách kiểm tra tài khoản `Postmix`, bạn sẽ quan sát thấy UTXOs kết quả từ các lần trộn ban đầu. Những đồng tiền này sẽ sẵn sàng cho các lần trộn lại sau đó, mà không phát sinh thêm phí.

![sparrow](assets/notext/28.webp)

Trong cột `Mixes`, có thể thấy số lượng coinjoins được thực hiện bởi mỗi đồng tiền của bạn. Như chúng ta sẽ thấy trong các phần sau, điều quan trọng thực sự không chỉ là số lượng remixes mà là các anonsets liên quan, mặc dù hai chỉ số này có mối liên hệ một phần.

![sparrow](assets/notext/29.webp)

Để tạm thời dừng việc trộn coin, chỉ cần nhấp vào `Stop Mixing`. Bạn sẽ có tùy chọn tiếp tục hoạt động bất cứ lúc nào bằng cách chọn `Start Mixing`.

![sparrow](assets/notext/30.webp)
Để đảm bảo khả năng sẵn có liên tục của UTXOs của bạn cho việc remixing, cần thiết phải giữ phần mềm Sparrow hoạt động. Đóng phần mềm hoặc tắt máy tính sẽ tạm dừng các coinjoins. Một giải pháp để khắc phục vấn đề này là vô hiệu hóa chức năng ngủ qua cài đặt hệ điều hành của bạn. Ngoài ra, Sparrow cung cấp một tùy chọn để ngăn máy tính tự động chuyển sang chế độ ngủ, bạn có thể tìm thấy dưới tab `Công cụ` với tiêu đề `Ngăn Máy Tính Ngủ`.

![sparrow](assets/notext/31.webp)

### Hoàn thành các coinjoins
Để chi tiêu bitcoins đã trộn của bạn, bạn có một số lựa chọn. Phương pháp trực tiếp nhất là truy cập vào tài khoản `Postmix` và chọn tab `Gửi`.

![sparrow](assets/notext/32.webp)

Trong phần này, bạn sẽ có tùy chọn nhập địa chỉ đích, số tiền gửi, và phí giao dịch, giống như cho bất kỳ giao dịch nào khác được thực hiện với Sparrow Wallet. Nếu bạn muốn, bạn cũng có thể tận dụng các tính năng bảo mật nâng cao như Stonewall, bằng cách nhấp vào nút `Bảo mật`.

![sparrow](assets/notext/33.webp)

[-> Tìm hiểu thêm về giao dịch Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Nếu bạn muốn chọn một cách chính xác hơn các đồng xu của mình để chi tiêu, hãy chuyển đến tab `UTXOs`. Chọn các UTXOs mà bạn muốn tiêu thụ cụ thể, sau đó nhấn nút `Gửi Đã Chọn` để khởi tạo giao dịch.

![sparrow](assets/notext/34.webp)
Cuối cùng, tùy chọn `Chuyển đến...` có sẵn trên Sparrow cho phép tự động loại bỏ một UTXO đã chọn khỏi các chu kỳ coinjoin, mà không phát sinh thêm phí. Tính năng này cho phép xác định số lần remix sau đó UTXO sẽ không được tái tích hợp vào tài khoản `Postmix` của bạn, mà thay vào đó sẽ được chuyển trực tiếp đến một ví khác. Tùy chọn này thường được sử dụng để tự động gửi bitcoins đã trộn đến một ví lạnh.
Để sử dụng tùy chọn này, bắt đầu bằng cách mở ví nhận cùng với ví coinjoin của bạn trong phần mềm Sparrow.

![sparrow](assets/notext/35.webp)

Sau đó, chuyển đến tab `UTXOs`, và chọn các đồng xu mà bạn quan tâm, sau đó nhấp vào nút `Chuyển đến...` ở phía dưới cửa sổ.

![sparrow](assets/notext/36.webp)

Một cửa sổ mở ra, bắt đầu bằng cách chọn ví đích từ danh sách thả xuống.

![sparrow](assets/notext/37.webp)

Chọn ngưỡng coinjoin mà sau đó việc rút tiền sẽ được thực hiện tự động. Tôi không thể đưa ra một số lượng chính xác các lần remix để thực hiện, vì điều này thay đổi tùy theo tình hình cá nhân và mục tiêu bảo mật của bạn, nhưng tránh chọn một ngưỡng quá thấp. Tôi khuyên bạn nên tham khảo bài viết khác này để tìm hiểu thêm về quá trình remixing: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)

Bạn có thể để tùy chọn `Phạm vi Chỉ số` ở giá trị mặc định, `Toàn bộ`. Chức năng này cho phép trộn đồng thời từ các khách hàng khác nhau, nhưng đó không phải là điều chúng ta muốn làm trong hướng dẫn này. Để hoàn tất và kích hoạt tùy chọn `Chuyển đến...`, nhấn `Khởi động lại Whirlpool`.

![sparrow](assets/notext/38.webp)

Tuy nhiên, hãy cẩn thận khi sử dụng tùy chọn `Chuyển đến`, vì việc loại bỏ các đồng xu đã trộn khỏi tài khoản `Postmix` của bạn có thể làm tăng đáng kể nguy cơ xâm phạm quyền riêng tư của bạn. Các lý do cho khả năng này được chi tiết trong các phần tiếp theo.

## Làm thế nào để biết chất lượng của các chu kỳ coinjoin của chúng ta?
Để một coinjoin thực sự hiệu quả, điều cần thiết là nó phải thể hiện sự đồng nhất tốt giữa các lượng input và output. Sự đồng nhất này làm tăng số lượng giải thích có thể có trong mắt của một quan sát viên bên ngoài, do đó tăng sự không chắc chắn xung quanh giao dịch. Để định lượng sự không chắc chắn này được tạo ra bởi một coinjoin, người ta có thể sử dụng cách tính entropy của giao dịch. Để khám phá sâu hơn về các chỉ số này, tôi giới thiệu bạn đọc hướng dẫn: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Mô hình Whirlpool được công nhận là mô hình mang lại sự đồng nhất nhiều nhất trong coinjoins. Tiếp theo, hiệu suất của nhiều chu kỳ coinjoin được đánh giá dựa trên kích thước của các nhóm mà một đồng tiền được ẩn giấu. Kích thước của các nhóm này định nghĩa cái gọi là anonsets. Có hai loại anonsets: loại đầu tiên đánh giá sự riêng tư đạt được chống lại phân tích hồi tưởng (từ hiện tại về quá khứ) và loại thứ hai, chống lại phân tích tiềm năng (từ quá khứ đến hiện tại). Để giải thích chi tiết về hai chỉ số này, tôi mời bạn tham khảo hướng dẫn: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

## Làm thế nào để quản lý postmix?
Sau khi thực hiện các chu kỳ coinjoin, chiến lược tốt nhất là giữ các UTXO của bạn trong tài khoản **postmix**, chờ đợi sử dụng trong tương lai của chúng. Thậm chí còn được khuyến khích để cho chúng remix vô thời hạn cho đến khi bạn cần tiêu chúng.

Một số người dùng có thể xem xét chuyển các bitcoin đã trộn của họ vào một ví được bảo vệ bởi một ví cứng. Điều này là khả thi, nhưng quan trọng là phải tuân theo các khuyến nghị của Samourai Wallet một cách cẩn thận để không làm tổn hại đến sự riêng tư đã đạt được.

Việc hợp nhất UTXO là lỗi thường gặp nhất. Cần tránh kết hợp các UTXO đã trộn với các UTXO chưa trộn trong cùng một giao dịch, để tránh CIOH (*Common-Input-Ownership-Heuristic*). Điều này đòi hỏi quản lý cẩn thận các UTXO của bạn trong ví, đặc biệt là về việc gắn nhãn. Ngoài coinjoin, việc hợp nhất UTXO nói chung là một thực hành xấu thường dẫn đến mất riêng tư khi không được quản lý đúng cách.

Cũng quan trọng là phải cẩn thận khi hợp nhất các UTXO đã trộn với nhau. Việc hợp nhất vừa phải là có thể xem xét nếu các UTXO đã trộn của bạn có anonsets đáng kể, nhưng điều này sẽ không tránh khỏi làm giảm bảo mật của các đồng tiền của bạn. Đảm bảo rằng việc hợp nhất không quá lớn hoặc được thực hiện sau một số lượng remix không đủ, vì điều này có nguy cơ thiết lập các liên kết có thể suy luận giữa các UTXO của bạn trước và sau các chu kỳ coinjoin. Trong trường hợp nghi ngờ về những thao tác này, thực hành tốt nhất là không hợp nhất các UTXO postmix, và chuyển chúng từng cái một vào ví cứng của bạn, tạo một địa chỉ trống mới mỗi lần. Một lần nữa, nhớ gắn nhãn đúng cách cho mỗi UTXO nhận được.
Cũng được khuyến cáo không chuyển các UTXO postmix của bạn vào một ví sử dụng các kịch bản không phổ biến. Ví dụ, nếu bạn nhập Whirlpool từ một ví multisig sử dụng kịch bản `P2WSH`, có ít cơ hội bạn sẽ được trộn với các người dùng khác có cùng loại ví ban đầu. Nếu bạn rút các postmix của mình về cùng một ví multisig đó, mức độ riêng tư của các bitcoin đã trộn của bạn sẽ bị giảm đáng kể. Ngoài kịch bản, có nhiều dấu vân tay ví khác có thể làm bạn nhầm lẫn.
Như với bất kỳ giao dịch Bitcoin nào, cũng quan trọng là không sử dụng lại các địa chỉ nhận. Mỗi giao dịch mới nên được nhận trên một địa chỉ trống mới.
Giải pháp đơn giản và an toàn nhất là để các UTXO đã trộn của bạn nghỉ ngơi trong tài khoản **postmix** của mình, cho phép chúng tái trộn và chỉ chạm vào chúng khi cần chi tiêu. Ví Samourai và Sparrow có thêm các biện pháp bảo vệ chống lại tất cả các rủi ro liên quan đến phân tích chuỗi. Những biện pháp bảo vệ này giúp bạn tránh mắc lỗi.

## Làm thế nào để quản lý sự thay đổi độc hại?
Tiếp theo, bạn cần phải cẩn thận trong việc quản lý sự thay đổi độc hại, sự thay đổi không thể nhập vào hồ coinjoin. Những UTXO độc hại này, kết quả từ việc sử dụng Whirlpool, đặt ra rủi ro cho quyền riêng tư của bạn vì chúng thiết lập một liên kết giữa bạn và việc sử dụng coinjoin. Do đó, việc xử lý chúng cẩn thận và không kết hợp chúng với các UTXO khác, đặc biệt là UTXO đã trộn, là điều cần thiết. Dưới đây là các chiến lược khác nhau để xem xét sử dụng chúng:
- **Trộn chúng trong các hồ nhỏ hơn:** Nếu UTXO độc hại của bạn đủ lớn để nhập vào một hồ nhỏ một mình, hãy xem xét trộn nó. Đây thường là lựa chọn tốt nhất. Tuy nhiên, điều quan trọng là không kết hợp nhiều UTXO độc hại để truy cập một hồ, vì điều này có thể liên kết các mục nhập khác nhau của bạn;
- **Đánh dấu chúng là "không thể chi tiêu":** Một cách tiếp cận khác là không sử dụng chúng nữa, đánh dấu chúng là "không thể chi tiêu" trong tài khoản dành riêng của chúng và chỉ Hodl. Điều này đảm bảo bạn không vô tình chi tiêu chúng. Nếu giá trị của bitcoin tăng, các hồ mới phù hợp hơn với UTXO độc hại của bạn có thể xuất hiện;
- **Làm từ thiện:** Xem xét làm từ thiện, ngay cả những khoản nhỏ, cho các nhà phát triển làm việc trên Bitcoin và phần mềm liên quan. Bạn cũng có thể quyên góp cho các tổ chức chấp nhận BTC. Nếu việc quản lý UTXO độc hại của bạn có vẻ quá phức tạp, bạn có thể đơn giản loại bỏ chúng bằng cách làm từ thiện;
- **Mua Thẻ Quà Tặng:** Các nền tảng như [Bitrefill](https://www.bitrefill.com/) cho phép bạn đổi bitcoin lấy thẻ quà tặng có thể sử dụng tại các nhà bán lẻ khác nhau. Đây có thể là cách để loại bỏ UTXO độc hại của bạn mà không mất giá trị liên quan.
- **Tổng hợp chúng trên Monero:** Ví Samourai hiện cung cấp dịch vụ hoán đổi nguyên tử giữa BTC và XMR. Đây là lý tưởng để quản lý UTXO độc hại bằng cách tổng hợp chúng trên Monero, không làm ảnh hưởng đến quyền riêng tư của bạn qua CIOH, trước khi gửi chúng trở lại Bitcoin. Tuy nhiên, lựa chọn này có thể tốn kém về phí khai thác và phí bổ sung do hạn chế về thanh khoản.
- **Gửi chúng đến Lightning Network:** Chuyển những UTXO này đến Lightning Network để hưởng lợi từ phí giao dịch giảm là một lựa chọn có thể thú vị. Tuy nhiên, phương pháp này có thể tiết lộ thông tin nhất định tùy thuộc vào cách sử dụng Lightning của bạn và do đó nên được thực hành một cách cẩn thận.

Các hướng dẫn chi tiết về việc thực hiện những kỹ thuật khác nhau này sẽ sớm được cung cấp trên PlanB Network.

**Tài Nguyên Bổ Sung:**
[Hướng dẫn Video Ví Sparrow](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)
[Hướng dẫn Video Ví Samourai](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)
- [Tài liệu Ví Samourai - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Chuỗi Tweet về CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Bài đăng Blog về CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).