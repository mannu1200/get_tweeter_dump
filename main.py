import wget
import os
from pipes import quote 


year = "2017"
month = "11"
from_date = "1"
to_date = "31" #Dont worry about month having 30 days, script wont break, we still would get a dummy file
mongo_db = "micromort"
mongo_collection = "tweets"


def download():

    
    for date in range(from_date, to_date+1):
        if(date < 10):
            date = '0' + str(date)
        url = "https://archive.org/download/archiveteam-twitter-stream-2017-11/twitter-stream-{}-{}-{}.tar".format(year, month, date)
        print url
        file_name = wget.download(url)
        print file_name


def extract_tar():
    root_dir = os.getcwd()
    zipped_files = [item for item in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, item))]
    for zipped_file in zipped_files:
        if zipped_file.endswith('.tar'):
            pa =  quote(root_dir + "/" + zipped_file)
            print "Extracting: " + pa
            os.system("tar -xvf " + pa)

def extract():
    root_dir = os.getcwd() + "/{}/".format(year)

    for month_dir in [item for item in os.listdir(root_dir) if not os.path.isfile(os.path.join(root_dir, item))]:
        
        month_dir_path = os.path.join(root_dir, month_dir)
        date_dirs = [item for item in os.listdir(month_dir_path) if not os.path.isfile(os.path.join(month_dir_path, item))]

        for date_dir in date_dirs:
            
            date_dir_path = os.path.join(month_dir_path, date_dir)
            time_dirs = [item for item in os.listdir(date_dir_path) if not os.path.isfile(os.path.join(date_dir_path, item))]
            
            for time_dir in time_dirs:
                
                time_dir_path = os.path.join(date_dir_path, time_dir)
                zipped_files = [item for item in os.listdir(time_dir_path) if os.path.isfile(os.path.join(time_dir_path, item))]

                for zipped_file in zipped_files:
                    if zipped_file.endswith(".bz2"):
                        zipped_file_path = os.path.join(time_dir_path, zipped_file)
                        print "Extracting: " + zipped_file_path
                        os.system("bzip2 -d " + zipped_file_path)                    


def dump():
    root_dir = os.getcwd() + "/{}/".format(year)

    for month_dir in [item for item in os.listdir(root_dir) if not os.path.isfile(os.path.join(root_dir, item))]:
        
        month_dir_path = os.path.join(root_dir, month_dir)
        date_dirs = [item for item in os.listdir(month_dir_path) if not os.path.isfile(os.path.join(month_dir_path, item))]

        for date_dir in date_dirs:
            
            date_dir_path = os.path.join(month_dir_path, date_dir)
            time_dirs = [item for item in os.listdir(date_dir_path) if not os.path.isfile(os.path.join(date_dir_path, item))]
            
            for time_dir in time_dirs:
                
                time_dir_path = os.path.join(date_dir_path, time_dir)
                zipped_files = [item for item in os.listdir(time_dir_path) if os.path.isfile(os.path.join(time_dir_path, item))]

                for zipped_file in zipped_files:
                    if zipped_file.endswith(".json"):
                        zipped_file_path = os.path.join(time_dir_path, zipped_file)
                        print "Dumping: " + zipped_file_path
                        os.system("mongoimport --db {} --collection {} ".format(mongo_db, mongo_collection) + zipped_file_path)      

download()   
extract_tar()
extract()
dump()