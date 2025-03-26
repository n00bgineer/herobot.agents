# HeroBot Agents

[**HeroBot**](https://herobot.site) is your personal AI learning wizard that guides you through the adventurous journey of acquiring new skills. It crafts personalized roadmaps based on your existing knowledge and familiarity with a subject, rather than imposing a one-size-fits-all approach to learning. As your loyal sidekick, HeroBot helps you stay on track with your learning goals, communicating through instant messaging platforms e.g., Telegram. To learn more about the hows (e.g., How does HeroBot help you learn more efficiently?) and whys (e.g., Why do you need yet-another learning tool?), please visit our ["about"](https://herobot.site/about) page. 

![tag : innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)

![https://res.cloudinary.com/dizbsofmd/image/upload/v1742999775/HeroBot_-_Multi-agent_system_gcpkdo.png](https://res.cloudinary.com/dizbsofmd/image/upload/v1742999775/HeroBot_-_Multi-agent_system_gcpkdo.png)

## Agents

Here are the agents that power HeroBot's prototype:

```
Name: ApolloAgent
Description: Named after the Greek God of truth & light, this AI agent helps to evaluate your proficiency on any topic that you've learnt. The best way to really know whether you really know something is 
Address:
Link:

Name: AthenaAgent
Description: Named after the Greek Goddess of knowledge & wisdom, this AI agent helps to answer all your queries & also generates a custom knowledge graph & roadmap for any subject you want to learn.
Address:
Link:

Name: HermesAgent
Description: Named after the Messenger of Greek Gods, this AI agent helps with actively communicating with users regarding their roadmap, etc.
Address:
Link
```

## Authorization

Since every agent in HeroBot is actively interacting with resources such as language model inference endpoints, databases, etc, so it raises the need of being able to monitor, authorize and ratelimit the usage of agents & to achieve this, HeroBot uses authorization tokens. 

To programmatically access and use HeroBot agents, follow through these steps: 
1. Register with [HeroBot](https://herobot.site).
2. Visit [this page](https://herobot.site/tokens) to generate an authorization token.
2. Click on `Add token` button, which will allow you to generate new tokens.
3. Please copy the token & add it to the message body, without which the request would fail:
```
{
  token: <TOKEN_VALUE>, // Authorization token
  ...                   // Other parts of message body
}
```
**Note:** If you're accessing these agents from the application, then you don't need to generate the token. 

## Usage

### **AthenaAgent**
```
WIP
```

### **ApolloAgent**
```
WIP
```

### **HermesAgent**
```
WIP
```

## Installation & Usage

HeroBot agents use Python **3.12+** & [`poetry`](https://python-poetry.org/docs/#installation) for dependency management. You can install the relevant dependencies using the following command: 

```
poetry install
```

## Directory Structure

The following is the directory structure of the HeroBot agents:

```
/
    /index.py                 # Server entry point

    /scripts                  # Directory containing scripts
        /deploy.sh            # Script for generating zip file for uploading to AWS Lambda functions

    /agents                   # Directory containing agents
      /athena_agent.py        # Source code for AthenaAgent
      /apollo_agent.py        # Source code for ApolloAgent
      /hermes_agent.py        # Source code for HermesAgent

    /models                   # Directory containing models used by the agents
      /athena_model.py        # Models used by AthenaAgent
      /apollo_model.py        # Models used by ApolloAgent
      /hermes_model.py        # Models used by HermesAgent

    /handlers                 # Directory containing handlers used by the agents
      /athena_handlers.py     # Methods & handlers used by AthenaAgent
      /apollo_handlers.py     # Methods & handlers used by ApolloAgent
      /hermes_handlers.py     # Methods & handlers used by HermesAgent
```