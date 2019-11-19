# Student Name = Connie Chen
# Student Number = 2510856218

from sentiment_analysis import compute_tweets

# takes user input (names of the files)
tweet_file_name = input("Enter the name of the file containing tweets: ")
keyword_file_name = input("Enter the name of the file containing keywords: ")

num_regions = 4
results = compute_tweets(tweet_file_name, keyword_file_name)

# loops over results from compute_tweets in sentiment_analysis
for i in range(num_regions):
    # make sure no empty list is returned
    if len(results) > 0:

        # following if and elif statements print out header for each timezone
        if i == 0:
            print("\n" + "For the EASTERN timezone:")
        elif i == 1:
            print("\n" + "For the CENTRAL timezone: ")
        elif i == 2:
            print("\n" + "For the MOUNTAIN timezone: ")
        elif i == 3:
            print("\n" + "For the PACIFIC timezone: ")

    # following print statements print out appropriate elements in tuples from sentiment_analysis
    # index i finds the tuple for appropriate region and index [0], [1], etc finds appropriate element to print
    print("The average happiness value is: ", results[i][0])
    print("THe number of keyword tweets is:", results[i][1])
    print("The total number of tweets is: ", results[i][2])



