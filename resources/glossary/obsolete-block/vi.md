---
term: OBSOLETE (BLOCK)
---

Đề cập đến một khối không có khối con: một khối hợp lệ, nhưng bị loại bỏ khỏi chuỗi chính của Bitcoin. Điều này xảy ra khi hai thợ mỏ tìm thấy một khối hợp lệ ở cùng một độ cao chuỗi trong một khoảng thời gian ngắn và phát sóng nó trên mạng. Các nút cuối cùng chỉ chọn một khối để bao gồm trong chuỗi, theo nguyên tắc của chuỗi có nhiều công việc tích lũy nhất, khiến cho khối kia trở nên "lỗi thời". Quy trình dẫn đến việc sản xuất một khối lỗi thời như sau:
* Hai thợ mỏ tìm thấy một khối hợp lệ ở cùng một độ cao chuỗi trong một khoảng thời gian ngắn. Hãy gọi chúng là `Khối A` và `Khối B`;
* Mỗi người phát sóng khối của mình đến mạng lưới nút Bitcoin. Mỗi nút giờ đây có 2 khối ở cùng một độ cao. Do đó, có hai chuỗi hợp lệ;
* Các thợ mỏ tiếp tục tìm kiếm bằng chứng công việc cho các khối tiếp theo, nhưng để làm được điều đó, họ phải chọn chỉ một khối giữa `Khối A` và `Khối B` mà họ sẽ đào;
* Một thợ mỏ cuối cùng tìm thấy một khối hợp lệ phía trên `Khối B`. Hãy gọi nó là `Khối B+1`;
* Họ phát sóng `Khối B+1` đến các nút mạng;
* Vì các nút theo dõi chuỗi dài nhất (với nhiều công việc tích lũy nhất), họ sẽ ước lượng rằng `Chuỗi B` là chuỗi cần theo đuổi;
* Họ sẽ bỏ qua `Khối A` không còn là một phần của chuỗi chính. Nó do đó trở thành một khối lỗi thời.

![](../../dictionnaire/assets/9.png)

> ► *Trong tiếng Anh, nó được gọi là "Stale Block". Trong tiếng Pháp, nó cũng có thể được gọi là "bloc périmé" hoặc "bloc abandonné". Mặc dù tôi không đồng ý với cách sử dụng này, một số người chơi bitcoin sử dụng thuật ngữ "bloc orphelin" để chỉ những gì thực sự là một khối lỗi thời.*