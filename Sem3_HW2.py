# Адаптер:
# Создайте класс ElectricSocket, который имеет метод supply_electricity(voltage). 
# Реализуйте класс USPlugAdapter, который адаптирует розетку стандарта США к европейскому стандарту.
# Создайте объекты и продемонстрируйте передачу электроэнергии через адаптер.



#Не знаю почему адаптер превращает 110 в 240, но если представить что может то как то так. 
class ElectricSocket:
    def supply_electricity(self, voltage: int):
        print(f"Поставка электроэнергии: {voltage} Вольт")

class USPlug:
    def __init__(self, voltage: int):
        self.voltage = voltage

    def plug_into(self, socket: ElectricSocket):
        socket.supply_electricity(self.voltage)

class EuroPlug:
    def __init__(self, voltage: int):
        self.voltage = voltage

    def plug_into(self, socket: ElectricSocket):
        socket.supply_electricity(self.voltage)

class USPlugToEuroSocketAdapter:
    def __init__(self, plug: USPlug):
        self.plug = plug

    def plug_into(self, socket: ElectricSocket):
        print("Использование адаптера для розетки стандарта США")
        euro_voltage = self.convert_voltage(self.plug.voltage)
        euro_plug = EuroPlug(euro_voltage)
        euro_plug.plug_into(socket)

    @staticmethod
    def convert_voltage(voltage: int) -> int:
        return voltage * 2

# Пример использования
socket = ElectricSocket()
us_plug = USPlug(110)
adapter = USPlugToEuroSocketAdapter(us_plug)
adapter.plug_into(socket)