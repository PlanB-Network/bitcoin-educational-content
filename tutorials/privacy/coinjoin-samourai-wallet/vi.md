---
name: Coinjoin - Ví Samourai
description: Làm thế nào để thực hiện một coinjoin trên Ví Samourai?
---
![cover](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Ví Samourai và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, công cụ Whirlpool không còn hoạt động, ngay cả đối với những người có Dojo riêng hoặc đang sử dụng Ví Sparrow. Tuy nhiên, vẫn có khả năng công cụ này có thể được khôi phục trong những tuần tới hoặc được ra mắt lại theo một cách khác. Hơn nữa, phần lý thuyết của bài viết này vẫn còn liên quan để hiểu về nguyên tắc và mục tiêu của coinjoins nói chung (không chỉ Whirlpool), cũng như hiểu về hiệu quả của mô hình Whirlpool.*

_Chúng tôi đang ch closely theo dõi sự phát triển của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này được cung cấp chỉ cho mục đích giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng những công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ các luật lệ trong phạm vi quyền hạn của họ._

---

"*một ví bitcoin cho cuộc sống hàng ngày*"

Trong hướng dẫn này, bạn sẽ học được coinjoin là gì và cách thực hiện một coinjoin sử dụng phần mềm Ví Samourai và triển khai Whirlpool.

## Coinjoin trên Bitcoin là gì?
**Coinjoin là một kỹ thuật làm giảm khả năng theo dõi bitcoin trên blockchain**. Nó dựa vào một giao dịch hợp tác với một cấu trúc cụ thể có tên là giao dịch coinjoin.

Coinjoins tăng cường sự riêng tư cho người dùng Bitcoin bằng cách làm phức tạp việc phân tích chuỗi cho những người quan sát bên ngoài. Cấu trúc của chúng cho phép kết hợp nhiều đồng tiền từ các người dùng khác nhau vào một giao dịch duy nhất, do đó làm mờ các dấu vết và khó xác định được liên kết giữa các địa chỉ đầu vào và đầu ra.

Nguyên tắc của coinjoin dựa trên một cách tiếp cận hợp tác: một số người dùng muốn trộn bitcoin của họ đặt cùng một số tiền như đầu vào của cùng một giao dịch. Những số tiền này sau đó được phân phối lại như các đầu ra có giá trị bằng nhau cho mỗi người dùng. Kết thúc giao dịch, trở nên không thể liên kết một đầu ra cụ thể với một người dùng đã biết ở đầu vào. Không có liên kết trực tiếp nào giữa các đầu vào và đầu ra, phá vỡ mối liên hệ giữa người dùng và UTXO của họ, cũng như lịch sử của mỗi đồng tiền.
![coinjoin](assets/notext/1.webp)

Ví dụ về một giao dịch coinjoin (không phải của tôi): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Để thực hiện một coinjoin trong khi đảm bảo rằng mỗi người dùng luôn kiểm soát quỹ của mình, quá trình bắt đầu với việc xây dựng giao dịch bởi một điều phối viên, người sau đó truyền đạt nó cho các bên tham gia. Mỗi người dùng sau đó ký vào giao dịch sau khi xác minh rằng nó phù hợp với họ. Tất cả chữ ký thu thập được cuối cùng được tích hợp vào giao dịch. Nếu có nỗ lực chuyển hướng quỹ bởi một người dùng hoặc điều phối viên, bằng cách sửa đổi các đầu ra của giao dịch coinjoin, các chữ ký sẽ chứng minh là không hợp lệ, dẫn đến việc từ chối giao dịch bởi các nút.

Có một số triển khai của coinjoin, như Whirlpool, JoinMarket, hoặc Wabisabi, mỗi cái nhằm mục đích quản lý sự điều phối giữa các bên tham gia và tăng hiệu quả của các giao dịch coinjoin.
Trong hướng dẫn này, chúng ta sẽ tìm hiểu về việc triển khai **Whirlpool**, mà tôi coi là giải pháp hiệu quả nhất để thực hiện coinjoins trên Bitcoin. Mặc dù có sẵn trên một số ví, trong hướng dẫn này, chúng ta sẽ chỉ khám phá việc sử dụng nó với ứng dụng di động Samourai Wallet, không kể đến Dojo.
## Tại sao lại thực hiện coinjoins trên Bitcoin?
Một trong những vấn đề ban đầu với bất kỳ hệ thống thanh toán ngang hàng nào là việc chi tiêu gấp đôi: làm thế nào để ngăn chặn các cá nhân có ý định xấu chi tiêu cùng một đơn vị tiền tệ nhiều lần mà không cần đến một cơ quan trung ương để phân xử?

Satoshi Nakamoto đã cung cấp một giải pháp cho bài toán này thông qua giao thức Bitcoin, một hệ thống thanh toán điện tử ngang hàng hoạt động độc lập với bất kỳ cơ quan trung ương nào. Trong bài viết của mình, ông nhấn mạnh rằng cách duy nhất để chứng minh sự vắng mặt của việc chi tiêu gấp đôi là đảm bảo tính hiển thị của tất cả các giao dịch trong hệ thống thanh toán.

Để đảm bảo rằng mỗi người tham gia đều biết về các giao dịch, chúng phải được công bố công khai. Do đó, hoạt động của Bitcoin dựa trên một cơ sở hạ tầng minh bạch và phân tán, cho phép bất kỳ người vận hành nút nào cũng có thể xác minh toàn bộ chuỗi chữ ký điện tử và lịch sử của mỗi đồng tiền, từ khi nó được tạo ra bởi một thợ mỏ.

Bản chất minh bạch và phân tán của blockchain Bitcoin có nghĩa là bất kỳ người dùng mạng nào cũng có thể theo dõi và phân tích các giao dịch của tất cả các bên tham gia khác. Kết quả là, sự ẩn danh ở cấp độ giao dịch là không thể. Tuy nhiên, sự ẩn danh được bảo toàn ở cấp độ nhận dạng cá nhân. Khác với hệ thống ngân hàng truyền thống, nơi mỗi tài khoản được liên kết với một danh tính cá nhân, trên Bitcoin, quỹ được liên kết với các cặp khóa mật mã, do đó cung cấp cho người dùng một hình thức giả danh sau các định danh mật mã.

Do đó, tính bảo mật trên Bitcoin bị xâm phạm khi các quan sát viên bên ngoài quản lý để liên kết các UTXO cụ thể với người dùng đã được xác định. Một khi mối liên kết này được thiết lập, việc truy vết các giao dịch của họ và phân tích lịch sử của bitcoin của họ trở nên khả thi. Coinjoin chính xác là một kỹ thuật được phát triển để phá vỡ khả năng truy vết của UTXOs, do đó cung cấp một lớp bảo mật nhất định cho người dùng Bitcoin ở cấp độ giao dịch.

## Whirlpool hoạt động như thế nào?
Whirlpool nổi bật so với các phương pháp coinjoin khác bằng cách sử dụng giao dịch "_ZeroLink_", đảm bảo rằng không có liên kết kỹ thuật nào có thể xảy ra giữa tất cả các đầu vào và tất cả các đầu ra. Sự pha trộn hoàn hảo này được đạt được thông qua một cấu trúc nơi mỗi người tham gia đóng góp một lượng như nhau vào đầu vào (ngoại trừ phí khai thác), do đó tạo ra các đầu ra với số lượng hoàn toàn bằng nhau.
Cách tiếp cận hạn chế này đối với đầu vào mang lại cho các giao dịch coinjoin Whirlpool một đặc điểm độc đáo: sự vắng mặt hoàn toàn của các liên kết xác định giữa đầu vào và đầu ra. Nói cách khác, mỗi đầu ra có khả năng bằng nhau được gán cho bất kỳ người tham gia nào, so với tất cả các đầu ra khác trong giao dịch.
Ban đầu, số lượng người tham gia trong mỗi Whirlpool coinjoin được giới hạn ở 5, với 2 người mới tham gia và 3 người remix (chúng tôi sẽ giải thích các khái niệm này thêm sau). Tuy nhiên, sự tăng của phí giao dịch trên chuỗi quan sát được vào năm 2023 đã thúc đẩy các đội ngũ của Samourai tái cấu trúc mô hình của họ để cải thiện quyền riêng tư trong khi giảm chi phí. Do đó, dựa trên tình hình thị trường của phí và số lượng người tham gia, điều phối viên giờ đây có thể tổ chức các coinjoins bao gồm 6, 7, hoặc 8 người tham gia. Những phiên tăng cường này được gọi là "_Surge Cycles_". Quan trọng là phải lưu ý rằng, bất kể cấu hình như thế nào, luôn chỉ có 2 người mới tham gia trong các coinjoin Whirlpool.

Do đó, các giao dịch Whirlpool được đặc trưng bởi một số lượng đầu vào và đầu ra giống nhau, có thể là:
- 5 đầu vào và 5 đầu ra;
![coinjoin](assets/notext/2.webp)
- 6 đầu vào và 6 đầu ra;
![coinjoin](assets/notext/3.webp)
- 7 đầu vào và 7 đầu ra;
![coinjoin](assets/notext/4.webp) - 8 đầu vào và 8 đầu ra.
![coinjoin](assets/notext/5.webp)
Mô hình được đề xuất bởi Whirlpool dựa trên các giao dịch coinjoin nhỏ. Khác với Wasabi và JoinMarket, nơi mà độ bền của các nhóm ẩn danh dựa vào số lượng người tham gia trong một chu kỳ duy nhất, Whirlpool đặt cược vào việc kết nối nhiều chu kỳ nhỏ.

Trong mô hình này, người dùng chỉ phải trả phí khi họ lần đầu tiên nhập vào một hồ bơi, cho phép họ tham gia vào nhiều lần remix mà không cần phí bổ sung. Những người mới tham gia sẽ trả phí khai thác cho những người remix trước.

Với mỗi lần coinjoin thêm vào mà một đồng tiền tham gia, cùng với các đối tác đã gặp trong quá khứ, các nhóm ẩn danh sẽ tăng lên theo cấp số nhân. Mục tiêu do đó là tận dụng những lần remix miễn phí này, mỗi lần đều góp phần tăng cường mật độ của các nhóm ẩn danh liên kết với mỗi đồng tiền được trộn.

Whirlpool được thiết kế dựa trên hai yêu cầu quan trọng:
- Khả năng triển khai trên thiết bị di động, vì Samourai Wallet chủ yếu là một ứng dụng dành cho điện thoại thông minh;
- Tốc độ của các chu kỳ remix để thúc đẩy sự tăng lên đáng kể của các nhóm ẩn danh.
Những yêu cầu này đã hướng dẫn các nhà phát triển của Samourai Wallet trong việc thiết kế Whirlpool, khiến họ hạn chế số lượng người tham gia mỗi chu kỳ. Quá ít người tham gia sẽ làm giảm hiệu quả của coinjoin, giảm đáng kể các nhóm ẩn danh được tạo ra mỗi chu kỳ, trong khi quá nhiều người tham gia sẽ gây ra vấn đề quản lý trên các ứng dụng di động và cản trở dòng chảy của các chu kỳ.
**Cuối cùng, không cần phải có một số lượng lớn người tham gia mỗi coinjoin trên Whirlpool vì các nhóm ẩn danh được đạt được thông qua việc tích lũy nhiều chu kỳ coinjoin.**

[-> Tìm hiểu thêm về các nhóm ẩn danh của Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Các hồ bơi và phí coinjoin
Để những chu kỳ nhiều lần này có thể tăng hiệu quả các nhóm ẩn danh của các đồng tiền được trộn, một khuôn khổ nhất định phải được thiết lập để hạn chế số lượng UTXO được sử dụng. Whirlpool do đó xác định các hồ bơi khác nhau.

Một hồ bơi đại diện cho một nhóm người dùng muốn trộn cùng nhau, họ đồng ý về số lượng UTXO sử dụng để tối ưu hóa quá trình coinjoin. Mỗi hồ bơi quy định một số lượng cố định cho UTXO, mà người dùng phải tuân thủ để tham gia. Do đó, để thực hiện coinjoins với Whirlpool, bạn cần chọn một hồ bơi. Các hồ bơi hiện có sẵn như sau:
- 0.5 bitcoins;
- 0.05 bitcoin;
- 0.01 bitcoin;
- 0.001 bitcoin (= 100,000 sats).

Khi tham gia vào một hồ bơi với bitcoins của bạn, chúng sẽ được chia để tạo ra UTXOs hoàn toàn đồng nhất với những người tham gia khác trong hồ bơi. Mỗi hồ bơi có một giới hạn tối đa; do đó, đối với các số lượng vượt quá giới hạn này, bạn sẽ buộc phải thực hiện hai lần nhập riêng biệt trong cùng một hồ bơi hoặc hướng đến một hồ bơi khác với số lượng lớn hơn:

| Hồ bơi (bitcoin) | Số lượng tối đa mỗi lần nhập (bitcoin) |
|------------------|----------------------------------------|
| 0.5              | 35                                     |
| 0.05             | 3.5                                    |
| 0.01             | 0.7                                    |
| 0.001            | 0.025                                  |
Như đã đề cập trước đây, một UTXO được coi là thuộc về một nhóm khi nó sẵn sàng được tích hợp vào một coinjoin. Tuy nhiên, điều này không có nghĩa là người dùng mất quyền sở hữu của nó. **Qua các chu kỳ trộn khác nhau, bạn vẫn giữ quyền kiểm soát đầy đủ các khóa của mình và do đó, cả bitcoin của bạn.** Đây là điều phân biệt kỹ thuật coinjoin với các kỹ thuật trộn tập trung khác.

Để tham gia vào một nhóm coinjoin, phí dịch vụ cũng như phí khai thác phải được thanh toán. Phí dịch vụ được cố định cho mỗi nhóm và nhằm mục đích bù đắp cho các đội ngũ chịu trách nhiệm phát triển và bảo trì Whirlpool.

Phí dịch vụ khi sử dụng Whirlpool chỉ phải trả một lần khi nhập vào nhóm. Sau bước này, bạn có cơ hội tham gia vào số lượng không giới hạn các lần remix mà không phải trả thêm phí nào. Dưới đây là các phí cố định hiện tại cho mỗi nhóm:

| Nhóm (bitcoin) | Phí Vào (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Những phí này cơ bản hoạt động như một vé vào cho nhóm được chọn, bất kể số lượng bạn đưa vào coinjoin. Do đó, dù bạn tham gia nhóm 0.01 với chính xác 0.01 BTC hay nhập vào với 0.5 BTC, phí sẽ giữ nguyên giá trị tuyệt đối.

Trước khi tiến hành coinjoins, người dùng có sự lựa chọn giữa 2 chiến lược:
- Chọn một nhóm nhỏ hơn để giảm thiểu phí dịch vụ, biết rằng họ sẽ nhận lại nhiều UTXO nhỏ;
- Hoặc ưu tiên một nhóm lớn hơn, đồng ý trả phí cao hơn để kết thúc với số lượng UTXO ít hơn nhưng giá trị lớn hơn.

Nói chung, việc hợp nhất nhiều UTXO đã trộn sau các chu kỳ coinjoin không được khuyến khích, vì điều này có thể làm mất đi tính bảo mật đã đạt được, đặc biệt là do Heuristic Sở Hữu Đầu Vào Chung (CIOH). Do đó, có thể sẽ khôn ngoan khi chọn một nhóm lớn hơn, ngay cả khi phải trả nhiều hơn, để tránh có quá nhiều UTXO giá trị nhỏ ở đầu ra. Người dùng phải cân nhắc những sự đánh đổi này để chọn nhóm họ ưa thích.

Ngoài phí dịch vụ, phí khai thác điển hình cho bất kỳ giao dịch Bitcoin nào cũng cần được xem xét. Là một người dùng Whirlpool, bạn sẽ phải trả phí khai thác cho giao dịch chuẩn bị (`Tx0`) cũng như cho coinjoin đầu tiên. Tất cả các lần remix tiếp theo sẽ miễn phí, nhờ vào mô hình của Whirlpool dựa trên việc thanh toán của người mới tham gia.

Thực tế, trong mỗi coinjoin Whirlpool, hai người dùng trong số các đầu vào là người mới tham gia. Các đầu vào khác đến từ những người remix. Kết quả là, phí khai thác cho tất cả các bên tham gia trong giao dịch được trả bởi hai người tham gia mới này, những người sau đó cũng sẽ được hưởng các lần remix miễn phí:
![coinjoin](assets/en/6.webp)
Nhờ vào hệ thống phí này, Whirlpool thực sự khác biệt so với các dịch vụ coinjoin khác vì anonsets của các UTXO không tỷ lệ với giá trả bởi người dùng. Do đó, có thể đạt được mức độ ẩn danh đáng kể cao chỉ bằng cách trả phí nhập hồ của nhóm và phí khai thác cho hai giao dịch (cả `Tx0` và hỗn hợp ban đầu).
Quan trọng cần lưu ý rằng người dùng cũng sẽ phải chịu phí đào để rút UTXO của họ khỏi bể sau khi hoàn thành nhiều lần coinjoin, trừ khi họ đã chọn tùy chọn `mix to`, điều này sẽ được thảo luận trong hướng dẫn dưới đây.
### Các tài khoản ví HD được sử dụng bởi Whirlpool
Để thực hiện coinjoin qua Whirlpool, ví cần phải tạo ra nhiều tài khoản riêng biệt. Một tài khoản, trong bối cảnh của một ví HD (*Hierarchical Deterministic*), tạo thành một phần hoàn toàn tách biệt với các phần khác, sự tách biệt này xảy ra ở mức độ thứ ba của hệ thống phân cấp của ví, tức là, ở mức của `xpub`.

Một ví HD lý thuyết có thể tạo ra tới `2^(32/2)` tài khoản khác nhau. Tài khoản ban đầu, được sử dụng mặc định trên tất cả các ví Bitcoin, tương ứng với chỉ mục `0'`.

Đối với các ví được điều chỉnh cho Whirlpool, như Samourai hoặc Sparrow, 4 tài khoản được sử dụng để đáp ứng nhu cầu của quá trình coinjoin:
- Tài khoản **deposit**, được xác định bởi chỉ mục `0'`;
- Tài khoản **bad bank** (hoặc doxxic change), được xác định bởi chỉ mục `2 147 483 644'`;
- Tài khoản **premix**, được xác định bởi chỉ mục `2 147 483 645'`;
- Tài khoản **postmix**, được xác định bởi chỉ mục `2 147 483 646'`.

Mỗi tài khoản này đều thực hiện một chức năng cụ thể trong quá trình coinjoin.

Tất cả các tài khoản này đều được liên kết với một hạt giống duy nhất, cho phép người dùng khôi phục quyền truy cập vào tất cả bitcoin của họ sử dụng cụm từ khôi phục và, nếu có, cụm từ bí mật của họ. Tuy nhiên, cần phải chỉ định cho phần mềm, trong quá trình khôi phục này, các chỉ mục tài khoản đã được sử dụng.

Bây giờ, hãy xem các giai đoạn khác nhau của một Whirlpool coinjoin trong những tài khoản này.

### Các giai đoạn khác nhau của coinjoins trên Whirlpool
**Giai đoạn 1: Tx0**
Điểm bắt đầu của bất kỳ Whirlpool coinjoin nào là tài khoản **deposit**. Đây là tài khoản bạn tự động sử dụng khi bạn tạo một ví Bitcoin mới. Tài khoản này phải được nạp với bitcoin mà người ta muốn trộn.
`Tx0` đại diện cho bước đầu tiên trong quá trình trộn Whirlpool. Mục tiêu là chuẩn bị và cân bằng UTXO cho coinjoin, bằng cách chia chúng thành các đơn vị tương ứng với số lượng của bể được chọn, để đảm bảo sự đồng nhất của việc trộn. Các UTXO được cân bằng sau đó được gửi đến tài khoản **premix**. Còn sự khác biệt không thể nhập vào bể được tách ra thành một tài khoản cụ thể: **bad bank** (hoặc "doxxic change").
Giao dịch ban đầu `Tx0` này cũng phục vụ để thanh toán phí dịch vụ cho người điều phối trộn. Khác với các bước tiếp theo, giao dịch này không phải là cộng tác; người dùng do đó phải chịu tất cả phí đào:
![coinjoin](assets/en/7.webp)

Trong ví dụ này của giao dịch `Tx0`, một đầu vào `372,000 sats` từ tài khoản **deposit** của chúng tôi được chia thành nhiều UTXO đầu ra, được phân bổ như sau:
- Một lượng `5,000 sats` dành cho người điều phối về phí dịch vụ, tương ứng với việc nhập vào bể của `100,000 sats`;
- Ba UTXO được chuẩn bị cho việc trộn, chuyển hướng đến tài khoản **premix** của chúng tôi và đăng ký với người điều phối. Các UTXO này được cân bằng ở mức `108,000 sats` mỗi cái, để trang trải phí đào cho lần trộn ban đầu của chúng;
- Số dư thừa không thể nhập vào hồ bơi, do quá nhỏ, được coi là thay đổi độc hại. Nó được gửi đến tài khoản cụ thể của nó. Tại đây, lượng thay đổi này lên đến `40,000 sats`;
- Cuối cùng, có `3,000 sats` không tạo thành một đầu ra, nhưng là phí khai thác cần thiết để xác nhận `Tx0`.

Ví dụ, đây là một Whirlpool Tx0 thực tế (không phải từ tôi): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Bước 2: Thay đổi độc hại**
Số dư thừa không thể được tích hợp vào hồ bơi, tương đương với `40,000 sats`, được chuyển hướng đến tài khoản **ngân hàng xấu**, còn được gọi là "thay đổi độc hại", để đảm bảo sự tách biệt nghiêm ngặt từ các UTXO khác trong ví.

UTXO này nguy hiểm cho quyền riêng tư của người dùng, vì không chỉ nó vẫn gắn liền với quá khứ của mình, và do đó có thể với danh tính của chủ sở hữu, mà nó còn được ghi nhận là thuộc về một người dùng đã thực hiện coinjoin.
Nếu UTXO này được hợp nhất với các đầu ra đã trộn, họ sẽ mất tất cả sự bảo mật đã đạt được trong các chu kỳ coinjoin, đặc biệt là do Heuristic Sở Hữu Đầu Vào Chung (CIOH). Nếu nó được hợp nhất với các thay đổi độc hại khác, người dùng có nguy cơ mất bảo mật vì điều này sẽ liên kết các đầu vào khác nhau của các chu kỳ coinjoin. Do đó, nó phải được xử lý cẩn thận. Cách quản lý UTXO độc hại này sẽ được chi tiết trong phần cuối của bài viết này, và các hướng dẫn tương lai sẽ đề cập sâu hơn về các phương pháp này trên Mạng PlanB.

**Bước 3: Hỗn Hợp Ban Đầu**
Sau khi `Tx0` hoàn thành, các UTXO được cân bằng sẽ được gửi đến tài khoản **premix** của ví chúng tôi, sẵn sàng được giới thiệu vào chu kỳ coinjoin đầu tiên của họ, còn được gọi là "hỗn hợp ban đầu". Nếu, như trong ví dụ của chúng tôi, `Tx0` tạo ra nhiều UTXO để trộn, mỗi UTXO sẽ được tích hợp vào một coinjoin ban đầu riêng biệt.

Sau những hỗn hợp đầu tiên này, tài khoản **premix** sẽ trống, trong khi số tiền của chúng tôi, sau khi đã trả phí khai thác cho coinjoin đầu tiên này, sẽ được điều chỉnh chính xác theo số lượng được xác định bởi hồ bơi đã chọn. Trong ví dụ của chúng tôi, UTXO ban đầu của chúng tôi `108 000 sats` sẽ được giảm xuống chính xác còn `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Bước 4: Các Lần Trộn Lại**
Sau hỗn hợp ban đầu, các UTXO được chuyển đến tài khoản **postmix**. Tài khoản này tập hợp các UTXO đã được trộn và những UTXO đang chờ được trộn lại. Khi khách hàng Whirlpool hoạt động, các UTXO trong tài khoản **postmix** sẽ tự động có sẵn để trộn lại và sẽ được chọn ngẫu nhiên để tham gia vào các chu kỳ mới.

Như một lời nhắc nhở, các lần trộn lại sau đó là miễn phí 100%: không yêu cầu thêm phí dịch vụ hay phí khai thác. Giữ các UTXO trong tài khoản **postmix** do đó giữ nguyên giá trị của chúng và đồng thời cải thiện các anonsets của họ. Đó là lý do tại sao việc cho phép những đồng tiền này tham gia vào nhiều chu kỳ coinjoin là quan trọng. Nó không tốn của bạn bất cứ điều gì, và nó tăng cấp độ ẩn danh của họ.
Khi bạn quyết định chi tiêu các UTXO hỗn hợp, bạn có thể làm điều đó trực tiếp từ tài khoản **postmix** này. Được khuyến nghị giữ các UTXO đã hỗn hợp trong tài khoản này để hưởng lợi từ việc remix miễn phí và tránh chúng rời khỏi chu trình Whirlpool, điều này có thể giảm bảo mật của chúng.
Như chúng ta sẽ thấy trong hướng dẫn sau, cũng có tùy chọn `mix to` cho phép tự động gửi tiền đã hỗn hợp của bạn đến một ví khác, như ví lạnh, sau một số lần coinjoin nhất định.
Sau khi đã nắm vững lý thuyết, chúng ta hãy bắt đầu thực hành với hướng dẫn sử dụng Whirlpool qua ứng dụng Samourai Wallet trên Android!
## Hướng dẫn: Coinjoin Whirlpool trên Samourai Wallet
Có nhiều lựa chọn để sử dụng Whirlpool. Lựa chọn mà tôi muốn giới thiệu ở đây là tùy chọn Samourai Wallet (không có Dojo), một ứng dụng quản lý ví Bitcoin mã nguồn mở trên Android.

Việc hỗn hợp trên Samourai mà không cần Dojo có ưu điểm là khá dễ sử dụng, nhanh chóng thiết lập, và không cần thiết bị khác ngoài điện thoại Android và kết nối internet.

Tuy nhiên, phương pháp này có hai nhược điểm đáng chú ý:
- Coinjoins chỉ xảy ra khi Samourai đang chạy ở chế độ nền và được kết nối. Điều này có nghĩa là nếu bạn muốn hỗn hợp và remix bitcoin của mình 24/7, bạn phải luôn giữ Samourai được bật;
- Nếu bạn sử dụng Whirlpool với Samourai Wallet mà không kết nối với Dojo của riêng mình, thì ứng dụng của bạn sẽ phải kết nối với máy chủ được duy trì bởi các đội ngũ Samourai, và bạn sẽ tiết lộ `xpub` của ví cho họ. Những thông tin ẩn danh này là cần thiết để ứng dụng của bạn tìm thấy các giao dịch của mình.

Giải pháp lý tưởng để vượt qua những hạn chế này là vận hành Dojo của riêng bạn kết hợp với một thể hiện Whirlpool CLI trên node Bitcoin cá nhân của bạn. Như vậy, bạn sẽ tránh được rò rỉ thông tin và đạt được sự độc lập hoàn toàn. Mặc dù hướng dẫn được trình bày dưới đây hữu ích cho một số mục tiêu hoặc cho người mới bắt đầu, để tối ưu hóa phiên coinjoin của bạn, việc sử dụng Dojo của riêng bạn được khuyến nghị. Một hướng dẫn chi tiết về cài đặt cấu hình này sẽ sớm có sẵn trên PlanB Network.

### Cài đặt Samourai Wallet
Để bắt đầu, bạn rõ ràng cần ứng dụng Samourai Wallet. Bạn có thể tải nó trực tiếp từ trang web chính thức sử dụng APK, từ GitLab của họ, hoặc từ Google Play Store.

### Tạo một Ví Phần Mềm
Sau khi cài đặt phần mềm, bạn sẽ cần tiến hành tạo một ví Bitcoin trên Samourai. Nếu bạn đã có một ví, bạn có thể bỏ qua trực tiếp sang bước tiếp theo.

Khi mở ứng dụng, nhấn nút `Start` màu xanh. Sau đó, bạn sẽ được yêu cầu chọn một vị trí trong tệp của điện thoại để lưu trữ bản sao lưu được mã hóa của ví mới của bạn.

![samourai](assets/notext/9.webp)
Kích hoạt Tor bằng cách nhấp vào nút tương ứng. Tại giai đoạn này, bạn cũng có tùy chọn chọn một Dojo cụ thể. Tuy nhiên, trong hướng dẫn này, chúng ta sẽ tiếp tục với Dojo mặc định; vì vậy bạn có thể để tùy chọn bị vô hiệu hóa. Khi Tor được kết nối, nhấn nút `Create a new wallet`.
![samourai](assets/notext/10.webp)

Samourai Wallet sau đó yêu cầu bạn thiết lập một cụm mật khẩu BIP39. Mật khẩu bổ sung này rất quan trọng vì nó trực tiếp tác động vào việc phát sinh khóa riêng của bạn. Một sự mất mát của cụm mật khẩu này sẽ dẫn đến việc không thể truy cập vào bitcoin của bạn, khiến chúng bị mất không thể khôi phục. Để khôi phục ví Samourai của bạn, việc có cả cụm từ khôi phục 12 từ và cụm mật khẩu là bắt buộc.
Vì vậy, việc chọn một cụm mật khẩu mạnh và tạo một hoặc nhiều bản sao vật lý, trên giấy hoặc trên một phương tiện kim loại, là rất quan trọng để đảm bảo an toàn cho bitcoin của bạn. Sau khi hoàn thành những công việc này, đánh dấu vào ô `Tôi đã biết rằng trong trường hợp mất...`, sau đó nhấn nút `TIẾP THEO`.
![samourai](assets/notext/11.webp)

Bạn sau đó cần định nghĩa một mã PIN gồm từ 5 đến 8 chữ số. Mã này sẽ bảo vệ quyền truy cập vào ví của bạn trên điện thoại. Mã PIN sẽ được yêu cầu mỗi khi bạn muốn mở ứng dụng Samourai. Chọn một mã PIN mạnh và đảm bảo giữ một bản sao lưu. Sau đó, bạn có thể nhấn nút `TIẾP THEO`.

![samourai](assets/notext/12.webp)

Samourai sẽ yêu cầu bạn nhập lại mã PIN để xác nhận. Nhập vào, sau đó nhấn `HOÀN TẤT`.

![samourai](assets/notext/13.webp)

Sau đó, bạn sẽ truy cập vào cụm từ khôi phục của mình gồm 12 từ. Cụm từ này cho phép bạn khôi phục ví của mình với cụm mật khẩu đã nhập trước đó. Rất khuyến khích tạo một hoặc nhiều bản sao của cụm từ này trên phương tiện vật lý, như giấy hoặc vật liệu kim loại, để đảm bảo an toàn cho bitcoin của bạn trong trường hợp có vấn đề.

Sau khi tạo những bản sao lưu này, bạn sẽ được chuyển đến giao diện của ví Samourai mới của mình.

![samourai](assets/notext/14.webp)

Bạn được đề nghị nhận PayNym Bot của mình. Bạn có thể yêu cầu nếu muốn, mặc dù nó không cần thiết cho hướng dẫn của chúng tôi.

![samourai](assets/notext/15.webp)
Trước khi tiến hành nhận bitcoin vào ví mới này, rất khuyến khích kiểm tra lại tính hợp lệ của các bản sao lưu ví của bạn (cụm mật khẩu và cụm từ khôi phục). Để xác minh cụm mật khẩu, bạn có thể chọn biểu tượng của PayNym Bot của mình ở góc trên bên trái của màn hình, sau đó theo dõi đường dẫn:
```plaintext
Cài đặt > Khắc phục sự cố > Kiểm tra cụm mật khẩu/sao lưu
```

Nhập cụm mật khẩu của bạn để thực hiện việc xác minh.

![samourai](assets/notext/16.webp)

Samourai sẽ xác nhận nếu nó hợp lệ.

![samourai](assets/notext/17.webp)

Để xác minh bản sao lưu của cụm từ khôi phục, truy cập vào biểu tượng của PayNym Bot của bạn, nằm ở góc trên bên trái của màn hình, và theo dõi đường dẫn này:
```plaintext
Cài đặt > Ví > Hiển thị cụm từ khôi phục 12 từ
```

Samourai sẽ hiển thị một cửa sổ với cụm từ khôi phục của bạn. Đảm bảo nó khớp chính xác với bản sao vật lý của bạn.

Để tiến xa hơn và thực hiện một bài kiểm tra khôi phục hoàn chỉnh, ghi chú một yếu tố chứng thực của ví của bạn, như một trong những `xpubs`, sau đó tiến hành xóa ví của bạn (miễn là nó vẫn trống). Mục tiêu là thử khôi phục ví trống này chỉ sử dụng các bản sao lưu vật lý của bạn. Nếu việc khôi phục thành công, điều này chỉ ra rằng các bản sao lưu của bạn hợp lệ và đáng tin cậy.

### Nhận bitcoin
Sau khi tạo ví của bạn, bạn sẽ bắt đầu với một tài khoản duy nhất, được xác định bởi chỉ số `0'`. Đây là tài khoản **nạp tiền** mà chúng tôi đã nói về trong các phần trước. Đó là tài khoản mà bạn sẽ cần chuyển bitcoin dành cho coinjoins.

Để làm điều này, nhấn vào biểu tượng `+` màu xanh dương nằm ở góc dưới bên phải của màn hình.

![samourai](assets/notext/18.webp)

Sau đó nhấn vào nút `Nhận` màu xanh lá.

![samourai](assets/notext/19.webp)

Samourai sẽ tự động tạo một địa chỉ mới trống để nhận bitcoin.

![samourai](assets/notext/20.webp)
Bạn có thể gửi bitcoin của mình để được trộn ở đó.
![samourai](assets/notext/21.webp)

### Thực hiện Giao dịch Tx0
Khi giao dịch được xác nhận, chúng ta có thể bắt đầu quá trình coinjoins. Để làm điều này, nhấp vào nút màu xanh `+` ở góc dưới bên phải của màn hình.

![samourai](assets/notext/22.webp)

Sau đó nhấp vào `Whirlpool` màu xanh.

![samourai](assets/notext/23.webp)

Chờ trong khi Whirlpool khởi tạo và Samourai tạo các tài khoản cần thiết.

![samourai](assets/notext/24.webp)

Bạn sẽ đến trang chủ của Whirlpool. Nhấp vào `Start`.
![samourai](assets/notext/25.webp)
Chọn UTXO từ tài khoản **deposit** mà bạn muốn gửi vào chu kỳ coinjoin, sau đó nhấp vào `Next`.

![samourai](assets/notext/26.webp)

Trong bước tiếp theo, bạn sẽ cần chọn mức phí để phân bổ cho `Tx0` cũng như cho lần trộn đầu tiên của bạn. Cài đặt này sẽ quyết định tốc độ xác nhận của `Tx0` và coinjoin đầu tiên (hoặc các coinjoins đầu tiên) của bạn. Hãy nhớ rằng phí khai thác cho `Tx0` và lần trộn đầu tiên là trách nhiệm của bạn, nhưng bạn sẽ không phải trả phí khai thác cho các lần trộn lại sau này. Bạn có lựa chọn giữa các tùy chọn `Low`, `Normal`, hoặc `High`.

![samourai](assets/notext/27.webp)

Trong cùng một cửa sổ, bạn có tùy chọn chọn hồ bơi mà bạn sẽ tham gia. Vì ban đầu tôi đã chọn một UTXO của `454,258 sats`, lựa chọn duy nhất có thể của tôi là hồ `100,000 sats`. Trang này cũng giới thiệu với bạn phí dịch vụ của hồ, ngoài phí khai thác, giúp bạn biết tổng chi phí cho chu kỳ coinjoin này. Nếu mọi thứ phù hợp với bạn, chọn hồ phù hợp và tiếp tục bằng cách nhấp vào nút màu xanh `VERIFY CYCLE DETAILS`.

![samourai](assets/notext/28.webp)

Bạn có thể thấy tất cả chi tiết của chu kỳ coinjoin của mình:
- số lượng UTXOs sẽ tham gia vào hồ;
- các phí phát sinh;
- lượng thay đổi độc hại...

Xác minh thông tin, sau đó nhấp vào nút màu xanh `START CYCLE`.

![samourai](assets/notext/29.webp)

Một cửa sổ sẽ xuất hiện để đề nghị bạn đánh dấu sự thay đổi độc hại kết quả từ việc bạn tham gia vào chu kỳ coinjoin là "không thể chi tiêu". Bằng cách chọn `YES`, UTXO này sẽ không hiển thị trong ví của bạn và không thể được chọn cho các giao dịch tương lai. Tuy nhiên, nó vẫn có thể truy cập trong danh sách UTXOs trong ví của bạn, nơi bạn có thể thay đổi trạng thái của nó một cách thủ công. Khuyến nghị chọn tùy chọn này để tránh bất kỳ lỗi xử lý nào có thể làm ảnh hưởng đến quyền riêng tư của bạn sau này. Nếu bạn chọn `NO`, sự thay đổi độc hại sẽ vẫn có sẵn để sử dụng trong ví của bạn. Nếu bạn muốn tìm hiểu thêm về quản lý và sử dụng sự thay đổi độc hại này, tôi khuyên bạn nên đọc phần cuối của hướng dẫn này.

![samourai](assets/notext/30.webp)

Samourai sau đó sẽ phát sóng Tx0 của bạn.

![samourai](assets/notext/31.webp)

### Thực hiện các coinjoins
Một khi Tx0 được phát sóng, bạn có thể tìm thấy nó trong tab `Transactions` của menu Whirlpool.

![samourai](assets/notext/32.webp)
Các UTXO của bạn sẵn sàng để được trộn nằm trong tab `Mixing in progress...`, tương ứng với tài khoản **Premix**. ![samourai](assets/notext/33.webp)

Một khi `Tx0` được xác nhận, các UTXO của bạn sẽ được tự động đăng ký với điều phối viên, và các lần trộn ban đầu sẽ bắt đầu một cách tự động liên tiếp.

![samourai](assets/notext/34.webp)

Bằng cách kiểm tra tab `Remixing`, tương ứng với tài khoản **Postmix**, bạn sẽ quan sát thấy các UTXO kết quả từ các lần trộn ban đầu. Những đồng tiền này sẽ sẵn sàng cho việc trộn lại tiếp theo, mà không phát sinh thêm phí. Tôi khuyên bạn nên tham khảo bài viết khác này để tìm hiểu thêm về quy trình trộn lại và hiệu quả của một chu kỳ coinjoin: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)

![samourai](assets/notext/35.webp)

Có thể tạm thời ngưng việc trộn của một UTXO bằng cách nhấn nút tạm dừng nằm bên phải của nó. Để làm cho nó đủ điều kiện để trộn lại, chỉ cần nhấn vào cùng một nút một lần nữa. Quan trọng là phải lưu ý rằng chỉ một coinjoin có thể được thực hiện cho mỗi người dùng và mỗi hồ bơi cùng một lúc. Do đó, nếu bạn có 6 UTXO của `100 000 sats` sẵn sàng cho coinjoin, chỉ một trong số chúng có thể được trộn. Sau khi trộn một UTXO, Samourai Wallet tiến hành chọn ngẫu nhiên một UTXO mới từ số lượng có sẵn của bạn, nhằm mục đích đa dạng hóa và cân bằng việc trộn lại của mỗi đồng tiền.

![samourai](assets/notext/36.webp)

Để đảm bảo sự sẵn có liên tục của các UTXO của bạn cho việc trộn lại, cần thiết phải giữ ứng dụng Samourai hoạt động ở chế độ nền. Bạn sẽ thấy một thông báo trên điện thoại xác nhận rằng Whirlpool đang chạy. Đóng ứng dụng hoặc tắt điện thoại sẽ tạm dừng các coinjoins.

### Hoàn thành các coinjoins
Để chi tiêu các bitcoin đã trộn của bạn, hãy đến tài khoản **Postmix** được ghi chú là `Remixing` trong các tab menu Whirlpool.

![samourai](assets/notext/37.webp)

Nhấn vào logo Whirlpool màu xanh nằm ở góc dưới bên phải.

![samourai](assets/notext/38.webp)

Sau đó nhấn vào `Spend Mixed UTXOs`.

![samourai](assets/notext/39.webp)

Bạn có thể nhập địa chỉ của người nhận và số tiền cần gửi, cũng như cho bất kỳ giao dịch nào khác được thực hiện với Samourai Wallet. Nền màu xanh chỉ ra rằng các quỹ đang được chi tiêu từ một tài khoản Whirlpool, chứ không phải từ tài khoản **deposit**.

![samourai](assets/notext/40.webp)

Bằng cách nhấn vào 3 chấm nhỏ ở góc trên bên phải, bạn có tùy chọn chọn các UTXO cụ thể.
![samourai](assets/notext/41.webp)
Bằng cách nhấn vào ô vuông trắng ở góc trên bên phải của cửa sổ, bạn có thể quét mã QR của địa chỉ nhận bằng camera của mình.

![samourai](assets/notext/42.webp)

Nhập thông tin cần thiết cho giao dịch chi tiêu của bạn, sau đó nhấn vào nút xanh `VERIFY TRANSACTION`.

![samourai](assets/notext/43.webp)
Trong bước tiếp theo, bạn có tùy chọn để chỉnh sửa mức phí liên quan đến giao dịch của mình. Bạn cũng có thể kích hoạt tùy chọn Stonewall bằng cách đánh dấu vào ô tương ứng. Nếu tùy chọn Stonewall không thể chọn, điều đó có nghĩa là tài khoản **Postmix** của bạn không chứa UTXO có kích thước đủ lớn để hỗ trợ cấu trúc giao dịch cụ thể này.
[-> Tìm hiểu thêm về giao dịch Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Nếu mọi thứ đều làm bạn hài lòng, nhấn vào nút màu xanh `SEND ... BTC`.

![samourai](assets/notext/44.webp)

Samourai sau đó sẽ tiến hành ký giao dịch trước khi phát sóng nó trên mạng. Bạn chỉ cần chờ đợi cho đến khi nó được thêm vào một khối bởi một thợ mỏ.

![samourai](assets/notext/45.webp)

### Sử dụng SCODE
Đôi khi, nhóm Samourai Wallet cung cấp "SCODEs". SCODE là một mã khuyến mãi cung cấp giảm giá cho phí dịch vụ của hồ bơi. Samourai Wallet thỉnh thoảng cung cấp những mã như vậy cho người dùng của mình trong các sự kiện đặc biệt. Tôi khuyên bạn [theo dõi Samourai Wallet](https://twitter.com/SamouraiWallet) trên mạng xã hội để không bỏ lỡ các SCODE trong tương lai.

Để áp dụng một SCODE trên Samourai, trước khi bắt đầu một chu kỳ coinjoin mới, vào menu Whirlpool và chọn ba chấm nhỏ nằm ở góc trên bên phải của màn hình.

![samourai](assets/notext/46.webp)

Nhấn vào `SCODE (mã khuyến mãi) Whirlpool`.

![samourai](assets/notext/47.webp)

Nhập SCODE vào cửa sổ mở ra, sau đó xác nhận bằng cách nhấn vào `OK`.

![samourai](assets/notext/48.webp)

Whirlpool sẽ tự động đóng lại. Chờ Samourai hoàn tất việc tải, sau đó mở lại menu Whirlpool.

![samourai](assets/notext/49.webp)

Đảm bảo SCODE của bạn đã được đăng ký chính xác bằng cách nhấn một lần nữa vào ba chấm nhỏ, sau đó chọn `SCODE (mã khuyến mãi) Whirlpool`. Nếu mọi thứ đều ổn, bạn đã sẵn sàng để bắt đầu một chu kỳ Whirlpool mới với mức giảm giá về phí dịch vụ. Quan trọng là phải lưu ý rằng những SCODE này là tạm thời: chúng chỉ còn hiệu lực trong vài ngày trước khi trở nên lỗi thời.

## Làm thế nào để biết chất lượng của các chu kỳ coinjoin của chúng ta?
Để một coinjoin thực sự hiệu quả, điều cần thiết là nó phải thể hiện sự đồng nhất tốt giữa các lượng của đầu vào và đầu ra. Sự đồng nhất này làm tăng số lượng giải thích có thể trong mắt một quan sát viên bên ngoài, do đó tăng sự không chắc chắn xung quanh giao dịch. Để định lượng sự không chắc chắn này được tạo ra bởi một coinjoin, người ta có thể sử dụng việc tính toán entropy của giao dịch. Để khám phá sâu hơn về những chỉ số này, tôi giới thiệu bạn đọc hướng dẫn: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Mô hình Whirlpool được công nhận là một trong những mô hình mang lại sự đồng nhất nhiều nhất cho coinjoins.
Tiếp theo, hiệu suất của một số chu kỳ coinjoin được đánh giá dựa trên quy mô của các nhóm mà trong đó một đồng tiền được ẩn giấu. Kích thước của những nhóm này xác định cái được gọi là anonsets. Có hai loại anonsets: loại đầu tiên đánh giá sự riêng tư đạt được đối với phân tích hồi tưởng (từ hiện tại về quá khứ) và loại thứ hai, đối với phân tích tiềm năng (từ quá khứ đến hiện tại). Để hiểu rõ hơn về hai chỉ số này, tôi mời bạn tham khảo hướng dẫn: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

## Làm thế nào để quản lý postmix?
Sau khi thực hiện các chu kỳ coinjoin, chiến lược tốt nhất là giữ các UTXO của bạn trong tài khoản **postmix**, chờ đợi việc sử dụng trong tương lai của chúng. Thậm chí nên để chúng remix vô thời hạn cho đến khi bạn cần tiêu chúng.

Một số người dùng có thể xem xét việc chuyển bitcoin đã trộn của họ vào một ví được bảo vệ bởi một ví cứng. Điều này là khả thi, nhưng quan trọng là phải tuân thủ chặt chẽ các khuyến nghị của Samourai Wallet để không làm ảnh hưởng đến sự riêng tư đã đạt được.

Việc kết hợp các UTXO là lỗi thường gặp nhất. Cần tránh kết hợp các UTXO đã trộn với các UTXO chưa trộn trong cùng một giao dịch, để tránh CIOH (*Common-Input-Ownership-Heuristic*). Điều này đòi hỏi quản lý cẩn thận các UTXO của bạn trong ví, đặc biệt là về việc gắn nhãn. Ngoài coinjoin, việc kết hợp các UTXO thường là một thực hành xấu thường dẫn đến mất bảo mật khi không được quản lý đúng cách.
Bạn cũng nên cảnh giác với việc kết hợp các UTXO đã trộn với nhau. Việc kết hợp vừa phải là khả thi nếu các UTXO đã trộn của bạn có anonsets đáng kể, nhưng điều này sẽ không tránh khỏi làm giảm sự riêng tư của đồng tiền của bạn. Đảm bảo rằng việc kết hợp không quá lớn hoặc được thực hiện sau một số lần remix không đủ, vì điều này có nguy cơ thiết lập các liên kết có thể suy luận giữa các UTXO của bạn trước và sau các chu kỳ coinjoin. Trong trường hợp nghi ngờ về những hoạt động này, thực hành tốt nhất là không kết hợp các UTXO postmix, và chuyển chúng từng cái một vào ví cứng của bạn, tạo một địa chỉ trống mới mỗi lần. Một lần nữa, nhớ gắn nhãn đúng cách cho mỗi UTXO nhận được.

Cũng được khuyến cáo không chuyển các UTXO postmix của bạn vào một ví sử dụng kịch bản không phổ biến. Ví dụ, nếu bạn nhập Whirlpool từ một ví multisig sử dụng kịch bản `P2WSH`, có ít cơ hội bạn sẽ được trộn với các người dùng khác có cùng loại ví ban đầu. Nếu bạn thoát postmix của mình vào cùng một ví multisig đó, mức độ riêng tư của bitcoin đã trộn của bạn sẽ bị giảm đáng kể. Ngoài kịch bản, có nhiều dấu vết ví khác có thể làm bạn nhầm lẫn.

Như với bất kỳ giao dịch Bitcoin nào, cũng thích hợp không tái sử dụng địa chỉ nhận. Mỗi giao dịch mới phải được nhận trên một địa chỉ trống mới.

Giải pháp đơn giản và an toàn nhất là để các UTXO đã trộn của bạn nghỉ ngơi trong tài khoản **postmix** của họ, cho phép chúng remix và chỉ chạm vào chúng để tiêu. Ví Samourai và Sparrow có thêm các biện pháp bảo vệ chống lại tất cả những rủi ro liên quan đến phân tích chuỗi. Những biện pháp bảo vệ này giúp bạn tránh mắc lỗi.

## Làm thế nào để quản lý doxxic change?
Tiếp theo, bạn phải cẩn thận trong việc quản lý doxxic change, phần tiền lẻ không thể nhập vào hồ coinjoin. Những UTXO độc hại này, kết quả từ việc sử dụng Whirlpool, đặt ra rủi ro cho sự riêng tư của bạn vì chúng thiết lập một liên kết giữa bạn và việc sử dụng coinjoin. Do đó, việc xử lý chúng một cách cẩn thận là điều bắt buộc và không kết hợp chúng với các UTXO khác, đặc biệt là các UTXO đã trộn. Dưới đây là các chiến lược khác nhau cần xem xét cho việc sử dụng chúng:
- **Trộn chúng trong các nhóm nhỏ hơn:** Nếu UTXO độc hại của bạn đủ lớn để tự mình tham gia vào một nhóm nhỏ, hãy xem xét việc trộn lẫn chúng. Đây thường là lựa chọn tốt nhất. Tuy nhiên, điều quan trọng là không nên kết hợp nhiều UTXO độc hại để truy cập một nhóm, vì điều này có thể liên kết các mục nhập khác nhau của bạn.
- **Đánh dấu chúng là "không thể tiêu":** Một cách tiếp cận khác là ngừng sử dụng chúng, đánh dấu chúng là "không thể tiêu" trong tài khoản dành riêng của chúng và chỉ giữ (Hodl). Điều này đảm bảo rằng bạn không vô tình tiêu chúng. Nếu giá trị của bitcoin tăng, các nhóm mới phù hợp hơn với UTXO độc hại của bạn có thể xuất hiện;
- **Làm từ thiện:** Xem xét việc làm từ thiện, ngay cả những đóng góp khiêm tốn, cho các nhà phát triển làm việc trên Bitcoin và phần mềm liên quan. Bạn cũng có thể quyên góp cho các tổ chức chấp nhận BTC. Nếu việc quản lý UTXO độc hại của bạn có vẻ quá phức tạp, bạn có thể đơn giản loại bỏ chúng bằng cách làm từ thiện;
- **Mua thẻ quà tặng:** Các nền tảng như [Bitrefill](https://www.bitrefill.com/) cho phép bạn đổi bitcoin lấy thẻ quà tặng có thể sử dụng tại các nhà bán lẻ khác nhau. Đây có thể là cách để loại bỏ UTXO độc hại của bạn mà không mất giá trị liên quan;
- **Tập hợp chúng trên Monero:** Samourai Wallet hiện cung cấp dịch vụ hoán đổi nguyên tử giữa BTC và XMR. Đây là lý tưởng để quản lý UTXO độc hại bằng cách tập hợp chúng trên Monero, mà không làm ảnh hưởng đến quyền riêng tư qua KYC, trước khi gửi chúng trở lại Bitcoin. Tuy nhiên, lựa chọn này có thể tốn kém về phí khai thác và phí bổ sung do hạn chế về thanh khoản;
- **Gửi chúng đến Lightning Network:** Chuyển những UTXO này đến Lightning Network để hưởng lợi từ phí giao dịch giảm là một lựa chọn có thể thú vị. Tuy nhiên, phương pháp này có thể tiết lộ một số thông tin tùy thuộc vào cách bạn sử dụng Lightning và do đó nên được thực hiện một cách cẩn thận.

Các hướng dẫn chi tiết về việc thực hiện những kỹ thuật khác nhau này sẽ sớm được cung cấp trên PlanB Network.

**Tài nguyên bổ sung:**
[Hướng dẫn video của Samourai Wallet](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)
- [Tài liệu Samourai Wallet - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Chuỗi tweet về coinjoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Bài đăng trên blog về coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).