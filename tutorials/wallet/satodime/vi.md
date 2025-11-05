---
name: Satodime
description: Tìm hiểu cách sử dụng Satodime với ứng dụng di động
---
![cover](assets/cover.webp)



Hướng dẫn này sẽ hướng dẫn bạn cài đặt, cấu hình và sử dụng ứng dụng di động Satodime. Bạn sẽ học cách nhận thẻ, tạo két an toàn, nạp tiền, mở khóa và khôi phục khóa riêng. Phần phụ lục cung cấp tài nguyên, thông tin thực hành tốt nhất và giải thích kỹ thuật.



## Giới thiệu



**Satodime**, được phát triển bởi **[Satochip](https://satochip.io/fr/)**, là một thẻ mang an toàn để lưu trữ Bitcoin một cách hữu hình và đơn giản. Nó hoạt động như một phần cứng wallet tự quản lý, nơi bạn có toàn quyền kiểm soát khóa riêng của mình mà không cần phụ thuộc vào bên thứ ba. Được cấp chứng nhận mã nguồn mở và EAL6+, Satodime hỗ trợ tối đa ba két an toàn độc lập.



### Bối cảnh sản phẩm



Satodime, một thẻ **carte au porteur, thuộc về bất kỳ ai sở hữu thực tế**, không cần đăng ký hoặc xác minh danh tính trước. Nó đáp ứng nhu cầu lưu trữ bitcoin di động an toàn, cho phép bất kỳ ai sở hữu thẻ sử dụng hoặc chuyển bitcoin bằng cách quét thẻ qua ứng dụng di động để chiếm hữu hoặc mở két. Không giống như hóa đơn giấy, Satodime sử dụng một con chip bảo mật để niêm phong khóa riêng tư, chỉ được tiết lộ sau khi mở khóa, khiến thẻ tương tự như tiền mặt, trong đó quyền sở hữu được xác định bằng quyền sở hữu thực tế. Lý tưởng để tặng bitcoin làm quà tặng, nó tạo điều kiện thuận lợi cho việc chuyển bitcoin an toàn từ tay này sang tay khác, trong khi ứng dụng di động khai thác NFC để tương tác dễ dàng trên điện thoại thông minh.





- Bảo mật**: Khóa riêng được tạo và lưu trữ trong chip chống giả mạo; trạng thái có thể nhìn thấy (đã niêm phong, chưa niêm phong, trống).
- Tính năng**: Mua bitcoin trực tiếp qua ứng dụng (đối tác của Paybis); quản lý Mainnet và Testnet.
- Mã nguồn mở**: Mã theo giấy phép AGPLv3, có thể xác minh trên GitHub.



### Tiến hóa liên tục



Ứng dụng được phát triển thường xuyên. Hãy kiểm tra trang web hoặc cửa hàng Satochip để cập nhật. Ví dụ: các blockchain mới hoặc chức năng mua hàng có thể được thêm vào. Hãy truy cập [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) để biết các phát triển đang diễn ra.



## 1. Điều kiện tiên quyết



Trước khi bắt đầu sử dụng **Satodime**, hãy đảm bảo bạn có những vật dụng sau:





- Điện thoại thông minh tương thích**: Thiết bị Android hoặc iOS có hỗ trợ NFC.
- Thẻ Satodime**: Mới hoặc chưa được khởi tạo.
- Kết nối Internet**: Để tải ứng dụng.
- Kiến thức cơ bản**: Hiểu về khóa riêng tư/khóa công khai và rủi ro mất mát (không thể đảo ngược).
- Phương tiện an toàn**: Nơi an toàn để ghi lại khóa riêng sau khi mở niêm phong (giấy, kim loại; không bao giờ lưu trữ ở dạng kỹ thuật số).



## 2. Cài đặt





- Tải ứng dụng**:
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Cửa hàng Google Play](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Kiểm tra nhà phát triển (Satochip) để tránh gian lận.
 - Satodime là **mã nguồn mở**. Mã nguồn: [GitHub của Satochip](https://github.com/Toporin/Satodime-Applet).





- Cài đặt và khởi chạy ứng dụng**: Kích hoạt NFC trên điện thoại nếu cần.



![image](assets/fr/01.webp)



## 3. Cấu hình ban đầu



### 3.1 Khởi chạy ứng dụng và quét



Mở ứng dụng và làm theo hướng dẫn. Đặt thẻ Satodime lên đầu đọc NFC của điện thoại (thường nằm ở mặt sau). Giữ chặt thẻ trong suốt quá trình để đảm bảo kết nối ổn định.





- Nếu NFC không hoạt động, hãy kiểm tra cài đặt điện thoại của bạn.
- Một lời chúc mừng khẳng định sự thành công: "Đọc thành công".



![image](assets/fr/02.webp)



Theo nguyên tắc chung, **tất cả các thao tác sau đây sẽ yêu cầu xác nhận bằng cách quét thẻ Satodime**



### 3.2 Nhận thẻ (*Ownership*)



Đối với lần sử dụng đầu tiên, hãy trở thành chủ sở hữu của thẻ để đảm bảo thẻ:





- Nhấp vào "*Làm Ownership*" trong ứng dụng.
- Xác nhận thao tác: thao tác này sẽ tạo ra một khóa chủ sở hữu duy nhất.
- Quét lại bản đồ để áp dụng các thay đổi.
- Cảnh báo**: Bước này không thể đảo ngược. Vui lòng tham khảo [bài viết về *quyền sở hữu*](https://satochip.io/satodime-ownership-explained/).



![image](assets/fr/03.webp)




## 4. Tạo một nơi an toàn



Satodime hỗ trợ tối đa 3 két sắt. Hãy tạo một két để lưu trữ bitcoin:





- Chọn một két sắt trống (ví dụ: Két sắt 01).
- Chọn blockchain (Bitcoin).
- Nhấp vào "*Tạo & Seal*".
- Quét thẻ vào generate và niêm phong khóa riêng (không biết cho đến khi được mở niêm phong).
- Xin chúc mừng**: Két sắt của bạn hiện đã được niêm phong và sẵn sàng để nhận tiền.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Thêm tiền



Sau khi niêm phong, hãy nạp bitcoin vào két:





- Chọn két an toàn.
- Nhấp vào "*Thêm tiền*".
- Sao chép địa chỉ công khai hoặc quét mã QR.
- Gửi tiền từ wallet khác.
- Kiểm tra số dư sau khi xác nhận trên blockchain.
- Tùy chọn mua hàng: Nhấp vào "*Mua hàng*" để mua trực tiếp qua Paybis (Visa, Mastercard, v.v.). Phí áp dụng.



![image](assets/fr/06.webp)



## 6. Mở niêm phong két sắt



Để truy cập khóa riêng tư và chuyển tiền đến nơi khác, hãy mở két sắt:





- Chọn két an toàn đã được niêm phong.
- Nhấp vào "Bỏ niêm phong".
- Xác nhận cảnh báo: thao tác này không thể đảo ngược.
- Quét thẻ để mở niêm phong.
- Két an toàn được đặt thành "*Không niêm phong*"; bây giờ có thể xem/xuất khóa riêng.
- Cảnh báo**: Sau khi mở khóa, khóa riêng tư có thể bị truy cập. Nếu ai đó chiếm đoạt điện thoại thông minh của bạn, họ có thể truy cập khóa này và lấy lại tiền trong két của bạn (không thể đảo ngược).



![image](assets/fr/07.webp)



## 7. Khôi phục khóa riêng



Sau khi mở niêm phong, xuất khóa để sử dụng trong wallet khác:





- Hãy đảm bảo bạn đang ở trong môi trường an toàn.
- Nhấp vào "*Hiển thị khóa riêng tư*".
- Chọn định dạng: Legacy, SegWit, WIF, v.v.
- Sao chép khóa hoặc quét mã QR.
- Bảo mật**: Không bao giờ chia sẻ khóa riêng của bạn. Lưu trữ ngoại tuyến.
- Nhập nó vào chương trình phần mềm wallet tương thích với quản lý quỹ (ví dụ: Sparrow Wallet hoặc Electrum).



![image](assets/fr/08.webp)





## 8. Đặt lại trunk



Việc đặt lại két sẽ xóa vĩnh viễn khóa riêng được liên kết. Nói cách khác, nếu bạn chưa sao chép khóa riêng hoặc nhập khóa riêng vào một thiết bị wallet khác, việc đặt lại két sẽ khiến số tiền trong đó bị mất vĩnh viễn.



![image](assets/fr/09.webp)



Việc đặt lại cốp xe sẽ làm trống khe cắm và sẵn sàng cho cốp xe mới.



## 9. Chuyển giao quyền sở hữu



Ví dụ, để cung cấp bitcoin thông qua Satodime, bạn phải:




- Hãy sở hữu thẻ,
- Tạo một két an toàn Bitcoin,
- Chuyển satss đến đó,
- Chuyển quyền sở hữu thẻ: người tiếp theo quét thẻ sẽ trở thành chủ sở hữu của thẻ,
- Đưa thẻ Satodime cho người bạn chọn và mời họ tải ứng dụng xuống, sau đó quét thẻ để sở hữu thẻ - và do đó có thể truy cập vào số bitcoin được 'lưu trữ' trên thẻ.



![image](assets/fr/10.webp)




## PHỤ LỤC



### A1. Thực hành tốt nhất



Để sử dụng **Satodime** một cách an toàn:





- Bảo mật thẻ**: Coi thẻ như tiền mặt; mất mát = mất tiền nếu không phải là chủ sở hữu.
- Sao lưu khóa**: Sau khi mở niêm phong, hãy ghi lại khóa riêng trên một phương tiện vật lý an toàn. Không bao giờ lưu trữ dưới dạng kỹ thuật số.
- Kiểm tra trạng thái**: Luôn quét để xác nhận quyền sở hữu thẻ và trạng thái đóng/mở của két sắt.
- Tính bảo mật**: Sử dụng địa chỉ mới; tránh các sàn giao dịch tập trung để chuyển tiền.
- Cập nhật**: Cập nhật ứng dụng thông qua các cửa hàng.
- Khôi phục**: Nếu thẻ bị mất nhưng vẫn còn, số tiền sẽ nằm trên blockchain; hãy sử dụng khóa riêng nếu thẻ chưa được niêm phong.



### A2. Tài nguyên bổ sung



Riêng với Satodime:




- [Sản phẩm Satodime](https://satochip.io/fr/product/satodime/)
- [Hướng dẫn dành cho thiết bị di động](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Academy](https://planb.academy/) để biết hướng dẫn về quyền tự quản, khóa riêng tư, v.v.



**Lưu cụm từ khôi phục của bạn**:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Hướng dẫn sử dụng Satochip (sản phẩm đầu tiên của thương hiệu này):**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Hướng dẫn của Seedkeeper:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Giới thiệu về Satochip



**Liên kết chính thức**:




- [Trang web Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Hỗ trợ: info@satochip.io



**Satochip** là một công ty Bỉ chuyên phát triển các giải pháp phần cứng và phần mềm để quản lý và lưu trữ bitcoin và các loại tiền điện tử khác. Sản phẩm chủ lực của công ty, phần cứng Satochip wallet, là một thẻ NFC được trang bị secure element đạt chứng nhận EAL6+. Cùng với Seedkeeper, một cụm từ ghi nhớ và quản lý bí mật, và Satodime, một thẻ mang, Satochip cung cấp một danh mục sản phẩm toàn diện được thiết kế riêng cho nhu cầu của người dùng. Các thiết bị của công ty, được hỗ trợ bởi phần mềm nguồn mở, hướng đến mục tiêu dân chủ hóa bảo mật trên Bitcoin.