import os

# Install kaggle API if not already installed
try:
    import kaggle
except ImportError:
    os.system("pip install kaggle")

# Path where dataset will be saved
DATASET_DIR = "data/garbage_dataset"

# Kaggle dataset identifier (from the URL)
KAGGLE_DATASET = "zlatan599/garbage-dataset-classification"

def download_dataset():
    # Ensure kaggle.json exists
    kaggle_json = os.path.expanduser("~/.kaggle/kaggle.json")
    if not os.path.exists(kaggle_json):
        raise FileNotFoundError(
            "⚠️ Kaggle API token not found!\n"
            "1. Go to https://www.kaggle.com/account\n"
            "2. Create API Token (downloads kaggle.json)\n"
            "3. Place kaggle.json in ~/.kaggle/ (Linux/Mac) or C:\\Users\\<username>\\.kaggle\\ (Windows)"
        )
    
    # Create dataset folder if not exists
    os.makedirs(DATASET_DIR, exist_ok=True)

    # Download dataset
    print("⬇️ Downloading dataset from Kaggle...")
    os.system(f"kaggle datasets download -d {KAGGLE_DATASET} -p {DATASET_DIR} --unzip")
    print(f"✅ Dataset downloaded and extracted to: {DATASET_DIR}")

if __name__ == "__main__":
    download_dataset()
