while True:
    import random
    coin = random.randint(0, 1)
    ans = input("동전 던지기를 계속 하시겠습니까? (yes, no)")

    if ans == 'yes':
        if coin == 0 :
          print("head")
        else :
          print("tail")
    else :
      break