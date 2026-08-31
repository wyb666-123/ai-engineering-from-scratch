# Phase 0 · Lesson 09 Data Management — 实验记录

## 环境适配（本课关键）
- huggingface.co 直连不通（curl 000），配置 HF_ENDPOINT=https://hf-mirror.com（已写入 ~/.bashrc）
- 镜像偶发抖动：datasets 自带 5 次重试，偶见 timeout→retry→成功，属正常噪音

## 实测数据
- 缓存验证：IMDB 首次下载 66s → 二次加载秒出（无进度条）
- 流式维基（20231101.en，教材的 20220301 已下架）：stream ready 64.9s，前 5 条 Anarchism/Albedo/A/Alabama/Achilles，未下载全量
- 格式对比（rotten_tomatoes 500 行样本）：CSV 59,539 / JSON 68,473 / Parquet 41,350 字节（小样本压缩率 1.4x，大数据集会拉大）
- 可复现切分：mrpc train 3668 行，70/15/15 → 2566/551/551，seed=42 两次完全一致
- HF 缓存现状：24 文件 / 128.4 MB（~/.cache/huggingface/）

## 踩坑记录
1. .bashrc 改完对已开会话不生效，需 export 或新开终端
2. `load_dataset("glue")` 在 datasets 5.x 报 HfUriError：新 URI 强制 namespace/name 双段，正确写法 nyu-mll/glue（教材老写法已过时）
3. 教材的 wikipedia 20220301 配置已下架，换 20231101.en
