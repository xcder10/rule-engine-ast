import unittest
from src.ast_engine import RuleEngine

class TestRuleEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RuleEngine()
        
    def test_create_rule(self):
        rule = "( age > 30 AND department == 'Sales' )"
        ast = self.engine.create_rule(rule)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.value, "AND")
        
    def test_evaluate_rule(self):
        rule = "( age > 30 AND department == 'Sales' )"
        ast = self.engine.create_rule(rule)
        data = {"age": 35, "department": "Sales"}
        result = self.engine.evaluate_rule(ast, data)
        self.assertTrue(result)
        
    def test_combine_rules(self):
        rules = [ "( age > 30 AND department == 'Sales' )", "( salary > 50000 OR experience > 5 )"]
        combined_ast = self.engine.combine_rules(rules)
        self.assertIsNotNone(combined_ast)
        
if __name__ == "__main__":
    unittest.main()