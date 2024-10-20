import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import matplotlib.pyplot as plt

def read_file(name):
    with open(name, 'r', encoding='utf-8') as file:
        read = file.read()
    return read

def tagging(data):
    words = word_tokenize(data)
    pos_tagged = pos_tag(words)
    return pos_tagged

def format_paragraph(pos_tagged):
    punctuation = {'.', ',', '!', '?', ';', ':', '-', '(', ')', '"', "'", '…'}
    formatted_text = []
    for word, tag in pos_tagged:
        if word not in punctuation:
            formatted_text.append(f"{word}({tag})")
    return ' '.join(formatted_text)

def save_to_file(formatted_paragraph, output_file):
    print("Saving to file...")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(formatted_paragraph)
    print(f"File saved at: {output_file}")

def plotting(pos_tagged):
    major_categories = {
        'Nouns': ['NN', 'NNS', 'NNP', 'NNPS'],
        'Verbs': ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
        'Adjectives': ['JJ', 'JJR', 'JJS'],
        'Adverbs': ['RB', 'RBR', 'RBS'],
        'Pronouns': ['PRP', 'PRP$', 'WP', 'WP$'],
        'Prepositions': ['IN'],
        'Conjunctions': ['CC'],
        'Determiners': ['DT']
    }

    tag_counts = {category: 0 for category in major_categories}

    for word, tag in pos_tagged:
        for category, tags in major_categories.items():
            if tag in tags:
                tag_counts[category] += 1
                break

    # Create a bar graph
    plt.figure(figsize=(12, 7))
    plt.bar(tag_counts.keys(), tag_counts.values(), color='skyblue')
    plt.title('Frequency of Major Parts of Speech')
    plt.xlabel('Major Parts of Speech')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Corrected file paths without extra quotes
    name = r'C:\Users\amogh\Desktop\nltk\data.txt'
    output_file = r'output.txt'
    
    data = read_file(name)
    pos_tagged = tagging(data)
    formatted_paragraph = format_paragraph(pos_tagged)
    
    # Save the formatted paragraph to output.txt
    save_to_file(formatted_paragraph, output_file)

    # Plot the frequency of POS categories
    plotting(pos_tagged)

if __name__ == "__main__":
    main()
