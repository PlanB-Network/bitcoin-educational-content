---
term: HASHCASH
---

HashCash là một hệ thống chứng minh công việc được thiết kế bởi Adam Back vào năm 1997 nhằm chống lại spam và các cuộc tấn công DoS. Nó dựa trên nguyên tắc rằng người gửi phải thực hiện một nhiệm vụ tính toán (cụ thể là tìm kiếm một va chạm một phần trên một hàm băm mật mã) để chứng minh công việc của họ. Nhiệm vụ này tốn kém về thời gian và năng lượng cho người gửi, nhưng việc xác minh kết quả bởi người nhận lại nhanh chóng và đơn giản. Giao thức này đã chứng minh đặc biệt phù hợp để chống lại spam trong giao tiếp email, vì nó tạo ra gánh nặng tối thiểu cho người dùng hợp pháp trong khi đặt ra một trở ngại đáng kể cho người gửi spam. Thực tế, việc gửi một email đơn lẻ yêu cầu vài giây tính toán, nhưng việc sao chép thao tác này hàng triệu lần trở nên cực kỳ tốn kém về năng lượng và thời gian, thường làm mất đi lợi ích kinh tế của các chiến dịch spam, dù chúng có mục đích tiếp thị hay ác ý. Hơn nữa, nó cho phép bảo tồn sự ẩn danh của người gửi.

HashCash nhanh chóng được nhóm cypherpunks chấp nhận, những người đang tìm cách phát triển một hệ thống tiền tệ điện tử ẩn danh mà không cần trung gian. Thực sự, sự đổi mới của Adam Back đã giới thiệu khái niệm về sự khan hiếm trong thế giới số lần đầu tiên. Khái niệm chứng minh công việc sau đó được tìm thấy trong một số hệ thống tiền tệ điện tử trước Bitcoin, bao gồm:
* b-money của Wei Dai được công bố vào năm 1998;
* R-POW của Hal Finney được công bố vào năm 2004;
* BitGold của Nick Szabo được công bố vào năm 2005.

Nguyên tắc của HashCash cũng được tìm thấy trong giao thức Bitcoin, nơi nó được sử dụng như một cơ chế bảo vệ chống lại các cuộc tấn công Sybil.