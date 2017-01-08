# -*- coding: utf-8 -*-
import MyJson
import os
import sys
import re


#++++++++++++++
def convertTag2Array(targetJson,dictionaryJson,initArray):
  retArray = initArray
  for key in targetJson[0]:
    border = 0.7
    if(key is "copyright"):
      border = 0.4
    elif(key is "character"):
      border = 0.5
    for valueArray in targetJson[0][key]:
        key = valueArray[0]
        value = valueArray[1]
        addValue = "["+dictionaryJson.getValue(key)+"]"
        if(value >= border and (addValue not in retArray)):
          retArray.append(addValue)
  return retArray


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def createInitTagArray(rootPath,filePath):
  path = filePath.replace(rootPath,"");
  pattern = r"\[.*?\]"
  text = path
  matchedList = []

  for matched in re.findall(pattern,text):
    #for windows
    matchedList.append(unicode(matched, 'cp932'))

  return matchedList
#++++++++++++++




targetJson = [{'rating': [(u'safe', 0.9786375164985657), (u'explicit', 0.012578213587403297), (u'questionable', 0.00825407262891531)], 'character': [(u'nishikino maki', 0.9992921352386475), (u'yazawa nico', 0.9928505420684814)], 'copyright': [(u'love live! school idol project', 0.9998996257781982)], 'general': [(u'red hair', 0.9775589108467102), (u'multiple girls', 0.9712580442428589), (u'purple eyes', 0.8058084845542908), (u'blush', 0.7864237427711487), (u'red eyes', 0.7253988981246948), (u'short hair', 0.6950022578239441), (u'bow', 0.6548388600349426), (u'food', 0.5972219109535217), (u'hair bow', 0.5430619716644287), (u'2girls', 0.529625654220581), (u'blue eyes', 0.501089870929718)]}]

dictionaryJson = MyJson.MyJson("convert_tag.json")


param = sys.argv
inputDir = param[1]


#++++++++++++++
files = find_all_files(inputDir)
inputFiles=[]

for file in files:
  if(os.path.isfile(file)):
    inputFiles.append(file)
#++++++++++++++

for filePath in inputFiles:
  print("----------------------------")
  print(filePath)
  initArray = createInitTagArray(inputDir,filePath)

  for hoge in convertTag2Array(targetJson,dictionaryJson,initArray):
    print hoge;



