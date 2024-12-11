class DataConverter:
    data = []
    keys = []
    Model_key = {}

    @classmethod
    def getDataToJsonFromDb(cls, jsonData):
        cls.data = []
        for i in jsonData:
            map = {}
            for j in cls.keys:
                map[j] = i[j]
            cls.data.append(map)


    @classmethod
    def getDataToDbFromJson(cls, jsonData):
        map = {}
        for j in cls.keys:
            map[j] = jsonData[j]
        cls.Model_key = map
        