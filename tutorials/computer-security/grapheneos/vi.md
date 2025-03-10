---
name: GrapheneOS

description: Hướng dẫn về Graphene OS
---

> "[GrapheneOS](https://grapheneos.org/) là một hệ điều hành di động tập trung vào quyền riêng tư và an ninh với khả năng tương thích ứng dụng Android, được phát triển như một dự án mã nguồn mở phi lợi nhuận."

GrapheneOS, ban đầu được thành lập vào năm 2014 với tên 'CopperheadOS', dựa trên mã nguồn Android truyền thống (AOSP), nhưng với nhiều thay đổi và cải tiến nhằm mục đích cải thiện quyền riêng tư và an ninh cho người dùng. GrapheneOS đặt người dùng vào vị trí kiểm soát điện thoại của họ, không phải các công ty công nghệ lớn.

### Mục lục:

- Giới thiệu
- Chuẩn bị
- Cài đặt
- Các Ứng dụng Thay thế
- Nhược điểm
- Thông Tin Hữu Ích

Hướng dẫn bởi https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md

## Tại sao sử dụng GrapheneOS?

Các điện thoại hiện đại là thiết bị theo dõi và thu thập dữ liệu có giá từ $500-$1000. Mọi khía cạnh của cuộc sống chúng ta đều diễn ra qua chúng, và không may, nhiều dữ liệu này được chia sẻ với bên thứ ba dưới một hình thức nào đó.
GrapheneOS được xây dựng cụ thể để giảm việc chia sẻ dữ liệu này và cải thiện an ninh thiết bị của bạn khỏi các vector tấn công tiềm ẩn. Không có thứ gọi là tài khoản GrapheneOS. Bạn không cần một tài khoản để tải xuống ứng dụng hoặc tương tác với hệ điều hành. Nói một cách đơn giản, bạn không phải là sản phẩm.

GrapheneOS cung cấp thêm an ninh cho trải nghiệm Android của bạn thông qua một số nguyên tắc cơ bản đơn giản.

1. **Giảm bề mặt tấn công** - Loại bỏ mã không cần thiết (hoặc phần mềm rác).
2. **Phòng ngừa lộ lọt lỗ hổng** - Cho phép người dùng đủ sự tinh tế để chọn những sự thỏa hiệp mà họ cảm thấy thoải mái.
3. **Kiểm soát sandbox** - GrapheneOS củng cố các sandbox Android hiện có, khóa chặt thêm khả năng giao tiếp của từng ứng dụng với phần còn lại của điện thoại.

Tìm hiểu thêm về các chi tiết kỹ thuật của bộ tính năng GrapheneOS [tại đây](https://grapheneos.org/features).

### Làm cho quá trình chuyển đổi dễ dàng hơn

Nếu bạn đã gắn bó với hệ sinh thái của Google hoặc Apple trong nhiều năm, ý nghĩ về việc mất tất cả sự tiện lợi đó qua đêm có thể là một điều đáng sợ. Nhưng với một số quyết định cài đặt ứng dụng được cân nhắc cẩn thận (được đề cập sau), phần lớn khó khăn dự kiến này có thể được giảm bớt hoặc loại bỏ.

Dù các lựa chọn thay thế đang trở nên tốt hơn, ý nghĩ về một sự thay đổi như vậy vẫn có thể làm bạn chùn bước. Nếu bạn cảm thấy mình trong tình huống này, lời khuyên tốt nhất của tôi là hãy sử dụng thiết bị GrapheneOS mới của bạn cùng với điện thoại hiện tại của bạn trong một thời gian. Từ đó, bạn có thể từ từ giảm bớt việc sử dụng 2-3 ứng dụng mỗi tuần cho đến khi bạn chỉ còn sử dụng thiết bị GrapheneOS của mình.

Nếu bạn áp dụng cách tiếp cận này, hãy nghiêm ngặt với bản thân và cắt bỏ sự phụ thuộc vào các lựa chọn được giám sát càng nhanh càng tốt. Chúng ta, con người, thường lười biếng và thường chọn con đường ít kháng cự nhất. Hãy nhớ lý do bạn thực hiện sự chuyển đổi này từ đầu.

**Thay vì trả bằng dữ liệu cá nhân của bạn, bạn đã chọn trả bằng thời gian của mình, và đôi khi là tiền bạc của bạn (tùy thuộc vào các ứng dụng thay thế bạn cài đặt).**

## Bắt đầu

Hiện tại, GrapheneOS chỉ được sản xuất cho dòng điện thoại [Google Pixel](https://grapheneos.org/faq#supported-devices) _(khá mỉa mai)_ . Điều này không phải không có lý do tốt. Dòng Pixel cung cấp an ninh dựa trên phần cứng tốt nhất để bổ sung cho công việc cải thiện hệ điều hành. Điều này bao gồm như cách ly thành phần cụ thể và khởi động đã được xác minh.

### Chọn một thiết bị

Khi chọn Pixel bạn muốn cài đặt GrapheneOS, hãy đảm bảo bạn kiểm tra thiết bị sẽ tiếp tục nhận được [cập nhật bảo mật](https://support.google.com/pixelphone/answer/4457705?hl=vi#zippy=%2Cpixel-xl-a-a-g-a-g) mặc định trong bao lâu.
Tại thời điểm viết bài, Pixel 6a là mẫu điện thoại có giá rẻ nhất với hỗ trợ dài hạn tốt, được đảm bảo cho đến tháng 7 năm 2027. Nếu bạn chọn mẫu này, việc mở khóa OEM sẽ không hoạt động với phiên bản hệ điều hành gốc từ nhà máy. Bạn cần cập nhật nó lên phiên bản phát hành tháng 6 năm 2022 hoặc mới hơn thông qua cập nhật qua không khí. Sau khi bạn đã cập nhật, bạn cũng cần phải khôi phục cài đặt gốc thiết bị để sửa lỗi mở khóa OEM. Tất cả các mẫu khác không khóa nhà mạng sẽ sẵn sàng cho GrapheneOS ngay khi mở hộp.

Khi chọn một thiết bị, bạn cũng sẽ muốn đảm bảo rằng bạn mua một phiên bản không khóa. Một số nhà mạng như Verizon giao thiết bị của họ đã khóa bootloader, điều này hoàn toàn ngăn chặn quy trình sau.

### Cài Đặt GrapheneOS

Trình cài đặt web của GrapheneOS [web installer](https://grapheneos.org/install/web) làm cho quá trình này trở nên dễ dàng, và có thể hoàn thành bởi bất kỳ ai trong vòng dưới 10 phút.
Hướng dẫn sau là phiên bản rút gọn được lấy từ liên kết trên.

Tất cả những gì bạn cần có là:

- Pixel
- Một cáp USB để kết nối từ điện thoại đến máy tính của bạn
- Một máy tính để chạy trình duyệt web (bất kỳ trình duyệt dựa trên Chromium: Chrome, Edge, Brave, v.v.)

1. Bước đầu tiên là vào **Cài đặt** > **Thông tin điện thoại** và nhấn liên tục vào số hiệu bản dựng cho đến khi bạn thấy **'Chế độ Nhà phát triển'** được kích hoạt.
2. Tiếp theo, hãy đến **Cài đặt** > **Hệ thống** > **Tùy chọn nhà phát triển** và kích hoạt **'Mở khóa OEM'**.
3. Bây giờ khởi động lại thiết bị và giữ nút giảm âm lượng trong khi điện thoại đang bật lại.
4. Kết nối điện thoại với laptop và nếu được yêu cầu xác thực, cho phép kết nối.
5. Trên trang trình cài đặt web, nhấp vào 'Mở khóa bootloader'.
6. Bạn sẽ thấy các tùy chọn điện thoại thay đổi. Sử dụng nút âm lượng để thay đổi lựa chọn thành `unlock` và sử dụng nút nguồn để chấp nhận.
7. Tiếp theo nhấp vào tải xuống bản phát hành trên trang trình cài đặt web.
8. Một khi đã tải xuống hoàn tất, chuyển sang bước tiếp theo và nhấp vào 'Flash release'. Quá trình này sẽ mất một hoặc hai phút và bạn không cần phải chạm vào điện thoại.
9. Cuối cùng, chuyển sang bước tiếp theo của trình cài đặt web và nhấp vào **Khóa Bootloader**. Bạn cần thay đổi lựa chọn và xác nhận bằng nút nguồn theo cách bạn đã làm trước đó trong quy trình.
10. Khi bạn thấy từ `Start`, xác nhận điều này bằng nút nguồn và thiết bị sẽ khởi động vào hệ điều hành mới không có Google của bạn.

![image](assets/2.webp)

Màn hình khởi đầu GrapheneOS

_Sau khi khởi động và thiết lập ban đầu, việc tắt mở khóa OEM từ Cài đặt > Hệ thống > Tùy chọn nhà phát triển là một thực hành tốt._

_Bạn cũng có thể muốn thực hiện bước thêm, tùy chọn nhưng được khuyến nghị là xác minh cài đặt qua ứng dụng Auditor. Bạn sẽ cần một điện thoại Android khác với ứng dụng đã cài đặt để hoàn thành bước này. Hướng dẫn cho việc này có thể được tìm thấy [tại đây](https://attestation.app/tutorial)._

![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Video mô tả các bước đơn giản được nêu trên

Nếu những bước đơn giản này dường như quá xa vời, bạn có thể xem xét mua một Pixel với phần mềm GrapheneOS [đã cài đặt sẵn](https://ronindojo.io/en/roninmobile). Chỉ cần lưu ý rằng bạn đang đặt một lượng nhỏ niềm tin vào nhà cung cấp.

### Ứng Dụng Đã Cài Đặt Sẵn

Bây giờ khi bạn đã thiết lập xong, bạn có thể nhận thấy GrapheneOS trông khá trống trải khi cài đặt lần đầu. Theo mặc định, bạn sẽ có những ứng dụng này đã được cài đặt:

![image](assets/3.webp)

Ứng dụng mặc định
Hai thuật ngữ bạn có thể chưa quen thuộc là 'Auditor' và 'Vanadium'.
- Ứng dụng [Auditor](https://play.google.com/store/apps/details?id=app.attestation.auditor) sử dụng các tính năng bảo mật dựa trên phần cứng để xác thực danh tính của thiết bị cùng với tính xác thực và toàn vẹn của hệ điều hành. Nó sẽ kiểm tra xem thiết bị có đang chạy hệ điều hành gốc với bootloader được khóa và không có sự can thiệp nào vào hệ điều hành hay không.
- [Vanadium](https://github.com/GrapheneOS/Vanadium) là một biến thể của trình duyệt web Chromium được tăng cường về quyền riêng tư và bảo mật.

## Tùy chỉnh

Cài đặt điện thoại là một việc cá nhân, nhưng dưới đây là một số mục đầu tiên tôi thay đổi khi cài đặt GrapheneOS để cảm thấy thoải mái hơn.

### Thiết lập hình nền và cập nhật chủ đề

Truy cập vào Cài đặt > Hình nền và Phong cách. Từ đây tôi:

- Cập nhật hình nền màn hình chính và màn hình khóa với hình ảnh tải xuống từ web.
- Chọn màu sắc nhấn được sử dụng xuyên suốt giao diện người dùng.
- Kích hoạt chế độ Tối.

### Hiển thị phần trăm pin

Truy cập vào **Cài đặt** > **Pin**, sau đó kích hoạt **Hiển thị phần trăm pin** trên thanh trạng thái.

### Nhập danh bạ

**Từ một điện thoại Android khác** - Truy cập vào ứng dụng Danh bạ và tìm tùy chọn Xuất ra VCF.

**Từ iOS** - Sử dụng một ứng dụng như Export Contact và sử dụng tùy chọn xuất 'vCard' để xuất một tệp VCF.
Sau khi bạn có tệp VCF, bạn có thể chuyển nó sang thiết bị GrapheneOS của mình bằng một tùy chọn lưu trữ ngoài như thẻ microSD hoặc ổ đĩa USB. Nếu bạn không có bất kỳ tùy chọn nào trong số này, bạn có thể chọn chia sẻ qua một trong số nhiều ứng dụng được liệt kê dưới đây.

![image](assets/4.webp)

Màn hình chính cá nhân hóa

## Ứng dụng Thay thế

Để điện thoại của bạn trở nên hữu ích, bạn sẽ muốn cài đặt một số ứng dụng! Các lựa chọn sau đây được bao gồm vì tôi đã sử dụng tất cả chúng cá nhân hoặc vì chúng nhận được những đánh giá cao từ cộng đồng quyền riêng tư rộng lớn hơn. Có nhiều lựa chọn thay thế tuyệt vời khác không được đề cập, và [Awesome Privacy](https://awesome-privacy.xyz) cung cấp một danh sách rất rộng lớn các ứng dụng bảo vệ quyền riêng tư cho mọi loại thiết bị.

Chỉ vì một ứng dụng là Phần Mềm Tự Do và Mã Nguồn Mở (FOSS) không có nghĩa là nó không có khả năng rò rỉ quyền riêng tư. Sử dụng [Exodus](https://reports.exodus-privacy.eu.org/en/) để xem các ứng dụng bạn ưa thích thực hiện như thế nào trước các kiểm toán quyền riêng tư của họ.

### F-Droid

[F-Droid](https://f-droid.org/) là một danh mục ứng dụng FOSS có thể cài đặt cho Android. Ứng dụng này giúp dễ dàng duyệt, cài đặt và cập nhật ứng dụng trên thiết bị của bạn. Đáng chú ý là cập nhật qua F-Droid đôi khi có thể chậm hơn so với các cửa hàng ứng dụng khác. Điều này chủ yếu phụ thuộc vào việc ứng dụng có được tìm thấy qua kho F-Droid chính thức hay một kho tùy chỉnh.

Để cài đặt F-Droid, chỉ cần truy cập trang web của họ qua trình duyệt trên điện thoại GrapheneOS của bạn và nhấn tải xuống. Điều này sẽ tải xuống một tệp `.apk`. Sau đó, bạn sẽ được hỏi liệu bạn có muốn cài đặt ứng dụng không.

Ngoài các ứng dụng được tìm thấy trong kho mặc định trên F-Droid, nhiều dự án Mã Nguồn Mở cũng sẽ tự host kho của riêng họ có thể được thêm vào trong cài đặt ứng dụng F-Droid. Nếu đây là trường hợp, dự án đó sẽ hướng dẫn bạn qua các bước rất đơn giản cần thiết để thực hiện điều này trên trang web của họ.

![image](assets/5.webp)

Màn hình chính F-Droid

### Aurora Store
[Aurora Store](https://auroraoss.com/) là phiên bản FOSS của Google Play Store. Aurora có giao diện và trải nghiệm rất giống với Play Store truyền thống và cho phép bạn tải xuống và cập nhật bất kỳ ứng dụng nào bạn thường tìm thấy qua lựa chọn của Google.
Tính năng nổi bật của Aurora là đăng nhập ẩn danh. Điều này có nghĩa là bạn có thể tải xuống bất kỳ ứng dụng yêu thích nào không có sẵn qua F-Droid hoặc APK trực tiếp, mà không cần phải đăng nhập vào tài khoản Google của mình.

Trước khi bạn vội vàng chọn đây là phương án cài đặt mặc định, hãy nhớ rằng nhiều ứng dụng mà chúng ta đang cố gắng tránh xa đã được cài đặt từ Play Store. Chỉ vì chúng có thể truy cập từ Aurora không thay đổi thực tế là một số có thể có tính năng theo dõi được nhúng vào. Không phải lúc nào cũng có thể, nhưng bất cứ khi nào bạn có thể, hãy tìm kiếm một lựa chọn thay thế từ F-Droid trước khi tải xuống qua Aurora.

Để cài đặt Aurora, chỉ cần tìm kiếm 'Aurora Store' trong F-Droid.

Aurora cũng có một số vấn đề tiềm ẩn, vì các "tài khoản ẩn danh" thực sự được tạo và kiểm soát bởi Aurora. Lý thuyết, họ có thể cung cấp các bản cập nhật độc hại hoặc đẩy ứng dụng vào điện thoại của bạn, mặc dù bạn vẫn phải chấp nhận lời nhắc cài đặt trên thiết bị. Aurora đôi khi cũng gặp phải một số vấn đề với ứng dụng không hiển thị do nhận diện sai khu vực và thiết bị. Thông thường, bạn có thể khắc phục vấn đề này với các bước dưới đây.

**Mẹo hàng đầu** - Đôi khi Aurora Store sẽ gặp phải giới hạn tốc độ, hạn chế khả năng tìm kiếm và cài đặt ứng dụng của bạn. Để khắc phục điều này, hãy vào **Cài đặt** > **Ứng dụng** > **Aurora** > **Mở theo mặc định**, sau đó thêm miền `play.google.com`. Bây giờ, bất cứ khi nào bạn truy cập vào trang web của một sản phẩm hoặc dịch vụ có liên kết 'Tải xuống qua Play Store', chỉ cần nhấn vào đó sẽ mở ứng dụng đó trong Aurora để bạn tải xuống.

![image](assets/6.webp)

Màn hình chính của Aurora Store

### Tải xuống APK

Ứng dụng trên Android cũng có thể được tải xuống và cài đặt qua tệp `.apk`. Đây là một lựa chọn tuyệt vời không yêu cầu bất kỳ cửa hàng ứng dụng bên thứ ba nào, chỉ cần tải tệp trực tiếp từ trang web của dự án hoặc kho lưu trữ GitHub.

Nhược điểm của phương pháp này là bạn không nhận được cập nhật tự động, vì vậy bạn sẽ cần theo dõi các kênh thông tin của dịch vụ để biết về các bản phát hành mới. Tuy nhiên, có một dự án tuyệt vời gọi là Obtanium nhằm khắc phục điều này. [Obtainium](https://github.com/ImranR98/Obtainium) cho phép bạn cài đặt và cập nhật ứng dụng mã nguồn mở trực tiếp từ trang phát hành của chúng và nhận thông báo khi có bản phát hành mới được cung cấp.

![image](assets/7.webp)

Xem trước Obtanium

### Web Apps

Đối với những lúc bạn muốn sử dụng một dịch vụ không thường xuyên và không muốn tải xuống một ứng dụng gốc, bạn có thể truy cập phiên bản web. Nhiều trang web ngày nay cũng hỗ trợ Progressive Web App (PWA). Đây là khi bạn có thể đánh dấu một trang web cụ thể (ví dụ Twitter.com) vào màn hình chính của điện thoại. Sau đó, khi bạn nhấn vào biểu tượng, nó mở ra như một ứng dụng toàn màn hình mà không có những phân tâm thường thấy với trải nghiệm trình duyệt thông thường. Bạn có thể thấy một ví dụ về cách này bên dưới.

Để thực hiện điều này trong Vanadium, trình duyệt gốc của GrapheneOS, chỉ cần điều hướng đến trang web bạn chọn, nhấn vào ba chấm dọc ở góc trên bên phải của màn hình và sau đó nhấn **'Thêm vào Màn Hình Chính'**.

Nhược điểm duy nhất của phương pháp này là vì đây chỉ là một trang web được đánh dấu, bạn sẽ không nhận được bất kỳ hình thức thông báo nào. Tuy nhiên, một số người có thể coi đó là một điểm tích cực!

![image](assets/8.webp)

Twitter PWA

### Trình Duyệt Web
Bạn hoàn toàn có thể yên tâm khi sử dụng gói ứng dụng sẵn có, Vanadium. Ứng dụng này hoạt động giống hệt như bất kỳ trình duyệt di động nào khác mà tôi đã thử và tôi chưa bao giờ gặp bất kỳ vấn đề tương thích nào.

Khi bạn cần truy cập vào các trang web `.onion` đặc thù của Tor, bạn có thể tải xuống Tor Browser APK trực tiếp từ [website](https://www.torproject.org/download/#android) của họ hoặc qua F-Droid.

### VPNs

Để bảo vệ hoạt động trực tuyến của bạn khỏi sự theo dõi của nhà cung cấp dịch vụ internet (ISP), ứng dụng Mạng Riêng Ảo (VPN) là một lựa chọn tốt. VPN chuyển lưu lượng internet của bạn qua một đường hầm mã hóa đến một địa chỉ IP chung được kiểm soát bởi nhà cung cấp dịch vụ VPN để đảm bảo hoạt động của thiết bị không thể liên kết với bạn.

Dưới đây là 3 lựa chọn được đánh giá cao cho phép bạn thanh toán dịch vụ bằng Bitcoin và không cần cung cấp bất kỳ thông tin cá nhân nào. Tất cả 3 lựa chọn đều có sẵn qua F-Droid.

- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)

### Tin nhắn

Trong những năm gần đây, giải pháp tin nhắn mã hóa đã trở nên phong phú. Tuy nhiên, vấn đề vẫn tồn tại, bạn có thể có lựa chọn tốt nhất và riêng tư nhất được cài đặt trên điện thoại của mình, nhưng nếu bạn không có liên lạc nào sử dụng nó, thì có ý nghĩa gì?

Hầu hết mọi người không quan tâm đến không gian riêng tư có lẽ sẽ sử dụng WhatsApp hoặc iMessage. Cái đầu tiên có thể được tải xuống qua Aurora Store nhưng cái sau thì không thể sử dụng trên GrapheneOS (rõ ràng!).

- [Signal](https://signal.org/) là một trong những ứng dụng nhắn tin mã hóa đầu cuối (E2EE) phổ biến hơn với bản lưu trữ vững chắc và bộ tính năng phong phú. Signal yêu cầu một số điện thoại để đăng ký, vì vậy nếu bạn dự định trò chuyện với những người mà bạn thích họ không biết số điện thoại của mình, có lẽ nên xem xét một số lựa chọn khác. Signal phải được tải xuống qua Aurora Store.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) là một ứng dụng nhắn tin E2EE khá mới. Nó không yêu cầu ID người dùng, số điện thoại hay thông tin cá nhân. Mọi người có thể tìm thấy bạn bằng cách quét mã QR cá nhân hoặc truy cập vào liên kết độc đáo của bạn. Simplex cũng cho phép người dùng nâng cao tự chạy máy chủ của mình để giảm sự phụ thuộc vào bất kỳ thực thể tập trung nào. Simplex không có ứng dụng cho máy tính, vì vậy có thể không phù hợp nếu việc sử dụng trên nhiều thiết bị là ưu tiên của bạn. Simplex cho Android có sẵn qua F-Droid.
- [Threema](https://threema.ch/en/faq/libre_installation) cung cấp trải nghiệm tương tự như Simplex, nhưng đã tồn tại lâu hơn và do đó, cảm giác hoàn thiện hơn một chút. Threema không miễn phí, bản quyền trọn đời có giá $4.99 và có thể mua bằng Bitcoin. Threema cung cấp ứng dụng web và ứng dụng máy tính để bàn gốc. Ứng dụng Android có sẵn qua F-Droid.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) là một bản fork FOSS không chính thức của ứng dụng Telegram chính thức cho Android. Telegram có chức năng 'cuộc trò chuyện bí mật' E2EE, nhưng lựa chọn mặc định không riêng tư. Telegram FOSS có thể được tải xuống từ F-Droid.

![image](assets/9.webp)
Trái: Threema
Phải: Simplex

### Truyền thông
- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) là một ứng dụng khách Spotify đa nền tảng không yêu cầu tài khoản Premium. Spotube có sẵn qua F-Droid.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) là một ứng dụng tuyệt vời cho việc phát bất kỳ bài hát nào từ YouTube Music miễn phí. ViMusic có sẵn từ F-Droid.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) mang lại trải nghiệm YouTube mà không có quảng cáo khó chịu và quyền truy cập đáng ngờ. Với NewPipe, bạn có thể đăng ký kênh, nghe nhạc nền và thậm chí tải xuống để xem ngoại tuyến. NewPipe có thể truy cập qua F-Droid.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) là một trình phát podcast cho phép bạn đăng ký và quản lý tất cả các chương trình yêu thích của mình. AntennaPod có sẵn qua F-Droid.

![hình ảnh](assets/11.webp)

Trái: Spotube
Phải: ViMusic

### Bản đồ

Nếu bạn muốn có sự hỗ trợ giọng nói khi lái xe và sử dụng ứng dụng bản đồ trên GrapheneOS, bạn cần cài đặt [RHVoice](https://rhvoice.org/installation/) và [cấu hình](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available) nó.

- [Magic Earth](https://www.magicearth.com/) là một lựa chọn thay thế cho bản đồ hỗ trợ điều hướng từng bước, bản đồ 3D và ngoại tuyến. Magic Earth có thể tải xuống từ Aurora Store.
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) là một lựa chọn thay thế bản đồ dành cho du khách, khách du lịch, người đi bộ đường dài và người đi xe đạp dựa trên dữ liệu OpenStreetMap do cộng đồng đóng góp. Đây là một phiên bản fork tập trung vào quyền riêng tư, mã nguồn mở của ứng dụng Maps.me (trước đây được biết đến với tên MapsWithMe). Nó hỗ trợ 100% tính năng mà không cần kết nối Internet và có thể tải xuống từ F-Droid.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) là một lựa chọn thay thế bản đồ tuyệt vời khác hỗ trợ tất cả các tính năng đã nêu trên.

![hình ảnh](assets/13.webp)

Trái: Magic Earth
Phải: Organic Maps

### Email

- [Proton Mail](https://proton.me/mail) cung cấp một dịch vụ email riêng tư miễn phí hỗ trợ mã hóa E2EE đã được kiểm định. Proton cũng cung cấp một phiên bản trả phí hỗ trợ tên miền tùy chỉnh và [aliasing](https://proton.me/support/creating-aliases). Proton Mail có thể tải xuống dưới dạng APK trực tiếp hoặc qua Aurora.
- [Tutanota](https://tutanota.com/) cung cấp các tính năng tương tự như Proton Mail, bao gồm các dịch vụ trả phí tùy chọn và có thể tải xuống dưới dạng APK trực tiếp hoặc qua F-Droid.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) là một ứng dụng email mã nguồn mở hoạt động với hầu hết mọi nhà cung cấp email. Nó hỗ trợ nhiều tài khoản, hộp thư đồng nhất và tiêu chuẩn mã hóa OpenPGP.

![hình ảnh](assets/15.webp)

Trái: Proton Mail
Phải: Tutanota

### Năng suất

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) là một chương trình đồng bộ hóa tệp. Nó đồng bộ hóa tệp giữa hai hoặc nhiều thiết bị theo thời gian thực, được bảo vệ an toàn khỏi ánh mắt tò mò. Dữ liệu của bạn là của riêng bạn và bạn xứng đáng quyết định nơi dữ liệu được lưu trữ, liệu nó có được chia sẻ với bên thứ ba nào và cách nó được truyền đi trên internet. Syncthing có sẵn qua F-Droid.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) giúp kết nối tất cả thiết bị của bạn để dễ dàng giao tiếp với nhau khi được kết nối với mạng nhà. Dễ dàng gửi tệp, ảnh, dữ liệu clipboard giữa tất cả các thiết bị của bạn (kể cả trên iOS!). KDE Connect có thể được tải về từ F-Droid.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) là ứng dụng ghi chú E2EE cho phép đồng bộ suy nghĩ và danh sách công việc của bạn trên tất cả các thiết bị. Gói miễn phí của họ nên đáp ứng hầu hết các trường hợp sử dụng cá nhân. Notesnook có sẵn trên F-Droid.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) rất giống với Notesnook, nhưng yêu cầu một kế hoạch trả phí để có đầy đủ tính năng. Standard Notes có sẵn thông qua F-Droid.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) là ứng dụng bàn phím cho phép bạn tùy chỉnh hầu như mọi thứ bạn có thể nghĩ đến khi nói đến trải nghiệm gõ phím trên điện thoại của mình. Có thể tải về qua F-Droid.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) là ứng dụng bàn phím mặc định của Google. Theo kinh nghiệm của tôi, nó cung cấp trải nghiệm gõ và vuốt tốt nhất. Nếu bạn tải ứng dụng này, hãy đảm bảo vô hiệu hóa hoàn toàn tất cả các quyền liên quan đến mạng. Có thể tải về qua Aurora.

![image](assets/17.webp)

Trái: Notesnook
Phải: KDE Connect

### Lối Sống

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) là ứng dụng thời tiết mã nguồn mở được thiết kế đẹp mắt, có sẵn qua F-Droid. Nó cũng hỗ trợ nhiều kích cỡ widget khác nhau để bạn có thể xem thời tiết tại địa điểm bạn chọn ngay từ màn hình chính của mình.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) là ứng dụng dịch thuật mã nguồn mở và bảo vệ quyền riêng tư hỗ trợ hơn 200 ngôn ngữ. Translate You có sẵn qua F-Droid.
- [Proton Calendar](https://proton.me/calendar/download) là ứng dụng lịch sử dụng đơn giản với E2EE tương tác mượt mà với các tài khoản email Proton của bạn. Proton Calendar có thể được tải về dưới dạng APK hoặc qua cửa hàng Aurora.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) là ứng dụng để hiển thị và lưu trữ thẻ lên máy bay, phiếu giảm giá, vé xem phim và thẻ thành viên, v.v. Chỉ cần tải về tệp `pkpass` hoặc `espass` liên quan và mở bằng ứng dụng. PassAndroid có sẵn qua F-Droid.

![image](assets/19.webp)
Trái: Geometric Weather
Phải: Proton Calendar

### Bảo Mật/Quyền Riêng Tư

- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) cung cấp một giải pháp quản lý mật khẩu miễn phí và E2EE đa nền tảng cho tất cả các thiết bị của bạn. Dịch vụ trả phí của họ cho phép bạn tích hợp mã 2FA vào ứng dụng. Phía máy chủ của Bitwarden có thể tự lưu trữ và ứng dụng Android có sẵn qua F-Droid.
- [Proton Pass](https://proton.me/pass/download) cung cấp một dịch vụ miễn phí tương tự như Bitwarden, nhưng khách hàng của [Proton Unlimited](https://proton.me/pricing) có thể truy cập các tính năng nâng cao bổ sung. Proton Pass có sẵn qua APK hoặc Aurora.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) là một ứng dụng xác thực hai yếu tố cho các hệ thống sử dụng các giao thức mật khẩu một lần. Token có thể được thêm vào dễ dàng bằng cách quét mã QR. FreeOTP có sẵn qua F-Droid.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) là một ứng dụng miễn phí, an toàn và mã nguồn mở cho Android để quản lý các token xác thực 2 bước cho các dịch vụ trực tuyến của bạn. Aegis có sẵn qua F-Droid.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) là một dịch vụ trả phí, đa nền tảng giúp mã hóa dữ liệu của bạn một cách cục bộ để bạn có thể an tâm tải lên dịch vụ đám mây yêu thích của mình. Cryptomator có thể được tải về qua F-Droid.

![image](assets/21.webp)
Trái: Proton Pass
Phải: Bitwarden

### Giải Pháp Đám Mây

- [Proton Drive](https://proton.me/drive/download) là một giải pháp đám mây E2EE trả phí để sao lưu và lưu trữ tất cả các tệp của bạn. Tại thời điểm viết bài, họ vừa công bố một ứng dụng máy tính để bàn cho Windows, nhưng người dùng Mac và Linux phải tiếp tục sử dụng phiên bản web để đồng bộ từ máy tính của họ (tạm thời). Ứng dụng Android có sẵn dưới dạng APK hoặc qua Aurora.
- [Skiff](https://skiff.com/download) cũng cung cấp lưu trữ đám mây E2EE trả phí và các công cụ hợp tác tệp. Họ cung cấp ứng dụng máy tính để bàn cho Mac và Windows (cũng như một ứng dụng web) và ứng dụng Android của họ phải được tải xuống từ Aurora.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) cung cấp một giải pháp đám mây đầy đủ tính năng cho hợp tác, đồng bộ thiết bị chéo và lưu trữ tệp. Người dùng nâng cao có thể chọn tự lưu trữ phần mềm miễn phí và mã nguồn mở trên bất kỳ phần cứng nào họ thích. Ứng dụng Android có thể được tải về qua F-Droid.
- [Cryptpad](https://cryptpad.fr/) cung cấp một lựa chọn thay thế miễn phí, dựa trên web, E2EE cho Google Docs.

![image](assets/23.webp)

Proton Drive

## Nhược Điểm

Các lựa chọn thay thế mã nguồn mở và bảo vệ quyền riêng tư cho các ứng dụng của công ty công nghệ lớn mà bạn đã quen sử dụng là rất nhiều, và một số trong chúng thậm chí còn tốt hơn các lựa chọn không mã nguồn mở, đầy rẫy phần mềm gián điệp.

Tuy nhiên, khi chuyển sang GrapheneOS, có một số tiện nghi mà bạn phải từ bỏ do không có lựa chọn thay thế. Bao gồm:

- **Apple CarPlay/Android Auto** - Bạn sẽ cần phải dùng đến Bluetooth, USB hoặc Aux truyền thống.
- **Apple/Google Pay** - Hầu như mọi người đều mang ví của họ theo bất cứ đâu!
- **Ứng dụng ngân hàng** - Không phải là chúng không hoạt động hoàn toàn. Một số hoạt động hoàn hảo. Một số khác chỉ hoạt động khi Google Play Services được kích hoạt (đọc thêm về điều này bên dưới) và một số khác thì không hoạt động chút nào. Đọc báo cáo về ngân hàng của bạn [tại đây](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) để xem tình hình hiện tại. Đừng lo nếu ngân hàng của bạn nằm trong danh sách không hoạt động, nhớ rằng bạn có thể lưu URL dưới dạng một ứng dụng web trên màn hình chính của mình.
- **Thông báo đẩy** - Hầu hết các ứng dụng gửi cho bạn cập nhật khi không sử dụng một ứng dụng cụ thể sẽ làm vậy thông qua Google Play Services. Dịch vụ này không được cài đặt mặc định với GrapheneOS, vì vậy nếu bạn thấy mình không được thông báo ngay lập tức khi bạn bè của bạn gửi email, đó có lẽ là lý do. Tin tốt là một số ứng dụng đã nêu trên đã triển khai kết nối nền của riêng họ để kiểm tra cập nhật định kỳ và sau đó gửi cho bạn thông báo khi cần

### Google Play Đã Được Cô Lập
GrapheneOS có một lớp tương thích cung cấp tùy chọn để cài đặt và sử dụng các phiên bản chính thức của Google Play trong sandbox ứng dụng tiêu chuẩn. Google Play không nhận bất kỳ quyền truy cập đặc biệt hay ưu đãi nào trên GrapheneOS so với việc bỏ qua sandbox ứng dụng và nhận được một lượng lớn quyền truy cập đặc quyền cao.

Nếu bạn thấy mình không thể sống thiếu những thông báo đẩy cho ứng dụng yêu thích của mình hoặc một ứng dụng 'phải có' nào đó trở nên vô dụng mà không có Dịch vụ Play, GrapheneOS cho phép bạn [cài đặt](https://grapheneos.org/usage#sandboxed-google-play-installation) các dịch vụ này trong một môi trường hoàn toàn cô lập. Một khi đã cài đặt, các dịch vụ này không yêu cầu tài khoản Google để hoạt động, và quyền của từng dịch vụ có thể được kiểm soát chặt chẽ.

Trước khi bạn vội vã cài đặt chúng ngay ngày đầu tiên, tôi khuyên bạn nên xem bạn có thể đi xa đến đâu mà không cần chúng. Bạn có thể sẽ ngạc nhiên khi thấy rằng có bao nhiêu ứng dụng hoạt động hoàn hảo mà không cần chúng.

Nếu bạn muốn cài đặt chúng, chỉ cần chạm vào ứng dụng 'Apps' được cài đặt sẵn sau đó là 'Google Play Services'. Cân nhắc cài đặt chúng cùng với những ứng dụng ít riêng tư mà bạn không thể sống thiếu, trong một hồ sơ người dùng hoàn toàn riêng biệt để cung cấp thêm một lớp phân tách khỏi phần còn lại của điện thoại của bạn.

![image](assets/24.webp)

Màn hình cài đặt Dịch vụ Play

### Hồ Sơ

GrapheneOS cho phép bạn có một trải nghiệm điện thoại riêng biệt, ngay trong điện thoại của bạn. Các hồ sơ bổ sung có thể cài đặt các ứng dụng và dịch vụ riêng của họ và không thể truy cập bất kỳ tệp tin hoặc dữ liệu nào từ tài khoản chủ sở hữu.
Nếu bạn chỉ có một hoặc hai ứng dụng 'phải có' đó yêu cầu Dịch vụ Play, nhưng chỉ sử dụng rất ít lần, việc cài đặt những ứng dụng này cùng với Dịch vụ Play trong một hồ sơ riêng biệt có thể là một ý tưởng tuyệt vời để tăng cường bảo vệ quyền riêng tư, ngay cả khi có những hậu quả nhỏ về quyền riêng tư khi chúng chạy trong hồ sơ chủ sở hữu.

Bạn có thể đọc thêm về trường hợp sử dụng này [tại đây](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).

Nếu bạn quyết định thêm một hồ sơ riêng để phù hợp với trường hợp sử dụng của mình, ứng dụng [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) có thể hữu ích cho bạn. Insular cho phép bạn dễ dàng sao chép bất kỳ ứng dụng hiện có nào của mình sang hồ sơ mới mà không cần phải qua bất kỳ con đường cài đặt truyền thống nào được đề cập trước đó trong hướng dẫn này. Insular cũng cho phép bạn nhanh chóng 'đóng băng' bất kỳ ứng dụng nào để hoàn toàn vô hiệu hóa tất cả các dịch vụ nền của ứng dụng đó từ việc chạy.

![image](assets/24.webp)

Màn hình quản lý hồ sơ người dùng

### e-SIM

Nếu bạn muốn nâng cao quyền riêng tư điện thoại của mình lên một tầm cao mới và có một dịch vụ di động không gắn liền với danh tính thực của bạn, eSIM có thể là dành cho bạn. eSIM là một SIM ảo mà bạn có thể mua trực tuyến và thêm vào điện thoại của mình qua mã QR. Các công ty cung cấp dịch vụ như vậy có thể được thanh toán ẩn danh bằng Bitcoin bao gồm [Silent.Link](https://silent.link/) và [Bitrefill](https://www.bitrefill.com/gb/en/esims/).

eSIM không nên được coi là giải pháp hoàn hảo cho quyền riêng tư điện thoại. Chúng có thể là một công cụ hữu ích khi nằm trong tay đúng người, nhưng xin hãy nghiên cứu về các [đánh đổi](https://grapheneos.org/faq#cellular-tracking) khi sử dụng bất kỳ loại dịch vụ di động nào nếu bạn có ý định hoàn toàn 'tách biệt khỏi mạng'.

Dịch vụ Play cô lập phải được cài đặt cho việc cung cấp eSIM trong GrapheneOS.

## Sao Lưu
Sau khi thiết lập xong chiếc điện thoại Pixel không còn dùng dịch vụ của Google, việc tạo một bản sao lưu cho bản thân là một ý kiến tốt. Bản sao lưu này sẽ giúp bạn có thể khôi phục điện thoại về trạng thái giống hệt như cũ trong trường hợp bạn làm mất điện thoại hoặc nó bị mất cắp.

Bạn có thể chọn lưu file sao lưu vào bất kỳ thiết bị lưu trữ ngoại vi nào, hoặc vào một giải pháp đám mây tự lưu trữ như Nextcloud, mặc dù một số người dùng báo cáo về các mức độ thành công khác nhau với lựa chọn sau.

Để tạo bản sao lưu đầu tiên của bạn:

1. Vào **Cài đặt** > **Hệ thống** > **Sao lưu**, sau đó ghi lại mã khôi phục 12 từ của bạn. Mã này là cần thiết để giải mã file sao lưu vào một ngày sau đó. Mất mã, mất quyền truy cập vào bản sao lưu điện thoại của bạn.
2. Tiếp theo, chọn vị trí lưu trữ của bạn. Tôi sẽ khuyên dùng ổ đĩa USB ngoại vi hoặc thẻ microSD cấp công nghiệp.
3. Chọn dữ liệu cần sao lưu. Nếu bạn có đủ không gian trên phương tiện lưu trữ đã chỉ định, tôi sẽ khuyên bạn nên chọn tất cả.
4. Chạm vào ba chấm ở góc trên bên phải và chọn **Sao lưu ngay**.

![hình ảnh](assets/26.webp)

Màn hình sao lưu

Hãy nhớ rằng, nếu bạn đang thực hiện sao lưu ngoại tuyến vào thiết bị lưu trữ ngoại vi, việc hoàn thành bước này một cách định kỳ là hợp lý để đảm bảo bất kỳ cập nhật quan trọng nào gần đây đối với điện thoại của bạn không bị mất nếu tình huống xấu nhất xảy ra.

![video](https://www.youtube.com/embed/eyWmcItzisk)

Video chi tiết quy trình sao lưu

## Kết luận

Trong những năm gần đây, phần mềm GrapheneOS đã phát triển đáng kể. Nó ổn định và tương thích hơn bao giờ hết. Kết hợp điều này với hệ sinh thái ứng dụng mã nguồn mở và bảo vệ quyền riêng tư đang phát triển mạnh mẽ, làm cho GrapheneOS trở thành một lựa chọn thực sự khả thi so với Android gốc hoặc iOS, ngay cả đối với những người 'bình thường' giống như bạn!

Việc vi phạm dữ liệu và giám sát rộng rãi đến mức chúng hầu như không còn là tin tức nữa trong thế giới ngày nay. Việc bảo vệ bản thân là do bạn. Sẽ có những điều chỉnh và hy sinh phải thực hiện trên đường đi, nhưng việc giảm thiểu sự phơi bày với những vi phạm như vậy không hề khó khăn như bạn nghĩ.

Tôi hy vọng hướng dẫn này phần nào giúp bạn trên hành trình của mình. Nếu bạn thấy hướng dẫn này hữu ích và muốn hỗ trợ công việc của tôi, xin hãy xem xét gửi một [quyên góp](/tips).

Nếu bạn là người dùng GrapheneOS hiện tại, hoặc trở thành một người dùng sau khi đọc hướng dẫn này, xin hãy xem xét [quyên góp](https://grapheneos.org/donate) để hỗ trợ công việc quan trọng của họ.

### Tìm hiểu thêm

GrapheneOS là một chủ đề mà bất kỳ ai cũng có thể dành hàng tuần để khám phá. Có rất nhiều điều bạn có thể học và tinh chỉnh để điều chỉnh trải nghiệm theo yêu cầu và mô hình đe dọa của bạn. Dưới đây là một số liên kết nơi bạn có thể tiếp tục hành trình của mình:

- [Hướng dẫn Sử dụng Chính thức của GrapheneOS](https://grapheneos.org/usage) - Trang Web Chính thức
- [Diễn đàn GrapheneOS](https://discuss.grapheneos.org/) - Trang Web Chính thức
- [Lớp Thạc sĩ Cài đặt GrapheneOS](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video của 'The Privacy Wayfinder'
- [Podcast Chung về GrapheneOS](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast của 'Watchman Privacy'

toàn bộ công nhận cho: https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md