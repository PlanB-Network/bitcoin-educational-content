---
name: Remix - Whirlpool
description: Số lần remix cần thực hiện trên Whirlpool là bao nhiêu?
---
![cover remix- wp](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, Công cụ Thống kê Whirlpool không còn có sẵn để tải xuống, vì nó được lưu trữ trên Gitlab của Samourai. Ngay cả khi bạn đã tải công cụ này về máy tính của mình trước đó, hoặc nó đã được cài đặt trên nút RoninDojo của bạn, WST sẽ không hoạt động vào thời điểm này. Nó phụ thuộc vào dữ liệu được cung cấp bởi OXT.me cho hoạt động của mình, và trang web này không còn truy cập được. Hiện tại, WST không đặc biệt hữu ích vì giao thức Whirlpool đang không hoạt động. Tuy nhiên, vẫn có khả năng các phần mềm này có thể được khôi phục trong những tuần tới. Hơn nữa, phần lý thuyết của bài viết này vẫn còn liên quan để hiểu các nguyên tắc và mục tiêu của coinjoins nói chung (không chỉ Whirlpool), cũng như hiểu về hiệu quả của mô hình Whirlpool. Bạn cũng có thể học cách định lượng sự riêng tư được cung cấp bởi các chu kỳ coinjoin.*

_Chúng tôi đang ch closely theo dõi các phát triển của vụ án này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này được cung cấp chỉ cho mục đích giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng các công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ các luật pháp trong phạm vi quyền hạn của họ._

---

> *"Phá vỡ liên kết mà đồng tiền của bạn để lại phía sau"*

Đây là câu hỏi mà tôi thường xuyên được hỏi. **Khi thực hiện coinjoins với Whirlpool, cần thực hiện bao nhiêu lần remix để đạt được kết quả thỏa đáng?**

Mục đích của coinjoin là cung cấp khả năng phủ nhận hợp lý bằng cách trộn đồng tiền của bạn với một nhóm các đồng tiền không thể phân biệt được. Mục tiêu của hành động này là để phá vỡ các liên kết theo dõi, cả từ quá khứ đến hiện tại và từ hiện tại trở về quá khứ. Nói cách khác, một nhà phân tích biết giao dịch ban đầu của bạn tại điểm nhập của các chu kỳ coinjoin không nên có thể xác định chắc chắn UTXO của bạn tại điểm thoát của các chu kỳ remix (phân tích từ chu kỳ nhập đến chu kỳ thoát).
![past-present links diagram](assets/en/1.webp)

Ngược lại, một nhà phân tích biết UTXO của bạn tại điểm thoát của các chu kỳ coinjoin không nên có thể xác định giao dịch gốc tại điểm nhập của các chu kỳ (phân tích từ chu kỳ thoát đến chu kỳ nhập).
![present-past links diagram](assets/en/2.webp)
Tuy nhiên, số lần remix không phải là tiêu chí đáng tin cậy để đánh giá khó khăn mà một nhà phân tích có thể gặp phải trong việc thiết lập các liên kết giữa quá khứ và hiện tại, hoặc ngược lại. Một chỉ số liên quan hơn sẽ là kích thước của các nhóm mà đồng tiền của bạn đang ẩn náu. Các chỉ số này được gọi là "anonsets". Trong trường hợp của Whirlpool, có hai loại anonsets.

Đầu tiên, chúng ta có thể xác định kích thước của nhóm nơi UTXO của bạn được ẩn tại điểm thoát của các chu kỳ coinjoin, tức là, số lượng đồng tiền không thể phân biệt được hiện diện trong nhóm này.
![probable UTXOs at exit](assets/en/3.webp)
Chỉ số này, được gọi là "prospective anonset" trong tiếng Pháp, "forward anonset" trong tiếng Anh, hay "chỉ số nhìn về tương lai", cho phép chúng ta đánh giá khả năng chống lại việc phân tích đường đi của đồng tiền của bạn từ khi nhập vào cho đến khi thoát ra khỏi các chu kỳ coinjoin. Chỉ số này ước lượng mức độ mà UTXO của bạn được bảo vệ chống lại các nỗ lực tái tạo lịch sử của nó từ điểm nhập vào đến điểm thoát ra trong quá trình coinjoin. Ví dụ, nếu giao dịch của bạn tham gia vào chu kỳ coinjoin đầu tiên và sau đó có thêm hai chu kỳ phía dưới được thực hiện, prospective anonset của đồng tiền của bạn sẽ là `13`: ![forward anonset](assets/en/4.webp)
Thứ hai, một chỉ số khác có thể được tính toán để đánh giá khả năng chống lại phân tích từ hiện tại về quá khứ của đồng tiền của bạn. Bằng cách biết UTXO của bạn ở cuối các chu kỳ, chỉ số này xác định số lượng giao dịch Tx0 tiềm năng có thể đã tạo thành đầu vào của bạn trong các chu kỳ coinjoin (phân tích từ cuối đến đầu của các chu kỳ). Chỉ số này đo lường mức độ khó khăn cho một nhà phân tích khi truy tìm nguồn gốc của đồng tiền của bạn sau khi nó đã trải qua coinjoins. ![Nguồn có thể tại đầu vào](assets/en/5.webp)
Tên của chỉ số này là "backward anonset" hoặc "chỉ số nhìn về quá khứ". Trong tiếng Pháp, tôi thích gọi nó là "anonset rétrospectif". Trong sơ đồ dưới đây, điều này tương ứng với tất cả các bong bóng Tx0 màu cam:
![backward anonset](assets/en/6.webp)
Để tìm hiểu thêm về phương pháp tính toán cho các chỉ số này, tôi khuyên bạn đọc [chuỗi tweet của tôi](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) về chủ đề này. Chúng tôi cũng đang chuẩn bị một bài viết toàn diện hơn về Mạng PlanB.

Tôi nhận thức được rằng câu trả lời cung cấp có thể không làm bạn hài lòng vì bạn hy vọng có một số lượng cụ thể về remixes, và tôi đang hướng dẫn bạn đến tài liệu. Lý do cho điều này là số lượng remixes là một chỉ số không đáng tin cậy để đánh giá sự ẩn danh đạt được trong các chu kỳ coinjoin. Do đó, không thể xác định một số lượng cố định của remixes như một ngưỡng bảo mật tuyệt đối và phổ quát.

Thật đúng là mỗi lần remix thêm của đồng tiền của bạn tăng cường bộ ẩn danh của nó. Tuy nhiên, điều quan trọng cần hiểu là chủ yếu là các remixes được thực hiện bởi các đồng nghiệp của bạn góp phần vào sự tăng trưởng của prospective anonset của bạn. Với mô hình Whirlpool, giao dịch của bạn có thể đạt được mức độ prospective anonset đáng kể chỉ với hai hoặc ba chu kỳ coinjoin, chỉ thông qua hoạt động của các đồng nghiệp tham gia vào các coinjoins trước đó.

Mặt khác, retrospective anonset không phải là mối quan tâm trong trường hợp của chúng ta. Thực tế, từ coinjoin ban đầu của bạn, bạn được thừa hưởng từ các giao dịch hồ bơi trước đó, ngay lập tức mang lại cho đồng tiền của bạn một backward anonset cao, với sự tăng nhẹ trong mỗi chu kỳ tiếp theo.
Cũng quan trọng là phải hiểu rằng việc tạo ra khả năng chối bỏ hợp lý không bao giờ hoàn chỉnh. Nó phụ thuộc vào khả năng truy vết đồng tiền của bạn. Khả năng này giảm xuống khi kích thước của các nhóm che giấu nó tăng lên. Do đó, bạn nên điều chỉnh mục tiêu của mình về anonsets tùy thuộc vào kỳ vọng cá nhân của bạn. Hãy tự hỏi về những lý do khiến bạn sử dụng coinjoins và các mức độ ẩn danh cần thiết để đạt được những mục tiêu này. Ví dụ, nếu việc sử dụng coinjoins chỉ nhằm mục đích bảo vệ sự riêng tư của ví của bạn khi gửi một số sats nhỏ cho cháu đỡ đầu của bạn nhân dịp sinh nhật, thì mức độ ẩn danh rất cao không cần thiết. Cháu bạn có lẽ không thể thực hiện phân tích chuỗi sâu, và ngay cả khi họ có thể, hậu quả đối với cuộc sống của bạn cũng không phải là thảm họa. Tuy nhiên, nếu bạn là mục tiêu của một chế độ độc tài, nơi mà thông tin nhỏ nhất cũng có thể dẫn đến việc bị giam giữ, hành động của bạn sẽ cần được hướng dẫn bởi những tiêu chí nghiêm ngặt hơn nhiều.

Để xác định những chỉ số anonset nổi tiếng này, bạn có thể sử dụng một công cụ Python gọi là **WST** (Whirlpool Stats Tool).

Tuy nhiên, không phải lúc nào bạn cũng cần tính toán anonsets cho từng đồng tiền của bạn đã coinjoin. Thiết kế của Whirlpool bản thân nó đã cung cấp cho bạn những bảo đảm. Như đã đề cập trước đó, anonset hồi tưởng hiếm khi là một mối quan tâm. Từ lần trộn đầu tiên của bạn, bạn đã nhận được một điểm số hồi tưởng đặc biệt cao. Đối với anonset tiềm năng, bạn chỉ cần giữ đồng tiền của mình trong tài khoản sau trộn một thời gian đủ dài. Ví dụ, dưới đây là điểm số anonset của một trong những đồng tiền `100,000 sats` của tôi sau khi dành hai tháng trong bể coinjoin:
![WST anonsets](assets/en/7.webp)
Nó hiển thị một điểm số hồi tưởng là `34,593` và một điểm số tiềm năng là `45,202`. Cụ thể, điều này có nghĩa là hai điều:
- Nếu một nhà phân tích biết đồng tiền của tôi ở cuối các chu kỳ và cố gắng truy vết nguồn gốc của nó, họ sẽ gặp phải `34,593` nguồn tiềm năng, mỗi nguồn có khả năng bằng nhau là của tôi.
- Nếu một nhà phân tích biết đồng tiền của tôi ở đầu các chu kỳ và cố gắng xác định sự tương ứng của nó ở cuối, họ sẽ đối mặt với `45,202` UTXOs tiềm năng, mỗi UTXO có cùng khả năng là của tôi.
Đó là lý do tại sao tôi coi việc sử dụng Whirlpool là đặc biệt liên quan trong một chiến lược `Hodl -> Mix -> Spend -> Replace`. Theo ý kiến của tôi, cách tiếp cận hợp lý nhất là giữ phần lớn tiền tiết kiệm của mình bằng bitcoin trong một ví lạnh, trong khi liên tục duy trì một số lượng nhất định của đồng tiền trong coinjoin trên Samourai để chi trả cho các chi phí hàng ngày. Một khi các bitcoin từ các coinjoins được chi tiêu, chúng được thay thế bằng những đồng mới để trở lại ngưỡng định nghĩa của đồng tiền đã trộn. Phương pháp này cho phép chúng ta tự do khỏi lo lắng về anonsets của UTXOs của mình, đồng thời làm cho thời gian cần thiết cho coinjoins trở nên hiệu quả ít hạn chế hơn.

Tôi hy vọng câu trả lời này đã làm sáng tỏ mô hình Whirlpool. Nếu bạn muốn tìm hiểu thêm về cách coinjoins hoạt động trên Bitcoin, tôi khuyên bạn đọc bài viết tổng hợp của tôi về chủ đề này:

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**Nguồn tài liệu bên ngoài:**
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
Vui lòng tuân thủ các hướng dẫn sau để đảm bảo một bản dịch chất lượng cao:

- **Ngôn Ngữ Gốc**: Nội dung ban đầu được viết bằng tiếng Anh.
- **Bản Chất Nội Dung**: Bạn sẽ gặp phải tài liệu kỹ thuật, có thể bao gồm thuật ngữ đặc thù của ngành.
- **Liên Kết & Thuật Ngữ Kỹ Thuật**: Không dịch các URL hoặc thuật ngữ kỹ thuật cực kỳ đặc thù. Nếu không chắc chắn, giữ nguyên thuật ngữ gốc.
- **Tính Nhất Quán về Định Dạng**: Duy trì cùng một bố cục markdown và định dạng như văn bản gốc. Sự nhất quán của cấu trúc là rất quan trọng.
- **Thuộc Tính YML**: Nếu một dòng bắt đầu với một thuộc tính YAML (ví dụ, 'name:', 'goal:', 'objectives:'), giữ nguyên tên thuộc tính bằng tiếng Anh.
- **Bối Cảnh Văn Hóa**: Đối với các tham chiếu văn hóa hoặc bối cảnh cụ thể có thể không dịch trực tiếp, diễn giải để bảo toàn ý định ban đầu hoặc cung cấp một giải thích ngắn gọn.
- **Điểm nhấn nên được đặt vào việc duy trì tính toàn vẹn của nội dung kỹ thuật trong khi đảm bảo bản dịch dễ hiểu và chính xác về bối cảnh trong tiếng Việt.**

Dựa trên các hướng dẫn trên, bản dịch của yêu cầu không thể được thực hiện vì không có nội dung cụ thể từ các liên kết được cung cấp để dịch. Hãy cung cấp nội dung cụ thể hoặc một yêu cầu dịch khác mà không yêu cầu truy cập vào các liên kết.