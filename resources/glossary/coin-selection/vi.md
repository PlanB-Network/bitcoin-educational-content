---
term: COIN SELECTION
---

Quy trình mà phần mềm ví Bitcoin chọn các UTXO để sử dụng làm đầu vào nhằm thỏa mãn các đầu ra của một giao dịch. Phương pháp lựa chọn coin rất quan trọng vì nó ảnh hưởng đến chi phí của giao dịch và quyền riêng tư của người dùng. Nó thường nhằm mục đích giảm thiểu số lượng đầu vào được sử dụng, nhằm giảm kích thước giao dịch và phí liên quan, đồng thời cố gắng bảo vệ quyền riêng tư bằng cách tránh gộp coin từ các nguồn khác nhau (CIOH). Có nhiều phương pháp lựa chọn coin tồn tại, như *Knapsack Solver* hoặc *Branch-and-Bound*. Khi việc lựa chọn coin được thực hiện thủ công bởi người dùng, nó được gọi là “*Coin Control*”.

> ► *Trong tiếng Anh, nó được gọi là "Coin Selection".*