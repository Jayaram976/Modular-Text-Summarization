# evaluator/evaluator.py

from rouge_score import rouge_scorer

class Evaluator:
    def __init__(self):
        self.scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

    def evaluate(self, reference, prediction):
        scores = self.scorer.score(reference, prediction)
        result = {
            k: {
                "precision": round(v.precision, 2),
                "recall": round(v.recall, 2),
                "f1": round(v.fmeasure, 2)
            }
            for k, v in scores.items()
        }
        return result