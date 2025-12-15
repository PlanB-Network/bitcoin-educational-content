---
name: Angry IP Scanner
description: Một cách đơn giản để quét mạng của bạn
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Florian BURNEL được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc có thể đã được chỉnh sửa.*



___



## I. Trình bày



Làm thế nào để quét mạng Windows để tìm các máy tính được kết nối một cách nhanh chóng và dễ dàng? Câu trả lời là Angry IP Scanner. Dự án nguồn mở này cho phép bạn quét mạng dễ dàng bằng giao diện đồ họa Interface dễ sử dụng.



Công cụ này có thể được sử dụng bởi cá nhân để **quét mạng cục bộ**, cũng như bởi các chuyên gia CNTT cho cùng mục đích. Bằng chứng là **công cụ này rất thiết thực** đã được **một số nhóm tội phạm mạng** sử dụng để quét mạng doanh nghiệp (tương tự như Nmap). Một ví dụ điển hình là [nhóm ransomware RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Đây vẫn là một phần mềm đáng tin cậy, nhưng cũng như các công cụ bảo mật và mạng khác, việc sử dụng nó có thể bị lạm dụng.



Ở đây, chúng ta sẽ sử dụng nó trên **Windows 11**, nhưng hoàn toàn có thể sử dụng nó trên các phiên bản **Windows** khác, cũng như trên **Linux** và **macOS**.



Tuy không toàn diện bằng Nmap, Angry IP Scanner vẫn là một công cụ hữu ích cho việc phân tích mạng cơ bản, nhanh chóng, nhưng cũng vì nó dễ sử dụng. Nó sẽ **phát hiện các máy chủ được kết nối với mạng** và xác định **tên máy chủ** cũng như **cổng mở**.



Nếu bạn muốn tìm hiểu thêm, hãy xem hướng dẫn về Nmap:



https://planb.academy/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Bắt đầu với Angry IP Scanner



### A. Tải xuống và cài đặt Angry IP Scanner



Bạn có thể tải xuống phiên bản mới nhất của Angry IP Scanner từ trang web chính thức của ứng dụng hoặc từ GitHub. Chúng tôi sẽ sử dụng tùy chọn thứ hai. Nhấp vào liên kết bên dưới và tải xuống phiên bản EXE: "**ipscan-3.9.1-setup.exe**".





- [GitHub của Angry IP](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Chạy file thực thi để tiến hành cài đặt. Không cần làm gì đặc biệt trong quá trình cài đặt.



![Image](assets/fr/013.webp)



### B. Chạy quét mạng ban đầu



Khi khởi chạy lần đầu, hãy dành thời gian đọc hướng dẫn trong cửa sổ "**Bắt đầu**" để tìm hiểu thêm về cách thức hoạt động của công cụ. Nhân tiện, có một số thuật ngữ cần lưu ý:





- **Feeder**: mô-đun chịu trách nhiệm tạo danh sách các địa chỉ IP cần quét, từ một dải IP ngẫu nhiên hoặc một tệp có danh sách các địa chỉ IP.
- **Trình tìm nạp**: một tập hợp các mô-đun để truy xuất thông tin về các máy chủ trên mạng. Ví dụ: có các trình tìm nạp để phát hiện địa chỉ MAC, quét cổng, phát hiện tên máy chủ hoặc gửi yêu cầu HTTP.



![Image](assets/fr/018.webp)



Để quét một mạng con IP, chỉ cần nhập **start IP Address** và **end IP Address** vào trường "**IP range**" (nếu không, hãy thay đổi loại ở bên phải). Sau đó, nhấp vào nút "**Start**".



![Image](assets/fr/019.webp)



Vài chục giây sau, kết quả sẽ hiển thị trên Interface của phần mềm. **Đối với mỗi IP Address trong phạm vi được phân tích, bạn sẽ thấy Angry IP Scanner có phát hiện máy chủ hay không.** Một bản tóm tắt cũng sẽ xuất hiện trên màn hình, cho biết số lượng máy chủ đang hoạt động (trong trường hợp này là 6) và số lượng máy chủ có cổng mở.



![Image](assets/fr/020.webp)



Tại đây, chúng ta có thể thấy sự hiện diện của một máy chủ có tên "**OPNsense.local.domain**", được liên kết với IP Address "**192.168.10.1**" và có thể truy cập trên **cổng 80** và **443** (HTTP và HTTPS). Nhấp chuột phải vào máy chủ sẽ cho phép truy cập các lệnh bổ sung, chẳng hạn như ping, theo dõi tuyến đường và mở trình duyệt thông qua IP Address này.



![Image](assets/fr/012.webp)



### C. Thêm cổng quét



Theo mặc định, **Angry IP Scanner** sẽ quét 3 cổng: **80** (HTTP), **443** (HTTPS) và **8080**. Bạn có thể thêm các cổng cần quét từ tùy chọn ứng dụng. Nhấp vào menu "**Công cụ**", sau đó vào tab "**Cổng**".



Tại đây, bạn có thể sửa đổi danh sách cổng thông qua tùy chọn "**Lựa chọn cổng**". Bạn có thể **chỉ định số cổng cụ thể được phân tách bằng dấu phẩy, hoặc phạm vi cổng**. Ví dụ bên dưới thêm hai cổng: **445** (SMB) và **389** (LDAP). Để quét các cổng từ 1 đến 1000, hãy nhập "**1-1000**". Không rõ việc quét cổng được thực hiện theo TCP, UDP hay cả hai.



![Image](assets/fr/021.webp)



Nếu bạn quét lại, bạn có thể sẽ nhận được thông tin mới. Trong ví dụ dưới đây, Angry IP Scanner cho tôi biết cổng 389 và 445 đang mở trên các máy chủ "**SRV-ADDS-01**" và "**SRV-ADDS-02**", nhờ cấu hình mới của các cổng cần quét.



![Image](assets/fr/022.webp)



**Lưu ý**: từ menu "**Máy quét**", bạn có thể xuất kết quả quét sang tệp văn bản.



Nếu bạn muốn quét sâu hơn, hãy nhấp vào menu "**Công cụ**", sau đó nhấp vào "**Trình tải dữ liệu**". Thao tác này sẽ thêm "khả năng" vào quá trình quét. Chỉ cần chọn một trình tải dữ liệu và di chuyển nó sang trái để kích hoạt. Thao tác này sẽ thêm một cột vào kết quả quét.



![Image](assets/fr/014.webp)



Ví dụ dưới đây minh họa các hàm "**NetBIOS info**" và "**Web detection**". Hàm đầu tiên cung cấp thông tin bổ sung như địa chỉ MAC Address và tên miền của máy, trong khi hàm thứ hai hiển thị tiêu đề trang web (có thể cung cấp một số thông tin về loại máy chủ web hoặc ứng dụng).



![Image](assets/fr/011.webp)



Cuối cùng, từ tùy chọn, bạn cũng có thể thay đổi phương thức sử dụng cho lệnh "**ping**", tức là để xem xét máy chủ có đang hoạt động hay không. Vì một số máy chủ không phản hồi ping, điều này cho phép bạn thử các phương pháp khác (gói UDP, thăm dò cổng TCP, ARP, kết hợp UDP + TCP, v.v.).



## III. Kết luận



Đơn giản và hiệu quả: Angry IP Scanner phát hiện các máy chủ được kết nối với mạng và cho phép bạn cấu hình quét cổng. Về tùy chọn, nó không linh hoạt và không đi xa bằng Nmap, nhưng vẫn là một khởi đầu tốt cho việc quét nhanh.



Nếu bạn muốn sử dụng **Nmap** với Interface đồ họa, bạn có thể sử dụng **ứng dụng Zenmap** (xem tổng quan bên dưới).



![Image](assets/fr/015.webp)



https://planb.academy/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d