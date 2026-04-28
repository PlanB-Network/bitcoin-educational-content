---
name: LNP2PBot
description: Hướng dẫn đầy đủ về giao dịch Bitcoin LNP2PBot và P2P
---
![cover](assets/cover.webp)


## Giới thiệu


Các sàn giao dịch ngang hàng không cần KYC (P2P) rất cần thiết để bảo vệ quyền riêng tư và quyền tự chủ tài chính của người dùng. Chúng cho phép giao dịch trực tiếp giữa các cá nhân mà không cần xác minh danh tính, điều này rất quan trọng đối với những người coi trọng quyền riêng tư. Để hiểu sâu hơn về các khái niệm lý thuyết, hãy tham khảo khóa học BTC204:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Việc mua bán bitcoin trực tiếp giữa người dùng (P2P) là một trong những phương pháp riêng tư nhất để mua hoặc bán bitcoin. LNP2PBot là một bot mã nguồn mở dựa trên Telegram, hỗ trợ các giao dịch P2P trên mạng Lightning, cho phép giao dịch nhanh chóng, chi phí thấp và không cần xác minh danh tính (KYC).


### Tại sao nên sử dụng Lnp2pbot?




- Không cần xác minh danh tính (KYC)
- Giao dịch nhanh chóng trên Lightning Network
- Chi phí thấp
- Giao diện đơn giản thông qua Telegram, một ứng dụng nhắn tin phổ biến có thể truy cập từ bất cứ đâu trên thế giới
- Hệ thống danh tiếng tích hợp
- Hệ thống ký quỹ tự động đảm bảo giao dịch an toàn
- Hỗ trợ đa tiền tệ
- Cộng đồng năng động và đang phát triển


### Điều kiện tiên quyết


Để sử dụng Lnp2pbot, bạn cần:


1. Lightning Network wallet (khuyên dùng Breez, Phoenix hoặc Blixt)


2. Ứng dụng Telegram đã được cài đặt (https://telegram.org/)


3. Một tài khoản Telegram với tên người dùng đã được xác định


## Cài đặt và cấu hình


### 1. Cấu hình Lightning wallet của bạn


Hãy bắt đầu bằng cách cài đặt thiết bị Lightning wallet tương thích. Dưới đây là các khuyến nghị chi tiết của chúng tôi:


**wallet được đề xuất**




- [Breez](https://breez.technology):
  - Tuyệt vời cho người mới bắt đầu
  - Giao diện trực quan, hiện đại
  - Không lưu giữ tài sản (bạn vẫn giữ quyền kiểm soát tiền của mình)
  - Hoàn toàn tương thích với Lnp2pbot
  - Có sẵn trên iOS và Android


Dưới đây là liên kết đến hướng dẫn dành cho wallet này:


https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06


- [Phoenix](https://phoenix.acinq.co) :
  - Đơn giản và đáng tin cậy
  - Cấu hình kênh tự động
  - Hỗ trợ gốc cho hóa đơn BOLT11
  - Tuyệt vời cho các giao dịch hàng ngày
  - Có sẵn trên iOS và Android


Dưới đây là liên kết đến hướng dẫn dành cho wallet này:


https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


- [Blixt](https://blixtwallet.github.io):
  - Mang tính kỹ thuật hơn nhưng rất đầy đủ
  - Tùy chọn cấu hình nâng cao
  - Phù hợp cho người dùng có kinh nghiệm
  - Mã nguồn mở
  - Có sẵn trên Android


Dưới đây là liên kết đến hướng dẫn dành cho wallet này:


https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Lưu ý quan trọng về các mẫu wallet khác**


⚠️ **Quan trọng**: Trước khi bán sats, hãy đảm bảo wallet của bạn hỗ trợ hóa đơn "giữ", được bot sử dụng như một hệ thống ký quỹ.




- Wallet of Satoshi**: Hoạt động tốt để nhận sats, nhưng có thể bị chậm trễ trong việc cập nhật số dư nếu giao dịch bị hủy.
- Muun**: Không khuyến nghị sử dụng vì có thể xảy ra lỗi thanh toán do giới hạn phí định tuyến của bot (tối đa 0,2%).
- Aqua**: Hoạt động để nhận sats, nhưng có thể bị chậm trễ kéo dài (lên đến 48 giờ) để cập nhật số dư trong trường hợp hủy giao dịch.


💡 **Mẹo**: Để có trải nghiệm tối ưu, hãy chọn các loại wallet được khuyến nghị (Breez, Phoenix hoặc Blixt).


⚠️ **Quan trọng**: Đừng quên lưu các cụm từ khôi phục của bạn ở một nơi an toàn.


### 2. Bắt đầu sử dụng Lnp2pbot


1. Nhấp vào liên kết này để truy cập bot: [@lnp2pBot](https://t.me/lnp2pbot)


2. Telegram sẽ tự động mở


3. Nhấp vào "Bắt đầu" hoặc gửi lệnh "/start"


4. Bot sẽ yêu cầu bạn tạo tên người dùng nếu bạn chưa có


5. Bot sẽ hướng dẫn bạn thực hiện cấu hình ban đầu


### 3. Tham gia cộng đồng




- Hãy tham gia kênh chính: [@p2plightning](https://t.me/p2plightning)
- Hỗ trợ: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)


## Mua bán Bitcoin


Có hai cách chính để trao đổi bitcoin trên Lnp2pbot:


1. Duyệt và phản hồi các lời đề nghị hiện có trên thị trường


2. Tự tạo đề nghị mua hoặc bán của riêng bạn


Trong hướng dẫn này, chúng ta sẽ xem xét chi tiết cách thức:




- Mua bitcoin từ một giao dịch hiện có
- Bán Bitcoin bằng cách tạo ra lời chào bán của riêng bạn


### Cách mua Bitcoin


**1. Tìm và chọn một ưu đãi**


![Sélection d'une offre de vente](assets/fr/01.webp)


Hãy xem các ưu đãi trong [@p2plightning](https://t.me/p2plightning) và nhấp vào nút "Mua satoshi" bên dưới quảng cáo mà bạn quan tâm.


**2. Xác nhận ưu đãi và số tiền**


![Validation de l'offre](assets/fr/02.webp)


1. Quay lại cuộc trò chuyện với bot


2. Xác nhận lựa chọn ưu đãi của bạn


3. Nhập số tiền bằng đơn vị tiền tệ bạn muốn mua


4. Bot sẽ yêu cầu bạn cung cấp hóa đơn Lightning với số tiền bằng satoshi


**3. Liên hệ với người bán**


![Mise en relation](assets/fr/03.webp)


Sau khi hóa đơn được gửi đi, hệ thống tự động sẽ liên hệ bạn với người bán.


4. Liên lạc với người bán


![Chat privé](assets/fr/04.webp)


Nhấp vào biệt danh của người bán để mở kênh trò chuyện riêng tư, nơi bạn có thể trao đổi thông tin thanh toán bằng tiền tệ pháp định.


5. Xác nhận thanh toán


![Confirmation du paiement](assets/fr/05.webp)


Sau khi thực hiện thanh toán bằng tiền pháp định, hãy sử dụng lệnh `/fiatsent` trong khung chat của bot. Khi giao dịch hoàn tất, bạn có thể đánh giá người bán và giao dịch sẽ được đóng lại.


### Cách bán Bitcoin


**1. Tạo bản chào hàng**


![Création d'une offre de vente](assets/fr/06.webp)


Để tạo phiếu chào hàng, chỉ cần sử dụng lệnh:


`/bán`


Sau đó, bot sẽ hướng dẫn bạn từng bước một:


1. Chọn đơn vị tiền tệ của bạn


2. Cho biết số lượng satoshi cần bán


3. Với mức giá đó, bạn có hai lựa chọn:




   - Đặt giá cố định cho số lượng satoshi
   - Sử dụng giá thị trường với tùy chọn áp dụng phí bảo hiểm (dương hoặc âm)


💡 **Mẹo**: Mức phí bảo hiểm cho phép bạn điều chỉnh giá bán so với giá thị trường. Ví dụ, mức phí bảo hiểm -1% có nghĩa là bạn đang bán với giá thấp hơn 1% so với giá thị trường.


**2. Xác nhận tạo đơn hàng**


![Confirmation de l'ordre de vente](assets/fr/07.webp)


Sau khi đơn hàng được tạo, bạn sẽ thấy một thông báo xác nhận với tùy chọn hủy đơn hàng bằng lệnh `/cancel`.


**3. Quản lý bán hàng**


![Prise de l'ordre par un acheteur](assets/fr/08.webp)




- Khi người mua phản hồi lại lời đề nghị của bạn, bạn sẽ nhận được thông báo kèm mã QR và hóa đơn thanh toán.
- Kiểm tra hồ sơ và uy tín của người mua.


![Mise en relation avec l'acheteur](assets/fr/09.webp)




- Nhấp vào biệt danh của người mua để mở kênh trò chuyện riêng tư.
- Cung cấp thông tin chi tiết về phương thức thanh toán bằng tiền tệ pháp định cho người mua.
- Chờ xác nhận thanh toán bằng tiền mặt từ người mua.
- Hãy kiểm tra xem khoản thanh toán đã được nhận vào tài khoản của bạn chưa.


![Confirmation de la fin de l'ordre](assets/fr/10.webp)




- Xác nhận giao dịch bằng lệnh `/release` và hoàn tất đơn hàng. Bạn sẽ có cơ hội đánh giá người mua.


## Thực hành tốt và an toàn


### Mẹo an toàn




- Hãy bắt đầu với số lượng nhỏ
- Luôn kiểm tra uy tín của người dùng
- Chỉ sử dụng các phương thức thanh toán được đề xuất
- Giữ tất cả các cuộc liên lạc trong kênh chat của bot
- Tuyệt đối không chia sẻ thông tin nhạy cảm


### Hệ thống danh tiếng




- Mỗi người dùng đều có một điểm uy tín
- Giao dịch thành công sẽ giúp tăng điểm số của bạn
- Chọn những người dùng có uy tín tốt
- Hãy báo cáo bất kỳ hành vi đáng ngờ nào cho người điều hành


### Giải quyết tranh chấp


1. Khi gặp vấn đề, hãy giữ bình tĩnh và chuyên nghiệp


2. Sử dụng lệnh `/dispute` để mở yêu cầu hỗ trợ


3. Cung cấp tất cả các bằng chứng cần thiết


4. Chờ người điều hành


## So sánh với các giải pháp khác


Lnp2pbot có một số ưu điểm và nhược điểm so với các giải pháp trao đổi P2P khác như Peach, Bisq, HodlHodl và Robosat:


### Ưu điểm của Lnp2pbot




- Không yêu cầu xác minh danh tính**: Không giống như một số nền tảng khác, Lnp2pbot không yêu cầu xác minh danh tính, do đó bảo vệ quyền riêng tư của người dùng.
- Giao dịch nhanh chóng**: Nhờ mạng Lightning, các giao dịch diễn ra gần như tức thì.
- Phí thấp**: Chi phí giao dịch thấp hơn so với các sàn giao dịch truyền thống.
- Khả năng truy cập trên thiết bị di động**: LNP2PBot có thể truy cập thông qua Telegram, giúp dễ dàng sử dụng trên các thiết bị di động.
- Dễ sử dụng**: Giao diện trực quan của Lnp2pbot giúp người dùng dễ dàng sử dụng, ngay cả với những người ít kinh nghiệm.


### Nhược điểm của Lnp2pbot




- **Yêu cầu bắt buộc đối với Telegram**: Việc sử dụng Lnp2pbot yêu cầu tài khoản Telegram, điều này có thể không phù hợp với tất cả người dùng.
- Thanh khoản thấp hơn**: So với các nền tảng đã được thiết lập như Bisq, thanh khoản có thể bị hạn chế hơn.


Để so sánh, các giải pháp như Bisq cung cấp tính thanh khoản cao hơn và giao diện máy tính để bàn, nhưng có thể có phí cao hơn và thời gian giao dịch lâu hơn. Trong khi đó, HodlHodl và Robosat cũng cung cấp giao dịch không cần xác minh danh tính (KYC), nhưng với cấu trúc phí và giao diện khác nhau.


## Tài nguyên hữu ích




- Trang web chính thức: https://lnp2pbot.com/
- Tài liệu hướng dẫn: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Hỗ trợ: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)