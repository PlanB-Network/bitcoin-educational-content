---
name: Nunchuk
description: Wallet di động phù hợp với tất cả
---
![cover](assets/cover.webp)



## Một Wallet mạnh mẽ


Nunchuk ra mắt vào cuối năm 2020 với triết lý rõ ràng: biến đa chữ ký thành tiêu chuẩn. Do đó, nó được thiết kế để thực hiện các chức năng rất tiên tiến, với lựa chọn có giá trị là xây dựng thiết kế trực tiếp trên Bitcoin Core, phần mềm tham chiếu cho hệ sinh thái Bitcoin.



Sau hơn 4 năm phát triển và sử dụng, nó đã sẵn sàng để thử nghiệm ở quy mô lớn. Nếu bạn là người mới bắt đầu và chưa quen với Nunchuk, hướng dẫn này sẽ giúp bạn thực hiện những bước đầu tiên và khám phá phần mềm này, với các chức năng nâng cao mà bạn có thể tìm hiểu sau khi vượt qua tác động đầu tiên. Bản thân hướng dẫn dành riêng cho người dùng trung cấp có các kỹ năng cần thiết để thực hiện tất cả các bước, nhưng nó có thể là nguồn cảm hứng cho mọi người tìm hiểu cách nâng cao kỹ năng. Chúng ta sẽ bắt đầu với phiên bản dành cho thiết bị di động và việc chỉ ra điều này là cần thiết, vì Nunchuk cũng có phần mềm để chạy trên máy tính.



## Tải về


Bước đầu tiên chắc chắn là quyết định nơi tải xuống ứng dụng. Truy cập [trang web chính thức](https://nunchuk.io/) nơi bạn có thể tìm thấy một số tài liệu (không nhiều nhưng là khởi đầu), bản trình bày tính năng cũng như, về phía cuối trang, tất cả các liên kết tải xuống.



📌 Đối với hướng dẫn này, tôi quyết định chỉ cho bạn cách tải xuống Software Wallet từ kho lưu trữ Github và cách xác minh bản phát hành trước khi cài đặt trên điện thoại di động của bạn. **Quy trình sau đây chỉ có thể thực hiện từ máy tính của bạn**, vì vậy tôi khuyên bạn nên thực hiện tất cả các bước này từ máy tính để bàn hoặc máy tính xách tay của mình và - sau khi xác minh xong - hãy chuyển tệp `.apk` sang điện thoại di động của bạn.



![image](assets/en/01.webp)



Nếu kỹ năng của bạn không quá cao, bạn có thể quyết định tải xuống `.apk` từ các cửa hàng chính thức và bỏ qua trực tiếp phần cấu hình của hướng dẫn này. Mặt khác, nếu bạn muốn thực hiện bước nhảy vọt, hãy tiếp tục làm theo từng bước.



Vì vậy, từ máy tính để bàn của bạn, hãy nhấp vào _Truy cập kho lưu trữ mã nguồn mở của chúng tôi_



Liên kết sẽ đưa bạn đến trang Github của Nunchuk, nơi bạn sẽ tìm thấy một số kho lưu trữ. Chúng tôi sẽ tập trung vào _nunchuk-android_



![image](assets/en/02.webp)



Trên màn hình tiếp theo, hãy định vị phần _Bản phát hành_ ở bên phải và chọn _Mới nhất_



![image](assets/en/03.webp)



Trong _Assets_, hãy tải xuống bản phát hành (trong ví dụ này là 1.67.apk), cùng với tệp SHA256SUMS và SHA256SUMS.asc.



![image](assets/en/04.webp)



Để tìm khóa GPG của nhà phát triển, hãy quay lại phần _Releases_ của kho lưu trữ và tìm phiên bản 1.9.53 (hoặc phiên bản cũ hơn) có chứa liên kết để lấy và tải xuống _GPG Key_



![image](assets/en/05.webp)



Chúng tôi sẽ tiến hành xác minh thông qua một công cụ tiện dụng do Sparrow wallet cung cấp, có một cửa sổ chuyên dụng cho mục đích này và hỗ trợ chữ ký PGP và SHA256 Manifest.



Sau đó khởi chạy Sparrow và từ menu _Công cụ_ chọn _Xác minh tải xuống_.



![image](assets/en/06.webp)



Trong cửa sổ bật lên, bạn sẽ thấy các trường để "điền vào": chọn nút _Browse_ ở bên phải và chọn, cho mỗi trường, các tệp tương ứng mà bạn vừa tải xuống từ Github. Khi bạn đã hoàn tất tất cả các bước, cửa sổ sẽ trông như sau, với các dấu kiểm Green và xác nhận Hash của manifest.



![image](assets/en/07.webp)


**Lưu ý: ảnh chụp màn hình này được chụp từ máy tính Windows, bạn có thể áp dụng cách này cho bất kỳ hệ điều hành nào trên máy tính của mình, chỉ cần cài đặt Sparrow wallet. Và xác minh!**



Bạn có thể tìm hướng dẫn về Sparrow wallet để tải xuống Software Wallet này


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Sau đó, bạn có thể chuyển tệp `.apk` từ máy tính sang điện thoại của bạn



![image](assets/en/08.webp)



và cài đặt Nunchuk



![image](assets/en/09.webp)



Trước khi khởi chạy Nunchuk trên điện thoại, hãy mở Orbot và đưa ứng dụng mới vào danh sách các ứng dụng sẽ được định tuyến theo Tor.



![image](assets/en/11.webp)



Bây giờ hãy chạy Nunchuk. Đối với các tính năng của dự án - không phải là chủ đề của hướng dẫn này - Nunchuk, sau khi mở, sẽ mời bạn đăng nhập qua email hoặc hồ sơ Google. Cho đến khi bạn có kế hoạch tận dụng các gói nâng cao của Nunchuk Inc, **tránh đăng nhập** và tiếp tục bằng cách chọn tùy chọn _Tiếp tục với tư cách khách_.



![image](assets/en/12.webp)



## Cài đặt


Nunchuk tự giới thiệu một cửa sổ _Trang chủ_ để trình bày, nơi bạn có thể dễ dàng hiểu được triết lý hoạt động của nó và chúng tôi sẽ trình bày chi tiết hơn sau đây.



Ở phía dưới, bạn có thể tìm thấy các menu và bước đầu tiên, hãy chọn _Hồ sơ_ để truy cập cài đặt.



![image](assets/en/10.webp)



Sau đó chọn _Cài đặt hiển thị_, tiếp tục bỏ qua lời mời tạo tài khoản.



![image](assets/en/14.webp)



Trong màn hình bên dưới, bạn có thể kiểm tra xem Wallet có trực tuyến hay không và bạn có thể kết nối máy chủ của mình hay không, hãy chú ý kỹ hướng dẫn tại liên kết được cung cấp khi nhấp vào _hướng dẫn này_.



![image](assets/en/15.webp)



Lưu cài đặt bằng lệnh _Save network settings_, quay lại menu _Profile_ và chọn _Security settings_.



![image](assets/en/16.webp)



Từ menu này, bạn thiết lập cách bảo vệ việc mở ứng dụng. Để ngăn chặn truy cập không mong muốn, bạn có thể bảo vệ Nunchuk bằng sinh trắc học của điện thoại và/hoặc thêm mã PIN bảo mật.



![image](assets/en/17.webp)



Ngoài ra, hãy xem menu _Giới thiệu_ mà bạn luôn tìm thấy trong cửa sổ _Hồ sơ_



![image](assets/en/18.webp)



cho phép bạn kiểm tra phiên bản ứng dụng hoặc liên hệ với nhà phát triển nếu cần.



![image](assets/en/19.webp)



## Tạo khóa và Wallet


Như dễ dàng đoán được từ triết lý của Nunchuk, phần mềm này được thiết kế như một công cụ hữu ích để quản lý Ví đa chữ ký. Để thực hiện chức năng này, Nunchuk cho phép tạo Wallet bằng cách tách chúng khỏi các khóa cần thiết để sắp xếp chữ ký số.



Trên thực tế, hoạt động lý tưởng của Nunchuk liên quan đến việc tạo ra các Ví chỉ có thể xem, phụ thuộc vào các khóa có thể là "Cold".



Trong các màn hình trước, bạn có thể nhận thấy có một menu ở phía dưới có tên là _Keys_. Nếu bạn vừa tải Nunchuk, trong cả _Home_ và _Keys_, bạn sẽ thấy một nút lớn mời bạn thêm phím, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Đây chính xác là cách Nunchuk hoạt động:** trước tiên bạn nhập generate/nhập khóa, sau đó tạo Wallet, cấu hình để chọn khóa nào sẽ cho phép mở khóa số tiền được lưu trữ trong đó.



Ngay cả trong trường hợp Wallet singlesig, trước tiên bạn tạo khóa và sau đó mới tạo Wallet. Và đó chính xác là những gì chúng ta sẽ làm bây giờ, bắt đầu với Wallet singlesig để phá vỡ sự ngại ngùng và khám phá các chức năng của Nunchuk.



Nhấp vào _Thêm khóa_



![image](assets/en/22.webp)



Nunchuk hiển thị một số thiết bị chữ ký được hỗ trợ nhưng để bắt đầu, hãy chọn _Phần mềm_.



![image](assets/en/23.webp)



Nunchuk sẽ generate một Mnemonic sẽ được lưu trữ trên thiết bị. Sau đó, bạn cần viết ra trình tự các từ để sao lưu, tạo ra các điều kiện môi trường tốt nhất và đảm bảo bạn có thời gian để thực hiện tốt và lặng lẽ. Phần mềm chỉ hiển thị Mnemonic một lần, cho dù bạn chọn hiển thị ngay hay sau, vì vậy hãy chọn _Tạo và sao lưu ngay_.



![image](assets/en/24.webp)



Nunchuk tạo ra các câu Mnemonic gồm 24 từ, xuất hiện ngay trên màn hình tiếp theo



![image](assets/en/25.webp)



và sau đó tiến hành kiểm tra nhanh, yêu cầu bạn chọn từ đúng trong 3 lựa chọn tương ứng với số trong chuỗi Mnemonic.


Nếu bạn đã viết đúng Mnemonic, nút _Continue_ sẽ hoạt động. Nhấn nút đó để tiếp tục.



![image](assets/en/26.webp)



Đặt tên cho khóa của bạn và nhấn _Tiếp tục_.



![image](assets/en/27.webp)



Vào cuối các bước này, bạn sẽ được hỏi có nên thêm [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39) vào cụm từ Mnemonic của bạn hay không. Nếu bạn không có đủ kiến thức cần thiết về cách sử dụng passphrase, sắp xếp sao lưu hoặc cách thức hoạt động của passphrase, tôi khuyên bạn nên chọn _Tôi không cần cụm mật khẩu_.



![image](assets/en/28.webp)



Cuối cùng, khóa sẽ được tạo và hiển thị cho bạn trong menu:




- Với _Key Spec_ dấu vân tay chính được chỉ định
- Bạn có cài đặt, ba dấu chấm ở trên cùng bên phải, nơi bạn có thể xóa khóa hoặc ký tin nhắn
- Bên cạnh tên khóa, bạn sẽ thấy biểu tượng ngòi bút, nhấp vào đó bạn có thể chỉnh sửa tên khóa, ví dụ để sắp xếp các khóa theo thứ tự trong tương lai.
- Lệnh cuối cùng, bạn có thể kiểm tra tình trạng của khóa: bằng cách nhấn _Chạy kiểm tra tình trạng_, bạn có thể yêu cầu ứng dụng kiểm tra xem khóa có bị xâm phạm không.



Khi bạn đã xong, hãy nhấp vào _Xong_



![image](assets/en/29.webp)



Trong menu _Keys_ bạn sẽ thấy phím đầu tiên của mình xuất hiện.



![image](assets/en/30.webp)



Bằng cách vào menu _Trang chủ_, tùy chọn tạo Wallet sẽ xuất hiện. Nhấp vào _Tạo ví mới_.



![image](assets/en/31.webp)



Nunchuk cho bạn thấy một số khả năng chủ yếu liên quan đến các dịch vụ mà công ty cung cấp không phải là chủ đề của hướng dẫn này.



Trong hướng dẫn này, chúng tôi sẽ tạo _Hot Wallet và _Ví tùy chỉnh_ bằng cách trình bày chi tiết.


Hãy bắt đầu với _Ví tùy chỉnh_.



![image](assets/en/32.webp)



Theo cách đơn giản, ứng dụng sẽ yêu cầu bạn đặt tên cho Wallet mới này và chọn tập lệnh cho các địa chỉ. Đối với hướng dẫn, tôi đã chọn để mặc định là _Native segwit_. Khi bạn hoàn tất, hãy chọn _Continue_



![image](assets/en/33.webp)



Cấu hình của Wallet tiếp tục yêu cầu bạn thiết lập khóa nào để mở khóa tiền của Wallet này. Nếu có nhiều khóa, bạn sẽ thấy danh sách để lựa chọn. Hiện tại chúng tôi chỉ tạo một khóa, vì vậy chúng tôi chọn đánh dấu kiểm vào khóa đó. Ở góc dưới bên phải, bạn có thể thấy Nunchuk sẽ yêu cầu bạn thiết lập chữ ký đa Wallet trong tương lai của mình, tăng số lượng _Khóa bắt buộc_.



![image](assets/en/34.webp)



Vì chúng ta đang tạo một chữ ký đơn, chúng ta để nguyên `1` và nhấp vào _Tiếp tục_.



Cuối cùng, màn hình xác minh sẽ xuất hiện, tại đó bạn có thể kiểm tra các tính năng của Wallet:




- tên
- `1/1 Multisig` tage, đó là cách Nunchuk đặt tên cho Wallet singlesig
- loại tập lệnh, `SegWit bản địa`
- chìa khóa `Keys`, với dấu vân tay và đường dẫn dẫn xuất của nó



Khi bạn đã hài lòng, hãy nhấn _Tạo ví_



![image](assets/en/35.webp)



Wallet đã được tạo và bạn có thể tải xuống tệp [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) làm bản sao lưu. Để quay lại menu chính, hãy nhấp vào mũi tên ở góc trên bên trái.



![image](assets/en/36.webp)



Bạn đang ở _Trang chủ_, nơi bạn sẽ thấy Wallet mới tạo báo cáo số dư và trạng thái của kết nối. Bằng cách nhấp vào khoảng trống màu xanh, bạn có thể truy cập các chức năng chính của Wallet.



![image](assets/en/37.webp)





- Biểu tượng ống kính ở góc trên bên phải cho phép bạn thực hiện tìm kiếm giao dịch;
- `Xem cấu hình Wallet` cung cấp quyền truy cập vào menu cấu hình, nơi bạn có thể chỉnh sửa tên của Wallet và bật các tùy chọn nâng cao, góc trên bên phải (bạn không thể lấy ảnh chụp màn hình). Tại đây, bạn có thể xuất cấu hình Wallet, nhãn, thay thế khóa, thay đổi [giới hạn khoảng cách](https://planb.network/en/resources/glossary/gap-limit) và nhiều hơn nữa.



## Giao dịch với Nunchuk



Giải thưởng _Nhận_



![image](assets/en/38.webp)



Ứng dụng được lập trình để hiển thị Mã QR của Address hoặc sao chép/chia sẻ scriptPubKey để nhận tiền trên chuỗi khối.



![image](assets/en/39.webp)



Chúng tôi đã có một chiếc UTXO đến vào ngày Address đầu tiên này,



![image](assets/en/40.webp)



nhưng chúng ta vẫn nhấp vào _Nhận_ để nhận thêm một cái nữa.



![image](assets/en/41.webp)



Mục đích là để bạn biết rằng Nunchuk báo cáo Address mới này cho bạn là _Địa chỉ chưa sử dụng_ nhưng cũng cho bạn biết rằng bạn có _Địa chỉ đã sử dụng_ và số lượng địa chỉ đó.



### Giao dịch chi tiêu với kiểm soát tiền xu



Khi UTXO thứ hai này cũng đã đến, hãy quay lại màn hình chính của Wallet để kiểm tra trạng thái của hai giao dịch đến và quan trọng nhất là nhấp vào tùy chọn _Xem tiền xu_



![image](assets/en/42.webp)



nơi bạn sẽ được hiển thị các UTXO riêng lẻ. Tại đây, bạn có thể chọn xem một UTXO cụ thể bằng cách nhấp vào mũi tên nhỏ bên cạnh số lượng



![image](assets/en/43.webp)



và kiểm tra khi nào nhận được, mô tả, chặn UTXO để không bị mất và nhiều hơn nữa.



![image](assets/en/44.webp)



Nhưng nếu bạn quay lại menu _Coins_ bằng cách nhấp vào mũi tên ở góc trên bên phải, bạn có thể bật "Kiểm soát Coin" để chi tiêu UTXO của mình theo cách có kiểm soát hơn.



Trong ví dụ sau, tôi chọn UTXO trong số 21.000 Sats, sau đó nhấp vào biểu tượng ở góc dưới bên trái.



![image](assets/en/45.webp)



Nunchuk tự động mở cửa sổ _Giao dịch mới_ để chi tiêu UTXO này. Trong giao dịch chi tiêu, trước tiên, bạn phải đặt số tiền theo cách thủ công hoặc bằng cách chọn _Gửi tất cả số đã chọn_ để gửi tất cả số dư kiểm soát tiền xu, mà không tạo số dư còn lại. Sau khi đặt số tiền, hãy chọn _Tiếp tục_



![image](assets/en/46.webp)



Bây giờ Nunchuk sẽ hiển thị nơi dán Address để chuyển tiền, mô tả chi tiết và hoàn tất giao dịch.



![image](assets/en/47.webp)



Chọn _Create transaction_ sẽ chuyển giao việc quản lý phí và giao dịch tự động cho ứng dụng. Tôi khuyên bạn nên chọn _Custom transaction_ để kiểm soát tốt hơn.



Trong màn hình mới này, điều quan trọng là phải chọn




- _Trừ phí khỏi số tiền gửi_, để tránh việc phải trả phí bởi một UTXO khác có trong Wallet, chi tiêu số tiền đó và tạo ra số dư (đây là một mất mát riêng tư có thể tránh được);
- và sau đó thiết lập phí thủ công sau khi kiểm tra trên trình khám phá.



Sau khi thực hiện tất cả các bước này, hãy nhấp vào _Tiếp tục_



![image](assets/en/48.webp)



Màn hình tiếp theo là tóm tắt đầy đủ về giao dịch. Nếu mọi thứ đều ổn, hãy xác nhận bằng cách chọn _Xác nhận và tạo giao dịch_.



![image](assets/en/49.webp)



Với _Chữ ký đang chờ_, Nunchuk sẽ thông báo cho bạn rằng giao dịch đang chờ chữ ký của bạn để chấp thuận khoản chi, bạn sẽ ký vào đó bằng cách nhấp vào _Ký_.



![image](assets/en/50.webp)



Lệnh _Broadcast_ xuất hiện ở phía dưới để truyền bá giao dịch đã hoàn tất và được ký.



![image](assets/en/51.webp)



### Giao dịch chi tiêu từ menu _Gửi_



Trong khi trên trang chính của Wallet, chúng ta thấy giao dịch đang được thực hiện và chờ xác nhận, chúng ta sử dụng menu _Gửi_ để mô phỏng chi phí hàng ngày.



![image](assets/en/52.webp)



Trên thực tế, khi nhấp vào _Gửi_, màn hình gửi giao dịch sẽ hiện ra, giống như màn hình vừa thấy nhưng không cần phải thông qua khâu kiểm soát tiền xu.



Cũng trong ví dụ thứ hai này, tôi quyết định chọn _Giao dịch tùy chỉnh_ và gửi toàn bộ số tiền, nhưng tôi có thể thiết lập thủ công. Sau khi bạn đã quyết định số tiền cần gửi, hãy nhấn _Tiếp tục_.



![image](assets/en/53.webp)



Sau đó, luôn đưa ra trường hợp liệu phí có được trừ khỏi UTXO hay không (trong ví dụ này, lựa chọn là bắt buộc vì chỉ có một lựa chọn), điều chỉnh thủ công phí theo tình hình tại thời điểm đó trong Mempool và nhấn _Tiếp tục_.



![image](assets/en/54.webp)



Nếu màn hình tóm tắt đáp ứng yêu cầu, hãy chọn _Xác nhận và tạo giao dịch_.



![image](assets/en/55.webp)



Ký giao dịch bằng _Sign_



![image](assets/en/56.webp)



và truyền nó vào mạng.



![image](assets/en/57.webp)



Wallet hiện đang ở thời điểm này với số dư bằng 0 và lịch sử đang được cập nhật.



![image](assets/en/58.webp)



## Tạo ra "Hot Wallet"



Cuối cùng và không bỏ sót bất cứ điều gì từ giai đoạn đầu của Nunchuk di động, chúng ta hãy xem cách nó tạo ra thứ mà ứng dụng gọi là "Hot Wallet".



Trong menu _Trang chủ_ của Nunchuk, nơi hiển thị danh sách Ví, hãy nhấp vào `+` ở góc trên bên phải.



![image](assets/en/59.webp)



Chọn _Ví nóng_ từ các tùy chọn



![image](assets/en/60.webp)



Nunchuk đưa ra một số lời khuyên về cách xử lý Ví Hot trên trang trình bày, nơi bạn sẽ chọn _Tiếp tục_ để tiếp tục.



![image](assets/en/61.webp)



Sau một vài phút, Wallet được tạo và xuất hiện trong danh sách với màu nâu. Đây là màu mà Nunchuk cảnh báo bạn rằng bạn chưa sao lưu Wallet.



![image](assets/en/62.webp)



Nhấp vào tên Wallet để truy cập cấu hình của nó và bạn có thể thấy lời mời sao lưu cụm từ Mnemonic ngay lập tức.



![image](assets/en/63.webp)



Quy trình này giống như chúng ta đã thấy trước đây, vì vậy chúng ta sẽ không đứng lại để xem lại nữa. Sau khi hoàn tất, Nunchuk sẽ đưa bạn đến trang khóa có liên quan, bạn có thể chỉnh sửa trang này thành trang bạn đã tạo bằng quy trình _Custom_.



![image](assets/en/64.webp)



Cũng hãy thử _Chạy kiểm tra sức khỏe_



![image](assets/en/65.webp)



hoặc để xem cách hiển thị tất cả Ví của bạn trong _Trang chủ_ của ứng dụng.



![image](assets/en/66.webp)



## Để ghi nhớ để tiếp tục độc lập


Tương tự như thứ tự tạo, nghĩa là đầu tiên tạo khóa rồi đến Wallet, bạn sẽ cần phải duy trì thứ tự ngược lại để xóa các mục này khỏi ứng dụng của mình.



Nếu bạn cần xóa một trong các khóa, trước tiên bạn phải có tầm nhìn xa để xóa Wallet hoặc Ví, sử dụng một trong các khóa chữ ký cho các giao dịch: trước tiên bạn xóa Ví và sau đó mới xóa các khóa. Nếu bạn không làm theo thứ tự này, bạn sẽ thấy mình không thể xóa khóa.



Bây giờ bạn đã biết cách bắt đầu với Nunchuk, bạn có thể tiếp tục nghiên cứu ứng dụng này và khám phá những bí mật của nó. Trong hướng dẫn này, chúng tôi chỉ thực hiện những bước đầu tiên, nhưng có những ứng dụng phức tạp hơn và nhu cầu nâng cao mà Software Wallet này có thể giúp bạn đáp ứng.