---
name: OXT - Phân Tích Chuỗi
description: Nắm vững cơ bản về phân tích chuỗi trên Bitcoin
---
![cover](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, **trang web OXT.me hiện không thể truy cập được**. Tuy nhiên, vẫn có khả năng công cụ này có thể được khởi động lại trong những tuần tới. Trong thời gian chờ đợi, bạn vẫn có thể hưởng lợi từ hướng dẫn này để hiểu cơ bản về phân tích chuỗi trên Bitcoin. Tất cả các phép suy luận và mô hình được trình bày ở đây vẫn áp dụng được cho các giao dịch Bitcoin. Mặc dù những công cụ này không được tối ưu như OXT, bạn có thể tạm thời sử dụng [Mempool.space](https://mempool.space/) hoặc [Bitcoin Explorer](https://bitcoinexplorer.org/) để áp dụng các khái niệm lý thuyết của bài viết này vào thực hành.*

_Chúng tôi đang ch closely theo dõi sự phát triển của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này chỉ mang tính chất giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng những công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ luật pháp tại quốc gia của họ._

---

Trong bài viết này, bạn sẽ học được những nền tảng lý thuyết cần thiết để bắt đầu phân tích chuỗi cơ bản trên Bitcoin, và quan trọng hơn, để hiểu cách những người quan sát bạn hoạt động. Mặc dù bài viết này không phải là hướng dẫn thực hành về công cụ OXT (chủ đề mà chúng tôi sẽ đề cập trong một hướng dẫn tương lai), nó tổng hợp một tập hợp kiến thức quan trọng cho việc sử dụng nó. Đối với mỗi mô hình, chỉ số, và chỉ báo được trình bày, một liên kết đến một giao dịch mẫu trên OXT được cung cấp, điều này sẽ giúp bạn hiểu rõ hơn về cách sử dụng và thực hành cùng với việc đọc.

## Giới Thiệu
Một trong những chức năng của tiền tệ là giải quyết vấn đề về sự trùng hợp kép của nhu cầu. Trong một hệ thống dựa trên trao đổi hàng hóa, việc hoàn thành một giao dịch không chỉ yêu cầu tìm kiếm một cá nhân đang cung cấp một hàng hóa đáp ứng nhu cầu của tôi mà còn phải cung cấp cho họ một hàng hóa có giá trị tương đương thỏa mãn nhu cầu của họ. Việc tìm kiếm sự cân bằng này chứng tỏ là phức tạp. Đó là lý do chúng ta sử dụng tiền tệ, cho phép chúng ta di chuyển giá trị cả về không gian và thời gian.

Để tiền tệ giải quyết vấn đề này, điều cần thiết là bên cung cấp hàng hóa hoặc dịch vụ phải tin tưởng vào khả năng của họ để chi tiêu số tiền đó sau này. Do đó, bất kỳ cá nhân hợp lý nào sẵn lòng chấp nhận một đồng tiền, dù là kỹ thuật số hay vật lý, sẽ đảm bảo rằng nó đáp ứng hai tiêu chí cơ bản:
- Đồng tiền phải nguyên vẹn và chính hãng;
- và nó không được chi tiêu hai lần.

Nếu chúng ta sử dụng tiền mặt, đặc điểm đầu tiên là phức tạp nhất để khẳng định. Ở các thời kỳ khác nhau trong lịch sử, tính toàn vẹn của đồng tiền kim loại thường xuyên bị ảnh hưởng bởi các hành vi như cắt xén hoặc khoan. Ví dụ, trong thời cổ đại Rome, việc người dân cạo mép của đồng tiền vàng để thu thập một chút kim loại quý, trong khi vẫn giữ chúng cho các giao dịch tương lai là điều phổ biến. Đây cũng là lý do tại sao sau này người ta đã dập rãnh trên mép của đồng tiền. Tính chính hãng cũng là một đặc điểm khó xác minh trên một phương tiện tiền tệ vật lý. Ngày nay, các kỹ thuật chống làm giả ngày càng phức tạp, buộc các nhà buôn phải đầu tư vào các hệ thống xác minh đắt tiền.

Mặt khác, do bản chất của chúng, việc chi tiêu hai lần không phải là vấn đề đối với tiền tệ vật lý. Nếu tôi đưa bạn một tờ €10, nó không thể quay trở lại tay tôi mà chuyển vào tay bạn, do đó loại trừ mọi khả năng chi tiêu nhiều lần các đơn vị tiền tệ mà nó đại diện.
Đối với tiền tệ số, thách thức là khác biệt. Đảm bảo tính xác thực và toàn vẹn của một đồng tiền thường đơn giản hơn, nhưng đảm bảo không có việc chi tiêu gấp đôi lại phức tạp hơn. Mọi hàng hóa số hóa về cơ bản là thông tin. Khác với hàng hóa vật lý, thông tin không bị chia nhỏ trong quá trình trao đổi mà được nhân bản. Ví dụ, nếu tôi gửi cho bạn một tài liệu qua email, nó sẽ được nhân bản. Ở phía bạn, bạn không thể xác minh chắc chắn rằng tôi đã xóa bản gốc của tài liệu.

Cách duy nhất để tránh sự nhân bản này của hàng hóa số là phải biết tất cả các giao dịch trên hệ thống. Như vậy, người ta có thể biết ai sở hữu cái gì và cập nhật tài khoản của mọi người dựa trên các giao dịch được thực hiện. Đây là những gì được thực hiện, ví dụ, với tiền ghi sổ. Khi bạn trả €10 cho một người bán hàng bằng thẻ tín dụng, ngân hàng ghi lại giao dịch này và cập nhật sổ cái.

Trên Bitcoin, việc ngăn chặn chi tiêu gấp đôi được thực hiện theo cùng một cách. Nó tìm cách xác nhận sự vắng mặt của một giao dịch đã chi tiêu các đồng tiền đó. Nếu những đồng tiền này chưa bao giờ được sử dụng, thì chúng ta có thể chắc chắn rằng không có việc chi tiêu gấp đôi nào xảy ra. Đây là câu nói nổi tiếng từ Satoshi Nakamoto trong Bản Trắng: "*Cách duy nhất để xác nhận sự vắng mặt của một giao dịch là phải biết tất cả các giao dịch.*"

Khác với mô hình ngân hàng, trên Bitcoin, chúng ta không muốn phải tin tưởng vào một thực thể trung tâm. Do đó, tất cả người dùng phải có thể xác nhận sự vắng mặt này của việc chi tiêu gấp đôi, mà không cần dựa vào bên thứ ba. Như vậy, mọi người phải biết tất cả các giao dịch Bitcoin.

Chính sự phổ biến công khai của thông tin này làm phức tạp việc bảo vệ quyền riêng tư trên Bitcoin. Trong hệ thống ngân hàng truyền thống, theo lý thuyết, chỉ có tổ chức tài chính biết về các giao dịch được thực hiện. Tuy nhiên, trên Bitcoin, tất cả người dùng đều được thông báo về tất cả các giao dịch, qua các nút tương ứng của họ.

Do ràng buộc này về sự phổ biến, mô hình quyền riêng tư của Bitcoin khác biệt so với hệ thống ngân hàng. Trong hệ thống sau, các giao dịch được liên kết với danh tính của người dùng, nhưng dòng thông tin bị cắt đứt giữa bên thứ ba đáng tin cậy và công chúng. Nói cách khác, người quản lý ngân hàng của bạn biết rằng bạn mua bánh mì baguette mỗi sáng tại tiệm bánh địa phương, nhưng hàng xóm của bạn không biết về tất cả các giao dịch này. Trong trường hợp của Bitcoin, do dòng thông tin không thể bị ngắt quãng giữa các giao dịch và lĩnh vực công cộng, mô hình quyền riêng tư dựa vào việc tách danh tính của người dùng khỏi chính các giao dịch.
![phân tích](assets/en/1.webp)
*Biểu đồ lấy cảm hứng từ Satoshi Nakamoto trong Bản Trắng: Bitcoin: Hệ thống Tiền tệ Điện tử Ngang hàng, mục 10 "Quyền riêng tư".*
Vì các giao dịch Bitcoin được công bố công khai, nên việc thiết lập liên kết giữa chúng để suy luận thông tin về các bên liên quan trở nên khả thi. Hoạt động này thậm chí còn là một chuyên môn riêng, thường được gọi là "phân tích chuỗi". Trong bài viết này, tôi mời bạn khám phá cơ bản của phân tích chuỗi để hiểu cách bitcoins của bạn được theo dõi.

Đa số các công ty chuyên về phân tích chuỗi hoạt động như những hộp đen và không tiết lộ phương pháp của họ. Do đó, việc thu thập thông tin về thực hành này trở nên khó khăn. Để viết bài viết này, tôi chủ yếu dựa vào một số nguồn tài nguyên mở có sẵn:
- Phần lớn bài viết của tôi được trích từ loạt bài viết gồm bốn phần có name: [Hiểu về Quyền riêng tư Bitcoin với OXT](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), do Samourai Wallet sản xuất vào năm 2021;
- Tôi cũng sử dụng các báo cáo khác nhau từ [OXT Research](https://medium.com/oxt-research), cũng như công cụ phân tích chuỗi miễn phí của họ;
- Rộng lớn hơn, kiến thức của tôi đến từ những tweet và nội dung khác nhau từ [@LaurentMT](https://twitter.com/LaurentMT) và [@ErgoBTC](https://twitter.com/ErgoBTC);- Tôi cũng được truyền cảm hứng từ [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) mà tôi đã tham gia cùng với [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), và [@LaurentMT](https://twitter.com/LaurentMT).

Tôi muốn cảm ơn các tác giả, nhà phát triển, và nhà sản xuất của họ. Không có các nội dung và phần mềm đa dạng của họ, bài viết này sẽ không tồn tại. Tôi cũng cảm ơn các nhà phê bình đã tỉ mỉ chỉnh sửa văn bản này và ban cho tôi lời khuyên chuyên môn của họ:
- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).

*Để bạn biết, tôi đã thêm một từ điển kỹ thuật ngắn ở cuối bài viết để định nghĩa một số thuật ngữ. Nếu bạn thấy một từ bạn không hiểu có dấu sao, định nghĩa của nó nằm ở cuối trang.*

## Phân tích chuỗi là gì?
Phân tích chuỗi là một thực hành bao gồm tất cả các phương pháp để theo dõi dòng Bitcoin trên blockchain. Nói chung, phân tích chuỗi dựa vào việc quan sát các đặc điểm trong mẫu của các giao dịch trước đó. Sau đó, nó liên quan đến việc xác định những đặc điểm tương tự trong một giao dịch mà người ta muốn phân tích và suy luận các giả thuyết có thể. Phương pháp giải quyết vấn đề này, dựa trên cách tiếp cận thực tế để tìm một giải pháp đủ tốt, là những gì được gọi là phép suy luận.

Để đơn giản hóa, phân tích chuỗi được thực hiện trong hai bước chính:
1. Xác định các đặc điểm đã biết;
2. Suy luận các giả thuyết.

Một trong những mục tiêu của phân tích chuỗi là để nhóm các hoạt động khác nhau trên Bitcoin để xác định tính độc đáo của người dùng đã thực hiện chúng. Sau đó, sẽ có thể cố gắng liên kết bó hoạt động này với một danh tính thực.

Hãy nhớ lại lời giới thiệu của tôi. Tôi đã giải thích tại sao mô hình bảo mật của Bitcoin ban đầu dựa vào việc tách biệt danh tính của người dùng khỏi các giao dịch của họ. Do đó, sẽ rất hấp dẫn khi nghĩ rằng phân tích chuỗi không cần thiết, vì ngay cả khi người ta quản lý để nhóm các hoạt động trên chuỗi, họ không thể liên kết chúng với một danh tính thực. Về lý thuyết, phát biểu này là chính xác. Các cặp khóa mật mã được sử dụng để thiết lập các điều kiện trên UTXOs. Bản chất, những cặp khóa này không tiết lộ bất kỳ thông tin nào về danh tính của người giữ chúng. Do đó, ngay cả khi người ta thành công trong việc nhóm các hoạt động liên quan đến các cặp khóa khác nhau, điều này không nói lên điều gì về thực thể đứng sau những hoạt động này.
Tuy nhiên, thực tế thực hành lại phức tạp hơn nhiều. Có một loạt các hành vi có nguy cơ liên kết danh tính thực của một người với hoạt động trên chuỗi. Trong phân tích, điều này được gọi là điểm nhập cảnh, và có rất nhiều điểm như vậy. Phổ biến nhất, tất nhiên, là KYC (Know Your Customer - Biết Khách Hàng của Bạn). Nếu bạn rút bitcoin của mình từ một nền tảng được quản lý về một trong những địa chỉ nhận cá nhân của bạn, thì một số người có thể liên kết danh tính của bạn với địa chỉ này. Một cách rộng lớn hơn, một điểm nhập cảnh có thể là bất kỳ hình thức tương tác nào giữa cuộc sống thực của bạn và một giao dịch Bitcoin. Ví dụ, nếu bạn công bố một địa chỉ nhận trên các mạng xã hội của mình, điều này có thể trở thành một điểm nhập cảnh cho phân tích. Nếu bạn thực hiện một khoản thanh toán bằng bitcoin cho người bán bánh của mình, họ có thể liên kết khuôn mặt của bạn (là một phần của danh tính của bạn) với một địa chỉ Bitcoin. Những điểm nhập cảnh này gần như không thể tránh khỏi khi sử dụng Bitcoin. Mặc dù người ta có thể tìm cách giới hạn phạm vi của chúng, chúng vẫn sẽ tồn tại. Đó là lý do tại sao việc kết hợp các phương pháp nhằm bảo vệ sự riêng tư của bạn là rất quan trọng. Mặc dù duy trì một sự tách biệt chấp nhận được giữa danh tính thực của bạn và các giao dịch của bạn là một cách tiếp cận đáng khen ngợi, nhưng nó vẫn không đủ. Thực tế, nếu tất cả các hoạt động trên chuỗi của bạn có thể được nhóm lại với nhau, thì ngay cả điểm nhập cảnh nhỏ nhất cũng có thể làm tổn hại đến lớp bảo vệ sự riêng tư duy nhất mà bạn đã thiết lập.

Do đó, việc xử lý phân tích chuỗi trong việc sử dụng Bitcoin của chúng ta cũng là cần thiết. Bằng cách làm như vậy, chúng ta có thể giảm thiểu việc tổng hợp các hoạt động của mình và giới hạn ảnh hưởng của một điểm nhập cảnh đối với sự riêng tư của mình. Cụ thể, để chống lại phân tích chuỗi một cách tốt hơn, cách tiếp cận tốt hơn là gì nếu không phải là làm quen với các phương pháp được sử dụng trong phân tích chuỗi? Nếu bạn muốn biết cách cải thiện sự riêng tư của mình trên Bitcoin, bạn phải hiểu những phương pháp này. Điều này sẽ cho phép bạn hiểu rõ hơn về các kỹ thuật như [Coinjoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) hoặc [Payjoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), và giảm thiểu những sai lầm bạn có thể mắc phải.

Trong điều này, chúng ta có thể rút ra một sự tương đồng với mật mã học và phân tích mật mã. Một nhà mật mã học giỏi trước hết là một nhà phân tích mật mã giỏi. Để tưởng tượng ra một thuật toán mã hóa mới, người ta phải biết nó sẽ đối mặt với những cuộc tấn công nào, và cũng nghiên cứu tại sao các thuật toán trước đó bị phá vỡ. Cùng một nguyên tắc áp dụng cho sự riêng tư trên Bitcoin. Hiểu các phương pháp của phân tích chuỗi là chìa khóa để bảo vệ chống lại nó. Đó là lý do tại sao tôi giới thiệu cho bạn bài viết này.

Quan trọng là phải hiểu rằng phân tích chuỗi không phải là một khoa học chính xác. Nó dựa trên các quy tắc suy luận được rút ra từ các quan sát trước đó hoặc các diễn giải lôgic. Những quy tắc này cho phép có kết quả tương đối đáng tin cậy, nhưng không bao giờ với độ chính xác tuyệt đối. Nói cách khác, phân tích chuỗi luôn bao gồm một khía cạnh về xác suất trong các kết luận rút ra. Chúng ta có thể ước lượng với độ chắc chắn ít nhiều rằng hai địa chỉ thuộc về cùng một thực thể, nhưng sự chắc chắn tuyệt đối luôn nằm ngoài tầm với.

Mục tiêu toàn bộ của phân tích chuỗi nằm chính xác trong việc tổng hợp các quy tắc suy luận khác nhau để giảm thiểu rủi ro sai lầm. Nó, theo một cách, là sự tích lũy bằng chứng cho phép chúng ta tiến gần hơn đến thực tế.

Những quy tắc suy luận nổi tiếng này có thể được nhóm vào các loại khác nhau mà chúng ta sẽ chi tiết cùng nhau:
- Mô hình giao dịch (hoặc mô hình giao dịch);
- Quy tắc suy luận nội bộ đối với giao dịch;
- Quy tắc suy luận bên ngoài đối với giao dịch.

Đáng chú ý là hai quy tắc suy luận đầu tiên trên Bitcoin được Satoshi Nakamoto tự mình đề xuất. Ông thảo luận về chúng trong phần 10 của Bản Trắng. Như chúng ta sẽ thấy sau, thú vị khi quan sát rằng hai quy tắc suy luận này vẫn giữ một vị thế quan trọng trong phân tích chuỗi ngày nay. Đó là:
- Quy tắc suy luận Sở Hữu Đầu Vào Chung (CIOH);
- và việc sử dụng lại địa chỉ.
Hãy cùng nhau khám phá các đặc điểm có thể quan sát được và những diễn giải có thể rút ra để tiến hành phân tích.
## Mô hình giao dịch (hoặc mô hình giao dịch)
Một mô hình giao dịch đơn giản là một mô hình giao dịch điển hình có thể tìm thấy trên blockchain, mà diễn giải của nó có thể được biết đến. Khi nghiên cứu các mô hình, chúng ta sẽ tập trung vào một giao dịch đơn lẻ mà chúng ta sẽ phân tích ở mức độ cao. Nói cách khác, chúng ta chỉ xem xét số lượng đầu vào và đầu ra, không đi sâu vào các chi tiết cụ thể hơn hoặc môi trường của nó. Từ mô hình quan sát được, chúng ta sẽ có thể diễn giải bản chất của giao dịch. Chúng ta sau đó sẽ tìm kiếm các đặc điểm về cấu trúc của nó và rút ra một diễn giải.

### Gửi đơn giản (hoặc thanh toán đơn giản)
Mô hình này được đặc trưng bởi việc tiêu thụ một hoặc nhiều UTXO làm đầu vào và tạo ra hai UTXO làm đầu ra.

![phân tích](assets/en/2.webp)

Diễn giải của mô hình này là chúng ta đang ở trong trường hợp của một giao dịch gửi hoặc thanh toán. Người dùng đã tiêu thụ UTXO của chính họ làm đầu vào để thỏa mãn trong đầu ra một UTXO thanh toán và một UTXO thay đổi (thay đổi quay trở lại cùng một người dùng). Do đó, chúng ta biết rằng người dùng quan sát được có khả năng không còn sở hữu một trong hai UTXO ở đầu ra (cái được thanh toán), nhưng vẫn còn sở hữu UTXO khác (cái thay đổi).

Tại thời điểm này, chúng ta không thể xác định đầu ra nào đại diện cho UTXO nào, vì đó không phải là mục tiêu của mô hình này. Chúng ta sẽ có thể làm điều đó bằng cách dựa vào các phương pháp suy luận mà chúng ta sẽ nghiên cứu trong phần tiếp theo. Tại giai đoạn này, mục tiêu của chúng ta giới hạn ở việc xác định bản chất của giao dịch đang được nói đến, đó, trong trường hợp này, là một gửi đơn giản.

Ví dụ, đây là một giao dịch Bitcoin tuân theo mô hình gửi đơn giản:
### Quét ("sweep" trong tiếng Anh)
Mô hình này được đặc trưng bởi việc tiêu thụ một UTXO duy nhất làm đầu vào và tạo ra một UTXO duy nhất làm đầu ra.

![phân tích](assets/en/3.webp)

Diễn giải của mô hình này là chúng ta đang ở trong trường hợp của một chuyển giao tự mình. Người dùng đã chuyển bitcoin của họ cho chính họ, sang một địa chỉ khác mà họ sở hữu. Thực sự, vì không có sự thay đổi nào trong giao dịch, rất khó có khả năng chúng ta đang xử lý một thanh toán. Chúng ta sau đó biết rằng người dùng quan sát được có khả năng vẫn còn sở hữu UTXO này.

Ví dụ, đây là một giao dịch Bitcoin tuân theo mô hình quét:
[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)

Tuy nhiên, loại mô hình này cũng có thể tiết lộ một chuyển giao tự mình sang một tài khoản giao dịch (nền tảng giao dịch tiền mã hóa). Việc nghiên cứu các địa chỉ được biết đến và bối cảnh của giao dịch sẽ cho phép chúng ta biết liệu đó có phải là một quét vào ví tự quản hay một rút tiền sang một nền tảng.

### Hợp nhất
Mô hình này được đặc trưng bởi việc tiêu thụ nhiều UTXO làm đầu vào và tạo ra một UTXO duy nhất làm đầu ra.

![phân tích](assets/en/4.webp)
Việc giải thích mô hình này là chúng ta đang chứng kiến một quá trình củng cố. Đây là một thực hành phổ biến trong số người dùng Bitcoin, nhằm mục đích hợp nhất nhiều UTXO trước khi có khả năng tăng phí giao dịch. Bằng cách thực hiện thao tác này trong một khoảng thời gian khi phí thấp, có thể tiết kiệm được phí trong tương lai.

Chúng ta có thể suy luận rằng người dùng đứng sau giao dịch này có khả năng sở hữu tất cả các UTXO ở đầu vào và vẫn giữ UTXO ở đầu ra. Do đó, chắc chắn đây là một giao dịch tự chuyển.

Giống như việc quét, mô hình này cũng có thể tiết lộ một giao dịch tự chuyển đến tài khoản trên sàn giao dịch. Việc nghiên cứu địa chỉ đã biết và bối cảnh của giao dịch sẽ cho phép chúng ta biết đó là một quá trình củng cố vào ví tự quản lý hay là một rút tiền đến nền tảng.

Ví dụ, đây là một giao dịch Bitcoin áp dụng mô hình củng cố:
[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)
### Mô Hình Chi Tiêu Hàng Loạt
Mô hình này được đặc trưng bởi việc tiêu thụ một vài UTXO ở đầu vào (thường chỉ một) và sản xuất nhiều UTXO ở đầu ra.

![phân tích](assets/en/5.webp)

Việc giải thích mô hình này là chúng ta đang chứng kiến một quá trình chi tiêu hàng loạt. Đây là một thực hành có khả năng tiết lộ hoạt động kinh tế đáng kể, chẳng hạn như một sàn giao dịch, ví dụ. Chi tiêu hàng loạt cho phép các thực thể này tiết kiệm phí bằng cách kết hợp chi tiêu của họ vào một giao dịch duy nhất.

Chúng ta có thể suy luận rằng UTXO đầu vào đến từ một công ty có hoạt động kinh tế đáng kể và các UTXO đầu ra sẽ được phân tán. Một số sẽ thuộc về khách hàng của công ty. Số khác có thể đi đến các công ty đối tác. Cuối cùng, chắc chắn sẽ có một phần thay đổi trở lại cho công ty phát hành.

Ví dụ, đây là một giao dịch Bitcoin áp dụng mô hình chi tiêu hàng loạt:
[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)

### Giao Dịch Đặc Thù của Giao Thức
Trong số các mô hình giao dịch, chúng ta cũng có thể xác định các mô hình tiết lộ việc sử dụng một giao thức cụ thể. Ví dụ, Whirlpool coinjoins sẽ có một cấu trúc dễ nhận biết cho phép chúng được phân biệt với các giao dịch cổ điển khác.

![phân tích](assets/en/6.webp)

Phân tích mô hình này gợi ý rằng chúng ta có khả năng đang chứng kiến một giao dịch hợp tác. Cũng có thể quan sát thấy một coinjoin. Nếu giả thuyết sau được chứng minh là chính xác, thì số lượng đầu ra có thể cung cấp cho chúng ta một ước lượng gần đúng về số lượng người tham gia.

Ví dụ, đây là một giao dịch Bitcoin áp dụng mô hình của loại giao dịch hợp tác coinjoin:
[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)
Có rất nhiều giao thức khác nhau có cấu trúc đặc thù của riêng mình. Do đó, chúng ta có thể phân biệt các giao dịch loại Wabisabi hoặc giao dịch Stamps, chẳng hạn.

## Heuristics Giao Dịch Nội Bộ
Heuristic nội bộ là một đặc điểm cụ thể được xác định trong chính giao dịch, không cần phải xem xét môi trường xung quanh, cho phép chúng ta đưa ra suy luận. Khác với các mẫu tập trung vào cấu trúc tổng thể của giao dịch, heuristic nội bộ dựa trên bộ dữ liệu có thể trích xuất. Điều này bao gồm:
- Số lượng các UTXO khác nhau cả đầu vào và đầu ra;
- Mọi thứ liên quan đến script: địa chỉ nhận, phiên bản, locktimes...

Nói chung, loại heuristic này cho phép chúng ta xác định sự thay đổi trong một giao dịch cụ thể. Bằng cách làm như vậy, chúng ta có thể tiếp tục theo dõi một thực thể qua nhiều giao dịch khác nhau.

Một lần nữa, tôi nhắc bạn rằng những heuristic này không hoàn toàn chính xác. Lấy riêng lẻ, chúng chỉ cho phép chúng ta xác định các kịch bản có thể. Chính sự tích lũy của nhiều heuristic góp phần giảm bớt sự không chắc chắn, mà không bao giờ loại bỏ hoàn toàn nó.

### Điểm Tương Đồng Nội Bộ
Heuristic này liên quan đến việc nghiên cứu sự tương đồng giữa các đầu vào và đầu ra của cùng một giao dịch. Nếu cùng một đặc điểm được quan sát trên các đầu vào và chỉ trên một đầu ra của giao dịch, thì có khả năng đầu ra này là sự thay đổi.

Đặc điểm rõ ràng nhất là việc tái sử dụng một địa chỉ nhận trong cùng một giao dịch.

![phân tích](assets/en/7.webp)

Heuristic này để lại ít phòng cho sự nghi ngờ. Trừ khi khóa riêng của họ đã bị xâm phạm, cùng một địa chỉ nhận không thể không tiết lộ hoạt động của một người dùng duy nhất. Sự diễn giải theo sau là sự thay đổi của giao dịch là đầu ra có cùng địa chỉ với đầu vào. Điều này cho phép chúng ta tiếp tục theo dõi cá nhân này từ sự thay đổi đó.

Ví dụ, đây là một giao dịch mà heuristic này có thể được áp dụng:
[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)

Những điểm tương đồng giữa các đầu vào và đầu ra không dừng lại ở việc tái sử dụng địa chỉ. Bất kỳ sự giống nhau nào trong việc sử dụng script cũng có thể cho phép áp dụng một heuristic. Ví dụ, đôi khi cùng một phiên bản giữa một đầu vào và một trong các đầu ra của giao dịch có thể được quan sát.

![phân tích](assets/en/8.webp)
Trong sơ đồ này, chúng ta có thể thấy rằng đầu vào số 0 mở khóa một script P2WPKH (SegWit V0 bắt đầu với "bc1q"). Đầu ra số 0 sử dụng cùng một loại script. Tuy nhiên, đầu ra số 1 sử dụng một script P2TR (SegWit V1 bắt đầu với "bc1p"). Sự diễn giải của đặc điểm này là có khả năng địa chỉ có cùng phiên bản với đầu vào là địa chỉ thay đổi. Do đó, nó vẫn thuộc về cùng một người dùng.
Đây là một giao dịch mà heuristic này có thể được áp dụng:
[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)
Trong giao dịch này, chúng ta có thể thấy rằng đầu vào số 0 và đầu ra số 1 sử dụng các script P2WPKH (SegWit V0), trong khi đầu ra số 0 sử dụng một loại script khác, P2PKH (Legacy).
### Thanh Toán Số Tròn
Một phép suy luận nội bộ khác có thể giúp chúng ta xác định đầu ra thay đổi là phép suy luận về số tròn. Nói chung, khi đối mặt với một mô hình thanh toán đơn giản (1 đầu vào và 2 đầu ra), nếu một trong các đầu ra chi tiêu một số tiền tròn, thì nó đại diện cho khoản thanh toán.

![phân tích](assets/en/9.webp)

Bằng cách loại trừ, nếu một đầu ra đại diện cho khoản thanh toán, đầu ra còn lại đại diện cho sự thay đổi. Do đó, chúng ta có thể giải thích rằng có khả năng người dùng ở đầu vào vẫn giữ đầu ra được xác định là sự thay đổi.

Cần lưu ý rằng phép suy luận này không phải lúc nào cũng áp dụng được, vì phần lớn các khoản thanh toán vẫn được thực hiện bằng đơn vị tiền tệ fiat. Thực tế, khi một người bán hàng ở Pháp chấp nhận bitcoin, họ thường không hiển thị giá cố định bằng sats. Họ sẽ chọn phương án chuyển đổi giữa giá bằng euro và số lượng bitcoin cần thanh toán. Do đó, không nên có một số tròn trong đầu ra giao dịch. Tuy nhiên, một nhà phân tích có thể cố gắng thực hiện việc chuyển đổi này, tính toán dựa trên tỷ giá hối đoái hiệu lực khi giao dịch được phát sóng trên mạng.

Nếu một ngày nào đó, bitcoin trở thành đơn vị tính toán ưa thích trong giao dịch của chúng ta, phép suy luận này có thể trở nên hữu ích hơn nhiều cho việc phân tích.

Ví dụ, đây là một giao dịch mà phép suy luận này có thể được áp dụng:
### Khoản Chi Tiêu Lớn

Khi một khoảng cách đủ lớn được phát hiện giữa hai đầu ra giao dịch trong một mô hình thanh toán đơn giản, có thể ước lượng rằng đầu ra lớn hơn có khả năng là sự thay đổi.

![phân tích](assets/en/10.webp)

Phép suy luận về đầu ra lớn nhất có lẽ là không chính xác nhất trong tất cả. Nếu được xác định một mình, nó khá yếu. Tuy nhiên, đặc điểm này có thể được kết hợp với các phép suy luận khác để giảm bớt sự không chắc chắn trong cách giải thích của chúng ta.

Ví dụ, nếu chúng ta xem xét một giao dịch có một đầu ra với một số tiền tròn và một đầu ra khác với số lượng lớn hơn, việc áp dụng chung phép suy luận về thanh toán số tròn và phép suy luận về đầu ra lớn nhất cho phép chúng ta giảm bớt mức độ không chắc chắn của mình.

Ví dụ, đây là một giao dịch mà phép suy luận này có thể được áp dụng:
[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)

## Phép Suy Luận Bên Ngoài Giao Dịch
Việc nghiên cứu các phép suy luận bên ngoài là phân tích sự giống nhau, các mô hình, và đặc điểm của một số yếu tố không phải là bản chất của chính giao dịch. Nói cách khác, nếu trước đây chúng ta chỉ giới hạn việc khai thác các yếu tố nội tại của giao dịch với các phép suy luận nội bộ, bây giờ chúng ta mở rộng lĩnh vực phân tích của mình ra môi trường giao dịch nhờ vào các phép suy luận bên ngoài.

### Tái Sử Dụng Địa Chỉ
Đây là một trong những phép suy luận được biết đến nhiều nhất trong số các Bitcoiner. Tái sử dụng địa chỉ cho phép thiết lập một liên kết giữa các giao dịch và các UTXO khác nhau. Nó được quan sát khi một địa chỉ nhận Bitcoin được sử dụng nhiều lần.

Việc giải thích tái sử dụng địa chỉ là tất cả các UTXO bị khóa trên địa chỉ này thuộc về (hoặc đã thuộc về) cùng một thực thể. Phép suy luận này để lại ít không gian cho sự không chắc chắn. Khi nó được xác định, giải thích theo sau có khả năng cao tương ứng với thực tế.
Như đã giải thích trong phần giới thiệu, phương pháp suy luận này được phát hiện bởi chính Satoshi Nakamoto. Trong Bản Trắng, ông cụ thể đề cập đến một giải pháp để ngăn chặn người dùng sản xuất nó, đó là sử dụng một địa chỉ mới cho mỗi giao dịch mới: "*Như một bức tường lửa bổ sung, một cặp khóa mới có thể được sử dụng cho mỗi giao dịch để giữ chúng không liên kết với một chủ sở hữu chung.*"
Ví dụ, đây là một địa chỉ được sử dụng lại qua nhiều giao dịch:
[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://mempool.space/address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)

### Sự Tương Đồng của Kịch Bản và Dấu Vân Tay Ví
Ngoài việc sử dụng lại địa chỉ, có nhiều phương pháp suy luận khác có thể liên kết các hành động với cùng một ví hoặc một cụm địa chỉ.

Đầu tiên, một nhà phân tích có thể sử dụng sự tương đồng trong việc sử dụng kịch bản. Ví dụ, các kịch bản thiểu số như multisig có thể dễ dàng được phát hiện hơn so với các kịch bản SegWit V0. Càng nhiều người chúng ta ẩn mình trong, thì càng khó để bị phát hiện. Điều này đặc biệt là lý do tại sao, trên giao thức Coinjoin Whirlpool, tất cả các thành viên sử dụng chính xác cùng một loại kịch bản.

Một cách rộng lớn hơn, một nhà phân tích cũng có thể tập trung vào các dấu vân tay đặc trưng của một ví. Đây là các quy trình cụ thể cho một sử dụng mà người ta có thể tìm cách xác định để khai thác chúng như các phương pháp suy luận truy vết. Nói cách khác, nếu một người quan sát sự tích tụ của cùng một đặc điểm nội bộ trên các giao dịch được gán cho thực thể đang được truy vết, người đó có thể cố gắng xác định những đặc điểm tương tự trên các giao dịch khác.

Ví dụ, có thể xác định rằng người dùng được truy vết hệ thống gửi tiền thừa của họ đến các địa chỉ P2TR* (bc1p…). Nếu quy trình này lặp lại, nó có thể được sử dụng như một phương pháp suy luận cho việc tiếp tục phân tích của chúng ta. Các dấu vân tay khác cũng có thể được sử dụng, như thứ tự của các UTXOs, vị trí của tiền thừa trong các đầu ra, việc báo hiệu RBF (Replace-by-Fee), hoặc thậm chí, số phiên bản và thời gian khóa.
Như [@LaurentMT](https://twitter.com/LaurentMT) đã chỉ ra trong [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (một podcast bằng tiếng Pháp), việc sử dụng dấu vân tay ví trong phân tích chuỗi ngày càng trở nên quan trọng theo thời gian. Thực vậy, số lượng loại kịch bản ngày càng tăng và việc triển khai dần dần những tính năng mới này bởi phần mềm ví làm tăng sự khác biệt. Thậm chí, người ta có thể chính xác xác định phần mềm được sử dụng bởi thực thể đang được truy vết. Do đó, quan trọng là phải hiểu rằng việc nghiên cứu dấu vân tay của một ví đặc biệt liên quan đến các giao dịch gần đây, hơn là những giao dịch được khởi xướng vào đầu những năm 2010.
Tóm lại, một dấu vân tay có thể là bất kỳ thực hành cụ thể nào, được thực hiện tự động bởi ví hoặc thủ công bởi người dùng, có thể được tìm thấy trên các giao dịch khác để hỗ trợ trong phân tích của chúng ta.

### CIOH
CIOH, viết tắt của "Common Input Ownership Heuristic," có thể được dịch là "phương pháp suy luận về sở hữu chung của các đầu vào" hoặc "phương pháp suy luận cùng chi tiêu," là một phương pháp suy luận cho rằng khi một giao dịch có nhiều đầu vào, những đầu vào này có khả năng đều đến từ một thực thể duy nhất. Do đó, sở hữu của chúng là chung.
Để áp dụng CIOH, trước tiên người ta quan sát một giao dịch có nhiều đầu vào. Điều này có thể là hai đầu vào, cũng như ba mươi đầu vào. Một khi đặc điểm này được phát hiện, người ta kiểm tra xem giao dịch có không thuộc về một mẫu đã biết. Ví dụ, nếu nó có 5 đầu vào với số lượng gần như nhau và 5 đầu ra với số lượng chính xác như nhau, chúng ta biết đó là cấu trúc của một Coinjoin Whirlpool. Do đó, CIOH không thể được áp dụng.
Tuy nhiên, nếu giao dịch không thuộc về bất kỳ mẫu giao dịch hợp tác nào đã biết, thì có thể hiểu rằng tất cả các đầu vào có khả năng đến từ cùng một thực thể. Điều này có thể rất hữu ích để mở rộng một cụm đã biết hoặc để tiếp tục theo dõi.

![phân tích](assets/en/11.webp)

CIOH được phát hiện bởi Satoshi Nakamoto. Ông thảo luận về nó trong phần 10 của Bản Trắng: "*[...] mối liên kết là không thể tránh khỏi với các giao dịch đa đầu vào, chúng chắc chắn tiết lộ rằng các đầu vào của chúng thuộc về cùng một chủ sở hữu. Rủi ro là nếu chủ sở hữu của một khóa được tiết lộ, các liên kết có thể tiết lộ các giao dịch khác thuộc về cùng một chủ sở hữu.*"
Điều đặc biệt thú vị là Satoshi Nakamoto, ngay cả trước khi Bitcoin chính thức ra mắt, đã nhận diện được hai lỗ hổng quyền riêng tư chính đối với người dùng, đó là CIOH và việc tái sử dụng địa chỉ. Sự nhìn xa trông rộng này thật đáng chú ý, vì đến nay, hai phép suy luận này vẫn là hữu ích nhất trong phân tích chuỗi.

### Dữ Liệu Ngoài Chuỗi
Rõ ràng, phân tích chuỗi không giới hạn ở dữ liệu trên chuỗi. Bất kỳ dữ liệu nào từ phân tích trước đó hoặc có thể truy cập trên Internet cũng có thể được sử dụng để tinh chỉnh phân tích.

Ví dụ, nếu quan sát thấy các giao dịch được theo dõi luôn được phát sóng từ cùng một nút Bitcoin và địa chỉ IP của nó có thể được xác định, có thể có khả năng phát hiện các giao dịch khác từ cùng một thực thể.

Nhà phân tích cũng có lựa chọn dựa vào các phân tích trước đó đã được công bố mã nguồn mở, hoặc trên các phân tích trước đó của chính họ. Có thể người ta sẽ tìm thấy một đầu ra chỉ đến một cụm địa chỉ đã được xác định trước đó. Đôi khi, cũng có thể dựa vào các đầu ra chỉ đến một sàn giao dịch, địa chỉ của các nền tảng này thường được biết đến.

Tương tự, người ta có thể thực hiện phân tích bằng cách loại trừ. Ví dụ, nếu trong quá trình phân tích một giao dịch với hai đầu ra, một trong số chúng được liên kết với một cụm địa chỉ đã biết nhưng khác biệt từ thực thể đang được theo dõi, thì có thể hiểu rằng đầu ra khác có khả năng đại diện cho tiền thối.

Phân tích chuỗi cũng bao gồm một phần của OSINT (Open Source Intelligence) có phần tổng quát hơn với các tìm kiếm trên internet. Đây là lý do tại sao không nên đăng địa chỉ nhận trực tiếp trên mạng xã hội hoặc trên một trang web, dù dưới một bí danh hay không.

### Mô Hình Thời Gian
Có thể bạn không ngay lập tức nghĩ đến nó, nhưng một số hành vi con người có thể được nhận biết trên chuỗi. Hữu ích nhất trong một nghiên cứu là mô hình giấc ngủ của bạn! Vâng, khi bạn đang ngủ, bạn có lẽ không phát sóng giao dịch Bitcoin. Vì bạn thường ngủ vào khoảng cùng một giờ, việc sử dụng các phân tích thời gian trong phân tích chuỗi là phổ biến. Đơn giản chỉ bao gồm việc ghi lại thời gian mà các giao dịch của một thực thể cụ thể được phát sóng lên mạng Bitcoin. Phân tích các mô hình thời gian này cho phép chúng ta suy luận nhiều thông tin.
Trước hết và quan trọng nhất, một phân tích thời gian đôi khi có thể xác định bản chất của thực thể đang được theo dõi. Nếu quan sát thấy các giao dịch được phát sóng liên tục trong 24 giờ, điều này có thể chỉ ra một hoạt động kinh tế mạnh mẽ. Thực thể đứng sau các giao dịch này có khả năng là một doanh nghiệp, có thể là quốc tế, và có lẽ với các thủ tục tự động nội bộ.
Ví dụ, tôi đã nhận ra mẫu này vài tuần trước khi phân tích một giao dịch đã nhầm lẫn phân bổ 19 bitcoin vào phí. Một phân tích thời gian đơn giản đã cho phép tôi giả định rằng chúng ta đang đối phó với một dịch vụ tự động, và do đó có khả năng là một thực thể lớn như một sàn giao dịch: https://twitter.com/Loic_Pandul/status/1701127409712452072
Quả thực, vài ngày sau, người ta phát hiện ra rằng số tiền thuộc về PayPal, thông qua sàn giao dịch Paxos.

Ngược lại, nếu thấy rằng mẫu thời gian được phân bổ rải rác qua 16 giờ cụ thể, thì có thể ước lượng rằng chúng ta đang đối phó với một người dùng cá nhân, hoặc có thể là một doanh nghiệp địa phương tùy thuộc vào khối lượng giao dịch.

Ngoài bản chất của thực thể được quan sát, mẫu thời gian cũng có thể cho chúng ta một vị trí gần đúng của người dùng. Chúng ta có thể do đó liên kết các giao dịch khác, và sử dụng dấu thời gian của những giao dịch này như một phép suy luận bổ sung có thể được thêm vào phân tích của chúng ta.

Ví dụ, về địa chỉ được sử dụng lại nhiều lần mà tôi đã đề cập trước đây, người ta có thể quan sát thấy rằng các giao dịch, dù là đến hay đi, đều tập trung trong khoảng thời gian 13 giờ.
![phân tích](assets/notext/12.webp)
*Credit: OXT*

Khoảng thời gian này có khả năng tương ứng với Châu Âu, Châu Phi, hoặc Trung Đông. Do đó, có thể giải thích rằng người dùng đứng sau những giao dịch này sống ở đó.

Trong một lĩnh vực khác, cũng là một phân tích thời gian như vậy đã cho phép giả thuyết rằng Satoshi Nakamoto không hoạt động từ Nhật Bản, mà thực sự từ Hoa Kỳ: [https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f)

### Phân Tích Khối Lượng
Một phép suy luận bên ngoài khác có thể được sử dụng là phân tích khối lượng giao dịch. Dựa trên số lượng có trong mỗi giao dịch được gán cho một thực thể, thông tin này có thể được sử dụng như một phép suy luận bổ sung cho phần còn lại của phân tích.
Phép suy luận này rõ ràng khá yếu, nhưng nó có thể giúp giảm bớt sự không chắc chắn khi được thêm vào các phép suy luận khác.

## Làm thế nào để bảo vệ bản thân khỏi phân tích chuỗi?
Là một người dùng Bitcoin, bạn có quyền bảo vệ sự riêng tư của mình. Điều này xuất phát từ quyền tự nhiên của bạn để sở hữu và tự quyết, mà mỗi cá nhân đều có, bất kể bất kỳ hạn chế pháp lý nào.

Quyền tự nhiên này để bảo vệ sự riêng tư của bản thân cũng được chuyển đổi thành quyền yêu sách, được ghi nhận trong Điều 12 của Tuyên ngôn Quyền con Người Toàn cầu, khẳng định rằng "*Không ai bị phơi bày cho sự can thiệp tùy tiện vào sự riêng tư, gia đình, nhà ở hoặc thư từ của mình, cũng như không bị tấn công danh dự và uy tín. Mọi người đều có quyền được pháp luật bảo vệ khỏi sự can thiệp hoặc tấn công như vậy.*".

Tuy nhiên, công việc chính của các công ty chuyên về phân tích chuỗi chính xác là xâm nhập vào không gian riêng tư của bạn, do đó làm tổn hại đến tính bảo mật của thư từ của bạn. Mặc dù người ta có thể hy vọng rằng, phù hợp với quyền yêu sách đã nêu, các quốc gia sẽ mạnh mẽ bảo vệ sự riêng tư của chúng ta, không chỉ họ không làm như vậy, mà họ còn cung cấp tài chính đáng kể cho việc tài trợ cho các công ty phân tích này. Cũng sẽ vô ích khi hy vọng được hỗ trợ từ các hiệp hội ngành, những người dường như sẵn lòng nhượng bộ trước nhà lập pháp.

Theo sự thật, quyền yêu sách này về sự riêng tư trên Bitcoin không tồn tại. Do đó, nó là trách nhiệm của bạn, người dùng, để khẳng định quyền tự nhiên của mình và bảo vệ tính bảo mật của thư từ của bạn. Điều này đòi hỏi việc áp dụng các kỹ thuật và thực hành sử dụng khác nhau, sẽ cho phép bạn ngăn chặn hoặc lừa dối các phép suy luận được sử dụng cho phân tích chuỗi.

### Tránh rơi vào các phép suy luận
Trước hết, trước khi xem xét các phương pháp mạnh mẽ hơn, chúng ta nên hạn chế tiếp xúc với các phương pháp phân tích chuỗi bằng cách sử dụng heuristics càng ít càng tốt. Như đã đề cập trước đó, hai heuristics mạnh mẽ nhất là tái sử dụng địa chỉ và COINJOIN.
Nguyên tắc cơ bản để đảm bảo quyền riêng tư trên Bitcoin là sử dụng một địa chỉ mới, sạch sẽ cho mỗi giao dịch đến ví của bạn. Tái sử dụng địa chỉ thực sự là mối đe dọa chính đối với bảo mật trên Bitcoin.
Đối với một người dùng cá nhân, việc tạo một địa chỉ mới cho mỗi khoản thanh toán đến là rất đơn giản. Ví hiện đại tự động thực hiện điều này ngay khi bạn nhấp vào "Nhận". Vì vậy, nếu bạn coi trọng quyền riêng tư của các giao dịch của mình, việc sử dụng địa chỉ mới là điều tối thiểu. Nếu bạn cần một điểm liên hệ cố định trên internet, thay vì đặt một địa chỉ nhận, bạn có thể sử dụng các giải pháp [như PayNym thực hiện BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).
Tiếp theo, nếu bạn muốn chống lại phân tích chuỗi, tránh gộp UTXOs tại đầu vào của một giao dịch. Ít nhất, nếu bạn thực sự cần gộp, hãy ưu tiên UTXOs có cùng nguồn gốc. Khuyến nghị này ngụ ý việc quản lý tốt UTXOs của bạn. Khi mua bitcoins, hãy ưu tiên chuyển khoản với số lượng lớn để tối đa hóa số lượng thanh toán bạn có thể thực hiện mà không cần phải gộp. Tôi cũng khuyên bạn nên gắn nhãn UTXOs trong phần mềm của mình để xác định nguồn gốc của chúng và tránh gộp từ các nguồn khác nhau.

Một cách rộng rãi hơn, đối với tất cả các heuristics khác, bạn cần biết chúng để cố gắng không rơi vào chúng:
- Không sử dụng các kịch bản thiểu số. Ưu tiên SegWit V0 hoặc có thể là SegWit V1;
- Không thực hiện các khoản thanh toán bằng số tròn. Ví dụ, nếu bạn cần gửi 100k sats cho một người bạn, hãy gửi 114,486 sats. Họ sẽ mua cho bạn một ly đồ uống để đáp lại;
- Cố gắng không luôn có một lượng tiền thối lớn hơn nhiều so với đầu ra thanh toán;
- Không đăng địa chỉ nhận của bạn trên mạng xã hội;
- Sử dụng node riêng của bạn dưới Tor để phát sóng giao dịch của bạn;
- Cố gắng không luôn phát sóng giao dịch Bitcoin của bạn vào cùng một thời điểm…

### Sử dụng công cụ bảo mật
Bạn cũng có thể chuyển sang các phương pháp làm cho việc sử dụng Bitcoin của bạn trở nên mơ hồ để ngăn chặn hoặc đánh lừa phân tích chuỗi.

Kỹ thuật phổ biến nhất chắc chắn là Coinjoin, một cấu trúc giao dịch hợp tác sử dụng nhiều UTXOs với cùng một số lượng. Mục tiêu ở đây là phá vỡ các liên kết xác định, do đó ngăn chặn phân tích từ hiện tại đến quá khứ và từ quá khứ đến hiện tại. Coinjoin cho phép phủ nhận hợp lý bằng cách ẩn đồng tiền của bạn trong một nhóm lớn các đồng tiền không thể phân biệt. Nếu bạn muốn tìm hiểu thêm về Coinjoin, cả về mặt kỹ thuật và thực hành, tôi đề xuất bạn đọc các bài viết và hướng dẫn khác:
- [COINJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [COINJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).
![phân tích](assets/en/13.webp)

CoinJoin là một công cụ xuất sắc để tạo ra sự phủ nhận hợp lý cho các đồng tiền, nhưng nó không được tối ưu hóa cho tất cả nhu cầu riêng tư của người dùng. Cụ thể, CoinJoin không được thiết kế để trở thành một công cụ thanh toán. Nó rất cứng nhắc về các số lượng được trao đổi để hoàn thiện việc sản xuất sự phủ nhận hợp lý. Vì không thể tự do chọn số lượng của các đầu ra giao dịch, CoinJoin không thể được sử dụng để thực hiện các khoản thanh toán bằng bitcoin.
Ví dụ, hãy tưởng tượng tôi muốn thanh toán cho chiếc bánh mì baguette của mình bằng bitcoin trong khi tối ưu hóa sự riêng tư của mình. Do không thể chọn lượng UTXO kết quả từ CoinJoin, tôi sẽ thấy mình không thể điều chỉnh số tiền chi tiêu của mình phù hợp với giá do người bán bánh đặt ra. Do đó, CoinJoin chứng minh là không phù hợp cho các giao dịch thanh toán.

Các công cụ khác đã được tạo ra để đáp ứng nhu cầu về sự riêng tư trong các trường hợp sử dụng cụ thể hơn. Ví dụ, chúng ta có [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), một loại mini-CoinJoin, chỉ bao gồm hai người tham gia và dựa trên một cấu trúc cho phép thanh toán.

Điểm độc đáo của PayJoin nằm ở khả năng tạo ra một giao dịch trông bình thường, trong khi thực tế đó là một mini-CoinJoin giữa hai người dùng. Trong cấu trúc này, người nhận giao dịch tham gia vào các input cùng với người gửi thực sự. Do đó, người nhận chèn một khoản thanh toán cho chính họ trong giao dịch giúp thực hiện thanh toán thực sự.

Ví dụ, nếu bạn mua một chiếc bánh mì baguette từ người bán bánh của mình với giá 6,000 sats từ một UTXO của 10,000 sats, và bạn muốn thực hiện một PayJoin, người bán bánh của bạn sẽ thêm một UTXO của 15,000 sats thuộc về họ như một input vào giao dịch ban đầu của bạn, mà họ sẽ hoàn toàn thu hồi như một output, nhằm đánh lừa các phân tích:

![phân tích](assets/en/14.webp)

Phí giao dịch được bỏ qua để đơn giản hóa việc hiểu cấu trúc.

Mục tiêu của PayJoin là hai lần. Đầu tiên, nó nhằm đánh lừa một quan sát viên bên ngoài bằng cách tạo ra một bức bình phong thông qua COH. Thực sự, khi một nhà phân tích quan sát giao dịch này, họ sẽ nghĩ rằng họ có thể áp dụng COH, và do đó giả định một sở hữu chung của các input khác nhau. Trên thực tế, giả định này là không chính xác, vì một input thuộc về người gửi, trong khi input khác được sở hữu bởi người nhận. Do đó, PayJoin làm hỏng phân tích chuỗi bằng cách dẫn dắt nhà phân tích đi sai hướng.
Mục tiêu thứ hai của PayJoin là đánh lừa nhà phân tích về số tiền thực sự của giao dịch, nhờ vào cấu trúc đặc biệt của các output của nó. Do đó, PayJoin thuộc về lĩnh vực steganography. Nó cho phép số tiền thực sự của giao dịch được ẩn trong một giao dịch lừa đảo.

Thực sự, nếu chúng ta xem xét lại ví dụ của chúng ta về việc sử dụng PayJoin để mua bánh mì baguette, một quan sát viên bên ngoài có thể nghĩ rằng chúng ta đang xử lý một khoản thanh toán 4,000 sats hoặc 21,000 sats. Trên thực tế, khoản thanh toán cho bánh mì baguette là 6,000 sats: 21,000 - 15,000 = 6,000. Do đó, giá trị thực sự của khoản thanh toán được ẩn trong một khoản thanh toán giả mạo hoạt động như một bức bình phong cho phân tích chuỗi.

Ngoài PayJoin và CoinJoin, có nhiều cấu trúc giao dịch Bitcoin khác hoặc chặn phân tích chuỗi hoặc đánh lừa nó. Trong số này, tôi có thể nhắc đến các giao dịch [Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) và [StonewallX2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b), cho phép tạo ra một mini Coinjoin linh hoạt hoặc mô phỏng một mini Coinjoin linh hoạt. Cũng có các giao dịch [Ricochet](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) mô phỏng sự thay đổi sở hữu của bitcoin bằng cách thực hiện nhiều chuyển giao giả mạo cho chính mình.

Tất cả các công cụ này đều có sẵn trên Samourai Wallet trên di động, và Sparrow Wallet trên PC. Nếu bạn muốn tìm hiểu thêm về các cấu trúc giao dịch cụ thể này, tôi khuyên bạn nên khám phá các hướng dẫn của tôi:
- [PAYJOIN](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PAYJOIN - SAMOURAI VÍ](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PAYJOIN - SPARROW VÍ](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

## Kết luận
Phân tích chuỗi là một thực hành liên quan đến việc cố gắng truy tìm dòng chảy của bitcoin trên chuỗi. Để làm điều này, các nhà phân tích tìm kiếm các mẫu và đặc điểm nhằm rút ra các giả thuyết và diễn giải có thể chấp nhận được.

Độ chính xác của các phương pháp suy luận này thay đổi: một số cung cấp một mức độ chắc chắn cao hơn những cái khác, nhưng không có cái nào có thể tuyên bố là không sai lầm. Tuy nhiên, sự tích lũy của nhiều phương pháp suy luận hợp lý có thể giảm bớt sự nghi ngờ này, mặc dù việc loại bỏ hoàn toàn nó là không thể.
Chúng ta có thể phân loại các phương pháp này thành ba loại chính:
- Mẫu, tập trung vào cấu trúc tổng thể của mỗi giao dịch;
- Suy luận nội bộ, cho phép kiểm tra toàn diện tất cả chi tiết của một giao dịch, không mở rộng ra ngữ cảnh của nó;
- Suy luận bên ngoài, bao gồm phân tích giao dịch trong môi trường của nó, cũng như bất kỳ dữ liệu bên ngoài nào có thể cung cấp cái nhìn sâu sắc.

Đối với người dùng Bitcoin, việc nắm vững các nguyên tắc cơ bản của phân tích chuỗi là cần thiết để hiệu quả chống lại nó và do đó bảo vệ quyền riêng tư của mình.

## Mini-Glossary Kỹ Thuật:
**P2PKH:** viết tắt của Pay to Public Key Hash. Đây là một mô hình script chuẩn được sử dụng để thiết lập các điều kiện chi tiêu trên một UTXO. Nó cho phép khóa bitcoin trên một hash của khóa công khai, tức là, trên một địa chỉ nhận. Script này được liên kết với tiêu chuẩn Legacy và được giới thiệu trong các phiên bản đầu tiên của Bitcoin bởi Satoshi Nakamoto. Khác với P2PK, nơi khóa công khai được bao gồm rõ ràng trong script, P2PKH sử dụng dấu ấn mật mã của khóa công khai, với một số metadata, còn được gọi là "địa chỉ nhận". Script này bao gồm hash RIPEMD160 của SHA256 của khóa công khai và quy định rằng, để truy cập vào quỹ, người nhận phải cung cấp một khóa công khai phù hợp với hash này, cũng như một chữ ký số hợp lệ được tạo từ khóa riêng tư tương ứng. Địa chỉ P2PKH được mã hóa sử dụng định dạng Base58Check, giúp chúng có khả năng chống lại lỗi đánh máy thông qua việc sử dụng một checksum. Các địa chỉ này luôn bắt đầu bằng số 1.
**P2TR:** viết tắt của Pay to Taproot ("thanh toán cho gốc"). Đây là một mô hình script chuẩn được sử dụng để thiết lập điều kiện chi tiêu cho một UTXO. P2TR được giới thiệu cùng với việc triển khai Taproot vào tháng 11 năm 2021. Nó sử dụng giao thức Schnorr để tổng hợp các khóa mật mã, cũng như cây Merkle cho các script thay thế, được biết đến với tên MAST (Merkelized Alternative Script Tree). Khác với các giao dịch truyền thống nơi điều kiện chi tiêu được công bố công khai (đôi khi khi nhận, đôi khi khi chi tiêu), P2TR cho phép ẩn các script phức tạp sau một khóa công khai rõ ràng duy nhất. Về mặt kỹ thuật, một script P2TR khóa bitcoin trên một khóa công khai Schnorr duy nhất, được ký hiệu là K. Tuy nhiên, khóa K này thực sự là sự tổng hợp của một khóa công khai P và một khóa công khai M, khóa sau được tính toán từ gốc Merkle của một danh sách ScriptPubKeys. Việc tổng hợp khóa được thực hiện sử dụng giao thức chữ ký Schnorr. Bitcoin bị khóa bằng một script P2TR có thể được chi tiêu theo hai cách riêng biệt: hoặc là công bố một chữ ký cho khóa công khai P, hoặc là thỏa mãn một trong các script chứa trong cây Merkle. Lựa chọn đầu tiên được gọi là "đường dẫn khóa" và lựa chọn thứ hai là "đường dẫn script." Do đó, P2TR cho phép người dùng gửi bitcoin hoặc đến một khóa công khai hoặc đến nhiều script theo lựa chọn của họ. Một lợi ích khác của script này là, mặc dù có nhiều cách để chi tiêu một đầu ra P2TR, chỉ có một cách được sử dụng cần phải được tiết lộ khi chi tiêu, cho phép các lựa chọn không sử dụng khác vẫn còn riêng tư. Ví dụ, nhờ tổng hợp khóa Schnorr, khóa công khai P có thể là một khóa tổng hợp, có khả năng đại diện cho một multisig. P2TR là một đầu ra SegWit phiên bản 1, nghĩa là chữ ký cho các đầu vào P2TR được lưu trữ trong phần chứng của một giao dịch, và không phải trong ScriptSig. Địa chỉ P2TR sử dụng mã hóa Bech32m và bắt đầu với bc1p.

**P2WPKH:** Viết tắt của Pay to Witness Public Key Hash. Đây là một mô hình script chuẩn được sử dụng để thiết lập điều kiện chi tiêu cho một UTXO. P2WPKH được giới thiệu cùng với việc triển khai SegWit vào tháng 8 năm 2017. Script này tương tự như P2PKH (Pay to Public Key Hash), ở chỗ nó cũng khóa bitcoin dựa trên hash của một khóa công khai, tức là, một địa chỉ nhận. Sự khác biệt nằm ở cách chữ ký và script được bao gồm trong giao dịch. Trong trường hợp của P2WPKH, thông tin script chữ ký (ScriptSig) được di chuyển từ cấu trúc giao dịch truyền thống sang một phần riêng biệt gọi là Witness. Điều này là một tính năng của bản cập nhật SegWit (Segregated Witness). Kỹ thuật này có lợi ích là giảm kích thước dữ liệu giao dịch trong phần chính, trong khi vẫn giữ lại thông tin script cần thiết cho việc xác thực trong một phần riêng biệt. Do đó, giao dịch P2WPKH thường ít tốn kém về phí so với giao dịch Legacy. Địa chỉ P2WPKH được viết bằng mã hóa Bech32, góp phần vào việc viết một cách ngắn gọn và ít lỗi hơn nhờ vào checksum BCH. Các địa chỉ này luôn bắt đầu với bc1q, làm cho chúng dễ dàng phân biệt với các địa chỉ nhận Legacy. P2WPKH là một đầu ra SegWit phiên bản 0.
**UTXO:** Viết tắt của Unspent Transaction Output. UTXO là một đầu ra của giao dịch chưa được tiêu dùng hoặc sử dụng làm đầu vào cho một giao dịch mới. UTXO đại diện cho phần bitcoin mà người dùng sở hữu và hiện đang có sẵn để tiêu. Mỗi UTXO được liên kết với một script đầu ra cụ thể, định nghĩa các điều kiện cần thiết để tiêu bitcoin đó. Giao dịch trong Bitcoin tiêu thụ những UTXO này như là đầu vào và tạo ra UTXO mới như là đầu ra. Mô hình UTXO là cơ bản đối với Bitcoin, vì nó cho phép dễ dàng xác minh rằng các giao dịch không cố gắng tiêu bitcoin không tồn tại hoặc đã được tiêu. Cơ bản, một UTXO là một phần của Bitcoin.






