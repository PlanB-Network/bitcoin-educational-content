---
term: BLOOM FILTER
---

Một cấu trúc dữ liệu xác suất được sử dụng để kiểm tra xem một phần tử có thuộc về một tập hợp hay không. Bộ lọc Bloom cho phép kiểm tra nhanh chóng việc thành viên mà không cần kiểm tra toàn bộ tập dữ liệu. Chúng đặc biệt hữu ích trong các bối cảnh mà không gian và tốc độ là quan trọng, nhưng một tỷ lệ lỗi thấp và có thể kiểm soát được là chấp nhận được. Thực tế, Bộ lọc Bloom không tạo ra lỗi âm, nhưng chúng tạo ra một lượng nhất định lỗi dương. Khi một phần tử được thêm vào bộ lọc, nhiều hàm băm tạo ra các vị trí trong một mảng bit. Để kiểm tra thành viên, cùng một hàm băm được sử dụng. Nếu tất cả các bit tương ứng được thiết lập, phần tử có thể nằm trong tập hợp, nhưng với rủi ro của lỗi dương. Bộ lọc Bloom được sử dụng rộng rãi trong các lĩnh vực của cơ sở dữ liệu và mạng. Đáng chú ý là Google sử dụng chúng cho hệ thống quản lý cơ sở dữ liệu nén *BigTable*. Trong giao thức Bitcoin, chúng được sử dụng đặc biệt cho ví SPV theo BIP37.

> ► *Khi cụ thể nói về việc sử dụng Bộ lọc Bloom trong bối cảnh của giao dịch Bitcoin, thuật ngữ "Transaction Bloom Filtering" đôi khi được gặp.*