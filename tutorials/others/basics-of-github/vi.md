---
name: Cơ bản về GitHub
description: Hiểu biết cơ bản về Git và GitHub
---

![cover](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin, có sẵn bằng càng nhiều ngôn ngữ khác nhau càng tốt. Tất cả nội dung được công bố trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, mang lại cơ hội cho bất kỳ ai đóng góp vào việc làm giàu cho nền tảng. Đóng góp có thể có nhiều hình thức: sửa chữa và hiệu đính các văn bản hiện có, dịch sang ngôn ngữ khác, cập nhật thông tin, hoặc tạo ra các hướng dẫn mới chưa có trên trang web của chúng tôi.

Nếu bạn muốn đóng góp cho Mạng lưới PlanB, bạn sẽ cần sử dụng Git và GitHub. Nếu những công cụ này là mới mẻ với bạn hoặc nếu cách hoạt động của chúng có vẻ mờ ám, đừng hoảng sợ, bài viết này dành cho bạn! Chúng ta sẽ cùng nhau xem xét các nguyên tắc cơ bản của Git và GitHub, cũng như thuật ngữ kỹ thuật liên quan, để bạn có thể sử dụng hiệu quả các công cụ này sau đó.

## Git là gì?

Git là một hệ thống quản lý phiên bản, được thiết kế đặc biệt để quản lý các dự án phần mềm. Được tạo ra vào năm 2005 bởi Linus Torvalds, Git nhanh chóng trở thành tiêu chuẩn trong ngành phát triển phần mềm cho việc quản lý phiên bản. Nhưng điều đó có nghĩa là gì?
![git](assets/1.webp)
Ở cốt lõi, Git cho phép các nhà phát triển theo dõi các thay đổi được thực hiện đối với mã nguồn của một dự án theo thời gian. Điều này có nghĩa là với mỗi thay đổi trong mã, Git ghi lại một phiên bản mới của dự án. Nếu một lỗi xảy ra hoặc nếu một tính năng thử nghiệm không hoạt động như mong đợi, có thể quay trở lại trạng thái trước của mã, giống như một loại máy thời gian cho các tệp.

Một trong những tính năng chính của Git là quản lý nhánh. Một nhánh là một dòng song song mà ở đó các nhà phát triển có thể làm việc độc lập với phần còn lại của dự án. Điều này rất thuận tiện cho việc thêm các tính năng mới hoặc sửa lỗi mà không làm ảnh hưởng đến mã chính. Một khi các sửa đổi được kiểm tra và xác nhận, chúng có thể được hợp nhất với nhánh chính.

Một đặc điểm của Git là khả năng hoạt động theo cách phân tán. Mỗi nhà phát triển có một bản sao đầy đủ của dự án trên ổ cứng máy tính của riêng họ, cho phép họ làm việc ngoại tuyến và sau đó hợp nhất các thay đổi khi có kết nối Internet. Điều này giảm thiểu nguy cơ xung đột và cho phép nhiều nhà phát triển làm việc cùng một lúc trên cùng một dự án mà không làm phiền lẫn nhau.
Ban đầu, Git chủ yếu được thiết kế cho các dự án phát triển phần mềm. Tuy nhiên, nó cũng có thể được sử dụng để quản lý các dự án viết nội dung. Thay vì cộng tác trên mã, chúng ta cộng tác trên văn bản. Và chính phương pháp này mà Mạng lưới PlanB đã áp dụng để quản lý nội dung của mình! Git tạo điều kiện cho việc cộng tác viết các khóa học và hướng dẫn, vì nó cho phép theo dõi chính xác các thay đổi, quản lý phiên bản hiệu quả và cũng cho phép xem xét và cải thiện nội dung bởi các đóng góp viên khác.
## GitHub là gì?

GitHub là một nền tảng quản lý và lưu trữ mã nguồn dựa trên hệ thống quản lý phiên bản Git mà chúng ta vừa thảo luận. Ra mắt vào năm 2008, GitHub nhanh chóng trở nên phổ biến và đã trở thành một điểm tham chiếu thiết yếu cho các nhà phát triển trên toàn thế giới. Nhưng GitHub khác biệt với Git như thế nào, và tại sao nó lại quan trọng đối với phương pháp sản xuất nội dung của chúng ta?
![github](assets/2.webp)
Đầu tiên, quan trọng là phải hiểu rằng GitHub được xây dựng dựa trên Git (mà chúng ta đã thảo luận trong phần trước). Trong khi Git là công cụ theo dõi các thay đổi mã, GitHub là dịch vụ trực tuyến lưu trữ, chia sẻ và quản lý mã này.

Hãy tưởng tượng Git như một loại sổ tay mà mỗi nhà phát triển sử dụng trên máy tính của riêng họ để ghi lại tất cả các thay đổi trong dự án của họ. GitHub, ngược lại, giống như một thư viện công cộng nơi tất cả những sổ tay này có thể được chia sẻ, so sánh và kết hợp.
Sự khác biệt cơ bản giữa Git và GitHub nằm ở chức năng của chúng: Git là công cụ được sử dụng một cách địa phương bởi mỗi nhà phát triển để quản lý các phiên bản mã của họ, trong khi GitHub là nền tảng trực tuyến chứa đựng các phiên bản này và tạo điều kiện cho sự hợp tác.

GitHub không chỉ đơn thuần là một dịch vụ lưu trữ mã. Đó là một nền tảng hợp tác cho phép các nhà phát triển làm việc cùng nhau một cách hiệu quả. Và thực sự, Mạng PlanB sử dụng nền tảng này để lưu trữ không chỉ tất cả mã lực cho trang web mà còn, và đây là điều chúng ta quan tâm, tất cả nội dung (hướng dẫn, đào tạo, tài nguyên...).

## Một số Thuật Ngữ Kỹ Thuật

Trên Git và GitHub, bạn sẽ gặp các lệnh và tính năng mà tên có thể có vẻ phức tạp. Trong phần cuối này, tôi cung cấp các định nghĩa đơn giản để hiểu các thuật ngữ kỹ thuật mà bạn có thể gặp khi sử dụng Git và GitHub:

- **Fetch origin:** Lệnh lấy thông tin và thay đổi gần đây từ một kho lưu trữ từ xa mà không hợp nhất chúng với công việc địa phương của bạn. Nó cập nhật kho lưu trữ địa phương của bạn với các nhánh và cam kết mới có mặt trong kho lưu trữ từ xa.

- **Pull origin:** Lệnh lấy cập nhật từ một kho lưu trữ từ xa và ngay lập tức tích hợp chúng vào nhánh địa phương của bạn để đồng bộ hóa nó. Điều này kết hợp các bước fetch và merge thành một lệnh duy nhất.
- **Sync Fork:** Một tính năng trên GitHub cho phép bạn cập nhật fork của một dự án với những thay đổi mới nhất từ kho lưu trữ nguồn. Điều này đảm bảo rằng bản sao của dự án của bạn luôn được cập nhật với sự phát triển chính.
- **Push origin:** Lệnh được sử dụng để gửi các thay đổi địa phương của bạn đến một kho lưu trữ từ xa.

- **Pull Request:** Một yêu cầu được gửi bởi một người đóng góp để chỉ ra rằng họ đã đẩy thay đổi vào một nhánh trong một kho lưu trữ từ xa và mong muốn những thay đổi này được xem xét và có khả năng được hợp nhất vào nhánh chính của kho lưu trữ.

- **Commit:** Lưu các thay đổi của bạn. Một commit giống như một bức ảnh tức thì của công việc của bạn tại một thời điểm nhất định, cho phép giữ lại lịch sử của các thay đổi. Mỗi commit bao gồm một thông điệp mô tả giải thích những gì đã được sửa đổi.

- **Branch:** Một phiên bản song song của kho lưu trữ, cho phép bạn làm việc trên các thay đổi mà không ảnh hưởng đến nhánh chính (thường được gọi là "main" hoặc "master"). Các nhánh tạo điều kiện cho việc phát triển các tính năng mới và sửa lỗi mà không có nguy cơ làm gián đoạn mã ổn định.

- **Merge:** Việc hợp nhất bao gồm việc tích hợp các thay đổi từ một nhánh này sang nhánh khác. Nó được sử dụng, ví dụ, để thêm các thay đổi từ một nhánh làm việc vào nhánh chính, cho phép thêm các đóng góp khác nhau.

- **Fork:** Forking một kho lưu trữ có nghĩa là tạo một bản sao của kho lưu trữ đó trên tài khoản GitHub của riêng bạn, cho phép bạn làm việc trên dự án mà không ảnh hưởng đến kho lưu trữ gốc. Fork có thể đi con đường riêng và trở thành một dự án khác biệt từ dự án gốc, hoặc nó có thể đồng bộ thường xuyên với dự án gốc để đóng góp cho nó.

- **Clone:** Cloning một kho lưu trữ có nghĩa là tạo một bản sao địa phương trên máy tính của bạn, cho phép bạn truy cập vào tất cả các tệp và lịch sử. Điều này cho phép bạn làm việc trực tiếp trên dự án một cách địa phương.

- **Repository:** Không gian lưu trữ cho một dự án trên GitHub. Một kho lưu trữ chứa tất cả các tệp dự án cũng như lịch sử của tất cả các thay đổi đã được thực hiện đối với nó. Đó là cơ sở của lưu trữ và hợp tác trên GitHub.

- **Issue:** Một công cụ để theo dõi nhiệm vụ và lỗi trên GitHub. Issues cho phép báo cáo vấn đề, đề xuất cải tiến, hoặc thảo luận về các tính năng mới. Mỗi issue có thể được gán, gắn nhãn, và bình luận.

Danh sách này rõ ràng không phải là toàn diện. Có nhiều thuật ngữ kỹ thuật khác đặc thù cho Git và GitHub. Tuy nhiên, những thuật ngữ được đề cập ở đây là những thuật ngữ chính mà bạn sẽ thường xuyên gặp.
Sau khi đọc bài viết này, có thể một số khía cạnh của Git và GitHub vẫn còn mơ hồ đối với bạn. Tôi khuyến khích bạn bắt đầu sử dụng chính những công cụ này. Thực hành thường là cách tốt nhất để hiểu cách máy móc hoạt động! Và để bắt đầu, bạn có thể khám phá 2 hướng dẫn khác sau đây:
**[Tạo tài khoản GitHub của bạn](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Thiết lập Môi trường Cục bộ của Bạn để Đóng góp vào Mạng PlanB](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**