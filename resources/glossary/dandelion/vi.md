---
term: DANDELION
---

Một đề xuất nhằm cải thiện sự riêng tư trong việc định tuyến giao dịch trên mạng Bitcoin để chống lại việc mất danh tính. Trong hoạt động tiêu chuẩn của Bitcoin, các giao dịch ngay lập tức được phát sóng đến nhiều nút. Hiện tượng này có thể cho phép người quan sát liên kết các giao dịch, thường là ẩn danh, với địa chỉ IP. Mục tiêu của BIP156 là giải quyết vấn đề này. Để làm được điều này, nó giới thiệu một giai đoạn bổ sung trong quá trình phát sóng để bảo tồn sự ẩn danh trước khi phát sóng công khai. Vì vậy, Dandelion trước tiên sử dụng giai đoạn "stem" (gốc) nơi giao dịch được gửi qua một đường dẫn ngẫu nhiên của các nút, trước khi được phát sóng đến toàn bộ mạng trong giai đoạn "fluff" (bông). Stem và fluff là những tham chiếu đến hành vi của sự lan truyền giao dịch qua mạng, giống hình dạng của một bông hoa bồ công anh. Phương pháp định tuyến này làm mờ dấu vết dẫn trở lại nút nguồn, khiến việc truy tìm một giao dịch qua mạng trở lại nguồn gốc của nó trở nên khó khăn.

![](../../dictionnaire/assets/36.png)