---
name: COLDCARD Mk4
description: Hướng dẫn thiết lập và sử dụng COLDCARD Mk4 với Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**wallet phần cứng** là các thiết bị vật lý được chế tạo riêng để lưu trữ khóa riêng của Bitcoin một cách an toàn. Chúng lưu trữ khóa riêng ngoại tuyến, có nghĩa là tin tặc không thể truy cập chúng qua internet. Trong khi **wallet phần mềm** chủ yếu được sử dụng cho các giao dịch hàng ngày, **wallet phần cứng** thường được sử dụng để lưu trữ một lượng lớn bitcoin một cách an toàn trong thời gian dài. Khi thực hiện giao dịch Bitcoin bằng **wallet phần cứng**, wallet có thể ký các giao dịch bên trong thiết bị, do đó khóa riêng không bao giờ bị lộ ra môi trường kết nối internet.


Trong hướng dẫn này, chúng ta sẽ tìm hiểu về một trong những thiết bị phần cứng wallet phổ biến nhất do Coinkite sản xuất, đó là Coldcard Mk4. Chúng ta sẽ xem xét cách thiết lập và sử dụng thiết bị phần cứng wallet này để thực hiện các giao dịch Bitcoin.


## Tổng quan về Coldcard Mk4


Coldcard Mk4 là phần cứng Bitcoin-only wallet do Coinkite sản xuất. Thiết bị này được trang bị màn hình, bàn phím số và nắp trượt bảo vệ. Ngoài ra, thiết bị cung cấp nhiều cách kết nối và tương tác, bao gồm USB-C, hoạt động không kết nối mạng bằng thẻ MicroSD, NFC và chế độ ổ đĩa ảo. Mk4 cũng bao gồm các tính năng bảo mật nâng cao như BIP39 passphrase và mã PIN bí mật, giúp người dùng kiểm soát và bảo vệ Bitcoin tốt hơn.


## Thiết lập ban đầu: Mã PIN và từ khóa chống lừa đảo


Để bắt đầu, bạn có thể mua Coldcard Mk4 trực tiếp từ trang web của Coinkite (https://store.coinkite.com/store). Người mua cũng có thể chọn thanh toán bằng tiền tệ pháp định hoặc Bitcoin. Ngoài ra, bạn cũng cần một thẻ MicroSD (4 GB là đủ) và một nguồn điện có thể kết nối qua cáp USB-C (Coldcard Mk4 chỉ có cổng nguồn USB-C). Lưu ý rằng vì Mk4 không có pin tích hợp, nên nó phải được kết nối với nguồn điện mọi lúc trong khi sử dụng.


Bạn sẽ nhận được thiết bị Mk4 trong một túi niêm phong chống giả mạo. Vui lòng đảm bảo rằng túi không bị hư hại. Nếu bạn phát hiện bất kỳ vấn đề nào như hư hỏng hoặc rách trên túi, bạn có thể thông báo cho Coinkite bằng cách gửi email đến support@coinkite.com. Ngoài ra, bạn cũng có thể tìm thấy một dãy số 12 chữ số trên túi niêm phong, mà chúng tôi sẽ gọi là số túi của Mk4. Số túi này sẽ được sử dụng sau này để xác minh rằng thiết bị không bị can thiệp trong quá trình vận chuyển và nó được gửi trực tiếp từ Coinkite. Số túi được lưu trữ an toàn trong secure element của thẻ Cold bằng bộ nhớ flash OTP (Lập trình một lần), có nghĩa là nó không thể thay đổi sau khi đã được lập trình. Khi bạn bật thiết bị lần đầu tiên, số hiển thị trên màn hình phải khớp với số trên túi. Điều này đảm bảo rằng Mk4 bạn nhận được là thiết bị chính hãng từ nhà máy và chưa bị thay thế hoặc sửa đổi. Mặc dù quá trình xác minh này chỉ xác nhận tính toàn vẹn của thiết bị tại thời điểm bật nguồn lần đầu, secure element vẫn tiếp tục bảo vệ các khóa riêng tư, mã PIN và passphrase của bạn, khiến cho việc can thiệp nhằm xâm phạm Bitcoin của bạn trở nên cực kỳ khó khăn. Ngoài ra, các biện pháp bảo mật tốt, chẳng hạn như bảo mật dữ liệu liên quan đến wallet một cách đúng đắn, sẽ có lợi cho tính bảo mật tổng thể của thẻ Cold. Để biết thêm thông tin, bạn có thể tham khảo bài viết này [article](https://blog.coinkite.com/understanding-mk4-security-model/) giải thích chi tiết mô hình bảo mật của thẻ Cold.


Bàn phím gồm 10 nút số, một nút OK (`✓`) và một nút hủy (`✕`). Một số nút số cũng có thể được sử dụng để điều hướng: `5` để điều hướng lên (`^`), `7` để điều hướng sang trái (`<`), `8` để điều hướng xuống `˅` và `9` để điều hướng sang phải (`>`).


![01](assets/en/01.webp)


Nếu không có vấn đề gì với bao bì, bạn có thể mở túi. Mk4 sẽ đi kèm với thẻ sao lưu wallet, có thể được sử dụng để lưu trữ thông tin liên quan đến mã PIN của thiết bị, các từ chống lừa đảo và seedphrase. Hãy làm theo các bước sau để khởi tạo:


1. Chuẩn bị một tờ giấy và một cây bút.

2. Kết nối Mk4 với nguồn điện (cáp USB-C) và lắp thẻ MicroSD.

3. Sau khi thiết bị được bật nguồn lần đầu tiên, màn hình sẽ hiển thị thông báo về Điều khoản Bán hàng và Sử dụng của Coldcard. Cuộn xuống, sau đó nhấn `✓` để tiếp tục.

4. Tiếp theo, một dãy số gồm 12 chữ số sẽ hiển thị trên màn hình. Hãy kiểm tra dãy số này so với dãy số trên túi niêm phong và bản sao bổ sung của số túi được kèm theo trong túi niêm phong để đảm bảo thiết bị không bị can thiệp. Nếu các số không khớp, hãy liên hệ ngay với bộ phận hỗ trợ của Coinkite trước khi tiếp tục. Nếu không, hãy nhấn `✓` để tiếp tục.


![02](assets/en/02.webp)


5. Chọn `Chọn mã PIN`.

6. Cuộn xuống theo hướng dẫn để chuyển sang bước tiếp theo.


![03](assets/en/03.webp)


7. Trên thiết bị Mk4, hãy tạo và nhập mã PIN tiền tố (phải dài từ 2 đến 6 ký tự) và ghi lại, sau đó nhấn `✓` để tiếp tục.

8. Hãy viết ra hai từ hiển thị trên màn hình. Đây là những từ chống lừa đảo trực tuyến. Nhấn `✓` để tiếp tục.


![04](assets/en/04.webp)


9. Tạo và nhập phần đuôi mã PIN (hoặc phần còn lại của mã PIN, phải dài từ 2 đến 6 ký tự) và ghi lại. Nhấn `✓` để tiếp tục.

10. Nhập lại mã PIN của bạn. Nhấn `✓` để tiếp tục.


![05](assets/en/05.webp)


11. Kiểm tra xem các từ chống lừa đảo có giống với từ bạn đã viết ở bước 8 hay không. Nhấn `✓` để tiếp tục.

12. Nhập lại phần đuôi mã PIN (hoặc phần còn lại của mã PIN). Nhấn `✓` để tiếp tục.


![06](assets/en/06.webp)


13. Mã PIN và cụm từ chống lừa đảo của Mk4 đã được tạo và lưu trữ thành công trên thiết bị.


![07](assets/en/07.webp)


Lưu ý rằng Coldcard Mk4 sẽ luôn yêu cầu bạn nhập mã PIN mỗi khi bật thiết bị. Nếu không có mã PIN này, bạn không thể truy cập vào Coldcard Mk4. Vì vậy, hãy đảm bảo bạn sao lưu đầy đủ mã PIN và các cụm từ chống lừa đảo.


## Thiết lập Wallet của bạn


Bước tiếp theo là thiết lập wallet của bạn. Có ba cách để bạn thực hiện việc này:


- Tạo một wallet mới (tiêu chuẩn)
- Tạo một wallet mới bằng cách tung xúc xắc
- Nhập khẩu wallet


### Tạo một chiếc wallet mới (tiêu chuẩn)


Để tạo một wallet mới, chỉ cần thực hiện các bước sau.


1. Chọn `New Wallet` (hoặc `New Seed Words`) > Chọn `12 Word` hoặc `24 Word (mặc định)` tùy theo sở thích của bạn.


![08](assets/en/08.webp)


2. Thiết bị sẽ tạo ra 12 hoặc 24 từ làm seedphrase tùy theo lựa chọn của bạn. Di chuyển xuống dưới và cẩn thận viết từng từ theo đúng thứ tự. Sau đó, nhấn `✓` để tiếp tục.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Thiết bị sẽ yêu cầu bạn xác minh seedphrase bằng cách đặt câu hỏi theo thứ tự ngẫu nhiên (ví dụ: `Từ 1 là?`, sau đó `Từ 5 là?`, rồi `Từ 12 là?`, v.v.) và sẽ có ba lựa chọn từ cho mỗi câu hỏi. Tham khảo ghi chú từ Bước 2 và chọn đúng từ (bằng cách nhấn `1`, `2` hoặc `3`, tùy thuộc vào từ đúng) để hoàn tất việc tạo wallet.


![09](assets/en/09.webp)


4. Mk4 sẽ hỏi bạn có muốn bật NFC/Chạm hay không. Hiện tại, hãy chọn `✕` cho tùy chọn này. Bạn có thể thay đổi tùy chọn này trong cài đặt sau này.

5. Cuối cùng, Mk4 cũng sẽ cho phép bạn tắt cổng USB (có thể dùng để truyền dữ liệu không kết nối mạng). Hiện tại, hãy chọn `✓` cho tùy chọn này. Bạn có thể thay đổi cài đặt này sau này.

6. Màn hình lúc này sẽ hiển thị menu chính với dòng chữ "Sẵn sàng ký" ở đầu. Điều này đánh dấu việc hoàn tất quá trình tạo wallet.


![10](assets/en/10.webp)


### Tạo một wallet mới bằng cách tung xúc xắc


Ngoài ra, bạn cũng có thể chọn tạo seedphrase mới bằng phương pháp ngẫu nhiên. Hãy làm điều này nếu bạn không tin tưởng vào seedphrase vừa được tạo ra từ Mk4.


Quy trình trên thẻ Coldcard Mk4 như sau:


1. Chọn `New Wallet` (hoặc `New Seed Words`) > Chọn `12 Word Dice Roll` hoặc `24 Word Dice Roll` tùy theo sở thích của bạn.

2. Bạn sẽ được yêu cầu nhập kết quả tung xúc xắc. Mỗi lần tung xúc xắc sẽ thêm yếu tố ngẫu nhiên vào quá trình tạo wallet, đảm bảo rằng seedphrase của bạn được tạo ra một cách hoàn toàn an toàn và không thể đoán trước. Số lần tung tối thiểu là 50 đối với seedphrase 12 từ và 99 đối với seedphrase 24 từ. Nhấn `✓` sau khi bạn đã nhập ít nhất 99 giá trị tung xúc xắc.


![11](assets/en/11.webp)


3. Thiết bị sẽ tạo ra 12 hoặc 24 từ làm seedphrase tùy theo lựa chọn của bạn. Di chuyển xuống dưới và cẩn thận viết từng từ theo đúng thứ tự. Sau đó, nhấn `✓` để tiếp tục.

4. Thiết bị sẽ yêu cầu bạn xác minh seedphrase bằng cách đặt câu hỏi theo thứ tự ngẫu nhiên (ví dụ: `Từ 1 là?`, sau đó `Từ 5 là?`, rồi `Từ 12 là?`, v.v.) và sẽ có ba lựa chọn từ cho mỗi câu hỏi. Tham khảo ghi chú từ Bước 3 và chọn đúng từ (bằng cách nhấn `1`, `2` hoặc `3`, tùy thuộc vào từ đúng) để hoàn tất việc tạo wallet.


![12](assets/en/12.webp)


5. Mk4 sẽ hỏi bạn có muốn bật NFC/Chạm hay không. Hiện tại, hãy chọn `✕` cho tùy chọn này. Bạn có thể thay đổi tùy chọn này trong cài đặt sau này.

6. Cuối cùng, Mk4 cũng sẽ cho phép bạn tắt cổng USB (có thể dùng để truyền dữ liệu không kết nối mạng). Hiện tại, hãy chọn `✓` cho tùy chọn này. Bạn có thể thay đổi cài đặt này sau này.

7. Màn hình lúc này sẽ hiển thị menu chính với dòng chữ "Sẵn sàng ký" ở đầu. Điều này đánh dấu sự hoàn tất của quá trình tạo wallet.


![13](assets/en/13.webp)


### Nhập khẩu wallet


Phương án cuối cùng là bạn nhập khẩu một chiếc wallet. Bạn có thể làm điều này nếu muốn khôi phục một chiếc wallet từ một chiếc seedphrase mà bạn đã có. Bạn có thể làm theo các bước sau:


1. Chọn `Nhập dữ liệu hiện có`.

2. Chọn `24 từ`, `18 từ` hoặc `12 từ`, tùy thuộc vào số lượng từ của seedphrase của bạn.


![14](assets/en/14.webp)


3. Coldcard Mk4 sẽ hỏi bạn từng từ theo thứ tự liên tiếp. Với mỗi từ, hãy di chuyển xuống hoặc lên cho đến khi bạn tìm thấy tiền tố chính xác của từ đó. Thiết bị sẽ thu hẹp các khả năng cho đến khi bạn tìm thấy từ đúng. Thực hiện tương tự với các từ còn lại.

4. Cuối cùng, Coldcard Mk4 sẽ chỉ hiển thị một số lượng từ có thể có giới hạn. Nếu không có từ nào khớp, có thể bạn đã nhập từ sai. Nếu không, hãy chọn từ khớp với từ trên seedphrase của bạn.


![15](assets/en/15.webp)


5. Mk4 sẽ hỏi bạn có muốn bật NFC/Chạm hay không. Hiện tại, hãy chọn `✕` cho tùy chọn này. Bạn có thể thay đổi tùy chọn này trong cài đặt sau này.

6. Cuối cùng, Mk4 cũng sẽ cho phép bạn tắt cổng USB (có thể dùng để truyền dữ liệu không kết nối mạng). Hiện tại, hãy chọn `✓` cho tùy chọn này. Bạn có thể thay đổi cài đặt này sau này.

7. Màn hình lúc này sẽ hiển thị menu chính với dòng chữ "Sẵn sàng ký" ở đầu. Điều này đánh dấu sự hoàn tất quá trình tạo wallet.


![16](assets/en/16.webp)


Xin lưu ý rằng seedphrase là thiết bị duy nhất có thể khôi phục wallet của bạn. Hãy tạo bản sao lưu seedphrase và lưu trữ ở nơi an toàn. **Không phải chìa khóa của bạn, không phải tiền của bạn**, bất cứ ai có seedphrase của bạn đều có quyền truy cập vào bitcoin của bạn!


## Thiết lập passphrase của bạn


Một trong những cách làm tốt nhất trong Bitcoin là sử dụng passphrase. passphrase đóng vai trò là từ thứ 13 hoặc thứ 25, bổ sung cho seedphrase. Điểm khác biệt là bạn có thể chọn bất kỳ cụm từ nào mình muốn, trong khi seedphrase được chọn từ một danh sách 2048 từ đã được xác định trước. Theo mặc định, sau khi thiết lập wallet, bạn sẽ bắt đầu với wallet có passphrase trống. Để thiết lập passphrase không trống, chỉ cần thực hiện các bước sau:


1. Vào mục `Mật khẩu`.

2. Cuộn xuống để đọc mô tả về passphrase, sau đó nhấn `✓` để tiếp tục.

3. Chọn `Chỉnh sửa cụm từ`.


![17](assets/en/17.webp)


4. Nhập passphrase của bạn:


   - Nhấn phím `1` (chữ cái), `2` (số) hoặc `3` (ký hiệu) để chọn loại ký tự.
   - Nhấn phím `4` để chuyển đổi giữa chữ thường và chữ hoa (chỉ có thể sử dụng khi nhập chữ).
   - Sử dụng phím `^` hoặc `˅` để chọn ký tự cho passphrase của bạn.
   - Sử dụng ký tự `<` hoặc `>` để di chuyển giữa các ký tự. Bạn cũng có thể sử dụng `>` để thêm khoảng trắng.
   - Nhấn `✕` để xóa các ký tự.
   - Nhấn `✓` khi bạn đã hoàn tất chỉnh sửa passphrase.

5. Ngoài ra, các tùy chọn khác còn có các chức năng sau:


   - Bạn có thể sử dụng chức năng "Thêm từ" hoặc "Thêm số" để thêm chữ cái/số vào tài liệu passphrase mà bạn đang chỉnh sửa.
   - Nhấn `Xóa TẤT CẢ` để đặt lại passphrase mà bạn đang chỉnh sửa.
   - Nhấn `HỦY` để quay lại menu chính.

6. Ghi lại thông tin về passphrase của bạn để dự phòng.

7. Nhấn `ÁP DỤNG` để truy cập wallet với passphrase mà bạn vừa thiết lập.

8. Sau đó, Mk4 sẽ hiển thị dấu vân tay khóa chính gồm 8 ký tự. Đây có thể được coi là "ID" của wallet. Hãy ghi lại dấu vân tay này và nhấn `✓` để tiếp tục.


![18](assets/en/18.webp)


9. Bây giờ, wallet sẽ hiển thị menu chính của wallet với passphrase mà bạn đã nhập vào.

10. Điều quan trọng cần lưu ý là wallet sẽ không thông báo cho bạn rằng bạn đã nhập sai passphrase, bởi vì mỗi passphrase tương ứng với một wallet riêng biệt với một mã định danh duy nhất (dấu vân tay khóa chính). Do đó, tốt nhất là nên nhập lại cùng một passphrase và kiểm tra xem nó có tạo ra cùng một dấu vân tay wallet hay không, để đảm bảo rằng bạn đã nhập đúng. Để làm điều đó, hãy thực hiện các bước từ 11 đến 14.

11. Trên menu chính, chọn `Khôi phục Master`, sau đó nhấn `✓`. Bây giờ bạn đã quay lại menu chính của wallet với passphrase trống.


![19](assets/en/19.webp)


12. Quay lại mục `Mật khẩu`, sau đó nhấn `✓` để tiếp tục.

13. Nhập lại mã passphrase mà bạn đã ghi lại ở Bước 6, sau đó nhấn `ÁP DỤNG`.

14. So sánh dấu vân tay khóa chính gồm 8 ký tự với dấu vân tay bạn đã ghi lại ở Bước 8. Nếu cả hai dấu vân tay không khớp, có thể bạn đã nhập sai ký tự. Bạn có thể chọn một passphrase mới và lặp lại quy trình từ Bước 1. Nhưng nếu cả hai dấu vân tay khớp, điều đó có nghĩa là bạn đã nhập passphrase chính xác.

15. Hệ thống wallet cùng với passphrase mà bạn đã chọn đã sẵn sàng để sử dụng.


## Xuất khẩu Wallet sang Sparrow


Giống như các thiết bị phần cứng wallet khác, Coldcard Mk4 không thể sử dụng độc lập. Nó cần được kết nối với phần mềm wallet đóng vai trò là giao diện. Phần mềm wallet cho phép bạn xem số dư, tạo giao dịch và quản lý địa chỉ, trong khi Coldcard ký các giao dịch đó một cách an toàn mà không bao giờ để lộ khóa riêng tư của bạn.


Trong hướng dẫn này, chúng ta sẽ sử dụng Sparrow và Wallet làm giao diện. Quy trình xuất dữ liệu cho wallet như sau:


1. Hãy đảm bảo rằng bạn đã lắp thẻ MicroSD vào Mk4.

2. Thực hiện các bước "Thiết lập passphrase của bạn" trên wallet với passphrase mà bạn muốn xuất. Nếu bạn muốn xuất wallet với passphrase trống, bạn có thể bỏ qua bước này.

3. Vào `Nâng cao/Công cụ` > Chọn `Xuất Wallet` > Chọn `JSON chung` > Cuộn xuống khi đọc hướng dẫn, sau đó nhấn `✓`.


![20](assets/en/20.webp)


4. Mk4 hiện đã tạo một tệp có định dạng `.json` trong thẻ MicroSD.


![21](assets/en/21.webp)


5. Tháo thẻ MicroSD khỏi Cold và lắp vào thiết bị nơi đã cài đặt Sparrow hoặc Wallet.

6. Mở Sparrow Wallet.

7. Nhấp vào `Tệp`


![22](assets/en/22.webp)


Tiếp theo, nhấp vào `New Wallet`


![23](assets/en/23.webp)


Sau đó, nhập tên cho wallet


![24](assets/en/24.webp)


Sau đó, nhấp vào `Tạo Wallet`


![25](assets/en/25.webp)


8. Chọn `Loại kịch bản`.


![26](assets/en/26.webp)


9. Trong mục Keystore, chọn `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Tìm Coldcard và nhấp vào `Nhập tệp...`.


![28](assets/en/28.webp)


11. Chọn tệp được tạo ở Bước 4 (tệp có định dạng `.json`).


![29](assets/en/29.webp)


12. Trên Mk4, quay lại menu chính và điều hướng đến `Nâng cao/Công cụ` > `Xem thông tin nhận dạng`. Đảm bảo rằng dấu vân tay hiển thị trên màn hình Mk4 khớp với dấu vân tay trên Sparrow Wallet (dấu vân tay chính trong phần Kho khóa)

13. Nhấp vào nút "Áp dụng" ở góc dưới bên phải.


![30](assets/en/30.webp)


14. Ngoài ra, bạn cũng có thể thêm mật khẩu cho wallet đã xuất. Mật khẩu này cần thiết mỗi khi bạn mở ứng dụng Sparrow hoặc Wallet để truy cập wallet. Nếu sau này bạn quên mật khẩu, bạn chỉ cần lặp lại các bước từ 1 đến 13 và chọn mật khẩu mới.


![31](assets/en/31.webp)


15. Chiếc wallet hiện đã được xuất khẩu thành công và sẵn sàng đưa vào sử dụng.


![32](assets/en/32.webp)


## Nhận bitcoin


Tiếp theo, chúng ta sẽ tìm hiểu cách nhận Bitcoin bằng Mk4. Quá trình này khá đơn giản vì bạn không cần sử dụng thiết bị Mk4. Chỉ cần bạn đã xuất wallet sang Sparrow, bạn có thể nhận Bitcoin trực tiếp thông qua Sparrow hoặc Wallet. Hãy làm theo các bước sau để nhận bitcoin bằng Mk4:


1. Mở Sparrow Wallet.

2. Chọn `Mở Wallet` > Chọn tệp wallet mà bạn muốn nhận bitcoin > Nhập mật khẩu liên kết với tệp wallet đó.


![33](assets/en/33.webp)


3. Trên giao diện của Sparrow, hãy nhấp vào tab `Nhận` ở phía bên trái của giao diện.


![34](assets/en/34.webp)


4. Một địa chỉ cùng với mã QR sẽ xuất hiện ở phía trên. Bạn có thể sao chép và dán địa chỉ hoặc quét mã QR bằng thiết bị wallet mà bạn sẽ sử dụng để gửi bitcoin đến Sparrow Wallet. Tùy chọn, bạn có thể nhập nhãn cho bitcoin bạn nhận được.


![35](assets/en/35.webp)


5. Sau khi bạn gửi bitcoin, trên giao diện của Sparrow, hãy nhấp vào tab `Giao dịch` ở phía bên trái của giao diện. Bạn sẽ thấy một mục mới ở đầu lịch sử giao dịch, tương ứng với giao dịch bạn vừa thực hiện.


![36](assets/en/36.webp)


6. Bạn cũng có thể điều hướng đến tab `UTXOs` ở phía bên trái giao diện để xem số bitcoin bạn vừa nhận được.


![37](assets/en/37.webp)


## Gửi bitcoin


Khác với việc nhận bitcoin, việc chi tiêu bitcoin liên kết với thẻ Cold của bạn yêu cầu bạn phải sử dụng thẻ Cold để ký giao dịch. Quy trình gửi bitcoin bằng Mk4 như sau:


1. Lắp thẻ MicroSD vào thiết bị có cài đặt Sparrow hoặc Wallet.

2. Mở Sparrow Wallet.

3. Chọn `Mở Wallet` > Chọn tệp wallet bạn muốn sử dụng để gửi bitcoin > Nhập mật khẩu liên kết với tệp wallet đó.


![38](assets/en/38.webp)


4. Trên giao diện của Sparrow, hãy nhấp vào tab `Gửi` ở phía bên trái của giao diện.


![39](assets/en/39.webp)


5. Trong tab "Thanh toán cho", nhập địa chỉ bạn muốn gửi bitcoin đến.

6. Thêm nhãn cho giao dịch.

7. Nhập số lượng bitcoin bạn muốn gửi.

8. Nhập phí bằng cách chuyển đổi mục `Phạm vi` hoặc nhập trực tiếp số vào mục `Phí`.


![40](assets/en/40.webp)


9. Ở góc dưới bên phải, nhấp vào `Tạo giao dịch`.


![41](assets/en/41.webp)


10. Bạn sẽ được chuyển đến một tab giao dịch mới có tên trùng với nhãn bạn đã nhập ở Bước 6. Nhấp vào `Hoàn tất giao dịch để ký`.


![42](assets/en/42.webp)


11. Nhấp vào `Lưu giao dịch` và lưu giao dịch vào thẻ MicroSD. Đổi tên tệp nếu cần. Bước này sẽ lưu giao dịch dưới dạng tệp PSBT.


![43](assets/en/43.webp)


12. Tháo thẻ MicroSD ra và lắp vào thẻ Coldcard Mk4 của bạn.

13. Bật nguồn Mk4 bằng cách kết nối với nguồn điện.

14. Nhập mã PIN của bạn.

15. Vào mục `Mật khẩu` và nhập passphrase của thiết bị wallet mà bạn muốn sử dụng để gửi bitcoin. Nếu bạn muốn sử dụng wallet với passphrase trống, hãy bỏ qua bước này.

16. Hãy đảm bảo dấu vân tay của khóa chính trùng khớp với dấu vân tay trên Sparrow hoặc Wallet của bạn. Bạn có thể kiểm tra điều này trên tab "Cài đặt" ở phía bên trái giao diện của Sparrow hoặc Wallet. Sau đó, nhấn "✓" trên Mk4 của bạn để tiếp tục. Thao tác này sẽ đưa bạn đến menu chính.

17. Trên menu chính của Mk4, chọn `Sẵn sàng ký`. Màn hình sẽ hiển thị thông báo `ĐỒNG Ý GỬI?`. Hãy đảm bảo số lượng bitcoin bạn muốn gửi và địa chỉ nhận đều chính xác. Nhấn `✓` để xác nhận hoặc `✕` để hủy.

18. Nếu có nhiều tệp PSBT để lựa chọn, Mk4 sẽ hiển thị thông báo `Chọn tệp PSBT cần ký`. Nhấn `✓` để tiếp tục. Sau đó, chọn tệp PSBT bạn muốn ký bằng cách di chuyển xuống hoặc lên. Thực hiện Bước 17 trên giao dịch đó.


![44](assets/en/44.webp)


19. Mk4 sẽ hiển thị thông báo `PSBT Signed` cùng với tên tệp của PSBT đã được ký. Nhấn `✓` để tiếp tục.

20. Tháo thẻ MicroSD khỏi Cold và lắp vào thiết bị nơi đã cài đặt Sparrow hoặc Wallet.

21. Trên Sparrow Wallet, nhấp vào `Tải giao dịch`.


![45](assets/en/45.webp)


22. Chọn tệp có cùng tên với tệp đã tạo ở Bước 19.


![46](assets/en/46.webp)


23. Nhấp vào `Giao dịch phát sóng`.


![47](assets/en/47.webp)


24. Giao dịch của bạn đã được gửi đi và đang được xử lý. Bạn có thể vào tab "Giao dịch" để xem trạng thái xác nhận giao dịch của mình.


![48](assets/en/48.webp)


## Nâng cấp phần mềm


### Kiểm tra phiên bản phần mềm của bạn


Phần mềm của Coldcard Mk4 luôn có thể được nâng cấp lên phiên bản mới hơn. Để kiểm tra xem Mk4 của bạn đã được nâng cấp lên phiên bản mới nhất hay chưa, hãy thực hiện các bước sau:

1. Bật nguồn Mk4 bằng cách kết nối với nguồn điện.

2. Nhập mã PIN của bạn.

3. Vào `Nâng cao/Công cụ` > Chọn `Nâng cấp phần mềm` > Chọn `Hiển thị phiên bản`.


![49](assets/en/49.webp)


Hãy kiểm tra phiên bản hiển thị trên màn hình của Mk4 so với phiên bản trên trang web của [Coinkite](https://coldcard.com/downloads). Nếu phiên bản khác nhau, bạn có thể nâng cấp firmware lên phiên bản mới hơn.


![50](assets/en/50.webp)


### Nâng cấp phần mềm của bạn


Nếu bạn muốn nâng cấp phần mềm lên phiên bản mới nhất, hãy thực hiện các bước sau:


1. Lắp thẻ MicroSD vào máy tính xách tay/máy tính để bàn của bạn.

2. Truy cập trang web của Coinkite (https://coldcard.com/downloads) và tải xuống firmware mới nhất vào thẻ MicroSD của bạn (nút màu đỏ bên phải hình ảnh Mk4 có số phiên bản).


![51](assets/en/51.webp)


Bạn cũng có thể tải xuống các phiên bản khác bằng cách nhấp vào `Tất cả tệp trên Mk4` và tìm phiên bản bạn muốn tải xuống. Tệp đã tải xuống sẽ ở định dạng `.dfu`.


![52](assets/en/52.webp)


3. Tháo thẻ MicroSD ra và lắp vào máy Mk4 của bạn.

4. Bật nguồn Mk4 bằng cách kết nối với nguồn điện.

5. Nhập mã PIN của bạn.

6. Vào `Nâng cao/Công cụ` > Chọn `Nâng cấp phần mềm` > Chọn `Từ thẻ MicroSD` > Cuộn xuống khi đọc hướng dẫn rồi nhấn `✓`.


![53](assets/en/53.webp)


7. Chọn tệp `.dfu` mà bạn đã tải xuống ở Bước 2.

8. Coldcard Mk4 sẽ hiển thị thông báo `Cài đặt firmware mới này?`. Cuộn xuống khi bạn đọc hướng dẫn rồi nhấn `✓`.


![54](assets/en/54.webp)


9. Chờ cho đến khi Mk4 hoàn tất quá trình cài đặt firmware mới. Không được ngắt nguồn điện trong suốt quá trình cài đặt.

10. Sau khi hoàn tất, Mk4 sẽ tự khởi động lại. Bạn có thể nhập mã PIN và thực hiện các bước "Kiểm tra phiên bản phần mềm" để kiểm tra xem phần mềm đã được nâng cấp hay chưa.


## Tính năng nâng cao


### Thay đổi mã PIN của bạn


Nếu bạn muốn thay đổi mã PIN đăng nhập, chỉ cần thực hiện các bước sau:


1. Chuẩn bị một cây bút và một tờ giấy.

2. Bật nguồn Mk4 bằng cách kết nối với nguồn điện.

3. Nhập mã PIN của bạn.

4. Vào `Cài đặt` > Chọn `Cài đặt đăng nhập` > Chọn `Thay đổi mã PIN chính`

5. Cuộn xuống khi đọc tin nhắn, sau đó nhấn `✓` để tiếp tục.


![55](assets/en/55.webp)


6. Nhập mã PIN cũ của bạn.

7. Nhập mã PIN mới của bạn (phải có từ 2 đến 6 ký tự) và ghi lại.

8. Mk4 sẽ hiển thị hai từ chống lừa đảo mới, hãy ghi lại chúng, sau đó nhấn `✓` để tiếp tục.

9. Nhập phần đuôi mã PIN mới của bạn (hoặc phần còn lại của mã PIN, phải có độ dài từ 2 đến 6 ký tự) và ghi lại.


![56](assets/en/56.webp)


10. Nhập lại mã PIN mới của bạn.

11. Kiểm tra xem các từ chống lừa đảo có khớp với từ bạn đã viết ở Bước 8 hay không.

12. Nhập lại hậu tố mã PIN mới (hoặc phần còn lại của mã PIN).


![57](assets/en/57.webp)


13. Mã PIN của bạn đã được thay đổi thành công.


### Mã PIN thủ thuật - Thêm thủ thuật mới


Mã PIN phụ (Trick PIN) là một mã PIN thay thế khác với mã PIN bạn sử dụng để thiết lập Coldcard Mk4 lần đầu tiên. Khi bật Mk4, bạn có thể nhập mã PIN phụ thay vì mã PIN chính để kích hoạt một số chức năng nhất định. Để cấu hình mã PIN phụ trong Mk4, bạn có thể thực hiện các bước sau:


1. Chuẩn bị một cây bút và một tờ giấy.

2. Bật nguồn Mk4 bằng cách kết nối với nguồn điện.

3. Nhập mã PIN của bạn.

4. Vào `Cài đặt` > Chọn `Cài đặt đăng nhập` > Chọn `Mã PIN bí mật` > Chọn `Thêm mã PIN bí mật mới`.


![58](assets/en/58.webp)


5. Nhập mã PIN bí mật của bạn (phải dài từ 2 đến 6 ký tự) và ghi lại.

6. Mk4 sẽ hiển thị hai từ chống lừa đảo mới, hãy ghi lại chúng, sau đó nhấn `✓` để tiếp tục.

7. Nhập phần đuôi mã PIN bí mật của bạn (hoặc phần còn lại của mã PIN, phải dài từ 2 đến 6 ký tự) và ghi lại.


![59](assets/en/59.webp)


8. Di chuyển xuống hoặc lên để chọn hành động bạn muốn ghép với mã PIN thủ thuật vừa tạo. Danh sách các hành động bao gồm:


    - Khi chọn tùy chọn "Brick Self", các chip trên chiếc Mk4 của bạn sẽ bị phá hủy sau khi nhập mã PIN, khiến chiếc Mk4 của bạn không thể sử dụng được vĩnh viễn.
    - `Xóa Seed`, bạn có thể chọn giữa các hành động sau:
      - `Xóa dữ liệu & Khởi động lại`: seed sẽ được xóa dữ liệu và Coldcard sẽ khởi động lại sau khi nhập mã PIN.
      - `Xóa dữ liệu im lặng`: seed được xóa dữ liệu một cách im lặng, tuy nhiên Coldcard sẽ hoạt động như thể mã PIN được nhập sai.
      - `Xóa -> Wallet`: seed sẽ bị xóa một cách im lặng, và thẻ Cold sẽ đưa bạn vào tình huống khẩn cấp wallet.
    - Khi chọn tùy chọn `Duress Wallet`, thiết bị Mk4 của bạn sẽ chuyển sang chế độ báo động wallet sau khi nhập mã PIN.
    - Trong mục `Đếm ngược đăng nhập`, bạn có thể chọn giữa các hành động sau:
      - `Xóa dữ liệu & Đếm ngược`: seed sẽ được xóa dữ liệu ngay lập tức, sau đó Mk4 sẽ bắt đầu hiển thị bộ đếm ngược.
      - `Đếm ngược & Hỏng`: Quá trình đếm ngược bắt đầu và Mk4 sẽ tự hỏng sau khi hết thời gian.
      - `Chỉ cần đếm ngược`: Mk4 sẽ bắt đầu đếm ngược và tự khởi động lại sau khi hết thời gian.
    - Khi chọn tùy chọn "Trông trống", sau khi nhập mã PIN bí mật, thẻ Cold sẽ hoạt động như thể thẻ seedphrase đã bị xóa dữ liệu, nhưng thực tế dữ liệu vẫn còn trong bộ nhớ.
    - Khi chọn tùy chọn "Chỉ cần khởi động lại", Coldcard sẽ tự khởi động lại sau khi nhập mã PIN bí mật.
    - Chế độ Delta (Delta Mode) là tính năng nâng cao dành cho người dùng có kinh nghiệm và được thiết kế để bảo vệ chống lại các mối đe dọa nghiêm trọng, chẳng hạn như sự ép buộc từ người có thông tin nội bộ. Khi Chế độ Delta được kích hoạt, COLDCARD sẽ hiển thị giao dịch mở wallet thật, cho phép kẻ tấn công duyệt và xác nhận rằng nó trông có vẻ chính hãng. Tuy nhiên, nó bí mật chặn tất cả các thao tác ký giao dịch, do đó không thể gửi bitcoin. Nó cũng vô hiệu hóa quyền truy cập vào cụm từ seed, và bất kỳ nỗ lực nào để xem cụm từ này sẽ xóa hoàn toàn nó. Để làm cho wallet giả trông thuyết phục hơn, mã PIN giả được sử dụng cho Chế độ Delta phải bắt đầu bằng các số giống với mã PIN thật (để hiển thị cùng các từ chống lừa đảo) nhưng kết thúc khác nhau.
    - Khi chọn tùy chọn `Mở khóa chính sách`, Chính sách chi tiêu chỉ dành cho người ký (SSSP) sẽ bị vô hiệu hóa sau khi nhập mã PIN bí mật.
    - Khi chọn tùy chọn `Mở khóa và xóa chính sách`, nó sẽ giả vờ vô hiệu hóa SSSP nhưng thực chất sẽ xóa sạch dữ liệu trên seedphrase trong quá trình này.

9. Sau khi bạn đã chọn hành động muốn ghép nối với mã PIN bí mật, hãy xác nhận lựa chọn của mình bằng cách nhấn `✓`. Mã PIN bí mật của bạn đã được cấu hình thành công.

10. Trong mục `Cài đặt` > `Cài đặt đăng nhập` > `Mã PIN đặc biệt`, bạn có thể xem danh sách các mã PIN đặc biệt đã tạo và các hành động được liên kết với chúng. Bạn có thể chọn cấu hình lại các mã PIN đặc biệt và các hành động được liên kết với chúng. Bạn cũng có thể ẩn hoặc xóa chúng bằng cách chọn mã PIN rồi chọn `Ẩn mã PIN đặc biệt` hoặc `Xóa mã PIN đặc biệt`.


![60](assets/en/60.webp)


### Mã PIN đánh lừa - Thêm nếu sai


Ngoài ra, bạn cũng có thể thêm hành động "Thêm nếu nhập sai" sẽ được kích hoạt sau khi nhập sai mã PIN một số lần nhất định. Bạn có thể cấu hình điều này bằng cách thực hiện các bước sau:


1. Bật nguồn Mk4 bằng cách kết nối với nguồn điện.

2. Nhập mã PIN của bạn.

3. Vào `Cài đặt` > Chọn `Cài đặt đăng nhập` > Chọn `Mã PIN bí mật` > Chọn `Thêm nếu sai`.


![61](assets/en/61.webp)


4. Mk4 sẽ hiển thị một thông báo liên quan đến cài đặt này. Cuộn xuống khi bạn đọc phần giải thích, sau đó nhấn `✓` để tiếp tục.

5. Nhập số lần nhập sai cần thiết để kích hoạt hành động. Lưu ý: Số lần nhập sai tối đa là 12. Điều này là do Mk4 được thiết kế sao cho khi nhập sai mã PIN 13 lần, thiết bị sẽ bị lỗi và không thể sử dụng được nữa. Sau khi nhập số, nhấn ✓ để tiếp tục.

6. Sử dụng phím mũi tên lên hoặc xuống để chọn thao tác. Các thao tác có sẵn như sau:


   - `Xóa, Dừng`: seedphrase bị xóa và thiết bị hiển thị “Dữ liệu đã bị xóa, Dừng lại.”
   - `Xóa dữ liệu & Khởi động lại`: seedphrase được xóa dữ liệu và thiết bị khởi động lại mà không hiển thị bất kỳ thông báo nào.
   - `Xóa im lặng`: seedphrase được xóa một cách im lặng và thiết bị hoạt động như thể nhập sai mã PIN (không có thông báo xóa rõ ràng).
   - `Brick Self`: Thiết bị bị vô hiệu hóa vĩnh viễn và chỉ hiển thị "Bricked" (Đã bị hỏng)
   - `Cơ hội cuối cùng`: seedphrase đã được xóa dữ liệu nhưng bạn có một lần thử nhập mã PIN cuối cùng; nếu nhập sai mã PIN một lần nữa, thiết bị sẽ bị hỏng hoàn toàn.
   - `Chỉ khởi động lại`: Thiết bị chỉ đơn giản là khởi động lại và không có gì khác thay đổi.

Chọn thao tác bạn muốn thực hiện và nhấn `✓` để tiếp tục


![62](assets/en/62.webp)


7. Bạn sẽ được đưa trở lại thư mục `Cài đặt > Cài đặt đăng nhập > Mã PIN bí mật`. Trong mục `Mã PIN bí mật:`, bạn sẽ tìm thấy danh sách các mã PIN bí mật cùng với tùy chọn `MÃ PIN SAI`. Bạn cũng có thể ẩn hoặc xóa mã PIN bằng cách chọn mã PIN đó rồi chọn `Ẩn mã PIN bí mật` hoặc `Xóa mã PIN bí mật`.


![63](assets/en/63.webp)



## Phần kết luận


Hướng dẫn này cung cấp các bước thiết lập Mk4, cách thực hiện giao dịch Bitcoin với Mk4 và cách sử dụng một số tính năng nâng cao của Mk4. Nó cung cấp các cách thức an toàn và linh hoạt để lưu trữ và quản lý bitcoin của bạn. Thiết kế của nó đảm bảo rằng khóa riêng tư không bao giờ rời khỏi thiết bị, trong khi các tính năng như passphrase, mã PIN giả và giao dịch không kết nối mạng cho phép người dùng kiểm soát hoàn toàn thiết lập bảo mật của họ. Nó có thể được ghép nối với Sparrow và Wallet để mang lại trải nghiệm thân thiện với người dùng khi tạo, ký và quản lý các giao dịch Bitcoin mà không ảnh hưởng đến quyền riêng tư hoặc bảo mật.


Nếu bạn muốn tìm hiểu thêm các chức năng khác, bạn có thể xem tài liệu trên trang web của Coinkite [tại đây](https://coldcard.com/docs/). Tôi hy vọng hướng dẫn này sẽ hữu ích cho bạn khi sử dụng Coldcard Mk4. Cảm ơn và hẹn gặp lại lần sau!