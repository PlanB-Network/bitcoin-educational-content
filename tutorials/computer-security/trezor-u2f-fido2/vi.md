---
name: Trezor U2F và FIDO2
description: Tăng cường bảo mật trực tuyến của bạn với Trezor
---
![cover](assets/cover.webp)



Thiết bị Trezor là ví phần cứng ban đầu được thiết kế để bảo mật Bitcoin Wallet, nhưng chúng cũng có các tùy chọn nâng cao để xác thực mạnh trên web. Nhờ khả năng tương thích với các giao thức **U2F** và **FIDO2**, chúng cho phép bạn bảo mật quyền truy cập vào tài khoản trực tuyến của mình mà không cần chỉ dựa vào mật khẩu.



Giao thức U2F (*Universal 2nd Factor*) được Google và Yubico giới thiệu vào năm 2014, sau đó được FIDO Alliance chuẩn hóa. Giao thức này cho phép thêm yếu tố xác thực vật lý thứ hai (2FA) khi đăng nhập. Sau khi kích hoạt, ngoài mật khẩu cổ điển, người dùng phải chấp thuận mỗi lần cố gắng kết nối với tài khoản của họ bằng cách nhấn nút trên Trezor. Trong bối cảnh này, Trezor hoạt động theo cách tương tự như Yubikey.



Phương pháp này dựa trên mật mã bất đối xứng: không có dữ liệu bí mật nào được truyền đi, khiến các cuộc tấn công lừa đảo hoặc chặn bắt trở nên không hiệu quả. U2F hiện được nhiều dịch vụ trực tuyến hỗ trợ.



Ngoài U2F, cho phép xác thực hai yếu tố, Trezor còn hỗ trợ FIDO2 (*Fast IDentity Online 2.0*), một sự phát triển của U2F. Đây là một giao thức xác thực chuẩn hóa từ năm 2018, mở rộng logic của U2F và hướng đến mục tiêu thay thế hoàn toàn mật khẩu. Giao thức này dựa trên hai thành phần: *WebAuthn* (phía trình duyệt) và *CTAP2* (phía khóa vật lý). FIDO2 cho phép xác thực "không cần mật khẩu": người dùng chỉ xác định danh tính của mình thông qua thiết bị Trezor, hoạt động như một mã thông báo mật mã duy nhất, không có mật khẩu bổ sung. Giao thức này hiện tương thích với một số dịch vụ trực tuyến, đặc biệt là những dịch vụ hướng đến doanh nghiệp.



Ngoài chức năng "không cần mật khẩu*", FIDO2 còn cho phép xác thực hai yếu tố theo cách tương tự như U2F.



FIDO2 cũng giới thiệu khái niệm về thông tin xác thực thường trú, tức là các mã định danh được lưu trữ trực tiếp trong Trezor, bao gồm cả khóa riêng cho phép kết nối và thông tin nhận dạng của người dùng. Cơ chế này cho phép xác thực thực sự không cần mật khẩu: chỉ cần cắm Trezor của bạn vào và xác nhận quyền truy cập mà không cần nhập ID hoặc mật khẩu. Ngược lại, thông tin xác thực không thường trú, thông thường hơn, chỉ lưu trữ khóa riêng trong thiết bị; ID người dùng vẫn được lưu trữ ở phía máy chủ và do đó phải được nhập vào mỗi lần kết nối. Chúng ta sẽ xem cách lưu chúng bằng Trezor của bạn sau.



Trong hướng dẫn này, chúng ta sẽ khám phá cách kích hoạt U2F hoặc FIDO2 để xác thực hai yếu tố và sau đó cách cấu hình FIDO2 để truy cập tài khoản của bạn mà không cần mật khẩu, trực tiếp bằng Trezor.



**Lưu ý:** U2F tương thích với tất cả các mẫu Trezor, nhưng FIDO2 chỉ được hỗ trợ trên Safe 3, Safe 5 và Model T, không phải Model One.



## Sử dụng U2F/FIDO2 cho 2FA trên Trezor



Trước khi bắt đầu, hãy đảm bảo bạn đã thiết lập Bitcoin Wallet trên Trezor của mình. Điều quan trọng là phải lưu Mnemonic của bạn đúng cách, vì các khóa được sử dụng cho U2F và FIDO2 trong xác thực hai yếu tố đều bắt nguồn từ Mnemonic này. Nếu Trezor của bạn bị mất hoặc bị hỏng, bạn có thể khôi phục quyền truy cập vào các khóa của mình bằng cách nhập cụm từ Mnemonic của mình trên một thiết bị Trezor khác (lưu ý rằng đối với thông tin xác thực FIDO2 ở chế độ "*passwordless*", chỉ riêng seed là không đủ, như chúng ta sẽ thấy trong các phần tiếp theo).



Kết nối Trezor với máy tính và mở khóa.



![Image](assets/fr/01.webp)



Truy cập tài khoản bạn muốn bảo mật bằng xác thực hai yếu tố. Ví dụ, tôi sẽ sử dụng tài khoản Bitwarden. Bạn thường sẽ tìm thấy tùy chọn 2FA trong cài đặt dịch vụ, trong các tab "*xác thực*", "*bảo mật*", "*đăng nhập*" hoặc "*mật khẩu*".



![Image](assets/fr/02.webp)



Trong phần dành riêng cho xác thực hai yếu tố, hãy chọn tùy chọn "*Mật khẩu*" (thuật ngữ có thể thay đổi tùy thuộc vào trang web bạn đang sử dụng).



![Image](assets/fr/03.webp)



Bạn thường sẽ được yêu cầu xác nhận mật khẩu hiện tại của mình.



![Image](assets/fr/04.webp)



Đặt tên cho khóa bảo mật để dễ nhận biết, sau đó nhấp vào "*Đọc khóa*".



![Image](assets/fr/05.webp)



Chi tiết tài khoản của bạn sẽ xuất hiện trên màn hình Trezor. Chạm vào màn hình hoặc nhấn nút để xác nhận. Bạn cũng sẽ được yêu cầu xác nhận mã PIN của mình.



![Image](assets/fr/06.webp)



Đăng ký khóa bảo mật này.



![Image](assets/fr/07.webp)



Từ bây giờ, khi bạn muốn kết nối với tài khoản của mình, ngoài mật khẩu thông thường, bạn sẽ được yêu cầu kết nối ví Trezor.



![Image](assets/fr/08.webp)



Sau đó, bạn có thể nhấn vào màn hình Trezor để xác nhận xác thực.



![Image](assets/fr/09.webp)



Ưu điểm của việc sử dụng Hardware Wallet Trezor để xác thực hai yếu tố là bạn có thể dễ dàng khôi phục khóa của mình nhờ cụm từ Mnemonic. Ngoài bản sao lưu cơ bản này, bạn cũng có thể sử dụng mã khẩn cấp do mỗi dịch vụ cung cấp khi bạn đã kích hoạt 2FA. Mã khẩn cấp này cho phép bạn kết nối với tài khoản của mình nếu bạn làm mất khóa bảo mật. Do đó, nó thay thế 2FA để kết nối nếu cần.



Ví dụ, trên Bitwarden, bạn có thể truy cập mã này bằng cách nhấp vào "*Xem mã khôi phục*".



![Image](assets/fr/10.webp)



Tôi khuyên bạn nên giữ mã này ở một nơi khác với nơi bạn lưu trữ mật khẩu chính, để tránh chúng bị đánh cắp cùng nhau. Ví dụ, nếu mật khẩu của bạn được lưu trong trình quản lý mật khẩu, hãy giữ mã khẩn cấp 2FA của bạn trên giấy, riêng biệt.



Phương pháp này cung cấp cho bạn hai cấp độ sao lưu trong trường hợp mất Trezor để xác thực 2FA: bản sao lưu đầu tiên sử dụng cụm từ Mnemonic cho tất cả các tài khoản của bạn và bản sao lưu thứ hai dành riêng cho từng tài khoản với mã khẩn cấp. Tuy nhiên, điều quan trọng là **không nhầm lẫn vai trò của Mnemonic với mã khẩn cấp**:




- Cụm từ Mnemonic gồm 12 hoặc 24 từ không chỉ cho phép bạn truy cập vào các khóa được sử dụng cho 2FA trên tất cả các tài khoản của bạn mà còn vào số bitcoin được bảo mật bằng Trezor của bạn;
- Mã khẩn cấp cho phép bạn tạm thời bỏ qua yêu cầu 2FA chỉ trên tài khoản liên quan (trong ví dụ này, chỉ trên Bitwarden).



## Sử dụng FIDO2 trên Trezor



Ngoài xác thực hai yếu tố, FIDO2 còn cho phép xác thực "không cần mật khẩu", tức là không cần nhập mật khẩu khi đăng nhập vào trang web. Chỉ cần kết nối Trezor với máy tính của bạn để truy cập tài khoản an toàn theo cách này. Sau đây là cách cấu hình tính năng này.



Trước khi bắt đầu, hãy đảm bảo bạn đã thiết lập Bitcoin Wallet trên Trezor của mình. Điều quan trọng là phải lưu Mnemonic, vì các định danh FIDO2 "*passwordless*" được mã hóa bằng seed của bạn (chúng ta sẽ tìm hiểu cách lưu các định danh này đúng cách trong phần tiếp theo).



Kết nối Trezor với máy tính và mở khóa.



![Image](assets/fr/01.webp)



Truy cập tài khoản bạn muốn bảo mật ở chế độ "*passwordless*". Tôi sẽ sử dụng tài khoản Bitwarden làm ví dụ. Tùy chọn này thường nằm trong cài đặt dịch vụ, thường nằm trong tab "*authentication*", "*security*" hoặc "*password*".



Ví dụ, trên Bitwarden, tùy chọn này nằm trong tab "*Mật khẩu chính*". Nhấp vào "*Bật*" để kích hoạt xác thực qua FIDO2.



![Image](assets/fr/11.webp)



Bạn thường sẽ được yêu cầu xác nhận mật khẩu.



![Image](assets/fr/12.webp)



Chi tiết tài khoản của bạn sẽ xuất hiện trên màn hình Trezor. Chạm vào màn hình hoặc nhấn nút để xác nhận. Bạn cũng cần xác nhận mã PIN của mình.



![Image](assets/fr/13.webp)



Trên trang web, hãy thêm tên để ghi nhớ khóa bảo mật của bạn, sau đó nhấp vào "*Bật*".



![Image](assets/fr/14.webp)



Sau đó, bạn sẽ được yêu cầu xác minh danh tính để kiểm tra xem chìa khóa có hoạt động bình thường không.



![Image](assets/fr/15.webp)



Từ bây giờ, khi đăng nhập vào tài khoản của bạn, bạn sẽ không cần phải nhập email Address hoặc đăng nhập nữa. Chỉ cần nhấp vào nút để xác thực bằng khóa vật lý trên biểu mẫu đăng nhập.



![Image](assets/fr/16.webp)



Xác nhận kết nối với Trezor của bạn bằng cách nhập mã PIN Hardware Wallet.



![Image](assets/fr/17.webp)



Bạn sẽ được kết nối với tài khoản của mình mà không cần phải nhập mật khẩu.



![Image](assets/fr/18.webp)



**Xin lưu ý rằng ngay cả khi bạn kích hoạt xác thực "*không cần mật khẩu*" thông qua FIDO2 trên Trezor của mình, mật khẩu chính cho tài khoản trực tuyến của bạn vẫn có hiệu lực để đăng nhập**



## Lưu thông tin xác thực FIDO2 của bạn (thông tin xác thực cư trú)



Nếu bạn đang sử dụng FIDO2 hoặc U2F để xác thực hai yếu tố, tức là để đăng nhập vào các tài khoản yêu cầu mật khẩu ngoài xác thực 2FA thông qua Trezor của bạn, thì chỉ riêng cụm từ Mnemonic sẽ truy xuất được quyền truy cập vào khóa của bạn. Tuy nhiên, nếu bạn đang sử dụng FIDO2 ở chế độ "*không cần mật khẩu*" như mô tả trong phần trước, bạn sẽ cần tạo một bản sao thông tin xác thực FIDO của mình ngoài việc sao lưu cụm từ Mnemonic mã hóa các thông tin xác thực này.



Để thực hiện việc này, bạn sẽ cần một máy tính cài đặt Python. Mở terminal và chạy lệnh sau để cài đặt phần mềm Trezor cần thiết:



```shell
pip3 install --upgrade trezor
```



Kết nối Trezor với máy tính qua USB và mở khóa bằng mã PIN.



![Image](assets/fr/01.webp)



Để lấy danh sách các mã định danh FIDO2 được lưu trữ trên Trezor, hãy chạy lệnh sau:



```shell
trezorctl fido credentials list
```



Xác nhận xuất dữ liệu trên Trezor của bạn.



![Image](assets/fr/19.webp)



Thông tin đăng nhập FIDO2 của bạn sẽ được hiển thị trên thiết bị đầu cuối của bạn. Ví dụ, đối với tài khoản Bitwarden của tôi, tôi nhận được thông tin này:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Sao chép và lưu tất cả thông tin này vào một tệp văn bản. Không có rủi ro đáng kể nào liên quan đến bản sao lưu này, ngoài việc tiết lộ rằng bạn đang sử dụng các dịch vụ này với FIDO2. "*Credential ID*" được mã hóa bằng seed của Wallet của bạn, điều này có nghĩa là kẻ tấn công có được bản sao lưu này sẽ không thể kết nối với các tài khoản của bạn, mà chỉ nhận thấy rằng bạn đang sử dụng các tài khoản này. Để giải mã các ID này, bạn cần seed trong Wallet của mình.



Do đó, bạn có thể tạo nhiều bản sao của tệp văn bản này và lưu trữ chúng ở nhiều nơi khác nhau, ví dụ như cục bộ trên máy tính của bạn, trên dịch vụ lưu trữ tệp và trên phương tiện bên ngoài như ổ USB. Tuy nhiên, hãy nhớ rằng bản sao lưu này không được cập nhật tự động, vì vậy bạn sẽ cần phải làm mới nó mỗi khi thiết lập kết nối "*không cần mật khẩu*" mới với Trezor của bạn.



Bây giờ hãy tưởng tượng bạn làm hỏng Trezor của mình. Để lấy lại thông tin xác thực FIDO2, trước tiên bạn cần khôi phục Wallet bằng cụm từ Mnemonic trên thiết bị Trezor mới tương thích với FIDO2.



Sau khi quá trình khôi phục hoàn tất, để nhập mã định danh FIDO2 vào thiết bị mới, hãy chạy lệnh sau trong thiết bị đầu cuối của bạn:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Chỉ cần thay thế `<CREDENTIAL_ID>` bằng một trong các mã định danh của bạn. Ví dụ, trong trường hợp của tôi, điều này sẽ đưa ra:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor của bạn sẽ nhắc bạn nhập mã định danh FIDO2. Xác nhận bằng cách nhấn vào màn hình.



![Image](assets/fr/20.webp)



Đăng nhập FIDO2 của bạn hiện đã hoạt động trên Trezor của bạn. Lặp lại quy trình này cho từng mã định danh của bạn.



Xin chúc mừng, giờ bạn đã nắm được cách sử dụng Trezor với U2F và FIDO2! Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Vui lòng chia sẻ hướng dẫn này trên các mạng xã hội của bạn. Cảm ơn bạn rất nhiều!



Tôi cũng muốn giới thiệu hướng dẫn khác này, trong đó chúng ta sẽ xem xét một giải pháp khác cho xác thực U2F và FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e