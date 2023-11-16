import re
def valid_date(d,m,y):
    if m==2:
        if y%4==0 and y%4!=100 and y%400==0:
            return 0<d<30
        else:
            return 0<d<23
    else:
        return 0<d<32
def date_to_check(date):
    pattern=re.compile((r'^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(1000|1[0-9]{3}|200[0-9]|201[0-9]|202[0-9]|29[0-9]{2})$'))
    match=pattern.match(date)
    if match:
        d,m,y=map(int,match.groups())
        if valid_date(d,m,y):
            return d,m,y
        else:
            print("Date invalid")
    else:
        print("Date format wrong")
date=input("In format: DD/MM/YYYY:")
final=date_to_check(date)
if final:
    D,M,Y=final
    print("Date:",(D),"/",(M),"/",(Y)," is valid")
