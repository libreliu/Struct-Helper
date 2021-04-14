#!/usr/bin/env python3

import sys
import lark

lark_src = None
with open('struct.lark', 'r') as f:
    lark_src = f.read()

struct_parser = lark.Lark(lark_src, start='entry')

source = None
with open(sys.argv[1], 'r') as f:
    source = f.read()

ast = struct_parser.parse(source)
# print(ast)
# print(ast.pretty())

class StructToIR(lark.Transformer):
    def declaration(self, e):
        return {'type': e[0], 'name': e[1]}

    def var_type(self, v):
        return v[0]
    
    def identifier(self, s):
        return str(s[0])
    
    def struct(self, s):
        return {
            'name': s[0],
            'content': s[1:]
        }
    
    def entry(self, e):
        return e[0]


output = StructToIR().transform(ast)
print(output)

def IRToParser(ir):
    struct_name = (ir['name'][0]).lower() + ir['name'][1:]
    struct_member_access = "->"

    code = ""
    for var in ir['content']:
        type = var['type']
        if type == 'String':
            method = 'readString'
        else:
            method = 'read'
        
        code += "reader.{}({}{}{});\n".format(
            method,
            struct_name,
            struct_member_access,
            var['name']
        )
    
    for var in ir['content']:
        type = var['type']
        suffix = ''
        if type == 'String':
            format_op = '%s'
            suffix = '.c_str()'
        elif type == 'F32':
            format_op = '%f'
        elif type == 'F64':
            format_op = '%lf'
        elif type == 'U32' or type =='I32':
            format_op = '%d'
        else:
            raise Exception("Unknown type {}".format(type))
        
        code += 'U3D_DUMP("{}: {}", {});\n'.format(
            var['name'],
            format_op,
            struct_name + struct_member_access + var['name'] + suffix,
        )

    return code

code = IRToParser(output)
print(code)