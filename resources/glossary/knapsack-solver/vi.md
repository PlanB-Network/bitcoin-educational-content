---
term: KNAPSACK SOLVER
---

Một phương pháp cũ được sử dụng để chọn lựa coin trong ví Bitcoin Core trước phiên bản 0.17. Knapsack Solver cố gắng giải quyết vấn đề lựa chọn coin bằng cách lặp đi lặp lại và chọn ngẫu nhiên các UTXO, sau đó cộng dồn chúng theo từng tập con, với mục tiêu là giảm thiểu phí và kích thước của giao dịch. Phương pháp này đã được thay thế bởi *Branch-and-Bound*.