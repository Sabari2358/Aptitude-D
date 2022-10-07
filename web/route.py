from web import app
from flask import render_template, redirect, url_for
from web.inputs import Inputs, pandcInputs
from web.PyDMath import div,combination,permutation,fact

@app.route('/')
def home_page():
    return render_template('home.html')

#  Divisor and Divisor results
@app.route('/resultc',defaults={'res':'Something went wrong'})
@app.route('/resultc/<string:res>')
def result_pagec(res):
    return render_template('resultc.html',result=res)

@app.route('/resultw',defaults={'res':'Something went wrong'})
@app.route('/resultw/<string:res>')
def result_pagew(res):
    return render_template('resultw.html',result=res)

@app.route('/divisor',methods=['GET', 'POST'])
def divisor_page():
    details = Inputs()
    if details.validate_on_submit():
        cap = details.number.data
        if cap > 1:
            obj1 = div(cap)
            print(str(cap))
            obj = str(cap) + " " + obj1
            return redirect(url_for('result_pagec',res=obj))
        else:
            return redirect(url_for('result_pagew',res='Number must be greater than 1'))
    return render_template('divisor.html',form=details,head="Find Divisor")


# Permutation and combination
@app.route('/pandc')
def pandc_page():
    return render_template('pandc.html')
# Results
@app.route('/combresultc',defaults={'res':'Something went wrong'})
@app.route('/combresultc/<string:res>')
def combresult_pagec(res):
    return render_template('/results/combresultc.html',result=res)

@app.route('/combresultw',defaults={'res':'Something went wrong'})
@app.route('/combresultw/<string:res>')
def combresult_pagew(res):
    return render_template('/results/combresultw.html',result=res)
# Combination
@app.route('/combination',methods=['GET', 'POST'])
def comb_page():
    datas = pandcInputs()
    if datas.validate_on_submit():
        n=datas.numbern.data
        r=datas.numberr.data
        if n >=1 and r >=1:
            obj1 = combination()
            obj = obj1.comb(n,r)
            return redirect(url_for('combresult_pagec',res=obj))
        else:
            return redirect(url_for('combresult_pagew',res='Positive values only allowed'))
    return render_template('combination.html',form=datas,head="Find Combination")
# Permutation
@app.route('/permutation',methods=['GET', 'POST'])
def per_page():
    datas = pandcInputs()
    if datas.validate_on_submit():
        n=datas.numbern.data
        r=datas.numberr.data
        if n >=1 and r >=1:
            obj1 = permutation()
            obj = obj1.per(n,r)
            return redirect(url_for('combresult_pagec',res=obj))
        else:
            return redirect(url_for('combresult_pagew',res='Positive values only allowed'))
    return render_template('combination.html',form=datas,head="Find Permutation")
# Factorial
@app.route('/factorial',methods=['GET', 'POST'])
def fact_page():
    datas = Inputs()
    if datas.validate_on_submit():
        n = datas.number.data
        if n > 1:
            obj = fact(n)
            return redirect(url_for('combresult_pagec',res=obj))
        else:
            return redirect(url_for('combresult_pagew',res='Positive values only'))
    return render_template('divisor.html',form=datas,head="Find Factorial")