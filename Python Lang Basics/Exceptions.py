#itemsInCart = 0

#2 items added to itemsInCart

#if itemsInCart != 2: #raise Exception("test case fail : cart count not matching")
  #  pass
#assert(itemsInCart == 2)
#---------------------------------------------------
# try:
#     with open ('file.txt', 'r') as reader:
#         reader.read()
        
# except:
#     print("try catch mechanism")
    
#---------------------------------------------------

try:
    with open ('file.txt', 'r') as reader:
         reader.read()
        
except Exception as e:
    print( e)
    
finally:
    print("cleaning up")