a=[
          [2],
         [9,7],
        [8,4,2],
       [2,5,7,4],
      [1,8,4,6,4],
     [7,8,6,1,4,8],
    [1,5,8,9,3,3,8],
   [7,2,9,5,4,8,8,1],
  [4,7,1,7,5,3,1,1,4]
]

def minipath(a,level,index):
    height=len(a)
    if level==height-1:
        return a[level][index]
    else:
        i=minipath(a,level+1,index)
        j=minipath(a,level+1,index+1)
        if i<j:
            return i+a[level][index]
        else:
            return j+a[level][index]

print(minipath(a,0,0))