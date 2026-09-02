# Phase 0 · Lesson 10 Terminal & Shell — 实验记录

## tmux（练习 1）
- 会话 training：三窗格（htop / watch -n1 date / python 计数器）
- detach（Ctrl+B d）→ 关终端 → 重开 → attach 后 watch 仍在运行（时间戳持续更新）
- 踩坑：VS Code 拦截 Ctrl+B（弹"Ctrl+B 不是命令"），需在键盘快捷方式里解绑侧边栏切换；tmux 会话活于 WSL 虚拟机内存，wsl --shutdown 会清空（断线保险≠断电保险）

## 管道三连（练习 3）
- 造 100 行假训练日志 → grep "loss" | awk '{print $NF}' > losses.txt
- 验收：100 行 / 1.0000 / .0100（bc 吃前导零）

## 别名库（练习 2）
- shell_aliases.sh 已 source 进 .bashrc；tls / memhogs 验证可用
- memhogs 揭示：VS Code 扩展宿主 677M + Pylance 634M + Copilot 249M ≈ AI 编辑器税 1.5GB

## SSH config（练习 4）
- wsl-local 条目写入 ~/.ssh/config（语法练习，远程 GPU 机时照抄改参）

## 未实操（环境所限，概念已过）
- nvidia-smi / nvtop（无 GPU）、scp/rsync 远程（无远程机）——将来 Colab/云机时回头实操
