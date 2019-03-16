
import time
import json

class activity:
    def __init__(self):
        self.start=-1
        self.end=-1
        self.strStart=""
        self.strEnd=""
        self.project="undifined"
        self.user="Sami"
        self.comments=""
        self.jsonfilename="./data/activities.json"

    def start_act(self):
        self.start =  time.time()
        self.strStart= time.strftime("%H:%M:%S - %a %d %b")
    def end_act(self):
        self.end = time.time()        
        self.strEnd= time.strftime("%H:%M:%S - %a %d %b")
    def elapsed(self):
        elapsed='%.2f'%(self.end - self.start)
        return elapsed
    
    def export2json(self):
        with open(self.jsonfilename, 'w+') as outfile:
            data={}            
            data["Start"]   =self.strStart
            data["End"]     =self.strEnd
            data["Elapsed"] =self.elapsed()            
            data["User"]    =self.user
            data["Comments"]=self.comments
            data["Project"] =self.project
            #jdata=json.dumps(data,indent=4, sort_keys=True)
            json.dump(data,outfile,indent=4, sort_keys=True)


