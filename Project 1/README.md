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

## NFHS-4 attributes for diabetes risk - needs evaluation 

### CASEID

1. CASEID : Case identification

2. V002 : Household number 

### Respondent's attributes

3. V012 : Respondent's current age 

4. V013 : Age in 5-years groups
          
          1 : 15-19
          2 : 20-24
          3 : 25-29
          4 : 30-34
          5 : 35-39
          6 : 40-44
          7 : 45:49
          na : Not applicable 

5. V020 : Ever married sample

          0 : All woman sample
          1 : Ever married sample 

6. V024 : State

7. V025 : Type of place of residence 

          1 : urban 
          2 : Rural

8. V026 : NA - De facto place of residence

          0 : Capital, large city
          1 : Small city
          2 : Town
          3 : Countryside 
          9 : missing 

9. MV002 : Household number 

10. MV012 : Current age 

11. MV015 : Age in 5-years groups
          
          1 : 15-19
          2 : 20-24
          3 : 25-29
          4 : 30-34
          5 : 35-39
          6 : 40-44
          7 : 45:49
          na : Not applicable

12. MV024 : State 

13. MV025 : Type of place of residence 

14. MV026 : NA - De facto place of residence

          0 : Capital, large city
          1 : Small city
          2 : Town
          3 : Countryside 
          9 : missing 

15. MV034A : NA - Wife or partner

          1 : Wife
          2 : Partner
          9 : missing 

16. MV034B : Age of wife / partner  

17. V101 : State

18. V102 : Type of place of residence 

          1 : urban 
          2 : Rural

19. V103 : NA- Childhood place of residence (required for migration - genetic or environmental)

          0 : Capital, large city
          1 : Small city
          2 : Town
          3 : Countryside 
          9 : missing 

20. V104 : Years lived in place of residence

21. V105 : NA - Type of place of previous residence 

          0 : Capital, large city
          1 : Small city
          2 : Town
          3 : Countryside 
          9 : missing

22. V106 : Highest educational level

          0 : No education 
          1 : Primary
          2 : Secondary
          3 : Higher 
          9 : Missing 

23. V123 : Household has bicycle (need for physical activity)

          0 : No
          1 : Yes
          7 : Not a de jure resident
          9 : Missing 

24. V124 : Household has motorcycle/scooter (need for physical activity)

          0 : No
          1 : Yes
          7 : Not a de jure resident
          9 : Missing 

25. V123 : Household has car/truck (need for physical activity)

          0 : No
          1 : Yes
          7 : Not a de jure resident
          9 : Missing 

26. V130 : Religion 

          1 : Hindu
          2 : Muslim 
          3 : Christian 
          4 : Sikh
          5 : Buddhist/Neo-Buddhist
          6 : Jain 
          7 : Jewish
          8 : Parsi/Zoroastrian 
          9 : No religion
          96 : other 

27. V131 : Caste or tribe 

          991 : Caste
          992 : Tribe
          993 : No caste / Tribe
          999 : Missing

28. V134 : De facto place of residence 

          0 : Capital, large city
          1 : Small city
          2 : Town
          3 : Countryside 
          9 : missing

30. V135 : Usual resident or visitor

          1 : Usual resident
          2 : Visitor
          9 : Missing 

31. V139 : De jure region of residence 

32. V140 : De jure type of place of residence 

          0 : Abroad
          1 : Urban
          2 : Rural
          7 : Not a de jure resident 
          9 : Missing 

33. V141 : NA - De jure place of residence 

          0 : capital, large city
          1 : City 
          2 : Town
          3 : Countryside
          4 : Abroad
          5 : Not a de jure resident 
          9 : Missing 

34. V149 : Educational attainment 

35. V150 : Relationship to household head

36. V166 : NA - Result of salt test for iodine 

37. V190 : Wealth index
          
          1 : Poorest
          2 : Poorer
          3 : Middle
          4 : Richer
          5 : Richest

38. V191 : Wealth index factor score 

39. MV101 : Region (state)

40. MV102 : Type of place of residence

          1 : Urban
          2 : Rural

41. MV130 : Religion 

42. MV131 : Ethnicity 

43. V213 : Currently Pregnant

          0 : No or unsure 
          1 : Yes

44. MV463A : Smokes Cigarettes (take care whether for woman or man)

          0 : No 
          1 : Yes
          9 : Missing 
          na : Not applicable 

45. MV463B : Smokes pipe

46. MV463C : Uses chewing tobacco 

47. MV463D : Uses snuff

48. MV463E : Smokes Cigars

49. MV463F : Gutka/Paan masala with tobacco

50. MV463G : Paan with tobacco 

51. MV463X : Smokes other(See SM609C and SM609E)

52. MV463Z : Smokes nothing 

53. MV463 : Number of cigarettes in last 24 hours 

54. V437 : Respondent's weight in kilograms (has lot of data on this but unnecessary for me)

55. V438 : Respondent's height in cms

56. V445 : BMI 

57. V446 : Rohrer' index 

58. V447 : Result of measurement - height/weight 

### Take care - data of women

59. V447A : Women's age in years 

60. V454 : Currently pregnant

61. V463A : Smokes cigarettes

62. V463B : Smokes pipe

63. V463C : Uses chewing tobacco 

64. V463D : Uses snuff

65. V463E : Smokes cigar

66. V463F : Gutka/Paan Masala with tobacco 

67. V463G : Paan with tobacco

68. V463X : Smokes other (see S710C and S710E)

69. V463Z : does not use tobacco 

70. V464 : Number of cigarettes in last 25 hours 

71. V472A to V472U

72. V701 : Husband/partner's education level

73. V702 : Husband/partner's highest year of education 

74. V703 : Husband/partner's occupation 

75. V716 : Respondent's occupation 

76. SDISTRI : District 

77. SSLUM0 : Slum designation by observation 

          0 : Non-Slum
          1 : Slum

78. S116 : Belong to a SC/ST 

          1 : SC
          2 : ST 
          3 : OBC
          4 : None of them
          5 : Don't know 

79. S707 : currently smoke bidis

          0 : No
          1 : Yes
          na : Not applicable 

80. S708 : Bidis smoked in last 24 hours

81. S710C : Type of tobacco used : Hookah

82. S710E : Tpe of tobacco used : Khaini

83. S715 : Somone smoked in respondent's home or presence

84. S716 : Drinks alcohol 

          0 : No
          1 : Yes

85. S717 : Frequency drinks alcohol

          1 : Almost every day
          2 : about once a week
          3 : Less than once a week 

86. S718A : Type of alcohol usually consumed : Tadi Madi

87. S718B : Type of alcohol usually consumed : Country liquor

88. S718C : Type of alcohol usually consumed : Beer 

89. S718D : Type of alcohol usually consumed : wine 

90. S718E : Type of alcohol usually consumed : hard liquor 

91. S718X : Type of alcohol usually consumed : other

92. S723A : Currently has diabetes

93. S723AB : Has sought treatment for diabetes

94. S723C : Currently has thyroid disorder 

95. S723CB : Has sought treatment for thyroid disorder

96. S723D : Currently has heart disease

97. S723DB : Has sought treatment for heart disease

98. S723E : Currently has cancer

99. S723EB : Has sought treatment for cancer

100. S726A : Frequency takes milk or curd

          0 : Never
          1 : Daily
          2 : Weekly
          3 : Occasionally 
          4 : Not applicable 

101. S726B : Frequency takes pulses or beans

102. S726C : Frequency eats dark green leafy vegetable

103. S726D : Frequency eats fruit

104. S726E : Frequency eats eggs

105. S726F : Frequency eats fish

106. S726G : Frequency eats chichen or meat

107. S726H : Frequency eats fried food 

108. S726I : Frequency takes aerated drinks

109. SB12A : 30 minutes prior to BP measures : eaten 

          0 : No
          1 : yes
          9 : Missing 

110. SB12A : 30 minutes prior to BP measures : had coffee, tea

111. SB12C : SB12A : 30 minutes prior to BP measures : smoked any tobacco

112. SB12D : 30 minutes prior to BP measures : use any other 

113. SB16S : First Systolic reading

          0:299 : Systolic reading 
          994 : refused
          995 : Technical problem
          996 : Other
          999 : Missing 

114. SB16D : First Diastolic reading 

115. SB18 : Told had high BP on two or more ocassions by doctor 

116. SB19 : Currently taking a prescribed medicine to lower 

117. SB23S : Second Systolic reading

          0:299 : Systolic reading 
          994 : refused
          995 : Technical problem
          996 : Other
          999 : Missing 

118. SB23D : Second Diastolic reading

119. SB27S : Third Systolic reading

          0:299 : Systolic reading 
          994 : refused
          995 : Technical problem
          996 : Other
          999 : Missing 

118. SB27D : Third Diastolic reading

119. SB70 : Glucose level

120. S190S : Wealth index within state

          1 : Poorest
          2 : Poorer
          3 : Middle
          4 : Richer
          5 : Richest

121. S190U : Wealth index - urban 

122. S191U : Wealth index factor score

123. S190US  : Wealth index - urban within state

124. S190R : Wealth index - rural

125. S191R : Wealth index factor score - rural

126. S190RS : Wealth index - rural within state

127. SMDISTRI : District 

128. 




## NFHS-3 attributes for diabetes risk

Calender (VCAL) codes - contains information on aspects of the respondent's immediate history

1. VCAL(1): 
                    
          Births, pregnancies and contraceptive use :
                    
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
                    
          HV024 :
          
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

6. Ownership of bovine - milk / Dairy  - for dietary pattern 
                    
          SH62A : Has cows/bulls/buffalo
          SH62B : Has camels
          SH62C : Has horses/donkeys/mules
          SH62D : Has goats
          SH62E : Has sheep 
          SH62F : Has chickens  

### Women

7. Geograhical location - migration factor / native state - genetic vs environment factor 
                    
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

Above attributes will be selected initially & PCA will be performed to reduce attributes.

