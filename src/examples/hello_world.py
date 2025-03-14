from agents import Agent, Runner

# エージェントを作成
agent = Agent(name="Assistant", instructions="You are a helpful assistant")

# エージェントを実行
result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")

# 結果を出力
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
