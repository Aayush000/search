from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog') == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.

def test_title_to_info_test1():
    ''' Tests for title_to_info(), function #1. '''
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['company', 'aayush', 567890, 1023, ['go', 'come', 'he', 'that', 'up', 'sentence']],
                     ['house', 'bhatta', 923456, 80529, ['more', 'she', 'would', 'bake', 'chill']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'company': {'author': 'aayush', 'timestamp': 567890, 'length': 1023}, 
                'house': {'author': 'bhatta', 'timestamp': 923456, 'length': 80529}}
    assert title_to_info(deepcopy(fake_metadata)) == expected
    

def test_title_to_info_test2():
    ''' Tests for title_to_info(), function #1. '''
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['economics', 'william', 233567890, 21023, ['she', 'alot', 'the', 'they']],
                     ['computer', 'charles', 645923456, 22529, ['most', 'will', 'may', 'spray', 'chilly']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'economics': {'author': 'william', 'timestamp': 233567890, 'length': 21023}, 
                'computer': {'author': 'charles', 'timestamp': 645923456, 'length': 22529}}
    assert title_to_info(deepcopy(fake_metadata)) == expected


def test_title_to_info_test3():
    ''' Tests for title_to_info(), function #1. '''
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['google', 'sundar', 2567890, 21022, ['gdf', 'the', 'opp', 'lot']],
                     ['microsoft', 'pichai', 65923456, 2229, ['god', 'sun', 'ming', 'sing', 'lily']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'google': {'author': 'sundar', 'timestamp': 2567890, 'length': 21022}, 
                'microsoft': {'author': 'pichai', 'timestamp': 65923456, 'length': 2229}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_keyword_to_titles_test1():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['car', 'aayush', 4567890, 223, ['go', 'words', 'her', 'make', 'so', 'sentence']],
                     ['bike', 'helloworld', 23423456, 22029, ['more', 'go', 'so', 'make', 'her']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'go': ['car', 'bike'], 'words': ['car'], 'her': ['car', 'bike'], 'make': ['car', 'bike'], 'so': ['car', 'bike'], 'sentence': ['car'], 'more': ['bike']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected


def test_keyword_to_titles_test2():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['pen', 'william', 234567890, 343, ['more', 'give', 'her', 'make', 'take', 'chill']],
                     ['paper', 'smith', 3333423456, 19029, ['more', 'go', 'might', 'give', 'her']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'more': ['pen', 'paper'], 'give': ['pen', 'paper'], 'her': ['pen', 'paper'], 'make': ['pen'], 'take': ['pen'], 'chill': ['pen'], 'go': ['paper'], 'might': ['paper']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected


def test_keyword_to_titles_test3():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['tea', 'aayush', 4367890, 2343, ['yes', 'no', 'there', 'make', 'move', 'mountain']],
                     ['candy', 'kumar', 553423456, 889029, ['more', 'go', 'yes', 'there', 'her']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'yes': ['tea', 'candy'], 'no': ['tea'], 'there': ['tea', 'candy'], 'make': ['tea'], 'move': ['tea'], 'mountain': ['tea'], 'more': ['candy'], 'go': ['candy'], 'her': ['candy']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected


def test_unit_tests1():
    # Basic search, function #3
    assert search('school') == SCHOOL

    # Advanced search option 1, function #4
    expected = {'Edogawa, Tokyo': {'author': 'Ciphers', 'timestamp': 1222607041, 'length': 4526}, 'Fisk University': {'author': 'NerdyScienceDude', 'timestamp': 1263393671, 'length': 16246}, 'Annie (musical)': {'author': 'Piano non troppo', 'timestamp': 1223619626, 'length': 27558}, 'Alex Turner (musician)': {'author': 'CambridgeBayWeather', 'timestamp': 1187010135, 'length': 9718}}
    assert article_info(deepcopy(SCHOOL), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Edogawa, Tokyo', 'Fisk University', 'Alex Turner (musician)']
    assert article_length(20000, deepcopy(SCHOOL), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Edogawa, Tokyo': 1222607041, 'Fisk University': 1263393671, 'Annie (musical)': 1223619626, 'Alex Turner (musician)': 1187010135}
    assert title_timestamp(deepcopy(SCHOOL), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('Ciphers', deepcopy(SCHOOL), TITLE_TO_INFO) == True
    assert favorite_author('Aayush', deepcopy(SCHOOL), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)', 'C Sharp (programming language)', 'Fisk University', 'Python (programming language)']
    assert multiple_keywords('program', deepcopy(SCHOOL)) == expected


def test_unit_tests2():
    # Basic search, function #3
    assert search('photo') == PHOTO

    # Advanced search option 1, function #4
    expected = {'Digital photography': {'author': 'Mintleaf', 'timestamp': 1095727840, 'length': 18093}}
    assert article_info(deepcopy(PHOTO), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = []
    assert article_length(5, deepcopy(PHOTO), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Digital photography': 1095727840}
    assert title_timestamp(deepcopy(PHOTO), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('Mintleaf', deepcopy(SCHOOL), TITLE_TO_INFO) == False
    assert favorite_author('Bhatta', deepcopy(PHOTO), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Digital photography', 'Fisk University']
    assert multiple_keywords('education', deepcopy(PHOTO)) == expected


def test_unit_tests3():
    # Basic search, function #3
    assert search('dance') == DANCE

    # Advanced search option 1, function #4
    expected = {'List of Canadian musicians': {'author': 'Bearcat', 'timestamp': 1181623340, 'length': 21023}, '2009 in music': {'author': 'SE KinG', 'timestamp': 1235133583, 'length': 69451}, 'Old-time music': {'author': 'Badagnani', 'timestamp': 1124771619, 'length': 12755}, '1936 in music': {'author': 'JohnRogers', 'timestamp': 1243745950, 'length': 23417}, 'Indian classical music': {'author': 'Davydog', 'timestamp': 1222543238, 'length': 9503}}
    assert article_info(deepcopy(DANCE), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']
    assert article_length(80000, deepcopy(DANCE), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'List of Canadian musicians': 1181623340, '2009 in music': 1235133583, 'Old-time music': 1124771619, '1936 in music': 1243745950, 'Indian classical music': 1222543238}
    assert title_timestamp(deepcopy(DANCE), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('JohnRogers', deepcopy(SCHOOL), TITLE_TO_INFO) == False
    assert favorite_author('google', deepcopy(DANCE), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music', 'List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']
    assert multiple_keywords('music', deepcopy(DANCE)) == expected


@patch('builtins.input')
def test_integration_test1(input_mock):
    keyword = 'programming'
    advanced_option = 1

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'C Sharp (programming language)': {'author': 'Eaglizard', 'timestamp': 1232492672, 'length': 52364}, 'Python (programming language)': {'author': 'Lulu of the Lotus-Eaters', 'timestamp': 1137530195, 'length': 41571}, 'Lua (programming language)': {'author': 'Makkuro', 'timestamp': 1113957128, 'length': 0}, 'Covariance and contravariance (computer science)': {'author': 'Wakapop', 'timestamp': 1167547364, 'length': 7453}, 'Personal computer': {'author': 'Darklock', 'timestamp': 1220391790, 'length': 45663}, 'Ruby (programming language)': {'author': 'Hervegirod', 'timestamp': 1193928035, 'length': 30284}}\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected


@patch('builtins.input')
def test_integration_test2(input_mock):
    keyword = 'school'
    advanced_option = 5
    advanced_response = 'music'

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)', 'List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected


@patch('builtins.input')
def test_integration_test3(input_mock):
    keyword = 'soccer'
    advanced_option = 3

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Spain national beach soccer team': 1233458894, 'Will Johnson (soccer)': 1218489712, 'Steven Cohen (soccer)': 1237669593}\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
    test_example_title_to_info_tests()
    test_example_keyword_to_titles_tests()
    test_example_unit_tests()
    test_example_integration_test()
    
    test_title_to_info_test1()
    test_title_to_info_test2()
    test_title_to_info_test3()
    test_keyword_to_titles_test1()
    test_keyword_to_titles_test2()
    test_keyword_to_titles_test3()
    test_unit_tests1()
    test_unit_tests2()
    test_unit_tests3()
    test_integration_test1()
    test_integration_test2()
    test_integration_test3()
    
    
    
    
    
    
    