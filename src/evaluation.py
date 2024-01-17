from sklearn.metrics import accuracy_score, precision_recall_fscore_support

class Evaluation:
    def __init__(self, solution_generator, baseline, test_data):
        self.solution_generator = solution_generator
        self.baseline = baseline
        self.test_data = test_data

    def evaluate(self):
        sg_predictions = []
        baseline_predictions = []
        true_labels = []

        for snippet, correct_solution in self.test_data:
            sg_pred = self.solution_generator.generate_solution(snippet)
            baseline_pred = self.baseline.generate_suggestion(snippet)

            sg_predictions.append(sg_pred)
            baseline_predictions.append(baseline_pred)
            true_labels.append(correct_solution)

        sg_accuracy = accuracy_score(true_labels, sg_predictions)
        sg_precision, sg_recall, sg_f1, _ = precision_recall_fscore_support(true_labels, sg_predictions, average='binary')

        baseline_accuracy = accuracy_score(true_labels, baseline_predictions)
        baseline_precision, baseline_recall, baseline_f1, _ = precision_recall_fscore_support(true_labels, baseline_predictions, average='binary')

        results = {
            'Solution Generator': {'Accuracy': sg_accuracy, 'Precision': sg_precision, 'Recall': sg_recall, 'F1 Score': sg_f1},
            'Baseline': {'Accuracy': baseline_accuracy, 'Precision': baseline_precision, 'Recall': baseline_recall, 'F1 Score': baseline_f1}
        }

        return results

