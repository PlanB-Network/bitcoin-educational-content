---
name: Trezor an toàn 5
description: Cấu hình và sử dụng Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*Tín dụng hình ảnh: [Trezo.io](https://trezor.io/)*



Trezor Safe 5 là Hardware Wallet thế hệ mới nhất do SatoshiLabs thiết kế và ra mắt vào năm 2024. Nó được định vị là phiên bản cao cấp của Safe 3, tập trung vào tính công thái học và độ bền. Nó được hưởng lợi từ những tiến bộ về an toàn giống như người tiền nhiệm của nó, Safe 3, so với Model One và Model T.



Với mức giá 169 euro, Safe 5 được định vị trong phân khúc cao cấp Hardware Wallet, cạnh tranh với các mẫu thẻ như Coldcard, Ledger Nano X và Flex, Jade Plus, Passport và Bitbox.



Safe 5 được phân biệt bằng màn hình cảm ứng màu 1,54 inch, được bảo vệ bằng *Gorilla Glass 3*, có khả năng chống va đập và trầy xước. Nó cũng được trang bị động cơ xúc giác *Trezor Touch* phát ra những rung động nhỏ khi chạm vào. Giống như Safe 3, nó kết hợp một Secure Element và hoạt động thông qua kết nối USB-C, với việc bổ sung thêm một cổng Micro SD.



Sự khác biệt chính giữa Safe 3 và Safe 5 nằm ở chất lượng của thiết bị, ngoài các khía cạnh an toàn. Nó cải thiện đáng kể trải nghiệm của người dùng, với hoạt động mượt mà hơn và màn hình thoải mái hơn. Về mặt an toàn, chúng tương đương nhau.



![Image](assets/fr/01.webp)



Safe 5 có tất cả các tính năng cần thiết mà bạn mong đợi từ một Hardware Wallet tốt, bao gồm tích hợp tuyệt vời của passphrase BIP39. Tuy nhiên, nó vẫn chưa hỗ trợ Miniscript.



Mẫu này đặc biệt phù hợp với người dùng mới bắt đầu và trung cấp. Mặt khác, nó có thể không đáp ứng được tất cả các kỳ vọng của người dùng nâng cao đang tìm kiếm các tính năng cụ thể hơn có sẵn trên các thiết bị như Coldcard. Tuy nhiên, nếu bạn không cần các tùy chọn nâng cao này, Trezor Safe 5 có thể là một lựa chọn tuyệt vời.



## Mô hình an toàn Trezor Safe 5



Giống như Safe 3, Trezor Safe 5 được trang bị **Secure Element** được chứng nhận EAL6+, một bước tiến đáng kể so với các mẫu trước đó như Model One và Model T. Đây là chip OPTIGA Trust M V3, không lưu trữ trực tiếp seed mà hoạt động như một thành phần mật mã để bảo mật quyền truy cập vào nó. Secure Element giữ lại một bí mật mà chỉ có thể truy cập được sau khi người dùng nhập đúng mã PIN. Bí mật này sau đó được sử dụng để giải mã seed, được lưu trữ dưới dạng mã hóa trong bộ nhớ chính của thiết bị.



Hệ thống bảo mật lai này cung cấp khả năng bảo vệ vật lý được cải thiện, đặc biệt là chống lại các cuộc tấn công trích xuất hoặc phân tích xâm lấn, những vấn đề mà Model One dễ gặp phải, đặc biệt là trong quản lý mã PIN. Những lỗ hổng này hiện đã được khắc phục nhờ sử dụng Secure Element. Model này cũng duy trì kiến trúc phần mềm nguồn mở: mã quản lý việc tạo và sử dụng khóa riêng vẫn có thể truy cập và xác minh được hoàn toàn. Chip OPTIGA chỉ quản lý mã PIN, một thành phần bên ngoài quản lý khóa Bitcoin Wallet. Nó chỉ giới hạn ở việc phát hành một bí mật có thể được sử dụng để giải mã seed. Ngoài ra, chip OPTIGA Trust M V3 được hưởng lợi từ giấy phép tương đối miễn phí, cho phép SatoshiLabs tự do công bố các lỗ hổng tiềm ẩn (Không có NDA).



Theo tôi, mô hình bảo mật này là một trong những sự thỏa hiệp tốt nhất hiện có trên thị trường. Nó kết hợp những ưu điểm của Secure Element với quản lý phần mềm nguồn mở. Trước đây, người dùng phải lựa chọn giữa bảo mật vật lý nâng cao với chip và tính minh bạch với nguồn mở; với Trezor Safe, bạn có thể hưởng lợi từ cả hai.



Trong hướng dẫn này, bạn sẽ học cách cấu hình và sử dụng Trezor Safe 5 một cách an toàn.



## Mở hộp Trezor Safe 5



Khi bạn nhận được Safe 5, hãy đảm bảo hộp và Seal còn nguyên vẹn để xác nhận rằng gói hàng chưa được mở. Kiểm tra phần mềm về tính xác thực và toàn vẹn của thiết bị cũng sẽ được thực hiện khi thiết lập sau.



Nội dung hộp bao gồm:




- Trezor Safe 5;
- Một túi đựng bìa cứng để ghi lại cụm từ Mnemonic, nhãn dán và hướng dẫn của bạn;
- Cáp USB-C sang USB-C.



Khi mở, Trezor Safe 5 của bạn sẽ được bảo vệ bằng lớp nhựa bảo vệ và cổng USB-C sẽ được cố định bằng Seal ba chiều. Hãy đảm bảo rằng nó ở đó.



![Image](assets/fr/02.webp)



Điều hướng trên thiết bị khá trực quan:




- Chạm vào nửa dưới của màn hình để di chuyển về phía trước;
- Trượt xuống để quay lại;
- Nhấn và giữ màn hình để xác nhận thao tác.



## Điều kiện tiên quyết



Trong hướng dẫn này, tôi sẽ chỉ cho bạn cách sử dụng Trezor Safe 5 với [phần mềm quản lý danh mục đầu tư Sparrow Wallet](https://sparrowwallet.com/download/). Nếu bạn chưa cài đặt phần mềm này, vui lòng cài đặt ngay. Nếu bạn cần trợ giúp, chúng tôi cũng có hướng dẫn chi tiết về cách cấu hình Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Bạn cũng sẽ cần phần mềm Trezor Suite để cấu hình Safe 5, kiểm tra tính xác thực của nó và cài đặt chương trình cơ sở. Chúng tôi sẽ chỉ sử dụng phần mềm này cho mục đích đó, và sau đó chỉ cần dùng để cập nhật chương trình cơ sở. Đối với việc quản lý hàng ngày của Wallet, chúng tôi sẽ sử dụng Sparrow Wallet độc quyền, vì nó được tối ưu hóa cho Bitcoin và dễ sử dụng, ngay cả đối với người mới bắt đầu (Sparrow chỉ hỗ trợ Bitcoin, không hỗ trợ altcoin).



[Tải xuống Trezor Suite từ trang web chính thức](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Đối với cả hai chương trình này, tôi thực sự khuyên bạn nên kiểm tra cả tính xác thực (với GnuPG) và tính toàn vẹn (thông qua Hash) trước khi cài đặt chúng trên máy của bạn. Nếu bạn không biết cách thực hiện, bạn có thể làm theo hướng dẫn khác này:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Khởi động Trezor Safe 5



Kết nối Safe 5 với máy tính đã cài đặt Trezor Suite và Sparrow Wallet.



![Image](assets/fr/04.webp)



Mở Trezor Suite, sau đó nhấp vào "*Thiết lập Trezor của tôi*".



![Image](assets/fr/05.webp)



Chọn "*Phần mềm chỉ dành cho Bitcoin*", sau đó nhấp vào "*Cài đặt chỉ dành cho Bitcoin*".



![Image](assets/fr/06.webp)



Sau đó, Trezor Suite sẽ cài đặt chương trình cơ sở trên Safe 5 của bạn. Vui lòng đợi trong khi cài đặt.



![Image](assets/fr/07.webp)



Nhấp vào "*Tiếp tục*".



![Image](assets/fr/08.webp)



Sau đó tiến hành kiểm tra tính xác thực để đảm bảo Hardware Wallet của bạn không phải là hàng giả hoặc bị xâm phạm.



![Image](assets/fr/09.webp)



Trên Safe 5, hãy nhấn vào màn hình để xác nhận.



![Image](assets/fr/10.webp)



Nếu Trezor của bạn là chính hãng, một thông báo xác nhận sẽ xuất hiện trong Trezor Suite.



![Image](assets/fr/11.webp)



Sau đó, bạn có thể bỏ qua phần cửa sổ có hướng dẫn vận hành cơ bản.



![Image](assets/fr/12.webp)



## Tạo danh mục đầu tư Bitcoin



Trên Trezor Suite, nhấp vào nút "*Tạo Wallet mới*".



![Image](assets/fr/13.webp)



Để tạo một BIP39 Wallet chuẩn, hãy bắt đầu bằng cách chọn "*Loại sao lưu Legacy Wallet*" từ menu thả xuống, sau đó chọn giữa cụm từ Mnemonic gồm 12 hoặc 24 từ (hiện tại khuyến nghị là 12 từ). Điều này sẽ cho phép bạn tạo một danh mục đầu tư đơn chữ ký cổ điển. Tôi khuyên bạn nên chọn các tham số tuân thủ BIP39 tại đây, để dễ dàng truy xuất và tránh bị giới hạn trong một môi trường cụ thể. Để hoàn tất, hãy nhấp vào "*Tạo Wallet*".



Nếu bạn muốn tìm hiểu thêm về các tùy chọn sao lưu khác có trên Trezor, bao gồm *Sao lưu nhiều lần chia sẻ*, tôi khuyên bạn nên tham khảo hướng dẫn này:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Chấp nhận các điều khoản sử dụng trên Hardware Wallet.



![Image](assets/fr/15.webp)



Nhấn và giữ màn hình để tạo danh mục đầu tư mới.



![Image](assets/fr/16.webp)



Trong Trezor Suite, nhấp vào "*Tiếp tục sao lưu*".



![Image](assets/fr/17.webp)



Phần mềm cung cấp hướng dẫn về cách quản lý cụm từ Mnemonic của bạn.



Mnemonic này cung cấp cho bạn quyền truy cập đầy đủ, không hạn chế vào tất cả bitcoin của bạn. Bất kỳ ai sở hữu cụm từ này đều có thể đánh cắp tiền của bạn, ngay cả khi không có quyền truy cập vật lý vào Trezor Safe 5 của bạn.



Cụm từ 12 từ này khôi phục quyền truy cập vào bitcoin của bạn trong trường hợp Hardware Wallet của bạn bị mất, bị trộm hoặc bị hỏng. Do đó, điều rất quan trọng là phải lưu giữ cẩn thận và cất giữ ở nơi an toàn.



Bạn có thể viết lên tấm bìa cứng đi kèm trong hộp hoặc để an toàn hơn, tôi khuyên bạn nên khắc lên đế thép không gỉ để bảo vệ khỏi hỏa hoạn, lũ lụt hoặc sập đổ.



Xác nhận hướng dẫn, sau đó nhấp vào nút "*Tạo bản sao lưu Wallet*".



![Image](assets/fr/18.webp)



Safe 5 sẽ tạo cụm từ Mnemonic của bạn bằng trình tạo số ngẫu nhiên của nó. Đảm bảo bạn không bị theo dõi trong quá trình thực hiện thao tác này. Viết các từ được cung cấp trên màn hình vào phương tiện vật lý mà bạn chọn. Tùy thuộc vào chiến lược bảo mật của mình, bạn có thể cân nhắc tạo nhiều bản sao vật lý hoàn chỉnh của cụm từ (nhưng trên hết, đừng chia nó ra). Điều quan trọng là phải đánh số các từ và sắp xếp theo thứ tự.



***Rõ ràng là bạn không bao giờ được chia sẻ những từ này trên Internet, như tôi đã làm trong hướng dẫn này. Ví dụ Wallet này sẽ chỉ được sử dụng trên Testnet và sẽ bị xóa vào cuối hướng dẫn



Để biết thêm thông tin về cách lưu và quản lý cụm từ Mnemonic đúng cách, tôi thực sự khuyên bạn nên làm theo hướng dẫn khác này, đặc biệt nếu bạn là người mới bắt đầu:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Để chuyển sang các từ tiếp theo, hãy nhấp vào cuối màn hình. Bạn có thể quay lại bằng cách trượt xuống. Sau khi viết xong tất cả các từ, hãy giữ ngón tay trên màn hình để chuyển sang bước tiếp theo.



![Image](assets/fr/20.webp)



Chọn các từ trong cụm từ Mnemonic của bạn theo thứ tự của chúng để xác nhận rằng bạn đã viết chúng chính xác.



![Image](assets/fr/21.webp)



Sau khi quá trình xác minh này hoàn tất, hãy nhấp vào màn hình để tiếp tục.



![Image](assets/fr/22.webp)



## Thiết lập mã PIN



Tiếp theo là bước mã PIN. Mã PIN mở khóa Trezor của bạn. Do đó, nó cung cấp khả năng bảo vệ chống lại truy cập vật lý trái phép. Mã PIN này không liên quan đến việc tạo ra khóa mật mã Wallet của bạn. Vì vậy, ngay cả khi không có quyền truy cập vào mã PIN, việc sở hữu cụm từ Mnemonic gồm 12 từ của bạn sẽ cho phép bạn lấy lại quyền truy cập vào bitcoin của mình.



Trên Trezor Suite, nhấp vào "*Tiếp tục nhập mã PIN*", sau đó nhấp vào nút "*Đặt mã PIN*".



![Image](assets/fr/23.webp)



Xác nhận bằng Safe 5.



![Image](assets/fr/24.webp)



Chúng tôi khuyên bạn nên chọn mã PIN càng ngẫu nhiên càng tốt. Hãy đảm bảo lưu mã này ở một vị trí riêng biệt với nơi lưu trữ Trezor của bạn (ví dụ: trong trình quản lý mật khẩu). Bạn có thể xác định mã PIN từ 8 đến 50 chữ số. Tôi khuyên bạn nên chọn mã PIN càng dài càng tốt để tăng cường bảo mật.



Sử dụng bàn di chuột để nhập mã PIN.



![Image](assets/fr/25.webp)



Khi hoàn tất, hãy nhấp vào dấu tích Green ở góc dưới bên phải, sau đó xác nhận mã PIN lần thứ hai.



![Image](assets/fr/26.webp)



Mã PIN của bạn đã được đăng ký.



![Image](assets/fr/27.webp)



Trên Trezor Suite, nhấp vào nút "*Hoàn tất thiết lập*".



![Image](assets/fr/28.webp)



Cấu hình Safe 5 của bạn hiện đã hoàn tất. Nếu muốn, bạn có thể thay đổi tên và trang chủ của Hardware Wallet.



![Image](assets/fr/29.webp)



Chúng ta sẽ không cần phần mềm Trezor Suite nữa, ngoại trừ việc thực hiện cập nhật chương trình cơ sở thường xuyên trên Hardware Wallet của bạn hoặc nếu bạn muốn chạy thử nghiệm phục hồi. Bây giờ chúng ta sẽ sử dụng Sparrow để quản lý danh mục đầu tư, vì phần mềm này hoàn toàn phù hợp để sử dụng riêng cho Bitcoin.



## Thiết lập danh mục đầu tư trên Sparrow Wallet



Bắt đầu bằng cách tải xuống và cài đặt Sparrow Wallet [từ trang web chính thức](https://sparrowwallet.com/) trên máy tính của bạn, nếu bạn chưa thực hiện.



Sau khi bạn đã mở Sparrow Wallet, hãy đảm bảo rằng phần mềm được kết nối với một nút Bitcoin, được biểu thị bằng dấu tích ở góc dưới bên phải của Interface. Nếu bạn gặp sự cố khi kết nối Sparrow, tôi khuyên bạn nên tham khảo phần đầu của hướng dẫn này:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Nhấp vào tab "*File*", sau đó nhấp vào "*New Wallet*".



![Image](assets/fr/30.webp)



Đặt tên cho danh mục đầu tư của bạn, sau đó nhấp vào "*Tạo Wallet*".



![Image](assets/fr/31.webp)



Trong menu thả xuống "*Script Type*", hãy chọn loại script sẽ được sử dụng để bảo mật bitcoin của bạn. Tôi khuyên bạn nên dùng "*Taproot*", hoặc nếu không thì dùng "*Native SegWit*".



![Image](assets/fr/32.webp)



Nhấp vào nút "*Connected Hardware Wallet*". Tất nhiên Safe 5 của bạn phải được kết nối với máy tính và mở khóa.



Khi bạn kết nối Safe 5 của mình với máy tính có Sparrow Wallet đang mở, bạn sẽ được nhắc nhập passphrase BIP39 trên màn hình Hardware Wallet. Tùy chọn nâng cao này sẽ được đề cập trong hướng dẫn sau. Hiện tại, bạn chỉ cần nhấp vào dấu tích Green ở góc trên bên phải để xác nhận rằng bạn muốn sử dụng passphrase trống (tức là không có passphrase). Để ngăn Trezor của bạn yêu cầu bạn nhập passphrase mỗi khi bạn khởi động, hãy vào Trezor Suite, truy cập cài đặt và thay đổi tùy chọn trong "*Thiết bị*" > "*Wallet mặc định*" thành "*Chuẩn*" thay vì "*passphrase*".



![Image](assets/fr/33.webp)



Nhấp vào nút "*Quét*". Safe 5 của bạn sẽ xuất hiện. Nhấp vào "*Nhập kho khóa*".



![Image](assets/fr/34.webp)



Bây giờ bạn có thể xem thông tin chi tiết về Wallet của mình, bao gồm khóa công khai mở rộng của tài khoản đầu tiên. Nhấp vào nút "*Áp dụng*" để hoàn tất việc tạo Wallet.



![Image](assets/fr/35.webp)



Chọn mật khẩu mạnh để bảo mật quyền truy cập vào Sparrow Wallet. Mật khẩu này sẽ đảm bảo quyền truy cập an toàn vào dữ liệu Sparrow Wallet của bạn, bảo vệ khóa công khai, địa chỉ, nhãn và lịch sử giao dịch của bạn khỏi bị truy cập trái phép.



Tôi khuyên bạn nên lưu mật khẩu này trong trình quản lý mật khẩu để không quên nó.



![Image](assets/fr/36.webp)



Và bây giờ danh mục đầu tư của bạn đã được nhập vào Sparrow Wallet!



![Image](assets/fr/37.webp)



Trước khi bạn nhận được bitcoin đầu tiên trong Wallet của mình, **Tôi thực sự khuyên bạn nên thực hiện một bài kiểm tra khôi phục rỗng**. Viết ra một số thông tin tham khảo, chẳng hạn như xpub của bạn, sau đó đặt lại Trezor Safe 5 của bạn trong khi Wallet vẫn còn rỗng. Sau đó, hãy thử khôi phục Wallet của bạn trên Trezor bằng cách sử dụng bản sao lưu giấy của bạn. Kiểm tra xem xpub được tạo sau khi khôi phục có khớp với bản bạn đã viết ban đầu không. Nếu khớp, bạn có thể yên tâm rằng bản sao lưu giấy của bạn là đáng tin cậy.



Để tìm hiểu thêm về cách thực hiện thử nghiệm phục hồi, tôi khuyên bạn nên tham khảo hướng dẫn khác này:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Tôi có thể nhận bitcoin bằng Trezor Safe 5 như thế nào?



Trên Sparrow, nhấp vào tab "*Nhận*".



![Image](assets/fr/38.webp)



Trước khi sử dụng Address do Sparrow Wallet đề xuất, hãy kiểm tra trên màn hình Trezor của bạn. Thực hành này cho phép bạn xác nhận rằng Address hiển thị trên Sparrow không phải là gian lận và Hardware Wallet thực sự giữ khóa riêng cần thiết để chi tiêu bitcoin được bảo mật bằng Address này sau đó. Điều này giúp bạn tránh được một số loại tấn công.



Để thực hiện kiểm tra này, hãy nhấp vào nút "*Hiển thị Address*".



![Image](assets/fr/39.webp)



Kiểm tra xem Address hiển thị trên Trezor của bạn có khớp với Wallet trên Sparrow không. Bạn cũng nên thực hiện kiểm tra này ngay trước khi giao Address cho người gửi để chắc chắn về tính hợp lệ của nó. Bạn có thể nhấn vào màn hình để xác nhận.



![Image](assets/fr/40.webp)



Sau đó, bạn có thể thêm "*Nhãn*" để mô tả nguồn bitcoin sẽ được bảo mật bằng Address này. Đây là một thực hành tốt cho phép bạn quản lý UTXO của mình tốt hơn.



![Image](assets/fr/41.webp)



Sau đó, bạn có thể sử dụng Address này để nhận bitcoin.



![Image](assets/fr/42.webp)



## Làm thế nào để gửi bitcoin bằng Trezor Safe 5?



Bây giờ bạn đã nhận được Satss đầu tiên trên Safe 5-secured Wallet của mình, bạn cũng có thể chi tiêu chúng! Kết nối Trezor của bạn với máy tính, mở khóa bằng mã PIN, khởi chạy Sparrow Wallet, sau đó chuyển đến tab "*Gửi*" để tạo giao dịch mới.



![Image](assets/fr/43.webp)



Nếu bạn muốn *Kiểm soát tiền*, tức là chọn cụ thể UTXO nào để sử dụng trong giao dịch, hãy chuyển đến tab "*UTXO*". Chọn UTXO bạn muốn chi tiêu, sau đó nhấp vào "*Gửi mục đã chọn*". Bạn sẽ được chuyển hướng đến cùng một màn hình trong tab "*Gửi*", nhưng với UTXO của bạn đã được chọn cho giao dịch.



![Image](assets/fr/44.webp)



Nhập địa chỉ đích Address. Bạn cũng có thể nhập nhiều địa chỉ bằng cách nhấp vào nút "*+ Thêm*".



![Image](assets/fr/45.webp)



Viết "*Nhãn*" để ghi nhớ mục đích của khoản chi phí này.



![Image](assets/fr/46.webp)



Chọn số tiền sẽ gửi đến Address này.



![Image](assets/fr/47.webp)



Điều chỉnh mức phí giao dịch của bạn theo thị trường hiện tại. Ví dụ, bạn có thể sử dụng [Mempool.space](https://Mempool.space/) để chọn mức phí phù hợp.



Hãy đảm bảo rằng tất cả thông số giao dịch của bạn đều chính xác, sau đó nhấp vào "*Tạo giao dịch*".



![Image](assets/fr/48.webp)



Nếu mọi thứ đều làm bạn hài lòng, hãy nhấp vào "*Hoàn tất giao dịch để ký*".



![Image](assets/fr/49.webp)



Nhấp vào "*Ký*".



![Image](assets/fr/50.webp)



Nhấp vào "*Ký*" bên cạnh Trezor Safe 5 của bạn.



![Image](assets/fr/51.webp)



Kiểm tra các thông số giao dịch trên màn hình Hardware Wallet của bạn, bao gồm Address của người nhận, số tiền đã gửi và khoản phí. Sau khi giao dịch đã được xác minh trên Trezor, hãy nhấn và giữ màn hình để ký.



![Image](assets/fr/52.webp)



Giao dịch của bạn hiện đã được ký. Kiểm tra lần cuối để đảm bảo mọi thứ đều ổn, sau đó nhấp vào "*Phát giao dịch*" để phát trên mạng Bitcoin.



![Image](assets/fr/53.webp)



Bạn có thể tìm thấy nó trong tab "*Giao dịch*" của Sparrow Wallet.



![Image](assets/fr/54.webp)



Xin chúc mừng, giờ bạn đã nắm được cách sử dụng Trezor Safe 5 cơ bản với Sparrow Wallet! Để tiến xa hơn nữa, tôi khuyên bạn nên xem hướng dẫn toàn diện này về cách sử dụng Trezor Hardware Wallet với passphrase BIP39 để tăng cường sự an toàn của bạn:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn bạn rất nhiều!