print("select any two prefered subjects :\n1.maths\n2.programming\n3.physics\n4.electrical\n5.chemistry\n6.biology\n8.statastics")

sub1=int(input("enter the first subject:"))
sub2=int(input("enter the second subject:"))

if(sub1==1 and sub2==2):
    print("career suggested:computer engineering")
if(sub1==3 and sub2==4):
    print("career suggested:electrical engineering")
if(sub1==5 and sub2==6):
    print("career suggested:biotechnology")
if(sub1==2 and sub2==8):
    print("career suggested:AIDS")     
