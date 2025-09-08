---
name: VirtualBox
description: Cài đặt VirtualBox trên Windows 11 và tạo máy ảo đầu tiên của bạn
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Florian Burnel được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc có thể đã có một số thay đổi.*



___




## I. Trình bày



Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách cài đặt VirtualBox trên Windows 11 để tạo máy ảo, có thể chạy Windows 10, Windows 11, Windows Server hoặc bản phân phối Linux (Debian, Ubuntu, Kali Linux, v.v.).



Hướng dẫn cơ bản về VirtualBox này sẽ giúp bạn bắt đầu với giải pháp ảo hóa nguồn mở do Oracle phát triển, hoàn toàn miễn phí. Các hướng dẫn khác sẽ được đăng tải trực tuyến sau để giúp bạn tìm hiểu sâu hơn về chủ đề này.



Khi nói đến việc ảo hóa máy trạm, dù là để thử nghiệm trong dự án hay trong quá trình học CNTT, VirtualBox rõ ràng là một giải pháp tốt. Nó cũng là một lựa chọn thay thế cho các giải pháp khác như Hyper-V, được tích hợp sẵn trong Windows 10 và Windows 11 (cũng như Windows Server), và VMware Workstation (có tính phí) / VMware Workstation Player (miễn phí cho mục đích sử dụng cá nhân).



Cấu hình của tôi: **một máy trạm Windows 11 để cài đặt VirtualBox**, nhưng bạn có thể cài đặt VirtualBox trên Windows 10 (hoặc phiên bản cũ hơn) cũng như trên Linux. Về máy ảo, VirtualBox hỗ trợ nhiều hệ điều hành, bao gồm Windows (ví dụ: Windows 10, Windows 11, Windows Server 2022, v.v.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, v.v.), BSD (PfSense) và macOS.



## II. Tải VirtualBox cho Windows 11



Để tải VirtualBox về cài đặt trên máy Windows, chỉ có một cách duy nhất: truy cập [trang web chính thức của VirtualBox](https://www.virtualbox.org/wiki/Downloads) trong mục "**Tải xuống**". Chỉ cần nhấp vào "Windows hosts" để bắt đầu tải xuống tệp thực thi này, dung lượng chỉ hơn 100 MB.



![Image](assets/fr/025.webp)



## III. Cài đặt VirtualBox trên Windows 11



### A. Cài đặt VirtualBox



Việc cài đặt VirtualBox** rất đơn giản và quy trình này giống nhau trên mọi phiên bản Windows. Hãy bắt đầu bằng cách khởi chạy tệp thực thi VirtualBox bạn vừa tải xuống, sau đó nhấp vào "**Tiếp theo**".



![Image](assets/fr/026.webp)



Cài đặt này có thể tùy chỉnh, nhưng tôi khuyên bạn nên cài đặt tất cả các tính năng: đó là trường hợp của lựa chọn mặc định. Trong hình ảnh bên dưới, bạn có thể thấy các tính năng khác nhau của Elements, bao gồm:





- Hỗ trợ USB VirtualBox** để cho phép VirtualBox hỗ trợ các thiết bị USB
- VirtualBox Bridged Network** để tích hợp hỗ trợ mạng ở chế độ "Bridge" (máy ảo có thể kết nối trực tiếp với mạng cục bộ của bạn)
- VirtualBox Host-Only Network** để tích hợp hỗ trợ mạng ở chế độ "Host-Only" (máy ảo chỉ có thể giao tiếp với máy chủ vật lý Windows 11 và các máy ảo khác ở chế độ này)



Nhấp vào "**Tiếp theo**" để tiếp tục.



![Image](assets/fr/001.webp)



Nhấp vào "**Có**", lưu ý rằng **mạng sẽ bị gián đoạn trong giây lát trên máy tính chạy Windows 11 của bạn**, trong khi VirtualBox thực hiện các sửa đổi mạng để hỗ trợ các loại mạng khác nhau, bao gồm cả chế độ Bridge.



![Image](assets/fr/002.webp)



Sau khi bạn xác nhận, quá trình cài đặt sẽ bắt đầu... Và thông báo "**Bạn có muốn cài đặt phần mềm thiết bị này không?**" sẽ xuất hiện. Hãy chọn tùy chọn "**Luôn tin tưởng phần mềm từ Oracle Corporation**" và nhấp vào "**Cài đặt**". VirtualBox thực sự cần cài đặt một số trình điều khiển trên máy tính của bạn.



![Image](assets/fr/003.webp)



Quá trình cài đặt đã hoàn tất! Đánh dấu vào tùy chọn "**Khởi động Oracle VM VirtualBox 6.1.34 sau khi cài đặt**" và nhấp vào "**Nhấp**" để khởi chạy phần mềm.



![Image](assets/fr/004.webp)



### B. Thêm gói mở rộng



Vẫn trên trang web chính thức của VirtualBox (xem liên kết trước), bạn có thể tải xuống gói mở rộng chính thức, có thể truy cập trong mục "**Gói mở rộng Oracle VM VirtualBox VirtualBox 6.1.34**" bằng cách nhấp vào liên kết "**Tất cả các nền tảng được hỗ trợ**". Gói này sẽ cho phép bạn thêm các chức năng bổ sung vào VirtualBox: không bắt buộc phải thêm, nhưng nó có thể hữu ích! Ví dụ: nó bao gồm hỗ trợ USB 3.0 trong máy ảo (VM), hỗ trợ webcam và mã hóa ổ đĩa.



Mở VirtualBox, nhấp vào "**File**" rồi nhấp vào "**Settings**" trong menu.



![Image](assets/fr/005.webp)



Nhấp vào "**Tiện ích mở rộng**" ở bên trái (1), sau đó nhấp vào nút "**+**" ở bên phải (2) để **tải gói tiện ích mở rộng VirtualBox** mà bạn vừa tải xuống (3).



![Image](assets/fr/006.webp)



Xác nhận bằng cách nhấp vào nút "**Cài đặt**".



![Image](assets/fr/007.webp)



Nhấp vào "**OK**": gói tiện ích mở rộng chính thức hiện đã được cài đặt trên phiên bản VirtualBox của bạn!



![Image](assets/fr/008.webp)



Chúng ta hãy chuyển sang bước tạo máy ảo đầu tiên.



## IV. Tạo máy ảo VirtualBox đầu tiên của bạn



Để tạo một máy ảo mới trên VirtualBox, chỉ cần nhấp vào nút "**Mới**" để khởi chạy trình hướng dẫn tạo máy ảo. Vì đây là lần đầu tiên bạn khởi động VirtualBox, tôi muốn cung cấp thêm một vài thông tin chi tiết về Interface và các nút khác.





- Cài đặt**: cấu hình VirtualBox chung (thư mục VM mặc định, quản lý cập nhật, ngôn ngữ, mạng NAT, tiện ích mở rộng, v.v.)
- Nhập**: nhập thiết bị ảo ở định dạng OVF
- Xuất**: xuất máy ảo hiện có ở định dạng OVF để tạo thiết bị ảo
- Thêm**: thêm một máy ảo hiện có vào kho VirtualBox của bạn, theo định dạng VirtualBox chuẩn (.vbox) hoặc định dạng XML



Ở bên trái, mục "**Công cụ**" cung cấp quyền truy cập vào các chức năng **nâng cao, đặc biệt là để quản lý mạng ảo, nhưng cũng để quản lý lưu trữ VM**. Trong mục "**Công cụ**", các máy ảo của bạn sẽ được thêm vào sau.



![Image](assets/fr/009.webp)



### A. Quá trình tạo VM



**Xin nhắc lại, VirtualBox hỗ trợ rất nhiều hệ điều hành, bao gồm Windows, Linux và BSD. Trong ví dụ này, tôi sẽ tạo một máy ảo cho Windows 11. Một số trường cần được điền vào:





- Name**: tên máy ảo (đây là tên sẽ được hiển thị trong VirtualBox)
- Thư mục máy**: nơi lưu trữ máy ảo, biết rằng một thư mục con có tên VM sẽ được tạo tại vị trí này
- Loại**: loại hệ điều hành, tùy thuộc vào hệ điều hành bạn muốn cài đặt
- Phiên bản**: phiên bản hệ thống bạn muốn cài đặt, trong trường hợp này là Windows 11, vì vậy "**Windows11_64**"



Nhấp vào "**Tiếp theo**" để tiếp tục.



![Image](assets/fr/010.webp)



Tùy thuộc vào hệ điều hành bạn đã chọn ở bước trước, **VirtualBox sẽ đưa ra khuyến nghị về tài nguyên phân bổ cho máy ảo**. Ở đây, chúng ta đang nói về lượng RAM bạn muốn phân bổ cho máy ảo. Giả sử là 4 GB, vì con số này thực sự được khuyến nghị cho Windows 11, nhưng nếu bạn thiếu tài nguyên, hãy chỉ định 2 GB. **Tiếp tục



**Lưu ý**: các tài nguyên được phân bổ cho máy ảo có thể được sửa đổi sau.



![Image](assets/fr/011.webp)



Về phần đĩa ảo Hard, chúng ta sẽ bắt đầu từ đầu, vì vậy cần chọn "**Tạo đĩa ảo Hard ngay**" để máy ảo có đủ dung lượng lưu trữ để cài đặt hệ điều hành và lưu trữ dữ liệu. Nhấp vào "**Tạo**".



![Image](assets/fr/012.webp)



VirtualBox hỗ trợ ba định dạng khác nhau cho ổ đĩa ảo Hard, một điểm khác biệt lớn so với các giải pháp khác như VMware và Hyper-V. Có ba định dạng để lựa chọn:





- VDI**, định dạng chính thức của VirtualBox
- VHD**, là định dạng Hyper-V chính thức, mặc dù định dạng VHDX mới được sử dụng thường xuyên hơn hiện nay
- VMDX** là định dạng VMware chính thức cho cả VMware Workstation và VMware ESXi



Để tạo một máy ảo chỉ sử dụng trên phiên bản VirtualBox này, hãy chọn "**VDI**". Mặt khác, nếu ổ đĩa ảo Hard sẽ được gắn vào máy chủ Hyper-V sau này, bạn nên bắt đầu với định dạng VHD để tránh phải chuyển đổi. Nhấp vào "**Tiếp theo**".



![Image](assets/fr/013.webp)



**Đĩa ảo có thể có kích thước động hoặc cố định**. Khi ở dạng động, tệp đại diện cho **đĩa ảo (ở đây là tệp .vdi) sẽ tăng lên khi dữ liệu được ghi vào đĩa** cho đến khi đạt kích thước tối đa, nhưng sẽ không giảm đi nếu dữ liệu bị xóa. Ngược lại, khi ở dạng cố định, **tổng dung lượng lưu trữ được phân bổ ngay lập tức (và do đó được dành riêng)**, cho phép hiệu suất cao hơn một chút, nhưng mất nhiều thời gian hơn khi đĩa ảo được tạo lần đầu.



Cá nhân tôi, để thử nghiệm máy ảo với VirtualBox, tôi cho rằng chế độ "**Phân bổ động**" là đủ.



![Image](assets/fr/014.webp)



**Bước tiếp theo là chỉ định dung lượng ổ đĩa ảo**, lưu ý rằng theo mặc định, ổ đĩa sẽ được lưu trữ trong thư mục VM (bạn có thể thay đổi dung lượng này tại thời điểm này). Tôi đã chỉ định dung lượng là 64 GB để tuân thủ các yêu cầu của Windows 11, nhưng một lần nữa, bạn có thể chỉ định dung lượng nhỏ hơn. Nhấp vào "**Tạo**" để tạo VM!



![Image](assets/fr/015.webp)



Lúc này, VM đã nằm trong kho của chúng tôi, đã được cấu hình, nhưng hệ điều hành chưa được cài đặt. Chúng ta cần hoàn tất cấu hình VM trước khi khởi động nó.



### B. Gán một hình ảnh ISO cho máy ảo VirtualBox



Để cài đặt Windows 11, hoặc bất kỳ hệ thống nào khác, chúng ta cần nguồn cài đặt. Trong hầu hết các trường hợp, chúng tôi sử dụng ảnh đĩa ở định dạng ISO để cài đặt hệ điều hành. **Cần phải tải ảnh ISO Windows 11 vào ổ đĩa DVD ảo của máy ảo (VM).



Nhấp vào máy ảo (VM) trong danh mục VirtualBox (1), sau đó nhấp vào nút "**Cấu hình**" (2), nút này cho phép truy cập vào cấu hình chung của máy ảo này. Menu này được sử dụng để quản lý tài nguyên (ví dụ: tăng RAM, cấu hình CPU, v.v.). Nhấp vào "**Lưu trữ**" ở bên trái (3), trên ổ đĩa DVD, nơi hiện đang hiển thị "**Trống**" (4), sau đó nhấp vào biểu tượng hình đĩa DVD (5) và chọn "**Chọn tệp đĩa**".



![Image](assets/fr/016.webp)



Chọn ảnh ISO của hệ điều hành bạn muốn cài đặt, sau đó nhấp vào OK. Đây là những gì tôi nhận được:



![Image](assets/fr/017.webp)



Ở lại phần "**Cấu hình**" của VM, tôi vẫn còn một vài điều cần giải thích.



### C. Kết nối mạng VM



Đi đến phần "**Mạng**" ở bên trái. Phần này cho phép bạn quản lý mạng của máy ảo: số lượng giao diện mạng ảo (tối đa 4 giao diện cho mỗi VM), MAC Address và chế độ truy cập mạng (NAT, truy cập cầu nối, mạng nội bộ, v.v.). **Nếu bạn muốn máy ảo của mình có thể truy cập Internet, hãy chọn "NAT" hoặc "Truy cập cầu nối"**, nhưng chế độ thứ hai này yêu cầu máy chủ DHCP phải hoạt động trên mạng của bạn, nếu không bạn sẽ phải cấu hình IP Address theo cách thủ công.



Lưu ý: Tôi sẽ quay lại phần mạng chi tiết hơn trong một bài viết chuyên sâu.



![Image](assets/fr/018.webp)



### D. Số lượng bộ xử lý ảo



Giống như máy tính vật lý, máy ảo cần RAM, đĩa Hard và bộ xử lý để hoạt động. Khi chúng ta tạo máy ảo, bạn có thể nhận thấy trình hướng dẫn không bao gồm cấu hình bộ xử lý. Tuy nhiên, bạn có thể cấu hình cấu hình này bất cứ lúc nào thông qua tab "**Hệ thống**", sau đó là "**Bộ xử lý**", nơi bạn có thể chọn số lượng bộ xử lý ảo.



Lưu ý: tùy chọn "**Enable VT-x/AMD-v nested**" là bắt buộc đối với ảo hóa lồng nhau.



Trong trường hợp của tôi, máy ảo có 2 bộ xử lý ảo:



![Image](assets/fr/019.webp)



**Đừng ngần ngại xem các phần khác của menu cấu hình.



### E. Khởi động lần đầu và cài đặt hệ điều hành



Để khởi động một máy ảo, chỉ cần chọn máy ảo đó trong danh mục và nhấp vào nút "**Bắt đầu**". Một cửa sổ thứ hai sẽ mở ra, cung cấp tổng quan trực quan về máy ảo.



![Image](assets/fr/020.webp)



Ôi trời, tôi gặp lỗi khó chịu và máy ảo của tôi không khởi động được! Lỗi là "Đăng nhập máy ảo không thành công..." với thông tin chi tiết như sau:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Thực ra, điều này là bình thường vì **tính năng ảo hóa chưa được bật trên máy tính của tôi**! Để khắc phục sự cố này, bạn cần khởi động lại máy tính để truy cập BIOS và bật tính năng ảo hóa.



![Image](assets/fr/021.webp)



Không chờ đợi, tôi khởi động lại máy tính và **nhấn phím "SUPPR" để truy cập BIOS** (phím có thể khác nhau tùy theo máy, ví dụ như F2) trên bo mạch chủ ASUS của tôi. Để kích hoạt ảo hóa, "Chế độ SVM" phải được bật trong trường hợp của tôi. Một lần nữa, tên gọi có thể thay đổi tùy theo từng bo mạch chủ, tùy theo nhà sản xuất. Hãy tìm hàm có liên quan đến **AMD-V** (dành cho CPU AMD) hoặc **Intel VT-x** (dành cho CPU Intel).



![Image](assets/fr/022.webp)



Sau khi hoàn tất, hãy lưu lại sửa đổi và khởi động lại máy vật lý... Lần này, **VirtualBox có thể khởi động máy ảo** và tải ảnh ISO Windows để cài đặt hệ điều hành! 🙂



![Image](assets/fr/023.webp)



Trên máy chủ vật lý Windows 11, nơi VirtualBox được cài đặt, chúng ta có thể thấy rằng thư mục máy ảo Windows 11 chứa nhiều tệp khác nhau.





- Tệp VBOX** (ở định dạng XML) tương ứng với cấu hình VM (RAM, CPU, v.v.)
- Tệp VBOX-PREV** là bản sao lưu của cấu hình trước đó
- Tệp VDI** tương ứng với đĩa Hard ảo ở chế độ động, do đó hiện tại nó chỉ có 13 GB, trong khi kích thước tối đa của nó là 64 GB
- Tệp NVRAM** chứa trạng thái BIOS của máy ảo, tương đương với bộ nhớ không bay hơi của máy vật lý



![Image](assets/fr/024.webp)



## V. Kết luận



**VirtualBox hiện đã hoạt động trên máy vật lý Windows 11 của chúng tôi! Việc còn lại là tận dụng nó và tạo máy ảo!** Tôi sẽ quay lại hướng dẫn cài đặt Windows 11 trên máy ảo VirtualBox trong một bài viết khác. Đối với Windows 10, Windows Server hoặc bản phân phối Linux (Ubuntu, Debian, v.v.), hãy để chúng tôi hướng dẫn bạn!