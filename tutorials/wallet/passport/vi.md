---
name: Hộ chiếu - Nền tảng
description: Cấu hình và sử dụng ví phần cứng Passport ở chế độ thủ công
---
![cover](assets/cover.webp)

Passport là ví phần cứng chỉ dành cho Bitcoin, được thiết kế bởi Foundation Devices, một công ty Mỹ được thành lập vào tháng 4 năm 2020 tại Boston.

Passport "*Batch 2*" mà chúng tôi giới thiệu trong hướng dẫn này là phiên bản kế nhiệm của "*Founder's Edition*". Thiết bị có thiết kế cao cấp, màn hình màu độ nét cao và bàn phím vật lý tiện dụng. Thiết bị hoạt động ở chế độ "*Air-Gap*", đảm bảo rằng khóa riêng của ví của bạn vẫn hoàn toàn tách biệt, có thể trao đổi thông qua thẻ MicroSD hoặc mã QR. Thiết bị bao gồm pin 1200 mAh có thể tháo rời.

Về khả năng kết nối, Passport được trang bị cổng MicroSD, cổng USB-C để sạc và camera sau để quét mã QR.

Về mặt bảo mật, Passport tích hợp một thành phần bảo mật và mã nguồn của thiết bị hoàn toàn là mã nguồn mở. Nó cung cấp tất cả các tính năng được mong đợi của một ví phần cứng Bitcoin tốt. Lưu ý rằng Passport hiện chưa hỗ trợ miniscript, nhưng tính năng này được lên kế hoạch vào quý 2 năm 2025.

Với mức giá 199 đô la, Passport được định vị là ví phần cứng cao cấp, cạnh tranh với Coldcard Q, Jade Plus, Tezor Safe 5 và các mẫu ví cao cấp nhất của Ledger.

![Image](assets/fr/01.webp)

Để quản lý ví an toàn của bạn trên Passport, bạn có một số tùy chọn. Ví phần cứng này tương thích với phần lớn các phần mềm quản lý ví trên thị trường, bao gồm Sparrow Wallet, Spectre Desktop, Nunchuk, Keeper, v.v. Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách sử dụng nó với Sparrow Wallet.

Nếu bạn là người mới bắt đầu, lựa chọn dễ nhất là sử dụng Passport của bạn với ứng dụng Envoy gốc do Foundation phát triển. Để tìm hiểu cách sử dụng Envoy với Passport của bạn, hãy xem hướng dẫn khác này:

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb
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

## Hộ chiếu bắt đầu

Nhấn nút bật/tắt ở bên cạnh thiết bị để khởi động.

![Image](assets/fr/04.webp)

Nhấn nút xác nhận để truy cập menu tiếp theo.

![Image](assets/fr/05.webp)

Trong hướng dẫn này, chúng tôi sẽ sử dụng Sparrow Wallet để quản lý ví Passport-secured. Chọn "*Manual Setup*".

![Image](assets/fr/06.webp)

Sau đó chấp nhận các điều khoản sử dụng.

![Image](assets/fr/07.webp)

Bước tiếp theo là kiểm tra thiết bị của bạn. Điều này xác nhận tính xác thực của Hộ chiếu của bạn và đảm bảo rằng nó không bị giả mạo trong quá trình vận chuyển. Bạn sẽ được yêu cầu quét mã QR.

![Image](assets/fr/08.webp)

Truy cập [trang web xác minh chính thức](https://validate.foundationdevices.com/) và chọn "*Hộ chiếu*".

![Image](assets/fr/09.webp)

Sử dụng camera trên Passport để quét mã QR hiển thị trên trang web.

![Image](assets/fr/10.webp)

Sau đó thiết bị của bạn sẽ hiển thị 4 từ.

![Image](assets/fr/11.webp)

Nhập những từ này vào trang web để xác nhận tính xác thực của Hộ chiếu của bạn và nhấp vào "*Xác thực*".

![Image](assets/fr/12.webp)

Nếu thông báo "*Đã vượt qua*" xuất hiện, ví phần cứng của bạn là chính hãng. Bây giờ bạn có thể sử dụng nó để bảo mật ví Bitcoin.

![Image](assets/fr/13.webp)

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

Để thực hiện việc này, hãy sử dụng thẻ MicroSD đi kèm trong hộp Passport của bạn (hoặc một thẻ khác) và lắp vào máy tính. Tải xuống phiên bản chương trình cơ sở mới nhất từ [trang tài liệu Foundation](https://docs.foundation.xyz/firmware-updates/passport/) hoặc [kho lưu trữ GitHub của họ](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Trước khi cài đặt trên thiết bị của bạn, chúng tôi khuyên bạn nên kiểm tra tính xác thực và toàn vẹn của phần mềm đã tải xuống. Nếu bạn cần trợ giúp về vấn đề này, hãy tham khảo hướng dẫn này:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Sau khi kiểm tra tệp `.bin`, hãy đặt tệp đó vào MicroSD của bạn, sau đó lắp vào Passport. Trình khám phá tệp Passport sẽ mở ra. Chọn tệp `vN.N.N-passport.bin`.

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

Cụm từ 12 từ này khôi phục quyền truy cập vào bitcoin của bạn trong trường hợp Hộ chiếu của bạn bị mất, bị trộm hoặc bị hỏng. Do đó, điều rất quan trọng là phải lưu trữ cẩn thận và cất giữ ở nơi an toàn.

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

## Khám phá thực đơn

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

Bạn cũng có thể nhập mật khẩu BIP39 (xem phần tiếp theo) hoặc sử dụng hạt giống tạm thời.

![Image](assets/fr/41.webp)

### Menu "Cài đặt"

Trong menu "*Cài đặt*", bạn sẽ tìm thấy tất cả cài đặt ví và thiết bị của mình.

![Image](assets/fr/42.webp)

Menu phụ "*Thiết bị*" cung cấp cho bạn các tùy chọn để tùy chỉnh độ sáng màn hình, thiết lập độ trễ trước khi tự động khóa, thay đổi mã PIN hoặc đổi tên thiết bị.

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

## Thêm mật khẩu BIP39

Trước khi tiếp tục, nếu muốn, bạn có thể thêm cụm mật khẩu BIP39. Cụm mật khẩu BIP39 là mật khẩu tùy chọn mà bạn có thể tự do lựa chọn và được thêm vào cụm từ ghi nhớ của bạn để tăng cường bảo mật cho ví. Khi bật tính năng này, việc truy cập vào ví Bitcoin của bạn sẽ yêu cầu cả cụm từ ghi nhớ và cụm mật khẩu. Nếu không có một trong hai, sẽ không thể khôi phục ví.

Trước khi cấu hình tùy chọn này trên Passport, chúng tôi khuyên bạn nên đọc bài viết này để hiểu đầy đủ về hoạt động lý thuyết của cụm mật khẩu và tránh các lỗi có thể dẫn đến mất bitcoin của bạn:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Để kích hoạt, hãy vào menu "*Thêm*" và nhấp vào "*Nhập mật khẩu*".

![Image](assets/fr/50.webp)

Nhập mật khẩu của bạn bằng bàn phím aA1 và đảm bảo bạn lưu mật khẩu một hoặc nhiều lần trên phương tiện vật lý (giấy hoặc kim loại). Ví dụ, tôi đang sử dụng một mật khẩu rất yếu, nhưng bạn nên chọn một mật khẩu mạnh, ngẫu nhiên, bao gồm tất cả các loại ký tự và đủ dài (như mật khẩu mạnh).

![Image](assets/fr/51.webp)

Xin lưu ý rằng mật khẩu BIP39 phân biệt chữ hoa và chữ thường. Nếu bạn nhập mật khẩu hơi khác so với mật khẩu được cấu hình ban đầu, Passport sẽ không báo lỗi, nhưng sẽ lấy một bộ khóa mật mã khác không phải là khóa trong ví ban đầu của bạn.

Do đó, điều quan trọng là khi cấu hình, hãy ghi lại dấu vân tay khóa chính mà bạn sẽ được cấp ở bước tiếp theo. Ví dụ, với mật khẩu `Plan B Network`, dấu vân tay khóa chính của tôi là `745D526B`.

![Image](assets/fr/52.webp)

Mỗi lần mở khóa Passport, bạn sẽ cần quay lại menu này để nhập mật khẩu và áp dụng vào ví của mình. Passport không lưu mật khẩu.

Mỗi lần bạn mở khóa, sau khi ghi lại mật khẩu, hãy kiểm tra trên màn hình xác nhận này xem dấu vân tay được cung cấp có giống với dấu vân tay bạn đã ghi lại trong quá trình cấu hình không. Nếu đúng, mật khẩu của bạn là chính xác và bạn đang truy cập vào đúng ví Bitcoin. Nếu không, bạn đang ở nhầm ví và cần thử lại, chú ý không nhập sai.

Trước khi bạn nhận được bitcoin đầu tiên trên ví của mình, **Tôi thực sự khuyên bạn nên thực hiện một bài kiểm tra khôi phục rỗng**. Ghi lại một số thông tin tham chiếu, chẳng hạn như xpub hoặc địa chỉ nhận đầu tiên của bạn, sau đó xóa ví của bạn trên Passport trong khi nó vẫn còn rỗng (`Cài đặt -> Nâng cao -> Xóa Hộ chiếu`). Sau đó, hãy thử khôi phục ví của bạn bằng cách sử dụng bản sao lưu giấy của cụm từ ghi nhớ và bất kỳ cụm mật khẩu nào. Kiểm tra xem thông tin cookie được tạo sau khi khôi phục có khớp với thông tin bạn đã ghi ban đầu không. Nếu có, bạn có thể yên tâm rằng bản sao lưu giấy của bạn là đáng tin cậy. Để tìm hiểu thêm về cách thực hiện khôi phục thử nghiệm, vui lòng tham khảo hướng dẫn khác này:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
![Image](assets/fr/53.webp)

## Cấu hình ví trên Sparrow Wallet

Trong hướng dẫn này, tôi sẽ chỉ cho bạn cách sử dụng Passport nâng cao với Sparrow Wallet. Tuy nhiên, ví phần cứng này cũng tương thích với Envoy (ứng dụng Foundation), Keeper, BlueWallet, Nunchuk, Spectre và nhiều ứng dụng khác...

Bắt đầu bằng cách tải xuống và cài đặt Sparrow Wallet [từ trang web chính thức](https://sparrowwallet.com/) trên máy tính của bạn, nếu bạn chưa thực hiện.

![Image](assets/fr/54.webp)

Hãy chắc chắn kiểm tra tính xác thực và tính toàn vẹn của phần mềm trước khi cài đặt. Nếu bạn không biết cách thực hiện, vui lòng tham khảo hướng dẫn này:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Sau khi mở Sparrow Wallet, hãy nhấp vào tab "*File*", sau đó nhấp vào "*New Wallet*".

![Image](assets/fr/55.webp)

Đặt tên cho ví của bạn, sau đó nhấp vào "*Tạo ví*".

![Image](assets/fr/56.webp)

Chọn "*Ví phần cứng không có kết nối mạng*".

![Image](assets/fr/57.webp)

Nhấp vào "*Quét...*" bên cạnh tùy chọn "*Hộ chiếu*". Thao tác này sẽ mở webcam của bạn.

![Image](assets/fr/58.webp)

Trên ví phần cứng của bạn, hãy vào menu "*Tài khoản*", chọn menu phụ "*Quản lý tài khoản*" và nhấp vào "*Kết nối ví*".

![Image](assets/fr/59.webp)

Trong danh sách thả xuống xuất hiện, chọn "*Sparrow*".

![Image](assets/fr/60.webp)

Sau đó chọn "*Single-sig*" để cấu hình bình thường, không có multisig.

![Image](assets/fr/61.webp)

Chọn tùy chọn "*Mã QR*".

![Image](assets/fr/62.webp)

Passport của bạn sau đó sẽ tạo mã QR động. Sử dụng webcam của máy tính để quét chúng vào phần mềm Sparrow.

![Image](assets/fr/63.webp)

Bây giờ bạn sẽ thấy dấu vân tay xpub và khóa chính của mình, chúng phải khớp với dấu vân tay hiển thị trên Hộ chiếu khi bạn nhập mật khẩu. Nhấp vào nút "*Áp dụng*".

![Image](assets/fr/64.webp)

Đặt mật khẩu mạnh để bảo mật quyền truy cập vào Ví Sparrow của bạn. Mật khẩu này sẽ bảo vệ khóa công khai, địa chỉ, nhãn và lịch sử giao dịch của bạn khỏi sự truy cập trái phép. Tốt nhất là bạn nên lưu mật khẩu này trong trình quản lý mật khẩu để không quên.

![Image](assets/fr/65.webp)

Sau đó, Hộ chiếu của bạn sẽ nhắc bạn quét địa chỉ tiếp nhận đầu tiên để xác nhận rằng quá trình nhập đã thành công.

![Image](assets/fr/66.webp)

Trong Sparrow, hãy chuyển đến tab "*Nhận*" và quét mã QR của địa chỉ đầu tiên.

![Image](assets/fr/67.webp)

Nếu thao tác thành công, Hộ chiếu của bạn sẽ hiển thị "*Đã xác minh*".

![Image](assets/fr/68.webp)

Điều này xác nhận rằng việc nhập đã thành công.

![Image](assets/fr/69.webp)

## Nhận bitcoin

Bây giờ Passport của bạn đã được thiết lập, bạn đã sẵn sàng nhận sats đầu tiên trên ví Bitcoin mới của mình. Để thực hiện, trên Sparrow, hãy nhấp vào menu "*Nhận*".

![Image](assets/fr/70.webp)

Sparrow sẽ hiển thị địa chỉ biên lai đầu tiên trống trong danh mục đầu tư của bạn. Bạn có thể thêm nhãn.

![Image](assets/fr/71.webp)

Trước khi sử dụng, chúng tôi sẽ kiểm tra địa chỉ trên màn hình Passport để đảm bảo rằng nó thuộc về ví Bitcoin của chúng tôi. Trên Sparrow, bạn có thể phóng to mã QR của địa chỉ bằng cách nhấp vào địa chỉ đó nếu cần. Trong menu "*Tài khoản*" của Passport, hãy chọn "*Công cụ tài khoản*".

![Image](assets/fr/72.webp)

Nhấp vào "*Xác minh địa chỉ*", sau đó quét mã QR hiển thị trên Ví Sparrow.

![Image](assets/fr/73.webp)

Hãy đảm bảo rằng địa chỉ hiển thị trên Hộ chiếu trùng khớp chính xác với địa chỉ hiển thị trên Sparrow và "*Đã xác minh*" phải xuất hiện.

![Image](assets/fr/74.webp)

Bây giờ bạn có thể sử dụng nó để nhận bitcoin. Khi giao dịch được phát trên mạng, nó sẽ xuất hiện trên Sparrow. Đợi cho đến khi bạn nhận được đủ xác nhận để coi giao dịch là chắc chắn.

![Image](assets/fr/75.webp)

## Gửi bitcoin

Bây giờ bạn đã có một vài sats trong ví, bạn cũng có thể gửi một ít. Để thực hiện, hãy nhấp vào menu "*UTXOs*".

![Image](assets/fr/76.webp)

Chọn UTXO bạn muốn sử dụng làm đầu vào cho giao dịch này, sau đó nhấp vào "*Gửi mục đã chọn*".

![Image](assets/fr/77.webp)

Nhập địa chỉ người nhận, nhãn ghi nhớ mục đích giao dịch và số tiền bạn muốn gửi đến địa chỉ này.

![Image](assets/fr/78.webp)

Điều chỉnh mức phí theo điều kiện thị trường hiện tại, sau đó nhấp vào "*Tạo giao dịch*".

![Image](assets/fr/79.webp)

Kiểm tra xem tất cả các thông số giao dịch đã chính xác chưa, sau đó nhấp vào "*Hoàn tất giao dịch để ký*".

![Image](assets/fr/80.webp)

Nhấp vào "*Hiển thị QR*" để hiển thị PSBT (*Giao dịch Bitcoin đã ký một phần*). Sparrow đã xây dựng giao dịch, nhưng vẫn thiếu chữ ký để mở khóa bitcoin được sử dụng trong đầu vào. Những chữ ký này chỉ có thể được thực hiện bởi Passport, nơi lưu trữ hạt giống của bạn, cung cấp quyền truy cập vào khóa riêng cần thiết để ký giao dịch.

![Image](assets/fr/81.webp)

Trên Hộ chiếu của bạn, hãy truy cập menu "*Tài khoản*" và nhấp vào "*Ký bằng Mã QR*".

![Image](assets/fr/82.webp)

Quét PSBT (*Giao dịch Bitcoin đã ký một phần*) được hiển thị trên Ví Sparrow.

![Image](assets/fr/83.webp)

Xác nhận địa chỉ nhận và số tiền gửi là chính xác, sau đó nhấn nút xác nhận.

![Image](assets/fr/84.webp)

Kiểm tra địa chỉ trao đổi. Trong ví dụ của tôi, không có địa chỉ nào vì giao dịch chỉ bao gồm một đầu ra duy nhất.

![Image](assets/fr/85.webp)

Hãy đảm bảo rằng đây là mức phí bạn đã chọn.

![Image](assets/fr/86.webp)

Nếu mọi thông tin đều chính xác, hãy nhấp vào nút xác nhận để ký giao dịch.

![Image](assets/fr/87.webp)

Trên Sparrow Wallet, nhấp vào "*Quét QR*" và quét mã QR hiển thị trên Hộ chiếu của bạn.

![Image](assets/fr/88.webp)

Giao dịch đã ký của bạn hiện đã sẵn sàng để phát trên mạng Bitcoin và được đưa vào khối bởi thợ đào. Nếu mọi thứ đều chính xác, hãy nhấp vào "*Phát Giao dịch*".

![Image](assets/fr/89.webp)

Giao dịch của bạn đã được phát sóng và đang chờ xác nhận.

![Image](assets/fr/90.webp)

Xin chúc mừng, giờ bạn đã biết cách cấu hình và sử dụng Passport. Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái màu xanh lá cây bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn vì đã chia sẻ!

Để biết thêm thông tin, hãy xem hướng dẫn của chúng tôi về phần mềm Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04