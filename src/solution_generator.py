# solution_generator.py

import random
from nltk.util import ngrams
from collections import defaultdict

class SolutionGenerator:
    def __init__(self, ngram_model):
        self.ngram_model = ngram_model

    def generate_solution(self, context):
        if context not in self.ngram_model:
            return None  # No suggestions available for this context

        possible_tokens = self.ngram_model[context]
        return max(possible_tokens, key=possible_tokens.get)  # Return the most likely token

    @staticmethod
    def train_ngram_model(dataset, n=3):
        
        model = defaultdict(lambda: defaultdict(lambda: 0))

        for line in dataset:
            # Tokenize the line and generate n-grams
            tokens = line.split()  # Basic tokenization
            for ngram in ngrams(tokens, n, pad_right=True, pad_left=True):
                model[ngram[:-1]][ngram[-1]] += 1

        # Convert counts to probabilities
        for ngram_context in model:
            total_count = float(sum(model[ngram_context].values()))
            for token in model[ngram_context]:
                model[ngram_context][token] /= total_count

        return model

