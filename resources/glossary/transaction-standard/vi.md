---
term: TIÊU CHUẨN GIAO DỊCH
---

Một giao dịch Bitcoin mà, ngoài việc tuân thủ các quy tắc đồng thuận, còn nằm trong các quy tắc chuẩn hóa được thiết lập mặc định trên các nút Bitcoin Core. Các quy tắc chuẩn hóa này được áp đặt riêng lẻ bởi mỗi nút Bitcoin, bổ sung cho các quy tắc đồng thuận, để xác định cấu trúc của các giao dịch chưa được xác nhận mà nó chấp nhận trong mempool của mình và phát sóng cho các nút đồng nghiệp.

Như vậy, các quy tắc này được cấu hình và thực thi một cách địa phương bởi mỗi nút và có thể thay đổi từ nút này sang nút khác. Chúng chỉ áp dụng độc quyền cho các giao dịch chưa được xác nhận. Do đó, một nút chỉ chấp nhận một giao dịch mà nó coi là không chuẩn nếu nó đã được bao gồm trong một khối hợp lệ.

Được lưu ý rằng, đa số các nút giữ nguyên cấu hình mặc định như được thiết lập trong Bitcoin Core, do đó tạo ra sự thống nhất về các quy tắc chuẩn hóa trên toàn mạng. Một giao dịch mà, mặc dù tuân thủ các quy tắc đồng thuận nhưng không tôn trọng các quy tắc chuẩn hóa này, sẽ gặp khó khăn trong việc lan truyền qua mạng. Tuy nhiên, nó vẫn có thể được bao gồm trong một khối hợp lệ nếu nó đạt được một thợ mỏ. Trên thực tế, những giao dịch này, được coi là không chuẩn, thường được truyền trực tiếp đến một thợ mỏ thông qua các phương tiện bên ngoài mạng ngang hàng Bitcoin. Đây thường là cách duy nhất để xác nhận một giao dịch như vậy. Ví dụ, một giao dịch không phân bổ phí là hợp lệ theo các quy tắc đồng thuận và không chuẩn, bởi vì chính sách mặc định của Bitcoin Core cho tham số `minRelayTxFee` là `0.00001` (trong BTC/kB).