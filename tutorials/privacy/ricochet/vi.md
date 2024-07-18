---
name: Ricochet
description: Hiểu và sử dụng giao dịch Ricochet
---
![cover ricochet](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, công cụ Ricochet không còn khả dụng. Tuy nhiên, có khả năng công cụ này có thể được khôi phục trong những tuần tới. Trong thời gian chờ đợi, bạn chỉ có thể thực hiện Ricochet một cách thủ công. Phần lý thuyết của bài viết này vẫn còn liên quan để hiểu cách hoạt động và học cách thực hiện nó một cách thủ công.*

_Chúng tôi đang theo dõi sát sao các diễn biến của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này chỉ mang tính chất giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích sử dụng các công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ luật pháp tại quốc gia của họ._

---

> *"Một công cụ cao cấp thêm các bước chuyển tiếp giả tạo vào giao dịch của bạn. Làm mờ danh sách đen và giúp bảo vệ chống lại việc đóng cửa tài khoản bất công từ bên thứ ba."*

## Ricochet là gì?
Ricochet là một kỹ thuật bao gồm việc thực hiện nhiều giao dịch giả tạo cho chính mình nhằm mô phỏng việc chuyển giao quyền sở hữu bitcoin. Công cụ này khác với các giao dịch Samourai khác vì nó không cung cấp tính ẩn danh tiềm năng, mà là một dạng của tính ẩn danh hồi tưởng. Ricochet giúp làm mờ các đặc điểm có thể làm ảnh hưởng đến tính chất không thể phân biệt của một đồng Bitcoin.

Ví dụ, nếu bạn thực hiện một coinjoin, đầu ra coin của bạn từ việc trộn sẽ được xác định như vậy. Các công cụ phân tích chuỗi khối có thể phát hiện các mô hình của giao dịch coinjoin và gắn nhãn cho các đồng tiền đi ra từ chúng. Thực tế, coinjoin nhằm mục đích phá vỡ các liên kết lịch sử của một đồng tiền, nhưng việc nó đi qua coinjoins vẫn có thể được phát hiện. Để làm một phép so sánh, hiện tượng này giống như việc mã hóa một văn bản: mặc dù chúng ta không thể truy cập vào văn bản gốc, nhưng có thể dễ dàng nhận biết rằng mã hóa đã được áp dụng.

Cụ thể, nhãn "đồng tiền đầu ra coinjoin" này có thể ảnh hưởng đến tính chất không thể phân biệt của một UTXO. Các thực thể được quản lý, như các nền tảng giao dịch, có thể từ chối chấp nhận một UTXO đã trải qua coinjoin, hoặc thậm chí yêu cầu giải thích từ chủ sở hữu, với rủi ro bị khóa tài khoản hoặc đóng băng tài sản. Trong một số trường hợp, nền tảng thậm chí có thể báo cáo hành vi của bạn cho các cơ quan nhà nước.

Đây là nơi phương pháp Ricochet được áp dụng. Để làm mờ dấu vết để lại bởi coinjoin, Ricochet thực hiện bốn giao dịch liên tiếp nơi người dùng chuyển tiền của họ cho chính họ trên các địa chỉ khác nhau. Sau chuỗi giao dịch này, công cụ Ricochet cuối cùng chuyển bitcoin đến điểm đến cuối cùng của chúng, chẳng hạn như một nền tảng giao dịch. Mục tiêu là tạo khoảng cách giữa giao dịch coinjoin ban đầu và hành động chi tiêu cuối cùng. Theo cách này, các công cụ phân tích chuỗi khối sẽ nghĩ rằng có lẽ đã có một sự chuyển giao quyền sở hữu sau coinjoin, và do đó không cần thiết phải hành động chống lại người gửi.
![ricochet diagram](assets/en/1.webp)
Trước phương pháp Ricochet, người ta có thể tưởng tượng rằng phần mềm phân tích chuỗi sẽ mở rộng việc kiểm tra của họ vượt qua bốn lần chuyển tiếp. Tuy nhiên, các nền tảng này đối mặt với một bài toán khó trong việc tối ưu hóa ngưỡng phát hiện. Họ phải thiết lập một giới hạn về số lần chuyển tiếp sau đó họ thừa nhận rằng một sự thay đổi quyền sở hữu có khả năng đã xảy ra và rằng liên kết với một coinjoin trước đó nên được bỏ qua. Tuy nhiên, việc xác định ngưỡng này là rủi ro: mỗi lần mở rộng số lần chuyển tiếp quan sát được tăng lên theo cấp số nhân khối lượng của các kết quả dương tính giả, tức là, những cá nhân bị đánh dấu nhầm là tham gia vào một coinjoin, khi thực tế hoạt động đó được thực hiện bởi người khác. Kịch bản này đặt ra một rủi ro lớn cho các công ty này, vì kết quả dương tính giả dẫn đến sự không hài lòng, có thể khiến khách hàng bị ảnh hưởng chuyển sang đối thủ cạnh tranh. Về lâu dài, một ngưỡng quá tham vọng khiến một nền tảng mất nhiều khách hàng hơn so với đối thủ của mình, có thể đe dọa đến sự tồn tại của nó. Do đó, việc tăng số lần chuyển tiếp quan sát được là phức tạp đối với các nền tảng này, và 4 thường là một con số đủ để chống lại phân tích của họ.
Như vậy, **trường hợp sử dụng phổ biến nhất cho Ricochet xuất hiện khi cần che giấu sự tham gia trước đó trong một coinjoin trên một UTXO thuộc về bạn**. Lý tưởng nhất là tránh chuyển bitcoin đã trải qua coinjoin cho các thực thể được quản lý. Tuy nhiên, trong trường hợp không có lựa chọn khác, đặc biệt trong tình huống cần chuyển đổi bitcoin thành tiền tệ fiat gấp, Ricochet cung cấp một giải pháp hiệu quả.

## Ricochet hoạt động như thế nào trên Samourai Wallet?
Ricochet đơn giản là một phương pháp mà người ta gửi bitcoin cho chính mình. Do đó, hoàn toàn có thể mô phỏng thủ công một Ricochet mà không cần sử dụng công cụ chuyên biệt. Tuy nhiên, đối với những người muốn tự động hóa quy trình trong khi hưởng lợi từ một kết quả tinh xảo hơn, công cụ Ricochet có sẵn thông qua ứng dụng Samourai Wallet là một giải pháp tốt.

Vì dịch vụ này được trả phí trên Samourai, một Ricochet sẽ tốn một khoản phí dịch vụ là `100,000 sats`, ngoài phí khai thác. Do đó, việc sử dụng nó được khuyến nghị hơn cho các giao dịch có số lượng lớn.

Ứng dụng Samourai cung cấp hai biến thể của Ricochet:
- Ricochet Củng cố, hay "giao hàng chia lớp", mang lại lợi ích là phân tán phí dịch vụ Samourai qua năm giao dịch liên tiếp. Tùy chọn này cũng đảm bảo rằng mỗi giao dịch được phát sóng vào một thời điểm riêng biệt và được ghi lại trong một khối khác nhau, mô phỏng chặt chẽ hành vi của sự thay đổi quyền sở hữu. Mặc dù chậm hơn, phương pháp này được ưa chuộng hơn cho những ai không vội, vì nó tối đa hóa hiệu quả của Ricochet bằng cách tăng cường khả năng chống lại phân tích chuỗi.
- Ricochet Cổ điển, được thiết kế để thực hiện hoạt động nhanh chóng bằng cách phát sóng tất cả các giao dịch trong một khoảng thời gian ngắn. Do đó, phương pháp này cung cấp ít quyền riêng tư và khả năng chống phân tích thấp hơn so với phương pháp củng cố. Nó chỉ nên được ưu tiên cho các chuyển giao khẩn cấp.

## Cách Thực Hiện Ricochet trên Samourai Wallet?
Để thực hiện một giao dịch Ricochet từ ứng dụng Samourai Wallet, hãy theo dõi hướng dẫn video của chúng tôi:
![Hướng dẫn video Ricochet trên YouTube](https://youtu.be/Gsz0zuVo3N4)

Nếu bạn muốn nghiên cứu các giao dịch Ricochet được thực hiện trong hướng dẫn này, đây là chúng:
- Giao dịch Ricochet đầu tiên: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://mempool.space/fr/testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Giao dịch Ricochet cuối cùng: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://mempool.space/fr/testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)
**Tài Nguyên Bên Ngoài:**
- https://docs.samourai.io/en/wallet/features/ricochet