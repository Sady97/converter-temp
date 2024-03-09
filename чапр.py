class Temperature:
    """"класс перевода температуры цельсия и фаренгейта"""
    def __init__(self,  t:int, scale:str):

        self.__t = t
        if scale.upper() in "CF":
            self.__scale = scale.upper()
        else:
            print("Не правилбно подобраны буквы(надо C или F)")
            raise ValueError("Не правилбно подобраны буквы(надо C или F)")
#перевод цельсия в фаренгейт
    def convert_c_to_f(self):
        if self.__scale == "C":
            self.__t = self.__t * 9/5 + 32
            self.__scale = "F"
#перевод фаренгейт в цельсия
    def convert_f_to_c(self):
        if self.__scale == "F":
            self.__t = (self.__t - 32) * 5/9
            self.__scale = "C"
    def get(self):
        return (self.__t,self.__scale)

    def set(self, t:int, scale:str):
        self.__t = t
        self.__scale = scale.upper()

t1 = Temperature(t= 100, scale= "c")
print(t1.get())
t1.convert_c_to_f()
print(t1.get())
t1.set(t=0, scale="c")
print(t1.get())





