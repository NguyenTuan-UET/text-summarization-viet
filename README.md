# 🇻🇳 TextRank - Tóm Tắt Văn Bản Tiếng Việt

Công cụ tóm tắt văn bản và trích xuất từ khóa tự động cho tiếng Việt, sử dụng thuật toán TextRank + VnCoreNLP.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)

---

## Tính Năng

- **Tóm tắt tự động** - 4+ phương thức tóm tắt
- **VnCoreNLP** - Tách từ tiếng Việt chính xác
- **Tùy chỉnh linh hoạt** - Điều chỉnh số câu, từ khóa
- **Stopwords** - Lọc 1,942 stop words tiếng Việt

---

## Cài Đặt (4 Bước)

```bash
# 1. Clone
git clone https://github.com/NguyenTuan-UET/text-summarization-viet.git
cd text-summarization-viet

# 2. Tạo venv
python3 -m venv venv
source venv/bin/activate

# 3. Cài dependencies
pip install -r requirements.txt

# 4. Chạy demo
python3 demo_vncorenlp.py
```

---

## 📖 Sử Dụng

### Bước 1: Khởi tạo
```python
from textrank_facade import TextRankFacade
from stopwords.vietnamese import Vietnamese
from py_vncorenlp import VnCoreNLP

# Khởi tạo VnCoreNLP
vncorenlp = VnCoreNLP(annotators=["wseg"], save_dir="./vncorenlp")

# Khởi tạo TextRank Facade
tr = TextRankFacade(vncorenlp, Vietnamese())
```

### Bước 2: Chuẩn bị văn bản
```python
text = """
Trí tuệ nhân tạo đang phát triển rất nhanh trong những năm gần đây.
Nhiều doanh nghiệp Việt Nam bắt đầu ứng dụng AI vào sản xuất và kinh doanh.
Các hệ thống gợi ý giúp cải thiện trải nghiệm người dùng trên nền tảng số.
Trong lĩnh vực giáo dục, AI được dùng để cá nhân hóa việc học tập.
Sinh viên công nghệ thông tin cần trang bị kiến thức nền tảng về dữ liệu.
Việc hiểu rõ thuật toán giúp lập trình viên tối ưu hệ thống tốt hơn.
"""
```

---

### Bước 3: Chọn phương thức tóm tắt

#### **Phương thức 1: `summarize()` - Tự động (KHUYẾN NGHỊ)**

```python
# Logic: ≤5 câu → max 3 câu, >5 câu → 40% min 5 câu
summary = tr.summarize(text)

print("TÓM TẮT TỰ ĐỘNG:")
for i, sentence in enumerate(summary, 1):
    print(f"{i}. {sentence}")
```

**Output:**
```
1. Nhiều doanh nghiệp Việt Nam bắt đầu ứng dụng AI vào sản xuất và kinh doanh.
2. Các hệ thống gợi ý giúp cải thiện trải nghiệm người dùng trên nền tảng số.
3. Việc hiểu rõ thuật toán giúp lập trình viên tối ưu hệ thống tốt hơn.
```

---

#### **Phương thức 2: `get_highlights()` - Highlights**

```python
# Lấy 15-25% câu quan trọng (min 2, max 6 câu)
highlights = tr.get_highlights(text)

print("HIGHLIGHTS:")
for i, sentence in enumerate(highlights, 1):
    print(f"{i}. {sentence}")
```

**Output:**
```
1. Nhiều doanh nghiệp Việt Nam bắt đầu ứng dụng AI vào sản xuất và kinh doanh.
2. Sinh viên công nghệ thông tin cần trang bị kiến thức nền tảng về dữ liệu.
```

---

#### **Phương thức 3: `summarize_text_compound()` - 3 câu quan trọng nhất**

```python
# Luôn trả về 3 câu, không theo thứ tự gốc
summary = tr.summarize_text_compound(text)

print("TOP 3 CÂU QUAN TRỌNG:")
for i, sentence in enumerate(summary, 1):
    print(f"{i}. {sentence}")
```

**Output:**
```
1. Các hệ thống gợi ý giúp cải thiện trải nghiệm người dùng trên nền tảng số.
2. Việc hiểu rõ thuật toán giúp lập trình viên tối ưu hệ thống tốt hơn.
3. Nhiều doanh nghiệp Việt Nam bắt đầu ứng dụng AI vào sản xuất và kinh doanh.
```

---

#### **Phương thức 4: `summarize_text_freely()` - Tùy chỉnh**

```python
# Tùy chỉnh: 5 từ khóa, 2 câu output
summary = tr.summarize_text_freely(
    text,
    analyzed_keywords=5,      # Số từ khóa để phân tích
    expected_sentences=2,     # Số câu muốn lấy
    summarize_type=TextRankFacade.GET_ALL_IMPORTANT  # Kiểu tóm tắt
)

print("⚙️ TÓM TẮT TÙY CHỈNH (5 keywords → 2 câu):")
for i, sentence in enumerate(summary, 1):
    print(f"{i}. {sentence}")
```

**Output:**
```
⚙️ TÓM TẮT TÙY CHỈNH (5 keywords → 2 câu):
1. Các hệ thống gợi ý giúp cải thiện trải nghiệm người dùng trên nền tảng số.
2. Việc hiểu rõ thuật toán giúp lập trình viên tối ưu hệ thống tốt hơn.
```

**Kiểu tóm tắt:**
- `GET_ALL_IMPORTANT` (0): Lấy câu quan trọng nhất, giữ thứ tự gốc
- `GET_FIRST_IMPORTANT_AND_FOLLOWINGS` (1): Lấy câu quan trọng + các câu theo sau

---

### Bước 4: Trích xuất từ khóa

```python
keywords = tr.get_only_keywords(text)

print("🔑 TOP 10 KEYWORDS:")
for rank, (word, score) in enumerate(list(keywords.items())[:10], 1):
    print(f"{rank:2d}. {word:<25s} {score:.4f}")
```

**Output:**
```
🔑 TOP 10 KEYWORDS:
 1. giúp                      1.0000
 2. gợi_ý                     0.8333
 3. cải_thiện                 0.8333
 4. lập_trình_viên            0.8333  ← Từ ghép được giữ nguyên!
 5. trải_nghiệm               0.6667
 6. nền_tảng                  0.6667
 7. kiến_thức                 0.6667
 8. doanh_nghiệp              0.5000
 9. việt_nam                  0.5000
10. bắt_đầu                   0.5000
```

💡 **Chú ý:** VnCoreNLP giữ nguyên từ ghép như `lập_trình_viên`, `công_nghệ_thông_tin` → Chính xác hơn nhiều!

---

## Các Phương Thức

| Method | Output | Use case |
|--------|--------|----------|
| `summarize()` | Tự động | ⭐ Khuyến nghị |
| `get_highlights()` | 15-25% câu | Văn bản dài |
| `summarize_text_compound()` | 3 câu | So sánh |
| `summarize_text_freely()` | Tùy chỉnh | Research |

---

## 📚 Tài Liệu

- [QUICKSTART.md](QUICKSTART.md) - 3 bước
- [HOW_TO_RUN.md](HOW_TO_RUN.md) - Chi tiết
- [CHANGELOG.md](CHANGELOG.md) - Lịch sử

---

## 🙏 Credits

- VnCoreNLP - VNU UET
- TextRank - Mihalcea & Tarau
- Stopwords - Community

**Made with ❤️ for Vietnamese NLP**
