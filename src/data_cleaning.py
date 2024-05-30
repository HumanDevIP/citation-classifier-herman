import pandas as pd
import os


def clearing():
    base_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    save_dir = os.path.join(base_dir, 'data')

    # Load the .parquet files
    train_df  = pd.read_parquet(os.path.join(save_dir, 'train.parquet'))
    test_df  = pd.read_parquet(os.path.join(save_dir, 'test.parquet'))

    # Clean train and test data separately
    clean_train_df = clean_data(train_df)
    clean_test_df = clean_data(test_df)

    # Remove duplicates from test that are present in train
    # clean_test_df = remove_test_duplicates(clean_train_df, clean_test_df)

    # Save the cleaned DataFrames to new .parquet files
    clean_train_df.to_parquet(os.path.join(save_dir, 'clean_train.parquet'))
    clean_test_df.to_parquet(os.path.join(save_dir, 'clean_test.parquet'))

    # Print the number of rows before and after cleaning
    print(f"Train set: Initial number of rows: {len(train_df)}")
    print(f"Train set: Number of rows after removing nulls and duplicates: {len(clean_train_df)}")
    print(f"Test set: Initial number of rows: {len(test_df)}")
    print(f"Test set: Number of rows after removing nulls and duplicates: {len(clean_test_df)}")



def clean_data(df):
        # Drop rows with null values in the 'text', 'text_b', and 'label' columns
        clean_df = df.dropna(subset=['text', 'text_b', 'label'])
        
        # Select the columns 'text', 'text_b', 'label'
        selected_columns = clean_df[['text', 'text_b', 'label']]
        
        # Find duplicate rows based on the selected columns
        duplicates = selected_columns.duplicated(keep='first')
        
        # Remove the duplicate rows from the original DataFrame
        clean_df = clean_df[~duplicates]
        
        return clean_df

def remove_test_duplicates(train_df, test_df):
    # Create a key column to identify duplicates
    train_df['key'] = train_df['text'] + train_df['text_b'] + train_df['label'].astype(str)
    test_df['key'] = test_df['text'] + test_df['text_b'] + test_df['label'].astype(str)

    # Remove duplicates in test set that are present in train set
    clean_test_df = test_df[~test_df['key'].isin(train_df['key'])]

    # Drop the key column
    train_df.drop(columns=['key'], inplace=True)
    clean_test_df.drop(columns=['key'], inplace=True)

    return clean_test_df
