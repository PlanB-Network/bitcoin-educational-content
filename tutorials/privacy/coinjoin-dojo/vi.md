---
name: Coinjoin - Dojo
description: Cách thực hiện coinjoin với Dojo của riêng bạn?
---
![cover](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, công cụ Whirlpool không còn hoạt động, ngay cả đối với những người có Dojo riêng hoặc đang sử dụng Sparrow Wallet. Tuy nhiên, vẫn có khả năng công cụ này có thể được khôi phục trong những tuần tới hoặc được ra mắt lại theo một cách khác. Hơn nữa, phần lý thuyết của bài viết này vẫn còn liên quan để hiểu về nguyên tắc và mục tiêu của coinjoins nói chung (không chỉ Whirlpool), cũng như hiểu về hiệu quả của mô hình Whirlpool.*

_Chúng tôi đang ch closely theo dõi sự phát triển của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này được cung cấp chỉ cho mục đích giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng các công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ các luật lệ trong phạm vi quyền hạn của họ._

---

Trong hướng dẫn này, bạn sẽ học được coinjoin là gì và cách thực hiện một coinjoin sử dụng phần mềm Samourai Wallet và triển khai Whirlpool, sử dụng Dojo của riêng bạn. Theo ý kiến của tôi, phương pháp này hiện là tốt nhất để trộn bitcoins của bạn.

## Coinjoin trên Bitcoin là gì?
**Coinjoin là một kỹ thuật làm gián đoạn khả năng theo dõi bitcoins trên blockchain**. Nó dựa vào một giao dịch hợp tác với cấu trúc cụ thể mang tên giống như vậy: giao dịch coinjoin.

Coinjoins tăng cường sự riêng tư cho người dùng Bitcoin bằng cách làm phức tạp việc phân tích chuỗi cho các quan sát viên bên ngoài. Cấu trúc của chúng cho phép kết hợp nhiều đồng tiền từ các người dùng khác nhau vào một giao dịch duy nhất, do đó làm mờ các dấu vết và khó xác định được liên kết giữa các địa chỉ đầu vào và đầu ra.

Nguyên tắc của coinjoin dựa trên một cách tiếp cận hợp tác: một số người dùng muốn trộn bitcoins của họ đặt cùng một số tiền như là đầu vào của cùng một giao dịch. Những số tiền này sau đó được phân phối lại như là đầu ra có giá trị bằng nhau cho mỗi người dùng. Khi giao dịch kết thúc, việc liên kết một đầu ra cụ thể với một người dùng cụ thể tại đầu vào trở nên không thể. Không có liên kết trực tiếp nào giữa các đầu vào và đầu ra, điều này phá vỡ mối liên kết giữa người dùng và UTXO của họ, cũng như lịch sử của mỗi đồng tiền.
![coinjoin](assets/notext/1.webp)

Ví dụ về một giao dịch coinjoin (không phải của tôi): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Để thực hiện một coinjoin trong khi đảm bảo rằng mỗi người dùng luôn kiểm soát quỹ của mình, quá trình bắt đầu với việc giao dịch được xây dựng bởi một điều phối viên, người sau đó truyền nó cho các bên tham gia. Mỗi người dùng sau đó ký vào giao dịch sau khi xác minh rằng nó phù hợp với họ. Tất cả chữ ký thu thập được cuối cùng được tích hợp vào giao dịch. Nếu một nỗ lực nhằm chuyển hướng quỹ được thực hiện bởi một người dùng hoặc điều phối viên, thông qua việc sửa đổi các đầu ra của giao dịch coinjoin, các chữ ký sẽ trở nên không hợp lệ, dẫn đến việc giao dịch bị các nút từ chối.

Có một số triển khai của coinjoin, như Whirlpool, JoinMarket, hoặc Wabisabi, mỗi cái nhằm mục đích quản lý sự phối hợp giữa các bên tham gia và tăng hiệu quả của các giao dịch coinjoin.
Trong hướng dẫn này, chúng ta sẽ tìm hiểu về việc triển khai **Whirlpool**, mà tôi coi là giải pháp hiệu quả nhất để thực hiện coinjoins trên Bitcoin. Mặc dù có sẵn trên một số ví, trong hướng dẫn này, chúng ta sẽ chỉ khám phá việc sử dụng nó với ứng dụng di động Samourai Wallet, không kể đến Dojo.
## Tại sao lại thực hiện coinjoins trên Bitcoin?
Một trong những vấn đề ban đầu với bất kỳ hệ thống thanh toán ngang hàng nào là việc chi tiêu gấp đôi: làm thế nào để ngăn chặn các cá nhân có ý đồ xấu chi tiêu cùng một đơn vị tiền tệ nhiều lần mà không cần đến một cơ quan trung ương để phân xử?

Satoshi Nakamoto đã cung cấp một giải pháp cho bài toán này thông qua giao thức Bitcoin, một hệ thống thanh toán điện tử ngang hàng hoạt động độc lập với bất kỳ cơ quan trung ương nào. Trong bài viết của mình, ông nhấn mạnh rằng cách duy nhất để chứng minh sự vắng mặt của việc chi tiêu gấp đôi là đảm bảo tính hiển thị của tất cả các giao dịch trong hệ thống thanh toán.

Để đảm bảo rằng mỗi người tham gia đều biết về các giao dịch, chúng phải được công bố công khai. Do đó, hoạt động của Bitcoin dựa trên một cơ sở hạ tầng minh bạch và phân tán, cho phép bất kỳ người vận hành nút nào cũng có thể xác minh toàn bộ chuỗi chữ ký điện tử và lịch sử của mỗi đồng tiền, từ khi nó được tạo ra bởi một thợ mỏ.

Bản chất minh bạch và phân tán của blockchain Bitcoin có nghĩa là bất kỳ người dùng nào của mạng cũng có thể theo dõi và phân tích các giao dịch của tất cả các bên khác. Kết quả là, sự ẩn danh ở cấp độ giao dịch là không thể. Tuy nhiên, sự ẩn danh được bảo toàn ở cấp độ nhận dạng cá nhân. Khác với hệ thống ngân hàng truyền thống nơi mỗi tài khoản được liên kết với một danh tính cá nhân, trên Bitcoin, quỹ được liên kết với các cặp khóa mật mã, do đó cung cấp cho người dùng một hình thức giả danh sau các định danh mật mã.

Do đó, bảo mật trên Bitcoin bị xâm phạm khi các quan sát viên bên ngoài quản lý để liên kết các UTXO cụ thể với người dùng đã được xác định. Một khi mối liên kết này được thiết lập, việc truy vết các giao dịch của họ và phân tích lịch sử của bitcoin của họ trở nên khả thi. Coinjoin chính xác là một kỹ thuật được phát triển để phá vỡ khả năng truy vết của UTXOs, do đó cung cấp một lớp bảo mật nhất định cho người dùng Bitcoin ở cấp độ giao dịch.

## Whirlpool hoạt động như thế nào?
Whirlpool nổi bật so với các phương pháp coinjoin khác bằng cách sử dụng giao dịch "_ZeroLink_", đảm bảo rằng không có liên kết kỹ thuật nào có thể xảy ra giữa tất cả các đầu vào và tất cả các đầu ra. Sự pha trộn hoàn hảo này được đạt được thông qua một cấu trúc nơi mỗi người tham gia đóng góp một lượng bằng nhau vào đầu vào (trừ phí khai thác), do đó tạo ra các đầu ra với số lượng hoàn hảo bằng nhau.
Cách tiếp cận hạn chế này đối với đầu vào mang lại cho các giao dịch coinjoin Whirlpool một đặc điểm độc đáo: sự vắng mặt hoàn toàn của các liên kết xác định giữa các đầu vào và đầu ra. Nói cách khác, mỗi đầu ra có khả năng bằng nhau được gán cho bất kỳ người tham gia nào, so với tất cả các đầu ra khác trong giao dịch.
Ban đầu, số lượng người tham gia trong mỗi Whirlpool coinjoin được giới hạn ở 5, với 2 người mới tham gia và 3 người remix (chúng tôi sẽ giải thích các khái niệm này thêm sau). Tuy nhiên, sự tăng của phí giao dịch trên chuỗi quan sát được vào năm 2023 đã thúc đẩy các đội ngũ của Samourai tái cấu trúc mô hình của họ để cải thiện quyền riêng tư trong khi giảm chi phí. Do đó, dựa trên tình hình thị trường của phí và số lượng người tham gia, điều phối viên giờ đây có thể tổ chức các coinjoins bao gồm 6, 7, hoặc 8 người tham gia. Những phiên tăng cường này được gọi là "_Surge Cycles_". Quan trọng là phải lưu ý rằng, bất kể cài đặt như thế nào, luôn chỉ có 2 người mới tham gia trong các coinjoins Whirlpool.

Do đó, các giao dịch Whirlpool được đặc trưng bởi một số lượng đầu vào và đầu ra giống nhau, có thể là:
- 5 đầu vào và 5 đầu ra;
![coinjoin](assets/notext/2.webp)
- 6 đầu vào và 6 đầu ra;
![coinjoin](assets/notext/3.webp)
- 7 đầu vào và 7 đầu ra;
![coinjoin](assets/notext/4.webp) - 8 đầu vào và 8 đầu ra.
![coinjoin](assets/notext/5.webp)
Mô hình được đề xuất bởi Whirlpool dựa trên các giao dịch coinjoin nhỏ. Khác với Wasabi và JoinMarket, nơi sự mạnh mẽ của anonsets dựa vào số lượng người tham gia trong một chu kỳ duy nhất, Whirlpool đặt cược vào việc kết nối nhiều chu kỳ nhỏ.

Trong mô hình này, người dùng chỉ phải trả phí khi họ lần đầu tiên nhập vào một hồ bơi, cho phép họ tham gia vào nhiều lần remix mà không cần phí bổ sung. Những người mới tham gia sẽ trả phí khai thác cho những người remix.

Với mỗi lần coinjoin thêm vào mà một đồng tiền tham gia, cùng với các đối tác đã gặp trước đó, anonsets sẽ tăng lên theo cấp số nhân. Mục tiêu do đó là tận dụng những lần remix miễn phí này, với mỗi lần xảy ra, góp phần tăng cường mật độ của anonsets liên quan đến mỗi đồng tiền được trộn.

Whirlpool được thiết kế với việc xem xét hai yêu cầu quan trọng:
- Khả năng triển khai trên thiết bị di động, vì Samourai Wallet chủ yếu là một ứng dụng dành cho điện thoại thông minh;
- Tốc độ của các chu kỳ remix để thúc đẩy sự tăng lên đáng kể trong anonsets.
Những yêu cầu này đã hướng dẫn sự lựa chọn của các nhà phát triển Samourai Wallet trong việc thiết kế Whirlpool, dẫn họ đến việc giới hạn số lượng người tham gia mỗi chu kỳ. Quá ít người tham gia sẽ làm giảm hiệu quả của coinjoin, giảm đáng kể anonsets được tạo ra mỗi chu kỳ, trong khi quá nhiều người tham gia sẽ gây ra vấn đề quản lý trên các ứng dụng di động và sẽ cản trở dòng chảy của các chu kỳ.
**Cuối cùng, không cần phải có số lượng người tham gia cao mỗi coinjoin trên Whirlpool vì anonsets được đạt được thông qua việc tích lũy nhiều chu kỳ coinjoin.**

[-> Tìm hiểu thêm về anonsets của Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Các hồ bơi và phí coinjoin
Để những chu kỳ nhiều lần này có thể tăng hiệu quả anonsets của các đồng tiền được trộn, một khuôn khổ nhất định phải được thiết lập để hạn chế số lượng UTXO được sử dụng. Whirlpool do đó xác định các hồ bơi khác nhau.

Một hồ bơi đại diện cho một nhóm người dùng muốn trộn cùng nhau, những người đồng ý về số lượng UTXO sử dụng để tối ưu hóa quá trình coinjoin. Mỗi hồ bơi chỉ định một số lượng cố định cho UTXO, mà người dùng phải tuân thủ để tham gia. Do đó, để thực hiện coinjoins với Whirlpool, bạn cần chọn một hồ bơi. Các hồ bơi hiện có sẵn như sau:
- 0.5 bitcoins;
- 0.05 bitcoin;
- 0.01 bitcoin;
- 0.001 bitcoin (= 100,000 sats).

Bằng cách tham gia vào một hồ bơi với bitcoins của bạn, chúng sẽ được chia để tạo ra UTXOs hoàn toàn đồng nhất với những người tham gia khác trong hồ bơi. Mỗi hồ bơi có một giới hạn tối đa; do đó, đối với số lượng vượt quá giới hạn này, bạn sẽ buộc phải thực hiện hai lần nhập riêng biệt trong cùng một hồ bơi hoặc chuyển sang một hồ bơi khác với số lượng lớn hơn:

| Hồ bơi (bitcoin) | Số lượng tối đa mỗi lần nhập (bitcoin) |
|------------------|----------------------------------------|
| 0.5              | 35                                     |
| 0.05             | 3.5                                    |
| 0.01             | 0.7                                    |
| 0.001            | 0.025                                  |
Như đã đề cập trước đây, một UTXO được coi là thuộc về một nhóm khi nó sẵn sàng để được tích hợp vào một coinjoin. Tuy nhiên, điều này không có nghĩa là người dùng mất quyền sở hữu của nó. **Qua các chu kỳ trộn lẫn khác nhau, bạn vẫn giữ quyền kiểm soát đầy đủ về khóa của mình và do đó, là bitcoin của bạn.** Đây là điều phân biệt kỹ thuật coinjoin với các kỹ thuật trộn lẫn tập trung khác.

Để tham gia vào một nhóm coinjoin, phí dịch vụ cũng như phí khai thác phải được thanh toán. Phí dịch vụ được cố định cho mỗi nhóm và nhằm bù đắp cho các đội ngũ chịu trách nhiệm phát triển và bảo trì Whirlpool.

Phí dịch vụ khi sử dụng Whirlpool chỉ phải trả một lần khi nhập vào nhóm. Sau bước này, bạn có cơ hội tham gia vào số lượng không giới hạn các lần remix mà không phải trả thêm phí nào. Dưới đây là các phí cố định hiện tại cho mỗi nhóm:

| Nhóm (bitcoin) | Phí Nhập (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Những phí này cơ bản hoạt động như một vé vào cửa cho nhóm được chọn, bất kể số lượng bạn đưa vào coinjoin. Do đó, dù bạn tham gia nhóm 0.01 với chính xác 0.01 BTC hay nhập vào với 0.5 BTC, phí sẽ giữ nguyên giá trị tuyệt đối.

Trước khi tiến hành coinjoins, người dùng do đó có sự lựa chọn giữa 2 chiến lược:
- Chọn một nhóm nhỏ hơn để giảm thiểu phí dịch vụ, biết rằng họ sẽ nhận lại nhiều UTXO nhỏ;
- Hoặc ưu tiên một nhóm lớn hơn, đồng ý trả phí cao hơn để kết thúc với số lượng UTXO giá trị lớn hơn ít hơn.

Nói chung, việc gộp nhiều UTXO đã trộn sau các chu kỳ coinjoin không được khuyến khích, vì điều này có thể làm mất đi tính bảo mật đã đạt được, đặc biệt là do Heuristic Sở Hữu Đầu Vào Chung (CIOH). Do đó, có thể sẽ khôn ngoan khi chọn một nhóm lớn hơn, ngay cả khi phải trả nhiều hơn, để tránh có quá nhiều UTXO giá trị nhỏ ở đầu ra. Người dùng phải cân nhắc những sự đánh đổi này để chọn nhóm họ ưa thích.

Ngoài phí dịch vụ, phí khai thác điển hình cho bất kỳ giao dịch Bitcoin nào cũng cần được xem xét. Là một người dùng Whirlpool, bạn sẽ phải trả phí khai thác cho giao dịch chuẩn bị (`Tx0`) cũng như cho coinjoin đầu tiên. Tất cả các lần remix sau đó sẽ miễn phí, nhờ vào mô hình của Whirlpool dựa trên việc thanh toán của người mới tham gia.

Thực sự, trong mỗi coinjoin Whirlpool, hai người dùng trong số các đầu vào là người mới tham gia. Các đầu vào khác đến từ những người remix. Kết quả là, phí khai thác cho tất cả các bên tham gia trong giao dịch được trả bởi hai người tham gia mới này, những người sau đó cũng sẽ được hưởng các lần remix miễn phí:
![coinjoin](assets/en/6.webp)
Nhờ vào hệ thống phí này, Whirlpool thực sự khác biệt so với các dịch vụ coinjoin khác vì anonsets của các UTXO không tỷ lệ với giá trả bởi người dùng. Do đó, có thể đạt được mức độ ẩn danh đáng kể cao chỉ bằng cách trả phí nhập của nhóm và phí khai thác cho hai giao dịch (các `Tx0` và hỗn hợp ban đầu).
Quan trọng cần lưu ý rằng người dùng cũng sẽ phải chịu phí đào để rút UTXO của họ khỏi pool sau khi hoàn thành nhiều lần coinjoin, trừ khi họ đã chọn tùy chọn `mix to`, điều này sẽ được thảo luận trong hướng dẫn dưới đây.
### Các tài khoản ví HD được sử dụng bởi Whirlpool
Để thực hiện coinjoin qua Whirlpool, ví cần tạo ra nhiều tài khoản riêng biệt. Một tài khoản, trong bối cảnh của một ví HD (*Hierarchical Deterministic*), tạo thành một phần hoàn toàn tách biệt khỏi các phần khác, sự tách biệt này xảy ra ở mức độ thứ ba của hệ thống phân cấp ví, tức là, ở mức của `xpub`.

Một ví HD lý thuyết có thể tạo ra tới `2^(32/2)` tài khoản khác nhau. Tài khoản ban đầu, được sử dụng mặc định trên tất cả các ví Bitcoin, tương ứng với chỉ mục `0'`.

Đối với các ví được điều chỉnh cho Whirlpool, như Samourai hoặc Sparrow, 4 tài khoản được sử dụng để đáp ứng nhu cầu của quá trình coinjoin:
- Tài khoản **deposit**, được xác định bởi chỉ mục `0'`;
- Tài khoản **bad bank** (hoặc doxxic change), được xác định bởi chỉ mục `2 147 483 644'`;
- Tài khoản **premix**, được xác định bởi chỉ mục `2 147 483 645'`;
- Tài khoản **postmix**, được xác định bởi chỉ mục `2 147 483 646'`.

Mỗi tài khoản này đều thực hiện một chức năng cụ thể trong coinjoin.

Tất cả các tài khoản này đều được liên kết với một seed duy nhất, cho phép người dùng khôi phục quyền truy cập vào tất cả bitcoin của họ sử dụng cụm từ khôi phục và, nếu cần, cụm từ mật khẩu của họ. Tuy nhiên, cần phải chỉ định cho phần mềm, trong quá trình khôi phục này, các chỉ mục tài khoản đã được sử dụng.

Bây giờ, hãy xem các giai đoạn khác nhau của một coinjoin Whirlpool trong các tài khoản này.

### Các giai đoạn khác nhau của coinjoins trên Whirlpool
**Giai đoạn 1: Tx0**
Điểm khởi đầu của bất kỳ coinjoin Whirlpool nào là tài khoản **deposit**. Đây là tài khoản bạn tự động sử dụng khi bạn tạo một ví Bitcoin mới. Tài khoản này phải được nạp với bitcoin mà người ta muốn trộn.
`Tx0` đại diện cho bước đầu tiên trong quá trình trộn Whirlpool. Mục tiêu là chuẩn bị và cân bằng UTXO cho coinjoin, bằng cách chia chúng thành các đơn vị tương ứng với số lượng của pool đã chọn, để đảm bảo sự đồng nhất của việc trộn. Các UTXO được cân bằng sau đó được gửi đến tài khoản **premix**. Còn sự khác biệt không thể nhập vào pool thì được tách ra thành một tài khoản cụ thể: **bad bank** (hoặc "doxxic change").
Giao dịch `Tx0` ban đầu này cũng phục vụ để thanh toán phí dịch vụ cho người điều phối trộn. Khác với các bước tiếp theo, giao dịch này không phải là cộng tác; người dùng do đó phải chịu tất cả phí đào:
![coinjoin](assets/en/7.webp)

Trong ví dụ này của giao dịch `Tx0`, một đầu vào `372,000 sats` từ tài khoản **deposit** của chúng tôi được chia thành nhiều UTXO đầu ra, được phân bổ như sau:
- Một số tiền `5,000 sats` dành cho người điều phối về phí dịch vụ, tương ứng với việc nhập vào pool của `100,000 sats`;
- Ba UTXO được chuẩn bị cho việc trộn, chuyển hướng đến tài khoản **premix** của chúng tôi và đăng ký với người điều phối. Các UTXO này được cân bằng ở mức `108,000 sats` mỗi cái, để trang trải phí đào cho lần trộn ban đầu của chúng;
- Số dư thừa không thể nhập vào hồ, do quá nhỏ, được coi là thay đổi độc hại. Nó được chuyển đến tài khoản cụ thể của nó. Tại đây, lượng thay đổi này lên đến `40,000 sats`;
- Cuối cùng, có `3,000 sats` không tạo thành một đầu ra, nhưng là phí khai thác cần thiết để xác nhận `Tx0`.

Ví dụ, đây là một giao dịch Whirlpool Tx0 thực tế (không phải của tôi): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Bước 2: Thay đổi độc hại**
Số dư thừa không thể được tích hợp vào hồ, tương đương với `40,000 sats`, được chuyển hướng đến tài khoản **ngân hàng xấu**, còn được gọi là "thay đổi độc hại", để đảm bảo sự tách biệt nghiêm ngặt từ các UTXO khác trong ví.

UTXO này nguy hiểm cho quyền riêng tư của người dùng vì không chỉ vẫn gắn liền với quá khứ của nó, và do đó có thể với danh tính của chủ sở hữu, mà nó còn được ghi nhận là thuộc về một người dùng đã thực hiện coinjoin.
Nếu UTXO này được hợp nhất với các đầu ra đã trộn, họ sẽ mất tất cả sự bảo mật đạt được trong các chu kỳ coinjoin, đặc biệt là do Heuristic Sở Hữu Đầu Vào Chung (CIOH). Nếu nó được hợp nhất với các thay đổi độc hại khác, người dùng có nguy cơ mất bảo mật vì điều này sẽ liên kết các đầu vào khác nhau của các chu kỳ coinjoin. Do đó, nó phải được xử lý cẩn thận. Cách quản lý UTXO độc hại này sẽ được chi tiết trong phần cuối của bài viết này, và các hướng dẫn tương lai sẽ đề cập kỹ lưỡng hơn về các phương pháp này trên Mạng PlanB.

**Bước 3: Hỗn Hợp Ban Đầu**
Sau khi `Tx0` hoàn thành, các UTXO được cân bằng sẽ được gửi đến tài khoản **premix** của ví chúng ta, sẵn sàng được giới thiệu vào chu kỳ coinjoin đầu tiên của họ, còn được gọi là "hỗn hợp ban đầu". Nếu, như trong ví dụ của chúng ta, `Tx0` tạo ra nhiều UTXO dành cho việc trộn, mỗi UTXO sẽ được tích hợp vào một coinjoin ban đầu riêng biệt.

Sau những hỗn hợp đầu tiên này, tài khoản **premix** sẽ trống, trong khi tiền xu của chúng ta, sau khi đã trả phí khai thác cho coinjoin đầu tiên này, sẽ được điều chỉnh chính xác theo số lượng được xác định bởi hồ đã chọn. Trong ví dụ của chúng ta, UTXO ban đầu của chúng ta `108 000 sats` sẽ được giảm xuống chính xác còn `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Bước 4: Các Lần Trộn Lại**
Sau hỗn hợp ban đầu, các UTXO được chuyển đến tài khoản **postmix**. Tài khoản này tập hợp các UTXO đã được trộn và những UTXO đang chờ được trộn lại. Khi ứng dụng Whirlpool hoạt động, các UTXO nằm trong tài khoản **postmix** sẽ tự động có sẵn để trộn lại và sẽ được chọn ngẫu nhiên để tham gia vào các chu kỳ mới.

Như một lời nhắc nhở, các lần trộn lại sau đó là miễn phí 100%: không yêu cầu thêm phí dịch vụ hay phí khai thác. Giữ các UTXO trong tài khoản **postmix** do đó duy trì giá trị không đổi của chúng và đồng thời cải thiện anonsets của họ. Đó là lý do tại sao việc cho phép những đồng tiền này tham gia vào nhiều chu kỳ coinjoin là quan trọng. Nó không tốn của bạn bất cứ điều gì, và nó tăng cấp độ ẩn danh của họ.
Khi bạn quyết định chi tiêu các UTXO đã được trộn lẫn, bạn có thể thực hiện trực tiếp từ tài khoản **postmix** này. Được khuyến nghị giữ các UTXO đã trộn trong tài khoản này để hưởng lợi từ việc remix miễn phí và tránh chúng rời khỏi chu trình Whirlpool, điều này có thể giảm bảo mật của chúng.

Như chúng ta sẽ thấy trong hướng dẫn sau, cũng có tùy chọn `mix to` cho phép tự động gửi tiền đã trộn của bạn đến một ví khác, chẳng hạn như ví lạnh, sau một số lần coinjoin đã định trước.

Sau khi đã nắm vững lý thuyết, chúng ta sẽ đi vào thực hành với một hướng dẫn sử dụng Whirlpool thông qua ứng dụng Samourai Wallet trên Android, đồng bộ với Whirlpool CLI và GUI trên Dojo của riêng bạn!
## Hướng dẫn: Coinjoin Whirlpool với Dojo của Riêng Bạn
Có nhiều lựa chọn để sử dụng Whirlpool. Lựa chọn mà tôi muốn giới thiệu ở đây là tùy chọn Samourai Wallet, một ứng dụng quản lý ví Bitcoin mã nguồn mở trên Android, nhưng lần này **với Dojo của riêng bạn**.

Thực hiện coinjoins qua Samourai Wallet sử dụng Dojo của riêng bạn, theo ý kiến của tôi, là chiến lược hiệu quả nhất để thực hiện coinjoins trên Bitcoin đến thời điểm hiện tại. Cách tiếp cận này đòi hỏi một khoản đầu tư ban đầu về cài đặt, nhưng một khi đã hoàn tất, nó cung cấp khả năng trộn và remix bitcoin của bạn liên tục, 24 giờ một ngày, 7 ngày một tuần, mà không cần phải giữ ứng dụng Samourai hoạt động suốt thời gian. Thực sự, nhờ vào Whirlpool CLI hoạt động trên một nút Bitcoin, bạn luôn sẵn sàng tham gia vào coinjoins. Sau đó, ứng dụng Samourai cho bạn cơ hội chi tiêu tiền đã trộn của mình bất cứ lúc nào, ở bất cứ đâu, trực tiếp từ điện thoại thông minh của bạn. Hơn nữa, phương pháp này có lợi thế là không bao giờ kết nối bạn với các máy chủ do đội ngũ Samourai quản lý, do đó bảo vệ `xpub` của bạn khỏi bất kỳ sự phơi bày bên ngoài nào.

Kỹ thuật này do đó là lý tưởng cho những ai tìm kiếm sự riêng tư tối đa và các chu kỳ coinjoin chất lượng cao nhất. Tuy nhiên, nó đòi hỏi phải có một nút Bitcoin sẵn có và, như chúng ta sẽ thấy sau, đòi hỏi một số cài đặt. Do đó, nó phù hợp hơn với người dùng trung cấp đến nâng cao. Đối với người mới bắt đầu, tôi khuyên nên làm quen với coinjoin thông qua hai hướng dẫn khác, cho thấy cách thực hiện từ Sparrow Wallet hoặc Samourai Wallet (không có Dojo):
- **[Hướng dẫn coinjoin Sparrow Wallet](https://planb.network/en/tutorials/privacy/coinjoin-sparrow-wallet)**;
- **[Hướng dẫn coinjoin Samourai Wallet (không có Dojo)](https://planb.network/en/tutorials/privacy/coinjoin-samourai-wallet)**.

### Hiểu về Cài Đặt
Để bắt đầu, bạn sẽ cần một Dojo! Dojo là một triển khai nút Bitcoin dựa trên Bitcoin Core, được phát triển bởi các đội ngũ Samourai.

Để chạy Dojo của riêng bạn, bạn có tùy chọn hoặc là tự cài đặt một nút Dojo một cách độc lập, hoặc tận dụng Dojo trên một giải pháp nút Bitcoin "node-in-box" khác. Hiện tại, các tùy chọn có sẵn là:
- [RoninDojo](https://ronindojo.io/), là một Dojo được nâng cấp với các công cụ bổ sung, bao gồm trợ lý cài đặt và trợ lý quản lý. Tôi chi tiết quy trình cài đặt và sử dụng RoninDojo trong hướng dẫn khác này: [RONINDOJO V2](https://planb.network/en/tutorials/node/ronin-dojo-v2);
- [Umbrel](https://umbrel.com/) với ứng dụng "Samourai Server";
- [MyNode](https://mynodebtc.com/) với ứng dụng "Dojo";
- [Nodl](https://www.nodl.eu/) với ứng dụng "Dojo";
- [Citadel](https://runcitadel.space/) với ứng dụng "Samourai".
![coinjoin](assets/notext/9.webp)
Trong cài đặt của chúng tôi, chúng tôi sẽ tương tác với ba giao diện riêng biệt:
- **Samourai Wallet**, nơi sẽ chứa ví Bitcoin của chúng tôi dành riêng cho coinjoins. Có sẵn miễn phí trên Android, ứng dụng FOSS này cho phép bạn kiểm soát ví trộn của mình, đặc biệt là để chi tiêu postmix từ điện thoại thông minh của bạn;
- **Whirlpool CLI** (_Giao Diện Dòng Lệnh_), sẽ hoạt động trên node chứa Dojo. Phần mềm này sẽ có quyền truy cập vào khóa của ví Samourai của bạn. Nó chịu trách nhiệm giao tiếp với điều phối viên và quản lý coinjoins liên tục. Nó hoạt động như một bản sao của ví Samourai của bạn trên node của bạn, sẵn sàng tham gia vào coinjoins bất cứ lúc nào;
- **Whirlpool GUI** (_Giao Diện Đồ Họa_), giao diện đồ họa mà chúng tôi sẽ sử dụng để theo dõi hoạt động của Whirlpool CLI và khởi tạo trộn từ xa. Whirlpool GUI cung cấp một biểu đồ trực quan về các hoạt động do Whirlpool CLI thực hiện. Phần mềm này phải được cài đặt trên một máy tính riêng biệt khỏi Dojo. Đối với người dùng của Umbrel, MyNode, Nodl và Citadel, Whirlpool GUI là bắt buộc. Tuy nhiên, với RoninDojo, giao diện Whirlpool GUI đã được tích hợp sẵn vào giao diện web của node qua ứng dụng `Whirlpool`. Do đó, bạn sẽ không cần phải cài đặt nó trên một PC riêng biệt.

Theo ý kiến của tôi, sử dụng RoninDojo đại diện cho giải pháp tốt nhất để thực hiện coinjoins với một Dojo. Vì phần mềm node-in-box này có quan hệ đối tác trực tiếp với các đội ngũ của Samourai, RoninDojo được tối ưu hóa nhiều hơn cho việc này. Hơn nữa, việc tích hợp Whirlpool GUI vào giao diện web đơn giản hóa đáng kể quá trình thiết lập. Trong hướng dẫn này, tôi vẫn sẽ giải thích cách thực hiện với các giải pháp khác tích hợp Dojo (Umbrel, Nodl, MyNode và Citadel).

### Chuẩn bị Dojo của bạn
Để bắt đầu, bạn sẽ cần cài đặt Dojo và nhận mã QR hoặc liên kết cho phép bạn kết nối với nó từ xa. Liên kết này là một địa chỉ Tor kết thúc bằng `.onion`. Nếu bạn sử dụng RoninDojo, chỉ cần điều hướng đến menu `Pairing` để truy cập thông tin này.
![coinjoin](assets/notext/10.webp)

Dưới `Samourai Dojo`, nhấp vào nút `Pair now`.

![coinjoin](assets/notext/11.webp)

Mã QR kết nối của bạn và liên kết tương ứng sẽ được hiển thị.

![coinjoin](assets/notext/12.webp)

Nếu bạn đang sử dụng Umbrel, hãy vào App Store và tìm kiếm ứng dụng `Samourai Server`. Nó nằm trong tab `Bitcoin`.

![coinjoin](assets/notext/13.webp)

Cài đặt ứng dụng.

![coinjoin](assets/notext/14.webp)

Khi mở ứng dụng, bạn sẽ có quyền truy cập vào mã QR để kết nối với Dojo của mình.

![coinjoin](assets/notext/15.webp)

Nếu bạn sử dụng phần mềm node-in-box khác như MyNode, Citadel, hoặc Nodl, quy trình tương tự như với Umbrel. Bạn cần cài đặt ứng dụng Samourai hoặc Dojo để nhận thông tin cần thiết để kết nối với Dojo của mình.

![coinjoin](assets/notext/16.webp)

### Chuẩn bị ví Samourai của bạn
Sau khi lấy được thông tin kết nối đến Dojo của bạn, bây giờ là lúc để thiết lập ví của bạn cho coinjoins. Có hai tình huống: nếu bạn chưa có Ví Samourai trên điện thoại thông minh, quá trình này rất đơn giản, chỉ cần tạo một cái mới.
Ngược lại, nếu bạn đã có Ví Samourai, bạn sẽ cần phải cài đặt lại ứng dụng để liên kết nó với một Dojo mới. Bước này là cần thiết vì việc kết nối với một Dojo chỉ có thể được thiết lập ngay khi ứng dụng được khởi chạy lần đầu. Tuy nhiên, nhờ vào tệp sao lưu được mã hóa tự động tạo ra bởi Samourai trên điện thoại của bạn, thủ tục này đơn giản và nhanh chóng.

*Nếu bạn chưa bao giờ sử dụng Samourai, bạn có thể bỏ qua các bước sơ bộ này và tiến thẳng đến việc cài đặt ứng dụng.*

Đầu tiên và quan trọng nhất, hãy đảm bảo ứng dụng Ví Samourai của bạn được cập nhật. Để làm điều này, kiểm tra Google Play Store hoặc so sánh phiên bản của ứng dụng của bạn trong `Cài đặt > Khác` với phiên bản có sẵn trên trang web của Samourai.

![coinjoin](assets/notext/17.webp)

Hãy chắc chắn bạn có cụm từ khôi phục ví Samourai của mình và nó phải dễ đọc. Sau đó, thực hiện một bài kiểm tra cụm từ BIP39 của bạn bằng cách điều hướng đến `Cài đặt > Khắc phục sự cố > Kiểm tra cụm từ/ Sao lưu` để xác nhận độ chính xác của nó.

![coinjoin](assets/notext/18.webp)
Nhập cụm từ của bạn, sau đó xác nhận rằng Samourai xác nhận tính hợp lệ của nó.
![coinjoin](assets/notext/19.webp)

Nếu cụm từ của bạn không hợp lệ, hoặc nếu bạn không có cụm từ khôi phục của mình, điều cần thiết là phải ngay lập tức dừng thủ tục! **Bạn có nguy cơ mất bitcoins trong quá trình này.** Trong trường hợp này, được khuyến nghị chuyển tiền của bạn sang một ví khác và bắt đầu với một ví Samourai trống mới. Các bước tiếp theo chỉ nên được thực hiện nếu bạn chắc chắn rằng bạn có tất cả thông tin sao lưu cần thiết và cụm từ của bạn hợp lệ.

Tiếp theo, tiến hành tạo một bản sao lưu được mã hóa của ví của bạn và sao chép nó vào bảng tạm của bạn. Để thực hiện thao tác này, nhấp vào ba chấm nhỏ nằm ở góc trên bên phải của màn hình, sau đó chọn `Xuất sao lưu ví`.

![coinjoin](assets/notext/20.webp)

**Từ bước này trở đi, không sao chép bất cứ thứ gì khác vào bảng tạm của bạn!** Việc giữ bản sao lưu đã sao chép là hoàn toàn cần thiết.

Nếu bạn đã thực hiện đúng các bước trước, bây giờ bạn có thể an toàn xóa ví Samourai của mình. Để làm điều này, đi đến: `Cài đặt > Ví > Xóa an toàn ví`.

![coinjoin](assets/notext/21.webp)

![coinjoin](assets/notext/22.webp)

*Nếu bạn chưa bao giờ sử dụng Samourai và đang cài đặt ứng dụng từ đầu, bạn có thể tiếp tục hướng dẫn từ bước này.*

Ứng dụng Samourai của bạn bây giờ đã được đặt lại. Mở ứng dụng và tiến hành các bước thiết lập như thể bạn đang sử dụng nó lần đầu tiên.

![coinjoin](assets/notext/23.webp)

Trong bước tiếp theo, bạn sẽ truy cập trang dành riêng cho việc cấu hình Dojo của mình. Chọn tùy chọn `Dojo`, sau đó nhập thông tin đăng nhập Dojo của bạn. Để làm điều này, bạn có tùy chọn quét thông tin bằng cách nhấn `Quét QR`.

![coinjoin](assets/notext/24.webp)

*Đối với người dùng mới của Samourai, sau đó sẽ cần thiết lập một ví từ đầu. Nếu bạn cần hỗ trợ, bạn có thể tham khảo hướng dẫn thiết lập một ví Samourai mới [trong hướng dẫn này, cụ thể là trong phần "Tạo một ví phần mềm"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*
Nếu bạn đang tiến hành khôi phục một ví Samourai đã tồn tại, chọn `Khôi phục ví đã có`, sau đó chọn `Tôi có tệp sao lưu Samourai`.
![coinjoin](assets/notext/25.webp)
Thông thường, bạn nên luôn có tệp khôi phục của mình trong bộ nhớ tạm. Sau đó nhấn vào `DÁN` để chèn tệp của bạn vào vị trí đã chỉ định. Để giải mã nó, cũng cần nhập cụm từ bí mật BIP39 của ví bạn vào trường tương ứng, nằm ngay bên dưới. Để hoàn tất, nhấn vào `HOÀN THÀNH`.
![coinjoin](assets/notext/26.webp)

Sau đó, bạn sẽ được chuyển hướng đến ví Samourai của mình, lần này, sẽ được kết nối với Dojo của riêng bạn.

![coinjoin](assets/notext/27.webp)

### Cài đặt Whirlpool GUI
Bây giờ là lúc để cài đặt Whirlpool GUI, giao diện người dùng đồ họa sẽ cho phép bạn quản lý các chu kỳ coinjoin từ PC quen thuộc của bạn. Đối với người dùng RoninDojo, bước này không cần thiết vì việc quản lý coinjoins có thể được thực hiện trực tiếp qua giao diện web trong `Ứng dụng > Whirlpool`. Tuy nhiên, nếu bạn đang sử dụng một giải pháp "node-in-box" Bitcoin khác, việc cài đặt này là bắt buộc.
![coinjoin](assets/notext/28.webp)
Truy cập vào máy tính cá nhân của bạn và tải xuống phần mềm Whirlpool từ trang web chính thức của Samourai Wallet, chọn phiên bản phù hợp với hệ điều hành của bạn.

![coinjoin](assets/notext/29.webp)

Trước khi khởi chạy Whirlpool GUI, cần phải cài đặt JAVA 8 hoặc phiên bản cao hơn trên máy của bạn. Để làm điều này, [bạn có thể cài đặt OpenJDK](https://adoptium.net/).
![coinjoin](assets/notext/30.webp)
Cũng cần phải có Tor Daemon hoặc Tor Browser hoạt động ở chế độ nền trên máy tính của bạn. Hãy chắc chắn khởi động Tor trước mỗi phiên sử dụng Whirlpool GUI. Nếu Tor chưa được cài đặt trên máy của bạn, [bạn có thể tải xuống và cài đặt nó từ trang web chính thức của dự án](https://www.torproject.org/download/), sau đó chắc chắn khởi chạy nó ở chế độ nền.

![coinjoin](assets/notext/31.webp)

Một khi JDK đã được cài đặt trên hệ thống của bạn và Tor được khởi chạy ở chế độ nền, bạn có thể bắt đầu Whirlpool GUI.

![coinjoin](assets/notext/32.webp)

Từ Whirlpool GUI, nhấn vào `Nâng cao: CLI từ xa` để kết nối Whirlpool CLI của bạn với Dojo. Bạn sẽ cần địa chỉ Tor của Whirlpool CLI của mình.

![coinjoin](assets/notext/33.webp)

Để tìm địa chỉ Tor trên Umbrel và các giải pháp "node-in-box" khác, chỉ cần khởi động ứng dụng Samourai Server hoặc Dojo (tên có thể thay đổi tùy theo phần mềm được sử dụng). Địa chỉ Tor sẽ được hiển thị trực tiếp trên trang của ứng dụng.
![coinjoin](assets/notext/34.webp)
Trong Whirlpool GUI, nhập địa chỉ Tor bạn đã nhận được trước đó vào trường `Địa chỉ CLI`. Giữ nguyên tiền tố `http://`, nhưng không thêm cổng `:8899` ở cuối. Chỉ dán địa chỉ như bạn được cung cấp.
![coinjoin](assets/notext/35.webp)
Trong trường Tor Proxy, nhập `socks5://127.0.0.1:9050` nếu bạn đang sử dụng Tor Daemon, hoặc `socks5://127.0.0.1:9150` nếu bạn sử dụng Tor Browser. Khi bạn kết nối lần đầu tiên với Whirlpool CLI qua Whirlpool GUI, bạn có thể để trống trường khóa API. Nếu đây không phải là lần kết nối đầu tiên của bạn, vui lòng nhập khóa API của bạn vào không gian dành riêng. Khóa này có thể được tìm thấy trên cùng một trang với địa chỉ Tor của bạn.
![coinjoin](assets/notext/36.webp)

Sau khi bạn đã điền đầy đủ, nhấn vào nút `Connect`. Vui lòng đợi, việc kết nối có thể mất vài phút.

![coinjoin](assets/notext/37.webp)

### Ghép nối ví Samourai của bạn với Whirlpool GUI
*Đối với người dùng RoninDojo, bạn có thể tiếp tục hướng dẫn tại đây.*

Bây giờ chúng ta sẽ ghép nối ví Samourai mà chúng ta đã cấu hình trước đó với phần mềm Whirlpool GUI, hoặc trực tiếp với RoninDojo cho những ai sử dụng phần mềm này. Dù bạn đang sử dụng Whirlpool GUI hay RoninDojo, bạn sẽ được yêu cầu dán hoặc quét thông tin ghép nối của ví Samourai của bạn.

![coinjoin](assets/notext/38.webp)

Để tìm thông tin này, vào cài đặt ví của bạn.

![coinjoin](assets/notext/39.webp)

Nhấn vào `Transactions`, sau đó nhấn vào `Pair to Whirlpool GUI`.

![coinjoin](assets/notext/40.webp)

Samourai sau đó sẽ cung cấp cho bạn thông tin cần thiết để thiết lập kết nối. Hãy cẩn thận, dữ liệu này rất nhạy cảm! Bạn có thể chuyển nó sang PC của mình bằng cách sao chép trực tiếp hoặc quét mã QR hiển thị, sử dụng webcam của máy tính sau khi nhấn vào biểu tượng mã QR.

![coinjoin](assets/notext/41.webp)

Sau khi thực hiện thao tác này, trong Whirlpool GUI, chọn `Initialize GUI`. Vui lòng đợi, vì bước này có thể mất một chút thời gian.

![coinjoin](assets/notext/42.webp)

Dù bạn đang sử dụng Whirlpool GUI hay RoninDojo, bạn sẽ được yêu cầu nhập cụm từ bí mật của ví Samourai của bạn. Nhập nó vào trường dành riêng, sau đó nhấn nút `Login` để tiếp tục.

![coinjoin](assets/notext/43.webp)

Sau đó, bạn sẽ đến trang chủ của Whirlpool CLI

![coinjoin](assets/notext/44.webp)

### Khởi tạo coinjoins từ Whirlpool GUI
*Đối với người dùng RoninDojo, quy trình cần thực hiện giống hệt. Giao diện ứng dụng Whirlpool tích hợp trong RoninDojo cung cấp các tùy chọn và chức năng giống như phần mềm Whirlpool GUI trên máy tính để bàn. Do đó, bạn có thể theo dõi các hướng dẫn này một cách tương tự.*
Bây giờ khi mọi thứ đã được thiết lập, bạn đã sẵn sàng để bắt đầu trộn bitcoins của mình. Để làm điều này, chuyển bitcoins mà bạn muốn trộn vào tài khoản **Deposit** của ví Samourai của bạn. Thao tác này có thể được thực hiện trực tiếp qua ứng dụng ví Samourai hoặc trên Whirlpool GUI. Từ trang chính, nhấn vào nút `+ Deposit` ở góc trên bên trái.

![coinjoin](assets/notext/45.webp)
Giao diện người dùng Whirlpool sẽ tạo một địa chỉ nhận. Nó cũng sẽ hiển thị số tiền tối thiểu cần thiết để tham gia vào mỗi nhóm coinjoin. Số lượng này thay đổi tùy thuộc vào thị trường phí. Bạn nên gửi một lượng tiền cao hơn một chút so với số tiền tối thiểu yêu cầu, vì nếu phí khai thác không giảm, UTXO của bạn có thể không được chấp nhận vào nhóm mong muốn. Do đó, hãy gửi bitcoin của bạn đến địa chỉ được cung cấp. Để nhận một địa chỉ mới, chỉ cần nhấp vào nút `Renew address`.

![coinjoin](assets/notext/46.webp)

Một khi khoản tiền gửi được xác nhận, bạn sẽ thấy nó xuất hiện trong tài khoản **Deposit** trên giao diện người dùng Whirlpool.

![coinjoin](assets/notext/47.webp)

Để bắt đầu các chu kỳ coinjoin, chọn các UTXO bạn muốn trộn và nhấn nút `Premix`. Hãy cẩn thận: nếu bạn chọn nhiều UTXO khác nhau cùng một lúc, chúng sẽ được kết hợp trong giao dịch chuẩn bị `TX0`. Việc kết hợp này có thể dẫn đến giảm bảo mật riêng tư, đặc biệt nếu các UTXO đến từ các nguồn khác nhau, do Heuristic Sở Hữu Đầu Vào Chung (CIOH).

![coinjoin](assets/notext/48.webp)

Trang cấu hình Whirlpool mở ra. Bạn có thể chọn nhóm bạn muốn tham gia. Cũng chọn phí khai thác dành cho `TX0` và các coinjoin đầu tiên. Ở cuối trang này, một bảng tóm tắt sẽ trình bày cho bạn số lượng tiền thay đổi doxxic cũng như số lượng và số UTXO sẽ được cân bằng và bao gồm trong các chu kỳ coinjoin. Nếu bạn hài lòng với cấu hình này, nhấn nút `Premix` để bắt đầu các chu kỳ coinjoin.
![coinjoin](assets/notext/49.webp)

Một khi `TX0` được tạo, bạn sẽ có thể thấy các UTXO của mình đã được cân bằng trong tài khoản **Premix**, chờ xác nhận. Để cho phép tiền của bạn tự động remix 24 giờ một ngày, 7 ngày một tuần, tôi khuyên bạn nên kích hoạt tùy chọn `Automatically mix premix & postmix`. Bạn sẽ tìm thấy tính năng này trong tab `Configuration`, nằm ở bên trái cửa sổ giao diện người dùng Whirlpool của bạn.
![coinjoin](assets/notext/50.webp)
Sau khi bắt đầu các coinjoins, bạn có thể thoát khỏi giao diện người dùng Whirlpool cũng như Samourai Wallet. Chỉ cần node của bạn cần phải kết nối để có thể tham gia vào các coinjoin liên tục. Tuy nhiên, bạn nên kiểm tra định kỳ tiến trình của các chu kỳ coinjoin của mình. Nếu bạn nhận thấy rằng các UTXO của mình không còn được chọn cho một coinjoin trong một thời gian, điều này có thể chỉ ra một lỗi. Trong trường hợp này, hãy đến Whirlpool CLI và chọn `Start` để khởi động lại khả năng sẵn sàng của bạn cho các coinjoin.

![coinjoin](assets/notext/51.webp)

Các UTXO đã trộn của bạn có thể được nhìn thấy từ tài khoản **Postmix** trên giao diện người dùng Whirlpool. Ngoài ra, bạn có tùy chọn xem và chi tiêu chúng trực tiếp qua giao diện Whirlpool trên Samourai Wallet của bạn. Để truy cập menu này, nhấp vào biểu tượng `+` màu xanh ở dưới cùng của màn hình, sau đó chọn `Whirlpool`.

![coinjoin](assets/notext/52.webp)

Các tài khoản Whirlpool dễ dàng được nhận diện trên Samourai Wallet bởi màu xanh của chúng. Điều này cho phép bạn chi tiêu các UTXO đã trộn của mình từ bất cứ đâu và vào bất kỳ lúc nào, trực tiếp từ điện thoại thông minh của bạn.

![coinjoin](assets/notext/53.webp)
Để theo dõi các giao dịch coinjoin tự động của bạn, tôi cũng khuyên bạn nên thiết lập một ví chỉ xem thông qua ứng dụng Sentinel. Thêm ZPUB của tài khoản **Postmix** của bạn và theo dõi tiến trình của các chu kỳ coinjoin của bạn theo thời gian thực. Nếu bạn muốn hiểu cách sử dụng Sentinel, tôi khuyên bạn nên tham khảo hướng dẫn khác này trên PlanB Network: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)