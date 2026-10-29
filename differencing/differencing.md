## What Is Differencing?

Differencing transforms a time series by computing the change between consecutive observations. It removes trends and makes non-stationary data stationary.

$$
\nabla y_t = y_t - y_{t-1}
$$

The first difference at time $t$ is the current value minus the previous value.

---

## The Formula

For a time series $y_1, y_2, ..., y_T$:

$$
\nabla y_t = y_t - y_{t-1}
$$

**Result:** New series with $T-1$ values.

**Lag-d differencing:**

$$
\nabla_d y_t = y_t - y_{t-d}
$$

**Common:** $d=1$ for non-seasonal, $d=12$ for monthly data with yearly seasonality.

---

## Worked Example

**Original series:** [100, 103, 108, 112, 109, 115, 120]

**First differences:**

- $\nabla y_2 = 103 - 100 = 3$
- $\nabla y_3 = 108 - 103 = 5$
- $\nabla y_4 = 112 - 108 = 4$
- $\nabla y_5 = 109 - 112 = -3$
- $\nabla y_6 = 115 - 109 = 6$
- $\nabla y_7 = 120 - 115 = 5$

**Result:** [3, 5, 4, -3, 6, 5]

**Interpretation:** Changes from period to period. Positive values indicate increases, negative indicate decreases.

---

## Why Difference?

**Stationarity requirement:**

Most time series models (ARIMA, VAR) require stationary data.

**Non-stationary indicators:**

- Strong trend
- Mean changes over time
- Autocorrelation decays slowly

**Differencing solution:**

Removes deterministic trends and random walks. Converts non-stationary to stationary.

---

## Order of Differencing

**First-order differencing ($d=1$):**

$$
\nabla y_t = y_t - y_{t-1}
$$

Removes linear trends.

**Second-order differencing ($d=2$):**

$$
\nabla^2 y_t = \nabla(\nabla y_t) = (y_t - y_{t-1}) - (y_{t-1} - y_{t-2}) = y_t - 2y_{t-1} + y_{t-2}
$$

Removes quadratic trends.

**Higher orders rare:** Most real data needs at most second-order differencing.

**Over-differencing:** Can introduce spurious autocorrelation. Use minimum necessary order.

---

## Second Difference Example

**Original:** [10, 12, 16, 22, 30, 40]

**First differences:** [2, 4, 6, 8, 10]

Still trending upward (acceleration).

**Second differences:**

- $(4-2) = 2$
- $(6-4) = 2$
- $(8-6) = 2$
- $(10-8) = 2$

**Result:** [2, 2, 2, 2]

Now stationary (constant).

**Original had quadratic trend:** $y_t \approx t^2$

---

## Seasonal Differencing

For seasonal period $s$:

$$
\nabla_s y_t = y_t - y_{t-s}
$$

**Monthly data ($s=12$):**

Compare each month to same month last year.

**Example:** January 2024 minus January 2023.

**Result:** Removes yearly seasonal pattern.

---

## Combined Differencing

For data with both trend and seasonality:

**Step 1:** Seasonal differencing:

$$
z_t = y_t - y_{t-s}
$$

**Step 2:** First differencing:

$$
w_t = z_t - z_{t-1}
$$

**Combined form:**

$$
w_t = (y_t - y_{t-s}) - (y_{t-1} - y_{t-s-1})
$$

**ARIMA notation:** $(p, d, q)(P, D, Q)_s$

$d$: non-seasonal differences

$D$: seasonal differences

---

## Unit Root and Integration

**Unit root process:**

$$
y_t = y_{t-1} + \epsilon_t
$$

Random walk. Non-stationary.

**First difference:**

$$
\nabla y_t = y_t - y_{t-1} = \epsilon_t
$$

White noise. Stationary.

**Integration order:** If $d$ differences needed for stationarity, series is $I(d)$ (integrated of order $d$).

**Example:** $I(1)$ means first difference is stationary.

---

## Testing for Stationarity

**Augmented Dickey-Fuller (ADF) test:**

Tests null hypothesis of unit root (non-stationary).

**Procedure:**

1. Run ADF test on original series
2. If non-stationary (fail to reject null), apply differencing
3. Test differenced series
4. Repeat until stationary

**KPSS test:**

Null hypothesis is stationarity (opposite of ADF).

**Use both:** Confirm stationarity from multiple angles.

---

## Information Loss

**Differencing removes level information:**

Cannot recover original values without initial condition.

**Example:** Given differences [2, 3, -1, 4] and $y_1 = 10$:

- $y_2 = 10 + 2 = 12$
- $y_3 = 12 + 3 = 15$
- $y_4 = 15 - 1 = 14$
- $y_5 = 14 + 4 = 18$

Without $y_1$, cannot reconstruct series.

**Forecasting:** When forecasting differenced series, integrate back to get level forecasts.

---

## Fractional Differencing

For long-memory processes:

$$
\nabla^d y_t = \sum_{k=0}^{\infty} \binom{d}{k} (-1)^k y_{t-k}
$$

where $d$ can be non-integer (e.g., $d=0.5$).

**Use case:** Removes non-stationarity while preserving long-range dependence.

**Application:** Financial data with long memory.

---

## Differencing vs Detrending

**Differencing:**

$$
\nabla y_t = y_t - y_{t-1}
$$

Non-parametric. Removes stochastic trends.

**Linear detrending:**

$$
\tilde{y}_t = y_t - (\hat{\beta}_0 + \hat{\beta}_1 t)
$$

Parametric. Removes deterministic trends.

**When to use which:**

- Random walk: Use differencing
- Deterministic trend: Use detrending
- Uncertain: Differencing is safer (more general)

---

## Invertibility

**Forward operation (differencing):**

$$
\nabla y_t = y_t - y_{t-1}
$$

**Inverse operation (integration/cumulative sum):**

$$
y_t = y_1 + \sum_{i=2}^{t} \nabla y_i
$$

**Important for forecasting:** Model differenced series, then integrate forecasts to original scale.

---

## Impact on Autocorrelation

**Before differencing:**

Non-stationary series: ACF decays slowly.

**After differencing:**

Stationary series: ACF decays quickly or is zero.

**Example:** Random walk has $\rho_k \approx 1$ for all $k$. After differencing, $\rho_k \approx 0$ for all $k > 0$.

**Over-differencing:** Creates negative autocorrelation at lag 1.

---

## Differencing in ARIMA Models

**ARIMA(p, d, q):**

- $p$: AR order
- $d$: differencing order
- $q$: MA order

**Modeling process:**

1. Difference $d$ times to achieve stationarity
2. Fit ARMA($p$, $q$) to differenced series
3. Integrate forecasts back to original scale

**Common models:**

- ARIMA(0,1,0): Random walk
- ARIMA(0,1,1): Exponential smoothing
- ARIMA(1,1,0): Differenced AR(1)

---

## Logarithmic Differencing

**Log transformation then difference:**

$$
\nabla \ln y_t = \ln y_t - \ln y_{t-1} = \ln\left(\frac{y_t}{y_{t-1}}\right)
$$

**Interpretation:** Approximately equals percentage change.

**Advantage:** Stabilizes variance for series with exponential growth.

**Example:** Stock prices. Log differences are returns.

---

## Multivariate Differencing

For vector time series $\mathbf{y}_t = [y_{1,t}, y_{2,t}, ..., y_{n,t}]^T$:

$$
\nabla \mathbf{y}_t = \mathbf{y}_t - \mathbf{y}_{t-1}
$$

**Each series differenced element-wise.**

**Cointegration consideration:** If series are cointegrated, differencing destroys long-run relationship. Use error correction model instead.

---

## Practical Differencing Steps

**Step 1:** Plot series and ACF.

**Step 2:** If non-stationary, apply first difference.

**Step 3:** Plot differenced series and ACF.

**Step 4:** Check if stationary:

- ACF decays quickly
- Mean is constant
- Variance is constant

**Step 5:** If still non-stationary, apply second difference.

**Step 6:** Never go beyond second difference in practice.

---

## Forecast Integration

**Differenced model forecast:**

$$
\hat{\nabla y}_{T+h}
$$

**Convert to level forecast:**

$$
\hat{y}_{T+h} = \hat{y}_{T+h-1} + \hat{\nabla y}_{T+h}
$$

**Bootstrap from last observed value:**

$$
\hat{y}_{T+1} = y_T + \hat{\nabla y}_{T+1}
$$

$$
\hat{y}_{T+2} = \hat{y}_{T+1} + \hat{\nabla y}_{T+2}
$$

---

## Differencing and Variance

**Original series variance:** $\text{Var}(y_t) = \sigma_y^2$

**First difference variance:**

$$
\text{Var}(\nabla y_t) = \text{Var}(y_t - y_{t-1}) = 2\sigma_y^2(1 - \rho_1)
$$

**For random walk ($\rho_1 = 1$):**

$$
\text{Var}(\nabla y_t) = 0
$$

Series becomes constant (perfect prediction).

**For white noise ($\rho_1 = 0$):**

$$
\text{Var}(\nabla y_t) = 2\sigma_y^2
$$

Variance increases.

---

## Business Cycle Removal

**Hodrick-Prescott filter:**

Alternative to differencing for removing trends while preserving cycles.

$$
\min_{\tau} \sum_{t=1}^{T} (y_t - \tau_t)^2 + \lambda \sum_{t=2}^{T-1} [(\tau_{t+1} - \tau_t) - (\tau_t - \tau_{t-1})]^2
$$

**Differencing is simpler but less flexible.**

**HP filter allows tuning smoothness via $\lambda$.**

---

## Mean Reversion After Differencing

**Non-stationary series:** May not revert to mean.

**Differenced series:** Should oscillate around zero.

**Check:** Mean of differenced series should be close to zero (or small constant).

**Drift term:** If differenced series has non-zero mean, original has linear trend:

$$
y_t = \beta_0 + \beta_1 t + \epsilon_t
$$

$$
E[\nabla y_t] = \beta_1
$$

---

## Spurious Regression

**Problem:** Regressing one non-stationary series on another yields significant results even if unrelated.

**Solution:** Difference both series before regression.

**Exception:** Cointegration. If series share common trend, regression in levels is valid.

**Test:** Check residuals for stationarity. If stationary, cointegration exists.