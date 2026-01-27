---
name: ArkadeOS
description: Hướng dẫn đầy đủ về danh mục đầu tư Arkade và Ark Protocol
---

![cover](assets/cover.webp)



Mạng lưới Bitcoin đang đối mặt với một thách thức lớn: khả năng mở rộng. Mặc dù lớp chính (lớp 1) mang lại khả năng bảo mật và phân quyền vượt trội, nhưng nó chỉ có thể xử lý một số lượng giao dịch hạn chế mỗi giây. Lightning Network nổi lên như một giải pháp lớp thứ hai (lớp 2) đầy hứa hẹn, cho phép thanh toán nhanh chóng và chi phí thấp. Tuy nhiên, Lightning cũng có những hạn chế riêng: quản lý kênh, nhu cầu về thanh khoản đầu vào và độ phức tạp về mặt kỹ thuật có thể khiến người dùng mới e ngại.



Đây là nền tảng của **Ark**, một giao thức lớp 2 mới được thiết kế để mang lại trải nghiệm người dùng đơn giản hơn mà không ảnh hưởng đến quyền tối cao. **ArkadeOS** (hay Arkade) là phiên bản triển khai chính đầu tiên của giao thức này, cung cấp danh mục Bitcoin thế hệ tiếp theo.



Hướng dẫn này sẽ hướng dẫn bạn khám phá thế giới Arkade. Chúng ta sẽ tìm hiểu cách thức hoạt động của giao thức Ark, cách cài đặt và cấu hình Arkade wallet, cũng như cách sử dụng nó để gửi và nhận bitcoin ngay lập tức, bảo mật và không gặp phải những khó khăn thường gặp của Lightning Network.



## Hiểu về giao thức Ark



Trước khi tìm hiểu sâu hơn về Arkade, điều quan trọng là phải nắm vững các khái niệm chính của giao thức Ark vận hành nó. Ark không phải là một blockchain riêng biệt, mà là một cơ chế phối hợp thông minh dựa trên Bitcoin.



### Khái niệm VTXO


Trọng tâm của Ark là **VTXO** (Virtual UTXO). VTXO là một UTXO chưa được công bố trên blockchain Bitcoin: nó tồn tại bên ngoài chuỗi chính (off-chain) nhưng được hỗ trợ bởi các giao dịch được ký trước trên blockchain.



Không giống như số dư trên sàn giao dịch tập trung, VTXO thực sự thuộc về bạn. Bạn nắm giữ bằng chứng mật mã cho phép bạn, bất cứ lúc nào, yêu cầu số bitcoin thực tương ứng trên blockchain, ngay cả khi máy chủ Ark biến mất. VTXO cho phép bạn chuyển giá trị ngay lập tức giữa những người dùng mà không cần chờ xác nhận khối.



### Vai trò của ASP (Nhà cung cấp dịch vụ Ark)


Giao thức Ark hoạt động theo mô hình máy khách-máy chủ. Máy chủ được gọi là **ASP** (Nhà cung cấp dịch vụ Ark). ASP đóng vai trò là người dẫn đường:




- Nó cung cấp tính thanh khoản cần thiết cho mạng lưới.
- Nó điều phối các giao dịch giữa người dùng.
- Nó tổ chức các "vòng" thanh toán trên blockchain.



Điều quan trọng cần lưu ý là ASP **không lưu ký**. Nó không bao giờ nắm giữ khóa riêng tư của bạn, cũng không thể đánh cắp tiền của bạn. Vai trò của nó hoàn toàn là kỹ thuật và hậu cần. Nếu ASP kiểm duyệt giao dịch của bạn hoặc ngừng hoạt động, bạn luôn có thể khôi phục tiền của mình thông qua quy trình thoát đơn phương.



### Vòng tròn và sự riêng tư


Các giao dịch trên Ark được hoàn tất theo từng đợt gọi là **Vòng**. Định kỳ (ví dụ: vài giây một lần), ASP sẽ tập hợp tất cả các giao dịch đang chờ xử lý và neo chúng trên blockchain Bitcoin trong một giao dịch được tối ưu hóa duy nhất.


Cơ chế này mang lại hai lợi thế chính:




- Khả năng mở rộng**: Một giao dịch on-chain có thể xác thực hàng nghìn khoản thanh toán off-chain, giúp giảm đáng kể chi phí cho người dùng.
- Bảo mật**: Mỗi vòng hoạt động như một **CoinJoin**. Tiền từ tất cả người tham gia được trộn vào một quỹ chung trước khi được phân phối lại dưới dạng VTXO mới. Điều này phá vỡ liên kết giữa người gửi và người nhận, khiến người quan sát bên ngoài rất khó, nếu không muốn nói là không thể, theo dõi các khoản thanh toán.



## Bài thuyết trình ArkadeOS



ArkadeOS là ứng dụng cụ thể giúp giao thức Ark được phổ biến rộng rãi đến công chúng. Được phát triển bởi Ark Labs, ArkadeOS là một hệ sinh thái hoàn chỉnh bao gồm danh mục đầu tư (Wallet), máy chủ (Operator) và các công cụ dành cho nhà phát triển.



Đối với người dùng cuối, Arkade mang hình thức của một ứng dụng web wallet (PWA - Ứng dụng Web Tiến bộ) thanh lịch và trực quan. Nó ẩn đi sự phức tạp về mật mã của VTXO và các vòng lặp đằng sau một giao diện quen thuộc. Với Arkade, bạn có một địa chỉ để nhận, một nút để gửi và lịch sử giao dịch, giống như wallet cổ điển, nhưng với sức mạnh tức thời và bảo mật của Ark.



## Cài đặt và cấu hình



Vì Arkade là một ứng dụng web tiến bộ nên việc cài đặt rất dễ dàng và không nhất thiết phải liên quan đến các cửa hàng ứng dụng truyền thống.



### Truy cập và cài đặt


Bạn có thể truy cập Arkade trực tiếp từ bất kỳ trình duyệt web hiện đại nào (Chrome, Safari, Brave) trên máy tính hoặc thiết bị di động.





- Truy cập trang web chính thức của ứng dụng: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Bạn sẽ được chào đón bằng một loạt màn hình giới thiệu về các khái niệm chính của Arkade: hệ sinh thái mới cho Bitcoin, tầm quan trọng của việc tự lưu ký và lợi ích của giao dịch hàng loạt.



![arkade onboarding](assets/fr/02.webp)





- Trên Android (Chrome/Brave)**: Nhấn vào menu trình duyệt (ba dấu chấm) và chọn "Cài đặt ứng dụng" hoặc "Thêm vào màn hình chính".
- Trên iOS (Safari)**: Nhấn nút chia sẻ (hình vuông có mũi tên hướng lên) và chọn "Trên màn hình chính".



Sau khi cài đặt, Arkade sẽ khởi chạy như một ứng dụng gốc, toàn màn hình và không có thanh địa chỉ.



### Tạo danh mục đầu tư


Khi khởi chạy lần đầu, bạn sẽ được yêu cầu cấu hình danh mục đầu tư của mình.





- Nhấp vào **"Tạo Wallet mới"**.



![create wallet](assets/fr/03.webp)





- wallet được tạo ngay lập tức. Không giống như ví Bitcoin truyền thống, **Arkade không sử dụng cụm từ khôi phục 12 hoặc 24 từ**. Thay vào đó, Arkade tự động tạo **khóa riêng** theo định dạng Nostr (nsec), khóa này sẽ được sử dụng để sao lưu và khôi phục wallet của bạn. Hãy nhớ lưu khóa này ngay lập tức (xem phần tiếp theo).





- Bạn sẽ thấy màn hình "wallet mới của bạn đã hoạt động!", xác nhận rằng wallet của bạn đã sẵn sàng để sử dụng. Nhấp vào **"ĐI ĐẾN VÍ"** để truy cập giao diện chính.



Sau khi vào wallet, bạn sẽ được chuyển đến giao diện chính của Arkade. Tại đây, bạn sẽ thấy số dư, các nút gửi và nhận tiền, và tab "Ứng dụng" cho phép truy cập vào các ứng dụng tích hợp như Boltz (giao dịch Lightning), LendaSat và LendaSwap (dịch vụ cho vay), và Fuji Money (tài sản tổng hợp).



![wallet interface](assets/fr/04.webp)



### Kết nối với ASP


Theo mặc định, danh mục đầu tư được tự động cấu hình để kết nối với Arkade Labs ASP chính thức. Bạn có thể kiểm tra máy chủ mình đang kết nối bằng cách vào **Cài đặt** > **Giới thiệu**, tại đó bạn sẽ thấy địa chỉ máy chủ (hiện tại là `https://arkade.computer`).



Trong phiên bản Arkade (Beta) hiện tại, bạn không thể tùy chỉnh máy chủ ASP theo cách thủ công. Ứng dụng sẽ tự động kết nối với ASP chính thức của Arkade Labs. Trong tương lai, người dùng có thể lựa chọn giữa các ASP khác nhau tùy theo sở thích, nhưng tính năng này hiện chưa khả dụng.



### Sao lưu khóa riêng của bạn


**Arkade sử dụng khóa riêng ở định dạng Nostr (nsec) làm phương pháp sao lưu và phục hồi. Để sao lưu khóa riêng của bạn:





- Vào **Cài đặt** từ màn hình chính.
- Chọn **"Sao lưu và quyền riêng tư"**.
- Bạn sẽ thấy **khóa riêng** của mình được hiển thị ở định dạng `nsec...`. Chuỗi ký tự dài này là cách duy nhất để bạn khôi phục wallet.
- Nhấn **"COPY NSEC TO CLIPBOARD"** để sao chép khóa riêng của bạn.
- Giữ chìa khóa này ở nơi an toàn**: viết ra giấy, lưu trữ trong trình quản lý mật khẩu an toàn hoặc sử dụng bất kỳ phương pháp sao lưu nào phù hợp với bạn.
- Arkade cũng cung cấp tùy chọn **"Bật sao lưu Nostr"**. Tính năng này sử dụng giao thức Nostr (một mạng phi tập trung) để tự động sao lưu một số dữ liệu nhất định từ wallet của bạn dưới dạng mã hóa đến các rơle Nostr. Điều này giúp đồng bộ hóa giữa nhiều thiết bị và giúp khôi phục trạng thái wallet của bạn dễ dàng hơn.



**Quan trọng**: Sao lưu Nostr chỉ là một tính năng **tiện lợi**. Chúng không thay thế bản sao lưu khóa nsec của bạn. Các rơle Nostr không đảm bảo lưu trữ dữ liệu vĩnh viễn. Khóa riêng nsec của bạn vẫn là phương tiện duy nhất được đảm bảo để khôi phục tiền của bạn.



![backup private key](assets/fr/05.webp)




## Sử dụng Arkade



Sau khi thiết lập wallet, bạn đã sẵn sàng khám phá các tính năng của Arkade. Giao diện được thiết kế để hợp nhất các loại hình thanh toán Bitcoin khác nhau (On-chain, Lightning, Ark) một cách liền mạch.



### Nhận tiền



Để tài trợ cho danh mục đầu tư của bạn, hãy nhấn **"Nhận"**. Arkade cung cấp ba phương thức nhận tiền:





- Thanh toán Ark**: Nếu người gửi cũng sử dụng Arkade, hãy chia sẻ địa chỉ Ark của bạn để chuyển tiền ngay lập tức, bảo mật và gần như miễn phí.
- Nạp tiền trực tuyến (Nạp tiền)**: Sử dụng địa chỉ Bitcoin (`bc1p...`) để nhận tiền từ wallet cổ điển hoặc sàn giao dịch. Cần xác nhận (khoảng 10 phút) trước khi tiền được chuyển đổi thành VTXO.
- Hoán đổi Lightning**: Tạo hóa đơn Lightning và thanh toán từ thiết bị Lightning wallet bên ngoài. Tiền sẽ được chuyển ngay lập tức thông qua tính năng hoán đổi tự động.



![receive amount](assets/fr/06.webp)



Màn hình biên lai hiển thị tất cả các tùy chọn khả dụng: mã QR, địa chỉ Ark, địa chỉ Bitcoin (BIP21) và hóa đơn Lightning. Đối với thanh toán Lightning, vui lòng giữ ứng dụng mở trong khi giao dịch.



![receive confirmation](assets/fr/07.webp)



### Gửi tiền



Để gửi tiền, hãy nhấn **"Gửi"** và dán địa chỉ người nhận hoặc quét mã QR. Arkade sẽ tự động phát hiện loại hình thanh toán cần thiết:





- Thanh toán Ark**: Chuyển khoản đến địa chỉ Ark ngay lập tức, riêng tư và gần như miễn phí (0 phí SATS). Người nhận không cần phải trực tuyến.
- Thanh toán Lightning**: Quét hóa đơn Lightning (`lnbc...`) và Arkade sẽ tự động thực hiện hoán đổi. ASP sẽ thanh toán hóa đơn cho bạn và trừ vào số dư Arkade của bạn.
- Thanh toán trên chuỗi**: Đối với địa chỉ Bitcoin cổ điển (`bc1q...` hoặc `bc1p...`), Arkade khởi tạo "Đầu ra hợp tác" sẽ được đưa vào vòng on-chain tiếp theo.



Kiểm tra thông tin chi tiết trên màn hình "Ký giao dịch", sau đó xác nhận bằng **"CHẠM ĐỂ KÝ"**.



![send payment](assets/fr/08.webp)



**Giới hạn hiện tại (Bản beta)**: Không thể sử dụng VTXO được tạo chưa đầy 24 giờ trước cho đầu ra on-chain. Nếu gặp lỗi, vui lòng đợi cho đến khi VTXO của bạn "hoàn thiện".



**Bảo mật đầu ra on-chain**: Ví dụ bên dưới hiển thị [giao dịch đầu ra Ark trên mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Chúng tôi quan sát đầu vào phân tán đến 4 đầu ra khác nhau, giống như CoinJoin. Đối với người quan sát bên ngoài, không thể xác định số tiền nào thuộc về người dùng nào.



![transaction ark mempool](assets/fr/11.webp)



## Các tính năng nâng cao



### Quản lý hết hạn VTXO


Một đặc điểm kỹ thuật của giao thức Ark là VTXO có **thời gian tồn tại giới hạn**. Giới hạn thời gian này vốn có trong thiết kế của giao thức. Thời gian hết hạn có thể được cấu hình bởi từng máy chủ ASP; trên Arkade Labs ASP chính thức, thời gian này là khoảng **4 tuần (≈30 ngày)**.



**Giới hạn này cho phép máy chủ Ark quản lý thanh khoản hiệu quả và dọn dẹp VTXO từ những người dùng không hoạt động. Sau khi hết hạn, về mặt kỹ thuật, máy chủ Ark có thể yêu cầu số tiền còn lại trong cây VTXO.



**Để duy trì hoạt động của VTXO, bạn cần "làm mới" chúng trước khi hết hạn. Việc làm mới bao gồm việc tham gia một "vòng" mới, trong đó các VTXO sắp hết hạn của bạn sẽ được đổi lấy các VTXO mới với thời hạn hiệu lực đầy đủ mới (khoảng 30 ngày trên Arkade Labs ASP).



Danh mục Arkade tự động quản lý quy trình này: ứng dụng liên tục theo dõi trạng thái VTXO của bạn và tự động làm mới chúng vài ngày trước khi hết hạn. Miễn là bạn mở ứng dụng thường xuyên (ít nhất một lần một tuần), VTXO của bạn sẽ tự động được duy trì hoạt động.



**Nếu bạn không mở danh mục đầu tư trong hơn 4 tuần, VTXO của bạn sẽ hết hạn. Tuy nhiên, bạn sẽ không mất tiền: bạn vẫn có thể thu hồi chúng thông qua **thoát lệnh đơn phương** (xem phần tiếp theo). Thủ tục này tốn kém hơn và chậm hơn, nhưng đảm bảo tiền của bạn vẫn có thể thu hồi được.



Việc phải mở ứng dụng thường xuyên khiến Arkade trở thành một ví **"Hot Wallet"** được thiết kế cho việc chi tiêu hàng ngày, chứ không phải là nơi an toàn cho việc tiết kiệm dài hạn. Để lưu trữ bitcoin mà không sử dụng trong thời gian dài, hãy ưu tiên phần cứng wallet lạnh.



**Kiểm tra trạng thái VTXO**: Bạn có thể theo dõi trạng thái VTXO trong **Cài đặt** > **Nâng cao**. Xem mục "Gia hạn tiếp theo" để biết thời điểm tự động gia hạn tiếp theo, và mục "Tiền ảo" để xem danh sách chi tiết tất cả VTXO của bạn cùng ngày hết hạn.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (Đơn phương rút lui)



Thoát đơn phương là một **bảo đảm mật mã cơ bản** của giao thức Ark, đảm bảo bạn lấy lại được tiền, ngay cả khi ASP biến mất, kiểm duyệt giao dịch của bạn hoặc từ chối hợp tác. Về mặt kỹ thuật, VTXO của bạn là **giao dịch Bitcoin đã được ký trước** mà bạn sở hữu. Trong trường hợp khẩn cấp tuyệt đối, bạn có thể phát các giao dịch này trên blockchain Bitcoin để thu hồi tiền mà không cần bất kỳ sự cho phép nào.



**Nó hoạt động như thế nào? Quá trình diễn ra theo hai giai đoạn. Đầu tiên, **Gỡ bỏ**: bạn lần lượt phát các giao dịch đã ký trước tạo nên VTXO của mình trên cây giao dịch. Sau đó là **Hoàn tất**: khi thời gian khóa hết hạn (thường là 24 giờ), bạn sẽ nhận bitcoin từ một địa chỉ tiêu chuẩn.



**Trạng thái hiện tại trong Arkade**: Trong phiên bản Beta, chưa có nút bấm hoặc giao diện người dùng đơn giản nào cho việc xuất dữ liệu một chiều. Chức năng này hiện yêu cầu sử dụng Arkade SDK và kiến thức chuyên môn về lập trình TypeScript.



**Ngay cả khi quy trình không thể truy cập chỉ bằng một nút bấm, vẫn có bảo đảm mật mã. VTXO của bạn chứa các giao dịch được ký trước, thuộc về bạn một cách hợp pháp. Chính bảo đảm kỹ thuật này khiến Ark trở thành một giao thức **phi lưu ký**: ngay cả trong trường hợp xấu nhất, tiền của bạn vẫn có thể được thu hồi về mặt kỹ thuật. Giao diện đơn giản hơn có thể sẽ được bổ sung trong các phiên bản Arkade trong tương lai.



## Ưu điểm và hạn chế



Để hiểu đúng về Arkade, chúng ta hãy tóm tắt những điểm mạnh và điểm yếu hiện tại của nó.



### Điểm nổi bật




- Trải nghiệm người dùng (UX)**: Không cần quản lý kênh, dung lượng đầu vào hay sao lưu kênh phức tạp như Lightning. Chỉ cần cài đặt và sử dụng.
- Quyền riêng tư**: Kiến trúc CoinJoin mặc định cung cấp mức độ ẩn danh cao hơn nhiều so với các giao dịch on-chain hoặc Lightning tiêu chuẩn.
- Khả năng tương tác**: Thanh toán bất kỳ mã QR Bitcoin nào (Trên chuỗi hoặc Lightning) từ một giao diện duy nhất.



### Hạn chế




- Giao thức Young**: Ark là một công nghệ rất mới. Có thể tồn tại lỗi. Không nên sử dụng Ark để lưu trữ các khoản tiền mà tổn thất có thể rất nghiêm trọng.
- Phụ thuộc ASP**: Mặc dù không lưu ký, hệ thống vẫn dựa vào tính khả dụng của ASP để đảm bảo tính lưu động. Nếu ASP ngoại tuyến, bạn không thể giao dịch ngay lập tức (chỉ có thể xuất tiền on-chain).
- Chỉ dành cho Hot Wallet**: Việc phải mở ứng dụng thường xuyên để làm mới VTXO không phù hợp để lưu trữ lạnh (Lưu trữ Cold).



## So sánh: Arkade vs Lightning vs Cashu



Để hiểu rõ hơn về vị thế của Arkade, chúng ta hãy so sánh nó với hai giải pháp mở rộng quy mô lớn khác.



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** là sự thỏa hiệp lý tưởng: sự đơn giản và tính bảo mật của Cashu, nhưng có chủ quyền (không giám sát) của Lightning.



## Hỗ trợ & Trợ giúp



Nếu bạn gặp bất kỳ vấn đề nào hoặc có bất kỳ câu hỏi nào khi sử dụng Arkade, ứng dụng cung cấp một số tùy chọn hỗ trợ:





- Vào **Cài đặt** > **Hỗ trợ**.
- Bạn sẽ tìm thấy một số tùy chọn:
  - Hỗ trợ khách hàng**: Nhận trợ giúp về danh mục đầu tư của bạn, báo cáo lỗi hoặc đặt câu hỏi.
  - Trò chuyện an toàn**: Các cuộc trò chuyện của bạn được bảo mật và riêng tư, với lịch sử được lưu giữ giữa các phiên trò chuyện.
  - Báo cáo lỗi**: Báo cáo mọi vấn đề bạn gặp phải, bao gồm các bước để tái hiện chúng.
  - Theo dõi tiến độ**: Luôn theo dõi các phiếu hỗ trợ và cuộc trò chuyện của bạn.



![support](assets/fr/10.webp)



Nhóm Arkade cũng hoạt động trên Telegram thông qua kênh @arkade_os để hỗ trợ và tích hợp.



## Lưu ý quan trọng: Ứng dụng trong bản Beta



**⚠️ Arkade hiện đang ở giai đoạn Beta Công khai trên mainnet Bitcoin**. Mặc dù ứng dụng hoạt động với bitcoin thật, nhưng vẫn cần lưu ý một số điểm sau.



### Khuyến nghị sử dụng




- Sử dụng số tiền nhỏ**: Tránh lưu trữ số tiền lớn trên Arkade. Hãy sử dụng wallet này cho các chi phí hàng ngày và giữ khoản tiết kiệm của bạn trên phần cứng wallet.
- Các lỗi và hạn chế có thể xảy ra**: Giống như bất kỳ ứng dụng nào đang được phát triển, Arkade có thể gặp lỗi hoặc hành vi không mong muốn. Vui lòng báo cáo bất kỳ sự cố nào thông qua bộ phận hỗ trợ tích hợp.
- Tiến hóa nhanh chóng**: Ứng dụng và giao thức liên tục được cải tiến. Một số tính năng có thể thay đổi hoặc được bổ sung trong các phiên bản tương lai.



### Những hạn chế hiện tại đã biết




- Độ trễ 24 giờ đối với VTXO**: Không thể sử dụng ngay VTXO mới tạo cho đầu ra on-chain.
- ASP unique**: Hiện tại vẫn chưa thể thay đổi máy chủ ASP trong ứng dụng.
- Đầu ra đơn phương về mặt kỹ thuật**: Chưa có giao diện đơn giản hóa nào cho đầu ra đơn phương (yêu cầu SDK).



Nhóm Arkade Labs đang tích cực làm việc để khắc phục những hạn chế này trong các phiên bản tương lai.



## Phần kết luận



ArkadeOS là một bước đột phá lớn trong hệ sinh thái Bitcoin. Việc triển khai giao thức Ark chứng minh rằng việc kết hợp tính đơn giản trong sử dụng với các nguyên tắc cơ bản của Bitcoin: không tin tưởng, hãy xác minh là hoàn toàn khả thi.



Mặc dù vẫn còn trong giai đoạn sơ khai, Arkade mang đến cái nhìn hấp dẫn về tương lai của thanh toán Bitcoin: tức thì, riêng tư và dễ dàng tiếp cận với tất cả mọi người mà không cần bất kỳ điều kiện tiên quyết kỹ thuật nào. Đây là công cụ hoàn hảo cho chi tiêu hàng ngày của bạn, bổ sung cho giải pháp tiết kiệm an toàn (Cold Wallet).



Chúng tôi khuyến khích bạn thử nghiệm Arkade với lượng nhỏ để tự mình khám phá giao thức mới này. Hệ sinh thái đang phát triển nhanh chóng, và Arkade đang đi đầu trong đổi mới này.



## Tài nguyên



Để tìm hiểu thêm, hãy tham khảo các nguồn chính thức:





- Trang web Arkade**: [arkadeos.com](https://arkadeos.com)
- Tài liệu**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Giao thức Ark**: [ark-protocol.org](https://ark-protocol.org)
- Mã nguồn** : [GitHub Arkade](https://github.com/arkade-os)