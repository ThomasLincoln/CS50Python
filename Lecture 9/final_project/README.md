# Text Analyser
#### Video Demo

  https://youtu.be/GSJtu8eNlQo

#### Description

My final project for the CS50 Introduction to Python course is a versatile text analyzer. It allows for the analysis of various metrics within user-input text or *.txt files.

Implemented Functionalities:
Word Count: The count_words() function tallies the total number of words in the text.

Letter Count: Using count_letters(), it computes the total number of letters, disregarding punctuation like commas and periods.

Paragraph and Line Count: count_paragraphs() calculates the number of paragraphs based on newline counts, while count_lines() estimates the number of lines by counting periods.

Word Frequencies: word_frequencies() generates a frequency dictionary for each word in the text, indicating how many times each appears.

Specific Word Frequency: The word_frequency() function computes the frequency of a specific word input by the user.

Program Implementation:
User input can be entered in two ways: direct typing or through a *.txt file. The code checks for the presence of the "--paste" argument to determine if the text is typed or from a file.

The user interface presents multiple options through a menu:

Counting words, letters, paragraphs, and lines.
Checking the frequency of all words or a specific one.
Displaying the complete text.
Program Structure:
Utilizing the argparse module, the program captures user-provided arguments upon script execution, offering greater flexibility in data input.

The menu logic is constructed through a while loop that awaits user input to process different analysis options.

The project lays a solid foundation for text analysis, but there's still room for improvement and future expansions.



### TODO

Potential Future Improvements:
Refinement of Text Processing: Enhancements can be made in handling punctuation, considering more cases to ensure accurate letter and word counting.

Graphical User Interface (GUI): Implementing a graphical interface to make interaction more intuitive and user-friendly.

Addition of New Metrics: Expanding functionalities to include additional metrics such as sentence counting, phrase frequency analysis, among others.