---
name: Sứ giả
description: Thiết lập và sử dụng Passport với ứng dụng Envoy
---
![cover](assets/cover.webp)

Envoy là ứng dụng quản lý ví Bitcoin do Foundation phát triển. Ứng dụng này được thiết kế đặc biệt để sử dụng với ví phần cứng Passport.

Passport "*Batch 2*" mà chúng tôi giới thiệu trong hướng dẫn này với ứng dụng Envoy là phiên bản kế nhiệm của "*Founder's Edition*". Nó có thiết kế cao cấp, màn hình màu độ nét cao và bàn phím vật lý tiện dụng. Nó hoạt động ở chế độ "*Air-Gap*", đảm bảo rằng khóa riêng của ví của bạn vẫn hoàn toàn tách biệt, có thể trao đổi thông qua thẻ MicroSD hoặc mã QR. Thiết bị bao gồm pin 1200 mAh có thể tháo rời.

Về khả năng kết nối, Passport được trang bị cổng MicroSD, cổng USB-C để sạc và camera sau để quét mã QR.

Về mặt bảo mật, Passport tích hợp một thành phần bảo mật và mã nguồn của thiết bị hoàn toàn là mã nguồn mở. Nó cung cấp tất cả các tính năng được mong đợi của một ví phần cứng Bitcoin tốt. Lưu ý rằng Passport hiện chưa hỗ trợ miniscript, nhưng tính năng này được lên kế hoạch vào quý 2 năm 2025.

Với mức giá 199 đô la, Passport được định vị là ví phần cứng cao cấp, cạnh tranh với Coldcard Q, Jade Plus, Tezor Safe 5 và các mẫu ví cao cấp nhất của Ledger.

![Image](assets/fr/01.webp)

Để quản lý ví an toàn của bạn trên Passport, bạn có một số tùy chọn. Ví phần cứng này tương thích với phần lớn các phần mềm quản lý ví trên thị trường, bao gồm Sparrow Wallet, Spectre Desktop, Nunchuk, Keeper, v.v.

Trong hướng dẫn này, dành cho người mới bắt đầu và người dùng trung cấp, chúng ta sẽ khám phá cách sử dụng ứng dụng Envoy với Passport của bạn. Đây là cách dễ nhất để tận dụng tối đa ví phần cứng của bạn.

Nếu bạn là người dùng nâng cao và muốn khám phá các tính năng phức tạp hơn, tôi khuyên bạn nên xem hướng dẫn khác này, trong đó chúng tôi cấu hình Passport bằng Sparrow Wallet:

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## Mở hộp Passport

Khi bạn nhận được Hộ chiếu, hãy đảm bảo hộp và niêm phong trên thùng carton còn nguyên vẹn để xác nhận rằng gói hàng chưa được mở. Xác minh phần mềm về tính xác thực và tính toàn vẹn của thiết bị cũng sẽ được thực hiện khi thiết lập.

![Image](assets/fr/02.webp)

Nội dung hộp bao gồm:


- Hộ chiếu;
- Một mảnh bìa cứng để viết ra cụm từ ghi nhớ của bạn;
- Một cáp USB-C để sạc;
- Thẻ nhớ MicroSD;
- Hai bộ chuyển đổi MicroSD sang Lightning hoặc USB-C;
- Nhãn dán.

Trên thiết bị, bạn sẽ tìm thấy:


- Bàn phím (1) ;
- Cổng USB-C (2);
- Nút xóa (3);
- Nút quay lại (4);
- Nút xác nhận (5);
- Bàn phím định hướng (6);
- Nút bật/tắt (7);
- Một chỉ báo trạng thái (8);
- Cổng MicroSD (9);
- Nút để thay đổi chế độ aA1 (10);
- Một camera phía sau.

![Image](assets/fr/03.webp)

## Tải ứng dụng Envoy

Vào cửa hàng ứng dụng của bạn để tải xuống Envoy:


- Trên [Cửa hàng Google Play](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- Trên [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- Trên [F-Cold](https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

Bạn cũng có thể tải xuống tệp APK trực tiếp [từ kho lưu trữ GitHub của Foundation](https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Sau khi mở ứng dụng, hãy chọn "*Quản lý hộ chiếu*".

![Image](assets/fr/52.webp)

Chọn xem bạn có muốn kích hoạt kết nối Tor để tăng cường tính bảo mật hay không, sau đó nhấn "*Tiếp tục*".

![Image](assets/fr/53.webp)

Chọn "*Kết nối Hộ chiếu hiện có*" nếu Hộ chiếu của bạn đã được cấu hình hoặc "*Thiết lập Hộ chiếu mới*" nếu bạn đang khởi tạo ví phần cứng lần đầu tiên.

![Image](assets/fr/54.webp)

Chấp nhận các điều khoản sử dụng.

![Image](assets/fr/55.webp)

Sau đó, bạn sẽ được yêu cầu xác minh tính xác thực của Hộ chiếu. Nhấp vào "*Tiếp theo*".

![Image](assets/fr/56.webp)

## Hộ chiếu bắt đầu

Nhấn nút bật/tắt ở bên cạnh thiết bị để khởi động.

![Image](assets/fr/04.webp)

Nhấn nút xác nhận để truy cập menu tiếp theo.

![Image](assets/fr/05.webp)

Trong hướng dẫn này, chúng ta sẽ sử dụng Envoy để quản lý ví Passport-secured. Chọn "*Ứng dụng Envoy*".

![Image](assets/fr/57.webp)

Nhấp vào "*Tiếp tục trên Envoy*".

![Image](assets/fr/58.webp)

Bước tiếp theo là kiểm tra thiết bị của bạn. Điều này xác nhận tính xác thực của Hộ chiếu của bạn và đảm bảo rằng nó không bị giả mạo trong quá trình vận chuyển. Bạn sẽ được yêu cầu quét mã QR.

![Image](assets/fr/08.webp)

Quét mã QR động được hiển thị trong ứng dụng bằng Hộ chiếu của bạn. Khi quét xong, hãy nhấp vào "*Tiếp theo*".

![Image](assets/fr/59.webp)

Sau đó sử dụng điện thoại để quét mã QR hiển thị trên Hộ chiếu của bạn.

![Image](assets/fr/60.webp)

Nếu thông báo "*Hộ chiếu của bạn được bảo mật*" xuất hiện, điều này xác nhận rằng ví phần cứng của bạn là chính hãng. Bây giờ bạn có thể sử dụng nó để bảo mật ví Bitcoin.

![Image](assets/fr/61.webp)

Xác nhận kết quả xét nghiệm trên Hộ chiếu của bạn.

![Image](assets/fr/14.webp)

## Thiết lập mã PIN

Tiếp theo là bước mã PIN. Mã PIN mở khóa Hộ chiếu của bạn. Do đó, nó cung cấp khả năng bảo vệ chống lại truy cập vật lý trái phép. Mã PIN không liên quan đến việc tạo ra khóa mật mã của ví của bạn. Vì vậy, ngay cả khi không có quyền truy cập vào mã PIN, việc sở hữu cụm từ ghi nhớ gồm 12 hoặc 24 từ sẽ cho phép bạn lấy lại quyền truy cập vào bitcoin của mình.

![Image](assets/fr/15.webp)

Chúng tôi khuyên bạn nên chọn mã PIN càng ngẫu nhiên càng tốt. Ngoài ra, hãy đảm bảo lưu mã này ở một nơi riêng biệt với nơi lưu trữ Passport của bạn (ví dụ: trong trình quản lý mật khẩu).

Bạn có thể chọn mã PIN từ 6 đến 12 chữ số. Tôi khuyên bạn nên chọn mã càng dài càng tốt.

Sử dụng bàn phím để nhập mã PIN của bạn. Khi hoàn tất, hãy nhấp vào nút xác nhận.

![Image](assets/fr/16.webp)

Xác nhận mã PIN lần thứ hai.

![Image](assets/fr/17.webp)

Mã PIN của bạn đã được đăng ký.

![Image](assets/fr/18.webp)

## Cập nhật phần mềm Passport

Ví phần cứng của bạn đề xuất bạn cập nhật chương trình cơ sở. Tôi khuyên bạn nên cập nhật ngay để được hưởng lợi từ những cải tiến và bản sửa lỗi do các phiên bản mới nhất mang lại. Để tiếp tục, hãy nhấp vào nút xác nhận ở bên phải.

![Image](assets/fr/19.webp)

Passport của bạn đã sẵn sàng nhận chương trình cơ sở mới thông qua thẻ MicroSD.

![Image](assets/fr/20.webp)

### Không có ứng dụng Envoy

Để thực hiện việc này, hãy sử dụng thẻ MicroSD đi kèm trong hộp Passport của bạn (hoặc một thẻ khác) và lắp vào máy tính. Tải xuống phiên bản chương trình cơ sở mới nhất từ [trang tài liệu Foundation](https://docs.foundation.xyz/firmware-updates/passport/) hoặc [kho lưu trữ GitHub của họ](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Trước khi cài đặt trên thiết bị của bạn, chúng tôi khuyên bạn nên kiểm tra tính xác thực và toàn vẹn của phần mềm đã tải xuống. Nếu bạn cần trợ giúp về vấn đề này, hãy tham khảo hướng dẫn này:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Với ứng dụng Envoy

Tùy chọn khác đơn giản hơn là sử dụng trực tiếp ứng dụng Envoy. Nhấp vào "*Tải xuống phần mềm*".

![Image](assets/fr/62.webp)

Sử dụng bộ chuyển đổi đi kèm với Passport để kết nối thẻ MicroSD với điện thoại.

![Image](assets/fr/63.webp)

Chọn thẻ MicroSD trong trình khám phá tệp của bạn để lưu chương trình cơ sở.

![Image](assets/fr/64.webp)

Phần mềm hệ thống hiện đã được lưu. Tháo thẻ MicroSD khỏi điện thoại thông minh và lắp vào Passport.

![Image](assets/fr/65.webp)

Trình khám phá tệp Passport sẽ mở ra. Chọn tệp `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Nhấp vào "*Chọn*".

![Image](assets/fr/23.webp)

Sau đó xác nhận cài đặt chương trình cơ sở.

![Image](assets/fr/24.webp)

Vui lòng đợi quá trình cập nhật hoàn tất.

![Image](assets/fr/25.webp)

Sau khi cập nhật hoàn tất, hãy nhập mã PIN để mở khóa thiết bị và tiếp tục cấu hình.

![Image](assets/fr/26.webp)

## Tạo ví Bitcoin mới

Bây giờ là lúc tạo ví Bitcoin mới. Nhấp vào nút xác nhận.

![Image](assets/fr/27.webp)

Để tạo danh mục đầu tư mới, hãy nhấp vào "*Tạo hạt giống mới*".

![Image](assets/fr/28.webp)

Bạn có thể chọn giữa cụm từ ghi nhớ 12 hoặc 24 từ. Mức độ bảo mật mà cả hai tùy chọn đều tương tự nhau, vì vậy bạn có thể chọn tùy chọn dễ lưu nhất, tức là 12 từ.

![Image](assets/fr/29.webp)

Nhấp vào "*Tiếp tục*".

![Image](assets/fr/30.webp)

Passport của bạn bây giờ sẽ tạo ra "*Mã sao lưu*". Đây là một chuỗi số có thể được sử dụng để giải mã bản sao lưu ví của bạn được lưu trữ trên MicroSD. Hệ thống sao lưu này, dành riêng cho các thiết bị Foundation, tạo thành bản sao lưu bổ sung cho cụm từ ghi nhớ của bạn, nhưng không tương thích với các phần mềm Bitcoin khác.

Nếu bạn quyết định sử dụng "*Mã sao lưu*" này, hãy đảm bảo giữ nó ở một vị trí khác với MicroSD của bạn chứa bản sao lưu được mã hóa của ví của bạn. Tuy nhiên, bạn có thể chọn không sử dụng hệ thống này nếu bạn cảm thấy rằng một bản sao lưu tốt của cụm từ ghi nhớ của bạn là đủ.

![Image](assets/fr/31.webp)

Nhập "*Mã dự phòng*" để xác nhận rằng bạn đã lưu đúng.

![Image](assets/fr/32.webp)

Nếu bạn lắp thẻ MicroSD, bản sao lưu được mã hóa của danh mục đầu tư của bạn sẽ được lưu ở đó.

![Image](assets/fr/33.webp)

Passport của bạn sẽ hiển thị cụm từ ghi nhớ gồm 12 từ. Cụm từ ghi nhớ này cho phép bạn truy cập đầy đủ, không giới hạn vào tất cả bitcoin của mình. Bất kỳ ai sở hữu cụm từ này đều có thể đánh cắp tiền của bạn, ngay cả khi không có quyền truy cập vật lý vào Passport của bạn.

Cụm từ 12 từ khôi phục quyền truy cập vào bitcoin của bạn trong trường hợp Hộ chiếu của bạn bị mất, bị trộm hoặc bị hỏng. Do đó, điều rất quan trọng là phải lưu trữ cẩn thận và cất giữ ở nơi an toàn.

Bạn có thể viết lên tấm bìa cứng đi kèm trong hộp hoặc để an toàn hơn, tôi khuyên bạn nên khắc lên đế thép không gỉ để bảo vệ khỏi hỏa hoạn, lũ lụt hoặc sụp đổ.

Nhấp vào nút xác nhận để xem cụm từ ghi nhớ của bạn.

![Image](assets/fr/34.webp)

Để biết thêm thông tin về cách lưu và quản lý cụm từ ghi nhớ đúng cách, tôi thực sự khuyên bạn nên làm theo hướng dẫn khác này, đặc biệt nếu bạn là người mới bắt đầu:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

tất nhiên, bạn không bao giờ được chia sẻ những từ này trên Internet, như tôi đang làm trong hướng dẫn này. Danh mục mẫu này sẽ chỉ được sử dụng trên Testnet và sẽ bị xóa vào cuối hướng dẫn.**_

Hãy sao lưu câu này lại.

![Image](assets/fr/35.webp)

Passport của bạn đã được cấu hình thành công. Nhấp vào nút xác nhận để tiếp tục.

![Image](assets/fr/36.webp)

## Thiết lập danh mục đầu tư trên Envoy

Trong hướng dẫn này, tôi sẽ chỉ cho bạn cách sử dụng Passport với ứng dụng Envoy. Tuy nhiên, ví phần cứng này cũng tương thích với Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Spectre và nhiều loại khác...

![Image](assets/fr/66.webp)

Sử dụng ứng dụng Envoy để quét mã QR hiển thị trên Hộ chiếu của bạn.

![Image](assets/fr/67.webp)

Khóa công khai của bạn hiện đã được nhập vào ứng dụng. Nhấp vào "*Xác thực địa chỉ nhận*".

![Image](assets/fr/68.webp)

Sử dụng Hộ chiếu của bạn để quét địa chỉ hiển thị trên Envoy.

![Image](assets/fr/69.webp)

Hộ chiếu của bạn sẽ xác nhận xem ví được nhập vào Envoy có hợp lệ hay không. Xác nhận trong ứng dụng.

![Image](assets/fr/70.webp)

Bây giờ bạn có thể truy cập thông tin công khai của ví trên Envoy, nhưng để chi tiêu bitcoin, bạn sẽ cần sử dụng Passport.

![Image](assets/fr/71.webp)

## Khám phá thực đơn Passport

Giao diện Passport của bạn có ba menu chính:


- "*Tài khoản*";
- "*Hơn*";
- "*Cài đặt*".

Để di chuyển giữa các menu này, hãy sử dụng mũi tên trái và phải trên bàn phím điều hướng.

### Menu "Tài khoản"

Trong menu "*Tài khoản*", bạn sẽ tìm thấy các tính năng chính của ví Bitcoin. Bạn có thể ký giao dịch thông qua camera hoặc qua cổng MicroSD.

![Image](assets/fr/37.webp)

Trình đơn phụ "*Công cụ tài khoản*" cung cấp các tùy chọn như xác minh địa chỉ, ký tin nhắn hoặc tham khảo các địa chỉ trong danh mục đầu tư của bạn.

![Image](assets/fr/38.webp)

Trong menu phụ "*Quản lý tài khoản*", bạn có thể kết nối ví Bitcoin của mình với phần mềm quản lý ví (chúng tôi sẽ đề cập ở các bước tiếp theo của hướng dẫn này) hoặc xem và đổi tên tài khoản của bạn.

![Image](assets/fr/39.webp)

### Menu "Thêm"

Trong menu "*Thêm*", bạn có thể tạo một tài khoản mới trong danh mục đầu tư của mình, được liên kết với cùng một cụm từ ghi nhớ.

![Image](assets/fr/40.webp)

Bạn cũng có thể nhập mật khẩu BIP39 hoặc sử dụng hạt giống tạm thời.

![Image](assets/fr/41.webp)

### Menu "Cài đặt"

Trong menu "*Cài đặt*", bạn sẽ tìm thấy tất cả cài đặt ví và thiết bị của mình.

![Image](assets/fr/42.webp)

Menu phụ "*Thiết bị*" cung cấp cho bạn các tùy chọn để tùy chỉnh độ sáng màn hình, thiết lập thời gian trễ trước khi tự động khóa, thay đổi mã PIN hoặc đổi tên thiết bị.

![Image](assets/fr/43.webp)

Trình đơn phụ "*Sao lưu*" cho phép bạn xuất bản sao lưu danh mục đầu tư đã mã hóa, kiểm tra tính hợp lệ của bản sao lưu hiện có hoặc tra cứu lại "*Mã sao lưu*" của bạn.

![Image](assets/fr/44.webp)

Menu phụ "*Firmware*" dùng để cập nhật firmware của Passport. Chúng tôi khuyên bạn nên thực hiện các bản cập nhật này thường xuyên để được hưởng lợi từ các bản sửa lỗi và tính năng mới nhất.

![Image](assets/fr/45.webp)

Menu phụ "*Bitcoin*" cho phép bạn thay đổi đơn vị hiển thị (BTC hoặc satoshi), quản lý ví Multisig hoặc chuyển sang chế độ "*Testnet*".

![Image](assets/fr/46.webp)

Trong "*Nâng cao*", bạn có thể xem các từ trong cụm từ ghi nhớ, thực hiện các thao tác trên thẻ MicroSD đã lắp, khôi phục cài đặt gốc cho Passport hoặc thực hiện kiểm tra tính xác thực như đã thực hiện trước đó.

![Image](assets/fr/47.webp)

Bạn có thể kích hoạt "*Security Words*", một tính năng bổ sung thêm một lớp bảo mật bằng cách hiển thị hai từ cụ thể khi mở khóa thiết bị sau khi nhập bốn chữ số đầu tiên của mã PIN. Những từ này, được lưu trong quá trình cấu hình, đảm bảo rằng Passport không bị thay thế hoặc can thiệp. Trong trường hợp có bất kỳ sự khác biệt nào sau này, chúng tôi khuyên bạn không nên sử dụng thiết bị. Tôi khuyên bạn nên kích hoạt tùy chọn này để ngăn ngừa hầu hết các rủi ro về xâm phạm vật lý của thiết bị.

![Image](assets/fr/48.webp)

Cuối cùng, menu phụ "*Phần mở rộng*" cho phép bạn kích hoạt các chức năng cụ thể cho một số mục đích sử dụng nhất định của thiết bị, chẳng hạn như giao thức Whirlpool coinjoin.

![Image](assets/fr/49.webp)

## Nhận bitcoin

Bây giờ Passport của bạn đã được thiết lập, bạn đã sẵn sàng nhận sats đầu tiên trên ví Bitcoin mới của mình. Để thực hiện, trên Envoy, hãy nhấp vào tài khoản "*Primary 0*" của bạn.

![Image](assets/fr/72.webp)

Nhấp vào nút "*Nhận*".

![Image](assets/fr/73.webp)

Ứng dụng Envoy của bạn hiển thị địa chỉ trống đầu tiên có sẵn trên ví của bạn. Trước khi sử dụng, hãy kiểm tra địa chỉ trên màn hình Passport để đảm bảo rằng địa chỉ đó thực sự thuộc về ví Bitcoin của chúng ta. Trong menu "*Tài khoản*" của Passport, hãy chọn "*Công cụ tài khoản*".

![Image](assets/fr/74.webp)

Nhấp vào "*Xác minh địa chỉ*", sau đó quét mã QR hiển thị trên Envoy.

![Image](assets/fr/75.webp)

Hãy đảm bảo rằng địa chỉ hiển thị trên Hộ chiếu trùng khớp chính xác với địa chỉ hiển thị trên Sparrow và "*Đã xác minh*" phải xuất hiện.

![Image](assets/fr/76.webp)

Bây giờ bạn có thể sử dụng nó để nhận bitcoin. Khi giao dịch được phát trên mạng, nó sẽ xuất hiện trên Envoy. Đợi cho đến khi bạn nhận được đủ xác nhận để coi giao dịch là chắc chắn.

![Image](assets/fr/77.webp)

## Gửi bitcoin

Bây giờ bạn đã có một vài sats trong ví, bạn cũng có thể gửi một ít. Để làm như vậy, hãy nhấp vào nút "*Gửi*".

![Image](assets/fr/78.webp)

Nhập địa chỉ người nhận bằng cách dán trực tiếp hoặc quét mã QR bằng camera trên điện thoại thông minh của bạn.

![Image](assets/fr/79.webp)

Xác định số tiền bạn muốn gửi, sau đó nhấp vào "*Xác nhận*".

![Image](assets/fr/80.webp)

Chọn phí giao dịch theo tình hình thị trường hiện tại, sau đó kiểm tra thông tin giao dịch. Nếu mọi thứ đều chính xác, hãy nhấp vào "*Ký bằng hộ chiếu*".

![Image](assets/fr/81.webp)

Thêm nhãn vào giao dịch của bạn để ghi lại mục đích rõ ràng.

![Image](assets/fr/82.webp)

Sau đó, Envoy sẽ hiển thị PSBT (*Giao dịch Bitcoin đã ký một phần*). Ứng dụng đã xây dựng giao dịch, nhưng vẫn thiếu chữ ký để mở khóa bitcoin được sử dụng trong đầu vào. Những chữ ký này chỉ có thể được thực hiện bởi Passport, nơi lưu trữ hạt giống của bạn, cung cấp quyền truy cập vào khóa riêng cần thiết để ký giao dịch.

![Image](assets/fr/83.webp)

Trên Hộ chiếu của bạn, hãy truy cập menu "*Tài khoản*" và nhấp vào "*Ký bằng Mã QR*".

![Image](assets/fr/84.webp)

Quét PSBT (*Giao dịch Bitcoin đã ký một phần*) được hiển thị trên Envoy.

![Image](assets/fr/85.webp)

Xác nhận địa chỉ nhận và số tiền gửi là chính xác, sau đó nhấn nút xác nhận.

![Image](assets/fr/86.webp)

Kiểm tra địa chỉ trao đổi. Trong ví dụ của tôi, không có địa chỉ nào vì giao dịch chỉ bao gồm một đầu ra duy nhất.

![Image](assets/fr/87.webp)

Hãy đảm bảo rằng đây là mức phí bạn đã chọn.

![Image](assets/fr/88.webp)

Nếu mọi thông tin đều chính xác, hãy nhấp vào nút xác nhận để ký giao dịch.

![Image](assets/fr/89.webp)

Hộ chiếu của bạn hiển thị giao dịch đã ký của bạn dưới dạng mã QR.

![Image](assets/fr/90.webp)

Trên ứng dụng Envoy, nhấp vào biểu tượng mã QR, sau đó quét PSBT hiển thị trên màn hình Hộ chiếu của bạn.

![Image](assets/fr/91.webp)

Kiểm tra lại thông tin giao dịch của bạn lần cuối. Nếu mọi thứ đều chính xác, hãy nhấn "*Gửi giao dịch*" để phát trên mạng Bitcoin.

![Image](assets/fr/92.webp)

Giao dịch của bạn hiện đang chờ xác nhận. Bạn có thể theo dõi trạng thái giao dịch trực tiếp từ tài khoản của mình.

![Image](assets/fr/93.webp)

Xin chúc mừng, giờ bạn đã biết cách thiết lập và sử dụng Passport với ứng dụng Envoy. Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái màu xanh lá cây bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn vì đã chia sẻ!

Để biết thêm thông tin, hãy xem hướng dẫn của chúng tôi về phần mềm Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
