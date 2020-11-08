import time
#method one
#ANSWER=input('type your answer:')
#if ANSWER==ans4:
#   print('correct')
#else:
#   print('wrong')
starttime=time.ctime().split()[3]
print('you have started the test at', starttime)
s1s="according to the world book of records the highes I.Q score is 228\n which was scored by MARILYN VOS SAVANT at 10years, and this\n is not normal, 0.5% of the world population can score \nthis so a mo advanced test is recormaded for you."
ffanz="You have been rewarded etra 5 for good time management so now\n you have %s, congratulations %s"
qn1="1).Which of the answers expresses the meaning of the specified word best ?\n REASSURING."
name=input("Enter your name please :")
instr="Dear \"%s\",\n you only have 9 minutes to be through with the test,\n the results shouldnt offend you GOD is all that matters most,\n it is an I.Q test, it will help you determine the estimate of your I.Q\n simply type the alphabet of the objective you choose for an answer\n have fun getting smarter"
print(instr %(name))
print(qn1)
ans1='compassionate'
ans2='comforting'
ans3='explanatory'
ans4='meddlesome'
#2
Answers="a).%s \nb).%s \nc).%s\nd).%s"
print(Answers % (ans1,ans2,ans3,ans4))
#ranking
mrk=0
#method two
dict={'b':'comforting'}
ANS=input('type your answer:')
if ANS in dict.keys():
    mark1=(mrk+1)
else:
    mark1=(mrk+0)
qn2="2).Which number logically follows the sequence?\n (4 6 9 6 14 6 ......)"
print(qn2)
ans1=6
ans2=17
ans3=19
ans4=21
#3
Answers="a).%s \nb).%s \nc).%s\nd).%s"
print(Answers % (ans1,ans2,ans3,ans4))
dict={'c':19}
ANS=input('type your answer:')
if ANS in dict.keys():
    mark2=(mark1+1)
else:
    mark2=(mark1+0)
qn3="3).Which conclussion follows from the statements with absolute certainity?\n1)Non of the stamp collectors is an architect.\n2)All the drones are stamp collectors"
print(qn3)
ans1='all stamp collectors are architects'
ans2='architects are not drones'
ans3='no stamp collectors are drones'
ans4='some drones are architects'
#2
Answers="a).%s \nb).%s \nc).%s\nd).%s"
print(Answers % (ans1,ans2,ans3,ans4))
#method two
dict={'b':'architects are not drones'}
ANS=input('type your answer:')
if ANS in dict.keys():
    mark3=(mark2+1)
else:
    mark3=(mark2+0)
qn4="4).Whats the correct answer?\nTom has anew set of golf clubs, using club 8, the ball travels an average distance of 100meters,\n using club 7, the ball travels an average distance of 108meters,\n using club 6, the ball travelsan average distance of 114meters.\nHow far will the ball go if club 5 is used by Tom?"
print(qn4)
ans1=122
ans2=120
ans3=118
ans4=116
#3
Answers="a).%s \nb).%s \nc).%s\nd).%s"
print(Answers % (ans1,ans2,ans3,ans4))
dict={'c':118}
ANS=input('type your answer:')
if ANS in dict.keys():
    mark4=(mark3+1)
else:
    mark4=(mark3+0)
qn5="5).Which answer expresses the meaning \"opposite\" of the specified word best?\n TOUGH."
print(qn5)
ans1='cowardly'
ans2='starch'
ans3='strong'
ans4='tender'
ans5='masculine'
#4
Answers="a).%s \nb).%s \nc).%s\nd).%s\ne).%s"
print(Answers % (ans1,ans2,ans3,ans4,ans5))
#method two
dict={'d':'tender'}
ANS=input('type your answer:')
if ANS in dict.keys():
    mark5=(mark4+1)
else:
    mark5=(mark4+0)
qn6="6).Which word(s) can logically replace the question mark?\n Water is to a pipe as \"?\" is to a wire!"
print(qn6)
ans1='cord'
ans2='electricity'
ans3='heat'
ans4='gas'
#2
Answers="a).%s \nb).%s \nc).%s\nd).%s"
print(Answers % (ans1,ans2,ans3,ans4))
dict={'b':'electricity'}
ANS=input('type your answer:')
if ANS in dict.keys():
    mark6=(mark5+1)
else:
    mark6=(mark5+0)
qn7="7).Which of the meanings is best fit for the specified word?\n DISPLEASURE."
print(qn7)
ans1='injustice'
ans2='complaint'
ans3='futile'
ans4='sin'
ans5='discord'
#2
Answers="a).%s \nb).%s \nc).%s\nd).%s\ne).%s"
print(Answers % (ans1,ans2,ans3,ans4,ans5))
#method two
dict={'b':'complaint'}
ANS=input('type your answer:')
if ANS in dict.keys():
    mark7=(mark6+1)
else:
    mark7=(mark6+0)
endtime=time.ctime().split()[3]
print('you have finished the test at',endtime)
#final calculation for converting the results.
fanz=(mark7*98.4375)/7
anz="Well in this test you have got %s questions right and your I.Q is %s"
print(anz % (mark7,fanz))
if fanz==98.4375:
    print(s1s)
elif fanz>=69.979 and fanz<90:
    print('This is what the average world population gets this qualifies for very normal')
else:
    print('NO ONE ISNOT SPECIAL, WE\'ALL ARE')
#the time management function
a=starttime[-1]
b=starttime[-2]
c=starttime[-4]
d=starttime[-5]
e=starttime[-7]
f=starttime[-8]
#
g=endtime[-1]
h=endtime[-2]
i=endtime[-4]
j=endtime[-5]
k=endtime[-7]
l=endtime[-8]
##
bbsec=(b+a)
bbmin=(d+c)
bbhr=(f+e)
#
eesec=(h+g)
eemin=(j+i)
eehr=(l+k)
##
bsec=int(bbsec)
bmin=int(bbmin)
bhr=int(bbhr)
#
esec=int(eesec)
emin=int(eemin)
ehr=int(eehr)
##
hrs=ehr-bhr
mins=emin-bmin
secs=esec-bsec
##
summation=(fanz+5)
if hrs == 0 and mins <= 10:
    print(ffanz % (summation,name))
else:
    print('Poor time management')
