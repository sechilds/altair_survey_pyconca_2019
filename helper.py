
def setcols(df, fn=lambda x: x.columns.map('_'.join), cols=None):
    """
        Sets the column of the data frame to the passed column list.
    """
    if cols:
        df.columns = cols
    else:
        df.columns = fn(df)
    return df
