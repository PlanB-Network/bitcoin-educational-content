---
term: MỤC TIÊU
---

Trong ví xác định và phân cấp (HD), mục tiêu (hoặc _mục đích_ trong tiếng Anh), được định nghĩa bởi BIP43, đại diện cho một cấp độ phái sinh cụ thể. Chỉ số này, nằm ở độ sâu đầu tiên của cây phái sinh (`m / purpose' /`), xác định tiêu chuẩn phái sinh mà ví sử dụng, nhằm tạo điều kiện tương thích giữa các phần mềm quản lý ví khác nhau. Ví dụ, trong trường hợp của địa chỉ SegWit (BIP84), mục tiêu được ghi như là `/84'/`. Phương pháp này cho phép tổ chức hiệu quả các khóa giữa các loại địa chỉ khác nhau trong cùng một ví HD. Các chỉ số tiêu chuẩn được sử dụng là:
* Đối với P2PKH: `44'`;
* Đối với P2WPKH-nested-in-P2SH: `49'`;
* Đối với P2WPKH: `84'`;
* Đối với P2TR: `86'`.

![](../../dictionnaire/assets/20.png)