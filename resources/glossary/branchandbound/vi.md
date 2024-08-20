---
term: BRANCH-AND-BOUND
---

Phương pháp được sử dụng để chọn lựa đầu vào trong ví Bitcoin Core từ phiên bản 0.17 và được phát minh bởi Murch. Branch-and-Bound (BnB) là một phương pháp tìm kiếm để tìm một tập hợp các UTXO phù hợp với số lượng chính xác của đầu ra cần được thực hiện trong một giao dịch, nhằm mục đích giảm thiểu tiền lẻ và các khoản phí liên quan. Mục tiêu của nó là giảm thiểu tiêu chí lãng phí, tính đến cả chi phí ngay lập tức và chi phí tương lai dự kiến cho tiền lẻ. Phương pháp này chính xác hơn về mặt phí so với các phương pháp heuristics trước đây như *Knapsack Solver*. *Branch-and-Bound* được lấy cảm hứng từ phương pháp giải quyết vấn đề cùng tên, được phát minh vào năm 1960 bởi Ailsa Land và Alison Harcourt.

> ► *Phương pháp này đôi khi cũng được gọi là "Thuật toán của Murch" để ghi nhận người phát minh.*