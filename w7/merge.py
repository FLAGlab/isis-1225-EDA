import recursivesinglelinkedlistv3 as List

def merge_sort(list):
    size = List.size(list)
    mid = size //2 
    if size == 1:
        return list
    else:
        l = sublist(list, 0, mid)
        r = sublist(list, mid+1, size)

        l_ord = merge_sort(l)
        r_ord = merge_sort(r)

        return order(l_ord, r_ord)


def order(l1, l2):
    def order_iter(l1, l2, res):
        if List.head(l1) == None and List.head(l2) == None:
            return List.reverse(res)
        elif List.head(l1) == None:
            return List.appen(List.reverse(res), l2)
        elif List.head(l2) == None:
            return List.append(List.reverse(res), l1)
        else:
            e1 = List.head(l1)
            e2 = List.head(l2)
            if e1 <= e2:
                res = List.cons(res, e1)
                return order_iter(List.tail(l1), l2, res)
            else:
                res = List.cons(res, e2)
                return order_iter(l1, List.tail(l2), res)
    return order_iter(l1, l2, List.create_list())



def sublist(list, init, end):
    def partir_iter(list, count, res):
        if count == end:
            return List.reverse(res)
        elif count < init:
            return (List.tail(list), count + 1, res)
        else:
            res = List.cons(res, List.head(list))
            count += 1
            return partir_iter(List.tail(list), count, res)
    return partir_iter(list, 0, List.create_list())