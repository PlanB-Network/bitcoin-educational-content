---
name: Coin Control
description: Làm quen với Coin Control, một công cụ quan trọng để bảo vệ quyền riêng tư của bạn trên Bitcoin
---
![cover](assets/cover.webp)


*Hướng dẫn này được nhập từ [một bài học của Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Giới thiệu



Tính vững chắc của giao thức Bitcoin được đảm bảo bởi những khái niệm cơ bản đơn giản. Trong số đó, tính minh bạch nổi bật: tất cả các giao dịch Bitcoin đều công khai và dễ dàng được bất kỳ ai xác minh. Mặc dù đặc điểm này là một cột mốc quan trọng của giao thức, vì nó ngăn chặn gian lận và đảm bảo tính xác thực của quỹ, nhưng nó cũng có thể là một thách thức đối với tính bảo mật. **Bạn đã bao giờ tự hỏi liệu sự minh bạch như vậy có thể làm suy giảm quyền riêng tư của mình không?**



Bạn nên làm vậy. Mặc dù việc tích lũy Satoshi không cần KYC khá dễ dàng, nhưng quyền riêng tư của bạn lại gặp rủi ro cao nhất ngay từ giai đoạn chi tiêu.



### Điều gì xảy ra khi bạn dành một UTXO



Việc chi tiêu Bitcoin không chỉ đơn thuần là chuyển giao giá trị cho người khác.



Bằng cách sử dụng một trong các UTXO của bạn, trên thực tế bạn phải đáp ứng các điều kiện áp dụng cho tính minh bạch của giao thức, vì bạn có nghĩa vụ chứng minh rằng bạn sở hữu số tiền đó. Do đó, bạn tự chịu trách nhiệm về:




- tiết lộ khóa công khai của bạn;
- tạo chữ ký số.



Do đó, thời điểm chi tiêu là quan trọng nhất: **chi tiêu Bitcoin là hành động cần được thực hiện một cách có ý thức và kiểm soát càng nhiều càng tốt**.



## Kiểm soát Coin



Trong giao thức Bitcoin, các mục như _tài khoản_ hoặc _đơn vị tiền tệ_ không tồn tại. Khái niệm về UTXO được giải thích rất hay trong khóa học sau, mà tôi thực sự khuyên bạn nên tham gia:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Với Bitcoin, những gì bạn tích lũy và chi tiêu sau này là các đơn vị tài khoản lớn hoặc nhỏ được đo bằng Satoshi, được biểu thị bằng `đầu ra giao dịch chưa sử dụng`, **UTXO**, còn được gọi là `coin`. Khi bạn sử dụng UTXO để tạo giao dịch, chúng sẽ bị hủy hoàn toàn và các UTXO khác sẽ được tạo ra thay thế.



Ví phần mềm được phát triển để tự động thực hiện lựa chọn này, sử dụng các đồng tiền được chọn "ngẫu nhiên", áp dụng một số thuật toán nhất định do giao thức cung cấp. Tiêu chí duy nhất mà các thuật toán này đáp ứng là trang trải số tiền cần thiết cho việc chi tiêu.



Họ có thể kết hợp các UTXO có độ tuổi khác nhau, hoặc ưu tiên sử dụng UTXO mới nhất hoặc "cũ nhất", tùy thuộc vào thuật toán do nhà phát triển lựa chọn. Các ví phần mềm tốt nhất cũng có kế hoạch để người dùng tự đưa ra lựa chọn quan trọng.



Sổ tay hướng dẫn `Coin Control`, còn được gọi là `Coin Selection`, là một tính năng của một số Ví phần mềm cho phép bạn **chọn thủ công UTXO để chi tiêu khi bạn thực hiện giao dịch**.



Giả sử chúng ta có Wallet với 3 UTXO lần lượt là 21.000, 42.000 và 63.000 Satoshi.



![img](assets/en/01.webp)



Nếu bạn phải chi 24.000 Sats và để thuật toán tự động lựa chọn, một Software Wallet giỏi có thể chọn kết hợp UTXO 1 + UTXO 2 để trả 24 nghìn phí Sats và Miner, tạo ra phần còn lại quay trở lại Address nội bộ của Wallet ban đầu.



![img](assets/en/02.webp)



Sau giao dịch, tình hình mới trong Wallet, chỉ tính UTXO, có thể được tóm tắt như sau.



![img](assets/en/03.webp)



Tuy nhiên, với phần mềm phù hợp và nhận thức của bạn, bạn có thể đã đưa ra một lựa chọn khác, theo một số cách chính xác hơn. Ví dụ, bằng cách chỉ chọn UTXO2 (từ 42.000 Sats).



![img](assets/en/04.webp)



Với tình huống kết thúc ở Wallet của bạn, ở mức UTXO, trông có vẻ khác so với trước.



![img](assets/en/05.webp)



## Tại sao coin control thủ công?



![img](assets/en/06.webp)



Trong hai ví dụ trên, số dư thực tế là `108.280 Sats`. Sau khi chi 24.000 Sats, nếu không chọn thủ công, chúng ta sẽ có 2 UTXO trong Wallet; nếu điều khiển thủ công Coin, chúng ta có tổng cộng 3.



Câu hỏi mà chúng ta có thể tự đặt ra là: **tại sao phải làm tất cả những điều này?** Có, hoặc có thể có, nhiều lý do tại sao chúng ta không sử dụng `UTXO1` **và tất cả đều là cơ sở cho việc tại sao—khi chi tiêu—kích hoạt coin control thủ công là một trong những thực hành tốt cần tuân theo**.



Việc lựa chọn UTXO cho phép bạn ưu tiên một số khía cạnh hơn những khía cạnh khác. Sự lựa chọn thực sự phụ thuộc vào mục tiêu bạn muốn đạt được.



### Sự riêng tư



Một trong những lợi thế chính khi nói đến việc kiểm soát Coin thủ công là **quyền riêng tư cao hơn cho người chi tiêu**. Hãy luôn lấy ví dụ này: việc chi 24.000 Satoshi _mà không cần lựa chọn Coin thủ công_. Vì Blockchain của Bitcoin là một hồ sơ công khai, một người quan sát bên ngoài có thể tuyên bố, không chút nghi ngờ, rằng các đầu vào `UTXO1 của 21.000 Sats` và `UTXO2 của 42.000 Sats`, cũng như phần còn lại, `UTXO5 của 38.280 Sats` **cả ba đều thuộc về cùng một người dùng**.



Mặt khác, khi chọn thủ công `UTXO2`, `UTXO1` vẫn được giữ nguyên hoàn toàn, nằm trong bộ UTXO và chờ được sử dụng vào thời điểm thích hợp hơn.



`UTXO1` có thể đến từ nguồn KYC, chẳng hạn như khoản thanh toán nhận được trong Exchange cho hàng hóa và dịch vụ, trong khi các UTXO khác thì không. Việc kết hợp UTXO-kyc với các mã khác có tính bảo mật cao hơn sẽ làm giảm tính ẩn danh của các quỹ không phải KYC.



**Các quỹ KYC sẽ tất yếu dẫn đến việc truy ra danh tính của người thanh toán. Nếu đó là ví của bạn, bạn có muốn một người quan sát bên ngoài có thể truy ra danh tính của bạn với sự chắc chắn tuyệt đối như vậy không?**



Sau đó, hãy thử xem xét rằng Ví thực hiện lựa chọn thủ công các UTXO, chẳng hạn, cho phép **phân tách một hoặc nhiều UTXO**, một chức năng được sử dụng khi những tình huống như vậy phát sinh.



Mặc dù tôi tin rằng tiền KYC nên được giữ trong Wallet riêng biệt so với Bitcoin được mua mà không cần KYC, nhưng nếu bạn gặp trường hợp này thì việc tách biệt một số địa chỉ của bạn là một trợ giúp quan trọng mà bạn có thể tận dụng bằng cách học cách tự tay chọn đầu vào chi tiêu.



### Tiết kiệm học phí



Việc chọn đúng UTXO để thực hiện chi tiêu **cho phép tối ưu hóa phí**. Một lần nữa, bắt đầu từ ví dụ ban đầu, Software Wallet đã chọn hai UTXO để chi trả cho chi phí cần thực hiện. Hai UTXO ngụ ý hai chữ ký sẽ được hiển thị cho mạng. Do đó, giao dịch có "trọng số" lớn hơn tính theo vByte.



Mặt khác, khi sử dụng bộ điều khiển thủ công Coin, bạn chỉ có thể chọn một giao dịch đủ để thanh toán số tiền, tiết kiệm phí bằng cách giảm "trọng số" của giao dịch.



Vào thời điểm phí cao nhưng bạn buộc phải chi Bitcoin On-Chain (ví dụ: để mở kênh Lightning Network), thì đó chính là lúc biện pháp kiểm soát Coin trở thành động lực kinh tế đúng đắn cần hướng tới.



### Tập hợp các di vật



Khi bạn thanh toán và sử dụng Bitcoin On-Chain, khả năng nhận được tiền thừa gần như luôn là điều chắc chắn. Mỗi khoản tiền còn lại tự thân nó đã là một mất mát nhỏ về quyền riêng tư, vì nó tiết lộ cho mạng lưới (và đặc biệt là cho người nhận thanh toán) một Address của bạn có thể được liên kết với đầu vào nguồn của bạn.



Khi xét đến các địa chỉ đặc biệt Wallet HDs generate tốt nhất dành cho các phần còn lại, bạn có thể dễ dàng nhận ra chúng và "phân loại" tất cả các phần còn lại của các giao dịch khác nhau đã thực hiện; khi chúng đạt đến một số lượng nhất định, bạn có thể chọn chúng theo cách thủ công và hợp nhất chúng hoặc chuyển sang Lightning Network (phương pháp tôi thích) và xử lý chúng để lấy lại quyền riêng tư bị mất khi chi tiêu.



### Chi phí từ Cold Wallet



Cold Wallet là một công cụ giúp bạn có được mức độ an toàn hợp lý, để lưu trữ bất kỳ khoản tiền nào để dành trong thời gian dài. Tuy nhiên, những sự cố bất ngờ có thể xảy ra, vì vậy cần phải có khoản tiết kiệm và ứng phó với một số chi phí bất ngờ.



Tôi không biết có bao nhiêu người có thể chia sẻ cách tiếp cận của tôi, nhưng lời khuyên của tôi là **đừng bao giờ chi tiêu trực tiếp từ Cold Wallet, để tránh nhận tiền thừa giữa các địa chỉ của cùng một địa chỉ**. Hãy học cách chọn thủ công các UTXO cần thiết để chi trả chi phí, chuyển chúng sang Wallet Hot và chuẩn bị giao dịch từ địa chỉ này. Sau đó, bất kỳ khoản tiền thừa nào, bạn có thể gửi lại cho Cold Wallet Address (nếu số tiền đủ), sử dụng cho các chi phí khác, hoặc vẫn tách riêng như chúng ta vừa thấy.



## Trình bày thực tế


Sau phần giới thiệu kỹ thuật về `tại sao`, chúng ta hãy cùng xem cách áp dụng điều khiển thủ công Coin vào thực tế với các phần mềm khác nhau, máy tính để bàn và thiết bị di động. Chúng tôi sẽ luôn sử dụng cùng một Wallet BIP39, được nhập vào từng công cụ đã chọn, để cho bạn thấy những khác biệt nhỏ giữa chúng.



## Máy tính để bàn Wallet



### Sparrow



Nếu bạn sử dụng Sparrow, hãy mở Wallet và chọn _UTXOs_ từ menu bên trái. Bạn sẽ thấy danh sách tất cả các UTXO được liên kết với Wallet của mình.



Chỉ cần nhấp chuột vào một trong số chúng và chọn _Gửi mục đã chọn_. Sparrow cũng hiển thị tổng số tiền có thể chi tiêu sau khi chọn, ngay bên cạnh lệnh. Về mặt đồ họa, Sparrow hiển thị UTXO đã chọn bằng cách tô sáng màu xanh lam.



![img](assets/en/07.webp)



Bạn cũng có thể chọn nhiều hơn một. Hãy tự mình sử dụng phím _CTRL_ để chọn các UTXO không liền kề trong danh sách.



![img](assets/en/08.webp)



Sau khi chọn UTXO theo cách thủ công, bạn có thể bắt đầu xây dựng giao dịch và Sparrow sẽ hiển thị rõ ràng cách thức cấu thành giao dịch bằng đồ họa.



![img](assets/en/09.webp)



#### Phân tách UTXO



Phân tách tiền nghĩa là "khóa" chúng trong Wallet để chúng không thể được sử dụng làm dữ liệu đầu vào cho giao dịch. Sparrow cho phép chức năng này, luôn được truy cập từ menu _UTXOs_: bạn di chuột lên UTXO cần "khóa" và nhấp chuột phải. Trong số các tính năng của quy trình này sẽ xuất hiện _Freeze UTXO_. Đây là cách bạn có thể phân tách Coin với ví Sparrow.



![img](assets/en/29.webp)



### Điện



Nếu máy tính để bàn Wallet của bạn là Electrum, bạn nên biết rằng bạn có thể chọn thủ công UTXO từ menu _Addresses_ hoặc từ menu _Coins_. Trong cả hai menu, việc chọn được thực hiện bằng cách trỏ chuột vào UTXO mong muốn và chọn _Add to Coin control_ sau khi nhấp chuột phải.



![img](assets/en/10.webp)



Ngay cả với phần mềm này, bạn vẫn có thể chọn nhiều hơn một UTXO bằng cách sử dụng phím _CTRL_ trên bàn phím nếu chúng không nằm cạnh nhau.



![img](assets/en/11.webp)



Về mặt đồ họa, Electrum sẽ hiển thị cho bạn lựa chọn bằng cách làm nổi bật các UTXO đã chọn trong Green, trong khi một thanh xuất hiện ở phía dưới, được làm nổi bật bằng cùng màu, cho thấy số dư khả dụng sau khi điều khiển Coin.



![img](assets/en/12.webp)



Sau khi đã chọn đầu ra hoặc các đầu ra, bạn có thể xây dựng giao dịch của mình như thường lệ từ menu _Gửi_.



#### Phân tách UTXO



Electrum cung cấp chức năng này bằng cách vào menu _Coins_, nơi bạn sẽ chọn một UTXO cụ thể và sau đó chọn _Freeze_ bằng cách nhấp chuột phải. Bạn có thể "đóng băng" Address ngay cả khi không có tiền trong menu _Addresses_, hoặc "Coin" để không tiêu tiền.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk cho phép bạn chọn thủ công UTXO từ menu chính sau khi mở. Khởi chạy Nunchuk và nhấp vào _Xem tiền_.



![img](assets/en/13.webp)



Thao tác này sẽ mở cửa sổ chứa tất cả các UTXO trong Wallet của bạn, nơi bạn có thể chọn một hoặc nhiều UTXO bằng cách đánh dấu vào ô bên cạnh mỗi số tiền. Sau khi chọn xong, hãy tiếp tục với _Tạo giao dịch_.



![img](assets/en/14.webp)



Sau đó, bạn có thể nhập điểm đến Address và thiết lập số tiền và phí.



![img](assets/en/15.webp)



#### Phân tách UTXO



Để hoàn thiện hơn, Nunchuk cũng cho phép tách biệt một (hoặc nhiều) UTXO theo hai cách khác nhau. Truy cập menu _Xem tiền_ và chọn thủ công từ danh sách tiền. Sau đó, nhấp vào menu _Thêm_ ở góc dưới bên phải: một danh sách các tùy chọn sẽ xuất hiện, từ đó bạn có thể chọn _Khóa tiền_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Bạn cũng có thể nhấp vào khoảng trống dành riêng cho UTXO để truy cập cửa sổ _Chi tiết tiền xu_. Tại đây, lệnh khóa/mở khóa UTXO sẽ xuất hiện ở góc trên bên phải.



![img](assets/en/41.webp)



### Ứng dụng Blockstream



Ứng dụng Blockstream trên máy tính để bàn, trước đây gọi là Green, cho phép bạn chọn Coin khi bạn đã bắt đầu xây dựng giao dịch. Do đó, hãy mở Wallet và nhấp vào _Gửi_.



![img](assets/en/16.webp)



Dán đích Address vào trường thích hợp rồi chọn _Lựa chọn Coin thủ công_.



![img](assets/en/17.webp)



Thao tác này sẽ mở ra cửa sổ cho phép bạn chọn một hoặc nhiều đồng UTXO. Trong ví dụ dưới đây, chúng tôi đã chọn hai đồng. Sau đó, hãy xác nhận lựa chọn của bạn bằng cách nhấp vào _Xác nhận lựa chọn Coin_.



![img](assets/en/18.webp)



Đặt số tiền và phí rồi tiến hành giao dịch bình thường.



![img](assets/en/19.webp)



⚠️ Lưu ý: Trong menu _Tiền_ của Green có các mục _Khóa_/_Mở_, báo hiệu khả năng tách UTXO. Tính năng này chỉ được kích hoạt trong các tài khoản được gọi là Multisig; nó cũng chỉ được kích hoạt khi chọn UTXO với số lượng rất nhỏ, gần với ngưỡng `Dust`.



## Wallet di động



Ví cũng có thể được chọn từ thiết bị di động, cho phép chọn UTXO theo cách thủ công. Hãy xem Blue Wallet là ví dụ đầu tiên.



### Màu xanh Wallet



Nếu bạn là người dùng Wallet này, hãy mở nó và nhấp để vào màn hình điều khiển liên quan đến một trong các Ví của bạn. Để truy cập hướng dẫn điều khiển Coin, bạn phải vào giai đoạn chi tiêu, sau đó nhấp vào _Gửi_.



![img](assets/en/21.webp)



Trên màn hình tiếp theo, hãy chọn các menu được biểu thị bằng ba dấu chấm ở góc trên bên phải. Một cửa sổ thả xuống sẽ mở ra với một loạt lệnh. Chọn lệnh cuối cùng: _Coin Control_.



![img](assets/en/22.webp)



Lúc này, Blue Wallet hiển thị tất cả các UTXO của bạn. Ngoài số lượng, chúng còn được phân biệt bằng đồ họa màu sắc.



![img](assets/en/27.webp)



Chọn UTXO để chọn sau đó chọn _Sử dụng tiền xu_.



![img](assets/en/23.webp)



Blue Wallet đưa bạn trở lại cửa sổ _Gửi_ để tiếp tục xây dựng giao dịch. Điều chỉnh số tiền và phí, sau đó chọn _Tiếp theo_.



![img](assets/en/24.webp)



Tại thời điểm này, bạn có thể kết thúc giao dịch như thường lệ.



#### Phân tách UTXO



Blue Wallet cũng cho phép bạn tách biệt các UTXO, khiến chúng không thể được sử dụng để chi tiêu, một tính năng không tệ đối với Wallet từ thiết bị di động. Bạn truy cập vào bộ điều khiển Coin theo quy trình vừa được giải thích và sau khi chọn UTXO, hãy chọn _Đóng băng_ thay vì _Sử dụng xu_.



![img](assets/en/26.webp)



### Nunchuk



Phiên bản di động của Nunchuk cũng cung cấp cho người dùng khả năng điều khiển Coin. Nếu bạn sử dụng ứng dụng này trên thiết bị di động, hãy mở ứng dụng và vào menu _Ví_. Từ đó, chọn _Xem tiền_.



![img](assets/en/30.webp)



Trong cửa sổ hiển thị danh sách UTXO, hãy nhấp vào _Chọn_.



![img](assets/en/38.webp)



Một chức năng lựa chọn sẽ xuất hiện bên cạnh mỗi UTXO. Giống như phiên bản máy tính để bàn, việc lựa chọn thủ công trên Nunchuk di động được thực hiện bằng cách đánh dấu vào ô vuông nhỏ bên cạnh số tiền. Màn hình hiển thị số lượng UTXO đã chọn và tổng số tiền khả dụng. Khi hoàn tất, hãy nhấp vào biểu tượng ₿ ở góc dưới bên trái, đây là lệnh để bắt đầu xây dựng giao dịch.



![img](assets/en/31.webp)



Bây giờ bạn có thể hoàn tất giao dịch bằng cách chọn số tiền và nhấp vào _Tiếp tục_.



![img](assets/en/32.webp)



Tiếp tục như bạn vẫn làm, dán đích Address, mô tả và tùy chỉnh cài đặt phí.



#### Phân tách UTXO



Bạn cũng có thể tách UTXO bằng Nunchuk di động. Truy cập cửa sổ danh sách coin chuyên dụng và chọn mũi tên bên cạnh UTXO bạn muốn tách.



![img](assets/en/42.webp)



Bạn sẽ thấy không gian dành riêng cho _Chi tiết tiền xu_, nơi bạn có thể chọn _Khóa đồng xu này_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper là Wallet cuối cùng chúng ta sẽ thấy trong hướng dẫn này. Chúng ta thấy chức năng của nó được áp dụng cho việc kiểm soát Coin với Wallet chữ ký đơn, mặc dù mục đích sử dụng đó không phải là mục đích của ứng dụng cụ thể này. Sau khi cài đặt Keeper trên điện thoại, hãy khởi chạy ứng dụng và mở Wallet chứa một số tiền. Ở giữa màn hình chính, hãy nhấp vào _Xem Tất cả Tiền_.



![img](assets/en/34.webp)



Keeper hiển thị tổng quan về các UTXO. Để truy cập màn hình lựa chọn, hãy nhấp vào _Chọn để Gửi_.



![img](assets/en/35.webp)



Bạn có thể chọn tiền xu bằng cách nhấp vào lệnh thích hợp. Khi hoàn tất, nhấp vào _Gửi_.



![img](assets/en/36.webp)



Bitcoin Keeper đưa bạn trực tiếp đến menu _Gửi_, nơi bạn có thể xây dựng giao dịch với các UTXO đã chọn.



![img](assets/en/37.webp)



## Hardware Wallet



Mỗi Ví Phần mềm được đề cập trong hướng dẫn này có thể là Interface chỉ dành cho thiết bị giám sát cho một trong các Ví Phần cứng của bạn. Điều này có nghĩa là việc điều khiển Coin cho thiết bị ký ngoại tuyến được thực hiện theo các bước đã nêu ở trên.



### Khuyến nghị chung



Kiểm soát Coin là một phương pháp rất hiệu quả để lựa chọn đầu vào giao dịch. Việc lựa chọn thủ công thậm chí còn hiệu quả hơn nếu bạn đã ghi rõ nguồn gốc Satoshi của mình khi mua/nhận tiền. Nếu bạn muốn học kỹ thuật này, tôi khuyên bạn nên xem hướng dẫn sau:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Chúng tôi đã nói trước đây về `phân loại phần còn lại`. Nếu bạn muốn khóa phần còn lại để xử lý sau và lấy lại quyền riêng tư (hoán đổi trên Layer 2), bạn phải cẩn thận `gắn nhãn` chúng mỗi khi nhận được. Trong số các Ví Phần mềm đã thấy cho đến nay, chỉ có Electrum tô màu đồ họa cho phần còn lại của UTXO để dễ dàng nhìn thấy. Các ví khác, chẳng hạn như Sparrow, hiển thị cho bạn chuỗi trong đường dẫn xuất của từng UTXO (`m/84'/0'/0'/1/11`).



Để áp dụng kỹ thuật này một cách hiệu quả, hãy nhớ luôn thêm mô tả vào số tiền thừa mà bạn nhận được: người mà bạn gửi tiền (khoản thanh toán, hướng dẫn hoặc hình thức khác) biết mã Address liên quan đến số tiền thừa và biết rằng số tiền đó thuộc về bạn vì nó xuất phát từ giao dịch mà hai người đã thực hiện cùng nhau!