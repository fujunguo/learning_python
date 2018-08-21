a=float(input('请输入你的身高：'))#身高输入单位为m
b=float(input('请输入你的体重：'))#体重输入单位为kg
BMI=float(b/pow(a,2))
if BMI <18.5:
    print('你的体型为过轻，BMI值为%d'%(BMI))
elif 18.5<=BMI<25:
    print('你的体型为正常，BMI值为%d'%(BMI))
elif 25<=BMI<28:
    print('你的体型为过重，BMI值为%d'%(BMI))
elif 28<=BMI<32:
    print('你的体型为肥胖，BMI值为%d'%(BMI))
else:
    print('你的体型为严重肥胖，BMI值为%d'%(BMI))