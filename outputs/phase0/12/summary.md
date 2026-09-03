# Phase 0 · Lesson 12 Debugging & Profiling — 实验记录

## debug_tools.py 全流程（10 段演示全绿）
- debug_print：min/max/mean 会被单个 NaN 污染，has_nan 是唯一诚实指标
- check_shapes：五层形状流水线 [4,784]→[4,256]→[4,64]→[4,10] 一目了然
- Timer：1000² 矩阵乘 0.02s vs 5000² 1.48s——O(n³) 的 75 倍代价
- logging：时间戳+分级+落盘，对比 print 的三大代差

## NaN 死亡三部曲（nan_hunt.py，lr=1e10 故意爆炸）
- step 0: loss=0.45, weight≈±0.5（健康起点）
- step 1: loss=1.49e20, weight≈±9e9（有限爆炸——lr 每步拧大一万亿倍）
- step 2-3: loss=inf（撞破 float32 天花板 3.4e38，静默溢出不报错）
- step 4: loss=nan, weight=[inf,inf,inf]（数学死亡）
- 死因链：权重溢出 → 前向输出溢出 → MSELoss 内 inf-inf 产出 NaN

## pdb 实操收获
- 条件断点（loss>1e8 才停）在异常时 100% 精准拦截，无误报
- grad=None 不是 bug：断点在 backward 之前，本轮梯度未算、上轮已清零
- pdb 属性名拼写错误当场报 AttributeError——调试器自带"体检"
- 提示符识别：$ 是 bash、(Pdb) 是调试器，命令体系完全不同

## 健康对照
- lr=0.01 同模型同数据：loss 平稳下降，全程无 [!] 触发（详见命令输出）

## 待做
- TensorBoard 演示（tb_demo.py）+ cProfile 实操（练习 2）
