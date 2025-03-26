# HeroBot Agents

[**HeroBot**](https://herobot.site) is your personal wizard that guides you through the adventurous journey of acquiring new skills. It crafts personalized roadmaps based on your existing knowledge and familiarity with a subject, rather than imposing a one-size-fits-all approach to learning. As your loyal sidekick, HeroBot helps you stay on track with your learning goals, communicating through instant messaging platforms e.g., Telegram. To learn more about the hows (e.g., How does HeroBot help you learn more efficiently?) and whys (e.g., Why do you need yet-another learning tool?), please visit our ["about"](https://herobot.site/about) page. 

![tag : innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)

![https://res.cloudinary.com/dizbsofmd/image/upload/v1742999775/HeroBot_-_Multi-agent_system_gcpkdo.png](https://res.cloudinary.com/dizbsofmd/image/upload/v1742999775/HeroBot_-_Multi-agent_system_gcpkdo.png)

## Agents

Here are the agents that power HeroBot's prototype:

```
HeroBot/ApolloAgent
Named after the Greek God of truth & light, this AI agent helps to evaluate your proficiency on any topic that you've learnt. The best way to really know whether you really know something is 
Address:
Link:

HeroBot/AthenaAgent
Named after the Greek Goddess of knowledge & wisdom, this AI agent helps to answer all your queries & also generates a custom knowledge graph & roadmap for any subject you want to learn.
Address:
Link:

HeroBot/HermesAgent
Named after the Messenger of Greek Gods, this AI agent helps with actively communicating with users regarding their roadmap, etc.
Address:
Link
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
    /index.py                 # SERVER ENTRY POINT
    /scripts                  # DIRECTORY CONTAINING SCRIPTS
        /deploy.sh            # SCRIPT FOR GENERATING ZIP FILE FOR UPLOADING TO AWS LAMBDA FUNCTIONS
    /agents                   # DIRECTORY CONTAINING AGENTS
      /athena_agent.py        # SOURCE CODE FOR AthenaAgent
      /apollo_agent.py        # SOURCE CODE FOR ApolloAgent
      /hermes_agent.py        # SOURCE CODE FOR HermesAgent
    /models                   # DIRECTORY CONTAINING MODELS USED BY THE AGENTS
      /athena_model.py        # MODELS USED BY AthenaAgent
      /apollo_model.py        # MODELS USED BY ApolloAgent
      /hermes_model.py        # MODELS USED BY HermesAgent
    /handlers                 # DIRECTORY CONTAINING HANDLERS USED BY THE AGENTS
      /athena_handlers.py     # METHODS & HANDLERS USED BY AthenaAgent
      /apollo_handlers.py     # METHODS & HANDLERS USED BY ApolloAgent
      /hermes_handlers.py     # METHODS & HANDLERS USED BY HermesAgent
```