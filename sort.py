class Sort:
    def __init__(self) -> None:
        pass

    def insertionSort(self, arrayToSort):
        # [2,4,1,3,8,6]
        # iterate over this arrayToSort.length amount of times
        for i in range(1, len(arrayToSort)):
            itemToSort = arrayToSort[i]
            indexOfLastSortedItem = i - 1
            while indexOfLastSortedItem >= 0 and arrayToSort[indexOfLastSortedItem] > itemToSort:
                arrayToSort[indexOfLastSortedItem + 1] = arrayToSort[indexOfLastSortedItem]
                indexOfLastSortedItem -= 1
            arrayToSort[indexOfLastSortedItem + 1] = itemToSort
        return arrayToSort

def main():
    myObj = Sort()
    print(myObj.insertionSort([7,4,9,10,34,1,2]))

main()