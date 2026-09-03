# Phase 0 · Lesson 11 Linux for AI — 查漏记录

## chmod 实操
- touch 三文件 → ls -la 读权限位 → chmod +x（rw-→rwx）/644/755 数字模式验证
- 数字模式：三位=所有者/组/其他人，每位=读4+写2+执行1

## 磁盘双查
- df -h：WSL vhdx 稀疏文件（1007G 显示容量 vs 实占 13G）
- du -sh ~/.cache 排序发现 uv 缓存 6.7G → uv cache clean 释放 6.4GiB（74773 文件），venv 不受影响（numpy/datasets/sklearn 复验完好）
- huggingface 缓存 212M（09 课遗产，保留）

## systemd 初见
- WSL 内 running 服务：cron/dbus/journald 等 7 个系统守护
- 概念：应用服务将来 systemctl start/enable 挂进去（Phase 17 部署用）

## 教材未覆盖已会的（实操史抵扣）
- 文件导航/apt 装包/htop/tmux/grep find/df du——10 课与日常使用已覆盖

## 教训
- 终端无输入法纠错：linunx/0la 两次手滑，&& 链和回车前检查是防御
