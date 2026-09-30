import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged_df = (pd.merge(visits, transactions, on='visit_id', how='left'))

    no_trans = merged_df[merged_df['transaction_id'].isna()]

    result = (
        no_trans.groupby('customer_id')['visit_id']
        .count()
        .reset_index(name='count_no_trans')
    )
    return result[['customer_id', 'count_no_trans']]