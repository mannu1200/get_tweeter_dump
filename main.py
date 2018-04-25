import wget
import os
from pipes import quote 

def download():
    for month in range(11,12+1):
        for date in range(0,31+1):
            if(date < 10):
                date = '0' + str(date)
            url = "https://archive.org/download/archiveteam-twitter-stream-2017-11/twitter-stream-2017-{}-{}.tar".format(month, date)
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
    root_dir = os.getcwd() + "/2017/"

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
    root_dir = os.getcwd() + "/2017/"

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
                        os.system("mongoimport --db micromort --collection tweets " + zipped_file_path)      


def dump_old():
    root_dir = os.getcwd()
    dirs = [item for item in os.listdir(root_dir) if not os.path.isfile(os.path.join(root_dir, item))]

    for dir_path in dirs:
        path = root_dir + "/" + dir_path
        path += "/" + os.listdir(path)[0]
        path += "/" + os.listdir(path)[0]
        inner_dirs = [item for item in os.listdir(path) if not os.path.isfile(os.path.join(path, item))]

        for inner_dir in inner_dirs:

            json_files = [item for item in os.listdir(path + "/" + inner_dir) if os.path.isfile(os.path.join(path + "/" + inner_dir, item))]
            for json_file in json_files:
                if json_file.endswith('.json'):
                    pa =  quote(path + "/" + inner_dir + "/" + json_file)
                    print "dumping: " + pa
                    os.system("mongoimport --db micromort --collection tweets " + pa)

download()   
extract_tar()
extract()
dump()