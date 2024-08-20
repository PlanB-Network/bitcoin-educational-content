---
term: MTP (MEDIAN TIME PAST)
---

Khái niệm này được sử dụng trong giao thức Bitcoin để xác định một biên độ về thời gian đồng thuận trên mạng. MTP được định nghĩa là trung vị của các dấu thời gian của 11 khối được khai thác gần nhất. Việc sử dụng chỉ số này giúp tránh những bất đồng giữa các nút về thời gian chính xác trong trường hợp có sự chênh lệch. Ban đầu, MTP được sử dụng để xác minh tính hợp lệ của dấu thời gian của các khối so với quá khứ. Kể từ BIP113, nó cũng được sử dụng như một tham chiếu cho thời gian mạng để xác minh tính hợp lệ của các giao dịch khóa thời gian (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, và `OP_CHECKSEQUENCEVERIFY`).