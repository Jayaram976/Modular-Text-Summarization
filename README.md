#  Text Summarization Pipeline using Local LLM

This project implements a complete pipeline for abstractive text summarization using a self-hosted LLM. It supports datasets like CNN/DM and SAMSum and evaluates summaries using ROUGE metrics.

---

##  Project Structure

```
.
├── app.py                # Main runner file
├── data_loader/          # Loads and samples dataset
├── evaluator/            # ROUGE score evaluation
├── models/               # Summarization model wrapper
├── pipeline/             # Preprocessing and postprocessing logic
├── utils/                # Logging and helper functions
├── requirements.txt
├── README.md
└── insights.md           # Summary insights and findings
```

---

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourname/Modular-text-summarizer.git
cd Modular-text-summarizer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

---

##  Features

-  Preprocessing of input texts
-  Summarization using LLM
-  Postprocessing of model output
-  ROUGE score evaluation
-  Logging and error handling

---

##  Datasets Supported

- CNN_DailyMail

---

##  Evaluation Metric

- ROUGE-1
- ROUGE-2
- ROUGE-L (Precision, Recall, F1)

---

## ✍ Author

- [Jayaram976](https://github.com/yourname)

---

##  License

This project is licensed under the MIT License.
```

###  `insights.md` Template

```markdown
#  Evaluation Insights

This document contains insights derived from the summarization output and ROUGE evaluation.

---

##  Summary Quality Analysis

### Dataset: SAMSum

| Sample | Reference Summary | Predicted Summary | ROUGE-1 | ROUGE-2 | ROUGE-L |
|--------|-------------------|-------------------|---------|---------|---------|
| #1     | "Mike and Jenny..."| "Mike met Jenny..."| 0.72 | 0.54 | 0.68 |
| #2     | "Mom called about..."| "Mother called..."| 0.80 | 0.62 | 0.76 |
| ...    | ...               | ...               | ...     | ...     | ...     |

---

##  Observations

- **Strengths**:
  - Model captures key entities and actions.
  - Coherent and grammatically correct summaries.

- **Areas of Improvement**:
  - Occasionally misses temporal details.
  - Some pronoun references are unclear.

---

##  Improve the Model Performace

- Fine-tune model on a larger dialogue dataset.

---

##  Key Takeaway

> The model performs strongly in short dialogue summarization but benefits from further contextual training and fine-tuning.
```

