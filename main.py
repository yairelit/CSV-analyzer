import os
import pandas as pd


def load_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    
    if extension == '.csv':
        df = pd.read_csv(file_path)
    elif extension in ['.xls', '.xlsx']:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type. Only .csv, .xls, and .xlsx are allowed.")
    
    return df

def basic_statistics(df):
    print(f"rows: {df.shape[0]}")
    print(f"columns: {df.shape[1]}")
    print("")
    print("columns names + dtypes:")
    print(df.dtypes)
    print("")
    print("basic math for numerical features:")
    print(df.describe().drop('count'))
    return


def filter_by_value(df, column, value):
    return df[df[column] == value]


def main():
    path = input("Enter the path of a CSV file: ").strip()
    
    try:
        df = load_file(path)
        basic_statistics(df)
    except FileNotFoundError:
        print("❌ File not found. Please check the path and try again.")
        return
    except pd.errors.ParserError:
        print("❌ The file could not be parsed as a CSV.")
        return
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return

    do_filter = input("\nWould you like to filter the data? (y/n): ").strip().lower()

    if do_filter == 'y':
        column = input("Enter column name: ").strip()
        value = input("Enter value to filter by: ").strip()
    
    if column not in df.columns:
        print("❌ Column not found.")
    else:
        filtered_df = filter_by_value(df, column, value)
        print("\nFiltered results:")
        print(filtered_df.head())

        save = input("\nSave filtered results to CSV? (y/n): ").strip().lower()
        if save == 'y':
            filtered_df.to_csv("filtered_output.csv", index=False)
            print("✅ Saved to 'filtered_output.csv'")


if __name__ == "__main__":
    main()
