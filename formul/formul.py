# -*- coding: cp1251 -*-
from sympy import *
from sympy.parsing.sympy_parser import *
import sympy as sympy

def spliter(inp,splsym=list(('*','+','-','/','.'))):
    postr = inp.split('\n')
    res = str()
    for i in postr:
        #сколько табов сначала
        tabs = 0
        for j in i:
            if(j=='\t'):
                tabs+=1
            else:
                break
        strs = i
        if(len(strs)>(79-3*tabs)):
            maxspl = -1;
            for j in splsym:
                a = strs.rfind(j,0,79-3*tabs)
                if(a>maxspl):
                    maxspl=a
            if(maxspl!=-1):
                res+=strs[:maxspl+1]+'\n'
                strs = strs[maxspl+1:]

                while(len(strs)>(79-3*(tabs+1))):
                    maxspln = -1;
                    for j in splsym:
                        a = strs.rfind(j,0,79-4*(tabs+1))
                        if(a>maxspln):
                            maxspln=a
                    if(maxspln!=-1):
                        res+=('\t'*(tabs+1))+strs[:maxspln+1]+'\n'
                        strs = strs[maxspln+1:]
                    else:
                        print("Проблема разделения строки"+strs)
                        break
                res+=('\t'*(tabs+1))+strs+'\n';
            else:
                res+=i+'\n'
                print("Проблема разделения строки"+i)
        else:
            res+=i+'\n'
    return res

def latinizator(letter):
    #в переменных методисты часто используют кирилицу. В названиях переменных
    #её использовать нельзя. Такой стыренный велосипед для этого
    legend = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'zh',
        'з':'z','и':'i', 'й':'y', 'к':'k', 'л':'l','м':'m','н':'n','о':'o','п':'p',
        'р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'c','ч':'ch','ш':'sh',
        'щ':'shch','ъ':'y','ы':'y','э':'e','ю':'yu','я':'ya','А':'A',
        'Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'Yo','Ж':'Zh','З':'Z','И':'I',
        'Й':'Y','К':'K','Л':'L','М':'M','Н':'N','О':'O','П':'P','Р':'R','С':'S',
        'Т':'T','У':'U','Ф':'F','Х':'H','Ц':'Ts','Ч':'Ch','Ш':'Sh','Щ':'Shch',
        'Ъ':'Y','Ы':'Y','Э':'E','Ю':'Yu','Я':'Ya',}
    for i, j in legend.items():
        letter = letter.replace(i, j)
    return letter

def tochupro(expr,prevfunc = None, frac=False, **keywords):
    #recursive
    res = str()
    if(expr == -1):
        if (prevfunc!=None and prevfunc.is_Mul):
            return "|\"-\"|"
        else:
            return "|\""+str(expr)+"\"|"
    elif(expr.is_Integer):
        return "|\""+str(expr)+"\"|"
    elif(expr.is_Rational):
        return "|frac_|"+"\""+str(expr.p)+"\""+"|_frac_|"+"\""+str(expr.q)+"\""+"|_frac|"
    elif(expr.is_Symbol):
        return replsym(expr)
    elif(expr.is_Add):
        if(prevfunc!=None):
            if((prevfunc.is_Mul or prevfunc.is_Pow) and not frac):
                res+="|\"(\"|"
        if(len(expr.args)>0):
            res+=tochupro(expr.args[0],expr.func)
            for i in range(1,len(expr.args)):
                if(expr.args[i].is_Mul and expr.args[i].args[0].is_real and expr.args[i].args[0]<0):
                    res+="|\"-\"|"+tochupro(Mul(-1,expr.args[i]),expr.func)
                else:
                    res+="|\"+\"|"+tochupro(expr.args[i],expr.func)
        if(prevfunc!=None):
            if((prevfunc.is_Mul or prevfunc.is_Pow) and not frac):
                res+="|\")\"|"
    elif(expr.is_Mul):
        #а вот тут еще с делением нужно разобраться
        div = False
        sqrt = False
        nom = Integer(1)
        denom = Integer(1)
        sqrtnom = Integer(1)
        sqrtdenom = Integer(1)
        sk = (prevfunc!=None and prevfunc.is_Pow and 'osn' in keywords and keywords['osn'])
        if(sk):
            res+='|"("|'
        for i in expr.args:
            if(i.is_Pow and (i.args[1].is_real and i.args[1] < 0)):
                if(i.args[1] == -1 and str(i.args[0].func)=='Sqrt'):
                    sqrt=True
                    sqrtdenom = Mul(sqrtdenom,i.args[0].args[0])
                else:
                    denom = Mul(denom,Pow(i.args[0],i.args[1].__abs__()))
                    div = True
            elif(i.is_Rational):
                if(i.q>1):
                    div = True
                if(i.p != 1):
                    nom = Mul(nom,i.p)
                denom = Mul(denom,i.q)
            elif(str(i.func) == 'Sqrt'):
                sqrt = True
                sqrtnom=Mul(sqrtnom,i.args[0])
            elif(i.is_Mul):
                #что-то придумать тут. Хорошо бы рекурсивный разбор
                #временный велосипед. Надо бы пофиксить как-нибудь
                for j in i.args:
                    if(j.is_Pow and (j.args[1].is_real and j.args[1] < 0)):
                        if(j.args[1] == -1 and str(j.args[0].func)=='Sqrt'):
                            sqrt=True
                            sqrtdenom = Mul(sqrtdenom,j.args[0].args[0])
                        else:
                            denom = Mul(denom,Pow(j.args[0],j.args[1].__abs__()))
                            div = True
                    else:
                        if(j!=1):
                            nom=Mul(nom,j)
            else:
                if(i!=1):
                    nom=Mul(nom,i)
        if(sqrt == False):
            if(div == False):
                #тогда умножение
                for i in expr.args:
                    res+="|"+tochupro(i,expr.func)+"|"
            elif(denom!=1):
                res+="|frac_|"+tochupro(nom,expr.func,True)+"|_frac_|"+tochupro(denom,expr.func,True)+"|_frac|"
        else:
            if(nom == 1 and sqrtdenom == 1):
                res+="|frac_|"+tochupro(Function('Sqrt')(sqrtnom))+"|_frac_|"+tochupro(denom,expr.func,True)+"|_frac|"
            else:
                if(nom/denom!=1):
                    res+="|"+tochupro(nom/denom,expr.func)
                res+="|"+tochupro(Function('Sqrt')(sqrtnom/sqrtdenom))+"|"
        if(sk):
            res+='|")"|'

    elif(expr.is_Pow):
        exarg1 = simplify(expr.args[1])
        if(exarg1.is_real):
            if(exarg1 == 2):
                res+="|"+tochupro(expr.args[0],expr.func,osn=True)+"|up2|"
            elif(exarg1 == -1):
                res+="|frac_|1|_frac_|"+tochupro(expr.args[0],expr.func)+"|_frac|"
            elif(exarg1 == 1/2):
                res+="|sqrt_|"+tochupro(expr.args[0],expr.func,True)+"|_sqrt|"
            elif(exarg1 == 1/3):
                res+="|curt_|"+tochupro(expr.args[0],expr.func,True)+"|_curt|"
            elif(exarg1<0):
                res+="|frac_|1|_frac_|"+tochupro(Pow(expr.args[0],exarg1.__abs__()),expr.func)+"|_frac|"
            elif(exarg1.is_Rational):
                if(exarg1.q>1):
                    if(exarg1.q==2):
                        res+="|sqrt_|"+tochupro(Pow(expr.args[0],exarg1.p),expr.func)+"|_sqrt|"
                    elif(exarg1.q==3):
                        res+="|curt_|"+tochupro(Pow(expr.args[0],exarg1.p),expr.func)+"|_curt|"
                    else:
                        res+="|root_|"+tochupro(Integer(exarg1.q),expr.func)+"|_root_|"+tochupro(Pow(expr.args[0],exarg1.p),expr.func) +"|_root|"
                else:
                    res+="|"+tochupro(expr.args[0],expr.func,osn=True)+"|up_|"+tochupro(expr.args[1],expr.func)+"|_up|"
            else:
                res+="|"+tochupro(expr.args[0],expr.func,osn=True)+"|up_|"+tochupro(expr.args[1],expr.func)+"|_up|"
        else:
            res+="|"+tochupro(expr.args[0],expr.func,osn=True)+"|up_|"+tochupro(expr.args[1],expr.func)+"|_up|"
    elif(str(expr.func) == 'Sqrt'):
        res+="|sqrt_|"+tochupro(expr.args[0],expr.func,True)+"|_sqrt|"

    elif(str(expr.func) == 'Sin' or str(expr.func) == 'sin'):
        res+="|func.sin|\"(\""+tochupro(expr.args[0],expr.func,True)+"|\")\"|"
    elif(str(expr.func) == 'Cos' or str(expr.func) == 'cos'):
        res+="|func.cos|\"(\""+tochupro(expr.args[0],expr.func,True)+"|\")\"|"

    elif(str(expr.func) in ('Arcsin', 'arcsin', 'Asin', 'asin')):
        res+="|func.arcsin|\"(\""+tochupro(expr.args[0],expr.func,True)+"|\")\"|"
    elif(str(expr.func) in ('Arccos', 'arccos', 'Acos', 'acos')):
        res+="|func.arccos|\"(\""+tochupro(expr.args[0],expr.func,True)+"|\")\"|"

    elif(str(expr.func) in ('Tg', 'tg', 'Tan', 'tan')):
        res+="|func.tg|\"(\""+tochupro(expr.args[0],expr.func,True)+"|\")\"|"
    elif(str(expr.func) == 'Ctg' or str(expr.func) == 'ctg'):
        res+="|func.ctg|\"(\""+tochupro(expr.args[0],expr.func,True)+"|\")\"|"

    elif(str(expr.func) in ('Arctg', 'arctg', 'Atan', 'atan')):
        res+="|func.arctg|\"(\""+tochupro(expr.args[0],expr.func,True)+"|\")\"|"
    elif(str(expr.func) in ('Arcctg', 'arcctg', 'Actg', 'actg')):
        res+="|func.arcctg|\"(\""+tochupro(expr.args[0],expr.func,True)+"|\")\"|"
    else:
        print ("No type",expr.func)
        print (expr)
        res+="/*"+str(expr.func)+"*/"
    return res

def replsym(sym):
    fparam =  open("paramsol.txt","r", encoding = "cp1251")
    base = {}
    for i in fparam:
        key = i.split()[0]
        key = key.replace("{","")
        key = key.replace("}","")
        key = key.replace("\\","")
        base[key] = i.split()[1]
    sym = str(sym)
    sym = sym.replace('sympy','')
    for i in base.keys():
        if sym == latinizator(i):
            return '|'+base[i]+'|'
    else:
        print("Ошибка символа в базе "+sym)
        return "/*"+sym+"*/"
def predobr(inp):
    expr = inp.replace('\\','')
    expr = expr.replace('{','')
    expr = expr.replace('}','')
    expr = expr.replace('[','(')#такие скобки парсер не поддерживает
    expr = expr.replace(']',')')
    expr = expr.replace("sqrt","Sqrt")
    expr = expr.replace('^','**')
    #lambda is keyword in sympy
    #and expr with lambda is not parse
    #i can`t fix it now
    expr = expr.replace('lambda','lambdasympy')
    #it`s replace not only lamba ofc
    #expr = expr.replace('S','Ssympy')
    #'S' is also keyword
    expr = latinizator(expr) #избавимся от кирилицы
    return expr

def exprtosol(inp):
    ret = str()
    expr = predobr(inp)
    for i in expr.split('='):
        try:
            sympyexpr = parse_expr(i, evaluate=False,global_dict=delglobal())
        except sympy.parsing.sympy_tokenize.TokenError:
            print('sympy.parsing.sympy_tokenize.TokenError\nдля '+i)
            return str()
        except SyntaxError:
            print('SyntaxError\nдля '+i)
            return str()
        except IndexError:
            print('IndexError\nдля '+i)
            return str()
        except AttributeError:
            print('AttributeError\nдля '+i+'\nДумаю, что ошибка в sympy.\nПопробую разобрать с evaluate=True. Там нет этой ошибки, кажется')
            try:
                sympyexpr = parse_expr(i, evaluate=True,global_dict=delglobal())
            except sympy.parsing.sympy_tokenize.TokenError:
                print('sympy.parsing.sympy_tokenize.TokenError\nдля '+i)
                return str()
            except SyntaxError:
                print('SyntaxError\nдля '+i)
                return str()
        ret+=tochupro(sympyexpr)+'|\"=\"|'
    ret = ret[:-5]#последнее равно
    while ret.find("||") != -1:
        ret = ret.replace("||","|")
    ret = ret.replace("\"|\"","")
    while ret.find("++")!=-1 or ret.find("--")!=-1 or ret.find("+-")!=-1 or ret.find("-+")!=-1:
        ret = ret.replace("++","+")
        ret = ret.replace("--","+")
        ret = ret.replace("+-","-")
        ret = ret.replace("-+","-")
    ret = ret.replace('_frac_|\"2\"|_frac',"_frac2")
    #разберемся с одиночными кавычками
    kav = ret.split("\"")
    ret = str()
    for i in range(0,len(kav)-1,2):
        ret+=kav[i]
        if(len(kav[i+1])==1):
            ret+='\''+kav[i+1]+'\''
        else:
            ret+='"'+kav[i+1]+'"'
    ret+=kav[-1]
    return ret


def replsymans(sym):
    fparam =  open("param.txt","r", encoding = "cp1251")
    base = {}
    for i in fparam:
        key = i.split()[0]
        key = key.replace("{","")
        key = key.replace("}","")
        key = key.replace("\\","")
        base[key] = i.split()[1]
    sym = str(sym)
    sym = sym.replace('sympy','')
    for i in base.keys():
        if sym == latinizator(i):
            return base[i]
    else:
        print("Ошибка символа в базе "+sym)
        return "/*"+sym+"*/"
def signexpr(expr):
    if(expr.is_real):
        if(expr < 0):
            return False #-
        else:
            return True
    elif(expr.is_Mul):
        for i in expr.args:
            if(i.is_real and i<0):
                return False
        else:
            return True
    else:
        return True
def findminus(expr):
    if(expr.is_real):
        if(expr < 0):
            return True
        else:
            return False
    if(expr.is_Add):
        for i in expr.args:
            if(not signexpr(i)):
                return True
        else:
            return False
    elif(expr.is_Pow and expr.args[1] == -1):
        return findminus(expr.args[0])
    else:
        return False
def mulminone(expr):
    if(expr.is_Add):
        return simplify(-expr)
    elif(expr.is_Pow and expr.args[1] == -1):
        return Pow(simplify(-expr.args[0]),-1)
    else:
        return simplify(-expr)
def toans(expr,prevfunc = None, **keywords):
    #recursive
    res = str()
    if(expr.is_Rational):
        return str(expr)
    elif(expr.is_Integer):
        return str(expr)
    elif(expr.is_Symbol):
        return replsymans(expr)
    elif(expr.is_Add):
        sk = False
        if(prevfunc!=None):
            if(prevfunc.is_Mul):
                sk = True
            if(prevfunc.is_Pow):
                if 'func' in keywords and keywords['func']:
                    sk = False
                else:
                    sk = True
        if sk:
            res+="("
        addarg = list(expr.args)
        for i in range(0,len(addarg)):
            if(addarg[i].is_Mul):
                fmo = False
                for j in addarg[i].args:
                    if(j.is_real and j<0):
                        fmo = True
                if(fmo == False):
                    addarg[0],addarg[i]=addarg[i],addarg[0]
                    break
            elif(not (addarg[i].is_real and addarg[i]<0)):
                addarg[0],addarg[i]=addarg[i],addarg[0]
                break

        for i in addarg:
            res+=toans(i,expr.func)+"+"
        res = res[:-1]
        if sk:
            res+=")"
    elif(expr.is_Mul):
        #а вот тут еще с делением нужно разобраться
        div = False
        sqrt = False
        nom = Integer(1)
        denom = Integer(1)
        sqrtnom = Integer(1)
        sqrtdenom = Integer(1)
        sk = ('denom' in keywords and keywords['denom'])
        if(sk):
            res+="("
        mularg = list(expr.args)
        find = False
        if(not signexpr(expr)):

            if(mularg[0].is_real and mularg[0]<0):

                for i in range(1, len(mularg)):
                    if(findminus(mularg[i])):
                        mularg[i] = mulminone(mularg[i])
                        mularg[0] = mulminone(mularg[0])
                        break

        for i in mularg:

            if(i.func.is_Pow and(i.args[1].is_real and i.args[1] < 0)):
                if(i.args[1] == -1 and str(i.args[0].func)=='Sqrt'):
                    sqrt=True
                    sqrtdenom = Mul(sqrtdenom,i.args[0].args[0])
                else:
                    denom = Mul(denom,Pow(i.args[0],i.args[1].__abs__()))
                    div = True
            elif(str(i.func) == 'Sqrt'):
                sqrt = True
                sqrtnom=Mul(sqrtnom,i.args[0])
            elif(i.is_Rational):
                if(i.q>1):
                    div = True
                nom = Mul(nom,i.p)
                denom = Mul(denom,i.q)
            else:
                nom=Mul(nom,i)
        if(sqrt == False):
            if(div == False):
                #тогда умножение
                for i in expr.args:
                    res+=toans(i,expr.func, denom=False)+"*"
                res = res[:-1]
            else:
                res+=toans(nom,expr.func, denom=False)+"/"+toans(denom,expr.func,denom=True)
        else:
            if(sqrtdenom == 1 and nom == 1):
                res+=toans(Function('Sqrt')(sqrtnom))+"/"+toans(denom,expr.func,denom=True)
            else:
                if(nom/denom != 1):
                    res+=toans(nom/denom,expr.func)+"*"
                res+=toans(Function('Sqrt')(sqrtnom/sqrtdenom))
        if(sk):
            res+=")"
    elif(expr.is_Pow):
        if(expr.args[1] == 1/2):
            return "matreal.sqrt("+toans(expr.args[0],expr.func,func=True)+")"
        elif(expr.args[1] == 1/3):
            return "matreal.curt("+toans(expr.args[0],expr.func,func=True)+")"
        elif(expr.args[1] == 2):
            sk = ('denom' in keywords and keywords['denom'])
            if(sk):
                res+="("
            res+=toans(expr.args[0],expr.func)+"*"+toans(expr.args[0],expr.func)
            if(sk):
                res+=")"
        elif(expr.args[1] == -1):
            return "1/"+toans(expr.args[0],expr.func)
        elif(expr.args[1] == 3):
            sk = ('denom' in keywords and keywords['denom'])
            if(sk):
                res+="("
            res+=toans(expr.args[0],expr.func)+"*"+toans(expr.args[0],expr.func)+"*"+toans(expr.args[0],expr.func)
            if(sk):
                res+=")"
        else:
            return "matreal.pow("+toans(expr.args[0],expr.func,func=True)+","+toans(expr.args[1],expr.func,func=True)+")"
    elif(str(expr.func) == 'Sqrt'):
        return "matreal.sqrt("+toans(expr.args[0],expr.func,func=True)+")"
    elif(str(expr.func) == 'Sin' or str(expr.func) == 'sin'):
        return "matreal.sin("+toans(expr.args[0],expr.func,func=True)+")"
    elif(str(expr.func) == 'Cos' or str(expr.func) == 'cos'):
        return "matreal.cos("+toans(expr.args[0],expr.func,func=True)+")"

    elif(str(expr.func) in ('Arcsin', 'arcsin', 'Asin', 'asin')):
        return "matreal.asin("+toans(expr.args[0],expr.func,func=True)+")"
    elif(str(expr.func) in ('Arccos', 'arccos', 'Acos', 'acos')):
        return "matreal.acos("+toans(expr.args[0],expr.func,func=True)+")"

    elif(str(expr.func) in ('Tg', 'tg', 'Tan', 'tan')):
        return "matreal.tan("+toans(expr.args[0],expr.func,func=True)+")"
    elif(str(expr.func) == 'Ctg' or str(expr.func) == 'ctg'):
        return "matreal.ctg("+toans(expr.args[0],expr.func,func=True)+")"

    elif(str(expr.func) in ('Arctg', 'arctg', 'Atan', 'atan')):
        return "matreal.atan("+toans(expr.args[0],expr.func,func=True)+")"
    elif(str(expr.func) in ('Arcctg', 'arcctg', 'Actg', 'actg')):
        return "matreal.actg("+toans(expr.args[0],expr.func,func=True)+")"

    else:
        print ("No type",expr.func)
        print(expr)
    return res

def delglobal():
    global_dict = {}
    exec_('from sympy import *', global_dict)
    del global_dict['S']
    del global_dict['C']
    del global_dict['O']
    del global_dict['I']
    del global_dict['N']
    del global_dict['E']
    del global_dict['Q']
    del global_dict['pi']
    del global_dict['beta']
    #del global_dict['Lambda']

    return global_dict


def exprtoans(inp):
    ret = str()
    expr = predobr(inp)

    try:
        sympyexpr = parse_expr(expr,global_dict=delglobal())
    except sympy.parsing.sympy_tokenize.TokenError:
        print('sympy.parsing.sympy_tokenize.TokenError\nдля '+expr)
        return str()
    except SyntaxError:
        print('SyntaxError\nдля '+expr)
        return str()
    sympyexpr = simplify(sympyexpr)
    ret = toans(sympyexpr)
    while ret.find("++")!=-1 or ret.find("--")!=-1 or ret.find("+-")!=-1 or ret.find("-+")!=-1:
        ret = ret.replace("++","+")
        ret = ret.replace("--","+")
        ret = ret.replace("+-","-")
        ret = ret.replace("-+","-")
    ret = ret.replace("-1*","-")
    return ret
