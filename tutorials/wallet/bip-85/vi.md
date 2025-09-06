---
name: BIP-85
description: Làm thế nào tôi có thể sử dụng nhiều cụm từ hạt giống BIP-85 đến generate từ seed chính?
---
![cover](assets/cover.webp)



## 1. Hiểu về BIP-85



### 1.1 BIP-85 là gì?



BIP-85 là một chức năng nâng cao cho phép bạn tạo nhiều **cụm từ phụ seed** từ một **cụm từ chính seed**.



Mỗi câu phụ seed có thể được sử dụng để tạo một danh mục đầu tư Bitcoin hoàn toàn độc lập. Các danh mục đầu tư này có thể được sử dụng cho nhiều mục đích khác nhau: danh mục đầu tư Hot, Wallet trên thiết bị di động, danh mục đầu tư cho người thân, danh mục đầu tư tiết kiệm riêng, v.v.



Tất cả các cụm từ phụ của seed đều **được suy ra từ toán học**, nhưng **không thể truy ngược lại cụm từ chính của seed** từ một cụm từ phụ. Điều này đảm bảo sự tách biệt hoàn toàn giữa mỗi danh mục đầu tư.



Chỉ cần bạn có quyền truy cập vào cụm từ chính seed của mình (và cụm từ passphrase liên quan nếu bạn đang sử dụng), bạn có thể tạo lại bất kỳ cụm từ phụ seed nào **giống hệt nhau**, mà không cần phải lưu riêng.



### 1.2 Tại sao nên sử dụng BIP-85?



BIP-85 hữu ích nếu bạn muốn:





- Tạo nhiều danh mục đầu tư Bitcoin độc lập mà không cần nhiều bản sao lưu
- Quản lý tiền của bạn theo các mục đích sử dụng khác nhau (tiết kiệm, chi phí, gia đình, dự án)
- Đảm bảo an toàn cho người thân (chức năng "Chú Jim")
- Xóa danh mục đầu tư mà không mất quyền truy cập vào tiền của bạn
- Đơn giản hóa bảo mật của bạn: chỉ cần một cụm từ khóa seed để bảo vệ



### 1.3 Ưu điểm so với BIP-32



Với BIP-32, một câu seed duy nhất có thể được sử dụng để generate toàn bộ hệ thống phân cấp các tài khoản và địa chỉ Bitcoin, sử dụng các đường dẫn phái sinh (ví dụ: `m/44'/0'/0'/0/0`). Mỗi đường dẫn có thể đại diện cho một tài khoản riêng biệt, nhưng **tất cả vẫn được liên kết đến cùng một câu seed**. Vì vậy, nếu cụm từ seed này bị xâm phạm, **tất cả các tài khoản phái sinh đều có thể truy cập được**.



Với BIP-85, một câu chính seed có thể được sử dụng để generate nhiều câu phụ seed hoàn toàn độc lập: **nếu một trong những hạt giống phụ này bị xâm phạm, kẻ tấn công sẽ không bao giờ có thể quay lại seed chính hoặc truy cập vào các danh mục đầu tư khác**.


Điều này giúp phân loại rủi ro một cách có thể:





- Bạn có thể sử dụng seed thứ cấp cho Hot Wallet hoặc sử dụng tạm thời, chấp nhận mức độ phơi sáng cao hơn.
- Ngay cả khi Hot Wallet này bị xâm phạm, các khoản tiền khác của bạn, được bảo vệ bởi các hạt giống thứ cấp khác hoặc được giữ ngoại tuyến, **vẫn an toàn**.



Mặt khác, đối với cả BIP-32 và BIP-85, nếu seed chính bị xâm phạm, **tất cả các quỹ đều dễ bị tấn công**. Do đó, việc bảo vệ nó với mức độ bảo mật cao nhất là vô cùng quan trọng.



![image](assets/fr/02.webp)


## 2. Các trường hợp sử dụng thực tế của BIP-85



BIP-85 cho phép bạn tạo nhiều danh mục đầu tư Bitcoin từ một cụm từ cốt lõi seed duy nhất, mỗi cụm từ có cụm từ phụ seed riêng. Dưới đây là năm trường hợp sử dụng thực tế để tổ chức và bảo mật quỹ Bitcoin của bạn. Mỗi trường hợp giải thích tại sao sử dụng BIP-85 thiết thực hơn so với việc quản lý nhiều tài khoản bằng một cụm từ seed duy nhất thông qua BIP-32.



### 2.1 Hạn chế rủi ro của danh mục đầu tư kém an toàn





- Tình huống**: Bạn sử dụng Wallet "Hot Wallet" (được cài đặt trên thiết bị có kết nối Internet) cho các giao dịch hàng ngày.
- Giải pháp BIP-85**: Bạn tạo cụm từ phụ seed dành riêng cho danh mục đầu tư này.
- Ưu điểm so với BIP-32**: Bạn không cần nhập cụm từ chính seed vào điện thoại, giúp giảm thiểu nguy cơ bị hack. Chỉ cụm từ phụ seed bị xâm phạm, bảo vệ các ví khác của bạn. Với BIP-32, bạn cần sử dụng cụm từ chính seed và một đường dẫn bỏ qua, khiến toàn bộ tiền của bạn bị lộ.



### 2.2 Tạo danh mục đầu tư cho một thành viên gia đình





- Tình huống**: Bạn thiết lập Bitcoin Wallet cho một người thân thiết với bạn (ví dụ: mẹ bạn), đồng thời có thể khôi phục lại nếu họ làm mất.
- Giải pháp BIP-85**: Bạn tạo một câu phụ seed chuyên dụng và chỉ chia sẻ câu này.
- Ưu điểm so với BIP-32**: Với BIP-32, việc tạo tài khoản cho người thân yêu yêu cầu bạn phải chia sẻ cụm từ seed chính của mình, mạo hiểm toàn bộ tiền của mình và làm phức tạp việc quản lý cho người thân yêu (quản lý các đường dẫn nhánh) hoặc tạo một cụm từ seed mới để lưu ngoài cụm từ seed chính của bạn.



### 2.3 Tạo điều kiện thuận lợi cho việc quản lý các danh mục đầu tư riêng biệt





- Kịch bản**: Bạn tách riêng số bitcoin của mình cho các mục đích khác nhau (ví dụ: tiết kiệm dài hạn, quỹ không KYC).
- Giải pháp BIP-85**: Bạn tạo các cụm từ phụ seed dành riêng cho từng mục tiêu.
- Ưu điểm so với BIP-32**: Với BIP-32, tất cả các tài khoản đều sử dụng chung một cụm từ seed, điều này làm phức tạp việc quản lý danh mục đầu tư của bên thứ ba do yêu cầu phải quản lý các đường dẫn phái sinh như `m/44'/0'/0'`. Ngoài ra, không thể chỉ định một tài khoản riêng cho mỗi thiết bị (ví dụ: "tiết kiệm trên Coldcard", "hàng ngày trên thiết bị di động", "kỳ nghỉ trên Trezor"). BIP-85 chỉ định một cụm từ phụ seed duy nhất cho mỗi mục tiêu, dễ dàng xác định và nhập riêng trên mỗi thiết bị.



### 2.4 Sử dụng Wallet tạm thời cho các giao dịch





- Kịch bản**: Bạn cần một danh mục đầu tư tạm thời cho một giao dịch một lần hoặc để bảo mật (ví dụ: trộn tiền, tương tác với Exchange KYC, v.v.).
- Giải pháp BIP-85**: Bạn tạo một câu phụ seed, sử dụng nó cho giao dịch, sau đó hủy nó nếu cần, vì biết rằng nó có thể được tạo lại.
- Ưu điểm so với BIP-32**: Với BIP-32, tài khoản tạm thời phụ thuộc vào câu chính seed, khiến toàn bộ tiền của bạn bị lộ nếu bị xâm phạm.





## 3. Trước khi bạn bắt đầu





- Phần cứng** (tùy chọn)
 - Coldcard Mk4 hoặc Q1
 - Thẻ nhớ MicroSD





- Kiến thức cơ bản
 - Hiểu các cụm từ Mnemonic (BIP-39): danh sách từ 12 đến 24 từ để lưu danh mục đầu tư.
 - Tìm hiểu Bitcoin Wallet là gì: phần mềm hoặc thiết bị để quản lý bitcoin của bạn và cách khôi phục bằng cụm từ Mnemonic.
 - Thêm tài nguyên trong Phụ lục.





- Phần mềm tương thích**
 - Sparrow wallet (máy tính, chỉ để theo dõi hoặc quản lý nâng cao)
 - Nunchuck (di động, dành cho nhiều chữ ký)
 - BlueWallet (di động)
 - ...





- 3.4 Cấu hình Coldcard**
 - Khởi tạo một câu seed gồm 24 từ trên Coldcard.
 - Tùy chọn: Thêm passphrase để bảo mật quyền truy cập vào các nhánh BIP-85.
 - Kích hoạt các tùy chọn hữu ích: NFC (để xuất), tắt USB trên pin (bảo mật).




## 4. Hướng dẫn từng bước



Thực hiện theo các bước sau để tạo, sử dụng và truy xuất Mnemonic thứ cấp với BIP-85 trên Coldcard của bạn.



### 4.1 generate a seed câu phụ



Bạn sẽ tạo cụm từ phụ seed từ cụm từ chính seed của mình.


Bật Coldcard, nhập mã PIN.





- 1. Nếu bạn đã áp dụng passphrase cho seed chính của mình:**
 - Từ màn hình chính, hãy vào `passphrase`.
    - Chọn `Thêm từ` và nhập mật khẩu của bạn.
    - Nhấn `Áp dụng`.
    - Kiểm tra danh tính của Wallet: Vào `Nâng cao > Xem danh tính` để ghi lại dấu vân tay của Wallet.





- 2. Vào menu BIP-85**
 - Từ màn hình chính, hãy vào `Nâng cao > Derive seed B85`
 - Đọc cảnh báo và xác nhận.



ColdCard thông báo cho bạn rằng các hạt giống được tạo ra có nguồn gốc toán học từ seed chính của bạn, nhưng hoàn toàn độc lập về mặt mật mã.


![image](assets/fr/03.webp)





- 3. Chọn định dạng


Chọn định dạng cụm từ seed: 12, 18 hoặc 24 từ. Kiểm tra số lượng từ được Wallet chấp nhận mà bạn muốn nhập cụm từ seed vào.


![image](assets/fr/04.webp)





- 4. Chọn chỉ mục
 - Nhập chỉ số từ 0 đến 9999.
 - Chỉ số này rất quan trọng để tái tạo seed thứ cấp sau này. Hãy giữ nó cẩn thận với các nhãn như: "Chỉ số 1 = Wallet di động", "Chỉ số 2 = dự án gia đình", "Chỉ số 4 = hỗn hợp thử nghiệm", ...
 - Nếu bạn làm mất nó, bạn sẽ không mất quyền truy cập vào tiền của mình, nhưng bạn sẽ phải thử các tổ hợp từ 0 đến 9999 để tìm ra chúng.


![image](assets/fr/05.webp)





- 5. Ghi chú hoặc xuất seed câu phụ**


ColdCard hiện hiển thị câu phụ seed mới. Bạn có thể:




 - **Ghi chú thủ công**.
 - Nhấn :
     - 1` để lưu vào thẻ SD
     - `2` để **vào chế độ "sử dụng seed này"** trên ColdCard (hữu ích khi xuất hoặc ký giao dịch)
     - 3` để hiển thị **mã QR** (để quét bằng ứng dụng di động như BlueWallet hoặc Nunchuck)
     - 4` để gửi nó bằng **NFC**



💡 Lúc này, bạn đã có một cụm từ seed độc lập, có thể sử dụng trong bất kỳ ví Wallet BIP39 nào (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Sử dụng seed thứ cấp



Bây giờ bạn có thể sử dụng seed được phái sinh này để tạo danh mục đầu tư mới trong:




- một ứng dụng di động
- một chiếc Hardware Wallet khác
- danh mục đầu tư Multisig



### 4.3 Khôi phục cụm từ thứ cấp seed bị mất



Để lấy lại seed thứ cấp bất cứ lúc nào, hãy lặp lại quy trình:


1. Khởi động lại ColdCard của bạn


2. Nhập mã PIN của bạn


3. Nhập passphrase của bạn, nếu được xác định


4. Vào `Nâng cao > Rút gọn seed B85`


5. Chọn định dạng (12/18/24 từ)


6. Nhập cùng một chỉ mục (ví dụ: `1`)


7. Bạn sẽ nhận được chính xác cùng một seed thứ cấp




## 5. Giới hạn, rủi ro và thực tiễn tốt nhất



### 5.1 Sự phụ thuộc vào câu chính seed + passphrase



Việc sử dụng BIP85 hoàn toàn dựa vào câu chính seed gồm 24 từ, cũng như passphrase nếu bạn đã áp dụng.




- Từ hai cụm từ Elements này, tất cả các cụm từ thứ cấp seed đều có thể được tái tạo.
- Nếu không có một trong 2 Elements này, bạn sẽ mất quyền truy cập vào tất cả các danh mục đầu tư phái sinh.



### 5.2 Rủi ro trong cấu hình đa chữ ký



Chúng tôi đặc biệt khuyên bạn không nên sử dụng cụm từ seed thứ cấp được tạo từ cùng cụm từ seed chính trong cấu hình multi-sig: nếu thiết bị hoặc cụm từ seed chính bị xâm phạm, tất cả các khóa multi-sig có thể được kẻ tấn công tạo lại.



### 5.3 Khả năng tương thích của phần mềm



Không phải tất cả các ứng dụng đều hỗ trợ trực tiếp việc dẫn xuất BIP85. Tuy nhiên, các hạt giống được tạo ra thông qua BIP85 là hạt giống BIP39 tiêu chuẩn (12, 18 hoặc 24 từ), do đó có thể được sử dụng trong bất kỳ danh mục đầu tư nào tương thích với BIP39.



### 5.4 Sổ đăng ký tài khoản BIP85



Bạn nên cập nhật sổ đăng ký cá nhân các cụm từ phụ seed.




- Nó cho phép bạn nhanh chóng tìm ra chỉ số BIP85 nào tương ứng với danh mục đầu tư nào mà không cần phải giữ lại các cụm từ phụ của seed.
- Sổ đăng ký này nên được giữ ở mức tối giản, không đề cập rõ ràng đến Bitcoin và nên được lưu trữ riêng biệt với seed chính. Hãy nhớ đề cập đến nó trong kế hoạch kế thừa của bạn.



Sổ đăng ký có thể chứa:




- Chỉ số bIP85 được sử dụng (số từ 0 đến 9999)
- tên sử dụng hoặc tên tham chiếu (ví dụ: Hot Wallet, tiết kiệm cá nhân, Wallet từ mẹ)
- nếu cần thiết, dấu vân tay Wallet để xác minh trong ColdCard



### 5.5 Sao lưu



Bản sao lưu phải bao gồm:




- seed chính
- gW-76 (nếu sử dụng)



Không bao giờ lưu trữ cùng nhau:




- seed và passphrase chính
- sổ đăng ký tài khoản chính seed và BIP85



Thêm tài nguyên trong Phụ lục.




## PHỤ LỤC



## A.1 Thuật ngữ





- [BÍP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [Cụm từ seed](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Lưu cụm từ khôi phục của bạn



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Hiểu về passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Danh mục đầu tư Bitcoin hoạt động như thế nào



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f