from web import app
from flask import render_template, redirect, url_for
from web.inputs import Inputs, pandcInputs, lcm_and_hcf, year_input,date_input
from web.PyDMath import div,combination,permutation,fact,lcm,hcf
from web import year
# from PyDMath import year

@app.route('/')
def home_page():
    return render_template('home.html')


# ======================================================================
#  Divisor and Divisor results
@app.route('/resultc',defaults={'res':'Something went wrong'})
@app.route('/resultc/<string:res>')
def result_pagec(res):
    return render_template('/results/overall_resultc.html',result=res,pat=url_for('divisor_page'))

@app.route('/resultw',defaults={'res':'Something went wrong'})
@app.route('/resultw/<string:res>')
def result_pagew(res):
    return render_template('/results/overall_resultw.html',result=res,pat=url_for('divisor_page'))

@app.route('/divisor',methods=['GET', 'POST'])
def divisor_page():
    details = Inputs()
    if details.validate_on_submit():
        cap = details.number.data
        if cap > 1:
            obj1 = div(cap)
            obj = str(cap) + " " + obj1
            return redirect(url_for('result_pagec',res=obj))
        else:
            return redirect(url_for('result_pagew',res='Number must be greater than 1'))
    return render_template('divisor.html',form=details,head="Find Divisor")


# ======================================================================
# Permutation and combination result
@app.route('/pandc')
def pandc_page():
    return render_template('pandc.html')
# Results
@app.route('/combresultc',defaults={'res':'Something went wrong'})
@app.route('/combresultc/<string:res>')
def combresult_pagec(res):
    return render_template('/results/overall_resultc.html',result=res,pat=url_for('pandc_page'))

@app.route('/combresultw',defaults={'res':'Something went wrong'})
@app.route('/combresultw/<string:res>')
def combresult_pagew(res):
    return render_template('/results/overall_resultw.html',result=res,pat=url_for('pandc_page'))

# ======================================================================
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

# ======================================================================
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

# ======================================================================
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


# ======================================================================
# LCM Results
@app.route('/r_lcmc',defaults={'res':'Something went wrong'})
@app.route('/r_lcmc/<string:res>')
def r_lcmc(res):
    return render_template('/results/overall_resultc.html',result=res,pat=url_for('lcm_and_hcf_page'))

@app.route('/r_lcmw',defaults={'res':'Something went wrong'})
@app.route('/r_lcmw/<string:res>')
def r_lcmw(res):
    return render_template('/results/overall_resultw.html',result=res,pat=url_for('lcm_and_hcf_page'))

# LCM and HCF
@app.route('/lcm_and_hcf',methods=['GET', 'POST'])
def lcm_and_hcf_page():
    datas = lcm_and_hcf()
    if datas.validate_on_submit():
        try:
            a = datas.values.data.split(' ')
        except:
            a = 'Unexcepted Error'
        if datas.submitL.data == True:
            result = lcm(a)
            if isinstance(result,int) or isinstance(result,float):
                return redirect(url_for('r_lcmc',res=result))
            else:
                return redirect(url_for('r_lcmw',res=result))
        elif datas.submitH.data == True:
            result = hcf(a)
            if isinstance(result,int) or isinstance(result,float):
                return redirect(url_for('r_lcmc',res=result))
            else:
                return redirect(url_for('r_lcmw',res=result))

    return render_template('lcmandhcf.html',form=datas,head="Find LCM and HCF",back=url_for('home_page'))

# ======================================================================
# Leap year and day finder page
@app.route('/time')
def time_page():
    return render_template('time.html')

@app.route('/year_result',defaults={'res':'Something went wrong'})
@app.route('/year_result/<string:res>')
def year_resultc(res):
    return render_template('results/lyear_exp_res.html',result=res,pat=url_for('year_page'))

# Leap year or not
@app.route('/findtheyear',methods=['GET', 'POST'])
def year_page():
    years = year_input()
    if years.validate_on_submit():
        a = years.year.data
        obj = year()
        result = obj.leap_year(str(a).split('-')[0])
        print(result)
        return redirect(url_for('year_resultc',res=result))
    else:
        print('Noooooo')
    return render_template('year.html',form=years,head='Leap year or not',back=url_for('time_page'))

# ======================================================================
# Find the day
@app.route('/day_resultc',defaults={'res':'Something went wrong'})
@app.route('/day_resultc/<string:res>')
def day_resultc(res):
    return render_template('results/overall_resultc.html',result=res,pat=url_for('day_page'))


# Not used ---------------------------------
@app.route('/day_resultw',defaults={'res':'Something went wrong'})
@app.route('/day_resultw/<string:res>')
def day_resultw(res):
    return render_template('results/overall_resultc.html',result=res,pat=url_for('day_page'))
# Not used ---------------------------------


@app.route('/findtheday',methods=['GET','POST'])
def day_page():
    form = date_input()
    if form.validate_on_submit():
        date = str(form.date.data)
        splited = date.split('-')
        obj = year()
        result = obj.find_day(splited[2],splited[1],splited[0])
        print(result)
        return redirect(url_for('day_resultc',res=result))

    return render_template('day.html',form=form,head='Find the date',back=url_for('time_page'))


# ======================================================================
