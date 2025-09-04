---
name: Ứng dụng Blockstream - Liquid
description: Cách cấu hình ứng dụng Blockstream và sử dụng Liquid Network
---
![cover](assets/cover.webp)


## 1. Giới thiệu


### 1.1 Mục tiêu hướng dẫn





- Hướng dẫn này giải thích cách sử dụng ứng dụng di động **Blockstream App** để quản lý danh mục đầu tư **Bitcoin Liquid**, tức là các giao dịch được ghi trực tiếp trên chuỗi bên "Liquid" của Bitcoin.
- Nó bao gồm cài đặt, cấu hình ban đầu, tạo Software Wallet và các hoạt động nhận và gửi bitcoin trên Liquid.
- Lưu ý: Các hướng dẫn khác trong Phụ lục bao gồm Onchain, Watch-Only và phiên bản dành cho máy tính để bàn.



### 1.2 Đối tượng mục tiêu





- Người mới bắt đầu**: Người dùng muốn quản lý bitcoin của mình bằng ứng dụng di động trực quan, tích hợp Liquid Network.
- Người dùng trung cấp**: Những người muốn tìm hiểu về các chức năng trên chuỗi và các tùy chọn quyền riêng tư như Tor hoặc SPV.



### 1.3 Giới thiệu Liquid



**Liquid** là **Sidechain** của Bitcoin, do **[Blockstream](https://blockstream.com/Liquid/)** phát triển, được thiết kế để cung cấp chức năng nhanh hơn, mạnh hơn Confidential Transactions và tiên tiến hơn, đồng thời vẫn kết nối với Blockchain Bitcoin chính.



Sidechain là một Blockchain độc lập, hoạt động song song với Bitcoin, sử dụng cơ chế được gọi là **chốt hai chiều**. Hệ thống này khóa bitcoin vào Blockchain chính để tạo ra **Liquid-Bitcoin (L-BTC)**, các token lưu hành trên Liquid Network trong khi vẫn giữ nguyên giá trị ngang bằng với bitcoin gốc. Tiền có thể được trả lại cho Blockchain Bitcoin bất cứ lúc nào.



![image](assets/fr/17.webp)






- (1) Peg-in**: Bitcoin (BTC) được liên kết với Blockchain chính bởi liên đoàn Liquid. Đổi lại, một lượng Bitcoin Liquid (L-BTC) tương đương, đảm bảo tính ngang bằng giữa hai chuỗi, được phát hành trên Blockchain Liquid và gửi đến người dùng.





- (2) Giao dịch độc lập**: Giao dịch có thể chạy đồng thời và độc lập trên Blockchain (BTC) và Sidechain Liquid (L-BTC) chính, tùy thuộc vào yêu cầu của người dùng.





- (3) Peg-out**: Người dùng gửi Liquid-Bitcoin (L-BTC) trở lại liên đoàn Liquid. Liên đoàn sau đó sẽ mở khóa một lượng Bitcoin (BTC) tương đương trên Blockchain chính và chuyển chúng cho người dùng.



Liquid dựa trên một **liên minh** gồm những người tham gia đáng tin cậy (các sàn giao dịch, các công ty Bitcoin được công nhận) quản lý việc xác thực khối và neo song phương. Không giống như Blockchain, Bitcoin phi tập trung và phụ thuộc vào thợ đào, Liquid là một mạng lưới **liên minh**, nghĩa là tính bảo mật và quản trị của nó phụ thuộc vào những người tham gia này. Mặc dù điều này ngụ ý một sự thỏa hiệp về tính phi tập trung, nhưng nó cho phép tối ưu hóa hiệu suất và chức năng nâng cao.



![image](assets/fr/18.webp)



##### Tại sao nên sử dụng Liquid?





- Tốc độ**: Giao dịch trên Liquid được xác nhận trong khoảng **1 phút**, so với 10 phút hoặc hơn đối với giao dịch trên chuỗi, nhờ vào các khối được tạo ra mỗi phút bởi liên đoàn các trình xác thực.
- Tính bảo mật được cải thiện**: Liquid sử dụng **Confidential Transactions**, giúp ẩn số lượng và loại tài sản được chuyển nhượng, giúp giao dịch riêng tư hơn (mặc dù địa chỉ vẫn hiển thị).
- Phí thấp**: Giao dịch trên Liquid thường ít tốn kém hơn, lý tưởng cho các giao dịch thường xuyên hoặc số tiền nhỏ.
- Nhiều tài sản**: Ngoài L-BTC, Liquid hỗ trợ phát hành các tài sản kỹ thuật số khác, chẳng hạn như stablecoin hoặc token, để sử dụng trong các ứng dụng cụ thể.
- Trường hợp sử dụng**: Liquid đặc biệt phù hợp với các sàn giao dịch đa nền tảng, thanh toán nhanh hoặc các ứng dụng yêu cầu hợp đồng thông minh, đồng thời vẫn được liên kết với tính bảo mật của Bitcoin.



**Lưu ý: Hướng dẫn này tập trung vào việc sử dụng Liquid thông qua ứng dụng Blockstream. Để hiểu sâu hơn về Liquid Network, bạn có thể tìm thấy tài liệu tham khảo trong phần phụ lục.



### 1.4. Nhắc nhở Hot Wallet





- Hot Wallet**, **Software Wallet**, **Wallet di động**, **Software Wallet**: tất cả tên gọi của một ứng dụng được cài đặt trên điện thoại thông minh, máy tính hoặc bất kỳ thiết bị nào được kết nối với Internet, cho phép quản lý và bảo mật khóa riêng từ Bitcoin Wallet.
- Không giống như **ví phần cứng**, còn được gọi là **ví Cold**, là loại ví cô lập khóa ngoại tuyến, ví phần mềm hoạt động trong môi trường được kết nối, khiến chúng dễ bị tấn công mạng hơn.





- Sử dụng được khuyến nghị**:
    - Thích hợp để quản lý lượng Bitcoin vừa phải, đặc biệt là cho các giao dịch hàng ngày.
    - Phù hợp cho người mới bắt đầu hoặc người dùng có tài sản hạn chế, đối với họ, Hardware Wallet có vẻ không cần thiết.





- Hạn chế**: Ít an toàn hơn khi lưu trữ số tiền lớn hoặc tiết kiệm dài hạn. Trong trường hợp này, hãy chọn Hardware Wallet.




## 2. Giới thiệu ứng dụng Blockstream





- Ứng dụng Blockstream** là ứng dụng di động (iOS, Android) và máy tính để bàn dùng để quản lý ví và tài sản Bitcoin trên Liquid Network. Được [Blockstream](https://blockstream.com/) mua lại vào năm 2016, trước đây ứng dụng này có tên là *Green Address* và sau đó là *Blockstream Green*.
- Các tính năng chính**:
    - Giao dịch Onchain** trên Blockchain Bitcoin.
    - Giao dịch trên mạng **Liquid** (Sidechain dành cho giao dịch nhanh chóng, bảo mật).
    - Danh mục đầu tư chỉ theo dõi** để theo dõi các quỹ mà không cần truy cập vào khóa.
    - Tùy chọn riêng tư: kết nối qua **Tor**, kết nối với **nút cá nhân** qua Electrum hoặc xác minh **SPV** để giảm sự phụ thuộc vào các nút của bên thứ ba.
    - Chức năng **Replace-by-fee (RBF)** giúp tăng tốc các giao dịch chưa được xác nhận.
- Khả năng tương thích**: Tích hợp ví phần cứng như **Blockstream Jade**.
- Interface**: Dễ sử dụng cho người mới bắt đầu, có các tùy chọn nâng cao dành cho chuyên gia.
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





## 4. Tạo danh mục đầu tư Bitcoin trên chuỗi



### 4.1. Bắt đầu tạo





- Thận trọng**: Thiết lập danh mục đầu tư của bạn ở môi trường riêng tư, không có máy quay hoặc người quan sát.
- Từ màn hình chính, nhấp vào "Bắt đầu":



![image](assets/fr/04.webp)





- Nếu bạn muốn quản lý **Cold Wallet** (Wallet ngoại tuyến): hãy nhấp vào **"Kết nối Jade "** để sử dụng Hardware Wallet Blockstream Jade hoặc các ví Cold tương thích khác.



![image](assets/fr/05.webp)






- Màn hình tiếp theo xuất hiện:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Tạo Hot Wallet (Hot Wallet) mới.
- (2) **"Khôi phục từ bản sao lưu"**: Nhập danh mục đầu tư hiện có bằng cụm từ Mnemonic (12 hoặc 24 từ). Cảnh báo: Không nhập cụm từ này từ Cold Wallet, vì nó sẽ bị lộ trên thiết bị được kết nối, làm mất hiệu lực bảo mật.
- (3) **"Chỉ xem"**: Nhập danh mục chỉ đọc hiện có để xem số dư (ví dụ: Cold Wallet của bạn) mà không hiển thị cụm từ Mnemonic. Xem hướng dẫn "Chỉ xem" trong phần phụ lục.



**Trong hướng dẫn này**: Nhấp vào **"Thiết lập Wallet di động"** để tạo Hot Wallet.


Wallet của bạn sẽ được tự động tạo và trang chủ Wallet, ở đây được gọi là "Wallet 5 của tôi", sẽ được hiển thị:



![image](assets/fr/07.webp)



**Quan trọng**: Ứng dụng Blockstream đã đơn giản hóa việc tạo Wallet bằng cách không tự động hiển thị cụm từ seed gồm 12 từ. *Mặc dù danh mục đầu tư hiện đã được tạo chỉ bằng một cú nhấp chuột, nhưng bạn vẫn có nguy cơ mất quyền truy cập vào tiền của mình nếu không lưu cụm từ seed*.



### 4.2. Lưu cụm từ seed





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

### 4.3. Kiểm tra câu seed



Trước khi gửi tiền đến Address liên kết với cụm từ seed này, bạn phải kiểm tra bản sao lưu của 12 từ của mình.


Để thực hiện điều này, chúng ta sẽ ghi lại một tham chiếu, xóa Wallet, khôi phục nó bằng bản sao lưu và kiểm tra xem tham chiếu có thay đổi không.





- Trên màn hình chính của Wallet, nhấp vào tab "Cài đặt", sau đó nhấp vào "Chi tiết Wallet" và sao chép zPub ([khóa công khai mở rộng](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Lưu ý: zpub Address có thể được nhập vào ứng dụng Blockstream của bạn để sử dụng chức năng "Chỉ xem" (xem Phụ lục).





- Xóa ứng dụng, sau đó khôi phục Wallet thông qua **"Khôi phục từ bản sao lưu"** bằng cách nhập cụm từ Mnemonic, và kiểm tra xem zpub có thay đổi không. Nếu đúng, bản sao lưu của bạn là chính xác và bạn có thể gửi tiền vào Wallet.





- Để tìm hiểu thêm về cách thực hiện thử nghiệm phục hồi, đây là hướng dẫn chuyên sâu:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Bảo mật quyền truy cập vào ứng dụng



Khóa quyền truy cập vào ứng dụng bằng mã PIN mạnh:




- Từ màn hình chính của Wallet, hãy vào **"Bảo mật"** sau đó nhấp vào **"Mã PIN"**
- Nhập và xác nhận **mã PIN ngẫu nhiên gồm 6 chữ số**.



**Tùy chọn sinh trắc học**: Có sẵn để thuận tiện hơn, nhưng kém an toàn hơn mã PIN mạnh (nguy cơ truy cập trái phép, ví dụ: quét vân tay hoặc khuôn mặt khi ngủ).



**Lưu ý**: Mã PIN bảo mật thiết bị, nhưng chỉ có cụm từ seed mới có thể được sử dụng để khôi phục tiền.





## 5. Sử dụng Liquid Wallet



### 5.1. Nhận bitcoin "L-BTC"



Để nhận Liquid-Bitcoin (L-BTC), có một số tùy chọn. Bạn có thể nhờ ai đó gửi trực tiếp cho mình bằng cách chia sẻ một Liquid nhận Address, được mô tả chi tiết bên dưới.



Ngoài ra, bạn có thể Exchange bitcoin của mình trên chuỗi hoặc thông qua Lightning Network để lấy L-BTC bằng cách sử dụng [một cầu nối như Boltz](https://boltz.Exchange/): nhập Liquid của bạn để nhận Address, thực hiện thanh toán theo ý muốn và nhận L-BTC của bạn.





- Từ màn hình chính của danh mục đầu tư, nhấp vào '"**Giao dịch**" rồi nhấp vào **"Nhận"**.



![image](assets/fr/19.webp)





- Theo mặc định, ứng dụng sẽ hiển thị một biên lai trống **Address, onchain** (định dạng SegWit v0, bắt đầu bằng `bc1q...`). Nhấp vào "Bitcoin" để chọn **Liquid Bitcoin**:



![image](assets/fr/20.webp)





- Tùy chọn** :
 - (1) Nhấp vào các mũi tên để chọn một Address mới khác được liên kết với câu seed này.
    - (2) Bạn cũng có thể chọn Address từ những địa chỉ đã sử dụng/hiển thị bằng cách nhấp vào ba dấu chấm ở trên cùng bên phải rồi nhấp vào "Danh sách địa chỉ"
    - (3) Để yêu cầu số tiền cụ thể, hãy nhấp vào ba dấu chấm ở góc trên bên phải, chọn "Yêu cầu số tiền" và nhập số tiền mong muốn. Mã QR sẽ được cập nhật và Address sẽ được thay thế bằng URI thanh toán Bitcoin.



![image](assets/fr/21.webp)





- Chia sẻ Address/URI bằng cách nhấp vào "**Chia sẻ**", sao chép văn bản hoặc quét mã QR.
- Xác minh**: Kiểm tra Address được chia sẻ với người nhận càng nhiều càng tốt để tránh lỗi hoặc tấn công (ví dụ: phần mềm độc hại sửa đổi bảng tạm).



### 5.2. gửi bitcoin





- Từ màn hình chính của danh mục đầu tư, nhấp vào "**Giao dịch**" rồi nhấp vào **"Gửi"** :



![image](assets/fr/22.webp)





- Nhập thông tin chi tiết**:
    - (1) Nhập **Address của người nhận** bằng cách dán lên hoặc quét mã QR.
    - (2) Kiểm tra tài sản và tài khoản mà tiền được gửi đi.
    - (3) Nhập **số tiền** cần gửi. Bạn có thể chọn đơn vị: L-BTC, L-satoshi, USD, ...



![image](assets/fr/23.webp)





- Kiểm tra** :
    - Kiểm tra Address, số tiền và phí trên màn hình tóm tắt.
    - Lỗi Address có thể dẫn đến mất tiền không thể phục hồi. Hãy cẩn thận với phần mềm độc hại sửa đổi bảng tạm.



![image](assets/fr/24.webp)





- Xác nhận**: Trượt nút "Gửi" để ký và phân phối giao dịch.
- Theo dõi**: Trong tab "Giao dịch" của Wallet, giao dịch sẽ hiển thị là "Chưa xác nhận", sau đó là "Đã xác nhận", rồi "Đã hoàn tất":



![image](assets/fr/25.webp)





- Thời gian giữa 2 khối là 1 phút trên Liquid, do đó giao dịch được xác nhận và hoàn tất nhanh chóng.




## Phụ lục



### A1. Các hướng dẫn khác về ứng dụng Blockstream



Sử dụng mạng Onchain



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Nhập và theo dõi Wallet ở chế độ "Chỉ theo dõi"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Phiên bản máy tính để bàn



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Thực hành tốt nhất



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
 - Để bảo mật tối đa, hãy kết nối Wallet của bạn với nút Bitcoin của riêng bạn thông qua máy chủ Electrum thay vì sử dụng nút công khai





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




### A3. Tài nguyên bổ sung





- Liên kết chính thức:**
 - [Trang web chính thức](https://blockstream.com/)**
 - [Hỗ trợ cho ứng dụng di động](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : tài liệu và trò chuyện
 - [GitHub](https://github.com/Blockstream/green_android)**





- Trình khám phá khối :**
 - on chain: **[Mempool.space](https://Mempool.space/)**
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
