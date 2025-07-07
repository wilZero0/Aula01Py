frutas = ("Banana", "Maça", "Kiwi")
listsfrutas = list(frutas)
listsfrutas.append("laranja")
frutas = tuple(listsfrutas)

print(frutas)

listsfrutas.remove("Kiwi")
frutas = tuple(listsfrutas)

print(frutas)

listsfrutas.insert(0, "Kiwi")
frutas = tuple(listsfrutas)

print(frutas)

tuplaNumero =(0,1,2,3)
listaNumero =list(tuplaNumero)
listaNumero.append(5)
listaNumero.insert(1,4)
tuplaNumero=tuple(listaNumero)

print(tuplaNumero)

listaNumero.remove(2)
tuplaNumero=tuple(listaNumero)

print(tuplaNumero)

listaNumero.pop(1)
tuplaNumero=tuple(listaNumero)

print(tuplaNumero)