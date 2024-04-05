from Model.modelo import Compuertas
from prettytable import PrettyTable

class Controller:
    def __init__(self):
        self.puertos = {}
        self.diccionario()

    @staticmethod
    def truth_table_AND():
        table_AND = PrettyTable()
        table_AND.field_names = ["A", "B", "A AND B"]
        for a in [False, True]:
            for b in [False, True]:
                result = a and b
                table_AND.add_row([a, b, result])
        return table_AND

    @staticmethod
    def truth_table_OR():
        table_OR = PrettyTable()
        table_OR.field_names = ["A", "B", "A OR B"]
        for a in [False, True]:
            for b in [False, True]:
                result = a or b
                table_OR.add_row([a, b, result])
        return table_OR

    @staticmethod
    def truth_table_NOT():
        table_NOT = PrettyTable()
        table_NOT.field_names = ["A", "NOT A"]
        for a in [False, True]:
            result = not a
            table_NOT.add_row([a, result])
        return table_NOT
    
    @staticmethod
    def truth_table_XOR():
        table_XOR = PrettyTable()
        table_XOR.field_names = ["A", "B", "A XOR B"]
        for a in [False, True]:
            for b in [False, True]:
                result = a ^ b
                table_XOR.add_row([a, b, result])
        return table_XOR
    
    @staticmethod
    def truth_table_NAND():
        table_NAND = PrettyTable()
        table_NAND.field_names = ["A", "B", "A NAND B"]
        for a in [False, True]:
            for b in [False, True]:
                result = not (a and b)
                table_NAND.add_row([a, b, result])
            return table_NAND
        
    @staticmethod
    def truth_table_NOR():
        table_NOR = PrettyTable()
        table_NOR.field_names = ["A", "B", "A NOR B"]
        for a in [False, True]:
            for b in [False, True]:
                result = not (a or b)
                table_NOR.add_row([a, b, result])
        return table_NOR


    def diccionario(self):
        self.puertos = {
            "and": Compuertas(
                nombre="Puerta Lógica AND",
                axioma="z=a.b",
                simbolo = '../image/and_gate.png',
                tabla=self.truth_table_AND()
            ),
            "or": Compuertas(
                nombre="Puerta Lógica OR",
                axioma="z=a+b",
                simbolo="../image/or_gate.png",
                tabla=self.truth_table_OR()
            ),
            "xor": Compuertas(
                nombre="Puerta Lógica xOR",
                axioma="Z=Ā.b+a.B̄",
                simbolo="../image/xor_gate.png",
                tabla=self.truth_table_AND()
            ),
            "not": Compuertas(
                nombre="Puerta Lógica NOT",
                axioma="Z=Ā",
                simbolo="../image/not_gate.png",
                tabla=self.truth_table_NOT()
            ),
            "nand": Compuertas(
                nombre="Puerta Lógica NAND",
                axioma="Z=Ā.B̄",
                simbolo="../image/nand_gate.png",
                tabla="•=0"
            ),
            "nor": Compuertas(
                nombre="Puerta Lógica NOR",
                axioma="Z=Ā+B̄",
                simbolo="../image/nor_gate.png",
                tabla=">=0"
            )
        }
        return self.puertos
    
    def get_compuerta(self, value):
        if value in self.puertos:
            return self.puertos[value]
        else:
            return None
        
    