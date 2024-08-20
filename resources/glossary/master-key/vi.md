---
term: MASTER KEY
---

Trong bối cảnh của ví HD (Hierarchical Deterministic), master private key là một khóa riêng duy nhất được tạo ra từ seed của ví. Để thu được master key, hàm `HMAC-SHA512` được áp dụng lên seed, sử dụng cụm từ "*Bitcoin seed*" một cách đliteral làm khóa. Kết quả của thao tác này tạo ra một output 512-bit, với 256 bit đầu tiên tạo thành master key, và 256 bit còn lại tạo thành master chain code. Master key và master chain code phục vụ như điểm bắt đầu để suy ra tất cả các khóa riêng và khóa công khai con trong cấu trúc cây của ví HD. Do đó, master private key nằm ở độ sâu 0 của quá trình suy ra.

![](../../dictionnaire/assets/19.png)