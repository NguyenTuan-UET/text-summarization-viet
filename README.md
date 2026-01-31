# TextRank - Tóm Tắt Văn Bản Tiếng Việt

Công cụ tóm tắt văn bản và trích xuất từ khóa tự động cho tiếng Việt sử dụng thuật toán **TextRank**.

## Tính Năng

- **Trích xuất từ khóa** - Tìm các từ quan trọng nhất trong văn bản
- **Tóm tắt văn bản** - Lựa chọn câu quan trọng nhất tự động
- **Tùy chỉnh linh hoạt** - Điều chỉnh số câu, từ khóa theo nhu cầu
- **Hỗ trợ tiếng Việt** - Sử dụng 1,942 stop words tiếng Việt
- **Không cần thư viện ngoài** - Chỉ dùng Python standard library

## Cài Đặt và Chạy

### Yêu cầu

- Python 3.7 trở lên
- Không cần cài đặt thư viện ngoài

### Chạy demo nhanh

```bash
cd python_version
python3 quick_start.py
```

## Hướng Dẫn Sử Dụng

### 1. Sử dụng cơ bản

```python
from textrank_facade import TextRankFacade
from stopwords.vietnamese import Vietnamese

# Khởi tạo
tr = TextRankFacade()
tr.set_stop_words(Vietnamese())

# Văn bản cần tóm tắt
text = """
Việt Nam là một quốc gia nằm ở phía đông của bán đảo Đông Dương.
Việt Nam có diện tích khoảng 331.000 km² và dân số hơn 97 triệu người.
Thủ đô của Việt Nam là Hà Nội. Thành phố lớn nhất là TP Hồ Chí Minh.
"""

# Tóm tắt văn bản (3 câu quan trọng nhất)
summary = tr.summarize_text_compound(text)
for sentence in summary:
    print(sentence)
```

### 3. Các phương thức tóm tắt

#### a) `summarize_text_basic()` - Tóm tắt cơ bản
Lấy câu quan trọng nhất + các câu kế tiếp

```python
summary = tr.summarize_text_basic(text)
```

#### b) `summarize_text_compound()` - Tóm tắt 3 câu
Lấy 3 câu quan trọng nhất (không theo thứ tự gốc)

```python
summary = tr.summarize_text_compound(text)
```

#### c) `get_highlights()` - Lấy 20% câu quan trọng
Tự động lấy 20% số câu quan trọng nhất

```python
highlights = tr.get_highlights(text)
```

#### d) `summarize_text_freely()` - Tùy chỉnh hoàn toàn
Tự do điều chỉnh tham số

```python
summary = tr.summarize_text_freely(
    text,
    analyzed_keywords=5,      # Số từ khóa phân tích
    expected_sentences=2,     # Số câu cần lấy
    summarize_type=TextRankFacade.GET_ALL_IMPORTANT
)
```

**Các kiểu tóm tắt:**
- `TextRankFacade.GET_ALL_IMPORTANT` - Lấy các câu quan trọng nhất
- `TextRankFacade.GET_FIRST_IMPORTANT_AND_FOLLOWINGS` - Lấy câu quan trọng nhất + các câu sau

## Thuật Toán TextRank

TextRank là thuật toán dựa trên **PageRank** (Google) để xếp hạng các từ/câu trong văn bản:

1. **Parse văn bản** → Tách thành câu và từ
2. **Tạo đồ thị** → Mỗi từ là một node, kết nối với từ trước/sau
3. **Tính điểm** → Dùng thuật toán TextRank để tính trọng số
4. **Chọn câu** → Lấy câu chứa từ có điểm cao nhất

### Ưu điểm
- Không cần training data
- Không phụ thuộc ngôn ngữ (chỉ cần stop words)
- Nhanh và hiệu quả
- Kết quả ổn định

## Credits

- Thuật toán TextRank: Mihalcea & Tarau (2004)
- Vietnamese stop words: Tổng hợp từ nhiều nguồn

---