def shippingC(p_orange):
    
    if p_orange > 100:
        cost = (p_orange * 0.32) + 6.00
        return cost
    else:
        cost = (p_orange * 0.32) + 7.50
        return cost
    

def weeklyPay(pay_r,work_hrs):
    if work_hrs > 40:
        pay= (40 * pay_r) + ((work_hrs-40) *(pay_r+ (pay_r*0.5)))
        return pay
    else:
        pay = work_hrs * pay_r
        return pay
                             