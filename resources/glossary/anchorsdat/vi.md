---
term: Anchors.dat

definition: Một tệp Bitcoin Core lưu trữ các địa chỉ IP của các nút mà máy khách đã kết nối trước khi tắt, để tạo điều kiện thuận lợi cho kết nối lại khi khởi động lại.
---
File used in the Bitcoin Core client to store the IP addresses of outgoing nodes to which a client was connected before being shut down. Anchors.dat is thus created every time the node is stopped and deleted when it is restarted. The nodes whose IP addresses are contained in this file are used to help quickly establish connections when the node is restarted.