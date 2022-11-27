import math
read = False
rfun = []
my_lib = [None]
ret = [None]
lib_name = []
lib_memo = []
global scanned_code

# class Read:
#     word = None
#     type = 0
#     def __repr__(self):
#         return f'{Word}'

class ScannedWord:
    word = None
    type = 0

    def __repr__(self):
        return f'(Word: \'{self.word}\', Type: {self.type})'





class Value:
    val = None
    type = 0

    def __repr__(self):
        return f'(val: \'{self.val}\', Type: {self.type})'

def scan(name):
    file = open(name, 'r', encoding='utf-8')
    glue = [['tr', 'er', 'fa', 'fa', 'fa'], ['tr', 'tr', 'fa', 'fa', 'fa'],
           ['fa', 'fa', 'tr', 'fa', 'fa'],
           ['fa', 'fa', 'fa', 'fa', 'fa'], ['fa', 'fa', 'fa', 'fa', 'fa']]
    current_char = file.read(1)
    # print(file_str)
    words = []
    word = ''
    word_type = 0

    while current_char != '':
        char_type = 0
        # if file_char
        # numbers == 1 , alpha == 2, space ==3
        if current_char.isdigit() or current_char == '.':
            char_type = 1
        elif current_char.isalpha() or "+-*/=!^%{}".__contains__(current_char):
            char_type = 2
        elif current_char.isspace():
            char_type = 3
        elif "()".__contains__(current_char):
            char_type = 4
        elif "\"'".__contains__(current_char):
            char_type = 5
        else:
            char_type = 2
            # print("Error!!!\nunknownchar\n(Er234)")

        if word_type == 0:
            word = current_char
            word_type = char_type
        elif glue[word_type - 1][char_type - 1] == 'tr':
            word += current_char
        elif glue[word_type - 1][char_type - 1] == 'fa':
            word_object = ScannedWord()
            word_object.word = word
            word_object.type = word_type
            words.append(word_object)
            word = current_char
            word_type = char_type
        else:
            print("Error!!!\nnumafterstr\n(Er178)")
        current_char = file.read(1)
        # print(file_str)

    word_object = ScannedWord()
    word_object.word = word
    word_object.type = word_type
    words.append(word_object)
    # print(words)
    return words


def remove_spaces(bad_list):
    good_list = []
    is_str = 0
    str = ''
    for word in bad_list:
        if word.word == '"':
            if is_str == 0:
                is_str = 1
            elif is_str == 1:
                is_str = 0
                l_object = ScannedWord()
                l_object.word = str
                l_object.type = 2
                good_list.append(l_object)
                str = ""
            else:
                str += '"'
        elif word.word == "'":
            if is_str == 0:
                is_str = 2
            elif is_str == 2:
                is_str = 0
                l_object = ScannedWord()
                l_object.word = str
                l_object.type = 2
                good_list.append(l_object)
                str = ''
            else:
                str += '"'
        elif is_str != 0:
            str += f'{word.word}'
        else:
            if word.type != 3 and word.type != 4:
                if word.type == 2:
                    word.type = 6
                good_list.append(word)
    # print(good_list)
    return good_list


def run():
    memo = []
    lib = [0]
    string_commands = ["add", "mul", "sub", "div", "fact", "neg", "pow", "mod",
        "+", "*", "-", "/", "**", "^", "!", "%","--", "=", "!=", "addstr", "+str", "coat", "d-coat",
        "if", "ifdo", "print", "display", "true", "false", "ask-no", "ask", "set", "get",
        "not", "and", "or", "arr", "+item", "index", "fun", "call", "fun-end", "if-end",
        "include", "libin", "libout", "lib", "l-set", "l-get", "{", "}", "return",
        "int", "str", "bool", "float"]
    scanned_code = remove_spaces(scan("code.txt"))
    # print(scanned_code)
    def recursive_run(read):
        if read == True:
            word = scanned_code.pop(0)
            return word
        elif read == False:
            if len(scanned_code) != 0:
                word = scanned_code.pop(0)
            else:
                ans = ScannedWord()
                ans.type = 7
                ans.word = "no"
                word = ans
        elif len(read) != 0:
            if read[0] == True:
                return(read[1].pop(0))
            word = read.pop(0)
        else:
            return False
        if read != True and read != False:
            nextread = read
        else:
            nextread = False
        # print(word, scanned_code)
        if word.type == 6 and word.word in string_commands:
            if word.word == 'add' or word.word == '+':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == "int" and op2.type == "int":
                    ans = Value()
                    ans.val = (op1.val + op2.val)
                    ans.type = "int"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>add\n(Er643)")
            elif word.word == 'addstr' or word.word == '+str':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == "str" and op2.type == "str":
                    ans = Value()
                    ans.val = (op1.val + op2.val)
                    ans.type = "str"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>add\n(Er644)")
            elif word.word == 'mul' or word.word == '*':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == "int" and op2.type == "int":
                    ans = Value()
                    ans.val = (op1.val * op2.val)
                    ans.type = "int"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>mul\n(Er645)")
            elif word.word == 'sub' or word.word == '-':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == "int" and op2.type == "int":
                    ans = Value()
                    ans.val = (op1.val - op2.val)
                    ans.type = "int"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>sub\n(Er646)")
            elif word.word == 'div' or word.word == '/':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == "int" and op2.type == "int" and op2.val != 0:
                    ans = Value()
                    ans.val = (op1.val / op2.val)
                    ans.type = "int"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>div\n(Er647)")
            elif word.word == 'fact' or word.word == '!':
                op1 = recursive_run(nextread)
                if op1.type == "int":
                    ans = Value()
                    ans.val = (math.factorial(op1.val))
                    ans.type = "int"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>fact\n(Er648)")
            elif word.word == 'neg' or word.word == '--':
                op1 = recursive_run(nextread)
                if op1.type == "int":
                    ans = Value()
                    ans.val = (-op1.val)
                    ans.type = "int"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>neg\n(Er649)")
            elif word.word == 'mod' or word.word == '%':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == "int" and op2.type == "int":
                    ans = Value()
                    ans.val = (op1.val % op2.val)
                    ans.type = "int"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>mod\n(Er650)")
            elif word.word == 'pow' or word.word == '^' or word.word == '**':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == "int" and op2.type == "int":
                    ans = Value()
                    ans.val = (op1.val ** op2.val)
                    ans.type = "int"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>pow\n(Er651)")
            # elif word.word == 'pow_n' or word.word == '^n' or word.word == '**n':
            #     op1 = recursive_run(nextread)
            #     op2 = recursive_run(nextread)
            #     ans = op1
            #     for i in range(op2 - 1):
            #         ans = op1 ** ans
            #     return (ans)

            # elif word.word == 'if':
            #     op1 = recursive_run(nextread)
            #     op2 = recursive_run(nextread)
            #     op3 = recursive_run(nextread)
            #     if op1.type == "int" or op1.type == "bool":
            #         if op1.val == 1 or op1 == True:
            #             return op2
            #         else:
            #             return op3
            #     else:
            #         print("Error!!!\nidontknowans=>if\n(Er652)")
            elif word.word == 'if':
                op1 = recursive_run(nextread)
                if op1.type == "int" or op1.type == "bool":
                    if op1.val == 1 or op1 == True:
                        op2 = recursive_run(nextread)
                        rif = op2
                        # ans = Read()
                        # print(rfun)
                        recursive_run(rif)
                    else:
                        op2 = recursive_run(nextread)
                        return op2
                    recursive_run(nextread)
                else:
                    print("Error!!!\nidontknowans=>if\n(Er652)")
            elif word.word == 'print':
                op1 = recursive_run(nextread)
                print(op1.val)
                return op1
            elif word.word == 'display':
                op1 = recursive_run(nextread)
                print(op1.val)
                recursive_run(nextread)
            elif word.word == 'true':
                ans = Value()
                ans.val = True
                ans.type = "bool"
                return ans
            elif word.word == 'false':
                ans = Value()
                ans.val = False
                ans.type = "bool"
                return ans
            elif word.word == '=':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == op2.type:
                    ans = Value()
                    ans.val = op1.val == op2.val
                    ans.type = "bool"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>equ\n(Er653)")
            elif word.word == '!=':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == op2.type:
                    ans = Value()
                    ans.val = op1.val != op2.val
                    ans.type = "bool"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>!equ\n(Er654)")
            elif word.word == 'and':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == "bool" and op2.type == "bool":
                    ans = Value()
                    ans.val = (op1.val and op2.val)
                    ans.type = "bool"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>and\n(Er655)")
            elif word.word == 'or':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type == "bool" and op2.type == "bool":
                    ans = Value()
                    ans.val = (op1.val or op2.val)
                    ans.type = "bool"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>or\n(Er656)")
            elif word.word == 'not':
                op1 = recursive_run(nextread)
                if op1.type == "bool":
                    ans = Value()
                    ans.val = (not op1.val)
                    ans.type = "bool"
                    return ans
                else:
                    print("Error!!!\nidontknowans=>not\n(Er657)")
            elif word.word == 'ask-no':
                op1 = recursive_run(nextread)
                ans = Value()
                ans.val = (float(input(op1.val)))
                ans.type = "bool"
                return ans
            elif word.word == 'ask':
                op1 = recursive_run(nextread)
                ans = Value()
                ans.val = (input(op1.val))
                ans.type = "bool"
                return ans
            elif word.word == 'set':
                #print(memo)
                #op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                op3 = recursive_run(nextread)
                if op2.type != 'int':
                    print("Error!!!\nidontknowdata=>set\n(Er658)")
                while len(memo) < op2.val:
                    memo.append('')
                # if op1.val == 'no':
                #     ans = Value()
                #     ans.val = int(op3)
                #     ans.type = "int"
                #     memo[op2.val-1] = ans
                # elif op1.val in ['str', 'array', 'fun']:
                memo[op2.val-1] = op3
                # else:
                #     print("Error!!!\nidontknowdata=>set\n(Er659)")
                # print(memo)
                recursive_run(nextread)
            elif word.word == 'get':
                op1 = recursive_run(nextread)
                return memo[op1.val - 1]
            elif word.word == 'arr':
                arr = []
                op1 = recursive_run(nextread)
                if op1.type != 'int':
                    print("Error!!!\nidontknowdata=>set\n(Er660)")
                for i in range(op1.val):
                    op2 = recursive_run(nextread)
                    arr.append(op2)
                ans = Value()
                ans.val = arr
                ans.type = 'arr'
                return ans
            elif word.word == '+item':
                arr = recursive_run(nextread)
                op1 = recursive_run(nextread)
                if arr.type != 'arr' or op1.type != 'int':
                    print("Error!!!\nidontknowdata=>+item\n(Er661)")
                for i in range(op1.val):
                    op2 = recursive_run(nextread)
                    arr.val.append(op2)
                return arr
            elif word.word == 'index':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if (op1.type != 'arr' and op1.type != 'str') or op2.type != 'int':
                    print("Error!!!\nidontknowdata=>index\n(Er662)")
                return op1[op2]
            elif word.word == 'fun':
                fun = []
                while True:
                    if nextread != False:
                        op1 = recursive_run(nextread)
                    else:
                        op1 = recursive_run(True)
                    # print(op1, 'op1')
                    if op1.word == 'fun-end':
                        break
                    else:
                        fun_object = ScannedWord()
                        fun_object.word = word.word
                        fun_object.type = word.type
                        fun.append(op1)
                return fun
            elif word.word == '{':
                fun = []
                counter = 1
                while True:
                    if nextread != False:
                        op1 = recursive_run(nextread)
                    else:
                        op1 = recursive_run(True)
                    # print(op1, 'op1')
                    if op1.word == '{':
                        counter += 1
                    elif op1.word == '}':
                        counter -= 1
                    else:
                        fun_object = ScannedWord()
                        fun_object.word = word.word
                        fun_object.type = word.type
                        fun.append(op1)
                    if counter == 0:
                        break
                return fun
            elif word.word == 'call':
                ans = ScannedWord()
                ans.word = ""
                ans.type = 7
                ret[0]= ans
                op1 = recursive_run(nextread)
                # print(op1.val - 1, memo)
                rfun = memo[op1.val - 1]
                # ans = Read()
                # print(rfun)
                op2 = recursive_run(rfun)
                # recursive_run(nextread)
                if ret[0].type == 7:
                    recursive_run(nextread)
                else:
                    return ret[0]
            elif word.word == 'coat':
                ans = Value()
                ans.val = "'"
                ans.type = 'str'
                return ans
            elif word.word == 'd-coat':
                ans = Value()
                ans.val = '"'
                ans.type = 'str'
                return ans
            elif word.word == 'include':
                # print('in')
                op1 = recursive_run(nextread)
                Lib = remove_spaces(scan(f"lib/{op1.val}/code.txt"))
                lib_name.append(op1.val)
                lib_memo.append([])
                my_lib[0]= op1.val
                # print(my_lib[0])
                # Lib.extend(scanned_code)
                # print(Lib)
                # ans = Read
                # ans.word = Lib
                # ans.type = True
                # recursive_run(ans)
                for i in reversed(Lib):
                    scanned_code.insert(0, i)
                # print(scanned_code)
                op2 = recursive_run(nextread)
            elif word.word == 'libin':
                op1 = recursive_run(nextread)
                lib[0] = op1
                # print(lib[0])
                recursive_run(nextread)
            elif word.word == 'libout':
                # print(lib)
                return lib[0]
            elif word.word == 'lib':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                # print(op1)
                if op2.type != 'int':
                    print("Error!!!\nidontknowdata=>set\n(Er663)")
                recursive_run(lib_memo[lib_name.index(op1.val)][op2.val - 1])
                recursive_run(nextread)
            elif word.word == 'l-set':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op1.type != 'int':
                    print("Error!!!\nidontknowdata=>set\n(Er664)")
                while len(lib_memo[lib_name.index(my_lib[0])]) < op1.val:
                    # print(len(lib_memo[lib_name.index(my_lib[0])]))
                    lib_memo[lib_name.index(my_lib[0])].append('')
                # print(lib_memo)
                lib_memo[lib_name.index(my_lib[0])][op1.val - 1] = op2
                recursive_run(nextread)
            elif word.word == 'l-get':
                op1 = recursive_run(nextread)
                op2 = recursive_run(nextread)
                if op2.type != 'int':
                    print("Error!!!\nidontknowdata=>set\n(Er664)")
                return lib_memo[lib_name.index(op1)][op2 - 1]
            elif word.word == 'return':
                ret[0] = recursive_run(nextread)
            elif word.word == 'int':
                op1 = recursive_run(nextread)
                op1.type = 'int'
                op1.val = int(float(op1.val))
                return op1
            elif word.word == 'str':
                op1 = recursive_run(nextread)
                op1.type = 'str'
                op1.val = str(op1.val)
                return op1
            elif word.word == 'bool':
                op1 = recursive_run(nextread)
                op1.type = 'bool'
                op1.val = bool(op1.val)
                return op1
            elif word.word == 'float':
                op1 = recursive_run(nextread)
                op1.type = 'int'
                op1.val = float(op1.val)
                return op1






        elif word.type == 1:
            int_object = Value()
            if float(word.word) % 1 != 0:
                int_object.val = float(word.word)
            else:
                int_object.val = int(float(word.word))
            int_object.type = 'int'
            return int_object
        elif word.type == 2 and not word.word in string_commands:
            str_object = Value()
            str_object.val = word.word
            str_object.type = 'str'
            return str_object
    while len(scanned_code) != 0:
        recursive_run(False)
    # return recursive_run(False)


run()
# def baz(num):
#     if num != 0:
#         print(num * ' ' + 'hello')
#         baz(num - 1)
#         print(num * ' ' + 'bye')

# print(scan("code.txt"))
