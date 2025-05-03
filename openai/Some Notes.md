Minimal terminology:

**Agents** which are LLMs equipped with instructions and tools.

**Handoffs** which allow agents to delegate to other agents for specific tasks.

**Guardrails** which enable the inputs to agents to be validated.

Three steps to use agents:

1. Create an instance of **Agent**

2. Use **with_trace()** to track the agent.

3. Call **runner.run()** to run the agent.

