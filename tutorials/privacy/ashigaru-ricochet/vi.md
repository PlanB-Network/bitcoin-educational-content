---
name: Ashigaru - Ricochet
description: Hiểu và sử dụng giao dịch Ricochet
---
![cover ricochet](assets/cover.webp)



> *Một công cụ cao cấp bổ sung thêm nhiều bước nhảy lịch sử vào giao dịch của bạn. Ngăn chặn danh sách đen và giúp bảo vệ tài khoản của bên thứ ba khỏi bị đóng bất hợp pháp.*

## Ricochet là gì?



Ricochet là một kỹ thuật bao gồm việc thực hiện một số giao dịch giả định với chính mình để mô phỏng việc chuyển giao quyền sở hữu bitcoin. Công cụ này khác với các giao dịch khác của Ashigaru (được kế thừa từ Samurai Wallet) ở chỗ nó không cung cấp tính ẩn danh dự kiến, mà là một hình thức ẩn danh hồi tố. Trên thực tế, Ricochet làm mờ đi những đặc điểm có thể ảnh hưởng đến tính linh hoạt của một bộ phận Bitcoin.



Ví dụ, nếu bạn thực hiện một lệnh coinjoin, phần của bạn thoát ra khỏi hỗn hợp sẽ được xác định là như vậy. Các công cụ phân tích chuỗi có thể phát hiện các mẫu của các giao dịch coinjoin và gán nhãn cho các phần thoát ra từ chúng. Trên thực tế, coinjoin nhằm mục đích phá vỡ các liên kết lịch sử của một đồng xu, nhưng việc nó đi qua các lệnh coinjoin vẫn có thể bị phát hiện. Tương tự, hiện tượng này tương tự như việc mã hóa một văn bản: mặc dù văn bản gốc không thể được truy cập ở dạng văn bản rõ, nhưng rất dễ nhận biết rằng mã hóa đã được áp dụng.



Nhãn "coinjoined" có thể ảnh hưởng đến khả năng thay thế của UTXO. Các đơn vị được quản lý, chẳng hạn như sàn giao dịch, có thể từ chối chấp nhận UTXO đã được coinjoined, hoặc thậm chí yêu cầu chủ sở hữu giải thích, với nguy cơ tài khoản của bạn bị khóa hoặc tiền của bạn bị đóng băng. Trong một số trường hợp, nền tảng thậm chí có thể báo cáo hành vi của bạn cho các cơ quan nhà nước.



Đây chính là lúc phương pháp Ricochet phát huy tác dụng. Để làm mờ dấu ấn do coinjoin để lại, Ricochet thực hiện bốn giao dịch liên tiếp, trong đó người dùng chuyển tiền cho chính mình tại các địa chỉ khác nhau. Sau chuỗi giao dịch này, công cụ Ricochet cuối cùng sẽ định tuyến bitcoin đến đích cuối cùng, chẳng hạn như một sàn giao dịch. Mục đích là tạo khoảng cách giữa giao dịch coinjoin ban đầu và hành động chi tiêu cuối cùng. Theo cách này, các công cụ phân tích blockchain sẽ giả định rằng có thể đã có sự chuyển giao quyền sở hữu sau khi coinjoin được thực hiện, và do đó không cần phải thực hiện hành động nào chống lại bên phát hành.



![image](assets/fr/01.webp)



Đối mặt với phương pháp Ricochet, người ta có thể nghĩ rằng phần mềm phân tích chuỗi sẽ đào sâu kiểm tra hơn bốn lần thoát. Tuy nhiên, các nền tảng này gặp phải một vấn đề nan giải trong việc tối ưu hóa ngưỡng phát hiện. Họ cần thiết lập một ngưỡng số lượng bước nhảy mà sau đó họ chấp nhận rằng có khả năng đã xảy ra thay đổi quyền sở hữu và liên kết đến một coinjoin trước đó nên được bỏ qua. Tuy nhiên, việc xác định ngưỡng này rất rủi ro: mỗi lần mở rộng số lượng bước nhảy quan sát được sẽ làm tăng theo cấp số nhân khối lượng kết quả dương tính giả, tức là các cá nhân bị đánh dấu nhầm là người tham gia vào một coinjoin, trong khi thực tế giao dịch được thực hiện bởi người khác. Kịch bản này đặt ra một rủi ro lớn cho các công ty này, vì kết quả dương tính giả dẫn đến sự không hài lòng, có thể khiến khách hàng bị ảnh hưởng chuyển sang đối thủ cạnh tranh. Về lâu dài, một ngưỡng phát hiện quá tham vọng sẽ khiến nền tảng mất nhiều khách hàng hơn so với đối thủ cạnh tranh, điều này có thể đe dọa đến khả năng tồn tại của nền tảng. Do đó, việc tăng số lần thoát quan sát được là rất khó khăn đối với các nền tảng này, và 4 thường là một con số đủ để phản bác lại các phân tích của họ.



Do đó, **trường hợp sử dụng Ricochet phổ biến nhất là khi cần che giấu việc tham gia trước đó vào một giao dịch coinjoin trên UTXO mà bạn sở hữu.** Lý tưởng nhất là tránh chuyển giao bitcoin đã trải qua giao dịch coinjoin sang các tổ chức được quản lý. Tuy nhiên, trong trường hợp không còn lựa chọn nào khác, đặc biệt là khi cần thanh lý gấp bitcoin bằng tiền tệ nhà nước, Ricochet là một giải pháp hiệu quả.



## Ricochet có tác dụng thế nào với Ashigaru?



Ricochet đơn giản là một phương pháp gửi bitcoin cho chính mình, ban đầu được phát minh bởi các nhà phát triển Samurai Wallet. Do đó, hoàn toàn có thể mô phỏng Ricochet theo cách thủ công mà không cần công cụ chuyên dụng. Tuy nhiên, đối với những người muốn tự động hóa quy trình mà vẫn có được kết quả hoàn hảo hơn, công cụ Ricochet có sẵn thông qua ứng dụng Ashigaru (là Samourai fork) là một giải pháp tốt.



Vì Ashigaru tính phí dịch vụ, nên một chiếc Ricochet có giá `100.000 sats` phí dịch vụ, cộng thêm phí mining. Do đó, nên sử dụng Ricochet cho các giao dịch chuyển tiền số lượng lớn.



Ứng dụng Ashigaru cung cấp hai phiên bản Ricochet:





- Ricochet được gia cố, hay còn gọi là "giao hàng so le", mang lại lợi thế là phân bổ phí dịch vụ của Ashigaru cho năm giao dịch liên tiếp. Tùy chọn này cũng đảm bảo mỗi giao dịch được phát sóng vào một thời điểm riêng biệt và được ghi lại trong một khối khác nhau, mô phỏng càng sát càng tốt hành vi của việc thay đổi quyền sở hữu. Mặc dù chậm hơn, phương pháp này được ưa chuộng hơn cho những người không vội vàng, vì nó tối đa hóa hiệu quả của Ricochet bằng cách tăng cường khả năng chống lại phân tích chuỗi;





- Ricochet cổ điển, được thiết kế để thực hiện thao tác nhanh chóng, phát sóng tất cả các giao dịch trong khoảng thời gian ngắn hơn. Do đó, phương pháp này ít bảo mật hơn và ít bị phân tích hơn so với phương pháp tăng cường. Phương pháp này chỉ nên được sử dụng cho các lô hàng khẩn cấp.



## Làm thế nào để thực hiện đòn Ricochet trên Ashigaru?



Việc gửi tiền trên Ashigaru rất đơn giản: chỉ cần kích hoạt tùy chọn tương ứng khi tạo giao dịch gửi tiền. Để bắt đầu, hãy nhấp vào nút `+`, sau đó nhấp vào `Gửi` và chọn tài khoản bạn muốn gửi tiền.



![Image](assets/fr/02.webp)



Điền thông tin giao dịch: số tiền cần gửi và địa chỉ cuối cùng của người nhận sau khi lệnh Ricochet được thực hiện. Sau đó, chọn tùy chọn `Ricochet`.



![Image](assets/fr/03.webp)



Sau đó, bạn có thể chọn giữa hai chế độ Ricochet được thảo luận trong phần lý thuyết: Ricochet cổ điển, trong đó tất cả các giao dịch được bao gồm trong cùng một khối hoặc phân phối theo giai đoạn, giúp cải thiện chất lượng Ricochet nhưng phải trả giá bằng độ trễ dài hơn.



Sau khi đã đưa ra lựa chọn, hãy nhấn vào mũi tên ở cuối màn hình để xác nhận.



![Image](assets/fr/04.webp)



Trên màn hình tiếp theo, bạn sẽ thấy tóm tắt đầy đủ về giao dịch của mình. Đây cũng là nơi bạn có thể điều chỉnh mức phí cho các giao dịch Ricochet theo điều kiện thị trường. Nếu mọi thứ đã ổn, hãy kéo mũi tên màu xanh lá cây để ký và phân phối các giao dịch Ricochet.



![Image](assets/fr/05.webp)



Chờ trong khi các bước nhảy khác nhau chạy tự động.



![Image](assets/fr/06.webp)



Giao dịch của bạn đã được phát thành công.



![Image](assets/fr/07.webp)



Giờ đây, bạn đã hoàn toàn quen thuộc với tùy chọn Ricochet có sẵn trong ứng dụng Ashigaru. Để tìm hiểu thêm, tôi khuyên bạn nên tham gia khóa đào tạo BTC 204 của tôi, khóa học này sẽ hướng dẫn bạn chi tiết cách tăng cường bảo mật onchain.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c