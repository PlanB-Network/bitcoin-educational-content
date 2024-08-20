---
term: NETWORK-ADJUSTED TIME (NAT)
---

Ước lượng thời gian phổ quát được thiết lập trên các đồng hồ của các nút mạng. Mỗi nút tính toán NAT của mình bằng cách lấy trung vị của các khoảng thời gian chênh lệch giữa đồng hồ địa phương của nó (UTC) và những của các nút mà nó kết nối, sau đó cộng đồng hồ địa phương của mình vào trung vị của những chênh lệch này, lên đến tối đa 70 phút. Thời gian điều chỉnh theo mạng do đó là trung vị của các thời gian nút được tính toán một cách địa phương bởi mỗi nút. Khung tham chiếu này sau đó được sử dụng để xác minh tính hợp lệ của các dấu thời gian khối. Thực sự, để một khối được một nút chấp nhận, dấu thời gian của nó phải nằm giữa MTP (thời gian trung bình của 11 khối được khai thác cuối cùng) và NAT cộng thêm 2 giờ:

```text
MTP < Dấu Thời Gian Hợp Lệ < (NAT + 2h)
```