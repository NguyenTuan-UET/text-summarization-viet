"""
Quick Start Guide - Vietnamese Text Summarization

Hướng dẫn nhanh cách sử dụng TextRank để tóm tắt văn bản tiếng Việt
"""

from textrank_facade import TextRankFacade
from stopwords.vietnamese import Vietnamese


def example_basic():
    """Ví dụ cơ bản nhất"""
    print("=" * 60)
    print("VÍ DỤ CƠ BẢN")
    print("=" * 60)
    
    # Văn bản ngắn để test
    text = """
    Việt Nam là một quốc gia nằm ở phía đông của bán đảo Đông Dương. 
    Việt Nam có diện tích khoảng 331.000 km² và dân số hơn 97 triệu người.
    Thủ đô của Việt Nam là Hà Nội. Thành phố lớn nhất là Thành phố Hồ Chí Minh.
    Việt Nam có nền kinh tế đang phát triển nhanh. Việt Nam là thành viên của ASEAN.
    """
    
    # Khởi tạo
    tr = TextRankFacade()
    tr.set_stop_words(Vietnamese())
    
    # Tóm tắt
    summary = tr.summarize_text_compound(text)
    
    print("\nVĂN BẢN GỐC:")
    print(text.strip())
    print("\nTÓM TẮT (3 câu quan trọng nhất):")
    for i, sentence in enumerate(summary, 1):
        print(f"{i}. {sentence}")
    print()


def example_keywords():
    """Ví dụ trích xuất từ khóa"""
    print("=" * 60)
    print("VÍ DỤ TRÍCH XUẤT TỪ KHÓA")
    print("=" * 60)
    
    text = """
    Trí tuệ nhân tạo đang thay đổi thế giới. Machine learning và deep learning
    là những công nghệ quan trọng trong AI. Python là ngôn ngữ phổ biến nhất
    để phát triển AI. TensorFlow và PyTorch là các framework mạnh mẽ.
    """
    
    tr = TextRankFacade()
    tr.set_stop_words(Vietnamese())
    
    keywords = tr.get_only_keywords(text)
    
    print("\nTOP 10 TỪ KHÓA:")
    for i, (word, score) in enumerate(list(keywords.items())[:10], 1):
        print(f"{i:2d}. {word:15s} (điểm: {score:.3f})")
    print()


def example_custom():
    """Ví dụ tùy chỉnh tham số"""
    print("=" * 60)
    print("VÍ DỤ TÙY CHỈNH")
    print("=" * 60)
    
    text = """
    Covid-19 là đại dịch toàn cầu gây ra bởi virus SARS-CoV-2.
    Đại dịch bắt đầu từ cuối năm 2019 tại Trung Quốc.
    Virus lây lan nhanh chóng ra toàn thế giới.
    Nhiều quốc gia phải thực hiện giãn cách xã hội.
    Vaccine đã được phát triển để ngăn chặn đại dịch.
    Người dân cần đeo khẩu trang và rửa tay thường xuyên.
    """
    
    tr = TextRankFacade()
    tr.set_stop_words(Vietnamese())
    
    # Tùy chỉnh: 3 từ khóa, 2 câu
    summary = tr.summarize_text_freely(
        text,
        analyzed_keywords=3,
        expected_sentences=2,
        summarize_type=TextRankFacade.GET_ALL_IMPORTANT
    )
    
    print("\nTÓM TẮT (sử dụng 3 từ khóa, lấy 2 câu):")
    for i, sentence in enumerate(summary, 1):
        print(f"{i}. {sentence}")
    print()


def example_compare_methods():
    """So sánh các phương thức tóm tắt"""
    print("=" * 60)
    print("SO SÁNH CÁC PHƯƠNG THỨC TÓM TẮT")
    print("=" * 60)
    
    text = """
    Đại học Bách khoa Hà Nội là một trong những trường đại học hàng đầu Việt Nam.
    Trường được thành lập năm 1956. Trường đào tạo nhiều ngành kỹ thuật.
    Sinh viên Bách Khoa được đào tạo chất lượng cao. 
    Nhiều cựu sinh viên thành công trong sự nghiệp.
    Trường có nhiều phòng thí nghiệm hiện đại.
    """
    
    tr = TextRankFacade()
    tr.set_stop_words(Vietnamese())
    
    print("\nVĂN BẢN GỐC:")
    print(text.strip())
    
    print("\n1. PHƯƠNG THỨC: summarize_text_basic()")
    print("   (Câu quan trọng nhất + các câu tiếp theo)")
    basic = tr.summarize_text_basic(text)
    for sentence in basic:
        print(f"   - {sentence}")
    
    print("\n2. PHƯƠNG THỨC: summarize_text_compound()")
    print("   (3 câu quan trọng nhất, không theo thứ tự)")
    compound = tr.summarize_text_compound(text)
    for sentence in compound:
        print(f"   - {sentence}")
    
    print("\n3. PHƯƠNG THỨC: get_highlights()")
    print("   (20% câu quan trọng nhất)")
    highlights = tr.get_highlights(text)
    for sentence in highlights:
        print(f"   - {sentence}")
    print()


if __name__ == "__main__":
    example_basic()
    example_keywords()
    example_custom()
    example_compare_methods()
    
    print("=" * 60)
    print("ĐỌC README.md ĐỂ BIẾT THÊM CHI TIẾT!")
    print("=" * 60)
