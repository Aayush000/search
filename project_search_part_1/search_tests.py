from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch

# List of all available article titles for this search engine
# The benefit of using this is faster code - article_titles() will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
ARTICLE_TITLES = article_titles()

def test_example_unit_tests():
    # Storing into a variable so don't need to copy and paste long list every time
    # If you want to store search results into a variable like this, make sure you pass a copy of it when
    # calling a function, otherwise the original list (ie the one stored in your variable) is going to be
    # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
    dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']

    # Example tests, these do not count as your tests

    # Basic search, function #1
    assert search('dog') == dog_search_results

    # Advanced search option 1, function #2
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']
    assert title_length(25, dog_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(3, dog_search_results.copy()) == ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid']

    # Advanced search option 3, function #4
    assert random_article(3, dog_search_results.copy()) == 'Black dog (ghost)'

    # Advanced search option 4, function #5
    assert favorite_article('Guide dog', dog_search_results.copy()) == True

    # Advanced search option 5, function #6
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']
    assert multiple_keywords('volleyball', dog_search_results.copy()) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 1
    advanced_response = 25

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'Edogawa, Tokyo\', \'Kevin Cadogan\', \'Endogenous cannabinoid\', \'Black dog (ghost)\', \'2007 Bulldogs RLFC season\', \'Mexican dog-faced bat\', \'Dalmatian (dog)\', \'Guide dog\', \'Georgia Bulldogs football\', \'Endoglin\', \'Sun dog\', \'The Mandogs\', \'Landseer (dog)\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.

def test_unit_tests1():
    volleyball_search_results = ['USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']

    # Basic search, function #1
    assert search('volleyball') == volleyball_search_results

    # Advanced search option 1, function #2
    expected = ['USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']
    assert title_length(30, volleyball_search_results.copy()) == expected
    
    expected = []
    assert title_length(5, volleyball_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(1, volleyball_search_results.copy()) == ['USC Trojans volleyball']
    assert article_count(0, volleyball_search_results.copy()) == []

    # Advanced search option 3, function #4
    assert random_article(1, volleyball_search_results.copy()) == 'Mets de Guaynabo (volleyball)'
    assert random_article(0, volleyball_search_results.copy()) == 'USC Trojans volleyball'

    # Advanced search option 4, function #5
    assert favorite_article('Guide dog', volleyball_search_results.copy()) == False
    assert favorite_article('USC Trojans volleyball', volleyball_search_results.copy()) == True

    # Advanced search option 5, function #6
    expected = ['USC Trojans volleyball', 'Mets de Guaynabo (volleyball)', 'List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
    assert multiple_keywords('music', volleyball_search_results.copy()) == expected
    
    expected = ['USC Trojans volleyball', 'Mets de Guaynabo (volleyball)', 'Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
    assert multiple_keywords('dog', volleyball_search_results.copy()) == expected


def test_unit_tests2():
    travel_search_results = ['Medical value travel', 'Time travel', 'List of video games with time travel']
    
    # Basic search, function #1
    assert search('travel') == travel_search_results

    # Advanced search option 1, function #2
    expected = ['Medical value travel', 'Time travel']
    assert title_length(23, travel_search_results.copy()) == expected
    
    expected = ['Time travel']
    assert title_length(15, travel_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(2, travel_search_results.copy()) == ['Medical value travel', 'Time travel']
    assert article_count(50, travel_search_results.copy()) == ['Medical value travel', 'Time travel', 'List of video games with time travel']
    
    # Advanced search option 3, function #4
    assert random_article(2, travel_search_results.copy()) == 'List of video games with time travel'
    assert random_article(0, travel_search_results.copy()) == 'Medical value travel'

    # Advanced search option 4, function #5
    assert favorite_article('Time travel', travel_search_results.copy()) == True
    assert favorite_article('Time travels', travel_search_results.copy()) == False

    # Advanced search option 5, function #6
    expected = ['Medical value travel', 'Time travel', 'List of video games with time travel', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)', "United States men's national soccer team 2009 results", 'China national soccer team', "Wake Forest Demon Deacons men's soccer"]
    assert multiple_keywords('soccer', travel_search_results.copy()) == expected
    
    expected = ['Medical value travel', 'Time travel', 'List of video games with time travel', '2007 Bulldogs RLFC season', 'Will Johnson (soccer)', 'Personal computer', 'Charles McPherson (musician)', 'Comparison of programming languages (basic instructions)']
    assert multiple_keywords('son', travel_search_results.copy()) == expected


def test_unit_tests3():
    empty_string_search_results = []
    
    # Basic search, function #1
    assert search('') == empty_string_search_results

    # Advanced search option 1, function #2
    expected = []
    assert title_length(3, empty_string_search_results.copy()) == expected
    assert title_length(0, empty_string_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(0, empty_string_search_results.copy()) == []
    assert article_count(50, empty_string_search_results.copy()) == []
    assert article_count(1, empty_string_search_results.copy()) == []
    
    # Advanced search option 3, function #4
    assert random_article(2, empty_string_search_results.copy()) == ''
    assert random_article(0, empty_string_search_results.copy()) == ''

    # Advanced search option 4, function #5
    assert favorite_article('Time travel', empty_string_search_results.copy()) == False
    assert favorite_article('', empty_string_search_results.copy()) == False

    # Advanced search option 5, function #6
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
    assert multiple_keywords('dog', empty_string_search_results.copy()) == expected
    
    expected = []
    assert multiple_keywords('Aayush', empty_string_search_results.copy()) == expected


def test_unit_tests4():
    caty_search_results = []
    
    # Basic search, function #1
    assert search('caty') == caty_search_results

    # Advanced search option 1, function #2
    expected = []
    assert title_length(5, caty_search_results.copy()) == expected
    assert title_length(30, caty_search_results.copy()) == expected
    
    # Advanced search option 2, function #3
    assert article_count(1, caty_search_results.copy()) == []
    assert article_count(0, caty_search_results.copy()) == []
  
    # Advanced search option 3, function #4
    assert random_article(0, caty_search_results.copy()) == ''
    assert random_article(6, caty_search_results.copy()) == ''

    # Advanced search option 4, function #5
    assert favorite_article('Google', caty_search_results.copy()) == False
    assert favorite_article('', caty_search_results.copy()) == False

    # Advanced search option 5, function #6
    expected = ['C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)']
    assert multiple_keywords('programming', caty_search_results.copy()) == expected
    
    expected = []
    assert multiple_keywords('coin', caty_search_results.copy()) == expected


@patch('builtins.input')
def test_integration_tests1(input_mock):
    keyword = 'volleyball'
    advanced_option = 1
    advanced_response = 30

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'USC Trojans volleyball\', \'Mets de Guaynabo (volleyball)\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected


@patch('builtins.input')
def test_integration_tests2(input_mock):
    keyword = 'program'
    advanced_option = 2
    advanced_response = 4

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'C Sharp (programming language)\', \'Reflection-oriented programming\', \'B (programming language)\', \'List of dystopian music, TV programs, and games\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
    
    
@patch('builtins.input')
def test_integration_tests3(input_mock):
    keyword = 'program'
    advanced_option = 2
    advanced_response = 56

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'C Sharp (programming language)\', \'Reflection-oriented programming\', \'B (programming language)\', \'List of dystopian music, TV programs, and games\', \'Python (programming language)\', \'Lua (programming language)\', \'Comparison of programming languages (basic instructions)\', \'Ruby (programming language)\', \'Semaphore (programming)\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected


@patch('builtins.input')
def test_integration_tests4(input_mock):
    keyword = 'music'
    advanced_option = 3
    advanced_response = 9

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: Aube (musician)\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected


@patch('builtins.input')
def test_integration_tests5(input_mock):
    keyword = 'music'
    advanced_option = 3
    advanced_response = 55

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nNo articles found\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected


@patch('builtins.input')
def test_integration_tests6(input_mock):
    keyword = 'photo'
    advanced_option = 4
    advanced_response = 'photography'

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'Digital photography\', \'Wildlife photography\']\nYour favorite article is not in the returned articles!\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
    
    
@patch('builtins.input')
def test_integration_tests7(input_mock):
    keyword = 'photo'
    advanced_option = 4
    advanced_response = 'Digital photography'

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'Digital photography\', \'Wildlife photography\']\nYour favorite article is in the returned articles!\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
    
    
@patch('builtins.input')
def test_integration_tests8(input_mock):
    keyword = 'soccer'
    advanced_option = 5
    advanced_response = 'ball'

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'Spain national beach soccer team\', \'Will Johnson (soccer)\', \'Steven Cohen (soccer)\', \'Craig Martin (soccer)\', "United States men\'s national soccer team 2009 results", \'China national soccer team\', "Wake Forest Demon Deacons men\'s soccer", \'USC Trojans volleyball\', \'2009 Louisiana Tech Bulldogs football team\', \'Georgia Bulldogs football\', \'Mets de Guaynabo (volleyball)\', \'Georgia Bulldogs football under Robert Winston\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected


@patch('builtins.input')
def test_integration_tests9(input_mock):
    keyword = ''
    advanced_option = 3
    advanced_response = 4

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nNo articles found\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
    
    
@patch('builtins.input')
def test_integration_tests10(input_mock):
    keyword = 'Aayush'
    advanced_option = 4
    advanced_response = 'Google'

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nNo articles found\nYour favorite article is not in the returned articles!\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
    

@patch('builtins.input')
def test_integration_tests11(input_mock):
    keyword = 'son'
    advanced_option = 6

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + '\nHere are your articles: [\'2007 Bulldogs RLFC season\', \'Will Johnson (soccer)\', \'Personal computer\', \'Charles McPherson (musician)\', \'Comparison of programming languages (basic instructions)\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected


# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To actually make all your tests run, call all of your test functions here.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    test_example_unit_tests()
    test_example_integration_test()
    
    test_unit_tests1()
    test_unit_tests2()
    test_unit_tests3()
    test_unit_tests4()
    test_integration_tests1()
    test_integration_tests2()
    test_integration_tests3()
    test_integration_tests4()
    test_integration_tests5()
    test_integration_tests6()
    test_integration_tests7()
    test_integration_tests8()
    test_integration_tests9()
    test_integration_tests10()
    test_integration_tests11()






