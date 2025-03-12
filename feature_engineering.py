# Define custom function to preprocess and add new features
def feature_engineering(X):
    """Preprocess data and create new interaction features."""
    X = X.copy()

    # Drop unnecessary columns
    columns_to_drop = ['State', 'Total day minutes', 'Total eve minutes', 'Total night minutes', 'Total intl minutes']
    X = X.drop(columns=columns_to_drop, errors='ignore')

    X.replace({'Yes': 1, 'No' : 0}, inplace=True)  # changing "Yes" and "No" to 0 and 1
    X["International plan"] = X["International plan"].astype(int)  # changing True and False to 0 and 1
    X["Voice mail plan"] = X["Voice mail plan"].astype(int)  # changing True and False to 0 and 1

    # Adding summary columns for charges, minutes, and calls
    X["Total charges"] = X["Total day charge"] + X["Total eve charge"] + X["Total night charge"] + X["Total intl charge"]
    X["Total calls"] = X["Total day calls"] + X["Total eve calls"] + X["Total night calls"] + X["Total intl calls"]
    
    return X