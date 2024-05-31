# Claim&cited-paragraph classification

The corresponding <a href="https://www.notion.so/Early-baseline-for-claim-cited-paragraph-classification-on-PatentMatch-Herman-330f50f586f74779a19b32c304c0b3d0">Plan of Experiment is provided here</a>.
The <a href="https://www.notion.so/Report-Herman-Early-Baseline-PatentMatch-Paragraph-Classification-edd3d425261047a5a1633f2550d13f4c">Full Report</a> describing the effort is also available.


## Goal of the experiment
The primary objective of this experiment is to develop a model capable of accurately classifying 'X' citations within the PatentMatch dataset, as part of our effort to create a “prior art” search model. The task involves analyzing pairs of text segments (claims and related passages) to determine the binary classification label that indicates the presence of an 'X' citation, which signifies a critical piece of prior art.

## How to run the code

### `src` Folder

- **`data_cleansing.py`**: Contains functions for cleaning the dataset by removing duplicate rows and null values.
- **`settings.py`**: Used for loading credentials from the `.env` file.

### `notebooks` Folder

- **`clear_dataset.ipynb`**: Calls functions to clean the dataset, splits the training dataset into train and validation sets in an 80/20 ratio, and saves everything as .parquet files in the `data` folder.
- **`test1.ipynb`**: Code for training a model using the Trainer API from Hugging Face's transformers library.
- **`test2.ipynb`**: Code for training a model with more manual handling of data preparation, training, and evaluation.

### Running the Code

1. Clean the data using `clear_dataset.ipynb`. (If you have your own data in the .parquet format. If not, you can use a ready-made one)
2. After cleaning the data, you can train the model using the library that suits you best. (test1 or test2)
3. The best weights and confusion matrixes will be saved in the `artifacts` folder
   
Requirements are listed in the `requirements.txt` file

The code includes comprehensive comments and supports running in Google Colab (sections of the code needed to run in Google Colab are marked with the comment `#code required by Colab`). 
Also this code is connected to MLflow (your credentials are needed).


### To clone this repository, run the following command:

```bash
git clone git@github.com:HumanDevIP/citation-classifier-herman.git
```
### Compute Environment Information:

- **Python version**: 3.12.2 
- **Compute environment**: Windows 11 on a local machine

![Python Version](https://img.shields.io/badge/python-3.12.2-blue)
![OS](https://img.shields.io/badge/os-Windows%2011-blue)
## Data

The cleaned and processed parts of the dataset are available in the `data` folder. These files include:

- `clean_test.parquet`
- `clean_train.parquet`
- `clean_val.parquet`

### Raw Data

The raw, unprocessed data files are also provided:

- `test.parquet`
- `train.parquet`

### Column Descriptions

- **text**: Contains the claims.
- **text_b**: Contains the corresponding passages.
- **label**: Indicates the type of citation:
  - `1`: 'X' citation
  - `0`: 'A' citation


## Credentials
To set up your environment, create a `.env` file and add the following configurations with your data:

```env
MLFLOW_TRACKING_URI=
MLFLOW_TRACKING_USERNAME=
MLFLOW_TRACKING_PASSWORD=
```

Replace the placeholders with your specific details to ensure proper tracking and authentication.

