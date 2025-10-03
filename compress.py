"""
Black Jack for NUMWORKS
github.com/lulutoulouse31/BlackJack-numworks

Compressed version
Code update 03/10/25

This software is licensed under the GNU AGPL-3.0 License
"""

I=isinstance;E=ord;T=int;S=enumerate;P=str;H=range;A=len
import math as G,time as L,random as K,kandinsky as C,ion as D
def N():
	F='BnkkkltBpnPmlFxiiipNvivHeabbaapAhePheFxddajNuasHeiCgbAheCtlEsihmBheBrmtDcjBpirCwnhjtAuasAvmpyCeiCkbAheBpaadxBoaddacyheAoahyDcjAqaaawAvdaeaapuasvdctDeaffealAheAnaaaabwvaiyAunyhepaiyEcjAnaaatAjcuBmvuaodctEecffeahAhetaaaaaadpawEhaaaxFcjqbaaabwbkEuabalFeiCnavhepaaaaaabpawEhagajFcjeaaaaakbjEuacfawEehBynavheycadeaalxahBsnAhdylaswmuAsanhaaaaamiatAxlvuaqxaeEeabbbajAheBunbvuBoaadafxheBdbxbadafxykeaimyycaccaouasApapDnkkkksBpmByposDtkioxArpBwouymimxCniqDnijuAxowBpo';F=''.join([(E(A)-64)*'z'if E(A)<=90 else A for A in F]);C.fill_rect(0,0,320,222,(255,255,255));I='Made by lulutoulouse31';B=8
	for(D,K)in S(I):
		for H in K:
			if H!=' ':J(H,B,211,(0,0,0))
			B+=4
	for(D,A)in S(F):
		L.sleep(1/999);A=(E(A)-97)*10
		if A!='z':B=(D-G.floor(D/64)*64)*5;M=G.floor(D/64)*5;C.fill_rect(B,M+75,5,5,(A,A,A))
def b():
	for A in H(15):B=0,G.floor(60+80/15*A),G.floor(10+40/15*A);C.fill_rect(0,222-A*16,320,16,B)
def h():
	B=[];C=[]
	for D in['R','R','B','B']*2:
		for E in H(2,11):B.append(P(E)+D)
		for G in['K','Q','J','A']:B.append(G+D)
	for E in H(A(B)):F=K.randint(0,A(B)-1);C.append(B[F]);B.pop(F)
	return C
def W(x,y,x2,y2):
	for A in H(y,y2+1):C.fill_rect(x,A,x2-x,1,C.get_pixel(x,A))
def R(C,D):
	if I(D,T):B='{:,}'.format(D).replace(',',' ')
	elif I(D,list):B=D.copy();B.reverse();B=['{:,}'.format(T(A)).replace(',',' ')for A in B];B=' / '.join(B)
	if C==0:C='Balance: '+B;E=280-4*A(B)
	else:W(0,0,160,10);E=5;C='Bet: '+B
	G=5
	for F in C:
		if F!=' ':J(F,E,G,(255,255,255))
		E+=4
def J(I,x,y,J):
	B="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?!.,:;%+-*/=<>'_→[](){}";G='2jg02oN06Fd07AE04l907dE07dl079907gl07h906lj06kl03aZ06jk07dd07da03bh05lj07IN079h05kj04ad05zj01li03jk06la06jwG6kj03YE07II05jl05jg05jz05gj05gI07Ad003l04cl003d01Bl007p03ca003lE4cj026N0119g4br04aZ007z006j007l006la03l907a003M04dZ005l005g005?005L005hE07AO7A202I200020002W0220022W5Ab00NG007000ge01AKW0uu01KH04HK02G00000u4NK03IJ06IM01IH04IK03MJ06JM0'
	for D in H(4):
		E=B.index(G[B.index(I)*4+D]);A=32
		for F in H(6):
			if E>=A:C.set_pixel(F%3+x,F//3+2*D+y,J);E-=A
			A=A//2
def X(K):
	C=[A+' '*10 for A in['UP: Stand','DOWN: Hit','LEFT: Double','RIGHT: Split']];A=15
	for(D,E)in S(C):
		F=(255,255,255)if K[D]else(0,45,10)
		for B in E:
			if B!=' ':J(B,A,211,F)
			A+=4
def c(H,F,G,B,O):
	E=B[0]+B[1]if A(B)==2 else B[0];C=[True,True,False,False];D=[A[:-1].replace('K','10').replace('Q','10').replace('J','10')for A in H]
	if A(D)==2 and E+O<=G:
		C[2]=True
		if D[0]==D[1]and F==1:C[3]=True
	return C
def d(M):
	while True:
		C=['S','H','DD','SP']
		for(A,B)in S([D.KEY_UP,D.KEY_DOWN,D.KEY_LEFT,D.KEY_RIGHT]):
			if D.keydown(B)and M[A]:
				while D.keydown(B):L.sleep(1/100)
				return C[A]
		L.sleep(1/100)
def B(x,y,D,E=0):
	G=(255+E,0,0)if'R'in D else(0,0,0);B=(245+E,245+E,245+E)if D!='back'else(160,19,162);C.fill_rect(x,y+2,1,41,B);C.fill_rect(x+30,y+2,1,41,B);C.fill_rect(x+1,y+1,1,43,B);C.fill_rect(x+29,y+1,1,43,B);C.fill_rect(x+2,y,27,45,B)
	if D!='back':F=D[:-1]
	else:F='$$';G=81,0,81
	H=-5 if A(F)==2 else 0;C.draw_string(F,x+10+H,y+13,G,B)
def M(H,I,A,pos=0,G=0):
	C=0 if pos==0 else 60 if pos==1 else-60;D=143+C;E=130 if H=='p'else 25
	for F in I:B(D-A*20,E-A*5,F,-7*(A%2)+G);A+=1
def O(J,K,L=0):
	D=0 if L==0 else 60 if L==1 else-60;F=149;G=179 if J=='p'else 73;E=[A[:-1]if A[:-1]not in['K','Q','J']else'10'for A in K];sum=0
	for B in E:B=11 if B=='A'else B;sum+=T(B)
	for J in H(E.count('A')):
		if sum>21:sum-=10
		else:break
	D+=6 if A(P(sum))==1 else 0;I=(200,0,0)if sum>21 else(0,120,180)if sum==21 else(0,30,0);C.draw_string(P(sum),F+D,G,(255,255,255),I);return sum
def F(V,N,S,G):
	B='{:,}'.format(N).replace(',',' ');D=255,255,255;E=90,90,90
	if V==0:
		W(60,60,260,100)
		if S:C.draw_string('> Balance: '+B+' <',83-3*A(B),70,D,E)
		else:C.draw_string('Balance: '+B,100-3*A(B),70,D,E)
	else:
		F=0 if G else-20;W(80,100+F,250,130+F)
		if S:C.draw_string('> Bet: '+B+' <',103-3*A(B),110+F,D,E)
		else:C.draw_string('Bet: '+B,122-3*A(B),110+F,D,E)
def Q(C,A,B):
	b();P=[A+' '*16 for A in['LEFT: Lower','RIGHT: Higher','OK: Start']];M=25
	for Q in P:
		for N in Q:
			if N!=' ':J(N,M,211,(255,255,255))
			M+=4
	E=1
	if B>A:B=G.floor(A/500)*500
	if C:E=0;F(0,A,True if E==0 else False,C)
	else:R(0,A)
	F(1,B,True if E==1 else False,C);O=True
	while O:
		for(K,T)in S([D.KEY_UP,D.KEY_DOWN,D.KEY_LEFT,D.KEY_RIGHT,D.KEY_OK]):
			if D.keydown(T):
				for I in H(2):
					if K==I and C and E==(I+1)%2:E=I;F(0,A,True if I==0 else False,C);F(1,B,True if I==1 else False,C)
				if K==2:
					if E==0 and A>1000 and A-1000>=B:A+=-1000;F(0,A,True,C)
					elif E==1 and B>500:B+=-500;F(1,B,True,C)
				elif K==3:
					if E==0 and A<1000000:A+=1000;F(0,A,True,C)
					elif E==1 and B<1000000 and B+500<=A:B+=500;F(1,B,True,C)
				elif K==4:O=False
				L.sleep(1/10)
		L.sleep(1/100)
	return A,B
def U(U,F):
	b();G=h();e=F;F=[F];B=[[G[0],G[1]]];I=[G[2]]
	for E in H(3):G.pop(0)
	M('p',B[0],0);M('d',['back']+I,0);sum=[O('p',B[0])];O('d',I);R(0,U);R(1,F[0])
	while True:
		if sum[0]>=21:break
		V=c(B[0],1,U,F,e);X(V);N=d(V)
		if N=='S':break
		elif N in['H','DD']:
			M('p',[G[0]],A(B[0]));B[0].append(G[0]);G.pop(0);sum[0]=O('p',B[0])
			if N=='DD':F[0]*=2;R(1,F[0]);X([False,False,False,False]);break
		elif N=='SP':
			F=[F[0],F[0]];B=[[B[0][0],G[0]],[B[0][1],G[1]]]
			for E in H(2):G.pop(0)
			W(120,120,177,200);sum=[O('p',B[0],1),O('p',B[1],2)];J=1 if sum[0]>=21 and sum[1]!=21 else 0
			for E in H(2):M('p',B[E],0,E+1,-170 if J==(E+1)%2 else 0)
			R(1,F)
			if sum==[21,21]:break
			f=True
			while f:
				Y=True
				while Y:
					V=c(B[J],2,U,F,e);X(V);N=d(V)
					if N=='S':Y=False
					elif N in['H','DD']:
						M('p',[G[0]],A(B[J]),J+1);B[J].append(G[0]);G.pop(0);sum[J]=O('p',B[J],J+1)
						if N=='DD':F[J]*=2;R(1,F);Y=False
					if sum[J]>=21:Y=False
				if J==0 and sum[1]<21:
					J=1
					for E in H(2):M('p',B[E],0,E+1,-170 if E==0 else 0)
				else:
					for E in H(2):M('p',B[E],0,E+1)
					f=False
			break
	X([False,False,False,False]);Q=0
	while Q<17:
		L.sleep(1)
		if A(I)>1:I.append(G[0])
		else:I.insert(0,G[0])
		G.pop(0);M('d',I if A(I)==2 else[I[-1]],0 if A(I)==2 else A(I)-1);Q=O('d',I)
		if A(sum)==1:
			if sum[0]>21 or sum[0]==21 and A(B[0])==2:break
		elif sum[0]>21 and sum[1]>21 or sum[0]==21 and A(B[0])==2 and sum[1]==21 and A(B[1])==2:break
	L.sleep(1);K=0
	for(E,Z)in S(sum):
		if Q==21 and A(I)==2 and A(B[E])!=2:K-=F[E]
		elif Z==21 and A(B[E])==2 and not(A(I)==2 and Q==21):K+=T(1.5*F[E])
		elif Z>21:K-=F[E]
		elif Z>Q or Q>21:K+=F[E]
		elif Z<Q:K-=F[E]
	i=(200,0,0)if K<0 else(88,88,88)if K==0 else(0,178,50);g='{:,}'.format(T(K)).replace(',',' ');a='Money earned: +'+P(g)if K>=0 else'Money lost: '+P(g)
	if K==0:a=a.replace('+','')
	C.draw_string(a,175-6*A(a),90,(255,255,255),i);C.draw_string('Press OK to continue',60,120,(255,255,255),(90,90,90))
	while not D.keydown(D.KEY_OK):L.sleep(1/100)
	while D.keydown(D.KEY_OK):L.sleep(1/100)
	U+=K;return U
def V(B):
	b();C.draw_string('Game played: '+P(B),95-6*A(P(B)),70,(255,255,255),(90,90,90));C.draw_string('Press OK to continue',60,100,(255,255,255),(90,90,90))
	while not D.keydown(D.KEY_OK):0
	while D.keydown(D.KEY_OK):0
def Y():
	N();L.sleep(2)
	while True:
		B=True;D=0;A=50000;C=5000;E=True
		while E:
			A,C=Q(B,A,C);B=False if B else B;A=U(A,C);D+=1
			if A<500:E=False
		V(D)
Y()