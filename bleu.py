from nltk.translate.bleu_score import sentence_bleu
import os
import statistics

reference = open(r"C:\Users\khore\OneDrive\Desktop\DATA309\bleu\sampling.txt", "r", encoding="utf8").read().splitlines()

# Specify the folder path where your text files are located
folder_path = r'C:\Users\khore\OneDrive\Desktop\DATA309\bleu\samples'

# Initialize an empty list to store the contents of text files
candidates = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a text file (you can add more specific checks if needed)
    if filename.endswith('.txt'):
        # Create the full path to the file
        file_path = os.path.join(folder_path, filename)
        
        # Open the file and read its contents into a string
        with open(file_path, 'r') as file:
            candidates.append(file.read().splitlines())

# Split candidate samples into a single list of each line
candidate = []
for x in candidates:
    for y in x:
        candidate.append(y)

# Calculate score for every line and take the average. It has been done this way because of the way that bleu score works, but also because
# there is no way to tell where a song ends and another starts in the original data
scores = []
for x in candidate:
    scores.append(sentence_bleu(reference, x))
print(statistics.mean(scores))

