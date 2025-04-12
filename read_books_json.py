import json
import pandas as pd

def read_json_to_dataframe(file_path="fetched_books_metadata.json"):
    try:
        # Read the JSON file
        with open(file_path, "r", encoding="utf-8") as f:
            book_data = json.load(f)
        
        # Prepare data for DataFrame
        rows = []
        for book_id, book_info in book_data.items():
            if isinstance(book_info, dict) and "error" not in book_info:
                row = {
                    "book_id": book_id,
                    "author": book_info.get("author"),
                    "year": book_info.get("year"),
                    "title": book_info.get("title"),
                    "description": book_info.get("description")
                }
                rows.append(row)
        
        # Create DataFrame
        df = pd.DataFrame(rows)
        
        # Reorder columns
        df = df[["book_id", "author", "year", "title", "description"]]
        
        return df
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Read JSON and create DataFrame
    df = read_json_to_dataframe()
    
    if df is not None:
        # Display the DataFrame
        print("\nBook Data DataFrame:")
        print("=" * 50)
        print(df)
        
        # Display basic information
        print("\nDataFrame Info:")
        print("=" * 50)
        print(f"Number of books: {len(df)}")
        print(f"Columns: {', '.join(df.columns)}")
        
        # Save to Excel
        df.to_excel("books_dataframe.xlsx", index=False)
        print("\nDataFrame saved to 'books_dataframe.xlsx'") 