# Rule Engine with AST

## Description
This project is a 3-tier rule engine that uses an Abstract Syntax Tree (AST) to dynamically create and evaluate rules.

## Setup
1.create project folder
2.create various folders
3.initialize git repository
4.create required files
5.setup virtual enviroment
6.install dependencies(unittest)
7.implementing the code --> ast data structure
                        --> writing tests cases
8.running the application
{all codes provided} 

## Sample tests
from src.ast_engine import RuleEngine
engine = RuleEngine()
rule = "( age > 30 AND department == 'Sales' )"
ast = engine.create_rule(rule)
data = {"age": 35, "department": "Sales", "salary": 60000}
result = engine.evaluate_rule(ast, data)
print("Result:", result)  # Should print: True

thank you for reading
