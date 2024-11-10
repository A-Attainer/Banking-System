# Obada Al-Refai
# Murtaza Hakimi
def main():
    customer_data=file_to_dictionary()# we defaine here so it does not reset each iteration
    Exit='False'
    while Exit=='False': 
        print('Please select one of the following:')
        print('1- Open an account')
        print('2- Close an account')
        print('3- Withdraw')
        print('4- Deposit')
        print('5- Inquiry')
        print('6- Transactions')
        print('7- Top five accounts')
        print('8- Exit')
        main_choice=input('Your choice:')
        while main_choice!='1' and main_choice!='2' and main_choice!='3' and main_choice!='4' and main_choice!='5' and main_choice!='6' and main_choice!='7' and main_choice!='8':
            print('invalid input')
            main_choice=input('Your choice:')
        if main_choice =='1':
            New_account(customer_data)   
        elif main_choice =='2':
            Close_account(customer_data)
        elif main_choice =='3':
            Withdraw(customer_data)
        elif main_choice =='4':
            deposit(customer_data)
        elif main_choice =='5':
            inquiry(customer_data)
        elif main_choice =='6':
            last_transactions(customer_data)
        elif main_choice =='7':
            topBalance(customer_data)
        elif main_choice =='8':
            saveData(customer_data)
            Exit='True'#braking loop

def file_to_dictionary(): #turns the file customers.txt into a dictionary called 'customer_data' 
    file=open('customers.txt','r')    
    data_dictionary={}    
    for line in file:
        All_data=line.split(',')
        data_dictionary[All_data[0]]=[All_data[1],All_data[2],All_data[3].rstrip('\n')]
    file.close()
    
    return data_dictionary

def ID_in(customer_data,new_account_number): #checks if ID exists in "customer_data" dictionary 
    if new_account_number in customer_data:
        return True
    else:
        return False

def New_account(customer_data):
    new_account_number=input('Enter account number:')
    outcome=ID_in(customer_data,new_account_number)
    if outcome==True:
        print('There is already an account with this number')
    else:
        new_account_name=input('Enter customer name:')
        customer_data[new_account_number]=[new_account_name,'a','0.0']
        return customer_data


def Close_account(customer_data):
    account_number=input('Enter account number:')
    outcome=ID_in(customer_data,account_number)
    if outcome==False:
        print('There is no account with this number')
    else:
        print('Name:',customer_data[account_number][0])
        if customer_data[account_number][2]!='0.0' and customer_data[account_number][2]!='0':
            print('The account has balance, cannot be closed')
        elif customer_data[account_number][1]=='c':
            print('The account is alredy closed')
        else:
            customer_data[account_number]=[customer_data[account_number][0],'c','0.0']


def Withdraw(customer_data):
    account_number=input('Enter account number:')
    outcome=ID_in(customer_data,account_number)
    if outcome==False:
        print('There is no account with this number')
    else:
        print('Name: ',customer_data[account_number][0])
        if customer_data[account_number][1]=='c':
            print('The account is closed')
        else:
            withdraw_amount=float(input('Enter withdraw amount:'))
            while withdraw_amount<0:
                print("incorrect input type")
                withdraw_amount=float(input('Enter withdraw amount:'))

            if withdraw_amount>float(customer_data[account_number][2]):
                print("Insuffcient fund")
            else:
                print("Transaction complete")
                balance=(float(customer_data[account_number][2])-withdraw_amount)
                customer_data[account_number]=[customer_data[account_number][0],customer_data[account_number][1],str(balance)]
                file=open('transactions.txt','a')
                file.write(account_number+','+'w'+','+str(withdraw_amount)+'\n')
                file.close()
                return customer_data

def deposit(customer_data):
    account_number=input('Enter account number:')
    outcome=ID_in(customer_data,account_number)
    if outcome==False:
        print('There is no account with this number')
    else:
        print('Name: ',customer_data[account_number][0])
        if customer_data[account_number][1]=='c':
            print('The account is closed')
        else:
            deposit_amount=float(input("Enter the amount to deposit:"))
            balance=deposit_amount+(float(customer_data[account_number][2]))
            print("Your new balance: ", balance)
            customer_data[account_number]=[customer_data[account_number][0],customer_data[account_number][1],str(balance)]
            file=open('transactions.txt','a')
            file.write(account_number+','+'d'+','+str(deposit_amount)+'\n')
            file.close()
            return customer_data

def inquiry(customer_data):
    account_number=input('Enter account number:')
    outcome=ID_in(customer_data,account_number)
    if outcome==False:
        print('There is no account with this number')
    else:
        print('Name: ',customer_data[account_number][0])
        if customer_data[account_number][1]=='a':
            print('Status: Active')
        else:
            print('Status: Closed')
        print('Blanace: ',customer_data[account_number][2])

def last_transactions(customer_data):
    account_number=input('Enter account number:')
    outcome=ID_in(customer_data,account_number)
    if outcome==False:
        print('There is no account with this number')
    else:
        file=open('transactions.txt','r')
        list=[]

        for line in file:#we append transactions into a list
            list.append(line.rstrip('\n'))
        counter=0

        for i in range(len(list)-1,-1,-1):# we read the list backwards 
            data=(list[i]).split(',')
            if data[0]==account_number:
                counter+=1
                print(data[1],data[2])
                if counter==5:# we stop once we print 5 transactions 
                    break

        file.close()


def topBalance(customer_data):
    if len(customer_data)<5:
        
        for key in customer_data:
            print(key,customer_data[key][0],customer_data[key][2])
    else:
        alldata=customer_data# we make a copy that we can modify, so we do not change the main one 
        big_five={}
        for i in range(5):# all code under this is finding max balance, Id and name. we append to dictionary 'big_five', and do 5 times.
            m_balance=0.0
            m_key=''
            m_name=''
            for key in alldata:
                if float(alldata[key][2])>=m_balance:
                    m_balance=float(alldata[key][2])
                    m_key=key
                    m_name=alldata[key][0]
            del alldata[m_key]# we delete the max as to not find it in next iteration 
            big_five[m_key]=[m_name,m_balance]

        for ID in big_five:
            print(ID,big_five[ID][0],big_five[ID][1])

def saveData(customer_data):

    myfile = open('customers.txt','w')

    for key in customer_data:

        account_number , name , status, balance = key , customer_data[key][0] , customer_data[key][1], customer_data[key][2]
        myfile.write(str(account_number) +','+ name + ',' + status + ',' + balance + '\n')

    myfile.close()


main()