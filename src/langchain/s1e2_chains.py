import json
from typing import List, Dict
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from chat import get_chat


# Define structured output schemas
class PoemAnalysis(BaseModel):
    themes: List[str] | None = Field(description="Main themes in the poem")
    devices: List[str] | None = Field(description="Poetic devices used with examples")
    tone: str | None = Field(description="Overall tone of the poem")
    interpretation: str | None = Field(description="Brief interpretation of meaning")


class PoemComparison(BaseModel):
    similarities: List[str] = Field(description="Thematic and stylistic similarities")
    differences: List[str] = Field(
        description="Key differences in approach and execution"
    )
    stronger_elements: List[str] = Field(
        description="Which poem is stronger in different aspects"
    )
    recommendation: List[str] = Field(
        description="Which poem might appeal to different readers"
    )


# Initialize ChatOpenAI
chat = get_chat()

# Create analyzers and parsers
analysis_parser = JsonOutputParser(pydantic_object=PoemAnalysis)
comparison_parser = JsonOutputParser(pydantic_object=PoemComparison)

# Create prompt templates
analysis_template = """
Analyze the following poem in detail:

POEM:
{poem}

{format_instructions}
"""

analysis_prompt = PromptTemplate(
    template=analysis_template,
    input_variables=["poem"],
    partial_variables={
        "format_instructions": analysis_parser.get_format_instructions()
    },
)

comparison_template = """
Compare and contrast the following two poems:

POEM 1 (TITLE: {title1}):
{poem1}

POEM 2 (TITLE: {title2}):
{poem2}

ANALYSIS OF POEM 1:
{analysis1}

ANALYSIS OF POEM 2:
{analysis2}

{format_instructions}
"""

comparison_prompt = PromptTemplate(
    template=comparison_template,
    input_variables=["title1", "poem1", "analysis1", "title2", "poem2", "analysis2"],
    partial_variables={
        "format_instructions": comparison_parser.get_format_instructions()
    },
)

# Build Runnable chains
# poem_analysis_chain = RunnableSequence(analysis_prompt, chat, analysis_parser)
poem_analysis_chain = analysis_prompt | chat | analysis_parser

# poem_comparison_chain = RunnableSequence(comparison_prompt, chat, comparison_parser)
poem_comparison_chain = comparison_prompt | chat | comparison_parser

# Main script
if __name__ == "__main__":
    poems = {
        "Sonnet": {
            "title": "Shall I compare thee to a summer's day?",
            "text": """Shall I compare thee to a summer's day?
                    Thou art more lovely and more temperate:
                    Rough winds do shake the darling buds of May,
                    And summer's lease hath all too short a date;
                    Sometime too hot the eye of heaven shines,
                    And often is his gold complexion dimm'd;
                    And every fair from fair sometime declines,
                    By chance or nature's changing course untrimm'd;
                    But thy eternal summer shall not fade,
                    Nor lose possession of that fair thou ow'st;
                    Nor shall death brag thou wander'st in his shade,
                    When in eternal lines to time thou grow'st:
                    So long as men can breathe or eyes can see,
                    So long lives this, and this gives life to thee.""",
        },
        "Haiku": {
            "title": "Candle",
            "text": """The light of a candle
                    Is transferred to another candle
                    spring twilight.""",
        },
    }

    # Run analysis
    parsed_analysis1 = poem_analysis_chain.invoke({"poem": poems["Sonnet"]["text"]})
    parsed_analysis2 = poem_analysis_chain.invoke({"poem": poems["Haiku"]["text"]})

    # Run comparison
    parsed_comparison = poem_comparison_chain.invoke(
        {
            "title1": poems["Sonnet"]["title"],
            "poem1": poems["Sonnet"]["text"],
            # "analysis1": parsed_analysis1.model_dump_json(),
            "analysis1": json.dumps(parsed_analysis1),
            "title2": poems["Haiku"]["title"],
            "poem2": poems["Haiku"]["text"],
            # "analysis2": parsed_analysis2.model_dump_json(),
            "analysis2": json.dumps(parsed_analysis2),
        }
    )

    # Output results
    print("Poetry Analysis Complete!\n")
    print("Analysis of Sonnet:")
    # print(parsed_analysis1.model_dump_json(indent=2))
    analysis1 = json.dumps(parsed_analysis1, indent=2)
    print(analysis1)

    print("\nAnalysis of Haiku:")
    # print(parsed_analysis2.model_dump_json(indent=2))
    analysis2 = json.dumps(parsed_analysis2, indent=2)
    print(analysis2)

    print("\nComparison:")
    # print(parsed_comparison.model_dump_json(indent=2))
    # comparison = json.dumps(parsed_comparison, indent=2)
    print(json.dumps(parsed_comparison, indent=2))
    comparison = PoemComparison(**parsed_comparison)
    # print(comparison)

    # Save results
    with open("poetry_analysis_results.json", "w") as f:
        json.dump(
            {
                "sonnet_analysis": analysis1,
                "haiku_analysis": analysis2,
                "comparison": comparison.model_dump(),
            },
            f,
            indent=2,
        )
