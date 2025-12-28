---
name: Trò chuyện bậy bạ
description: Nhắn tin phi tập trung, không cần Internet, cho giao tiếp tự do.
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Video hướng dẫn này từ BTC Sessions sẽ hướng dẫn bạn từng bước thiết lập và sử dụng Bitchat!*


Bitchat ra đời từ một nỗ lực tạo mẫu nhanh, trong đó [@jack](https://primal.net/jack) đã phát triển ý tưởng ban đầu trong một buổi lập trình cuối tuần. [@calle](https://primal.net/calle) đã tham gia dự án ngay sau đó để cùng phát triển phiên bản Android. Hiện tại, Jack đang dẫn dắt việc phát triển phiên bản iOS, trong khi calle giám sát phiên bản Android với sự hỗ trợ của nhiều người đóng góp khác.


## Giới thiệu: Trò chuyện tự do, không cần lưới


Hãy tưởng tượng bạn có thể gửi tin nhắn khi internet bị gián đoạn, trong thảm họa thiên nhiên, hoặc ở những nơi mà việc liên lạc bị hạn chế. Bitchat biến điều đó thành hiện thực. Đây là một ứng dụng nhắn tin phi tập trung, ngang hàng (peer-to-peer) bỏ qua các máy chủ trung tâm, cho phép các thiết bị giao tiếp trực tiếp với nhau, hoàn toàn ngoại tuyến bằng Bluetooth và mạng lưới dạng lưới (mesh networking). Được thiết kế với mục tiêu bảo mật và khả năng phục hồi, Bitchat lý tưởng để sử dụng ở những khu vực có kết nối truyền thống không đáng tin cậy hoặc không khả dụng—chẳng hạn như trong các tình huống thảm họa, ở những địa điểm hẻo lánh, hoặc đối với những người muốn tránh bị giám sát. Về cốt lõi, Bitchat sử dụng mật mã để đảm bảo mọi tin nhắn đều được mã hóa đầu cuối, xác minh và không thể bị giả mạo.


Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách Bitchat hoạt động và cách bạn có thể sử dụng nó để liên lạc riêng tư thực sự, ngay cả khi ngoại tuyến.


## 🚀 Các tính năng chính


Bitchat cho phép nhắn tin ngoại tuyến thông qua các [tính năng](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Tương thích đa nền tảng**: Hoàn toàn tương thích giao thức giữa iOS và Android.
- Mạng lưới dạng lưới phi tập trung**: Tự động phát hiện các thiết bị ngang hàng và chuyển tiếp tin nhắn đa bước qua Bluetooth năng lượng thấp (BLE)
- Mã hóa đầu cuối**: Trao đổi khóa X25519 + AES-256-GCM cho tin nhắn riêng tư
- Trò chuyện theo kênh**: Nhắn tin nhóm theo chủ đề với tùy chọn bảo vệ bằng mật khẩu.
- Lưu trữ & Chuyển tiếp**: Tin nhắn được lưu vào bộ nhớ đệm cho những người dùng ngoại tuyến và được gửi khi họ kết nối lại.
- Bảo mật là trên hết**: Không có tài khoản, không có số điện thoại, không có mã định danh cố định.
- Các lệnh kiểu IRC: Giao diện quen thuộc kiểu `/join, /msg, /who`.
- Lưu giữ tin nhắn**: Chức năng lưu tin nhắn trên toàn kênh tùy chọn, do chủ sở hữu kênh kiểm soát.
- Xóa khẩn cấp**: Nhấn ba lần vào biểu tượng để xóa ngay lập tức tất cả dữ liệu
- Giao diện người dùng Android hiện đại**: Jetpack Compose với Material Design 3
- Chủ đề Tối/Sáng**: Giao diện lấy cảm hứng từ giao diện dòng lệnh, phù hợp với phiên bản iOS.
- Tối ưu hóa pin**: Quét thích ứng và quản lý năng lượng


## 1️⃣ Cách thức hoạt động của Bitchat - đơn giản


Bitchat cho phép bạn nhắn tin trực tiếp cho các điện thoại ở gần thông qua Bluetooth (BLE), không cần internet hoặc tín hiệu di động. Khi bạn bắt đầu cuộc trò chuyện, các điện thoại sẽ thực hiện quá trình bắt tay bảo mật để tạo ra một khóa mã hóa tạm thời duy nhất cho cuộc trò chuyện của bạn. Mỗi tin nhắn đều được bảo vệ bằng mã hóa đầu cuối, và một khóa mới được sử dụng cho mỗi tin nhắn để đảm bảo các tin nhắn trước đó vẫn an toàn ngay cả khi điện thoại của bạn bị xâm phạm sau này. Cuối cùng, ứng dụng chia tin nhắn thành nhiều phần nhỏ và trộn chúng với dữ liệu giả ngẫu nhiên để che giấu hoạt động nhắn tin của bạn. Đối với các cuộc trò chuyện trực tiếp giữa các thiết bị, nó chỉ hoạt động trong phạm vi tối đa khoảng 100m. Nó giống như việc truyền những mẩu giấy mã hóa trong một căn phòng đông người — các thiết bị thì thầm trực tiếp với nhau, loại bỏ khóa sau mỗi tin nhắn.


Bitchat cũng cho phép bạn tham gia các phòng chat dựa trên vị trí bằng cách sử dụng giao thức Nostr và `#geohashes`. Geohash là một mã ngắn, giống như `#u33d`, đại diện cho một khu vực địa lý cụ thể, từ một khu phố nhỏ đến toàn bộ thành phố hoặc khu vực. Bạn có thể `dịch chuyển tức thời` đến bất kỳ phòng chat geohash nào trên toàn thế giới chỉ bằng cách nhập thẻ của phòng đó. Tin nhắn của bạn được gửi qua một mạng lưới chuyển tiếp phi tập trung, giúp bảo vệ vị trí chính xác của bạn. Hơn nữa, mỗi khi bạn tham gia một phòng geohash, bạn sẽ được cấp một danh tính tạm thời mới, tăng thêm một lớp bảo mật cho các cuộc trò chuyện dựa trên vị trí của bạn.


Để biết thêm chi tiết kỹ thuật chính xác hơn, vui lòng tham khảo [Sách trắng chính thức](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Cài đặt & Thiết lập


### Tìm Bitchat ở đâu?


Bạn có thể cài đặt Bitchat thông qua:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (dành cho thiết bị iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (dành cho thiết bị Android)


Người dùng Android cũng có những lựa chọn thay thế khác:



- Tải xuống tệp APK trực tiếp từ trang [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) hoặc
- Cài đặt thông qua [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr) tương thích với Nostr


![image](assets/en/01.webp)


**Lưu ý:** _Hướng dẫn này tập trung chủ yếu vào cách triển khai trên Android. Phiên bản iOS có thể khác._


### Quy trình thiết lập


Sau khi cài đặt, hãy mở Bitchat để thấy màn hình cấp quyền ban đầu này. Đây là những gì bạn cần làm:


1. **Cấp các quyền cần thiết sau:**


   - Truy cập Bluetooth** (để tìm người dùng Bitchat ở gần)
   - Vị trí chính xác** (Android yêu cầu điều này để sử dụng chức năng Bluetooth)
   - Thông báo** (để nhận thông báo qua tin nhắn riêng)

2. **Tắt chế độ tối ưu hóa pin**:


   - Điều này cho phép Bitchat chạy ngầm trong nền.
   - Duy trì liên tục các kết nối mạng lưới dạng lưới


Nhấn vào `Cấp quyền`, làm theo hướng dẫn và `Tắt tối ưu hóa pin` để chuyển sang màn hình tiếp theo.


![image](assets/en/02.webp)


Chào mừng bạn đến với màn hình chính của Bitchat. Hãy cùng làm quen nhé:


### Cài đặt


Trước hết, bạn cần mở menu cài đặt bằng cách chạm vào biểu tượng Bitchat. Menu này có các tùy chọn sau:



- Thiết lập chế độ hiển thị (hệ thống/sáng/tối).
- Bật tính năng "Bằng chứng công việc" cho geohash để ngăn chặn thư rác (tùy chọn)
- Hãy bật Tor để tăng cường quyền riêng tư.


![image](assets/en/16.webp)


### Thiết lập danh tính của bạn


Nhấn vào ô `bitchat/anonXXXX` ở trên cùng để chọn tên người dùng của bạn. Đây là cách người khác sẽ nhìn thấy bạn cả ở chế độ Bluetooth và internet. Ví dụ, bạn có thể thay đổi "anon2022" thành tên người dùng mà bạn muốn.


![image](assets/en/03.webp)


### Chọn kênh mạng


Sử dụng menu `#location channels` (bên phải tên người dùng) để chuyển đổi giữa các loại kết nối:



- BLE Mesh***: Chế độ Bluetooth mặc định (không có internet, phạm vi từ 10 đến 50 mét)
- #geohashes**: Các cộng đồng địa lý được kết nối Internet sử dụng [giao thức Nostr](https://nostr.com/)


Khi bạn chọn chế độ `#geohashes`, Bitchat sẽ tích hợp với giao thức Nostr để tạo ra các cộng đồng dựa trên vị trí địa lý. Tin nhắn của bạn được đăng tải lên các `máy chủ chuyển tiếp Nostr phi tập trung` thay vì mạng ngang hàng của Bitchat, cho phép các cuộc trò chuyện rộng hơn nhưng vẫn được lọc theo vị trí. Điều quan trọng là, khóa định danh Bitchat của bạn sẽ được mã hóa để ký tất cả các sự kiện Nostr nhằm duy trì xác thực, trong khi các thẻ geohash (như `#u4pruyd` cho một khu phố) sẽ lọc tin nhắn theo mức độ chính xác bạn đã chọn. Điều này có nghĩa là bạn có thể tham gia vào các cuộc thảo luận địa phương mà không cần tiết lộ tọa độ chính xác, mặc dù cần có kết nối internet.


![image](assets/en/04.webp)


### Theo dõi các đồng nghiệp

Giấy phép: CC-BY-SA-V4

Bộ đếm người dùng hiển thị số người dùng:



- Gần đó (BLE Mesh) hoặc
- Trong vùng geohash của bạn (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Trò chuyện toàn cầu & Tin nhắn riêng tư


Bitchat cung cấp hai chế độ giao tiếp riêng biệt để phù hợp với các nhu cầu khác nhau:



- Kênh công cộng:** Để trò chuyện cởi mở với những người khác. Bạn có thể kết nối thông qua mạng lưới BLE cục bộ với người dùng ở gần hoặc qua #geohash toàn cầu dành cho các cộng đồng dựa trên vị trí và có kết nối internet.
- Tin nhắn riêng tư:** Để trò chuyện riêng tư, an toàn. Những tin nhắn này thiết lập kết nối trực tiếp, được mã hóa để giữ bí mật các cuộc trao đổi của bạn.


Hiểu rõ cả hai phương thức này sẽ giúp bạn điều hướng các cuộc hội thoại của mình dễ dàng hơn.


### Kênh công cộng: Trung tâm cộng đồng


Menu `#location channels` (góc trên bên phải) điều khiển khả năng hiển thị công khai của bạn. Chọn `mesh` sẽ kết nối bạn với tất cả người dùng lân cận thông qua mạng lưới BLE, thường là các thiết bị trong phạm vi 10-50 mét. Điều này tạo ra một diễn đàn mở nơi các tin nhắn được phát đến tất cả mọi người trong phạm vi, lý tưởng cho các thông báo sự kiện hoặc cảnh báo cục bộ.


Để mở rộng phạm vi địa lý, hãy chọn bất kỳ thẻ `#geohash` nào để tham gia các cộng đồng trực tuyến được lọc theo vị trí. Các kênh này sử dụng bộ chuyển tiếp giao thức Nostr, cho phép liên lạc giữa các thành phố hoặc khu vực trong khi vẫn duy trì tính phù hợp dựa trên vị trí. Tin nhắn của bạn sẽ hiển thị trực tiếp cho những người khác trong cùng kênh, và người tham gia mới sẽ tự động thấy lịch sử tin nhắn gần đây khi tham gia.


![image](assets/en/06.webp)


### Trò chuyện riêng tư: Bảo mật & Mã hóa


Để bắt đầu cuộc trò chuyện riêng tư, hãy nhấn một lần trực tiếp vào bất kỳ tên người dùng nào hiển thị trong mục "Tổng quan người dùng". Bạn cũng có thể nhấn vào biểu tượng ngôi sao để đánh dấu người dùng này là người dùng yêu thích, điều này sẽ giúp họ luôn hiển thị trong danh sách liên lạc của bạn ngay cả khi họ ngoại tuyến.


![image](assets/en/07.webp)


Bitchat tự động khởi tạo "quá trình bắt tay bảo mật" khi bạn bắt đầu một cuộc trò chuyện riêng tư. Các thiết bị trao đổi khóa tạm thời để tạo ra một đường hầm mã hóa dành riêng cho cuộc trò chuyện của bạn. Quá trình này đảm bảo rằng tất cả tin nhắn và tệp được chia sẻ của bạn luôn được bảo mật nhờ mã hóa đầu cuối liên tục. Tin nhắn riêng tư hỗ trợ chia sẻ văn bản và tệp.


![image](assets/en/08.webp)


## 4️⃣ Các tính năng bổ sung


Bạn có thể truy cập bảng thao tác ngay lập tức bằng cách gõ `/` ở bất kỳ đâu trong Bitchat. Thao tác này sẽ hiển thị menu lệnh để thực hiện các thao tác nhanh.



- Quản lý kết nối**: `Chặn người dùng` hoặc `Bỏ chặn người dùng khác`
- Điều khiển kênh**: `Hiển thị kênh` hoặc `Tham gia/tạo kênh`
- Tương tác xã hội**: `Gửi cái ôm ấm áp` hoặc `tát bằng cá hồi` 🎣
- Bảo trì trò chuyện**: `Xóa tin nhắn trò chuyện`
- Công cụ bảo mật**: `Xem ai đang trực tuyến` hoặc `Gửi tin nhắn riêng tư`


Các lệnh được thực thi ngay lập tức - ví dụ như `/block Satoshi` để bịt miệng những người chỉ trích hoặc `/hug Hal` để lan tỏa sự tích cực 🫂.


![image](assets/en/09.webp)


## 5️⃣ Tạo kênh


Các kênh trong Bitchat cho phép giao tiếp có tổ chức xoay quanh các chủ đề, địa điểm hoặc cộng đồng. Để tạo kênh của riêng bạn, hãy làm theo quy trình sau:


### Bước 1: Tạo kênh


Để tạo kênh, hãy nhập `/j` hoặc `/join` theo sau là `tên kênh` trong bất kỳ khung chat nào (ví dụ: `/j <tên kênh>`). Sau khi tạo, một `biểu tượng ⧉` mới sẽ xuất hiện để báo hiệu kênh mới. Người dùng khác có thể tham gia bằng cách nhập cùng lệnh đó (ví dụ: `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Bước 2: Cấu hình cài đặt


Ngoài các lệnh mặc định, các cài đặt sau đây cũng có sẵn trong một kênh:



- Sử dụng lệnh `/save` để lưu tin nhắn cục bộ.
- `/transfer` để chuyển quyền sở hữu kênh và
- Sử dụng lệnh `/pass` để thay đổi mật khẩu kênh.


Đối với các cộng đồng riêng tư, lệnh này cho phép bảo vệ bằng mật khẩu, yêu cầu các thành viên được chấp thuận phải nhập mật khẩu tùy chỉnh trước khi tham gia.


## 6️⃣ Chế độ hoảng loạn


Giờ hãy nói về chế độ "khẩn cấp": nhấn ba lần vào biểu tượng "Bitchat" sẽ xóa hoàn toàn tất cả tin nhắn và dữ liệu cục bộ trong ứng dụng. Đây là biện pháp bảo vệ quyền riêng tư tối ưu, hoàn hảo cho những tình huống cần sự kín đáo ngay lập tức.


**Lưu ý quan trọng:** _Chế độ khẩn cấp là chế độ vĩnh viễn. Sau khi kích hoạt, dữ liệu không thể khôi phục được. Hãy sử dụng thận trọng._


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Các kênh Geohash cho phép các cuộc trò chuyện có mục tiêu dựa trên 'vị trí địa lý' thay vì các kết nối mạng truyền thống. Tính năng này biến các cuộc trò chuyện thông thường thành một công cụ giao tiếp nhận biết vị trí, lý tưởng cho việc phối hợp địa phương, xây dựng cộng đồng và thảo luận theo vị trí cụ thể.


### Cách thức hoạt động của `#geohashes`


Hệ thống này chia thế giới thành các ô vuông lưới bằng cách sử dụng [hệ thống Geohash](https://en.wikipedia.org/wiki/Geohash), trong đó mỗi ký tự trong mã băm thể hiện độ chính xác cao hơn:



- Cấp độ 4** (ví dụ: `u33d`): Bao phủ diện tích khoảng 25km × 25km - lý tưởng cho các cuộc thảo luận trên toàn thành phố.
- Cấp độ 6** (ví dụ: `u33d8z`): Bao phủ khoảng 1,2 km × 1,2 km - độ chính xác vùng lân cận
- Cấp độ 8** (ví dụ: `u33d8z1k`): Bao phủ diện tích khoảng 150 m × 150 m - độ chính xác theo đoạn đường


Lựa chọn độ chính xác cân bằng giữa quyền riêng tư và tính hữu dụng: các cấp độ cao hơn tạo ra các khu vực riêng tư hơn nhưng tiết lộ vị trí của bạn chính xác hơn.


### Tham gia kênh `#geohash`


1. Truy cập menu `#location channels`.

2. Chọn mức độ chính xác mong muốn và nhập `#geohash` (ví dụ: #u33d)

3. Nhấn vào nút `Dịch chuyển` để tham gia kênh `#location`.


![image](assets/en/12.webp)


Ngoài ra, bạn có thể chạm vào biểu tượng bản đồ để sử dụng chế độ xem bản đồ nhằm xác định mức độ chính xác và chạm vào "chọn" để tham gia kênh #location.


![image](assets/en/13.webp)


**Lưu ý quan trọng**: Chức năng #geohash yêu cầu kết nối internet hoạt động - không giống như mạng lưới BLE hoạt động ngoại tuyến thông qua Bluetooth.


## 8️⃣ Bản đồ nhiệt


Bản đồ nhiệt là một cách thú vị để khám phá các sự kiện và kênh Bitchat trên toàn thế giới. [Bitmap](https://bitmap.lat/) trực quan hóa và theo dõi các tin nhắn ẩn danh, dựa trên vị trí trên mạng Nostr, hiển thị các sự kiện Nostr diễn ra trong thời gian ngắn. Hãy xem và tham gia các kênh và cuộc trò chuyện theo vị trí cụ thể.


![image](assets/en/15.webp)


## 🎯 Kết luận


Bitchat cho phép liên lạc an toàn, phi tập trung trong những trường hợp mà tin nhắn truyền thống không hoạt động. Ứng dụng có thể hoạt động mà không cần cơ sở hạ tầng internet nhờ mạng lưới BLE mesh, phù hợp cho các cuộc biểu tình, khu vực thiên tai và vùng sâu vùng xa nơi kết nối bị hạn chế hoặc kiểm duyệt. Ứng dụng đảm bảo quyền riêng tư thông qua mã hóa khóa tạm thời, kênh định vị dựa trên geohash và chế độ xóa dữ liệu khẩn cấp.


Ứng dụng vẫn đang trong giai đoạn phát triển ban đầu, nhưng đã cho thấy nhiều tiềm năng. Người dùng nên lường trước những lỗi nhỏ có thể xảy ra và báo cáo sự cố qua [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Ứng dụng đang được lên kế hoạch cải tiến, bao gồm tích hợp `ecash` cho các giao dịch riêng tư trong ứng dụng bằng giao thức Cashu.


![image](assets/en/14.webp)


## 📚 Tài nguyên Bitchat


[Github](https://github.com/permissionlesstech) | [Trang web](https://bitchat.free/)| [Sách trắng](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)