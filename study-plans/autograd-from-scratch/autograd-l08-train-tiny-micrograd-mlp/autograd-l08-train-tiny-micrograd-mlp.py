import torch

def forward(inputs, Ws, bs):
    acts = [inputs]
    H = inputs
    for W, b in zip(Ws, bs):
        H = torch.tanh(H @ W.T + b)
        acts.append(H)
    return acts

def backprop(acts, targets, Ws):
    n = len(Ws)
    dWs = [None] * n
    dbs = [None] * n
    G = 2 * (acts[-1] - targets.reshape(-1, 1))
    for l in reversed(range(n)):          # n-1, n-2, ..., 0
        D = G * (1 - acts[l + 1] ** 2)
        dWs[l] = D.T @ acts[l]
        dbs[l] = D.sum(dim=0)
        G = D @ Ws[l]
    return dWs, dbs    

def train_tiny_micrograd_mlp(inputs: torch.Tensor, targets: torch.Tensor, weights: list[torch.Tensor], biases: list[torch.Tensor], learning_rate: float, steps: int) -> tuple:
    """
    Returns final predictions, final loss, trained weights, trained biases, and pre-update loss history.
    """

    Ws = [w.clone() for w in weights]
    bs = [b.clone() for b in biases]
    history = []
    for step in range(steps):
        acts = forward(inputs,Ws,bs)
        preds = acts[-1][:, 0]
        loss = ((preds - targets) ** 2).sum()
        history.append(loss)
        dWs , dbs = backprop(acts , targets , Ws)
        for l in range(len(Ws)):
            Ws[l] = Ws[l] - learning_rate * dWs[l]
            bs[l] = bs[l] - learning_rate * dbs[l]
    acts = forward(inputs, Ws, bs)
    preds = acts[-1][:, 0]
    loss = ((preds - targets) ** 2).sum()
    return preds, loss, Ws, bs, history
    

    
