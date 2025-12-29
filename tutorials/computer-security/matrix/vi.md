---
name: Ma trận
description: Hướng dẫn tìm hiểu, cấu hình và sử dụng Matrix, nền tảng truyền thông an toàn, mở và phi tập trung.
---

![cover](assets/cover.webp)



## Matrix là gì?



Matrix là một **giao thức truyền thông phi tập trung** được thiết kế để cho phép trao đổi tin nhắn, tập tin và cuộc gọi âm thanh/video giữa người dùng và ứng dụng, mà không phụ thuộc vào một doanh nghiệp trung tâm. Không giống như các nền tảng nhắn tin truyền thống, Matrix là một **cơ sở hạ tầng mở**, tương tự như email: bất kỳ ai cũng có thể chọn một máy chủ hoặc tự vận hành một máy chủ, đồng thời vẫn giữ khả năng trao đổi với phần còn lại của mạng.



Matrix được phân biệt bởi ba nguyên tắc cơ bản:



### Đây là một giao thức, không phải là một ứng dụng.



Matrix không phải là một ứng dụng giống như WhatsApp hay Telegram.


Đó là một ngôn ngữ tiêu chuẩn mà nhiều ứng dụng có thể sử dụng.


Nói cách khác, rất nhiều phần mềm của Element, như FluffyChat, Cinny, Nheko và các phần mềm khác, đều cung cấp quyền truy cập vào cùng một mạng Matrix.



Điều này đảm bảo sự tự do hoàn toàn: thay đổi ứng dụng mà không mất liên lạc, đa dạng giao diện, độc lập khỏi một nhà cung cấp duy nhất.



![capture](assets/fr/03.webp)



### Một mạng lưới phi tập trung, liên kết



Cấu trúc của Matrix dựa trên **liên kết**, một mô hình trong đó nhiều máy chủ độc lập hợp tác với nhau.


Mỗi máy chủ (gọi là _máy chủ chính_) có thể lưu trữ người dùng, phòng trò chuyện và đồng bộ hóa tin nhắn với các máy chủ khác trên mạng.


Do đó:





- Không có một thực thể nào kiểm soát toàn bộ hệ thống;
- Một máy chủ có thể biến mất mà không ảnh hưởng đến phần còn lại của mạng;
- Mỗi tổ chức hoặc cá nhân có thể tự quản lý không gian của mình.



Mô hình này đảm bảo **khả năng phục hồi cao** và phản ánh các giá trị của chủ quyền công nghệ.



![capture](assets/fr/03.webp)



### Một hệ thống an toàn, được mã hóa



Matrix hỗ trợ **mã hóa đầu cuối (E2EE)** cho các cuộc trao đổi riêng tư và các nhóm được mã hóa.


Chỉ những người tham gia mới có thể đọc được tin nhắn, chứ không phải máy chủ trung gian.


Cách tiếp cận này cho phép giao tiếp mà không cần tiết lộ nội dung trao đổi cho bên thứ ba, đồng thời vẫn duy trì tính minh bạch của giao thức và khả năng tự vận hành máy chủ riêng.



![capture](assets/fr/05.webp)



### Khả năng tương tác độc đáo



Một trong những ưu điểm chính của Matrix là khả năng hoạt động như một **cầu nối giữa các hệ thống truyền thông khác nhau**. Nhờ có các _cầu nối_ này, người ta có thể kết nối:





- Telegram
- WhatsApp
- Signal
- Tin nhắn
- Slack
- Discord
- IRC, XMPP, v.v.



Điều này giúp hợp nhất các cộng đồng phân tán trên nhiều nền tảng khác nhau, đồng thời vẫn duy trì quyền kiểm soát cơ sở hạ tầng.



![capture](assets/fr/06.webp)



## Matrix hoạt động như thế nào?



Phần này trình bày cấu trúc nội bộ của mạng Matrix để hiểu cách người dùng, máy chủ và ứng dụng tương tác trong hệ sinh thái phi tập trung này. Matrix dựa trên ba yếu tố thiết yếu: _máy chủ chính_, định danh và _máy khách_ được sử dụng để giao tiếp.



### Máy chủ: máy chủ tại nhà



Matrix hoạt động trên các máy chủ độc lập được gọi là _máy chủ gia đình_.


Mỗi máy chủ gia đình quản lý:





- các tài khoản người dùng mà nó lưu trữ,
- các cuộc trò chuyện riêng tư và phòng chờ mà những người dùng này tham gia,
- Đồng bộ hóa với các máy chủ mạng khác.



Tất cả các máy chủ gia đình được kết nối với mạng Matrix đều tự động trao đổi tin nhắn và sự kiện từ các phòng khách dùng chung. Ví dụ:





- Người dùng đã đăng ký trên máy chủ A có thể trò chuyện với người dùng trên máy chủ B.
- Một salon có thể được phân bổ trên hàng chục máy chủ.
- Không ai có quyền kiểm soát một tiệm làm tóc hay toàn bộ cộng đồng.



Mô hình này có khả năng phục hồi cao và cho phép mỗi tổ chức hoặc cá nhân tự quản lý cơ sở hạ tầng của mình.



### Mã định danh ma trận



Mỗi người dùng có một mã định danh duy nhất, được gọi là **MXID** (Mã định danh ma trận), có dạng như một địa chỉ:



```bash
@nomdutilisateur:serveur.xyz
```



Nó bao gồm:





- Tên người dùng, đứng trước bởi **@**
- Tên máy chủ nơi tài khoản được tạo, đứng trước bởi **:**



Ví dụ:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Mã định danh này cho phép giao tiếp với bất kỳ người dùng Matrix nào khác, bất kể máy chủ gốc là ở đâu.



### Các ứng dụng khách của Matrix



Để sử dụng Matrix, bạn cần kết nối với một ứng dụng có tên là **client Matrix**.



Những cái tên nổi tiếng nhất là:





- Phần tử (web, di động, máy tính để bàn)
- FluffyChat (phiên bản di động)
- Cinny (giao diện web/máy tính để bàn tối giản)
- Nheko (máy tính để bàn)



Các ứng dụng này chỉ đơn thuần là giao diện cho:





- để xem tin nhắn,
- gửi văn bản, hình ảnh hoặc tệp tin.
- tham gia hoặc tạo ra các hội chợ thương mại.
- Thực hiện cuộc gọi thoại/video.



Tất cả các ứng dụng đều giao tiếp với máy chủ thông qua cùng một giao thức tiêu chuẩn.



### Phòng trò chuyện và tin nhắn riêng (DM)



Trong Matrix, các cuộc trao đổi diễn ra trong **các phòng** :





- Một căn phòng có thể là phòng công cộng hoặc phòng riêng.
- Nó có thể chứa hai người hoặc hàng nghìn người.
- Nó có thể được chia sẻ giữa nhiều máy chủ.
- Nó có một mã định danh duy nhất bắt đầu bằng **!**



Tin nhắn riêng tư đơn giản là các phòng trò chuyện chỉ có hai người tham gia, thường được gọi là **DM (Tin nhắn trực tiếp)**.



Quá trình đồng bộ hóa Salon diễn ra trong thời gian thực giữa các máy chủ tham gia, đảm bảo trải nghiệm liền mạch đồng thời duy trì tính phi tập trung.



## Tại sao nên sử dụng Matrix?



Matrix không chỉ là một giải pháp thay thế cho các hệ thống nhắn tin tập trung: đó là một công nghệ đáp ứng các nhu cầu thực tế về chủ quyền kỹ thuật số, bảo mật và khả năng tương tác. Có rất nhiều lý do khiến ngày càng nhiều người, công ty và tổ chức lựa chọn giao thức này để liên lạc.



### Giành lại quyền kiểm soát thông tin liên lạc của bạn



Hầu hết các nền tảng nhắn tin hoạt động theo mô hình tập trung: một bên duy nhất kiểm soát máy chủ, quyền truy cập, dữ liệu và các quy tắc sử dụng. Mô hình này ngụ ý sự phụ thuộc hoàn toàn vào nhà cung cấp.


Matrix áp dụng một cách tiếp cận khác.


Bất kỳ ai cũng có thể chọn nơi lưu trữ tài khoản của mình, hoặc thậm chí tự triển khai máy chủ riêng. Không có tổ chức nào có quyền chặn người dùng, yêu cầu xác minh danh tính xâm phạm quyền riêng tư hoặc áp đặt thay đổi chính sách.


Kiến trúc này trao lại quyền tự chủ cho cả cá nhân và tổ chức. Việc giao tiếp không còn dựa trên sự tin tưởng vào một công ty, mà dựa trên một giao thức mở, được ghi chép và có thể kiểm chứng.



### Giao tiếp an toàn, được mã hóa



Matrix hỗ trợ mã hóa đầu cuối cho các cuộc trò chuyện riêng tư và nhóm. Cơ chế này đảm bảo rằng chỉ những người tham gia mới có thể đọc được tin nhắn, ngay cả khi chúng đi qua các máy chủ của bên thứ ba trong liên kết.



Giao thức này sử dụng thuật toán Megolm/Olm, được thiết kế đặc biệt để cung cấp tính bảo mật mạnh mẽ trong môi trường phân tán, đa thiết bị.



Điều này cho phép:





- bảo vệ các cuộc trò chuyện nhạy cảm,
- ngăn chặn truy cập trái phép (kể cả từ máy chủ lưu trữ),
- Duy trì tính bảo mật trong thời gian dài.



Mã hóa không phải là một tùy chọn: nó là một thành phần cốt lõi của giao thức.



### Không còn phụ thuộc vào một ứng dụng duy nhất nữa.



Matrix không phải là một ứng dụng, mà là một giao thức.



Sự đa dạng về khách hàng này đảm bảo:





- Một sự lựa chọn phù hợp với nhu cầu cá nhân.
- Khả năng sử dụng Matrix trên mọi loại thiết bị.
- Không phụ thuộc vào một phần mềm duy nhất.



Nếu khách hàng không phù hợp hoặc ngừng duy trì dịch vụ, chỉ cần chọn khách hàng khác: tài khoản vẫn tiếp tục hoạt động bình thường.



### Liên kết và kết nối các cộng đồng khác nhau



Liên kết máy chủ cho phép các máy chủ khác nhau hoạt động cùng nhau trong khi vẫn được quản lý độc lập.


Do đó:





- Một tổ chức có thể tự quản lý máy chủ tại nhà của mình.
- Cá nhân có thể tham gia các máy chủ công cộng.
- Mọi người đều có thể giao tiếp với nhau như thể họ đang ở trên cùng một nền tảng.



Tính linh hoạt này cho phép tạo ra các không gian giao tiếp phù hợp với mọi nhu cầu: nhóm, hiệp hội, cộng đồng, tổ chức hoặc các dự án mã nguồn mở.



Matrix đặc biệt phổ biến trong giới kỹ thuật, các nhóm hoạt động xã hội, các nhà nghiên cứu, chính phủ và ngày càng được ưa chuộng trong cộng đồng GW3.



### Khả năng tương tác độc đáo trong lĩnh vực nhắn tin



Một trong những thế mạnh chính của Matrix là khả năng **mở rộng** các sàn giao dịch nhờ các cầu nối có khả năng liên kết:





- WhatsApp
- Telegram
- Signal
- Slack
- Discord
- IRC
- XMPP
- và nhiều nền tảng khác



Như vậy, Matrix trở thành một lớp thống nhất cho việc giao tiếp, kết nối nhiều cộng đồng rải rác trên các ứng dụng khác nhau.



Khả năng tương tác này giúp giảm sự phân mảnh và đơn giản hóa quá trình hợp tác.



### Một giao thức tự do, mở và bền vững



Giao thức Matrix hoàn toàn là mã nguồn mở và được phát triển một cách minh bạch.


Điều này đảm bảo một số lợi thế:





- sự phát triển liên tục của tiêu chuẩn,
- Khả năng cho phép bất kỳ ai cũng có thể kiểm tra mã.
- độc lập khỏi những thay đổi về thương mại hoặc chính trị,
- Khả năng phục hồi lâu dài.



Không giống như các hệ thống nhắn tin độc quyền, tương lai của Matrix không phụ thuộc vào một công ty duy nhất, mà phụ thuộc vào cộng đồng toàn cầu và một tiêu chuẩn mở.



## Tôi cần làm gì để tạo tài khoản Matrix?



Việc tạo tài khoản Matrix rất đơn giản và không yêu cầu kỹ năng kỹ thuật nào. Người dùng có thể tham gia máy chủ hiện có, tạo tên đăng nhập và bắt đầu trò chuyện ngay lập tức. Phần này sẽ nêu rõ các bước cần thiết.



### Chọn máy chủ (công cộng hoặc riêng tư)



Matrix là một mạng lưới liên kết: có rất nhiều máy chủ (máy chủ cá nhân) được quản lý bởi các tổ chức, cộng đồng hoặc cá nhân khác nhau. Việc lựa chọn máy chủ chỉ xác định _nơi_ tài khoản được lưu trữ, nhưng không ngăn cản việc giao tiếp với toàn bộ mạng lưới.


Có hai lựa chọn:**



### - Sử dụng máy chủ công cộng



Đây là giải pháp đơn giản nhất.


Ví dụ về các máy chủ phổ biến:





- _matrix.org_ (trang web nổi tiếng nhất)
- _envs.net_
- máy chủ cộng đồng theo chủ đề (công nghệ, quyền riêng tư, mã nguồn mở...)



Các máy chủ này phù hợp với người dùng mới muốn đăng ký nhanh chóng.



### - Sử dụng máy chủ riêng



Thích hợp cho:





- một tổ chức,
- một gia đình,
- một dự án mã nguồn mở,
- một nhóm làm việc,
- hoặc để sử dụng độc lập, tự lưu trữ.



Trong trường hợp này, cần có người quản trị máy chủ (Synapse, Dendrite, Conduit...).


Dù bạn chọn máy chủ nào, người dùng vẫn có thể giao tiếp với nhau nhờ vào tính năng liên kết máy chủ.



### Tạo tài khoản từng bước một



Vì Matrix là một giao thức mở, nên nó có thể được truy cập bởi nhiều ứng dụng khác nhau.


Như đã mô tả ở trên, chúng cung cấp các giao diện và chức năng khác nhau tùy thuộc vào yêu cầu:





- Element**: ứng dụng khách đầy đủ tính năng nhất, có sẵn trên mọi nền tảng.
- FluffyChat**: đơn giản, hiện đại và lý tưởng cho thiết bị di động.
- Nheko**: phần mềm khách hàng nhẹ, tiện dụng dành cho máy tính cá nhân.
- SchildiChat**: Phiên bản Element với những cải tiến về mặt công thái học.
- NeoChat**: được tích hợp vào hệ sinh thái KDE.



Việc lựa chọn ứng dụng khách không ảnh hưởng đến tài khoản: tất cả đều hoạt động với bất kỳ máy chủ Matrix nào.



### Các bước cổ điển:





- Mở ứng dụng đã chọn. Trong trường hợp này, chúng ta sẽ thực hiện điều này với [Element](app.element.io).
- Chọn "Tạo tài khoản".



![cover-kali](assets/fr/10.webp)



Để đơn giản, bạn có thể tạo tài khoản Matrix bằng **Google, Facebook, Apple, GitHub hoặc GitLab**. Các dịch vụ này chỉ biết rằng tài khoản của họ đã được sử dụng để truy cập Matrix: điều này được gọi là **kết nối mạng xã hội**.



Để bảo mật thông tin tốt hơn, bạn cũng có thể đăng ký thủ công bằng cách chọn **tên người dùng**, **mật khẩu** và **địa chỉ email**.



Tùy thuộc vào máy chủ được chọn, bạn có thể cần phải nhập mã **captcha** cũng như chấp nhận **điều khoản sử dụng**.



Sau khi đăng ký được xác nhận, một email xác nhận sẽ được gửi đến bạn.


Chỉ cần nhấp vào liên kết để kích hoạt tài khoản của bạn và truy cập ứng dụng web (Element) để tham gia các cuộc trò chuyện Matrix đầu tiên.



![cover-kali](assets/fr/11.webp)



Giờ bạn đã có tài khoản và đang sử dụng phiên bản web của Element.



## Thêm thông tin liên hệ đầu tiên của bạn



Để liên lạc với ai đó trên Matrix, tất cả những gì bạn cần biết là mã định danh đầy đủ của họ, được gọi là **ID Matrix**.



Ví dụ:



`@alice:matrix.org @bened:monserveur.bj`



### Thêm liên hệ



Để mời bạn bè vào nhóm trò chuyện, hãy nhấp vào biểu tượng hình tròn chữ "i" ở góc trên bên phải. Thao tác này sẽ mở bảng điều khiển bên phải. Nhấp vào "Mọi người" để hiển thị danh sách thành viên trong phòng trò chuyện: hiện tại chỉ có bạn đang có mặt.



![cover-kali](assets/fr/12.webp)



Nhấp vào "Mời vào phòng này" ở đầu danh sách người tham gia và một cửa sổ nhắc sẽ hiện ra để bạn có thể mời bạn bè tham gia Matrix. Nếu họ đã đăng nhập vào Matrix, hãy nhập ID Matrix của họ. Nếu chưa, hãy nhập địa chỉ email của họ và họ sẽ được mời tham gia cùng chúng ta.



Không có hệ thống "bạn bè": một người liên hệ đơn giản chỉ là người mà bạn đã bắt chuyện cùng.



![cover-kali](assets/fr/13.webp)



Người bạn mời có thể chấp nhận hoặc từ chối lời mời. Nếu họ chấp nhận, bạn sẽ thấy họ tham gia vào phòng. Càng đông càng vui!



![cover-kali](assets/fr/14.webp)



### Thiết lập máy chủ của riêng bạn



Matrix thực sự phát huy tối đa hiệu quả khi được sử dụng kết hợp với máy chủ cá nhân.


Việc tự triển khai máy chủ tại nhà cho phép bạn:





- Duy trì quyền kiểm soát hoàn toàn đối với dữ liệu.
- tự định nghĩa các quy tắc sử dụng của riêng mình.
- Quản lý nhiều tài khoản (bạn bè, nhóm, cộng đồng),
- và đảm bảo khả năng phục hồi tối đa trong trường hợp bị hạn chế hoặc kiểm duyệt.



**Các giải pháp hiện có:**





- Synapse**: phiên bản triển khai hoàn chỉnh và mang tính lịch sử nhất.
- Dendrite**: nhẹ hơn, mạnh mẽ hơn và được thiết kế cho tương lai của giao thức.
- Conduit**: một biến thể tối giản, dễ triển khai.



**Điều kiện tiên quyết:**





- một tên miền,
- một máy ảo hoặc VPS,
- Kỹ năng quản trị hệ thống tối thiểu.



Ngay cả khi cần một chút cấu hình, việc tự quản lý máy chủ sẽ biến Matrix thành một công cụ độc lập và bền vững.



### Tham gia các triển lãm thương mại lần đầu tiên của bạn



Matrix phụ thuộc rất nhiều vào _phòng_ (phòng khách).


Có các hội chợ thương mại công cộng, tư nhân, cộng đồng, kỹ thuật, địa phương và quốc tế.



**Ba cách để gia nhập một salon:**



1. **Thông qua liên kết mời** (thường ở dạng URL `matrix.to`).


2. **Tìm kiếm tên salon** trong ứng dụng.


3. **Bằng cách nhập toàn bộ ID chương trình**, ví dụ:


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Sau khi tham gia, phòng chat hoạt động như một nhóm tin tức thông thường, với lịch sử, mã hóa, tệp tin, biểu cảm và cuộc gọi âm thanh/video, tùy thuộc vào ứng dụng khách được sử dụng.



![capture](assets/fr/09.webp)



## Tiến xa hơn



Sau khi nắm vững những kiến thức cơ bản, Matrix cung cấp vô số khả năng nâng cao. Cho dù bạn muốn kết nối với các hệ thống nhắn tin khác, tự vận hành máy chủ riêng hay tổ chức một cộng đồng, hệ sinh thái này đều rất phong phú.



### Các cầu nối (WhatsApp, Telegram, Signal, v.v.)



Một cầu nối kết nối Matrix với các hệ thống nhắn tin khác.


Với ứng dụng này, bạn có thể gửi và nhận tin nhắn từ:





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discord
- Slack**
- IRC** (IRC)
- và nhiều người khác



### Những công dụng của cầu





- Tập trung tất cả các cuộc trò chuyện của bạn vào Matrix.
- Cung cấp giao diện mở để tương tác với các dịch vụ độc quyền.
- Quản lý cộng đồng đa nền tảng từ một vị trí duy nhất.



Một số cây cầu là cầu chính thức, số khác do cộng đồng tự quản lý.


Tùy thuộc vào từng bộ phận, họ có thể yêu cầu:





- một máy chủ cá nhân,
- một cấu hình bổ sung,
- hoặc sử dụng một cây cầu công cộng hiện có.



### Sử dụng Matrix cho một tổ chức, cộng đồng hoặc dự án Bitcoin



Matrix không chỉ là một công cụ cá nhân.


Nó có thể được sử dụng để cơ cấu các nhóm làm việc, tổ chức cộng đồng địa phương hoặc quản lý việc liên lạc trong dự án.



**Ví dụ về cách sử dụng:**





- Cộng đồng mã nguồn mở
- Các dự án hệ sinh thái Bitcoin và Lightning
- Nhóm sinh viên hoặc nhà phát triển
- Các tổ chức công dân
- Truyền thông độc lập
- Các nhóm và hiệp hội địa phương



**Tại sao điều này lại thú vị?**





- Công cụ mã nguồn mở 100%**
- Truyền thông độc lập và phi tập trung**
- Không gian được tổ chức thành **phòng chờ**, **nhóm nhỏ**, **phòng chờ riêng**, v.v.
- Tích hợp với Nextcloud, GitLab, Mattermost hoặc các bot tùy chỉnh.
- Quản lý quyền hạn và kiểm duyệt được tinh chỉnh kỹ lưỡng.



Như vậy, Matrix trở thành trụ cột giao tiếp cho bất kỳ cấu trúc nào muốn duy trì tính độc lập khỏi các nền tảng tập trung lớn.



## Phần kết luận



Matrix đại diện cho một giải pháp hiện đại, mở và an toàn cho giao tiếp thời gian thực, cung cấp một lựa chọn phi tập trung thay thế cho các nền tảng truyền thống. Nhờ kiến trúc liên kết và các giao thức mã hóa tiên tiến, nó cho phép người dùng duy trì quyền kiểm soát dữ liệu của họ trong khi vẫn tận hưởng trải nghiệm mượt mà và khả năng tương tác cao. Cho dù là sử dụng cá nhân, chuyên nghiệp hay cộng đồng, Matrix đều cung cấp một khung mạnh mẽ và có khả năng mở rộng để xây dựng môi trường giao tiếp phù hợp với nhu cầu hiện nay.



Để tìm hiểu thêm và khám phá tất cả các tính năng mà Matrix cung cấp, bạn có thể tham khảo tài liệu chính thức có sẵn tại đây:


[https://matrix.org/docs/](https://matrix.org/docs/)