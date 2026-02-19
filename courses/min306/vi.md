---
name: Thành thạo Mining nguồn mở của Bitaxe
goal: Nắm vững toàn bộ hệ sinh thái Bitaxe, từ lắp ráp phần cứng đến tùy chỉnh nâng cao và tối ưu hóa hiệu suất
objectives: 

  - Hiểu triết lý của phần cứng nguồn mở Bitcoin mining
  - Xây dựng thiết bị Bitaxe mining từ đầu
  - Cấu hình và tối ưu hóa phần mềm mining bao gồm AxeOS và Public Pool
  - Triển khai các tối ưu hóa hiệu suất nâng cao bao gồm ép xung và đánh giá hiệu suất

---

# Hướng dẫn sử dụng Bitaxe Mining của bạn


Chào mừng bạn đến với khóa học Bitaxe toàn diện, nơi bạn sẽ nắm vững phần cứng mã nguồn mở mang tính cách mạng Bitcoin mining, đang dân chủ hóa việc tiếp cận công nghệ mining. Khóa học này sẽ hướng dẫn bạn từ việc tìm hiểu nền tảng triết lý của mining phi tập trung đến các kỹ thuật tùy chỉnh phần cứng và tối ưu hóa hiệu suất tiên tiến.


Dự án Bitaxe đại diện cho một sự thay đổi mô hình trong Bitcoin mining, phá vỡ thế độc quyền của các nhà sản xuất ASIC độc quyền bằng cách cung cấp các thiết kế, phần mềm và phần mềm nguồn mở hoàn toàn. Thông qua các chương thực hành này, bạn sẽ có được các kỹ năng thực tế về lắp ráp phần cứng, cấu hình phần mềm, thiết kế PCB và tối ưu hóa hiệu suất.


Không yêu cầu kinh nghiệm mining trước đó, nhưng kiến thức điện tử cơ bản và sự quen thuộc với GitHub sẽ rất hữu ích. Khóa học sẽ biến bạn từ một người quan sát tò mò thành một người xây dựng và đóng góp Bitaxe có năng lực.


+++


# Giới thiệu


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Tổng quan về khóa học


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Chào mừng bạn đến với khóa học MIN 306 _**Bitaxe Open Source Mining Mastery**_, một hành trình toàn diện khám phá thế giới Bitaxe mining. Khóa học này được thiết kế dành cho những ai muốn tìm hiểu, xây dựng và tối ưu hóa phần cứng Bitaxe mining của riêng mình, đồng thời khám phá những nền tảng triết lý và kỹ thuật làm nên sự độc đáo của dự án này trong hệ sinh thái Bitcoin.


### Hiểu về Bitaxe


Phần đầu tiên đặt nền tảng thiết yếu: bạn sẽ khám phá nguồn gốc của dự án Bitaxe, quá trình phát triển của nó, cũng như các giá trị của sự phi tập trung và minh bạch định hình dự án. Bạn sẽ tìm hiểu Bitaxe thực sự là gì, nó khác với ASIC độc quyền như thế nào, và tìm kiếm các nguồn lực cộng đồng để nâng cao kiến thức. Phần này cung cấp bối cảnh cần thiết để hiểu tại sao Bitaxe lại đại diện cho một bước ngoặt trong lịch sử Bitcoin và mining.


### Phần mềm và Hoạt động


Phần thứ hai tập trung vào môi trường phần mềm, với phần trình bày chi tiết về *AxeOS*: hệ điều hành mã nguồn mở được thiết kế riêng cho các thiết bị Bitaxe. Bạn sẽ tìm hiểu các tính năng chính của hệ điều hành này cũng như cách cấu hình và tương tác với thiết bị để bắt đầu vận hành mining đầu tiên.


### Cộng đồng và Hợp tác


Phần thứ ba nêu bật khía cạnh hợp tác của dự án. Bạn sẽ khám phá triết lý nguồn mở được áp dụng cho cả quá trình phát triển phần cứng và phần mềm của Bitaxe. Thông qua các bài tập thực hành, bạn sẽ học cách đóng góp trực tiếp vào mã nguồn, đồng thời khám phá _Public Pool_, một nền tảng cộng đồng để tập hợp sức mạnh tính toán. Bạn cũng sẽ học cách cài đặt nền tảng này trên một node Umbrel để tích hợp cục bộ và toàn quyền.


### Lắp ráp phần cứng và khắc phục sự cố


Trong phần thứ tư, bạn sẽ tìm hiểu sâu hơn về phần cứng. Bạn sẽ học cách xác định các công cụ cần thiết để lắp ráp Bitaxe, khắc phục sự cố hàn và thực hiện chẩn đoán toàn diện bằng *AxeOS* và các công cụ USB. Phần này nhấn mạnh vào thực hành thực hành và hiểu sâu về cách các thành phần phần cứng và phần mềm tương tác với nhau.


### Tùy chỉnh nâng cao


Phần thứ năm dành riêng cho việc tùy chỉnh. Bạn sẽ học cách sửa đổi PCB (bảng mạch in), tạo tệp gốc và sử dụng _Btaxe Web Flasher_. Phần này dành cho những ai muốn vượt ra ngoài việc lắp ráp đơn giản và thực sự thiết kế các phiên bản tùy chỉnh cho thiết bị của riêng mình.


### Tối ưu hóa hiệu suất


Cuối cùng, phần thứ sáu sẽ đề cập đến các kỹ thuật tối ưu hóa nâng cao. Bạn sẽ học cách đánh giá hiệu suất của Bitaxe và cách ép xung hiệu quả. Những kỹ năng này sẽ giúp bạn tận dụng tối đa phần cứng của mình mà vẫn tôn trọng các giới hạn vật lý của nó.


Giống như mọi khóa học trên Plan ₿ Academy, phần cuối cùng bao gồm phần đánh giá được thiết kế để củng cố kiến thức của bạn.


Hãy tham gia ngay vào cuộc phiêu lưu kỹ thuật này — tương lai của Bitcoin mining nằm trong tay bạn!


# Hiểu về Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Lịch sử

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Dự án Bitaxe đại diện cho một bước chuyển mình đột phá trong quá trình phát triển phần cứng Bitcoin và [mining](https://planb.academy/resources/glossary/mining), mang các nguyên tắc nguồn mở đến với một ngành công nghiệp vốn bị chi phối bởi các giải pháp độc quyền. Chuỗi bài học này khám phá lịch sử toàn diện, những đổi mới kỹ thuật và sự phát triển do cộng đồng thúc đẩy của Bitaxe, cung cấp những hiểu biết sâu sắc về cách tầm nhìn của một kỹ sư đơn lẻ đã chuyển đổi thành một hệ sinh thái phần cứng mining phi tập trung đang phát triển mạnh mẽ. Thông qua việc xem xét nguồn gốc, thách thức và thành tựu của dự án, chúng ta có được những hiểu biết quý giá về cả sự phức tạp về mặt kỹ thuật của quá trình phát triển [ASIC](https://planb.academy/resources/glossary/asic) và sức mạnh của sự hợp tác nguồn mở trong không gian Bitcoin.


### Câu chuyện nguồn gốc: Từ khám phá Con đường tơ lụa đến tầm nhìn năng lượng mặt trời Mining


Skot, người sáng lập Bitaxe, bắt đầu hành trình khám phá Bitcoin tại một bữa tiệc sinh viên, nơi anh lần đầu biết đến Bitcoin thông qua một người mua hàng trên Con đường Tơ lụa. Lần đầu tiên tiếp xúc với Bitcoin với giá khoảng 20 đô la một đồng đã khơi dậy sự tò mò, sau này phát triển thành một dự án mining mang tính cách mạng. Nền tảng kỹ thuật cho công việc tương lai của anh được thiết lập trong thời gian học đại học, nơi anh được tiếp cận với nguồn tài nguyên FPGA phong phú trong môi trường phòng thí nghiệm. Làm việc cùng với người giám sát của mình, Skot bắt đầu thử nghiệm các luồng bit FPGA nguồn mở cho Bitcoin mining, ban đầu với mục tiêu khiêm tốn là Bitcoin đủ tiền để mua một chiếc pizza cho văn phòng của họ.


Quá trình chuyển đổi từ thử nghiệm học thuật sang phát triển nghiêm túc diễn ra nhiều năm sau đó, khi Skot đang nghiên cứu các cổng năng lượng mặt trời cho việc thu thập dữ liệu từ xa ở Châu Phi. Kinh nghiệm chuyên môn với hệ thống năng lượng mặt trời này đã khơi dậy nhận thức rằng ASIC Bitcoin mining, về cơ bản là các thiết bị DC điện áp thấp, sẽ kết hợp hoàn hảo với các tấm pin mặt trời. Ý tưởng này có vẻ tự nhiên và tinh tế. Tuy nhiên, khi Skot bắt đầu nghiên cứu các giải pháp hiện có, ông phát hiện ra một khoảng trống đáng kể trên thị trường: không giống như những ngày đầu của Bitcoin mining khi các thiết kế FPGA được công khai, sự ra đời của ASIC đã đưa ngành công nghiệp này hướng tới các giải pháp hoàn toàn độc quyền, mã nguồn đóng.


Việc thiếu phần cứng mining nguồn mở đã trở thành một trở ngại lớn đối với Skot, đặc biệt là khi xét đến kinh nghiệm phát triển phần mềm nguồn mở của anh và niềm tin rằng bản chất nguồn mở của Bitcoin nên được mở rộng sang cơ sở hạ tầng mining. Sự thống nhất triết lý này với các nguyên tắc nguồn mở, cùng với thách thức kỹ thuật trong việc thiết kế ngược các thiết kế ASIC độc quyền, đã đặt nền móng cho dự án Bitaxe sau này. Tầm nhìn ban đầu đầy tham vọng nhưng cũng rất thực tế: tạo ra một [máy đào](https://planb.academy/resources/glossary/miner) Bitcoin chạy bằng năng lượng mặt trời, có thể hoạt động độc lập mà không cần máy tính riêng để điều khiển, giúp nó phù hợp để triển khai ở những vị trí xa xôi dưới các tấm pin mặt trời.


### Những thách thức kỹ thuật và đột phá về kỹ thuật đảo ngược


Việc phát triển Bitaxe đòi hỏi phải vượt qua những trở ngại kỹ thuật đáng kể, chủ yếu xoay quanh việc thiếu tài liệu hướng dẫn về chip ASIC của Bitmain. Cách tiếp cận của Skot đối với thách thức này thể hiện sự quyết tâm và khéo léo cần thiết để thực hiện kỹ thuật đảo ngược thành công. Không được tiếp cận với các bảng dữ liệu chính thức hoặc thông số kỹ thuật, ông phải dùng đến việc kiểm tra chip dưới kính hiển vi, đo khoảng cách giữa các chân cắm bằng thước cặp, và thậm chí quét chip để xác định chính xác yêu cầu về diện tích tiếp xúc (footprint) của chúng. Quá trình tỉ mỉ này đã dẫn đến nhiều nguyên mẫu thất bại, với hai lần lặp lại đầu tiên của "máy đào ban ngày" không hoạt động bình thường do tính toán diện tích tiếp xúc không chính xác.


Bước đột phá đến với lần lặp lại thứ ba vào tháng 5 năm 2022, khi Skot tạo thành công một thiết kế hai chip hoạt động được bằng cách sử dụng chip BM1387 được lấy từ các máy Antminer S9. Thành tựu này đánh dấu sự ra đời của tên gọi Bitaxe, lấy cảm hứng từ ý tưởng về một chiếc cuốc chim cho Bitcoin mining. Thành công của thiết kế này đã xác nhận phương pháp thiết kế ngược và chứng minh rằng các nhà phát triển độc lập có thể tạo ra phần cứng mining hoạt động mà không cần sự hỗ trợ của nhà sản xuất. Tuy nhiên, những thách thức kỹ thuật không chỉ nằm ở giao diện chip mà còn bao gồm cả thiết kế bộ nguồn phức tạp, vì ASIC yêu cầu điều chỉnh điện áp chính xác ở dòng điện cao, thường hoạt động ở điện áp thấp tới 0,6 vôn trong khi tiêu thụ một lượng ampe đáng kể.


Việc phát triển firmware lại thêm một tầng phức tạp nữa, vì dự án yêu cầu tạo ra phần mềm mining có thể chạy trực tiếp trên vi điều khiển ESP32 thay vì dựa vào các máy tính bên ngoài chạy phần mềm như CGMiner. Cách tiếp cận độc lập này là yếu tố then chốt cho tầm nhìn của Skot về các thiết bị mining có thể triển khai độc lập. Sự kết hợp giữa kỹ thuật đảo ngược phần cứng và phát triển firmware nhúng đã tạo ra một thách thức kỹ thuật toàn diện, đòi hỏi chuyên môn trên nhiều lĩnh vực, từ kỹ thuật điện và thiết kế PCB đến lập trình nhúng và giao thức mạng.


### Hình thành cộng đồng và hợp tác nguồn mở


Việc Bitaxe chuyển đổi từ một dự án đơn lẻ thành một sáng kiến cộng đồng phát triển mạnh mẽ là một trong những khía cạnh quan trọng nhất trong thành công của dự án. Ban đầu, những nỗ lực của Skot nhằm thu hút sự quan tâm của generate thông qua các diễn đàn và mạng xã hội Bitcoin chỉ gặp phải phản hồi hạn chế và đôi khi còn tỏ ra hoài nghi. Bước đột phá đến khi các thành viên cộng đồng như SirVapesAlot nhận ra tiềm năng của mining mã nguồn mở và thành lập máy chủ Discord Open Source Miners United (OSMU). Nền tảng này cung cấp môi trường hợp tác cần thiết để dự án phát triển mạnh mẽ, thu hút những người đóng góp từ nhiều nền tảng khác nhau, những người có chung mối quan tâm trong việc dân chủ hóa công nghệ Bitcoin mining.


Mô hình phát triển do cộng đồng thúc đẩy đã chứng minh hiệu quả đáng kể, với sự xuất hiện của những người đóng góp chủ chốt như johnny9 và Ben để giải quyết những thách thức kỹ thuật cụ thể. Chuyên môn của Johnny9 trong phát triển phần mềm cơ sở đã giải quyết các vấn đề triển khai phần mềm quan trọng, trong khi kỹ năng phát triển front-end của Ben đã tạo ra bảng điều khiển AxeOS trực quan, giúp đơn giản hóa việc cấu hình và giám sát thiết bị. Những đóng góp bổ sung của Ben bao gồm việc thiết lập năng lực sản xuất và tạo ra Public Pool, một [pool mining](https://planb.academy/resources/glossary/pool-mining) mã nguồn mở được tối ưu hóa cho các thiết bị Bitaxe. Phương pháp tiếp cận hợp tác này đã chứng minh các nguyên tắc nguồn mở có thể đẩy nhanh quá trình phát triển vượt xa những gì một cá nhân đóng góp có thể đạt được một cách độc lập.


Cộng đồng OSMU cũng tạo dựng một môi trường hòa nhập, nơi những người mới đến có thể học hỏi và đóng góp bất kể trình độ chuyên môn kỹ thuật ban đầu của họ. Hành trình của Ben từ một người mới vào nghề hàn đến một nhà sản xuất lớn là minh chứng rõ ràng cho cách tiếp cận cởi mở này đối với việc phát triển kỹ năng. Cam kết của cộng đồng đối với việc giáo dục và hỗ trợ lẫn nhau đã tạo ra một vòng tròn lành mạnh, nơi các thành viên giàu kinh nghiệm hướng dẫn những người mới đến, và sau đó chính họ trở thành những người đóng góp. Mô hình này đã chứng minh được tầm quan trọng của việc mở rộng dự án vượt ra ngoài phạm vi ban đầu và thiết lập một hệ sinh thái bền vững cho sự đổi mới và tăng trưởng liên tục.


### Tầm nhìn cho Mining phi tập trung và tác động trong tương lai


Tầm nhìn dài hạn của Skot dành cho Bitaxe không chỉ dừng lại ở việc tạo ra một thiết bị mining khác: đó là một sự chuyển đổi cơ bản trong bối cảnh mining của Bitcoin. Mục tiêu đầy tham vọng là sản xuất một triệu máy đào một terahash sẽ tạo ra một exahash năng lượng mining phân tán, đại diện cho một bước tiến đáng kể hướng tới sự phi tập trung hóa mining. Tầm nhìn này giải quyết những lo ngại quan trọng về việc tập trung hóa mining, nơi các nhóm khai thác lớn và hoạt động công nghiệp có khả năng chịu áp lực từ chính phủ hoặc sự kiểm soát của cơ quan quản lý. Bằng cách phân phối năng lượng mining cho vô số máy đào tại nhà, mạng lưới trở nên linh hoạt hơn và phù hợp với các nguyên tắc phi tập trung của Bitcoin.


Mô hình kinh tế hỗ trợ tầm nhìn này dựa trên các đặc điểm độc đáo của mining tại nhà, nơi chi phí cơ sở hạ tầng gần như bằng không và thợ đào có thể hoạt động với sự giám sát tối thiểu. Không giống như các hoạt động mining công nghiệp đòi hỏi đầu tư vốn lớn vào cơ sở vật chất, cơ sở hạ tầng điện và hệ thống làm mát, thợ đào tại nhà chỉ cần cắm thiết bị vào ổ cắm điện và kết nối internet hiện có. Về mặt lý thuyết, phương pháp này có thể mang lại [tỷ lệ băm](https://planb.academy/resources/glossary/hashrate) đáng kể mà không cần các rào cản gia nhập truyền thống thường gặp ở các hoạt động mining quy mô lớn.


Thành công của dự án đã bắt đầu tác động đến hệ sinh thái Bitcoin mining rộng lớn hơn, với tiềm năng truyền cảm hứng cho các nhà sản xuất khác áp dụng các mô hình phát triển nguồn mở. Khả năng tài chính khả thi mà các nhà sản xuất Bitaxe chứng minh chứng minh rằng phần cứng nguồn mở có thể thành công về mặt thương mại mà vẫn duy trì được tính minh bạch và sự tham gia của cộng đồng. Khi dự án tiếp tục phát triển với các tích hợp chip mới, thiết kế được cải tiến và quan hệ đối tác sản xuất được mở rộng, nó đóng vai trò là bằng chứng về cách Bitcoin mining có thể quay trở lại nguồn gốc phi tập trung của nó trong khi áp dụng công nghệ ASIC hiện đại. Mục tiêu cuối cùng không chỉ đơn thuần là phân phối tỷ lệ băm mà còn bao gồm tác động giáo dục, giúp nhiều người tiếp xúc trực tiếp với quy trình mining cơ bản của Bitcoin và thúc đẩy sự hiểu biết sâu sắc hơn về mô hình bảo mật của mạng.


## Bitaxe là gì?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Tổng quan và Khả năng của Phần cứng


Hệ sinh thái Bitaxe bao gồm nhiều phiên bản phần cứng, mỗi phiên bản được thiết kế để tối ưu hóa các khía cạnh khác nhau của trải nghiệm mining trong khi vẫn duy trì triết lý cốt lõi về khả năng truy cập mã nguồn mở. Các thiết bị này không chỉ đóng vai trò là phần cứng mining chức năng mà còn là công cụ giáo dục cho phép người dùng hiểu được mối quan hệ phức tạp giữa chip ASIC, vi điều khiển và quy trình Bitcoin. Việc hiểu được triết lý thiết kế và triển khai kỹ thuật của Bitaxe mang lại những hiểu biết sâu sắc về cách phần cứng mining hiện đại hoạt động ở cả cấp độ linh kiện và hệ thống.



### Bitaxe Max, Triển khai thế hệ đầu tiên


Bitaxe Max đại diện cho việc triển khai nền tảng của khái niệm Bitaxe, sử dụng chip BM1397 ASIC ban đầu được Bitmain phát triển cho dòng sản phẩm S17 mining của họ. Việc tích hợp chip này chứng minh cách phần cứng nguồn mở có thể tái sử dụng công nghệ ASIC hiện có để tạo ra các giải pháp mining dễ tiếp cận. Bitaxe Max cung cấp tốc độ băm ước tính từ 300 đến 400 gigahash mỗi giây, định vị nó là một nền tảng mining mang tính giáo dục và thử nghiệm hơn là một giải pháp quy mô thương mại.


Việc tích hợp chip BM1397 vào Bitaxe Max đòi hỏi sự cân nhắc kỹ lưỡng về quản lý năng lượng, kiểm soát nhiệt độ và giao thức truyền thông. Thiết kế của bo mạch đáp ứng các yêu cầu cụ thể của ASIC này, đồng thời cung cấp mạch hỗ trợ cần thiết cho hoạt động ổn định. Việc triển khai này cho thấy cách phát triển phần cứng nguồn mở có thể tận dụng công nghệ bán dẫn hiện có để tạo ra các ứng dụng và cơ hội học tập mới trong cộng đồng mining.


### Bitaxe Ultra, Công nghệ chip tiên tiến


Bitaxe Ultra đại diện cho sự phát triển của nền tảng Bitaxe, tích hợp chip BM1366 ASIC tiên tiến hơn từ dòng S19 của Bitmain. Công nghệ chip mới hơn này mang lại hiệu suất và đặc tính hiệu năng được cải thiện cho nền tảng Bitaxe, đồng thời vẫn duy trì triết lý thiết kế cơ bản. Việc nâng cấp lên chip BM1366 chứng minh khả năng thích ứng của nền tảng và cam kết của cộng đồng trong việc tích hợp những tiến bộ công nghệ vào các giải pháp mining nguồn mở.


Việc chuyển đổi từ chip BM1397 sang chip BM1366 đòi hỏi phải điều chỉnh hệ thống cung cấp điện, quản lý nhiệt và thuật toán điều khiển của bo mạch. Những thay đổi này minh họa cho tính chất lặp đi lặp lại của quá trình phát triển phần cứng và tầm quan trọng của việc duy trì khả năng tương thích trong khi vẫn nâng cao hiệu suất. Việc triển khai Bitaxe Ultra cung cấp cho người dùng quyền truy cập vào công nghệ ASIC mới hơn trong khi vẫn duy trì tính chất giáo dục và thử nghiệm của nền tảng.


### Hệ thống vi điều khiển và truyền thông


Trung tâm của mỗi thiết bị Bitaxe là một bộ vi điều khiển ESP, đóng vai trò là giao diện chính giữa người dùng và chip ASIC. Bộ vi điều khiển này chạy phần mềm chuyên dụng do cộng đồng Open Source Miners United (OSMU) phát triển, cho phép kiểm soát chính xác các thông số hoạt động của ASIC. Giao tiếp giữa bộ vi điều khiển và ASIC được thực hiện thông qua các đường truyền nối tiếp được thiết kế cẩn thận, được khắc trực tiếp lên bảng mạch in dưới dạng các dấu vết có thể nhìn thấy.


Vai trò của vi điều khiển không chỉ giới hạn ở việc điều khiển ASIC đơn giản: nó bao gồm quản lý nguồn điện, giám sát nhiệt độ và các chức năng giao diện người dùng. Thông qua màn hình hiển thị tích hợp, người dùng có thể theo dõi các thông số vận hành quan trọng như nhiệt độ, tốc độ băm, địa chỉ IP và các số liệu thống kê liên quan khác của mining. Hệ thống phản hồi thời gian thực này cung cấp những thông tin chi tiết có giá trị về hiệu suất của thiết bị và giúp người dùng tối ưu hóa hoạt động của mining, đồng thời tìm hiểu về hoạt động của phần cứng bên dưới.


### Quản lý điện năng và cân nhắc về an toàn


Nền tảng Bitaxe hoạt động với yêu cầu nguồn điện 5 volt nghiêm ngặt, khiến việc lựa chọn nguồn điện phù hợp trở nên vô cùng quan trọng đối với tuổi thọ và độ an toàn của thiết bị. Hệ thống quản lý nguồn trên bo mạch Bitaxe bao gồm các mạch điện tinh vi được thiết kế để điều chỉnh điện áp cung cấp cho chip ASIC, đồng thời giám sát mức tiêu thụ điện năng ở các chế độ hoạt động khác nhau. Khả năng quản lý nguồn này cho phép thiết bị hoạt động hiệu quả trên nhiều tần số và điện áp bên trong, thường tiêu thụ từ 5 đến 25 watt tùy thuộc vào cấu hình.


Hiểu rõ các yêu cầu về công suất trở nên vô cùng quan trọng khi xét đến việc áp dụng điện áp không đúng cách có thể làm hỏng thiết bị vĩnh viễn. Mối quan hệ giữa tần số, điện áp, mức tiêu thụ điện năng và tốc độ băm minh họa các nguyên tắc cơ bản của hoạt động ASIC, áp dụng trên toàn bộ phần cứng mining. Người dùng có thể thử nghiệm với các cài đặt công suất khác nhau để hiểu rõ những đánh đổi về hiệu suất vốn có trong hoạt động của mining, đồng thời tích lũy kinh nghiệm thực tế với các khái niệm áp dụng cho việc triển khai mining quy mô lớn.


### Tập trung và tham gia mạng lưới Solo Mining


Nền tảng Bitaxe đặc biệt nhắm đến các ứng dụng mining đơn lẻ, nơi các thợ đào riêng lẻ cố gắng giải quyết các [khối](https://planb.academy/resources/glossary/block) Bitcoin một cách độc lập thay vì tham gia vào các nhóm mining lớn. Mặc dù tỷ lệ băm của các thiết bị Bitaxe khiến việc khám phá khối thành công về mặt thống kê là không chắc chắn, nhưng cách tiếp cận này phục vụ các mục đích giáo dục và triết lý quan trọng trong cộng đồng Bitcoin. mining đơn lẻ với các thiết bị Bitaxe giúp người dùng hiểu được cơ chế cơ bản của hệ thống [proof-of-work](https://planb.academy/resources/glossary/proof-of-work) của Bitcoin, đồng thời góp phần vào sự phân cấp mạng lưới.


Việc tập trung vào mining đơn lẻ phản ánh cam kết của cộng đồng OSMU trong việc khuyến khích sự tham gia cá nhân vào mô hình bảo mật của Bitcoin. Bằng cách cung cấp phần cứng dễ tiếp cận và hoạt động độc lập, nền tảng Bitaxe cho phép người dùng tự vận hành mining mà không cần dựa vào cơ sở hạ tầng nhóm. Cách tiếp cận này thúc đẩy sự hiểu biết sâu sắc hơn về cơ chế [đồng thuận](https://planb.academy/resources/glossary/consensus) của Bitcoin, đồng thời hỗ trợ tính chất phi tập trung của mạng lưới thông qua việc tăng cường tính đa dạng của thợ đào.


### Sự phát triển của phần cứng và cải tiến sản xuất


Nền tảng Bitaxe tiếp tục phát triển thông qua phản hồi của cộng đồng và tối ưu hóa sản xuất, với các phiên bản mới hơn tích hợp những cải tiến giúp nâng cao khả năng sản xuất và trải nghiệm người dùng. Các bản cập nhật phiên bản thường tập trung vào hiệu quả sản xuất hơn là những thay đổi cơ bản về hiệu suất, đảm bảo người dùng hiện tại không phải đối mặt với áp lực lỗi thời. Các tính năng như chuyển đổi từ đầu nối micro-USB sang USB-C và hệ thống kết nối nguồn được cải tiến phản ánh sự chú ý của cộng đồng đối với những cải tiến về khả năng sử dụng thực tế.


Cách tiếp cận mang tính tiến hóa này minh chứng cho lợi ích của việc phát triển phần cứng nguồn mở, nơi ý kiến đóng góp của cộng đồng thúc đẩy những cải tiến gia tăng mang lại lợi ích cho tất cả người dùng. Triết lý "nếu nó băm, nó băm" nhấn mạnh sự tập trung của nền tảng vào chức năng hơn là nâng cấp liên tục, khuyến khích người dùng bảo trì và vận hành thiết bị của họ thay vì theo đuổi các phiên bản mới nhất. Cách tiếp cận này hỗ trợ các hoạt động phần cứng bền vững đồng thời duy trì giá trị giáo dục của Bitaxe.


## Tôi có thể tìm hiểu thêm ở đâu?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Dự án Bitaxe đại diện cho một sáng kiến mining mã nguồn mở toàn diện, vượt xa phạm vi một thiết bị đơn lẻ. Việc tìm kiếm thông tin đáng tin cậy, tài nguyên kỹ thuật và hỗ trợ cộng đồng là vô cùng quan trọng đối với bất kỳ ai muốn tham gia vào hệ sinh thái này. Chương này cung cấp hướng dẫn đầy đủ về các nền tảng và tài nguyên thiết yếu tạo nên nền tảng của cộng đồng Bitaxe và Open Source Miners United (OSMU).


### Bitaxe.org, Trung tâm


Trang web Bitaxe.org đóng vai trò là cổng thông tin chính cho tất cả thông tin và tài nguyên liên quan đến dự án. Nền tảng tập trung này hoạt động như điểm tham khảo đầu tiên của bạn bất cứ khi nào bạn cần tìm hiểu về các thiết bị Bitaxe hoặc khám phá các dự án khác trong cộng đồng OSMU. Thiết kế của trang web ưu tiên tính dễ tiếp cận và tính tổ chức, cung cấp cho người truy cập các liên kết được chọn lọc kỹ lưỡng, kết nối đến nhiều tài nguyên chuyên biệt khác nhau trong toàn bộ hệ sinh thái.


Tầm quan trọng của trung tâm này không thể được đánh giá quá cao, vì nó loại bỏ sự nhầm lẫn thường đi kèm với các dự án nguồn mở phi tập trung. Thay vì phải tìm kiếm trên nhiều nền tảng hoặc dựa vào thông tin có thể đã lỗi thời từ các nguồn không chính thức, người dùng có thể tin tưởng Bitaxe.org cung cấp các liên kết cập nhật, đã được xác minh đến tất cả các tài nguyên thiết yếu. Cách tiếp cận này đảm bảo rằng cả người mới và thành viên cộng đồng giàu kinh nghiệm đều có thể tìm thấy thông tin cụ thể mà họ cần cho dự án của mình một cách hiệu quả.


### Tài nguyên kỹ thuật và tài liệu phát triển


Kho lưu trữ tệp thiết kế phần cứng trên GitHub là một trong những nguồn tài nguyên giá trị nhất cho bất kỳ ai quan tâm đến việc tìm hiểu hoặc xây dựng các thiết bị Bitaxe. Kho lưu trữ công khai này chứa tài liệu toàn diện, bao gồm mọi khía cạnh của quy trình thiết kế phần cứng, từ khái niệm ban đầu đến thông số kỹ thuật sản xuất cuối cùng. Kho lưu trữ bao gồm hình ảnh chi tiết, mục tiêu dự án, mô tả tính năng và giải thích linh kiện tích hợp, cung cấp cả chiều sâu kỹ thuật lẫn hướng dẫn thực tế.


Đối với những ai quan tâm đến việc tự sản xuất thiết bị, kho lưu trữ bao gồm các tệp tài liệu cụ thể như building.md, cung cấp hướng dẫn từng bước cho toàn bộ quy trình sản xuất. Tài liệu này bao gồm các công cụ phần mềm cần thiết cho thiết kế PCB, quy trình gửi tệp cho nhà sản xuất và các bước liên quan đến việc tiếp nhận và xác thực PCB đã sản xuất. Mức độ chi tiết này đảm bảo rằng các cá nhân hoặc tổ chức nhỏ có thể điều hướng thành công quy trình sản xuất mà không cần nhiều kinh nghiệm về sản xuất phần cứng.


Kho lưu trữ ESP-Miner đóng vai trò là nơi lưu trữ trung tâm tất cả mã và tài liệu liên quan đến firmware. Kho lưu trữ GitHub này chứa mọi dòng mã được viết cho firmware Bitaxe, cùng với tài liệu toàn diện giải thích các yêu cầu hệ thống, thông số kỹ thuật phần cứng và các tùy chọn cấu hình. Cấu trúc kho lưu trữ được thiết kế để phù hợp với cả người dùng ưa chuộng tệp nhị phân được biên dịch sẵn và các nhà phát triển muốn xây dựng firmware từ mã nguồn.


Tài liệu trong kho lưu trữ này bao gồm các phần chi tiết về yêu cầu phần cứng, tùy chọn cấu hình trước và giá trị khuyến nghị cho nhiều cài đặt khác nhau. Thông tin này rất hữu ích cho người dùng muốn tùy chỉnh thiết bị hoặc khắc phục sự cố cụ thể. Ngoài ra, kho lưu trữ còn bao gồm thông tin về các phát triển mới hơn, chẳng hạn như tích hợp Raspberry Pi, đảm bảo tài liệu luôn cập nhật với sự phát triển liên tục của dự án.


### Công cụ quản lý và bảo trì thiết bị


Trình flasher web Bitaxe là một giải pháp thiết thực cho việc bảo trì và cập nhật thiết bị. Công cụ dựa trên web này cho phép người dùng flash firmware vào thiết bị mà không cần phần mềm chuyên dụng hay quy trình dòng lệnh phức tạp. Trình flasher hỗ trợ nhiều biến thể thiết bị, bao gồm Bitaxe Ultra với nhiều phiên bản cổng khác nhau và các mẫu Bitaxe Max cũ hơn. Người dùng có thể lựa chọn giữa việc cập nhật firmware hiện có thông qua giao diện web hoặc thực hiện khôi phục cài đặt gốc hoàn toàn bằng kết nối USB.


Công cụ này giải quyết một trong những thách thức phổ biến nhất mà những người đam mê phần cứng gặp phải: duy trì và cập nhật firmware thiết bị. Bằng cách cung cấp giao diện web thân thiện với người dùng, công cụ flasher loại bỏ nhiều rào cản kỹ thuật có thể ngăn cản người dùng cập nhật thiết bị của họ với các bản phát hành firmware mới nhất. Thiết kế của công cụ ưu tiên sự đơn giản nhưng vẫn duy trì tính linh hoạt cần thiết cho các cấu hình thiết bị và tình huống cập nhật khác nhau.


### Nền tảng cộng đồng và kênh truyền thông


Máy chủ Discord là trung tâm của tương tác và hỗ trợ cộng đồng thời gian thực trong hệ sinh thái Bitaxe. Tổ chức của máy chủ phản ánh sở thích và nhu cầu đa dạng của các thành viên cộng đồng, với các kênh được cấu trúc cẩn thận, tạo điều kiện cho các cuộc thảo luận tập trung vào các chủ đề cụ thể. Thành viên mới sẽ trải qua quy trình xác minh, yêu cầu đọc và chấp nhận các quy tắc cộng đồng, đảm bảo tất cả người tham gia đều hiểu rõ các kỳ vọng về tương tác tôn trọng và hiệu quả.


Cấu trúc kênh của máy chủ bao gồm các khu vực thảo luận chung về các chủ đề như tích hợp năng lượng mặt trời, nhóm mining và các cuộc thảo luận liên quan đến Bitcoin. Các phần chuyên sâu hơn tập trung vào các thiết bị cụ thể, bao gồm các kênh dành riêng cho các biến thể Bitaxe Ultra, Hex và Supra. Kênh firmware cung cấp một không gian tập trung cho các cuộc thảo luận kỹ thuật về phát triển phần mềm và khắc phục sự cố, trong khi kênh phát hành chính thức đảm bảo các thành viên cộng đồng nhận được thông báo kịp thời về các phát triển mới.


Dự án cũng có khu vực dành cho người đăng ký, mang đến các lợi ích bổ sung cho các thành viên cộng đồng lựa chọn hỗ trợ tài chính cho dự án. Phương pháp tiếp cận phân tầng này cho phép cộng đồng cung cấp các dịch vụ nâng cao trong khi vẫn duy trì quyền truy cập mở vào các kênh thông tin và hỗ trợ thiết yếu. Kênh trợ giúp đóng vai trò là không gian chuyên dụng để khắc phục sự cố và hỗ trợ kỹ thuật, đảm bảo người dùng nhận được hỗ trợ kịp thời khi gặp khó khăn.



Wiki Open Source Miners United (osmu.wiki) cung cấp tài liệu toàn diện, bổ sung cho các cuộc thảo luận trực tiếp diễn ra trên Discord. Không giống như các nền tảng trò chuyện, wiki này cung cấp tài liệu có cấu trúc, có thể tìm kiếm, bao quát mọi khía cạnh của dự án Bitaxe và các sáng kiến liên quan. Cách thức tổ chức của wiki phản ánh cấu trúc của dự án, với các mục riêng cho từng dòng thiết bị và hướng dẫn thiết lập toàn diện.


Bản chất mã nguồn mở của wiki cho phép các thành viên cộng đồng đóng góp trực tiếp vào tài liệu. Người dùng có thể chỉnh sửa trang, gửi bản sửa lỗi và thêm thông tin mới thông qua tích hợp GitHub, đảm bảo cơ sở kiến thức luôn được cập nhật và minh bạch. Phương pháp tiếp cận hợp tác này tận dụng chuyên môn chung của cộng đồng, đồng thời duy trì kiểm soát chất lượng thông qua quy trình xem xét các thay đổi được gửi.


Wiki bao gồm các tài nguyên thiết thực như hướng dẫn cài đặt PDF cung cấp hướng dẫn từng bước về cấu hình và sử dụng thiết bị. Những hướng dẫn này đóng vai trò là tài liệu tham khảo hữu ích cho cả người dùng mới và thành viên cộng đồng giàu kinh nghiệm, những người cần truy cập nhanh vào các quy trình hoặc chi tiết cấu hình cụ thể.


### Thông tin mua hàng và nhà cung cấp


Danh sách hợp pháp của Bitaxe giải quyết một nhu cầu quan trọng trong cộng đồng phần cứng nguồn mở: xác định các nhà cung cấp đáng tin cậy và tránh những người bán gian lận. Danh sách được tuyển chọn này bao gồm các nhà bán lẻ và nhà sản xuất đã được xác minh, đáp ứng các tiêu chí cụ thể về tính hợp pháp và hỗ trợ cộng đồng. Mỗi danh sách đều bao gồm các liên kết trực tiếp đến trang web của nhà cung cấp, thông tin khu vực và mô tả công ty, giúp người dùng đưa ra quyết định mua hàng sáng suốt.


Điều quan trọng là danh sách này cho biết liệu mỗi nhà cung cấp có đóng góp trở lại cho cộng đồng OSMU hay không, dù là về mặt tài chính hay thông qua các hình thức hỗ trợ khác. Sự minh bạch này giúp các thành viên cộng đồng hiểu rõ nhà cung cấp nào đang tích cực hỗ trợ sự phát triển và tính bền vững của dự án. Danh sách này cũng đóng vai trò là một biện pháp bảo vệ chống lại các hình thức lừa đảo phổ biến, chẳng hạn như việc đặt hàng trước trái phép các sản phẩm chưa phát hành, vốn trước đây đã gây ra nhiều vấn đề trong cộng đồng.


Việc nhấn mạnh vào các liên kết không liên kết thể hiện cam kết của cộng đồng trong việc cung cấp các đề xuất nhà cung cấp khách quan. Người dùng có thể tin tưởng rằng các đề xuất này dựa trên tính hợp pháp của nhà cung cấp và đóng góp của cộng đồng hơn là các ưu đãi tài chính, đảm bảo rằng các quyết định mua hàng hỗ trợ cả nhu cầu cá nhân và tính bền vững của cộng đồng.



# Phần mềm và Hoạt động

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## AxeOS là gì?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS là phần mềm hệ thống và giao diện web dành cho thiết bị Bitaxe mining, cung cấp cho người dùng khả năng kiểm soát và giám sát toàn diện thông qua bảng điều khiển trực quan dựa trên trình duyệt. Hệ thống này biến nhiệm vụ quản lý ASIC phức tạp thành trải nghiệm dễ tiếp cận, cho phép thợ đào theo dõi hiệu suất, điều chỉnh cài đặt và quản lý nhiều thiết bị từ một giao diện duy nhất. Hiểu rõ AxeOS là điều cần thiết để tối đa hóa tiềm năng thiết bị Bitaxe của bạn và duy trì hoạt động tối ưu của mining.


### Tổng quan về bảng điều khiển và số liệu cốt lõi


Bảng điều khiển AxeOS đóng vai trò là cửa sổ chính để bạn theo dõi hiệu suất thiết bị Bitaxe, hiển thị các số liệu quan trọng của mining theo định dạng thời gian thực, được sắp xếp hợp lý. Khi bạn truy cập địa chỉ IP của thiết bị Bitaxe, bạn sẽ ngay lập tức thấy bốn chỉ số hiệu suất chính xác định trạng thái hoạt động hiện tại của mining. Màn hình hiển thị tốc độ băm cho thấy tốc độ tính toán thực tế mà chip ASIC của bạn đang tạo ra khi xử lý mẫu khối hiện tại, cung cấp phản hồi tức thì về chức năng cốt lõi của thiết bị.


Bên cạnh tỷ lệ băm, bộ đếm chia sẻ theo dõi mọi giải pháp hợp lệ mà thiết bị Bitaxe của bạn gửi đến nhóm mining, tăng dần với mỗi lần gửi thành công và đóng vai trò là thước đo trực tiếp về đóng góp của thiết bị vào nỗ lực mining của nhóm. Chỉ số hiệu suất cung cấp thông tin chi tiết quan trọng về hiệu suất năng lượng của thiết bị bằng cách tính toán tỷ lệ băm trên mức tiêu thụ điện năng, giúp bạn tối ưu hóa lợi nhuận vận hành. Chỉ báo độ khó tốt nhất lưu giữ hồ sơ về tỷ lệ độ khó cao nhất mà thiết bị của bạn từng đạt được, duy trì thành tích này ngay cả khi khởi động lại và cập nhật, chỉ đặt lại khi bạn thực hiện flash hoàn toàn về cài đặt gốc.


Hệ thống menu mở rộng của bảng điều khiển, được điều khiển bằng nút chuyển đổi, cung cấp quyền truy cập vào tất cả các chức năng của AxeOS trong khi vẫn duy trì giao diện gọn gàng. Biểu đồ tỷ lệ băm trực tiếp là một trong những tính năng giá trị nhất của nó, hiển thị dữ liệu hiệu suất theo thời gian thực, chính xác và đầy đủ thông tin hơn khi bạn duy trì phiên làm việc lâu hơn. Các mục nguồn, nhiệt và hiệu suất cung cấp khả năng giám sát toàn diện trạng thái hoạt động của thiết bị, bao gồm các cảnh báo điện áp đầu vào để cảnh báo bạn về các sự cố tiềm ẩn về nguồn điện, đồng thời đảm bảo hoạt động liên tục trong các thông số an toàn.


### Thông tin hệ thống và giám sát nâng cao


Khả năng giám sát của AxeOS vượt xa khả năng theo dõi tốc độ băm cơ bản, cung cấp thông tin chi tiết về mọi khía cạnh hoạt động của thiết bị Bitaxe. Mục công suất hiển thị mức tiêu thụ điện năng được tính toán từ các mạch tích hợp trên bo mạch, các phép đo điện áp đầu vào từ kết nối nguồn điện của bạn và các mức điện áp ASIC được yêu cầu. Khi xảy ra sụt áp, AxeOS sẽ ngay lập tức hiển thị thông báo cảnh báo, mặc dù những thông báo này thường không ảnh hưởng đến hoạt động của mining mà chỉ đơn giản là chỉ ra các cơ hội tối ưu hóa nguồn điện tiềm năng.


Việc giám sát nhiệt độ tập trung vào quản lý nhiệt chip ASIC, với các giá trị đo được lấy từ các vị trí chiến lược trên thiết bị để cung cấp dữ liệu nhiệt chính xác với độ lệch phù hợp cho độ chính xác cấp chip. Màn hình hiển thị tần số và điện áp cung cấp phản hồi theo thời gian thực về các thông số điều chỉnh ASIC của bạn, với điện áp đo được thể hiện là giá trị đo chính xác nhất hiện có, được lấy trực tiếp tại vị trí chip ASIC. Độ chính xác này cho phép tinh chỉnh các thông số hiệu suất trong khi vẫn duy trì điều kiện vận hành an toàn.


Phần trạng thái kết nối cung cấp khả năng hiển thị tức thì cấu hình nhóm mining của bạn, hiển thị URL tầng hiện tại, cổng và định danh người dùng. Đối với các thiết bị được kết nối với nhóm công cộng, AxeOS tạo các liên kết nhanh tiện lợi đưa bạn trực tiếp đến giao diện web của nhóm, nơi bạn có thể truy cập số liệu thống kê chi tiết, danh sách thiết bị và dữ liệu hiệu suất lịch sử. Sự tích hợp này hợp lý hóa quy trình giám sát bằng cách kết nối thông tin cấp thiết bị và cấp nhóm trong một quy trình làm việc liền mạch.


### Quản lý bầy đàn và kiểm soát nhiều thiết bị


Chức năng Swarm đại diện cho giải pháp của AxeOS cho sự phức tạp của việc quản lý nhiều thiết bị Bitaxe trên mạng, loại bỏ nhu cầu ghi nhớ và điều hướng đến nhiều địa chỉ IP. Hệ thống quản lý tập trung này cho phép bạn thêm thiết bị chỉ bằng cách nhập địa chỉ IP của chúng, tự động phát hiện các máy đào Bitaxe đang hoạt động và tích hợp chúng vào bảng điều khiển thống nhất. Sau khi được cấu hình, Swarm cung cấp khả năng kiểm soát toàn diện toàn bộ hoạt động của mining từ một giao diện duy nhất.


Thông qua giao diện Swarm, bạn có thể thực hiện các tác vụ quản lý quan trọng trên nhiều thiết bị cùng lúc hoặc riêng lẻ, bao gồm thay đổi cấu hình nhóm, khởi động lại thiết bị, điều chỉnh tần suất và giám sát hiệu suất. Phương pháp tập trung này giúp giảm đáng kể chi phí quản lý cho các hoạt động mining quy mô lớn, đồng thời đảm bảo cấu hình nhất quán trên tất cả các thiết bị. Hệ thống duy trì danh tính thiết bị riêng lẻ đồng thời cung cấp khả năng quản lý tập trung, tạo nên sự cân bằng tối ưu giữa kiểm soát chi tiết và hiệu quả vận hành.


Bảng điều khiển Swarm hiển thị trạng thái hiện tại, số liệu hiệu suất và các điều khiển truy cập nhanh cho từng thiết bị được quản lý, cho phép phản hồi nhanh chóng các sự cố về hiệu suất hoặc thay đổi cấu hình. Chức năng này đặc biệt hữu ích đối với các thợ đào vận hành nhiều thiết bị ở nhiều địa điểm khác nhau hoặc những người thường xuyên điều chỉnh các thông số mining dựa trên điều kiện thị trường hoặc hiệu suất của nhóm.


### Quản lý cấu hình và cài đặt hệ thống


Phần Cài đặt của AxeOS cung cấp khả năng kiểm soát toàn diện mọi khía cạnh có thể cấu hình của thiết bị Bitaxe, từ kết nối mạng đến các thông số mining và tối ưu hóa phần cứng. Cấu hình mạng bắt đầu bằng thiết lập Wi-Fi, nơi bạn chỉ định tên mạng và mật khẩu, với AxeOS đề xuất tên mạng đơn, không có khoảng trắng để đảm bảo kết nối đáng tin cậy. Hệ thống xử lý toàn bộ quy trình cấu hình không dây, cho phép quản lý và giám sát từ xa.


Cấu hình Mining tập trung vào cài đặt tầng, nơi bạn chỉ định URL của nhóm mining đã chọn mà không cần tiền tố giao thức hoặc số cổng, được xử lý trong các trường riêng biệt. Trường người dùng tầng đáp ứng các yêu cầu khác nhau của nhóm, hỗ trợ cả địa chỉ Bitcoin cho mining đơn lẻ và hệ thống tên người dùng cho nhóm mining, với khả năng thêm mã định danh thiết bị cho các hoạt động đa thiết bị. Chức năng mật khẩu tầng mới được bổ sung hỗ trợ các nhóm yêu cầu xác thực, mặc dù hầu hết các nhóm công cộng đều hoạt động mà không cần yêu cầu này.


Tối ưu hóa phần cứng thông qua điều chỉnh tần số và điện áp lõi là khả năng tinh chỉnh hiệu năng mạnh mẽ nhất của AxeOS. Tùy thuộc vào phiên bản thiết bị và trình duyệt, các cài đặt này có thể xuất hiện dưới dạng menu thả xuống với cấu hình cài sẵn hoặc dưới dạng trường mở cho phép tùy chỉnh giá trị. Cài đặt mặc định là tần số 485 MHz và điện áp lõi 1200 mV đảm bảo hoạt động ổn định cho thử nghiệm ban đầu, trong khi người dùng nâng cao có thể tối ưu hóa các thông số này để đạt hiệu suất hoặc hiệu quả tối đa dựa trên yêu cầu và điều kiện vận hành cụ thể của họ.


### Bảo trì hệ thống và các tính năng nâng cao


AxeOS bao gồm các tính năng bảo trì hệ thống tinh vi được thiết kế để giữ cho thiết bị Bitaxe của bạn hoạt động ở hiệu suất cao nhất, đồng thời cung cấp thông tin chẩn đoán để khắc phục sự cố và tối ưu hóa. Hệ thống cập nhật đơn giản hóa việc quản lý firmware bằng cách hiển thị bản phát hành mới nhất trực tiếp trên giao diện và cung cấp liên kết tải xuống trực tiếp đến các tệp firmware chính thức. Việc tích hợp này giúp loại bỏ nhu cầu điều hướng thủ công các kho lưu trữ GitHub hoặc quản lý tải xuống tệp, đơn giản hóa quy trình cập nhật chỉ với vài cú nhấp chuột.


Giao diện cập nhật chấp nhận các tệp firmware được đặt tên chính xác, cụ thể là esp-miner.bin và www.bin, đảm bảo khả năng tương thích và ngăn ngừa lỗi cài đặt. Đối với người dùng gặp khó khăn với quy trình cập nhật tiêu chuẩn, AxeOS cung cấp tài liệu tham khảo về các quy trình flash gốc toàn diện, có thể khôi phục thiết bị về chức năng ban đầu. Phương pháp tiếp cận kép này đáp ứng cả các bản cập nhật thông thường và các tình huống khôi phục.


Hệ thống ghi nhật ký cung cấp thông tin chi tiết theo thời gian thực về hoạt động của thiết bị, hiển thị thông tin chi tiết về model chip ASIC, thời gian hoạt động của hệ thống, trạng thái kết nối Wi-Fi, bộ nhớ khả dụng, phiên bản firmware và các bản sửa đổi bo mạch. Những nhật ký này vô cùng hữu ích cho các nhà phát triển và người dùng nâng cao muốn tìm hiểu hành vi của thiết bị, chẩn đoán sự cố hoặc tối ưu hóa hiệu suất. Trình xem nhật ký theo thời gian thực hiển thị dữ liệu hoạt động trực tiếp, bao gồm xử lý [nonce](https://planb.academy/resources/glossary/nonce), tính toán độ khó và các tham số gửi mining, mang đến khả năng hiển thị chưa từng có vào chính quy trình mining.


Các tính năng bổ sung của hệ thống bao gồm điều khiển hướng màn hình cho các thiết bị được sử dụng trong tủ tùy chỉnh, đảo ngược cực tính quạt cho các cấu hình làm mát chuyên dụng và điều khiển quạt tự động, điều chỉnh khả năng làm mát dựa trên nhiệt độ ASIC. Điều khiển tốc độ quạt thủ công cung cấp khả năng quản lý làm mát chính xác khi hệ thống tự động không đáp ứng các yêu cầu cụ thể. Tất cả các thay đổi cấu hình đều yêu cầu lưu và khởi động lại thiết bị để có hiệu lực, đảm bảo hoạt động ổn định và ngăn ngừa các trạng thái cấu hình cục bộ có thể ảnh hưởng đến hiệu suất của mining.



# Cộng đồng và Hợp tác

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Tổng quan về đóng góp nguồn mở

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub và vai trò của nó trong phát triển phần mềm


GitHub đại diện cho một sự thay đổi căn bản trong cách quản lý và chia sẻ các dự án phát triển phần mềm trên toàn cộng đồng lập trình viên toàn cầu. Là một nền tảng đám mây lưu trữ các dự án phát triển phần mềm sử dụng Git, một hệ thống kiểm soát phiên bản phân tán, GitHub cho phép các nhà phát triển cộng tác liền mạch trong các dự án bất kể vị trí địa lý của họ. Nền tảng này vừa là một công cụ kỹ thuật vừa là một mạng xã hội dành cho các lập trình viên, cho phép họ theo dõi các thay đổi, hợp nhất các bản cập nhật, duy trì các phiên bản mã khác nhau và đóng góp vào các sáng kiến nguồn mở như dự án BitX của Open Source Miners United.


Sức mạnh của GitHub nằm ở khả năng đơn giản hóa quy trình phát triển cộng tác phức tạp. Khi nhiều nhà phát triển cùng làm việc trên một dự án, GitHub cung cấp cơ sở hạ tầng để quản lý các đóng góp, xem xét các thay đổi, xử lý các vấn đề của dự án và duy trì tài liệu toàn diện. Phương pháp tiếp cận cộng tác này đã biến GitHub trở thành một thành phần thiết yếu của quy trình phát triển phần mềm hiện đại, chuyển đổi cách thức cả nhà phát triển cá nhân và các tổ chức lớn tiếp cận việc quản lý dự án và chia sẻ mã nguồn.


### Điều hướng GitHub Interface và Cấu trúc Kho lưu trữ


Việc hiểu giao diện GitHub bắt đầu bằng việc nhận biết các thành phần chính tạo nên bất kỳ trang kho lưu trữ nào. Thanh điều hướng trên cùng chứa một số mục quan trọng bao gồm Mã, Sự cố, Yêu cầu kéo, Thảo luận, Hành động, Dự án, Bảo mật và Thông tin chi tiết. Mỗi mục phục vụ một mục đích cụ thể trong hệ sinh thái quản lý dự án, với mục Mã hiển thị các tệp và thư mục thực tế cấu thành dự án.


Cấu trúc kho lưu trữ tự nó phản ánh cách tiếp cận tổ chức của những người bảo trì dự án. Một số kho lưu trữ chỉ chứa một tệp duy nhất, có thể là một tập lệnh shell đơn giản, trong khi những kho lưu trữ khác, chẳng hạn như dự án phần cứng BitX, chứa nhiều tệp được tổ chức thành các thư mục và thư mục con. Tên kho lưu trữ xuất hiện nổi bật và đóng vai trò vừa là định danh vừa là mô tả ngắn gọn về mục đích của dự án. Các yếu tố tương tác thiết yếu bao gồm nút Watch để nhận thông báo về các bản cập nhật kho lưu trữ, nút Fork để tạo bản sao cá nhân của kho lưu trữ, và nút Star hoạt động như một hệ thống xác nhận cộng đồng tương tự như tính năng "thích".


Phần Giới thiệu cung cấp thông tin quan trọng về dự án dưới dạng cô đọng, bao gồm mô tả một dòng, thông tin cấp phép và các chi tiết chính của dự án. Đối với dự án BitX, phần này xác định dự án là "phần cứng đào ASIC Bitcoin mã nguồn mở" và nêu rõ giấy phép GPL 3.0. Việc hiểu rõ về cấp phép đặc biệt quan trọng vì GitHub hoạt động như một nền tảng mã nguồn mở, nơi toàn bộ cộng đồng có thể truy cập các kho lưu trữ công khai nhưng nội dung chỉ có thể được sử dụng và phân phối theo các quy tắc tuân thủ của từng giấy phép.


### Làm việc với các nhánh và phiên bản dự án


Khái niệm nhánh (branch) là một trong những tính năng mạnh mẽ nhất của GitHub trong việc quản lý các phiên bản và hướng phát triển khác nhau trong cùng một dự án. Về cơ bản, nhánh tạo ra một bản sao hoặc phiên bản đã sửa đổi của cơ sở mã nguồn chính, cho phép các nhà phát triển làm việc trên các tính năng cụ thể, sửa lỗi hoặc thay đổi thử nghiệm mà không ảnh hưởng đến dòng phát triển chính. Nhánh chính thường đóng vai trò là phiên bản mặc định và ổn định nhất của dự án, trong khi các nhánh bổ sung hỗ trợ các lần lặp lại, giai đoạn thử nghiệm hoặc các biến thể sản phẩm hoàn toàn khác nhau.


Trong dự án phần cứng BitX, có nhiều nhánh (branch) để quản lý các phiên bản và cấu hình phần cứng khác nhau. Ví dụ: nhánh Ultra v2 chứa các tệp dành riêng cho phiên bản phần cứng đó, trong khi nhánh Super 401 tập trung vào việc triển khai sử dụng chip S21 ASIC để cải thiện hiệu quả. Mỗi nhánh có thể có nhiều commit trước hoặc sau nhánh chính, cho thấy mức độ thay đổi và hoạt động phát triển. Khi xem xét các nhánh khác nhau, người dùng sẽ nhận thấy cấu trúc tệp, tài liệu và thậm chí cả hình ảnh minh họa hoàn toàn khác nhau, phản ánh các yêu cầu và thông số kỹ thuật riêng biệt của từng biến thể phần cứng.


Hệ thống nhánh giúp ngăn ngừa sự nhầm lẫn giữa người đóng góp và người dùng bằng cách phân tách rõ ràng các hướng phát triển khác nhau. Thay vì trộn lẫn các tính năng thử nghiệm với các bản phát hành ổn định, hoặc kết hợp các phiên bản phần cứng khác nhau tại một vị trí, các nhánh cung cấp sự phân tách rõ ràng, đồng thời vẫn duy trì khả năng hợp nhất các thay đổi thành công trở lại dòng phát triển chính khi cần thiết. Phương pháp tiếp cận có tổ chức này đảm bảo người dùng có thể dễ dàng tìm thấy phiên bản cụ thể họ cần trong khi các nhà phát triển có thể làm việc để cải tiến mà không làm gián đoạn dự án chính.


### Đóng góp thông qua các vấn đề


Phần Sự cố đóng vai trò là kênh giao tiếp chính giữa người dùng và người bảo trì dự án để báo cáo sự cố, đề xuất cải tiến và ghi lại lỗi. Tuy nhiên, điều quan trọng cần hiểu là phần Sự cố được thiết kế riêng cho các vấn đề kỹ thuật chính đáng chứ không phải các câu hỏi chung chung hoặc yêu cầu hỗ trợ. Khi người dùng gặp phải sự cố thực tế, hành vi bất ngờ hoặc xác định các cải tiến tiềm năng, việc tạo một sự cố được ghi chép đầy đủ sẽ giúp ích cho toàn bộ cộng đồng bằng cách thu hút sự chú ý đến các vấn đề có thể ảnh hưởng đến nhiều người dùng.


Việc báo cáo sự cố hiệu quả đòi hỏi phải ghi chép chi tiết về sự cố, bao gồm các tình huống dẫn đến sự cố, các bước tái hiện sự cố và bất kỳ chi tiết kỹ thuật liên quan nào. Dự án BitX minh họa nguyên tắc này thông qua nhiều sự cố đã đóng, cho thấy quy trình giải quyết, từ việc xác định vấn đề ban đầu, thông qua thảo luận cộng đồng cho đến giải pháp cuối cùng. Một số sự cố dẫn đến cải tiến phần cứng, chẳng hạn như bổ sung các lỗ lắp để tăng khả năng làm mát, trong khi những sự cố khác có thể được giải quyết thông qua đào tạo người dùng hoặc cập nhật phần mềm.


Sự khác biệt giữa Issues và Discussions rất quan trọng để duy trì tương tác cộng đồng có tổ chức. Trong khi Issues tập trung vào các vấn đề kỹ thuật cụ thể, phần Discussions cung cấp một môi trường giống như diễn đàn cho các câu hỏi, ý tưởng và hoạt động tương tác chung của cộng đồng. Mặc dù máy chủ Discord đã trở thành kênh giao tiếp chính của cộng đồng BitX, phần Thảo luận GitHub vẫn có sẵn cho các cuộc trò chuyện chính thức hoặc có thể tìm kiếm được, nhờ vào tài liệu hướng dẫn lâu dài và dễ tham khảo.


### Hiểu về yêu cầu kéo


Pull Request (Yêu cầu kéo) là cơ chế mà qua đó những người đóng góp bên ngoài đề xuất thay đổi cho kho lưu trữ dự án. Khi ai đó xác định được một cải tiến, sửa lỗi hoặc tính năng mới có lợi cho dự án, họ có thể tạo một Pull Request để gửi những thay đổi của mình để xem xét và tích hợp vào cơ sở mã nguồn chính. Quy trình này đảm bảo rằng tất cả các sửa đổi đều được xem xét trước khi trở thành một phần của dự án chính thức, duy trì chất lượng mã và tính nhất quán của dự án, đồng thời cho phép cộng đồng đóng góp.


Quy trình yêu cầu kéo thường bắt đầu khi người đóng góp phân nhánh kho lưu trữ, tạo bản sao riêng để thực hiện thay đổi, rồi gửi những thay đổi đó trở lại dự án gốc thông qua yêu cầu kéo. Người bảo trì dự án sau đó có thể xem xét các thay đổi được đề xuất, thảo luận về các sửa đổi với người đóng góp, và cuối cùng quyết định có nên hợp nhất các thay đổi đó vào dự án chính hay không. Quy trình đánh giá hợp tác này giúp duy trì các tiêu chuẩn của dự án, đồng thời khuyến khích sự tham gia và cải tiến của cộng đồng.


Hiểu rõ về thẻ và bản phát hành bổ sung thêm một lớp nữa cho quản lý dự án và kiểm soát phiên bản. Thẻ đóng vai trò là điểm đánh dấu trong dòng thời gian phát triển, xác định các điểm cụ thể đại diện cho các phiên bản hoặc cột mốc cụ thể. Trong các dự án phần cứng như BitX, thẻ thường tương ứng với số model hoặc phiên bản phần cứng cụ thể, cung cấp điểm tham chiếu rõ ràng cho người dùng tìm kiếm các phiên bản cụ thể. Bản phát hành, thường được sử dụng nhiều hơn trong các dự án phần mềm, đại diện cho việc phân phối chính thức các tính năng đã hoàn thành và bản sửa lỗi, thường kèm theo ghi chú phát hành chi tiết và các gói có thể tải xuống.


Hệ sinh thái GitHub tạo ra một môi trường toàn diện cho sự cộng tác mã nguồn mở, vượt xa việc chia sẻ tệp đơn thuần. Bằng cách hiểu rõ các thành phần khác nhau này và cách sử dụng hợp lý, những người đóng góp có thể tham gia hiệu quả vào các dự án, giúp cải thiện thiết kế phần mềm và phần cứng, đồng thời hưởng lợi từ kiến thức và nỗ lực chung của cộng đồng phát triển toàn cầu. Dù là báo cáo sự cố, đề xuất cải tiến hay đóng góp mã nguồn, GitHub đều cung cấp các công cụ và cấu trúc cần thiết cho sự cộng tác hiệu quả trong thế giới mã nguồn mở.


## Thực hành đóng góp mã nguồn mở

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Dựa trên nền tảng của việc tạo ra các vấn đề và khám phá các dự án nguồn mở, chương này tập trung vào các khía cạnh thực tế của việc đóng góp trực tiếp thông qua các yêu cầu kéo và quản lý kho lưu trữ. Hiểu cách tạo kho lưu trữ fork, thực hiện thay đổi và gửi yêu cầu kéo là một bộ kỹ năng quan trọng đối với bất kỳ nhà phát triển nào muốn đóng góp có ý nghĩa cho các dự án nguồn mở, dù liên quan đến phát triển phần mềm hay thiết kế phần cứng.


Quy trình đóng góp thay đổi mã tuân theo một quy trình làm việc chuẩn hóa, đảm bảo tính toàn vẹn của dự án đồng thời cho phép phát triển cộng tác. Quy trình làm việc này bao gồm việc tạo bản sao kho lưu trữ dự án của riêng bạn, thực hiện các sửa đổi trong môi trường được kiểm soát, và sau đó đề xuất những thay đổi đó trở lại dự án gốc thông qua một quy trình đánh giá chính thức. Mặc dù các ví dụ trong chương này chủ yếu tập trung vào các đóng góp phần mềm, các nguyên tắc và quy trình tương tự cũng áp dụng cho các dự án phần cứng liên quan đến thiết kế PCB, sơ đồ mạch và các tài liệu kỹ thuật khác.


### Hiểu về Fork và Cấu trúc Kho lưu trữ


Nền tảng để đóng góp cho bất kỳ dự án nguồn mở nào đều bắt đầu bằng việc tạo một fork, đóng vai trò là bản sao cá nhân của kho lưu trữ gốc. Khi bạn điều hướng đến kho lưu trữ GitHub và nhấp vào nút "fork", bạn sẽ tạo một bản sao độc lập trong tài khoản GitHub của riêng mình, duy trì kết nối rõ ràng với nguồn gốc. Kho lưu trữ được phân nhánh này sẽ xuất hiện trong tài khoản của bạn với dấu hiệu rõ ràng về nguồn gốc của nó, hiển thị dòng chữ như "phân nhánh từ [chủ sở hữu gốc]/[tên kho lưu trữ]" bên dưới tiêu đề kho lưu trữ.


Kho lưu trữ phân nhánh của bạn hoạt động độc lập với kho lưu trữ gốc, cho phép bạn thực hiện các thay đổi mà không ảnh hưởng đến dự án chính. Tuy nhiên, nó vẫn duy trì nhận thức về các bản cập nhật cho kho lưu trữ gốc thông qua các tính năng đồng bộ hóa của GitHub. Khi kho lưu trữ gốc nhận được các bản cập nhật mà fork của bạn thiếu, GitHub sẽ hiển thị thông tin trạng thái như "Nhánh này có X commit chậm" hoặc "X commit nhanh", giúp bạn dễ dàng theo dõi mối quan hệ giữa fork của bạn và kho lưu trữ thượng nguồn. Bạn có thể đồng bộ hóa fork của mình với kho lưu trữ gốc bất cứ lúc nào bằng cách nhấp vào nút "Đồng bộ hóa fork", nút này sẽ tự động cập nhật các thay đổi mới nhất từ nguồn thượng nguồn.


Mối quan hệ giữa fork của bạn và kho lưu trữ gốc trở nên đặc biệt quan trọng khi bạn bắt đầu thực hiện các thay đổi. Khi bạn triển khai các sửa đổi và commit chúng lên fork, GitHub sẽ theo dõi những khác biệt này và hiển thị chúng dưới dạng commit trước khi commit lên kho lưu trữ gốc. Hệ thống theo dõi này cho phép thực hiện quy trình pull request, nơi bạn có thể đề xuất các thay đổi để đưa vào dự án chính mà vẫn duy trì lịch sử rõ ràng về những gì đã được sửa đổi.


### Thiết lập môi trường phát triển của bạn


Việc tạo ra một môi trường phát triển hiệu quả đòi hỏi sự chú ý cẩn thận đến cả các công cụ phát triển chung và các yêu cầu cụ thể của từng dự án. Visual Studio Code đóng vai trò là một môi trường phát triển tích hợp (IDE) tuyệt vời cho hầu hết các đóng góp mã nguồn mở, cung cấp các tính năng thiết yếu để chỉnh sửa mã, tích hợp kiểm soát phiên bản và quản lý dự án. Thành phần quan trọng đầu tiên bao gồm việc cài đặt và cấu hình tiện ích mở rộng Git, cho phép tích hợp liền mạch với kho lưu trữ GitHub trực tiếp từ môi trường phát triển của bạn.


Các phiên bản Visual Studio Code hiện đại thường mặc định hỗ trợ Git, nhưng bạn phải xác thực bằng tài khoản GitHub để kích hoạt đầy đủ chức năng. Quy trình xác thực này bao gồm việc đăng nhập vào GitHub thông qua IDE, sau đó cho phép bạn sao chép kho lưu trữ, cam kết thay đổi và đẩy các bản cập nhật trực tiếp từ môi trường phát triển của mình. Tích hợp GitHub xuất hiện dưới dạng biểu tượng ở thanh bên trái, cung cấp quyền truy cập vào các tính năng sao chép kho lưu trữ, quản lý nhánh và đồng bộ hóa mà không cần thao tác dòng lệnh.


Đối với các dự án liên quan đến hệ thống nhúng hoặc nền tảng phần cứng cụ thể, cần có thêm các công cụ bổ sung. Phần mở rộng ESP-IDF là một thành phần quan trọng cho các dự án nhắm đến vi điều khiển ESP32, yêu cầu khả năng tương thích phiên bản cụ thể để đảm bảo chức năng hoạt động bình thường. Quá trình cài đặt bao gồm việc chọn phiên bản ESP-IDF phù hợp, cấu hình đường dẫn công cụ và thiết lập môi trường container phát triển. Phiên bản 5.1.3 hiện là cấu hình được khuyến nghị cho nhiều dự án dựa trên ESP32, mặc dù các yêu cầu này có thể thay đổi khi các dự án cập nhật các phần phụ thuộc và chuỗi công cụ.


### Thực hiện thay đổi và quản lý cam kết


Sau khi môi trường phát triển của bạn được cấu hình đúng cách, quá trình đóng góp ý nghĩa sẽ bắt đầu bằng việc tải xuống hoặc sao chép kho lưu trữ đã phân nhánh vào máy cục bộ của bạn. Bạn có thể thực hiện việc này bằng cách tải xuống tệp ZIP chứa nội dung kho lưu trữ hoặc sử dụng chức năng sao chép tích hợp của Visual Studio Code, giúp quy trình làm việc được sắp xếp hợp lý hơn cho quá trình phát triển liên tục. Quá trình sao chép sẽ tạo ra một bản sao cục bộ của kho lưu trữ, được đồng bộ hóa với GitHub fork của bạn, cho phép bạn làm việc ngoại tuyến mà vẫn duy trì khả năng kiểm soát phiên bản.


Khi làm việc với kho lưu trữ cục bộ, bạn có quyền truy cập vào toàn bộ cấu trúc dự án, bao gồm các tệp mã nguồn, tệp cấu hình, tài liệu hướng dẫn và bất kỳ tệp thiết kế phần cứng nào. Hầu hết các dự án phần mềm cơ sở đều sử dụng các ngôn ngữ lập trình như C cho chức năng cốt lõi, với các thành phần bổ sung được viết bằng TypeScript cho giao diện người dùng hoặc Java cho các tiện ích cụ thể. Việc hiểu rõ cấu trúc dự án giúp bạn xác định các tệp phù hợp để sửa đổi và đảm bảo rằng các thay đổi của bạn phù hợp với các mẫu kiến trúc và tiêu chuẩn mã hóa của dự án.


Quy trình commit là một khía cạnh cơ bản của kiểm soát phiên bản, đòi hỏi sự chú ý cẩn thận đến cả độ chính xác kỹ thuật và tính rõ ràng trong giao tiếp. Trước khi thực hiện bất kỳ thay đổi nào, bạn nên hiểu rõ mã hiện có và kiểm tra mọi sửa đổi trong môi trường cục bộ của mình. Nguyên tắc cốt lõi của đóng góp mã nguồn mở nhấn mạnh rằng không bao giờ được xuất bản mã chưa được kiểm tra, vì điều này có thể gây ra lỗi hoặc lỗ hổng bảo mật ảnh hưởng đến toàn bộ cộng đồng dự án. Ngoài ra, bạn không bao giờ được commit thông tin nhạy cảm như mật khẩu, mã thông báo API hoặc thông tin đăng nhập cá nhân lên kho lưu trữ công cộng, vì thông tin này sẽ bị truy cập vĩnh viễn bởi bất kỳ ai có quyền truy cập kho lưu trữ.


### Tạo và quản lý yêu cầu kéo


Điểm mấu chốt trong nỗ lực đóng góp của bạn là tạo một yêu cầu kéo, đóng vai trò như một đề xuất chính thức để hợp nhất các thay đổi của bạn vào kho lưu trữ dự án gốc. Quá trình này bắt đầu trong GitHub fork của bạn, nơi bạn có thể xem xét sự khác biệt giữa kho lưu trữ của mình và nguồn gốc. Giao diện của GitHub hiển thị rõ ràng số lượng commit trước hoặc sau, giúp bạn dễ dàng nắm bắt phạm vi các thay đổi được đề xuất. Trước khi tạo yêu cầu kéo, bạn nên đảm bảo fork của mình được đồng bộ hóa với các thay đổi mới nhất từ nguồn gốc để giảm thiểu xung đột tiềm ẩn.


Việc tạo một yêu cầu kéo hiệu quả không chỉ đơn thuần là gửi các thay đổi mã của bạn. Mô tả yêu cầu kéo đóng vai trò là cơ hội để bạn truyền đạt mục đích, phạm vi và tác động của các sửa đổi đến người bảo trì dự án và cộng đồng. Một mô tả được viết tốt sẽ giải thích những vấn đề mà các thay đổi của bạn giải quyết, cách bạn triển khai giải pháp và bất kỳ tác động tiềm ẩn nào đối với các phần khác của dự án. Tài liệu này đặc biệt quan trọng đối với những thay đổi phức tạp mà có thể không dễ dàng nhận thấy ngay lập tức nếu chỉ xem xét sự khác biệt về mã.


Quy trình đánh giá thể hiện khía cạnh hợp tác của phát triển mã nguồn mở, nơi những người bảo trì dự án và những người đóng góp giàu kinh nghiệm cùng đánh giá các thay đổi bạn đề xuất. Bạn có thể yêu cầu những người đánh giá cụ thể, những người có chuyên môn trong lĩnh vực mà các thay đổi của bạn ảnh hưởng, đảm bảo rằng các thành viên cộng đồng am hiểu sẽ xem xét công việc của bạn. Quy trình đánh giá có thể bao gồm nhiều lần lặp lại, với những người đánh giá cung cấp phản hồi, yêu cầu sửa đổi hoặc yêu cầu kiểm tra bổ sung. Quy trình tinh chỉnh hợp tác này giúp duy trì chất lượng mã nguồn đồng thời mang đến những cơ hội học tập quý giá cho những người đóng góp ở mọi cấp độ kinh nghiệm.


Việc hiểu rằng không phải tất cả các yêu cầu kéo đều được chấp nhận giúp thiết lập kỳ vọng phù hợp cho quy trình đóng góp. Người bảo trì dự án có thể từ chối các yêu cầu kéo vì nhiều lý do, bao gồm sự không phù hợp với mục tiêu dự án, kiểm tra chưa đầy đủ, hoặc đã có các giải pháp thay thế đang được phát triển. Thay vì xem việc từ chối là thất bại, hãy coi đó là cơ hội để học hỏi từ phản hồi, tinh chỉnh phương pháp tiếp cận và có khả năng đóng góp các giải pháp thay thế đáp ứng tốt hơn nhu cầu của dự án. Cộng đồng nguồn mở phát triển mạnh mẽ nhờ quy trình lặp đi lặp lại này của việc đề xuất, đánh giá và tinh chỉnh, cuối cùng thúc đẩy các dự án tiến triển thông qua nỗ lực tập thể và chia sẻ chuyên môn.



## Public-Pool là gì?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool đại diện cho một cách tiếp cận mang tính cách mạng đối với Bitcoin mining, giải quyết nhiều vấn đề mà thợ đào gặp phải với các nhóm mining truyền thống. Là một nhóm Bitcoin mining solo hoàn toàn mã nguồn mở, Public Pool thay đổi cơ bản mô hình phân phối phần thưởng mà thợ đào đã quen thuộc. Không giống như các nhóm mining thông thường, nơi người tham gia chia sẻ phần thưởng khi bất kỳ thợ đào nào trong nhóm tìm thấy một khối, Public Pool hoạt động theo nguyên tắc mining solo, trong đó các thợ đào riêng lẻ giữ lại 100% phần thưởng khối của họ khi họ khai thác thành công một khối.


Điểm hấp dẫn nhất của Public Pool là cơ chế không phí. Khi thợ đào tìm thấy một khối thành công bằng Public Pool, họ sẽ nhận được toàn bộ phần thưởng khối cùng với tất cả [phí giao dịch](https://planb.academy/resources/glossary/transaction-fees) liên quan, mà không phải khấu trừ bất kỳ chi phí vận hành nào. Điều này hoàn toàn trái ngược với các pool mining truyền thống, thường tính phí từ 1-3% phần thưởng mining. Mô hình không phí khiến Public Pool đặc biệt hấp dẫn đối với những thợ đào muốn tối đa hóa lợi nhuận tiềm năng trong khi vẫn duy trì toàn quyền kiểm soát hoạt động mining của mình.


Để hiểu vị thế độc đáo của Public Pool, điều quan trọng là phải nắm được sự khác biệt cơ bản giữa mining solo và mining gộp. mining solo thực sự có nghĩa là bạn khai thác độc lập và nhận được phần thưởng khối đầy đủ (hiện tại là 3,125 BTC + phí) nếu bạn tìm thấy một khối, nhưng xác suất tỷ lệ thuận với tỷ lệ băm của bạn so với toàn bộ mạng—tạo ra sự khác biệt cực độ có thể kéo dài hàng tháng hoặc hàng năm giữa các phần thưởng. Các nhóm khai thác truyền thống kết hợp sức mạnh băm để tìm khối thường xuyên hơn, phân phối phần thưởng theo tỷ lệ và cung cấp thu nhập ổn định, có thể dự đoán được. Đối với những thợ đào có vốn đầu tư đáng kể vào phần cứng và chi phí vận hành, mining solo hoàn toàn thường không thực tế bất kể những lợi thế về mặt triết lý của nó—sự khác biệt khiến việc trang trải chi phí điện và thu hồi vốn đầu tư gần như không thể. Thực tế kinh tế này có nghĩa là hầu hết thợ đào sẽ chọn mining gộp vì những lý do tài chính thực tế. Public Pool hoạt động như một pool mining solo, nghĩa là bạn vẫn phải đối mặt với sự khác biệt của mining solo (bạn chỉ được thưởng khi đích thân tìm thấy một khối), nhưng bạn được hưởng lợi từ cơ sở hạ tầng của pool và hoạt động minh bạch, không mất phí.


### Lợi thế của nguồn mở và triển khai kỹ thuật


Cam kết phát triển mã nguồn mở của Public Pool mang lại cho thợ đào sự minh bạch và khả năng kiểm soát chưa từng có đối với hoạt động mining của họ. Toàn bộ cơ sở mã nguồn có sẵn trên GitHub, cho phép thợ đào kiểm tra chính xác cách thức hoạt động của phần mềm, sửa đổi theo nhu cầu của họ và thậm chí đóng góp vào quá trình phát triển. Sự minh bạch này giải quyết một mối lo ngại đáng kể trong cộng đồng mining liên quan đến các cấu hình và hoạt động chưa được biết đến của các nhóm mining truyền thống.


Kiến trúc phần mềm bao gồm cả chức năng nhóm mining cốt lõi và kho lưu trữ giao diện người dùng riêng biệt, cả hai đều có sẵn miễn phí để tải xuống và chỉnh sửa. Thợ đào có thể chạy Nhóm Công khai (Public Pool) ở nhiều cấu hình khác nhau, bao gồm cả container Docker, giúp nó phù hợp với các thiết lập phần cứng và tùy chọn kỹ thuật khác nhau. Tài liệu toàn diện được cung cấp trong kho lưu trữ GitHub cung cấp hướng dẫn cài đặt chi tiết, tùy chọn cấu hình và hướng dẫn chỉnh sửa, giúp thợ đào có trình độ kỹ thuật khác nhau đều có thể sử dụng.


Việc kết nối với Public Pool yêu cầu cấu hình tối thiểu so với thiết lập mining truyền thống. Thợ đào chỉ cần cấu hình thiết bị mining của họ với thông tin kết nối [Stratum](https://planb.academy/resources/glossary/stratum) và cung cấp địa chỉ Bitcoin làm tên người dùng. Có thể thêm tên người dùng tùy chọn sau dấu chấm phân cách cho mục đích tổ chức.


### Đặc điểm cộng đồng và mô hình bền vững


Public Pool tích hợp nhiều tính năng cải tiến giúp củng cố cộng đồng Bitcoin mining trong khi vẫn duy trì hoạt động không thu phí. Nền tảng này hiển thị số liệu thống kê toàn diện, bao gồm tổng hashrate của các thợ đào được kết nối, thường dao động từ 1 đến 2 PetaHash mỗi giây vào năm 2024 và khoảng 40 PH/giây vào tháng 11 năm 2025, đồng thời cung cấp thông tin chi tiết về các thiết bị mining được kết nối. Đặc biệt đáng chú ý là nền tảng này tập trung vào phần cứng mining nguồn mở, với các thiết bị được đánh dấu bằng sao cho biết thiết kế hoàn toàn nguồn mở, kèm theo liên kết đến kho lưu trữ GitHub tương ứng.


Tính bền vững của hoạt động không phí của Public Pool phụ thuộc vào chương trình liên kết sáng tạo với các nhà cung cấp phần cứng mining. Khi thợ đào mua thiết bị từ các công ty đối tác bằng mã giảm giá "SOLO", năm mươi phần trăm thu nhập từ chương trình liên kết sẽ hỗ trợ chi phí vận hành của Public Pool, trong khi năm mươi phần trăm còn lại được phân phối dưới dạng phần thưởng cho những thợ đào đạt được mức độ khó cao nhất mỗi tháng. Mô hình này tạo ra một mối quan hệ cộng sinh, trong đó thợ đào được giảm giá khi mua thiết bị, nhà cung cấp có được khách hàng, và Public Pool duy trì hoạt động mà không tính phí trực tiếp.


### Triết lý phi tập trung và các phương pháp hay nhất


Mặc dù Public Pool cung cấp một giải pháp thay thế tuyệt vời cho các pool mining truyền thống, điều quan trọng là phải hiểu vai trò của nó trong bối cảnh rộng hơn của mô hình phi tập trung Bitcoin. Nền tảng này đóng vai trò là bước đệm hướng tới mục tiêu cuối cùng của các thợ đào cá nhân vận hành pool mining của riêng họ. Việc vận hành pool mining của riêng bạn thể hiện mức độ phi tập trung cao nhất, vì nó loại bỏ sự phụ thuộc vào bất kỳ cơ sở hạ tầng hoặc phần mềm của bên thứ ba nào, bất kể bên thứ ba đó có minh bạch hay có thiện chí đến đâu.


Bản chất mã nguồn mở của Public Pool khiến nó trở thành một nền tảng học tập lý tưởng cho những thợ đào muốn tìm hiểu hoạt động của pool trước khi triển khai giải pháp của riêng họ. Việc cung cấp hướng dẫn cài đặt cho nhiều hệ điều hành và tài liệu toàn diện cung cấp cho thợ đào kiến thức cần thiết để chuyển đổi từ việc sử dụng Public Pool sang vận hành cơ sở hạ tầng mining của riêng họ. Khía cạnh giáo dục này phù hợp với các nguyên tắc cơ bản của Bitcoin về chủ quyền tự chủ và phi tập trung, trao quyền cho từng thợ đào kiểm soát hoàn toàn hoạt động mining của họ, đồng thời đóng góp vào bảo mật và phi tập trung tổng thể của mạng lưới Bitcoin.


Giao diện người dùng của nền tảng cung cấp cho thợ đào khả năng giám sát chi tiết, bao gồm trạng thái công nhân, thống kê tỷ lệ băm và số liệu hiệu suất. Các tính năng này giúp thợ đào tối ưu hóa hoạt động, đồng thời tìm hiểu về các nguyên tắc quản lý nhóm mà sau này họ có thể áp dụng cho việc triển khai nhóm mining của riêng mình.


## Cách cài đặt Public-Pool trên Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Việc vận hành hồ bơi Bitcoin mining tại nhà ngày càng dễ dàng hơn nhờ phần cứng hiện đại và các giải pháp phần mềm đơn giản. Chương này sẽ khám phá việc triển khai thực tế một hồ bơi công cộng tại nhà bằng phần cứng mini PC giá cả phải chăng và phần mềm quản lý [node](https://planb.academy/resources/glossary/node) hợp lý. Đến cuối hướng dẫn này, bạn sẽ hiểu các yêu cầu về phần cứng, quy trình thiết lập phần mềm và cấu hình cơ bản cần thiết để thiết lập cơ sở hạ tầng hồ bơi mining của riêng mình.


### Yêu cầu phần cứng và thiết lập


Nền tảng của bất kỳ hệ thống pool mining gia đình nào đều bắt đầu bằng việc lựa chọn phần cứng phù hợp, cân bằng giữa hiệu suất, chi phí và hiệu quả năng lượng. Một máy tính mini là giải pháp lý tưởng cho ứng dụng này, cung cấp đủ sức mạnh xử lý trong khi vẫn duy trì kích thước nhỏ gọn và mức tiêu thụ điện năng hợp lý. Cấu hình được đề xuất bao gồm bộ xử lý Intel N100, cung cấp đủ tài nguyên tính toán cho hoạt động của pool, kết hợp với ít nhất một terabyte bộ nhớ NVMe để lưu trữ [blockchain](https://planb.academy/resources/glossary/blockchain) Bitcoin và dữ liệu liên quan.


Yêu cầu lưu trữ đặc biệt quan trọng vì việc vận hành một nhóm mining đòi hỏi phải duy trì một nút Bitcoin được đồng bộ hóa hoàn toàn. Ổ đĩa NVMe dung lượng một terabyte đảm bảo các thao tác đọc/ghi nhanh chóng, thiết yếu cho việc đồng bộ hóa blockchain và xử lý [giao dịch](https://planb.academy/resources/glossary/transaction-tx) đang diễn ra. Ngoài ra, việc phân bổ RAM đầy đủ hỗ trợ hoạt động trơn tru của cả hệ điều hành Linux cơ bản và phần mềm quản lý nút sẽ điều phối các hoạt động của nhóm.


### Kiến trúc phần mềm và quản lý nút


Bộ phần mềm cho nhóm mining tại nhà được xây dựng trên nền tảng Linux, mang lại sự ổn định và bảo mật cần thiết cho hoạt động của Bitcoin. Trên nền tảng hệ thống cơ sở này, phần mềm quản lý nút chuyên dụng như Umbrel tạo ra một giao diện trực quan để quản lý cơ sở hạ tầng Bitcoin. Phương pháp này loại bỏ phần lớn sự phức tạp thường gặp khi vận hành các nút Bitcoin, giúp người dùng không cần kiến thức chuyên sâu về kỹ thuật cũng có thể vận hành nhóm.


Umbrel hoạt động như một nền tảng quản lý node toàn diện, xử lý việc cài đặt, đồng bộ hóa và bảo trì liên tục [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core) thông qua giao diện web. Mô hình cửa hàng ứng dụng của nền tảng cho phép dễ dàng cài đặt các dịch vụ bổ sung, bao gồm phần mềm nhóm mining, chỉ bằng các thao tác trỏ và nhấp chuột đơn giản. Kiến trúc này đảm bảo người dùng có thể tập trung vào việc vận hành nhóm thay vì quản trị hệ thống, đồng thời vẫn duy trì toàn quyền kiểm soát cơ sở hạ tầng Bitcoin của mình.


### Cài đặt và cấu hình hồ bơi công cộng


Việc cài đặt phần mềm pool công cộng thông qua nền tảng Umbrel cho thấy tính hợp lý của việc triển khai cơ sở hạ tầng Bitcoin hiện đại. Quá trình bắt đầu bằng việc truy cập cửa hàng ứng dụng Umbrel thông qua giao diện web, nơi chỉ cần tìm kiếm "public pool" là bạn sẽ thấy phần mềm pool mining khả dụng. Việc cài đặt chỉ cần vài cú nhấp chuột: chọn ứng dụng, xác nhận cài đặt và chờ quá trình thiết lập tự động hoàn tất.


Quá trình cài đặt sẽ tự động cấu hình các kết nối cần thiết giữa phần mềm nhóm công cộng và nút Bitcoin cơ bản. Sự tích hợp này đảm bảo nhóm có thể xác thực giao dịch, xây dựng mẫu khối và phân phối công việc cho các thợ đào được kết nối mà không cần cấu hình thủ công các tham số mạng phức tạp. Sau khi cài đặt hoàn tất, giao diện nhóm có thể truy cập ngay lập tức thông qua mạng cục bộ, cung cấp khả năng giám sát và quản lý theo thời gian thực.


### Kết nối thợ đào và cân nhắc mạng lưới


Việc kết nối phần cứng mining với nhóm mới thành lập của bạn yêu cầu cấu hình cài đặt nhóm thợ đào để trỏ đến cơ sở hạ tầng cục bộ của bạn. Việc này bao gồm việc thay thế địa chỉ nhóm mặc định bằng địa chỉ IP cục bộ của bạn và số cổng thích hợp được chỉ định trong quá trình cài đặt nhóm công cộng. Việc thay đổi cấu hình sẽ chuyển hướng các hoạt động tính toán của phần cứng mining từ các nhóm bên ngoài sang cơ sở hạ tầng tại nhà, cho phép bạn duy trì toàn quyền kiểm soát hoạt động của mining và các phần thưởng tiềm năng.


Cấu hình mạng đóng vai trò quan trọng trong khả năng truy cập và chức năng của nhóm. Thiết lập mạng cục bộ thường bao gồm địa chỉ IP tiêu chuẩn, nhưng người dùng có thể gặp phải sự khác biệt trong việc phân giải DNS tùy thuộc vào cấu hình bộ định tuyến của họ. Một số bộ định tuyến cung cấp dịch vụ DNS cục bộ tạo tên miền thân thiện cho các dịch vụ cục bộ, trong khi một số khác yêu cầu truy cập địa chỉ IP trực tiếp. Để có khả năng truy cập rộng hơn ngoài mạng cục bộ, có thể cần cấu hình chuyển tiếp cổng trên bộ định tuyến, mặc dù điều này đi kèm với các cân nhắc bảo mật bổ sung đòi hỏi phải đánh giá cẩn thận các rủi ro và lợi ích liên quan.


Việc thành lập thành công nhóm mining tại nhà là một bước tiến quan trọng hướng tới cơ sở hạ tầng Bitcoin phi tập trung, mang lại cả giá trị giáo dục và khả năng thực tế của mining đồng thời vẫn duy trì quyền kiểm soát hoàn toàn đối với hoạt động Bitcoin của bạn.


# Lắp ráp phần cứng và khắc phục sự cố

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Sử dụng công cụ nào?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

Trong lĩnh vực hàn linh kiện gắn trên bề mặt (SMD), đặc biệt là khi làm việc với các dự án Bitaxe, việc có đúng công cụ sẽ tạo nên sự khác biệt giữa thất bại và thành công. Hướng dẫn toàn diện này bao gồm các thiết bị thiết yếu cần thiết để thực hiện các dự án hàn SMD hiệu quả, từ các dụng cụ cầm tay cơ bản đến các thiết bị chuyên dụng giúp nâng cao khả năng hàn của bạn.


Nếu bạn muốn tham khảo một số tài liệu về sơ đồ, hãy kiểm tra [kho GitHub](https://github.com/skot/bitaxe-doc/tree/main).


### Dụng cụ cầm tay cơ bản và dụng cụ chính xác


Nền tảng của bất kỳ thiết lập hàn SMD nào cũng bắt đầu bằng nhíp chất lượng, đóng vai trò là công cụ chính để gắn linh kiện. Hai loại nhíp tỏ ra hữu ích nhất trong công việc này: nhíp đầu thẳng tiêu chuẩn và nhíp đầu cong nhẹ. Loại đầu thẳng có thể xử lý hầu hết các linh kiện SMD thường thấy trong bộ dụng cụ Bitaxe thông thường, trong khi nhíp đầu cong lại rất phù hợp khi làm việc với các linh kiện cực nhỏ đòi hỏi vị trí chính xác. Những dụng cụ này thường được bán kèm với các bộ dụng cụ sửa chữa, chẳng hạn như bộ dụng cụ iFixit được thiết kế để sửa chữa điện thoại, giúp chúng dễ dàng tiếp cận với hầu hết những người yêu thích công nghệ.


Bên cạnh nhíp, một chiếc kéo tốt cũng là vật dụng không thể thiếu để cắt băng keo điện, một vật dụng đa năng trong các dự án điện tử. Băng keo điện cung cấp khả năng cách điện thiết yếu cho dây cáp và linh kiện, và việc có sẵn băng keo chất lượng cao giúp đơn giản hóa quy trình hàn. Những vật dụng cơ bản này có thể được tìm mua tại các cửa hàng phần cứng hoặc các nhà bán lẻ trực tuyến mà không cần đến các nhà cung cấp thiết bị điện tử chuyên dụng.


### Ứng dụng và quản lý kem hàn


Việc sử dụng kem hàn là một trong những khía cạnh quan trọng nhất của hàn SMD, và dụng cụ phù hợp sẽ giúp quá trình này vừa chính xác vừa thú vị. Những ống tiêm nhỏ, không sắc nhọn chứa kem hàn mang lại khả năng kiểm soát tuyệt vời việc đặt kem hàn. Phương pháp này cho phép sử dụng chính xác lượng kem hàn cần thiết cho mỗi mối hàn, và hầu hết mọi người đều nhanh chóng phát triển kỹ thuật phù hợp để kiểm soát áp suất và lưu lượng thông qua thực hành.


Bản thân việc lựa chọn kem hàn ảnh hưởng đáng kể đến thành công của quá trình hàn. ChipQuik TS391SNL50 nổi bật là một loại kem hàn đặc biệt cho các dự án Bitaxe và công việc hàn SMD nói chung. Kem hàn này duy trì độ đặc và đặc tính nóng chảy thích hợp, tránh được các vấn đề thường gặp ở các loại kem hàn rẻ tiền hơn có điểm nóng chảy quá thấp. Kem hàn chất lượng thấp có thể gây ra các vấn đề như mối hàn trước đó bị chảy trở lại khi gia nhiệt các vùng lân cận, dẫn đến linh kiện bị dịch chuyển và kết nối kém. Mặc dù kem hàn chất lượng cao đòi hỏi đầu tư ban đầu cao hơn, nhưng kết quả cải thiện và giảm thiểu sự khó chịu hoàn toàn xứng đáng với chi phí bỏ ra.


### Công cụ giải quyết vấn đề và dọn dẹp


Ngay cả thợ hàn giàu kinh nghiệm cũng gặp phải những vấn đề cần khắc phục, khiến thiết bị hút hàn trở nên thiết yếu trong bất kỳ bộ dụng cụ hoàn chỉnh nào. Một giàn hút hàn, về cơ bản là một dụng cụ hút chân không được gia nhiệt, giúp loại bỏ lượng hàn thừa và sửa chữa các kết nối cầu nối giữa các chân linh kiện. Những dụng cụ này hoạt động hiệu quả nhất khi kết hợp với dung dịch trợ dung, giúp cải thiện dòng chảy của chất hàn và giúp quá trình hút hàn diễn ra hiệu quả hơn.


Chất trợ dung có nhiều dạng, bao gồm dạng rắn và dạng lỏng, và có nhiều công dụng khác nhau, ngoài việc hỗ trợ tháo mối hàn. Khi kem hàn bắt đầu mất hiệu quả sau thời gian dài làm việc, việc bổ sung chất trợ dung sẽ khôi phục lại đặc tính chảy thích hợp và đảm bảo kết nối đáng tin cậy. Một dụng cụ nhỏ hình thìa, thường thấy trong bộ dụng cụ sửa chữa chính xác, giúp bôi chất trợ dung chính xác vào các khu vực cụ thể mà không làm nhiễm bẩn các linh kiện xung quanh.


Vệ sinh bo mạch là bước cuối cùng trong quy trình làm việc chuyên nghiệp, đòi hỏi phải có cồn isopropanol và bàn chải chuyên dụng. Một bàn chải đánh răng cũ là lựa chọn hoàn hảo cho mục đích này, và một chai bóp chứa isopropanol cho phép kiểm soát lượng dung dịch vệ sinh. Sự kết hợp này loại bỏ cặn thuốc hàn và cặn keo, mang lại cho bo mạch vẻ ngoài sạch sẽ, chuyên nghiệp, đồng thời giúp kiểm tra các mối hàn dễ dàng hơn.


### Thiết bị chuyên dụng và công cụ tiên tiến


Đối với các dự án liên quan đến mạch tích hợp phức tạp, đặc biệt là ASIC, khuôn in chuyển đổi quy trình hàn từ việc đặt tay thủ công tẻ nhạt sang việc dán keo hiệu quả và chính xác. Những khuôn in được cắt chính xác này đảm bảo độ dày và vị trí dán keo đồng đều, giảm đáng kể thời gian cần thiết cho các linh kiện phức tạp đồng thời cải thiện độ tin cậy. Việc đầu tư vào khuôn in chất lượng mang lại lợi ích về cả tiết kiệm thời gian lẫn cải thiện kết quả.


Quản lý nhiệt trở nên rất quan trọng khi làm việc với các linh kiện điện, vì vậy keo tản nhiệt hoặc mỡ tản nhiệt là những vật dụng thiết yếu. Những vật liệu này đảm bảo truyền nhiệt chính xác giữa bộ tản nhiệt và mạch tích hợp, ngăn ngừa hư hỏng do nhiệt và đảm bảo hoạt động đáng tin cậy. Vật liệu giao diện nhiệt chất lượng cao chỉ là một khoản đầu tư nhỏ nhưng lại bảo vệ được các linh kiện đắt tiền hơn nhiều.


Trọng tâm của bất kỳ hệ thống hàn SMD nào là trạm hàn khí nóng, cung cấp nhiệt lượng được kiểm soát cần thiết cho công việc gắn trên bề mặt. Mặc dù các trạm hàn giá rẻ trong khoảng 30-50 đô la có thể hoạt động tốt, nhưng chúng thường thiếu độ tin cậy và độ chính xác của các thiết bị cao cấp hơn. Các trạm hàn cấp thấp này thường hoạt động hiệu quả ở 355°C và có chức năng tự động giảm nhiệt độ khi tay cầm được lắp lại vào giá đỡ. Tuy nhiên, độ tin cậy của chúng có thể không ổn định, với một số thiết bị bị hỏng sớm. Đối với công việc nghiêm túc, việc đầu tư vào thiết bị chất lượng cao hơn từ các nhà cung cấp thiết bị điện tử chuyên dụng sẽ mang lại giá trị lâu dài tốt hơn nhờ độ tin cậy được cải thiện và khả năng kiểm soát nhiệt độ chính xác hơn.


Sự kết hợp của các công cụ này tạo nên khả năng hàn SMD hoàn chỉnh, vượt xa các dự án Bitaxe và cả công việc điện tử nói chung. Hiểu rõ vai trò của từng công cụ và lựa chọn thiết bị chất lượng phù hợp với trình độ kỹ năng và yêu cầu dự án của bạn sẽ đảm bảo kết quả hàn thành công và trải nghiệm hàn thú vị.



## Sửa lỗi hàn

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Bộ thu phát Bitaxe đặt ra những thách thức đặc biệt trong quá trình lắp ráp, đòi hỏi sự chú ý cẩn thận đến hướng linh kiện, ngăn ngừa cầu hàn và quản lý nhiệt độ phù hợp. Việc hiểu rõ những vấn đề thường gặp này và giải pháp khắc phục là rất cần thiết để chế tạo thành công bộ linh kiện và tránh hư hỏng linh kiện tốn kém. Chương này xem xét các vấn đề hàn thường gặp nhất trong quá trình lắp ráp Bitaxe và cung cấp các kỹ thuật thực tế để xác định và giải quyết chúng.


### Định hướng và nhận dạng thành phần


Định hướng linh kiện đúng là một trong những yếu tố quan trọng nhất để lắp ráp Bitaxe thành công, đặc biệt là với MOSFET Q1 và Q2. Các linh kiện này có các điểm đánh dấu định hướng đặc biệt cần được quan sát cẩn thận trong quá trình lắp đặt. Mỗi MOSFET có một dấu chấm nhỏ tương ứng với vị trí sắp xếp các miếng đệm cụ thể trên bảng mạch. Chìa khóa để định hướng chính xác nằm ở việc hiểu cấu trúc vật lý của các linh kiện này, với bốn chân được sắp xếp với một miếng đệm lớn và ba miếng đệm nhỏ hơn không kết nối với miếng đệm lớn.


Khi lắp đặt Q1 và Q2, hãy kiểm tra kỹ lưỡng cả linh kiện và bảng mạch. Sơ đồ mạch thể hiện rõ hướng dự định thông qua cấu hình pad, với bốn chân được bố trí khớp với cấu trúc MOSFET. Trước khi hàn bất kỳ linh kiện lớn nào, hãy luôn kiểm tra hướng bằng cách so sánh các dấu hiệu vật lý của linh kiện với cách bố trí pad của bảng mạch. Bước kiểm tra đơn giản này giúp tránh tình trạng phải tháo hàn và lắp lại các linh kiện bị định hướng sai.


Hậu quả của việc định hướng sai không chỉ giới hạn ở các vấn đề chức năng đơn thuần. MOSFET định hướng sai có thể gây ra các sự cố mạch điện khó chẩn đoán và có thể cần phải thay thế toàn bộ linh kiện. Việc dành thời gian xác minh định hướng trước khi gia nhiệt sẽ đảm bảo mạch hoạt động bình thường và ngăn ngừa việc khắc phục sự cố không cần thiết sau này trong quá trình lắp ráp.


### Quản lý cầu hàn và hàn dư


Cầu hàn là một thách thức phổ biến khác trong lắp ráp Bitaxe, đặc biệt là xung quanh các linh kiện có bước chân nhỏ như U10. Những kết nối không mong muốn này giữa các chân liền kề có thể gây ra trục trặc mạch và đòi hỏi kỹ thuật tháo lắp cẩn thận. Phương pháp hiệu quả nhất là sử dụng bấc hút hàn, một vật liệu bện bằng đồng có khả năng hấp thụ lượng hàn thừa khi được làm nóng. Kỹ thuật này đòi hỏi sự kiên nhẫn và lựa chọn dụng cụ phù hợp để tránh làm hỏng các linh kiện mỏng manh.


Khi xử lý cầu hàn trên mạch tích hợp, hãy sử dụng giá đỡ PCB hoặc kẹp khớp nối để giữ chặt linh kiện trong khi làm việc. Làm nóng nhẹ vùng bị ảnh hưởng và cẩn thận kéo bấc hàn qua các kết nối cầu nối. Bện đồng sẽ tự động hấp thụ lượng hàn thừa, tách các kết nối không mong muốn. Quá trình này có thể cần nhiều lần thử, nhưng nếu kiên trì, các kết nối sẽ sạch và tách biệt đúng cách.


Phòng ngừa vẫn là cách tốt nhất để quản lý cầu hàn. Sử dụng lượng kem hàn vừa đủ và giữ tay ổn định trong quá trình lắp ráp linh kiện sẽ giúp giảm đáng kể hiện tượng cầu hàn. Khi cầu hàn xuất hiện, hãy xử lý ngay lập tức thay vì hy vọng chúng sẽ không ảnh hưởng đến hoạt động của mạch. Ngay cả những cầu hàn tưởng chừng nhỏ cũng có thể gây ra các vấn đề chức năng nghiêm trọng, khó chẩn đoán sau khi bo mạch đã được lắp ráp hoàn chỉnh.


### Các thành phần quan trọng và những cân nhắc đặc biệt


Bộ chuyển đổi buck U9 đáng được đặc biệt chú ý do vai trò quan trọng của nó trong việc chuyển đổi 5 volt sang 1,2 volt cho chip ASIC. Linh kiện này đặt ra những thách thức đặc biệt do năm kết nối nhỏ và dễ hỏng. Việc lắp đặt đúng cách đòi hỏi phải bôi kem hàn chính xác và quản lý nhiệt cẩn thận. Kem hàn không đủ bên dưới U9 có thể dẫn đến kết nối kém, ngăn cản việc chuyển đổi điện áp đúng cách, trong khi kem hàn dư thừa có thể tạo ra cầu nối gây ra sự cố mạch.


U9 tạo ra các tín hiệu âm thanh đặc trưng khi gặp sự cố cầu hàn, tạo ra tiếng ồn tần số cao khác với hoạt động bình thường của ASIC. Kỹ thuật chẩn đoán bằng thính giác này có thể giúp xác định sự cố, mặc dù đòi hỏi khả năng nghe tần số cao tốt để phát hiện. Khi không thể chẩn đoán bằng âm thanh, việc kiểm tra bằng mắt thường là rất cần thiết. Hãy kiểm tra kỹ lưỡng tất cả các kết nối, tìm kiếm cầu hàn hoặc vùng phủ hàn không đủ.


Nếu U9 không cung cấp đủ điện áp 1,2 volt cần thiết mặc dù có vẻ đã được hàn đúng cách, hãy cân nhắc nguyên nhân có thể là do thiếu kem hàn. Tháo linh kiện ra, bôi thêm một lượng nhỏ kem hàn và lắp lại. Trong trường hợp các chân cắm riêng lẻ không được phủ đủ kem hàn, hãy cẩn thận bôi một lượng nhỏ kem hàn vào các vị trí cụ thể bằng nhíp. Kem hàn sẽ tự động chảy xuống dưới linh kiện khi được làm nóng, tạo ra các kết nối thích hợp thông qua hiện tượng mao dẫn.


### Quản lý nhiệt và bảo vệ linh kiện


Quản lý nhiệt đúng cách bảo vệ các linh kiện nhạy cảm khỏi hư hỏng do nhiệt, đồng thời đảm bảo mối hàn chắc chắn. Các linh kiện như bộ dao động tinh thể Y1 và U1 đặc biệt nhạy cảm với nhiệt độ cao trong thời gian dài và cần được kiểm soát nhiệt độ cẩn thận. Duy trì nhiệt độ mỏ hàn ở mức 350 độ C, nhưng giảm thiểu thời gian gia nhiệt để tránh hư hỏng linh kiện. Kỹ thuật hàn nhanh chóng và hiệu quả sẽ bảo vệ các linh kiện nhạy cảm này đồng thời đạt được kết nối đáng tin cậy.


Chip ASIC đòi hỏi kỹ thuật xử lý đặc biệt do cấu trúc chân cắm phức tạp và nhạy cảm với ứng suất cơ học. Khi sử dụng khuôn in để bôi kem hàn, hãy đảm bảo phủ đều kem hàn lên tất cả các chân để tránh tình trạng linh kiện lắp ráp không đều. Nếu kem hàn quá nhiều khiến ASIC lắp ráp không đều, hãy để cụm chip nguội hoàn toàn trước khi thực hiện các điều chỉnh. Trong khi gia nhiệt, chỉ ấn nhẹ vào các cạnh được dán nhãn của linh kiện, tuyệt đối không ấn vào vùng trung tâm của khuôn để đạt được vị trí lắp ráp chính xác.


Linh kiện U8 mang đến những thách thức đặc biệt do số lượng chân cắm lớn và khả năng bị cong chân. Khi chân cắm bị cong trong quá trình xử lý, hãy sử dụng giá đỡ PCB hoặc kẹp khớp nối để cố định linh kiện và cẩn thận nắn thẳng các chân cắm bị ảnh hưởng. Thao tác chậm rãi và kiên nhẫn để tránh làm gãy các chân cắm mỏng manh. Hiểu rằng một số nhóm chân cắm trên U8 được kết nối nội bộ có thể giúp đơn giản hóa việc khắc phục sự cố, vì các cầu nối giữa các chân cắm cụ thể này không ảnh hưởng đến hoạt động của mạch. Tuy nhiên, các cầu nối giữa các chân cắm khác cần được tháo ra cẩn thận để đảm bảo hoạt động bình thường.


## Cách gỡ lỗi Bitaxe của bạn bằng AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Khi làm việc với các thiết bị Bitaxe mining, lỗi phần cứng có thể biểu hiện theo nhiều cách khác nhau mà có thể không dễ nhận biết ngay lập tức. Việc hiểu cách chẩn đoán các sự cố này một cách có hệ thống bằng hệ điều hành AxeOS có thể tiết kiệm đáng kể thời gian và ngăn ngừa việc thay thế linh kiện không cần thiết. Chương này khám phá các kỹ thuật chẩn đoán và phương pháp xử lý sự cố mà các kỹ thuật viên giàu kinh nghiệm sử dụng để xác định các sự cố phần cứng cụ thể thông qua phân tích phần mềm.


### Hiểu về các chỉ số tiêu thụ điện năng


Chỉ báo chẩn đoán đầu tiên và quan trọng nhất trong AxeOS là theo dõi mức tiêu thụ điện năng. Các thiết bị Bitaxe thông thường, bao gồm các mẫu Bitaxe Ultra và Bitaxe Supra, thường tiêu thụ từ 10 đến 17 watt trong quá trình hoạt động tiêu chuẩn. Phép đo cơ sở này đóng vai trò là chỉ báo sức khỏe chính cho toàn bộ hệ thống. Khi mức tiêu thụ điện năng giảm đáng kể xuống dưới phạm vi này, đặc biệt là dưới 3 watt, điều này báo hiệu sự cố cơ bản với chip ASIC hoặc mạch hỗ trợ của nó.


Các trường hợp tiêu thụ điện năng thấp cần được xử lý ngay lập tức vì chúng cho thấy chip mining hoàn toàn không hoạt động hoặc đang hoạt động ở trạng thái xuống cấp nghiêm trọng. Chỉ riêng phép đo này có thể giúp bạn nhanh chóng phân biệt giữa các vấn đề về hiệu suất và lỗi phần cứng hoàn toàn. Việc đọc công suất trong AxeOS cung cấp phản hồi theo thời gian thực, cho phép bạn theo dõi hiệu quả của bất kỳ nỗ lực sửa chữa nào bạn thực hiện cho thiết bị.


### Phân tích phép đo điện áp ASIC


Tính năng đo điện áp ASIC trong AxeOS cung cấp thông tin chẩn đoán quan trọng giúp xác định chính xác bản chất của sự cố phần cứng. Khi kiểm tra các chỉ số điện áp, bạn cần hiểu mối quan hệ giữa điện áp đo được và điện áp yêu cầu để chẩn đoán chính xác sự cố. Hệ thống hiển thị cả điện áp được cung cấp cho chip ASIC và điện áp mà chip yêu cầu từ hệ thống quản lý nguồn.


Khi bạn quan sát thấy điện áp ASIC đo được chính xác là 1,2 vôn kết hợp với mức tiêu thụ điện năng dưới 3 watt, sự kết hợp cụ thể này cho thấy chip ASIC có vấn đề về hàn hoặc chip ASIC đã bị hỏng hoàn toàn. Điện áp này cho thấy nguồn điện đang đến vị trí chip, nhưng bản thân chip không hoạt động bình thường. Kiểm tra vật lý chip ASIC có thể phát hiện các vết nứt hoặc hư hỏng nhìn thấy được khác, giải thích cho kiểu hành vi này.


Một kịch bản chẩn đoán khác xuất hiện khi bạn thấy mức tiêu thụ điện năng thấp kết hợp với các chỉ số điện áp yêu cầu rất thấp, chẳng hạn như 100 milivôn hoặc 0,5 vôn. Mẫu này cho thấy chip ASIC không được cung cấp đủ điện áp, thường là do sự cố với linh kiện bộ chuyển đổi buck U9. Bộ chuyển đổi buck chịu trách nhiệm cung cấp điện áp chính xác mà chip ASIC cần để hoạt động bình thường.


### Giải thích Dữ liệu Nhật ký và Giao tiếp ASIC


Hệ thống ghi nhật ký AxeOS cung cấp thông tin chi tiết có giá trị về việc chip ASIC của bạn có đang giao tiếp với hệ thống điều khiển hay không. Khi bạn truy cập nhật ký thông qua chức năng "hiển thị nhật ký", sự hiện diện của các mục "Kết quả ASIC" xác nhận rằng chip không chỉ được cấp nguồn mà còn đang xử lý công việc và trả về kết quả. Giao tiếp này cho biết ASIC đã được hàn đúng cách và duy trì kết nối với mạch điều khiển.


Việc không có lỗi ASIC trong nhật ký, đặc biệt khi kết hợp với các triệu chứng khác, giúp thu hẹp vấn đề xuống các thành phần cụ thể hoặc sự cố kết nối. Phương pháp chẩn đoán này cho phép bạn phân biệt giữa các chip hoàn toàn không phản hồi và các chip có thể gặp sự cố kết nối không liên tục. Phân tích nhật ký trở nên đặc biệt hữu ích khi khắc phục sự cố phức tạp, trong đó nhiều triệu chứng có thể gợi ý các nguyên nhân gốc rễ khác nhau.


### Phương pháp khắc phục sự cố có hệ thống


Khi chẩn đoán sự cố phần cứng Bitaxe, việc áp dụng phương pháp tiếp cận có hệ thống giúp tránh bỏ sót các vấn đề nghiêm trọng và đảm bảo quy trình sửa chữa hiệu quả. Bắt đầu bằng việc ghi lại mức tiêu thụ điện năng và điện áp, sau đó đối chiếu các phép đo này với dữ liệu nhật ký để xây dựng bức tranh toàn cảnh về hoạt động của hệ thống. Phương pháp tiếp cận có hệ thống này giúp xác định liệu sự cố bắt nguồn từ chính chip ASIC, hệ thống cung cấp điện hay đường dẫn truyền thông tin giữa các thành phần.


Trong trường hợp bộ chuyển đổi buck U9 có vẻ là vấn đề, có thể cần kiểm tra vật lý và hàn lại. Linh kiện U9 đặc biệt dễ gặp sự cố hàn, đặc biệt là trong các trường hợp lắp ráp lần đầu. Khi nghi ngờ có vấn đề về điều chỉnh điện áp, việc sử dụng đồng hồ vạn năng để xác minh rằng 1,2 vôn thực sự có ở các chân ASIC sẽ giúp xác nhận chắc chắn các vấn đề về cung cấp điện. Nếu có điện áp ở các chân nhưng ASIC vẫn không hoạt động và kiểm tra vật lý không phát hiện hư hỏng, thì việc thay thế chip ASIC là bước hợp lý tiếp theo. Nếu sự cố vẫn tiếp diễn ngay cả sau khi thay thế ASIC, linh kiện U2, bộ điều khiển chip ASIC, có thể cần được xử lý như là thành phần cuối cùng trong trình tự khắc phục sự cố.


## Làm thế nào để gỡ lỗi bằng USB?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Khi xử lý sự cố thiết bị Bitaxe mining, việc truy cập trực tiếp vào hệ thống ghi nhật ký nội bộ của thiết bị sẽ mang lại những thông tin chi tiết vô giá mà giao diện web không thể cung cấp. Chương này sẽ tìm hiểu cách thiết lập kết nối nối tiếp USB trực tiếp với thiết bị Bitaxe của bạn bằng nền tảng ESP-IDF, cho phép giám sát nhật ký hệ thống, trình tự khởi động và thông báo lỗi theo thời gian thực. Phương pháp gỡ lỗi này đặc biệt quan trọng khi xử lý các thiết bị thường xuyên khởi động lại hoặc gặp sự cố phần cứng, vì nó ghi lại tất cả thông tin chẩn đoán có thể bị mất trong quá trình khởi động lại hệ thống.


Quá trình gỡ lỗi yêu cầu Visual Studio Code với phần mở rộng ESP-IDF, mặc dù có thể sử dụng bất kỳ IDE tương thích nào. Phương pháp này hoạt động với tất cả các biến thể Bitaxe có cổng USB, bao gồm Bitaxe Ultra 204 và các mẫu khác trong cùng dòng. Kết nối nối tiếp trực tiếp bỏ qua các hạn chế tiềm ẩn của giao diện web và cung cấp quyền truy cập không bị lọc vào thông tin trạng thái bên trong của thiết bị.


### Thiết lập truyền thông nối tiếp


Việc thiết lập giao tiếp với thiết bị Bitaxe của bạn bắt đầu bằng việc kết nối cáp USB và mở terminal ESP-IDF trong môi trường phát triển. Lệnh `idf.py monitor` sẽ khởi tạo quá trình kết nối, tự động quét các cổng COM khả dụng để thiết lập giao tiếp UART với chip ESP32 trên thiết bị Bitaxe. Hệ thống thường sẽ tuần hoàn qua các cổng khả dụng (COM3, COM4, COM16, v.v.) cho đến khi tìm thấy kết nối chính xác.


Sau khi kết nối, thiết bị đầu cuối sẽ hiển thị toàn bộ trình tự khởi động và nhật ký hoạt động đang diễn ra. Quá trình kết nối ban đầu có thể mất vài phút để hệ thống xác định đúng cổng giao tiếp. Nếu tính năng tự động phát hiện cổng không thành công, bạn có thể chỉ định thủ công cổng COM thông qua giao diện chọn cổng của IDE. Kênh giao tiếp trực tiếp này vẫn hoạt động trong suốt quá trình hoạt động của thiết bị, cung cấp quyền truy cập liên tục vào các thông tin chẩn đoán hệ thống và số liệu hiệu suất.


### Giải thích trình tự khởi động và nhật ký hoạt động bình thường


Trình tự khởi động cung cấp thông tin quan trọng về cấu hình phần cứng và quá trình khởi tạo thiết bị Bitaxe của bạn. Nhật ký khởi động thông thường bắt đầu bằng thông tin phiên bản ESP-IDF, tiếp theo là thông báo đặc trưng "Welcome to the Bitaxe. Hack the planet" xác nhận việc tải firmware thành công. Sau đó, hệ thống hiển thị cấu hình tần số ASIC, nhận dạng model thiết bị và chi tiết phiên bản bo mạch.


Một thiết bị hoạt động bình thường sẽ hiển thị quá trình khởi tạo I2C thành công và điều chỉnh điện áp ASIC ở mức 1,2 volt. Nhật ký hiển thị thông tin trạng thái GPIO và chuỗi khởi tạo Wi-Fi, tiếp theo là cấu hình máy chủ DHCP và gán địa chỉ IP. Một trong những chỉ báo quan trọng nhất là thông báo phát hiện chip ASIC, thông báo này sẽ báo cáo "đã phát hiện một chip ASIC" cho một thiết bị chỉ có một chip. Xác nhận này xác nhận rằng phần cứng mining đã được kết nối và giao tiếp đúng cách với bộ điều khiển ESP32.


Nhật ký hoạt động cho thấy nhiều tác vụ đồng thời đang chạy trên thiết bị, bao gồm giao tiếp API tầng, phối hợp tác vụ chính, quản lý tác vụ ASIC và xử lý tác vụ tầng. Các mã định danh tác vụ khác nhau này giúp phân tách các vấn đề cho các thành phần hệ thống cụ thể. Hoạt động bình thường bao gồm thiết lập kết nối nhóm, thông báo điều chỉnh độ khó, xếp hàng và hủy xếp hàng tác vụ, và báo cáo tạo nonce. Các tác vụ mining thành công sẽ hiển thị kết quả ASIC kèm theo tính toán độ khó và mining sẽ gửi xác nhận khi số lượng chia sẻ đạt ngưỡng yêu cầu.


### Xác định lỗi phần cứng và các mẫu lỗi


Lỗi phần cứng được thể hiện trong nhật ký thông qua các mẫu lỗi cụ thể, cho biết linh kiện nào đang hoạt động không bình thường. Kiểu lỗi phổ biến nhất liên quan đến lỗi giao tiếp I2C với các mạch tích hợp cụ thể trên bo mạch Bitaxe. Ví dụ, lỗi giao tiếp DS4432U xuất hiện dưới dạng thông báo "ESP_ERROR_CHECK failed" kèm theo chỉ báo thời gian chờ, cho thấy sự cố điều chỉnh điện áp hoặc sự cố hàn ảnh hưởng đến linh kiện U10 chịu trách nhiệm giao tiếp hiển thị.


Các thông báo lỗi này bao gồm thông tin gỡ lỗi chi tiết, chẳng hạn như tệp nguồn cụ thể (main_ds4432u.c), lệnh gọi hàm bị lỗi và lõi bộ xử lý xử lý tác vụ. Thông tin backtrace cung cấp thêm ngữ cảnh cho việc khắc phục sự cố nâng cao. Các mẫu lỗi tương tự có thể xảy ra với chip điều khiển nhiệt độ và quạt EMC2101, mỗi mẫu lỗi tạo ra các chữ ký nhật ký riêng biệt giúp xác định thành phần bị lỗi.


Các sự cố phần cứng vật lý thường xuất hiện dưới dạng các chu kỳ lỗi lặp lại, sau đó là khởi động lại hệ thống. Nếu thiết bị của bạn phát ra tiếng ồn trong quá trình hoạt động, điều này thường chỉ ra các vấn đề về hàn, chẳng hạn như cầu nối giữa các chân linh kiện hoặc mối hàn không đủ tốt. Mặc dù các sự cố cơ học này không phải lúc nào cũng xuất hiện trong các mục nhật ký cụ thể của generate, nhưng chúng tạo ra các điều kiện vận hành không ổn định, biểu hiện dưới dạng các chu kỳ sập nguồn và khởi động lại thường xuyên trong đầu ra giám sát.


### Chiến lược khắc phục sự cố nâng cao


Giám sát tuần tự mang lại nhiều lợi thế so với giao diện gỡ lỗi dựa trên web, đặc biệt là đối với các lỗi gián đoạn hoặc thiết bị khởi động lại thường xuyên. Việc ghi nhật ký liên tục đảm bảo không mất thông tin chẩn đoán trong quá trình khởi động lại hệ thống, không giống như giao diện web có thể mất dữ liệu trong các sự kiện ngắt kết nối. Khả năng ghi nhật ký toàn diện này cho phép xác định các mẫu lỗi và đối chiếu các điều kiện lỗi cụ thể với các yếu tố phần cứng hoặc môi trường.


Khi phân tích các thiết bị có vấn đề, hãy tập trung vào chuỗi sự kiện dẫn đến lỗi thay vì các thông báo lỗi riêng lẻ. Giao tiếp ASIC thành công phải thể hiện quy trình xử lý tác vụ, tạo nonce và chu kỳ gửi chia sẻ đều đặn. Việc thiếu kết quả ASIC trong nhật ký cho thấy lỗi giao tiếp giữa ESP32 và chip mining, thường do sự cố nguồn điện, lỗi đường truyền hoặc lỗi linh kiện.


Để khắc phục sự cố một cách hệ thống, hãy ghi lại các mẫu lỗi và lỗi cụ thể của từng linh kiện trước khi tìm kiếm sự hỗ trợ từ cộng đồng. Nhật ký lỗi chi tiết, bao gồm mã định danh chip và chế độ lỗi cụ thể, cho phép người dùng có kinh nghiệm cung cấp hướng dẫn sửa chữa cụ thể, chẳng hạn như quy trình thay thế linh kiện hoặc sửa lỗi hàn. Phương pháp gỡ lỗi phần cứng có hệ thống này cải thiện đáng kể tỷ lệ sửa chữa thành công và giảm thời gian khắc phục sự cố cho các vấn đề phức tạp.


# Tùy chỉnh nâng cao

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Sửa đổi PCB

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad là một trong những công cụ mã nguồn mở mạnh mẽ nhất hiện có dành cho thiết kế và định tuyến bảng mạch in (PCB). Phần mềm chuyên nghiệp này cho phép các kỹ sư và người đam mê tạo ra các thiết kế điện tử phức tạp bằng cách đặt các linh kiện lên bảng mạch ảo và định tuyến các đường dẫn phức tạp kết nối các linh kiện này với nhau. Điều khiến KiCad đặc biệt hữu ích cho mục đích giáo dục và phát triển là tính chất mã nguồn mở hoàn toàn, cho phép người dùng sửa đổi, tùy chỉnh và học hỏi từ các thiết kế hiện có mà không bị hạn chế về bản quyền.


Dự án Bitaxe minh họa sức mạnh của phát triển phần cứng nguồn mở, cung cấp thiết kế PCB hoàn chỉnh mà người dùng có thể xem xét, sửa đổi và tùy chỉnh theo nhu cầu cụ thể. Khả năng tiếp cận này tạo ra một môi trường học tập tuyệt vời, nơi sinh viên và người thực hành có thể khám phá các thiết kế PCB thực tế, đồng thời nâng cao hiểu biết về hệ thống điện tử. Khả năng tùy chỉnh các yếu tố trực quan như logo mang đến một điểm khởi đầu dễ tiếp cận cho những người dùng có thể e ngại về sự phức tạp kỹ thuật của thiết kế điện tử.


### Thiết lập môi trường KiCad của bạn


Trước khi bắt đầu bất kỳ công việc tùy chỉnh nào, việc thiết lập môi trường phát triển phù hợp là điều cần thiết. Kho lưu trữ Bitaxe phải được tải xuống máy cục bộ của bạn, thường được thực hiện thông qua chức năng tải xuống ZIP của GitHub. Kho lưu trữ này chứa tất cả các tệp dự án cần thiết, bao gồm các tệp dự án KiCad, thư viện thành phần và tài liệu thiết kế cần thiết để sửa đổi thành công.


Việc cài đặt KiCad nên được hoàn tất bằng bản phân phối chính thức từ trang web KiCad, đảm bảo tính tương thích với các tệp dự án và khả năng truy cập các tính năng mới nhất. Sau khi cả kho lưu trữ và KiCad được cài đặt đúng cách, việc mở dự án yêu cầu điều hướng đến tệp dự án Bitaxe Ultra KiCad trong cấu trúc kho lưu trữ đã tải xuống. Tệp dự án này đóng vai trò là trung tâm liên kết tất cả các tệp thiết kế, thư viện thành phần và cài đặt cấu hình liên quan.


Cái nhìn ban đầu về một thiết kế PCB phức tạp có thể khiến người xem choáng ngợp, với vô số linh kiện, mạch in và lớp phủ tạo nên một bức tranh trực quan dày đặc. Tuy nhiên, chức năng xem 3D của KiCad cung cấp một công cụ vô giá để hiểu bố cục vật lý và các mối quan hệ không gian trong thiết kế. Góc nhìn ba chiều này biến biểu diễn sơ đồ trừu tượng thành hình ảnh trực quan chân thực của sản phẩm cuối cùng, giúp dễ dàng nắm bắt vị trí lắp đặt linh kiện và tính thẩm mỹ tổng thể của thiết kế.


### Quy trình tùy chỉnh logo


Tùy chỉnh logo trên thiết kế PCB là một trong những chỉnh sửa dễ dàng nhất dành cho người dùng mới làm quen với KiCad, chỉ cần kiến thức kỹ thuật tối thiểu mà vẫn mang lại kết quả trực quan tức thì. Quá trình này bắt đầu với công cụ chuyển đổi hình ảnh, giúp chuyển đổi các tệp hình ảnh tiêu chuẩn sang định dạng dấu chân tương thích với phần mềm thiết kế PCB. Quá trình chuyển đổi này đòi hỏi sự chú ý cẩn thận đến các thông số kích thước, thường được đo bằng milimét để đảm bảo tỷ lệ chính xác trên bo mạch thành phẩm.


Quy trình chuyển đổi hình ảnh bao gồm một số bước quan trọng quyết định hình thức và vị trí cuối cùng của logo tùy chỉnh. Việc lựa chọn hình ảnh gốc nên ưu tiên các thiết kế có độ tương phản cao, có thể chuyển đổi tốt sang quy trình in lụa được sử dụng trong sản xuất PCB. Kích thước logo trở nên rất quan trọng, vì logo phải đủ lớn để vẫn dễ đọc sau khi sản xuất mà không ảnh hưởng đến vị trí lắp đặt hoặc chức năng của linh kiện. Việc lựa chọn giữa lớp in lụa mặt trước và mặt sau ảnh hưởng đến cả khả năng hiển thị và các cân nhắc trong sản xuất.


Quản lý thư viện Footprint là một khía cạnh cơ bản của việc tùy chỉnh KiCad, yêu cầu người dùng hiểu cách phần mềm tổ chức và truy cập các yếu tố thiết kế. Việc thêm logo tùy chỉnh bao gồm việc tạo thư viện footprint mới hoặc sửa đổi các thư viện hiện có, sau đó liên kết các thư viện này một cách chính xác trong cấu trúc dự án. Quy trình này đảm bảo các yếu tố tùy chỉnh vẫn có thể truy cập được trong các phiên thiết kế khác nhau và có thể dễ dàng chia sẻ với các thành viên khác trong nhóm hoặc cộng tác viên.


### Khám phá và hiểu biết thiết kế nâng cao


Không chỉ đơn giản là tùy chỉnh logo, KiCad còn cung cấp các công cụ mạnh mẽ để khám phá và hiểu các thiết kế PCB phức tạp. Hệ thống quản lý lớp cho phép người dùng xem xét một cách có chọn lọc các khía cạnh khác nhau của thiết kế, từ vị trí và định tuyến linh kiện đến thông số kỹ thuật sản xuất và thông tin lắp ráp. Phương pháp tiếp cận phân lớp này cho phép phân tích chi tiết các yếu tố thiết kế cụ thể mà không bị rối mắt bởi các thành phần không liên quan.


Phân tích định tuyến theo dõi là một trong những khía cạnh giáo dục nhất của việc khám phá PCB, cho thấy cách các kết nối điện chạy giữa các linh kiện và hệ thống con. Bằng cách theo dõi từng tín hiệu riêng lẻ hoặc nhóm các tín hiệu liên quan, người dùng có thể hiểu rõ hơn về chức năng mạch và các quyết định thiết kế. Ví dụ, việc kiểm tra mạng lưới phân phối điện cho thấy cách các thành phần điều chỉnh điện áp và lọc hoạt động cùng nhau để cung cấp nguồn điện sạch, ổn định cho các linh kiện điện tử nhạy cảm.


Mối quan hệ giữa thiết kế sơ đồ mạch và bố cục vật lý trở nên rõ ràng thông qua việc xem xét kỹ lưỡng vị trí đặt linh kiện và các quyết định về định tuyến. Việc hiểu được lý do tại sao các linh kiện cụ thể được đặt ở những vị trí cụ thể, cách các yếu tố nhiệt ảnh hưởng đến quyết định bố trí và cách các yêu cầu về tính toàn vẹn tín hiệu chi phối các lựa chọn định tuyến mang lại những hiểu biết quý giá về thực hành thiết kế PCB chuyên nghiệp. Kiến thức này vô cùng hữu ích cho người dùng đang tự phát triển thiết kế hoặc sửa đổi thiết kế hiện có cho các ứng dụng cụ thể.


Các công cụ kiểm tra và xác minh quy tắc thiết kế toàn diện của KiCad đảm bảo các sửa đổi duy trì khả năng tương thích về điện và sản xuất. Các hệ thống tự động này giúp ngăn ngừa các lỗi thiết kế phổ biến, đồng thời hướng dẫn người dùng về các tiêu chuẩn và phương pháp tối ưu trong ngành. Việc tích hợp hình ảnh 3D với dữ liệu thiết kế điện tạo ra một môi trường học tập mạnh mẽ, nơi các khái niệm lý thuyết trở nên hữu hình thông qua hình ảnh minh họa và khám phá tương tác.


## Làm thế nào để tạo một tập tin nhà máy?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Việc xây dựng firmware tùy chỉnh cho các thiết bị mining dựa trên ESP đòi hỏi sự chú ý cẩn thận đến cấu hình, các thành phần phụ thuộc và quy trình xây dựng phù hợp. Hướng dẫn toàn diện này hướng dẫn toàn bộ quy trình tạo cả tệp nhị phân firmware tiêu chuẩn và tệp gốc bao gồm các thiết lập được cấu hình sẵn, giúp việc triển khai hiệu quả hơn và giảm thời gian thiết lập cho người dùng cuối.


Lưu ý rằng chương này khá chuyên môn và bạn có thể dễ dàng đọc lướt qua nếu tò mò.


### Thiết lập môi trường phát triển


Để bắt đầu phát triển firmware ESP-Miner, bạn nên thiết lập môi trường phát triển phù hợp trong Visual Studio Code, lý tưởng nhất là trên bản phân phối Linux. Phần mở rộng ESP-IDF đóng vai trò là nền tảng của quá trình thiết lập này, cung cấp các công cụ và tích hợp khung cần thiết cho việc phát triển ESP32. Khi cài đặt phần mở rộng ESP-IDF lần đầu tiên, người dùng sẽ thấy hướng dẫn thiết lập giúp quá trình cấu hình dễ dàng hơn.


Một cân nhắc quan trọng trong quá trình thiết lập là chọn phiên bản ESP-IDF phù hợp. Mặc dù trước đây khuyến nghị sử dụng phiên bản 5.1.3, nhưng kinh nghiệm thực tế cho thấy phiên bản này có thể gây ra các vấn đề về xây dựng, làm phức tạp quá trình phát triển. Phương pháp được khuyến nghị hiện nay là sử dụng ESP-IDF phiên bản 5.3 Beta 1, phiên bản này đã được chứng minh là giải quyết được những vấn đề phức tạp này và đảm bảo các thiết bị Bitaxe hoạt động bình thường. Quá trình cài đặt yêu cầu chọn tùy chọn cài đặt Express và đặc biệt chọn phiên bản 5.3 Beta 1 từ các tùy chọn có sẵn.


Thiết lập môi trường phát triển mở rộng ra ngoài phạm vi cài đặt ESP-IDF để bao gồm cấu hình terminal phù hợp. Visual Studio Code cung cấp nhiều phương thức để truy cập chức năng ESP-IDF, bao gồm tùy chọn bảng lệnh để mở terminal ESP-IDF hoặc sử dụng biểu tượng terminal chuyên dụng nằm trong giao diện. Môi trường terminal chuyên dụng này đảm bảo tất cả các lệnh ESP-IDF hoạt động chính xác và cung cấp quyền truy cập vào toàn bộ chuỗi công cụ.


### Cấu hình cài đặt ESP-Miner


Tệp cấu hình là cốt lõi của quy trình tùy chỉnh ESP-Miner, chứa tất cả các thông số thiết yếu xác định cách thiết bị sẽ hoạt động trong môi trường mục tiêu. Cấu hình này bao gồm các thiết lập mạng, kết nối nhóm mining và các thông số phần cứng cụ thể phải được điều chỉnh cho phù hợp với từng kịch bản triển khai cụ thể.


Cấu hình mạng là thành phần chính của quy trình thiết lập, yêu cầu chỉ định thông tin đăng nhập Wi-Fi bao gồm SSID và mật khẩu. Thay vì sử dụng các giá trị giữ chỗ như "test", cấu hình sản xuất nên bao gồm thông tin đăng nhập mạng thực tế mà thiết bị sẽ sử dụng trong môi trường hoạt động. Cấu hình này cũng hỗ trợ nhiều thiết lập nhóm mining khác nhau, hỗ trợ cả cấu hình nhóm riêng với địa chỉ IP cụ thể và nhóm công cộng như public-pool.io với cài đặt cổng tương ứng.


Các tham số cấu hình dành riêng cho Mining bao gồm thiết lập người dùng tầng, thường tương ứng với địa chỉ Bitcoin, nơi phần thưởng mining sẽ được chuyển hướng. Các tham số phần cứng bổ sung như thiết lập tần số, thiết lập điện áp và thông số kỹ thuật loại ASIC phải phù hợp với nền tảng phần cứng mục tiêu. Kho lưu trữ GitHub cung cấp các ví dụ được cấu hình sẵn cho các biến thể phần cứng khác nhau, chẳng hạn như cấu hình BM1368 được thiết kế cho các thiết bị Super và thiết lập BM1366 cho các biến thể Ultra. Thông số kỹ thuật phiên bản bo mạch, chẳng hạn như đặt phiên bản cổng thành 401 cho các bản sửa đổi phần cứng mới hơn, đảm bảo khả năng tương thích với các đặc điểm cụ thể của thiết bị mục tiêu.


### Xây dựng Web Interface và Phần mềm lõi


Dự án ESP-Miner tích hợp một giao diện web tinh vi, yêu cầu biên dịch riêng trước khi quá trình xây dựng firmware chính có thể bắt đầu. Giao diện web này, được gọi là firmware AxeOS, cung cấp cho người dùng một giao diện quản lý toàn diện để giám sát và điều khiển các thiết bị mining của họ.


Quá trình xây dựng giao diện web bắt đầu bằng việc điều hướng đến thư mục máy chủ HTTP trong cấu trúc kho lưu trữ chính, cụ thể là thư mục con AxeOS. Vị trí này chứa ứng dụng web dựa trên Node.js, yêu cầu cài đặt phụ thuộc thông qua lệnh npm install. Hệ thống xây dựng giả định rằng Node.js đã được cài đặt đúng cách trên hệ thống phát triển, vì đây là yêu cầu cơ bản đối với quá trình biên dịch giao diện web.


Sau khi cài đặt dependency, lệnh npm run build sẽ biên dịch các thành phần giao diện web, tạo các tệp cần thiết để nhúng vào firmware ESP32. Quá trình biên dịch này tạo ra các tài nguyên web được tối ưu hóa, cung cấp chức năng giao diện người dùng đồng thời duy trì hiệu quả sử dụng bộ nhớ trên nền tảng ESP32 bị hạn chế. Việc hoàn thành thành công bước build này là rất quan trọng trước khi tiến hành biên dịch firmware chính, vì firmware ESP-Miner tích hợp các thành phần giao diện web này như một chức năng không thể thiếu.


### Tạo tệp gốc với cấu hình nhúng


Việc tạo tệp gốc là một chiến lược triển khai tiên tiến, nhúng trực tiếp các thiết lập cấu hình vào tệp nhị phân chương trình cơ sở, loại bỏ nhu cầu cấu hình thủ công trong quá trình thiết lập thiết bị. Phương pháp này đặc biệt hữu ích cho các triển khai quy mô lớn hoặc các tình huống đòi hỏi cấu hình nhất quán trên nhiều thiết bị.


Quá trình tạo tệp gốc bắt đầu bằng việc tạo tệp cấu hình nhị phân từ tệp cấu hình CSV bằng công cụ tạo phân vùng NVS của ESP-IDF. Công cụ này, nằm trong thư mục thành phần ESP-IDF tại nvs-flash/nvs-partition-generator, sẽ chuyển đổi cấu hình dễ đọc sang định dạng nhị phân phù hợp để lưu trữ trực tiếp trên bộ nhớ flash. Tập lệnh nvs-partition-gen.py sẽ xử lý tệp config.csv và tạo tệp config.binary nhắm đến không gian địa chỉ bộ nhớ 0x6000.


Việc lắp ráp cuối cùng các tệp gốc sử dụng các tập lệnh hợp nhất chuyên biệt để kết hợp các tệp nhị phân firmware lõi với dữ liệu cấu hình. Kho lưu trữ cung cấp nhiều tùy chọn hợp nhất, bao gồm một tập lệnh hợp nhất tiêu chuẩn cho các tệp gốc cơ bản và một tập lệnh hợp nhất bao gồm cấu hình cho các tệp gốc toàn diện. Tập lệnh merge-bin-with-config.sh tạo các tệp gốc bao gồm cả chức năng firmware và các thiết lập được cấu hình sẵn, tạo thành một gói triển khai hoàn chỉnh. Phương pháp này cho phép tạo các tệp gốc dành riêng cho thiết bị, chẳng hạn như các phiên bản được thiết kế riêng cho các thiết bị Bitaxe Ultra với các bản sửa đổi bo mạch cụ thể, đồng thời duy trì tính linh hoạt cho các tệp gốc chung generate mà không cần cấu hình nhúng cho các tình huống yêu cầu tính linh hoạt khi thiết lập thủ công.


Các tệp gốc đã hoàn thành cung cấp cho các nhóm triển khai các tệp nhị phân sẵn sàng để flash bao gồm tất cả các thành phần chương trình cơ sở và cài đặt cấu hình cần thiết, hợp lý hóa quy trình cung cấp thiết bị và đảm bảo các thông số hoạt động nhất quán trên các thiết bị mining đã triển khai.


## Làm thế nào để sử dụng Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Trình cài đặt web Bitaxe là một phương pháp tiếp cận hợp lý để quản lý firmware cho các thiết bị Bitaxe, cung cấp cho người dùng nhiều tùy chọn cài đặt thông qua giao diện web. Công cụ toàn diện này loại bỏ sự phức tạp thường gặp khi cập nhật firmware và cài đặt mới, giúp người dùng dễ dàng quản lý thiết bị bất kể trình độ kỹ thuật của họ. Việc hiểu rõ cách sử dụng trình cài đặt này là rất quan trọng để duy trì hiệu suất thiết bị tối ưu và tránh những lỗi thường gặp có thể khiến thiết bị tạm thời không hoạt động.


### Yêu cầu về khả năng tương thích của trình duyệt và truy cập


Trình cài đặt web Bitaxe có thể được truy cập thông qua URL chuyên dụng [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (URL được trình bày trong video hiện đã ngừng hoạt động), đóng vai trò là trung tâm cho tất cả các hoạt động cài đặt phần mềm. Tuy nhiên, để sử dụng thành công công cụ dựa trên web này, trình duyệt cần phải tương thích, vì trình cài đặt dựa trên các công nghệ web cụ thể không được hỗ trợ trên tất cả các trình duyệt. Chrome là trình duyệt được đề xuất chính cho trình cài đặt, cung cấp khả năng tương thích hoàn toàn với tất cả các tính năng và chức năng. Mặc dù các trình duyệt dựa trên Chromium khác có thể cung cấp chức năng tương tự, nhưng các lựa chọn thay thế phổ biến như Brave và Firefox lại thiếu hỗ trợ web serial API cần thiết, khiến chúng không tương thích với các hoạt động cốt lõi của trình cài đặt.


Hạn chế này của trình duyệt xuất phát từ việc trình cài đặt phụ thuộc vào giao tiếp nối tiếp trực tiếp với các thiết bị Bitaxe thông qua giao diện web. Giao tiếp nối tiếp web API, cho phép giao tiếp này, vẫn là một tiêu chuẩn web tương đối mới và chưa được trình duyệt phổ biến chấp nhận. Người dùng cố gắng truy cập trình cài đặt thông qua các trình duyệt không được hỗ trợ sẽ gặp lỗi kết nối và không thể giao tiếp với thiết bị, buộc phải chuyển sang trình duyệt tương thích trước khi tiến hành bất kỳ hoạt động cài đặt nào.


### Yêu cầu về nguồn điện và chuẩn bị thiết bị


Thiết bị Bitaxe có yêu cầu nguồn điện khác nhau tùy thuộc vào model và phiên bản cụ thể, do đó việc quản lý nguồn điện phù hợp là rất quan trọng để cài đặt firmware thành công. Thiết bị chạy phiên bản 204 trở xuống chỉ có thể hoạt động thông qua nguồn USB, lấy đủ dòng điện từ máy tính được kết nối để duy trì hoạt động trong quá trình flash. Việc sắp xếp nguồn điện đơn giản này giúp các phiên bản trước đó đặc biệt thuận tiện cho việc cập nhật firmware, vì người dùng chỉ cần kết nối một cáp USB duy nhất để bắt đầu quá trình cài đặt.


Tuy nhiên, các thiết bị chạy phiên bản 205 trở lên yêu cầu nguồn điện ngoài kết nối USB, phản ánh những thay đổi về mức tiêu thụ điện năng và thiết kế mạch trong các bản sửa đổi phần cứng mới hơn. Các thiết bị này không thể sử dụng đủ điện năng chỉ thông qua USB, do đó cần phải kết nối với nguồn điện tiêu chuẩn trong quá trình cài đặt firmware. Việc không cung cấp đủ điện cho các thiết bị mới này sẽ dẫn đến lỗi cài đặt và có khả năng làm hỏng quá trình cập nhật firmware.


Quá trình kết nối vật lý yêu cầu thời gian cụ thể và thao tác nút bấm để đảm bảo giao tiếp chính xác giữa trình cài đặt và thiết bị. Người dùng phải nhấn và giữ nút khởi động trên thiết bị Bitaxe trước khi kết nối cáp USB-C với máy tính. Trình tự này sẽ đưa thiết bị vào chế độ bộ nạp khởi động, cho phép trình cài đặt giao tiếp trực tiếp với bộ nhớ firmware của thiết bị. Việc kết nối cáp USB trước khi nhấn nút khởi động sẽ khiến thiết bị hoạt động bình thường thay vì chế độ bộ nạp khởi động cần thiết để cài đặt firmware, ngăn trình cài đặt thiết lập kênh giao tiếp cần thiết.


### Tùy chọn cài đặt và ứng dụng của chúng


Trình cài đặt Bitaxe Web Installer cung cấp bốn tùy chọn cài đặt riêng biệt, mỗi tùy chọn được thiết kế cho các trường hợp sử dụng và cấu hình thiết bị cụ thể. Bitaxe Superboard phiên bản 4.0.1 là phần mềm hệ thống mới nhất dành cho các thiết bị Super, với phiên bản 4.0.2 dự kiến sẽ được phát hành trong tương lai. Tùy chọn này bao gồm cả phiên bản gốc và phiên bản cập nhật, mang lại sự linh hoạt trong cách cài đặt dựa trên nhu cầu của người dùng và trạng thái thiết bị.


Cài đặt gốc đại diện cho việc thay thế hoàn toàn phần mềm hệ thống, phản ánh quy trình sản xuất ban đầu, bao gồm các quy trình tự kiểm tra toàn diện để xác minh chức năng thiết bị trên tất cả các hệ thống. Khi người dùng chọn cài đặt gốc, trình cài đặt sẽ xóa hoàn toàn phần mềm hệ thống và dữ liệu cấu hình hiện có, thay thế bằng một cài đặt mới, sạch sẽ, giống hệt với những gì sẽ được áp dụng trong quá trình sản xuất. Quy trình này bao gồm tự kiểm tra tự động để xác thực hoạt động phần cứng bình thường, yêu cầu người dùng khởi động lại thiết bị sau khi hoàn tất trước khi có thể tiếp tục hoạt động bình thường. Cài đặt gốc đặc biệt hữu ích khi thiết bị gặp sự cố dai dẳng hoặc khi người dùng muốn đưa thiết bị trở về thông số kỹ thuật ban đầu của nhà sản xuất.


Cài đặt bản cập nhật cung cấp một phương pháp bảo thủ hơn, giữ nguyên dữ liệu cấu hình hiện có trong khi chỉ cập nhật các thành phần phần mềm cốt lõi. Tùy chọn này lý tưởng cho những người dùng đã tùy chỉnh cài đặt thiết bị và muốn duy trì cấu hình cá nhân, đồng thời tận dụng các cải tiến và sửa lỗi phần mềm. Quá trình cập nhật chỉ nhắm mục tiêu đến các thành phần phần mềm cần sửa đổi, giữ nguyên các cài đặt cụ thể của người dùng, thông tin đăng nhập WiFi và địa chỉ Bitcoin trong suốt quá trình cài đặt.


### Những cân nhắc quan trọng về cài đặt và bảo vệ dữ liệu


Sự khác biệt giữa cài đặt gốc và cài đặt cập nhật mang lại những tác động đáng kể đến cấu hình thiết bị và bảo toàn dữ liệu người dùng. Cài đặt gốc sẽ xóa hoàn toàn thiết bị, xóa tất cả các cài đặt do người dùng cấu hình, bao gồm thông tin đăng nhập WiFi, địa chỉ Bitcoin và mọi thông số thiết bị được cá nhân hóa. Sau khi cài đặt gốc, người dùng phải kết nối lại với mạng WiFi mặc định của thiết bị và cấu hình lại tất cả cài đặt cá nhân từ đầu, về cơ bản là coi thiết bị như mới từ nhà sản xuất.


Việc cài đặt bản cập nhật yêu cầu phải chú ý cẩn thận đến tùy chọn xóa thiết bị được hiển thị trong quá trình cài đặt. Trình cài đặt sẽ hỏi người dùng "Bạn có muốn xóa thiết bị trước khi cài đặt Bitaxe Flasher không?" kèm theo cảnh báo rằng tất cả dữ liệu trên thiết bị sẽ bị mất. Người dùng thực hiện cài đặt bản cập nhật phải từ chối tùy chọn này bằng cách nhấp vào "Tiếp theo" thay vì xác nhận thao tác xóa. Việc chấp nhận tùy chọn xóa trong quá trình cài đặt bản cập nhật sẽ xóa tệp cấu hình của thiết bị, có khả năng khiến thiết bị không hoạt động cho đến khi cấu hình phù hợp được khôi phục. Mặc dù tình huống này không làm hỏng thiết bị vĩnh viễn, nhưng nó tạo ra những rắc rối không cần thiết và yêu cầu các bước cấu hình bổ sung để khôi phục hoạt động bình thường.


Quá trình cài đặt sẽ tự động diễn ra sau khi người dùng lựa chọn và xác nhận. Trình cài đặt xử lý mọi khía cạnh kỹ thuật của việc chuyển giao và xác minh firmware, đồng thời cung cấp các chỉ báo tiến độ và cập nhật trạng thái trong suốt quá trình. Phương pháp tự động này giúp người dùng không cần phải hiểu các quy trình cài đặt firmware phức tạp, đồng thời đảm bảo kết quả đáng tin cậy và nhất quán trên các mẫu thiết bị và phiên bản firmware khác nhau.


## Làm thế nào để tạo và đặt hàng PCB?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Chương này tập trung vào quy trình thực tế tạo tệp sản xuất từ các dự án KiCad và đặt hàng PCB chuyên nghiệp từ các nhà sản xuất trực tuyến. Lấy dự án Bitaxe làm ví dụ, chúng ta sẽ xem xét toàn bộ quy trình làm việc từ khi tạo tệp đến khi đặt hàng với nhà sản xuất PCB.


### Hiểu về quy trình sản xuất PCB


Hành trình từ một thiết kế KiCad hoàn chỉnh đến một PCB vật lý bao gồm một số bước quan trọng, thu hẹp khoảng cách giữa thiết kế kỹ thuật số và sản xuất thực tế. Khi làm việc với các dự án phức tạp như Bitaxe, trình chỉnh sửa PCB trong KiCad cung cấp một cái nhìn toàn diện về thiết kế của bạn, hiển thị tất cả các linh kiện và kết nối của chúng thông qua các dấu vết màu. Các đường màu đỏ và xanh lam bạn thấy đại diện cho các kết nối điện giữa các mạch tích hợp và linh kiện khác nhau trên bo mạch. Tính năng xem 3D của KiCad cho phép bạn hình dung bo mạch lắp ráp cuối cùng sẽ trông như thế nào, cung cấp cái nhìn sâu sắc có giá trị về vị trí lắp ráp linh kiện và các xung đột cơ học tiềm ẩn.


Quy trình sản xuất yêu cầu các định dạng tệp cụ thể mà các nhà sản xuất PCB có thể diễn giải và sử dụng để chế tạo bo mạch của bạn. Các tệp này chứa thông tin chính xác về lớp đồng, lỗ khoan, vị trí lắp ráp linh kiện và các thông số kỹ thuật sản xuất khác. Việc hiểu rõ quy trình làm việc này là rất quan trọng, dù bạn đang làm việc với thiết kế Bitaxe tiêu chuẩn hay tạo các sửa đổi như thêm logo tùy chỉnh, thay đổi giá trị linh kiện hoặc điều chỉnh bố cục bo mạch để đáp ứng các yêu cầu cụ thể.


### Tạo tệp Gerber cho sản xuất


Tệp Gerber đóng vai trò là tiêu chuẩn công nghiệp để truyền đạt thông tin thiết kế PCB cho nhà sản xuất. Các tệp này chứa tất cả dữ liệu cần thiết để chế tạo PCB, bao gồm mẫu lớp đồng, định nghĩa mặt nạ hàn và vị trí lỗ khoan. Để sử dụng generate các tệp này trong KiCad, hãy điều hướng đến trình soạn thảo PCB và truy cập các kết quả chế tạo thông qua menu Tệp. Phần mềm sẽ tự động cấu hình các thiết lập phù hợp cho các quy trình sản xuất tiêu chuẩn, bao gồm cấu trúc thư mục đầu ra phù hợp thường được sắp xếp dưới dạng "tệp sản xuất/gerber".


Quá trình tạo ra nhiều tệp Gerber, mỗi tệp đại diện cho các khía cạnh khác nhau của thiết kế PCB. Các tệp này hoạt động cùng nhau để cung cấp cho nhà sản xuất hướng dẫn chế tạo đầy đủ. Sau khi tạo, các tệp này phải được nén thành tệp ZIP, vì đây là định dạng chuẩn mà hầu hết các nhà sản xuất PCB mong đợi. Tệp ZIP chứa tất cả dữ liệu sản xuất cần thiết và đảm bảo không có tệp nào bị mất hoặc bị hỏng trong quá trình tải lên trang web của nhà sản xuất.


Cần lưu ý rằng nhiều dự án nguồn mở, bao gồm cả Bitaxe, thường bao gồm các tệp sản xuất được tạo sẵn trong kho lưu trữ của họ. Tuy nhiên, việc hiểu cách tự mình tạo các tệp generate này là rất quan trọng khi thực hiện các sửa đổi thiết kế hoặc làm việc với các phiên bản bo mạch khác nhau. Kiến thức này đặc biệt hữu ích khi tùy chỉnh thiết kế hoặc xử lý sự cố sản xuất.


### Lựa chọn nhà sản xuất PCB và hiểu rõ các tùy chọn


Thị trường sản xuất PCB cung cấp nhiều lựa chọn uy tín, trong đó JLCPCB và PCBWay là những lựa chọn phổ biến nhất cho cả người dùng nghiệp dư lẫn chuyên nghiệp. Cả hai nhà sản xuất đều cung cấp các dịch vụ tương tự với giá cả cạnh tranh và chất lượng đáng tin cậy, mặc dù mỗi nhà sản xuất đều có những lợi thế riêng tùy thuộc vào yêu cầu dự án của bạn. JLCPCB thường thu hút người dùng lần đầu nhờ giá ưu đãi và giao diện thân thiện với người dùng, trong khi PCBWay có thể cung cấp các tùy chọn vật liệu khác nhau hoặc dịch vụ chuyên biệt.


Khi tải tệp Gerber lên trang web của nhà sản xuất, hệ thống sẽ tự động phân tích thiết kế của bạn và đưa ra các tùy chọn sản xuất khác nhau. Các cài đặt mặc định do các nền tảng này cung cấp thường phù hợp với hầu hết các thiết kế tiêu chuẩn, và bạn nên duy trì các cài đặt này trừ khi có yêu cầu cụ thể. Các thông số chính bao gồm độ dày PCB, trọng lượng đồng, độ hoàn thiện bề mặt và số lượng tối thiểu. Hầu hết các nhà sản xuất yêu cầu đơn hàng tối thiểu là năm bo mạch, điều này thực sự phù hợp với các dự án của người dùng nghiệp dư, nơi việc có bo mạch dự phòng hoặc chia sẻ với bạn bè sẽ rất hữu ích.


Tùy chọn màu sắc là một trong số ít lựa chọn mang tính thẩm mỹ trong quá trình sản xuất. Mặc dù màu xanh lá cây vẫn là lựa chọn truyền thống và tiết kiệm chi phí nhất, các nhà sản xuất thường cung cấp các lựa chọn thay thế bao gồm xanh lam, đỏ, vàng, tím và đen. Việc lựa chọn màu sắc chỉ mang tính thẩm mỹ và không ảnh hưởng đến hiệu suất điện của PCB, mặc dù một số màu có thể có tác động nhỏ đến chi phí hoặc thời gian sản xuất lâu hơn.


### Những cân nhắc về sản xuất tiên tiến và các tùy chọn lắp ráp


Ngoài việc chế tạo PCB cơ bản, các nhà sản xuất hiện đại còn cung cấp các dịch vụ bổ sung giúp đơn giản hóa đáng kể việc hoàn thành dự án của bạn. Khuôn in là một trong những dịch vụ bổ sung giá trị nhất, đặc biệt đối với các thiết kế có linh kiện bước chân nhỏ như chip ASIC trong các dự án Bitcoin và mining. Khuôn in về cơ bản là một khuôn nhôm được cắt chính xác với các lỗ tương ứng chính xác với vị trí miếng hàn trên PCB của bạn. Công cụ này cho phép bôi kem hàn một cách nhất quán và chính xác, cải thiện đáng kể chất lượng lắp ráp và giảm khả năng xảy ra lỗi hàn.


Các lựa chọn khuôn in thường bao gồm khuôn in đơn với cả hoa văn trên và dưới, hoặc khuôn in riêng cho mỗi mặt của bảng mạch. Đối với hầu hết các dự án, khuôn in kết hợp tỏ ra tiện lợi và tiết kiệm chi phí hơn. Độ dày khuôn in được tính toán cẩn thận để phủ một lượng kem hàn phù hợp cho từng loại linh kiện và kích thước miếng đệm cụ thể của bạn. Sử dụng khuôn in sẽ biến quy trình thủ công vốn tẻ nhạt và dễ xảy ra lỗi thành một bước lắp ráp nhanh chóng và chuyên nghiệp.


Mặc dù một số nhà sản xuất cung cấp dịch vụ lắp ráp một phần hoặc toàn bộ, nhưng các lựa chọn này đòi hỏi sự cân nhắc kỹ lưỡng cho các dự án phức tạp như Bitaxe. Tính khả dụng của linh kiện, chi phí và giá trị giáo dục của việc tự lắp ráp đều là những yếu tố ảnh hưởng đến quyết định này. Nhiều linh kiện chuyên dụng cần thiết cho các dự án Bitcoin mining có thể không có sẵn thông qua các dịch vụ lắp ráp PCB tiêu chuẩn, khiến việc tìm nguồn linh kiện và lắp ráp thủ công trở thành phương pháp thiết thực hơn. Các tập tiếp theo của loạt bài này sẽ đề cập đến các chiến lược tìm nguồn linh kiện và kỹ thuật lắp ráp để giúp bạn hoàn thành thành công dự án Bitaxe của mình từ PCB trần đến thiết bị hoạt động.


Quy trình sản xuất và lắp ráp là cầu nối quan trọng giữa thiết kế kỹ thuật số và triển khai thực tế. Hiểu rõ các quy trình công việc này giúp bạn kiểm soát dự án, giảm chi phí và tích lũy kinh nghiệm thực tế quý báu với các quy trình sản xuất chuyên nghiệp. Cho dù bạn đang xây dựng một nguyên mẫu đơn lẻ hay lên kế hoạch sản xuất quy mô nhỏ, việc thành thạo những kỹ năng này sẽ mở ra những khả năng mới để hiện thực hóa các thiết kế điện tử của bạn.


# Tối ưu hóa hiệu suất

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Đánh giá Bitaxe của bạn

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Việc theo đuổi hiệu suất tối ưu của mining đòi hỏi một phương pháp tiếp cận cấu hình phần cứng có hệ thống, cân bằng giữa hashrate, hiệu suất và quản lý nhiệt. Bitaxe cung cấp nhiều thông số cấu hình có thể ảnh hưởng đáng kể đến hiệu suất, nhưng việc kiểm tra thủ công mọi kết hợp cài đặt sẽ không thực tế và tốn thời gian. Chương này sẽ khám phá cách tận dụng các công cụ đánh giá hiệu suất tự động để tối ưu hóa hiệu suất của Bitaxe một cách khoa học trong khi vẫn duy trì các điều kiện vận hành an toàn.


### Hiểu về số liệu hiệu suất Bitaxe và cấu hình cơ sở


Trước khi đi sâu vào các kỹ thuật tối ưu hóa, điều quan trọng là phải hiểu các chỉ số hiệu suất chính xác định hiệu suất hoạt động của Bitaxe. Các chỉ số chính bao gồm hashrate được đo bằng terahash mỗi giây, hiệu suất công suất được biểu thị bằng joule trên terahash, tần số ASIC tính bằng megahertz và điện áp lõi tính bằng vôn. Một Bitaxe được cấu hình tốt có thể đạt khoảng 1,1 terahash với hiệu suất khoảng 17 joule trên terahash, hoạt động ở tần số 550 megahertz với điện áp ASIC đo được là 1,14 vôn. Những con số cơ sở này cung cấp một điểm tham chiếu để hiểu những cải tiến tiềm năng có được thông qua tối ưu hóa hệ thống.


Mối quan hệ giữa các số liệu này rất phức tạp và phụ thuộc lẫn nhau. Tần số cao hơn thường làm tăng hashrate nhưng cũng làm tăng mức tiêu thụ điện năng và sinh nhiệt. Tương tự, việc điều chỉnh điện áp ảnh hưởng đến cả hiệu suất và đặc tính nhiệt. Thách thức nằm ở việc tìm ra sự cân bằng tối ưu để tối đa hóa hashrate hoặc hiệu suất trong khi vẫn duy trì hoạt động ổn định trong giới hạn nhiệt độ an toàn. Quá trình tối ưu hóa này đòi hỏi phải thử nghiệm có phương pháp trên nhiều tổ hợp thông số, khiến các công cụ tự động trở nên vô cùng hữu ích để đạt được kết quả tối ưu.


### Kiến trúc công cụ chuẩn Bitaxe Hashrate


Công cụ [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) là một giải pháp tinh vi dựa trên Python, ban đầu được WhiteCookie phát triển và sau đó được mrv777 cải tiến. Công cụ mã nguồn mở này, được phân phối theo giấy phép GPLv3, tự động hóa quy trình phức tạp gồm nhiều kết hợp cấu hình để xác định cài đặt tối ưu cho phần cứng cụ thể của bạn. Điểm mạnh chính của công cụ nằm ở cách tiếp cận có hệ thống đối với việc kiểm tra thông số, điều chỉnh tần số và điện áp theo từng bước, đồng thời liên tục theo dõi các chỉ số hiệu suất và điều kiện nhiệt.


Quá trình đánh giá chuẩn thường mất từ 30 đến 40 phút để hoàn tất, trong thời gian đó, công cụ sẽ kiểm tra một cách có phương pháp các kết hợp khác nhau của cài đặt tần số và điện áp ASIC. Công cụ bắt đầu với các cài đặt cơ sở thận trọng, thường bắt đầu từ 1,15 vôn và 500 megahertz, sau đó tăng dần các thông số này trong khi theo dõi hashrate, nhiệt độ và độ ổn định. Quan trọng là, công cụ ưu tiên vận hành an toàn hơn hiệu suất tối đa, tự động giảm các cài đặt gây ra hiện tượng sinh nhiệt quá mức hoặc mất ổn định. Cách tiếp cận thận trọng này đảm bảo rằng quá trình tối ưu hóa không ảnh hưởng đến tuổi thọ hoặc độ tin cậy của phần cứng.


### Yêu cầu cài đặt và thiết lập


Việc triển khai công cụ Bitaxe Hashrate Benchmark yêu cầu một số thành phần phần mềm tiên quyết trên máy tính cục bộ của bạn. Các yêu cầu chính bao gồm Python để thực thi các tập lệnh đánh giá chuẩn, Git để quản lý kho lưu trữ, và tùy chọn Visual Studio Code để nâng cao khả năng của môi trường phát triển. Mặc dù công cụ có thể được vận hành từ giao diện dòng lệnh, việc sử dụng môi trường phát triển tích hợp như VS Code sẽ giúp bạn dễ dàng theo dõi quy trình đánh giá chuẩn và phân tích kết quả hơn.


Quy trình cài đặt tuân theo các quy trình phát triển Python tiêu chuẩn, bắt đầu bằng việc sao chép kho lưu trữ từ GitHub sang máy cục bộ của bạn. Sau khi kho lưu trữ được tải xuống, bạn sẽ cần tạo một môi trường ảo để tách biệt các phần phụ thuộc của công cụ khỏi cài đặt Python trên hệ thống. Việc tách biệt này giúp ngăn ngừa xung đột tiềm ẩn với các ứng dụng Python khác và đảm bảo hoạt động nhất quán. Sau khi kích hoạt môi trường ảo, bạn sẽ cài đặt các phần phụ thuộc cần thiết bằng tệp yêu cầu được cung cấp, tệp này sẽ tự động cấu hình tất cả các thư viện và mô-đun cần thiết để công cụ hoạt động bình thường.


### Thực hiện chuẩn mực và diễn giải kết quả


Việc chạy benchmark yêu cầu thực hiện một lệnh Python duy nhất, trong đó địa chỉ IP của Bitaxe được sử dụng làm tham số. Công cụ sẽ tự động kết nối với giao diện web của máy đào và bắt đầu quá trình kiểm tra hệ thống. Trong quá trình thực thi, công cụ cung cấp thông tin ghi nhật ký chi tiết, hiển thị lần lặp kiểm tra hiện tại, cài đặt điện áp và tần số được áp dụng, kết quả hashrate, điện áp đầu vào, giá trị nhiệt độ và dữ liệu nhiệt từ các thành phần quan trọng như bộ chuyển đổi buck. Phản hồi theo thời gian thực này cho phép bạn theo dõi tiến trình benchmark và hiểu rõ các cài đặt khác nhau ảnh hưởng đến hiệu suất máy đào như thế nào.


Khả năng quản lý nhiệt thông minh của công cụ trở nên rõ ràng khi nhiệt độ đạt ngưỡng an toàn 66 độ C. Thay vì vượt quá giới hạn vận hành an toàn, điểm chuẩn sẽ tự động giảm cài đặt để duy trì độ ổn định nhiệt. Cách tiếp cận thận trọng này đảm bảo rằng quá trình tối ưu hóa ưu tiên độ tin cậy phần cứng lâu dài hơn là lợi ích hiệu suất ngắn hạn. Sau khi hoàn tất, công cụ sẽ tạo ra kết quả toàn diện ở định dạng JSON, xếp hạng năm cấu hình hàng đầu cho cả hashrate tối đa và hiệu suất tối ưu. Những kết quả này cung cấp hướng dẫn rõ ràng để lựa chọn cấu hình phù hợp nhất với các ưu tiên vận hành của bạn, cho dù tập trung vào sản lượng tối đa hay hiệu quả năng lượng.


Công cụ đo điểm chuẩn cũng cung cấp các tùy chọn tùy chỉnh cho người dùng nâng cao muốn điều chỉnh các thông số thử nghiệm. Các đối số dòng lệnh cho phép bạn chỉ định điện áp và tần số khởi động tùy chỉnh, cho phép tối ưu hóa mục tiêu hơn cho các trường hợp sử dụng cụ thể. Ví dụ: nếu bạn đã biết phần cứng của mình hoạt động tốt ở tần số cao hơn, bạn có thể bắt đầu đo điểm chuẩn ở cài đặt nâng cao thay vì bắt đầu từ các giá trị mặc định bảo thủ. Tính linh hoạt này làm cho công cụ trở nên hữu ích cho cả người dùng mới tìm kiếm tối ưu hóa tự động và thợ đào giàu kinh nghiệm muốn tinh chỉnh các đặc tính hiệu suất cụ thể.


## Ép xung Bitaxe của bạn

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Việc ép xung thiết bị Bitaxe đòi hỏi phải cân nhắc kỹ lưỡng cả những hạn chế về phần cứng lẫn yêu cầu tản nhiệt. Mặc dù nhiều người dùng thích ép xung thấp hơn để thiết bị hoạt động êm ái hơn, nhưng việc hiểu rõ các kỹ thuật ép xung phù hợp là điều cần thiết cho những ai muốn đạt hiệu suất tối đa mà không làm hỏng phần cứng. Quá trình này bao gồm việc tăng tần số và có thể điều chỉnh cài đặt điện áp vượt quá thông số kỹ thuật của nhà sản xuất, vốn dĩ làm tăng nhiệt lượng tỏa ra và gây áp lực lên các linh kiện.


Nền tảng của việc ép xung thành công nằm ở cơ sở hạ tầng tản nhiệt đầy đủ. Trước khi thử bất kỳ thay đổi tần số nào, bạn phải đảm bảo Bitaxe của mình có khả năng tản nhiệt phù hợp. Một Bitaxe Gamma với bộ tản nhiệt và quạt chất lượng cao sẽ cung cấp khả năng quản lý nhiệt cần thiết để ép xung an toàn. Không nên ép xung các thiết bị có bộ tản nhiệt nhỏ và quạt không đủ tiêu chuẩn, vì hiệu suất làm mát kém sẽ dẫn đến hiện tượng giảm xung nhịp do nhiệt và tiềm ẩn nguy cơ hư hỏng phần cứng. Mối quan hệ giữa nhiệt độ và tuổi thọ linh kiện là rất quan trọng cần hiểu rõ—nhiệt độ quá cao tạo ra áp lực làm suy giảm các linh kiện điện tử theo thời gian, làm giảm đáng kể tuổi thọ hoạt động của thiết bị.


### Vị trí đặt tản nhiệt chiến lược


Linh kiện quan trọng nhất cần được làm mát bổ sung là bộ chuyển đổi buck, một linh kiện nhỏ màu đen nằm ở mặt sau của Bitaxe, gần cuộn dây lớn. Thiết bị này chuyển đổi nguồn điện 5V đầu vào xuống điện áp phù hợp cho chip ASIC, thường khoảng 1,2V. Bộ chuyển đổi buck, thường được gọi là TPS, tạo ra lượng nhiệt đáng kể trong quá trình hoạt động và là một nút thắt cổ chai nhiệt, hạn chế khả năng ép xung. Việc lắp đặt một bộ tản nhiệt dính nhỏ trên linh kiện này không chỉ cho phép tăng khả năng ép xung mà còn cải thiện hiệu suất tổng thể bằng cách giảm tổn thất nhiệt.


Việc bố trí thêm tản nhiệt có thể mang lại lợi ích cho các khu vực dòng điện cao khác trên bo mạch. Mạch điều chỉnh điện áp chịu áp lực điện đáng kể khi dòng điện chạy từ phần đầu vào xuống qua các đường dẫn khác nhau trên bo mạch để cung cấp cho chip ASIC. Nhiều người ép xung giàu kinh nghiệm lắp đặt tản nhiệt ở mặt trước của Bitaxe tại các khu vực dòng điện cao này để cải thiện khả năng tản nhiệt. Mặc dù không thực sự cần thiết cho việc ép xung vừa phải, nhưng các biện pháp làm mát bổ sung này trở nên quan trọng khi đẩy tần số lên mức cực đại.


### Những cân nhắc và hạn chế của hệ thống làm mát


Bộ điều khiển ESP32, hiển thị dưới dạng linh kiện màu bạc trên bo mạch, thường không cần tản nhiệt bổ sung. Linh kiện này tỏa nhiệt rất ít một cách độc lập và chỉ nóng lên do sự truyền nhiệt từ các linh kiện xung quanh. Việc lắp đặt tản nhiệt gần ESP32 có thể gây nhiễu ăng-ten Wi-Fi liền kề, làm giảm kết nối không dây và chất lượng tín hiệu. Hãy tập trung làm mát vào các linh kiện điều chỉnh công suất và khu vực ASIC thay vì mạch điều khiển.


Cấu hình quạt kép mang lại cả cơ hội lẫn hạn chế. Mặc dù việc thêm một quạt thứ hai để thổi khí qua mặt sau của Bitaxe có thể cải thiện hiệu suất làm mát, nhưng phần mềm hệ thống của thiết bị chỉ có thể điều khiển một quạt một cách chính xác. Bitaxe có hai đầu cắm quạt nhưng chỉ có một bộ điều khiển quạt, nghĩa là việc kết nối hai quạt sẽ gây nhầm lẫn cho phần mềm hệ thống do nhận được các tín hiệu RPM xung đột. Cấu hình này vẫn hoạt động nhưng có thể dẫn đến việc điều khiển quạt không ổn định.


### Đánh giá hiệu suất cơ bản


Trước khi thử bất kỳ thay đổi ép xung nào, hãy thiết lập các chỉ số hiệu suất cơ bản bằng cách chạy Bitaxe ở cài đặt mặc định trong vài giờ. Theo dõi nhiệt độ ASIC, nhiệt độ bộ điều chỉnh điện áp và tỷ lệ phần trăm tốc độ quạt thông qua giao diện web. Nhiệt độ hoạt động tối ưu nên duy trì ASIC dưới 60°C và bộ điều chỉnh điện áp dưới 60°C trong điều kiện bình thường. Nếu thiết bị của bạn đã hoạt động trên 65°C trên ASIC hoặc 70-80°C trên bộ điều chỉnh điện áp ở cài đặt mặc định, bắt buộc phải có phần cứng làm mát bổ sung trước khi tiến hành ép xung.


Phương pháp tiếp cận có hệ thống để tăng tần số bao gồm các bước tăng dần sử dụng các tùy chọn tần số được xác định trước trong menu cài đặt. Bắt đầu bằng cách chọn bước tần số khả dụng tiếp theo cao hơn cài đặt hiện tại của bạn trong khi vẫn duy trì điện áp lõi mặc định. Phương pháp tiếp cận thận trọng này cho phép bạn đánh giá tác động về nhiệt và độ ổn định trước khi thực hiện các thay đổi bổ sung. Cho phép thiết bị hoạt động ở mỗi cài đặt tần số mới trong ít nhất 30 phút đến một giờ, đồng thời theo dõi xu hướng nhiệt độ và độ ổn định của tốc độ băm trong suốt quá trình đánh giá.


### Cấu hình tùy chỉnh nâng cao


Để truy cập các thiết lập tần số và điện áp tùy chỉnh, người dùng cần bật giao diện ép xung nâng cao bằng cách thêm "?OC" vào URL giao diện web của thiết bị. Thao tác này sẽ mở khóa các trường nhập liệu thủ công để kiểm soát tần số và điện áp chính xác, kèm theo các cảnh báo phù hợp về rủi ro khi vận hành ngoài các thông số được thiết kế. Giao diện tùy chỉnh cho phép tinh chỉnh vượt ra ngoài các bước tần số tiêu chuẩn, cho phép người dùng có kinh nghiệm tối ưu hóa hiệu suất cho các cấu hình làm mát cụ thể của họ.


Khi sử dụng cài đặt tùy chỉnh, hãy duy trì kích thước gia số thận trọng 10-15 MHz cho mỗi bước điều chỉnh. Phương pháp này giúp ngăn ngừa các đột biến nhiệt đột ngột và cho phép kiểm tra độ ổn định phù hợp ở mỗi mức tần số. Một số người dùng nâng cao đạt được tần số khoảng 700 MHz với điện áp lõi được điều chỉnh đến 1,175V hoặc các giá trị tương tự, nhưng những cài đặt cực đoan này đòi hỏi phải điều chỉnh tản nhiệt đáng kể và theo dõi cẩn thận. Bộ điều chỉnh điện áp có thể hoạt động ở nhiệt độ lên đến 100°C mà không bị hư hỏng ngay lập tức, nhưng nhiệt độ cao hơn sẽ làm giảm hiệu suất và độ tin cậy lâu dài. Ép xung thành công đòi hỏi sự kiên nhẫn, thử nghiệm có hệ thống và theo dõi liên tục để đạt được cải thiện hiệu suất ổn định trong khi vẫn bảo toàn tính toàn vẹn của phần cứng.


# Phần cuối

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Đánh giá khóa học này

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Phần kết luận

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>