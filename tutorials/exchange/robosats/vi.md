---
name: Robosats

description: Hướng dẫn sử dụng Robosats
---

![cover](assets/cover.webp)

RoboSats (https://learn.robosats.com/) là một cách dễ dàng để trao đổi Bitcoin với các đồng tiền quốc gia một cách riêng tư. Nó đơn giản hóa trải nghiệm ngang hàng và sử dụng hóa đơn giữ chỗ trên Lightning để giảm thiểu yêu cầu về quản lý và tin cậy.

![video](https://youtu.be/XW_wzRz_BDI)

## Hướng dẫn

> Hướng dẫn này được lấy từ Bitocin Q&A ( https://bitcoiner.guide/robosats/). Mọi công lao thuộc về anh ấy, hãy ủng hộ anh ấy tại đây (https://bitcoiner.guide/contribute); BitcoinQ&A cũng là một người hướng dẫn về bitcoin. Liên hệ với anh ấy để được hướng dẫn!

![image](assets/0.webp)

RoboSats - Một sàn giao dịch P2P dựa trên Lightning đơn giản và riêng tư

## Trước khi bạn bắt đầu

### Những điều bạn cần biết

| Thuật ngữ       | Định nghĩa                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Danh tính giao dịch riêng tư tự động được tạo. Không sử dụng cùng một robot nhiều lần vì điều này có thể làm giảm quyền riêng tư của bạn.                                                             |
| Token        | Một chuỗi ký tự ngẫu nhiên được sử dụng để tạo robot độc đáo của bạn.                                                                                                                              |
| Maker        | Người dùng tạo ra một lời đề nghị mua hoặc bán Bitcoin.                                                                                                                                            |
| Taker        | Người dùng chấp nhận lời đề nghị mua hoặc bán Bitcoin của người khác.                                                                                                                        |
| Bond         | Một lượng Bitcoin được cả hai bên khóa lại như một lời cam kết chơi công bằng và hoàn thành phần giao dịch của họ. Bond thường là 3% tổng số tiền giao dịch và được hỗ trợ bởi Hodl Invoices. |
| Trade Escrow | Được người bán sử dụng như một phương pháp giữ lượng Bitcoin của giao dịch, một lần nữa sử dụng Hodl Invoices.                                                                                              |
| Fees         | RoboSats thu phí 0.2% số tiền giao dịch, được chia cho cả maker và taker. Người taker trả 0.175% và người maker trả 0.025%.                                                       |

## Những thứ bạn cần có

### Một Ví Lightning

RoboSats là bản địa của Lightning, vì vậy bạn sẽ cần một Ví Lightning để tài trợ cho bond và nhận sats đã mua như một người mua. Bạn nên cẩn thận khi chọn ví của mình, do công nghệ được sử dụng để RoboSats hoạt động, không phải tất cả đều tương thích.

Nếu bạn là người chạy node, Zeus là lựa chọn tốt nhất. Nếu bạn không có node riêng, tôi rất khuyên dùng Phoenix, một ví di động đa nền tảng với cài đặt đơn giản và truy cập vào Lightning. Phoenix đã được sử dụng trong việc sản xuất hướng dẫn này.

### Một số Bitcoin

Người mua và người bán cần tài trợ cho một bond trước khi bất kỳ giao dịch nào có thể diễn ra. Đây thường là một lượng nhỏ (~3% số tiền giao dịch), nhưng dù sao cũng là một điều kiện tiên quyết.

Sử dụng RoboSats để mua sats đầu tiên của bạn? Tại sao không nhờ một người bạn cho bạn mượn một lượng nhỏ cần thiết để bắt đầu!? Nếu bạn tự mình, đây là một số lựa chọn tốt khác để có được một số sats không cần KYC để bắt đầu.

### Truy cập vào RoboSats

Rõ ràng bạn sẽ cần truy cập vào RoboSats! Có bốn cách chính bạn có thể làm điều này:

1. Qua Trình duyệt Tor (Khuyến nghị!)
2. Qua một trình duyệt web thông thường (Không khuyến nghị!)
3. Qua APK Android
4. Khách hàng của riêng bạn

Nếu bạn mới làm quen với trình duyệt Tor, tìm hiểu thêm và tải xuống [tại đây](https://www.torproject.org/download/).
Lưu ý nhanh cho người dùng iOS muốn truy cập RoboSats qua Tor từ điện thoại của họ. 'Onion Browser' không phải là Tor Browser. Thay vào đó, hãy sử dụng Orbot + Safari và Orbot + DuckDuckGo.

## Mua Bitcoin

Các bước sau đây được thực hiện vào tháng 5 năm 2023 sử dụng phiên bản 0.5.0, truy cập qua trình duyệt Tor. Các bước này nên giống hệt với người dùng truy cập RoboSats qua APK Android.

Tại thời điểm viết bài này, RoboSats vẫn đang trong quá trình phát triển tích cực, vì vậy giao diện có thể thay đổi một chút trong tương lai, nhưng các bước cơ bản cần thiết để hoàn thành giao dịch nên vẫn gần như không thay đổi.

> Khi bạn lần đầu tiên tải RoboSats, bạn sẽ thấy trang đầu này. Nhấp vào Start.

![image](assets/2.webp)

Tạo token của bạn và lưu trữ nó ở nơi an toàn như ứng dụng ghi chú được mã hóa hoặc trình quản lý mật khẩu. Token này có thể được sử dụng để khôi phục ID Robot tạm thời của bạn trong trường hợp trình duyệt hoặc ứng dụng của bạn đóng cửa giữa chừng giao dịch.

![image](assets/3.webp)

Gặp danh tính Robot mới của bạn, sau đó nhấp vào Continue.

![image](assets/4.webp)

Nhấp vào Offers để duyệt sổ lệnh. Ở đầu trang, bạn có thể lọc theo sở thích của mình. Hãy chắc chắn ghi chú về tỷ lệ phần trăm của khoản bảo đảm và phí bảo hiểm so với tỷ giá trung bình trên thị trường.

- Chọn Buy
- Chọn đồng tiền của bạn
- Chọn phương thức thanh toán của bạn

![image](assets/5.webp)

> Nhấp vào ưu đãi mà bạn muốn chọn. Nhập số tiền (bằng đồng tiền fiat bạn chọn) mà bạn muốn mua từ người bán, sau đó kiểm tra lại thông tin cuối cùng và nhấp vào Take Order.

Nếu người bán không trực tuyến (được biểu thị bằng một dấu chấm đỏ trên hình ảnh hồ sơ của họ), bạn sẽ thấy một cảnh báo rằng giao dịch có thể mất nhiều thời gian hơn bình thường. Nếu bạn tiếp tục và người bán không tiến hành kịp thời, bạn sẽ được bồi thường 50% số tiền bảo đảm của họ cho thời gian lãng phí của bạn.

![image](assets/6.webp)

Tiếp theo, bạn cần phải khóa khoản bảo đảm giao dịch của mình bằng cách thanh toán hóa đơn trên màn hình. Đây là một hóa đơn giữ chỗ sẽ bị đóng băng trong ví của bạn. Nó chỉ được tính phí nếu bạn không hoàn thành phần giao dịch của mình.

![image](assets/7.webp)

Trong Ví Lightning của bạn, quét mã QR và thanh toán hóa đơn.

![image](assets/8.webp)

Tiếp theo, trong Ví Lightning của bạn, tạo một hóa đơn cho số tiền được hiển thị và dán vào không gian được cung cấp.

![image](assets/9.webp)

Chờ đợi người bán khóa số tiền giao dịch của họ. Khi điều này diễn ra, RoboSats sẽ tự động chuyển sang bước tiếp theo nơi cửa sổ trò chuyện sẽ mở ra. Nói Hi và yêu cầu người bán cung cấp thông tin thanh toán fiat của họ. Sau khi được cung cấp, gửi thanh toán qua phương thức đã chọn sau đó xác nhận điều này trong RoboSats. Tất cả cuộc trò chuyện trong RoboSats đều được mã hóa PGP nghĩa là chỉ có bạn và đối tác giao dịch của bạn mới có thể đọc được tin nhắn.

![image](assets/10.webp)

Một khi người bán xác nhận đã nhận được thanh toán, RoboSats tự động giải phóng thanh toán sử dụng hóa đơn được cung cấp trước đó.

![image](assets/11.webp)

Khi hóa đơn được thanh toán, giao dịch kết thúc và khoản bảo đảm của bạn được mở khóa. Bạn sẽ thấy một bản tóm tắt giao dịch.

![image](assets/12.webp)

Kiểm tra Ví Lightning của bạn để xác nhận rằng sats đã đến.

![image](assets/13.webp)

## Tính năng bổ sung

Ngoài việc mua và bán Bitcoin rõ ràng, RoboSats còn có một số tính năng khác bạn nên biết.
Robot Garage
Muốn thực hiện nhiều giao dịch cùng một lúc nhưng không muốn chia sẻ cùng một danh tính cho tất cả? Không vấn đề gì! Nhấp vào tab Robot, tạo thêm một Robot và tạo hoặc nhận lệnh tiếp theo của bạn.
![image](assets/14.webp)

### Tạo Lệnh

Ngoài việc nhận lời đề nghị của người khác, bạn cũng có thể tự tạo lời đề nghị của mình và chờ đợi một Robot khác tìm đến bạn.

- Mở trang Tạo lệnh.
- Xác định lệnh của bạn là mua hay bán Bitcoin.
- Nhập số lượng và loại tiền tệ bạn muốn Mua/Bán.
- Nhập phương thức thanh toán bạn sẵn lòng sử dụng.
- Nhập % 'Phí trên Giá Thị Trường' bạn chấp nhận. Lưu ý rằng con số này có thể là một giá trị âm để đặt giá thấp hơn so với giá thị trường hiện tại.
- Nhấp Tạo Lệnh.
- Thanh toán hóa đơn Lightning để khóa Maker Bond của bạn.
- Lệnh của bạn giờ đây đã được kích hoạt. Hãy ngồi lại và chờ đợi ai đó chấp nhận nó.

![image](assets/15.webp)

### Thanh Toán On-chain

RoboSats tập trung vào Lightning, nhưng người mua có lựa chọn nhận sats vào địa chỉ Bitcoin on-chain của họ. Người mua có thể chọn lựa chọn này sau khi khóa bond của họ. Sau khi chọn on-chain, người mua sẽ thấy tổng quan về phí. Các phí bổ sung cho dịch vụ này bao gồm:

- Phí hoán đổi do RoboSats thu - Phí này là động và thay đổi tùy thuộc vào mức độ bận rộn của mạng Bitcoin.
- Phí khai thác cho giao dịch thanh toán - Người mua có thể cấu hình phí này.

![image](assets/16.webp)

### Giao Dịch P2P

RoboSats cho phép người dùng chuyển đổi sats vào hoặc ra khỏi Ví Lightning của họ. Chỉ cần nhấp vào nút hoán đổi ở đầu trang đề nghị để xem các lời đề nghị hoán đổi hiện tại.

Là người mua của lời đề nghị ‘Hoán Đổi Vào’, bạn gửi Bitcoin on-chain cho đối tác và nhận lại sats, trừ các phí và/hoặc phí bổ sung được quảng cáo, vào Ví Lightning của mình. Là người mua của lời đề nghị ‘Hoán Đổi Ra’, bạn gửi sats qua Lightning và nhận Bitcoin, trừ bất kỳ phí và/hoặc phí bổ sung nào, vào địa chỉ on-chain của mình. Người dùng ví Samourai hoặc Sparrow cũng có thể tận dụng tính năng Stowaway để hoàn thành một giao dịch hoán đổi.

Các lời đề nghị hoán đổi của RoboSats cũng có thể bao gồm các lựa chọn thay thế cho Bitcoin bao gồm RBTC, LBTC và WBTC. Bạn nên cực kỳ cẩn thận khi tương tác với các token này vì chúng đều đi kèm với các sự đánh đổi khác nhau. Bitcoin được ghim không phải là Bitcoin!

![image](assets/17.webp)

### Vận Hành Client RoboSats của Riêng Bạn

Người chạy nút Umbrel, Citadel và Start9 có thể cài đặt client RoboSats của riêng họ trực tiếp lên nút của họ. Lợi ích của việc làm như vậy bao gồm:

- Thời gian tải trang nhanh hơn đáng kể.
- An toàn hơn: bạn kiểm soát client ứng dụng RoboSats nào bạn chạy.
- Truy cập RoboSats một cách an toàn từ bất kỳ trình duyệt / thiết bị nào. Không cần sử dụng TOR nếu bạn đang ở trên mạng nội bộ hoặc sử dụng VPN: backend nút của bạn xử lý việc tor hóa cần thiết cho việc ẩn danh.
- Cho phép kiểm soát việc kết nối với trình điều phối thị trường P2P nào (mặc định là robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)

![image](assets/18.webp)

## Câu Hỏi Thường Gặp

### Tôi có thể bị lừa đảo không?
Là người mua, nếu bạn đã gửi số tiền fiat cần thiết cho phần giao dịch của mình, nhưng người bán không giải phóng sats cho bạn thì bạn có thể mở một tranh chấp. Nếu trong quá trình tranh chấp này bạn có thể chứng minh với các trọng tài RoboSats rằng bạn đã gửi tiền fiat, số tiền escrow và khoản bảo lãnh giao dịch của người bán sẽ được giải phóng cho bạn. Làm thế nào để hủy một giao dịch?

Bạn có thể hủy một giao dịch sau khi đăng ký bảo lãnh của mình bằng cách nhấp vào nút Hủy Hợp Tác trong menu giao dịch. Nếu đối tác giao dịch của bạn đồng ý hủy, bạn sẽ không phải chịu bất kỳ phí nào. Nhưng nếu đối tác giao dịch của bạn muốn hoàn thành giao dịch và bạn vẫn tiếp tục hủy, bạn sẽ mất khoản bảo lãnh giao dịch của mình.

### RoboSats có hoạt động với phương thức thanh toán ‘X’ không?

RoboSats không hạn chế về phương thức thanh toán. Nếu bạn không thấy bất kỳ đề nghị nào với phương thức mong muốn của mình, hãy tạo đề nghị của riêng bạn sử dụng phương thức đó!

![hình ảnh](assets/19.webp)

### RoboSats biết gì về tôi khi tôi sử dụng nó?

Miễn là bạn sử dụng RoboSats qua Tor hoặc ứng dụng Android, không có gì cả! Tìm hiểu thêm tại đây.

- Tor bảo vệ sự riêng tư mạng của bạn.
- Mã hóa PGP giữ cho cuộc trò chuyện giao dịch của bạn được riêng tư.
- Không có tài khoản nghĩa là một Robot cho mỗi giao dịch. Điều này có nghĩa là RoboSats không thể liên kết nhiều giao dịch với một thực thể duy nhất.

Tuy nhiên, có một số điều cần lưu ý! Lightning khá riêng tư khi bạn là người gửi, nhưng không phải khi bạn là người nhận. Nếu bạn nhận qua node Lightning của riêng mình, ID node của bạn được chia sẻ trong hóa đơn của bạn. ID node này cung cấp cho bất kỳ ai biết nó một điểm bắt đầu để cố gắng liên kết hoạt động trên chuỗi của bạn. Điều này cũng đúng nếu người dùng chọn nhận giao dịch của họ qua thanh toán trên chuỗi.

Để giảm thiểu điều này, người dùng có thể chọn sử dụng một giải pháp như Ví Proxy cho Lightning hoặc Coinjoin cho thanh toán trên chuỗi.

### Liên minh

Hiện tại chỉ có một điều phối viên RoboSats duy nhất được vận hành bởi nhóm phát triển RoboSats. Trong Bitcoin, bất kỳ hình thức tập trung nào cũng tạo thành mục tiêu dễ dàng hơn cho chính phủ hoặc các cơ quan quản lý có thể không nhìn nhận tích cực về một dịch vụ cụ thể.

Với việc RoboSats là một dự án mã nguồn mở, bất kỳ ai cũng có thể lấy mã và bắt đầu vận hành điều phối viên của riêng họ. Mặc dù điều này phần nào giảm bớt rủi ro khỏi một mục tiêu duy nhất, nhưng cũng làm phân mảnh một thị trường thanh khoản đã mỏng.

Nhóm RoboSats nhận ra điều này và đã bắt đầu làm việc trên một mô hình liên minh. Là người dùng cuối, điều này không nên thay đổi quy trình giao dịch được trình bày ở trên nhiều lắm, nhưng sẽ có thêm các giao diện hoặc màn hình cho bạn để thêm hoặc loại bỏ các điều phối viên khác nhau xuất hiện.

KẾT thúc hướng dẫn
https://bitcoiner.guide/robosats/