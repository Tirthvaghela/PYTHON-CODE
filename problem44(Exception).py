while True :
    try : 
        n=int(input("(try- ) please enter values :"))
    except Exception as e:
        print("noot acceptable")
        print("messege : ",e)
    else :
        print("input accepted")
        break
    finally:
        print("(FINAL)")
print("done",n)
