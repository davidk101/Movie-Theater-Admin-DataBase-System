import string
import random
import os
import pickle

class movie:
    def __init__(self):
        self.mname=''
        self.mcast=''
        self.plot=''
        self.mtime=''
        self.mbaseprice=0


    def getdata(self):
        self.mname=raw_input('ENTER NAME OF MOVIE: ')
        self.mcast=raw_input('ENTER THE PROTAGONISTS: ')
        self.mplot=raw_input('ENTER SYNOPSIS: ')
        self.mtime=raw_input('ENTER SHOWTIME {NOTE: PLEASE ENTER TIME IN 24-HOUR FORMAT}: ')
        self.mbaseprice=input('ENTER PRICE OF TICKET: DHS.')
        print
    def display(self):
        print '\t',self.mname.upper(),'\nSynopsis: ',self.mplot,'\n'
        print 'Protagonist: ',self.mcast,'\n'
        print 'Shows: ',self.mtime
        print '\nBase Price: DHS.',self.mbaseprice,
        print '\n'

def append():
    f=open('movie.dat','ab')
    m=movie()
    m.getdata()
    pickle.dump(m,f)
    f.close()

def show():
    if os.path.isfile('movie.dat'):
        f=open('movie.dat','rb')
        try:
            while True:
                x=pickle.load(f)
                x.display()

        except EOFError:
            pass
        else:
            print 'FILE DOES NOT EXIST'

def search():
    if os.path.isfile('movie.dat'):
        f=open('movie.dat','rb')
        name=raw_input('ENTER NAME OF MOVIE TO BE SEARCHED: ')
        try:
            while True:
                x=pickle.load(f)
                if name.lower()== x.mname.lower():
                    print
                    print x.display()
                    break
        except EOFError:
            print  '\tMOVIE NOT FOUND\n'

def delete():
    if os.path.isfile('movie.dat'):
        f=open('movie.dat','rb')
        g=open('temp.dat','wb')
        name=raw_input('ENTER NAME OF MOVIE TO BE DELETED: ')
        c=0
        try:
            while True:
                x=pickle.load(f)
                if name.lower()!=x.mname.lower():
                    pickle.dump(x,g)
                else:
                    c=1
        except EOFError:
            if c==0:
                print '\tMOVIE NOT FOUND\n'
            else:
                print '\t MOVIE IS DELETED SUCCESSFULLY \n'
        f.close()
        g.close()
        os.remove('movie.dat')
        os.rename('temp.dat','movie.dat')
    else:
        print '\tFILE DOES NOT EXIST\n'

def update():
    if os.path.isfile('movie.dat'):
        f=open('movie.dat','rb')
        g=open('temp.dat','wb')
        name=raw_input('ENTER NAME OF MOVIE TO BE UPDATED: ')
        c=0
        try:
            while True:
                x=pickle.load(f)
                if name.lower()!=x.mname.lower():
                    pickle.dump(x,g)
                else:
                    y=movie()
                    y.getdata()
                    pickle.dump(y,g)
                    c=1
        except EOFError:
            if c==0:
                print '\tMOVIE NOT FOUND\n'

        f.close()
        g.close()
        os.remove('movie.dat')
        os.rename('temp.dat','movie.dat')
        print 'NEW MOVIE DATA IS',
        y.display()
    else:
        print 'FILE DOES NOT EXIST'

def custlist():
    if os.path.isfile('cust.dat'):
        f=open('cust.dat')
        c=customer()
        print '\nTICKET REFERENCE\tCUSTOMER NAME\tMOVIE NAME\tNO.OF TICKETS\tPRICE'
        try:
            while True:
                c=pickle.load(f)
                print '%12s\t%16s\t%10s\t%13s\t%5s'%(c.ticketref,c.cname,c.mtname,c.seatno,c.tprice)

        except EOFError:
            pass
        print

        f.close()
    else:
        print '\tNO BOOKINGS DONE\n'

class customer:
    def __init__(self):
        self.cname=''
        self.cnum=0
        self.cemail=''
        self.seattype=''
        seatno=0
        self.mtname=''
        self.mtime=''
        self.price=''
        self.tprice=''
        self.ticketref=''

    def inputdata(self):
        self.cname=raw_input('ENTER CUSTOMER NAME: ')
        self.cnum=raw_input('ENTER YOUR CONTACT NUMBER: ')
        self.cemail=raw_input('ENTER YOUR E-MAIL ID: ')
        print
        show()
        self.movie()
        self.seattype=raw_input('ENTER SEAT TYPE(NORMAL/VIP): ')
        self.seatno=input('ENTER NUMBER OF SEATS: ')
        self.reference()
        self.calprice()

    def reference(self):
        self.ticketref=self.mtname[0:1]+str(random.randint(10000,20000))
        print 'PLEASE NOTE YOUR BOOKING REFERENCE CODE TO VIEW THE TICKET',self.ticketref

    def movie(self):
        self.mtname=raw_input('SELECT YOUR MOVIE: ')
        f=open('movie.dat','rb')
        m=movie()
        flag=0
        while True:
            try:
                while True:
                    m=pickle.load(f)
                    if self.mtname.lower()==m.mname.lower():
                        self.mtime=raw_input('ENTER THE TIME: ')
                        self.price=m.mbaseprice
                        flag=1
                        break
            except EOFError:
                print 'ENTER A MOVIE NAME FROM THE LIST OF MOVIES SHOWN ABOVE'
                self.mname=raw_input('SELECT YOUR MOVIE: ')
            if flag==1:
                break
            f.close

    def calprice(self):
        if self.seattype.lower()=='vip':
            self.price+=30
        self.tprice=self.price*self.seatno

    def ticket(self):
        print '\nCustomer Name:',self.cname
        print 'Phone Number:',self.cnum
        print 'Customer E-mail ID:',self.cemail
        print 'Movie Name:',self.mtname
        print 'Movie Time:',self.mtime
        print 'Seat Type:',self.seattype
        print 'Price per seat:',self.price
        print 'Number of seats:',self.seatno
        print 'Total price:',self.tprice

def addcustomer():
    f=open('cust.dat','ab')
    c=customer()
    c.inputdata()
    pickle.dump(c,f)
    f.close

def viewticket():
    bref=raw_input("ENTER YOUR BOOKING REFERENCE CODE: ")
    c=customer()
    f=open("cust.dat","rb")
    try:
        while True:
            c=pickle.load(f)
            if c.ticketref==bref:
                c.ticket()
                break
    except EOFError:
        print '\tBOOKING NOT FOUND\n'
    f.close()
ch="yes"

while ch.lower()=="yes":
    print "\n1. ADMIN MENU OPTIONS\n2. CUSTOMER MENU OPTIONS\n"
    user=input('PLEASE ENTER YOUR CHOICE:')
    print ''
    if user==1:
        print "WELCOME ADMIN TO YOUR DATABASE"
        while True:
            print "1. ADD MOVIE\n2. SEARCH MOVIE\n3. UPDATE MOVIE\n4. DELETE MOVIE\n5. DISPLAY MOVIE\n6. DISPLAY BOOKED TICKET INFO\n7. EXIT ADMIN MENU\n"
            opt=input("PLEASE ENTER YOUR CHOICE:")
            if opt==1:
                append()
            elif opt==2:
                search()
            elif opt==3:
                update()
            elif opt==4:
                delete()
            elif opt==5:
                print
                show()
            elif opt==6:
                custlist()
            elif opt==7:
                break
    elif user==2:
        c=customer()
        ch1="yes"
        while ch1.lower()=="yes":
            print "1.BOOK A TICKET\n2.VIEW TICKET\n"
            opt1=input("ENTER YOUR CHOICE: ")
            if opt1==1:
                addcustomer()
            elif opt1==2:
                viewticket()
            else:
                print "INVALID CHOICE"
            ch1=raw_input("\nENTER |Yes| TO CONTINUE WITH CUSTOMER MENU OR |No| TO GO BACK TO MAIN MENU: ")
            print
    else:
        print"INVALID CHOICE"
    ch=raw_input("DO YOU WISH TO CONTINUE WITH PROGRAM? ")
print '   THANK YOU FOR USING THIS PROGRAM'
