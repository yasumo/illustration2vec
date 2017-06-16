# -*- coding: utf-8 -*-
import json

class MyJson:
    def __init__(self,filePath):
        # jsonデータを読み込んだファイルオブジェクトからPythonデータを作成
        self.f = open(filePath,encoding='utf8')
        self.data = json.load(self.f)

    def getValue(self, key):
      if(key in self.data):
        return self.data[key];
      else:
        #todo ログ
        print("not exist value. key:"+key)
        return key

    def getAllValue(self):
      retArray = []
      for key in self.data:
        retArray.append(self.data[key])
      return retArray

    def close(self):
      # ファイルを閉じる
      self.f.close()


