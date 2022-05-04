print("              WELCOME TO EXPERT SYSTEM          ")
print("              -------------------------------------")
print("            THIS EXPERT SYSTEM IS USED TO ORGANIZE CONFERENCES        ")
print("         ------------------------------------------------------------------")
a=[]
d=[]
print("DECIDE ON THEME")
print("1.TELECOMMUNICATIONS")
print("2.AUTOMOBILES")
print("3.ROBOTICS")
print("4.ARTIFICIAL INTELLIGENCE")
print("5.CYBER SECURITY")
print("Select a topic for conference")
n1=int(input())
if n1==1:
    print("ASSEMBLE YOUR TEAM")
    print("enter the no of team members for telecommunications")
    n2=int(input())
    print("Enter names of team members")
    while(n2>0):
        n3=input()
        a.append(n3)
        n2-=1
    print("Your BUDGET for Organizing Conferenece")
    n4=int(input())
    u=0
    sponsors={
        "TELENOR":"10000-25000",
        "MOBILINK":"25001-50000",
        "UFONE":"50001-70000"
        }
    for x in sponsors:
        r,l=sponsors[x].split("-")
        r=int(r)
        l=int(l)
        if n4>=r and n4<=l:
            u=1
            print("This company is ready to sponsor your conference")
            print(x)
            spon=x
            print("are you interested (Y/N)")
            z=input()
            if z=='N':
                print(" OH! ITS GREAT YOU ARE A SELF SPONSOR")
            else:
                print("OK! COMPANY IS READY TO SPONSOR YOUR CONFERENCE")
    if u==0:
      print("No company sponsered")
            
    print("enter the no.of days to organize this conference")
    n5=int(input())
    print("enter the starting date of the conference")
    e=input()
    print("choose your venue")
    print("1.SUBHAM CONVENTIONS")
    print("2.SIDDHARTHA GARDENS")
    print("3.BANDLAMUDI GARDENS")
    print("4.LIONS CLUB,GUNTUR")
    f=int(input())
    print("choose the catering")
    print("1.ANNAPURNA CATERINGS")
    print("2.RAMU CATERINGS")
    p=int(input())
    print("enter the no.of Speakers")
    b=int(input())
    print("LINE UP YOUR SPEAKERS")
    while(b>0):
        c=input()
        d.append(c)
        b-=1
    print("----------------------------------------------")
    print(" YOUR THEME IS TELECOMMUNICATIONS")
    print("YOUR TEAM")
    print(a)
    print("BUDGET IS")
    print(n4)
    print("YOUR SPONSOR IS")
    print(spon)
    print("STARTING DATE OF CONFERENCE IS")
    print(e)
    print("VENUE FOR CONFERENCE IS")
    if(f==1):
        print("SUBHAM CONVENTIONS")
    elif(f==2):
         print("SIDDHARTHA GARDENS")
    elif(f==3):
        print("BANDLAMUDI GARDENS")
    elif (f==4):
        print("LIONS CLUB,GUNTUR")
    else:
        print("SORRY! NO VENUE")
    print("CATERING FOR YOUR CONFERENCE IS")
    if(p==1):
        print("ANNAPURNA CATERINGS")
    elif(p==2):
        print("RAMU CATERINGS")
    else:
        print("NO CATERING")
    print("YOUR SPEAKERS ARE")
    print(d)    
elif n1==2:
    print("ASSEMBLE YOUR TEAM")
    print("enter the no of team members for automobiles")
    n2=int(input())
    print("Enter names of team members")
    while(n2>0):
        n3=input()
        a.append(n3)
        n2-=1
    print("Your BUDGET for Organizing Conferenece")
    n4=int(input())
    u=0
    sponsors={
        "TATA MOTORS":"10000-25000",
        "MAHINDRA":"25000-50000",
        "TOYOTA":"50000-70000"
        }
    for x in sponsors:
        r,l=sponsors[x].split("-")
        r=int(r)
        l=int(l)
        if n4>=r and n4<=l:
            u=1
            print("The company is ready to sponsor your conference")
            print(x)
            spon=x
            print("are you interested (Y/N)")
            z=input()
            if z=='N':
                print("OH! ITS GREAT YOU ARE A SELF SPONSOR")
            else:
                print("OK! COMPANY IS READY TO SPONSOR YOUE CONFERENCE")
    if u==0:
        print("No company sponsered")
        print("enter the no.of days to organize this conference")
    n5=int(input())
    print("enter the starting date of the conference")
    e=input()
    print("choose your venue")
    print("1.SUBHAM CONVENTIONS")
    print("2.SIDDHARTHA GARDENS")
    print("3.BANDLAMUDI GARDENS")
    print("4.LIONS CLUB,GUNTUR")
    f=int(input())
    print("choose the catering")
    print("1.ANNAPURNA CATERINGS")
    print("2.RAMU CATERINGS")
    p=int(input())
    print("enter the no.of Speakers")
    b=int(input())
    print("LINE UP YOUR SPEAKERS")
    while(b>0):
        c=input()
        d.append(c)
        b-=1
    print("----------------------------------------------")
    print(" YOUR THEME IS AUTOMOBILES")
    print("YOUR TEAM")
    print(a)
    print("BUDGET IS")
    print(n4)
    print("YOUR SPONSOR IS")
    print(spon)
    print("STARTING DATE OF CONFERENCE IS")
    print(e)
    print("VENUE FOR CONFERENCE IS")
    if(f==1):
        print("SUBHAM CONVENTIONS")
    elif(f==2):
         print("SIDDHARTHA GARDENS")
    elif(f==3):
        print("BANDLAMUDI GARDENS")
    elif (f==4):
        print("LIONS CLUB,GUNTUR")
    else:
        print("SORRY! NO VENUE")
    print("CATERING FOR YOUR CONFERENCE IS")
    if(p==1):
        print("ANNAPURNA CATERINGS")
    elif(p==2):
        print("RAMU CATERINGS")
    else:
        print("NO CATERING")
    print("YOUR SPEAKERS ARE")
    print(d)    
    
elif n1==3:
    print("ASSEMBLE YOUR TEAM")
    print("enter the no of team members for ROBOTICS")
    n2=int(input())
    print("Enter names of team members")
    while(n2>0):
        n3=input()
        a.append(n3)
        n2-=1
    print("Your BUDGET for Organizing Conference")
    n4=int(input())
    u=0
    sponsors={
        "FETCH ROBOTICS":"10000-25000",
        "GPS":"25001-50000",
        "BLUE ROBOTICS":"50001-70000"
        }
    for x in sponsors:
        r,l=sponsors[x].split("-")
        r=int(r)
        l=int(l)
        if n4>=r and n4<=l:
            u=1
            print("The company is ready to sponsor your conference")
            print(x)
            spon=x
            print("are you interested (Y/N)")
            z=input()
            if z=='N':
                print("OH! ITS GREAT YOU ARE A SELF SPONSOR")
            else:
                print("OK! COMPANY IS READY TO SPONSOR YOUE CONFERENCE")
    if u==0:
      print("No company sponsered")
    print("enter the no.of days to organize this conference")
    n5=int(input())
    print("enter the starting date of the conference")
    e=input()
    print("choose your venue")
    print("1.SUBHAM CONVENTIONS")
    print("2.SIDDHARTHA GARDENS")
    print("3.BANDLAMUDI GARDENS")
    print("4.LIONS CLUB,GUNTUR")
    f=int(input())
    print("choose the catering")
    print("1.ANNAPURNA CATERINGS")
    print("2.RAMU CATERINGS")
    p=int(input())
    print("enter the no.of Speakers")
    b=int(input())
    print("LINE UP YOUR SPEAKERS")
    while(b>0):
        c=input()
        d.append(c)
        b-=1
    print("----------------------------------------------")
    print(" YOUR THEME IS ROBOTICS")
    print("YOUR TEAM")
    print(a)
    print("BUDGET IS")
    print(n4)
    print("YOUR SPONSOR IS")
    print(spon)
    print("STARTING DATE OF CONFERENCE IS")
    print(e)
    print("VENUE FOR CONFERENCE IS")
    if(f==1):
        print("SUBHAM CONVENTIONS")
    elif(f==2):
         print("SIDDHARTHA GARDENS")
    elif(f==3):
        print("BANDLAMUDI GARDENS")
    elif (f==4):
        print("LIONS CLUB,GUNTUR")
    else:
        print("SORRY! NO VENUE")
    print("CATERING FOR YOUR CONFERENCE IS")
    if(p==1):
        print("ANNAPURNA CATERINGS")
    elif(p==2):
        print("RAMU CATERINGS")
    else:
        print("NO CATERING")
    print("YOUR SPEAKERS ARE")
    print(d)    
elif n1==4:
    print("ASSEMBLE YOUR TEAM")
    print("enter the no of team members for ARTIFICIAL INTELLIGENCE")
    n2=input()
    n2=int(n2)
    print("Enter names of team members")
    while(n2>0):
        n3=input()
        a.append(n3)
        n2-=1
    print("Your BUDGER for Organizing Conference")
    n4=int(input())
    u=0
    sponsors={
        "CLOUD MINDS":"10000-25000",
        "DEEP MIND":"25001-50000",
        "AI BRAIN":"50001-70000"
        }
    for x in sponsors:
        r,l=sponsors[x].split("-")
        r=int(r)
        l=int(l)
        if n4>=r and n4<=l:
            u=1
            print("The company is ready to sponsor your conference")
            print(x)
            spon=x
            print("are you interested (Y/N)")
            z=input()
            if z=='N':
                print("OH! ITS GREAT YOU ARE A SELF SPONSOR")
            else:
                print("OK! COMPANY IS READY TO SPONSOR YOUR CONFERENCE")
    if u==0:
        print("No company sponsered")
        
            
    print("enter the no.of days to organize this conference")
    n5=int(input())
    print("enter the  starting date of the conference")
    e=input()
    print("choose your venue")
    print("1.SUBHAM CONVENTIONS")
    print("2.SIDDHARTHA GARDENS")
    print("3.BANDLAMUDI GARDENS")
    print("4.LIONS CLUB,GUNTUR")
    f=int(input())
    print("choose the catering")
    print("1.ANNAPURNA CATERINGS")
    print("2.RAMU CATERINGS")
    p=int(input())
    print("enter the no.of Speakers")
    b=int(input())
    print("LINE UP YOUR SPEAKERS")
    while(b>0):
        c=input()
        d.append(c)
        b-=1
    print("----------------------------------------------")
    print(" YOUR THEME IS ARTIFICIAL INTELLIGENCE")
    print("YOUR TEAM")
    print(a)
    print("BUDGET IS")
    print(n4)
    print("YOUR SPONSOR IS")
    print(spon)
    print(" STARTING DATE OF CONFERENCE IS")
    print(e)
    print("VENUE FOR CONFERENCE IS")
    if(f==1):
        print("SUBHAM CONVENTIONS")
    elif(f==2):
         print("SIDDHARTHA GARDENS")
    elif(f==3):
        print("BANDLAMUDI GARDENS")
    elif (f==4):
        print("LIONS CLUB,GUNTUR")
    else:
        print("SORRY! NO VENUE")
    print("CATERING FOR YOUR CONFERENCE IS")
    if(p==1):
        print("ANNAPURNA CATERINGS")
    elif(p==2):
        print("RAMU CATERINGS")
    else:
        print("NO CATERING")
    print("YOUR SPEAKERS ARE")
    print(d)    
elif n1==5:
    print("ASSEMBLE YOUR TEAM")
    print("enter the no of team members for CYBER SECURITY")
    n2=input()
    n2=int(n2)
    print("Enter names of team members")
    while(n2>0):
        n3=input()
        a.append(n3)
        n2-=1
    print("Your BUDGET for Organizing Conference")
    n4=int(input())
    u=0
    sponsors={
        "SYMANTEC":"10000-25000",
        "CHECK POINT":"25001-50000",
        "CISCO":"50001-70000"
        }
    for x in sponsors:
        r,l=sponsors[x].split("-")
        r=int(r)
        l=int(l)
        if n4>=r and n4<=l:
            u=1
            print("The company is ready to sponsor your conference")
            print(x)
            spon=x
            print("are you interested (Y/N)")
            z=input()
            if z=='N':
                print("OH! ITS GREAT YOU ARE A SELF SPONSOR")
            else:
                print("OK! COMPANY IS READY TO SPONSOR YOUR CONFERENCE")
    if u==0:
        print("No company sponsered")
        

    print("enter the no.of days to organize this conference")
    n5=int(input())
    print("enter the starting date of the conference")
    e=input()
    print("choose your venue")
    print("1.SUBHAM CONVENTIONS")
    print("2.SIDDHARTHA GARDENS")
    print("3.BANDLAMUDI GARDENS")
    print("4.LIONS CLUB,GUNTUR")
    f=int(input())
    print("choose the catering")
    print("1.ANNAPURNA CATERINGS")
    print("2.RAMU CATERINGS")
    p=int(input())
    print("enter the no.of Speakers")
    b=int(input())
    print("LINE UP YOUR SPEAKERS")
    while(b>0):
        c=input()
        d.append(c)
        b-=1
    print("----------------------------------------------")
    print(" YOUR THEME IS CYBER SECURITY")
    print("YOUR TEAM")
    print(a)
    print("BUDGET IS")
    print(n4)
    print("YOUR SPONSOR IS")
    print(spon)
    print(" STARTING DATE OF CONFERENCE IS")
    print(e)
    print("VENUE FOR CONFERENCE IS")
    if(f==1):
        print("SUBHAM CONVENTIONS")
    elif(f==2):
         print("SIDDHARTHA GARDENS")
    elif(f==3):
        print("BANDLAMUDI GARDENS")
    elif (f==4):
        print("LIONS CLUB,GUNTUR")
    else:
        print("SORRY! NO VENUE")
    print("CATERING FOR YOUR CONFERENCE IS")
    if(p==1):
        print("ANNAPURNA CATERINGS")
    elif(p==2):
        print("RAMU CATERINGS")
    else:
        print("NO CATERING")
    print("YOUR SPEAKERS ARE")
    print(d)    
