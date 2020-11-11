from wiki import article_metadata, ask_search, ask_advanced_search

# FOR ALL OF THESE FUNCTIONS, READ THE FULL INSTRUCTIONS.

# 1) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for in article metadata
#
# Returns: list of metadata for articles in which the article contains the keyword.
# If the user does not enter anything, return an empty list
#
# Hint: to get list of existing article metadata, use article_metadata()

# TODO Write code for #1 here
def search(keyword):
    if keyword == '':
        return []

    metadata_lists = []
    for metadata in article_metadata():
        for item in metadata[4]:
            if keyword.lower() == item.lower():
                metadata_lists.append(metadata[0:4])
    
    return metadata_lists

'''
Functions 2-7 are called after searching for article metadata with the user's keyword, 
and the given metadata parameter is the result of metadata resulting from that search.
'''

# 2) 
#
# Function: article_length
#
# Parameters:
#   max_length - max character length of articles
#   metadata - article metadata to search through
#
# Returns: list of article metadata from given metadata with articles not exceeding
# max_length number of characters 

# TODO Write code for #2 here
def article_length(max_length, metadata):
    new_metadata = []

    for article_list in metadata:
        if  article_list[3] <= max_length:
            new_metadata.append(article_list)

    return new_metadata

# 3) 
#
# Function: article_count
#
# Parameters:
#   count - max number of returned articles
#   metadata - article metadata
#
# Returns: list of article metadata in given metadata starting from the 
# beginning that do not exceed given count in total. If there are no 
# given article metadata, return an empty list regardless of the count.
#
# Warning: Python will not throw an error when the index goes beyond
# the length of the list. Please take care of that case - if your code
# gets the index beyond the length of the title, points will get taken
# off.

# TODO Write code for #3 here
def article_count(count, metadata):
    if count >= len(metadata):
        return metadata
    return metadata[0:count]

# 4) 
#
# Function: random_article
#
# Parameters:
#   index - index at which article title to return
#   metadata - article metadata
#
# Returns: article metadata in given metadata at given index. If
# index is not valid or there are no articles, return an empty string

# TODO Write code for #4 here
def random_article(index, metadata):
    if index >= len(metadata) or metadata == []:
        return ''
    return metadata[index]
# 5) 
#
# Function: favorite_author
#
# Parameters:
#   favorite - favorite author title
#   metadata - article metadata
#
# Returns: True if favorite author is in the given articles, 
# False otherwise

# TODO Write code for #5 here
def favorite_author(favorite, metadata):
    for article_list in metadata:
        if favorite == article_list[1]:
            return True
    return False

# 6) 
#
# Function: title_author
#
# Parameters:
#   metadata - article metadata
#
# Returns: list of only [title, author] for given metadata.
# If g

# TODO Write code for #6 here
def title_author(metadata):
    new_metadata = []

    for article_list in metadata:
        new_metadata.append(article_list[0:2])

    return new_metadata

# 7) 
#
# Function: multiple_keywords
#
# Parameters:
#   keyword - additional keyword to search
#   metadata - article metadata from basic search
#
# Returns: searches for article metadata from entire list of available
# articles and adds those articles to list of article metadata from basic 
# search

# TODO Write code for #7 here
def multiple_keywords(keyword, metadata):
    return metadata + search(keyword)

# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-5)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article metadata to contain only ones of the maximum length
        # TODO uncomment following line after writing the function and delete pass
        articles = article_length(value, articles)

    if advanced == 2:
        # value stores max number of articles
        # Update article metadata to contain only the max number of articles
        # TODO uncomment following line after writing the function and delete pass
        articles = article_count(value, articles)

    elif advanced == 3:
        # value stores random number
        # Update articles to only contain article metadata at index of random number
        # TODO uncomment following line after writing the function and delete pass
        articles = random_article(value, articles)

    elif advanced == 4:
        # value stores author
        # Store whether author is in search results into variable named has_favorite
        # TODO uncomment following line after writing the function and delete pass
        has_favorite = favorite_author(value, articles)

    elif advanced == 5:
        # Update article metadata to only contain titles and authors
        # TODO uncomment following line after writing the function and delete pass
        articles = title_author(articles)

    elif advanced == 6:
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
