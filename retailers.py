import math

class retailer():
    def __init__(self, name, URL, favorite=False):
        self.info = {
            "name" : name,
            "URL" : URL,
            "favorite" : favorite
        }
    
    def get_info(self):
        return self.info

    def add_stock(self):
        pass

    def remove_stock(self):
        pass

    def update_stock(self):
        pass

    def get_stock(self):
        pass

    def update_favorite(self, status):
        self.info["favorite"] = status

class retailers(dict):
    def __init__(self,*arg,**kw):
        super(retailers, self).__init__(*arg, **kw)

    def add_retailer(self, name, URL):
        new_retailer = {name.lower() : retailer(name, URL)}
        self.update(new_retailer)
        return

    def get_retailer(self, retailer):
        if self.get(retailer.lower()):
            return self[retailer.lower()]
        else:
            return 0

    def add_favorite(self, retailer):
        retailer = retailer.lower()
        if self.get(retailer):
            for name in self.keys():
                retail_info = self.get_retailer(name).get_info()
                if retail_info["favorite"]:
                    self.get_retailer(name).update_favorite(False)
            self.get_retailer(retailer).update_favorite(True)
            return "Favorite updated"
        else:
            return "This retailer does not exist"
    

if __name__ == '__main__':
    # retails = retailers()

    # retails.add_retailer("Home Depot", "homedepot.ca")
    # retails.add_retailer("Rona", "rona.ca")

    # if retails.get_retailer("rona"):
    #     rona = retails.get_retailer("rona")
    #     print(rona.get_info())
    
    # homedepot = retails.get_retailer("home depot")
    # print(homedepot.get_info(), "\n")
    
    # #print(retails.items())

    # retails.add_favorite("rona")

    # print(rona.get_info())
    # print(homedepot.get_info(), "\n")

    # retails.add_favorite("home depot")

    # print(rona.get_info())
    # print(homedepot.get_info())
