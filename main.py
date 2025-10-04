import file_processing as fp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main(df_list, combined_list): # Still need to specify how combined_list works
    processed_list = []
    for filepath in df_list:
        fin_df_instance = fp.FinancialDf(filepath)
        df = fin_df_instance.get_dataframe() 
        processed_list.append(df)
    return processed_list

    # Potentially interesting to apply CombinedDF here too, but not sure how to do that with
    # this programme flow.

if __name__ == '__main__':
    df_files = ['credit1.csv', 'credit2.csv']
    processed_dfs = main(df_files) # convert files into dataframes
    
    credit1_instance = processed_dfs[0] # process first file
    credit1_instance = credit1_instance[['Date', 'Amount']]
    credit1_instance['Amount'] = credit1_instance['Amount'] * -1
    credit1_instance = credit1_instance.set_index('Date')

    credit2_instance = processed_dfs[1] #process second file
    credit2_instance = credit2_instance[['Date', 'Amount']]
    credit2_instance['Amount'] = credit2_instance['Amount'] * -1
    credit2_instance = credit2_instance.set_index('Date')

    combined_instance = fp.CombinedDf([credit1_instance, credit2_instance])
    combined_instance = combined_instance.finalise_df() # Combined dfs

    fig, ax = plt.subplots(figsize=(4, 3)) # Generate chart

    ax.scatter(combined_instance.index, combined_instance['Amount'], marker='o', label='Daily Spending')  

    ax.set_xlabel('Date') # Adjust format
    ax.set_ylabel('Amount (€)')
    ax.set_title('Spending Over Time')

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show() 


