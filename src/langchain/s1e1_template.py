import json
from langchain_core.prompts import PromptTemplate

# JsonOutputParser
# CommaSeparatedListOutputParser,
# ListOutputParser,
# MarkdownListOutputParser,
# NumberedListOutputParser,
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnablePassthrough
from typing import List
from chat import get_chat


# Define the output schema using Pydantic
class Poem(BaseModel):
    title: str = Field(description="The title of the poem")
    content: str = Field(description="The full text of the poem")
    form: str = Field(description="The poetic form (sonnet, haiku, free verse, etc.)")
    themes: List[str] = Field(description="Main themes present in the poem")
    analysis: str = Field(description="A brief analysis of the poetic devices used")


# Initialize ChatOpenAI
chat = get_chat(temperature=0.8)

# Create a parser based on the Pydantic model
parser = JsonOutputParser(pydantic_object=Poem)

# Create a prompt template
template = """
You are a skilled poet. Create a poem based on the following parameters:

Topic: {topic}
Mood: {mood}
Style: {style}
Length: {length} lines

Your response should be in the following JSON format:
{format_instructions}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["topic", "mood", "style", "length"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Create the chain
poetry_chain = (
    {
        "topic": RunnablePassthrough(),
        "mood": RunnablePassthrough(),
        "style": RunnablePassthrough(),
        "length": RunnablePassthrough(),
    }
    | prompt
    | chat
    | parser
)

# Test the chain
if __name__ == "__main__":
    poetry_requests = [
        {
            "topic": "machine learning",
            "mood": "contemplative",
            "style": "sonnet",
            "length": "1",
        },
        {
            "topic": "data science",
            "mood": "humorous",
            "style": "limerick",
            "length": "1",
        },
    ]

    for req in poetry_requests:
        print(f"\nGenerating poem about: {req['topic']} in {req['style']} form")
        result = poetry_chain.invoke(req)

        # Print the poem
        print(f"\n{'-'*40}")
        print(f"Title: {result.title}")
        print(f"{'-'*40}")
        print(result.content)
        print(f"{'-'*40}")
        print(f"Form: {result.form}")
        print(f"Themes: {', '.join(result.themes)}")
        print(f"Analysis: {result.analysis}")

        # Save the poem to a file
        filename = f"{req['topic'].replace(' ', '_')}_{req['style']}.json"
        with open(filename, "w") as f:
            f.write(json.dumps(result.dict(), indent=2))
