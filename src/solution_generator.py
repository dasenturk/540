# solution_generator.py

import random
from nltk.util import ngrams
from collections import defaultdict

class SolutionGenerator:
    def __init__(self, ngram_model):
        self.ngram_model = ngram_model

    def generate_solution(self, constraints):
        if 'functions' in constraints and constraints['functions']:
            last_function = constraints['functions'][-1]
            func_name = last_function['name']
            context = (func_name, ) 
        elif 'variables' in constraints and constraints['variables']:
            context = variables[-1]
        elif 'classes' in constraints and constraints['classes']:
            context = constraints['classes'][-1]
        elif 'imports' in constraints and constraints['imports']:
            context = constraints['imports'][-1]
        
        if context in self.ngram_model:
            return max(self.ngram_model[context], key=self.ngram_model[context].get)

        return None

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

