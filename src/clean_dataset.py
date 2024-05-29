import pandas as pd
import os


def clearing():
    base_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    save_dir = os.path.join(base_dir, 'data')

    # Load the .parquet files
    df1 = pd.read_parquet(os.path.join(save_dir, 'train.parquet'))
    df2 = pd.read_parquet(os.path.join(save_dir, 'test.parquet'))

    # Concatenate them into one DataFrame
    combined_df = pd.concat([df1, df2])

    # Drop rows with null values in the 'text', 'text_b', and 'label' columns
    clean_df = combined_df.dropna(subset=['text', 'text_b', 'label'])

    # Select the columns 'text', 'text_b', 'label'
    selected_columns = clean_df[['text', 'text_b', 'label']]

    # Find duplicate rows based on the selected columns
    duplicates = selected_columns.duplicated(keep='first')

    # Remove the duplicate rows from the original DataFrame
    clean_df = clean_df[~duplicates]

    # Save the cleaned DataFrame to a new .parquet file
    clean_df.to_parquet(os.path.join(save_dir, 'clean_data.parquet'))

    # Print the number of rows before and after cleaning
    print(f"Initial number of rows: {len(combined_df)}")
    print(f"Number of rows after removing nulls and duplicates: {len(clean_df)}")


