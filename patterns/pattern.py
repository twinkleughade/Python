# ---------------------------             1               -------------------------
#*    
#**    
#***    
#****    
#*****
'''n=int(input("enter any no"))
i=1
while i<=n:
    print('*'*i +(n-1)*' ')
    i=i+1'''
# -------------------------                 2             ----------------------------
#*****
#****
#***
#**
#*
'''n=int(input("enter any number"))
i=0
while i<n:
    print((n-i)*'*'+' '*i)
    i=i+1'''
#-----------------------------                3            -------------------------------
#*****
# ****
#  ***
#   **
#    *
'''n=int(input("enter any number"))
i=0
while i<n:
    print(' '*i+'*'*(n-i))
    i=i+1'''

#------------------------------              4              ------------------------------------
#    *
#   **
#  ***
# ****
#*****
'''n=int(input("enter any no"))
i=1
while i<=n:
    print((n-i)*' '+ i*'*')
    i=i+1'''

#-------------------------------                   5           ----------------------------------
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
'''n=int(input("enter any no"))
i=1
while i<=n:
    print((n-i)*' '+ i*' *')
    i=i+1'''

#-----------------------------                    6               --------------------------------

n=int(input("enter any no"))
i=1
while i<=n:
    print(i*''+(n-1)*' ')
    i=i+1

#-----------------------------                      7             -------------------------------
#*
#**
#***
#**** 
#*****
#****
#***
#**
#*
'''n=int(input("enter any no"))
i=1
while i<=n:
    print('*'*i +(n-1)*' ')
    i=i+1
i=i-2
while i>0:
    print('*'*i)
    i=i-1'''


#---------------------------------------           8                -------------------------------------------------------
#    *
#   **
#  ***
# ****
#*****
# ****
#  ***
#   **
#    *
'''n=int(input("enter any number"))
i=1
while i<=n:
    print(' '*(n-i)+'*'*i)
    i=i+1
i=i-2
while i>0:
    print((n-i)*' '+'*'*i)
    i=i-1'''

#-----------------------------------------              9             ----------------------------------
# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****
'''n=int(input("enter the number"))
i=n
while i>0:
    print('*'*i)
    i=i-1
i=i+2
while i<=n:
    print('*'*i)
    i=i+1'''



