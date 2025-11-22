from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, inp):
        self.data = DoublyLinkedList()
        for ch in inp:
            if ch.isdigit():
                self.data.add_last(int(ch))

    def __add__(self, othr):
        res = Integer('')
        cur1 = self.data.trailer.prev
        cur2 = othr.data.trailer.prev
        car = 0
        while cur1 is not self.data.header or cur2 is not othr.data.header or car:
            v1 = cur1.data if cur1 is not self.data.header else 0
            v2 = cur2.data if cur2 is not othr.data.header else 0
            tot = v1 + v2 + car
            res.data.add_first(tot % 10)
            car = tot // 10
            if cur1 is not self.data.header:
                cur1 = cur1.prev
            if cur2 is not othr.data.header:
                cur2 = cur2.prev
        return res

    def __repr__(self):
        if self.data.is_empty():
            return '0'
        out = ''
        cur = self.data.header.next
        lead = True
        while cur is not self.data.trailer:
            if lead and cur.data == 0:
                cur = cur.next
                continue
            lead = False
            out += str(cur.data)
            cur = cur.next
        return out if out else '0'

    def __mul__(self, othr):
        # inline zero checks
        if self.data.is_empty() or othr.data.is_empty():
            return Integer('0')
        isz = True
        nd = self.data.header.next
        while nd is not self.data.trailer:
            if nd.data != 0:
                isz = False
                break
            nd = nd.next
        if isz:
            return Integer('0')
        isz = True
        nd = othr.data.header.next
        while nd is not othr.data.trailer:
            if nd.data != 0:
                isz = False
                break
            nd = nd.next
        if isz:
            return Integer('0')

        res = Integer('0')
        curo = othr.data.trailer.prev
        ppos = 0
        while curo is not othr.data.header:
            mld = curo.data
            part = Integer('')
            car = 0
            curs = self.data.trailer.prev
            while curs is not self.data.header or car:
                sd = curs.data if curs is not self.data.header else 0
                prod = sd * mld + car
                part.data.add_first(prod % 10)
                car = prod // 10
                if curs is not self.data.header:
                    curs = curs.prev
            for _ in range(ppos):
                part.data.add_last(0)
            res = res + part
            curo = curo.prev
            ppos += 1
        return res

