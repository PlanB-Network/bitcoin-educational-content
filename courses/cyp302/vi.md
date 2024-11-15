---
name: Giới thiệu về Mật mã học chính thức
goal: Một bài giới thiệu sâu rộng về khoa học và thực hành của mật mã học.
objectives:
  - Khám phá các mã Beale và phương pháp mật mã học hiện đại để hiểu về các khái niệm cơ bản và lịch sử của mật mã học.
  - Đào sâu vào lý thuyết số, nhóm và trường để nắm vững các khái niệm toán học chính yếu đằng sau mật mã học.
  - Nghiên cứu về mã dòng RC4 và AES với khóa 128-bit để tìm hiểu về các thuật toán mật mã đối xứng.
  - Khảo sát hệ thống mật mã RSA, phân phối khóa và hàm băm để khám phá mật mã học bất đối xứng.

---
# Sâu lắng vào mật mã học

Rất khó để tìm thấy nhiều tài liệu cung cấp một lập trường trung lập tốt trong giáo dục mật mã học.

Một mặt, có những luận án dài và chính thức, thực sự chỉ dành cho những người có nền tảng vững chắc trong toán học, logic, hoặc một số lĩnh vực chính thức khác. Mặt khác, có những giới thiệu rất tổng quát mà thực sự che giấu quá nhiều chi tiết đối với bất kỳ ai ít nhất là một chút tò mò.

Bài giới thiệu này về mật mã học tìm cách nắm bắt lập trường trung lập. Mặc dù nó nên tương đối thách thức và chi tiết đối với bất kỳ ai mới với mật mã học, nó không phải là hố thỏ của một luận án cơ bản điển hình.

+++

# Giới thiệu
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Mô tả ngắn gọn
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Cuốn sách này cung cấp một bài giới thiệu sâu rộng về khoa học và thực hành của mật mã học. Nơi có thể, nó tập trung vào việc trình bày khái niệm, thay vì trình bày chính thức của vật liệu.

> Khóa học này dựa trên [kho của JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Tất cả quyền thuộc về anh ấy. Nội dung chưa hoàn thiện và chỉ ở đây để trình bày cách chúng ta có thể tích hợp nếu JWburger đồng ý.

### Động lực và mục tiêu

Rất khó để tìm thấy nhiều tài liệu cung cấp một lập trường trung lập tốt trong giáo dục mật mã học.

Một mặt, có những luận án dài và chính thức, thực sự chỉ dành cho những người có nền tảng vững chắc trong toán học, logic, hoặc một số lĩnh vực chính thức khác. Mặt khác, có những giới thiệu rất tổng quát mà thực sự che giấu quá nhiều chi tiết đối với bất kỳ ai ít nhất là một chút tò mò.

Bài giới thiệu này về mật mã học tìm cách nắm bắt lập trường trung lập. Mặc dù nó nên tương đối thách thức và chi tiết đối với bất kỳ ai mới với mật mã học, nó không phải là hố thỏ của một luận án cơ bản điển hình.

### Đối tượng mục tiêu

Từ các nhà phát triển đến những người tò mò về trí tuệ, cuốn sách này hữu ích cho bất kỳ ai muốn hiểu sâu hơn về mật mã học. Nếu mục tiêu của bạn là nắm vững lĩnh vực mật mã học, thì cuốn sách này cũng là một điểm khởi đầu tốt.

### Hướng dẫn đọc

Cuốn sách hiện tại bao gồm bảy chương: "Mật mã học là gì?" (Chương 1), "Nền tảng Toán học của Mật mã học I" (Chương 2), "Nền tảng Toán học của Mật mã học II" (Chương 3), "Mật mã học Đối xứng" (Chương 4), "RC4 và AES" (Chương 5), "Mật mã học Bất đối xứng" (Chương 6), và "Hệ thống mật mã RSA" (Chương 7). Một chương cuối cùng, "Mật mã học trong Thực hành," sẽ được thêm vào. Nó tập trung vào các ứng dụng mật mã học khác nhau, bao gồm bảo mật lớp vận chuyển, định tuyến onion, và hệ thống trao đổi giá trị của Bitcoin.
Trừ khi bạn có một nền tảng vững chắc về toán học, lý thuyết số có lẽ là chủ đề khó nhất trong cuốn sách này. Tôi đã cung cấp một cái nhìn tổng quan về nó trong Chương 3, và nó cũng xuất hiện trong phần trình bày về AES trong Chương 5 và hệ thống mật mã RSA trong Chương 7.
Nếu bạn thực sự gặp khó khăn với các chi tiết chính thức trong những phần này của cuốn sách, tôi khuyên bạn nên chấp nhận đọc sơ qua chúng lần đầu tiên.

### Lời Cảm Ơn

Cuốn sách có ảnh hưởng nhất trong việc hình thành cuốn sách này là _Introduction to Modern Cryptography_ của Jonathan Katz và Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Một khóa học đi kèm có sẵn trên Coursera với tên "Cryptography."

Những nguồn thông tin chính thêm vào đã hữu ích trong việc tạo ra cái nhìn tổng quan trong cuốn sách này bao gồm Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar và Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) và [một khóa học dựa trên cuốn sách của Paar có tên “Introduction to Cryptography”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); và Bruce Schneier, Applied Cryptography, ấn bản thứ 2, 2015 (Indianapolis, IN: John Wiley & Sons).

Tôi chỉ trích dẫn thông tin và kết quả cụ thể mà tôi lấy từ những nguồn này, nhưng muốn công nhận sự nợ món chung của mình với họ ở đây.

Đối với những độc giả muốn tìm hiểu kiến thức nâng cao hơn về mật mã học sau khi đã được giới thiệu, tôi rất khuyên bạn đọc cuốn sách của Katz và Lindell. Khóa học của Katz trên Coursera dễ tiếp cận hơn so với cuốn sách.

### Đóng Góp

Vui lòng xem [tệp đóng góp trong kho lưu trữ](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) để biết một số hướng dẫn về cách hỗ trợ dự án.

### Ký Hiệu

**Thuật ngữ chính:**

Các thuật ngữ chính trong các bài giới thiệu được làm nổi bật bằng cách in đậm. Ví dụ, việc giới thiệu thuật ngữ Rijndael cipher sẽ trông như sau: **Rijndael cipher**.

Các thuật ngữ chính được định nghĩa một cách rõ ràng, trừ khi chúng là tên riêng hoặc ý nghĩa của chúng rõ ràng từ bối cảnh thảo luận.

Bất kỳ định nghĩa nào thường được đưa ra ngay khi giới thiệu một thuật ngữ chính, mặc dù đôi khi thuận tiện hơn khi để lại định nghĩa cho một thời điểm sau.

**Các từ và cụm từ được nhấn mạnh:**

Các từ và cụm từ được nhấn mạnh qua cách in nghiêng. Ví dụ, cụm từ "Nhớ mật khẩu của bạn" sẽ trông như sau: *Nhớ mật khẩu của bạn*.

**Ký hiệu chính thức:**

Ký hiệu chính thức chủ yếu liên quan đến biến, biến ngẫu nhiên và tập hợp.

* Biến: Chúng thường chỉ được chỉ ra bằng một chữ cái thường (ví dụ, "x" hoặc "y"). Đôi khi chúng được viết hoa để rõ ràng (ví dụ, "M" hoặc "K").
* Biến ngẫu nhiên: Chúng luôn được chỉ ra bằng một chữ cái in hoa (ví dụ, "X" hoặc "Y")
* Tập hợp: Chúng luôn được chỉ ra bằng chữ in đậm, chữ cái in hoa (ví dụ, **S**)

# Mật mã học là gì?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Các mật mã Beale
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>
Hãy bắt đầu cuộc tìm hiểu của chúng ta về lĩnh vực mật mã học với một trong những tập hợp câu chuyện hấp dẫn và giải trí nhất trong lịch sử của nó: đó là câu chuyện về các mã Beale. [1]
Theo ý kiến của tôi, câu chuyện về các mã Beale có lẽ gần giống với hư cấu hơn là thực tế. Nhưng nó được cho là đã xảy ra như sau.

Trong cả mùa Đông năm 1820 và 1822, một người đàn ông tên là Thomas J. Beale đã ở tại một quán trọ do Robert Morriss sở hữu ở Lynchburg (Virginia). Vào cuối lần ở thứ hai của Beale, ông đã giao cho Morriss một chiếc hộp sắt chứa các tài liệu quý giá để bảo quản.

Vài tháng sau, Morriss nhận được một bức thư từ Beale ngày 9 tháng 5 năm 1822. Bức thư nhấn mạnh giá trị lớn của nội dung chiếc hộp sắt và đưa ra một số hướng dẫn cho Morriss: nếu Beale hoặc bất kỳ đồng minh nào của ông ta không bao giờ đến yêu cầu chiếc hộp, ông ta nên mở nó đúng mười năm từ ngày thư được viết (tức là ngày 9 tháng 5 năm 1832). Một số tài liệu bên trong sẽ được viết bằng văn bản thông thường. Tuy nhiên, một số khác sẽ là “không thể hiểu được nếu không có sự giúp đỡ của một chìa khóa.” Chìa khóa này sau đó sẽ được một người bạn không tên của Beale giao cho Morriss vào tháng 6 năm 1832.

Mặc dù có hướng dẫn rõ ràng, Morriss không mở hộp vào tháng 5 năm 1832 và người bạn bí ẩn của Beale cũng không xuất hiện vào tháng 6 của năm đó. Phải đến năm 1845, người chủ quán trọ mới quyết định mở chiếc hộp. Trong đó, Morriss tìm thấy một ghi chú giải thích cách Beale và các đồng minh của mình đã phát hiện ra vàng và bạc ở phía Tây và chôn chúng, cùng với một số trang sức, để bảo quản. Ngoài ra, chiếc hộp chứa ba **ciphertexts**: tức là, các văn bản được viết bằng mã mà cần có một **khóa mật mã**, hoặc một bí mật, và một thuật toán đi kèm để mở khóa. Quá trình mở khóa một ciphertext được gọi là **giải mã**, trong khi quá trình khóa được gọi là **mã hóa**. (Như đã giải thích trong Chương 3, thuật ngữ cipher có thể có nhiều nghĩa. Trong tên "Beale ciphers", nó được viết tắt cho ciphertexts.)

Ba ciphertexts mà Morriss tìm thấy trong chiếc hộp sắt mỗi cái đều bao gồm một chuỗi số được phân tách bằng dấu phẩy. Theo ghi chú của Beale, những ciphertexts này riêng biệt cung cấp vị trí của kho báu, nội dung của kho báu, và một danh sách tên với những người thừa kế hợp pháp của kho báu và phần của họ (thông tin cuối cùng này có liên quan trong trường hợp Beale và các đồng minh của ông ta không bao giờ đến yêu cầu chiếc hộp).

Morris đã cố gắng giải mã ba ciphertexts trong hai mươi năm. Điều này sẽ dễ dàng với chiếc chìa khóa. Nhưng Morriss không có chìa khóa và không thành công trong các nỗ lực của mình để khôi phục các văn bản gốc, hay **plaintexts** như chúng thường được gọi trong mật mã học.

Khi cuộc đời đang dần kết thúc, Morriss chuyển chiếc hộp cho một người bạn vào năm 1862. Người bạn này sau đó đã xuất bản một cuốn sách nhỏ vào năm 1885, dưới bút danh J.B. Ward. Nó bao gồm một mô tả về (được cho là) lịch sử của chiếc hộp, ba ciphertexts, và một giải pháp mà anh ta đã tìm ra cho ciphertext thứ hai. (Rõ ràng, có một chìa khóa cho mỗi ciphertext, và không phải một chìa khóa hoạt động trên tất cả ba ciphertexts như Beale ban đầu có vẻ đã đề xuất trong thư của mình gửi cho Morriss.)

Bạn có thể thấy ciphertext thứ hai trong *Hình 2* dưới đây. [2] Chìa khóa cho ciphertext này là Tuyên ngôn Độc lập của Hoa Kỳ. Quy trình giải mã được thực hiện bằng cách áp dụng hai quy tắc sau:
* Đối với bất kỳ số nào trong văn bản mã hóa, tìm từ thứ n trong Bản Tuyên Ngôn Độc Lập của Hoa Kỳ* Thay thế số n bằng chữ cái đầu tiên của từ bạn tìm được

*Hình 1: Mật mã Beale số 2*

![Hình 1: Mật mã Beale số 2.](assets/Figure1-1.webp "Hình 1: Mật mã Beale số 2")

Ví dụ, số đầu tiên của văn bản mã hóa thứ hai là 115. Từ thứ 115 của Bản Tuyên Ngôn Độc Lập là “instituted,” vậy nên chữ cái đầu tiên của văn bản gốc là “i.” Văn bản mã hóa không chỉ rõ khoảng trắng và việc viết hoa. Nhưng sau khi giải mã một vài từ đầu tiên, bạn có thể suy luận một cách hợp lý rằng từ đầu tiên của văn bản gốc đơn giản là “I.” (Văn bản bắt đầu với cụm từ “I have deposited in the county of Bedford.”)

Sau khi giải mã, thông điệp thứ hai cung cấp nội dung chi tiết về kho báu (vàng, bạc, và đá quý), và gợi ý rằng nó được chôn giấu trong các nồi sắt và được che phủ bằng đá ở Quận Bedford (Virginia). Mọi người yêu thích một bí ẩn hay, vì vậy nhiều nỗ lực đã được bỏ ra để giải mã hai mật mã Beale còn lại, đặc biệt là mật mã mô tả vị trí của kho báu. Ngay cả các nhà mật mã học nổi tiếng cũng đã thử sức với chúng. Tuy nhiên, cho đến nay, chưa ai có thể giải mã được hai văn bản mã hóa còn lại.

**Ghi chú:**

[1] Để có một bản tóm tắt tốt về câu chuyện, xem Simon Singh, *The Code Book*, Fourth Estate (London, 1999), trang 82-99. Một bộ phim ngắn về câu chuyện đã được Andrew Allen thực hiện vào năm 2010. Bạn có thể tìm xem bộ phim, “The Thomas Beale Cipher,” [trên trang web của nó](http://www.thomasbealecipher.com/).

[2] Hình ảnh này có sẵn trên trang Wikipedia về các mật mã Beale.

## Mật mã học hiện đại
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Những câu chuyện sinh động như về các mật mã Beale là những gì mà hầu hết chúng ta liên tưởng đến với mật mã học. Tuy nhiên, mật mã học hiện đại khác biệt ít nhất bốn cách quan trọng so với những ví dụ lịch sử này.

Đầu tiên, lịch sử mật mã học chỉ quan tâm đến **bí mật** (hoặc bảo mật). [3] Các văn bản mã hóa được tạo ra để đảm bảo rằng chỉ những bên nhất định mới có thể tiếp cận thông tin trong văn bản gốc, như trường hợp của các mật mã Beale. Để một hệ thống mã hóa phục vụ mục đích này tốt, việc giải mã văn bản mã hóa chỉ nên khả thi nếu bạn có chìa khóa.

Mật mã học hiện đại quan tâm đến một phạm vi chủ đề rộng lớn hơn chỉ là bí mật. Những chủ đề này bao gồm chủ yếu là (1) **tính toàn vẹn của thông điệp**—đó là, đảm bảo rằng một thông điệp không bị thay đổi; (2) **tính xác thực của thông điệp**—đó là, đảm bảo rằng một thông điệp thực sự đến từ một người gửi cụ thể; và (3) **không thể chối bỏ**—đó là, đảm bảo rằng một người gửi không thể phủ nhận sau này rằng họ đã gửi một thông điệp. [4]

Một sự phân biệt quan trọng cần ghi nhớ là giữa một **hệ thống mã hóa** và một **hệ thống mật mã**. Một hệ thống mã hóa chỉ quan tâm đến bí mật. Mặc dù một hệ thống mã hóa là một hệ thống mật mã, nhưng ngược lại không đúng. Một hệ thống mật mã cũng có thể phục vụ các chủ đề chính khác của mật mã học, bao gồm tính toàn vẹn, tính xác thực, và không thể chối bỏ.
Các chủ đề về tính toàn vẹn và xác thực cũng quan trọng như bí mật. Hệ thống truyền thông hiện đại của chúng ta sẽ không thể hoạt động nếu không có sự đảm bảo về tính toàn vẹn và xác thực của thông tin liên lạc. Không thể phủ nhận cũng là một mối quan tâm quan trọng, chẳng hạn như đối với hợp đồng số, nhưng không cần thiết phải có mặt phổ biến trong các ứng dụng mật mã như bí mật, tính toàn vẹn và xác thực.

Thứ hai, các phương pháp mã hóa cổ điển như mã Beale luôn liên quan đến một khóa được chia sẻ giữa tất cả các bên liên quan. Tuy nhiên, nhiều phương pháp mật mã hiện đại không chỉ liên quan đến một, mà là hai khóa: một **khóa riêng tư** và một **khóa công khai**. Trong khi khóa trước nên được giữ kín trong bất kỳ ứng dụng nào, khóa sau thường là kiến thức công cộng (do đó, tên của chúng). Trong lĩnh vực mã hóa, khóa công khai có thể được sử dụng để mã hóa tin nhắn, trong khi khóa riêng tư có thể được sử dụng để giải mã.

Nhánh của mật mã học xử lý các phương pháp mà tất cả các bên chia sẻ một khóa được biết đến là **mật mã đối xứng**. Khóa đơn trong một phương pháp như vậy thường được gọi là **khóa riêng tư** (hoặc khóa bí mật). Nhánh của mật mã học xử lý các phương pháp yêu cầu một cặp khóa riêng tư-công khai được biết đến là **mật mã bất đối xứng**. Các nhánh này đôi khi cũng được gọi là **mật mã khóa riêng** và **mật mã khóa công**, tương ứng (mặc dù điều này có thể gây nhầm lẫn, vì các phương pháp mật mã khóa công cũng có khóa riêng).

Sự ra đời của mật mã bất đối xứng vào cuối những năm 1970 đã là một trong những sự kiện quan trọng nhất trong lịch sử của mật mã học. Không có nó, hầu hết hệ thống truyền thông hiện đại của chúng ta, bao gồm cả Bitcoin, sẽ không thể khả thi, hoặc ít nhất là rất bất tiện.

Quan trọng, mật mã học hiện đại không chỉ là nghiên cứu về các phương pháp mật mã khóa đối xứng và bất đối xứng (mặc dù điều đó bao gồm phần lớn lĩnh vực). Ví dụ, mật mã học cũng quan tâm đến các hàm băm và bộ sinh số ngẫu nhiên giả, và bạn có thể xây dựng các ứng dụng trên những nguyên tắc cơ bản này không liên quan đến mật mã khóa đối xứng hoặc bất đối xứng.

Thứ ba, các phương pháp mã hóa cổ điển, như những phương pháp được sử dụng trong mã Beale, được coi là nghệ thuật hơn là khoa học. Sự an toàn của chúng chủ yếu dựa vào trực giác về độ phức tạp của chúng. Chúng thường được vá lỗi khi một cuộc tấn công mới được biết đến, hoặc bị bỏ hoàn toàn nếu cuộc tấn công đặc biệt nghiêm trọng. Tuy nhiên, mật mã học hiện đại là một khoa học nghiêm ngặt với một cách tiếp cận toán học, hình thức để phát triển và phân tích các phương pháp mật mã. [5]

Cụ thể, mật mã học hiện đại tập trung vào **chứng minh an toàn** hình thức. Bất kỳ chứng minh an toàn nào cho một phương pháp mật mã đều tiến hành theo ba bước:

1. Phát biểu một **định nghĩa mật mã về an toàn**, tức là một tập hợp các mục tiêu an toàn và mối đe dọa từ kẻ tấn công.
2. Phát biểu bất kỳ giả định toán học nào liên quan đến độ phức tạp tính toán của phương pháp. Ví dụ, một phương pháp mật mã có thể chứa một bộ sinh số ngẫu nhiên giả. Mặc dù chúng ta không thể chứng minh chúng tồn tại, chúng ta có thể giả định rằng chúng tồn tại.
3. Trình bày một **chứng minh an toàn** toán học của phương pháp dựa trên khái niệm hình thức về an toàn và bất kỳ giả định toán học nào.

Thứ tư, trong khi trước đây mật mã học chủ yếu được sử dụng trong các cài đặt quân sự, nó đã trở nên phổ biến trong các hoạt động hàng ngày của chúng ta trong kỷ nguyên số. Cho dù bạn đang giao dịch ngân hàng trực tuyến, đăng bài trên mạng xã hội, mua sản phẩm từ Amazon bằng thẻ tín dụng, hay chuyển bitcoin cho bạn bè, mật mã học là điều không thể thiếu của kỷ nguyên số của chúng ta.

Xét về bốn khía cạnh này của mật mã học hiện đại, chúng ta có thể mô tả mật mã học hiện đại là khoa học quan tâm đến việc phát triển và phân tích hình thức các phương pháp mật mã để bảo vệ thông tin số khỏi các cuộc tấn công của đối thủ. [6] An toàn ở đây nên được hiểu một cách rộng rãi là ngăn chặn các cuộc tấn công làm hại đến bí mật, tính toàn vẹn, xác thực, và/hoặc không thể phủ nhận trong giao tiếp.
Mật mã học được xem là một phân ngành của **an ninh mạng**, chuyên về việc ngăn chặn việc trộm cắp, hư hại và lạm dụng các hệ thống máy tính. Lưu ý rằng nhiều vấn đề về an ninh mạng có ít hoặc chỉ một phần liên quan đến mật mã học.
Chẳng hạn, nếu một công ty lưu trữ máy chủ đắt tiền tại chỗ, họ có thể quan tâm đến việc bảo vệ phần cứng này khỏi bị trộm và hư hại. Mặc dù đây là một mối quan tâm về an ninh mạng, nhưng nó ít liên quan đến mật mã học.

Ví dụ khác, **các cuộc tấn công phishing** là một vấn đề phổ biến trong thời đại hiện đại của chúng ta. Những cuộc tấn công này cố gắng lừa đảo mọi người qua email hoặc một số phương tiện thông điệp khác để từ bỏ thông tin nhạy cảm như mật khẩu hoặc số thẻ tín dụng. Mặc dù mật mã học có thể giúp giải quyết các cuộc tấn công phishing đến một mức độ nhất định, nhưng một cách tiếp cận toàn diện yêu cầu nhiều hơn là chỉ sử dụng một số mật mã học.

**Ghi chú:**

[3] Để chính xác, các ứng dụng quan trọng của các kế hoạch mật mã học đã được quan tâm đến bí mật. Ví dụ, trẻ em thường sử dụng các kế hoạch mật mã học đơn giản cho “vui”. Bí mật không thực sự là một mối quan tâm trong những trường hợp đó.

[4] Bruce Schneier, *Applied Cryptography*, ấn bản thứ 2, 2015 (Indianapolis, IN: John Wiley & Sons), tr. 2.

[5] Xem Jonathan Katz và Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), đặc biệt là trang 16–23, để có một mô tả tốt.

[6] Cf. Katz và Lindell, ibid., tr. 3. Tôi nghĩ rằng sự mô tả của họ có một số vấn đề, vì vậy tôi trình bày một phiên bản hơi khác của tuyên bố của họ ở đây.

## Giao tiếp mở
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Mật mã học hiện đại được thiết kế để cung cấp đảm bảo an ninh trong môi trường **giao tiếp mở**. Nếu kênh giao tiếp của chúng ta được bảo vệ tốt đến mức kẻ nghe trộm không có cơ hội can thiệp hoặc thậm chí chỉ quan sát tin nhắn của chúng ta, thì mật mã học là không cần thiết. Tuy nhiên, hầu hết các kênh giao tiếp của chúng ta không được bảo vệ tốt như vậy.

Xương sống của giao tiếp trong thế giới hiện đại là một mạng lưới lớn các cáp quang. Việc thực hiện cuộc gọi điện thoại, xem truyền hình và duyệt web trong một hộ gia đình hiện đại chủ yếu dựa vào mạng lưới cáp quang này (một tỷ lệ nhỏ có thể hoàn toàn dựa vào vệ tinh). Đúng là bạn có thể có các kết nối dữ liệu khác nhau trong nhà, như cáp đồng trục, dòng thuê bao số (asymmetric) và cáp quang. Nhưng, ít nhất là ở thế giới phát triển, những phương tiện dữ liệu khác nhau này nhanh chóng kết nối bên ngoài nhà bạn với một nút trong mạng lưới cáp quang khổng lồ nối liền toàn cầu. Ngoại lệ là một số khu vực hẻo lánh của thế giới phát triển, như ở Hoa Kỳ và Úc, nơi lưu lượng dữ liệu vẫn có thể di chuyển một khoảng cách đáng kể qua dây điện thoại đồng truyền thống.

Việc ngăn chặn các kẻ tấn công tiềm năng truy cập vật lý vào mạng lưới cáp này và cơ sở hạ tầng hỗ trợ của nó là không thể. Thực tế, chúng ta đã biết rằng hầu hết dữ liệu của chúng ta bị các cơ quan tình báo quốc gia chặn lại tại các điểm giao nhau quan trọng của Internet.[7] Điều này bao gồm mọi thứ từ tin nhắn Facebook đến địa chỉ trang web mà bạn truy cập.

Mặc dù việc giám sát dữ liệu trên quy mô lớn đòi hỏi một đối thủ mạnh mẽ, như một cơ quan tình báo quốc gia, nhưng các kẻ tấn công chỉ với ít tài nguyên cũng có thể dễ dàng cố gắng nghe lén ở quy mô địa phương hơn. Mặc dù điều này có thể xảy ra ở cấp độ gắn kết dây, nhưng việc chỉ chặn bắt giao tiếp không dây là dễ dàng hơn nhiều.
Hầu hết dữ liệu mạng địa phương của chúng ta—dù ở nhà, tại văn phòng, hay trong quán cà phê—nay đều truyền qua sóng vô tuyến đến các điểm truy cập không dây trên các bộ định tuyến đa năng, thay vì qua các cáp vật lý. Vì vậy, kẻ tấn công cần rất ít nguồn lực để chặn bất kỳ lưu lượng mạng địa phương nào của bạn. Điều này đặc biệt đáng lo ngại vì hầu hết mọi người rất ít khi bảo vệ dữ liệu di chuyển qua mạng địa phương của họ. Ngoài ra, các kẻ tấn công tiềm năng cũng có thể nhắm vào các kết nối băng thông rộng di động của chúng ta, như 3G, 4G và 5G. Tất cả các giao tiếp không dây này đều là mục tiêu dễ dàng cho kẻ tấn công.

Do đó, ý tưởng giữ bí mật thông tin liên lạc bằng cách bảo vệ kênh truyền thông là một ảo tưởng hoàn toàn không tưởng đối với phần lớn thế giới hiện đại. Mọi thứ chúng ta biết đều đáng để cực kỳ hoang mang: bạn nên luôn giả định rằng có ai đó đang nghe lén. Và mật mã học là công cụ chính mà chúng ta có để đạt được bất kỳ loại an ninh nào trong môi trường hiện đại này.

**Ghi chú:**

[7] Xem, ví dụ, Olga Khazan, “The creepy, long-standing practice of undersea cable tapping”, *The Atlantic*, ngày 16 tháng 7 năm 2013 (có sẵn tại [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Nền tảng Toán học của Mật mã học 1
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Biến ngẫu nhiên
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Mật mã học dựa vào toán học. Và nếu bạn muốn hiểu biết hơn về mật mã học, bạn cần phải thoải mái với toán học đó.

Chương này giới thiệu hầu hết các kiến thức toán học cơ bản mà bạn sẽ gặp khi học về mật mã học. Các chủ đề bao gồm biến ngẫu nhiên, các phép toán modulo, các phép toán XOR, và tính ngẫu nhiên giả. Bạn nên nắm vững nội dung trong các phần này để có một hiểu biết không hời hợt về mật mã học.

Phần tiếp theo đề cập đến lý thuyết số, đây là phần thách thức hơn nhiều.

### Biến ngẫu nhiên

Một biến ngẫu nhiên thường được ký hiệu bằng một chữ cái viết hoa không in đậm. Ví dụ, chúng ta có thể nói về một biến ngẫu nhiên $X$, một biến ngẫu nhiên $Y$, hoặc một biến ngẫu nhiên $Z$. Đây là ký hiệu mà tôi cũng sẽ sử dụng từ đây trở đi.

Một **biến ngẫu nhiên** có thể nhận hai hoặc nhiều giá trị có thể xảy ra, mỗi giá trị với một xác suất dương nhất định. Các giá trị có thể xảy ra được liệt kê trong **tập hợp kết quả**.

Mỗi khi bạn **lấy mẫu** một biến ngẫu nhiên, bạn rút ra một giá trị cụ thể từ tập hợp kết quả của nó theo các xác suất đã định.

Hãy xem xét một ví dụ đơn giản. Giả sử một biến $X$ được định nghĩa như sau:

- $X$ có tập hợp kết quả $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

Dễ thấy $X$ là một biến ngẫu nhiên. Đầu tiên, có hai hoặc nhiều giá trị có thể mà $X$ có thể nhận, cụ thể là $1$ và $2$. Thứ hai, mỗi giá trị có thể có một xác suất dương xảy ra mỗi khi bạn lấy mẫu $X$, cụ thể là $0.5$.
Tất cả những gì một biến ngẫu nhiên yêu cầu là một tập hợp kết quả với hai hoặc nhiều khả năng, nơi mỗi khả năng có một xác suất dương xảy ra khi lấy mẫu. Về nguyên tắc, vậy thì, một biến ngẫu nhiên có thể được định nghĩa một cách trừu tượng, không cần bất kỳ bối cảnh nào. Trong trường hợp này, bạn có thể nghĩ đến việc "lấy mẫu" như thực hiện một thí nghiệm tự nhiên nào đó để xác định giá trị của biến ngẫu nhiên.

Biến $X$ ở trên được định nghĩa một cách trừu tượng. Do đó, bạn có thể nghĩ đến việc lấy mẫu biến $X$ như là tung một đồng xu công bằng và gán “2” trong trường hợp xuất hiện mặt ngửa và “1” trong trường hợp xuất hiện mặt sấp. Đối với mỗi lần lấy mẫu của $X$, bạn tung đồng xu lại.

Mặt khác, bạn cũng có thể nghĩ đến việc lấy mẫu $X$, như là lăn một con xúc xắc công bằng và gán “2” trong trường hợp con xúc xắc đổ ra $1$, $3$, hoặc $4$, và gán “1” trong trường hợp con xúc xắc đổ ra $2$, $5$, hoặc $6$. Mỗi lần bạn lấy mẫu $X$, bạn lăn con xúc xắc lại.

Thực sự, bất kỳ thí nghiệm tự nhiên nào cho phép bạn định nghĩa xác suất của các giá trị có thể có của $X$ ở trên đều có thể được tưởng tượng liên quan đến việc vẽ.

Tuy nhiên, thường thì biến ngẫu nhiên không chỉ được giới thiệu một cách trừu tượng. Thay vào đó, tập hợp các giá trị kết quả có thể có có ý nghĩa thực tế rõ ràng (không chỉ là như những con số). Ngoài ra, các giá trị kết quả này có thể được định nghĩa dựa trên một loại thí nghiệm cụ thể (không phải là bất kỳ thí nghiệm tự nhiên nào với những giá trị đó).

Bây giờ, hãy xem xét một ví dụ về biến $X$ không được định nghĩa một cách trừu tượng. X được định nghĩa như sau để xác định đội nào bắt đầu một trận bóng đá:

- $X$ có tập hợp kết quả {đội đỏ đá khởi điểm, đội xanh đá khởi điểm}
- Tung một đồng xu cụ thể $C$: sấp = “đội đỏ đá khởi điểm”; ngửa = “đội xanh đá khởi điểm”

$$
Pr [X = \text{đội đỏ đá khởi điểm}] = 0.5
$$

$$
Pr [X = \text{đội xanh đá khởi điểm}] = 0.5
$$

Trong trường hợp này, tập hợp kết quả của X được cung cấp một ý nghĩa cụ thể, đó là đội nào bắt đầu trong một trận bóng đá. Ngoài ra, các kết quả có thể xảy ra và xác suất liên quan của chúng được xác định bởi một thí nghiệm cụ thể, đó là tung một đồng xu cụ thể $C$.

Trong các cuộc thảo luận về mật mã học, biến ngẫu nhiên thường được giới thiệu dựa trên một tập hợp kết quả có ý nghĩa thực tế. Đó có thể là tập hợp tất cả các thông điệp có thể được mã hóa, được biết đến là không gian thông điệp, hoặc tập hợp tất cả các khóa mà các bên sử dụng mã hóa có thể chọn, được biết đến là không gian khóa.

Tuy nhiên, trong các cuộc thảo luận về mật mã học, biến ngẫu nhiên thường không được định nghĩa dựa trên một thí nghiệm tự nhiên cụ thể, mà dựa trên bất kỳ thí nghiệm nào có thể tạo ra phân phối xác suất đúng.

Biến ngẫu nhiên có thể có phân phối xác suất rời rạc hoặc liên tục. Biến ngẫu nhiên với **phân phối xác suất rời rạc**—nghĩa là, biến ngẫu nhiên rời rạc—có một số lượng hữu hạn các kết quả có thể xảy ra. Biến ngẫu nhiên $X$ trong cả hai ví dụ được đưa ra cho đến nay là rời rạc.

**Biến ngẫu nhiên liên tục** thay vào đó có thể nhận giá trị trong một hoặc nhiều khoảng. Ví dụ, bạn có thể nói rằng, khi lấy mẫu, một biến ngẫu nhiên sẽ nhận bất kỳ giá trị thực nào từ 0 đến 1, và mỗi số thực trong khoảng này có khả năng xảy ra như nhau. Trong khoảng này, có vô số giá trị có thể xảy ra.

Đối với các cuộc thảo luận về mật mã học, bạn chỉ cần hiểu về biến ngẫu nhiên rời rạc. Bất kỳ cuộc thảo luận nào về biến ngẫu nhiên từ đây trở đi nên được hiểu là đề cập đến biến ngẫu nhiên rời rạc, trừ khi có nói rõ khác.

### Vẽ đồ thị biến ngẫu nhiên
Các giá trị có thể có và xác suất tương ứng của một biến ngẫu nhiên có thể được hình dung một cách dễ dàng thông qua một đồ thị. Ví dụ, xem xét biến ngẫu nhiên $X$ từ phần trước với một tập hợp kết quả là $\{1, 2\}$, và $Pr [X = 1] = 0.5$ và $Pr [X = 2] = 0.5$. Chúng ta thường hiển thị một biến ngẫu nhiên như vậy dưới dạng một biểu đồ cột như trong *Hình 1*.
*Hình 1: Biến ngẫu nhiên X*

![Hình 1: Biến ngẫu nhiên X.](assets/Figure2-1.webp)

Các cột rộng trong *Hình 1* rõ ràng không có ý nghĩa là biến ngẫu nhiên $X$ thực sự liên tục. Thay vào đó, các cột được làm rộng để trở nên hấp dẫn hơn về mặt hình ảnh (chỉ một đường thẳng lên trên cung cấp một hình ảnh trực quan ít hơn).

### Biến đều

Trong cụm từ “biến ngẫu nhiên,” thuật ngữ “ngẫu nhiên” chỉ đơn giản là “xác suất”. Nói cách khác, điều đó chỉ có nghĩa là hai hoặc nhiều kết quả có thể xảy ra của biến số xảy ra với một số xác suất nhất định. Tuy nhiên, những kết quả này không nhất thiết phải có khả năng xảy ra bằng nhau (mặc dù thuật ngữ “ngẫu nhiên” thực sự có thể có ý nghĩa đó trong các ngữ cảnh khác).

Một **biến đều** là một trường hợp đặc biệt của biến ngẫu nhiên. Nó có thể nhận hai hoặc nhiều giá trị với xác suất bằng nhau. Biến ngẫu nhiên $X$ được mô tả trong *Hình 1* rõ ràng là một biến đều, vì cả hai kết quả có thể xảy ra đều có xác suất $0.5$. Tuy nhiên, có nhiều biến ngẫu nhiên không phải là trường hợp của biến đều.

Xem xét, ví dụ, biến ngẫu nhiên $Y$. Nó có một tập hợp kết quả $\{1, 2, 3, 8, 10\}$ và phân phối xác suất sau:

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Mặc dù hai kết quả có thể xảy ra có xác suất bằng nhau, cụ thể là $1$ và $8$, $Y$ cũng có thể nhận một số giá trị với xác suất khác $0.25$ khi lấy mẫu. Do đó, mặc dù $Y$ thực sự là một biến ngẫu nhiên, nó không phải là một biến đều.

Một hình ảnh mô tả của $Y$ được cung cấp trong *Hình 2*.

*Hình 2: Biến ngẫu nhiên Y*

![Hình 2: Biến ngẫu nhiên Y.](assets/Figure2-2.webp "Hình 2: Biến ngẫu nhiên Y")

Để xem xét một ví dụ cuối cùng, xem xét biến ngẫu nhiên Z. Nó có tập hợp kết quả {1,3,7,11,12} và phân phối xác suất sau:

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Bạn có thể thấy nó được mô tả trong *Hình 3*. Biến ngẫu nhiên Z, trái ngược với Y, là một biến đều, vì tất cả các xác suất cho các giá trị có thể xảy ra khi lấy mẫu đều bằng nhau.

*Hình 3: Biến ngẫu nhiên Z*
![Hình 3: Biến ngẫu nhiên Z.](assets/Figure2-3.webp "Hình 3: Biến ngẫu nhiên Z")

### Xác suất có điều kiện

Giả sử Bob dự định chọn ngẫu nhiên một ngày từ năm lịch trước. Chúng ta nên kết luận xác suất ngày được chọn rơi vào mùa Hè là bao nhiêu?

Miễn là chúng ta nghĩ rằng quy trình của Bob thực sự sẽ hoàn toàn ngẫu nhiên, chúng ta nên kết luận rằng có xác suất 1/4 Bob chọn một ngày trong mùa Hè. Đây là **xác suất không điều kiện** của việc ngày được chọn ngẫu nhiên rơi vào mùa Hè.

Giả sử bây giờ thay vì chọn ngẫu nhiên một ngày lịch, Bob chỉ chọn ngẫu nhiên từ những ngày mà nhiệt độ buổi trưa tại Crystal Lake (New Jersey) là 21 độ Celcius hoặc cao hơn. Với thông tin bổ sung này, chúng ta có thể kết luận gì về xác suất Bob sẽ chọn một ngày trong mùa Hè?

Chúng ta thực sự nên rút ra một kết luận khác so với trước, ngay cả khi không có thêm thông tin cụ thể nào khác (ví dụ, nhiệt độ buổi trưa mỗi ngày trong năm lịch trước).

Biết rằng Crystal Lake nằm ở New Jersey, chúng ta chắc chắn không mong đợi nhiệt độ buổi trưa đạt 21 độ Celsius hoặc cao hơn vào mùa Đông. Thay vào đó, nó có khả năng cao hơn là một ngày ấm áp vào mùa Xuân hoặc mùa Thu, hoặc một ngày nào đó trong mùa Hè. Do đó, biết rằng nhiệt độ buổi trưa tại Crystal Lake vào ngày được chọn là 21 độ Celsius hoặc cao hơn, xác suất ngày được chọn bởi Bob rơi vào mùa Hè trở nên cao hơn nhiều. Đây là **xác suất có điều kiện** của việc ngày được chọn ngẫu nhiên rơi vào mùa Hè, với điều kiện nhiệt độ buổi trưa tại Crystal Lake là 21 độ Celsius hoặc cao hơn.

Không giống như trong ví dụ trước, xác suất của hai sự kiện cũng có thể hoàn toàn không liên quan. Trong trường hợp đó, chúng ta nói rằng chúng là **độc lập**.

Giả sử, ví dụ, một đồng xu công bằng nào đó đã đáp mặt. Dựa vào sự kiện này, thì xác suất trời mưa ngày mai là bao nhiêu? Xác suất có điều kiện trong trường hợp này nên giống như xác suất không điều kiện trời mưa ngày mai, vì việc tung đồng xu không thường có ảnh hưởng gì đến thời tiết.

Chúng ta sử dụng ký hiệu "|" để viết các phát biểu xác suất có điều kiện. Ví dụ, xác suất của sự kiện $A$ với điều kiện sự kiện $B$ đã xảy ra có thể được viết như sau:

$$
Pr[A|B]
$$

Vậy, khi hai sự kiện, $A$ và $B$, là độc lập, thì:

$$
Pr[A|B] = Pr[A] \text{ và } Pr[B|A] = Pr[B]
$$

Điều kiện cho sự độc lập có thể được đơn giản hóa như sau:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Một kết quả quan trọng trong lý thuyết xác suất được biết đến là **Định lý Bayes**. Nó cơ bản khẳng định rằng $Pr[A|B]$ có thể được viết lại như sau:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Thay vì sử dụng xác suất có điều kiện với các sự kiện cụ thể, chúng ta cũng có thể xem xét xác suất có điều kiện liên quan đến hai hoặc nhiều biến ngẫu nhiên trên một tập hợp các sự kiện có thể xảy ra. Giả sử hai biến ngẫu nhiên, $X$ và $Y$. Chúng ta có thể chỉ định bất kỳ giá trị nào có thể có cho $X$ bằng $x$, và bất kỳ giá trị nào có thể có cho $Y$ bằng $y$. Chúng ta có thể nói, sau đó, rằng hai biến ngẫu nhiên là độc lập nếu phát biểu sau đây đúng:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

cho tất cả $x$ và $y$.

Hãy làm rõ hơn về ý nghĩa của phát biểu này.
Giả sử rằng các tập hợp kết quả cho $X$ và $Y$ được định nghĩa như sau: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ và **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Thông thường, các tập giá trị được chỉ định bằng các chữ cái in đậm, in hoa.)
Bây giờ giả sử bạn lấy mẫu $Y$ và quan sát $y_1$. Phát biểu trên cho chúng ta biết rằng xác suất thu được $x_1$ từ việc lấy mẫu $X$ là hoàn toàn giống như khi chúng ta chưa bao giờ quan sát $y_1$. Điều này đúng với bất kỳ $y_i$ nào mà chúng ta có thể đã rút ra từ việc lấy mẫu ban đầu của $Y$. Cuối cùng, điều này không chỉ đúng với $x_1$. Đối với bất kỳ $x_i$ nào, xác suất xảy ra không bị ảnh hưởng bởi kết quả của việc lấy mẫu $Y$. Tất cả điều này cũng áp dụng cho trường hợp $X$ được lấy mẫu trước.

Hãy kết thúc cuộc thảo luận của chúng ta trên một điểm hơi triết lý hơn. Trong bất kỳ tình huống thực tế nào, xác suất của một sự kiện luôn được đánh giá dựa trên một tập hợp thông tin cụ thể. Không có "xác suất không điều kiện" nào trong bất kỳ nghĩa nào chặt chẽ của từ này.

Ví dụ, giả sử tôi hỏi bạn xác suất lợn sẽ bay vào năm 2030. Mặc dù tôi không cung cấp thêm thông tin nào, bạn rõ ràng biết rất nhiều về thế giới có thể ảnh hưởng đến phán đoán của bạn. Bạn chưa bao giờ thấy lợn bay. Bạn biết rằng hầu hết mọi người sẽ không mong đợi chúng bay. Bạn biết rằng chúng không thực sự được tạo ra để bay. Vân vân.

Do đó, khi chúng ta nói về "xác suất không điều kiện" của một sự kiện trong bối cảnh thực tế, thuật ngữ đó thực sự chỉ có ý nghĩa nếu chúng ta hiểu nó là "xác suất mà không có thêm bất kỳ thông tin rõ ràng nào". Bất kỳ sự hiểu biết nào về "xác suất có điều kiện" nên, sau đó, luôn được hiểu là đối với một mẩu thông tin cụ thể.

Ví dụ, tôi có thể hỏi bạn xác suất lợn sẽ bay vào năm 2030, sau khi cung cấp cho bạn bằng chứng rằng một số con dê ở New Zealand đã học cách bay sau vài năm huấn luyện. Trong trường hợp này, bạn có thể điều chỉnh phán đoán của mình về xác suất lợn sẽ bay vào năm 2030. Vì vậy, xác suất lợn sẽ bay vào năm 2030 phụ thuộc vào bằng chứng này về dê ở New Zealand.

## Phép toán modulo
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

Biểu thức cơ bản nhất với **phép toán modulo** có dạng sau: $x \mod y$.

Biến $x$ được gọi là số bị chia và biến $y$ là số chia. Để thực hiện phép toán modulo với số bị chia dương và số chia dương, bạn chỉ cần xác định phần dư của phép chia.

Ví dụ, xem xét biểu thức $25 \mod 4$. Số 4 chia vào số 25 tổng cộng 6 lần. Phần dư của phép chia là 1. Do đó, $25 \mod 4$ bằng 1. Một cách tương tự, chúng ta có thể đánh giá các biểu thức dưới đây:

* $29 \mod 30 = 29$ (vì 30 chia vào 29 tổng cộng 0 lần và phần dư là 29)
* $42 \mod 2 = 0$ (vì 2 chia vào 42 tổng cộng 21 lần và phần dư là 0)
* $12 \mod 5 = 2$ (vì 5 chia hết vào 12 tổng cộng 2 lần và phần dư là 2)
* $20 \mod 8 = 4$ (vì 8 chia hết vào 20 tổng cộng 2 lần và phần dư là 4)

Khi số bị chia hoặc số chia là số âm, các phép toán modulo có thể được xử lý khác nhau bởi các ngôn ngữ lập trình.

Bạn chắc chắn sẽ gặp các trường hợp với số bị chia âm trong mật mã học. Trong những trường hợp này, cách tiếp cận thông thường như sau:

* Đầu tiên xác định giá trị gần nhất *thấp hơn hoặc bằng* số bị chia mà số chia chia hết với phần dư bằng không. Gọi giá trị đó là $p$.
* Nếu số bị chia là $x$, thì kết quả của phép toán modulo là giá trị của $x – p$.

Ví dụ, giả sử số bị chia là $–20$ và số chia là 3. Giá trị gần nhất thấp hơn hoặc bằng $–20$ mà 3 chia hết đều là $–21$. Giá trị của $x – p$ trong trường hợp này là $–20 – (–21)$. Điều này bằng 1 và, do đó, $–20 \mod 3$ bằng 1. Tương tự, chúng ta có thể đánh giá các biểu thức dưới đây:

* $–8 \mod 5 = 2$
* $–19 \mod 16 = 13$
* $–14 \mod 6 = 4$

Về ký hiệu, bạn sẽ thường thấy các loại biểu thức sau: $x = [y \mod z]$. Do có dấu ngoặc, phép toán modulo trong trường hợp này chỉ áp dụng cho phía bên phải của biểu thức. Nếu $y$ bằng 25 và $z$ bằng 4, ví dụ, thì $x$ được đánh giá là 1.

Không có dấu ngoặc, phép toán modulo tác động lên *cả hai bên* của biểu thức. Giả sử, ví dụ, biểu thức sau: $x = y \mod z$. Nếu $y$ bằng 25 và $z$ bằng 4, thì tất cả những gì chúng ta biết là $x \mod 4$ được đánh giá là 1. Điều này phù hợp với bất kỳ giá trị nào của $x$ từ tập hợp $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.

Nhánh toán học liên quan đến các phép toán modulo trên số và biểu thức được gọi là **số học modulo**. Bạn có thể coi nhánh này như là số học cho các trường hợp mà dãy số không vô hạn dài. Mặc dù chúng ta thường gặp phép toán modulo cho các số nguyên (dương) trong mật mã học, bạn cũng có thể thực hiện các phép toán modulo sử dụng bất kỳ số thực nào.

### Mật mã dịch chuyển

Phép toán modulo thường xuyên được gặp trong mật mã học. Để minh họa, hãy xem xét một trong những hệ thống mã hóa lịch sử nổi tiếng nhất: mật mã dịch chuyển.

Hãy định nghĩa nó trước. Giả sử một từ điển *D* tương đương tất cả các chữ cái của bảng chữ cái tiếng Anh, theo thứ tự, với tập hợp các số $\{0, 1, 2, \ldots, 25\}$. Giả định một không gian tin nhắn **M**. **Mật mã dịch chuyển** là, sau đó, một hệ thống mã hóa được định nghĩa như sau:

- Chọn đồng nhất một khóa $k$ từ không gian khóa **K**, nơi **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Mã hóa một tin nhắn $m \in \mathbf{M}$, như sau:
    - Tách $m$ thành các chữ cái riêng lẻ $m_0, m_1, \ldots, m_i, \ldots, m_l$
- Chuyển đổi mỗi $m_i$ thành một số theo *D*
    - Đối với mỗi $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Chuyển đổi mỗi $c_i$ thành một chữ cái theo *D*
    - Sau đó kết hợp $c_0, c_1, \ldots, c_l$ để tạo ra bản mã $c$
- Giải mã một bản mã $c$ như sau:
    - Chuyển đổi mỗi $c_i$ thành một số theo *D*
    - Đối với mỗi $c_i$, $m_i = [(c_i – k) \mod 26]$
    - Chuyển đổi mỗi $m_i$ thành một chữ cái theo *D*
    - Sau đó kết hợp $m_0, m_1, \ldots, m_l$ để tạo ra thông điệp gốc $m$

Toán tử modulo trong mã dịch chuyển đảm bảo rằng các chữ cái được bao quanh, để tất cả các chữ cái bản mã được định nghĩa. Để minh họa, xem xét việc áp dụng mã dịch chuyển trên từ “DOG”.

Giả sử bạn đã chọn một khóa có giá trị là 17. Chữ “O” tương đương với 15. Nếu không có toán tử modulo, việc cộng số của bản rõ này với khóa sẽ tạo ra một số bản mã là 32. Tuy nhiên, số bản mã đó không thể được chuyển đổi thành một chữ cái bản mã, vì bảng chữ cái tiếng Anh chỉ có 26 chữ cái. Toán tử modulo đảm bảo rằng số bản mã thực sự là 6 (kết quả của $32 \mod 26$), tương đương với chữ cái bản mã “G”.

Toàn bộ quá trình mã hóa từ “DOG” với giá trị khóa là 17 như sau:

* Thông điệp = DOG = D,O,G = 3,15,6
* $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
* $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
* $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
* $c = UGX$

Mọi người có thể hiểu một cách trực quan cách hoạt động của mã dịch chuyển và có thể tự mình sử dụng nó. Tuy nhiên, để nâng cao kiến thức về mật mã học, điều quan trọng là bắt đầu trở nên thoải mái hơn với việc hình thức hóa, vì các kế hoạch sẽ trở nên phức tạp hơn. Do đó, lý do tại sao các bước cho mã dịch chuyển đã được hình thức hóa.

**Ghi chú:**

[1] Chúng ta có thể định nghĩa chính xác câu này, sử dụng thuật ngữ từ phần trước. Hãy để một biến đều $K$ có $K$ là tập hợp các kết quả có thể có. Vậy:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...và cứ thế. Lấy mẫu biến đều $K$ một lần để tạo ra một khóa cụ thể.

## Thao tác XOR
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Tất cả dữ liệu máy tính được xử lý, lưu trữ và gửi qua mạng ở cấp độ bit. Bất kỳ kế hoạch mật mã nào được áp dụng cho dữ liệu máy tính cũng hoạt động ở cấp độ bit.

Chẳng hạn, giả sử bạn đã nhập một e-mail vào ứng dụng e-mail của mình. Bất kỳ mã hóa nào bạn áp dụng không xảy ra trực tiếp trên các ký tự ASCII của e-mail của bạn. Thay vào đó, nó được áp dụng cho biểu diễn bit của các chữ cái và các biểu tượng khác trong e-mail của bạn.
Một phép toán toán học quan trọng cần hiểu cho mã hóa hiện đại, ngoài phép toán modulo, là phép toán **XOR**, hay còn gọi là phép toán "hoặc độc quyền". Phép toán này nhận vào hai bit và cho ra một bit khác. Phép toán XOR sẽ được ký hiệu đơn giản là "XOR". Nó cho ra 0 nếu hai bit giống nhau và 1 nếu hai bit khác nhau. Bạn có thể thấy bốn khả năng dưới đây. Ký hiệu $\oplus$ đại diện cho "XOR":
* $0 \oplus 0 = 0$
* $0 \oplus 1 = 1$
* $1 \oplus 0 = 1$
* $1 \oplus 1 = 0$

Ví dụ, giả sử bạn có một thông điệp $m_1$ (01111001) và một thông điệp $m_2$ (01011001). Phép toán XOR của hai thông điệp này có thể được thấy dưới đây.

* $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

Quy trình này khá đơn giản. Bạn trước tiên XOR các bit bên trái nhất của $m_1$ và $m_2$. Trong trường hợp này là $0 \oplus 0 = 0$. Sau đó bạn XOR cặp bit thứ hai từ bên trái. Trong trường hợp này là $1 \oplus 1 = 0$. Bạn tiếp tục quy trình này cho đến khi bạn đã thực hiện phép toán XOR trên các bit bên phải nhất.

Dễ thấy rằng phép toán XOR là giao hoán, tức là $m_1 \oplus m_2 = m_2 \oplus m_1$. Ngoài ra, phép toán XOR cũng là kết hợp. Đó là, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

Một phép toán XOR trên hai chuỗi có độ dài khác nhau có thể có các cách giải thích khác nhau, tùy thuộc vào bối cảnh. Chúng tôi sẽ không quan tâm ở đây với bất kỳ phép toán XOR nào trên các chuỗi có độ dài khác nhau.

Một phép toán XOR tương đương với trường hợp đặc biệt của việc thực hiện phép toán modulo trên phép cộng của các bit khi số chia là 2. Bạn có thể thấy sự tương đương trong các kết quả sau:

* $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
* $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
* $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
* $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Tính Ngẫu Nhiên Giả
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Trong cuộc thảo luận của chúng tôi về biến ngẫu nhiên và đồng nhất, chúng tôi đã rút ra một sự phân biệt cụ thể giữa “ngẫu nhiên” và “đồng nhất”. Sự phân biệt này thường được duy trì trong thực hành khi mô tả các biến ngẫu nhiên. Tuy nhiên, trong bối cảnh hiện tại của chúng tôi, sự phân biệt này cần được bỏ qua và “ngẫu nhiên” và “đồng nhất” được sử dụng đồng nghĩa. Tôi sẽ giải thích lý do vào cuối phần này.

Để bắt đầu, chúng ta có thể gọi một chuỗi nhị phân có độ dài $n$ là **ngẫu nhiên** (hoặc **đồng nhất**), nếu nó là kết quả của việc lấy mẫu một biến đồng nhất $S$ mà cho mỗi chuỗi nhị phân có độ dài như vậy $n$ một xác suất bằng nhau được chọn.
Giả sử, ví dụ, tập hợp tất cả các chuỗi nhị phân có độ dài 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Thông thường, một chuỗi 8 bit được viết thành hai tứ tệt, mỗi tứ tệt được gọi là một **nibble**.) Hãy gọi tập hợp các chuỗi này là **$S_8$**.

Theo định nghĩa trên, chúng ta có thể gọi một chuỗi nhị phân cụ thể có độ dài 8 là ngẫu nhiên (hoặc đồng nhất), nếu nó là kết quả của việc lấy mẫu một biến ngẫu nhiên $S$ mà cho mỗi chuỗi trong **$S_8$** có một xác suất chọn lựa đồng nhất. Với việc tập hợp **$S_8$** bao gồm $2^8$ phần tử, xác suất chọn lựa khi lấy mẫu sẽ phải là $1/2^8$ cho mỗi chuỗi trong tập hợp.

Một khía cạnh quan trọng của tính ngẫu nhiên của một chuỗi nhị phân là nó được định nghĩa dựa trên quy trình mà nó được chọn. Do đó, hình thức của bất kỳ chuỗi nhị phân cụ thể nào trên chính nó, vì thế, không tiết lộ bất cứ điều gì về tính ngẫu nhiên trong việc chọn lựa.

Ví dụ, nhiều người một cách trực giác có ý tưởng rằng một chuỗi như $1111\ 1111$ không thể được chọn một cách ngẫu nhiên. Nhưng điều này rõ ràng là sai.

Xác định một biến đồng nhất $S$ trên tất cả các chuỗi nhị phân có độ dài 8, khả năng chọn $1111\ 1111$ từ tập hợp **$S_8$** là như nhau so với một chuỗi như $0111\ 0100$. Do đó, bạn không thể biết bất cứ điều gì về tính ngẫu nhiên của một chuỗi, chỉ bằng cách phân tích chính chuỗi đó.

Chúng ta cũng có thể nói về các chuỗi ngẫu nhiên mà không cụ thể chỉ là chuỗi nhị phân. Chúng ta có thể, ví dụ, nói về một chuỗi hex ngẫu nhiên $AF\ 02\ 82$. Trong trường hợp này, chuỗi sẽ được chọn một cách ngẫu nhiên từ tập hợp tất cả các chuỗi hex có độ dài 6. Điều này tương đương với việc chọn ngẫu nhiên một chuỗi nhị phân có độ dài 24, vì mỗi chữ số hex biểu diễn 4 bit.

Thông thường, cụm từ “một chuỗi ngẫu nhiên”, không có điều kiện, ám chỉ một chuỗi được chọn một cách ngẫu nhiên từ tập hợp tất cả các chuỗi có cùng độ dài. Đây là cách tôi đã mô tả ở trên. Một chuỗi có độ dài $n$ có thể, tất nhiên, cũng được chọn một cách ngẫu nhiên từ một tập hợp khác. Một tập hợp, ví dụ, chỉ bao gồm một tập hợp con của tất cả các chuỗi có độ dài $n$, hoặc có thể là một tập hợp bao gồm các chuỗi có độ dài khác nhau. Trong những trường hợp đó, tuy nhiên, chúng ta sẽ không gọi nó là “một chuỗi ngẫu nhiên”, mà là “một chuỗi được chọn một cách ngẫu nhiên từ một tập hợp **S**”.

Một khái niệm chủ chốt trong mật mã học là tính giả ngẫu nhiên. Một **chuỗi giả ngẫu nhiên** có độ dài $n$ xuất hiện *như thể* nó là kết quả của việc lấy mẫu một biến đồng nhất $S$ mà cho mỗi chuỗi trong **$S_n$** một xác suất chọn lựa đồng nhất. Tuy nhiên, thực tế, chuỗi là kết quả của việc lấy mẫu một biến đồng nhất $S'$ chỉ định một phân phối xác suất—không nhất thiết với xác suất đồng nhất cho tất cả các kết quả có thể—trên một tập hợp con của **$S_n$**. Điểm then chốt ở đây là không ai có thể thực sự phân biệt giữa các mẫu từ $S$ và $S'$, ngay cả khi bạn lấy nhiều mẫu.
Giả sử, chẳng hạn, một biến ngẫu nhiên $S$. Tập hợp kết quả của nó là **$S_{256}$**, đây là tập hợp tất cả các chuỗi nhị phân có độ dài 256. Tập hợp này có $2^{256}$ phần tử. Mỗi phần tử có một xác suất bằng nhau khi được chọn, $1/2^{256}$, khi lấy mẫu.

Ngoài ra, giả sử một biến ngẫu nhiên $S'$. Tập hợp kết quả của nó chỉ bao gồm $2^{128}$ chuỗi nhị phân có độ dài 256. Nó có một số phân phối xác suất đối với những chuỗi đó, nhưng phân phối này không nhất thiết phải đồng đều.

Giả sử rằng bây giờ tôi lấy 1000s mẫu từ $S$ và 1000s mẫu từ $S'$ và đưa hai tập hợp kết quả cho bạn. Tôi nói cho bạn biết tập hợp kết quả nào tương ứng với biến ngẫu nhiên nào. Tiếp theo, tôi lấy một mẫu từ một trong hai biến ngẫu nhiên. Nhưng lần này tôi không nói cho bạn biết tôi lấy mẫu từ biến ngẫu nhiên nào. Nếu $S'$ là giả ngẫu nhiên, thì ý tưởng là khả năng bạn đoán đúng biến ngẫu nhiên mà tôi lấy mẫu thực tế không tốt hơn $1/2$.

Thông thường, một chuỗi giả ngẫu nhiên có độ dài $n$ được tạo ra bằng cách chọn ngẫu nhiên một chuỗi có kích thước $n – x$, nơi $x$ là một số nguyên dương, và sử dụng nó làm đầu vào cho một thuật toán mở rộng. Chuỗi ngẫu nhiên này có kích thước $n – x$ được biết đến là **hạt giống**.

Chuỗi giả ngẫu nhiên là một khái niệm chính để làm cho mật mã học trở nên thiết thực. Xem xét, chẳng hạn, các mật mã dòng. Với một mật mã dòng, một khóa được chọn ngẫu nhiên được cắm vào một thuật toán mở rộng để tạo ra một chuỗi giả ngẫu nhiên lớn hơn nhiều. Chuỗi giả ngẫu nhiên này sau đó được kết hợp với bản rõ thông qua một hoạt động XOR để tạo ra một bản mã.

Nếu chúng ta không thể tạo ra loại chuỗi giả ngẫu nhiên này cho một mật mã dòng, thì chúng ta sẽ cần một khóa có độ dài bằng với thông điệp để đảm bảo an ninh. Đây không phải là một lựa chọn thực tế trong hầu hết các trường hợp.

Khái niệm về giả ngẫu nhiên được thảo luận trong phần này có thể được định nghĩa một cách chính thức hơn. Nó cũng mở rộng sang các bối cảnh khác. Nhưng chúng ta không cần phải đi sâu vào cuộc thảo luận đó ở đây. Tất cả những gì bạn thực sự cần hiểu một cách trực quan cho phần lớn mật mã học là sự khác biệt giữa một chuỗi ngẫu nhiên và một chuỗi giả ngẫu nhiên. [2]

Lý do để bỏ qua sự phân biệt giữa “ngẫu nhiên” và “đồng đều” trong cuộc thảo luận của chúng ta bây giờ cũng nên rõ ràng. Trên thực tế, mọi người sử dụng thuật ngữ giả ngẫu nhiên để chỉ một chuỗi có vẻ **như thể** nó là kết quả của việc lấy mẫu một biến đồng đều $S$. Nói một cách nghiêm túc, chúng ta nên gọi một chuỗi như vậy là “giả đồng đều,” áp dụng ngôn ngữ của chúng ta từ trước. Vì thuật ngữ “giả đồng đều” vừa cồng kềnh và không được ai sử dụng, chúng ta sẽ không giới thiệu nó ở đây cho rõ ràng. Thay vào đó, chúng ta chỉ bỏ qua sự phân biệt giữa “ngẫu nhiên” và “đồng đều” trong bối cảnh hiện tại.

**Ghi chú**

[2] Nếu quan tâm đến một bài trình bày chính thức hơn về những vấn đề này, bạn có thể tham khảo *Introduction to Modern Cryptography* của Katz và Lindell, đặc biệt là chương 3.


# Cơ sở Toán học của Mật mã học 2
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

## Lý thuyết số là gì?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>
Chương này trình bày về một chủ đề nâng cao hơn trong nền tảng toán học của mật mã học: lý thuyết số. Mặc dù lý thuyết số quan trọng đối với mật mã đối xứng (như trong Mã hóa Rijndael), nó đặc biệt quan trọng trong cài đặt mật mã công khai.

Nếu bạn thấy chi tiết của lý thuyết số khó hiểu, tôi khuyên bạn nên đọc sơ qua lần đầu. Bạn luôn có thể quay lại nó vào một thời điểm sau.

___

Bạn có thể mô tả **lý thuyết số** là việc nghiên cứu về các tính chất của số nguyên và các hàm toán học làm việc với số nguyên.

Xem xét, chẳng hạn, rằng bất kỳ hai số $a$ và $N$ là **nguyên tố cùng nhau** (hoặc **số nguyên tương đối**) nếu ước chung lớn nhất của chúng bằng 1. Giả sử bây giờ một số nguyên cụ thể $N$. Có bao nhiêu số nguyên nhỏ hơn $N$ là nguyên tố cùng nhau với $N$? Chúng ta có thể đưa ra các phát biểu chung về câu trả lời cho câu hỏi này không? Đây là các loại câu hỏi điển hình mà lý thuyết số tìm cách trả lời.

Lý thuyết số hiện đại dựa vào các công cụ của đại số trừu tượng. Lĩnh vực **đại số trừu tượng** là một phân ngành của toán học nơi các đối tượng chính của phân tích là các đối tượng trừu tượng được biết đến như cấu trúc đại số. Một **cấu trúc đại số** là một tập hợp các phần tử kết hợp với một hoặc nhiều phép toán, tuân theo một số tiên đề nhất định. Thông qua cấu trúc đại số, các nhà toán học có thể thu được cái nhìn sâu sắc vào các vấn đề toán học cụ thể, bằng cách trừu tượng hóa khỏi chi tiết của chúng.

Lĩnh vực đại số trừu tượng đôi khi cũng được gọi là đại số hiện đại. Bạn cũng có thể gặp khái niệm **toán học trừu tượng** (hoặc **toán học thuần túy**). Thuật ngữ sau không phải là một tham chiếu đến đại số trừu tượng, mà thực sự nghĩa là việc nghiên cứu toán học vì chính nó, và không chỉ với mục đích nhìn vào các ứng dụng tiềm năng.

Các tập hợp từ đại số trừu tượng có thể đối phó với nhiều loại đối tượng, từ các biến đổi bảo toàn hình dạng trên một tam giác đều đến các mẫu hình nền. Đối với lý thuyết số, chúng ta chỉ xem xét các tập hợp các phần tử chứa số nguyên hoặc các hàm làm việc với số nguyên.

## Nhóm
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Một khái niệm cơ bản trong toán học là tập hợp các phần tử. Một tập hợp thường được ký hiệu bằng dấu ngoặc nhọn với các phần tử được phân tách bằng dấu phẩy.

Ví dụ, tập hợp tất cả các số nguyên là $\{…, -2, -1, 0, 1, 2, …\}$. Các dấu ba chấm ở đây có nghĩa là một mẫu nhất định tiếp tục theo một hướng cụ thể. Vì vậy, tập hợp tất cả các số nguyên cũng bao gồm $3, 4, 5, 6$ và tiếp tục, cũng như $-3, -4, -5, -6$ và tiếp tục. Tập hợp tất cả các số nguyên này thường được ký hiệu là $\mathbb{Z}$.

Một ví dụ khác về tập hợp là $\mathbb{Z} \mod 11$, hoặc tập hợp tất cả các số nguyên modulo 11. Trái ngược với toàn bộ tập hợp $\mathbb{Z}$, tập hợp này chỉ chứa một số lượng hữu hạn các phần tử, cụ thể là $\{0, 1, \ldots, 9, 10\}$.
Một sai lầm phổ biến là nghĩ rằng tập hợp $\mathbb{Z} \mod 11$ thực sự là $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Nhưng thực tế không phải vậy, dựa vào cách chúng ta đã định nghĩa phép toán modulo trước đó. Bất kỳ số nguyên âm nào khi được giảm bằng modulo 11 sẽ được chuyển vào tập hợp $\{0, 1, \ldots, 9, 10\}$. Ví dụ, biểu thức $-2 \mod 11$ được chuyển thành $9$, trong khi biểu thức $-27 \mod 11$ được chuyển thành $5$.

Một khái niệm cơ bản khác trong toán học là phép toán nhị phân. Đây là bất kỳ phép toán nào lấy hai phần tử để tạo ra một phần tử thứ ba. Ví dụ, từ toán học cơ bản và đại số, bạn sẽ quen thuộc với bốn phép toán nhị phân cơ bản: cộng, trừ, nhân và chia.

Hai khái niệm toán học cơ bản này, tập hợp và phép toán nhị phân, được sử dụng để định nghĩa khái niệm về nhóm, cấu trúc quan trọng nhất trong đại số trừu tượng.

Cụ thể, giả sử một phép toán nhị phân $\circ$. Ngoài ra, giả sử một tập hợp các phần tử **S** được trang bị phép toán đó. "Được trang bị" ở đây có nghĩa là phép toán $\circ$ có thể được thực hiện giữa bất kỳ hai phần tử nào trong tập hợp **S**.

Sự kết hợp $\langle \mathbf{S}, \circ \rangle$ là một **nhóm** nếu nó đáp ứng bốn điều kiện cụ thể, được biết đến như các tiên đề nhóm.

1. Đối với bất kỳ $a$ và $b$ nào là các phần tử của $\mathbf{S}$, $a \circ b$ cũng là một phần tử của $\mathbf{S}$. Điều này được biết đến là **điều kiện đóng**.
2. Đối với bất kỳ $a$, $b$, và $c$ nào là các phần tử của $\mathbf{S}$, thì $(a \circ b) \circ c = a \circ (b \circ c)$. Điều này được biết đến là **điều kiện kết hợp**.
3. Có một phần tử duy nhất $e$ trong $\mathbf{S}$, sao cho với mọi phần tử $a$ trong $\mathbf{S}$, phương trình sau đây được thỏa mãn: $e \circ a = a \circ e = a$. Vì chỉ có một phần tử như vậy $e$, nó được gọi là **phần tử đơn vị**. Điều kiện này được biết đến là **điều kiện đơn vị**.
4. Đối với mỗi phần tử $a$ trong $\mathbf{S}$, tồn tại một phần tử $b$ trong $\mathbf{S}$, sao cho phương trình sau đây được thỏa mãn: $a \circ b = b \circ a = e$, nơi $e$ là phần tử đơn vị. Phần tử $b$ ở đây được biết đến là **phần tử nghịch đảo**, và thường được ký hiệu là $a^{-1}$. Điều kiện này được biết đến là **điều kiện nghịch đảo** hoặc **điều kiện khả năng đảo ngược**.

Hãy khám phá thêm về nhóm. Ký hiệu tập hợp tất cả các số nguyên bằng $\mathbb{Z}$. Tập hợp này kết hợp với phép cộng tiêu chuẩn, hay $\langle \mathbb{Z}, + \rangle$, rõ ràng phù hợp với định nghĩa của một nhóm, vì nó đáp ứng bốn tiên đề trên.

1. Đối với bất kỳ $x$ và $y$ nào là các phần tử của $\mathbb{Z}$, $x + y$ cũng là một phần tử của $\mathbb{Z}$. Vì vậy $\langle \mathbb{Z}, + \rangle$ đáp ứng điều kiện đóng.
2. Đối với bất kỳ $x$, $y$, và $z$ nào là các phần tử của $\mathbb{Z}$, $(x + y) + z = x + (y + z)$. Vì vậy, $\langle \mathbb{Z}, + \rangle$ thỏa mãn điều kiện kết hợp.

3. Có một phần tử đồng nhất trong $\langle \mathbb{Z}, + \rangle$, cụ thể là 0. Đối với bất kỳ $x$ nào trong $\mathbb{Z}$, điều này có nghĩa là: $0 + x = x + 0 = x$. Vì vậy, $\langle \mathbb{Z}, + \rangle$ thỏa mãn điều kiện đồng nhất.

4. Cuối cùng, đối với mỗi phần tử $x$ trong $\mathbb{Z}$, có một $y$ sao cho $x + y = y + x = 0$. Nếu $x$ là 10, ví dụ, $y$ sẽ là $-10$ (trong trường hợp $x$ là 0, $y$ cũng là 0). Vì vậy, $\langle \mathbb{Z}, + \rangle$ thỏa mãn điều kiện nghịch đảo.

Quan trọng là, việc tập hợp các số nguyên với phép cộng tạo thành một nhóm không có nghĩa là nó tạo thành một nhóm với phép nhân. Bạn có thể xác minh điều này bằng cách kiểm tra $\langle \mathbb{Z}, \cdot \rangle$ đối với bốn tiên đề của nhóm (nơi $\cdot$ có nghĩa là phép nhân tiêu chuẩn).

Hai tiên đề đầu tiên rõ ràng được thỏa mãn. Ngoài ra, dưới phép nhân, phần tử 1 có thể đóng vai trò là phần tử đồng nhất. Bất kỳ số nguyên $x$ nào nhân với 1, cụ thể là cho ra $x$. Tuy nhiên, $\langle \mathbb{Z}, \cdot \rangle$ không thỏa mãn điều kiện nghịch đảo. Đó là, không có một phần tử duy nhất $y$ trong $\mathbb{Z}$ cho mỗi $x$ trong $\mathbb{Z}$, sao cho $x \cdot y = 1$.

Ví dụ, giả sử $x = 22$. Giá trị $y$ nào từ tập hợp $\mathbb{Z}$ nhân với $x$ sẽ cho ra phần tử đồng nhất 1? Giá trị của $1/22$ sẽ phù hợp, nhưng điều này không nằm trong tập hợp $\mathbb{Z}$. Thực tế, bạn sẽ gặp phải vấn đề này với bất kỳ số nguyên $x$ nào, ngoại trừ các giá trị của 1 và -1 (nơi $y$ sẽ phải là 1 và -1 tương ứng).

Nếu chúng ta cho phép sử dụng số thực cho tập hợp của chúng ta, thì phần lớn vấn đề sẽ biến mất. Đối với bất kỳ phần tử $x$ nào trong tập hợp, phép nhân với $1/x$ cho ra 1. Vì phân số được bao gồm trong tập hợp các số thực, một phần tử nghịch đảo có thể được tìm thấy cho mọi số thực. Ngoại lệ là số không, vì bất kỳ phép nhân nào với số không sẽ không bao giờ cho ra phần tử đồng nhất 1. Do đó, tập hợp các số thực không bằng không được trang bị phép nhân thực sự là một nhóm.

Một số nhóm thỏa mãn một điều kiện tổng quát thứ năm, được biết đến là **điều kiện giao hoán**. Điều kiện này như sau:

* Giả sử một nhóm $G$ với tập hợp **S** và một toán tử nhị phân $\circ$. Giả sử $a$ và $b$ là các phần tử của **S**. Nếu trường hợp $a \circ b = b \circ a$ đúng cho bất kỳ hai phần tử $a$ và $b$ nào trong **S**, thì $G$ thỏa mãn điều kiện giao hoán.
Bất kỳ nhóm nào thỏa mãn điều kiện giao hoán được biết đến là **nhóm giao hoán**, hoặc **nhóm Abel** (đặt theo tên của Niels Henrik Abel). Việc xác minh rằng cả tập hợp số thực qua phép cộng và tập hợp số nguyên qua phép cộng đều là nhóm Abel là điều dễ dàng. Tập hợp số nguyên qua phép nhân không phải là một nhóm, do đó không thể là một nhóm Abel. Ngược lại, tập hợp các số thực khác không qua phép nhân cũng là một nhóm Abel.

Bạn nên chú ý đến hai quy ước quan trọng về ký hiệu. Đầu tiên, các dấu “+” hoặc “×” thường xuyên được sử dụng để biểu thị các phép toán nhóm, ngay cả khi các phần tử không phải là số. Trong những trường hợp này, bạn không nên hiểu những dấu hiệu này như là phép cộng hoặc nhân tiêu chuẩn. Thay vào đó, chúng là các phép toán chỉ có sự tương đồng trừu tượng với các phép toán số học này.

Trừ khi bạn cụ thể đề cập đến phép cộng hoặc nhân số học, việc sử dụng các biểu tượng như $\circ$ và $\diamond$ cho các phép toán nhóm là dễ dàng hơn, vì những biểu tượng này không mang nhiều ý nghĩa văn hóa sâu đậm.

Thứ hai, cùng một lý do mà “+” và “×” thường được sử dụng để chỉ ra các phép toán không phải số học, các phần tử đồng nhất của nhóm thường được biểu thị bằng “0” và “1”, ngay cả khi các phần tử trong nhóm này không phải là số. Trừ khi bạn đang đề cập đến phần tử đồng nhất của một nhóm có số, việc sử dụng một biểu tượng trung lập hơn như “$e$” để chỉ phần tử đồng nhất là dễ dàng hơn.

Nhiều tập hợp giá trị khác nhau và rất quan trọng trong toán học, được trang bị các phép toán nhị phân nhất định, là nhóm. Tuy nhiên, các ứng dụng mật mã chỉ làm việc với các tập hợp số nguyên hoặc ít nhất là các phần tử được mô tả bằng số nguyên, tức là, trong lĩnh vực lý thuyết số. Do đó, các tập hợp với số thực khác với số nguyên không được sử dụng trong các ứng dụng mật mã.

Hãy kết thúc bằng việc cung cấp một ví dụ về các phần tử có thể được “mô tả bằng số nguyên”, mặc dù chúng không phải là số nguyên. Một ví dụ tốt là các điểm của đường cong elliptic. Mặc dù bất kỳ điểm nào trên đường cong elliptic rõ ràng không phải là số nguyên, nhưng điểm đó thực sự được mô tả bởi hai số nguyên.

Đường cong elliptic, ví dụ, rất quan trọng đối với Bitcoin. Bất kỳ cặp khóa riêng và khóa công khai tiêu chuẩn nào của Bitcoin đều được chọn từ tập hợp các điểm được định nghĩa bởi đường cong elliptic sau:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(số nguyên tố lớn nhất nhỏ hơn $2^{256}$). Tọa độ $x$ là khóa riêng và tọa độ $y$ là khóa công khai của bạn.

Các giao dịch trong Bitcoin thường liên quan đến việc khóa đầu ra với một hoặc nhiều khóa công khai theo một cách nào đó. Giá trị từ những giao dịch này có thể, sau đó, được mở khóa bằng cách tạo chữ ký số với các khóa riêng tương ứng.

## Nhóm tuần hoàn
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Một sự phân biệt quan trọng mà chúng ta có thể rút ra là giữa **nhóm hữu hạn** và **nhóm vô hạn**. Nhóm đầu tiên có một số lượng phần tử hữu hạn, trong khi nhóm sau có một số lượng phần tử vô hạn. Số lượng phần tử trong bất kỳ nhóm hữu hạn nào được biết đến là **bậc của nhóm**. Tất cả các ứng dụng mật mã thực tế liên quan đến việc sử dụng nhóm đều dựa trên nhóm hữu hạn (lý thuyết số).

Trong mật mã khóa công khai, một lớp nhất định của nhóm Abel hữu hạn được biết đến là nhóm tuần hoàn rất quan trọng. Để hiểu về nhóm tuần hoàn, trước tiên chúng ta cần hiểu về khái niệm lũy thừa phần tử nhóm.
Giả sử một nhóm $G$ với phép toán nhóm $\circ$, và $a$ là một phần tử của $G$. Biểu thức $a^n$ nên được hiểu là phần tử $a$ kết hợp với chính nó tổng cộng $n – 1$ lần. Ví dụ, $a^2$ có nghĩa là $a \circ a$, $a^3$ có nghĩa là $a \circ a \circ a$, và cứ thế tiếp tục. (Lưu ý rằng phép lũy thừa ở đây không nhất thiết là phép lũy thừa trong nghĩa số học tiêu chuẩn.)

Hãy xem xét một ví dụ. Giả sử $G = \langle \mathbb{Z} \mod 7, + \rangle$, và giá trị của $a$ bằng 4. Trong trường hợp này, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Ngược lại, $a^4$ sẽ được biểu diễn là $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Một số nhóm Abel có một hoặc nhiều phần tử, có thể tạo ra tất cả các phần tử nhóm khác thông qua phép lũy thừa liên tục. Những phần tử này được gọi là **bộ sinh** hoặc **phần tử nguyên thủy**.

Một lớp quan trọng của những nhóm như vậy là $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, nơi $N$ là một số nguyên tố. Ký hiệu $\mathbb{Z}^*$ ở đây có nghĩa là nhóm chứa tất cả các số nguyên dương không bằng không nhỏ hơn $N$. Do đó, nhóm này luôn có $N – 1$ phần tử.

Xem xét, ví dụ, $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Nhóm này có các phần tử sau: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Cấp của nhóm này là 10 (đúng bằng $11 – 1$).

Hãy khám phá việc lũy thừa phần tử 2 từ nhóm này. Các phép tính cho đến $2^{12}$ được hiển thị dưới đây. Lưu ý rằng ở phía bên trái của phương trình, số mũ ám chỉ phép lũy thừa phần tử nhóm. Trong ví dụ cụ thể của chúng ta, điều này thực sự liên quan đến phép lũy thừa số học ở phía bên phải của phương trình (nhưng nó cũng có thể liên quan, ví dụ, đến phép cộng). Để làm rõ, tôi đã viết ra phép toán lặp lại, thay vì dạng số mũ ở phía bên phải.

* $2^1 = 2 \mod 11$
* $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
* $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
* $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
* $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
* $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
* $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
* $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
* $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
* $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
* $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
* $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Nếu bạn quan sát kỹ, bạn có thể thấy rằng việc thực hiện phép lũy thừa với phần tử 2 lặp qua tất cả các phần tử của $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ theo thứ tự sau: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Sau $2^{10}$, việc tiếp tục lũy thừa phần tử 2 lặp lại tất cả các phần tử một lần nữa và theo cùng một thứ tự. Do đó, phần tử 2 là một sinh tử trong $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Mặc dù $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ có nhiều sinh tử, không phải tất cả các phần tử của nhóm này đều là sinh tử. Xem xét, ví dụ, phần tử 3. Thực hiện 10 phép lũy thừa đầu tiên, không hiển thị các phép tính phức tạp, cho kết quả sau:

* $3^1 = 3 \mod 11$
* $3^2 = 9 \mod 11$
* $3^3 = 5 \mod 11$
* $3^4 = 4 \mod 11$
* $3^5 = 1 \mod 11$
* $3^6 = 3 \mod 11$
* $3^7 = 9 \mod 11$
* $3^8 = 5 \mod 11$
* $3^9 = 4 \mod 11$
* $3^{10} = 1 \mod 11$
Thay vì lặp qua tất cả các giá trị trong $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, việc lũy thừa phần tử 3 chỉ dẫn đến một tập hợp con của những giá trị đó: 3, 9, 5, 4, và 1. Sau lần lũy thừa thứ năm, những giá trị này bắt đầu lặp lại.

Chúng ta có thể định nghĩa một **nhóm tuần hoàn** là bất kỳ nhóm nào có ít nhất một sinh tử. Nghĩa là, có ít nhất một phần tử của nhóm từ đó bạn có thể tạo ra tất cả các phần tử khác của nhóm thông qua lũy thừa.

Bạn có thể đã nhận thấy trong ví dụ trên của chúng tôi rằng cả $2^{10}$ và $3^{10}$ đều bằng $1 \mod 11$. Thực tế, mặc dù chúng tôi sẽ không thực hiện các phép tính, việc lũy thừa bằng 10 của bất kỳ phần tử nào trong nhóm $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ sẽ cho kết quả là $1 \mod 11$. Tại sao lại như vậy?

Đây là một câu hỏi quan trọng, nhưng cần một số công việc để trả lời.

Để bắt đầu, giả sử hai số nguyên dương $a$ và $N$. Một định lý quan trọng trong lý thuyết số nói rằng $a$ có nghịch đảo nhân modulo $N$ (nghĩa là, một số nguyên $b$ sao cho $a \cdot b = 1 \mod N$) nếu và chỉ nếu ước chung lớn nhất giữa $a$ và $N$ bằng 1. Nghĩa là, nếu $a$ và $N$ là hai số nguyên tố cùng nhau.

Vì vậy, đối với bất kỳ nhóm số nguyên nào được trang bị phép nhân modulo $N$, chỉ những số nguyên tố cùng nhau nhỏ hơn với $N$ mới được bao gồm trong tập hợp. Chúng ta có thể ký hiệu tập hợp này bằng $\mathbb{Z}^c \mod N$.

Ví dụ, giả sử $N$ là 10. Chỉ có các số nguyên 1, 3, 7, và 9 là số nguyên tố cùng nhau với 10. Vì vậy, tập hợp $\mathbb{Z}^c \mod 10$ chỉ bao gồm $\{1, 3, 7, 9\}$. Bạn không thể tạo ra một nhóm với phép nhân số nguyên modulo 10 sử dụng bất kỳ số nguyên nào khác từ 1 đến 10. Đối với nhóm cụ thể này, các nghịch đảo là các cặp 1 và 9, và 3 và 7.

Trong trường hợp $N$ chính là một số nguyên tố, tất cả các số nguyên từ 1 đến $N – 1$ đều là số nguyên tố cùng nhau với $N$. Như vậy, một nhóm như vậy có bậc là $N – 1$. Sử dụng ký hiệu trước đây của chúng tôi, $\mathbb{Z}^c \mod N$ bằng $\mathbb{Z}^* \mod N$ khi $N$ là số nguyên tố. Nhóm mà chúng tôi đã chọn cho ví dụ trước đây, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, là một ví dụ cụ thể của lớp nhóm này.

Tiếp theo, hàm $\phi(N)$ tính số lượng số nguyên tố cùng nhau cho đến một số $N$, và được biết đến là **Hàm Phi của Euler**. [1] Theo **Định lý Euler**, bất cứ khi nào hai số nguyên $a$ và $N$ là số nguyên tố cùng nhau, điều sau đây được giữ:

* $a^{\phi(N)} \mod N = 1 \mod N$
Điều này có một ý nghĩa quan trọng đối với lớp các nhóm $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ nơi $N$ là số nguyên tố. Đối với những nhóm này, phép lũy thừa của phần tử nhóm đại diện cho phép lũy thừa số học. Cụ thể, $a^{\phi(N)} \mod N$ đại diện cho phép toán số học $a^{\phi(N)} \mod N$. Vì mọi phần tử $a$ trong những nhóm nhân này đều nguyên tố cùng nhau với $N$, điều này có nghĩa là $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.

Định lý Euler là một kết quả thực sự quan trọng. Đầu tiên, nó ngụ ý rằng tất cả các phần tử trong $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ chỉ có thể lặp qua một số lượng giá trị bằng phép lũy thừa chia hết cho $N – 1$. Trong trường hợp của $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, điều này có nghĩa là mỗi phần tử chỉ có thể lặp qua 2, 5, hoặc 10 phần tử. Các giá trị nhóm mà bất kỳ phần tử nào lặp qua qua phép lũy thừa được biết đến là **bậc của phần tử**. Một phần tử có bậc tương đương với bậc của một nhóm là một sinh viên.

Hơn nữa, định lý Euler ngụ ý rằng chúng ta luôn biết kết quả của $a^{N – 1} \mod N$ cho bất kỳ nhóm $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ nào mà $N$ là số nguyên tố. Điều này đúng bất kể các phép tính thực tế có thể phức tạp như thế nào.

Ví dụ, giả sử nhóm của chúng ta là $\mathbb{Z}^* \mod 160,481,182$ (nơi 160,481,182 thực sự là một số nguyên tố). Chúng ta biết rằng tất cả các số nguyên từ 1 đến 160,481,181 phải là các phần tử của nhóm này, và rằng $\phi(n) = 160,481,181$. Mặc dù chúng ta không thể thực hiện tất cả các bước trong các phép tính, chúng ta biết rằng các biểu thức như $514^{160,481,181}$, $2,005^{160,481,181}$, và $256,212^{160,481,181}$ đều phải đánh giá là $1 \mod 160,481,182$.

**Ghi chú:**

[1] Hàm hoạt động như sau. Bất kỳ số nguyên $N$ nào cũng có thể được phân tích thành một tích của các số nguyên tố. Giả sử một $N$ cụ thể được phân tích như sau: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ nơi tất cả các $p$ đều là các số nguyên tố và tất cả các $e$ đều là các số nguyên lớn hơn hoặc bằng 1. Sau đó:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Công thức hàm Phi của Euler cho phân tích số nguyên tố của $N$.

## Lĩnh Vực
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Một nhóm là cấu trúc đại số cơ bản trong đại số trừu tượng, nhưng còn nhiều cấu trúc đại số khác. Cấu trúc đại số duy nhất khác mà bạn cần quen thuộc là của một **trường**, cụ thể là của một **trường hữu hạn**. Loại cấu trúc đại số này thường được sử dụng trong mật mã học, như trong Tiêu chuẩn Mã hóa Nâng cao. Đây là lược đồ mã hóa đối xứng chính mà bạn sẽ gặp trong thực tế.
Một trường được phát triển từ khái niệm của một nhóm. Cụ thể, một **trường** là một tập hợp các phần tử **S** được trang bị hai toán tử nhị phân $\circ$ và $\diamond$, đáp ứng các điều kiện sau:
1. Tập hợp **S** được trang bị $\circ$ là một nhóm Abel.
2. Tập hợp **S** được trang bị $\diamond$ là một nhóm Abel đối với các phần tử “không bằng không”.
3. Tập hợp **S** được trang bị hai toán tử đáp ứng điều kiện phân phối: Giả sử $a$, $b$, và $c$ là các phần tử của **S**. Khi đó **S** được trang bị hai toán tử đáp ứng tính chất phân phối khi $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Lưu ý rằng, giống như với các nhóm, định nghĩa của một trường rất trừu tượng. Nó không đưa ra bất kỳ tuyên bố nào về loại các phần tử trong **S**, hoặc về các phép toán $\circ$ và $\diamond$. Nó chỉ nói rằng một trường là bất kỳ tập hợp các phần tử nào với hai phép toán mà ba điều kiện trên được thỏa mãn. (Phần tử “không” trong nhóm Abel thứ hai có thể được hiểu một cách trừu tượng.)

Vậy một ví dụ về trường có thể là gì? Một ví dụ tốt là tập hợp $\mathbb{Z} \mod 7$, hoặc $\{0, 1, \ldots, 7\}$ được định nghĩa trên phép cộng chuẩn (thay cho $\circ$ ở trên) và phép nhân chuẩn (thay cho $\diamond$ ở trên).

Đầu tiên, $\mathbb{Z} \mod 7$ đáp ứng điều kiện để trở thành một nhóm Abel qua phép cộng, và nó đáp ứng điều kiện để trở thành một nhóm Abel qua phép nhân nếu bạn chỉ xem xét các phần tử không bằng không. Thứ hai, sự kết hợp của tập hợp với hai toán tử đáp ứng điều kiện phân phối.

Việc khám phá những tuyên bố này bằng cách sử dụng một số giá trị cụ thể là rất có giá trị về mặt giáo dục. Hãy lấy các giá trị thử nghiệm 5, 2, và 3, một số phần tử được chọn ngẫu nhiên từ tập hợp $\mathbb{Z} \mod 7$, để kiểm tra trường $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Chúng ta sẽ sử dụng ba giá trị này theo thứ tự, như cần thiết để khám phá các điều kiện cụ thể.

Hãy khám phá xem $\mathbb{Z} \mod 7$ được trang bị phép cộng là một nhóm Abel hay không.

1. **Điều kiện đóng**: Hãy lấy 5 và 2 làm giá trị của chúng ta. Trong trường hợp đó, $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Đây thực sự là một phần tử của $\mathbb{Z} \mod 7$, vì vậy kết quả phù hợp với điều kiện đóng.
2. **Điều kiện kết hợp**: Hãy lấy 5, 2, và 3 làm giá trị của chúng ta. Trong trường hợp đó, $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Điều này phù hợp với điều kiện kết hợp.
3. **Điều kiện phần tử đơn vị**: Hãy lấy 5 làm giá trị của chúng ta. Trong trường hợp đó, $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Vậy 0 có vẻ là phần tử đơn vị cho phép cộng.
4. **Điều kiện nghịch đảo**: Xét nghịch đảo của 5. Cần phải có $[5 + d] \mod 7 = 0$, với một giá trị $d$ nào đó. Trong trường hợp này, giá trị duy nhất từ $\mathbb{Z} \mod 7$ thỏa mãn điều kiện này là 2.
5. **Điều kiện giao hoán**: Hãy lấy 5 và 3 làm giá trị của chúng ta. Trong trường hợp này, $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Điều này phù hợp với điều kiện giao hoán.

Tập hợp $\mathbb{Z} \mod 7$ khi kết hợp với phép cộng rõ ràng là một nhóm Abel. Bây giờ, hãy khám phá xem $\mathbb{Z} \mod 7$ khi kết hợp với phép nhân có phải là một nhóm Abel đối với tất cả các phần tử khác không hay không.

1. **Điều kiện đóng**: Hãy lấy 5 và 2 làm giá trị của chúng ta. Trong trường hợp này, $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Đây cũng là một phần tử của $\mathbb{Z} \mod 7$, vì vậy kết quả phù hợp với điều kiện đóng.
2. **Điều kiện kết hợp**: Hãy lấy 5, 2, và 3 làm giá trị của chúng ta. Trong trường hợp này, $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Điều này phù hợp với điều kiện kết hợp.
3. **Điều kiện phần tử đơn vị**: Hãy lấy 5 làm giá trị của chúng ta. Trong trường hợp này, $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Vì vậy, 1 có vẻ là phần tử đơn vị cho phép nhân.
4. **Điều kiện nghịch đảo**: Xét nghịch đảo của 5. Cần phải có $[5 \cdot d] \mod 7 = 1$, với một giá trị $d$ nào đó. Giá trị duy nhất từ $\mathbb{Z} \mod 7$ thỏa mãn điều kiện này là 3. Điều này phù hợp với điều kiện nghịch đảo.
5. **Điều kiện giao hoán**: Hãy lấy 5 và 3 làm giá trị của chúng ta. Trong trường hợp này, $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Điều này phù hợp với điều kiện giao hoán.

Tập hợp $\mathbb{Z} \mod 7$ rõ ràng dường như đáp ứng các quy tắc để trở thành một nhóm Abel khi kết hợp với phép cộng hoặc phép nhân trên các phần tử khác không.

Cuối cùng, tập hợp này khi kết hợp với cả hai toán tử dường như đáp ứng điều kiện phân phối. Hãy lấy 5, 2, và 3 làm giá trị của chúng ta. Chúng ta có thể thấy rằng $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Chúng ta đã thấy rằng $\mathbb{Z} \mod 7$ khi kết hợp với phép cộng và phép nhân đáp ứng các tiên đề của một trường hữu hạn khi kiểm tra với các giá trị cụ thể. Tất nhiên, chúng ta cũng có thể chứng minh điều này một cách tổng quát, nhưng sẽ không làm vậy ở đây.

Một điểm khác biệt quan trọng là giữa hai loại trường: trường hữu hạn và trường vô hạn.
Một **trường vô hạn** liên quan đến một trường mà tập hợp **S** có kích thước vô hạn. Tập hợp các số thực $\mathbb{R}$ được trang bị phép cộng và phép nhân là một ví dụ về trường vô hạn. Một **trường hữu hạn**, còn được biết đến với tên **trường Galois**, là một trường mà tập hợp **S** là hữu hạn. Ví dụ trên của chúng ta về $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ là một trường hữu hạn.

Trong mật mã học, chúng ta chủ yếu quan tâm đến trường hữu hạn. Nói chung, có thể chứng minh rằng một trường hữu hạn tồn tại cho một tập hợp các phần tử **S** nếu và chỉ nếu nó có $p^m$ phần tử, nơi $p$ là một số nguyên tố và $m$ là một số nguyên dương lớn hơn hoặc bằng một. Nói cách khác, nếu thứ tự của một tập hợp **S** là một số nguyên tố ($p^m$ nơi $m = 1$) hoặc một lũy thừa của số nguyên tố ($p^m$ nơi $m > 1$), thì bạn có thể tìm thấy hai toán tử $\circ$ và $\diamond$ sao cho các điều kiện cho một trường được thỏa mãn.

Nếu một trường hữu hạn có một số nguyên tố phần tử, thì nó được gọi là một **trường nguyên tố**. Nếu số lượng phần tử trong trường hữu hạn là một lũy thừa của số nguyên tố, thì trường đó được gọi là một **trường mở rộng**. Trong mật mã học, chúng ta quan tâm đến cả trường nguyên tố và trường mở rộng. [2]

Các trường nguyên tố chính quan tâm trong mật mã học là những trường mà tập hợp tất cả các số nguyên được điều chỉnh bởi một số nguyên tố nào đó, và các toán tử là phép cộng và phép nhân tiêu chuẩn. Lớp trường hữu hạn này bao gồm $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, và vân vân. Đối với bất kỳ trường nguyên tố $\mathbb{Z} \mod p$ nào, tập hợp các số nguyên của trường là như sau: $\{0, 1, \ldots, p – 2, p – 1\}$.

Trong mật mã học, chúng ta cũng quan tâm đến trường mở rộng, đặc biệt là bất kỳ trường nào có $2^m$ phần tử nơi $m > 1$. Các trường hữu hạn như vậy, ví dụ, được sử dụng trong Mã hóa Rijndael, làm nền tảng cho Tiêu chuẩn Mã hóa Nâng cao. Mặc dù trường nguyên tố tương đối trực quan, nhưng những trường mở rộng cơ sở 2 có lẽ không dành cho bất kỳ ai không quen với đại số trừu tượng.

Để bắt đầu, thật sự đúng là bất kỳ tập hợp số nguyên nào có $2^m$ phần tử đều có thể được gán hai toán tử làm cho sự kết hợp của chúng trở thành một trường (miễn là $m$ là một số nguyên dương). Tuy nhiên, chỉ vì một trường tồn tại không nhất thiết có nghĩa là nó dễ dàng được khám phá hoặc đặc biệt thực tiễn cho một số ứng dụng.

Hóa ra, các trường mở rộng đặc biệt áp dụng được của $2^m$ trong mật mã học là những trường được định nghĩa trên các tập hợp biểu thức đa thức cụ thể, thay vì một tập hợp số nguyên nào đó.

Ví dụ, giả sử rằng chúng ta muốn một trường mở rộng với $2^3$ (tức là, 8) phần tử trong tập hợp. Mặc dù có thể có nhiều tập hợp khác nhau có thể được sử dụng cho các trường có kích thước như vậy, một tập hợp như vậy bao gồm tất cả các đa thức duy nhất dưới dạng $a_2x^2 + a_1x + a_0$, nơi mỗi hệ số $a_i$ là 0 hoặc 1. Do đó, tập hợp **S** này bao gồm các phần tử sau:
1. $0$: Trường hợp $a_2 = 0$, $a_1 = 0$, và $a_0 = 0$.
2. $1$: Trường hợp $a_2 = 0$, $a_1 = 0$, và $a_0 = 1$.
3. $x$: Trường hợp $a_2 = 0$, $a_1 = 1$, và $a_0 = 0$.
4. $x + 1$: Trường hợp $a_2 = 0$, $a_1 = 1$, và $a_0 = 1$.
5. $x^2$: Trường hợp $a_2 = 1$, $a_1 = 0$, và $a_0 = 0$.
6. $x^2 + 1$: Trường hợp $a_2 = 1$, $a_1 = 0$, và $a_0 = 1$.
7. $x^2 + x$: Trường hợp $a_2 = 1$, $a_1 = 1$, và $a_0 = 0$.
8. $x^2 + x + 1$: Trường hợp $a_2 = 1$, $a_1 = 1$, và $a_0 = 1$.

Vậy **S** sẽ là tập hợp $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Hai phép toán nào có thể được định nghĩa trên tập hợp các phần tử này để đảm bảo sự kết hợp của chúng tạo thành một trường?

Phép toán đầu tiên trên tập hợp **S** ($\circ$) có thể được định nghĩa là phép cộng đa thức chuẩn modulo 2. Bạn chỉ cần cộng các đa thức như bạn thường làm, và sau đó áp dụng modulo 2 cho mỗi hệ số của đa thức kết quả. Dưới đây là một số ví dụ:

* $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
* $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
* $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

Phép toán thứ hai trên tập hợp **S** ($\diamond$) cần thiết để tạo ra trường là phức tạp hơn. Đó là một loại phép nhân, nhưng không phải phép nhân chuẩn từ số học. Thay vào đó, bạn phải xem mỗi phần tử như một vector và hiểu phép toán như là phép nhân của hai vector đó modulo một đa thức bất khả quy.

Hãy chuyển sang ý tưởng về một **đa thức bất khả quy**. Một đa thức bất khả quy là một đa thức không thể phân tích (giống như một số nguyên tố không thể phân tích thành các thành phần khác ngoài 1 và chính số nguyên tố đó). Đối với mục đích của chúng ta, chúng ta quan tâm đến các đa thức được coi là bất khả quy đối với tập hợp tất cả các số nguyên. (Lưu ý rằng bạn có thể có khả năng phân tích một số đa thức bằng cách sử dụng, ví dụ, các số thực hoặc phức, ngay cả khi bạn không thể phân tích chúng sử dụng các số nguyên.)
Ví dụ, xem xét đa thức $x^2 - 3x + 2$. Đa thức này có thể được viết lại như $(x – 1)(x – 2)$. Do đó, đa thức này không phải là bất khả quy. Bây giờ, xem xét đa thức $x^2 + 1$. Chỉ sử dụng số nguyên, không có cách nào để phân tích thêm biểu thức này. Do đó, đây là một đa thức bất khả quy đối với số nguyên.

Tiếp theo, hãy chuyển sang khái niệm nhân vector. Chúng ta sẽ không khám phá sâu về chủ đề này, nhưng bạn chỉ cần hiểu một quy tắc cơ bản: Bất kỳ phép chia vector nào cũng có thể diễn ra miễn là bị chia có bậc cao hơn hoặc bằng với bậc của bội số. Nếu bị chia có bậc thấp hơn bội số, thì bị chia không thể được chia cho bội số nữa.

Ví dụ, xem xét biểu thức $x^6 + x + 1 \mod x^5 + x^2$. Rõ ràng là biểu thức này giảm tiếp vì bậc của bị chia, 6, cao hơn bậc của bội số, 5. Bây giờ xem xét biểu thức $x^5 + x + 1 \mod x^5 + x^2$. Biểu thức này cũng giảm tiếp, vì bậc của bị chia, 5, và bội số, 5, là bằng nhau.

Tuy nhiên, bây giờ xem xét biểu thức $x^4 + x + 1 \mod x^5 + x^2$. Biểu thức này không giảm tiếp, vì bậc của bị chia, 4, thấp hơn bậc của bội số, 5.

Dựa trên thông tin này, chúng ta giờ đây đã sẵn sàng để tìm phép toán thứ hai cho tập hợp $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Tôi đã nói rằng phép toán thứ hai này nên được hiểu là nhân vector modulo một đa thức bất khả quy nào đó. Đa thức bất khả quy này nên đảm bảo rằng phép toán thứ hai định nghĩa một nhóm Abel trên **S** và phù hợp với điều kiện phân phối. Vậy đa thức bất khả quy đó nên là gì?

Vì tất cả các vector trong tập hợp đều có bậc 2 hoặc thấp hơn, đa thức bất khả quy nên có bậc 3. Nếu bất kỳ phép nhân nào của hai vector trong tập hợp tạo ra một đa thức có bậc 3 hoặc cao hơn, chúng ta biết rằng modulo một đa thức có bậc 3 luôn tạo ra một đa thức có bậc 2 hoặc thấp hơn. Điều này là do bất kỳ đa thức nào có bậc 3 hoặc cao hơn luôn có thể chia cho một đa thức có bậc 3. Ngoài ra, đa thức đóng vai trò là bội số phải là bất khả quy.

Hóa ra có một số đa thức bất khả quy có bậc 3 mà chúng ta có thể sử dụng làm bội số. Mỗi đa thức này định nghĩa một trường khác nhau kết hợp với tập hợp **S** của chúng ta và phép cộng modulo 2. Điều này có nghĩa là bạn có nhiều lựa chọn khi sử dụng trường mở rộng $2^m$ trong mật mã học.

Đối với ví dụ của chúng ta, giả sử rằng chúng ta chọn đa thức $x^3 + x + 1$. Đây thực sự là bất khả quy, vì bạn không thể phân tích nó sử dụng số nguyên. Ngoài ra, nó sẽ đảm bảo rằng bất kỳ phép nhân nào của hai phần tử cũng sẽ tạo ra một đa thức có bậc 2 hoặc thấp hơn.
Hãy cùng xem xét một ví dụ về phép toán thứ hai sử dụng đa thức $x^3 + x + 1$ làm bộ chia để minh họa cách thức hoạt động của nó. Giả sử bạn nhân các phần tử $x^2 + 1$ với $x^2 + x$ trong tập hợp **S** của chúng ta. Sau đó, chúng ta cần tính biểu thức $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Điều này có thể được đơn giản hóa như sau:
* $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
* $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
* $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Chúng ta biết rằng $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ có thể được giảm bớt vì bị chia có bậc cao hơn (4) so với bộ chia (3).

Để bắt đầu, bạn có thể thấy rằng biểu thức $x^3 + x + 1$ đi vào $x^4 + x^3 + x^2 + x$ tổng cộng $x$ lần. Bạn có thể xác minh điều này bằng cách nhân $x^3 + x + 1$ với $x$, là $x^4 + x^2 + x$. Vì thuật ngữ sau cùng có cùng bậc với bị chia, cụ thể là 4, chúng ta biết điều này khả thi. Bạn có thể tính phần dư của phép chia này bằng $x$ như sau:

* $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
* $[x^3] \mod x^3 + x + 1 =$
* $x^3$

Vậy sau khi chia $x^4 + x^3 + x^2 + x$ bằng $x^3 + x + 1$ tổng cộng $x$ lần, chúng ta có một phần dư là $x^3$. Liệu điều này có thể được chia thêm bởi $x^3 + x + 1$?

Một cách trực giác, có thể hấp dẫn khi nói rằng $x^3$ không thể được chia thêm bởi $x^3 + x + 1$, bởi vì thuật ngữ sau có vẻ lớn hơn. Tuy nhiên, hãy nhớ lại cuộc thảo luận của chúng ta về phép chia vector trước đó. Miễn là bị chia có bậc lớn hơn hoặc bằng bộ chia, biểu thức có thể được giảm thêm. Cụ thể, biểu thức $x^3 + x + 1$ có thể đi vào $x^3$ đúng 1 lần. Phần dư được tính như sau:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Bạn có thể tự hỏi tại sao $(x^3) - (x^3 + x + 1)$ đánh giá là $x + 1$ chứ không phải $-x - 1$. Hãy nhớ rằng phép toán đầu tiên của trường số của chúng ta được định nghĩa theo modulo 2. Do đó, việc trừ hai vector cho kết quả chính xác giống như việc cộng hai vector.
Tóm lại việc nhân $x^2 + 1$ và $x^2 + x$: Khi bạn nhân hai số hạng này, bạn sẽ nhận được một đa thức bậc 4, $x^4 + x^3 + x^2 + x$, cần được giảm modulo $x^3 + x + 1$. Đa thức bậc 4 chia hết cho $x^3 + x + 1$ đúng $x + 1$ lần. Phần dư sau khi chia $x^4 + x^3 + x^2 + x$ cho $x^3 + x + 1$ đúng $x + 1$ lần là $x + 1$. Đây quả thực là một phần tử trong tập hợp của chúng ta $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Tại sao các trường mở rộng với cơ sở 2 trên các tập hợp của đa thức, như trong ví dụ trên, lại hữu ích cho mật mã học? Lý do là bạn có thể xem các hệ số trong các đa thức của những tập hợp như vậy, hoặc là 0 hoặc là 1, như là các phần tử của chuỗi nhị phân với độ dài cụ thể. Tập hợp **S** trong ví dụ trên, ví dụ, có thể được xem thay vào đó là một tập hợp **S** bao gồm tất cả các chuỗi nhị phân có độ dài 3 (000 đến 111). Các thao tác trên **S**, sau đó, cũng có thể được sử dụng để thực hiện các thao tác trên những chuỗi nhị phân này và tạo ra một chuỗi nhị phân có cùng độ dài.

**Ghi chú:**

[2] Các trường mở rộng trở nên rất phi trực giác. Thay vì có các phần tử của số nguyên, chúng có các tập hợp của đa thức. Ngoài ra, bất kỳ thao tác nào cũng được thực hiện modulo một số đa thức bất khả quy nào đó.

## Đại số trừu tượng trong thực hành
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Mặc dù ngôn ngữ chính thức và tính trừu tượng của cuộc thảo luận, khái niệm về nhóm không nên quá khó để nắm bắt. Đó chỉ là một tập hợp các phần tử cùng với một phép toán nhị phân, nơi thực hiện phép toán nhị phân đó trên những phần tử đó đáp ứng bốn điều kiện chung. Một nhóm Abel còn có một điều kiện bổ sung được biết đến là tính giao hoán. Một nhóm tuần hoàn, lần lượt, là một loại nhóm Abel đặc biệt, tức là một nhóm có một sinh viên. Một trường chỉ đơn giản là một cấu trúc phức tạp hơn từ khái niệm nhóm cơ bản.

Nhưng nếu bạn là một người thực tế, bạn có thể tự hỏi vào lúc này: Ai quan tâm? Biết một số tập hợp các phần tử với một toán tử là một nhóm, hoặc thậm chí là một nhóm Abel hay nhóm tuần hoàn, có ý nghĩa gì trong thế giới thực không? Biết một cái gì đó là một trường?

Không đi sâu vào quá nhiều chi tiết, câu trả lời là “có”. Nhóm được tạo ra lần đầu tiên vào thế kỷ 19 bởi nhà toán học người Pháp Evariste Galois. Ông đã sử dụng chúng để rút ra kết luận về việc giải các phương trình đa thức có bậc cao hơn năm.

Kể từ đó, khái niệm về nhóm đã giúp làm sáng tỏ một số vấn đề trong toán học và lĩnh vực khác. Dựa trên cơ sở đó, ví dụ, nhà vật lý Murray-Gellman đã có thể dự đoán sự tồn tại của một hạt trước khi nó thực sự được quan sát trong thí nghiệm. [3] Ví dụ khác, các nhà hóa học sử dụng lý thuyết nhóm để phân loại hình dạng của các phân tử. Các nhà toán học thậm chí đã sử dụng khái niệm về nhóm để rút ra kết luận về một cái gì đó cụ thể như giấy dán tường!
Cơ bản, việc chứng minh một tập hợp các phần tử với một phép toán nào đó tạo thành một nhóm, có nghĩa là bạn đang mô tả một dạng đối xứng đặc biệt. Không phải đối xứng theo nghĩa thông thường của từ này, mà ở một hình thức trừu tượng hơn. Và điều này có thể cung cấp cái nhìn sâu sắc đáng kể vào các hệ thống và vấn đề cụ thể. Những khái niệm phức tạp hơn từ đại số trừu tượng chỉ cho chúng ta thêm thông tin.

Quan trọng nhất, bạn sẽ thấy tầm quan trọng của các nhóm và trường lý thuyết số trong thực hành thông qua ứng dụng của chúng trong mật mã học, đặc biệt là mật mã học khóa công khai. Chúng ta đã thấy trong cuộc thảo luận về trường, ví dụ, cách các trường mở rộng được sử dụng trong Mã hóa Rijndael. Chúng ta sẽ giải quyết ví dụ đó trong *Chương 5*.

Để thảo luận thêm về đại số trừu tượng, tôi khuyên bạn nên xem loạt video xuất sắc về đại số trừu tượng của Socratica. [4] Tôi đặc biệt khuyên bạn nên xem các video sau: “What is abstract algebra?”, “Group definition (expanded)”, “Ring definition (expanded)”, và “Field definition (expanded).” Bốn video này sẽ cho bạn thêm cái nhìn sâu sắc vào phần lớn cuộc thảo luận ở trên. (Chúng tôi không thảo luận về các vòng, nhưng một trường chỉ là một loại vòng đặc biệt.)

Để thảo luận thêm về lý thuyết số hiện đại, bạn có thể tham khảo nhiều cuộc thảo luận nâng cao về mật mã học. Tôi sẽ gợi ý Jonathan Katz và Yehuda Lindell’s Introduction to Modern Cryptography hoặc Christof Paar và Jan Pelzl’s Understanding Cryptography để thảo luận thêm. [5]

**Ghi chú:**

[3] Xem [Video YouTube](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Abstract Algebra](https://www.socratica.com/subject/abstract-algebra)

[5] Katz và Lindell, *Introduction to Modern Cryptography*, ấn bản thứ 2, 2015 (CRC Press: Boca Raton, FL). Paar và Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlin).

# Mật mã học đối xứng
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice và Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Một trong hai nhánh chính của mật mã học là mật mã học đối xứng. Nó bao gồm các phương pháp mã hóa cũng như các phương pháp liên quan đến xác thực và tính toàn vẹn. Cho đến những năm 1970, toàn bộ mật mã học sẽ bao gồm các phương pháp mã hóa đối xứng.

Cuộc thảo luận chính bắt đầu bằng cách xem xét các phương pháp mã hóa đối xứng và làm rõ sự khác biệt quan trọng giữa mã hóa luồng và mã hóa khối. Sau đó, chúng ta chuyển sang các mã xác thực tin nhắn, là các phương pháp để đảm bảo tính toàn vẹn và xác thực của tin nhắn. Cuối cùng, chúng ta khám phá cách kết hợp các phương pháp mã hóa đối xứng và mã xác thực tin nhắn để đảm bảo giao tiếp an toàn.

Chương này thảo luận qua loa về các phương pháp mật mã học đối xứng từ thực tiễn. Chương tiếp theo sẽ trình bày chi tiết về mã hóa với một mã hóa luồng và một mã hóa khối từ thực tiễn, cụ thể là RC4 và AES.

Trước khi bắt đầu cuộc thảo luận về mật mã học đối xứng, tôi muốn nhanh chóng nhắc lại một số ý kiến về hình ảnh minh họa Alice và Bob trong chương này và các chương tiếp theo.

___

Trong việc minh họa các nguyên tắc của mật mã học, người ta thường dựa vào các ví dụ liên quan đến Alice và Bob. Tôi cũng sẽ làm như vậy.

Đặc biệt nếu bạn mới làm quen với mật mã học, điều quan trọng cần nhận ra là những ví dụ về Alice và Bob chỉ nhằm mục đích minh họa các nguyên tắc và cấu trúc mật mã học trong một môi trường đơn giản. Tuy nhiên, các nguyên tắc và cấu trúc này có thể áp dụng cho một phạm vi rộng lớn các bối cảnh thực tế.
Dưới đây là năm điểm chính cần nhớ về các ví dụ liên quan đến Alice và Bob trong mật mã học:
1. Chúng có thể dễ dàng được chuyển đổi thành các ví dụ với các loại diễn viên khác như các công ty hoặc tổ chức chính phủ.
2. Chúng có thể dễ dàng được mở rộng để bao gồm ba hoặc nhiều diễn viên hơn.
3. Trong các ví dụ, Bob và Alice thường là những người tham gia tích cực trong việc tạo ra từng tin nhắn và trong việc áp dụng các kế hoạch mật mã học lên tin nhắn đó. Nhưng trên thực tế, giao tiếp điện tử phần lớn là tự động. Khi bạn truy cập một trang web sử dụng bảo mật lớp vận chuyển, ví dụ, mật mã học thường được xử lý hoàn toàn bởi máy tính của bạn và máy chủ web.
4. Trong bối cảnh giao tiếp điện tử, "tin nhắn" được gửi qua kênh giao tiếp thường là các gói TCP/IP. Chúng có thể thuộc về một email, một tin nhắn Facebook, một cuộc trò chuyện qua điện thoại, một lần chuyển file, một trang web, một bản tải lên phần mềm, và vân vân. Chúng không phải là tin nhắn theo nghĩa truyền thống. Tuy nhiên, các nhà mật mã học thường đơn giản hóa thực tế này bằng cách nói rằng tin nhắn, ví dụ, là một email.
5. Các ví dụ thường tập trung vào giao tiếp điện tử, nhưng chúng cũng có thể được mở rộng ra các hình thức giao tiếp truyền thống như thư từ.

## Các kế hoạch mã hóa đối xứng
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Chúng ta có thể định nghĩa một cách lỏng lẻo **kế hoạch mã hóa đối xứng** là bất kỳ kế hoạch mật mã học nào với ba thuật toán:

1. Một **thuật toán tạo khóa**, tạo ra một khóa riêng tư.
2. Một **thuật toán mã hóa**, lấy khóa riêng tư và một bản rõ làm đầu vào và xuất ra một bản mã.
3. Một **thuật toán giải mã**, lấy khóa riêng tư và bản mã làm đầu vào và xuất ra bản rõ gốc.

Thông thường, một kế hoạch mã hóa—dù là đối xứng hay bất đối xứng—cung cấp một mẫu cho việc mã hóa dựa trên một thuật toán cốt lõi, thay vì một thông số kỹ thuật chính xác.

Ví dụ, xem xét Salsa20, một kế hoạch mã hóa đối xứng. Nó có thể được sử dụng với cả độ dài khóa 128 và 256 bit. Sự lựa chọn về độ dài khóa ảnh hưởng đến một số chi tiết nhỏ của thuật toán (số vòng trong thuật toán để chính xác).

Nhưng người ta sẽ không nói rằng sử dụng Salsa20 với khóa 128 bit là một kế hoạch mã hóa khác so với Salsa20 với khóa 256 bit. Thuật toán cốt lõi vẫn giữ nguyên. Chỉ khi thuật toán cốt lõi thay đổi thì chúng ta mới thực sự nói về hai kế hoạch mã hóa khác nhau.

Các kế hoạch mã hóa đối xứng thường hữu ích trong hai loại trường hợp: (1) Những trường hợp mà hai hoặc nhiều đại lý giao tiếp từ xa và muốn giữ bí mật nội dung giao tiếp của họ; và (2) những trường hợp mà một đại lý muốn giữ bí mật nội dung của một tin nhắn theo thời gian.

Bạn có thể thấy một hình ảnh về tình huống (1) trong *Hình 1* dưới đây. Bob muốn gửi một tin nhắn $M$ cho Alice từ xa, nhưng không muốn người khác có thể đọc tin nhắn đó.

Bob trước tiên mã hóa tin nhắn $M$ với khóa riêng tư $K$. Sau đó, anh ấy gửi bản mã $C$ cho Alice. Một khi Alice nhận được bản mã, cô ấy có thể giải mã nó sử dụng khóa $K$ và đọc bản rõ. Với một kế hoạch mã hóa tốt, bất kỳ kẻ tấn công nào chặn được bản mã $C$ cũng không nên có thể học được bất cứ điều gì có ý nghĩa thực sự về tin nhắn $M$.

Bạn có thể thấy một hình ảnh về tình huống (2) trong *Hình 2* dưới đây. Bob muốn ngăn chặn người khác xem thông tin nhất định. Một tình huống điển hình có thể là Bob là một nhân viên lưu trữ dữ liệu nhạy cảm trên máy tính của mình, mà cả người ngoài lẫn đồng nghiệp không được phép đọc.
Bob mã hóa thông điệp $M$ vào thời điểm $T_0$ bằng khóa $K$ để tạo ra bản mã $C$. Vào thời điểm $T_1$, anh ta cần thông điệp đó một lần nữa và giải mã bản mã $C$ bằng khóa $K$. Bất kỳ kẻ tấn công nào có thể đã tình cờ gặp phải bản mã $C$ trong thời gian đó không nên có khả năng suy luận ra bất cứ điều gì đáng kể về $M$ từ nó.

*Hình 1: Bí mật qua không gian*

![Hình 1: Bí mật qua không gian](assets/Figure4-1.webp "Hình 1: Bí mật qua không gian")

*Hình 2: Bí mật qua thời gian*

![Hình 2: Bí mật qua thời gian](assets/Figure4-2.webp "Hình 2: Bí mật qua thời gian")

## Ví dụ: Mã Caesar
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Trong Chương 2, chúng ta đã gặp mã Caesar, đây là ví dụ về một lược đồ mã hóa đối xứng rất đơn giản. Hãy xem xét nó một lần nữa ở đây.

Giả sử một từ điển *D* tương đương tất cả các chữ cái của bảng chữ cái tiếng Anh, theo thứ tự, với tập hợp các số $\{0,1,2,\dots,25\}$. Giả định một tập hợp các thông điệp có thể có **M**. Mã Caesar, vậy, là một lược đồ mã hóa được định nghĩa như sau:

- Chọn ngẫu nhiên một khóa $k$ từ tập hợp các khóa có thể có **K**, nơi **K** = $\{0,1,2,\dots,25\}$
- Mã hóa một thông điệp $m \in$ **M**, như sau:
    - Tách $m$ thành các chữ cái riêng lẻ $m_0, m_1,\dots, m_i, \dots, m_l$
    - Chuyển đổi mỗi $m_i$ thành một số theo *D*
    - Đối với mỗi $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Chuyển đổi mỗi $c_i$ thành một chữ cái theo *D*
    - Sau đó kết hợp $c_0, c_1,\dots, c_l$ để tạo ra bản mã $c$
- Giải mã một bản mã $c$ như sau:
    - Chuyển đổi mỗi $c_i$ thành một số theo *D*
    - Đối với mỗi $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Chuyển đổi mỗi $m_i$ thành một chữ cái theo *D*
    - Sau đó kết hợp $m_0, m_1,\dots, m_l$ để tạo ra thông điệp gốc $m$

Điều làm cho mã Caesar trở thành một lược đồ mã hóa đối xứng là cùng một khóa được sử dụng cho cả quá trình mã hóa và giải mã. Ví dụ, giả sử bạn muốn mã hóa thông điệp “DOG” sử dụng mã Caesar, và bạn đã chọn ngẫu nhiên "24" làm khóa. Mã hóa thông điệp với khóa này sẽ tạo ra “BME”. Cách duy nhất để lấy lại thông điệp gốc là sử dụng cùng một khóa, "24", cho quá trình giải mã.

Mã Caesar là ví dụ về **mã thay thế monoalphabetic**: một lược đồ mã hóa nơi bảng chữ cái của bản mã được cố định (tức là, chỉ sử dụng một bảng chữ cái). Giả sử rằng thuật toán giải mã là xác định, mỗi ký tự trong bản mã thay thế tối đa chỉ có thể tương ứng với một ký tự trong bản rõ.
Cho đến thế kỷ 18, nhiều ứng dụng của mã hóa dựa nhiều vào các hệ mã đơn bảng chữ cái, mặc dù thường chúng phức tạp hơn nhiều so với Mã dịch chuyển. Ví dụ, bạn có thể ngẫu nhiên chọn một chữ cái từ bảng chữ cái cho mỗi chữ cái văn bản gốc dưới ràng buộc rằng mỗi chữ cái chỉ xuất hiện một lần trong bảng chữ cái mã hóa. Điều này có nghĩa là bạn sẽ có 26 giai thừa khả năng khóa riêng tư, con số này rất lớn trong thời đại trước máy tính.

Lưu ý rằng bạn sẽ gặp thuật ngữ **mã hóa** rất nhiều trong mật mã học. Hãy nhận thức rằng thuật ngữ này có nhiều ý nghĩa khác nhau. Thực tế, tôi biết ít nhất năm ý nghĩa riêng biệt của thuật ngữ này trong mật mã học.

Trong một số trường hợp, nó đề cập đến một kế hoạch mã hóa, như trong Mã dịch chuyển và mã đơn bảng chữ cái. Tuy nhiên, thuật ngữ này cũng có thể đề cập cụ thể đến thuật toán mã hóa, khóa riêng tư, hoặc chỉ là văn bản mã hóa của bất kỳ kế hoạch mã hóa nào.

Cuối cùng, thuật ngữ mã hóa cũng có thể đề cập đến một thuật toán cốt lõi từ đó bạn có thể xây dựng các kế hoạch mật mã. Những cái này có thể bao gồm các thuật toán mã hóa khác nhau, nhưng cũng bao gồm các loại kế hoạch mật mã khác. Ý nghĩa của thuật ngữ này trở nên liên quan trong bối cảnh của mã khối (xem phần “Mã Khối” bên dưới).

Bạn cũng có thể gặp các thuật ngữ **mã hóa** hoặc **giải mã**. Những thuật ngữ này chỉ đơn giản là đồng nghĩa cho việc mã hóa và giải mã.

## Các cuộc tấn công bằng lực lượng cưỡng bức và nguyên tắc Kerckhoff
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Mã dịch chuyển là một kế hoạch mã hóa đối xứng rất không an toàn, ít nhất là trong thế giới hiện đại. [1] Một kẻ tấn công chỉ cần thử giải mã bất kỳ văn bản mã hóa nào với tất cả 26 khóa có thể để xem kết quả nào có ý nghĩa. Loại tấn công này, nơi kẻ tấn công chỉ đơn giản là lặp qua các khóa để xem cái nào hoạt động, được biết đến là **tấn công bằng lực lượng cưỡng bức** hoặc **tìm kiếm khóa kiệt sức**.

Đối với bất kỳ kế hoạch mã hóa nào để đáp ứng một khái niệm tối thiểu về an ninh, nó phải có một tập hợp các khóa có thể, hoặc **không gian khóa**, lớn đến mức các cuộc tấn công bằng lực lượng cưỡng bức trở nên không khả thi. Tất cả các kế hoạch mã hóa hiện đại đều đáp ứng tiêu chuẩn này. Điều này được biết đến là **nguyên tắc không gian khóa đủ**. Một nguyên tắc tương tự thường được áp dụng trong các loại kế hoạch mật mã khác nhau.

Để cảm nhận được kích thước không gian khóa khổng lồ trong các kế hoạch mã hóa hiện đại, giả sử rằng một tệp đã được mã hóa với một khóa 128-bit sử dụng tiêu chuẩn mã hóa nâng cao. Điều này có nghĩa là kẻ tấn công có một tập hợp $2^{128}$ khóa mà cô ấy cần phải lặp qua để thực hiện một cuộc tấn công bằng lực lượng cưỡng bức. Một cơ hội thành công 0.78% với chiến lược này sẽ yêu cầu kẻ tấn công phải lặp qua khoảng $2.65 \times 10^{36}$ khóa.

Giả sử chúng ta lạc quan giả định rằng một kẻ tấn công có thể thử $10^{16}$ khóa mỗi giây (tức là, 10 nghìn tỷ khóa mỗi giây). Để kiểm tra 0.78% tất cả các khóa trong không gian khóa, cuộc tấn công của cô ấy sẽ phải kéo dài $2.65 \times 10^{20}$ giây. Đây là khoảng 8.4 nghìn tỷ năm. Vì vậy, ngay cả một cuộc tấn công bằng lực lượng cưỡng bức bởi một đối thủ cực kỳ mạnh mẽ cũng không thực tế với một kế hoạch mã hóa 128-bit hiện đại. Đây là nguyên tắc không gian khóa đủ được áp dụng.

Liệu mã dịch chuyển có an toàn hơn nếu kẻ tấn công không biết thuật toán mã hóa? Có thể, nhưng không nhiều.
Trong mọi trường hợp, mật mã hiện đại luôn giả định rằng sự an toàn của bất kỳ hệ thống mã hóa đối xứng nào chỉ dựa vào việc giữ bí mật khóa riêng tư. Người tấn công luôn được giả định biết tất cả các chi tiết khác, bao gồm không gian tin nhắn, không gian khóa, không gian văn bản mã hóa, thuật toán chọn khóa, thuật toán mã hóa và thuật toán giải mã.
Ý tưởng rằng sự an toàn của một hệ thống mã hóa đối xứng chỉ có thể dựa vào sự bí mật của khóa riêng tư được biết đến như là **Nguyên tắc Kerckhoffs**.

Như Kerckhoffs đã ban đầu dự định, nguyên tắc này chỉ áp dụng cho các hệ thống mã hóa đối xứng. Tuy nhiên, một phiên bản tổng quát hơn của nguyên tắc này cũng áp dụng cho tất cả các loại hệ thống mật mã hiện đại khác: Thiết kế của bất kỳ hệ thống mật mã nào không được yêu cầu phải giữ bí mật để đảm bảo an toàn; sự bí mật chỉ có thể mở rộng đến một số chuỗi thông tin, thường là một khóa riêng tư.

Nguyên tắc Kerckhoffs là trung tâm của mật mã hiện đại vì bốn lý do. [2] Đầu tiên, chỉ có một số lượng hạn chế các hệ thống mật mã cho các loại ứng dụng cụ thể. Ví dụ, hầu hết các ứng dụng mã hóa đối xứng hiện đại sử dụng mật mã Rijndael. Vì vậy, sự bí mật về thiết kế của một hệ thống chỉ rất hạn chế. Tuy nhiên, có nhiều linh hoạt hơn trong việc giữ bí mật một số khóa riêng tư cho mật mã Rijndael.

Thứ hai, việc thay thế một chuỗi thông tin dễ dàng hơn là thay thế toàn bộ hệ thống mật mã. Giả sử rằng tất cả nhân viên của một công ty đều sử dụng cùng một phần mềm mã hóa, và mỗi hai nhân viên có một khóa riêng tư để giao tiếp mật. Việc khóa bị lộ là một rắc rối trong tình huống này, nhưng ít nhất công ty có thể giữ phần mềm với những lỗ hổng bảo mật như vậy. Nếu công ty dựa vào sự bí mật của hệ thống, thì bất kỳ sự lộ bí mật nào cũng đòi hỏi phải thay thế toàn bộ phần mềm.

Thứ ba, nguyên tắc Kerckhoffs cho phép tiêu chuẩn hóa và tương thích giữa người dùng của các hệ thống mật mã. Điều này mang lại lợi ích lớn về hiệu quả. Ví dụ, rất khó để tưởng tượng hàng triệu người có thể kết nối an toàn với máy chủ web của Google mỗi ngày, nếu sự an toàn đó đòi hỏi phải giữ bí mật các hệ thống mật mã.

Thứ tư, nguyên tắc Kerckhoff cho phép sự giám sát công khai của các hệ thống mật mã. Loại giám sát này là hoàn toàn cần thiết để đạt được các hệ thống mật mã an toàn. Một cách minh họa, thuật toán chính trong mật mã đối xứng, mật mã Rijndael, là kết quả của một cuộc thi do Viện Tiêu chuẩn và Công nghệ Quốc gia tổ chức từ năm 1997 đến 2000.

Bất kỳ hệ thống nào cố gắng đạt được **an toàn bằng cách che giấu** là một hệ thống dựa vào việc giữ bí mật các chi tiết thiết kế và/hoặc triển khai. Trong mật mã, đây cụ thể là một hệ thống dựa vào việc giữ bí mật các chi tiết thiết kế của hệ thống mật mã. Vì vậy, an toàn bằng cách che giấu trái ngược trực tiếp với nguyên tắc Kerckhoffs.

Khả năng của sự mở cửa để tăng cường chất lượng và an toàn cũng mở rộng rộng lớn hơn đến thế giới số hóa chứ không chỉ là mật mã. Các bản phân phối Linux mã nguồn mở và miễn phí như Debian, ví dụ, thường có nhiều ưu điểm hơn so với các đối thủ Windows và MacOS về quyền riêng tư, ổn định, an toàn và linh hoạt. Mặc dù có thể có nhiều nguyên nhân, nhưng nguyên tắc quan trọng nhất có lẽ, như Eric Raymond đã diễn đạt trong bài luận nổi tiếng của mình "The Cathedral and the Bazaar," rằng "với đủ nhiều con mắt, mọi lỗi đều nông cạn.” [3] Đó là nguyên tắc loại trí tuệ của đám đông đã mang lại thành công lớn nhất cho Linux.
Không thể khẳng định một cách không mơ hồ rằng một phương pháp mã hóa là "an toàn" hay "không an toàn." Thay vào đó, có nhiều khái niệm về sự an toàn cho các phương pháp mã hóa. Mỗi **định nghĩa về sự an toàn mã hóa** phải chỉ rõ (1) mục tiêu an toàn, cũng như (2) khả năng của kẻ tấn công. Phân tích các phương pháp mã hóa dựa trên một hoặc nhiều khái niệm cụ thể về sự an toàn cung cấp cái nhìn sâu sắc vào ứng dụng và giới hạn của chúng.

Mặc dù chúng ta sẽ không đi sâu vào tất cả chi tiết của các khái niệm về sự an toàn mã hóa, bạn nên biết rằng hai giả định là phổ biến đối với tất cả các khái niệm mã hóa hiện đại về sự an toàn liên quan đến các phương pháp đối xứng và bất đối xứng (và trong một số hình thức đối với các nguyên tắc mã hóa khác):

* Kiến thức của kẻ tấn công về phương pháp tuân theo nguyên tắc Kerckhoffs.
* Kẻ tấn công không thể thực hiện một cuộc tấn công bằng cách sử dụng lực lượng mù một cách khả thi. Cụ thể, các mô hình đe dọa của các khái niệm về sự an toàn mã hóa thường không cho phép các cuộc tấn công bằng lực lượng mù, vì chúng giả định rằng những điều này không phải là một yếu tố cần xem xét.

**Ghi chú:**

[1] Theo Seutonius, một loại mã dịch với giá trị khóa cố định là 3 đã được Julius Caesar sử dụng trong giao tiếp quân sự của mình. Vì vậy, A luôn trở thành D, B luôn là E, C luôn là F, và cứ thế. Phiên bản cụ thể của mã dịch này, do đó, đã trở nên nổi tiếng với tên gọi **Mã Caesar** (mặc dù nó không thực sự là một mã trong nghĩa hiện đại của từ này, vì giá trị khóa là cố định). Mã Caesar có thể đã an toàn vào thế kỷ thứ nhất trước Công nguyên, nếu kẻ thù của Rome rất không quen thuộc với việc mã hóa. Nhưng rõ ràng nó sẽ không phải là một phương pháp rất an toàn trong thời đại hiện đại.

[2] Jonathan Katz và Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), tr. 7f.

[3] Eric Raymond, “The Cathedral and the Bazaar,” bài báo được trình bày tại Linux Kongress, Würzburg, Đức (27 tháng 5 năm 1997). Có một số phiên bản tiếp theo cũng như một cuốn sách. Trích dẫn của tôi đến từ trang 30 trong cuốn sách: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, bản sửa đổi (2001), O’Reilly: Sebastopol, CA.

## Mã hóa luồng
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Các phương pháp mã hóa đối xứng thường được chia thành hai loại: **mã hóa luồng** và **mã hóa khối**. Sự phân biệt này có phần rắc rối, tuy nhiên, vì mọi người sử dụng các thuật ngữ này một cách không nhất quán. Trong vài phần tiếp theo, tôi sẽ trình bày sự phân biệt theo cách tôi cho là tốt nhất. Tuy nhiên, bạn nên biết rằng nhiều người sẽ sử dụng các thuật ngữ này một cách khác biệt so với cách tôi trình bày.

Hãy đầu tiên xem xét mã hóa luồng. Một **mã hóa luồng** là một phương pháp mã hóa đối xứng nơi mã hóa bao gồm hai bước.

Đầu tiên, một chuỗi có độ dài bằng với văn bản gốc được tạo ra thông qua một khóa riêng. Chuỗi này được gọi là **keystream**.

Tiếp theo, keystream được kết hợp toán học với văn bản gốc để tạo ra văn bản mã hóa. Sự kết hợp này thường là một phép toán XOR. Để giải mã, bạn chỉ cần đảo ngược thao tác. (Lưu ý rằng $A \oplus B = B \oplus A$, trong trường hợp $A$ và $B$ là chuỗi bit. Vì vậy, thứ tự của một phép toán XOR trong mã hóa luồng không ảnh hưởng đến kết quả. Tính chất này được biết đến là **tính giao hoán**.)
Một ví dụ điển hình về mật mã luồng XOR được mô tả trong *Hình 3*. Đầu tiên, bạn lấy một khóa riêng tư $K$ và sử dụng nó để tạo ra một luồng khóa. Sau đó, luồng khóa này được kết hợp với bản rõ thông qua một phép toán XOR để tạo ra bản mã. Bất kỳ đại lý nào nhận được bản mã đều có thể dễ dàng giải mã nếu họ có khóa $K$. Tất cả những gì cô ấy cần làm là tạo ra một luồng khóa dài bằng bản mã theo quy trình được chỉ định của lược đồ và XOR nó với bản mã.

*Hình 3: Một mật mã luồng XOR*

![Hình 3: Một mật mã luồng XOR](assets/Figure4-3.webp "Hình 3: Một mật mã luồng XOR")

Hãy nhớ rằng, một lược đồ mã hóa thường là một mẫu cho việc mã hóa với cùng một thuật toán cốt lõi, chứ không phải là một thông số kỹ thuật chính xác. Theo cách mở rộng, một mật mã luồng thường là một mẫu cho việc mã hóa trong đó bạn có thể sử dụng các khóa có độ dài khác nhau. Mặc dù độ dài khóa có thể ảnh hưởng đến một số chi tiết nhỏ của lược đồ, nhưng nó sẽ không ảnh hưởng đến hình thức cơ bản của nó.

Mật mã dịch là một ví dụ về một mật mã luồng đơn giản và không an toàn. Sử dụng một chữ cái đơn lẻ (khóa riêng tư), bạn có thể tạo ra một chuỗi các chữ cái có độ dài bằng với thông điệp (luồng khóa). Sau đó, luồng khóa này được kết hợp với bản rõ thông qua một phép toán modulo để tạo ra bản mã. (Phép toán modulo này có thể được đơn giản hóa thành một phép toán XOR khi biểu diễn các chữ cái dưới dạng bit).

Một ví dụ nổi tiếng khác về mật mã luồng là **mật mã Vigenere**, theo tên của Blaise de Vigenere, người đã phát triển hoàn chỉnh nó vào cuối thế kỷ 16 (mặc dù đã có nhiều công trình tiền nghiệm). Đây là một ví dụ về **mật mã thay thế đa bảng chữ cái**: một lược đồ mã hóa nơi bảng chữ cái bản mã cho một ký tự bản rõ thay đổi tùy thuộc vào vị trí của nó trong văn bản. Trái ngược với mật mã thay thế đơn bảng chữ cái, các ký tự bản mã có thể được liên kết với nhiều hơn một ký tự bản rõ.

Khi mã hóa trở nên phổ biến ở châu Âu thời Phục Hưng, **phân tích mật mã**—tức là, việc phá vỡ bản mã—cũng trở nên phổ biến, đặc biệt là sử dụng **phân tích tần suất**. Phương pháp này sử dụng các quy luật thống kê trong ngôn ngữ của chúng ta để phá vỡ bản mã, và đã được các học giả Ả Rập phát hiện ra từ thế kỷ thứ chín. Đây là một kỹ thuật hoạt động đặc biệt tốt với các văn bản dài. Và ngay cả những mật mã thay thế đơn bảng chữ cái tinh vi nhất cũng không còn đủ để chống lại phân tích tần suất vào thế kỷ 18 ở châu Âu, đặc biệt là trong các cài đặt quân sự và an ninh. Khi mật mã Vigenere mang lại một bước tiến lớn về mặt an ninh, nó trở nên phổ biến trong thời kỳ này và được phổ biến rộng rãi vào cuối thế kỷ 18.

Nói một cách không chính thức, lược đồ mã hóa hoạt động như sau:

1. Chọn một từ có nhiều chữ cái làm khóa riêng tư.
2. Đối với bất kỳ thông điệp nào, áp dụng mật mã dịch cho mỗi chữ cái của thông điệp sử dụng chữ cái tương ứng trong từ khóa làm dịch.
3. Nếu bạn đã lặp qua từ khóa nhưng vẫn chưa mã hóa hoàn toàn bản rõ, lại áp dụng các chữ cái của từ khóa như một mật mã dịch cho các chữ cái tương ứng trong phần còn lại của văn bản.
4. Tiếp tục quá trình này cho đến khi toàn bộ thông điệp được mã hóa.

Để minh họa, giả sử khóa riêng tư của bạn là "GOLD" và bạn muốn mã hóa thông điệp "CRYPTOGRAPHY". Trong trường hợp đó, bạn sẽ tiến hành như sau theo mật mã Vigenère:

- $c_0  = [(2 + 6) \mod 26] = 8 = I$
- $c_1  = [(17 + 14) \mod 26] = 5 = F$
- $c_2  = [(24 + 11) \mod 26] = 9 = J$
- $c_3  = [(15 + 3) \mod 26] = 18 = S$
- $c_4  = [(19 + 6) \mod 26] = 25 = Z$
- $c_5  = [(14 + 14) \mod 26] = 2 = C$
- $c_6  = [(6 + 11) \mod 26] = 17 = R$
- $c_7  = [(17 + 3) \mod 26] = 20 = U$
- $c_8  = [(0 + 6) \mod 26] = 6 = G$
- $c_9  = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Như vậy, bản mã $c$ = "IFJSZCRUGDSB".

Một ví dụ nổi tiếng khác về mật mã luồng là **mật mã một lần** (one-time pad). Với mật mã một lần, bạn chỉ cần tạo một chuỗi bit ngẫu nhiên có độ dài bằng với thông điệp gốc và tạo ra bản mã thông qua phép toán XOR. Do đó, khóa riêng và chuỗi khóa trong mật mã một lần là tương đương.

Trong khi mật mã dịch và mật mã Vigenere rất không an toàn trong thời đại hiện đại, mật mã một lần lại rất an toàn nếu được sử dụng đúng cách. Có lẽ ứng dụng nổi tiếng nhất của mật mã một lần, ít nhất là cho đến những năm 1980, là cho **đường dây nóng Washington-Moscow**.

Đường dây nóng là một liên kết truyền thông trực tiếp giữa Washington và Moscow cho các vấn đề khẩn cấp, được lắp đặt sau cuộc khủng hoảng tên lửa Cuba. Công nghệ cho đường dây nóng đã thay đổi qua nhiều năm. Hiện nay, nó bao gồm một cáp quang trực tiếp cũng như hai liên kết vệ tinh (để dự phòng), cho phép gửi email và tin nhắn văn bản. Liên kết kết thúc ở nhiều nơi tại Mỹ. Lầu Năm Góc, Nhà Trắng và Núi Raven Rock là các điểm kết thúc được biết đến. Trái với ý kiến phổ biến, đường dây nóng chưa bao giờ sử dụng điện thoại.

Bản chất của mật mã một lần hoạt động như sau. Cả Washington và Moscow sẽ có hai bộ số ngẫu nhiên. Một bộ số ngẫu nhiên, do người Nga tạo ra, liên quan đến việc mã hóa và giải mã bất kỳ thông điệp nào bằng tiếng Nga. Một bộ số ngẫu nhiên, do người Mỹ tạo ra, liên quan đến việc mã hóa và giải mã bất kỳ thông điệp nào bằng tiếng Anh. Thỉnh thoảng, thêm số ngẫu nhiên sẽ được giao cho phía bên kia bởi các sứ giả đáng tin cậy.

Washington và Moscow, sau đó, có thể giao tiếp một cách bí mật bằng cách sử dụng những số ngẫu nhiên này để tạo ra mật mã một lần. Mỗi khi bạn cần giao tiếp, bạn sẽ sử dụng phần tiếp theo của số ngẫu nhiên cho thông điệp của mình.

Mặc dù rất an toàn, mật mã một lần đối mặt với những hạn chế thực tế đáng kể: khóa cần phải dài bằng thông điệp và không một phần nào của mật mã một lần có thể được tái sử dụng. Điều này có nghĩa là bạn cần phải theo dõi vị trí của mình trong mật mã một lần, lưu trữ một lượng lớn bit và trao đổi bit ngẫu nhiên với các đối tác từ thời gian này sang thời gian khác. Do đó, mật mã một lần không thường xuyên được sử dụng trong thực tế.

Thay vào đó, các mật mã luồng giả ngẫu nhiên thường được sử dụng trong thực tế. Salsa20 và một biến thể gần gũi được gọi là ChaCha là những ví dụ về các mật mã luồng giả ngẫu nhiên thường được sử dụng.
Với những thuật toán mã hóa luồng giả ngẫu nhiên này, bạn trước tiên cần chọn ngẫu nhiên một khóa K ngắn hơn độ dài của văn bản gốc. Khóa ngẫu nhiên K này thường được máy tính của chúng ta tạo ra dựa trên dữ liệu không dự đoán trước được mà nó thu thập theo thời gian, như thời gian giữa các tin nhắn mạng, chuyển động của chuột, v.v. Khóa ngẫu nhiên $K$ sau đó được đưa vào một thuật toán mở rộng, tạo ra một dòng khóa giả ngẫu nhiên dài bằng thông điệp. Bạn có thể chỉ định chính xác độ dài của dòng khóa cần thiết (ví dụ, 500 bit, 1000 bit, 1200 bit, 29,117 bit, v.v.).

Một dòng khóa giả ngẫu nhiên xuất hiện *như thể* nó được chọn hoàn toàn ngẫu nhiên từ tập hợp tất cả các chuỗi có cùng độ dài. Do đó, việc mã hóa với một dòng khóa giả ngẫu nhiên xuất hiện như thể nó đã được thực hiện với một bảng mã một lần. Nhưng đó, tất nhiên, không phải là trường hợp.

Vì khóa riêng của chúng ta ngắn hơn dòng khóa và thuật toán mở rộng của chúng ta cần phải là xác định để quá trình mã hóa/giải mã hoạt động, không phải mọi dòng khóa có độ dài cụ thể đó có thể là kết quả đầu ra từ hoạt động mở rộng của chúng ta.

Giả sử, ví dụ, khóa riêng của chúng ta có độ dài 128 bit và chúng ta có thể chèn nó vào một thuật toán mở rộng để tạo ra một dòng khóa dài hơn nhiều, giả sử là 2,500 bit. Vì thuật toán mở rộng của chúng ta cần phải là xác định, thuật toán của chúng ta tối đa chỉ có thể chọn $1/2^{128}$ chuỗi với độ dài 2,500 bit. Vì vậy, một dòng khóa như vậy không bao giờ có thể được chọn hoàn toàn ngẫu nhiên từ tất cả các chuỗi cùng độ dài.

Định nghĩa của chúng ta về một thuật toán mã hóa luồng có hai khía cạnh: (1) một dòng khóa dài bằng văn bản gốc được tạo ra với sự giúp đỡ của một khóa riêng; và (2) dòng khóa này được kết hợp với văn bản gốc, thường qua một hoạt động XOR, để tạo ra văn bản mã hóa.

Đôi khi mọi người định nghĩa điều kiện (1) một cách chặt chẽ hơn, bằng cách khẳng định rằng dòng khóa phải cụ thể là giả ngẫu nhiên. Điều này có nghĩa là cả thuật toán mã hóa dịch chuyển lẫn bảng mã một lần sẽ không được coi là thuật toán mã hóa luồng.

Theo quan điểm của tôi, việc định nghĩa điều kiện (1) một cách rộng rãi hơn cung cấp một cách dễ dàng hơn để tổ chức các kế hoạch mã hóa. Ngoài ra, nó có nghĩa là chúng ta không phải ngừng gọi một kế hoạch mã hóa cụ thể là thuật toán mã hóa luồng chỉ vì chúng ta biết rằng nó thực sự không dựa vào dòng khóa giả ngẫu nhiên.

**Ghi chú:**

[4] Bảo tàng Mật mã, "Đường dây nóng Washington-Moscow," 2013, có sẵn tại [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Thuật toán mã hóa khối
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Cách đầu tiên mà một **thuật toán mã hóa khối** thường được hiểu là như một cái gì đó nguyên thủy hơn thuật toán mã hóa luồng: Một thuật toán cốt lõi thực hiện một biến đổi bảo toàn độ dài trên một chuỗi có độ dài phù hợp với sự giúp đỡ của một khóa. Thuật toán này có thể được sử dụng để tạo ra các kế hoạch mã hóa và có thể là các loại kế hoạch mật mã khác.
Thường xuyên, một thuật toán mã hóa khối có thể nhận đầu vào là các chuỗi có độ dài khác nhau như 64, 128, hoặc 256 bit, cũng như các khóa có độ dài khác nhau như 128, 192, hoặc 256 bit. Mặc dù một số chi tiết của thuật toán có thể thay đổi tùy thuộc vào các biến số này, nhưng thuật toán cốt lõi không thay đổi. Nếu nó thay đổi, chúng ta sẽ nói về hai thuật toán mã hóa khối khác nhau. Lưu ý rằng việc sử dụng thuật ngữ thuật toán cốt lõi ở đây giống như đối với các phương thức mã hóa.

Một hình ảnh mô tả cách một thuật toán mã hóa khối hoạt động có thể được thấy trong *Hình 4* dưới đây. Một thông điệp $M$ có độ dài $L$ và một khóa $K$ phục vụ như là đầu vào cho Thuật toán mã hóa khối. Nó xuất ra một thông điệp $M'$ có độ dài $L$. Khóa không nhất thiết cần phải có cùng độ dài với $M$ và $M'$ đối với hầu hết các thuật toán mã hóa khối.

*Hình 4: Một thuật toán mã hóa khối*

![Hình 4: Một thuật toán mã hóa khối](assets/Figure4-4.webp "Hình 4: Một thuật toán mã hóa khối")

Một thuật toán mã hóa khối một mình không phải là một phương thức mã hóa. Nhưng một thuật toán mã hóa khối có thể được sử dụng với các **chế độ hoạt động** khác nhau để tạo ra các phương thức mã hóa khác nhau. Một chế độ hoạt động đơn giản thêm một số hoạt động bổ sung bên ngoài thuật toán mã hóa khối.

Để minh họa cách thức hoạt động này, giả sử một thuật toán mã hóa khối (BC) yêu cầu một chuỗi đầu vào 128-bit và một khóa riêng tư 128-bit. Hình 5 dưới đây hiển thị cách thuật toán mã hóa khối đó có thể được sử dụng với **chế độ sách mã điện tử** (**ECB mode**) để tạo ra một phương thức mã hóa. (Các dấu chấm lửng ở bên phải chỉ ra rằng bạn có thể lặp lại mô hình này theo nhu cầu).

*Hình 5: Một thuật toán mã hóa khối với chế độ ECB*

![Hình 5: Một thuật toán mã hóa khối với chế độ ECB](assets/Figure4-5.webp "Hình 5: Một thuật toán mã hóa khối với chế độ ECB")

Quy trình mã hóa sách mã điện tử với thuật toán mã hóa khối như sau. Xem bạn có thể chia thông điệp văn bản gốc của mình thành các khối 128-bit không. Nếu không, thêm **đệm** vào thông điệp, để kết quả có thể được chia đều theo kích thước khối 128 bit. Đây là dữ liệu của bạn được sử dụng cho quá trình mã hóa.

Bây giờ chia dữ liệu thành các chuỗi 128-bit ($M_1$, $M_2$, $M_3$, và vân vân). Chạy từng chuỗi 128-bit qua thuật toán mã hóa khối với khóa 128-bit của bạn để tạo ra các khối mã hóa 128-bit ($C_1$, $C_2$, $C_3$, và vân vân). Những khối này, khi được kết hợp lại, tạo thành mã hóa đầy đủ.

Giải mã chỉ là quá trình đảo ngược, mặc dù người nhận cần một cách nhận biết nào đó để loại bỏ bất kỳ đệm nào từ dữ liệu đã giải mã để tạo ra thông điệp văn bản gốc.

Mặc dù tương đối đơn giản, một thuật toán mã hóa khối với chế độ sách mã điện tử thiếu an toàn. Điều này là do nó dẫn đến **mã hóa xác định**. Bất kỳ hai chuỗi dữ liệu 128-bit giống hệt nhau đều được mã hóa chính xác theo cùng một cách. Thông tin đó có thể bị khai thác.

Thay vào đó, bất kỳ phương thức mã hóa nào được xây dựng từ một thuật toán mã hóa khối nên là **xác suất**: tức là, việc mã hóa bất kỳ thông điệp $M$, hoặc bất kỳ khối cụ thể nào của $M$, nên chung quy cho một kết quả khác nhau mỗi lần. [5]

**Chế độ chuỗi khối mã hóa** (**CBC mode**) có lẽ là chế độ phổ biến nhất được sử dụng với một thuật toán mã hóa khối. Sự kết hợp, nếu được thực hiện đúng cách, tạo ra một phương thức mã hóa xác suất. Bạn có thể thấy một hình ảnh mô tả chế độ hoạt động này trong *Hình 6* dưới đây.

*Hình 6: Một thuật toán mã hóa khối với chế độ CBC*
![Hình 6: Một mật mã khối với chế độ CBC](assets/Figure4-6.webp "Hình 6: Một mật mã khối với chế độ CBC")
Giả sử kích thước khối là 128 bit. Vì vậy, để bắt đầu, bạn cần đảm bảo rằng thông điệp văn bản gốc của bạn nhận được đệm cần thiết.

Sau đó, bạn XOR phần 128-bit đầu tiên của văn bản gốc với một **vector khởi tạo** 128-bit. Kết quả được đưa vào mật mã khối để tạo ra một bản mã hóa cho khối đầu tiên. Đối với khối thứ hai 128 bit, bạn trước tiên XOR văn bản gốc với bản mã hóa từ khối đầu tiên, trước khi chèn nó vào mật mã khối. Bạn tiếp tục quá trình này cho đến khi bạn đã mã hóa toàn bộ thông điệp văn bản gốc của mình.

Khi hoàn thành, bạn gửi thông điệp đã mã hóa cùng với vector khởi tạo chưa mã hóa cho người nhận. Người nhận cần biết vector khởi tạo, nếu không cô ấy không thể giải mã bản mã hóa.

Cấu trúc này an toàn hơn nhiều so với chế độ sách mã điện tử khi được sử dụng đúng cách. Đầu tiên, bạn nên đảm bảo rằng vector khởi tạo là một chuỗi ngẫu nhiên hoặc giả ngẫu nhiên. Ngoài ra, bạn nên sử dụng một vector khởi tạo khác nhau mỗi lần bạn sử dụng phương thức mã hóa này.

Nói cách khác, vector khởi tạo của bạn nên là một nonce ngẫu nhiên hoặc giả ngẫu nhiên, nơi mà **nonce** có nghĩa là "một số chỉ được sử dụng một lần." Nếu bạn giữ nguyên thực hành này, thì chế độ CBC với mật mã khối đảm bảo rằng bất kỳ hai khối văn bản gốc giống nhau nào cũng sẽ được mã hóa khác nhau mỗi lần.

Cuối cùng, hãy chú ý đến **chế độ phản hồi đầu ra** (**chế độ OFB**). Bạn có thể thấy một hình ảnh về chế độ này trong *Hình 7*.

*Hình 7: Một mật mã khối với chế độ OFB*

![Hình 7: Một mật mã khối với chế độ OFB](assets/Figure4-7.webp "Hình 7: Một mật mã khối với chế độ OFB")

Với chế độ OFB, bạn cũng chọn một vector khởi tạo. Nhưng ở đây, cho khối đầu tiên, vector khởi tạo được trực tiếp chèn vào mật mã khối với khóa của bạn. 128-bit kết quả, sau đó, được xử lý như một luồng khóa. Luồng khóa này được XOR với văn bản gốc để tạo ra bản mã hóa cho khối. Đối với các khối tiếp theo, bạn sử dụng luồng khóa từ khối trước đó làm đầu vào vào mật mã khối và lặp lại các bước.

Nếu bạn quan sát kỹ, những gì thực sự được tạo ra ở đây từ mật mã khối với chế độ OFB là một mật mã luồng. Bạn tạo ra các phần luồng khóa 128-bit cho đến khi bạn có độ dài của văn bản gốc (loại bỏ các bit bạn không cần từ phần luồng khóa 128-bit cuối cùng). Sau đó, bạn XOR luồng khóa với thông điệp văn bản gốc của mình để nhận được bản mã hóa.

Trong phần trước về mật mã luồng, tôi đã nói rằng bạn tạo ra một luồng khóa với sự giúp đỡ của một khóa riêng tư. Để chính xác, nó không chỉ được tạo ra với một khóa riêng tư. Như bạn có thể thấy trong chế độ OFB, luồng khóa được sản xuất với sự hỗ trợ của cả một khóa riêng tư và một vector khởi tạo.

Lưu ý rằng như với chế độ CBC, việc chọn một nonce ngẫu nhiên hoặc giả ngẫu nhiên cho vector khởi tạo mỗi lần bạn sử dụng một mật mã khối trong chế độ OFB là quan trọng. Nếu không, cùng một chuỗi thông điệp 128-bit được gửi trong các giao tiếp khác nhau sẽ được mã hóa theo cùng một cách. Đây là một cách để tạo ra mã hóa xác suất với một mật mã luồng.
Một số thuật toán mã hóa luồng chỉ sử dụng khóa riêng để tạo ra dòng khóa. Đối với những thuật toán mã hóa luồng này, việc sử dụng một nonce ngẫu nhiên để chọn khóa riêng cho mỗi lần giao tiếp là rất quan trọng. Nếu không, kết quả của việc mã hóa với những thuật toán mã hóa luồng này cũng sẽ là định trước, dẫn đến các vấn đề về bảo mật.

Thuật toán mã hóa khối phổ biến nhất hiện nay là **Rijndael cipher**. Đây là bản thắng cuộc trong số mười lăm bài dự thi của một cuộc thi do Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) tổ chức từ năm 1997 đến năm 2000 nhằm thay thế một tiêu chuẩn mã hóa cũ, **tiêu chuẩn mã hóa dữ liệu** (**DES**).

Rijndael cipher có thể được sử dụng với các thông số kỹ thuật khác nhau cho độ dài khóa và kích thước khối, cũng như trong các chế độ hoạt động khác nhau. Ban tổ chức cuộc thi NIST đã chọn một phiên bản hạn chế của Rijndael cipher—cụ thể là một phiên bản yêu cầu kích thước khối 128-bit và độ dài khóa là 128 bit, 192 bit, hoặc 256 bit—làm một phần của **tiêu chuẩn mã hóa nâng cao** (**AES**). Đây thực sự là tiêu chuẩn chính cho các ứng dụng mã hóa đối xứng. Nó an toàn đến mức ngay cả NSA cũng sẵn lòng sử dụng nó với khóa 256-bit cho các tài liệu mật hàng đầu. [6]

Thuật toán mã hóa khối AES sẽ được giải thích chi tiết trong *Chương 5*.

**Ghi chú:**

[5] Tầm quan trọng của mã hóa xác suất lần đầu tiên được nhấn mạnh bởi Shafi Goldwasser và Silvio Micali, “Probabilistic encryption,” _Journal of Computer and System Sciences_, 28 (1984), 270–99.

[6] Xem NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).

## Làm rõ sự nhầm lẫn
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Sự nhầm lẫn về sự phân biệt giữa thuật toán mã hóa khối và thuật toán mã hóa luồng xuất hiện bởi vì đôi khi mọi người sẽ hiểu thuật ngữ thuật toán mã hóa khối như đang đề cập cụ thể đến *thuật toán mã hóa khối với chế độ mã hóa khối*.

Xem xét các chế độ ECB và CBC trong phần trước. Những chế độ này cụ thể yêu cầu dữ liệu cho việc mã hóa phải chia hết cho kích thước khối (nghĩa là bạn có thể phải sử dụng đệm cho tin nhắn gốc). Ngoài ra, dữ liệu trong những chế độ này cũng được thuật toán mã hóa khối xử lý trực tiếp (và không chỉ kết hợp với kết quả của một hoạt động mã hóa khối như trong chế độ OFB).

Do đó, một cách khác, bạn có thể định nghĩa một **thuật toán mã hóa khối** là bất kỳ phương pháp mã hóa nào, hoạt động trên các khối tin nhắn có độ dài cố định mỗi lần (nơi mỗi khối phải dài hơn một byte, nếu không nó sẽ chuyển thành thuật toán mã hóa luồng). Cả dữ liệu cho mã hóa và văn bản mã hóa phải chia đều theo kích thước khối này. Thông thường, kích thước khối là 64, 128, 192, hoặc 256 bit. Ngược lại, một thuật toán mã hóa luồng có thể mã hóa bất kỳ tin nhắn nào theo từng bit hoặc byte một lúc.

Với sự hiểu biết cụ thể hơn này về thuật toán mã hóa khối, bạn có thể khẳng định rằng các phương pháp mã hóa hiện đại hoặc là thuật toán mã hóa luồng hoặc là thuật toán mã hóa khối. Từ đây trở đi, tôi sẽ sử dụng thuật ngữ thuật toán mã hóa khối trong nghĩa rộng hơn trừ khi có chỉ định khác.
Cuộc thảo luận về chế độ OFB trong phần trước cũng đề cập đến một điểm thú vị khác. Một số thuật toán mã hóa luồng được xây dựng từ các thuật toán mã hóa khối, như Rijndael với OFB. Một số khác như Salsa20 và ChaCha không được tạo ra từ các thuật toán mã hóa khối. Bạn có thể gọi những thuật toán sau là **thuật toán mã hóa luồng nguyên thủy**. (Thực sự không có một thuật ngữ chuẩn mực nào để chỉ các thuật toán mã hóa luồng như vậy.)

Khi mọi người nói về ưu và nhược điểm của thuật toán mã hóa luồng và thuật toán mã hóa khối, họ thường so sánh thuật toán mã hóa luồng nguyên thủy với các phương pháp mã hóa dựa trên thuật toán mã hóa khối.

Mặc dù bạn luôn có thể dễ dàng xây dựng một thuật toán mã hóa luồng từ một thuật toán mã hóa khối, thì việc xây dựng một loại cấu trúc nào đó với chế độ mã hóa khối (như với chế độ CBC) từ một thuật toán mã hóa luồng nguyên thủy thường rất khó khăn.

Từ cuộc thảo luận này, bạn nên hiểu được *Hình 8*. Nó cung cấp một cái nhìn tổng quan về các phương pháp mã hóa đối xứng. Chúng tôi sử dụng ba loại phương pháp mã hóa: thuật toán mã hóa luồng nguyên thủy, thuật toán mã hóa luồng dựa trên thuật toán mã hóa khối, và thuật toán mã hóa khối trong một chế độ khối (cũng được gọi là “thuật toán mã hóa khối” trong sơ đồ).

*Hình 8: Tổng quan về các phương pháp mã hóa đối xứng*

![Hình 8: Tổng quan về các phương pháp mã hóa đối xứng](assets/Figure4-8.webp "Hình 8: Tổng quan về các phương pháp mã hóa đối xứng")

## Mã xác thực tin nhắn
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Mã hóa quan tâm đến bí mật. Nhưng mật mã học cũng quan tâm đến các chủ đề rộng lớn hơn, như tính toàn vẹn của tin nhắn, tính xác thực, và không thể chối cãi. Các **mã xác thực tin nhắn** (MACs) là các phương pháp mật mã học dựa trên khóa đối xứng hỗ trợ tính xác thực và toàn vẹn trong giao tiếp.

Tại sao cần có gì ngoài bí mật trong giao tiếp? Giả sử Bob gửi cho Alice một tin nhắn sử dụng mã hóa gần như không thể phá vỡ. Bất kỳ kẻ tấn công nào chặn được tin nhắn này cũng sẽ không thể hiểu được bất kỳ thông tin quan trọng nào về nội dung. Tuy nhiên, kẻ tấn công vẫn có ít nhất hai vector tấn công khác có sẵn:

1. Cô ta có thể chặn bản mã hóa, thay đổi nội dung của nó và gửi bản mã hóa đã thay đổi đến Alice.
2. Cô ta có thể chặn hoàn toàn tin nhắn của Bob và gửi bản mã hóa do mình tạo ra.

Trong cả hai trường hợp này, kẻ tấn công có thể không có bất kỳ hiểu biết nào về nội dung từ các bản mã hóa (1) và (2). Nhưng cô ta vẫn có thể gây ra thiệt hại đáng kể theo cách này. Đây là nơi mà mã xác thực tin nhắn trở nên quan trọng.

Mã xác thực tin nhắn được định nghĩa một cách lỏng lẻo là các phương pháp mật mã học đối xứng với ba thuật toán: một thuật toán tạo khóa, một thuật toán tạo thẻ, và một thuật toán xác minh. Một MAC an toàn đảm bảo rằng các thẻ là **không thể giả mạo tồn tại** đối với bất kỳ kẻ tấn công nào - tức là, họ không thể thành công trong việc tạo ra một thẻ trên tin nhắn mà được xác minh, trừ khi họ có khóa riêng.

Bob và Alice có thể chống lại việc thao túng một tin nhắn cụ thể bằng cách sử dụng MAC. Giả sử trong một thời điểm họ không quan tâm đến bí mật. Họ chỉ muốn đảm bảo rằng tin nhắn mà Alice nhận được thực sự từ Bob và không bị thay đổi theo bất kỳ cách nào.

Quy trình được mô tả trong *Hình 9*. Để sử dụng **MAC** (Mã Xác Thực Tin Nhắn), họ sẽ trước tiên tạo ra một khóa riêng $K$ được chia sẻ giữa hai người. Bob tạo ra một thẻ $T$ cho tin nhắn sử dụng khóa riêng $K$. Sau đó, anh ấy gửi tin nhắn cùng với thẻ tin nhắn cho Alice. Cô ấy sau đó có thể xác minh rằng Bob thực sự đã tạo ra thẻ, bằng cách chạy khóa riêng, tin nhắn, và thẻ qua một thuật toán xác minh.

*Hình 9: Tổng quan về các phương pháp mã hóa đối xứng*
![Hình 9: Tổng quan về các phương pháp mã hóa đối xứng](assets/Figure4-9.webp "Hình 9: Tổng quan về các phương pháp mã hóa đối xứng")
Do **khả năng không thể giả mạo tồn tại**, một kẻ tấn công không thể thay đổi thông điệp $M$ theo bất kỳ cách nào hoặc tạo ra một thông điệp của riêng mình với một thẻ hợp lệ. Điều này vẫn đúng, ngay cả khi kẻ tấn công quan sát các thẻ của nhiều thông điệp giữa Bob và Alice sử dụng chung một khóa riêng. Tối đa, kẻ tấn công có thể ngăn Alice nhận được thông điệp $M$ (một vấn đề mà mật mã học không thể giải quyết).

Một MAC đảm bảo rằng một thông điệp thực sự được tạo ra bởi Bob. Tính xác thực này, tự động ngụ ý tính toàn vẹn của thông điệp—nghĩa là, nếu Bob đã tạo ra một số thông điệp, thì, theo đó, nó không được thay đổi theo bất kỳ cách nào bởi kẻ tấn công. Vì vậy từ đây trở đi, mọi quan tâm đến xác thực nên được tự động hiểu là bao gồm quan tâm đến tính toàn vẹn.

Mặc dù tôi đã phân biệt giữa tính xác thực và tính toàn vẹn của thông điệp trong bài thảo luận của mình, cũng thường thấy việc sử dụng những thuật ngữ này như những từ đồng nghĩa. Chúng, sau đó, đề cập đến ý tưởng của các thông điệp được tạo ra bởi một người gửi cụ thể và không bị thay đổi theo bất kỳ cách nào. Theo tinh thần này, mã xác thực thông điệp thường cũng được gọi là **mã toàn vẹn thông điệp**.


## Mã hóa xác thực
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Thông thường, bạn sẽ muốn đảm bảo cả bí mật và tính xác thực trong giao tiếp và, do đó, các phương pháp mã hóa và các phương pháp MAC thường được sử dụng cùng nhau.

Một **phương pháp mã hóa xác thực** là một phương pháp kết hợp mã hóa với một MAC một cách an toàn cao. Cụ thể, nó phải đáp ứng các tiêu chuẩn cho khả năng không thể giả mạo tồn tại cũng như một khái niệm rất mạnh về bí mật, cụ thể là khả năng chống lại **các cuộc tấn công chọn bản mã**. [7]

Để một phương pháp mã hóa có khả năng chống lại các cuộc tấn công chọn bản mã, nó phải đáp ứng các tiêu chuẩn cho **khả năng không biến dạng**: tức là, bất kỳ sự thay đổi nào của bản mã bởi kẻ tấn công nên dẫn đến một bản mã không hợp lệ hoặc một bản mã mà khi giải mã sẽ không có mối liên hệ nào với bản gốc. [8]

Vì một phương pháp mã hóa xác thực đảm bảo rằng một bản mã được tạo ra bởi kẻ tấn công luôn không hợp lệ (vì thẻ sẽ không được xác minh), nó đáp ứng các tiêu chuẩn cho khả năng chống lại các cuộc tấn công chọn bản mã. Thú vị là, bạn có thể chứng minh rằng một phương pháp mã hóa xác thực luôn có thể được tạo ra từ sự kết hợp của một MAC không thể giả mạo tồn tại và một phương pháp mã hóa đáp ứng một khái niệm an toàn ít mạnh mẽ hơn, được biết đến là **an toàn trước cuộc tấn công chọn bản rõ**.

Chúng tôi sẽ không đi sâu vào tất cả các chi tiết của việc xây dựng các phương pháp mã hóa xác thực. Nhưng quan trọng là phải biết hai chi tiết trong cấu trúc của chúng.

Đầu tiên, một phương pháp mã hóa xác thực trước tiên xử lý việc mã hóa và sau đó tạo một thẻ thông điệp trên bản mã. Hóa ra, các phương pháp khác—như kết hợp bản mã với một thẻ trên bản rõ, hoặc trước tiên tạo một thẻ và sau đó mã hóa cả bản rõ và thẻ—là không an toàn. Ngoài ra, cả hai hoạt động đều có khóa riêng được chọn ngẫu nhiên của riêng mình, nếu không an ninh của bạn sẽ bị tổn hại nghiêm trọng.

Nguyên tắc nêu trên áp dụng một cách tổng quát hơn: *bạn nên luôn sử dụng các khóa khác nhau khi kết hợp các phương pháp mật mã học cơ bản*.

Một phương pháp mã hóa xác thực được mô tả trong *Hình 10*. Bob trước tiên tạo ra một bản mã $C$ từ thông điệp $M$ sử dụng một khóa $K_C$ được chọn ngẫu nhiên. Sau đó, anh ta tạo ra một thẻ thông điệp $T$ bằng cách chạy bản mã và một khóa ngẫu nhiên khác $K_T$ qua thuật toán tạo thẻ. Cả bản mã và thẻ thông điệp đều được gửi cho Alice.
Alice giờ đây trước tiên kiểm tra xem thẻ có hợp lệ với bản mã $C$ và khóa $K_T$ hay không. Nếu hợp lệ, cô ấy có thể giải mã tin nhắn bằng khóa $K_C$. Không chỉ cô ấy được đảm bảo một khái niệm rất mạnh mẽ về bí mật trong giao tiếp của họ, mà cô ấy còn biết rằng tin nhắn được tạo ra bởi Bob.
*Hình 10: Một lược đồ mã hóa xác thực*

![Hình 10: Một lược đồ mã hóa xác thực](assets/Figure4-10.webp "Hình 10: Một lược đồ mã hóa xác thực")

MAC được tạo ra như thế nào? Mặc dù MAC có thể được tạo ra thông qua nhiều phương pháp, một cách phổ biến và hiệu quả để tạo chúng là qua **hàm băm mật mã**.

Chúng tôi sẽ giới thiệu kỹ hơn về hàm băm mật mã trong *Chương 6*. Hiện tại, chỉ cần biết rằng một **hàm băm** là một hàm có thể tính toán hiệu quả, nhận đầu vào có kích thước tùy ý và tạo ra đầu ra có độ dài cố định. Ví dụ, hàm băm phổ biến **SHA-256** (secure hash algorithm 256) luôn tạo ra một đầu ra 256-bit bất kể kích thước của đầu vào. Một số hàm băm, như SHA-256, có ứng dụng hữu ích trong mật mã học.

Loại thẻ phổ biến nhất được tạo ra với hàm băm mật mã là **mã xác thực tin nhắn dựa trên băm** (HMAC). Quy trình được mô tả trong *Hình 11*. Một bên tạo ra hai khóa riêng biệt từ một khóa riêng $K$, khóa bên trong $K_1$ và khóa bên ngoài $K_2$. Bản rõ $M$ hoặc bản mã $C$ sau đó được băm cùng với khóa bên trong. Kết quả $T'$ sau đó được băm với khóa bên ngoài để tạo ra thẻ tin nhắn $T$.

Có một bảng màu của các hàm băm có thể được sử dụng để tạo ra một HMAC. Hàm băm thường được sử dụng nhất là SHA-256.

*Hình 11: HMAC*

![Hình 11: HMAC](assets/Figure4-11.webp "Hình 11: HMAC")

**Ghi chú:**

[7] Các kết quả cụ thể được thảo luận trong phần này đến từ Katz và Lindell, trang 131–47.

[8] Về mặt kỹ thuật, định nghĩa của các cuộc tấn công bản mã được chọn khác với khái niệm không thể biến đổi. Nhưng bạn có thể chứng minh rằng hai khái niệm về bảo mật này là tương đương.

## Phiên giao tiếp an toàn
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Giả sử hai bên đang trong một phiên giao tiếp, vì vậy họ gửi nhiều tin nhắn qua lại.

Một lược đồ mã hóa xác thực cho phép người nhận của một tin nhắn xác minh rằng nó được tạo ra bởi đối tác của họ trong phiên giao tiếp (miễn là khóa riêng không bị rò rỉ). Điều này hoạt động tốt đủ cho một tin nhắn đơn lẻ. Tuy nhiên, thường thì hai bên gửi tin nhắn qua lại trong một phiên giao tiếp. Và trong bối cảnh đó, một lược đồ mã hóa xác thực đơn giản như được mô tả trong phần trước không đủ để cung cấp bảo mật.

Lý do chính là một lược đồ mã hóa xác thực không cung cấp bất kỳ bảo đảm nào rằng tin nhắn thực sự cũng được gửi bởi đại lý đã tạo ra nó trong một phiên giao tiếp. Xem xét ba vectơ tấn công sau:

1. **Tấn công phát lại**: Một kẻ tấn công gửi lại một bản mã và một thẻ mà cô ta đã chặn giữa hai bên tại một thời điểm trước đó.
2. **Tấn công thay đổi thứ tự**: Một kẻ tấn công chặn hai tin nhắn tại các thời điểm khác nhau và gửi chúng đến người nhận theo thứ tự ngược lại.
3. **Tấn công phản xạ**: Một kẻ tấn công quan sát một tin nhắn được gửi từ A đến B, và cũng gửi tin nhắn đó đến A.

Mặc dù kẻ tấn công không biết thông tin về bản mã và không thể tạo ra bản mã giả mạo, các cuộc tấn công trên vẫn có thể gây ra thiệt hại đáng kể trong giao tiếp.
Giả sử, ví dụ, một thông điệp cụ thể giữa hai bên liên quan đến việc chuyển giao tài chính. Một cuộc tấn công replay có thể chuyển giao số tiền một lần nữa. Một lược đồ mã hóa xác thực cơ bản không có phòng vệ chống lại những cuộc tấn công như vậy.
May mắn thay, những loại tấn công này có thể được giảm thiểu một cách dễ dàng trong một phiên giao tiếp sử dụng **identifiers** và **relative time indicators**.

Các identifiers có thể được thêm vào thông điệp văn bản gốc trước khi mã hóa. Điều này sẽ ngăn chặn bất kỳ cuộc tấn công phản chiếu nào. Một chỉ báo thời gian tương đối, ví dụ, có thể là một số thứ tự trong một phiên giao tiếp cụ thể. Mỗi bên thêm một số thứ tự vào thông điệp trước khi mã hóa, vì vậy người nhận biết được thứ tự mà các thông điệp được gửi. Điều này loại bỏ khả năng của các cuộc tấn công sắp xếp lại. Nó cũng loại bỏ các cuộc tấn công replay. Bất kỳ thông điệp nào mà kẻ tấn công gửi đi sau này sẽ có một số thứ tự cũ, và người nhận sẽ biết không xử lý lại thông điệp đó.

Để minh họa cách thức hoạt động của phiên giao tiếp an toàn, giả sử lại Alice và Bob. Họ gửi tổng cộng bốn thông điệp qua lại. Bạn có thể thấy một lược đồ mã hóa xác thực với các identifiers và số thứ tự hoạt động như thế nào dưới đây trong *Hình 11*.

Phiên giao tiếp bắt đầu với Bob gửi một bản mã hóa $C_{0,B}$ cho Alice với một thẻ thông điệp $T_{0,B}$. Bản mã hóa chứa thông điệp, cũng như một identifier (BOB) và một số thứ tự (0). Thẻ $T_{0,B}$ được tạo ra trên toàn bộ bản mã hóa. Trong các giao tiếp tiếp theo, Alice và Bob duy trì giao thức này, cập nhật các trường dữ liệu khi cần thiết.

*Hình 12: Một phiên giao tiếp an toàn*

![Hình 12: Một phiên giao tiếp an toàn](assets/Figure4-12.webp "Hình 12: Một phiên giao tiếp an toàn")

# RC4 và AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## Bộ mã hóa luồng RC4
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

Trong Chương này, chúng ta sẽ thảo luận chi tiết về một lược đồ mã hóa với một bộ mã hóa luồng hiện đại, RC4 (hoặc "Rivest cipher 4"), và một bộ mã hóa khối hiện đại, AES. Mặc dù bộ mã hóa RC4 đã không còn được ưa chuộng làm phương pháp mã hóa, AES là tiêu chuẩn cho mã hóa đối xứng hiện đại. Hai ví dụ này sẽ giúp hiểu rõ hơn về cách thức hoạt động của mã hóa đối xứng từ bên trong.

___

Để có cái nhìn về cách thức hoạt động của các bộ mã hóa luồng giả ngẫu nhiên hiện đại, tôi sẽ tập trung vào bộ mã hóa luồng RC4. Đây là một bộ mã hóa luồng giả ngẫu nhiên đã được sử dụng trong các giao thức bảo mật điểm truy cập không dây WEP và WAP cũng như trong TLS. Do RC4 có nhiều điểm yếu đã được chứng minh, nó đã không còn được ưa chuộng. Thực tế, Internet Engineering Task Force hiện nay cấm sử dụng các bộ RC4 bởi các ứng dụng client và server trong mọi trường hợp của TLS. Tuy nhiên, nó vẫn là một ví dụ tốt để minh họa cách một bộ mã hóa luồng nguyên thủy hoạt động.

Để bắt đầu, tôi sẽ trước tiên chỉ cách mã hóa một thông điệp văn bản gốc với một bộ mã hóa RC4 nhỏ. Giả sử thông điệp văn bản gốc của chúng ta là “SOUP.” Mã hóa với bộ mã hóa RC4 nhỏ của chúng ta, sau đó, tiến hành trong bốn bước.

### Bước 1
Đầu tiên, hãy định nghĩa một mảng **S** với $S[0] = 0$ đến $S[7] = 7$. Một mảng ở đây đơn giản chỉ là một tập hợp các giá trị có thể thay đổi được tổ chức bởi một chỉ số, còn được gọi là danh sách trong một số ngôn ngữ lập trình (ví dụ, Python). Trong trường hợp này, chỉ số chạy từ 0 đến 7, và các giá trị cũng chạy từ 0 đến 7. Vậy **S** như sau:
- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Các giá trị ở đây không phải là số ASCII, mà là biểu diễn giá trị thập phân của các chuỗi 1 byte. Vậy giá trị 2 sẽ bằng $0000 \ 0011$. Do đó, độ dài của mảng **S** là 8 byte.

### Bước 2

Thứ hai, hãy định nghĩa một mảng khóa **K** có độ dài 8 byte bằng cách chọn một khóa từ 1 đến 8 byte (không chấp nhận phân số byte). Vì mỗi byte là 8 bit, bạn có thể chọn bất kỳ số nào từ 0 đến 255 cho mỗi byte của khóa của bạn.

Giả sử chúng ta chọn khóa **k** của mình là $[14, 48, 9]$, vậy nó có độ dài 3 byte. Mỗi chỉ số của mảng khóa của chúng ta, sau đó, được thiết lập theo giá trị thập phân cho từng phần tử cụ thể của khóa, theo thứ tự. Nếu bạn chạy qua toàn bộ khóa, bắt đầu lại từ đầu, cho đến khi bạn đã điền đủ 8 ô của mảng khóa. Vậy mảng khóa của chúng ta như sau:

- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Bước 3

Thứ ba, chúng ta sẽ biến đổi mảng **S** sử dụng mảng khóa **K**, trong một quá trình được gọi là **lập lịch khóa**. Quá trình này được mô tả như sau trong giả mã:

- Tạo biến **j** và **i**
- Đặt biến $j = 0$
- Đối với mỗi $i$ từ 0 đến 7:
    - Đặt $j = (j + S[i] + K[i]) \mod 8$
    - Hoán đổi $S[i]$ và $S[j]$

Sự biến đổi của mảng **S** được ghi lại bởi *Bảng 1*.

Để bắt đầu, bạn có thể thấy trạng thái ban đầu của **S** là $[0, 1, 2, 3, 4, 5, 6, 7]$ với giá trị ban đầu là 0 cho **j**. Điều này sẽ được biến đổi sử dụng mảng khóa $[14, 48, 9, 14, 48, 9, 14, 48]$.

Vòng lặp for bắt đầu với $i = 0$. Theo giả mã trên, giá trị mới của **j** trở thành 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Hoán đổi $S[0]$ và $S[6]$, trạng thái của **S** sau 1 vòng trở thành $[6, 1, 2, 3, 4, 5, 0, 7]$.
Ở hàng tiếp theo, $i = 1$. Khi đi qua vòng lặp for một lần nữa, **j** nhận được giá trị là 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Khi hoán đổi $S[1]$ và $S[7]$ từ trạng thái hiện tại của **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, ta được $[6, 7, 2, 3, 4, 5, 0, 1]$ sau vòng 2.
Chúng ta tiếp tục quá trình này cho đến khi tạo ra hàng cuối cùng ở phía dưới cho mảng **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Bảng 1: Bảng lập lịch khóa*

| Vòng   | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Ban đầu |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Bước 4
Là bước thứ tư, chúng ta tạo ra **keystream**. Đây là chuỗi giả ngẫu nhiên có độ dài bằng với thông điệp mà chúng ta muốn gửi. Điều này sẽ được sử dụng để mã hóa thông điệp gốc “SOUP.” Vì keystream cần phải dài bằng thông điệp, chúng ta cần một chuỗi có 4 byte.
Keystream được tạo ra bởi pseudocode sau:

- Tạo các biến **j**, **i**, và **t**.
- Đặt $j = 0$.
- Đối với mỗi $i$ của plaintext, bắt đầu từ $i = 1$ và tiếp tục cho đến $i = 4$, mỗi byte của keystream được tạo ra như sau:
    - $j = (j + S[i]) \mod 8$
    - Hoán đổi $S[i]$ và $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - Byte thứ $i$ của keystream = $S[t]$

Bạn có thể theo dõi các phép tính trong *Bảng 2*.

Trạng thái ban đầu của **S** là $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Đặt $i = 1$, giá trị của **j** trở thành 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Chúng ta sau đó hoán đổi $S[1]$ và $S[4]$ để tạo ra sự biến đổi của **S** ở hàng thứ hai, $[6, 3, 1, 0, 4, 7, 5, 2]$. Giá trị của **t** sau đó là 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Cuối cùng, byte cho keystream là $S[7]$, hay 2.

Chúng ta sau đó tiếp tục tạo ra các byte khác cho đến khi chúng ta có bốn byte sau: 2, 6, 3, và 7. Mỗi byte này sau đó có thể được sử dụng để mã hóa mỗi chữ cái của plaintext, "SOUP".

Để bắt đầu, sử dụng bảng ASCII, chúng ta có thể thấy rằng “SOUP” được mã hóa bởi các giá trị thập phân của các chuỗi byte cơ bản là “83 79 85 80”. Kết hợp với keystream “2 6 3 7” tạo ra “85 85 88 87”, giữ nguyên sau một phép toán modulo 256. Trong ASCII, ciphertext “85 85 88 87” bằng “UUXW”.

Điều gì xảy ra nếu từ cần mã hóa dài hơn mảng **S**? Trong trường hợp đó, mảng **S** chỉ tiếp tục biến đổi theo cách được hiển thị ở trên cho mỗi byte **i** của plaintext, cho đến khi chúng ta có một số byte trong keystream bằng với số chữ cái trong plaintext.

*Bảng 2: Tạo keystream*

| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
Ví dụ mà chúng ta vừa thảo luận chỉ là phiên bản giản lược của **mã hóa luồng RC4**. Mã hóa luồng RC4 thực tế có một mảng **S** dài 256 byte, không phải 8 byte, và một khóa có thể từ 1 đến 256 byte, không phải từ 1 đến 8 byte. Mảng khóa và các luồng khóa sau đó đều được sản xuất dựa trên độ dài 256 byte của mảng **S**. Các phép tính trở nên phức tạp hơn nhiều, nhưng nguyên tắc vẫn giữ nguyên. Sử dụng cùng một khóa, [14,48,9], với mã hóa RC4 tiêu chuẩn, thông điệp văn bản "SOUP" được mã hóa thành 67 02 ed df trong định dạng thập lục phân.

Một mã hóa luồng trong đó luồng khóa cập nhật độc lập với thông điệp văn bản hoặc văn bản mã hóa là **mã hóa luồng đồng bộ**. Luồng khóa chỉ phụ thuộc vào khóa. Rõ ràng, RC4 là một ví dụ của mã hóa luồng đồng bộ, vì luồng khóa không có mối quan hệ nào với văn bản gốc hoặc văn bản mã hóa. Tất cả các mã hóa luồng nguyên thủy của chúng tôi được đề cập trong chương trước, bao gồm mã hóa dịch chuyển, mã hóa Vigenère, và mã hóa một lần, cũng thuộc loại đồng bộ.

Ngược lại, một **mã hóa luồng không đồng bộ** có luồng khóa được sản xuất bởi cả khóa và các phần tử trước đó của văn bản mã hóa. Loại mã hóa này còn được gọi là **mã hóa tự đồng bộ**.

Quan trọng là luồng khóa được sản xuất với RC4 nên được xem như một mã hóa một lần, và bạn không thể sản xuất luồng khóa một cách chính xác như lần trước. Thay vì thay đổi khóa mỗi lần, giải pháp thực tế là kết hợp khóa với một **nonce** để sản xuất luồng byte.

## AES với khóa 128-bit
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Như đã đề cập trong chương trước, Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) đã tổ chức một cuộc thi từ năm 1997 đến năm 2000 để xác định một tiêu chuẩn mã hóa đối xứng mới. **Mã hóa Rijndael** đã trở thành bài dự thi chiến thắng. Tên gọi là một trò chơi chữ dựa trên tên của các nhà sáng tạo người Bỉ, Vincent Rijmen và Joan Daemen.
Mật mã Rijndael là một **mật mã khối**, có nghĩa là có một thuật toán cốt lõi, có thể được sử dụng với các thông số kỹ thuật khác nhau cho độ dài khóa và kích thước khối. Bạn có thể, sau đó, sử dụng nó với các chế độ hoạt động khác nhau để xây dựng các kế hoạch mã hóa.

Ủy ban của cuộc thi NIST đã chấp nhận một phiên bản hạn chế của mật mã Rijndael—cụ thể là phiên bản yêu cầu kích thước khối 128-bit và độ dài khóa là 128 bit, 192 bit, hoặc 256 bit—là một phần của **Tiêu chuẩn Mã hóa Nâng cao (AES)**. Phiên bản hạn chế này của mật mã Rijndael cũng có thể được sử dụng dưới nhiều chế độ hoạt động. Thông số kỹ thuật cho tiêu chuẩn được biết đến là **Tiêu chuẩn Mã hóa Nâng cao (AES)**.

Để minh họa cách mật mã Rijndael hoạt động, cốt lõi của AES, tôi sẽ trình bày quy trình mã hóa với một khóa 128-bit. Kích thước khóa có ảnh hưởng đến số vòng được tổ chức cho mỗi khối mã hóa. Đối với khóa 128-bit, cần 10 vòng. Với 192 bit và 256 bit, sẽ là 12 và 14 vòng, tương ứng.

Ngoài ra, tôi sẽ giả định rằng AES được sử dụng trong **chế độ ECB**. Điều này làm cho việc trình bày dễ dàng hơn và không ảnh hưởng đến thuật toán Rijndael. Để chắc chắn, chế độ ECB không an toàn trong thực tế vì nó dẫn đến mã hóa xác định. Chế độ an toàn thường được sử dụng với AES là **CBC** (Cipher Block Chaining).

Hãy gọi khóa là $K_0$. Cấu trúc với các thông số trên, sau đó, trông như trong *Hình 1*, nơi $M_i$ đại diện cho một phần của thông điệp bản rõ 128 bit và $C_i$ cho một phần của bản mã 128 bit. Đệm được thêm vào bản rõ cho khối cuối cùng, nếu bản rõ không thể chia đều cho kích thước khối.


*Hình 1: AES-ECB với một khóa 128-bit*

![Hình 1: AES-ECB với một khóa 128-bit](assets/Figure5-1.webp "Hình 1: AES-ECB với một khóa 128-bit")

Mỗi khối văn bản 128-bit đi qua mười vòng trong kế hoạch mã hóa Rijndael. Điều này yêu cầu một khóa vòng riêng biệt cho mỗi vòng ($K_1$ đến $K_{10}$). Những khóa này được sản xuất cho mỗi vòng từ khóa 128-bit gốc $K_0$ sử dụng một **thuật toán mở rộng khóa**. Do đó, cho mỗi khối văn bản cần được mã hóa, chúng ta sẽ sử dụng khóa gốc $K_0$ cũng như mười khóa vòng riêng biệt. Lưu ý rằng những 11 khóa này được sử dụng cho mỗi khối bản rõ 128-bit cần mã hóa.

Thuật toán mở rộng khóa dài và phức tạp. Việc xem xét nó có ít lợi ích giáo dục. Bạn có thể tự mình xem qua thuật toán mở rộng khóa, nếu bạn muốn. Một khi các khóa vòng được sản xuất, mật mã Rijndael sẽ thao tác khối bản rõ 128-bit đầu tiên, $M_1$, như thấy trong *Hình 2*. Chúng ta sẽ giờ đi qua các bước này.

*Hình 2: Sự thao tác của $M_1$ với mật mã Rijndael:*

**Vòng 0:**
- XOR $M_1$ và $K_0$ để tạo ra $S_0$

---

**Vòng n cho n = {1,...,9}:**
- XOR $S_{n-1}$ và $K_n$
- Thay thế Byte
- Dịch Hàng
- Trộn Cột
- XOR $S$ và $K_n$ để tạo ra $S_n$

---

**Vòng 10:**
- XOR $S_9$ và $K_{10}$- Thay thế byte
- Dịch hàng
- XOR $S$ và $K_{10}$ để tạo ra $S_{10}$
- $S_{10}$ = $C_1$

### Vòng 0

Vòng 0 của thuật toán mã hóa Rijndael khá đơn giản. Một mảng $S_0$ được tạo ra bởi phép toán XOR giữa bản rõ 128-bit và khóa riêng. Cụ thể là,

- $S_0 = M_1 \oplus K_0$

### Vòng 1

Trong vòng 1, mảng $S_0$ đầu tiên được kết hợp với khóa vòng $K_1$ sử dụng phép toán XOR. Điều này tạo ra một trạng thái mới của $S$.

Thứ hai, thực hiện phép **thay thế byte** trên trạng thái hiện tại của $S$. Phép toán này hoạt động bằng cách lấy từng byte của mảng 16-byte $S$ và thay thế nó bằng một byte từ một mảng được gọi là **Rijndael’s S-box**. Mỗi byte có một phép biến đổi duy nhất, và một trạng thái mới của $S$ được tạo ra như một kết quả. Rijndael's S-box được hiển thị trong *Hình 3*.

*Hình 3: Rijndael's S-Box*

|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
Đây là một bảng mã hexa, thường được sử dụng trong lĩnh vực công nghệ thông tin và mật mã học để biểu diễn dữ liệu một cách rõ ràng và ngắn gọn. Mỗi cặp ký tự trong bảng biểu diễn một byte dữ liệu, với mỗi byte gồm 8 bit. Bảng này có thể được sử dụng trong nhiều tình huống khác nhau, bao gồm nhưng không giới hạn ở việc mã hóa, lập trình, và phân tích dữ liệu. Việc hiểu và biết cách sử dụng bảng mã hexa là một kỹ năng quan trọng trong nhiều ngành nghề liên quan đến công nghệ thông tin.
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |

Hộp S này là một ví dụ về việc đại số trừu tượng được áp dụng trong mã hóa Rijndael, cụ thể là **trường Galois**.

Để bắt đầu, bạn định nghĩa mỗi phần tử byte có thể có từ 00 đến FF là một vector 8-bit. Mỗi vector như vậy là một phần tử của **trường Galois GF(2^8)** nơi đa thức không thể giản lược cho phép toán modulo là $x^8 + x^4 + x^3 + x + 1$. Trường Galois với các thông số này còn được gọi là **Trường Hữu Hạn Rijndael**.

Tiếp theo, cho mỗi phần tử có thể có trong trường, chúng ta tạo ra cái được gọi là **Hộp S Nyberg**. Trong hộp này, mỗi byte được ánh xạ vào **nghịch đảo nhân của nó** (nghĩa là, sao cho tích của chúng bằng 1). Sau đó, chúng ta ánh xạ những giá trị đó từ Hộp S Nyberg sang Hộp S Rijndael sử dụng **biến đổi affine**.

Thao tác thứ ba trên mảng **S** là thao tác **dịch hàng**. Nó lấy trạng thái của **S** và liệt kê tất cả mười sáu byte trong một ma trận. Việc điền ma trận bắt đầu ở góc trên bên trái và tiếp tục bằng cách đi từ trên xuống dưới và sau đó, mỗi khi một cột được điền, dịch sang phải một cột và lên trên.

Một khi ma trận của **S** đã được xây dựng, bốn hàng được dịch chuyển. Hàng đầu tiên giữ nguyên. Hàng thứ hai dịch sang trái một vị trí. Hàng thứ ba dịch sang trái hai vị trí. Hàng thứ tư dịch sang trái ba vị trí. Một ví dụ về quy trình được cung cấp trong *Hình 4*. Trạng thái ban đầu của **S** được hiển thị ở trên, và trạng thái kết quả sau thao tác dịch hàng được hiển thị bên dưới.

*Hình 4: Thao tác dịch hàng*

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


Trong bước thứ tư, **trường Galois** lại xuất hiện một lần nữa. Để bắt đầu, mỗi cột của ma trận **S** được nhân với cột của ma trận 4 x 4 được thấy trong *Hình 5*. Nhưng thay vì là phép nhân ma trận thông thường, đây là phép nhân vector **theo modulo một đa thức không thể giản lược**, $x^8 + x^4 + x^3 + x + 1$. Các hệ số vector kết quả đại diện cho các bit riêng lẻ của một byte.

*Hình 5: Ma trận trộn cột*

| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   || 03   | 01   | 01   | 02   |

Phép nhân cột đầu tiên của ma trận **S** với ma trận 4 x 4 ở trên cho kết quả trong *Hình 6*.

*Hình 6: Phép nhân cột đầu tiên:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Bước tiếp theo, tất cả các số hạng trong ma trận sẽ được chuyển đổi thành đa thức. Ví dụ, F1 đại diện cho 1 byte và sẽ trở thành $x^7 + x^6 + x^5 + x^4 + 1$, và 03 đại diện cho 1 byte và sẽ trở thành $x + 1$.

Tất cả các phép nhân sau đó được thực hiện **modulo** $x^8 + x^4 + x^3 + x + 1$. Kết quả là việc cộng bốn đa thức trong mỗi ô của cột. Sau khi thực hiện các phép cộng này **modulo 2**, bạn sẽ thu được bốn đa thức. Mỗi đa thức này đại diện cho một chuỗi 8-bit, hay 1 byte, của **S**. Chúng tôi sẽ không thực hiện tất cả các phép tính này ở đây trên ma trận trong *Hình 6* vì chúng rất phức tạp.

Sau khi cột đầu tiên đã được xử lý, ba cột còn lại của ma trận **S** được xử lý theo cùng một cách. Cuối cùng, điều này sẽ tạo ra một ma trận với mười sáu byte có thể được chuyển đổi thành một mảng.

Bước cuối cùng, mảng **S** được kết hợp lại với khóa vòng một lần nữa trong một phép toán **XOR**. Điều này tạo ra trạng thái $S_1$. Đó là,

- $S_1 = S \oplus K_0$

### Vòng 2 đến 10

Các vòng từ 2 đến 9 chỉ là sự lặp lại của vòng 1, *mutatis mutandis*. Vòng cuối cùng trông rất giống với các vòng trước, ngoại trừ việc bước **mix columns** được loại bỏ. Đó là, vòng 10 được thực hiện như sau:

- $S_9 \oplus K_{10}$
- Thay thế Byte
- Dịch Hàng
- $S_{10} = S \oplus K_{10}$

Trạng thái $S_{10}$ bây giờ được thiết lập thành $C_1$, 128 bit đầu tiên của bản mã hóa. Tiếp tục với các khối bản rõ 128-bit còn lại cho ra bản mã hóa đầy đủ **C**.

### Các thao tác của mật mã Rijndael

Lý do đằng sau các thao tác khác nhau được thấy trong mật mã Rijndael là gì?

Mà không cần đi sâu vào chi tiết, các phương pháp mã hóa được đánh giá dựa trên mức độ chúng tạo ra sự nhầm lẫn và phân tán. Nếu phương pháp mã hóa có một mức độ **nhầm lẫn** cao, nghĩa là bản mã hóa trông rất khác so với bản rõ. Nếu phương pháp mã hóa có một mức độ **phân tán** cao, nghĩa là bất kỳ sự thay đổi nhỏ nào đối với bản rõ cũng tạo ra một bản mã hóa rất khác.
Lý do đằng sau các thao tác của mã hóa Rijndael là chúng tạo ra cả hai mức độ hỗn loạn và khuếch tán cao. Sự hỗn loạn được tạo ra bởi thao tác thay thế byte, trong khi khuếch tán được tạo ra bởi các thao tác dịch hàng và trộn cột.
# Mật mã Bất đối xứng
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Vấn đề phân phối và quản lý khóa
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Giống như mật mã đối xứng, các phương pháp bất đối xứng có thể được sử dụng để đảm bảo cả bí mật và xác thực. Tuy nhiên, điểm khác biệt là các phương pháp này sử dụng hai khóa thay vì một: một khóa riêng tư và một khóa công khai.

Chúng ta bắt đầu cuộc tìm hiểu với việc khám phá mật mã bất đối xứng, đặc biệt là các vấn đề đã thúc đẩy nó. Tiếp theo, chúng ta thảo luận về cách thức hoạt động ở mức độ cao của các phương pháp mã hóa và xác thực bất đối xứng. Sau đó, chúng ta giới thiệu về hàm băm, là chìa khóa để hiểu các phương pháp xác thực bất đối xứng, và cũng có liên quan trong các ngữ cảnh mật mã khác, như cho các mã xác thực tin nhắn dựa trên băm mà chúng ta đã thảo luận trong Chương 4.

___

Giả sử Bob muốn mua một chiếc áo mưa mới từ Jim’s Sporting Goods, một nhà bán lẻ đồ thể thao trực tuyến với hàng triệu khách hàng ở Bắc Mỹ. Đây sẽ là lần mua đầu tiên của anh ấy từ họ và anh ấy muốn sử dụng thẻ tín dụng của mình. Vì vậy, Bob sẽ cần phải tạo một tài khoản với Jim’s Sporting Goods, yêu cầu gửi qua các chi tiết cá nhân như địa chỉ và thông tin thẻ tín dụng của mình. Sau đó, anh ấy có thể thực hiện các bước cần thiết để mua chiếc áo mưa.

Bob và Jim’s Sporting Goods sẽ muốn đảm bảo rằng giao tiếp của họ an toàn trong suốt quá trình này, xem xét rằng Internet là một hệ thống giao tiếp mở. Ví dụ, họ sẽ muốn đảm bảo rằng không có kẻ tấn công tiềm năng nào có thể xác định được chi tiết thẻ tín dụng và địa chỉ của Bob, và không có kẻ tấn công tiềm năng nào có thể lặp lại việc mua hàng của anh ấy hoặc tạo ra những giao dịch giả mạo thay mặt anh ấy.

Một phương pháp mã hóa xác thực tiên tiến như đã thảo luận trong chương trước chắc chắn có thể làm cho giao tiếp giữa Bob và Jim’s Sporting Goods an toàn. Nhưng rõ ràng có những trở ngại thực tế để triển khai một phương pháp như vậy.

Để minh họa những trở ngại thực tế này, giả sử chúng ta sống trong một thế giới mà chỉ có các công cụ của mật mã đối xứng tồn tại. Jim’s Sporting Goods và Bob, sau đó, có thể làm gì để đảm bảo giao tiếp an toàn?

Trong những hoàn cảnh đó, họ sẽ phải đối mặt với chi phí đáng kể để giao tiếp một cách an toàn. Vì Internet là một hệ thống giao tiếp mở, họ không thể chỉ trao đổi một bộ khóa qua nó. Do đó, Bob và một đại diện cho Jim’s Sporting Goods sẽ cần phải thực hiện trao đổi khóa trực tiếp.

Một khả năng là Jim’s Sporting Goods tạo ra các địa điểm trao đổi khóa đặc biệt, nơi Bob và các khách hàng mới khác có thể nhận được một bộ khóa cho giao tiếp an toàn. Điều này rõ ràng sẽ tạo ra chi phí tổ chức đáng kể và giảm đáng kể hiệu quả mà khách hàng mới có thể thực hiện mua hàng.

Một cách khác, Jim’s Sporting Goods có thể gửi cho Bob một cặp khóa thông qua một dịch vụ chuyển phát tin cậy cao. Điều này có lẽ hiệu quả hơn việc tổ chức các địa điểm trao đổi khóa. Nhưng điều này vẫn sẽ tạo ra chi phí đáng kể, đặc biệt nếu nhiều khách hàng chỉ thực hiện một hoặc vài lần mua hàng.

Tiếp theo, một phương pháp mã hóa xác thực đối xứng cũng buộc Jim’s Sporting Goods phải lưu trữ các bộ khóa riêng biệt cho tất cả khách hàng của họ. Điều này sẽ là một thách thức thực tế đáng kể cho hàng nghìn khách hàng, chứ đừng nói đến hàng triệu.
Để hiểu điểm sau cùng này, giả sử rằng Jim’s Sporting Goods cung cấp cho mỗi khách hàng cùng một cặp chìa khóa. Điều này sẽ cho phép mỗi khách hàng - hoặc bất kỳ ai khác có thể lấy được cặp chìa khóa này - có thể đọc và thậm chí là thao túng tất cả các giao tiếp giữa Jim’s Sporting Goods và khách hàng của họ. Bạn có thể, sau đó, không cần sử dụng mã hóa trong giao tiếp của mình.

Ngay cả việc lặp lại một bộ chìa khóa cho chỉ một số khách hàng cũng là một thực hành an ninh tồi tệ. Bất kỳ kẻ tấn công tiềm năng nào cũng có thể cố gắng khai thác tính năng đó của hệ thống (nhớ rằng người tấn công được giả định biết mọi thứ về một hệ thống trừ chìa khóa, theo nguyên tắc Kerckhoffs.)

Vì vậy, Jim’s Sporting Goods sẽ phải lưu trữ một cặp chìa khóa cho mỗi khách hàng, bất kể cách phân phối các cặp chìa khóa này như thế nào. Điều này rõ ràng đặt ra một số vấn đề thực tế.

- Jim’s Sporting Goods sẽ phải lưu trữ hàng triệu cặp chìa khóa, một bộ cho mỗi khách hàng.
- Những chìa khóa này sẽ phải được bảo vệ một cách thích hợp, vì chúng sẽ là mục tiêu chắc chắn cho hacker. Bất kỳ sự vi phạm an ninh nào sẽ yêu cầu việc lặp lại việc trao đổi chìa khóa tốn kém, hoặc tại các địa điểm trao đổi chìa khóa đặc biệt hoặc qua dịch vụ chuyển phát.
- Bất kỳ khách hàng nào của Jim’s Sporting Goods cũng sẽ phải lưu trữ một cặp chìa khóa một cách an toàn tại nhà. Mất mát và trộm cắp sẽ xảy ra, yêu cầu việc lặp lại việc trao đổi chìa khóa. Khách hàng cũng sẽ phải trải qua quy trình này với bất kỳ cửa hàng trực tuyến nào hoặc các loại thực thể khác mà họ muốn giao tiếp và giao dịch qua Internet.

Hai thách thức chính vừa được mô tả là những mối quan tâm cơ bản cho đến cuối những năm 1970. Chúng được biết đến là **vấn đề phân phối chìa khóa** và **vấn đề quản lý chìa khóa**, tương ứng.

Những vấn đề này luôn tồn tại, tất nhiên, và thường gây đau đầu trong quá khứ. Ví dụ, lực lượng quân sự sẽ phải liên tục phân phối sách chứa chìa khóa cho giao tiếp an toàn cho nhân viên trên thực địa với rủi ro và chi phí lớn. Nhưng những vấn đề này trở nên tồi tệ hơn khi thế giới ngày càng chuyển sang giao tiếp kỹ thuật số từ xa, đặc biệt là cho các thực thể phi chính phủ.

Nếu những vấn đề này không được giải quyết vào những năm 1970, việc mua sắm hiệu quả và an toàn tại Jim’s Sporting Goods có lẽ sẽ không tồn tại. Thực tế, phần lớn thế giới hiện đại của chúng ta với việc gửi email thực tế và an toàn, ngân hàng trực tuyến, và mua sắm có lẽ chỉ là một giấc mơ xa vời. Bất cứ thứ gì giống như Bitcoin có lẽ sẽ không thể tồn tại.

Vậy, điều gì đã xảy ra vào những năm 1970? Làm thế nào chúng ta có thể mua sắm trực tuyến ngay lập tức và duyệt web thế giới một cách an toàn? Làm sao chúng ta có thể gửi Bitcoin tức thì khắp thế giới từ điện thoại thông minh của mình?

## Hướng mới trong mã hóa
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Vào những năm 1970, vấn đề phân phối chìa khóa và quản lý chìa khóa đã thu hút sự chú ý của một nhóm các nhà mã hóa học học thuật Mỹ: Whitfield Diffie, Martin Hellman, và Ralph Merkle. Trước sự hoài nghi nặng nề từ đa số đồng nghiệp của họ, họ đã mạo hiểm tìm ra giải pháp cho nó.

Ít nhất một động lực chính cho nỗ lực của họ là sự nhìn xa trông rộng rằng giao tiếp máy tính mở sẽ ảnh hưởng sâu sắc đến thế giới của chúng ta. Như Diffie và Hellman lưu ý vào năm 1976,
Sự phát triển của các mạng lưới giao tiếp điều khiển bởi máy tính hứa hẹn việc liên lạc không mất công sức và ít tốn kém giữa những người hoặc máy tính ở hai phía đối diện của thế giới, thay thế hầu hết thư từ và nhiều chuyến đi bằng việc giao tiếp từ xa. Đối với nhiều ứng dụng, các liên lạc này cần phải được bảo mật chống lại cả việc nghe lén và sự chèn vào của các tin nhắn không hợp lệ. Tuy nhiên, hiện nay, giải pháp cho các vấn đề an ninh lại tụt hậu so với các lĩnh vực khác của công nghệ giao tiếp. *Cryptography hiện đại không thể đáp ứng được các yêu cầu, bởi việc sử dụng nó sẽ gây ra những bất tiện nghiêm trọng cho người dùng hệ thống, đến mức loại bỏ nhiều lợi ích của việc xử lý từ xa.* [1]

Sự kiên trì của Diffie, Hellman và Merkle đã được đền đáp. Bài báo đầu tiên công bố kết quả của họ là một bài báo của Diffie và Hellman vào năm 1976 với tựa đề “New Directions in Cryptography.” Trong đó, họ đã trình bày hai cách tiếp cận mới để giải quyết vấn đề phân phối khóa và quản lý khóa.

Giải pháp đầu tiên họ đề xuất là một *giao thức trao đổi khóa từ xa*, tức là, một tập hợp các quy tắc cho việc trao đổi một hoặc nhiều khóa đối xứng qua một kênh giao tiếp không an toàn. Giao thức này hiện được biết đến với tên gọi *giao thức trao đổi khóa Diffie-Hellman* hoặc *giao thức trao đổi khóa Diffie-Hellman-Merkle*. [2]

Với giao thức trao đổi khóa Diffie-Hellman, hai bên trước tiên trao đổi một số thông tin một cách công khai trên một kênh không an toàn như Internet. Dựa trên thông tin đó, họ sau đó, độc lập tạo ra một khóa đối xứng (hoặc một cặp khóa đối xứng) cho việc giao tiếp an toàn. Mặc dù cả hai bên tạo ra khóa của mình một cách độc lập, thông tin họ chia sẻ công khai đảm bảo rằng quá trình tạo khóa này mang lại cùng một kết quả cho cả hai.

Quan trọng là, mặc dù mọi người có thể quan sát thông tin được trao đổi công khai bởi các bên qua kênh không an toàn, chỉ có hai bên tham gia vào việc trao đổi thông tin mới có thể tạo ra khóa đối xứng từ nó.

Điều này, tất nhiên, nghe có vẻ hoàn toàn trái với trực giác. Làm thế nào mà hai bên có thể trao đổi một số thông tin một cách công khai mà chỉ cho phép họ tạo ra khóa đối xứng từ nó? Tại sao bất kỳ ai khác quan sát việc trao đổi thông tin không thể tạo ra cùng một khóa?

Nó dựa vào một số toán học tuyệt đẹp, tất nhiên. Giao thức trao đổi khóa Diffie-Hellman hoạt động thông qua một hàm một chiều với một cửa hậu. Hãy thảo luận về ý nghĩa của hai thuật ngữ này lần lượt.

Giả sử bạn được cho một hàm $f(x)$ và kết quả $f(a) = y$, nơi $a$ là một giá trị cụ thể cho $x$. Chúng ta nói rằng $f(x)$ là một **hàm một chiều** nếu việc tính toán giá trị $y$ khi biết $a$ và $f(x)$ là dễ dàng, nhưng việc tính toán giá trị $a$ khi biết $y$ và $f(x)$ là không khả thi về mặt tính toán. Tên gọi **hàm một chiều**, tất nhiên, xuất phát từ thực tế là hàm này chỉ thực tế để tính toán theo một hướng.

Một số hàm một chiều có cái được biết đến là **cửa hậu**. Mặc dù việc tính toán $a$ chỉ từ $y$ và $f(x)$ là gần như không thể, có một mảnh thông tin $Z$ làm cho việc tính toán $a$ từ $y$ trở nên khả thi về mặt tính toán. Mảnh thông tin $Z$ này được biết đến là **cửa hậu**. Các hàm một chiều có cửa hậu được biết đến là **hàm cửa hậu**.
Chúng ta sẽ không đi sâu vào chi tiết của việc trao đổi khóa Diffie-Helmann ở đây. Nhưng cơ bản, mỗi bên tham gia tạo ra một số thông tin, một phần được chia sẻ công khai và một số khác được giữ bí mật. Sau đó, mỗi bên lấy phần thông tin bí mật của mình và thông tin công khai được chia sẻ bởi bên kia để tạo ra một khóa riêng tư. Và một cách kỳ diệu nào đó, cả hai bên sẽ kết thúc với cùng một khóa riêng tư.
Bất kỳ bên nào chỉ quan sát thông tin được chia sẻ công khai giữa hai bên trong việc trao đổi khóa Diffie Helmann đều không thể tái tạo các phép tính này. Họ sẽ cần thông tin riêng tư từ một trong hai bên để làm điều đó.

Mặc dù phiên bản cơ bản của việc trao đổi khóa Diffie-Helmann được trình bày trong bài báo năm 1976 không rất an toàn, nhưng các phiên bản phức tạp hơn của giao thức cơ bản chắc chắn vẫn được sử dụng ngày nay. Quan trọng nhất, mọi giao thức trao đổi khóa trong phiên bản mới nhất của giao thức bảo mật lớp vận chuyển (phiên bản 1.3) đều cơ bản là phiên bản được làm giàu của giao thức được trình bày bởi Diffie và Hellman vào năm 1976. Giao thức bảo mật lớp vận chuyển là giao thức chủ đạo để trao đổi thông tin một cách an toàn theo giao thức truyền tải siêu văn bản (http), tiêu chuẩn để trao đổi nội dung Web.

Quan trọng, việc trao đổi khóa Diffie-Helmann không phải là một kế hoạch không đối xứng. Nói một cách chính xác, nó có lẽ thuộc về lĩnh vực của mật mã khóa đối xứng. Nhưng vì cả việc trao đổi khóa Diffie-Helmann và mật mã không đối xứng đều dựa vào các hàm số học một chiều với cửa hậu, chúng thường được thảo luận cùng nhau.

Cách thứ hai mà Diffie và Helmann đề xuất để giải quyết vấn đề phân phối và quản lý khóa trong bài báo của họ năm 1976, tất nhiên, thông qua mật mã không đối xứng.

Trái ngược với việc trình bày của họ về việc trao đổi khóa Diffie-Hellman, họ chỉ cung cấp các đường nét chung về cách các kế hoạch mật mã không đối xứng có thể được xây dựng một cách hợp lý. Họ không cung cấp bất kỳ hàm một chiều nào có thể đáp ứng cụ thể các điều kiện cần thiết cho sự an toàn hợp lý trong các kế hoạch đó.

Tuy nhiên, một cách thực hiện thực tế của một kế hoạch không đối xứng đã được tìm thấy một năm sau đó bởi ba nhà mật mã học và toán học học thuật khác nhau: Ronald Rivest, Adi Shamir, và Leonard Adleman. Hệ mật mã mà họ giới thiệu đã được biết đến với tên là **hệ mật mã RSA** (theo tên họ của họ).

Các hàm cửa hậu được sử dụng trong mật mã không đối xứng (và việc trao đổi khóa Diffie Helmann) đều liên quan đến hai vấn đề **khó tính toán** chính: phân tích thừa số nguyên tố và tính toán logarit rời rạc.

**Phân tích thừa số nguyên tố** yêu cầu, như tên gọi, phân tích một số nguyên thành các thừa số nguyên tố của nó. Vấn đề RSA là ví dụ nổi tiếng nhất về một hệ mật mã liên quan đến phân tích thừa số nguyên tố.

Vấn đề **logarit rời rạc** là một vấn đề xảy ra trong các nhóm tuần hoàn. Cho một sinh viên trong một nhóm tuần hoàn cụ thể, nó yêu cầu tính toán số mũ duy nhất cần thiết để tạo ra một phần tử khác trong nhóm từ sinh viên.

Các kế hoạch dựa trên logarit rời rạc dựa vào hai loại nhóm tuần hoàn chính: nhóm nhân của các số nguyên và nhóm bao gồm các điểm trên các đường cong elliptic. Việc trao đổi khóa Diffie Helmann ban đầu như được trình bày trong "New Directions in Cryptography" hoạt động với một nhóm nhân tuần hoàn của các số nguyên. Thuật toán chữ ký số của Bitcoin và kế hoạch chữ ký Schnorr mới được giới thiệu (2021) đều dựa trên vấn đề logarit rời rạc cho một nhóm tuần hoàn đường cong elliptic cụ thể.

Tiếp theo, chúng ta sẽ chuyển sang cái nhìn tổng quan cấp cao về bí mật và xác thực trong bối cảnh không đối xứng. Tuy nhiên, trước khi làm vậy, chúng ta cần phải lưu ý một chút về lịch sử.
Giờ đây, có vẻ hợp lý khi cho rằng một nhóm các chuyên gia mật mã và toán học người Anh làm việc cho Cơ quan Truyền thông Chính phủ (GCHQ) đã độc lập phát hiện ra những điều được đề cập ở trên vài năm sớm hơn. Nhóm này gồm có James Ellis, Clifford Cocks và Malcolm Williamson.

Theo lời kể của họ và của GCHQ, James Ellis là người đầu tiên nghĩ ra khái niệm về mật mã khóa công khai vào năm 1969. Có vẻ như sau đó, Clifford Cocks đã phát hiện ra hệ thống mật mã RSA vào năm 1973, và Malcolm Williamson phát hiện ra khái niệm về trao đổi khóa Diffie-Hellman vào năm 1974. [4] Tuy nhiên, những phát hiện của họ được cho là không được tiết lộ cho đến năm 1997, do bản chất bí mật của công việc được thực hiện tại GCHQ.

**Ghi chú:**

[1] Whitfield Diffie và Martin Hellman, “New directions in cryptography,” _IEEE Transactions on Information Theory_ IT-22 (1976), tr. 644–654, tại tr. 644.

[2] Ralph Merkle cũng thảo luận về một giao thức trao đổi khóa trong “Secure communications over insecure channels”, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Mặc dù Merkle đã nộp bài này trước bài của Diffie và Hellman, nhưng nó được xuất bản sau. Giải pháp của Merkle không an toàn theo cấp số nhân, không giống như Diffie-Hellman.

[3] Ron Rivest, Adi Shamir, và Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, _Communications of the Association for Computing Machinery_, 21 (1978), tr. 120–26.

[4] Một lịch sử tốt về những phát hiện này được cung cấp bởi Simon Singh, _The Code Book_, Fourth Estate (London, 1999), Chương 6.

## Mã hóa và xác thực bất đối xứng
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Một cái nhìn tổng quan về **mã hóa bất đối xứng** với sự giúp đỡ của Bob và Alice được cung cấp trong *Hình 1*.

Alice đầu tiên tạo ra một cặp khóa, bao gồm một khóa công khai ($K_P$) và một khóa riêng tư ($K_S$), nơi “P” trong $K_P$ đại diện cho “public” (công khai) và “S” trong $K_S$ đại diện cho “secret” (bí mật). Sau đó, cô ấy phân phối khóa công khai này một cách tự do cho người khác. Chúng ta sẽ quay lại chi tiết của quá trình phân phối này một chút sau. Nhưng bây giờ, hãy giả định rằng bất kỳ ai, bao gồm cả Bob, cũng có thể an toàn nhận được khóa công khai $K_P$ của Alice.

Tại một thời điểm sau đó, Bob muốn viết một thông điệp $M$ cho Alice. Vì nó bao gồm thông tin nhạy cảm, anh ấy muốn nội dung này chỉ được bảo mật cho riêng Alice. Vì vậy, Bob đầu tiên mã hóa thông điệp $M$ của mình sử dụng $K_P$. Sau đó, anh ấy gửi bản mã hóa $C$ cho Alice, người giải mã $C$ bằng $K_S$ để tạo ra thông điệp gốc $M$.

*Hình 1: Mã hóa bất đối xứng*

![Hình 1: Mã hóa bất đối xứng](assets/Figure6-1.webp "Hình 1: Mã hóa bất đối xứng")

Bất kỳ kẻ tấn công nào nghe lén giao tiếp giữa Bob và Alice có thể quan sát $C$. Cô ấy cũng biết $K_P$ và thuật toán mã hóa $E(\cdot)$. Tuy nhiên, quan trọng là, thông tin này không cho phép kẻ tấn công có khả năng giải mã bản mã hóa $C$. Việc giải mã cụ thể yêu cầu $K_S$, mà kẻ tấn công không có.
Các phương pháp mã hóa đối xứng thường cần phải đảm bảo an toàn trước một kẻ tấn công có khả năng mã hóa hợp lệ các thông điệp văn bản (được biết đến như là bảo mật trước cuộc tấn công bằng văn bản đã chọn). Tuy nhiên, nó không được thiết kế với mục đích rõ ràng là cho phép việc tạo ra các văn bản mã hợp lệ bởi kẻ tấn công hoặc bất kỳ ai khác.
Điều này trái ngược hoàn toàn với một phương pháp mã hóa bất đối xứng, nơi mục đích chính của nó là cho phép bất kỳ ai, bao gồm cả kẻ tấn công, tạo ra các văn bản mã hợp lệ. Do đó, các phương pháp mã hóa bất đối xứng có thể được gọi là **mã truy cập nhiều lần**.

Để hiểu rõ hơn về điều gì đang xảy ra, hãy tưởng tượng thay vì gửi một thông điệp điện tử, Bob muốn gửi một bức thư vật lý trong bí mật. Một cách để đảm bảo bí mật sẽ là Alice gửi một ổ khóa an toàn cho Bob, nhưng giữ chìa khóa để mở nó. Sau khi viết thư, Bob có thể đặt bức thư vào một hộp và đóng nó lại với ổ khóa của Alice. Sau đó, anh có thể gửi hộp đã khóa với thông điệp đến Alice, người có chìa khóa để mở nó.

Mặc dù Bob có thể khóa ổ khóa, nhưng cả anh ta lẫn bất kỳ người nào khác chặn được hộp không thể mở ổ khóa nếu nó thực sự an toàn. Chỉ có Alice mới có thể mở nó và xem nội dung của bức thư của Bob vì cô ấy có chìa khóa.

Một phương pháp mã hóa bất đối xứng, nói một cách đơn giản, là phiên bản số hóa của quy trình này. Ổ khóa tương đương với khóa công khai và chìa khóa ổ khóa tương đương với khóa riêng tư. Tuy nhiên, vì ổ khóa là số hóa, nên việc Alice phân phối nó cho bất kỳ ai muốn gửi thông điệp bí mật cho cô ấy trở nên dễ dàng và không tốn kém.

Đối với xác thực trong bối cảnh bất đối xứng, chúng ta sử dụng **chữ ký số**. Do đó, chúng có chức năng giống như mã xác thực thông điệp trong bối cảnh đối xứng. Một cái nhìn tổng quan về chữ ký số được cung cấp trong *Hình 2*.

Bob đầu tiên tạo ra một cặp khóa, bao gồm khóa công khai ($K_P$) và khóa riêng tư ($K_S$), và phân phối khóa công khai của mình. Khi anh muốn gửi một thông điệp được xác thực cho Alice, anh trước tiên lấy thông điệp $M$ và khóa riêng tư của mình để tạo ra một **chữ ký số** $D$. Bob sau đó gửi cho Alice thông điệp của mình cùng với chữ ký số.

Alice chèn thông điệp, khóa công khai, và chữ ký số vào một **thuật toán xác minh**. Thuật toán này tạo ra hoặc là **true** cho một chữ ký hợp lệ, hoặc **false** cho một chữ ký không hợp lệ.

Một chữ ký số, như cái tên rõ ràng chỉ ra, là tương đương số hóa của một chữ ký viết tay trên thư, hợp đồng, và vân vân. Thực tế, một chữ ký số thường an toàn hơn nhiều. Với một chút nỗ lực, bạn có thể làm giả một chữ ký viết tay; quá trình này trở nên dễ dàng hơn do việc chữ ký viết tay thường không được kiểm tra kỹ lưỡng. Tuy nhiên, một chữ ký số an toàn, giống như một mã xác thực thông điệp an toàn, là **không thể giả mạo tồn tại**: tức là, với một phương pháp chữ ký số an toàn, không ai có thể khả thi tạo ra một chữ ký cho một thông điệp nào đó vượt qua quy trình xác minh, trừ khi họ có khóa riêng tư.

*Hình 2: Xác thực bất đối xứng*

![Hình 2: Xác thực bất đối xứng](assets/Figure6-2.webp "Hình 2: Xác thực bất đối xứng")

Giống như với mã hóa bất đối xứng, chúng ta thấy một sự tương phản thú vị giữa chữ ký số và mã xác thực thông điệp. Đối với cái sau, thuật toán xác minh chỉ có thể được sử dụng bởi một trong các bên tham gia vào giao tiếp an toàn. Điều này là do nó yêu cầu một khóa riêng tư. Tuy nhiên, trong bối cảnh bất đối xứng, bất kỳ ai cũng có thể xác minh một chữ ký số $S$ được tạo ra bởi Bob.
Tất cả những điều này làm cho chữ ký số trở thành một công cụ cực kỳ mạnh mẽ. Nó tạo nên cơ sở, ví dụ, để tạo chữ ký trên các hợp đồng có thể được xác minh cho mục đích pháp lý. Nếu Bob đã tạo một chữ ký trên một hợp đồng trong giao dịch trên, Alice có thể hiển thị thông điệp $M$, hợp đồng, và chữ ký $S$ cho tòa án. Sau đó, tòa án có thể xác minh chữ ký sử dụng khóa công khai của Bob. [5]
Ví dụ khác, chữ ký số là một khía cạnh quan trọng của việc phân phối phần mềm và cập nhật phần mềm an toàn. Loại khả năng xác minh công khai này không bao giờ có thể được tạo ra chỉ bằng cách sử dụng mã xác thực tin nhắn.

Là một ví dụ cuối cùng về sức mạnh của chữ ký số, hãy xem xét Bitcoin. Một trong những hiểu lầm phổ biến nhất về Bitcoin, đặc biệt là trong truyền thông, là rằng các giao dịch được mã hóa: chúng không phải vậy. Thay vào đó, giao dịch Bitcoin hoạt động với chữ ký số để đảm bảo an ninh.

Bitcoin tồn tại trong các lô gọi là đầu ra giao dịch chưa tiêu (hoặc **UTXO’s**). Giả sử bạn nhận được ba khoản thanh toán trên một địa chỉ Bitcoin cụ thể cho mỗi 2 bitcoin. Bạn kỹ thuật số không có 6 bitcoin trên địa chỉ đó. Thay vào đó, bạn có ba lô của 2 bitcoin được khóa bởi một vấn đề mật mã liên quan đến địa chỉ đó. Đối với bất kỳ khoản thanh toán nào bạn thực hiện, bạn có thể sử dụng một, hai, hoặc tất cả ba lô này, tùy thuộc vào số lượng bạn cần cho giao dịch.

Bằng chứng về quyền sở hữu đối với đầu ra giao dịch chưa tiêu thường được hiển thị qua một hoặc nhiều chữ ký số. Bitcoin hoạt động chính xác vì chữ ký số hợp lệ trên đầu ra giao dịch chưa tiêu là không thể tính toán được, trừ khi bạn sở hữu thông tin bí mật cần thiết để tạo chúng.

Hiện tại, giao dịch Bitcoin minh bạch bao gồm tất cả thông tin cần được xác minh bởi các bên tham gia trong mạng, như nguồn gốc của đầu ra giao dịch chưa tiêu được sử dụng trong giao dịch. Mặc dù có thể ẩn một số thông tin đó và vẫn cho phép xác minh (như một số tiền điện tử thay thế như Monero làm), điều này cũng tạo ra các rủi ro an ninh cụ thể.

Sự nhầm lẫn đôi khi phát sinh giữa chữ ký số và chữ ký viết được chụp lại một cách số hóa. Trong trường hợp sau, bạn chụp một hình ảnh của chữ ký viết của mình và dán nó vào một tài liệu điện tử như một hợp đồng lao động. Tuy nhiên, đây không phải là chữ ký số trong nghĩa mật mã học. Chữ ký số sau cùng chỉ là một con số dài chỉ có thể được tạo ra bằng cách sở hữu một khóa riêng.

Giống như trong cài đặt khóa đối xứng, bạn cũng có thể sử dụng mã hóa và các kế hoạch xác thực đối xứng cùng nhau. Các nguyên tắc tương tự áp dụng. Đầu tiên, bạn nên sử dụng các cặp khóa riêng công khai khác nhau cho việc mã hóa và tạo chữ ký số. Ngoài ra, bạn nên mã hóa một thông điệp và sau đó xác thực nó.

Quan trọng, trong nhiều ứng dụng, mật mã học đối xứng không được sử dụng xuyên suốt quá trình giao tiếp. Thay vào đó, nó thường chỉ được sử dụng để *trao đổi khóa đối xứng* giữa các bên mà họ sẽ thực sự giao tiếp.

Đây là trường hợp, ví dụ, khi bạn mua hàng trực tuyến. Biết khóa công khai của người bán, cô ấy có thể gửi cho bạn các thông điệp được ký số một cách số hóa mà bạn có thể xác minh tính xác thực của chúng. Trên cơ sở này, bạn có thể tuân theo một trong nhiều giao thức để trao đổi khóa đối xứng để giao tiếp một cách an toàn.

Lý do chính cho sự phổ biến của cách tiếp cận nêu trên là vì mật mã học đối xứng ít hiệu quả hơn nhiều so với mật mã học đối xứng trong việc tạo ra một mức độ an ninh cụ thể. Đây là một lý do tại sao chúng ta vẫn cần mật mã học khóa đối xứng bên cạnh mật mã học công khai. Ngoài ra, mật mã học khóa đối xứng tự nhiên hơn nhiều trong các ứng dụng cụ thể như một người dùng máy tính mã hóa dữ liệu của chính họ.

Vậy chữ ký số và mã hóa khóa công khai giải quyết vấn đề phân phối khóa và quản lý khóa như thế nào?
Không có một câu trả lời duy nhất ở đây. Mật mã bất đối xứng là một công cụ và không có một cách duy nhất để sử dụng công cụ đó. Nhưng hãy lấy ví dụ trước đây từ Jim’s Sporting Goods để cho thấy các vấn đề thường được giải quyết như thế nào trong ví dụ này.

Để bắt đầu, Jim’s Sporting Goods có lẽ sẽ tiếp cận một **cơ quan chứng nhận**, tổ chức hỗ trợ trong việc phân phối khóa công khai. Cơ quan chứng nhận sẽ đăng ký một số chi tiết về Jim’s Sporting Goods và cấp cho nó một khóa công khai. Sau đó, nó sẽ gửi cho Jim’s Sporting Goods một chứng chỉ, được biết đến là **chứng chỉ TLS/SSL**, với khóa công khai của Jim’s Sporting Goods được ký số bằng khóa công khai của chính cơ quan chứng nhận. Như vậy, cơ quan chứng nhận xác nhận rằng một khóa công khai cụ thể thực sự thuộc về Jim’s Sporting Goods.

Chìa khóa để hiểu quy trình này với các chứng chỉ TLS/SSL là, mặc dù bạn sẽ chung quy không có khóa công khai của Jim’s Sporting Goods được lưu trữ ở đâu trên máy tính của bạn, nhưng khóa công khai của các cơ quan chứng nhận được công nhận thực sự được lưu trữ trong trình duyệt hoặc hệ điều hành của bạn. Chúng được lưu trữ trong những gì được gọi là **chứng chỉ gốc**.

Do đó, khi Jim’s Sporting Goods cung cấp cho bạn chứng chỉ TLS/SSL của mình, bạn có thể xác minh chữ ký số của cơ quan chứng nhận qua một chứng chỉ gốc trong trình duyệt hoặc hệ điều hành của bạn. Nếu chữ ký là hợp lệ, bạn có thể tương đối chắc chắn rằng khóa công khai trên chứng chỉ thực sự thuộc về Jim’s Sporting Goods. Trên cơ sở này, việc thiết lập một giao thức giao tiếp an toàn với Jim’s Sporting Goods trở nên dễ dàng.

Việc phân phối khóa giờ đây đã trở nên vô cùng đơn giản cho Jim’s Sporting Goods. Không khó để thấy rằng quản lý khóa cũng đã trở nên đơn giản hóa rất nhiều. Thay vì phải lưu trữ hàng ngàn khóa, Jim’s Sporting Goods chỉ cần lưu trữ một khóa riêng tư cho phép nó tạo chữ ký cho khóa công khai trên chứng chỉ SSL của mình. Mỗi khi một khách hàng truy cập vào trang web của Jim’s Sporting Goods, họ có thể thiết lập một phiên giao tiếp an toàn từ khóa công khai này. Khách hàng cũng không cần lưu trữ bất kỳ thông tin nào (ngoại trừ khóa công khai của các cơ quan chứng nhận được công nhận trong hệ điều hành và trình duyệt của họ).

**Ghi chú:**

[5] Bất kỳ kế hoạch nào cố gắng đạt được không thể chối cãi, chủ đề khác mà chúng ta đã thảo luận trong Chương 1, sẽ cơ bản cần phải liên quan đến chữ ký số.

## Hàm băm

Hàm băm là một phần không thể thiếu trong mật mã. Chúng không phải là các kế hoạch đối xứng hay bất đối xứng, nhưng rơi vào một danh mục mật mã riêng biệt.

Chúng ta đã gặp hàm băm trong Chương 4 với việc tạo ra các thông điệp xác thực dựa trên băm. Chúng cũng quan trọng trong bối cảnh của chữ ký số, mặc dù vì một lý do hơi khác: Chữ ký số thường được tạo ra trên giá trị băm của một số (được mã hóa) thông điệp, thay vì chính (được mã hóa) thông điệp đó. Trong phần này, tôi sẽ giới thiệu kỹ hơn về hàm băm.

Hãy bắt đầu với việc định nghĩa một hàm băm. Một **hàm băm** là bất kỳ hàm nào có thể tính toán hiệu quả mà nhận đầu vào có kích thước tùy ý và cho ra kết quả có độ dài cố định.

Một **hàm băm mật mã** chỉ đơn giản là một hàm băm hữu ích cho các ứng dụng trong mật mã. Kết quả của một hàm băm mật mã thường được gọi là **băm**, **giá trị băm**, hoặc **tóm tắt thông điệp**.

Trong bối cảnh mật mã, một “hàm băm” thường đề cập đến một hàm băm mật mã. Tôi sẽ áp dụng thực hành đó từ đây trở đi.
Một ví dụ về hàm băm phổ biến là **SHA-256** (secure hash algorithm 256). Bất kể kích thước của đầu vào (ví dụ, 15 bit, 100 bit, hoặc 10,000 bit), hàm này sẽ tạo ra một giá trị băm 256-bit. Dưới đây bạn có thể thấy một vài ví dụ về kết quả của hàm SHA-256.
“Hello”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

“Cryptography is fun”: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Tất cả các kết quả đều chính xác là 256 bit được viết ra dưới dạng hệ thập lục phân (mỗi chữ số hệ thập lục phân có thể được biểu diễn bởi bốn chữ số nhị phân). Vì vậy, ngay cả khi bạn đã nhập toàn bộ cuốn sách *Chúa tể của những chiếc nhẫn* của Tolkien vào hàm SHA-256, kết quả vẫn sẽ là 256 bit.

Các hàm băm như SHA-256 được sử dụng cho nhiều mục đích trong mật mã học. Các tính chất cần thiết từ một hàm băm thực sự phụ thuộc vào bối cảnh của một ứng dụng cụ thể. Có hai tính chất chính thường được mong muốn từ các hàm băm trong mật mã học: [6]

1.	Kháng va chạm
2.	Ẩn giấu

Một hàm băm $H$ được cho là **kháng va chạm** nếu việc tìm hai giá trị, $x$ và $y$, sao cho $x \neq y$, nhưng $H(x) = H(y)$ là không khả thi.

Các hàm băm kháng va chạm quan trọng, ví dụ, trong việc xác minh phần mềm. Giả sử bạn muốn tải xuống phiên bản Windows của Bitcoin Core 0.21.0 (một ứng dụng máy chủ cho việc xử lý lưu lượng mạng Bitcoin). Các bước chính bạn cần thực hiện để xác minh tính hợp lệ của phần mềm, như sau:

1.	Bạn cần tải xuống và nhập khóa công khai của một hoặc nhiều người đóng góp Bitcoin Core vào phần mềm có thể xác minh chữ ký số (ví dụ: Kleopetra). Bạn có thể tìm thấy các khóa công khai này [tại đây](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Được khuyến nghị rằng bạn nên xác minh phần mềm Bitcoin Core với khóa công khai từ nhiều người đóng góp.
2.	Tiếp theo, bạn cần xác minh các khóa công khai mà bạn đã nhập. Ít nhất một bước bạn nên thực hiện là xác minh rằng các khóa công khai bạn tìm thấy giống như được công bố ở các vị trí khác nhau. Bạn có thể, ví dụ, tham khảo các trang web cá nhân, trang Twitter, hoặc trang Github của những người mà bạn đã nhập khóa công khai. Thông thường, việc so sánh này được thực hiện bằng cách so sánh một bản băm ngắn của khóa công khai được biết đến là dấu vân tay.
3.	Tiếp theo, bạn cần tải xuống tệp thực thi cho Bitcoin Core từ [website](www.bitcoincore.org) của họ. Sẽ có các gói phần mềm dành cho hệ điều hành Linux, Windows, và MAC.
4.	Tiếp theo, bạn phải tìm hai tệp phát hành. Tệp đầu tiên chứa bản băm SHA-256 chính thức cho tệp thực thi bạn đã tải xuống cùng với các bản băm cho tất cả các gói phần mềm khác được phát hành. Một tệp phát hành khác sẽ chứa các chữ ký từ nhiều người đóng góp trên tệp phát hành với các bản băm gói phần mềm. Cả hai tệp phát hành này nên được tìm thấy trên website của Bitcoin Core.
5. Tiếp theo, bạn cần tính toán giá trị băm SHA-256 của tệp thực thi mà bạn đã tải về từ trang web Bitcoin Core trên máy tính của mình. Sau đó, bạn so sánh kết quả này với giá trị băm chính thức của gói tệp thực thi. Chúng phải giống nhau.
6. Cuối cùng, bạn cần xác minh rằng một hoặc nhiều chữ ký số trên tệp phát hành với các giá trị băm chính thức của gói tệp thực sự tương ứng với một hoặc nhiều khóa công khai bạn đã nhập (các bản phát hành của Bitcoin Core không luôn được ký bởi tất cả mọi người). Bạn có thể làm điều này với một ứng dụng như Kleopetra.

Quy trình xác minh phần mềm này có hai lợi ích chính. Đầu tiên, nó đảm bảo rằng không có lỗi nào trong quá trình truyền tải khi tải về từ trang web của Bitcoin Core. Thứ hai, nó đảm bảo rằng không có kẻ tấn công nào có thể khiến bạn tải về mã độc hại đã được sửa đổi, bằng cách hack trang web Bitcoin Core hoặc bằng cách chặn lưu lượng truy cập.

Quy trình xác minh phần mềm trên bảo vệ chống lại những vấn đề này như thế nào?

Nếu bạn đã kiểm tra cẩn thận các khóa công khai bạn đã nhập, thì bạn có thể khá chắc chắn rằng những khóa này thực sự thuộc về họ và không bị xâm phạm. Vì chữ ký số có tính chất không thể giả mạo, bạn biết rằng chỉ những người đóng góp này mới có thể tạo ra chữ ký số trên các giá trị băm chính thức trên tệp phát hành.

Giả sử các chữ ký trên tệp phát hành bạn đã tải về được kiểm tra đúng. Bây giờ bạn có thể so sánh giá trị băm bạn đã tính toán tại chỗ cho tệp thực thi Windows bạn đã tải về với giá trị được bao gồm trong tệp phát hành đã được ký đúng. Như bạn biết, hàm băm SHA-256 có khả năng chống va chạm, một sự trùng khớp có nghĩa là tệp thực thi của bạn chính xác giống như tệp thực thi chính thức.

Bây giờ, chúng ta hãy chuyển sang tính chất thứ hai phổ biến của các hàm băm: **ẩn giấu**. Bất kỳ hàm băm $H$ nào được cho là có tính chất ẩn giấu nếu, cho bất kỳ $x$ nào được chọn ngẫu nhiên từ một phạm vi rất lớn, thì không thể tìm ra $x$ khi chỉ biết $H(x)$.

Dưới đây, bạn có thể thấy đầu ra SHA-256 của một thông điệp mà tôi đã viết. Để đảm bảo đủ tính ngẫu nhiên, thông điệp bao gồm một chuỗi ký tự được tạo ngẫu nhiên ở cuối. Vì SHA-256 có tính chất ẩn giấu, không ai có thể giải mã thông điệp này.

- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Nhưng tôi sẽ không để bạn chờ đợi cho đến khi SHA-256 trở nên yếu hơn. Thông điệp gốc mà tôi đã viết như sau:

* “Đây là một thông điệp rất ngẫu nhiên, hoặc cũng có thể nói là khá ngẫu nhiên. Phần đầu không phải, nhưng tôi sẽ kết thúc với một số ký tự tương đối ngẫu nhiên để đảm bảo một thông điệp không thể đoán trước được. XLWz4dVG3BxUWm7zQ9qS”.

Một cách phổ biến mà các hàm băm với tính chất ẩn giấu được sử dụng là trong quản lý mật khẩu (khả năng chống va chạm cũng quan trọng đối với ứng dụng này). Bất kỳ dịch vụ dựa trên tài khoản trực tuyến đáng tin cậy nào như Facebook hoặc Google sẽ không lưu trữ trực tiếp mật khẩu của bạn để quản lý quyền truy cập vào tài khoản của bạn. Thay vào đó, họ chỉ lưu trữ một giá trị băm của mật khẩu đó. Mỗi lần bạn nhập mật khẩu trên trình duyệt, một giá trị băm sẽ được tính toán trước. Chỉ có giá trị băm đó mới được gửi đến máy chủ của nhà cung cấp dịch vụ và so sánh với giá trị băm được lưu trữ trong cơ sở dữ liệu phía sau. Tính chất ẩn giấu có thể giúp đảm bảo rằng kẻ tấn công không thể khôi phục mật khẩu từ giá trị băm.
Quản lý mật khẩu thông qua băm chỉ hiệu quả nếu người dùng thực sự chọn mật khẩu khó. Tính chất ẩn giả định rằng x được chọn ngẫu nhiên từ một phạm vi rất lớn. Việc chọn mật khẩu như “1234”, “mypassword”, hoặc ngày sinh của bạn sẽ không mang lại bất kỳ sự bảo mật thực sự nào. Có những danh sách dài các mật khẩu phổ biến và băm của chúng tồn tại mà kẻ tấn công có thể tận dụng nếu họ có được băm của mật khẩu bạn. Các loại tấn công này được biết đến là **tấn công từ điển**. Nếu kẻ tấn công biết một số chi tiết cá nhân của bạn, họ cũng có thể thử một số đoán thông minh. Do đó, bạn luôn cần những mật khẩu dài, an toàn (tốt nhất là chuỗi ngẫu nhiên dài từ một trình quản lý mật khẩu).

Đôi khi một ứng dụng có thể cần một hàm băm có cả khả năng chống va chạm và ẩn. Nhưng chắc chắn không phải lúc nào cũng vậy. Quy trình xác minh phần mềm mà chúng ta đã thảo luận, ví dụ, chỉ yêu cầu hàm băm thể hiện khả năng chống va chạm, tính ẩn không quan trọng.

Mặc dù khả năng chống va chạm và ẩn là các tính chất chính được tìm kiếm của hàm băm trong mật mã học, trong một số ứng dụng, các loại tính chất khác cũng có thể được mong muốn.

**Ghi chú:**

[6] Thuật ngữ “ẩn” không phải là ngôn ngữ phổ thông, nhưng được lấy cụ thể từ Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, và Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Chương 1.

# Hệ mật mã RSA
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Vấn đề phân tích thừa số
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Trong khi mật mã đối xứng thường khá trực quan đối với hầu hết mọi người, thì điều này thường không đúng với mật mã bất đối xứng. Mặc dù bạn có thể thoải mái với mô tả cấp cao được cung cấp trong các phần trước, bạn có thể tự hỏi chính xác hàm một chiều là gì và chúng được sử dụng như thế nào để xây dựng các kế hoạch bất đối xứng.

Trong chương này, tôi sẽ làm sáng tỏ một số bí ẩn xung quanh mật mã bất đối xứng, bằng cách xem xét sâu hơn vào một ví dụ cụ thể, đó là hệ mật mã RSA. Trong phần đầu tiên, tôi sẽ giới thiệu về vấn đề phân tích thừa số mà vấn đề RSA dựa trên. Sau đó, tôi sẽ trình bày một số kết quả chính từ lý thuyết số. Trong phần cuối, chúng ta sẽ kết hợp thông tin này để giải thích vấn đề RSA, và làm thế nào nó có thể được sử dụng để tạo ra các kế hoạch mật mã bất đối xứng.

Việc thêm chiều sâu vào cuộc thảo luận này không phải là một nhiệm vụ dễ dàng. Nó đòi hỏi phải giới thiệu khá nhiều định lý và đề xuất lý thuyết số. Nhưng đừng để toán học làm bạn nản lòng. Làm việc qua cuộc thảo luận này sẽ cải thiện đáng kể sự hiểu biết của bạn về những gì nằm dưới mật mã bất đối xứng và là một khoản đầu tư đáng giá.

Bây giờ chúng ta hãy chuyển sang vấn đề phân tích thừa số.

___

Bất cứ khi nào bạn nhân hai số, giả sử $a$ và $b$, chúng ta gọi các số $a$ và $b$ là **thừa số**, và kết quả là **tích**. Cố gắng viết một số $N$ thành phép nhân của hai hoặc nhiều thừa số được gọi là **phân tích thừa số** hoặc **phân tích**. [1] Bạn có thể gọi bất kỳ vấn đề nào đòi hỏi điều này là một **vấn đề phân tích thừa số**.

Khoảng 2,500 năm trước, nhà toán học Hy Lạp Euclid của Alexandria đã phát hiện ra một định lý quan trọng về phân tích thừa số của các số nguyên. Nó thường được gọi là **định lý phân tích thừa số duy nhất** và tuyên bố như sau:

**Định lý 1**. Mọi số nguyên $N$ lớn hơn 1 đều là một số nguyên tố, hoặc có thể được biểu diễn dưới dạng tích của các thừa số nguyên tố.
Tất cả những gì phần sau của tuyên bố này có nghĩa là bạn có thể lấy bất kỳ số nguyên không nguyên tố $N$ lớn hơn 1, và viết nó dưới dạng tích của các số nguyên tố. Dưới đây là một số ví dụ về các số nguyên không nguyên tố được viết dưới dạng tích của các thừa số nguyên tố.
* $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
* $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
* $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Đối với cả ba số nguyên trên, việc tính toán các thừa số nguyên tố của chúng tương đối dễ dàng, ngay cả khi bạn chỉ được cho $N$. Bạn bắt đầu với số nguyên tố nhỏ nhất, cụ thể là 2, và xem số nguyên $N$ chia hết cho nó bao nhiêu lần. Sau đó, bạn chuyển sang kiểm tra tính chia hết của $N$ cho 3, 5, 7, và cứ thế tiếp tục. Bạn tiếp tục quá trình này cho đến khi số nguyên $N$ của bạn được viết dưới dạng tích của chỉ các số nguyên tố.

Lấy ví dụ, số nguyên 84. Dưới đây bạn có thể thấy quá trình xác định các thừa số nguyên tố của nó. Tại mỗi bước, chúng tôi lấy ra thừa số nguyên tố nhỏ nhất còn lại (ở bên trái) và xác định số dư cần được phân tích. Chúng tôi tiếp tục cho đến khi số dư cũng là một số nguyên tố. Tại mỗi bước, phân tích hiện tại của 84 được hiển thị ở phía xa bên phải.

* Thừa số nguyên tố = 2: số dư = 42 	($84 = 2 \cdot 42$)
* Thừa số nguyên tố = 2: số dư = 21 	($84 = 2 \cdot 2 \cdot 21$)
* Thừa số nguyên tố = 3: số dư = 7 	($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
* Vì 7 là một số nguyên tố, kết quả là $2 \cdot 2 \cdot 3 \cdot 7$, hoặc $2^2 \cdot 3 \cdot 7$.

Giả sử bây giờ $N$ rất lớn. Việc giảm $N$ thành các thừa số nguyên tố của nó sẽ khó khăn như thế nào?

Điều đó thực sự phụ thuộc vào $N$. Giả sử, ví dụ, $N$ là 50,450,400. Mặc dù con số này trông đáng sợ, nhưng các phép tính không quá phức tạp và có thể dễ dàng thực hiện bằng tay. Như trên, bạn chỉ cần bắt đầu với 2 và tiếp tục công việc. Dưới đây, bạn có thể thấy kết quả của quá trình này một cách tương tự như trên.

* 2: 25,225,200 	($50,450,400 = 2 \cdot 25,225,200$)  
* 2: 12,612,600 	($50,450,400 = 2^2 \cdot 12,612,600$)  
* 2: 6,306,300 	($50,450,400 = 2^3 \cdot 6,306,300$)  
* 2: 3,153,150 	($50,450,400 = 2^4 \cdot 3,153,150$)  
* 2: 1,576,575 	($50,450,400 = 2^5 \cdot 1,576,575$)
* 3: 525,525 ($50,450,400 = 2^5 \cdot 3 \cdot 525,525$)
* 3: 175,175 ($50,450,400 = 2^5 \cdot 3^2 \cdot 175,175$)
* 5: 35,035 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35,035$)
* 5: 7,007 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7,007$)
* 7: 1,001 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1,001$)
* 7: 143 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
* 11: 13 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
* Vì 13 là một số nguyên tố, kết quả là $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Việc giải quyết vấn đề này bằng tay mất một chút thời gian. Một máy tính, tất nhiên, có thể làm tất cả những điều này chỉ trong một phần nhỏ của giây. Thực tế, một máy tính thường có thể phân tích các số nguyên lớn cực kỳ nhanh chóng. 

Tuy nhiên, có một số ngoại lệ. Giả sử rằng chúng ta đầu tiên chọn ngẫu nhiên hai số nguyên tố lớn. Thông thường, chúng ta gọi chúng là $p$ và $q$, và tôi sẽ tuân theo quy ước đó ở đây.

Cụ thể, giả sử $p$ và $q$ đều là các số nguyên tố 1024-bit, và chúng thực sự cần ít nhất 1024 bit để được biểu diễn (vì vậy bit đầu tiên phải là 1). Vì vậy, ví dụ, 37 không thể là một trong những số nguyên tố đó. Bạn chắc chắn có thể biểu diễn 37 bằng 1024 bit. Nhưng rõ ràng *bạn không cần* nhiều bit như vậy để biểu diễn nó. Bạn có thể biểu diễn 37 bằng bất kỳ chuỗi nào có 6 bit trở lên. (Trong 6 bit, 37 sẽ được biểu diễn là $100101$).

Quan trọng là phải nhận thức được $p$ và $q$ lớn như thế nào nếu được chọn dưới các điều kiện trên. Là một ví dụ, tôi đã chọn một số nguyên tố ngẫu nhiên cần ít nhất 1024 bit để biểu diễn dưới đây.
Giả sử bây giờ sau khi chọn ngẫu nhiên các số nguyên tố $p$ và $q$, chúng ta nhân chúng lại với nhau để thu được một số nguyên $N$. Số nguyên này, do đó, là một số có 2048 bit yêu cầu ít nhất 2048 bit để biểu diễn. Nó lớn hơn nhiều so với $p$ hoặc $q$.

Giả sử bạn chỉ đưa cho máy tính $N$, và yêu cầu nó tìm hai yếu tố nguyên tố 1024 bit của $N$. Khả năng máy tính phát hiện ra $p$ và $q$ là cực kỳ nhỏ. Bạn có thể nói rằng nó là không thể cho mọi mục đích thực tế. Điều này vẫn đúng, ngay cả khi bạn sử dụng một siêu máy tính hoặc thậm chí là một mạng lưới các siêu máy tính.

Để bắt đầu, giả sử rằng máy tính cố gắng giải quyết vấn đề bằng cách lặp qua các số 1024 bit, kiểm tra trong mỗi trường hợp xem chúng có phải là số nguyên tố và nếu chúng là yếu tố của $N$. Tập hợp các số nguyên tố cần được kiểm tra sau đó là khoảng $1.265 \cdot 10^{305}$. [2]

Ngay cả khi bạn lấy tất cả các máy tính trên hành tinh và có chúng cố gắng tìm và kiểm tra các số nguyên tố 1024-bit theo cách này, một cơ hội một trong một tỷ để thành công tìm thấy một yếu tố nguyên tố của $N$ sẽ yêu cầu một khoảng thời gian tính toán dài hơn nhiều so với tuổi của Vũ trụ.

Bây giờ trên thực tế, một máy tính có thể làm tốt hơn quy trình thô sơ vừa được mô tả. Có một số thuật toán mà máy tính có thể áp dụng để đến với việc phân tích yếu tố nhanh hơn. Tuy nhiên, điểm quan trọng là, ngay cả khi sử dụng những thuật toán hiệu quả hơn này, nhiệm vụ của máy tính vẫn là không khả thi về mặt tính toán. [3]

Quan trọng, khó khăn của việc phân tích yếu tố dưới các điều kiện vừa được mô tả dựa trên giả định rằng không có thuật toán hiệu quả về mặt tính toán để tính toán các yếu tố nguyên tố. Chúng ta không thể chứng minh rằng một thuật toán hiệu quả không tồn tại. Tuy nhiên, giả định này là rất hợp lý: mặc dù đã có nhiều nỗ lực kéo dài hàng trăm năm, chúng ta vẫn chưa tìm thấy một thuật toán hiệu quả về mặt tính toán như vậy.

Do đó, vấn đề phân tích yếu tố, dưới một số hoàn cảnh, có thể được giả định là một vấn đề khó. Cụ thể, khi $p$ và $q$ là các số nguyên tố rất lớn, sản phẩm của chúng $N$ không khó để tính toán; nhưng phân tích yếu tố chỉ với $N$ là thực tế không thể.

**Ghi chú:**

[1] Phân tích yếu tố cũng có thể quan trọng khi làm việc với các loại đối tượng toán học khác ngoài số. Ví dụ, nó có thể hữu ích để phân tích các biểu thức đa thức như $x^2 - 2x + 1$. Trong cuộc thảo luận của chúng tôi, chúng tôi sẽ chỉ tập trung vào việc phân tích yếu tố của số, cụ thể là số nguyên.
[2] Theo **định lý số nguyên tố**, số lượng số nguyên tố nhỏ hơn hoặc bằng $N$ xấp xỉ $N/\ln(N)$. Điều này có nghĩa là bạn có thể ước lượng số lượng số nguyên tố có độ dài 1024 bit bằng cách:
$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...kết quả xấp xỉ là $1.265 \times 10^{305}$.

[3] Điều tương tự cũng đúng với các vấn đề logarithm rời rạc. Do đó, lý do tại sao các cấu trúc bất đối xứng sử dụng khóa lớn hơn nhiều so với các cấu trúc mật mã đối xứng.

## Kết quả lý thuyết số
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Thật không may, vấn đề phân tích thừa số không thể được sử dụng trực tiếp cho các lược đồ mật mã bất đối xứng. Tuy nhiên, chúng ta có thể sử dụng một vấn đề phức tạp hơn nhưng liên quan để đạt được hiệu quả này: vấn đề RSA.

Để hiểu vấn đề RSA, chúng ta cần hiểu một số định lý và đề xuất từ lý thuyết số. Những nội dung này được trình bày trong phần này qua ba tiểu mục: (1) thứ tự của N, (2) tính khả nghịch modulo N, và (3) định lý Euler.

Một số nội dung trong ba tiểu mục này đã được giới thiệu trong *Chương 3*. Nhưng tôi sẽ ở đây tái trình bày nội dung đó cho tiện lợi.

### Thứ tự của N

Một số nguyên $a$ là **coprime** hoặc **số nguyên tố cùng nhau** với một số nguyên $N$, nếu ước số chung lớn nhất giữa chúng là 1. Mặc dù theo quy ước số 1 không phải là số nguyên tố, nhưng nó là coprime của mọi số nguyên (cũng như $-1$).

Ví dụ, xem xét trường hợp khi $a = 18$ và $N = 37$. Rõ ràng chúng là coprimes. Số nguyên lớn nhất chia hết cho cả 18 và 37 là 1. Ngược lại, xem xét trường hợp khi $a = 42$ và $N = 16$. Rõ ràng chúng không phải là coprimes. Cả hai số đều chia hết cho 2, lớn hơn 1.

Bây giờ chúng ta có thể định nghĩa thứ tự của $N$ như sau. Giả sử $N$ là một số nguyên lớn hơn 1. **Thứ tự của N** là số lượng tất cả các coprimes với $N$ sao cho với mỗi coprime $a$, điều kiện sau được thỏa mãn: $1 \leq a < N$.

Ví dụ, nếu $N = 12$, thì 1, 5, 7, và 11 là những coprimes duy nhất đáp ứng yêu cầu trên. Do đó, thứ tự của 12 bằng 4.

Giả sử $N$ là một số nguyên tố. Khi đó bất kỳ số nguyên nào nhỏ hơn $N$ nhưng lớn hơn hoặc bằng 1 đều là coprime với nó. Điều này bao gồm tất cả các phần tử trong tập hợp sau: $\{1,2,3,….,N - 1\}$. Do đó, khi $N$ là số nguyên tố, thứ tự của $N$ là $N - 1$. Điều này được nêu trong đề xuất 1, nơi $\phi(N)$ biểu thị thứ tự của $N$.

**Đề xuất 1**. $\phi(N) = N - 1$ khi $N$ là số nguyên tố
Giả sử $N$ không phải là số nguyên tố. Bạn có thể, sau đó, tính toán bậc của nó sử dụng **Hàm Phi của Euler**. Trong khi việc tính toán bậc của một số nguyên nhỏ tương đối đơn giản, Hàm Phi của Euler trở nên đặc biệt quan trọng đối với các số nguyên lớn hơn. Đề xuất của Hàm Phi của Euler được trình bày dưới đây.

**Định lý 2**. Cho $N$ bằng $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, nơi tập hợp $\{p_i\}$ bao gồm tất cả các ước số nguyên tố phân biệt của $N$ và mỗi $e_i$ chỉ ra số lần ước số nguyên tố $p_i$ xuất hiện cho $N$. Khi đó,

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

**Định lý 2** cho thấy một khi bạn đã phân tích bất kỳ số $N$ không phải là số nguyên tố nào thành các ước số nguyên tố phân biệt của nó, việc tính toán bậc của $N$ trở nên dễ dàng.

Ví dụ, giả sử $N = 270$. Đây rõ ràng không phải là số nguyên tố. Phân tích $N$ thành các ước số nguyên tố của nó cho ra biểu thức: $2 \cdot 3^3 \cdot 5$. Theo Hàm Phi của Euler, bậc của $N$ sau đó như sau:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Giả sử tiếp theo rằng $N$ là tích của hai số nguyên tố, $p$ và $q$. **Định lý 2** ở trên, sau đó, tuyên bố rằng bậc của $N$ như sau:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

Đây là một kết quả chính cho vấn đề RSA nói riêng, và được trình bày trong **Đề xuất 2** dưới đây.

**Đề xuất 2**. Nếu $N$ là tích của hai số nguyên tố, $p$ và $q$, thì bậc của $N$ là tích $(p - 1) \cdot (q - 1)$.

Để minh họa, giả sử $N = 119$. Số nguyên này có thể được phân tích thành hai số nguyên tố, cụ thể là 7 và 17. Do đó, Hàm Phi của Euler gợi ý rằng bậc của 119 như sau:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

Nói cách khác, số nguyên 119 có 96 số nguyên tố cùng nhau trong phạm vi từ 1 đến 119. Thực tế, tập hợp này bao gồm tất cả các số nguyên từ 1 đến 119, không phải là bội số của 7 hoặc 17.
Từ đây, hãy ký hiệu tập hợp các số nguyên tố cùng nhau xác định thứ tự của $N$ là $C_N$. Đối với ví dụ của chúng ta khi $N = 119$, tập hợp $C_{119}$ quá lớn để liệt kê đầy đủ. Nhưng một số phần tử trong đó như sau:
$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Tính khả nghịch modulo N

Chúng ta có thể nói rằng một số nguyên $a$ là **khả nghịch modulo N**, nếu tồn tại ít nhất một số nguyên $b$ sao cho $a \cdot b \mod N = 1 \mod N$. Bất kỳ số nguyên $b$ nào như vậy được gọi là **nghịch đảo** (hoặc **nghịch đảo nhân**) của $a$ khi giảm theo modulo $N$.

Giả sử, ví dụ, $a = 5$ và $N = 11$. Có nhiều số nguyên mà bạn có thể nhân với 5, sao cho $5 \cdot b \mod 11 = 1 \mod 11$. Xem xét, ví dụ, các số nguyên 20 và 31. Dễ dàng thấy rằng cả hai số nguyên này đều là nghịch đảo của 5 khi giảm theo modulo 11.

* $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
* $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Mặc dù 5 có nhiều nghịch đảo khi giảm theo modulo 11, bạn có thể chứng minh rằng chỉ tồn tại một nghịch đảo dương duy nhất của 5 nhỏ hơn 11. Thực tế, điều này không chỉ đặc biệt cho ví dụ của chúng ta, mà là một kết quả chung.

**Đề xuất 3**. Nếu số nguyên $a$ là khả nghịch modulo $N$, thì phải có chính xác một nghịch đảo dương của $a$ nhỏ hơn $N$. (Vậy, nghịch đảo duy nhất này của $a$ phải đến từ tập hợp $\{1, \dots, N - 1\}$).

Hãy ký hiệu nghịch đảo duy nhất của $a$ từ **Đề xuất 3** là $a^{-1}$. Trong trường hợp khi $a = 5$ và $N = 11$, bạn có thể thấy $a^{-1} = 9$, vì $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Lưu ý rằng bạn cũng có thể thu được giá trị 9 cho $a^{-1}$ trong ví dụ của chúng ta bằng cách đơn giản là giảm bất kỳ nghịch đảo nào khác của $a$ theo modulo 11. Ví dụ, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Vì vậy, bất cứ khi nào một số nguyên $a > N$ là khả nghịch modulo $N$, thì $a \mod N$ cũng phải khả nghịch modulo $N$.

Không nhất thiết là một nghịch đảo của $a$ tồn tại khi giảm theo modulo $N$. Giả sử, ví dụ, $a = 2$ và $N = 8$. Không có $b$, hoặc cụ thể là bất kỳ $a^{-1}$ nào, sao cho $2 \cdot b \mod 8 = 1 \mod 8$. Điều này là bởi vì bất kỳ giá trị nào của $b$ luôn sản sinh ra một bội số của 2, vì vậy không có phép chia nào cho 8 có thể tạo ra một số dư bằng 1.
Làm thế nào chúng ta biết một số nguyên $a$ có nghịch đảo đối với một số $N$ cho trước? Như bạn có thể đã nhận thấy trong ví dụ ở trên, ước số chung lớn nhất giữa 2 và 8 lớn hơn 1, cụ thể là 2. Và điều này thực sự minh họa cho kết quả tổng quát sau đây:
**Định lý 4**. Một nghịch đảo của số nguyên $a$ tồn tại khi giảm modulo $N$, và cụ thể là một nghịch đảo dương duy nhất nhỏ hơn $N$, nếu và chỉ nếu ước số chung lớn nhất giữa $a$ và $N$ là 1 (nghĩa là, nếu chúng là hai số nguyên tố cùng nhau).

Trong trường hợp khi $a = 5$ và $N = 11$, chúng ta kết luận rằng $a^{-1} = 9$, vì $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Điều quan trọng cần lưu ý là điều ngược lại cũng đúng. Đó là, khi $a = 9$ và $N = 11$, thì $a^{-1} = 5$.

### Định lý Euler

Trước khi chuyển sang vấn đề RSA, chúng ta cần hiểu thêm một định lý quan trọng nữa, đó là **Định lý Euler**. Nó tuyên bố như sau:

**Định lý 3**. Giả sử hai số nguyên $a$ và $N$ là hai số nguyên tố cùng nhau. Khi đó, $a^{\phi(N)} \mod N = 1 \mod N$.

Đây là một kết quả đáng chú ý, nhưng hơi khó hiểu lúc đầu. Hãy xem xét một ví dụ để hiểu nó.

Giả sử $a = 5$ và $N = 7$. Đây thực sự là hai số nguyên tố cùng nhau như Định lý Euler yêu cầu. Chúng ta biết rằng thứ tự của 7 bằng 6, vì 7 là một số nguyên tố (xem **Định lý 1**).

Bây giờ, Định lý Euler tuyên bố rằng $5^6 \mod 7$ phải bằng $1 \mod 7$. Dưới đây là các phép tính để chứng minh điều này là đúng.

* $5^6 \mod 7 = 15,625 \mod 7 = 1 \mod N$

Số nguyên 7 chia hết cho 15,624 tổng cộng 2,233 lần. Do đó, phần dư của phép chia 16,625 cho 7 là 1.

Tiếp theo, sử dụng hàm Phi của Euler, **Định lý 2**, bạn có thể suy ra **Định lý 5** dưới đây.

**Định lý 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ đối với bất kỳ số nguyên dương $a$ và $b$ nào.

Chúng ta sẽ không chứng minh tại sao điều này là đúng. Nhưng chỉ cần lưu ý rằng bạn đã thấy bằng chứng của định lý này qua việc $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ khi $p$ và $q$ là các số nguyên tố, như được nêu trong **Định lý 2**.

Định lý Euler kết hợp với **Định lý 5** có những hàm ý quan trọng. Xem xét những gì xảy ra, ví dụ, trong các biểu thức dưới đây, nơi $a$ và $N$ là hai số nguyên tố cùng nhau.

* $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
* $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$* $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Như vậy, sự kết hợp của định lý Euler và **Đề xuất 5** cho phép chúng ta tính toán đơn giản một số biểu thức. Nói chung, chúng ta có thể tóm tắt hiểu biết như trong **Đề xuất 6**.

**Đề xuất 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Bây giờ chúng ta phải kết hợp mọi thứ lại trong một bước cuối cùng khéo léo.

Giống như $N$ có một thứ tự $\phi(N)$ bao gồm các phần tử của tập hợp $C_N$, chúng ta biết rằng số nguyên $\phi(N)$ phải lần lượt cũng có một thứ tự và một tập hợp các số nguyên tố cùng nhau. Hãy đặt $\phi(N) = R$. Sau đó, chúng ta biết rằng cũng có một giá trị cho $\phi(R)$ và một tập hợp các số nguyên tố cùng nhau $C_R$.

Giả sử rằng chúng ta bây giờ chọn một số nguyên $e$ từ tập hợp $C_R$. Chúng ta biết từ **Đề xuất 3** rằng số nguyên $e$ này chỉ có một nghịch đảo dương duy nhất nhỏ hơn $R$. Nghĩa là, $e$ có một nghịch đảo duy nhất từ tập hợp $C_R$. Hãy gọi nghịch đảo này là $d$. Dựa vào định nghĩa của một nghịch đảo, điều này có nghĩa là $e \cdot d = 1 \mod R$.

Chúng ta có thể sử dụng kết quả này để đưa ra một phát biểu về số nguyên gốc $N$ của chúng ta. Điều này được tóm tắt trong **Đề xuất 7**.

**Đề xuất 7**. Giả sử rằng $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Sau đó, đối với bất kỳ phần tử $a$ nào của tập hợp $C_N$, nó phải là trường hợp $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Bây giờ chúng ta đã có tất cả các kết quả lý thuyết số cần thiết để trình bày rõ ràng vấn đề RSA.


## Hệ mật mã RSA
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Chúng ta giờ đây đã sẵn sàng để trình bày vấn đề RSA. Giả sử bạn tạo ra một tập hợp các biến bao gồm $p$, $q$, $N$, $\phi(N)$, $e$, $d$, và $y$. Gọi tập hợp này là $\Pi$. Nó được tạo ra như sau:

1. Tạo ra hai số nguyên tố ngẫu nhiên $p$ và $q$ có kích thước bằng nhau và tính tích của chúng $N$.
2. Tính thứ tự của $N$, $\phi(N)$, bằng cách nhân sau: $(p - 1) \cdot (q - 1)$.
3. Chọn một $e > 2$ sao cho nó nhỏ hơn và nguyên tố cùng nhau với $\phi(N)$.
4. Tính $d$ bằng cách đặt $e \cdot d \mod \phi(N) = 1$.
5. Chọn một giá trị ngẫu nhiên $y$ nhỏ hơn và nguyên tố cùng nhau với $N$.
Vấn đề RSA bao gồm việc tìm một $x$ sao cho $x^e = y$, trong khi chỉ được cung cấp một tập hợp thông tin về $\Pi$, cụ thể là các biến $N$, $e$, và $y$. Khi $p$ và $q$ rất lớn, thường được khuyến nghị rằng chúng có kích thước 1024 bit, vấn đề RSA được cho là khó. Bạn có thể thấy tại sao đây là trường hợp dựa trên cuộc thảo luận trước đó.

Một cách dễ dàng để tính $x$ khi $x^e \mod N = y \mod N$ đơn giản chỉ bằng cách tính $y^d \mod N$. Chúng ta biết $y^d \mod N = x \mod N$ qua các phép tính sau:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Vấn đề là chúng ta không biết giá trị $d$, vì nó không được cung cấp trong vấn đề. Do đó, chúng ta không thể trực tiếp tính $y^d \mod N$ để tạo ra $x \mod N$.

Tuy nhiên, chúng ta có thể gián tiếp tính được $d$ từ thứ tự của $N$, $\phi(N)$, vì chúng ta biết rằng $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Nhưng theo giả định, vấn đề cũng không cung cấp giá trị cho $\phi(N)$.

Cuối cùng, thứ tự có thể được tính gián tiếp với các yếu tố nguyên tố $p$ và $q$, để chúng ta có thể cuối cùng tính được $d$. Nhưng theo giả định, các giá trị $p$ và $q$ cũng không được cung cấp cho chúng ta.

Nói một cách chính xác, ngay cả khi vấn đề phân tích trong một vấn đề RSA là khó, chúng ta không thể chứng minh rằng vấn đề RSA cũng khó. Có thể có những cách khác để giải quyết vấn đề RSA ngoài việc phân tích. Tuy nhiên, nói chung được chấp nhận và giả định rằng nếu vấn đề phân tích trong vấn đề RSA là khó, thì chính vấn đề RSA cũng khó.

Nếu vấn đề RSA thực sự khó, thì nó tạo ra một hàm một chiều với một cửa hậu. Hàm ở đây là $f(g) = g^e \mod N$. Với kiến thức về $f(g)$, bất kỳ ai cũng có thể dễ dàng tính được giá trị $y$ cho một $g = x$ cụ thể. Tuy nhiên, thực tế là không thể tính được giá trị $x$ cụ thể chỉ từ việc biết giá trị $y$ và hàm $f(g)$. Ngoại lệ là khi bạn được cung cấp một thông tin $d$, cửa hậu. Trong trường hợp đó, bạn có thể đơn giản tính $y^d$ để cho ra $x$.

Hãy đi qua một ví dụ cụ thể để minh họa vấn đề RSA. Tôi không thể chọn một vấn đề RSA được coi là khó dưới các điều kiện trên, vì các số sẽ không dễ quản lý. Thay vào đó, ví dụ này chỉ để minh họa cách vấn đề RSA hoạt động nói chung.

Để bắt đầu, giả sử bạn chọn hai số nguyên tố ngẫu nhiên là 13 và 31. Vậy $p = 13$ và $q = 31$. Tích $N$ của hai số nguyên tố này bằng 403. Chúng ta có thể dễ dàng tính thứ tự của 403. Nó tương đương với $(13 - 1) \cdot (31 - 1) = 360$.
Tiếp theo, như được chỉ đạo bởi bước 3 của bài toán RSA, chúng ta cần chọn một số nguyên tố cùng nhau với 360 lớn hơn 2 và nhỏ hơn 360. Chúng ta không cần phải chọn giá trị này một cách ngẫu nhiên. Giả sử rằng chúng ta chọn 103. Đây là một số nguyên tố cùng nhau với 360 vì ước chung lớn nhất của nó với 103 là 1.

Bước 4 yêu cầu chúng ta tính giá trị $d$ sao cho $103 \cdot d \mod 360 = 1$. Đây không phải là một nhiệm vụ dễ dàng khi thực hiện bằng tay khi giá trị của $N$ lớn. Điều này đòi hỏi chúng ta phải sử dụng một quy trình gọi là **thuật toán Euclid mở rộng**.

Mặc dù tôi không trình bày quy trình ở đây, nó cho kết quả là 7 khi $e = 103$. Bạn có thể xác minh rằng cặp giá trị 103 và 7 thực sự đáp ứng điều kiện chung $e \cdot d \mod \phi(n) = 1$ thông qua các phép tính dưới đây.

* $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Quan trọng là, dựa vào *Đề xuất 4*, chúng ta biết rằng không có số nguyên nào khác giữa 1 và 360 cho $d$ sẽ tạo ra kết quả $103 \cdot d = 1 \mod 360$. Ngoài ra, đề xuất này ngụ ý rằng việc chọn một giá trị khác cho $e$, sẽ tạo ra một giá trị duy nhất khác cho $d$.

Trong bước 5 của bài toán RSA, chúng ta phải chọn một số nguyên dương $y$ là một số nguyên tố cùng nhau nhỏ hơn của 403. Giả sử rằng chúng ta đặt $y = 2^{103}$. Phép lũy thừa của 2 với 103 cho kết quả dưới đây.

* $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$

Bài toán RSA trong ví dụ cụ thể này giờ đây như sau: Bạn được cung cấp $N = 403$, $e = 103$, và $y = 349 \mod 403$. Bây giờ bạn phải tính $x$ sao cho $x^{103} = 349 \mod 403$. Nghĩa là, bạn phải tìm ra giá trị ban đầu trước khi lũy thừa bởi 103 là 2.

Việc tính $x$ sẽ dễ dàng (ít nhất là đối với máy tính) nếu chúng ta biết $d = 7$. Trong trường hợp đó, bạn chỉ cần xác định $x$ như dưới đây.

* $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$

Vấn đề là bạn không được cung cấp thông tin rằng $d = 7$. Bạn có thể, tất nhiên, tính $d$ từ thực tế là $103 \cdot d = 1 \mod 360$. Vấn đề là bạn cũng không được cung cấp thông tin rằng thứ tự của $N = 360$. Cuối cùng, bạn cũng có thể tính thứ tự của 403 bằng cách tính sản phẩm sau: $(p - 1) \cdot (q - 1)$. Nhưng bạn cũng không được thông báo rằng $p = 13$ và $q = 31$.

Tất nhiên, một máy tính vẫn có thể giải quyết bài toán RSA cho ví dụ này một cách tương đối dễ dàng, bởi vì các số nguyên tố liên quan không lớn. Nhưng khi các số nguyên tố trở nên rất lớn, nó đối mặt với một nhiệm vụ gần như không thể.
Chúng tôi đã trình bày vấn đề RSA, một tập hợp các điều kiện khiến nó trở nên khó khăn, và toán học cơ bản đằng sau nó. Vậy, tất cả những điều này giúp ích như thế nào cho mật mã hóa không đối xứng? Cụ thể, làm thế nào chúng ta có thể biến độ khó của vấn đề RSA dưới một số điều kiện nhất định thành một phương thức mã hóa hoặc một phương thức chữ ký số?

Một cách tiếp cận là lấy vấn đề RSA và xây dựng các phương thức một cách trực tiếp. Ví dụ, giả sử bạn đã tạo ra một tập hợp các biến $\Pi$ như được mô tả trong vấn đề RSA, và đảm bảo rằng $p$ và $q$ đủ lớn. Bạn đặt khóa công khai của mình bằng $(N, e)$ và chia sẻ thông tin này với thế giới. Như đã mô tả ở trên, bạn giữ bí mật các giá trị của $p$, $q$, $\phi(n)$, và $d$. Thực tế, $d$ là khóa riêng của bạn.

Bất kỳ ai muốn gửi cho bạn một thông điệp $m$ là một phần tử của $C_N$ có thể đơn giản mã hóa nó như sau: $c = m^e \mod N$. (Bản mã $c$ ở đây tương đương với giá trị $y$ trong vấn đề RSA.) Bạn có thể dễ dàng giải mã thông điệp này chỉ bằng cách tính toán $c^d \mod N$.

Bạn cũng có thể cố gắng tạo ra một phương thức chữ ký số theo cùng một cách. Giả sử bạn muốn gửi cho ai đó một thông điệp $m$ với một chữ ký số $S$. Bạn chỉ cần đặt $S = m^d \mod N$ và gửi cặp $(m,S)$ cho người nhận. Bất kỳ ai cũng có thể xác minh chữ ký số chỉ bằng cách kiểm tra xem $S^e \mod N = m \mod N$ hay không. Tuy nhiên, bất kỳ kẻ tấn công nào cũng sẽ gặp khó khăn thực sự khi tạo ra một $S$ hợp lệ cho một thông điệp, vì họ không sở hữu $d$.

Thật không may, việc biến vấn đề RSA, một vấn đề khó khăn riêng biệt, thành một phương thức mật mã không phải là điều dễ dàng như vậy. Đối với phương thức mã hóa trực tiếp, bạn chỉ có thể chọn các số nguyên tố cùng nhau của $N$ làm thông điệp của mình. Điều này không để lại cho chúng ta nhiều thông điệp có thể, chắc chắn không đủ cho giao tiếp tiêu chuẩn. Ngoài ra, những thông điệp này phải được chọn một cách ngẫu nhiên. Điều này có vẻ khá bất tiện. Cuối cùng, bất kỳ thông điệp nào được chọn hai lần sẽ tạo ra cùng một bản mã. Điều này cực kỳ không mong muốn trong bất kỳ phương thức mã hóa nào và không đáp ứng bất kỳ tiêu chuẩn an ninh mật mã hiện đại nghiêm ngặt nào.

Vấn đề càng trở nên tồi tệ hơn đối với phương thức chữ ký số trực tiếp của chúng tôi. Như hiện tại, bất kỳ kẻ tấn công nào cũng có thể dễ dàng làm giả chữ ký số chỉ bằng cách trước tiên chọn một số nguyên tố cùng nhau của $N$ làm chữ ký và sau đó tính toán thông điệp gốc tương ứng. Điều này rõ ràng phá vỡ yêu cầu về khả năng không thể giả mạo tồn tại.

Tuy nhiên, với việc thêm một chút phức tạp thông minh, vấn đề RSA có thể được sử dụng để tạo ra một phương thức mã hóa khóa công khai an toàn cũng như một phương thức chữ ký số an toàn. Chúng tôi sẽ không đi vào chi tiết của những cấu trúc như vậy ở đây. [4] Quan trọng là, tuy nhiên, sự phức tạp bổ sung này không thay đổi vấn đề RSA cơ bản mà các phương thức này dựa trên.

**Ghi chú:**

[4] Xem, ví dụ, Jonathan Katz và Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), trang 410–32 về mã hóa RSA và trang 444–41 cho chữ ký số RSA.

## Đánh giá khóa học
<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>
<isCourseReview>true</isCourseReview>