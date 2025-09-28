---
name: Trezor Model One
description: Thiết lập và sử dụng Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Tín dụng hình ảnh: [Trezo.io](https://trezor.io/)*



Trezor Model One là Hardware Wallet đầu tiên từng được phát hành, ra mắt vào năm 2014 bởi SatoshiLabs. Sau hơn mười năm tồn tại, nó vẫn là một lựa chọn thú vị, đặc biệt là đối với những người dùng đang tìm kiếm một Hardware Wallet có thể tiếp cận được cả về mặt kỹ thuật và ngân sách. Trên thực tế, nó có giá 49 € trên trang web chính thức của Trezor. Đây là một trong số ít ví phần cứng trong tầm giá này. Nó nằm giữa các thiết bị cấp thấp với giá khoảng 20 €, chẳng hạn như Tapsigner, thường không có màn hình, và các thiết bị tầm trung với giá khoảng 80 €, chẳng hạn như Ledger Nano S Plus hoặc Trezor Safe 3.



Model One có màn hình OLED đơn sắc 0,96 inch và hai nút bấm vật lý. Nó hoạt động mà không cần pin, chỉ sử dụng kết nối micro-USB để cấp nguồn và dữ liệu Exchange.



![Image](assets/fr/01.webp)



Nhược điểm chính của Model One là thiếu Secure Element, khiến nó dễ bị tấn công vật lý, một số trong đó tương đối dễ thực hiện. Các cuộc tấn công này có thể bao gồm phân tích các kênh phụ trợ để xác định mã PIN của thiết bị hoặc các kỹ thuật tiên tiến hơn để trích xuất seed đã mã hóa nhằm tấn công bằng cách dùng vũ lực sau này. Lưu ý rằng các cuộc tấn công này yêu cầu phải truy cập vật lý vào thiết bị. Tuy nhiên, lỗ hổng này có thể được giảm đáng kể bằng cách sử dụng passphrase BIP39 chắc chắn. Nếu bạn chọn Hardware Wallet này, tôi thực sự khuyên bạn nên định cấu hình passphrase.



Model One mang lại hai lợi thế quan trọng:




- Nó dựa trên kiến trúc mã nguồn mở hoàn toàn. Không giống như các mô hình gần đây hơn với Secure Element, tất cả các thành phần phần cứng và phần mềm của Model One đều có thể kiểm tra được;
- Nó được trang bị màn hình. Theo tôi biết, đây là Hardware Wallet duy nhất trên thị trường trong tầm giá này có màn hình. Đây là một tính năng rất quan trọng, vì nó cho phép xác minh thông tin đã ký và địa chỉ tiếp nhận, do đó ngăn chặn nhiều cuộc tấn công kỹ thuật số.



Do đó, Trezor Model One có thể là lựa chọn sáng suốt cho người mới bắt đầu và người dùng trung cấp có ngân sách hạn chế. Tuy nhiên, điều quan trọng là phải lưu ý đến những hạn chế về khả năng bảo vệ vật lý của nó, do không có Secure Element. Nếu ngân sách của bạn hạn hẹp, đây là một lựa chọn tốt, nhưng nếu bạn có đủ khả năng để lựa chọn một mẫu cao cấp hơn, chẳng hạn như Trezor Safe 3 với giá 79 €, thì đây là lựa chọn tốt hơn, vì nó bao gồm Secure Element.



## Mở hộp Trezor Model One



Khi bạn nhận được Model One, hãy đảm bảo hộp và Seal còn nguyên vẹn để xác nhận rằng gói hàng chưa được mở. Xác minh phần mềm về tính xác thực và tính toàn vẹn của thiết bị cũng sẽ được thực hiện khi thiết lập sau đó.



Nội dung hộp bao gồm:




- Trezor Model One;
- Giấy bìa cứng để ghi cụm từ Mnemonic, nhãn dán và hướng dẫn;
- Cáp USB-A sang micro-USB.



![Image](assets/fr/02.webp)



Việc điều hướng thiết bị rất đơn giản:




- Nhấp chuột phải để xác nhận và tiến hành các bước tiếp theo;
- Sử dụng nút bên trái để quay lại.



## Điều kiện tiên quyết



Trong hướng dẫn này, tôi sẽ chỉ cho bạn cách sử dụng Trezor Model One với [phần mềm quản lý danh mục đầu tư Sparrow Wallet](https://sparrowwallet.com/download/). Nếu bạn chưa cài đặt phần mềm này, vui lòng cài đặt ngay. Nếu bạn cần trợ giúp, chúng tôi cũng có hướng dẫn chi tiết về cách cấu hình Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Bạn cũng sẽ cần phần mềm Trezor Suite để cấu hình Model One, kiểm tra tính xác thực của nó và cài đặt chương trình cơ sở. Chúng tôi sẽ chỉ sử dụng phần mềm này cho mục đích đó, và sau đó chỉ cần dùng để cập nhật chương trình cơ sở. Đối với việc quản lý hàng ngày của Wallet, chúng tôi sẽ sử dụng Sparrow Wallet độc quyền, vì nó được tối ưu hóa cho Bitcoin và dễ sử dụng, ngay cả đối với người mới bắt đầu (Sparrow chỉ hỗ trợ Bitcoin, không hỗ trợ altcoin).



[Tải xuống Trezor Suite từ trang web chính thức](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Đối với cả hai chương trình này, tôi thực sự khuyên bạn nên kiểm tra cả tính xác thực (với GnuPG) và tính toàn vẹn (thông qua Hash) trước khi cài đặt chúng trên máy của bạn. Nếu bạn không biết cách thực hiện, bạn có thể làm theo hướng dẫn khác này:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Bắt đầu Trezor Model One



Kết nối Model One với máy tính đã cài đặt Trezor Suite và Sparrow Wallet.



![Image](assets/fr/04.webp)



Mở Trezor Suite, sau đó nhấp vào "*Thiết lập Trezor của tôi*".



![Image](assets/fr/05.webp)



Chọn "*Phần mềm chỉ dành cho Bitcoin*", sau đó nhấp vào "*Cài đặt chỉ dành cho Bitcoin*".



![Image](assets/fr/06.webp)



Trezor Suite sau đó sẽ cài đặt chương trình cơ sở trên Model One của bạn. Vui lòng đợi trong khi cài đặt.



![Image](assets/fr/07.webp)



Nhấp vào "*Tiếp tục*".



![Image](assets/fr/08.webp)



## Tạo danh mục đầu tư Bitcoin



Trên Trezor Suite, nhấp vào nút "*Tạo Wallet mới*".



![Image](assets/fr/09.webp)



Chấp nhận các điều khoản sử dụng trên Hardware Wallet.



![Image](assets/fr/10.webp)



Trong Trezor Suite, nhấp vào "*Tiếp tục sao lưu*".



![Image](assets/fr/11.webp)



Phần mềm cung cấp hướng dẫn về cách quản lý cụm từ Mnemonic của bạn.



Mnemonic này cung cấp cho bạn quyền truy cập đầy đủ, không hạn chế vào tất cả bitcoin của bạn. Bất kỳ ai sở hữu cụm từ này đều có thể đánh cắp tiền của bạn, ngay cả khi không có quyền truy cập vật lý vào Trezor Model One của bạn.



Cụm từ 24 từ này khôi phục quyền truy cập vào bitcoin của bạn trong trường hợp Hardware Wallet của bạn bị mất, bị trộm hoặc bị hỏng. Do đó, điều rất quan trọng là phải lưu trữ cẩn thận và cất giữ ở nơi an toàn.



Bạn có thể viết lên tấm bìa cứng đi kèm trong hộp hoặc để an toàn hơn, tôi khuyên bạn nên khắc lên đế thép không gỉ để bảo vệ khỏi hỏa hoạn, lũ lụt hoặc sụp đổ.



Xác nhận hướng dẫn, sau đó nhấp vào nút "*Tạo bản sao lưu Wallet*".



![Image](assets/fr/12.webp)



Model One sẽ tạo cụm từ Mnemonic của bạn bằng trình tạo số ngẫu nhiên. Đảm bảo bạn không bị theo dõi trong quá trình này. Viết các từ được cung cấp trên màn hình vào phương tiện vật lý mà bạn chọn. Tùy thuộc vào chiến lược bảo mật của mình, bạn có thể cân nhắc tạo nhiều bản sao vật lý hoàn chỉnh của cụm từ (nhưng trên hết, đừng chia nó ra). Điều quan trọng là phải đánh số các từ và sắp xếp theo thứ tự.



**Rõ ràng là bạn không bao giờ được chia sẻ những từ này trên Internet, như tôi đã làm trong hướng dẫn này. Ví dụ Wallet này sẽ chỉ được sử dụng trên Testnet và sẽ bị xóa vào cuối hướng dẫn**



Để biết thêm thông tin về cách lưu và quản lý cụm từ Mnemonic của bạn, tôi thực sự khuyên bạn nên làm theo hướng dẫn khác này, đặc biệt nếu bạn là người mới bắt đầu:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Để chuyển sang các từ tiếp theo, hãy nhấp chuột phải. Sau khi bạn đã viết hết các từ, hãy nhấp vào nút bên phải một lần nữa để chuyển sang bước tiếp theo.



![Image](assets/fr/13.webp)



Hardware Wallet của bạn lại hiển thị tất cả các từ của bạn. Kiểm tra xem bạn đã viết hết chúng ra chưa.



![Image](assets/fr/14.webp)



## Thiết lập mã PIN



Tiếp theo là bước mã PIN. Mã PIN mở khóa Trezor của bạn. Do đó, nó cung cấp khả năng bảo vệ chống lại truy cập vật lý trái phép. Mã PIN này không liên quan đến việc tạo ra khóa mật mã Wallet của bạn. Vì vậy, ngay cả khi không có quyền truy cập vào mã PIN, việc sở hữu cụm từ Mnemonic gồm 12 từ của bạn sẽ cho phép bạn lấy lại quyền truy cập vào bitcoin của mình.



Trên Trezor Suite, nhấp vào "*Tiếp tục nhập mã PIN*", sau đó nhấp vào nút "*Đặt mã PIN*".



![Image](assets/fr/15.webp)



Xác nhận trên Model One.



![Image](assets/fr/16.webp)



Chúng tôi khuyên bạn nên chọn mã PIN càng ngẫu nhiên càng tốt. Hãy đảm bảo lưu mã này ở một vị trí riêng biệt với nơi lưu trữ Trezor của bạn (ví dụ: trong trình quản lý mật khẩu). Bạn có thể xác định mã PIN từ 8 đến 50 chữ số. Tôi khuyên bạn nên chọn mã PIN càng dài càng tốt để tăng cường bảo mật.



Mã PIN phải được nhập vào Trezor Suite trên máy tính của bạn bằng cách nhấp vào các dấu chấm tương ứng với các chữ số, theo cấu hình bàn phím hiển thị trên Trezor Model One.



Phương pháp nhập mã PIN cụ thể này được yêu cầu mỗi khi bạn mở khóa Trezor Model One, cho dù thông qua Trezor Suite hay Sparrow Wallet.



![Image](assets/fr/17.webp)



Khi hoàn tất, hãy nhấp vào nút "*Nhập mã PIN*".



![Image](assets/fr/18.webp)



Ghi lại mã PIN của bạn một lần nữa để xác nhận.



![Image](assets/fr/19.webp)



Trên Trezor Suite, nhấp vào nút "*Hoàn tất thiết lập*".



![Image](assets/fr/20.webp)



Cấu hình Model One của bạn hiện đã hoàn tất. Nếu muốn, bạn có thể thay đổi tên và trang chủ của Hardware Wallet.



![Image](assets/fr/21.webp)



Chúng ta sẽ không cần phần mềm Trezor Suite nữa, ngoại trừ việc thực hiện cập nhật chương trình cơ sở thường xuyên trên Hardware Wallet của bạn hoặc nếu bạn muốn chạy thử nghiệm phục hồi. Bây giờ chúng ta sẽ sử dụng Sparrow để quản lý danh mục đầu tư, vì phần mềm này hoàn toàn phù hợp để sử dụng chỉ trên Bitcoin.



## Thiết lập danh mục đầu tư trên Sparrow Wallet



Bắt đầu bằng cách tải xuống và cài đặt Sparrow Wallet [từ trang web chính thức](https://sparrowwallet.com/) trên máy tính của bạn, nếu bạn chưa thực hiện.



Sau khi bạn đã mở Sparrow Wallet, hãy đảm bảo rằng phần mềm được kết nối với một nút Bitcoin, được biểu thị bằng dấu tích ở góc dưới bên phải của Interface. Nếu bạn gặp sự cố khi kết nối Sparrow, tôi khuyên bạn nên tham khảo phần đầu của hướng dẫn này:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Nhấp vào tab "*File*", sau đó nhấp vào "*New Wallet*".



![Image](assets/fr/22.webp)



Đặt tên cho danh mục đầu tư của bạn, sau đó nhấp vào "*Tạo Wallet*".



![Image](assets/fr/23.webp)



Trong menu thả xuống "*Script Type*", hãy chọn loại script sẽ được sử dụng để bảo mật bitcoin của bạn. Tôi khuyên bạn nên dùng "*Taproot*", hoặc nếu không thì dùng "*Native SegWit*".



![Image](assets/fr/24.webp)



Nhấp vào nút "*Đã kết nối Hardware Wallet*". Tất nhiên Model One của bạn phải được kết nối với máy tính.



![Image](assets/fr/25.webp)



Nhấp vào nút "*Quét*". Model One của bạn sẽ xuất hiện.



Khi bạn kết nối Model One với máy tính có Sparrow Wallet đang mở, bạn sẽ được nhắc nhập passphrase BIP39 trên Sparrow. Tùy chọn nâng cao này sẽ được đề cập trong hướng dẫn sau. Hiện tại, bạn chỉ cần chọn "*Toggle passphrase Off*" để ngăn Trezor nhắc bạn nhập passphrase mỗi khi bạn khởi động.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Nhấp vào "*Nhập kho khóa*".



![Image](assets/fr/27.webp)



Bây giờ bạn có thể xem thông tin chi tiết về Wallet của mình, bao gồm khóa công khai mở rộng của tài khoản đầu tiên. Nhấp vào nút "*Áp dụng*" để hoàn tất việc tạo Wallet.



![Image](assets/fr/28.webp)



Chọn mật khẩu mạnh để bảo mật quyền truy cập vào Sparrow Wallet. Mật khẩu này sẽ đảm bảo quyền truy cập an toàn vào dữ liệu Sparrow Wallet của bạn, bảo vệ khóa công khai, địa chỉ, nhãn và lịch sử giao dịch của bạn khỏi bị truy cập trái phép.



Tôi khuyên bạn nên lưu mật khẩu này trong trình quản lý mật khẩu để không quên nó.



![Image](assets/fr/29.webp)



Và bây giờ danh mục đầu tư của bạn đã được nhập vào Sparrow Wallet!



![Image](assets/fr/30.webp)



Trước khi bạn nhận được bitcoin đầu tiên trong Wallet của mình, **Tôi thực sự khuyên bạn nên thực hiện một bài kiểm tra khôi phục rỗng**. Viết ra một số thông tin tham khảo, chẳng hạn như xpub của bạn, sau đó đặt lại Trezor Model One của bạn trong khi Wallet vẫn còn rỗng. Sau đó, hãy thử khôi phục Wallet của bạn trên Trezor bằng cách sử dụng bản sao lưu giấy của bạn. Kiểm tra xem xpub được tạo sau khi khôi phục có khớp với bản bạn đã viết ban đầu không. Nếu khớp, bạn có thể yên tâm rằng bản sao lưu giấy của bạn là đáng tin cậy.



Để tìm hiểu thêm về cách thực hiện thử nghiệm phục hồi, tôi khuyên bạn nên tham khảo hướng dẫn khác này:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Làm thế nào để nhận bitcoin bằng Trezor Model One?



Trên Sparrow, nhấp vào tab "*Nhận*".



![Image](assets/fr/31.webp)



Trước khi sử dụng Address do Sparrow Wallet đề xuất, hãy kiểm tra trên màn hình Trezor của bạn. Thực hành này cho phép bạn xác nhận rằng Address hiển thị trên Sparrow không phải là gian lận và Hardware Wallet thực sự giữ khóa riêng cần thiết để chi tiêu bitcoin được bảo mật bằng Address này. Điều này giúp bạn tránh được một số loại tấn công.



Để thực hiện kiểm tra này, hãy nhấp vào nút "*Hiển thị Address*".



![Image](assets/fr/32.webp)



Kiểm tra xem Address hiển thị trên Trezor của bạn có khớp với Wallet trên Sparrow không. Bạn cũng nên thực hiện kiểm tra này ngay trước khi gửi Address cho người gửi để chắc chắn về tính hợp lệ của nó. Bạn có thể nhấn nút bên phải để xác nhận.



![Image](assets/fr/33.webp)



Bạn cũng có thể thêm "*Nhãn*" để mô tả nguồn bitcoin sẽ được bảo mật bằng Address này. Đây là một thực hành tốt cho phép bạn quản lý UTXO của mình tốt hơn.



![Image](assets/fr/34.webp)



Sau đó, bạn có thể sử dụng Address này để nhận bitcoin.



![Image](assets/fr/35.webp)



## Làm thế nào để gửi bitcoin bằng Trezor Model One?



Bây giờ bạn đã nhận được Satss đầu tiên trong Wallet được bảo mật Model One của mình, bạn cũng có thể chi tiêu chúng! Kết nối Trezor của bạn với máy tính, khởi chạy Sparrow Wallet, sau đó chuyển đến tab "*Gửi*" để tạo giao dịch mới.



![Image](assets/fr/36.webp)



Nếu bạn muốn *Kiểm soát tiền*, tức là chọn cụ thể UTXO nào để sử dụng trong giao dịch, hãy chuyển đến tab "*UTXO*". Chọn UTXO bạn muốn sử dụng, sau đó nhấp vào "*Gửi mục đã chọn*". Bạn sẽ được chuyển hướng đến cùng một màn hình trong tab "*Gửi*", nhưng với UTXO đã được chọn cho giao dịch.



![Image](assets/fr/37.webp)



Nhập địa chỉ đích Address. Bạn cũng có thể nhập nhiều địa chỉ bằng cách nhấp vào nút "*+ Thêm*".



![Image](assets/fr/38.webp)



Viết "*Nhãn*" để ghi nhớ mục đích của khoản chi phí này.



![Image](assets/fr/39.webp)



Chọn số tiền sẽ gửi đến Address này.



![Image](assets/fr/40.webp)



Điều chỉnh mức phí giao dịch của bạn theo thị trường hiện tại. Ví dụ, bạn có thể sử dụng [Mempool.space](https://Mempool.space/) để chọn mức phí phù hợp.



Hãy đảm bảo rằng tất cả thông số giao dịch của bạn đều chính xác, sau đó nhấp vào "*Tạo giao dịch*".



![Image](assets/fr/41.webp)



Nếu mọi thứ đều làm bạn hài lòng, hãy nhấp vào "*Hoàn tất giao dịch để ký*".



![Image](assets/fr/42.webp)



Nhấp vào "*Ký*".



![Image](assets/fr/43.webp)



Nhấp vào "*Ký*" bên cạnh Trezor Model One của bạn.



![Image](assets/fr/44.webp)



Kiểm tra các thông số giao dịch trên màn hình Hardware Wallet của bạn, bao gồm Address của người nhận, số tiền đã gửi và phí. Sau khi giao dịch đã được xác minh trên Trezor, hãy nhấp chuột phải để ký.



![Image](assets/fr/45.webp)



Giao dịch của bạn hiện đã được ký. Kiểm tra lần cuối để đảm bảo mọi thứ đều ổn, sau đó nhấp vào "*Phát giao dịch*" để phát trên mạng Bitcoin.



![Image](assets/fr/46.webp)



Bạn có thể tìm thấy nó trong tab "*Giao dịch*" của Sparrow Wallet.



![Image](assets/fr/47.webp)



Xin chúc mừng, giờ bạn đã nắm được cách sử dụng Trezor Model One cơ bản với Sparrow Wallet! Để tiến xa hơn nữa, tôi khuyên bạn nên xem hướng dẫn toàn diện này về cách sử dụng Trezor Hardware Wallet với passphrase BIP39 để tăng cường sự an toàn của bạn:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn bạn rất nhiều!