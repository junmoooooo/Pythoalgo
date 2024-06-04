heap =['최소합']

def heap_pop():
    if len(heap) == 1:
        print('힙이 비어 있어서 삭제가 불가능 합니다.')
        return

    result = heap[1]
    heap[1] = heap[-1]
    heap.pop()

    parent = 1
    child = parent * 2

    if child + 1 <= len(heap)-1:
        if heap[child] > heap[child+1]:
            child += 1

    while child <= len(heap)-1 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent*2
        if child +1 <= len(heap) -1 :
            if heap[child] > heap[child-1]:
                child +=1

    return result
