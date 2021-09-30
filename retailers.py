class retailer():
    def __init__(self, name, URL, favorite=False):
        self.info = {
            "name" : name,
            "URL" : URL,
            "favorite" : favorite
        }
        self.stock = {}
    
    def get_info(self):
        return self.info

    def get_stock(self):
        return self.stock
    
    def get_category(self, category):
        if self.stock.get(category):
            return self.stock[category]
        else:
            return "Category not found"

    def add_stock(self, category, length, price):
        if self.stock.get(category):
            stocks = self.stock.get(category)
            for len in stocks:
                if len[0] is length:
                    stocks.remove(len)
                    break
            stocks.append((length, price))
            self.stock.update({category : stocks})
        else:
            new_stock = {category : [(length, price)]}
            self.stock.update(new_stock)
    
    def remove_stock(self, category):
        if self.stock.get(category):
            self.stock.pop(category)
        else:
            return "Category not found"

    def remove_length(self, category, length):
        if self.stock.get(category):
            stocks = self.stock.get(category)
            for len in stocks:
                if len[0] is length:
                    stocks.remove(len)
                    self.stock.update({category : stocks})
                    break
                else:
                    return "Length not found"
        else:
            return "Category not found"

    def clear_stock(self):
        self.stock = {}

    def update_price(self):
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
    
    #print(retails.items())

    # retails.add_favorite("rona")

    # print(rona.get_info())
    # print(homedepot.get_info(), "\n")

    # retails.add_favorite("home depot")

    # print(rona.get_info())
    # print(homedepot.get_info(), "\n")

    # rona.add_stock("2x4", 10, 3.50)
    # print("Rona 2x4 stocks are: ", rona.get_category("2x4"))
    
    # rona.add_stock("2x4", 12, 4.25)
    # print("Rona 2x4 stocks are: ", rona.get_category("2x4"))

    # rona.add_stock("2x6", 12, 4.50)
    # print("Rona 2x6 stocks are: ", rona.get_category("2x6"))

    # print("Rona's stock is: ", rona.get_stock())
    # rona.clear_stock()
    # print("Rona's stock is: ", rona.get_stock())
