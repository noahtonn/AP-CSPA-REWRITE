itemName = ["2pk black ballpoint pen", "3pk black blue red variety pens",
    "latex free pink eraser", "3pk high-polymer eraser", "15pk rainbow gel pens",
    "steel mechanical pencil with extra led and erasers", "20pk multicolor mechanical pencils",
    "white out liquid", "white out strips", "10pk rainbow variety mini - highlighters", 
    "10pk type 2 pencils", "3pk pink yellow orange highlighters", "3 inch binder",
    "2 inch binder", "1.5 inch binder", "2pk 3 inch binder", "bass boosted earbuds"]
itemTypes = ["Pens", "Erasers", "Mechanical Pencils", "Pencils", "Highlighters", "Binders", "Electronics"]
itemTypeNumbers = [0, 0, 1, 1, 0, 2, 2, 1, 1, 4, 3, 4, 5, 5, 5, 5, 6]
itemPrice = [5.99, 7.99, 1.99, 4.99, 9.99, 4.59, 8.99, 3.99, 3.49, 11.99, 4.99, 5.99, 4.99, 4.59, 3.99, 7.99, 9.99] 

def main():
    search = Search(input("Welcome to The School Supply Store, please enter your search: \n"))
    search.Search()
    Inrepeat = True
    while Inrepeat:
        search.displayTopFive()
        choice = OrderChoice()
        if choice < 6:
            search.completeOrder(choice)
            Inrepeat = False
        else:
            search.sortOrder(choice)


class Search:
    itemWeight = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    topFiveItem = ["", "", "", "", ""]

    def __init__(self, query):
        self.query = query

    def Search(self):
        userSearchSep = self.query.split()
        #For each item in database
        for x in range (0, len(itemName)):
            #Seperates current by word.
            currentCompare = itemName[x].split()
            #For each word in current.
            for y in range (0, len(currentCompare)):
                #For each word in user search
                for i in range (0, len(userSearchSep)):
                    currentUserSearch = userSearchSep[i]
                    #If current words are equivalent
                    if currentUserSearch == currentCompare[y]:
                        #Add 100 to weight
                        self.itemWeight[x] += 100
        #Removes spaces between words
        userSearchCondense = self.query.replace(" ", "")
        #For each item in database
        for y in range(0, len(itemName)):
            #Removes spaces between words
            currentCompareCondense = itemName[y].replace(" ", "")
            #For each character in compare
            for x in range(0, len(currentCompareCondense)):
                #For each character in user search
                for i in range(0, len(userSearchCondense)):
                    #If characters in user search and compare are equivalent
                    if userSearchCondense[i] ==  currentCompareCondense[x]:
                        #Add 1 to weight
                        self.itemWeight[y] += 1
        itemWeightDelete = self.itemWeight.copy()
        itemWeightCopy = self.itemWeight.copy()
        itemWeightCopy.sort(reverse = True)
        for x in range(0, len(self.topFiveItem)):
            self.topFiveItem[x] = itemName[itemWeightDelete.index(itemWeightCopy[x])]
            itemWeightDelete.pop(itemWeightDelete.index(itemWeightCopy[x]))

    def displayTopFive(self):
        for x in range(0, len(self.topFiveItem)):
                y = x + 1
                print(y, ". " + self.topFiveItem[x].title() + " - ", itemPrice[itemName.index(self.topFiveItem[x])])

    def completeOrder(self, index):
        print("Your order of " + self.topFiveItem[index - 1] + " will cost $", itemPrice[itemName.index(self.topFiveItem[index - 1])], "\nThanks for your order, have a good day") 
    
    def getTopFiveItem(self):
        return self.topFiveItem
    
    def sortOrder(self, sortType):
        if sortType == 6:
            topFivePrice = ["", "", "", "", ""]
            for x in range(0, len(self.topFiveItem)):
                topFivePrice[x] = itemPrice[itemName.index(self.topFiveItem[x])]
            topFivePriceCopy = topFivePrice.copy()
            topFivePriceCopy.sort()
            topFiveItemCopy = self.topFiveItem.copy()
            for y in range(0, len(self.topFiveItem)):
                self.topFiveItem[y] = topFiveItemCopy[topFivePrice.index(topFivePriceCopy[y])]
                topFivePrice[topFivePrice.index(topFivePriceCopy[y])] = 0
        else:
            for y in range(0, len(itemTypes)):
                print(y + 1, ". " + itemTypes[y])
            type  = int(input("Please enter the number corresponding to the desired item type: \n")) - 1
            if 0 < type < 8:
                typePopCount = 0
                for x in range(0, 5):
                    if itemTypeNumbers[itemName.index(self.topFiveItem[x - typePopCount])] != type:
                        self.topFiveItem.pop(x - typePopCount)
                        typePopCount+=1

def OrderChoice():
    repeat = True
    while repeat:
        response = int(input("Please enter the number corresponding to your selection, if you would like to sort; enter 0: \n"))
        if 0 < response < 6:
            return response
        elif response == 0:
            sortRepeat = True
            if sortRepeat:
                sortType = int(input("Please enter 6 for price sorting, or 7 for type sorting: \n"))
                if sortType == 6 or sortType == 7:
                    return sortType

main()