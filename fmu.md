VARIABLES IN THE MODEL



<iframe src="https://basaga.org/basaga_files/ruffle/" width=550 height=550></iframe>

Only the variables essential for the purposes of the study participate in the model

Each variable has

unambiguously defined name

initial value (s), which may be:

 constant

 calculated from the initial values ​​of the other variables

a well-defined mathematical description

place (cells) in the EXCEL table

<br>

TYPES OF VARIABLES IN THE MODEL

Exogenous (External) variables

Disturbing effects, reflecting the actions of the external environment

Management influences, reflecting the decisions of the subject of management

Endogenous variables - determined on the basis of exogenous variables and other endogenous variables

internal (intermediate, calculated) variables

output variables (presented in a user-friendly form)

<br>EXTERNAL (EXOGENOUS) VARIABLES IN THE MODEL

 

External variables reflect the action of the external environment and external control influences.

Parameters. External parameters with constant value.

External variables changing over time.

Initial conditions. Depth of reported background .

Mathematical descriptions of external variables.

Programming of mathematical descriptions in the model.

List of assumptions (working hypotheses).

Scenario.

Simulation of the external environment through real data, simulation data or model.

<br>

MODEL PARAMETER (EXAMPLE)

 

"Increase in sales revenue " (Sales growth) is the parameter model (external variable having a constant value over time).

Its numerical value can be determined on the basis of:

- previous experience or statistics (ex post)

- on the basis of expected or forecast data (ex ante).

Changing the numerical value of a parameter will cause parametric changes in the model (respectively parametric experiments) with the structure preserved.

 

<br>

METHODS FOR SYNTHESIS OF MATHEMATICAL DESCRIPTIONS

 

Index method for synthesis of mathematical descriptions:

- Simple

- generates some new variables in the model

- implies previous experience or availability of statistical data.

 

Organic method for synthesis of mathematical descriptions: assumes a priori knowledge of the modeled system

Balance sheet equations and balancing variables.

 

Synthesis of mathematical descriptions based on observations on influencing and dependent variables (“black box” approach)

<br>MATHEMATICAL DESCRIPTION OF AN EXTERNAL VARIABLE (EXAMPLE)

"Sales revenue" is an external variable for the model (most common in financial models of business systems).

Sales revenue (T) = Sales revenue (T-1) * (1 + Increase in sales revenue)

Sales (T) = Sales (T-1) * (1 + Sales growth)

This is one of the possible (but not the only possible) mathematical description of the variable "Sales revenue", accepted as an assumption (working hypothesis) in the construction of the model.

Accepting another assumption for the mathematical description (another mathematical notation or dependence on other variables) will cause structural changes in the model (respectively structural experiments).

<br>PROGRAMMING OF MATHEMATICAL DESCRIPTIONS IN EXCEL (EXAMPLE)

 

A3: Increase in sales revenue / Parameter name 

B3: 10% / Numeric value of the parameter 

A16: Sales revenue / Variable name 

B16: 1000 / Initial value of the variable 

C16: = B16 * (1 + $ B $ 3) / Mathematical description in EXCEL 

<br>

LIST OF SELECTED ESSENTIAL VARIABLES IN THE MODEL

The corresponding names of the essential variables in the model and their initial values ​​are reflected in rows 14 to 40 of the EXCEL Table .

 

<table id="table1">
<tr>
<td></td>
<td>A</td>
<td>B</td>
</tr>
<tr>
<td>14</td>
<td>Year</td>
<td>0</td>
</tr>
<tr>
<td>15</td>
<td>Income statement</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>Sales revenue</td>
<td>1000</td>
</tr>
<tr>
<td>17</td>
<td>Cost of goods sold (Costs of goods sold)</td>
<td>-500</td>
</tr>
<tr>
<td>18</td>
<td>Interest payments on debt</td>
<td>-32</td>
</tr>
<tr>
<td>19</td>
<td>Interest income and C.K. (Interest earned on cash and marketable securities)</td>
<td>6</td>
</tr>
<tr>
<td>20</td>
<td>Depreciation</td>
<td>-100</td>
</tr>
<tr>
<td>21</td>
<td>Profit before tax</td>
<td>374</td>
</tr>
<tr>
<td>22</td>
<td>Taxes</td>
<td>-150</td>
</tr>
<tr>
<td>23</td>
<td>Profit after tax</td>
<td>225</td>
</tr>
<tr>
<td>24</td>
<td>Dividends paid</td>
<td>-90</td>
</tr>
<tr>
<td>25</td>
<td>Retained earnings</td>
<td>135</td>
</tr>
<tr>
<td>26</td>
<td></td>
<td></td>
</tr>
<tr>
<td>27</td>
<td>Balance sheet</td>
<td></td>
</tr>
<tr>
<td>28</td>
<td>Money and tradable C.K. (Cash and marketable securities)</td>
<td>80</td>
</tr>
<tr>
<td>29</td>
<td>Current assets</td>
<td>150</td>
</tr>
<tr>
<td>30</td>
<td>Fixed assets</td>
<td></td>
</tr>
<tr>
<td>31</td>
<td>At cost</td>
<td>1070</td>
</tr>
<tr>
<td>32</td>
<td>Accumulated Depreciation</td>
<td>-300</td>
</tr>
<tr>
<td>33</td>
<td>Net fixed assets</td>
<td>770</td>
</tr>
<tr>
<td>34</td>
<td>Total assets</td>
<td>1000</td>
</tr>
<tr>
<td>35</td>
<td></td>
<td></td>
</tr>
<tr>
<td>36</td>
<td>Current liabilities</td>
<td>80</td>
</tr>
<tr>
<td>37</td>
<td>Loans (Debt)</td>
<td>320</td>
</tr>
<tr>
<td>38</td>
<td>Share capital (Stock)</td>
<td>450</td>
</tr>
<tr>
<td>39</td>
<td>Accumulated retained earnings</td>
<td>150</td>
</tr>
<tr>
<td>40</td>
<td>Total liabilities and equity</td>
<td>1000</td>
</tr>
</table>

<br>ASSUMPTIONS REGARDING EXTERNAL VARIABLES:

 

The corresponding names of the model parameters and their numerical values ​​are reflected in rows 3 to 12 of the EXCEL Table .

Sales revenues will grow at a constant rate of 10% per year.

The value of short-term assets for a period is about 15% of sales revenue.

The value of short-term liabilities for one period is about 8% of sales revenue.

The value of net fixed assets for a period is about 77% of sales revenue.

The relative cost of sales is about 50% of sales revenue.

ASSUMPTIONS REGARDING EXTERNAL VARIABLES:

 

The corresponding names of the model parameters and their numerical values ​​are reflected in rows 3 to 12 of the EXCEL Table .

The depreciation rate is 10% of the average value of fixed assets during the previous and current years.

Fixed assets will include only net fixed assets plus the accumulated depreciation value.

Over the next five years, the company will not change the amount of its debt (it will not take new loans or repay existing ones).

ASSUMPTIONS REGARDING EXTERNAL VARIABLES:

 

The corresponding names of the model parameters and their numerical values ​​are reflected in rows 3 to 12 of the EXCEL Table .

The interest rate for existing loans is 10% and no changes are expected.

The company will not issue any securities for the next five years.

 The corporate income tax rate is 40% (flat tax) and no changes are expected.

ASSUMPTIONS REGARDING EXTERNAL VARIABLES:

 

The corresponding names of the model parameters and their numerical values ​​are reflected in rows 3 to 12 of the EXCEL Table .

 The company intends to pay dividends of 40% of the taxed profit.

 The rest of the taxed profit will be accumulated in "Accumulated retained earnings" for future use.

 The average yield on cash accounts and securities is 8%.

<div class="break"></div>

 "Money and marketable securities" will be used as a balancing variable to balance the Balance sheet.

The financial meaning of this choice reflects the chosen way of financing the company. It will not issue securities, will not repay its old debts and will not take on new debts. The necessary financing will be taken from "Money and marketable securities", and if the company has a free cash resource, it will be referred to the same account again. This also means that the mathematical description of the variable will be:

Money and marketable securities (T) = Total liabilities and equity (T) - Current assets (T) - Net value of fixed assets (T)

This ensures that assets and liabilities will always be equal.

A variant of the model with another balancing variable will be considered below.

<br>

<div class="break"></div>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

Sales revenue (T) = Sales revenue (T-1) * (1 + Increase in sales revenue)

Sales (T) = Sales (T-1) * (1 + Sa les growth)

Hypothesis: Sales revenues grow at a constant annual rate.

Other hypotheses considered: none.

Initial value in period T = 0: 1000

Parameter: Increase in sales revenue

Programming:

A3: Increase in sales revenue / Parameter name 

B3: 10% / Numeric value of the parameter 

A16: Sales revenue / Variable name 

B16: 1000 / Initial value of the variable 

C16: = B16 * (1 + $ B $ 3) / Mathematical description in EXCEL 

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

 

Cost of sales (T) = - Sales revenue (T) * Relative cost of sales

Hypothesis: The prime cost of the realized production in the period T is a proportional part of the sales revenues in the same period T and depends only on the sales revenues.

Other hypotheses considered: The prime cost also depends on some relatively fixed costs: general production, administrative or commercial. (Selling, general and administrative expenses SG&A).

Initial value in the period T = 0: -500

Parameter: Relative cost of sales

Programming:

A7: Relative cost of sales

B7: 50%

A17: Cost of sales

B17: - B16 * $ B $ 7

C17: -C1 6 * $ B $ 7

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

 

Interest payable (T) = - Interest rate on loans * Average amount of loans during the year (T)

Average amount of loans during the year (T) = (Loans (T-1) + Loans (T)) / 2

Hypothesis: In the next five years, the company will not change the amount of its debt (it will not take new loans or repay existing ones).

Other hypotheses considered: It is possible to change the amount of debt and its restructuring at changing interest rates.

Initial value in the period T = 0: -32

Parameter: Interest rate on loans

Programming:

A9: Interest rate on loans

B9: 10%

A18: Interest payable

B18: -32

C18: = - $ B $ 9 * (B37 + C37) / 2

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

 

Interest and securities income (T) = Yield on cash accounts and securities * Average amount of cash accounts and securities during the year (T)

Average amount of cash accounts and securities during the year (T) = (Money and marketable securities (T-1) + Money and marketable securities (T)) / 2

Hypothesis: The variable is assumed to be the equivalent interest rate on the financial income from available financial assets.

Other hypotheses considered: none.

Initial value in the period T = 0: 6

Parameter: Yield on cash accounts and securities.

Programming:

A10: Yield on cash accounts and securities

B10: 8%

A19: Interest and securities income

B19: 6

C 19: = $ B $ 10 * (B28 + C28) / 2

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

 

Depreciation (T) = - Depreciation rate * Average value of fixed assets during the year (T)

Average value of fixed assets during the year (T) = (Value of fixed assets (T-1) + Value of fixed assets (T)) / 2

Hypothesis: It is assumed that all new fixed assets are acquired during the year and there are no other disposals of fixed assets (eg sales, liquidations, scrapping, etc.).

Other hypotheses considered: none.

Initial value in the period T = 0: -100

Parameter: Depreciation rate

Programming:

A8: Depreciation rate

B8: 10%

A20: Depreciation

B20: -100

C20: - $ B $ 8 * (C31 + B31) / 2

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

 

Profit before taxes (T) = Sales revenue (T) - Cost of goods sold (T) - Interest payable (T) + Interest and securities income (T) - Depreciation (T)

Hypothesis: None. The mathematical description follows organically from economic theory.

Other hypotheses considered: None.

Initial value in the period T = 0: 374

Parameter: None.

Programming:

A21: Profit before taxes

B21: = SUM (B16: B20)

C21: = SUM (C16: C20)

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

 

Taxes (T) = Tax rate * Profit before taxes (T)

Hypothesis: A single tax rate is assumed for the profit tax, ie a "flat" tax, and there are no other explicitly reported taxes.

Other hypotheses considered: None.

Initial value in the period T = 0: -149

Parameter: Tax rate.

Programming:

A11: Tax rate

B11: 40%

A22: Taxes

B22: - $ B $ 11 * B21

C22: - $ B $ 11 * C21

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

 

Profit after taxes (T) = Profit before taxes (T) - Taxes (T)

Hypothesis: None.

Other hypotheses considered: None.

Initial value in the period T = 0: 225

Parameter: None.

Programming:

A23: Profit after tax

B23: B22 + B21

C23: C22 + C21

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

 

Dividends paid (T) = Dividend payout ratio * Profit after taxes (T)

Hypothesis: The dividend policy of the company is to pay dividends in an amount proportional to the taxed profit.

Other hypotheses considered: The company pays a fixed dividend per share or the company has a target value for dividend per share.

Initial value in the period T = 0: -90

Parameter: Dividend payment ratio.

Programming:

A12: Dividend payment ratio

B12: 40%

A24: Dividends paid

B24: = - $ B $ 12 * B23

C24: = - $ B $ 12 * C23

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(STATEMENT OF INCOME AND EXPENSES)

 

Retained earnings (T) = Profit after tax (T) - Dividends paid (T)

Hypothesis: Retained earnings will be accumulated in "Accumulated retained earnings" for future use.

Other hypotheses considered: None.

Initial value in the period T = 0: 135

Parameter: None.

Programming:

A25: Retained earnings

B25: = B23 + B24

C25: = C23 + C24

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 

Money and marketable securities (T) = Total liabilities and equity (T) - Current assets (T) - Net value of fixed assets (T)

Hypothesis: The variable is used as a balancing variable in the balance sheet. This ensures that assets and liabilities will always be equal.

The financial meaning of this choice reflects the chosen way of financing the company. It will not issue securities, will not repay its old debts and will not take on new debts. The necessary financing will be taken from "Money and marketable securities", and if the company has a free cash resource, it will be referred to the same account again.

Other hypotheses considered: A variant of the model with another balancing variable will be considered below.

Initial value in the period T = 0: 80

Parameter: None.

Programming:

A28: Money and marketable securities

B28: = B40-B29-B33

C28: = C40-C29-C33

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

Current assets (T) = Current assets to sales revenue * Sales revenue (T)

Hypothesis: The value of current assets at the end of the period is proportional to sales revenue for the same period.

Other hypotheses considered: None.

Initial value in the period T = 0: 150

Parameter: Current assets to sales revenue.

Programming:

A4: Current assets to sales revenue

B4: 15%

A29: Current assets

B29: = $ B $ 4 * B16

C29: = $ B $ 4 * C16

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 

Value of fixed assets (T) = Net value of fixed assets (T) - Accumulated depreciation (T)

Hypothesis: The model does not distinguish between different types of fixed assets (for example: land, buildings and structures, machinery and equipment, facilities, etc.).

Other hypotheses considered: None.

Initial value in the period T = 0: 1070

Parameter: None.

Programming:

A31: Value of fixed assets

B31: = B33-B32

C31: = C33-C32

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 

Accumulated depreciation (T) = Accumulated depreciation (T-1) + Depreciation rate * Average value of fixed assets (T)

Average value of fixed assets (T) = (Value of fixed assets (T-1) + Value of fixed assets (T)) / 2

Hypothesis: None.

Other hypotheses considered: None.

Initial value in the period T = 0: -300

Parameter: Depreciation rate

Programming:

A8: Depreciation rate

B8: 10%

A32: Accumulated depreciation

B32: -300

C32: = B32- $ B $ 8 * (B31 + C31) / 2

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 Net value of fixed assets (T) = Net fixed assets to sales revenue * Sales revenue (T)

Hypothesis: The value of net fixed assets at the end of the period is proportional to sales revenue for the same period.

Other hypotheses considered: The value of fixed assets is a stepwise function of sales revenue.

Initial value in the period T = 0: 847

Parameter: Net fixed assets to sales revenue.

Programming:

A6: Net fixed assets to sales revenue.

B6: 77%

A33: Net value of fixed assets

B33: = $ B $ 6 * B16

C33: = $ B $ 6 * C16

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 

Total assets (T) = Cash and marketable securities (T) + Current assets (T) + Net value of fixed assets (T)

Hypothesis: None.

Other hypotheses considered: None.

Initial value in the period T = 0: 1000

Parameter: None.

Programming:

A34: Total assets

B34: = B33 + B28 + B29

C34: = C33 + C28 + C29

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 

Short-term liabilities (T) = Short-term liabilities to sales revenues * Sales revenues (T)

Hypothesis: The value of short-term liabilities at the end of the period is proportional to sales revenue for the same period.

Other hypotheses considered: None.

Initial value in the period T = 0: 80

Parameter: Short-term liabilities to sales revenues.

Programming:

A5: Short-term liabilities to sales revenues.

B5: 8%

A36: Current liabilities

B36: = $ B $ 5 * B16

C36: = $ B $ 5 * C16

<br>MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 

Loans (T) = Loans (T-1)

Hypothesis: The size of the loans is assumed to be constant.

Other hypotheses considered: The amount of loans is considered as a balancing variable, ensuring the equalization of the Balance sheet.

Initial value in the period T = 0: 320

Parameter: None.

Programming:

A37: Loans

B37: 320

C37: = B37

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 

Share capital (T) = Share capital (T-1)

Hypothesis: The size of the share capital is assumed to be constant. The company does not issue any securities.

Other hypotheses considered: None.

Initial value in the period T = 0: 450

Parameter: None.

Programming:

A38: Share capital

B38: 450

C38: = B38

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 

Accumulated retained earnings (T) = Accumulated retained earnings (T-1) + Retained earnings (T)

Hypothesis: None.

Other hypotheses considered: None.

Initial value in the period T = 0: 150

Parameter: None.

Programming:

A39: Accumulated retained earnings

B39: 150

C39: B39 + C25

<br>

MATHEMATICAL DESCRIPTION OF THE EQUATIONS IN THE MODEL

(BALANCE SHEET)

 

Total liabilities and capital (T) = Short-term liabilities (T) + Loans (T) + Share capital (T) + Accumulated retained earnings (T)

Hypothesis: None.

Other hypotheses considered: None.

Initial value in the period T = 0: 1000

Parameter: None.

Programming:

A40: Total liabilities and equity

B40: = SUM (B36: B39)

C40: = SUM (C36: C39)
