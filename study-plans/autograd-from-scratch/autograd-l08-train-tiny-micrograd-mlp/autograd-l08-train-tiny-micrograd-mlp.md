# <span style="font-size: 20px;">Train a Tiny Micrograd MLP</span>

<span style="font-size: 14px;">Training a tiny multi-layer perceptron repeats the complete learning cycle several times. Every step evaluates the current network, derives all layer gradients manually, updates every parameter together, and records the loss that existed before the update.</span>

---

## <span style="font-size: 16px;">The batched forward pass</span>

<span style="font-size: 14px;">Let $H_0$ be the input batch. Each layer applies an affine transformation followed by tanh:</span>

$$
H_l=\tanh\left(H_{l-1}W_l^{\mathsf T}+b_l\right)
$$

<span style="font-size: 14px;">Rows are batch examples, and the final layer's only column contains their scalar predictions.</span>

---

## <span style="font-size: 16px;">Summed squared-error loss</span>

<span style="font-size: 14px;">If $p_i$ is the only final activation for example $i$, the training loss is:</span>

$$
L=\sum_{i=1}^{B}(p_i-y_i)^2
$$

<span style="font-size: 14px;">The loss is recorded before parameters change at each step.</span>

---

## <span style="font-size: 16px;">Starting the reverse pass</span>

<span style="font-size: 14px;">The derivative of the loss with respect to the final activation is:</span>

$$
G_L=2(H_L-y)
$$

<span style="font-size: 14px;">The target vector is treated as a batch-by-one column so it aligns with the final activation. This gradient begins at the network output and moves backward one layer at a time.</span>

---

## <span style="font-size: 16px;">Backpropagating through one layer</span>

<span style="font-size: 14px;">The saved activation supplies the tanh derivative:</span>

$$
D_l=G_l\odot(1-H_l^2)
$$

<span style="font-size: 14px;">The weight gradient combines every example's preactivation gradient with the preceding activation:</span>

$$
\frac{\partial L}{\partial W_l}=D_l^{\mathsf T}H_{l-1}
$$

<span style="font-size: 14px;">Summing over batch rows gives one bias gradient per output neuron:</span>

$$
\frac{\partial L}{\partial b_l}=\sum_{i=1}^{B}D_{l,i}
$$

<span style="font-size: 14px;">The gradient passed to the preceding activation is:</span>

$$
G_{l-1}=D_lW_l
$$

<span style="font-size: 14px;">Repeating these equations from the final layer to the first produces gradients with the same shapes as every supplied weight matrix and bias vector.</span>

---

## <span style="font-size: 16px;">All gradients precede every update</span>

<span style="font-size: 14px;">Backpropagation for one step must use one consistent parameter state. Every layer gradient is computed before any weight or bias is changed.</span>

$$
W_l'=W_l-\eta\frac{\partial L}{\partial W_l}
$$

$$
b_l'=b_l-\eta\frac{\partial L}{\partial b_l}
$$

<span style="font-size: 14px;">Simultaneous updates preserve the meaning of the derived gradients. Changing a later layer before computing an earlier gradient would make the reverse pass combine parameters from different model states.</span>

---

## <span style="font-size: 16px;">Fresh gradients on every step</span>

<span style="font-size: 14px;">Each training step starts with new gradient tensors. Gradients from an earlier step describe an earlier parameter state and must not be added to the current derivatives.</span>

<span style="font-size: 14px;">This mirrors zeroing gradients in a conventional training loop. Here, the gradients are derived manually, so creating fresh layer-gradient containers makes the reset explicit and prevents stale accumulation.</span>

---

## <span style="font-size: 16px;">Loss history and final evaluation</span>

<span style="font-size: 14px;">For each requested step, the history receives the current loss before the parameter update. After the final update, one additional forward pass produces predictions and loss aligned with the returned trained parameters.</span>

<span style="font-size: 14px;">The final loss is not necessarily the last history entry. The last history entry belongs to the model before the final update, while the final loss belongs to the model after it.</span>

<span style="font-size: 14px;">When the requested step count is zero, the history is empty and the final evaluation uses the supplied parameters unchanged.</span>

---

## <span style="font-size: 16px;">A one-step scalar example</span>

<span style="font-size: 14px;">Consider one input of $1$, one target of $1$, and a single tanh layer whose weight and bias both begin at zero. The initial prediction is zero and the pre-update loss is one.</span>

<span style="font-size: 14px;">The output gradient and tanh derivative give a preactivation gradient of $-2$. Both the weight and bias gradients are therefore $-2$. With learning rate $0.1$, both parameters become $0.2$.</span>

<span style="font-size: 14px;">The final preactivation is $0.4$, the final prediction is approximately $0.379949$, and the final loss is approximately $0.384463$. The history contains only the pre-update loss of one.</span>

---

## <span style="font-size: 16px;">Dtype, device, and input preservation</span>

<span style="font-size: 14px;">Inputs, targets, weights, and biases share one floating-point dtype and device. Working parameters preserve both while the supplied tensors remain unchanged.</span>

---

## <span style="font-size: 16px;">Pitfalls</span>

* <span style="font-size: 14px;">**Skipping tanh at the final layer.** Every layer in this model applies the activation.</span>
* <span style="font-size: 14px;">**Updating before all gradients are known.** One step's gradients must come from one consistent parameter state.</span>
* <span style="font-size: 14px;">**Reusing gradient tensors across steps.** Each iteration requires fresh derivatives.</span>
* <span style="font-size: 14px;">**Recording post-update loss in the history.** History entries are explicitly pre-update losses.</span>
* <span style="font-size: 14px;">**Returning the final history entry as final loss.** A separate forward pass is required after the last update.</span>
* <span style="font-size: 14px;">**Changing supplied parameters.** Training occurs on cloned working tensors.</span>

<span style="font-size: 14px;">Tiny-MLP training combines all earlier ideas into one loop: layer composition, saved activations, reverse-mode gradients, fresh accumulation, simultaneous descent updates, and a final evaluation of the trained model.</span>

---