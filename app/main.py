from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from uuid import uuid4

app = FastAPI(title="RPN API")
stacks: Dict[str, List[int]] = {}

# --- Models ---
class StackValue(BaseModel):
    value: int

# --- Routes ---

@app.post("/rpn/stack")
def create_stack():
    stack_id = str(uuid4())
    stacks[stack_id] = []
    return {"stack_id": stack_id, "stack": stacks[stack_id]}

@app.get("/rpn/stack")
def list_stacks():
    return {"stacks": list(stacks.keys())}

@app.post("/rpn/stack/{stack_id}")
def push_value(stack_id: str, item: StackValue):
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")
    stacks[stack_id].append(item.value)
    return {"stack_id": stack_id, "stack": stacks[stack_id]}

@app.get("/rpn/stack/{stack_id}")
def get_stack(stack_id: str):
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")
    return {"stack_id": stack_id, "stack": stacks[stack_id]}

@app.delete("/rpn/stack/{stack_id}")
def delete_stack(stack_id: str):
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")
    del stacks[stack_id]
    return {"message": f"Stack {stack_id} deleted."}

@app.get("/rpn/op")
def list_operations():
    return {"operations": ["+", "-", "*", "/"]}

@app.post("/rpn/op/{op}/stack/{stack_id}")
def apply_operation(op: str, stack_id: str):
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")

    stack = stacks[stack_id]
    if len(stack) < 2:
        raise HTTPException(status_code=400, detail="Not enough operands on the stack")

    b = stack.pop()
    a = stack.pop()

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        result = int(a / b)
    else:
        raise HTTPException(status_code=400, detail="Unsupported operation")

    stack.append(result)
    return {"stack_id": stack_id, "stack": stack}
