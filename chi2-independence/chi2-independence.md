## What Is the Chi-Square Test for Independence?

The Chi-Square test for independence determines whether there is a **statistically significant association** between two categorical variables.

**Null hypothesis ($H_0$):** The two variables are independent (no association).

**Alternative hypothesis ($H_1$):** The two variables are not independent (there is an association).

If the test rejects $H_0$, we conclude the variables are related.

---

## When to Use This Test

Use the Chi-Square test for independence when:

- You have two categorical (nominal or ordinal) variables
- You want to test if they are related
- Observations are independent
- Expected frequencies are sufficiently large (typically $\geq 5$)

**Examples:**
- Is gender associated with voting preference?
- Is education level related to employment status?
- Is treatment type associated with patient outcome?

---

## The Contingency Table

Data is organized in a **contingency table** (cross-tabulation):

For two variables with $r$ rows and $c$ columns:

- $O_{ij}$ = observed count in cell $(i, j)$
- Row totals: $R_i = \sum_{j=1}^{c} O_{ij}$
- Column totals: $C_j = \sum_{i=1}^{r} O_{ij}$
- Grand total: $N = \sum_{i}\sum_{j} O_{ij}$

---

## Expected Frequencies Under Independence

If the variables are independent, the expected count in each cell is:

$$
E_{ij} = \frac{R_i \times C_j}{N}
$$

This formula comes from the definition of independence:

$$
P(\text{row } i \text{ and column } j) = P(\text{row } i) \times P(\text{column } j)
$$

$$
E_{ij} = N \times \frac{R_i}{N} \times \frac{C_j}{N} = \frac{R_i \times C_j}{N}
$$

---

## The Chi-Square Test Statistic

The test statistic measures how much observed counts deviate from expected:

$$
\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
$$

**Interpretation:**
- Each cell contributes $(O - E)^2 / E$ to the statistic
- Large deviations increase $\chi^2$
- Under $H_0$, $\chi^2$ follows a chi-square distribution

---

## Degrees of Freedom

The degrees of freedom for the test:

$$
df = (r - 1)(c - 1)
$$

where $r$ = number of rows and $c$ = number of columns.

**Intuition:** We lose 1 degree of freedom for each row and column constraint (totals must match).

**Examples:**
- 2x2 table: $df = (2-1)(2-1) = 1$
- 3x4 table: $df = (3-1)(4-1) = 6$

---

## Step-by-Step Procedure

**Step 1:** Set up hypotheses
- $H_0$: Variables are independent
- $H_1$: Variables are not independent

**Step 2:** Choose significance level $\alpha$ (typically 0.05)

**Step 3:** Calculate expected frequencies $E_{ij}$

**Step 4:** Compute the test statistic $\chi^2$

**Step 5:** Find the critical value or p-value from $\chi^2_{df}$ distribution

**Step 6:** Make a decision
- If p-value $< \alpha$, reject $H_0$
- If $\chi^2 > \chi^2_{critical}$, reject $H_0$

---

## Worked Example

**Research question:** Is there an association between smoking status (smoker/non-smoker) and lung disease (yes/no)?

**Observed data:**

- Smokers with lung disease: 90
- Smokers without lung disease: 60
- Non-smokers with lung disease: 30
- Non-smokers without lung disease: 120

**Totals:**
- Smokers: $R_1 = 90 + 60 = 150$
- Non-smokers: $R_2 = 30 + 120 = 150$
- Lung disease: $C_1 = 90 + 30 = 120$
- No lung disease: $C_2 = 60 + 120 = 180$
- Grand total: $N = 300$

---

**Step 1: Compute expected frequencies**

$E_{11} = \frac{150 \times 120}{300} = \frac{18000}{300} = 60$

$E_{12} = \frac{150 \times 180}{300} = \frac{27000}{300} = 90$

$E_{21} = \frac{150 \times 120}{300} = \frac{18000}{300} = 60$

$E_{22} = \frac{150 \times 180}{300} = \frac{27000}{300} = 90$

---

**Step 2: Compute the test statistic**

$$
\chi^2 = \frac{(90-60)^2}{60} + \frac{(60-90)^2}{90} + \frac{(30-60)^2}{60} + \frac{(120-90)^2}{90}
$$

$$
= \frac{900}{60} + \frac{900}{90} + \frac{900}{60} + \frac{900}{90}
$$

$$
= 15 + 10 + 15 + 10 = 50
$$

**Step 3: Degrees of freedom**

$df = (2-1)(2-1) = 1$

**Step 4: P-value**

For $\chi^2 = 50$ with $df = 1$, p-value $< 0.0001$

**Conclusion:** Reject $H_0$. There is a significant association between smoking and lung disease.

---

## Critical Values

Common critical values for chi-square distribution:

**At $\alpha = 0.05$:**
- $df = 1$: $\chi^2_{crit} = 3.841$
- $df = 2$: $\chi^2_{crit} = 5.991$
- $df = 3$: $\chi^2_{crit} = 7.815$
- $df = 4$: $\chi^2_{crit} = 9.488$
- $df = 5$: $\chi^2_{crit} = 11.070$

If $\chi^2 > \chi^2_{crit}$, reject the null hypothesis.

---

## Assumptions and Requirements

**1. Independence of observations**

Each subject contributes to only one cell.

**2. Random sampling**

Data should be a random sample from the population.

**3. Expected frequency requirement**

All expected frequencies should be $\geq 5$ for the approximation to be valid.

If expected frequencies are too small, use Fisher's exact test (for 2x2) or combine categories.

---

## Effect Size: Cramér's V

The chi-square statistic depends on sample size. For effect size, use Cramér's V:

$$
V = \sqrt{\frac{\chi^2}{N \times (k - 1)}}
$$

where $k = \min(r, c)$ is the smaller of rows or columns.

**Interpretation:**
- $V \approx 0.1$: Small effect
- $V \approx 0.3$: Medium effect
- $V \approx 0.5$: Large effect

**Example:** With $\chi^2 = 50$, $N = 300$, $k = 2$:

$$
V = \sqrt{\frac{50}{300 \times 1}} = \sqrt{0.167} = 0.41
$$

This is a medium-to-large effect.

---

## For 2x2 Tables: Phi Coefficient

For 2x2 tables specifically, the phi coefficient ($\phi$) equals Cramér's V:

$$
\phi = \sqrt{\frac{\chi^2}{N}}
$$

Range: $-1$ to $1$ (but typically reported as absolute value)

---

## Yates' Continuity Correction

For 2x2 tables, Yates' correction adjusts for the discrete nature of counts:

$$
\chi^2_{Yates} = \sum \frac{(|O_{ij} - E_{ij}| - 0.5)^2}{E_{ij}}
$$

This gives a more conservative test (larger p-value). It is less commonly used today.

---

## One-Tailed vs Two-Tailed

The chi-square test for independence is inherently **two-tailed**.

It tests whether there is any association, not the direction of association.

To assess direction, examine:
- The pattern of observed vs expected counts
- Standardized residuals: $(O_{ij} - E_{ij})/\sqrt{E_{ij}}$

---

## Residual Analysis

**Standardized residuals** show which cells contribute most to the chi-square:

$$
r_{ij} = \frac{O_{ij} - E_{ij}}{\sqrt{E_{ij}}}
$$

**Adjusted standardized residuals** (more commonly used):

$$
d_{ij} = \frac{O_{ij} - E_{ij}}{\sqrt{E_{ij}(1 - R_i/N)(1 - C_j/N)}}
$$

If $|d_{ij}| > 2$, the cell contributes significantly to rejecting $H_0$.

---

## Chi-Square vs Other Tests

**Chi-Square test:**
- For categorical vs categorical
- Tests association
- Requires sufficient expected counts

**Fisher's exact test:**
- For 2x2 tables with small expected counts
- Exact p-values, no approximation

**G-test (likelihood ratio test):**
- Alternative to chi-square
- Uses $G = 2\sum O_{ij} \ln(O_{ij}/E_{ij})$
- Asymptotically equivalent

---

## Relationship to Other Chi-Square Tests

**Goodness-of-fit test:**
- One variable, compares observed to theoretical distribution
- $df = k - 1$ where $k$ = number of categories

**Test for independence:**
- Two variables, tests association
- $df = (r-1)(c-1)$

**Test for homogeneity:**
- Same formula as independence test
- Different sampling scheme (compare groups)

---

## Common Mistakes

**1. Using percentages instead of counts**

Always use raw counts, not percentages or proportions.

**2. Including the same subject multiple times**

Violates independence assumption.

**3. Ignoring small expected frequencies**

Can lead to invalid p-values.

**4. Confusing statistical and practical significance**

Large samples can make small effects significant.

---

## Applications in Machine Learning

**Feature selection:**
- Test if a categorical feature is associated with the target
- Features with significant association may be predictive

**Model evaluation:**
- Compare predicted vs actual categories
- Test if predictions are better than random

**A/B testing:**
- Test if conversion rates differ between variants

**Data exploration:**
- Discover relationships between categorical variables