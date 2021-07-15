# Search

## Introduction
Working with about 100 pre-determined Wikipedia articles, this project does various searches through those articles.

Part 1 works with the article titles and lists, and a user searches with word to get a list of article titles with that keyword. The user is also able to do the following advanced searches: restrict the maximum article title length, get a certain number of articles, get a random article, check whether a favorite article is in the returned list, and search for multiple keywords.

Part 2 works with article metadata (article title, author, timestamp, length of article, and list of keywords of the article) and 2D lists. A user searches with a word and gets a list of article metadata for articles that include the given word in its keywords list. The user is also able to do the following advanced searches: restrict the maximum article title length, get a certain number of articles, get a random article, check whether a favorite article is in the returned list, receive only title and author information, and search for multiple keywords.

Part 3 works with article metadata (article title, author, timestamp, length of article, and list of keywords of the article) and dictionaries. A user searches with a word and gets a list of article titles for articles that include the given word in its keywords list. The user is also able to do the following advanced searches: get the articles' metadata, restrict the maximum article title length, receive only titles and timestamp information, check whether a favorite article wrote any articles in the returned article titles list, and search for multiple keywords.


## Usage
`python search.py`: performs a search (for any of the parts). To do so, input a word when prompted, choose an advanced option, and input an appropriate response to the advanced option question.


### Other Files
`wiki.py`, `constants.py`: scraped article data from Wikipedia to be searched through

`search_tests.py`: unit and integration tests

`search_tests_helper.py`: helper functions for unit and integration tests
