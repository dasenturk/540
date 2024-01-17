

from src.constraint_extractor import ConstraintExtractor
from src.solution_generator import SolutionGenerator

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

    # Sample dataset for training the n-gram model (in real scenario, load a large dataset)
    example_dataset = ["def calculate_sum(a, b):", "return a + b"]

    # Train the n-gram model
    ngram_model = SolutionGenerator.train_ngram_model(example_dataset)

    # Initialize the SolutionGenerator with the trained model
    solution_generator = SolutionGenerator(ngram_model)

    # Generate a solution based on a context
    # For demonstration, let's assume we want to complete after "def calculate_sum(a,"
    context = ("def", "calculate_sum(a,")  # This context would be dynamically derived from the code in real scenarios
    next_token = solution_generator.generate_solution(context)
    print("Suggested Completion:", next_token)

if __name__ == "__main__":
    main()
