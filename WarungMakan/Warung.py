class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan

    def getNamaPelanggan(self):
        return self._namaPelanggan

class WarungMakan:
    DEFAULT_CAPACITY = 5
    def __init__(self): #tidak boleh mengganti / menambah metode init
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def dequeue(self): #menghapus data paling depan, dan memajukan urutan data yang dibelangkangnya
        if self.is_empty():
            print("Data kosong!")
        answer = self._data[self._front]
        for i in range(self._size):
            self._data[i] = self._data[i+1]
            self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    def enqueue(self, namaPelanggan): #menambah data ke list
        if self._size == len(self._data):
            self.resizeBy3()
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = namaPelanggan
        self._size += 1

    def resizeBy3(self): #menambah ukuran queue sebesar 3
        WarungMakan.DEFAULT_CAPACITY += 3
        old = self._data
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0
    def printAll(self):
        print("\n=== WarungMakan ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i])
            else:
                print(i+1,end=". ")
                print("Kosong")
# test case program
wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()
wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()
wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()