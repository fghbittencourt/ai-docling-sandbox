from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from chat import get_chat


def main():
    # Initialize ChatOpenAI
    llm = get_chat()

    # 1. Prompt Templates
    prompt = PromptTemplate.from_template(
        "Write a {tone} poem about {topic} in the style of {poet}."
    )

    # Formatting a prompt
    formatted_prompt = prompt.format(
        tone="melancholic", topic="artificial intelligence", poet="Edgar Allan Poe"
    )
    print("Formatted Prompt:")
    print(formatted_prompt)

    # 2. Output Parsers
    output_parser = StrOutputParser()

    # 3. Chains
    # A simple chain: prompt -> llm(chat) -> output_parser
    chain = (
        {
            "tone": RunnablePassthrough(),
            "topic": RunnablePassthrough(),
            "poet": RunnablePassthrough(),
        }
        | prompt
        | llm
        | output_parser
    )

    # Run the chain
    result = chain.invoke(
        {
            "tone": "melancholic",
            "topic": "artificial intelligence",
            "poet": "Edgar Allan Poe",
        }
    )
    print("\nChain Result:")
    print(result)


if __name__ == "__main__":
    main()
