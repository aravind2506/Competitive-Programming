def check(s1, s2):
    s1=s1.lower()
    s2=s2.lower()
    s1=s1.replace(" ", "")
    s2=s2.replace(" ", "")
    if(sorted(s1)== sorted(s2)):
        print("True") 
    else:
        print("False")     

s1 ="anagram"
s2 ="nagaram"
s3="Keep"
s4="Peek"
s5="Mother In Law"
s6="Hitler Woman"
s7="School Master"
s8="The Classroom"
s9="ASTRONOMERS"
s10="NO MORE STARS"
s11="Toss"
s12="Shot"
check(s1, s2)
check(s3, s4)
check(s5, s6)
check(s7, s8)
check(s9, s10)
check(s11, s12)
check("joy", "enjoy")
check("Debit Card", "Bad Credit")
check("SiLeNt CAT", "LisTen AcT")
check("Dormitory", "Dirty Room")



# Test case1: anagram, nagaram – true 
# Test case2: Keep, Peek – true 
# Test case3: Mother In Law, Hitler Woman – true 
# Test case4: School Master, The Classroom – true 
# Test case5: ASTRONOMERS, NO MORE STARS – true 
# Test case6: Toss, Shot – false 
# Test case7: joy, enjoy – false 
# Test case8: Debit Card, Bad Credit – true 
# Test case9: SiLeNt CAT, LisTen AcT – true 
# Test case10: Dormitory, Dirty Room – true 