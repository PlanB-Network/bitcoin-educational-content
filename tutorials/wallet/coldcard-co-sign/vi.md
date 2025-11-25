---
name: COLDCARD - Đồng ký
description: Khám phá tính năng Đồng ký và sử dụng trên COLDCARD của bạn
---

![cover](assets/cover.webp)


*Lưu ý: Hướng dẫn này dành cho những người đã có kinh nghiệm sử dụng ví đa chữ ký, thiết bị Coinkite và phần mềm như Sparrow wallet hoặc Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Tại sao nên ký chung với ColdCard?



Tính năng này cho phép bạn thêm **điều kiện chi tiêu** vào thiết bị ColdCard (Q hoặc Mk4) của mình theo cách của Mô-đun bảo mật phần cứng (HSM) để bảo vệ tiền của bạn trong khi vẫn duy trì tính linh hoạt và khả năng kiểm soát đáng kể đối với tiền.



Điều kiện chi tiêu có thể là:





- Giới hạn về quy mô**: giới hạn số lượng bitcoin bạn có thể chi tiêu trong một giao dịch duy nhất.
- Giới hạn tốc độ:** quyết định số lượng giao dịch bạn có thể thực hiện trên một đơn vị thời gian (mỗi giờ, mỗi ngày, mỗi tuần, v.v.), yêu cầu số khối tối thiểu giữa các giao dịch.
- Địa chỉ được chấp thuận trước:** Chỉ cho phép gửi bitcoin đến các địa chỉ được chấp thuận trước.
- Xác thực hai yếu tố:** Yêu cầu xác nhận từ ứng dụng di động 2FA của bên thứ ba (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) trên điện thoại thông minh/máy tính bảng hỗ trợ NFC và có kết nối internet.



**Cách thức hoạt động



Bằng cách thêm seed thứ hai vào thiết bị ColdCard Mk4 hoặc Q của bạn, được gọi là "Khóa chính sách chi tiêu", mà chúng tôi sẽ gọi trong suốt hướng dẫn này là "Khóa C".


Ngoài seed bổ sung này, bạn sẽ được yêu cầu Supply thêm ít nhất một khóa bổ sung (XPUB), mà chúng tôi sẽ gọi là "Khóa dự phòng", để tạo Wallet Multisig 2-on-N.



Tóm lại, chúng ta sẽ tạo Wallet Multisig và thiết bị ColdCard của bạn sẽ chứa 2 khóa riêng cần thiết để chi tiêu tiền, khóa chính seed của thiết bị và "Khóa chính sách chi tiêu".



Mỗi lần yêu cầu "Khóa C" ký, các điều kiện chi tiêu đã chỉ định sẽ được áp dụng và ColdCard sẽ chỉ ký nếu giao dịch tuân thủ các điều kiện đó.



Nếu bạn muốn bỏ qua những điều kiện chi tiêu này, bạn có thể thực hiện như sau:




- bằng cách ký bằng một trong các chìa khóa dự phòng và tay seed, hoặc 2 chìa khóa dự phòng tùy thuộc vào kích thước Multisig của bạn.
- bằng cách nhập "Khóa Chính sách Chi tiêu" hoặc "Khóa C" vào menu "Đồng ký". **Không thể xem trực tiếp khóa sau trên thiết bị, nếu không, bất kỳ ai cũng có thể hủy các điều kiện chi tiêu đã thiết lập.**




## Cấu hình đồng ký ColdCard



![video](https://youtu.be/MjMPDUWWegw)



### 1- Kích hoạt chức năng



Trước hết, hãy đảm bảo thiết bị của bạn có ít nhất phiên bản phần mềm mới nhất:




- Mk4: v5.4.2
- Hỏi: v1.3.2Q




Trên Mk4 hoặc ColdCardQ, hãy vào *Công cụ nâng cao > Đồng ký ColdCard*.



![Co-Sign](assets/fr/01.webp)



*Trong hướng dẫn sau, ảnh chụp màn hình sẽ được chụp trên ColdCardQ để thuận tiện, nhưng các bước và menu là giống hệt nhau giữa Mk4 và Q.*



Tóm tắt chức năng sẽ được hiển thị.


Thuật ngữ được sử dụng để chỉ định các khóa, mà chúng ta sẽ sử dụng lại trong Wallet đa chữ ký 2-on-3 mà chúng ta sắp tạo ra, là:



Phím A = Coldcard master seed


Khóa B = Khóa dự phòng


Chìa khóa C = Chìa khóa chính sách chi tiêu



Nhấp vào **"ENTER "**.



![Co-Sign](assets/fr/02.webp)



Bước tiếp theo là quyết định khóa riêng nào sẽ đóng vai trò là "Khóa chính sách chi tiêu" hoặc "Khóa C".



Chúng ta có thể thấy rằng có một số lựa chọn mở ra cho chúng ta:





- Hoặc nhấn **"ENTER "** để generate tạo một câu seed mới gồm 12 từ.





- Nhấp vào **"(1) "** để nhập seed 12 từ hiện có hoặc chọn **"(2) "** để nhập seed 24 từ hiện có.





- Hoặc nhấn **"(6) "** để nhập seed từ kho lưu trữ của thiết bị.



Đối với mục đích của hướng dẫn này, chúng tôi quyết định nhập seed 12 từ hiện có bằng cách nhấn **"(1) "**. Đây có thể là bất kỳ seed BIP39 nào mà bạn đã sở hữu và rõ ràng là bạn có bản sao lưu.



Sử dụng bàn phím để nhập 12 từ trong seed. Trong ví dụ này, chúng ta sẽ chọn cụm từ hợp lệ của seed là "thịt bò" x 12. Sau đó nhấn **"ENTER"**.


*Lưu ý: nếu bạn không có bản sao lưu của seed này, bạn sẽ không thể sửa đổi cài đặt "Đồng ký" trên thiết bị của mình để thay đổi điều kiện chi tiêu*



Tính năng "Đồng ký" hiện đã được kích hoạt trên thiết bị. Tiếp theo, chúng ta cần chọn điều kiện chi tiêu, sau đó hoàn tất việc tạo Wallet đa chữ ký.



![Co-Sign](assets/fr/03.webp)



### 2- Chọn điều kiện chi tiêu hoặc "*chính sách chi tiêu*"



Tại đây, chúng tôi chỉ định các điều kiện chi tiêu phải đáp ứng khi **"Phím C "** hoặc **"Phím chính sách chi tiêu**" ký giao dịch.



Trong menu **"Đồng ký"**, hãy nhấp vào **"Chính sách chi tiêu**".



Sau đó, bạn có thể chọn mức tối đa, tức là số satoshi tối đa có thể chi tiêu trong một giao dịch duy nhất.



Trong ví dụ này, chúng ta sẽ chọn độ lớn tối đa là **21212** satoshi. Nhấp vào **"ENTER"** để xác nhận.




![Co-Sign](assets/fr/04.webp)



Sau đó, chúng ta chọn đặt tốc độ tối đa, tức là số lượng giao dịch mà thiết bị có thể ký trên một đơn vị thời gian. Trong hướng dẫn này, chúng ta sẽ chọn tốc độ không giới hạn, tức là không giới hạn số lượng giao dịch.




![Co-Sign](assets/fr/05.webp)



### 3- Tạo Wallet Multisig 2-on-N



Chúng ta vẫn cần chọn khóa thứ ba cho Wallet Multisig, tức là **"Khóa dự phòng"** (Khóa B), ngoài **khóa chính seed** của thiết bị (Khóa A) và **"Khóa chính sách chi tiêu"** (Khóa C).



"B Key" của chúng ta sẽ phải được nhập qua thẻ SD hoặc qua mã QR trong trường hợp của ColdCardQ.


Để thực hiện điều này, chúng ta sẽ cần một thiết bị ColdCard Mk4 hoặc Q thứ hai, trên đó sử dụng "Phím B".



Trên thiết bị thứ hai chứa **"Khóa sao lưu"** của bạn, ví dụ như ColdCard Mk4, hãy vào từ menu chính đến **"Cài đặt"**, sau đó là **"Multisig Wallet"**, và cuối cùng là **"Xuất Xpub"**.


(Tất nhiên, nếu thiết bị thứ hai của bạn là ColdCardQ, bạn sẽ có tùy chọn xuất Xpub qua mã QR).





![Co-Sign](assets/fr/06.webp)





Ở màn hình tiếp theo, hãy lắp thẻ SD và nhấp vào nút **"xác thực"** ở góc dưới bên phải. Sau đó, nhấp vào **"(1) "** để lưu tệp vào thẻ SD.



Tệp sẽ chứa dấu vân tay khóa công khai (*dấu vân tay*) trong tên của nó và sẽ có dạng `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Sau đó, lắp thẻ SD vào ColdCardQ "ban đầu" để nhập "Khóa sao lưu" (khóa B).


Trong menu "ColdCard Co-Signing", chọn "Build 2-of-N", sau đó trên màn hình tiếp theo, nhấp vào **"ENTER "**, sau đó nhấp lại **"ENTER "** để nhập "Khóa sao lưu" từ thẻ SD.



![Co-Sign](assets/fr/08.webp)



Trên màn hình tiếp theo, hãy để trống mục "Số tài khoản" (trừ khi bạn biết chính xác mình đang làm gì) và nhấp vào **"ENTER "** một lần nữa.



![Co-Sign](assets/fr/09.webp)



Cuối cùng, chúng ta đã sẵn sàng sử dụng Wallet Multisig 2-sur-3 mới của mình, được cấu tạo như sau:



Phím A= Coldcard Q master seed


Khóa B = Khóa dự phòng (vừa được nhập từ thiết bị Coldcard thứ hai)


Khóa C = Khóa chính sách chi tiêu (nếu dùng để ký, áp đặt các điều kiện chi tiêu được xác định trước)



## Đồng ký với Sparrow wallet



Nếu cần, hãy tham khảo hướng dẫn bên dưới để làm quen với phần mềm Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Xuất Wallet Multisig 2-sur-3 sang Sparrow wallet



Bây giờ chúng ta cần xuất Wallet Multisig sang Sparrow để có thể đặt những satoshi đầu tiên vào đó.



Từ menu chính của ColdCardQ, chọn **"Cài đặt"**, sau đó chọn **"Ví Multisig"**.


Bộ ví Multisig mà ColdCard của bạn biết hiện được hiển thị, với số lượng khóa liên quan ở đây là "2/3" (2-sur3). Chọn Multisig **"ColdCard Co-Sign"** mà chúng ta vừa tạo, sau đó nhấp vào **"ColdCard Export"**.



![Co-Sign](assets/fr/10.webp)




Cuối cùng, hãy chọn phương pháp cho phép bạn xuất Wallet sang Sparrow. Trong trường hợp này, chúng tôi sẽ chọn thẻ SD, sau đó nhấp vào **"(1) "** sau khi lắp thẻ SD vào khe A của thiết bị.



![Co-Sign](assets/fr/11.webp)



Sau đó trong Sparrow wallet, chọn "Nhập Wallet".



![Co-Sign](assets/fr/12.webp)



Sau đó nhấp vào **"Nhập tệp"**. Sau đó chọn tệp **"export-Coldcard_Co-sign.txt"** trên thẻ SD của bạn.



![Co-Sign](assets/fr/13.webp)



Đặt tên cho Wallet theo tên hiển thị trong Sparrow và chọn mật khẩu để mã hóa Wallet (hoặc không).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Bây giờ chúng ta đã sẵn sàng nhận những satoshi đầu tiên và thử nghiệm các điều kiện chi tiêu mà chúng tôi đã áp dụng cho Wallet.



![Co-Sign](assets/fr/16.webp)



### 2- Kiểm tra các chính sách chi tiêu được xác định trước



Xin nhắc lại, chúng tôi đã quyết định giá trị tối đa cho Wallet Multisig là 21212 satoshi. Điều này có nghĩa là mỗi khi Khóa Chính sách Chi tiêu (Khóa C) ký một giao dịch, giao dịch sau sẽ chỉ hợp lệ nếu số tiền chi tiêu nhỏ hơn hoặc bằng 21212 satoshi.



Chúng ta hãy thử nghiệm nhé.


Đầu tiên, hãy nhấp vào tab "Nhận" trong Sparrow và thả một vài Satss vào Wallet, chúng ta sẽ sử dụng trong suốt hướng dẫn này.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Sau đó, chúng ta hãy thử chi tiêu nhiều hơn số satoshi được phép là 21.212 bằng cách mô phỏng giao dịch 50.000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Sau khi quét mã QR đại diện cho giao dịch *chưa ký* bằng ColdCardQ để nhập giao dịch, màn hình sẽ hiển thị như sau. Một thông báo cảnh báo cho biết các điều kiện chi tiêu chưa được đáp ứng. Nếu chúng tôi vẫn ký giao dịch, thì chỉ một trong hai khóa (khóa chính seed trên thiết bị, chứ không phải "Khóa C") được ký.




![Co-Sign](assets/fr/23.webp)



Ở đây, sau khi nhập giao dịch vào Sparrow, chúng ta có thể thấy rằng chỉ có một chữ ký được áp dụng cho giao dịch.



![Co-Sign](assets/fr/24.webp)




Bây giờ chúng ta hãy lặp lại thử nghiệm, nhưng đối với giao dịch 21.000 satoshi, tức là nhỏ hơn mức tối đa (21212 Sats) mà chúng ta đặt cho Wallet này.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Hãy thử ký giao dịch này bằng ColdCardQ của chúng tôi.



Lần này không có vấn đề gì, không có thông báo cảnh báo nào xuất hiện và khi chúng tôi nhập giao dịch đã ký vào Sparrow wallet, lần này 2 chữ ký đã được áp dụng, khiến giao dịch trở nên hợp lệ và sẵn sàng để phân phối.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Đồng ký với Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA & Địa chỉ được liệt kê trắng



Trong đoạn này, chúng ta sẽ sử dụng Wallet Multisig Co-Sign với Nunchuk và tận dụng cơ hội này để áp dụng các điều kiện chi tiêu mới để xem mọi việc diễn ra như thế nào.



Vào *Công cụ nâng cao > Đồng ký ColdCard*.


Chúng tôi được yêu cầu nhập "Mã Chính sách Chi tiêu" để truy cập menu cho phép chúng tôi thay đổi điều kiện chi tiêu. Trong trường hợp này, chúng tôi nhập 12 x "thịt bò".



Chúng tôi quyết định giữ nguyên độ lớn 21212 Sats và "Tốc độ Giới hạn" tối đa vì những lý do thực tế liên quan đến hướng dẫn này. Mặt khác, chúng tôi sẽ sử dụng menu **"Danh sách Địa chỉ Trắng"** để áp đặt các địa chỉ mà tiền của chúng tôi có thể được chi tiêu.




![Co-Sign](assets/fr/31.webp)




Quét mã QR liên quan đến các địa chỉ (chúng tôi sẽ chọn 2) mà bạn muốn thêm vào danh sách trắng, sau đó nhấp vào **"ENTER "**. Sau khi xác thực địa chỉ của bạn bằng cách nhấn **"ENTER "** liên tiếp, chúng tôi thấy rằng giới hạn về Quy mô và địa chỉ người thụ hưởng đã được áp dụng.



![Co-Sign](assets/fr/32.webp)



Cuối cùng, để có được bức tranh toàn cảnh về những khả năng mà "Co-Sign" mang lại, hãy kích hoạt tùy chọn "Web 2FA".


Tính năng này cho phép bạn sử dụng ứng dụng tuân thủ TOTP RFC-6238 như Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / hoặc Aegis Authenticator để tăng cường bảo mật Layer.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Cụ thể, trước khi ký giao dịch, bạn cần đưa thiết bị hỗ trợ NFC và kết nối internet đến gần Coldcard. Thao tác này sẽ tự động đưa bạn đến trang web coldcard.com, nơi bạn sẽ được yêu cầu nhập mã 6 chữ số cho ứng dụng của mình. Nếu bạn nhập đúng mã, trang web sẽ hiển thị mã QR để quét ColdCardQ hoặc mã 8 chữ số để nhập vào thẻ Mk4 của bạn, nhằm cho phép thiết bị ký.





![Co-Sign](assets/fr/33.webp)



Sau khi quét mã QR hiển thị trong ứng dụng xác thực kép và thêm tài khoản ColdCard Co-Sign (CCC), bạn sẽ được yêu cầu xác minh mọi thứ đều ổn bằng cách nhập mã 2FA.



Nhập ColdCard vào mặt sau của thiết bị NFC.



![Co-Sign](assets/fr/34.webp)



Trên trang web mở ra, hãy nhập mã 2FA của ứng dụng bạn yêu thích. Sau đó, quét mã QR hiển thị bằng ColdCardQ (hoặc nhập mã 8 chữ số hiển thị trên thẻ Mk4).



![Co-Sign](assets/fr/35.webp)




Hiện tại chúng tôi đã áp dụng giới hạn về độ lớn (21212 Sats), địa chỉ đích và xác thực kép.



![Co-Sign](assets/fr/36.webp)



### 2- Xuất Wallet Multisig 2-on-3 sang Nunchuk



Lần này chúng ta hãy xuất Wallet Multisig 2-on-3 vào Nunchuk, giống như chúng ta đã làm với Sparrow trước đó.


Vào *Cài đặt > Ví Multisig > 2/3: Đồng ký ColdCard > Xuất ColdCard*.



![Co-Sign](assets/fr/10.webp)



Lần này hãy chọn tùy chọn NFC để xuất bằng cách nhấp vào nút ColdcardQ có cùng tên **"NFC "**.



![Co-Sign](assets/fr/37.webp)



Trong Nunchuk, nếu bạn mở ứng dụng lần đầu tiên, hãy nhấp vào **"Khôi phục Wallet hiện có"**.



![Co-Sign](assets/fr/38.webp)



Nếu bạn đã có Wallet trong ứng dụng, hãy nhấp vào **"+"** ở trên cùng bên phải, sau đó nhấp vào **"Khôi phục Wallet hiện có"**.



![Co-Sign](assets/fr/39.webp)




Sau đó chọn **"Khôi phục Wallet từ COLDCARD"** rồi chọn **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Cuối cùng, chạm mặt sau của điện thoại thông minh vào màn hình ColdCardQ để nhập Wallet qua NFC.



![Co-Sign](assets/fr/41.webp)



Tài khoản của chúng tôi và số satoshi đã gửi trước đó qua Sparrow wallet đã trở lại.



![Co-Sign](assets/fr/42.webp)



### 3- Kiểm tra các chính sách chi tiêu được xác định trước



Bây giờ, hãy thử thực hiện một giao dịch vi phạm 2 điều kiện chi tiêu đã đặt ra. **Chúng ta sẽ thử chi nhiều hơn 21212 Sats cho một Address chưa được chấp thuận.** Hãy thử gửi 2222 Sats cho một Address ngẫu nhiên.



![Co-Sign](assets/fr/43.webp)



Sau khi giao dịch được tạo, hãy nhấp vào 3 dấu chấm nhỏ ở góc trên bên phải để xuất giao dịch đó sang ColdCard của bạn.



![Co-Sign](assets/fr/44.webp)



Sau đó chọn **"Xuất qua BBQR"** và quét mã QR hiển thị bằng ColdCardQ của bạn.



![Co-Sign](assets/fr/45.webp)



Sau đó, ColdcardQ của bạn sẽ hiển thị cảnh báo, khi bạn cuộn xuống cuối màn hình, cảnh báo sẽ làm rõ rằng giao dịch vi phạm các điều kiện chi tiêu như mong đợi.



**Lưu ý rằng thiết bị không cho chúng tôi biết các điều kiện chi tiêu liên quan để ngăn chặn kẻ tấn công tiềm năng cố gắng lách luật.**




![Co-Sign](assets/fr/46.webp)



Nếu bạn vẫn xác thực bằng cách nhấn **"ENTER"**, mã QR đại diện cho giao dịch đã ký sẽ xuất hiện. Nếu bạn nhập mã QR này vào Nunchuk, bạn sẽ thấy chỉ có một chữ ký được áp dụng.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Chúng ta hãy thực hiện chính xác thao tác tương tự, nhưng lần này là giao dịch tuân thủ giới hạn độ lớn (21212 Sats) và chi satoshi vào một trong 2 địa chỉ mà chúng ta đã cấu hình trước.



Chúng tôi gửi Nunchuk 12121 Sats đến một trong 2 địa chỉ của chúng tôi. Sau đó, chúng tôi xuất giao dịch sang ColdCard như đã làm trước đó.



![Co-Sign](assets/fr/49.webp)




Sau khi nhập giao dịch chưa ký vào ColdCardQ, hãy xem lần này chúng ta sẽ thấy gì.



Luôn có cảnh báo, nhưng lần này, khi cuộn xuống cuối màn hình, chúng tôi thấy rằng cần xác thực giao dịch qua 2FA. Thiết bị yêu cầu chúng tôi đưa ColdcardQ lại gần thiết bị đầu cuối NFC được kết nối Internet (điện thoại thông minh hoặc máy tính bảng), và chúng tôi đã làm theo.



![Co-Sign](assets/fr/50.webp)



Một trang web mở ra trên điện thoại thông minh của chúng tôi, yêu cầu chúng tôi nhập mã 2FA và chúng tôi thực hiện được điều này nhờ Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





Sau đó quét mã QR xuất hiện trên trang web để cho phép ColdCard của bạn ký giao dịch.


Giao dịch hiện được ký bằng 2 khóa và do đó có hiệu lực.



Nếu tính năng "Đẩy giao dịch" được bật trên ColdCardQ, bạn có thể truyền giao dịch trực tiếp đến mạng chỉ bằng một cú chạm đơn giản vào mặt sau của điện thoại thông minh.



![Co-Sign](assets/fr/52.webp)




Nếu bạn không kích hoạt "Đẩy giao dịch", hãy nhấn nút "QR" trên ColdCardQ để hiển thị giao dịch đã ký dưới dạng mã QR và nhập giao dịch đó vào Nunchuk theo cách tương tự như trong ví dụ trước.



![Co-Sign](assets/fr/53.webp)



Lần này chúng tôi nhận thấy rằng 2 chữ ký đã được áp dụng, do đó giao dịch đã sẵn sàng để phát trên mạng Bitcoin.



![Co-Sign](assets/fr/54.webp)




Chúng ta đã đến phần cuối của hướng dẫn này, hướng dẫn này sẽ cung cấp cho bạn cái nhìn tổng quan về các khả năng mà chức năng Co-Sign tích hợp vào các thiết bị ColdCardQ và Mk4 của Coinkite mang lại, cũng như cách sử dụng chức năng này thông qua các ví như Sparrow và Nunchuk.