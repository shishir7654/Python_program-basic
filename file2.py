def main():
    #wrie to file
    out=open("test.txt","a")
    for i in range(5):
        inputTOFile =input("Enter string to write to file:")
        out.write("\n{}".format(inputTOFile))
    out.close()
if __name__=='__main__':main()
