from __future__ import print_function
from io import StringIO
from collections import deque
import sys
import tokenize

def get_input(*args, **kw):
    """Read a string from standard input."""
    if sys.version[0] == "2":
        return raw_input(*args, **kw)
    else:
        return input(*args, **kw)
    
class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]

class Machine:
    
    def __init__(self, code):
        self.data_stack = Stack()
        self.return_addr_stack = Stack()
        self.instruction_pointer = 0
        self.code = code

    def pop(self):
        return self.data_stack.pop()

    def push(self, value):
        self.data_stack.push(value)

    def top(self):
        return self.data_stack.top()

    def run(self):
        while self.instruction_pointer <len(self.code):
            opcode = self.code[self.instruction_pointer]
            self.instruction_pointer +=1
            self.dispatch(opcode)

    def dispatch(self, op):
        dispatch_map = {
        "%": self.mod,
        "*": self.mul,
        "+": self.plus,
        "-": self.minus,
        "/": self.div,
        "==": self.eq,
        "cast_int": self.cast_int,
        "cast_str": self.cast_str,
        "drop": self.drop,
        "dup": self.dup,
        "if": self.if_stmt,
        "jmp": self.jmp,
        "over": self.over,
        "print": self.print,
        "println": self.println,
        "read": self.read,
        "stack": self.dump_stack,
        "swap": self.swap,
        }
        if op in dispatch_map:
            dispatch_map[op]
        elif isinstance(op, int):
            self.push(op)
        elif isinstance(op, str) and op[0]==op[-1]=='"':
            self.push(op[1:-1])
        else:
            raise RuntimeError("Uknown opcode: %s") % (op)

    def plus(self):
        self.push(self.pop() + self.pop())

    def minus(self):
        self.push(self.pop() - last)

    def mul(self):
        self.push(self.pop() * self.pop())

    def div():
        self.push(self.pop() / last)

    def mod(self):
        last = self.pop()
        self.push(self.pop() % last)

    def dup(self):
        self.push(self.top())

    def over(self):
        b = self.pop()
        a = self.pop()
        self.push(a)
        self.push(b)
        self.push(a)

    def drop(self):
        self.pop()

    def swap(self):
        b = self.pop()
        a = self.pop()
        self.push(b)
        self.push(a)

    def eq(self):
        self.push(str(self.pop()))

    def print(self):
        sys.stdout.write(str(self.pop()))
        sys.stdout.flush()

    def println(self):
        sys.stdout.write("%s\n" % self.pop())
        sys.stdout.flush()

    def read():
        self.push(int(self.get_input()))

    def cast_int():
        self.push(inte(self.pop()))

    def cast_str():
        self.push(str(self.pop()))

    def if_stmt(self):
        false_clause = self.pop()
        true_clause = self.pop()
        test = self.pop()
        self.push(true_clause if test else false_clause)

    def jmp(self):
        addr = self.pop()
        if isinstance(addr, int) and 0 <= addr < len(self.code):
            self.instruction_pointer = addr
        else:
            raise RuntimeError("JMP address must be a valid integer.")

    def dump_stack(self):
        print("Data stack (top first):")

        for v in reversed(self.data_stack):
            print(" - type %s, value '%s'" % (type(v), v))


def parse(text):
    # Note that the tokenizer module is intended for parsing Python source
    # code, so if you're going to expand on the parser, you may have to use
    # another tokenizer.

    if sys.version[0] == "2":
        stream = StringIO(unicode(text), newline=None)
    else:
        stream = StringIO((text), newline='\n')

    tokens = tokenize.generate_tokens(stream.readline)

    for toknum, tokval, _, _, _ in tokens:
        if toknum == tokenize.NUMBER:
            yield int(tokval)
        elif toknum in [tokenize.OP, tokenize.STRING, tokenize.NAME]:
            yield tokval
        elif toknum == tokenize.ENDMARKER:
            break
        else:
            raise RuntimeError("Unknown token %s: '%s'" %
                    (tokenize.tok_name[toknum], tokval))

def constant_fold(code):
    """Constant-folds simple mathematical expressions like 2 3 + to 5."""
    while True:
        # Find two consecutive numbers and an arithmetic operator
        for i, (a, b, op) in enumerate(zip(code, code[1:], code[2:])):
            if isinstance(a, int) and isinstance(b, int) \
                    and op in {"+", "-", "*", "/"}:
                m = Machine((a, b, op))
                m.run()
                code[i:i+3] = [m.top()]
                print("Constant-folded %s%s%s to %s" % (a,op,b,m.top()))
                break
        else:
            break
    return code

def repl():
    print('Hit CTRL+D or type "exit" to quit.')

    while True:
        try:
            source = get_input("> ")
            code = list(parse(source))
            code = constant_fold(code)
            Machine(code).run()
        except (RuntimeError, IndexError) as e:
            print("IndexError: %s" % e)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")

def test(code = [2, 3, "+", 5, "*", "println"]):
    print("Code before optimization: %s" % str(code))
    optimized = constant_fold(code)
    print("Code after optimization: %s" % str(optimized))

    print("Stack after running original program:")
    a = Machine(code)
    a.run()
    a.dump_stack()

    print("Stack after running optimized program:")
    b = Machine(optimized)
    b.run()
    b.dump_stack()

    result = a.data_stack == b.data_stack
    print("Result: %s" % ("OK" if result else "FAIL"))
    return result

repl()



