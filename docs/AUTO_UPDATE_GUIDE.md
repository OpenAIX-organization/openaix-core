# OpenAIX 自动更新方案

## 概述

本方案实现数据的自动更新，无需手动干预。包含三个层面：

1. **GitHub Actions 自动流水线** - 后台自动处理
2. **前端缓存清除机制** - 确保获取最新数据
3. **本地快速更新脚本** - 手动触发

---

## 🔄 方案一：GitHub Actions 自动流水线（推荐）

### 工作原理

```
新评测数据提交 → GitHub Actions触发 → 自动运行standardize_data.py → 
更新rankings_current.json → 自动推送到GitHub Pages
```

### 触发条件

1. **定时触发** - 每天凌晨2点自动运行
2. **文件变更触发** - `data/evaluations/` 目录有新文件时
3. **手动触发** - 在GitHub Actions页面点击"Run workflow"

### 配置文件

`.github/workflows/auto-update.yml`

### 如何启用

1. 确保GitHub仓库已启用Actions
2. 文件已提交到仓库（已提交 ✅）
3. 不需要额外配置，自动生效

---

## 🌐 方案二：前端缓存清除机制

### 已实现功能

1. **时间戳防缓存**
   ```javascript
   const cacheBuster = `?t=${Date.now()}`;
   fetch(`../data/exports/rankings_current.json${cacheBuster}`)
   ```

2. **自动刷新**
   - 每5分钟自动刷新数据
   - 控制台显示更新时间

3. **错误处理和强制刷新**
   - 加载失败显示详细错误信息
   - 提供"强制刷新"按钮

### 验证数据新鲜度

打开浏览器控制台(F12)，查看：
```
📊 Data last updated: 2026/2/25 10:13:32
```

---

## 💻 方案三：本地快速更新脚本

### 使用场景

- 本地开发时快速更新数据
- 手动触发数据重新处理
- 测试数据变更

### 使用方法

```bash
# 方式1：使用脚本
./scripts/update_data.sh

# 方式2：直接运行Python
python3 scripts/data_pipeline/standardize_data.py

# 方式3：一键更新并启动服务器
python3 scripts/data_pipeline/standardize_data.py && python3 -m http.server 8080
```

### 更新后验证

```bash
# 检查数据条数
python3 -c "import json; d=json.load(open('data/exports/rankings_current.json')); print(f'Sites: {len(d[\"sites\"])}')"

# 查看最新更新时间
python3 -c "import json; d=json.load(open('data/exports/rankings_current.json')); print(f'Updated: {d[\"meta\"][\"generated_at\"]}')"
```

---

## 📁 完整工作流程

### 日常使用（自动化）

```
1. 有新的网站评测完成 → 文件自动保存到 data/evaluations/YYYYMMDD/
2. GitHub Actions 检测到变更 → 自动运行 standardize_data.py
3. 生成新的 rankings_current.json → 自动提交并推送
4. 网站自动获取最新数据（通过时间戳防缓存）
```

### 手动更新（开发/测试）

```bash
# 1. 确保在项目根目录
cd /Users/wesley/Desktop/repo/openaix-core

# 2. 运行更新脚本
python3 scripts/data_pipeline/standardize_data.py

# 3. 本地测试
python3 -m http.server 8080

# 4. 访问 http://localhost:8080/website/
```

---

## 🎯 最佳实践

### 1. 本地开发

```bash
# 终端1：监视数据变化并自动更新
watch -n 60 'python3 scripts/data_pipeline/standardize_data.py'

# 终端2：启动开发服务器
python3 -m http.server 8080
```

### 2. 生产部署

```bash
# 确保使用GitHub Pages
# Settings → Pages → Source: Deploy from a branch → Branch: main
# 网站会自动部署，数据会自动更新
```

### 3. 调试缓存问题

```javascript
// 在浏览器控制台运行，清除缓存
localStorage.clear();
sessionStorage.clear();
location.reload(true);
```

---

## 🔧 故障排除

### 问题1：网站显示旧数据

**解决方案：**
1. 强制刷新：`Ctrl + Shift + R` (Windows) 或 `Cmd + Shift + R` (Mac)
2. 清除浏览器缓存
3. 检查控制台是否有更新时间日志

### 问题2：数据加载失败

**检查步骤：**
1. 确认文件存在：`ls data/exports/rankings_current.json`
2. 检查JSON格式：`python3 -c "import json; json.load(open('data/exports/rankings_current.json'))"`
3. 确认服务器从根目录启动：`python3 -m http.server 8080` (在项目根目录)

### 问题3：GitHub Actions不触发

**检查步骤：**
1. 仓库Settings → Actions → General → 确保Actions已启用
2. 检查workflow文件语法
3. 查看Actions日志排查错误

---

## 📊 监控和日志

### GitHub Actions 日志

在GitHub仓库页面：
1. 点击"Actions"标签
2. 查看"Auto Update Rankings"工作流
3. 点击具体运行记录查看日志

### 本地日志

```bash
# 运行脚本时显示详细信息
python3 scripts/data_pipeline/standardize_data.py --verbose

# 查看数据摘要
python3 -c "
import json
d = json.load(open('data/exports/rankings_current.json'))
print(f'Total sites: {len(d[\"sites\"])}')
print(f'Last update: {d[\"meta\"][\"generated_at\"]}')
print(f'Average score: {sum(s[\"score\"] for s in d[\"sites\"])/len(d[\"sites\"]):.1f}')
"
```

---

## 🚀 进阶：实时数据API（可选）

如果需要更实时的数据更新，可以考虑：

1. **使用 GitHub Pages API**
   ```javascript
   // 通过GitHub API获取最新commit时间
   fetch('https://api.github.com/repos/OpenAIX-organization/openaix-core/commits?path=data/exports/rankings_current.json')
   ```

2. **使用第三方实时数据库**
   - Firebase Realtime Database
   - Supabase
   - 直接存储JSON到对象存储（S3/Cloudflare R2）

---

## ✅ 检查清单

部署前确认：

- [ ] `.github/workflows/auto-update.yml` 已提交
- [ ] `scripts/update_data.sh` 可执行 (`chmod +x`)
- [ ] 网站代码包含时间戳防缓存
- [ ] GitHub Pages 已启用
- [ ] Actions 权限已配置

---

**总结**：现在数据更新完全自动化！你只需要添加新的评测文件到 `data/evaluations/`，剩下的交给GitHub Actions处理。网站会自动获取最新数据。🎉
