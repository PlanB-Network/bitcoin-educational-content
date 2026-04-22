---
name: Lightning Network+
description: Nhận thanh khoản đầu vào miễn phí với các cơ chế mở hợp tác trên node Lightning của bạn
---

![cover](assets/cover.webp)



## Giới thiệu



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) là một nền tảng cộng đồng được thiết kế để tạo điều kiện thuận lợi cho sự hợp tác giữa các nhà điều hành nút Lightning Network. Mục tiêu chính của nó là cải thiện khả năng kết nối, tính thanh khoản và tính phi tập trung của mạng Lightning, mà không cần đến các trung gian tập trung.



Bài hướng dẫn này sẽ tập trung vào dịch vụ **"Swaps"**, tính năng được sử dụng rộng rãi nhất và có tính cấu trúc cao nhất của LN+ hiện nay. Các dịch vụ khác do nền tảng này cung cấp cũng sẽ được giới thiệu.



## Tổng quan về LN+



### Lightning Network Plus là gì?



Lightning Network Plus (LN+) là một nền tảng cộng đồng dành cho các nhà điều hành nút Lightning muốn hợp tác trực tiếp và tự nguyện. Nền tảng này nhằm mục đích tạo điều kiện thuận lợi cho việc hình thành các kênh Lightning hữu ích, cân bằng và bền vững, đồng thời tránh sự cần thiết phải sử dụng các giải pháp tập trung hoặc các trung tâm điều khiển áp đặt.



LN+ dựa trên một nguyên tắc cơ bản: hợp tác ngang hàng, được xây dựng trên nền tảng minh bạch, tương hỗ và uy tín.



### Tổng quan về các dịch vụ của LN+



LN+ cung cấp một số dịch vụ được thiết kế để cải thiện cấu trúc liên kết và tính thanh khoản của mạng Lightning, bao gồm:





- Trao đổi**: việc mở kênh có đi có lại giữa các nhà mạng (dịch vụ chính).
- Vòng**: các khe hở hình tròn giữa nhiều người tham gia.
- Giao dịch hoán đổi dựa trên sự tin tưởng**: các biến thể dựa nhiều hơn vào sự tin tưởng và lịch sử giao dịch của các bên tham gia.
- Các tính năng xã hội**: hồ sơ cá nhân, bình luận và hệ thống đánh giá danh tiếng.



Trong phần còn lại của hướng dẫn này, chúng ta sẽ tập trung hoàn toàn vào dịch vụ **Swaps**, vốn là cốt lõi của việc sử dụng LN+ hiện nay.



## Dịch vụ "Trao đổi" LN+



### Định nghĩa về trao đổi LN+



LN+ **hoán đổi** là một thỏa thuận tự nguyện giữa hai nhà điều hành nút Lightning để cùng nhau mở các kênh Lightning có dung lượng tương đương (hoặc đã được thỏa thuận trước). Không giống như việc mở kênh đơn phương thông thường, việc hoán đổi dựa trên **sự tương hỗ rõ ràng**.



Trên thực tế:





- Bạn mở một kênh kết nối đến nút mạng của đối tác.
- Đối tác của bạn mở một kênh kết nối đến nút mạng của bạn.
- Cả hai bên đều đang nắm giữ một lượng bitcoin on-chain tương đương nhau.



### Mục đích của việc hoán đổi đối với các nhà điều hành nút là gì?



Dịch vụ Swaps giải quyết một số vấn đề chính mà các nhà khai thác Lightning gặp phải:





- Kết nối được cải thiện**: tạo ra các kênh hai chiều hữu ích ngay khi chúng được mở.
- Quản lý thanh khoản tốt hơn**: mỗi bên đều có khả năng nhận và chi tiền.
- Giảm thiểu rủi ro về các kênh không cần thiết**: đối tác được khuyến khích giữ kênh mở.
- Phân quyền cao hơn**: kết nối trực tiếp giữa các nhà điều hành, không cần các trung tâm trung gian.



### Việc hoán đổi (swap) có ích cho những cấu hình nút nào?



Trao đổi đặc biệt hữu ích cho:





- Các nút mạng mới mong muốn nhanh chóng cải thiện khả năng định tuyến của mình.
- Các nhà điều hành trung gian đang tìm cách tăng mật độ kênh phân phối của họ.
- Các nút định tuyến muốn tối ưu hóa cấu trúc liên kết của chúng.



## Kết nối nút Lightning của bạn với LN+



### Yêu cầu kỹ thuật



Trước khi bắt đầu, bạn sẽ cần:





- Một thiết bị Lightning đang hoạt động (LND, Core Lightning hoặc Eclair).
- Truy cập vào giao diện quản lý của nút mạng.
- Công suất on-chain đủ để mở các kênh.



Truy cập trang web [Lightning Network](https://lightningnetwork.plus/) Plus và nhấp vào nút `Đăng nhập` ở góc trên bên phải giao diện.



![capture](assets/fr/03.webp)



### Xác thực bằng chữ ký tin nhắn



Để xác thực danh tính, bạn cần ký vào thông điệp được cung cấp bằng khóa riêng của nút Lightning của mình. Với ThunderHub, thao tác này rất đơn giản.



Hãy bắt đầu bằng cách sao chép thông báo hiển thị trên LN+.



![capture](assets/fr/04.webp)



Trong ThunderHub, hãy vào tab `Công cụ`, sau đó nhấp vào nút `Ký tên` trong phần `Tin nhắn`.



![capture](assets/fr/05.webp)



Dán thông báo xác thực do LN+ cung cấp, sau đó nhấp vào `Ký`.



![capture](assets/fr/06.webp)



ThunderHub sau đó sẽ ký tin nhắn này bằng khóa riêng của nút mạng của bạn. Sao chép chữ ký đã tạo.



![capture](assets/fr/07.webp)



Dán chữ ký này vào ô tương ứng trên trang LN+, sau đó nhấp vào `Đăng nhập`.



![capture](assets/fr/08.webp)



Bạn hiện đã được kết nối với LN+ bằng node Lightning của mình. Quá trình này cho phép LN+ xác minh rằng bạn là chủ sở hữu hợp pháp của node mà bạn đã đăng ký trên nền tảng của họ.



![capture](assets/fr/09.webp)



Nếu muốn, bạn có thể cá nhân hóa hồ sơ LN+ của mình, ví dụ như thêm một đoạn tiểu sử ngắn.



## Tham gia vào một giao dịch trao đổi hiện có



### Truy cập vào các ưu đãi trao đổi



Để tham gia vào lần mở kênh đầu tiên, hãy vào menu `Swaps` ở đầu giao diện. Tại đây, bạn sẽ tìm thấy tất cả các giao dịch hoán đổi hiện có, tùy thuộc vào đặc điểm của node của bạn.



![capture](assets/fr/10.webp)



### Điều kiện đủ điều kiện



Để tham gia vào một giao dịch trao đổi hiện có, chỉ cần chọn quảng cáo tương ứng và đăng ký. Tuy nhiên, LN+ cho phép người tạo giao dịch trao đổi xác định một số **điều kiện tham gia** nhất định, chẳng hạn như:





- Số lượng kênh tối thiểu đã được mở;
- tổng dung lượng nút tối thiểu;
- Một số loại kết nối nhất định được chấp nhận.



### Các nút gần đây



Do đó, đặc biệt là trong giai đoạn đầu sử dụng, có thể **sẽ có rất ít hoặc không có ưu đãi nào** dành cho node của bạn. Đây là tình huống thường gặp đối với các node mới hoặc những node chưa được kết nối.



Trong trường hợp của tôi, mặc dù có một vài kênh liên hệ mở, nhưng không có lời đề nghị nào đáp ứng được các tiêu chí cần thiết.



## Tạo đề nghị trao đổi của riêng bạn



### Khi nào bạn nên tạo trang trao đổi của riêng mình?



Khi không có sẵn lời đề nghị nào, việc tự tạo ra một giao dịch hoán đổi thường là giải pháp tốt nhất. Điều này cũng cho phép bạn giữ quyền kiểm soát các thông số của giao dịch hoán đổi.



### Cấu hình hoán đổi



Nhấp vào **Bắt đầu trao đổi Liquidity**, sau đó cấu hình các thông số chào hàng của bạn:





- Chọn tổng số người tham gia (3, 4 hoặc 5);
- Cho biết dung lượng của các kênh sẽ được mở;
- Xác định khoảng thời gian cam kết mà trong đó người tham gia đồng ý không đóng kênh của họ;
- Hãy nêu rõ bất kỳ hạn chế nào áp dụng cho người tham gia (số kênh tối thiểu, tổng dung lượng tối thiểu, loại kết nối được chấp nhận).



![capture](assets/fr/11.webp)



### Ấn phẩm và kỳ vọng của người tham gia



Sau khi nhập đầy đủ các thông số, hãy nhấp vào **Bắt đầu trao đổi Liquidity** để đăng tải lời đề nghị của bạn. Bây giờ tất cả những gì bạn cần làm là chờ đợi các nhà mạng khác đăng ký.



![capture](assets/fr/12.webp)



## Hoàn tất giao dịch trao đổi



### Mở kênh hiệu quả



Giờ đây, khi tất cả các vị trí hoán đổi đã được thiết lập, mỗi người tham gia có thể xem, từ giao diện LN+ của mình, nút nào họ cần mở kênh Lightning để kết nối.



![capture](assets/fr/13.webp)



Về phía bạn, hãy mở kênh bằng cách sử dụng ID nút do LN+ cung cấp và tuân thủ số lượng được chỉ định. Thao tác này có thể được thực hiện thông qua ThunderHub, một trình quản lý nút Lightning khác hoặc trực tiếp thông qua giao diện cơ bản của nút của bạn.



![capture](assets/fr/14.webp)



Sau khi mở, kênh sẽ xuất hiện trong phần kênh chờ.



![capture](assets/fr/15.webp)



### Xác nhận trong LN+



Sau đó quay lại LN+ để xác nhận rằng bạn đã bắt đầu mở kênh bằng cách nhấp vào nút `Channel Opening Started`.



![capture](assets/fr/16.webp)



### Kết thúc trao đổi



Khi tất cả người tham gia đã mở các kênh mà họ đã cam kết, quá trình trao đổi được coi là hoàn tất.



## Uy tín và thực tiễn giao tiếp tốt



### Hệ thống danh tiếng LN+



LN+ tích hợp hệ thống đánh giá uy tín dựa trên ý kiến ​​của người tham gia khi kết thúc các giao dịch. Những ý kiến ​​này được công khai và ảnh hưởng trực tiếp đến khả năng tham gia hoặc tạo ra các giao dịch trong tương lai của người điều hành.



![capture](assets/fr/17.webp)



### Các phương pháp thực hành tốt nhất được khuyến nghị



Để giữ gìn uy tín và đảm bảo các giao dịch hoán đổi diễn ra suôn sẻ, nên thực hiện các bước sau:





- Tuân thủ thời hạn mở kênh;
- Thông báo nhanh chóng trong trường hợp có sự cố hoặc chậm trễ;
- Hãy sử dụng phần bình luận để trao đổi quan điểm với những người tham gia khác;
- Không được đóng kênh trước khi kết thúc thời hạn cam kết.




![capture](assets/fr/18.webp)



### Vì sao danh tiếng lại quan trọng đối với LN+



LN+ dựa trên mô hình hợp tác tự nguyện, không có ràng buộc kỹ thuật chặt chẽ. Do đó, uy tín là động lực chính để đảm bảo độ tin cậy của các thành viên tham gia.



## Các dịch vụ LN+ khác



Ngoài các giao dịch hoán đổi (Swaps), LN+ còn cung cấp các dịch vụ khác được thiết kế để cải thiện khả năng kết nối và phối hợp giữa các nhà điều hành nút Lightning. Các vòng (Rings)** cho phép nhiều người tham gia tạo ra một vòng lặp mở kênh, do đó tăng cường tính dự phòng của các đường dẫn định tuyến và mật độ của đồ thị Lightning. Các giao dịch hoán đổi dựa trên độ tin cậy (Trust-based swaps)** dựa trên các nguyên tắc tương tự như các giao dịch hoán đổi truyền thống, nhưng mang lại sự linh hoạt hơn cho những người tham gia đã có uy tín trên nền tảng.



LN+ cũng tích hợp các tính năng xã hội như hồ sơ nút công khai, bình luận trao đổi và hệ thống đánh giá uy tín. Những công cụ này không phải là dịch vụ kỹ thuật thuần túy, nhưng đóng vai trò trung tâm trong việc vận hành trơn tru nền tảng, tạo điều kiện thuận lợi cho giao tiếp, phối hợp và xây dựng lòng tin giữa các nhà điều hành.



## Phần kết luận



Dịch vụ Swaps của LN+ là một công cụ hiệu quả để cải thiện khả năng kết nối, tính thanh khoản và tính phi tập trung trong mạng Lightning. Bằng cách thúc đẩy việc mở kênh có đi có lại và phối hợp, LN+ cho phép các nhà điều hành nút tăng cường cấu trúc liên kết của họ, đồng thời thúc đẩy sự hợp tác có trách nhiệm và phi tập trung.