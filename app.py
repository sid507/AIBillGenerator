from fastapi import FastAPI
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder

app = FastAPI()


class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        # Assuming request is a pydantic object like: {"question": "your text"}
        messages = {"messages": [query.question]}

        output = react_app.invoke(messages)

        # If result is dict with messages:
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Last AI response
        else:
            final_output = str(output)

        return {"answer": final_output}
    except Exception as e:
        return {"error": str(e)}