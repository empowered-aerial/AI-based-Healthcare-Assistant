from backend import GraphRetriever
from backend import VectorDebriefer

def main():
    API_KEY = "AIzaSyDmkAjMGxsSd8RnY0mrllhiCfYoktaTzLk"

    GRAPH_PROMPT_PATH = "prompts/graph_retrieval.txt"
    STEPBACK_PROMPT_PATH = "prompts/stepback_questioner.txt"
    SUMMARIZER_PATH = "prompts/final_content.txt"

    graph = GraphRetriever(
        api_key=API_KEY,
        prompt_path=GRAPH_PROMPT_PATH
    )

    vector = VectorDebriefer(
        api_key=API_KEY,
        stepback_prompt_path=STEPBACK_PROMPT_PATH,
        final_answer_prompt_path=SUMMARIZER_PATH
    )

    print("Hybrid Graph + Vector RAG Ready (type 'exit' to quit)\n")

    while True:
        query = input("Enter query: ")

        if query.lower() == "exit":
            break

        # Step 1: Graph Retrieval
        graph_result = graph.get_context(query)

        print("\n🧠 Generated Cypher:")
        print(graph_result.get("cypher", "N/A"))

        print("\n📊 Graph Results:")
        for r in graph_result.get("data", []):
            print(r)

        print("\n" + "-"*50)

        # Step 2: Vector RAG Pipeline
        final_answer = vector.user_output(graph_result)

        # Step 3: Final Output
        print("\n🚀 Final Answer:")
        print(final_answer)

        print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()