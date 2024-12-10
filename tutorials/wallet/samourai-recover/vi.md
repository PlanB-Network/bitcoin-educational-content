---
name: Khôi phục tiền trên Samourai Wallet
description: Làm thế nào để khôi phục bitcoin bị kẹt trên Samourai Wallet?
---
![cover](assets/cover.webp)

Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, một số chức năng của ứng dụng hiện không hoạt động, và người dùng không có Dojo riêng của họ không thể phát sóng giao dịch nữa.

Sau khi hỗ trợ một số người dùng khôi phục bitcoin của họ trong những ngày gần đây, tôi tin rằng mình đã gặp phải hầu hết các vấn đề có thể xảy ra trong quá trình khôi phục một ví Samourai. Do đó, hướng dẫn này sẽ bắt đầu với một bản báo cáo về tình hình để xác định các chức năng vẫn còn hoạt động và những chức năng không còn khả dụng trong hệ sinh thái Samourai Wallet và phần mềm bị ảnh hưởng bởi sự cố này. Tiếp theo, chúng ta sẽ tiến hành từng bước để khôi phục một ví Samourai sử dụng phần mềm Sparrow Wallet. Chúng ta sẽ xem xét tất cả các trở ngại tiềm ẩn có thể gặp phải trong quá trình này và tìm cách để giải quyết chúng. Cuối cùng, trong phần cuối, bạn sẽ tìm hiểu các rủi ro tiềm ẩn đối với quyền riêng tư của bạn sau khi máy chủ bị tịch thu.

*Một lời cảm ơn lớn đến [@Louferlou](https://twitter.com/Louferlou), người đã hỗ trợ một số người dùng trong quá trình khôi phục của họ và đã chia sẻ kinh nghiệm với tôi, và cũng đã đóng góp vào việc kiểm tra để xác định những gì vẫn còn hoạt động.*

## Samourai Wallet vẫn hoạt động chứ?

Có, **ứng dụng Samourai Wallet vẫn hoạt động**, nhưng dưới một số điều kiện nhất định.

Đầu tiên, điều cần thiết là ứng dụng đã được cài đặt trước đó trên điện thoại thông minh của bạn. Google Play Store đã gỡ bỏ ứng dụng, và APK được lưu trữ trên trang web đã bị tịch thu. Do đó, việc cài đặt Samourai vào lúc này khá phức tạp. Bạn có thể tìm thấy APK trực tuyến, nhưng tôi khuyên bạn không nên tải chúng trừ khi bạn chắc chắn về nguồn gốc.

Vì trang Samourai Wallet không còn có sẵn trên Google Play Store, không thể vô hiệu hóa cập nhật tự động. Nếu ứng dụng quay trở lại các nền tảng tải xuống, sẽ khôn ngoan khi **vô hiệu hóa cập nhật tự động** cho đến khi có thêm thông tin về sự phát triển của vụ việc.

Nếu Samourai Wallet đã được cài đặt trên điện thoại thông minh của bạn, bạn vẫn có thể truy cập ứng dụng. Để sử dụng chức năng ví của Samourai, điều cần thiết là kết nối với một Dojo. Trước đây, người dùng không có Dojo cá nhân phụ thuộc vào máy chủ của Samourai để truy cập thông tin blockchain Bitcoin và để phát sóng giao dịch. Với việc các máy chủ này bị tịch thu, ứng dụng không thể truy cập dữ liệu này nữa.
Nếu bạn không có Dojo được kết nối trước đó nhưng bây giờ có, bạn có thể thiết lập nó để sử dụng lại ứng dụng Samourai Wallet của mình. Điều này bao gồm việc kiểm tra bản sao lưu của bạn, xóa ví (lưu ý, xoá ví, không phải ứng dụng), và khôi phục ví bằng cách kết nối Dojo của bạn với ứng dụng. Để biết thêm chi tiết về các bước này, bạn có thể tham khảo [hướng dẫn này, trong phần "_Chuẩn bị Ví Samourai của bạn_": COINJOIN - DOJO](https://planb.network/en/tutorials/privacy/coinjoin-dojo).
Nếu ứng dụng Samourai Wallet của bạn đã được kết nối với Dojo của riêng bạn, thì phần ví sẽ hoạt động trơn tru cho bạn. Bạn vẫn có thể xem số dư và phát sóng giao dịch. Mặc cho tất cả những gì đang xảy ra, tôi nghĩ Samourai Wallet vẫn là phần mềm ví di động tốt nhất vào lúc này. Cá nhân tôi dự định tiếp tục sử dụng nó.
Vấn đề chính bạn có thể gặp phải là không thể truy cập vào các tài khoản Whirlpool từ ứng dụng. Thông thường, Samourai cố gắng thiết lập kết nối với Whirlpool CLI của bạn và bắt đầu các chu kỳ trộn coin trước khi cho bạn truy cập vào các tài khoản này. Tuy nhiên, do kết nối này không còn khả thi, ứng dụng tiếp tục tìm kiếm mà không bao giờ cho bạn truy cập vào các tài khoản Whirlpool. Trong trường hợp này, bạn có thể khôi phục các tài khoản này trên một phần mềm ví khác trong khi chỉ giữ tài khoản gửi tiền trên Samourai.

### Công cụ nào vẫn còn sẵn có trên Samourai?

Một số công cụ bị ảnh hưởng bởi việc tắt máy chủ hoặc hoàn toàn không khả dụng.

Về công cụ chi tiêu cá nhân, mọi thứ vẫn hoạt động bình thường miễn là, tất nhiên, bạn có Dojo riêng của mình. Giao dịch Stonewall (không phải Stonewall x2) hoạt động bình thường mà không có vấn đề gì.

Các bình luận trên Twitter đã chỉ ra rằng, có thể là bây giờ, sự riêng tư được cung cấp bởi một giao dịch Stonewall đã giảm. Giá trị cộng thêm của một giao dịch Stonewall nằm ở chỗ nó không thể phân biệt được với một giao dịch Stonewall x2 về cấu trúc. Khi một nhà phân tích gặp phải mẫu cụ thể này, họ không thể xác định liệu đó là một Stonewall tiêu chuẩn với một người dùng duy nhất hay một Stonewall x2 liên quan đến hai người dùng. Tuy nhiên, như chúng ta sẽ thấy trong các phần sau, việc thực hiện giao dịch Stonewall x2 đã trở nên phức tạp hơn do sự không khả dụng của Soroban. Một số người do đó nghĩ rằng, giờ đây, một nhà phân tích có thể giả định rằng bất kỳ giao dịch nào với cấu trúc này là một Stonewall bình thường. Cá nhân tôi không đồng ý với giả định này. Mặc dù các giao dịch Stonewall x2 có thể ít phổ biến hơn (và tôi nghĩ chúng đã ít phổ biến như vậy trước sự cố này), thực tế là chúng vẫn có thể làm vô hiệu một phân tích dựa trên giả định rằng chúng không phải là.
**[-> Tìm hiểu thêm về giao dịch Stonewall.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**
Về Ricochet, tôi chưa thể xác minh liệu dịch vụ này vẫn còn hoạt động hay không, do không sở hữu một Dojo trên Testnet, và tôi không muốn mạo hiểm chi tiêu `100 000 sats` vào một ví có thể được kiểm soát bởi cơ quan chức năng. Nếu bạn đã có cơ hội thử nghiệm công cụ này gần đây, rất mong liên hệ với tôi để chúng tôi có thể cập nhật bài viết này.

Nếu bạn cần sử dụng Ricochet, hãy biết rằng bạn vẫn có thể thực hiện thao tác này một cách thủ công với bất kỳ phần mềm ví nào. Để tìm hiểu cách thực hiện các bước nhảy một cách thủ công một cách đúng đắn, tôi khuyên bạn nên tham khảo bài viết khác này: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

Công cụ JoinBot không còn hoạt động, vì nó hoàn toàn phụ thuộc vào sự tham gia của một ví được quản lý bởi Samourai.

Về các loại giao dịch hợp tác khác, thường được gọi là "cahoots," chúng vẫn có thể thực hiện, nhưng chỉ theo cách thủ công. Trước khi máy chủ bị tắt, bạn có hai lựa chọn để thực hiện giao dịch Stonewall x2 hoặc Stowaway (PayJoin):
- Sử dụng mạng Soroban để tự động và trao đổi từ xa các PSBT;
- Hoặc thực hiện các giao dịch này theo cách thủ công bằng cách quét nhiều mã QR.

Sau một số lần thử nghiệm, có vẻ như Soroban không còn hoạt động. Để thực hiện các giao dịch hợp tác này, việc trao đổi dữ liệu phải được thực hiện một cách thủ công. Dưới đây là hai lựa chọn để thực hiện việc trao đổi này:
- Nếu bạn ở gần người hợp tác về mặt vật lý, bạn có thể quét các mã QR liên tiếp;
- Nếu bạn ở xa người cộng tác, bạn có thể trao đổi PSBTs thông qua một kênh liên lạc bên ngoài ứng dụng. Tuy nhiên, hãy cẩn thận, vì dữ liệu trong các PSBTs này rất nhạy cảm về mặt quyền riêng tư. Tôi khuyên bạn nên sử dụng dịch vụ nhắn tin mã hóa để đảm bảo tính bảo mật của việc trao đổi.
**[-> Tìm hiểu thêm về giao dịch Stonewall x2.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4-x2)**

**[-> Tìm hiểu thêm về giao dịch Stowaway.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**

Về Whirlpool, giao thức này dường như không còn hoạt động, ngay cả đối với những người dùng có Dojo riêng của họ. Tôi đã theo dõi RoninDojo của mình trong những ngày qua và thử nghiệm một số thao tác cơ bản, nhưng Whirlpool CLI không thể kết nối kể từ khi máy chủ ngừng hoạt động.

Tuy nhiên, tôi vẫn hy vọng rằng giao thức này có thể được kích hoạt lại hoặc có thể được tái tạo lại theo một cách khác trong những tuần tới, tùy thuộc vào diễn biến của sự việc bắt giữ. Sự tạm dừng này có thể là cơ hội để khám phá các phương pháp mới hoặc cải tiến tiềm năng cho hệ thống này.
### Công cụ bên ngoài nào vẫn còn có sẵn để dùng?
Về các công cụ khác liên quan đến môi trường Samourai, một số vẫn còn sẵn dùng trong khi một số khác thì không.

Trang web phân tích chuỗi miễn phí OXT.me hiện tại không còn sẵn dùng.

Công cụ Whirlpool Stats Tool không còn sẵn dùng để tải xuống, vì nó được lưu trữ trên GitLab của Samourai. Ngay cả khi bạn đã tải công cụ Python này về máy tính cục bộ trước đó, hoặc nếu nó đã được cài đặt trên node RoninDojo của bạn, WST sẽ không hoạt động trong thời gian này. Thực tế, nó phụ thuộc vào dữ liệu được cung cấp bởi OXT.me để hoạt động, và trang web này hiện không còn truy cập được. Hiện tại, WST không đặc biệt hữu ích vì giao thức Whirlpool đang không hoạt động.

Trang web KYCP.org hiện tại không còn truy cập được.

GitLab lưu trữ mã cho công cụ Boltzmann Calculator Python cũng đã bị thu giữ. Vì vậy, hiện tại không thể tải xuống công cụ này. Nhưng nếu bạn có một RoninDojo, bạn có thể tiếp tục sử dụng Boltzmann Calculator như trước đây.

Về RoninDojo, phần mềm node-in-box này vẫn tiếp tục hoạt động bình thường bất chấp sự không khả dụng của một số công cụ cụ thể như Whirlpool CLI và WST. Nó vẫn có thể được sử dụng cho phần mềm ví khác nhờ vào Fulcrum hoặc Electrs. Nếu bạn muốn có thêm thông tin về RoninDojo hoặc nếu bạn có câu hỏi cụ thể, tôi khuyên bạn nên tham gia [nhóm Telegram của họ](https://t.me/RoninDojoNode).

Tuy nhiên, mã nguồn cho RoninDojo hiện tại không còn truy cập được, vì nó được lưu trữ trên GitLab của Samourai. Vì vậy, hiện tại không thể cài đặt thủ công nó trên Raspberry Pi.

Về phần mềm ví chỉ dùng để xem Sentinel, tình hình tương tự như ứng dụng Samourai. Nếu bạn có Dojo riêng, bạn có thể tiếp tục sử dụng Sentinel mà không gặp vấn đề gì. Tuy nhiên, nếu bạn không có Dojo, bạn sẽ không thể thiết lập kết nối. Khác với Samourai, trang web của Sentinel vẫn còn truy cập được trực tuyến. Nhưng hãy cẩn thận với trang web này và APK được cung cấp ở đó, vì hiện nay không rõ ai đang kiểm soát những nguồn lực này.

### Sparrow Wallet có bị ảnh hưởng không?
Ví Sparrow vẫn hoạt động bình thường, ngoại trừ các công cụ của Samourai không còn khả dụng. Hiện tại, việc thực hiện trộn coin qua Sparrow không còn khả thi. Tương tự, các công cụ chi tiêu cộng tác cũng không còn truy cập được, vì Sparrow không cung cấp tùy chọn trao đổi PSBTs thủ công, không giống như Samourai. Đối với tất cả các chức năng khác, Sparrow hoạt động bình thường, không gặp vấn đề gì. Bạn cũng có thể sử dụng phần mềm này để khôi phục ví Samourai nếu cần thiết.

## Làm thế nào để khôi phục ví Samourai?
Như chúng ta đã thấy ở các phần trước, nếu bạn tự sở hữu Dojo của mình, không nhất thiết phải chuyển đổi phần mềm. **Samourai vẫn một lựa chọn ví nóng tuyệt vời** cho việc chi tiêu hàng ngày của bạn. Tuy nhiên, nếu bạn không có Dojo hoặc nếu bạn muốn chọn một phần mềm khác, tôi sẽ giải thích quy trình khôi phục đầy đủ, chi tiết về bất kỳ trở ngại tiềm ẩn nào bạn có thể gặp phải.

Dù sao, điều quan trọng là phải dành thời gian và đảm bảo không mắc lỗi. Hãy nhớ rằng, không cần vội, vì bạn giữ chìa khóa riêng tư của mình, và việc tịch thu máy chủ của Samourai không ảnh hưởng đến điều này theo bất kỳ cách nào. Dù có chuyện gì xảy ra, họ rõ ràng không thể truy cập vào chìa khóa riêng tư của bạn.

### Xác minh cụm từ bí mật

Để khôi phục ví của mình, bạn phải có cụm từ bí mật, ngay cả khi bạn chọn khôi phục qua tệp sao lưu. Bắt đầu bằng cách xác minh tính hợp lệ của cụm từ bí mật này. Mở ứng dụng Samourai Wallet của bạn, nhấp vào biểu tượng Paynym ở góc trên bên trái, sau đó chọn `Cài đặt - Settings`.

![samourai](assets/1.webp)

Tiếp theo, nhấp vào `Troubleshooting` và sau đó là `Passphrase/backup test`.

![samourai](assets/2.webp)

Nhập cụm từ bí mật của bạn và nhấp `Ok`. Nếu đúng, Samourai sẽ xác nhận. Bạn cũng có tùy chọn để xác minh tệp sao lưu nếu bạn dự định sử dụng nó sau này.

![samourai](assets/3.webp)

Bước này là tùy chọn nhưng được khuyến khích. Nó xác nhận rằng cụm từ bí mật là chính xác, loại bỏ một vấn đề phát sinh tiềm ẩn sau này. Nếu Samourai chỉ ra rằng cụm từ bí mật không chính xác ở giai đoạn này, việc khôi phục sẽ không thể thực hiện được. Đảm bảo bạn đã nhập cụm từ bí mật chính xác và kiểm tra lại.

### Tùy chọn 1: Khôi phục ví trên Sparrow với tệp sao lưu

Kể từ phiên bản 1.8.6 của Sparrow Wallet, việc nhập trực tiếp ví Samourai của bạn sử dụng tệp văn bản sao lưu có tên `samourai.txt`, mà ứng dụng của bạn tự động tạo ra, đã trở nên khả thi. Tệp này chứa tất cả các thông tin cần thiết để khôi phục ví của bạn và được mã hóa bằng cụm từ bí mật của bạn để đảm bảo an toàn.

Nếu bạn chọn tùy chọn này, bạn sẽ cần tệp `samourai.txt` và cụm từ bí mật của bạn. Để tạo tệp này trên Samourai Wallet, nhấp vào ba chấm nhỏ ở góc trên bên phải, sau đó chọn `Xuất bản sao lưu ví - Export wallet backup`.

![samourai](assets/4.webp)
Sau đó, chọn `Export to Clipboard`. Sau đó, bạn sẽ cần chuyển tệp này sang PC của mình một cách an toàn. Vì tệp được mã hóa, nhưng chỉ cần cụm từ bí mật là đủ để giải mã, nên việc sử dụng các biện pháp phòng ngừa trong quá trình truyền tải là quan trọng. Nếu bạn chọn chuyển trực tiếp dưới dạng văn bản thuần túy, bạn sẽ cần tạo một tệp `samourai.txt` trên PC của mình và dán nội dung của bảng tạm vào đó. Một phương án khác là trực tiếp lấy tệp `samourai.txt` từ các tệp được lưu trữ trên điện thoại của bạn.
Khi bạn có quyền truy cập vào tệp trên PC, mở Ví Sparrow, nhấp vào tab `File`, và chọn `Import Wallet` để bắt đầu nhập ví của bạn.

![samourai](assets/5.webp)
Cuộn xuống đến `Samourai Backup`, nhấp vào `Import File`, và sau đó chọn tệp `samourai.txt` của bạn.
![samourai](assets/6.webp)

Sparrow sau đó sẽ yêu cầu bạn nhập mật khẩu để giải mã file. Mật khẩu này thực chất là passphrase. Nhập nó vào trường tương ứng và nhấp vào `Import`.

![samourai](assets/7.webp)

Nếu ở giai đoạn này, ví của bạn không xuất hiện, có thể bạn đã mắc lỗi khi sao chép file `samourai.txt` hoặc khi nhập cụm từ bí mật. Bạn có thể tham khảo phần khắc phục sự cố để được trợ giúp thêm.

![samourai](assets/8.webp)

Đối với loại kịch bản, nếu bạn chưa cấu hình các kịch bản khác trong Samourai, bạn nên sử dụng chỉ SegWit V0 (Native SegWit / P2WPKH). Giữ kịch bản mặc định này và nhấp vào `Import`.

![samourai](assets/9.webp)

Đặt tên cho ví của bạn, ví dụ, "Samourai Recovery", và sau đó nhấp vào `Create Wallet`.

![samourai](assets/10.webp)

Sparrow sau đó sẽ yêu cầu bạn chọn một mật khẩu. Mật khẩu này chỉ bảo vệ quyền truy cập vào ví của bạn trên PC này và không liên quan đến việc tạo ra các khóa của ví. Hãy chắc chắn chọn một mật khẩu mạnh, ghi chú lại để nhớ, và nhấp vào `Set Password`.

![samourai](assets/11.webp)

Sparrow sau đó sẽ tạo ra các khóa của ví và tìm kiếm các giao dịch tương ứng.

![samourai](assets/12.webp)

Hiện tại, chỉ có tài khoản gửi tiền của bạn là có thể truy cập. Nếu bạn chỉ sử dụng Samourai cho tài khoản này, bạn nên thấy tất cả số tiền của mình. Tuy nhiên, nếu bạn cũng sử dụng Whirlpool, bạn sẽ cần phải tạo ra các tài khoản `premix`, `postmix`, và `badbank`. Trên Sparrow, chỉ cần nhấp vào tab `Settings`, sau đó vào `Add Accounts...`.

![samourai](assets/13.webp)
Trong cửa sổ mở ra, chọn `Whirlpool Accounts` từ menu thả xuống, sau đó nhấp vào `OK`.
![samourai](assets/14.webp)

Sau đó, bạn sẽ thấy các tài khoản Whirlpool của mình xuất hiện, và Sparrow sẽ tạo ra các khóa cần thiết để sử dụng các quỹ bitcoin liên quan.

![samourai](assets/15.webp)

Nếu bạn sử dụng phần mềm khác ngoài Sparrow, như Electrum, để khôi phục ví Samourai của mình, đây là các chỉ số tài khoản Whirlpool cho việc khôi phục thủ công:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Bây giờ bạn đã có quyền truy cập vào bitcoin của mình trên Sparrow. Nếu bạn cần trợ giúp sử dụng Sparrow Wallet, bạn cũng có thể xem [hướng dẫn chuyên dụng của chúng tôi](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Tôi cũng khuyên bạn nên nhập thủ công lại các nhãn bạn đã liên kết với các UTXO trên Samourai. Điều này sẽ cho phép bạn kiểm soát coin của mình hiệu quả trên Sparrow sau này.

### Lựa chọn 2: Khôi phục ví trên Sparrow bằng cụm từ khôi phục

Nếu bạn không muốn thực hiện việc khôi phục bằng tệp sao lưu, bạn có thể chọn một phương pháp truyền thống hơn bằng cách sử dụng cụm từ khôi phục 12 từ và passphrase của bạn. Lựa chọn thứ hai này thường đơn giản hơn.
Để bắt đầu, hãy chắc chắn bạn có sẵn cụm từ khôi phục và passphrase của mình trong tay. Sau đó, mở phần mềm Sparrow Wallet, nhấp vào tab `File`, và chọn `Import Wallet` để bắt đầu nhập ví của bạn.
![samourai](assets/16.webp)

Chọn `Mnemonic Words (BIP39)` và, trong menu thả xuống, nhấp vào `Use 12 Words`.

![samourai](assets/17.webp)

Nhập 12 từ của cụm từ khôi phục của bạn theo đúng thứ tự.

![samourai](assets/18.webp)

Nếu Sparrow hiển thị thông báo `Invalid Checksum`, điều này chỉ ra rằng checksum của cụm từ khôi phục không hợp lệ, có nghĩa là bạn có thể đã nhập sai các từ.

![samourai](assets/19.webp)

Nếu cụm từ của bạn chính xác, click chọn hộp `Use Passphrase?` và nhập passphrase của bạn vào trường dành riêng. Cuối cùng, nếu mọi thứ dường như chính xác, nhấp vào nút `Discover Wallet`.

![samourai](assets/20.webp)

Đặt tên cho ví của bạn, ví dụ, "Samourai Recovery", sau đó nhấp vào `Create Wallet`.

![samourai](assets/21.webp)
Sparrow sau đó sẽ yêu cầu bạn chọn một mật khẩu. Mật khẩu này chỉ bảo vệ quyền truy cập vào ví của bạn trên PC này và không liên quan đến việc tạo ra các khóa của ví. Hãy chắc chắn chọn một mật khẩu mạnh, ghi lại để nhớ, và nhấp vào `Set Password`.
![samourai](assets/22.webp)

Sparrow sau đó sẽ tạo ra các khóa cho ví của bạn và tìm kiếm các giao dịch tương ứng.

![samourai](assets/23.webp)

Nếu ở giai đoạn này, ví của bạn không xuất hiện, có thể bạn đã nhập sai cụm từ mật khẩu hoặc passphrase. Bạn có thể tham khảo phần hướng dẫn khắc phục sự cố dành riêng để được giúp đỡ thêm.

Hiện tại, chỉ có tài khoản gửi tiền của bạn là có thể truy cập. Nếu bạn chỉ sử dụng Samourai cho tài khoản này, bạn sẽ thấy tất cả số tiền của mình. Tuy nhiên, nếu bạn cũng sử dụng Whirlpool, bạn sẽ cần phải tạo ra các tài khoản `premix`, `postmix`, và `badbank`. Trên Sparrow, chỉ cần nhấp vào tab `Settings`, sau đó vào `Add Accounts...`.

![samourai](assets/24.webp)

Trong cửa sổ mở ra, chọn `Whirlpool Accounts` từ danh sách thả xuống, sau đó nhấp vào `OK`.

![samourai](assets/25.webp)

Bạn sẽ thấy các tài khoản Whirlpool của mình xuất hiện, và Sparrow sẽ tạo ra các khóa cần thiết để sử dụng các quỹ bitcoin liên quan.

![samourai](assets/26.webp)

Nếu bạn đang sử dụng phần mềm khác như Electrum để khôi phục ví Samourai của mình, đây là các chỉ số của tài khoản Whirlpool cho việc khôi phục thủ công:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Bây giờ bạn đã có quyền truy cập vào bitcoin của mình trên Sparrow. Nếu bạn cần trợ giúp sử dụng Sparrow Wallet, bạn cũng có thể tham khảo [hướng dẫn dành riêng của chúng tôi](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Tôi cũng khuyên bạn nên nhập thủ công lại các nhãn bạn đã liên kết với các UTXO của mình trên Samourai. Điều này sẽ giúp bạn kiểm soát coin của mình hiệu quả trên Sparrow sau này.

### Những vấn đề thường gặp là gì?
Sau khi hỗ trợ nhiều người trong những ngày qua, tôi tin rằng mình đã gặp phải hầu hết các vấn đề có thể cản trở việc khôi phục ví của bạn. Nếu bạn vẫn không thể truy cập vào ví của mình dù đã thực hiện theo các hướng dẫn trước đó, dưới đây là một số khuyến nghị bổ sung. Đầu tiên và quan trọng nhất, để việc khôi phục thành công, điều tuyệt đối cần thiết là cụm từ khôi phục phải chính xác. Nếu bạn không thể tìm thấy cụm từ 12 từ của mình, bạn có thể sử dụng *tùy chọn 1* để khôi phục từ tệp sao lưu của Samourai. Bạn cũng có thể truy cập cụm từ khôi phục trực tiếp trong Samourai Wallet bằng cách đi đến `Cài đặt - Settings`, sau đó là `Ví - Wallet`, và cuối cùng chọn `Hiển thị cụm từ khôi phục 12 từ - Show 12-ửod recovery phrase`.

Tiếp theo, một lỗi đánh máy trong cụm từ bí mật của bạn trong quá trình khôi phục cũng sẽ dẫn đến việc tạo ra các khóa sai, điều này sẽ ngăn chặn việc khôi phục ví của bạn trên Sparrow. **Cụm từ bí mật phải hoàn toàn chính xác!**

Để giải quyết điều này, đầu tiên, tôi khuyên bạn nên kiểm tra tính hợp lệ của cụm từ bí mật của mình trong ứng dụng Samourai như được mô tả trong phần "_Xác minh cụm từ bí mật_" của bài viết này:
1. **Xác nhận trong Samourai:** Nếu Samourai xác nhận rằng cụm từ bí mật là chính xác, hãy thử lại việc khôi phục từ đầu, đảm bảo nhập chính xác cụm từ bí mật trong Sparrow mà không có lỗi;
2. **Lỗi passphrase:** Nếu Samourai chỉ ra rằng passphrase không chính xác, việc tiếp tục thử nghiệm trên Sparrow là vô ích. Miễn là passphrase chính xác không được tìm thấy, việc khôi phục ví của bạn là không thể. Nếu bạn đã mất vĩnh viễn passphrase của mình, hãy giữ ứng dụng Samourai của bạn an toàn. Tất cả những gì bạn có thể làm là hy vọng rằng các máy chủ được khởi động lại để bạn có thể thực hiện các giao dịch trực tiếp từ ứng dụng mà không cần khôi phục. **Không cố gắng kết nối với một Dojo trong trường hợp này**, vì điều này sẽ đồng nghĩa với việc đặt lại ví của bạn trên Samourai, điều này yêu cầu truy cập vào passphrase.

Trong số các lỗi khác đã gặp, nhiều lỗi liên quan đến cấu hình mạng trên Sparrow.

Đầu tiên, đảm bảo rằng Sparrow được cấu hình đúng cách trong chế độ `mainnet` thay vì chế độ `testnet`. Thực sự, nếu Sparrow tìm kiếm các giao dịch của bạn trên Testnet, nó sẽ không tìm thấy gì, bởi vì ví của bạn ở trên Mainnet. Testnet là một phiên bản thay thế của Bitcoin, chỉ được sử dụng cho việc thử nghiệm và phát triển, và hoạt động trên một mạng riêng biệt so với mạng chính (Mainnet), với các khối và giao dịch riêng của nó. Để kiểm tra bạn đang ở trên mạng nào, nhấp vào tab `Công cụ - Tools`, sau đó là `Khởi động lại trong - Restart In`. Nếu tùy chọn `Mainnet` được hiển thị, thì bạn không ở trên mạng chính. Chọn nó để khởi động lại Sparrow trên Mainnet, và sau đó bắt đầu lại quá trình khôi phục của bạn.

![samourai](assets/27.webp)
Một số người cũng gặp khó khăn khi kết nối Sparrow với node của họ. Ở góc dưới bên phải của Sparrow, một công tắc màu sắc chỉ ra liệu phần mềm của bạn có được kết nối chính xác với một node Bitcoin hay không. Để truy xuất các giao dịch Samourai của bạn, việc phần mềm được kết nối tốt là cần thiết. Kiểm tra xem công tắc đã được kích hoạt chưa, như trong hình dưới đây của tôi (vàng cho một node công cộng, xanh lá cho Bitcoin Core, và xanh dương cho một máy chủ Electrum).
![samourai](assets/28.webp)

Nếu công tắc không được kích hoạt, nhấp vào nó để kích hoạt lại kết nối.

![samourai](assets/29.webp)

Nếu vấn đề vẫn tiếp tục tồn tại, dưới đây là một số giải pháp có thể:
- Nếu bạn đang cố gắng kết nối với máy chủ Electrum của riêng mình (xanh dương) hoặc Bitcoin Core của mình (xanh lá) và Sparrow không thể kết nối, kiểm tra thông tin kết nối dưới `File > Preferences... > Server`;

![samourai](assets/30.webp)
- Nếu vấn đề kết nối vẫn tiếp tục, có thể do việc đồng bộ hóa node của bạn chưa hoàn tất. Đảm bảo rằng node và indexer của bạn đã được đồng bộ hóa 100%. Nếu cần thiết, như một biện pháp cuối cùng, hãy ngắt kết nối node của bạn khỏi Sparrow và kết nối với một node công cộng;
- Nếu bạn đã kết nối với một node công cộng và kết nối thất bại, hãy thử thay đổi node bằng cách chọn một node khác từ danh sách thả xuống.

![samourai](assets/31.webp)

Nếu bạn đã khôi phục ví của mình thành công, nhưng nó có vẻ không đầy đủ, có thể có một vấn đề liên quan đến sự phái sinh.

Vấn đề có thể xảy ra nếu bạn đã sử dụng tài khoản gửi tiền Samourai với một loại script khác so với `P2WPKH`. Mặc định, Samourai sử dụng loại script này, nhưng nếu bạn đã thay đổi nó một cách thủ công, bạn cũng cần phải điều chỉnh điều này khi khôi phục trên Sparrow.

Để phái sinh các nhánh cho các loại script khác, bạn cần phải lặp lại quá trình khôi phục cho mỗi loại script đã sử dụng. Để làm điều này, vào `File > New Wallet` trên Sparrow, chọn một loại script khác từ danh sách thả xuống, nhấp vào `New or Imported Software Wallet`, và làm theo các bước giống như trong hướng dẫn ban đầu.

![samourai](assets/32.webp)

Một vấn đề phái sinh khác mà tôi gặp phải liên quan đến giá trị Gap Limit. Giá trị này cho Sparrow biết sau bao nhiêu địa chỉ trống nó nên dừng việc phái sinh địa chỉ mới. Nếu sau khi khôi phục, bạn nhận thấy một số giao dịch bị thiếu, điều này có thể do Gap Limit quá thấp. Để giải quyết vấn đề này, vào tài khoản đang gây ra vấn đề, ví dụ như tài khoản postmix (nếu có nhiều tài khoản liên quan, lặp lại thao tác này cho mỗi tài khoản).

![samourai](assets/33.webp)

Nhấp vào tab `Settings` và sau đó vào nút `Advanced...`.
![samourai](assets/34.webp)
Tăng dần giá trị của Gap Limit, ví dụ, tôi đã đặt nó là `400` ở đây. Sau đó, nhấp vào nút `Close`.

![samourai](assets/35.webp)

Nhấp vào `Apply` để hoàn tất. Sparrow sau đó sẽ phái sinh ra một số lượng lớn hơn các địa chỉ và tìm kiếm tiền trên chúng, điều này nên giúp khôi phục tất cả các giao dịch của bạn.

![samourai](assets/36.webp)

Đó là các vấn đề khôi phục mà tôi đã gặp phải trong những ngày qua. Nếu, sau khi thử tất cả các giải pháp này, bạn vẫn gặp rắc rối, tôi mời bạn tham gia [Discord Discover Bitcoin](https://discord.gg/xKKm29XGBb) để yêu cầu giúp đỡ. Tôi thường xuyên hiện diện Discord này và sẽ rất vui được giúp đỡ nếu tôi có giải pháp. Các bitcoiner khác cũng sẽ có thể chia sẻ kinh nghiệm của họ và cung cấp sự hỗ trợ của họ. **Dù trong trường hợp nào, việc giữ bí mật cụm từ khôi phục, tệp sao lưu, và passphrase của bạn là cực kỳ quan trọng**. Đừng chia sẻ chúng với bất kỳ ai, vì điều này có thể cho phép họ ăn cắp bitcoin của bạn.

Một khi việc khôi phục hoàn tất, bạn giờ đây có quyền truy cập vào bitcoin của mình. Đó là một điều tốt, nhưng có thể không đủ. Thực tế, việc tịch thu máy chủ nảy sinh những rủi ro tiềm ẩn mới cho quyền riêng tư của bạn. Trong phần tiếp theo, chúng ta sẽ xem xét chi tiết những rủi ro này và đề cập đến các biện pháp phòng ngừa để bảo vệ quyền riêng tư của bạn.

## Hậu quả đối với quyền riêng tư trong các giao dịch của bạn là gì?

### Là một người dùng Samourai không có Dojo

Nếu bạn đã sử dụng Samourai Wallet mà không kết nối với Dojo của riêng mình, xpubs của bạn phải được thông báo cho máy chủ của Samourai để ứng dụng hoạt động. Với việc tịch thu các máy chủ này, có khả năng giờ đây các cơ quan chức năng có quyền truy cập vào các xpubs này.
Kịch bản này vẫn là giả định. Chúng ta không biết liệu các xpub này đã được ghi lại hay không, liệu có bất kỳ kho lưu trữ tiềm năng nào đã bị phá hủy hay chưa, liệu cơ quan chức năng đã thu hồi chúng, và liệu họ có kế hoạch sử dụng chúng cho phân tích chuỗi hay không. Tuy nhiên, trong tình huống như vậy, việc cân nhắc kịch bản xấu nhất, nơi mà cơ quan chức năng có các xpub của người dùng không kết nối với Dojo của riêng họ là điều hợp lý và cần thiết.

Để tham khảo, một xpub là một chuỗi ký tự chứa tất cả các yếu tố cần thiết để tạo ra các khóa công khai con (khóa công khai + mã chuỗi). Nó được sử dụng trong ví tất định phân cấp - HD để tạo địa chỉ nhận và quan sát các giao dịch của một tài khoản mà không tiết lộ các khóa riêng tư liên quan. Điều này cho phép, ví dụ, tạo một ví "chỉ xem - watch-only". Tuy nhiên, việc tiết lộ xpubs có thể làm lộ thông tin cá nhân của người dùng, vì chúng cho phép bên thứ ba theo dõi các giao dịch và xem số dư của các tài khoản liên quan.
Bất kỳ ai biết xpubs của bạn có thể nhìn thấy tất cả các địa chỉ nhận của ví bạn, những địa chỉ đã sử dụng trong quá khứ và những địa chỉ sẽ được tạo ra trong tương lai.

Đối với người dùng không có Dojo, việc rò rỉ xpubs của bạn có hai hậu quả lớn:
- Các giao dịch trộn coin của bạn có thể đã thực hiện trở nên không hiệu quả từ góc độ bảo mật cho bất kỳ ai biết xpubs của bạn, do đó, tiền của bạn mất hết tính ẩn danh;
- Người này cũng có thể theo dõi tất cả các địa chỉ nhận của ví Samourai của bạn.

Do đó, việc cân nhắc kịch bản xấu nhất và từ bỏ ví này, chiếc ví có thể đã bị xâm phạm về mặt quyền riêng tư, là điều quan trọng. Để làm điều này, tạo một ví mới từ đầu với phần mềm khác, như Sparrow Wallet. Sau khi xác minh tính hợp lệ của bản sao lưu ví mới, chuyển tất cả số dư của bạn bằng cách thực hiện giao dịch. Mặc dù hoạt động này không phá vỡ liên kết theo dõi tiền của bạn, nhưng nó sẽ ngăn cơ quan chức năng biết chắc chắn các địa chỉ trên ví mới của bạn.

Trong quá trình chuyển này, tôi khuyên bạn nên tránh hợp nhất tiền của mình. Nếu chúng ta giả sử rằng xpubs của bạn bị xâm phạm, việc gộp sẽ không có tác động từ quan điểm của người có quyền truy cập vào các xpubs này, vì quyền riêng tư của bạn đã bị xâm phạm với họ. Tuy nhiên, tôi khuyên bạn không nên hợp nhất tiền của mình quá nhiều chủ yếu để bảo vệ quyền riêng tư của bạn khỏi người khác. Trong trường hợp xấu nhất, chỉ có cơ quan chức năng có thể truy cập vào xpubs của bạn, nhưng phần còn lại của thế giới không biết về chúng. Do đó, từ góc nhìn của người khác, việc hợp nhất tiền của bạn có thể gây hại đáng kể cho quyền riêng tư của bạn do Giả định Sở Hữu Đầu Vào Chung (CIOH).

Cuối cùng, để chấm dứt việc theo dõi, bạn cũng nên cân nhắc thực hiện trộn coin từ ví mới này.
**Cảnh báo:** Chỉ lấy lại ví Samourai của bạn trên Sparrow Wallet không đủ. Nếu bạn muốn tránh sử dụng xpubs có thể đã bị rò rỉ, việc tạo một ví hoàn toàn mới với cụm từ khôi phục mới là cần thiết. Nếu bạn nhập hạt giống hiện có của mình vào Sparrow, bạn chỉ thay đổi phần mềm quản lý ví, nhưng ví vẫn giữ nguyên.

### Là người dùng của Sparrow hoặc Samourai với Dojo

Nếu ví của bạn chỉ được quản lý trên Sparrow Wallet, xpubs của bạn không thể bị rò rỉ, cho dù bạn đang sử dụng một node công khai hay node Bitcoin của riêng bạn. Tương tự, nếu bạn đang sử dụng ứng dụng Samourai và luôn kết nối ứng dụng này với Dojo của riêng mình kể từ khi tạo ví, xpubs của bạn cũng được bảo vệ.
Tuy nhiên, nếu bạn đã sử dụng cùng một ví trong một khoảng thời gian **không có Dojo của riêng mình** và sau đó là với Dojo của riêng bạn, có khả năng là các máy chủ Samourai có thể đã truy cập vào xpubs của bạn, và do đó cơ quan chức năng có thể biết chúng. Nếu bạn đang trong tình huống cụ thể này, tôi khuyên bạn nên tuân theo các khuyến nghị của phần trước và coi xpubs của mình như đã bị xâm phạm.
Đối với những người luôn sử dụng Sparrow hoặc Samourai với Dojo của riêng họ, rủi ro chính là tập hợp ẩn danh (anonsets) của các đồng tiền của bạn có thể bị giảm. Giả sử, trong trường hợp xấu nhất, tất cả người dùng không có Dojo có xpubs trong tay của cơ quan chức năng, thì con đường của các đồng tiền của họ qua các chu kỳ trộn coin có thể được cơ quan này truy dấu.

Để minh họa điều này, hãy lấy một ví dụ cụ thể. Hãy tưởng tượng bạn đã tham gia vào một chu kỳ ctrộn coin đầu tiên, tiếp theo là hai chu kỳ trộn coin phụ phía sau. Nếu xpubs của người dùng không có Dojo không bị rò rỉ, thì tập hợp ẩn danh tiềm năng của đồng tiền của bạn sẽ là 13.

![samourai](assets/37.webp)

Tuy nhiên, nếu chúng ta giả sử rằng xpubs đã bị rò rỉ và bạn đã gặp một người dùng không có dojo trong chu kỳ trộn coin ban đầu, và sau đó là 2 trong đợt trộn coin phụ đầu tiên, thì tập hợp ẩn danh tiềm năng của bạn chỉ còn là 10 thay vì 13 từ góc nhìn của cơ quan chức năng.

![samourai](assets/38.webp)
Tiềm năng suy giảm của tập hợp ẩn danh này khó có thể định lượng được, vì nó phụ thuộc vào nhiều yếu tố, và mỗi đồng tiền bị ảnh hưởng khác nhau. Ví dụ, một người dùng không có Dojo trong các chu kỳ trộn coin đầu ảnh hưởng đến tập hợp ẩn danh tiềm năng nhiều hơn so với một người không dùng Dojo riêng trong các chu kỳ trộn coin sau. Để bạn dễ hình dung, mặc dù vẫn là giả thuyết, số liệu thống kê mới nhất do Samourai cung cấp chỉ ra rằng có khoảng từ 85% đến 90% các đồng tiền tham gia vào trộn coin đến từ người dùng có Dojo, Sparrow, hoặc Bitcoin Keeper, tức là những người dùng mà, ngay cả trong trường hợp xấu nhất, cũng sẽ không bị rò rỉ xpubs của họ.
Mặc dù những con số này khó có thể xác minh, chúng dường như hợp lý với tôi vì hai lý do:
- Sparrow Wallet được sử dụng rộng rãi;
- Hầu hết phần mềm node-in-box cung cấp các triển khai Dojo, và những phần mềm chính thống như Umbrel hiện nay rất phổ biến.

Do đó, cần phải xem xét một số khía cạnh. Nếu sự riêng tư của các đồng tiền của bạn đối với cơ quan chức năng là vô cùng quan trọng với bạn, bạn nên thận trọng chuẩn bị cho kịch bản xấu nhất, và khó có thể đảm bảo 100% rằng các chu kỳ ctrộn coin Whirlpool của bạn không thể bị truy dấu do sự rò rỉ tiềm năng của xpubs từ người dùng không có Dojo. Mặc dù giả định này rất khó xảy ra, nhưng không phải là không thể.

Mặt khác, nếu sự riêng tư của các đồng tiền của bạn đối với cơ quan chức năng có khả năng sở hữu những xpubs này không quan trọng với bạn, thì tình hình có thể được xem xét khác đi.

Tôi nhấn mạnh "đối với cơ quan chức năng" bởi vì quan trọng là phải nhớ rằng chỉ có cơ quan chức năng đã thu giữ máy chủ mới có khả năng biết những xpubs này. Nếu mục tiêu của bạn khi sử dụng trộn coin là để ngăn chặn người bán bánh mì cho bạn có khả năng theo dõi tiền của mình, thì họ không có gì thay đổi so với trước khi máy chủ bị tịch thu, vì họ chẳng có thêm thông tin gì khác cả.
Cuối cùng, việc xem xét tập hợp ẩn danh ban đầu cho đồng tiền của bạn, trước khi máy chủ bị tịch thu, là điều cần thiết. Hãy lấy ví dụ về một đồng tiền đã đạt được tập hợp ẩn danh tiềm năng là 40,000; sự giảm sút tiềm năng trong tập hợp ẩn danh này có lẽ là không đáng kể. Thực sự, với một tập hợp ẩn danh về cơ bản đã rất cao, khả năng mà một vài người dùng không sử dụng Dojo có thể thay đổi đáng kể tình hình là không cao. Tuy nhiên, nếu đồng tiền của bạn chỉ có tập hợp ẩn danh là 40, thì rò rỉ tiềm năng này có thể ảnh hưởng nghiêm trọng đến tập hợp ẩn danh của bạn và có khả năng sẽ bị truy vết.

Với công cụ WST hiện không còn hoạt động sau khi OXT.me bị đóng cửa, bạn chỉ có thể ước lượng về các tập hợp ẩn danh này. Đối với tập hợp ẩn danh hồi tưởng (Retrospective Anonset), không có quá nhiều điều phải lo lắng vì mô hình Whirlpool đảm bảo rằng nó rất cao ngay từ lần trộn coin đầu tiên, nhờ vào di sản của các đối tác của bạn. Trường hợp duy nhất có thể gây ra vấn đề là nếu đồng tiền của bạn không được tái trộn trong vài năm và nó được trộn vào giai đoạn ra mắt của một pool. Về tập hợp ẩn danh tương lai (Prospective Anonset), bạn có thể xem xét thời gian đồng tiền của bạn đã ở trong chương trình trộn coin. Nếu đã vài tháng, thì có lẽ nó đã có một tập hợp ẩn danh tiềm năng cực kỳ cao. Ngược lại, nếu nó được thêm vào một pool chỉ vài giờ trước khi máy chủ bị tịch thu, thì tập hợp ẩn danh tiềm năng của nó có lẽ rất thấp.
[**-> Tìm hiểu thêm về anonsets và phương pháp tính toán của chúng.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

Một khía cạnh khác cần xem xét là ảnh hưởng của việc hợp nhất đối với tập hợp ẩn danh của các đồng tiền đã được trộn. Do tài khoản Whirlpool không còn truy cập được qua ứng dụng Samourai, có khả năng nhiều người dùng đã chuyển ví của họ sang phần mềm khác và cố gắng rút tiền từ Whirlpool. Đặc biệt, vào cuối tuần trước, khi phí giao dịch trên mạng Bitcoin tương đối cao, đã có một động lực kỹ thuật và kinh tế mạnh mẽ để hợp nhất các đồng tiền sau khi trộn. Điều này có nghĩa là có khả năng nhiều người dùng đã thực hiện các hợp nhất.

Vấn đề với những hợp nhất sau khi trộn này là chúng luôn làm giảm tập hợp ẩn danh, không chỉ cho người dùng thực hiện việc hợp nhất mà còn cho những người dùng mà họ gặp trong các chu kỳ trộn coin của mình. Mặc dù tôi không thể xác minh hoặc định lượng chính xác hiện tượng này, nhưng các động lực kinh tế liên quan đến phí giao dịch vào thời điểm đó có thể khiến chúng ta giả định rằng tập hợp ẩn danh thực tế có thể thấp hơn.

### Là một người dùng Sentinel

Hoạt động mạng của ứng dụng ví chỉ dùng để xem Sentinel tương tự như Samourai. Để truy cập thông tin ví của bạn, ứng dụng phải truyền các xpubs, khóa công khai, và địa chỉ bạn đã cung cấp cho một Dojo. Nếu bạn luôn sử dụng Dojo của riêng mình trên Sentinel, thì không có vấn đề gì và bạn có thể tiếp tục sử dụng ứng dụng mà không lo lắng. Tuy nhiên, nếu bạn phụ thuộc vào máy chủ của Samourai cho Sentinel của mình, có khả năng xpubs của bạn đã bị tiết lộ. Trong trường hợp này, việc tuân theo quy trình thay đổi ví được khuyến nghị cho Samourai Wallet khi kết nối với máy chủ của Samourai là điều khuyến khích.

Trong trường hợp hiếm hoi là bạn sử dụng Dojo của mình với Samourai nhưng không phải với Sentinel, thì sẽ khôn ngoan hơn khi xem xét rằng xpubs của bạn đã bị xâm phạm.

## Kết luận
Cảm ơn bạn đã đọc bài viết này đến cuối. Nếu bạn nghĩ thông tin còn thiếu hoặc nếu bạn có gợi ý, xin đừng ngần ngại liên hệ với tôi để chia sẻ suy nghĩ của bạn. Ngoài ra, nếu bạn cần thêm sự hỗ trợ trong việc khôi phục Samourai Wallet của mình sau hướng dẫn này, tôi mời bạn tham gia [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) để yêu cầu giúp đỡ. Tôi thường xuyên ghé thăm Discord này và sẽ rất vui lòng hỗ trợ bạn nếu tôi có giải pháp. Những Bitcoiner khác cũng sẽ có thể chia sẻ kinh nghiệm và cung cấp sự hỗ trợ của họ. **Dù trong trường hợp nào, việc giữ bí mật cụm từ khôi phục, tệp sao lưu và passphrase của bạn là cực kỳ quan trọng**. Đừng chia sẻ chúng với bất kỳ ai, vì điều này có thể cho phép họ ăn cắp bitcoin của bạn.
