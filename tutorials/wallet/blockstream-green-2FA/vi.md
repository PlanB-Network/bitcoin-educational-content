---
name: Blockstream Green - 2FA
description: Thiết lập 2/2 multisig trên Green Wallet
---
![cover](assets/cover.webp)


___


***Lưu ý:*** Kể từ tháng 5 năm 2025, sẽ không thể kích hoạt tài khoản mới được bảo vệ bằng xác thực hai yếu tố (2FA) nữa. Tính năng này chỉ khả dụng đối với những người dùng đã kích hoạt loại tài khoản này trước đó


___


Phần mềm wallet là một ứng dụng được cài đặt trên máy tính, điện thoại thông minh hoặc thiết bị kết nối Internet khác, cho phép bạn quản lý và bảo mật các khóa Bitcoin và wallet của mình. Không giống như các thiết bị wallet phần cứng, vốn cách ly các khóa riêng tư, các thiết bị wallet "nóng" hoạt động trong môi trường có nguy cơ bị tấn công mạng, làm tăng nguy cơ vi phạm bản quyền và trộm cắp.


Các thiết bị Software wallet nên được sử dụng để quản lý một lượng bitcoin hợp lý, đặc biệt là cho các giao dịch hàng ngày. Chúng cũng có thể là một lựa chọn thú vị cho những người có tài sản bitcoin hạn chế, đối với họ việc đầu tư vào một thiết bị wallet phần cứng có vẻ không tương xứng. Tuy nhiên, việc chúng liên tục tiếp xúc với Internet khiến chúng kém an toàn hơn khi lưu trữ tiền tiết kiệm dài hạn hoặc các khoản tiền lớn. Đối với trường hợp sau, tốt nhất nên chọn các giải pháp an toàn hơn, chẳng hạn như thiết bị wallet phần cứng.


Trong hướng dẫn này, tôi sẽ chỉ cho bạn cách tăng cường bảo mật cho một thiết bị wallet đang bị tấn công bằng tùy chọn "*2FA*" trên Blockstream Green.


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## Giới thiệu Blockstream Green


Blockstream Green là phần mềm wallet có sẵn trên thiết bị di động và máy tính để bàn. Trước đây được biết đến với tên gọi *Green Address*, wallet này đã trở thành một dự án của Blockstream sau khi được công ty này mua lại vào năm 2016.


Green là một ứng dụng đặc biệt dễ sử dụng, điều này khiến nó trở nên thú vị đối với người mới bắt đầu. Nó cung cấp tất cả các tính năng thiết yếu của một Bitcoin, wallet tốt, bao gồm RBF (*Thay thế bằng phí*), tùy chọn kết nối Tor, khả năng kết nối nút riêng của bạn, SPV (*Xác minh thanh toán đơn giản*), gắn thẻ và kiểm soát tiền điện tử.


Blockstream Green cũng hỗ trợ mạng Liquid, một sidechain của Bitcoin được phát triển bởi Blockstream để thực hiện các giao dịch nhanh chóng và bảo mật bên ngoài mạng chính blockchain. Trong hướng dẫn này, chúng ta tập trung hoàn toàn vào Bitcoin, nhưng tôi cũng đã tạo một hướng dẫn khác để học cách sử dụng Liquid trên Green:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Tùy chọn 2/2 multisig (2FA)


Trên Green, bạn có thể tạo một wallet "chỉ dùng một chữ ký" cổ điển. Nhưng bạn cũng có tùy chọn "multisig xác thực hai yếu tố (2FA)", giúp tăng cường bảo mật cho wallet của bạn mà không làm phức tạp việc quản lý hàng ngày.


Vì vậy, bạn sẽ thiết lập cấu hình 2/2 multisig wallet, có nghĩa là mỗi giao dịch sẽ yêu cầu chữ ký của hai khóa. Khóa đầu tiên, được tạo ra từ cụm từ ghi nhớ gồm 12 hoặc 24 từ của bạn, được bảo mật cục bộ bằng mã PIN trên điện thoại của bạn. Bạn có toàn quyền kiểm soát khóa này. Khóa thứ hai được lưu giữ trên máy chủ của Blockstream và việc sử dụng nó để ký yêu cầu xác thực, có thể được thực hiện thông qua mã nhận được qua email, SMS, cuộc gọi điện thoại hoặc, như chúng ta sẽ thấy trong hướng dẫn này, thông qua một ứng dụng xác thực (Authy, Google Authenticator, v.v.).


Để đảm bảo quyền tự chủ của bạn trong trường hợp Blockstream gặp sự cố (ví dụ: trường hợp công ty phá sản hoặc máy chủ lưu trữ khóa thứ hai bị phá hủy), một cơ chế khóa thời gian sẽ được áp dụng cho multisig của bạn. Cơ chế này sẽ chuyển đổi multisig 2/2 thành multisig 1/2 sau khoảng một năm (hoặc chính xác là 51.840 khối, nhưng giá trị này có thể thay đổi), sau đó wallet của bạn sẽ chỉ cần khóa cục bộ để chi tiêu bitcoin. Vì vậy, nếu bạn mất quyền truy cập vào máy chủ của Blockstream hoặc xác thực 2FA, bạn chỉ cần đợi tối đa một năm để có thể tự do sử dụng bitcoin của mình với ứng dụng mà không cần phụ thuộc vào Blockstream.


![GREEN 2FA MULTISIG](assets/fr/02.webp)


Phương pháp này giúp tăng cường đáng kể tính bảo mật cho thiết bị wallet của bạn, đồng thời cho phép bạn kiểm soát bitcoin và sử dụng chúng hàng ngày một cách dễ dàng. Tuy nhiên, phương pháp này yêu cầu làm mới khóa thời gian thường xuyên để duy trì tính bảo mật của xác thực hai yếu tố (2FA). Thời gian đếm ngược 360 ngày, trong đó tiền của bạn được bảo vệ bởi 2FA, bắt đầu ngay khi bạn nhận được bitcoin. Nếu sau 360 ngày kể từ khi nhận được bitcoin, bạn không thực hiện giao dịch nào bằng số tiền này, bitcoin của bạn sẽ chỉ được bảo vệ bằng khóa cục bộ của bạn, mà không có 2FA.


Hạn chế này khiến tùy chọn xác thực hai yếu tố (2FA) phù hợp hơn với tài khoản wallet dùng cho chi tiêu, nơi các giao dịch thường xuyên tự động gia hạn thời hạn khóa. Đối với tài khoản wallet tiết kiệm dài hạn, điều này có thể gây ra vấn đề, vì bạn sẽ cần phải cân nhắc thực hiện giao dịch chuyển tiền tự động cho chính mình mỗi năm trước khi thời hạn khóa hết hạn.


Một nhược điểm khác của phương pháp bảo mật này là bạn sẽ phải sử dụng các mẫu script thiểu số. Điều này có nghĩa là, từ góc độ quyền riêng tư, mọi thứ trở nên phức tạp hơn: rất ít người sử dụng cùng loại script với bạn, khiến người ngoài dễ dàng nhận diện dấu vân tay wallet của bạn. Hơn nữa, các script này sẽ phát sinh chi phí giao dịch cao hơn do kích thước lớn hơn của chúng.


Nếu bạn không muốn sử dụng tùy chọn xác thực hai yếu tố (2FA) và chỉ muốn thiết lập wallet "singlesig" trên Green, tôi mời bạn tham khảo hướng dẫn khác này:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Cài đặt và cấu hình phần mềm Blockstream Green


Bước đầu tiên tất nhiên là tải xuống ứng dụng Green. Hãy vào cửa hàng ứng dụng của bạn:



- [Dành cho Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Dành cho Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


Đối với người dùng Android, bạn cũng có thể cài đặt ứng dụng thông qua tệp `.apk` [có sẵn trên GitHub của Blockstream](https://github.com/Blockstream/green_android/releases).


![GREEN 2FA MULTISIG](assets/fr/04.webp)


Khởi động ứng dụng, sau đó tích vào ô "Tôi chấp nhận các điều khoản...".


![GREEN 2FA MULTISIG](assets/fr/05.webp)


Khi bạn mở Green lần đầu tiên, màn hình chính sẽ hiện ra mà không có wallet nào được cấu hình sẵn. Sau này, nếu bạn tạo hoặc nhập wallet, chúng sẽ xuất hiện trong giao diện này. Trước khi tiến hành tạo wallet, tôi khuyên bạn nên điều chỉnh cài đặt ứng dụng cho phù hợp với nhu cầu của mình. Nhấp vào "Cài đặt ứng dụng".


![GREEN 2FA MULTISIG](assets/fr/06.webp)


Tùy chọn "Bảo mật nâng cao", chỉ có trên Android, giúp tăng cường bảo mật bằng cách vô hiệu hóa chụp ảnh màn hình và ẩn bản xem trước ứng dụng. Nó cũng tự động khóa quyền truy cập ứng dụng ngay khi điện thoại của bạn bị khóa, khiến dữ liệu của bạn khó bị lộ hơn.


![GREEN 2FA MULTISIG](assets/fr/07.webp)


Đối với những người muốn tăng cường quyền riêng tư, ứng dụng cung cấp tùy chọn mã hóa lưu lượng truy cập của bạn thông qua Tor, một mạng lưới mã hóa tất cả các kết nối và khiến hoạt động của bạn khó bị theo dõi. Mặc dù tùy chọn này có thể làm chậm hoạt động của ứng dụng một chút, nhưng nó rất được khuyến khích để bảo vệ quyền riêng tư của bạn, đặc biệt nếu bạn không sử dụng node riêng hoàn chỉnh của mình.


![GREEN 2FA MULTISIG](assets/fr/08.webp)


Đối với người dùng sở hữu node hoàn chỉnh riêng, Green và Wallet cung cấp khả năng kết nối với node đó thông qua máy chủ Electrum, đảm bảo kiểm soát hoàn toàn thông tin mạng Bitcoin và việc phân phối giao dịch.


![GREEN 2FA MULTISIG](assets/fr/09.webp)


Một tính năng thay thế khác là tùy chọn "*Xác minh SPV*", cho phép bạn xác minh trực tiếp một số dữ liệu blockchain nhất định và do đó giảm bớt sự cần thiết phải tin tưởng vào nút mặc định của Blockstream, mặc dù phương pháp này không cung cấp tất cả các đảm bảo như full node.


![GREEN 2FA MULTISIG](assets/fr/10.webp)


Sau khi điều chỉnh các cài đặt theo nhu cầu của bạn, hãy nhấp vào nút "Lưu" và khởi động lại ứng dụng.


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## Tạo Bitcoin wallet trên Blockstream Green


Giờ bạn đã sẵn sàng tạo Bitcoin wallet. Nhấp vào nút "*Bắt đầu*".


![GREEN 2FA MULTISIG](assets/fr/12.webp)


Bạn có thể chọn tạo wallet phần mềm cục bộ hoặc quản lý wallet ngoại tuyến thông qua wallet phần cứng. Trong hướng dẫn này, chúng ta sẽ tập trung vào việc tạo wallet hoạt động, vì vậy bạn cần chọn tùy chọn "*Trên thiết bị này*".


![GREEN 2FA MULTISIG](assets/fr/13.webp)


Sau đó, bạn có thể chọn khôi phục Bitcoin/wallet hiện có hoặc tạo một thiết bị mới. Trong hướng dẫn này, chúng ta sẽ tạo một wallet mới. Tuy nhiên, nếu bạn cần khôi phục Bitcoin/wallet hiện có từ cụm từ ghi nhớ của nó, ví dụ như sau khi mất điện thoại cũ, bạn cần chọn tùy chọn thứ hai.


![GREEN 2FA MULTISIG](assets/fr/14.webp)


Sau đó, bạn có thể chọn giữa cụm từ ghi nhớ gồm 12 từ hoặc 24 từ. Cụm từ này sẽ cho phép bạn khôi phục quyền truy cập vào wallet của mình từ bất kỳ phần mềm tương thích nào trong trường hợp điện thoại của bạn gặp sự cố. Hiện tại, việc chọn cụm từ 24 từ không mang lại tính bảo mật cao hơn so với cụm từ 12 từ. Do đó, tôi khuyên bạn nên chọn cụm từ ghi nhớ 12 từ.


Green sẽ cung cấp cho bạn cụm từ ghi nhớ. Trước khi tiếp tục, hãy chắc chắn rằng bạn không bị theo dõi. Nhấp vào "*Hiển thị cụm từ khôi phục*" để hiển thị nó trên màn hình.


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**Cụm từ ghi nhớ này cho phép bạn truy cập đầy đủ và không hạn chế vào tất cả bitcoin của mình**. Bất kỳ ai sở hữu cụm từ này đều có thể đánh cắp tiền của bạn, ngay cả khi không có quyền truy cập vật lý vào điện thoại của bạn (trừ trường hợp khóa thời gian đã hết hạn hoặc xác thực hai yếu tố trong trường hợp wallet 2/2 trên Green).


Nó cho phép bạn khôi phục quyền truy cập vào các khóa cục bộ của mình trong trường hợp điện thoại bị mất, bị đánh cắp hoặc bị hỏng. Vì vậy, điều rất quan trọng là phải sao lưu cẩn thận **trên phương tiện vật lý (không phải kỹ thuật số)** và lưu trữ ở nơi an toàn. Bạn có thể viết nó ra giấy, hoặc để tăng cường bảo mật, nếu đó là một thiết bị wallet lớn, tôi khuyên bạn nên khắc nó lên giá đỡ bằng thép không gỉ để bảo vệ nó khỏi nguy cơ hỏa hoạn, lũ lụt hoặc sụp đổ (đối với một thiết bị wallet được thiết kế để bảo vệ một lượng nhỏ bitcoin, bản sao lưu bằng giấy đơn giản có lẽ là đủ).


*Rõ ràng là bạn tuyệt đối không được chia sẻ những từ ngữ này trên Internet, như tôi đã làm trong hướng dẫn này. Đoạn mã mẫu wallet này chỉ được sử dụng trên Testnet và sẽ bị xóa khi kết thúc hướng dẫn.*


![GREEN 2FA MULTISIG](assets/fr/16.webp)


Sau khi bạn đã ghi lại chính xác cụm từ ghi nhớ của mình vào một phương tiện vật lý, hãy nhấp vào "*Tiếp tục*". Green Wallet sau đó sẽ yêu cầu bạn xác nhận một số từ trong cụm từ ghi nhớ để đảm bảo bạn đã ghi lại chúng chính xác. Hãy điền vào chỗ trống những từ còn thiếu.


![GREEN 2FA MULTISIG](assets/fr/17.webp)


Hãy chọn mã PIN cho thiết bị của bạn, mã này sẽ được sử dụng để mở khóa Green hoặc wallet. Đây là biện pháp bảo vệ bạn khỏi sự truy cập vật lý trái phép. Mã PIN này không liên quan đến việc tạo ra các khóa mã hóa của wallet. Vì vậy, ngay cả khi không có mã PIN này, việc sở hữu cụm từ ghi nhớ gồm 12 hoặc 24 từ sẽ cho phép bạn truy cập lại các khóa cục bộ của mình.


Chúng tôi khuyên bạn nên chọn mã PIN 6 chữ số càng ngẫu nhiên càng tốt. Hãy nhớ lưu mã này để không quên, nếu không bạn sẽ buộc phải lấy lại wallet từ hộp nhớ. Sau đó, bạn có thể thêm tùy chọn khóa sinh trắc học để tránh phải nhập mã PIN mỗi khi sử dụng. Nói chung, sinh trắc học kém an toàn hơn nhiều so với mã PIN. Vì vậy, theo mặc định, tôi khuyên bạn không nên thiết lập tùy chọn mở khóa này.


![GREEN 2FA MULTISIG](assets/fr/18.webp)


Nhập mã PIN lần thứ hai để xác nhận.


![GREEN 2FA MULTISIG](assets/fr/19.webp)


Hãy đợi cho đến khi tài khoản wallet của bạn được tạo xong, sau đó nhấp vào nút "*Tạo tài khoản*".


![GREEN 2FA MULTISIG](assets/fr/20.webp)


Sau đó, bạn có thể chọn giữa wallet tiêu chuẩn có chữ ký đơn hoặc wallet được bảo vệ bằng xác thực hai yếu tố (2FA). Trong hướng dẫn này, chúng ta sẽ chọn tùy chọn thứ hai.


![GREEN 2FA MULTISIG](assets/fr/21.webp)


Bitcoin multisig wallet của bạn đã được tạo bằng ứng dụng Green!


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## Thiết lập xác thực hai yếu tố (2FA)


Nhấp vào tài khoản của bạn.


![GREEN 2FA MULTISIG](assets/fr/23.webp)


Nhấp vào nút màu xanh lá cây "*Tăng cường bảo mật cho tài khoản của bạn bằng cách thêm xác thực hai yếu tố*".


![GREEN 2FA MULTISIG](assets/fr/24.webp)


Sau đó, bạn sẽ có thể chọn phương thức xác thực để truy cập vào khóa thứ hai của thiết bị 2/2 multisig. Trong hướng dẫn này, chúng ta sẽ sử dụng một ứng dụng xác thực. Nếu bạn chưa quen với loại ứng dụng này, tôi khuyên bạn nên tham khảo hướng dẫn của chúng tôi về Authy:


https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Chọn "*Ứng dụng xác thực*".


![GREEN 2FA MULTISIG](assets/fr/25.webp)


Green sau đó sẽ hiển thị mã QR và khóa khôi phục. Khóa này cho phép bạn khôi phục quyền truy cập vào xác thực hai yếu tố (2FA) trong trường hợp mất ứng dụng Authy. Bạn nên sao lưu khóa này một cách an toàn, mặc dù bạn vẫn có thể khôi phục quyền truy cập vào bitcoin của mình sau khi thời gian khóa hết hạn, như đã giải thích ở trên.


Trong ứng dụng xác thực của bạn, hãy thêm mã mới, sau đó quét mã QR do Green cung cấp.


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*Rõ ràng là bạn tuyệt đối không được chia sẻ khóa và mã QR này trên Internet, như tôi đang làm trong hướng dẫn này. Mẫu wallet này chỉ được sử dụng trên Testnet và sẽ bị xóa khi kết thúc hướng dẫn.*


Nhấp vào nút "*Tiếp tục*".


![GREEN 2FA MULTISIG](assets/fr/27.webp)


Nhập mã động gồm 6 chữ số có trên ứng dụng xác thực của bạn.


![GREEN 2FA MULTISIG](assets/fr/28.webp)


Xác thực hai yếu tố hiện đã được kích hoạt.


![GREEN 2FA MULTISIG](assets/fr/29.webp)


Bằng cách duyệt qua menu này, bạn cũng có thể thiết lập thời gian khóa. Bộ đếm ngược này bắt đầu ngay khi Bitcoin được nhận và sau khi thời gian khóa hết hạn, tiền của bạn chỉ có thể được chi tiêu bằng khóa cục bộ mà không cần xác thực hai yếu tố (2FA). Thời gian mặc định được đặt là 12 tháng, nhưng đối với wallet dùng để tiết kiệm, bạn nên chọn 15 tháng để giảm thiểu tần suất gia hạn khóa. Ngược lại, đối với wallet dùng để chi tiêu, thời gian khóa 6 tháng có thể phù hợp hơn, vì nó sẽ được gia hạn thường xuyên với các giao dịch hàng ngày của bạn, và thời gian khóa ngắn hơn sẽ giảm thời gian chờ đợi trong trường hợp xảy ra sự cố với 2FA. Bạn có thể tự quyết định thời gian khóa phù hợp nhất với mình.


![GREEN 2FA MULTISIG](assets/fr/30.webp)


Bạn có thể thoát khỏi menu này. multisig wallet của bạn đã sẵn sàng!


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## Thiết lập wallet của bạn trên Blockstream Green


Nếu bạn muốn cá nhân hóa chiếc wallet của mình, hãy nhấp vào ba dấu chấm nhỏ ở góc trên bên phải.


![GREEN 2FA MULTISIG](assets/fr/32.webp)


Tùy chọn "*Đổi tên*" cho phép bạn tùy chỉnh tên của wallet, điều này đặc biệt hữu ích nếu bạn quản lý nhiều wallet trên cùng một ứng dụng.


![GREEN 2FA MULTISIG](assets/fr/33.webp)


Menu "*Đơn vị*" cho phép bạn thay đổi đơn vị cơ bản của wallet. Ví dụ, bạn có thể chọn hiển thị nó bằng satoshi thay vì bitcoin.


![GREEN 2FA MULTISIG](assets/fr/34.webp)


Menu "*Cài đặt*" cho phép truy cập vào các tùy chọn khác nhau của Bitcoin wallet.


![GREEN 2FA MULTISIG](assets/fr/35.webp)


Ví dụ, ở đây bạn sẽ tìm thấy khóa công khai mở rộng và *mô tả* của nó, hữu ích nếu bạn dự định thiết lập wallet ở chế độ chỉ xem từ wallet này.


![GREEN 2FA MULTISIG](assets/fr/36.webp)


Bạn cũng có thể thay đổi mã PIN của wallet và kích hoạt kết nối sinh trắc học.


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## Sử dụng Blockstream Green


Giờ đây, Bitcoin và wallet của bạn đã được thiết lập xong, bạn đã sẵn sàng nhận sats đầu tiên! Chỉ cần nhấp vào nút "*Nhận*".


![GREEN 2FA MULTISIG](assets/fr/38.webp)


Green sẽ hiển thị địa chỉ nhận trống đầu tiên trên wallet của bạn. Bạn có thể quét mã QR tương ứng hoặc sao chép trực tiếp địa chỉ để gửi bitcoin. Loại địa chỉ này không chỉ định số tiền người gửi cần gửi. Tuy nhiên, bạn có thể tạo địa chỉ yêu cầu một số tiền cụ thể bằng cách nhấp vào ba dấu chấm nhỏ ở góc trên bên phải, sau đó nhấp vào "*Số tiền yêu cầu*" và nhập số tiền mong muốn.


![GREEN 2FA MULTISIG](assets/fr/39.webp)


Khi giao dịch được phát sóng trên mạng, nó sẽ xuất hiện trong wallet của bạn.


![GREEN 2FA MULTISIG](assets/fr/40.webp)


Hãy đợi cho đến khi bạn nhận được đủ xác nhận để coi giao dịch là hoàn tất.


![GREEN 2FA MULTISIG](assets/fr/41.webp)


Với Bitcoin trong wallet, giờ đây bạn cũng có thể gửi Bitcoin. Nhấp vào "*Gửi*".


![GREEN 2FA MULTISIG](assets/fr/42.webp)


Ở trang tiếp theo, hãy nhập địa chỉ người nhận. Bạn có thể nhập thủ công hoặc quét mã QR.


![GREEN 2FA MULTISIG](assets/fr/43.webp)


Chọn số tiền thanh toán.


![GREEN 2FA MULTISIG](assets/fr/44.webp)


Ở cuối màn hình, bạn có thể chọn mức phí cho giao dịch này. Bạn có thể chọn theo khuyến nghị của ứng dụng hoặc tùy chỉnh mức phí của mình. Mức phí càng cao so với các giao dịch đang chờ xử lý khác, giao dịch của bạn sẽ được xử lý càng nhanh. Để biết thông tin về thị trường phí, vui lòng truy cập [Mempool.space](https://mempool.space/) trong mục "*Phí giao dịch*".


![GREEN 2FA MULTISIG](assets/fr/45.webp)


Nhấp vào "*Tiếp theo*" để truy cập màn hình tóm tắt giao dịch. Kiểm tra xem địa chỉ, số tiền và phí có chính xác không.


![GREEN 2FA MULTISIG](assets/fr/46.webp)


Nếu mọi việc diễn ra suôn sẻ, hãy trượt nút màu xanh lá cây ở cuối màn hình sang bên phải để ký và phát sóng giao dịch trên mạng Bitcoin.


![GREEN 2FA MULTISIG](assets/fr/47.webp)


Đây là lúc bạn cần nhập mã xác thực để mở khóa thiết bị multisig thứ hai do Blockstream giữ. Nhập mã 6 chữ số hiển thị trên ứng dụng xác thực của bạn.


![GREEN 2FA MULTISIG](assets/fr/48.webp)


Giao dịch của bạn hiện sẽ hiển thị trên bảng điều khiển Bitcoin wallet, chờ xác nhận.


![GREEN 2FA MULTISIG](assets/fr/49.webp)


Vậy là giờ bạn đã biết cách dễ dàng thiết lập cấu hình 2/2 multisig wallet bằng tùy chọn xác thực hai yếu tố (2FA) của Blockstream Green rồi!


Nếu bạn thấy hướng dẫn này hữu ích, tôi rất biết ơn nếu bạn để lại một biểu tượng ngón tay cái màu xanh lá cây bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn rất nhiều!


Tôi cũng khuyên bạn nên xem hướng dẫn chi tiết khác về ứng dụng di động Blockstream Green để thiết lập Liquid wallet:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a