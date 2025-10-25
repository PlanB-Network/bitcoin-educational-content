---
name: Jade Plus - Sparrow
description: Cấu hình nâng cao của Jade Plus với Sparrow Wallet
---
![cover](assets/cover.webp)

Jade Plus là ví phần cứng chỉ dành cho Bitcoin do Blockstream thiết kế. Đây là phiên bản kế thừa của Jade cổ điển, với các cải tiến về phần mềm, nhiều tùy chọn hơn và thiết kế công thái học được thiết kế lại để sử dụng trực quan hơn. Phiên bản mới này tự hào có màn hình LCD 1,9 inch tuyệt đẹp, với gam màu rộng hơn so với phiên bản trước. Các nút và điều hướng menu cũng đã được tối ưu hóa.

Jade Plus có thể được sử dụng theo nhiều cách: thông qua kết nối có dây USB-C, ở chế độ "*Air-Gap*" với thẻ micro SD (cần có bộ chuyển đổi), qua Bluetooth hoặc thậm chí bằng cách trao đổi mã QR nhờ camera tích hợp. Ví phần cứng này chạy bằng pin.

Có giá từ 149,99 đô la cho phiên bản màu đen cơ bản và giá có thể tăng lên đến 20 đô la cho phiên bản "*Genesis Grey*" hoặc "*Lunar Silver*". Do đó, Jade Plus là một lựa chọn thú vị, với các chức năng tiên tiến tương đương với các ví phần cứng cao cấp như Coldcard Q hoặc Passport V2, nhưng với mức giá khá thấp, gần với các mẫu tầm trung.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

Jade Plus tương thích với hầu hết các phần mềm quản lý danh mục đầu tư. Sau đây là tóm tắt về khả năng tương thích tại thời điểm viết bài (tháng 1 năm 2025):

| Máy tính để bàn | Di động | USB | Bluetooth | QR | JadeLink | Phần mềm quản lý

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Dòng xanh xanh | 🟢 | 🟢 | 🟢 (Di động) | 🟢 | 🔴 |

| dây leo | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |

| Chim sẻ | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 |

| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |

| Bóng ma | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |

| Ví Xanh | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |

| Điện | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

| Thủ môn | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

Trong hướng dẫn này, chúng tôi sẽ thiết lập cấu hình nâng cao của Jade Plus với phần mềm Sparrow Wallet trên máy tính để bàn ở chế độ mã QR. Cấu hình này lý tưởng cho người dùng trung cấp hoặc có kinh nghiệm. Nếu bạn đang tìm kiếm một cách tiếp cận đơn giản hơn cho người mới bắt đầu, tôi khuyên bạn nên xem hướng dẫn này, trong đó chúng tôi sử dụng Jade Plus với Green Wallet qua kết nối Bluetooth:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Mô hình an toàn Jade Plus

Jade Plus sử dụng mô hình bảo mật dựa trên "phần tử bảo mật ảo", được hiện thực hóa bằng "blind oracle". Cụ thể, cơ chế này kết hợp mã PIN do người dùng chọn, một bí mật được lưu trữ trên Jade và một bí mật do oracle nắm giữ (máy chủ do Blockstream duy trì), để tạo khóa AES-256 phân phối trên hai thực thể. Trong quá trình khởi tạo, trao đổi ECDH bảo mật thông tin liên lạc với oracle và mã hóa cụm từ khôi phục trên ví phần cứng. Trên thực tế, khi bạn muốn truy cập hạt giống để ký giao dịch, bạn cần truy cập vào:


- Bản thân thiết bị Jade Plus;
- Để PIN để mở khóa thiết bị;
- Và đến bí mật của lời sấm truyền.

Ưu điểm chính của phương pháp này là không có điểm lỗi duy nhất ở cấp độ phần cứng, vì nếu kẻ tấn công có thể truy cập vào Jade của bạn, việc trích xuất khóa đòi hỏi phải xâm phạm đồng thời Jade và oracle. Mô hình này cũng có nghĩa là Jade Plus hoàn toàn là mã nguồn mở, tránh được các ràng buộc liên quan đến việc sử dụng các thành phần bảo mật vật lý thực sự, chẳng hạn như các thành phần được sử dụng trên Ledger.

Nhược điểm của hệ thống này là việc sử dụng Jade Plus phụ thuộc vào oracle do Blockstream duy trì. Nếu oracle này không thể truy cập được, bạn sẽ không thể sử dụng ví phần cứng trực tiếp bằng mã PIN nữa. Tuy nhiên, điều này không có nghĩa là bitcoin của bạn bị mất, vì chúng vẫn có thể được khôi phục bằng cụm từ khôi phục của bạn, bạn có thể nhập cụm từ này vào Jade Plus ở chế độ "*stateless*". Để khắc phục sự phụ thuộc này, bạn cũng có thể cấu hình và quản lý máy chủ oracle của riêng mình.

Một lựa chọn khác để quản lý hạt giống của bạn là không đăng ký nó trên Jade Plus. Trong trường hợp này, Jade chỉ trở thành thiết bị chữ ký. Trong quá trình khởi tạo, ngoài việc lưu cụm từ khôi phục dưới dạng từ thông thường, bạn cũng sẽ lưu nó dưới dạng mã QR được tạo thủ công. Theo cách này, mỗi lần bạn sử dụng ví của mình, bạn có thể nhập hạt giống bằng camera của Jade. Đây có thể là một lựa chọn thú vị cho người dùng nâng cao, tùy thuộc vào chiến lược bảo mật của bạn, nhưng bạn cần cẩn thận để lưu hạt giống và bảo vệ nó, vì ngay cả khi là mã QR, nó vẫn có thể cho phép bất kỳ ai đánh cắp tiền của bạn. Chúng ta sẽ xem xét tùy chọn này trong hướng dẫn này, nhưng nó không bắt buộc.

## Mở hộp Jade Plus

Khi nhận được Jade Plus, hãy kiểm tra xem hộp và niêm phong có còn nguyên vẹn không để đảm bảo gói hàng chưa bị mở.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

Trong hộp bạn sẽ tìm thấy:


- Ngọc bích Plus;
- Cáp USB-C;
- Thẻ để ghi lại cụm từ ghi nhớ của bạn dưới dạng từ hoặc dưới dạng "*CompactSeedQR*";
- Một số hướng dẫn sử dụng;
- Một sợi dây;
- Một số nhãn dán.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

Thiết bị có 4 nút điều hướng:


- Nút ở góc dưới bên phải để bật Jade;
- Nút lớn ở mặt trước của thiết bị được dùng để chọn một mục;
- Hai nút nhỏ ở trên cùng cho phép bạn điều hướng sang trái và phải;
- Bạn cũng có thể chọn một mục bằng cách nhấp đồng thời vào hai nút ở phía trên cùng của thiết bị.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Thiết lập ví Bitcoin mới

Nhấp vào nút bắt đầu.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Nhấp vào "*Cài đặt Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Chọn "Cài đặt nâng cao".

![Image](assets/fr/07.webp)

Sau đó nhấp vào "*Tạo ví mới*" để tạo hạt giống mới. Bạn có thể chọn giữa cụm từ ghi nhớ 12 hoặc 24 từ. Tính bảo mật của ví của bạn vẫn tương đương với cả hai tùy chọn, vì vậy có thể thuận tiện hơn khi chọn tùy chọn đơn giản nhất để lưu, tức là 12 từ.

![Image](assets/fr/08.webp)

Nhấp vào nút "*Tiếp tục*" để hiển thị cụm từ khôi phục mới của bạn.

![Image](assets/fr/09.webp)

Jade Plus của bạn hiển thị cụm từ ghi nhớ 12 từ của bạn. **Cụm từ ghi nhớ này cung cấp cho bạn quyền truy cập đầy đủ, không hạn chế vào tất cả bitcoin của bạn. Bất kỳ ai sở hữu cụm từ này đều có thể đánh cắp tiền của bạn, ngay cả khi không có quyền truy cập vật lý vào Jade Plus của bạn. Cụm từ 12 từ khôi phục quyền truy cập vào bitcoin của bạn trong trường hợp Jade của bạn bị mất, bị trộm hoặc bị vỡ. Do đó, điều rất quan trọng là phải lưu trữ cẩn thận và cất giữ ở nơi an toàn.**

Bạn có thể viết lên tấm bìa cứng đi kèm trong hộp hoặc để an toàn hơn, tôi khuyên bạn nên khắc lên đế thép không gỉ để bảo vệ khỏi hỏa hoạn, lũ lụt hoặc sụp đổ.

![Image](assets/fr/10.webp)

Để biết thêm thông tin về cách lưu và quản lý cụm từ ghi nhớ đúng cách, tôi thực sự khuyên bạn nên làm theo hướng dẫn khác này, đặc biệt nếu bạn là người mới bắt đầu:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

tất nhiên, bạn không bao giờ được chia sẻ những từ này trên Internet, như tôi đang làm trong hướng dẫn này. Danh mục mẫu này sẽ chỉ được sử dụng trên Testnet và sẽ bị xóa vào cuối hướng dẫn.

Nhấp vào mũi tên bên phải màn hình để hiển thị các từ sau.

![Image](assets/fr/11.webp)

Sau khi bạn đã lưu cụm từ của mình, Jade Plus sẽ yêu cầu bạn xác nhận. Chọn từ đúng theo thứ tự bằng cách sử dụng các nút ở đầu thiết bị và nhấp vào nút ở giữa để chuyển sang từ tiếp theo.

![Image](assets/fr/12.webp)

Sau đó, bạn có 2 lựa chọn. Như đã giải thích trong phần giới thiệu, bạn có thể chọn lưu hạt giống trực tiếp trên thiết bị và sử dụng hệ thống bảo vệ "*Virtual Secure Element*" của Blockstream để truy cập ví của bạn (Lựa chọn 1) hoặc lưu hạt giống của bạn dưới dạng mã QR và quét mã này mỗi khi sử dụng (Lựa chọn 2).

Đối với Tùy chọn 1, hãy chọn "*Không*", và đối với Tùy chọn 2, hãy chọn "*Có*".

![Image](assets/fr/13.webp)

### Tùy chọn 1: Mở khóa mã PIN QR

Nếu bạn đã chọn tùy chọn 1 (CompactSeedQR: "*No*"), bạn sẽ được đưa trực tiếp đến lựa chọn phương thức kết nối. Trong hướng dẫn này, chúng tôi muốn sử dụng thiết bị ở chế độ Air-Gap thông qua trao đổi mã QR, vì vậy hãy chọn "*QR*".

![Image](assets/fr/27.webp)

Nhấp vào "*Tiếp tục*".

![Image](assets/fr/28.webp)

Mã PIN được sử dụng để mở khóa Jade của bạn và cung cấp khả năng bảo vệ chống lại truy cập vật lý trái phép. Mã PIN này không liên quan đến việc tạo ra khóa mật mã của ví của bạn. Vì vậy, ngay cả khi không truy cập được vào mã PIN này, việc sở hữu cụm từ ghi nhớ 12 từ của bạn sẽ cho phép bạn lấy lại quyền truy cập vào bitcoin của mình. Chúng tôi khuyên bạn nên chọn mã PIN càng ngẫu nhiên càng tốt. Ngoài ra, hãy đảm bảo rằng bạn lưu mã này ở một nơi riêng biệt với nơi lưu trữ Jade của bạn, chẳng hạn như trong trình quản lý mật khẩu.

Chọn mã PIN gồm 6 chữ số trên Jade của bạn bằng cách sử dụng các nút trái và phải để cuộn qua các chữ số và nút giữa để xác nhận từng chữ số.

![Image](assets/fr/29.webp)

Xác nhận mã PIN lần thứ hai.

![Image](assets/fr/30.webp)

Như đã giải thích trong phần giới thiệu, hạt giống của bạn được lưu trữ mã hóa trên Jade Plus. Để giải mã, bạn phải cung cấp:


- Mã PIN hợp lệ (mà chúng tôi vừa thiết lập);
- Bí mật của nhà tiên tri được Blockstream nắm giữ.

Trong hướng dẫn nâng cao này, chúng ta sẽ sử dụng Sparrow Wallet để quản lý ví Bitcoin của mình. Tuy nhiên, không giống như phần mềm Green Wallet của Blockstream, Sparrow không có quyền truy cập vào oracle trên máy chủ của Blockstream. Do đó, chúng ta sẽ sử dụng trang web của Blockstream để lấy bí mật oracle mỗi lần mở khóa Jade Plus.

Truy cập https://jadefw.blockstream.com/pinqr/index.html

Nhấp vào "*Bắt đầu mở khóa QR*".

![Image](assets/fr/31.webp)

Nhấp vào "*Hoàn tất*" vì bạn đã chọn mã PIN trên Jade Plus.

![Image](assets/fr/32.webp)

Sử dụng camera của máy tính để quét mã QR hiển thị trên màn hình Jade.

![Image](assets/fr/33.webp)

Xác nhận trên Jade để truy cập vào màn hình tiếp theo.

![Image](assets/fr/34.webp)

Quét mã QR hiện có trên trang web để tìm ra bí mật của lời sấm truyền.

![Image](assets/fr/35.webp)

Bây giờ danh mục đầu tư của bạn đã được tạo, bạn có thể tiến hành các bước tiếp theo và bỏ qua phần phụ "*Tùy chọn 2: CompactSeedQR*".

![Image](assets/fr/36.webp)

Mỗi lần khởi động, hãy nhấp vào "*Chế độ QR*".

![Image](assets/fr/37.webp)

Chọn "*Mở khóa mã PIN QR*".

![Image](assets/fr/38.webp)

Nhập mã PIN của bạn.

![Image](assets/fr/39.webp)

Sau đó, hãy truy cập [trang web Blockstream](https://jadefw.blockstream.com/pinqr/qrpin.html) để trao đổi mã QR với oracle.

![Image](assets/fr/40.webp)

Jade của bạn hiện đã được mở khóa.

![Image](assets/fr/41.webp)

### Tùy chọn 2: CompactSeedQR

Nếu bạn đã chọn tùy chọn 2 (CompactSeedQR: "*Có*"), hãy nhấp vào "*Có*" một lần nữa.

![Image](assets/fr/14.webp)

Nhấp vào "*Bắt đầu*".

![Image](assets/fr/15.webp)

Bạn có thể sử dụng cơ sở mã QR được cung cấp trong hộp Jade Plus. Chọn hộp phù hợp tùy thuộc vào việc bạn đã chọn câu 12 hay 24 từ. Bạn cũng có thể [in mẫu từ trang web Blockstream](https://help.blockstream.com/hc/article_attachments/41928319071769).

Jade Plus của bạn sẽ hiển thị từng vùng mã QR.

![Image](assets/fr/16.webp)

Sử dụng bút để tô màu vào các ô vuông và tái tạo hạt giống của bạn dưới dạng mã QR. Hãy chính xác để đảm bảo rằng máy ảnh Jade Plus có thể quét sau. Sử dụng mũi tên để chuyển sang khu vực tiếp theo.

![Image](assets/fr/17.webp)

Khi hoàn tất, nhấp vào "*Xong*".

![Image](assets/fr/18.webp)

Quét mã QR thủ công của bạn bằng Jade Plus để kiểm tra tính hợp lệ.

![Image](assets/fr/19.webp)

Nếu bản sao lưu giấy tờ của bạn chính xác, hãy nhấp vào "*Tiếp tục*".

![Image](assets/fr/20.webp)

Trong hướng dẫn này, chúng ta sẽ sử dụng chế độ kết nối dựa hoàn toàn vào chức năng quét mã QR, vì vậy hãy chọn "*QR*".

![Image](assets/fr/21.webp)

Bạn cũng có thể chọn thêm mã PIN ngoài bản sao lưu CompactSeedQR của mình, như trong tùy chọn 1. Tùy chọn này cung cấp hai cách để truy cập ví của bạn: thông qua mã PIN và hệ thống "Phần tử bảo mật ảo" của Blockstream hoặc thông qua CompactSeedQR.

Nếu bạn chọn tùy chọn mã PIN kép, hãy chọn "*PIN*" và làm theo các bước tương tự như trong tùy chọn 1 để đặt mã PIN.

Nếu bạn chỉ muốn tiếp tục sử dụng CompactSeedQR, hãy chọn "*SeedQR*".

![Image](assets/fr/22.webp)

Bây giờ danh mục đầu tư của bạn đã được tạo, bạn có thể chuyển sang các bước tiếp theo.

![Image](assets/fr/23.webp)

Mỗi lần khởi động, hãy nhấp vào nút "*Chế độ QR*", sau đó nhấp vào "*Quét SeedQR*".

![Image](assets/fr/24.webp)

Sử dụng camera của thiết bị để quét hạt giống đã lưu dưới dạng mã QR.

![Image](assets/fr/25.webp)

Jade của bạn hiện đã được mở khóa.

![Image](assets/fr/26.webp)

## Thêm mật khẩu BIP39

Cụm mật khẩu BIP39 là mật khẩu tùy chọn mà bạn có thể tự do lựa chọn và được thêm vào cụm từ ghi nhớ của bạn để tăng cường bảo mật cho ví. Khi bật tính năng này, việc truy cập vào ví Bitcoin của bạn sẽ yêu cầu cả cụm từ ghi nhớ và cụm mật khẩu. Nếu không có một trong hai, sẽ không thể khôi phục ví.

Trước khi cấu hình tùy chọn này trên Jade Plus, chúng tôi khuyên bạn nên đọc bài viết này để hiểu đầy đủ về hoạt động lý thuyết của cụm mật khẩu và tránh các lỗi có thể dẫn đến mất bitcoin của bạn:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Khi Jade vẫn bị khóa (chỉ có thể nhập mật khẩu khi thiết bị chưa được mở khóa), hãy truy cập vào menu "*Tùy chọn*".

![Image](assets/fr/42.webp)

Chọn "*Mật khẩu BIP39*".

![Image](assets/fr/43.webp)

Trong tùy chọn "*Tần suất*", bạn có thể chọn xem Jade Plus có yêu cầu bạn nhập mật khẩu mỗi khi khởi động hay không:


- "*Đã tắt*" vô hiệu hóa việc sử dụng cụm mật khẩu;
- "*Chỉ đăng nhập tiếp theo*" sẽ yêu cầu bạn quay lại menu này để kích hoạt yêu cầu mật khẩu của bạn khi khởi động lần sau. Tùy chọn này cho phép bạn không tiết lộ cách sử dụng;
- "*Luôn hỏi*" khiến Jade liên tục yêu cầu bạn nhập mật khẩu mỗi khi khởi động, qua đó tiết lộ rằng ví của bạn được bảo vệ bằng mật khẩu.

Chọn tùy chọn theo chiến lược bảo mật của bạn. Cá nhân tôi chọn "*Luôn hỏi*" làm ví dụ.

![Image](assets/fr/44.webp)

Sau đó, bạn có thể chọn một trong hai phương pháp để nhập mật khẩu:


- "*Thủ công*: Bàn phím ảo cho phép bạn nhập chữ cái (chữ hoa và chữ thường), số và ký hiệu, từng ký tự một. Đây là phương pháp tiêu chuẩn cho tất cả ví phần cứng;
- "*WordList*": Phương pháp cụ thể do Blockstream thiết kế cho Jade, giúp tăng tốc độ nhập mật khẩu và tăng entropy của nó. Trong quá trình nhập, hệ thống gợi ý các từ trong danh sách BIP39, giúp việc mở khóa dễ dàng hơn. Phương pháp này tự động tạo ra một câu bằng cách nối các từ đã chọn, cách nhau bằng dấu cách (ví dụ: `abandon ability able`).

Cá nhân tôi khuyên bạn nên sử dụng phương pháp đầu tiên vì đây là tiêu chuẩn mà bạn sẽ tìm thấy trên tất cả các hỗ trợ danh mục đầu tư khác.

![Image](assets/fr/45.webp)

Sau đó, bạn có thể quay lại màn hình chính và mở khóa ví như bình thường, bằng mã PIN hoặc CompactSeedQR (như hình trên). Sau đó, bạn sẽ được yêu cầu nhập mật khẩu.

![Image](assets/fr/46.webp)

Nhập nó vào bàn phím Jade và đảm bảo tạo một hoặc nhiều bản sao lưu trên phương tiện vật lý (giấy hoặc kim loại). Ví dụ, tôi đang sử dụng một cụm mật khẩu rất yếu, nhưng bạn cần chọn một cụm mật khẩu mạnh, ngẫu nhiên bao gồm tất cả các loại ký tự và đủ dài (như mật khẩu mạnh).

![Image](assets/fr/47.webp)

Nếu mật khẩu của bạn hợp lệ, hãy xác nhận.

![Image](assets/fr/48.webp)

Xin lưu ý rằng mật khẩu BIP39 phân biệt chữ hoa và chữ thường. Nếu bạn nhập mật khẩu hơi khác so với mật khẩu được cấu hình ban đầu, Jade sẽ không báo lỗi nhưng sẽ lấy một bộ khóa mật mã khác không phải là khóa trong danh mục đầu tư ban đầu của bạn.

Do đó, điều quan trọng là khi cấu hình, hãy ghi lại dấu vân tay khóa chính của bạn, có thể tìm thấy ở góc dưới bên phải màn hình. Ví dụ, với cụm mật khẩu `PBN`, dấu vân tay khóa chính của tôi là `3AD1AE65`.

![Image](assets/fr/49.webp)

Mỗi lần bạn mở khóa Jade bằng mật khẩu của mình, hãy kiểm tra xem dấu vân tay có giống với dấu vân tay bạn đã nhập trong quá trình cấu hình không. Nếu đúng, mật khẩu của bạn là chính xác và bạn đang truy cập đúng ví Bitcoin. Nếu không, bạn đang truy cập nhầm ví và cần thử lại, chú ý không nhập sai.

Trước khi bạn nhận được bitcoin đầu tiên trong ví của mình, **Tôi thực sự khuyên bạn nên thực hiện một bài kiểm tra khôi phục rỗng**. Ghi lại một số thông tin tham chiếu, chẳng hạn như xpub hoặc địa chỉ nhận đầu tiên của bạn, sau đó xóa ví của bạn trên Jade Plus trong khi nó vẫn còn rỗng (`Tùy chọn -> Thiết bị -> Khôi phục cài đặt gốc`). Sau đó, hãy thử khôi phục ví của bạn bằng cách sử dụng bản sao lưu giấy của cụm từ ghi nhớ và bất kỳ cụm mật khẩu nào. Kiểm tra xem thông tin cookie được tạo sau khi khôi phục có khớp với thông tin bạn đã ghi ban đầu không. Nếu có, bạn có thể yên tâm rằng bản sao lưu giấy của bạn là đáng tin cậy. Để tìm hiểu thêm về cách thực hiện khôi phục thử nghiệm, hãy xem hướng dẫn khác này:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Cấu hình ví trên Sparrow Wallet

Trong hướng dẫn này, tôi trình bày cách sử dụng nâng cao Jade Plus bằng Sparrow Wallet. Tuy nhiên, ví phần cứng này tương thích với nhiều chương trình khác, chẳng hạn như Liana, Nunchuk, Spectre, Green và Keeper. Các khả năng tương thích này khác nhau về mặt kết nối: USB, Bluetooth hoặc mã QR (xem bảng trong phần giới thiệu để biết chi tiết).

Bắt đầu bằng cách tải xuống và cài đặt Sparrow Wallet [từ trang web chính thức](https://sparrowwallet.com/) trên máy tính của bạn, nếu bạn chưa thực hiện.

![Image](assets/fr/50.webp)

Hãy chắc chắn kiểm tra tính xác thực và tính toàn vẹn của phần mềm trước khi cài đặt. Nếu bạn không biết cách thực hiện, vui lòng tham khảo hướng dẫn này:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sau khi mở Sparrow Wallet, hãy nhấp vào tab "*File*", sau đó nhấp vào "*New Wallet*".

![Image](assets/fr/51.webp)

Đặt tên cho ví của bạn, sau đó nhấp vào "*Tạo ví*".

![Image](assets/fr/52.webp)

Chọn "*Ví phần cứng không có kết nối mạng*".

![Image](assets/fr/53.webp)

Nhấp vào "*Quét...*" bên cạnh tùy chọn "*Jade*".

![Image](assets/fr/54.webp)

Mở khóa Jade Plus của bạn và nếu bạn đang sử dụng Jade Plus, hãy nhập mật khẩu của bạn. Sau đó, hãy vào menu "*Tùy chọn*", chọn "*Ví*" và nhấp vào "*Xuất Xpub*".

![Image](assets/fr/55.webp)

Jade của bạn sẽ hiển thị Keystore của bạn thông qua một số mã QR. Quét chúng trên máy của bạn bằng Sparrow.

![Image](assets/fr/56.webp)

Bây giờ bạn sẽ thấy dấu vân tay xpub và khóa chính của mình, chúng phải khớp với dấu vân tay trên Jade Plus của bạn. Nhấp vào "*Áp dụng*".

![Image](assets/fr/57.webp)

Đặt mật khẩu mạnh để bảo mật quyền truy cập vào Ví Sparrow của bạn. Mật khẩu này sẽ bảo vệ khóa công khai, địa chỉ, nhãn và lịch sử giao dịch của bạn khỏi sự truy cập trái phép. Tốt nhất là bạn nên lưu mật khẩu này trong trình quản lý mật khẩu để không quên.

![Image](assets/fr/58.webp)

Danh mục đầu tư của bạn hiện đã được cấu hình chính xác trên Sparrow.

![Image](assets/fr/59.webp)

## Nhận bitcoin

Bây giờ Jade Plus của bạn đã được cấu hình, bạn đã sẵn sàng nhận sats đầu tiên trên ví Bitcoin mới của mình. Để thực hiện, trên Sparrow, hãy nhấp vào menu "*Nhận*".

![Image](assets/fr/60.webp)

Sparrow sẽ hiển thị địa chỉ tiếp tân trống đầu tiên trong danh mục đầu tư của bạn.

![Image](assets/fr/61.webp)

Trước khi sử dụng, hãy kiểm tra trên màn hình Jade Plus để đảm bảo nó thuộc về ví Bitcoin của chúng ta. Trên Jade, nhấp vào "*Quét QR*", sau đó quét mã QR của địa chỉ được hiển thị trên Sparrow.

![Image](assets/fr/62.webp)

Kiểm tra xem địa chỉ hiển thị trên màn hình Jade của bạn có tương ứng với địa chỉ hiển thị trên Sparrow Wallet không. Nếu có, hãy nhấp vào dấu kiểm để tiếp tục.

![Image](assets/fr/63.webp)

Sau đó, ví phần cứng của bạn sẽ xác nhận rằng địa chỉ này là một phần trong ví của bạn và nó chứa khóa riêng có liên quan.

![Image](assets/fr/64.webp)

Nếu địa chỉ được Jade của bạn xác thực, giờ đây bạn có thể sử dụng nó để nhận bitcoin. Khi giao dịch được phát trên mạng, nó sẽ xuất hiện trên Sparrow. Đợi cho đến khi bạn nhận được đủ xác nhận để coi giao dịch là xác thực.

![Image](assets/fr/65.webp)

## Gửi bitcoin

Bây giờ bạn đã có một vài sats trong ví, bạn cũng có thể gửi một ít. Để thực hiện, hãy nhấp vào menu "*UTXOs*".

![Image](assets/fr/66.webp)

Chọn UTXO bạn muốn sử dụng làm đầu vào cho giao dịch này, sau đó nhấp vào "*Gửi mục đã chọn*".

![Image](assets/fr/67.webp)

Nhập địa chỉ người nhận, nhãn ghi nhớ mục đích giao dịch và số tiền bạn muốn gửi đến địa chỉ này.

![Image](assets/fr/68.webp)

Điều chỉnh mức phí theo điều kiện thị trường hiện tại, sau đó nhấp vào "*Tạo giao dịch*".

![Image](assets/fr/69.webp)

Kiểm tra xem tất cả các thông số giao dịch đã chính xác chưa, sau đó nhấp vào "*Hoàn tất giao dịch để ký*".

![Image](assets/fr/70.webp)

Nhấp vào "*Hiển thị QR*" để hiển thị PSBT (*Giao dịch Bitcoin đã ký một phần*). Sparrow đã xây dựng giao dịch, nhưng vẫn thiếu chữ ký để mở khóa bitcoin được sử dụng trong đầu vào. Những chữ ký này chỉ có thể được thực hiện bởi Jade Plus, nơi lưu trữ hạt giống của bạn, cung cấp quyền truy cập vào khóa riêng cần thiết để ký giao dịch.

![Image](assets/fr/71.webp)

Trên Jade Plus, hãy nhấp vào "*Quét QR*" để quét PSBT hiển thị trên Sparrow.

![Image](assets/fr/72.webp)

Xác nhận địa chỉ giao hàng và số tiền gửi là chính xác, sau đó nhấp vào mũi tên để xác nhận.

![Image](assets/fr/73.webp)

Hãy đảm bảo số tiền phí là số tiền bạn đã chọn, sau đó nhấp vào biểu tượng dấu tích ở góc trên bên trái của giao diện để ký giao dịch.

![Image](assets/fr/74.webp)

Trên Ví Sparrow, nhấp vào "*Quét QR*" và quét mã QR hiển thị trên Jade của bạn.

![Image](assets/fr/75.webp)

Giao dịch đã ký của bạn hiện đã sẵn sàng để phát trên mạng Bitcoin và được đưa vào khối bởi thợ đào. Nếu mọi thứ đều chính xác, hãy nhấp vào "*Phát Giao dịch*".

![Image](assets/fr/76.webp)

Giao dịch của bạn đã được phát sóng và đang chờ xác nhận.

![Image](assets/fr/77.webp)

Xin chúc mừng, giờ bạn đã biết cách thiết lập và sử dụng Jade Plus ở chế độ QR. Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái màu xanh lá cây bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn vì đã chia sẻ!

Để tìm hiểu sâu hơn, tôi xin giới thiệu hướng dẫn khác về Jade Plus, trong đó chúng tôi định cấu hình Jade Plus qua Bluetooth bằng ứng dụng di động Green:

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0