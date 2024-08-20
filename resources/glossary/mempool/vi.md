---
term: MEMPOOL
---

Là sự kết hợp của hai từ "memory" (bộ nhớ) và "pool" (nhóm). Điều này ám chỉ một không gian ảo nơi mà các giao dịch Bitcoin đang chờ được bao gồm trong một khối được nhóm lại với nhau. Khi một giao dịch được tạo ra và phát sóng trên mạng Bitcoin, nó đầu tiên được các nút của mạng xác minh. Nếu giao dịch được coi là hợp lệ, nó sau đó được đặt trong Mempool của mỗi nút, nơi nó ở lại cho đến khi được một thợ mỏ chọn để bao gồm trong một khối.

Quan trọng là phải lưu ý rằng mỗi nút trong mạng Bitcoin duy trì Mempool riêng của mình, và do đó, có thể có sự biến đổi trong nội dung của Mempool giữa các nút khác nhau tại bất kỳ thời điểm nào. Đáng chú ý, tham số `maxmempool` trong tệp `bitcoin.conf` của mỗi nút cho phép các nhà điều hành kiểm soát lượng RAM (bộ nhớ truy cập ngẫu nhiên) mà nút của họ sẽ sử dụng để lưu trữ các giao dịch đang chờ xử lý trong Mempool. Bằng cách giới hạn kích thước của Mempool, các nhà điều hành nút có thể ngăn nó tiêu thụ quá nhiều tài nguyên trên hệ thống của họ. Tham số này được chỉ định bằng megabyte (MB). Giá trị mặc định cho Bitcoin Core đến nay là 300 MB.

Các giao dịch có mặt trong Mempool là tạm thời. Chúng không nên được coi là không thể thay đổi cho đến khi chúng được bao gồm trong một khối, và sau một số lượng xác nhận nhất định. Chúng thường có thể được thay thế hoặc loại bỏ.