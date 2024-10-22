class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # 'operator' or 'operand'
        self.value = value     # value if it's an operand (eg. 'age>30')
        self.left = left       # left child node
        self.right = right     # right child node
        
    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"
    
class RuleEngine:
    def create_rule(self, rule_string):
        """Parses the rule string into an AST."""
        tokens = rule_string.replace("(","( ").replace(")", " )").split()
        return self._parse(tokens)
    
    def _parse(self, tokens):
        """Recursively builds as AST from then token list."""
        token = tokens.pop(0)
        if token == "(":
            left = self._parse(tokens)
            operator = tokens.pop(0)
            right = self._parse(tokens)
            tokens.pop(0) #discard ')'
            return Node("operator", operator, left, right)
        return Node("operand", token)
    
    def evaluate_rule(self, node, data):
        """Evaluates the AST against provided data."""
        if node.type == "operand":
            return eval(node.value, {}, data)  #unsafe, for demo only
        left_val = self.evaluate_rule(node.left, data)
        right_val = self.evaluate_rule(node.right, data)
        if node.value == "AND":
            return left_val and right_val
        elif node.value == "OR":
            return left_val or right_val
        else:
            raise ValueError(f"Unknown operator: {node.value}")
        
    def combine_rules(self, rules):
        """Combines multiple rules into a single AST."""
        combined_root = Node("operator", "AND")
        for rule in rules:
            combined_root.left = combined_root.left or self.create_rule(rule)
            combined_root.right = self.create_rule(rule)
        return combined_root