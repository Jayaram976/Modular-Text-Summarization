from data_loader.loader import DataLoader
from models.summarizer import Summarizer
from pipeline.preprocessor import preprocess
from pipeline.postprocessor import postprocess
from evaluator import Evaluator
from utils.logger import get_logger

logger = get_logger("SummarizerApp")

def main():
    try:
        logger.info("Loading dataset...")
        data_loader = DataLoader(sample_size=5)
        dataset = data_loader.load_data()

        summarizer = Summarizer()
        evaluator = Evaluator()

        for i, item in enumerate(dataset):
            logger.info(f"\n=== Sample {i+1} ===")

            # Automatically detect which dataset is being used
            if "dialogue" in item:
                input_text = item["dialogue"]
                reference_summary = item["summary"]
            elif "article" in item:
                input_text = item["article"]
                reference_summary = item["highlights"]
            else:
                logger.warning("Unrecognized data format. Skipping sample.")
                continue

            cleaned_text = preprocess(input_text)
            predicted_summary = summarizer.summarize(cleaned_text)
            final_output = postprocess(predicted_summary)

            print(f"\n Input Text:\n{input_text}")
            print(f" Reference Summary:\n{reference_summary}")
            print(f" Predicted Summary:\n{final_output}")


            # Rouge Score
            scores = evaluator.evaluate(reference_summary, final_output)
            print(f" ROUGE Scores: {scores}")

    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()