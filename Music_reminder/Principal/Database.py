
import pymongo
import datetime


class mongo:

    def __init__(self) -> None:
        # self.conection=pymongo.MongoClient("mongodb+srv://music_search:@cluster0.hadso.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.conection=pymongo.MongoClient("mongodb+srv://music_search:Reminder@cluster0.hadso.mongodb.net/?retryWrites=true&w=majority")

    def querymusic(self):
        # recive the user to get the info and comapare the tiempstamp of now  with the tiempstamp of the song 
        # Send which songs have been heard 1 year ago or more
        db=self.conection["music_remider"]
        collec_user=db["user"]

        now = datetime.datetime.now()
        years= datetime.timedelta(days=3)
        limitdate=now-years
        print(limitdate)
        
        match={
            "$match":{
                "username":"ivanov"
                }
            }
        lookup = {
            "$lookup": {  
                "from":"history",
                "localField":"username",
                "foreignField":"user",
                "as":"logs"
            }
        }
        filter_Song={
            "$project": {
                
                "name": 1,
                "username":1,
                 "history":{ 
                     "$slice":[{
                "$filter": 
                { 
                    "input": "$logs", 
                    "as": "log", 
                    "cond": { "$lt": [ "$$log.last_played",limitdate ] } 
                     }},
                     3
                     ]
                } 
            }
        }
        pipeline=[
            match,
            lookup,
            filter_Song
        ]
        Songs=[]
        for user in collec_user.aggregate(pipeline):
            
            Songs.append(user["history"])
            number_song=len(user["history"])
            return(user,number_song)

