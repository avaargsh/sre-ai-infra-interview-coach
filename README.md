# SRE & AI Infrastructure Interview Coach

[![Validate Skill](https://github.com/avaargsh/sre-ai-infra-interview-coach/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/avaargsh/sre-ai-infra-interview-coach/actions/workflows/validate.yml)

一个基于开放 Agent Skills 格式的场景化面试教练，帮助用户练习资深 SRE、Platform Engineering 与 AI Infrastructure 生产故障分析。每轮先独立作答，再按照公开评分标准评估、核验技术细节，并继续一道不同机制的新题。

**目标是训练证据链、风险控制和恢复验收，而不是背答案。**

## 能力

- 每轮一道 5–10 分钟场景题：有架构、症状、指标、时间窗口与操作约束。
- 初始只出题，不泄露根因、提示或答案。
- 作答后按 10 分制评价五个维度，区分事实错误、未证实假设和遗漏。
- 领域覆盖 Linux/kernel、TCP/DNS/TLS、Kubernetes/容器运行时、SLO/可观测性、Go、数据库/缓存/队列、发布/安全/DR、GPU、LLM 推理、RDMA/NCCL 和 Agent Runtime/Control Plane。
- 提供近期主题记录，减少重复题，并支持复制进度到新对话。

所有事故指标均为训练用的虚构示例，除非明确引用真实来源。本项目不需要 API Key、MCP 或运行时网络访问。

## 安装

### ChatGPT

从 [GitHub Releases](https://github.com/avaargsh/sre-ai-infra-interview-coach/releases) 下载 Skill ZIP。在支持 Skills 的 ChatGPT 入口中，打开 Plugins → Skills → Create → Upload from your computer，按界面提示上传。功能可用性取决于产品、账号与工作区策略，参见 [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)。

如果没有 Skill 安装入口，复制 QUICKSTART.md 中的提示词到普通 ChatGPT 对话即可练习；这属于提示词启动，不等同于安装 Skill。

首次正式 Release 发布前，也可在 [Actions → Validate Skill](https://github.com/avaargsh/sre-ai-infra-interview-coach/actions/workflows/validate.yml) 最新成功的 main 分支运行中下载 Skill package artifact（临时构建产物保留 14 天）；稳定分发请使用 Releases 中的版本化 ZIP。

### Codex 和兼容 Agent Skills 的工具

本项目使用 SKILL.md 目录结构。请参考所用工具的最新官方安装说明，将整个目录安装至其用户级或仓库级 Skills 路径。OpenAI 指南：[Build skills](https://learn.chatgpt.com/docs/build-skills)。

## 使用方式

- 开始：开始今天的资深 SRE / AI Infrastructure 场景面试题，只给题目。
- 继续：评估上一题，然后给一道不同领域的新题。
- 仅评估：只评分，不继续出题。
- 恢复进度：粘贴 references/progress-template.md 的进度记录。

标准作答格式：假设 → 验证 → 判断标准 → 止血 → 验收。

## 开发与验证

需要 Python 3，无第三方 Python 依赖：

    python tests/validate_skill.py
    python tests/check_references.py
    python scripts/package_skill.py

打包输出为 dist/sre-ai-infra-interview-coach-skill.zip。发布流程见 [docs/RELEASING.md](docs/RELEASING.md)。正式发布：打开 GitHub **Actions → Build Skill Release → Run workflow**，选 `main` 并输入版本号（如 `v0.1.0`），工作流会校验、打包并创建 GitHub Release。

## 质量原则

- 单题聚焦一个主故障机制，包含 3–4 个递进问题。
- 不以换产品名的方式重复同一根因。
- 先读后改，明确风险范围、回滚条件和验收标准。
- 指标和命令存在版本差异时要注明边界。
- 新对话不能假设自动记得其他对话的历史；使用进度记录续练。

欢迎提交场景与文档改进，详见 CONTRIBUTING.md。安全报告流程见 SECURITY.md。

## License

MIT，见 LICENSE。
