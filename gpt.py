from src.constraint_extractor import ConstraintExtractor
from src.solution_generator import SolutionGenerator
from src.evaluation import Evaluation

def main():
    code_snippet = "your_code_snippet_here"

    extractor = ConstraintExtractor()
    generator = SolutionGenerator(dataset)

    evaluator = Evaluation()

    constraints = extractor.extract(code_snippet)
    solutions = generator.generate(constraints)
    ranked_solutions = evaluator.evaluate(solutions)

    print("Top solution:", ranked_solutions[0] if ranked_solutions else "No solution found")

if __name__ == "__main__":
    main()
