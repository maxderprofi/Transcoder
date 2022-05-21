import math

class NumberNode:
  def __init__(self, tok):
    self.tok = tok

    # self.pos_start = self.tok.pos_start
    # self.pos_end = self.tok.pos_end

  def __repr__(self):
    return f'{self.tok}'

class StringNode:
  def __init__(self, tok):
    self.tok = tok

    self.pos_start = self.tok.pos_start
    self.pos_end = self.tok.pos_end

  def __repr__(self):
    return f'{self.tok}'

class ListNode:
  def __init__(self, element_nodes, pos_start, pos_end):
    self.element_nodes = element_nodes

    self.pos_start = pos_start
    self.pos_end = pos_end

class VarAccessNode:
  def __init__(self, var_name_tok):
    self.var_name_tok = var_name_tok

    self.pos_start = self.var_name_tok.pos_start
    self.pos_end = self.var_name_tok.pos_end

class VarAssignNode:
  def __init__(self, var_name_tok, value_node):
    self.var_name_tok = var_name_tok
    self.value_node = value_node

    self.pos_start = self.var_name_tok.pos_start
    self.pos_end = self.value_node.pos_end

class BinOpNode:
  def __init__(self, left_node, op_tok, right_node):
    self.left_node = left_node
    self.op_tok = op_tok
    self.right_node = right_node

    self.pos_start = self.left_node.pos_start
    self.pos_end = self.right_node.pos_end

  def __repr__(self):
    return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class UnaryOpNode:
  def __init__(self, op_tok, node):
    self.op_tok = op_tok
    self.node = node

    self.pos_start = self.op_tok.pos_start
    self.pos_end = node.pos_end

  def __repr__(self):
    return f'({self.op_tok}, {self.node})'

class IfNode:
  def __init__(self, cases, else_case):
    self.cases = cases
    self.else_case = else_case

    self.pos_start = self.cases[0][0].pos_start
    self.pos_end = (self.else_case or self.cases[len(self.cases) - 1])[0].pos_end

class ForNode:
  def __init__(self, var_name_tok, start_value_node, end_value_node, step_value_node, body_node, should_return_null):
    self.var_name_tok = var_name_tok
    self.start_value_node = start_value_node
    self.end_value_node = end_value_node
    self.step_value_node = step_value_node
    self.body_node = body_node
    self.should_return_null = should_return_null

    self.pos_start = self.var_name_tok.pos_start
    self.pos_end = self.body_node.pos_end

class WhileNode:
  def __init__(self, condition_node, body_node, should_return_null):
    self.condition_node = condition_node
    self.body_node = body_node
    self.should_return_null = should_return_null

    self.pos_start = self.condition_node.pos_start
    self.pos_end = self.body_node.pos_end

class FuncDefNode:
  def __init__(self, var_name_tok, arg_name_toks, body_node, should_auto_return):
    self.var_name_tok = var_name_tok
    self.arg_name_toks = arg_name_toks
    self.body_node = body_node
    self.should_auto_return = should_auto_return

    if self.var_name_tok:
      self.pos_start = self.var_name_tok.pos_start
    elif len(self.arg_name_toks) > 0:
      self.pos_start = self.arg_name_toks[0].pos_start
    else:
      self.pos_start = self.body_node.pos_start

    self.pos_end = self.body_node.pos_end

class CallNode:
  def __init__(self, node_to_call, arg_nodes):
    self.node_to_call = node_to_call
    self.arg_nodes = arg_nodes

    self.pos_start = self.node_to_call.pos_start

    if len(self.arg_nodes) > 0:
      self.pos_end = self.arg_nodes[len(self.arg_nodes) - 1].pos_end
    else:
      self.pos_end = self.node_to_call.pos_end

class ReturnNode:
  def __init__(self, node_to_return, pos_start, pos_end):
    self.node_to_return = node_to_return

    self.pos_start = pos_start
    self.pos_end = pos_end

class ContinueNode:
  def __init__(self, pos_start, pos_end):
    self.pos_start = pos_start
    self.pos_end = pos_end

class BreakNode:
  def __init__(self, pos_start, pos_end):
    self.pos_start = pos_start
    self.pos_end = pos_end




class Value:
  def __init__(self):
    self.set_pos()
    self.set_context()

  def set_pos(self, pos_start=None, pos_end=None):
    self.pos_start = pos_start
    self.pos_end = pos_end
    return self

  def set_context(self, context=None):
    self.context = context
    return self

  def added_to(self, other):
    return None, self.illegal_operation(other)

  def subbed_by(self, other):
    return None, self.illegal_operation(other)

  def multed_by(self, other):
    return None, self.illegal_operation(other)

  def dived_by(self, other):
    return None, self.illegal_operation(other)

  def powed_by(self, other):
    return None, self.illegal_operation(other)

  def get_comparison_eq(self, other):
    return None, self.illegal_operation(other)

  def get_comparison_ne(self, other):
    return None, self.illegal_operation(other)

  def get_comparison_lt(self, other):
    return None, self.illegal_operation(other)

  def get_comparison_gt(self, other):
    return None, self.illegal_operation(other)

  def get_comparison_lte(self, other):
    return None, self.illegal_operation(other)

  def get_comparison_gte(self, other):
    return None, self.illegal_operation(other)

  def anded_by(self, other):
    return None, self.illegal_operation(other)

  def ored_by(self, other):
    return None, self.illegal_operation(other)

  def notted(self, other):
    return None, self.illegal_operation(other)

  def execute(self, args):
    return RTResult().failure(self.illegal_operation())

  def copy(self):
    raise Exception('No copy method defined')

  def is_true(self):
    return False

  def illegal_operation(self, other=None):
    if not other: other = self
    return RTError(
      self.pos_start, other.pos_end,
      'Illegal operation',
      self.context
    )


class Number(Value):
  def __init__(self, value):
    super().__init__()
    self.value = value

  def added_to(self, other):
    if isinstance(other, Number):
      return Number(self.value + other.value).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def bor_to(self, other):
    if isinstance(other, Number):
      return Number(self.value | other.value).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def subbed_by(self, other):
    if isinstance(other, Number):
      return Number(self.value - other.value).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def multed_by(self, other):
    if isinstance(other, Number):
      return Number(self.value * other.value).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def dived_by(self, other):
    if isinstance(other, Number):
      if other.value == 0:
        return None, RTError(
          other.pos_start, other.pos_end,
          'Division by zero',
          self.context
        )

      return Number(self.value / other.value).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def powed_by(self, other):
    if isinstance(other, Number):
      return Number(self.value ** other.value).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def get_comparison_eq(self, other):
    if isinstance(other, Number):
      return Number(int(self.value == other.value)).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def get_comparison_ne(self, other):
    if isinstance(other, Number):
      return Number(int(self.value != other.value)).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def get_comparison_lt(self, other):
    if isinstance(other, Number):
      return Number(int(self.value < other.value)).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def get_comparison_gt(self, other):
    if isinstance(other, Number):
      return Number(int(self.value > other.value)).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def get_comparison_lte(self, other):
    if isinstance(other, Number):
      return Number(int(self.value <= other.value)).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def get_comparison_gte(self, other):
    if isinstance(other, Number):
      return Number(int(self.value >= other.value)).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def anded_by(self, other):
    if isinstance(other, Number):
      return Number(int(self.value and other.value)).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def ored_by(self, other):
    if isinstance(other, Number):
      return Number(int(self.value or other.value)).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def notted(self):
    return Number(1 if self.value == 0 else 0).set_context(self.context), None

  def copy(self):
    copy = Number(self.value)
    copy.set_pos(self.pos_start, self.pos_end)
    copy.set_context(self.context)
    return copy

  def is_true(self):
    return self.value != 0

  def __str__(self):
    return str(self.value)

  def __repr__(self):
    return str(self.value)

Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)
Number.math_PI = Number(math.pi)

class String(Value):
  def __init__(self, value):
    super().__init__()
    self.value = value

  def added_to(self, other):
    if isinstance(other, String):
      return String(self.value + other.value).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def multed_by(self, other):
    if isinstance(other, Number):
      return String(self.value * other.value).set_context(self.context), None
    else:
      return None, Value.illegal_operation(self, other)

  def is_true(self):
    return len(self.value) > 0

  def copy(self):
    copy = String(self.value)
    copy.set_pos(self.pos_start, self.pos_end)
    copy.set_context(self.context)
    return copy

  def __str__(self):
    return self.value

  def __repr__(self):
    return f'"{self.value}"'

class List(Value):
  def __init__(self, elements):
    super().__init__()
    self.elements = elements

  def added_to(self, other):
    new_list = self.copy()
    new_list.elements.append(other)
    return new_list, None

  def subbed_by(self, other):
    if isinstance(other, Number):
      new_list = self.copy()
      try:
        new_list.elements.pop(other.value)
        return new_list, None
      except:
        return None, RTError(
          other.pos_start, other.pos_end,
          'Element at this index could not be removed from list because index is out of bounds',
          self.context
        )
    else:
      return None, Value.illegal_operation(self, other)

  def multed_by(self, other):
    if isinstance(other, List):
      new_list = self.copy()
      new_list.elements.extend(other.elements)
      return new_list, None
    else:
      return None, Value.illegal_operation(self, other)

  def dived_by(self, other):
    if isinstance(other, Number):
      try:
        return self.elements[other.value], None
      except:
        return None, RTError(
          other.pos_start, other.pos_end,
          'Element at this index could not be retrieved from list because index is out of bounds',
          self.context
        )
    else:
      return None, Value.illegal_operation(self, other)

  def copy(self):
    copy = List(self.elements)
    copy.set_pos(self.pos_start, self.pos_end)
    copy.set_context(self.context)
    return copy

  def __str__(self):
    return ", ".join([str(x) for x in self.elements])

  def __repr__(self):
    return f'[{", ".join([repr(x) for x in self.elements])}]'

class BaseFunction(Value):
  def __init__(self, name):
    super().__init__()
    self.name = name or "<anonymous>"

  def generate_new_context(self):
    new_context = Context(self.name, self.context, self.pos_start)
    new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
    return new_context

  def check_args(self, arg_names, args):
    res = RTResult()

    if len(args) > len(arg_names):
      return res.failure(RTError(
        self.pos_start, self.pos_end,
        f"{len(args) - len(arg_names)} too many args passed into {self}",
        self.context
      ))

    if len(args) < len(arg_names):
      return res.failure(RTError(
        self.pos_start, self.pos_end,
        f"{len(arg_names) - len(args)} too few args passed into {self}",
        self.context
      ))

    return res.success(None)

  def populate_args(self, arg_names, args, exec_ctx):
    for i in range(len(args)):
      arg_name = arg_names[i]
      arg_value = args[i]
      arg_value.set_context(exec_ctx)
      exec_ctx.symbol_table.set(arg_name, arg_value)

  def check_and_populate_args(self, arg_names, args, exec_ctx):
    res = RTResult()
    res.register(self.check_args(arg_names, args))
    if res.should_return(): return res
    self.populate_args(arg_names, args, exec_ctx)
    return res.success(None)

class Function(BaseFunction):
  def __init__(self, name, body_node, arg_names, should_auto_return):
    super().__init__(name)
    self.body_node = body_node
    self.arg_names = arg_names
    self.should_auto_return = should_auto_return

  def execute(self, args):
    res = RTResult()
    interpreter = Interpreter()
    exec_ctx = self.generate_new_context()

    res.register(self.check_and_populate_args(self.arg_names, args, exec_ctx))
    if res.should_return(): return res

    value = res.register(interpreter.visit(self.body_node, exec_ctx))
    if res.should_return() and res.func_return_value == None: return res

    ret_value = (value if self.should_auto_return else None) or res.func_return_value or Number.null
    return res.success(ret_value)

  def copy(self):
    copy = Function(self.name, self.body_node, self.arg_names, self.should_auto_return)
    copy.set_context(self.context)
    copy.set_pos(self.pos_start, self.pos_end)
    return copy

  def __repr__(self):
    return f"<function {self.name}>"

class BuiltInFunction(BaseFunction):
  def __init__(self, name):
    super().__init__(name)

  def execute(self, args):
    res = RTResult()
    exec_ctx = self.generate_new_context()

    method_name = f'execute_{self.name}'
    method = getattr(self, method_name, self.no_visit_method)

    res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
    if res.should_return(): return res

    return_value = res.register(method(exec_ctx))
    if res.should_return(): return res
    return res.success(return_value)

  def no_visit_method(self, node, context):
    raise Exception(f'No execute_{self.name} method defined')

  def copy(self):
    copy = BuiltInFunction(self.name)
    copy.set_context(self.context)
    copy.set_pos(self.pos_start, self.pos_end)
    return copy

  def __repr__(self):
    return f"<built-in function {self.name}>"
