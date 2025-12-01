---
name: Tự làm Spectre
description: Hướng dẫn thiết lập Spectre DIY
---

![cover](assets/cover.webp)


## Spectre-DIY


> Cypherpunks viết mã. Chúng ta biết rằng ai đó phải viết phần mềm để bảo vệ quyền riêng tư, và vì chúng ta không thể có được quyền riêng tư trừ khi tất cả cùng làm, nên chúng ta sẽ viết nó.

*Tuyên ngôn của Cypherpunk - Eric Hughes - 9 tháng 3 năm 1993*


Ý tưởng của dự án là xây dựng phần cứng wallet từ các linh kiện có sẵn.

Mặc dù chúng tôi có bảng mở rộng giúp sắp xếp mọi thứ gọn gàng và giúp bạn tránh phải hàn, chúng tôi vẫn sẽ tiếp tục hỗ trợ và duy trì khả năng tương thích với các thành phần tiêu chuẩn.


![image](assets/fr/01.webp)


Chúng tôi cũng muốn giữ cho dự án linh hoạt để nó có thể hoạt động trên bất kỳ bộ thành phần nào khác với những thay đổi tối thiểu. Có thể bạn muốn tạo một wallet phần cứng trên một kiến trúc khác (RISC-V?), với modem âm thanh làm kênh giao tiếp - bạn sẽ có thể làm được. Việc thêm hoặc thay đổi chức năng của Spectre phải dễ dàng và chúng tôi cố gắng trừu tượng hóa các mô-đun logic càng nhiều càng tốt.


Mã QR là phương thức mặc định để Spectre giao tiếp với máy chủ. Mã QR khá tiện lợi và cho phép người dùng kiểm soát việc truyền dữ liệu - mỗi mã QR có dung lượng rất hạn chế và giao tiếp diễn ra theo một chiều. Hơn nữa, nó được cách ly khỏi mạng không dây - bạn không cần phải kết nối wallet với máy tính bất cứ lúc nào.


Đối với lưu trữ bí mật, chúng tôi hỗ trợ chế độ không cần biết (wallet quên tất cả bí mật khi tắt), chế độ liều lĩnh (lưu trữ bí mật trong bộ nhớ flash của vi điều khiển ứng dụng) và tích hợp secure element sẽ sớm ra mắt.


Trọng tâm chính của chúng tôi là thiết lập đa chữ ký với các ví phần cứng khác, nhưng wallet cũng có thể hoạt động như một trình ký đơn. Chúng tôi cố gắng làm cho nó tương thích với Bitcoin Core ở những điểm có thể - PSBT cho các giao dịch chưa ký, wallet để nhập/xuất ví đa chữ ký. Để giao tiếp với Bitcoin Core dễ dàng hơn, chúng tôi cũng đang phát triển [ứng dụng Specter Desktop] (https://github.com/cryptoadvance/specter-desktop) - một máy chủ python nhỏ gọn giao tiếp với nút Bitcoin Core của bạn.


Phần lớn phần mềm được viết bằng MicroPython, giúp việc kiểm tra và thay đổi mã dễ dàng. Chúng tôi sử dụng thư viện [secp256k1](https://github.com/bitcoin-core/secp256k1) từ Bitcoin Core để tính toán đường cong elliptic và thư viện [LittlevGL](https://lvgl.io/) cho giao diện người dùng đồ họa (GUI).


## Tuyên bố miễn trừ trách nhiệm


Dự án đã được cải thiện đáng kể, đến mức mức độ bảo mật của Spectre-DIY hiện ngang bằng với các ví phần cứng thương mại trên thị trường. Chúng tôi đã triển khai một bộ nạp khởi động an toàn để xác minh các bản nâng cấp firmware, vì vậy bạn có thể chắc chắn rằng chỉ firmware đã ký mới có thể được tải lên thiết bị sau khi thiết lập ban đầu. Tuy nhiên, không giống như các thiết bị ký thương mại, bộ nạp khởi động phải được người dùng cài đặt thủ công và không được thiết lập sẵn tại nhà máy của nhà cung cấp thiết bị. Vì vậy, hãy đặc biệt chú ý trong quá trình cài đặt firmware ban đầu và đảm bảo bạn đã xác minh chữ ký PGP và flash firmware từ một máy tính an toàn.


Nếu có điều gì không ổn, hãy mở một vấn đề ở đây hoặc đặt câu hỏi trong [nhóm Telegram](https://t.me/+VEinVSYkW5TUl5Ai) của chúng tôi.


## Danh sách mua sắm cho Spectre-DIY


Ở đây chúng tôi sẽ mô tả những gì cần mua và trong phần lắp ráp tiếp theo, chúng tôi sẽ giải thích cách lắp ráp và một vài lưu ý về bo mạch - dây nối nguồn, cổng USB, v.v.


### Bảng khám phá


Phần chính của thiết bị là bo mạch phát triển:



- Bo mạch phát triển STM32F469I-DISCO (tức là từ [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) hoặc [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Cáp Mini**USB
- Cáp MicroUSB tiêu chuẩn để giao tiếp qua USB


Tùy chọn nhưng được khuyến nghị:


- [Máy quét mã QR Waveshare](https://www.waveshare.com/barcode-scanner-module.htm) có đầu cắm chân dài như [những đầu cắm này](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) hoặc [những đầu cắm này](https://www.amazon.com/gp/product/B015KA0RRU/) để kết nối máy quét với bo mạch (cần đầu cắm 4 chân).


Hiện tại, chúng tôi đang phát triển một bo mạch mở rộng bao gồm khe cắm thẻ thông minh, máy quét mã QR, pin và vỏ máy in 3D, nhưng nó không bao gồm phần chính - bo mạch khám phá mà bạn cần đặt hàng riêng. Bằng cách này, tấn công chuỗi cung ứng vẫn không phải là vấn đề vì các linh kiện quan trọng về bảo mật được mua từ các cửa hàng điện tử ngẫu nhiên.


Bạn có thể bắt đầu sử dụng Spectre ngay cả khi không có bất kỳ thành phần bổ sung nào, nhưng bạn vẫn có thể giao tiếp với nó qua USB hoặc khe cắm thẻ SD tích hợp. Sử dụng Spectre qua USB đồng nghĩa với việc nó không bị ngắt kết nối mạng, do đó bạn sẽ mất đi một tính năng bảo mật quan trọng.


### Máy quét QR


Đối với máy quét mã QR, bạn có một số tùy chọn.


**Lựa chọn 1. Khuyến nghị.** Máy quét khá tốt từ Waveshare (40$)


[Máy quét Waveshare](https://www.waveshare.com/barcode-scanner-module.htm) - bạn sẽ cần tìm cách gắn nó sao cho đẹp, có thể sử dụng một loại tấm chắn Arduino Prototype và một ít băng dính.


Không cần hàn, nhưng nếu bạn có kỹ năng hàn, bạn có thể làm cho wallet đẹp hơn ;)


**Lựa chọn 2.** Máy quét rất tốt của Mikroe nhưng khá đắt (150$):


[Nhấp vào mã vạch](https://www.mikroe.com/barcode-click) + [Bộ chuyển đổi](https://www.mikroe.com/arduino-uno-click-shield)


**Tùy chọn 3.** Bất kỳ máy quét QR nào khác


Bạn có thể tìm thấy một số máy quét giá rẻ ở Trung Quốc. Chất lượng của chúng thường không tốt lắm, nhưng bạn có thể thử. Thậm chí ESPcamera cũng có thể làm được. Bạn chỉ cần kết nối nguồn, UART (chân D0 và D1) và trigger với D5.


**Tùy chọn 4.** Không có máy quét.


Khi đó bạn chỉ có thể sử dụng Spectre với USB/Thẻ SD.


Trừ khi bạn tự xây dựng mô-đun giao tiếp sử dụng thứ khác thay vì mã QR - audiomodem, bluetooth hoặc bất cứ thứ gì khác. Ngay khi nó có thể được kích hoạt và gửi dữ liệu qua cổng nối tiếp, bạn có thể làm bất cứ điều gì bạn muốn.


### Các thành phần tùy chọn


Nếu bạn thêm một bộ sạc dự phòng nhỏ hoặc pin & bộ sạc/bộ tăng cường năng lượng, wallet của bạn sẽ trở nên hoàn toàn độc lập ;)



## Lắp ráp Spectre-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Kết nối máy quét mã vạch Waveshare


Phần mềm wallet sẽ cấu hình máy quét cho bạn trong lần chạy đầu tiên, do đó không cần phải cấu hình thủ công trước.


Sau đây là cách bạn kết nối máy quét với bảng mạch:


![image](assets/fr/02.webp)


Để thuận tiện, bạn có thể mua một tấm chắn Arduino Protype và hàn & gắn mọi thứ vào đó (ví dụ [cái này](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Quản lý năng lượng


Ở mặt trên của bo mạch có một jumper xác định vị trí cấp nguồn. Bạn có thể thay đổi vị trí của jumper và chọn nguồn điện là một trong các cổng USB hoặc chân VIN và kết nối pin ngoài vào đó (nên là 5V).


### Vỏ bọc cho DIY


Kiểm tra thư mục [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Hãy sáng tạo!


Tự lắp ráp Spectre-DIY và gửi hình ảnh cho chúng tôi (gửi yêu cầu kéo hoặc liên hệ với chúng tôi).


Hãy xem [Thư viện ảnh](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) với những Specter được cộng đồng tập hợp!




## Cài đặt mã đã biên dịch


Với bộ nạp khởi động an toàn, việc cài đặt firmware ban đầu có đôi chút khác biệt. Việc nâng cấp dễ dàng hơn và không yêu cầu kết nối phần cứng wallet với máy tính.


![video](https://youtu.be/eF4cgK_L6T4)


### Đang flash firmware ban đầu


**Lưu ý** Nếu bạn không muốn sử dụng tệp nhị phân từ các bản phát hành, hãy xem [tài liệu về trình khởi động](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) để biết cách biên dịch và cấu hình để sử dụng khóa công khai của bạn thay vì khóa của chúng tôi.



- Nếu bạn đang nâng cấp từ các phiên bản thấp hơn `1.4.0` hoặc tải chương trình cơ sở lên lần đầu tiên, hãy sử dụng `initial_firmware_<version>.bin` từ trang [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Xác minh chữ ký của tệp `sha256.signed.txt` với [khóa PGP của Stepan](https://stepansnigirev.com/ss-specter-release.asc)
 - Xác minh giá trị băm của `initial_firmware_<version>.bin` so với giá trị băm được lưu trữ trong `sha256.signed.txt`
- Nếu bạn đang nâng cấp từ bộ nạp khởi động trống hoặc bạn thấy thông báo lỗi bộ nạp khởi động cho biết chương trình cơ sở không hợp lệ, hãy xem phần tiếp theo - Nạp chương trình cơ sở Spectre đã ký.
- Đảm bảo cầu nối nguồn của bo mạch khám phá của bạn ở vị trí STLK
- Kết nối bo mạch khám phá với máy tính của bạn thông qua cáp **miniUSB** ở phía trên bo mạch.
    - Bo mạch chủ sẽ xuất hiện dưới dạng một đĩa rời có tên `DIS_F469NI`.
- Sao chép tệp `initial_firmware_<version>.bin` vào thư mục gốc của hệ thống tệp `DIS_F469NI`.
- Khi quá trình flash firmware hoàn tất, bo mạch sẽ tự reset và khởi động lại vào bootloader. Bootloader sẽ kiểm tra firmware và khởi động vào firmware chính. Nếu thấy thông báo lỗi không tìm thấy firmware, hãy làm theo hướng dẫn cập nhật và tải firmware qua thẻ SD.
- Bây giờ bạn có thể chuyển đổi cầu nối nguồn đến nơi bạn muốn và cấp nguồn cho bo mạch từ bộ sạc dự phòng hoặc pin.


Việc flash firmware ban đầu bằng cách sao chép-dán tệp `.bin` đôi khi không thành công - thường là do cáp hoặc nếu bạn kết nối thiết bị qua hub USB. Trong trường hợp này, bạn có thể thử lại vài lần nữa (thường thành công sau 2-3 lần thử).


Nếu lỗi liên tục, bạn có thể sử dụng công cụ mã nguồn mở [stlink](https://github.com/stlink-org/stlink/releases/latest). Cài đặt và nhập vào terminal: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. Thông thường, nó hoạt động ổn định hơn nhiều.


### Nâng cấp chương trình cơ sở



- Tải xuống `specter_upgrade_<version>.bin` từ [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Sao chép tệp nhị phân này vào thư mục gốc của thẻ SD (định dạng FAT, tối đa 32 GB)
 - Đảm bảo chỉ có một tệp `specter_upgrade***.bin` trong thư mục gốc
- Cắm thẻ SD vào khe cắm SD của bo mạch Discovery và bật nguồn cho bo mạch
- Bootloader sẽ nạp chương trình cơ sở và sẽ thông báo cho bạn khi quá trình hoàn tất.
- Khởi động lại bo mạch - bây giờ bạn sẽ thấy giao diện Spectre-DIY, nó sẽ gợi ý bạn chọn mã PIN


Mỗi khi có phiên bản mới, chỉ cần tải xuống `specter_upgrade_<version>.bin` từ bản phát hành, chép vào thẻ SD và nâng cấp thiết bị như bước trước. Bootloader sẽ đảm bảo chỉ có firmware đã ký mới có thể được tải vào bo mạch.


### Làm thế nào để tìm ra phiên bản phần mềm


Vào menu `Cài đặt thiết bị` - số phiên bản sẽ hiển thị bên dưới tiêu đề của màn hình.


## Sử dụng Spectre-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Bảo mật của Spectre-DIY


### Phần cứng


Màn hình được điều khiển bởi ứng dụng MCU.


Việc tích hợp phần tử bảo mật vẫn chưa hoàn tất - hiện tại, các bí mật cũng được lưu trữ trên MCU chính. Tuy nhiên, bạn có thể sử dụng wallet mà không cần lưu trữ bí mật - bạn cần nhập cụm từ khôi phục mỗi lần. Tại sao phải nhớ cụm từ passphrase dài dòng nếu bạn có thể nhớ toàn bộ cụm từ ghi nhớ?


Thiết bị sử dụng bộ nhớ flash ngoài để lưu trữ một số tệp (QSPI), nhưng tất cả tệp của người dùng đều được wallet ký và kiểm tra khi tải.


Chức năng quét QR nằm trên một vi điều khiển riêng biệt, do đó mọi quá trình xử lý hình ảnh đều diễn ra bên ngoài MCU quan trọng về bảo mật. Hiện tại, USB và thẻ SD vẫn được quản lý bởi MCU chính, vì vậy đừng sử dụng thẻ SD và USB nếu bạn muốn giảm thiểu bề mặt tấn công.


### Bảo vệ mã PIN (xác thực người dùng)


Trong lần khởi động đầu tiên, một mã bí mật duy nhất sẽ được tạo trên MCU chính. Mã bí mật này cho phép bạn xác minh rằng thiết bị không bị thay thế bởi mã độc - khi bạn nhập mã PIN, bạn sẽ thấy một danh sách các từ sẽ không thay đổi trong suốt thời gian mã bí mật được sử dụng.


Mã PIN của bạn cùng với bí mật duy nhất này được sử dụng để tạo khóa giải mã generate cho khóa Bitcoin của bạn (nếu bạn lưu trữ chúng). Vì vậy, nếu kẻ tấn công có thể vượt qua màn hình mã PIN, việc giải mã vẫn sẽ thất bại.


Nếu bạn đã khóa chương trình cơ sở (TODO: thêm liên kết hướng dẫn tại đây), thì nó cũng sẽ khóa bí mật, do đó, nếu kẻ tấn công cài đặt chương trình cơ sở khác vào bảng mạch, bí mật sẽ bị xóa và bạn sẽ có thể nhận ra khi bắt đầu nhập mã PIN - trình tự các từ sẽ khác.


### Tạo cụm từ phục hồi


Đây là một trong những phần quan trọng nhất của wallet - chìa khóa generate được bảo mật. Để làm tốt điều này, chúng tôi sử dụng nhiều nguồn entropy:



- TRNG của vi điều khiển. Độc quyền, được chứng nhận và có thể tốt nhưng chúng tôi không tin tưởng nó.
- Màn hình cảm ứng. Mỗi lần bạn chạm vào màn hình, chúng tôi sẽ đo vị trí và thời điểm xảy ra thao tác chạm (theo đơn vị vi điều khiển ở tần số 180MHz).
- Micrô tích hợp - chưa có. Bo mạch có hai micrô, vì vậy phần cứng wallet có thể nghe bạn và trộn dữ liệu này vào nhóm entropy.


Toàn bộ entropy này được băm nhỏ lại và chuyển đổi thành cụm từ khôi phục của bạn. Entropy thu được luôn tốt hơn bất kỳ nguồn entropy riêng lẻ nào.


### Logic cấp cao - ví


Spectre hoạt động như một kho lưu trữ khóa. Nó lưu trữ các khóa riêng tư HD có thể được sử dụng trong ví. Ví được định nghĩa bằng các mô tả của chúng. Chúng tôi cũng hỗ trợ miniscript.


Mỗi wallet thuộc về một mạng cụ thể. Điều này có nghĩa là nếu bạn đã nhập wallet trên `testnet`, nó sẽ không khả dụng trên `mainnet` hoặc `regtest` - bạn cần chuyển sang mạng này và nhập wallet riêng.


### Xác minh giao dịch


Các quy tắc sau đây áp dụng cho các giao dịch mà wallet sẽ ký:



- nếu phát hiện các đầu vào hỗn hợp từ các ví khác nhau, người dùng sẽ được cảnh báo ([tấn công](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- thay đổi đầu ra hiển thị tên của wallet mà chúng được gửi đến
- để sử dụng multisig hoặc miniscript, trước tiên bạn cần nhập wallet bằng cách thêm mô tả wallet (qua QR, USB hoặc thẻ SD)


## Hỗ trợ mô tả


Tất cả các mô tả Bitcoin thông thường đều hoạt động. Ngoài ra, chúng tôi có một số phần mở rộng:


### Nhiều nhánh trong các mô tả


Để tiết kiệm dung lượng trong mã QR, chúng tôi cho phép thêm các mô tả với nhiều nhánh cùng một lúc. Nếu bạn muốn sử dụng `wpkh(xpub/0/*)` cho địa chỉ nhận và `wpkh(xpub/1/*)` cho địa chỉ thay đổi, bạn có thể kết hợp chúng trong một mô tả duy nhất: `wpkh(xpub/{0,1}/*)` - wallet sẽ coi chỉ mục đầu tiên của phần thiết lập `{}` là nhánh cho địa chỉ nhận và chỉ mục thứ hai là địa chỉ thay đổi.


Bạn cũng có thể chỉ định nhiều hơn hai nhánh và chỉ mục nhánh có thể khác nhau đối với những người đồng ký khác nhau, do đó mô tả này rất kỳ lạ nhưng hoàn toàn hợp lệ:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Ở đây để nhận địa chỉ số 17, wallet sẽ sử dụng tập lệnh từ `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


Yêu cầu duy nhất là số lượng chỉ mục trong tất cả các tập hợp phải giống nhau (3 trong trường hợp trên).


### Các dẫn xuất mặc định


Nếu bộ mô tả chứa khóa công khai chính nhưng không chứa dẫn xuất ký tự đại diện, dẫn xuất mặc định `/{0,1}/*` sẽ được thêm vào tất cả các khóa mở rộng trong bộ mô tả. Nếu ít nhất một trong các xpub có dẫn xuất ký tự đại diện, bộ mô tả sẽ không bị thay đổi.


Bộ mô tả `wpkh(xpub)` sẽ được chuyển đổi thành `wpkh(xpub/{0,1}/*)`.


### Bản thảo ngắn


Spectre hỗ trợ miniscript, nhưng không hỗ trợ biên dịch chính sách sang miniscript (vì quá tốn kém). Chúng tôi thực hiện một số kiểm tra trên miniscript, do đó chỉ cho phép các tập lệnh `B` ở cấp cao nhất và tất cả các đối số trong các miniscript phụ phải có thuộc tính theo [spec](http://bitcoin.sipa.be/miniscript/).


Bạn có thể sử dụng [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) để generate một mô tả từ chính sách rồi nhập nó vào wallet.


Ví dụ, chính sách "Tôi có thể chi tiêu ngay bây giờ hoặc trong 100 ngày nữa vợ tôi có thể chi tiêu" có thể được chuyển đổi thành wallet như sau:


Chính sách: `or(9@pk(xpubA),and(older(14400),pk(B)))` (khóa của tôi có khả năng cao hơn gấp 9 lần)


Bản ghi nhỏ: `or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Vì ở đây chúng ta không có bất kỳ dẫn xuất ký tự đại diện nào nên dẫn xuất mặc định của `/{0,1}/*` sẽ được thêm vào xpub.



---

Giấy phép MIT


Bản quyền (c) 2019 cryptoadvance


---