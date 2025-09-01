---
name: Whonix
description: Bảo vệ sự riêng tư và bảo mật của bạn.
---

![cover](assets/cover.webp)



**Whonix** là một bản phân phối Linux dựa trên **Debian**, được thiết kế để cung cấp một môi trường kết hợp **bảo mật**, **ẩn danh** và **riêng tư**. Dễ học và tương thích với nhiều giao diện khác nhau (máy ảo, hệ điều hành Qubes, chế độ Live), Whonix bao gồm định tuyến lưu lượng mạng mặc định qua **Tor**, **tường lửa kép** (một tường lửa trên Cổng và một tường lửa trên Máy trạm), **bảo vệ toàn diện chống rò rỉ IP/DNS** và các công cụ để che giấu hiệu quả hoạt động của bạn khỏi những người theo dõi mạng, bao gồm cả ISP của bạn. Không chỉ là một hệ thống ẩn danh, **Whonix** là một môi trường phát triển bảo mật hoàn chỉnh.



## Tại sao nên chọn Whonix?





- Miễn phí**: Giống như hầu hết các bản phân phối Linux, Whonix là một hệ thống mã nguồn mở được cấp phép hoàn toàn miễn phí. Nó được phát triển theo mã nguồn mở, với một cộng đồng năng động và minh bạch.
- Quyền riêng tư, bảo mật và ẩn danh**: Mục tiêu chính của Whonix là cung cấp một môi trường cực kỳ an toàn, trong đó mọi dữ liệu của bạn được bảo vệ và thông tin liên lạc của bạn được mã hóa thông qua mạng Tor.
- Dễ sử dụng**: Whonix cung cấp giao diện đồ họa trực quan, được cấu hình sẵn, phù hợp ngay cả với người dùng mới. Không cần phải là chuyên gia để tận hưởng khả năng bảo vệ nâng cao.
- Môi trường lý tưởng cho phát triển an toàn**: Whonix cho phép bạn phát triển, thử nghiệm, kiểm tra hoặc chạy chương trình mà không cần tiết lộ IP thực của Address hoặc thói quen duyệt web hoặc giao tiếp mạng của bạn.
- Phiên dùng một lần và chế độ Trực tiếp**: Whonix có thể được khởi chạy ở chế độ Trực tiếp hoặc thông qua các máy dùng một lần (ví dụ: thông qua **Qubes OS**), cho phép thực hiện các tác vụ quan trọng mà không để lại dấu vết lâu dài sau khi phiên kết thúc.
- Cài đặt tương đối đơn giản**: Các hình ảnh sẵn sàng sử dụng được cung cấp để cài đặt nhanh chóng trên các máy ảo (VirtualBox, KVM, Qubes). Hệ thống được ghi chép và cập nhật thường xuyên.



## Cài đặt và cấu hình



Trước khi chuyển sang cài đặt Whonix, điều quan trọng cần lưu ý là bản phân phối này **vẫn chưa chính thức có sẵn** dưới dạng hệ thống chính có thể cài đặt trực tiếp trên đĩa Hard (ở chế độ bare metal). Nói cách khác, bạn **vẫn chưa thể cài đặt Whonix làm hệ điều hành máy chủ cổ điển**, như Ubuntu hoặc Debian tiêu chuẩn.



Tuy nhiên, có một số phiên bản cho phép sử dụng Whonix ở chế độ **biến động** (chế độ trực tiếp, phiên tạm thời) hoặc **bền vững** (thông qua máy ảo hoặc tích hợp trong hệ điều hành Qubes).



Để sử dụng ổn định và lâu dài, **ảo hóa hiện là phương pháp duy nhất được khuyến nghị chính thức**. Bạn có thể chạy Whonix bằng **VirtualBox** (Whonix-Gateway và Whonix-Workstation) hoặc tích hợp nó vào một hệ thống như **Qubes OS**. Trong hướng dẫn này, chúng ta sẽ tập trung vào việc cài đặt VirtualBox.



### Điều kiện tiên quyết



Trước khi cài đặt Whonix ở chế độ ảo, hãy đảm bảo máy tính của bạn đáp ứng các yêu cầu kỹ thuật tối thiểu. Ảo hóa yêu cầu một số tài nguyên nhất định mà không phải máy tính nào cũng có thể đáp ứng. Do đó, điều quan trọng là bộ xử lý của bạn phải hỗ trợ công nghệ ảo hóa (Intel VT-x hoặc AMD-V) và tùy chọn này phải được bật trong BIOS/UEFI.



Sau đây là thông số kỹ thuật được đề xuất để có trải nghiệm mượt mà và ổn định với Whonix:





- Bộ nhớ Truy cập Ngẫu nhiên (RAM)**: khuyến nghị tối thiểu **8 GB**. RAM càng nhiều, bạn càng có thể phân bổ nhiều tài nguyên hơn cho các máy ảo (Gateway và Workstation), giúp cải thiện hiệu suất.
- Dung lượng đĩa trống**: vui lòng chừa ít nhất 30 GB dung lượng đĩa trống**. Dung lượng này bao gồm dung lượng cần thiết cho hai máy ảo, tệp hệ thống và bất kỳ dữ liệu hoặc ảnh chụp nhanh nào.
- Bộ xử lý**: nên sử dụng bộ xử lý có ít nhất **4 lõi vật lý** (8 luồng logic), đặc biệt nếu bạn muốn chạy các dịch vụ hoặc công cụ khác song song.



### Tải xuống Whonix



Whonix có nhiều phiên bản, tùy thuộc vào loại môi trường bạn muốn sử dụng. Đối với hầu hết người dùng (Windows, Linux hoặc MacOs), phiên bản VirtualBox là dễ cài đặt nhất. Bạn có thể tải xuống hình ảnh trực tiếp từ [trang web chính thức](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **không tương thích** với MacBook sử dụng bộ xử lý Apple Silicon (kiến trúc ARM).



## Cài đặt VirtualBox



Để chạy Whonix, bạn sẽ cần một **trình quản lý ảo** như VirtualBox, Qubes hoặc KVM.



Sau khi tải xuống tệp, hãy cài đặt nó như bất kỳ phần mềm nào khác. Hãy chấp nhận các tùy chọn mặc định trừ khi bạn có yêu cầu cụ thể. Bạn có thấy khó hiểu không? Hãy xem hướng dẫn sử dụng VirtualBox của chúng tôi.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Nhập Whonix



Sau khi VirtualBox được cài đặt, bạn có thể nhập các tệp Whonix `.ova` mà bạn đã tải xuống trước đó (`Whonix-Gateway-Xfce.ova` và `Whonix-Workstation-Xfce.ova`).



Mở VirtualBox, sau đó nhấp vào **Tệp → Nhập thiết bị**.


Chọn tệp `.ova` tương ứng (bắt đầu bằng Gateway).



![0_03](assets/fr/03.webp)



Chọn vị trí lưu trữ các tệp máy ảo Whonix.



![0_04](assets/fr/04.webp)



Chấp nhận các điều khoản sử dụng, sau đó khởi chạy quá trình nhập và đợi quá trình hoàn tất.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Cấu hình Whonix



Trước khi khởi động Whonix, điều quan trọng là phải điều chỉnh một số **cài đặt hệ thống** để đảm bảo hiệu suất tốt hơn:



Chọn máy ảo **Whonix-Workstation-Xfce**, sau đó nhấp vào **Cấu hình**.



![0_06](assets/fr/07.webp)



Chuyển đến tab **Hệ thống**, nơi phân bổ RAM mặc định là 2048 MB. Chúng tôi khuyên bạn nên **tăng lên 4096 MB (4 GB)** để hoạt động mượt mà hơn, đặc biệt nếu bạn định mở nhiều ứng dụng hoặc làm việc trong các phiên dài. Cổng có thể duy trì ở mức 2048 MB, trừ khi bạn sử dụng nhiều kết nối Tor song song.



![0_08](assets/fr/08.webp)



### Bắt đầu với Whonix



Để Whonix hoạt động bình thường và an toàn, **bạn phải làm theo trình tự khởi động này**:



Trước tiên, hãy khởi động máy **Whonix-Gateway-Xfce**. Máy này chịu trách nhiệm định tuyến tất cả lưu lượng truy cập qua mạng **Tor**. Nếu không có cổng, sẽ không có lưu lượng truy cập nào được định tuyến qua Tor và bạn sẽ mất tính ẩn danh.



![0_09](assets/fr/09.webp)



Sau khi Gateway được khởi chạy hoàn toàn (bạn sẽ thấy Tor được kết nối), bạn có thể khởi động **Whonix-Workstation-Xfce**, chương trình sẽ tự động kết nối qua Gateway.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Cập nhật hệ thống



Vào terminal, nhập lệnh sau để cập nhật danh sách các gói:



```shell
sudo apt update
```



Sau đó chạy lệnh sau để cài đặt các bản cập nhật có sẵn:



```shell
sudo apt full-upgrade
```



## Khám phá Whonix



**Whonix** là một hệ thống được thiết kế để cung cấp một môi trường máy tính **an toàn**, **ẩn danh** và **bảo mật**, lý tưởng cho việc lướt Internet mà không làm lộ danh tính hoặc dữ liệu của bạn. Để đạt được điều này, Whonix đi kèm với một số ứng dụng hữu ích hàng ngày được thiết kế để tăng cường bảo mật kỹ thuật số của bạn ngay từ đầu.


### KeepassXC



**KeePassXC** là trình quản lý mật khẩu tích hợp của Whonix. Nó cho phép bạn **tạo, lưu trữ và quản lý** mật khẩu một cách an toàn mà không cần phải nhớ tất cả theo cách thủ công. Mật khẩu được lưu trữ trong **cơ sở dữ liệu được mã hóa**, được bảo vệ bằng mật khẩu chính.



### Trình duyệt Tor



**Trình duyệt Tor** là trình duyệt web mặc định của Whonix. Nó dựa trên mạng lưới **Tor**, chuyển hướng lưu lượng truy cập của bạn qua nhiều trạm trung chuyển trên khắp thế giới, khiến việc xác định địa chỉ IP thực của bạn (Address) gần như không thể.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** là một Bitcoin Wallet nhẹ và nhanh, được cài đặt sẵn trên Whonix để cho phép bạn quản lý **các giao dịch tiền điện tử** một cách ẩn danh. Nó không tải xuống toàn bộ Blockchain mà sử dụng các máy chủ từ xa để lấy thông tin cần thiết, khiến nó nhẹ hơn nhiều so với Wallet đầy đủ.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix không chỉ là một hệ điều hành: nó là một **môi trường bảo mật** thực sự được thiết kế để bảo vệ tính ẩn danh, quyền riêng tư và các hoạt động nhạy cảm của bạn. Nhờ kiến trúc dựa trên Tor, phân vùng thông minh giữa Cổng và Máy trạm, cùng các công cụ được cài đặt sẵn như Trình duyệt Tor, KeePassXC và Electrum, Whonix cung cấp giải pháp trọn gói cho bất kỳ ai muốn **duyệt web ẩn danh**, **làm việc an toàn** hoặc **xử lý dữ liệu bí mật**.



Để tăng cường bảo mật trên hệ thống Unix của bạn, hãy xem hướng dẫn của chúng tôi về cách kiểm tra máy của bạn: kiểm tra lỗ hổng bảo mật trong hệ điều hành và đảm bảo dữ liệu của bạn không bị xâm phạm.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af