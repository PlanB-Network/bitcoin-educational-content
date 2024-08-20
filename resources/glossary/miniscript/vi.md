---
term: MINISCRIPT
---

Khung làm việc được thiết kế để cung cấp một khung cho việc lập trình các script một cách an toàn trên Bitcoin. Ngôn ngữ gốc của Bitcoin được gọi là script. Nó khá phức tạp để sử dụng trong thực tế, đặc biệt là cho các ứng dụng tinh vi và tùy chỉnh. Trên hết, việc xác minh giới hạn của một script là rất khó khăn. Miniscript sử dụng một tập con của Bitcoin script để đơn giản hóa việc tạo ra, phân tích và xác minh chúng. Mỗi miniscript tương đương 1 cho 1 với một script gốc. Một ngôn ngữ chính sách thân thiện với người dùng được sử dụng, sau đó được biên dịch thành miniscript, để cuối cùng tương ứng với một script gốc.

![](../../dictionnaire/assets/30.png)

Miniscript do đó cho phép các nhà phát triển xây dựng các script phức tạp một cách an toàn và đáng tin cậy hơn. Các tính chất cơ bản của Miniscript như sau:
* Nó cho phép phân tích tĩnh script, bao gồm các điều kiện chi tiêu mà nó cho phép và chi phí về nguồn lực;
* Nó cho phép tạo ra các script tuân thủ đồng thuận;
* Nó cho phép phân tích liệu các con đường chi tiêu khác nhau có tuân thủ các quy tắc tiêu chuẩn của các nút hay không;
* Nó thiết lập một tiêu chuẩn chung, dễ hiểu và có thể kết hợp, cho tất cả phần mềm và phần cứng ví.

Dự án Miniscript được khởi xướng vào năm 2018 bởi Peter Wuille, Andrew Poelstra, và Sanket Kanjalkar, thông qua công ty Blockstream. Miniscript đã được thêm vào ví Bitcoin Core ở chế độ chỉ xem vào tháng 12 năm 2022 với phiên bản 24.0, và sau đó hoàn toàn vào tháng 5 năm 2023 với phiên bản 25.0.