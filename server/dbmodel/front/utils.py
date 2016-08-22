#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from dbmodel import models

def isPropInProps(cprops):
    arr = []
    for cprop in cprops:
        d = models.Props.objects.filter(propid=cprop)
        if d == None or len(d) <= 0:
            msg = cprop+" is not find."
            # print msg
            arr.append(msg)
        else:
            pname = d[0].name
            if pname == u'待定战姬':
                msg = cprop+" is 待定战姬."
                # print msg
                arr.append(msg)
    return arr


