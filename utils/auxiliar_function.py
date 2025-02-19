import pandas as pd


def extract_metadata_from_paths(file_paths, column_names, indices):
    """
    Extracts metadata from a list of file paths and returns a DataFrame.

    Parameters:
    ----------
    file_paths : list of str
        List of file paths.
    column_names : list of str
        Names of metadata columns to be extracted.
    indices : list of int
        List of indices to extract from the file path split.

    Returns:
    -------
    metadata_df : pd.DataFrame
        DataFrame containing extracted metadata.
    """
    metadata_list = []

    for file_path in file_paths:
        file_parts = file_path.split(os.sep)  # Uses OS-independent separator
        metadata = {col: file_parts[i] for col, i in zip(column_names, indices)}
        metadata["file_path"] = file_path
        metadata_list.append(metadata)

    return pd.DataFrame(metadata_list)


"""# Example usage
column_names = ["split", "TYPE", "WC", "part"]
indices = [4, 6, 7, 8]  # Adjust indices based on your file path structure

metadata_df = extract_metadata_from_paths(csv_files, column_names, indices)
metadata_df["part"] = metadata_df["part"].str.split(".").str[0]  # Remove file extension

print(metadata_df.head())
"""
