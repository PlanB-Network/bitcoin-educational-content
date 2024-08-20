---
term: LOẠI TIỀN TỆ
---

Trong bối cảnh của ví xác định và phân cấp (HD wallets), loại tiền tệ (*coin type* trong tiếng Anh) là một cấp độ phái sinh cho phép phân biệt các nhánh của ví dựa trên các loại tiền điện tử khác nhau được sử dụng. Lớp phái sinh này, được định nghĩa bởi BIP 44, nằm ở độ sâu thứ 2 của cấu trúc phái sinh, theo sau khóa chính và mục đích. Ví dụ, đối với Bitcoin, chỉ số được gán là `0x80000000`, được ghi là `/0'/` trong đường dẫn phái sinh. Điều này có nghĩa là tất cả các địa chỉ và tài khoản phái sinh từ đường dẫn này đều được liên kết với Bitcoin. Lớp phái sinh này cho phép phân tách rõ ràng các tài sản khác nhau trong một ví đa tiền tệ. Dưới đây là các chỉ số được sử dụng cho các loại tiền điện tử khác nhau:
* Bitcoin: `0x80000000`;
* Bitcoin Testnet: `0x80000001`;
* Litecoin: `0x80000002`;
* Dogecoin: `0x80000003`;
* Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.png)