import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
#---------------------------------------------------------------------------------------------
customer = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
#تعداد کل مشتری ها
#Total number of customers
all_customs_num = len(customer)
#دیتای مشتری هایی ک ریزش کردن
#data of curn customers
chorn_yes = customer[customer['Churn']== 'Yes']
chorn_no = customer[customer['Churn']== 'No']
#تعداد مشتری های ریزش کرده
#total number of churned customers
chorn_yes_num = len(chorn_yes)
chorn_no_num = len(chorn_no)
#درصد مشتری های ریزش کرده
#percentage of churned customers
chorn_percent = (int(chorn_yes_num)/int(all_customs_num))*100
chorn_no_percent = (int(chorn_no_num)/int(all_customs_num))*100
#هر روش پرداخت چ تعداد مشتری ریزشی داشته ؟
#How many customers did each payment method lose?
payment_churn_num = chorn_yes['PaymentMethod'].value_counts()
#هر روش پرداخت چ درصدی از کل مشتری ها مشتری زیرشی داشتن؟
#What percentage of all customers for each payment method had churn?
payment_churn_percentage = (payment_churn_num) / (all_customs_num) *100
#هر جنسیت چ تعداد مشتری ریزشی داشته ؟
#How many customers did each gender lose?
gender_churn_num = chorn_yes['gender'].value_counts()
#هر جنسیت چ درصدی از کل مشتری ها مشتری ریزشی داشته ؟
#What percentage of all customers of each gender have lost customers?
gender_churn_percentage = (gender_churn_num) / (all_customs_num) *100
#هر نوع قرارداد چ تعداد مشتری ریزشی داشته ؟
#How many customers did each contract lose?
contract_churn_num = chorn_yes['Contract'].value_counts()
#هر نوع قرارداد چ درصدی از کل مشتری ها مشتری ریزشی داشته؟
#What percentage of all customers of each contract have lost customers?
contract_churn_percentage = (contract_churn_num) / (all_customs_num) *100
#مدت اشتراک مشتری های ریزشی بین چ ماه و چ ماهی بوده و بیشتر چ ماهی بوده؟-----
#The subscription period of the dropout customers was between what month and what month,and what month was it the most?-----
#قدیمی‌ترین مشتری‌ای که ریزش کرده، چند ماه عضو بوده
#How many months was the oldest customer who churned a member?
max_chorn_yes_tenure = chorn_yes['tenure'].max()
max_chorn_no_tenure = chorn_no['tenure'].max()
#سریع‌ترین ریزش بعد از چند ماه اتفاق افتاده
#After how many months did the fastest churn occur?
min_chorn_yes_tenure = chorn_yes['tenure'].min()
#در هر ماه چند نفر ریزش کردن؟
#How many people churned each month?
churn_by_month = chorn_yes['tenure'].value_counts().sort_index()
churn_no_by_month = chorn_no['tenure'].value_counts().sort_index()
#کدوم ماه بیشترین تعداد مشتری ریزشی رو داشته؟
#which month had the most number of churned customers?
churn_by_month_max= churn_by_month.idxmax()
#تو کدوم روش پرداخت بیشتر دارم مشتری از دست میدم ؟
#in which payment method i'm losing the most customers?
payment_count = customer['PaymentMethod'].value_counts()
payment_churn_rate = (payment_churn_num / payment_count) * 100


#visualizations------------------
fig, ax = plt.subplots()
df_chorn_by_month = churn_by_month.reset_index()
df_no_chorn_by_month = churn_no_by_month.reset_index()
df_chorn_by_month.columns = ['tenure','count']

# churned customers by tenure
plt.plot(df_chorn_by_month['tenure'], df_chorn_by_month['count'])
ax.set_xlabel(
    'tenure',
    fontsize=12,
    color='darkblue',
    fontweight='bold')
ax.set_ylabel(
    'count of churned customers',
    fontsize=12,
    color='darkred',
    fontweight='bold')
ax.set_title('count of churned customers by tenure',fontsize=14,fontweight='bold')
ax.set_facecolor('lightgray')
ax.tick_params(colors='darkgreen',labelsize=10)


#Customers establishment
plt.plot(df_no_chorn_by_month['tenure'], df_no_chorn_by_month['count'])
ax.set_xlabel(
    'tenure',
    fontsize=12,
    color='darkblue',
    fontweight='bold')
ax.set_ylabel(
    'count of Stable customers',
    fontsize=12,
    color='darkred',
    fontweight='bold')
ax.set_title('Customers establishment',fontsize=14,fontweight='bold')
ax.set_facecolor('lightgray')
ax.tick_params(colors='darkgreen',labelsize=10)


#Customers churn by contract
contract_churn_rate = contract_churn_num.sort_values(ascending=False)
plt.bar(contract_churn_rate.index ,contract_churn_rate.values,
        color= ['#E0BBE4','#D291BC','#FEC8D8'], edgecolor='black' , linewidth=1.2)
plt.grid(axis='y', linestyle='--', alpha=0.6)
ax.set_title('Customers churn by contract',fontsize=14,fontweight='bold')
ax.set_xlabel(
    'contract',
    fontsize=12,
    color='darkblue',
    fontweight='bold')
ax.set_ylabel(
    'count of churned customers',
    fontsize=12,
    color='darkred',
    fontweight='bold')
for i, v in enumerate(contract_churn_num.values):
    percent = (v / chorn_yes_num) * 100
    plt.text(i, v + 20, f'{percent:.1f}%', ha='center')


#Customers churn by payment methode
payment_churn_rate= payment_churn_num.sort_values(ascending = False)
plt.bar(payment_churn_rate.index ,payment_churn_rate.values,
        color= ['#FBFFD4','#D8C9FF','#C7E9FF','#D6FFC7'], edgecolor='black' , linewidth=1.2)
plt.grid(axis='y', linestyle='--', alpha=0.6)
ax.set_title('Customers churn by payment methode',fontsize=14,fontweight='bold')
ax.set_xlabel(
    'payment methode',
    fontsize=12,
    color='darkblue',
    fontweight='bold')
ax.set_ylabel(
    'count of churned customers',
    fontsize=12,
    color='darkred',
    fontweight='bold')
plt.xticks(fontsize = 6, fontweight='bold')    
plt.yticks(fontweight='bold')
for i, v in enumerate(payment_churn_num.values):
    percent = (v / chorn_yes_num) * 100
    plt.text(i, v + 20, f'{percent:.1f}%', ha='center')


#count of churned customers VS stable customers
plt.plot(churn_by_month.index, churn_by_month.values, label='churned')
plt.plot(churn_no_by_month.index,churn_no_by_month.values, label='stable')
ax.set_xlabel(
    'tenure',
    fontsize=12,
    color='darkblue',
    fontweight='bold')
ax.set_ylabel(
    'count of customers',
    fontsize=12,
    color='darkred',
    fontweight='bold')
ax.set_title('count of churned customers VS stable customers',fontsize=14,fontweight='bold')
ax.set_facecolor('lightgray')
ax.tick_params(colors='darkgreen',labelsize=10)
plt.legend()


#Distribution of customer churn by tenure
sns.violinplot(data = chorn_yes, x='Churn',y='tenure',
        palette='Set2',cut=0,width=0.7)
ax.set_title('Distribution of customer churn by tenure',fontsize=14,fontweight='bold')
ax.set_xlabel(
    'churn',
    fontsize=12,
    color='darkblue',
    fontweight='bold')
ax.set_ylabel(
    'tenure',
    fontsize=12,
    color='darkred',
    fontweight='bold')
ax.set_facecolor('lightgray')
ax.tick_params(colors='darkgreen',labelsize=10)
plt.show()
