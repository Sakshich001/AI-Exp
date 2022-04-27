import math
from IPython.core.display import ProgressBar
W = [[1.0 , 0.0], [0.1 , 0.9], [0.1, 0.9], [0.01 , 0.99]]
R = [[0.8, 0.2], [0.2, 0.8]]
S = [[0.5 , 0.5] , [0.9, 0.1]]
C = [[0.5, 0.5]]
dag = {'C' :['S', 'R'], 'S' :['W'], 'R' : ['W']}

probS = float(input('Enter probability of S :'))
probC = float(input('Enter probability of C :'))
probSF = 1 - probS
probR = float(input('Enter probability of R :'))
probRF = 1 - probR
probWSR = float(input('Enter probability of W/SR :'))
probWSR_ = float(input('Enter probability of W/SRF :'))
probWS_R = float(input('Enter probability of W/SFR :'))
probWS_R_ = float(input('Enter probability of W/SFRF :'))


probW = probWSR * probS *probR + probWSR_ * probS * probRF + probWS_R * probSF * probR + probWS_R_ * probSF * probRF
print('The probability of wet grass is :', probW)

probA = probW *probRF *probS *probC
print('The probability of the given condition is:', probA)


#Output
#Enter probability of S :0.30
#Enter probability of C :0.50
#Enter probability of R :0.50
#Enter probability of W/SR :0.99
#Enter probability of W/SRF :0.90
#Enter probability of W/SFR :0.90
#Enter probability of W/SFRF :0.00
#The probability of wet grass is : 0.5985
#The probability of the given condition is: 0.044887500000000004
