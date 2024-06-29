st = input("Enter Message: ")
words = st.split(" ")
# coding = True  # ya encript kerna k liya..
# coding = False  # ya decript kerna k liya....
coding = input("1 for coding or 0 fo decoding: ")
coding =True if (coding=="1") else False
if(coding):
    nwords =[]
    for word in words:
      if(len(word)>=3):
         r1 ="bsf"
         r2 = "jkd"
         stnew = r1+  word[1:] + word[0] + r2
         nwords.append(stnew)
      else:
          nwords.append(word[::-1])
    print(" ".join(nwords))  # join method mai string starting mai ati hai or last mai list ati hai...
else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))