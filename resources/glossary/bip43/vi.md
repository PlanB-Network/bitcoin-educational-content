---
term: BIP43
---

Đề xuất cải tiến giới thiệu việc sử dụng một cấp độ đường dẫn phái sinh để mô tả trường mục đích trong cấu trúc của ví HD, trước đó được giới thiệu trong BIP32. Theo BIP43, cấp độ phái sinh đầu tiên của một ví HD, ngay sau khóa chính được ký hiệu là `m/`, được dành riêng cho số mục đích, chỉ ra tiêu chuẩn phái sinh được sử dụng cho phần còn lại của đường dẫn. Số này được ghi nhận như một chỉ số cứng. Ví dụ, nếu ví tuân theo tiêu chuẩn SegWit (BIP84), phần đầu của đường dẫn phái sinh của nó sẽ là: `m/84'/`. BIP43 do đó cho phép làm rõ các tiêu chuẩn mà mỗi phần mềm ví tuân theo để có sự tương tác tốt hơn giữa chúng. Việc chuẩn hóa phần còn lại của đường dẫn phái sinh được mô tả trong BIP44.