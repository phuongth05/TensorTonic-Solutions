import numpy as np
from typing import List, Dict
from collections import Counter

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        special_tokens = [self.pad_token, 
                          self.unk_token, 
                          self.bos_token, 
                          self.eos_token]

        word_counter = Counter()

        for text in texts:
            word_counter.update(text.lower().split())

        self.word_to_id = {key: idx for idx, key in enumerate(special_tokens)}

        sorted_unique_words = sorted(word_counter.keys())

        for idx, word in enumerate(sorted_unique_words, start=len(self.word_to_id)):
            self.word_to_id[word] = idx

        self.id_to_word = {idx: word for word, idx in self.word_to_id.items()}
        self.vocab_size = len(self.word_to_id)
        return
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE

        words = text.lower().split()

        unk_id = self.word_to_id[self.unk_token]

        encoded_text = [self.word_to_id.get(word, unk_id) for word in words]

        return encoded_text

    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        words = [self.id_to_word.get(idx, self.unk_token) for idx in ids]

        return " ".join(words)
