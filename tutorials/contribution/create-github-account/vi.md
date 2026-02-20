---
name: Tài Khoản GitHub
description: Cách tạo tài khoản của riêng bạn trên GitHub?
---

![cover](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn học liệu hàng đầu về Bitcoin bằng nhiều ngôn ngữ nhất có thể. Toàn bộ nội dung được đăng tải trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, tạo điều kiện cho bất kỳ ai cũng có thể tham gia đóng góp và làm phong phú thêm kho kiến thức chung này. Đóng góp có thể dưới nhiều hình thức: sửa lỗi và soát lỗi các văn bản hiện có, dịch sang các ngôn ngữ khác, cập nhật thông tin hoặc tạo các hướng dẫn mới chưa có trên trang web của chúng tôi.

Nếu bạn muốn đóng góp cho Plan ₿ Academy, bạn sẽ cần sử dụng Git và GitHub, vì vậy, nếu bạn chưa quen thuộc với những công cụ này hoặc thấy cách hoạt động của chúng khó hiểu, đừng lo lắng, bài viết này dành cho bạn! Hãy cùng xem xét những kiến ​​thức cơ bản về Git và GitHub, cũng như các thuật ngữ kỹ thuật liên quan, để bạn có thể sử dụng chúng một cách hiệu quả sau này.

## Git là gì?

Git là một hệ thống quản lý phiên bản, được thiết kế đặc biệt để quản lý các dự án phần mềm. Được tạo ra vào năm 2005 bởi Linus Torvalds, Git nhanh chóng trở thành tiêu chuẩn trong ngành phát triển phần mềm cho việc quản lý phiên bản. Nhưng chính xác thì nó có nghĩa là gì?

![git](assets/11.webp)

Về cơ bản, Git cho phép các nhà phát triển theo dõi những thay đổi được thực hiện đối với mã nguồn của dự án theo thời gian. Điều này có nghĩa là với mỗi thay đổi trong mã, Git sẽ ghi lại một phiên bản mới của dự án. Nếu xảy ra lỗi hoặc nếu một tính năng thử nghiệm không hoạt động như mong đợi, có thể quay lại trạng thái trước đó của mã, giống như một loại cỗ máy thời gian, nhưng dành cho các tệp.

Một trong những tính năng quan trọng của Git là quản lý nhánh. Nhánh (branch) là một dạng đường thẳng song song, nơi các nhà phát triển có thể làm việc độc lập với phần còn lại của dự án. Điều này giúp việc bổ sung các tính năng mới hoặc sửa lỗi trở nên dễ dàng hơn mà không làm ảnh hưởng đến mã nguồn chính. Sau khi các sửa đổi được kiểm tra và xác nhận, chúng có thể được hợp nhất với nhánh chính (main branch).

Một trong những đặc điểm độc đáo của Git là khả năng hoạt động phân tán. Mỗi nhà phát triển có một bản sao hoàn chỉnh của dự án trên ổ cứng máy tính của riêng họ, cho phép họ làm việc ngoại tuyến và hợp nhất các thay đổi sau này khi kết nối Internet. Điều này giảm thiểu nguy cơ xung đột và cho phép nhiều nhà phát triển làm việc đồng thời trên cùng một dự án mà không gây cản trở lẫn nhau.
Ban đầu, Git chủ yếu được thiết kế cho các dự án phát triển phần mềm. Tuy nhiên, nó cũng có thể được sử dụng để quản lý các dự án viết nội dung. Thay vì cộng tác trên mã, chúng ta cộng tác trên văn bản. Và chính phương pháp này mà Plan ₿ Academy đã áp dụng để quản lý nội dung của mình! Git tạo điều kiện thuận lợi cho việc cộng tác trong việc viết các khóa học và hướng dẫn, vì nó cho phép theo dõi chính xác các thay đổi, quản lý phiên bản hiệu quả và cũng cho phép xem xét và cải thiện nội dung bởi những người đóng góp khác.

## GitHub là gì?

GitHub là một nền tảng quản lý và lưu trữ mã nguồn dựa trên hệ thống kiểm soát phiên bản Git mà chúng ta vừa thảo luận. Ra mắt năm 2008, GitHub nhanh chóng trở nên phổ biến và trở thành một công cụ tham khảo thiết yếu cho các nhà phát triển trên toàn thế giới. Nhưng GitHub khác với Git như thế nào, và tại sao nó lại quan trọng đến vậy trong phương pháp sản xuất nội dung của chúng ta?

![github](assets/12.webp)

Trước hết, chúng ta phải hiểu rằng GitHub được xây dựng trên nền tảng Git (như đã đề cập ở phần trước). Trong khi Git là công cụ theo dõi các thay đổi mã, thì GitHub là dịch vụ trực tuyến lưu trữ, chia sẻ và quản lý mã này.

Hãy tưởng tượng Git như một cuốn nhật ký mà mỗi lập trình viên sử dụng trên máy tính cá nhân để ghi lại tất cả các thay đổi trong dự án của họ. Mặt khác, GitHub giống như một thư viện công cộng, nơi tất cả các nhật ký này có thể được chia sẻ, so sánh và kết hợp.

Sự khác biệt cơ bản giữa Git và GitHub nằm ở chức năng của chúng: Git là công cụ được mỗi nhà phát triển sử dụng cục bộ (locally) để quản lý các phiên bản mã nguồn của mình, trong khi GitHub là nền tảng trực tuyến lưu trữ các phiên bản này và tạo điều kiện thuận lợi cho sự hợp tác.

GitHub không chỉ đơn thuần là một dịch vụ lưu trữ mã nguồn. Đó là một nền tảng hợp tác cho phép các nhà phát triển làm việc cùng nhau một cách hiệu quả. Và thực tế, Plan ₿ Academy sử dụng nền tảng này để lưu trữ không chỉ toàn bộ mã nguồn vận hành trang web mà còn cả, và đây là điều chúng ta quan tâm, toàn bộ nội dung (hướng dẫn, đào tạo, tài nguyên...).

## Một số thuật ngữ kỹ thuật

Trên Git và GitHub, bạn sẽ gặp các lệnh và tính năng có tên gọi khá phức tạp. Trong phần cuối này, tôi sẽ cung cấp một số định nghĩa đơn giản để giúp bạn hiểu các thuật ngữ kỹ thuật có thể gặp phải khi sử dụng Git và GitHub:

- **`Repository`:** là kho lưu trữ cho một dự án trên GitHub. Một repository chứa tất cả các tệp dự án cũng như lịch sử của tất cả các thay đổi đã được thực hiện đối với dự án đó. Đây là nền tảng của việc lưu trữ và cộng tác trên GitHub.

- **`Fork`:** Tạo một bản sao của repository đó trên tài khoản GitHub của riêng bạn, cho phép bạn làm việc trên dự án mà không ảnh hưởng đến repository gốc. Bản sao này có thể phát triển độc lập và trở thành một dự án khác với dự án gốc, hoặc nó có thể thường xuyên đồng bộ hóa với dự án gốc để đóng góp vào dự án đó.

- **`Fetch origin`:** Lệnh lấy thông tin và những thay đổi gần đây từ repository từ xa mà không hợp nhất chúng với công việc cục bộ của bạn. Nó cập nhật repository cục bộ của bạn với các nhánh và commit mới có trong repository từ xa.

- **`Pull origin`:** Lệnh này lấy các bản cập nhật từ repository từ xa và ngay lập tức tích hợp chúng vào nhánh cục bộ của bạn để đồng bộ hóa. Nó kết hợp các bước tìm nạp và hợp nhất thành một lệnh duy nhất.

- **`Sync Fork`:** Một tính năng trên GitHub cho phép bạn cập nhật bản fork dự án của mình với những thay đổi mới nhất từ repository nguồn. Điều này đảm bảo bản fork luôn được cập nhật với quá trình phát triển chính.

- **`Push origin`:** Lệnh được sử dụng để gửi các thay đổi cục bộ của bạn đến repository từ xa.

- **`Pull Request`:** Yêu cầu được gửi bởi một người đóng góp để cho biết họ đã gửi các thay đổi lên một nhánh trong repository từ xa và muốn các thay đổi này được xem xét và có thể được hợp nhất vào nhánh chính của repository.

- **`Commit`:** Lưu lại các thay đổi của bạn. Một commit giống như một bản sao lại trạng thái về công việc của bạn tại một thời điểm nhất định, cho phép lưu giữ lịch sử các thay đổi. Mỗi commit mô tả giải thích những gì đã được sửa đổi.

- **`Branch`:** Một phiên bản song song của repository, cho phép bạn thực hiện các thay đổi mà không ảnh hưởng đến nhánh chính (thường được gọi là "main" hoặc "master"). Các nhánh giúp phát triển các tính năng mới và sửa lỗi mà không làm gián đoạn mã nguồn ổn định hiện tại.

- **`Merge`:** "Merge" bao gồm việc tích hợp các thay đổi từ một nhánh vào một nhánh khác. Ví dụ, nó được sử dụng để thêm các thay đổi từ một nhánh làm việc vào nhánh chính, cho phép thêm các đóng góp khác nhau.

- **`Clone`:** Tạo một bản sao cục bộ trên máy tính của bạn, cho phép bạn truy cập vào tất cả các tệp và lịch sử. Điều này giúp bạn có thể làm việc trực tiếp trên dự án ngay tại máy tính của mình.

- **`Issue`:** Một công cụ để theo dõi các tác vụ và lỗi trên GitHub. Chức năng "Issues" cho phép báo cáo sự cố, đề xuất cải tiến hoặc thảo luận về các tính năng mới. Mỗi vấn đề có thể được chỉ định, gắn nhãn và bình luận.

Danh sách này không phải là đầy đủ nhất. Có rất nhiều thuật ngữ kỹ thuật khác đặc thù cho Git và GitHub. Tuy nhiên, những thuật ngữ được đề cập ở đây là những thuật ngữ chính mà bạn sẽ thường xuyên gặp.

Sau khi đọc bài viết này, có thể một số khía cạnh về Git và GitHub vẫn chưa rõ ràng với bạn, vì vậy tôi khuyến khích bạn bắt đầu tự mình sử dụng các công cụ này. Thực hành thường là cách tốt nhất để hiểu cách thức hoạt động của máy móc! Và để bắt đầu, bạn có thể tham khảo thêm 2 hướng dẫn khác:

## Cách tạo tài khoản GitHub

Nếu bạn muốn đóng góp cho Plan ₿ Academy, bạn sẽ cần một tài khoản GitHub. Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn từng bước cách tạo tài khoản của riêng mình, thiết lập và bảo mật đúng cách.

- Truy cập [https://github.com/signup](https://github.com/signup). 
- Nhập địa chỉ email của bạn, rồi nhấn `Continue`:
![github](assets/1.webp)
- Chọn một mật khẩu mạnh, rồi nhấn `Continue`:
![github](assets/2.webp)
- Tiếp theo, chọn tên người dùng cho mình. Bạn có thể tiết lộ danh tính thực của mình, hoặc sử dụng một bí danh. Rồi nhấn `Continue`:
![github](assets/3.webp)
- Hoàn thành Captcha:
![github](assets/4.webp)
- Một email chứa mã xác nhận sẽ được gửi cho bạn; bạn sẽ cần nhập nó để hoàn tất việc tạo tài khoản:
![github](assets/5.webp)
- Điền vào các câu hỏi nếu bạn muốn GitHub hướng dẫn bạn sử dụng các công cụ cụ thể, hoặc nhấn vào `Skip personalization` để bỏ qua:
![github](assets/6.webp)
- Chọn gói miễn phí bằng cách nhấn nút `Continue for free`:
![github](assets/7.webp)
- Sau đó, bạn sẽ được chuyển hướng đến bảng điều khiển của mình.
- Nếu muốn, bạn có thể tùy chỉnh tài khoản của mình bằng cách nhấn vào hình ảnh hồ sơ của mình ở góc trên bên phải của màn hình, sau đó truy cập vào menu `Settings`:
![github](assets/8.webp)
- Trong phần này, bạn có tùy chọn thêm hình ảnh hồ sơ mới, chọn tên, thêm tiểu sử của mình, hoặc thêm liên kết đến trang web cá nhân của bạn:
![github](assets/9.webp)
- Tôi cũng khuyên bạn nên truy cập menu `Password and authentication` để thiết lập xác thực 2 yếu tố:
![github](assets/10.webp)
