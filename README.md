# AI Agent Marketplace

[![PyPI](https://img.shields.io/pypi/v/ai-agent-marketplace)](https://pypi.org/project/ai-agent-marketplace/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

Official repository for the [DeepNLP AI Agent Marketplace](https://www.deepnlp.org/store/ai-agent) — a public registry and search index of 10,000+ AI agents across 30+ categories, including autonomous agents, chatbots, MCP servers, skills, CLIs, and industry-specific tools.

| Resource | Link |
|----------|------|
| Marketplace | [deepnlp.org/store/ai-agent](https://www.deepnlp.org/store/ai-agent) |
| PyPI Package | [ai-agent-marketplace](https://pypi.org/project/ai-agent-marketplace/) |
| HuggingFace Dataset | [AI-Agent-Marketplace-Index](https://huggingface.co/datasets/DeepNLP/AI-Agent-Marketplace-Index) |
| CLI (agtm) | [github.com/aiagenta2z/agtm](https://github.com/aiagenta2z/agtm) |
| OneKey Gateway | [github.com/aiagenta2z/onekey-gateway](https://github.com/aiagenta2z/onekey-gateway) |

---

## Features

- **Agent Registry** — Submit agent metadata via website, CLI (`agtm`), or Python SDK
- **Search Engine & API** — Discover agents by keyword with ranking and traffic data
- **A2Z Middleware** — Deploy Python/Node agents with free `*.aiagenta2z.com` subdomains
- **OneKey Gateway** — Single access key for 30+ commercial API categories
- **Domain Verification** — Subdomain verification for ChatGPT Apps, MCP, WeChat, DingTalk, and more
- **Monetization** — Stripe, Alipay, and credit-based billing for agent APIs
- **Research Dataset** — Periodic snapshots on HuggingFace for tracking marketplace growth

---

## Project Structure

```
ai-agent-marketplace/
├── AGENT.md                          # Community agent directory (10K+ listings)
├── CONTRIBUTING.md                   # Guidelines for adding agents to AGENT.md
├── LICENSE                           # MIT license
├── README.md
├── pyproject.toml                    # Modern Python packaging config
├── setup.py                          # Setuptools entry point
├── requirements.txt
│
├── docs/
│   └── api/
│       ├── registry.md               # Agent registration guide
│       └── search.md                 # Search API guide
│
├── examples/
│   ├── agent.json                    # Sample agent registration (JSON)
│   └── agent.yaml                    # Sample agent registration (YAML)
│
└── src/
    └── ai_agent_marketplace/         # Python package
        ├── __init__.py               # Public API: search(), add()
        ├── __version__.py
        ├── constants.py              # API endpoints and defaults
        ├── base.py                   # Backward-compatible re-exports
        ├── utils.py                  # Backward-compatible re-exports
        │
        ├── client/                   # HTTP API clients
        │   ├── base.py               # BaseAPI class
        │   ├── search.py             # SearchFunctionAPI
        │   ├── registry.py           # AddServiceAPI
        │   └── mock.py               # Offline demo data loader
        │
        ├── utils/                    # Helper utilities
        │   └── schema.py             # Function-to-tool-schema converters
        │
        └── data/                     # Bundled mock API responses
            ├── search_api_demo.json
            └── add_service_api_demo.json
```

---

## Installation

```bash
pip install ai-agent-marketplace
```

Or install from source:

```bash
git clone https://github.com/aiagenta2z/ai-agent-marketplace.git
cd ai-agent-marketplace
pip install -e .
```

---

## Quick Start

### Search Agents

```python
import ai_agent_marketplace as aa

# Search the marketplace
result = aa.search(q="coding agent", limit=20, timeout=5)
print(result)

# Empty query returns bundled demo data (offline)
demo = aa.search(q="")
```

### Register an Agent

Get your API key at [Marketplace API Keys](https://www.deepnlp.org/workspace/keys).

```python
import ai_agent_marketplace as aa

result = aa.add(
    access_key="your_access_key",
    name="My First AI Agent",
    item_info={
        "content": "An AI agent that helps with programming tasks",
        "website": "https://www.example.com",
        "field": "AI AGENT",
        "subfield": "Coding Agent",
        "content_tag_list": "coding,python",
        "github": "https://github.com/your-org/your-agent",
    },
)

print(result.get("url"))
```

See [docs/api/registry.md](docs/api/registry.md) and [docs/api/search.md](docs/api/search.md) for full API documentation.

---

## CLI Usage (agtm)

Install the CLI via pip or npm:

```bash
pip install agtm
# or
npm install -g @aiagenta2z/agtm
```

```bash
export AI_AGENT_MARKETPLACE_ACCESS_KEY="your_access_key"

# Register from GitHub repo
agtm upload --github https://github.com/your-org/your-agent

# Register from config file
agtm upload --config ./examples/agent.json

# Search
agtm search --q "coding agent"
agtm search --id "google-maps/google-maps"
```

---

## Deployment & Live URLs

Deploy Python or Node.js agents and get a free subdomain at `*.aiagenta2z.com`.

| Live URL | Description |
|----------|-------------|
| [derekzz.aiagenta2z.com/fortune-compass-agent/mcp](https://derekzz.aiagenta2z.com/fortune-compass-agent/mcp) | Fortune Telling ChatGPT App |
| [jjjmc.aiagenta2z.com/perplexity_agent/mcp](https://jjjmc.aiagenta2z.com/perplexity_agent/mcp) | Perplexity Deep Research Agent |
| [agent.deepnlp.org/agent/craftsman-agent](https://agent.deepnlp.org/agent/craftsman-agent/craftsman-agent) | Craftsman 3D Build Generator |

[Deployment docs](https://deepnlp.org/doc/agent_mcp_deployment) | [Deployment workspace](https://www.deepnlp.org/workspace/deploy)

---

## OneKey Gateway

Route requests to 30+ commercial API categories with a single access key:

```bash
npx onekey agent google-maps/google-maps maps_search_places '{"query":"New York City Italian Restaurants"}'
npx onekey mcp <server_name> [--name config_name]
npx onekey llm --provider <provider> --model <model> --messages <json|@file>
```

[OneKey Gateway docs](https://deepnlp.org/doc/onekey_gateway) | [Supported APIs](https://github.com/aiagenta2z/onekey-gateway)

---

## Domain Verification

Verify subdomain ownership for platform integrations:

| Platform | Verification URL |
|----------|-----------------|
| ChatGPT App Store | `https://{username}.aiagenta2z.com/.well-known/openai-apps-challenge` |
| MCP Official Registry | `https://{username}.aiagenta2z.com/.well-known/mcp-register-challenge` |
| WeCom (Tencent) | `https://{username}.aiagenta2z.com/WW_verify_xxxxxx.txt` |
| WeChat | `https://{username}.aiagenta2z.com/MP_verify_xxxxxx.txt` |
| DingTalk | `https://{username}.aiagenta2z.com/verify_xxxxxx.txt` |

Manage verification at the [Deployment Workspace](https://deepnlp.org/workspace/deploy).

---

## Agent Directory

Browse the community-curated agent directory:

- [Full Agent Collection](./AGENT.md)
- [Email Writing Agents](./AGENT.md#email-writing-ai-agent)
- [Benchmark Agents](./AGENT.md#benchmark-ai-agent)

---

## Contributing

Contributions to [AGENT.md](./AGENT.md) are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the PR format and submission guidelines.

You can also register agents via:
- [Web submission](https://www.deepnlp.org/workspace/my_ai_services)
- [`agtm` CLI](https://github.com/aiagenta2z/agtm)
- Python SDK (`aa.add()`)

---

## News

1. **[OneKey Gateway](https://github.com/aiagenta2z/onekey-gateway)** — Register APIs and distribute as CLIs, MCPs, and Skills 10x faster via [`agtm`](https://github.com/aiagenta2z/agtm).
2. **[Agent & MCP Deployment Pipeline](https://github.com/aiagenta2z/agent-mcp-deployment-templates)** — Deploy agents with free `*.aiagenta2z.com` subdomains. [Docs](https://www.deepnlp.org/doc/agent_mcp_deployment) | [Workspace](https://www.deepnlp.org/workspace/deploy).

---

## License

This project is licensed under the [MIT License](LICENSE).
