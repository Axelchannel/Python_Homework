# Информация по Pyton 

* ## Переменные 
int, float,boolean,  str, list, None

value = 2809

name = "German"

Чтобы у знать тип данных Print(type(a))

* ## Вывод переменный

print(a,b,s)

print(a, ' - ', b,' - ', s)

print('{} - {} - {}'.format(a,b,s))

print(f'{a} - {b} - {c}')

print('{1} - {2} - {0}'.format(a,b,s))

* ## Логическая переменная

f=True

* ## Списки

list = []   ( print(list) )

list = ['1', '2', '3', 'hello',1,2,1.4,True]

* ## Ввод и вывод данный

input() - вывод данных

input() - ввод данных

int(input()) - ввод целого числа

float(input()) - ввод вещественных чисел

* ## Арифметические операции 
* c= a+b --> print(c)

* c= a-b --> print(c)
* c= a / b --> print(c) - для вещественных чисел 

   c= a // b  --> print(c) - целое 

   c= a % b --> print(c) - остаток

* c= a ** b --> print(c) - возведение в степень 

* с = a * b 
получим (1.3 * 3 = 3.90000004) -->

round(a*b,n) - округление по мат.правилам, где n - кол-во знаков


* Операции присваивания 

     a+= 5 (Вместо + любые другие операции)

* Логические операции

<>, >=, <,<=, ==, !=

not,and,or, in
    
* ## Логические ветвления 
1. if-else

if condition:

        command
 
else: 

        command


2. if - elif

if name == "Маша:

        print(name)

elif name =="Марина":

        print(name)


3. While

while condition:
        
        command

else condition:

        command

4. for

for i in enumeration:

        command

* Example

r=range(10)

for i in r:

        print(i)

Варианты записи range:

range (1,10) , range (1,10,n), где n - шаг


* ## Строки

1. len(text) - длина
2. 'n' in text - наличие n в строке
3. text.isdigit() - все ли элментры в строке числа
4. text.islower() - элементы нижнего регистра?
5. text.replace ('n', 'N' ) - замена элементов
6. text[:] - вывод от 0 : N 

* # Списки: введение

* number=[1,2,3]
* ran=range(1,6)

  number= list(ran)

* number[0] = 10

  len(number) - кол-во элементов

* for i in number
     
    i*=2
    print(i)  [1,4,6]

* Добавление/ удаление элементов

    colours = ['red','green']

    colors.append('gray") - добавить в конец

    colors.remove('red') - удалить элемент

    del colors[0]

* # Функции

def function(x):

      command

      return






