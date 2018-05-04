This script gets tweet dumps from Archive.org (https://archive.org/details/twitterstream) and then dump all of them to mongo.

Steps: 
1. Get data from https://archive.org/details/twitterstream for desired year/month/dates
2. Extract all the tars
3. Extract the tweet jsons
4. Insert into mongo

Run:
1. Change following parameters before running the main script:
    1.1 year
    1.2 month
    1.3 from_date
    1.4 to_date
    1.5 mongo_db
    1.6 mongo_collection
2. Install the requirements
3. Create a unique index on tweet id (As the dumps from archiv.orge contain a lot of duplicate data): `db.tweets.createIndex({"id":1}, {unique:true})`
4. Run `python main.py`

Note:
1. Steps mentioned above are sequential, unless all the tweet dumps for given dates have been downloaded, the script will not move ahead to dump any of the file.
2. It is advised to have a unique index in your mongo collection on tweet.id, as the tweet dumps contain a lot of duplicate data.
`db.tweets.createIndex({"id":1}, {unique:true})`
3. Downloading the data for a month, even for few days takes a lot of time, it is also advised to try running the script to get data for single day, to get some confidence before running the script for a month's data.
4. Make sure you have enough storage left, dont run it on your macbook air :).
