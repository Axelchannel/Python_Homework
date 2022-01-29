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


* # Файлы

* Хранение данных
* Передача данных в клиент-серверных проектах
* Хранение конфигов 

Как рабоать с файлами : 

1) Связать файловую переменную с файлом,определив модификатор работы
2) а - открытие для добавления данных
3) r - открытие для чтения данных
4) w - открытие для записи данных
5) w+, r+ 

# Example

colors = [ 'red', 'green' , 'blue']

data = open('file.txt,'a')
* Создаём текстовую переменную data и связываем её с текстовыми переменными  

data.writelines(colours) - разделитей не будет
* Функционал для записи данных  

Либо:

data=write('\nLINE 2\n')

data.write('LINE 3\n')
#
data.close()

## Пример другой записи
with open('file.txt, 'w') as data:
     
       data.write('line 1\n')

       data.write('line 2 \n')
#

## Чтение данных из файла

path= 'file.txt' - путь к папке

data=open(path, 'r') - открываем папку в режиме чтения

for line in data:

       print(line)
data.close()
#

## Функции и модули

Имеем файл python.py в котором написана функция.

Для того, чтобы обратиться к этой функции в другой файле необходимо:

import hello as h

print(h.имя функции(x))
#

def new_string(symbol,count):

     return symbol*count

print(new_string('!', 5)) !!!!!

print(new_string('!')) TypeError missing 1 required

или

ef new_string(symbol,count = 3):

     return symbol*count

print(new_string('!', 5)) !!!!!

print(new_string('!')) !!!

print(new_string(4)) 12

#
## Возможность передачи неограниченного кол-ва переменных

def concatentatio(*params):
      
        res: str = ""
        for item in params:
             res += item
        return res
print(concatentatio('a','s','d','w')) asdw

print(concatentatio('a','1','d','2')) a1d2

print(concatentatio(1,2,3,4)) error
#
## Рекурсия

      def fib(n):
          if n in [1,2]:
               return 1
          else 
               return fib(n-1) + fib(n-2)

        list = []
        for e in range (1,10):
               list.append(fib(e))
        print(list) 1 1 2 3 5 8 13 21 34
##
# Кортеж
Незменяемый список

        a = (3,4)
        print(a)  (3,4)
        print(a[0]) 3 
        print(a[-1]) 4

        
        a = (3,4,5)
        for item in a:
             print(item)  3 4 5  
        
Распаковка кортежа

        t = tuple(['red','green','blue'])
        red,green,blue = t
        print('r:{},'g:{},'b:{}.format(red,green,blue) r:red g:green b:blue
#
## Словари 
Непорядоченные коллекции призвольных объектов с доступом по ключу 

        dictionary = {} - пустой словарь
        dictionary = \  - указание пар
            {
                    'up' : p
                    'left' : l
            }
        
        print(dictionary) 'up': p , 'left': l
        print(dictionary['left'])  l 

Для того, чтобы пробежаться по ключам:

        for k in dictionary.keys()
            print(k)  up, left 
Для того, чтобы увидеть конкретные значения:

        for k in dictionary.values()
            print(k)  p, l
#
## Множества

       colors = {'red','green'}
       print(colors)
       colors.add('red')
       colors.remove('green')
       colors.discard('red')
       colors.clear()

       a = {1,2,3,4}
       b = {2,5,8}
       c=a.copy() c={1,2,3,4}
       u.a.union(b) c={1,2,3,4,5,8}
       i=a.intersection(b) i = P{2}
       dl = a.difference(b) dl = {}
##
# Списки

       list1 = [1,2,3,4,5]
       print(list1.pop()) - извлеякает последний элемент

       print(list1.pop(2)) - удаление 2-го элемента

       print(list1.instert(2,11,) добавление 11 на 2 позицию 
       print(list1.append(11)) добавление в конец 
