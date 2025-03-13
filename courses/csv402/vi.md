---
name: Giao thức RGB, từ lý thuyết đến thực hành
goal: Có được các kỹ năng cần thiết để hiểu và sử dụng RGB
objectives: 

  - Hiểu các khái niệm cơ bản của giao thức RGB
  - Nắm vững các nguyên tắc xác thực phía khách hàng và cam kết Bitcoin
  - Tìm hiểu cách tạo, quản lý và chuyển giao hợp đồng RGB
  - Cách vận hành nút Lightning tương thích RGB

---
# Khám phá giao thức RGB

Khám phá thế giới RGB, một giao thức được thiết kế để triển khai và thực thi các quyền kỹ thuật số, dưới dạng hợp đồng và tài sản, dựa trên các quy tắc đồng thuận và hoạt động của chuỗi khối Bitcoin. Khóa đào tạo toàn diện này hướng dẫn bạn qua các nền tảng kỹ thuật và thực tế của RGB, từ các khái niệm về "Xác thực phía máy khách" và "Con dấu sử dụng một lần", đến việc triển khai các hợp đồng thông minh nâng cao.

Thông qua chương trình từng bước có cấu trúc, bạn sẽ khám phá ra các cơ chế xác thực phía máy khách, các cam kết xác định trên Bitcoin và các mẫu tương tác giữa người dùng. Tìm hiểu cách tạo, quản lý và chuyển token RGB trên Bitcoin hoặc Lightning Network.

Cho dù bạn là nhà phát triển, người đam mê Bitcoin hay chỉ đơn giản là tò mò muốn tìm hiểu thêm về công nghệ này, khóa đào tạo này sẽ cung cấp cho bạn các công cụ và kiến thức cần thiết để làm chủ RGB và xây dựng các giải pháp sáng tạo trên Bitcoin.

Khóa học dựa trên hội thảo trực tiếp do Fulgur'Ventures tổ chức và được giảng dạy bởi ba giáo viên và chuyên gia RGB nổi tiếng.

+++
# Giới thiệu

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Bài thuyết trình khóa học

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Xin chào mọi người và chào mừng đến với khóa đào tạo này dành riêng cho RGB, một hệ thống hợp đồng thông minh được xác thực phía máy khách chạy trên Bitcoin và Lightning Network. Cấu trúc của khóa học này được thiết kế để cho phép khám phá sâu hơn về chủ đề phức tạp này. Sau đây là cách tổ chức khóa học:

**Phần 1: Lý thuyết

Phần đầu tiên dành riêng cho các khái niệm lý thuyết cần thiết để hiểu các nguyên tắc cơ bản của xác thực phía máy khách và RGB. Như bạn sẽ khám phá trong khóa học này, RGB giới thiệu một loạt các khái niệm kỹ thuật thường không thấy trong Bitcoin. Trong phần này, bạn cũng sẽ tìm thấy một bảng chú giải thuật ngữ cung cấp các định nghĩa cho tất cả các thuật ngữ cụ thể cho giao thức RGB.

**Phần 2: Thực hành

Phần thứ hai sẽ tập trung vào việc áp dụng các khái niệm lý thuyết được thấy trong phần 1. Chúng ta sẽ học cách tạo và thao tác các hợp đồng RGB. Chúng ta cũng sẽ xem cách lập trình bằng các công cụ này. Hai phần đầu tiên này được trình bày bởi Maxim Orlovsky.

**Mục 3: Ứng dụng

Phần cuối cùng do các diễn giả khác trình bày về các ứng dụng cụ thể dựa trên RGB để làm nổi bật các trường hợp sử dụng thực tế.

---
Khóa đào tạo này ban đầu phát triển từ trại huấn luyện phát triển nâng cao kéo dài hai tuần tại Viareggio, Tuscany, do [Fulgur'Ventures](https://fulgur.ventures/) tổ chức. Tuần đầu tiên, tập trung vào Rust và SDK, có thể được tìm thấy trong khóa học khác này:

https://planb.network/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58
Trong khóa học này, chúng ta sẽ tập trung vào tuần thứ hai của trại huấn luyện, tập trung vào RGB.

**Tuần 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**Tuần 2 - Chương trình đào tạo hiện tại CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

Xin chân thành cảm ơn những người tổ chức các khóa học trực tiếp này và 3 giáo viên đã tham gia:


- Maxim Orlovsky: *Ex Tenebrae senentia sapiens dominabitur astris. Cypher, AI, robot, thuyết xuyên nhân loại. Người tạo ra RGB, Prime, Radiant và lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo: *Nhà phát triển, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Tôi đang góp sức biến thế giới thành một thế giới phi thực tế của cypherpunk. Hiện đang làm việc về RGB tại Bitfinex*.

Phiên bản viết của khóa đào tạo này được soạn thảo bằng cách sử dụng 2 nguồn chính:


- Video hội thảo của Maxim Orlovsky, Hunter Trujilo và Frederico Tenga tại Lightning Bootcamp;
- Tài liệu RGB, được tài trợ bởi [Bitfinex](https://www.bitfinex.com/).

# RGB về mặt lý thuyết

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Giới thiệu về các khái niệm điện toán phân tán

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)

RGB là một giao thức được thiết kế để áp dụng và thực thi các quyền kỹ thuật số (dưới dạng hợp đồng và tài sản) theo cách có thể mở rộng và bảo mật, dựa trên các quy tắc đồng thuận và hoạt động của chuỗi khối Bitcoin. Mục đích của chương đầu tiên này là trình bày các khái niệm và thuật ngữ cơ bản xung quanh giao thức RGB, đặc biệt nhấn mạnh mối liên hệ chặt chẽ của nó với các khái niệm điện toán phân tán cơ bản như Xác thực phía máy khách và Dấu niêm phong sử dụng một lần.

Trong chương này, chúng ta sẽ khám phá những điều cơ bản của **hệ thống đồng thuận phân tán** và xem RGB phù hợp với họ công nghệ này như thế nào. Chúng tôi cũng sẽ giới thiệu các nguyên tắc chính giúp chúng ta hiểu lý do tại sao RGB hướng đến mục tiêu mở rộng và độc lập với cơ chế đồng thuận của Bitcoin, đồng thời dựa vào nó khi cần thiết.

### Giới thiệu

Điện toán phân tán, một nhánh cụ thể của khoa học máy tính, nghiên cứu các giao thức được sử dụng để lưu thông và xử lý thông tin trên một mạng lưới các nút. Cùng nhau, các nút này và các quy tắc giao thức tạo nên cái được gọi là hệ thống phân tán. Trong số các thuộc tính thiết yếu đặc trưng cho một hệ thống như vậy là:


- **Khả năng xác minh và xác thực độc lập** của một số dữ liệu nhất định bởi mỗi nút;
- Khả năng cho các nút xây dựng (tùy thuộc vào giao thức) chế độ xem toàn bộ hoặc một phần thông tin. Các chế độ xem này là **trạng thái** của hệ thống phân tán;
- **Thứ tự thời gian** của các hoạt động, để dữ liệu được đóng dấu thời gian một cách đáng tin cậy và có sự đồng thuận về trình tự các sự kiện (trình tự trạng thái).

Đặc biệt, khái niệm **sự đồng thuận** trong hệ thống phân tán bao gồm hai khía cạnh:


- Việc công nhận tính hợp lệ** của các thay đổi trạng thái (theo các quy tắc giao thức);
- **Thỏa thuận về thứ tự** của các thay đổi trạng thái này khiến việc viết lại hoặc đảo ngược các hoạt động đã xác thực sau đó trở nên không thể (điều này cũng được gọi trong Bitcoin là "bảo vệ chi tiêu gấp đôi").

Việc triển khai chức năng đầu tiên, không cần cấp phép của cơ chế đồng thuận phân tán đã được Satoshi Nakamoto giới thiệu với Bitcoin, nhờ vào việc sử dụng kết hợp cấu trúc dữ liệu blockchain và thuật toán Proof-of-Work (PoW). Trong hệ thống này, độ tin cậy của lịch sử khối phụ thuộc vào sức mạnh tính toán dành cho nó bởi các nút (thợ đào). Do đó, Bitcoin là một ví dụ quan trọng và mang tính lịch sử về hệ thống đồng thuận phân tán mở cho tất cả mọi người (*không cần cấp phép*).

Trong thế giới blockchain và điện toán phân tán, chúng ta có thể phân biệt hai mô hình cơ bản: ***blockchain*** theo nghĩa truyền thống và ***state channels***, ví dụ tốt nhất về mô hình này trong sản xuất là Lightning Network. Blockchain được định nghĩa là một sổ đăng ký các sự kiện theo thứ tự thời gian, được sao chép bằng sự đồng thuận trong một mạng mở, không cần cấp phép. Mặt khác, state channels là các kênh ngang hàng cho phép hai (hoặc nhiều) người tham gia duy trì trạng thái được cập nhật ngoài chuỗi, chỉ sử dụng blockchain khi mở và đóng các kênh này.

Trong bối cảnh của Bitcoin, chắc hẳn bạn đã quen thuộc với các nguyên tắc khai thác, phi tập trung và tính cuối cùng của các giao dịch trên blockchain, cũng như cách thức hoạt động của các kênh thanh toán. Với RGB, chúng tôi giới thiệu một mô hình mới có tên là **Xác thực phía máy khách**, không giống như blockchain hay Lightning, bao gồm việc lưu trữ và xác thực cục bộ (phía máy khách) các chuyển đổi trạng thái của hợp đồng thông minh. Điều này cũng khác với các kỹ thuật "DeFi" khác (_rollups_, _plasma_, _ARK_, v.v.), ở chỗ Xác thực phía máy khách dựa vào blockchain để ngăn chặn chi tiêu gấp đôi và có hệ thống đóng dấu thời gian, đồng thời giữ sổ đăng ký các trạng thái và chuyển đổi ngoài chuỗi, chỉ với những người tham gia có liên quan.

![RGB-Bitcoin](assets/fr/003.webp)

Sau này, chúng tôi cũng sẽ giới thiệu một thuật ngữ quan trọng: khái niệm "**stash**", ám chỉ tập hợp dữ liệu phía máy khách cần thiết để duy trì trạng thái của hợp đồng, vì dữ liệu này không được sao chép toàn cầu trên toàn mạng. Cuối cùng, chúng ta sẽ xem xét cơ sở lý luận đằng sau RGB, một giao thức tận dụng Xác thực phía máy khách và lý do tại sao nó bổ sung cho các phương pháp tiếp cận hiện có (chuỗi khối và kênh trạng thái).

### Bộ ba vấn đề trong điện toán phân tán

Để hiểu cách Xác thực phía máy khách và RGB giải quyết các vấn đề chưa được blockchain và Lightning giải quyết, chúng ta hãy cùng khám phá 3 "bộ ba" chính trong điện toán phân tán:


- Khả năng mở rộng, Phân quyền, Quyền riêng tư** ;
- Định lý CAP** (Tính nhất quán, Tính khả dụng, Độ dung sai phân vùng);
- Bộ ba nguy hiểm của CIA** (Bảo mật, Toàn vẹn, Khả dụng).

#### 1. Khả năng mở rộng, phân cấp và bảo mật


- Chuỗi khối (Bitcoin)**

Blockchain có tính phi tập trung cao, nhưng không có khả năng mở rộng. Hơn nữa, vì mọi thứ đều nằm trong sổ đăng ký công khai toàn cầu nên tính bảo mật bị hạn chế. Chúng ta có thể thử cải thiện tính bảo mật bằng các công nghệ không kiến thức (giao dịch bí mật, chương trình mimblewimble, v.v.), nhưng chuỗi công khai không thể ẩn biểu đồ giao dịch.


- Kênh Lightning/State**

Các kênh trạng thái (như với Lightning Network) có khả năng mở rộng hơn và riêng tư hơn blockchain, vì các giao dịch diễn ra ngoài chuỗi. Tuy nhiên, nghĩa vụ công bố công khai một số yếu tố nhất định (giao dịch tài trợ, cấu trúc mạng) và việc giám sát lưu lượng mạng có thể làm giảm tính bảo mật. Sự phi tập trung cũng bị ảnh hưởng: định tuyến tốn nhiều tiền mặt và các nút chính có thể trở thành điểm tập trung. Đây chính xác là hiện tượng mà chúng ta bắt đầu thấy trên Lightning.


- Xác thực phía máy khách (RGB)**

Mô hình mới này thậm chí còn có khả năng mở rộng và bảo mật hơn, vì chúng ta không chỉ có thể tích hợp các kỹ thuật bằng chứng kiến thức không tiết lộ mà còn không có biểu đồ giao dịch toàn cầu, vì không ai nắm giữ toàn bộ sổ đăng ký. Mặt khác, nó cũng ngụ ý một sự thỏa hiệp nhất định về tính phi tập trung: bên phát hành hợp đồng thông minh có thể có vai trò trung tâm (giống như "bên triển khai hợp đồng" trong Ethereum). Tuy nhiên, không giống như blockchain, với Xác thực phía máy khách, bạn chỉ lưu trữ và xác thực các hợp đồng mà bạn quan tâm, điều này cải thiện khả năng mở rộng bằng cách tránh nhu cầu tải xuống và xác minh tất cả các trạng thái hiện có.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. Định lý CAP (Tính nhất quán, Tính khả dụng, Dung sai phân vùng)

Định lý CAP nhấn mạnh rằng một hệ thống phân tán không thể đồng thời thỏa mãn tính nhất quán (*Tính nhất quán*), tính khả dụng (*Tính khả dụng*) và dung sai phân vùng (*Dung sai phân vùng*).


- Chuỗi khối**

Blockchain ưu tiên tính nhất quán và khả dụng, nhưng lại không hiệu quả với phân vùng mạng: nếu bạn không thể nhìn thấy một khối, bạn không thể hành động và có cùng góc nhìn với toàn bộ mạng.


- Tia chớp** (bằng tiếng Pháp)

Hệ thống kênh trạng thái có tính khả dụng và khả năng phân vùng (vì hai nút vẫn có thể kết nối với nhau ngay cả khi mạng bị phân mảnh), nhưng tính nhất quán tổng thể phụ thuộc vào việc mở và đóng các kênh trên chuỗi khối.


- Xác thực phía máy khách (RGB)**

Một hệ thống như RGB cung cấp tính nhất quán (mỗi người tham gia xác thực dữ liệu của mình tại địa phương, không có sự mơ hồ) và khả năng phân vùng (bạn lưu trữ dữ liệu của mình một cách tự chủ), nhưng không đảm bảo tính khả dụng toàn cầu (mọi người phải đảm bảo rằng họ có các phần lịch sử có liên quan và một số người tham gia có thể không công bố bất cứ điều gì hoặc ngừng chia sẻ một số thông tin nhất định).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. Bộ ba CIA (Bảo mật, Chính trực, Sẵn sàng)

Bộ ba này nhắc nhở chúng ta rằng tính bảo mật, tính toàn vẹn và tính khả dụng không thể được tối ưu hóa cùng một lúc. Blockchain, Lightning và Xác thực phía máy khách nằm ở những vị trí khác nhau trong sự cân bằng này. Ý tưởng là không có hệ thống đơn lẻ nào có thể cung cấp mọi thứ; cần phải kết hợp một số phương pháp (đóng dấu thời gian của blockchain, phương pháp đồng bộ của Lightning và xác thực cục bộ với RGB) để có được một gói thống nhất cung cấp các đảm bảo tốt trong từng chiều.

![RGB-Bitcoin](assets/fr/006.webp)

### Vai trò của blockchain và khái niệm phân mảnh

Blockchain (trong trường hợp này là Bitcoin) chủ yếu đóng vai trò là cơ chế _đóng dấu thời gian_ và bảo vệ chống lại việc chi tiêu gấp đôi. Thay vì chèn toàn bộ dữ liệu của hợp đồng thông minh hoặc hệ thống phi tập trung, chúng tôi chỉ cần đưa **cam kết mật mã** (_cam kết_) vào các giao dịch (theo nghĩa Xác thực phía máy khách, mà chúng tôi sẽ gọi là "chuyển đổi trạng thái"). Do đó:


- Chúng tôi giải phóng blockchain khỏi lượng lớn dữ liệu và logic;
- Mỗi người dùng chỉ lưu trữ lịch sử cần thiết cho phần hợp đồng của riêng mình ("*mảnh*" của người đó), thay vì sao chép trạng thái toàn cầu.

Phân mảnh là một khái niệm có nguồn gốc từ cơ sở dữ liệu phân tán (ví dụ: MySQL cho các mạng xã hội như Facebook hoặc Twitter). Để giải quyết vấn đề về khối lượng dữ liệu và độ trễ đồng bộ hóa, cơ sở dữ liệu được phân đoạn thành các _shards_ (Hoa Kỳ, Châu Âu, Châu Á, v.v.). Mỗi phân đoạn đều nhất quán cục bộ và chỉ được đồng bộ hóa một phần với các phân đoạn khác.

Đối với các hợp đồng thông minh loại RGB, chúng tôi phân mảnh theo chính các hợp đồng. Mỗi hợp đồng là một _shard_ độc lập. Ví dụ, nếu bạn chỉ giữ token USDT, bạn không phải lưu trữ hoặc xác thực toàn bộ lịch sử của một token khác như USDC. Trên Bitcoin, blockchain không thực hiện _sharding_: bạn có một tập hợp UTXO toàn cầu. Với Xác thực phía máy khách, mỗi người tham gia chỉ giữ lại dữ liệu hợp đồng mà họ giữ hoặc sử dụng.

Do đó, chúng ta có thể hình dung hệ sinh thái như sau:


- Blockchain (Bitcoin)** là nền tảng đảm bảo sao chép hoàn toàn một sổ đăng ký tối thiểu và đóng vai trò là lớp đóng dấu thời gian;
- Mạng lưới Lightning** cho các giao dịch nhanh chóng, bảo mật, vẫn dựa trên tính bảo mật và thanh toán cuối cùng của chuỗi khối Bitcoin;
- Xác thực phía máy khách và RGB** để thêm logic hợp đồng thông minh phức tạp hơn mà không làm lộn xộn blockchain hoặc mất tính bảo mật.

![RGB-Bitcoin](assets/fr/007.webp)

Ba yếu tố này tạo thành một tổng thể hình tam giác, thay vì một chồng tuyến tính của "lớp 2", "lớp 3" v.v. Lightning có thể kết nối trực tiếp với Bitcoin hoặc được liên kết với các giao dịch Bitcoin kết hợp dữ liệu RGB. Tương tự như vậy, một ứng dụng "BiFi" (tài chính trên Bitcoin) có thể kết hợp với blockchain, với Lightning và với RGB theo nhu cầu về tính bảo mật, khả năng mở rộng hoặc logic hợp đồng.

![RGB-Bitcoin](assets/fr/008.webp)

### Khái niệm về chuyển đổi trạng thái

Trong bất kỳ hệ thống phân tán nào, mục đích của cơ chế xác thực là có thể **xác định tính hợp lệ và thứ tự thời gian của các thay đổi trạng thái**. Mục đích là để xác minh rằng các quy tắc giao thức đã được tôn trọng và chứng minh rằng các thay đổi trạng thái này theo sau nhau theo thứ tự xác định, không thể chối cãi.

Để hiểu cách thức xác thực này hoạt động trong bối cảnh của **Bitcoin** và nói chung là để nắm bắt triết lý đằng sau Xác thực phía máy khách, trước tiên chúng ta hãy cùng nhìn lại các cơ chế của chuỗi khối Bitcoin, trước khi xem Xác thực phía máy khách khác với các cơ chế đó như thế nào và nó có thể tối ưu hóa những gì.

![RGB-Bitcoin](assets/fr/009.webp)

Trong trường hợp của chuỗi khối Bitcoin, việc xác thực giao dịch dựa trên một quy tắc đơn giản:


- Tất cả các nút mạng tải xuống mọi khối và giao dịch;
- Họ xác thực các giao dịch này để xác minh sự tiến hóa chính xác của bộ UTXO (tất cả các đầu ra chưa sử dụng);
- Họ lưu trữ dữ liệu này (dưới dạng khối) để có thể phát lại lịch sử nếu cần.

![RGB-Bitcoin](assets/fr/010.webp)

Tuy nhiên, mô hình này có hai nhược điểm lớn:


- Khả năng mở rộng**: vì mỗi nút phải xử lý, xác minh và lưu trữ các giao dịch của mọi người nên có giới hạn rõ ràng về khả năng giao dịch, liên quan cụ thể đến kích thước khối tối đa (trung bình 1 MB trong 10 phút đối với Bitcoin, không bao gồm cookie);
- Quyền riêng tư**: mọi thứ đều được phát sóng và lưu trữ công khai (số lượng, địa chỉ đích, v.v.), điều này hạn chế tính bảo mật của các giao dịch.

![RGB-Bitcoin](assets/fr/012.webp)

Trên thực tế, mô hình này hoạt động như một lớp cơ sở cho Bitcoin (Lớp 1), nhưng có thể không đủ cho những mục đích sử dụng phức tạp hơn, đồng thời yêu cầu thông lượng giao dịch cao và mức độ bảo mật nhất định.

Xác thực phía máy khách dựa trên ý tưởng ngược lại: thay vì yêu cầu toàn bộ mạng xác thực và lưu trữ tất cả các giao dịch, mỗi người tham gia (máy khách) sẽ chỉ xác thực phần lịch sử liên quan đến mình:


- Khi một người nhận được tài sản (hoặc bất kỳ tài sản kỹ thuật số nào khác), họ chỉ cần biết và xác minh chuỗi hoạt động (chuyển đổi trạng thái) dẫn đến tài sản đó và chứng minh tính hợp pháp của nó;
- Chuỗi hoạt động này, từ ***Genesis*** (vấn đề ban đầu) đến giao dịch gần đây nhất, tạo thành một đồ thị có hướng phi chu trình (DAG) hoặc phân đoạn, tức là một phần của toàn bộ lịch sử.

![RGB-Bitcoin](assets/fr/013.webp)

Đồng thời, để phần còn lại của mạng (hay chính xác hơn là lớp cơ sở, chẳng hạn như Bitcoin) có thể khóa ở trạng thái cuối cùng mà không cần xem thông tin chi tiết về dữ liệu này, Xác thực phía máy khách dựa trên khái niệm ***cam kết***.

*Cam kết* là một cam kết mật mã, thường là _băm_ (ví dụ SHA-256) được chèn vào giao dịch Bitcoin, chứng minh rằng dữ liệu riêng tư đã được đưa vào mà không tiết lộ dữ liệu này.

Nhờ những _cam kết_ này, chúng ta có thể chứng minh:


- Sự tồn tại của thông tin (vì nó được cam kết với hàm băm);
- Tính ưu tiên của thông tin này (vì nó được neo và đóng dấu thời gian trong chuỗi khối, với ngày tháng và thứ tự khối).

Tuy nhiên, nội dung chính xác không được tiết lộ, do đó vẫn giữ được tính bảo mật.

Nói một cách cụ thể, quá trình chuyển đổi trạng thái RGB diễn ra như sau:


- Bạn chuẩn bị một quá trình chuyển đổi trạng thái mới (ví dụ: chuyển mã thông báo RGB);
- Bạn tạo một cam kết mật mã cho quá trình chuyển đổi này và chèn nó vào giao dịch Bitcoin (những cam kết này được gọi là "*mỏ neo*" trong giao thức RGB);
- Bên đối tác (bên nhận) sẽ truy xuất lịch sử phía khách hàng liên quan đến tài sản này và xác thực tính nhất quán từ đầu đến cuối, từ khi hợp đồng thông minh được hình thành cho đến quá trình chuyển đổi mà bạn truyền tải đến hợp đồng.

![RGB-Bitcoin](assets/fr/014.webp)

Xác thực phía máy khách mang lại hai lợi ích chính:


- Khả năng mở rộng:**

Các cam kết (*cam kết*) được đưa vào blockchain là nhỏ (khoảng vài chục byte). Điều này đảm bảo rằng không gian khối không bị bão hòa, vì chỉ cần bao gồm hàm băm. Nó cũng cho phép giao thức ngoài chuỗi phát triển, vì mỗi người dùng chỉ phải lưu trữ đoạn lịch sử của mình (_stash_ của mình).


- Sự riêng tư :**

Bản thân các giao dịch (tức là nội dung chi tiết của chúng) không được công bố trên chuỗi. Chỉ có dấu vân tay của chúng (*băm*) là được công bố. Do đó, số tiền, địa chỉ và logic hợp đồng vẫn được giữ riêng tư và người nhận có thể xác minh, cục bộ, tính hợp lệ của phân đoạn của mình bằng cách kiểm tra tất cả các lần chuyển đổi trước đó. Không có lý do gì để người nhận công khai dữ liệu này, ngoại trừ trong trường hợp có tranh chấp hoặc khi cần bằng chứng.

Trong một hệ thống như RGB, nhiều trạng thái chuyển đổi từ các hợp đồng khác nhau (hoặc các tài sản khác nhau) có thể được tổng hợp thành một giao dịch Bitcoin duy nhất thông qua một _cam kết_ duy nhất. Cơ chế này thiết lập một liên kết xác định, có dấu thời gian giữa giao dịch trên chuỗi và dữ liệu ngoài chuỗi (các chuyển đổi được xác thực phía máy khách) và cho phép nhiều phân đoạn được ghi đồng thời trong một điểm neo duy nhất, giúp giảm thêm chi phí và dấu chân trên chuỗi.

Trên thực tế, khi giao dịch Bitcoin này được xác thực, nó sẽ "khóa" vĩnh viễn trạng thái của các hợp đồng cơ bản, vì không thể sửa đổi hàm băm đã được ghi trong chuỗi khối.

![RGB-Bitcoin](assets/fr/015.webp)

### Khái niệm cất giấu

**Stash** là tập hợp dữ liệu phía máy khách mà người tham gia phải giữ lại hoàn toàn để duy trì tính toàn vẹn và lịch sử của hợp đồng thông minh RGB. Không giống như kênh Lightning, nơi một số trạng thái nhất định có thể được tái tạo cục bộ từ thông tin được chia sẻ, stash của hợp đồng RGB không được sao chép ở nơi khác: nếu bạn mất nó, sẽ không ai có thể khôi phục lại cho bạn, vì bạn chịu trách nhiệm về phần lịch sử của mình. Đây là lý do tại sao bạn cần áp dụng một hệ thống có quy trình sao lưu đáng tin cậy trong RGB.

![RGB-Bitcoin](assets/fr/016.webp)

### Con dấu dùng một lần: nguồn gốc và hoạt động

Khi chấp nhận một tài sản như tiền tệ, có hai đảm bảo cần thiết:


- Tính xác thực của sản phẩm nhận được;
- Tính độc đáo của sản phẩm nhận được để tránh chi phí gấp đôi.

Đối với tài sản vật chất, chẳng hạn như tiền giấy, sự hiện diện vật lý là đủ để chứng minh rằng nó không bị sao chép. Tuy nhiên, trong thế giới kỹ thuật số, nơi tài sản hoàn toàn mang tính thông tin, việc xác minh này phức tạp hơn vì thông tin có thể dễ dàng nhân lên và bị sao chép.

Như chúng ta đã thấy trước đó, việc người gửi tiết lộ lịch sử chuyển đổi trạng thái cho phép chúng ta đảm bảo tính xác thực của mã thông báo RGB. Bằng cách truy cập vào tất cả các giao dịch kể từ giao dịch genesis, chúng ta có thể xác nhận tính xác thực của mã thông báo. Nguyên tắc này tương tự như nguyên tắc của Bitcoin, trong đó lịch sử của các đồng tiền có thể được truy ngược lại giao dịch coinbase ban đầu để xác minh tính hợp lệ của chúng. Tuy nhiên, không giống như Bitcoin, lịch sử chuyển đổi trạng thái trong RGB này là riêng tư và được lưu giữ ở phía máy khách.

Để ngăn chặn việc chi tiêu hai lần token RGB, chúng tôi sử dụng một cơ chế có tên là "**Single-use Seal**". Hệ thống này đảm bảo rằng mỗi token, sau khi đã sử dụng, không thể được sử dụng lại một cách gian lận lần thứ hai.

Con dấu sử dụng một lần là nguyên mẫu mật mã, được Peter Todd đề xuất vào năm 2016, tương tự như khái niệm con dấu vật lý: một khi con dấu đã được đóng vào thùng chứa, thì không thể mở hoặc sửa đổi nó mà không làm vỡ con dấu đó vĩnh viễn.

![RGB-Bitcoin](assets/fr/018.webp)

Cách tiếp cận này, được chuyển sang thế giới kỹ thuật số, giúp chứng minh rằng một chuỗi sự kiện thực sự đã diễn ra và không thể thay đổi nó sau đó nữa. Do đó, Dấu niêm phong dùng một lần vượt ra ngoài logic đơn giản của `băm + dấu thời gian`, bổ sung thêm khái niệm về một dấu niêm phong chỉ có thể đóng **một lần**.

![RGB-Bitcoin](assets/fr/017.webp)

Để Con dấu sử dụng một lần có hiệu quả, bạn cần một phương tiện chứng minh xuất bản có khả năng chứng minh sự tồn tại hoặc không tồn tại của một ấn phẩm, và khó (nếu không muốn nói là không thể) làm giả một khi thông tin đã được phổ biến. Một **chuỗi khối** (như Bitcoin) có thể đảm nhiệm vai trò này, cũng như một tờ báo giấy có lưu hành công khai chẳng hạn. Ý tưởng như sau:


- Chúng tôi muốn chứng minh rằng một cam kết nhất định về tin nhắn `h(m)` đã được công bố cho người nghe mà không tiết lộ nội dung của tin nhắn `m`;
- Chúng tôi muốn chứng minh rằng không có cam kết tin nhắn `h(m')` cạnh tranh nào khác được công bố thay cho `h(m)`;
- Chúng tôi cũng muốn kiểm tra xem tin nhắn `m` có tồn tại trước một ngày cụ thể hay không.

Blockchain thực sự phù hợp với vai trò này: ngay khi một giao dịch được đưa vào một khối, toàn bộ mạng sẽ có cùng bằng chứng không thể xác thực về sự tồn tại và nội dung của giao dịch đó (ít nhất là một phần, vì _cam kết_ có thể ẩn các chi tiết trong khi chứng minh tính xác thực của thông điệp).

Do đó, Con dấu sử dụng một lần có thể được coi là lời hứa chính thức về việc công bố một thông điệp (vẫn chưa được biết đến ở giai đoạn này) một lần và chỉ một lần duy nhất, theo cách mà tất cả các bên quan tâm có thể xác minh được.

Không giống như _cam kết_ đơn giản (băm) hoặc dấu thời gian, chứng thực ngày tồn tại, Dấu niêm phong dùng một lần cung cấp thêm sự đảm bảo rằng **không có cam kết thay thế nào** có thể cùng tồn tại: bạn không thể đóng cùng một dấu niêm phong hai lần hoặc cố gắng thay thế tin nhắn đã niêm phong.

So sánh sau đây giúp hiểu rõ hơn nguyên tắc này:


- Cam kết mật mã (băm)**: Với hàm băm, bạn có thể cam kết với một phần dữ liệu (một số) bằng cách công bố băm của nó. Dữ liệu vẫn được giữ bí mật cho đến khi bạn tiết lộ hình ảnh trước, nhưng bạn có thể chứng minh rằng bạn đã biết trước;
- Dấu thời gian (chuỗi khối)**: Bằng cách chèn hàm băm này vào chuỗi khối, chúng tôi cũng chứng minh rằng chúng tôi biết nó tại một thời điểm chính xác (thời điểm đưa vào khối);
- Dấu niêm phong dùng một lần**: Với dấu niêm phong dùng một lần, chúng tôi tiến thêm một bước nữa bằng cách làm cho cam kết trở nên duy nhất. Với một băm duy nhất, bạn có thể tạo ra một số cam kết trái ngược nhau song song (vấn đề của bác sĩ thông báo "*Là con trai*" với gia đình và "*Là con gái*" trong nhật ký cá nhân của mình). Dấu niêm phong dùng một lần loại bỏ khả năng này bằng cách kết nối cam kết với phương tiện chứng minh công bố, chẳng hạn như chuỗi khối Bitcoin, để việc chi tiêu UTXO sẽ niêm phong cam kết một cách chắc chắn. Sau khi chi tiêu, cùng một UTXO không thể được chi tiêu lại để thay thế cam kết.

|                                                                                  | Cam kết đơn giản (tóm tắt/băm) | Dấu thời gian | Con dấu dùng một lần |
| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |
| Việc công bố cam kết không tiết lộ thông điệp                                   | Có                              | Có         | Có               |
| Chứng minh ngày cam kết / sự tồn tại của thông điệp trước một ngày nhất định    | Không thể                       | Có thể     | Có thể          |
| Chứng minh rằng không có cam kết thay thế nào có thể tồn tại                    | Không thể                       | Không thể  | Có thể          | |

Con dấu dùng một lần hoạt động theo ba giai đoạn chính:

**Định nghĩa của Seal:**


- Alice xác định trước các quy tắc để công bố con dấu (khi nào, ở đâu và bằng cách nào thông điệp sẽ được công bố);
- Bob chấp nhận hoặc thừa nhận những điều kiện này.

![RGB-Bitcoin](assets/fr/021.webp)

**Đóng kín :**


- Khi chạy, Alice đóng dấu bằng cách xuất bản thông báo thực tế (thường ở dạng _cam kết_, ví dụ như hàm băm);
- Nó cũng cung cấp một **bằng chứng** (bằng chứng mật mã) chứng minh rằng con dấu đã được đóng và không thể hủy ngang.

![RGB-Bitcoin](assets/fr/019.webp)

**Xác minh con dấu :**


- Sau khi niêm phong được đóng lại, Bob không thể mở nó ra nữa: anh ta chỉ có thể kiểm tra xem nó đã được đóng chưa;
- Bob thu thập con dấu, **nhân chứng** và thông điệp (hoặc cam kết của anh ấy) để đảm bảo rằng mọi thứ đều khớp nhau và không có con dấu cạnh tranh hoặc phiên bản khác nhau.

Quá trình này có thể được tóm tắt như sau:

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

Tuy nhiên, xác thực phía máy khách tiến xa hơn một bước nữa: nếu định nghĩa về con dấu nằm ngoài chuỗi khối, về mặt lý thuyết, có thể ai đó sẽ thách thức sự tồn tại hoặc tính hợp pháp của con dấu đang được đề cập. Để khắc phục vấn đề này, một chuỗi Con dấu sử dụng một lần liên kết được sử dụng:


- Mỗi con dấu đóng chứa định nghĩa của con dấu sau;
- Chúng tôi ghi lại các lần đóng này (cùng với _cam kết_ của chúng) trong chuỗi khối (trong giao dịch Bitcoin);
- Vì vậy, bất kỳ nỗ lực nào nhằm sửa đổi con dấu trước đó đều sẽ mâu thuẫn với lịch sử có trong Bitcoin.

Đây chính xác là những gì hệ thống RGB thực hiện:


- Các thông điệp được xuất bản là _cam kết_ đối với dữ liệu đã được xác thực ở phía máy khách;
- Định nghĩa con dấu có liên quan đến Bitcoin UTXO;
- Con dấu đóng lại khi UTXO này được chi tiêu hoặc khi một đầu ra mới được ghi có vào cùng một cam kết;
- Chuỗi giao dịch sử dụng các UTXO này tương ứng với bằng chứng công bố: mọi quá trình chuyển đổi hoặc thay đổi trạng thái trên RGB đều được neo trong Bitcoin.

Tóm lại:


- _Định nghĩa con dấu_ là UTXO mà bạn dự định đóng dấu một cam kết trong tương lai;
- _Đóng dấu_ xảy ra khi bạn chi tiêu UTXO này, tạo ra một giao dịch chứa cam kết;
- _Chứng cứ_ chính là giao dịch đó, chứng minh rằng bạn đã đóng dấu có nội dung này;
- Bạn không thể chứng minh rằng con dấu chưa được đóng (bạn không thể hoàn toàn chắc chắn rằng UTXO chưa được chi tiêu hoặc sẽ không được chi tiêu trong khối mà bạn chưa nhìn thấy), nhưng bạn có thể chứng minh rằng nó thực sự đã được đóng.

Tính duy nhất này rất quan trọng đối với Xác thực phía máy khách: khi bạn xác thực quá trình chuyển đổi trạng thái, bạn kiểm tra xem nó có tương ứng với UTXO duy nhất, chưa từng được chi tiêu trong cam kết cạnh tranh hay không. Đây là điều đảm bảo không có chi tiêu gấp đôi trong các hợp đồng thông minh ngoài chuỗi.

### Nhiều cam kết và gốc rễ

Một hợp đồng thông minh RGB có thể cần sử dụng nhiều Dấu niêm phong sử dụng một lần (nhiều UTXO) cùng một lúc. Hơn nữa, một giao dịch Bitcoin đơn lẻ có thể tham chiếu đến nhiều hợp đồng riêng biệt, mỗi hợp đồng niêm phong trạng thái chuyển đổi riêng của nó. Điều này đòi hỏi một cơ chế **đa cam kết** để chứng minh, một cách xác định và duy nhất, rằng không có cam kết nào tồn tại trùng lặp. Đây là nơi khái niệm **mỏ neo** phát huy tác dụng trong RGB: một cấu trúc đặc biệt liên kết một giao dịch Bitcoin và một hoặc nhiều cam kết phía máy khách (chuyển đổi trạng thái), mỗi cam kết có khả năng thuộc về một hợp đồng khác nhau. Chúng ta sẽ xem xét kỹ hơn khái niệm này trong chương tiếp theo.

![RGB-Bitcoin](assets/fr/023.webp)

Hai kho lưu trữ GitHub chính của dự án (thuộc tổ chức LNPBP) nhóm các triển khai cơ bản của các khái niệm đã nghiên cứu trong chương đầu tiên:


- client_side_validation**: Chứa các nguyên hàm Rust để xác thực cục bộ;
- single_use_seals**: Triển khai logic để xác định và đóng các niêm phong này một cách an toàn.

![RGB-Bitcoin](assets/fr/020.webp)

Lưu ý rằng các khối phần mềm này không phụ thuộc vào Bitcoin; về mặt lý thuyết, chúng có thể được áp dụng cho bất kỳ phương tiện chứng minh xuất bản nào khác (một sổ đăng ký khác, một tạp chí, v.v.). Trên thực tế, RGB dựa vào Bitcoin vì tính mạnh mẽ và sự đồng thuận rộng rãi của nó.

![RGB-Bitcoin](assets/fr/021.webp)

### Câu hỏi từ công chúng

#### Hướng tới việc sử dụng rộng rãi hơn các con dấu dùng một lần

Peter Todd cũng đã tạo ra giao thức _Open Timestamps_ và khái niệm Single-use Seal là sự mở rộng tự nhiên của những ý tưởng này. Ngoài RGB, có thể hình dung ra các trường hợp sử dụng khác, chẳng hạn như việc xây dựng _sidechains_ mà không cần dùng đến _merge mining_ hoặc các đề xuất liên quan đến drivechain như BIP300. Về nguyên tắc, bất kỳ hệ thống nào yêu cầu một cam kết duy nhất đều có thể khai thác nguyên thủy mật mã này. Ngày nay, RGB là triển khai toàn diện lớn đầu tiên.

#### Các vấn đề về tính khả dụng của dữ liệu

Vì trong Xác thực phía máy khách, mỗi người dùng lưu trữ phần lịch sử của riêng mình, nên tính khả dụng của dữ liệu không được đảm bảo trên toàn cầu. Nếu bên phát hành hợp đồng giữ lại hoặc thu hồi một số thông tin nhất định, bạn có thể không biết về sự phát triển thực tế của ưu đãi. Trong một số trường hợp (chẳng hạn như stablecoin), bên phát hành được kỳ vọng sẽ duy trì dữ liệu công khai để chứng minh khối lượng đang lưu hành, nhưng không có nghĩa vụ kỹ thuật nào phải làm như vậy. Do đó, có thể thiết kế các hợp đồng cố tình không minh bạch với nguồn cung không giới hạn, điều này đặt ra câu hỏi về lòng tin.

#### Phân mảnh và cô lập hợp đồng

Mỗi hợp đồng đại diện cho một _shard_ riêng biệt: USDT và USDC, ví dụ, không phải chia sẻ lịch sử của chúng. Hoán đổi nguyên tử vẫn có thể thực hiện được, nhưng điều này không liên quan đến việc hợp nhất sổ đăng ký của chúng. Mọi thứ đều được thực hiện bằng cam kết mật mã, mà không tiết lộ toàn bộ biểu đồ lịch sử cho từng người tham gia.

### Phần kết luận

Chúng ta đã thấy khái niệm Xác thực phía máy khách phù hợp với blockchain và _kênh trạng thái_ như thế nào, cách nó phản ứng với bộ ba điện toán phân tán và cách nó tận dụng blockchain Bitcoin một cách độc đáo để tránh chi tiêu gấp đôi và để *đóng dấu thời gian*. Ý tưởng này dựa trên khái niệm **Dấu niêm phong sử dụng một lần**, cho phép tạo ra các cam kết duy nhất mà bạn không thể chi tiêu lại theo ý muốn. Theo cách này, mỗi người tham gia chỉ tải lên lịch sử thực sự cần thiết, tăng khả năng mở rộng và tính bảo mật của hợp đồng thông minh trong khi vẫn giữ được tính bảo mật của Bitcoin làm nền tảng.

Bước tiếp theo sẽ là giải thích chi tiết hơn về cách cơ chế Single-use Seal này được áp dụng trong Bitcoin (thông qua UTXO), cách tạo và xác thực các neo, sau đó là cách xây dựng hợp đồng thông minh hoàn chỉnh trong RGB. Cụ thể, chúng ta sẽ xem xét vấn đề về nhiều cam kết, thách thức kỹ thuật trong việc chứng minh rằng một giao dịch Bitcoin đồng thời niêm phong nhiều trạng thái chuyển đổi trong các hợp đồng khác nhau, mà không gây ra lỗ hổng hoặc cam kết kép.

Trước khi đi sâu vào các chi tiết kỹ thuật hơn của chương thứ hai, bạn có thể thoải mái đọc lại các định nghĩa chính (Xác thực phía máy khách, Dấu niêm phong dùng một lần, mỏ neo, v.v.) và ghi nhớ logic chung: chúng tôi đang tìm cách dung hòa các điểm mạnh của chuỗi khối Bitcoin (bảo mật, phi tập trung, đóng dấu thời gian) với các giải pháp ngoài chuỗi (tốc độ, tính bảo mật, khả năng mở rộng) và đây chính xác là những gì RGB và Xác thực phía máy khách đang cố gắng đạt được.

## Lớp cam kết

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

Trong chương này, chúng ta sẽ xem xét việc triển khai Xác thực phía máy khách và Dấu niêm phong sử dụng một lần trong chuỗi khối Bitcoin. Chúng tôi sẽ trình bày các nguyên tắc chính của **lớp cam kết** (lớp 1) của RGB, đặc biệt tập trung vào lược đồ **TxO2** mà RGB sử dụng để xác định và đóng dấu niêm phong trong giao dịch Bitcoin. Tiếp theo, chúng ta sẽ thảo luận về hai điểm quan trọng chưa được đề cập chi tiết:


- _Những cam kết mang tính quyết định của Bitcoin_;
- Cam kết đa giao thức.

Sự kết hợp của những khái niệm này cho phép chúng ta chồng nhiều hệ thống hoặc hợp đồng lên một UTXO duy nhất và do đó là một blockchain duy nhất.

Cần nhớ rằng các hoạt động mã hóa được mô tả có thể được áp dụng, theo nghĩa tuyệt đối, cho các blockchain hoặc phương tiện xuất bản khác, nhưng các đặc điểm của Bitcoin (về mặt phi tập trung, chống kiểm duyệt và cởi mở với tất cả mọi người) khiến nó trở thành nền tảng lý tưởng để phát triển khả năng lập trình nâng cao như khả năng mà **RGB** yêu cầu.

### Các chương trình cam kết trong Bitcoin và việc sử dụng chúng của RGB

Như chúng ta đã thấy trong chương đầu tiên của khóa học, Dấu niêm phong dùng một lần là một khái niệm chung: chúng ta hứa sẽ đưa cam kết (_cam kết_) vào một vị trí cụ thể của giao dịch và vị trí này hoạt động như một dấu niêm phong mà chúng ta đóng trên một thông điệp. Tuy nhiên, trên chuỗi khối Bitcoin, có một số tùy chọn để chọn nơi đặt _cam kết_ này.

Để hiểu logic, chúng ta hãy nhớ lại nguyên tắc cơ bản: để đóng _con dấu sử dụng một lần_, chúng ta sử dụng vùng đã niêm phong bằng cách chèn _cam kết_ vào một thông điệp nhất định. Trong Bitcoin, điều này có thể được thực hiện theo một số cách:


- Sử dụng khóa công khai hoặc địa chỉ**

Chúng ta có thể quyết định rằng một khóa công khai hoặc địa chỉ cụ thể là _con dấu sử dụng một lần_. Ngay khi khóa hoặc địa chỉ này xuất hiện trên chuỗi trong một giao dịch, điều đó có nghĩa là con dấu được đóng lại bằng một thông báo nhất định.


- Sử dụng đầu ra giao dịch Bitcoin**

Điều này có nghĩa là _con dấu sử dụng một lần_ được định nghĩa là _outpoint_ chính xác (một cặp TXID + số đầu ra). Ngay khi _outpoint_ này được sử dụng hết, con dấu sẽ được đóng lại.

Trong khi làm việc trên RGB, chúng tôi đã xác định được ít nhất 4 cách khác nhau để triển khai các con dấu này trên Bitcoin:


- Xác định con dấu thông qua khóa công khai và đóng nó trong _output_;
- Xác định dấu niêm phong bằng _outpoint_ và đóng nó bằng _output_;
- Xác định con dấu thông qua giá trị của khóa công khai và đóng nó trong _input_;
- Xác định dấu niêm phong thông qua _outpoint_ và đóng nó trong _input_.

| Tên sơ đồ    | Định nghĩa niêm phong      | Đóng niêm phong       | Yêu cầu bổ sung                                                | Ứng dụng chính               | Các sơ đồ cam kết có thể có   |
| ------------ | ------------------------- | --------------------- | -------------------------------------------------------------- | ---------------------------- | ------------------------------ |
| PkO          | Giá trị của khóa công khai | Đầu ra giao dịch      | P2(W)PKH                                                       | Hiện tại chưa có             | Keytweak, taptweak, opret      |
| TxO2         | Đầu ra giao dịch          | Đầu ra giao dịch      | Yêu cầu các cam kết xác định trên Bitcoin                      | RGBv1 (phổ quát)             | Keytweak, tapret, opret        |
| PkI          | Giá trị của khóa công khai | Đầu vào giao dịch     | Chỉ hỗ trợ Taproot & không tương thích với ví Legacy          | Danh tính dựa trên Bitcoin   | Sigtweak, witweak              |
| TxO1         | Đầu ra giao dịch          | Đầu vào giao dịch     | Chỉ hỗ trợ Taproot & không tương thích với ví Legacy          | Hiện tại chưa có             | Sigtweak, witweak              |


Chúng tôi sẽ không đi sâu vào từng cấu hình này, vì trong RGB, chúng tôi đã chọn sử dụng **một _outpoint_ làm định nghĩa của seal** và đặt _commitment_ vào đầu ra của giao dịch chi tiêu _outpoint_ này. Do đó, chúng tôi có thể giới thiệu các khái niệm sau cho phần tiếp theo:


- "Định nghĩa con dấu "**: Một _điểm ra_ nhất định (được xác định bởi TXID + số đầu ra) ;
- "Đóng dấu"**: Giao dịch chi tiêu _outpoint_ này, trong đó _cam kết_ được thêm vào tin nhắn.

Sơ đồ này được chọn vì tính tương thích của nó với kiến trúc RGB, nhưng các cấu hình khác có thể hữu ích cho những mục đích sử dụng khác nhau.

"O2" trong "TxO2" nhắc nhở chúng ta rằng cả định nghĩa và đóng đều dựa trên chi phí (hoặc tạo ra) của đầu ra giao dịch.

### Ví dụ về sơ đồ TxO2

Xin nhắc lại, việc xác định _con dấu sử dụng một lần_ không nhất thiết phải yêu cầu công bố giao dịch trên chuỗi. Ví dụ, đối với Alice, chỉ cần có một UTXO chưa sử dụng là đủ. Cô ấy có thể quyết định: "_Điểm ra_ này (đã tồn tại) hiện là con dấu của tôi". Cô ấy ghi chú điều này tại địa phương (_phía máy khách_) và cho đến khi UTXO này được sử dụng, con dấu được coi là mở.

![RGB-Bitcoin](assets/fr/024.webp)

Vào ngày muốn đóng dấu (để báo hiệu một sự kiện hoặc neo một thông điệp cụ thể), nó sẽ sử dụng UTXO này trong một giao dịch mới (giao dịch này thường được gọi là "_giao dịch chứng kiến_" (không liên quan đến _segwit_, đó chỉ là thuật ngữ chúng tôi đặt cho nó). Giao dịch mới này sẽ chứa _cam kết_ cho thông điệp.

![RGB-Bitcoin](assets/fr/025.webp)

Lưu ý rằng trong ví dụ này:


- Không ai ngoài Bob (hoặc những người mà Alice chọn tiết lộ toàn bộ bằng chứng) biết rằng có một thông điệp nhất định được ẩn trong giao dịch này;
- Mọi người đều có thể thấy rằng _outpoint_ đã được chi tiêu, nhưng chỉ có Bob mới nắm giữ bằng chứng cho thấy thông điệp thực sự được neo trong giao dịch.

Để minh họa cho sơ đồ TxO2 này, chúng ta có thể sử dụng _con dấu sử dụng một lần_ làm cơ chế để thu hồi khóa PGP. Thay vì công bố chứng chỉ thu hồi trên máy chủ, Alice có thể nói: "Đầu ra Bitcoin này, nếu được chi tiêu, có nghĩa là khóa PGP của tôi đã bị thu hồi".

Do đó, Alice có một UTXO cụ thể, trong đó một trạng thái hoặc dữ liệu nhất định (chỉ cô ấy biết) được liên kết cục bộ (ở phía máy khách).

Alice thông báo cho Bob rằng nếu UTXO này được chi tiêu, một sự kiện cụ thể sẽ được coi là đã xảy ra. Từ bên ngoài, tất cả những gì chúng ta thấy là một giao dịch Bitcoin; nhưng Bob biết rằng khoản chi tiêu này có một ý nghĩa ẩn.

![RGB-Bitcoin](assets/fr/026.webp)

Khi Alice sử dụng UTXO này, cô ấy đóng niêm phong trên một thông báo cho biết khóa mới của mình hoặc đơn giản là thu hồi khóa cũ. Theo cách này, bất kỳ ai theo dõi on-chain sẽ thấy UTXO đã được sử dụng, nhưng chỉ những người có bằng chứng đầy đủ mới biết rằng đó chính xác là việc thu hồi khóa PGP.

![RGB-Bitcoin](assets/fr/027.webp)

Để Bob hoặc bất kỳ ai khác có liên quan có thể kiểm tra tin nhắn ẩn, Alice phải cung cấp cho anh ta thông tin ngoài chuỗi.

![RGB-Bitcoin](assets/fr/028.webp)

Do đó, Alice phải cung cấp cho Bob:


- Bản thân thông báo (ví dụ: khóa PGP mới);
- Bằng chứng mật mã chứng minh rằng tin nhắn có liên quan đến giao dịch (được gọi là _bằng chứng giao dịch bổ sung_ hoặc _mỏ neo_).

![RGB-Bitcoin](assets/fr/029.webp)

Bên thứ ba không có thông tin này. Họ chỉ thấy rằng UTXO đã được chi tiêu. Do đó, tính bảo mật được đảm bảo.

Để làm rõ cấu trúc, chúng ta hãy tóm tắt quy trình thành hai giao dịch:


- Giao dịch 1**: Giao dịch này chứa _định nghĩa dấu niêm phong_, tức là _điểm ra_ sẽ đóng vai trò là dấu niêm phong.

![RGB-Bitcoin](assets/fr/031.webp)


- Giao dịch 2**: Chi tiêu _outpoint_ này. Thao tác này đóng dấu và, trong cùng giao dịch, chèn _cam kết_ vào tin nhắn.

![RGB-Bitcoin](assets/fr/033.webp)

Do đó, chúng tôi gọi giao dịch thứ hai là "_giao dịch chứng kiến_".

Để minh họa điều này từ một góc độ khác, chúng ta có thể biểu diễn hai lớp:


- Lớp trên cùng (chuỗi khối, công khai)**: mọi người đều thấy giao dịch và biết rằng _điểm ra_ đã được chi tiêu;
- Lớp dưới (phía máy khách, riêng tư)**: chỉ Alice (hoặc người có liên quan) biết rằng khoản chi này tương ứng với thông điệp này thông qua bằng chứng mật mã và thông điệp mà cô ấy lưu giữ cục bộ.

![RGB-Bitcoin](assets/fr/034.webp)

Nhưng khi đóng dấu, câu hỏi đặt ra là nên chèn _cam kết_ vào đâu

Trong phần trước, chúng tôi đã đề cập ngắn gọn về cách mô hình Xác thực phía máy khách có thể được áp dụng cho RGB và các hệ thống khác. Ở đây, chúng tôi giải quyết phần về **cam kết Bitcoin xác định** và cách tích hợp chúng vào giao dịch. Ý tưởng là để hiểu lý do tại sao chúng tôi cố gắng chèn một cam kết duy nhất vào _giao dịch chứng kiến_ và trên hết là cách đảm bảo rằng không có cam kết cạnh tranh nào khác không được tiết lộ.

### Vị trí cam kết trong một giao dịch

Khi bạn cung cấp cho ai đó bằng chứng rằng một thông điệp nhất định được nhúng trong giao dịch, bạn cần có khả năng đảm bảo rằng không có hình thức cam kết nào khác (một thông điệp ẩn thứ hai) trong cùng một giao dịch mà bạn chưa được tiết lộ. Để xác thực phía máy khách vẫn mạnh mẽ, bạn cần một cơ chế **xác định** để đặt một _cam kết_ duy nhất trong giao dịch đóng _dấu niêm phong sử dụng một lần_.

_Giao dịch chứng kiến_ chi tiêu UTXO nổi tiếng (hoặc _định nghĩa con dấu_) và khoản chi tiêu này tương ứng với việc đóng con dấu. Về mặt kỹ thuật, chúng ta biết rằng mỗi điểm ra chỉ có thể được chi tiêu một lần. Đây chính xác là điều củng cố khả năng chống lại chi tiêu gấp đôi của Bitcoin. Nhưng giao dịch chi tiêu có thể có nhiều _đầu vào_, nhiều _đầu ra_ hoặc được tạo thành theo cách phức tạp (coinjoin, kênh Lightning, v.v.). Do đó, chúng ta cần xác định rõ ràng nơi chèn _cam kết_ vào cấu trúc này, một cách rõ ràng và thống nhất.

Bất kể phương pháp nào (PkO, TxO2, v.v.), _cam kết_ đều có thể được chèn vào:


- Trong Đầu vào** qua:
    - Sigtweak** (sửa đổi thành phần `r` của chữ ký ECDSA, tương tự như nguyên tắc "Ký hợp đồng");
    - Witweak** (dữ liệu chứng thực _được phân tách_ của giao dịch được sửa đổi).
- Trong Đầu ra** thông qua:
    - Keytweak** (khóa công khai của người nhận được "điều chỉnh" bằng tin nhắn);
    - Opret** (tin nhắn được đặt trong đầu ra không thể chi tiêu `OP_RETURN`);
    - Tapret** (hay _Taptweak_), dựa vào taproot để chèn cam kết vào phần tập lệnh của khóa taproot, do đó sửa đổi khóa công khai một cách xác định.

![RGB-Bitcoin](assets/fr/035.webp)

Sau đây là thông tin chi tiết về từng phương pháp:

![RGB-Bitcoin](assets/fr/038.webp)

***Điều chỉnh chữ ký (ký hợp đồng) :***

Một kế hoạch trước đó liên quan đến việc khai thác phần ngẫu nhiên của chữ ký (ECDSA hoặc Schnorr) để nhúng _cam kết_: đây là kỹ thuật được gọi là "**Sign-to-contract**". Bạn thay thế nonce được tạo ngẫu nhiên bằng hàm băm chứa dữ liệu. Theo cách này, chữ ký ngầm tiết lộ cam kết của bạn, mà không cần bất kỳ khoảng trống bổ sung nào trong giao dịch. Cách tiếp cận này có một số lợi thế:


- Không có tình trạng quá tải trên chuỗi (bạn sử dụng cùng một vị trí như nonce cơ bản);
- Về mặt lý thuyết, điều này có thể khá rời rạc vì nonce ban đầu là một dữ liệu ngẫu nhiên.

Tuy nhiên, 2 nhược điểm lớn đã xuất hiện:


- Multisig trước Taproot: khi bạn có nhiều người ký, bạn cần quyết định chữ ký nào sẽ mang _cam kết_. Chữ ký có thể được sắp xếp theo thứ tự khác nhau và nếu một người ký từ chối, bạn sẽ mất quyền kiểm soát kết quả của _cam kết_;
- MuSig và nonce được chia sẻ: với Schnorr multisig (*MuSig*), việc tạo nonce là một thuật toán đa bên và việc điều chỉnh nonce riêng lẻ trở nên hầu như không thể.

Trên thực tế, **sig tweak** cũng không tương thích lắm với phần cứng hiện có (ví phần cứng) và định dạng (Lightning, v.v.). Vì vậy, ý tưởng tuyệt vời này khó có thể đưa vào thực tế.

***Điều chỉnh chính (trả tiền theo hợp đồng) :***

**Điều chỉnh khóa** sử dụng khái niệm lịch sử về _pay-to-contract_. Chúng tôi lấy khóa công khai `X` và điều chỉnh nó bằng cách thêm giá trị `H(message)`. Cụ thể, nếu `X = x * G` và `h = H(message)`, thì khóa mới sẽ là `X' = X + h * G`. Khóa điều chỉnh này ẩn cam kết với `message`. Người giữ khóa riêng ban đầu có thể, bằng cách thêm `h` vào khóa riêng `x` của mình, chứng minh rằng anh ta có khóa để chi tiêu đầu ra. Về mặt lý thuyết, điều này rất thanh lịch, bởi vì:


- _Cam kết_ được nhập mà không cần thêm bất kỳ trường bổ sung nào;
- Bạn không lưu trữ bất kỳ dữ liệu bổ sung nào trên chuỗi.

Tuy nhiên, trên thực tế, chúng ta gặp phải những khó khăn sau:


- Ví không còn nhận dạng được khóa công khai chuẩn nữa vì nó đã bị "điều chỉnh", do đó chúng không thể dễ dàng liên kết UTXO với khóa thông thường của bạn;
- Ví phần cứng không được thiết kế để ký bằng khóa không có nguồn gốc từ khóa chuẩn của chúng;
- Bạn cần phải điều chỉnh kịch bản, mô tả, v.v. của mình.

Trong bối cảnh RGB, con đường này được hình dung cho đến năm 2021, nhưng nó tỏ ra quá phức tạp để có thể hoạt động với các tiêu chuẩn và cơ sở hạ tầng hiện tại.

***Điều chỉnh nhân chứng :***

Một ý tưởng khác, mà một số giao thức như _inscriptions Ordinals_ đã đưa vào thực hành, là đặt dữ liệu trực tiếp vào phần `witness` của giao dịch (do đó có cụm từ "witness tweak"). Tuy nhiên, phương pháp này:


- Làm cho sự tương tác được nhìn thấy ngay lập tức (bạn thực sự dán dữ liệu thô vào nhân chứng);
- Có thể bị kiểm duyệt (thợ đào hoặc nút có thể từ chối chuyển tiếp nếu nó quá lớn hoặc có bất kỳ đặc điểm tùy ý nào khác);
- Chiếm không gian trong các khối, trái với mục tiêu kín đáo và nhẹ nhàng của RGB.

Ngoài ra, witness được thiết kế để có thể cắt xén trong một số bối cảnh nhất định, điều này có thể khiến việc có được bằng chứng mạnh mẽ trở nên phức tạp hơn.

***Trả lời mở (opret) :***

Rất đơn giản trong hoạt động của nó, `OP_RETURN` cho phép bạn lưu trữ một hàm băm hoặc tin nhắn trong một trường đặc biệt của giao dịch. Nhưng nó có thể phát hiện ngay lập tức: mọi người đều thấy rằng có một _cam kết_ trong giao dịch và nó có thể bị kiểm duyệt hoặc loại bỏ, cũng như thêm đầu ra bổ sung. Vì điều này làm tăng tính minh bạch và kích thước, nên nó được coi là ít thỏa đáng hơn theo quan điểm của giải pháp Xác thực phía Máy khách.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

Tùy chọn cuối cùng là sử dụng **Taproot** (được giới thiệu với BIP341) với sơ đồ *Tapret*. *Tapret* là một hình thức cam kết xác định phức tạp hơn, mang lại những cải tiến về dấu chân trên blockchain và tính bảo mật cho các hoạt động hợp đồng. Ý tưởng chính là ẩn cam kết trong phần `Script Path Spend` của [giao dịch taproot](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/fr/036.webp)

Trước khi mô tả cách cam kết được chèn vào giao dịch taproot, chúng ta hãy xem **hình thức chính xác** của cam kết, **bắt buộc** phải tương ứng với chuỗi 64 byte [được xây dựng](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) như sau:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- 29 byte `OP_RESERVED`, theo sau là `OP_RETURN`, rồi `OP_PUSHBYTE_33`, tạo thành phần _prefix_ 31 byte;
- Tiếp theo là _cam kết_ 32 byte (thường là gốc Merkle từ **MPC**), chúng ta thêm 1 byte **Nonce** (tổng cộng là 33 byte cho phần thứ hai này).

Vì vậy, phương thức `Tapret` 64 byte trông giống như `Opret` mà chúng ta đã thêm tiền tố 29 byte `OP_RESERVED` và thêm một byte bổ sung làm Nonce.

Để duy trì tính linh hoạt về mặt triển khai, tính bảo mật và khả năng mở rộng, chương trình Tapret sẽ tính đến nhiều trường hợp sử dụng khác nhau, tùy thuộc vào yêu cầu:


- Việc kết hợp duy nhất cam kết Tapret vào giao dịch taproot mà không có cấu trúc Script Path có sẵn;
- Tích hợp cam kết Tapret vào giao dịch Taproot đã được trang bị Đường dẫn tập lệnh.

Chúng ta hãy xem xét kỹ hơn từng tình huống trong hai tình huống này.

#### Kết hợp Tapret mà không có Script Path hiện có

Trong trường hợp đầu tiên này, chúng ta bắt đầu từ khóa đầu ra taproot (*Khóa đầu ra Taproot*) `Q` chỉ chứa khóa công khai nội bộ `P` *(Khóa nội bộ*), không có đường dẫn tập lệnh liên quan (*Đường dẫn tập lệnh*):

![RGB-Bitcoin](assets/fr/047.webp)


- `P`: khóa công khai nội bộ cho _Key Path Spend_.
- `G`: điểm tạo nên đường cong elip [secp256k1](https://en.bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` là hệ số điều chỉnh, được tính toán thông qua _băm được gắn thẻ_ (ví dụ: `SHA-256(SHA-256(TapTweak) || P)`), theo [BIP86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). Điều này chứng tỏ không có tập lệnh ẩn nào.

Để bao gồm cam kết **Tapret**, hãy thêm **Chi tiêu đường dẫn tập lệnh** với **tập lệnh duy nhất**, như sau:

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)` sau đó trở thành hệ số điều chỉnh mới, bao gồm **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` biểu thị gốc của **script** này, về cơ bản là một hàm băm có kiểu `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

Bằng chứng về tính bao gồm và tính duy nhất trong cây rễ cái ở đây được tóm gọn lại bằng khóa công khai nội bộ duy nhất `P`.

#### Tích hợp Tapret vào Script Path đã có sẵn

Kịch bản thứ hai liên quan đến đầu ra `Q` taproot** phức tạp hơn, vốn đã chứa một số tập lệnh. Ví dụ, chúng ta có một cây gồm 3 tập lệnh:

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` chỉ định hàm băm được gắn thẻ chuẩn hóa của một tập lệnh lá.
- a, B, C` biểu diễn các tập lệnh đã có trong cấu trúc taproot.

Để thêm cam kết Tapret, chúng ta cần chèn một *tập lệnh không thể chi tiêu* ở cấp độ đầu tiên của cây, dịch chuyển các tập lệnh hiện có xuống một cấp độ. Về mặt trực quan, cây trở thành:

![RGB-Bitcoin](assets/fr/050.webp)


- tHABC` biểu thị băm được gắn thẻ của nhóm cấp cao nhất `A, B, C`.
- tHT` biểu thị hàm băm của tập lệnh tương ứng với `Tapret` 64 byte.

Theo quy tắc rễ cọc, mỗi nhánh/lá phải được kết hợp theo thứ tự băm từ điển. Có hai trường hợp có thể xảy ra:


- `tHT` > `tHABC`: cam kết Tapret di chuyển sang bên phải của cây. Bằng chứng duy nhất chỉ cần `tHABC` và `P`;
- tHT` < `tHABC`**: cam kết Tapret được đặt ở bên trái. Để chứng minh rằng không có cam kết Tapret nào khác ở bên phải, `tHAB` và `tHC` phải được tiết lộ để chứng minh sự vắng mặt của bất kỳ tập lệnh nào khác như vậy.

Ví dụ trực quan cho trường hợp đầu tiên (`tHABC < tHT`):

![RGB-Bitcoin](assets/fr/051.webp)

Ví dụ cho trường hợp thứ hai (`tHABC > tHT`):

![RGB-Bitcoin](assets/fr/052.webp)

#### Tối ưu hóa với nonce

Để cải thiện tính bảo mật, chúng ta có thể "khai thác" (một thuật ngữ chính xác hơn sẽ là "bruteforce") giá trị của `<Nonce>` (byte cuối cùng của `Tapret` 64 byte) trong nỗ lực để có được hàm băm `tHT` sao cho `tHABC < tHT`. Trong trường hợp này, cam kết được đặt ở bên phải, giúp người dùng không phải tiết lộ toàn bộ nội dung của các tập lệnh hiện có để chứng minh tính duy nhất của Tapret.

Tóm lại, `Tapret` cung cấp một cách riêng biệt và xác định để kết hợp cam kết vào giao dịch taproot, đồng thời tôn trọng yêu cầu về tính duy nhất và rõ ràng cần thiết cho logic Xác thực phía máy khách và Dấu niêm phong sử dụng một lần của RGB.

#### Lối thoát hợp lệ

Đối với các giao dịch cam kết RGB, yêu cầu chính đối với một chương trình cam kết Bitcoin hợp lệ như sau: Giao dịch (*giao dịch chứng kiến*) phải chứng minh được là chứa một cam kết duy nhất. Yêu cầu này khiến không thể xây dựng lịch sử thay thế cho dữ liệu được xác thực phía máy khách trong cùng một giao dịch. Điều này có nghĩa là thông điệp xung quanh _dấu niêm phong sử dụng một lần_ là duy nhất.

Để đáp ứng nguyên tắc này, và bất kể số lượng đầu ra trong một giao dịch, chúng tôi yêu cầu **một và chỉ một đầu ra** có thể chứa một cam kết (*cam kết*). Đối với mỗi lược đồ được sử dụng (*Opret* hoặc *Tapret*), các đầu ra hợp lệ duy nhất có thể chứa một _cam kết_ RGB là:


- Đầu ra đầu tiên `OP_RETURN` (nếu có) cho lược đồ *Opret*;
- Đầu ra rễ cái đầu tiên (nếu có) cho lược đồ *Tapret*.

Lưu ý rằng một giao dịch hoàn toàn có thể chứa một cam kết `Opret` và một cam kết `Tapret` trong hai đầu ra riêng biệt. Nhờ bản chất xác định của Seal Definition, hai cam kết này sau đó tương ứng với hai phần dữ liệu riêng biệt được xác thực ở phía máy khách.

### Phân tích và lựa chọn thực tế trong RGB

Khi chúng tôi bắt đầu RGB, chúng tôi đã xem xét tất cả các phương pháp này để xác định nơi và cách đặt _cam kết_ trong giao dịch theo cách xác định. Chúng tôi đã xác định một số tiêu chí:


- Khả năng tương thích với nhiều tình huống khác nhau (ví dụ: đa chữ ký, Lightning, ví phần cứng, v.v.);
- Tác động đến không gian trên chuỗi;
- Khó khăn trong việc triển khai và bảo trì;
- Tính bảo mật và chống kiểm duyệt.


| Phương pháp                                        | Dấu vết và kích thước on-chain | Kích thước phía client | Tích hợp ví | Tương thích phần cứng | Tương thích Lightning | Tương thích Taproot |
| -------------------------------------------------- | ------------------------------ | ---------------------- | ------------- | ---------------------- | ---------------------- | ---------------------- |
| Keytweak (P2C xác định)                            | 🟢                              | 🟡                       | 🔴                          | 🟠                        | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🟢 MuSig  |
| Sigtweak (S2C xác định)                            | 🟢                              | 🟢                       | 🟠                          | 🔴                        | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🔴 MuSig  |
| Opret (OP_RETURN)                                  | 🔴                              | 🟢                       | 🟢                          | 🟠                        | 🔴 BOLT, 🟠 Bifrost     | -                     |
| Thuật toán Tapret : nút trên cùng bên trái        | 🟠                              | 🔴                       | 🟠                          | 🟢                        | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Thuật toán Tapret #4 : bất kỳ nút nào + bằng chứng | 🟢                              | 🟠                       | 🟠                          | 🟢                        | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |

| Lược đồ cam kết xác định                              | Tiêu chuẩn    | Chi phí on-chain                                                                                                          | Kích thước bằng chứng phía client                                                                                     |
| ------------------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| Keytweak (P2C xác định)                               | LNPBP-1, 2    | 0 bytes                                                                                                                  | 33 bytes (khóa chưa chỉnh sửa)                                                                                       |
| Sigtweak (S2C xác định)                               | WIP (LNPBP-39)| 0 bytes                                                                                                                  | 0 bytes                                                                                                              |
| Opret (OP_RETURN)                                     | -             | 36 (v)bytes (TxOut bổ sung)                                                                                             | 0 bytes                                                                                                              |
| Thuật toán Tapret : nút trên cùng bên trái           | LNPBP-6       | 32 bytes trong nhân chứng (8 vbytes) trên bất kỳ multisig n-of-m nào và chi tiêu theo đường dẫn script                 | 0 bytes trên scriptless scripts taproot ~270 bytes trong trường hợp script duy nhất, ~128 bytes nếu có nhiều script |
| Thuật toán Tapret #4 : bất kỳ nút nào + bằng chứng   | LNPBP-6       | 32 bytes trong nhân chứng (8 vbytes) cho các trường hợp script duy nhất, 0 bytes trong nhân chứng trong hầu hết các trường hợp khác | 0 bytes trên scriptless scripts taproot, 65 bytes cho đến khi Taptree có khoảng một chục script                      |

| Lớp                          | Chi phí on-chain (bytes/vbytes) | Chi phí on-chain (bytes/vbytes) | Chi phí on-chain (bytes/vbytes) | Chi phí on-chain (bytes/vbytes) | Chi phí on-chain (bytes/vbytes) | Chi phí phía client (bytes) | Chi phí phía client (bytes) | Chi phí phía client (bytes) | Chi phí phía client (bytes) | Chi phí phía client (bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| **Loại**                       | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**               | **Tapret #4**            | **Keytweak**             | **Sigtweak**             | **Opret**                |
| Single-sig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | 0?                       | 0                        |
| MuSig (n-of-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | ? > 0                    | 0                        |
| Multi-sig 2-of-3               | 32/8                         | 32/8 hoặc 0                   | 0                            | n/a                          | 32                           | ~270                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 3-of-5               | 32/8                         | 32/8 hoặc 0                   | 0                            | n/a                          | 32                           | ~340                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 2-of-3 với timeouts  | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                       | 65                       | 32                       | n/a                      | 0                        |

| Lớp                              | Chi phí on-chain (vbytes) | Chi phí on-chain (vbytes) | Chi phí on-chain (vbytes) | Chi phí phía client (bytes) | Chi phí phía client (bytes) |
| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |
| **Loại**                         | **Cơ bản**             | **Tapret #2**          | **Tapret #4**          | **Tapret #2**            | **Tapret #4**            |
| MuSig (n-of-n)                   | 16.5                   | 0                      | 0                      | 0                        | 0                        |
| FROST (n-of-m)                   | ?                      | 0                      | 0                      | 0                        | 0                        |
| Multi_a (n-of-m)                 | 1+16n+8m               | 8                      | 8                      | 33 * m                   | 65                       |
| Nhánh MuSig / Multi_a (n-of-m)   | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| Với timeouts (n-of-m)            | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |

| Phương pháp                                 | Bảo mật và khả năng mở rộng | Tính tương tác | Tương thích | Di động | Độ phức tạp |
| ------------------------------------------- | -------------------------- | -------------- | ----------- | ------- | ----------- |
| Keytweak (P2C xác định)                     | 🟢                         | 🔴             | 🔴          | 🟡      | 🟡         |
| Sigtweak (S2C xác định)                     | 🟢                         | 🔴             | 🔴          | 🟢      | 🔴         |
| Opret (OP_RETURN)                           | 🔴                         | 🟠             | 🔴          | 🟢      | 🟢         |
| Thuật toán Tapret : nút trên cùng bên trái  | 🟠                         | 🟢             | 🟢          | 🔴      | 🟠         |
| Thuật toán Tapret #4 : Nút bất kỳ + bằng chứng | 🟢                         | 🟢             | 🟢          | 🟠      | 🔴         |



Trong quá trình nghiên cứu, rõ ràng là không có chương trình cam kết nào hoàn toàn tương thích với tiêu chuẩn Lightning hiện tại (không sử dụng Taproot, _muSig2_ hoặc hỗ trợ _cam kết_ bổ sung). Các nỗ lực đang được tiến hành để sửa đổi cấu trúc kênh của Lightning (*BiFrost*) để cho phép chèn các cam kết RGB. Đây là một lĩnh vực khác mà chúng ta cần xem xét lại cấu trúc giao dịch, các khóa và cách thức ký các bản cập nhật kênh.

Phân tích cho thấy, trên thực tế, các phương pháp khác (điều chỉnh khóa, điều chỉnh chữ ký, điều chỉnh chứng kiến, v.v.) còn gây ra những dạng phức tạp khác:


- Hoặc là chúng ta có khối lượng giao dịch lớn trên chuỗi;
- Hoặc là có sự không tương thích cơ bản với mã ví hiện tại;
- Hoặc giải pháp này không khả thi trong đa chữ ký không hợp tác.

Đối với RGB, có hai phương pháp đặc biệt nổi bật: ***Opret*** và ***Tapret***, cả hai đều được phân loại là "Đầu ra giao dịch" và tương thích với chế độ TxO2 mà giao thức sử dụng.

### Cam kết đa giao thức - MPC

Trong phần này, chúng ta sẽ xem xét cách **RGB** xử lý việc tổng hợp nhiều hợp đồng (hay chính xác hơn là _các bó chuyển tiếp_ của chúng) trong một cam kết duy nhất (*cam kết*) được ghi lại trong giao dịch Bitcoin thông qua một lược đồ xác định (theo `Opret` hoặc `Tapret`). Để đạt được điều này, thứ tự Merkelization của các hợp đồng khác nhau diễn ra trong một cấu trúc được gọi là **MPC Tree** (_Multi Protocol Commitment Tree_). Trong phần này, chúng ta sẽ xem xét cách xây dựng MPC Tree này, cách lấy gốc của nó và cách nhiều hợp đồng có thể chia sẻ cùng một giao dịch một cách bảo mật và rõ ràng.

Cam kết đa giao thức (MPC) được thiết kế để đáp ứng hai nhu cầu:


- Việc xây dựng hàm băm `mpc::Commitment`: hàm băm này sẽ được đưa vào chuỗi khối Bitcoin theo lược đồ `Opret` hoặc `Tapret` và phải phản ánh tất cả các thay đổi trạng thái cần được xác thực;
- Lưu trữ đồng thời nhiều hợp đồng trong một _cam kết_ duy nhất, cho phép quản lý các bản cập nhật riêng biệt trên nhiều tài sản hoặc hợp đồng RGB trong một giao dịch Bitcoin duy nhất.

Cụ thể, mỗi _gói chuyển tiếp_ thuộc về một hợp đồng cụ thể. Tất cả thông tin này được chèn vào **MPC Tree**, gốc của nó (`mpc::Root`) sau đó được băm lại để đưa ra `mpc::Commitment`. Chính hàm băm cuối cùng này được đặt trong giao dịch Bitcoin (_giao dịch chứng kiến_), theo phương pháp xác định đã chọn.

![RGB-Bitcoin](assets/fr/042.webp)

#### Băm gốc MPC

Giá trị thực sự được viết trên chuỗi (trong `Opret` hoặc `Tapret`) được gọi là `mpc::Commitment`. Giá trị này được tính theo dạng [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), theo công thức:

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

Ở đâu :


- `mpc_tag` là thẻ: `urn:ubideco:mpc:commitment#2024-01-31`, được chọn theo [quy ước gắn thẻ RGB](https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) biểu thị độ sâu của *Cây MPC*;
- cofactor` (16 bit, theo kiểu Little Endian) là một tham số được sử dụng để thúc đẩy tính duy nhất của các vị trí được chỉ định cho mỗi hợp đồng trong cây;
- `mpc::Root` là gốc của *Cây MPC*, được tính toán theo quy trình được mô tả trong phần tiếp theo.

![RGB-Bitcoin](assets/fr/044.webp)

#### Xây dựng cây MPC

Để xây dựng Cây MPC này, chúng ta cần đảm bảo rằng mỗi hợp đồng tương ứng với một vị trí lá duy nhất. Giả sử chúng ta có:


- c` hợp đồng được bao gồm, được lập chỉ mục bởi `i` trong `i = {0,1,..,C-1}`;
- Đối với mỗi hợp đồng `c_i`, chúng ta có một mã định danh `ContractId(i) = c_i`.

Sau đó, chúng ta xây dựng một cây có chiều rộng `w` và chiều sâu `d` sao cho `2^d = w`, với `w > C`, sao cho mỗi hợp đồng có thể được đặt trong một _lá_ riêng biệt. Vị trí `pos(c_i)` của mỗi hợp đồng trong cây được xác định bởi:

```txt
pos(c_i) = c_i mod (w - cofactor)
```

trong đó `cofactor` là một số nguyên làm tăng khả năng đạt được các vị trí riêng biệt cho mỗi hợp đồng. Trong thực tế, xây dựng tuân theo một quy trình lặp lại:


- Chúng tôi bắt đầu từ độ sâu tối thiểu (`d=3` theo quy ước để ẩn số lượng hợp đồng chính xác);
- Chúng tôi thử nhiều `cofactor` khác nhau (lên đến `w/2` hoặc tối đa 500 vì lý do hiệu suất);
- Nếu chúng ta không thể định vị tất cả các hợp đồng mà không có va chạm, chúng ta sẽ tăng `d` và bắt đầu lại.

Mục đích là tránh những cây quá cao, đồng thời giảm thiểu nguy cơ va chạm ở mức tối thiểu. Lưu ý rằng hiện tượng va chạm tuân theo logic phân phối ngẫu nhiên, liên quan đến [Nghịch lý kỷ niệm](https://en.wikipedia.org/wiki/Birthday_problem).

#### Lá có người ở

Sau khi `C` các vị trí riêng biệt `pos(c_i)` đã được xác định cho các hợp đồng `i = {0,1,..,C-1}`, mỗi trang tính được điền bằng một hàm băm (*được gắn thẻ băm*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

Ở đâu :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, luôn được chọn theo quy ước Merkle của RGB;
- `0x10` xác định một _lá hợp đồng_;
- `c_i` là mã định danh hợp đồng 32 byte (được lấy từ hàm băm Genesis);
- bundleId(c_i)` là hàm băm 32 byte mô tả tập hợp `Chuyển đổi trạng thái` liên quan đến `c_i` (được tập hợp thành *Gói chuyển đổi*).

#### Lá không có người ở

Các lá còn lại, không được gán cho hợp đồng (tức là các lá `w - C`), được điền bằng giá trị "giả" (_lá entropy_):

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

Ở đâu :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, luôn được chọn theo quy ước Merkle của RGB;
- `0x11` biểu thị một _lá entropy_;
- `entropy` là giá trị ngẫu nhiên 64 byte, do người xây dựng cây chọn;
- `j` là vị trí (theo kiểu Little Endian 32 bit) của lá này trong cây.

#### Các nút MPC

Sau khi tạo ra các lá `w` (có người ở hoặc không), chúng ta tiến hành merkelization. Bất kỳ nút bên trong nào cũng được băm như sau:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

Ở đâu :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, luôn được chọn theo quy ước Merkle của RGB;
- b` là _hệ số phân nhánh_ (8 bit). Thông thường, `b=0x02` vì cây là nhị phân và đầy đủ;
- d` là độ sâu của nút trong cây;
- `w` là chiều rộng của cây (theo hệ nhị phân Little Endian 256-bit);
- tH1` và `tH2` là các giá trị băm của các nút con (hoặc nút lá), đã được tính toán như hiển thị ở trên.

Tiến triển theo cách này, chúng ta có được gốc `mpc::Root`. Sau đó, chúng ta có thể tính toán `mpc::Commitment` (như đã giải thích ở trên) và chèn nó vào chuỗi.

Để minh họa điều này, hãy tưởng tượng một ví dụ trong đó `C=3` (ba hợp đồng). Các vị trí của chúng được cho là `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Các lá khác (vị trí 0, 1, 3, 5, 6) là _lá entropy_. Sơ đồ bên dưới hiển thị trình tự băm đến gốc với:


- `BUNDLE_i` biểu diễn `BundleId(c_i)`;
- `tH_MPC_LEAF(A)`, v.v., biểu diễn các lá (một số biểu diễn hợp đồng, một số biểu diễn entropy);
- Mỗi nhánh `tH_MPC_BRANCH(...)` kết hợp các giá trị băm của hai nhánh con của nó.

Kết quả cuối cùng là **mpc::Root**, sau đó là `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### Kiểm tra trục MPC

Khi một người xác minh muốn đảm bảo rằng một hợp đồng `c_i` (và `BundleId`) được bao gồm trong `mpc::Commitment` cuối cùng, anh ta chỉ cần nhận được một bằng chứng Merkle. Bằng chứng này chỉ ra các nút cần thiết để theo dõi các lá (trong trường hợp này là _contract leaf_ của `c_i`) trở lại gốc. Không cần phải tiết lộ toàn bộ *MPC Tree*: điều này bảo vệ tính bảo mật của các hợp đồng khác.

Trong ví dụ, trình xác minh `c_2` chỉ cần một hàm băm trung gian (`tH_MPC_LEAF(D)`), hai `tH_MPC_BRANCH(...)`, bằng chứng vị trí `pos(c_2)` và giá trị `cofactor`. Sau đó, nó có thể tái tạo gốc cục bộ, sau đó tính toán lại `mpc::Commitment` và so sánh với giá trị được viết trong giao dịch Bitcoin (trong `Opret` hoặc `Tapret`).

![RGB-Bitcoin](assets/fr/054.webp)

Cơ chế này đảm bảo rằng:


- Trạng thái liên quan đến `c_2` thực sự được bao gồm trong khối thông tin tổng hợp (phía máy khách);
- Không ai có thể xây dựng lịch sử thay thế với cùng một giao dịch, vì _cam kết_ trên chuỗi trỏ đến một gốc MPC duy nhất.

#### Tóm tắt về cấu trúc MPC

Multi Protocol Commitment* (MPC) là nguyên tắc cho phép RGB tổng hợp nhiều hợp đồng thành một giao dịch Bitcoin duy nhất, đồng thời duy trì tính duy nhất của các cam kết và tính bảo mật đối với những người tham gia khác. Nhờ vào cấu trúc xác định của cây, mỗi hợp đồng được chỉ định một vị trí duy nhất và sự hiện diện của các lá "giả" (*Entropy Leaves*) che giấu một phần tổng số hợp đồng tham gia vào giao dịch.

Toàn bộ cây Merkle không bao giờ được lưu trữ trên máy khách. Chúng tôi chỉ tạo một _đường dẫn Merkle_ cho mỗi hợp đồng liên quan, để truyền đến người nhận (người sau đó có thể xác thực cam kết). Trong một số trường hợp, bạn có thể có một số tài sản đã đi qua cùng một UTXO. Sau đó, bạn có thể hợp nhất một số _đường dẫn Merkle_ thành một khối cam kết đa giao thức được gọi là _khối cam kết đa giao thức_, để tránh trùng lặp quá nhiều dữ liệu.

Do đó, mỗi _Merkle proof_ đều nhẹ, đặc biệt là khi độ sâu của cây không vượt quá 32 trong RGB. Ngoài ra còn có khái niệm "khối Merkle", lưu giữ nhiều thông tin hơn (mặt cắt ngang, entropy, v.v.), hữu ích cho việc kết hợp hoặc tách nhiều nhánh.

Đó là lý do tại sao phải mất nhiều thời gian để hoàn thiện RGB. Chúng tôi đã có tầm nhìn chung từ năm 2019: đưa mọi thứ lên phía máy khách, lưu hành token ngoài chuỗi. Nhưng đối với các chi tiết như phân mảnh cho nhiều hợp đồng, cấu trúc của cây Merkle, cách xử lý va chạm và hợp nhất bằng chứng... tất cả những điều này đều cần phải lặp lại.

### Mỏ neo: một hội đồng toàn cầu

Tiếp theo sau việc xây dựng các cam kết của chúng tôi (`Opret` hoặc `Tapret`) và MPC (*Cam kết đa giao thức*), chúng tôi cần giải quyết khái niệm **Mỏ neo** trong giao thức RGB. Mỏ neo là một cấu trúc được xác thực ở phía máy khách, tập hợp các yếu tố cần thiết để xác minh rằng cam kết Bitcoin thực sự chứa thông tin hợp đồng cụ thể. Nói cách khác, Mỏ neo tóm tắt tất cả dữ liệu cần thiết để xác thực _cam kết_ được mô tả ở trên.

Một Anchor bao gồm ba trường được sắp xếp theo thứ tự:


- `Xiết`
- `Bằng chứng MPC`
- Bằng chứng giao dịch bổ sung - ETP

Mỗi trường này đều đóng một vai trò trong quá trình xác thực, cho dù đó là vấn đề tái cấu trúc giao dịch Bitcoin cơ bản hay chứng minh sự tồn tại của một cam kết ẩn (đặc biệt là trong trường hợp của `Tapret`).

#### Mã số Tx

Trường `Txid` tương ứng với mã định danh 32 byte của giao dịch Bitcoin có chứa cam kết `Opret` hoặc `Tapret`.

Về mặt lý thuyết, có thể tìm thấy `Txid` này bằng cách theo dõi chuỗi các chuyển đổi trạng thái mà bản thân chúng trỏ đến từng giao dịch chứng kiến, theo logic của Single-use Seals. Tuy nhiên, để tạo điều kiện và đẩy nhanh quá trình xác minh, `Txid` này chỉ đơn giản được đưa vào Anchor, do đó giúp trình xác thực không phải quay lại toàn bộ lịch sử ngoài chuỗi.

#### Bằng chứng MPC

Trường thứ hai, `MPC Proof`, đề cập đến bằng chứng cho thấy hợp đồng cụ thể này (ví dụ: `c_i`) được bao gồm trong _Multi Protocol Commitment_. Đây là sự kết hợp của:


- `pos_i`, vị trí của hợp đồng này trong cây MPC;
- cofactor`, giá trị được xác định để giải quyết xung đột vị trí;
- `Merkle Proof`, tức là tập hợp các nút và hàm băm được sử dụng để tái tạo gốc MPC và xác minh rằng mã định danh hợp đồng và `Transition Bundle` của nó đã được cam kết với gốc.

Cơ chế này đã được mô tả trong phần trước về việc xây dựng *Cây MPC*, trong đó mỗi hợp đồng có một nhánh duy nhất nhờ vào:

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Sau đó, một lược đồ merkelization xác định được sử dụng để tổng hợp tất cả các lá (hợp đồng + entropy). Cuối cùng, `MPC Proof` cho phép gốc được tái tạo cục bộ và so sánh với `mpc::Commitment` được bao gồm trên chuỗi.

#### Bằng chứng giao dịch bổ sung - ETP

Trường thứ ba, **ETP**, phụ thuộc vào loại cam kết được sử dụng. Nếu cam kết thuộc loại `Opret`, không cần thêm bằng chứng nào. Trình xác thực kiểm tra đầu ra `OP_RETURN` đầu tiên của giao dịch và tìm `mpc::Commitment` trực tiếp tại đó.

**Nếu cam kết thuộc loại `Tapret`**, phải cung cấp một bằng chứng bổ sung có tên là *Bằng chứng giao dịch bổ sung - ETP*. Bằng chứng này bao gồm:


- Khóa công khai nội bộ (`P`) của đầu ra taproot trong đó *cam kết* được nhúng vào;
- Các nút đối tác của `Script Path Spend` (khi *cam kết* Tapret được chèn vào một tập lệnh), để chứng minh vị trí chính xác của tập lệnh này trong cây gốc:
 - Nếu `Tapret` *cam kết* nằm ở nhánh bên phải, chúng tôi sẽ hiển thị nút bên trái (ví dụ: `tHABC`),
 - Nếu *cam kết* `Tapret` nằm ở bên trái, bạn cần phải tiết lộ 2 nút (ví dụ: `tHAB` và `tHC`) để chứng minh rằng không có *cam kết* nào khác nằm ở phía bên phải.
- `Nonce` có thể được sử dụng để "khai thác" cấu hình tốt nhất, cho phép *cam kết* được đặt ở bên phải của cây (tối ưu hóa bằng chứng).

Bằng chứng bổ sung này rất cần thiết vì, không giống như `Opret`, cam kết `Tapret` được tích hợp vào cấu trúc của tập lệnh taproot, yêu cầu tiết lộ một phần của cây taproot để xác thực chính xác vị trí của *cam kết*.

![RGB-Bitcoin](assets/fr/045.webp)

Do đó, **Anchors** bao gồm tất cả thông tin cần thiết để xác thực cam kết Bitcoin trong bối cảnh RGB. Chúng chỉ ra cả giao dịch có liên quan (`Txid`) và bằng chứng định vị hợp đồng (`MPC Proof`), đồng thời quản lý bằng chứng bổ sung (`ETP`) trong trường hợp `Tapret`. Theo cách này, Anchor bảo vệ tính toàn vẹn và tính duy nhất của trạng thái ngoài chuỗi bằng cách đảm bảo rằng cùng một giao dịch không thể được diễn giải lại cho dữ liệu hợp đồng khác.

### Phần kết luận

Trong chương này, chúng tôi sẽ đề cập đến:


- Cách áp dụng khái niệm Con dấu dùng một lần vào Bitcoin (đặc biệt là thông qua _outpoint_);
- Các phương pháp khác nhau để chèn _cam kết_ một cách xác định vào giao dịch (Điều chỉnh chữ ký, Điều chỉnh khóa, Điều chỉnh chứng thực, op_return, Taproot/Tapret);
- Lý do RGB tập trung vào các cam kết của Tapret;
- Quản lý nhiều hợp đồng thông qua _cam kết đa giao thức_, điều cần thiết nếu bạn không muốn tiết lộ toàn bộ trạng thái hoặc các hợp đồng khác khi bạn muốn chứng minh một điểm cụ thể;
- Chúng ta cũng đã thấy vai trò của _Anchors_, giúp kết hợp mọi thứ lại với nhau (TXID giao dịch, bằng chứng cây Merkle và bằng chứng Taproot) trong một gói duy nhất.

Trong thực tế, việc triển khai kỹ thuật được chia thành nhiều _crates_ Rust chuyên dụng (trong _client_side_validation_, _commit-verify_, _bp_core_, v.v.). Các khái niệm cơ bản nằm ở đó:

![RGB-Bitcoin](assets/fr/046.webp)

Trong chương tiếp theo, chúng ta sẽ xem xét thành phần hoàn toàn ngoài chuỗi của RGB, cụ thể là logic hợp đồng. Chúng ta sẽ xem cách các hợp đồng RGB, được tổ chức như _máy trạng thái hữu hạn_ được sao chép một phần, đạt được khả năng biểu đạt cao hơn nhiều so với các tập lệnh Bitcoin, trong khi vẫn bảo toàn tính bảo mật của dữ liệu.

## Giới thiệu về hợp đồng thông minh và trạng thái của chúng

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

Trong chương này và chương tiếp theo, chúng ta sẽ xem xét khái niệm **hợp đồng thông minh** trong môi trường RGB và khám phá những cách khác nhau mà các hợp đồng này có thể xác định và phát triển *trạng thái* của chúng. Chúng ta sẽ xem lý do tại sao kiến trúc RGB, sử dụng trình tự có thứ tự của Dấu niêm phong sử dụng một lần, giúp thực hiện nhiều loại ***Hoạt động hợp đồng*** theo cách có thể mở rộng và không cần thông qua sổ đăng ký tập trung. Chúng ta cũng sẽ xem xét vai trò cơ bản của ***Logic kinh doanh*** trong việc định hình sự phát triển của trạng thái hợp đồng.

### Hợp đồng thông minh và quyền sở hữu kỹ thuật số

Mục tiêu của RGB là cung cấp cơ sở hạ tầng để triển khai hợp đồng thông minh trên Bitcoin. Theo "hợp đồng thông minh", chúng tôi muốn nói đến một thỏa thuận giữa nhiều bên được thực thi tự động và tính toán, không cần sự can thiệp của con người để thực thi các điều khoản. Nói cách khác, luật của hợp đồng được thực thi bởi phần mềm, không phải bởi bên thứ ba đáng tin cậy.

Tự động hóa này đặt ra câu hỏi về sự phân cấp: làm thế nào chúng ta có thể giải phóng bản thân khỏi một sổ đăng ký tập trung (ví dụ: một nền tảng trung tâm hoặc cơ sở dữ liệu) để quản lý quyền sở hữu và hiệu suất hợp đồng? Ý tưởng ban đầu, được RGB đưa ra, là quay trở lại chế độ sở hữu được gọi là "công cụ mang tên". Theo truyền thống, một số chứng khoán nhất định (trái phiếu, cổ phiếu, v.v.) được phát hành dưới dạng mang tên, cho phép bất kỳ ai sở hữu tài liệu thực tế thực thi các quyền của mình.

![RGB-Bitcoin](assets/fr/055.webp)

RGB áp dụng khái niệm này vào thế giới kỹ thuật số: quyền (và nghĩa vụ) được đóng gói trong dữ liệu được xử lý ngoài chuỗi và trạng thái của dữ liệu này được xác thực bởi chính những người tham gia. Điều này cho phép, trước tiên, mức độ bảo mật và độc lập cao hơn nhiều so với các phương pháp tiếp cận khác dựa trên sổ đăng ký công khai.

### Giới thiệu về trạng thái RGB của Hợp đồng thông minh

Hợp đồng thông minh trong RGB có thể được coi như một máy trạng thái, được định nghĩa bởi:


- **Trạng thái**, tức là tập hợp thông tin phản ánh cấu hình hiện tại của hợp đồng;
- **Logic kinh doanh** (bộ quy tắc), mô tả trạng thái có thể được sửa đổi trong điều kiện nào và bởi ai.

![RGB-Bitcoin](assets/fr/056.webp)

Điều quan trọng là phải hiểu rằng các hợp đồng này không chỉ giới hạn ở việc chuyển giao token đơn giản. Chúng có thể bao gồm nhiều ứng dụng khác nhau: từ tài sản truyền thống (token, cổ phiếu, trái phiếu) đến các cơ chế phức tạp hơn (quyền sử dụng, điều khoản thương mại, v.v.). Không giống như các blockchain khác, nơi mã hợp đồng có thể truy cập và thực thi được bởi tất cả mọi người, cách tiếp cận của RGB phân chia quyền truy cập và kiến thức về hợp đồng cho những người tham gia ("***người tham gia hợp đồng***"). Có một số vai trò:


- Người phát hành** hoặc người tạo ra hợp đồng, người xác định Nguồn gốc của hợp đồng và các biến ban đầu của nó;
- Các bên có quyền** (*quyền sở hữu*) hoặc năng lực thực thi khác;
- Người quan sát**, có khả năng chỉ nhìn thấy một số thông tin nhất định nhưng không thể kích hoạt sửa đổi.

Sự tách biệt vai trò này góp phần vào khả năng chống kiểm duyệt, bằng cách đảm bảo rằng chỉ những người được ủy quyền mới có thể tương tác với trạng thái hợp đồng. Nó cũng cung cấp cho RGB khả năng mở rộng theo chiều ngang: phần lớn các xác thực diễn ra bên ngoài blockchain và chỉ các neo mật mã (các *cam kết*) được ghi trên Bitcoin.

### Trạng thái và Logic kinh doanh trong RGB

Theo quan điểm thực tế, **Logic kinh doanh** của hợp đồng có dạng các quy tắc và tập lệnh, được định nghĩa trong cái mà RGB gọi là **Sơ đồ**. Sơ đồ mã hóa:


- Cấu trúc nhà nước (lĩnh vực nào là công? Lĩnh vực nào thuộc sở hữu của bên nào?
- Điều kiện hợp lệ (cần kiểm tra những gì trước khi cho phép cập nhật trạng thái?);
- Quyền hạn (ai có thể khởi tạo *Chuyển đổi trạng thái*? Ai chỉ có thể quan sát?).

Đồng thời, **Trạng thái hợp đồng** thường được chia thành hai thành phần:


- **Nhà nước toàn cầu**: phần công khai, có khả năng được tất cả mọi người quan sát (tùy thuộc vào cấu hình);
- Trạng thái sở hữu**: các phần riêng tư, được phân bổ cụ thể cho chủ sở hữu thông qua UTXO được tham chiếu trong logic hợp đồng.

Như chúng ta sẽ thấy trong các chương sau, bất kỳ cập nhật trạng thái nào (*Hoạt động hợp đồng*) phải gắn vào _cam kết_ Bitcoin (thông qua `Opret` hoặc `Tapret`) và tuân thủ các tập lệnh *Logic kinh doanh* để được coi là hợp lệ.

### Hoạt động hợp đồng: sự hình thành và phát triển của Nhà nước

Trong vũ trụ RGB, ***Hoạt động hợp đồng*** là bất kỳ sự kiện nào thay đổi hợp đồng từ **trạng thái cũ** sang **trạng thái mới**. Các hoạt động này tuân theo logic sau:


- Chúng tôi ghi nhận tình trạng hiện tại của hợp đồng;
- Chúng tôi áp dụng quy tắc hoặc hoạt động (một ***Chuyển đổi trạng thái***, một ***Khởi tạo*** nếu đó là trạng thái đầu tiên hoặc một ***Mở rộng trạng thái*** nếu có *hóa trị* công khai để kích hoạt lại);
- Chúng tôi neo sự thay đổi thông qua một _cam kết_ mới trên chuỗi khối, đóng một _con dấu sử dụng một lần_ và tạo một con dấu khác;
- Người nắm giữ bản quyền liên quan xác thực cục bộ (*phía máy khách*) rằng quá trình chuyển đổi tuân thủ *Sơ đồ* và giao dịch Bitcoin liên quan được đăng ký trên chuỗi.

![RGB-Bitcoin](assets/fr/057.webp)

Kết quả cuối cùng là một hợp đồng được cập nhật, giờ đây với một trạng thái khác. Quá trình chuyển đổi này không yêu cầu toàn bộ mạng lưới Bitcoin phải quan tâm đến các chi tiết, vì chỉ có một dấu vân tay mật mã nhỏ (_cam kết_) được ghi lại trong chuỗi khối. Chuỗi Dấu niêm phong sử dụng một lần ngăn chặn bất kỳ hành vi chi tiêu gấp đôi hoặc sử dụng gấp đôi nào của Nhà nước.

### Chuỗi hoạt động: từ Genesis đến Terminal State

Để hiểu rõ hơn, một hợp đồng thông minh RGB bắt đầu bằng **Genesis**, trạng thái đầu tiên. Sau đó, nhiều Hoạt động hợp đồng khác nhau sẽ theo sau nhau, tạo thành DAG (*Đồ thị không có chu trình có hướng*) của các hoạt động:


- Mỗi quá trình chuyển đổi đều dựa trên một trạng thái trước đó (hoặc nhiều trạng thái, trong trường hợp chuyển đổi hội tụ);
- Thứ tự thời gian được đảm bảo bằng cách đưa từng quá trình chuyển đổi vào một mỏ neo Bitcoin, có dấu thời gian và không thể thay đổi nhờ sự đồng thuận của Proof-of-Work;
- Khi không còn hoạt động nào đang diễn ra, sẽ đạt đến **Trạng thái cuối**: trạng thái gần đây nhất và hoàn chỉnh nhất của hợp đồng.

![RGB-Bitcoin](assets/fr/012.webp)

Cấu trúc DAG này (thay vì chuỗi tuyến tính đơn giản) phản ánh khả năng các phần khác nhau của hợp đồng có thể phát triển song song, miễn là chúng không mâu thuẫn với nhau. Sau đó, RGB sẽ xử lý để tránh mọi sự không nhất quán bằng cách xác minh *phía máy khách* của từng bên tham gia.

### Bản tóm tắt

Hợp đồng thông minh trong RGB giới thiệu một mô hình công cụ mang kỹ thuật số, phi tập trung nhưng được neo trong Bitcoin để đóng dấu thời gian và đảm bảo thứ tự giao dịch. Việc thực hiện tự động các hợp đồng này dựa trên:


- **Trạng thái hợp đồng*, biểu thị cấu hình hiện tại của hợp đồng (quyền, số dư, biến số, v.v.);
- **Logic kinh doanh** (*Sơ đồ*), xác định những chuyển đổi nào được phép và cách chúng phải được xác thực;
- Hoạt động hợp đồng**, cập nhật trạng thái này từng bước, nhờ vào các cam kết được neo trong các giao dịch Bitcoin.

Trong chương tiếp theo, chúng ta sẽ đi sâu hơn vào cách thể hiện cụ thể của các ***trạng thái*** và ***chuyển đổi trạng thái*** này ở cấp độ ngoài chuỗi và cách chúng liên quan đến UTXO và Dấu niêm phong sử dụng một lần được nhúng trong Bitcoin. Đây sẽ là cơ hội để xem cách cơ chế nội bộ của RGB, dựa trên xác thực phía máy khách, quản lý để duy trì tính nhất quán của hợp đồng thông minh trong khi vẫn bảo toàn tính bảo mật của dữ liệu.

## Hoạt động hợp đồng RGB

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

Trong chương này, chúng ta sẽ xem xét cách thức hoạt động của các hoạt động trong hợp đồng thông minh và chuyển đổi trạng thái, một lần nữa trong giao thức RGB. Mục đích cũng sẽ là hiểu cách một số người tham gia hợp tác để chuyển giao quyền sở hữu một tài sản.

### Chuyển đổi trạng thái và cơ chế của chúng

Nguyên tắc chung vẫn là Xác thực phía máy khách, trong đó dữ liệu trạng thái được chủ sở hữu nắm giữ và được người nhận xác thực. Tuy nhiên, tính đặc thù ở đây với RGB nằm ở chỗ Bob, với tư cách là người nhận, yêu cầu Alice kết hợp một số thông tin nhất định vào dữ liệu hợp đồng để có quyền kiểm soát thực sự đối với tài sản đã nhận, thông qua một tham chiếu ẩn đến một trong các UTXO của anh ta.

Để minh họa quá trình *Chuyển đổi trạng thái* (là một trong những ***Hoạt động hợp đồng*** cơ bản trong RGB), chúng ta hãy xem ví dụ từng bước về việc chuyển giao tài sản giữa Alice và Bob:

**Tình hình ban đầu:**

Alice có ***stash RGB*** dữ liệu được xác thực cục bộ (*client-side*). Stash này đề cập đến một trong những UTXO của cô ấy trên Bitcoin. Điều này có nghĩa là _định nghĩa dấu_ trong dữ liệu này trỏ đến một UTXO thuộc về Alice. Ý tưởng là cho phép cô ấy chuyển một số quyền kỹ thuật số được liên kết với một tài sản (ví dụ: mã thông báo RGB) cho Bob.

![RGB-Bitcoin](assets/fr/058.webp)

**Bob cũng có UTXO :**

Mặt khác, Bob có ít nhất một UTXO của riêng mình, không có liên kết trực tiếp nào đến UTXO của Alice. Trong trường hợp Bob không có UTXO, vẫn có thể thực hiện chuyển giao cho anh ta bằng chính *giao dịch chứng kiến*: đầu ra của giao dịch này sau đó sẽ bao gồm cam kết (_cam kết_) và ngầm liên kết quyền sở hữu hợp đồng mới với Bob.

![RGB-Bitcoin](assets/fr/059.webp)

**Xây dựng cơ sở mới (*Tiểu bang mới*) :**

Bob gửi cho Alice thông tin được mã hóa dưới dạng ***hóa đơn*** (chúng ta sẽ đi sâu hơn vào việc xây dựng hóa đơn trong các chương sau), yêu cầu cô ấy tạo một trạng thái mới tuân thủ các quy tắc của hợp đồng. Trạng thái này sẽ bao gồm một *định nghĩa dấu niêm phong* mới trỏ đến một trong các UTXO của Bob. Theo cách này, Bob được trao quyền sở hữu các tài sản được xác định trong trạng thái mới này, ví dụ như một số lượng token RGB nhất định.

![RGB-Bitcoin](assets/fr/060.webp)

**Chuẩn bị mẫu giao dịch:**

Sau đó, Alice tạo một giao dịch Bitcoin chi tiêu UTXO được tham chiếu trong con dấu trước đó (con dấu hợp pháp hóa cô ấy là người nắm giữ). Trong đầu ra của giao dịch này, một *cam kết* (thông qua `Opret` hoặc `Tapret`) được chèn vào để neo trạng thái RGB mới. Các cam kết `Opret` hoặc `Tapret` được lấy từ một *cây MPC* (như đã thấy trong các chương trước), có thể tổng hợp một số chuyển đổi từ các hợp đồng khác nhau.

**Chuyển *Lệnh gửi* cho Bob:**

Trước khi phát sóng giao dịch, Alice gửi cho Bob một ***Consignment*** chứa tất cả dữ liệu *phía máy khách* cần thiết (*kho lưu trữ* của anh ấy) và thông tin trạng thái mới có lợi cho Bob. Tại thời điểm này, Bob áp dụng các quy tắc đồng thuận RGB:


- Nó xác thực tất cả dữ liệu RGB có trong *Giao dịch*, bao gồm trạng thái mới cấp cho nó quyền sở hữu tài sản;
- Dựa trên *Mỏ neo* có trong *Khoản ký gửi*, nó xác minh trình tự thời gian của các giao dịch chứng kiến (từ Genesis đến quá trình chuyển đổi gần đây nhất) và xác thực các cam kết tương ứng trong chuỗi khối.

**Hoàn tất quá trình chuyển đổi:**

Nếu Bob hài lòng, anh ta có thể chấp thuận (ví dụ, bằng cách ký *giao dịch ký gửi*). Sau đó, Alice có thể phát giao dịch mẫu đã chuẩn bị. Sau khi xác nhận, giao dịch này sẽ đóng dấu niêm phong trước đó do Alice nắm giữ và chính thức hóa quyền sở hữu của Bob. Bảo mật chống chi tiêu gấp đôi sau đó dựa trên cùng một cơ chế như trong Bitcoin: UTXO được chi tiêu, chứng minh rằng Alice không thể sử dụng lại nó nữa.

![RGB-Bitcoin](assets/fr/061.webp)

Trạng thái mới hiện tham chiếu đến UTXO của Bob, trao cho Bob quyền sở hữu trước đó do Alice nắm giữ. Đầu ra Bitcoin nơi dữ liệu RGB được neo trở thành bằng chứng không thể hủy ngang về việc chuyển giao quyền sở hữu.

Một ví dụ về DAG tối thiểu (*Đồ thị không có chu trình có hướng*) bao gồm hai hoạt động hợp đồng (một **Genesis** sau đó là ***Chuyển đổi trạng thái***) có thể minh họa cách trạng thái RGB (lớp *phía máy khách*, màu đỏ) kết nối với chuỗi khối Bitcoin (lớp *Cam kết*, màu cam).

![RGB-Bitcoin](assets/fr/062.webp)

Điều này cho thấy Genesis định nghĩa một con dấu (*định nghĩa con dấu*), sau đó *Chuyển đổi trạng thái* đóng con dấu này lại để tạo một con dấu mới trong UTXO khác.

Trong bối cảnh này, sau đây là một số lời nhắc nhở về thuật ngữ:


- Một ***Bài tập*** kết hợp:
    - ***Định nghĩa về Seal*** (trỏ đến UTXO);
    - Các quốc gia sở hữu**, tức là dữ liệu được liên kết với quyền sở hữu (ví dụ: số lượng mã thông báo được chuyển nhượng).
- **Nhà nước toàn cầu** tập hợp các đặc tính chung của hợp đồng, có thể nhìn thấy được đối với tất cả mọi người và đảm bảo tính nhất quán toàn cầu của quá trình phát triển.

Chuyển đổi trạng thái**, được mô tả trong chương trước, là hình thức chính của hoạt động hợp đồng. Chúng tham chiếu đến một hoặc nhiều trạng thái trước đó (từ Genesis hoặc một Chuyển đổi trạng thái khác) và cập nhật chúng thành trạng thái mới.

![RGB-Bitcoin](assets/fr/063.webp)

Sơ đồ này cho thấy cách thức, trong một *State Transition Bundle*, một số seal có thể được đóng trong một giao dịch mẫu duy nhất, đồng thời mở các seal mới. Thật vậy, một tính năng thú vị của giao thức RGB là khả năng mở rộng quy mô của nó: một số transition có thể được tổng hợp thành một Transition Bundle, mỗi tổng hợp được liên kết với một lá riêng biệt của *cây MPC* (một mã định danh bundle duy nhất). Nhờ cơ chế *Deterministic Bitcoin Commitment* (DBC), toàn bộ thông báo được chèn vào đầu ra `Tapret` hoặc `Opret`, đồng thời đóng các seal trước đó và có thể xác định seal mới. `Anchor* đóng vai trò là liên kết trực tiếp giữa cam kết được lưu trữ trong blockchain và cấu trúc xác thực phía máy khách (*client-side*).

Trong các chương sau, chúng ta sẽ xem xét tất cả các thành phần và quy trình liên quan đến việc xây dựng và xác thực Chuyển đổi trạng thái. Hầu hết các thành phần này là một phần của sự đồng thuận RGB, được triển khai trong **Thư viện lõi RGB**.

### Gói chuyển tiếp

Trên RGB, có thể đóng gói các Chuyển đổi trạng thái khác nhau thuộc cùng một hợp đồng (tức là chia sẻ cùng **ContractId**, bắt nguồn từ **OpId** Genesis). Trong trường hợp đơn giản nhất, như giữa Alice và Bob trong ví dụ trên, **Gói chuyển đổi** chỉ chứa một chuyển đổi. Nhưng hỗ trợ cho các hoạt động của nhiều bên thanh toán (như coinjoin, mở kênh Lightning, v.v.) có nghĩa là một số người dùng có thể kết hợp các Chuyển đổi trạng thái của họ trong một gói duy nhất.

Sau khi thu thập, các chuyển đổi này được neo (bằng cơ chế MPC + DBC) trong một giao dịch Bitcoin duy nhất:


- Mỗi Chuyển đổi Trạng thái được băm và nhóm thành một Gói Chuyển đổi;
- Gói chuyển tiếp được băm và chèn vào nhánh cây MPC tương ứng với hợp đồng này (BundleId);
- Cuối cùng, cây MPC được kích hoạt thông qua `Opret` hoặc `Tapret` trong giao dịch chứng kiến, do đó đóng các con dấu đã sử dụng và xác định các con dấu mới.

Về mặt kỹ thuật, **BundleId** được chèn vào bảng tính MPC được lấy từ hàm băm được gắn thẻ áp dụng cho quá trình tuần tự hóa nghiêm ngặt của trường *InputMap* của bundle:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

Trong đó `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03` chẳng hạn.

*InputMap* là một cấu trúc dữ liệu liệt kê, đối với mỗi đầu vào `i` của giao dịch mẫu, tham chiếu đến *OpId* của Chuyển đổi trạng thái tương ứng. Ví dụ:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- `N` là tổng số mục nhập trong giao dịch tham chiếu đến `OpId`;
- opId(input_j)` là mã định danh hoạt động của một trong các Chuyển đổi trạng thái có trong gói.

Bằng cách tham chiếu mỗi mục nhập chỉ một lần và theo thứ tự, chúng tôi ngăn chặn việc cùng một con dấu được sử dụng hai lần trong hai Chuyển đổi trạng thái đồng thời.

### Tạo trạng thái và trạng thái hoạt động

Do đó, Chuyển đổi trạng thái có thể được sử dụng để chuyển quyền sở hữu tài sản từ người này sang người khác. Tuy nhiên, chúng không phải là hoạt động duy nhất có thể có trong giao thức RGB. Giao thức định nghĩa ba **Hoạt động hợp đồng**:


- Chuyển đổi trạng thái** ;
- Sáng thế** ;
- Mở rộng của tiểu bang**.

Trong số này, **Genesis** và **State Extension** đôi khi được gọi là "*State Generation operations*", vì chúng tạo ra các trạng thái mới mà không đóng ngay lập tức bất kỳ trạng thái nào. Đây là một điểm rất quan trọng: **Genesis** và **State Extension** không liên quan đến việc đóng một con dấu. Thay vào đó, chúng định nghĩa một con dấu mới, sau đó phải được sử dụng bởi **State Transition** tiếp theo để thực sự được xác thực trong lịch sử blockchain.

![RGB-Bitcoin](assets/fr/064.webp)

**Trạng thái hoạt động** của hợp đồng thường được định nghĩa là tập hợp các trạng thái mới nhất xuất phát từ lịch sử (DAG) của các giao dịch, bắt đầu từ Genesis và theo sau tất cả các neo trong chuỗi khối Bitcoin. Bất kỳ trạng thái cũ nào đã lỗi thời (tức là được gắn vào UTXO đã sử dụng) không còn được coi là hoạt động nữa, nhưng vẫn cần thiết để kiểm tra tính nhất quán của lịch sử.

### Sáng thế

Genesis là điểm khởi đầu của mọi hợp đồng RGB. Nó được tạo ra bởi bên phát hành hợp đồng và xác định các tham số ban đầu, theo **Schema**. Trong trường hợp của một mã thông báo RGB, Genesis có thể chỉ định, ví dụ:


- Số lượng token ban đầu được tạo ra và chủ sở hữu của chúng;
- Tổng số trần phát hành có thể có;
- Bất kỳ quy tắc tái ban hành nào và những người tham gia nào đủ điều kiện.

Là giao dịch đầu tiên trong hợp đồng, Genesis không tham chiếu đến bất kỳ trạng thái nào trước đó, cũng không đóng bất kỳ con dấu nào. Tuy nhiên, để xuất hiện trong lịch sử và được xác thực, Genesis phải được **tiêu thụ** (đóng) bởi một Chuyển đổi trạng thái đầu tiên (thường là giao dịch quét/tự động chi tiêu cho chính bên phát hành hoặc phân phối ban đầu cho người dùng).

### Mở rộng nhà nước

State Extensions** cung cấp một tính năng gốc cho hợp đồng thông minh. Chúng giúp có thể mua lại một số quyền kỹ thuật số (*Valencies*) được quy định trong định nghĩa hợp đồng mà không cần đóng dấu ngay lập tức. Thông thường, điều này liên quan đến:


- Phát hành token phân tán;
- Cơ chế hoán đổi tài sản;
- Phát hành lại có điều kiện (có thể bao gồm việc phá hủy các tài sản khác, v.v.).

Về mặt kỹ thuật, một State Extension tham chiếu đến một *Redeem* (một loại đầu vào RGB cụ thể) tương ứng với một *Valency* được định nghĩa trước đó (ví dụ, trong Genesis hoặc một State Transition khác). Nó định nghĩa một con dấu mới, có sẵn cho người hoặc tình trạng được hưởng lợi từ nó. Để con dấu này có hiệu lực, nó phải được sử dụng bởi một State Transition tiếp theo.

![RGB-Bitcoin](assets/fr/065.webp)

Ví dụ: Genesis tạo ra quyền phát hành (*Valency*). Quyền này có thể được thực hiện bởi một tác nhân được ủy quyền, sau đó xây dựng một State Extension:


- Nó ám chỉ đến sự cứu chuộc;
- Nó tạo ra một *nhiệm vụ* mới (dữ liệu *Trạng thái sở hữu* mới) trỏ tới UTXO;
- Chuyển đổi trạng thái trong tương lai do chủ sở hữu UTXO mới này phát hành sẽ thực sự chuyển hoặc phân phối các mã thông báo mới được phát hành.

### Các thành phần của một hoạt động hợp đồng

Bây giờ tôi muốn xem xét chi tiết từng thành phần cấu thành của **Hoạt động hợp đồng** trong RGB. Hoạt động hợp đồng là hành động sửa đổi trạng thái của hợp đồng và được xác thực ở phía máy khách, theo cách xác định, bởi người nhận hợp pháp. Cụ thể, chúng ta sẽ xem Hoạt động hợp đồng tính đến, một mặt, **trạng thái cũ** (*Trạng thái cũ*) của hợp đồng và mặt khác, định nghĩa về **trạng thái mới** (*Trạng thái mới*).

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

Nếu chúng ta nhìn vào sơ đồ trên, chúng ta có thể thấy rằng Hoạt động hợp đồng bao gồm các thành phần tham chiếu đến **Trạng thái mới** và các thành phần khác tham chiếu đến **Trạng thái cũ** đã cập nhật.

Các yếu tố của **Nhà nước mới** là:


- Bài tập**, trong đó được định nghĩa:
 - **Định nghĩa về hải cẩu**;
 - **Nhà nước sở hữu**.
- **Nhà nước toàn cầu** có thể được sửa đổi hoặc làm giàu;
- Các giá trị**, có thể được xác định trong Chuyển đổi trạng thái hoặc Khởi nguyên.

**Trạng thái cũ** được tham chiếu qua:


- Đầu vào**, trỏ tới *Các nhiệm vụ* của các quá trình chuyển đổi trạng thái trước đó (không có trong Genesis);
- Đổi thưởng**, ám chỉ đến các Giá trị được xác định trước đó (chỉ có trong Phần mở rộng của tiểu bang).

Ngoài ra, Hoạt động theo hợp đồng bao gồm các trường tổng quát hơn cụ thể cho hoạt động đó:


- ffv` (*Phiên bản chuyển tiếp nhanh*): số nguyên 2 byte biểu thị phiên bản hợp đồng;
- transitionType` hoặc ExtensionType`: số nguyên 16 bit chỉ định loại Transition hoặc Extension, theo logic nghiệp vụ;
- `ContractId`: số 32 byte tham chiếu đến *OpId* của hợp đồng Genesis. Bao gồm trong Transitions and Extensions, nhưng không có trong Genesis;
- schemaId: chỉ có trong Genesis, đây là mã băm 32 byte biểu diễn cấu trúc (*Schema*) của hợp đồng;
- testnet`: Boolean cho biết bạn đang ở trên mạng Testnet hay Mainnet. Chỉ Genesis;
- altlayers1`: biến xác định lớp thay thế (sidechain hoặc lớp khác) được sử dụng để neo dữ liệu ngoài Bitcoin. Chỉ có trong Genesis;
- "siêu dữ liệu": trường có thể lưu trữ thông tin tạm thời, hữu ích cho việc xác thực hợp đồng phức tạp, nhưng không được ghi lại trong lịch sử trạng thái cuối cùng.

Cuối cùng, tất cả các trường này được cô đọng lại bằng một quy trình băm tùy chỉnh, để tạo ra một dấu vân tay duy nhất, `OpId`. `OpId` này sau đó được tích hợp vào Transition Bundle, cho phép nó được xác thực và xác thực trong giao thức.

Do đó, mỗi *Contract Operation* được xác định bằng một hàm băm 32 byte có tên là `OpId`. Hàm băm này được tính toán bằng hàm băm SHA256 của tất cả các thành phần tạo nên hoạt động. Nói cách khác, mỗi *Contract Operation* có cam kết mật mã riêng, bao gồm tất cả dữ liệu cần thiết để xác minh tính xác thực và tính nhất quán của hoạt động.

Sau đó, hợp đồng RGB được xác định bằng `ContractId`, bắt nguồn từ Genesis `OpId` (vì không có hoạt động nào trước Genesis). Cụ thể, chúng tôi lấy Genesis `OpId`, đảo ngược thứ tự byte và áp dụng mã hóa Base58. Mã hóa này giúp `ContractId` dễ xử lý và nhận dạng hơn.

### Phương pháp và quy tắc cập nhật trạng thái

**Trạng thái hợp đồng** biểu thị tập hợp thông tin mà giao thức RGB phải theo dõi cho một hợp đồng nhất định. Nó bao gồm:


- Một quốc gia toàn cầu duy nhất**: đây là phần công khai, toàn cầu của hợp đồng, tất cả mọi người đều có thể nhìn thấy;
- Một hoặc nhiều Bang sở hữu**: mỗi Bang sở hữu được liên kết với một con dấu duy nhất (và do đó là UTXO trên Bitcoin). Có sự phân biệt giữa:
    - Các tiểu bang **công** sở hữu,
    - Các quốc gia **do tư nhân** sở hữu.

![RGB-Bitcoin](assets/fr/066.webp)

*Nhà nước toàn cầu* được bao gồm trực tiếp trong *Hoạt động hợp đồng* dưới dạng một khối duy nhất. *Các nhà nước sở hữu* được định nghĩa trong mỗi *Giao nhiệm*, cùng với *Định nghĩa con dấu*.

Một tính năng chính của RGB là cách mà Global State và Owned State được sửa đổi. Nhìn chung có hai loại hành vi:


- Có thể thay đổi**: khi một phần tử trạng thái được mô tả là có thể thay đổi, mỗi thao tác mới sẽ thay thế trạng thái trước đó bằng một trạng thái mới. Dữ liệu cũ sau đó được coi là lỗi thời;
- Tích lũy**: khi một phần tử trạng thái được định nghĩa là tích lũy, mỗi thao tác mới sẽ thêm thông tin mới vào trạng thái trước đó mà không ghi đè lên. Kết quả là một loại lịch sử tích lũy.

Nếu trong hợp đồng, một phần tử trạng thái không được định nghĩa là có thể thay đổi hoặc tích lũy, phần tử này sẽ vẫn trống cho các hoạt động tiếp theo (nói cách khác, không có phiên bản mới nào cho trường này). Chính Sơ đồ hợp đồng (tức là logic kinh doanh được mã hóa) sẽ xác định xem trạng thái (Toàn cục hoặc Sở hữu) có thể thay đổi, tích lũy hay cố định. Sau khi Genesis đã được định nghĩa, các thuộc tính này chỉ có thể được sửa đổi nếu bản thân hợp đồng cho phép, ví dụ thông qua một Phần mở rộng trạng thái cụ thể.

Bảng dưới đây minh họa cách mỗi loại Hoạt động hợp đồng có thể thao túng (hoặc không) Trạng thái toàn cầu và Trạng thái sở hữu:

|                              | Genesis | Mở rộng trạng thái | Chuyển đổi trạng thái |
| ---------------------------- | :-----: | :---------------: | :------------------: |
| **Thêm Global State**        |    +    |        -         |        +           |
| **Thay đổi Global State**    |   n/a   |        -         |        +           |
| **Thêm Owned State**         |    +    |        -         |        +           |
| **Thay đổi Owned State**     |   n/a   |       Không      |        +           |
| **Thêm Valencies**           |    +    |        +         |        +           |


**`+`** : hành động có thể thực hiện nếu Sơ đồ hợp đồng cho phép.

**`-`**: hoạt động phải được xác nhận bằng Chuyển đổi trạng thái tiếp theo (Chỉ riêng Mở rộng trạng thái không đóng Dấu niêm phong sử dụng một lần).

Ngoài ra, phạm vi thời gian và quyền cập nhật của từng loại dữ liệu có thể được phân biệt trong bảng sau:

|                                 | Metadata                                  | Trạng thái toàn cục                           | Trạng thái sở hữu                                                                                              |
| ------------------------------- | ---------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Phạm vi**                     | Được xác định cho một thao tác hợp đồng duy nhất | Được xác định toàn cục cho hợp đồng         | Được xác định cho từng niêm phong (*Assignment*)                                                              |
| **Ai có thể cập nhật?**         | Không thể cập nhật lại (dữ liệu tạm thời) | Thao tác do các tác nhân phát hành (issuer, v.v.) | Phụ thuộc vào chủ sở hữu hợp pháp của niêm phong (người có thể chi tiêu nó trong một giao dịch tiếp theo)  |
| **Phạm vi thời gian**           | Chỉ trong thao tác hiện tại              | Trạng thái được thiết lập sau khi thao tác hoàn tất | Trạng thái được xác định trước thao tác (bởi *Seal Definition* của thao tác trước đó)                        |


### Nhà nước toàn cầu

Global State thường được mô tả là "không ai sở hữu, mọi người đều biết". Nó chứa thông tin chung về hợp đồng, được công khai. Ví dụ, trong hợp đồng phát hành token, nó có khả năng chứa:


- Ký hiệu (viết tắt tượng trưng của mã thông báo): `ticker` ;
- Tên đầy đủ của mã thông báo: `name`;
- Độ chính xác (số chữ số thập phân): `precision` ;
- Đề nghị ban đầu (và/hoặc giới hạn mã thông báo tối đa): `issuedSupply`;
- Ngày phát hành: `created` ;
- Dữ liệu pháp lý hoặc thông tin công khai khác: `dữ liệu`.

Global State này có thể được đặt trên các nguồn công cộng (trang web, IPFS, Nostr, Torrent, v.v.) và phân phối cho cộng đồng. Ngoài ra, động lực kinh tế (nhu cầu nắm giữ và chuyển các mã thông báo này, v.v.) tự nhiên thúc đẩy người dùng hợp đồng tự duy trì và truyền bá dữ liệu này.

### Bài tập

*Bài tập* là cấu trúc cơ bản để xác định:


- Con dấu (*Định nghĩa con dấu*), trỏ đến một UTXO cụ thể;
- *Trạng thái sở hữu*, tức là tài sản hoặc dữ liệu liên quan đến con dấu này.

*Assignment* có thể được xem như tương tự như đầu ra giao dịch Bitcoin, nhưng linh hoạt hơn. Ở đây nằm ở logic chuyển nhượng tài sản: *Assignment* liên kết một loại tài sản hoặc quyền cụ thể (`AssignmentType`) với một con dấu. Bất kỳ ai sở hữu khóa riêng của UTXO được liên kết với con dấu này (hoặc bất kỳ ai có thể chi tiêu UTXO này) đều được coi là chủ sở hữu của *Owned State* này.

Một trong những điểm mạnh lớn của RGB nằm ở khả năng hiển thị (*tiết lộ*) hoặc ẩn (*giấu*) các trường *Seal Definition* và *Owned State* theo ý muốn. Điều này mang lại sự kết hợp mạnh mẽ giữa tính bảo mật và tính chọn lọc. Ví dụ, bạn có thể chứng minh rằng một quá trình chuyển đổi là hợp lệ mà không cần tiết lộ toàn bộ dữ liệu, bằng cách cung cấp phiên bản đã tiết lộ cho người phải xác thực, trong khi bên thứ ba chỉ nhìn thấy phiên bản ẩn (một hàm băm). Trong thực tế, `OpId` của một quá trình chuyển đổi luôn được tính toán từ dữ liệu *bị ẩn*.

![RGB-Bitcoin](assets/fr/067.webp)

#### Định nghĩa con dấu

*Định nghĩa về Seal*, ở dạng được tiết lộ, có bốn trường cơ bản: `txptr`, `vout`, `blinding` và `method`:


- txptr**: đây là tham chiếu đến UTXO trên Bitcoin:
    - Trong trường hợp của **con dấu Genesis**, nó trỏ trực tiếp đến một UTXO hiện có (con dấu liên quan đến Genesis);
    - Trong trường hợp của **Graph seal**, chúng ta có thể có:
        - Một `txid` đơn giản, nếu trỏ đến một UTXO cụ thể,
        - Hoặc `WitnessTx`, chỉ định tham chiếu tự thân: con dấu trỏ đến chính giao dịch. Điều này đặc biệt hữu ích khi không có UTXO bên ngoài nào khả dụng, ví dụ như trong các giao dịch mở kênh Lightning hoặc nếu người nhận không có UTXO.
- vout**: số đầu ra của giao dịch được chỉ định bởi `txptr`. Chỉ có trong dấu Graph chuẩn (không có trong `WitnessTx`);
- blinding**: một số ngẫu nhiên gồm 8 byte, để tăng cường tính bảo mật và ngăn chặn các nỗ lực tấn công bằng vũ lực vào danh tính của UTXO;
- phương pháp**: biểu thị phương pháp neo được sử dụng (`Tapret` hoặc `Opret`).

Dạng *ẩn* của Định nghĩa Dấu niêm phong là hàm băm SHA256 (được gắn thẻ) của phép nối 4 trường này, với một thẻ cụ thể cho RGB.

![RGB-Bitcoin](assets/fr/068.webp)

#### Các tiểu bang sở hữu

Thành phần thứ hai của *Assignment* là Owned State. Không giống như Global State, nó có thể tồn tại ở dạng công khai hoặc riêng tư:


- Nhà nước công sở**: mọi người đều biết dữ liệu liên quan đến con dấu. Ví dụ, hình ảnh công cộng;
- Nhà nước tư nhân**: dữ liệu được ẩn, chỉ chủ sở hữu (và có thể là người xác thực nếu cần) mới biết. Ví dụ: số lượng mã thông báo được nắm giữ.

RGB định nghĩa bốn loại trạng thái có thể có (*StateTypes*) cho một Trạng thái sở hữu:


- Khai báo**: không chứa dữ liệu số, chỉ có quyền khai báo (ví dụ: quyền bỏ phiếu). Các hình thức ẩn và hiển thị là giống hệt nhau;
- Fungible**: biểu thị một số lượng có thể thay thế (như token). Ở dạng được tiết lộ, chúng ta có `amount` và `blinding`. Ở dạng ẩn, chúng ta có một *Pedersen commit* duy nhất ẩn số lượng và blinding;
- Structured**: lưu trữ dữ liệu có cấu trúc (tối đa 64 kB). Ở dạng hiển thị, đó là blob dữ liệu. Ở dạng ẩn, đó là băm được gắn thẻ của blob này:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Với ví dụ như:

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Tệp đính kèm**: liên kết một tệp (âm thanh, hình ảnh, nhị phân, v.v.) với Trạng thái sở hữu, lưu trữ tệp băm `file_hash`, loại MIME `media type` và một muối mật mã `salt`. Bản thân tệp được lưu trữ ở nơi khác. Ở dạng ẩn, nó là một băm được gắn thẻ với ba mục dữ liệu trước đó:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Với ví dụ như:

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

Tóm lại, sau đây là 4 loại trạng thái có thể có ở dạng công khai và ẩn:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

| **Thành phần**        | **Khai báo**   | **Có thể thay thế**                  | **Có cấu trúc**                | **Tệp đính kèm**             |
| --------------------- | -------------- | ------------------------------------ | ----------------------------- | ---------------------------- |
| **Dữ liệu**          | Không có       | Số nguyên có dấu hoặc không dấu 64 bit | Bất kỳ loại dữ liệu nghiêm ngặt nào | Bất kỳ tệp nào               |
| **Loại thông tin**   | Không có       | Có dấu hoặc không dấu                 | Loại nghiêm ngặt               | Loại MIME                    |
| **Bảo mật**         | Không yêu cầu  | Cam kết Pedersen                     | Băm với blinding               | Định danh tệp được băm       |
| **Giới hạn kích thước** | N/A           | 256 byte                             | Tối đa 64 KB                   | Tối đa ~500 GB               |


### Đầu vào

Đầu vào của *Hoạt động hợp đồng* đề cập đến *Các nhiệm vụ* đang được chi tiêu trong hoạt động mới này. Đầu vào chỉ ra:


- prevOpId`: mã định danh (`OpId`) của hoạt động trước đó nơi *Bài tập* được đặt;
- assignmentType`: loại *Assignment* (ví dụ: `assetOwner` cho một mã thông báo);
- `Index`: chỉ mục của *Bài tập* trong danh sách liên kết với `OpId` trước đó, được xác định sau khi sắp xếp theo thứ tự từ điển các con dấu ẩn.

Đầu vào không bao giờ xuất hiện trong Genesis vì không có Assignments trước đó. Chúng cũng không xuất hiện trong State Extensions (vì State Extensions không đóng các con dấu; thay vào đó, chúng xác định lại các con dấu mới dựa trên Valencies).

Khi chúng ta có các Trạng thái sở hữu thuộc loại `Fungible`, logic xác thực (thông qua tập lệnh AluVM được cung cấp trong Sơ đồ) sẽ kiểm tra tính nhất quán của các tổng: tổng các mã thông báo đến (*Đầu vào*) phải bằng tổng các mã thông báo đi (trong *Gán* mới).

### Siêu dữ liệu

Trường **Siêu dữ liệu** có thể lên đến 64 KiB và được sử dụng để bao gồm dữ liệu tạm thời hữu ích cho việc xác thực, nhưng không được tích hợp vào trạng thái cố định của hợp đồng. Ví dụ, các biến tính toán trung gian cho các tập lệnh phức tạp có thể được lưu trữ tại đây. Không gian này không được dự định lưu trữ trong lịch sử toàn cầu, đó là lý do tại sao nó nằm ngoài phạm vi của Owned States hoặc Global State.

### Hóa trị

Valencies** là cơ chế giao thức RGB gốc. Chúng có thể được tìm thấy trong Genesis, State Transitions hoặc State Extensions. Chúng đại diện cho các quyền số có thể được kích hoạt bởi State Extension (thông qua *Redeems*), sau đó được hoàn thiện bằng Transition tiếp theo. Mỗi Valency được xác định bằng `ValencyType` (16 bit). Ngữ nghĩa của nó (quyền tái phát hành, hoán đổi token, quyền ghi, v.v.) được định nghĩa trong Schema.

Cụ thể hơn, chúng ta có thể tưởng tượng Genesis định nghĩa "quyền tái phát hành" giá trị. Một State Extension sẽ tiêu thụ nó (*Đổi*) nếu đáp ứng được một số điều kiện nhất định, để giới thiệu một lượng token mới. Sau đó, một State Transition phát sinh từ người nắm giữ con dấu được tạo ra như vậy có thể chuyển những token mới này.

### Đổi thưởng

Redeem là Valency tương đương với Inputs for Assignments. Chúng chỉ xuất hiện trong State Extensions, vì đây là nơi Valency được xác định trước đó được kích hoạt. Redeem bao gồm hai trường:


- `PrevOpId`: `OpId` của hoạt động trong đó Valency được chỉ định;
- `ValencyType`: loại Valency bạn muốn kích hoạt (mỗi `ValencyType` chỉ có thể được sử dụng một lần bởi State Extension).

Ví dụ: Redeem có thể tương ứng với lệnh thực thi CoinSwap, tùy thuộc vào thông tin được mã hóa trong Valency.

### Đặc điểm trạng thái RGB

Bây giờ chúng ta sẽ xem xét một số đặc điểm trạng thái cơ bản trong RGB. Cụ thể, chúng ta sẽ xem xét:


- **Hệ thống kiểu dữ liệu nghiêm ngặt** áp dụng cách tổ chức dữ liệu chính xác và có kiểu dữ liệu;
- Tầm quan trọng của việc tách biệt **xác thực** khỏi **quyền sở hữu**;
- Hệ thống **tiến hóa đồng thuận** trong RGB, bao gồm các khái niệm *tua nhanh* và *đẩy lùi*.

Như thường lệ, hãy nhớ rằng mọi thứ liên quan đến trạng thái hợp đồng đều được xác thực ở phía máy khách theo các quy tắc đồng thuận được nêu trong giao thức và có tham chiếu mật mã cuối cùng được neo trong các giao dịch Bitcoin.

#### Hệ thống kiểu nghiêm ngặt

RGB sử dụng *Hệ thống kiểu nghiêm ngặt* và chế độ tuần tự hóa xác định (*Mã hóa nghiêm ngặt*). Tổ chức này được thiết kế để đảm bảo khả năng tái tạo và độ chính xác hoàn hảo trong việc định nghĩa, xử lý và xác thực dữ liệu hợp đồng.

Trong nhiều môi trường lập trình (JSON, YAML...), cấu trúc dữ liệu có thể linh hoạt, thậm chí là quá dễ dãi. Ngược lại, trong RGB, Cấu trúc và Kiểu của mỗi trường được xác định với các ràng buộc rõ ràng. Ví dụ:


- Mỗi biến có một kiểu cụ thể (ví dụ, số nguyên không dấu 8 bit `u8`, hoặc số nguyên có dấu 16 bit, v.v.);
- Các kiểu có thể được tạo thành (các kiểu lồng nhau). Điều này có nghĩa là bạn có thể định nghĩa một kiểu dựa trên các kiểu khác (ví dụ: một kiểu tổng hợp chứa trường `u8`, trường `bool`, v.v.);
- Bộ sưu tập cũng có thể được chỉ định: danh sách (*list*), tập hợp (*set*) hoặc từ điển (*map*), với thứ tự tiến triển xác định;
- Mỗi trường được giới hạn (*giới hạn dưới* / *giới hạn trên*). Chúng tôi cũng áp đặt giới hạn cho số lượng phần tử trong các bộ sưu tập (giới hạn);
- Dữ liệu được căn chỉnh theo byte và quá trình tuần tự hóa được xác định nghiêm ngặt và rõ ràng.

Nhờ vào giao thức mã hóa nghiêm ngặt này:


- Thứ tự các trường luôn giống nhau, bất kể cách triển khai hoặc ngôn ngữ lập trình được sử dụng;
- Do đó, các hàm băm được tính toán trên cùng một tập dữ liệu có thể tái tạo được và giống hệt nhau (cam kết *hoàn toàn xác định*);
- Các ranh giới ngăn chặn sự tăng trưởng không kiểm soát về kích thước dữ liệu (ví dụ: quá nhiều trường);
- Hình thức mã hóa này tạo điều kiện thuận lợi cho việc xác minh mật mã, vì mỗi người tham gia đều biết chính xác cách tuần tự hóa và băm dữ liệu.

Trong thực tế, cấu trúc (*Schema*) và mã kết quả (*Interface* và logic liên quan) được biên dịch. Một ngôn ngữ mô tả được sử dụng để xác định hợp đồng (kiểu, trường, quy tắc) và tạo ra một định dạng nhị phân nghiêm ngặt. Khi biên dịch, kết quả là:


- *Bố cục bộ nhớ* cho mỗi trường;
- Định danh ngữ nghĩa (chỉ ra liệu việc thay đổi tên biến có ảnh hưởng đến logic hay không, ngay cả khi cấu trúc bộ nhớ vẫn giữ nguyên).

Hệ thống kiểu nghiêm ngặt cũng cho phép theo dõi chính xác các thay đổi: bất kỳ sửa đổi nào đối với cấu trúc (kể cả thay đổi tên trường) đều có thể phát hiện được và có thể dẫn đến thay đổi trong dấu chân tổng thể.

Cuối cùng, mỗi biên dịch tạo ra một dấu vân tay, một mã định danh mật mã chứng thực phiên bản chính xác của mã (dữ liệu, quy tắc, xác thực). Ví dụ, một mã định danh có dạng:

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

Điều này giúp quản lý sự đồng thuận hoặc cập nhật triển khai, đồng thời đảm bảo khả năng truy xuất chi tiết các phiên bản được sử dụng trong mạng.

Để ngăn chặn trạng thái của hợp đồng RGB trở nên quá phức tạp để xác thực ở phía máy khách, một quy tắc đồng thuận áp đặt kích thước tối đa là `2^16` byte (64 Kio) cho bất kỳ dữ liệu nào liên quan đến tính toán xác thực. Điều này áp dụng cho mỗi biến hoặc cấu trúc: không quá 65536 byte hoặc tương đương về số (32768 số nguyên 16 bit, v.v.). Điều này cũng áp dụng cho các bộ sưu tập (danh sách, tập hợp, bản đồ), không được vượt quá `2^16` phần tử.

Giới hạn này đảm bảo:


- Kiểm soát kích thước tối đa của dữ liệu được xử lý trong quá trình chuyển đổi trạng thái;
- Khả năng tương thích với máy ảo (*AluVM*) được sử dụng để chạy các tập lệnh xác thực.

#### Mô hình Xác thực != Quyền sở hữu

Một trong những cải tiến lớn của RGB là sự tách biệt chặt chẽ giữa hai khái niệm:


- Xác thực**: kiểm tra xem quá trình chuyển đổi trạng thái có tuân thủ các quy tắc của hợp đồng hay không (logic nghiệp vụ, lịch sử, v.v.);
- **Quyền sở hữu** (quyền sở hữu hoặc quyền kiểm soát): thực tế sở hữu Bitcoin UTXO cho phép Con dấu sử dụng một lần được chi tiêu (hoặc đóng) và do đó quá trình chuyển đổi trạng thái diễn ra.

Xác thực** diễn ra ở cấp độ ngăn xếp phần mềm RGB (thư viện, giao thức *cam kết*, v.v.). Vai trò của nó là đảm bảo các quy tắc nội bộ của hợp đồng (số lượng, quyền, v.v.) được tôn trọng. Người quan sát hoặc những người tham gia khác cũng có thể xác thực lịch sử dữ liệu.

Mặt khác, quyền sở hữu** hoàn toàn phụ thuộc vào tính bảo mật của Bitcoin. Sở hữu khóa riêng của UTXO có nghĩa là kiểm soát khả năng khởi chạy một quá trình chuyển đổi mới (đóng Dấu sử dụng một lần). Vì vậy, ngay cả khi ai đó có thể xem hoặc xác thực dữ liệu, họ cũng không thể thay đổi trạng thái nếu họ không sở hữu UTXO liên quan.

![RGB-Bitcoin](assets/fr/069.webp)

Cách tiếp cận này hạn chế các lỗ hổng cổ điển gặp phải trong các blockchain phức tạp hơn (nơi tất cả mã của hợp đồng thông minh đều công khai và có thể được bất kỳ ai sửa đổi, điều này đôi khi dẫn đến các vụ hack). Trên RGB, kẻ tấn công không thể chỉ tương tác với trạng thái trên chuỗi, vì quyền hành động trên trạng thái (*quyền sở hữu*) được bảo vệ bởi lớp Bitcoin.

Hơn nữa, việc tách rời này cho phép RGB tích hợp tự nhiên với Lightning Network. Các kênh Lightning có thể được sử dụng để tham gia và di chuyển các tài sản RGB mà không cần tham gia *cam kết* trên chuỗi mọi lúc. Chúng ta sẽ xem xét kỹ hơn về việc tích hợp RGB trên Lightning này trong các chương sau của khóa học.

#### Sự phát triển đồng thuận trong RGB

Ngoài phiên bản mã ngữ nghĩa, RGB bao gồm một hệ thống để phát triển hoặc cập nhật các quy tắc đồng thuận của hợp đồng theo thời gian. Có hai hình thức phát triển chính:


- Chuyển tiếp nhanh**
- Đẩy lùi** (bằng tiếng Pháp)

Chuyển tiếp nhanh xảy ra khi một quy tắc trước đây không hợp lệ trở thành hợp lệ. Ví dụ, nếu hợp đồng phát triển để cho phép một loại `AssignmentType` mới hoặc một trường mới:


- Điều này không thể so sánh với hardfork blockchain cổ điển vì RGB hoạt động trong quá trình xác thực phía máy khách và không ảnh hưởng đến khả năng tương thích tổng thể của blockchain;
- Trên thực tế, loại thay đổi này được biểu thị bằng trường `Ffv` (*phiên bản tua nhanh*) trong hoạt động hợp đồng;
- Người sở hữu thẻ hiện tại không bị ảnh hưởng: tình trạng của họ vẫn có giá trị;
- Mặt khác, người thụ hưởng mới (hoặc người dùng mới) cần cập nhật phần mềm (ví của họ) để nhận ra các quy tắc mới.

Đẩy lùi có nghĩa là một quy tắc hợp lệ trước đó trở nên không hợp lệ. Do đó, đây là một "sự cứng rắn" của các quy tắc, nhưng không hoàn toàn là một softfork:


- Những người nắm giữ hiện tại có thể bị ảnh hưởng (họ có thể thấy tài sản của mình trở nên lỗi thời hoặc không hợp lệ trong phiên bản mới);
- Chúng ta có thể coi rằng thực tế chúng ta đang tạo ra một giao thức mới: bất kỳ ai áp dụng quy tắc mới đều rời khỏi quy tắc cũ;
- Bên phát hành có thể quyết định phát hành lại tài sản theo giao thức mới này, buộc người dùng phải duy trì hai ví riêng biệt (một cho giao thức cũ, một cho giao thức mới) nếu họ muốn quản lý cả hai phiên bản.

Trong chương này về các hoạt động của hợp đồng RGB, chúng ta đã khám phá các nguyên tắc cơ bản làm nền tảng cho giao thức này. Như bạn đã thấy, tính phức tạp vốn có của giao thức RGB đòi hỏi phải sử dụng nhiều thuật ngữ kỹ thuật. Vì vậy, trong chương tiếp theo, tôi sẽ cung cấp cho bạn một bảng thuật ngữ tóm tắt tất cả các khái niệm được đề cập trong phần lý thuyết đầu tiên này, với các định nghĩa của tất cả các thuật ngữ kỹ thuật liên quan đến RGB. Sau đó, trong phần tiếp theo, chúng ta sẽ xem xét thực tế về định nghĩa và triển khai hợp đồng RGB.

## Thuật ngữ RGB

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Nếu bạn cần quay lại bảng chú giải thuật ngữ kỹ thuật quan trọng này được sử dụng trong thế giới RGB (được liệt kê theo thứ tự bảng chữ cái), bạn sẽ thấy nó hữu ích. Chương này không cần thiết nếu bạn đã hiểu mọi thứ chúng tôi đã đề cập trong phần đầu tiên.

#### AluVM

Từ viết tắt AluVM là viết tắt của "_Algorithmic logic unit Virtual Machine_", một máy ảo dựa trên thanh ghi được thiết kế để xác thực hợp đồng thông minh và tính toán phân tán. Nó được sử dụng (nhưng không dành riêng) để xác thực hợp đồng RGB. Do đó, các tập lệnh hoặc hoạt động có trong hợp đồng RGB có thể được thực thi trong môi trường AluVM.

Để biết thêm thông tin: [Trang web chính thức của AluVM](https://www.aluvm.org/)

#### Neo

Anchor biểu thị một tập hợp dữ liệu phía máy khách được sử dụng để chứng minh việc bao gồm một _cam kết_ duy nhất trong một giao dịch. Trong giao thức RGB, Anchor bao gồm các thành phần sau:


- Mã định danh giao dịch Bitcoin (TXID) của **giao dịch chứng kiến**;
- **Cam kết đa giao thức (MPC)**;
- **Cam kết Bitcoin tất định (DBC)**;
- **Bằng chứng giao dịch bổ sung (ETP)** nếu cơ chế cam kết **Tapret** được sử dụng (xem phần dành riêng cho mô hình này).

Do đó, Anchor có chức năng thiết lập liên kết có thể xác minh giữa giao dịch Bitcoin cụ thể và dữ liệu riêng tư được xác thực bởi giao thức RGB. Nó đảm bảo rằng dữ liệu này thực sự được đưa vào blockchain mà không tiết lộ nội dung chính xác của chúng cho công chúng.

#### Phân công

Trong logic của RGB, Assignment tương đương với đầu ra giao dịch sửa đổi, cập nhật hoặc tạo ra các thuộc tính nhất định trong trạng thái của hợp đồng. Assignment bao gồm hai thành phần:


- **Định nghĩa về con dấu** (tham chiếu đến UTXO cụ thể);
- **Tiểu bang sở hữu** (dữ liệu mô tả tiểu bang liên quan đến chủ sở hữu mới này).

Do đó, một Nhiệm vụ chỉ ra rằng một phần của tiểu bang (ví dụ: tài sản) hiện được phân bổ cho một người nắm giữ cụ thể, được xác định thông qua Con dấu sử dụng một lần được liên kết với UTXO.

#### Logic kinh doanh

Logic kinh doanh nhóm tất cả các quy tắc và hoạt động nội bộ của một hợp đồng, được mô tả bằng **sơ đồ** của nó (tức là cấu trúc của chính hợp đồng). Nó chỉ ra cách trạng thái của hợp đồng có thể phát triển và trong những điều kiện nào.

#### Xác thực phía máy khách

Xác thực phía máy khách đề cập đến quá trình mà mỗi bên (máy khách) xác minh một tập hợp dữ liệu được trao đổi riêng tư, theo các quy tắc của một giao thức. Trong trường hợp RGB, dữ liệu được trao đổi này được nhóm lại với nhau trong cái được gọi là **giao dịch**. Không giống như giao thức Bitcoin, yêu cầu tất cả các giao dịch phải được công bố trên chuỗi, RGB chỉ cho phép _cam kết_ (được neo trong Bitcoin) được lưu trữ công khai, trong khi thông tin hợp đồng thiết yếu (chuyển đổi, xác nhận, bằng chứng) vẫn nằm ngoài chuỗi, chỉ được chia sẻ giữa những người dùng có liên quan.

#### Sự cam kết

Cam kết (theo nghĩa mật mã) là một đối tượng toán học, được ký hiệu là `C`, được suy ra một cách xác định từ một phép toán trên dữ liệu có cấu trúc `m` (thông điệp) và một giá trị ngẫu nhiên `r`. Chúng ta viết:

$$
C = \text{commit}(m, r)
$$

Cơ chế này bao gồm hai hoạt động chính:


- Cam kết**: một hàm mật mã được áp dụng cho một thông điệp `m` và một số ngẫu nhiên `r` để tạo ra `C`;
- Xác minh**: chúng ta sử dụng `C`, thông báo `m` và giá trị `r` để kiểm tra xem cam kết này có đúng không. Hàm trả về `True` hoặc `False`.

Một cam kết phải tôn trọng hai đặc tính:


- Ràng buộc**: không thể tìm thấy hai thông báo khác nhau tạo ra cùng một `C`:

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Chẳng hạn như :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Ẩn**: kiến thức về `C` không được tiết lộ nội dung của `m`.

Trong giao thức RGB, một cam kết sẽ được đưa vào giao dịch Bitcoin để chứng minh sự tồn tại của một thông tin nhất định tại một thời điểm nhất định mà không tiết lộ thông tin đó.

#### Gửi hàng

**Consignment** nhóm các dữ liệu được trao đổi giữa các bên, tùy thuộc vào Xác thực phía máy khách trong RGB. Có hai loại chính của lô hàng:


- Hợp đồng ký gửi**: do *bên phát hành* (bên phát hành hợp đồng) cung cấp, bao gồm thông tin khởi tạo như Sơ đồ, Nguồn gốc, Giao diện và Triển khai giao diện.
- Chuyển giao hàng hóa**: do bên thanh toán (*người thanh toán*) cung cấp. Nó chứa toàn bộ lịch sử chuyển đổi trạng thái dẫn đến việc chuyển giao hàng hóa cuối cùng (tức là trạng thái cuối cùng mà người thanh toán nhận được).

Những lô hàng này không được ghi lại công khai trên blockchain; chúng được trao đổi trực tiếp giữa các bên liên quan thông qua kênh liên lạc mà họ lựa chọn.

#### Hợp đồng

Hợp đồng là một tập hợp các quyền được thực hiện kỹ thuật số giữa một số tác nhân thông qua giao thức RGB. Hợp đồng có trạng thái hoạt động và logic nghiệp vụ, được xác định bởi Sơ đồ, chỉ rõ các hoạt động nào được ủy quyền (chuyển nhượng, mở rộng, v.v.). Trạng thái của hợp đồng, cũng như các quy tắc hợp lệ của nó, được thể hiện trong Sơ đồ. Tại bất kỳ thời điểm nào, hợp đồng chỉ phát triển theo những gì được phép bởi Sơ đồ này và bởi các tập lệnh xác thực (chạy, ví dụ, trong AluVM).

#### Hoạt động hợp đồng

Hoạt động hợp đồng là cập nhật trạng thái hợp đồng được thực hiện theo quy tắc Schema. Các hoạt động sau tồn tại trong RGB:


- Chuyển đổi trạng thái** ;
- Sáng thế** ;
- Mở rộng của tiểu bang**.

Mỗi thao tác sẽ sửa đổi trạng thái bằng cách thêm hoặc thay thế dữ liệu nhất định (Trạng thái toàn cục, Trạng thái sở hữu...).

#### Người tham gia hợp đồng

Người tham gia hợp đồng là một diễn viên tham gia vào các hoạt động liên quan đến hợp đồng. Trong RGB, có sự phân biệt giữa:


- Người phát hành hợp đồng, là người tạo ra Genesis (nguồn gốc của hợp đồng);
- Các bên tham gia hợp đồng, tức là những người nắm giữ quyền đối với trạng thái của hợp đồng;
- Các bên công cộng có thể xây dựng các phần mở rộng của Nhà nước nếu hợp đồng cung cấp Valencies cho công chúng.

#### Quyền hợp đồng

Quyền hợp đồng đề cập đến các quyền khác nhau mà những người tham gia vào hợp đồng RGB có thể thực hiện. Chúng thuộc một số loại:


- Quyền sở hữu**, liên quan đến quyền sở hữu của một UTXO cụ thể (thông qua _Định nghĩa con dấu_);
- Quyền hành pháp**, tức là khả năng xây dựng một hoặc nhiều quá trình chuyển đổi (Chuyển đổi trạng thái) theo Sơ đồ;
- Quyền công cộng**, khi Sơ đồ cho phép một số mục đích sử dụng công cộng nhất định, ví dụ như việc tạo Phần mở rộng trạng thái thông qua việc đổi một Valency.

#### Trạng thái hợp đồng

Trạng thái hợp đồng tương ứng với trạng thái hiện tại của hợp đồng tại một thời điểm nhất định. Nó có thể bao gồm cả dữ liệu công khai và riêng tư, phản ánh trạng thái của hợp đồng. RGB phân biệt giữa:


- **Trạng thái toàn cầu**, bao gồm các thuộc tính công khai của hợp đồng (được thiết lập trong Genesis hoặc được thêm vào thông qua các bản cập nhật được ủy quyền);
- Các tiểu bang sở hữu**, thuộc về chủ sở hữu cụ thể, được xác định bằng UTXO của họ.

#### Cam kết Bitcoin xác định - DBC

Cam kết Bitcoin xác định (DBC) là tập hợp các quy tắc được sử dụng để chứng minh và đăng ký duy nhất một _cam kết_ trong giao dịch Bitcoin. Trong giao thức RGB, có hai dạng chính của DBC:


- Hoạt động**
- Tapret**

Các cơ chế này xác định chính xác cách _cam kết_ được mã hóa trong đầu ra hoặc cấu trúc của giao dịch Bitcoin, để đảm bảo rằng cam kết này có thể theo dõi và xác minh được một cách chắc chắn.

#### Đồ thị có hướng phi chu trình - DAG

DAG (hay *Acyclic Guided Graph*) là đồ thị không có chu kỳ, cho phép lập lịch tôpô. Blockchain, giống như _shards_ của hợp đồng RGB, có thể được biểu diễn bằng DAG.

Để biết thêm thông tin: [Đồ thị có hướng không theo chu trình](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Khắc

Khắc là một chuỗi dữ liệu tùy chọn mà những người sở hữu hợp đồng kế tiếp có thể nhập vào lịch sử hợp đồng. Tính năng này tồn tại, ví dụ, trong giao diện **RGB21** và cho phép thêm thông tin kỷ niệm hoặc mô tả vào lịch sử hợp đồng.

#### Bằng chứng giao dịch bổ sung - ETP

ETP (*Bằng chứng giao dịch bổ sung*) là phần của Anchor chứa dữ liệu bổ sung cần thiết để xác thực **Tapret** *cam kết* (trong bối cảnh của _taproot_). Nó bao gồm, trong số những thứ khác, khóa công khai nội bộ của tập lệnh taproot (_internal PubKey_) và thông tin cụ thể cho _Script Path Spend_.

#### Sáng thế

Genesis đề cập đến tập hợp dữ liệu, được quản lý bởi một Schema, tạo thành trạng thái ban đầu của bất kỳ hợp đồng nào trong RGB. Nó có thể được so sánh với khái niệm _Genesis Block_ của Bitcoin hoặc với khái niệm giao dịch Coinbase, nhưng ở đây ở cấp độ _client-side_ và mã thông báo RGB.

#### Nhà nước toàn cầu

Global State là tập hợp các thuộc tính công khai có trong Contract State. Nó được định nghĩa tại Genesis và tùy thuộc vào các quy tắc hợp đồng, có thể được cập nhật bằng các chuyển đổi được ủy quyền. Không giống như Owned States, Global State không thuộc về một thực thể cụ thể; nó gần giống với một sổ đăng ký công khai trong hợp đồng.

#### Giao diện

Giao diện là tập hợp các hướng dẫn được sử dụng để giải mã dữ liệu nhị phân được biên dịch trong Sơ đồ hoặc trong các hoạt động hợp đồng và trạng thái của chúng, để làm cho chúng có thể đọc được đối với người dùng hoặc ví của họ. Nó hoạt động như một lớp diễn giải.

#### Triển khai giao diện

Triển khai Giao diện là tập hợp các khai báo liên kết **Giao diện** với **Schema**. Nó cho phép dịch ngữ nghĩa do chính Giao diện thực hiện, để người dùng hoặc phần mềm liên quan (ví) có thể hiểu được dữ liệu thô của hợp đồng.

#### Hóa đơn

Hóa đơn có dạng URL được mã hóa trong [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), trong đó nhúng dữ liệu cần thiết để xây dựng **Chuyển đổi trạng thái** (bởi bên thanh toán). Nói cách khác, đó là hóa đơn cho phép bên đối tác (*bên thanh toán*) tạo chuyển đổi tương ứng để chuyển giao tài sản hoặc cập nhật trạng thái của hợp đồng.

#### Mạng lưới sét

Lightning Network là mạng lưới phi tập trung các kênh thanh toán (hoặc _kênh trạng thái_) trên Bitcoin, bao gồm 2/2 ví đa chữ ký. Nó cho phép giao dịch _ngoài chuỗi_ nhanh chóng, chi phí thấp, đồng thời dựa vào Lớp 1 của Bitcoin để phân xử (hoặc đóng) khi cần thiết.

Để biết thêm thông tin về cách thức hoạt động của Lightning, tôi khuyên bạn nên tham gia khóa học khác này:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
#### Cam kết đa giao thức - MPC

Multi Protocol Commitment (MPC) đề cập đến cấu trúc cây Merkle được sử dụng trong RGB để bao gồm, trong một giao dịch Bitcoin duy nhất, một số **Transition Bundle** từ các hợp đồng khác nhau. Ý tưởng là nhóm lại với nhau một số cam kết (có khả năng tương ứng với các hợp đồng khác nhau hoặc các tài sản khác nhau) trong một điểm neo duy nhất để tối ưu hóa việc chiếm dụng không gian khối.

#### Nhà nước sở hữu

Một Bang sở hữu là một phần của một Bang hợp đồng được bao gồm trong một Chuyển nhượng và liên kết với một người nắm giữ cụ thể (thông qua một Dấu niêm phong dùng một lần trỏ đến một UTXO). Ví dụ, điều này đại diện cho một tài sản kỹ thuật số hoặc một quyền hợp đồng cụ thể được giao cho người đó.

#### Quyền sở hữu

Quyền sở hữu đề cập đến khả năng kiểm soát và chi tiêu UTXO được tham chiếu bởi Định nghĩa về Dấu niêm phong. Khi một Trạng thái sở hữu được liên kết với một UTXO, chủ sở hữu của UTXO này có quyền, có khả năng, chuyển nhượng hoặc phát triển trạng thái liên quan, theo các quy tắc của hợp đồng.

#### Giao dịch Bitcoin đã ký một phần - PSBT

PSBT (_Giao dịch Bitcoin đã ký một phần_) là giao dịch Bitcoin chưa được ký đầy đủ. Nó có thể được chia sẻ giữa nhiều thực thể, mỗi thực thể có thể thêm hoặc xác minh một số yếu tố nhất định (chữ ký, tập lệnh...), cho đến khi giao dịch được coi là sẵn sàng để phân phối trên chuỗi.

Để biết thêm thông tin: [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Cam kết của Pedersen

Cam kết Pedersen là một loại cam kết mật mã có đặc tính là **đồng cấu** đối với phép toán cộng. Điều này có nghĩa là có thể xác thực tổng của hai cam kết mà không tiết lộ các giá trị riêng lẻ.

Về mặt hình thức, nếu:

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

sau đó :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Thuộc tính này hữu ích trong việc che giấu số lượng mã thông báo được trao đổi, trong khi vẫn có thể xác minh tổng số.

Thông tin thêm: [Cam kết của Pedersen](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Chuộc lại

Trong phần Mở rộng của Tiểu bang, một lệnh Đổi thưởng đề cập đến hành động đòi lại (hoặc khai thác) một **Valency** đã được tuyên bố trước đó. Vì Valency là quyền công cộng, lệnh Đổi thưởng cho phép người tham gia được ủy quyền yêu cầu một phần mở rộng của tiểu bang hợp đồng cụ thể.

#### Sơ đồ

Schema trong RGB là một đoạn mã khai báo mô tả tập hợp các biến, quy tắc và logic nghiệp vụ (*Logic nghiệp vụ*) chi phối hoạt động của hợp đồng. Schema xác định cấu trúc trạng thái, các loại chuyển đổi được phép và các điều kiện xác thực.

#### Định nghĩa con dấu

Định nghĩa Seal là một phần của Assignment liên kết _cam kết_ với UTXO do người nắm giữ mới sở hữu. Nói cách khác, nó chỉ ra vị trí của điều kiện (trong UTXO nào) và thiết lập quyền sở hữu tài sản hoặc quyền.

#### Mảnh vỡ

Shard đại diện cho một nhánh trong DAG của lịch sử Chuyển đổi trạng thái của hợp đồng RGB. Nói cách khác, đó là một tập hợp con mạch lạc của lịch sử tổng thể của hợp đồng, tương ứng, ví dụ, với trình tự chuyển đổi cần thiết để chứng minh tính hợp lệ của một tài sản nhất định kể từ _Genesis_.

#### Con dấu dùng một lần

Con dấu sử dụng một lần là lời hứa mật mã cam kết với một thông điệp chưa được biết đến, sẽ chỉ được tiết lộ một lần trong tương lai và phải được tất cả các thành viên của một đối tượng cụ thể biết. Mục đích là để ngăn chặn việc tạo ra nhiều cam kết cạnh tranh cho cùng một con dấu.

#### Cất giữ

Stash là tập hợp dữ liệu phía máy khách mà người dùng lưu trữ cho một hoặc nhiều hợp đồng RGB, nhằm mục đích xác thực (*Xác thực phía máy khách*). Bao gồm lịch sử chuyển đổi, lô hàng, bằng chứng về tính hợp lệ, v.v. Mỗi người giữ chỉ giữ lại các phần lịch sử mà họ cần (*phân đoạn*).

#### Mở rộng nhà nước

State Extension là một hoạt động hợp đồng được sử dụng để kích hoạt lại các bản cập nhật trạng thái bằng cách đổi **Valencies** đã khai báo trước đó. Để có hiệu lực, State Extension sau đó phải được đóng lại bằng State Transition (cập nhật trạng thái cuối cùng của hợp đồng).

#### Chuyển đổi trạng thái

State Transition là hoạt động thay đổi trạng thái của hợp đồng RGB sang trạng thái mới. Nó có thể sửa đổi dữ liệu Global State và/hoặc Owned State. Trong thực tế, mỗi lần chuyển đổi được xác minh bằng các quy tắc Schema và được neo trong chuỗi khối Bitcoin thông qua _cam kết_.

#### Rễ cái

Đề cập đến định dạng giao dịch Segwit v1 của Bitcoin, được giới thiệu bởi [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) và [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot cải thiện tính bảo mật và tính linh hoạt của các tập lệnh, đặc biệt là bằng cách làm cho các giao dịch nhỏ gọn hơn và khó phân biệt với nhau hơn.

#### Ký gửi đầu cuối - Điểm cuối ký gửi

Ký gửi cuối cùng (hoặc _Điểm cuối ký gửi_) là *ký gửi chuyển nhượng* chứa trạng thái cuối cùng của hợp đồng, bao gồm Chuyển đổi trạng thái được tạo từ Hóa đơn của người nhận (*người nhận thanh toán*). Do đó, đây là điểm cuối của một giao dịch chuyển nhượng, với dữ liệu cần thiết để chứng minh rằng quyền sở hữu hoặc trạng thái đã được chuyển nhượng.

#### Gói chuyển tiếp

Transition Bundle là một tập hợp các RGB State Transitions (thuộc cùng một hợp đồng) đều tham gia vào cùng một ***giao dịch chứng kiến*** Bitcoin. Điều này giúp có thể đóng gói nhiều bản cập nhật hoặc chuyển giao thành một neo trên chuỗi duy nhất.

#### UTXO

Bitcoin UTXO (*Unspent Transaction Output*) được định nghĩa bằng hàm băm của giao dịch và chỉ số đầu ra (*vout*). Đôi khi nó cũng được gọi là _outpoint_. Trong giao thức RGB, tham chiếu đến UTXO (thông qua **Seal Definition**) cho phép xác định vị trí của **Owned State**, tức là tài sản được giữ trên blockchain.

#### Hóa trị

Valency là quyền công cộng không yêu cầu lưu trữ trạng thái như vậy, nhưng có thể được mua lại thông qua **Gia hạn trạng thái**. Do đó, đây là một hình thức khả năng mở cho tất cả (hoặc một số người chơi nhất định), được tuyên bố trong logic của hợp đồng, để thực hiện một gia hạn cụ thể vào một ngày sau đó.

#### Giao dịch chứng kiến

Giao dịch chứng kiến là giao dịch Bitcoin đóng Dấu niêm phong sử dụng một lần xung quanh một thông điệp có chứa Cam kết đa giao thức (MPC). Giao dịch này sử dụng UTXO hoặc tạo một UTXO để niêm phong cam kết được liên kết với giao thức RGB. Nó hoạt động như một bằng chứng trên chuỗi cho thấy trạng thái đã được thiết lập tại một thời điểm cụ thể.

# Lập trình trên RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Triển khai hợp đồng RGB

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

Trong chương này, chúng ta sẽ xem xét kỹ hơn cách hợp đồng RGB được định nghĩa và triển khai. Chúng ta sẽ xem các thành phần của hợp đồng RGB là gì, vai trò của chúng là gì và chúng được xây dựng như thế nào.

### Các thành phần của hợp đồng RGB

Cho đến nay, chúng ta đã thảo luận về **Genesis**, đại diện cho điểm khởi đầu của một hợp đồng và chúng ta đã thấy nó phù hợp như thế nào với logic của một *Contract Operation* và trạng thái của giao thức. Tuy nhiên, định nghĩa đầy đủ về hợp đồng RGB không chỉ giới hạn ở Genesis: nó bao gồm ba thành phần bổ sung, cùng nhau tạo thành cốt lõi của việc triển khai.

Thành phần đầu tiên được gọi là **Schema**. Đây là tệp mô tả cấu trúc cơ bản và logic nghiệp vụ (*logic nghiệp vụ*) của hợp đồng. Nó chỉ định các kiểu dữ liệu được sử dụng, các quy tắc xác thực, các hoạt động được phép (ví dụ: phát hành mã thông báo ban đầu, chuyển nhượng, điều kiện đặc biệt, v.v.) - nói tóm lại, là khuôn khổ chung chỉ định cách thức hoạt động của hợp đồng.

Thành phần thứ hai là **Giao diện**. Nó tập trung vào cách người dùng (và theo nghĩa mở rộng, phần mềm danh mục đầu tư) sẽ tương tác với hợp đồng này. Nó mô tả ngữ nghĩa, tức là biểu diễn dễ đọc của các trường và hành động khác nhau. Vì vậy, trong khi Sơ đồ xác định cách hợp đồng hoạt động về mặt kỹ thuật, Giao diện xác định cách trình bày và hiển thị các chức năng này: tên phương thức, hiển thị dữ liệu, v.v.

Thành phần thứ ba là **Triển khai Giao diện**, bổ sung cho hai thành phần trước bằng cách hoạt động như một loại cầu nối giữa Sơ đồ và Giao diện. Nói cách khác, nó liên kết ngữ nghĩa được thể hiện bởi Giao diện với các quy tắc cơ bản được xác định trong Sơ đồ. Chính triển khai này sẽ quản lý, ví dụ, việc chuyển đổi giữa một tham số được nhập vào ví và cấu trúc nhị phân do giao thức áp đặt hoặc việc biên dịch các quy tắc xác thực trong ngôn ngữ máy.

Tính mô-đun này là một tính năng thú vị của RGB vì nó cho phép các nhóm nhà phát triển khác nhau làm việc riêng biệt trên các khía cạnh này (*Sơ đồ*, *Giao diện*, *Triển khai*), miễn là họ tuân theo các quy tắc đồng thuận của giao thức.

Tóm lại, mỗi hợp đồng bao gồm:


- Genesis**, là trạng thái ban đầu của hợp đồng (và có thể được ví như một giao dịch đặc biệt xác định quyền sở hữu đầu tiên của một tài sản, một quyền hoặc bất kỳ dữ liệu tham số hóa nào khác);
- Schema**, mô tả logic kinh doanh của hợp đồng (kiểu dữ liệu, quy tắc xác thực, v.v.);
- Giao diện**, cung cấp lớp ngữ nghĩa cho cả ví và người dùng, làm rõ việc đọc và thực hiện giao dịch;
- Giao diện triển khai**, thu hẹp khoảng cách giữa logic kinh doanh và cách trình bày, để đảm bảo định nghĩa hợp đồng nhất quán với trải nghiệm của người dùng.

![RGB-Bitcoin](assets/fr/070.webp)

Điều quan trọng cần lưu ý là để ví quản lý tài sản RGB (cho dù là mã thông báo có thể thay thế hay quyền nào đó), ví phải có tất cả các yếu tố sau được biên dịch: *Schema*, *Interface*, *Interface Implementation* và *Genesis*. Điều này được truyền qua ***hợp đồng ký gửi***, tức là một gói dữ liệu chứa mọi thứ cần thiết để xác thực hợp đồng phía máy khách.

Để giúp làm rõ những khái niệm này, sau đây là bảng tóm tắt so sánh các thành phần của hợp đồng RGB với các khái niệm đã biết trong lập trình hướng đối tượng (OOP) hoặc trong hệ sinh thái Ethereum:

| Thành phần hợp đồng RGB     | Ý nghĩa                                  | Tương đương OOP                                   | Tương đương Ethereum               |
| --------------------------- | --------------------------------------- | ------------------------------------------------ | ---------------------------------- |
| **Genesis**                 | Trạng thái ban đầu của hợp đồng         | Class constructor                                | Contract constructor               |
| **Schema**                  | Logic nghiệp vụ của hợp đồng            | Class                                            | Contract                           |
| **Interface**               | Ngữ nghĩa của hợp đồng                  | Interface (Java) / trait (Rust) / protocol (Swift) | ERC Standard                       |
| **Interface Implementation**| Ánh xạ ngữ nghĩa và logic              | Impl (Rust) / Implements (Java)                  | Application Binary Interface (ABI) |


Cột bên trái hiển thị các thành phần cụ thể cho giao thức RGB. Cột giữa hiển thị chức năng cụ thể của từng thành phần. Sau đó, trong cột "OOP tương đương", chúng ta tìm thấy thuật ngữ tương đương trong lập trình hướng đối tượng:


- **Genesis** đóng vai trò tương tự như *Hàm tạo lớp*: đây là nơi trạng thái của hợp đồng được khởi tạo;
- **Schema** là mô tả về một lớp, tức là định nghĩa về các thuộc tính, phương thức và logic cơ bản của lớp đó;
- **Giao diện** tương ứng với *giao diện* (Java), *đặc điểm* (Rust) hoặc *giao thức* (Swift): đây là các định nghĩa công khai về hàm, sự kiện, trường... ;
- **Triển khai Giao diện** tương ứng với *Impl* trong Rust hoặc *Triển khai* trong Java, trong đó chúng ta chỉ định cách mã thực sự thực thi các phương thức được thông báo trong giao diện.

Trong bối cảnh Ethereum, Genesis gần hơn với *trình xây dựng hợp đồng*, Schema gần hơn với định nghĩa hợp đồng, Giao diện gần hơn với tiêu chuẩn như ERC-20 hoặc ERC-721 và Triển khai giao diện gần hơn với ABI (*Giao diện nhị phân ứng dụng*), chỉ định định dạng tương tác với hợp đồng.

Ưu điểm của tính mô-đun của RGB cũng nằm ở thực tế là các bên liên quan khác nhau có thể viết, ví dụ, Giao diện triển khai của riêng họ, miễn là họ tôn trọng logic của *Schema* và ngữ nghĩa của *Giao diện*. Do đó, bên phát hành có thể phát triển một giao diện người dùng mới, thân thiện hơn (Giao diện), mà không cần sửa đổi logic của hợp đồng hoặc ngược lại, người ta có thể mở rộng Giao diện để thêm chức năng và cung cấp phiên bản mới của Giao diện triển khai đã điều chỉnh, trong khi các triển khai cũ vẫn có hiệu lực đối với chức năng cơ bản.

Khi chúng tôi biên soạn một hợp đồng mới, chúng tôi tạo ra Genesis (bước đầu tiên trong việc phát hành hoặc phân phối tài sản), cũng như các thành phần của nó (Schema, Interface, Interface Implementation). Sau đó, hợp đồng hoạt động đầy đủ và có thể được truyền bá đến ví và người dùng. Phương pháp này, trong đó Genesis được kết hợp với ba thành phần này, đảm bảo mức độ tùy chỉnh cao (mỗi hợp đồng có thể có logic riêng), phi tập trung (mọi người có thể đóng góp vào một thành phần nhất định) và bảo mật (xác thực vẫn được xác định nghiêm ngặt bởi giao thức, mà không phụ thuộc vào mã chuỗi tùy ý như thường xảy ra trên các blockchain khác).

Bây giờ tôi muốn xem xét kỹ hơn từng thành phần này: **Sơ đồ**, **Giao diện** và **Triển khai giao diện**.

### Sơ đồ

Trong phần trước, chúng ta đã thấy rằng trong hệ sinh thái RGB, một hợp đồng được tạo thành từ một số thành phần: Genesis, thiết lập trạng thái ban đầu và một số thành phần bổ sung khác. Mục đích của Schema là mô tả một cách khai báo tất cả logic kinh doanh của hợp đồng, tức là cấu trúc dữ liệu, các kiểu được sử dụng, các hoạt động được phép và các điều kiện của chúng. Do đó, đây là một thành phần rất quan trọng trong việc đưa hợp đồng vào hoạt động ở phía máy khách, vì mỗi bên tham gia (ví dụ như ví) phải kiểm tra xem các chuyển đổi trạng thái mà họ nhận được có tuân thủ logic được xác định trong Schema hay không.

Schema có thể được ví như một "lớp" trong lập trình hướng đối tượng (OOP). Nói chung, nó đóng vai trò như một mô hình xác định các thành phần của hợp đồng, chẳng hạn như:


- Các loại Nhà nước sở hữu và Quyền chuyển nhượng khác nhau;
- Quyền lợi, tức là các quyền đặc biệt có thể được kích hoạt (*đổi lại*) cho một số hoạt động nhất định;
- Các trường Trạng thái toàn cầu, mô tả các thuộc tính toàn cầu, công khai và được chia sẻ của hợp đồng;
- Cấu trúc Genesis (hoạt động đầu tiên kích hoạt hợp đồng);
- Các hình thức được phép của Chuyển đổi trạng thái và Mở rộng trạng thái, và cách thức các hoạt động này có thể sửa đổi;
- Siêu dữ liệu liên quan đến từng hoạt động, để lưu trữ thông tin tạm thời hoặc bổ sung;
- Các quy tắc xác định cách dữ liệu hợp đồng nội bộ có thể phát triển (ví dụ: liệu một trường có thể thay đổi hay tích lũy);
- Trình tự các hoạt động được coi là hợp lệ: ví dụ, thứ tự chuyển tiếp cần được tôn trọng hoặc một tập hợp các điều kiện logic cần được đáp ứng.

![RGB-Bitcoin](assets/fr/071.webp)

Khi *bên phát hành* một tài sản trên RGB công bố hợp đồng, bên này sẽ cung cấp Genesis và Schema liên quan đến hợp đồng đó. Người dùng hoặc ví muốn tương tác với tài sản sẽ lấy Schema này để hiểu logic đằng sau hợp đồng và sau đó có thể xác minh rằng các quá trình chuyển đổi mà họ sẽ tham gia là hợp lệ.

Bước đầu tiên, đối với bất kỳ ai nhận thông tin về tài sản RGB (ví dụ: chuyển giao mã thông báo), là xác thực thông tin này với Schema. Điều này liên quan đến việc sử dụng biên dịch Schema để:


- Kiểm tra xem các Trạng thái sở hữu, Nhiệm vụ và các phần tử khác có được định nghĩa đúng không và chúng có tôn trọng các kiểu áp đặt hay không (cái gọi là *hệ thống kiểu nghiêm ngặt*);
- Kiểm tra xem các quy tắc chuyển tiếp (tập lệnh xác thực) có được đáp ứng không. Các tập lệnh này có thể được chạy thông qua AluVM, có ở phía máy khách và chịu trách nhiệm xác thực tính nhất quán của logic kinh doanh (số tiền chuyển, điều kiện đặc biệt, v.v.).

Trên thực tế, Schema không phải là mã thực thi, như có thể thấy trong các blockchain lưu trữ mã trên chuỗi (EVM trên Ethereum). Ngược lại, RGB tách logic kinh doanh (khai báo) khỏi mã thực thi trên blockchain (chỉ giới hạn ở các neo mật mã). Do đó, Schema xác định các quy tắc, nhưng việc áp dụng các quy tắc này diễn ra bên ngoài blockchain, tại trang web của mỗi người tham gia, theo nguyên tắc Xác thực phía máy khách.

Schema phải được biên dịch trước khi có thể được các ứng dụng RGB sử dụng. Biên dịch này tạo ra một tệp nhị phân (ví dụ: `.rgb`) hoặc một tệp nhị phân được mã hóa (`.rgba`). Khi ví nhập tệp này, nó biết:


- Mỗi kiểu dữ liệu (số nguyên, cấu trúc, mảng...) trông như thế nào nhờ hệ thống kiểu nghiêm ngặt;
- Genesis nên được cấu trúc như thế nào (để hiểu về việc khởi tạo tài sản);
- Các loại hoạt động khác nhau (Chuyển đổi trạng thái, Mở rộng trạng thái) và cách chúng có thể sửa đổi trạng thái;
- Các quy tắc viết kịch bản (được giới thiệu trong Sơ đồ) mà công cụ AluVM sẽ áp dụng để kiểm tra tính hợp lệ của các hoạt động.

Như đã giải thích trong các chương trước, *hệ thống kiểu nghiêm ngặt* cung cấp cho chúng ta một định dạng mã hóa ổn định, xác định: tất cả các biến, cho dù là Owned States, Global State hay Valencies, đều được mô tả chính xác (kích thước, giới hạn dưới và trên nếu cần, kiểu có dấu hoặc không dấu, v.v.). Cũng có thể định nghĩa các cấu trúc lồng nhau, ví dụ để hỗ trợ các trường hợp sử dụng phức tạp.

Tùy chọn, Schema có thể tham chiếu đến gốc `SchemaId`, giúp tái sử dụng cấu trúc cơ bản hiện có (mẫu). Theo cách này, bạn có thể phát triển hợp đồng hoặc tạo các biến thể (ví dụ: loại mã thông báo mới) từ mẫu đã được chứng minh. Tính mô-đun này tránh nhu cầu tạo lại toàn bộ hợp đồng và khuyến khích chuẩn hóa các phương pháp hay nhất.

Một điểm quan trọng khác là logic của quá trình tiến hóa trạng thái (chuyển giao, cập nhật, v.v.) được mô tả trong Sơ đồ dưới dạng các tập lệnh, quy tắc và điều kiện. Vì vậy, nếu nhà thiết kế hợp đồng muốn ủy quyền phát hành lại hoặc áp dụng cơ chế ghi (hủy mã thông báo), anh ta có thể chỉ định các tập lệnh tương ứng cho AluVM trong phần xác thực của Sơ đồ.

#### Sự khác biệt so với blockchain có thể lập trình trên chuỗi

Không giống như các hệ thống như Ethereum, nơi mã hợp đồng thông minh (có thể thực thi) được viết vào chính blockchain, RGB lưu trữ hợp đồng (logic của nó) ngoài chuỗi, dưới dạng một tài liệu khai báo được biên dịch. Điều này ngụ ý rằng:


- Không có VM Turing-complete nào chạy trong mọi nút của mạng Bitcoin. Các quy tắc của hợp đồng RGB không được thực thi trên blockchain, mà ở mỗi người dùng muốn xác thực trạng thái;
- Dữ liệu hợp đồng không làm ô nhiễm blockchain: chỉ có bằng chứng mật mã (*cam kết*) được nhúng trong các giao dịch Bitcoin (thông qua `Tapret` hoặc `Opret`);
- Có thể cập nhật hoặc từ chối Schema (*chuyển tiếp nhanh*, *đẩy lùi*, v.v.) mà không cần phải phân nhánh trên chuỗi khối Bitcoin. Ví chỉ cần nhập Schema mới và thích ứng với những thay đổi đồng thuận.

#### Sử dụng bởi bên phát hành và người dùng

Khi một *bên phát hành* tạo ra một tài sản (ví dụ: một mã thông báo có thể thay thế không lạm phát), bên đó sẽ chuẩn bị:


- Sơ đồ mô tả các quy tắc phát xạ, truyền tải, v.v.;
- Genesis được điều chỉnh theo Sơ đồ này (có tổng số mã thông báo đã phát hành, danh tính của chủ sở hữu ban đầu, bất kỳ Valencies đặc biệt nào để phát hành lại, v.v.).

Sau đó, nó cung cấp Schema đã biên dịch (tệp `.rgb`) cho người dùng, để bất kỳ ai nhận được chuyển giao mã thông báo này đều có thể kiểm tra tính nhất quán của hoạt động cục bộ. Nếu không có Schema này, người dùng sẽ không thể diễn giải dữ liệu trạng thái hoặc kiểm tra xem nó có tuân thủ các quy tắc hợp đồng hay không.

Vì vậy, khi một ví mới muốn hỗ trợ một tài sản, nó chỉ cần tích hợp Schema có liên quan. Cơ chế này giúp có thể thêm khả năng tương thích vào các loại tài sản RGB mới mà không cần thay đổi cơ sở phần mềm của ví: tất cả những gì cần thiết là nhập nhị phân Schema và hiểu cấu trúc của nó.

Schema định nghĩa logic kinh doanh trong RGB. Nó liệt kê các quy tắc tiến hóa của hợp đồng, cấu trúc dữ liệu của hợp đồng (Trạng thái sở hữu, Trạng thái toàn cục, Giá trị) và các tập lệnh xác thực liên quan (có thể thực thi bởi AluVM). Nhờ tài liệu khai báo này, định nghĩa của hợp đồng (tệp đã biên dịch) được tách biệt rõ ràng khỏi việc thực thi thực tế các quy tắc (phía máy khách). Sự tách biệt này mang lại cho RGB tính linh hoạt tuyệt vời, cho phép sử dụng nhiều trường hợp (mã thông báo có thể thay thế, NFT, hợp đồng phức tạp hơn) đồng thời tránh được sự phức tạp và các lỗi thường gặp của các chuỗi khối lập trình trên chuỗi.

#### Ví dụ về sơ đồ

Hãy cùng xem một ví dụ cụ thể về Schema cho hợp đồng RGB. Đây là một trích xuất trong Rust từ tệp `nia.rs` (chữ viết tắt của "*Non-Inflatable Assets*"), định nghĩa một mô hình cho các token có thể thay thế không thể được phát hành lại sau khi cung cấp ban đầu của chúng (một tài sản không lạm phát). Loại token này có thể được coi là tương đương, trong vũ trụ RGB, của ERC20 trên Ethereum, tức là các token có thể thay thế tuân thủ một số quy tắc cơ bản nhất định (ví dụ: về chuyển nhượng, khởi tạo cung cấp, v.v.).

Trước khi đi sâu vào mã, chúng ta nên nhớ lại cấu trúc chung của RGB Schema. Có một loạt các khai báo đóng khung:


- `SchemaId` có thể chỉ ra việc sử dụng một Schema cơ bản khác làm mẫu;
- **Các quốc gia toàn cầu** và **Các quốc gia sở hữu** (với các loại nghiêm ngặt của chúng);
- Hóa trị** (nếu có);
- Các **Hoạt động** (Khởi tạo, Chuyển đổi trạng thái, Mở rộng trạng thái) có thể tham chiếu đến các trạng thái và hóa trị này;
- **Hệ thống kiểu nghiêm ngặt** được sử dụng để mô tả và xác thực dữ liệu;
- Tập lệnh xác thực** (chạy qua AluVM).

![RGB-Bitcoin](assets/fr/072.webp)

Mã bên dưới hiển thị định nghĩa đầy đủ của Rust Schema. Chúng tôi sẽ bình luận từng phần, theo các chú thích (1) đến (9) bên dưới:

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - Tiêu đề hàm và SubSchema**

Hàm `nia_schema()` trả về `SubSchema`, cho biết Schema này có thể kế thừa một phần từ một schema chung hơn. Trong hệ sinh thái RGB, tính linh hoạt này giúp có thể tái sử dụng một số thành phần chuẩn của một schema chính, sau đó xác định các quy tắc cụ thể cho hợp đồng đang xét. Ở đây, chúng tôi chọn không cho phép kế thừa, vì `subset_of` sẽ là `None`.


- (2) - Thuộc tính chung: ffv, subset_of, type_system**

Thuộc tính `ffv` tương ứng với phiên bản *chuyển tiếp nhanh* của hợp đồng. Giá trị `zero!()` ở đây cho biết chúng ta đang ở phiên bản 0 hoặc phiên bản ban đầu của lược đồ này. Nếu sau này bạn muốn thêm các chức năng mới (loại hoạt động mới, v.v.), bạn có thể tăng phiên bản này để chỉ ra sự thay đổi đồng thuận.

Thuộc tính `subset_of: None` xác nhận không có sự kế thừa. Trường `type_system` tham chiếu đến hệ thống kiểu nghiêm ngặt đã được xác định trong thư viện `types`. Dòng này chỉ ra rằng tất cả dữ liệu được hợp đồng sử dụng đều sử dụng triển khai tuần tự hóa nghiêm ngặt do thư viện đang đề cập cung cấp.


- (3) - Các quốc gia toàn cầu

Trong khối `global_types`, chúng ta khai báo bốn phần tử. Chúng ta sử dụng khóa, chẳng hạn như `GS_NOMINAL` hoặc `GS_ISSUED_SUPPLY`, để tham chiếu chúng sau:


- `GS_NOMINAL` đề cập đến kiểu `DivisibleAssetSpec`, mô tả nhiều trường khác nhau của mã thông báo được tạo (tên đầy đủ, mã chứng khoán, độ chính xác...);
- `GS_DATA` biểu thị dữ liệu chung, chẳng hạn như tuyên bố từ chối trách nhiệm, siêu dữ liệu hoặc văn bản khác;
- `GS_TIMESTAMP` đề cập đến ngày phát hành;
- `GS_ISSUED_SUPPLY` thiết lập tổng nguồn cung, tức là số lượng mã thông báo tối đa có thể được tạo.

Từ khóa `once(...)` có nghĩa là mỗi trường này chỉ có thể xuất hiện một lần.


- (4) - Các loại sở hữu

Trong `owned_types`, chúng tôi khai báo `OS_ASSET`, mô tả trạng thái có thể thay thế. Chúng tôi sử dụng `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, chỉ ra rằng số lượng tài sản (mã thông báo) được lưu trữ dưới dạng số nguyên không dấu 64 bit. Do đó, bất kỳ giao dịch nào cũng sẽ gửi một số lượng đơn vị nhất định của mã thông báo này, sẽ được xác thực theo cấu trúc số được gõ nghiêm ngặt này.


- (5) - Hóa trị**

Chúng tôi chỉ ra `valency_types: none!()`, nghĩa là không có Valencies nào trong lược đồ này, nói cách khác là không có quyền đặc biệt hoặc quyền bổ sung (như phát hành lại, ghi có điều kiện, v.v.). Nếu lược đồ bao gồm bất kỳ quyền nào, chúng sẽ được khai báo trong phần này.


- (6) - Sáng thế: hoạt động đầu tiên

Ở đây chúng ta nhập phần khai báo Contract Operations. Genesis được mô tả bởi:


- Không có `siêu dữ liệu` (trường `siêu dữ liệu: Ty::<SemId>::UNIT.id(None)`) ;
- Các trạng thái toàn cầu phải xuất hiện một lần (`Một lần`);
- Danh sách Assignments trong đó `OS_ASSET` phải xuất hiện `OnceOrMore`. Điều này có nghĩa là Genesis yêu cầu ít nhất một Assignment `OS_ASSET` (một chủ sở hữu ban đầu);
- Không có giá trị: `valencies: none!()`.

Đây là cách chúng ta giới hạn định nghĩa về vấn đề mã thông báo ban đầu: chúng ta phải khai báo nguồn cung đã phát hành (`GS_ISSUED_SUPPLY`), cộng với ít nhất một người nắm giữ (Trạng thái sở hữu có kiểu `OS_ASSET`).


- (7) - Phần mở rộng

Trường `extensions: none!()` chỉ ra rằng không có State Extension nào được dự kiến trong hợp đồng này. Điều này có nghĩa là không có hoạt động nào để mua lại quyền kỹ thuật số (Valency) hoặc thực hiện mở rộng trạng thái trước khi Chuyển đổi. Mọi thứ đều được thực hiện thông qua Genesis hoặc State Transitions.


- (8) - Chuyển tiếp: TS_TRANSFER

Trong `transitions`, chúng tôi định nghĩa loại hoạt động `TS_TRANSFER`. Chúng tôi giải thích rằng:


- Nó không có siêu dữ liệu;
- Nó không sửa đổi Trạng thái toàn cầu (đã được định nghĩa trong Genesis);
- Nó lấy một hoặc nhiều `OS_ASSETs` làm đầu vào. Điều này có nghĩa là nó phải sử dụng các Owned States hiện có;
- Nó tạo ra (`assignments`) ít nhất một `OS_ASSET` mới (nói cách khác, người nhận hoặc những người nhận sẽ nhận được mã thông báo);
- Nó không tạo ra hóa trị mới.

Mô hình này mô phỏng hành vi của một giao dịch chuyển tiền cơ bản, trong đó sử dụng mã thông báo trên UTXO, sau đó tạo ra các Trạng thái sở hữu mới có lợi cho người nhận và do đó bảo toàn tính bình đẳng của tổng số tiền giữa đầu vào và đầu ra.


- (9) - Tập lệnh AluVM và Điểm vào** (bằng tiếng Pháp)

Cuối cùng, chúng ta khai báo một tập lệnh AluVM (`Script::AluVM(AluScript { ... })`). Tập lệnh này chứa:


- Một hoặc nhiều thư viện bên ngoài (`libs`) được sử dụng trong quá trình xác thực;
- Điểm vào trỏ đến các vị trí bù trừ chức năng trong mã AluVM, tương ứng với xác thực Genesis (`ValidateGenesis`) và mỗi Transition được khai báo (`ValidateTransition(TS_TRANSFER)`).

Mã xác thực này chịu trách nhiệm áp dụng logic kinh doanh. Ví dụ, nó sẽ kiểm tra:


- Không vượt quá `GS_ISSUED_SUPPLY` trong Genesis;
- Tổng số `đầu vào` (mã thông báo đã chi) bằng tổng số `nhiệm vụ` (mã thông báo đã nhận) cho `TS_TRANSFER`.

Nếu không tuân thủ các quy tắc này, quá trình chuyển đổi sẽ bị coi là không hợp lệ.

Ví dụ này về Sơ đồ "*Non Inflatable Fungible Asset*" giúp chúng ta hiểu rõ hơn về cấu trúc của hợp đồng token có thể thay thế RGB đơn giản. Chúng ta có thể thấy rõ sự tách biệt giữa mô tả dữ liệu (Trạng thái toàn cục và trạng thái sở hữu), khai báo hoạt động (Genesis, Transitions, Extensions) và triển khai xác thực (tập lệnh AluVM). Nhờ mô hình này, một token hoạt động giống như một token có thể thay thế cổ điển, nhưng vẫn được xác thực ở phía máy khách và không phụ thuộc vào cơ sở hạ tầng trên chuỗi để thực thi mã của nó. Chỉ có các cam kết mật mã được neo trong chuỗi khối Bitcoin.

### Giao diện

Giao diện là lớp được thiết kế để làm cho hợp đồng có thể đọc được và thao tác được, cả bởi người dùng (đọc bằng con người) và bởi danh mục đầu tư (đọc bằng phần mềm). Do đó, Giao diện đóng vai trò tương đương với giao diện trong ngôn ngữ lập trình hướng đối tượng (Java, Rust, v.v.), ở chỗ nó phơi bày và làm rõ cấu trúc chức năng của hợp đồng, mà không nhất thiết phải tiết lộ các chi tiết bên trong của logic kinh doanh.

Không giống như Schema, chỉ mang tính khai báo và được biên dịch thành tệp nhị phân khó sử dụng, Interface cung cấp các khóa đọc cần thiết để:


- Liệt kê và mô tả các quốc gia toàn cầu và các quốc gia sở hữu có trong hợp đồng;
- Truy cập tên và giá trị của từng trường để có thể hiển thị chúng (ví dụ: đối với một mã thông báo, hãy tìm mã hiệu, số tiền tối đa, v.v.);
- Diễn giải và xây dựng các Hoạt động Hợp đồng (Khởi tạo, Chuyển đổi Trạng thái hoặc Mở rộng Trạng thái) bằng cách liên kết dữ liệu với tên dễ hiểu (ví dụ: thực hiện chuyển giao bằng cách chỉ định rõ ràng "số lượng" thay vì mã định danh nhị phân).

![RGB-Bitcoin](assets/fr/073.webp)

Nhờ Giao diện, bạn có thể, ví dụ, viết mã trong ví, thay vì thao tác các trường, trực tiếp thao tác các nhãn như "số lượng mã thông báo", "tên tài sản", v.v. Theo cách này, việc quản lý hợp đồng trở nên trực quan hơn. Theo cách này, việc quản lý hợp đồng trở nên trực quan hơn.

#### Hoạt động chung

Phương pháp này có nhiều ưu điểm:


- Chuẩn hóa:**

Cùng một loại hợp đồng có thể được hỗ trợ bởi Giao diện chuẩn, được chia sẻ giữa nhiều triển khai ví. Điều này tạo điều kiện cho khả năng tương thích và tái sử dụng mã.


- Phân tách rõ ràng giữa Schema và Interface:**

Trong thiết kế RGB, Schema (logic nghiệp vụ) và Interface (trình bày và thao tác) là hai thực thể độc lập. Các nhà phát triển viết logic hợp đồng có thể tập trung vào Schema mà không cần lo lắng về công thái học hoặc biểu diễn dữ liệu, trong khi một nhóm khác (hoặc cùng một nhóm, nhưng trên một mốc thời gian khác) có thể phát triển Interface.


- Tiến hóa linh hoạt:**

Giao diện có thể được sửa đổi hoặc thêm vào sau khi tài sản đã được phát hành, mà không cần phải thay đổi bản thân hợp đồng. Đây là một sự khác biệt lớn so với một số hệ thống hợp đồng thông minh trên chuỗi, trong đó Giao diện (thường được trộn với mã thực thi) bị đóng băng trong chuỗi khối.


- Khả năng đa giao diện

Cùng một hợp đồng có thể được đưa ra thông qua các Giao diện khác nhau được điều chỉnh theo nhu cầu riêng biệt: một Giao diện đơn giản cho người dùng cuối, một Giao diện khác tiên tiến hơn cho bên phát hành cần quản lý các hoạt động cấu hình phức tạp. Sau đó, ví có thể chọn Giao diện nào để nhập, tùy thuộc vào mục đích sử dụng.

![RGB-Bitcoin](assets/fr/074.webp)

Trên thực tế, khi ví lấy hợp đồng RGB (thông qua tệp `.rgb` hoặc `.rgba`), nó cũng nhập Giao diện liên quan, cũng được biên dịch. Khi chạy, ví có thể, ví dụ:


- Duyệt danh sách các tiểu bang và đọc tên của chúng để hiển thị Mã chứng khoán, Số tiền ban đầu, Ngày phát hành, v.v. trên giao diện người dùng, thay vì mã số không thể đọc được;
- Xây dựng một hoạt động (như chuyển khoản) bằng cách sử dụng tên tham số rõ ràng: thay vì viết `assignments { OS_ASSET => 1 }`, nó có thể cung cấp cho người dùng trường "Số tiền" trong biểu mẫu và dịch thông tin này thành các trường được gõ chặt chẽ theo yêu cầu của hợp đồng.

#### Sự khác biệt giữa Ethereum và các hệ thống khác

Trên Ethereum, Giao diện (được mô tả qua ABI, *Giao diện nhị phân ứng dụng*) thường được bắt nguồn từ mã được lưu trữ trên chuỗi (hợp đồng thông minh). Có thể tốn kém hoặc phức tạp khi sửa đổi một phần cụ thể của giao diện mà không động đến chính hợp đồng. Tuy nhiên, RGB dựa trên logic hoàn toàn ngoài chuỗi, với dữ liệu được neo trong *cam kết* trên Bitcoin. Thiết kế này giúp có thể sửa đổi Giao diện (hoặc việc triển khai của nó) mà không ảnh hưởng đến tính bảo mật cơ bản của hợp đồng, vì việc xác thực các quy tắc kinh doanh vẫn nằm trong Sơ đồ và mã AluVM được tham chiếu.

#### Biên dịch giao diện

Giống như Schema, Giao diện được định nghĩa trong mã nguồn (thường là Rust) và được biên dịch thành tệp `.rgb` hoặc `.rgba`. Tệp nhị phân này chứa tất cả thông tin mà ví yêu cầu để:


- Xác định các trường theo tên;
- Liên kết từng trường (và giá trị của trường đó) với loại hệ thống nghiêm ngặt được xác định trong hợp đồng;
- Biết các hoạt động khác nhau được phép và cách thực hiện chúng.

Sau khi Giao diện được nhập, ví có thể hiển thị chính xác hợp đồng và đề xuất các tương tác cho người dùng.

### Giao diện được chuẩn hóa bởi hiệp hội LNP/BP

Trong hệ sinh thái RGB, Giao diện được sử dụng để cung cấp ý nghĩa có thể đọc và thao tác được cho dữ liệu và hoạt động của hợp đồng. Do đó, Giao diện bổ sung cho Sơ đồ, mô tả logic kinh doanh nội bộ (các kiểu nghiêm ngặt, tập lệnh xác thực, v.v.). Trong phần này, chúng ta sẽ xem xét các Giao diện chuẩn do hiệp hội LNP/BP phát triển cho các loại hợp đồng phổ biến (mã thông báo có thể thay thế, NFT, v.v.).

Xin nhắc lại, ý tưởng là mỗi Giao diện mô tả cách hiển thị và thao tác hợp đồng ở phía ví, đặt tên rõ ràng cho các trường (như `spec`, `ticker`, `issuedSupply`...) và xác định các thao tác có thể thực hiện (như `Transfer`, `Burn`, `Rename`...). Một số Giao diện đã hoạt động, nhưng sẽ có nhiều hơn nữa trong tương lai.

#### Một số giao diện sẵn sàng sử dụng

**RGB20** là Giao diện cho các tài sản có thể thay thế, có thể so sánh với tiêu chuẩn ERC20 của Ethereum. Tuy nhiên, nó tiến xa hơn một bước, cung cấp chức năng mở rộng hơn:


- Ví dụ, khả năng đổi tên tài sản (thay đổi *mã chứng khoán* hoặc tên đầy đủ) sau khi phát hành hoặc điều chỉnh độ chính xác của tài sản (*chia tách cổ phiếu*);
- Nó cũng có thể mô tả các cơ chế tái phát hành thứ cấp (có giới hạn hoặc không giới hạn) và để đốt rồi thay thế, nhằm cho phép bên phát hành phá hủy rồi tái tạo tài sản trong những điều kiện nhất định;

Ví dụ, Giao diện RGB20 có thể được liên kết với chương trình **Tài sản không thể bơm hơi (NIA)**, áp dụng nguồn cung ban đầu không thể bơm hơi hoặc với các chương trình tiên tiến hơn khác nếu cần.

**RGB21** liên quan đến các hợp đồng loại NFT hoặc rộng hơn là bất kỳ nội dung kỹ thuật số độc đáo nào, chẳng hạn như biểu diễn phương tiện kỹ thuật số (hình ảnh, nhạc, v.v.). Ngoài việc mô tả vấn đề phát hành và chuyển giao một tài sản duy nhất, nó còn bao gồm các tính năng như:


- Hỗ trợ tích hợp để đưa trực tiếp tệp (tối đa 16 MB) vào hợp đồng (để truy xuất ở phía máy khách);
- Chủ sở hữu có thể nhập "*khắc*" vào lịch sử để chứng minh quyền sở hữu trước đây của NFT.

**RGB25** là một tiêu chuẩn lai kết hợp các khía cạnh có thể thay thế và không thể thay thế. Nó được thiết kế cho các tài sản có thể thay thế một phần, chẳng hạn như mã hóa bất động sản, nơi bạn muốn chia nhỏ một tài sản trong khi vẫn giữ liên kết đến một tài sản gốc duy nhất (nói cách khác, bạn có các phần có thể thay thế của một ngôi nhà, được liên kết đến một ngôi nhà không thể thay thế). Về mặt kỹ thuật, giao diện này có thể được liên kết với lược đồ **Tài sản có thể thay thế sưu tầm* (CFA)**, có tính đến khái niệm chia nhỏ trong khi theo dõi tài sản gốc.

#### Giao diện đang được phát triển

Các Giao diện khác được lên kế hoạch cho mục đích sử dụng chuyên biệt hơn nhưng hiện chưa có sẵn:


- RGB22**, dành riêng cho danh tính kỹ thuật số, để quản lý các mã định danh và hồ sơ trên chuỗi trong hệ sinh thái RGB;
- RGB23**, để đóng dấu thời gian nâng cao, sử dụng một số ý tưởng của *Opentimestamps*, nhưng có các tính năng truy xuất nguồn gốc;
- RGB24**, hướng tới mục tiêu tương đương với hệ thống tên miền phi tập trung (DNS) tương tự như *Ethereum Name Service*;
- RGB26**, được thiết kế để quản lý DAO (*Tổ chức tự trị phi tập trung*) theo định dạng phức tạp hơn (quản trị, bỏ phiếu, v.v.);
- RGB30**, rất giống với RGB20 nhưng có đặc điểm là tính đến việc phát hành ban đầu phi tập trung và sử dụng State Extensions. Điều này sẽ được sử dụng cho các tài sản mà việc phát hành lại được quản lý bởi nhiều thực thể hoặc tuân theo các điều kiện tinh vi hơn.

Tất nhiên, tùy thuộc vào ngày bạn tham khảo khóa học này, các giao diện này có thể đã hoạt động và có thể truy cập được.

#### Ví dụ về giao diện

Đoạn mã Rust này hiển thị Giao diện [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) (tài sản có thể thay thế). Mã này được lấy từ tệp `rgb20.rs` trong thư viện RGB chuẩn. Chúng ta hãy xem xét nó để hiểu cấu trúc của Giao diện và cách nó cung cấp cầu nối giữa, một mặt, logic kinh doanh (được xác định trong Sơ đồ) và mặt khác, các chức năng được cung cấp cho ví và người dùng.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

Trong giao diện này, chúng ta nhận thấy những điểm tương đồng với cấu trúc Schema: chúng ta tìm thấy một tuyên bố về Global State, Owned States, Contract Operations (Genesis và Transitions), cũng như xử lý lỗi. Nhưng Interface tập trung vào việc trình bày và thao tác các thành phần này cho ví hoặc bất kỳ ứng dụng nào khác.

Sự khác biệt với Schema nằm ở bản chất của các kiểu. Schema sử dụng các kiểu nghiêm ngặt (như `FungibleType::Unsigned64Bit`) và các định danh kỹ thuật hơn. Giao diện sử dụng tên trường, macro (`fname!()`, `tn!()`) và tham chiếu đến các lớp đối số (`ArgSpec`, `OwnedIface::Rights`...). Mục đích ở đây là tạo điều kiện thuận lợi cho việc hiểu chức năng và tổ chức các thành phần cho ví.

Ngoài ra, Giao diện có thể giới thiệu chức năng bổ sung cho Sơ đồ cơ bản (ví dụ: quản lý quyền `burnEpoch`), miễn là điều này vẫn nhất quán với logic phía máy khách đã được xác thực cuối cùng. Phần "script" AluVM trong Sơ đồ sẽ đảm bảo tính hợp lệ về mặt mật mã, trong khi Giao diện mô tả cách người dùng (hoặc ví) tương tác với các trạng thái và chuyển đổi này.

#### Trạng thái toàn cầu và nhiệm vụ

Trong phần `global_state`, chúng ta tìm thấy các trường như `spec` (mô tả tài sản), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Đây là các trường mà ví có thể đọc và hiển thị. Ví dụ:


- `spec` sẽ hiển thị cấu hình mã thông báo;
- `issuedSupply` hoặc `burnedSupply` cung cấp cho chúng ta tổng số token đã phát hành hoặc đã đốt, v.v.

Trong phần `assignments`, chúng tôi định nghĩa nhiều vai trò hoặc quyền khác nhau. Ví dụ:


- `assetOwner` tương ứng với việc nắm giữ các mã thông báo (đó là *Trạng thái sở hữu* có thể thay thế);
- `burnRight` tương ứng với khả năng đốt token;
- updateRight` tương ứng với quyền đổi tên tài sản.

Từ khóa `public` hoặc `private` (ví dụ: `AssignIface::public(...)`) chỉ ra liệu các trạng thái này có thể nhìn thấy (`public`) hay bí mật (`private`). Đối với `Req::NoneOrMore`, `Req::Optional`, chúng chỉ ra sự kiện dự kiến.

#### Sáng thế và chuyển tiếp

Phần `genesis` mô tả cách khởi tạo tài sản:


- Các trường `spec`, `data`, `created`, `issuedSupply` là bắt buộc (`ArgSpec::required()`) ;
- Các nhiệm vụ như `assetOwner` có thể xuất hiện ở nhiều bản sao (`ArgSpec::many()`), cho phép phân phối mã thông báo cho nhiều người nắm giữ ban đầu;
- Các trường như `inflationAllowance` hoặc `burnEpoch` có thể (hoặc không thể) được bao gồm trong Genesis.

Sau đó, đối với mỗi Chuyển đổi (`Chuyển`, `Phát hành`, `Đốt`...), Giao diện xác định các trường mà hoạt động mong đợi là đầu vào, các trường mà hoạt động sẽ tạo ra là đầu ra và bất kỳ lỗi nào có thể xảy ra. Ví dụ:

**Chuyển tiếp :**


- Đầu vào: `previous` → phải là `assetOwner`;
- Nhiệm vụ: `người thụ hưởng` → sẽ là `chủ sở hữu tài sản` mới;
- Lỗi: `NON_EQUAL_AMOUNTS` (do đó, ví sẽ có thể xử lý các trường hợp tổng đầu vào không tương ứng với tổng đầu ra).

**Vấn đề chuyển tiếp:**


- Tùy chọn (`tùy chọn: đúng`), vì phát xạ bổ sung không nhất thiết phải được kích hoạt;
- Đầu vào: `used` → `inflationAllowance`, tức là quyền thêm nhiều mã thông báo hơn;
- Nhiệm vụ: `beneficiary` (nhận được mã thông báo mới) và `future` (`inflationAllowance` còn lại);
- Các lỗi có thể xảy ra: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, v.v.

**Chuyển đổi quá trình đốt cháy :**


- Đầu vào: `used` → a `burnRight` ;
- Toàn cục: `burnedSupply` là bắt buộc;
- Bài tập: `future` → có thể tiếp tục `burnRight` nếu chúng ta chưa đốt cháy mọi thứ;
- Lỗi: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Do đó, mỗi hoạt động được mô tả theo cách có thể đọc được đối với ví. Điều này giúp có thể hiển thị giao diện đồ họa, nơi người dùng có thể thấy rõ: "Bạn có quyền đốt. Bạn có muốn đốt một số tiền nhất định không? Mã biết điền vào trường `burnedSupply` và kiểm tra xem `burnRight` có hợp lệ không.

Tóm lại, điều quan trọng cần lưu ý là một Giao diện, dù hoàn chỉnh đến đâu, cũng không tự nó xác định được logic bên trong của hợp đồng. Trọng tâm của công việc được thực hiện bởi **Schema**, bao gồm các kiểu nghiêm ngặt, cấu trúc Genesis, chuyển tiếp, v.v. Giao diện chỉ đơn giản là trình bày các thành phần này theo cách trực quan hơn và được đặt tên, để sử dụng trong một ứng dụng.

Nhờ tính mô-đun của RGB, Giao diện có thể được nâng cấp (ví dụ, bằng cách thêm chuyển đổi `Đổi tên`, sửa lỗi hiển thị của một trường, v.v.) mà không cần phải viết lại toàn bộ hợp đồng. Người dùng Giao diện này sau đó có thể hưởng lợi ngay từ những cải tiến này, ngay khi họ cập nhật tệp `.rgb` hoặc `.rgba`.

Nhưng sau khi bạn đã khai báo một Giao diện, bạn cần liên kết nó với Sơ đồ tương ứng. Điều này được thực hiện thông qua ***Triển khai Giao diện***, chỉ định cách ánh xạ từng trường được đặt tên (chẳng hạn như `fname!("assetOwner")`) với ID nghiêm ngặt (chẳng hạn như `OS_ASSET`) được định nghĩa trong Sơ đồ. Điều này đảm bảo, ví dụ, rằng khi một ví thao tác với trường `burnRight`, thì đây là trạng thái, trong Sơ đồ, mô tả khả năng ghi mã thông báo.

### Triển khai giao diện

Trong kiến trúc RGB, chúng ta đã thấy rằng mỗi thành phần (Schema, Interface, v.v.) có thể được phát triển và biên dịch độc lập. Tuy nhiên, vẫn còn một thành phần không thể thiếu liên kết các khối xây dựng khác nhau này lại với nhau: ***Interface Implementation***. Đây là thành phần ánh xạ rõ ràng các định danh hoặc trường được xác định trong Schema (ở phía logic nghiệp vụ) với các tên được khai báo trong Interface (ở phía trình bày và tương tác của người dùng). Vì vậy, khi ví tải hợp đồng, nó có thể hiểu chính xác trường nào tương ứng với trường nào và cách một hoạt động được đặt tên trong Interface liên quan đến logic của Schema.

Một điểm quan trọng là Interface Implementation không nhất thiết có ý định phơi bày tất cả các chức năng của Schema, cũng như tất cả các trường Interface: nó có thể bị giới hạn ở một tập hợp con. Trong thực tế, điều này giúp hạn chế hoặc lọc một số khía cạnh nhất định của Schema. Ví dụ, bạn có thể có một Schema với bốn loại hoạt động, nhưng một Implementation Interface chỉ ánh xạ hai trong số chúng trong một ngữ cảnh nhất định. Ngược lại, nếu một Interface đề xuất các điểm cuối bổ sung, chúng ta có thể chọn không triển khai chúng ở đây.

Sau đây là một ví dụ điển hình về Triển khai Giao diện, trong đó chúng ta liên kết Sơ đồ *Tài sản không thể bơm phồng* (NIA) với Giao diện RGB20:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

Trong Giao diện triển khai này:


- Chúng tôi tham chiếu rõ ràng đến Schema, thông qua `nia_schema()`, và Interface, thông qua `Rgb20::iface()`. Các lệnh gọi `schema.schema_id()` và `iface.iface_id()` được sử dụng để neo Interface Implementation vào phía biên dịch (điều này liên kết các định danh mật mã của hai thành phần này);
- Một ánh xạ được thiết lập giữa các phần tử Schema và các phần tử Interface. Ví dụ, trường `GS_NOMINAL` trong Schema được liên kết với chuỗi `"spec"` ở phía Interface (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Chúng tôi thực hiện tương tự đối với các hoạt động, chẳng hạn như `TS_TRANSFER`, mà chúng tôi liên kết với `"Transfer"` trong Interface... ;
- Chúng ta có thể thấy rằng không có hóa trị (`valencies: none!()`) hoặc phần mở rộng (`extensions: none!()`), phản ánh thực tế là hợp đồng NIA này không sử dụng các tính năng này.

Kết quả sau khi biên dịch là một tệp `.rgb` hoặc `.rgba` riêng biệt, được nhập vào ví ngoài Schema và Interface. Do đó, phần mềm biết cách kết nối cụ thể hợp đồng NIA này (có logic được mô tả bởi Schema) với Giao diện "RGB20" (cung cấp tên người và chế độ tương tác cho các token có thể thay thế), áp dụng Triển khai Giao diện này làm cổng giữa hai giao diện.

#### Tại sao phải tách biệt việc triển khai giao diện?

Phân tách tăng cường tính linh hoạt. Một Schema đơn lẻ có thể có một số Interface Implementation riêng biệt, mỗi Interface ánh xạ một tập hợp các chức năng khác nhau. Hơn nữa, Interface Implementation có thể tự phát triển hoặc được viết lại mà không cần thay đổi Schema hoặc Interface. Điều này giữ nguyên nguyên tắc mô-đun của RGB: mỗi thành phần (Schema, Interface, Interface Implementation) có thể được phiên bản hóa và cập nhật độc lập, miễn là các quy tắc tương thích do giao thức áp đặt được tôn trọng (cùng một định danh, tính nhất quán của các loại, v.v.).

Trong quá trình sử dụng cụ thể, khi ví tải hợp đồng, ví phải:


- Tải **Schema** đã biên dịch (để biết cấu trúc của logic nghiệp vụ);
- Tải **Giao diện** đã biên dịch (để hiểu tên và hoạt động phía người dùng);
- Tải **Triển khai giao diện** đã biên dịch (để liên kết logic Sơ đồ với tên Giao diện, từng thao tác, từng trường).

Kiến trúc mô-đun này có thể thực hiện được các tình huống sử dụng như:


- Giới hạn một số thao tác nhất định đối với một số người dùng nhất định: cung cấp Giao diện triển khai một phần chỉ cung cấp quyền truy cập vào các bản chuyển giao cơ bản mà không cung cấp chức năng ghi hoặc cập nhật, ví dụ;
- Thay đổi cách trình bày: thiết kế một Triển khai Giao diện đổi tên một trường trong Giao diện hoặc ánh xạ nó theo cách khác mà không làm thay đổi cơ sở của hợp đồng;
- Hỗ trợ nhiều lược đồ: ví có thể tải nhiều Triển khai Giao diện cho cùng một loại Giao diện để xử lý các lược đồ khác nhau (logic mã thông báo khác nhau), miễn là cấu trúc của chúng tương thích.

Ở chương tiếp theo, chúng ta sẽ xem xét cách thức chuyển nhượng hợp đồng và cách tạo hóa đơn RGB.

## Chuyển nhượng hợp đồng

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)

Trong chương này, chúng ta sẽ phân tích quá trình chuyển giao hợp đồng trong hệ sinh thái RGB. Để minh họa cho điều này, chúng ta sẽ xem xét Alice và Bob, những nhân vật chính thường thấy của chúng ta, những người muốn trao đổi một tài sản RGB. Chúng ta cũng sẽ trình bày một số trích đoạn lệnh từ công cụ dòng lệnh `rgb`, để xem nó hoạt động như thế nào trong thực tế.

### Hiểu về chuyển giao hợp đồng RGB

Hãy lấy ví dụ về giao dịch chuyển tiền giữa Alice và Bob. Trong ví dụ này, chúng ta giả sử Bob mới bắt đầu sử dụng RGB, trong khi Alice đã nắm giữ tài sản RGB trong ví của mình. Chúng ta sẽ xem Bob thiết lập môi trường của mình như thế nào, nhập hợp đồng có liên quan, sau đó yêu cầu chuyển tiền từ Alice và cuối cùng là cách Alice thực hiện giao dịch thực tế trên chuỗi khối Bitcoin.

#### 1) Cài đặt ví RGB

Trước hết, Bob cần cài đặt ví RGB, tức là phần mềm tương thích với giao thức. Ví này không chứa bất kỳ hợp đồng nào ngay từ đầu. Bob cũng sẽ cần:


- Ví Bitcoin để quản lý UTXO của bạn;
- Kết nối tới một nút Bitcoin (hoặc tới máy chủ Electrum) để bạn có thể xác định UTXO của mình và truyền bá các giao dịch trên mạng.

Xin nhắc lại, **Các tiểu bang sở hữu** trong RGB ám chỉ Bitcoin UTXO. Do đó, chúng ta phải luôn có thể quản lý và chi tiêu UTXO trong giao dịch Bitcoin kết hợp các cam kết mật mã (`Tapret` hoặc `Opret`) trỏ đến dữ liệu RGB.

#### 2) Thu thập thông tin hợp đồng

Sau đó, Bob cần lấy dữ liệu hợp đồng mà anh ấy quan tâm. Dữ liệu này có thể lưu hành qua bất kỳ kênh nào: trang web, email, ứng dụng nhắn tin... Trong thực tế, chúng được nhóm lại với nhau trong một ***lô hàng***, tức là một gói dữ liệu nhỏ chứa:


- **Genesis**, xác định trạng thái ban đầu của hợp đồng;
- **Sơ đồ** mô tả logic kinh doanh (kiểu nghiêm ngặt, tập lệnh xác thực, v.v.);
- **Giao diện**, xác định lớp trình bày (tên trường, thao tác có thể truy cập);
- **Triển khai Giao diện**, liên kết cụ thể Sơ đồ với Giao diện.

![RGB-Bitcoin](assets/fr/075.webp)

Tổng kích thước thường vào khoảng vài kilobyte, vì mỗi thành phần thường nặng dưới 200 byte. Cũng có thể phát sóng lô hàng này trong Base58, qua các kênh chống kiểm duyệt (như Nostr hoặc qua Lightning Network, chẳng hạn) hoặc dưới dạng mã QR.

#### 3) Nhập khẩu và xác nhận hợp đồng

Sau khi Bob nhận được lô hàng, anh ấy nhập nó vào ví RGB của mình. Sau đó, điều này sẽ:


- Kiểm tra xem Genesis và Schema có hợp lệ không;
- Tải giao diện và triển khai giao diện;
- Cập nhật kho dữ liệu phía máy khách của bạn.

Bây giờ Bob có thể thấy tài sản trong ví của mình (ngay cả khi anh ấy chưa sở hữu nó) và hiểu được những trường nào có sẵn, những thao tác nào có thể thực hiện... Sau đó, anh ấy cần liên hệ với một người thực sự sở hữu tài sản để chuyển nhượng. Trong ví dụ của chúng tôi, đó là Alice.

Quá trình khám phá ai nắm giữ một tài sản RGB nhất định cũng tương tự như việc tìm người trả tiền Bitcoin. Chi tiết về kết nối này phụ thuộc vào mục đích sử dụng (thị trường, kênh trò chuyện riêng tư, lập hóa đơn, bán hàng hóa và dịch vụ, lương...).

#### 4) Phát hành hóa đơn

Để bắt đầu chuyển giao tài sản RGB, trước tiên Bob phải xuất hóa đơn. Hóa đơn này được sử dụng để:


- Cho Alice biết loại thao tác cần thực hiện (ví dụ: `Chuyển` từ giao diện RGB20);
- Cung cấp cho Alice *định nghĩa con dấu* của Bob (tức là UTXO nơi anh ấy muốn nhận tài sản);
- Chỉ định số lượng thành phần hoạt tính cần thiết (ví dụ: 100 đơn vị).

Bob sử dụng công cụ `rgb` trên dòng lệnh. Giả sử anh ấy muốn 100 đơn vị mã thông báo có `ContractId` được biết đến, muốn dựa vào `Tapret` và chỉ định UTXO của nó (`456e3..dfe1:0`):

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

Chúng ta sẽ xem xét kỹ hơn cấu trúc của hóa đơn RGB ở cuối chương này.

#### 5) Truyền hóa đơn

Hóa đơn được tạo (ví dụ như URL: `rgb:2WBcas9.../RGB20/100+utxob:...`) chứa tất cả thông tin mà Alice cần để chuẩn bị chuyển khoản. Cũng giống như lô hàng, nó có thể được mã hóa nhỏ gọn (Base58 hoặc định dạng khác) và được gửi qua ứng dụng nhắn tin, email, Nostr...

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Chuẩn bị giao dịch ở phía Alice

Alice nhận được hóa đơn của Bob. Trong ví RGB của cô ấy, cô ấy có một kho chứa tài sản cần chuyển. Để chi tiêu UTXO chứa tài sản, trước tiên cô ấy phải tạo PSBT (*Giao dịch Bitcoin đã ký một phần*), tức là một giao dịch Bitcoin chưa hoàn thành, sử dụng UTXO mà cô ấy có:

```bash
alice$ wallet construct tx.psbt
```

Giao dịch cơ bản này (chưa được ký vào lúc này) sẽ được sử dụng để neo cam kết mật mã được liên kết với giao dịch chuyển tiền cho Bob. Do đó, UTXO của Alice sẽ được chi tiêu và trong đầu ra, chúng tôi sẽ đặt cam kết `Tapret` hoặc `Opret` cho Bob.

#### 7) Tạo lô hàng chuyển nhượng

Tiếp theo, Alice xây dựng ***lô hàng đầu cuối*** (đôi khi được gọi là "lô hàng chuyển giao") thông qua lệnh:

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

Tệp `consignment.rgb` mới này chứa:


- Toàn bộ lịch sử Chuyển đổi trạng thái cần thiết để xác thực tài sản cho đến thời điểm hiện tại (kể từ Genesis);
- Quá trình chuyển đổi trạng thái mới chuyển tài sản từ Alice sang Bob theo hóa đơn mà Bob đã phát hành;
- Giao dịch Bitcoin chưa hoàn tất (*giao dịch chứng kiến*) (`tx.psbt`), trong đó chi tiêu Con dấu sử dụng một lần của Alice, đã được sửa đổi để bao gồm cam kết mật mã với Bob.

Ở giai đoạn này, giao dịch vẫn chưa được phát trên mạng Bitcoin. Lô hàng lớn hơn lô hàng cơ bản vì nó bao gồm toàn bộ lịch sử (*chuỗi bằng chứng*) để chứng minh tính hợp pháp của tài sản.

#### 8) Bob kiểm tra và chấp nhận lô hàng

Alice chuyển **hàng gửi cuối cùng** này cho Bob. Sau đó Bob sẽ:


- Kiểm tra tính hợp lệ của Chuyển đổi trạng thái (đảm bảo lịch sử nhất quán, các quy tắc hợp đồng được tôn trọng, v.v.);
- Thêm nó vào kho dự trữ địa phương của bạn;
- Có thể tạo chữ ký (`sig:...`) trên lô hàng để chứng minh rằng lô hàng đã được kiểm tra và chấp thuận (đôi khi được gọi là "*phiếu lương*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Tùy chọn: Bob gửi xác nhận lại cho Alice (*phiếu lương*)

Nếu Bob muốn, anh ta có thể gửi chữ ký này trở lại cho Alice. Điều này cho biết:


- Rằng nó công nhận sự chuyển đổi là hợp lệ;
- Rằng anh ấy đồng ý cho phát sóng giao dịch Bitcoin.

Điều này không bắt buộc, nhưng nó có thể giúp Alice đảm bảo rằng sẽ không có tranh chấp nào xảy ra sau này về việc chuyển nhượng.

#### 10) Alice ký và công bố giao dịch

Sau đó Alice có thể:


- Kiểm tra chữ ký của Bob (`rgb check <sig>`);
- Ký vào *giao dịch chứng kiến* vẫn là PSBT (`ký hiệu ví`);
- Công bố giao dịch chứng kiến trên mạng Bitcoin (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Sau khi xác nhận, giao dịch này đánh dấu kết thúc quá trình chuyển nhượng. Bob trở thành chủ sở hữu mới của tài sản: giờ đây anh ta có một Trạng thái sở hữu trỏ đến UTXO mà anh ta kiểm soát, được chứng minh bằng sự hiện diện của cam kết trong giao dịch.

Tóm lại, đây là toàn bộ quá trình chuyển giao:

![RGB-Bitcoin](assets/fr/079.webp)

### Ưu điểm của chuyển đổi RGB


- Bảo mật** :

Chỉ có Alice và Bob có quyền truy cập vào tất cả dữ liệu Chuyển đổi trạng thái. Họ trao đổi thông tin này bên ngoài blockchain, thông qua các lô hàng. Các cam kết mật mã trong giao dịch Bitcoin không tiết lộ loại tài sản hoặc số lượng, điều này đảm bảo tính bảo mật cao hơn nhiều so với các hệ thống mã thông báo trên chuỗi khác.


- Xác thực phía khách hàng**:

Bob có thể kiểm tra tính nhất quán của giao dịch chuyển tiền bằng cách so sánh *giao dịch ký gửi* với *mỏ neo* trong chuỗi khối Bitcoin. Anh ấy không cần xác thực của bên thứ ba. Alice không phải công bố toàn bộ lịch sử trên chuỗi khối, điều này làm giảm tải cho giao thức cơ sở và cải thiện tính bảo mật.


- Nguyên tử đơn giản hóa**:

Các trao đổi phức tạp (ví dụ như hoán đổi nguyên tử giữa BTC và tài sản RGB) có thể được thực hiện trong một giao dịch duy nhất, tránh nhu cầu về các tập lệnh HTLC hoặc PTLC. Nếu thỏa thuận không được phát sóng, mọi người có thể sử dụng lại UTXO của họ theo những cách khác.

### Biểu đồ tóm tắt chuyển giao

Trước khi xem xét chi tiết các hóa đơn, đây là sơ đồ tóm tắt về luồng tổng thể của quá trình chuyển RGB:


- Bob cài đặt ví RGB và nhận được hợp đồng ký gửi ban đầu;
- Bob xuất hóa đơn ghi rõ UTXO nơi nhận tài sản;
- Alice nhận hóa đơn, xây dựng PSBT và tạo lô hàng đầu cuối;
- Bob chấp nhận, kiểm tra, thêm dữ liệu vào kho lưu trữ của mình và ký (*phiếu lương*) nếu cần thiết;
- Alice công bố giao dịch trên mạng Bitcoin;
- Việc xác nhận giao dịch sẽ chính thức chuyển nhượng.

![RGB-Bitcoin](assets/fr/080.webp)

Việc chuyển tiền minh họa cho tất cả sức mạnh và tính linh hoạt của giao thức RGB: một sàn giao dịch riêng tư, được xác thực ở phía máy khách, được neo tối thiểu và kín đáo trên blockchain Bitcoin, và vẫn giữ được tính bảo mật tốt nhất của giao thức (không có nguy cơ chi tiêu gấp đôi). Điều này khiến RGB trở thành một hệ sinh thái đầy hứa hẹn cho các giao dịch giá trị bảo mật và có khả năng mở rộng hơn so với các blockchain lập trình trên chuỗi.

### Hóa đơn RGB

Trong phần này, chúng tôi sẽ giải thích chi tiết cách **hóa đơn** hoạt động trong hệ sinh thái RGB và cách chúng cho phép các hoạt động (đặc biệt là chuyển khoản) được thực hiện bằng hợp đồng. Trước tiên, chúng ta sẽ xem xét các mã định danh được sử dụng, sau đó là cách chúng được mã hóa và cuối cùng là cấu trúc của hóa đơn được thể hiện dưới dạng URL (một định dạng đủ tiện dụng để sử dụng trong ví).

#### Mã định danh và mã hóa

Một mã định danh duy nhất được xác định cho mỗi phần tử sau:


- Hợp đồng RGB;
- Sơ đồ của nó (logic kinh doanh);
- Giao diện và triển khai giao diện của nó;
- Tài sản của nó (mã thông báo, NFT, v.v.),

Tính duy nhất này rất quan trọng vì mỗi thành phần của hệ thống phải có thể phân biệt được. Ví dụ, hợp đồng X không được nhầm lẫn với hợp đồng Y khác và hai giao diện khác nhau (ví dụ: RGB20 so với RGB21) phải có mã định danh riêng biệt.

Để làm cho các mã định danh này vừa hiệu quả (kích thước nhỏ) vừa dễ đọc, chúng tôi sử dụng:


- Mã hóa Base58, tránh sử dụng các ký tự gây nhầm lẫn (ví dụ: `0` và chữ `O`) và cung cấp các chuỗi tương đối ngắn;
- Tiền tố biểu thị bản chất của mã định danh, thường ở dạng `rgb:` hoặc URN tương tự.

Ví dụ, `ContractId` có thể được biểu diễn bằng nội dung như sau:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Tiền tố `rgb:` xác nhận rằng đây là mã định danh RGB chứ không phải liên kết HTTP hoặc giao thức khác. Nhờ tiền tố này, ví có thể diễn giải chuỗi chính xác.

#### Phân đoạn định danh

Mã định danh RGB thường khá dài vì bảo mật (mật mã) cơ bản có thể yêu cầu các trường 256 bit trở lên. Để tạo điều kiện cho con người đọc và xác minh, chúng tôi *chunk* các chuỗi này thành nhiều khối được phân tách bằng dấu gạch nối (`-`). Vì vậy, thay vì có một chuỗi ký tự dài, không bị gián đoạn, chúng tôi chia nó thành các khối ngắn hơn. Thực hành này phổ biến đối với thẻ tín dụng hoặc số điện thoại và cũng áp dụng ở đây để dễ xác minh. Vì vậy, ví dụ, người dùng hoặc đối tác có thể được yêu cầu: "*Vui lòng kiểm tra xem khối thứ ba có phải là `9GEgnyMj7`* không", thay vì phải so sánh toàn bộ cùng một lúc. Khối cuối cùng thường được sử dụng làm **tổng kiểm** để có hệ thống phát hiện lỗi hoặc lỗi đánh máy.

Ví dụ, `ContractId` được mã hóa và phân đoạn theo chuẩn base58 có thể là:

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Mỗi dấu gạch ngang chia chuỗi thành các phần. Điều này không ảnh hưởng đến ngữ nghĩa của mã, chỉ ảnh hưởng đến cách trình bày.

#### Sử dụng URL cho hóa đơn

Hóa đơn RGB được trình bày dưới dạng URL. Điều này có nghĩa là có thể nhấp hoặc quét (dưới dạng mã QR) và ví có thể trực tiếp diễn giải để thực hiện giao dịch. Sự đơn giản trong tương tác này khác với một số hệ thống khác, nơi bạn phải sao chép và dán nhiều phần dữ liệu khác nhau vào các trường khác nhau trong phần mềm.

Hóa đơn cho một mã thông báo có thể thay thế (ví dụ: mã thông báo RGB20) có thể trông như thế này:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Hãy cùng phân tích URL này:


- `rgb:`** (tiền tố): biểu thị liên kết gọi giao thức RGB (tương tự như `http:` hoặc `bitcoin:` trong các ngữ cảnh khác);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: biểu thị `ContractId` của mã thông báo mà bạn muốn thao tác;
- `/RGB20/100`**: chỉ ra rằng giao diện `RGB20` được sử dụng và 100 đơn vị tài sản được yêu cầu. Cú pháp là: `/Interface/amount` ;
- `+utxob:`**: chỉ định rằng thông tin về UTXO của người nhận (hay chính xác hơn là định nghĩa về Con dấu sử dụng một lần) được thêm vào;
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: đây là UTXO (hoặc định nghĩa niêm phong) *bị che giấu*. Nói cách khác, Bob đã che giấu UTXO chính xác của mình, vì vậy người gửi (Alice) không biết địa chỉ chính xác là gì. Cô ấy chỉ biết rằng có một niêm phong hợp lệ tham chiếu đến UTXO do Bob kiểm soát.

Thực tế là mọi thứ đều nằm trong một URL duy nhất giúp người dùng dễ dàng hơn: chỉ cần nhấp chuột hoặc quét vào ví là giao dịch đã sẵn sàng để thực hiện.

Người ta có thể tưởng tượng ra các hệ thống mà một mã đơn giản (ví dụ: `USDT`) được sử dụng thay cho `ContractId`. Tuy nhiên, điều này sẽ gây ra các vấn đề lớn về lòng tin và bảo mật: mã không phải là một tham chiếu duy nhất (một số hợp đồng có thể tuyên bố được gọi là `USDT`). Với RGB, chúng ta muốn có một mã định danh mật mã duy nhất, rõ ràng. Do đó, việc áp dụng chuỗi 256 bit, được mã hóa theo cơ số 58 và được phân đoạn. Người dùng biết rằng mình đang thao tác chính xác hợp đồng có ID là `2WBcas9-yjz...` chứ không phải bất kỳ hợp đồng nào khác.

#### Tham số URL bổ sung

Bạn cũng có thể thêm các tham số bổ sung vào URL theo cách tương tự như với HTTP, chẳng hạn như:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: ví dụ, biểu thị chữ ký liên quan đến hóa đơn, một số ví có thể xác minh chữ ký này;
- Nếu ví không quản lý chữ ký này, nó sẽ bỏ qua tham số này.

Hãy lấy trường hợp của NFT thông qua giao diện RGB21. Ví dụ, chúng ta có thể có:

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Ở đây chúng ta thấy:


- `rgb:`**: Tiền tố URL;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Mã hợp đồng (NFT);
- rGB21**: giao diện cho tài sản không thể thay thế (NFT);
- `DbwzvSu-4BZU81jEp-...`**: tham chiếu rõ ràng đến phần duy nhất của NFT, ví dụ như hàm băm của blob dữ liệu (phương tiện, siêu dữ liệu...);
- `+utxob:egXsFnw-...`**: định nghĩa con dấu.

Ý tưởng thì giống nhau: truyền một liên kết duy nhất mà ví có thể hiểu được, xác định rõ ràng tài sản duy nhất cần chuyển.

#### Các hoạt động khác thông qua URL

URL RGB không chỉ được sử dụng để yêu cầu chuyển giao. Chúng cũng có thể mã hóa các hoạt động nâng cao hơn, chẳng hạn như phát hành mã thông báo mới (*phát hành*). Ví dụ:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Ở đây chúng ta tìm thấy:


- `rgb:` : giao thức ;
- `2WBcas9-...`: ID hợp đồng;
- `/RGB20/issue/100000`: cho biết bạn muốn gọi quá trình chuyển đổi "*Issue*" để tạo thêm 100.000 mã thông báo;
- `+utxob:`: định nghĩa con dấu.

Ví dụ, ví có thể ghi: "Tôi được yêu cầu thực hiện một hoạt động `phát hành` từ giao diện `RGB20`, theo hợp đồng này, cho 100.000 đơn vị, vì lợi ích của Con dấu dùng một lần này.*"

Bây giờ chúng ta đã xem xét các yếu tố chính của lập trình RGB, tôi sẽ hướng dẫn bạn chương tiếp theo về cách soạn thảo hợp đồng RGB.

## Soạn thảo hợp đồng thông minh

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

Trong chương này, chúng ta sẽ thực hiện từng bước để viết hợp đồng, sử dụng công cụ dòng lệnh `rgb`. Mục đích là để chỉ cách cài đặt và thao tác CLI, biên dịch **Schema**, nhập **Interface** và **Interface Implementation**, sau đó phát hành (*issue*) một tài sản. Chúng ta cũng sẽ xem xét logic cơ bản, bao gồm biên dịch và xác thực trạng thái. Đến cuối chương này, bạn sẽ có thể tái tạo quy trình và tạo hợp đồng RGB của riêng mình.

Xin nhắc lại, logic nội bộ của RGB dựa trên các thư viện Rust mà bạn, với tư cách là nhà phát triển, có thể nhập vào các dự án của mình để quản lý phần Xác thực phía máy khách. Ngoài ra, nhóm Hiệp hội LNP/BP đang làm việc trên các ràng buộc cho các ngôn ngữ khác, nhưng điều này vẫn chưa được hoàn thiện. Ngoài ra, các thực thể khác như Bitfinex đang phát triển các ngăn xếp tích hợp của riêng họ (chúng ta sẽ nói về những điều này trong 2 chương cuối của khóa học). Do đó, hiện tại, CLI `rgb` là tài liệu tham khảo chính thức, ngay cả khi nó vẫn tương đối chưa được trau chuốt.

### Cài đặt và trình bày công cụ rgb

Lệnh chính chỉ đơn giản được gọi là `rgb`. Nó được thiết kế để gợi nhớ đến `git`, với một tập hợp các lệnh phụ để thao tác hợp đồng, gọi chúng, phát hành tài sản, v.v. Ví Bitcoin hiện chưa được tích hợp, nhưng sẽ có trong phiên bản sắp tới (0.11). Phiên bản tiếp theo này sẽ cho phép người dùng tạo và quản lý ví của họ (thông qua các mô tả) trực tiếp từ `rgb`, bao gồm tạo PSBT, khả năng tương thích với phần cứng bên ngoài (ví dụ: ví phần cứng) để ký và khả năng tương tác với phần mềm như Sparrow. Điều này sẽ đơn giản hóa toàn bộ kịch bản phát hành và chuyển giao tài sản.

#### Cài đặt qua Cargo

Chúng tôi cài đặt công cụ trong Rust bằng:

```bash
cargo install rgb-contracts --all-features
```

(Lưu ý: crate được gọi là `rgb-contracts` và lệnh được cài đặt sẽ được đặt tên là `rgb`. Nếu một crate có tên `rgb` đã tồn tại, có thể đã xảy ra va chạm, do đó có tên như vậy)

Quá trình cài đặt biên dịch một số lượng lớn các phụ thuộc (ví dụ: phân tích lệnh, tích hợp Electrum, quản lý bằng chứng không kiến thức, v.v.).

Sau khi cài đặt hoàn tất,:

```bash
rgb
```

Chạy `rgb` (không có đối số) sẽ hiển thị danh sách các lệnh phụ có sẵn, chẳng hạn như `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, v.v. Bạn có thể thay đổi thư mục lưu trữ cục bộ (nơi lưu trữ tất cả nhật ký, sơ đồ và triển khai), chọn mạng (testnet, mainnet) hoặc cấu hình máy chủ Electrum của bạn.

![RGB-Bitcoin](assets/fr/081.webp)

#### Tổng quan đầu tiên về các điều khiển

Khi bạn chạy lệnh sau, bạn sẽ thấy giao diện `RGB20` đã được tích hợp theo mặc định:

```bash
rgb interfaces
```

Nếu giao diện này không được tích hợp, hãy sao chép:

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Biên dịch nó:

```bash
cargo run
```

Sau đó nhập giao diện bạn chọn:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

Mặt khác, chúng tôi được thông báo rằng chưa có lược đồ nào được nhập vào phần mềm. Cũng không có hợp đồng nào trong stash. Để xem, hãy chạy lệnh:

```bash
rgb schemata
```

Sau đó, bạn có thể sao chép kho lưu trữ để lấy một số sơ đồ nhất định:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

Kho lưu trữ này chứa, trong thư mục `src/` của nó, một số tệp Rust (ví dụ `nia.rs`) định nghĩa các lược đồ (NIA cho "*Non Inflatable Asset*", UDA cho "*Unique Digital Asset*", v.v.). Để biên dịch, sau đó bạn có thể chạy:

```bash
cd rgb-schemata
cargo run
```

Điều này tạo ra một số tệp `.rgb` và `.rgba` tương ứng với sơ đồ đã biên dịch. Ví dụ, bạn sẽ tìm thấy `NonInflatableAsset.rgb`.

#### Nhập Sơ đồ và Triển khai Giao diện

Bây giờ bạn có thể nhập sơ đồ vào `rgb`:

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

Điều này thêm nó vào stash cục bộ. Nếu chúng ta chạy lệnh sau, chúng ta thấy rằng sơ đồ hiện xuất hiện:

```bash
rgb schemata
```

### Tạo hợp đồng (phát hành)

Có hai cách để tạo ra một tài sản mới:


- Chúng ta có thể sử dụng một tập lệnh hoặc mã trong Rust để xây dựng Hợp đồng bằng cách điền vào các trường lược đồ (trạng thái toàn cục, Trạng thái sở hữu, v.v.) và tạo ra tệp `.rgb` hoặc `.rgba`;
- Hoặc sử dụng trực tiếp lệnh phụ `issue`, với tệp YAML (hoặc TOML) mô tả thuộc tính của mã thông báo.

Bạn có thể tìm thấy các ví dụ trong Rust trong thư mục `examples`, minh họa cách bạn xây dựng `ContractBuilder`, điền vào `global state` (tên tài sản, mã chứng khoán, nguồn cung, ngày, v.v.), xác định Owned State (UTXO được gán cho tài sản đó), sau đó biên dịch tất cả những thông tin này thành một *hợp đồng ký gửi* mà bạn có thể xuất, xác thực và nhập vào một kho lưu trữ.

Cách khác là chỉnh sửa thủ công tệp YAML để tùy chỉnh `ticker`, `name`, `supply`, v.v. Giả sử tệp có tên là `RGB20-demo.yaml`. Bạn có thể chỉ định:


- `spec`: mã hiệu, tên, độ chính xác;
- `điều khoản`: một trường dành cho các thông báo pháp lý;
- `issuedSupply`: số lượng mã thông báo được phát hành;
- `assignments`: biểu thị Con dấu sử dụng một lần (*định nghĩa con dấu*) và số lượng đã mở khóa.

Sau đây là ví dụ về tệp YAML cần tạo:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

Sau đó chỉ cần chạy lệnh:

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

Trong trường hợp của tôi, định danh lược đồ duy nhất (được đặt trong dấu ngoặc đơn) là `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` và tôi chưa đặt bất kỳ đơn vị phát hành nào. Vì vậy, đơn hàng của tôi là:

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Nếu bạn không biết ID lược đồ, hãy chạy lệnh:

```bash
rgb schemata
```

CLI trả lời rằng một hợp đồng mới đã được phát hành và thêm vào stash. Nếu chúng ta nhập lệnh sau, chúng ta thấy rằng bây giờ có một hợp đồng bổ sung, tương ứng với hợp đồng vừa được phát hành:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

Sau đó, lệnh tiếp theo sẽ hiển thị các trạng thái toàn cầu (tên, mã chứng khoán, nguồn cung...) và danh sách các Trạng thái sở hữu, tức là các phân bổ (ví dụ: 1 triệu mã thông báo `PBN` được xác định trong UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Xuất, nhập và xác thực

Để chia sẻ hợp đồng này với những người dùng khác, bạn có thể xuất hợp đồng từ kho lưu trữ sang:

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

Tệp `myContractPBN.rgb` có thể được chuyển cho người dùng khác, người này có thể thêm tệp này vào kho lưu trữ của mình bằng lệnh:

```bash
rgb import myContractPBN.rgb
```

Khi nhập, nếu đó là *hợp đồng ký gửi* đơn giản, chúng ta sẽ nhận được thông báo "`Nhập ký gửi rgb`". Nếu đó là *chuyển tiếp trạng thái ký gửi* lớn hơn, lệnh sẽ khác (`rgb accept`).

Để đảm bảo tính hợp lệ, bạn cũng có thể sử dụng hàm xác thực cục bộ. Ví dụ, bạn có thể chạy:

```bash
rgb validate myContract.rgb
```

#### Sử dụng, xác minh và hiển thị Stash

Xin nhắc lại, stash là một kho lưu trữ cục bộ các lược đồ, giao diện, triển khai và hợp đồng (Genesis + transitions). Mỗi lần bạn chạy "import", bạn thêm một phần tử vào stash. Có thể xem stash này chi tiết bằng lệnh:

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

Thao tác này sẽ tạo ra một thư mục chứa thông tin chi tiết về toàn bộ kho lưu trữ.

### Chuyển và PSBT

Để thực hiện giao dịch chuyển tiền, bạn sẽ cần phải thao tác với ví Bitcoin cục bộ để quản lý các cam kết `Tapret` hoặc `Opret`.

#### Tạo hóa đơn

Trong hầu hết các trường hợp, tương tác giữa những người tham gia hợp đồng (ví dụ: Alice và Bob) diễn ra thông qua việc tạo hóa đơn. Nếu Alice muốn Bob thực hiện một việc gì đó (chuyển token, phát hành lại, hành động trong DAO, v.v.), Alice sẽ tạo hóa đơn nêu chi tiết hướng dẫn của cô ấy cho Bob. Vì vậy, chúng ta có:


- Alice** (người phát hành hóa đơn);
- Bob** (người nhận và thực hiện hóa đơn).

Không giống như các hệ sinh thái khác, hóa đơn RGB không giới hạn ở khái niệm thanh toán. Nó có thể nhúng bất kỳ yêu cầu nào được liên kết với hợp đồng: thu hồi khóa, bỏ phiếu, tạo bản khắc (*khắc*) trên NFT, v.v. Hoạt động tương ứng có thể được mô tả trong giao diện hợp đồng. Hoạt động tương ứng có thể được mô tả trong giao diện hợp đồng.

Lệnh sau đây tạo ra hóa đơn RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Với :


- `$CONTRACT`: Mã định danh hợp đồng (*ContractId*);
- `$INTERFACE`: giao diện sẽ được sử dụng (ví dụ: `RGB20`);
- `$ACTION`: tên của hoạt động được chỉ định trong giao diện (đối với một chuyển giao token có thể thay thế đơn giản, có thể là "Chuyển"). Nếu giao diện đã cung cấp một hành động mặc định, bạn không cần phải nhập lại ở đây;
- `$STATE`: dữ liệu trạng thái được chuyển (ví dụ: số lượng mã thông báo nếu mã thông báo có thể thay thế được chuyển);
- `$SEAL`: Con dấu sử dụng một lần của người thụ hưởng (Alice), tức là một tham chiếu rõ ràng đến UTXO. Bob sẽ sử dụng thông tin này để xây dựng giao dịch chứng kiến và đầu ra tương ứng sau đó sẽ thuộc về Alice (ở dạng *UTXO ẩn* hoặc không được mã hóa).

Ví dụ, với các lệnh sau

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI sẽ tạo ra hóa đơn như sau:

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Nó có thể được truyền tới Bob qua bất kỳ kênh nào (văn bản, mã QR, v.v.).

#### Thực hiện chuyển khoản

Để chuyển từ hóa đơn này:


- Bob (người giữ token trong kho của mình) có một ví Bitcoin. Anh ta cần chuẩn bị một giao dịch Bitcoin (dưới dạng PSBT, ví dụ: `tx.psbt`) để chi tiêu UTXO tại nơi có token RGB cần thiết, cộng với một UTXO để đổi tiền (trao đổi);
- Bob thực hiện lệnh sau:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Điều này tạo ra một tệp `consignment.rgb` chứa:
 - Lịch sử chuyển đổi chứng minh với Alice rằng các mã thông báo là chính hãng;
 - Quá trình chuyển đổi mới chuyển mã thông báo sang Con dấu dùng một lần của Alice;
 - Giao dịch có người chứng kiến (chưa ký).
- Bob gửi tệp `consignment.rgb` này cho Alice (qua e-mail, máy chủ chia sẻ hoặc giao thức RGB-RPC, Storm, v.v.);
- Alice nhận được `consignment.rgb` và chấp nhận nó trong kho lưu trữ riêng của nó:

```bash
alice$ rgb accept consignment.rgb
```


- CLI kiểm tra tính hợp lệ của quá trình chuyển đổi và thêm nó vào kho lưu trữ của Alice. Nếu không hợp lệ, lệnh sẽ không thành công với thông báo lỗi chi tiết. Nếu không, lệnh sẽ thành công và báo cáo rằng giao dịch mẫu vẫn chưa được phát trên mạng Bitcoin (Bob đang chờ đèn xanh của Alice);
- Để xác nhận, lệnh `accept` trả về một chữ ký (*phiếu lương*) mà Alice có thể gửi cho Bob để cho anh ta thấy rằng cô ấy đã xác thực *lệnh gửi*;
- Sau đó, Bob có thể ký và công bố (`--publish`) giao dịch Bitcoin của mình:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Ngay khi giao dịch này được xác nhận trên chuỗi, quyền sở hữu tài sản được coi là đã chuyển cho Alice. Ví của Alice, theo dõi quá trình khai thác của giao dịch, thấy Trạng thái sở hữu mới xuất hiện trong kho lưu trữ của nó.

Ở chương tiếp theo, chúng ta sẽ xem xét kỹ hơn cách tích hợp RGB vào Lightning Network.

## RGB trên Mạng Lightning

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

Trong chương này, tôi đề xuất xem xét cách RGB có thể được sử dụng trong Lightning Network để tích hợp và di chuyển tài sản RGB (mã thông báo, NFT, v.v.) thông qua các kênh thanh toán ngoài chuỗi.

Ý tưởng cơ bản là quá trình chuyển đổi trạng thái RGB (*Chuyển đổi trạng thái*) có thể được cam kết với một giao dịch Bitcoin, sau đó có thể vẫn nằm ngoài chuỗi cho đến khi kênh Lightning đóng lại. Vì vậy, mỗi lần kênh được cập nhật, một quá trình chuyển đổi trạng thái RGB mới có thể được kết hợp vào giao dịch cam kết mới, sau đó vô hiệu hóa quá trình chuyển đổi cũ. Theo cách này, các kênh Lightning có thể được sử dụng để chuyển tài sản RGB và có thể được định tuyến theo cùng một cách như các khoản thanh toán Lightning thông thường.

### Tạo kênh và tài trợ

Để tạo kênh Lightning mang nội dung RGB, chúng ta cần hai thành phần:


- Tài trợ Bitcoin để tạo ra đa chữ ký 2/2 của kênh (UTXO cơ bản cho kênh);
- Nguồn tài trợ RGB, gửi tài sản đến cùng một tổ chức đa chữ ký.

Theo thuật ngữ Bitcoin, giao dịch tài trợ phải tồn tại để xác định UTXO tham chiếu, ngay cả khi nó chỉ chứa một lượng nhỏ sats (chỉ là vấn đề của mỗi đầu ra trong các giao dịch cam kết trong tương lai vẫn ở trên giới hạn bụi). Ví dụ, Alice có thể quyết định cung cấp 10k sats và 500 USDT (được phát hành dưới dạng tài sản RGB). Trong giao dịch tài trợ, chúng tôi thêm một cam kết (`Opret` hoặc `Tapret`) neo giữ quá trình chuyển đổi trạng thái RGB.

![RGB-Bitcoin](assets/fr/091.webp)

Sau khi giao dịch tài trợ đã được chuẩn bị (nhưng chưa phát sóng), các giao dịch cam kết được tạo ra để bất kỳ bên nào cũng có thể đóng kênh một cách đơn phương bất kỳ lúc nào. Các giao dịch này giống với các giao dịch cam kết cổ điển của Lightning, ngoại trừ việc chúng tôi thêm một đầu ra bổ sung chứa neo RGB (OP_RETURN hoặc Taproot) được liên kết với quá trình chuyển đổi trạng thái mới.

Sau đó, quá trình chuyển đổi trạng thái RGB di chuyển tài sản từ 2/2 multisig của nguồn tài trợ đến đầu ra của giao dịch cam kết. Ưu điểm của quá trình này là tính bảo mật của trạng thái RGB khớp chính xác với cơ chế trừng phạt của Lightning: nếu Bob phát một trạng thái kênh cũ, Alice có thể trừng phạt anh ta và chi tiêu đầu ra, để khôi phục cả sats và mã thông báo RGB. Do đó, động cơ thậm chí còn mạnh hơn trong kênh Lightning không có tài sản RGB, vì kẻ tấn công có thể mất không chỉ sats mà còn cả tài sản RGB của kênh.

Do đó, giao dịch cam kết do Alice ký và gửi cho Bob sẽ trông như thế này:

![RGB-Bitcoin](assets/fr/092.webp)

Và giao dịch cam kết đi kèm, được Bob ký và gửi cho Alice, sẽ như thế này:

![RGB-Bitcoin](assets/fr/093.webp)

### Cập nhật kênh

Khi thanh toán xảy ra giữa hai bên tham gia kênh (hoặc họ muốn thay đổi phân bổ tài sản), họ tạo một cặp giao dịch cam kết mới. Số lượng sats trên mỗi đầu ra có thể không thay đổi hoặc không, tùy thuộc vào cách triển khai, vì vai trò chính của nó là cho phép xây dựng UTXO hợp lệ. Mặt khác, đầu ra OP_RETURN (hoặc Taproot) phải được sửa đổi để chứa neo RGB mới, biểu thị phân phối tài sản mới trong kênh.

Ví dụ, nếu Alice chuyển 30 USDT cho Bob trong kênh, quá trình chuyển đổi trạng thái mới sẽ phản ánh số dư là 400 USDT cho Alice và 100 USDT cho Bob. Giao dịch cam kết được thêm vào (hoặc sửa đổi bởi) neo OP_RETURN/Taproot để bao gồm quá trình chuyển đổi này. Lưu ý rằng, theo quan điểm của RGB, đầu vào cho quá trình chuyển đổi vẫn là đa chữ ký ban đầu (nơi các tài sản trên chuỗi thực sự được phân bổ cho đến khi kênh đóng). Chỉ có đầu ra RGB (phân bổ) thay đổi, tùy thuộc vào việc phân phối lại được quyết định.

Giao dịch cam kết được Alice ký, sẵn sàng để Bob phân phối:

![RGB-Bitcoin](assets/fr/094.webp)

Giao dịch cam kết được Bob ký, sẵn sàng để Alice phân phối:

![RGB-Bitcoin](assets/fr/095.webp)

### Quản lý HTLC

Trên thực tế, Lightning Network cho phép thanh toán được định tuyến qua nhiều kênh, sử dụng HTLC (*Hợp đồng khóa thời gian băm*). RGB cũng vậy: đối với mọi khoản thanh toán đang chuyển qua kênh, một đầu ra HTLC được thêm vào giao dịch cam kết và một phân bổ RGB được liên kết với HTLC này. Do đó, bất kỳ ai chi tiêu đầu ra HTLC (nhờ bí mật hoặc sau khi hết thời gian khóa) đều thu hồi được cả sats và tài sản RGB liên quan. Mặt khác, rõ ràng là bạn cần phải có đủ tiền mặt trên đường về cả sats và tài sản RGB.

![RGB-Bitcoin](assets/fr/096.webp)

Do đó, hoạt động của RGB trên Lightning phải được xem xét song song với hoạt động của chính Lightning Network. Nếu bạn muốn tìm hiểu sâu hơn về chủ đề này, tôi thực sự khuyên bạn nên xem khóa đào tạo toàn diện khác này:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
### Bản đồ mã RGB

Cuối cùng, trước khi chuyển sang phần tiếp theo, tôi muốn cung cấp cho bạn tổng quan về mã được sử dụng trong RGB. Giao thức này dựa trên một tập hợp các thư viện Rust và thông số kỹ thuật nguồn mở. Sau đây là tổng quan về các kho lưu trữ và thùng chính:

![RGB-Bitcoin](assets/fr/097.webp)

#### Xác thực phía máy khách


- Kho lưu trữ**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Thùng**: [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

Quản lý xác thực ngoài chuỗi và logic Con dấu sử dụng một lần.

#### Cam kết Bitcoin xác định (DBC)


- Kho lưu trữ**: [bp-core](https://github.com/BP-WG/bp-core)
- Thùng**: [bp-dbc](https://crates.io/crates/bp-dbc)

Quản lý neo xác định trong các giao dịch Bitcoin (Tapret, OP_RETURN, v.v.).

#### Cam kết đa giao thức (MPC)


- Kho lưu trữ**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crate** : [commit_verify](https://crates.io/crates/commit_verify)

Nhiều sự kết hợp tương tác và tích hợp với các giao thức khác nhau.

#### Các loại nghiêm ngặt & Mã hóa nghiêm ngặt


- Thông số kỹ thuật**: [trang web strict-types.org](https://www.strict-types.org/)
- Kho lưu trữ**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Thùng**: [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Hệ thống gõ nghiêm ngặt và tuần tự hóa xác định được sử dụng để xác thực phía máy khách.

#### Lõi RGB


- Kho lưu trữ**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- Thùng**: [rgb-core](https://crates.io/crates/rgb-core)

Cốt lõi của giao thức bao gồm logic chính của xác thực RGB.

#### Thư viện chuẩn RGB & Ví


- Kho lưu trữ**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- Thùng**: [rgb-std](https://crates.io/crates/rgb-std)

Triển khai chuẩn, quản lý kho lưu trữ và ví.

#### Giao diện dòng lệnh RGB


- Kho lưu trữ**: [rgb](https://github.com/RGB-WG/rgb)
- Thùng**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

`rgb` CLI và ví crate để thao tác hợp đồng bằng dòng lệnh.

#### Sơ đồ RGB


- Kho lưu trữ**: [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Bao gồm các ví dụ về lược đồ (NIA, UDA, v.v.) và cách triển khai của chúng.

#### ALuVM


- Thông tin**: [aluvm.org](https://www.aluvm.org/)
- Kho lưu trữ**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- Thùng**: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Máy ảo dựa trên sổ đăng ký được sử dụng để chạy các tập lệnh xác thực.

#### Giao thức Bitcoin - BP


- Kho lưu trữ**: [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Tiện ích bổ sung hỗ trợ giao thức Bitcoin (giao dịch, bỏ qua, v.v.).

#### Máy tính xác định phổ biến - UBIDECO


- Kho lưu trữ**: [UBIDECO](https://github.com/UBIDECO)

Hệ sinh thái liên kết với các phát triển mang tính quyết định nguồn mở.

# Xây dựng trên RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA và dự án Bitmask

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

Phần cuối cùng của khóa học này dựa trên các bài thuyết trình của nhiều diễn giả khác nhau tại trại huấn luyện RGB. Nó bao gồm các lời chứng thực và suy ngẫm về RGB và hệ sinh thái của nó, cũng như các bài thuyết trình về các công cụ và dự án dựa trên giao thức. Chương đầu tiên này được điều hành bởi Hunter Beast, và hai chương tiếp theo do Frederico Tenga điều hành.

### Từ JavaScript đến Rust và vào hệ sinh thái Bitcoin

Lúc đầu, Hunter Beast chủ yếu làm việc với JavaScript. Sau đó, anh ấy phát hiện ra **Rust**, cú pháp của nó có vẻ không hấp dẫn và gây khó chịu lúc đầu. Tuy nhiên, anh ấy đã đánh giá cao sức mạnh của ngôn ngữ, khả năng kiểm soát bộ nhớ (*heap* và *stack*), cũng như tính bảo mật và hiệu suất đi kèm với nó. Anh ấy nhấn mạnh rằng Rust là một nền tảng đào tạo tuyệt vời để hiểu sâu hơn về cách máy tính hoạt động.

Hunter Beast kể lại lý lịch của mình trong nhiều dự án khác nhau trong hệ sinh thái *altcoin*, chẳng hạn như Ethereum (với Solidity, TypeScript, v.v.), và sau đó là Filecoin. Ông giải thích rằng ban đầu ông ấn tượng với một số giao thức, nhưng cuối cùng lại cảm thấy thất vọng với hầu hết chúng, một phần là do tokenomics của chúng. Ông lên án các động cơ tài chính đáng ngờ, việc tạo ra các token lạm phát làm loãng các nhà đầu tư và khía cạnh có khả năng khai thác của các dự án này. Vì vậy, cuối cùng ông đã áp dụng lập trường **Bitcoin tối đa**, một phần là do một số người đã mở mắt ông ra với các cơ chế kinh tế lành mạnh hơn của Bitcoin và sự mạnh mẽ của hệ thống này.

### Sự hấp dẫn của RGB và xây dựng trên các lớp

Theo lời ông, điều chắc chắn thuyết phục ông về sự liên quan của Bitcoin là việc khám phá ra RGB và khái niệm về các lớp. Ông tin rằng các chức năng hiện có trên các blockchain khác có thể được tái tạo trên các lớp cao hơn, trên Bitcoin, mà không cần thay đổi giao thức cơ bản.

Vào tháng 2 năm 2022, anh ấy đã tham gia **DIBA** để làm việc cụ thể về RGB, và đặc biệt là về ví **Bitmask**. Vào thời điểm đó, Bitmask vẫn đang ở phiên bản 0.01 và đang chạy RGB ở phiên bản 0.4, chỉ để quản lý các mã thông báo đơn lẻ. Anh ấy lưu ý rằng điều này ít hướng đến việc tự lưu ký hơn so với ngày nay, vì logic một phần dựa trên máy chủ. Kể từ đó, kiến trúc đã phát triển theo hướng mô hình này, được những người dùng bitcoin đánh giá cao.

### Nền tảng của giao thức RGB

Giao thức **RGB** là hiện thân mới nhất và tiên tiến nhất của khái niệm _tiền xu màu_, đã được khám phá vào khoảng năm 2012-2013. Vào thời điểm đó, một số nhóm đang tìm cách liên kết các giá trị bitcoin khác nhau trên UTXO, dẫn đến nhiều triển khai rải rác. Việc thiếu chuẩn hóa này và nhu cầu thấp vào thời điểm đó đã ngăn cản các giải pháp này có được chỗ đứng lâu dài.

Ngày nay, RGB nổi bật với tính mạnh mẽ về mặt khái niệm và các thông số kỹ thuật thống nhất thông qua liên kết LNP/BP. Nguyên tắc này dựa trên xác thực phía máy khách. Chuỗi khối Bitcoin chỉ lưu trữ các cam kết mật mã (_cam kết_, thông qua Taproot hoặc OP_RETURN), trong khi phần lớn dữ liệu (định nghĩa hợp đồng, lịch sử chuyển nhượng, v.v.) được lưu trữ bởi người dùng liên quan. Theo cách này, tải lưu trữ được phân bổ và tính bảo mật của các giao dịch được tăng cường, mà không làm giảm khối lượng công việc. Cách tiếp cận này cho phép tạo ra các tài sản có thể thay thế (**chuẩn RGB20**) hoặc các tài sản duy nhất (**chuẩn RGB21**), trong một khuôn khổ có thể mở rộng và mô-đun.

### Chức năng mã thông báo (RGB20) và tài sản duy nhất (RGB21)

Với **RGB20**, chúng tôi định nghĩa một token có thể thay thế trên Bitcoin. Người phát hành chọn một _nguồn cung_, một _độ chính xác_ và tạo ra một _hợp đồng_ trong đó anh ta có thể thực hiện chuyển khoản. Mỗi lần chuyển khoản được tham chiếu đến một Bitcoin UTXO, hoạt động như một *Dấu niêm phong sử dụng một lần*. Logic này đảm bảo rằng người dùng sẽ không thể chi tiêu cùng một tài sản hai lần, vì chỉ người có khả năng chi tiêu UTXO mới thực sự nắm giữ khóa để cập nhật trạng thái của hợp đồng phía máy khách.

**RGB21** nhắm mục tiêu đến các tài sản duy nhất (hoặc "NFT"). Tài sản có nguồn cung là 1 và có thể được liên kết với siêu dữ liệu (tệp hình ảnh, âm thanh, v.v.) được mô tả thông qua một trường cụ thể. Không giống như NFT trên blockchain công khai, dữ liệu và mã định danh MIME của chúng có thể vẫn riêng tư, được phân phối ngang hàng theo quyết định của chủ sở hữu.

### Giải pháp Bitmask: ví cho RGB

Để khai thác khả năng của RGB trong thực tế, dự án **DIBA** đã thiết kế một ví có tên là [Bitmask](https://bitmask.app/). Ý tưởng là cung cấp một công cụ không lưu ký, dựa trên Taproot, có thể truy cập dưới dạng ứng dụng web hoặc tiện ích mở rộng của trình duyệt. Bitmask quản lý cả tài sản RGB20 và RGB21 và tích hợp nhiều cơ chế bảo mật khác nhau:


- Mã cốt lõi được viết bằng Rust, sau đó được biên dịch trong WebAssembly để chạy trong môi trường JavaScript (React);
- Khóa được tạo cục bộ, sau đó được lưu trữ dưới dạng mã hóa cục bộ;
- Dữ liệu trạng thái (stash) được lưu trong bộ nhớ, được tuần tự hóa và mã hóa thông qua thư viện **Carbonado**, thực hiện nén, sửa lỗi, mã hóa và xác minh luồng bằng Blake3.

Nhờ kiến trúc này, tất cả các giao dịch tài sản đều diễn ra ở phía máy khách. Nhìn từ bên ngoài, giao dịch Bitcoin không gì khác hơn là một giao dịch chi tiêu Taproot cổ điển, mà không ai ngờ rằng cũng mang theo một giao dịch chuyển nhượng token hoặc NFT. Việc không có quá tải trên chuỗi (không có siêu dữ liệu được lưu trữ công khai) đảm bảo một mức độ tùy ý nhất định và giúp chống lại các nỗ lực kiểm duyệt có thể xảy ra dễ dàng hơn.

### Bảo mật và kiến trúc phân tán

Trong chừng mực giao thức RGB yêu cầu mỗi người tham gia phải giữ lại lịch sử giao dịch của mình (để chứng minh tính hợp lệ của các giao dịch mà họ nhận được), thì vấn đề lưu trữ sẽ nảy sinh. Bitmask đề xuất tuần tự hóa kho lưu trữ này cục bộ, sau đó gửi đến một số máy chủ hoặc đám mây (tùy chọn). Dữ liệu vẫn được người dùng mã hóa thông qua **Carbonado**, do đó máy chủ không thể đọc được. Trong trường hợp bị hỏng một phần, lớp sửa lỗi có thể tái tạo nội dung.

Việc sử dụng CRDT (_Kiểu dữ liệu sao chép không xung đột_) cho phép hợp nhất các phiên bản khác nhau của stash, nếu chúng khác nhau. Mọi người đều có thể tự do lưu trữ dữ liệu này ở bất kỳ đâu họ muốn, vì không có nút đầy đủ nào mang tất cả thông tin được liên kết với tài sản. Điều này phản ánh chính xác triết lý *Xác thực phía máy khách*, trong đó mỗi chủ sở hữu có trách nhiệm lưu trữ bằng chứng về tính hợp lệ của tài sản RGB của họ.

### Hướng tới một hệ sinh thái rộng lớn hơn: thị trường, khả năng tương tác và các chức năng mới

Công ty đứng sau Bitmask không giới hạn mình chỉ phát triển ví đơn thuần. DIBA có ý định phát triển:


- Một **thị trường** để trao đổi mã thông báo, đặc biệt là ở dạng **RGB21**;
- Khả năng tương thích với các ví khác (như *Ví Iris*);
- Kỹ thuật chuyển hàng loạt**, tức là khả năng bao gồm nhiều lần chuyển RGB liên tiếp trong một giao dịch duy nhất.

Đồng thời, chúng tôi đang nghiên cứu **WebBTC** hoặc **WebLN** (các tiêu chuẩn cho phép các trang web yêu cầu ví ký các giao dịch Bitcoin hoặc Lightning), cũng như khả năng "teleburn" các mục Ordinals (nếu chúng tôi muốn hồi hương Ordinals sang định dạng RGB linh hoạt và kín đáo hơn).

### Phần kết luận

Toàn bộ quá trình cho thấy hệ sinh thái RGB có thể được triển khai và cung cấp cho người dùng cuối thông qua các giải pháp kỹ thuật mạnh mẽ như thế nào. Sự chuyển đổi từ góc nhìn altcoin sang tầm nhìn tập trung hơn vào Bitcoin, cùng với việc khám phá ra *Xác thực phía máy khách*, minh họa cho một con đường khá hợp lý: chúng tôi hiểu rằng có thể triển khai nhiều chức năng khác nhau (token có thể thay thế, NFT, hợp đồng thông minh...) mà không cần phân nhánh blockchain, chỉ cần tận dụng các cam kết mật mã trên các giao dịch Taproot hoặc OP_RETURN.

Ví **Bitmask** là một phần của phương pháp này: về phía blockchain, tất cả những gì bạn thấy là một giao dịch Bitcoin thông thường; về phía người dùng, bạn thao tác một giao diện web nơi bạn tạo, trao đổi và lưu trữ mọi loại tài sản ngoài chuỗi. Mô hình này rõ ràng tách biệt cơ sở hạ tầng tiền tệ (Bitcoin) khỏi logic phát hành và chuyển giao (RGB), đồng thời đảm bảo mức độ bảo mật cao và khả năng mở rộng tốt hơn.

## Công trình của Bitfinex trên RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

Trong chương này, dựa trên bài thuyết trình của Frederico Tenga, chúng ta sẽ xem xét một bộ công cụ và dự án do nhóm Bitfinex tạo ra dành riêng cho RGB, với mục đích thúc đẩy sự xuất hiện của một hệ sinh thái phong phú và đa dạng xung quanh giao thức này. Mục tiêu ban đầu của nhóm không phải là phát hành một sản phẩm thương mại cụ thể, mà là cung cấp các khối xây dựng phần mềm, đóng góp cho chính giao thức RGB và đề xuất các tham chiếu triển khai cụ thể như ví di động (*Iris Wallet*) hoặc nút Lightning tương thích với RGB.

### Bối cảnh và mục tiêu

Kể từ khoảng năm 2022, nhóm Bitfinex RGB đã tập trung vào việc phát triển công nghệ cho phép RGB được khai thác và thử nghiệm hiệu quả. Một số đóng góp đã được thực hiện:


- Tham gia vào mã nguồn và thông số kỹ thuật giao thức, bao gồm viết đề xuất cải tiến, sửa lỗi, v.v.;
- Công cụ dành cho nhà phát triển để đơn giản hóa việc tích hợp RGB vào ứng dụng của họ;
- Thiết kế ví di động có tên [Iris](https://iriswallet.com/) để thử nghiệm và minh họa các phương pháp hay nhất khi sử dụng RGB;
- Tạo một nút Lightning tùy chỉnh, có khả năng quản lý các kênh có nội dung RGB;
- Hỗ trợ các nhóm khác xây dựng giải pháp trên RGB để khuyến khích sự đa dạng và hệ sinh thái mạnh mẽ.

Phương pháp này nhằm mục đích đáp ứng toàn bộ chuỗi nhu cầu: từ thư viện cấp thấp (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), cho phép triển khai ví, đến khía cạnh sản xuất (nút Lightning, ví cho Android, v.v.).

### Thư viện RGBlib: đơn giản hóa việc phát triển các ứng dụng RGB

Một điểm quan trọng trong việc dân chủ hóa việc tạo ra ví RGB và các ứng dụng là tạo ra một sự trừu tượng đủ đơn giản để các nhà phát triển không phải học mọi thứ về logic bên trong của giao thức. Đây chính xác là mục đích của **RGBlib**, được viết bằng Rust.

RGBlib đóng vai trò là cầu nối giữa các yêu cầu rất linh hoạt (nhưng đôi khi phức tạp) của RGB mà chúng ta đã có thể nghiên cứu trong các chương trước và các nhu cầu cụ thể của nhà phát triển ứng dụng. Nói cách khác, một ví (hoặc dịch vụ) muốn quản lý việc chuyển token, phát hành tài sản, xác minh, v.v., có thể dựa vào RGBlib mà không cần biết mọi chi tiết mật mã hoặc mọi tham số RGB có thể tùy chỉnh.

Hiệu sách cung cấp:


- Chức năng chìa khóa trao tay để phát hành (_phát hành_) tài sản (có thể thay thế hoặc không);
- Khả năng chuyển giao (gửi/nhận) tài sản bằng cách thao tác các đối tượng đơn giản (địa chỉ, số tiền, UTXO, v.v.);
- Một cơ chế lưu trữ và tải thông tin trạng thái (*hàng gửi*) cần thiết cho Xác thực phía Máy khách.

Do đó, RGBlib dựa vào các khái niệm phức tạp dành riêng cho RGB (Xác thực phía máy khách, các neo Tapret/Opret), nhưng đóng gói chúng để ứng dụng cuối cùng không phải lập trình lại mọi thứ hoặc đưa ra quyết định rủi ro. Hơn nữa, RGBlib đã được liên kết trong một số ngôn ngữ (Kotlin và Python), mở ra cánh cửa cho các ứng dụng vượt ra ngoài vũ trụ Rust đơn giản.

### Ví Iris: một ví dụ về ví RGB trên Android

Để chứng minh tính hiệu quả của RGBlib, nhóm Bitfinex đã phát triển **Iris Wallet**, độc quyền trên Android ở giai đoạn này. Đây là ví di động minh họa trải nghiệm người dùng tương tự như ví Bitcoin thông thường: bạn có thể phát hành tài sản, gửi, nhận và xem lịch sử của tài sản đó, trong khi vẫn duy trì mô hình tự lưu ký.

Iris có một số đặc điểm thú vị:

**Sử dụng máy chủ Electrum:**

Giống như bất kỳ ví nào, Iris cần biết về xác nhận giao dịch trên blockchain. Thay vì nhúng một nút hoàn chỉnh, Iris mặc định là máy chủ Electrum do nhóm Bitfinex duy trì. Tuy nhiên, người dùng có thể cấu hình máy chủ của riêng họ hoặc dịch vụ của bên thứ ba khác. Theo cách này, các giao dịch Bitcoin có thể được xác thực và thông tin được truy xuất (lập chỉ mục) theo cách mô-đun.

**Máy chủ proxy RGB:**

Không giống như Bitcoin, RGB yêu cầu trao đổi siêu dữ liệu ngoài chuỗi (*giao dịch ký gửi*) giữa người gửi và người nhận. Để đơn giản hóa quy trình này, Iris cung cấp một giải pháp trong đó giao tiếp diễn ra thông qua máy chủ proxy. Ví nhận tạo ra một *hóa đơn* đề cập đến nơi người gửi nên gửi dữ liệu *phía máy khách*. Theo mặc định, URL trỏ đến proxy do nhóm Bitfinex lưu trữ, nhưng bạn có thể thay đổi proxy này (hoặc lưu trữ proxy của riêng bạn). Ý tưởng là quay lại trải nghiệm người dùng quen thuộc, trong đó người nhận hiển thị mã QR và người gửi quét mã này để thực hiện giao dịch mà không cần bất kỳ thao tác bổ sung phức tạp nào.

**Sao lưu liên tục:**

Trong bối cảnh Bitcoin nghiêm ngặt, việc sao lưu hạt giống của bạn thường là đủ (mặc dù hiện nay chúng tôi khuyên bạn nên sao lưu hạt giống và các mô tả thay thế). Với RGB, điều này là không đủ: bạn cũng cần lưu giữ lịch sử cục bộ (các *lô hàng*) để chứng minh rằng bạn thực sự sở hữu một tài sản RGB. Mỗi lần bạn nhận được biên lai, thiết bị sẽ lưu trữ dữ liệu mới, dữ liệu này rất cần thiết cho việc chi tiêu sau này. Iris tự động quản lý bản sao lưu được mã hóa trong Google Drive của người dùng. Điều này không yêu cầu sự tin tưởng đặc biệt nào vào Google, vì bản sao lưu được mã hóa và các tùy chọn mạnh mẽ hơn (như máy chủ cá nhân) được lên kế hoạch cho tương lai để tránh mọi rủi ro kiểm duyệt hoặc xóa bởi bên thứ ba.

**Các tính năng khác:**


- Tạo một vòi để nhanh chóng kiểm tra hoặc phân phối mã thông báo để thử nghiệm hoặc quảng bá;
- Một hệ thống chứng nhận (hiện đang tập trung) để phân biệt một mã thông báo hợp lệ với một mã thông báo giả mạo sao chép một mã thông báo nổi tiếng. Trong tương lai, chứng nhận này có thể trở nên phi tập trung hơn (thông qua DNS hoặc các cơ chế khác).

Nhìn chung, Iris cung cấp trải nghiệm người dùng gần giống với ví Bitcoin cổ điển, ẩn đi sự phức tạp bổ sung (quản lý kho, lịch sử *ký gửi*, v.v.) nhờ RGBlib và việc sử dụng máy chủ proxy.

### Máy chủ proxy và trải nghiệm của người dùng

Máy chủ proxy được giới thiệu ở trên xứng đáng được trình bày chi tiết, vì nó là chìa khóa cho trải nghiệm người dùng mượt mà. Thay vì người gửi phải truyền thủ công *hàng gửi* cho người nhận, giao dịch RGB diễn ra ở chế độ nền thông qua:


- Người nhận tạo một *hóa đơn* (có chứa nhiều thông tin, trong đó có địa chỉ proxy);
- Người gửi gửi (thông qua yêu cầu HTTP) một dự án chuyển tiếp (*lệnh gửi*) đến proxy;
- Người nhận lấy dự án này, thực hiện xác thực *phía máy khách* cục bộ;
- Sau đó, người nhận sẽ công bố, thông qua proxy, việc chấp nhận (hoặc có thể là từ chối) quá trình chuyển đổi trạng thái;
- Người gửi có thể xem trạng thái xác thực và nếu được chấp nhận, có thể phát giao dịch Bitcoin để hoàn tất việc chuyển tiền.

Theo cách này, ví hoạt động gần giống như một ví thông thường. Người dùng không biết tất cả các bước trung gian. Phải thừa nhận rằng, proxy hiện tại không được mã hóa hoặc xác thực (điều này gây ra mối lo ngại về tính bảo mật và tính toàn vẹn), nhưng những cải tiến này có thể thực hiện được trong các phiên bản sau. Khái niệm proxy vẫn cực kỳ hữu ích để tái tạo trải nghiệm "Tôi gửi mã QR, bạn quét để thanh toán".

### Tích hợp RGB trên Mạng Lightning

Một trọng tâm chính khác trong công việc của nhóm Bitfinex là làm cho Lightning Network tương thích với các tài sản RGB. Mục đích là cho phép các kênh Lightning trong USDT (hoặc bất kỳ mã thông báo nào khác) và hưởng lợi từ những lợi thế tương tự như bitcoin trên Lightning (giao dịch gần như tức thời, định tuyến, v.v.). Cụ thể, điều này liên quan đến việc tạo ra một nút Lightning được sửa đổi thành:


- Mở một kênh bằng cách đặt không chỉ satoshi mà còn một hoặc nhiều tài sản RGB vào UTXO đa chữ ký tài trợ;
- Tạo giao dịch cam kết Lightning (phía Bitcoin) kèm theo các chuyển đổi trạng thái RGB tương ứng. Mỗi lần kênh được cập nhật, một chuyển đổi RGB sẽ xác định lại phân phối tài sản trong đầu ra Lightning;
- Cho phép đóng đơn phương, trong đó tài sản được truy xuất trong UTXO độc quyền, tuân thủ các quy tắc của Lightning Network (HTLC, khóa thời gian, hình phạt, v.v.).

Giải pháp này, được gọi là "**RGB Lightning Node**", sử dụng LDK (*Lightning Dev Kit*) làm cơ sở và thêm các cơ chế cần thiết để đưa token RGB vào các kênh. Các cam kết Lightning vẫn giữ nguyên cấu trúc cổ điển (đầu ra có thể chấm điểm, khóa thời gian...), và ngoài ra còn neo chuyển đổi trạng thái RGB (thông qua `Opret` hoặc `Tapret`). Đối với người dùng, điều này mở đường cho các kênh Lightning trong stablecoin hoặc bất kỳ tài sản nào khác được phát ra thông qua RGB.

### Tiềm năng và tác động của DEX lên Bitcoin

Khi một số tài sản được quản lý thông qua Lightning, có thể hình dung ra một **trao đổi nguyên tử** trên một đường dẫn định tuyến Lightning duy nhất, sử dụng cùng một logic về bí mật và khóa thời gian. Ví dụ, người dùng A giữ bitcoin trên một kênh Lightning và người dùng B giữ USDT RGB trên một kênh Lightning khác. Họ có thể xây dựng một đường dẫn liên kết hai kênh của họ và đồng thời trao đổi BTC lấy USDT mà không cần phải tin tưởng. Đây không gì khác hơn là một **hoán đổi nguyên tử** diễn ra trong một số bước nhảy, khiến những người tham gia bên ngoài gần như không biết rằng họ đang thực hiện một giao dịch, không chỉ là một định tuyến. Cách tiếp cận này cung cấp:


- Độ trễ rất thấp vì mọi thứ đều nằm ngoài chuỗi trên Lightning.
- **Quyền riêng tư** cao hơn: không ai biết đó là giao dịch chứ không phải là tuyến đường bình thường;
- Tránh chạy trước, một vấn đề thường gặp đối với DEX trên chuỗi;
- Giảm chi phí (bạn không phải trả phí blockspace, chỉ phải trả phí định tuyến Lightning).

Sau đó, chúng ta có thể hình dung một hệ sinh thái nơi các nút Lightning cung cấp giá hoán đổi (bằng cách cung cấp thanh khoản). Mỗi nút, nếu muốn, có thể đóng vai trò là _nhà tạo lập thị trường_, mua và bán nhiều loại tài sản khác nhau trên Lightning. Triển vọng về _lớp-2_ DEX này củng cố ý tưởng rằng không cần phải phân nhánh hoặc sử dụng blockchain của bên thứ ba để có được các sàn giao dịch tài sản phi tập trung.

Tác động lên Bitcoin có thể là tích cực: Cơ sở hạ tầng của Lightning (các nút, kênh và dịch vụ) sẽ được sử dụng đầy đủ hơn nhờ vào khối lượng được tạo ra bởi các *stablecoin*, các sản phẩm phái sinh và các token khác. Các thương gia quan tâm đến thanh toán bằng USDT trên Lightning sẽ tự động khám phá ra các khoản thanh toán bằng BTC trên Lightning (do cùng một ngăn xếp quản lý). Việc bảo trì và tài trợ cho cơ sở hạ tầng của Lightning Network cũng có thể được hưởng lợi từ việc nhân lên các luồng không phải BTC này, điều này sẽ gián tiếp mang lại lợi ích cho người dùng Bitcoin.

### Kết luận và tài nguyên

Nhóm Bitfinex dành riêng cho RGB minh họa, thông qua công việc của mình, sự đa dạng của những gì có thể được thực hiện trên giao thức. Một mặt, có RGBlib, một thư viện tạo điều kiện thuận lợi cho việc thiết kế ví và ứng dụng. Mặt khác, chúng ta có Iris Wallet, một bản trình diễn thực tế trên Android về giao diện người dùng cuối gọn gàng. Cuối cùng, việc tích hợp RGB với Lightning cho thấy các kênh stablecoin là khả thi và mở đường cho một DEX phi tập trung tiềm năng trên Lightning.

Cách tiếp cận này phần lớn vẫn đang trong giai đoạn thử nghiệm và tiếp tục phát triển: thư viện RGBlib đang được cải tiến trong quá trình thực hiện, Iris Wallet đang nhận được những cải tiến thường xuyên và nút Lightning chuyên dụng vẫn chưa phải là máy khách Lightning chính thống.

Đối với những người muốn tìm hiểu thêm hoặc đóng góp, có một số tài nguyên có sẵn, bao gồm:


- [Kho lưu trữ Công cụ RGB của GitHub](https://github.com/RGB-Tools);
- [Trang thông tin dành riêng cho Iris Wallet](https://iriswallet.com/) để thử nghiệm ví trên Android.

Ở chương tiếp theo, chúng ta sẽ xem xét kỹ hơn cách khởi chạy một nút RGB Lightning.

## RLN - Nút RGB Lightning

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)

Trong chương cuối cùng này, Frederico Tenga sẽ hướng dẫn bạn từng bước thiết lập một nút Lightning RGB trên môi trường Regtest và chỉ cho bạn cách tạo mã thông báo RGB trên đó. Bằng cách khởi chạy hai nút riêng biệt, bạn cũng sẽ khám phá cách mở kênh Lightning giữa chúng và trao đổi tài sản RGB.

Video này đóng vai trò như một bài hướng dẫn, tương tự như nội dung chúng tôi đã đề cập trong chương trước, nhưng lần này tập trung cụ thể vào Lightning!

Tài nguyên chính cho video này là kho lưu trữ Github [RGB Lightning Node](https://github.com/RGB-Tools/rgb-lightning-node), giúp bạn dễ dàng khởi chạy cấu hình này trong Regtest.

### Triển khai một nút Lightning tương thích với RGB

Quá trình này tiếp thu và đưa vào thực hành tất cả các khái niệm đã đề cập trong các chương trước:


- Ý tưởng rằng **UTXO** bị chặn trên kênh Lightning đa chữ ký 2/2 không chỉ có thể nhận được bitcoin mà còn có thể là Con dấu sử dụng một lần của tài sản RGB (có thể thay thế hoặc không);
- Việc bổ sung, trong mỗi giao dịch tương tác Lightning, một đầu ra (`Tapret` hoặc `Opret`) dành riêng cho việc neo chuyển đổi trạng thái RGB;
- Cơ sở hạ tầng liên quan (bitcoind/indexer/proxy) để xác thực các giao dịch Bitcoin và trao đổi dữ liệu *phía máy khách*.

### Giới thiệu rgb-lightning-node

Dự án **`rgb-lightning-node`** là một daemon Rust dựa trên nhánh `rust-lightning` (LDK) được sửa đổi để tính đến sự tồn tại của các tài sản RGB trong một kênh. Khi một kênh được mở, sự hiện diện của các tài sản có thể được chỉ định và mỗi lần trạng thái kênh được cập nhật, một chuyển đổi RGB được tạo ra, phản ánh sự phân phối của tài sản trong các đầu ra Lightning. Điều này cho phép:


- Mở kênh Lightning bằng USDT, ví dụ;
- Định tuyến các mã thông báo này qua mạng, với điều kiện các đường dẫn định tuyến có đủ tính thanh khoản;
- Khai thác logic khóa thời gian và trừng phạt của Lightning mà không cần sửa đổi: chỉ cần neo chuyển đổi RGB trong đầu ra bổ sung của giao dịch cam kết.

Mã này vẫn đang ở giai đoạn alpha: chúng tôi khuyên bạn chỉ nên sử dụng nó trong **regtest** hoặc trên **testnet**.

### Cài đặt nút

Để biên dịch và cài đặt nhị phân `rgb-lightning-node`, chúng ta bắt đầu bằng cách sao chép kho lưu trữ và các mô-đun con của nó, sau đó chúng ta chạy:

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- Tùy chọn `--recurse-submodules` cũng sao chép các thiết bị phụ cần thiết (bao gồm cả phiên bản đã sửa đổi của `rust-lightning`);
- Tùy chọn `--shallow-submodules` hạn chế độ sâu của bản sao để tăng tốc độ tải xuống, đồng thời vẫn cung cấp quyền truy cập vào các cam kết cần thiết.

Từ thư mục gốc của dự án, chạy lệnh sau để biên dịch và cài đặt tệp nhị phân:

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--locked` đảm bảo rằng phiên bản của các phụ thuộc được tôn trọng nghiêm ngặt;
- `--debug` không bắt buộc, nhưng có thể giúp bạn tập trung (bạn có thể sử dụng `--release` nếu thích);
- `--path .` yêu cầu `cargo install` cài đặt từ thư mục hiện tại.

Vào cuối lệnh này, một tệp thực thi `rgb-lightning-node` sẽ có trong `$CARGO_HOME/bin/` của bạn. Đảm bảo đường dẫn này nằm trong `$PATH` của bạn để bạn có thể gọi lệnh từ bất kỳ thư mục nào.

### Yêu cầu về hiệu suất

Để hoạt động, daemon `rgb-lightning-node` yêu cầu sự hiện diện và cấu hình của:


- Một nút `bitcoind`**

Mỗi phiên bản RLN sẽ cần giao tiếp với `bitcoind` để phát và giám sát các giao dịch trên chuỗi của nó. Xác thực (đăng nhập/mật khẩu) và URL (máy chủ/cổng) sẽ cần được cung cấp cho daemon.


- Người lập chỉ mục** (Electrum hoặc Esplora)

Daemon phải có khả năng liệt kê và khám phá các giao dịch trên chuỗi, đặc biệt là tìm UTXO mà tài sản đã được neo vào. Bạn sẽ cần chỉ định URL của máy chủ Electrum hoặc Esplora.


- Một proxy RGB**

Như đã thấy trong các chương trước, **máy chủ proxy** là một thành phần (tùy chọn, nhưng được khuyến khích) để đơn giản hóa việc trao đổi *giao dịch* giữa các đối tác Lightning. Một lần nữa, phải chỉ định URL.

ID và URL được nhập khi daemon được _mở khóa_ thông qua API. Thông tin chi tiết về điều này sẽ được nêu sau.

### Ra mắt Regtest

Để sử dụng đơn giản, có một tập lệnh `regtest.sh` tự động khởi động một tập hợp các dịch vụ thông qua Docker: `bitcoind`, `electrs` (bộ lập chỉ mục), `rgb-proxy-server`.

![RGB-Bitcoin](assets/fr/100.webp)

Điều này cho phép bạn khởi chạy một môi trường cục bộ, bị cô lập, được cấu hình trước. Nó tạo và hủy các container và thư mục dữ liệu sau mỗi lần khởi động lại. Chúng ta sẽ bắt đầu bằng cách khởi động:

```bash
./regtest.sh start
```

Tập lệnh này sẽ:


- Tạo thư mục `docker/` để lưu trữ;
- Chạy `bitcoind` trong regtest, cũng như trình lập chỉ mục `electrs` và `rgb-proxy-server`;
- Chờ cho đến khi mọi thứ đã sẵn sàng để sử dụng.

![RGB-Bitcoin](assets/fr/101.webp)

Tiếp theo, chúng ta sẽ khởi chạy một số nút RLN. Trong các shell riêng biệt, hãy chạy, ví dụ (để khởi chạy 3 nút RLN):

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- Tham số `--network regtest` chỉ ra việc sử dụng cấu hình regtest;
- `--daemon-listening-port` chỉ ra cổng REST nào mà nút Lightning sẽ lắng nghe các lệnh gọi API (JSON);
- `--ldk-peer-listening-port` chỉ định cổng Lightning p2p nào sẽ được lắng nghe;
- `dataldk0/`, `dataldk1/` là các đường dẫn đến các thư mục lưu trữ (mỗi nút lưu trữ thông tin riêng biệt).

Bạn cũng có thể chạy lệnh trên các nút RLN của mình từ trình duyệt:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Để một nút mở kênh, trước tiên nó phải có bitcoin trên địa chỉ được tạo bằng lệnh sau (ví dụ: đối với nút số 1):

```bash
curl -X POST http://localhost:3001/address
```

Câu trả lời sẽ cung cấp cho bạn địa chỉ.

![RGB-Bitcoin](assets/fr/103.webp)

Trên Regtest `bitcoind`, chúng ta sẽ đào một vài bitcoin. Chạy:

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Gửi tiền đến địa chỉ nút được tạo ở trên:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Sau đó đào một khối để xác nhận giao dịch:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Ra mắt Testnet (không có Docker)

Nếu bạn muốn thử nghiệm một kịch bản thực tế hơn, bạn có thể khởi chạy 3 nút RLN trên Testnet thay vì trong Regtest, trỏ đến các dịch vụ công cộng:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Theo mặc định, nếu không tìm thấy cấu hình nào, daemon sẽ thử sử dụng:


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Với đăng nhập:


- `bitcoind_rpc_username`: `người dùng`
- `bitcoind_rpc_username`: `mật khẩu`

Bạn cũng có thể tùy chỉnh các thành phần này thông qua API `init`/`unlock`.

### Phát hành mã thông báo RGB

Để phát hành mã thông báo, chúng ta sẽ bắt đầu bằng cách tạo UTXO "có thể tô màu":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

Tất nhiên, bạn có thể điều chỉnh thứ tự. Để xác nhận giao dịch, chúng tôi khai thác:

```bash
./regtest.sh mine 1
```

Bây giờ chúng ta có thể tạo một tài sản RGB. Lệnh sẽ phụ thuộc vào loại tài sản bạn muốn tạo và các tham số của nó. Ở đây tôi đang tạo một mã thông báo NIA (*Tài sản không thể bơm phồng*) có tên là "PBN" với nguồn cung là 1000 đơn vị. `precision` cho phép bạn xác định khả năng chia hết của các đơn vị.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

Phản hồi bao gồm ID của tài sản mới được tạo. Hãy nhớ ghi lại mã định danh này. Trong trường hợp của tôi, đó là:

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

Sau đó, bạn có thể chuyển nó trên chuỗi hoặc phân bổ nó trong kênh Lightning. Đó chính xác là những gì chúng ta sẽ làm trong phần tiếp theo.

### Mở kênh và chuyển tài sản RGB

Trước tiên, bạn phải kết nối nút của mình với một nút ngang hàng trên mạng Lightning bằng lệnh `/connectpeer`. Trong ví dụ của tôi, tôi kiểm soát cả hai nút. Vì vậy, tôi sẽ lấy khóa công khai của nút Lightning thứ hai của mình bằng lệnh này:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Lệnh trả về khóa công khai của nút số 2 của tôi:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

Tiếp theo, chúng ta sẽ mở kênh bằng cách chỉ định tài sản có liên quan (`PBN`). Lệnh `/openchannel` cho phép bạn xác định kích thước của kênh theo satoshi và chọn bao gồm tài sản RGB. Tùy thuộc vào những gì bạn muốn tạo, nhưng trong trường hợp của tôi, lệnh là:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Tìm hiểu thêm tại đây:


- `peer_pubkey_and_opt_addr`: Mã định danh của đối tác mà chúng ta muốn kết nối (khóa công khai mà chúng ta đã tìm thấy trước đó);
- `capacity_sat`: Tổng dung lượng kênh tính bằng satoshi;
- `push_msat`: Số lượng tính bằng millisatoshi ban đầu được chuyển cho đối tác khi kênh được mở (ở đây tôi chuyển ngay 10.000 sats để đối tác có thể thực hiện chuyển RGB sau);
- `asset_amount`: Số lượng tài sản RGB được cam kết với kênh;
- `asset_id`: Mã định danh duy nhất của tài sản RGB được sử dụng trong kênh;
- `public`: Chỉ ra liệu kênh có nên được công khai để định tuyến trên mạng hay không.

![RGB-Bitcoin](assets/fr/111.webp)

Để xác nhận giao dịch, 6 khối được khai thác:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

Kênh Lightning hiện đã mở và cũng chứa 500 token `PBN` ở phía nút n°1. Nếu nút n°2 muốn nhận token `PBN`, nó phải tạo hóa đơn. Sau đây là cách thực hiện:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Với :


- `amt_msat`: Số tiền hóa đơn tính bằng millisatoshi (tối thiểu 3000 sats);
- `expiry_sec`: Thời gian hết hạn của hóa đơn tính bằng giây;
- `asset_id`: Mã định danh của tài sản RGB được liên kết với hóa đơn;
- `asset_amount`: Số lượng tài sản RGB sẽ được chuyển cùng với hóa đơn này.

Đáp lại, bạn sẽ nhận được hóa đơn RGB (như đã mô tả ở các chương trước):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

Bây giờ chúng ta sẽ thanh toán hóa đơn này từ nút đầu tiên, nơi lưu trữ số tiền mặt cần thiết bằng mã thông báo `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Thanh toán đã được thực hiện. Điều này có thể được xác minh bằng cách thực hiện lệnh:

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

Sau đây là cách triển khai một nút Lightning được sửa đổi để mang theo các tài sản RGB. Bản trình diễn này dựa trên:


- Môi trường regtest (thông qua `./regtest.sh`) hoặc testnet;
- Một nút Lightning (`rgb-lightning-node`) dựa trên `bitcoind`, một trình lập chỉ mục và một `rgb-proxy-server`;
- Một loạt các API REST JSON để mở/đóng kênh, phát hành mã thông báo, chuyển giao tài sản qua Lightning, v.v.

Nhờ vào quá trình này:


- Các giao dịch tương tác sét bao gồm một đầu ra bổ sung (OP_RETURN hoặc Taproot) với việc neo chuyển đổi RGB;
- Việc chuyển tiền được thực hiện theo cách hoàn toàn giống với phương thức thanh toán Lightning truyền thống, nhưng có thêm mã thông báo RGB;
- Nhiều nút RLN có thể được liên kết để định tuyến và thử nghiệm thanh toán trên nhiều nút, với điều kiện có đủ thanh khoản bằng cả bitcoin và tài sản RGB trên đường dẫn.

Dự án vẫn đang trong giai đoạn alpha. Do đó, chúng tôi khuyên bạn nên giới hạn bản thân trong các môi trường thử nghiệm (regtest, testnet).

Các cơ hội mở ra bởi khả năng tương thích LN-RGB này là rất đáng kể: stablecoin trên Lightning, DEX layer-2, chuyển giao các token có thể thay thế hoặc NFT với chi phí rất thấp... Các chương trước đã phác thảo kiến trúc khái niệm và logic xác thực. Bây giờ bạn đã có cái nhìn thực tế về cách đưa một nút như vậy vào hoạt động, cho các phát triển hoặc thử nghiệm trong tương lai của bạn.

# Phần kết luận

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>

## Đánh giá & Xếp hạng

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>
## Phần kết luận

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>