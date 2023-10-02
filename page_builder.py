import pandas as pd

class page_builder:
    def __init__(self):
        # Read the CSV file
        df = pd.read_csv('LLM_Glossary_Terms.csv')
        self.vocab_data = self.process_dataframe(df)
        self.menu = sorted(list(set([key[0].upper() for key in self.vocab_data.keys()])))


    def process_dataframe(self, df):
        data = {}
        for index, row in df.iterrows():
            item = {
                'Target': row['Target'],
                'Tag': row['Tag'].split(';') if ';' in str(row['Tag']) else [row['Tag']], # 여러개의 태그를 붙이려면 ;로 구분
                'Example': [ex for ex in [row['Example1'], row['Example2']] if pd.notna(ex)],
                'URL': [url for url in [row['URL1'], row['URL2']] if pd.notna(url)]
            }
            data[row['Source']] = item
        return data

    def get_vocab_data(self, letter):
        # Return items that start with the given letter
        return {key: value for key, value in self.vocab_data.items() if key.lower().startswith(letter.lower())}

