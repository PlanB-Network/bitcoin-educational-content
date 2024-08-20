---
term: QUY TẮC TIÊU CHUẨN HÓA
---

Quy tắc tiêu chuẩn hóa được mỗi nút Bitcoin áp dụng riêng biệt, bổ sung cho các quy tắc đồng thuận, nhằm định nghĩa cấu trúc của các giao dịch chưa xác nhận mà nó chấp nhận vào mempool và phát sóng cho các nút khác. Do đó, các quy tắc này được cấu hình và thực thi một cách địa phương bởi mỗi nút và có thể khác nhau giữa các nút. Chúng chỉ áp dụng cho các giao dịch chưa xác nhận. Vì vậy, một nút chỉ chấp nhận một giao dịch mà nó coi là không chuẩn nếu giao dịch đó đã được bao gồm trong một khối hợp lệ.

Được lưu ý rằng, đa số các nút giữ nguyên cấu hình mặc định như đã được thiết lập trong Bitcoin Core, do đó tạo ra sự thống nhất về quy tắc tiêu chuẩn hóa trên toàn mạng. Một giao dịch mà, mặc dù tuân thủ các quy tắc đồng thuận nhưng không tuân thủ các quy tắc tiêu chuẩn hóa, sẽ gặp khó khăn trong việc được phát sóng trên mạng. Tuy nhiên, nó vẫn có thể được bao gồm trong một khối hợp lệ nếu nó đạt được một thợ đào. Trên thực tế, những giao dịch này, được gọi là "không chuẩn," thường được truyền trực tiếp đến một thợ đào thông qua các phương tiện bên ngoài mạng ngang hàng Bitcoin. Đây thường là cách duy nhất để xác nhận loại giao dịch này.

Ví dụ, một giao dịch không phân bổ phí là hợp lệ theo các quy tắc đồng thuận và không chuẩn vì chính sách mặc định của Bitcoin Core đối với tham số `minRelayTxFee` là `0.00001` (trong BTC/kB).

> ► *Thuật ngữ "quy tắc mempool" cũng đôi khi được sử dụng để chỉ các quy tắc tiêu chuẩn hóa.*