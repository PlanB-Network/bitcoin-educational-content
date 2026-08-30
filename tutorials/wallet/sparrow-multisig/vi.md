---
name: Sparrow Wallet - Multisig
description: Tạo ví đa chữ ký trên Sparrow
---
![bìa](assets/cover.webp)


Ví đa chữ ký (thường được gọi là "*Multisig*") là một cấu trúc ví Bitcoin yêu cầu nhiều chữ ký mật mã, từ các khóa khác nhau, để cho phép một khoản chi tiêu. Khác với ví thông thường ("*singlesig*"), trong đó một khóa bí mật duy nhất là đủ để mở khóa một UTXO, Multisig dựa trên mô hình **m-of-n**: trong số _n_ khóa gắn với ví, _m_ khóa bắt buộc phải cùng ký mỗi giao dịch.


Cơ chế này cho phép nhiều thực thể hoặc thiết bị cùng chia sẻ quyền kiểm soát một ví. Ví dụ, trong cấu hình 2-trong-3, ba bộ khóa độc lập được tạo, nhưng chỉ cần hai bộ để giải phóng tiền. Kiến trúc này giảm mạnh các rủi ro liên quan đến việc một khóa bị lộ hoặc bị mất: kẻ trộm chỉ có quyền truy cập vào một khóa không thể rút sạch ví, và người dùng làm mất một khóa vẫn có thể truy cập tiền của mình bằng hai khóa còn lại.


![Hình ảnh](assets/fr/01.webp)


Tuy nhiên, mức bảo mật cao hơn này đi kèm với độ phức tạp cao hơn. Việc thiết lập ví Multisig yêu cầu bảo mật nhiều cụm từ khôi phục (một cụm từ cho mỗi yếu tố chữ ký) và các khóa công khai mở rộng ("*xpub*"). Thật vậy, nếu bạn sử dụng ví Multisig 2-trong-3, để khôi phục ví, bạn phải có cả ba cụm từ khôi phục, hoặc ít nhất hai trong ba cụm từ. Nhưng nếu bạn chỉ có hai trong ba cụm từ, bạn cũng cần truy cập vào ba *xpub*; nếu không, bạn sẽ không thể khôi phục các khóa công khai cần thiết để truy cập số bitcoin mà chúng bảo vệ.


Tóm lại, để khôi phục ví Multisig, bạn phải:


- Hoặc truy cập tất cả các cụm từ khôi phục gắn với từng yếu tố chữ ký;
- Hoặc có số cụm từ khôi phục tối thiểu mà ngưỡng yêu cầu để có thể ký, đồng thời cũng có quyền truy cập vào xpub của tất cả các yếu tố để khôi phục các khóa công khai cần thiết.


![Hình ảnh](assets/fr/02.webp)


Việc quản lý các bản sao lưu ví Multisig được hỗ trợ bởi *Bộ mô tả kịch bản đầu ra*, vốn gom nhóm tất cả dữ liệu công khai cần thiết để truy cập tiền. Tuy nhiên, chức năng này chưa được triển khai trong tất cả phần mềm quản lý ví.


Multisig đặc biệt phù hợp với những bitcoiner muốn có bảo mật tăng cường hoặc quản lý tiền tập thể: công ty, hiệp hội, gia đình, hoặc người dùng cá nhân nắm giữ một lượng bitcoin đáng kể. Nó có thể được dùng để tạo các mô hình quản trị phi tập trung, ví dụ như phân bổ thẩm quyền ký giữa nhiều quản lý hoặc thành viên trong nhóm.


Trong hướng dẫn này, chúng ta sẽ học cách tạo và sử dụng một ví đa chữ ký cổ điển với **Sparrow Wallet**. Nếu bạn muốn tạo một ví đa chữ ký tùy chỉnh với timelock, tôi khuyên bạn nên dùng Liana thay thế:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Điều kiện tiên quyết


Trong hướng dẫn này, tôi sẽ chỉ cho bạn cách tạo Multisig bằng [phần mềm quản lý ví Sparrow Wallet](https://sparrowwallet.com/download/). Nếu bạn chưa cài đặt phần mềm này, hãy cài đặt ngay. Nếu cần trợ giúp, chúng tôi cũng có một hướng dẫn chi tiết về cách cấu hình Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Để thiết lập ví đa chữ ký, bạn sẽ cần các ví phần cứng khác nhau. Ví dụ, với Multisig 2-trong-3, bạn có thể dùng:


- Trezor Model One;
- Ledger Flex;
- Passport Core.


![Hình ảnh](assets/fr/03.webp)


Bạn nên sử dụng ví phần cứng từ các hãng khác nhau trong cấu hình Multisig của mình. Điều này bảo đảm rằng nếu một mẫu cụ thể gặp vấn đề nghiêm trọng, nó sẽ không ảnh hưởng đến mức an toàn tổng thể của Multisig. Hơn nữa, cách này cho phép bạn hưởng lợi từ các ưu điểm riêng của từng thiết bị. Ví dụ, trong cấu hình của tôi:



- Trezor Model One hoàn toàn mã nguồn mở, giúp có thể xác minh quá trình tạo seed. Tuy nhiên, vì không được trang bị Secure Element, nó vẫn dễ bị tấn công vật lý;



- Ledger Flex, ngược lại, hưởng lợi từ firmware độc quyền không thể xác minh, nhưng tích hợp Secure Element cung cấp khả năng bảo vệ vật lý xuất sắc;



- Passport Core kết hợp firmware hoàn toàn mã nguồn mở, Secure Element, và trao đổi mã QR air-gapped. Đây là bên ký thứ ba độc lập, có thể xác minh địa chỉ và ký PSBT mà không cần kết nối dữ liệu USB.


Trước khi cấu hình ví Multisig, hãy bảo đảm rằng mỗi ví phần cứng đã được cấu hình đúng cách (tạo và lưu cụm từ khôi phục, đặt PIN). Để xem hướng dẫn chi tiết, bạn có thể tham khảo các hướng dẫn của chúng tôi cho từng ví phần cứng, ví dụ:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Như chúng ta sẽ thấy ở phần sau của hướng dẫn này, bạn cũng có thể tích hợp vào cấu hình Multisig của mình một yếu tố không gắn với ví phần cứng, nhưng có khóa bí mật được lưu trên PC của bạn. Phương pháp này rõ ràng kém an toàn hơn so với việc chỉ dùng ví phần cứng, nhưng có thể phù hợp trong một số trường hợp. Ví dụ, với Multisig 2-trong-3, bạn có thể chọn hai ví phần cứng và một ví phần mềm.

> ⚠️ **Thông báo bảo mật Coldcard MK3:** không tạo seed mới trên MK3 đang chạy firmware cũ hơn 4.2.0. Seed được tạo trên firmware cũ hơn phải được thay thế và tiền phải được chuyển đi. Vì vậy, hướng dẫn này dùng Passport Core làm thiết bị ký tham chiếu air-gapped.


## Tạo ví Multisig


Mở Sparrow Wallet, nhấp vào tab "*Tệp*", sau đó chọn "*Ví mới*".


![Hình ảnh](assets/fr/04.webp)


Gán tên cho ví đa chữ ký của bạn, sau đó nhấp vào "*Tạo ví*" để xác nhận.


![Hình ảnh](assets/fr/05.webp)


Trong menu thả xuống "*Loại chính sách*", chọn tùy chọn "*Đa chữ ký*".


![Hình ảnh](assets/fr/06.webp)


Ở góc trên bên phải, giờ đây bạn có thể xác định tổng số khóa trong Multisig của mình, cũng như số người đồng ký cần thiết để cho phép một khoản chi. Trong ví dụ của tôi, đây là mô hình 2-trong-3.


![Hình ảnh](assets/fr/07.webp)


Ở cuối cửa sổ, Sparrow Wallet hiển thị ba "*Kho khóa*". Mỗi mục đại diện cho một bộ khóa. Ở đây, tôi dùng ba ví phần cứng, nên mỗi "*Kho khóa*" tương ứng với một thiết bị. Bây giờ chúng ta sẽ cấu hình chúng.


Tôi bắt đầu với Passport Core. Trong tab "*Kho khóa 1*", tôi chọn tùy chọn "*Ví phần cứng air-gapped*".


![Hình ảnh](assets/fr/08.webp)


Trên Passport, mở tài khoản bạn muốn sử dụng, sau đó chọn "*Kết nối ví*" > "*Sparrow*" > "*Kết nối dưới dạng Multisig*". Passport hiển thị một mã QR động chứa thông tin khóa công khai của nó.

Trong Sparrow, chọn "*Quét...*" bên cạnh "*Passport*" và quét mã QR động đó bằng webcam của máy tính. Kiểm tra dấu vân tay khóa chính do Sparrow hiển thị với dấu vân tay hiển thị trên Passport, rồi nhập kho khóa.

xpub Passport của bạn hiện đã được nhập. Lặp lại quy trình phù hợp cho Ledger Flex và Trezor Model One.


Đối với Ledger Flex, tôi chọn "*Kho khóa 2*", sau đó nhấp vào "*Ví phần cứng đã kết nối*". Bảo đảm Ledger được kết nối với máy tính, đã mở khóa và ứng dụng Bitcoin đang mở.


![Hình ảnh](assets/fr/15.webp)


Sau đó nhấp vào nút "*Quét...*".


![Hình ảnh](assets/fr/16.webp)


Bên cạnh tên ví phần cứng của bạn, nhấp vào "*Nhập kho khóa*".


![Hình ảnh](assets/fr/17.webp)


Bên ký thứ hai hiện đã được đăng ký đúng cách trong Sparrow Wallet.


![Hình ảnh](assets/fr/18.webp)


Tôi lặp lại đúng quy trình đó với Trezor One để hoàn tất cấu hình Multisig.


![Hình ảnh](assets/fr/19.webp)


Trong cấu hình của tôi, chúng ta không đề cập đến trường hợp này, nhưng nếu bạn muốn đưa một chữ ký thông qua ví phần mềm trong Sparrow (ví nóng) vào Multisig của mình, chỉ cần nhấp vào nút "*Ví phần mềm mới hoặc đã nhập*".


Giờ đây, khi tất cả thiết bị ký của bạn đã được nhập vào Sparrow Wallet, bạn có thể hoàn tất việc tạo Multisig bằng cách nhấp vào "*Áp dụng*".


![Hình ảnh](assets/fr/20.webp)


Chọn một mật khẩu mạnh để bảo mật quyền truy cập vào ví Sparrow Wallet của bạn. Mật khẩu này bảo vệ khóa công khai, địa chỉ, nhãn và lịch sử giao dịch của bạn khỏi truy cập trái phép.


Hãy nhớ lưu mật khẩu này ở nơi an toàn, chẳng hạn như trình quản lý mật khẩu, để tránh làm mất nó.


![Hình ảnh](assets/fr/21.webp)


## Sao lưu ví Multisig


Bây giờ chúng ta sẽ lưu *Bộ mô tả kịch bản đầu ra* trên một phương tiện độc lập và giữ nhiều bản sao của nó.


*Bộ mô tả* chứa tất cả xpub trong ví Multisig của bạn, cũng như các đường dẫn dẫn xuất dùng để tạo khóa. Hãy nhớ những gì chúng ta đã thấy trong Phần 1: để khôi phục ví Multisig, bạn phải có **tất cả** các cụm từ khôi phục, hoặc chỉ số lượng tối thiểu cần thiết để đạt ngưỡng chữ ký. Tuy nhiên, trong trường hợp sau, bạn cũng bắt buộc phải có **các xpub** của những bên ký bị thiếu. *Bộ mô tả* chứa tất cả xpub của Multisig của bạn.


Nếu điều này chưa rõ, chỉ cần nhớ điều này: để khôi phục một Multisig, bạn cần số cụm từ khôi phục tối thiểu cho từng ví phần cứng đã dùng, tùy theo ngưỡng (trong trường hợp của tôi: 2 cụm từ), cũng như *Bộ mô tả*.


*Bộ mô tả* này không chứa khóa bí mật, chỉ chứa khóa công khai. Điều này có nghĩa là nó không cho quyền truy cập tiền. Vì vậy, nó không nghiêm trọng bằng cụm từ khôi phục, vốn cho quyền truy cập đầy đủ vào bitcoin của bạn. Rủi ro với *Bộ mô tả* chỉ liên quan đến tính bảo mật thông tin: nếu bị lộ, bên thứ ba có thể quan sát tất cả giao dịch của bạn, nhưng không thể chi tiêu tiền của bạn.


Tôi khuyên mạnh bạn tạo nhiều bản sao của *Bộ mô tả* này và giữ chúng cùng với từng thiết bị ký trong Multisig của bạn. Ví dụ, trong trường hợp của tôi, tôi in *Bộ mô tả* ra giấy và giữ một bản với Passport, một bản khác với Trezor, và một bản với Ledger. Tôi cũng lưu *Bộ mô tả* này dưới dạng tệp PDF trên ba USB, mỗi USB được cất cùng một ví phần cứng. Bằng cách này, tôi tối đa hóa khả năng không bao giờ làm mất *Bộ mô tả* này, và tôi chắc chắn có hai bản sao (một bản vật lý và một bản kỹ thuật số) với mỗi thiết bị.


Sau khi ví Multisig của bạn được tạo, Sparrow tự động cung cấp *Bộ mô tả* này. Nhấp vào nút "*Lưu PDF...*" để lưu nó vừa dưới dạng văn bản vừa dưới dạng mã QR.


![Hình ảnh](assets/fr/22.webp)


Sau đó, bạn có thể in PDF này và sao chép nó vào các USB của mình.


![Hình ảnh](assets/fr/23.webp)


Passport dùng cấu hình multisig do Sparrow nhập để hiển thị và xác minh thông tin khóa liên quan trong luồng ghép nối QR và ký. Hãy giữ *Bộ mô tả* một cách độc lập: nó vẫn thiết yếu để khôi phục ví nếu một bên ký không khả dụng.


Ngoài việc lưu *Bộ mô tả*, đừng quên đặc biệt chú ý đến việc lưu các cụm từ khôi phục cho từng thiết bị ký của bạn. Nếu bạn mới bắt đầu, tôi rất khuyến nghị bạn tham khảo hướng dẫn khác này để học cách lưu và quản lý chúng đúng cách:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Trước khi nhận những bitcoin đầu tiên trên Multisig của bạn, **tôi mạnh mẽ khuyên bạn thực hiện một bài kiểm tra khôi phục rỗng**. Ghi lại một số thông tin tham chiếu, chẳng hạn như địa chỉ nhận đầu tiên, rồi đặt lại các ví phần cứng trong khi ví vẫn còn trống. Tiếp theo, thử khôi phục ví Multisig của bạn trên các ví phần cứng bằng bản sao lưu giấy của cụm từ khôi phục, sau đó trên Sparrow bằng *Bộ mô tả*. Kiểm tra rằng địa chỉ đầu tiên được tạo sau khi khôi phục khớp với địa chỉ bạn đã ghi lại ban đầu. Nếu khớp, bạn có thể yên tâm rằng các bản sao lưu giấy của mình đáng tin cậy.


Để tìm hiểu thêm về cách thực hiện bài kiểm tra khôi phục, tôi gợi ý bạn tham khảo hướng dẫn khác này:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Nhận bitcoin trên Multisig của bạn


Ví của bạn hiện đã sẵn sàng nhận bitcoin. Trong Sparrow, nhấp vào tab "*Nhận*".


![Hình ảnh](assets/fr/30.webp)


Trước khi sử dụng địa chỉ do Sparrow Wallet tạo, hãy dành thời gian kiểm tra trực tiếp địa chỉ đó trên màn hình của các ví phần cứng. Điều này sẽ bảo đảm địa chỉ không bị sửa đổi, và các thiết bị của bạn nắm giữ khóa bí mật cần thiết để chi tiêu số tiền liên quan. Việc này giúp bảo vệ bạn trước một số vector tấn công.


Để làm việc này, nhấp vào "*Hiển thị địa chỉ*" để hiển thị địa chỉ trên Trezor hoặc Ledger của bạn, khi thiết bị được kết nối bằng cáp.


![Hình ảnh](assets/fr/31.webp)


Với Passport, chọn tài khoản multisig và chọn "*Xác minh địa chỉ*". Quét mã QR của địa chỉ nhận do Sparrow hiển thị. Passport xác nhận trên màn hình của nó liệu địa chỉ đó có thuộc ví multisig hay không.


Kiểm tra rằng địa chỉ hiển thị trên mỗi ví phần cứng khớp chính xác với địa chỉ trong Sparrow Wallet. Bạn nên làm việc này ngay trước khi chia sẻ địa chỉ với người trả tiền, để chắc chắn về tính toàn vẹn của nó.


Sau đó, bạn có thể gán một "*Nhãn*" cho địa chỉ này, để chỉ ra nguồn gốc của số bitcoin đã nhận. Đây là cách tốt để tổ chức việc quản lý các UTXO của bạn.


![Hình ảnh](assets/fr/34.webp)


Sau khi đã xác minh, bạn có thể dùng địa chỉ này để nhận bitcoin.


![Hình ảnh](assets/fr/35.webp)


## Gửi bitcoin bằng Multisig của bạn


Giờ đây, khi bạn đã nhận những Satss đầu tiên trên ví Multisig, bạn cũng có thể chi tiêu chúng! Trong Sparrow, vào tab "*Gửi*" để dựng một giao dịch mới.


![Hình ảnh](assets/fr/36.webp)


Nếu bạn muốn dùng *Coin Control*, tức là chọn thủ công các UTXO bạn muốn chi tiêu, hãy vào tab "*UTXO*". Chọn các UTXO bạn muốn chi tiêu, sau đó nhấp vào "*Gửi mục đã chọn*". Bạn sẽ tự động được chuyển đến tab "*Gửi*", với các UTXO đã được điền sẵn.


![Hình ảnh](assets/fr/37.webp)


Nhập địa chỉ đích. Có thể thêm nhiều địa chỉ bằng cách nhấp vào "*+ Thêm*".


![Hình ảnh](assets/fr/38.webp)


Thêm một "*Nhãn*" để mô tả mục đích của khoản chi này, giúp bạn theo dõi các giao dịch dễ dàng hơn.


![Hình ảnh](assets/fr/39.webp)


Nhập số tiền sẽ gửi đến địa chỉ đã chọn.


![Hình ảnh](assets/fr/40.webp)


Điều chỉnh mức phí theo điều kiện mạng hiện tại. Ví dụ, hãy tham khảo [Mempool.space](https://Mempool.space/) để chọn một mức phí phù hợp.


Sau khi kiểm tra tất cả tham số giao dịch, nhấp vào "*Tạo giao dịch*".


![Hình ảnh](assets/fr/41.webp)


Nếu mọi thứ ổn, nhấp vào "*Hoàn tất giao dịch để ký*".


![Hình ảnh](assets/fr/42.webp)


Ở cuối màn hình, bạn sẽ thấy Sparrow đang chờ 2 chữ ký. Điều này là bình thường: ví được dùng ở đây là Multisig 2-trong-3.


![Hình ảnh](assets/fr/43.webp)


Tôi bắt đầu ký bằng Passport. Trong Sparrow, nhấp vào "*Hiển thị QR*" để hiển thị PSBT (*Giao dịch Bitcoin được ký một phần*) dưới dạng các mã QR động. Trên Passport, chọn tài khoản multisig và chọn "*Ký bằng mã QR*", rồi quét mã QR do Sparrow hiển thị.

Trên màn hình ví phần cứng của bạn, hãy kiểm tra cẩn thận các tham số giao dịch: địa chỉ người nhận, số tiền gửi và phí. Sau khi giao dịch đã được xác nhận, hãy phê duyệt để tiếp tục ký.

Sau khi bạn phê duyệt giao dịch, Passport hiển thị PSBT đã ký dưới dạng các mã QR động. Trong Sparrow, nhấp vào "*Quét QR*" và quét các mã đó bằng webcam của bạn. Chữ ký Passport sau đó được thêm vào. Bây giờ tôi dùng Ledger cho chữ ký bắt buộc thứ hai: tôi kết nối và mở khóa nó, rồi nhấp vào "*Ký*" trong Sparrow.


![Hình ảnh](assets/fr/48.webp)


Nhấp vào "*Ký*" bên cạnh tên ví phần cứng của bạn.


![Hình ảnh](assets/fr/49.webp)


Lần đầu tiên bạn dùng Ledger với Multisig này, Sparrow sẽ yêu cầu bạn xác minh các khóa công khai mở rộng (xpub) của những người đồng ký. Giống như với Passport, bước này ngăn bạn ký mù sau này. Để xác thực thông tin này, hãy so sánh xpub hiển thị trên màn hình Ledger với những xpub được cung cấp trực tiếp bởi các ví phần cứng khác của bạn.


![Hình ảnh](assets/fr/50.webp)


Kiểm tra địa chỉ người nhận, số tiền được chuyển và phí giao dịch, rồi ký giao dịch.


![Hình ảnh](assets/fr/51.webp)


Nhấn màn hình để ký.


![Hình ảnh](assets/fr/52.webp)


Sparrow hiện có hai chữ ký cần thiết để giải phóng tiền từ ví Multisig. Kiểm tra giao dịch lần cuối, và nếu mọi thứ ổn, nhấp vào "*Phát giao dịch*" để phát nó lên mạng.


![Hình ảnh](assets/fr/53.webp)


Bạn sẽ tìm thấy giao dịch này trong tab "*Giao dịch*" của Sparrow Wallet.


![Hình ảnh](assets/fr/54.webp)


Chúc mừng, giờ đây bạn đã biết cách thiết lập và sử dụng ví đa chữ ký trên Sparrow. Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón cái xanh bên dưới. Hãy thoải mái chia sẻ bài viết này trên các mạng xã hội của bạn. Cảm ơn bạn đã chia sẻ!


Để đi xa hơn, tôi khuyên bạn tham khảo hướng dẫn này về một phương pháp khác để tăng bảo mật cho ví Bitcoin của bạn, cụm từ mật khẩu BIP39:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
