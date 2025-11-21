---
term: KHÁCH QUAN
---

Trong danh mục đầu tư xác định và phân cấp (HD), mục đích, được định nghĩa bởi BIP43, biểu thị một cấp độ phái sinh cụ thể. Chỉ mục này, nằm ở độ sâu đầu tiên của cây phái sinh (`m / mục đích' /`), xác định tiêu chuẩn phái sinh được danh mục đầu tư áp dụng, để tạo điều kiện tương thích giữa các phần mềm quản lý danh mục đầu tư khác nhau. Ví dụ, trong trường hợp địa chỉ SegWit (BIP84), mục đích được ghi chú là `/84'/`. Phương pháp này cho phép tổ chức các khóa một cách hiệu quả giữa các loại Address khác nhau trong một danh mục đầu tư HD duy nhất. Các chỉ mục tiêu chuẩn được sử dụng là:




- Đối với P2PKH: `44'`;
- Đối với P2WPKH lồng nhau trong P2SH: `49'` ;
- Đối với P2WPKH: `84'` ;
- Đối với P2TR: `86'`.