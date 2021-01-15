from datetime import date
import json

 
class addBook:
    def __init__(self):
        nme=str(raw_input('enter book name:'))
        book=False
        lines=[]
        with open("Books.csv", 'r+w') as f:
            lines = f.readlines()
            for i in range(lines.__len__()):
                    line = lines[i]
                    line = line[0:-1]
                    cut = line.find(',')
                    index = line[0:cut]
                    line = line[cut+1:]
                    cut = line.find(',')
                    name = line[0:cut].lstrip(' ')
                    line=line[cut+1:]
                    cut=line.find(',')
                    price = line[0:cut].lstrip(' ')
                    num = line[cut+1:].lstrip(' ')
                    if nme==name:
                        book=True
                        print("*** This book is already on the list ***")
                        n=str(raw_input("Do you want to change the number of books?(y/n)"))
                        if n=='y':
                            numb=int(input("enter book's new number:"))
                        elif n=="n":
                            numb=num
                            
                        p=raw_input("Do you want to change book's price?(y/n)")
                        if p=="y":
                            pric=float(input("enter book's price:"))
                        elif p=="n":
                            pric=price
                            
                        data = "{index:02d},{name:>30},{price:>10},{number:>5}\n".format(
                            index=(i) ,
                            name= nme,
                            price=pric,
                            number=numb
                            )
                        lines[i]=data
        if book==True:
            with open("Books.csv", 'w') as f: 
                f.writelines(lines)
                
        if book== False:           
            with open("Books.csv", 'r+w') as f: 
                lines = f.readlines()      
                data = "{index:02d},{name:>30},{price:>10},{number:>5}\n".format(
                    index=(lines.__len__()) ,
                    name= nme,
                    price=float(input("enter book's price:")),
                    number=int(input("enter book's number:"))
                    )
                f.write(data)
        
            
            

class sellAndRemove:
    def __init__(self):
        book=False
        price=float
        bookname=str(raw_input('enter book name to sell:'))
        lines=[]
        with open("Books.csv", 'r') as f:
            lines = f.readlines()
            
          
            for i in range(1,lines.__len__()):
                line = lines[i]
                line = line[0:-1]
                cut = line.find(',')
                index = line[0:cut]
                line = line[cut+1:]
                cut = line.find(',')
                name = line[0:cut].lstrip(' ')
                line=line[cut+1:]
                cut=line.find(',')
                price = line[0:cut].lstrip(' ')
                num = line[cut+1:].lstrip(' ')
                num=int(num)
                num-=1
                index=int(index) 
                
                if name==bookname:
                    book=True
                    data = "{index:02d},{name:>30},{price:>10},{number:>5}\n".format(
                            index=index ,
                            name= name,
                            price=price,
                            number=num
                            )
                    
                    lines[index]=data
        if book==True:
            with open("Books.csv", 'w') as f:            
                f.writelines(lines)
                
            buyername=str(raw_input("enter buyer's name: "))
            buyerfile="bills/{name}.json".format(
                name=buyername
            )
            
            d=date.today()
            d=str(d)
        
            with open(buyerfile,'w') as f:
                x = {
                "Buyer's name": buyername,
                "Book's name:": bookname,
                "Price": price,
                "Date":d
            }
                sorted_string = json.dumps(x, indent=3, sort_keys=False)

                f.write(sorted_string)
                
            with open("sale_statistics.csv",'r+w') as f:
                l=f.readlines()
                index=l.__len__()
                data = "{index:02d},{name:>30},{price:>10},{date:>5}\n".format(
                                index=index ,
                                name= bookname,
                                price=price,
                                date=d
                                )
                f.write(data)
                
        elif book==False :
            print("this book is no exist")
            
class saleStatistics:
        
    def __init__(self):
        pass
        
    def all_sale(self):
        with open("sale_statistics.csv",'r+w') as f:
            lines=f.readlines()
            number=lines.__len__()
            number-=1
            d="you have sold {num} Books all the time".format(
                num=number
            )
            print(d)

    def date_sale(self):
        day1=input("enter start day for check:")
        mon1=input("enter star month for check:")
        day2=input("enter end day for check:")
        mon2=input("enter end month for check:")
        
        start="2021-{month:02d}-{day:02d}".format(
            day=day1,
            month=mon1
        )
        end="2021-{month:02d}-{day:02d}".format(
            day=day2,
            month=mon2
        )
        
       
        with open("sale_statistics.csv",'r+w') as f:
            lines=f.readlines()
            first=False
            second=False
            
            for i in range(1,lines.__len__()): 
                
                line = lines[i]
                line = line[0:-1]
                cut = line.find(',')
                index = line[0:cut]
                line = line[cut+1:]
                cut = line.find(',')
                name = line[0:cut].lstrip(' ')
                line=line[cut+1:]
                cut=line.find(',')
                price = line[0:cut].lstrip(' ')
                date = line[cut+1:].lstrip(' ')
                
                if date>=start and first==False:
                    firstindex=int(index)
                    first=True
                
                if date>=end and second==False:
                    secondindex=int(index)
                    second=True
                
            number=secondindex-firstindex
            d="you have sold {num} Books in specific date you enter".format(
            num=number
            ) 
            print(d)
                
                
        
txt="""
for see all sale statistics enter 1
for see statistics on specific date enter 2
"""    
text = """
for add a book enter 1
for sell a book enter 2
for see sale statistics enter 3
"""
if __name__ == '__main__':
    while True:
        print(text)
        num=raw_input("enter number : ")
        if num=='1':
            addBook()
        elif num=='2':
            sellAndRemove()
        elif num=='3':
            sale=saleStatistics()
            print(txt)
            nm=raw_input("enter number : ")
            if nm=='1':
                sale.all_sale()
            if nm=='2':
                sale.date_sale()    
        else:
            print("enter 1 or 2 or 3")
            
    
