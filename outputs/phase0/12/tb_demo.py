import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("outputs/phase0/12/runs/demo")
model = nn.Linear(3, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

for step in range(200):
    x, y = torch.randn(32, 3), torch.randn(32, 1)
    optimizer.zero_grad()
    loss = loss_fn(model(x), y)
    loss.backward()
    optimizer.step()
    writer.add_scalar("loss/train", loss.item(), step)      # 每步记一个点
    if step % 20 == 0:                                       # 每 20 步存一次权重快照
        for name, p in model.named_parameters():
            writer.add_histogram(f"weights/{name}", p, step)

writer.close()
print("demo done, 200 steps logged")
