---
name: Breez - POS
description: Breez giúp bạn dễ dàng thu tiền thanh toán bằng bitcoin cho doanh nghiệp của mình.
---

![cover](assets/cover.webp)



Kể từ đại dịch COVID-19, thanh toán kỹ thuật số không tiếp xúc đã trở nên phổ biến, ngay cả ở những cửa hàng nhỏ nhất. Trong thời gian này, nhiều doanh nghiệp đã khám phá ra tính thực tiễn của các giải pháp Bitcoin Cash, cho phép họ nhận thanh toán từ khắp nơi trên thế giới. Tuy nhiên, các giải pháp này đôi khi khó sử dụng hoặc không phù hợp với các doanh nghiệp nhỏ. Trong hướng dẫn này, chúng ta sẽ tìm hiểu về thiết bị đầu cuối thanh toán Breez, một giải pháp nổi bật với tính dễ sử dụng, đồng thời cho phép bạn kiểm soát hoàn toàn việc quản lý Bitcoin của mình.



## Cài đặt Breez POS



Breez POS là dịch vụ tự quản lý do Breez wallet cung cấp. Tiện ích của dịch vụ này là cho phép các thương nhân thu tiền qua Bitcoin mà vẫn duy trì giao diện đơn giản, rất giống với các ví Lightning khác. Breez POS có sẵn trên các nền tảng tải xuống [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) và [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS).



![download](assets/fr/01.webp)



![setup](assets/fr/12.webp)



⚠️ Xin lưu ý rằng các ứng dụng này vẫn đang trong quá trình phát triển và có thể có một số lỗi trong quá trình sử dụng các chức năng. Chúng tôi khuyến nghị bạn nên sử dụng ở mức vừa phải.



Với ứng dụng này, Breez cung cấp cho bạn quyền kiểm soát hoàn toàn đối với cấu hình mạng và cài đặt phí, đồng thời đảm bảo quyền tự chủ của bạn trong việc quản lý bitcoin.



Bạn có thể khám phá các tùy chọn Breez wallet khác nhau bằng cách làm theo hướng dẫn bên dưới. Bước này sẽ giúp bạn hiểu rõ hơn về hệ sinh thái điểm bán hàng và áp dụng các phương pháp tối ưu để bảo mật hiệu quả số bitcoin liên quan đến seed của bạn.



https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Sử dụng Breez POS



Trong hướng dẫn này, chúng tôi sẽ tập trung vào phần "*Điểm bán hàng*" để giúp bạn hiểu cách tích hợp phần này làm phương tiện thanh toán trong doanh nghiệp của mình.



Điểm bán hàng là một phần không thể thiếu của danh mục đầu tư Breez và chủ yếu dựa vào Lightning Network để thu tiền.



Trong menu "*Điểm bán hàng*", bạn có giao diện trực tiếp để thu tiền. Giao diện này được chia thành hai phần:



### Ghi nợ trực tiếp



Phần đầu tiên là bàn phím ghi nợ trực tiếp. Giao diện này rất tiện lợi để thu toàn bộ khoản thanh toán khi bạn biết tổng số tiền khách hàng đã mua, hoặc khi doanh nghiệp của bạn không cần danh mục sản phẩm cố định (ví dụ: dịch vụ tự do).



![keyboard](assets/fr/02.webp)



Để sử dụng Breez POS lần đầu tiên, bạn sẽ cần thanh toán hơn 2.500 satoshi (khoảng 3 euro theo tỷ giá hối đoái hiện tại). Số tiền này, chỉ được thanh toán trong lần rút tiền đầu tiên của bạn, thể hiện chi phí tạo kênh thanh toán để bạn có thể giao tiếp với các nút Lightning Network khác và gửi/nhận satoshi.



![channel_fee](assets/fr/03.webp)


### Danh mục sản phẩm



Phần thứ hai là danh mục sản phẩm. Giao diện này lý tưởng khi bạn có danh mục sản phẩm với giá được định sẵn. Tại đây, bạn có thể cấu hình trước sản phẩm và sau đó sử dụng chúng để xuất hóa đơn generate nhằm cải thiện khả năng truy xuất nguồn gốc biên lai thu tiền.



![items](assets/fr/04.webp)



Bạn có thể cấu hình thủ công từng mục từ giao diện này bằng cách nhấp vào nút "**Plus**" rồi xác định tên, giá và mã định danh cho mục này.



![add_items](assets/fr/05.webp)



Sau đó, bạn có thể thêm nó và xác định số lượng để thu khoản thanh toán liên quan.



Khi danh mục của bạn khá lớn, việc thêm từng sản phẩm có thể trở nên phức tạp. Để thực hiện việc này, trong phần **Tùy chọn > Cài đặt Điểm bán hàng**, từ menu "Danh sách mặt hàng", bạn có thể tự động nhập và xuất danh sách mặt hàng từ tệp CSV.



![import](assets/fr/07.webp)



Trong cùng phần này, bạn có thể xác định thời hạn hiệu lực của hóa đơn Lightning. Từ giờ trở đi, đối với tất cả hóa đơn, khách hàng của bạn có `N` giây để thanh toán, nếu không bạn sẽ phải tạo lại hóa đơn Lightning mới.



![invoice_time](assets/fr/08.webp)



Với tư cách là người quản lý, bạn có thể tăng cường bảo mật cho bitcoin của mình bằng cách thêm mật khẩu bắt buộc cho tất cả các khoản thanh toán từ wallet của bạn. Tính năng này đặc biệt hữu ích khi bạn không phải là người duy nhất quản lý cửa hàng của mình.



![manager](assets/fr/09.webp)



Trong menu **Giao dịch**, bạn sẽ thấy danh sách tất cả các khoản thanh toán đã thu thập. Bạn cũng có thể lọc kết quả theo một khoảng thời gian cụ thể bằng cách nhấp vào nút **Lịch**.



![transactions](assets/fr/10.webp)



Bạn cũng có thể xem tóm tắt hàng ngày về doanh số bán hàng và tổng số tiền thu được bằng cách nhấp vào nút **Tài liệu**.



![summary](assets/fr/11.webp)



Giờ đây, bạn đã nắm rõ toàn bộ tính năng điểm bán hàng mà ứng dụng Breez cung cấp để tích hợp liền mạch Bitcoin vào doanh nghiệp của mình. Nếu bạn thấy hướng dẫn này hữu ích, chúng tôi khuyên bạn nên xem hướng dẫn về be-BOP, một nền tảng thương mại điện tử cho phép bạn nhận thanh toán bằng bitcoin và kiếm tiền từ doanh nghiệp của mình.



https://planb.academy/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa