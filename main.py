from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calculation(BaseModel):
    operation: str
    operands: list[float]

@app.post("/calculate/")
def calculate(calc: Calculation):
    if calc.operation == "add":
        result = sum(calc.operands)
    elif calc.operation == "subtract":
        result = calc.operands[0] - sum(calc.operands[1:])
    elif calc.operation == "multiply":
        result = 1
        for num in calc.operands:
            result *= num
    elif calc.operation == "divide":
        result = calc.operands[0]
        try:
            for num in calc.operands[1:]:
                result /= num
        except ZeroDivisionError:
            return {"error": "Division by zero is not allowed."}
    else:
        return {"error": "Unsupported operation."}
    return {"result": result}
