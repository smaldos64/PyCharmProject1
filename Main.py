class Module_Test:

    def Add_Numbers(Number1, Number2):
        Number3 = Number1 + Number2
        return Number3

    def Subtract_Numbers(Number1, Number2):
        Number3 = Number1 - Number2
        return (Number3)

if __name__ == '__main__':
    print("Hej med dig !!!")

    var1 = 10

    if (10 == var1):
        print("Værdien af var1 er 10")
        print("Og nu kører det for os")
    else:
        print("Værdien af var1 er forskellig fra 10")
        print("Og nu kører det ikke for os")

    print("Her kører jeg altid !!!")

    var2 = 12
    var3 = 24

    var4 = Module_Test.Add_Numbers(var2, var3)

    print("Resultatet af %d + %d er %d" % (var2, var3, var4))

    var4 = Module_Test.Add_Numbers(23, 78)

    print("Resultatet af %d + %d er %d" % (23, 78, var4))