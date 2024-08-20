---
name: Giới thiệu về Mật mã học chính thức
goal: Một bài giới thiệu sâu rộng về khoa học và thực hành của mật mã học.
objectives:
  - Khám phá mã Beale và các phương pháp mật mã học hiện đại để hiểu về các khái niệm cơ bản và lịch sử của mật mã học.
  - Đào sâu vào lý thuyết số, nhóm và trường để nắm vững các khái niệm toán học chính yếu đằng sau mật mã học.
  - Nghiên cứu về mã dòng RC4 và AES với khóa 128-bit để tìm hiểu về các thuật toán mật mã đối xứng.
  - Điều tra về hệ thống mật mã RSA, phân phối khóa và các hàm băm để khám phá mật mã học bất đối xứng.

---
# Sâu lắng vào mật mã học

Rất khó để tìm thấy nhiều tài liệu cung cấp một lập trường trung lập tốt trong giáo dục mật mã học.

Một mặt, có những luận án dài và chính thức, thực sự chỉ dành cho những người có nền tảng vững chắc trong toán học, logic, hoặc một lĩnh vực chính thức nào đó. Mặt khác, có những giới thiệu rất tổng quan mà thực sự che giấu quá nhiều chi tiết đối với bất kỳ ai ít nhất là một chút tò mò.

Bài giới thiệu này về mật mã học tìm cách nắm bắt lập trường trung lập. Mặc dù nó nên tương đối thách thức và chi tiết đối với bất kỳ ai mới đến với mật mã học, nó không phải là hố thỏ của một luận án cơ bản điển hình.

+++

# Một Giới thiệu về Mật mã học
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Mô tả ngắn gọn
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Cuốn sách này cung cấp một bài giới thiệu sâu rộng về khoa học và thực hành của mật mã học. Nơi có thể, nó tập trung vào việc trình bày khái niệm, thay vì trình bày chính thức của vật liệu.

> Khóa học này dựa trên [kho lưu trữ của JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Mọi quyền thuộc về anh ấy. Nội dung chưa hoàn thiện và chỉ ở đây để trình bày cách chúng ta có thể tích hợp nếu JWburger đồng ý.

### Động cơ và mục tiêu

Rất khó để tìm thấy nhiều tài liệu cung cấp một lập trường trung lập tốt trong giáo dục mật mã học.

Một mặt, có những luận án dài và chính thức, thực sự chỉ dành cho những người có nền tảng vững chắc trong toán học, logic, hoặc một lĩnh vực chính thức nào đó. Mặt khác, có những giới thiệu rất tổng quan mà thực sự che giấu quá nhiều chi tiết đối với bất kỳ ai ít nhất là một chút tò mò.

Bài giới thiệu này về mật mã học tìm cách nắm bắt lập trường trung lập. Mặc dù nó nên tương đối thách thức và chi tiết đối với bất kỳ ai mới đến với mật mã học, nó không phải là hố thỏ của một luận án cơ bản điển hình.

### Đối tượng mục tiêu

Từ các nhà phát triển đến những người tò mò về trí tuệ, cuốn sách này hữu ích cho bất kỳ ai muốn hiểu sâu hơn về mật mã học. Nếu mục tiêu của bạn là nắm vững lĩnh vực mật mã học, thì cuốn sách này cũng là một điểm khởi đầu tốt.

### Hướng dẫn đọc

Cuốn sách hiện tại bao gồm bảy chương: "Mật mã học là gì?" (Chương 1), "Nền tảng Toán học của Mật mã học I" (Chương 2), "Nền tảng Toán học của Mật mã học II" (Chương 3), "Mật mã đối xứng" (Chương 4), "RC4 và AES" (Chương 5), "Mật mã bất đối xứng" (Chương 6), và "Hệ thống mật mã RSA" (Chương 7). Một chương cuối cùng, "Mật mã học trong Thực hành," sẽ được thêm vào. Nó tập trung vào các ứng dụng mật mã học khác nhau, bao gồm bảo mật lớp vận chuyển, định tuyến onion, và hệ thống trao đổi giá trị của Bitcoin.
Trừ khi bạn có một nền tảng vững chắc về toán học, lý thuyết số có lẽ là chủ đề khó nhất trong cuốn sách này. Tôi đã giới thiệu tổng quan về nó trong Chương 3, và nó cũng xuất hiện trong phần trình bày về AES trong Chương 5 và hệ thống mật mã RSA trong Chương 7.
Nếu bạn thực sự gặp khó khăn với các chi tiết chính thức trong những phần này của cuốn sách, tôi khuyên bạn nên đọc sơ qua chúng lần đầu tiên.

### Lời cảm ơn

Cuốn sách có ảnh hưởng nhất trong việc hình thành cuốn sách này đã là _Introduction to Modern Cryptography_ của Jonathan Katz và Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Một khóa học đi kèm có sẵn trên Coursera với tên "Cryptography."

Những nguồn thông tin chính thêm vào đã hữu ích trong việc tạo ra bản tổng quan trong cuốn sách này là Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar và Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) và một khóa học dựa trên cuốn sách của Paar có tên “Introduction to Cryptography” (có sẵn tại https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); và Bruce Schneier, Applied Cryptography, ấn bản thứ 2, 2015 (Indianapolis, IN: John Wiley & Sons).

Tôi chỉ trích dẫn những thông tin và kết quả cụ thể mà tôi lấy từ những nguồn này, nhưng muốn công nhận sự nợ nần chung của tôi với họ ở đây.

Đối với những độc giả muốn tìm hiểu kiến thức nâng cao hơn về mật mã học sau bài giới thiệu này, tôi rất khuyến khích cuốn sách của Katz và Lindell. Khóa học của Katz trên Coursera dễ tiếp cận hơn so với cuốn sách.

### Đóng góp

Vui lòng xem tệp đóng góp trong kho lưu trữ để biết một số hướng dẫn về cách hỗ trợ dự án.

# Mật mã học là gì?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

Hãy bắt đầu cuộc tìm hiểu của chúng ta về lĩnh vực mật mã học với một trong những tập hợp câu chuyện hấp dẫn và giải trí nhất trong lịch sử của nó: đó là các mã Beale.<sup>[1](#footnote1)</sup>

Theo ý kiến của tôi, câu chuyện về các mã Beale có lẽ nhiều khả năng là hư cấu hơn là thực tế. Nhưng nó được cho là đã diễn ra như sau.

## Các mã Beale
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

Trong cả mùa Đông năm 1820 và 1822, một người đàn ông tên là Thomas J. Beale đã ở tại một quán trọ do Robert Morriss sở hữu ở Lynchburg (Virginia). Vào cuối lần ở thứ hai của Beale, ông đã giao cho Morriss một chiếc hộp sắt chứa các giấy tờ quý giá để giữ an toàn.

Một vài tháng sau, Morriss nhận được một bức thư từ Beale có ngày tháng là 9 tháng 5 năm 1822. Bức thư nhấn mạnh giá trị lớn của nội dung chiếc hộp sắt và đưa ra một số hướng dẫn cho Morriss: nếu Beale hoặc bất kỳ đồng minh nào của ông không bao giờ đến yêu cầu chiếc hộp, ông nên mở nó đúng mười năm từ ngày thư được viết (tức là ngày 9 tháng 5 năm 1832). Một số giấy tờ bên trong sẽ được viết bằng văn bản thông thường. Tuy nhiên, một số khác sẽ “không thể hiểu được mà không có sự giúp đỡ của một chìa khóa.” Chìa khóa này, sau đó, sẽ được một người bạn không tên của Beale giao cho Morriss vào tháng 6 năm 1832.
Mặc dù đã có hướng dẫn rõ ràng, Morriss không mở chiếc hộp vào tháng 5 năm 1832 và người bạn bí ẩn của Beale cũng không xuất hiện vào tháng 6 của năm đó. Phải đến năm 1845, chủ quán trọ mới quyết định mở chiếc hộp. Trong đó, Morriss tìm thấy một ghi chú giải thích cách Beale và các cộng sự của mình đã phát hiện ra vàng và bạc ở phía Tây và chôn chúng, cùng với một số trang sức, để bảo quản. Ngoài ra, chiếc hộp chứa ba **ciphertexts**: tức là, các văn bản được viết bằng mã mà cần có **khóa mật mã**, hoặc một bí mật, và một thuật toán đi kèm để mở khóa. Quá trình mở khóa một ciphertext được biết đến là **giải mã**, trong khi quá trình khóa được biết đến là **mã hóa**. (Như đã giải thích trong Chương 3, thuật ngữ cipher có thể có nhiều nghĩa. Trong tên "Beale ciphers", nó được viết tắt cho ciphertexts.)

Ba ciphertexts mà Morriss tìm thấy trong chiếc hộp sắt mỗi cái đều bao gồm một chuỗi số được phân cách bằng dấu phẩy. Theo ghi chú của Beale, những ciphertexts này riêng biệt cung cấp vị trí của kho báu, nội dung của kho báu, và một danh sách tên với những người thừa kế hợp pháp của kho báu và phần của họ (thông tin cuối cùng này có liên quan trong trường hợp Beale và các cộng sự của mình không bao giờ đến để yêu cầu chiếc hộp).

Morris đã cố gắng giải mã ba ciphertexts trong hai mươi năm. Điều này sẽ dễ dàng với chiếc khóa. Nhưng Morriss không có chiếc khóa và không thành công trong các nỗ lực của mình để khôi phục các văn bản gốc, hay **plaintexts** như chúng thường được gọi trong mật mã học.

Khi cuộc đời đang dần kết thúc, Morriss đã chuyển chiếc hộp cho một người bạn vào năm 1862. Người bạn này sau đó đã xuất bản một cuốn sách nhỏ vào năm 1885, dưới bút danh J.B. Ward. Nó bao gồm một mô tả về lịch sử (được cho là) của chiếc hộp, ba ciphertexts, và một giải pháp mà anh ta đã tìm ra cho ciphertext thứ hai. (Rõ ràng, có một khóa cho mỗi ciphertext, và không phải một khóa hoạt động trên tất cả ba ciphertexts như Beale ban đầu có vẻ đã đề xuất trong thư của mình gửi cho Morriss.)

Bạn có thể thấy ciphertext thứ hai trong *Hình 2* dưới đây.<sup>[2](#footnote2)</sup> Khóa cho ciphertext này là Tuyên ngôn Độc lập của Hoa Kỳ. Quy trình giải mã được thực hiện theo hai quy tắc sau:

* Đối với bất kỳ số nào trong ciphertext, tìm từ thứ n trong Tuyên ngôn Độc lập của Hoa Kỳ
* Thay thế số n bằng chữ cái đầu tiên của từ bạn tìm được

*Hình 1: Beale cipher số 2*

![Hình 1: Beale cipher số 2.](assets/Figure1-1.webp "Hình 1: Beale cipher số 2")

Ví dụ, số đầu tiên của ciphertext thứ hai là 115. Từ thứ 115 của Tuyên ngôn Độc lập là “instituted,” vì vậy chữ cái đầu tiên của plaintext là “i.” Ciphertext không trực tiếp chỉ ra khoảng trắng và việc viết hoa. Nhưng sau khi giải mã một vài từ đầu tiên, bạn có thể logic suy luận rằng từ đầu tiên của plaintext đơn giản là “I.” (Plaintext bắt đầu với cụm từ “I have deposited in the county of Bedford.”)
Sau khi giải mã, thông điệp thứ hai cung cấp nội dung chi tiết về kho báu (vàng, bạc và đá quý), và gợi ý rằng nó đã được chôn trong những cái nồi sắt và phủ đá ở Quận Bedford (Virginia). Mọi người đều thích một bí ẩn hay, vì vậy đã có nhiều nỗ lực lớn được bỏ ra để giải mã hai thông điệp Beale còn lại, đặc biệt là thông điệp mô tả vị trí của kho báu. Thậm chí nhiều nhà mật mã học nổi tiếng cũng đã thử sức. Tuy nhiên, cho đến nay, chưa ai có thể giải mã được hai bản mã văn khác.

## Mật mã học hiện đại
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Những câu chuyện đầy màu sắc như về các mã Beale là những gì mà hầu hết chúng ta liên tưởng đến với mật mã học. Tuy nhiên, mật mã học hiện đại khác biệt ít nhất bốn cách quan trọng so với những ví dụ lịch sử này.

Đầu tiên, lịch sử mật mã học chỉ quan tâm đến **bí mật** (hoặc bảo mật). Các bản mã văn được tạo ra để đảm bảo rằng chỉ những bên nhất định mới có thể tiếp cận thông tin trong bản rõ, như trường hợp của các mã Beale. Để một hệ thống mã hóa phục vụ mục đích này tốt, việc giải mã bản mã văn chỉ nên khả thi nếu bạn có chìa khóa.

Mật mã học hiện đại quan tâm đến một phạm vi chủ đề rộng lớn hơn chỉ là bí mật. Những chủ đề này bao gồm chủ yếu là (1) **tính toàn vẹn của thông điệp**—đó là, đảm bảo rằng một thông điệp không bị thay đổi; (2) **tính xác thực của thông điệp**—đó là, đảm bảo rằng một thông điệp thực sự đến từ một người gửi cụ thể; và (3) **không chối bỏ**—đó là, đảm bảo rằng một người gửi không thể phủ nhận sau này rằng họ đã gửi một thông điệp.

Một sự phân biệt quan trọng cần giữ trong tâm trí, do đó, giữa một **hệ thống mã hóa** và một **hệ thống mật mã**. Một hệ thống mã hóa chỉ quan tâm đến bí mật. Trong khi một hệ thống mã hóa là một hệ thống mật mã, ngược lại không đúng. Một hệ thống mật mã cũng có thể phục vụ các chủ đề chính khác của mật mã học, bao gồm tính toàn vẹn, xác thực, và không chối bỏ.

Các chủ đề về tính toàn vẹn và xác thực quan trọng không kém bí mật. Hệ thống truyền thông hiện đại của chúng ta sẽ không thể hoạt động mà không có các bảo đảm về tính toàn vẹn và xác thực của thông tin liên lạc. Không chối bỏ cũng là một mối quan tâm quan trọng, như đối với các hợp đồng số, nhưng ít cần thiết trong các ứng dụng mật mã học hơn so với bí mật, tính toàn vẹn và xác thực.

Thứ hai, các hệ thống mã hóa cổ điển như mã Beale luôn liên quan đến một chìa khóa được chia sẻ giữa tất cả các bên liên quan. Tuy nhiên, nhiều hệ thống mật mã học hiện đại không chỉ liên quan đến một, mà là hai chìa khóa: một **chìa khóa riêng tư** và một **chìa khóa công khai**. Trong khi cái trước nên được giữ kín trong bất kỳ ứng dụng nào, cái sau thường là kiến thức công cộng (do đó, tên của chúng). Trong lĩnh vực mã hóa, chìa khóa công khai có thể được sử dụng để mã hóa thông điệp, trong khi chìa khóa riêng tư có thể được sử dụng để giải mã.

Ngành của mật mã học xử lý các hệ thống mà tất cả các bên chia sẻ một chìa khóa được biết đến là **mật mã học đối xứng**. Chìa khóa duy nhất trong một hệ thống như vậy thường được gọi là **chìa khóa riêng tư** (hoặc chìa khóa bí mật). Ngành của mật mã học xử lý các hệ thống yêu cầu một cặp chìa khóa riêng tư-công khai được biết đến là **mật mã học bất đối xứng**. Những ngành này đôi khi cũng được gọi là **mật mã học chìa khóa riêng** và **mật mã học chìa khóa công khai**, tương ứng (mặc dù điều này có thể gây nhầm lẫn, vì các hệ thống mật mã học chìa khóa công khai cũng có chìa khóa riêng).
Sự ra đời của mật mã học bất đối xứng vào cuối những năm 1970 đã là một trong những sự kiện quan trọng nhất trong lịch sử của mật mã học. Nếu không có nó, hầu hết các hệ thống giao tiếp hiện đại của chúng ta, bao gồm cả Bitcoin, sẽ không thể thực hiện được, hoặc ít nhất là rất không thực tế.

Quan trọng, mật mã học hiện đại không chỉ là nghiên cứu về các hệ thống mật mã khóa đối xứng và bất đối xứng (mặc dù điều đó chiếm phần lớn lĩnh vực). Ví dụ, mật mã học cũng liên quan đến các hàm băm và bộ sinh số ngẫu nhiên giả mạo, và bạn có thể xây dựng các ứng dụng trên những nguyên tắc cơ bản này không liên quan đến mật mã khóa đối xứng hoặc bất đối xứng.

Thứ ba, các hệ thống mã hóa cổ điển, như những hệ thống được sử dụng trong các mã Beale, được coi là nghệ thuật hơn là khoa học. Sự an toàn của chúng chủ yếu dựa vào trực giác về độ phức tạp của chúng. Chúng thường được vá lỗi khi một cuộc tấn công mới được biết đến, hoặc bị loại bỏ hoàn toàn nếu cuộc tấn công đặc biệt nghiêm trọng. Tuy nhiên, mật mã học hiện đại là một khoa học nghiêm ngặt với một cách tiếp cận toán học, hình thức để phát triển và phân tích các hệ thống mật mã.

Cụ thể, mật mã học hiện đại tập trung vào **chứng minh về sự an toàn**. Bất kỳ chứng minh sự an toàn nào cho một hệ thống mật mã đều tiến hành theo ba bước:

1. Phát biểu về **định nghĩa mật mã học về sự an toàn**, tức là, một tập hợp các mục tiêu an toàn và mối đe dọa từ kẻ tấn công.
2. Phát biểu về bất kỳ giả định toán học nào liên quan đến độ phức tạp tính toán của hệ thống. Ví dụ, một hệ thống mật mã có thể chứa một bộ sinh số ngẫu nhiên giả mạo. Mặc dù chúng ta không thể chứng minh chúng tồn tại, nhưng chúng ta có thể giả định rằng chúng tồn tại.
3. Trình bày một **chứng minh toán học về sự an toàn** của hệ thống dựa trên khái niệm hình thức về sự an toàn và bất kỳ giả định toán học nào.

Thứ tư, trong khi trước đây mật mã học chủ yếu được sử dụng trong các cài đặt quân sự, nó đã trở nên phổ biến trong các hoạt động hàng ngày của chúng ta trong kỷ nguyên số. Dù bạn đang giao dịch ngân hàng trực tuyến, đăng bài trên mạng xã hội, mua sản phẩm từ Amazon bằng thẻ tín dụng, hay chuyển bitcoin cho bạn bè, mật mã học là điều không thể thiếu trong kỷ nguyên số của chúng ta.

Với bốn khía cạnh này của mật mã học hiện đại, chúng ta có thể mô tả mật mã học hiện đại là khoa học liên quan đến việc phát triển và phân tích hình thức của các hệ thống mật mã để bảo vệ thông tin số chống lại các cuộc tấn công từ đối thủ. An toàn ở đây nên được hiểu một cách rộng rãi là ngăn chặn các cuộc tấn công làm hại đến bí mật, tính toàn vẹn, xác thực, và/hoặc không chối bỏ trong giao tiếp.

Mật mã học được coi là một tiểu ngành của **an ninh mạng**, lo ngại về việc ngăn chặn việc trộm cắp, hư hại, và lạm dụng các hệ thống máy tính. Lưu ý rằng nhiều mối quan tâm về an ninh mạng có ít hoặc chỉ một phần liên quan đến mật mã học.

Ví dụ, nếu một công ty lưu trữ máy chủ đắt tiền tại chỗ, họ có thể quan tâm đến việc bảo vệ phần cứng này khỏi bị trộm và hư hại. Mặc dù đây là một mối quan tâm về an ninh mạng, nhưng nó ít liên quan đến mật mã học.

Ví dụ khác, **các cuộc tấn công phishing** là một vấn đề phổ biến trong kỷ nguyên hiện đại của chúng ta. Những cuộc tấn công này cố gắng lừa đảo mọi người qua email hoặc một số phương tiện thông điệp khác để từ bỏ thông tin nhạy cảm như mật khẩu hoặc số thẻ tín dụng. Mặc dù mật mã học có thể giúp giải quyết các cuộc tấn công phishing đến một mức độ nào đó, một cách tiếp cận toàn diện yêu cầu nhiều hơn là chỉ sử dụng một số mật mã học.

## Giao tiếp mở
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Mật mã học hiện đại được thiết kế để cung cấp đảm bảo an toàn trong một môi trường **giao tiếp mở**. Nếu kênh giao tiếp của chúng ta được bảo vệ tốt đến mức người nghe trộm không có cơ hội can thiệp hoặc thậm chí chỉ quan sát tin nhắn của chúng ta, thì mật mã học là không cần thiết. Tuy nhiên, hầu hết các kênh giao tiếp của chúng ta không được bảo vệ tốt như vậy.
Xương sống của giao tiếp trong thế giới hiện đại là một mạng lưới lớn các cáp quang. Việc thực hiện cuộc gọi điện thoại, xem truyền hình và lướt web trong một hộ gia đình hiện đại chủ yếu phụ thuộc vào mạng lưới cáp quang này (một tỷ lệ nhỏ có thể hoàn toàn phụ thuộc vào vệ tinh). Quả thực, bạn có thể có các kết nối dữ liệu khác nhau trong nhà, như cáp đồng trục, dòng thuê bao số (không đối xứng) và cáp quang. Nhưng, ít nhất là ở các nước phát triển, các phương tiện truyền dữ liệu khác nhau này nhanh chóng kết nối bên ngoài nhà bạn với một nút trong mạng lưới cáp quang khổng lồ kết nối toàn cầu. Ngoại lệ là một số khu vực hẻo lánh của thế giới phát triển, như ở Hoa Kỳ và Úc, nơi mà dữ liệu có thể vẫn di chuyển một khoảng cách đáng kể trên dây điện thoại đồng truyền thống.

Việc ngăn chặn các kẻ tấn công tiếp cận vật lý mạng lưới cáp này và cơ sở hạ tầng hỗ trợ của nó là điều không thể. Thực tế, chúng ta đã biết rằng hầu hết dữ liệu của chúng ta bị các cơ quan tình báo quốc gia chặn đứng tại các điểm giao nhau quan trọng của Internet. Điều này bao gồm mọi thứ từ tin nhắn Facebook đến địa chỉ trang web mà bạn truy cập.

Mặc dù việc giám sát dữ liệu trên quy mô lớn đòi hỏi một đối thủ mạnh mẽ, như một cơ quan tình báo quốc gia, nhưng các kẻ tấn công chỉ với ít tài nguyên cũng có thể dễ dàng cố gắng nghe lén trên quy mô địa phương hơn. Mặc dù điều này có thể xảy ra ở cấp độ gắn kết dây, nhưng việc chặn đứng các tín hiệu không dây lại dễ dàng hơn nhiều.

Hầu hết dữ liệu mạng địa phương của chúng ta—cho dù ở nhà, tại văn phòng, hay trong quán cà phê—nay di chuyển qua sóng radio đến các điểm truy cập không dây trên các bộ định tuyến đa năng, thay vì qua cáp vật lý. Vì vậy, một kẻ tấn công cần rất ít tài nguyên để chặn bất kỳ lưu lượng truy cập địa phương nào của bạn. Điều này đặc biệt đáng lo ngại vì hầu hết mọi người làm rất ít để bảo vệ dữ liệu di chuyển qua mạng địa phương của họ. Ngoài ra, các kẻ tấn công tiềm năng cũng có thể nhắm vào các kết nối băng thông rộng di động của chúng ta, như 3G, 4G và 5G. Tất cả các giao tiếp không dây này đều là mục tiêu dễ dàng cho các kẻ tấn công.

Do đó, ý tưởng giữ bí mật thông tin liên lạc bằng cách bảo vệ kênh truyền thông là một ước mơ hoàn toàn ảo tưởng đối với phần lớn thế giới hiện đại. Mọi thứ chúng ta biết đều đáng để cảnh giác nghiêm trọng: bạn nên luôn giả định rằng có ai đó đang nghe. Và mật mã học là công cụ chính mà chúng ta có để đạt được bất kỳ loại bảo mật nào trong môi trường hiện đại này.

### Ghi chú
[^1]: Để có một bản tóm tắt tốt về câu chuyện, xem Simon Singh, *The Code Book*, Fourth Estate (London, 1999), trang 82-99. Một bộ phim ngắn về câu chuyện đã được Andrew Allen thực hiện vào năm 2010. Bạn có thể tìm thấy bộ phim, “The Thomas Beale Cipher,” trên trang web của nó [^1].

[^2]: Hình ảnh này có sẵn trên trang Wikipedia về các mật mã Beale [^2].

[^3]: Để chính xác, các ứng dụng quan trọng của các kế hoạch mật mã đã được quan tâm đến bí mật. Ví dụ, trẻ em thường xuyên sử dụng các kế hoạch mật mã đơn giản cho “vui”. Bí mật không thực sự là một mối quan tâm trong những trường hợp đó [^3].

[^4]: Bruce Schneier, *Applied Cryptography*, ấn bản thứ 2, 2015 (Indianapolis, IN: John Wiley & Sons), trang 2 [^4].

[^5]: Xem Jonathan Katz và Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), đặc biệt là trang 16–23, để có một mô tả tốt [^5].

[^6]: Cf. Katz và Lindell, ibid., trang 3. Tôi nghĩ rằng sự mô tả của họ có một số vấn đề, vì vậy tôi trình bày một phiên bản hơi khác của tuyên bố của họ ở đây [^6].
[^7]: Xem, ví dụ, Olga Khazan, "Thực hành lâu đời, rùng rợn của việc nghe lén cáp dưới biển", *The Atlantic*, ngày 16 tháng 7 năm 2013 (có thể tìm đọc tại [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)) [^7].

# Nền tảng Toán học của Mật mã học I
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

Mật mã học dựa trên toán học. Và nếu bạn muốn hiểu sâu hơn về mật mã học, bạn cần phải thoải mái với toán học đó.

Chương này giới thiệu hầu hết các kiến thức toán học cơ bản mà bạn sẽ gặp khi học mật mã học. Các chủ đề bao gồm biến ngẫu nhiên, phép toán modulo, phép toán XOR, và tính ngẫu nhiên giả. Bạn nên nắm vững nội dung trong các phần này để có một hiểu biết không hời hợt về mật mã học.

Chương tiếp theo sẽ đề cập đến lý thuyết số, đây là phần thách thức hơn nhiều.

## Biến ngẫu nhiên
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Một biến ngẫu nhiên thường được ký hiệu bằng một chữ cái viết hoa không in đậm. Ví dụ, chúng ta có thể nói về một biến ngẫu nhiên X, một biến ngẫu nhiên Y, hoặc một biến ngẫu nhiên Z. Đây là ký hiệu mà tôi cũng sẽ sử dụng từ đây trở đi.

Một **biến ngẫu nhiên** có thể nhận hai hoặc nhiều giá trị có thể xảy ra, mỗi giá trị với một xác suất dương nhất định. Các giá trị có thể xảy ra được liệt kê trong **tập hợp kết quả**.

Mỗi lần bạn **lấy mẫu** một biến ngẫu nhiên, bạn rút ra một giá trị cụ thể từ tập hợp kết quả của nó theo các xác suất đã định.

Hãy xem xét một ví dụ đơn giản. Giả sử một biến X được định nghĩa như sau:

* X có tập hợp kết quả {1,2}
* Pr [X = 1] = 0.5
* Pr [X = 2] = 0.5

Dễ thấy X là một biến ngẫu nhiên. Đầu tiên, có hai hoặc nhiều giá trị có thể xảy ra mà X có thể nhận, cụ thể là 1 và 2. Thứ hai, mỗi giá trị có thể xảy ra có một xác suất dương xảy ra mỗi khi bạn lấy mẫu X, cụ thể là 0.5.

Tất cả những gì một biến ngẫu nhiên yêu cầu là một tập hợp kết quả với hai hoặc nhiều khả năng, nơi mỗi khả năng có một xác suất dương xảy ra khi lấy mẫu. Về nguyên tắc, thì một biến ngẫu nhiên có thể được định nghĩa một cách trừu tượng, không liên quan đến bất kỳ bối cảnh nào. Trong trường hợp này, bạn có thể nghĩ về “lấy mẫu” như thực hiện một thí nghiệm tự nhiên để xác định giá trị của biến ngẫu nhiên.

Biến X ở trên được định nghĩa một cách trừu tượng. Do đó, bạn có thể nghĩ về việc lấy mẫu biến X như là tung một đồng xu công bằng và gán “2” trong trường hợp xuất hiện mặt ngửa và “1” trong trường hợp xuất hiện mặt sấp. Mỗi lần bạn lấy mẫu X, bạn tung đồng xu lại.

Hoặc, bạn cũng có thể nghĩ về việc lấy mẫu X như là tung một con xúc xắc công bằng và gán “2” nếu xúc xắc đổ 1, 3, hoặc 4, và gán “1” nếu xúc xắc đổ 2, 5, hoặc 6. Mỗi lần bạn lấy mẫu X, bạn tung xúc xắc lại.

Thực sự, bất kỳ thí nghiệm tự nhiên nào cho phép bạn định nghĩa các xác suất của các giá trị có thể xảy ra của X ở trên đều có thể được tưởng tượng liên quan đến việc rút ra.
Thường xuyên, tuy nhiên, các biến ngẫu nhiên không chỉ được giới thiệu một cách trừu tượng. Thay vào đó, tập hợp các giá trị kết quả có thể xảy ra có ý nghĩa thực tế rõ ràng (không chỉ là các con số). Ngoài ra, các giá trị kết quả này có thể được định nghĩa dựa trên một loại thí nghiệm cụ thể (không phải là bất kỳ thí nghiệm tự nhiên nào với những giá trị đó).

Bây giờ, hãy xem xét một ví dụ về biến X không được định nghĩa một cách trừu tượng. X được định nghĩa như sau để xác định đội nào bắt đầu một trận bóng đá:

* X có tập hợp kết quả {đội đỏ đá mở màn, đội xanh đá mở màn}
* Lật một đồng xu cụ thể C: mặt ngửa = “đội đỏ đá mở màn”; mặt sấp = “đội xanh đá mở màn”
* Pr [X = đội đỏ đá mở màn] = 0.5
* Pr [X = đội xanh đá mở màn] = 0.5

Trong trường hợp này, tập hợp kết quả của X được cung cấp với một ý nghĩa cụ thể, đó là đội nào bắt đầu trong một trận bóng đá. Ngoài ra, các kết quả có thể xảy ra và xác suất liên quan của chúng được xác định bởi một thí nghiệm cụ thể, đó là lật một đồng xu cụ thể C.

Trong các cuộc thảo luận về mật mã học, các biến ngẫu nhiên thường được giới thiệu dựa trên một tập hợp kết quả có ý nghĩa thực tế. Đó có thể là tập hợp tất cả các thông điệp có thể được mã hóa, được biết đến là không gian thông điệp, hoặc tập hợp tất cả các khóa mà các bên sử dụng mã hóa có thể chọn, được biết đến là không gian khóa.

Tuy nhiên, các biến ngẫu nhiên trong các cuộc thảo luận về mật mã học thường không được định nghĩa dựa trên một thí nghiệm tự nhiên cụ thể, mà dựa trên bất kỳ thí nghiệm nào có thể tạo ra các phân phối xác suất phù hợp.

Các biến ngẫu nhiên có thể có phân phối xác suất rời rạc hoặc liên tục. Các biến ngẫu nhiên với **phân phối xác suất rời rạc**—nghĩa là, các biến ngẫu nhiên rời rạc—có một số lượng hữu hạn các kết quả có thể xảy ra. Biến ngẫu nhiên X trong cả hai ví dụ được đưa ra cho đến nay là rời rạc.

**Các biến ngẫu nhiên liên tục** thay vào đó có thể nhận giá trị trong một hoặc nhiều khoảng. Ví dụ, bạn có thể nói rằng, khi lấy mẫu, một biến ngẫu nhiên sẽ nhận bất kỳ giá trị thực nào từ 0 đến 1, và mỗi số thực trong khoảng này có khả năng xảy ra như nhau. Trong khoảng này, có vô số giá trị có thể xảy ra.

Đối với các cuộc thảo luận về mật mã học, bạn chỉ cần hiểu về các biến ngẫu nhiên rời rạc. Bất kỳ cuộc thảo luận nào về các biến ngẫu nhiên từ đây trở đi nên được hiểu là đề cập đến các biến ngẫu nhiên rời rạc, trừ khi có nêu rõ khác.

### Biểu đồ các biến ngẫu nhiên

Các giá trị có thể xảy ra và xác suất liên quan của một biến ngẫu nhiên có thể được hình dung dễ dàng thông qua một biểu đồ. Ví dụ, xem xét biến ngẫu nhiên X từ phần trước với tập hợp kết quả là {1,2}, và Pr [X = 1] = 0.5 và Pr [X = 2] = 0.5. Chúng ta thường hiển thị một biến ngẫu nhiên như vậy dưới dạng một biểu đồ cột như trong *Hình 1*.

*Hình 1: Biến ngẫu nhiên X*

![Hình 1: Biến ngẫu nhiên X.](assets/Figure2-1.webp)

Các cột rộng trong *Hình 1* rõ ràng không có ý nghĩa là biến ngẫu nhiên X thực sự liên tục. Thay vào đó, các cột được làm rộng ra nhằm mục đích hấp dẫn hơn về mặt hình ảnh (chỉ một đường thẳng đứng lên cung cấp một hình ảnh trực quan kém hơn).

### Các biến đồng nhất

Trong cụm từ “biến ngẫu nhiên,” thuật ngữ “ngẫu nhiên” chỉ có nghĩa là “xác suất”. Nói cách khác, nó chỉ có nghĩa là hai hoặc nhiều kết quả có thể xảy ra của biến xảy ra với một số xác suất nhất định. Tuy nhiên, các kết quả này không nhất thiết phải có khả năng xảy ra như nhau (mặc dù thuật ngữ “ngẫu nhiên” thực sự có thể có ý nghĩa đó trong các ngữ cảnh khác).
Một **biến ngẫu nhiên đều** là một trường hợp đặc biệt của biến ngẫu nhiên. Nó có thể nhận hai hoặc nhiều giá trị với xác suất bằng nhau. Biến ngẫu nhiên X được mô tả trong *Hình 1* rõ ràng là một biến ngẫu nhiên đều, vì cả hai kết quả có thể xảy ra với xác suất 0.5. Tuy nhiên, có nhiều biến ngẫu nhiên không phải là trường hợp của biến ngẫu nhiên đều.
Xem xét, ví dụ, biến ngẫu nhiên Y. Nó có bộ kết quả {1,2,3,8,10} và phân phối xác suất sau: Pr [Y = 1] = 0.25; Pr [Y = 2] = 0.35; Pr [Y = 3] = 0.1; Pr [Y = 8] = 0.25; Pr [Y = 10] = 0.05.

Mặc dù hai kết quả có thể xảy ra thực sự có xác suất bằng nhau, cụ thể là 1 và 8, Y cũng có thể nhận một số giá trị với xác suất khác 0.25 khi lấy mẫu. Do đó, mặc dù Y thực sự là một biến ngẫu nhiên, nó không phải là một biến ngẫu nhiên đều.

Một biểu đồ mô tả Y được cung cấp trong *Hình 2*.

*Hình 2: Biến ngẫu nhiên Y*

![Hình 2: Biến ngẫu nhiên Y.](assets/Figure2-2.webp "Hình 2: Biến ngẫu nhiên Y")

Ví dụ cuối cùng, xem xét biến ngẫu nhiên Z. Nó có bộ kết quả {1,3,7,11,12} và phân phối xác suất sau: Pr (2) = 0.2; Pr (3) = 0.2; Pr (9) = 0.2; Pr (11) = 0.2; Pr (12) = 0.2. Bạn có thể thấy nó được mô tả trong Hình 3. Biến ngẫu nhiên Z, trái ngược với Y, thực sự là một biến ngẫu nhiên đều, vì tất cả các xác suất cho các giá trị có thể xảy ra khi lấy mẫu là bằng nhau.

*Hình 3: Biến ngẫu nhiên Z*

![Hình 3: Biến ngẫu nhiên Z.](assets/Figure2-3.webp "Hình 3: Biến ngẫu nhiên Z")


### Xác suất có điều kiện

Giả sử Bob có ý định chọn đều một ngày từ năm lịch trước. Chúng ta nên kết luận xác suất của việc chọn được một ngày vào mùa Hè là bao nhiêu?

Miễn là chúng ta nghĩ quy trình của Bob thực sự là đều, chúng ta nên kết luận rằng có xác suất 1/4 Bob chọn một ngày vào mùa Hè. Đây là **xác suất không điều kiện** của việc ngày được chọn ngẫu nhiên là vào mùa Hè.

Giả sử bây giờ thay vì chọn đều một ngày lịch, Bob chỉ chọn đều từ những ngày mà nhiệt độ buổi trưa tại Crystal Lake (New Jersey) là 21 độ Celsius hoặc cao hơn. Với thông tin bổ sung này, chúng ta có thể kết luận xác suất Bob sẽ chọn một ngày vào mùa Hè là bao nhiêu?

Chúng ta thực sự nên rút ra một kết luận khác so với trước, ngay cả khi không có thêm thông tin cụ thể nào (ví dụ, nhiệt độ buổi trưa mỗi ngày trong năm lịch trước).

Biết rằng Crystal Lake nằm ở New Jersey, chúng ta chắc chắn không mong đợi nhiệt độ buổi trưa là 21 độ Celsius hoặc cao hơn vào mùa Đông. Thay vào đó, có khả năng cao hơn là một ngày ấm áp vào mùa Xuân hoặc mùa Thu, hoặc một ngày nào đó trong mùa Hè. Do đó, biết nhiệt độ buổi trưa tại Crystal Lake vào ngày được chọn là 21 độ Celsius hoặc cao hơn, xác suất ngày được Bob chọn là vào mùa Hè trở nên cao hơn. Đây là **xác suất có điều kiện** của việc ngày được chọn ngẫu nhiên là vào mùa Hè, với điều kiện nhiệt độ buổi trưa tại Crystal Lake là 21 độ Celsius hoặc cao hơn.
Khác với ví dụ trước, xác suất của hai sự kiện cũng có thể hoàn toàn không liên quan. Trong trường hợp đó, chúng ta nói rằng chúng là **độc lập**.

Giả sử, ví dụ, một đồng xu công bằng đã đáp mặt ngửa. Dựa vào sự kiện này, vậy thì xác suất trời sẽ mưa ngày mai là bao nhiêu? Xác suất có điều kiện trong trường hợp này nên giống như xác suất không điều kiện trời sẽ mưa ngày mai, vì việc tung đồng xu nói chung không có ảnh hưởng gì đến thời tiết.

Chúng ta sử dụng ký hiệu “|” để viết các phát biểu xác suất có điều kiện. Ví dụ, xác suất của sự kiện A biết rằng sự kiện B đã xảy ra có thể được viết như sau: Pr[A|B]. Vậy, khi hai sự kiện, A và B, là độc lập, thì Pr[A|B] = Pr[A] và Pr[B|A] = Pr[B]. Điều kiện cho sự độc lập có thể được đơn giản hóa như sau: Pr[A,B] = Pr[A]*Pr[B].

Một kết quả quan trọng trong lý thuyết xác suất được biết đến là **Định lý Bayes**. Nó cơ bản nói rằng Pr[A|B] có thể được viết lại như sau:

Pr[A|B] = (Pr[B|A] • Pr[A]) / Pr[B]

Thay vì sử dụng xác suất có điều kiện với các sự kiện cụ thể, chúng ta cũng có thể xem xét các xác suất có điều kiện liên quan đến hai hoặc nhiều biến ngẫu nhiên trên một tập hợp các sự kiện có thể. Giả sử hai biến ngẫu nhiên, X và Y. Chúng ta có thể chỉ định bất kỳ giá trị nào có thể cho X bằng x, và bất kỳ giá trị nào có thể cho Y bằng y. Chúng ta có thể nói rằng, hai biến ngẫu nhiên là độc lập nếu phát biểu sau đây được giữ vững:

Pr[X = x,Y = y] = Pr[X = x] • Pr[Y = y] cho mọi x và y

Hãy làm rõ hơn về ý nghĩa của phát biểu này.

Giả sử rằng các tập hợp kết quả cho X và Y được định nghĩa như sau: **X** = {x<sub>1</sub>,x<sub>2</sub>….,x<sub>i</sub>,….x<sub>n</sub>} và **Y** = {y<sub>1</sub>,y<sub>2</sub>….,y<sub>i</sub>,….y<sub>m</sub>}. (Thông thường, các tập hợp giá trị được chỉ định bằng chữ in đậm, chữ hoa.)

Bây giờ giả sử bạn lấy mẫu Y và quan sát y<sub>1</sub>. Phát biểu trên cho chúng ta biết rằng xác suất hiện tại thu được x<sub>1</sub> từ việc lấy mẫu X chính xác giống như khi chúng ta chưa bao giờ quan sát y<sub>1</sub>. Điều này đúng cho bất kỳ y<sub>i</sub> nào chúng ta có thể đã rút ra từ việc lấy mẫu ban đầu của Y. Cuối cùng, điều này không chỉ đúng cho x<sub>1</sub>. Đối với bất kỳ x<sub>i</sub> nào, xác suất xảy ra không bị ảnh hưởng bởi kết quả của việc lấy mẫu Y. Tất cả điều này cũng áp dụng cho trường hợp X được lấy mẫu trước.

Hãy kết thúc cuộc thảo luận của chúng ta trên một điểm hơi triết lý hơn. Trong bất kỳ tình huống thực tế nào, xác suất của một sự kiện luôn được đánh giá dựa trên một tập hợp thông tin cụ thể. Không có "xác suất không điều kiện" nào trong bất kỳ nghĩa nào chặt chẽ của từ này.

Ví dụ, giả sử tôi hỏi bạn xác suất lợn sẽ bay vào năm 2030. Mặc dù tôi không cung cấp thêm thông tin nào, bạn rõ ràng biết rất nhiều về thế giới có thể ảnh hưởng đến phán đoán của mình. Bạn chưa bao giờ thấy lợn bay. Bạn biết rằng hầu hết mọi người sẽ không mong đợi chúng bay. Bạn biết rằng chúng không thực sự được tạo ra để bay. Và vân vân.
Vậy, khi chúng ta nói về "xác suất không điều kiện" của một sự kiện nào đó trong bối cảnh thực tế, thuật ngữ này thực sự chỉ có ý nghĩa nếu chúng ta hiểu nó như là "xác suất mà không cần bất kỳ thông tin rõ ràng nào khác". Mọi hiểu biết về "xác suất có điều kiện" thì luôn phải được hiểu là dựa trên một thông tin cụ thể nào đó.
Ví dụ, tôi có thể hỏi bạn xác suất lợn sẽ bay vào năm 2030, sau khi cung cấp cho bạn bằng chứng rằng một số con dê ở New Zealand đã học cách bay sau vài năm huấn luyện. Trong trường hợp này, bạn có thể sẽ điều chỉnh phán đoán của mình về xác suất lợn sẽ bay vào năm 2030. Vậy xác suất lợn sẽ bay vào năm 2030 phụ thuộc vào bằng chứng này về dê ở New Zealand.

## Phép toán modulo
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

Biểu thức cơ bản nhất với **phép toán modulo** có dạng sau: x mod y.

Biến x được gọi là số bị chia và biến y là số chia. Để thực hiện phép toán modulo với số bị chia dương và số chia dương, bạn chỉ cần xác định phần dư của phép chia.

Ví dụ, xem xét biểu thức 25 mod 4. Số 4 chia vào số 25 tổng cộng 6 lần. Phần dư của phép chia đó là 1. Do đó, 25 mod 4 bằng 1. Một cách tương tự, chúng ta có thể đánh giá các biểu thức dưới đây:

* 29 mod 30 = 29 (vì 30 chia vào 29 tổng cộng 0 lần và phần dư là 29)
* 42 mod 2 = 0 (vì 2 chia vào 42 tổng cộng 21 lần và phần dư là 0)
* 12 mod 5 = 2 (vì 5 chia vào 12 tổng cộng 2 lần và phần dư là 2)
* 20 mod 8 = 4 (vì 8 chia vào 20 tổng cộng 2 lần và phần dư là 4)

Khi số bị chia hoặc số chia là số âm, các ngôn ngữ lập trình có thể xử lý phép toán modulo theo cách khác nhau.

Bạn chắc chắn sẽ gặp trường hợp với số bị chia âm trong mật mã học. Trong những trường hợp này, cách tiếp cận điển hình như sau:

* Đầu tiên xác định giá trị gần nhất *thấp hơn hoặc bằng* số bị chia mà số chia chia hết cho số đó với phần dư bằng không. Gọi giá trị đó là p.
* Nếu số bị chia là x, thì kết quả của phép toán modulo là giá trị của x – p.

Ví dụ, giả sử số bị chia là –20 và số chia là 3. Giá trị gần nhất thấp hơn hoặc bằng –20 mà 3 chia hết là –21. Giá trị của x – p trong trường hợp này là –20 – (–21). Điều này bằng 1 và, do đó, –20 mod 3 bằng 1. Một cách tương tự, chúng ta có thể đánh giá các biểu thức dưới đây:

* –8 mod 5 = 2
* –19 mod 16 = 13
* –14 mod 6 = 4

Về ký hiệu, bạn sẽ thường thấy các loại biểu thức sau: x = [y mod z]. Do có dấu ngoặc, phép toán modulo trong trường hợp này chỉ áp dụng cho phần bên phải của biểu thức. Nếu y bằng 25 và z bằng 4, ví dụ, thì x được đánh giá là 1.
Không có dấu ngoặc, phép toán modulo tác động lên *cả hai bên* của một biểu thức. Giả sử, ví dụ, biểu thức sau: x = y mod z. Nếu y bằng 25 và z bằng 4, thì tất cả những gì chúng ta biết là x mod 4 đánh giá bằng 1. Điều này phù hợp với bất kỳ giá trị nào của x từ tập hợp {….– 7, – 3, 1, 5, 9….}.
Nhánh của toán học liên quan đến các phép toán modulo trên các số và biểu thức được gọi là **số học modulo**. Bạn có thể coi nhánh này như là số học cho các trường hợp mà dòng số không vô hạn dài. Mặc dù chúng ta thường gặp phép toán modulo cho các số nguyên (dương) trong mật mã học, bạn cũng có thể thực hiện các phép toán modulo sử dụng bất kỳ số thực nào.

### Mật mã dịch chuyển

Phép toán modulo thường xuyên được gặp trong mật mã học. Để minh họa, hãy xem xét một trong những phương pháp mã hóa lịch sử nổi tiếng nhất: mật mã dịch chuyển.

Hãy định nghĩa nó trước. Giả sử một từ điển *D* tương đương tất cả các chữ cái của bảng chữ cái tiếng Anh, theo thứ tự, với tập hợp các số {0,1,2…,25}. Giả định một không gian tin nhắn **M**. **Mật mã dịch chuyển** là, sau đó, một phương pháp mã hóa được định nghĩa như sau:

- Chọn đồng nhất một khóa k từ không gian khóa **K**, nơi **K** = {0,1,2,…,25}<sup>[1](#footnote1)</sup>
- Mã hóa một tin nhắn m thuộc **M**, như sau:
    - Tách m thành các chữ cái riêng lẻ m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Chuyển đổi mỗi m<sub>i</sub> thành một số theo *D*
    - Đối với mỗi m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Chuyển đổi mỗi c<sub>i</sub> thành một chữ cái theo *D*
    - Sau đó kết hợp c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub> để tạo ra bản mã hóa c
- Giải mã một bản mã hóa c như sau:
    -- Chuyển đổi mỗi c<sub>i</sub> thành một số theo *D*
    -- Đối với mỗi c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    -- Chuyển đổi mỗi m<sub>i</sub> thành một chữ cái theo *D*
    -- Sau đó kết hợp m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub> để tạo ra tin nhắn gốc m

Toán tử modulo trong mật mã dịch chuyển đảm bảo rằng các chữ cái được bao phủ, sao cho tất cả các chữ cái mã hóa được định nghĩa. Để minh họa, xem xét việc áp dụng mật mã dịch chuyển trên từ “DOG”.

Giả sử bạn đã chọn đồng nhất một khóa có giá trị 17. Chữ “O” tương đương với 15. Không có phép toán modulo, việc cộng số này với khóa sẽ tạo ra một số mã hóa là 32. Tuy nhiên, số mã hóa đó không thể được chuyển đổi thành một chữ cái mã hóa, vì bảng chữ cái tiếng Anh chỉ có 26 chữ cái. Phép toán modulo đảm bảo rằng số mã hóa thực sự là 6 (kết quả của 32 mod 26), tương đương với chữ cái mã hóa “G”.

Toàn bộ quá trình mã hóa từ “DOG” với giá trị khóa 17 như sau:
* Tin nhắn = DOG = D,O,G = 3,15,6* c<sub>0</sub> = [(3 + 17) Mod 26] = [(20) Mod 26] = 20 = U
* c<sub>1</sub> = [(15 + 17) Mod 26] = [(32) Mod 26] = 6 = G
* c<sub>2</sub> = [(6 + 17) Mod 26] = [(23) Mod 26] = 23 = X
* c = UGX

Mọi người có thể hiểu một cách trực quan cách hoạt động của mã dịch chuyển và có thể tự mình sử dụng nó. Tuy nhiên, để nâng cao kiến thức về mật mã học, điều quan trọng là bắt đầu trở nên thoải mái hơn với việc hình thức hóa, vì các kế hoạch sẽ trở nên phức tạp hơn nhiều. Do đó, các bước cho mã dịch chuyển đã được hình thức hóa.

## Phép toán XOR
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Tất cả dữ liệu máy tính được xử lý, lưu trữ và gửi qua mạng ở cấp độ bit. Bất kỳ kế hoạch mật mã nào được áp dụng cho dữ liệu máy tính cũng hoạt động ở cấp độ bit.

Chẳng hạn, giả sử bạn đã nhập một e-mail vào ứng dụng e-mail của mình. Bất kỳ mã hóa nào bạn áp dụng không diễn ra trực tiếp trên các ký tự ASCII của e-mail của bạn. Thay vào đó, nó được áp dụng cho biểu diễn bit của các chữ cái và các ký hiệu khác trong e-mail của bạn.

Một phép toán toán học quan trọng cần hiểu cho mật mã học hiện đại, ngoài phép toán modulo, là phép toán **XOR**, hay phép toán “hoặc độc quyền”. Phép toán này nhận hai bit làm đầu vào và cho ra một bit khác làm đầu ra. Phép toán XOR sẽ đơn giản được ký hiệu là "XOR". Nó cho ra 0 nếu hai bit giống nhau và 1 nếu hai bit khác nhau. Bạn có thể thấy bốn khả năng dưới đây.

* 0 XOR 0 = 0
* 0 XOR 1 = 1
* 1 XOR 0 = 1
* 1 XOR 1 = 0

Bạn có thể thực hiện phép toán XOR trên hai tin nhắn dài hơn một bit bằng cách xếp các bit của hai tin nhắn đó và thực hiện phép toán XOR trên từng cặp bit riêng lẻ.

Để minh họa, giả sử bạn có một tin nhắn m<sub>1</sub> (01111001) và một tin nhắn m<sub>2</sub> (01011001). Phép toán XOR của hai tin nhắn này có thể được thấy dưới đây.

* m<sub>1</sub> XOR m<sub>2</sub> = 01111001 XOR 01011001 = 00100000

Quy trình này rất đơn giản. Bạn đầu tiên XOR các bit ở cực trái của m<sub>1</sub> và m<sub>2</sub>. Trong trường hợp này là 0 XOR 0 = 0. Sau đó bạn XOR cặp bit thứ hai từ trái sang. Trong trường hợp này là 1 XOR 1 = 0. Bạn tiếp tục quy trình này cho đến khi bạn đã thực hiện phép toán XOR trên các bit cực phải.
Dễ thấy rằng phép toán XOR có tính chất giao hoán, tức là m<sub>1</sub> XOR m<sub>2</sub> = m<sub>2</sub> XOR m<sub>1</sub>. Ngoài ra, phép toán XOR cũng có tính chất kết hợp. Điều đó có nghĩa là, (m<sub>1</sub> XOR m<sub>2</sub>) XOR m<sub>3</sub> = m<sub>1</sub> XOR (m<sub>2</sub> XOR m<sub>3</sub>).
Phép toán XOR trên hai chuỗi có độ dài khác nhau có thể được hiểu theo nhiều cách, tùy thuộc vào ngữ cảnh. Chúng ta sẽ không quan tâm đến các phép toán XOR trên các chuỗi có độ dài khác nhau ở đây.

Phép toán XOR tương đương với trường hợp đặc biệt của việc thực hiện phép toán modulo trên tổng của các bit khi số chia là 2. Bạn có thể thấy sự tương đương trong các kết quả sau:

* (0 + 0) mod 2 = 0 XOR 0 = 0
* (1 + 0) mod 2 = 1 XOR 0 = 1
* (0 + 1) mod 2 = 0 XOR 1 = 1
* (1 + 1) mod 2 = 1 XOR 1 = 0

## Tính Ngẫu Nhiên Giả
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Trong cuộc thảo luận của chúng tôi về các biến ngẫu nhiên và đồng nhất, chúng tôi đã rõ ràng phân biệt giữa “ngẫu nhiên” và “đồng nhất”. Sự phân biệt này thường được duy trì trong thực hành khi mô tả các biến ngẫu nhiên. Tuy nhiên, trong ngữ cảnh hiện tại của chúng tôi, sự phân biệt này cần được bỏ qua và “ngẫu nhiên” và “đồng nhất” được sử dụng một cách đồng nghĩa. Tôi sẽ giải thích lý do vào cuối phần này.

Để bắt đầu, chúng ta có thể gọi một chuỗi nhị phân có độ dài n là **ngẫu nhiên** (hoặc **đồng nhất**), nếu nó là kết quả của việc lấy mẫu một biến đồng nhất S mà cho mỗi chuỗi nhị phân có độ dài n một xác suất chọn lựa đồng nhất.

Giả sử, ví dụ, tập hợp tất cả các chuỗi nhị phân có độ dài 8: {0000 0000, 0000 0001,…, 1111 1111}. (Thông thường, một chuỗi 8-bit được viết thành hai bộ tứ, mỗi bộ được gọi là một **nibble**.) Hãy gọi tập hợp này là **S<sub>8</sub>**.

Theo định nghĩa trên, chúng ta có thể, sau đó, gọi một chuỗi nhị phân cụ thể có độ dài 8 là ngẫu nhiên (hoặc đồng nhất), nếu nó là kết quả của việc lấy mẫu một biến đồng nhất S mà cho mỗi chuỗi trong **S<sub>8</sub>** một xác suất chọn lựa đồng nhất. Với việc tập hợp **S<sub>8</sub>** bao gồm 2<sup>8</sup> phần tử, xác suất chọn lựa khi lấy mẫu sẽ phải là 1/2<sup>8</sup> cho mỗi chuỗi trong tập hợp.

Một khía cạnh quan trọng của tính ngẫu nhiên của một chuỗi nhị phân là nó được định nghĩa dựa trên quy trình mà qua đó nó được chọn. Do đó, hình thức của bất kỳ chuỗi nhị phân cụ thể nào, vì thế, không tiết lộ bất cứ điều gì về tính ngẫu nhiên trong việc chọn lựa của nó.

Ví dụ, nhiều người một cách trực giác có ý tưởng rằng một chuỗi như 1111 1111 không thể được chọn một cách ngẫu nhiên. Nhưng điều này rõ ràng là sai.
Định nghĩa một biến đồng nhất S trên tất cả các chuỗi nhị phân có độ dài 8, khả năng chọn được chuỗi 1111 1111 từ tập **S<sub>8</sub>** là như nhau so với một chuỗi như 0111 01001. Do đó, bạn không thể nói bất cứ điều gì về tính ngẫu nhiên của một chuỗi, chỉ bằng cách phân tích chính chuỗi đó. 
Chúng ta cũng có thể nói về chuỗi ngẫu nhiên mà không cụ thể chỉ là chuỗi nhị phân. Chẳng hạn, chúng ta có thể nói về một chuỗi hex ngẫu nhiên AF 02 82. Trong trường hợp này, chuỗi được chọn ngẫu nhiên từ tập hợp tất cả các chuỗi hex có độ dài 6. Điều này tương đương với việc chọn ngẫu nhiên một chuỗi nhị phân có độ dài 24, vì mỗi chữ số hex biểu diễn 4 bit.

Thông thường, cụm từ “một chuỗi ngẫu nhiên”, không có điều kiện, ám chỉ một chuỗi được chọn ngẫu nhiên từ tập hợp tất cả các chuỗi có cùng độ dài. Đây là cách tôi đã mô tả ở trên. Một chuỗi có độ dài n có thể, tất nhiên, cũng được chọn ngẫu nhiên từ một tập hợp khác. Một tập hợp, chẳng hạn, chỉ bao gồm một tập hợp con của tất cả các chuỗi có độ dài n, hoặc có thể là một tập hợp bao gồm các chuỗi có độ dài khác nhau. Tuy nhiên, trong những trường hợp đó, chúng ta sẽ không gọi nó là “một chuỗi ngẫu nhiên”, mà là “một chuỗi được chọn ngẫu nhiên từ một số tập hợp **S**”.

Một khái niệm chủ chốt trong mật mã học là khái niệm về tính giả ngẫu nhiên. Một **chuỗi giả ngẫu nhiên** có độ dài n trông *như thể* nó là kết quả của việc lấy mẫu một biến đồng nhất S mà cho mỗi chuỗi trong **S<sub>n</sub>** một khả năng được chọn ngang nhau. Tuy nhiên, thực tế, chuỗi đó là kết quả của việc lấy mẫu một biến đồng nhất S' chỉ định một phân phối xác suất - không nhất thiết là một phân phối có xác suất ngang nhau cho tất cả các kết quả có thể - trên một tập hợp con của **S<sub>n</sub>**. Điểm then chốt ở đây là không ai có thể thực sự phân biệt được giữa các mẫu từ S và S', ngay cả khi bạn lấy rất nhiều mẫu.

Giả sử, ví dụ, một biến ngẫu nhiên S. Tập hợp kết quả của nó là **S<sub>256</sub>**, đây là tập hợp tất cả các chuỗi nhị phân có độ dài 256. Tập hợp này có 2<sup>256</sup> phần tử. Mỗi phần tử có một khả năng được chọn ngang nhau, 1/2<sup>256</sup>, khi lấy mẫu.

Thêm vào đó, giả sử một biến ngẫu nhiên S’. Tập hợp kết quả của nó chỉ bao gồm 2<sup>128</sup> chuỗi nhị phân có độ dài 256. Nó có một số phân phối xác suất trên những chuỗi đó, nhưng phân phối này không nhất thiết là đồng nhất.

Giả sử rằng bây giờ tôi lấy 1000 mẫu từ S và 1000 mẫu từ S' và đưa hai tập hợp kết quả cho bạn. Tôi nói cho bạn biết tập hợp kết quả nào liên quan đến biến ngẫu nhiên nào. Tiếp theo, tôi lấy một mẫu từ một trong hai biến ngẫu nhiên. Nhưng lần này tôi không nói cho bạn biết tôi lấy mẫu từ biến ngẫu nhiên nào. Nếu S' là giả ngẫu nhiên, thì ý tưởng là khả năng bạn đoán đúng biến ngẫu nhiên mà tôi lấy mẫu gần như không tốt hơn 1/2.

Thông thường, một chuỗi giả ngẫu nhiên có độ dài n được tạo ra bằng cách chọn ngẫu nhiên một chuỗi có kích thước n – x, nơi x là một số nguyên dương, và sử dụng nó làm đầu vào cho một thuật toán mở rộng. Chuỗi ngẫu nhiên có kích thước n – x này được biết đến là **hạt giống**.
Các chuỗi giả ngẫu nhiên là một khái niệm chính để làm cho mật mã học trở nên thiết thực. Xem xét, ví dụ, các mật mã dòng. Với một mật mã dòng, một khóa được chọn ngẫu nhiên được cắm vào một thuật toán mở rộng để tạo ra một chuỗi giả ngẫu nhiên lớn hơn nhiều. Chuỗi giả ngẫu nhiên này sau đó được kết hợp với bản rõ thông qua một phép toán XOR để tạo ra một bản mã hóa. Nếu chúng ta không thể tạo ra loại chuỗi giả ngẫu nhiên này cho một mật mã dòng, thì chúng ta sẽ cần một khóa có độ dài bằng với thông điệp để đảm bảo an ninh. Đây không phải là một lựa chọn thực tế trong hầu hết các trường hợp.

Khái niệm về giả ngẫu nhiên được thảo luận trong phần này có thể được định nghĩa một cách chính thức hơn. Nó cũng mở rộng ra các bối cảnh khác. Nhưng chúng ta không cần phải đi sâu vào cuộc thảo luận đó ở đây. Tất cả những gì bạn thực sự cần hiểu một cách trực quan cho phần lớn mật mã học là sự khác biệt giữa một chuỗi ngẫu nhiên và một chuỗi giả ngẫu nhiên.

Lý do để bỏ qua sự phân biệt giữa "ngẫu nhiên" và "đồng nhất" trong cuộc thảo luận của chúng ta bây giờ cũng nên rõ ràng. Trên thực tế, mọi người sử dụng thuật ngữ giả ngẫu nhiên để chỉ một chuỗi có vẻ **như thể** nó là kết quả của việc lấy mẫu một biến đồng nhất S. Nói một cách chính xác, chúng ta nên gọi một chuỗi như vậy là "giả đồng nhất," áp dụng ngôn ngữ của chúng ta từ trước. Vì thuật ngữ "giả đồng nhất" vừa cồng kềnh và không được ai sử dụng, chúng ta sẽ không giới thiệu nó ở đây để rõ ràng. Thay vào đó, chúng ta chỉ bỏ qua sự phân biệt giữa "ngẫu nhiên" và "đồng nhất" trong bối cảnh hiện tại.

## Ghi chú

<chapterId>7cccd92c-15bc-5394-9024-af126988ecd7</chapterId>

[^1]: Chúng ta có thể định nghĩa chính xác câu này, sử dụng thuật ngữ từ phần trước. Hãy để một biến đồng nhất K có **K** là tập hợp các kết quả có thể có. Vì vậy Pr [K = 0] = 1/26, Pr [K = 1] = 1/26, và cứ thế. Lấy mẫu biến đồng nhất K một lần để tạo ra một khóa cụ thể [^1].

[^2]: Nếu quan tâm đến một bài trình bày chính thức hơn về những vấn đề này, bạn có thể tham khảo *Introduction to Modern Cryptography* của Katz và Lindell, đặc biệt là chương 3 [^2].

# Nền tảng Toán học của Mật mã học II
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

Chương này bao gồm một chủ đề nâng cao hơn về nền tảng toán học của mật mã học: lý thuyết số. Mặc dù lý thuyết số quan trọng đối với mật mã đối xứng (như trong Mật mã Rijndael), nó đặc biệt quan trọng trong cài đặt mật mã công khai.

Nếu bạn thấy chi tiết của lý thuyết số gây khó chịu, tôi sẽ khuyên bạn nên đọc sơ qua lần đầu tiên. Bạn luôn có thể quay lại nó vào một thời điểm sau.

## Lý thuyết số là gì?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>

Bạn có thể mô tả **lý thuyết số** là nghiên cứu về các tính chất của số nguyên và các hàm toán học làm việc với số nguyên.

Xem xét, ví dụ, rằng bất kỳ hai số nào a và N là **nguyên tố cùng nhau** (hoặc **số nguyên tố tương đối**) nếu ước chung lớn nhất của chúng bằng 1. Giả sử bây giờ một số nguyên cụ thể N. Có bao nhiêu số nguyên nhỏ hơn N là nguyên tố cùng nhau với N? Chúng ta có thể đưa ra các phát biểu chung về câu trả lời cho câu hỏi này không? Đây là các loại câu hỏi điển hình mà lý thuyết số tìm cách trả lời.
Lý thuyết số hiện đại dựa vào các công cụ của đại số trừu tượng. Lĩnh vực **đại số trừu tượng** là một nhánh con của toán học, nơi mà đối tượng chính của phân tích là các đối tượng trừu tượng được biết đến như cấu trúc đại số. Một **cấu trúc đại số** là một tập hợp các phần tử kết hợp với một hoặc nhiều phép toán, tuân theo một số tiên đề nhất định. Thông qua cấu trúc đại số, các nhà toán học có thể hiểu sâu hơn về các vấn đề toán học cụ thể, bằng cách trừu tượng hóa khỏi chi tiết của chúng.

Lĩnh vực đại số trừu tượng đôi khi còn được gọi là đại số hiện đại. Bạn cũng có thể gặp khái niệm **toán học trừu tượng** (hoặc **toán học thuần túy**). Thuật ngữ sau không phải là ám chỉ đến đại số trừu tượng, mà có nghĩa là việc nghiên cứu toán học vì chính nó, không chỉ với mục đích ứng dụng tiềm năng.

Các tập hợp từ đại số trừu tượng có thể đối phó với nhiều loại đối tượng, từ các biến đổi bảo toàn hình dạng trên một tam giác đều cho đến các mẫu hình nền. Đối với lý thuyết số, chúng ta chỉ xem xét các tập hợp các phần tử chứa số nguyên hoặc các hàm làm việc với số nguyên.

## Nhóm
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Một khái niệm cơ bản trong toán học là về một tập hợp các phần tử. Một tập hợp thường được ký hiệu bằng dấu ngoặc nhọn với các phần tử được phân tách bằng dấu phẩy.

Ví dụ, tập hợp tất cả các số nguyên là {…,-2,-1,0,1,2,…}. Dấu chấm lửng ở đây có nghĩa là một mẫu nhất định tiếp tục theo một hướng cụ thể. Vì vậy, tập hợp tất cả các số nguyên cũng bao gồm 3,4,5,6 và tiếp tục như vậy, cũng như -3,-4,-5,-6 và tiếp tục như vậy. Tập hợp tất cả các số nguyên này thường được ký hiệu là ℤ.

Một ví dụ khác về tập hợp là ℤ mod 11, hoặc tập hợp tất cả các số nguyên theo modulo 11. Trái ngược với toàn bộ tập hợp ℤ, tập hợp này chỉ chứa một số lượng hữu hạn các phần tử, cụ thể là {0,1,…,9,10}.

Một sai lầm phổ biến là nghĩ rằng tập hợp ℤ mod 11 thực sự là {-10,-9,….,0,….,9,10}. Nhưng đây không phải là trường hợp, dựa trên cách chúng ta đã định nghĩa phép toán modulo trước đây. Bất kỳ số nguyên âm nào giảm bằng modulo 11 đều được chuyển thành {0,1,….,9,10}. Ví dụ, biểu thức -2 mod 11 được chuyển thành 9, trong khi biểu thức -27 mod 11 được chuyển thành 5.

Một khái niệm cơ bản khác trong toán học là về phép toán nhị phân. Đây là bất kỳ phép toán nào lấy hai phần tử để tạo ra một phần tử thứ ba. Ví dụ, từ đại số và số học cơ bản, bạn sẽ quen thuộc với bốn phép toán nhị phân cơ bản: cộng, trừ, nhân và chia.

Hai khái niệm toán học cơ bản này, tập hợp và phép toán nhị phân, được sử dụng để định nghĩa khái niệm về nhóm, cấu trúc quan trọng nhất trong đại số trừu tượng.

Cụ thể, giả sử một phép toán nhị phân ◌. Ngoài ra, giả sử một tập hợp các phần tử **S** được trang bị phép toán đó. Tất cả “được trang bị” ở đây có nghĩa là phép toán ◌ có thể được thực hiện giữa bất kỳ hai phần tử nào trong tập hợp **S**.

Sự kết hợp 〈**S**, ◌〉, vậy, là một **nhóm** nếu nó đáp ứng bốn điều kiện cụ thể, được biết đến như các tiên đề nhóm.

1. Đối với bất kỳ a và b nào là các phần tử của **S**, a ◌ b cũng là một phần tử của **S**. Điều này được biết đến như **điều kiện đóng**.
2. Đối với bất kỳ a, b, và c nào là các phần tử của **S**, ta có (a ◌ b) ◌ c = a ◌ (b ◌ c). Điều này được biết đến là **điều kiện kết hợp**. 3. Có một phần tử duy nhất e trong **S**, sao cho với mọi phần tử a trong **S**, phương trình sau được thỏa mãn: e ◌ a = a ◌ e = a. Vì chỉ có một phần tử e như vậy, nó được gọi là **phần tử đồng nhất**. Điều kiện này được biết đến là **điều kiện đồng nhất**.
4. Đối với mỗi phần tử a trong **S**, tồn tại một phần tử b trong **S**, sao cho phương trình sau được thỏa mãn: a ◌ b = b ◌ a = e, nơi e là phần tử đồng nhất. Phần tử b ở đây được biết đến là **phần tử nghịch đảo**, và thường được ký hiệu là a<sup>-1</sup>. Điều kiện này được biết đến là **điều kiện nghịch đảo** hoặc **điều kiện khả nghịch**.

Hãy khám phá thêm về nhóm. Ký hiệu tập hợp tất cả các số nguyên bằng ℤ. Tập hợp này kết hợp với phép cộng tiêu chuẩn, hay 〈ℤ, +〉, rõ ràng phù hợp với định nghĩa của một nhóm, vì nó đáp ứng bốn tiên đề trên.

1. Đối với bất kỳ x và y nào là các phần tử của ℤ, x + y cũng là một phần tử của ℤ. Vì vậy 〈ℤ, +〉 thỏa mãn điều kiện đóng.
2. Đối với bất kỳ x, y, và z nào là các phần tử của ℤ, (x + y) + z = x + (y + z). Vì vậy 〈ℤ, +〉 thỏa mãn điều kiện kết hợp.
3. Có một phần tử đồng nhất trong 〈ℤ, +〉, cụ thể là 0. Đối với bất kỳ x nào trong ℤ, nó cụ thể thỏa mãn: 0 + x = x + 0 = x. Vì vậy 〈ℤ, +〉 thỏa mãn điều kiện đồng nhất.
4. Cuối cùng, đối với mỗi phần tử x trong ℤ, có một y sao cho x + y = y + x = 0. Nếu x là 10, ví dụ, y sẽ là – 10 (trong trường hợp x là 0, y cũng là 0). Vì vậy 〈ℤ, +〉 thỏa mãn điều kiện nghịch đảo.

Quan trọng là, việc tập hợp các số nguyên với phép cộng tạo thành một nhóm không có nghĩa là nó tạo thành một nhóm với phép nhân. Bạn có thể xác minh điều này bằng cách kiểm tra 〈ℤ, •〉 đối với bốn tiên đề nhóm (nơi • biểu thị phép nhân tiêu chuẩn).

Hai tiên đề đầu tiên rõ ràng được thỏa mãn. Ngoài ra, dưới phép nhân, phần tử 1 có thể đóng vai trò là phần tử đồng nhất. Bất kỳ số nguyên x nào nhân với 1, cụ thể cho ra x. Tuy nhiên, 〈ℤ, •〉 không thỏa mãn điều kiện nghịch đảo. Đó là, không có một phần tử y duy nhất trong ℤ cho mỗi x trong ℤ, sao cho x • y = 1.

Ví dụ, giả sử x = 22. Giá trị y nào từ tập hợp ℤ nhân với x sẽ cho ra phần tử đồng nhất 1? Giá trị của 1/22 sẽ phù hợp, nhưng đây không phải là trong tập hợp ℤ. Thực tế, bạn sẽ gặp vấn đề này với bất kỳ số nguyên x nào, ngoại trừ các giá trị của 1 và -1 (nơi y sẽ phải là 1 và -1 tương ứng).
Nếu chúng ta cho phép sử dụng số thực cho tập hợp của mình, thì phần lớn các vấn đề sẽ biến mất. Đối với bất kỳ phần tử x nào trong tập hợp, phép nhân với 1/x sẽ cho kết quả là 1. Vì phân số được bao gồm trong tập hợp số thực, nên có thể tìm thấy nghịch đảo cho mọi số thực. Ngoại lệ là số không, vì bất kỳ phép nhân nào với số không cũng không bao giờ cho kết quả là phần tử đồng nhất 1. Do đó, tập hợp các số thực không phải là số không, được trang bị phép nhân, thực sự là một nhóm.

Một số nhóm đáp ứng điều kiện tổng quát thứ năm, được biết đến là **điều kiện giao hoán**. Điều kiện này như sau:

* Giả sử một nhóm G với tập hợp **S** và một toán tử nhị phân ◌. Giả sử rằng a và b là các phần tử của **S**. Nếu trường hợp a ◌ b = b ◌ a đúng cho bất kỳ hai phần tử a và b nào trong **S**, thì G đáp ứng điều kiện giao hoán.

Bất kỳ nhóm nào đáp ứng điều kiện giao hoán được biết đến là **nhóm giao hoán**, hoặc một **nhóm Abel** (đặt theo tên Niels Henrik Abel). Dễ dàng xác minh rằng cả tập hợp số thực qua phép cộng và tập hợp số nguyên qua phép cộng đều là nhóm Abel. Tập hợp số nguyên qua phép nhân không phải là một nhóm, do đó không thể là một nhóm Abel. Ngược lại, tập hợp các số thực không phải là số không qua phép nhân cũng là một nhóm Abel.

Bạn nên chú ý đến hai quy ước quan trọng về ký hiệu. Đầu tiên, các dấu “+” hoặc “x” thường xuyên được sử dụng để biểu thị các phép toán nhóm, ngay cả khi các phần tử không phải là số. Trong những trường hợp này, bạn không nên hiểu những dấu này như là phép cộng hoặc nhân số học tiêu chuẩn. Thay vào đó, chúng là các phép toán chỉ có sự tương đồng trừu tượng với các phép toán số học này.

Trừ khi bạn cụ thể đề cập đến phép cộng hoặc nhân số học, thì dễ dàng hơn khi sử dụng các biểu tượng như ◌ và ◊ cho các phép toán nhóm, vì những biểu tượng này không có ý nghĩa văn hóa sâu đậm.

Thứ hai, cùng một lý do mà “+” và “x” thường được sử dụng để chỉ ra các phép toán không phải số học, các phần tử đồng nhất của nhóm thường được biểu thị bằng “0” và “1”, ngay cả khi các phần tử trong những nhóm này không phải là số. Trừ khi bạn đang đề cập đến phần tử đồng nhất của một nhóm có số, thì dễ dàng hơn khi sử dụng một biểu tượng trung lập hơn như “e” để chỉ phần tử đồng nhất.

Nhiều tập hợp giá trị khác nhau và rất quan trọng trong toán học được trang bị các phép toán nhị phân nhất định là nhóm. Tuy nhiên, các ứng dụng mật mã chỉ làm việc với tập hợp số nguyên hoặc ít nhất là các phần tử được mô tả bằng số nguyên, tức là trong lĩnh vực lý thuyết số. Do đó, các tập hợp với số thực khác với số nguyên không được sử dụng trong các ứng dụng mật mã.

Hãy kết thúc bằng cách cung cấp một ví dụ về các phần tử có thể được “mô tả bằng số nguyên”, mặc dù chúng không phải là số nguyên. Một ví dụ tốt là các điểm trên đường cong elliptic. Mặc dù bất kỳ điểm nào trên đường cong elliptic rõ ràng không phải là số nguyên, nhưng điểm đó thực sự được mô tả bởi hai số nguyên.

Đường cong elliptic, ví dụ, rất quan trọng đối với Bitcoin. Bất kỳ cặp khóa riêng và khóa công khai tiêu chuẩn nào của Bitcoin đều được chọn từ tập hợp các điểm được định nghĩa bởi đường cong elliptic sau: x<sup>3</sup> + 7 = y<sup>2</sup> mod 2<sup>256</sup> – 232 – 29 – 28 – 27 – 26 - 24 - 1 (số nguyên tố lớn nhất nhỏ hơn 2<sup>256</sup>). Tọa độ x là khóa riêng và tọa độ y là khóa công khai của bạn.
Giao dịch trong Bitcoin thường liên quan đến việc khóa đầu ra cho một hoặc nhiều khóa công khai theo một cách nào đó. Sau đó, giá trị từ những giao dịch này có thể được mở khóa bằng cách tạo chữ ký số với các khóa riêng tương ứng.

## Nhóm chu kỳ
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Một sự phân biệt quan trọng mà chúng ta có thể rút ra là giữa **nhóm hữu hạn** và **nhóm vô hạn**. Nhóm đầu tiên có một số lượng hữu hạn các phần tử, trong khi nhóm sau có một số lượng vô hạn các phần tử. Số lượng phần tử trong bất kỳ nhóm hữu hạn nào được biết đến là **bậc của nhóm**. Tất cả các ứng dụng mật mã thực tế liên quan đến việc sử dụng nhóm đều dựa trên nhóm hữu hạn (lý thuyết số).

Trong mật mã khóa công khai, một loại nhóm hữu hạn Abelian được biết đến là nhóm chu kỳ rất quan trọng. Để hiểu về nhóm chu kỳ, trước tiên chúng ta cần hiểu về khái niệm lũy thừa phần tử nhóm.

Giả sử một nhóm G với một phép toán nhóm ◌, và a là một phần tử của G. Biểu thức a<sup>n</sup> nên được hiểu là phần tử a kết hợp với chính nó tổng cộng n – 1 lần. Ví dụ, a<sup>2</sup> có nghĩa là a ◌ a, a<sup>3</sup> có nghĩa là a ◌ a ◌ a, và cứ thế. (Lưu ý rằng lũy thừa ở đây không nhất thiết là lũy thừa trong nghĩa số học tiêu chuẩn.)

Hãy xem xét một ví dụ. Giả sử G = 〈ℤ mod 7,+〉, và giá trị của chúng ta cho a bằng 4. Trong trường hợp này, a<sup>2</sup> = [4 + 4 mod 7] = [8 mod 7] = 1 mod 7. Ngược lại, a<sup>4</sup> sẽ đại diện cho [4 + 4 + 4 + 4 mod 7] = [16 mod 7] = 2 mod 7.

Một số nhóm Abelian có một hoặc nhiều phần tử, có thể tạo ra tất cả các phần tử nhóm khác thông qua việc lũy thừa liên tục. Những phần tử này được gọi là **bộ sinh** hoặc **phần tử nguyên thủy**.

Một loại nhóm quan trọng như vậy là 〈ℤ* mod N, •〉, nơi N là một số nguyên tố. Ký hiệu ℤ* ở đây có nghĩa là nhóm chứa tất cả các số nguyên dương không bằng không nhỏ hơn N. Do đó, một nhóm như vậy luôn có N – 1 phần tử.

Xem xét, ví dụ, G = 〈ℤ* mod 11, •〉. Nhóm này có các phần tử sau: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}. Bậc của nhóm này là 10 (đúng bằng 11 – 1).

Hãy khám phá việc lũy thừa phần tử 2 từ nhóm này. Các phép tính cho đến 2<sup>12</sup> được hiển thị dưới đây. Lưu ý rằng ở phía bên trái của phương trình, số mũ đề cập đến lũy thừa phần tử nhóm. Trong ví dụ cụ thể của chúng ta, điều này thực sự liên quan đến lũy thừa số học ở phía bên phải của phương trình (nhưng nó cũng có thể liên quan, ví dụ, đến phép cộng). Để làm rõ, tôi đã viết ra phép toán lặp lại, thay vì dạng số mũ ở phía bên phải.

* 2<sup>1</sup> = 2 mod 11 
* 2<sup>2</sup> = 2 · 2 mod 11 = 4 mod 11
* 2<sup>3</sup> = 2 · 2 · 2 mod 11 = 8 mod 11
* 2<sup>4</sup> = 2 · 2 · 2 · 2 mod 11 = 16 mod 11 = 5 mod 11
* 2<sup>5</sup> = 2 · 2 · 2 · 2 · 2 mod 11 = 32 mod 11 = 10 mod 11
* 2<sup>6</sup> = 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 64 mod 11 = 9 mod 11
* 2<sup>7</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 128 mod 11 = 7 mod 11
* 2<sup>8</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 256 mod 11 = 3 mod 11
* 2<sup>9</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 512 mod 11 = 6 mod 11
* 2<sup>10</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 1024 mod 11 = 1 mod 11
* 2<sup>11</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 2048 mod 11 = 2 mod 11
* 2<sup>12</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 4096 mod 11 = 4 mod 11

Nếu bạn quan sát kỹ, bạn có thể thấy rằng việc thực hiện phép lũy thừa với phần tử 2 lặp qua tất cả các phần tử của 〈ℤ* mod 11, •〉 theo thứ tự sau: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Sau 2<sup>10</sup>, việc tiếp tục lũy thừa phần tử 2 lặp lại tất cả các phần tử một lần nữa và theo cùng một thứ tự. Do đó, phần tử 2 là một sinh tử trong 〈ℤ* mod 11, •〉.

Mặc dù 〈ℤ* mod 11, •〉 có nhiều sinh tử, không phải tất cả các phần tử của nhóm này đều là sinh tử. Xem xét, ví dụ, phần tử 3. Thực hiện 10 phép lũy thừa đầu tiên, không hiển thị các phép tính phức tạp, cho kết quả sau:

* 3<sup>1</sup> = 3 mod 11
* 3<sup>2</sup> = 9 mod 11
* 3<sup>3</sup> = 5 mod 11
* 3<sup>4</sup> = 4 mod 11
* 3<sup>5</sup> = 1 mod 11
* 3<sup>6</sup> = 3 mod 11
* 3<sup>7</sup> = 9 mod 11
* 3<sup>8</sup> = 5 mod 11
* 3<sup>9</sup> = 4 mod 11
* 3<sup>10</sup> = 1 mod 11

Thay vì duyệt qua tất cả các giá trị trong 〈ℤ* mod 11, •〉, phép lũy thừa của phần tử 3 chỉ dẫn đến một tập hợp con của những giá trị đó: 3, 9, 5, 4, và 1. Sau lần lũy thừa thứ năm, những giá trị này bắt đầu lặp lại.

Chúng ta có thể định nghĩa một **nhóm tuần hoàn** là bất kỳ nhóm nào có ít nhất một phần tử sinh. Điều này có nghĩa là, có ít nhất một phần tử của nhóm từ đó bạn có thể tạo ra tất cả các phần tử khác của nhóm thông qua phép lũy thừa.

Bạn có thể đã nhận thấy trong ví dụ trên rằng cả 2<sup>10</sup> và 3<sup>10</sup> đều bằng 1 mod 11. Thực tế, mặc dù chúng ta sẽ không thực hiện các phép tính, việc lũy thừa bởi 10 của bất kỳ phần tử nào trong nhóm 〈ℤ* mod 11, •〉 đều cho kết quả là 1 mod 11. Tại sao lại như vậy?

Đây là một câu hỏi quan trọng, nhưng cần một số công việc để trả lời.

Để bắt đầu, giả sử hai số nguyên dương a và N. Một định lý quan trọng trong lý thuyết số khẳng định rằng a có một nghịch đảo nhân modulo N (tức là, một số nguyên b sao cho a • b = 1 mod N) nếu và chỉ nếu ước chung lớn nhất giữa a và N bằng 1. Điều này có nghĩa là, nếu a và N là hai số nguyên tố cùng nhau.

Vì vậy, đối với bất kỳ nhóm số nguyên nào được trang bị phép nhân modulo N chỉ bao gồm các số nguyên tố cùng nhau nhỏ hơn với N trong tập hợp. Chúng ta có thể ký hiệu tập hợp này bằng ℤ<sup>c</sup> mod N.

Ví dụ, giả sử N là 10. Chỉ có các số nguyên 1, 3, 7, và 9 là số nguyên tố cùng nhau với 10. Vì vậy, tập hợp ℤ<sup>c</sup> mod 10 chỉ bao gồm {1, 3, 7, 9}. Bạn không thể tạo ra một nhóm với phép nhân số nguyên modulo 10 sử dụng bất kỳ số nguyên nào khác giữa 1 và 10. Đối với nhóm cụ thể này, các cặp nghịch đảo là 1 và 9, và 3 và 7.

Trong trường hợp N chính là một số nguyên tố, tất cả các số nguyên từ 1 đến N – 1 đều là số nguyên tố cùng nhau với N. Như vậy, một nhóm như vậy, có một trật tự là N – 1. Sử dụng ký hiệu trước đó của chúng ta, ℤ<sup>c</sup> mod N bằng ℤ* mod N khi N là số nguyên tố. Nhóm mà chúng ta đã chọn cho ví dụ trước đó, 〈ℤ* mod 11, •〉, là một ví dụ cụ thể của lớp nhóm này.

Tiếp theo, hàm φ(N) tính số lượng số nguyên tố cùng nhau cho đến một số N, và được biết đến là **Hàm Phi của Euler**.<sup>[1](#footnote1)</sup> Theo **Định lý Euler**, bất cứ khi nào hai số nguyên a và N là số nguyên tố cùng nhau, điều sau đây được giữ:

* a<sup>φ(N)</sup> mod N = 1 mod N
Điều này có một hàm ý quan trọng đối với lớp các nhóm 〈ℤ* mod N, •〉 khi N là số nguyên tố. Đối với các nhóm này, phép lũy thừa của phần tử nhóm đại diện cho phép lũy thừa số học. Cụ thể, a<sup>φ(N)</sup> mod N đại diện cho phép toán số học a<sup>φ(N)</sup> mod N. Vì mọi phần tử a trong các nhóm nhân này đều nguyên tố cùng nhau với N, điều này có nghĩa là a<sup>φ(N)</sup> mod N = a<sup>N – 1</sup> mod N = 1 mod N.

Định lý Euler là một kết quả thực sự quan trọng. Đầu tiên, nó ngụ ý rằng tất cả các phần tử trong 〈ℤ* mod N, •〉 chỉ có thể lặp qua một số lượng giá trị bằng phép lũy thừa chia hết cho N – 1. Trong trường hợp của 〈ℤ* mod 11, •〉, điều này có nghĩa là mỗi phần tử chỉ có thể lặp qua 2, 5, hoặc 10 phần tử. Các giá trị nhóm mà bất kỳ phần tử nào lặp qua qua phép lũy thừa được biết đến là **bậc của phần tử**. Một phần tử có bậc tương đương với bậc của một nhóm là một sinh viên.

Hơn nữa, định lý Euler ngụ ý rằng chúng ta luôn biết kết quả của a<sup>N – 1</sup> mod N cho bất kỳ nhóm 〈ℤ* mod N, •〉 nào khi N là số nguyên tố. Điều này đúng bất kể các phép tính thực tế có thể phức tạp như thế nào.

Ví dụ, giả sử nhóm của chúng ta là ℤ* mod 160,481,182 (nơi 160,481,182 thực sự là một số nguyên tố). Chúng ta biết rằng tất cả các số nguyên từ 1 đến 160,481,181 phải là các phần tử của nhóm này, và rằng φ(n) = 160,481,181. Mặc dù chúng ta không thể thực hiện tất cả các bước trong các phép tính, chúng ta biết rằng các biểu thức như 514<sup>160,481,181</sup>, 2,005<sup>160,481,181</sup>, và 256,212<sup>160,481,181</sup> đều phải đánh giá là 1 mod 160,481,182.

## Fields
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Một nhóm là cấu trúc đại số cơ bản trong đại số trừu tượng, nhưng còn nhiều hơn nữa. Cấu trúc đại số duy nhất khác mà bạn cần quen thuộc là của một trường, cụ thể là của một trường hữu hạn. Loại cấu trúc đại số này thường được sử dụng trong mật mã học, chẳng hạn như trong Tiêu chuẩn Mã hóa Nâng cao. Đây là lược đồ mã hóa đối xứng chính mà bạn sẽ gặp trong thực tế.

Một trường được phát triển từ khái niệm của một nhóm. Cụ thể, một **trường** là một tập hợp các phần tử **S** được trang bị hai toán tử nhị phân ◌ và ◊, đáp ứng các điều kiện sau:

1. Tập hợp **S** được trang bị ◌ là một nhóm Abel.
2. Tập hợp **S** được trang bị ◊ là một nhóm Abel đối với các phần tử “không bằng không”.
3. Tập hợp **S** được trang bị hai toán tử đáp ứng điều kiện phân phối: Giả sử rằng a, b, và c là các phần tử của **S**. Sau đó **S** được trang bị hai toán tử đáp ứng tính chất phân phối khi a ◌ (b ◊ c) = a ◌ b ◊ a ◌ c.
Lưu ý rằng, giống như với các nhóm, định nghĩa của một trường là rất trừu tượng. Nó không đưa ra bất kỳ tuyên bố nào về các loại phần tử trong **S**, hoặc về các phép toán ◌ và ◊. Nó chỉ nêu rằng một trường là bất kỳ tập hợp các phần tử nào với hai phép toán mà ba điều kiện trên đây được thỏa mãn. (Phần tử “không” trong nhóm Abel thứ hai có thể được giải thích một cách trừu tượng.)

Vậy một ví dụ về trường có thể là gì? Một ví dụ tốt là tập hợp ℤ mod 7, hoặc {0,1,…,7} được định nghĩa trên phép cộng chuẩn (thay cho ◌ ở trên) và phép nhân chuẩn (thay cho ◊ ở trên).

Đầu tiên, ℤ mod 7 đáp ứng điều kiện để trở thành một nhóm Abel qua phép cộng, và nó đáp ứng điều kiện để trở thành một nhóm Abel qua phép nhân nếu bạn chỉ xem xét các phần tử không bằng không. Thứ hai, sự kết hợp của tập hợp với hai toán tử đáp ứng điều kiện phân phối.

Việc khám phá những tuyên bố này bằng cách sử dụng một số giá trị cụ thể là rất có giá trị về mặt giáo dục. Hãy lấy các giá trị thử nghiệm 5, 2, và 3, một số phần tử được chọn ngẫu nhiên từ tập hợp ℤ mod 7, để kiểm tra trường 〈ℤ mod 7, +, •〉. Chúng ta sẽ sử dụng ba giá trị này theo thứ tự, khi cần thiết để khám phá các điều kiện cụ thể.

Hãy khám phá xem ℤ mod 7 kết hợp với phép cộng có phải là một nhóm Abel hay không.

1. Điều kiện đóng: Hãy lấy 5 và 2 làm giá trị của chúng ta. Trong trường hợp đó, [5 + 2] mod 7 = 7 mod 7 = 0. Đây thực sự là một phần tử của ℤ mod 7, vì vậy kết quả phù hợp với điều kiện đóng.
2. Điều kiện kết hợp: Hãy lấy 5, 2, và 3 làm giá trị của chúng ta. Trong trường hợp đó, [(5 + 2) + 3] mod 7 = [5 + (2 + 3)] mod 7 = 10 mod 7 = 3. Điều này phù hợp với điều kiện kết hợp.
3. Điều kiện phần tử đồng nhất: Hãy lấy 5 làm giá trị của chúng ta. Trong trường hợp đó, [5 + 0] mod 7 = [0 + 5] mod 7 = 5. Vậy 0 có vẻ là phần tử đồng nhất cho phép cộng.
4. Điều kiện nghịch đảo: Xem xét nghịch đảo của 5. Cần phải có [5 + d] mod 7 = 0, cho một giá trị d nào đó. Trong trường hợp này, giá trị duy nhất từ ℤ mod 7 thỏa mãn điều kiện này là 2.
5. Điều kiện giao hoán: Hãy lấy 5 và 3 làm giá trị của chúng ta. Trong trường hợp đó, [5 + 3] mod 7 = [3 + 5] mod 7 = 1. Điều này phù hợp với điều kiện giao hoán.

Tập hợp ℤ mod 7 kết hợp với phép cộng rõ ràng xuất hiện là một nhóm Abel. Bây giờ hãy khám phá xem ℤ mod 7 kết hợp với phép nhân có phải là một nhóm Abel cho tất cả các phần tử không bằng không hay không.

1. Điều kiện đóng: Hãy lấy 5 và 2 làm giá trị của chúng ta. Trong trường hợp đó, [5 • 2] mod 7 = 10 mod 7 = 3. Đây cũng là một phần tử của ℤ mod 7, vì vậy kết quả phù hợp với điều kiện đóng.
2. Điều kiện kết hợp: Hãy lấy 5, 2 và 3 làm giá trị của chúng ta. Trong trường hợp đó, [(5 • 2) • 3] mod 7 = [5 • (2 • 3)] mod 7 = 30 mod 7 = 2. Điều này phù hợp với điều kiện kết hợp.
3. Điều kiện phần tử đơn vị: Hãy lấy 5 làm giá trị của chúng ta. Trong trường hợp đó, [5 • 1] mod 7 = [1 • 5] mod 7 = 5. Vậy 1 có vẻ là phần tử đơn vị cho phép nhân.
4. Điều kiện nghịch đảo: Xem xét nghịch đảo của 5. Cần phải có [5 • d] mod 7 = 1, với một giá trị nào đó của d. Giá trị duy nhất từ ℤ mod 7 thỏa mãn điều kiện này là 3. Điều này phù hợp với điều kiện nghịch đảo.
5. Điều kiện giao hoán: Hãy lấy 5 và 3 làm giá trị của chúng ta. Trong trường hợp đó, [5 • 3] mod 7 = [3 • 5] mod 7 = 15 mod 7 = 1. Điều này phù hợp với điều kiện giao hoán.

Tập hợp ℤ mod 7 rõ ràng dường như đáp ứng các quy tắc để trở thành một nhóm Abel khi kết hợp với phép cộng hoặc phép nhân trên các phần tử không bằng không.

Cuối cùng, tập hợp này kết hợp với cả hai toán tử dường như đáp ứng điều kiện phân phối. Hãy lấy 5, 2 và 3 làm giá trị của chúng ta. Chúng ta có thể thấy rằng [5 • (2 + 3)] mod 7 = [5 • 2 + 5 • 3] mod 7 = 25 mod 7 = 4.

Chúng ta đã thấy rằng ℤ mod 7 được trang bị phép cộng và phép nhân đáp ứng các tiên đề cho một trường hữu hạn khi kiểm tra với các giá trị cụ thể. Tất nhiên, chúng ta cũng có thể chứng minh điều này một cách tổng quát, nhưng sẽ không làm vậy ở đây.

Một điểm khác biệt quan trọng là giữa hai loại trường: trường hữu hạn và trường vô hạn.

Một **trường vô hạn** liên quan đến một trường mà tập hợp **S** là vô hạn lớn. Tập hợp các số thực ℝ được trang bị phép cộng và phép nhân là một ví dụ về trường vô hạn. Một **trường hữu hạn**, còn được biết đến là **trường Galois**, là một trường mà tập hợp **S** là hữu hạn. Ví dụ trên của chúng ta về 〈ℤ mod 7, +, •〉 là một trường hữu hạn.

Trong mật mã học, chúng ta quan tâm chủ yếu đến trường hữu hạn. Nói chung, có thể chứng minh rằng một trường hữu hạn tồn tại cho một tập hợp các phần tử **S** nếu và chỉ nếu nó có p<sup>m</sup> phần tử, nơi p là một số nguyên tố và m là một số nguyên dương lớn hơn hoặc bằng một. Nói cách khác, nếu thứ tự của một tập hợp **S** là một số nguyên tố (p<sup>m</sup> nơi m = 1) hoặc một lũy thừa của số nguyên tố (p<sup>m</sup> nơi m > 1), thì bạn có thể tìm thấy hai toán tử ◌ và ◊ sao cho các điều kiện cho một trường được thỏa mãn.

Nếu một trường hữu hạn có một số nguyên tố phần tử, thì nó được gọi là một **trường nguyên tố**. Nếu số lượng phần tử trong trường hữu hạn là một lũy thừa của số nguyên tố, thì trường đó được gọi là một **trường mở rộng**. Trong mật mã học, chúng ta quan tâm đến cả trường nguyên tố và trường mở rộng.
Các lĩnh vực chính quan tâm trong mật mã học là những lĩnh vực mà tập hợp tất cả các số nguyên được điều chỉnh bởi một số nguyên tố nào đó, và các phép toán là phép cộng và nhân tiêu chuẩn. Lớp trường hữu hạn này bao gồm ℤ mod 2, ℤ mod 3, ℤ mod 5, ℤ mod 7, ℤ mod 11, ℤ mod 13, và cứ thế tiếp tục. Đối với bất kỳ trường nguyên tố ℤ mod p nào, tập hợp các số nguyên của trường đó như sau: {0,1,….,p – 2, p – 1}.
Trong mật mã học, chúng ta cũng quan tâm đến các trường mở rộng, đặc biệt là bất kỳ trường nào có 2<sup>m</sup> phần tử với m > 1. Các trường hữu hạn như vậy, ví dụ, được sử dụng trong Mã Rijndael, làm nền tảng cho Tiêu chuẩn Mã hóa Nâng cao. Trong khi các trường nguyên tố tương đối trực quan, những trường mở rộng cơ sở 2 có lẽ không dành cho bất kỳ ai không quen với đại số trừu tượng.

Để bắt đầu, thực sự đúng là bất kỳ tập hợp số nguyên nào có 2<sup>m</sup> phần tử đều có thể được gán hai phép toán làm cho sự kết hợp của chúng trở thành một trường (miễn là m là một số nguyên dương). Tuy nhiên, chỉ vì một trường tồn tại không nhất thiết có nghĩa là nó dễ dàng được khám phá hoặc đặc biệt thực tiễn cho một số ứng dụng nhất định.

Hóa ra, các trường mở rộng đặc biệt áp dụng được trong mật mã học của 2<sup>m</sup> là những trường được định nghĩa trên các tập hợp biểu thức đa thức cụ thể, thay vì một số tập hợp số nguyên nào đó.

Ví dụ, giả sử chúng ta muốn một trường mở rộng với 2<sup>3</sup> (tức là, 8) phần tử trong tập hợp. Mặc dù có thể có nhiều tập hợp khác nhau có thể được sử dụng cho các trường có kích thước như vậy, một tập hợp như vậy bao gồm tất cả các đa thức duy nhất có dạng a<sub>2</sub>x<sup>2</sup> + a<sub>1</sub>x + a<sub>0</sub>, nơi mỗi hệ số a<sub>i</sub> là 0 hoặc 1. Do đó, tập hợp này **S** bao gồm các phần tử sau:

1. 0: Trường hợp a<sub>2</sub> = 0, a<sub>1</sub> = 0, và a<sub>0</sub> = 0.
2. 1: Trường hợp a<sub>2</sub> = 0, a<sub>1</sub> = 0, và a<sub>0</sub> = 1.
3. x: Trường hợp a<sub>2</sub> = 0, a<sub>1</sub> = 1, và a<sub>0</sub> = 0.
4. x + 1: Trường hợp a<sub>2</sub> = 0, a<sub>1</sub> = 1, và a<sub>0</sub> = 1.
5. x<sup>2</sup>: Trường hợp a<sub>2</sub>= 1, a<sub>1</sub> = 0, và a<sub>0</sub> = 0.
6. x<sup>2</sup> + 1: Trường hợp a<sub>2</sub> = 1, a<sub>1</sub> = 0, và a<sub>0</sub> = 1.
7. x<sup>2</sup> + x: Trường hợp a<sub>2</sub> = 1, a<sub>1</sub> = 1 và a<sub>0</sub> = 0. 8. x<sup>2</sup> + x + 1: Trường hợp a<sub>2</sub> = 1, a<sub>1</sub> = 1 và a<sub>0</sub> = 1.

Vậy **S** sẽ là tập hợp {0,1,x,x + 1, x<sup>2</sup>,x<sup>2</sup> + 1, x<sup>2</sup> + x, x<sup>2</sup> + x + 1}. Hai phép toán nào có thể được định nghĩa trên tập hợp các phần tử này để đảm bảo sự kết hợp của chúng tạo thành một trường?

Phép toán đầu tiên trên tập hợp S (◌) có thể được định nghĩa là phép cộng đa thức chuẩn modulo 2. Tất cả những gì bạn cần làm là cộng các đa thức như bạn thường làm, và sau đó áp dụng modulo 2 cho mỗi hệ số của đa thức kết quả. Dưới đây là một số ví dụ:

* [(x<sup>2</sup>) + (x<sup>2</sup> + x + 1)] mod 2 = [2x<sup>2</sup> + x + 1] mod 2 = x + 1
* [(x<sup>2</sup> + x) + (x)] mod 2 = [x<sup>2</sup> + 2x] mod 2 = x<sup>2</sup>
* [(x + 1) + (x<sup>2</sup> + x + 1)] mod 2 = [x<sup>2</sup> + 2x + 2] mod 2 = x<sup>2</sup> + 1

Phép toán thứ hai trên tập hợp S (◌) cần thiết để tạo ra trường là phức tạp hơn. Đó là một loại phép nhân, nhưng không phải là phép nhân chuẩn từ số học. Thay vào đó, bạn phải xem mỗi phần tử như một vector và hiểu phép toán này như là phép nhân của hai vector đó modulo một đa thức bất khả quy.

Hãy chuyển sang ý tưởng về một đa thức bất khả quy. Một **đa thức bất khả quy** là một đa thức không thể phân tích (giống như một số nguyên tố không thể phân tích thành các thành phần khác ngoài 1 và chính số nguyên tố đó). Đối với mục đích của chúng ta, chúng ta quan tâm đến các đa thức được coi là bất khả quy đối với tập hợp tất cả các số nguyên. (Lưu ý rằng bạn có thể phân tích một số đa thức bằng cách sử dụng, ví dụ, các số thực hoặc phức, ngay cả khi bạn không thể phân tích chúng sử dụng các số nguyên.)

Ví dụ, xem xét đa thức x<sup>2</sup> - 3x + 2. Điều này có thể được viết lại là (x – 1)(x – 2). Do đó, đây không phải là bất khả quy. Bây giờ xem xét đa thức x<sup>2</sup> + 1. Chỉ sử dụng các số nguyên, không có cách nào để phân tích thêm biểu thức này. Do đó, đây là một đa thức bất khả quy đối với các số nguyên.
Tiếp theo, chúng ta hãy xem xét khái niệm nhân vector. Chúng ta sẽ không khám phá sâu về chủ đề này, bạn chỉ cần hiểu một quy tắc cơ bản: Bất kỳ phép chia vector nào cũng có thể diễn ra miễn là bị chia có bậc cao hơn hoặc bằng với bậc của bội số. Nếu bị chia có bậc thấp hơn bội số, thì bị chia không thể được chia cho bội số nữa.

Ví dụ, xem xét biểu thức x<sup>6</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Rõ ràng, biểu thức này được giảm tiếp vì bậc của bị chia, 6, cao hơn bậc của bội số, 5. Bây giờ xem xét biểu thức x<sup>5</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Biểu thức này cũng được giảm tiếp, vì bậc của bị chia, 5, và bội số, 5, là bằng nhau.

Tuy nhiên, bây giờ xem xét biểu thức x<sup>4</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Biểu thức này không được giảm tiếp, vì bậc của bị chia, 4, thấp hơn bậc của bội số, 5.

Dựa trên thông tin này, chúng ta giờ đây đã sẵn sàng để tìm phép toán thứ hai cho tập hợp {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

Tôi đã nói rằng phép toán thứ hai này nên được hiểu là nhân vector modulo một đa thức bất khả quy. Đa thức bất khả quy này nên đảm bảo rằng phép toán thứ hai định nghĩa một nhóm Abel trên **S** và phù hợp với điều kiện phân phối. Vậy đa thức bất khả quy đó nên là gì?

Vì tất cả các vector trong tập hợp đều có bậc 2 hoặc thấp hơn, đa thức bất khả quy nên có bậc 3. Nếu bất kỳ phép nhân nào của hai vector trong tập hợp tạo ra một đa thức bậc 3 hoặc cao hơn, chúng ta biết rằng modulo một đa thức bậc 3 luôn tạo ra một đa thức bậc 2 hoặc thấp hơn. Điều này là do bất kỳ đa thức nào có bậc 3 hoặc cao hơn luôn có thể chia hết cho một đa thức bậc 3. Ngoài ra, đa thức đóng vai trò là bội số phải là bất khả quy.

Hóa ra có một số đa thức bất khả quy bậc 3 mà chúng ta có thể sử dụng làm bội số. Mỗi đa thức này định nghĩa một trường khác nhau kết hợp với tập hợp S của chúng ta và phép cộng modulo 2. Điều này có nghĩa là bạn có nhiều lựa chọn khi sử dụng trường mở rộng 2<sup>m</sup> trong mật mã học.

Đối với ví dụ của chúng ta, giả sử chúng ta chọn đa thức x<sup>3</sup> + x + 1. Đây thực sự là bất khả quy, bởi vì bạn không thể phân tích nó sử dụng số nguyên. Ngoài ra, nó sẽ đảm bảo rằng bất kỳ phép nhân nào của hai phần tử cũng sẽ tạo ra một đa thức bậc 2 hoặc ít hơn.
Hãy cùng xem xét một ví dụ về phép toán thứ hai sử dụng đa thức x<sup>3</sup> + x + 1 làm bộ chia để minh họa cách thức hoạt động của nó. Giả sử bạn nhân các phần tử x<sup>2</sup> + 1 với x<sup>2</sup> + x trong tập hợp **S** của chúng ta. Sau đó, chúng ta cần tính biểu thức [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1. Điều này có thể được đơn giản hóa như sau:
* [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 =
* [x<sup>2</sup> • x<sup>2</sup> + x<sup>2</sup> • x + 1 • x<sup>2</sup> + 1 • x] mod x<sup>3</sup> + x + 1 = 
* [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1
    
Chúng ta biết rằng [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1 có thể được giảm bớt vì bậc của số bị chia (4) cao hơn bộ chia (3).

Để bắt đầu, bạn có thể thấy rằng biểu thức x<sup>3</sup> + x + 1 đi vào x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x tổng cộng x lần. Bạn có thể xác minh điều này bằng cách nhân x<sup>3</sup> + x + 1 với x, tức là x<sup>4</sup> + x<sup>2</sup> + x. Vì thuật ngữ sau có cùng bậc với số bị chia, cụ thể là 4, chúng ta biết điều này khả thi. Bạn có thể tính phần dư của phép chia này bằng x như sau:

* [(x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x) – (x<sup>4</sup> + x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 = 
* [x<sup>3</sup>] mod x<sup>3</sup> + x + 1 =
* x<sup>3</sup>

Vậy sau khi chia x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x bằng x<sup>3</sup> + x + 1 tổng cộng x lần, chúng ta có một phần dư là x<sup>3</sup>. Liệu điều này có thể được chia thêm bởi x<sup>3</sup> + x + 1 không?
Một cách trực giác, có thể bạn sẽ nghĩ rằng x<sup>3</sup> không thể chia hết cho x<sup>3</sup> + x + 1, bởi vì hạng tử sau có vẻ lớn hơn. Tuy nhiên, hãy nhớ lại cuộc thảo luận của chúng ta về phép chia vector trước đây. Miễn là bị chia có bậc lớn hơn hoặc bằng bậc của số chia, biểu thức có thể được giảm thêm. Cụ thể, biểu thức x<sup>3</sup> + x + 1 có thể chia hết cho x<sup>3</sup> đúng 1 lần. Phần dư được tính như sau:
[(x<sup>3</sup>) – (x<sup>3</sup> + x + 1)] mod x<sup>3</sup> + x + 1 = 
[x + 1] mod x<sup>3</sup> + x + 1 = 
x + 1

Bạn có thể tự hỏi tại sao (x<sup>3</sup>) – (x<sup>3</sup> + x + 1) lại được đánh giá là x + 1 chứ không phải – x – 1. Hãy nhớ rằng, phép toán đầu tiên của trường của chúng ta được định nghĩa theo modulo 2. Do đó, phép trừ hai vector cho kết quả giống hệt như phép cộng hai vector.

Tóm lại việc nhân x<sup>2</sup> + 1 và x<sup>2</sup> + x: Khi bạn nhân hai hạng tử này, bạn nhận được một đa thức bậc 4, x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x, cần được giảm modulo x<sup>3</sup> + x + 1. Đa thức bậc 4 chia hết cho x<sup>3</sup> + x + 1 đúng x + 1 lần. Phần dư sau khi chia x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x cho x<sup>3</sup> + x + 1 đúng x + 1 lần là x + 1. Đây quả thực là một phần tử trong tập hợp của chúng ta {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

Tại sao các trường mở rộng với cơ sở 2 trên các tập hợp đa thức, như trong ví dụ trên, lại hữu ích cho mật mã học? Lý do là bạn có thể xem các hệ số trong các đa thức của những tập hợp này, hoặc là 0 hoặc là 1, như là các phần tử của chuỗi nhị phân với một độ dài cụ thể. Tập hợp **S** trong ví dụ trên của chúng ta, ví dụ, có thể được xem như là một tập hợp S bao gồm tất cả các chuỗi nhị phân có độ dài 3 (000 đến 111). Các phép toán trên **S**, do đó, cũng có thể được sử dụng để thực hiện các phép toán trên những chuỗi nhị phân này và tạo ra một chuỗi nhị phân có cùng độ dài.

## Đại số trừu tượng trong thực hành
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>
Mặc dù ngôn ngữ trang trọng và tính trừu tượng của cuộc thảo luận, khái niệm về nhóm không nên quá khó để nắm bắt. Đó chỉ là một tập hợp các phần tử cùng với một phép toán nhị phân, nơi thực hiện phép toán nhị phân đó trên những phần tử đó đáp ứng bốn điều kiện chung. Một nhóm Abelian chỉ có thêm một điều kiện được biết đến là tính giao hoán. Một nhóm tuần hoàn, lần lượt, là một loại nhóm Abelian đặc biệt, cụ thể là một nhóm có một sinh tử. Một trường chỉ đơn giản là một cấu trúc phức tạp hơn từ khái niệm nhóm cơ bản.

Nhưng nếu bạn là một người thực tế, bạn có thể tự hỏi vào lúc này: Ai quan tâm? Việc biết một tập hợp các phần tử với một toán tử là một nhóm, hoặc thậm chí là một nhóm Abelian hoặc nhóm tuần hoàn, có ý nghĩa gì trong thực tế không? Việc biết một cái gì đó là một trường có ý nghĩa gì không?

Mà không đi sâu vào quá nhiều chi tiết, câu trả lời là “có”. Nhóm được tạo ra lần đầu tiên vào thế kỷ 19 bởi nhà toán học người Pháp Evariste Galois. Ông đã sử dụng chúng để rút ra kết luận về việc giải các phương trình đa thức có bậc cao hơn năm.

Kể từ đó, khái niệm về nhóm đã giúp làm sáng tỏ một số vấn đề trong toán học và các lĩnh vực khác. Dựa trên cơ sở đó, ví dụ, nhà vật lý Murray-Gellman đã có thể dự đoán sự tồn tại của một hạt trước khi nó thực sự được quan sát trong thí nghiệm. Đối với một ví dụ khác, các nhà hóa học sử dụng lý thuyết nhóm để phân loại hình dạng của các phân tử. Các nhà toán học thậm chí đã sử dụng khái niệm về nhóm để rút ra kết luận về một cái gì đó cụ thể như giấy dán tường!

Cơ bản, việc chứng minh một tập hợp các phần tử với một toán tử là một nhóm, có nghĩa là những gì bạn đang mô tả có một loại đối xứng đặc biệt. Không phải đối xứng theo nghĩa thông thường của từ, mà ở một hình thức trừu tượng hơn. Và điều này có thể cung cấp cái nhìn sâu sắc đáng kể vào các hệ thống và vấn đề cụ thể. Các khái niệm phức tạp hơn từ đại số trừu tượng chỉ cho chúng ta thêm thông tin.

Quan trọng nhất, bạn sẽ thấy tầm quan trọng của các nhóm và trường lý thuyết số trong thực hành thông qua ứng dụng của chúng trong mật mã học, đặc biệt là mật mã học khóa công khai. Chúng ta đã thấy trong cuộc thảo luận về trường, ví dụ, cách mà các trường mở rộng được sử dụng trong Mã hóa Rijndael. Chúng ta sẽ làm việc với ví dụ đó trong *Chương 5*.

## Khám phá thêm
<chapterId>ab51038d-82bd-5c5d-a759-276cfbf7fbce</chapterId>

Để thảo luận thêm về đại số trừu tượng, tôi sẽ giới thiệu loạt video xuất sắc về đại số trừu tượng của Socratica. Tôi đặc biệt giới thiệu các video sau: “What is abstract algebra?”, “Group definition (expanded)”, “Ring definition (expanded)”, và “Field definition (expanded).” Bốn video này sẽ cung cấp cho bạn một số cái nhìn bổ sung vào phần lớn cuộc thảo luận ở trên. (Chúng tôi không thảo luận về các vòng, nhưng một trường chỉ đơn giản là một loại vòng đặc biệt.)

Để thảo luận thêm về lý thuyết số hiện đại, bạn có thể tham khảo nhiều cuộc thảo luận tiên tiến về mật mã học. Tôi sẽ đề xuất Jonathan Katz và Yehuda Lindell’s Introduction to Modern Cryptography hoặc Christof Paar và Jan Pelzl’s Understanding Cryptography để thảo luận thêm.
[^1]: Hàm hoạt động như sau. Bất kỳ số nguyên N nào cũng có thể được phân tích thành tích của các số nguyên tố. Giả sử rằng một N cụ thể được phân tích như sau: p<sub>1</sub><sup>e1</sup> • p<sub>2</sub><sup>e2</sup> …. • p<sub>m</sub><sup>em</sup> trong đó tất cả các p đều là số nguyên tố và tất cả các e đều là số nguyên lớn hơn hoặc bằng 1. Khi đó, φ(N) = Tổng<sub>i=1…m</sub>[p<sub>i</sub><sup>ei</sup> – p<sub>i</sub><sup>ei - 1</sup>] [^1].
[^2]: Các trường mở rộng trở nên rất phi trực giác. Thay vì có các phần tử là số nguyên, chúng có các tập hợp của đa thức. Ngoài ra, mọi phép toán được thực hiện modulo một đa thức bất khả quy [^2].

[^3]: Xem [Video YouTube](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be) [^3].

[^4]: Socratica, [Đại Số Trừu Tượng](https://www.socratica.com/subject/abstract-algebra) [^4].

[^5]: Katz và Lindell, *Giới Thiệu về Mật Mã Học Hiện Đại*, ấn bản thứ 2, 2015 (CRC Press: Boca Raton, FL). Paar và Pelzl, *Hiểu Biết về Mật Mã Học*, 2010 (Springer-Verlag: Berlin) [^5].


# Mật Mã Học Đối Xứng
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

Một trong hai nhánh chính của mật mã học là mật mã học đối xứng. Nó bao gồm các phương pháp mã hóa cũng như các phương pháp liên quan đến xác thực và toàn vẹn. Cho đến những năm 1970, toàn bộ mật mã học sẽ đã bao gồm các phương pháp mã hóa đối xứng.

Cuộc thảo luận chính bắt đầu bằng việc xem xét các phương pháp mã hóa đối xứng và làm rõ sự phân biệt quan trọng giữa mã hóa luồng và mã hóa khối. Sau đó, chúng ta chuyển sang mã xác thực tin nhắn, là các phương pháp để đảm bảo tính toàn vẹn và xác thực của tin nhắn. Cuối cùng, chúng ta khám phá cách kết hợp các phương pháp mã hóa đối xứng và mã xác thực tin nhắn để đảm bảo giao tiếp an toàn.

Chương này thảo luận qua loa về các phương pháp mật mã học đối xứng từ thực tiễn. Chương tiếp theo cung cấp một bài trình bày chi tiết về mã hóa với một mã hóa luồng và một mã hóa khối từ thực tiễn, cụ thể là RC4 và AES tương ứng.

Trước khi bắt đầu cuộc thảo luận về mật mã học đối xứng, tôi muốn nhanh chóng nhắc lại một số ý kiến về các minh họa Alice và Bob trong chương này và các chương tiếp theo.


## Alice và Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Trong việc minh họa các nguyên tắc của mật mã học, người ta thường dựa vào các ví dụ liên quan đến Alice và Bob. Tôi cũng sẽ làm như vậy.

Đặc biệt nếu bạn mới làm quen với mật mã học, điều quan trọng là phải nhận ra rằng những ví dụ về Alice và Bob chỉ nhằm mục đích minh họa các nguyên tắc và cấu trúc mật mã học trong một môi trường đơn giản. Tuy nhiên, các nguyên tắc và cấu trúc này có thể áp dụng cho một phạm vi rộng lớn các bối cảnh thực tế.

Dưới đây là năm điểm chính cần ghi nhớ về các ví dụ liên quan đến Alice và Bob trong mật mã học:

1. Chúng có thể dễ dàng được dịch thành các ví dụ với các loại diễn viên khác như các công ty hoặc tổ chức chính phủ.
2. Chúng có thể dễ dàng được mở rộng để bao gồm ba hoặc nhiều diễn viên hơn.
3. Trong các ví dụ, Bob và Alice thường là những người tham gia tích cực trong việc tạo ra từng thông điệp và áp dụng các phương pháp mật mã hóa lên thông điệp đó. Nhưng trên thực tế, giao tiếp điện tử phần lớn là tự động. Khi bạn truy cập một trang web sử dụng bảo mật lớp vận chuyển, ví dụ, việc mã hóa thường được xử lý hoàn toàn bởi máy tính của bạn và máy chủ web. 4. Trong bối cảnh của giao tiếp điện tử, "thông điệp" được gửi qua kênh giao tiếp thường là các gói TCP/IP. Chúng có thể thuộc về một email, một tin nhắn Facebook, một cuộc trò chuyện qua điện thoại, một lần chuyển file, một trang web, một bản tải lên phần mềm, và vân vân. Chúng không phải là thông điệp theo nghĩa truyền thống. Tuy nhiên, các nhà mật mã học thường đơn giản hóa thực tế này bằng cách nói rằng thông điệp, ví dụ, là một email.
5. Các ví dụ thường tập trung vào giao tiếp điện tử, nhưng chúng cũng có thể được mở rộng ra các hình thức giao tiếp truyền thống như thư từ.

## Các phương pháp mã hóa đối xứng
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Chúng ta có thể định nghĩa một cách lỏng lẻo **phương pháp mã hóa đối xứng** là bất kỳ phương pháp mật mã nào với ba thuật toán:

1. Một **thuật toán tạo khóa**, tạo ra một khóa riêng tư.
2. Một **thuật toán mã hóa**, lấy khóa riêng tư và một bản rõ làm đầu vào và xuất ra một bản mã.
3. Một **thuật toán giải mã**, lấy khóa riêng tư và bản mã làm đầu vào và xuất ra bản rõ gốc.

Thông thường, một phương pháp mã hóa—dù là đối xứng hay bất đối xứng—cung cấp một mẫu cho việc mã hóa dựa trên một thuật toán cốt lõi, chứ không phải là một thông số kỹ thuật chính xác.

Ví dụ, xem xét Salsa20, một phương pháp mã hóa đối xứng. Nó có thể được sử dụng với cả độ dài khóa 128 và 256 bit. Sự lựa chọn về độ dài khóa ảnh hưởng đến một số chi tiết nhỏ của thuật toán (số vòng trong thuật toán để chính xác).

Nhưng người ta sẽ không nói rằng sử dụng Salsa20 với khóa 128 bit là một phương pháp mã hóa khác so với Salsa20 với khóa 256 bit. Thuật toán cốt lõi vẫn giữ nguyên. Chỉ khi thuật toán cốt lõi thay đổi thì chúng ta mới thực sự nói về hai phương pháp mã hóa khác nhau.

Các phương pháp mã hóa đối xứng thường hữu ích trong hai loại trường hợp: (1) Những trường hợp mà hai hoặc nhiều đối tác giao tiếp từ xa và muốn giữ bí mật nội dung giao tiếp của họ; và (2) những trường hợp mà một đối tác muốn giữ bí mật nội dung của một thông điệp theo thời gian.

Bạn có thể thấy một hình ảnh về tình huống (1) trong *Hình 1* dưới đây. Bob muốn gửi một thông điệp M cho Alice từ xa, nhưng không muốn người khác có thể đọc được thông điệp đó.

Bob đầu tiên mã hóa thông điệp M với khóa riêng tư K. Sau đó, anh ấy gửi bản mã C cho Alice. Khi Alice nhận được bản mã, cô ấy có thể giải mã nó sử dụng khóa K và đọc bản rõ. Với một phương pháp mã hóa tốt, bất kỳ kẻ tấn công nào chặn được bản mã C cũng không nên có thể học được điều gì đáng kể về thông điệp M.

Bạn có thể thấy một hình ảnh về tình huống (2) trong *Hình 2* dưới đây. Bob muốn ngăn chặn người khác xem thông tin nhất định. Một tình huống điển hình có thể là Bob là một nhân viên lưu trữ dữ liệu nhạy cảm trên máy tính của mình, mà cả người ngoài lẫn đồng nghiệp không được phép đọc.
Bob mã hóa thông điệp M vào thời điểm T<sub>0</sub> bằng khóa K để tạo ra bản mã C. Vào thời điểm T<sub>1</sub>, anh ta cần thông điệp đó một lần nữa và giải mã bản mã C bằng khóa K. Bất kỳ kẻ tấn công nào có thể đã tìm thấy bản mã C trong thời gian đó không nên có khả năng suy luận bất cứ điều gì đáng kể về M từ nó.
*Hình 1: Bí mật qua không gian*

![Hình 1: Bí mật qua không gian](assets/Figure4-1.webp "Hình 1: Bí mật qua không gian")

*Hình 2: Bí mật qua thời gian*

![Hình 2: Bí mật qua thời gian](assets/Figure4-2.webp "Hình 2: Bí mật qua thời gian")

## Ví dụ: Mã Caesar
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Trong Chương 2, chúng ta đã gặp mã Caesar, là một ví dụ về một kế hoạch mã hóa đối xứng rất đơn giản. Hãy xem xét nó một lần nữa ở đây.

Giả sử một từ điển *D* tương đương tất cả các chữ cái của bảng chữ cái tiếng Anh, theo thứ tự, với tập hợp các số {0,1,2…,25}. Giả định một tập hợp các thông điệp có thể có **M**. Mã Caesar, vậy, là một kế hoạch mã hóa được định nghĩa như sau:

- Chọn ngẫu nhiên một khóa k từ tập hợp các khóa có thể có **K**, nơi **K** = {0,1,2,…,25}
- Mã hóa một thông điệp m є **M**, như sau:
    - Tách m thành từng chữ cái riêng lẻ m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Chuyển đổi mỗi m<sub>i</sub> thành một số theo *D*
    - Đối với mỗi m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Chuyển đổi mỗi c<sub>i</sub> thành một chữ cái theo *D*
    - Sau đó kết hợp c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub> để tạo ra bản mã c
- Giải mã một bản mã c như sau:
    - Chuyển đổi mỗi c<sub>i</sub> thành một số theo *D*
    - Đối với mỗi c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    - Chuyển đổi mỗi m<sub>i</sub> thành một chữ cái theo *D*
    - Sau đó kết hợp m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub> để tạo ra thông điệp gốc m

Điều làm cho mã Caesar trở thành một kế hoạch mã hóa đối xứng là cùng một khóa được sử dụng cho cả quá trình mã hóa và giải mã. Ví dụ, giả sử bạn muốn mã hóa thông điệp “DOG” sử dụng mã Caesar, và bạn đã chọn ngẫu nhiên "24" làm khóa. Mã hóa thông điệp với khóa này sẽ tạo ra “BME”. Cách duy nhất để lấy lại thông điệp gốc là sử dụng cùng một khóa, "24", cho quá trình giải mã.
Mã dịch Shift là một ví dụ của **mã thay thế đơn bảng chữ cái**: một phương pháp mã hóa mà bảng chữ cái mã hóa là cố định (nghĩa là, chỉ sử dụng một bảng chữ cái). Giả sử rằng thuật toán giải mã là xác định, mỗi ký tự trong bảng chữ cái thay thế có thể tối đa tương ứng với một ký tự trong bản rõ.

Cho đến thế kỷ 1700, nhiều ứng dụng của mã hóa dựa nhiều vào mã thay thế đơn bảng chữ cái, mặc dù thường chúng phức tạp hơn nhiều so với mã dịch Shift. Ví dụ, bạn có thể ngẫu nhiên chọn một chữ cái từ bảng chữ cái cho mỗi chữ cái văn bản gốc dưới ràng buộc rằng mỗi chữ cái chỉ xuất hiện một lần trong bảng chữ cái mã hóa. Điều này có nghĩa là bạn sẽ có 26 giai thừa khả năng khóa riêng, đó là một con số khổng lồ trong thời đại trước máy tính.

Lưu ý rằng bạn sẽ gặp thuật ngữ **cipher** rất nhiều trong mật mã học. Hãy nhận thức rằng thuật ngữ này có nhiều nghĩa khác nhau. Thực tế, tôi biết ít nhất năm nghĩa khác nhau của thuật ngữ này trong mật mã học.

Trong một số trường hợp, nó đề cập đến một phương pháp mã hóa, như trong mã dịch Shift và mã thay thế đơn bảng chữ cái. Tuy nhiên, thuật ngữ cũng có thể đề cập cụ thể đến thuật toán mã hóa, khóa riêng, hoặc chỉ là bản mã hóa của bất kỳ phương pháp mã hóa nào.

Cuối cùng, thuật ngữ cipher cũng có thể đề cập đến một thuật toán cốt lõi từ đó bạn có thể xây dựng các phương pháp mật mã. Những cái này có thể bao gồm các thuật toán mã hóa khác nhau, nhưng cũng bao gồm các loại phương pháp mật mã khác. Ý nghĩa của thuật ngữ này trở nên liên quan trong bối cảnh của mã khối (xem phần “Mã Khối” bên dưới).

Bạn cũng có thể gặp các thuật ngữ **encipher** hoặc **decipher**. Những thuật ngữ này chỉ đơn giản là từ đồng nghĩa cho việc mã hóa và giải mã.

## Các cuộc tấn công bằng phương pháp lực lượng brút và nguyên tắc Kerckhoff
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Mã dịch Shift là một phương pháp mã hóa đối xứng rất không an toàn, ít nhất là trong thế giới hiện đại.<sup>[1](#footnote1)</sup> Một kẻ tấn công chỉ cần thử giải mã bất kỳ bản mã hóa nào với tất cả 26 khóa có thể để xem kết quả nào có ý nghĩa. Loại tấn công này, nơi kẻ tấn công chỉ đơn giản là lặp qua các khóa để xem cái nào hoạt động, được biết đến là **tấn công bằng phương pháp lực lượng brút** hoặc **tìm kiếm khóa kiệt sức**.

Đối với bất kỳ phương pháp mã hóa nào để đáp ứng một khái niệm tối thiểu về bảo mật, nó phải có một tập hợp các khóa có thể, hay **không gian khóa**, lớn đến mức các cuộc tấn công bằng phương pháp lực lượng brút trở nên không khả thi. Tất cả các phương pháp mã hóa hiện đại đều đáp ứng tiêu chuẩn này. Điều này được biết đến là **nguyên tắc không gian khóa đủ lớn**. Một nguyên tắc tương tự thường được áp dụng trong các loại phương pháp mật mã khác nhau.

Để cảm nhận được kích thước không gian khóa khổng lồ trong các phương pháp mã hóa hiện đại, giả sử rằng một tệp đã được mã hóa bằng một khóa 128-bit sử dụng tiêu chuẩn mã hóa nâng cao. Điều này có nghĩa là một kẻ tấn công có một tập hợp 2<sup>128</sup> khóa mà cô ấy cần phải lặp qua để thực hiện một cuộc tấn công bằng phương pháp lực lượng brút. Một cơ hội thành công 0.78% với chiến lược này sẽ yêu cầu kẻ tấn công phải lặp qua khoảng 2.65 x 10<sup>36</sup> khóa.
Giả sử chúng ta lạc quan cho rằng một kẻ tấn công có thể thử nghiệm 10 nghìn tỷ khóa mỗi giây (tức là, 10<sup>16</sup> khóa mỗi giây). Để kiểm tra 0.78% tất cả các khóa trong không gian khóa, cuộc tấn công của họ sẽ phải kéo dài 2.65 x 10<sup>20</sup> giây. Điều này tương đương khoảng 8.4 nghìn tỷ năm. Vì vậy, ngay cả một cuộc tấn công bằng vũ lực mù quáng từ một đối thủ cực kỳ mạnh mẽ cũng không thực tế với một lược đồ mã hóa 128-bit hiện đại. Đây là nguyên tắc không gian khóa đủ lớn đang được áp dụng.

Liệu mã dịch chuyển có an toàn hơn nếu kẻ tấn công không biết thuật toán mã hóa? Có thể, nhưng không nhiều.

Dù sao đi nữa, mật mã học hiện đại luôn giả định rằng sự an toàn của bất kỳ lược đồ mã hóa đối xứng nào chỉ dựa vào việc giữ bí mật khóa riêng. Người tấn công luôn được giả định biết tất cả các chi tiết khác, bao gồm không gian tin nhắn, không gian khóa, không gian văn bản mã hóa, thuật toán chọn khóa, thuật toán mã hóa và thuật toán giải mã.

Ý tưởng rằng sự an toàn của một lược đồ mã hóa đối xứng chỉ có thể dựa vào sự bí mật của khóa riêng được biết đến như là **nguyên tắc Kerckhoffs**.

Như Kerckhoffs đã ban đầu ý định, nguyên tắc này chỉ áp dụng cho các lược đồ mã hóa đối xứng. Tuy nhiên, một phiên bản tổng quát hơn của nguyên tắc này cũng áp dụng cho tất cả các loại lược đồ mật mã hiện đại khác: Thiết kế của bất kỳ lược đồ mật mã nào không được yêu cầu phải giữ bí mật để đảm bảo an toàn; sự bí mật chỉ có thể mở rộng đến một số chuỗi thông tin, thường là một khóa riêng.

Nguyên tắc Kerckhoffs là trung tâm của mật mã học hiện đại vì bốn lý do.<sup>[2](#footnote2)</sup> Đầu tiên, chỉ có một số lượng hạn chế các lược đồ mật mã cho các loại ứng dụng cụ thể. Ví dụ, hầu hết các ứng dụng mã hóa đối xứng hiện đại sử dụng mã Rijndael. Vì vậy, sự bí mật về thiết kế của một lược đồ chỉ rất hạn chế. Tuy nhiên, có nhiều linh hoạt hơn trong việc giữ bí mật một số khóa riêng cho mã Rijndael.

Thứ hai, việc thay thế một chuỗi thông tin dễ dàng hơn nhiều so với việc thay thế toàn bộ lược đồ mật mã. Giả sử rằng tất cả nhân viên của một công ty đều sử dụng cùng một phần mềm mã hóa, và mỗi hai nhân viên có một khóa riêng để giao tiếp mật. Việc khóa bị lộ là một rắc rối trong tình huống này, nhưng ít nhất công ty có thể giữ phần mềm với những lỗ hổng bảo mật như vậy. Nếu công ty dựa vào sự bí mật của lược đồ, thì bất kỳ sự lộ bí mật nào cũng đòi hỏi phải thay thế tất cả phần mềm.

Thứ ba, nguyên tắc Kerckhoffs cho phép tiêu chuẩn hóa và tương thích giữa người dùng của các lược đồ mật mã. Điều này mang lại lợi ích to lớn về hiệu quả. Ví dụ, rất khó để tưởng tượng hàng triệu người có thể kết nối an toàn với máy chủ web của Google mỗi ngày, nếu sự an toàn đó đòi hỏi phải giữ bí mật các lược đồ mật mã.

Thứ tư, nguyên tắc Kerckhoff cho phép sự giám sát công khai của các lược đồ mật mã. Loại giám sát này là hoàn toàn cần thiết để đạt được các lược đồ mật mã an toàn. Một cách minh họa, thuật toán chính trong mật mã đối xứng, mã Rijndael, là kết quả của một cuộc thi do Viện Tiêu chuẩn và Công nghệ Quốc gia tổ chức từ năm 1997 đến 2000.

Bất kỳ hệ thống nào cố gắng đạt được **an toàn bằng sự mơ hồ** là một hệ thống dựa vào việc giữ bí mật các chi tiết thiết kế và/hoặc triển khai của nó. Trong mật mã, đây cụ thể là một hệ thống dựa vào việc giữ bí mật các chi tiết thiết kế của lược đồ mật mã. Vì vậy, an toàn bằng sự mơ hồ trái ngược trực tiếp với nguyên tắc Kerckhoffs.
Khả năng mở cửa để tăng cường chất lượng và an ninh cũng được mở rộng rộng lớn hơn trong thế giới số so với chỉ là mã hóa. Các bản phân phối Linux mã nguồn mở và miễn phí như Debian, ví dụ, thường có nhiều ưu điểm hơn so với các đối thủ Windows và MacOS về quyền riêng tư, ổn định, an ninh và linh hoạt. Mặc dù có thể có nhiều nguyên nhân, nhưng nguyên tắc quan trọng nhất có lẽ, như Eric Raymond đã diễn đạt trong bài luận nổi tiếng của mình "The Cathedral and the Bazaar," là "[g]iven enough eyeballs, all bugs are shallow.”<sup>[3](#footnote3)</sup> Đó là nguyên tắc trí tuệ của đám đông đã mang lại thành công lớn nhất cho Linux.
Không bao giờ có thể khẳng định một cách không mơ hồ rằng một lược đồ mã hóa là "an toàn" hay "không an toàn." Thay vào đó, có các khái niệm khác nhau về an ninh cho các lược đồ mã hóa. Mỗi **định nghĩa về an ninh mã hóa** phải chỉ rõ (1) mục tiêu an ninh, cũng như (2) khả năng của kẻ tấn công. Phân tích các lược đồ mã hóa dựa trên một hoặc nhiều khái niệm cụ thể về an ninh cung cấp cái nhìn sâu sắc vào ứng dụng và giới hạn của chúng.

Mặc dù chúng ta sẽ không đi sâu vào tất cả các chi tiết của các khái niệm an ninh mã hóa khác nhau, bạn nên biết rằng hai giả định là phổ biến với tất cả các khái niệm an ninh mã hóa hiện đại liên quan đến các lược đồ đối xứng và bất đối xứng (và dưới một hình thức nào đó đối với các nguyên tắc mã hóa khác):

* Kiến thức của kẻ tấn công về lược đồ tuân theo nguyên tắc Kerckhoffs.
* Kẻ tấn công không thể thực hiện một cuộc tấn công bằng lực lượng mù một cách khả thi. Cụ thể, các mô hình đe dọa của các khái niệm an ninh mã hóa thường không cho phép các cuộc tấn công bằng lực lượng mù, vì chúng giả định rằng những điều này không phải là một xem xét liên quan.

## Mã hóa luồng
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Các lược đồ mã hóa đối xứng thường được chia thành hai loại: mã hóa luồng và mã hóa khối. Tuy nhiên, sự phân biệt này có phần rắc rối, vì mọi người sử dụng các thuật ngữ này một cách không nhất quán. Trong vài phần tiếp theo, tôi sẽ trình bày sự phân biệt theo cách tôi cho là tốt nhất. Tuy nhiên, bạn nên biết rằng nhiều người sẽ sử dụng các thuật ngữ này một cách khác biệt so với cách tôi trình bày.

Hãy đầu tiên xem xét mã hóa luồng. Một **mã hóa luồng** là một lược đồ mã hóa đối xứng nơi mã hóa bao gồm hai bước.

Đầu tiên, một chuỗi có độ dài bằng với bản rõ được tạo ra thông qua một khóa riêng. Chuỗi này được gọi là **keystream**.

Tiếp theo, keystream được kết hợp toán học với bản rõ để tạo ra bản mã. Sự kết hợp này thường là một hoạt động XOR. Để giải mã, bạn chỉ cần đảo ngược hoạt động. (Lưu ý rằng A XOR B = B XOR A, trong trường hợp A và B là chuỗi bit. Vì vậy, thứ tự của một hoạt động XOR trong một mã hóa luồng không ảnh hưởng đến kết quả. Tính chất này được biết đến là tính giao hoán.)

Một mã hóa luồng XOR điển hình được mô tả trong *Hình 3*. Bạn đầu tiên lấy một khóa riêng K và sử dụng nó để tạo ra một keystream. Keystream, sau đó, được kết hợp với bản rõ thông qua một hoạt động XOR để tạo ra bản mã. Bất kỳ đại lý nào nhận được bản mã có thể dễ dàng giải mã nó nếu họ có khóa K. Tất cả những gì cô ấy cần làm là tạo ra một keystream dài bằng với bản mã theo quy trình đã được chỉ định của lược đồ và XOR nó với bản mã.

*Hình 3: Một mã hóa luồng XOR*

![Hình 3: Một mã hóa luồng XOR](assets/Figure4-3.webp "Hình 3: Một mã hóa luồng XOR")
Hãy nhớ rằng, một phương pháp mã hóa thường là một khuôn mẫu cho việc mã hóa với cùng một thuật toán cốt lõi, chứ không phải là một đặc tả chính xác. Theo đó, một mã hóa dòng (stream cipher) thường là một khuôn mẫu cho việc mã hóa trong đó bạn có thể sử dụng các khóa với độ dài khác nhau. Mặc dù độ dài khóa có thể ảnh hưởng đến một số chi tiết nhỏ của phương pháp, nhưng nó sẽ không ảnh hưởng đến hình thức cơ bản của nó.

Mã hóa dịch chuyển (shift cipher) là ví dụ về một mã hóa dòng đơn giản và không an toàn. Sử dụng một chữ cái đơn lẻ (khóa riêng tư), bạn có thể tạo ra một chuỗi các chữ cái có độ dài bằng với thông điệp (dòng khóa). Sau đó, dòng khóa này được kết hợp với văn bản gốc thông qua một phép toán modulo để tạo ra một văn bản mã hóa. (Phép toán modulo này có thể được đơn giản hóa thành một phép toán XOR khi biểu diễn các chữ cái dưới dạng bit).

Một ví dụ nổi tiếng khác về mã hóa dòng là **Mã Vigenere**, được phát triển hoàn chỉnh bởi Blaise de Vigenere vào cuối thế kỷ 16 (mặc dù đã có nhiều công trình nghiên cứu trước đó). Đây là ví dụ về một **mã thay thế đa bảng chữ cái**: một phương pháp mã hóa nơi bảng chữ cái mã hóa cho một ký tự văn bản gốc thay đổi tùy thuộc vào vị trí của nó trong văn bản. Trái ngược với mã thay thế đơn bảng chữ cái, các ký tự mã hóa có thể được liên kết với nhiều hơn một ký tự văn bản gốc.

Khi mã hóa trở nên phổ biến ở châu Âu thời Phục Hưng, **phân tích mã hóa**—tức là, việc phá vỡ các văn bản mã hóa—cũng trở nên phổ biến, đặc biệt là sử dụng **phân tích tần suất**. Phương pháp này sử dụng các quy luật thống kê trong ngôn ngữ của chúng ta để phá vỡ các văn bản mã hóa, và đã được các học giả Ả Rập phát hiện ra từ thế kỷ thứ chín. Đây là một kỹ thuật hoạt động đặc biệt hiệu quả với các văn bản dài. Và ngay cả những mã thay thế đơn bảng chữ cái tinh vi nhất cũng không còn đủ để chống lại phân tích tần suất vào thế kỷ 18 ở châu Âu, đặc biệt trong các cài đặt quân sự và an ninh. Khi Mã Vigenere cung cấp một bước tiến đáng kể về mặt an ninh, nó trở nên phổ biến trong thời kỳ này và được phổ biến rộng rãi vào cuối thế kỷ 18.

Nói một cách không chính thức, phương pháp mã hóa hoạt động như sau:

1.	Chọn một từ có nhiều chữ cái làm khóa riêng tư
2.	Với bất kỳ thông điệp nào, áp dụng mã hóa dịch chuyển cho mỗi chữ cái của thông điệp sử dụng chữ cái tương ứng trong từ khóa làm dịch chuyển
3.	Nếu bạn đã lặp qua từ khóa nhưng vẫn chưa mã hóa hoàn toàn văn bản gốc, lại áp dụng các chữ cái của từ khóa như một mã hóa dịch chuyển cho các chữ cái tương ứng trong phần còn lại của văn bản
4.	Tiếp tục quá trình này cho đến khi toàn bộ thông điệp được mã hóa

Để minh họa, giả sử khóa riêng tư của bạn là GOLD và bạn muốn mã hóa thông điệp "CRYPTOGRAPHY". Trong trường hợp đó, bạn sẽ tiến hành như sau theo Mã Vigenere:

- c<sub>0</sub>  = [(2 + 6) Mod 26] = 8 = I
- c<sub>1</sub>  = [(17 + 14) Mod 26] = 5 = F
- c<sub>2</sub>  = [(24 + 11) Mod 26] = 9 = J
- c<sub>3</sub>  = [(15 + 3) Mod 26] = 18 = S
- c<sub>4</sub>  = [(19 + 6) Mod 26] = 25 = Z
- c<sub>5</sub>  = [(14 + 14) Mod 26] = 2 = C
- c<sub>6</sub>  = [(6 + 11) Mod 26] = 17 = R
- c<sub>7</sub> = [(17 + 3) Mod 26] = 20 = U
- c<sub>8</sub> = [(0 + 6) Mod 26] = 6 = G
- c<sub>9</sub> = [(15 + 14) Mod 26] = 3 = D
- c<sub>10</sub> = [(7 + 11) Mod 26] = 18 = S
- c<sub>11</sub> = [(24 + 3) Mod 26] = 1 = B
- c = "IFJSZCRUGDSB"

Một ví dụ nổi tiếng khác về mật mã luồng là **mật mã một lần** (one-time pad). Với mật mã một lần, bạn chỉ cần tạo một chuỗi bit ngẫu nhiên có độ dài bằng với thông điệp bản rõ và tạo ra bản mã thông qua phép toán XOR. Do đó, khóa riêng và dòng khóa trong mật mã một lần là tương đương nhau.

Trong khi mật mã dịch và mật mã Vigenere rất không an toàn trong thời đại hiện đại, mật mã một lần lại rất an toàn nếu được sử dụng đúng cách. Có lẽ ứng dụng nổi tiếng nhất của mật mã một lần, ít nhất là cho đến những năm 1980, là cho **đường dây nóng Washington-Moscow**.

Đường dây nóng là một liên kết truyền thông trực tiếp giữa Washington và Moscow cho các vấn đề khẩn cấp, được lắp đặt sau cuộc khủng hoảng tên lửa Cuba. Công nghệ cho đường dây nóng đã biến đổi qua nhiều năm. Hiện nay, nó bao gồm một cáp quang trực tiếp cũng như hai liên kết vệ tinh (để dự phòng), cho phép gửi email và tin nhắn văn bản. Liên kết kết thúc ở nhiều nơi tại Mỹ. Lầu Năm Góc, Nhà Trắng và Núi Raven Rock là những điểm cuối được biết đến. Trái với ý kiến phổ biến, đường dây nóng chưa bao giờ sử dụng điện thoại.

Bản chất của kế hoạch mật mã một lần hoạt động như sau. Cả Washington và Moscow sẽ có hai bộ số ngẫu nhiên. Một bộ số ngẫu nhiên, được tạo ra bởi người Nga, liên quan đến việc mã hóa và giải mã bất kỳ thông điệp nào bằng tiếng Nga. Một bộ số ngẫu nhiên, được tạo ra bởi người Mỹ, liên quan đến việc mã hóa và giải mã bất kỳ thông điệp nào bằng tiếng Anh. Thỉnh thoảng, thêm số ngẫu nhiên sẽ được giao cho phía bên kia bởi những sứ giả đáng tin cậy.

Washington và Moscow, sau đó, có thể giao tiếp một cách bí mật bằng cách sử dụng những số ngẫu nhiên này để tạo ra mật mã một lần. Mỗi khi bạn cần giao tiếp, bạn sẽ sử dụng phần tiếp theo của số ngẫu nhiên cho thông điệp của mình.

Mặc dù rất an toàn, mật mã một lần đối mặt với những hạn chế thực tế đáng kể: khóa cần phải dài bằng thông điệp và không một phần nào của mật mã một lần có thể được tái sử dụng. Điều này có nghĩa là bạn cần phải theo dõi vị trí của mình trong mật mã một lần, lưu trữ một lượng lớn bit và trao đổi bit ngẫu nhiên với các bên liên quan từ thời gian này sang thời gian khác. Do đó, mật mã một lần không thường xuyên được sử dụng trong thực tế.

Thay vào đó, các mật mã luồng giả ngẫu nhiên thường được sử dụng trong thực tế. Salsa20 và một biến thể gần gũi được gọi là ChaCha là những ví dụ về các mật mã luồng giả ngẫu nhiên thường được sử dụng.

Với những mật mã luồng giả ngẫu nhiên này, bạn đầu tiên chọn ngẫu nhiên một khóa K ngắn hơn độ dài của thông điệp bản rõ. Một khóa ngẫu nhiên K như vậy thường được máy tính của chúng ta tạo ra dựa trên dữ liệu không dự đoán trước được mà nó thu thập được theo thời gian, như thời gian giữa các tin nhắn mạng, chuyển động của chuột, và vân vân.
Khóa ngẫu nhiên K sau đó được chèn vào một thuật toán mở rộng, tạo ra một dòng khóa giả ngẫu nhiên dài bằng thông điệp. Bạn có thể xác định chính xác độ dài của dòng khóa cần thiết (ví dụ, 500 bit, 1000 bit, 1200 bit, 29,117 bit, v.v.). Một dòng khóa giả ngẫu nhiên xuất hiện *như thể* nó được chọn hoàn toàn ngẫu nhiên từ tập hợp tất cả các chuỗi có cùng độ dài. Do đó, việc mã hóa với một dòng khóa giả ngẫu nhiên xuất hiện như thể nó đã được thực hiện với một bảng mã một lần. Nhưng đó, tất nhiên, không phải là trường hợp.

Vì khóa riêng của chúng ta ngắn hơn dòng khóa và thuật toán mở rộng của chúng ta cần phải là xác định để quá trình mã hóa/giải mã hoạt động, không phải mọi dòng khóa có độ dài cụ thể đó có thể được tạo ra như một đầu ra từ hoạt động mở rộng của chúng ta.

Giả sử, ví dụ, khóa riêng của chúng ta có độ dài 128 bit và chúng ta có thể chèn nó vào một thuật toán mở rộng để tạo ra một dòng khóa dài hơn nhiều, giả sử 2,500 bit. Vì thuật toán mở rộng của chúng ta cần phải là xác định, thuật toán của chúng ta tối đa chỉ có thể chọn 1/2<sup>128</sup> chuỗi với độ dài 2,500 bit. Vì vậy, một dòng khóa như vậy không bao giờ có thể được chọn hoàn toàn ngẫu nhiên từ tất cả các chuỗi cùng độ dài.

Định nghĩa của chúng ta về một mật mã dòng có hai khía cạnh: (1) một dòng khóa dài bằng văn bản gốc được tạo ra với sự giúp đỡ của một khóa riêng; và (2) dòng khóa này được kết hợp với văn bản gốc, thường qua một hoạt động XOR, để tạo ra văn bản mã hóa.

Đôi khi người ta định nghĩa điều kiện (1) một cách chặt chẽ hơn, bằng cách khẳng định rằng dòng khóa cụ thể phải là giả ngẫu nhiên. Điều này có nghĩa là cả mật mã dịch chuyển lẫn bảng mã một lần sẽ không được coi là mật mã dòng.

Theo quan điểm của tôi, việc định nghĩa điều kiện (1) một cách rộng rãi hơn cung cấp một cách dễ dàng hơn để tổ chức các kế hoạch mã hóa. Ngoài ra, nó có nghĩa là chúng ta không phải ngừng gọi một kế hoạch mã hóa cụ thể là mật mã dòng chỉ vì chúng ta biết rằng nó thực sự không dựa vào dòng khóa giả ngẫu nhiên.

## Mật mã khối
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Cách đầu tiên mà một **mật mã khối** thường được hiểu là như một cái gì đó nguyên thủy hơn mật mã dòng: Một thuật toán cốt lõi thực hiện một biến đổi bảo toàn độ dài trên một chuỗi có độ dài phù hợp với sự giúp đỡ của một khóa. Thuật toán này có thể được sử dụng để tạo ra các kế hoạch mã hóa và có thể là các loại kế hoạch mật mã khác.

Thường xuyên, một mật mã khối có thể nhận đầu vào là các chuỗi có độ dài khác nhau như 64, 128, hoặc 256 bit, cũng như các khóa có độ dài khác nhau như 128, 192, hoặc 256 bit. Mặc dù một số chi tiết của thuật toán có thể thay đổi tùy thuộc vào các biến số này, thuật toán cốt lõi không thay đổi. Nếu nó thay đổi, chúng ta sẽ nói về hai mật mã khối khác nhau. Lưu ý rằng việc sử dụng thuật ngữ thuật toán cốt lõi ở đây giống như đối với các kế hoạch mã hóa.

Một miêu tả về cách một mật mã khối hoạt động có thể được thấy trong *Hình 4* dưới đây. Một thông điệp M có độ dài L và một khóa K phục vụ như là đầu vào cho Mật mã khối. Nó xuất ra một thông điệp M’ có độ dài L. Khóa không nhất thiết cần phải có cùng độ dài với M và M’ đối với hầu hết các mật mã khối.

*Hình 4: Một mật mã khối*

![Hình 4: Một mật mã khối](assets/Figure4-4.webp "Hình 4: Một mật mã khối")
Một thuật toán mã hóa khối một mình không phải là một phương thức mã hóa. Tuy nhiên, một thuật toán mã hóa khối có thể được sử dụng với các **chế độ hoạt động** khác nhau để tạo ra các phương thức mã hóa khác nhau. Chế độ hoạt động chỉ đơn giản là thêm một số thao tác bổ sung bên ngoài thuật toán mã hóa khối.

Để minh họa cách thức này hoạt động, giả sử một thuật toán mã hóa khối (BC) yêu cầu một chuỗi đầu vào 128-bit và một khóa riêng tư 128-bit. Hình 5 dưới đây hiển thị cách thuật toán mã hóa khối đó có thể được sử dụng với **chế độ sách mã điện tử** (**ECB mode**) để tạo ra một phương thức mã hóa. (Các dấu chấm lửng bên phải chỉ ra rằng bạn có thể lặp lại mẫu này theo nhu cầu).

*Hình 5: Một thuật toán mã hóa khối với chế độ ECB*

![Hình 5: Một thuật toán mã hóa khối với chế độ ECB](assets/Figure4-5.webp "Hình 5: Một thuật toán mã hóa khối với chế độ ECB")

Quy trình mã hóa sách mã điện tử với thuật toán mã hóa khối như sau. Xem bạn có thể chia thông điệp văn bản gốc của mình thành các khối 128-bit không. Nếu không, thêm **đệm** vào thông điệp, sao cho kết quả có thể được chia đều theo kích thước khối 128 bit. Đây là dữ liệu của bạn được sử dụng cho quá trình mã hóa.

Bây giờ, chia dữ liệu thành các chuỗi 128-bit (M<sub>1</sub>, M<sub>2</sub>, M<sub>3</sub>, và tiếp theo). Chạy từng chuỗi 128-bit qua thuật toán mã hóa khối với khóa 128-bit của bạn để tạo ra các khối mã hóa 128-bit (C<sub>1</sub>, C<sub>2</sub>, C<sub>3</sub>, và tiếp theo). Những khối này khi kết hợp lại tạo thành mã hóa đầy đủ.

Giải mã chỉ là quá trình đảo ngược, mặc dù người nhận cần có một cách nhận biết để loại bỏ bất kỳ đệm nào từ dữ liệu đã giải mã để tạo ra thông điệp văn bản gốc.

Mặc dù tương đối đơn giản, một thuật toán mã hóa khối với chế độ sách mã điện tử thiếu an toàn. Điều này là do nó dẫn đến **mã hóa xác định**. Bất kỳ hai chuỗi dữ liệu 128-bit giống hệt nhau đều được mã hóa chính xác theo cùng một cách. Thông tin đó có thể bị khai thác.

Thay vào đó, bất kỳ phương thức mã hóa nào được xây dựng từ một thuật toán mã hóa khối nên là **xác suất**: tức là, việc mã hóa bất kỳ thông điệp M nào, hoặc bất kỳ phần cụ thể nào của M, nên chung quy tạo ra một kết quả khác nhau mỗi lần.<sup>[5](#footnote5)</sup>

**Chế độ chuỗi khối mã hóa** (**CBC mode**) có lẽ là chế độ phổ biến nhất được sử dụng với một thuật toán mã hóa khối. Sự kết hợp, nếu thực hiện đúng, tạo ra một phương thức mã hóa xác suất. Bạn có thể thấy một hình ảnh về chế độ hoạt động này trong Hình 6 dưới đây.

*Hình 6: Một thuật toán mã hóa khối với chế độ CBC*

![Hình 6: Một thuật toán mã hóa khối với chế độ CBC](assets/Figure4-6.webp "Hình 6: Một thuật toán mã hóa khối với chế độ CBC")

Giả sử kích thước khối lại là 128 bit. Vì vậy, để bắt đầu, bạn lại cần đảm bảo rằng thông điệp văn bản gốc của bạn nhận được đệm cần thiết.

Sau đó, bạn XOR phần 128-bit đầu tiên của thông điệp văn bản gốc với một **vector khởi tạo** 128-bit. Kết quả được đặt vào thuật toán mã hóa khối để tạo ra mã hóa cho khối đầu tiên. Đối với khối thứ hai 128 bit, bạn trước tiên XOR văn bản gốc với mã hóa từ khối đầu tiên, trước khi đưa nó vào thuật toán mã hóa khối. Bạn tiếp tục quá trình này cho đến khi bạn đã mã hóa toàn bộ thông điệp văn bản gốc.

Khi hoàn thành, bạn gửi thông điệp đã mã hóa cùng với vector khởi tạo không mã hóa cho người nhận. Người nhận cần biết vector khởi tạo, nếu không cô ấy không thể giải mã mã hóa.
Kiến trúc này an toàn hơn nhiều so với chế độ mã hóa sổ mã điện tử khi được sử dụng đúng cách. Đầu tiên, bạn cần đảm bảo rằng vector khởi tạo là một chuỗi ngẫu nhiên hoặc giả ngẫu nhiên. Ngoài ra, bạn nên sử dụng một vector khởi tạo khác nhau mỗi lần bạn sử dụng phương thức mã hóa này.
Nói cách khác, vector khởi tạo của bạn nên là một nonce ngẫu nhiên hoặc giả ngẫu nhiên, nơi mà **nonce** có nghĩa là "một số chỉ được sử dụng một lần." Nếu bạn giữ nguyên thực hành này, thì chế độ CBC với một mã hóa khối đảm bảo rằng bất kỳ hai khối văn bản gốc giống nhau sẽ được mã hóa khác nhau mỗi lần.

Cuối cùng, hãy chú ý đến **chế độ phản hồi đầu ra** (**OFB mode**). Bạn có thể thấy một hình ảnh về chế độ này trong *Hình 7*.

*Hình 7: Một mã hóa khối với chế độ OFB*

![Hình 7: Một mã hóa khối với chế độ OFB](assets/Figure4-7.webp "Hình 7: Một mã hóa khối với chế độ OFB")

Với chế độ OFB, bạn cũng chọn một vector khởi tạo. Nhưng ở đây, cho khối đầu tiên, vector khởi tạo được trực tiếp chèn vào mã hóa khối với khóa của bạn. 128-bit kết quả, sau đó, được xử lý như một luồng khóa. Luồng khóa này được XOR với văn bản gốc để tạo ra văn bản mã cho khối. Đối với các khối tiếp theo, bạn sử dụng luồng khóa từ khối trước đó làm đầu vào cho mã hóa khối và lặp lại các bước.

Nếu bạn quan sát kỹ, những gì thực sự được tạo ra ở đây từ mã hóa khối với chế độ OFB là một mã hóa luồng. Bạn tạo ra các phần luồng khóa 128-bit cho đến khi bạn có độ dài của văn bản gốc (loại bỏ các bit bạn không cần từ phần luồng khóa 128-bit cuối cùng). Sau đó, bạn XOR luồng khóa với thông điệp văn bản gốc của mình để thu được văn bản mã.

Trong phần trước về mã hóa luồng, tôi đã nói rằng bạn tạo ra một luồng khóa với sự giúp đỡ của một khóa riêng tư. Để chính xác, nó không chỉ được tạo ra với một khóa riêng tư. Như bạn có thể thấy trong chế độ OFB, luồng khóa được tạo ra với sự hỗ trợ của cả một khóa riêng tư và một vector khởi tạo.

Lưu ý rằng như với chế độ CBC, việc chọn một nonce giả ngẫu nhiên hoặc ngẫu nhiên cho vector khởi tạo mỗi lần bạn sử dụng mã hóa khối trong chế độ OFB là quan trọng. Nếu không, cùng một chuỗi thông điệp 128-bit được gửi trong các giao tiếp khác nhau sẽ được mã hóa theo cùng một cách. Đây là một cách để tạo ra mã hóa xác suất với một mã hóa luồng.

Một số mã hóa luồng chỉ sử dụng một khóa riêng tư để tạo ra một luồng khóa. Đối với những mã hóa luồng đó, quan trọng là bạn sử dụng một nonce ngẫu nhiên để chọn khóa riêng tư cho mỗi trường hợp giao tiếp. Nếu không, kết quả của việc mã hóa với những mã hóa luồng đó cũng sẽ là định hình, dẫn đến các vấn đề về an ninh.

Mã hóa khối hiện đại phổ biến nhất là **mã hóa Rijndael**. Đây là bài dự thi chiến thắng trong số mười lăm bài dự thi trong một cuộc thi do Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) tổ chức từ năm 1997 đến năm 2000 nhằm thay thế một tiêu chuẩn mã hóa cũ hơn, **tiêu chuẩn mã hóa dữ liệu** (**DES**).
Mã hóa Rijndael có thể được sử dụng với các thông số kỹ thuật khác nhau cho độ dài khóa và kích thước khối, cũng như trong các chế độ hoạt động khác nhau. Ủy ban của cuộc thi NIST đã chấp nhận một phiên bản hạn chế của mã hóa Rijndael—cụ thể là phiên bản yêu cầu kích thước khối 128-bit và độ dài khóa là 128 bit, 192 bit, hoặc 256 bit—là một phần của **tiêu chuẩn mã hóa nâng cao** (**AES**). Đây thực sự là tiêu chuẩn chính cho các ứng dụng mã hóa đối xứng. Nó an toàn đến mức ngay cả NSA cũng sẵn lòng sử dụng nó với khóa 256-bit cho các tài liệu tối mật.<sup>[6](#footnote6)</sup>
Mã khối AES sẽ được giải thích chi tiết trong *Chương 5*.

## Làm rõ sự nhầm lẫn
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Sự nhầm lẫn về sự phân biệt giữa mã khối và mã dòng xuất phát từ việc đôi khi mọi người sẽ hiểu thuật ngữ mã khối như là chỉ đặc biệt đến *mã khối với chế độ mã hóa khối*.

Xem xét các chế độ ECB và CBC trong phần trước. Những chế độ này đặc biệt yêu cầu dữ liệu để mã hóa phải chia hết cho kích thước khối (nghĩa là bạn có thể phải sử dụng đệm cho tin nhắn gốc). Ngoài ra, dữ liệu trong các chế độ này cũng được mã khối xử lý trực tiếp (và không chỉ kết hợp với kết quả của một hoạt động mã khối như trong chế độ OFB).

Do đó, thay thế, bạn có thể định nghĩa một **mã khối** là bất kỳ phương thức mã hóa nào, hoạt động trên các khối cố định của tin nhắn một lúc (nơi bất kỳ khối nào cũng phải dài hơn một byte, nếu không nó sẽ chuyển thành mã dòng). Cả dữ liệu để mã hóa và văn bản mã hóa phải chia đều theo kích thước khối này. Thông thường, kích thước khối là 64, 128, 192, hoặc 256 bit về độ dài. Ngược lại, một mã dòng có thể mã hóa bất kỳ tin nhắn nào theo từng bit hoặc byte một lúc.

Với sự hiểu biết cụ thể hơn này về mã khối, bạn có thể thực sự tuyên bố rằng các phương thức mã hóa hiện đại là mã dòng hoặc mã khối. Từ đây trở đi, tôi sẽ sử dụng thuật ngữ mã khối trong nghĩa rộng hơn trừ khi có chỉ định khác.

Cuộc thảo luận về chế độ OFB trong phần trước cũng đưa ra một điểm thú vị khác. Một số mã dòng được xây dựng từ mã khối, như Rijndael với OFB. Một số như Salsa20 và ChaCha không được tạo ra từ mã khối. Bạn có thể gọi những cái sau là **mã dòng nguyên thủy**. (Thực sự không có thuật ngữ chuẩn nào để chỉ các mã dòng như vậy.)

Khi mọi người nói về ưu và nhược điểm của mã dòng và mã khối, họ thường so sánh mã dòng nguyên thủy với các phương thức mã hóa dựa trên mã khối.

Mặc dù bạn luôn có thể dễ dàng xây dựng một mã dòng từ một mã khối, thì thường rất khó để xây dựng một loại cấu trúc với chế độ mã hóa khối (như với chế độ CBC) từ một mã dòng nguyên thủy.

Từ cuộc thảo luận này, bạn nên hiểu *Hình 8*. Nó cung cấp một cái nhìn tổng quan về các phương thức mã hóa đối xứng. Chúng tôi sử dụng ba loại phương thức mã hóa: mã dòng nguyên thủy, mã dòng mã khối, và mã khối trong chế độ khối (cũng được gọi là “mã khối” trong sơ đồ).

*Hình 8: Tổng quan về các phương thức mã hóa đối xứng*

![Hình 8: Tổng quan về các phương thức mã hóa đối xứng](assets/Figure4-8.webp "Hình 8: Tổng quan về các phương thức mã hóa đối xứng")

## Mã xác thực tin nhắn
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>
Mã hóa liên quan đến bí mật. Nhưng mật mã học cũng quan tâm đến các chủ đề rộng lớn hơn, như tính toàn vẹn của thông điệp, tính xác thực, và không thể chối cãi. Các **mã xác thực thông điệp** (MACs) là các kế hoạch mật mã học khóa đối xứng hỗ trợ tính xác thực và toàn vẹn trong giao tiếp.

Tại sao cần có gì ngoài bí mật trong giao tiếp? Giả sử Bob gửi cho Alice một thông điệp sử dụng mã hóa không thể phá vỡ được về mặt thực tế. Bất kỳ kẻ tấn công nào chặn được thông điệp này cũng sẽ không thể hiểu được bất kỳ thông tin quan trọng nào về nội dung. Tuy nhiên, kẻ tấn công vẫn có ít nhất hai phương thức tấn công khác có sẵn:

1. Cô ta có thể chặn bản mã, thay đổi nội dung của nó và gửi bản mã đã thay đổi đến Alice.
2. Cô ta có thể chặn hoàn toàn thông điệp của Bob và gửi bản mã do chính mình tạo ra.

Trong cả hai trường hợp này, kẻ tấn công có thể không có bất kỳ hiểu biết nào về nội dung từ các bản mã (1) và (2). Nhưng cô ta vẫn có thể gây ra thiệt hại đáng kể theo cách này. Đây là nơi mà mã xác thực thông điệp trở nên quan trọng.

Mã xác thực thông điệp được định nghĩa một cách lỏng lẻo là các kế hoạch mật mã học khóa đối xứng với ba thuật toán: một thuật toán tạo khóa, một thuật toán tạo thẻ, và một thuật toán xác minh. Một MAC an toàn đảm bảo rằng các thẻ là **không thể giả mạo tồn tại** đối với bất kỳ kẻ tấn công nào - tức là, họ không thể thành công tạo ra một thẻ trên thông điệp mà được xác minh, trừ khi họ có khóa riêng.

Bob và Alice có thể chống lại việc thao túng một thông điệp cụ thể bằng cách sử dụng MAC. Giả sử trong lúc này họ không quan tâm đến bí mật. Họ chỉ muốn đảm bảo rằng thông điệp mà Alice nhận được thực sự từ Bob và không bị thay đổi theo bất kỳ cách nào.

Quy trình được mô tả trong *Hình 9*. Để sử dụng MAC, trước tiên họ sẽ tạo một khóa riêng K được chia sẻ giữa hai người. Bob tạo một thẻ T cho thông điệp sử dụng khóa riêng K. Sau đó, anh ấy gửi thông điệp cũng như thẻ thông điệp cho Alice. Cô ấy có thể, sau đó, xác minh rằng Bob thực sự đã tạo thẻ, bằng cách chạy khóa riêng, thông điệp, và thẻ qua một thuật toán xác minh.

*Hình 9: Tổng quan về các kế hoạch mã hóa đối xứng*

![Hình 9: Tổng quan về các kế hoạch mã hóa đối xứng](assets/Figure4-9.webp "Hình 9: Tổng quan về các kế hoạch mã hóa đối xứng")

Do tính không thể giả mạo tồn tại, một kẻ tấn công không thể thay đổi thông điệp M theo bất kỳ cách nào hoặc tạo ra một thông điệp của riêng mình với một thẻ hợp lệ. Điều này vẫn đúng, ngay cả khi kẻ tấn công quan sát các thẻ của nhiều thông điệp giữa Bob và Alice sử dụng cùng một khóa riêng. Nhiều nhất, một kẻ tấn công có thể ngăn Alice nhận được thông điệp M (một vấn đề mà mật mã học không thể giải quyết).

Một MAC đảm bảo rằng một thông điệp thực sự được tạo ra bởi Bob. Tính xác thực này, tự động ngụ ý tính toàn vẹn của thông điệp - tức là, nếu Bob đã tạo ra một thông điệp nào đó, thì, theo đó, nó không bị thay đổi theo bất kỳ cách nào bởi kẻ tấn công. Vì vậy từ đây trở đi, mọi quan tâm đến xác thực nên được tự động hiểu là quan tâm đến toàn vẹn.

Mặc dù tôi đã phân biệt giữa tính xác thực và toàn vẹn của thông điệp trong cuộc thảo luận của mình, nhưng cũng thường thấy việc sử dụng những thuật ngữ này như những từ đồng nghĩa. Chúng, sau đó, đề cập đến ý tưởng của các thông điệp được tạo ra bởi một người gửi cụ thể và không bị thay đổi theo bất kỳ cách nào. Theo tinh thần này, mã xác thực thông điệp thường cũng được gọi là **mã toàn vẹn thông điệp**.

## Mã hóa xác thực
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>
Thông thường, bạn sẽ muốn đảm bảo cả tính bí mật và tính xác thực trong giao tiếp, do đó, các phương pháp mã hóa và các phương pháp MAC thường được sử dụng cùng nhau. 
Một **phương pháp mã hóa xác thực** là một phương pháp kết hợp mã hóa với MAC một cách an toàn cao. Cụ thể, nó phải đáp ứng các tiêu chuẩn về không thể giả mạo tồn tại cũng như một khái niệm rất mạnh mẽ về tính bí mật, cụ thể là khả năng chống lại **các cuộc tấn công chọn bản mã**.<sup>[7](#footnote7)</sup>

Để một phương pháp mã hóa có thể chống lại các cuộc tấn công chọn bản mã, nó phải đáp ứng các tiêu chuẩn về **không thể biến đổi**: tức là, bất kỳ sự thay đổi nào của bản mã bởi kẻ tấn công cũng sẽ dẫn đến một bản mã không hợp lệ hoặc một bản mã giải mã thành văn bản rõ không liên quan gì đến bản gốc.<sup>[8](#footnote8)</sup>

Vì một phương pháp mã hóa xác thực đảm bảo rằng một bản mã được tạo ra bởi kẻ tấn công luôn không hợp lệ (vì thẻ sẽ không được xác minh), nó đáp ứng các tiêu chuẩn chống lại các cuộc tấn công chọn bản mã. Thú vị là, bạn có thể chứng minh rằng một phương pháp mã hóa xác thực luôn có thể được tạo ra từ sự kết hợp của một MAC không thể giả mạo tồn tại và một phương pháp mã hóa đáp ứng một khái niệm an toàn ít mạnh mẽ hơn, được biết đến là **an toàn trước cuộc tấn công chọn văn bản rõ**.

Chúng tôi sẽ không đi sâu vào tất cả các chi tiết của việc xây dựng các phương pháp mã hóa xác thực. Nhưng quan trọng là phải biết hai chi tiết trong việc xây dựng chúng.

Đầu tiên, một phương pháp mã hóa xác thực trước tiên xử lý việc mã hóa và sau đó tạo một thẻ thông điệp trên bản mã. Hóa ra, các phương pháp khác—như kết hợp bản mã với một thẻ trên văn bản rõ, hoặc trước tiên tạo một thẻ và sau đó mã hóa cả văn bản rõ và thẻ—là không an toàn. Ngoài ra, cả hai hoạt động đều có khóa riêng biệt được chọn ngẫu nhiên, nếu không an ninh của bạn sẽ bị tổn hại nghiêm trọng.

Nguyên tắc nêu trên áp dụng một cách tổng quát hơn: *bạn luôn nên sử dụng các khóa khác nhau khi kết hợp các phương pháp mật mã cơ bản*.

Một phương pháp mã hóa xác thực được mô tả trong *Hình 10*. Bob trước tiên tạo ra một bản mã C từ thông điệp M sử dụng một khóa K<sub>C</sub> được chọn ngẫu nhiên. Sau đó, anh ta tạo ra một thẻ thông điệp T bằng cách chạy bản mã và một khóa khác được chọn ngẫu nhiên K<sub>T</sub> qua thuật toán tạo thẻ. Cả bản mã và thẻ thông điệp đều được gửi đến Alice.

Alice bây giờ trước tiên kiểm tra xem thẻ có hợp lệ với bản mã C và khóa K<sub>T</sub> hay không. Nếu hợp lệ, cô ấy có thể, sau đó, giải mã thông điệp sử dụng khóa K<sub>C</sub>. Không chỉ cô ấy được đảm bảo về một khái niệm rất mạnh mẽ về tính bí mật trong giao tiếp của họ, cô ấy cũng biết rằng thông điệp được tạo ra bởi Bob.

*Hình 10: Một phương pháp mã hóa xác thực*

![Hình 10: Một phương pháp mã hóa xác thực](assets/Figure4-10.webp "Hình 10: Một phương pháp mã hóa xác thực")

MAC được tạo như thế nào? Mặc dù MAC có thể được tạo ra thông qua nhiều phương pháp, một cách phổ biến và hiệu quả để tạo chúng là qua các hàm băm mật mã.

Chúng tôi sẽ giới thiệu kỹ hơn về các hàm băm mật mã trong *Chương 6*. Bây giờ, chỉ cần biết rằng một **hàm băm** là một hàm có thể tính toán hiệu quả, nhận đầu vào có kích thước tùy ý và cho ra kết quả có độ dài cố định. Ví dụ, hàm băm phổ biến **SHA-256** (secure hash algorithm 256) luôn tạo ra một đầu ra 256-bit bất kể kích thước của đầu vào. Một số hàm băm, như SHA-256, có các ứng dụng hữu ích trong mật mã học.
Loại thẻ phổ biến nhất được tạo ra bằng hàm băm mật mã là **mã xác thực tin nhắn dựa trên băm** (HMAC). Quy trình được mô tả trong *Hình 11*. Một bên tạo ra hai khóa riêng biệt từ một khóa riêng K, khóa bên trong K<sub>1</sub> và khóa bên ngoài K<sub>2</sub>. Bản rõ M hoặc bản mã hóa C sau đó được băm cùng với khóa bên trong. Kết quả T' sau đó được băm với khóa bên ngoài để tạo ra thẻ tin nhắn T.
Có một bảng màu của các hàm băm có thể được sử dụng để tạo ra một HMAC. Hàm băm thường được sử dụng nhất là SHA-256.

*Hình 11: HMAC*

![Hình 11: HMAC](assets/Figure4-11.webp "Hình 11: HMAC")


## Phiên giao tiếp an toàn
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Giả sử hai bên đang trong một phiên giao tiếp, vì vậy họ gửi nhiều tin nhắn qua lại.

Một lược đồ mã hóa xác thực cho phép người nhận của một tin nhắn xác minh rằng nó được tạo bởi đối tác của mình trong phiên giao tiếp (miễn là khóa riêng không bị rò rỉ). Điều này hoạt động tốt đối với một tin nhắn đơn lẻ. Tuy nhiên, thường thì hai bên gửi tin nhắn qua lại trong một phiên giao tiếp. Và trong bối cảnh đó, một lược đồ mã hóa xác thực đơn giản như được mô tả trong phần trước không đủ để cung cấp an ninh.

Lý do chính là vì một lược đồ mã hóa xác thực không cung cấp bất kỳ bảo đảm nào rằng tin nhắn thực sự cũng được gửi bởi người tạo ra nó trong một phiên giao tiếp. Xem xét ba vector tấn công sau:

1. **Tấn công phát lại**: Một kẻ tấn công gửi lại một bản mã và một thẻ mà cô ta đã chặn giữa hai bên tại một thời điểm trước đó.
2. **Tấn công đảo thứ tự**: Một kẻ tấn công chặn hai tin nhắn tại các thời điểm khác nhau và gửi chúng cho người nhận theo thứ tự ngược lại.
3. **Tấn công phản xạ**: Một kẻ tấn công quan sát một tin nhắn được gửi từ A đến B, và cũng gửi tin nhắn đó cho A.

Mặc dù kẻ tấn công không biết nội dung của bản mã và không thể tạo ra bản mã giả, các cuộc tấn công trên vẫn có thể gây ra thiệt hại đáng kể trong giao tiếp.

Giả sử, chẳng hạn, rằng một tin nhắn cụ thể giữa hai bên liên quan đến việc chuyển tiền tài chính. Một cuộc tấn công phát lại có thể chuyển tiền một lần nữa. Một lược đồ mã hóa xác thực đơn giản không có phòng vệ chống lại những cuộc tấn công như vậy.

May mắn thay, những loại tấn công này có thể dễ dàng được giảm thiểu trong một phiên giao tiếp sử dụng **bộ nhận dạng** và **chỉ báo thời gian tương đối**.

Bộ nhận dạng có thể được thêm vào tin nhắn rõ ràng trước khi mã hóa. Điều này sẽ ngăn chặn bất kỳ cuộc tấn công phản xạ nào. Một chỉ báo thời gian tương đối, ví dụ, có thể là một số thứ tự trong một phiên giao tiếp cụ thể. Mỗi bên thêm một số thứ tự vào một tin nhắn trước khi mã hóa, vì vậy người nhận biết thứ tự mà các tin nhắn được gửi. Điều này loại bỏ khả năng của các cuộc tấn công đảo thứ tự. Nó cũng loại bỏ các cuộc tấn công phát lại. Bất kỳ tin nhắn nào mà kẻ tấn công gửi xuống dòng sau này sẽ có một số thứ tự cũ, và người nhận sẽ biết không xử lý lại tin nhắn.

Để minh họa cách thức hoạt động của phiên giao tiếp an toàn, giả sử lại Alice và Bob. Họ gửi tổng cộng bốn tin nhắn qua lại. Bạn có thể thấy cách một lược đồ mã hóa xác thực với bộ nhận dạng và số thứ tự hoạt động dưới đây trong *Hình 11*.
Phiên giao tiếp bắt đầu bằng việc Bob gửi một bản mã hóa C<sub>0,B</sub> cho Alice với một thẻ tin nhắn T<sub>0,B</sub>. Bản mã hóa chứa thông điệp, cũng như một bộ nhận dạng (BOB) và một số thứ tự (0). Thẻ T<sub>0,B</sub> được tạo ra trên toàn bộ bản mã hóa. Trong các giao tiếp tiếp theo, Alice và Bob duy trì giao thức này, cập nhật các trường thông tin khi cần thiết.
*Hình 12: Một phiên giao tiếp an toàn*

![Hình 12: Một phiên giao tiếp an toàn](assets/Figure4-12.webp "Hình 12: Một phiên giao tiếp an toàn")

## Ghi chú
<chapterId>b96d38dd-c9cb-56a7-8764-4af8526bc63f</chapterId>

[^1]: Theo Seutonius, một loại mã hóa dịch chuyển với giá trị khóa cố định là 3 đã được Julius Caesar sử dụng trong giao tiếp quân sự của mình. Vì vậy, A luôn trở thành D, B luôn là E, C luôn là F, và cứ thế. Phiên bản cụ thể của mã hóa dịch chuyển này, do đó, đã trở nên nổi tiếng với tên gọi **Mã Caesar** (mặc dù nó không thực sự là một mã hóa trong nghĩa hiện đại của từ, vì giá trị khóa là cố định). Mã Caesar có thể đã an toàn vào thế kỷ thứ nhất trước Công Nguyên, nếu kẻ thù của Rome rất không quen thuộc với việc mã hóa. Nhưng rõ ràng nó sẽ không phải là một phương pháp rất an toàn trong thời đại hiện đại [^1].

[^2]: Jonathan Katz và Yehuda Lindell, *Giới thiệu về Mật mã học Hiện đại*, CRC Press (Boca Raton, FL: 2015), tr. 7f [^2].

[^3]: Eric Raymond, “Nhà thờ và Chợ búa,” bài báo được trình bày tại Linux Kongress, Würzburg, Đức (27 tháng 5, 1997). Có một số phiên bản sau này cũng như một cuốn sách. Trích dẫn của tôi đến từ trang 30 trong sách: Eric Raymond, *Nhà thờ và Chợ búa: Suy ngẫm về Linux và Nguồn mở bởi một Cách mạng tình cờ*, bản sửa đổi (2001), O’Reilly: Sebastopol, CA [^3].

[^4]: Bảo tàng Mật mã, "Đường dây nóng Washington-Moscow," 2013, có sẵn tại [Crypto Museum](https://www.cryptomuseum.com/crypto/hotline/index.htm) [^4].

[^5]: Tầm quan trọng của mã hóa xác suất lần đầu tiên được nhấn mạnh bởi Shafi Goldwasser và Silvio Micali, “Mã hóa xác suất,” *Journal of Co [^5].

# RC4 và AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

Trong Chương này, chúng ta sẽ thảo luận chi tiết về một phương pháp mã hóa với một mã hóa luồng nguyên thủy hiện đại, RC4 (hay "mã Rivest 4"), và một mã hóa khối hiện đại, AES. Mặc dù mã hóa RC4 đã không còn được ưa chuộng làm phương pháp mã hóa, AES là tiêu chuẩn cho mã hóa đối xứng hiện đại. Hai ví dụ này sẽ cung cấp một cái nhìn tốt hơn về cách mã hóa đối xứng hoạt động từ bên trong.
Để hiểu cách thức hoạt động của các mật mã luồng giả ngẫu nhiên hiện đại, tôi sẽ tập trung vào mật mã luồng RC4. Đây là một mật mã luồng giả ngẫu nhiên đã được sử dụng trong các giao thức bảo mật điểm truy cập không dây WEP và WAP cũng như trong TLS. Do RC4 có nhiều điểm yếu đã được chứng minh, nó đã trở nên không được ưa chuộng. Thực tế, Internet Engineering Task Force hiện nay cấm sử dụng các bộ RC4 bởi các ứng dụng client và server trong mọi trường hợp của TLS.<sup>[3](#footnote3)</sup> Tuy nhiên, nó vẫn là một ví dụ tốt để minh họa cách một mật mã luồng nguyên thủy hoạt động.

Để bắt đầu, tôi sẽ trình bày cách mã hóa một thông điệp văn bản rõ với một mật mã RC4 nhỏ. Giả sử thông điệp văn bản rõ của chúng ta là “SOUP.” Việc mã hóa với mật mã RC4 nhỏ của chúng ta, sau đó, diễn ra qua bốn bước.

### Bước 1

Đầu tiên, định nghĩa một mảng S với S[0] = 0 đến S[7] = 7. Một mảng ở đây đơn giản là một tập hợp các giá trị có thể thay đổi được tổ chức bởi một chỉ số, cũng được gọi là danh sách trong một số ngôn ngữ lập trình (ví dụ, Python). Trong trường hợp này, chỉ số chạy từ 0 đến 7, và các giá trị cũng chạy từ 0 đến 7. Vậy S như sau:

- S = [0,1,2,3,4,5,6,7]

Các giá trị ở đây không phải là số ASCII, mà là biểu diễn giá trị thập phân của chuỗi byte 1 byte. Vậy giá trị 2 sẽ bằng 0000 0011. Độ dài của mảng S, do đó, là 8 byte.

### Bước 2

Thứ hai, định nghĩa một mảng khóa K có độ dài 8 byte bằng cách chọn một khóa từ 1 đến 8 byte (không chấp nhận phân số byte). Vì mỗi byte là 8 bit, bạn có thể chọn bất kỳ số nào từ 0 đến 255 cho mỗi byte của khóa của bạn.

Giả sử chúng ta chọn khóa k của chúng ta là [14,48,9], vậy nó có độ dài 3 byte. Mỗi chỉ số của mảng khóa của chúng ta, sau đó, được thiết lập theo giá trị thập phân cho từng phần tử cụ thể của khóa, theo thứ tự. Nếu bạn chạy qua toàn bộ khóa, bắt đầu lại từ đầu, cho đến khi bạn đã điền đủ 8 ô của mảng khóa. Vậy, mảng khóa của chúng ta như sau

- K = [14,48,9,14,48,9,14,48]

### Bước 3

Thứ ba, chúng ta sẽ biến đổi mảng S sử dụng mảng khóa K, trong một quá trình được biết đến là lập lịch khóa. Quá trình này được mô tả như sau trong giả mã:

- Tạo biến j và i
- Đặt biến j = 0
- Đối với mỗi i từ 0 đến 7:
	- Đặt j = j + S[i] + K[i] mod 8
	- Hoán đổi S[i] và S[j]

Sự biến đổi của mảng S được ghi lại bởi *Bảng 1*.

Để bắt đầu, bạn có thể thấy trạng thái ban đầu của S là [0,1,2,3,4,5,6,7] với giá trị ban đầu là 0 cho j. Điều này sẽ được biến đổi sử dụng mảng khóa [14,48,9,14,48,9,14,48].
Vòng lặp for bắt đầu với i = 0. Theo mã giả mà chúng ta đã nêu ở trên, giá trị mới của j trở thành 6 (j = j + S[0] + K[0] mod 8 = 0 + 0 + 14 mod 8 = 6 mod 8). Hoán đổi S[0] và S[6], trạng thái của S sau 1 vòng trở thành [6,1,2,3,4,5,0,7]. 
Trong hàng tiếp theo, i = 1. Tiếp tục qua vòng lặp for, j nhận được giá trị là 7 (j = j + S[1] + K[1] mod 8 = 6 + 1 + 48 mod 8 = 55 mod 8 = 7 mod 8). Hoán đổi S[1] và S[7] từ trạng thái hiện tại của S, [6,1,2,3,4,5,0,7], ta được [6,7,2,3,4,5,0,1] sau vòng 2.

Chúng ta tiếp tục quá trình này cho đến khi tạo ra hàng cuối cùng ở dưới cùng cho mảng S, [6,4,1,0,3,7,5,2].

*Bảng 1: Bảng lập lịch khóa*

![Bảng 1: Bảng lập lịch khóa](assets/Table5-1.webp "Bảng 1: Bảng lập lịch khóa")

### Bước 4

Là bước thứ tư, chúng ta tạo ra dòng khóa. Đây là chuỗi ngẫu nhiên giả có độ dài bằng với thông điệp mà chúng ta muốn gửi. Đây sẽ là thứ được sử dụng để mã hóa thông điệp gốc “SOUP.” Vì dòng khóa cần phải dài bằng với thông điệp, chúng ta cần một dòng có 4 byte.

Dòng khóa được tạo ra bởi mã giả sau:

- Tạo các biến j, i, và t
- Đặt j = 0
- Đối với mỗi i của bản rõ, bắt đầu với i = 1 và đi cho đến i = 4, mỗi byte của dòng khóa được tạo ra như sau:
    - j = j + S[i] mod 8
	- Hoán đổi S[i] và S[j]
	- t = S[i] + S[j] mod 8
	- Byte thứ i của dòng khóa = S[t]

Bạn có thể theo dõi các tính toán trong *Bảng 2*.

Trạng thái ban đầu của S = S = [6,4,1,0,3,7,5,2]. Đặt i = 1, giá trị j trở thành 4 (j = j + S[i] mod 8 = 0 + 4 mod 8 = 4). Sau đó, chúng ta hoán đổi S[1] và S[4] để tạo ra sự biến đổi của S trong hàng thứ hai, [6,3,1,0,4,7,5,2]. Giá trị t sau đó là 7 (t = S[i] + S[j] mod 8 = 3 + 4 mod 8 = 7). Cuối cùng, byte cho dòng khóa sau đó là S[7], hay 2.

Chúng ta có thể, sau đó, tiếp tục tạo ra các byte khác cho đến khi chúng ta có bốn byte sau: 2, 6, 3, và 7. Mỗi byte này có thể, sau đó, được sử dụng để mã hóa mỗi chữ cái của bản rõ, "SOUP".
Để bắt đầu, sử dụng bảng ASCII, chúng ta có thể thấy rằng “SOUP” được mã hóa bởi các giá trị thập phân của chuỗi byte cơ bản là “83 79 85 80”. Kết hợp với dòng khóa “2 6 3 2” tạo ra “85 85 88 82”, giá trị này vẫn giữ nguyên sau phép toán modulo 256. Trong ASCII, bản mã hóa “85 85 88 82” tương đương với “UUXR”. 
Điều gì xảy ra nếu từ cần mã hóa dài hơn mảng S? Trong trường hợp đó, mảng S chỉ tiếp tục biến đổi theo cách được hiển thị ở trên cho mỗi byte i của bản rõ, cho đến khi chúng ta có một số byte trong dòng khóa bằng với số chữ cái trong bản rõ.

*Table 2: Keystream generation*

![Table 2: Keystream generation](assets/Table5-2.webp "Table 2: Keystream generation")

Ví dụ mà chúng ta vừa thảo luận chỉ là phiên bản giản lược của mã hóa luồng RC4. Mã hóa luồng RC4 thực sự có một mảng S dài 256 byte, không phải 8 byte, và một khóa có thể dài từ 1 đến 256 byte, không phải từ 1 đến 8 byte. Mảng khóa và các dòng khóa, sau đó, đều được sản xuất dựa trên chiều dài 256 byte của mảng S. Những tính toán trở nên cực kỳ phức tạp, nhưng các nguyên tắc vẫn giữ nguyên. Sử dụng cùng một khóa, [14,48,9], với mã hóa luồng RC4 tiêu chuẩn, thông điệp bản rõ "SOUP" được mã hóa thành 67 02 ed df theo định dạng thập lục phân.

Một mã hóa luồng trong đó dòng khóa cập nhật độc lập với thông điệp bản rõ hoặc bản mã hóa là **mã hóa luồng đồng bộ**. Dòng khóa chỉ phụ thuộc vào khóa. Rõ ràng, RC4 là một ví dụ của mã hóa luồng đồng bộ, vì dòng khóa không có mối quan hệ nào với bản rõ hoặc bản mã hóa. Tất cả các mã hóa luồng nguyên thủy mà chúng ta đã đề cập trong chương trước, bao gồm mã hóa dịch chuyển, mã hóa Vigenere, và mã hóa một lần, cũng thuộc loại đồng bộ.

Ngược lại, một **mã hóa luồng không đồng bộ** có dòng khóa được sản xuất bởi cả khóa và các phần tử trước đó của bản mã hóa. Loại mã hóa này còn được gọi là **mã hóa tự đồng bộ**.

Quan trọng, dòng khóa được sản xuất với RC4 nên được xem như một mã hóa một lần, và bạn không thể sản xuất dòng khóa một cách chính xác theo cùng một cách vào lần sau. Thay vì thay đổi khóa mỗi lần, giải pháp thực tế là kết hợp khóa với một nonce để sản xuất dòng byte.

## AES với khóa 128-bit
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Như đã đề cập trong chương trước, Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) đã tổ chức một cuộc thi từ năm 1997 đến năm 2000 để xác định một tiêu chuẩn mã hóa đối xứng mới. Mã hóa Rijndael đã trở thành bài dự thi chiến thắng. Tên gọi là một trò chơi chữ dựa trên tên của các nhà sáng tạo người Bỉ, Vincent Rijmen và Joan Daemen.

Mã hóa Rijndael là một mã hóa khối, có nghĩa là có một thuật toán cốt lõi, có thể được sử dụng với các thông số kỹ thuật khác nhau cho độ dài khóa và kích thước khối. Bạn có thể, sau đó, sử dụng nó với các chế độ hoạt động khác nhau để xây dựng các lược đồ mã hóa.
Ủy ban của cuộc thi NIST đã chọn phiên bản thu hẹp của mật mã Rijndael—cụ thể là phiên bản yêu cầu kích thước khối 128-bit và độ dài khóa là 128 bit, 192 bit hoặc 256 bit—làm một phần của tiêu chuẩn mã hóa nâng cao. Phiên bản thu hẹp này của mật mã Rijndael cũng có thể được sử dụng dưới nhiều chế độ hoạt động khác nhau. Đặc tả cho tiêu chuẩn này được biết đến là Tiêu Chuẩn Mã Hóa Nâng Cao (AES).

Để minh họa cách mật mã Rijndael hoạt động, làm nền tảng của AES, tôi sẽ trình bày quy trình mã hóa với khóa 128-bit. Kích thước khóa ảnh hưởng đến số vòng được thực hiện cho mỗi khối mã hóa. Đối với khóa 128-bit, cần 10 vòng. Với 192 bit và 256 bit, sẽ lần lượt là 12 và 14 vòng.

Ngoài ra, tôi sẽ giả định rằng AES được sử dụng trong chế độ ECB. Điều này làm cho việc trình bày dễ dàng hơn và không ảnh hưởng đến thuật toán Rijndael. Để chắc chắn, chế độ ECB không an toàn trong thực tế vì nó dẫn đến mã hóa xác định. Chế độ an toàn thường được sử dụng với AES là CBC.

Hãy gọi khóa là K<sub>0</sub>. Cấu trúc với các tham số trên, sau đó, trông như trong Hình 1, nơi M<sub>i</sub> đại diện cho một phần của thông điệp văn bản rõ dài 128 bit và C<sub>i</sub> cho một phần của văn bản mã dài 128 bit. Đệm được thêm vào văn bản rõ cho khối cuối cùng, nếu văn bản rõ không thể chia đều theo kích thước khối.

*Hình 1: AES-ECB với khóa 128-bit*

![Hình 1: AES-ECB với khóa 128-bit](assets/Figure5-1.webp "Hình 1: AES-ECB với khóa 128-bit")

Mỗi khối văn bản 128-bit đi qua mười vòng trong kế hoạch mã hóa Rijndael. Điều này yêu cầu một khóa vòng riêng biệt cho mỗi vòng (K<sub>1</sub> đến K<sub>10</sub>). Những khóa này được sản xuất cho mỗi vòng từ khóa gốc 128-bit K<sub>0</sub> sử dụng một thuật toán mở rộng khóa. Do đó, cho mỗi khối văn bản cần được mã hóa, chúng ta sẽ sử dụng khóa gốc K<sub>0</sub> cũng như mười khóa vòng riêng biệt. Lưu ý rằng những 11 khóa này được sử dụng cho mỗi khối văn bản rõ 128-bit cần mã hóa.

Thuật toán mở rộng khóa dài và phức tạp. Việc nghiên cứu qua nó có ít lợi ích giáo dục. Bạn có thể tự tìm hiểu thuật toán mở rộng khóa nếu bạn muốn. Một khi các khóa vòng được sản xuất, mật mã Rijndael sẽ thao tác khối văn bản rõ 128-bit đầu tiên, M<sub>1</sub>, như thấy trong Hình 2. Bây giờ chúng ta sẽ đi qua các bước này.

*Hình 2: Sự thao tác của M<sub>1</sub> với mật mã Rijndael*

![Hình 2: AES-ECB với khóa 128-bit](assets/Figure5-2.webp "Hình 2: AES-ECB với khóa 128-bit")

### Vòng 0

Vòng 0 của mật mã Rijndael rất đơn giản. Một mảng S<sub>0</sub> được tạo ra bởi một phép toán XOR giữa văn bản rõ 128-bit và khóa riêng. Cụ thể là,

- S<sub>0</sub> = M<sub>1</sub> XOR K<sub>0</sub>
Trong vòng 1, mảng S<sub>0</sub> đầu tiên được kết hợp với khóa vòng K<sub>1</sub> thông qua phép toán XOR. Điều này tạo ra trạng thái mới của S.
Thứ hai, thực hiện phép thay thế byte trên trạng thái hiện tại của S. Phép toán này hoạt động bằng cách lấy từng byte của mảng S 16-byte và thay thế nó bằng một byte từ một mảng được gọi là **Rijndael’s S-box**. Mỗi byte có một phép biến đổi duy nhất, và một trạng thái mới của S được tạo ra như một kết quả. Rijndael's S-box được hiển thị trong *Hình 3*.

*Hình 3: Rijndael's S-Box*

![Hình 3: Rijndael's S-Box](assets/Figure5-3.webp "Hình 3: Rijndael's S-Box")

S-Box này là một nơi mà đại số trừu tượng được áp dụng trong mã hóa Rijndael, cụ thể là trường Galois.

Để bắt đầu, bạn định nghĩa mỗi phần tử byte có thể có từ 00 đến FF như một vector 8-bit. Mỗi vector như vậy là một phần tử của trường Galois GF(2<sup>8</sup>) nơi đa thức không thể giảm được cho phép toán modulo là x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Trường Galois với các thông số này cũng được gọi là Trường Hữu Hạn Rijndael.

Tiếp theo, cho mỗi phần tử có thể có trong trường, chúng ta tạo ra cái được gọi là **Nyberg S-Box**. Trong hộp này, mỗi byte được ánh xạ vào nghịch đảo nhân của nó (tức là, sao cho tích của chúng bằng 1). Sau đó, chúng ta ánh xạ những giá trị đó từ Nyberg S-box sang Rijndael’s S-Box sử dụng phép biến đổi affine.

Phép toán thứ ba trên mảng S là phép dịch hàng. Nó lấy trạng thái của S và liệt kê tất cả mười sáu byte trong một ma trận. Việc điền ma trận bắt đầu ở góc trên bên trái và di chuyển xung quanh bằng cách đi từ trên xuống dưới và sau đó, mỗi khi một cột được điền, dịch một cột sang phải và lên trên.

Một khi ma trận của S đã được xây dựng, bốn hàng được dịch chuyển. Hàng đầu tiên giữ nguyên. Hàng thứ hai dịch chuyển sang trái một vị trí. Hàng thứ ba dịch chuyển sang trái hai vị trí. Hàng thứ tư dịch chuyển sang trái ba vị trí. Một ví dụ về quá trình này được cung cấp trong *Hình 4*. Trạng thái ban đầu của S được hiển thị ở trên, trạng thái kết quả sau phép dịch hàng được hiển thị bên dưới.

*Hình 4: Phép dịch hàng*

![Hình 4: Phép dịch hàng](assets/Figure5-4.webp "Hình 4: Phép dịch hàng")

Trong bước thứ tư, trường Galois lại xuất hiện một lần nữa. Để bắt đầu, mỗi cột của ma trận S được nhân với cột của ma trận 4 x 4 được thấy trong *Hình 5*. Nhưng thay vì là phép nhân ma trận thông thường, đây là phép nhân vector modulo một đa thức không thể giảm, x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Các hệ số vector kết quả đại diện cho các bit riêng lẻ của một byte.

*Hình 5: Ma trận trộn cột*

![Hình 5: Ma trận trộn cột](assets/Figure5-5.webp "Hình 5: Ma trận trộn cột")

Phép nhân cột đầu tiên của ma trận S với ma trận 4 x 4 ở trên tạo ra kết quả trong *Hình 6*.
*Hình 6: Phép nhân cột đầu tiên*
![Hình 6: Phép nhân cột đầu tiên](assets/Figure5-6.webp "Hình 6: Phép nhân cột đầu tiên")

Bước tiếp theo, tất cả các số hạng trong ma trận sẽ được chuyển đổi thành đa thức. Ví dụ, F1 đại diện cho 1 byte và sẽ trở thành x<sup>7</sup> + x<sup>6</sup> + x<sup>5</sup> + x<sup>4</sup> + 1 và 03 đại diện cho 1 byte và sẽ trở thành x + 1.

Tất cả các phép nhân sau đó được thực hiện modulo x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Kết quả là việc cộng bốn đa thức trong mỗi ô của cột. Sau khi thực hiện các phép cộng modulo 2, bạn sẽ có bốn đa thức. Mỗi đa thức này đại diện cho một chuỗi 8-bit, hay 1 byte, của S. Chúng tôi sẽ không thực hiện tất cả các phép tính này tại đây trên ma trận trong *Hình 6* vì chúng khá phức tạp.

Sau khi cột đầu tiên đã được xử lý, ba cột còn lại của ma trận S được xử lý theo cùng một cách. Cuối cùng, điều này sẽ tạo ra một ma trận với mười sáu byte có thể được chuyển đổi thành một mảng.

Bước cuối cùng, mảng S được kết hợp với khóa vòng lại trong một phép toán XOR. Điều này tạo ra trạng thái S<sub>1</sub>. Đó là,

- S<sub>1</sub> = S XOR K<sub>0</sub>

### Vòng 2 đến 10

Các vòng từ 2 đến 9 chỉ là sự lặp lại của vòng 1, *mutatis mutandis*. Vòng cuối cùng trông rất giống với các vòng trước, ngoại trừ bước trộn cột được loại bỏ. Đó là, vòng 10 được thực hiện như sau:

- S<sub>9</sub> XOR K<sub>10</sub>
- Thay Thế Byte
- Dịch Hàng
- S<sub>10</sub> = S XOR K<sub>10</sub>

Trạng thái S<sub>10</sub> bây giờ được thiết lập thành C<sub>1</sub>, 128 bit đầu tiên của bản mã hóa. Tiếp tục với các khối bản rõ 128-bit còn lại sẽ tạo ra bản mã hóa đầy đủ C.

### Các thao tác của mật mã Rijndael

Lý do đằng sau các thao tác khác nhau trong mật mã Rijndael là gì?

Không đi sâu vào chi tiết, các phương pháp mã hóa được đánh giá dựa trên mức độ chúng tạo ra sự nhầm lẫn và phân tán. Nếu phương pháp mã hóa có một mức độ **nhầm lẫn** cao, điều này có nghĩa là bản mã hóa trông rất khác so với bản rõ. Nếu phương pháp mã hóa có một mức độ **phân tán** cao, điều này có nghĩa là bất kỳ sự thay đổi nhỏ nào đối với bản rõ cũng tạo ra một bản mã hóa rất khác biệt.

Lý do cho các thao tác đằng sau mật mã Rijndael là chúng tạo ra cả một mức độ nhầm lẫn và phân tán cao. Sự nhầm lẫn được tạo ra bởi thao tác Thay Thế Byte, trong khi sự phân tán được tạo ra bởi các thao tác Dịch Hàng và Trộn Cột.

# Mật Mã Bất Đối Xứng
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

Giống như mật mã đối xứng, các phương pháp bất đối xứng có thể được sử dụng để đảm bảo cả bí mật và xác thực. Tuy nhiên, ngược lại, các phương pháp này sử dụng hai khóa thay vì một: một khóa riêng và một khóa công khai.
Chúng ta bắt đầu cuộc điều tra của mình với việc khám phá ra mật mã bất đối xứng, đặc biệt là những vấn đề đã thúc đẩy nó. Tiếp theo, chúng ta sẽ thảo luận về cách thức hoạt động của các phương pháp mã hóa và xác thực bất đối xứng ở mức độ cao. Sau đó, chúng ta giới thiệu về hàm băm, đó là chìa khóa để hiểu về các phương pháp xác thực bất đối xứng, và cũng có liên quan trong các bối cảnh mật mã khác, như cho các mã xác thực tin nhắn dựa trên băm mà chúng ta đã thảo luận trong Chương 4.

## Vấn đề phân phối và quản lý khóa
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Giả sử Bob muốn mua một chiếc áo mưa mới từ Jim’s Sporting Goods, một nhà bán lẻ đồ thể thao trực tuyến với hàng triệu khách hàng ở Bắc Mỹ. Đây sẽ là lần mua hàng đầu tiên của anh ấy từ họ và anh ấy muốn sử dụng thẻ tín dụng của mình. Vì vậy, Bob sẽ cần phải tạo một tài khoản với Jim’s Sporting Goods, điều này đòi hỏi phải gửi các thông tin cá nhân như địa chỉ và thông tin thẻ tín dụng của mình. Sau đó, anh ấy có thể thực hiện các bước cần thiết để mua chiếc áo mưa.

Bob và Jim’s Sporting Goods sẽ muốn đảm bảo rằng giao tiếp của họ an toàn trong suốt quá trình này, xem xét rằng Internet là một hệ thống giao tiếp mở. Họ sẽ muốn đảm bảo, ví dụ, rằng không có kẻ tấn công tiềm năng nào có thể biết được thông tin thẻ tín dụng và địa chỉ của Bob, và không có kẻ tấn công tiềm năng nào có thể lặp lại việc mua hàng của anh ấy hoặc tạo ra những giao dịch giả mạo thay mặt anh ấy.

Một phương pháp mã hóa xác thực tiên tiến như đã được thảo luận trong chương trước chắc chắn có thể làm cho giao tiếp giữa Bob và Jim’s Sporting Goods an toàn. Nhưng rõ ràng có những trở ngại thực tế để triển khai một phương pháp như vậy.

Để minh họa những trở ngại thực tế này, giả sử chúng ta sống trong một thế giới mà chỉ có các công cụ của mật mã đối xứng tồn tại. Jim’s Sporting Goods và Bob, sau đó, có thể làm gì để đảm bảo giao tiếp an toàn?

Trong những hoàn cảnh đó, họ sẽ phải đối mặt với chi phí đáng kể để giao tiếp một cách an toàn. Vì Internet là một hệ thống giao tiếp mở, họ không thể chỉ trao đổi một bộ khóa qua nó. Do đó, Bob và một đại diện cho Jim’s Sporting Goods sẽ cần phải thực hiện trao đổi khóa trực tiếp.

Một khả năng là Jim’s Sporting Goods tạo ra các địa điểm trao đổi khóa đặc biệt, nơi Bob và các khách hàng mới khác có thể lấy một bộ khóa cho giao tiếp an toàn. Điều này rõ ràng sẽ tốn kém về tổ chức và giảm đáng kể hiệu quả mà khách hàng mới có thể thực hiện mua hàng.

Mặt khác, Jim’s Sporting Goods có thể gửi cho Bob một cặp khóa thông qua một dịch vụ chuyển phát tin cậy cao. Điều này có lẽ hiệu quả hơn việc tổ chức các địa điểm trao đổi khóa. Nhưng điều này vẫn sẽ tốn kém đáng kể, đặc biệt nếu nhiều khách hàng chỉ thực hiện một hoặc vài lần mua hàng.

Tiếp theo, một phương pháp mã hóa xác thực đối xứng cũng buộc Jim’s Sporting Goods phải lưu trữ các bộ khóa riêng biệt cho tất cả khách hàng của họ. Điều này sẽ là một thách thức thực tế đáng kể cho hàng nghìn khách hàng, chứ đừng nói đến hàng triệu.

Để hiểu điểm này, giả sử Jim’s Sporting Goods cung cấp cho mỗi khách hàng cùng một cặp khóa. Điều này sẽ cho phép mỗi khách hàng - hoặc bất kỳ ai khác có thể lấy được cặp khóa này - đọc và thậm chí là thao túng tất cả các giao tiếp giữa Jim’s Sporting Goods và khách hàng của họ. Bạn có thể, sau đó, cũng không sử dụng mật mã trong giao tiếp của mình.

Thậm chí việc lặp lại một bộ khóa cho chỉ một số khách hàng cũng là một thực hành bảo mật tồi tệ. Bất kỳ kẻ tấn công tiềm năng nào cũng có thể cố gắng khai thác tính năng đó của phương pháp (nhớ rằng kẻ tấn công được giả định biết mọi thứ về một phương pháp trừ khóa, theo nguyên tắc Kerckhoffs.)

Vì vậy, Jim’s Sporting Goods sẽ phải lưu trữ một cặp khóa cho mỗi khách hàng, bất kể cách phân phối các cặp khóa này như thế nào. Điều này rõ ràng đặt ra một số vấn đề thực tế.

- Jim’s Sporting Goods sẽ phải lưu trữ hàng triệu cặp khóa, một bộ cho mỗi khách hàng.
- Những chiếc chìa khóa này cần phải được bảo mật cẩn thận, vì chúng chắc chắn sẽ trở thành mục tiêu cho các hacker. Bất kỳ sự vi phạm nào về an ninh đều yêu cầu việc lặp lại việc trao đổi chìa khóa tốn kém, hoặc tại các địa điểm trao đổi chìa khóa đặc biệt hoặc qua dịch vụ chuyển phát. - Bất kỳ khách hàng nào của Jim’s Sporting Goods cũng cần phải lưu trữ an toàn một cặp chìa khóa tại nhà. Việc mất mát và trộm cắp sẽ xảy ra, yêu cầu việc lặp lại việc trao đổi chìa khóa. Khách hàng cũng cần phải trải qua quy trình này với bất kỳ cửa hàng trực tuyến nào hoặc các loại thực thể khác mà họ muốn giao tiếp và giao dịch qua Internet.

Hai thách thức chính vừa được mô tả là những mối quan tâm cơ bản cho đến cuối những năm 1970. Chúng được biết đến là **vấn đề phân phối chìa khóa** và **vấn đề quản lý chìa khóa**, tương ứng.

Những vấn đề này luôn tồn tại, tất nhiên, và thường gây ra những rắc rối trong quá khứ. Ví dụ, lực lượng quân sự sẽ phải liên tục phân phối sách chìa khóa cho giao tiếp an toàn đến nhân viên trên thực địa với rủi ro và chi phí lớn. Nhưng những vấn đề này trở nên tồi tệ hơn khi thế giới ngày càng chuyển sang giao tiếp kỹ thuật số từ xa, đặc biệt là cho các thực thể phi chính phủ.

Nếu những vấn đề này không được giải quyết vào những năm 1970, việc mua sắm hiệu quả và an toàn tại Jim’s Sporting Goods có lẽ sẽ không tồn tại. Thực tế, phần lớn thế giới hiện đại của chúng ta với việc gửi email thực tế và an toàn, ngân hàng trực tuyến, và mua sắm có lẽ chỉ là một giấc mơ xa vời. Bất cứ thứ gì giống như Bitcoin có lẽ không thể tồn tại.

Vậy, điều gì đã xảy ra vào những năm 1970? Làm thế nào mà chúng ta có thể mua sắm trực tuyến ngay lập tức và duyệt web thế giới một cách an toàn? Làm thế nào mà chúng ta có thể gửi Bitcoin tức thì khắp thế giới từ điện thoại thông minh của mình?

## Hướng mới trong mật mã học
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Vào những năm 1970, vấn đề phân phối chìa khóa và quản lý chìa khóa đã thu hút sự chú ý của một nhóm các nhà mật mã học học thuật Mỹ: Whitfield Diffie, Martin Hellman, và Ralph Merkle. Trước sự hoài nghi nặng nề từ đa số đồng nghiệp của họ, họ đã mạo hiểm tìm ra giải pháp cho nó.

Ít nhất một động lực chính cho sự mạo hiểm của họ là sự nhìn xa trông rộng rằng giao tiếp máy tính mở sẽ ảnh hưởng sâu sắc đến thế giới của chúng ta. Như Diffie và Hellman lưu ý vào năm 1976,

> Sự phát triển của các mạng lưới giao tiếp điều khiển bằng máy tính hứa hẹn liên lạc dễ dàng và ít tốn kém giữa những người hoặc máy tính ở hai phía của thế giới, thay thế hầu hết thư từ và nhiều chuyến đi bằng giao tiếp viễn thông. Đối với nhiều ứng dụng, những liên lạc này cần được bảo mật chống lại cả việc nghe lén và sự chèn vào của tin nhắn không hợp lệ. Tuy nhiên, hiện tại, giải pháp cho các vấn đề an ninh lại tụt hậu so với các lĩnh vực khác của công nghệ giao tiếp. *Mật mã học hiện đại không thể đáp ứng được các yêu cầu, bởi việc sử dụng nó sẽ gây ra những bất tiện nghiêm trọng cho người dùng hệ thống, đến mức loại bỏ nhiều lợi ích của việc xử lý thông tin từ xa.*<sup>[1](#footnote1)</sup>

Sự kiên trì của Diffie, Hellman, và Merkle đã được đền đáp. Bản công bố đầu tiên của kết quả nghiên cứu của họ là một bài báo của Diffie và Hellman vào năm 1976 có tựa đề “Hướng mới trong Mật mã học.” Trong đó, họ đã trình bày hai cách tiếp cận mới để giải quyết vấn đề phân phối chìa khóa và quản lý chìa khóa.
Giải pháp đầu tiên họ đề xuất là một *giao thức trao đổi khóa từ xa*, tức là, một bộ quy tắc cho việc trao đổi một hoặc nhiều khóa đối xứng qua một kênh truyền thông không an toàn. Giao thức này hiện được biết đến với tên gọi *giao thức trao đổi khóa Diffie-Helmann* hoặc *giao thức trao đổi khóa Diffie-Helmann-Merkle*.<sup>[2](#footnote2)</sup>
Với giao thức trao đổi khóa Diffie-Helmann, hai bên trước tiên công bố một số thông tin một cách công khai trên một kênh không an toàn như Internet. Dựa trên thông tin đó, họ sau đó, độc lập tạo ra một khóa đối xứng (hoặc một cặp khóa đối xứng) cho việc giao tiếp an toàn. Mặc dù cả hai bên tạo ra khóa của mình một cách độc lập, thông tin họ chia sẻ công khai đảm bảo rằng quá trình tạo khóa này mang lại cùng một kết quả cho cả hai bên.

Quan trọng là, mặc dù mọi người có thể quan sát thông tin được trao đổi công khai bởi các bên qua kênh không an toàn, chỉ có hai bên tham gia vào việc trao đổi thông tin mới có thể tạo ra khóa đối xứng từ nó.

Điều này, tất nhiên, nghe có vẻ hoàn toàn trái với trực giác. Làm thế nào mà hai bên có thể trao đổi một số thông tin một cách công khai mà chỉ cho phép họ tạo ra khóa đối xứng từ nó? Tại sao bất kỳ ai khác quan sát việc trao đổi thông tin không thể tạo ra cùng một khóa?

Nó dựa trên một số toán học tuyệt đẹp, tất nhiên. Giao thức trao đổi khóa Diffie-Helmann hoạt động thông qua một hàm một chiều với một cửa hậu. Hãy thảo luận về ý nghĩa của hai thuật ngữ này lần lượt.

Giả sử bạn được cho một hàm f(x) và kết quả f(a) = y, nơi a là một giá trị cụ thể cho x. Chúng ta nói rằng f(x) là một **hàm một chiều** nếu việc tính toán giá trị y khi biết a và f(x) là dễ dàng, nhưng việc tính toán giá trị a khi biết y và f(x) là không khả thi về mặt tính toán. Tên gọi hàm một chiều, tất nhiên, xuất phát từ thực tế là hàm đó chỉ thực tế để tính toán theo một hướng.

Một số hàm một chiều có cái gọi là cửa hậu. Mặc dù việc tính toán a khi chỉ biết y và f(x) là gần như không thể, có một thông tin cụ thể Z làm cho việc tính toán a từ y trở nên khả thi về mặt tính toán. Thông tin này Z được biết đến là **cửa hậu**. Các hàm một chiều có cửa hậu được biết đến là **hàm cửa hậu**.

Chúng tôi sẽ không đi sâu vào chi tiết của giao thức trao đổi khóa Diffie-Helmann ở đây. Nhưng cơ bản, mỗi bên tạo ra một số thông tin, một phần của nó được chia sẻ công khai và một số phần còn lại được giữ bí mật. Mỗi bên, sau đó, lấy phần thông tin bí mật của mình và thông tin công khai được chia sẻ bởi bên kia để tạo ra một khóa riêng tư. Và một cách kỳ diệu, cả hai bên sẽ kết thúc với cùng một khóa riêng tư.

Bất kỳ bên nào chỉ quan sát thông tin được chia sẻ công khai giữa hai bên trong một giao dịch trao đổi khóa Diffie Helmann không thể sao chép các phép tính này. Họ sẽ cần thông tin riêng tư từ một trong hai bên để làm như vậy.

Mặc dù phiên bản cơ bản của giao thức trao đổi khóa Diffie-Helmann được trình bày trong bài báo năm 1976 không rất an toàn, các phiên bản tinh vi hơn của giao thức cơ bản chắc chắn vẫn được sử dụng ngày nay. Quan trọng nhất, mọi giao thức trao đổi khóa trong phiên bản mới nhất của giao thức bảo mật lớp vận chuyển (phiên bản 1.3) đều cơ bản là một phiên bản được làm giàu của giao thức được trình bày bởi Diffie và Hellman vào năm 1976. Giao thức bảo mật lớp vận chuyển là giao thức chủ đạo cho việc trao đổi thông tin một cách an toàn được định dạng theo giao thức truyền tải siêu văn bản (http), tiêu chuẩn cho việc trao đổi nội dung Web.
Quan trọng, việc trao đổi khóa Diffie-Hellman không phải là một phương thức bất đối xứng. Nói một cách chính xác, nó có thể được coi là thuộc về lĩnh vực của mật mã khóa đối xứng. Nhưng vì cả việc trao đổi khóa Diffie-Hellman và mật mã học bất đối xứng đều dựa vào các hàm số học một chiều với cửa hậu, chúng thường được thảo luận cùng nhau.

Cách thứ hai mà Diffie và Hellman đề xuất để giải quyết vấn đề phân phối và quản lý khóa trong bài báo của họ năm 1976, tất nhiên, thông qua mật mã học bất đối xứng.

Trái ngược với việc trình bày về việc trao đổi khóa Diffie-Hellman, họ chỉ cung cấp các đường nét chung về cách các phương thức mật mã học bất đối xứng có thể được xây dựng một cách hợp lý. Họ không đề xuất bất kỳ hàm một chiều nào có thể đáp ứng cụ thể các điều kiện cần thiết cho sự an toàn hợp lý trong các phương thức đó.

Tuy nhiên, một năm sau, việc triển khai thực tế của một phương thức bất đối xứng đã được tìm thấy bởi ba nhà mật mã học và toán học học thuật khác nhau: Ronald Rivest, Adi Shamir, và Leonard Adleman. Hệ mật mã mà họ giới thiệu được biết đến với tên gọi **hệ mật mã RSA** (theo tên họ của họ).

Các hàm cửa hậu được sử dụng trong mật mã học bất đối xứng (và việc trao đổi khóa Diffie Hellman) đều liên quan đến hai vấn đề **khó tính toán** chính: phân tích thừa số nguyên tố và tính toán logarit rời rạc.

**Phân tích thừa số nguyên tố** yêu cầu, như tên gọi, phân rã một số nguyên thành các thừa số nguyên tố của nó. Vấn đề RSA là ví dụ nổi tiếng nhất về một hệ mật mã liên quan đến phân tích thừa số nguyên tố.

Vấn đề **logarit rời rạc** là một vấn đề xảy ra trong các nhóm chu kỳ. Cho một sinh viên trong một nhóm chu kỳ cụ thể, nó yêu cầu tính toán số mũ duy nhất cần thiết để tạo ra một phần tử khác trong nhóm từ sinh viên. 

Các phương thức dựa trên logarit rời rạc dựa vào hai loại nhóm chu kỳ chính: nhóm nhân của các số nguyên và nhóm bao gồm các điểm trên đường cong elliptic. Việc trao đổi khóa Diffie Hellman ban đầu như được trình bày trong “New Directions in Cryptography” hoạt động với một nhóm nhân chu kỳ của các số nguyên. Thuật toán chữ ký số của Bitcoin và phương thức chữ ký Schnorr mới được giới thiệu gần đây (2021) đều dựa trên vấn đề logarit rời rạc cho một nhóm chu kỳ đường cong elliptic cụ thể.

Tiếp theo, chúng ta sẽ chuyển sang cái nhìn tổng quan về bí mật và xác thực trong môi trường bất đối xứng. Tuy nhiên, trước khi làm vậy, chúng ta cần phải lưu ý một chút về lịch sử.

Giờ đây, có vẻ hợp lý khi một nhóm các nhà mật mã học và toán học Anh làm việc cho Cơ quan Trụ sở Giao tiếp Chính phủ (GCHQ) đã độc lập thực hiện các phát hiện nêu trên vài năm trước đó. Nhóm này bao gồm James Ellis, Clifford Cocks, và Malcolm Williamson.

Theo tài khoản của chính họ và của GCHQ, James Ellis là người đầu tiên đề xuất khái niệm về mật mã học khóa công khai vào năm 1969. Có vẻ như Clifford Cocks sau đó đã phát hiện ra hệ thống mật mã RSA vào năm 1973, và Malcolm Williamson khái niệm về việc trao đổi khóa Diffie Hellman vào năm 1974. Tuy nhiên, các phát hiện của họ được cho là không được tiết lộ cho đến năm 1997, do bản chất bí mật của công việc được thực hiện tại GCHQ.

## Mã hóa và xác thực bất đối xứng
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Một cái nhìn tổng quan về mã hóa bất đối xứng với sự giúp đỡ của Bob và Alice được cung cấp trong *Hình 1*.
Alice đầu tiên tạo ra một cặp khóa, bao gồm một khóa công khai (K<sub>P</sub>) và một khóa riêng tư (K<sub>S</sub>), nơi mà “P” trong K<sub>P</sub> đại diện cho “public” (công khai) và “S” trong K<sub>S</sub> đại diện cho “secret” (bí mật). Sau đó, cô ấy phân phối khóa công khai này một cách tự do cho người khác. Chúng ta sẽ quay lại chi tiết của quá trình phân phối này một chút sau. Nhưng bây giờ hãy giả định rằng bất kỳ ai, bao gồm cả Bob, cũng có thể an toàn lấy được khóa công khai K<sub>P</sub> của Alice.
Tại một thời điểm sau, Bob muốn viết một tin nhắn M cho Alice. Tuy nhiên, vì nó bao gồm thông tin nhạy cảm, anh ấy muốn nội dung của nó vẫn là bí mật đối với mọi người trừ Alice. Vì vậy, Bob đầu tiên mã hóa tin nhắn M của mình sử dụng K<sub>P</sub>. Sau đó, anh ấy gửi bản mã hóa C đến Alice, người giải mã C với K<sub>S</sub> để tạo ra tin nhắn gốc M.

*Hình 1: Mã hóa bất đối xứng*

![Hình 1: Mã hóa bất đối xứng](assets/Figure6-1.webp "Hình 1: Mã hóa bất đối xứng")

Bất kỳ kẻ thù nào nghe lén cuộc giao tiếp giữa Bob và Alice cũng có thể quan sát C. Cô ấy cũng biết K<sub>P</sub> và thuật toán mã hóa E(·). Tuy nhiên, quan trọng là, thông tin này không cho phép kẻ tấn công có khả năng giải mã bản mã hóa C. Việc giải mã cụ thể yêu cầu K<sub>S</sub>, mà kẻ tấn công không sở hữu.

Các phương pháp mã hóa đối xứng nói chung cần phải an toàn chống lại kẻ tấn công có thể hợp lệ mã hóa các tin nhắn văn bản (được biết đến với tên là bảo mật chống lại cuộc tấn công bằng văn bản đã chọn). Tuy nhiên, nó không được thiết kế với mục đích rõ ràng là cho phép tạo ra các bản mã hóa hợp lệ như vậy bởi kẻ tấn công hoặc bất kỳ ai khác.

Điều này trái ngược hoàn toàn với một phương pháp mã hóa bất đối xứng, nơi mục đích toàn bộ của nó là cho phép bất kỳ ai, bao gồm cả kẻ tấn công, tạo ra các bản mã hóa hợp lệ. Do đó, các phương pháp mã hóa bất đối xứng có thể được gọi là **mã hóa truy cập nhiều**.

Để hiểu rõ hơn về điều gì đang xảy ra, hãy tưởng tượng thay vì gửi một tin nhắn điện tử, Bob muốn gửi một bức thư vật lý trong bí mật. Một cách để đảm bảo bí mật sẽ là Alice gửi một ổ khóa an toàn cho Bob, nhưng giữ chìa khóa để mở nó. Sau khi viết thư của mình, Bob có thể đặt bức thư vào một hộp và đóng nó lại với ổ khóa của Alice. Sau đó, anh ấy có thể gửi hộp đã khóa với tin nhắn đến Alice, người có chìa khóa để mở nó.

Mặc dù Bob có thể khóa ổ khóa, nhưng không có anh ấy hay bất kỳ người nào khác chặn được hộp có thể mở ổ khóa nếu nó thực sự an toàn. Chỉ có Alice mới có thể mở nó và xem nội dung của bức thư của Bob vì cô ấy có chìa khóa.

Một phương pháp mã hóa bất đối xứng, nói một cách đơn giản, là một phiên bản số hóa của quá trình này. Ổ khóa tương tự như khóa công khai và chìa khóa ổ khóa tương tự như khóa riêng tư. Tuy nhiên, vì ổ khóa là số hóa, nên việc phân phối nó cho bất kỳ ai muốn gửi tin nhắn bí mật cho cô ấy trở nên dễ dàng và không tốn kém.

Đối với xác thực trong cài đặt bất đối xứng, chúng ta sử dụng **chữ ký số**. Do đó, chúng có chức năng giống như mã xác thực tin nhắn trong cài đặt đối xứng. Một cái nhìn tổng quan về chữ ký số được cung cấp trong *Hình 2*.
Bob đầu tiên tạo ra một cặp khóa, bao gồm khóa công khai (K<sub>P</sub>) và khóa riêng tư (K<sub>S</sub>), và phân phối khóa công khai của mình. Khi anh ấy muốn gửi một tin nhắn được xác thực cho Alice, anh ấy đầu tiên lấy tin nhắn M và khóa riêng tư của mình để tạo ra một chữ ký số D. Sau đó, Bob gửi cho Alice tin nhắn của mình cùng với chữ ký số. Alice chèn tin nhắn, khóa công khai, và chữ ký số vào một thuật toán xác minh. Thuật toán này tạo ra kết quả là true cho một chữ ký hợp lệ, hoặc false cho một chữ ký không hợp lệ.
Chữ ký số, như cái tên rõ ràng chỉ ra, là tương đương số hóa của một chữ ký viết tay trên thư từ, hợp đồng, và vân vân. Thực tế, một chữ ký số thường an toàn hơn nhiều. Với một chút nỗ lực, bạn có thể làm giả một chữ ký viết tay; quá trình này trở nên dễ dàng hơn do việc chữ ký viết tay thường không được kiểm tra kỹ lưỡng. Tuy nhiên, một chữ ký số an toàn, giống như một mã xác thực tin nhắn an toàn, là **không thể giả mạo**: tức là, với một hệ thống chữ ký số an toàn, không ai có thể tạo ra một chữ ký cho một tin nhắn mà vượt qua quy trình xác minh, trừ khi họ có khóa riêng tư.

*Hình 2: Xác thực không đối xứng*

![Hình 2: Xác thực không đối xứng](assets/Figure6-2.webp "Hình 2: Xác thực không đối xứng")

Như với mã hóa không đối xứng, chúng ta thấy một sự tương phản thú vị giữa chữ ký số và mã xác thực tin nhắn. Đối với cái sau, thuật toán xác minh chỉ có thể được sử dụng bởi một trong những bên tham gia vào giao tiếp an toàn. Điều này là bởi vì nó yêu cầu một khóa riêng tư. Tuy nhiên, trong môi trường không đối xứng, bất kỳ ai cũng có thể xác minh một chữ ký số S được tạo ra bởi Bob.

Tất cả điều này làm cho chữ ký số trở thành một công cụ cực kỳ mạnh mẽ. Nó tạo nên cơ sở, ví dụ, để tạo chữ ký trên hợp đồng có thể được xác minh cho mục đích pháp lý. Nếu Bob đã tạo một chữ ký trên một hợp đồng trong giao dịch trên, Alice có thể hiện tin nhắn M, hợp đồng, và chữ ký S cho một tòa án. Tòa án, sau đó, có thể xác minh chữ ký sử dụng khóa công khai của Bob.<sup>[5](#footnote5)</sup>

Ví dụ khác, chữ ký số là một khía cạnh quan trọng để bảo mật phần mềm và phân phối cập nhật phần mềm. Loại khả năng xác minh công khai này không bao giờ có thể được tạo ra chỉ sử dụng mã xác thực tin nhắn.

Là một ví dụ cuối cùng về sức mạnh của chữ ký số, hãy xem xét Bitcoin. Một trong những hiểu lầm phổ biến nhất về Bitcoin, đặc biệt là trong truyền thông, là rằng các giao dịch được mã hóa: chúng không phải. Thay vào đó, giao dịch Bitcoin hoạt động với chữ ký số để đảm bảo an ninh.

Bitcoin tồn tại trong các lô gọi là đầu ra giao dịch chưa tiêu (hoặc UTXO). Giả sử bạn nhận được ba khoản thanh toán trên một địa chỉ Bitcoin cụ thể cho mỗi 2 bitcoin. Bạn kỹ thuật không có 6 bitcoin trên địa chỉ đó. Thay vào đó, bạn có ba lô của 2 bitcoin được khóa bởi một vấn đề mật mã liên quan đến địa chỉ đó. Đối với bất kỳ khoản thanh toán nào bạn thực hiện, bạn có thể sử dụng một, hai, hoặc tất cả ba lô này, tùy thuộc vào số lượng bạn cần cho giao dịch.

Bằng chứng sở hữu đối với đầu ra giao dịch chưa tiêu thường được hiển thị qua một hoặc nhiều chữ ký số. Bitcoin hoạt động chính xác bởi vì chữ ký số hợp lệ trên đầu ra giao dịch chưa tiêu là không thể tính toán được để tạo ra, trừ khi bạn sở hữu thông tin bí mật cần thiết để tạo chúng.
Hiện nay, các giao dịch Bitcoin bao gồm một cách minh bạch tất cả thông tin cần được các bên tham gia trong mạng lưới xác minh, như nguồn gốc của các đầu ra giao dịch chưa tiêu được sử dụng trong giao dịch. Mặc dù có thể ẩn một số thông tin đó và vẫn cho phép xác minh (như một số đồng tiền điện tử thay thế như Monero làm), điều này cũng tạo ra các rủi ro an ninh cụ thể.

Đôi khi sự nhầm lẫn phát sinh giữa chữ ký số và chữ ký viết được chụp lại một cách số hóa. Trong trường hợp sau, bạn chụp ảnh chữ ký viết của mình và dán nó vào một tài liệu điện tử như hợp đồng lao động. Tuy nhiên, đây không phải là chữ ký số trong nghĩa mật mã học. Chữ ký số chỉ là một dãy số dài chỉ có thể được tạo ra khi sở hữu khóa riêng.

Giống như trong cài đặt khóa đối xứng, bạn cũng có thể sử dụng mã hóa và xác thực không đối xứng cùng nhau. Các nguyên tắc tương tự áp dụng. Đầu tiên, bạn nên sử dụng các cặp khóa riêng - công khai khác nhau cho việc mã hóa và tạo chữ ký số. Ngoài ra, bạn nên mã hóa một thông điệp trước sau đó mới xác thực nó.

Quan trọng, trong nhiều ứng dụng, mã hóa không đối xứng không được sử dụng xuyên suốt quá trình giao tiếp. Thay vào đó, nó thường chỉ được sử dụng để *trao đổi khóa đối xứng* giữa các bên để họ có thể giao tiếp thực sự.

Điều này xảy ra, chẳng hạn, khi bạn mua hàng trực tuyến. Biết khóa công khai của nhà cung cấp, cô ấy có thể gửi cho bạn các thông điệp đã ký số mà bạn có thể xác minh tính xác thực. Dựa trên cơ sở này, bạn có thể tuân theo một trong nhiều giao thức để trao đổi khóa đối xứng để giao tiếp một cách an toàn.

Lý do chính cho sự phổ biến của cách tiếp cận nêu trên là vì mã hóa không đối xứng kém hiệu quả hơn nhiều so với mã hóa đối xứng trong việc tạo ra một mức độ bảo mật cụ thể. Đây là một lý do tại sao chúng ta vẫn cần mã hóa khóa đối xứng bên cạnh mã hóa công khai. Ngoài ra, mã hóa khóa đối xứng tự nhiên hơn trong các ứng dụng cụ thể như một người dùng máy tính mã hóa dữ liệu của chính họ.

Vậy chữ ký số và mã hóa khóa công khai giải quyết vấn đề phân phối và quản lý khóa như thế nào?

Không có một câu trả lời duy nhất ở đây. Mã hóa không đối xứng là một công cụ và không có một cách duy nhất để sử dụng công cụ đó. Nhưng hãy lấy ví dụ trước đây từ Jim’s Sporting Goods để xem các vấn đề thường được giải quyết như thế nào trong ví dụ này.

Để bắt đầu, Jim’s Sporting Goods có lẽ sẽ tiếp cận một **cơ quan chứng nhận**, tổ chức hỗ trợ trong việc phân phối khóa công khai. Cơ quan chứng nhận sẽ đăng ký một số chi tiết về Jim’s Sporting Goods và cấp cho nó một khóa công khai. Sau đó, nó sẽ gửi cho Jim’s Sporting Goods một chứng chỉ, được biết đến là **chứng chỉ TLS/SSL**, với khóa công khai của Jim’s Sporting Goods được ký số một cách số hóa bằng khóa công khai của chính cơ quan chứng nhận. Như vậy, cơ quan chứng nhận xác nhận rằng một khóa công khai cụ thể thực sự thuộc về Jim’s Sporting Goods.

Chìa khóa để hiểu quy trình này với chứng chỉ TLS/SSL là, mặc dù bạn sẽ chung không có khóa công khai của Jim’s Sporting Goods được lưu trữ ở đâu trên máy tính của mình, nhưng khóa công khai của các cơ quan chứng nhận được công nhận thực sự được lưu trữ trong trình duyệt hoặc hệ điều hành của bạn. Chúng được lưu trữ trong những gì được gọi là **chứng chỉ gốc**.

Do đó, khi Jim’s Sporting Goods cung cấp cho bạn chứng chỉ TLS/SSL của mình, bạn có thể xác minh chữ ký số của cơ quan chứng nhận thông qua một chứng chỉ gốc trong trình duyệt hoặc hệ điều hành của bạn. Nếu chữ ký là hợp lệ, bạn có thể khá chắc chắn rằng khóa công khai trên chứng chỉ thực sự thuộc về Jim’s Sporting Goods. Dựa trên cơ sở này, việc thiết lập một giao thức giao tiếp an toàn với Jim’s Sporting Goods trở nên dễ dàng.
Việc phân phối khóa đã trở nên đơn giản hơn rất nhiều đối với Jim’s Sporting Goods. Không khó để thấy rằng quản lý khóa cũng trở nên đơn giản hơn nhiều. Thay vì phải lưu trữ hàng nghìn khóa, Jim’s Sporting Goods chỉ cần lưu trữ một khóa riêng tư cho phép họ tạo chữ ký cho khóa công khai trên chứng chỉ SSL của mình. Mỗi khi một khách hàng truy cập vào trang web của Jim’s Sporting Goods, họ có thể thiết lập một phiên giao tiếp an toàn từ khóa công khai này. Khách hàng cũng không cần phải lưu trữ bất kỳ thông tin nào (ngoại trừ các khóa công khai của các cơ quan chứng nhận được công nhận trong hệ điều hành và trình duyệt của họ).

## Hàm băm
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Hàm băm là một phần không thể thiếu trong mật mã học. Chúng không phải là các hệ thống đối xứng hay bất đối xứng, nhưng lại thuộc vào một danh mục riêng biệt trong mật mã học.

Chúng ta đã gặp hàm băm trong Chương 4 với việc tạo ra các thông điệp xác thực dựa trên băm. Chúng cũng quan trọng trong bối cảnh của chữ ký số, mặc dù với một lý do hơi khác: Chữ ký số thường được tạo ra trên giá trị băm của một số (đã được mã hóa) thông điệp, thay vì chính (đã được mã hóa) thông điệp đó. Trong phần này, tôi sẽ giới thiệu kỹ hơn về hàm băm.

Hãy bắt đầu với việc định nghĩa một hàm băm. Một **hàm băm** là bất kỳ hàm nào có thể tính toán hiệu quả mà nhận đầu vào có kích thước tùy ý và cho ra kết quả có độ dài cố định.

Một **hàm băm mật mã** chỉ đơn giản là một hàm băm có ích cho các ứng dụng trong mật mã học. Kết quả của một hàm băm mật mã thường được gọi là **băm**, **giá trị băm**, hoặc **tóm tắt thông điệp**.

Trong bối cảnh của mật mã học, một “hàm băm” thường đề cập đến một hàm băm mật mã. Tôi sẽ áp dụng thực hành đó từ đây trở đi.

Một ví dụ về hàm băm phổ biến là **SHA-256** (secure hash algorithm 256). Bất kể kích thước của đầu vào (ví dụ, 15 bit, 100 bit, hoặc 10,000 bit), hàm này sẽ cho ra một giá trị băm 256-bit. Dưới đây bạn có thể thấy một vài ví dụ về kết quả của hàm SHA-256.

* “Hello”: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
* “52398”: a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90
* “Cryptography is fun”: 3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c

Tất cả các kết quả đều chính xác là 256 bit được viết ra dưới dạng thập lục phân (mỗi chữ số thập lục phân có thể được biểu diễn bằng bốn chữ số nhị phân). Vì vậy, ngay cả khi bạn đã nhập toàn bộ cuốn sách *Chúa tể của những chiếc nhẫn* của Tolkien vào hàm SHA-256, kết quả vẫn sẽ là 256 bit.

Hàm băm như SHA-256 được sử dụng cho các mục đích khác nhau trong mật mã học. Các tính chất cần thiết từ một hàm băm thực sự phụ thuộc vào bối cảnh của một ứng dụng cụ thể. Có hai tính chất chính thường được mong muốn từ hàm băm trong mật mã học:

1.	Kháng va chạm
2.	Ẩn giấu

Một hàm băm H được cho là **kháng va chạm** nếu việc tìm hai giá trị, x và y, sao cho x ≠ y, nhưng H(x) = H(y) là không khả thi.
Các hàm băm chống va chạm rất quan trọng, ví dụ, trong việc xác minh phần mềm. Giả sử bạn muốn tải xuống phiên bản Windows của Bitcoin Core 0.21.0 (một ứng dụng máy chủ để xử lý lưu lượng mạng Bitcoin). Các bước chính bạn cần thực hiện để xác minh tính hợp lệ của phần mềm, như sau:
1. Bạn cần tải xuống và nhập khóa công khai của một hoặc nhiều người đóng góp Bitcoin Core vào phần mềm có thể xác minh chữ ký số (ví dụ: Kleopetra). Bạn có thể tìm thấy các khóa công khai này [tại đây](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Được khuyến nghị rằng bạn nên xác minh phần mềm Bitcoin Core với khóa công khai từ nhiều người đóng góp.
2. Tiếp theo, bạn cần xác minh các khóa công khai mà bạn đã nhập. Ít nhất một bước bạn nên thực hiện là xác minh rằng các khóa công khai bạn tìm thấy giống như được công bố ở các vị trí khác nhau. Bạn có thể, ví dụ, tham khảo các trang web cá nhân, trang Twitter, hoặc trang Github của những người mà bạn đã nhập khóa công khai. Thông thường, việc so sánh này được thực hiện bằng cách so sánh một hash ngắn của khóa công khai được biết đến như là dấu vân tay.
3. Tiếp theo, bạn cần tải xuống tệp thực thi cho Bitcoin Core từ [website](www.bitcoincore.org) của họ. Sẽ có các gói phần mềm dành cho hệ điều hành Linux, Windows, và MAC.
4. Tiếp theo, bạn phải tìm hai tệp phát hành. Tệp đầu tiên chứa hash SHA-256 chính thức cho tệp thực thi bạn đã tải xuống cùng với các hash cho tất cả các gói khác đã được phát hành. Một tệp phát hành khác sẽ chứa các chữ ký từ nhiều người đóng góp trên tệp phát hành với các hash gói. Cả hai tệp phát hành này nên được đặt trên website của Bitcoin Core.
5. Tiếp theo, bạn cần tính toán hash SHA-256 của tệp thực thi bạn đã tải xuống từ website Bitcoin Core trên máy tính của mình. Sau đó, bạn so sánh kết quả này với hash gói chính thức cho tệp thực thi. Chúng nên giống nhau.
6. Cuối cùng, bạn cần xác minh rằng một hoặc nhiều chữ ký số trên tệp phát hành với các hash gói chính thức thực sự tương ứng với một hoặc nhiều khóa công khai bạn đã nhập (các bản phát hành của Bitcoin Core không luôn được ký bởi tất cả mọi người). Bạn có thể làm điều này với một ứng dụng như Kleopetra.

Quy trình xác minh phần mềm này có hai lợi ích chính. Đầu tiên, nó đảm bảo rằng không có lỗi trong quá trình truyền tải khi tải xuống từ website của Bitcoin Core. Thứ hai, nó đảm bảo rằng không có kẻ tấn công nào có thể khiến bạn tải xuống mã độc hại đã được sửa đổi, bằng cách hack website Bitcoin Core hoặc bằng cách chặn lưu lượng truy cập.

Quy trình xác minh phần mềm trên bảo vệ chống lại những vấn đề này như thế nào?

Nếu bạn đã kiểm tra cẩn thận các khóa công khai bạn đã nhập, thì bạn có thể khá chắc chắn rằng những khóa này thực sự thuộc về họ và không bị xâm phạm. Vì chữ ký số có tính không thể giả mạo tồn tại, bạn biết rằng chỉ những người đóng góp này mới có thể tạo ra chữ ký số trên các hash gói chính thức trên tệp phát hành.

Giả sử các chữ ký trên tệp phát hành bạn đã tải xuống được kiểm tra. Bây giờ bạn có thể so sánh giá trị hash bạn đã tính toán tại chỗ cho tệp thực thi Windows bạn đã tải xuống với giá trị được bao gồm trong tệp phát hành đã được ký đúng cách. Như bạn biết hàm hash SHA-256 có khả năng chống va chạm, một sự trùng khớp có nghĩa là tệp thực thi của bạn chính xác giống như tệp thực thi chính thức.

Bây giờ chúng ta hãy chuyển sang tính chất thứ hai phổ biến của các hàm băm: tính ẩn giấu. Bất kỳ hàm băm H nào được cho là có tính chất ẩn giấu, nếu, đối với bất kỳ x nào được chọn ngẫu nhiên từ một phạm vi rất lớn, thì việc tìm x khi chỉ biết H(x) là không khả thi.
Dưới đây, bạn có thể thấy đầu ra SHA-256 của một thông điệp mà tôi đã viết. Để đảm bảo đủ tính ngẫu nhiên, thông điệp đã bao gồm một chuỗi ký tự được tạo ngẫu nhiên ở cuối. Vì SHA-256 có tính chất ẩn danh, không ai có thể giải mã được thông điệp này.
* b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded

Nhưng tôi sẽ không để bạn chờ đợi cho đến khi SHA-256 trở nên yếu đi. Thông điệp gốc mà tôi đã viết như sau:

* “Đây là một thông điệp rất ngẫu nhiên, hoặc cũng có thể coi là ngẫu nhiên. Phần đầu không phải, nhưng tôi sẽ kết thúc với một số ký tự tương đối ngẫu nhiên để đảm bảo một thông điệp không thể đoán trước. XLWz4dVG3BxUWm7zQ9qS”.

Một cách phổ biến mà các hàm băm với tính chất ẩn danh được sử dụng là trong quản lý mật khẩu (khả năng chống va chạm cũng quan trọng đối với ứng dụng này). Bất kỳ dịch vụ dựa trên tài khoản trực tuyến đáng tin cậy nào như Facebook hoặc Google sẽ không lưu trữ trực tiếp mật khẩu của bạn để quản lý quyền truy cập vào tài khoản. Thay vào đó, họ chỉ lưu trữ một bản băm của mật khẩu đó. Mỗi lần bạn nhập mật khẩu trên trình duyệt, một bản băm sẽ được tính toán trước. Chỉ có bản băm đó được gửi đến máy chủ của nhà cung cấp dịch vụ và so sánh với bản băm được lưu trữ trong cơ sở dữ liệu phía sau. Tính chất ẩn danh có thể giúp đảm bảo rằng kẻ tấn công không thể khôi phục mật khẩu từ giá trị băm.

Quản lý mật khẩu qua băm, tất nhiên, chỉ hiệu quả nếu người dùng thực sự chọn mật khẩu khó. Tính chất ẩn danh giả định rằng x được chọn một cách ngẫu nhiên từ một phạm vi rất lớn. Chọn mật khẩu như “1234”, “mypassword”, hoặc ngày sinh của bạn sẽ không cung cấp bất kỳ sự bảo mật thực sự nào. Danh sách dài các mật khẩu phổ biến và bản băm của chúng tồn tại mà kẻ tấn công có thể tận dụng nếu họ từng có được bản băm của mật khẩu của bạn. Các loại tấn công này được biết đến là **tấn công từ điển**. Nếu kẻ tấn công biết một số chi tiết cá nhân của bạn, họ cũng có thể thử một số đoán mò có thông tin. Do đó, bạn luôn cần mật khẩu dài, an toàn (tốt nhất là chuỗi ký tự ngẫu nhiên dài từ một trình quản lý mật khẩu).

Đôi khi một ứng dụng có thể cần một hàm băm có cả khả năng chống va chạm và ẩn danh. Nhưng chắc chắn không phải lúc nào cũng vậy. Quy trình xác minh phần mềm mà chúng ta đã thảo luận, ví dụ, chỉ yêu cầu hàm băm hiển thị khả năng chống va chạm, ẩn danh không quan trọng.

Mặc dù khả năng chống va chạm và ẩn danh là các tính chất chính được tìm kiếm của hàm băm trong mật mã học, trong một số ứng dụng, các loại tính chất khác cũng có thể mong muốn.

### Ghi chú
[^1]: Whitfield Diffie và Martin Hellman, “New directions in cryptography,” *IEEE Transactions on Information Theory* IT-22 (1976), tr. 644–654, tại tr. 644 [^1].

[^2]: Ralph Merkle cũng thảo luận về một giao thức trao đổi khóa trong “Secure communications over insecure channels”, *Communications of the Association for Computing Machinery*, 21 (1978), 294–99. Mặc dù Merkle đã nộp bài này trước bài của Diffie và Hellman, nhưng nó được xuất bản sau. Giải pháp của Merkle không được bảo mật theo cấp số nhân, không giống như Diffie-Hellman [^2].

[^3]: Ron Rivest, Adi Shamir, và Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, *Communications of the Association for Computing Machinery*, 21 (1978), tr. 120–26 [^3].

[^4]: Một lịch sử tốt về những phát hiện này được cung cấp bởi Simon Singh, *The Code Book*, Fourth Estate (London, 1999), Chương 6 [^4].
[^5]: Mọi giải pháp nhằm đạt được tính không chối cãi, chủ đề khác mà chúng ta đã thảo luận trong *Chương 1*, sẽ cần phải dựa trên việc sử dụng chữ ký số [^5].
[^6]: Thuật ngữ "ẩn giấu" không phải là ngôn ngữ phổ thông, nhưng được lấy cụ thể từ Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, và Steven Goldfeder, *Bitcoin và Công nghệ Tiền mã hóa*, Nhà Xuất Bản Đại Học Princeton (Princeton, 2016), Chương 1 [^6].

# Hệ mật mã RSA
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

Trong khi mật mã đối xứng thường khá trực quan đối với hầu hết mọi người, điều này thường không đúng với mật mã bất đối xứng. Mặc dù bạn có thể thoải mái với mô tả cấp cao được đề cập trong các phần trước, bạn có thể tự hỏi chính xác hàm một chiều là gì và chúng được sử dụng như thế nào để xây dựng các giải pháp bất đối xứng.

Trong chương này, tôi sẽ làm sáng tỏ một số bí ẩn xung quanh mật mã bất đối xứng, bằng cách xem xét sâu hơn vào một ví dụ cụ thể, đó là hệ mật mã RSA. Trong phần đầu tiên, tôi sẽ giới thiệu về vấn đề phân tích nhân tử mà vấn đề RSA dựa trên. Sau đó, tôi sẽ trình bày một số kết quả chính từ lý thuyết số. Trong phần cuối, chúng ta sẽ kết hợp thông tin này để giải thích vấn đề RSA, và làm thế nào nó có thể được sử dụng để tạo ra các giải pháp mật mã bất đối xứng.

Việc thêm chiều sâu vào cuộc thảo luận của chúng ta không phải là một nhiệm vụ dễ dàng. Nó đòi hỏi phải giới thiệu khá nhiều định lý và đề xuất lý thuyết số. Nhưng đừng để toán học làm bạn nản lòng. Việc thảo luận qua vấn đề này sẽ cải thiện đáng kể sự hiểu biết của bạn về những gì nằm dưới mật mã bất đối xứng và là một khoản đầu tư đáng giá.

Bây giờ, hãy chúng ta quay lại với vấn đề phân tích nhân tử.

## Vấn đề phân tích nhân tử
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Bất cứ khi nào bạn nhân hai số, giả sử là a và b, chúng ta gọi các số a và b là **nhân tử**, và kết quả là **tích**. Việc cố gắng viết một số N thành phép nhân của hai hoặc nhiều nhân tử được gọi là **phân tích nhân tử** hoặc **phân tích**.<sup>[1](#footnote1)</sup> Bạn có thể gọi bất kỳ vấn đề nào đòi hỏi điều này là một **vấn đề phân tích nhân tử**.

Khoảng 2,500 năm trước, nhà toán học Hy Lạp Euclid của Alexandria đã phát hiện ra một định lý quan trọng về phân tích nhân tử của các số nguyên. Nó thường được gọi là **định lý phân tích nhân tử duy nhất** và tuyên bố như sau:

*Định lý 1*. Mọi số nguyên N lớn hơn 1 đều là một số nguyên tố, hoặc có thể được biểu diễn dưới dạng tích của các thừa số nguyên tố.

Tất cả những gì phần sau của tuyên bố này có nghĩa là bạn có thể lấy bất kỳ số nguyên không phải là số nguyên tố nào lớn hơn 1, và viết nó ra dưới dạng phép nhân của các số nguyên tố. Dưới đây là một số ví dụ về các số nguyên không phải là số nguyên tố được viết dưới dạng tích của các thừa số nguyên tố.

* 18 = 2 • 3 • 3 = 2 • 3<sup>2</sup>
* 84 = 2 • 2 • 3 • 7 = 2<sup>2</sup> • 3 • 7
* 144 = 2 • 2 • 2 • 2 • 3 • 3 = 2<sup>4</sup> • 3<sup>2</sup>
Đối với cả ba số nguyên trên, việc tính toán các thừa số nguyên tố của chúng tương đối dễ dàng, ngay cả khi bạn chỉ được cho N. Bạn bắt đầu với số nguyên tố nhỏ nhất, cụ thể là 2, và xem số lần số nguyên N chia hết cho nó. Sau đó, bạn chuyển sang kiểm tra tính chia hết của N cho 3, 5, 7, và cứ thế tiếp tục. Bạn tiếp tục quá trình này cho đến khi số nguyên N của bạn được viết dưới dạng sản phẩm của chỉ các số nguyên tố.

Lấy ví dụ, số nguyên 84. Dưới đây bạn có thể thấy quá trình xác định các thừa số nguyên tố của nó. Tại mỗi bước, chúng tôi lấy ra thừa số nguyên tố nhỏ nhất còn lại (ở bên trái) và xác định số dư cần được phân tích. Chúng tôi tiếp tục cho đến khi số dư cũng là một số nguyên tố. Tại mỗi bước, phân tích hiện tại của 84 được hiển thị ở phía bên phải.

* Thừa số nguyên tố = 2: số dư = 42 	(84 = 2 • 42)
* Thừa số nguyên tố = 2: số dư = 21 	(84 = 2 • 2 • 21)
* Thừa số nguyên tố = 3: số dư = 7 		(84 = 2 • 2 • 3 • 7)
* Vì 7 là một số nguyên tố, kết quả là 2 • 2 • 3 • 7, hoặc 2<sup>2</sup> • 3 • 7.

Giả sử bây giờ N rất lớn. Việc giảm N thành các thừa số nguyên tố của nó sẽ khó khăn như thế nào?

Điều đó thực sự phụ thuộc vào N. Giả sử, ví dụ, N là 50,450,400. Mặc dù con số này trông đáng sợ, nhưng các phép tính không quá phức tạp và có thể dễ dàng thực hiện bằng tay. Như trên, bạn chỉ cần bắt đầu với 2 và tiếp tục công việc. Dưới đây, bạn có thể thấy kết quả của quá trình này một cách tương tự như trên.

* 2: 25,225,200 	(50,450,400 = 2 • 25,225,200)  
* 2: 12,612,600 	(50,450,400 = 2<sup>2</sup> • 12,612,600)  
* 2: 6,306,300 		(50,450,400 = 2<sup>3</sup> • 6,306,300)  
* 2: 3,153,150 		(50,450,400 = 2<sup>4</sup> • 3,153,150)  
* 2: 1,576,575 		(50,450,400 = 2<sup>5</sup> • 1,576,575)  
* 3: 525,525 		(50,450,400 = 2<sup>5</sup> • 3 • 525,525)
* 3: 175,175 		(50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 175,175)
* 5: 35,035 		(50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5 • 35,035)
* 5: 7,007		    (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7,007)
* 7: 1,001 (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7 • 1,001)
* 7: 143 (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 143)
* 11: 13 (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13)
* Vì 13 là một số nguyên tố, kết quả là 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13.

Việc giải quyết vấn đề này bằng tay mất một chút thời gian. Một máy tính, tất nhiên, có thể làm tất cả những điều này chỉ trong một phần nhỏ của giây. Thực tế, máy tính thường xuyên có thể phân tích thừa số của các số nguyên cực lớn chỉ trong một phần nhỏ của giây.

Tuy nhiên, có một số ngoại lệ. Giả sử rằng chúng ta đầu tiên chọn ngẫu nhiên hai số nguyên tố cực lớn. Thông thường, người ta gọi chúng là p và q, và tôi sẽ tuân theo quy ước đó ở đây.

Cụ thể, giả sử p và q đều là các số nguyên tố 1024-bit, và chúng thực sự cần ít nhất 1024 bit để được biểu diễn (vì vậy bit đầu tiên phải là 1). Ví dụ, 37 không thể là một trong những số nguyên tố đó. Bạn chắc chắn có thể biểu diễn 37 bằng 1024 bit. Nhưng rõ ràng *bạn không cần* nhiều bit như vậy để biểu diễn nó. Bạn có thể biểu diễn 37 bằng bất kỳ chuỗi nào có 6 bit trở lên. (Trong 6 bit, 37 sẽ được biểu diễn là 100101).

Quan trọng là phải nhận thức được p và q lớn như thế nào nếu được chọn dưới các điều kiện trên. Là một ví dụ, tôi đã chọn một số nguyên tố ngẫu nhiên cần ít nhất 1024 bit để biểu diễn dưới đây.

* 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589

Giả sử bây giờ sau khi chọn ngẫu nhiên các số nguyên tố p và q, chúng ta nhân chúng lại với nhau để thu được một số nguyên N. Số nguyên này, do đó, là một số 2048 bit, yêu cầu ít nhất 2048 bit để biểu diễn. Nó lớn hơn nhiều so với p hoặc q.
Giả sử bạn chỉ đưa cho máy tính một số N, và yêu cầu nó tìm hai thừa số nguyên tố 1024 bit của N. Khả năng máy tính tìm ra p và q là cực kỳ nhỏ. Bạn có thể nói rằng việc này là không thể cho mọi mục đích thực tế. Điều này vẫn đúng, ngay cả khi bạn sử dụng một siêu máy tính hoặc thậm chí là một mạng lưới các siêu máy tính.

Để bắt đầu, giả sử rằng máy tính cố gắng giải quyết vấn đề bằng cách lặp qua các số 1024 bit, kiểm tra trong mỗi trường hợp xem chúng có phải là số nguyên tố và có phải là thừa số của N không. Tập hợp các số nguyên tố cần được kiểm tra sau đó là khoảng 1.265 • 10<sup>305</sup>.<sup>[2](#footnote2)</sup>

Ngay cả khi bạn sử dụng tất cả các máy tính trên hành tinh và khiến chúng cố gắng tìm và kiểm tra các số nguyên tố 1024-bit theo cách này, cơ hội 1 trong một tỷ để thành công tìm ra một thừa số nguyên tố của N sẽ yêu cầu một khoảng thời gian tính toán dài hơn nhiều so với tuổi của Vũ trụ.

Bây giờ trên thực tế, máy tính có thể làm tốt hơn so với quy trình thô sơ vừa được mô tả. Có một số thuật toán mà máy tính có thể áp dụng để đến với việc phân tích thừa số nhanh hơn. Tuy nhiên, điểm quan trọng là, ngay cả khi sử dụng những thuật toán hiệu quả hơn này, nhiệm vụ của máy tính vẫn là không khả thi về mặt tính toán.<sup>[3](#footnote3)</sup>

Quan trọng là, khó khăn của việc phân tích thừa số dưới các điều kiện vừa được mô tả dựa trên giả định rằng không có thuật toán hiệu quả về mặt tính toán để tính toán các thừa số nguyên tố. Chúng ta không thể chứng minh rằng một thuật toán hiệu quả không tồn tại. Tuy nhiên, giả định này rất hợp lý: mặc dù đã có nhiều nỗ lực kéo dài hàng trăm năm, chúng ta vẫn chưa tìm ra một thuật toán hiệu quả về mặt tính toán như vậy.

Do đó, vấn đề phân tích thừa số, dưới một số hoàn cảnh, có thể được giả định một cách hợp lý là một vấn đề khó. Cụ thể, khi p và q là các số nguyên tố rất lớn, sản phẩm N của chúng không khó để tính toán; nhưng việc phân tích thừa số chỉ với N là gần như không thể.

## Kết quả lý thuyết số
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Thật không may, vấn đề phân tích thừa số không thể được sử dụng trực tiếp cho các lược đồ mật mã bất đối xứng. Tuy nhiên, chúng ta có thể sử dụng một vấn đề phức tạp hơn nhưng liên quan để đạt được hiệu quả này: vấn đề RSA.

Để hiểu vấn đề RSA, chúng ta cần hiểu một số định lý và đề xuất từ lý thuyết số. Những nội dung này được trình bày trong phần này qua ba tiểu mục: (1) thứ tự của N, (2) tính khả nghịch modulo N, và (3) định lý Euler.

Một số nội dung trong ba tiểu mục này đã được giới thiệu trong *Chương 3*. Nhưng tôi sẽ ở đây tái bản nội dung đó cho tiện lợi.

### Thứ tự của N

Một số nguyên a là **coprime** hoặc một **số nguyên tố cùng nhau** với một số nguyên N, nếu ước số chung lớn nhất giữa chúng là 1. Mặc dù 1 theo quy ước không phải là một số nguyên tố, nhưng nó là một số nguyên tố cùng nhau của mọi số nguyên (như là – 1).

Ví dụ, xem xét trường hợp khi a = 18 và N = 37. Rõ ràng chúng là coprimes. Số nguyên lớn nhất chia hết cho cả 18 và 37 là 1. Ngược lại, xem xét trường hợp khi a = 42 và N = 16. Rõ ràng chúng không phải là coprimes. Cả hai số đều chia hết cho 2, số này lớn hơn 1.
Chúng ta có thể định nghĩa cấp bậc của N như sau. Giả sử N là một số nguyên lớn hơn 1. **Cấp bậc của N** là số lượng tất cả các số nguyên tố cùng nhau với N sao cho với mỗi số nguyên tố cùng nhau a, điều kiện sau được thỏa mãn: 1 ≤ a < N.
Ví dụ, nếu N = 12, thì 1, 5, 7 và 11 là những số nguyên tố cùng nhau duy nhất đáp ứng yêu cầu trên. Do đó, cấp bậc của 12 bằng 4.

Giả sử N là một số nguyên tố. Khi đó, bất kỳ số nguyên nào nhỏ hơn N nhưng lớn hơn hoặc bằng 1 đều là số nguyên tố cùng nhau với nó. Điều này bao gồm tất cả các phần tử trong tập hợp sau: {1,2,3….,N – 1}. Do đó, khi N là số nguyên tố, cấp bậc của N là N – 1. Điều này được nêu trong đề xuất 1, nơi φ(N) biểu thị cấp bậc của N.

**Đề xuất 1**. φ(N) = N – 1 khi N là số nguyên tố

Giả sử N không phải là số nguyên tố. Bạn có thể, sau đó, tính toán cấp bậc của nó sử dụng **Hàm Phi của Euler**. Mặc dù việc tính toán cấp bậc của một số nguyên nhỏ tương đối đơn giản, Hàm Phi của Euler trở nên đặc biệt quan trọng đối với các số nguyên lớn hơn. Đề xuất của Hàm Phi của Euler được nêu dưới đây.

*Định lý 2*. Cho N bằng p<sub>1</sub><sup>e_1</sup> • p<sub>2</sub><sup>e_2</sup> • … • p<sub>i</sub><sup>e_i</sup> • … • p<sub>n</sub><sup>e_n</sup>, nơi tập hợp {p<sub>i</sub>} bao gồm tất cả các yếu tố nguyên tố phân biệt của N và mỗi e_i chỉ ra số lần yếu tố nguyên tố p<sub>i</sub> xuất hiện cho N. Khi đó, φ(N) = p<sub>1</sub><sup>e_1 - 1</sup> • (p<sub>1</sub> - 1) • p<sub>2</sub><sup>e_2 - 1</sup> • (p<sub>2</sub> - 1) • … • p<sub>n</sub><sup>e_n - 1</sup> • (p<sub>n</sub> - 1).

*Định lý 2* cho thấy một khi bạn đã phân tích bất kỳ N không phải là số nguyên tố nào thành các yếu tố nguyên tố phân biệt của nó, việc tính toán cấp bậc của N trở nên dễ dàng.

Ví dụ, giả sử N = 270. Rõ ràng đây không phải là số nguyên tố. Phân tích N thành các yếu tố nguyên tố của nó cho biểu thức: 2 • 3<sup>3</sup> • 5. Theo Hàm Phi của Euler, cấp bậc của N sau đó như sau:

* φ(N) = 2<sup>1 – 1</sup> (2 – 1) + 3<sup>3 – 1</sup> (3 – 1) + 5<sup>1 – 1</sup> (5 – 1) = 1 (1) + 9 (2) + 1 (4) = 1 + 18 + 4 = 23
Giả sử tiếp theo rằng N là tích của hai số nguyên tố, p và q. *Định lý 2* ở trên, vậy, khẳng định rằng thứ tự của N như sau: p<sup>1 – 1</sup> (p – 1) x q<sup>1 – 1</sup> (q – 1) = (p – 1) x (q – 1). Đây là một kết quả chính cho vấn đề RSA nói riêng, và được trình bày trong *Đề xuất 2* dưới đây.
*Đề xuất 2*. Nếu N là tích của hai số nguyên tố, p và q, thứ tự của N là tích (p – 1) x (q – 1).

Để minh họa, giả sử rằng N = 119. Số nguyên này có thể được phân tích thành hai số nguyên tố, cụ thể là 7 và 17. Do đó, hàm Phi của Euler gợi ý rằng thứ tự của 119 như sau:

* φ(119) = (7 – 1) • (17 – 1) = 6 • 16 = 96.

Nói cách khác, số nguyên 119 có 96 số nguyên tố cùng nhau trong phạm vi từ 1 đến 119. Thực tế, tập hợp này bao gồm tất cả các số nguyên từ 1 đến 119, không phải là bội số của 7 hoặc 17.

Từ đây, hãy ký hiệu tập hợp các số nguyên tố cùng nhau xác định thứ tự của N là **C<sub>N</sub>**. Đối với ví dụ của chúng ta khi N = 119, tập hợp **C<sub>119</sub>** quá lớn để liệt kê đầy đủ. Nhưng một số phần tử như sau: **C<sub>119</sub>** = {1,2,…,6,8…,13,15,16,18,…,33,35…,96}.

### Tính Khả Nghịch modulo N

Chúng ta có thể nói rằng một số nguyên a là **khả nghịch modulo N**, nếu tồn tại ít nhất một số nguyên b sao cho a x b modulo N = 1 modulo N. Bất kỳ số nguyên b nào như vậy được gọi là **nghịch đảo** (hoặc **nghịch đảo nhân**) của a cho phép giảm modulo N.

Giả sử, ví dụ, rằng a = 5 và N = 11. Có nhiều số nguyên mà bạn có thể nhân với 5, sao cho 5 x b mod 11 = 1 mod 11. Xem xét, ví dụ, các số nguyên 20 và 31. Dễ dàng thấy rằng cả hai số nguyên này là nghịch đảo của 5 cho giảm modulo 11.

* 5 x 20 mod 11 = 100 mod 11 = 1 mod 11
* 5 x 31 mod 11 = 155 mod 11 = 1 mod 11

Mặc dù 5 có nhiều nghịch đảo giảm modulo 11, bạn có thể chứng minh rằng chỉ tồn tại một nghịch đảo dương duy nhất của 5 nhỏ hơn 11. Thực tế, điều này không độc đáo cho ví dụ cụ thể của chúng ta, mà là một kết quả chung.

*Đề xuất 3*. Nếu số nguyên a là khả nghịch modulo N, thì phải có chính xác một nghịch đảo dương của a nhỏ hơn N. (Vậy, nghịch đảo duy nhất này của a phải đến từ tập hợp {1,…,N – 1}).
Hãy ký hiệu nghịch đảo duy nhất của a từ Đề xuất 3 là a<sup>-1</sup>. Trong trường hợp khi a = 5 và N = 11, bạn có thể thấy rằng a<sup>-1</sup> = 9, bởi vì 5 x 9 mod 11 = 45 mod 11 = 1 mod 11.
Lưu ý rằng bạn cũng có thể thu được giá trị 9 cho a<sup>-1</sup> trong ví dụ của chúng ta bằng cách đơn giản là giảm bất kỳ nghịch đảo nào khác của a bằng modulo 11. Ví dụ, 20 mod 11 = 31 mod 11 = 9 mod 11. Vì vậy, bất cứ khi nào một số nguyên a > N có thể nghịch đảo modulo N, thì a mod N cũng phải có thể nghịch đảo modulo N.

Không nhất thiết là trường hợp nghịch đảo của a tồn tại giảm modulo N. Giả sử, ví dụ, rằng a = 2 và N = 8. Không có b, hoặc cụ thể là bất kỳ a<sup>-1</sup> nào, sao cho 2 x b mod 8 = 1 mod 8. Điều này là bởi vì bất kỳ giá trị nào của b cũng sẽ luôn tạo ra một bội số của 2, vì vậy không có phép chia nào cho 8 có thể tạo ra một số dư bằng 1.

Làm thế nào chúng ta biết chắc chắn nếu một số nguyên a có nghịch đảo cho một N cho trước? Như bạn có thể đã nhận thấy trong ví dụ trên, ước số chung lớn nhất giữa 2 và 8 cao hơn 1, cụ thể là 2. Và điều này thực sự minh họa cho kết quả tổng quát sau:

*Đề xuất 4*. Một nghịch đảo tồn tại của một số nguyên a giảm modulo N, và cụ thể là một nghịch đảo dương duy nhất nhỏ hơn N, nếu và chỉ nếu ước số chung lớn nhất giữa a và N là 1 (nghĩa là, nếu chúng là số nguyên tố cùng nhau).

Trong trường hợp khi a = 5 và N = 11, chúng ta kết luận rằng a<sup>-1</sup> = 9, bởi vì 5 x 9 mod 11 = 45 mod 11 = 1 mod 11. Điều quan trọng cần lưu ý là điều ngược lại cũng đúng. Đó là, khi a = 9 và N = 11, thì a<sup>-1</sup> = 5.

### Định lý Euler

Trước khi chuyển sang vấn đề RSA, chúng ta cần hiểu thêm một định lý quan trọng nữa, đó là **Định lý Euler**. Nó tuyên bố như sau:

*Định lý 3*. Giả sử hai số nguyên a và N là số nguyên tố cùng nhau. Khi đó, a<sup>φ(N)</sup> mod N = 1 mod N.

Đây là một kết quả đáng chú ý, nhưng hơi khó hiểu lúc đầu. Hãy xem xét một ví dụ để hiểu nó.

Giả sử rằng a = 5 và N = 7. Đây thực sự là số nguyên tố cùng nhau như Định lý Euler yêu cầu. Chúng ta biết rằng thứ tự của 7 bằng 6, bởi vì 7 là một số nguyên tố (xem **Đề xuất 1**).

Bây giờ, Định lý Euler tuyên bố rằng 5<sup>6</sup> mod 7 phải bằng 1 mod 7. Dưới đây là các phép tính để chứng minh điều này là đúng.

* 5<sup>6</sup> mod 7 = 15,625 mod 7 = 1 mod N

Số nguyên 7 chia vào 15,624 tổng cộng 2,233 lần. Do đó, số dư của việc chia 16,625 cho 7 là 1.

Tiếp theo, sử dụng hàm Phi của Euler, *Định lý 2*, bạn có thể suy ra *Đề xuất 5* dưới đây.
*Đề xuất 5*. φ(a • b) = φ(a) • φ(b) cho bất kỳ số nguyên dương nào a và b.
Chúng tôi sẽ không giải thích tại sao lại như vậy. Nhưng chỉ lưu ý rằng bạn đã thấy bằng chứng của đề xuất này qua việc φ(p • q) = φ(p) • φ(q) = (p – 1) • (q – 1) khi p và q là các số nguyên tố, như đã nêu trong *Đề xuất 2*.

Định lý Euler kết hợp với *Đề xuất 5* có những hàm ý quan trọng. Hãy xem điều gì xảy ra, chẳng hạn, trong các biểu thức dưới đây, nơi a và N là các số nguyên tố cùng nhau.

* a<sup>2 • φ(N)</sup> mod N = a<sup>φ(N)</sup> • a<sup>φ(N)</sup> mod N = 1 • 1 mod N = 1 mod N
* a<sup>φ(N) + 1</sup> mod N = a<sup>φ(N)</sup> • a<sup>1</sup> mod N = 1 • a<sup>1</sup> mod N = a mod N
* a<sup>8 • φ(N) + 3</sup> mod N = a<sup>8 • φ(N)</sup> • a<sup>3</sup>  mod N = 1 • a<sup>3</sup>  mod N = a<sup>3</sup>  mod N

Do đó, sự kết hợp của định lý Euler và *Đề xuất 5* cho phép chúng ta tính toán đơn giản một số biểu thức. Nói chung, chúng ta có thể tóm tắt hiểu biết như trong *Đề xuất 6*.

*Đề xuất 6*. a<sup>x</sup> mod N = a<sup>x mod φ(N)</sup>

Bây giờ chúng ta phải kết hợp mọi thứ trong một bước cuối cùng khéo léo.

Giống như N có một thứ tự φ(N) bao gồm các phần tử của tập hợp **C<sub>N</sub>**, chúng ta biết rằng số nguyên φ(N) phải lần lượt cũng có một thứ tự và một tập hợp các số nguyên tố cùng nhau. Hãy đặt φ(N) = R. Sau đó, chúng ta biết rằng cũng có một giá trị cho φ(R) và một tập hợp các số nguyên tố cùng nhau **C<sub>R</sub>**.

Giả sử rằng bây giờ chúng ta chọn một số nguyên e từ tập hợp **C<sub>R</sub>**. Chúng ta biết từ *Đề xuất 3* rằng số nguyên e này chỉ có một nghịch đảo dương duy nhất nhỏ hơn R. Điều này có nghĩa là, e có một nghịch đảo duy nhất từ tập hợp **C<sub>R</sub>**. Hãy gọi nghịch đảo này là d. Dựa vào định nghĩa của một nghịch đảo, điều này có nghĩa là e • d = 1 mod R.

Chúng ta có thể sử dụng kết quả này để đưa ra một phát biểu về số nguyên N ban đầu của chúng ta. Điều này được tóm tắt trong *Đề xuất 7*.

*Đề xuất 7*. Giả sử rằng e • d mod φ(N) = 1 mod φ(N). Sau đó, đối với bất kỳ phần tử nào a của tập hợp **C<sub>N</sub>** phải là a<sup>e • d mod φ(N)</sup> = a<sup>1 mod φ(N)</sup> = a mod N.

Bây giờ chúng ta có tất cả các kết quả lý thuyết số cần thiết để trình bày rõ ràng vấn đề RSA.


## Hệ mật mã RSA
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>
Chúng ta giờ đây đã sẵn sàng để trình bày vấn đề RSA. Giả sử bạn tạo ra một tập hợp các biến bao gồm p, q, N, φ(N), e, d, và y. Gọi tập hợp này là Π. Nó được tạo ra như sau:
1. Tạo hai số nguyên tố ngẫu nhiên p và q có kích thước bằng nhau và tính tích của chúng là N.
2. Tính cấp của N, φ(N), bằng cách nhân: (p – 1) • (q – 1).
3. Chọn một e > 2 sao cho nó nhỏ hơn và nguyên tố cùng nhau với φ(N).
4. Tính d bằng cách đặt e • d mod φ(N) = 1.
5. Chọn một giá trị ngẫu nhiên y nhỏ hơn và nguyên tố cùng nhau với N.

Vấn đề RSA bao gồm việc tìm một x sao cho x<sup>e</sup> = y, trong khi chỉ được cung cấp một tập hợp con thông tin về Π, cụ thể là các biến N, e, và y. Khi p và q rất lớn, thường được khuyến nghị rằng chúng có kích thước 1024 bit, vấn đề RSA được cho là khó. Bây giờ bạn có thể thấy tại sao điều này là trường hợp dựa trên cuộc thảo luận trước đó.

Một cách dễ dàng để tính x khi x<sup>e</sup> mod N = y mod N là đơn giản bằng cách tính y<sup>d</sup> mod N. Chúng ta biết y<sup>d</sup> mod N = x mod N qua các phép tính sau:

* y<sup>d</sup> mod N = x<sup>e • d</sup> mod N = x<sup>e • d mod φ(N)</sup> mod N = x<sup>1 mod φ(N)</sup> mod N = x mod N.

Vấn đề là chúng ta không biết giá trị d, vì nó không được cung cấp trong vấn đề. Do đó, chúng ta không thể trực tiếp tính y<sup>d</sup> mod N để tạo ra x mod N.

Tuy nhiên, chúng ta có thể gián tiếp tính được d từ cấp của N, φ(n), vì chúng ta biết rằng e • d mod φ(N) = 1 mod φ(N). Nhưng theo giả định, vấn đề cũng không cung cấp giá trị cho φ(N).

Cuối cùng, cấp có thể được tính gián tiếp với các yếu tố nguyên tố p và q, để chúng ta có thể cuối cùng tính được d. Nhưng theo giả định, các giá trị p và q cũng không được cung cấp cho chúng ta.

Nói một cách chính xác, ngay cả khi vấn đề phân tích trong một vấn đề RSA là khó, chúng ta không thể chứng minh rằng vấn đề RSA cũng khó. Có thể có những cách khác để giải quyết vấn đề RSA ngoài việc phân tích. Tuy nhiên, nói chung được chấp nhận và giả định rằng nếu vấn đề phân tích trong vấn đề RSA là khó, thì chính vấn đề RSA cũng khó.

Nếu vấn đề RSA thực sự khó, thì nó tạo ra một hàm một chiều với một cửa hậu. Hàm ở đây là f(g) = g<sup>e</sup> mod N. Với kiến thức về f(g), bất kỳ ai cũng có thể dễ dàng tính một giá trị y cho một g = x cụ thể. Tuy nhiên, thực tế là không thể tính một giá trị x cụ thể chỉ từ việc biết giá trị y và hàm f(g). Ngoại lệ là khi bạn được cung cấp một thông tin d, cửa hậu. Trong trường hợp đó, bạn có thể đơn giản tính y<sup>d</sup> để cho ra x.

Hãy đi qua một ví dụ cụ thể để minh họa vấn đề RSA. Tôi không thể chọn một vấn đề RSA được coi là khó dưới các điều kiện trên, vì các số sẽ rất khó xử lý. Thay vào đó, ví dụ này chỉ để minh họa cách vấn đề RSA hoạt động nói chung.
Để bắt đầu, giả sử bạn chọn hai số nguyên tố ngẫu nhiên là 13 và 31. Vậy p = 13 và q = 31. Tích N của hai số nguyên tố này bằng 403. Chúng ta có thể dễ dàng tính toán cấp của 403. Nó tương đương với (13 - 1) • (31 - 1) = 360.
Tiếp theo, như được chỉ định bởi bước 3 của bài toán RSA, chúng ta cần chọn một số nguyên tố cùng nhau với 360 lớn hơn 2 và nhỏ hơn 360. Chúng ta không cần phải chọn giá trị này một cách ngẫu nhiên. Giả sử rằng chúng ta chọn 103. Đây là một số nguyên tố cùng nhau của 360 vì ước số chung lớn nhất của nó với 103 là 1.

Bước 4 yêu cầu chúng ta tính giá trị d sao cho 103 • d mod 360 = 1. Đây không phải là một nhiệm vụ dễ dàng khi thực hiện bằng tay khi giá trị của N lớn. Điều này đòi hỏi chúng ta phải sử dụng một quy trình gọi là **thuật toán Euclid mở rộng**.

Mặc dù tôi không trình bày quy trình ở đây, nó cho ra giá trị 7 khi e = 103. Bạn có thể xác minh rằng cặp giá trị 103 và 7 thực sự đáp ứng điều kiện chung e • d mod φ(n) = 1 thông qua các phép tính dưới đây.

* 103 • 7 mod 360 = 721 mod 360 = 1 mod 360

Quan trọng là, dựa vào *Đề xuất 4*, chúng ta biết rằng không có số nguyên nào khác từ 1 đến 360 cho d sẽ tạo ra kết quả 103 • d = 1 mod 360. Ngoài ra, đề xuất cũng ngụ ý rằng việc chọn một giá trị khác cho e, sẽ tạo ra một giá trị duy nhất khác cho d.

Trong bước 5 của bài toán RSA, chúng ta phải chọn một số nguyên dương y nào đó là một số nguyên tố cùng nhau nhỏ hơn của 403. Giả sử rằng chúng ta đặt y = 2<sup>103</sup>. Lũy thừa của 2 với 103 cho kết quả dưới đây.

* 2<sup>103</sup> mod 403 = 10,141,204,801,825,835,211,973,625,643,008 mod 403 = 349 mod 403

Bài toán RSA trong ví dụ cụ thể này giờ đây như sau: Bạn được cung cấp N = 403, e = 103, và y = 349 mod 403. Bây giờ bạn phải tính x sao cho x<sup>103</sup> = 349 mod 403. Nghĩa là, bạn phải tìm ra giá trị ban đầu trước khi lũy thừa bởi 103 là 2.

Việc tính x sẽ dễ dàng (ít nhất là đối với máy tính) nếu chúng ta biết rằng d = 7. Trong trường hợp đó, bạn chỉ cần xác định x như dưới đây.

* x = y<sup>7</sup> mod 403 = 349<sup>7</sup> mod 403 = 630,634,881,591,804,949 mod 403 = 2 mod 403

Vấn đề là bạn không được cung cấp thông tin rằng d = 7. Bạn có thể, tất nhiên, tính d từ thực tế là 103 • d = 1 mod 360. Vấn đề là bạn cũng không được cung cấp thông tin rằng cấp của N = 360. Cuối cùng, bạn cũng có thể tính cấp của 403 bằng cách tính sản phẩm sau: (p – 1) • (q – 1). Nhưng bạn cũng không được thông báo rằng p = 13 và q = 31.
Dĩ nhiên, một máy tính vẫn có thể giải quyết vấn đề RSA trong ví dụ này một cách tương đối dễ dàng, bởi vì các số nguyên tố liên quan không lớn. Nhưng khi các số nguyên tố trở nên rất lớn, nó đối mặt với một nhiệm vụ gần như không thể thực hiện được.

Chúng tôi đã trình bày vấn đề RSA, một tập hợp các điều kiện mà dưới đó, việc giải quyết nó trở nên khó khăn, và toán học cơ bản đằng sau nó. Làm thế nào tất cả những điều này giúp ích cho mật mã bất đối xứng? Cụ thể, làm thế nào chúng ta có thể biến độ khó của vấn đề RSA dưới một số điều kiện thành một hệ thống mã hóa hoặc một hệ thống chữ ký số?

Một cách tiếp cận là lấy vấn đề RSA và xây dựng các hệ thống một cách trực tiếp. Ví dụ, giả sử bạn đã tạo ra một tập hợp các biến Π như được mô tả trong vấn đề RSA, và đảm bảo rằng p và q đủ lớn. Bạn đặt khóa công khai của mình bằng (N, e) và chia sẻ thông tin này với thế giới. Như đã mô tả ở trên, bạn giữ bí mật các giá trị của p, q, φ(n), và d. Thực tế, d là khóa riêng của bạn.

Bất kỳ ai muốn gửi cho bạn một tin nhắn m là một phần tử của **C<sub>N</sub>** có thể đơn giản mã hóa nó như sau: c = m<sup>e</sup> mod N. (Bản mã c ở đây tương đương với giá trị y trong vấn đề RSA.) Bạn có thể dễ dàng giải mã tin nhắn này chỉ bằng cách tính toán c<sup>d</sup> mod N.

Bạn cũng có thể cố gắng tạo ra một hệ thống chữ ký số theo cùng một cách. Giả sử bạn muốn gửi cho ai đó một tin nhắn m với một chữ ký số S. Bạn chỉ cần đặt S = m<sup>d</sup> mod N và gửi cặp (m,S) cho người nhận. Bất kỳ ai cũng có thể xác minh chữ ký số chỉ bằng cách kiểm tra liệu S<sup>e</sup> mod N = m mod N. Tuy nhiên, bất kỳ kẻ tấn công nào cũng sẽ gặp khó khăn thực sự khi tạo ra một S hợp lệ cho một tin nhắn, vì họ không sở hữu d.

Thật không may, việc biến vấn đề RSA, một vấn đề khó khăn riêng lẻ, thành một hệ thống mật mã không hề đơn giản như vậy. Đối với hệ thống mã hóa trực tiếp, bạn chỉ có thể chọn các số nguyên tố cùng nhau của N làm tin nhắn của mình. Điều này không để lại cho chúng ta nhiều tin nhắn có thể, chắc chắn không đủ cho giao tiếp tiêu chuẩn. Ngoài ra, những tin nhắn này phải được chọn một cách ngẫu nhiên. Điều này có vẻ khá không thực tế. Cuối cùng, bất kỳ tin nhắn nào được chọn hai lần sẽ tạo ra cùng một bản mã. Điều này cực kỳ không mong muốn trong bất kỳ hệ thống mã hóa nào, và không đáp ứng bất kỳ tiêu chuẩn an ninh mật mã hiện đại nghiêm ngặt nào.

Vấn đề trở nên tồi tệ hơn đối với hệ thống chữ ký số trực tiếp của chúng tôi. Như hiện tại, bất kỳ kẻ tấn công nào cũng có thể dễ dàng làm giả chữ ký số chỉ bằng cách trước tiên chọn một số nguyên tố cùng nhau của N làm chữ ký và sau đó tính toán tin nhắn gốc tương ứng. Điều này rõ ràng phá vỡ yêu cầu về khả năng không thể giả mạo tồn tại.

Tuy nhiên, với việc thêm một chút phức tạp thông minh, vấn đề RSA có thể được sử dụng để tạo ra một hệ thống mã hóa khóa công khai an toàn cũng như một hệ thống chữ ký số an toàn. Chúng tôi sẽ không đi vào chi tiết của những cấu trúc như vậy ở đây.<sup>[4](#footnote4)</sup> Tuy nhiên, quan trọng là, sự phức tạp bổ sung này không thay đổi vấn đề RSA cơ bản mà các hệ thống này dựa trên.

### Ghi chú

[^1]: Phân tích thành nhân tử cũng có thể quan trọng khi làm việc với các loại đối tượng toán học khác ngoài số. Ví dụ, nó có thể hữu ích để phân tích thành nhân tử các biểu thức đa thức như x^2 – 2x + 1. Trong cuộc thảo luận của chúng tôi, chúng tôi chỉ tập trung vào việc phân tích thành nhân tử của số, cụ thể là số nguyên [^1].
[^2]: Theo định lý số nguyên tố, số lượng số nguyên tố nhỏ hơn hoặc bằng N xấp xỉ N/ln(N). Điều này có nghĩa là bạn có thể ước lượng số lượng số nguyên tố có độ dài 1024 bit bằng 2^1024/ln(2^1024) - 2^1023/ln(2^1023) tương đương xấp xỉ 1.265 x 10^305 [^2].

# Đóng góp
<partId>4556aab1-4876-552a-b6db-df6837bbf27a</partId>

## Giới thiệu
<chapterId>ff08a57b-740f-5d7e-8cf2-81db0908166e</chapterId>

Mọi đóng góp đều được hoan nghênh. Trước khi thực hiện, vui lòng xem qua thông tin nền tảng về kế hoạch của tôi cho cuốn sách cũng như các hướng dẫn để đóng góp.

### Kế hoạch hiện tại

Kế hoạch hiện tại của tôi cho sự phát triển tiếp theo của cuốn sách như sau:

- Tạo một chương cuối cùng đi vào chi tiết về các ứng dụng mật mã thực tế, như bảo mật lớp vận chuyển, định tuyến onion, và trao đổi giá trị trong Bitcoin
- Tạo nhiều hình ảnh và sơ đồ tốt hơn để hỗ trợ thảo luận bằng văn bản
- Sử dụng LaTeX Math hoặc một ứng dụng đánh dấu khác cho ký hiệu chính thức (thay vì chỉ Markdown)

### Hướng dẫn cho đóng góp

Nếu bạn có những chỉnh sửa nhỏ hoặc đề xuất liên quan đến văn bản hiện tại, bạn có thể tạo một pull request hoặc đưa ra một vấn đề. Nếu bạn tạo một pull request, vui lòng tuân thủ các hướng dẫn sau:

- Tạo các commit trên một nhánh riêng biệt trong fork của bạn từ kho lưu trữ
- Gắn nhãn các commit một cách rõ ràng
- Tạo các commit riêng biệt cho các vấn đề logic khác nhau để quá trình xem xét dễ dàng hơn

Nếu bạn có những đề xuất đáng kể hơn liên quan đến cuốn sách, vui lòng đưa ra một vấn đề hoặc liên hệ trực tiếp với tôi qua **jaburgers@protonmail.com**.

### Bản quyền

Công việc trong kho lưu trữ này được cấp phép theo Giấy phép Quốc tế Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0).

Bạn có thể tìm thấy một mô tả ngắn của giấy phép [tại đây](https://creativecommons.org/licenses/by-nc-nd/4.0/).

Bạn có thể tìm thấy phiên bản đầy đủ của giấy phép [tại đây](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode).

## Ký hiệu
<chapterId>07250f8d-ad7c-5531-a70c-4417d6d1b865</chapterId>

### Thuật ngữ chính

Các thuật ngữ chính trong các bài giới thiệu được làm nổi bật bằng cách in đậm. Ví dụ, việc giới thiệu thuật ngữ **Rijndael cipher** sẽ được thể hiện như sau: **Rijndael cipher**.

Các thuật ngữ chính được định nghĩa rõ ràng, trừ khi chúng là tên riêng hoặc ý nghĩa của chúng rõ ràng từ bối cảnh thảo luận.

Bất kỳ định nghĩa nào thường được đưa ra khi giới thiệu một thuật ngữ chính, mặc dù đôi khi thuận tiện hơn khi để định nghĩa cho đến một điểm sau.

### Các từ và cụm từ được nhấn mạnh

Các từ và cụm từ được nhấn mạnh qua cách in nghiêng. Ví dụ, cụm từ "Nhớ mật khẩu của bạn" sẽ được thể hiện như sau: *Nhớ mật khẩu của bạn*.

### Ký hiệu chính thức

Ký hiệu chính thức chủ yếu liên quan đến các biến, biến ngẫu nhiên, và tập hợp.

* Biến: Chúng thường chỉ được chỉ định bằng một chữ cái thường (ví dụ, "x" hoặc "y"). Đôi khi chúng được viết hoa để rõ ràng hơn (ví dụ, "M" hoặc "K").
* Biến ngẫu nhiên: Chúng luôn được chỉ định bằng một chữ cái in hoa (ví dụ, "X" hoặc "Y")
* Tập hợp: Được chỉ định bằng chữ in đậm, chữ hoa (ví dụ, **S**)