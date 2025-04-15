from datasets import load_dataset

class DataLoader:
    def __init__(self, dataset_name="cnn_dailymail", split="test", sample_size=5):
        self.dataset_name = dataset_name
        self.split = split
        self.sample_size = sample_size

    def load_data(self):
        dataset = load_dataset("cnn_dailymail", "3.0.0", split="test", trust_remote_code=True)
        return dataset.select(range(min(self.sample_size, len(dataset))))