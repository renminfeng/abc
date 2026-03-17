from __future__ import annotations

import ast


class SafeEvaluator(ast.NodeVisitor):
    """Safely evaluate arithmetic expressions."""

    ALLOWED_BINOPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod)
    ALLOWED_UNARYOPS = (ast.UAdd, ast.USub)

    def visit_Expression(self, node: ast.Expression) -> float:
        return self.visit(node.body)

    def visit_BinOp(self, node: ast.BinOp) -> float:
        if not isinstance(node.op, self.ALLOWED_BINOPS):
            raise ValueError("不支持的运算符")
        left = self.visit(node.left)
        right = self.visit(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            if right == 0:
                raise ValueError("除数不能为 0")
            return left / right
        if isinstance(node.op, ast.Pow):
            return left**right
        if isinstance(node.op, ast.Mod):
            return left % right

        raise ValueError("不支持的运算")

    def visit_UnaryOp(self, node: ast.UnaryOp) -> float:
        if not isinstance(node.op, self.ALLOWED_UNARYOPS):
            raise ValueError("不支持的一元运算符")
        value = self.visit(node.operand)
        return +value if isinstance(node.op, ast.UAdd) else -value

    def visit_Constant(self, node: ast.Constant) -> float:
        if not isinstance(node.value, (int, float)):
            raise ValueError("只允许数字")
        return float(node.value)

    def visit_Num(self, node: ast.Num) -> float:  # pragma: no cover (compat)
        return float(node.n)

    def generic_visit(self, node: ast.AST):
        raise ValueError("表达式包含不允许的内容")


def evaluate_expression(expression: str) -> float:
    if not expression.strip():
        raise ValueError("请输入表达式")

    parsed = ast.parse(expression, mode="eval")
    evaluator = SafeEvaluator()
    return evaluator.visit(parsed)
