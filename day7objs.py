class ListNodes():
    def __init__(self, name, parent=False):
        self.name = name
        self.contents = []
        self.parent = parent
        self.size = 0

    def additem(self, item):
        info = item.split(' ')
        if info[0] == 'dir':
            self.contents.append(ListNodes(info[1], self))
        else:
            self.contents.append(info)

    def getParent(self):
        if self.parent:
            return self.parent

    def fetch(self, name):
        for item in self.contents:
            print(str(type(item)))
            if type(item) == type(ListNodes('f')):
                if item.name == name:
                    return item

    def setsizeofme(self):
        total = 0
        for item in self.contents:
            print(str(type(item)))
            if type(item) == type(ListNodes('f')):
                total = total + item.setsizeofme()
            else:
                total = total + int(item[0])

        self.size = total
        return total

    def FindNodesUnderSize(self, size, passlist):
        if self.size <= size:
            passlist.append(self)

        for item in self.contents:
            if type(item) == type(ListNodes('f')):
                item.FindNodesUnderSize(size, passlist)

        return passlist

    def FindOverSize(self, size, passlist):
        if self.size >= size:
            passlist.append(self)

        for item in self.contents:
            if type(item) == type(ListNodes('f')):
                item.FindOverSize(size, passlist)

        return passlist






