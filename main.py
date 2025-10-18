import file_processing as fp
import pandas as pd
import matplotlib.pyplot as plt


def main(df_list):
    """Load and normalise transaction files, returning a date-indexed summary."""
    processed_list = []
    for filepath in df_list:
        try:
            fin_df_instance = fp.FinancialDf(filepath)
            df = fin_df_instance.get_dataframe() 
            df = df[['Date', 'Amount']]  # Limit to the columns needed downstream
            df['Amount'] = df['Amount']* -1  # Treat debits as positive outflows
            df = df.set_index('Date')
            processed_list.append(df)
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            continue
    if not processed_list:
        raise ValueError("No valid DataFrames were processed")

    combined_instance = fp.CombinedDf(processed_list) # Combines dfs in processed_list
    return combined_instance.finalise_df()


if __name__ == '__main__':
    df_files = ['credit1.csv', 'credit2.csv']
    try:
        combined_file = main(df_files)
        # Basic spending scatter plot for a quick visual sanity check
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.scatter(combined_file.index, combined_file['Amount'], marker='o', label='Daily Spending')  
        ax.set_xlabel('Date')
        ax.set_ylabel('Amount (€)')
        ax.set_title('Spending Over Time')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show() 
    except Exception as e:
        print(f"Execution error {e}")
