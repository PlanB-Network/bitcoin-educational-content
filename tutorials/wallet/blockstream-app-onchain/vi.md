---
name: Blockstream App - Onchain
description: Thiết lập ứng dụng Blockstream trên thiết bị di động và quản lý các giao dịch trên chuỗi
---
![cover](assets/cover.webp)


## 1. Giới thiệu


### 1.1 Mục tiêu hướng dẫn





- Hướng dẫn này giải thích cách sử dụng ứng dụng di động **Blockstream App** để quản lý Bitcoin **onchain** Wallet, tức là các giao dịch được ghi trực tiếp trên Blockchain Bitcoin chính.
- Nó bao gồm cài đặt, cấu hình ban đầu, tạo Software Wallet và các hoạt động nhận và gửi bitcoin.
- Lưu ý: Các hướng dẫn khác trong Phụ lục bao gồm Liquid, Watch-Only và phiên bản dành cho máy tính để bàn.



![image](assets/fr/01.webp)



### 1.2 Đối tượng mục tiêu





- **Người mới bắt đầu**: Người dùng muốn quản lý bitcoin của mình bằng ứng dụng di động trực quan.
- **Người dùng trung cấp**: Những người muốn tìm hiểu về các chức năng trên chuỗi và các tùy chọn quyền riêng tư như Tor hoặc SPV.



### 1.3. Nhắc nhở về ví Hot





- **Hot Wallet**, **Software Wallet**, **Wallet di động**, **Software Wallet**: tất cả tên gọi của một ứng dụng được cài đặt trên điện thoại thông minh, máy tính hoặc bất kỳ thiết bị nào được kết nối Internet, cho phép quản lý và bảo mật khóa riêng từ Bitcoin Wallet.
- Không giống như **ví phần cứng**, còn được gọi là **ví Cold**, nơi cô lập khóa ngoại tuyến, ví phần mềm hoạt động trong môi trường được kết nối, khiến chúng dễ bị tấn công mạng hơn.





- Sử dụng được khuyến nghị:
    - Thích hợp để quản lý lượng Bitcoin vừa phải, đặc biệt là cho các giao dịch hàng ngày.
    - Phù hợp cho người mới bắt đầu hoặc người dùng có tài sản hạn chế, đối với họ, Hardware Wallet có vẻ không cần thiết.





- **Hạn chế**: Ít an toàn hơn khi lưu trữ số tiền lớn hoặc tiết kiệm dài hạn. Trong trường hợp này, hãy chọn Hardware Wallet.




## 2. Giới thiệu ứng dụng Blockstream





- Ứng dụng **Blockstream** là ứng dụng di động (iOS, Android) và máy tính để bàn dùng để quản lý danh mục đầu tư và tài sản Bitcoin trên Liquid Network. Được [Blockstream](https://blockstream.com/) mua lại vào năm 2016, trước đây ứng dụng này có tên là *Green Address* và sau đó là *Blockstream Green*.
- **Các tính năng chính**:
- Giao dịch **Onchain** trên Blockchain Bitcoin.
    - Giao dịch mạng **Liquid** (Sidechain dành cho giao dịch nhanh chóng, bảo mật).
- Danh mục đầu tư chỉ theo dõi để theo dõi các quỹ mà không cần truy cập vào khóa.
    - Tùy chọn riêng tư: kết nối qua **Tor**, kết nối với **nút cá nhân** qua Electrum hoặc xác minh **SPV** để giảm sự phụ thuộc vào các nút của bên thứ ba.
    - Chức năng **Replace-by-fee (RBF)** giúp tăng tốc các giao dịch chưa được xác nhận.
- **Khả năng tương thích**: Tích hợp ví phần cứng như **Blockstream Jade**.
- **Interface**: Dễ sử dụng cho người mới bắt đầu, có các tùy chọn nâng cao dành cho chuyên gia.
- **Lưu ý**: Hướng dẫn này tập trung vào việc sử dụng onchain. Các hướng dẫn khác trong Phụ lục bao gồm Liquid, Watch-Only và phiên bản dành cho máy tính để bàn.



## 3. Cài đặt và cấu hình ứng dụng Blockstream



### 3.1. tải xuống





- Đối với **Android**:
    - Tải xuống [Ứng dụng Blockstream](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) từ Cửa hàng Google Play.
    - Cách khác: Cài đặt thông qua tệp APK có sẵn trên [GitHub chính thức của Blockstream](https://github.com/Blockstream/green_android).
- Đối với **iOS**:
    - Tải xuống [Ứng dụng Blockstream](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) từ App Store.
- **Lưu ý**: Hãy tải xuống từ nguồn chính thức để tránh các ứng dụng lừa đảo.



### 3.2. cấu hình ban đầu





- **Màn hình chính**: Khi mở lần đầu, ứng dụng sẽ hiển thị màn hình chưa có Wallet được cấu hình. Các danh mục đầu tư đã tạo hoặc nhập sẽ xuất hiện ở đây sau.



![image](assets/fr/02.webp)





- **Tùy chỉnh cài đặt**: Nhấp vào "Cài đặt ứng dụng", điều chỉnh các tùy chọn bên dưới, nhấp vào "Lưu", khởi động lại ứng dụng và tạo danh mục đầu tư của bạn.



![image](assets/fr/03.webp)



#### 3.2.1. Quyền riêng tư được nâng cao (chỉ dành cho Android)





- **Chức năng**: Vô hiệu hóa ảnh chụp màn hình, ẩn bản xem trước ứng dụng trong trình quản lý tác vụ và khóa quyền truy cập khi điện thoại bị khóa.
- **Tại sao?**: Bảo vệ dữ liệu của bạn khỏi sự truy cập vật lý trái phép hoặc phần mềm độc hại chụp màn hình.


#### 3.2.2. Kết nối qua Tor





- **Chức năng**: Định tuyến lưu lượng mạng qua **Tor**, một mạng ẩn danh mã hóa các kết nối của bạn.
- **Tại sao?**: Ẩn IP Address của bạn và bảo vệ quyền riêng tư của bạn, lý tưởng nếu bạn không tin tưởng vào mạng của mình (ví dụ: Wi-Fi công cộng).
- **Nhược điểm**: Có thể làm chậm ứng dụng do mã hóa.
- **Khuyến nghị**: Kích hoạt Tor nếu tính bảo mật là ưu tiên hàng đầu, nhưng hãy kiểm tra tốc độ kết nối.


#### 3.2.3. Kết nối với một nút cá nhân





- **Chức năng**: Kết nối ứng dụng với **nút Bitcoin hoàn chỉnh** của bạn thông qua máy chủ **Electrum**.
- **Tại sao?**: Cung cấp khả năng kiểm soát hoàn toàn dữ liệu Blockchain, loại bỏ sự phụ thuộc vào máy chủ Blockstream.
- **Điều kiện tiên quyết**: Một nút Bitcoin đã được cấu hình.
- **Khuyến nghị**: Người dùng nâng cao muốn có quyền tối đa.


#### 3.2.4. Xác minh SPV





- **Chức năng**: Sử dụng **Xác minh thanh toán đơn giản (SPV)** để xác minh trực tiếp một số dữ liệu Blockchain mà không cần tải xuống toàn bộ chuỗi.
- **Tại sao?**: Giảm sự phụ thuộc vào nút mặc định của Blockstream, đồng thời vẫn nhẹ cho thiết bị di động.
- **Nhược điểm**: Ít an toàn hơn Full node vì nó phụ thuộc vào các nút của bên thứ ba để lấy một số thông tin.
- **Khuyến nghị**: Kích hoạt SPV nếu bạn không thể sử dụng nút cá nhân nhưng muốn sử dụng Full node để có bảo mật tối ưu.





## 4. Tạo danh mục đầu tư Bitcoin trên chuỗi



### 4.1. Bắt đầu tạo





- **Thận trọng**: Thiết lập danh mục đầu tư của bạn ở môi trường riêng tư, không có máy quay hoặc người quan sát.
- Từ màn hình chính, nhấp vào "Bắt đầu":



![image](assets/fr/04.webp)





- Nếu bạn muốn quản lý **Cold Wallet** (Wallet ngoại tuyến): hãy nhấp vào **"Kết nối Jade "** để sử dụng Hardware Wallet Blockstream Jade hoặc các ví Cold tương thích khác.



![image](assets/fr/05.webp)





- Màn hình tiếp theo xuất hiện:



![image](assets/fr/06.webp)





- (1) **"Setup Mobile Wallet"** : Tạo Hot Wallet mới (Hot Wallet).
- (2) **"Khôi phục từ bản sao lưu"**: Nhập danh mục đầu tư hiện có bằng cụm từ Mnemonic (12 hoặc 24 từ). Thận trọng: Không nhập cụm từ Cold Wallet vì nó sẽ bị lộ trên thiết bị được kết nối, làm mất hiệu lực bảo mật.
- (3) **"Chỉ xem"**: Nhập danh mục chỉ đọc hiện có để xem số dư (ví dụ: Cold Wallet của bạn) mà không hiển thị cụm từ Mnemonic. Xem hướng dẫn Chỉ xem trong phần phụ lục.



**Trong hướng dẫn này**: Nhấp vào **"Thiết lập Wallet di động"** để tạo Hot Wallet.


Wallet của bạn sẽ tự động được tạo và trang chủ Wallet, ở đây được gọi là "Wallet 5 của tôi", sẽ được hiển thị:



![image](assets/fr/07.webp)



**Quan trọng**: Ứng dụng Blockstream đã đơn giản hóa việc tạo Wallet bằng cách không tự động hiển thị cụm từ seed gồm 12 từ. *Mặc dù danh mục đầu tư hiện được tạo chỉ bằng một cú nhấp chuột, bạn vẫn có nguy cơ mất quyền truy cập vào tiền của mình nếu không lưu cụm từ seed*.



### 4.2. Lưu câu seed





- Trên màn hình chính của Wallet, hãy nhấp vào tab "Bảo mật", sau đó nhấp vào lời nhắc "Sao lưu" hoặc menu "Cụm từ khôi phục":



![image](assets/fr/08.webp)



Cụm từ 12 từ seed sẽ được hiển thị để bạn lưu lại.





- Hãy ghi lại cụm từ khôi phục của bạn thật cẩn thận. Viết nó ra giấy hoặc kim loại và cất giữ ở nơi an toàn (nơi an toàn, ngoại tuyến). Cụm từ này là cách duy nhất để bạn truy cập bitcoin của mình trong trường hợp mất thiết bị hoặc xóa ứng dụng.
- Điều quan trọng cần lưu ý là bất kỳ ai có cụm từ này đều có thể đánh cắp toàn bộ bitcoin của bạn. Tuyệt đối không lưu trữ dưới dạng kỹ thuật số:
 - Không có ảnh chụp màn hình
 - Không có bản sao lưu đám mây, email hoặc tin nhắn
 - Không sao chép/dán (nguy cơ lưu vào bảng tạm)



**! Điểm này rất quan trọng**. Để biết thêm thông tin về sao lưu:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Xác nhận câu seed



Trước khi gửi tiền cho Address liên quan đến câu seed này, bạn phải kiểm tra bản sao lưu của 12 từ của mình.



Để thực hiện việc này, chúng ta sẽ ghi lại một tham chiếu, xóa Wallet, khôi phục nó bằng bản sao lưu và kiểm tra xem tham chiếu có thay đổi không.





- Trên màn hình chính của Wallet, nhấp vào tab "Cài đặt", sau đó nhấp vào "Chi tiết Wallet" và sao chép zPub ([khóa công khai mở rộng](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Lưu ý: zpub Address có thể được nhập vào ứng dụng Blockstream của bạn để sử dụng chức năng "Chỉ xem" (xem Phụ lục).





- Xóa ứng dụng, sau đó khôi phục Wallet thông qua **"Khôi phục từ bản sao lưu"** bằng cách nhập cụm từ Mnemonic, và kiểm tra xem zpub có thay đổi không. Nếu đúng, bản sao lưu của bạn đã chính xác và bạn có thể gửi tiền vào Wallet.





- Để tìm hiểu thêm về cách thực hiện thử nghiệm phục hồi, đây là hướng dẫn chuyên sâu:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Bảo mật quyền truy cập vào ứng dụng



Khóa quyền truy cập vào ứng dụng bằng mã PIN mạnh:




- Từ màn hình chính của Wallet, hãy vào **"Bảo mật"** sau đó nhấp vào **"Mã PIN"**
- Nhập và xác nhận **mã PIN ngẫu nhiên gồm 6 chữ số**.



**Tùy chọn sinh trắc học**: Có sẵn để thuận tiện hơn, nhưng kém an toàn hơn mã PIN mạnh (nguy cơ truy cập trái phép, ví dụ: quét vân tay hoặc khuôn mặt khi ngủ).



**Lưu ý**: Mã PIN bảo mật thiết bị, nhưng chỉ có thể sử dụng cụm từ seed để lấy tiền.





## 5. Sử dụng Wallet trên chuỗi



### 5.1. Nhận bitcoin





- Từ màn hình chính của danh mục đầu tư, nhấp vào '"**Giao dịch**" rồi nhấp vào **"Nhận"**.



![image](assets/fr/10.webp)





- Ứng dụng sẽ hiển thị **mã nhận Address trống** (định dạng SegWit v0, bắt đầu bằng `bc1q...`). Sử dụng mã Address mới mỗi khi nhận Bitcoin sẽ cải thiện tính bảo mật của bạn.





- **Tùy chọn**:
    - (1) "Bitcoin": nhấp để chọn lô hàng trên chuỗi hoặc Liquid và chọn tài sản.
    - (2) Nhấp vào các mũi tên để chọn một Address mới khác được liên kết với câu seed này.
    - (3) Bạn cũng có thể chọn Address từ những địa chỉ đã sử dụng/hiển thị bằng cách nhấp vào ba dấu chấm ở trên cùng bên phải rồi nhấp vào "Danh sách địa chỉ"
    - (4) Để yêu cầu số tiền cụ thể, hãy nhấp vào ba dấu chấm ở góc trên bên phải, chọn "Yêu cầu số tiền" và nhập số tiền mong muốn. Mã QR sẽ được cập nhật và Address sẽ được thay thế bằng URI thanh toán Bitcoin.




![image](assets/fr/11.webp)





- Chia sẻ Address/URI bằng cách nhấp vào "**Chia sẻ**", sao chép văn bản hoặc quét mã QR.
- **Xác minh**: Kiểm tra Address được chia sẻ với người nhận càng nhiều càng tốt để tránh lỗi hoặc tấn công (ví dụ: phần mềm độc hại sửa đổi bảng tạm).



### 5.2. gửi bitcoin





- Từ màn hình chính của danh mục đầu tư, nhấp vào "**Giao dịch**" rồi nhấp vào **"Gửi"** :



![image](assets/fr/12.webp)





- Nhập thông tin chi tiết:
    - (1) Nhập **Address của người nhận** bằng cách dán lên hoặc quét mã QR.
    - (2) Kiểm tra tài sản và tài khoản mà tiền được gửi đi.
    - (3) Chỉ định **số tiền** cần gửi. Bạn có thể chọn đơn vị: BTC, satoshi, USD, ...


Số lượng tối thiểu (giới hạn dush) vào ngày 03/08/2025 là 546 Sats.




    - (4) Chọn **phí giao dịch**:
        - Chọn từ các tùy chọn được đề xuất (ví dụ: nhanh, trung bình, chậm) tùy theo mức độ khẩn cấp và thời gian chuyển khoản gần đúng sẽ được hiển thị.
        - Đối với các mức phí tùy chỉnh, hãy điều chỉnh thủ công số lượng Satoshi trên mỗi vbyte (xem [Mempool.space](https://Mempool.space/) để biết giá thị trường).




![image](assets/fr/13.webp)





- **Kiểm tra**:
    - Kiểm tra Address, số tiền và phí trên màn hình tóm tắt.
    - Lỗi Address có thể dẫn đến mất tiền không thể phục hồi. Hãy cẩn thận với phần mềm độc hại sửa đổi bảng tạm.



![image](assets/fr/14.webp)





- **Xác nhận**: Trượt nút "Gửi" để ký và phân phối giao dịch.
- **Theo dõi**: Trong tab "Giao dịch" của Wallet, giao dịch sẽ hiển thị là "đang chờ xử lý" cho đến khi xác nhận (từ 1 đến 6 xác nhận):



![image](assets/fr/15.webp)





- Miễn là giao dịch chưa được xác nhận, chức năng "Replace by fee" (xem Phụ lục) cho phép bạn đẩy nhanh quá trình xử lý bằng cách tăng phí giao dịch:



![image](assets/fr/16.webp)




## Phụ lục



### A1. Các hướng dẫn khác về Blockstream



Sử dụng Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Nhập và theo dõi Wallet ở chế độ "Chỉ xem"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Phiên bản máy tính để bàn



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Giải thích về Replace-by-fee (RBF)



**Định nghĩa**: Replace-by-fee (RBF) là một tính năng của mạng Bitcoin cho phép người gửi đẩy nhanh quá trình xác nhận giao dịch **trên chuỗi** bằng cách đồng ý trả phí cao hơn.



**Giới hạn** :




- RBF không khả dụng cho giao dịch Liquid hoặc Lightning.
- Giao dịch ban đầu phải được đánh dấu là tương thích với RBF khi được tạo, đây là thao tác tự động mà ứng dụng Blockstream thực hiện.



**Thông tin thêm:**




- [Thuật ngữ](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Thực hành tốt nhất



Để sử dụng **Ứng dụng Blockstream** một cách an toàn và hiệu quả, hãy làm theo các khuyến nghị sau. Chúng sẽ giúp bạn bảo vệ tiền, tối ưu hóa giao dịch và giữ bí mật trên các mạng **Bitcoin (onchain)**, **Liquid** và **Lightning**.





- **Bảo mật cụm từ khôi phục của bạn**:
 - Hướng dẫn: Lưu cụm từ Mnemonic của bạn



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Sử dụng xác thực an toàn**:
 - Kích hoạt **mã PIN mạnh** hoặc **xác thực sinh trắc học** (nhận dạng dấu vân tay hoặc khuôn mặt) để bảo vệ quyền truy cập vào ứng dụng.
 - Không bao giờ chia sẻ mã PIN hoặc dữ liệu sinh trắc học của bạn.





- **Bảo vệ quyền riêng tư của bạn**:
 - generate là Address mới cho mỗi lần tiếp nhận trên chuỗi hoặc Liquid để hạn chế theo dõi trên Blockchain.
 - Kích hoạt các chức năng "Bảo mật nâng cao", "Tor" và "SPV".
 - Để có tính bảo mật tối đa, hãy kết nối Wallet của bạn với nút Bitcoin của riêng bạn thông qua máy chủ Electrum thay vì sử dụng nút công khai





- **Chọn mạng phù hợp nhất với nhu cầu của bạn**:
- **Onchain**: Được ưu tiên cho việc lưu ký dài hạn hoặc giao dịch có giá trị lớn (phí không đáng kể so với số tiền).
- **Liquid**: Sử dụng để chuyển tiền nhanh chóng, chi phí thấp với tính bảo mật cao.
- **Lightning**: Chọn dịch vụ chuyển tiền tức thời, chi phí thấp cho số tiền nhỏ.





- **Luôn kiểm tra địa chỉ giao hàng**:
 - Trước khi gửi tiền, vui lòng kiểm tra kỹ Address. Tiền gửi nhầm đến Address sẽ bị mất vĩnh viễn. Vui lòng sử dụng chức năng sao chép/dán hoặc quét mã QR, tuyệt đối không sao chép/sửa đổi Address bằng tay.





- **Tối ưu hóa chi phí**:
 - Đối với các giao dịch trên chuỗi, hãy chọn mức phí phù hợp (chậm, trung bình, nhanh) tùy theo mức độ khẩn cấp và tắc nghẽn mạng.
 - Sử dụng Liquid hoặc Lightning cho số lượng nhỏ.





- Giữ cho ứng dụng được cập nhật




### A4. Tài nguyên bổ sung





- Liên kết chính thức:
- [Trang web chính thức](https://blockstream.com/)
- [Hỗ trợ cho ứng dụng di động](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/) : tài liệu và trò chuyện
- [GitHub](https://github.com/Blockstream/green_android)





- Trình khám phá khối:
 - on chain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Thông tin về dòng khối](https://blockstream.info/Liquid)**
 - Sét: **[1ML (Lightning Network)](https://1ml.com/)**





- Học tập và hướng dẫn: **[Plan ₿ Network](https://planb.network/)**
 - Bảo mật cụm từ khôi phục của bạn



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Thuật ngữ](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Thuật ngữ](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb