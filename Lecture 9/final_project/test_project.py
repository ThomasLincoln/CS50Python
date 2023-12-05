from project import count_letters, count_words, count_lines, count_paragraphs, word_frequencies, word_frequency

def test_count_words():
    text = "This is an example sentence."
    assert count_words(text) == 5

def test_count_letters():
    text = "Example text."
    assert count_letters(text) == 12

def test_count_paragraphs():
    text = "Paragraph 1\nParagraph 2\nParagraph 3"
    assert count_paragraphs(text) == 3

def test_count_lines():
    text = "Line 1. Line 2. Line 3."
    assert count_lines(text) == 3

def test_word_frequencies():
    text = "Python is a powerful programming language Python is versatile."
    frequencies = word_frequencies(text)
    assert frequencies.get('Python') == 2
    assert frequencies.get('is') == 2
    assert frequencies.get('programming') == 1

def test_word_frequency():
    text = "Python is a powerful programming language Python is versatile."
    frequency = word_frequency(text, 'Python')
    assert frequency.get('Python') == 2

if __name__ == "__main__":
    test_count_words()
    test_count_letters()
    test_count_paragraphs()
    test_count_lines()
    test_word_frequencies()
    test_word_frequency()
    print("All tests passed!")
