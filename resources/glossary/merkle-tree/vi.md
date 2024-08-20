---
term: MERKLE TREE
---

Merkle Tree là một bộ tích lũy mã hóa. Đây là phương pháp chứng minh sự thuộc về của một thông tin cụ thể trong một tập hợp lớn hơn. Nó là một cấu trúc dữ liệu giúp xác minh thông tin trong một định dạng gọn nhẹ. Trong hệ thống Bitcoin, Merkle Trees được sử dụng để nhóm và cô đọng các giao dịch của một khối thành một hash duy nhất, được gọi là Merkle Root (hoặc "*Root Hash*"). Mỗi giao dịch được hash, sau đó các hash liền kề được hash cùng nhau theo cấp bậc cho đến khi thu được Merkle Root.

![](../../dictionnaire/assets/1.png)

Cấu trúc này cho phép việc xác minh nhanh chóng liệu một giao dịch cụ thể có được bao gồm trong một khối nhất định mà không cần phải phân tích tất cả các giao dịch. Ví dụ, nếu tôi chỉ có Merkle Root và tôi muốn xác minh rằng `TX 7` thực sự là một phần của cây, tôi chỉ cần các bằng chứng sau:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
Với những thông tin này, tôi có thể tính toán các nút trung gian cho đến Merkle Root.

![](../../dictionnaire/assets/2.png)

Merkle Trees đặc biệt được sử dụng cho các nút nhẹ (được biết đến là "SPV") chỉ giữ các tiêu đề khối, nhưng không giữ các giao dịch. Cấu trúc này cũng được tìm thấy trong giao thức UTREEXO, một giao thức cho phép cô đọng bộ UTXO của các nút, và trong MAST Taproot.

> ► *Merkle Tree được đặt theo tên của Ralph Merkle, một nhà mật mã học đã thiết kế cấu trúc này vào năm 1979. Merkle Tree cũng có thể được gọi là "cây hash". Trong tiếng Pháp, nó được gọi là "Arbre de Merkle" hoặc "arbre de hachage".*