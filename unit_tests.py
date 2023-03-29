import pytest
import os
from counter import counter


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        counter('invalid_file.txt')


def test_count_words_and_sentences():
    expected_num_words = 15
    expected_num_sentences = 2
    file_path = os.path.join(os.getcwd(), 'test_file.txt')
    with open(file_path, 'w') as f:
        f.write('This is a test file. It has 15 words.')
    assert counter(file_path) == (expected_num_words, expected_num_sentences)
    os.remove(file_path)