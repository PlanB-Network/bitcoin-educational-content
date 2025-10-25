---
name: COLDCARD Q - Key Teleport
description: Key Teleport là gì và tôi sử dụng nó như thế nào?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Tính năng **Key Teleport** được Coinkite cung cấp cùng với thiết bị ColdCardQ hàng đầu của họ là gì?



**Key Teleport** cho phép bạn truyền dữ liệu mật giữa 2 ColdCardQ một cách an toàn. Kênh truyền thậm chí không cần mã hóa và có thể được công khai.



Có thể sử dụng để chuyển:





- Cụm từ **gW-0** (seed master của ColdCard Q hoặc các bí mật được lưu trữ trong [seed Vault] của ColdCardQ(https://coldcard.com/docs/temporary-seeds/#seed-vault).
- **ghi chú và mật khẩu bí mật**: đây có thể là bất kỳ thông tin bí mật nào hoặc toàn bộ thư mục [Ghi chú & Mật khẩu Bảo mật] (https://coldcard.com/docs/secure_notes/) trên ColdCardQ của bạn.
- bản sao lưu toàn bộ **ColdCardQ** của bạn: ColdCardQ nhận bản sao lưu này không được có seed Master để tính năng này hoạt động.
- gW-3 (*Giao dịch Bitcoin được ký một phần*) là một phần của chương trình **đa chữ ký**.



Điều này yêu cầu bạn phải nâng cấp [phần mềm thiết bị lên phiên bản v1.3.2Q](https://coldcard.com/docs/upgrade/) hoặc cao hơn.



## Làm thế nào để sử dụng Key Teleport?



### 1- Để chuyển bất kỳ loại dữ liệu nào



Ở đây, chúng ta sẽ xem xét việc chuyển các câu, ghi chú, mật khẩu seed hoặc toàn bộ quá trình chuyển bản sao lưu ColdCardQ. Trường hợp chuyển PSBT cho các giao dịch đa chữ ký sẽ được đề cập sau.



#### Chuẩn bị thiết bị để nhận bí mật



Trong menu **"Nâng cao / Công cụ**" trên ColdCardQ, chọn **"Dịch chuyển phím (bắt đầu) "**.


Trên màn hình tiếp theo, một mật khẩu 8 chữ số được đề xuất, ví dụ "20420219". Bạn sẽ cần cung cấp mật khẩu này cho người gửi. Ví dụ: sử dụng tin nhắn SMS để gửi mật khẩu này, hoặc hệ thống nhắn tin bảo mật yêu thích của bạn, hoặc thậm chí là cuộc gọi thoại.



Sau đó nhấp vào nút **"Enter**" trên ColdCardQ của bạn để chuyển sang bước tiếp theo.




![CCQ-key-teleport](assets/fr/01.webp)




Một mã QR sẽ được tạo trên màn hình. Một lần nữa, bạn cần cung cấp mã QR này cho "người gửi" ColdCardQ. Cách dễ nhất để thực hiện việc này là thông qua cuộc gọi video.



**KHÔNG GỬI MÃ QR NÀY QUA KÊNH TRUYỀN ĐÃ ĐƯỢC SỬ DỤNG ĐỂ GỬI MẬT KHẨU 8 CHỮ SỐ TRƯỚC ĐÓ**.



![CCQ-key-teleport](assets/fr/02.webp)



*Đối với những ai quan tâm, chúng ta hãy cùng tìm hiểu cơ chế cơ bản cho phép truyền tải bí mật qua các kênh không an toàn*



*Những gì chúng ta thực sự đang làm ở đây là khởi tạo việc chuyển giao bí mật thông qua phương pháp Diffie-Hellman, được đề cập trong khóa học BTC204 mà tôi đã đưa vào bên dưới*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Chúng tôi hiện có:*




- đã tạo một cặp khóa tạm thời (lần lượt là công khai/riêng tư Ka và ka với Ka=G.ka, G là điểm tạo ECDH) và một mật khẩu 8 chữ số.
- đã sử dụng mật khẩu này để mã hóa khóa công khai (Ka) thông qua AES-256-CTR, sau đó truyền mật khẩu này qua kênh truyền thông A đến ColdCardQ "gửi".
- Cuối cùng, chúng tôi truyền gói tin được mã hóa đến người gửi thông qua mã QR ở trên, sử dụng kênh truyền thông thứ hai B khác với kênh thứ nhất.



#### Chuẩn bị thiết bị sẽ gửi các bí mật



Từ thiết bị gửi, hãy nhấp vào nút **"QR"** để quét mã QR được thiết bị nhận gửi đến, sau đó nhập mật khẩu 8 chữ số đã được cung cấp ở bước trước qua một kênh riêng. Bây giờ, chúng ta đã sẵn sàng để bắt đầu gửi dữ liệu từ thiết bị "gửi".



**Vui lòng không nhập sai mật khẩu 8 chữ số, vì sẽ không có thông báo lỗi nào được hiển thị và quá trình sẽ tiếp tục. Tuy nhiên, quá trình truyền dữ liệu cuối cùng sẽ không thành công và bạn sẽ phải bắt đầu lại**.



![CCQ-key-teleport](assets/fr/03.webp)



*Đối với những ai tò mò hơn, chúng ta hãy cùng xem xét lại những gì chúng tôi đang thực hiện về mặt mật mã và chuyển giao bí mật:*




- chúng tôi đã nhập dữ liệu được mã hóa bằng cách quét mã QR trên thiết bị nhận.
- sau đó chúng tôi giải mã chúng bằng mật khẩu 8 chữ số được truyền cho chúng tôi qua kênh thứ cấp.
- do đó chúng ta sở hữu khóa công khai (Ka) được người nhận tạo ra ban đầu.
- Sau đó, chúng tôi generate một cặp khóa tạm thời mới (Kb/kb, với Kb=G.kb) trên thiết bị gửi, chúng tôi sử dụng cặp khóa này để áp dụng ECDH cho Ka. Do đó, chúng tôi thực hiện thao tác kb.Ka=Ks, trong đó Ks được gọi là **"Khóa Phiên"**.




Bây giờ bạn được yêu cầu chọn bản chất của bí mật sẽ được truyền giữa 2 ColdCardQ (ghi chú bí mật, mật khẩu, bản sao lưu đầy đủ, hạt giống có trong kho lưu trữ của bạn, thiết bị chính seed).



![CCQ-key-teleport](assets/fr/04.webp)



Bí mật của chúng ta sẽ là một tin nhắn ngắn bằng cách chọn **"Tin nhắn văn bản nhanh"**. Nhập tin nhắn của bạn (đối với chúng tôi là "PlanB Network tuyệt vời") rồi nhấn **"ENTER"**.


Sau đó, thiết bị sẽ tạo ra một mật khẩu ngẫu nhiên mới có tên là **"Mật khẩu dịch chuyển tức thời"**, trong ví dụ là "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Nhấn **"ENTER"** và bạn sẽ thấy một mã QR mới. Hãy quét mã này bằng thiết bị nhận. Và trên một kênh truyền thông khác, hãy truyền **"Mật khẩu dịch chuyển tức thời"** đến thiết bị nhận.



![CCQ-key-teleport](assets/fr/06.webp)



*Một lần nữa, dành cho những ai tò mò, trong giai đoạn này:*




- sau khi chọn bí mật cần truyền, chúng tôi generate tạo một mật khẩu ngẫu nhiên mới có tên là **"Mật khẩu dịch chuyển tức thời"**.
- sau đó chúng tôi mã hóa các bí mật thông qua AES-256-CTR bằng cách sử dụng **"Khóa phiên"**, "Ks", được tạo ở bước trước.
- chúng tôi thêm tiền tố cho gói tin đã được mã hóa bằng **"Khóa phiên"** với khóa công khai Kb của chúng tôi, sau đó thêm Layer của mã hóa AES-256-CTR với **"Mật khẩu dịch chuyển tức thời"**. Sau đó, toàn bộ dữ liệu được mã hóa thành mã QR




#### Hoàn tất việc chuyển giao bí mật đến thiết bị nhận



Nhấn nút **"QR"** để quét mã QR do thiết bị gửi hiển thị thông qua kênh Visio. Bạn sẽ được yêu cầu nhập **"Mật khẩu dịch chuyển"** cho chúng tôi "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





Sau đó, dữ liệu được giải mã và thiết bị nhận có thể hiểu được. Thông điệp nhận được thực sự là "PlanB Network thật tuyệt vời". Chỉ vậy thôi.



![CCQ-key-teleport](assets/fr/08.webp)



*Điều gì thực sự đã xảy ra trong giai đoạn cuối này :*?




- chúng tôi đã giải mã dữ liệu được truyền đi bởi người gửi bằng cách sử dụng **"Mật khẩu dịch chuyển tức thời"**.
- do đó chúng ta có khóa công khai Kb và thông điệp bí mật được mã hóa bằng **"Khóa phiên"**, "Ks". Nhưng làm sao chúng ta có thể làm được điều này vì, với tư cách là người nhận, chúng ta không biết Ks, được tạo bởi người gửi?
- Chúng ta cần áp dụng khóa riêng "ka" từ bước đầu tiên **"Chuẩn bị thiết bị sẽ nhận dữ liệu"** cho khóa công khai Kb.
- Trên thực tế, bằng cách tính ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks, ta tìm được Ks. Cuối cùng, Ks được dùng để giải mã thông điệp bí mật.



### 2- Để chuyển PSBT sang Multisig (nâng cao)



Điều này giả định rằng Wallet Multisig của bạn đã được tạo và thiết bị ColdCardQ của bạn đã được thiết lập sẵn để có thể thực hiện các giao dịch đa chữ ký. Nếu không, vui lòng xem giải thích tại [đây](https://coldcard.com/docs/Multisig/) trên trang web Coinkite.



Một lời nhắc nhở nhanh về chữ ký đa dạng Wallet (Multisig).



Thông thường, để chi tiêu số tiền Wallet của bạn, chỉ cần một khóa riêng để mở khóa UTXO liên kết với địa chỉ của bạn.


Trong trường hợp Wallet Multisig, có thể cần tới 15 khóa riêng tư và do đó cần 15 chữ ký để chi tiêu số tiền này. Danh mục này được gọi là danh mục "M trên N", với N từ 1 đến 15 và M là số chữ ký cần thiết để số tiền này có thể được chi tiêu. Ví dụ: danh mục Wallet Multisig 3 trên 5 sẽ yêu cầu ít nhất 3 chữ ký trong số 5 chữ ký có thể.



Thách thức lúc này là phải phối hợp giữa những người ký để lần lượt ký "PSBT" cho "Partially Signed Bitcoin Transaction". Trong bối cảnh này, "**Key Teleport**" có thể được sử dụng để truyền tải PSBT giữa những người đồng ký một cách đơn giản và bảo mật. Một cuộc gọi video đơn giản giữa những người đồng ký sẽ là giải pháp.



Sau đây là cách thực hiện trên Multisig 3 trong số 4.



**Người ký tên 1:**



Người ký 1 nhập và ký PSBT. Cuối cùng, anh ta nhấp vào **"T "** để sử dụng **"Key Teleport "** để truyền PSBT đến người ký 2.



![CCQ-key-teleport](assets/fr/09.webp)




Sau khi chọn người ký 2 bằng cách nhấp vào **"ENTER"**, một "MẬT KHẨU TRUYỀN TẢI" (ở đây là JJ YC AB 6A) sẽ được cung cấp, mật khẩu này phải được truyền đến người ký 2 qua một kênh liên lạc khác. Ví dụ: tin nhắn SMS hoặc cuộc gọi thoại, **không phải** cuộc gọi video.



Nhấn **"ENTER "** lần nữa và mã QR đại diện cho PSBT được ký bởi 1 sau đó được mã hóa bằng "MẬT KHẨU TELEPORT" sẽ xuất hiện.



![CCQ-key-teleport](assets/fr/10.webp)



**Người ký tên 2:**



Người ký 2 quét mã QR được người ký 1 cung cấp. Sau đó nhập "MẬT KHẨU TELEPORT" được truyền qua kênh truyền thông thứ cấp để giải mã dữ liệu đã truyền.



Người ký 2 ký giao dịch và sau đó nhấp vào **"T "** để truyền PSBT cho người ký 3 thông qua "Key Teleport".


Rõ ràng, 2 chữ ký đã được áp dụng. Chỉ còn thiếu chữ ký của người ký số 3 để giao dịch có hiệu lực. Chọn người ký số 3 bằng cách nhấp vào **"ENTER "**.



![CCQ-key-teleport](assets/fr/11.webp)



Và một "MẬT KHẨU TELEPORT" mới được tạo ra, tiếp theo là mã QR mã hóa PSBT được ký bởi 1 và 2, sau đó được mã hóa bằng "MẬT KHẨU TELEPORT" mới này (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Người ký tên thứ 3:**



Lặp lại các bước tương tự như trên.


Người ký 3 quét mã QR được người ký 2 cung cấp. Sau đó nhập "MẬT KHẨU TELEPORT" được truyền qua kênh truyền thông phụ.



Người ký số 3 ký vào giao dịch và lần này, vì 3 trong số 4 chữ ký đã được áp dụng nên giao dịch được chỉ định là đã hoàn tất và sẵn sàng để phân phối qua nhiều phương tiện khác nhau (Thẻ SD, NFC, QR, v.v.).



![CCQ-key-teleport](assets/fr/13.webp)



Nếu tính năng "Đẩy giao dịch" của ColdCardQ được kích hoạt, bạn chỉ cần dán ColdCardQ vào mặt sau của bất kỳ thiết bị nào được kết nối Internet hỗ trợ NFC (điện thoại thông minh/máy tính bảng) để phát giao dịch qua mạng Bitcoin.



![CCQ-key-teleport](assets/fr/14.webp)



*Đối với việc chuyển giao PSBT từ bên ký kết này sang bên ký kết khác, "Dịch chuyển Khóa" chỉ đơn giản được sử dụng thông qua "Mật khẩu Dịch chuyển" ở mỗi giai đoạn, giúp mã hóa PSBT khi nó được chuyển từ bên ký kết này sang bên ký kết khác. Vì dữ liệu được truyền đi không thể bị sử dụng để đánh cắp tiền, nên không cần sử dụng Diffie-Hellman như khi gửi các thông tin mật (seed, mật khẩu, v.v.)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Nguồn: [Trang web chính thức của ColdCard](https://coldcard.com/)*