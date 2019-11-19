# Student Name = Connie Chen
# Student Number = 2510856218


def compute_tweets(tweet_file_name, keyword_file_name):
    # try input from main.py to see if keyword and tweet files exist. if not, return error as blank list
    try:
        keyword_file = open(keyword_file_name, "r", encoding="utf-8")
        # initiate keyword_value and keyword_word file to store sentiment keywords and their happiness values
        keyword_value = []
        keyword_word = []

        # clean each keyword line by splitting at; results with ["keyword", "value"], then append to lists in lines 14 and 15
        for key_line in keyword_file:
            clean_key_line = key_line.split(",")
            keyword_word.append(clean_key_line[0])
            keyword_value.append(clean_key_line[1].strip("\n"))
    except IOError:
        print("File error: inputted keyword file does not exist")
        return []

    try:
        tweet_file = open(tweet_file_name, "r", encoding="utf-8")

        # initialize variables that count the total number of tweets in each region
        eastern_count_tweet = 0
        pacific_count_tweet = 0
        central_count_tweet = 0
        mountain_count_tweet = 0

        # initialize variables that count the total number of KEY tweets in each region
        eastern_count_key = 0
        pacific_count_key = 0
        central_count_key = 0
        mountain_count_key = 0

        # initialize variables that sum the happiness scores in each region
        east_happyScore = 0
        pacific_happyScore = 0
        central_happyScore = 0
        mountain_happyScore = 0

        # clean each tweet line
        for tweet_line in tweet_file:
            split_tweet_line = tweet_line.split()  # split each line of tweet by spaces, creating ["[latitude," , "longitude]", "value", "date", "tweet"]

            latitude = split_tweet_line[0].strip("[,")
            latitude = float(latitude)
            longitude = split_tweet_line[1].strip("]")
            longitude = float(longitude)

            # use the function region to check which timezone you are in
            timeZone = region(latitude, longitude)

            # use the happyScore function to determine happiness score and check for existence of keyword in tweet
            happyScore = wordValueMatch(split_tweet_line, keyword_value, keyword_word)

            if timeZone == "EASTERN":
                eastern_count_tweet += 1
                if happyScore > 0:  # if there is a keyword in the tweet
                    eastern_count_key += 1  # counter for number of keyword tweets in Eastern region
                    east_happyScore += happyScore  # sum happiness score in Eastern timezone

            elif timeZone == "CENTRAL":
                central_count_tweet += 1
                if happyScore > 0:
                    central_count_key += 1
                    central_happyScore += happyScore

            elif timeZone == "MOUNTAIN":
                mountain_count_tweet += 1
                if happyScore > 0:
                    mountain_count_key += 1
                    mountain_happyScore += happyScore

            elif timeZone == "PACIFIC":
                pacific_count_tweet += 1
                if happyScore > 0:
                    pacific_count_key += 1
                    pacific_happyScore += happyScore

        # tuples = (average, number of keyword tweets, total tweets in region)
        eastern_tuple = (str(average(east_happyScore, eastern_count_key)), str(eastern_count_key), str(eastern_count_tweet))
        central_tuple = (str(average(central_happyScore, central_count_key)), str(central_count_key), str(central_count_tweet))
        mountain_tuple = (str(average(mountain_happyScore, mountain_count_key)), str(mountain_count_key), str(mountain_count_tweet))
        pacific_tuple = (str(average(pacific_happyScore, pacific_count_key)), str(pacific_count_key), str(pacific_count_tweet))

        keyword_file.close()  # close files once finished
        tweet_file.close()

        return eastern_tuple, central_tuple, mountain_tuple, pacific_tuple

    except IOError:
        print("File error: inputted tweets file does not exist")
        return []


# this function determines which timezone the tweet is in based off of longitude and latitude coordinates
def region(latitude, longitude):
    if 49.189789 >= latitude >= 24.660845:
        if -87.518395 <= longitude <= -67.444574:
            return "EASTERN"
        elif -101.998892 <= longitude <= -87.518395:
            return "CENTRAL"
        elif -115.236428 <= longitude <= -101.998892:
            return "MOUNTAIN"
        elif -125.242264 <= longitude <= -115.236428:
            return "PACIFIC"


# this function matches word from tweet with keywords and calculates happiness score (total score for all counted tweets in region / number of keywords)
def wordValueMatch(split_tweet_line, keyword_value, keyword_word):
    happyScore = 0
    countKeyword = 0
    for i in split_tweet_line:
        from string import punctuation
        punctuation = punctuation + " "
        i = i.lower().strip(punctuation)
        for j in keyword_word:
            if i == j:  # match word with keywords list
                countKeyword += 1
                happyScore += int(keyword_value[keyword_word.index(i)])

    if countKeyword == 0:
        return 0
    else:
        happyScore = happyScore / countKeyword
    return happyScore


# this function calculates average happiness score (first element in tuple) and zero division error trapping
def average(happyScore, count_keyword):
    try:
        avg_happinessScore = happyScore / count_keyword
        avg_happinessScore = round(avg_happinessScore, 4)
    except ZeroDivisionError:
        avg_happinessScore = 0

    return avg_happinessScore




