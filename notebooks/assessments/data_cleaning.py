import csv
from io import open
import codecs

# read csv
import pandas as pd

df = pd.read_csv('data_1.csv')
df.dropna(inplace=True)

from nlp_modules import process

output_sentence_processed = process(output_sentence)

print("ok")
# cleaning
# Write new csv file
datafile = "formatted_data.txt"
delimiter = '\t'
delimiter = str(codecs.decode(delimiter, "unicode_escape"))

with open(datafile, 'w', encoding='utf-8') as outputfile:
    writer = csv.writer(outputfile, delimiter=delimiter, lineterminator='\n')

    for i in df.index:
        try:
            row = df.iloc[i]
            input_sentence = row['input']
            input_sentence_processed = process(input_sentence)
            output_sentence = row['output']
            output_sentence_processed = process(output_sentence)
            writer.writerow([input_sentence_processed, output_sentence_processed])
            if i % 100 == 0:
                print(i)
        except Exception as e:
            pass
# write to text_file
