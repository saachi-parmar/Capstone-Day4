# Inheritance ----------------------------------------------------
class Animal:
    
    def speak(self):
        print("Animal speaks")
        
class Dog(Animal):
    
    def speak(self):
        print("Dog barks")
        
dog = Dog()
dog.speak()
dog = Animal()
dog.speak()
            
class Cat(Animal):
    
    def speak(self):
        print("Cat meows")   
        
cat = Cat()
cat.speak()


print("\n")



class father:
    
    def father_traits(self):
        print("traits from father")
        
class mother:
    
    def mother_traits(self):
        print("traits from mother")

            
class child(father, mother):
    
    def child_traits(self):
        print("traits of child") 
        

child = child()
child.father_traits()
child.mother_traits()
child.child_traits()


print("\n")



class grandparent:
    
    def grandparent_traits(self):
        print("Traits from grandparent")
        
class parent(grandparent):
    
    def parent_traits(self):
        print("Traits from parent")
        
class child(parent):
    
    def child_traits(self):
        print("Traits of child from parent and grandparent")
        
    
child = child()
child.grandparent_traits()
child.parent_traits()
child.child_traits()


print("\n")



class base:
    
    def base_method(self):
        print("Base class method")
        
class A(base):
    
    def A_method(self):
        print("A class method")
        
class B(base):
    
    def B_method(self):
        print("B class method")
        
class C(A,B):
    
    def C_method(Self):
        print("class method")
        
obj = C()
obj.base_method()
obj.A_method()
obj.B_method()
obj.C_method()

print(C.mro())

print("\n")
