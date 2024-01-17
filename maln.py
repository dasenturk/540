from datasets import load_dataset

from src.constraint_extractor import ConstraintExtractor
from src.solution_generator import SolutionGenerator
from stc.baseline import RuleBasedBaseline

def main():
    # Sample code snippet for which we want to generate completions
    code_snippet = """
def calculate_sum(a, b):
    return a + b
"""

    # Initialize the ConstraintExtractor
    constraint_extractor = ConstraintExtractor(code_snippet)

    # Extract constraints from the code snippet
    constraints = constraint_extractor.extract_constraints()
    print("Extracted Constraints:", constraints)

    
    train_dataset = load_dataset ("AhmedSSoliman/CodeSearchNet", split='train')
    test_dataset = load_dataset ("AhmedSSoliman/CodeSearchNet", split='test')

    # Train the n-gram model
    ngram_model = SolutionGenerator.train_ngram_model(train_dataset)

    # Initialize the SolutionGenerator with the trained model
    solution_generator = SolutionGenerator(ngram_model)

    # Generate a solution based on a context
    context = ("def", "calculate_sum(a,")  
    next_token = solution_generator.generate_solution(context)
    print("Suggested Completion:", next_token)
    
    rule_based_baseline = RuleBasedBaseline()
    last_line = code_snippet.strip().split('\n')[-1]
    baseline_solution = rule_based_baseline.generate_suggestion(last_line)
    print("Rule-Based Baseline Suggestion:", baseline_solution)

if __name__ == "__main__":
    main()
