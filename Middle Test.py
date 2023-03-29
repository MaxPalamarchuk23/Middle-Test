def counter(fname):
    """
    Counts the number of sentences and words in a text file.
    
    Args:
        fname (str): The filename of the text file to be counted.
        
    Returns:
        None
    """
    num_words = 0
    num_sentences = 0
     
    try:
        with open(fname, 'r') as f:
            word_chars = [",", " ", ":", ";"]
            sentence_chars = [".", "!", "?", "..."]
            
            for line in f:
                # count number of words in line
                words = line.split()
                for word in words:
                    if any(char in word for char in word_chars):
                        num_words += 1
        
                # count number of sentences in line
                for char in line:
                    if char in sentence_chars:
                        num_sentences += 1

        print("Number of sentences: ", num_sentences)
        print("Number of words in text file: ", num_words)

    except FileNotFoundError:
        print('File not found')

# Driver Code:
if __name__ == '__main__':
    fname = 'File1.txt'
    counter(fname)