---
name: Blockstream App - Desktop
description: Làm thế nào để sử dụng Hardware Wallet với ứng dụng Blockstream trên máy tính?
---
![cover](assets/cover.webp)



## 1. Giới thiệu



### 1.1 Mục tiêu hướng dẫn





- Hướng dẫn này giải thích cách sử dụng **Ứng dụng Blockstream** trên máy tính để quản lý Bitcoin **onchain** Wallet với **Hardware Wallet**, cho phép ghi lại các giao dịch an toàn trên Blockchain Bitcoin chính.
- Nó bao gồm cài đặt, cấu hình ban đầu, kết nối Hardware Wallet và nhận và gửi bitcoin trên chuỗi.
- Lưu ý: Các hướng dẫn khác trong Phụ lục bao gồm Liquid, Watch-Only và ứng dụng di động.



### 1.2 Đối tượng mục tiêu





- **Người mới bắt đầu**: Người dùng muốn quản lý bitcoin của mình bằng phần mềm máy tính để bàn an toàn và Hardware Wallet.
- **Người dùng trung cấp**: Những người muốn tìm hiểu cách sử dụng Hardware Wallet cho các giao dịch trên chuỗi và các tùy chọn bảo mật như Tor hoặc SPV.



### 1.3. Bối cảnh về ví phần cứng





- **Hardware Wallet**, **Cold Wallet**: Một thiết bị vật lý lưu trữ khóa riêng ngoại tuyến, mang lại mức độ bảo mật cao chống lại các cuộc tấn công mạng, không giống như **ví Hot** (ví phần mềm trên các thiết bị được kết nối).
- Sử dụng được khuyến nghị:
    - Lý tưởng để đảm bảo số tiền lớn hoặc tiết kiệm dài hạn.
    - Phù hợp với người dùng chú trọng bảo mật, muốn bảo vệ tiền của mình khỏi những rủi ro liên quan đến các thiết bị được kết nối.
- **Hạn chế**: Cần có phần mềm như Blockstream App để xem số dư, địa chỉ generate và phát các giao dịch có chữ ký Hardware Wallet.



## 2. Giới thiệu ứng dụng Blockstream





- **Blockstream App** là ứng dụng di động (iOS, Android) và máy tính để bàn dùng để quản lý ví và tài sản Bitcoin trên Liquid Network. Được Blockstream mua lại vào năm 2016, ứng dụng này ban đầu được gọi là *GreenAddress*, sau đó được đổi tên thành *Blockstream Green* (năm 2019) và hiện được gọi là *Blockstream app* (năm 2025).
- **Các tính năng chính**:
- Giao dịch **Onchain** trên Blockchain Bitcoin.
    - Giao dịch trên mạng **Liquid** (Sidechain dành cho giao dịch nhanh chóng, bảo mật).
- Danh mục đầu tư chỉ theo dõi để theo dõi các quỹ mà không cần truy cập vào khóa.
    - Tùy chọn riêng tư: kết nối qua **Tor**, kết nối với **nút cá nhân** qua Electrum hoặc xác minh **SPV** để giảm sự phụ thuộc vào các nút của bên thứ ba.
    - Chức năng **Replace-by-fee (RBF)** giúp tăng tốc các giao dịch chưa được xác nhận.
- **Khả năng tương thích**: Tích hợp ví phần cứng như **Blockstream Jade**.
- **Interface**: Trực quan dành cho người mới bắt đầu, với các tùy chọn nâng cao dành cho chuyên gia.
- **Lưu ý**: Hướng dẫn này tập trung vào việc sử dụng onchain với Hardware Wallet trên phiên bản máy tính để bàn. Các hướng dẫn khác được cung cấp dưới dạng phụ lục sẽ hướng dẫn sử dụng trên ứng dụng di động, cho các tính năng onchain, Liquid và Watch-Only.



## 3. Cài đặt và thiết lập Blockstream App Desktop



### 3.1. tải xuống





- Truy cập [trang web chính thức](https://blockstream.com/app/) và nhấp vào "_Tải xuống ngay_". Tải xuống phiên bản tương ứng với hệ điều hành của bạn (Windows, macOS, Linux).
- **Lưu ý**: Hãy tải xuống từ nguồn chính thức để tránh phần mềm lừa đảo.



### 3.2. cấu hình ban đầu





- **Màn hình chính**: Khi mở lần đầu, ứng dụng sẽ hiển thị màn hình chưa có Wallet được cấu hình. Các danh mục đầu tư đã tạo hoặc nhập sẽ xuất hiện ở đây sau.



![image](assets/fr/02.webp)





- **Tùy chỉnh cài đặt**: Nhấp vào biểu tượng cài đặt ở góc dưới bên trái, điều chỉnh các tùy chọn bên dưới, sau đó thoát khỏi Interface để tiếp tục.



![image](assets/fr/03.webp)



#### 3.2.1. Các thông số chung





- Trong menu Cài đặt, nhấp vào "**Chung**".
- **Chức năng**: Thay đổi ngôn ngữ phần mềm và kích hoạt các chức năng thử nghiệm nếu cần.



![image](assets/fr/04.webp)



#### 3.2.2. Kết nối qua Tor





- Trong menu Cài đặt, nhấp vào "**Mạng**".
- **Chức năng**: Định tuyến lưu lượng mạng qua **Tor**, một mạng ẩn danh mã hóa các kết nối của bạn.
- **Tại sao?**: Ẩn địa chỉ IP Address của bạn và bảo vệ quyền riêng tư của bạn, lý tưởng nếu bạn không tin tưởng vào mạng của mình (ví dụ: Wi-Fi công cộng).
- **Nhược điểm**: Có thể làm chậm ứng dụng do mã hóa.
- **Khuyến nghị**: Kích hoạt Tor nếu tính bảo mật là ưu tiên hàng đầu, nhưng hãy kiểm tra tốc độ kết nối.



![image](assets/fr/05.webp)



#### 3.2.3. Kết nối với một nút cá nhân





- Trong menu Cài đặt, nhấp vào "**Máy chủ tùy chỉnh và xác thực**".
- **Chức năng**: Kết nối ứng dụng với **nút Bitcoin hoàn chỉnh** của bạn thông qua **máy chủ Electrum**.
- **Tại sao?**: Cung cấp khả năng kiểm soát hoàn toàn dữ liệu Blockchain, loại bỏ sự phụ thuộc vào máy chủ Blockstream.
- **Điều kiện tiên quyết**: Một nút Bitcoin đã được cấu hình.
- **Khuyến nghị**: Người dùng nâng cao muốn có quyền tối đa.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Xác minh SPV





- Trong menu Cài đặt, nhấp vào "**Máy chủ tùy chỉnh và xác thực**".
- **Chức năng**: Sử dụng **Xác minh thanh toán đơn giản (SPV)** để tải xuống tiêu đề khối và xác minh giao dịch của bạn bằng bằng chứng bao gồm (Merkle), mà không cần lưu trữ toàn bộ Blockchain.
- **Tại sao?**: Giảm sự phụ thuộc vào nút mặc định của Blockstream, đồng thời vẫn nhẹ cho các thiết bị.
- **Nhược điểm**: Ít an toàn hơn Full node vì nó phụ thuộc vào các nút của bên thứ ba để lấy một số thông tin.
- **Khuyến nghị**: Kích hoạt SPV nếu bạn không thể sử dụng nút cá nhân nhưng muốn sử dụng Full node để có bảo mật tối ưu.



![image](assets/fr/07.webp)



## 4. Kết nối Hardware Wallet với ứng dụng Blockstream



### 4.1. Những cân nhắc sơ bộ



#### 4.1.1. Dành cho người dùng Ledger





- Blockstream Green chỉ hỗ trợ ứng dụng **Bitcoin Legacy** trên các thiết bị Ledger (Nano S, Nano X).
- Các bước cần thực hiện trong **Ledger Live** trước khi kết nối thiết bị của bạn:


1. Vào **"Cài đặt"** → **"Tính năng thử nghiệm"** và kích hoạt **chế độ nhà phát triển**.


2. Vào **"My Ledger"** → **"App Catalogue "**, sau đó cài đặt ứng dụng **Bitcoin Legacy**


3. Mở ứng dụng **Bitcoin Legacy** trên Ledger trước khi khởi chạy Blockstream Green để thiết lập kết nối.




- **Lưu ý**: Đảm bảo Ledger của bạn được mở khóa bằng mã PIN và ứng dụng Bitcoin Legacy đang hoạt động khi bạn kết nối.



#### 4.1.2 Khởi tạo Hardware Wallet





- Nếu Hardware Wallet (Ledger, Trezor hoặc Blockstream Jade) của bạn chưa từng được sử dụng (dù với Blockstream Green hay các phần mềm khác như Ledger Live), trước tiên bạn cần khởi tạo nó. Bước này bao gồm, trong một môi trường an toàn, không có camera hoặc người giám sát:


1. **Tạo cụm từ seed / Cụm từ Mnemonic** (12, 18 hoặc 24 từ): Viết cẩn thận ra một tờ giấy.


2. **Xác minh cụm từ seed**: Kiểm tra việc nhập Wallet từ các từ đã ghi chú, ví dụ: bằng cách xác minh khóa công khai mở rộng. Cần thực hiện trước khi gửi tiền đến Wallet và bảo mật cụm từ seed vĩnh viễn.


3. **Bảo mật cụm từ seed**: Lưu trữ cụm từ trên một phương tiện vật lý (giấy hoặc kim loại) và ở nơi an toàn. Tuyệt đối không lưu trữ dưới dạng kỹ thuật số (không lưu trữ ảnh chụp màn hình, đám mây hoặc email).




- **Quan trọng**: Cụm từ seed là cách duy nhất để bạn lấy lại tiền nếu thiết bị bị mất hoặc trục trặc. Bất kỳ ai có quyền truy cập đều có thể đánh cắp bitcoin của bạn.
- **Tài nguyên** để sao lưu và kiểm tra câu seed:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Cấu hình cho hướng dẫn này:





- Chúng ta sẽ giả định rằng Hardware Wallet đã được khởi tạo bằng cụm từ seed và mã PIN khóa.
- Chúng tôi giả định rằng Hardware Wallet chưa bao giờ được kết nối với Ứng dụng Blockstream, yêu cầu tạo tài khoản mới. Nếu Hardware Wallet đã được sử dụng với Ứng dụng Blockstream, tài khoản sẽ tự động xuất hiện khi mở ứng dụng.



### 4.2. Bắt đầu kết nối





- Từ màn hình chính, nhấp vào "**Thiết lập Wallet mới**", sau đó xác nhận các điều khoản và điều kiện và nhấp vào "**Bắt đầu**":



![image](assets/fr/08.webp)





- Chọn tùy chọn "**Trên Hardware Wallet**":



![image](assets/fr/09.webp)





- Nếu bạn đang sử dụng **Blockstream Jade**, hãy nhấp vào nút tương ứng. Nếu không, hãy chọn "**Kết nối một thiết bị phần cứng khác**":



![image](assets/fr/10.webp)





- Kết nối Hardware Wallet của bạn với máy tính qua USB và chọn nó trong Ứng dụng Blockstream:



![image](assets/fr/22.webp)





- Vui lòng đợi trong khi ứng dụng Blockstream nhập thông tin danh mục đầu tư của bạn:



![image](assets/fr/23.webp)



### 4.3. Tạo tài khoản





- Nếu Hardware Wallet của bạn đã được sử dụng với ứng dụng Blockstream, tài khoản của bạn sẽ tự động xuất hiện trong Interface sau khi nhập. Nếu không, hãy tạo tài khoản bằng cách nhấp vào "**Tạo Tài khoản**":



![image](assets/fr/24.webp)





- Chọn "**Tiêu chuẩn**" để cấu hình danh mục đầu tư Bitcoin cổ điển:



![image](assets/fr/25.webp)





- Sau khi tài khoản của bạn được tạo, bạn có thể truy cập danh mục đầu tư Interface chính của mình:



![image](assets/fr/26.webp)





## 5. Sử dụng Wallet trên chuỗi với Hardware Wallet



### 5.1. Nhận bitcoin





- Từ màn hình danh mục đầu tư chính, nhấp vào "**Nhận**":



![image](assets/fr/27.webp)





- Ứng dụng sẽ hiển thị **mã Address trống**. Sử dụng mã Address mới cho mỗi lần nhận sẽ cải thiện tính bảo mật của bạn. Nhấp vào "**Sao chép Address**" để sao chép mã Address, hoặc để người gửi quét mã QR được hiển thị:



![image](assets/fr/12.webp)



**Tùy chọn** :




- (1) Nhấp vào mũi tên để generate tạo Address mới liên kết với danh mục đầu tư của bạn.
- (2) Để yêu cầu một số tiền cụ thể, hãy nhấp vào "**Tùy chọn khác**" rồi nhấp vào "**Yêu cầu số tiền**". Mã QR sẽ được cập nhật và Address sẽ được thay thế bằng URI thanh toán Bitcoin, chẳng hạn như: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Để sử dụng lại Address trước đó, hãy nhấp vào "**Thêm tùy chọn**" rồi nhấp vào "**Danh sách địa chỉ**":



![image](assets/fr/14.webp)





- **Xác minh**: Kiểm tra cẩn thận Address được chia sẻ để tránh lỗi hoặc tấn công (ví dụ: phần mềm độc hại sửa đổi bảng tạm).
- Sau khi giao dịch được phát trên mạng, nó sẽ xuất hiện trong Wallet của bạn. Hãy chờ từ 1 đến 6 xác nhận để xem giao dịch là không thể thay đổi.



![image](assets/fr/28.webp)



### 5.2. gửi bitcoin





- Từ màn hình danh mục đầu tư chính, nhấp vào "**Gửi**".



![image](assets/fr/29.webp)





- Nhập thông tin chi tiết:
    - (1) Kiểm tra xem tài sản được chọn có phải là **Bitcoin** (trên chuỗi) không.
    - (2) Nhập **Address của người nhận** bằng cách dán hoặc quét mã QR bằng webcam của bạn.
    - (3) Chỉ định **số tiền** cần gửi (bằng BTC, satoshi hoặc đơn vị khác).




![image](assets/fr/16.webp)





- Chọn **phí giao dịch** (tùy chọn):
 - Chọn từ các tùy chọn được đề xuất (nhanh, trung bình, chậm) theo mức độ khẩn cấp, kèm theo thời gian xác nhận ước tính.
 - Để tùy chỉnh mức phí, hãy điều chỉnh thủ công số satoshi trên mỗi vbyte. Số satoshi này được hiển thị trên màn hình chính. Xem thêm [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- Lựa chọn thủ công UTXO (tùy chọn): Nhấp vào "**Lựa chọn Coin thủ công**" để chọn UTXO cụ thể sẽ được sử dụng trong giao dịch.



![image](assets/fr/18.webp)





- **Xác minh sơ bộ**: Kiểm tra Address, số tiền và phí trên màn hình tóm tắt, sau đó nhấp vào "**Xác nhận giao dịch**". Trên thực tế, giao dịch sẽ không được chuyển vào mạng cho đến khi bạn ký nó bằng Hardware Wallet, vốn là thiết bị duy nhất có khóa bí mật liên kết với các địa chỉ mà UTXO (satoshi) sẽ được trừ vào.



![image](assets/fr/19.webp)





- **Kiểm tra lần cuối và ký tên**: Đảm bảo tất cả các thông số giao dịch trên màn hình Hardware Wallet của bạn đều chính xác, sau đó ký giao dịch bằng màn hình này. Lỗi Address có thể dẫn đến mất tiền không thể phục hồi.





- **Phát sóng**: Sau khi ký, ứng dụng Blockstream sẽ tự động phát sóng giao dịch trên mạng Bitcoin.



![image](assets/fr/20.webp)





- **Theo dõi**:
 - Giao dịch sẽ hiển thị trên màn hình chính của Wallet ở trạng thái "đang chờ xử lý" cho đến khi được xác nhận.
 - Miễn là giao dịch chưa được xác nhận, chức năng **Replace-by-fee (RBF)** có thể được sử dụng để tăng tốc độ xác nhận bằng cách tăng phí (xem Phụ lục).



![image](assets/fr/21.webp)



## Phụ lục



### A1. Các hướng dẫn khác về Blockstream





- Sử dụng Liquid Network:



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Nhập và theo dõi danh mục đầu tư trong "Chỉ xem":



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Sử dụng ứng dụng Blockstream trên điện thoại di động (Hot Wallet):



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Giải thích về Replace-by-fee (RBF)





- **Định nghĩa**: Replace-by-fee (RBF) là một tính năng của mạng Bitcoin cho phép người gửi đẩy nhanh quá trình xác nhận giao dịch **trên chuỗi** bằng cách tăng phí.
- **Giới hạn**:
    - RBF không khả dụng cho giao dịch Liquid hoặc Lightning.
    - Giao dịch ban đầu phải được đánh dấu là tương thích với RBF, ứng dụng Blockstream sẽ tự động thực hiện điều này.
- Để biết thêm thông tin, hãy xem [thuật ngữ của chúng tôi](https://planb.network/resources/glossary/RBF-replacebyfee).



### A3. Thực hành tốt nhất





- **Bảo mật cụm từ khôi phục của bạn**:
    - Lưu cụm từ Mnemonic của Hardware Wallet trên một vật chứa (giấy, kim loại) ở nơi an toàn.
    - Không bao giờ lưu trữ dưới dạng kỹ thuật số (đám mây, email, ảnh chụp màn hình).
    - Hướng dẫn: Lưu cụm từ Mnemonic của bạn:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Bảo vệ quyền riêng tư của bạn**:





    - generate và Address mới cho mỗi lần tiếp nhận trực tuyến.
    - Kích hoạt **Tor** hoặc **SPV** để hạn chế theo dõi.
    - Kết nối với nút Bitcoin của bạn thông qua Electrum để có quyền quản lý tối đa.
- **Luôn kiểm tra địa chỉ giao hàng**:





    - Kiểm tra Address trên màn hình Hardware Wallet của bạn trước khi ký.
    - Sử dụng chức năng sao chép/dán hoặc mã QR để tránh lỗi thủ công.
- **Tối ưu hóa chi phí**:





    - Điều chỉnh mức phí theo mức độ khẩn cấp và tắc nghẽn mạng (xem [Mempool.space](https://Mempool.space/)).
    - Sử dụng Liquid hoặc Lightning để thực hiện các giao dịch nhanh chóng, chi phí thấp và không yêu cầu bảo mật trên chuỗi.
- **Cập nhật phần mềm**:





    - Luôn cập nhật ứng dụng Blockstream và chương trình cơ sở Hardware Wallet của bạn với các tính năng và bản vá bảo mật mới nhất.



### A4. Tài nguyên bổ sung





- **Liên kết chính thức**:
    - [Trang web chính thức](https://blockstream.com/)
    - [Hỗ trợ cho ứng dụng Blockstream](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): tài liệu và trò chuyện
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Trình khám phá khối**:
    - Onchain: [Mempool.space](https://Mempool.space/)
    - Liquid : [Thông tin về dòng khối](https://blockstream.info/Liquid)
    - Sét: [1ML (Lightning Network)](https://1ml.com/)





- **Bảo mật cụm từ khôi phục của bạn:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Thuật ngữ](https://planb.network/fr/resources/glossary/Liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Thuật ngữ](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb