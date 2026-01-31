# Class Facade cho thuật toán tóm tắt văn bản TextRank

from typing import List, Dict, Optional
from tools.parser import Parser
from tools.graph import Graph
from tools.score import Score
from tools.summarize import Summarize
from tools.text import Text
from stopwords.vietnamese import Vietnamese


class TextRankFacade:
    
    # Hằng số cho kiểu tóm tắt
    GET_ALL_IMPORTANT = Summarize.GET_ALL_IMPORTANT
    GET_FIRST_IMPORTANT_AND_FOLLOWINGS = Summarize.GET_FIRST_IMPORTANT_AND_FOLLOWINGS
    
    def __init__(self):
        self._stop_words: Optional[Vietnamese] = None
    
    def set_stop_words(self, stop_words: Vietnamese) -> None:
        # Thiết lập stop words để lọc trong quá trình phân tích
        self._stop_words = stop_words
    
    def get_only_keywords(self, raw_text: str) -> Dict[str, float]:
        # Trích xuất từ khóa và điểm số từ văn bản
        parser = Parser()
        parser.set_minimum_word_length(3)
        parser.set_raw_text(raw_text)
        
        if self._stop_words:
            parser.set_stop_words(self._stop_words)
        
        text = parser.parse()
        
        graph = Graph()
        graph.create_graph(text)
        
        score = Score()
        return score.calculate(graph, text)
    
    def get_highlights(self, raw_text: str) -> List[str]:
        # Tìm các câu quan trọng nhất (20% tổng số câu)
        parser = Parser()
        parser.set_minimum_word_length(3)
        parser.set_raw_text(raw_text)
        
        if self._stop_words:
            parser.set_stop_words(self._stop_words)
        
        text = parser.parse()
        maximum_sentences = int(len(text.get_sentences()) * 0.2)
        
        graph = Graph()
        graph.create_graph(text)
        
        score = Score()
        scores = score.calculate(graph, text)
        
        summarize = Summarize()
        return summarize.get_summarize(
            scores,
            graph,
            text,
            12,
            maximum_sentences,
            Summarize.GET_ALL_IMPORTANT
        )
    
    def summarize_text_compound(self, raw_text: str) -> List[str]:
        # Tìm 3 câu quan trọng nhất từ văn bản
        parser = Parser()
        parser.set_minimum_word_length(3)
        parser.set_raw_text(raw_text)
        
        if self._stop_words:
            parser.set_stop_words(self._stop_words)
        
        text = parser.parse()
        
        graph = Graph()
        graph.create_graph(text)
        
        score = Score()
        scores = score.calculate(graph, text)
        
        summarize = Summarize()
        return summarize.get_summarize(
            scores,
            graph,
            text,
            10,
            3,
            Summarize.GET_ALL_IMPORTANT
        )
    
    def summarize_text_basic(self, raw_text: str) -> List[str]:
        # Tìm câu quan trọng nhất và các câu kế tiếp
        parser = Parser()
        parser.set_minimum_word_length(3)
        parser.set_raw_text(raw_text)
        
        if self._stop_words:
            parser.set_stop_words(self._stop_words)
        
        text = parser.parse()
        
        graph = Graph()
        graph.create_graph(text)
        
        score = Score()
        scores = score.calculate(graph, text)
        
        summarize = Summarize()
        return summarize.get_summarize(
            scores,
            graph,
            text,
            10,
            3,
            Summarize.GET_FIRST_IMPORTANT_AND_FOLLOWINGS
        )
    
    def summarize_text_freely(
        self,
        raw_text: str,
        analyzed_keywords: int,
        expected_sentences: int,
        summarize_type: int
    ) -> List[str]:
        # Tùy chỉnh tóm tắt văn bản theo tham số
        parser = Parser()
        parser.set_minimum_word_length(3)
        parser.set_raw_text(raw_text)
        
        if self._stop_words:
            parser.set_stop_words(self._stop_words)
        
        text = parser.parse()
        
        graph = Graph()
        graph.create_graph(text)
        
        score = Score()
        scores = score.calculate(graph, text)
        
        summarize = Summarize()
        return summarize.get_summarize(
            scores,
            graph,
            text,
            analyzed_keywords,
            expected_sentences,
            summarize_type
        )
