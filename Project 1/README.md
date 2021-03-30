# Project 1

## NFHS Dataset 

1. [DHS - National Family Health Survey, 4 (2015-2016) - India](https://www.dhsprogram.com/data/dataset/India_Standard-DHS_2015.cfm?flag=0)
2. [DHS - National Family Health Survey, 3 (2005-2006) - India](https://www.dhsprogram.com/data/dataset/India_Standard-DHS_2006.cfm?flag=1)
3. [National Family Health Survey, 4 (2015-2016) - India](http://rchiips.org/NFHS/factsheet_NFHS-4.shtml) 
4. [National Family Health Survey, 3 (2005-2006) - India](http://rchiips.org/NFHS/factsheet.shtml)
5. Data for project has been taken from https://data.gov.in/
6. Link to the dataset: https://data.gov.in/catalog/key-indicators-national-family-health-survey-nfhs

## Assessment of risk of diabetes using spatial dietary intake profile from NFHS-4 and NFHS-3 dataset

This project explores two problems: discovering a set of attributes that predicts risk of diabetes and analysing the influence of socio-economic indicator on risk of diabetes. The NFHS-4 and NFHS-3 data will be used in machine learning techniques and other advanced data analytics approaches for analysis.

This project is a part of economics course HSP511 : Economics lab at [IIT Delhi](https://hss.iitd.ac.in/economics) under the guidance of [Prof. Sourabh B Paul](https://hss.iitd.ac.in/faculty/sourabh-b-paul)

## Attributes selection for prediction of diabetes 

Attributes used in Machine learning for diabetes prediction 
1. preganancies
2. glucose
3. Blood pressure 
4. Skin Thickness - NFHS not available 
5. Insulin - NFHS not available 
6. BMI 
7. DiabetesPedigreeFunction - based upon family history - (doubtful)
8. Age

### NHFS-3 attributes for diabetes risk

Calender (VCAL) codes - contains information on aspects of the respondent's immediate history

1. VCAL(1): Births, pregnancies and contraceptive use 
          B = Birth
          P = Pregnancies
          T = Terminated pregnancy / non-live birth
          0 = Non-use of contraception
          1 = Pill
          2 = IUD
          3 = Injections
          4 = Diaphragm
          5 = Condom
          6 = Female sterilization
          7 = Male sterilization
          8 = Periodic abstinence/rhythm 
          9 = Withdrawal
          W = other traditional methods
          N = Norplant/implants
          C = Female condom
          F = Foam or jelly
          ? = Missing

2. Standard of living index - below attributes for physical activity 
          HV210 = 1: Bicycle     Assigned SLI score : 2
          SH47W = 1: Tractor     Assigned SLI score : 4
          HV212 = 1: Car         Assigned SLI score : 4
          HV211 = 1: Motorcycle  Assigned SLI score : 3

3. State 
          HV024
          [AP] Andhra Pradesh           28
          [AS] Assam                    18
          [JH] Jharkhand                20  
          [BH] Bihar                    10
          [GO] Goa                      30
          [GJ] Gujarat                  24
          [HR] Haryana                  6
          [HP] Himachal Pradesh         2
          [JM] Jammu and Kashmir        1
          [KA] Karnataka                29
          [KE] Kerala                   32
          [CH] Chhattisgarh             22
          [MP] Madhya Pradesh           23
          [MH] Maharashtra              27
          [MN] Manipur                  14
          [MG] Meghalaya                17
          [MZ] Mizoram                  15
          [NA] Nagaland                 13
          [OR] Orissa                   21
          [PJ] Punjab                   3
          [RJ] Rajasthan                8
          [SK] Sikkim                   11
          [TN] Tamil Nadu               33
          [WB] West Bengal              19
          [UP] Uttar Pradesh            9
          [UC] Uttaranchal              5
          [DL] Delhi                    7
          [AR] Arunachal Pradesh        12
          [TR] Tripura                  16

### Household variables

4. Geographical location
          SH025 - City/Town/Countryside
          SHCITY - Selected cities 

5. Socio-Economic attributes - dietary pattern may vary 
          SH44 : Household head's religion
          SH45 : Caste or tribe of household head 
          SH46 : Type of caste or tribe of the household head 
          SH66 : Household has a BPL card
          SHSLI : standard of living index 

6. Ownership of bovine - milk giving - for dietary pattern 
          SH62A : Has cows/bulls/buffalo
          SH62B : Has camels
          SH62C : Has horses/donkeys/mules
          SH62D : Has goats
          SH62E : Has sheep 
          SH62F : Has chickens  

### Women

7. Geograhical location 
          S025 : City\Town\Countryside 
          SCITY : selected cities 

          V024 : State
          V101 : State 

          V139 : De jure state of residence 
          V150 : Relationship to household head 
                    1 = Head
                    2 = Wife
	          3 = Daughter
	          4 = Daughter-in-law
	          5 = Grandchild
	          6 = Parent
	          7 = Parent-in-law
	          8 = Sister
	          9 = Co-spouse
	          10 = Other relative
	          11 = Adopted/foster child
	          12 = Not related
	          13 = Niece by blood
	          14 = Niece by marriage
	          15 = Sister-in-law
	          16 = Niece
	          17 = Domestic servant
	          98 = DK



8. Socio-Economic attributes - dietary pattern may vary 
          S44 : Household head's religion
          S45 : Caste or tribe of household head 
          S46 : Type of caste or tribe of the household head 
          S66 : Household has a BPL card
          SSLI : standard of living index 

          SV122 : Educational level during 2005-06 school year

          V130 : Religion
                    1 = Hindu
	          2 = Muslim
	          3 = Christian
	          4 = Sikh
	          5 = Buddhist/Neo-Buddhist
	          6 = Jain
	          7 = Jewish
	          8 = Parsi/Zoroastrian
	          9 = No religion
	          10 = Donyi polo
	          96 = Other

          V704 : Partner's Occupation
          V716 : Respondent's occupation

9. Ownership of bovine - milk giving - for dietary pattern 
          S62A : Has cows/bulls/buffalo
          S62B : Has camels
          S62C : Has horses/donkeys/mules
          S62D : Has goats
          S62E : Has sheep 
          S62F : Has chickens  

10. Dietary pattern 
          S558A : Mother consumed: milk or curd
	S558B : Mother consumed: pulses or beans
	S558C : Mother consumed: dark green leafy veggies
	S558D : Mother consumed: fruits
	S558E : Mother consumed: eggs
	S558F : Mother consumed: fish
	S558G : Mother consumed: chicken or meat

11. Other disease - high correlation between diabetes and other disease
          S569  : Drinks alcohol
	S570  : Frequency of alcohol use
	S575A : Do you have: diabetes
          S575C : Do you have: goiter or other thyroid disorder

          V166 : Results of salt iodine test 

### MEN

12. Geograhical location 
          SM025 : City\Town\Countryside 
          SMCITY : selected cities 

          MV024 : State
          MV101 : State


13. Socio-Economic attributes - dietary pattern may vary 
          S44 : Household head's religion
          SM119 : Caste or tribe 
          SM120 : Type of caste or tribe  
          S66 : Household has a BPL card
          SMSLI : standard of living index 

          SMV122 : Educational level during 2005-06 school year

          MV130 : Religion
          MV150 : Relationship to household head 

          MV716 : Respondent's occupation 

14. Ownership of bovine - milk giving - for dietary pattern 
          S62A : Has cows/bulls/buffalo
          S62B : Has camels
          S62C : Has horses/donkeys/mules
          S62D : Has goats
          S62E : Has sheep 
          S62F : Has chickens  

15. Dietary pattern 
          SM601A : Man consumed: milk or curd
	SM601B : Man consumed: pulses or beans
	SM601C : Man consumed: dark green leafy veggies
	SM601D : Man consumed: fruits
	SM601E : Man consumed: eggs
	SM601F : Man consumed: fish
	SM601G : Man consumed: chicken or meat


16. Other disease - high correlation between diabetes and other disease
          SM612  : Drinks alcohol
	SM613  : Frequency of alcohol use
	SM618A : Do you have: diabetes
          SM618C : Do you have: goiter or other thyroid disorder

### Health 

17. Health factors & BMI
          MV042	Household selection for hemoglobin
	MV437	Respondent's weight (kilos-1d)
	MV438	Respondent's height (cms-1d)
	MV439	Ht/A Percentile (resp)
	MV440	Ht/A Standard deviations (resp)
	MV441	Ht/A Percent ref. median (resp)
	MV442	Wt/Ht Percent ref. median (DHS)
	MV443	Wt/Ht Percent ref. median (Fog)
	MV444	Wt/Ht Percent ref. median (WHO)
	MV444A	Wt/Ht Std deviations (resp) DHS
	MV445	Body mass index for respondent
	MV446	Rohrer's index for respondent - for leaness
 	MV447	Result of measurement of respondent
	MV447A	Man's age in years from household report

          HV234 :  Test salt for Iodine
	          0 = 0 PPM (No Iodine)
	          991 = Less than 15 PPM
	          992 = 15 PPM or more
                    994 = Salt not tested
	          995 = No salt in household


 
 ### Household 

18. Survey 
          HV101 : Relationship to head
	1 = Head
	2 = Wife or husband
	3 = Son/daughter
	4 = Son/daughter-in-law
	5 = Grandchild
	6 = Parent
	7 = Parent-in-law
	8 = Brother/sister
	9 = Co-spouse
	10 = Other relative
	11 = Adopted/foster child
	12 = Not related
	13 = Niece/nephew by blood
	14 = Niece/nephew by marriage
	15 = Brother-in-law/sister-in-law
	16 = Niece/nephew
	17 = Domestic servant
	98 = DK

