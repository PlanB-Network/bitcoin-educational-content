---
name: Bisq Easy Mobile
description: Một giao thức giao dịch ngang hàng dành cho người dùng Bitcoin mới - không cần trung gian, không cần xác minh danh tính (KYC).
---
![cover](assets/cover.webp)


## Giới thiệu


Giao thức giao dịch [Bisq Easy](https://bisq.network/bisq-easy/) được thiết kế cho [Bisq 2](https://github.com/bisq-network/bisq2), phiên bản kế nhiệm của [Bisq v1](https://github.com/bisq-network/bisq). Bisq 2 sẽ hỗ trợ nhiều giao thức giao dịch, mạng lưới bảo mật và danh tính khác nhau. Nó tạo điều kiện thuận lợi cho việc mua Bitcoin với phí giao dịch bằng không và không yêu cầu đặt cọc bảo đảm. Nó dành cho những người mua Bitcoin mới đang tìm kiếm một lựa chọn không cần KYC, những người muốn được hỗ trợ nhanh chóng bởi những người bán giàu kinh nghiệm và am hiểu nền tảng Bisq.


Hiện tại, Bisq Easy là giao thức giao dịch duy nhất dành cho Bisq 2. Nhiều giao thức giao dịch khác đang được lên kế hoạch cho tương lai. Tìm hiểu thêm về Bisq 2 trong hướng dẫn này:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

Hướng dẫn ngắn này bổ sung cho hướng dẫn ở trên về việc mua Bitcoin bằng ứng dụng [Bisq Easy Mobile](https://github.com/bisq-network/bisq-mobile) và Lightning.


## 1️⃣ Bắt đầu


Để bắt đầu, hãy tải xuống Bisq Easy Mobile từ trang tải xuống (https://bisq.network/downloads/). Bạn nên xác minh tệp đã tải xuống. Hướng dẫn xác minh cũng có trên trang tải xuống (https://bisq.network/downloads/). Sau khi cài đặt, bạn cần chấp nhận Thỏa thuận người dùng. Tiếp theo, hãy tạo một hồ sơ công khai bao gồm tên người dùng (nickname) và ảnh đại diện (được biểu thị bằng biểu tượng bot). Với Bisq Easy, bạn cũng có thể tạo nhiều hồ sơ người dùng trong cùng một ứng dụng. Sau quá trình khởi tạo ngắn, bạn sẽ đến màn hình chính. Ứng dụng hiển thị các tài liệu hướng dẫn trực tiếp trên trang chính. Nhấn vào "Mở Hướng dẫn Giao dịch" để làm quen với các thông tin mới nhất.


![image](assets/en/01.webp)


Cẩm nang thương mại giải thích mọi thứ liên quan một cách dễ hiểu theo từng bước:



- Hướng dẫn giao dịch dễ dàng trên Bisq
- Quy trình giao dịch diễn ra như thế nào?
- Tôi cần biết những gì về các quy tắc thương mại?


Một phần quan trọng khác là **"Giao dịch trên Bisq Easy an toàn đến mức nào?"**


![image](assets/en/08.webp)


Đánh dấu vào ô có nhãn "Tôi đã đọc và hiểu" rồi nhấn "Hoàn tất".


![image](assets/en/02.webp)


## 2️⃣ Sao lưu dữ liệu của bạn


Trước khi bắt đầu, hãy thực hiện một số tác vụ quản trị và tạo bản sao lưu dữ liệu của bạn. Vào mục "Thêm" > "Sao lưu & Khôi phục" để lưu hồ sơ và lịch sử giao dịch của bạn. Nếu bạn mất thiết bị mà không có bản sao lưu, danh tiếng và các giao dịch đang thực hiện của bạn sẽ không thể khôi phục được. Cung cấp "Mật khẩu" để mã hóa bản sao lưu của bạn.


![image](assets/en/11.webp)


## 3️⃣ Ưu đãi


Từ màn hình chính, có hai cách để truy cập vào các ưu đãi. Chạm vào "Khám phá ưu đãi" ở giữa màn hình hoặc chạm vào "Ưu đãi" trong menu dưới cùng. Từ đó, chọn loại tiền tệ bạn muốn giao dịch.


![image](assets/en/03.webp)


Không giống như [Bisq 1](https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), yêu cầu tài sản thế chấp, Bisq Easy chỉ dựa vào uy tín của người bán để đảm bảo an ninh. Mặc dù phương pháp này cho phép người mua mua Bitcoin lần đầu tiên mà không cần sở hữu trước đó, nhưng nó đặt niềm tin rất lớn vào khả năng giao hàng Bitcoin của người bán sau khi nhận được thanh toán bằng tiền pháp định. Do đó, mô hình bảo mật của Bisq Easy chỉ được tối ưu hóa cho các giao dịch có số lượng nhỏ và các giao dịch bị giới hạn ở mức tương đương 600 USD mỗi giao dịch để giảm thiểu rủi ro. Trong phần `Offerbook`, hãy chọn bộ lọc cho phương thức thanh toán và thanh toán bằng Lightning hoặc Bitcoin (on-chain).


![image](assets/en/04.webp)


Sau khi áp dụng `bộ lọc`, hãy chọn một ưu đãi phù hợp từ một đối tác thương mại uy tín. Phương thức thanh toán và loại giao dịch được người bán lựa chọn trước (`Lightning` hoặc `on-chain`) sẽ được hiển thị. Hãy đảm bảo rằng chúng phù hợp với sở thích của bạn trước khi tiếp tục. Ở đây chúng ta chọn tùy chọn Lightning ⚡.


![image](assets/en/05.webp)


Xem lại và xác nhận chi tiết giao dịch bằng cách nhấn vào `Xác nhận chấp nhận đề nghị`. Sau đó, một màn hình bật lên sẽ xác nhận rằng bạn đã chấp nhận đề nghị thành công. Nhấn vào Hiển thị giao dịch trong `Giao dịch đang mở`. Trong phần Giao dịch đang mở, dán `hóa đơn Lightning` của bạn và nhấn `Gửi cho người bán` để chia sẻ. Bây giờ hãy đợi thông tin tài khoản thanh toán của người bán. Người bán có thể cần thời gian để phản hồi. Hãy kiểm tra định kỳ để cập nhật thông tin trong cửa sổ trò chuyện.


![image](assets/en/06.webp)


Hãy gửi lời chào ngắn gọn trong phần trò chuyện. Người bán sẽ chia sẻ thông tin thanh toán khi họ trực tuyến


![image](assets/en/09.webp)


Sau khi nhận được thông tin thanh toán cần thiết từ người bán, hãy tiến hành thanh toán. Sau đó, nhấn vào nút "Xác nhận đã thanh toán" và kiên nhẫn chờ xác nhận đã nhận được tiền. ️ ⌛️


Cuối cùng, khi người bán xác nhận đã nhận được thanh toán, bạn cũng phải xác nhận đã nhận được Bitcoin. Như vậy là hoàn tất giao dịch mua bán bằng Bisq ở Chế độ Dễ. Chúc mừng! Giờ bạn có thể nhấn vào nút "kết thúc giao dịch".


![image](assets/en/10.webp)


## 4️⃣ Giải quyết tranh chấp trên Bisq Dễ dàng


Nếu có bất kỳ vấn đề nào phát sinh trong giao dịch, cả người mua và người bán đều có thể yêu cầu hỗ trợ hòa giải.


**Những việc mà người hòa giải có thể làm:**

• Hỗ trợ hoàn tất giao dịch thành công

• Xác minh các khoản thanh toán bằng tiền pháp định, altcoin và Bitcoin

• Hủy giao dịch khi cần thiết

• Báo cáo các vi phạm nghiêm trọng quy tắc cho người điều hành để có thể bị cấm sử dụng


**Hậu quả đối với người bán hàng gian lận:**

Tùy thuộc vào loại danh tiếng của họ:



- Danh tiếng trái phiếu BSQ**: DAO có thể tịch thu BSQ ngoại quan của họ
- Uy tín Onion Address**: Địa chỉ onion Bisq 1 của họ có thể bị cấm


**Lưu ý quan trọng:** Vì tất cả điểm uy tín đều gắn liền với hồ sơ người dùng của bạn, việc bị cấm sẽ làm mất hoàn toàn điểm uy tín của bạn.


## 5️⃣ Tạo ưu đãi của riêng bạn


Thay vì chấp nhận các lời đề nghị hiện có, bạn có thể tạo lời đề nghị mua của riêng mình và để người bán liên hệ với bạn. Đây là lựa chọn phù hợp nếu bạn không tìm thấy bất kỳ lời đề nghị nào với mức phí bảo hiểm hoặc phương thức thanh toán phù hợp trên thị trường mà bạn muốn giao dịch, mặc dù bạn sẽ cần phải chờ người bán chấp nhận.


Từ màn hình "Ưu đãi", chạm vào biểu tượng "+" màu xanh lá cây ở góc dưới bên phải. Sau đó chọn "Mua Bitcoin" và chọn loại tiền tệ bạn muốn sử dụng.


Thiết lập các thông số giao dịch của bạn:



- Số tiền cố định hoặc số tiền trong khoảng**: Chọn số tiền bạn muốn chi tiêu.
- Phương thức thanh toán**: Chọn từ các tùy chọn có sẵn
- Khu định cư**: Chọn Lightning ⚡ hoặc ₿ on-chain


Xem lại thông tin chi tiết của bạn và nhấn vào `Tạo ưu đãi`. Ưu đãi của bạn giờ sẽ xuất hiện trong `Sổ ưu đãi`.


![image](assets/en/07.webp)


*Lưu ý: Là người mua trên Bisq Easy, bạn không cần có uy tín—đây là lợi thế quan trọng. Người bán chịu trách nhiệm về yêu cầu và rủi ro về uy tín, đó là lý do tại sao họ tính phí cao hơn. Giá chào bán của bạn chỉ cần đủ hấp dẫn để người bán có uy tín xem xét.*


Sau khi đăng bán, hãy chờ trong mục `Offerbook`. Khi người bán chấp nhận đề nghị của bạn, bạn sẽ nhận được thông báo. Mở giao dịch trong mục `Open Trades`, nơi bạn và người bán có thể trao đổi thông tin thanh toán. Gửi địa chỉ Bitcoin hoặc hóa đơn Lightning của bạn cho người bán. Sau khi gửi tiền, hãy xác nhận thanh toán. Khi người bán xác nhận đã nhận được tiền, họ sẽ gửi Bitcoin để hoàn tất giao dịch.


## 🎯 Kết luận


Bisq Easy cho phép mua Bitcoin mà không cần tài sản thế chấp, giải quyết được vấn đề "con gà và quả trứng" kinh điển cho người mua mới. Sự đánh đổi rất rõ ràng: bạn dựa vào uy tín của người bán thay vì tiền bị khóa để đảm bảo an toàn. Cách tiếp cận dựa trên sự tin tưởng này giải thích mức phí bảo hiểm điển hình từ 5-15%, nhằm bù đắp cho những người bán có uy tín vì khoản đầu tư của họ vào việc xây dựng lòng tin và cung cấp hỗ trợ. Mặc dù hệ thống giới hạn giao dịch ở số lượng nhỏ để hạn chế tổn thất tiềm tàng, hãy luôn chọn những người bán có điểm uy tín cao. Đối với những người mới sẵn sàng chấp nhận các điều khoản này, Bisq Easy cung cấp một điểm khởi đầu dễ dàng để tiếp cận Bitcoin.


## 📚 Tài nguyên di động dễ sử dụng Bisq


[Github](https://github.com/bisq-network/bisq-mobile) | [Trang web](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)