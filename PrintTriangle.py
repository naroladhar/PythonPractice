def printTriangle(nrows):
    '''
    objective: to print triangle
    input variables:
          nrows: number of lines to be printed
    output variables:
          * : character to print out
    return value: none
    '''
    for i in range(1,nrows+1):
        for j in range(0,i):
            print('*',end=" ")
        print("")        
def printreverseTraingle(nrows):
    '''
    objective: to print triangle
    input variables:
          nrows: number of lines to be printed
    output variables:
          * : character to print out
    return value: none
    '''
    for i in range(1,nrows):
        print('*' * (nrows-i))

def printtriangle(nrows):
    '''
    objective: to print triangle
    input variables:
          nrows: number of lines to be printed
    output variables:
          * : character to print out
    return value: none
    '''
    for i in range(1,nrows):
        print("\n")
        for j in range(1,i):
          print(j,end=" ")
    
def _printtriangle_(nrows):
    '''
    objective: to print triangle
    input variables:
          nrows: number of lines to be printed
    output variables:
          * : character to print out
    return value: none
    '''
    for i in range(0,nrows):
        print("\n")
        for j in range(0,i):
          print(i,end=" ")
          
def _printtriangletrial_(nrows):
    '''
    objective: to print triangle
    input variables:
          nrows: number of lines to be printed
    output variables:
          * : character to print out
    return value: none
    '''
    for i in range(1,nrows+1):
        print("\n")
        for j in range(i,nrows+1):
          print(i,end=" ")

'''         
def print_triangle(nrows):
    '''
    '''
    objective: to print triangle
    input variables:
          nrows: number of lines to be printed
    output variables:
          * : character to print out
    return value: none
    '''
    '''
    for i in range(1,nrows)
        for j in range(0,j)
'''            
