# function is Block of statements that perform a secific task.

def data():
    a = 5
    b = 10
    sum = a + b
    print(sum) 

data();


def cal_sum(a, b):
    sum = a + b
    print(sum);

cal_sum(2,2);
cal_sum(4,2);
cal_sum(5,2); 

def avg_three_number(a,b,c):
    avg = a + b + c / 3
    print(avg);

avg_three_number(2,2,2);


list = [1,2,3,4]
def find_leng():
    length = len(list)
    print(length)

find_leng()

def element_of_list():
    print(list);

element_of_list()

n = int(input("What is u number!"))
def factorial_of_number():
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

factorial_of_number()