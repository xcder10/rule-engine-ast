from src.ast_engine import RuleEngine

def main():
    engine = RuleEngine()
    
    rule = "( age > 30 AND department == 'Sales' )"
    ast = engine.create_rule(rule)
    
    print("Generated AST:", ast)
    
    data = {"age": 35, "department": "Sales", "salary": 60000}
    
    result = engine.evaluate_rule(ast, data)
    print("Evaluation Result:", result)
    
if __name__ == "__main__":
    main()