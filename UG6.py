class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None


    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

    def insert_head(self, no_rekening, nama, saldo=0):
        new_node = NodeTabungan(no_rekening, nama, saldo)
        if self._size == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            self._size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self._size += 1

    def delete_head(self):
        if self._size == 0:
            return False
        elif self._size == 1:
            baru = self.head
            self.head = None
            self.tail = None
            del baru
            self._size = self._size - 1
            return True
        else:
            baru = self.head
            self.head = self.head.next
            self.tail.next = self.head
            del baru
            self._size = self._size - 1
            return True

    def print(self):
        if self._size == 0:
            print('Linked List is empty')
        else:
            baru = self.head
            while(baru!=self.tail.next):
                print('Norek: ', baru.no_rekening)
                print('Nama: ', baru.nama)
                print('Saldo: ', baru.saldo)
                baru = baru.next
                print('Norek: ', baru.no_rekening)
                print('Nama: ', baru.nama)
                print('Saldo: ', baru.saldo) 
            print()
        print("rekening")

slnc=SLNC()
slnc.insert_head(201,"Hanif", 250000)
slnc.insert_head(110,"Yudha", 150000)
slnc.print()