import torch
import torch.nn as nn

torch.manual_seed(42)                      # 固定随机种子：每次跑结果一样（可复现）
model = nn.Linear(3, 1)                    # 权重表格：3 进 1 出的最小模型
optimizer = torch.optim.SGD(model.parameters(), lr=1e10)  # 学习率故意爆炸：正常应是 0.01
loss_fn = nn.MSELoss()                     # 损失函数：衡量"预测和答案差多远"

for step in range(100):
    x = torch.randn(8, 3)                  # 一批 8 个样本，每个 3 个数
    y = torch.randn(8, 1)                  # 对应的正确答案

    optimizer.zero_grad()                  # 清掉上一轮的旧梯度
    loss = loss_fn(model(x), y)            # 前向：模型加工 → 和答案比差距

    # 条件断点：只有出事才停（这就是"条件 breakpoint"模式）
    if torch.isnan(loss) or loss.item() > 1e8:
        print(f"\n[!] step {step}: loss={loss.item()}")
        for name, p in model.named_parameters():
            if p.grad is not None:
                print(f"    grad {name}: nan={torch.isnan(p.grad).any().item()}")
        breakpoint()                       # ← 掉进调试器，下面是验尸时间

    loss.backward()                        # 反向：算出每个权重该怎么调（梯度）
    optimizer.step()                       # 调旋钮（lr=1e10 → 每次拧过头一万倍）
    print(f"step {step:3d}  loss={loss.item():.4f}")
