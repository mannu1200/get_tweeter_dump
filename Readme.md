This script gets tweet dumps from Archive.org (https://archive.org/details/twitterstream) and does a mongo dump.

Steps: 
1. Get data from https://archive.org/details/twitterstream for desired year/month/dates
2. Extract all the tars
3. Extract the tweet jsons
4. Insert into mongo

Run:
1. Change following parameters before running the main script:
""" year
    month
    from_date
    to_date
    mongo_db
    mongo_collection
"""
2. Install the requirements
3. Run `python main.py`

Notes:
1. Steps mentioned above are sequential, unless all the tweet dumps for given dates have downloaded, the script will not move ahead to further steps.
2. It is advised to have a unique index in your mongo collection on tweet.id, as the tweet dumps contain a lot of duplicate data.
`db.tweets.createIndex({"id":1}, {unique:true})`
3. Downloading the data for a month, even for few days takes a lot of time, it is also advised to try running the script to get data for single day, to get some confidence before running for a month's data.
4. Make sure you have enough storage left, dont run it on our mac air :).