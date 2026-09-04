# Phase 1 · Lesson 1 Linear Algebra Intuition — 直觉笔记

## 空间三部曲（几何直觉）
- 向量 = 空间箭头：[3,2] 有方向有长度（√13）；784 维 = 描述用 784 个数字，MNIST 一图一点
- 矩阵 = 变换机器：rot90 把 [3,1] 变 [-1,3]（实测）；2×3 = 吃 3 维吐 2 维；NN 层 = 矩阵乘法
- 点积 = 相似度体温计：逐维投票，>0 相似 / =0 垂直 / <0 相反；cos = 去长度只比方向

## RAG 串场
- 入库/提问（embedding 矩阵搬运）→ 检索（点积排序）→ 作答（top-k 喂给 LLM）

## 下半场四概念
- 线性无关：v3=2v1+v2 即复读机，z 轴盲区；特征冗余 = 多重共线性
- 秩：真实自由度；rank([[1,2],[2,4]])=1 实测；满秩/秩亏/秩1/病态四档
- 投影：影子即降维，[3,4]→x轴=[3,0]，残差⊥b 实测
- Gram-Schmidt：撕影子+归一化；两两点积全0、模长全1 实测；= QR 的内心戏
- LoRA：ΔW≈B×A 低秩赌注，4096²≈16.7M → 131K 参数（省99%）

## 动手（全部实测通过）
- 手写 Vector 类：__init__/dot/magnitude/normalize/cosine_similarity
- 验收：dot=32、|a|=3.7417、cos=0.9746、|a|²=a·a=14、垂直点积=0、normalize 后模长 1
- 变形实验：a·a 与 |a|² 相等（|a|=√(a·a)）；[1,1]⊥[1,-1] 点积 0；cosine 量程 [-1,1]
- 课程脚本 vectors.py 全段跑通（含 angle_between、独立性判定、秩示例、NN 层演示）
- torch autodiff：d(a·b)/da = b 本身，backward() 自动串梯度链

## 踩坑实录（均为手敲自曝，报错阅读实战）
1. outputs/phase1/01/ 目录未建 → nano 保存报 Error writing；mkdir -p 先行
2. Tab/空格混用 → TabError；nano Ctrl+\ 全局替换 Tab→4 空格，后转 VS Code（Convert Indentation to Spaces）
3. onther/cosine_similaryity 拼错 → VS Code Pylance 波浪线提示
4. a.cosine_similarity 忘括号调用 → round 收到方法对象，TypeError；方法名不带括号=体温计本身，带括号=读数
5. cosine 少除 other.magnitude() → cos=8.5524 超量程 [-1,1]；"不可能的数字"即线索
6. 变形实验忘 print → 结果被丢弃；int 分量导致输出 0 而非 0.0（等价）

## 环境
- VS Code WSL 模式接通（绿色 WSL: Ubuntu 标记），venv 解释器自动选中，断点调试功能就位
