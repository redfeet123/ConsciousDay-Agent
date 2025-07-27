import os
from langchain_together import Together
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

PROMPT_TEMPLATE = """
You are a daily reflection and planning assistant. Your job is to:

1. Reflect on the user's journal and dream.
2. Interpret emotional and mental state.
3. Understand intention and top 3 priorities.
4. Generate a practical and aligned day strategy.

INPUT:
Morning Journal: {journal}
Dream: {dream}
Intention: {intention}
Top 3 Priorities: {priorities}

Respond with:
1. Inner Reflection Summary
2. Dream Interpretation
3. Energy/Mindset Insight
4. Suggested Day Strategy (time-aligned tasks)
"""

def run_agent(journal, intention, dream, priorities):
    llm = Together(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        api_key=os.getenv("TOGETHER_API_KEY"),
        temperature=0.5,
        max_tokens=1200,
    )

    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    final_prompt = prompt.format(
        journal=journal,
        dream=dream,
        intention=intention,
        priorities=priorities
    )

    output = llm.invoke(final_prompt)
    return StrOutputParser().invoke(output)
