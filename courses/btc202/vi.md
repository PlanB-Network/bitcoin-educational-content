---
name: Thiết lập nút Bitcoin đầu tiên của bạn
goal: Hiểu, cài đặt, cấu hình và sử dụng nút Bitcoin
objectives: 


  - Hiểu vai trò và mục đích của nút Bitcoin.
  - Xác định các giải pháp phần cứng và phần mềm khác nhau hiện có.
  - Cài đặt và cấu hình Full node (Bitcoin core).
  - Sử dụng Interface Umbrel và thêm các ứng dụng hữu ích.
  - Kết nối Wallet cá nhân với nút riêng của nó.
  - Khám phá các cài đặt nâng cao và biện pháp bảo mật tốt nhất.


---
# Trở thành một người dùng bitcoin có chủ quyền



Có lẽ bạn đã quen thuộc với câu châm ngôn "Not your key, not your coin" (Không phải chìa khóa, không phải tiền của bạn), câu nói khuyến khích việc tự quản lý bitcoin của mình. Việc sở hữu chìa khóa của riêng bạn quả thực là bước đầu tiên thiết yếu, nhưng chưa đủ. Để đạt được chủ quyền tiền tệ thực sự, bạn cũng cần cài đặt và sử dụng nút Bitcoin của riêng mình. Khóa học này được thiết kế để hướng dẫn bạn thực hiện bước cơ bản này trong hành trình Bitcoin của mình!



BTC 202 là một khóa học dễ tiếp cận, được thiết kế để hướng dẫn bạn cách tự làm nút thắt Bitcoin, ngay cả khi bạn không phải là chuyên gia kỹ thuật. Chúng ta sẽ bắt đầu bằng cách định nghĩa nút thắt Bitcoin là gì, công dụng của nó, và tại sao việc tự làm một nút thắt Bitcoin lại vô cùng cần thiết. Sau đó, tôi sẽ hướng dẫn bạn từng bước lựa chọn phần cứng, cài đặt phần mềm cần thiết, kết nối Wallet và thực hiện những tối ưu hóa đầu tiên để nâng cao hơn nữa.



Vận hành một node Bitcoin không chỉ là một lựa chọn cho các chuyên gia; mà còn là một điều cần thiết. Đây là một công cụ phục hồi mà mọi người dùng cần hiểu và triển khai. Khóa học này chính là điểm khởi đầu để bạn trở thành một người dùng Bitcoin có chủ quyền!




+++




# Giới thiệu


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Tổng quan về khóa học


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Chào mừng bạn đến với BTC 202, nơi bạn sẽ học cách cài đặt, cấu hình và sử dụng node Bitcoin một cách dễ dàng và độc lập. Nhưng chưa hết: bạn cũng sẽ tìm hiểu thêm về vị trí và chức năng của các node trong hệ thống Bitcoin. Khóa học xen kẽ giữa các phần giải thích lý thuyết và thực hành có hướng dẫn.



### Phần 1 - Giới thiệu



Trong phần đầu tiên của khóa học này, chúng ta sẽ làm rõ các khái niệm cơ bản và sau đó đi sâu vào các định nghĩa chi tiết hơn. Node là gì? Sự khác biệt giữa node, Wallet và Miner là gì? Sau đó, bạn sẽ tìm hiểu về Bitcoin core và các triển khai của giao thức. Mục tiêu là để hiểu rõ, tránh nhầm lẫn và thiết lập nền tảng lý thuyết vững chắc.



### Phần 2 - Trở thành người dùng bitcoin có chủ quyền



Trong phần thứ hai này, tôi sẽ bắt đầu bằng cách giải thích tầm quan trọng của việc vận hành node Bitcoin của riêng bạn. Sau đó, chúng ta sẽ tìm hiểu các loại node hiện có (node hoàn chỉnh, pruned, SPV...), cách thức hoạt động và ý nghĩa kỹ thuật của chúng.



Sau đó, chúng tôi sẽ cung cấp cho bạn tổng quan về phần mềm có sẵn để chạy nút Bitcoin, bao gồm cả ưu điểm và nhược điểm của chúng. Cuối cùng, chúng tôi sẽ kết luận bằng một số khuyến nghị rất thiết thực để lựa chọn phần cứng phù hợp với nhu cầu và ngân sách của bạn.



Do đó, phần này minh họa con đường của người khai thác bitcoin có chủ quyền: hiểu lý do tại sao cần phải chạy một nút, chọn loại nút dựa trên lựa chọn này, chọn phần mềm và tùy thuộc vào phần mềm đã chọn, xác định phần cứng phù hợp.



### Phần 3 - Cài đặt nút Bitcoin dễ dàng



Sau khi hoàn tất khâu chuẩn bị này, đã đến lúc thực hành với Phần 3 dành riêng cho Umbrel: hệ điều hành đám mây tại nhà giúp đơn giản hóa việc tự lưu trữ và cài đặt nút Bitcoin và Lightning.



Sau phần giới thiệu ngắn gọn về Umbrel, chúng tôi sẽ cung cấp hướng dẫn chi tiết để hướng dẫn bạn quy trình cài đặt và cấu hình trên máy DIY của riêng bạn. Mục tiêu của phần này rất rõ ràng: sở hữu nút Bitcoin đầu tiên hoạt động hoàn chỉnh và đồng bộ.



### Phần 4 - Kết nối Wallet với nút của bạn



Bây giờ bạn đã thiết lập xong nút Bitcoin, đã đến lúc sử dụng nó! Trong phần này, bạn sẽ học cách kết nối phần mềm quản lý Wallet (như Sparrow wallet) với bộ lập chỉ mục Address của riêng bạn (Electrs hoặc Fulcrum), hoặc trực tiếp với Bitcoin core, để bạn không còn phụ thuộc vào máy chủ công cộng nữa.



Chúng ta cũng sẽ xem xét vai trò của các trình lập chỉ mục và các phương pháp khác nhau để kết nối với nút của bạn (LAN, Tor, Tailscale, v.v.). Cuối cùng, trong chương cuối cùng, chúng ta sẽ xem xét các ứng dụng hữu ích nhất có sẵn trên Umbrel dành cho người dùng bitcoin hàng ngày.



### Phần 5 - Các khái niệm nâng cao và thực tiễn tốt nhất



Trong phần cuối cùng của BTC 202 này, mục tiêu là giúp bạn nâng cao kiến thức. Trước tiên, chúng ta sẽ xem xét các phương pháp hay nhất cần áp dụng với node Bitcoin mới của bạn và cách bảo trì nó về lâu dài.



Sau đó, chúng ta sẽ dành thời gian xem lại một số lý thuyết đã được đề cập trước đó trong khóa học, bao gồm hiểu chi tiết về quy trình IBD và khám phá ngang hàng, khám phá cấu trúc của một nút và cuối cùng là tìm hiểu cách sử dụng tệp `Bitcoin.conf` để tinh chỉnh cài đặt của bạn.



### Phần 6 - Phần cuối



Giống như tất cả các khóa học Plan ₿ Network, ở phần cuối, bạn sẽ thấy bài kiểm tra cuối kỳ để kiểm tra kiến thức của bạn về các nút Bitcoin.



Vậy, bạn đã sẵn sàng bật nút Bitcoin đầu tiên của mình chưa? Hãy đặt ra lộ trình cho chủ quyền!



## Nút Bitcoin là gì?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Theo mô tả của người sáng lập Satoshi Nakamoto, Bitcoin tự giới thiệu mình là một hệ thống tiền điện tử ngang hàng. Câu đơn giản này, cũng chính là tiêu đề của Sách Trắng, ẩn chứa nhiều manh mối về bản chất của Bitcoin:




- Trước hết, Satoshi mô tả Bitcoin là một "hệ thống", nói cách khác, là một tập hợp các thành phần phần cứng và phần mềm thống nhất tương tác với nhau để cung cấp một dịch vụ cụ thể hoặc thực hiện một chức năng cụ thể;
- Tiếp theo, ông giải thích rằng hệ thống này cho phép sử dụng tiền điện tử, tức là một hình thức tiền tệ vô hình;
- Cuối cùng, ông chỉ ra rằng hệ thống này không phụ thuộc vào bất kỳ thực thể trung tâm nào: nó là "ngang hàng", nghĩa là chính người dùng vận hành hệ thống.



Vì Bitcoin là một hệ thống, nó nhất thiết phải được chạy trên máy tính. Và, do tính chất ngang hàng, chính người dùng mới là người chịu trách nhiệm vận hành các máy này. Cái mà chúng tôi gọi là "nút Bitcoin" chính xác là máy tính mà phần mềm triển khai giao thức Bitcoin (giống như Bitcoin core, nhưng chúng ta sẽ quay lại vấn đề này sau) đang chạy. Đây là điều cho phép Bitcoin hoạt động mà không cần cơ quan quản lý trung tâm: việc xác thực được thực hiện theo cách phân tán, bởi hàng nghìn máy tính độc lập thuộc sở hữu của hàng nghìn người dùng.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: Hệ thống tiền điện tử ngang hàng*. https://Bitcoin.org/Bitcoin.pdf



Chính những người dùng này đảm bảo tính bảo mật của Bitcoin. Như Eric Voskuil giải thích trong cuốn sách *Cryptoeconomics* của mình, tính bảo mật của Bitcoin không phụ thuộc vào Blockchain, cũng không phụ thuộc vào sức mạnh băm, cũng không phụ thuộc vào xác thực, phi tập trung, mật mã, mã nguồn mở hay lý thuyết trò chơi. Tính bảo mật của Bitcoin chủ yếu phụ thuộc vào những cá nhân sẵn sàng chấp nhận rủi ro cá nhân. Phi tập trung cho phép phân tán rủi ro này trên một số lượng lớn cá nhân, và chỉ có khả năng chống lại rủi ro của họ mới đảm bảo tính vững chắc của hệ thống.



Nguyên lý này rất dễ hiểu: nếu Bitcoin phụ thuộc vào một nút duy nhất do một người sở hữu, thì việc giam giữ người đó cũng đủ để đánh sập mạng lưới, vì chỉ riêng họ đã gánh chịu mọi rủi ro. Với hàng chục nghìn nút phân tán khắp thế giới, rủi ro sẽ được phân tán: mỗi nhà điều hành này sẽ phải bị vô hiệu hóa để đánh sập Bitcoin.



![Image](assets/fr/048.webp)



Do đó, chúng ta có thể phân biệt và nêu tên một số khái niệm để làm rõ vấn đề trong phần còn lại của khóa học này:




- Tiền tệ Bitcoin: đơn vị tính toán được sử dụng cho các giao dịch trong hệ thống này;
- Mạng Bitcoin: tập hợp tất cả các nút được kết nối;
- Các nút Bitcoin: máy chạy chương trình triển khai Bitcoin;
- Triển khai Bitcoin: phần mềm dịch giao thức thành các lệnh có thể thực thi;
- Giao thức Bitcoin: tập hợp các quy tắc quản lý hoạt động của hệ thống;
- Hệ thống Bitcoin: sự kết hợp chặt chẽ của tất cả các hệ thống Elements.



### Vai trò của nút Bitcoin



Các nút Bitcoin kết hợp với nhau tạo thành mạng lưới Bitcoin. Chúng cho phép toàn bộ hệ thống hoạt động tự động, không cần sự can thiệp của cơ quan quản lý trung tâm hay hệ thống máy chủ phân cấp.



Ngay từ đầu, Bitcoin được thiết kế để cho phép mỗi người dùng chạy một nút cá nhân. Điều này vẫn đúng với phần mềm Bitcoin core ngày nay, kết hợp vai trò của Wallet và nút. Tuy nhiên, ngày nay, chức năng này thường bị tách rời: nhiều ví Bitcoin hiện đại chỉ là ví kết nối với các nút bên ngoài (thuộc sở hữu của cùng một người hoặc không).



### Giữ Blockchain



Nhiệm vụ đầu tiên của một nút là duy trì một bản sao cục bộ của Blockchain. Để ngăn chặn Double-spending trên Bitcoin mà không cần sự can thiệp của cơ quan quản lý trung ương, mỗi người dùng phải kiểm tra xem không có giao dịch nào tồn tại trong hệ thống. Cách duy nhất để chắc chắn điều này là biết tất cả các giao dịch được thực hiện trên Bitcoin. Vì lý do này, tất cả các giao dịch đều được đóng dấu thời gian và nhóm thành các khối, và mỗi nút lưu trữ toàn bộ Blockchain.



> Cách duy nhất để xác nhận sự vắng mặt của giao dịch là nhận biết tất cả các giao dịch.

Nakamoto, S. (2008). *Bitcoin: Hệ thống tiền điện tử ngang hàng*. https://Bitcoin.org/Bitcoin.pdf



Do đó, Blockchain là một thanh ghi đang phát triển: mỗi khi một khối mới được Miner xuất bản, nút sẽ kiểm tra tính hợp lệ của khối đó trước khi thêm vào bản sao cục bộ của chuỗi. Tính đến thời điểm hiện tại (tháng 7 năm 2025), toàn bộ Blockchain vượt quá 675 GB và kích thước này tiếp tục tăng lên, với trung bình một khối mới được thêm vào sau mỗi 10 phút.



![Image](assets/fr/049.webp)



Nút này cũng lưu giữ một bản ghi cục bộ về tất cả các UTXO hiện có tại bất kỳ thời điểm nào, được gọi là **bộ UTXO**. Cơ sở dữ liệu này chứa tất cả các đoạn Bitcoin chưa được sử dụng. Chúng ta sẽ xem xét lại chủ đề này một cách chi tiết trong phần cuối của khóa học.



### Xác minh và phân phối giao dịch



Vai trò thứ hai của một nút là đảm bảo việc xác minh và truyền tải các giao dịch. Khi một giao dịch mới đến nút (thông qua phần mềm Wallet hoặc một nút khác), nút sẽ kiểm tra xem giao dịch đó có tuân thủ một bộ quy tắc (quy tắc đồng thuận và quy tắc chuyển tiếp) hay không. Ví dụ:




- bitcoin đã sử dụng phải tồn tại trong tập UTXO của nó (cơ sở dữ liệu về các đầu ra chưa sử dụng);
- chữ ký phải hợp lệ và phải đáp ứng mọi điều kiện chi tiêu (chữ ký hợp lệ);
- tổng số lượng đầu ra không được vượt quá tổng số lượng đầu vào, nghĩa là chi phí không thể âm.



![Image](assets/fr/050.webp)



Sau khi xác thực, giao dịch được lưu trữ trong Mempool của nút, một không gian bộ nhớ tạm thời dành riêng cho các giao dịch chưa được xác nhận, và sau đó được chuyển tiếp đến các nút ngang hàng khác trong mạng mà giao dịch được kết nối. Cơ chế phân phối và xác thực này tiếp tục từ nút này sang nút khác. Theo cách này, giao dịch được lan truyền qua mạng Bitcoin, và mỗi nút lưu trữ giao dịch đó trong Mempool cho đến khi nó được Miner đưa vào một khối hợp lệ, sau đó Miner sẽ thực hiện xác nhận đầu tiên.



### Kiểm tra và phân phối các khối



Vai trò thứ ba của nút liên quan đến việc quản lý các khối đã khai thác. Khi Miner phát hiện ra một khối mới với mã Proof of Work hợp lệ, khối này sẽ được phát trên mạng. Các nút nhận được khối này, kiểm tra xem nó có tuân thủ tất cả các quy tắc giao thức hay không, và sau đó tích hợp nó vào bản sao cục bộ của Blockchain nếu nó hợp lệ. Tương tự như các giao dịch, các khối mới được xác thực sau đó sẽ được chuyển tiếp đến tất cả các nút ngang hàng được kết nối với nút. Quá trình này tiếp tục cho đến khi tất cả các nút trên mạng Bitcoin nhận biết được khối mới.



![Image](assets/fr/051.webp)



## Sự khác biệt giữa cung và Wallet là gì?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Điều cần thiết là phải phân biệt hai loại phần mềm riêng biệt khi sử dụng Bitcoin: phần mềm nút và phần mềm Wallet.



Như đã đề cập ở trên, nút Bitcoin là một phần mềm tích cực tham gia vào mạng ngang hàng. Nó thực hiện ba nhiệm vụ chính:




- dự phòng của Blockchain,
- xác thực và chuyển tiếp giao dịch,
- xác thực khối và chuyển tiếp.



Mặt khác, Bitcoin (Wallet) là một phần mềm được thiết kế để lưu trữ và quản lý khóa riêng của bạn. Các khóa này cho phép bạn chi tiêu bitcoin bằng cách đáp ứng các tập lệnh khóa (thường thông qua chữ ký). Wallet có thể kết nối với một nút (nội bộ hoặc từ xa) để tham khảo trạng thái của Blockchain và phát các giao dịch mà nó tạo ra, nhưng bản thân nó không phải là một bên tham gia vào mạng lưới.



Trong một số trường hợp, hai chức năng này cùng tồn tại trong cùng một phần mềm, như trường hợp của Bitcoin core, đóng vai trò vừa là Full node vừa là Wallet. Tuy nhiên, nhiều chương trình Wallet phổ biến (Sparrow, BlueWallet, v.v.) yêu cầu kết nối với một nút bên ngoài (có thể là của bạn hoặc của bên thứ ba) để phát sóng giao dịch và xác định số dư Wallet.



![Image](assets/fr/052.webp)



## Sự khác biệt giữa node và Miner là gì?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Khái niệm nút và Miner thường bị nhầm lẫn. Tuy nhiên, hai Elements này thực hiện các chức năng hoàn toàn khác nhau trong hệ thống.



Ban đầu, khi Bitcoin được Satoshi Nakamoto ra mắt vào năm 2009, mọi người dùng đều được kỳ vọng sẽ tham gia vào mạng lưới như một tổng thể. Do đó, phần mềm Bitcoin ban đầu kết hợp nhiều chức năng cùng một lúc: nó hoạt động như một Wallet, một nút, và cũng là một Miner, có khả năng tạo ra các khối mới. Vào thời điểm đó, độ khó của Mining rất thấp. Tất cả những gì bạn phải làm là chạy phần mềm Bitcoin trên máy tính của mình để tìm các khối và nhận bitcoin làm phần thưởng.



Tuy nhiên, với sự phổ biến dần dần của Bitcoin và số lượng thợ đào ngày càng tăng, bối cảnh cạnh tranh trong Mining đã có sự thay đổi đáng kể. Ngày nay, Mining đã trở thành một hoạt động cực kỳ cạnh tranh, do các công ty công nghiệp được trang bị cơ sở hạ tầng chuyên dụng thống trị. Công suất cần thiết để đào một khối mới hiện nay lớn đến mức một người dùng cá nhân gần như không thể thực hiện được việc này chỉ bằng một máy tính thông thường. Do đó, Mining hiện chủ yếu được thực hiện bằng các máy móc chuyên dụng gọi là ASIC (Mạch Tích hợp Chuyên dụng). Các chip này được tối ưu hóa riêng để chạy thuật toán SHA-256 kép, thuật toán được sử dụng cho Mining trên Bitcoin.



![Image](assets/fr/053.webp)



Trước sự phát triển này, vai trò của nút Bitcoin và nút Miner đã trở nên rõ ràng hơn. Như đã trình bày ở trên, vai trò của nút Bitcoin hoàn toàn mang tính thông tin và dựa trên xác thực. Vai trò của nút Miner thì khác:




- Nó chọn các giao dịch đang chờ xử lý trong Mempool.
- Nó xây dựng một khối ứng viên tích hợp các giao dịch này.
- Anh ta tìm kiếm bằng cách thử và sai để có được một mã Proof of Work hợp lệ.
- Nếu tìm thấy bằng chứng hợp lệ, nó sẽ truyền khối đó qua nút của nó đến các nút khác.



Miner cần có một nút Bitcoin để tương tác với mạng.



Vai trò của Miner đôi khi cũng được phân biệt với vai trò của máy băm. Máy băm là một máy có nhiệm vụ tạo mẫu các khối do máy chủ của nhóm cung cấp, tìm kiếm các giá trị băm thỏa mãn mục tiêu độ khó được xác định cho các phần chia sẻ, chứ không phải mục tiêu của Bitcoin. Phần còn lại của quy trình Mining, bao gồm xây dựng khối thực tế, lựa chọn giao dịch hoặc tìm kiếm Proof-of-Work theo độ khó riêng của Bitcoin, cũng như phân phối, được thực hiện trực tiếp bởi các nhóm.



![Image](assets/fr/054.webp)



Cuối cùng, có một sự khác biệt quan trọng về mặt động lực kinh tế giữa Miner và nút. Việc vận hành nút Bitcoin không mang lại lợi ích tài chính trực tiếp. Mặt khác, việc tham gia Mining mang lại phần thưởng (tiền trợ cấp và phí giao dịch) cho mỗi khối được tìm thấy.



Trong Phần 2, chúng ta sẽ khám phá chi tiết hơn về những lợi ích thực tế và cá nhân của việc cài đặt và sử dụng nút Bitcoin, không chỉ về mặt tài chính.



## Bitcoin core và triển khai giao thức


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Giao thức Bitcoin không phải là phần mềm: nó là một tập hợp các quy tắc ngầm được chia sẻ giữa người dùng mạng. Nó xác định các điều kiện hợp lệ của giao dịch, cơ chế tạo tiền, định dạng khối, các điều kiện Proof-of-Work và nhiều thông số kỹ thuật khác. Để tương tác với giao thức này, người dùng phải chạy phần mềm triển khai các quy tắc này: đây được gọi là **triển khai** Bitcoin.



Do đó, một triển khai là phần mềm nút: một chương trình có khả năng giao tiếp với các máy khác trên mạng Bitcoin, tải xuống, xác minh, lưu trữ và truyền các khối và giao dịch, đồng thời thực thi cục bộ các quy tắc đồng thuận và chuyển tiếp. Mỗi triển khai là một diễn giải cụ thể của giao thức, được viết bằng một ngôn ngữ lập trình nhất định, với kiến trúc, hiệu suất và tính công thái học riêng. Mỗi triển khai cũng sẽ có tổ chức phát triển riêng, với sự phân chia trách nhiệm riêng.



Trong số các triển khai này, có một triển khai chiếm ưu thế hơn hẳn: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Một triển khai mang tính lịch sử đã trở thành chuẩn mực



Bitcoin core là phần mềm tham chiếu cho giao thức Bitcoin. Nó được phát triển từ mã nguồn gốc do Satoshi Nakamoto viết vào năm 2008-2009, và là sự tiếp nối trực tiếp của nó. Ban đầu được gọi là "*Bitcoin*", sau đó là "*Bitcoin QT*" (do bổ sung giao diện đồ họa Interface thông qua thư viện Qt), nó được đổi tên thành "*Bitcoin core*" vào năm 2014 để phân biệt rõ ràng phần mềm với giao thức mạng. Kể từ phiên bản 0.5, nó được phân phối với hai thành phần: `Bitcoin-qt` (giao diện đồ họa Interface) và `bitcoind` (giao diện dòng lệnh Interface).



Về lý thuyết, Bitcoin core không đại diện cho giao thức Bitcoin; đúng hơn, nó chỉ là một trong số rất nhiều triển khai. Tuy nhiên, nó nổi bật bởi mức độ áp dụng rộng rãi, tuổi đời cao, tính mạnh mẽ của mã nguồn và quy trình phát triển nghiêm ngặt. Do đó, trên thực tế, các quy tắc được áp dụng bởi Bitcoin core thực chất là các quy tắc của giao thức Bitcoin: người dùng, nhà phát triển, thợ đào và các dịch vụ hệ sinh thái gần như chỉ tham chiếu đến nó.



### Phân phối hiện tại của các triển khai



Theo [dữ liệu được thu thập vào tháng 8 năm 2025 bởi Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (một nhà phát triển nổi tiếng trong hệ sinh thái), việc phân bổ các triển khai giữa các nút công khai của mạng như sau:




- Bitcoin core**: 87,3% số nút
- Bitcoin Knots**: 12,5
- Các triển khai tích lũy khác**: 0,2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Nói cách khác, khoảng 9/10 nút công khai đang chạy Bitcoin core. Phần còn lại của mạng lưới phụ thuộc vào các máy khách ít quan trọng hơn (mặc dù thị phần của Knots đã tăng mạnh trong những tháng gần đây, một phần do những tranh luận về giới hạn kích thước `OP_RETURN`). Các triển khai thay thế này thường được duy trì bởi một người hoặc một nhóm nhỏ.



**Lưu ý:** Tuy nhiên, những con số này vẫn chỉ là ước tính, vì chúng chủ yếu dựa trên các *nút lắng nghe*, tức là các nút chấp nhận kết nối đến (với cổng 8333 mở). Việc đếm các nút không lắng nghe* phức tạp hơn nhiều, vì không thể kết nối trực tiếp với chúng: bạn phải chờ chúng chủ động, dưới dạng kết nối đi. Trang web của Luke Dashjr tuyên bố cũng đang cố gắng đếm các *nút không lắng nghe* này, nhưng vẫn không thể có được dữ liệu hoàn toàn chính xác về chúng, và việc cập nhật các số liệu thống kê này chắc chắn sẽ chậm trễ so với thực tế.



### Hoạt động bên trong của Bitcoin core



Bitcoin core được viết bằng C++. Đây cũng là một dự án nguồn mở được duy trì bởi một cộng đồng các nhà phát triển tình nguyện hoặc được trả lương bởi nhiều tổ chức khác nhau (thường là các công ty trong hệ sinh thái có lợi ích liên quan đến việc phát triển Core). [Mã được lưu trữ trên GitHub](https://github.com/Bitcoin/Bitcoin), và quá trình phát triển tuân theo một quy trình nghiêm ngặt:




- Người đóng góp** gửi đề xuất dưới dạng _yêu cầu kéo_ (PR). Về nguyên tắc, bất kỳ ai cũng có thể đề xuất thay đổi, nhưng phải được kiểm tra, ghi chép và trải qua quy trình đánh giá ngang hàng.
- **Người bảo trì** có quyền phê duyệt và hợp nhất các PR. Họ là những người đảm bảo tính nhất quán và ổn định của dự án. Tính đến tháng 7 năm 2025, có năm người trong số họ: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao và Ryan Ofsky.
- Không có **người bảo trì chính** nào kể từ tháng 2 năm 2023. Vai trò này ban đầu do Satoshi Nakamoto đảm nhiệm khi ra mắt Bitcoin, sau đó là Gavin Andresen sau khi Nakamoto rời đi vào đầu năm 2011, và cuối cùng là Wladimir J. Van Der Laan từ năm 2014 đến năm 2023.



![Image](assets/fr/057.webp)



Việc phát triển Bitcoin core tuân theo logic trọng dụng nhân tài: những người đóng góp mới được khuyến khích xem xét và kiểm tra mã nguồn trước khi tự đề xuất bất kỳ thay đổi nào. Các quyết định được đưa ra dựa trên sự đồng thuận kỹ thuật, và những sửa đổi lớn (đặc biệt là trong các lĩnh vực đã đạt được sự đồng thuận) đòi hỏi phải thảo luận trực tiếp trên các kênh công khai, chẳng hạn như danh sách gửi thư hoặc câu lạc bộ đánh giá quan hệ công chúng.



### Các triển khai Bitcoin khác



Mặc dù còn hạn chế về mặt ứng dụng, vẫn có những khách hàng khác. Khách hàng chính là Bitcoin Knots, do Luke Dashjr phát triển, một phiên bản Fork của Bitcoin core, tích hợp các tùy chọn bổ sung và phương pháp phát triển thận trọng hơn. Những điều này bao gồm các hạn chế chặt chẽ hơn về định dạng giao dịch.



![Image](assets/fr/058.webp)



Chúng ta cũng có thể đề cập đến:




- Libbitcoin**: một thư viện C++ dạng mô-đun được phát triển bởi Amir Taaki và được bảo trì bởi Eric Voskuil;
- Bcoin**: một triển khai JavaScript, hiện không còn được duy trì tích cực;
- BTCD/btcsuit**e: một triển khai trong Go.



Các dự án này góp phần vào sự đa dạng của hệ sinh thái, nhưng việc áp dụng chúng vẫn còn rất hạn chế, khiến Bitcoin core khó có thể tiến hóa độc lập.



### Sức mạnh của các nhà phát triển Core



Bạn có thể nghĩ rằng các nhà phát triển Bitcoin core có quyền kiểm soát trực tiếp Bitcoin, nhưng không phải vậy. Họ không thể áp đặt thay đổi lên giao thức. Vai trò của họ là đề xuất mã. Mỗi người dùng, thông qua nút của họ, sẽ quyết định có sử dụng mã này hay không.



Điều này có nghĩa là nếu một thay đổi trong Bitcoin core không đạt được sự đồng thuận, các nút có thể bỏ qua nó, bằng cách không cập nhật Bitcoin core hoặc chỉ cần thay đổi cách triển khai. Ngược lại, nếu một tính năng mà người dùng mong muốn bị chặn trong quá trình phát triển Lõi, thì luôn có thể chuyển sang một triển khai khác hoặc chuyển sang Fork cho dự án.



Như chúng ta sẽ thảo luận sau trong khóa học này, chính các nút, theo trọng số kinh tế của chúng (tức là các thương gia), sẽ mang lại tiện ích cho một phiên bản của giao thức (và do đó cho loại tiền tệ tương ứng), bằng cách chấp nhận các đơn vị tuân thủ các quy tắc của nó. Do đó, quyền quản lý thực sự đối với Bitcoin nằm trong tay các thương gia này, chứ không phải các nhà phát triển.




# Trở thành một người dùng bitcoin có chủ quyền


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Tại sao phải tự vặn nút thắt của mình?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Có một niềm tin rộng rãi rằng việc vận hành một nút Bitcoin là một hành động hoàn toàn vị tha, không vì lợi ích cá nhân, mà chỉ nhằm phục vụ cho sự phi tập trung của mạng lưới. Một số người coi việc hỗ trợ hệ thống và thể hiện lòng biết ơn đối với Bitcoin là một hình thức nghĩa vụ của những người dùng Bitcoin.



Thật vậy, như chúng tôi đã chỉ ra trong các chương trước, việc dệt nút không mang lại lợi ích tài chính trực tiếp nào. Do đó, người ta có thể nghĩ rằng việc này không liên quan gì đến lợi ích cá nhân. Tuy nhiên, việc vận hành nút riêng mang lại nhiều lợi ích cá nhân. Để thuyết phục bạn về điều này, trong chương này, tôi sẽ trình bày tất cả các lý do, cả về mặt kỹ thuật lẫn chiến lược, tại sao bạn nên cài đặt và sử dụng nút Bitcoin của riêng mình.



### Phổ biến giao dịch bí mật hơn



Khi phần mềm Wallet kết nối với một nút bên ngoài, nó sẽ truyền các giao dịch đến một cơ sở hạ tầng không nằm trong tầm kiểm soát của bạn. Điều này tạo ra những rủi ro rõ ràng về giám sát: người vận hành nút từ xa có thể phân tích chi tiết các giao dịch của bạn, bao gồm số tiền và tần suất, và bằng cách kiểm tra chéo một số siêu dữ liệu nhất định (chẳng hạn như địa chỉ IP, thời gian và vị trí), có khả năng liên kết chúng với danh tính của bạn.



Thật vậy, như đã đề cập trong chương trước, ví không tự động giao tiếp với mạng Bitcoin; chúng phải kết nối với một nút để xem số dư hoặc phát sóng giao dịch. Nếu bạn chưa bao giờ thiết lập nút riêng, điều này có nghĩa là Wallet của bạn phụ thuộc vào cơ sở hạ tầng của bên thứ ba (thường là công ty phát triển phần mềm). Bên thứ ba này, đặc biệt nếu là một công ty, có thể theo dõi, khai thác hoặc thậm chí tiết lộ dữ liệu này: cho dù vì lý do thương mại, do ràng buộc pháp lý, hay do vi phạm bản quyền.



![Image](assets/fr/059.webp)



Bằng cách sử dụng nút riêng, bạn truyền tải giao dịch trực tiếp lên mạng, bỏ qua các bên trung gian. Miễn là bạn bảo mật nút đúng cách (chúng ta sẽ thảo luận sau) hoặc tuân thủ các tiêu chuẩn nhất định, thông tin sẽ không bị lộ: cả địa chỉ IP Address lẫn chi tiết giao dịch của bạn đều không đi qua bất kỳ thực thể nào mà bạn không kiểm soát. Đây là điều kiện tiên quyết cơ bản để bảo vệ tính bảo mật của bạn trên Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Giao dịch không thể kiểm duyệt



Vì những lý do tương tự đã đề cập ở trên, phần mềm Wallet dựa trên nút của bên thứ ba dễ bị kiểm duyệt: nhà điều hành nút từ xa có thể từ chối chuyển tiếp một số giao dịch nhất định vì nhiều lý do. Họ có thể coi chúng là đáng ngờ hoặc trái với chính sách của mình. Giao dịch cũng có thể bị chặn nếu không tuân thủ các quy tắc chuyển tiếp của nút. Cuối cùng, nhà điều hành có thể nhắm mục tiêu cụ thể vào địa chỉ IP Address của bạn để chặn việc phát sóng các giao dịch của bạn.



Ngược lại, bằng cách sử dụng nút riêng, bạn đảm bảo việc truyền tải các giao dịch của mình trong mạng ngang hàng. Điều này có nghĩa là bạn giữ toàn quyền kiểm soát việc phân phối các giao dịch mà không phụ thuộc vào bên trung gian. Miễn là giao dịch tuân thủ các quy tắc đồng thuận và chuyển tiếp của các nút được kết nối với nút của bạn, nó sẽ được phát trên mạng và sau đó, với điều kiện là có đủ phí, sẽ được tích hợp vào một khối bởi Miner. Việc có nút riêng đảm bảo việc xác nhận giao dịch của bạn một cách trung lập, không cần cấp phép.



### Xác minh dữ liệu độc lập



Nếu không có nút cá nhân, bạn vẫn phụ thuộc vào bên thứ ba để truy cập thông tin, chẳng hạn như số dư Address, trạng thái xác nhận giao dịch và tính hợp lệ của khối. Điều này ngụ ý sự tin tưởng ngầm định vào tính chính xác và toàn vẹn của nút bên ngoài.



![Image](assets/fr/060.webp)



Chạy Full node nghĩa là bạn có thể tự mình kiểm tra tất cả các quy tắc giao thức, cho mọi giao dịch và mọi khối. Do đó, số dư được hiển thị bởi Wallet của bạn không phải là dữ liệu nhận được từ máy chủ từ xa, mà là kết quả được tính toán cục bộ từ bản sao hoàn chỉnh của Blockchain, được xác thực từng khối. Cách tiếp cận này mang lại ý nghĩa đầy đủ cho châm ngôn của những người dùng Bitcoin:



> Đừng tin, hãy xác minh.

### Phân phối bảo mật hệ thống tốt hơn



Mỗi nút tham gia mạng lưới đều củng cố tính dự phòng và khả năng phục hồi của Bitcoin. Nó tạo điều kiện thuận lợi cho việc truyền bá thông tin và cho phép các nút mới kết nối với nhau. Nếu không có các nút, hệ thống sẽ không thể hoạt động.



Như chúng ta đã thấy, tính bảo mật của Bitcoin không dựa trên phi tập trung, Mining hay mật mã: như bất kỳ hệ thống nào khác, nó phụ thuộc vào cá nhân. Chính xác hơn, nó phụ thuộc vào khả năng chống lại sự ép buộc của các nhà điều hành nút.



Điểm khác biệt của các hệ thống phi tập trung như Bitcoin là sự phân bổ rủi ro giữa tất cả những người tham gia vận hành. Việc vận hành node Bitcoin của riêng bạn đồng nghĩa với việc chấp nhận chia sẻ rủi ro bằng cách đảm bảo tính bảo mật cho instance của bạn; đồng thời, bạn cũng giảm bớt gánh nặng rủi ro cho các nhà vận hành node khác.



Vì vậy, đây không phải là lợi ích cá nhân trực tiếp: việc vận hành một nút đồng nghĩa với việc bạn phải chịu một phần trách nhiệm về bảo mật mạng. Trên hết, đây là lợi ích tập thể, bởi vì sự tham gia của bạn giúp phân tán rủi ro. Đổi lại, bạn cũng nâng cao khả năng sử dụng Bitcoin một cách đáng tin cậy.



### Làm sâu sắc thêm sự hiểu biết của bạn về hệ thống



Việc cài đặt Full node không phải là một thao tác đơn giản. Nó bao gồm việc cài đặt phần mềm, tìm hiểu các thao tác cơ bản, giám sát đồng bộ hóa, kiểm tra nhật ký khi có sự cố và thậm chí là sử dụng thiết bị đầu cuối. Điều này chắc chắn sẽ giúp bạn hiểu sâu hơn về giao thức. Đây là một lợi thế gián tiếp nhưng không hề nhỏ.



Việc có được kiến thức này sẽ củng cố niềm tin của bạn vào công cụ và có thể giảm thiểu nguy cơ mắc lỗi hoặc bị lừa đảo. Tự mình thắt nút cũng là một hình thức học tập.



### Chọn quy tắc nào để áp dụng



Một khía cạnh quan trọng, thường bị hiểu lầm, là việc vận hành một nút cho phép bạn chọn các quy tắc áp dụng cục bộ. Có hai loại quy tắc chính:





- Quy tắc đồng thuận**:



Đây là các quy tắc cơ bản của giao thức Bitcoin, đảm bảo tính toàn vẹn của hệ thống và thiết lập các tiêu chí để xác thực giao dịch và khối. Bất kỳ giao dịch nào không tuân thủ các quy tắc đồng thuận này sẽ không bao giờ được đưa vào một khối hợp lệ. Ví dụ: một giao dịch có chữ ký không hợp lệ trên một trong các mục nhập của nó sẽ bị loại trừ một cách có hệ thống.



Việc thay đổi các quy tắc này tương đương với việc thay đổi giao thức, và do đó là thay đổi cả tiền tệ (Hard Fork). Tuy nhiên, ngay cả khi không cố gắng sửa đổi chúng, việc áp dụng nghiêm ngặt các quy tắc hiện hành cũng mang lại một sức mạnh nhất định: nếu một khối vi phạm các quy tắc, nút sẽ ngay lập tức từ chối khối đó.





- Quy tắc tiếp sức**:



Đây là các quy tắc dành riêng cho từng nút Bitcoin, được thêm vào các quy tắc đồng thuận để xác định cấu trúc của các giao dịch chưa được xác nhận được chấp nhận trong Mempool và được chuyển tiếp đến các nút ngang hàng. Mỗi nút cấu hình và áp dụng các quy tắc này cục bộ, điều này giải thích tại sao chúng có thể khác nhau giữa các nút. Chúng chỉ áp dụng cho các giao dịch chưa được xác nhận: một giao dịch được một nút coi là "không chuẩn" sẽ chỉ được chấp nhận nếu nó đã xuất hiện trong một khối hợp lệ. Việc thay đổi các quy tắc này không loại trừ nút đó khỏi hệ thống Bitcoin.



Ví dụ, một giao dịch không mất phí, theo quy tắc đồng thuận, hoàn toàn hợp lệ, nhưng sẽ bị từ chối theo mặc định theo chính sách chuyển tiếp Bitcoin core, vì tham số `minRelayTxFee` được đặt thành `0,00001` (tính bằng BTC/kB). Tuy nhiên, trên node của bạn, bạn có thể tự hạ ngưỡng này xuống để chuyển tiếp các giao dịch có phí thấp hơn, hoặc ngược lại, tăng giới hạn, chẳng hạn, lên 2 Sats/vB, để tránh chuyển tiếp các giao dịch có phí thấp.



Việc tự tạo nút của riêng bạn có nghĩa là khẳng định: "Tôi xác thực những gì tôi chọn xác thực, theo các quy tắc mà chính tôi đã áp dụng"*. Do đó, bạn trở thành một tác nhân trong việc quản trị hệ thống, có thể từ chối một sự phát triển mà bạn cho là không thể chấp nhận được, hoặc phê duyệt một bản cập nhật theo tiêu chí của riêng bạn.



Vì vậy, chúng ta có thể nhanh chóng tìm hiểu xem bạn có bao nhiêu quyền hạn đối với các quy tắc nhờ vào nút của mình. Và mức độ quyền hạn này sẽ phụ thuộc vào loại quy tắc.



#### Đối với các quy tắc tiếp sức



Về quy tắc chuyển tiếp, điều cốt yếu là sở hữu một nút, bất kể hoạt động kinh tế của nó. Vấn đề ở đây là bạn có đồng ý chuyển tiếp một số loại giao dịch nhất định hay không.



Ví dụ, nếu bạn tin rằng các giao dịch có phí dưới 1 sat/vB nên được chấp nhận trên Bitcoin, bạn có thể điều chỉnh quy tắc này trên nút của mình để nó phát các giao dịch này, do đó tạo điều kiện thuận lợi cho việc lan truyền chúng trên mạng cho đến khi Miner cuối cùng đưa chúng vào một khối hợp lệ. Về cơ bản, vấn đề nằm ở quyền lực trong việc phân phối các giao dịch: mỗi nút có quyền quyết định, vì việc đồng ý chuyển tiếp một loại giao dịch đồng nghĩa với việc thúc đẩy việc chấp nhận giao dịch đó trên mạng Bitcoin. Do đó, nếu bạn vận hành nhiều nút, bạn sẽ có ảnh hưởng lớn hơn đến chính sách chuyển tiếp, vì mỗi nút có các kết nối và phạm vi tác động riêng trên mạng.



Thật vậy, việc có một hoặc nhiều nút được cấu hình với các quy tắc chuyển tiếp cụ thể có nghĩa là xác định phần nào của mạng chấp nhận truyền bá một loại giao dịch nhất định. Việc truyền bá một thông điệp trong đồ thị ngang hàng, như trường hợp của các giao dịch Bitcoin, tuân theo logic của lý thuyết thấm lọc. Hãy tưởng tượng mỗi nút là một vị trí có thể hoạt động (`p` = nó chuyển tiếp) hoặc không hoạt động (`1-p`). Ngay khi tỷ lệ `p` vượt qua ngưỡng tới hạn (`p_c`), một thành phần khổng lồ xuất hiện: giao dịch có thể đi qua mạng và có mọi cơ hội để đạt đến Miner. Trong một mạng như Bitcoin, nơi mỗi nút duy trì trung bình 8 kết nối đi, ngưỡng `p_c` thường chỉ được đặt ở mức vài phần trăm, thậm chí thấp hơn nếu một số nút có số lượng kết nối rất lớn.



![Image](assets/fr/061.webp)



Miễn là `p` vẫn nhỏ hơn `p_c`, giao dịch sẽ bị giới hạn trong các vùng riêng biệt và không đạt đến ngưỡng Miner. Ngay khi vượt quá ngưỡng này, giao dịch sẽ lan truyền gần như ngay lập tức trên toàn bộ mạng.



Cuối cùng, chính các thợ đào (miner) mới là người quyết định có nên đưa một giao dịch vào khối hay không. Tuy nhiên, các nút (node) can thiệp ngược dòng bằng cách tác động đến việc phân phối giao dịch: chúng quyết định liệu các thợ đào có nhận thức được giao dịch đó hay không. Nếu một giao dịch không được chuyển tiếp đến các thợ đào, rõ ràng là họ không thể đưa giao dịch đó vào khối.



Do đó, việc thêm một vài nút nữa sẽ chỉ có tác động nhỏ nếu mạng đã ở giai đoạn thẩm thấu cho một loại giao dịch nhất định, nhưng nó có thể mang tính quyết định khi ngưỡng thẩm thấu đến gần. Việc sở hữu hoặc tác động đến nhiều nút, đặc biệt nếu chúng được kết nối tốt, có thể làm tăng hoặc giảm giá trị của `p` và do đó, gián tiếp điều khiển các quy tắc chuyển tiếp xác định giao dịch nào được nhìn thấy và cuối cùng được thợ đào chấp nhận.



#### Đối với các quy tắc đồng thuận



Khi nói đến ảnh hưởng của nút của bạn đối với các quy tắc đồng thuận, trên hết, trọng số kinh tế của nó sẽ là yếu tố quyết định. Đây là một khái niệm quan trọng: giá trị của bất kỳ loại tiền tệ nào đều liên quan trực tiếp đến khả năng tạo điều kiện thuận lợi cho Exchange. Thật vậy, nếu một vật thể không được bất kỳ ai trong Exchange chấp nhận làm hàng hóa hoặc dịch vụ, về mặt lý thuyết, nó không có giá trị tiền tệ. Ví dụ, nếu không có thương gia nào chấp nhận sỏi làm phương tiện thanh toán, thì chúng không có giá trị sử dụng làm tiền. Tất nhiên, tiện ích vẫn là một khái niệm chủ quan ở quy mô cá nhân, nhưng trong một lãnh thổ nhất định, số lượng thương gia chấp nhận một vật thể làm phương tiện của Exchange càng lớn, thì khả năng vật thể đó có giá trị tiền tệ đối với người dân sống trong lãnh thổ đó càng cao.



Hãy lấy ví dụ về một ngôi làng nơi nhiều thương nhân chấp nhận vàng để đổi lấy hàng hóa trong Exchange: rất có thể vàng có giá trị tiền tệ đối với dân làng. Điều này cho thấy giá trị của một loại tiền tệ phụ thuộc trực tiếp vào quyết định chấp nhận hay từ chối của thương nhân.



Khái niệm này rất quan trọng để hiểu được động lực quyền lực đang diễn ra trong hệ thống Bitcoin. Satoshi nêu rõ: Bitcoin là một hệ thống tiền điện tử; nói cách khác, nó cung cấp một dịch vụ cung cấp một hình thức tiền tệ, Bitcoin (hoặc BTC). Khi các quy tắc giao thức được sửa đổi theo cách không tương thích ngược (Hard Fork), điều này đồng nghĩa với việc tạo ra một hệ thống mới và do đó là một loại tiền tệ mới. Sự thành công hay thất bại của Fork này phụ thuộc vào quy mô nền kinh tế của nó, mà quy mô này lại được quyết định bởi số lượng thương nhân chấp nhận hình thức tiền tệ mới này.



![Image](assets/fr/062.webp)



Hãy lấy một ví dụ: giả sử Bitcoin gặp phải Hard Fork. Khi đó sẽ có 2 hình thức tiền tệ riêng biệt: BTC-1 (phiên bản gốc, không thay đổi) và BTC-2 (tiền tệ mới với các quy tắc đồng thuận khác nhau). Nếu tất cả các thương gia đã chấp nhận BTC-1 tiếp tục chấp nhận nhưng từ chối BTC-2, thì về mặt lý thuyết, BTC-2 sẽ có rất ít tiện ích tiền tệ. Là một người dùng, tôi sẽ không quan tâm đến việc giữ và sử dụng BTC-2, vì biết rằng không thương gia nào muốn sử dụng nó trong Exchange cho hàng hóa hoặc dịch vụ. Ngược lại, nếu 50% thương gia chọn chấp nhận BTC-2 độc quyền và 50% còn lại chỉ nhận BTC-1, thì về mặt lý thuyết, tiện ích của BTC-1 sẽ giảm một nửa. Tôi sử dụng thuật ngữ "về mặt lý thuyết" vì tiện ích vẫn mang tính chủ quan ở cấp độ cá nhân và phụ thuộc vào vô số yếu tố (chẳng hạn như lãnh thổ và thói quen tiêu dùng) mà khó có thể hiểu được trong từng trường hợp cụ thể.



Trên Bitcoin, vai trò của "thương nhân", được hiểu là bất kỳ thực thể nào có trọng lượng kinh tế nhất định, tất nhiên bao gồm các doanh nghiệp (cửa hàng thực, trang web bán hàng trực tuyến, nhà cung cấp dịch vụ, v.v.), mà còn cả các nền tảng Exchange, vì họ chấp nhận Bitcoin trong Exchange cho các loại tiền tệ khác và thợ đào, vì họ chấp nhận Bitcoin thông qua phí trong Exchange cho dịch vụ đưa giao dịch vào một khối.



Về mặt quy tắc đồng thuận, nút của bạn cho phép bạn định hướng hoạt động kinh tế của mình theo một loại tiền tệ này hay loại tiền tệ khác. Ví dụ: nếu bạn có 10 nút đầy đủ tại nhà nhưng không có hoạt động kinh tế đáng kể nào, ảnh hưởng của bạn trong Fork sẽ gần như bằng không. Ngược lại, một nút duy nhất được sử dụng để quản lý chuỗi 200 cửa hàng chấp nhận Bitcoin sẽ mang lại giá trị kinh tế đáng kể.



Vậy nên, điều quan trọng không phải là số lượng nút, mà là tầm quan trọng của hoạt động kinh tế mà chúng hỗ trợ. Hơn nữa, nếu hoạt động kinh tế của bạn phụ thuộc vào một nút mà bạn không kiểm soát, chủ sở hữu của nút đó sẽ quyết định loại tiền tệ bạn sử dụng, miễn là bạn vẫn kết nối với nút đó. Đây là lý do tại sao việc vận hành và sử dụng nút của riêng bạn lại đặc biệt quan trọng trong bối cảnh quản trị hệ thống:



> Không phải nút thắt của bạn, không phải quy tắc của bạn.


## Các loại nút Bitcoin khác nhau


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Do đó, một nút Bitcoin là một máy chạy một phiên bản triển khai của giao thức Bitcoin. Đằng sau định nghĩa chung về nút này, có một số cấu hình khả thi, không phải tất cả đều cung cấp cùng mức độ tự chủ, mức tiêu thụ tài nguyên và tính hữu ích cho mạng. Trong chương này, chúng ta sẽ cố gắng tìm hiểu những khác biệt này để giúp bạn lựa chọn kiến trúc nút phù hợp với nhu cầu sử dụng và các ràng buộc về phần cứng của mình.



### Nút thắt hoàn chỉnh



Full node đơn giản là một nút Bitcoin tải xuống toàn bộ Blockchain từ khối Genesis, xác thực từng khối một cách độc lập và lưu trữ lịch sử của tất cả Blockchain đó cục bộ. Đây là dạng "bình thường" của một nút Bitcoin, như Satoshi Nakamoto đã hình dung.



![Image](assets/fr/063.webp)



Full node không cần phải tin tưởng bất kỳ ai vì nó xác thực và nắm rõ mọi thông tin trong hệ thống. Đây là loại nút mang lại cho bạn nhiều sự đảm bảo nhất: bạn biết, mà không cần dựa vào bên thứ ba, liệu một khoản thanh toán có hợp lệ hay không, liệu một khối có hợp lệ hay không, liệu việc tái tổ chức có hợp pháp hay không, v.v.



Trên thực tế, Full node yêu cầu tài nguyên không hề nhỏ, bao gồm hàng trăm gigabyte cho các tệp khối, bộ xử lý có khả năng xác thực tập lệnh, RAM cho Mempool và bộ nhớ đệm, cùng băng thông ổn định. Quá trình đồng bộ hóa đầu tiên (*IBD*) đọc và xác minh toàn bộ lịch sử: rất phức tạp, nhưng chỉ diễn ra một lần. Full node tích cực tham gia vào mạng, chuyển tiếp các khối và giao dịch, và có thể chấp nhận các kết nối đến để hỗ trợ các đồng nghiệp khác.



Tùy thuộc vào nhu cầu, bạn có thể thêm một bộ lập chỉ mục vào Full node. Bitcoin core cung cấp tính năng lập chỉ mục giao dịch như một tính năng tùy chọn (mặc định bị tắt), có thể hữu ích cho các mục đích cụ thể. Tuy nhiên, nó không bao gồm bộ lập chỉ mục Address, vốn thường là tính năng được người dùng cá nhân tìm kiếm nhiều nhất. Để khắc phục điều này, bạn có thể cài đặt phần mềm chuyên dụng trên nút của mình, chẳng hạn như Electrs hoặc Fulcrum, để tăng tốc các truy vấn xác minh số dư Address từ các UTXO được liên kết. Chúng ta sẽ quay lại vai trò của bộ lập chỉ mục chi tiết hơn trong một chương riêng.



### Nút thắt pruned



Nút pruned xác thực mọi thứ như Full node, từ khối Genesis đến đầu chuỗi có khối lượng công việc nhiều nhất, nhưng **chỉ giữ lại phần gần đây nhất của các tệp khối**. Sau khi các khối cũ được kiểm tra, nó sẽ dần xóa chúng để giữ dung lượng dưới giới hạn dung lượng bạn có thể thiết lập. Cấu hình này lý tưởng nếu bạn có hạn chế về dung lượng ổ đĩa: bạn vẫn giữ được tính độc lập của việc xác thực khối mà không cần lưu trữ toàn bộ lịch sử Blockchain. Tùy chọn này đặc biệt hữu ích nếu bạn chỉ muốn cài đặt Bitcoin core trên máy tính cá nhân mà không cần sử dụng máy chuyên dụng.



![Image](assets/fr/064.webp)



Ý nghĩa kỹ thuật của tùy chọn này khá đơn giản: nút pruned hoàn toàn có khả năng phát sóng các giao dịch của bạn, tham gia vào quá trình chuyển tiếp, xác minh các khối và giao dịch, và theo dõi chuỗi. Mặt khác, nó không thể đóng vai trò là nguồn dữ liệu lịch sử vượt quá giới hạn của nó cho các ứng dụng khác (ví dụ: trình khám phá đầy đủ, trình lập chỉ mục, ví). Do đó, các chức năng yêu cầu lưu trữ (hoặc lập chỉ mục toàn cục) sẽ không khả dụng.



Trên thực tế, bạn có thể sử dụng nút pruned để kết nối phần mềm quản lý Wallet như Sparrow wallet. Tuy nhiên, bạn sẽ không thể quét các giao dịch trên Wallet trước giới hạn cắt tỉa. Ví dụ: nếu bạn có một giao dịch được đăng ký trong khối 901 458, nhưng nút của bạn chỉ giữ các khối từ 905 402 trở lên (vì khối cũ nhất là pruned), bạn sẽ không thể quét giao dịch này. Mặt khác, nếu bạn đã quét giao dịch khi nút của bạn vẫn còn chiều cao khối này, thì phần mềm quản lý Wallet sẽ lưu trữ thông tin và hiển thị chính xác số dư của các UTXO tương ứng.



Tóm lại, việc theo dõi Wallet hoạt động trơn tru trên một nút pruned nếu bạn tạo một Wallet mới trong khi phần mềm của bạn đã được kết nối với nút đó. Mặt khác, bạn có thể gặp khó khăn nếu khôi phục Wallet cũ, vì các giao dịch trước đó không còn được nút lưu giữ rõ ràng sẽ không thể truy xuất được.



### Nút thắt nhẹ / SPV



Một nút SPV (*Xác minh Thanh toán Đơn giản hóa*), hay nút nhẹ, chỉ lưu giữ tiêu đề khối, không lưu giữ chi tiết giao dịch, và dựa vào các nút đầy đủ khác để lấy bằng chứng giao dịch nằm trong khối (chứng minh Merkle thông qua cây) mà nó có tiêu đề. Khái niệm xác minh thanh toán đơn giản hóa không phải là mới, đã được chính Satoshi Nakamoto đề xuất trong phần 8 của Sách Trắng.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: Hệ thống tiền điện tử ngang hàng*. https://Bitcoin.org/Bitcoin.pdf



Loại nút này rõ ràng nhẹ hơn nhiều về mặt lưu trữ và sử dụng CPU so với nút Full node hoặc thậm chí pruned. Do đó, nút SPV rất phù hợp với các thiết bị nhỏ hơn và kết nối không liên tục. Trên thực tế, nó thường được tích hợp trực tiếp vào Wallet, đặc biệt là các phần mềm di động như ứng dụng Blockstream.



Đánh đổi ở đây là sự tin cậy và bảo mật: máy khách SPV không tự kiểm tra các tập lệnh hoặc chính sách xác thực; nó mặc định rằng chuỗi có khối lượng công việc nhiều nhất là hợp lệ và phụ thuộc vào một hoặc nhiều nút đầy đủ để phản hồi. Do đó, sử dụng loại nút này là một lựa chọn tốt hơn so với việc kết nối với một nút của bên thứ ba; tuy nhiên, nó vẫn kém lợi thế hơn so với việc sử dụng nút Full node hoặc thậm chí là nút pruned.



![Image](assets/fr/065.webp)



### Nút nào phục vụ cho nhu cầu nào?





- Người dùng di động / người mới bắt đầu



Đối với người dùng mới chỉ có Wallet trên ứng dụng di động, sử dụng nút SPV chắc chắn là cách tốt nhất để bắt đầu. Việc cài đặt nhanh chóng, ít tốn tài nguyên, và trải nghiệm đơn giản và mượt mà. Điều này có nghĩa là bạn có thể tự xác minh một số thông tin nhất định và do đó, ít phụ thuộc vào các nút của bên thứ ba hơn, đồng thời độc lập hơn khi phát sóng các giao dịch.





- PC / người dùng trung cấp



Người dùng trung cấp có máy tính cá nhân có thể cài đặt nút pruned để tận dụng hầu hết các ưu điểm của Full node mà không cần phải làm quá tải máy tính hàng ngày: xác thực đầy đủ, sử dụng ổ đĩa vừa phải và bảo trì đơn giản. Đây là giải pháp lý tưởng để kết nối ví máy tính để bàn và duy trì sự độc lập trong việc phân phối giao dịch, mà không cần đầu tư vào một máy tính chuyên dụng hoặc làm quá tải dung lượng ổ đĩa.





- Người dùng Bitcoin có chủ quyền / nâng cao



Full node vẫn là giải pháp tốt nhất nếu bạn muốn hoàn toàn độc lập trong việc sử dụng Bitcoin và không giới hạn bản thân vào các ứng dụng nâng cao sau này như lập chỉ mục, nút Lightning, hay thậm chí là Block explorer. Đó chính xác là những gì chúng ta sẽ khám phá trong khóa học này!



## Tổng quan về các giải pháp phần mềm


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Về mặt phần mềm, có 2 cách chính để chạy một nút Bitcoin:




- cài đặt trực tiếp một giao thức triển khai, chẳng hạn như Bitcoin core (được khuyến nghị) hoặc Bitcoin Knots,
- hoặc sử dụng bản phân phối trọn gói (thường được gọi là "_node-in-a-box_") tích hợp triển khai Bitcoin theo cùng một cách, nhưng cũng bao gồm hệ thống quản trị Interface, kho ứng dụng và các công cụ sẵn sàng sử dụng (Lightning, trình duyệt, máy chủ chỉ mục, thậm chí cả các ứng dụng tự lưu trữ bên ngoài Bitcoin...).



Cả hai phương pháp đều hướng đến cùng một mục tiêu: sở hữu một node riêng, nhưng chúng khác nhau về cách lắp đặt và sử dụng Interface, bảo trì, khả năng mở rộng và chi phí. Đó là những gì chúng ta sẽ tìm hiểu trong chương này.



### Triển khai nút Bitcoin thô



Cài đặt một triển khai thô nghĩa là sử dụng trực tiếp phần mềm của triển khai giao thức Bitcoin (chẳng hạn như Core), mà không cần bất kỳ phần mềm bổ sung nào của Layer. Bạn tự quản lý cấu hình, cập nhật và các dịch vụ liên quan (lập chỉ mục, API, Lightning, sao lưu, v.v.) theo nhu cầu của mình.



Đây là cách tiếp cận chủ động và linh hoạt nhất: bạn biết chính xác những gì đang chạy, dữ liệu ở đâu và mọi thứ hoạt động như thế nào. Mặt khác, mọi thứ trở nên phức tạp hơn ngay khi bạn muốn vượt ra ngoài hoạt động đơn giản của một nút Bitcoin. Nếu mục tiêu của bạn chỉ là có một nút, độ phức tạp tương đương với một nút đóng gói sẵn, hoặc thậm chí còn ít hơn, vì chỉ cần cài đặt phần mềm.



#### Bitcoin core (khách hàng cực kỳ đa số)



[Bitcoin core là máy khách chiếm đa số trong mạng](https://bitcoincore.org/). Nó tải xuống, xác thực và bảo trì Blockchain, cung cấp API RPC/REST và có thể tích hợp Wallet. Nếu bạn thích các công cụ tiêu chuẩn và cảm thấy thoải mái khi tự thêm các dịch vụ (chẳng hạn như máy chủ Electrum, trình duyệt và LND), tốt hơn hết bạn nên sử dụng Core.



**Lợi ích:** Độ ổn định tối đa, hành vi có thể dự đoán được, trải nghiệm thô sơ, dễ cài đặt và cấu hình.



**Nhược điểm:** Bạn phải tự tay xây dựng phần còn lại của ngăn xếp để tạo ra một môi trường ứng dụng hoàn chỉnh, thay vì chỉ một nút Bitcoin.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (khách hàng thay thế chính)



[Bitcoin Knots là Fork của Bitcoin core](https://bitcoinknots.org/), được Luke Dashjr duy trì. Đây là máy khách thay thế chính cho Core để triển khai giao thức Bitcoin. Hoàn toàn tương thích với phần còn lại của mạng (nó không phải là Hard Fork như Bitcoin Cash), tuy nhiên nó vẫn cung cấp các tính năng bổ sung, bao gồm các tùy chọn chính sách chuyển tiếp không có trong Core, hoặc được áp dụng nghiêm ngặt hơn theo mặc định để hạn chế những gì một số người coi là thư rác.



Có 2 lý do để chọn Knots thay vì Core:




- Kỹ thuật**: Các tùy chọn khác nhau từ Core, đặc biệt là về mặt quản lý chuyển tiếp, bằng cách xác định giao dịch nào được nút của bạn chấp nhận và phát đi.
- Chính sách**: Một số người thích sử dụng các máy khách thay thế như Knots vì những lý do phi kỹ thuật, đặc biệt là để hỗ trợ một giải pháp thay thế cho Core và do đó giảm bớt sự độc quyền của nó. Nếu Core bị xâm phạm, việc có các máy khách thay thế vững chắc, được bảo trì tốt sẽ rất hữu ích không chỉ mà còn phải biết cách sử dụng chúng một cách hiệu quả. Những người khác sử dụng Knots cho mục đích phản đối, vì họ đã mất niềm tin vào các nhà phát triển của Core hoặc không đồng tình với phần lớn ban quản lý của máy khách.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Cá nhân tôi khuyên bạn nên chọn Core, chủ yếu để được hưởng lợi từ các bản vá bảo mật nhanh hơn. Thực tế, một số lỗ hổng được phát hiện trong Knots được khắc phục khá chậm. Nhìn chung, quy trình phát triển của Core được xây dựng chặt chẽ và được hỗ trợ bởi một số lượng lớn người đóng góp, trong khi Knots chỉ được duy trì bởi một người và có cộng đồng nhỏ hơn nhiều. Mặt khác, các quy tắc chuyển tiếp có xu hướng mất đi tính hữu ích ngày nay, đặc biệt là khi chỉ được áp dụng bởi một phần rất nhỏ của mạng lưới (theo lý thuyết thẩm thấu).



### Phân phối Node-in-a-box



_Node-in-a-box_ kết hợp Bitcoin core (hoặc Knots) với hệ điều hành được cấu hình sẵn, Interface Web và App Store với các dịch vụ tự lưu trữ (Lightning, explorers, Electrum server, Mempool, BTCPay Server, Nextcloud, v.v.). Chỉ với một cú nhấp chuột, bạn có thể cài đặt, cập nhật và kết nối các mô-đun khác nhau này.



Đây là giải pháp đơn giản hơn nhiều cho việc khởi động và quản lý nhiều ứng dụng phụ trợ hàng ngày. Nhược điểm là khi xảy ra sự cố (ví dụ: xung đột ảnh Docker, cập nhật lỗi, cơ sở dữ liệu bị hỏng), việc gỡ lỗi có thể trở nên rất phức tạp, vì bạn phụ thuộc vào khả năng tích hợp riêng của bản phân phối. Hơn nữa, hỗ trợ cộng đồng hoặc hỗ trợ chính thức thường rất phức tạp.



Vì vậy, một node-in-a-box cực kỳ dễ sử dụng miễn là mọi thứ hoạt động bình thường, nhưng trong trường hợp có lỗi, bạn phải chuẩn bị thực hiện các tìm kiếm dài dòng, chờ trợ giúp và phải tự mình thực hiện.



Hầu hết các giải pháp này đều có hai định dạng:




- Máy được lắp ráp sẵn: là một máy tính hoàn chỉnh đã được cài đặt sẵn hệ điều hành. Những máy tính trả tiền theo nhu cầu này chỉ cần được cắm vào nguồn điện và kết nối Internet là có thể hoạt động. Nếu ngân sách cho phép, lựa chọn này có ưu điểm là rất dễ thiết lập, thường được ưu tiên hỗ trợ và đóng góp vào việc tài trợ cho quá trình phát triển, vì mô hình kinh doanh của các công ty này thường dựa trên việc bán phần cứng.
- Tự cài đặt: cài đặt hệ điều hành phân phối trên máy tính của bạn (PC cũ, NUC, Raspberry Pi, máy chủ gia đình...). Đây là giải pháp tiết kiệm nhất, vì bạn có thể tái chế máy cũ hoặc chọn phần cứng phù hợp với nhu cầu và ngân sách của mình. Đây cũng là lựa chọn linh hoạt nhất và dễ cấu hình nhất. Chúng ta sẽ tìm hiểu phương pháp này trong phần thực hành của khóa học.



Sau đây là tổng quan về các giải pháp node-in-a-box chính có sẵn (năm 2025):



### Umbrel (umbrelOS & Umbrel Home)



[Ngày nay, Umbrel là công ty hàng đầu về các giải pháp node-in-a-box (https://umbrel.com/). Thành công của Umbrel phần lớn nhờ vào tính đơn giản trong cài đặt (khi được triển khai trên một chiếc Raspberry Pi đơn giản), bộ xử lý Interface thanh lịch và trực quan, cùng hệ sinh thái ứng dụng phát triển nhanh chóng và hiện nay cực kỳ rộng lớn.



![Image](assets/fr/067.webp)



Ra mắt vào năm 2020 với tư cách là một nút Bitcoin đơn giản đi kèm một vài ứng dụng phụ trợ, Umbrel đã dần phát triển thành một đám mây gia đình hiện đại, đầy đủ tính năng.



Tôi sẽ không đi sâu vào chi tiết về cách thức hoạt động và các tính năng cụ thể của nó ở đây, vì chúng ta sẽ xem xét kỹ hơn trong chương đầu tiên của phần tiếp theo. Thật vậy, với mục đích của khóa học BTC 202 này, tôi đã chọn sử dụng UmbrelOS, mà tôi tin là giải pháp node-in-a-box tốt nhất hiện nay cho người dùng mới bắt đầu và trung cấp.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



Start9 cung cấp StartOS (https://start9.com/), một hệ thống được thiết kế cho "điện toán chủ quyền": mục tiêu là để mọi người sở hữu và quản lý máy chủ riêng của mình, được tăng cường bởi một thị trường các ứng dụng tự lưu trữ. Bạn có thể mua máy chủ Start9 (Server One giá 619 đô la, Server Pure giá 899 đô la) hoặc tự lắp ráp máy chủ theo chế độ DIY trên máy tính của mình.



Về phía Bitcoin, StartOS cho phép bạn cài đặt Full node, một node Lightning, Máy chủ BTCPay, Electrs và nhiều dịch vụ khác. Tuy nhiên, sức hấp dẫn của Start9 còn vượt xa hơn thế: nó cung cấp khả năng khám phá, cấu hình và triển khai nhiều phần mềm khác nhau (đám mây tệp, nhắn tin, giám sát) một cách thống nhất, với khả năng kiểm soát hoàn toàn. Do đó, dự án hướng đến những người dùng mong muốn một nền tảng tự lưu trữ mạnh mẽ, chứ không chỉ là một node Bitcoin đơn thuần. Đây có lẽ là hệ sinh thái hoàn chỉnh nhất sau Umbrel.



![Image](assets/fr/068.webp)



Điểm khác biệt chính với Umbrel nằm ở Interface. Umbrel dựa trên giao diện người dùng (UX) được trau chuốt kỹ lưỡng, trong khi Start9 cung cấp một Interface thô sơ và nhiều chức năng hơn. Hệ sinh thái ứng dụng của Start9 kém phong phú hơn Umbrel, nhưng bù lại, nó có một số lợi thế kỹ thuật: việc truy cập vào các cài đặt ứng dụng nâng cao được đơn giản hóa, trong khi Umbrel nhanh chóng trở nên hạn chế nếu Interface không cung cấp tùy chọn mong muốn. Start9 cũng vượt trội về quản lý sao lưu: ngoài giải pháp hiệu quả của Umbrel dành cho LND, Start9 không có cơ chế thống nhất, không giống như Start9. Hơn nữa, nó cung cấp các công cụ giám sát dễ tiếp cận hơn và kết nối từ xa được mã hóa (`https`), trong khi truy cập cục bộ vào Umbrel thông qua `http`.



Tóm lại, nếu bạn chỉ cần các ứng dụng thiết yếu cho Bitcoin, không quan tâm nhiều đến hệ sinh thái phong phú của Umbrel, và người dùng Interface không phải là ưu tiên hàng đầu, thì Start9 là lựa chọn tốt hơn. Còn lại, Umbrel là lựa chọn tốt hơn.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### Nút của tôi



[MyNode là một bản phân phối tập trung độc quyền vào Bitcoin và Lightning](https://mynodebtc.com/), cung cấp Interface trên web, một chợ ứng dụng và các bản nâng cấp chỉ bằng một cú nhấp chuột. Bạn có thể mua phần cứng sẵn sàng sử dụng (*Model Two* có giá 549 đô la) hoặc cài đặt MyNode miễn phí trên máy tính của mình. Dự án cũng cung cấp phiên bản phần mềm *Cao cấp* (94 đô la), bao gồm hỗ trợ ưu tiên và các tính năng nâng cao.



![Image](assets/fr/069.webp)



Trên thực tế, MyNode tập hợp tất cả các khối xây dựng cơ bản cần thiết để vận hành Full node, cũng như các ứng dụng thiết yếu cho người dùng Bitcoin. Do đó, đây là giải pháp phù hợp nếu bạn không yêu cầu các ứng dụng bên ngoài hệ sinh thái Bitcoin, chẳng hạn như các ứng dụng tự lưu trữ có trong hệ thống Start9 và Umbrel.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz là một dự án mã nguồn mở 100%](https://docs.raspiblitz.org/) (giấy phép MIT) để gắn một node Bitcoin và một node Lightning trên Raspberry Pi. Chỉ cần tải xuống hình ảnh, khởi động, sau đó làm theo hướng dẫn để có một node-in-a-box hoạt động trên Raspberry Pi của bạn. Các bộ dụng cụ lắp ráp sẵn cũng có sẵn từ các bên thứ ba, thường có giá từ 300 đến 400 đô la, tùy thuộc vào phần cứng. RaspiBlitz cũng cung cấp một loạt các ứng dụng bổ sung, dễ cài đặt.



![Image](assets/fr/070.webp)



Nếu bạn sở hữu Raspberry Pi, đây là một lựa chọn tuyệt vời, vì các hệ thống hoàn thiện hơn như Umbrel đang ngày càng trở nên nặng nề đối với loại máy tính mini này.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo là một node-in-a-box tập trung vào quyền riêng tư](https://wiki.ronindojo.io/en/home) tự động triển khai Samurai Dojo và Whirlpool, với Interface chuyên dụng và các plugin được thiết kế riêng cho hệ sinh thái Samurai.



Nguyên tắc rất đơn giản: nếu bạn sử dụng Ashigaru Wallet (phiên bản kế nhiệm của Samurai Wallet là Fork sau khi các nhà phát triển bị bắt) hoặc nếu bạn muốn hưởng lợi từ các công cụ bảo mật tiên tiến, RoninDojo là lựa chọn dành cho bạn.



![Image](assets/fr/071.webp)



Trước đây, dự án đã cung cấp một máy được cấu hình sẵn có tên là Tanto, nhưng hiện tại không khả dụng. Máy có thể sẽ quay trở lại vào một ngày nào đó sau. Trong thời gian chờ đợi, bạn có thể dễ dàng cài đặt RoninDojo trên Rock5B+ hoặc Rockpro64, hoặc thậm chí gián tiếp trên Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Một giải pháp [node-in-a-box] khác là Nodl (https://www.nodl.eu/). Giống như các dự án trước, bạn có thể mua phần cứng được cấu hình sẵn (giá từ 599 đến 799 euro, tùy thuộc vào mẫu máy) hoặc tự cài đặt ở chế độ DIY.



Về mặt phần mềm, Nodl tích hợp Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, cũng như BTC RPC Explorer, tất cả đều có chuỗi cập nhật tích hợp và mã nguồn mở theo giấy phép MIT.



![Image](assets/fr/072.webp)



Sau khi khám phá nhiều giải pháp phần mềm khác nhau, giờ là lúc chọn máy sẽ lưu trữ nút của bạn!




## Tổng quan về các giải pháp phần cứng


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Bây giờ chúng ta đã khám phá tất cả các khả năng phần mềm, hãy tập trung vào phần cứng cần thiết cho node của bạn. Tôi sẽ cung cấp cho bạn một số lời khuyên cụ thể về việc lựa chọn linh kiện, cùng với các cấu hình được điều chỉnh phù hợp với ngân sách khác nhau. Tất nhiên, đây chỉ là ý kiến và phản hồi cá nhân của tôi: chắc chắn còn có những lựa chọn thay thế phù hợp khác ngoài những lựa chọn được trình bày ở đây. Hơn nữa, tôi sẽ không nhắc lại các máy móc được lắp ráp sẵn của các dự án node-in-a-box, mà chúng ta đã đề cập trong chương trước. Ở đây, chúng ta sẽ chỉ tập trung vào các giải pháp DIY.



### Bạn có thực sự cần một máy chuyên dụng không?



Trong vài năm qua, những người dùng Bitcoin ngày càng nhận thức rõ một quan niệm sai lầm phổ biến, đặc biệt là với sự phổ biến của mô hình node-in-a-box vào đầu những năm 2020: một node Bitcoin nhất thiết phải chạy trên một máy tính chuyên dụng cho mục đích này. Nhưng điều này không đúng. Bạn không nhất thiết phải cần một máy tính chuyên dụng để chạy một node Bitcoin: Bitcoin core hoàn toàn có thể chạy trên máy tính cá nhân thông thường của bạn. Nếu bạn có đủ dung lượng ổ đĩa cho Blockchain hoặc bật tính năng cắt tỉa, bạn có thể xác thực chuỗi, kết nối Wallet và thậm chí đóng chương trình khi sử dụng xong. Ưu điểm của phương pháp này rất đáng kể: không cần đầu tư ban đầu và độ phức tạp tối thiểu.



![Image](assets/fr/074.webp)



Tuy nhiên, sử dụng máy chủ chuyên dụng thường thoải mái hơn. Nó có thể chạy liên tục (24/7), có thể truy cập từ xa mọi lúc, không chiếm dụng tài nguyên của máy chủ chính, và trên hết, tách biệt các nhu cầu sử dụng (một biện pháp bảo mật hiệu quả: nếu máy tính cá nhân của bạn gặp sự cố, máy chủ của bạn vẫn tiếp tục hoạt động và ngược lại). Vì vậy, câu hỏi không phải là "Tôi có cần một máy chủ chuyên dụng không?", mà là "Tôi có cần một máy chủ luôn trực tuyến, có thể truy cập bằng các thiết bị khác và có khả năng phát triển không?" (ví dụ như Lightning, bộ lập chỉ mục, các ứng dụng bổ sung...). Nếu câu trả lời là có, việc lựa chọn một máy chủ riêng sẽ giúp mọi việc đơn giản hơn nhiều.



### 3 phương pháp thu mua: tái chế, đồ cũ và đồ mới



#### Tái chế máy tính cũ



Đây là giải pháp tiết kiệm nhất. Hầu hết chúng ta đều có một chiếc PC cũ Dust ở nhà, hoặc ở cùng bạn bè và gia đình: đây là cơ hội hoàn hảo để đưa nó trở lại hoạt động! Để sử dụng như một máy chủ Bitcoin, chỉ cần lắp thêm ổ SSD 2TB và, tùy theo nhu cầu, có thể thay thế hoặc lắp thêm thanh RAM để tăng RAM. Dự kiến chi phí sẽ dao động từ 100 đến 200 euro cho một chiếc máy tính đầy đủ chức năng.



Trước khi mua bất kỳ phần cứng nào, hãy kiểm tra số lượng khe cắm ổ đĩa có sẵn, loại kết nối (M.2 hoặc SATA), định dạng RAM (SODIMM hoặc DIMM) và thế hệ RAM (DDR4, v.v.). Bạn cũng nên vệ sinh máy, đặc biệt là quạt, để đảm bảo hiệu suất tối ưu.



Tuy nhiên, hãy cẩn thận nếu bạn đang sử dụng máy tính xách tay: pin có thể trở thành vấn đề theo thời gian (sẽ nói thêm về vấn đề này sau trong chương).



#### Đã tân trang hoặc đã qua sử dụng



Thị trường tràn ngập các máy tính mini doanh nghiệp tân trang như *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini*, hay *Dell OptiPlex Micro*. Những máy này chắc chắn, nhỏ gọn, êm ái và tiết kiệm điện năng. Giá của chúng thấp hơn nhiều so với máy mới, và bạn có thể dễ dàng tìm thấy các mẫu được trang bị bộ vi xử lý i5/i7 thế hệ thứ 6 đến thứ 10 và RAM từ 8 đến 16 GB, tất cả đều có mức giá rất hấp dẫn, thường từ 70 đến 200 euro, tùy thuộc vào cấu hình. Theo tôi, đây có thể là lựa chọn tốt nhất nếu bạn đang tìm kiếm một máy tính chuyên dụng cho node Bitcoin của mình.



![Image](assets/fr/075.webp)



Bạn cũng có thể tìm thấy những chiếc PC và máy tính xách tay đã qua sử dụng từ vài năm trước, có cấu hình thú vị và giá trị tuyệt vời.



**Lưu ý:** các máy tính trong đội ngũ doanh nghiệp, chẳng hạn như *ThinkCentre Tiny*, thường chỉ được trang bị cổng *DisplayPort* (DP) cho màn hình, không có đầu ra HDMI. Vì vậy, đừng quên mang theo bộ chuyển đổi hoặc cáp DP-to-HDMI nếu bạn cần.



#### Mua mới



Nếu ngân sách cho phép, bạn cũng có thể chọn mua máy mới. Đây là một lựa chọn tốt nếu bạn muốn có phần cứng mới với hiệu năng tốt, đặc biệt nếu bạn dự định sử dụng Umbrel hoặc Start9 với các ứng dụng bổ sung ngoài hệ sinh thái Bitcoin để tự lưu trữ.



### Tôi nên chọn loại máy nào?



#### Mini-PC "NUC" / barebone



Theo tôi, máy tính mini là lựa chọn tối ưu nhất để lưu trữ một node Bitcoin tại nhà. Tiết kiệm không gian, dễ dàng đặt trên kệ, tiêu thụ điện năng tối thiểu và dễ dàng nâng cấp phần cứng, chẳng hạn như thêm RAM hoặc thay thế ổ SSD.



Cá nhân tôi thích *Lenovo ThinkCentre Tiny* hơn, vốn rất phổ biến trên thị trường máy tính cũ (từ các đội máy tính doanh nghiệp); chúng đặc biệt bền bỉ và dễ dàng sửa đổi. Tất nhiên, còn có nhiều sản phẩm tương đương từ các nhà sản xuất khác: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*..



![Image](assets/fr/001.webp)



**Điểm nổi bật:** kích thước nhỏ, mức tiêu thụ điện năng vừa phải, độ ồn thấp, khả năng mở rộng (tùy theo kiểu máy) và độ tin cậy.



**Điểm yếu:** đắt hơn một chút so với SBC loại Raspberry Pi, không có màn hình tích hợp (truy cập từ xa hoặc thông qua màn hình ngoài), không có pin (tắt đột ngột khi mất điện).



#### Máy tính xách tay chuyên dụng



Đây là một lựa chọn thay thế tuyệt vời với chi phí thấp cho máy tính mini: ngày nay, bạn có thể tìm thấy máy tính xách tay đã qua sử dụng hoặc thậm chí là máy tính mới với giá rẻ, được trang bị bộ vi xử lý tốt, nhiều cổng kết nối, cũng như màn hình và bàn phím tích hợp (rất tiện lợi cho việc lắp đặt ban đầu). Trên hết, pin hoạt động như một bộ lưu điện tự nhiên: trong trường hợp mất điện, máy tính không bị tắt đột ngột và thậm chí có thể hoạt động trong vài giờ.



![Image](assets/fr/076.webp)



**Điểm nổi bật:** Giải pháp tất cả trong một, pin hoạt động như một UPS (không bị mất điện), cài đặt đơn giản nhờ màn hình và bàn phím tích hợp, card Wi-Fi tích hợp và nhiều lựa chọn thị trường đã qua sử dụng và mới (thường có nghĩa là bạn có thể thương lượng giá cả).



**Nhược điểm:** tiêu thụ điện năng cao hơn một chút so với máy tính mini thông thường, pin hao mòn dần khi hoạt động 24/7 và giảm dung lượng, nguy cơ pin bị phồng hoặc tăng nhiệt độ theo thời gian, tuy hiếm nhưng có thật. Chính vì vậy, tôi cho rằng máy tính mini là lựa chọn tốt hơn máy tính xách tay: pin bị hao mòn dần và những rủi ro đi kèm.



Nếu bạn chọn giải pháp này, tôi khuyên bạn nên theo dõi chặt chẽ tình trạng pin để tránh mọi nguy hiểm. Hãy chú ý xem có hiện tượng quá nhiệt, mùi lạ, không ổn định hoặc vỏ pin bị biến dạng không. Trong trường hợp có báo động, hãy tắt máy tính và rút phích cắm ngay lập tức, sau đó mang pin đến cơ sở tái chế chuyên dụng.



**Mẹo:** Nếu BIOS/UEFI hoặc công cụ của nhà sản xuất cho phép, hãy đặt giới hạn tải (ví dụ: 60% hoặc 80%) để kéo dài tuổi thọ pin.



#### Raspberry Pi và các SBC khác: ý tưởng sai lầm



Đầu những năm 2020, với sự trỗi dậy của phần mềm node-in-a-box, cơn sốt Raspberry Pi cũng nổi lên như một phương tiện để chạy node Bitcoin. Ý tưởng này có vẻ hấp dẫn: giá rẻ, nhỏ gọn và dễ tiếp cận.



![Image](assets/fr/073.webp)



Trên thực tế, nếu mục tiêu của bạn chỉ là chạy một node Bitcoin mà không cần các ứng dụng bổ sung, Raspberry Pi có thể là đủ. Nhưng ngay khi bạn muốn sử dụng Umbrel, Start9 hoặc một hệ sinh thái phong phú hơn (Block explorer, trình lập chỉ mục Address, node Lightning, ứng dụng tự lưu trữ...), máy sẽ nhanh chóng đạt đến giới hạn.



Raspberry Pi có một số nhược điểm:




- bộ xử lý quá mỏng, với kiến trúc ARM đôi khi không tương thích với một số phần mềm nhất định hoặc cần xử lý nhiều hơn;
- RAM hàn, không thể nâng cấp, cấu hình hạn chế (thường tối đa là 8 GB);
- hộp đựng ngoài cho ổ SSD được kết nối bằng cáp, là nguồn phát sinh lỗi thường xuyên, đòi hỏi phải mua một loại card chuyên dụng cho ổ SSD ổn định;
- xu hướng nóng lên nhanh chóng và khó đảm bảo làm mát đúng cách;
- cần mua thêm phần cứng (vỏ máy, quạt, thẻ SSD, v.v.);
- kết nối rất hạn chế.



Theo truyền thống, ưu điểm lớn nhất của SBC như Raspberry Pi chính là giá thành: chỉ với vài chục euro, bạn đã có thể sở hữu một máy tính chuyên dụng. Tuy nhiên, ngày nay, giá cả đã tăng mạnh, và một khi bạn đã bổ sung tất cả các phần cứng cần thiết, chi phí sẽ gần bằng giá của một chiếc máy tính mini x86 đã qua sử dụng hoặc tân trang lần đầu, mà theo tôi, chúng có nhiều ưu điểm hơn hẳn. Vì lý do này, tôi không khuyên bạn nên chọn SBC.



### Chọn thành phần



#### Lưu trữ đĩa: Bắt buộc phải có SSD, tối thiểu 2 TB



Về mặt kỹ thuật, có thể chạy một nút Bitcoin trên ổ cứng HDD. Vấn đề là mọi thứ sẽ chậm đi đáng kể, đặc biệt là IBD, vốn sẽ trở nên cực kỳ lâu do Bitcoin core sử dụng đĩa làm bộ nhớ đệm (đặc biệt là đối với bộ UTXO). Đây là lý do tại sao tôi thực sự khuyên bạn không nên sử dụng ổ cứng HDD: nó tạo ra một nút thắt cổ chai thực sự, hạn chế nghiêm trọng sự phát triển trong tương lai (ví dụ: đối với một nút Lightning), và thậm chí có thể dẫn đến sự không đồng bộ hóa với đầu đọc Blockchain. Hơn nữa, áp lực liên tục lên đĩa cơ học làm tăng nguy cơ hao mòn sớm.



SSD thay đổi hoàn toàn trải nghiệm người dùng của bạn: mọi thứ trở nên nhanh hơn, mượt mà hơn, với độ tin cậy cao hơn rất nhiều. Do đó, việc sử dụng SSD (gần như) là bắt buộc đối với máy chủ của bạn, và bạn sẽ không hối tiếc, đặc biệt là khi các mẫu ổ cứng dung lượng cao hiện nay có giá cả tương đối phải chăng.



![Image](assets/fr/077.webp)



Về mặt dung lượng, 2TB đang dần khẳng định vị thế là mức dung lượng tối thiểu hợp lý mới. Vào mùa hè năm 2025, Blockchain đã đạt gần 700 GB, và nếu bạn thêm Umbrel, một trình lập chỉ mục Address và một vài ứng dụng, ổ SSD 1 TB sẽ nhanh chóng bị bão hòa. Với 2TB, bạn có một khoảng dự trữ thoải mái cho những năm tới (ước tính chung là từ 5 đến 15 năm). Bạn cũng có thể chọn 4TB nếu dự định sử dụng nhiều ứng dụng trên Umbrel, lưu trữ các tệp lớn trên máy chủ tự lưu trữ, hoặc nếu bạn muốn dự đoán nhu cầu dung lượng ổ đĩa của mình ở mức độ lớn.



![Image](assets/fr/078.webp)



Về định dạng, điều này sẽ phụ thuộc vào các cổng có sẵn trên máy của bạn; tuy nhiên, nếu có thể, tôi khuyên bạn nên sử dụng ổ SSD NVMe M.2.



#### Bộ nhớ (RAM): 8 đến 16 GB



Riêng đối với Bitcoin core (không có lớp phủ Umbrel), khuyến nghị dành cho nhà phát triển chỉ ra mức RAM tối thiểu là 256 MB với cài đặt được điều chỉnh ở mức thấp nhất, 512 MB với cài đặt mặc định và 1 GB cho mục đích sử dụng bình thường.



Mặt khác, nếu bạn đang sử dụng hệ thống node-in-a-box như Umbrel hoặc Start9, yêu cầu về RAM sẽ cao hơn đáng kể. Các nhà phát triển Umbrel khuyến nghị RAM tối thiểu 4 GB. Dung lượng này có thể đủ để chỉ chạy Core, nhưng bạn sẽ sớm bị giới hạn. Do đó, họ khuyến nghị 8 GB, mà tôi cũng coi là mức tối thiểu cho cấu hình cơ bản xung quanh Bitcoin (Core, LND, indexer và một vài ứng dụng). Theo kinh nghiệm của tôi, với Umbrel và một vài dịch vụ bổ sung, 8 GB vẫn hơi chật. Để thực sự thoải mái và có thêm chút dư địa, tôi khuyên bạn nên sử dụng RAM 16 GB.



#### Bộ xử lý (CPU)



Đối với một máy chủ Umbrel, yêu cầu tối thiểu là bộ xử lý lõi kép 64-bit của Intel hoặc AMD. Nếu bạn muốn sử dụng một vài ứng dụng ngoài Bitcoin core, bộ xử lý lõi tứ (hoặc cao hơn) sẽ tạo ra sự khác biệt thực sự về mặt hiệu năng. Ví dụ, bộ xử lý i5/i7 thế hệ thứ 6 đến 10 là những lựa chọn tuyệt vời trên thị trường máy tính cũ.



### Ví dụ về cấu hình cụ thể



Dưới đây, tôi đề xuất ba cấu hình cụ thể, phù hợp với các ngân sách và nhu cầu khác nhau, với các mô hình cụ thể hỗ trợ. Những lựa chọn này được cung cấp như ví dụ minh họa cho thông tin trong chương này; bạn không có nghĩa vụ phải chọn chính xác các mô hình này. Vì tôi coi Mini-PC là lựa chọn tốt nhất về lâu dài, tôi sẽ dựa vào định dạng này cho ba cấu hình được đề xuất.



*Giá hiển thị bên dưới chỉ mang tính chất tham khảo và có thể thay đổi tùy theo khu vực, nhà cung cấp và thời điểm*



Trước hết, bạn cần một ổ SSD đủ lớn để chứa Blockchain, đồng thời vẫn có đủ không gian để thao tác. SSD có tuổi thọ hạn chế về số chu kỳ ghi và tổng dung lượng dữ liệu được ghi. Tuy nhiên, một ổ SSD Bitcoin tạo ra tải trọng đáng kể lên ổ đĩa khi ghi. Đó là lý do tại sao tôi không khuyên dùng các mẫu máy tính giá rẻ; thay vào đó, tôi khuyên bạn nên sử dụng SSD NVMe, vốn mang lại hiệu năng tốt hơn đáng kể.



Ví dụ, cho mục đích của khóa học này, tôi đã chọn mẫu ổ cứng sau: *Ổ cứng SSD Samsung 990 EVO Plus NVMe M.2 2Tb*, có giá khoảng 120 euro trên Amazon. Bạn cũng có thể lựa chọn các thương hiệu nổi tiếng khác như Crucial, Western Digital hoặc Kingston.



![Image](assets/fr/046.webp)



#### Cấu hình giá rẻ



Rõ ràng, nếu ngân sách của bạn rất hạn chế (dưới 200 euro), tôi khuyên bạn không nên đầu tư vào một máy chuyên dụng mà nên cài đặt Bitcoin core trực tiếp trên máy tính cá nhân sử dụng hàng ngày của bạn (ở chế độ pruned nếu bạn thiếu dung lượng ổ đĩa).



Nếu không, với ngân sách dành cho người mới bắt đầu, tôi khuyên bạn nên dùng *HP EliteDesk 800 G2 Mini*. Tôi tìm thấy một mẫu máy tính tân trang với giá 96 euro trên Amazon, được trang bị bộ xử lý Intel Core i5 thế hệ thứ 6 và RAM 8 GB. Đây là một lựa chọn đặc biệt thú vị cho người mới bắt đầu: bộ xử lý và dung lượng bộ nhớ này là quá đủ để chạy Core trên Umbrel, cũng như nhiều ứng dụng cùng lúc, chẳng hạn như trình lập chỉ mục Electrs, nút Lightning và phiên bản Mempool, miễn là bạn không phân bổ quá nhiều bộ nhớ đệm cho Core. Hơn nữa, loại máy tính mini này giúp bạn dễ dàng tăng RAM lên 16 GB nếu cần (dự kiến sẽ phải trả thêm khoảng 30-40 euro cho một hoặc hai thanh nhớ chất lượng).



![Image](assets/fr/045.webp)



Sau đó, chỉ cần thêm ổ SSD vào ngân sách. Bắt đầu với ổ Samsung 2TB giá 120 euro, tổng chi phí cho một máy hoàn chỉnh, hoạt động tốt là 216 euro.



#### Cấu hình ngân sách trung bình



Nếu bạn có ngân sách trung bình khoảng 300 euro cho máy chủ node, tôi khuyên bạn nên chọn *Lenovo ThinkCentre Tiny*, chẳng hạn, được trang bị bộ xử lý hiệu năng cao và RAM đủ dùng. Tôi tìm thấy một mẫu máy tân trang trên Amazon với giá 180 euro, được trang bị bộ xử lý Intel Core i7 thế hệ thứ 6 và RAM 16 GB. Cộng thêm ổ SSD 2 TB với giá 120 euro, tổng chi phí là 300 euro.



![Image](assets/fr/044.webp)



Với chiếc máy này, bạn có cấu hình thoải mái: IBD nhanh và khả năng chạy nhiều ứng dụng trên Umbrel hoặc Start9 mà không gặp khó khăn. Đây chính xác là cấu hình tôi đang sử dụng cho khóa học BTC 202 này.



#### Cấu hình cao cấp



Với ngân sách lớn hơn, khả năng sẽ trở nên rộng mở hơn đáng kể. Bạn có thể chọn cấu hình DIY, hoặc thậm chí chọn máy lắp ráp sẵn được cung cấp trực tiếp bởi một dự án node-in-a-box.



Ví dụ, *ASUS NUC 14 Pro* hiện đang được bán mới trên Amazon với giá 540 euro. Với mức giá này, bạn sẽ sở hữu bộ vi xử lý Intel Core Ultra 5 (mới và hiệu năng cao), cùng với 16 GB RAM DDR5. Với cấu hình này, bạn có thể hoàn thành một bài kiểm tra IBD trong thời gian kỷ lục và cài đặt các ứng dụng nặng mà không gặp khó khăn.



Đây là một cấu hình cực kỳ thoải mái, thậm chí là hơi quá mức nếu mục tiêu ban đầu chỉ đơn giản là chạy một node Bitcoin. Mặt khác, nếu bạn muốn tận dụng tối đa tất cả các ứng dụng tự lưu trữ có sẵn trên Umbrel và Start9, thì mức công suất này là hoàn toàn phù hợp với bạn.



![Image](assets/fr/043.webp)



Tùy thuộc vào mục đích sử dụng, bạn có thể chọn ổ SSD 2TB như các cấu hình khác, hoặc mua trực tiếp ổ SSD 4TB với giá 260 euro nếu bạn muốn lưu trữ dữ liệu cá nhân và mở rộng phạm vi sử dụng dịch vụ tự lưu trữ. Với ổ SSD 2TB, tổng chi phí cấu hình là 660 euro, trong khi với ổ SSD 4TB, chi phí lên tới 800 euro.



### Một vài mẹo nữa





- Nếu bạn muốn mua thiết bị cũ và thanh toán bằng Bitcoin, hãy đến buổi gặp mặt gần bạn! Bằng cách trò chuyện với những người tham gia khác, chắc chắn bạn sẽ tìm được thiết bị phù hợp với mức giá tốt, đồng thời góp phần duy trì nền kinh tế tuần hoàn quanh Bitcoin. Đây cũng là cơ hội để bạn nhận được những lời khuyên bổ ích từ cộng đồng.





- Để kết nối Internet, tất nhiên bạn sẽ cần cáp Ethernet RJ45, ít nhất là để cài đặt hệ thống.





- Một số môi trường, chẳng hạn như Umbrel, cho phép bạn sử dụng Wi-Fi, nhưng hiệu suất thường sẽ kém hơn (đặc biệt nếu bạn muốn sử dụng nút Lightning từ xa, vì điều này có thể ảnh hưởng). Nếu bạn chọn Wi-Fi, hãy đảm bảo máy của bạn có card tích hợp hoặc thêm một thiết bị tương thích.





- Luôn sử dụng nguồn điện Supply chính hãng của nhà sản xuất cho máy của bạn. Điều này rất quan trọng để tránh hư hỏng thiết bị và ngăn ngừa nguy cơ hỏa hoạn.





- Nếu máy của bạn không có pin tích hợp, bạn nên đầu tư vào bộ biến tần để tránh tình trạng tắt máy đột ngột.





- Tùy thuộc vào giá trị thiết bị và vị trí địa lý của bạn, hệ thống chống sét cũng có thể phù hợp, có thể lắp trực tiếp tại bảng điện hoặc trên ổ cắm điện được sử dụng.





- Cuối cùng, hãy nhớ tối ưu hóa khả năng làm mát của máy: vệ sinh máy thường xuyên và lắp đặt máy ở nơi thoáng mát, thông gió tốt, gọn gàng để tránh tình trạng quá nhiệt, có thể dẫn đến hiện tượng giảm tốc độ (tự động giới hạn tốc độ bộ xử lý).



# Cài đặt nút Bitcoin dễ dàng


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: nhiều hơn một nút Bitcoin


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel là hệ điều hành máy chủ cá nhân được thiết kế để giúp việc tự lưu trữ trở nên dễ dàng: bạn cài đặt Umbrel, mở trình duyệt trên `umbrel.local` và quản lý mọi thứ thông qua một thiết bị điều khiển từ xa đơn giản Interface.



Dự án đầu tiên phổ biến ý tưởng về một nút Bitcoin và Lightning chỉ cần một cú nhấp chuột, sau đó mở rộng thành một "đám mây tại nhà" thực sự: lưu trữ tệp và ảnh, phát trực tuyến đa phương tiện, công cụ mạng, tự động hóa gia đình, AI cục bộ và hàng trăm ứng dụng có thể cài đặt từ App Store tích hợp.



Trong Umbrel, mỗi ứng dụng chạy trong một container Docker (cô lập, cập nhật nguyên tử, khởi động/dừng độc lập). Interface tập trung quyền truy cập vào tất cả các ứng dụng này, cung cấp tính năng đăng nhập một lần (với tùy chọn xác thực hai yếu tố), cập nhật hệ điều hành và ứng dụng chỉ bằng một cú nhấp chuột, giám sát trực tiếp máy (CPU, RAM, nhiệt độ, lưu trữ), quản lý quyền giữa các ứng dụng và tổng quan về mức tiêu thụ tài nguyên của chúng.



Do đó, mục tiêu của Umbrel là trao lại cho bạn quyền kiểm soát và bảo mật dữ liệu mà không cần dựa vào các dịch vụ đám mây, ngoài việc chỉ cần vận hành một nút Bitcoin.



### Umbrel Home so với umbrelOS



Umbrel cung cấp hai cách tiếp cận riêng biệt:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): Đây là một máy chủ mini sẵn sàng sử dụng, được thiết kế và tối ưu hóa đặc biệt cho umbrelOS. Nhỏ gọn, êm ái, kết nối Ethernet, được trang bị ổ SSD NVMe (tùy chọn lên đến 4TB), RAM 16GB và CPU lõi tứ. Chỉ cần đặt hàng, cắm điện và truy cập `umbrel.local`. Bạn có thể thiết lập và vận hành Umbrel chỉ trong vài phút. Đó chính là lựa chọn cắm và chạy.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): đây là hệ điều hành bạn có thể tự cài đặt trên phần cứng của mình (mini-PC, NUC, tower, máy tính xách tay chuyên dụng...). Bạn có cùng một Interface và cùng một App Store như trên Umbrel Home.



![Image](assets/fr/080.webp)



Trong cả hai trường hợp, trải nghiệm người dùng đều giống hệt nhau về mặt phần mềm: quản trị dựa trên trình duyệt, cập nhật chỉ bằng một cú nhấp chuột, cài đặt ứng dụng theo yêu cầu... Giải pháp tự lắp đặt thường tiết kiệm hơn so với việc mua Umbrel Home (tùy thuộc vào máy tính được sử dụng). Tuy nhiên, tôi không nhất thiết khuyên bạn luôn chọn giải pháp tự lắp đặt, vì **việc mua Umbrel Home đóng góp trực tiếp vào việc tài trợ cho quá trình phát triển dự án**, vì mô hình kinh doanh của nó dựa trên việc bán phần cứng. Và thẳng thắn mà nói, với mức giá 389 euro cho 2TB dung lượng lưu trữ, mức giá này vẫn rất hợp lý so với chất lượng của máy tính được cung cấp.



![Image](assets/fr/079.webp)



Trong chương tiếp theo, chúng ta sẽ tìm hiểu cách tự cài đặt umbrelOS trên máy tính của bạn. Tuy nhiên, bạn có thể tham khảo khóa học BTC 202 này theo cách tương tự nếu bạn đã chọn Umbrel Home.



### Trường hợp sử dụng: từ nút Bitcoin đến đám mây gia đình



Umbrel có thể giữ nguyên thiết kế tối giản và chỉ tập trung vào Bitcoin, hoặc phát triển thành một máy chủ cá nhân đa chức năng thực sự, tùy thuộc vào nhu cầu của bạn. Dưới đây là những ứng dụng chính của Umbrel:





- Nút Bitcoin đơn giản**: đây là ứng dụng nền tảng mà Umbrel đã dựa vào ngay từ đầu. Bạn có thể chạy Bitcoin core (hoặc Knots), kết nối ví trực tiếp với nút, hiển thị máy chủ Electrum, lưu trữ Mempool Block explorer để xem Blockchain và ước tính chi phí... Chúng ta sẽ tập trung vào những ứng dụng này trong khóa học này.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel cũng cho phép bạn triển khai LND hoặc Core Lightning, hai phiên bản triển khai của Lightning Network, để quản lý node Lightning của riêng bạn. Bạn sẽ có thể mở kênh, quản lý thanh khoản, thực hiện thanh toán, tự động cân bằng, cung cấp dịch vụ, kết nối Wallet từ xa hoặc tận dụng tính năng quản lý Interface tiên tiến nhờ vào nhiều ứng dụng có sẵn. Chúng ta sẽ xem xét trường hợp sử dụng cụ thể này trong khóa học LNP 202 tiếp theo.



![Image](assets/fr/083.webp)





- Tự lưu trữ chung**: với Nextcloud, Immich, Jellyfin/Plex, trình chặn quảng cáo toàn DNS (Pi-hole/AdGuard), VPN (WireGuard, Tailscale), tự động hóa nhà (Home Assistant), sao lưu, quản lý ghi chú, công cụ văn phòng, AI cục bộ (Ollama + Open WebUI)... Umbrel có thể trở thành máy chủ cá nhân của bạn, cho phép bạn lấy lại quyền kiểm soát dữ liệu. Bạn tự lưu trữ các dịch vụ bạn sử dụng hàng ngày, với trải nghiệm người dùng được trau chuốt gần giống với các giải pháp bên ngoài, đồng thời vẫn giữ được toàn quyền kiểm soát dữ liệu và quyền riêng tư của mình.



Bằng cách triển khai các ứng dụng trong vùng chứa, bạn có thể định hình Umbrel theo ý muốn: bắt đầu với một nút Bitcoin đơn giản và một vài ứng dụng được liên kết với hệ sinh thái của nó, sau đó cài đặt một nút Lightning cùng với nút Bitcoin của bạn và dần dần làm phong phú thêm phiên bản của bạn bằng các ứng dụng tự lưu trữ mà bạn cần.



### Cộng đồng và hỗ trợ lẫn nhau



Một trong những lợi thế chính của Umbrel so với các đối thủ cạnh tranh là cộng đồng người dùng đông đảo và năng động. Bạn có thể liên hệ với họ chủ yếu qua Discord (https://discord.gg/efNtFzqtdx) và diễn đàn trực tuyến (https://community.umbrel.com/). Tại đây, bạn không chỉ tìm thấy những lời khuyên thiết thực mà còn tìm thấy các giải pháp để giải quyết vấn đề hoặc sửa lỗi. Đây là một nơi tuyệt vời để bắt đầu, để phát triển và cuối cùng là để giúp đỡ những người dùng khác, vì vậy bạn sẽ không bị bỏ lại một mình với Coin của mình.



![Image](assets/fr/084.webp)



### Giấy phép UmbrelOS



Mã nguồn của Umbrel được công khai (bạn có thể xem Fork và chỉnh sửa nó), nhưng nó không được cấp phép theo giấy phép nguồn mở thực sự. Trên thực tế, umbrelOS được phân phối theo giấy phép [*PolyForm Noncommercial 1.0*] (https://polyformproject.org/licenses/noncommercial/1.0.0/), mặc dù một số công cụ phát triển liên quan được cung cấp theo giấy phép MIT.



Trên thực tế, bạn có thể làm bất cứ điều gì bạn muốn với umbrelOS, miễn là sử dụng cho mục đích cá nhân, phi thương mại: sửa đổi, phân phối lại cho mục đích phi lợi nhuận, tạo sản phẩm phái sinh cho chính bạn hoặc cho các tổ chức phi lợi nhuận, miễn là bạn tôn trọng các thông báo pháp lý.



Tuy nhiên, việc bán Umbrel hoặc các sản phẩm phái sinh của Umbrel (ví dụ: máy được lắp ráp sẵn với hệ điều hành umbrelOS), cung cấp các dịch vụ liên quan đến Umbrel cho mục đích thương mại hoặc tích hợp mã của Umbrel vào sản phẩm để kiếm lợi nhuận đều bị nghiêm cấm.



Về mặt kỹ thuật, giấy phép này không hạn chế việc cài đặt, kiểm tra hoặc điều chỉnh Umbrel cho mục đích sử dụng cá nhân. Về mặt pháp lý, giấy phép này bảo vệ dự án khỏi việc bán lại trái phép hoặc lưu trữ thương mại, đặc biệt là bởi các nhà cung cấp dịch vụ đám mây. Do đó, Umbrel không phải là mã nguồn mở, mặc dù mã nguồn của nó vẫn có thể truy cập công khai.



Tuy nhiên, mỗi ứng dụng trong Store đều có giấy phép riêng, thường là mã nguồn mở.




## Cài đặt Full node với Umbrel


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Bây giờ chúng ta đã có đầy đủ thông tin cần thiết, đã đến lúc đi sâu vào chi tiết. Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn cách cài đặt một node Bitcoin hoàn chỉnh bằng UmbrelOS.



### Vật liệu cần thiết



Ở đây, chúng tôi sẽ sử dụng ảnh UmbrelOS x86 (chính xác hơn là phiên bản x86_64). Bạn có thể làm theo hướng dẫn này trên bất kỳ máy tính nào bạn chọn, miễn là máy tính đó không được trang bị bộ xử lý kiến trúc ARM (không phải Apple Silicon, Raspberry Pi, v.v.). Điều này có nghĩa là bất kỳ máy tính nào có bộ xử lý Intel hoặc AMD 64-bit đều có thể đáp ứng, miễn là đáp ứng các yêu cầu tối thiểu, tùy thuộc vào cách bạn định sử dụng Umbrel (khuyến nghị ít nhất một bộ xử lý lõi kép).



Nếu bạn đã chọn Raspberry Pi 5 (một lựa chọn tôi không khuyến khích, như đã đề cập ở phần trước), quá trình cài đặt sẽ hơi khác một chút. Sau đó, bạn có thể làm theo hướng dẫn chuyên sâu này và quay lại khóa học của tôi sau khi truy cập trang web Interface `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Như đã đề cập ở phần trước, tôi đã chọn chạy hướng dẫn này trên một chiếc PC nhỏ đã tân trang mà tôi tìm thấy với mức giá tốt: *Lenovo ThinkCentre M900 Tiny* được trang bị bộ vi xử lý Intel Core i7 và RAM 16 GB. Đây là cấu hình rất thoải mái để chạy Umbrel, đặc biệt là đối với một node Bitcoin. Tuy nhiên, tôi chọn cấu hình này vì tôi muốn cài đặt một node Lightning và các ứng dụng đòi hỏi nhiều tài nguyên hơn sau này. Tôi cũng đã thêm một ổ SSD 2TB vào ThinkCentre của mình để giữ nguyên toàn bộ Blockchain và vẫn có một khoản dự phòng thoải mái. Với cấu hình này, tổng chi phí là 270 euro, bao gồm tất cả các chi phí.



![Image](assets/fr/001.webp)



Tôi đặc biệt thích dòng ThinkCentre Tiny của Lenovo vì chúng nhỏ gọn, êm ái và rất bền bỉ. Những chiếc máy tính này rất được ưa chuộng trong giới doanh nghiệp và do đó rất phổ biến trên thị trường máy tính cũ, nơi bạn có thể tìm thấy những cấu hình thú vị với mức giá từ 70 đến 200 euro.



Nếu, giống như tôi, bạn chọn máy tính không có màn hình, **bạn sẽ chỉ cần kết nối màn hình và bàn phím** trong suốt quá trình cài đặt. Sau đó, bạn có thể truy cập từ xa từ một máy tính khác cùng mạng (hoặc thông qua các phương pháp khác mà chúng tôi sẽ đề cập trong các chương sau). Bạn cũng cần một cáp Ethernet RJ45 để kết nối máy tính với mạng cục bộ và một ổ USB dung lượng ít nhất 4 GB để lưu trữ ảnh cài đặt.



Tóm lại, đây là các yêu cầu về thiết bị:




- Máy tính có bộ xử lý x86_64 (tối thiểu Dual-core, khuyến nghị Quad-core);
- Bộ nhớ RAM (tối thiểu 4 GB, khuyến nghị 8 GB trở lên để sử dụng lâu dài);
- SSD (khuyến nghị + 2 TB);
- Ổ USB (+ 4 GB) để cài đặt ảnh UmbrelOS;
- Màn hình và bàn phím (chỉ hữu ích cho lần cài đặt đầu tiên nếu máy tính không được trang bị);
- Cáp Ethernet RJ45.



### Bước 1 - Lắp máy tính



Tùy thuộc vào phần cứng bạn đã chọn, bước đầu tiên là lắp ráp các thành phần khác nhau của máy tính. Ví dụ, trong trường hợp của tôi, ổ SSD ban đầu chỉ có dung lượng 256 GB, vì vậy tôi sẽ tái chế nó để sử dụng cho mục đích khác và thay thế bằng ổ SSD 2 TB. Nếu bạn cũng muốn thay thế các mô-đun RAM, bây giờ là lúc để thực hiện.



### Bước 2: Chuẩn bị một ổ USB có thể khởi động



Trước khi cài đặt UmbrelOS trên máy tính, bạn cần tạo một ổ USB có thể khởi động chứa hệ điều hành. Tất cả các bước trong bước 2 phải được thực hiện trên máy tính cá nhân của bạn (và không phải trực tiếp trên máy tính được chỉ định làm node của bạn).





- Bắt đầu bằng cách tải xuống phiên bản UmbrelOS mới nhất ở định dạng USB:



Truy cập [trang web chính thức của Umbrel để tải xuống ảnh ISO](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) để cài đặt qua USB. Đảm bảo bạn chọn phiên bản tương thích với kiến trúc x86_64 (tệp có tên `umbrelos-amd64-usb-installer.iso`). Quá trình tải xuống có thể mất một chút thời gian vì ảnh ISO khá lớn.



![Image](assets/fr/002.webp)





- Cài đặt Balena Etcher:



Để tạo ổ USB có thể khởi động, bạn sẽ sử dụng một công cụ đa nền tảng đơn giản có tên là [Balena Etcher](https://www.balena.io/etcher/). Tải xuống và cài đặt trên máy tính của bạn.



![Image](assets/fr/003.webp)





- Cắm một ổ USB trống có dung lượng ít nhất 4 GB:



Cắm ổ USB vào máy tính (là ổ USB mà bạn vừa tải xuống UmbrelOS và Balena Etcher). **Cảnh báo: toàn bộ dữ liệu trên ổ USB sẽ bị xóa**. Hãy đảm bảo ổ USB không chứa bất kỳ tệp quan trọng nào.





- Ghi ảnh ISO vào ổ USB bằng Balena Etcher:



Khởi chạy Balena Etcher và chọn tệp ISO `umbrelos-amd64-usb-installer.iso` bạn vừa tải xuống bằng cách nhấp vào nút "*Flash from file*". Sau đó, chọn ổ USB làm thiết bị đích và nhấp vào "*Flash!*" để bắt đầu ghi.



![Image](assets/fr/004.webp)



Sau khi hoàn tất thao tác, bạn sẽ có một ổ USB có thể khởi động chứa UmbrelOS, sẵn sàng để khởi động và cài đặt Umbrel trên máy của bạn.



![Image](assets/fr/005.webp)



### Bước 3: Khởi động máy tính từ ổ USB



Bây giờ ổ USB có thể khởi động chứa UmbrelOS đã sẵn sàng, bạn có thể khởi động máy tính vào đó để bắt đầu cài đặt hệ thống. Rút ổ USB khỏi máy tính chính và cắm vào thiết bị bạn muốn cài đặt Umbrel và node Bitcoin.



Như đã giải thích ở đầu chương này, để hoàn tất quá trình cài đặt, bạn cần một thiết bị hiển thị và một thiết bị đầu vào. Kết nối màn hình qua HDMI (hoặc cổng khác, tùy thuộc vào máy tính của bạn) và kết nối bàn phím qua USB với máy tính. Những thiết bị này chỉ cần thiết cho quá trình cài đặt; bạn sẽ không cần chúng sau đó, vì Umbrel sẽ được truy cập từ xa từ một máy tính khác. Hãy kết nối hai thiết bị này với máy tính của bạn.



**Mẹo:** Nếu bạn không có màn hình ngoại vi ở nhà, bạn có thể sử dụng TV. Với đầu vào HDMI (hoặc loại khác), bạn có thể dùng TV làm màn hình tạm thời trong khi cài đặt hệ điều hành.



Umbrel rõ ràng yêu cầu kết nối Internet. Hãy kết nối cáp Ethernet RJ45 giữa thiết bị và bộ định tuyến của bạn.



![Image](assets/fr/006.webp)



Bật máy tính. Trong hầu hết các trường hợp, máy tính sẽ tự động phát hiện ổ USB và khởi động từ ổ USB đó. Sau đó, bạn sẽ thấy màn hình cài đặt UmbrelOS Interface xuất hiện.



Nếu thiết bị khởi động trên hệ thống khác hoặc hiển thị thông báo lỗi, điều này có thể có nghĩa là thiết bị không tự động khởi động từ ổ USB. Trong trường hợp này, hãy khởi động lại và vào cài đặt BIOS/UEFI (thường được truy cập bằng cách nhấn `DEL`, `F2`, `F12` hoặc `ESC`, tùy thuộc vào nhà sản xuất máy tính). Sau đó, hãy thay đổi thứ tự khởi động để ưu tiên ổ USB. Cuối cùng, khởi động lại thiết bị để chạy UmbrelOS.



### Bước 4: Cài đặt UmbrelOS trên máy tính của bạn



Sau khi thiết bị khởi động từ ổ USB, bạn sẽ thấy quá trình cài đặt UmbrelOS Interface. Bước này bao gồm việc cài đặt hệ thống trực tiếp vào ổ đĩa Hard bên trong máy.



Màn hình xuất hiện liệt kê tất cả các thiết bị lưu trữ nội bộ được máy tính phát hiện. Mỗi ổ đĩa đi kèm với một số, tên và dung lượng lưu trữ. Hãy tìm ổ đĩa bạn muốn cài đặt Umbrel. **Cảnh báo: tất cả các tệp trên ổ đĩa này sẽ bị xóa vĩnh viễn.**



![Image](assets/fr/007.webp)



Sau khi xác định đúng ổ đĩa (thường là ổ đĩa có dung lượng lớn nhất để chứa Blockchain), hãy ghi lại số được gán cho ổ đĩa đó. Ví dụ: nếu ổ đĩa bạn chọn hiển thị số `2`, chỉ cần nhập `2`, sau đó nhấn phím `Enter` trên bàn phím.



![Image](assets/fr/008.webp)



Chương trình sẽ định dạng ổ đĩa đã chọn, cài đặt UmbrelOS và tự động cấu hình hệ thống. Quá trình này có thể mất vài phút. Hãy để quá trình chạy mà không bị gián đoạn.



![Image](assets/fr/009.webp)



Khi quá trình cài đặt hoàn tất, bạn sẽ được nhắc tắt thiết bị. Nhấn phím bất kỳ để tắt máy tính.



![Image](assets/fr/010.webp)



Bây giờ bạn có thể tháo ổ USB, bàn phím và màn hình, những thứ không còn cần thiết cho Umbrel của bạn nữa. Tất cả những gì còn lại của thiết bị là nguồn Supply và cáp Ethernet RJ45.



![Image](assets/fr/011.webp)



Trước khi khởi động lại thiết bị, hãy kiểm tra hai điểm sau:





- Ổ USB không được rút ra**: nếu ổ USB vẫn được kết nối, hệ thống có thể khởi động lại trên ổ USB đó thay vì ổ đĩa bên trong;
- Cáp Ethernet đã được cắm vào**: thiết bị phải được kết nối với bộ định tuyến để hoạt động.



Nhấn nút nguồn. Hệ thống sẽ tự động khởi động từ ổ đĩa bên trong nơi UmbrelOS được cài đặt. Lần khởi động đầu tiên có thể mất khoảng **5 phút**. Trong thời gian này, Umbrel sẽ khởi tạo các dịch vụ và Interface.



Từ một máy tính khác (máy tính bạn dùng hàng ngày) được kết nối với **cùng mạng cục bộ**, hãy mở trình duyệt web (Firefox, Chrome...) và truy cập vào:



```
http://umbrel.local
```



Address này được sử dụng để truy cập người dùng đồ họa Umbrel Interface Interface từ xa và bắt đầu cấu hình.



Nếu Address `http://umbrel.local` không hoạt động trên trình duyệt của bạn sau khi đợi ít nhất 5 phút, chỉ cần thử:



```
http://umbrel
```



Nếu vẫn không được, hãy nhập địa chỉ IP cục bộ Address của Umbrel trực tiếp vào trình duyệt. Ví dụ (thay `42` bằng số máy tính của bạn đang lưu trữ Umbrel trên mạng cục bộ):



```
http://192.168.1.42
```



Để xác định IP Address của Umbrel, có một số phương pháp, từ đơn giản nhất đến tiên tiến nhất:





- Truy cập vào trang quản trị bộ định tuyến Interface và tìm IP Address của thiết bị Umbrel trên mạng cục bộ.





- Sử dụng phần mềm quét mạng như Angry IP Scanner để phát hiện các thiết bị được kết nối và định vị địa chỉ IP Address của Umbrel.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Cuối cùng, hãy kết nối lại màn hình và bàn phím với thiết bị, đăng nhập (tên đăng nhập mặc định: `umbrel`, mật khẩu: `umbrel`), sau đó nhập lệnh sau:



```
hostname -I
```



Bây giờ bạn đã sẵn sàng sử dụng Umbrel!



### Bước 5: Bắt đầu với Umbrel



Để bắt đầu cấu hình Umbrel, hãy nhấp vào nút "*Bắt đầu*".



![Image](assets/fr/013.webp)



#### Tạo một tài khoản



Chọn một bút danh hoặc nhập tên của bạn, sau đó đặt mật khẩu mạnh. Hãy cẩn thận: mật khẩu này là rào cản duy nhất bảo vệ quyền truy cập vào Umbrel của bạn từ mạng của bạn (và do đó, có khả năng là cả bitcoin của bạn nếu bạn chạy một nút Lightning trên Umbrel). Nó cũng bảo vệ quyền truy cập từ xa qua Tor hoặc VPN, nếu các dịch vụ này được bật.



Chọn mật khẩu mạnh và đảm bảo bạn giữ ít nhất một bản sao lưu (khuyến khích sử dụng trình quản lý mật khẩu).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Sau khi nhập mật khẩu, hãy nhấp vào nút "*Tạo*".



![Image](assets/fr/014.webp)



Cấu hình Umbrel của bạn hiện đã hoàn tất.



![Image](assets/fr/015.webp)



#### Khám phá Interface



Interface của Umbrel khá trực quan:





- Trên trang chủ, bạn có thể xem các ứng dụng và tiện ích đã cài đặt.



![Image](assets/fr/016.webp)





- "*App Store*" cho phép bạn cài đặt các ứng dụng mới,



![Image](assets/fr/017.webp)





- Menu "*Tệp*" tập trung tất cả tài liệu được lưu trữ trên Umbrel của bạn.



![Image](assets/fr/018.webp)





- Menu "*Cài đặt*" cho phép bạn sửa đổi cài đặt của Umbrel và truy cập thông tin của nó, bao gồm:
    - Cập nhật, khởi động lại hoặc dừng máy của bạn;
    - Tham khảo dung lượng lưu trữ khả dụng, mức sử dụng RAM và nhiệt độ bộ xử lý;
    - Thay đổi hình nền;
    - Quản lý quyền truy cập từ xa qua Tor, kích hoạt Wi-Fi hoặc 2FA.



![Image](assets/fr/019.webp)



#### Cài đặt bảo mật và kết nối



Trước hết, tôi thực sự khuyên bạn nên bật xác thực hai yếu tố (2FA). Điều này tăng thêm mức bảo mật Layer cho mật khẩu của bạn. Nó gần như không thể thiếu nếu bạn định sử dụng Umbrel để lưu trữ tệp cá nhân, chạy nút Lightning hoặc thực hiện bất kỳ hoạt động nhạy cảm nào khác.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Để thực hiện việc này, hãy nhấp vào ô tương ứng trong phần cài đặt.



![Image](assets/fr/020.webp)



Sau đó, quét mã QR được hiển thị bằng ứng dụng xác thực của bạn. Sau đó, nhập mã động gồm 6 chữ số vào trường được cung cấp trên Umbrel của bạn.



Từ bây giờ, mọi kết nối mới tới Umbrel của bạn sẽ yêu cầu cả mật khẩu và mã 6 chữ số do ứng dụng xác thực hai yếu tố (2FA) của bạn tạo ra.



![Image](assets/fr/021.webp)



Về việc truy cập từ xa qua Tor, nếu bạn không cần, tôi khuyên bạn nên tắt tùy chọn này để hạn chế nguy cơ tấn công vào Umbrel. Theo mặc định, nút của bạn chỉ có thể được truy cập từ một máy tính được kết nối với cùng mạng cục bộ. Tuy nhiên, việc bật quyền truy cập qua Tor vẫn cho phép bạn quản lý Umbrel khi đang di chuyển.



Nếu bạn bật tính năng này, về mặt lý thuyết, bất kỳ máy nào trên thế giới cũng có thể kết nối đến nút của bạn, miễn là nó biết Tor Address. Tuy nhiên, mật khẩu và xác thực hai yếu tố (2FA) của bạn vẫn sẽ được bảo vệ.



Nếu bạn kích hoạt tùy chọn này, hãy đảm bảo rằng bạn đã bật xác thực hai yếu tố (2FA), mật khẩu mạnh và không bao giờ tiết lộ kết nối Tor của bạn Address.



Chỉ cần nhập Tor Address này vào trình duyệt Tor của bạn để truy cập Interface của Umbrel từ bất kỳ mạng nào.



![Image](assets/fr/026.webp)



Cuối cùng, trên trang cài đặt này, bạn cũng có thể kích hoạt kết nối Wi-Fi. Nếu máy chủ Umbrel của bạn có card mạng Wi-Fi hoặc thiết bị phát Wi-Fi, bạn có thể truy cập Internet mà không cần dùng cáp RJ45. Tuy nhiên, tùy thuộc vào cấu hình của bạn, giải pháp này có thể làm chậm kết nối, ảnh hưởng đến quá trình đồng bộ hóa ban đầu (IBD) và việc sử dụng node trong tương lai (ví dụ: cho giao dịch Lightning). Cá nhân tôi không khuyến nghị tùy chọn này, vì node không dành cho thiết bị di động: nó luôn được truy cập từ xa, vì vậy tốt nhất là bạn nên cắm nó vào nguồn điện.



### Bước 6: Cài đặt nút Bitcoin trên Umbrel



Bây giờ UmbrelOS đã được cài đặt và cấu hình chính xác trên máy của bạn, bạn có thể tiến hành cài đặt nút Bitcoin. Không gì đơn giản hơn: vào App Store, mở danh mục "*Bitcoin*", sau đó chọn ứng dụng "*Bitcoin Node*" (thực ra là Bitcoin core).



![Image](assets/fr/022.webp)



Sau đó nhấp vào nút "*Cài đặt*".



![Image](assets/fr/023.webp)



Sau khi cài đặt hoàn tất, nút Bitcoin của bạn sẽ khởi chạy IBD (*Tải xuống khối ban đầu*): nút này sẽ tải xuống và xác thực tất cả các giao dịch và khối kể từ khi Bitcoin được tạo vào năm 2009.



![Image](assets/fr/024.webp)



Giai đoạn này đặc biệt tốn thời gian, vì thời lượng của nó phụ thuộc vào nhiều yếu tố, bao gồm dung lượng RAM được phân bổ cho bộ nhớ đệm nút, tốc độ ổ đĩa, tốc độ kết nối Internet và sức mạnh bộ xử lý. Do đó, phạm vi thời gian rất rộng, tùy thuộc vào cấu hình. Với một PC hiệu năng cao (SSD NVMe, RAM +32 GB, bộ xử lý mạnh mẽ và kết nối Internet tốt), IBD có thể hoàn thành trong khoảng mười giờ. Mặt khác, một bộ xử lý cũ, RAM yếu, hoặc thậm chí tệ hơn, một ổ đĩa cơ Hard (không khuyến khích sử dụng) có thể kéo dài quá trình này đến vài tuần.



Với một chiếc PC có cấu hình bình thường (bộ xử lý tốt, RAM 8 đến 16 GB và ổ SSD), máy có thể hoạt động được khoảng 2 đến 7 ngày.



Để tăng tốc IBD một chút, bạn có thể tăng RAM được phân bổ cho bộ nhớ đệm nút (chủ yếu được sử dụng cho bộ UTXO, chúng ta sẽ xem xét lại sau trong khóa học) thông qua tham số `dbcache`. Trên Umbrel, việc điều chỉnh này được thực hiện trong tham số nút của bạn, trong tab "*Tối ưu hóa*".



![Image](assets/fr/025.webp)



Theo mặc định, giá trị của tham số `dbcache` trong Bitcoin core được đặt thành 450 MiB, tương đương khoảng 472 MB. Bằng cách tăng giá trị này, bạn có thể tăng tốc IBD một chút. Tuy nhiên, tôi không nhất thiết khuyến nghị tăng giá trị này quá cao: ngay cả khi đặt nó lên 4 GiB, tốc độ đồng bộ hóa cũng chỉ nhanh hơn khoảng 10% và có thể khiến bạn mất thời gian nếu bị gián đoạn trong quá trình IBD.



Hãy cẩn thận không phân bổ giá trị quá lớn cho máy của bạn. Nếu RAM khả dụng cho UmbrelOS hết, nút của bạn có thể dừng đột ngột, làm gián đoạn IBD và yêu cầu bạn phải khởi động lại thủ công, gây mất thời gian đáng kể.



Để tìm hiểu thêm về tác động của tham số `dbcache` đối với quá trình đồng bộ hóa ban đầu, tôi khuyên bạn nên xem phân tích này của Jameson Lopp: [*Ảnh hưởng của kích thước DBcache đến tốc độ đồng bộ hóa nút Bitcoin*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Sau khi quá trình IBD của nút hoàn tất (đồng bộ hóa 100%), giờ đây bạn đã có một nút Bitcoin hoạt động hoàn chỉnh. Xin chúc mừng, giờ đây bạn đã là một phần không thể thiếu của mạng lưới Bitcoin!



![Image](assets/fr/027.webp)



Trong phần tiếp theo, chúng ta sẽ khám phá cách sử dụng thực tế nút mới của bạn: cách kết nối Wallet với nút này và những ứng dụng nào bạn nên cài đặt để trở thành một Bitcoiner có chủ quyền.





# Kết nối Wallet với nút của bạn


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Người lập chỉ mục: vai trò, hoạt động và giải pháp


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Nếu bạn đã tìm hiểu về các node Bitcoin trước khi tham gia khóa học này, bạn có thể đã từng gặp thuật ngữ "indexer". Đây là những công cụ như Electrs hoặc Fulcrum, có thể được thêm vào node Bitcoin core. Nhưng vai trò chính xác của chúng là gì? Chúng hoạt động như thế nào trong thực tế? Và bạn có nên cài đặt một công cụ như vậy trên node Bitcoin mới của mình không? Đó là những gì chúng ta sẽ tìm hiểu trong chương này.



### Người lập chỉ mục là gì?



Nói chung, một chương trình lập chỉ mục là một chương trình quét một tập hợp dữ liệu thô, trích xuất các khóa liên quan (chẳng hạn như từ, mã định danh và địa chỉ) và xây dựng một tệp phụ, được gọi là "chỉ mục", trong đó mỗi khóa tham chiếu đến vị trí chính xác của dữ liệu trong kho ngữ liệu. Giai đoạn tiền xử lý này sử dụng thời gian CPU và cần một số dung lượng đĩa, nhưng nó loại bỏ nhu cầu xử lý toàn bộ kho ngữ liệu mỗi khi cơ sở dữ liệu được truy vấn; chỉ cần truy vấn chỉ mục là có thể nhận được phản hồi gần như ngay lập tức.



Nói một cách dễ hiểu, nguyên tắc này giống như mục lục trong sách: nếu bạn đang tìm kiếm một thông tin cụ thể, thay vì đọc lại toàn bộ cuốn sách, bạn sẽ tham khảo mục lục để tìm trực tiếp trang có thông tin bạn đang tìm.



Trong một nút Bitcoin, chẳng hạn như Bitcoin core, dữ liệu Blockchain được lưu trữ ở dạng thô, theo thứ tự thời gian. Mỗi khối chứa các giao dịch, sau đó chứa các đầu vào và đầu ra, mà không có bất kỳ phân loại cụ thể nào theo Address, mã định danh hoặc Wallet. Tổ chức tuyến tính này được tối ưu hóa cho việc xác thực khối, nhưng không phù hợp cho các tìm kiếm có mục tiêu. Ví dụ: nếu bạn muốn tìm tất cả các giao dịch được liên kết với một Address cụ thể trong một nút không được lập chỉ mục, bạn sẽ phải xem xét thủ công toàn bộ Blockchain, từng khối và từng giao dịch. Đây chính xác là lúc bộ lập chỉ mục trên nút Bitcoin của bạn phát huy tác dụng.



![Image](assets/fr/085.webp)



Trình lập chỉ mục là một chương trình phần mềm chuyên dụng phân tích khối dữ liệu thô này (bộ Blockchain, Mempool, UTXO) và trích xuất các khóa, chẳng hạn như mã định danh giao dịch, địa chỉ và chiều cao khối. Từ các khóa này, chương trình sẽ xây dựng chỉ mục, liên kết từng khóa với vị trí chính xác của thông tin trong bộ nhớ của nút.



![Image](assets/fr/086.webp)



Việc lập chỉ mục cho phép bạn tìm kiếm thông tin trên nút của mình một cách nhanh chóng, chính xác và hiệu quả. Ví dụ: khi bạn kết nối một Wallet như Sparrow với nút của mình, nó có thể hiển thị số dư của Address gần như ngay lập tức. Cụ thể, nó sẽ truy vấn trình lập chỉ mục bằng một yêu cầu như: "_Những UTXO nào được liên kết với tập lệnh Hash này?_". Trình lập chỉ mục phản hồi gần như ngay lập tức, mà không cần phải đọc lại toàn bộ Blockchain, vì dữ liệu này đã được liệt kê trong cơ sở dữ liệu của nó.



### Bitcoin core có bộ lập chỉ mục không?



Nếu không cần phần mềm bổ sung, Bitcoin core, nói một cách chính xác, không cung cấp một trình lập chỉ mục Address hoàn chỉnh tương đương với các phần mềm như Electrs hoặc Fulcrum. Tuy nhiên, nó tích hợp một số cơ chế lập chỉ mục nội bộ, cũng như các tùy chọn để mở rộng khả năng truy vấn. Để hiểu đầy đủ tình hình, chúng ta cần xem xét lại lịch sử của dự án.



Cho đến phiên bản 0.8.0 của Bitcoin core, việc xác thực giao dịch dựa trên một chỉ mục giao dịch toàn cục, được gọi là `txindex`. Chỉ mục này tham chiếu đến tất cả các giao dịch Blockchain và đầu ra của chúng. Khi một nút nhận được một giao dịch mới, nó sẽ tham khảo chỉ mục này để xác minh rằng các đầu ra đã sử dụng (trong đầu vào) thực sự tồn tại và chưa được chi tiêu. Do đó, `txindex` là không thể thiếu cho việc xác thực giao dịch vào thời điểm đó.



Tuy nhiên, cách tiếp cận này có những hạn chế: chậm, tốn kém về mặt lưu trữ và dư thừa thông tin. Để khắc phục điều này, phiên bản 0.8.0 giới thiệu một bản đại tu mô hình xác thực có tên là ***Ultraprune***. Thay vì lưu trữ mọi thứ dưới dạng chỉ mục giao dịch, Bitcoin core duy trì một cơ sở dữ liệu đơn giản dành riêng cho UTXO, được gọi là `chainstate` (trong ngôn ngữ thông thường, nó được gọi là "bộ UTXO"), và cập nhật danh sách của nó khi các đầu ra được sử dụng và tạo ra.



Phương pháp này nhanh hơn nhiều và chỉ lưu trữ trạng thái hiện tại của thanh ghi, khiến cho bộ lập chỉ mục `txindex` trở nên không cần thiết. Tuy nhiên, thay vì xóa mã `txindex`, các nhà phát triển đã chọn giữ chức năng này đằng sau một tham số đơn giản (`txindex=1`). Bằng cách bật tùy chọn này trên nút của bạn, bạn có thể truy vấn bất kỳ giao dịch nào từ `txid` của nó.



Trái với suy nghĩ thông thường, Bitcoin core không cung cấp tính năng lập chỉ mục dựa trên Address như Electrs hay Fulcrum. Có một số lý do cho lựa chọn này:





- Vai trò của Bitcoin core không phải là trở thành một Block explorer hoàn chỉnh, cũng không phải là cung cấp một API được thiết kế riêng cho từng mục đích sử dụng. Việc tích hợp một chỉ mục dựa trên Address sẽ dẫn đến một Commitment cần được bảo trì dài hạn, vượt ra ngoài phạm vi ban đầu của phần mềm.





- Hầu hết các trường hợp sử dụng đều có thể được đề cập theo những cách khác. Ví dụ: để ước tính số dư của Address, bạn có thể sử dụng lệnh `scantxoutset`, lệnh này sẽ truy vấn trực tiếp tập hợp UTXO mà không cần lập chỉ mục đầy đủ.





- Mỗi chương trình phần mềm đều có những yêu cầu cụ thể về định dạng hoặc loại dữ liệu cần lập chỉ mục (Address, tập lệnh Hash, thẻ độc quyền, v.v.). Sẽ linh hoạt và hợp lý hơn khi để các chương trình này tự xây dựng chỉ mục tùy chỉnh thay vì áp dụng giải pháp chung chung trong Bitcoin core.



Bitcoin core có một bộ lập chỉ mục giao dịch tùy chọn (`txindex`), một dấu tích của hoạt động lịch sử, nhưng nó không cung cấp chỉ mục Address, cũng không cung cấp Interface trực tiếp cho các tìm kiếm phức tạp. Do đó, trong một số trường hợp, việc thêm một bộ lập chỉ mục bên ngoài có thể hữu ích.



### Bạn có nên thêm trình lập chỉ mục Address vào nút của mình không?



Việc thêm bộ lập chỉ mục Address, chẳng hạn như Electrs hoặc Fulcrum, không phải là bắt buộc; điều này phụ thuộc vào nhu cầu cụ thể của bạn.



Nếu bạn chỉ muốn kết nối Wallet, chẳng hạn như Sparrow, với nút của mình để xem số dư và phát sóng giao dịch, bạn hoàn toàn có thể thực hiện trực tiếp thông qua Interface RPC của Bitcoin core, cục bộ hoặc từ xa qua Tor.



Mặt khác, để sử dụng phần mềm tiên tiến hơn, chẳng hạn như chạy Mempool. Tại địa phương, việc cài đặt trình lập chỉ mục Address trở nên không thể thiếu đối với không gian Block explorer.



Bộ lập chỉ mục cần một khoảng thời gian đồng bộ hóa nhất định (ít hơn IBD) và sẽ chiếm thêm dung lượng ổ đĩa. Nếu ổ SSD của bạn vẫn còn đủ dung lượng trống sau khi tải xuống Blockchain, bạn có thể dễ dàng thêm bộ lập chỉ mục.



### Nên chọn công cụ lập chỉ mục nào?



Hai chương trình phần mềm thường được sử dụng để xây dựng loại chỉ mục Address này và giúp nó dễ truy cập: **Electrs** và **Fulcrum**. Các công cụ này lập chỉ mục Blockchain theo script-Hash (địa chỉ) và sau đó đề xuất một Interface được chuẩn hóa (giao thức Electrum), mà nhiều ví như Electrum Wallet, Sparrow hoặc Phoenix kết nối.



![Image](assets/fr/087.webp)



Nói một cách đơn giản, Electrs khá gọn nhẹ: nó lập chỉ mục Blockchain nhanh hơn và chiếm ít dung lượng đĩa hơn, nhưng hiệu suất truy vấn kém hơn một chút so với Fulcrum. Ngược lại, Fulcrum chiếm nhiều dung lượng đĩa hơn và mất nhiều thời gian lập chỉ mục hơn, nhưng hiệu suất truy vấn lại vượt trội hơn.



Đối với mục đích sử dụng cá nhân, tôi khuyên dùng Electrs: nó chiếm ít dung lượng hơn, được bảo trì tốt, và mặc dù hơi chậm hơn Fulcrum trong một số yêu cầu, nhưng vẫn quá đủ cho nhu cầu sử dụng hàng ngày. Nếu bạn có thời gian và dung lượng ổ đĩa, bạn cũng có thể dùng thử Fulcrum, nó sẽ hoạt động tốt hơn đáng kể, đặc biệt là trên các ví có nhiều địa chỉ cần xác minh.



Cụ thể, vào tháng 8 năm 2025, Electrs sẽ cần khoảng 56 GB dung lượng lưu trữ, so với khoảng 178 GB của Fulcrum. Do đó, lựa chọn trình lập chỉ mục của bạn cũng phụ thuộc vào dung lượng lưu trữ của bạn:




- Nếu dung lượng đĩa của bạn rất hạn chế, bạn sẽ phải sử dụng Bitcoin core mà không cần trình lập chỉ mục Address bên ngoài.
- Nếu bạn muốn sử dụng công cụ lập chỉ mục nhưng vẫn bị hạn chế về năng lực, hãy chọn Electrs.
- Nếu bạn có đủ dung lượng đĩa, Fulcrum có thể là thứ bạn đang tìm kiếm.



Trong phần còn lại của khóa học BTC 202 này, tôi sẽ sử dụng Electrs, nhưng bạn có thể dễ dàng làm theo với Fulcrum: quy trình cài đặt giống hệt nhau, cũng như kết nối Interface với Wallet, vì cả hai đều hiển thị máy chủ Electrum.



### Làm thế nào để cài đặt trình lập chỉ mục trên Umbrel?



Để cài đặt Electrs (hoặc Fulcrum) trên Umbrel của bạn, quy trình rất đơn giản: vào App Store, tìm kiếm ứng dụng có liên quan (nằm trong tab Bitcoin), sau đó nhấp vào nút "*Cài đặt*".



![Image](assets/fr/028.webp)



Sau khi quá trình cài đặt hoàn tất, Electrs sẽ tiến hành giai đoạn đồng bộ hóa (lập chỉ mục), có thể mất vài giờ.



![Image](assets/fr/029.webp)



Sau khi quá trình đồng bộ hóa hoàn tất, bạn có thể kết nối phần mềm Wallet với máy chủ Electrum được lưu trữ trên Umbrel.



## Làm thế nào để kết nối Wallet với nút Bitcoin của tôi?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Giờ bạn đã có một node Bitcoin hoàn chỉnh, đã đến lúc tận dụng nó! Trong chương tiếp theo, chúng ta sẽ khám phá những ứng dụng tiềm năng khác cho instance Umbrel của bạn. Tuy nhiên, hãy bắt đầu với những điều cơ bản: kết nối phần mềm Wallet của bạn để sử dụng thông tin từ Blockchain và phân phối giao dịch thông qua node của riêng bạn.



Như đã đề cập ở trên, có hai giao diện kết nối chính:




- Kết nối trực tiếp tới Bitcoin core thông qua RPC;
- Hoặc kết nối với máy chủ Electrum (Electrs hoặc Fulcrum).



Trong hướng dẫn này, chúng ta sẽ tập trung vào việc kết nối với nút của bạn qua Tor, vì đây là một giải pháp vừa đơn giản vừa an toàn cho người mới bắt đầu. Tôi thực sự khuyên bạn không nên để lộ cổng RPC của nút, vì việc cấu hình sai có thể gây ra rủi ro đáng kể cho tính bảo mật và an toàn của dữ liệu. Nhược điểm chính của giao tiếp qua Tor là tốc độ chậm. Trong chương tiếp theo, chúng ta sẽ khám phá một giải pháp thay thế nhanh chóng và an toàn cho Tor để truy cập từ xa vào nút của bạn: VPN.



Chúng tôi sẽ sử dụng Sparrow làm ví dụ trong chương này, nhưng quy trình này cũng tương tự đối với tất cả các phần mềm quản lý Wallet khác chấp nhận kết nối đến máy chủ Electrum. Chỉ cần tìm cài đặt tương ứng trong tham số ứng dụng của bạn (thường nằm trong "*Server*", "*Network*", "*Node*"...).



Trên Sparrow, mở tab "*File*" và vào menu "Settings".



![Image](assets/fr/030.webp)



Sau đó nhấp vào "*Máy chủ*" để truy cập các thông số kết nối.



![Image](assets/fr/031.webp)



Sau đó, bạn sẽ khám phá ra ba tùy chọn để liên kết phần mềm của mình với một nút Bitcoin:




- Máy chủ công cộng* (màu vàng): theo mặc định, nếu bạn không sở hữu node Bitcoin, tùy chọn này sẽ kết nối bạn với một node công cộng mà bạn không sở hữu (thường là của công ty). Tùy chọn này không liên quan ở đây, vì bạn đã có node riêng trên Umbrel.
- Bitcoin core* (Green): tùy chọn này tương ứng với kết nối qua Interface RPC, tức là trực tiếp tới Bitcoin core.
- Electrum riêng tư* (màu xanh): tùy chọn này cho phép bạn kết nối thông qua Máy chủ Electrum Interface của người lập chỉ mục (Electrs hoặc Fulcrum).



### Kết nối với Bitcoin core RPC



Nếu nút Umbrel của bạn không có bộ lập chỉ mục, đây là tùy chọn bạn cần chọn. Trên Sparrow, hãy nhấp vào "*Bitcoin core*".



![Image](assets/fr/032.webp)



Sau đó, bạn sẽ cần nhập một số thông tin để thiết lập kết nối với nút của mình. Tất cả dữ liệu này có thể được truy cập từ ứng dụng "*Bitcoin Node*" trên Umbrel bằng cách nhấp vào nút "*Kết nối*" ở góc trên bên phải của Interface.



![Image](assets/fr/033.webp)



Tab "*Chi tiết RPC*" hiển thị tất cả thông tin cần thiết cho kết nối. Chọn kết nối qua Tor Address (trong `.onion`).



![Image](assets/fr/034.webp)



Nhập các dữ liệu này vào các trường tương ứng trên Sparrow wallet, sau đó nhấp vào nút "*Kiểm tra kết nối*".



![Image](assets/fr/035.webp)



Nếu kết nối thành công, tín hiệu Green và thông báo xác nhận sẽ xuất hiện.



![Image](assets/fr/036.webp)



Dấu tích ở góc dưới bên phải của Interface Sparrow wallet bây giờ sẽ là Green (chỉ ra kết nối trực tiếp tới Bitcoin core).



**Lưu ý:** Để kết nối thành công, nút của bạn phải được đồng bộ hóa 100%. Nếu chưa, vui lòng đợi đến khi kết thúc IBD.



### Kết nối với Electrs



Nếu nút của bạn có bộ lập chỉ mục, tốt hơn là kết nối với nó thay vì sử dụng trực tiếp Bitcoin core, vì các truy vấn của bạn sẽ được xử lý nhanh hơn.



Trên Sparrow, hãy chuyển đến tab "*Private Electrum*".



![Image](assets/fr/037.webp)



Sau đó, bạn sẽ cần nhập một số thông tin để thiết lập kết nối với người lập chỉ mục. Bạn sẽ tìm thấy dữ liệu này trong ứng dụng "*Electrs*" (hoặc, nếu có, "*Fulcrum*") trên Umbrel.



Chọn tab "*Tor*" để lấy kết nối `.onion` Address. Nếu bạn muốn kết nối phần mềm di động Wallet, bạn cũng có thể quét trực tiếp mã QR.



![Image](assets/fr/038.webp)



Chỉ cần nhập Tor Address của máy chủ Electrum vào trường "*URL*", sau đó nhấp vào nút "*Kiểm tra kết nối*".



![Image](assets/fr/039.webp)



Nếu kết nối thành công, dấu kiểm và thông báo xác nhận sẽ hiển thị.



![Image](assets/fr/040.webp)



Dấu tích ở góc dưới bên phải của Interface Sparrow wallet sẽ chuyển sang màu xanh lam (màu liên quan đến kết nối với máy chủ Electrum).



**Lưu ý:** Để kết nối hoạt động, trình lập chỉ mục của bạn phải được đồng bộ hóa 100%. Nếu chưa, hãy đợi cho đến khi quá trình lập chỉ mục hoàn tất.



Giờ bạn đã biết cách kết nối Wallet với node Bitcoin! Trong chương tiếp theo, tôi sẽ giới thiệu cho bạn một số ứng dụng bổ sung có sẵn trên Umbrel mà tôi đặc biệt yêu thích, giúp bạn nâng cao khả năng sử dụng Bitcoin hàng ngày thông qua node của mình.




## Tổng quan về các ứng dụng có sẵn


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel cung cấp một kho ứng dụng phong phú. Như bạn sẽ thấy, có rất nhiều công cụ liên quan đến Bitcoin, nhưng cũng có rất nhiều ứng dụng đa dạng trong các lĩnh vực rất khác nhau: giải pháp tự lưu trữ cho dịch vụ và tệp, ứng dụng năng suất, công cụ tài chính tổng quát hơn, quản lý phương tiện, bảo mật và quản trị mạng, phát triển, trí tuệ nhân tạo, mạng xã hội, và thậm chí cả tự động hóa nhà ở.



Trong khóa học BTC 202 này, chúng ta sẽ tập trung hoàn toàn vào các ứng dụng liên quan đến Bitcoin. Tuy nhiên, bạn có thể thoải mái khám phá phần còn lại của danh mục để tìm các công cụ có thể hữu ích cho bạn.



Tất nhiên, việc liệt kê tất cả các ứng dụng của Bitcoin ở đây là không thể. Trong chương này, tôi muốn giới thiệu cho bạn những công cụ thiết yếu giúp bạn sử dụng Bitcoin dễ dàng và hiệu quả hơn.



### Mempool.không gian



Trong quá trình sử dụng Bitcoin hàng ngày, nếu có một công cụ thực sự không thể thiếu, thì đó chính là Block explorer. Dù truy cập trực tuyến hay cài đặt cục bộ, công cụ này đều chuyển đổi dữ liệu thô của Blockchain thành định dạng có cấu trúc, rõ ràng và dễ đọc. Công cụ này cũng tích hợp công cụ tìm kiếm cho phép người dùng nhanh chóng tìm thấy một khối, giao dịch hoặc Address cụ thể.



Cụ thể, trình khám phá cho phép bạn ước tính phí cần thiết để giao dịch của bạn được đưa vào một khối, sau đó theo dõi tiến trình của nó: tìm hiểu xem giao dịch đó có khả năng được đưa vào trong tương lai gần hay không, tùy thuộc vào thị trường phí, và cuối cùng xác nhận rằng giao dịch đó thực sự đã được đưa vào một khối. Nó cũng cung cấp khả năng phân tích các giao dịch trước đây của bạn và tham khảo lịch sử của chúng. Tóm lại, nó giống như con dao đa năng của người dùng bitcoin.



Như đã đề cập trước đó, trình duyệt có thể được lưu trữ trực tuyến trên một trang web hoặc chạy cục bộ trên máy tính của bạn. Một nhược điểm lớn của các dịch vụ trực tuyến là chúng có thể xâm phạm quyền riêng tư của bạn. Nếu không có VPN hoặc Tor, máy chủ lưu trữ trình duyệt có thể liên kết IP Address của bạn với các giao dịch bạn đang xem, điều này có thể cung cấp một điểm vào lý tưởng cho phân tích chuỗi.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Hơn nữa, Nhà cung cấp dịch vụ Internet (ISP) của bạn có thể biết bạn đang xem một giao dịch cụ thể thông qua trang web Block explorer. Điều này cũng đặt ra vấn đề về lòng tin: bạn phải tin tưởng vào dịch vụ trực tuyến để cung cấp thông tin chính xác về các giao dịch của mình mà không thể tự mình xác minh tính xác thực của thông tin đó.



Đó là lý do tại sao tốt nhất nên sử dụng Block explorer cục bộ của bạn. Bằng cách này, dữ liệu liên quan đến hoạt động tìm kiếm của bạn sẽ không bị rò rỉ, vì tất cả các truy vấn đều được xử lý trực tiếp trên máy do bạn kiểm soát, không cần thông qua Internet. Hơn nữa, trình khám phá cục bộ dựa trên dữ liệu từ nút Bitcoin của bạn, mà bạn đã tự xác thực theo quy tắc riêng của mình và bạn có thể tin tưởng.



Umbrel cung cấp một số trình khám phá khối:




- Mempool.Không gian
- Bitfeed
- Máy thám hiểm BTC RPC



Tôi đặc biệt thích Mempool.Space, mà tôi đã cài đặt trên node của mình. Xin lưu ý: để sử dụng hầu hết các trình khám phá khối trên Umbrel, cần có trình lập chỉ mục Address. Do đó, bạn cần ứng dụng Node Bitcoin (hoặc Bitcoin Knots), có Blockchain được đồng bộ hóa 100%, cũng như một trình lập chỉ mục như Electrs hoặc Fulcrum, cũng được đồng bộ hóa 100%.



Sau khi cài đặt ứng dụng, bạn chỉ cần mở ứng dụng để truy cập trình khám phá của riêng bạn.



![Image](assets/fr/041.webp)



Để tìm hiểu thêm về cách sử dụng Mempool.Space explorer, tôi xin giới thiệu hướng dẫn toàn diện này:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Nút sét



Bây giờ bạn đã có nút Bitcoin của riêng mình, bạn cũng có thể thiết lập nút Lightning để thực hiện giao dịch off-chain mà không cần dựa vào cơ sở hạ tầng của bên thứ ba.



Umbrel cung cấp một số ứng dụng giúp bạn thiết lập và vận hành nút Lightning. Bạn có thể lựa chọn giữa hai cách triển khai chính:




- LND, thông qua ứng dụng *Lightning Node*;
- Lõi sét.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Sau đó, bạn có thể quản lý nút của mình từ Interface chính, hoặc để có chức năng tốt hơn và các tùy chọn nâng cao hơn, hãy cài đặt *Ride The Lightning* hoặc *ThunderHub*. Các công cụ này sẽ cung cấp cho bạn một hệ thống quản lý Interface dựa trên web toàn diện hơn nhiều cho nút của bạn.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Cuối cùng, tôi khuyên bạn nên sử dụng ứng dụng *Lightning Network+*, ứng dụng này cho phép bạn tìm kiếm những người ngang hàng để mở kênh, cho phép thực hiện cả giao dịch tiền mặt đi và đến.



![Image](assets/fr/089.webp)



Nhờ Umbrel, việc quản lý một node Lightning cá nhân đã được đơn giản hóa đáng kể, nhưng vẫn còn tương đối phức tạp. Vì lý do này, chúng ta sẽ xem xét kỹ hơn chủ đề này trong một khóa học sắp tới dành riêng cho việc sử dụng này.



### Vảy đuôi



Một ứng dụng khác tôi đặc biệt thích trên Umbrel là Tailscale. Đây là một ứng dụng VPN được thiết kế để đơn giản hóa việc tạo mạng an toàn giữa nhiều thiết bị, bất kể chúng ở đâu trên thế giới. Không giống như các VPN truyền thống, vốn dựa vào các máy chủ tập trung, Tailscale sử dụng giao thức WireGuard để thiết lập các kết nối được mã hóa đầu cuối giữa các máy tính khác nhau của bạn. Điều này có nghĩa là bạn có thể triển khai một VPN hoạt động chỉ trong vài phút mà không cần cấu hình mạng phức tạp.



Trên Umbrel, cài đặt Tailscale kết nối nút Bitcoin của bạn với mạng riêng ảo của riêng bạn. Sau khi cấu hình, nút của bạn sẽ nhận được địa chỉ IP riêng Tailscale Address, chỉ có thể truy cập từ các thiết bị khác được kết nối với cùng mạng Tailscale (chẳng hạn như máy tính, điện thoại thông minh và máy tính bảng). Kết nối này được mã hóa đầu cuối và không đi qua mạng công cộng không được bảo vệ, giúp tăng cường đáng kể tính bảo mật so với kết nối không được mã hóa.



![Image](assets/fr/090.webp)



Cụ thể, Tailscale mang lại cho bạn một số lợi thế khi sử dụng Umbrel:





- Bạn có thể quản lý Interface Umbrel hoặc truy cập các ứng dụng được liên kết với nút của bạn (chẳng hạn như Mempool, Ride The Lightning, ThunderHub...) từ bất kỳ đâu, như thể bạn đang ở trên cùng một mạng cục bộ, mà không cần mở cổng trên Internet và không cần phải thông qua Tor, vốn rất chậm;





- Bạn có thể kết nối với máy chủ Electrum (Electrs hoặc Fulcrum) hoặc trực tiếp đến Bitcoin core thông qua VPN, bỏ qua Tor. Điều này cung cấp một kết nối an toàn, tương đương với việc sử dụng Tor, nhưng với tốc độ cao hơn nhiều và độ trễ thấp hơn. Tóm lại, bạn vẫn giữ được các lợi ích về quyền riêng tư và bảo mật của Tor trong khi vẫn tận hưởng tốc độ của kết nối Clearnet. Đối với On-Chain Wallet, lợi ích này có vẻ không đáng kể, nhưng nếu bạn dự định thiết lập nút Lightning của riêng mình sau này, sự khác biệt là đáng kể. Thực tế, việc thanh toán qua nút của bạn khi đang di chuyển trên Tor cực kỳ chậm do cần nhiều giao dịch, trong khi với Tailscale, nó hoạt động hoàn hảo.





- Không cần cấu hình quy tắc NAT, mở cổng hoặc thiết lập máy chủ VPN thông thường. Sau khi ứng dụng được cài đặt trên Umbrel và thiết bị của bạn, mạng sẽ tự động được thiết lập.



Do đó, Tailscale trên Umbrel là một giải pháp rất thú vị nếu bạn muốn truy cập nút của mình từ bất kỳ đâu trên thế giới theo cách an toàn, hiệu suất cao và dễ cấu hình mà không ảnh hưởng đến quyền riêng tư hoặc bảo mật.



Để cài đặt và cấu hình Tailscale trên Umbrel của bạn, hãy xem hướng dẫn này, phần 4: "*Sử dụng Tailscale trên Umbrel*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, viết tắt của "*Ghi chú và các nội dung khác được truyền tải qua rơle*", là một giao thức mở, phi tập trung được thiết kế để cho phép các thông điệp được xuất bản và trao đổi trên Internet mà không cần phụ thuộc vào một nền tảng tập trung. Mỗi người dùng có một cặp khóa mật mã: khóa công khai (`npub`), đóng vai trò là mã định danh, và khóa riêng tư (`nsec`), được sử dụng để ký các thông điệp và đảm bảo tính xác thực của chúng.



Tin nhắn được truyền qua một mạng lưới các rơle độc lập. Kiến trúc phân tán này giúp Nostr chống lại kiểm duyệt: không có máy chủ nào kiểm soát quyền truy cập hoặc phân phối, và người dùng có thể kết nối với bao nhiêu rơle tùy thích.



Giao thức này rất phổ biến trong cộng đồng Bitcoin vì, giống như Bitcoin, Nostr giải quyết các vấn đề về chủ quyền kỹ thuật số và kiểm soát dữ liệu. Người sáng lập ra giao thức này, Fiatjaf, là một nhà phát triển đã được công nhận trong hệ sinh thái nhờ những đóng góp to lớn của mình.



Với Umbrel, bạn có thể tối ưu hóa việc sử dụng Nostr. Bằng cách cài đặt ứng dụng ***Nostr Relay***, bạn có thể lưu trữ relay riêng tư trực tiếp trên máy tính của mình, đảm bảo tất cả bài đăng và tương tác của bạn trên Nostr được lưu cục bộ và không thể bị xóa bởi relay công khai.



Các ứng dụng khách Nostr ***noStrudel*** hoặc ***Snort*** cũng có sẵn trên Umbrel. Nhờ các ứng dụng này, bạn có thể đăng, đọc, tìm kiếm hồ sơ và tương tác với hệ sinh thái Nostr trực tiếp từ web Interface trên Umbrel của mình.



Cuối cùng, còn có ứng dụng ***Nostr Wallet Connect*** trên Umbrel, cho phép thanh toán Lightning gốc trong Nostr. Cụ thể, bạn có thể liên kết nút Lightning tương lai của mình với khách hàng Nostr để gửi các khoản thanh toán nhỏ, được gọi là "*zaps*", để thưởng cho nội dung hoặc tương tác theo hình thức kiếm tiền, mà không cần thông qua dịch vụ của bên thứ ba. Các khoản thanh toán này được gửi trực tiếp từ nút cá nhân của bạn thông qua các kênh của bạn.



Để tìm hiểu cách sử dụng tất cả các ứng dụng này, tôi khuyên bạn nên xem hướng dẫn đầy đủ sau:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### Máy chủ BTCPay



BTCPay Server là bộ xử lý thanh toán mã nguồn mở miễn phí cho phép bạn chấp nhận thanh toán qua Bitcoin và Lightning Network mà không cần trung gian, đồng thời vẫn giữ được quyền tự quản lý tiền.



Kiến trúc của BTCPay Server dựa trên một node Bitcoin và, đối với Lightning, dựa trên một triển khai tương thích (LND, Core Lightning...), khiến nó trở thành một trong những giải pháp PoS hoàn toàn không cần lưu ký. Đây cũng là phần mềm toàn diện nhất để theo dõi và kế toán.



![Image](assets/fr/091.webp)



Nếu bạn sở hữu một doanh nghiệp và muốn chấp nhận thanh toán Bitcoin trực tiếp qua nút Umbrel của mình, ứng dụng Máy chủ BTCPay là lựa chọn lý tưởng. Để tìm hiểu thêm về chủ đề này, tôi khuyên bạn nên tham khảo các tài nguyên sau:





- Khóa học BIZ 101 về cách sử dụng Bitcoin trong doanh nghiệp của bạn:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- Khóa học POS 305 về cách sử dụng BTCPay Server:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- Hướng dẫn sử dụng máy chủ BTCPay:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Các khái niệm nâng cao và thực hành tốt nhất


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Duy trì nút thắt ô của bạn


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Để bắt đầu phần cuối cùng này, và trước khi chuyển sang lý thuyết nâng cao hơn, tôi muốn xem xét các phương pháp hay nhất và hành động cụ thể bạn có thể thực hiện sau khi nút Umbrel của bạn được cài đặt, đồng bộ hóa và cấu hình chính xác trong chương ngắn này. Bạn bảo trì nó hàng ngày như thế nào?



### Giữ cho thiết bị luôn khỏe mạnh



Một nút đáng tin cậy bắt đầu từ phần cứng ổn định. Đảm bảo máy chứa nút của bạn được thông gió tốt, không chứa Dust và được lắp đặt trong môi trường khô ráo, tránh xa mọi nguồn nhiệt và độ ẩm. Tránh đặt nút trong không gian hạn chế và hãy chọn vị trí thông thoáng.



Trên Raspberry Pi và máy tính mini, Dust cuối cùng sẽ làm tắc nghẽn bộ tản nhiệt, làm tăng nhiệt độ và dẫn đến hiện tượng điều tiết (tự động giới hạn sử dụng tài nguyên), từ đó làm giảm hiệu suất của node. Đó là lý do tại sao tôi khuyên bạn nên vệ sinh cửa hút gió và quạt định kỳ, lý tưởng nhất là vài tháng một lần.



Hãy đảm bảo sử dụng nguồn điện Supply chất lượng cao, vì điện áp không ổn định có thể dẫn đến hỏng hệ thống và thậm chí gây ra nguy cơ hỏa hoạn. Tốt nhất, bạn nên sử dụng nguồn điện Supply chính hãng do nhà sản xuất cung cấp. Cũng cần lưu ý đến hiện tượng quá nhiệt do hiệu ứng Joule trên ổ cắm điện: luôn tuân thủ công suất tối đa cho phép và không bao giờ kết nối nhiều ổ cắm điện theo kiểu nối tiếp.



Tôi cũng khuyên bạn nên đầu tư vào một bộ lưu điện (UPS). Bộ lưu điện này bảo vệ nút của bạn khỏi việc tắt đột ngột, cho phép Umbrel tắt máy an toàn trong trường hợp mất điện và đảm bảo hoạt động liên tục trong thời gian ngắn hoặc sự cố ngắn hạn.



Về mặt lưu trữ, hãy theo dõi tiến độ: nếu ổ đĩa sắp đầy, hãy cân nhắc giải phóng dung lượng (gỡ cài đặt các ứng dụng không sử dụng, điều chỉnh cài đặt chỉ mục) hoặc di chuyển sang ổ SSD lớn hơn. Nhược điểm của một node Bitcoin đầy đủ là yêu cầu lưu trữ tăng liên tục, vì một khối mới được tạo ra sau mỗi 10 phút và các khối cũ không thể bị xóa (trừ khi node đó là pruned). Do đó, tôi khuyên bạn nên lên kế hoạch cho một dung lượng đủ lớn khi mua phần cứng (tối thiểu 2 TB).



### Cập nhật



Việc cập nhật node rất quan trọng vì ba lý do chính: thứ nhất, bảo mật (vá lỗ hổng, tăng cường bảo mật mạng và bảo vệ chống tấn công DoS); thứ hai, khả năng tương thích (thay đổi chính sách chuyển tiếp, thay đổi định dạng và nâng cấp giao thức); và thứ ba, độ tin cậy và hiệu suất (sửa lỗi, tiêu thụ tài nguyên và các cải tiến khác). Vì vậy, hãy kiểm tra định kỳ để đảm bảo UmbrelOS và các ứng dụng của bạn được cập nhật:





- Để cập nhật hệ thống: Mở menu cài đặt, sau đó nhấp vào nút "*Kiểm tra cập nhật*" bên cạnh tham số "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Để cập nhật ứng dụng: Truy cập App Store. Nếu bất kỳ ứng dụng nào của bạn cần cập nhật, một nút có bong bóng màu đỏ sẽ xuất hiện ở góc trên bên phải của Interface. Chỉ cần nhấp vào nút đó, sau đó cập nhật từng ứng dụng.



Thực hiện thao tác này thường xuyên để giữ cho hệ điều hành và ứng dụng của bạn được cập nhật.



### Sao lưu



Nếu bạn chỉ sử dụng nút Bitcoin để xác thực và phân phối giao dịch, nhưng ví của bạn được quản lý bên ngoài Umbrel (ví dụ: với Hardware Wallet và Sparrow wallet), thì không có dữ liệu nào cần sao lưu trực tiếp vào Umbrel. Trong trường hợp này, dữ liệu sao lưu thiết yếu vẫn là cụm từ khôi phục và Descriptor của Wallet bên ngoài, và điều này áp dụng cho dù bạn có sử dụng nút riêng hay không. Vì vậy, không có gì thay đổi so với cấu hình trước đó của bạn.



Mặt khác, tùy thuộc vào các ứng dụng bổ sung bạn sử dụng trên Umbrel, có thể cần thêm các bản sao lưu. Điều này đặc biệt đúng nếu bạn vận hành một node Lightning trên Umbrel. Trong trường hợp này, việc sao lưu seed được cung cấp khi bạn cài đặt node Lightning là hoàn toàn cần thiết. Ngoài seed, bạn cần một ***Sao lưu Kênh Tĩnh (SCB)*** được cập nhật để có thể khôi phục node Lightning của mình trong trường hợp có sự cố. SCB cho phép bạn khôi phục tiền bằng cách buộc đóng các kênh. Nếu seed hoặc SCB bị mất, việc khôi phục node Lightning là không thể.



Umbrel cũng cung cấp tùy chọn sao lưu tự động và động SCB này trên máy chủ của họ, thông qua Tor, để đảm bảo tệp tin luôn được cập nhật. Trong trường hợp này, chỉ cần seed để khôi phục nút.



Chúng tôi sẽ xem xét lại những khía cạnh này một cách chi tiết trong khóa học LNP202 tiếp theo.



### An toàn hoạt động hàng ngày



Về bảo mật, hãy sử dụng mật khẩu dài, duy nhất và ngẫu nhiên cho Interface Umbrel, và nhớ kích hoạt xác thực hai yếu tố (2FA). Đối với các ứng dụng cung cấp cả bảo vệ bằng mật khẩu và 2FA, hãy luôn kích hoạt cả hai và thay đổi mật khẩu mặc định.



Không bao giờ để bảng điều khiển truy cập Internet mà không sử dụng cổng bảo mật (chẳng hạn như VPN, Tor hoặc chỉ truy cập cục bộ). Hạn chế số lượng ứng dụng bạn cài đặt và thường xuyên xóa những ứng dụng không cần thiết để giảm thiểu nguy cơ bị tấn công.



Để hiểu sâu hơn về bảo mật máy tính nói chung, tôi thực sự khuyên bạn nên tham khảo khóa học miễn phí khác này:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Chẩn đoán và tự giúp đỡ



Trong trường hợp Umbrel của bạn gặp lỗi, trước tiên hãy tải gói chẩn đoán generate thông qua phần khắc phục sự cố của UmbrelOS hoặc ứng dụng liên quan, sau đó khởi động lại ứng dụng. Nếu cần, hãy thử khởi động lại toàn bộ hệ thống.



Nếu sự cố vẫn tiếp diễn, tôi khuyên bạn nên [tham gia cộng đồng người dùng Umbrel trên Discord](https://discord.gg/efNtFzqtdx). Trước tiên, hãy tìm kiếm xem có ai đã gặp phải vấn đề tương tự và tìm ra giải pháp chưa. Nếu chưa, bạn có thể đăng tin nhắn lên kênh `general-support`. Bạn cũng có thể sử dụng [diễn đàn Umbrel](https://community.umbrel.com/).



Những khu vực này không chỉ cho phép bạn theo dõi các thông báo và cập nhật bảo mật mà còn cho phép bạn đặt câu hỏi và cuối cùng là hỗ trợ người dùng khác. Thông thường, những phương pháp hay nhất sẽ được khám phá thông qua các sàn giao dịch này.



Với những thói quen đơn giản này, nút Umbrel của bạn sẽ luôn ổn định, an toàn và hữu ích cho cả bạn và mạng Bitcoin.




## Hiểu về IBD và quá trình khám phá ngang hàng


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Nút Bitcoin của bạn khởi động mà không cần biết trước lịch sử giao dịch. Ban đầu, nó chỉ là một máy tính chạy phần mềm (Bitcoin core hoặc tương tự). Để trở thành một nút Bitcoin được đồng bộ hóa và hoạt động hoàn toàn, nó phải tái tạo cục bộ trạng thái của Ledger bằng cách kiểm tra tất cả các khối đã được công bố kể từ khối Genesis (khối 0, do Satoshi Nakamoto công bố vào ngày 3 tháng 1 năm 2009). Bước này được gọi là **IBD (_Tải xuống Khối Ban đầu_)**.



IBD bao gồm việc tải xuống và xác minh từng khối và giao dịch riêng lẻ, áp dụng các quy tắc đồng thuận, để xây dựng phiên bản Blockchain riêng. Mục đích không chỉ đơn thuần là lấy lại bản sao dữ liệu chưa được xác minh, mà còn đi đến kết luận tương tự một cách hoàn toàn độc lập, như phần lớn mạng lưới trung thực đã làm.



![Image](assets/fr/092.webp)



### Các mốc quan trọng của IBD



Quá trình đồng bộ hóa bắt đầu với bước _**headers-first**_. Nút của bạn yêu cầu chuỗi tiêu đề khối từ nhiều nút ngang hàng và, đối với mỗi nút, xác minh Proof of Work, điều chỉnh độ khó, cú pháp, cũng như các quy tắc Timestamp và số phiên bản. Tóm lại, nó đảm bảo rằng mỗi tiêu đề nhận được đều tuân thủ các quy tắc đồng thuận.



![Image](assets/fr/093.webp)



Xin nhắc lại, một khối Bitcoin bao gồm một tiêu đề 80 byte và một danh sách các giao dịch. Dấu vân tay của khối được lấy bằng cách áp dụng thuật toán SHA-256 kép Hash vào tiêu đề này, bao gồm 6 trường:




- phiên bản
- Hash của khối trước
- Merkle Root của các giao dịch
- Timestamp (lớn hơn thời gian trung bình của 11 khối trước đó)
- mục tiêu khó khăn
- Nonce



![Image](assets/fr/094.webp)



Các giao dịch được xác nhận vào Merkle Tree. Đây là một cấu trúc tóm tắt một tập dữ liệu lớn (trong trường hợp này là tất cả các giao dịch trong khối) bằng cách tổng hợp các hàm băm của chúng theo thứ tự từng cặp xuống một "gốc", do đó chứng minh rằng một phần tử thuộc về tập hợp (và phát hiện bất kỳ sửa đổi nào). Theo cách này, bất kỳ sửa đổi nào đối với một giao dịch cũng sẽ sửa đổi gốc của Merkle Tree và do đó là dấu vân tay của tiêu đề khối. SegWit đã giới thiệu một Commitment bổ sung riêng biệt cho cookie (chữ ký), được đặt trong coinbase.



![Image](assets/fr/095.webp)



Bước _**headers-first**_ này cho phép nút xác định nhánh có khối lượng công việc nhiều nhất (bất kể số khối), tức là nhánh mà các nút Bitcoin đồng bộ hóa. Sau khi nhánh này được xác định, nút sẽ tải xuống nội dung của các khối song song từ nhiều kết nối, sau đó xác thực từng giao dịch: định dạng, tính hợp lệ của các tập lệnh (ngoại trừ `assumevalid=1`), số tiền và việc không có chi tiêu trùng lặp. Với mỗi lần kiểm tra thành công, trạng thái hiện tại của các đồng xu chưa sử dụng (bộ UTXO) sẽ được cập nhật trong cơ sở dữ liệu `chainstate/`: các đầu ra đã sử dụng sẽ bị xóa, trong khi các đầu ra hợp lệ mới sẽ được thêm vào.



Mặt khác, Mempool chỉ phát huy tác dụng khi tiếp cận đầu chuỗi: miễn là nút vẫn ở độ trễ, nó sẽ không có giao dịch nào đang chờ xử lý để lưu trữ.



Khi IBD hoàn tất, nút sẽ bước vào giai đoạn bình thường: xác thực các khối mới khi chúng được xuất bản, duy trì Mempool với các giao dịch đang chờ xử lý theo các quy tắc chuyển tiếp, chuyển tiếp các giao dịch và khối và quản lý mọi hoạt động tổ chức lại chuỗi.



### Giả định hợp lệ



Bitcoin core kết hợp một cơ chế được thiết kế để giảm thời gian cần thiết trước khi một nút hoạt động hoàn toàn, đồng thời vẫn giữ nguyên bản chất của nguyên tắc xác minh tự động: AssumeValid.



Tham số `assumevalid` dựa trên một khối tham chiếu trước đó, trong đó Hash được tích hợp vào từng phiên bản phần mềm. Trong quá trình IBD, nếu nút của bạn thấy khối này thực sự nằm trên nhánh có khối lượng công việc nhiều nhất, nó có thể bỏ qua việc xác minh tập lệnh cho tất cả các giao dịch trước thời điểm này.



Tất cả các quy tắc khác (cấu trúc khối, Proof of Work, giới hạn kích thước, số lượng giao dịch, UTXO, v.v.) vẫn được xác minh đầy đủ. Chỉ tính toán các tập lệnh trước khối tham chiếu này mới bị bỏ qua. Hiệu suất tăng đáng kể trên IBD, vì việc xác minh chữ ký chiếm phần lớn tải CPU. Sau khối tham chiếu này, việc xác minh sẽ trở lại trạng thái bình thường.



Bạn có thể buộc xác thực đầy đủ tất cả các tập lệnh bằng cách vô hiệu hóa cơ chế này, với cái giá phải trả là IBD dài hơn nhiều, bằng cách sử dụng tham số `assumevalid=0` trong tệp `Bitcoin.conf`.



### Giả sửUTXO



`assumeutxo` là một tham số hiện có khác, nhưng không giống như `assumevalid`, nó không được kích hoạt theo mặc định. Cơ chế này cho phép phần mềm tải ảnh chụp nhanh của bộ UTXO, cùng với siêu dữ liệu của nó, và tạm thời coi nó là trạng thái tham chiếu, sau khi xác minh rằng các tiêu đề thực sự dẫn đến Blockchain với khối lượng công việc nhiều nhất.



Nhờ đó, nút này nhanh chóng hoạt động cho các mục đích sử dụng chung (RPC, kết nối ví, v.v.), đồng thời khởi chạy quá trình tái tạo hoàn chỉnh và đã được xác minh của bộ UTXO của chính nó ở chế độ nền. Khi giai đoạn này hoàn tất, ảnh chụp nhanh ban đầu sẽ được thay thế bằng trạng thái tái tạo cục bộ. Cách tiếp cận này tách biệt việc cung cấp nút nhanh với việc xác minh đầy đủ, mà không ảnh hưởng đến việc xác minh đầy đủ.



### Khám phá ngang hàng: Nút của bạn tìm thấy mạng Bitcoin như thế nào?



Khi một nút khởi động lần đầu tiên, nó chưa biết bất kỳ nút ngang hàng nào. Tuy nhiên, nó phải tìm các nút Bitcoin khác trên Internet để yêu cầu tiêu đề, sau đó là khối, để hoàn thành IBD của mình. Để khởi tạo các kết nối này, Bitcoin core tuân theo logic ưu tiên.



![Image](assets/fr/096.webp)



Khi nút khởi động lại sau khi đã được sử dụng, Core trước tiên sẽ cố gắng kết nối lại với các nút ngang hàng (peers) đã đăng ký trước khi tắt máy, thông tin được lưu trữ trong tệp `anchors.dat`. Sau đó, nó tham khảo sổ IP Address **``peers.dat`**, nơi lưu trữ danh sách các nút ngang hàng đã gặp trước đó, để kết nối lại với chúng. Đây chỉ là một tệp cục bộ, được Core cập nhật và lưu giữ. Mặt khác, đối với một nút mới vừa được khởi chạy, 2 tệp này sẽ trống, vì nó chưa từng giao tiếp với các nút Bitcoin khác.



Trong trường hợp này, phần mềm sẽ truy vấn _**hạt giống DNS**_. Đây là [các máy chủ được duy trì bởi các nhà phát triển hệ sinh thái được công nhận](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), trả về danh sách địa chỉ IP của các nút được cho là đang hoạt động. Các địa chỉ này cho phép nút mới khởi tạo các kết nối đầu tiên và yêu cầu dữ liệu cần thiết từ IBD. Dưới đây là danh sách *hạt giống DNS* đang hoạt động cho đến nay (tháng 8 năm 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Chuyên gia cấp cao: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz`
- Ava Chow: `seed.Mainnet.achownodes.xyz.`



Trong phần lớn các trường hợp, bước *hạt giống DNS* là đủ để thiết lập kết nối đầu tiên với các nút khác. Nếu, ngoại lệ, các máy chủ này không phản hồi trong vòng 60 giây, nút sẽ chuyển sang phương pháp khác: [danh sách tĩnh gồm hơn 1.000 địa chỉ](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) của _hạt giống nút_ được tích hợp sẵn trong mã của Bitcoin core và được cập nhật thường xuyên. Nếu hai phương pháp đầu tiên để lấy địa chỉ IP không thành công, giải pháp cuối cùng này sẽ thiết lập kết nối ban đầu, từ đó nút có thể yêu cầu địa chỉ IP mới.



![Image](assets/fr/097.webp)



Cuối cùng, bạn có thể nhập địa chỉ IP Supply theo cách thủ công thông qua tệp `peers.dat` để buộc thực hiện các kết nối cụ thể.



Sau khi khởi động, trình quản lý Address nội bộ sẽ đa dạng hóa các nguồn (các mạng tự trị riêng biệt, clearnet và Tor, cũng như các khu vực địa lý khác nhau) để giảm thiểu rủi ro cô lập về mặt cấu trúc. Nút thiết lập các kết nối đi này (các kết nối mà nó tự chọn, do đó an toàn hơn).



Nếu nút của bạn đang lắng nghe trên một cổng mở (mặc định là 8333), nó sẽ chấp nhận các kết nối đến. Điều này củng cố khả năng phục hồi tổng thể của mạng bằng cách cung cấp một điểm liên lạc cho các nút mới mà không mang lại bất kỳ lợi ích cụ thể nào cho IBD của bạn. Nếu nút của bạn chạy trên Tor, logic vẫn giữ nguyên, nhưng địa chỉ được sử dụng là các dịch vụ `.onion`.




## Cấu tạo nút thắt Bitcoin của bạn


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Khi nút của bạn hoàn tất quá trình đồng bộ hóa ban đầu, nó sẽ lưu trữ cục bộ một số tập dữ liệu bổ sung, cho phép nó xác thực các khối và giao dịch, phục vụ các đối tác mạng và khởi động lại nhanh chóng trong khi vẫn duy trì trạng thái của nó. 3 khối chính cần thiết trên một nút:




- gW-402 **khối** được lưu trữ trên đĩa,
- bộ **UTXO** được duy trì trong cơ sở dữ liệu khóa-giá trị,
- và **Mempool** được lưu trữ trong RAM và được tuần tự hóa theo định kỳ.



Ngoài ra, một số tệp phụ trợ (peer, ước tính phí, danh sách loại trừ, ví, v.v.) cũng góp phần hoàn thiện bức tranh. Hãy cùng khám phá vai trò của tất cả các tệp này.



### Dữ liệu của nút thực sự nằm ở đâu?



Theo mặc định, Bitcoin core lưu dữ liệu của mình trong một thư mục làm việc cụ thể. Trong GNU/Linux, thư mục này thường nằm trong `~/.Bitcoin/`, trong Windows là `%APPDATA%\Bitcoin/`, và trong macOS là `~/Library/Application Support/Bitcoin/`. Nếu bạn đang sử dụng một giải pháp đóng gói (ví dụ: trong một bản phân phối node), thư mục này có thể được gắn ở nơi khác, nhưng cấu trúc của nó vẫn giữ nguyên. Các thư mục con và tệp quan trọng được mô tả bên dưới vẫn nằm ở đây.



![Image](assets/fr/098.webp)



### Các khối



Do đó, Blockchain là một tập hợp các khối. Full node lưu trữ các khối này dưới dạng các tệp phẳng tuần tự và duy trì một chỉ mục song song để truy xuất nhanh chóng. Khi cần (tổ chức lại, quét lại Wallet, dịch vụ ngang hàng), dữ liệu này được đọc lại nguyên trạng.



**Lưu ý:** Tái tổ chức, hay đồng bộ hóa lại, là hiện tượng Blockchain trải qua sự thay đổi cấu trúc do sự tồn tại của các khối cạnh tranh ở cùng độ cao. Điều này xảy ra khi một phần của Blockchain được thay thế bằng một chuỗi khác có khối lượng công việc tích lũy lớn hơn. Những sự đồng bộ hóa lại này là một phần tự nhiên trong hoạt động của Bitcoin, khi các thợ đào khác nhau có thể tìm thấy các khối mới gần như đồng thời, do đó chia tách mạng lưới Bitcoin thành hai. Trong những trường hợp như vậy, mạng lưới có thể tạm thời chia thành các chuỗi cạnh tranh. Cuối cùng, khi một trong những chuỗi này tích lũy được nhiều công việc hơn, các chuỗi còn lại sẽ bị các nút bỏ rơi, và các khối của chúng được gọi là "khối lỗi thời" hoặc "khối mồ côi". Quá trình thay thế một chuỗi bằng một chuỗi khác được gọi là đồng bộ hóa lại.



#### Tệp Blk*.dat (dữ liệu khối thô)



Các khối đã nhận và được xác thực sẽ được ghi vào các vùng chứa tuần tự có tên `blkNNNNN.dat`, được lưu trữ trong thư mục `blocks/`. Mỗi tệp được điền theo trình tự cho đến khi đạt kích thước tối đa 128 MiB, tại thời điểm đó, Core sẽ mở tệp tiếp theo. Bên trong, mỗi khối được tuần tự hóa theo định dạng mạng, được đặt trước bởi một mã định danh ma thuật và một độ dài. Cách tổ chức này cho phép ghi nhanh vào đĩa và tạo điều kiện thuận lợi cho dịch vụ khối đồng bộ hóa các đối tác.



![Image](assets/fr/099.webp)



Ở chế độ pruned, nút chỉ giữ lại một cửa sổ gần đây của các tệp này để hạn chế dung lượng đĩa. Nó xóa các container `blk*.dat` cũ nhất ngay khi đạt đến mục tiêu không gian được cấu hình, đồng thời giữ lại đủ lịch sử để duy trì tính nhất quán với chuỗi đã biết. Chỉ mục và bộ UTXO vẫn giữ nguyên trạng thái bình thường, cho phép xác thực các giao dịch và khối tiếp theo.



#### Tệp Rev*.dat (dữ liệu hủy bỏ)



Để có thể quay ngược thời gian trong quá trình sắp xếp lại, Core lưu song song với mỗi tệp `blk` một tệp `revNNNNN.dat` trong `blocks/`. Tệp này chứa thông tin cần thiết để hoàn tác tác động của một khối lên bộ UTXO: với mỗi đầu ra được khối sử dụng, trạng thái trước đó của UTXO tương ứng sẽ được lưu trữ (số lượng, tập lệnh, chiều cao...). Trong trường hợp khối bị hủy, nút có thể nhanh chóng khôi phục trạng thái trước đó mà không cần phải quét lại toàn bộ chuỗi.



![Image](assets/fr/100.webp)



#### Chỉ số khối (khối/chỉ số)



Việc tìm kiếm một khối trực tiếp trong các tệp phẳng sẽ rất tốn thời gian. Do đó, Core duy trì một cơ sở dữ liệu LevelDB trong `blocks/index/`, liệt kê, cho mỗi khối đã biết, siêu dữ liệu như Hash, chiều cao, trạng thái xác thực, tệp `blk` và vị trí của khối đó. Khi một đối tác yêu cầu một khối, hoặc khi một thành phần nội bộ cần truy cập vào một khối cụ thể, chỉ mục này sẽ cung cấp quyền truy cập nhanh chóng. Nếu không có chỉ mục này, sẽ cần quá nhiều thao tác.



![Image](assets/fr/101.webp)



#### Chỉ mục tùy chọn (indexes/)



Một số chỉ mục là tùy chọn và bị vô hiệu hóa theo mặc định vì chúng làm tăng dung lượng đĩa:




- `indexes/txindex/`, mà chúng tôi đã đề cập, cung cấp một bảng ánh xạ giao dịch → vị trí, cho phép truy xuất bất kỳ giao dịch nào đã được xác nhận mà không cần biết khối chứa giao dịch đó. Điều này hữu ích cho các truy vấn loại `getrawtransaction` ngoài Wallet, nhưng khá tốn kém.
- indexes/blockfilter/` có thể chứa các bộ lọc khối nhỏ gọn (BIP157/158) cho máy khách mỏng. Các cấu trúc này tăng tốc quá trình xác minh phía máy khách, nhưng lại tiêu tốn thêm dung lượng lưu trữ trên nút lập chỉ mục.



### Bộ UTXO (chainstate)



Mô hình UTXO (*Đầu ra giao dịch chưa sử dụng*) là biểu diễn kế toán của Bitcoin: mỗi đầu ra chưa sử dụng là một "Coin" khả dụng có thể được sử dụng làm đầu vào cho giao dịch trong tương lai.



![Image](assets/fr/102.webp)



Tổng số tất cả các phần này tại một thời điểm T nhất định tạo thành tập UTXO: một danh sách lớn tất cả các phần hiện có. Chính trạng thái này mà nút tham khảo để quyết định xem một giao dịch có sử dụng các đơn vị hợp lệ chưa được sử dụng trong giao dịch trước đó hay không (để tránh Double-spending).



![Image](assets/fr/103.webp)



Bộ UTXO được lưu trữ trong thư mục `chainstate/` dưới dạng cơ sở dữ liệu LevelDB nhỏ gọn. Mỗi phần liên kết một khóa được lấy từ Hash của giao dịch và chỉ mục đầu ra với một giá trị bao gồm: số tiền, khóa `scriptPubKey`, chiều cao của khối tạo và chỉ báo coinbase.



![Image](assets/fr/104.webp)



Nút duy trì bộ nhớ đệm phía trên LevelDB để hấp thụ các thao tác đọc và ghi thường xuyên. Tham số `dbcache` có thể được sử dụng để điều chỉnh kích thước của bộ nhớ đệm này: kích thước càng lớn, IBD và quá trình xác thực hiện tại càng được hưởng lợi từ quyền truy cập bộ nhớ nhiều hơn, với cái giá phải trả là mức tiêu thụ RAM cao hơn. Khi một khối mới được tìm thấy bởi Miner, nút sẽ xóa khỏi bộ nhớ đệm UTXO các đầu ra đã được sử dụng (hoặc tiêu thụ) bởi các giao dịch có trong khối và thêm các đầu ra mới được tạo.



Về mặt lý thuyết, chúng ta có thể xác thực một giao dịch bằng cách quét lại lịch sử khối để kiểm tra xem đầu ra chưa từng được sử dụng. Tuy nhiên, trên thực tế, việc này sẽ tốn quá nhiều thời gian, vì toàn bộ Blockchain sẽ phải được quét cho mỗi giao dịch mới. Do đó, bộ UTXO cung cấp góc nhìn tối thiểu cần thiết để chứng minh cục bộ và trong một khoảng thời gian hợp lý sự vắng mặt của Double-spending.



Lưu ý rằng bộ UTXO thường là tâm điểm của những lo ngại về tính phi tập trung của Bitcoin, vì kích thước của nó tự nhiên tăng nhanh chóng. Điều này một phần là do giá Bitcoin tăng cao, dẫn đến tình trạng phân mảnh các bộ phận, và một phần là do sự gia tăng áp dụng hệ thống: càng có nhiều người dùng, nhu cầu về UTXO càng lớn.



![Image](assets/fr/105.webp)



Sự phát triển của bộ UTXO cũng bắt nguồn từ cấu trúc của các giao dịch thanh toán đơn giản trên Bitcoin. Thực tế, khi thực hiện thanh toán, bạn sử dụng một UTXO làm đầu vào và tạo ra 2 UTXO mới làm đầu ra (một cho thanh toán và một cho Exchange). Cuối cùng, một phương pháp phân tích chuỗi, được gọi là CIOH (*Phương pháp Đầu vào Chung Ownership*), cung cấp thêm động lực để tránh hợp nhất Coin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Vì một phần của nó phải được lưu trữ trong RAM để xác minh các giao dịch trong thời gian hợp lý, bộ UTXO có thể dần dần khiến việc vận hành Full node trở nên quá tốn kém. Để giải quyết vấn đề này, một số đề xuất đã được đưa ra, đáng chú ý là [Utreexo](https://planb.network/resources/glossary/utreexo).



### Mempool



Mempool là tập hợp cục bộ các giao dịch hợp lệ đã được nhận nhưng chưa được xác nhận. Xin nhắc lại, một "giao dịch đã được xác nhận" là giao dịch đã được đưa vào một khối hợp lệ. Mỗi nút duy trì Mempool riêng, có thể khác với Mempool của các nút khác trong mạng tùy thuộc vào:




- kích thước được phân bổ cho Mempool thông qua tham số `maxmempool`: một nút có Mempool lớn hơn sẽ có thể chứa nhiều giao dịch hơn một nút có Mempool nhỏ hơn (trừ khi nút sau bị trống);
- Quy tắc gW-433: đây là một tập hợp con các quy tắc chuyển tiếp của nút và xác định các đặc điểm mà một giao dịch chưa xác nhận phải đáp ứng để được chấp nhận trong Mempool;
- sự thẩm thấu giao dịch: do nhiều yếu tố khác nhau, một giao dịch nhất định có thể đã được phân phối đến một phần của mạng nhưng chưa đến được phần khác.



Điều quan trọng cần lưu ý là các mempool nút không có giá trị đồng thuận. Bitcoin hoạt động hoàn hảo ngay cả khi mỗi nút có một Mempool khác nhau. Về cơ bản, các khối có thẩm quyền luôn là các khối được thêm vào Blockchain. Ví dụ: ngay cả khi một nút ban đầu từ chối một giao dịch nhất định trong Mempool của mình (hợp lệ theo quy tắc đồng thuận), nút đó sẽ buộc phải chấp nhận giao dịch đó nếu cuối cùng giao dịch đó được đưa vào một khối có Proof of Work hợp lệ. Nếu nút đó không làm như vậy và từ chối khối này, mặc dù nó đã tuân thủ các quy tắc đồng thuận, thì nó sẽ kích hoạt Hard Fork, tức là tạo ra một Bitcoin mới, riêng biệt mà nó sẽ ở một mình.



#### Chính sách và quản lý bộ nhớ



Khi nhận được giao dịch, Core sẽ áp dụng một loạt kiểm tra dựa trên các quy tắc đồng thuận (cú pháp, tập lệnh hợp lệ, không chi tiêu gấp đôi, v.v.) và các quy tắc Mempool, vốn là chính sách cục bộ (RBF, ngưỡng phí tối thiểu, giới hạn dữ liệu trong `OP_RETURN`, v.v.). Nếu giao dịch tuân thủ các quy tắc này, giao dịch sẽ được lưu trữ trong bộ nhớ.



Kích thước của Mempool bị giới hạn bởi tham số `maxmempool` trong tệp `Bitcoin.conf` (sẽ đề cập thêm về điều này trong chương tiếp theo). Theo mặc định, giới hạn là 300 MB. Khi đầy, nút sẽ tự động tăng ngưỡng phí tối thiểu và loại bỏ các giao dịch ít lợi nhuận nhất trước (tức là giữ lại các giao dịch cần được khai thác trước). Các giao dịch quá cũ cũng có thể hết hạn sau một khoảng thời gian trì hoãn được cấu hình.



#### Mempool lưu trên đĩa



Để tăng tốc độ khởi động lại, Core định kỳ tuần tự hóa trạng thái của Mempool trong tệp `Mempool.dat` khi nút bị tắt. Ngoài Mempool thực tế vẫn còn trong bộ nhớ, Core còn lưu trữ tệp `Mempool.dat` này trên đĩa. Lần tiếp theo nút được khởi chạy, nó sẽ tải lại ảnh chụp nhanh này và xóa bất kỳ nội dung nào không còn hợp lệ đối với Blockchain hiện tại.



### Các tập tin phụ trợ và cơ sở dữ liệu



Một số tệp khác ở cùng cấp độ như `blocks/`, `chainstate/` và `indexes/` tham gia vào hoạt động bình thường của:




- `peers.dat` lưu trữ một danh sách IP Address các peer tiềm năng, được cung cấp bởi các hoạt động khám phá DNS ban đầu, trao đổi mạng và bổ sung thủ công. Khi nút khởi động, nó có thể sử dụng tệp này để thiết lập các kết nối đi.
- Khi nút bị tắt, `anchors.dat` sẽ lưu địa chỉ của các đối tác gửi đi để bạn có thể thử liên hệ lại với họ một cách nhanh chóng vào lần khởi động tiếp theo.
- `banlist.json` chứa các lệnh cấm cục bộ do người vận hành hoặc nút quyết định (hành vi không hợp lệ lặp lại) nhằm ngăn nút kết nối lại hoặc chấp nhận kết nối từ các đối tác cụ thể này.
- `fee_estimates.dat` lưu trữ số liệu thống kê về mốc thời gian đối với các xác nhận được quan sát, được bộ ước tính phí sử dụng để đề xuất mức phí phù hợp với mục tiêu độ trễ đã chọn khi tạo giao dịch.
- gW-446.conf` chứa các tham số cấu hình của nút. Đây là nơi bạn có thể điều chỉnh các quy tắc chuyển tiếp. Tôi sẽ nói thêm về điều này trong chương tiếp theo.
- `settings.json` chứa các tham số bổ sung cho `Bitcoin.conf`.
- `debug.log` là nhật ký văn bản chẩn đoán, có thể được sử dụng để hiểu hoạt động của nút trong trường hợp xảy ra lỗi.
- gW-448.pid` lưu trữ mã định danh quy trình khi chạy, cho phép các ứng dụng hoặc tập lệnh khác dễ dàng nhận dạng bitcoind (*Bitcoin daemon*) và tương tác với nó nếu cần. Mã này được tạo khi khởi động nút và bị xóa khi tắt máy.
- `ip_asn.map` là bảng ánh xạ IP → ASN (hệ thống độc lập) được sử dụng để phân nhóm và đa dạng hóa ngang hàng (tùy chọn `-asmap`).
- `onion_v3_private_key` lưu trữ khóa riêng của dịch vụ Tor v3 khi tùy chọn `-listenonion` được bật, nhằm duy trì onion Address ổn định giữa các lần khởi động lại.
- `i2p_private_key` lưu trữ khóa riêng tư I2P khi `-i2psam=` được sử dụng để tạo kết nối đi và có thể là kết nối đến trên I2P.
- `.cookie` chứa mã xác thực RPC tạm thời (được tạo khi khởi động, bị xóa khi tắt máy) khi sử dụng xác thực cookie. Ví dụ, mã này có thể được sử dụng để kết nối phần mềm Wallet.
- `.lock` là khóa thư mục dữ liệu, ngăn chặn nhiều phiên bản ghi vào cùng một datadir cùng một lúc.
- `guisettings.ini.bak` là tùy chọn tự động lưu cài đặt GUI (*Bitcoin Qt*) khi sử dụng tùy chọn `-resetguisettings`.



Như chúng ta đã thấy trong các phần đầu của khóa học BTC 202 này, Bitcoin core vừa là phần mềm node Bitcoin vừa là phần mềm node Wallet. Tuy nhiên, đây không nhất thiết là giải pháp tôi khuyên dùng để quản lý ví của bạn, vì Interface vẫn còn khá cơ bản và chức năng còn hạn chế so với các phần mềm hiện đại như Sparrow hoặc Liana. Core cũng bao gồm các tệp để quản lý ví của bạn:





- `wallets/` là thư mục mặc định lưu trữ một hoặc nhiều;
- `wallets/<name>/Wallet.dat` là cơ sở dữ liệu SQLite của Wallet (khóa, mô tả, siêu dữ liệu giao dịch, v.v.);
- wallets/<name>/Wallet.dat-journal` là nhật ký khôi phục SQLite.



Tóm lại, đây là cấu trúc tệp Bitcoin core:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Đường dẫn xác thực cho một khối mới



Khi nhận được một khối mới, nút của bạn sẽ kiểm tra Proof of Work và, nói chung là, việc tuân thủ các quy tắc đồng thuận. Nếu mọi thứ đều ổn, nút sẽ áp dụng các thay đổi theo từng giao dịch vào tập hợp UTXO của mình: nút sẽ kiểm tra xem mỗi mục nhập có sử dụng các UTXO hiện có với một tập lệnh hợp lệ hay không, xóa các UTXO này và thêm các lối thoát mới. Nếu mọi thứ đều hợp lệ, các thay đổi sẽ được cam kết vào `chainstate/`.



Đồng thời, dữ liệu hoàn tác được ghi vào `rev*.dat` và siêu dữ liệu được ghi vào chỉ mục `blocks/index/`. Khối sau đó được tuần tự hóa thành tệp `blk*.dat` chính xác. Trong trường hợp tổ chức lại, nút sẽ đọc `rev*.dat` theo chiều ngược lại để ngắt kết nối các khối bị bỏ rơi một cách sạch sẽ, khôi phục tập hợp UTXO, rồi kết nối các khối của chuỗi tốt nhất mới.





## Hiểu về Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Tệp `Bitcoin.conf` là tệp cấu hình Interface chính cho Bitcoin core. Tệp này cho phép bạn điều chỉnh hành vi và các tham số của nút mà không cần phải biên dịch lại mã nguồn hoặc thực hiện các sửa đổi dòng lệnh. Cụ thể, đây là một tệp văn bản thuần túy được cấu trúc theo cặp khóa-giá trị, nghĩa là mỗi dòng của tệp tham chiếu đến một tham số cụ thể (khóa) và giá trị liên quan, có thể được sửa đổi để điều chỉnh tham số đó.



Các tham số mạng, chuyển tiếp giao dịch, hiệu suất, lập chỉ mục, ghi nhật ký và truy cập RPC có thể được định nghĩa trong `Bitcoin.conf`. Tuy nhiên, tệp cấu hình này không bao giờ sửa đổi các quy tắc đồng thuận của giao thức: nó chỉ thiết lập chính sách cục bộ của nút (quy tắc chuyển tiếp), cách nút kết nối, lập chỉ mục và hiển thị các dịch vụ.



### Vị trí và ưu tiên



Theo mặc định, `Bitcoin.conf` nằm trong thư mục dữ liệu Bitcoin core. Đây là thư mục nổi tiếng mà chúng tôi đã đề cập trong chương trước. Tuy nhiên, tệp này không được Bitcoin core tự động tạo, ngoại trừ trong một số môi trường nhất định, chẳng hạn như Umbrel. Nếu tệp này chưa tồn tại, bạn sẽ phải tự tạo bằng cách tạo một tệp có tên `Bitcoin.conf`, sau đó mở tệp đó trong trình soạn thảo văn bản để thực hiện các chỉnh sửa.



Các tham số được xác định trong `Bitcoin.conf` có thể được ghi đè bởi 2 lớp:




- `settings.json` (được viết động bằng đồ họa Interface hoặc một số RPC),
- và các tùy chọn được sửa đổi thông qua dòng lệnh.



Lưu ý rằng bất kỳ sửa đổi nào đối với `Bitcoin.conf` đều yêu cầu phải khởi động lại nút để có hiệu lực.



### Định dạng và cấu trúc



Do đó, định dạng của `Bitcoin.conf` rất đơn giản: mỗi tùy chọn một dòng, dưới dạng `option=value`. Các khoảng trắng và dòng trống không cần thiết sẽ bị bỏ qua, và chú thích mã bắt đầu bằng `#`.



Hầu như tất cả các tùy chọn Boolean đều có thể bị vô hiệu hóa bằng tiền tố `no`. Ví dụ, `listen=0` và `nolisten=1` tương đương nhau tùy theo phiên bản.



Để phân đoạn cấu hình theo mạng, bạn có thể sử dụng các phần: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Ngoài ra, bạn có thể thêm tiền tố `regtest.maxmempool=100` vào tên tùy chọn.



### Những gì Bitcoin.conf có thể và không thể làm



Như đã giải thích ở trên, rõ ràng là các quy tắc đồng thuận không thể cấu hình được trong `Bitcoin.conf`, vì điều này có thể tạo ra lỗi Hard Fork. Mặt khác, nhiều khía cạnh khác có thể cấu hình được. Có 3 lớp hữu ích cần lưu ý:




- Các tham số hoàn toàn cục bộ. Chúng chỉ ảnh hưởng đến nút của bạn: kích thước bộ nhớ đệm (`dbcache`), chế độ pruned (`prune`), chỉ mục tùy chọn... Chúng ảnh hưởng đến hiệu suất máy của bạn, nhưng không ảnh hưởng đến mạng.
- Chính sách Relay và Mempool. Những chính sách này quyết định những gì nút của bạn chấp nhận, lưu giữ và chuyển tiếp trước khi xác nhận: ngưỡng phí tối thiểu (`minrelaytxfee`), kích thước và thời gian lưu giữ Mempool (`maxmempool`, `mempoolexpiry`), thay thế giao dịch (RBF)... Các quy tắc này không phải là một phần của sự đồng thuận, vì vậy hai nút khác nhau có thể có các chính sách khác nhau mà vẫn hoàn toàn tương thích. Mặt khác, các tham số này sẽ ảnh hưởng đến mạng Bitcoin (như đã giải thích trong phần đầu tiên, đặc biệt là với lý thuyết thẩm thấu).
- Kết nối mạng. Các tùy chọn này xác định cách nút của bạn tìm kiếm các nút ngang hàng, lắng nghe, duyệt qua NAT, sử dụng Tor hoặc proxy, hoặc giới hạn băng thông. Chúng định hình cấu trúc mạng của bạn, nhưng không thay đổi việc chuyển tiếp các giao dịch.



Việc hiểu rõ sự tách biệt này rất quan trọng: nếu một giao dịch không tuân thủ các quy tắc đồng thuận, nút của bạn sẽ từ chối nó trong mọi trường hợp. Tuy nhiên, một chính sách cục bộ chặt chẽ hơn có thể từ chối chuyển tiếp một giao dịch hợp lệ theo nghĩa đồng thuận.



### Mạng và cấu trúc mạng



Trước hết, điều quan trọng là phải phân biệt rõ ràng 2 loại kết nối mà một nút Bitcoin có thể có:




- Các kết nối đi được khởi tạo từ nút của chúng ta đến một nút khác;



![Image](assets/fr/106.webp)





- Các kết nối đến được khởi tạo bởi một nút khác đến nút của chúng ta.



![Image](assets/fr/107.webp)



Hai loại kết nối này hoàn toàn có khả năng trao đổi cùng một dữ liệu theo cả hai hướng; vấn đề không phải là giới hạn hướng truyền dữ liệu, mà chỉ là sự khác biệt về điểm khởi tạo kết nối. Theo quan điểm của nút, các kết nối đi thường được coi là an toàn hơn, vì chúng tôi khởi tạo chúng và chọn chính xác nút nào để kết nối, khiến kết nối đó ít có khả năng là kết nối độc hại. Theo mặc định, Bitcoin core duy trì 10 kết nối đi (8 "*full-relay*" + 2 "*block-relay-only*").



Full node tăng thêm giá trị cho mạng bằng cách chấp nhận các kết nối đến. Tham số `listen=1` cho phép lắng nghe trên cổng mặc định 8333 của mạng đang xét, cho phép các kết nối đến này được nhận trên clearnet. Để tính năng này hoạt động, cổng này cũng phải được mở trên bộ định tuyến của bạn. Nếu không, nút của bạn sẽ tiếp tục hoạt động chỉ với các kết nối đi, điều này sẽ không ảnh hưởng đến việc sử dụng Bitcoin cá nhân của bạn. Việc có cho phép các kết nối đến hay không là tùy thuộc vào bạn; không có "lựa chọn tốt nhất".



Nếu bạn không muốn mở cổng trên bộ định tuyến nhưng vẫn chấp nhận các kết nối đến, bạn có thể kích hoạt tham số `listenonion=1`. Thao tác này cũng sẽ đạt được kết quả tương tự, nhưng chỉ thông qua mạng Tor chứ không phải clearnet.



Ở cấp độ mạng, chúng ta cũng có:




- `addnode`: thêm một đối tác thân thiện để liên hệ ngoài chức năng khám phá thông thường (có thể chỉ định nhiều lần).
- connect`: hạn chế nghiêm ngặt các kết nối đến Address được cung cấp (có thể được chỉ định nhiều lần). Core sẽ không kết nối với bất kỳ nút nào khác.
- `seednode`: chỉ được sử dụng để điền vào book-Address khi kết nối với một nút, sau đó ngắt kết nối.
- `maxconnections`: xác định giới hạn toàn cục cho các kết nối đến và đi. Theo mặc định, tham số này được đặt thành 125, nghĩa là nút của bạn sẽ không bao giờ chấp nhận quá 125 kết nối.
- maxuploadtarget`: giới hạn tải lên để giới hạn băng thông trong khung thời gian 24 giờ. Giới hạn này không làm ảnh hưởng đến việc truyền tải Elements thiết yếu gần đây.
- `onlynet`: giới hạn kết nối đi chỉ với các mạng được chọn (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Ví dụ: nếu bạn muốn nút của mình chỉ kết nối với mạng Bitcoin qua Tor, bạn có thể bật tham số `onlynet=onion` và tắt kết nối đến (hoặc chỉ cho phép kết nối qua Tor).
- `dnsseed`: cho phép hoặc không cho phép _DNS seeds_ yêu cầu các đối tác khi nhóm Address cục bộ của bạn sắp hết (mặc định: `1`, trừ khi `-connect` hoặc `-maxconnections=0`).
- `forcednsseed`: buộc _hạt giống DNS_ phải được yêu cầu khi khởi động, ngay cả khi bạn đã có địa chỉ trong kho (mặc định: `0`).
- `fixedseeds`: Cho phép sử dụng *các nút seed* (danh sách Address được mã hóa cứng) nếu _hạt giống DNS_ không thành công hoặc bị vô hiệu hóa (mặc định: `1`).
- `dns`: Cho phép giải quyết DNS nói chung (ví dụ: đối với `-addnode`/`-seednode`/`-connect`).



Theo mặc định, nút của bạn giao tiếp qua clearnet, Tor và I2P. Điều này có nghĩa là các nút ngang hàng mà nó kết nối trên clearnet có thể thấy địa chỉ IP công khai Address của bạn, và ISP của bạn có thể sẽ phát hiện ra rằng bạn đang chạy nút Bitcoin (mặc dù P2P Transport V2 khiến ISP khó nghe lén hơn). Điều này không hẳn là vấn đề, nhưng nếu bạn muốn tránh rò rỉ thông tin này, bạn có thể kết nối nút của mình hoàn toàn qua mạng Tor.



Để kích hoạt Tor hoàn toàn, bạn cần buộc Bitcoin core chỉ sử dụng mạng này và tạo một dịch vụ ẩn cho các kết nối đến (nếu bạn muốn kích hoạt chúng). Trong `Bitcoin.conf`, bạn cần thêm cấu hình này:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `nghe=1`,
- liên kết=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Tất cả các kết nối P2P của bạn đều đi qua Tor. Nút của bạn nhận được `.onion` Address cho các kết nối đến, do đó không cần mở cổng trên bộ định tuyến. Nhà cung cấp dịch vụ Internet (ISP) của bạn chỉ thấy lưu lượng Tor, và các đối tác của bạn không biết địa chỉ IP công cộng thực tế của bạn là Address.



Để tránh việc phân giải DNS không rõ ràng, bạn có thể thêm `dnsseed=0` và `dns=0` vào cấu hình của mình. Sau đó, bạn sẽ cần phải tự tay cung cấp các nút ngang hàng `.onion` thông qua `seednode=` hoặc `addnode=`, vì nếu không, việc khám phá các nút mới sẽ khó khăn.



Rõ ràng, nếu bạn là người mới bắt đầu, tôi khuyên bạn nên tạm thời để nguyên các thiết lập mạng này. Cấu hình mặc định thường là đủ.



### Mempool và chính sách chuyển tiếp



#### Các thông số cơ bản



Sau đây là các tham số cơ bản bạn có thể sửa đổi trên `Bitcoin.conf` liên quan đến việc quản lý Mempool và chuyển tiếp các giao dịch chưa được xác nhận:





- `maxmempool=<n>`: Giới hạn kích thước tối đa của Mempool cục bộ ở mức `<n>` megabyte (mặc định: `300`). Khi đạt đến giới hạn, nút của bạn sẽ tự động tăng ngưỡng phí hiệu dụng và ưu tiên các giao dịch ít sinh lời nhất (dựa trên mức phí, không phải giá trị tuyệt đối) để duy trì dưới giới hạn. Bạn có thể giữ nguyên cài đặt này. Việc tăng ngưỡng này có thể hữu ích nếu bạn sử dụng Mining một mình, hoặc nếu bạn muốn có cái nhìn chính xác hơn về tình trạng tắc nghẽn của Mempool và cải thiện ước tính phí. Ngược lại, việc giảm ngưỡng này sẽ tiết kiệm RAM và, ở mức độ thấp hơn, các tài nguyên hệ thống khác.





- `mempoolexpiry=<n>`: Thời gian lưu giữ tối đa cho các giao dịch chưa được xác nhận trong Mempool (tính bằng giờ, mặc định: `336`). Sau thời gian này, các giao dịch sẽ bị xóa ngay cả khi vẫn còn dung lượng trống.





- `persistmempool=1`: Lưu ảnh chụp nhanh của Mempool khi máy tính đang dừng và tải lại khi khởi động lại (mặc định: `1`). Điều này giúp tăng tốc độ phục hồi sau khi khởi động lại, tránh việc phải học lại trạng thái qua mạng.





- `maxorphantx=<n>`: Số lượng tối đa các giao dịch mồ côi được giữ lại (đầu vào phụ thuộc từ các UTXO chưa được tìm thấy trong bộ UTXO, mặc định: `100`). Vượt quá ngưỡng này, các giao dịch cũ nhất sẽ bị xóa để tránh việc bộ nhớ đệm tăng trưởng không kiểm soát.





- blocksonly=1`: Vô hiệu hóa việc chấp nhận và truyền lại các giao dịch chưa được xác nhận nhận được từ các peer (trừ khi được cấp quyền đặc biệt). Giờ đây, node chỉ tải lên và quảng bá các khối. Các giao dịch được tạo cục bộ vẫn có thể được phát sóng (để sử dụng node của bạn với phần mềm Wallet). Điều này giúp giảm đáng kể yêu cầu về băng thông và RAM, mặc dù phải trả giá bằng việc giảm tính hữu dụng của relay và hoàn toàn không quen thuộc với Mempool.





- `minrelaytxfee=<n>`: Mức phí tối thiểu (tính bằng BTC/kvB) mà dưới mức đó, giao dịch sẽ không được chấp nhận trong Mempool của nút và không được chuyển tiếp đến các nút ngang hàng (mặc định: `0,00001` = 1 sat/vB). Giá trị này càng cao, nút của bạn càng lọc các giao dịch chi phí thấp một cách tích cực.





- `mempoolfullrbf=1`: Chấp nhận các giao dịch RBF ngay cả khi không có tín hiệu RBF rõ ràng trong giao dịch được thay thế. Với chính sách "*full-RBF*" này, một giao dịch cung cấp mức phí cao hơn có thể thay thế một giao dịch khác trong Mempool nếu các điều kiện thay thế khác được đáp ứng.



Xin nhắc lại, RBF là một cơ chế giao dịch cho phép người gửi thay thế một giao dịch bằng một giao dịch có phí cao hơn để tăng tốc độ xác nhận. Nếu một giao dịch có phí quá thấp vẫn bị chặn, người gửi có thể sử dụng *Replace-by-fee* để tăng phí và ưu tiên giao dịch thay thế của họ trong mempool và với thợ đào.



#### Cài đặt nâng cao và cụ thể



Sau đây là các cài đặt nâng cao cho Mempool và chính sách rơle. Nếu bạn là người mới bắt đầu, bạn không cần phải điều chỉnh các cài đặt này:





- datacarrier=1`: Cho phép chuyển tiếp và (nếu Mining thông qua nút) bao gồm các giao dịch mang dữ liệu phi tài chính thông qua đầu ra `OP_RETURN` (mặc định: `1`). Việc hủy kích hoạt tham số này sẽ làm giảm nhẹ diện tích bề mặt cho dữ liệu spam phi tài chính, đồng thời làm giảm khả năng tương thích với một số mục đích sử dụng nhất định. Trong mọi trường hợp, bạn phải chấp nhận `OP_RETURN` đã được khai thác.





- `datacarriersize=<n>`: Kích thước tối đa (tính bằng byte) của `OP_RETURN` mà nút chuyển tiếp (mặc định: `83`). Việc giảm giá trị này sẽ hạn chế tải trọng được truyền qua `OP_RETURN`. Lưu ý rằng giới hạn này sẽ bị xóa theo mặc định trong phiên bản Bitcoin core trong tương lai.





- `bytespersigop=<n>`: Tham số chuyển đổi các giao dịch chữ ký thành các byte tương đương để đánh giá giới hạn chuyển tiếp (mặc định: `20`). Điều này sẽ ảnh hưởng đến việc chấp nhận các giao dịch giàu `sigops` theo các quy tắc chính sách cục bộ.





- `permitbaremultisig=1`: Cho phép chuyển tiếp các giao dịch P2MS *bare-Multisig* (mặc định: `1`). Đây là mẫu tập lệnh lâu đời nhất để thiết lập điều kiện đa chữ ký trên UTXO (được Gavin Andresen phát minh vào năm 2011).





- `whitelistrelay=1`: Tự động cấp quyền chuyển tiếp cho các peer đến được liệt kê trong danh sách trắng (mặc định: `1`). Các peer này sẽ được relay chấp nhận giao dịch ngay cả khi node của bạn không ở chế độ chuyển tiếp chung.





- `whitelistforcerelay=1`: Gán quyền "*forcerelay*" cho các nút ngang hàng được liệt kê trắng với quyền mặc định (mặc định: `0`). Sau đó, nút sẽ chuyển tiếp các giao dịch của chúng ngay cả khi chúng đã có trong Mempool, do đó bỏ qua các cơ chế chống trùng lặp.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Liên kết một phạm vi Interface hoặc Address và gán các quyền chi tiết cho các đối tác tương ứng: `relay`, `forcerelay`, `Mempool` (yêu cầu nội dung Mempool), `noban`, `download`, `addr`, `bloomfilter`. Điều này có thể hữu ích để cấp quyền truy cập đặc quyền cho các đối tác đáng tin cậy (chẳng hạn như cổng, mạng LAN và dịch vụ nội bộ).





- peerbloomfilters=1`: Bật hỗ trợ cho bộ lọc Bloom (BIP37) để phục vụ các khối/giao dịch đã lọc cho máy khách mỏng (mặc định: `0`). Cảnh báo: điều này làm tăng tải cho tài nguyên của bạn.





- peerblockfilters=1`: Cung cấp bộ lọc nhỏ gọn BIP157 (*Neutrino*) cho các đối tác (mặc định: `0`).





- `blockreconstructionextratxn=<n>`: Số lượng giao dịch bổ sung được lưu giữ trong bộ nhớ để xây dựng lại các khối nén (mặc định: `100`). Cải thiện khả năng thành công của việc tái tạo trong quá trình đồng bộ hóa nén, với chi phí sử dụng ít bộ nhớ hơn.



Xin nhắc lại, tất cả các quy tắc chuyển tiếp này không ảnh hưởng đến tính hợp lệ của các giao dịch được bao gồm trong một khối hợp lệ. Chúng chỉ giúp điều chỉnh đóng góp của bạn vào chuyển tiếp, bảo vệ tài nguyên của bạn và giúp nút của bạn có thể dự đoán được trong các môi trường hạn chế, nhưng không bao giờ cho phép bạn từ chối các khối tuân thủ các quy tắc đồng thuận.



### Ví



Bạn cũng có thể điều chỉnh cách quản lý ví của mình trong tệp `Bitcoin.conf`. Nếu bạn không sử dụng Wallet trực tiếp trong Core mà sử dụng phần mềm quản lý bên ngoài như Sparrow hoặc Liana, các thông số này sẽ không mấy quan trọng:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Xác định định dạng của các địa chỉ do Wallet tạo ra để tiếp nhận.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Buộc định dạng Exchange Address (phần còn lại của thông tin đầu vào trên một khoản thanh toán duy nhất).





- `Wallet=<đường dẫn>`: Tải Wallet hiện có khi khởi động (có thể lặp lại để tải nhiều ví).





- `walletdir=<dir>`: Thư mục chứa ví (mặc định: `<datadir>/wallets` nếu có, nếu không thì là `<datadir>`). Điều này có thể hữu ích nếu bạn muốn lưu trữ ví trên một ổ đĩa chuyên dụng hoặc được mã hóa.





- `walletbroadcast=1`: Tự động phát sóng các giao dịch được tạo bởi ví đã tải (mặc định: `1`). Đặt thành `0` nếu bạn muốn quản lý phát sóng qua kênh khác.





- `walletrbf=1`: Cho phép RBF chọn tham gia để báo hiệu RBF trên tất cả các giao dịch (mặc định: `1`). Cho phép bạn tăng phí sau này trong trường hợp giao dịch bị chặn.





- `txconfirmtarget=<n>`: Mục tiêu xác nhận cho giao dịch (tính theo số khối, mặc định: `6`). Wallet sẽ tự động đặt mức phí cho giao dịch được xác nhận trong số khối này.





- `paytxfee=<amt>`: Mức phí cố định (BTC/kvB) áp dụng cho các giao dịch Wallet. Tránh sử dụng chung: sử dụng ước tính thích ứng thông qua `txconfirmtarget`.





- fallbackfee=<amt>`: Tỷ lệ dự phòng (BTC/kvB) được sử dụng nếu bộ ước tính hết dữ liệu (mặc định: `0,00`). Đặt thành 0 sẽ vô hiệu hóa hoàn toàn tính năng dự phòng.





- `mintxfee=<amt>`: Ngưỡng tối thiểu (BTC/kvB) để Wallet tạo giao dịch (mặc định: `0,00001`). Wallet sẽ từ chối tạo giao dịch dưới ngưỡng này.





- `maxtxfee=<amt>`: Giới hạn tuyệt đối cho tổng phí cho giao dịch Wallet (mặc định: `0,10` BTC). Bảo vệ khỏi mức phí cao bất thường có thể làm mất bitcoin một cách không cần thiết.





- `avoidpartialspends=1`: Chọn UTXO theo cụm Address để tránh chi tiêu một phần.





- `spendzeroconfchange=1`: Cho phép sử dụng lại UTXO Exchange chưa được xác nhận làm mục nhập trong giao dịch mới (mặc định: `1`).





- `consolidatefeerate=<amt>`: Mức giá tối đa (BTC/kvB) mà ngoài mức đó, Wallet sẽ tránh việc thêm nhiều đầu vào hơn mức cần thiết để hợp nhất. Điều này cho phép hợp nhất theo cơ hội với giá thấp và giảm chi phí khi chi phí cao.





- `maxapsfee=<n>`: Ngân sách cho các khoản phí bổ sung (BTC, giá trị tuyệt đối) mà Wallet đồng ý thanh toán để kích hoạt tùy chọn "*tránh chi tiêu một phần*".





- `discardfee=<amt>`: Tỷ giá (BTC/kvB) cho biết mức độ chấp nhận bỏ Exchange của bạn bằng cách thêm nó vào phí. Các đầu ra có giá trị hơn một phần ba giá trị của chúng ở mức giá này sẽ bị loại bỏ.





- `keypool=<n>`: Kích thước của nhóm Address được tạo sẵn (mặc định: `1000`). Giá trị quá nhỏ sẽ làm tăng nguy cơ khôi phục không hoàn chỉnh.





- `disablewallet=1`: Khởi động Bitcoin core mà không cần hệ thống con Wallet và vô hiệu hóa các RPC liên quan. Giảm bề mặt tấn công và dấu vết nếu nút chỉ được sử dụng để xác thực/giải phóng.



### Lưu trữ, lập chỉ mục và hiệu suất



Tệp cấu hình cũng cho phép bạn điều chỉnh các thông số liên quan đến máy của mình. Điều này đặc biệt hữu ích nếu bạn có tài nguyên hạn chế, hoặc ngược lại, dung lượng khả dụng lớn:





- `datadir=<dir>`: Đặt thư mục dữ liệu chính của Bitcoin core.





- `blocksdir=<dir>`: Tách vị trí của các tệp khối (`blocks/blk*.dat` và `blocks/rev*.dat`) khỏi `datadir`. Điều này có thể hữu ích khi đặt kho lưu trữ khối trên một ổ đĩa khác, trong khi vẫn giữ cơ sở trạng thái (`chainstate/`) trên một phương tiện nhanh hơn, chẳng hạn.





- `dbcache=<n>`: Phân bổ `<n>` MiB cho bộ nhớ đệm cơ sở dữ liệu (*LevelDB*) được sử dụng bởi chỉ mục khối và `chainstate` (mặc định: `450`). Giá trị càng cao, IBD và xác thực hiện tại càng nhanh, nhưng tiêu tốn RAM nhiều hơn.





- `prune=<n>`: Cho phép cắt bớt các tệp khối và đặt mục tiêu dung lượng đĩa trong MiB (mặc định: `0` = vô hiệu hóa; `1` = cắt bớt thủ công thông qua RPC; `>=550` = tự động cắt bớt bên dưới mục tiêu). Không tương thích với `txindex=1`. Nút vẫn là nút xác thực đầy đủ, nhưng không thể cung cấp lịch sử cũ nữa. Tùy chọn này đặc biệt hữu ích nếu dung lượng đĩa của bạn bị hạn chế, ví dụ: khi cài đặt một nút trên máy tính tại nhà.





- txindex=1`: Xây dựng và duy trì một chỉ mục toàn cầu cho các giao dịch đã xác nhận. Cần thiết cho một số truy vấn nhất định (`getrawtransaction` không phải Wallet) và cho mục đích khám phá, nhưng làm tăng đáng kể dung lượng ổ đĩa. Không tương thích với chế độ pruned.





- `assumevalid=<hex>`: Chỉ ra một khối được coi là hợp lệ, cho phép bạn bỏ qua việc kiểm tra tập lệnh đối với khối tổ tiên của nó (đặt `0` để kiểm tra mọi thứ). Xem chương trước để biết thêm thông tin.





- `reindex=1`: Tái tạo chỉ mục khối và trạng thái (`chainstate`) từ các tệp `blk*.dat` trên đĩa. Đồng thời tái tạo các chỉ mục hoạt động tùy chọn. Đây là một thao tác tốn thời gian để sửa chữa cơ sở dữ liệu bị hỏng hoặc kích hoạt/hủy kích hoạt các chỉ mục nặng một cách sạch sẽ.





- `reindex-chainstate=1`: Chỉ xây dựng lại `chainstate` từ chỉ mục khối hiện tại. Ưu tiên khi các tệp khối hoạt động tốt.





- `blockfilterindex=<type>`: Duy trì chỉ mục của các bộ lọc khối nhỏ gọn (ví dụ: `basic`) được sử dụng bởi máy khách mỏng (BIP157/158) và một số RPC. Mặc định bị tắt (`0`). Tiêu tốn thêm dung lượng đĩa và thời gian lập chỉ mục.





- `coinstatsindex=1`: Duy trì chỉ mục thống kê tập hợp UTXO được vận hành bởi lệnh gọi `gettxoutsetinfo`. Hữu ích cho việc kiểm toán và đo lường, loại bỏ nhu cầu tính toán lại tốn kém. Mặc định bị tắt.





- `loadblock=<file>`: Nhập khối khi khởi động từ tệp `blk*.dat` bên ngoài. Được sử dụng để tải trước lịch sử từ nguồn ngoại tuyến (bản sao cục bộ, phương tiện bên ngoài) nhằm tăng tốc quá trình khởi tạo.





- `par=<n>`: Thiết lập số luồng xác minh tập lệnh (từ `-10` đến `15`, `0` = tự động, `<0` = để trống số lõi này). Cho phép bạn điều chỉnh chế độ song song của CPU trong quá trình xác thực. Chế độ tự động phù hợp trong hầu hết các trường hợp.





- `debuglogfile=<file>`: Chỉ định vị trí của nhật ký `debug.log`.





- `shrinkdebugfile=1`: Giảm kích thước của `debug.log` khi khởi động (mặc định: `1` khi `-debug` không hoạt động).





- `settings=<file>`: Đường dẫn đến tệp cài đặt động `settings.json`.



### RPC truy cập và an toàn vận hành



Cuối cùng, tệp `Bitcoin.conf` cũng cho phép bạn cấu hình các tham số truy cập cho nút của mình. Hãy thận trọng với các thiết lập này, đặc biệt nếu bạn mới bắt đầu: tránh thay đổi chúng nếu chưa hiểu rõ ý nghĩa, vì điều này có thể gây ra lỗ hổng bảo mật.





- `server=1`: Kích hoạt máy chủ JSON-RPC. Thiết yếu nếu bạn đang chạy `bitcoind` thông qua `bitcoin-cli` hoặc ứng dụng của bên thứ ba. Tắt (`0`) trên một nút chỉ xác thực, không hiển thị bất kỳ API nào hoặc đã sử dụng máy chủ Electrum.





- `rpcbind=<addr>[:port]`: Máy chủ RPC đang lắng nghe Address/cổng. Theo mặc định, việc lắng nghe chỉ được thực hiện cục bộ (`127.0.0.1` và `::1`). Tham số này bị bỏ qua nếu `rpcallowip` không được định nghĩa. Sử dụng tham số này để hạn chế rõ ràng Interface.





- `rpcport=<port>`: Cổng RPC (mặc định: `8332` trên Mainnet, `18332` trên Testnet, `38332` trên dấu trang, `18443` trên regtest).





- `rpcallowip=<ip|cidr>`: Cho phép máy khách RPC từ một IP hoặc mạng con nhất định (có thể lặp lại). Sử dụng kết hợp với `rpcbind` để chỉ hiển thị API cho một phân đoạn đáng tin cậy (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Phương thức xác thực RPC được đề xuất (mật khẩu băm). Cho phép nhập nhiều lần và tránh lưu trữ bí mật dưới dạng văn bản thuần túy.





- `rpccookiefile=<path>`: Đường dẫn đến cookie xác thực (mặc định: tệp `.cookie` trong `datadir/`). Đường dẫn này được sử dụng cho cùng một người dùng truy cập cục bộ mà không cần quản lý mật khẩu cố định. Ví dụ: bạn có thể sử dụng nó để kết nối Liana Wallet với Bitcoin core của bạn trên cùng một máy.





- `rpcuser=<user>` / `rpcpassword=<pw>`: Xác thực RPC cổ điển với mật khẩu dạng văn bản thuần túy. Tránh sử dụng tùy chọn này để thay thế bằng `rpcauth` hoặc cookie.





- `rpcthreads=<n>`: Số luồng để phục vụ các lệnh gọi RPC (mặc định: `4`). Tăng giá trị này nếu bạn có lượng lệnh gọi cao ở phía giám sát/công cụ bên ngoài.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Danh sách trắng các API được ủy quyền. Giảm thiểu bề mặt tấn công bằng cách hạn chế các phương thức có thể truy cập.





- `rpcwhitelistdefault=1|0`: Hành vi danh sách trắng mặc định: nếu được bật và danh sách trắng được sử dụng, các cuộc gọi không được liệt kê sẽ bị từ chối. Điều này cũng có thể áp dụng một tập hợp rỗng mặc định (không cho phép cuộc gọi) miễn là không có gì được liệt kê rõ ràng.





- `rest=1`: Bật REST API công khai (mặc định bị tắt). Chỉ được hiển thị trên mạng đáng tin cậy (cảnh báo tương tự như JSON-RPC).





- `conf=<file>`: Chỉ định, trên dòng lệnh, một tệp cấu hình chỉ đọc. Hữu ích để đóng băng cấu hình thực thi (không thể thay đổi) ở phía ops.





- `includeconf=<file>`: Tải một tệp cấu hình bổ sung (đường dẫn tương đối đến `datadir/`). Cho phép phân tách các vai trò: cơ sở chung + quá tải cục bộ nhạy cảm.





- `daemon=1` / `daemonwait=1`: Khởi động `bitcoind` ở chế độ nền và chờ quá trình khởi tạo hoàn tất trước khi bàn giao với `daemonwait`. Điều này giúp tích hợp dễ dàng hơn với các trình giám sát (systemd, runit).





- `pid=<tệp>`: Vị trí của tệp PID.





- `sandbox=<log-and-abort|abort>`: Cho phép hộp cát các cuộc gọi hệ thống thử nghiệm: chỉ các cuộc gọi hệ thống mong đợi mới được phép.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Thực thi lệnh khi khởi động hoặc tắt máy.





- `alertnotify=<cmd>`: Kích hoạt lệnh khi nhận được cảnh báo.





- `blocknotify=<cmd>`: Thực thi lệnh cho mỗi khối mới.





- `debug=<category>|1` / `debugexclude=<category>`: Bật/tắt các danh mục nhật ký chi tiết (ví dụ: `net`, `Mempool`, `RPC`, `validation`...).





- `logips=1`: Ghi lại địa chỉ IP.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Thêm vị trí nguồn, tên luồng và dấu thời gian chính xác vào nhật ký.





- `printtoconsole=1`: Gửi dấu vết/gỡ lỗi đến bảng điều khiển (*stdout*).





- `help-debug=1`: Hiển thị tùy chọn gỡ lỗi trợ giúp và thoát.





- `uacomment=<cmt>`: Thêm bình luận vào User-Agent P2P.



Chúng ta đã hoàn tất việc liệt kê hầu hết các tham số cấu hình. Tệp `Bitcoin.conf` này cấu thành bảng điều khiển thực sự của nút của bạn: nó định nghĩa cấu hình mạng, quản lý Mempool, sử dụng đĩa và bộ nhớ, lập chỉ mục và quản trị chung. Nếu bạn muốn tìm hiểu thêm về tệp này và tạo một tệp phù hợp với nhu cầu của mình, tôi khuyên bạn nên sử dụng [trình tạo của Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/).



Chúng ta đã đi đến phần kết thúc của khóa học BTC 202 này, khóa học sẽ giúp bạn không chỉ hiểu được những kiến thức cơ bản về cách thức hoạt động và tương tác của các nút trong hệ thống, mà còn thiết lập nút riêng của mình. Giờ đây, bạn đã là một Bitcoiner có chủ quyền, với tài khoản tự quản lý Wallet, phát sóng các giao dịch của mình thông qua nút riêng. Xin chúc mừng!



Bây giờ bạn có thể chuyển sang phần cuối cùng của khóa học, nơi bạn có thể đánh giá BTC 202, sau đó nhận bằng tốt nghiệp để kiểm tra xem bạn đã nắm vững tất cả các khái niệm được đề cập hay chưa.



Bây giờ bạn có một số lựa chọn. Bước hợp lý tiếp theo là thiết lập nút Lightning của riêng bạn, cho phép bạn hoàn toàn độc lập với các giao dịch off-chain. Đây sẽ là chủ đề của một khóa học sắp tới, dự kiến được xuất bản vào mùa thu năm 2025 trên Plan ₿ Network.



Trong khi đó, tôi mời bạn khám phá khóa đào tạo BTC 204, khóa đào tạo này sẽ giúp bạn hiểu và nắm vững các nguyên tắc bảo vệ quyền riêng tư khi sử dụng Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Phần cuối


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Đánh giá & Xếp hạng


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Kỳ thi cuối kỳ


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Phần kết luận


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>