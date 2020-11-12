from wiki import article_metadata, ask_search, ask_advanced_search, title_to_info_map, keyword_to_titles_map

# FOR ALL OF THESE FUNCTIONS, READ THE FULL INSTRUCTIONS.

# 1) 
#
# Function: title_to_info
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping article title to a dictionary with the following keys:
# author, timestamp, length of article

# Example return value:
# {
#   'article title': {'author': 'some author', 'timestamp': 1234567890, 'length': 2491}
#   'another title': {'author': 'another author', 'timestamp': 9876543210, 'length': 85761}
# }
#
# TODO Write code for #1 here
def title_to_info(metadata):
    main_dictionary = {}
    value_dictionary = {}
    dictionary = {'author':1, 'timestamp':2, 'length':3}
    
    for article in metadata:
        for item in dictionary:
            value_dictionary[item] = article[dictionary[item]]
        main_dictionary[article[0]] = value_dictionary
        value_dictionary = {}
            
    return main_dictionary

#
# Function: keyword_to_titles
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping keyword to list of article titles in which the
# articles contain keyword

# Example return value:
# {
#   'keyword': ['keyword article', 'another article']
#   'another_keyword': ['another keyword article', 'article title']
# }
#
# TODO Write code for #2 here
def keyword_to_titles(metadata):
    main_dict = {}
    
    for article in metadata:
        for keyword in article[4]:
            if keyword not in main_dict:
                main_dict[keyword] = [article[0]]
            else:
                main_dict[keyword] += [article[0]]
            
    return main_dict

#
# Function: search
#
# Parameters:
#   keyword - search word to look for
#   keyword_to_titles - dictionary mapping keyword to list of titles with articles
#                       containing the keyword
#
# Return: list of titles with articles containing the keyword 
#
# Hint: to get a mapping of article titles to list of titles with articles containing
# a keyword, use keyword_to_titles_map()
#
# TODO Write code for #3 here
def search(keyword):
    if keyword == '':
        return []
    
    for key in keyword_to_titles_map():
        if keyword.lower() == key.lower():
            return keyword_to_titles_map()[key]
    return []

'''
Functions 4-8 are called after searching for a list of articles containing the user's keyword.
'''
# 4) 
#
# Function: article_info
#
# Parameters:
#   titles - list of articles
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: dictionary mapping given article titles to corresponding metadata 
# (author, timestamp, length)
#
# TODO Write code for #4 here
def article_info(titles, title_to_info):
    main_dict = {}
    
    for item in titles:
        if item in title_to_info:
            main_dict[item] = title_to_info[item]
    
    return main_dict

# 5) 
#
# Function: article_length
#
# Parameters:
#   article_length - max character length of articles
#   titles - list of articles
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from given titles for articles that do not exceed article_length 
# number of characters
#
# TODO Write code for #5 here
def article_length(article_length, titles, title_to_info):
    req_list = []
    
    for item in titles:
        if title_to_info[item]['length'] <= article_length:
            req_list.append(item)
    
    return req_list

# 6) 
#
# Function: title_timestamp
#
# Parameters:
#   titles - list of articles
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: dictionary mapping article title to author for given titles
#
# TODO Write code for #6 here
def title_timestamp(titles, title_to_info):
    req_dict = {}
    
    for item in titles:
        req_dict[item] = title_to_info[item]['timestamp']
    
    return req_dict

# 7) 
#
# Function: favorite_author
#
# Parameters:
#   author - author name
#   titles - list of articles
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: True if given author wrote an article in given titles, False otherwise
#
# TODO Write code for #7 here
def favorite_author(author, titles, title_to_info):
    for item in titles:
        if author == title_to_info[item]['author']:
            return True
    return False

# 8) 
#
# Function: multiple_keywords
#
# Parameters:
#   keyword - additional keyword to search
#   titles - list of articles resulting from basic search
#
# Return: searches for articles containing the keyword from entire list of 
# available articles and adds those articles to list of given titles from basic 
# search
#
# TODO Write code for #8 here
def multiple_keywords(keyword, titles):
    return titles + search(keyword)

# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-7)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # Update articles to contain metadata
        # TODO uncomment following line after writing the function and delete pass
        articles = article_info(articles, title_to_info_map())

    if advanced == 2:
        # value stores max length of articles
        # Update articles to contain only ones not exceeding the maximum length
        # TODO uncomment following line after writing the function and delete pass
        articles = article_length(value, articles, title_to_info_map())

    elif advanced == 3:
        # Update article metadata to only contain titles and timestamps
        # TODO uncomment following line after writing the function and delete pass
        articles = title_timestamp(articles, title_to_info_map())

    elif advanced == 4:
        # Store whether author wrote an article in search results into variable 
        # named has_favorite
        # TODO uncomment following line after writing the function and delete pass
        has_favorite = favorite_author(value, articles, title_to_info_map())

    elif advanced == 5:
        # value stores keyword to search
        # Update article metadata to contain article metadata from both searches
        # TODO uncomment following line after writing the function and delete pass
        articles = multiple_keywords(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite author is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
