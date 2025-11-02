---
name: Ledger U2F & FIDO2
description: Tăng cường bảo mật trực tuyến của bạn với Ledger
---
![cover](assets/cover.webp)



Thiết bị Ledger là ví phần cứng ban đầu được thiết kế để bảo mật Bitcoin Wallet, nhưng chúng cũng có các tùy chọn nâng cao để xác thực mạnh trên web. Nhờ khả năng tương thích với các giao thức **U2F** và **FIDO2**, chúng cho phép bạn bảo mật quyền truy cập vào tài khoản trực tuyến của mình bằng cách thiết lập yếu tố xác thực thứ hai.



Giao thức U2F (Universal 2nd Factor) được Google và Yubico giới thiệu vào năm 2014, sau đó được chuẩn hóa bởi FIDO Alliance. Giao thức này cho phép thêm yếu tố xác thực vật lý thứ hai (2FA) khi đăng nhập. Sau khi được kích hoạt, ngoài mật khẩu cổ điển, người dùng phải chấp thuận mỗi lần cố gắng kết nối với tài khoản của họ bằng cách nhấn nút trên Ledger của họ. Trong bối cảnh này, Ledger hoạt động theo cách tương tự như Yubikey. U2F thực tế là một thành phần phụ của tiêu chuẩn FIDO2, bao gồm nó trong khi mang lại những cải tiến đáng kể, bao gồm hỗ trợ gốc cho các trình duyệt hiện đại và tính linh hoạt cao hơn trong quản lý khóa xác thực.



Các phương pháp này dựa trên mật mã bất đối xứng: không có dữ liệu bí mật nào được truyền đi, khiến các cuộc tấn công lừa đảo hoặc chặn bắt trở nên không hiệu quả. U2F và FIDO2 hiện được nhiều dịch vụ trực tuyến hỗ trợ.



Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn cách kích hoạt U2F và FIDO2 để xác thực hai yếu tố với Ledger của bạn.



**Lưu ý:** U2F và FIDO2 được hỗ trợ trên tất cả các thiết bị Ledger được trang bị chương trình cơ sở mới nhất: từ phiên bản 2.1.0 cho Nano X và Nano S classic và từ phiên bản 1.1.0 cho Nano S Plus. Các mẫu Stax và Flex tương thích gốc.



## Cài đặt ứng dụng Khóa bảo mật Ledger



Nếu bạn đang sử dụng thiết bị Ledger, bạn có thể biết rằng riêng phần mềm không chứa tất cả các tính năng cần thiết để quản lý ví tiền điện tử. Ví dụ, để sử dụng Bitcoin Wallet, bạn cần cài đặt ứng dụng "*Bitcoin*". Tương tự, để quản lý khóa MFA, bạn sẽ cần cài đặt ứng dụng "*Security Key*".



Trước khi bắt đầu, hãy đảm bảo bạn đã thiết lập Bitcoin Wallet trên Ledger. Điều quan trọng là phải lưu Mnemonic của bạn đúng cách, vì các khóa được sử dụng cho 2FA được lấy từ Mnemonic này. Nếu Ledger của bạn bị mất hoặc bị hỏng, bạn có thể khôi phục quyền truy cập vào các khóa của mình bằng cách nhập cụm từ Mnemonic của bạn trên một thiết bị Ledger khác (hiện tại, các định danh FIDO2 ở chế độ "*passwordless*" vẫn chưa được hỗ trợ trên Ledgers, vì vậy không có định danh thường trú nào).



Kết nối Ledger vào máy tính và mở khóa.



![Image](assets/fr/01.webp)



Để cài đặt ứng dụng, hãy mở phần mềm [Ledger Live] (https://www.Ledger.com/Ledger-live), sau đó chuyển đến tab "*My Ledger*". Tìm ứng dụng "*Security Key*" và cài đặt trên thiết bị của bạn.



![Image](assets/fr/02.webp)



Ứng dụng "*Security Key*" bây giờ sẽ xuất hiện cùng với các ứng dụng khác được cài đặt trên Ledger của bạn.



![Image](assets/fr/03.webp)



Nhấp vào ứng dụng để mở ứng dụng cho các bước tiếp theo trong hướng dẫn.



![Image](assets/fr/04.webp)



## Sử dụng U2F/FIDO2 cho 2FA với Ledger



Truy cập tài khoản bạn muốn bảo mật bằng xác thực hai yếu tố. Ví dụ, tôi sẽ sử dụng tài khoản Bitwarden. Bạn thường sẽ tìm thấy tùy chọn 2FA trong cài đặt dịch vụ, trong các tab "*xác thực*", "*bảo mật*", "*đăng nhập*" hoặc "*mật khẩu*".



![Image](assets/fr/05.webp)



Trong phần dành riêng cho xác thực hai yếu tố, hãy chọn tùy chọn "*Mật khẩu*" (thuật ngữ có thể thay đổi tùy thuộc vào trang web bạn đang sử dụng).



![Image](assets/fr/06.webp)



Bạn thường sẽ được yêu cầu xác nhận mật khẩu hiện tại của mình.



![Image](assets/fr/07.webp)



Đặt tên cho khóa bảo mật để dễ nhận biết, sau đó nhấp vào "*Đọc khóa*".



![Image](assets/fr/08.webp)



Chi tiết tài khoản của bạn sẽ hiển thị trên màn hình Ledger. Nhấn nút "*Đăng ký*" để xác nhận (hoặc cả hai nút cùng lúc, tùy thuộc vào kiểu máy bạn đang sử dụng).



![Image](assets/fr/09.webp)



Khóa truy cập đã được đăng ký thành công.



![Image](assets/fr/10.webp)



Đăng ký khóa bảo mật này.



![Image](assets/fr/11.webp)



Từ bây giờ, khi bạn đăng nhập vào tài khoản, ngoài mật khẩu thông thường, bạn sẽ được yêu cầu kết nối Ledger.



![Image](assets/fr/12.webp)



Sau đó, bạn có thể nhấn nút "*Đăng nhập*" trên màn hình Ledger để xác nhận xác thực (hoặc cả hai nút cùng lúc, tùy thuộc vào kiểu máy bạn đang sử dụng).



![Image](assets/fr/13.webp)



Ưu điểm của việc sử dụng Hardware Wallet Ledger để xác thực hai yếu tố là bạn có thể dễ dàng khôi phục khóa của mình nhờ cụm từ Mnemonic. Ngoài bản sao lưu cơ bản này, bạn cũng có thể sử dụng mã khẩn cấp do mỗi dịch vụ cung cấp khi bạn đã kích hoạt 2FA. Mã khẩn cấp này cho phép bạn kết nối với tài khoản của mình nếu bạn làm mất khóa bảo mật. Do đó, nó thay thế 2FA để kết nối nếu cần.



Ví dụ, trên Bitwarden, bạn có thể truy cập mã này bằng cách nhấp vào "*Xem mã khôi phục*".



![Image](assets/fr/14.webp)



Tôi khuyên bạn nên giữ mã này ở một nơi khác với nơi bạn lưu trữ mật khẩu chính, để tránh chúng bị đánh cắp cùng nhau. Ví dụ, nếu mật khẩu của bạn được lưu trong trình quản lý mật khẩu, hãy giữ mã khẩn cấp 2FA của bạn trên giấy, riêng biệt.



Phương pháp này cung cấp cho bạn hai cấp độ sao lưu trong trường hợp mất Ledger để xác thực 2FA: bản sao lưu đầu tiên sử dụng cụm từ Mnemonic cho tất cả các tài khoản của bạn và bản sao lưu thứ hai dành riêng cho tài khoản sử dụng mã khẩn cấp. Tuy nhiên, điều quan trọng là **không nhầm lẫn vai trò của Mnemonic với vai trò của mã khẩn cấp**:




- Cụm từ Mnemonic gồm 12 hoặc 24 từ không chỉ cho phép bạn truy cập vào các khóa được sử dụng cho 2FA trên tất cả các tài khoản của bạn mà còn vào bitcoin được bảo mật bằng Ledger của bạn;
- Mã khẩn cấp cho phép bạn tạm thời bỏ qua yêu cầu 2FA chỉ trên tài khoản liên quan (trong ví dụ này, chỉ trên Bitwarden).



Xin chúc mừng, giờ bạn đã nắm được cách sử dụng Ledger cho MFA! Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Vui lòng chia sẻ hướng dẫn này trên các mạng xã hội của bạn. Cảm ơn bạn rất nhiều!



Tôi cũng muốn giới thiệu hướng dẫn khác này, trong đó chúng ta sẽ xem xét một giải pháp khác cho xác thực U2F và FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e