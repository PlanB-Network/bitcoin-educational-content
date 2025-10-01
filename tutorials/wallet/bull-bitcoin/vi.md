---
name: Bull Bitcoin Wallet
description: Tìm hiểu cách sử dụng Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Hướng dẫn này sẽ hướng dẫn bạn cài đặt, cấu hình và sử dụng Bull Bitcoin Mobile. Bạn sẽ học cách nhận và gửi tiền trên ba mạng lưới: onchain, Liquid và Lightning, cũng như cách chuyển Bitcoin từ mạng lưới này sang mạng lưới khác. Phần phụ lục cung cấp tài nguyên và thông tin liên hệ, thông tin cơ bản và giải thích ngắn gọn về các khái niệm kỹ thuật.



## Giới thiệu



**Bull Bitcoin Mobile**, được phát triển bởi **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([tạo tài khoản](https://app.bullbitcoin.com/registration/orangepeel)), là một Bitcoin Wallet **tự quản**, nghĩa là bạn có toàn quyền kiểm soát khóa riêng tư và do đó là tiền của mình mà không cần phụ thuộc vào bên thứ ba. Là mã nguồn mở và dựa trên triết lý Cypherpunk, Wallet này kết hợp sự đơn giản, tính bảo mật và các tính năng tiên tiến như hoán đổi chéo mạng và hỗ trợ PayJoin. Nó cho phép bạn quản lý bitcoin của mình trên ba mạng: **Bitcoin onchain**, **Liquid** và **Lightning**, mỗi mạng được thiết kế riêng cho các mục đích sử dụng cụ thể.



### Bối cảnh phát triển



Wallet giải quyết một thách thức lớn: Phí mạng Bitcoin không phù hợp cho các khoản thanh toán nhỏ hoặc mở các kênh Lightning tự lưu trữ quy mô nhỏ. Wallet Bull Bitcoin Mobile cung cấp giải pháp tự quản lý dựa trên 3 mạng Bitcoin chính:





- **Mạng Bitcoin (trên chuỗi)**: Lý tưởng để lưu trữ UTXO và các giao dịch có giá trị lớn trong thời gian trung và dài hạn, trong đó phí không đáng kể.
- **Liquid Network**: Được thiết kế để thực hiện giao dịch nhanh chóng (~2 phút), bảo mật hơn (số tiền ẩn), chi phí thấp, hoàn hảo để tích lũy số tiền nhỏ hoặc bảo vệ quyền riêng tư của bạn.
- **Mạng Lightning**: Được tối ưu hóa cho các khoản thanh toán tức thời, chi phí thấp, phù hợp với các giao dịch hàng ngày có giá trị từ nhỏ đến trung bình.



Ví dụ, với Bull Bitcoin Mobile, bạn có thể tích lũy số tiền nhỏ trong danh mục đầu tư **Liquid** hoặc **Lightning** và sau đó, khi đã đạt được số tiền đáng kể, bạn có thể:





- Chuyển sang mạng lưới onchain để lưu trữ trung hạn hoặc dài hạn an toàn, có tính bảo mật được cải thiện với Liquid và/hoặc Lightning upstream, và với phí onchain cho một giao dịch duy nhất



### Tiến hóa liên tục



Wallet liên tục phát triển, vì vậy đừng ngạc nhiên nếu bạn thấy có sự khác biệt giữa hướng dẫn này và ứng dụng mới nhất của bạn.




- Ví dụ: kể từ ngày 19/07/2025, các nút **"Mua / Bán / Thanh toán"** vẫn hiển thị nhưng bị mờ đi trong ứng dụng, vì các tùy chọn này, có sẵn trên Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel), sẽ sớm được tích hợp để tạo nên một trải nghiệm thống nhất. Việc sử dụng chúng vẫn hoàn toàn tùy chọn. Nhiều cải tiến khác đang được tiến hành hoặc lên kế hoạch: quản lý đa Wallet, passphrase, khả năng tương thích với ví phần cứng...
- Trên [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), bạn có thể xem các chủ đề hiện tại và những phát triển sắp tới. Vì dự án hoàn toàn mã nguồn mở và được "xây dựng công khai", bạn cũng có thể gửi cho chúng tôi các đề xuất và bất kỳ lỗi nào bạn gặp phải.




## 1. Điều kiện tiên quyết



Trước khi bắt đầu sử dụng **Bull Bitcoin Mobile**, hãy đảm bảo bạn có những vật dụng sau:





- **Điện thoại thông minh tương thích**: Thiết bị **iOS** (iPhone hoặc iPad) hoặc **Android**
- Kết nối Internet
- **Phương tiện sao lưu an toàn**: Viết **cụm từ khôi phục** (12 từ) ra giấy hoặc kim loại và cất giữ ở nơi an toàn.
- **Kiến thức cơ bản**: Cần hiểu biết tối thiểu về các khái niệm Bitcoin (địa chỉ, giao dịch, phí), mặc dù hướng dẫn này giải thích từng bước cho người mới bắt đầu.



## 2. Cài đặt





- **Tải ứng dụng**:
- [Cửa hàng Google Play](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share) **Tải xuống từ cửa hàng ứng dụng cho thiết bị Android**
- [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) **Tải xuống APK trực tiếp cho thiết bị Android**
- [iOS](https://testflight.apple.com/join/FJbE4JPN) **Tải xuống qua TestFlight cho các thiết bị Apple**
 - Kiểm tra tên nhà phát triển (Bull Bitcoin) để tránh các ứng dụng gian lận.
 - Đảm bảo rằng phiên bản đã tải xuống tương ứng với phiên bản ổn định mới nhất được chỉ định trên GitHub.
 - Bull Bitcoin Mobile là **mã nguồn mở**. Để xem mã: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Cài đặt ứng dụng




## 3. Cấu hình ban đầu



### 3.1 Khởi chạy ứng dụng:



Ứng dụng sử dụng cụm từ khôi phục 12 từ duy nhất cho cả hai danh mục đầu tư:




- **Bitcoin Wallet** an toàn: Dành cho các giao dịch trên mạng Bitcoin (trên chuỗi)
- **Wallet** của Instant Payments: Dành cho các giao dịch tức thì trên mạng Liquid và Lightning



Khi mở, bạn sẽ được nhắc nhập cụm từ khôi phục hiện có hoặc tạo Wallet mới:



![image](assets/fr/02.webp)



### 3.2 Cụm từ phục hồi:



Nếu bạn muốn sử dụng lại Wallet hiện có, hãy nhấp vào "**Khôi phục Wallet**" và điền 12 từ trong cụm từ khôi phục của bạn.



Nếu không, hãy nhấp vào "**Tạo Wallet mới**":




- Hãy ghi lại cụm từ khôi phục của bạn thật cẩn thận. Viết nó ra giấy hoặc kim loại và cất giữ ở nơi an toàn (két sắt, nơi lưu trữ ngoại tuyến). Cụm từ này là cách duy nhất để bạn truy cập bitcoin của mình trong trường hợp thiết bị bị mất hoặc ứng dụng bị xóa.
- Điều quan trọng cần lưu ý là bất kỳ ai có cụm từ này đều có thể đánh cắp toàn bộ bitcoin của bạn. Tuyệt đối không lưu trữ dưới dạng kỹ thuật số:
 - Không có ảnh chụp màn hình
 - Không có bản sao lưu đám mây, email hoặc tin nhắn
 - Không sao chép/dán (nguy cơ lưu vào bảng tạm)



**! Điểm này rất quan trọng**. Để được hỗ trợ thêm:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Bảo mật quyền truy cập:





- Vào cài đặt rồi nhấp vào **Mã PIN**.
- Thiết lập mã PIN mạnh mẽ để bảo vệ quyền truy cập vào ứng dụng.
- Bước này là tùy chọn, nhưng được khuyến nghị mạnh mẽ để ngăn chặn bất kỳ ai có quyền truy cập vào điện thoại của bạn có thể truy cập vào Wallet.



![image](assets/fr/03.webp)



### 3.4 Kết nối với nút cá nhân (tùy chọn):



Wallet BullBitcoin kết nối với máy chủ Electrum theo mặc định: máy chủ đầu tiên do Bull Bitcoin quản lý và máy chủ thứ cấp từ Blockstream, cả hai đều được coi là không lưu giữ nhật ký, giúp giảm nguy cơ bị theo dõi.



Để bảo mật hơn, bạn có thể kết nối ứng dụng với nút Bitcoin của riêng mình thông qua máy chủ Electrum (hướng dẫn có sẵn trên [GitHub của BullBitcoin](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Nhận tiền



Việc nhận tiền bằng **Bull Bitcoin Mobile** rất đơn giản và phù hợp với nhu cầu của bạn, cho dù bạn sử dụng:




  - mạng lưới **Bitcoin (trên chuỗi)** để bảo tồn lâu dài,
  - mạng **Liquid** cho Confidential Transactions nhanh hơn,
  - mạng lưới **Lightning** cho các khoản thanh toán tức thời, giá trị thấp.



Ứng dụng sẽ tự động tạo địa chỉ thu sóng Lightning hoặc địa chỉ Invoice, tùy thuộc vào mạng được chọn. Sau đây là cách thực hiện cho từng mạng.



### 4.1. onchain (mạng Bitcoin)



Trên màn hình chính, bạn có thể:




- hoặc chọn **Secure Bitcoin Wallet** sau đó nhấp vào "**Receive "** :



![image](assets/fr/04.webp)





- hoặc nhấp vào "**Nhận "**, sau đó chọn mạng **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Tùy chọn "Chỉ sao chép hoặc quét Address" đã bị vô hiệu hóa (mặc định)



![image](assets/fr/06.webp)





- Điều này cho phép truy cập vào các tham số nâng cao tùy chọn. Bạn có thể chỉ định:
 - Một **số tiền** bằng BTC, Sats hoặc tiền pháp định.
 - **Ghi chú cá nhân** sẽ được đính kèm trong bản sao của URI/Mã QR.
 - Kích hoạt **PayJoin** (xem Phụ lục 3 để biết chi tiết), giúp cải thiện tính bảo mật bằng cách kết hợp các mục nhập của người gửi và người nhận.





- Ví dụ về URI được tạo tự động:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- **Cách sử dụng**: Sao chép URI để chia sẻ với người gửi hoặc để họ quét mã QR.



#### 4.1.2. Tùy chọn "Chỉ sao chép hoặc quét Address" được bật



![image](assets/fr/07.webp)





- Khi bật tùy chọn **"Chỉ sao chép hoặc quét Address"**, ứng dụng sẽ tạo ra một Bitcoin Address đơn giản theo định dạng SegWit (bech32).





- Ví dụ:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Ngay cả khi bạn nhập số tiền hoặc ghi chú, chúng sẽ không được đưa vào mã QR hoặc bản sao của Address





- **Cách sử dụng**: Sao chép Address để chia sẻ với người gửi hoặc để họ quét mã QR.



#### 4.1.3. Tạo Address mới





- Tại sao lại sử dụng mã Address mới cho mỗi giao dịch? Mã này **bảo vệ quyền riêng tư của bạn** bằng cách ngăn chặn nhiều khoản thanh toán được liên kết đến cùng một mã Address và hạn chế khả năng theo dõi trên mã Blockchain.
- Theo mặc định, Bull Bitcoin sẽ tự động tạo ra một Address chưa sử dụng.
 - Bạn có thể buộc tạo Address mới bằng cách nhấp vào **"Address mới"** ở cuối màn hình.
 - Tất cả các địa chỉ của bạn đều được liên kết với cụm từ seed: bất kể bạn sử dụng bao nhiêu địa chỉ, danh mục đầu tư của bạn sẽ hiển thị một số dư duy nhất và có thể tự động hợp nhất tiền khi giao dịch được thực hiện.





- Mẹo: Luôn sử dụng **Address** mới do Bull Bitcoin cung cấp, trừ khi bạn có nhu cầu cụ thể (ví dụ: Address công cộng để nhận tiền quyên góp).



### 4.2. Liquid



Trên màn hình chính, bạn có thể:




- hoặc chọn **Thanh toán tức thì Wallet** sau đó nhấp vào **"Nhận"** sau đó **"Liquid"** :



![image](assets/fr/08.webp)





- hoặc nhấp vào "**Nhận "**, sau đó chọn mạng **Liquid**:



![image](assets/fr/09.webp)



Khi bạn ở trên màn hình **"Nhận"**, hãy sao chép Liquid Address:





- Không có số tiền hoặc ghi chú. Ví dụ:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Hoặc bằng cách chỉ định **số tiền** (bằng BTC, Sats hoặc tiền pháp định) và/hoặc **ghi chú cá nhân** để đưa vào bản sao của URI/Mã QR. Ví dụ:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Cách sử dụng**: Sao chép Address/URI để chia sẻ với người gửi hoặc để họ quét mã QR.



### 4.3. Sét



Trên màn hình chính, bạn có thể:




- hoặc chọn **Thanh toán tức thì Wallet** sau đó nhấp vào "**Nhận"** :



![image](assets/fr/10.webp)





- hoặc nhấp vào "**Nhận "**, sau đó chọn mạng **Lightning**:



![image](assets/fr/11.webp)



#### 4.3.1. Hoạt động, giới hạn và lợi ích





- **Cơ chế**: Bull Bitcoin Wallet là Wallet cho phép thực hiện và nhận thanh toán qua Lightning. Tiền nhận được qua Lightning được lưu trữ trên mạng **Liquid** (trong Wallet Instant Payments) nhờ tính năng hoán đổi tự động qua **Boltz**. Điều này cho phép bạn tương tác với Lightning mà không cần phải quản lý các kênh thanh khoản, đồng thời vẫn tự quản lý.





- **Giới hạn:**
- Số tiền tối thiểu **là 100 satoshi** (tính đến ngày 19/07/2025) khi bạn generate Invoice.
- Bạn trả phí, số tiền này sẽ được khấu trừ vào số tiền người gửi gửi, không giống như khi nhận bằng Wallet Lightning native, khi đó người gửi chỉ phải trả phí chuyển tiền ngoài số tiền đã gửi. Tính đến ngày 19/07/2025, 47 Sats đã được khấu trừ vào số tiền đã gửi.





- **Những lợi ích**:
- **Tự quản lý**: Tiền của bạn vẫn nằm trong tầm kiểm soát của bạn và được lưu trữ trên Liquid Network.
- **Không có phí onchain cao**: Lưu trữ trên Liquid giúp bạn tránh được chi phí nạp onchain tốn kém để mở kênh Lightning hoặc bổ sung thanh khoản. Các thao tác này có thể được thực hiện sau, khi số tiền tích lũy trên Liquid đủ bù đắp chi phí.





- **Mẹo:** Nếu người gửi có Wallet Bull Bitcoin, hãy sử dụng trực tiếp Liquid Network để tránh phí hoán đổi



#### 4.3.2. generate Invoice





- Nhập **số tiền** (bằng BTC, Sats hoặc tiền pháp định)





- Thêm **ghi chú cá nhân** sẽ được tích hợp vào Invoice. Nếu người gửi thanh toán bằng Invoice, Wallet của bạn cũng sẽ bao gồm ghi chú này trong chi tiết giao dịch.





- **Hiệu lực của Invoice:** Thẻ Lightning Invoice có hiệu lực trong **12 giờ**. Sau thời gian này, thẻ sẽ hết hạn và không thể thanh toán được nữa. Bạn phải tạo thẻ Invoice mới.





- **Cách sử dụng**: Sao chép Invoice để chia sẻ với người gửi hoặc để họ quét mã QR.




## 5. Gửi tiền



### 5.1. Nguyên lý cơ bản



Từ trang chủ hoặc từ ví:



![image](assets/fr/12.webp)



để truy cập vào màn hình gửi:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** giúp việc gửi tiền trở nên dễ dàng bằng cách tự động phát hiện mạng (Bitcoin, Liquid hoặc Lightning) dựa trên Address hoặc Invoice đã nhập (sao chép hoặc quét qua mã QR).



### 5.2. truyền dẫn trên chuỗi (mạng Bitcoin)



#### 5.2.1. Gửi màn hình



**Hành động**: Nhập hoặc quét Bitcoin trên chuỗi Address





- Nếu số tiền chưa được xác định, ví dụ:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Sau đó bạn có thể chọn trên màn hình gửi:
 - Số tiền tính bằng BTC, satoshi hoặc fiat. Số tiền tối thiểu: 546 satoshi vào ngày 22/07/2025.
 - Ghi chú tùy chọn để xác định giao dịch. Chỉ bạn mới thấy được trong phần chi tiết giao dịch.



![image](assets/fr/14.webp)





- Nếu số tiền đã được xác định, ví dụ:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Sau đó, bạn sẽ được đưa trực tiếp đến màn hình xác nhận bên dưới.



#### 5.2.2 Màn hình xác nhận



Hãy dành thời gian kiểm tra tất cả các thông số, đặc biệt là số tiền, điểm đến Address và phí.


Sau đó, bạn có thể điều chỉnh các thông số:



![image](assets/fr/15.webp)




- **Phí**: Bạn có thể chọn:
- **Tốc độ thực hiện** của giao dịch của bạn và các khoản phí liên quan sẽ được ước tính
- **Phí** ở chế độ Phí tuyệt đối (tổng phí tính bằng satoshi) hoặc Phí tương đối (phí cho mỗi byte) và tốc độ giao dịch của bạn sẽ được ước tính





- **Cài đặt nâng cao**:





- **Replace-by-fee (RBF)**: Được kích hoạt theo mặc định, chức năng này tăng tốc giao dịch bằng cách trả phí cao hơn (xem Phụ lục 4 để biết chi tiết).





- Chọn thủ công **UTXO**: Nếu tiền của bạn được lưu trữ tại nhiều địa chỉ Wallet khác nhau, bạn có thể chọn địa chỉ để gửi tiền. Tại sao bạn nên làm điều này? Với việc Bitcoin ngày càng được sử dụng rộng rãi, phí chuyển tiền đang tăng lên. Gửi tiền từ nhiều địa chỉ với số tiền nhỏ sẽ tốn kém hơn so với gửi từ một địa chỉ Address, nhưng việc thực hiện ngay bây giờ sẽ giúp bạn tránh phải thực hiện sau này, khi phí sẽ còn cao hơn nữa. Điều này được gọi là **hợp nhất UTXO**.



![image](assets/fr/16.webp)





- **Gửi với PayJoin**: Nếu chức năng đã được kích hoạt bởi người nhận cung cấp URI, ví dụ:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Sau đó, Bull Bitcoin Mobile sẽ cấu hình việc gửi bằng cách kết hợp UTXO của bạn với UTXO của người nhận làm đầu vào, cải thiện tính bảo mật (xem Phụ lục 3 để biết chi tiết).



### 5.3. Gửi đến Liquid



#### 5.3.1 Gửi màn hình



Mạng lưới **Liquid** cho phép giao dịch nhanh chóng (khoảng 2 phút nhờ một khối mỗi phút), bảo mật hơn (số tiền được che giấu) so với mạng lưới onchain, và với mức phí rất thấp. Tiền được rút từ **Thanh toán tức thì Wallet**.



**Hành động**: Nhập hoặc quét Liquid Address





- Nếu số tiền chưa được xác định, ví dụ:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Sau đó bạn có thể chọn trên màn hình gửi:




- Số tiền bằng BTC, sat hoặc fiat. Không có mức tối thiểu, có thể là 1 Satoshi;
- Ghi chú tùy chọn để xác định giao dịch. Chỉ bạn mới thấy được trong phần chi tiết giao dịch.



![image](assets/fr/17.webp)





- Nếu số tiền đã được xác định, ví dụ:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Sau đó, bạn sẽ được đưa trực tiếp đến màn hình xác nhận bên dưới.



#### 5.3.2 Màn hình xác nhận



Hãy dành thời gian kiểm tra tất cả các thông số, đặc biệt là số lượng và đích đến Address.



![image](assets/fr/18.webp)





- **Phí**: Tỷ lệ thuận với độ phức tạp của giao dịch, thường là 0,1 sat/vB, tức là 20-40 satoshi cho một giao dịch đơn giản (33 Sats vào ngày 22/07/2025).



### 5.4. Gửi đến Lightning



#### 5.4.1 Gửi màn hình



Mạng **Lightning** cho phép thanh toán tức thời, chi phí thấp cho các khoản tiền nhỏ, lý tưởng cho các giao dịch nhỏ hàng ngày.



**Hành động**: Nhập hoặc quét Lightning Invoice





- Nếu bạn quét LN-URL Address cho phép bạn thiết lập số lượng


Ví dụ: `orangepeel@walletofsatoshi.com`.


sau đó bạn có thể chọn trên màn hình gửi:




 - Số tiền bằng BTC, sat hoặc fiat. Số tiền tối thiểu là 1000 satoshi vào ngày 23/07/2025
 - Ghi chú tùy chọn để xác định giao dịch. Ghi chú này sẽ được gửi đến người nhận.



![image](assets/fr/19.webp)





- Nếu bạn quét Lightning Invoice có chứa một lượng xác định


Ví dụ:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Sau đó, bạn sẽ được đưa trực tiếp đến màn hình xác nhận bên dưới.



Lưu ý: số tiền phải lớn hơn 21 Sats vào ngày 23/07/2025



#### 5.4.2 Hoạt động, giới hạn và lợi ích





- **Cơ chế**: Tiền được rút từ **Thanh toán tức thì Wallet** (Liquid) và được chuyển đổi thông qua giao dịch hoán đổi **Liquid → Lightning** với **Boltz**.





- **Giới hạn:**
- Số tiền tối thiểu cao hơn **Wallet Lightning native** (xem ở trên)
- **Chi phí** cộng với Liquid → Trao đổi sét qua Boltz





- **Những lợi ích**:
- **Tự quản lý**: Tiền của bạn vẫn nằm trong tầm kiểm soát của bạn, được lưu trữ trên Liquid Network và có thể chuyển qua Lightning nếu cần
- **Không có phí onchain cao**: Lưu trữ trên Liquid giúp bạn tiết kiệm chi phí nạp onchain để mở kênh Lightning hoặc bổ sung thanh khoản. Các thao tác này có thể được thực hiện sau, khi số tiền tích lũy trên Liquid đủ bù đắp chi phí.





- **Mẹo:** Nếu người nhận có Wallet Bull Bitcoin, hãy sử dụng trực tiếp Liquid Network để tránh chi phí hoán đổi



#### 5.3.3 Màn hình xác nhận



Hãy dành thời gian kiểm tra tất cả các thông số, đặc biệt là số lượng và đích đến Address.



![image](assets/fr/20.webp)




## 6. Xem lịch sử



**Bull Bitcoin Mobile** giúp bạn dễ dàng theo dõi các giao dịch trên mạng lưới **Bitcoin (onchain)**, **Liquid** và **Lightning**. Lịch sử giao dịch có thể được truy cập theo hai cách và hiển thị thông tin chi tiết cho từng loại giao dịch. Bạn cũng có thể kiểm tra giao dịch của mình bằng trình duyệt khối bên ngoài.



### 6.1. Lịch sử truy cập





- Qua màn hình chính:
 - Nhấp vào **Secure Bitcoin Wallet** để xem các giao dịch **trên chuỗi** hoặc vào **Instant Payments Wallet** cho các giao dịch **Liquid** và **Lightning**.
 - Lịch sử được hiển thị ngay bên dưới tổng danh mục đầu tư, được lọc theo loại Wallet đã chọn.



![image](assets/fr/21.webp)





- Thông qua trang chuyên dụng:
 - Trên màn hình chính, nhấp vào **biểu tượng lịch sử** (biểu tượng đồng hồ hoặc biểu tượng tương tự).
 - Truy cập trang liệt kê tất cả các giao dịch, với bộ lọc theo loại hành động: **Gửi**, **Nhận**, **Hoán đổi**, **PayJoin**, **Bán**, **Mua** (lưu ý: Bán và Mua đang được phát triển và không khả dụng tại thời điểm này, ngày 20 tháng 7 năm 2025).



![image](assets/fr/22.webp)



### 6.2. Chi tiết giao dịch



Mỗi giao dịch hiển thị thông tin cụ thể tùy thuộc vào mạng lưới và loại hành động (gửi hoặc nhận). Dưới đây là thông tin chi tiết về **giao dịch trên chuỗi**:



![image](assets/fr/23.webp)



### 6.3. Kiểm tra thông qua Block explorer



Danh sách các trình khám phá cho mạng **Bitcoin onchain**, **Liquid** và **Lightning** có trong Phụ lục 4.



Đối với **Lightning**, giao dịch không hiển thị trên trình duyệt công cộng. Vui lòng kiểm tra chi tiết (bao gồm cả ID Swap cho Boltz) trong ứng dụng.




## 7. Cài đặt



Có thể truy cập trang "Cài đặt" trực tiếp từ trang chủ ứng dụng Bull Bitcoin và được sử dụng để cấu hình và quản lý nhiều khía cạnh khác nhau của danh mục đầu tư và trải nghiệm người dùng.



![image](assets/fr/24.webp)





- **Wallet Sao lưu**: Hiển thị cụm từ khôi phục của danh mục đầu tư để sao lưu an toàn. Xem phần 3 về tạo danh mục đầu tư để biết các phương pháp hay nhất trong việc quản lý và lưu trữ cụm từ khôi phục.





- Chi tiết **Wallet**:
- **Pubkey**: Khóa công khai liên kết với Wallet, được sử dụng cho địa chỉ tiếp nhận generate Bitcoin.
- **Đường dẫn phái sinh**: Đường dẫn phái sinh được sử dụng để lấy địa chỉ generate Wallet từ khóa riêng.





- **Electrum Server (Nút Bitcoin)**: Thiết lập kết nối tới nút Bitcoin tùy chỉnh cho các giao dịch trên chuỗi.





- **Mã PIN**: Kích hoạt và/hoặc sửa đổi mã bảo mật để bảo vệ quyền truy cập vào ứng dụng và các chức năng của Wallet.





- **Tiền tệ**: Chọn hiển thị số tiền theo BTC hoặc Sats và loại tiền tệ fiat mặc định (đô la, euro, v.v.).





- **Cài đặt hoán đổi tự động**: Chức năng *Hoán đổi tự động* cho phép bạn tự động chuyển BTC từ **Thanh toán tức thì Wallet (Liquid)** sang **Bitcoin On-Chain** Wallet của bạn ngay khi số tiền đạt đến ngưỡng mà bạn cho là đủ cao để biện minh cho phí giao dịch.





- **Nhật ký**: Nhật ký hoạt động có thể xem được, có thể chia sẻ với bộ phận hỗ trợ kỹ thuật để hỗ trợ khắc phục sự cố.





- **Truy cập Telegram để được hỗ trợ**: Liên kết trực tiếp đến kênh Telegram chính thức để được hỗ trợ người dùng.





- **Truy cập Github**: Liên kết đến [Kho lưu trữ Github Bull Bitcoin](https://github.com/SatoshiPortal) để xem mã nguồn mở hoặc báo cáo sự cố.




## PHỤ LỤC



### A1. Giải thích về PayJoin (P2EP)



![image](assets/fr/25.webp)



**Sự định nghĩa** :




- PayJoin, hay **Pay-to-EndPoint (P2EP)**, là một kỹ thuật giao dịch Bitcoin giúp tăng cường tính bảo mật trên mạng **onchain**. Kỹ thuật này kết hợp các mục nhập của người gửi và người nhận trong một giao dịch duy nhất, giúp việc theo dõi số tiền và địa chỉ trở nên khó khăn hơn.



**Hoạt động:**




- Trong giao dịch PayJoin, người gửi và người nhận làm việc cùng nhau thông qua máy chủ PayJoin tương thích để thực hiện giao dịch chung generate.
- Thay vì chỉ người gửi cung cấp các mục nhập (UTXO), người nhận cũng đóng góp một trong các UTXO của riêng mình. Điều này làm mờ thông tin hiển thị trên Blockchain: thay vì một mục nhập duy nhất tương ứng với số tiền thực tế, giờ đây có hai mục nhập, và đầu ra không phản ánh trực tiếp số tiền được trao đổi.
- Giao dịch cuối cùng giống với giao dịch Bitcoin chuẩn (nhiều đầu vào/nhiều đầu ra), nhưng ẩn số tiền thực tế đã gửi và các liên kết giữa các địa chỉ nhờ cấu trúc ẩn chữ.



**Sử dụng cho Bull Bitcoin Mobile**




- **Nhận** (Address Supply): PayJoin được bật theo mặc định.
- **Gửi**: Wallet tự động phát hiện URI PayJoin và cấu hình giao dịch cho phù hợp, ví dụ:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Những lợi ích**




- **Tính bảo mật được cải thiện**: PayJoin vô hiệu hóa giả định rằng tất cả các mục nhập trong một giao dịch đều thuộc về một thực thể duy nhất. Với PayJoin, dữ liệu đầu vào đến từ cả bên gửi và bên nhận, phá vỡ giả định này.
- **Che giấu số tiền**: Số tiền thực tế được trao đổi không hiển thị trực tiếp trong kết quả đầu ra. Số tiền này được tính bằng chênh lệch giữa số tiền UTXO đến và đi của người nhận, khiến việc phân tích bị sai lệch.



**Giới hạn**




- PayJoin yêu cầu người gửi và người nhận phải sử dụng ví tương thích, nếu không thì sẽ sử dụng giao dịch onchain tiêu chuẩn.
- Giao dịch phức tạp hơn một chút (nhiều đầu vào và đầu ra hơn), dẫn đến chi phí cao hơn một chút.
- Mặc dù được thiết kế giống với giao dịch tiêu chuẩn, nhưng các phương pháp tìm kiếm nâng cao (ví dụ: đầu ra không rõ ràng, máy chủ PayJoin đã biết) có thể khiến người ta nghi ngờ về việc sử dụng phương pháp này, mặc dù không chắc chắn tuyệt đối.



**Thông tin thêm:**




- [Thuật ngữ](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les giao dịch PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Giải thích về Replace-by-fee (RBF)



**Định nghĩa**: Replace-by-fee (RBF) là một tính năng của mạng Bitcoin cho phép người gửi đẩy nhanh quá trình xác nhận giao dịch **trên chuỗi** bằng cách đồng ý trả phí cao hơn.



**Giới hạn** :




- RBF không khả dụng cho giao dịch Liquid hoặc Lightning.
- Giao dịch ban đầu phải được đánh dấu là tương thích với RBF khi được tạo, Bull Bitcoin Mobile sẽ tự động thực hiện điều này trừ khi bị vô hiệu hóa.



**Thông tin thêm:**




- [Thuật ngữ](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Thực hành tốt nhất



Để sử dụng **Bull Bitcoin Mobile** một cách an toàn và hiệu quả, hãy làm theo các khuyến nghị sau. Chúng sẽ giúp bạn bảo vệ tiền, tối ưu hóa giao dịch và giữ bí mật trên các mạng **Bitcoin (onchain)**, **Liquid** và **Lightning**.





- **Bảo mật cụm từ khôi phục của bạn**:
 - Hướng dẫn: [Lưu cụm từ Mnemonic của bạn](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La cụm từ mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- **Sử dụng xác thực an toàn**:
 - Kích hoạt **mã PIN mạnh** hoặc **xác thực sinh trắc học** (nhận dạng dấu vân tay hoặc khuôn mặt) để bảo vệ quyền truy cập vào ứng dụng.
 - Không bao giờ chia sẻ mã PIN hoặc dữ liệu sinh trắc học của bạn.





- **Bảo vệ quyền riêng tư của bạn**:
 - generate là Address mới cho mỗi lần tiếp nhận trên chuỗi hoặc Liquid để hạn chế theo dõi trên Blockchain.
 - Sử dụng PayJoin khi có thể để tăng tính bảo mật liên quan đến số tiền được gửi trên chuỗi
 - Để bảo mật tối đa, hãy kết nối Wallet của bạn với nút Bitcoin của riêng bạn thông qua máy chủ Electrum thay vì sử dụng nút công khai





- **Chọn mạng phù hợp nhất với nhu cầu của bạn**:
- **Onchain**: Được ưu tiên cho việc lưu ký dài hạn hoặc giao dịch có giá trị lớn (phí không đáng kể so với số tiền).
- **Liquid**: Sử dụng để chuyển tiền nhanh chóng, chi phí thấp với tính bảo mật cao.
- **Lightning**: Chọn chuyển khoản tức thời, chi phí thấp cho số tiền nhỏ. Nếu bạn có hai người dùng Wallet Bull Bitcoin, hãy chọn Liquid để tránh phí hoán đổi Lightning <> Liquid qua Boltz.





- **Luôn kiểm tra địa chỉ giao hàng**:
 - Trước khi gửi tiền, vui lòng kiểm tra kỹ Address. Tiền gửi sai địa chỉ Address sẽ bị mất vĩnh viễn. Vui lòng sử dụng chức năng sao chép/dán hoặc quét mã QR, tuyệt đối không sao chép/sửa đổi Address bằng tay.





- **Tối ưu hóa chi phí**:
 - Đối với các giao dịch trên chuỗi, hãy chọn mức phí phù hợp (chậm, trung bình, nhanh) tùy theo mức độ khẩn cấp và tắc nghẽn mạng.
 - Sử dụng Liquid hoặc Lightning cho số lượng nhỏ.
 - Kích hoạt Replace-by-fee (RBF) (xem Phụ lục 4) cho các lô hàng trên chuỗi nếu bạn dự đoán cần đẩy nhanh quá trình xác nhận.





- Giữ cho ứng dụng được cập nhật




### A4. Tài nguyên bổ sung





- Liên kết chính thức và hỗ trợ:
- [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com), **support@bullbitcoin.com** : email hỗ trợ
- [Trang web chính thức của Bull Bitcoin](https://bullbitcoin.com/): **Thông tin về các dịch vụ của Bull Bitcoin, cách tạo tài khoản, cách truy cập ứng dụng**
- [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile): **Xem mã, quá trình phát triển và lộ trình, đóng góp vào quá trình phát triển...**
- [Tài khoản X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)
- Nhóm **Telegram** dành cho thiết bị di động Wallet: trò chuyện nhóm với bộ phận hỗ trợ, xem trang "Cài đặt".





- Trình khám phá khối:
 - on chain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Thông tin về dòng khối](https://blockstream.info/Liquid)**
 - Sét: **[1ML (Lightning Network)](https://1ml.com/)**





- Học tập và hướng dẫn: **[Plan ₿ Network](https://planb.network/)**
 - Bảo mật cụm từ khôi phục của bạn



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Thuật ngữ](https://planb.network/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- **Lightning Network**:
- [Thuật ngữ](https://planb.network/resources/glossary/lightning-network)




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bò Bitcoin



#### Tổng quan về công ty



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, là nền tảng Exchange phi lưu ký lâu đời nhất, dành riêng cho Bitcoin, được thành lập năm 2013 tại Đại sứ quán Bitcoin ở Montreal, Canada. Dưới sự lãnh đạo của Francis Pouliot, một người tiên phong được công nhận trong hệ sinh thái Bitcoin, công ty tự định vị mình là một nhân tố chủ chốt trong việc thúc đẩy chủ quyền tài chính và quyền tự chủ của người dùng. Sứ mệnh của công ty là giúp mọi người lấy lại quyền kiểm soát tiền bạc của mình bằng cách sử dụng Bitcoin như một công cụ cho tự do và thanh toán, đồng thời từ chối các loại tiền tệ fiat và tiền điện tử khác ngoài Bitcoin.



![image](assets/fr/26.webp)



[Tạo tài khoản](https://app.bullbitcoin.com/registration/orangepeel) với mức giảm giá 0,25% khi mua và bán Bitcoin.



#### Giá trị và triết lý



Bull Bitcoin nổi bật với các nguyên tắc Commitment đến Cypherpunk và đạo đức Bitcoin:





- **Tập trung độc quyền vào Bitcoin**: Nền tảng này đúng với tầm nhìn về một loại tiền tệ phi tập trung, chống kiểm duyệt.





- **Không phải người giám hộ**: Người dùng vẫn giữ toàn quyền kiểm soát Bitcoin của mình bằng cách gửi tiền vào danh mục đầu tư của riêng họ.





- **Bảo mật**: Giảm thiểu việc thu thập dữ liệu cá nhân, với các tùy chọn mua hàng không cần KYC cho các giao dịch dưới 999 USD. Dữ liệu được bảo vệ theo quy định (FINTRAC tại Canada, AMF tại Pháp).





- **Tính minh bạch**: Không có phí ẩn, chi phí đã được bao gồm trong chênh lệch giá (chênh lệch giữa giá mua và giá bán).





- **Chủ quyền tài chính**: Bull Bitcoin thúc đẩy sự độc lập khỏi hệ thống ngân hàng truyền thống và các tổ chức tập trung.



#### Dịch vụ chính





- **Tiền gửi bằng tiền pháp định**: Người dùng có thể nạp tiền vào tài khoản Bull Bitcoin của mình bằng tiền pháp định (CAD, EUR, v.v.) thông qua chuyển khoản ngân hàng hoặc tiền mặt/thẻ ghi nợ tại các bưu điện Canada được chọn.





- **Mua Bitcoin**: Người dùng có thể mua Bitcoin được gửi trực tiếp vào danh mục đầu tư không lưu ký của họ, đảm bảo quyền kiểm soát hoàn toàn đối với tiền của họ.





- **Giao dịch mua Bitcoin theo lịch trình**: Bull Bitcoin cung cấp dịch vụ mua hàng định kỳ tự động (DCA - Trung bình chi phí bằng đô la) theo các khoảng thời gian đều đặn, sử dụng số dư khả dụng của bạn, với việc chuyển Bitcoin trực tiếp đến Wallet do người dùng kiểm soát, giúp giảm tác động của biến động giá.



Lưu ý rằng tùy chọn "Mua Tự Động" cho phép bạn chuyển đổi tiền pháp định ngay khi chúng chạm đến số dư Bull Bitcoin của bạn và gửi Bitcoin đến tài khoản Wallet của bạn. Tùy chọn này cũng có thể được kết hợp với chuyển khoản ngân hàng định kỳ được lên lịch với ngân hàng của bạn để thực hiện DCA. Tùy chọn này tự động tích lũy Bitcoin của bạn mà không cần phải mở ứng dụng.






- Mua Bitcoin với mức giá cố định **'Lệnh giới hạn'**: Cho phép bạn mua Bitcoin với mức giá do người dùng chỉ định trước, lệnh này sẽ tự động được thực hiện khi giá chỉ số Bull Bitcoin đạt hoặc giảm xuống dưới mức giới hạn đã đặt.





- **Bán Bitcoin**: Người dùng có thể bán Bitcoin của mình và nhận tiền bằng tiền pháp định trực tiếp vào tài khoản ngân hàng thông qua chuyển khoản ngân hàng hoặc SEPA.





- **Thanh toán của bên thứ ba**: Bull Bitcoin cho phép người dùng gửi tiền pháp định vào tài khoản ngân hàng từ Bitcoin của họ, hoàn toàn minh bạch với người nhận.





- **Bull Bitcoin Prime**: Bull Bitcoin Prime là dịch vụ cao cấp dành cho khách hàng doanh nghiệp và khách hàng có giá trị tài sản ròng cao, cung cấp các giải pháp tùy chỉnh và hỗ trợ cao cấp. Dịch vụ này bao gồm quyền truy cập vào mức phí ưu đãi, quản lý tài khoản chuyên dụng và các dịch vụ doanh nghiệp được thiết kế riêng. Dịch vụ này hướng đến các tổ chức, nhà giao dịch chuyên nghiệp và khách hàng doanh nghiệp đang tìm kiếm chuyên môn sâu rộng và dịch vụ ưu tiên.





- **Mobile Wallet**: Bull Bitcoin cung cấp Wallet di động mã nguồn mở, tự quản lý, có sẵn trên Android và iOS, hỗ trợ các giao dịch onchain, Liquid và Lightning Network.





- **Hỗ trợ giáo dục**: Hướng dẫn miễn phí và hướng dẫn cá nhân hóa giúp người dùng tạo, bảo mật và quản lý danh mục đầu tư Bitcoin của mình, củng cố quyền tự chủ về tài chính.



#### Tuân thủ và an toàn





- **Quy định**: Đã đăng ký với FINTRAC (Canada) và AMF (Pháp), Bull Bitcoin tuân thủ các yêu cầu KYC/AML.





- **Bảo mật**: Sử dụng danh mục đầu tư an toàn và các khuyến nghị lưu trữ ngoại tuyến. Dữ liệu cá nhân được lưu trữ trên cơ sở hạ tầng Bitcoin của Bull, hoàn toàn tự lưu trữ và không phụ thuộc vào bất kỳ bên thứ ba nào.