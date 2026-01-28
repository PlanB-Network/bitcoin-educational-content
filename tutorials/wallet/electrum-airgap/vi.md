---
name: Electrum Airgap
description: Bước đầu tiên hướng tới bảo mật, một cold wallet với Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



Trong hướng dẫn này, tôi sẽ giải thích cách tạo thiết bị ký airgap đầu tiên của bạn, ngắt kết nối khỏi Internet, ngay cả khi không có Hardware Wallet chuyên dụng. Tất cả những gì bạn cần là có hai máy tính:




- một thiết bị cũ sẽ không bao giờ có thể kết nối Internet;
- máy tính bạn sử dụng hàng ngày.



Cấu hình này mang lại mức độ bảo mật cao hơn so với `Hot Wallet` cổ điển: máy tính cũ - không có kết nối mạng - là người lưu giữ khóa riêng của bạn, không bao giờ được tiết lộ trên Internet mà được lưu trữ ngoại tuyến ("airgap" hoặc "Cold").



Thay vào đó, bạn sẽ cài đặt màn hình Wallet ("chỉ xem") trên máy tính sử dụng hằng ngày của mình, được kết nối với mạng và có thể dùng để kiểm tra số dư và chuẩn bị giao dịch biên lai.



## Wallet Airgap: Cái gì và như thế nào



Bằng cách thực hiện các bước trong hướng dẫn này, chúng tôi sẽ cài đặt hai Electrum Software Wallet trên hai máy tính khác nhau và cuối cùng tạo hai Ví với các kho khóa khác nhau: airgap Wallet sẽ sử dụng toàn bộ hệ thống phân cấp của Wallet HD, trong khi màn hình Wallet sẽ được tạo bằng khóa công khai chính.



Hai Ví này sẽ, về mọi mặt, rất khác nhau. Điểm chung duy nhất của chúng, như chúng ta sẽ thấy, là các địa chỉ:




- gW-13 trên máy tính airgap chỉ có thể ký nhưng không kết nối được với mạng nên không biết số dư và địa chỉ đã sử dụng;
- Wallet trên máy tính hàng ngày sẽ chỉ có thể chuẩn bị và truyền bá các giao dịch mà không thể xử lý chi phí nếu không có khóa riêng.



## Chuẩn bị sơ bộ



Để tải Electrum, tôi khuyên bạn nên làm theo các bước đầu tiên trong hướng dẫn này:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Sau khi tải xuống, hãy luôn xác minh bản phát hành trước khi cài đặt, sau đó tiến hành cấu hình "Một máy chủ", như bạn sẽ tìm thấy trong phần trợ giúp, trong mục `Bắt đầu với Wallet giả`.



Thao tác cấu hình "Một máy chủ" chỉ cần thiết cho Wallet được cài đặt trên máy tính sử dụng hàng ngày, vì máy tính kia sẽ luôn ngoại tuyến.



Các thao tác sau đây liên quan đến việc thực hành trên hai máy tính khác nhau (và Ví), vì vậy - để thuận tiện và tập trung - tôi đã chọn cài đặt chế độ airgap Wallet với chủ đề sáng, trong khi màn hình Wallet có chủ đề tối.



## Tạo khoảng hở không khí Wallet



Sau khi tải xuống và xác minh việc tải xuống Electrum, hãy sao chép tệp thực thi và đưa nó vào máy tính ngoại tuyến của bạn. Sau đó khởi chạy nó và cài đặt Electrum.



Nhấp đúp để khởi động Electrum: máy tính mà bạn sẽ sử dụng Wallet đang ngoại tuyến, hãy bỏ qua các thiết lập mạng và tiến hành tạo Wallet mà trong hướng dẫn này chúng tôi sẽ gọi là `airgap`.



![image](assets/en/01.webp)



Chọn _Ví chuẩn_.



![image](assets/en/02.webp)



Sau đó chọn _Tạo hạt giống mới_ để có phần mềm generate là Mnemonic.



![image](assets/en/03.webp)



Ghi chép chính xác 12 từ generate từ Electrum vào một tờ giấy lót và tiến hành bước xác minh, nhập lại các từ theo thứ tự khi Electrum yêu cầu.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Sau khi hoàn tất việc tạo Wallet, hãy đặt mật khẩu phức tạp (`Strong`) để mã hóa tệp Wallet trên thiết bị airgap. Bước này rất tinh tế và quan trọng, vì mật khẩu được chọn hiện tại sẽ ngăn chặn quyền truy cập vào Wallet có quyền quyết định, có thể chi tiền để ký giao dịch.



![image](assets/en/06.webp)



Bằng cách nhấp vào _Finish_, Wallet được xác định và xuất hiện trên màn hình. Tất nhiên, chỉ báo kết nối mạng, tức là chấm màu ở góc dưới bên phải, có màu đỏ, vì máy tính bị ngắt kết nối và không cho phép Wallet hiển thị các khóa trực tuyến.



![image](assets/en/07.webp)



## Tạo Wallet của Visualization



Bây giờ Wallet của bạn đã có khóa riêng ngoại tuyến, bạn cần thiết lập Wallet hiển thị hoặc `chỉ xem`, cho phép bạn xem số dư cũng như chuẩn bị giao dịch biên lai để tiếp tục tích lũy Sats một cách an toàn.



Từ Wallet nằm trên thiết bị ngoại tuyến, hãy chọn menu _Ví_ -> _Thông tin_



![image](assets/en/08.webp)



Cửa sổ chứa tất cả thông tin Wallet của bạn sẽ xuất hiện, tại đó bạn có thể kiểm tra `derivation path` và `master fingerprint`, ví dụ như đánh dấu chúng bên cạnh các từ trong câu Mnemonic (khuyến khích sử dụng).



![image](assets/en/09.webp)



Hãy nhớ rằng bạn đang lấy dữ liệu này từ một máy tính không được kết nối, vì vậy bạn sẽ phải sao chép/dán `zpub` vào một tệp văn bản và lưu vào ổ USB.



Bây giờ bạn có thể di chuyển đến máy tính được kết nối Internet để khởi chạy Electrum và tạo Wallet mới.



Từ menu _File_, chọn _New/Restore_.



![image](assets/en/10.webp)



Wallet mới chỉ dùng để xem, vì vậy trong hướng dẫn này chúng tôi sẽ gọi nó là `chỉ dùng để xem`.



![image](assets/en/12.webp)



Trên màn hình tiếp theo, chọn _Ví chuẩn_ và tiếp tục bằng cách nhấp vào _Tiếp theo_.



![image](assets/en/13.webp)



Khi chọn `Keystore` hãy cẩn thận: để tạo màn hình Wallet, hãy chọn _Sử dụng khóa chính_. Sau đó, hãy tiếp tục với _Tiếp theo_.



![image](assets/en/14.webp)



Dán vào đây file `zpub` đã sao chép từ Wallet ngoại tuyến và bạn đã mang file này đến máy tính này thông qua phương tiện USB.



![image](assets/en/15.webp)



Kết thúc bằng cách đặt mật khẩu mạnh cho Wallet này, có thể khác với mật khẩu đã chọn cho Cold tương ứng.



Bạn sẽ thấy màn hình Wallet xuất hiện, kèm theo cảnh báo. Thông báo nhắc bạn rằng đây là màn hình Wallet chỉ hiển thị và bạn không thể chi tiêu số tiền liên quan bằng màn hình này.



**Lưu ý Well**: **do đó, bạn sẽ luôn cần phải sở hữu khóa riêng để xử lý UTXO của Wallet này**. Với một hệ thống sao lưu tốt, bạn sẽ không gặp khó khăn gì để giữ toàn bộ Bitcoin của mình.



![image](assets/en/16.webp)



Cảnh báo này sẽ xuất hiện mỗi lần bạn mở Wallet này. Nhấp vào _Ok_ và chúng ta hãy chuyển sang bước xác minh.



## Kiểm chứng hai chiếc Wallet



Như chúng ta đã tìm hiểu ở phần đầu của hướng dẫn này, Wallet airgap và màn hình hiển thị Wallet là hai danh mục đầu tư có chức năng khác nhau nhưng **có cùng địa chỉ**.



Nếu chúng ta nhìn vào hai chiếc Wallet cạnh nhau, về mặt trực quan, chúng ta nhận thấy rằng trong airgap Wallet có biểu tượng "seed", trong khi ở watch-only thì không có. Ngay cả chi tiết này cũng sẽ giúp bạn nhớ rằng màn hình Wallet Wallet không có khóa riêng.



![image](assets/en/17.webp)



Tuy nhiên, để thực hiện kiểm tra đầu tiên chính xác, hãy chọn menu `Địa chỉ` trong cả hai Ví: vì chúng có cùng địa chỉ nên danh sách địa chỉ phải giống hệt nhau cho cả hai Ví.



![image](assets/en/18.webp)



⚠️ **LƯU Ý**: **không thể có điểm trung gian; các địa chỉ phải giống nhau. Trong trường hợp chúng khác nhau, cần phải xóa tất cả các công việc đã thực hiện cho đến nay và bắt đầu lại**.



Bây giờ bạn có thể tiến hành thực hiện hai lần kiểm tra khác nhau. Đầu tiên, hãy thử xóa hai Ví và khôi phục chúng từ đầu, mỗi Ví trên máy tính phù hợp. Trong trường hợp bạn tiến hành xác minh này, các thủ tục cho màn hình Wallet giống hệt như những thủ tục được nêu ở trên.



Tuy nhiên, đối với Wallet airgap, trên màn hình `keystore`, bạn sẽ phải chọn _Tôi đã có hạt giống_ và nhập các từ bằng cách sao chép chúng từ bản sao lưu giấy của bạn.



Sau khi thời gian dùng thử "không tải" kết thúc, bạn có thể thử thực hiện giao dịch với số tiền nhỏ và chi tiêu ngay lập tức.



## Giao dịch nhận và chi tiêu



Để bắt đầu sử dụng Electrum airgap, bạn có thể thực hiện giao dịch biên lai với số tiền nhỏ, sau đó chi tiêu số tiền đó cho Address của riêng bạn. Sau đó, bạn có thể tự làm quen với quy trình, xác minh rằng bạn kiểm soát hoàn toàn số tiền.



**Lưu ý**: Tôi không khuyên bạn nên gửi một số tiền lớn vào Wallet trước khi bạn tự tin rằng mình có thể thực hiện mọi giao dịch một cách suôn sẻ.



Các bước được giải thích dưới đây thoạt nhìn có vẻ phức tạp. Đừng để điều này làm bạn nản lòng: khi bạn đã thử lần đầu, bạn sẽ thấy rằng chúng chỉ mất vài phút để hoàn thành.



Để nhận tiền, bạn nhất thiết phải sử dụng màn hình Wallet nằm trên máy tính của bạn được kết nối với Internet. Từ menu `Receive`, hãy nhấp vào _Create request_ để Electrum generate là Address khả dụng đầu tiên và sử dụng nó để gửi cho chúng tôi một vài Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Sau khi giao dịch được truyền đi, bạn có thể thấy rằng - theo lẽ tự nhiên - giao dịch chỉ hiển thị trên màn hình Wallet chứ không hiển thị trên airgap Wallet.



![image](assets/en/21.webp)



Sau khi giao dịch của bạn đã nhận được một số xác nhận, bạn có thể chuẩn bị chi phí và do đó thử quy trình ký từ Wallet ngoài mạng. Sau đó chuẩn bị giao dịch trên watch-only và nhấn _Preview_ để kiểm tra



![image](assets/en/22.webp)



Bạn sẽ thấy cửa sổ giao dịch nâng cao nơi bạn có thể thấy:




- giao dịch chưa được ký (`Trạng thái: Chưa ký);
- Các lệnh `Sign` và `Broadcast` bị cấm.



Điều duy nhất bạn có thể làm là xuất giao dịch theo nguyên trạng, mang đến Wallet airgap và ký vào đó.



Cắm ổ đĩa flash USB vào máy tính và từ menu ở góc dưới bên trái, chọn _Chia sẻ_.



![image](assets/en/23.webp)



Sau đó chọn _Lưu vào tệp_.



![image](assets/en/24.webp)



Lưu giao dịch vào thẻ nhớ USB.



Bạn sẽ nhận thấy rằng Electrum đặt tên tệp có chữ số đầu tiên của transaction ID và phần mở rộng tệp là `.PSBT`, nghĩa là `Partially Signed Bitcoin Transaction`.



Giải nén phương tiện có tệp `.PSBT` và kết nối nó với máy tính ngoại tuyến.



Từ airgap Wallet, bây giờ hãy chọn menu _Tools_, sau đó chọn _Load transaction_ và tiếp theo là From file_.



![image](assets/en/25.webp)



Với trình quản lý tệp, hãy chọn `.PSBT` từ vị trí của tệp đó.



![image](assets/en/29.webp)



Phần mềm máy tính ngoài mạng sẽ tự động mở cửa sổ giao dịch nâng cao, hoàn toàn giống với cách bạn thấy trên màn hình Wallet. Trạng thái là `Unsigned`, nhưng điểm khác biệt là lệnh `Sign` ở đây đang hoạt động. Và đó chính xác là những gì bạn sẽ phải thực hiện.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Bây giờ giao dịch đã được ký, hãy nhớ rằng Wallet của bạn đang ở trên một máy ngoại tuyến. Do đó, ngay cả khi bạn thấy lệnh `Broadcast` đang hoạt động, Wallet của bạn sẽ không thể truyền giao dịch đến mạng Bitcoin.



Điều bạn cần làm bây giờ là lặp lại thao tác xuất giao dịch đã ký vào ổ USB để có thể nhập giao dịch đó vào máy tính được kết nối Internet và truyền bá.



Từ menu bên trái phía dưới, chọn _Chia sẻ_ một lần nữa rồi chọn _Lưu vào tệp_.



![image](assets/en/28.webp)



Bây giờ tệp có phần mở rộng khác: **thay vì `.PSBT` thì giao dịch có phần mở rộng là `.txn`. Từ giờ trở đi, Electrum sẽ cho phép bạn nhận dạng các giao dịch đã ký từ các giao dịch chưa ký**.



![image](assets/en/30.webp)



Để thực hiện giao dịch cuối cùng, hãy lấy ổ USB ra khỏi máy tính ngoại tuyến và cắm vào máy tính được kết nối Internet.



Từ mục chỉ xem, lặp lại quy trình nhập, nghĩa là từ menu _Công cụ_, chọn _Tải giao dịch_ và cuối cùng là _Từ tệp_.



![image](assets/en/31.webp)



Electrum sẽ mở cửa sổ giao dịch cho bạn, khác biệt đáng kể so với cửa sổ được hiển thị trước đó trên Wallet này ở chỗ cửa sổ này hiện đã được ký (`Trạng thái: Đã ký`) và lệnh `Phát sóng` có thể truy cập được.



Thao tác cuối cùng bạn cần thực hiện chỉ là:



![image](assets/en/32.webp)



## Kết luận



Các bài kiểm tra của bạn hiện đã hoàn tất. Nếu bạn làm theo hướng dẫn và nhận được kết quả tương tự, bạn đã tạo được Wallet Cold với Electrum, trên hai máy tính khác nhau, mà bạn có thể sử dụng theo kiểu airgap để lưu trữ Bitcoin của mình.



Có hai điều duy nhất bạn cần chú ý kỹ:


1) **không bao giờ sử dụng Wallet airgap đến địa chỉ nhận generate**. Vì nó ngoại tuyến, nó sẽ luôn cung cấp cho bạn Address đầu tiên, trùng với địa chỉ bạn vừa sử dụng để thực hiện giao dịch thử nghiệm;



![image](assets/en/33.webp)



_Như bạn có thể thấy từ hình ảnh trên, Wallet ngoại tuyến không biết lịch sử Address của chính nó. Nó hoàn toàn mù về mặt này. **Nhiệm vụ duy nhất nó có thể làm cho bạn là lưu trữ khóa ngoại tuyến và ký giao dịch của bạn**_.



2) Sử dụng ổ đĩa flash USB chỉ dành riêng cho mục đích này, **đừng sử dụng phương tiện mà bạn thường dùng**. Các công cụ hàng ngày có nhiều khả năng bị tấn công mạng hơn và vô tình, bạn có thể tấn công cả máy tính mà bạn đang ngắt kết nối khỏi mạng. Một ổ đĩa USB mà bạn chỉ sử dụng cho mục đích này có rất ít cơ hội tiếp xúc với PC trực tuyến của bạn, đặc biệt nếu bạn là người nắm giữ không phải chi tiêu, do đó làm giảm khả năng nhận và sau đó truyền vi-rút, phần mềm độc hại, v.v.