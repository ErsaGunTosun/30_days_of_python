# Day 1

# Math operation(Matematiksel işlem)

print(3+1)    # addition(toplama)
print(7-2)    # subtraction(çıkarma)
print(5*9)    # multiplication(çarpma)
print(6/3)    # divison(bölme )
print(7%4)    # modulus(kalan)
print(7 // 4) # Floor division operator(bölüm)
print(9**2)   # exponential(üst alma)



# Data types (veri değerleri)
    # type() içine girilen verinin türünü geri döndürür.
print(type(10))                  #int
print(type(3.1))                 #float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List(Liste)
print(type({'name':'Asabeneh'})) # Dictionary(Sözlük)
print(type({9.8, 3.14, 2.7}))    # Set(Küme)
print(type((9.8, 3.14, 2.7)))    # Tuple(Demet)


# set VS list VS disctionary VS tuple
x = {1,2,3,4,5} #küme
print('---**---')
print(type(x))
    #print(x[1]) küme index ile eleman alınamaz

y = [1,2,3,4,5] #liste
print('---**---')
print(type(y))
print(y[4])

z = {"name":"ersagun","last name":"tosun"}  #sözlük
print('---**---')
print(type(z))
print(z['last name'])

w = (1,2,3,4,5,6) #demet
print('---**---')
print(type(w))
print(w[-1])


