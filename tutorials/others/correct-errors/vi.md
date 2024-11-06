---
name: Đóng Góp - Sửa Lỗi
description: Làm thế nào để sửa một lỗi trên Mạng PlanB?
---
![cover](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin bằng càng nhiều ngôn ngữ khác nhau càng tốt. Tất cả nội dung được công bố trên trang web là mã nguồn mở và được lưu trữ trên GitHub, điều này cho phép bất kỳ ai cũng có thể tham gia vào việc làm giàu cho nền tảng. Sự đóng góp có thể có nhiều hình thức: sửa chữa và đọc lại các văn bản hiện có, dịch sang ngôn ngữ khác, cập nhật thông tin, hoặc tạo mới các hướng dẫn chưa có trên trang web của chúng tôi.

Nếu, trong khi tham khảo một trong những nội dung giáo dục của chúng tôi (hướng dẫn, đào tạo, tài nguyên...), bạn phát hiện ra một lỗi, dù đó là lỗi chính tả, ngữ pháp, một lỗi dịch nhỏ trong ngôn ngữ mẹ đẻ của bạn, hay thậm chí một lỗi đánh máy, chúng tôi sẽ rất biết ơn nếu bạn có thể đề xuất một sửa đổi nhanh chóng bởi chính bạn.

Hướng dẫn này sẽ dẫn dắt bạn từng bước qua quá trình sửa những lỗi nhỏ này. Đây là một hướng dẫn dành cho người mới bắt đầu, những người không muốn lấn sâu vào những phức tạp của Git. Tuy nhiên, nếu bạn thoải mái với Git, đây là một tóm tắt nhanh: bạn chỉ cần fork [kho dữ liệu của Mạng PlanB](https://github.com/PlanB-Network/bitcoin-educational-content), thực hiện thay đổi trên một nhánh riêng biệt, và gửi một Pull Request đối với nhánh `dev` của kho lưu trữ gốc.

Xin lưu ý rằng nếu bạn dự định thực hiện một bản xem xét và sửa đổi toàn diện của một tài liệu, đặc biệt là dịch nội dung, tôi mời bạn tham khảo hướng dẫn chi tiết hơn này.

https://planb.network/tutorials/others/content-review-tutorial

 Ở đây, chúng tôi chỉ tập trung vào cách thực hiện một sửa đổi nhanh cho một lỗi nhỏ.

- Đầu tiên, bạn cần có một tài khoản trên GitHub. Nếu bạn không biết cách tạo một tài khoản, chúng tôi đã tạo một hướng dẫn chi tiết để hướng dẫn bạn.

https://planb.network/tutorials/others/create-github-account


- Truy cập vào [kho GitHub của PlanB dành riêng cho dữ liệu](https://github.com/PlanB-Network/bitcoin-educational-content):
![typos](assets/01.webp)
- Tại đây, bạn sẽ tìm thấy tất cả nội dung của chúng tôi được tổ chức theo phần.
- Nếu bạn muốn chỉnh sửa một hướng dẫn, ví dụ, hãy vào thư mục `tutorials`:
![typos](assets/02.webp)
- Bạn sẽ tìm thấy các loại hướng dẫn khác nhau trên trang web của chúng tôi. Ví dụ, nếu bạn muốn chỉnh sửa một hướng dẫn trong danh mục `Privacy`, hãy nhấp vào thư mục tương ứng:
![typos](assets/03.webp)
- Sau đó chọn thư mục tương ứng với nội dung bạn muốn sửa:
![typos](assets/04.webp)
- Trong mỗi thư mục nội dung, bạn sẽ tìm thấy dữ liệu có sẵn bằng các ngôn ngữ khác nhau. Ví dụ, tệp `en.md` tương ứng với phiên bản tiếng Anh của hướng dẫn, trong khi tệp `fr.md` đại diện cho phiên bản tiếng Pháp. Chọn tệp tương ứng với ngôn ngữ bạn muốn chỉnh sửa: ![typos](assets/05.webp)
- Bạn sẽ đến trang GitHub của nội dung. Đảm bảo bạn đang ở trên tài liệu bạn muốn chỉnh sửa: ![typos](assets/06.webp)
- Nhấp vào biểu tượng bút chì nhỏ ở góc trên bên trái: ![typos](assets/07.webp)
- Nếu bạn chưa bao giờ đóng góp nội dung cho Mạng PlanB trước đây, bạn sẽ cần tạo fork của kho lưu trữ gốc. Fork một kho lưu trữ có nghĩa là tạo một bản sao của kho lưu trữ đó trên tài khoản GitHub của riêng bạn, điều này cho phép bạn làm việc trên dự án mà không ảnh hưởng đến kho lưu trữ gốc. Nhấp vào nút `Fork this repository`: ![typos](assets/08.webp)
- Bạn sẽ đến trang chỉnh sửa của GitHub: ![typos](assets/09.webp)- Hãy chỉnh sửa văn bản để sửa các lỗi bạn đã phát hiện. Đừng ngần ngại, bạn hiện đang ở trên fork của riêng mình, vì vậy điều này sẽ không thay đổi bất cứ điều gì trên trang web của PlanB Network vào lúc này. Ví dụ, ở đây, hãy tưởng tượng rằng tôi đã sửa từ "entrées" vì nó có lỗi chính tả: ![typos](assets/10.webp)
- Một khi bạn hoàn thành việc sửa đổi tài liệu này, bạn có thể nhấn vào nút màu xanh `Commit Changes...`. Một commit giống như một bức ảnh tức thì của công việc của bạn tại một thời điểm nhất định, cho phép giữ lại lịch sử của các thay đổi: ![typos](assets/11.webp)
- Thêm tiêu đề cho các sửa đổi của bạn, cũng như một mô tả ngắn gọn: ![typos](assets/12.webp)
- Nhấn vào nút màu xanh `Propose changes`: ![typos](assets/13.webp)
- Bạn sẽ đến trang tóm tắt tất cả các thay đổi của bạn: ![typos](assets/14.webp)
- Kéo xuống, bạn có thể thấy các sửa đổi cụ thể mà bạn đã thực hiện: ![typos](assets/15.webp)
- Nếu mọi thứ phù hợp với bạn và bạn đã hoàn thành các sửa đổi của mình, bạn có thể nhấn vào nút màu xanh `Create Pull Request`: ![typos](assets/16.webp)
- Bạn sẽ đến trang PR. Một Pull Request là một yêu cầu được gửi bởi một người đóng góp để chỉ ra rằng họ đã đẩy các sửa đổi trên một nhánh trong một kho lưu trữ từ xa và họ mong muốn các sửa đổi này được xem xét và có khả năng được hợp nhất vào nhánh chính của kho lưu trữ: ![typos](assets/17.webp)
- Bạn có thể thêm tiêu đề và một mô tả ngắn gọn cho PR của bạn: ![typos](assets/18.webp)
- Nếu mọi thứ đều ổn với bạn, bạn có thể nhấn vào nút màu xanh `Create Pull Request`: ![typos](assets/19.webp)
- Xin chúc mừng, PR của bạn đã được gửi! Bạn có thể theo dõi tiến trình của nó trong tab `Pull requests` trên [kho lưu trữ GitHub của PlanB Network](https://github.com/PlanB-Network/bitcoin-educational-content/pulls) :![typos](assets/20.webp)
Cảm ơn bạn rất nhiều vì đã đóng góp! Nếu bạn muốn thực hiện các loại đóng góp khác cho PlanB Network như viết nội dung hoặc dịch thuật, đừng ngần ngại xem các hướng dẫn khác trong mục "Đóng góp".

https://planb.network/tutorials/others


