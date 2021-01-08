def SwapFileData():
    swapFile=input("Enter The names of the files that you want to swap") 
    with open(file1,"r") as a:
     data_a=a.read()
    with open(file1,"w") as a:
     a.write(data_b) 
SwapFileData()