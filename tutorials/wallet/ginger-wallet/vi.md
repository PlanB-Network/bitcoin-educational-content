---
name: Ginger Wallet
description: Phần mềm Bitcoin wallet tự quản, mã nguồn mở, fork từ Wasabi Wallet, tích hợp Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet là một danh mục đầu tư Bitcoin mã nguồn mở, không lưu ký, tập trung vào tính bảo mật và quyền riêng tư. Nó bắt đầu được phát triển từ fork của Wasabi Wallet (sau phiên bản 2.0.7.2 - giấy phép MIT).



Ginger Wallet vẫn giữ nguyên kiến trúc kỹ thuật của Wasabi nhưng bổ sung thêm một vài tính năng cụ thể. Theo [tài liệu về Ginger Wallet](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), Wasabi nhấn mạnh vào **tính tự chủ và khả năng kiểm soát**, trong khi Ginger tập trung vào **tính dễ sử dụng, bảo mật và trải nghiệm đơn giản hóa**, giúp những người ít am hiểu về kỹ thuật cũng có thể dễ dàng tiếp cận.



Ginger Wallet là phần mềm wallet chỉ dành cho máy tính (không có ứng dụng di động).



## Coinjoin là gì?



**coinjoin** là một cấu trúc giao dịch Bitcoin đặc biệt, tập hợp nhiều bên tham gia vào một giao dịch hợp tác duy nhất. Cơ chế này trộn lẫn các mục nhập của nhiều người dùng khác nhau vào một giao dịch chung, khiến việc theo dõi nguồn tiền trở nên cực kỳ khó khăn - nếu không muốn nói là thường xuyên bất khả thi, nếu được thực hiện đúng cách. Kết quả là, người quan sát bên ngoài gần như không thể xác định chắc chắn nguồn gốc và đích đến của số bitcoin liên quan, không giống như trong các giao dịch Bitcoin thông thường.



Với tư cách là người dùng, coinjoin giúp bảo vệ tính bảo mật của bạn. Ví dụ: nếu bạn nhận được khoản quyên góp 10.000 sats vào địa chỉ Bitcoin, người gửi có thể theo dõi số tiền này và, trong một số trường hợp, suy ra rằng bạn nắm giữ một lượng bitcoin lớn hơn, hoặc theo dõi các hoạt động của bạn. Việc thực hiện coinjoin sau khoản quyên góp 10.000 sats này đồng nghĩa với việc bạn đã phá vỡ khả năng theo dõi: người gửi sẽ không còn có thể lấy được bất kỳ thông tin nào về bạn từ khoản thanh toán này nữa.



Coinjoin Chaumian mang lại mức độ bảo mật cao, vì tiền luôn nằm dưới sự kiểm soát độc quyền của người dùng. Ngay cả người vận hành máy chủ điều phối cũng không thể chuyển hướng bitcoin của người tham gia trong bất kỳ trường hợp nào. Cả người dùng và người điều phối đều không cần tin tưởng lẫn nhau: mỗi bên đều nắm quyền kiểm soát khóa riêng của mình và chỉ được phép xác thực giao dịch. Do đó, không bên thứ ba nào có thể chiếm đoạt bitcoin của bạn trong quá trình coinjoin, cũng như không thể thiết lập liên kết trực tiếp giữa dữ liệu đầu vào và đầu ra của bạn.



Để tìm hiểu thêm về coinjoin, hãy xem khóa học BTC 204 của Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Cài đặt Ginger Wallet



Để cài đặt Ginger Wallet, hãy truy cập trang web [Ginger Wallet](https://gingerwallet.io).



Nhấn **Tải xuống** để tải xuống phiên bản phù hợp với máy tính của bạn (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Một lựa chọn khác là truy cập [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) của dự án để tải xuống.



![screen](assets/fr/04.webp)



Sau đó chạy chương trình cài đặt.



![screen](assets/fr/05.webp)




## Cài đặt tham số



### Cấu hình sơ bộ



Mở Ginger Wallet, chọn ngôn ngữ bạn muốn.



![screen](assets/fr/06.webp)



Ngay từ đầu, Ginger sẽ nhắc bạn về các chi phí liên quan đến quá trình coinjoin.



![screen](assets/fr/07.webp)



Sau đó nhấn **Bắt đầu**, rồi **Mới** để tạo danh mục đầu tư mới.



![screen](assets/fr/08.webp)



Tiếp theo, hãy lưu và xác nhận seedphrase của bạn.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Để tăng cường bảo mật, Ginger Wallet cung cấp cho bạn tùy chọn thêm passphrase.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sau khi thêm vào, passphrase sẽ được yêu cầu mỗi khi bạn truy cập vào danh mục đầu tư của mình.



![screen](assets/fr/12.webp)



Ginger sẽ tự động kích hoạt **Coinjoin** mặc định khi bạn tạo danh mục đầu tư. Bạn sẽ được thông báo về điều này và sau đó có thể tùy chỉnh cài đặt cho phù hợp với nhu cầu của mình.



![screen](assets/fr/13.webp)




### Cài đặt chung



Sau khi tạo xong danh mục đầu tư đầu tiên, bạn sẽ được chuyển đến giao diện Ginger Wallet.



![screen](assets/fr/14.webp)



Kích hoạt **Chế độ kín đáo** nếu bạn muốn ẩn số dư trong ví của mình.



![screen](assets/fr/15.webp)



Bạn có thể tạo nhiều danh mục đầu tư trên Ginger Wallet. Chỉ cần nhấp vào **Thêm danh mục đầu tư**.



![screen](assets/fr/16.webp)



Ginger hỗ trợ việc sử dụng danh mục phần cứng thông qua giao diện Bitcoin Core chuẩn, mặc dù khả năng tích hợp trực tiếp từ hoặc đến danh mục phần cứng vẫn chưa khả dụng.



Danh mục phần cứng tương thích bao gồm (nhưng không giới hạn ở):




- Blockstream Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- vân vân.



Bây giờ hãy nhấp vào **Cài đặt**.



![screen](assets/fr/17.webp)



Các thiết lập này là thiết lập chung của ứng dụng và cấu hình bạn thực hiện ở đó sẽ áp dụng cho tất cả danh mục đầu tư.



Trong **Cài đặt**, bạn có các tab:





- Tổng quan**



![screen](assets/fr/18.webp)





- Vẻ bề ngoài



Trong tab này, bạn có thể thay đổi ngôn ngữ, tiền tệ và đơn vị hiển thị phí (BTC/Satoshi), cùng nhiều tùy chọn khác.



![screen](assets/fr/19.webp)





- Bitcoin**



Tab này cho phép bạn kích hoạt Bitcoin Knots chạy khi khởi động ứng dụng, chọn mạng của bạn (Main/RegTest) và nhà cung cấp mức phí (Mempool Space/Blockstream info/Full Node), v.v.



![screen](assets/fr/20.webp)





- Các tính năng an toàn**



Trong tab Bảo mật, bạn có thể bật xác thực hai yếu tố, kích hoạt hoặc hủy kích hoạt Tor và thậm chí vô hiệu hóa nó sau khi ứng dụng Ginger đã đóng.



![screen](assets/fr/21.webp)



**Lưu ý** :




- Đối với xác thực hai yếu tố, hãy đảm bảo ứng dụng xác thực của bạn hỗ trợ giao thức SHA256 và mã 8 chữ số. Ginger Wallet yêu cầu mã 2FA 8 chữ số để tăng cường bảo mật. Định dạng dài hơn này giúp mã khó đoán hoặc bị xâm phạm hơn, mang lại khả năng bảo vệ tốt hơn trước các truy cập trái phép.
- Theo mặc định, tất cả lưu lượng mạng Ginger đều đi qua Tor, loại bỏ nhu cầu cấu hình thủ công. Nếu Tor đã được kích hoạt trên hệ thống của bạn, Ginger sẽ tự động ưu tiên Tor.



Nhưng sau khi bạn tắt Tor trong phần cài đặt, quyền riêng tư của bạn nhìn chung vẫn được bảo toàn, ngoại trừ hai trường hợp sau:




- trong quá trình Coinjoin, người điều phối có thể liên kết dữ liệu đầu vào và đầu ra của bạn với địa chỉ IP của bạn;
- khi phát sóng một giao dịch, một nút độc hại mà bạn kết nối có thể liên kết giao dịch của bạn với IP của bạn.



Đừng quên nhấn **Xong** (ở góc dưới bên phải) mỗi lần để lưu cài đặt. Một số cài đặt yêu cầu phải khởi động lại Ginger Wallet để có hiệu lực.



Ngoài ra, thanh tìm kiếm ở đầu danh mục đầu tư cho phép bạn tìm kiếm và truy cập bất kỳ tham số nào, v.v.



![screen](assets/fr/22.webp)




### Cấu hình danh mục đầu tư



Bạn có thể tạo nhiều danh mục đầu tư trong ứng dụng, vì vậy mỗi danh mục đầu tư có thể được cấu hình để phù hợp với nhu cầu của bạn. Để thực hiện việc này, hãy nhấp vào **ba dấu chấm** phía trước tên danh mục đầu tư, sau đó nhấp vào **Cài đặt danh mục đầu tư**.



![screen](assets/fr/23.webp)



Như bạn thấy, ngoài tham số wallet, bạn sẽ có thể xem UTXO (danh sách mã thông báo bạn sở hữu), số liệu thống kê và thông tin wallet (ví dụ: khóa công khai mở rộng).



Để quay lại cấu hình danh mục đầu tư của chúng tôi, khi bạn nhấp vào các thông số danh mục đầu tư, bạn sẽ được đưa đến các tab sau:




- Chung** (nơi bạn có thể thay đổi tên danh mục đầu tư);



![screen](assets/fr/24.webp)





- Coinjoin** (nơi bạn có thể tùy chỉnh cài đặt coinjoin cho wallet này);



![screen](assets/fr/25.webp)





- Công cụ** (nơi bạn có thể kiểm tra seedphrase, đồng bộ lại danh mục đầu tư hoặc xóa danh mục đầu tư).



![screen](assets/fr/26.webp)




## Nhận bitcoin



![video](https://youtu.be/cqv35wBDWMQ)



Để nhận bitcoin trong wallet của bạn trên Ginger Wallet:




- nhấn **Nhận** ;



![screen](assets/fr/27.webp)





- Nhập tên nguồn mà bạn muốn liên kết địa chỉ. Đây là nhãn để theo dõi các khoản thanh toán của bạn. Điều này không liên quan đến on-chain; nó chỉ đơn giản là thông tin truy xuất nguồn gốc được lưu trữ cục bộ trong ứng dụng của bạn;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- nhấp vào mũi tên nhỏ bên trái **Tạo** để chọn định dạng địa chỉ của bạn (**SegWit** /**Taproot**), sau đó nhấp vào **Tạo**, để generate nhập địa chỉ và mã QR.



![screen](assets/fr/29.webp)



Người gửi sẽ sử dụng địa chỉ hoặc mã QR này để gửi bitcoin cho bạn.



![screen](assets/fr/30.webp)




## Gửi bitcoin




![video](https://youtu.be/2nf5aAimfhg)



Để thực hiện điều này:




- Nhấn nút **Gửi**;
- nhập địa chỉ người nhận, số tiền cần gửi và nhãn;
- kiểm tra tổng quan giao dịch và xác nhận gửi.



![screen](assets/fr/31.webp)




## Chi tiêu bitcoin



Thật dễ dàng để mua và bán Bitcoin bằng Ginger Wallet. Chỉ với vài bước, bạn có thể sử dụng bitcoin của mình.



### Mua bitcoin



![video](https://youtu.be/lEqTBzm5MEA)



Người dùng Ginger Wallet có thể mua bitcoin.





- Nhấn nút **Mua**. Nút này vẫn hiển thị ngay cả khi wallet hết hàng.



![screen](assets/fr/32.webp)





- Chọn quốc gia của bạn, hoặc thậm chí là tiểu bang của bạn (ở một số khu vực, chẳng hạn như Canada), trước khi tiến hành mua bitcoin. Trên thực tế, khi bạn nhấp vào chức năng **Mua** lần đầu tiên, bạn cũng cần chỉ định khu vực của mình.



![screen](assets/fr/33.webp)



Nhấn **Tiếp tục** để tiếp tục quá trình mua hàng.





- Sau đó, nhập số lượng Bitcoin bạn muốn mua vào trường chuyên dụng. Bạn cũng có thể chọn loại tiền tệ giao dịch.



![screen](assets/fr/34.webp)



Mỗi loại tiền tệ đều có giới hạn mua tối thiểu và tối đa. Ví dụ: bằng USD, giới hạn tối đa là 30.000 đô la.



Nếu bạn đã mua hàng, bạn có thể xem lịch sử giao dịch bằng cách nhấp vào nút **Đơn hàng trước**. Danh sách các giao dịch trước đó và trạng thái của chúng sẽ được hiển thị.





- Chọn ưu đãi phù hợp với bạn.



Tại thời điểm này, bạn sẽ thấy danh sách tất cả các ưu đãi hiện có. Với mỗi ưu đãi, bạn có:




 - tên nhà cung cấp (1) ;
 - số lượng bitcoin tương đương với số tiền đã nhập trước đó, phương thức thanh toán và phí mua (2);
 - nút **Chấp nhận** (3).



![screen](assets/fr/35.webp)



Các khoản phí được nêu trong ưu đãi không phải là chi phí bổ sung. Chúng đã được bao gồm trong tổng số tiền ưu đãi.



Góc trên bên phải màn hình, được gắn nhãn **Tất cả**, cho phép bạn lọc ưu đãi theo phương thức thanh toán. Phương thức thanh toán bạn chọn sẽ được đặt mặc định, nhưng bạn có thể thay đổi bất cứ lúc nào.



![screen](assets/fr/36.webp)



Nếu bạn tìm thấy một ưu đãi phù hợp, hãy nhấp vào nút **Chấp nhận** để tiếp tục mua hàng. Sau đó, bạn sẽ được chuyển hướng đến trang của người bán, nơi bạn có thể hoàn tất giao dịch.



### Bán bitcoin



Người dùng Ginger Wallet có thể bán Bitcoin. Nút **Bán** chỉ hiển thị khi danh mục đầu tư có sẵn tiền.





- Nhấp vào **Bán**.



![screen](assets/fr/37.webp)





- Tương tự như tùy chọn **Mua**, khi bạn sử dụng chức năng Bán lần đầu tiên, bạn phải chọn quốc gia của mình trước khi tiến hành bán bitcoin.





- Tiếp theo, bạn cần nhập số lượng Bitcoin bạn muốn bán. Bạn có thể nhập số lượng này bằng BTC hoặc bằng tiền pháp định như đô la Mỹ (USD).





- Sau khi hoàn tất, bạn sẽ thấy danh sách các ưu đãi hiện có. Chọn ưu đãi phù hợp với bạn, sau đó nhấp vào **Chấp nhận** để tiếp tục.





- Bây giờ bạn cần hoàn tất giao dịch:
 - Sau khi bạn chấp nhận lời đề nghị, bạn sẽ được chuyển hướng đến trang của nhà cung cấp;
 - Thực hiện theo hướng dẫn trên trang của nhà cung cấp;
 - Vào một thời điểm nào đó, bạn sẽ nhận được địa chỉ người nhận và số tiền chính xác cần gửi;
 - Sau đó quay lại Ginger Wallet để tiếp tục quá trình;
 - Khi quay lại Ginger Wallet, một hộp thoại sẽ xuất hiện, cho phép bạn tiếp tục bằng cách nhấp vào **Gửi**.



Thao tác này sẽ mở màn hình **Gửi** với địa chỉ và số tiền người nhận đã được điền sẵn. Bạn cũng có thể sử dụng nút **Gửi** trên màn hình chính. Mặc dù bạn có thể gửi giao dịch theo cách thủ công, chúng tôi khuyên bạn nên hoàn tất giao dịch thông qua hộp thoại để tối ưu hóa quy trình.



## Thực hiện lệnh coinjoin trên Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Bảo vệ tính bảo mật của bitcoin của bạn với **Coinjoin**, được tích hợp trực tiếp vào Ginger Wallet. wallet sử dụng **WabiSabi**, một giao thức coinjoin Chaumian được thiết kế để tạo điều kiện cho việc coinjoin dễ tiếp cận và hiệu quả hơn.



Bạn có thể lựa chọn chiến lược coinjoin (tự động hoặc thủ công) phù hợp nhất với mình.



Ginger Coinjoin đã sẵn sàng sử dụng ngay sau khi bạn tải xuống (không cần thực hiện thêm bước nào). Ginger Coinjoin sẽ tự động chạy nền để bảo vệ quyền riêng tư của bạn trong mọi giao dịch. Trên thực tế, trình phát Coinjoin sẽ xuất hiện bất cứ khi nào bạn có số dư có thể ẩn danh.



Đối với việc khởi động coinjoin thủ công, chỉ cần một cú nhấp chuột. Bắt đầu vòng chơi và chờ giao dịch coinjoin được xây dựng và xác nhận. Bạn sẽ thấy điểm ẩn danh trong giao diện.



Có thể thực hiện nhiều bản phối cho đến khi đạt được mức độ ẩn danh mong muốn. Bạn cũng có thể loại trừ một số phần nhất định khỏi bản phối.



Theo mặc định, Ginger sử dụng bộ điều phối riêng với tất cả các tham số được cấu hình sẵn và phí được đảm bảo. Việc Coinjoin các token có giá trị hơn 0,03 BTC sẽ phải chịu phí điều phối 0,3% ngoài phí mining. Các khoản đầu tư có giá trị 0,03 BTC trở xuống, cũng như các giao dịch phối lại, được miễn phí điều phối, ngay cả sau một giao dịch duy nhất. Do đó, khoản thanh toán được thực hiện bằng tiền Coinjoin cho phép cả người gửi và người nhận phối lại coin của họ mà không phải chịu phí điều phối.



Ginger ưu tiên các coinjoin có nhiều người tham gia hơn là các vòng nhỏ hơn, nhanh hơn. Các coinjoin lớn hơn mang lại tính ẩn danh cao hơn, chi phí thấp hơn và hiệu quả sử dụng không gian khối cao hơn.




## An toàn và thực hành tốt nhất



Mong muốn phân quyền và bảo vệ quyền riêng tư đòi hỏi phải áp dụng một số biện pháp tốt nhất sau:




- Luôn giữ seedphrase của bạn ở nơi an toàn khi ngoại tuyến;
- Nếu bạn bị mất máy tính hoặc nghi ngờ bị truy cập trái phép, hãy tạo ngay một tài khoản wallet mới. Chuyển tiền của bạn vào danh mục đầu tư mới này và xóa tài khoản cũ;
- Sử dụng một địa chỉ khác nhau cho mỗi lần tiếp nhận để tránh việc sử dụng lại địa chỉ;
- Luôn tải xuống ứng dụng danh mục đầu tư của bạn độc quyền từ tài khoản GitHub chính thức hoặc trang web chính thức.



Bây giờ bạn đã quen với việc sử dụng ứng dụng Ginger Wallet để gửi, nhận và chi tiêu bitcoin.



Nếu bạn thấy hướng dẫn này hữu ích, vui lòng để lại cho tôi một like bên dưới. Đừng ngần ngại chia sẻ bài viết này qua các nền tảng mạng xã hội của bạn. Cảm ơn bạn rất nhiều!



Tôi cũng gợi ý bạn nên xem hướng dẫn này về cách sử dụng ứng dụng máy tính Liana để gửi và nhận bitcoin, cũng như triển khai kế hoạch quản lý tài sản tự động.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04