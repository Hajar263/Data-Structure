"""User defined array using oop 
The class has the most common used method the clasic array has
To create a list you have to give it the size of the array and the type of the elements
The created list contain automatically a {size}same elements of the detected data type"""


class ARRAY:
    def __init__(self, Type, size):
        self.Type = Type
        self.size = size
        self.items = self.size * [Type(1)]

    def __str__(self):
        return str(self.items)

    # To access or get a certain element = array[index]
    def Access(self, position):
        return self.items[position]  # O(1)

    # To search for a certain element and return its position if its found = find
    def Search(self, item):
        for i in range(self.size):
            if self.items[i] == item:
                print(f'Found at index : {i}')
                quit()
        else:
            print('Not found')

    # To insert a certain element to a spesific index = append
    def Insert(self, item, position):
        if position < self.size:  # O(1*((n*1)+1))
            for i in range(self.size - 2, position - 1, -1):
                self.items[i + 1] = self.items[i]
            self.items[position] = item
        else:
            print('out of range')

    # To remove a certain index = pop
    def Remove(self, position):
        if position < self.size:  # O(1*(N*1+1))
            for i in range(position, self.size - 1):
                self.items[i] = self.items[i + 1]
            self.items[-1] = 100
        else:
            print('Unvalid Position')


# Test your array class
array = ARRAY(int, 5)
print(array)
print(array.Access(4))
array.Insert(-3, 0)
array.Insert(-2, 1)
array.Insert(-4, 2)
array.Insert(8, 3)
array.Insert(0, 4)
array.Insert(6, 8)
print(array)
array.Insert(22, -2)
print(array)
array.Remove(1)
print(array)