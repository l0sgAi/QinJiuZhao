N=4 #N次多项式
a=[4,3,2,1] #表示多项式各个位的系数，a[n]表示X^(N-n)的系数
s=0 #输出多项式的结果
x=4 #带入多项式中x的值
for i in range(N-1):
    if i==0:
        s=a[i]*x+a[i+1] #第一次运算，给最内侧的算式赋值
        print("第1次运算s的值为:")
        print(s)  
    else:
        s=s*x+a[i+1] #后续运算，与x进行累乘的同时累加相应常数项
        print("第"+str(i+1)+"次运算s的值为:")
        print(s) 
        
        
         




