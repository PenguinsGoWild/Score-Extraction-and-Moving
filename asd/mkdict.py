import os
import re

class GenDict:

    def __init__(self):
        cwd = os.getcwd()
        self.path = os.path.join(cwd, "Template")


    def readFiles(self):
        dir_list = os.listdir(self.path)
        return dir_list

    def generate(self, filein):
        set1 = set(filein)
        #print(set1)
        dir_list = self.readFiles()
        og_list = dir_list.copy()
        for i in range(0, len(dir_list)):
            dir_list[i] = dir_list[i][4:]
        #print(dir_list)
        dic = {}
        for name in set1:
            matched = False
            for instrument in range(len(dir_list)):
                if "Bass Clarinet" in name:
                    dic[name] = "04. Clarinet"
                    matched = True
                elif "Bass Trombone" in name:
                    dic[name] = "08. Trombone"
                    matched = True
                elif "Bass Drum" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Baritone Saxophone" in name:
                    dic[name] = "05. Saxophone"
                    matched = True
                elif "Bassoon" in name:
                    dic[name] = "03. Bassoon"
                    matched = True
                elif "Baritone" in name:
                    dic[name] = "09. Euphonium"
                    matched = True
                elif re.search(r'\b' + re.escape(dir_list[instrument]) + r's?\b', name):
                    dic[name] = og_list[instrument]
                    matched = True
                elif "Piccolo" in name:
                    dic[name] = "02. Flute"
                    matched = True
                elif "Horn" in name:
                    dic[name] = "07. French Horn"
                    matched = True
                elif "Electric Guitar" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Glock" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Drum" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Timpani" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Marimba" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Xylophone" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Conductor" in name:
                    dic[name] = "00. Conductor"
                    matched = True
                elif "Full Score" in name:
                    dic[name] = "00. Conductor"
                    matched = True
                elif "Vibraphone" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Mallet" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Cymbal" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Conga" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Tambourine" in name:
                    dic[name] = "12. Percussion"
                    matched = True
                elif "Cornet" in name:
                    dic[name] = "06. Trumpet"
                    matched = True
                elif "Chime" in name:
                    dic[name] = "12. Percussion"
                    matched = True
            if not matched:
                dic[name] = "15. Others"
                                
        return dic

