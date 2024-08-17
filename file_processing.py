import pandas as pd

class FinancialDf:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = self.read_file()

    def read_file(self):
        """Reads file based on its extension."""
        if self.filepath.endswith('.csv'):
            return pd.read_csv(self.filepath)
        elif self.filepath.endswith('.xlsx') or self.filepath.endswith('.xls'):
            return pd.read_excel(self.filepath)
        else:
            raise ValueError("Unsupported file format. Please use a CSV or Excel file.")

    def get_dataframe(self):
        """Returns the DataFrame."""
        return self.df
    
class CombinedDf:
    def __init__(self, df_list):
        self.df_list = df_list

    def combine_df(self):
        """Combines multiple DataFrames into one."""
        if not self.df_list:
            return None 
        combined_df = pd.concat(self.df_list)
        return combined_df
        
    def finalise_df(self):
        """Finalises the combined DataFrame."""
        if not self.df_list:
            return None
        combined_df = self.combine_df()
        return combined_df.groupby(combined_df.index).sum()
    
#def exclude_val(df, amount, column):
#    return df.query(df[column] < amount)
