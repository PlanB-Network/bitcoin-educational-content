---
name: Ứng dụng Blockstream - Chỉ xem
description: Làm thế nào để cấu hình Watch-only wallet trên ứng dụng Blockstream?
---

![cover](assets/cover.webp)


## 1. Giới thiệu


### 1.1 Mục tiêu của bài hướng dẫn





- Hướng dẫn này giải thích cách thiết lập và sử dụng tính năng **Chỉ xem** của ứng dụng di động **Ứng dụng Blockstream** để giám sát Bitcoin Wallet mà không cần truy cập vào khóa riêng của thiết bị.
- Nó bao gồm cài đặt, cấu hình ban đầu, nhập khóa công khai mở rộng và sử dụng khóa này để theo dõi số dư và địa chỉ nhận generate.
- Lưu ý: Các hướng dẫn khác được cung cấp trong phần phụ lục bao gồm Onchain, Liquid và phiên bản dành cho máy tính để bàn.



### 1.2. Đối tượng mục tiêu





- Người mới bắt đầu**: Người dùng muốn theo dõi danh mục đầu tư Bitcoin (thường liên quan đến Hardware Wallet) thông qua ứng dụng di động trực quan.
- Người dùng trung cấp**: Những người muốn quản lý danh mục đầu tư chỉ đọc trong khi sử dụng các tùy chọn bảo mật như Tor hoặc SPV.
- Người dùng Hardware Wallet**: Để kiểm tra số dư và địa chỉ generate mà không cần kết nối thiết bị.
- Doanh nghiệp và cửa hàng**:
 - Theo dõi các giao dịch của bạn cho mục đích kế toán mà không tiết lộ khóa riêng tư.
 - Xác minh các giao dịch đã nhận mà không cần nhập khóa riêng tư vào hệ thống thanh toán trực tuyến.
 - Cho phép nhân viên generate cấp địa chỉ tiếp tân mới mà không cần truy cập vào khóa riêng.
- Các tổ chức và gây quỹ cộng đồng**: Hiển thị số dư một cách minh bạch cho các nhà tài trợ mà không cho phép tiếp cận nguồn tiền.



### 1.3. Giới thiệu chế độ Chỉ xem



Wallet **Watch-Only** cho phép bạn theo dõi các giao dịch và số dư của Bitcoin Wallet mà không cần truy cập vào khóa riêng. Không giống như Wallet thông thường, nó chỉ lưu trữ dữ liệu công khai, chẳng hạn như **khóa công khai **mở rộng** (tạo ra "**xpub**", sau đó là "zpub", "ypub", v.v.), cho phép nó lấy địa chỉ nhận và theo dõi lịch sử giao dịch trên Blockchain Bitcoin. Việc không có khóa riêng tư khiến việc giải ngân tiền từ ứng dụng là không thể, đảm bảo tính bảo mật được tăng cường.



![image](assets/fr/10.webp)



**Tại sao nên sử dụng Watch-only wallet?





- Bảo mật**: Lý tưởng để theo dõi danh mục đầu tư được bảo mật bằng **Hardware Wallet** mà không tiết lộ khóa riêng trên thiết bị được kết nối.
- Tiện lợi**: Cho phép bạn kiểm tra số dư và địa chỉ người nhận mới của generate mà không cần kết nối Hardware Wallet.
- Tính bảo mật**: Tương thích với các tùy chọn như **Tor** hoặc **SPV** để hạn chế sự phụ thuộc vào máy chủ của bên thứ ba.
- Các trường hợp sử dụng**: Theo dõi tiền khi di chuyển, tạo địa chỉ để nhận thanh toán hoặc xác minh giao dịch mà không sợ lộ khóa riêng tư.



![image](assets/fr/01.webp)



### 1.4. Khóa công khai mở rộng



**Khóa công khai mở rộng** (xpub, ypub, zpub, v.v.) là một phần dữ liệu có nguồn gốc từ Bitcoin Wallet tạo ra tất cả các khóa công khai con và địa chỉ nhận liên quan của chúng, mà không cấp quyền truy cập vào khóa riêng.





- Nguyên lý hoạt động**: Khóa công khai mở rộng được tạo từ cụm từ seed thông qua một quy trình xác định (BIP-32). Nó tạo ra một cây phân cấp các khóa công khai con, mỗi khóa có thể được chuyển đổi thành một Address nhận. Sử dụng cùng một đường dẫn xuất (ví dụ: `m/44'/0'/0'`) như Wallet đang theo dõi, Watch-only wallet tạo ra cùng một địa chỉ, cho phép theo dõi tiền và tạo các địa chỉ nhận mới.



![image](assets/fr/11.webp)





- Các loại khóa công khai mở rộng
 - xpub**: Được sử dụng cho danh mục đầu tư Legacy (địa chỉ bắt đầu bằng "1", BIP-44) và danh mục đầu tư Taproot (địa chỉ bắt đầu bằng "bc1p", BIP-86).
 - ypub**: Được thiết kế cho ví SegWit tương thích (địa chỉ bắt đầu bằng "3", BIP-49).
 - zpub**: Liên kết với danh mục đầu tư SegWit gốc (địa chỉ bắt đầu bằng "bc1q", BIP-84).
 - Khác (tpub, upub, vpub, v.v.)**: Được sử dụng cho các mạng thay thế (như Testnet) hoặc các tiêu chuẩn cụ thể. Ví dụ: tpub dành cho mạng Testnet.





- Phân biệt**: Việc lựa chọn giữa xpub, ypub hoặc zpub phụ thuộc vào loại Address (cũ, SegWit, Taproot hoặc SegWit lồng nhau) và chuẩn BIP được Wallet sử dụng. Hãy kiểm tra định dạng mà danh mục nguồn của bạn yêu cầu để đảm bảo khả năng tương thích với Ứng dụng Blockstream.





- Bảo mật và bí mật**: Khóa công khai mở rộng không nhạy cảm về mặt bảo mật, vì nó không cho phép chi tiêu tiền (không cho phép truy cập vào khóa riêng). Tuy nhiên, nó nhạy cảm về mặt bảo mật, vì nó tiết lộ tất cả các địa chỉ công khai và lịch sử giao dịch liên quan.



**Khuyến nghị**: Bảo vệ khóa công khai mở rộng của bạn như thông tin nhạy cảm.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Nhắc nhở Hot Wallet





- Hot Wallet**, **Software Wallet**, **Wallet di động**, **Software Wallet**: tất cả tên gọi của một ứng dụng được cài đặt trên điện thoại thông minh, máy tính hoặc bất kỳ thiết bị nào được kết nối với Internet, cho phép quản lý và bảo mật khóa riêng từ Bitcoin Wallet.
- Không giống như **ví phần cứng**, còn được gọi là **ví Cold**, nơi cô lập khóa ngoại tuyến, ví phần mềm hoạt động trong môi trường được kết nối, khiến chúng dễ bị tấn công mạng hơn.





- Sử dụng được khuyến nghị**:
    - Thích hợp để quản lý lượng Bitcoin vừa phải, đặc biệt là cho các giao dịch hàng ngày.
    - Phù hợp cho người mới bắt đầu hoặc người dùng có tài sản hạn chế, đối với họ, Hardware Wallet có vẻ không cần thiết.





- Hạn chế**: Ít an toàn hơn khi lưu trữ số tiền lớn hoặc tiết kiệm dài hạn. Trong trường hợp này, hãy chọn Hardware Wallet.




## 2. Giới thiệu ứng dụng Blockstream





- Ứng dụng Blockstream** là ứng dụng di động (iOS, Android) và máy tính để bàn dùng để quản lý danh mục đầu tư và tài sản Bitcoin trên Liquid Network. Được [Blockstream](https://blockstream.com/) mua lại vào năm 2016, trước đây ứng dụng này có tên là *Green Address* và sau đó là *Blockstream Green*.
- Các tính năng chính**:
    - Giao dịch Onchain** trên Blockchain Bitcoin.
    - Giao dịch trên mạng **Liquid** (Sidechain dành cho giao dịch nhanh chóng, bảo mật).
    - Danh mục đầu tư chỉ theo dõi** để theo dõi các quỹ mà không cần truy cập vào khóa.
    - Tùy chọn riêng tư: kết nối qua **Tor**, kết nối với **nút cá nhân** qua Electrum hoặc xác minh **SPV** để giảm sự phụ thuộc vào các nút của bên thứ ba.
    - Chức năng **Replace-by-fee (RBF)** giúp tăng tốc các giao dịch chưa được xác nhận.
- Khả năng tương thích**: Tích hợp ví phần cứng như **Blockstream Jade**.
- Interface**: Trực quan dành cho người mới bắt đầu, với các tùy chọn nâng cao dành cho chuyên gia.
- Lưu ý**: Hướng dẫn này tập trung vào việc sử dụng Onchain. Các hướng dẫn khác trong Phụ lục bao gồm Onchain, Watch-Only và phiên bản máy tính để bàn.




## 3. Cài đặt và cấu hình ứng dụng Blockstream



### 3.1. tải xuống





- Đối với Android**:
    - Tải xuống [Ứng dụng Blockstream](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) từ Cửa hàng Google Play.
    - Cách khác: Cài đặt thông qua tệp APK có sẵn trên [GitHub chính thức của Blockstream](https://github.com/Blockstream/green_android).
- Đối với iOS**:
    - Tải xuống [Ứng dụng Blockstream](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) từ App Store.
- Lưu ý**: Hãy tải xuống từ nguồn chính thức để tránh các ứng dụng lừa đảo.



### 3.2. cấu hình ban đầu





- Màn hình chính**: Khi mở lần đầu, ứng dụng sẽ hiển thị màn hình chưa có Wallet được cấu hình. Các danh mục đầu tư đã tạo hoặc nhập sẽ xuất hiện ở đây sau.



![image](assets/fr/02.webp)





- Tùy chỉnh cài đặt**: Nhấp vào "Cài đặt ứng dụng", điều chỉnh các tùy chọn bên dưới, nhấp vào "Lưu", khởi động lại ứng dụng và tạo danh mục đầu tư của bạn.



![image](assets/fr/03.webp)



#### 3.2.1. Quyền riêng tư được nâng cao (chỉ dành cho Android)





- Chức năng**: Vô hiệu hóa ảnh chụp màn hình, ẩn bản xem trước ứng dụng trong trình quản lý tác vụ và khóa quyền truy cập khi điện thoại bị khóa.
- Tại sao?**: Bảo vệ dữ liệu của bạn khỏi sự truy cập vật lý trái phép hoặc phần mềm độc hại chụp màn hình.



#### 3.2.2. Kết nối qua Tor





- Chức năng**: Định tuyến lưu lượng mạng qua **Tor**, một mạng ẩn danh mã hóa các kết nối của bạn.
- Tại sao?**: Ẩn IP Address của bạn và bảo vệ quyền riêng tư của bạn, lý tưởng nếu bạn không tin tưởng vào mạng của mình (ví dụ: Wi-Fi công cộng).
- Nhược điểm**: Có thể làm chậm ứng dụng do mã hóa.
- Khuyến nghị**: Kích hoạt Tor nếu tính bảo mật là ưu tiên hàng đầu, nhưng hãy kiểm tra tốc độ kết nối.



#### 3.2.3. Kết nối với một nút cá nhân





- Chức năng**: Kết nối ứng dụng với **nút Bitcoin hoàn chỉnh** của bạn thông qua **máy chủ Electrum**.
- Tại sao?**: Cung cấp khả năng kiểm soát hoàn toàn dữ liệu Blockchain, loại bỏ sự phụ thuộc vào máy chủ Blockstream.
- Điều kiện tiên quyết**: Một nút Bitcoin đã được cấu hình.
- Khuyến nghị**: Người dùng nâng cao muốn có quyền tối đa.



#### 3.2.4. Xác minh SPV





- Chức năng**: Sử dụng **Xác minh thanh toán đơn giản (SPV)** để xác minh trực tiếp một số dữ liệu Blockchain mà không cần tải xuống toàn bộ chuỗi.
- Tại sao?**: Giảm sự phụ thuộc vào nút mặc định của Blockstream, đồng thời vẫn nhẹ cho thiết bị di động.
- Nhược điểm**: Ít an toàn hơn Full node vì nó phụ thuộc vào các nút của bên thứ ba để lấy một số thông tin.
- Khuyến nghị**: Kích hoạt SPV nếu bạn không thể sử dụng nút cá nhân nhưng muốn sử dụng Full node để có bảo mật tối ưu.





## 4. Tạo danh mục đầu tư "Chỉ theo dõi" Bitcoin



### 4.1. Khôi phục khóa công khai mở rộng



Để thiết lập Watch-only wallet, trước tiên bạn phải lấy khóa công khai mở rộng (xpub, ypub, zpub, v.v.) của Wallet cần giám sát. Thông tin này thường có sẵn trong phần cài đặt hoặc phần "Thông tin Wallet" của phần mềm hoặc Hardware Wallet.





- Ví dụ với ứng dụng Blockstream: Từ màn hình chính của Wallet, hãy vào "Cài đặt", sau đó vào "Chi tiết Wallet" và sao chép zpub:



![image](assets/fr/09.webp)





- Phương án 1: generate là mã QR chứa khóa công khai mở rộng để quét ở bước tiếp theo.
- Phương án 2: Sử dụng output descriptor nếu Wallet của bạn có chức năng này.



### 4.2. nhập khẩu Wallet Chỉ xem





- Thận trọng**: Thiết lập danh mục đầu tư của bạn ở môi trường riêng tư, không có máy quay hoặc người quan sát.
- Từ màn hình chính, nhấp vào "Thiết lập danh mục đầu tư mới" rồi nhấp vào "Bắt đầu":



![image](assets/fr/04.webp)





- Màn hình tiếp theo xuất hiện:



![image](assets/fr/06.webp)






- (1) **"Thiết lập Wallet di động"**: Tạo Hot Wallet mới. Xem hướng dẫn "Ứng dụng Blockstream - Onchain" trong phần phụ lục.
- (2) **"Khôi phục từ bản sao lưu"**: Nhập danh mục đầu tư hiện có bằng cụm từ Mnemonic (12 hoặc 24 từ). Thận trọng: Không nhập cụm từ này từ Cold Wallet, vì nó sẽ bị lộ trên thiết bị được kết nối, làm mất hiệu lực bảo mật.
- (3) **"Chỉ xem"**: tùy chọn mà chúng tôi quan tâm trong hướng dẫn này.





- Sau đó chọn "**Chữ ký đơn**" và mạng "**Bitcoin**":



![image](assets/fr/12.webp)





- Dán khóa công khai mở rộng (xpub, ypub, zpub, v.v.), quét mã QR tương ứng hoặc nhập mã output descriptor. Ngay cả khi ứng dụng chỉ định "xpub", các khóa ypub, zpub, v.v. cũng được xác thực. Sau đó, nhấp vào "Kết nối":



![image](assets/fr/13.webp)




### 4.3. Chỉ sử dụng Đồng hồ Wallet



Sau khi được nhập, Watch-only wallet sẽ hiển thị tổng số dư và lịch sử giao dịch của các địa chỉ được lấy từ khóa công khai mở rộng. Chỉ các giao dịch trên chuỗi mới được hiển thị (các giao dịch Liquid bị bỏ qua). Để theo dõi Liquid Wallet, hãy lặp lại thao tác nhập bằng cách chọn "Liquid" ở bước trước.





- Xem số dư và lịch sử**: từ màn hình chính, xem tổng số dư và lịch sử giao dịch trên chuỗi:



![image](assets/fr/14.webp)





- generate nhận Address**: Nhấp vào "Giao dịch", sau đó "Nhận" để tạo Address trên chuỗi mới. Chia sẻ qua mã QR hoặc sao chép để nhận tiền:



![image](assets/fr/15.webp)





- Gửi tiền**: Nhấp vào **"Giao dịch"**, sau đó **"Gửi"**. Bạn có thể nhập:
 - Address của người nhận.
 - Số tiền giao dịch.
 - Phí giao dịch.



Tuy nhiên, vì Watch-only wallet không giữ khóa riêng tư nên bạn không thể gửi tiền trực tiếp. Để ký giao dịch, hãy kết nối Hardware Wallet hoặc Exchange PSBT của bạn bằng cách quét mã QR (ví dụ: tùy chọn này có trên Coldcard Q).



![image](assets/fr/16.webp)





- Lưu ý**: Luôn kiểm tra mã Address nhận và thông tin giao dịch để tránh sai sót. Tiền đã gửi nhầm mã Address sẽ không thể được hoàn lại.




## Phụ lục



### A1. Các hướng dẫn khác về ứng dụng Blockstream





- Sử dụng mạng Onchain:



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Sử dụng Liquid Network:



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Phiên bản máy tính để bàn:



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Khóa công khai mở rộng





- Thuật ngữ:
 - [Khóa công khai mở rộng](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Khóa học :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Thực hành tốt nhất



Để sử dụng **Ứng dụng Blockstream** một cách an toàn và hiệu quả, hãy làm theo các khuyến nghị sau. Chúng sẽ giúp bạn bảo vệ tiền, tối ưu hóa giao dịch và giữ bí mật trên các mạng **Bitcoin (onchain)**, **Liquid** và **Lightning**.





- Bảo mật cụm từ khôi phục của bạn**:
 - Hướng dẫn: Lưu cụm từ Mnemonic của bạn



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Sử dụng xác thực an toàn**:
 - Kích hoạt **mã PIN mạnh** hoặc **xác thực sinh trắc học** (nhận dạng dấu vân tay hoặc khuôn mặt) để bảo vệ quyền truy cập vào ứng dụng.
 - Không bao giờ chia sẻ mã PIN hoặc dữ liệu sinh trắc học của bạn.





- Bảo vệ quyền riêng tư của bạn** :
 - generate là Address mới cho mỗi lần tiếp nhận trên chuỗi hoặc Liquid để hạn chế theo dõi trên Blockchain.
 - Kích hoạt các chức năng "Bảo mật nâng cao", "Tor" và "SPV".
 - Để có tính bảo mật tối đa, hãy kết nối Wallet của bạn với nút Bitcoin của riêng bạn thông qua máy chủ Electrum thay vì sử dụng nút công khai





- Chọn mạng phù hợp nhất với nhu cầu của bạn**:
 - Onchain**: Được ưu tiên cho việc lưu ký dài hạn hoặc giao dịch có giá trị lớn (phí không đáng kể so với số tiền).
 - Liquid**: Sử dụng để chuyển tiền nhanh chóng, chi phí thấp với tính bảo mật cao.
 - Lightning**: Chọn dịch vụ chuyển tiền tức thời, chi phí thấp cho số tiền nhỏ.





- Luôn kiểm tra địa chỉ giao hàng**:
 - Trước khi gửi tiền, vui lòng kiểm tra kỹ Address. Tiền gửi nhầm đến Address sẽ bị mất vĩnh viễn. Vui lòng sử dụng chức năng sao chép/dán hoặc quét mã QR, tuyệt đối không sao chép/sửa đổi Address bằng tay.





- Tối ưu hóa chi phí**:
 - Đối với các giao dịch trên chuỗi, hãy chọn mức phí phù hợp (chậm, trung bình, nhanh) tùy theo mức độ khẩn cấp và tắc nghẽn mạng.
 - Sử dụng Liquid hoặc Lightning cho số lượng nhỏ.





- Giữ cho ứng dụng được cập nhật




### A4. Tài nguyên bổ sung





- Liên kết chính thức của Blockstream:**
 - [Trang web chính thức](https://blockstream.com/)**
 - [Hỗ trợ cho ứng dụng di động](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : tài liệu và trò chuyện
 - [GitHub](https://github.com/Blockstream/green_android)**





- Trình khám phá khối :**
 - Trên chuỗi: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Thông tin về dòng khối](https://blockstream.info/Liquid)**
 - Sét: **[1ML (Lightning Network)](https://1ml.com/)**





 - Học tập và hướng dẫn:** **[Plan ₿ Network](https://planb.network/)** :
  - Bảo mật cụm từ khôi phục của bạn



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Thuật ngữ](https://planb.network/fr/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Thuật ngữ](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
