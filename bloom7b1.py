prompt = """
question:查询所有员工的信息, answer:"SELECT * FROM employees;"
question:查询所有年龄大于30岁员工的信息, answer:"SELECT * FROM employees WHERE age > 30;"
question:查询所有员工的姓名和年龄, answer:"SELECT name, age FROM employees;"
question:查询所有年龄大于30岁员工的姓名和年龄, answer:
"""
# pip install -q transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigscience/bloomz-7b1"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

inputs = tokenizer.encode(prompt, return_tensors="pt")
outputs = model.generate(inputs, max_length=100)
full_res = tokenizer.decode(outputs[0])
string = full_res.split(prompt)[1].split("</s>")[0]

import re
match = re.search(r'"(.*)"', string)
if match:
    sql = match.group(1)

print(f"sql:{sql}")
print(tokenizer.decode(outputs[0]))
