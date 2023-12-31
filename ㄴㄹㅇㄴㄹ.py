arr = ['A', 'B', 'C', 'D', 'E']  #idx
sel = [0, 0, 0]     # sidx

def comvination(idx, sidx):
    if sidx==3:
        print(sel)
        return
    if idx==5:
        return
    
    sel[sidx] = arr[idx]
    comvination(idx+1, sidx+1)
    comvination(idx+1, sidx)

comvination(0,0)

