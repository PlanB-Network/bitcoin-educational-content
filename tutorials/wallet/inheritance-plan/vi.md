---
name: Kế hoạch thừa kế Bitcoin
description: Cách chuyển Bitcoin cho người thân yêu
---

![cover](assets/cover.webp)



Việc chuyển nhượng bitcoin представляет một thách thức kỹ thuật lớn mà nhiều người nắm giữ thường bỏ qua. Không giống như các tài sản ngân hàng truyền thống, nơi một tổ chức tài chính có thể chuyển tiền cho chủ sở hữu hợp pháp, Bitcoin hoạt động mà không cần trung gian. Người thân của bạn sẽ không bao giờ có thể truy cập vào tiền của bạn nếu không có thông tin kỹ thuật cần thiết, bất kể tính hợp pháp của họ.



Hướng dẫn này sẽ hướng dẫn bạn cách tạo kế hoạch kế thừa kỹ thuật. Bạn sẽ tìm hiểu cách thức hoạt động của cơ chế truyền tải tự động on-chain, cách lập tài liệu cấu hình và cách chọn giải pháp phù hợp để đảm bảo rằng di sản Bitcoin của bạn vẫn có thể truy cập được đối với những người thân yêu.



## Vì sao kế hoạch bảo tồn di sản kỹ thuật lại quan trọng



Bitcoin dựa trên một nguyên tắc mật mã cơ bản: ai nắm giữ khóa riêng tư sẽ kiểm soát được tiền. Quyền kiểm soát này trở thành một lỗ hổng lớn khi người nắm giữ biến mất mà không truyền đạt thông tin cần thiết.



Kế hoạch thừa kế Bitcoin phải đáp ứng hai mục tiêu tưởng chừng như mâu thuẫn: cho phép người thân của bạn tiếp cận số tiền của bạn khi đến lúc thích hợp, đồng thời ngăn chặn bất kỳ ai khác tiếp cận chúng trước thời hạn. Sự cân bằng tinh tế này phụ thuộc vào khả năng lập trình vốn có của Bitcoin.



Sự phức tạp về mặt kỹ thuật làm tăng thêm độ khó. Người thừa kế của bạn sẽ phải thao tác với các khái niệm như cụm từ khôi phục, mô tả danh mục đầu tư hoặc đường dẫn thừa kế. Nếu không chuẩn bị đầy đủ, ngay cả người thừa kế có thiện chí cũng có nguy cơ mắc phải những sai lầm không thể khắc phục.



## Cơ chế kế thừa trong on-chain hoạt động như thế nào?



Bitcoin sử dụng ngôn ngữ kịch bản của mình để mã hóa trực tiếp các điều kiện chi tiêu trong giao dịch. Khả năng kế thừa của on-chain khai thác tính năng lập trình này để tạo ra các lộ trình phục hồi thay thế được kích hoạt tự động.



### Khóa thời gian



Cơ chế khóa thời gian là nền tảng của việc thừa kế trong Bitcoin. Chúng cho phép khóa tiền cho đến khi điều kiện thời gian được đáp ứng.



**CLTV (CheckLockTimeVerify)**: Cơ chế khóa thời gian tuyệt đối này kiểm tra xem một thời điểm cụ thể (ngày hoặc độ cao khối) đã được đạt đến trước khi cho phép chi tiêu. Ví dụ: "số tiền này chỉ có thể được chi tiêu sau khối 900000" hoặc "sau ngày 1 tháng 1 năm 2026". Ưu điểm của CLTV là cho phép trì hoãn dài (vài năm), nhưng ngày được cố định và áp dụng giống hệt nhau cho tất cả các UTXO trong danh mục đầu tư. Để duy trì quyền kiểm soát tiền của bạn, bạn phải định kỳ tạo một danh mục đầu tư mới với ngày hết hạn được kéo dài và chuyển tiền của bạn vào đó.



**CSV (CheckSequenceVerify)**: Cơ chế khóa thời gian tương đối này xác minh rằng một số lượng khối nhất định đã trôi qua kể từ khi UTXO được tạo. Ví dụ: "số tiền này chỉ có thể được chi tiêu sau 52560 khối (~1 năm) kể từ khi nhận được". Ưu điểm của CSV là mỗi UTXO có bộ đếm độc lập riêng. Mỗi khi bạn thực hiện giao dịch, các UTXO mới được tạo sẽ đặt lại giới hạn thời gian của chúng. Tuy nhiên, giới hạn kỹ thuật là 65535 khối (~15 tháng tối đa) sẽ hạn chế khung thời gian có thể. Cách tiếp cận này tự nhiên hơn cho việc sử dụng hàng ngày, vì hoạt động bình thường của bạn sẽ tự động đẩy lùi thời hạn.



### Nhiều con đường chi tiêu



Danh mục đầu tư thừa kế kết hợp nhiều phương thức chi tiêu khác nhau tại mỗi địa chỉ:





- Đường dẫn chính**: Chủ sở hữu có thể sử dụng tiền của mình bất cứ lúc nào bằng chìa khóa chính, không có giới hạn thời gian.
- Lộ trình khôi phục**: Một hoặc nhiều khóa thay thế chỉ có thể sử dụng tiền sau khi một khoảng thời gian nhất định đã trôi qua.



Mỗi giao dịch do chủ sở hữu thực hiện sẽ "làm mới" UTXO, tạo ra các đầu ra mới với khóa thời gian được đặt lại. Cơ chế này đảm bảo rằng miễn là chủ sở hữu vẫn hoạt động, các đường dẫn phục hồi sẽ không bao giờ được kích hoạt.



### Miniscript và Taproot



**Miniscript** là một ngôn ngữ có cấu trúc được phát triển bởi Andrew Poelstra, Pieter Wuille và Sanket Kanjalkar, giúp dễ dàng viết và phân tích các kịch bản Bitcoin phức tạp. Nó cho phép bạn soạn thảo các điều kiện chi tiêu dễ đọc và có thể kiểm chứng, điều cần thiết cho các cấu hình kế thừa liên quan đến nhiều khóa và khóa thời gian.



**Taproot** (được kích hoạt vào tháng 11 năm 2021) cải thiện đáng kể cơ chế thừa kế của on-chain. Nhờ cấu trúc cây (MAST), chỉ điều kiện chi tiêu được sử dụng mới được hiển thị trên blockchain. Nếu chủ sở hữu chi tiêu tiền của mình một cách bình thường, các điều kiện thừa kế sẽ vẫn ẩn. Tính bảo mật này cũng làm giảm chi phí giao dịch đối với các đường dẫn phức tạp.



## Tầm quan trọng then chốt của các từ mô tả



Đối với các danh mục đầu tư cũ, cụm từ phục hồi (seed) là không đủ để khôi phục quyền truy cập vào quỹ. **Mô tả** trở thành yếu tố quan trọng.



Mô tả (descriptor) là một chuỗi ký tự mô tả đầy đủ cấu trúc của một danh mục đầu tư: các khóa công khai liên quan, điều kiện chi tiêu, đường dẫn tạo ra (decipation paths) và các khóa thời gian đã được cấu hình. Dưới đây là một ví dụ đơn giản:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Mô tả này nói rằng: "hoặc khóa chính có thể được sử dụng ngay lập tức, hoặc khóa phục hồi có thể được sử dụng sau 52560 khối".



Hãy cùng phân tích ví dụ này:




- `wsh()` : Tập lệnh chứng thực Hash, cho biết loại địa chỉ (P2WSH)
- `or_d()`: điều kiện "hoặc" với nhánh mặc định
- pk([fingerprint/path]xpub...)`: Khóa công khai chính với dấu vân tay và đường dẫn tạo ra nó.
- `and_v()`: Điều kiện "và" kết hợp khóa phục hồi với khóa thời gian
- `older(52560)`: Khóa thời gian tương đối của 52560 khối



**Nếu thiếu mô tả, ngay cả với tất cả các cụm từ khôi phục, người thừa kế của bạn cũng không thể khôi phục lại danh mục đầu tư.** Danh mục đầu tư tiêu chuẩn chỉ có thể được khôi phục từ seed vì nó tuân theo các đường dẫn dẫn xuất tiêu chuẩn (BIP44, BIP84). Mặt khác, danh mục đầu tư cũ sử dụng các tập lệnh tùy chỉnh mà không thể đoán được. Bản sao lưu mô tả (hoặc tệp cấu hình được phần mềm của bạn xuất ra) phải đi kèm với các cụm từ khôi phục trong kế hoạch thừa kế của bạn.



## Các thành phần văn bản của kế hoạch thừa kế



Ngoài các cơ chế kỹ thuật, một kế hoạch kế thừa hiệu quả dựa trên ba trụ cột về tài liệu.



### Giấy thừa kế



Bức thư cá nhân này là điểm khởi đầu cho kế hoạch của bạn. Được viết cho những người thừa kế của bạn, nó giải thích bối cảnh và các biện pháp phòng ngừa cần thực hiện.



Thư của bạn phải bao gồm các quy tắc an toàn rõ ràng:




- Đừng vội vàng, hãy dành thời gian tìm hiểu trước khi chuyển tiền.
- Không bao giờ truyền đạt câu nói về sự hồi phục hoàn toàn cho chỉ một người.
- Tuyệt đối không nhập cụm từ khôi phục vào bất kỳ phần mềm hoặc máy tính nào chưa được xác minh.
- Hãy cảnh giác với các chiêu trò lừa đảo và những người đề nghị giúp đỡ không được yêu cầu.
- Hãy tham khảo ý kiến của ít nhất hai người bạn tin tưởng trước khi đưa ra bất kỳ quyết định nào.



Thư này cũng bao gồm thông tin liên lạc của công chứng viên và địa điểm lưu giữ di chúc của bạn. Tuyệt đối không được chứa cụm từ khôi phục hoặc mật khẩu.



### Danh bạ các liên hệ đáng tin cậy



Không người thừa kế nào nên tự mình đối mặt với việc khôi phục Bitcoin. Danh bạ này liệt kê những người có thể cung cấp hỗ trợ kỹ thuật hoặc pháp lý.



Đối với mỗi người liên hệ, hãy ghi lại: họ tên đầy đủ, mối quan hệ với bạn, vai trò trong kế hoạch, mức độ tin cậy, kỹ năng Bitcoin và thông tin liên lạc đầy đủ. Nguyên tắc cơ bản: người thừa kế của bạn luôn nên tham khảo ý kiến của ít nhất hai người khác nhau trước khi đưa ra bất kỳ quyết định quan trọng nào.



### Kiểm kê tài sản Bitcoin



Phần này liệt kê tất cả bitcoin của bạn cùng với thông tin kỹ thuật cần thiết để khôi phục chúng.



Đối với mỗi danh mục đầu tư, hãy ghi lại:




- Loại danh mục đầu tư**: phần cứng, phần mềm, cấu hình (đơn chữ ký, đa chữ ký, cũ)
- Vị trí thiết bị**: vị trí vật lý của phần cứng wallet
- Vị trí tệp cấu hình Descriptor**: rất quan trọng đối với các danh mục đầu tư nâng cao
- Vị trí của cụm từ phục hồi**: tách biệt với phần mô tả
- Mã truy cập**: nơi lưu trữ mã PIN và mật khẩu.
- Độ trễ đã cấu hình**: khi các đường dẫn phục hồi được kích hoạt



## Các giải pháp kỹ thuật có sẵn



Một số gói phần mềm triển khai cơ chế kế thừa on-chain. Mỗi gói đều có những đặc điểm kỹ thuật riêng.



### Liana



Liana là phần mềm máy tính để bàn (Linux, macOS, Windows) sử dụng Miniscript để tạo danh mục đầu tư với lộ trình phục hồi theo thời gian. Dự án được phát triển bởi Wizardsardine, đồng sáng lập bởi Antoine Poinsot (người đóng góp chính cho Bitcoin).



**Kiến trúc kỹ thuật**: Liana tạo ra các danh mục P2WSH (SegWit gốc) theo mặc định, với hỗ trợ Taproot tùy thuộc vào khả năng tương thích của phần cứng wallet của bạn. Kiến trúc dựa trên một đường dẫn chính và một hoặc nhiều đường dẫn phục hồi. Mô tả được tạo ra mã hóa tất cả các điều kiện và phải được lưu lại.



**Thời gian khóa được sử dụng**: Liana sử dụng thời gian khóa tương đối (CSV), giới hạn ở 65535 khối (~15 tháng). Để duy trì quyền kiểm soát, bạn phải thực hiện giao dịch làm mới trước khi thời gian khóa hết hạn.



**Tích hợp phần cứng wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY và các thiết bị khác tương thích để ký giao dịch.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper là một ứng dụng di động (iOS, Android) kết hợp chữ ký đa chữ ký và khóa thời gian thông qua "Kho lưu trữ nâng cao" của nó. Cách tiếp cận trên thiết bị di động với hướng dẫn tích hợp giúp người dùng không am hiểu kỹ thuật dễ dàng sử dụng.



**Kiến trúc kỹ thuật**: Enhanced Vaults sử dụng Miniscript để tạo cấu hình đa chữ ký, trong đó các khóa bổ sung được kích hoạt sau các khoảng thời gian trễ xác định. Khóa kế thừa bổ sung vào số lượng người dùng tối thiểu hiện có, trong khi Khóa khẩn cấp có thể bỏ qua hoàn toàn cấu hình đa chữ ký.



**Thời gian khóa được sử dụng**: Bitcoin Keeper sử dụng thời gian khóa tuyệt đối (CLTV), cho phép thời gian chờ vượt quá 15 tháng. Ngày kích hoạt được thiết lập khi tạo wallet và áp dụng cho tất cả các UTXO. Ứng dụng tích hợp chức năng "tái lưu trữ" tự động quản lý việc làm mới: người dùng chỉ cần làm theo các bước hướng dẫn, mà không cần phải tự tạo wallet mới.



**Các tính năng bổ sung**: Tài liệu thừa kế tích hợp, Ví Canary để phát hiện việc xâm phạm khóa và nhắc nhở làm mới.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Di sản



Heritage là một ứng dụng máy tính để bàn sử dụng các tập lệnh Taproot để mã hóa các điều kiện thừa kế. Việc sử dụng Taproot mang lại tính bảo mật cao hơn, vì các đường dẫn không được sử dụng sẽ vẫn ẩn trên chuỗi khối.



**Kiến trúc kỹ thuật**: Mỗi địa chỉ Heritage tích hợp một lộ trình chính và các lộ trình thay thế cho mỗi người thừa kế, với khung thời gian tăng dần. Cấu trúc phân cấp cho phép xác định bản sao lưu cá nhân sau 6 tháng và người thừa kế gia đình sau 12-15 tháng.



**Các chế độ sử dụng**: Phiên bản độc lập với nút mạng riêng của bạn (miễn phí) hoặc dịch vụ được quản lý bổ sung thêm lời nhắc và thông báo cho người thừa kế (0,05%/năm).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Quá trình phục hồi của người thừa kế



Hiểu rõ quy trình phục hồi giúp lập kế hoạch hiệu quả. Dưới đây là các bước kỹ thuật mà người thừa kế cần thực hiện.



### Yêu cầu phục hồi



Người thừa kế cần:


1. **Tệp mô tả hoặc tệp cấu hình** của danh mục đầu tư gốc (định dạng JSON hoặc văn bản, tùy thuộc vào phần mềm)


2. **Cụm từ khôi phục** (cụm từ liên quan đến khóa kế thừa, thường gồm 12 hoặc 24 từ)


3. **Phần mềm tương thích** (Liana, Bitcoin Keeper, Heritage hoặc Sparrow/Specter cho các mô tả tiêu chuẩn)


4. Kết nối đến nút **Bitcoin** để kiểm tra trạng thái khóa thời gian và phát sóng giao dịch.



### Các bước phục hồi



1. **Cài đặt phần mềm** trên thiết bị an toàn và cấu hình kết nối với mạng Bitcoin (nút cá nhân hoặc máy chủ Electrum).


2. **Nhập mô tả** để tái cấu trúc danh mục đầu tư. Phần mềm sẽ tự động generate tất cả các địa chỉ được sử dụng.


3. **Khôi phục khóa kế thừa** từ cụm từ khôi phục. Phần mềm sẽ kiểm tra xem khóa này có tương ứng với một trong các khóa được ủy quyền trong mô tả hay không.


4. **Đồng bộ hóa danh mục đầu tư** để phát hiện tất cả các UTXO và điều kiện chi tiêu của chúng.


5. **Kiểm tra thời hạn hết hạn khóa thời gian**: phần mềm sẽ cho biết đối với mỗi UTXO, đường dẫn khôi phục có đang hoạt động hay không.


6. **Tạo giao dịch khôi phục** đến địa chỉ do người thừa kế kiểm soát hoàn toàn (lý tưởng nhất là một wallet mới duy nhất)


7. **Ký và phát sóng** giao dịch trên mạng Bitcoin.



Nếu thời hạn khóa chưa hết hạn, người thừa kế sẽ phải chờ. Phần mềm sẽ hiển thị ngày hoặc khối mà từ đó việc khôi phục trở nên khả thi. Trong thời gian chờ đợi này, số tiền vẫn được bảo mật trên chuỗi khối.



### Những điểm cần lưu ý đối với người thừa kế



Người thừa kế phải đặc biệt chú ý đến:




- Kiểm tra tính xác thực của phần mềm đã tải xuống** (mã kiểm tra, chữ ký)
- Đừng bao giờ chia sẻ cụm từ phục hồi của bạn** với bất kỳ ai đề nghị giúp đỡ.
- Hãy tham khảo ý kiến ít nhất hai người bạn tin tưởng** trước khi tiến hành phục hồi.
- Chuyển số tiền đó vào một danh mục đầu tư đơn giản** mà anh ấy hoàn toàn kiểm soát sau khi hồi phục.



## Thực tiễn tốt nhất



### Phân tách thông tin



Không bao giờ lưu trữ tất cả thông tin ở cùng một nơi. Mô tả phải được tách biệt khỏi các cụm từ khôi phục, và các cụm từ khôi phục này lại được tách biệt khỏi mã PIN. Việc phân tán thông tin như vậy sẽ làm phức tạp việc truy cập của kẻ tấn công, đồng thời vẫn đảm bảo tính khả thi trong việc khôi phục lại dữ liệu bởi những người thừa kế hợp pháp của bạn.



### Kiểm tra phục hồi



Trước khi gửi một khoản tiền lớn, hãy thử nghiệm toàn bộ quy trình khôi phục với một số tiền nhỏ. Xác minh rằng bạn có thể khôi phục danh mục đầu tư từ mô tả và cụm từ khôi phục trên một thiết bị trống. Ghi lại các bước này để trình bày cho người thừa kế của bạn.



### Bảo trì khóa thời gian



Hãy lên kế hoạch gia hạn khóa thời gian của bạn trước khi chúng hết hạn. Đối với khóa thời gian 12 tháng, hãy thực hiện giao dịch cứ sau 9-10 tháng. Phần mềm thường cung cấp chức năng nhắc nhở hoặc gia hạn tự động.



### Cập nhật kế hoạch



Cấu hình Bitcoin của bạn sẽ được cải tiến liên tục. Mỗi thay đổi quan trọng (danh mục đầu tư mới, điều chỉnh thời hạn, bổ sung người kế nhiệm) đều phải được phản ánh trong tài liệu của bạn. Hãy thiết lập quy trình xem xét hàng năm.



## Lựa chọn cách tiếp cận của bạn



Việc lựa chọn giữa các giải pháp khác nhau phụ thuộc vào trình độ chuyên môn kỹ thuật và nhu cầu cụ thể của bạn.



**Liana** phù hợp với người dùng máy tính để bàn ưa thích phần mềm mã nguồn mở với quyền kiểm soát hoàn toàn thông qua máy chủ riêng của họ. Việc cấu hình vẫn dễ dàng nhờ giao diện hướng dẫn. Khóa thời gian tương đối (CSV) đơn giản hóa việc bảo trì, vì hoạt động thông thường của bạn sẽ tự động đẩy lùi thời hạn. Giới hạn: độ trễ tối đa khoảng 15 tháng (65535 khối).



**Bitcoin Keeper** hướng đến người dùng di động đang tìm kiếm giao diện trực quan với các tài liệu đi kèm được tích hợp. Ứng dụng cung cấp hai loại khóa đặc biệt: Khóa Kế thừa (bổ sung vào số lượng người dùng tối thiểu) và Khóa Khẩn cấp (bỏ qua hoàn toàn số lượng người dùng tối thiểu). Khóa thời gian tuyệt đối (CLTV) cho phép thời gian chờ vượt quá 15 tháng, với chức năng khôi phục tích hợp giúp đơn giản hóa việc làm mới. Gói Diamond Hands mở khóa các tính năng kế thừa nâng cao.



**Chế độ kế thừa** hướng đến người dùng kỹ thuật, những người đánh giá cao tính bảo mật của Taproot và khả năng kế thừa theo thứ bậc với độ trễ tăng dần. Cấu trúc cây của Taproot che giấu các điều kiện kế thừa trong các giao dịch thông thường, chỉ tiết lộ điều kiện được sử dụng trong quá trình phục hồi.



Cả ba giải pháp đều có một điểm chung: chúng đều yêu cầu làm mới định kỳ để ngăn chặn việc kích hoạt sớm các đường dẫn phục hồi. Hạn chế này vừa là cái giá phải trả vừa là sự đảm bảo của hệ thống kế thừa không đáng tin cậy của on-chain. Hãy lên lịch nhắc nhở thường xuyên và biến việc bảo trì này thành một phần trong quy trình quản lý Bitcoin của bạn.



## Phần kết luận



Kế hoạch kế thừa kỹ thuật Bitcoin kết hợp các cơ chế mã hóa (khóa thời gian, Miniscript, Taproot) với tài liệu hướng dẫn chi tiết. Ví điện tử tiên tiến cho phép bạn tự động chuyển Bitcoin sau một thời gian không hoạt động, mà không cần sự can thiệp của bên thứ ba.



Những yếu tố quan trọng cần truyền lại cho người thừa kế của bạn là: tệp mô tả hoặc cấu hình, cụm từ khôi phục, hướng dẫn khôi phục chi tiết và thông tin liên hệ của những người có chuyên môn có thể hỗ trợ họ.



Hãy bắt đầu bằng cách chọn một giải pháp kỹ thuật phù hợp với hồ sơ của bạn, thử nghiệm với một lượng nhỏ dữ liệu, sau đó ghi lại toàn bộ quy trình trong một kế hoạch có cấu trúc. Độ phức tạp ban đầu đảm bảo rằng tài sản Bitcoin của bạn sẽ được chuyển giao một cách hoàn toàn tự tin.



## Tài nguyên



### Mẫu kế hoạch thừa kế





- [Mẫu Kế hoạch Thừa kế Bitcoin (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Mẫu Tài liệu Plan ₿ Network



### Tài liệu tham khảo kỹ thuật





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Đặc tả về khóa thời gian tuyệt đối (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Đặc tả khóa thời gian tương đối (CSV)
- [Tài liệu tham khảo Miniscript](https://bitcoin.sipa.be/miniscript/) - Tài liệu chính thức về Miniscript do Pieter Wuille biên soạn.



### Trang web giải pháp chính thức





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7