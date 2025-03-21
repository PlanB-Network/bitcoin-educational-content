---
name: Xây dựng với Elements và Liquid Network
goal: Học cách sử dụng và phát triển với nền tảng blockchain mã nguồn mở Elements và các tính năng chính của nó
objectives: 

  - Hiểu các khái niệm cơ bản của nền tảng blockchain Elements và sidechain Liquid.
  - Tìm hiểu cách thiết lập và chạy các nút Elements cho cấu hình độc lập và chuỗi phụ.
  - Có được kinh nghiệm thực tế với phương thức ký khối liên bang và phương thức chốt 2 chiều liên bang.
  - Thiết lập và quản lý môi trường blockchain an toàn, hiệu quả cho các trường hợp sử dụng thực tế.

---
# Xây dựng trên chất lỏng và các yếu tố

Khám phá các tính năng và khả năng nâng cao của Liquid and Elements, và tìm hiểu cách sử dụng hiệu quả các công cụ này để nâng cao các dự án phát triển của bạn. Khóa đào tạo này cung cấp nền tảng lý thuyết và thực hành hoàn chỉnh, cho phép bạn thành thạo các tính năng như Giao dịch bảo mật, Tài sản đã phát hành và Ký khối liên bang.

Liquid, dựa trên khuôn khổ Elements, được thiết kế để cải thiện quyền riêng tư, khả năng mở rộng và chức năng cho các giải pháp tài chính và kỹ thuật. Trong khóa học này, bạn sẽ có được kinh nghiệm thực tế về phát hành và quản lý tài sản, Federated 2-Way Peg và sử dụng các công cụ như elementsd và elements-cli, giúp bạn tạo ra các giải pháp sáng tạo phù hợp với nhu cầu của mình.

Khóa học này được thiết kế riêng cho các nhà phát triển ở mọi cấp độ kinh nghiệm. Người mới bắt đầu và người dùng trung cấp sẽ tìm thấy các giải thích dễ hiểu và ví dụ thực tế, trong khi người dùng nâng cao có thể tìm hiểu sâu hơn về các chi tiết kỹ thuật và các tính năng ít được biết đến của Liquid và Elements.

Hãy tham gia cùng chúng tôi để nâng cao kỹ năng của bạn, khai phá toàn bộ tiềm năng của Liquid và Elements, đồng thời tạo ra các công cụ có tác động lớn cho tương lai đổi mới của Liquid.

+++
# Giới thiệu

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Giới thiệu khóa học

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

Mục đích của Elements Academy là giới thiệu và giải thích các khái niệm chính của Elements, nền tảng mã nguồn mở mà Liquid được xây dựng trên đó. Đến cuối khóa học, bạn sẽ hiểu rõ về các tính năng chính của Elements, chẳng hạn như Giao dịch bí mật và Tài sản đã phát hành, cũng như các quy trình liên quan đến việc chạy Elements Core.

Mỗi phần sẽ có các bài học với văn bản giải thích và video kết thúc bằng bài kiểm tra. Số lượng câu hỏi liên quan đến quy mô của chủ đề trước đó. Phần 10 sẽ tóm tắt nội dung khóa học và kết thúc bằng bài kiểm tra lớn hơn.

Mọi thắc mắc, yêu cầu cung cấp thêm thông tin hoặc thắc mắc về câu trả lời bài kiểm tra có thể liên hệ với giáo viên James Dorfman.

## Tổng quan về các yếu tố

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements là một nền tảng blockchain mã nguồn mở, có khả năng sử dụng sidechain, cung cấp quyền truy cập vào các tính năng mạnh mẽ do các thành viên cộng đồng phát triển, chẳng hạn như Giao dịch bí mật và Tài sản đã phát hành.

Về cơ bản, Elements là một giao thức cho phép hình thành sự đồng thuận xung quanh lịch sử giao dịch và các quy tắc chi phối việc chuyển giao và tạo ra tài sản được lưu trữ trong sổ cái blockchain phân tán.

Bạn có thể dễ dàng tìm thấy thông tin cơ bản hơn về Elements trên trang web Elements Project (https://elementsproject.org/), blog chính thức của Liquid (https://blog.liquid.net/) và cổng thông tin dành cho nhà phát triển (https://liquid.net/devs).

### Các yếu tố

Ra mắt vào năm 2015, Elements giúp giảm chi phí phát triển và nghiên cứu nội bộ và khai thác công nghệ blockchain mới nhất, mở ra nhiều trường hợp sử dụng mới để triển khai. Một blockchain dựa trên Elements có thể hoạt động như một Blockchain độc lập hoặc được gắn với một Blockchain khác và chạy như một Sidechain. Chạy Elements như một Sidechain cho phép chuyển giao tài sản có thể xác minh được giữa các blockchain khác nhau.

Được xây dựng dựa trên và mở rộng cơ sở mã của Bitcoin, nó cho phép các nhà phát triển quen thuộc với API bitcoind tạo ra các blockchain hoạt động và thử nghiệm các dự án bằng chứng khái niệm một cách nhanh chóng và tiết kiệm chi phí. Được xây dựng trên cơ sở mã Bitcoin cũng cho phép Elements hoạt động như một nền tảng thử nghiệm cho các thay đổi đối với chính giao thức Bitcoin.

Sau đây là một số tính năng chính của Elements.

#### Giao dịch bí mật

Theo mặc định, tất cả các địa chỉ trong Elements đều được ẩn bằng Giao dịch bí mật. Ẩn là quá trình mà số lượng và loại tài sản được chuyển giao được ẩn bằng mật mã khỏi mọi người, ngoại trừ những người tham gia và những người mà họ chọn để tiết lộ khóa ẩn.

#### Tài sản đã phát hành

Tài sản đã phát hành trên Elements cho phép nhiều loại tài sản được phát hành và chuyển giao giữa những người tham gia mạng lưới. Tài sản đã phát hành cũng được hưởng lợi từ Giao dịch bí mật và có thể được phát hành lại hoặc hủy bỏ bởi bất kỳ ai nắm giữ mã thông báo phát hành lại có liên quan.

#### Peg 2 chiều liên bang

Elements là một nền tảng blockchain mục đích chung cũng có thể được "gắn" vào một blockchain hiện có (như Bitcoin) để cho phép chuyển giao tài sản theo hai chiều từ chuỗi này sang chuỗi khác. Việc triển khai Elements như một sidechain cho phép bạn giải quyết một số thuộc tính vốn có của chuỗi chính, đồng thời vẫn giữ được mức độ bảo mật tốt do tài sản được bảo mật trên chuỗi chính cung cấp.

#### Khối đã ký

Elements sử dụng Liên đoàn mạnh mẽ của những người ký tên, được gọi là Người ký khối, những người ký và tạo khối theo cách đáng tin cậy và kịp thời. Điều này loại bỏ độ trễ giao dịch của quy trình khai thác PoW, vốn chịu sự thay đổi lớn về thời gian khối do phân phối Poisson ngẫu nhiên của nó. Quy trình Ký khối liên bang đạt được khả năng tạo khối đáng tin cậy mà không cần đến sự tin tưởng của bên thứ ba hoặc khai thác dựa trên `thuật toán` tính toán.

Elements bổ sung tất cả các tính năng này vào cơ sở dữ liệu mã Bitcoin Core, mở rộng khả năng của giao thức chuỗi chính và cho phép các trường hợp sử dụng kinh doanh mới khi triển khai dưới dạng chuỗi phụ hoặc giải pháp chuỗi khối độc lập.

# Yếu tố

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Nguyên lý hoạt động của Elements

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements cung cấp giải pháp kỹ thuật cho các vấn đề mà người dùng blockchain phải đối mặt hàng ngày; độ trễ giao dịch, thiếu quyền riêng tư và rủi ro thay thế.

Elements khắc phục những vấn đề này thông qua việc sử dụng Giao dịch bảo mật và Ký khối liên bang.

Không giống như mạng lưới Bitcoin, quá trình ký khối trong Elements không phụ thuộc vào Chữ ký đa bên thành viên động (DMMS) và Bằng chứng công việc (PoW). Thay vào đó, Elements sử dụng Liên đoàn mạnh của những người ký tên, được gọi là Người ký khối, những người có thể ký và tạo khối một cách đáng tin cậy và kịp thời. Điều này loại bỏ độ trễ giao dịch của quá trình khai thác PoW, vốn phụ thuộc vào sự thay đổi thời gian khối lớn do phân phối Poisson ngẫu nhiên của nó. Quá trình Ký khối liên bang đạt được khả năng tạo khối đáng tin cậy mà không cần sự tin tưởng của bên thứ ba.

Các thành phần có thể chạy như một chuỗi phụ của một blockchain khác, chẳng hạn như Bitcoin, hoặc như một blockchain độc lập mà không phụ thuộc vào các mạng khác.

Khi được sử dụng như một sidechain, Strong Federation cũng bao gồm các thành viên cho phép chuyển giao tài sản an toàn và được kiểm soát giữa một mainchain và một sidechain Elements. Việc chuyển giao tài sản được kiểm soát được gọi là Federated 2-Way Peg và các thành viên thực hiện vai trò chuyển giao tài sản được gọi là Watchmen.

Các quy trình liên quan đến việc vận hành mạng lưới Elements và vai trò của những người tham gia mạng lưới rất quan trọng để hiểu cách thức hoạt động của Elements.

Cho dù được triển khai dưới dạng chuỗi phụ hay chuỗi khối độc lập, Elements đều sử dụng Liên đoàn mạnh của Người ký khối để tạo ra các khối.

### Liên đoàn mạnh mẽ

Elements sử dụng mô hình đồng thuận đầu tiên được Blockstream đề xuất, được gọi là Strong Federations. Strong Federation không cần Proof of Work (PoW) mà thay vào đó dựa vào hành động tập thể của một nhóm những người tham gia không tin tưởng lẫn nhau, được gọi là Functionaries.

Các vai trò mà một Functionary có thể đảm nhiệm trong Strong Federation là: Block Signers và Watchmen. Block Signers là bắt buộc nếu bạn chạy Elements ở chế độ sidechain hoặc blockchain độc lập, trong khi Watchmen chỉ bắt buộc trong thiết lập sidechain.

Các hành động mà thành viên của Liên đoàn mạnh có thể thực hiện được chia thành hai vai trò riêng biệt nhằm tăng cường bảo mật và hạn chế thiệt hại mà kẻ tấn công có thể gây ra.

Khi kết hợp, vai trò của những người tham gia này cho phép Elements cung cấp cả khả năng tạo khối nhanh chóng (xác nhận giao dịch nhanh hơn và cuối cùng) và tài sản có thể chuyển nhượng được đảm bảo (tài sản được neo giá có thể liên kết trực tiếp với blockchain khác).

Bạn có thể đọc báo cáo chính thức của Strong Federations tại đây: https://blockstream.com/strong-federations.pdf

### Người ký tên khối

Một blockchain như Bitcoin được mở rộng khi bất kỳ ai tham gia vào một nhóm người ký khối năng động mở rộng chuỗi bằng cách chứng minh bằng chứng công việc đã sử dụng. Bản chất năng động của tập hợp này đưa ra các vấn đề về độ trễ vốn có trong các hệ thống như vậy.

Bằng cách sử dụng một bộ ký cố định, mô hình Liên bang thay thế bộ động bằng một bộ đã biết, lược đồ đa chữ ký. Giảm số lượng người tham gia cần thiết để mở rộng blockchain giúp tăng tốc độ và khả năng mở rộng của hệ thống, trong khi xác thực của tất cả các bên đảm bảo tính toàn vẹn của lịch sử giao dịch.

Việc ký khối liên bang bao gồm một số giai đoạn:


- Bước 1 - Người ký khối đề xuất các khối ứng cử viên theo cách vòng tròn cho tất cả những Người ký khối tham gia khác.
- Bước 2 - Mỗi Người ký khối sẽ thể hiện ý định của mình bằng cách cam kết ký vào khối ứng viên đã cho.
- Bước 3 - Nếu ngưỡng cam kết trước được đáp ứng, mỗi Người ký khối sẽ ký vào khối.
- Bước 4 - Nếu ngưỡng chữ ký (có thể khác với ngưỡng của bước 3) được đáp ứng, khối được chấp nhận và gửi đến mạng. Liên đoàn mạnh đã đạt được sự đồng thuận về khối giao dịch mới nhất.
- Bước 5 - Khối tiếp theo sẽ được Người ký khối tiếp theo đề xuất trong vòng tròn và quá trình này được lặp lại.

Vì việc tạo khối của Strong Federation không phải là xác suất và dựa trên một tập hợp cố định những người ký tên, nên nó sẽ không bao giờ phải chịu sự sắp xếp lại nhiều khối. Điều này cho phép giảm đáng kể thời gian chờ liên quan đến việc xác nhận giao dịch. Nó cũng loại bỏ động lực khai thác để kiếm lợi nhuận (tức là phần thưởng khối) và thay thế bằng động lực tham gia có hiệu quả vào một mạng lưới nơi tất cả những người tham gia đều có cùng một mục tiêu chung; đảm bảo mạng lưới tiếp tục hoạt động theo cách có lợi cho tất cả mọi người. Nó thực hiện điều này mà không đưa ra một điểm lỗi duy nhất hoặc yêu cầu tin cậy cao hơn.

### Các yếu tố như một Sidechain - Watchmen và Federated 2-Way Peg

Khi chạy như một sidechain, một số thành viên của Strong Federation có thêm một vai trò nữa cần thực hiện, đó là Watchmen. Watchmen chịu trách nhiệm chuyển giao tài sản vào và ra khỏi sidechain Elements, các quy trình được gọi là `Peg-In` và `Peg-Out`.

Để một sidechain hoạt động theo cách đáng tin cậy, nó phải cho phép những người tham gia xác minh rằng nguồn cung cấp tài sản được kiểm soát và có thể xác minh được. Một sidechain Elements sử dụng 2-Way Federated Peg để cho phép chuyển giao tài sản theo hai chiều vào và ra khỏi một blockchain Elements. Điều này đáp ứng các yêu cầu về phát hành có thể chứng minh được và chuyển giao giữa các chuỗi.

Tính năng Peg 2 chiều liên bang cho phép một tài sản có thể tương tác với các blockchain khác và đại diện cho tài sản gốc của blockchain khác. Bằng cách gắn blockchain của bạn với blockchain khác, bạn có thể mở rộng khả năng của mainchain và khắc phục một số hạn chế vốn có của nó.

Ở cấp độ cao, việc chuyển vào sidechain xảy ra khi ai đó gửi tài sản mainchain đến một địa chỉ được kiểm soát bởi ví Watchmen đa chữ ký. Điều này thực sự đóng băng tài sản trên mainchain. Sau đó, Watchmen xác thực giao dịch và giải phóng cùng một lượng tài sản liên quan trong sidechain. Tài sản được giải phóng được gửi đến ví sidechain có thể chứng minh quyền sở hữu đối với tài sản mainchain gốc. Quá trình này thực sự di chuyển tài sản từ chuỗi chính sang sidechain.

Để chuyển tài sản trở lại mainchain, người dùng thực hiện giao dịch chốt đặc biệt trên sidechain. Giao dịch này được kiểm tra bởi Watchmen, sau đó họ ký giao dịch chi tiêu từ ví đa chữ ký mà họ kiểm soát trên mainchain. Một số lượng người tham gia ngưỡng trong liên đoàn phải ký trước khi giao dịch mainchain có hiệu lực. Khi Watchmen gửi tài sản trở lại mainchain, họ cũng hủy số tiền tương ứng trên sidechain, về cơ bản là chuyển tài sản giữa các blockchain.

## Thiết lập và chạy các thành phần

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Vì Elements dựa trên cơ sở mã Bitcoin nên các thành phần tạo nên một mạng lưới hoạt động rất giống nhau.

Bản thân phần mềm nút Elements được gọi là `elementsd` và chạy như một daemon trên máy của người dùng. Daemon (hoặc dịch vụ trong Windows) là một chương trình chạy như một dịch vụ nền mà không cần sự kiểm soát trực tiếp của người dùng đã đăng nhập.

Lưu ý: Trong suốt tài liệu này, chúng tôi sẽ luôn gọi elementsd là phiên bản daemon, nhưng mọi thứ đều có thể thực hiện được bằng elements-qt, với điều kiện tùy chọn máy chủ được bật.

Daemon Elements kết nối với các nút khác trên mạng để có thể trao đổi dữ liệu giao dịch và khối, xác thực và mở rộng bản sao cục bộ của chuỗi khối mạng.

Phần mềm Elements cũng bao gồm một chương trình máy khách có tên là `elements-cli` cho phép bạn gửi lệnh Remote Procedure Call (RPC) đến elementsd từ dòng lệnh. Điều này có thể được sử dụng để truy vấn số dư ví, xem giao dịch hoặc dữ liệu khối hoặc phát giao dịch chẳng hạn. Thiết lập này sẽ quen thuộc với bất kỳ ai đã sử dụng các loại Bitcoin tương đương; bitcoind và bitcoin-cli.

Vì một nút Elements có thể được cấu hình bằng cách truyền tham số khi khởi động hoặc thông qua tệp cấu hình nên có thể có nhiều hơn một phiên bản chạy trên cùng một máy. Điều này hữu ích cho mục đích thử nghiệm và phát triển vì bạn có thể thiết lập mạng cục bộ của riêng mình trên một máy duy nhất, với mỗi nút Elements có bản sao dữ liệu blockchain riêng, quản lý nhóm giao dịch hợp lệ chưa được xác nhận và lắng nghe các yêu cầu RPC trên các cổng khác nhau.

### Kho lưu trữ mã và cộng đồng Elements

Elements là một dự án mã nguồn mở và mã nguồn của nó có thể được tìm thấy trong kho lưu trữ GitHub của Elements tại https://github.com/ElementsProject/elements. Kho lưu trữ này chứa mã nguồn cho các chương trình elementsd và elements-cli cùng với các công cụ cài đặt và xây dựng hỗ trợ, một bộ các bài kiểm tra và một số tài liệu hướng dẫn.

Để bổ sung cho kho lưu trữ mã, còn có trang web https://elementsproject.org, một nguồn tài nguyên tập trung vào cộng đồng chứa các giải thích về Elements là gì, cách thức hoạt động và phần hướng dẫn toàn diện. Hướng dẫn tập trung vào việc tìm hiểu về Elements bằng cách làm theo các ví dụ dòng lệnh và chỉ cho bạn cách xây dựng các ứng dụng web và máy tính để bàn đơn giản trên đó. Trang web này cũng liệt kê các diễn đàn thảo luận cộng đồng Elements phổ biến và bản thân nó được lưu trữ trên GitHub, cho phép cộng đồng đóng góp vào nội dung của trang web.

Để chạy Elements trên máy của bạn, trước tiên bạn cần sao chép (tải xuống bản sao) mã nguồn, cài đặt bất kỳ phụ thuộc nào mà mã có và cuối cùng là xây dựng daemon và các tệp thực thi của máy khách. Sau đó, phần mềm Elements đã sẵn sàng để được cấu hình và chạy.

## Cấu hình các nút và mạng

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Cài đặt cấu hình có thể được truyền đến một nút Elements khi khởi động để thay đổi cách chạy, xác thực dữ liệu, kết nối với các nút khác và khởi tạo dữ liệu blockchain của nút đó.

Các thiết lập được tải từ tệp `elements.conf` được chỉ định hoặc được truyền vào dưới dạng tham số thông qua dòng lệnh.

Một số thứ có thể thay đổi bằng cách sử dụng các thông số sau:


- Tên của tài sản mặc định được sử dụng trong triển khai blockchain độc lập.
- Số lượng tài sản ban đầu được tạo ra.
- Tài sản được sử dụng khi thanh toán phí giao dịch trên mạng.
- Vị trí lưu trữ các tệp dữ liệu blockchain.
- Thông tin xác thực RPC được sử dụng để kết nối với một nút Bitcoin.
- Ngưỡng `n trên m` cần đạt được và khóa công khai hợp lệ có thể ký các khối.
- Tập lệnh cần phải thỏa mãn để có thể chuyển tài sản vào và ra khỏi chuỗi phụ.
- Có nên kết nối với một nút Bitcoin như một chuỗi phụ hay không.

Nhiều trong số này là một phần của các quy tắc đồng thuận của mạng, vì vậy điều quan trọng là chúng phải được áp dụng trên tất cả các nút khi khởi động. Một số có thể được thay đổi sau khi chuỗi đã được khởi tạo nhưng một số cần được sửa sau khi chúng được sử dụng để khởi tạo chuỗi.

Việc sử dụng các tham số sẽ được đề cập sau trong khóa học khi chúng liên quan đến từng phần.

### Các thao tác cơ bản sử dụng dòng lệnh

Khóa học này sẽ trình bày các ví dụ sử dụng chương trình `elements-cli` để thực hiện các lệnh gọi RPC đến một hoặc nhiều nút Elements. Điều này được thực hiện từ phiên terminal và để làm cho các lệnh ngắn gọn hơn, `alias` sẽ được sử dụng. Theo quy ước này, khi bạn thấy một cái gì đó giống như các lệnh sau:

```bash
e1-dae
e1-cli getnewaddress
```

`e1-dae` và `e1-cli` thực ra là một phím tắt kiểu chữ sử dụng tính năng `alias` của terminal. `e1-dae` và `e1-cli` thực ra sẽ được thay thế khi lệnh được thực thi và lệnh sẽ chạy sẽ tương tự như sau:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Những gì chúng ta thấy ở trên là một lệnh gọi để khởi động trình nền Elements và một lệnh gọi đến các chương trình elements-cli nằm trong thư mục `$HOME/elements/src` và một giá trị cho tham số `datadir`. Tham số `datadir` cho phép chúng ta cho các phiên bản daemon và client biết vị trí đặt các tệp cấu hình của chúng và, trong trường hợp của daemon, vị trí lưu trữ bản sao blockchain của nó. Khi chúng chia sẻ một tệp cấu hình, client sẽ có thể thực hiện các lệnh gọi RPC đến daemon.

Bằng cách chạy lại lệnh trên, nhưng với giá trị `datadir` khác, chúng ta có thể khởi động nhiều hơn một phiên bản của Elements, mỗi phiên bản có bản sao riêng của blockchain và cài đặt cấu hình. Theo quy ước này, chúng ta sẽ sử dụng bí danh `e2-dae` và `e2-cli` trong khóa học để tham chiếu đến một thư mục datadir khác với e1. Vì vậy, ví dụ trên cho phiên bản `e2` thứ hai của chúng ta sẽ là:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

Điều này cho phép chúng tôi thực hiện mọi loại hoạt động như giao dịch tài sản giữa các nút, phát hành tài sản và kiểm tra việc sử dụng tính năng che giấu trong Giao dịch bí mật giữa các nút khác nhau trên cùng một mạng.

# Sử dụng Element Trường hợp sử dụng thực tế

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Giao dịch bí mật

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

Trong phần này, bạn sẽ học cách sử dụng tính năng Giao dịch bảo mật của Elements.

Theo mặc định, tất cả các địa chỉ trong Elements đều được ẩn bằng Giao dịch bảo mật, giúp giữ cho số lượng và loại tài sản được chuyển nhượng chỉ hiển thị với những người tham gia giao dịch (và những người mà họ chọn tiết lộ khóa ẩn), đồng thời vẫn đảm bảo về mặt mật mã rằng không thể chi tiêu nhiều tiền hơn số tiền có sẵn.

### Địa chỉ bí mật và giao dịch bí mật

Theo mặc định, khi bạn tạo một địa chỉ mới trong Elements bằng lệnh `getnewaddress`, địa chỉ đó sẽ được tạo dưới dạng địa chỉ bí mật.

Để chứng minh các giao dịch bí mật, chúng ta sẽ yêu cầu e2 tự gửi một số tiền và sau đó thử xem giao dịch từ e1. Điều này sẽ chứng minh bản chất bí mật của các giao dịch trong Elements.

Mọi địa chỉ mới được tạo ra bởi một nút Elements đều được bảo mật theo mặc định. Chúng ta có thể chứng minh điều này bằng cách yêu cầu e2 tạo ra một địa chỉ mới.

```
e2-cli getnewaddress
```

Lưu ý rằng địa chỉ bắt đầu bằng e1. Điều này xác định đây là Địa chỉ bí mật. Kiểm tra địa chỉ chi tiết hơn bằng lệnh getaddressinfo sẽ hiển thị thêm chi tiết về địa chỉ.

```
e2-cli getaddressinfo <address>
```

Bạn có thể thấy có thuộc tính secrets_key cho chúng ta biết đây là địa chỉ bí mật.

secrets_key là khóa công khai, được thêm vào chính địa chỉ bí mật. Đây là lý do tại sao địa chỉ bí mật lại dài như vậy.

Nó cũng có một địa chỉ không bảo mật liên quan. Nếu bạn muốn sử dụng các giao dịch thông thường, không bảo mật trong Elements, tài sản nên được gửi đến địa chỉ này thay vì địa chỉ có tiền tố lq1.

Bây giờ chúng ta có thể yêu cầu e2 gửi một số tiền đến địa chỉ mà nó tạo ra. Điều này sau đó sẽ chứng minh rằng e1, vì không phải là một trong những bên giao dịch, sẽ không thể xem chi tiết giao dịch.

```
e2-cli sendtoaddress <address>
```

Lưu ý ID giao dịch. Xác nhận giao dịch.

```
e2-cli -generate 101
```

Nhìn vào giao dịch mà e2 gửi một số tiền cho chính nó theo góc nhìn của chính e2.

```
e2-cli gettransaction <txid>
```

Cuộn lên chi tiết giao dịch, bạn có thể thấy rằng e2 có thể xem số tiền đã gửi và nhận cũng như tài sản đã giao dịch. Bạn cũng có thể thấy các thuộc tính amountblinder và assetblinder, được sử dụng để ẩn chi tiết từ các nút khác không liên quan đến giao dịch.

Để kiểm tra thông tin chi tiết của cùng một giao dịch từ e1, trước tiên chúng ta cần lấy thông tin chi tiết thô của giao dịch.

```
e1-cli getrawtransaction <txid>
```

Điều đó trả về chi tiết giao dịch thô. Nếu bạn nhìn vào phần vout, bạn có thể thấy có ba trường hợp. Hai trường hợp đầu tiên là số tiền nhận và thay đổi, và trường hợp thứ ba là phí giao dịch. Trong ba số tiền này, phí là trường hợp duy nhất mà bạn có thể thấy giá trị, vì bản thân phí luôn không bị che khuất trong Elements.

### Chìa khóa chói mắt

Hai phần vout đầu tiên hiển thị "phạm vi mù" của số tiền giá trị và dữ liệu cam kết đóng vai trò là bằng chứng về số tiền thực tế và loại tài sản được giao dịch.

Ngay cả khi chúng ta nhập khóa riêng của e2 vào ví của e1, nó vẫn không thể thấy được số lượng và loại tài sản được giao dịch vì nó vẫn không biết khóa mù được e2 sử dụng. Chúng ta sẽ chứng minh điều này bằng cách nhập khóa riêng được e2 sử dụng vào ví của e1. Đầu tiên, chúng ta cần xuất khóa từ e2

```
e2-cli dumpprivkey <address>
```

Sau đó nhập nó vào e1.

```
e1-cli importprivkey <privkey>
```

Bây giờ chúng ta có thể chứng minh rằng e1 vẫn không thể nhìn thấy các giá trị.

```
e1-cli gettransaction <txid>
```

Trên thực tế, nó hiển thị số tiền giao dịch là 0 trong khi thực tế là 1.

Để có thể thấy giá trị thực tế, không bị che khuất, chúng ta cần khóa che khuất. Để làm điều này, trước tiên chúng ta xuất khóa che khuất từ e2.

```
e2-cli dumpblindingkey <address>
```

Sau đó nhập nó vào e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Bây giờ khi chúng ta nhận được thông tin chi tiết giao dịch từ e1.

```
e1-cli gettransaction <txid>
```

Điều này cho thấy rằng với khóa mù được nhập vào, giờ đây chúng ta có thể xem giá trị thực tế là 1 trong giao dịch.

Trong phần này, chúng ta đã thấy rằng việc sử dụng khóa che giấu sẽ ẩn số lượng và loại tài sản trong một giao dịch và bằng cách nhập khóa che giấu phù hợp, chúng ta có thể tiết lộ những giá trị đó. Trong quá trình sử dụng thực tế, khóa che giấu có thể được cung cấp cho kiểm toán viên, ví dụ, trong trường hợp cần xác minh số lượng và loại tài sản do một bên nắm giữ. Tính năng Giao dịch bảo mật của Elements cũng cho phép thực hiện "bằng chứng phạm vi". Bằng chứng phạm vi có thể chứng minh rằng số lượng tài sản được nắm giữ trong một phạm vi nhất định mà không cần phải tiết lộ số lượng thực tế.

Chúng tôi cũng thấy rằng Giao dịch bảo mật là tùy chọn nhưng được bật theo mặc định khi tạo địa chỉ mới.

Bài học này đến đây là hết; chúc các bạn may mắn trong bài kiểm tra và hẹn gặp lại ở bài kiểm tra tiếp theo!

## Tài sản đã phát hành

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

Trong phần này, bạn sẽ học cách sử dụng tính năng Tài sản đã phát hành của Elements.

Tài sản đã phát hành cho phép nhiều loại tài sản được phát hành và chuyển giao giữa những người tham gia mạng lưới Elements. Bất kỳ nút nào trên mạng lưới cũng có thể phát hành tài sản của riêng mình. Việc phát hành có thể đại diện cho quyền sở hữu có thể thay thế của bất kỳ tài sản nào bao gồm chứng từ, phiếu giảm giá, tiền tệ, tiền gửi, trái phiếu, cổ phiếu, v.v. Tài sản đã phát hành mở ra cánh cửa để xây dựng các sàn giao dịch không cần tin cậy, quyền chọn và các hợp đồng thông minh tiên tiến khác liên quan đến tài sản tự phát hành.

Tài sản đã phát hành cũng được hưởng lợi từ Giao dịch bí mật và chúng có thể được phát hành lại bởi bất kỳ ai nắm giữ mã thông báo liên quan.

Bước đầu tiên là chúng ta cần truy cập vào hai nút Elements, chúng ta sẽ gọi là e1 và e2. Các nút này đã được thiết lập lại blockchain và phân chia tài sản mặc định giữa chúng.

Hai nút nằm trên cùng một mạng cục bộ và được kết nối với nhau, do đó chia sẻ cùng các giao dịch trong mempool giao dịch và các blockchain giống hệt nhau. Mặc dù chúng chạy trên cùng một máy, nhưng cần lưu ý rằng chúng không chia sẻ cùng các tệp blockchain thực tế. Mỗi nút quản lý bản sao blockchain cục bộ của riêng mình, chứa cùng lịch sử giao dịch vì chúng đồng thuận và tuân thủ cùng các quy tắc giao thức như nhau.

Chúng ta hãy bắt đầu bằng cách kiểm tra chế độ xem của từng nút về các đợt phát hành tài sản hiện có trên mạng.

Việc này được thực hiện bằng lệnh listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Như bạn thấy, cả hai nút đều hiển thị cùng một lịch sử phát hành. Cả hai đều hiển thị một tài sản, đợt phát hành ban đầu là 21 triệu Bitcoin được tạo ra khi khởi tạo chuỗi. Bạn có thể thấy id hex của tài sản trong kết quả chạy lệnh ở trên và nhãn được gán cho tài sản, đó là 'bitcoin'.

Cần lưu ý rằng tài sản mặc định luôn được gắn nhãn khi chuỗi được khởi tạo. Khi bạn phát hành tài sản của riêng mình, bạn có thể tự đặt nhãn cho chúng, chúng tôi sẽ sớm thực hiện việc này. Trước khi có thể thực hiện việc đó, chúng tôi cần phát hành tài sản của riêng mình.

Chúng ta sẽ yêu cầu e1 phát hành tài sản mới. Điều này được thực hiện bằng lệnh issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` chấp nhận 3 tham số.

Số lượng tài sản mới để phát hành, chúng tôi đã sử dụng 100. Số lượng token để tạo (token được sử dụng để phát hành lại số lượng tài sản), trong đó chúng tôi đã chọn 1. Tham số cuối cùng cho Elements biết tạo đợt phát hành tài sản dưới dạng blinded hoặc unblinded. Chúng tôi sẽ sử dụng unblinded vì chúng tôi muốn xem số lượng phát hành từ e2 trong một phút, vì vậy chúng tôi sẽ nhập false.

Chạy lệnh sẽ trả về dữ liệu về việc phát hành. Bao gồm ID giao dịch, bạn có thể sao chép để sử dụng sau, giá trị hex duy nhất của tài sản và giá trị hex duy nhất của mã thông báo tài sản.

Tạo khối để xác nhận giao dịch phát hành.

```
e1-cli -generate 1
```

Chạy lại lệnh `listissuances` với e1.

```
e1-cli listissuances
```

Điều đó cho thấy e1 hiện đã biết về 2 đợt phát hành, đợt phát hành ban đầu của Bitcoin và tài sản mới phát hành của chúng tôi, trong đó chúng tôi có thể thấy 100. Lưu ý giá trị hex của tài sản mới và không có nhãn tài sản liên quan, như đối với đợt phát hành bitcoin.

Kiểm tra lại danh sách các bản phát hành đã biết của e2.

```
e2-cli listissuances
```

Điều đó cho thấy e2 không biết về việc phát hành tài sản mà e1 đã thực hiện. Nó chỉ có thể thấy đợt phát hành bitcoin ban đầu mà nó có thể đã thấy.

Nguyên nhân là do e2 không biết và không theo dõi địa chỉ mà tài sản mới được gửi đến khi e1 phát hành.

Điều đáng chú ý là mặc dù e2 không thể nhìn thấy bản phát hành, e1 vẫn có thể gửi cho e2 một số tài sản. Tài sản mới sau đó sẽ hiển thị dưới dạng số dư khả dụng trong ví của e2, mặc dù e2 không biết về bản phát hành ban đầu.

Để e2 có thể thấy được số tiền phát hành thực tế (và do đó là số tiền được phát hành), chúng ta cần thêm địa chỉ vào e2 dưới dạng địa chỉ được theo dõi.

Để làm được điều này, chúng ta cần tìm ra địa chỉ mà tài sản được gửi đến. Đối với điều này, chúng ta sẽ sử dụng ID giao dịch mà chúng ta đã sao chép trước đó và yêu cầu e1 lấy thông tin chi tiết về giao dịch đó để chúng ta có thể tìm ra địa chỉ chính xác để thêm vào danh sách theo dõi ví của e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Cuộn lên qua giá trị hex của dữ liệu giao dịch, bạn sẽ thấy địa chỉ nhận được 100 tài sản mới của chúng tôi, được xác định bằng giá trị hex của nó.

Lấy địa chỉ và sao chép nó để chúng ta có thể nhập vào e2.

Bây giờ hãy nhập địa chỉ đó vào e2. Để thực hiện việc này, chúng ta sử dụng lệnh importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Bây giờ chúng ta hãy kiểm tra danh sách phát hành của e2.

```
e2-cli listissuances
```

Bạn có thể thấy rằng tài sản mới phát hành của chúng tôi hiện đã được đưa vào danh sách. Nút e2 cũng có thể xác định số lượng tài sản đã được phát hành, cùng với số lượng mã thông báo liên quan, vì đợt phát hành là đợt phát hành không bị che giấu. Để cho phép sử dụng ID tài sản để ánh xạ tên trong Elements, trước tiên hãy dừng Elements.

```
e1-cli stop
```

Sau đó khởi động lại nó với một tham số bổ sung ánh xạ hex của một tài sản tới nhãn được cung cấp. Điều này cho phép nút hiển thị dữ liệu về tài sản cho chúng ta theo định dạng dễ đọc hơn đối với con người. Bạn có thể thêm điều này vào cuối elements.conf nếu bạn thích, sau đó bạn không cần phải thêm đối số vào daemon mỗi khi bạn khởi động nó. Ví dụ:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Nhưng chúng ta sẽ sử dụng phương pháp lập luận ở đây.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Truy vấn lại nút để có danh sách các bản phát hành.

```
e1-cli listissuances
```

Điều đó cho thấy việc ánh xạ giá trị hex của tài sản vào nhãn của nó đang hoạt động. Kiểm tra lại danh sách phát hành của nút e2.

```
e2-cli listissuances
```

Bạn có thể thấy rằng nút e2 không có quyền truy cập vào nhãn này, vì nhãn chỉ khả dụng với nút đã đặt chúng. Thật vậy, chúng ta có thể gán một nhãn khác cho cùng một hex tài sản trên e2 so với nhãn chúng ta đã làm trên e1. Trước tiên, hãy dừng nút e2.

```
e2-cli stop
```

Bắt đầu lại bằng nhãn khác được gán cho mã hex của tài sản mới.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Niêm yết các đợt phát hành từ e2.

```
e2-cli listissuances
```

Nhãn tài sản là nhãn cục bộ của mỗi nút, chỉ có mã hex của tài sản mới được các nút khác trên mạng nhận dạng.

Việc ánh xạ nhãn thành hex tài sản rất hữu ích khi thực hiện các hành động như giao dịch và truy vấn số dư ví, vì nó cho phép một cách viết tắt để tham chiếu đến một tài sản. Ví dụ, nếu chúng ta muốn gửi một số tài sản mới của mình (số lượng là 10) từ e1 đến e2 mà không cần sử dụng nhãn.

Đầu tiên chúng ta cần có địa chỉ để gửi tài sản tới.

```
e2-cli getnewaddress
```

Sau đó sử dụng lệnh sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Xác nhận giao dịch bằng cách tạo khối.

```
generate 1
```

Kiểm tra tài sản đã được nhận vào e2.

```
e2-cli getwalletinfo
```

Chúng ta có thể thấy rằng tài sản thực sự đã được nhận.

Lưu ý rằng e2 ánh xạ hex của tài sản đã nhận và hiển thị nó bằng nhãn riêng của nó. Một cách dễ dàng hơn để làm điều tương tự là sử dụng nhãn tài sản của e1 khi gửi.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Ở chế độ nền, Elements ánh xạ các nhãn cục bộ thành các giá trị hex để giúp đơn giản hóa việc sử dụng các tài sản đã phát hành.

Trong phần này chúng ta đã thấy cách phát hành và dán nhãn tài sản. Trong phần tiếp theo chúng ta sẽ xem xét việc phát hành lại và hủy số lượng tài sản đã phát hành.

## Phát hành lại tài sản

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

Trong phần này, bạn sẽ học cách phát hành thêm tài sản đã phát hành và cách hủy một lượng tài sản đã phát hành nhất định.

Nhu cầu tái phát hành (tạo thêm) một tài sản hoặc phá hủy một lượng tài sản là điều có khả năng xảy ra khi tài sản đại diện cho thứ gì đó không có nguồn cung cố định. Điều này có thể áp dụng cho các tài sản đại diện cho vàng được giữ trong két chẳng hạn; khi các đơn vị vàng di chuyển vào và ra khỏi két, tài sản đại diện cho nguồn cung của két cần phải điều chỉnh tăng hoặc giảm cho phù hợp.

Việc phát hành lại một lượng tài sản yêu cầu phải có quyền sở hữu mã thông báo liên quan được tạo ra cùng với tài sản khi nó được phát hành ban đầu.

Khi tạo thêm một tài sản, không quan trọng nút nào đã phát hành tài sản ngay từ đầu, miễn là nút đang phát hành lại một lượng tài sản thì nó sở hữu cái thường được gọi là mã thông báo phát hành lại của tài sản. Chúng ta sẽ xem xét cách tạo mã thông báo phát hành lại ban đầu, cách sử dụng nó để phát hành lại một lượng tài sản và cách chuyển mã thông báo phát hành lại cho các nút khác, để họ cũng có quyền phát hành lại tài sản.

Chúng ta sẽ cần truy cập vào hai nút Elements, chúng ta sẽ gọi là e1 và e2. Các nút này đã được thiết lập lại blockchain và phân chia tài sản mặc định giữa chúng.

Chúng ta sẽ yêu cầu e1 phát hành một lượng 100 tài sản mới và tạo 1 mã thông báo phát hành lại cho cùng tài sản đó. Chúng ta sẽ tạo đợt phát hành dưới dạng không bị che giấu để đơn giản hóa ví dụ. Vậy hãy tiếp tục và phát hành tài sản và mã thông báo phát hành lại liên quan.

```
e1-cli issueasset 100 1 false
```

Lưu ý ID của tài sản cũng như ID của mã thông báo (phát hành lại).

Vì sau này chúng tôi sẽ phát hành lại nhiều tài sản hơn từ e2 nên chúng tôi sẽ cần ghi lại ID giao dịch mà tài sản được phát hành và sử dụng ID đó để nhập địa chỉ mà tài sản được gửi đến.

Xác nhận giao dịch.

```
e1-cli -generate 1
```

Bây giờ chúng ta sẽ kiểm tra thông tin chi tiết của giao dịch bằng lệnh gettransaction:

```
e1-cli gettransaction <txid>
```

Cuộn lên phía trên qua phần dữ liệu giao dịch, bạn sẽ thấy rằng trong giao dịch e1 đã nhận được 1 mã thông báo phát hành lại và 100 tài sản liên quan.

Sao chép địa chỉ để chúng tôi có thể nhập vào e2.

Và bây giờ nhập địa chỉ vào ví e2.

```
e2-cli importaddress <address>
```

Bây giờ chúng ta có thể thấy rằng cả e1 và e2 đều biết về việc phát hành tài sản.

```
e1-cli listissuances
e2-cli listissuances
```

Hiện tại e1 nắm giữ một lượng tài sản và 1 mã thông báo phát hành lại nhưng e2 thì không.

```
e1-cli getwalletinfo
```

Cũng lưu ý rằng e1 có ít tài sản mặc định hơn trước vì nó đã trả một khoản tiền nhỏ để trang trải phí giao dịch. Số tiền này sẽ được e1 thu thập khi khối được tạo ra đạt đến độ sâu hơn 100 khối.

```
e2-cli getwalletinfo
```

Vì e1 giữ mã thông báo phát hành lại nên nó có thể phát hành lại nhiều hơn. Điều này được thực hiện bằng cách sử dụng lệnh reissueasset. Hãy để e1 phát hành lại 100 tài sản khác.

```
e1-cli reissueasset <asset-id> 100
```

Kiểm tra việc phát hành lại đã thành công.

```
e1-cli getwalletinfo
```

Bạn có thể thấy rằng e1 hiện nắm giữ 200 tài sản như mong đợi.

Vì e2 không nắm giữ số lượng token tái phát hành nên họ sẽ nhận được lỗi nếu họ cố gắng tái phát hành tài sản.

```
e2-cli reissueasset <asset-id> 100
```

Lưu ý thông báo lỗi.

Chúng ta có thể xem thông tin chi tiết về việc phát hành lại từ e1 bằng lệnh listissuances.

```
e1-cli listissuances
```

Lưu ý cờ `is_reissuance`.

Nếu bây giờ chúng ta gửi e2 một lượng token tái phát hành, họ sẽ có thể tự phát hành lại một lượng tài sản. Trước tiên, chúng ta cần một địa chỉ để gửi đến. Cần lưu ý rằng token tái phát hành được xử lý giống như bất kỳ tài sản nào khác trong các phần tử khi gửi và hiển thị số dư và nó cũng có thể được chia nhỏ thành các mệnh giá nhỏ hơn như bất kỳ tài sản nào khác, vì vậy chúng ta không cần phải gửi 1 token tái phát hành đến e2 để nó có thể tái phát hành tài sản. Bất kỳ mệnh giá nào cũng đủ. Tạo một địa chỉ để e2 nhận token tái phát hành.

```
e2-cli getnewaddress
```

Sau đó gửi một phần RIT từ e1 đến e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Xác nhận giao dịch.

```
e1-cli -generate 1
```

Bây giờ chúng ta có thể thấy rằng e2 giữ nguyên giá trị 0,1 mà nó đã gửi.

```
e2-cli getwalletinfo
```

Điều này có nghĩa là e2 hiện có thể phát hành lại nhiều tài sản liên quan đến RIT mà nó nắm giữ trong ví của mình. Chúng ta sẽ yêu cầu e2 phát hành lại 500 tài sản.

```
e2-cli reissueasset <asset-id> 500
```

Kiểm tra kết quả cấp lại.

```
e2-cli getwalletinfo
```

Bạn có thể thấy rằng e2 hiện giữ số tiền được phát hành lại trong số dư ví của nó và bản thân RIT không bị tiêu tốn trong quá trình phát hành lại tài sản.

Bất kỳ ai nắm giữ ít nhất số lượng tài sản bị phá hủy đều có thể thực hiện việc hủy bỏ một lượng tài sản nhất định, việc này không bị chi phối bởi mã thông báo tái phát hành.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

Trong phần này, chúng ta đã thấy cách phát hành một tài sản, cùng với cách sử dụng mã thông báo tái phát hành được tạo tùy chọn như một phần của việc phát hành tài sản. Chúng ta cũng đã thấy cách chuyển mã thông báo tái phát hành đơn giản như chuyển bất kỳ tài sản nào khác và việc nắm giữ bất kỳ số lượng mã thông báo tái phát hành nào cũng cấp cho người nắm giữ quyền phát hành thêm tài sản liên quan. Do đó, việc kiểm soát những người có quyền truy cập vào mã thông báo tái phát hành trong mạng của bạn là rất quan trọng. Chúng ta cũng đã thấy cách hủy một số lượng tài sản và quá trình này không bị kiểm soát bởi việc sở hữu mã thông báo tái phát hành.

# Liên bang nguyên tố

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Ký khối

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements hỗ trợ mô hình ký liên bang cho phép bạn chỉ định số lượng thành viên Liên bang mạnh phải ký vào khối được đề xuất để tạo ra khối hợp lệ.

Trước đây, để dễ hiểu hơn, chúng tôi đã tạo các khối bằng lệnh `generate`, lệnh này không cần phải đáp ứng yêu cầu đa chữ ký để các khối được tạo ra được mạng chấp nhận là hợp lệ.

Chúng tôi sẽ thiết lập các nút của mình để yêu cầu tạo khối đa chữ ký 2 trong 2. Điều này sẽ được thiết lập bằng tham số signblockscript, có thể được thêm vào tệp cấu hình hoặc được truyền vào nút khi khởi động. Để khởi tạo chuỗi với tham số này, trước tiên chúng ta cần xây dựng tập lệnh mà chuỗi đó tạo thành.

Chúng tôi sẽ thực hiện việc này bằng một số nút hiện có, lưu dữ liệu mà chúng xuất ra và sau đó xóa chuỗi để chúng tôi có thể khởi động lại bằng tham số signblockscript của mình. Điều này là cần thiết vì tập lệnh tạo thành một phần của các quy tắc đồng thuận của mạng và sẽ cần được thiết lập khi khởi tạo chuỗi. Không thể thêm nó vào chuỗi đã tồn tại sau này.

Chúng ta sẽ cần truy cập vào hai nút Elements, chúng ta sẽ gọi là e1 và e2. Các nút này đã được thiết lập lại blockchain và phân chia tài sản mặc định giữa chúng.

Đảm bảo rằng tham số con_max_block_sig_size được đặt thành giá trị cao trong tệp elements.conf của bạn, nếu không, việc ký khối sẽ không thành công sau này trong phần này. Chúng tôi đã đặt con_max_block_sig_size=2000 cho hướng dẫn này.

Vì chúng tôi sẽ thiết lập lại blockchain và xóa các ví liên quan đến e1 và e2, nên chúng tôi sẽ cần sao chép các địa chỉ, khóa công khai và khóa riêng tư mà chúng tôi sử dụng để tạo tập lệnh ký khối để có thể sử dụng chúng sau này.

Đầu tiên, chúng ta cần mỗi nút ký khối tạo ra một địa chỉ mới, bạn cần sao chép địa chỉ này.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Sau đó, chúng ta cần trích xuất khóa công khai từ các địa chỉ và ghi lại chúng để sử dụng sau.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Sau đó trích xuất khóa riêng, chúng ta sẽ nhập lại sau để các nút có thể ký các khối sau khi chúng ta khởi tạo lại dữ liệu blockchain và ví.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Bây giờ chúng ta cần tạo một tập lệnh đổi thưởng với yêu cầu đa chữ ký 2 trong số 2. Chúng ta thực hiện điều này bằng cách sử dụng lệnh createmultisig và truyền tham số đầu tiên là 2 rồi cung cấp hai khóa công khai. Đây là những khóa cần chứng minh quyền sở hữu sau này khi khối được tạo.

Bất kỳ nút nào, e1 hoặc e2, đều có thể tạo ra đa chữ ký.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

Điều đó cung cấp cho chúng ta mã lệnh đổi thưởng mà bạn có thể sao chép để sử dụng sau.

Bây giờ chúng ta cần xóa dữ liệu blockchain và ví hiện có để có thể bắt đầu lại với signblockscript mới như một phần của các quy tắc đồng thuận của chuỗi. Đây là lý do tại sao chúng ta cần sao chép một số dữ liệu trước đó, chẳng hạn như khóa riêng sẽ được sử dụng trong chuỗi mới để ký khối. Bạn cần thực hiện việc này trước khi tiếp tục.

Với ví và dữ liệu chuỗi hiện tại đã bị xóa, giờ đây chúng ta có thể bắt đầu các nút của mình và yêu cầu chúng khởi tạo chuỗi mới bằng tham số signblockscript. Hãy truyền vào -evbparams=dynafed:0::: để vô hiệu hóa kích hoạt dynafed, vì chúng ta không cần tính năng nâng cao đó cho ví dụ này.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Bây giờ chúng ta cần nhập khóa riêng đã lưu trước đó để các nút của chúng ta có thể ký và giúp hoàn thành bất kỳ khối nào được đề xuất.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

Việc sử dụng lệnh generate hiện sẽ báo lỗi vì nó không đáp ứng được các quy tắc ký khối bắt buộc hiện được các nút của chúng tôi áp dụng.

```
e1-cli -generate 1
```

Để đề xuất một khối mới, mỗi nút có thể gọi lệnh getnewblockhex. Lệnh này trả về hex của khối mới cần được ký trước khi được bất kỳ nút nào trên mạng của chúng tôi chấp nhận.

```
e1-cli getnewblockhex
```

Hãy nhớ rằng lệnh chỉ tạo một khối được đề xuất, chứ không tạo ra khối nào.

Để xác nhận điều này, chúng ta có thể thấy rằng hiện tại không có khối nào trong blockchain của chúng ta.

```
e1-cli getblockcount
```

Nếu chúng ta thử gửi khối hex mà không ký trước.

```
e1-cli submitblock <block-hex>
```

Chúng tôi nhận được thông báo cho biết rằng bằng chứng khối không hợp lệ. Điều này là do nó chưa được 2 trong số 2 bên bắt buộc ký.

Vậy hãy để e1 ký vào khối được đề xuất.

```
e1-cli signblock <block-hex>
```

Để e2 ký hiệu thập lục phân.

```
e2-cli signblock <block-hex>
```

Lưu ý rằng e2 không ký kết đầu ra được tạo ra từ e1 ký khối được đề xuất. Cả hai đều ký hex khối được đề xuất độc lập với kết quả của nhau.

Bây giờ chúng ta cần kết hợp các chữ ký khối của e1 và e2. Mỗi nút có thể thực hiện điều này, tất cả những gì chúng cần là khối hex có dấu từ nút kia.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Bạn có thể thấy lệnh combineblocksigs xuất ra mã hex của khối đã ký cũng như trạng thái hoàn tất, cho chúng ta biết mã hex của khối đã sẵn sàng để gửi.

Bây giờ bất kỳ nút nào cũng có thể gửi khối hex đã hoàn thành. Chúng ta sẽ để e1 thực hiện.

```
e1-cli submitblock <combined-signed-hex>
```

Kiểm tra xem bài nộp có hợp lệ không.

```
e1-cli getblockcount
e2-cli getblockcount
```

Bạn có thể thấy rằng cả e1 và e2 đều chấp nhận khối này là hợp lệ và thêm nó vào đầu bản sao cục bộ của chuỗi khối.

Để tóm tắt quá trình. Trong phần này chúng ta có:


- Đề xuất chặn.
- Yêu cầu mỗi nút ký vào đó.
- Kết hợp các chữ ký.
- Đã kiểm tra xem chữ ký có hợp lệ và đáp ứng ngưỡng redemptionscript của chuỗi không.
- Đã nộp khối.

Mỗi nút trên mạng xác thực khối và thêm nó vào bản sao cục bộ của blockchain.

### Ký khối

Mặc dù quá trình này ban đầu có vẻ phức tạp, nhưng trình tự ký khối trong Elements luôn giống nhau và thiết lập ban đầu chỉ cần thực hiện một lần:

1. Thiết lập ban đầu (thực hiện một lần)

2. Một địa chỉ đa chữ ký được tạo ra có tên là `signblockscript` bằng cách sử dụng khóa công khai của Người ký khối liên bang.

3. Tập lệnh đổi thưởng từ đây được sử dụng để bắt đầu một blockchain mới.

4. Sản xuất khối (đang tiến hành)

5. Các khối được đề xuất sẽ được tạo ra và trao đổi để ký.

Khi một số lượng người ký ngưỡng đã ký vào khối được đề xuất, nó sẽ được kết hợp và gửi lên mạng. Nếu nó đáp ứng các tiêu chí của `signblockscript` của chuỗi, các nút sẽ chấp nhận nó như một khối hợp lệ.

## Phần tử như một chuỗi bên

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements là một nền tảng blockchain mã nguồn mở, mục đích chung, cũng có thể được `pegged` vào một blockchain hiện có, chẳng hạn như Bitcoin. Khi được pegged vào một blockchain khác, Elements được cho là hoạt động như một `sidechain`. Sidechain cho phép chuyển giao tài sản theo hai chiều từ chuỗi này sang chuỗi khác. Việc triển khai Elements như một sidechain cho phép bạn giải quyết một số hạn chế vốn có của mainchain, đồng thời vẫn giữ được mức độ bảo mật tốt do các tài sản được bảo mật trên mainchain cung cấp.

Trong khi sidechain nhận thức được mainchain và lịch sử giao dịch của nó, mainchain không nhận thức được sidechain và không cần sidechain để vận hành. Điều này cho phép sidechain đổi mới mà không bị hạn chế hoặc chậm trễ liên quan đến các đề xuất cải tiến giao thức mainchain. Thay vì cố gắng thay đổi trực tiếp, việc mở rộng giao thức chính cho phép mainchain tự duy trì tính bảo mật và chuyên biệt, hỗ trợ hoạt động trơn tru của sidechain.

Bằng cách mở rộng chức năng của Bitcoin và tận dụng bảo mật cơ bản của nó, sidechain dựa trên Elements có thể cung cấp chức năng mới mà trước đây người dùng mainchain không có. Một ví dụ về sidechain dựa trên Elements trong quá trình sử dụng sản xuất là Liquid Network.

Để khởi tạo chuỗi khối Elements dưới dạng chuỗi phụ, chúng ta cần sử dụng tham số tập lệnh peg liên kết. Tham số này có thể được đặt trong tệp cấu hình của nút hoặc được truyền vào khi khởi động.

Tập lệnh chốt liên bang xác định thành viên nào của liên bang mạnh có thể thực hiện chức năng chốt vào và chốt ra. Những chức năng này được gọi là `Watchmen` vì họ theo dõi chuỗi chính và chuỗi phụ để tìm các giao dịch chốt vào và chốt ra hợp lệ và thực hiện chúng nếu hợp lệ. `Chốt ra` có nghĩa là di chuyển tài sản được chốt ra khỏi chuỗi phụ và vào chuỗi chính và `chốt vào` có nghĩa là di chuyển tài sản được chốt vào chuỗi phụ từ chuỗi chính. Khi chúng tôi nói `di chuyển vào chuỗi phụ`, ý chúng tôi thực sự muốn nói là tiền bị khóa trong một địa chỉ đa chữ ký trên chuỗi chính và một lượng tài sản tương ứng được tạo trên chuỗi phụ Elements. Khi chúng tôi nói `di chuyển ra khỏi chuỗi phụ`, ý chúng tôi muốn nói là tài sản bị hủy trên chuỗi phụ Elements và số tiền tương ứng được giải phóng khỏi các quỹ bị khóa được giữ trên chuỗi chính. Quyền thực hiện các chức năng chốt vào và chốt ra yêu cầu các chức năng phải chứng minh quyền sở hữu đối với khóa công khai được sử dụng trong tập lệnh chốt liên bang. Điều này được thực hiện bằng cách sử dụng khóa riêng tương ứng.

Để tạo một tập lệnh chốt liên bang, do đó, trước tiên chúng ta cần để mỗi nút của mình tạo một khóa công khai. Chúng ta cũng cần lưu trữ các khóa riêng liên quan để sử dụng sau này vì chúng ta sẽ cần xóa mọi dữ liệu chuỗi hiện có và khởi tạo chuỗi mới bằng tập lệnh chốt liên bang. Điều này là do tập lệnh chốt liên bang tạo thành một phần của các quy tắc đồng thuận của chuỗi phụ và không thể áp dụng cho chuỗi khối hiện có, không chốt vào thời điểm sau này.

Vì vậy, hãy tạo một địa chỉ với mỗi nút của chúng ta, lưu trữ dữ liệu có liên quan để sử dụng sau này và tạo tập lệnh chốt liên kết mà chúng ta sẽ sử dụng để khởi tạo chuỗi phụ sau này.

Đầu tiên, chúng ta cần mỗi nút, đóng vai trò là Người canh gác trong mạng, tạo một địa chỉ mới.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Sau đó, chúng tôi xác thực địa chỉ để lấy khóa công khai.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Và sau đó lấy khóa riêng liên quan đến từng địa chỉ.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Lưu trữ khóa riêng tư và khóa công khai để sử dụng sau.

Bây giờ chúng ta cần xóa dữ liệu blockchain và ví hiện có vì chúng ta sẽ khởi tạo chuỗi mới bằng cách sử dụng tập lệnh peg liên kết. Bạn có thể thực hiện việc này ngay bây giờ. Đừng quên khởi động daemon Bitcoin, chúng ta sẽ cần peg-in.

Bây giờ chúng ta có thể khởi tạo một chuỗi mới với một tập lệnh chốt liên kết được tạo bằng khóa công khai mà chúng ta đã lưu trữ trước đó. Các số mà chúng ta nhập và bao quanh khóa công khai của chúng ta xác định và phân định số lượng khóa được sử dụng và quyền sở hữu khóa phải được chứng minh để chốt vào và ra khỏi chuỗi phụ của chúng ta.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Bây giờ chúng ta sẽ nhập khóa riêng đã lưu trước đó để các nút của chúng ta có thể ký và hoàn tất việc chuyển giao tài sản giữa các chuỗi và đáp ứng các yêu cầu của tập lệnh chốt liên bang.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Bây giờ chúng ta cần hoàn thiện một số khối trên cả hai chuỗi. Sự hoàn thiện của các khối là yêu cầu của quy trình chốt vì nó bảo vệ chống lại việc tổ chức lại khối trên chuỗi chính dẫn đến lạm phát nguồn cung tài sản được chốt trong chuỗi phụ.

Để phần này tập trung vào chốt liên bang, chúng ta sẽ tạo các khối mà không sử dụng mô hình ký khối đã xem xét ở phần trước và quay lại sử dụng lệnh 'generate' để tạo các khối mới.

```
b-cli generate 101
e1-cli generate 1
```

Chúng ta không nhất thiết phải tạo khối ngay bây giờ cho các phần tử. Nhưng hãy tạo một khối. Đây là một cách làm tốt để tránh những mâu thuẫn tiềm ẩn.

Bây giờ chuỗi của chúng ta đã sẵn sàng để peg-in. Để peg-in, chúng ta cần tạo một loại địa chỉ đặc biệt bằng lệnh getpeginaddress. Lưu ý rằng khoảng thời gian giữa việc tạo địa chỉ peg-in bằng getpeginaddress và yêu cầu địa chỉ đó bằng claimpegin phải được giữ càng nhỏ càng tốt. Địa chỉ peg-in không bền lâu và không nên sử dụng lại.

```
e1-cli getpeginaddress
```

Bạn có thể thấy lệnh này tạo ra một địa chỉ mainchain mới, cũng như một tập lệnh mới cần phải thỏa mãn để yêu cầu các khoản tiền peg-in. Địa chỉ mainchain là một địa chỉ `pay to script hash` sẽ được sử dụng bởi các chức năng thực hiện vai trò Watchmen trong mạng lưới Elements.

Giống như getnewaddress, getpeginaddress thêm một bí mật mới vào ví của nút gọi, do đó, điều quan trọng là phải đưa việc sao lưu tệp ví vào quy trình quản lý nút của bạn.

Bây giờ chúng ta sẽ gửi một số bitcoin từ chuỗi chính đến chuỗi phụ. Ví thử nghiệm hồi quy chuỗi chính của chúng tôi đã giữ một số tiền.

```
b-cli getwalletinfo
```

Chúng ta có thể thấy rằng ví chứa 50 bitcoin. Chúng ta sẽ gửi một bitcoin từ chuỗi chính đến chuỗi phụ. Chúng ta cần gửi tiền đến địa chỉ chuỗi chính mà nút của chúng ta đã tạo trước đó.

```
b-cli sendtoaddress <e1-pegin-address>
```

Chúng tôi cần giữ ID của giao dịch này vì chúng tôi cần nó để làm bằng chứng tài trợ sau này.

Bây giờ chúng ta có thể thấy số dư ví mainchain đã giảm đi đúng số tiền chúng ta đã gửi, cộng thêm một số tiền nhỏ để trang trải phí giao dịch.

```
b-cli getwalletinfo
```

Chúng ta cần phải hoàn tất giao dịch một lần nữa.

```
b-cli generate 101
```

Để nút Elements của chúng ta yêu cầu tiền peg-in, chúng ta cần có `bằng chứng` cho thấy giao dịch peg-in đã được thực hiện. Bằng chứng mật mã sử dụng ID giao dịch tài trợ để tính toán đường dẫn merkel và chứng minh rằng giao dịch có trong một khối đã xác nhận.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Chúng tôi cũng cần dữ liệu giao dịch thô.

```
b-cli getrawtransaction <tx-id>
```

Với bằng chứng và dữ liệu thô cho giao dịch peg-in, nút phần tử của chúng ta hiện có thể yêu cầu peg-in bằng cách sử dụng giao dịch thô và bằng chứng giao dịch.

```
e1-cli claimpegin <raw> <proof>
```

Lưu ý rằng có một đối số thứ ba tùy chọn mà chúng ta có thể cung cấp cho claimpegin. Tham số thứ ba này có thể được sử dụng để chỉ định địa chỉ sidechain để gửi tiền đã yêu cầu. Điều này không cần thiết trong ví dụ của chúng tôi vì chúng tôi đang gọi lệnh từ cùng một nút sở hữu địa chỉ mà tiền đã yêu cầu sẽ đến.

Kiểm tra số dư của e1.

```
e1-cli getwalletinfo
```

Tạo khối để xác nhận yêu cầu.

```
e1-cli generate 1
```

Kiểm tra số dư của e1.

```
e1-cli getwalletinfo
```

Chúng ta có thể thấy rằng lệnh chốt đã được xác nhận thành công.

Để chốt ra, quy trình cũng tương tự. Trong đó, một địa chỉ được tạo ra, tiền được gửi đến địa chỉ đó và tiền được giải phóng nếu giao dịch hợp lệ. Chúng tôi sẽ không đề cập đến toàn bộ quy trình chốt ra vì nó liên quan đến công việc trên chuỗi chính nằm ngoài phạm vi của khóa học này. Các bước về sự kiện Elements là một địa chỉ được tạo ra trên chuỗi chính.

```
b-cli getnewaddress
```

Tiền được gửi đến địa chỉ chuỗi chính từ một nút Elements bằng lệnh sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Tạo khối để xác nhận giao dịch.

```
e1-cli generate 1
```

Kiểm tra số dư ví của nút.

```
e1-cli getwalletinfo
```

Và thấy rằng số dư đã giảm.

Trong phần này chúng ta đã thấy cách:


- Tạo một tập lệnh chốt liên kết.
- Khởi tạo chuỗi mới sử dụng tập lệnh làm quy tắc tham số đồng thuận mạng.
- Gửi tiền từ chuỗi chính tới chuỗi phụ.
- Yêu cầu tiền trong sidechain Elements.
- Hiểu cách bắt đầu gửi tiền trở lại chuỗi chính.

### Liên kếtPegScript

Để cho phép Elements hoạt động như một sidechain, khối genesis trong blockchain của nó phải được tạo bằng `fedpegscript`. Điều này được thực hiện bằng cách truyền tham số `fedpegscript` khi khởi động nút. Sau đó, tập lệnh sẽ tạo thành một phần của các quy tắc đồng thuận của blockchain Elements và cho phép các yêu cầu peg-in và peg-out được xác thực và thực hiện.

`fedpegscript` được tạo thành từ các khóa công khai được kiểm soát bởi những người được ủy quyền thực hiện các hành động chốt. Sau đây là ví dụ về định dạng của fedpegscript đa chữ ký 2 trong 2:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Lưu ý: Các ký tự bên ngoài khóa công khai là các dấu phân cách biểu thị khóa công khai và yêu cầu `n trong số m`. Ví dụ: mẫu cho fedpegscript 1-trong-1 sẽ là '5121<khóa công khai 1>51ae'.

### Chốt vào

Trước khi một peg-in có thể được chấp nhận bởi sidechain Elements, nó phải có đủ xác nhận trên mainchain. Điều này là cần thiết để tránh lạm phát trong nguồn cung của tài sản được neo trên sidechain Elements có thể do việc tổ chức lại mainchain gây ra.

Việc tổ chức lại ngắn gọn phần đầu của chuỗi khối Bitcoin được mong đợi như một phần của hoạt động bình thường của cơ chế đồng thuận Proof of Work (PoW). Do đó, Elements chỉ chấp nhận một peg-in là hợp lệ khi nó có đủ độ sâu trong chuỗi khối Bitcoin. Điều này giúp ngăn Elements chấp nhận cùng một peg-in nhiều hơn một lần.

### Chốt-Ra

Một lệnh peg-out xảy ra khi một nút Elements gọi lệnh `sendtomainchain`, lệnh này lấy đầu vào là địa chỉ chuỗi chính (điểm đến peg-out) cũng như số lượng tài sản được chốt sẽ được `rút`. Điều này tạo ra một giao dịch peg-out trên chuỗi phụ. Khi các Chức năng đóng vai trò là Người canh gác phát hiện ra rằng giao dịch peg-out đã được xác nhận trên chuỗi phụ, họ sẽ thực sự giải phóng tài sản trên chuỗi chính đến điểm đến peg-out, như chúng ta đã học trong các phần trước của khóa học.

## Các yếu tố như một Blockchain độc lập

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Cho đến nay, chúng ta đã xem xét cách chạy Elements như một sidechain. Tuy nhiên, nó cũng có thể hoạt động như một giải pháp blockchain độc lập với tài sản gốc mặc định của riêng nó. Trong thiết lập này, blockchain Elements vẫn giữ lại tất cả các tính năng của triển khai sidechain, chẳng hạn như Giao dịch bí mật và Tài sản đã phát hành, nhưng không cần peg-in hoặc peg-out để thêm hoặc xóa số lượng tài sản mặc định khỏi lưu thông.

Trong phần này chúng ta sẽ:

Khởi tạo blockchain Elements mới với tài sản mặc định có tên là `newasset`.

Chỉ định 1.000.000 `tài sản mới` sẽ được tạo cùng với 2 mã thông báo phát hành lại cho tài sản đó.

Nhận tất cả các đồng tiền `newasset` mà bất kỳ ai cũng có thể chi tiêu.

Yêu cầu tất cả các mã thông báo phát hành lại mà bất kỳ ai cũng có thể chi tiêu cho 'tài sản mới'.

Gửi tài sản và mã thông báo phát hành lại của nó tới ví của một nút khác.

Phát hành lại nhiều 'tài sản mới' hơn từ cả hai nút.

Để khởi tạo mạng Elements hoạt động như một blockchain độc lập, mỗi nút cần được bắt đầu bằng một số tham số cơ bản. Chúng được sử dụng để yêu cầu nút không thử và xác thực các peg-in từ blockchain khác, tên tài sản mặc định của mạng và số lượng tài sản mặc định và mã thông báo phát hành lại liên quan để tạo.

Chúng ta sẽ bắt đầu một chuỗi mới bằng cách sử dụng các tham số này trên hai nút Elements được kết nối của chúng ta ngay bây giờ. Chúng ta sẽ đặt tên cho tài sản mặc định là `newasset` và phát hành một triệu trong số chúng và hai mã thông báo phát hành lại `newasset`.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Lưu ý rằng số tiền được sử dụng ở đây là mệnh giá nhỏ nhất mà mạng có thể chấp nhận, vì vậy hai trăm triệu token tái phát hành thực sự tương đương với hai token nguyên vẹn. Điều tương tự cũng đúng với mệnh giá của các đồng tiền miễn phí ban đầu.

Kiểm tra số dư ví hiện tại của nút của chúng tôi.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Chúng ta có thể thấy rằng quá trình khởi tạo đã hoạt động chính xác.

Vì đợt phát hành tài sản ban đầu được tạo ra với mục đích `bất kỳ ai cũng có thể chi tiêu`, chúng ta sẽ yêu cầu e1 yêu cầu tất cả chúng để có thể loại bỏ quyền truy cập của e2 vào chúng.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Lưu ý rằng chúng ta không cần phải chỉ định 'newasset' là tài sản cần gửi vì nó đã là tài sản mặc định và do đó cũng là tài sản mặc định được sử dụng để thanh toán phí mạng.

Trong Elements, bạn có thể gửi nhiều loại tài sản đến cùng một địa chỉ, do đó chúng ta có thể sử dụng lại địa chỉ vừa tạo để nhận tài sản mặc định và sử dụng địa chỉ đó làm địa chỉ đích cho mã thông báo phát hành lại.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Xác nhận giao dịch.

```
e1-cli generate 101
```

Chúng tôi sẽ kiểm tra xem e1 có phải là người duy nhất nắm giữ tài sản và mã thông báo tái phát hành của tài sản đó hay không.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Chúng ta có thể thấy điều này thực sự đúng.

Bây giờ chúng ta sẽ gửi một số 'tài sản mới' cho e2, người hiện đang có số dư bằng 0.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Lưu ý rằng chúng tôi không phải chỉ định loại tài sản sẽ được gửi vì `newasset` đã được tạo làm tài sản mặc định của mạng

Chúng ta cũng hãy gửi một số mã thông báo phát hành lại cho `newasset` tới e2.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Xác nhận giao dịch.

```
e1-cli generate 101
```

Chúng ta có thể kiểm tra xem ví đã được cập nhật tương ứng hay chưa.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Bây giờ chúng ta sẽ phát hành lại một số tài sản mặc định từ e1. Lưu ý rằng khả năng thực hiện việc này được kích hoạt bởi tham số khởi động initialreissuancetokens. Nếu bỏ qua hoặc đặt thành 0, sẽ dẫn đến một tài sản mặc định không thể phát hành lại vào một ngày sau đó.

```
e1-cli reissueasset newasset 100
```

Chúng tôi có thể sử dụng nhãn `newasset` thay vì phải cung cấp giá trị id hex vì chuỗi Elements luôn gắn nhãn cho tài sản mặc định của nó.

Kiểm tra xem việc phát hành lại tài sản mặc định có hiệu quả không:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Bây giờ chúng ta sẽ chứng minh rằng vì e2 nắm giữ một số mã thông báo tái phát hành `newasset` nên nó cũng có thể tái phát hành tài sản mặc định.

```
e2-cli reissueasset newasset 100
```

Kiểm tra xem việc phát hành lại tài sản mặc định của e2 có hiệu quả không.

```
e2-cli generate 101
e2-cli getwalletinfo
```

Trong phần này, chúng tôi đã thiết lập Elements như một blockchain độc lập và kiểm tra xem chức năng cơ bản có hoạt động như mong đợi hay không.

Chúng tôi sử dụng các tham số khởi động để:

Khởi tạo blockchain Elements mới với tài sản mặc định có tên là 'newasset'.

Chỉ định số lượng tài sản mặc định sẽ được tạo khi khởi tạo chuỗi.

Tạo một số mã thông báo phát hành lại cho tài sản mặc định và phát hành lại nhiều tài sản mặc định hơn từ cả hai nút.

Trên mạng lưới Blockchain Elements độc lập của chúng tôi, tất cả các hoạt động giao dịch khác sẽ hoạt động theo cùng một cách như các ví dụ được trình bày trong các phần chính của khóa học, nhưng sẽ sử dụng 'newasset' thay vì `bitcoin` làm tài sản mặc định và phí.

### Tham số khởi động nút và khởi tạo chuỗi

Để yêu cầu một nút Elements hoạt động như một blockchain độc lập, một số tham số phải được sử dụng cùng nhau. Chúng ta sẽ xem xét từng tham số ngay bây giờ và tìm hiểu xem chúng làm gì.

#### `xác thực_mã_số=0`

Vì blockchain độc lập không cần xác thực bất kỳ giao dịch peg-in hoặc peg-out nào, chúng ta cần vô hiệu hóa các kiểm tra đó. Với cài đặt này, bạn không cần chạy phần mềm máy khách Bitcoin hoặc lưu trữ bản sao của blockchain Bitcoin, vì mạng Elements sẽ hoạt động độc lập.

#### `tên tài sản mặc định`

Tính năng này cho phép bạn chỉ định tên của tài sản mặc định được tạo khi khởi tạo blockchain.

#### `tiền miễn phí ban đầu`

Số lượng (tương đương với đơn vị Satoshi của Bitcoin) của tài sản mặc định cần tạo.

#### `mã thông báo phát hành lại ban đầu`

Số lượng (tương đương với đơn vị Satoshi của Bitcoin) của các mã thông báo tái phát hành để tạo ra tài sản mặc định. Nếu không có số này, sẽ không thể tạo thêm tài sản mặc định. Nếu bạn không muốn có thể tạo thêm tài sản mặc định, bạn có thể đặt số này thành 0 hoặc bỏ qua.

Sử dụng các tham số này, lệnh chung để bắt đầu một nút sẽ trông giống như thế này:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Các hoạt động cơ bản

Tham số `defaultpeggedassetname` áp dụng nhãn cho tài sản mặc định. Nếu không có thiết lập này, tài sản mặc định sẽ tự động được đặt tên là `bitcoin`. Trong các phần trước, khi chúng tôi gửi tài sản mà chúng tôi tự phát hành đến một nút khác, chúng tôi phải chỉ định mã hex tài sản hoặc nhãn tài sản được áp dụng cục bộ để cho Elements biết chúng tôi đang gửi tài sản nào. Vì `defaultpeggedassetname` áp dụng trên tất cả các nút nên chúng tôi không cần đặt tên cho nó khi gửi, ngay cả khi tên của nó không phải là `bitcoin`. Mọi hàm đã gửi `bitcoin` trước đó theo mặc định giờ đây sẽ gửi bất kỳ thứ gì bạn chọn để gắn nhãn cho tài sản mặc định.

Vì vậy, việc gửi 10 tài sản mặc định mới đến một địa chỉ cũng đơn giản như sau:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Nếu bạn cũng cung cấp cho nút một giá trị cho `initialreissuancetokens` lớn hơn 0 thì bạn cũng sẽ có thể phát hành lại nhiều tài sản mặc định hơn, điều này không thể thực hiện được nếu bạn chạy Elements dưới dạng chuỗi phụ.

Để thực hiện điều này, bất kỳ nút nào nắm giữ số lượng mã thông báo được liên kết với tài sản mặc định chỉ cần đưa ra lệnh theo mẫu:

```
e1-cli reissueasset <default asset name> <amount>
```

Bằng cách sử dụng các tham số trên, bạn có thể vận hành Elements như một blockchain độc lập với tài sản mặc định riêng, tách biệt khỏi Bitcoin và các blockchain khác.

## Phần kết luận

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

Trong khóa học này, chúng ta đã tìm hiểu rằng Elements là một giao thức mạng nguồn mở có thể được triển khai như một chuỗi phụ cho một chuỗi khối khác hoặc như một giải pháp chuỗi khối độc lập.

Chúng tôi đã thấy rằng mã nguồn và trang web cho Elements (https://github.com/ElementsProject/elements) được lưu trữ trên GitHub và có các diễn đàn thảo luận cộng đồng, chẳng hạn như Build On L2 (https://community.liquid.net/c/developers/) hoặc Liquid Developers Telegram (https://t.me/liquid_devel), có thể được sử dụng để tìm hiểu thêm về việc triển khai và phát triển các ứng dụng trên Elements và Liquid. Các tính năng chính như Giao dịch bí mật và Tài sản đã phát hành đã được đề cập, cùng với cách các thành viên của Liên đoàn mạnh cho phép ký khối liên bang và cơ chế Peg 2 chiều.

Bước tiếp theo là thử thách bản thân bằng bài kiểm tra tổng hợp bao gồm tất cả các phần trước, sau đó bắt đầu hành trình Elements của bạn…chúc may mắn!

# Phần kết luận

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Đánh giá & Xếp hạng

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>
## Phần kết luận

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Xin chúc mừng vì đã hoàn thành khóa học này!

Chúng tôi rất vui mừng khi bạn đã đạt được cột mốc này trong hành trình học tập của mình. Nhờ sự tận tâm và cam kết, bạn đã có được kiến thức và kỹ năng giá trị giúp ích cho sự phát triển nghề nghiệp của bạn.